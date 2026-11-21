"""Release zips and release notes. One zip per pool, plus one zip with every pool.

Zips use a fixed date and a fixed file order, so the same input always gives the same
SHA-256."""
import hashlib
import os
import zipfile

REPO = "https://github.com/Miabeyefendi/Squad-MapPool"
VERSION = "v1.0.0"
STAMP = (2026, 11, 21, 0, 0, 0)

# key -> (zip name, what it does, good for)
INFO = {
    "03-day-night": ("Recommended-Day-Evening", "Narva and Gorodok in the day, Mutaha, Fallujah and Yehorivka in the evening. All other maps all day.",
                     "Most servers. Every big map every day, but they don't follow each other."),
    "01-weekly-plan-4w": ("Weekly-4-Weeks", "One big map per week, all other maps every week. Swap the file every week.",
                          "Servers that want the most variety and can change a file once a week."),
    "02-weekly-plan-5w": ("Weekly-5-Weeks", "Same as Weekly-4-Weeks, but Gorodok and Yehorivka get their own week.",
                          "Same as above, one more week in the cycle."),
    "04-all-best": ("All-Maps-Best", "Every map with its most played RAAS and Invasion layer.",
                    "A clean all-maps pool without the weak layer versions."),
    "05-raas-best": ("Only-RAAS", "Most played RAAS layer of every map. No Invasion.", "RAAS only servers."),
    "06-invasion-best": ("Only-Invasion", "Most played Invasion layer of every map. No RAAS.", "Invasion nights or Invasion servers."),
    "07-size-large": ("Big-Maps", "Only maps of 4 km and more (Gorodok, Black Coast, Yehorivka, Skorpo and more).",
                      "Vehicle heavy servers and long rounds."),
    "08-size-medium": ("Medium-Maps", "Only Narva, Mutaha, Fallujah and Anvil. 4 vote options.", "Events. Too few maps for every day."),
    "09-size-small": ("Small-Maps", "Only Sumari, Logar, Fools Road, Mestia and Kokan. 4 vote options.",
                      "Infantry events. Too few maps for every day."),
    "13-seed-low-players": ("Seed-Low-Players", "Small, fast RAAS maps while the server fills up (LayerVotingLowPlayers.cfg).",
                            "Add this to any other pool for seeding."),
    "14-biome-balanced": ("Biome-Balanced", "Desert and forest maps about half and half.", "Servers that want less forest in a row."),
    "15-rising": ("Rising-Maps", "More layers for maps that grew lately (Gorodok, Yehorivka, Black Coast, Al Basrah, Manicouagan, Kohat).",
                  "Servers that want the reworked maps more often."),
    "16-discovery": ("Discovery", "The less played half of the maps with all their layers, popular maps with one layer.",
                     "Servers that want to bring back forgotten maps."),
    "00-today": ("Default-All-Layers", "Every RAAS and Invasion layer, like a default vote server. The baseline.",
                 "Comparison, or going back to default."),
}
FAMILY = {
    "10-cycle-variety-": ("Variety-{n}-Weeks", "The 9 most played maps are spread over {n} weeks, small maps every week.",
                          "Weekly rotation with less repeat of the big maps."),
    "11-cycle-favorites-": ("Favorites-{n}-Weeks", "The 9 most played maps every week, small maps spread over {n} weeks.",
                            "Servers that never want to drop a popular map."),
    "12-cycle-low-variety-": ("Low-Variety-{n}-Weeks", "Only 8 maps per week, Narva, Mutaha and Fallujah always in.",
                              "Test only. Shows what a too small pool does."),
}
GROUPS = [("Not sure? Take this one", ["03-day-night"]),
          ("Weekly plans", ["01-weekly-plan-4w", "02-weekly-plan-5w"]),
          ("One pool, no file swap", ["04-all-best", "05-raas-best", "06-invasion-best", "14-biome-balanced",
                                      "15-rising", "16-discovery", "00-today"]),
          ("By map size", ["07-size-large", "08-size-medium", "09-size-small"]),
          ("Seeding", ["13-seed-low-players"]),
          ("Weekly cycles, variety", [f"10-cycle-variety-{n}w" for n in range(2, 8)]),
          ("Weekly cycles, favorites", [f"11-cycle-favorites-{n}w" for n in range(2, 8)]),
          ("Weekly cycles, low variety", [f"12-cycle-low-variety-{n}w" for n in range(2, 8)])]


def info(key):
    if key in INFO:
        return INFO[key]
    for prefix, (name, what, who) in FAMILY.items():
        if key.startswith(prefix):
            n = key[len(prefix):-1]
            return name.format(n=n), what.format(n=n), who
    raise KeyError(key)


