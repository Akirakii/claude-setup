# TODO: the object catalogue

A design, not yet built (session of 2026-10-08). It replaces the stored-needs design in
`docs/TODO_creature_black_box.md`. Each slice below gets its own `/design` pass before
code. Status words: **decided** (the user chose it), **proposed** (Claude's pick, the user
has not confirmed it), **open** (no pick yet).

## Frame
A creature's free time goes to placed objects. What makes the player place one object
over another is what that object changes, never how much mood it gives. So each object
gets one identity that reads from its everyday name, and variety comes from different
outputs, scarce spots, and a herd that needs different things.

## Rules
| # | Rule | Status |
|---|---|---|
| 1 | No stored need meters. Mood is the only fast-changing layer: events move it (meals, sleep, dawn, grief; harm through health), the mustache shows it | Decided (the user built on it; never stated outright) |
| 2 | An object is one row in a shared place shape: **output** (a permanent change), **input** it uses up (only where competing for that input is the identity; most objects have none), **reach** (spot, radius) | Decided |
| 3 | No time-of-day axis and no "who" axis: who uses an object follows from its output | Decided |
| 4 | Offers (the creature picks the spot) and job sites (the player assigns it) are one shape; this absorbs slice 2b of the black-box doc | Proposed |
| 5 | Capacity is **visible spots**: what the object physically is (a jail cell holds 1, a bed holds 2). No hidden number, no body blocking | Decided |
| 6 | An object's purpose reads from its everyday name; prefer common objects over clever gags | Decided |
| 7 | A **stat gate** is the minimum stat a creature needs to use an object (the lab already needs INT 12) | Decided |
| 7b | A gate never sits on the object that trains the same stat (it would lock out the creatures that need training) | Proposed |
| 8 | Mood is never an object's purpose; an object may cause a mood event only as a side effect of its output | Proposed pillar |
| 9 | No object works by blocking space (no walls of bodies, no choke points) | Proposed pillar (the user rejected the living wall for this) |
| 10 | Every job grows the stat it is gated on (today every job grows INT) | Proposed |

Rules 8 and 9 go to `MEMORY.md` once the user confirms them.

## The catalogue (10 now, 2 VIT slots later)
| Object | Identity | Output | Input | Spots | Gate | Status |
|---|---|---|---|---|---|---|
| Bench press | Trains STR | STR | - | visible spots | - | Decided (the gym, renamed) |
| Treadmill | Trains DEX | DEX | - | visible spots | - | Decided |
| Library | Trains INT in free time (driven readers) until INT 12 | INT | - | 1 | - | Decided |
| Kitchen | Cooks crops into dishes | Dish | Crops | 1 cook | DEX 8 (today INT 8) | Kitchen decided; DEX gate proposed |
| Lab | Researches new cards | A card | - | 1 | INT 12 | Decided (exists) |
| Campfire | Company (heal role cut: HP comes back only from food, dishes, and a slow trickle) | - | - | visible spots | - | Heal reversed by the user (2026-10-08) |
| Nest (was the double bed; 4x4 footprint) | Love: a courting couple at full love both ways settles in it and lays one egg in it | Egg | - | 2 (one egg per nest) | - | Decided (no crop: none has a source since the brewing barrel went) |
| Medic bed | A downed creature carried here gets back up (on 1 HP) | Revive | - | 1 | - | Decided (the user rejected the first-aid tent) |
| Woodpile | An open frame box: choppers take an axe here (no limit) and bring the logs back; trees are chopped only within 24 m | A floating log stack the player walks into | Logs | - | INT 8 (the chop gate) | Built (2026-10-08), reshaped by the user |
| Jail | Troublemakers serve a time-out | Time-out; maybe warmth up | - | 1 per cell | STR 10 warden (proposed) | Decided; effect open |
| Dinner table | Creatures who share a dish become friends | Friendship | Dish | visible spots | - | Proposed |
| VIT trainer | - | VIT | - | - | - | Skipped for now (user) |
| VIT user | - | - | - | - | VIT | Skipped for now (user) |

