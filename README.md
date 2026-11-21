# Squad Map Pool

Vote pool configs for Squad servers, and a simulation of each one.

On most vanilla servers Narva, Mutaha and Fallujah are about a third of all rounds. When one of them is played, one of the other two is very often back within the next 3 rounds. The pools here try to spread these maps out without taking them away, and use only the server's own cfg files. No plugin is needed.

![30 rounds in a row](design/charts/sequence.svg)

## Download

<!-- BEGIN:download -->
Every pool is a separate zip on the [release page](https://github.com/Miabeyefendi/Squad-MapPool/releases/latest). Not sure which one? Take **Recommended-Day-Evening.zip**. Each zip has the cfg files, the VoteConfig lines and a `HOW-TO-INSTALL.txt`.

The zips only hold text files (cfg and txt). They are made by `python src/main.py`, which writes them to `releases/` with a fixed date and file order, so you can build them yourself and compare the SHA-256.

<details><summary>SHA-256 of every zip</summary>

| File | SHA-256 |
|---|---|
| `All-Maps-Best.zip` | `f24a00d7d4acb19762d52ec9642d37212d6d2fd2bf0fbae4a73997220126c7e2` |
| `All-Pools.zip` | `fde9b05b5b0a357c1f9e16766bb7f5bd368517c1cb416bcc76e178f60021da06` |
| `Big-Maps.zip` | `75fdcf6667cfe26a615cee4053703c1e04d41ea51ede6bffbb75cf041fec6d4b` |
| `Biome-Balanced.zip` | `aff37ccdc7e84a1c6fead212f03b044defc3d85db6e7c10320402f5a3a4cb848` |
| `Default-All-Layers.zip` | `0046ad9e3f81172cd269856b7bf0f6877f953d79c31aef61faf13a9064da5b1d` |
| `Discovery.zip` | `6f889dd282c57adfd295898148ace3967d9d6d66a96923c25b9ba32773d26b1a` |
| `Favorites-2-Weeks.zip` | `aab88d32358e4a94d41bfbccbaa519491f2ee7885271a0e43166ce66413b33c7` |
| `Favorites-3-Weeks.zip` | `e9006cec5ab7bd3f6da2bd6c6d24272b8f5e763ab52d0fa9e5becd916bb4befb` |
| `Favorites-4-Weeks.zip` | `32d57759a1df7d25bb95a4574abe693eecb71837704b8e15706b0e43ffc41784` |
| `Favorites-5-Weeks.zip` | `b597ee1c6423fe39584d3b061c980b24c244319271a790fc40311bf6ca60f583` |
| `Favorites-6-Weeks.zip` | `28bef820fadc8b9cda35f478d4a01ee0e4b6b7a7de96d92f492d49cb9f7b4a39` |
| `Favorites-7-Weeks.zip` | `fd2b966185b4c9a18d1d2f3d7aaa58eaba6850690c8ccc4428436a188d063d74` |
| `Low-Variety-2-Weeks.zip` | `37edf2f691af14ee8a3033611f7653a44c3d9abd8e938813eb029f104318ca23` |
| `Low-Variety-3-Weeks.zip` | `a4635a190a88d268e0a71ebe375ea1041a61890153b5fb66d42e4e674817cfb8` |
| `Low-Variety-4-Weeks.zip` | `c6cd10fdcb520877a0f9cea30569ef2a20ee26334e2fef8577cf11157e6dd791` |
| `Low-Variety-5-Weeks.zip` | `55b7e9d059cf7f2229d8d099f605bf6e7bef135553c1b94429fad62642c72d15` |
| `Low-Variety-6-Weeks.zip` | `9f321194ad8234afbdad324be03dbcd0db24dcf14485729c7511d15418c3729f` |
| `Low-Variety-7-Weeks.zip` | `0d7ac6b3bf930f25349ab4fb57d8529c6145ce1451a9005a8f09ddcaa40eb38d` |
| `Medium-Maps.zip` | `c68f15879b913a79d77229ef001ed77227b6893883c9903121b8783a03c8a43e` |
| `Only-Invasion.zip` | `8c325a779d789e54c1168f1154417daee7bf18e6079daf0c9d82485236d9a1e9` |
| `Only-RAAS.zip` | `16aa48d1b778d126b14697f5e72dedfca25c7cd504cc7618de4973801025aa2d` |
| `Recommended-Day-Evening.zip` | `620a76aa3661ab012752529c5896155d8c9590937adaaaae33c6e5505e5910c9` |
| `Rising-Maps.zip` | `5a493a3122eda5090d8cac83fb9c518cba02b8430c8f015d1d8dc11314d4db54` |
| `Seed-Low-Players.zip` | `4d95062801221562455b023f0cf2b06e5668bced0ff1cc977818ebe9f6c22fa8` |
| `Small-Maps.zip` | `538f1963f6e7e3e049cdcb974e60f7491bde5ff9e3402b06622b314ae241f34a` |
| `Variety-2-Weeks.zip` | `db023748d95e7d22024f834a2278e765a4c08ce9029e2ad2f75ff7db714b9653` |
| `Variety-3-Weeks.zip` | `60440380a61897095deebb85f20c053f230e81f270e9deefff967bb2c26ba36b` |
| `Variety-4-Weeks.zip` | `f34ab865b9c4c051cbcd08674d72800859edbc70d7983dc01ec0ed47e53f9a4e` |
| `Variety-5-Weeks.zip` | `7e458d1042d7e563bed29bbec760096de63ef460d7ec73cf8e885fc4795be314` |
| `Variety-6-Weeks.zip` | `44ea2566008af50af1fa411087a3c66f1a483e8ae454169a15e407754a32f12d` |
| `Variety-7-Weeks.zip` | `a70777515b67f9c48762abc33230e3ddfe3f28468e46141dfc5654bc4b656eb9` |
| `Weekly-4-Weeks.zip` | `5962f34d37f15aec1ef7f84cef07f3bd7309ddc2dfc80cb93bb4531323d18296` |
| `Weekly-5-Weeks.zip` | `28a06b84bb41089bb75e3af028d5665612ad4135d4d8207eca2d668081fa36cc` |

</details>
<!-- END:download -->

## How to use a pool

1. `Server.cfg` needs `MapRotationMode=LayerList_Vote` and `UseVoteLayer=true`.
2. Copy the `LayerVoting*.cfg` files of a pool (from its zip, or from [`src/configs/pools/`](src/configs/pools)) to `ServerConfig/`.
3. Merge the keys from the pool's `VoteConfig.cfg` into `ServerConfig/VoteConfig.cfg`. Keys that are not listed stay as they are.
4. Restart the server. Weekly pools: copy the next week's file at the weekly restart.

Every pool keeps the reroll (`CanRegenerateLayerList=true`) and has no AAS layers.

## Results

![Pools compared](design/charts/pool-compare.svg)

**Big 3** means Narva, Mutaha and Fallujah. **Big 3 in 3 rounds**: after a big 3 round, how often another big 3 map comes back within the next 3 rounds. **Rules relaxed**: how often the vote screen could not be filled with the MapSkip and biome rules, so the model had to ignore a rule for one slot.

<!-- BEGIN:pools -->
Check of the model: the "today" pool gives a big 3 share of 32% and a top 5 share of 55%. Real servers in window B: 32% and 50% (of the 23 maps).

| Pool | Layers | Vote | Big 3 share | Big 3 next round | Big 3 in 3 rounds | Maps / day | Maps / week | RAAS | Rules relaxed |
|---|---|---|---|---|---|---|---|---|---|
| [Today (model of a default vote server)](src/configs/pools/00-today) | 75 | 4R+2I, skip 1 | 32% | 24% | 68% | 8.2 | 16.1 | 78% | 0% |
| [Weekly plan, 4 weeks](src/configs/pools/01-weekly-plan-4w) | 38-40 | 5R+1I, skip 8 | 8% | 0% | 1% | 10.9 | 18.2 | 84% | 1% |
| [Weekly plan, 5 weeks](src/configs/pools/02-weekly-plan-5w) | 38 | 5R+1I, skip 8 | 6% | 0% | 2% | 10.9 | 18.1 | 84% | 1% |
| [Day / evening pool](src/configs/pools/03-day-night) | 40-42 | 5R+1I, skip 3, biome | 18% | 5% | 34% | 9.5 | 18.9 | 85% | 2% |
| [All maps, best version](src/configs/pools/04-all-best) | 44 | 5R+1I, skip 3, biome | 35% | 29% | 68% | 8.9 | 17.6 | 89% | 0% |
| [RAAS only, best version](src/configs/pools/05-raas-best) | 23 | 6R+0I, skip 3, biome | 35% | 29% | 69% | 8.9 | 17.8 | 100% | 0% |
| [Invasion only, best version](src/configs/pools/06-invasion-best) | 21 | 0R+6I, skip 3, biome | 36% | 30% | 70% | 8.8 | 16.8 | 0% | 0% |
| [Large and massive maps](src/configs/pools/07-size-large) | 33 | 5R+1I, skip 3, biome | 0% | 0% | 0% | 8.2 | 12.9 | 87% | 51% |
| [Medium maps](src/configs/pools/08-size-medium) | 11 | 3R+1I, skip 1 | 97% | 97% | 100% | 3.3 | 3.9 | 80% | 100% |
| [Small maps](src/configs/pools/09-size-small) | 9 | 3R+1I, skip 1 | 0% | 0% | 0% | 4.8 | 5.0 | 84% | 5% |
| [Variety cycle, 2 weeks](src/configs/pools/10-cycle-variety-2w) | 34-36 | 5R+1I, skip 3, biome | 18% | 1% | 30% | 8.3 | 15.6 | 82% | 9% |
| [Variety cycle, 3 weeks](src/configs/pools/10-cycle-variety-3w) | 31-32 | 5R+1I, skip 3, biome | 18% | 0% | 2% | 7.9 | 15.1 | 82% | 9% |
| [Variety cycle, 4 weeks](src/configs/pools/10-cycle-variety-4w) | 28-32 | 5R+1I, skip 3, biome | 13% | 0% | 1% | 8.0 | 14.9 | 82% | 26% |
| [Variety cycle, 5 weeks](src/configs/pools/10-cycle-variety-5w) | 26-29 | 5R+1I, skip 3, biome | 11% | 0% | 1% | 8.0 | 14.7 | 83% | 19% |
| [Variety cycle, 6 weeks](src/configs/pools/10-cycle-variety-6w) | 26-30 | 5R+1I, skip 3, biome | 10% | 0% | 2% | 8.1 | 14.6 | 83% | 34% |
| [Variety cycle, 7 weeks](src/configs/pools/10-cycle-variety-7w) | 26-30 | 5R+1I, skip 3, biome | 9% | 1% | 2% | 8.1 | 14.5 | 83% | 34% |
| [Favorites cycle, 2 weeks](src/configs/pools/11-cycle-favorites-2w) | 32-36 | 5R+1I, skip 3, biome | 36% | 29% | 70% | 8.4 | 13.5 | 86% | 6% |
| [Favorites cycle, 3 weeks](src/configs/pools/11-cycle-favorites-3w) | 28-33 | 5R+1I, skip 3, biome | 38% | 30% | 72% | 8.2 | 12.2 | 87% | 24% |
| [Favorites cycle, 4 weeks](src/configs/pools/11-cycle-favorites-4w) | 27-30 | 5R+1I, skip 3, biome | 38% | 30% | 72% | 8.2 | 11.5 | 88% | 47% |
| [Favorites cycle, 5 weeks](src/configs/pools/11-cycle-favorites-5w) | 25-28 | 5R+1I, skip 3, biome | 38% | 30% | 73% | 8.1 | 10.9 | 88% | 63% |
| [Favorites cycle, 6 weeks](src/configs/pools/11-cycle-favorites-6w) | 24-28 | 5R+1I, skip 3, biome | 38% | 30% | 73% | 8.1 | 10.6 | 88% | 71% |
| [Favorites cycle, 7 weeks](src/configs/pools/11-cycle-favorites-7w) | 24-26 | 5R+1I, skip 3, biome | 38% | 30% | 73% | 8.0 | 10.4 | 89% | 75% |
| [Low variety cycle, 2 weeks](src/configs/pools/12-cycle-low-variety-2w) | 18-19 | 5R+1I, skip 3, biome | 53% | 49% | 90% | 6.5 | 8.0 | 89% | 99% |
| [Low variety cycle, 3 weeks](src/configs/pools/12-cycle-low-variety-3w) | 16-19 | 5R+1I, skip 3, biome | 61% | 61% | 94% | 6.1 | 8.0 | 86% | 99% |
| [Low variety cycle, 4 weeks](src/configs/pools/12-cycle-low-variety-4w) | 11-19 | 5R+1I, skip 3, biome | 67% | 68% | 96% | 5.7 | 7.9 | 77% | 99% |
| [Low variety cycle, 5 weeks](src/configs/pools/12-cycle-low-variety-5w) | 11-19 | 5R+1I, skip 3, biome | 62% | 63% | 94% | 6.0 | 7.9 | 80% | 100% |
| [Low variety cycle, 6 weeks](src/configs/pools/12-cycle-low-variety-6w) | 11-19 | 5R+1I, skip 3, biome | 62% | 62% | 94% | 6.0 | 7.9 | 81% | 99% |
| [Low variety cycle, 7 weeks](src/configs/pools/12-cycle-low-variety-7w) | 11-19 | 5R+1I, skip 3, biome | 64% | 65% | 95% | 5.9 | 7.9 | 81% | 99% |
| [Seed pool (low player count)](src/configs/pools/13-seed-low-players) | 7 | 4R+0I, skip 2 | 0% | 0% | 0% | 6.3 | 7.0 | 100% | 0% |
| [Biome balanced](src/configs/pools/14-biome-balanced) | 40 | 5R+1I, skip 3, biome | 36% | 29% | 71% | 8.7 | 17.2 | 91% | 23% |
| [Rising and reworked maps](src/configs/pools/15-rising) | 44 | 5R+1I, skip 3, biome | 29% | 22% | 57% | 8.9 | 17.3 | 86% | 13% |
| [Discovery](src/configs/pools/16-discovery) | 41 | 5R+1I, skip 3, biome | 34% | 28% | 67% | 9.1 | 18.1 | 97% | 0% |

- **Today (model of a default vote server)** (`00-today`): All RAAS and Invasion layers, 4 RAAS + 2 Invasion, MapSkipRounds=1, no biome rule. Used as the baseline in every chart.
- **Weekly plan, 4 weeks** (`01-weekly-plan-4w`): One big map per week (Gorodok and Yehorivka share week 4). All other maps every week.
- **Weekly plan, 5 weeks** (`02-weekly-plan-5w`): Same as the 4 week plan, but Gorodok and Yehorivka get their own week.
- **Day / evening pool** (`03-day-night`): Day: Narva + Gorodok. Evening: Mutaha + Fallujah + Yehorivka. Same other maps. Uses NightTime in VoteConfig.cfg.
- **All maps, best version** (`04-all-best`): Every map once: its most played RAAS and its most played Invasion layer.
- **RAAS only, best version** (`05-raas-best`): Most played RAAS layer of every map. No Invasion.
- **Invasion only, best version** (`06-invasion-best`): Most played Invasion layer of every map that has Invasion.
- **Large and massive maps** (`07-size-large`): Maps of 4 km and more: Gorodok, BlackCoast, AlBasrah, Manicouagan, GooseBay, Harju, Tallil, Chora, Kohat, Sanxian, Kamdesh, Lashkar, Yehorivka, Skorpo.
- **Medium maps** (`08-size-medium`): Only Narva, Mutaha, Fallujah, Anvil. 4 maps can not fill 6 options with different maps, so 4 options and UniqueMap=false.
- **Small maps** (`09-size-small`): Only Kokan, Mestia, Sumari, FoolsRoad, Logar. 4 options.
- **Seed pool (low player count)** (`13-seed-low-players`): Small and fast RAAS maps for LayerVotingLowPlayers.cfg, used while the server fills up.
- **Biome balanced** (`14-biome-balanced`): Forest maps get 1 layer, desert maps get all RAAS + best Invasion, Goose Bay (snow) gets all its layers. Desert and forest end up close to half and half.
- **Rising and reworked maps** (`15-rising`): Maps outside the big 3 that grew in the last 3 months (Gorodok, Yehorivka, BlackCoast, AlBasrah, Manicouagan, Kohat) with all their RAAS and Invasion layers. Other maps with only their best RAAS.
- **Discovery** (`16-discovery`): The less played half of the maps with all their layers. The popular half with only one RAAS layer each, so they still show up.
<!-- END:pools -->

### Weekly cycles from 2 to 7 weeks

<p>
<img src="design/charts/cycle-top3.svg" width="49%" alt="Cycle length vs big 3 share">
<img src="design/charts/cycle-repeat.svg" width="49%" alt="Cycle length vs big 3 repeat">
<img src="design/charts/cycle-maps-week.svg" width="49%" alt="Cycle length vs maps per week">
</p>

- **Variety cycle**: the 9 most played maps are dealt to the weeks, so two big 3 maps are only in the same week when there are 2 weeks. From 3 weeks on the big 3 repeat is almost gone.
- **Favorites cycle**: the 9 most played maps stay in every week and only the smaller maps rotate. The big 3 share goes up, not down. Rotating the small maps does not help.
- **Low variety cycle**: 8 maps per week with the big 3 always in. This is what happens when a pool gets too small: the big 3 take more than half of all rounds.

### What the model shows

- The share of the big 3 only goes down when they are **not on the same vote screen**. As long as one of them is on the screen it wins most of the time, so adding more small maps or more layers of small maps (Discovery, Biome balanced) changes very little.
- Splitting the big maps over time (weekly plans, day / evening) is the only thing that breaks the "Narva, Mutaha, Narva, Mutaha" pattern.
- `MapBiomeSkipRounds=1` has a side effect: Goose Bay is the only snow map, so it is allowed after every round and gets played more. In the day / evening pool it becomes the most played map (about 13%). If this is a problem, use `MapBiomeSkipRounds=0` and a higher `MapSkipRounds`.
- With only 4 or 5 maps (medium and small size pools) the screen can not be filled with different maps. These pools only make sense as a seed or event pool.

## Data

![Map share](design/charts/map-share.svg)

![Most played layers](design/charts/top-layers.svg)

<!-- BEGIN:data -->
Source: MySquadStats API, vanilla servers. Window A: 2026-05-21 to 2026-08-20 (36,703 matches). Window B: 2026-08-21 to 2026-11-20 (24,146 matches). The API allows 92 days per request.

**Game modes**

| Mode | Matches A | Matches B | Share B |
|---|---|---|---|
| RAAS | 24,997 | 16,366 | 67.8% |
| Invasion | 6,064 | 4,215 | 17.5% |
| AAS | 5,062 | 3,215 | 13.3% |
| TC | 342 | 167 | 0.7% |
| Skirmish | 162 | 159 | 0.7% |
| Insurgency | 41 | 13 | 0.1% |
| Destruction | 35 | 11 | 0.0% |

**Maps** (share of matches on the 23 vanilla maps, change = share B against share A)

| # | Map | Matches B | Share B | Change | Size | Biome |
|---|---|---|---|---|---|---|
| 1 | Narva | 2,767 | 11.5% | +3% | 2.8 km (medium) | Forest |
| 2 | Mutaha | 2,577 | 10.7% | +6% | 2.8 km (medium) | Desert |
| 3 | Fallujah | 2,267 | 9.4% | -1% | 3.0 km (medium) | Desert |
| 4 | Gorodok | 2,202 | 9.1% | +6% | 4.1 km (large) | Forest |
| 5 | Yehorivka | 2,148 | 8.9% | +3% | 6.3 km (massive) | Forest |
| 6 | BlackCoast | 1,605 | 6.7% | +10% | 4.6 km (large) | Forest |
| 7 | AlBasrah | 1,599 | 6.6% | +10% | 4.0 km (large) | Desert |
| 8 | Manicouagan | 1,597 | 6.6% | +2% | 4.0 km (large) | Forest |
| 9 | GooseBay | 1,336 | 5.5% | -9% | 4.0 km (large) | Snow |
| 10 | Harju | 967 | 4.0% | -5% | 4.0 km (large) | Forest |
| 11 | Tallil | 878 | 3.6% | -5% | 4.7 km (large) | Desert |
| 12 | Skorpo | 712 | 3.0% | -9% | 6.9 km (massive) | Forest |
| 13 | Chora | 446 | 1.9% | -13% | 4.1 km (large) | Desert |
| 14 | Kohat | 410 | 1.7% | +2% | 4.6 km (large) | Desert |
| 15 | Anvil | 406 | 1.7% | -1% | 3.1 km (medium) | Desert |
| 16 | Kokan | 368 | 1.5% | -11% | 2.5 km (small) | Desert |
| 17 | Sanxian | 364 | 1.5% | -14% | 4.6 km (large) | Forest |
| 18 | Mestia | 306 | 1.3% | -14% | 2.4 km (small) | Forest |
| 19 | Sumari | 274 | 1.1% | -8% | 1.3 km (small) | Desert |
| 20 | Kamdesh | 232 | 1.0% | -15% | 4.0 km (large) | Forest |
| 21 | FoolsRoad | 218 | 0.9% | -29% | 1.8 km (small) | Forest |
| 22 | Lashkar | 218 | 0.9% | -6% | 4.3 km (large) | Desert |
| 23 | Logar | 201 | 0.8% | -14% | 1.8 km (small) | Desert |

**Layer versions per map** (matches in window B, most played first)

| Map | RAAS | Invasion | Best Invasion |
|---|---|---|---|
| Narva | RAAS v1 (1,525) | Invasion v2 (286), Invasion v1 (244) | Invasion v2 |
| Mutaha | RAAS v1 (1,023), RAAS v2 (822) | Invasion v1 (283) | Invasion v1 |
| Fallujah | RAAS v1 (829), RAAS v2 (722) | Invasion v1 (236), Invasion v2 (177) | Invasion v1 |
| Gorodok | RAAS v1 (937), RAAS v2 (838) | Invasion v1 (102), Invasion v2 (101), Invasion v3 (65) | Invasion v1 |
| Yehorivka | RAAS v2 (818), RAAS v1 (781) | Invasion v1 (154), Invasion v2 (152) | Invasion v1 |
| BlackCoast | RAAS v1 (631), RAAS v2 (602) | Invasion v2 (107), Invasion v1 (85), Invasion v3 (56) | Invasion v2 |
| AlBasrah | RAAS v1 (551), RAAS v2 (436), RAAS v3 (0) | Invasion v1 (175), Invasion v2 (120), Invasion v3 (104) | Invasion v1 |
| Manicouagan | RAAS v1 (597), RAAS v2 (588) | Invasion v1 (127), Invasion v2 (94) | Invasion v1 |
| GooseBay | RAAS v1 (557), RAAS v2 (464) | Invasion v1 (128), Invasion v2 (111) | Invasion v1 |
| Harju | RAAS v1 (413), RAAS v2 (224) | Invasion v1 (60), Invasion v3 (43), Invasion v2 (40) | Invasion v1 |
| Tallil | RAAS v1 (249), RAAS v2 (212) | Invasion v1 (353) | Invasion v1 |
| Skorpo | RAAS v1 (454) | Invasion v1 (105), Invasion v3 (74), Invasion v2 (67) | Invasion v1 |
| Chora | RAAS v1 (230) | Invasion v1 (27), Invasion v2 (22) | Invasion v1 |
| Kohat | RAAS v1 (185), RAAS v2 (45) | Invasion v1 (82), Invasion v2 (51) | Invasion v1 |
| Anvil | RAAS v2 (162), RAAS v1 (159) | Invasion v1 (49) | - |
| Kokan | RAAS v1 (219) | Invasion v1 (54) | Invasion v1 |
| Sanxian | RAAS v1 (127), RAAS v2 (120) | Invasion v2 (44), Invasion v1 (27), Invasion v3 (0) | Invasion v2 |
| Mestia | RAAS v1 (167) | Invasion v1 (42) | Invasion v1 |
| Sumari | RAAS v1 (136) | Invasion v1 (52) | Invasion v1 |
| Kamdesh | RAAS v1 (145) | Invasion v1 (29) | Invasion v1 |
| FoolsRoad | RAAS v1 (99) | Invasion v1 (43) | Invasion v1 |
| Lashkar | RAAS v1 (141) | Invasion v1 (44) | Invasion v1 |
| Logar | RAAS v1 (156) | none | - |

**Rising:** AlBasrah (+10%), BlackCoast (+10%), Mutaha (+6%), Gorodok (+6%), Narva (+3%), Yehorivka (+3%).  
**Falling:** FoolsRoad (-29%), Kamdesh (-15%), Mestia (-14%), Sanxian (-14%), Logar (-14%), Chora (-13%), Kokan (-11%), Skorpo (-9%), GooseBay (-9%), Sumari (-8%), Lashkar (-6%), Tallil (-5%), Harju (-5%).
<!-- END:data -->

The raw numbers are in [`src/assets/mysquadstats.json`](src/assets/mysquadstats.json). Layer names, biomes and map sizes come from [SquadLayerList](https://github.com/fantinodavide/SquadLayerList) ([`src/assets/layers.json`](src/assets/layers.json)).

## How the model works

It is a model, not the game code. For every round:

1. Build a vote screen. Every slot has a fixed mode (`GameModeChoices`), and the layer is drawn with equal chance from the layers that pass the rules: map not on the screen yet (`UniqueMap`), map not played in the last `MapSkipRounds`, biome not played in the last `MapBiomeSkipRounds`. If nothing passes, the rules are relaxed in this order: biome, map skip, unique map.
2. Reroll: if no top 5 map is on the screen, players reroll with a 60% chance. One new screen.
3. Players vote. A layer wins with

   ```
   P(win) = w(layer) / sum of w on the screen
   w(layer) = share(map) ^ 1.4        (x 0.5 for Invasion)
   ```

   `share` is the map's share of matches in window B. The power 1.4 and the 0.5 were tuned so that the "today" pool gives the real big 3 and top 5 share (see the check line above the results table).

Each pool runs 25,200 rounds (300 weeks, 12 rounds a day). Day / evening switches pool every 6 rounds.

The chance that a map with `r` RAAS layers is on a 5 RAAS + 1 Invasion screen is about

```
P(on screen) = 1 - (1 - r / R) ^ 5        R = RAAS layers that pass the rules
```

so one more layer of a map gives it more screen time, and more screen time is almost the same as more wins for a popular map.

## Not verified

- How the game really draws layers for the screen. The model draws with equal chance per layer.
- Whether `GameModeChoices` is a fixed count per screen or an upper limit. The model uses a fixed count.
- `NightTime` and `LayerVotingNight.cfg` were seen in a server template, not tested on a vanilla server. The `NightTime` value in the day / evening pool is an example and has to match the server's own busy hours.
- The key for `LayerVotingLowPlayers.cfg` (player count threshold) was not tested.
- Whether a cfg change needs a restart or `AdminReloadServerConfig` is enough. Plan for a restart.
- No pool was tested on a live server.

## Run it yourself

Python 3.10 or newer, no packages.

```
python src/main.py
```

This rebuilds every cfg in `src/configs/pools/`, runs all simulations, writes the charts to `design/charts/` and the numbers to `src/configs/results.json`, and fills the tables in this README. The pools are defined in [`src/core/pools.py`](src/core/pools.py), the model is in [`src/core/model.py`](src/core/model.py).
