"""Pool definitions. Every pool is built from the data in src/assets, so the cfg files
and the simulation always use the same layer lists."""
from .model import (LAYERS, LAYER_B, MAP_A, MAP_B, MAPS, TOP3, TOP5, BIOME, Settings,
                    size_class, WEEK, DAY)

INF = 10 ** 9
TOP5_ORDER = MAPS[:5]
MID4 = MAPS[5:9]
REST = MAPS[9:]

# Curated layer set for every map that is not in the top 5. Picked by play count in the
# last 3 months: the RAAS versions people play and the Invasion version people play.
# Anvil: RAAS v2 only. AlBasrah RAAS v3 is never played and stays out.
CURATED = {
    "AlBasrah": ["AlBasrah_RAAS_v1", "AlBasrah_RAAS_v2", "AlBasrah_Invasion_v1"],
    "Anvil": ["Anvil_RAAS_v2"],
    "BlackCoast": ["BlackCoast_RAAS_v1", "BlackCoast_RAAS_v2", "BlackCoast_Invasion_v2"],
    "Chora": ["Chora_RAAS_v1"],
    "FoolsRoad": ["FoolsRoad_RAAS_v1"],
    "GooseBay": ["GooseBay_RAAS_v1", "GooseBay_RAAS_v2", "GooseBay_Invasion_v1"],
    "Harju": ["Harju_RAAS_v1", "Harju_RAAS_v2", "Harju_Invasion_v1"],
    "Kamdesh": ["Kamdesh_RAAS_v1"],
    "Kohat": ["Kohat_RAAS_v1", "Kohat_RAAS_v2", "Kohat_Invasion_v1"],
    "Kokan": ["Kokan_RAAS_v1"],
    "Lashkar": ["Lashkar_RAAS_v1"],
    "Logar": ["Logar_RAAS_v1"],
    "Manicouagan": ["Manicouagan_RAAS_v1", "Manicouagan_RAAS_v2", "Manicouagan_Invasion_v1"],
    "Mestia": ["Mestia_RAAS_v1", "Mestia_Invasion_v1"],
    "Sanxian": ["Sanxian_RAAS_v1", "Sanxian_RAAS_v2", "Sanxian_Invasion_v2"],
    "Skorpo": ["Skorpo_RAAS_v1", "Skorpo_Invasion_v1"],
    "Sumari": ["Sumari_RAAS_v1"],
    "Tallil": ["Tallil_RAAS_v1", "Tallil_RAAS_v2", "Tallil_Invasion_v1"],
}


def layers_of(m, md=None, allowed=None):
    out = [k for k, v in LAYERS.items() if v["map"] == m and (md is None or v["mode"] == md)]
    if m == "Anvil":
        out = [x for x in out if x == "Anvil_RAAS_v2"]
    if m == "AlBasrah":
        out = [x for x in out if x != "AlBasrah_RAAS_v3"]
    return sorted(x for x in out if allowed is None or LAYERS[x]["mode"] in allowed)


def best(m, md):
    c = layers_of(m, md)
    return max(c, key=lambda x: LAYER_B.get(x, 0)) if c else None


def popular(m):
    return [x for x in (best(m, "RAAS"), best(m, "Invasion")) if x]


def std(m):
    return popular(m) if m in TOP5 else CURATED[m]


def every(m):
    return layers_of(m, allowed=("RAAS", "Invasion"))


def flat(*groups):
    out = []
    for g in groups:
        for x in g:
            if x not in out:
                out.append(x)
    return out


def snake(items, n):
    """Deal items to n groups in popularity order: 0..n-1, n-1..0, ..."""
    groups = [[] for _ in range(n)]
    for i, x in enumerate(items):
        r, k = divmod(i, n)
        groups[k if r % 2 == 0 else n - 1 - k].append(x)
    return groups


class Pool:
    def __init__(self, key, title, files, schedule, settings, group, note="", extra_vote=None):
        self.key, self.title, self.files = key, title, files
        self.schedule, self.settings = schedule, settings
        self.group, self.note, self.extra_vote = group, note, extra_vote or {}