Removed: protein bar (VIT trainer rejected), taming crops (all three variants), clock zone,
combiner, the nest, the living wall.

## Per object
- **Campfire.** Today it seats creatures for company (`OfferPlace.Kind.COMPANY`), gives a
  one-off `cozy` moodlet, and hosts hangouts that build bonds. New: it heals HP of
  creatures in its spots; the cozy moodlet and the bond role go.
- **Bed.** Today it heals the wounded (`BED_REGEN_MULT` 3x) and holds a downed body until
  it mends; a breeding pair lays an egg wherever they meet (`Creature.lay_egg`). New: a
  double bed (`block_size` 4x?x4, today `Vector3i(4, 2, 2)`) where a love-bonded pair fed a
  breeding crop sleeps and lays the egg. It no longer heals or revives.
- **Recovery object.** Takes over reviving: friends already carry a downed friend to the
  nearest free bed (`Creature` rescue, `_take_bed_in_reach`); that target becomes this
  object.
- **Kitchen and the dish.** The dish's only effect today is mood ("good mood for half a
  day"). New: the dish is an input that the dinner table uses up; eating it still fires the
  meal moodlet as a side event.
- **Jail.** For creatures that cause trouble. Trouble already exists as behaviour: bully and
  squabble get likelier as warmth drops (`temper = -warmth`, `SocialAction.affinity`), and
  the player sees 💢 and 😢. The player carries the troublemaker into a cell (existing
  carry verb); while jailed it cannot hurt others' mood and does no work.
- **Library.** Kept: chop and cook need INT 8, research INT 12, so reading at the
  library is how a bunny or fox (INT 5) gets into every other job.