def howto(p, res):
    name, what, who = info(p.key)
    weekly = any(k.startswith("week-") for k in p.files)
    files = sorted(p.files)
    lines = [name, "=" * len(name), "", what, "Good for: " + who, "", "INSTALL", ""]
    lines.append("1. ServerConfig/Server.cfg must have: MapRotationMode=LayerList_Vote and UseVoteLayer=true")
    if weekly:
        lines.append("2. Copy Week-1/LayerVoting.cfg into ServerConfig/ (keep a backup of your old file).")
    else:
        names = ", ".join(os.path.basename(f) for f in files)
        lines.append(f"2. Copy {names} into ServerConfig/ (keep a backup of your old files).")
    lines += ["3. Open ServerConfig/VoteConfig.cfg and set the keys from VoteConfig-lines.cfg.",
              "   Keys that are not in VoteConfig-lines.cfg stay as they are.",
              "4. Restart the server."]
    if weekly:
        lines += ["5. Every week, at the restart, copy the next week's LayerVoting.cfg.",
                  "   After the last week, start again with Week-1."]
    if "LayerVotingNight.cfg" in p.files:
        lines += ["", "NightTime in VoteConfig-lines.cfg is an example (19:00-06:00, server time).",
                  "Set it so the day and the evening have about the same number of full rounds."]
    if "LayerVotingLowPlayers.cfg" in p.files:
        lines += ["", "LayerVotingLowPlayers.cfg is used while the player count is low.",
                  "Use it together with any other pool."]
    r = res[p.key]
    lines += ["", "SIMULATION (model, not tested on a live server)", "",
              f"Narva/Mutaha/Fallujah share of rounds: {r['top3']:.0f}% (default server: {res['00-today']['top3']:.0f}%)",
              f"One of them again within 3 rounds:     {r['top3_in3']:.0f}% (default server: {res['00-today']['top3_in3']:.0f}%)",
              f"Different maps per day (12 rounds):    {r['maps_day']:.1f} (default server: {res['00-today']['maps_day']:.1f})",
              "", "More: " + REPO, ""]
    return "\r\n".join(lines)


def add(z, arc, data):
    zi = zipfile.ZipInfo(arc, STAMP)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    z.writestr(zi, data)


def pool_entries(p, pool_dir, res, prefix=""):
    out = [(prefix + "HOW-TO-INSTALL.txt", howto(p, res).encode("utf-8"))]
    src = os.path.join(pool_dir, p.key)
    for rel in sorted(p.files):
        arc = rel.replace("week-", "Week-")
        with open(os.path.join(src, rel), "rb") as f:
            out.append((prefix + arc, f.read()))
    with open(os.path.join(src, "VoteConfig.cfg"), "rb") as f:
        out.append((prefix + "VoteConfig-lines.cfg", f.read()))
    return out


def build_zips(pools, pool_dir, out_dir, res):
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if f.endswith(".zip"):
            os.remove(os.path.join(out_dir, f))
    sums = {}
    every = []
    for p in pools:
        name = info(p.key)[0]
        entries = pool_entries(p, pool_dir, res)
        every += pool_entries(p, pool_dir, res, prefix=name + "/")
        sums[name + ".zip"] = write_zip(os.path.join(out_dir, name + ".zip"), entries)
    sums["All-Pools.zip"] = write_zip(os.path.join(out_dir, "All-Pools.zip"), every)
    return sums


def write_zip(path, entries):
    with zipfile.ZipFile(path, "w") as z:
        for arc, data in entries:
            add(z, arc, data)
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def notes(pools, res):
    by_key = {p.key: p for p in pools}
    base = res["00-today"]
    url = f"{REPO}/releases/download/{VERSION}/"
    out = ["Vote pool configs for Squad servers. Pick one zip, download it, and follow `HOW-TO-INSTALL.txt` inside. "
           "Every zip has the cfg files, the VoteConfig lines and the install steps.", "",
           f"**Big 3** = Narva, Mutaha, Fallujah. On a default vote server they are {base['top3']:.0f}% of all rounds, "
           f"and after one of them, another one comes back within 3 rounds {base['top3_in3']:.0f}% of the time. "
           "Lower is more variety. The numbers come from a simulation, not from a live server.", ""]
    for title, keys in GROUPS:
        out += [f"### {title}", "", "| Download | What it does | Good for | Big 3 share | Big 3 back within 3 rounds |",
                "|---|---|---|---|---|"]
        for k in keys:
            name, what, who = info(k)
            r = res[by_key[k].key]
            out.append(f"| [**{name}**]({url}{name}.zip) | {what} | {who} | {r['top3']:.0f}% | {r['top3_in3']:.0f}% |")
        out.append("")
    out += ["### Everything", "", f"[**All-Pools.zip**]({url}All-Pools.zip): every pool above in one file.", "",
            "No AAS layers in any pool. Reroll stays on in every pool. "
            f"SHA-256 values and the full results are in the [README]({REPO}#download).", ""]
    return "\n".join(out)


def readme_block(sums):
    rows = "\n".join(f"| `{n}` | `{h}` |" for n, h in sorted(sums.items()))
    return "\n".join([
        f"Every pool is a separate zip on the [release page]({REPO}/releases/latest). Not sure which one? "
        "Take **Recommended-Day-Evening.zip**. Each zip has the cfg files, the VoteConfig lines and a "
        "`HOW-TO-INSTALL.txt`.", "",
        "The zips only hold text files (cfg and txt). They are made by `python src/main.py`, which writes "
        "them to `releases/` with a fixed date and file order, so you can build them yourself and compare the SHA-256.", "",
        "<details><summary>SHA-256 of every zip</summary>", "", "| File | SHA-256 |", "|---|---|", rows, "", "</details>"])