def weekly(key, title, weeks, settings, group, note=""):
    files = {f"week-{i + 1}/LayerVoting.cfg": (w, f"Week {i + 1}") for i, w in enumerate(weeks)}
    return Pool(key, title, files, [(w, WEEK) for w in weeks], settings, group, note)


def single(key, title, layers, settings, group, note="", name="LayerVoting.cfg"):
    return Pool(key, title, {name: (layers, title)}, [(layers, INF)], settings, group, note)


def common_pool():
    return flat(*(CURATED[m] for m in MID4 + REST))


def build():
    S = Settings
    pools = []
    common = common_pool()
    every_layer = flat(*(every(m) for m in MAPS))

    pools.append(single(
        "00-today", "Today (model of a default vote server)", every_layer,
        S(raas=4, invasion=2, map_skip=1, biome_skip=0), "base",
        "All RAAS and Invasion layers, 4 RAAS + 2 Invasion, MapSkipRounds=1, no biome rule. "
        "Used as the baseline in every chart."))

    plan4 = [["Narva"], ["Mutaha"], ["Fallujah"], ["Gorodok", "Yehorivka"]]
    pools.append(weekly(
        "01-weekly-plan-4w", "Weekly plan, 4 weeks",
        [flat(*(popular(m) for m in w), common) for w in plan4],
        S(map_skip=8, biome_skip=0), "main",
        "One big map per week (Gorodok and Yehorivka share week 4). All other maps every week."))

    pools.append(weekly(
        "02-weekly-plan-5w", "Weekly plan, 5 weeks",
        [flat(popular(m), common) for m in TOP5_ORDER],
        S(map_skip=8, biome_skip=0), "main",
        "Same as the 4 week plan, but Gorodok and Yehorivka get their own week."))

    day = flat(popular("Narva"), popular("Gorodok"), common)
    night = flat(popular("Mutaha"), popular("Fallujah"), popular("Yehorivka"), common)
    pools.append(Pool(
        "03-day-night", "Day / evening pool",
        {"LayerVoting.cfg": (day, "Day pool"), "LayerVotingNight.cfg": (night, "Evening pool")},
        [(day, DAY // 2), (night, DAY // 2)], S(map_skip=3, biome_skip=1), "main",
        "Day: Narva + Gorodok. Evening: Mutaha + Fallujah + Yehorivka. Same other maps. "
        "Uses NightTime in VoteConfig.cfg.", {"NightTime": "19:00-06:00"}))

    pools.append(single(
        "04-all-best", "All maps, best version", flat(*(popular(m) for m in MAPS)),
        S(), "main", "Every map once: its most played RAAS and its most played Invasion layer."))
    pools.append(single(
        "05-raas-best", "RAAS only, best version", [best(m, "RAAS") for m in MAPS],
        S(raas=6, invasion=0), "mode", "Most played RAAS layer of every map. No Invasion."))
    pools.append(single(
        "06-invasion-best", "Invasion only, best version",
        [x for x in (best(m, "Invasion") for m in MAPS) if x],
        S(raas=0, invasion=6), "mode", "Most played Invasion layer of every map that has Invasion."))

    by_size = {c: [m for m in MAPS if size_class(m) == c] for c in ("small", "medium", "large", "massive")}
    pools.append(single(
        "07-size-large", "Large and massive maps",
        flat(*(std(m) for m in by_size["large"] + by_size["massive"])), S(), "size",
        "Maps of 4 km and more: " + ", ".join(by_size["large"] + by_size["massive"]) + "."))
    pools.append(single(
        "08-size-medium", "Medium maps", flat(*(every(m) for m in by_size["medium"])),
        S(raas=3, invasion=1, map_skip=1, biome_skip=0, unique=False), "size",
        "Only " + ", ".join(by_size["medium"]) + ". 4 maps can not fill 6 options with "
        "different maps, so 4 options and UniqueMap=false."))
    pools.append(single(
        "09-size-small", "Small maps", flat(*(every(m) for m in by_size["small"])),
        S(raas=3, invasion=1, map_skip=1, biome_skip=0), "size",
        "Only " + ", ".join(by_size["small"]) + ". 4 options."))

    rotating = TOP5_ORDER + MID4
    for n in range(2, 8):
        weeks = [flat(*(std(m) for m in g), common_rest()) for g in snake(rotating, n)]
        pools.append(weekly(
            f"10-cycle-variety-{n}w", f"Variety cycle, {n} weeks", weeks, S(), "cycle-variety",
            f"The 9 most played maps are dealt to {n} weeks, the other 14 maps are in every week."))
    for n in range(2, 8):
        weeks = [flat(*(std(m) for m in rotating), *(std(m) for m in g)) for g in snake(REST, n)]
        pools.append(weekly(
            f"11-cycle-favorites-{n}w", f"Favorites cycle, {n} weeks", weeks, S(), "cycle-favorites",
            f"The 9 most played maps are in every week, the other 14 maps are dealt to {n} weeks."))
    others = [m for m in MAPS if m not in TOP3]
    for n in range(2, 8):
        weeks = []
        for w in range(n):
            pick = [others[(5 * w + k) % len(others)] for k in range(5)]
            weeks.append(flat(*(std(m) for m in MAPS[:3]), *(std(m) for m in pick)))
        pools.append(weekly(
            f"12-cycle-low-variety-{n}w", f"Low variety cycle, {n} weeks", weeks, S(),
            "cycle-low", "Only 8 maps per week: Narva, Mutaha, Fallujah always, plus 5 other maps."))

    seed_maps = by_size["small"] + ["Anvil", "Chora"]
    pools.append(single(
        "13-seed-low-players", "Seed pool (low player count)",
        flat(*(layers_of(m, "RAAS") for m in seed_maps)),
        S(raas=4, invasion=0, map_skip=2, biome_skip=0), "extra",
        "Small and fast RAAS maps for LayerVotingLowPlayers.cfg, used while the server fills up.",
        name="LayerVotingLowPlayers.cfg"))

    biome_layers = []
    for m in MAPS:
        if BIOME[m] == "FOREST":
            biome_layers += [best(m, "RAAS")]
        elif BIOME[m] == "SNOW":
            biome_layers += every(m)
        else:
            biome_layers += flat(layers_of(m, "RAAS"), [x for x in [best(m, "Invasion")] if x])
    pools.append(single(
        "14-biome-balanced", "Biome balanced", flat(biome_layers), S(), "extra",
        "Forest maps get 1 layer, desert maps get all RAAS + best Invasion, Goose Bay (snow) "
        "gets all its layers. Desert and forest end up close to half and half."))

    rising = [m for m in MAPS if trend(m) > 0 and m not in TOP3]
    pools.append(single(
        "15-rising", "Rising and reworked maps",
        flat(*(every(m) for m in rising), [best(m, "RAAS") for m in MAPS if m not in rising]),
        S(), "extra",
        "Maps outside the big 3 that grew in the last 3 months (" + ", ".join(rising) + ") with all their RAAS "
        "and Invasion layers. Other maps with only their best RAAS."))

    low_half = MAPS[len(MAPS) // 2:]
    pools.append(single(
        "16-discovery", "Discovery", flat(*(every(m) for m in low_half),
                                          [best(m, "RAAS") for m in MAPS[:len(MAPS) // 2]]),
        S(), "extra",
        "The less played half of the maps with all their layers. The popular half with only one "
        "RAAS layer each, so they still show up."))
    return pools


def common_rest():
    return flat(*(CURATED[m] for m in REST))


def trend(m):
    """Change of map share between window A and window B, in percent of A."""
    a = MAP_A[m] / sum(MAP_A.values())
    b = MAP_B[m] / sum(MAP_B.values())
    return (b - a) / a * 100