## Open calls (user)
| # | Call | Lean |
|---|---|---|
| 1 | Recovery object: first-aid tent or hot spring | First-aid tent (reads as "medic near the fight") |
| 2 | Jail effect: rehabilitate (each stay raises warmth a little, permanently) or time-out only | Rehabilitate: a jail that changes nothing only parks the problem |
| 3 | Jail warden gate STR 10, so STR has an object that needs it | Yes |
| 4 | Kitchen gate moves from INT 8 to DEX 8, so DEX has an object that needs it | Yes |
| 5 | Every job grows its gated stat (rule 10) | Yes |
| 6 | Dinner table makes friends (bonds need a source once the campfire stops) | Yes |
| 7 | Confirm pillars 8 and 9 | - |
| 8 | VIT trainer and VIT user (candidates: swimming pool; guard post, a tough guard that draws raiders' attacks) | Later |
| 9 | Show the 5-night wave forecast (in data, no UI), so stat choices can be planned | Yes |
| 10 | How the chooser scores a place with no needs. `OfferPlace.want` still reads belonging and `TRAIN_NEED`. Scoring the campfire by missing HP would derive a need from the deficit of its outcome (pillar) | Open; a box `/design` before slice 2. The signs read `draw_for`, so they stay true whatever it becomes |

## Slices (each is a walking skeleton; run `/design` first)
1. [x] **Visible spots on offers (built AFK, 2026-10-08).** A place's capacity is its
   `Spot*` `Marker3D` children; each has a ground pad, lit in the place's tint while held
   (`OfferPlace.taken`, a replicated bitmask). A creature walks to its own spot and uses
   the place only while within `SPOT_RADIUS` (0.6 m) of it. Campfire 4 spots, training
   places 2. Job sites and the shared row moved to slice 1b.
1b. **Job sites as spots, and the shared row.** Kitchen, library, and lab get one spot
   each when work becomes an offer (rule 4), so assignment and capacity have one owner.
2. **Campfire heals.** Fire spots give HP regen; remove the cozy moodlet and the fire's
   hangout link. Bonds keep forming in ambient hangouts until slice 5 lands.
3. [x] **Medic bed and the nest (2026-10-08; the bed became a nest on 2026-10-09).** A 1-slot medic bed revives; nothing
   sleeps. A breeding crop sends a creature and its returned love to a free nest (2
   spots), and the egg appears on it; courtship no longer lays eggs by itself.
4. **Remove taming crops** (`FoodType.TAMING` and its three crop variants).
5. **Dinner table.** Shared dish makes friends; the kitchen gets its consumer.
6. [x] **Jail (built AFK, 2026-10-08, cheat `/jail`).** Cells with one spot; the carry verb puts a creature in; the time-out, then the
   effect from open call 2.
7. **Gates and job growth.** Kitchen DEX 8, jail warden STR 10, each job grows its stat.

Each slice ships with a cheat key that jumps to its state. Re-measure with the headless sim
(`SIM_PLACES=1`) after slices 2 and 5: who sits where changes.

## AFK decision log (2026-10-08, audit these)
| Gate | Resolved as | Why |
|---|---|---|
| Slice 1 scope: offers only, or offers and job sites | Offers only; job sites wait for rule 4 (slice 1b) | The job board owns one worker per site (`JobBoard._worker_at`), trees included. Spots on job sites now would make two owners of who holds a site, or a second board path for placed sites |
| Row fields in code (output, input, gate) | Not added: a spot list is the only generic field | Output is per-object code (stat, dish, card); input and gate have no reader on offers yet. A field no stage reads is dead data |
| Spot shape | `Marker3D` children in the scene | Reuses `Intent.move_to_node`, so the walk to a spot is the existing nav path; the count reads from what the object physically is |
| "What do they lack?" with no needs | The turned-away bubble (`💭` + the full place's glyph), from one scorer shared with the chooser and the announce flash | It reports spot contention, the chooser's real state. Cut: no bubble (demand invisible, so a second gym is a hidden call); a need bubble (invents a need); a "full" mark on the place (the lit pads already say it); a queue beside the place (changes an output to get a sign) |
| Spot distance | 1.3 m (fire), 1.2 m (training) from the centre | Outside the 0.9 m box plus the 0.3 to 0.5 m navmesh agent radius, so the spot is walkable |

## Code facts this design leans on (verified 2026-10-08)
- STR adds damage per hit, DEX attack speed, VIT HP, regen, knockback resist, INT work
  reach and job gates (`StatsComponent`). No armor exists.
- Species base stats: bunny 5/5/5/5, fox STR 7 DEX 9, frog VIT 7 INT 10.
- Creatures do not collide with each other (`collision_mask` is world + structures).
- Raiders punch through any piece they bump into (`docs/LAW_rooms.md` rule 5).
- The statue has HP and takes damage.
- Buildable today: block, half block, ramp, bed, campfire (wood); kitchen, library, gym,
  protein bar, treadmill (draft cards, 10 gems); the lab is placed at the start.
| Open call 1: recovery object | First-aid tent (3 cots), a `Bed` of kind RECOVERY | The lean; a tent reads as "medic near the fight", and one furniture class with a kind keeps spots and reservation on one path |
| Open call 2: jail effect | Rehabilitate: a served time-out (30 dilated s) adds +0.2 warmth for good; an early pickup changes nothing | The lean; a jail that changes nothing only parks the problem |
| Warden gate (open call 3) | Not built; waits for slice 7 | Gates land together with job growth |
| Bonded pair or any pair | Bonded: the fed creature's love, returned, same species | Love then has a gameplay output (who), the crop says when, the bed says where; one egg path, and courtship no longer bypasses the bed |
| Woodpile: how the player gets the wood | Walk into the floating log stack (user) | Reuses the dropped-item pickup; replaced right click spill |
| Start set | One woodpile beside the lab | Chopping near the base keeps working from the first minute, as before the ring gate |
| What starts breeding | The dusk roll (`docs/LAW_life.md` rule 5) replaced the court trigger, so the herd replaces itself. Breeding crops removed | The user meant the existing love trigger, moved onto the nest |
