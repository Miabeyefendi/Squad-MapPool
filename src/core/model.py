"""Vote model for the Squad layer vote (MapRotationMode=LayerList_Vote).

This is a model, not the game code. Assumptions:
- Every vote screen has a fixed number of slots per game mode (GameModeChoices).
- Each slot is drawn with equal chance from the layers that pass the rules:
  map not on this screen yet (UniqueMap), map not played in the last MapSkipRounds,
  biome not played in the last MapBiomeSkipRounds.
- If no layer passes, rules are relaxed in this order: biome, map skip, unique map.
  If still nothing, the slot stays empty.
- Reroll (CanRegenerateLayerList): when no top 5 map is on the screen, players
  reroll with probability REROLL_P. One new screen, no second reroll.
- Players pick with weight share(map) ** BETA. Invasion layers get INV_F.
  BETA and INV_F were tuned so the "today" pool gives the real top 5 share.
- One day = 12 rounds, one week = 84 rounds.
"""
import json
import os
import random
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

BETA, INV_F, REROLL_P = 1.4, 0.5, 0.6
DAY, WEEK = 12, 84
ROUNDS = 25200
TEST_MAPS = {"PacificProvingGrounds"}


def load_json(name):
    with open(os.path.join(ASSETS, name), encoding="utf-8") as f:
        return json.load(f)


STATS = load_json("mysquadstats.json")
LAYERS = {k: v for k, v in load_json("layers.json")["layers"].items() if v["map"] not in TEST_MAPS}

MAP_A = {m: a for m, a, b in STATS["maps"] if m not in TEST_MAPS}
MAP_B = {m: b for m, a, b in STATS["maps"] if m not in TEST_MAPS}
LAYER_B = {n.replace(" ", "_"): b for n, a, b in STATS["layers"]}
SHARE = {m: v / sum(MAP_B.values()) * 100 for m, v in MAP_B.items()}
MAPS = sorted(SHARE, key=SHARE.get, reverse=True)
TOP3 = set(MAPS[:3])
TOP5 = set(MAPS[:5])
BIOME = {v["map"]: v["biome"] for v in LAYERS.values()}
KM = {v["map"]: v["km"] for v in LAYERS.values()}


def size_class(m):
    km = KM[m]
    return "small" if km <= 2.5 else "medium" if km <= 3.2 else "large" if km < 6 else "massive"


def mp(layer):
    return LAYERS[layer]["map"]


def mode(layer):
    return LAYERS[layer]["mode"]


def weight(layer):
    return SHARE[mp(layer)] ** BETA * (INV_F if mode(layer) == "Invasion" else 1.0)


class Settings:
    def __init__(self, raas=5, invasion=1, map_skip=3, biome_skip=1, unique=True, reroll=True):
        self.raas, self.invasion = raas, invasion
        self.map_skip, self.biome_skip = map_skip, biome_skip
        self.unique, self.reroll = unique, reroll

    @property
    def options(self):
        return self.raas + self.invasion


def make_ballot(rng, pool, recent_maps, recent_biomes, s):
    slots = ["RAAS"] * s.raas + ["Invasion"] * s.invasion
    rng.shuffle(slots)
    ballot, used, relaxed, empty = [], set(), False, 0
    for slot_mode in slots:
        cand = []
        for step, (use_biome, use_skip, use_unique) in enumerate(
                ((True, True, True), (False, True, True), (False, False, True), (False, False, False))):
            if step == 3 and s.unique:
                break
            cand = [x for x in pool if mode(x) == slot_mode and x not in ballot
                    and not (use_unique and mp(x) in used)
                    and not (use_skip and mp(x) in recent_maps)
                    and not (use_biome and BIOME[mp(x)] in recent_biomes)]
            if cand:
                relaxed = relaxed or step > 0
                break
        if cand:
            pick = rng.choice(cand)
            ballot.append(pick)
            used.add(mp(pick))
        else:
            empty += 1
    return ballot, relaxed, empty


def simulate(schedule, settings, rounds=ROUNDS, seed=7):
    """schedule: list of (pool, rounds_active). The list repeats."""
    rng = random.Random(seed)
    cycle = sum(n for _, n in schedule)
    hist, relaxed, empty, rerolls = [], 0, 0, 0
    for r in range(rounds):
        t = r % cycle
        for pool, n in schedule:
            if t < n:
                break
            t -= n
        s = settings
        recent = {mp(x) for x in hist[-s.map_skip:]} if s.map_skip else set()
        biomes = {BIOME[mp(x)] for x in hist[-s.biome_skip:]} if s.biome_skip else set()
        ballot, rx, em = make_ballot(rng, pool, recent, biomes, s)
        if s.reroll and not any(mp(x) in TOP5 for x in ballot) and rng.random() < REROLL_P:
            rerolls += 1
            ballot, rx, em = make_ballot(rng, pool, recent, biomes, s)
        relaxed += rx
        empty += em
        hist.append(rng.choices(ballot, [weight(x) for x in ballot])[0])
    return hist, dict(relaxed=relaxed / rounds, empty=empty / rounds, reroll=rerolls / rounds)


def metrics(hist, extra):
    maps = [mp(x) for x in hist]
    n = len(maps)
    hits = [i for i in range(n - 3) if maps[i] in TOP3]
    days = [maps[i:i + DAY] for i in range(0, n - DAY + 1, DAY)]
    weeks = [maps[i:i + WEEK] for i in range(0, n - WEEK + 1, WEEK)]
    count = {m: maps.count(m) for m in set(maps)}
    top = max(count, key=count.get)
    return dict(
        top3=sum(m in TOP3 for m in maps) / n * 100,
        top5=sum(m in TOP5 for m in maps) / n * 100,
        top3_next=sum(maps[i + 1] in TOP3 for i in hits) / max(1, len(hits)) * 100,
        top3_in3=sum(any(x in TOP3 for x in maps[i + 1:i + 4]) for i in hits) / max(1, len(hits)) * 100,
        maps_day=statistics.mean(len(set(d)) for d in days),
        maps_week=statistics.mean(len(set(w)) for w in weeks),
        raas=sum(mode(x) == "RAAS" for x in hist) / n * 100,
        top_map=top,
        top_map_share=count[top] / n * 100,
        top3_per_day=statistics.mean(sum(d.count(m) for m in TOP3) for d in days) / 3,
        desert=sum(BIOME[m] == "DESERT" for m in maps) / n * 100,
        snow=sum(BIOME[m] == "SNOW" for m in maps) / n * 100,
        relaxed=extra["relaxed"] * 100,
        empty=extra["empty"],
        sample=maps[DAY * 50:DAY * 50 + 36],
    )
