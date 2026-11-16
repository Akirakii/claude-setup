# TODO: block build + new core loop roadmap

Replaces the draft + build direction. The user set the direction on 2026-10-05 and asked
for AFK execution, one ship per step. Each step gets its own `/design` pass before code.

## Direction (user calls, 2026-10-05)
- Building is one 3D block lattice. Every build takes whole cells. No edge walls, no floor
  slabs, no snap guessing.
- Placement is the face rule: a click fills the cell touching the face under the crosshair.
- Basic construction comes from a hammer. Non-basic things come from a stationary shop.
- The well, the poop goal, and the draft cards are removed.
- The player handles the world with two hand verbs, break and grab, not an axe swing.
- A block cell is 0.5 m on every axis, on one world-fixed lattice. Nothing is measured from
  the ground under a column.
- The ground is one flat plane. No generated hills, platforms, or obstacle rocks.
- Advanced technology unlocks through a lab staffed by creatures. The player sets the
  direction of research; what is discovered is random.

## AFK decision log (audit these)
| Decision | Resolved as | Evidence or reason |
|---|---|---|
| Block cell size | 2 m on every axis (`Grid.BLOCK`) | Measured: a 1 m gap and a 1 m wide ramp give no creature path; 2 m gives a path (agent radius 0.5, nav cell 0.25). A 1 m cell would let the player build doors creatures cannot use, which is a hidden rule |
| Block height | Each column stacks up from the terrain under its centre (cell = column x, stack index, column z) | The terrain rolls everywhere (no flat clearing). A world-fixed height lattice buries or lifts a ground piece by up to 1 m, which hides a fence or a bed and puts furniture out of a creature's reach. Cost: tops in neighbouring columns step with the slope, so a platform on a hill is stepped |
| Gap under a ground block on a slope | The block grows a foundation down to the lowest corner | Nothing walks or sees under a wall; raised blocks stay open below so bridges stay bridges |
| Support rule | None | The face rule only places against something, so every new block already touches the world. Removing a block may leave floaters |
| Body inside the target cell | Placement refused (ghost shows red) | A 2 m block placed around a player or creature traps it |
| Fence shape | A low solid cell (2 x 1 x 2 m), not a thin panel | A thin panel needs a facing and leaves corner gaps; a full cell needs neither |
| Floor piece | Cut. A block placed at height is the floor | Same purpose as a block; one piece, one rule |
| Ramp direction | Leans toward the block whose side face you click; on open ground it climbs away from you | The common case (a ramp up to a platform) needs no facing guess. The ghost shows the direction |
| Building on a ramp's slope | Refused | A sloped face has no single touching cell |
| Furniture cell | One block cell each (bed, kitchen, library, stations) | One lattice for everything; a block above a bed leaves it a 2 m room |
| Axe on a build piece | Picks it back up as its item | A shoved piece would have to hop cells; that rule moves to A3 with the machines |
| Wild creatures and blocks | Unchanged: hostiles still pass through structure pieces, only a fence is attackable | Existing combat rule, not part of this rework. OPEN for the user: should a block stop a hostile? |
| Hammer form | A hotbar tool given at spawn, not a mode key | The user asked for basics "at the hammer"; a held tool is visible in hand |
| Picking the piece | `R` cycles block, ramp, fence, bed. No palette panel | A panel is menu-driven action (rejected antipattern). The ghost is the readout: it is the piece, with its name and wood cost above it |
| Short of wood | Ghost goes red, nothing is placed | Same signal as a taken cell: one colour means "this click does nothing" |
| Getting a basic | Zero trips: select hammer, aim, click | The original complaint was shop + inventory shuffle + slot + place |
| Basics in the shop | Removed | One source per thing |
| Built-count tally for basics | Not kept | Their cost is flat, so nothing reads the count. The probe still sees every placement |
| Left click while holding the hammer | Still the axe swing, which picks a piece back up | The axe is always in hand; build and unbuild sit on the two mouse buttons |
| Shop place | 10 m east of the well, on the terrain, frozen | "Stationary" read as: always there, never moves. The spot is OPEN for the user |
| Shop price | Unchanged (poop, rising per copy) | What poop is for is step D's question |
| Buying a piece | It lands in the hotbar, its slot is selected, the panel closes | Removes pick-up, inventory shuffle, and slot change from the original complaint. Path is now: open shop, click card, aim, click |
| No free hotbar slot | The shop drops the piece beside itself, as before | A purchase is never lost |
| Machine footprints | Sized to the model: clock 1x3x1, tent 3x2x3, combiner 1x2x1 cells, centred on the aimed cell | A piece owns the cells it fills, so nothing is built through it |
| Axe on a tent or combiner | Runs the machine's own verb (shake crops loose, hit the fuse button). It does not pick the machine up | The axe hit was already their verb; a pick-up on the same click would eat it. Cost: once placed they stay. OPEN for the user: how to move one |
| Axe on a clock | Picks it back up, like furniture | It has no axe verb of its own |
| Wide piece on a slope | Seated at the aimed cell's ground height; its outer cells can hang or sink with the slope | Known rough edge of terrain-relative columns; place wide machines on flatter ground |
| Setting the research direction | By what you throw into the lab: crops study crop cards, poop studies creature cards, wood studies machine cards | A thrown item is an existing verb (kitchen, tent). No menu. The topic shows on the lab |
| Which card each topic finds | crop: kitchen. creature: library, combiner, tent. machine: clock, van | Grouped by the card's existing substrate tag |
| Changing direction | Not until the fuel and the bar are spent | The lab is occupied by its topic: the choice is a commitment, not a toggle |
| What is discovered | Uniform random among the locked cards of that kind | The user's rule: direction is chosen, the find is random |
| Research cost | 6 fuel, plus 4 for each card already known | A pace knob, uncalibrated. Each item thrown in is one fuel |
| Who researches | A creature with the Research job, INT 12 or more | Links library (study raises INT) to lab. Consequence: a student now stays at the library until INT 12, not 8 |
| Getting the first lab | Hammer basic, 10 wood | The unlock path cannot itself be locked |
| What poop is for | Creature-research fuel, and shop prices | Step D removes its other sink (the well goal) |
| Seeing a discovery | The lab shows the card's name; the card is now in the shop | Readout only. A bigger moment is listed under E-open |
| Crops and seeds | Keep the 1 m ground cells; a block cell covers 2x2 of them and is refused while any holds a crop | PRE-PILLAR (unconfirmed): one lattice, crops use its fine ground level |
| Pending Phase 10 work in the tree | Shipped first as its own PR (#219) | It was finished and marked done in the roadmap; keeping it separate keeps this work reviewable |
| Break reach | The aim ray's full length, the same ray placement uses | One hand range for place and break; no second number |
| Tent and combiner under the hold | Their own verb fires at once on the press (shake, fuse), as the axe hit did | Their new input is blocked-list row 5; until then they cannot be broken, so a placed one stays |
| Local probe captures (`util/probe/presets/index.js`, 264 MB) | Left out of every commit | Over GitHub's 100 MB file limit |

## Steps
- [x] **Gate 0: nav measurements.** Results in the log above; pinned by `test_block_nav.gd`.
- [x] **A1: walking skeleton** (#220). One block piece, face rule, ghost, server check,
  cheat key `B` (99 blocks). The old pieces still use the old rules.
- [x] **A2: every build on the lattice** (#221). Block, ramp, fence, bed, kitchen, library,
  barrel, cauldron, smoker are block pieces. Deleted: floor, wall, stairs, the edge map,
  the story ladder, the support lattice, phase snap, the stairs bridge search, floor
  columns. Crops and saplings keep the 1 m ground cells.
- [x] **A3: machines on the lattice** (#224). Clock (1x3x1 cells), tent (3x2x3), combiner
  (1x2x1) are placed pieces bought at the shop; they land in hand like a kitchen. The van
  stays a vehicle and still rolls out beside the shop.
- [x] **B: hammer** (#222). A starting hotbar tool that holds every basic. `R` picks the
  piece, the ghost shows it with its wood cost, right-click places and pays the wood. The
  shop no longer sells basics.
- [x] **C: stationary shop** (#223). A fixed prop beside the well from match start; the
  visit schedule is gone. A bought piece goes straight into the buyer's hand and the panel
  closes. Machines (clock, tent, combiner, van) still roll out beside the shop until A3.
- [x] **D1: draft cards removed** (#226). No pick-1-of-3, no reroll, no skip, no tiers.
  Research is the only unlock path. A met poop goal still heals the well, respawns
  forage, and grows the map, then arms the next goal on its own.
- [x] **D2: hands, beds, and the well's removal.** See "D2 design" below.
  - [x] **D2a: hold to break.** The swing, the charge, and the bat knockback are gone. A
    held left click breaks the aimed block piece or tree in 1 second and harvests a ripe
    crop on contact; a felled tree leaves its logs and a sapling in its own cell.
  - [x] **D2b: grab** (#233).
  - [x] **D2c: bed rescue and recruit** (#233).
  - [x] **D2d: start beds, watering off.** The match starts with 3 beds in a row beside
    the shop. Plants count as watered and never dry (`CropConfig.drying`, off); the frog no
    longer hands out the watering can. The shop stays 10 m east of the well until D2e moves
    it to the centre.
  - [x] **D2e: delete the well, its goal, and their tests.** Off the level in #235; code
    and tests deleted in the cleanup step.
  - [ ] **D2-open, left out of D2a:** an unripe crop takes the hold but
    still gives its old hit result, not its seed; the server does not rate-limit break
    requests; no probe counter for breaks; the dealer's hand weapon still knocks creatures.
- [x] **E: lab research skeleton** (#225). The lab is a hammer basic (10 wood). Thrown fuel
  sets its topic, a researcher (INT 12) burns one fuel per labor tick, and a full bar
  discovers one random locked card of that kind. The draft still runs beside it until D.
- [x] **F: quarter cells on a world lattice, flat ground** (#229). A cell is 0.5 m,
  `floor(world / 0.5)` on every axis. The ground is one flat plane; the hill, platform,
  obstacle, and prop generators are deleted. Furniture and machines keep their size in
  metres (footprints 4x in cells); the bed is 4 x 2 x 2 cells and turns with its step.
  Supersedes these decision-log rows: block cell size, block height, gap under a ground
  block, fence shape, furniture cell, wide piece on a slope.
- [ ] **F-open:** three physics suites still pass hill and platform counts that nothing
  reads (`test_terrain_creatures_reach_centre`, `test_spawn_above_terrain`,
  `test_level_navmesh_reachability`); trim them to what flat ground can still fail. Frame
  cost of thousands of block nodes is unmeasured on screen (headless has no renderer).
- [x] **G: build menu on `R`, no hammer, four basics, wood refund** (#230). `R` opens a
  menu of block, half block, ramp, bed; the pick is the build hand over the hotbar, right
  click places it for wood, and any hotbar slot puts it down. A broken basic drops the
  wood it cost. A one-cell piece breaks in 0.25 s. One lab stands in the start set.
  Supersedes these decision-log rows: hammer form, picking the piece, basics in the shop,
  getting the first lab, left click while holding the hammer.
- [x] **U1: discoveries land in the build menu** (#231). Every unlocked placed piece is
  in the `R` menu; a discovered piece is paid in poop on placing and costs more per copy.
  The shop sells only what is not a placed piece (the van).
- [ ] **U-open:** a second lab is not obtainable (U-c wanted "lab" as a discovery; that
  is a new card, so it waits for the user). The price is paid by the placing client and
  tallied by the server on the client's word, as wood always was.
- [ ] **G-open:** the menu is a plain row of buttons, not a radial. The fence is out of the menu but its code
  and the fence-only hostile rule remain. The build menu is the logged exception to the
  menu-driven-action rule.
- [ ] **E-open:** a louder discovery moment than the label over the lab; tier pacing
  (today any locked card of the kind can come first); cost curve calibration.
- [ ] **Cross-cutting, per step:** tests, probe counters, cheat keys, guide tips, co-op sync.

## Remaining work (2026-10-05, after #231 and the user's picks)

Frame: the player defends one fixed thing. Hostiles walk a straight line to it and wreck
every block on that line without slowing. Nothing the player builds stops them; only the
herd does, and beds keep the herd standing.

PRE-PILLAR (unconfirmed): the player defends one fixed place, and the run ends when it
falls.

### Words used below
- **Wild crops:** the crops already standing on the map at match start, harvested without
  planting. (Code name: forage.)
- **Well goal:** today the well asks for N poop; when it is fed, wild crops respawn, one
  tree grows, the map widens 2 m per side, and a bigger ask starts. It goes with the well.
- **How blocks are held:** today every placed block is its own engine object (a mesh, a
  collision body, a script). The alternative is one table of cell -> piece kind that the
  engine draws in batches (Godot `GridMap`). The player sees no difference; it only
  matters for frame rate at thousands of blocks.

### Decided
| # | Work | Decision | Source |
|---|---|---|---|
| 1 | Hostiles and blocks | **Superseded by `docs/LAW_rooms.md` rule 5 (user, 2026-10-09): pieces are solid to wilds, which punch through.** Was: blocks are transparent to hostiles: no collision, no pathing, no slowing. A basic (block, half block, ramp, bed) that a hostile's body passes through is destroyed on the spot and drops the wood it cost, the same as when the player breaks it. Every other piece is left standing and untouched. There is no walling in this game, and no piece health. `CreatureConfig.HOSTILES_WRECK_BASICS` switches the wrecking; it is off, so hostiles pass through and leave basics standing | User |
| 2 | Grab | Left click on a creature picks it up, left click again puts it down. No size cap. Right click throws it the way the player faces: a tap is a short toss, a hold of up to 1 s winds up to 50% more force, shown as a ring closing around the crosshair. A heavier creature flies less far. Every live hostile the thrown body touches on its way stands stunned for 2 s (no moving, no swinging), shown by 💫 | User |
| 3 | Bed rescue and recruit | Position decides: any downed body within 2 m of a free bed lies in it, whether it was put down, thrown, or fell there. In the bed a blue recovery bar in place of its health bar fills at the bed regen rate over its max health; full, it gets up friendly on 1 hp and keeps the bed to heal in; under a quarter health a fight does not pull a friendly out of its bed; it mends there and gets up friendly | User |
| 5 | Player health | There is none. Remove the player's health and death code; a hostile's hit on the player is knockback only (which is what ends a grab) | User |
| 6 | Tent | Out for now: off the research pool and the build menu | User |
| 7 | Van, shop | No van for now. The shop is fixed in place; the player cannot hit or move it | User |
| 10 | Hand weapon | Removed | User |
| 11 | Hat strip, rotate key | Dropped | User |
| 13 | Cleanup | Do it (list in the build order) | User |
| 14 | Standing Clock, Fusion Cube | Out for now: off the research pool, so research finds only the kitchen and the library | User |

### Row 1, how a passing hostile finds the blocks
Ask the lattice: each move tick, the cells the hostile's body overlaps are looked up
(`Grid.get_block`) and any piece there is destroyed. The lattice already owns what stands
where, so there is one owner and the result is the same on every peer. (Cut: a physics
area on the hostile, a second owner of occupancy.)

What blocks are for (user): shaping where friendlies go, height and reach, looks and
layout. Later, to be designed: rooms that raise stats (a comfortable bedroom, a fitting
workroom), in the manner of RimWorld.

Follows from "only basics": the lab, kitchen, library, clock, and combiner are never
wrecked, so research cannot be lost to a wave. The bed is a basic, so a hostile walking
through a bed wrecks it (5 wood drop) and whoever lay in it is on the ground again.
Assumed, to confirm with the user: that the bed is meant to be wrecked this way.

### Row 4, what the player defends
**Decided (user, 2026-10-05): a goddess statue, for now.** Its own object, standing in the
open, fixed, apart from the shop.

- It has health and a health bar. Waves walk to it in a straight line; a hostile in reach
  hits it. The run ends at zero.
- It gets health back by itself during the day, and not at night.
- The player cannot hit, break, or move it.

It gets back about a quarter of its health in one day (user), so a bad night still costs
the next one. The exact rate is sized against the day's length when built.

The shop: fixed, not hittable, sells nothing for now; what it sells is to be designed.

### Row 12, as answered
- **Research has no direction pick and no fuel** (user, 2026-10-05: no direction, and "go
  with recommended" on fuel). Candidates were: fuel stays and any item counts; only poop
  is fuel; no fuel. Picked no fuel: the cost of research is the worker it keeps off the
  field (sacrifice through occupied shared state), and throwing items at a lab by hand is
  a chore with no choice left in it once the direction is gone.
- **The research pool is four cards** with the tent and the van out: kitchen, library,
  combiner, clock. The barrel, cauldron, and smoker exist as pieces but are on no card, so
  nothing unlocks them today. Whether they join the pool is open.
- **Breeding does not need the tent.** Checked in the code: a friendly fed its breeding
  food turns to breeding, two breeders meet and lay an egg. (An earlier note here said
  otherwise, from a stale comment.)
- **Second lab, menu shape:** unchanged, wait until played.

### Piece sizes (user, 2026-10-06; #237)
The grid stays 0.5 m. The basics grow to fill several cells:
| Piece | Cells | Metres |
|---|---|---|
| Block | 2 x 2 x 2 | 1 x 1 x 1 |
| Half block | 2 x 1 x 2 | 1 x 0.5 x 1: exactly one grid layer, no part-filled cell any more |
| Ramp | 2 x 2 x 2 | 1 x 1 x 1 |
| Bed | 4 x 2 x 2 | 2 x 1 x 1 (unchanged) |

- Placement still snaps every 0.5 m. A piece placed on a face lies flush against that face
  (its footprint extends away from it), so wide pieces stack side by side and hang under
  an underside.
- A small piece (up to 8 cells: block, half block, ramp) breaks in 0.25 s; anything larger
  in 1 s.
- Measured: one ramp (1 m wide) carries no creature path; two abreast do. A creature door
  is still 3 cells (1.5 m).
- Cost is unchanged at 1 wood each, so wood now buys 8 times the volume.

### Placement resolve (#238)
User ask: a placement is always found, the piece is centred on the cursor, and it feels
natural.

Prior art: Minecraft fills the cell touching the clicked face and shows nothing when it is
taken. Terraria's Smart Cursor "places a block at the nearest legal space to the cursor"
([Terraria wiki](https://terraria.wiki.gg/wiki/Smart_Cursor)); that is the shape taken.

| # | Candidate | Verdict |
|---|---|---|
| a | **Low-corner anchor, one rule per axis, then a nearest-valid search.** Along the face's normal the piece lies flush against the face; across it the piece is centred on the aimed point; if that spot is taken, the free spot whose piece sits nearest the aimed point is used | Picked. One rule covers every size and every face, with no even-size bias |
| b | Keep the centre-cell anchor and bolt a search on | Cut: an even-sized piece has no centre cell, so it can never be centred on the cursor |
| c | Free placement with snap points on neighbours (Valheim) | Cut: it leaves the lattice |

Rules as built:
- The anchor of a piece is its low corner cell.
- Wanted spot: flush on the hit face along its normal, centred on the hit point on the
  other two axes, snapped to 0.5 m.
- If the wanted spot is taken or a body stands in it: candidates are slides across the face
  up to the piece's own size, and steps out along the normal up to its own size. The one
  whose centre is nearest the aimed point wins.
- If none of those is free, the ghost shows red at the wanted spot. So "always" holds
  unless everything within one piece-size is full.
- The server checks the cell the client resolved, as before.

Limit of the search, not tuned: at most (2s+1)^2 x (s+1) candidates for a piece s cells
wide, only walked when the wanted spot is blocked.

### Creatures defend the statue (#239)
Report: the run is lost because creatures do not defend the statue.
Measured cause: a friendly only fought a wild within 12 m of its own home, and home was
where it was born or recruited; carrying it did not move its home. In a headless raid (six
foxes, six defenders): defenders living beside the statue, 4 of 7 fought and the statue
took no damage; the same defenders living 20 m east, 1 of 7 fought and the statue lost 116
health in 12 s.
Fix (user picks):
- The fight leash is effectively infinite for now (`CreatureConfig.FIGHT_LEASH_RADIUS`,
  larger than any map). A friendly
  fights any hostile it notices, however far from home.
- Home follows the hand: where a creature is put down is its home.
- A worker's home is its job site.
After the fix, same far defenders: 6 of 6 fought, the statue took no damage.
Still a limit: a friendly notices a hostile only within 15 m of where it stands (its
targeting rule's detection radius), so a worker further than that from the fight does not
join. Whether that radius should grow is open.

### Placement pull, bed mend, clock (user, 2026-10-06)
- **Whole-piece placement.** Across the aimed face a piece lands only a whole number of
  pieces from the piece aimed at (from the world origin on bare ground): no half-piece
  offsets. A taken spot slides one whole piece. The lattice is still 0.5 m, so a half
  block still stacks in half-height layers along the face's normal. (A tunable pull
  toward whole steps was built first the same day and dropped for this.)
- **Wood.** An oak drops 6 to 10 logs (was 3 to 5).
- **Bed mend.** A downed body put down at a free bed lies in it, still down. The bed is
  taken, the body's rot timer stops, and it heals at the bed rate. At full health it gets
  up friendly and groggy. Grabbed out, or the bed wrecked, it is on the ground downed and
  the timer runs on from where it stopped.
- **Statue in the navmesh.** Creatures were walking into the statue: the navmesh had no
  hole there, so paths ran through its collider. Any node in the `nav_obstacle` group now
  carves a hole of its own radius at bake time; the statue joins it (1.7 m). Hostiles are
  unaffected, they walk straight at their target. The shop is not in the group.
- **Grab aim.** A creature is picked when its body is within 0.6 m of the aim line
  (`CreatureConfig.AIM_SLACK`), not only on an exact hit. Same rule for the inspector and
  the aimed cheats.
- **Nearest job site.** Each board poll (0.5 s) a worker swaps to a free site of its own
  job when that one is nearer by more than `CreatureConfig.JOB_SWITCH_MARGIN` (2 m). So a
  chopper takes the nearest tree, and a tree that grows beside it beats the far one it was
  walking to. Which job a creature gets is unchanged: sites still pick workers in the
  order they were posted.
- **Clock.** The day runs from match start; nothing freezes it. The run opens at the first
  moment of daylight.
- **Day length.** `DayNightConfig.FIRST_DAYLIGHT_SECONDS` (15) sets the first day; the
  2:1 ratio gives a 7.5 s night, 2.8 s dawn and dusk, a 28.1 s cycle. Each cycle is 10% of
  the first longer (daylight 15, 16.5, 18).
  Follows from it, not tuned: creature and statue regen are sized on the first daylight,
  so both run about 2.1 times faster per second than at the 60 s cycle.
  Unmeasured: whether a wave can spawn and reach the statue inside a 7.5 s night (groups
  spawn 1 s apart).

### Build order
1. [x] Removals and research (#232): the player cannot strike with a weapon (creatures
   still wield them); the player has no health, a hostile's hit is knockback only; the
   tent and the van are off the research pool; the fence is deleted; research has no fuel
   and no direction: the researcher's labor fills the bar and a full bar finds a random
   locked card.
   Left for later: the barrel, cauldron, and smoker are discarded (user) but only
   unobtainable, not deleted; their code is tangled with storage, drops, and the kitchen.
   Measured in a 200 s headless run: three of the four cards found. The pool empties in
   minutes, so research cost needs sizing against the day once the loop is played.
2. [x] Grab, bed rescue and recruit (#233). Left click on a creature within 4 m picks it
   up; left click again puts it down. Any knockback on the holder or on the carried
   creature ends the grab; a carried live hostile keeps swinging at its holder. A downed
   body put down within 2 m of a free bed gets up friendly in it, at 1 health and groggy,
   and the bed then heals it like any wounded friendly. While carrying, the hands do
   nothing else. The lead item is gone; the combiner now takes a creature just put down
   by hand.
   Since the 2026-10-06 change below, the body stays down in the bed until it is mended.
3. [x] Hostiles wreck basics in passing, and the statue (#234). A hostile goes straight at
   its target and never paths, so nothing built is in its way. Each behavior tick, every
   basic piece inside the box around its body is broken and drops its wood; other pieces
   are untouched. The statue stands 10 m west of the centre: 1000 health, a health bar,
   a base target for waves, a quarter of its health back over one daytime, and the run
   ends when it falls. The well no longer ends the run and is no longer a target.
   Measured in a headless raid (six foxes, one defender): six of nine blocks wrecked, the
   kitchen left standing, the statue at 474 of 1000 after 12 s. Statue health against
   wave damage is untuned.
4. [x] The well leaves the level (#235). No well stands on the map; the statue is at the
   centre. The starter herd appears in a ring around the statue. The poop goal, its HUD
   bar, and everything a met goal did (wild crops respawn, one tree, the map widening) are
   gone. The player faces the statue at spawn.
   Left for the cleanup step: the well's own code, config, and tests still exist, unused by
   the level, because the stations, the combiner, and the reward-spot service read its
   config constants. The guide frog's tips are not shown any more (they named the well and
   its goal); the tutorial needs rewriting for the new loop.
   Seen in a headless run: the starter herd is one frog, and the first waves take the
   statue down by a few percent. Start herd size and wave strength are untuned. The goal's reward (wild crops
   respawn, a tree, a wider map) is removed with it, not moved (user).
5. [x] Combiner fuse on right click (#236); left hold breaks it like any piece, and a
   combiner broken with creatures inside releases them merged first.
6. Cleanup.
   - [x] The well's code, config, scene, and suites are deleted. What machines still used
     of it moved to its one user: spit speeds to `Station`, the spot ring to
     `SpotService`, the start forage budget to `CropConfig`. Roam's well-avoid, the
     navmesh carve, the can's refill at the well, and the under-world item eject went with
     it. `WELL_PRIORITY_RANK` is `BASE_PRIORITY_RANK` (the statue is the base).
   - [x] Hill, platform, and obstacle counts dropped from the terrain suites.
   - [x] Deleted: tent, medical van, barrel, cauldron, smoker, watering can and its
     droplets, with what only they used (van driving on the player, tent mode in creature
     AI, station fly-in and its spot search, water request, hotbar water bar, their probe
     tallies and config). Breeding by breeding food is untouched.
   - [x] Deleted (user, 2026-10-06): crop and tree drying, the empty shop and the
     `Station` base it was the last user of, the fly-in arc for placed things, orphan
     `.uid` files. `test_terrain_creatures_reach_well` is now `..._reach_centre`.
     Kept: the probe's `goals` and `wgl_` keys (the analyzer reads them, and `wgl_` still
     counts every friendly spawned as an adult), and `PushableBody` (no subclass left,
     one knockback test uses it).
   - [x] Dropped (user): an unripe crop giving its seed. There are no crop seeds.
   - [x] Guide tips: the run HUD shows the dens loop's tips for the first days. The old guide
     frog is still unspawned; what to do with it is open call 5 in
     `docs/TODO_v1_release.md`.
   - [x] Probe counters for break, grab, throw (place is `builds`, rescue is `rescued`).
   - [ ] A server rate limit on break and place.
7. [x] Block-field cheat (#236): `F4` lays a 45 x 45 square of blocks (about 2,000) ahead
   of the player; press it again facing elsewhere for more. Spawning 2,009 took 523 ms
   headless. Frame rate with them on screen is the number still owed, from a playtest.

## D2 design: hands, beds, and the well's removal

Frame: the player stops hitting things and starts handling them. Two hand verbs replace the
axe swing: **break** (hold on a thing to take it out of the world) and **grab** (pick a
creature up, put it down). The bed becomes the one place a downed body gets up again.

### User calls (2026-10-05)
- The bed owns both recruit (a downed wild) and rescue (a downed friendly).
- Watering is off; plants do not dry.
- The axe bonk is gone. The player never knocks a creature back.
- The player grabs and releases any creature, friendly or enemy. An enemy escapes when its
  attack knocks the player back.
- Blocks place and break as in Minecraft. Breaking needs no tool and takes about 1 second;
  an axe appears by itself and plays the chop.
- A tree is chopped with the same hold. The whole tree breaks at once and leaves a sapling.
- The player starts with the shop and 3 beds.

### Prior art
| Field practice | Source | Taken or not |
|---|---|---|
| Break progress builds only while the button is held on one block and resets on release | [Minecraft: Breaking](https://minecraft.wiki/w/Breaking) | Taken |
| Break time is a per-block number (hardness); some things break instantly | same | Taken: one table, crops at 0 |
| Cutting the base of a tree removes the whole tree and can drop its seed | [Terraria: Trees](https://terraria.wiki.gg/wiki/Trees) | Taken; the sapling is planted, not dropped |
| A felled tree leaves a stump that blocks replanting until cleared | [Stardew Valley: Trees](https://stardewvalleywiki.com/Trees) | Not taken: a second chore with no choice in it |
| A grab ends when the held one is hit hard enough from outside; the hold is time-limited | [SmashWiki: Grab](https://www.ssbwiki.com/Grab) | Taken as one rule: knockback on either side ends the grab |
| A downed friend is carried to a free bed; a downed enemy to a separate prisoner bed, then recruited over time by a warden | [RimWorld recruit guide](https://alittlebithuman.com/how-to-get-more-colonists-in-rimworld/) (practitioner source) | Free-bed gate taken. Separate bed type and warden not taken (user call: one bed, both jobs) |

### Candidates and cuts
**Break.** (1) A hold-to-break hand verb on the aimed thing, time per kind. (2) Keep the
swing, drop only its knockback. (3) A break mode on the hammer. Picked 1. Cut 2: a swing
that does nothing to a creature is a dead input on the most common target. Cut 3: the user
call says no tool is needed, and a mode is hidden state.

**Grab.** (1) Carry: the creature is pinned to the holder until released or knocked out.
(2) Leash: it walks behind the holder (today's lead item). (3) Push: the player shoves it by
walking into it. Picked 1 (user call). Cut 2 as the same purpose (move a creature where I
want) with a weaker read; the lead item goes. Cut 3: no way to lift a body onto a bed or
over a wall.

**Bed.** (1) A downed body released on a free bed lies there as a sleeper; it gets up
friendly when the bed has healed it to full. (2) It stands up at once at 1 HP. (3) It is
held until dawn, as the well did. Picked 1: the bed is occupied for the whole mend, so a
rescue, a recruit, and a wounded worker compete for the same 3 beds (sacrifice through
occupied shared state). Cut 2: the bed is free again instantly, so nothing is given up. Cut
3: a wait with no choice in it.

### Rules
**Break**
- Hold left click on the aimed thing. Progress fills on the player's dilated clock and
  resets when the button is released or the aim leaves the thing.
- The axe model shows and loops its chop while progress runs. There is no swing, no charge.
- At full progress the thing leaves the world and gives back what it is made of.
- Creatures with the Chop job fell a tree through the same server call, in one labor tick.

| Kind | Break time | Gives back |
|---|---|---|
| Hammer basic (block, ramp, fence, bed, lab) | 1.0 s | Its full wood cost, into the inventory |
| Shop piece (kitchen, library, stations, clock, tent, combiner) | 1.0 s | The piece, into the hand |
| Grown tree | 1.0 s | Logs at the stump; a sapling planted in the tree's own cell |
| Sapling | 1.0 s | The sapling item |
| Grown crop | 0 s (breaks on contact, so a held sweep harvests a row) | Its produce |
| Ungrown crop | 1.0 s | Its seed |

This closes A-open "a way to move a placed tent or combiner": break it and place it again.
It also removes the tree's felling flight; nothing reads the chop direction any more.

**Grab**
- One input on an aimed creature within reach picks it up; the same input puts it down in
  front of the player. No throw.
- Hands are shared: while carrying, the held hotbar item is hidden and break and place do
  nothing.
- A carried creature does not move or work. A carried live enemy keeps its attack timer and
  swings at its holder.
- **One escape rule: knockback on the holder or on the carried creature ends the grab.** So
  a live enemy is held for about one of its attack cooldowns, any other enemy's hit frees
  it, and a friendly's hit on a carried enemy knocks it out of the player's hands.
- A downed body never attacks, so it is carried until released. Its down timer keeps
  running in hand.
- One holder per creature, one creature per holder. The server owns it.

**Bed**
- A downed body released within reach of a free bed is taken by it: the body lies in the
  bed, its down timer stops, and the bed heals it at the bed's heal rate.
- At full health it gets up friendly, whatever it was before, with the existing groggy
  window.
- A bed already holding a creature refuses the body; it lands beside the bed and its timer
  runs on.
- A wounded friendly still walks to a free bed by itself. That is the contention: three
  scratched workers can fill the beds a downed one needs. The player frees a bed by
  grabbing the sleeper out of it.
- Breaking an occupied bed puts the occupant on the ground as it was (a downed body stays
  downed).

**Start set**
- The match starts with the shop where the well stood and 3 beds beside it, placed through
  the normal lattice placement so they break and move like any bed.
- The hotbar starts with the hammer only. The always-in-hand axe item, the watering can,
  and the lead item leave.

**Watering off**
- Crops and saplings never dry: planted things count as watered and the dry check is gated
  by one config flag. The can, its refill at the well, and the dry tint stay in the code
  behind that flag so the mechanic can come back. Bringing it back is a TODO in
  `TODO_design_backlog.md`, not a comment in source.

### Data dictionary
| Variable | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| `break_target` | node or none | Player (local) | The thing the hold is working on | Set on press, cleared on release or aim change |
| `break_progress` | float 0..1 | Player (local) | Fraction of the break time elapsed | Reset to 0 whenever `break_target` changes; at 1 the client asks the server to break |
| `break_sec` | float, seconds | Static, per kind (table above) | Time to break | Constant |
| `held` | creature or none | Player (server) | The creature in hand | Set by grab; cleared by release, either side's knockback, the creature leaving the tree |
| `holder` | player or none | Creature (server); replaces `lead.holder` | Who carries it | Mirrors `held`; cleared on the same events |
| `occupant` | creature or none | Bed (server), exists today | Who lies in the bed | Set when a body is taken or a wounded friendly reserves; cleared at full health, on grab, on break |
| `down timer` | seconds, exists today | Creature (server) | Time left before a downed body is gone | Runs while downed; paused while `occupant` of a bed |

### Pipeline
| Stage | Reads | Writes | Passes on |
|---|---|---|---|
| Aim | crosshair ray | `break_target` | target kind |
| Hold | `break_target`, `break_sec`, player clock | `break_progress`, axe visual | break request at 1.0 |
| Server break | target, its kind | world (piece removed), inventory or hand, sapling | probe event |
| Grab | aimed creature, `held`, `holder` | `held`, `holder`, hand visibility | carried pose each tick |
| Knockback (either side) | `held`, `holder` | clears both | creature dropped in place |
| Release | `held`, nearest free bed within reach | clears `held`, `holder`; may set bed `occupant` | body on bed or on ground |
| Bed mend | `occupant`, heal rate | health; at full: state friendly, clears `occupant` | probe event (tame or rescue) |

No stage reads a value nothing writes. `break_progress` is local only: a client that lies
about it gains a faster break, which the server bounds by rate-limiting break requests per
player to one per `break_sec`.

### Constants
| Constant | Value | Kind | Why |
|---|---|---|---|
| `BREAK_SEC` per kind | 1.0, crops 0 | Pace | User call: about 1 second. A day is long against it, so a wall of 10 costs 10 s of attention, not a phase |
| Hand reach | The block-placement reach | Limit | Break, grab, and place share one range; no second number |
| `BED_TAKE_REACH` | 1 block cell (2 m) | Limit | The body must be released at the bed, not near the base |
| Start beds | 3 | Limit | User call |

No new constant sets how long an enemy stays held: the enemy's own attack cooldown does.

### Code shape
One `HandComponent` owner for both verbs on the player (it already owns what the hand
shows). Break and grab are two branches of one aimed-target resolve, not two tools. On the
server, one `break_piece` verb replaces `hit_by_axe` and `chop`; `holder` replaces the lead
component; the bed gains one `take(body)` verb beside `reserve`. Deleted: the axe swing and
charge, bat knockback and its config, the hat strip, the lead item, the tree's yeet, the
shove of placed pieces.

### Blocked on the user
| # | Open call | Why it blocks | Lean |
|---|---|---|---|
| 1 | **What ends the run, and what waves attack,** once the well is gone | The well is the loss condition and the wave target. D2e cannot delete it without a new owner | The run ends when no friendly creature is standing and none lies in a bed. Beds are then the visible comeback, and the shop keeps one job. Against: a wipe can snowball. Alternative: the shop gets HP and waves target it (one actor, two jobs, which the user rejected once for the well) |
| 2 | Grab input: left click on a creature, or its own key | Left click also breaks; one button doing two verbs is close to the rejected one-verb multiplex | Left click. With the bonk gone, left click on a creature would otherwise do nothing |
| 3 | Can every creature be grabbed, whatever its size (a fused giant, a boss) | Carrying a boss to the far fence solves a wave by hand (a god power) | Any downed body; a live one only up to a size cap |
| 4 | Break refund: full wood back, or a part | Full refund makes every build free to undo | Full. The cost is the second of attention and the hole it leaves mid-wave |
| 5 | Tent shake and combiner fuse were axe hits | The verb is gone | Right click, the same "use" input as the shop |
| 6 | The charged swing stripped job hats off a crowd | The verb is gone | Drop it; grabbing a worker already takes it off its job |
| 7 | The medical van carries downed bodies and released them on an axe hit | Its release verb is gone, and grab now does its job one body at a time | Keep it as the bulk carry; right click releases; bodies still need beds |
| 8 | The poop goal's reward (fresh forage, one tree, a bigger map) | The goal goes with the well | Each lab discovery grows the map and respawns forage |
| 9 | Should a block stop a hostile | Open since A2. It decides whether walls are defense or only layout | Yes, with fences as the breakable gap |
| 10 | Where the player heals and what a dead player does | Player death prints a line and nothing else today | Out of D2; needs its own design |

## F design: quarter cells on a world lattice, flat ground

Frame: the lattice stops adapting to the world. One fixed 0.5 m grid, and the ground is
made to fit it (flat, at a cell boundary), not the other way round.

### User calls (2026-10-05)
- Cell edge 0.5 m (a quarter of the 2 m edge).
- The lattice is world-fixed on all three axes.
- A 1-cell gap does not need to fit a creature; doors are wider.
- The ground is one flat plane. Trees and wild crops still scatter.

### What follows directly
- `cell = floor(world / 0.5)` on each axis; the ground plane sits at y = 0, so stack index 0
  stands on it. The per-column base, the foundation under a ground block, and the
  "level with the neighbour column" step in the face rule all go.
- A 1 m ground cell (crops, trees) is exactly 2 x 2 block columns; a ground block is
  refused while the ground cell it stands in holds a plant.
- Furniture and machines keep their size in metres, so their footprints in cells grow 4x
  per axis (a bed 4 x 2 x 4, a tent 12 x 8 x 12).

### Measured (2026-10-05, `test_block_nav.gd` and a one-off bench)
| Question | Result | Consequence |
|---|---|---|
| Narrowest creature door | 3 cells (1.5 m) carries a path, 2 cells does not | A door is 3 cells wide |
| Does a wall one cell thick stop a creature | Yes at 1 and at 2 cells high: its 0.5 m top is too narrow to stand on | A single row of blocks is already a wall. Only a platform wide enough to stand on is a step |
| Navmesh build and bake with 500 / 2,000 / 8,000 block nodes | 34 / 60 / 166 ms | The bake is not the limit at these counts |

An earlier note here said a 0.5 m block is "a step, not a wall". That was read off the
0.7 m walk-up limit without a bake, and the bake disproved it for thin walls.

### The six points, as built or decided
| # | Point | Decision | Why |
|---|---|---|---|
| 1 | Unlocks | U1 (see G): lab in the start set, a discovery adds its piece to the build menu | One build path, no dependence on the shop |
| 2 | Wood cost | 1 for block, half block, and ramp (user) | |
| 3 | A second half block in a taken cell | Refused; the cell is taken. No merge into a block | With every basic at 1 wood a merge has no purpose of its own: breaking and placing a block does the same |
| 4 | Break time | 0.25 s for a one-cell basic; 1 s for a bed, a tree, and anything wider | The user's 1 s was for a 2 m block; a 2 x 2 m hole is now 16 cells |
| 5 | Hill, platform, obstacle generator | Deleted | With flat ground those are paths nothing runs. The jump and drop navlinks stay for player-built platforms |
| 6 | Block storage (F1) | One node per block | Bake cost holds to 8,000. On-screen frame cost is the open half: playtest with the block-field cheat before building big |

### Not affected
The face rule (a click fills the cell touching the aimed face), body-in-cell refusal,
hold-to-break, the hammer, the shop, research.

## G design: the build menu, the four basics, and unlocks

### User calls (2026-10-05)
- The player builds only four things for now: block, half block, ramp, bed (2 x 1 m, so
  4 x 2 cells). The fence and the lab leave the build list.
- There is no hammer tool. `R` opens the build menu; the picked piece is what the hand
  builds. Right click places, left hold removes.
- The menu picks the piece. This is menu-driven action, which `MEMORY.md`
  rejects; the user took it as an **exception for now**. Revisit when the piece list or the
  input settles.
- Breaking a basic gives back the materials it cost, not the piece as an item. (Answers F4;
  closes the D2-open item on refunds.)
- This also answers F2 (the ramp stays) and F3 (the fence is out for now).

### Build input: what the field does
| Game | Open the piece menu | Place | Remove | Source |
|---|---|---|---|---|
| Valheim | Right click, hammer in hand | Left click | Middle click | [Valheim controls](https://www.bisecthosting.com/pl-pl/blog/valheim-controls-guide-pc-console-controller-xbox-keybinds) |
| Rust | Hold right click (radial wheel), building plan in hand | Left click | A separate hammer tool | [Rustafied: building](https://www.rustafied.com/rust-how-do-i-build-walls) |
| Minecraft | None: the piece is the hotbar item | Right click | Hold left click | [Minecraft: Breaking](https://minecraft.wiki/w/Breaking) |

Finding: every game with a piece menu uses three inputs (menu, place, remove). None opens
the menu on both mouse buttons, because one of them has to place. This game already took
Minecraft's two (left hold breaks, right click places), so the menu needs a third.

| # | Option | What it optimizes | Cost |
|---|---|---|---|
| H1 | **A key opens a radial menu** (the existing piece key, `R`); the ghost caption shows the piece, its cost, and the key. With no piece chosen yet, the first click opens the menu instead | Both mouse buttons keep one meaning each, everywhere | One more key to learn; the caption teaches it |
| H2 | Valheim layout while the hammer is in hand: right click opens the menu, left click places, middle click breaks | Matches the closest known game | Left and right swap meaning between the hammer and every other slot; break moves off the button the user asked for |
| H3 | Hold right click opens the radial (Rust), a tap places | No new key | Hold-to-keep-placing is lost: a held right click can no longer lay a wall |

**Answered (user, 2026-10-05): H1, and no hammer.** Right click places, left hold removes,
`R` opens the build menu from any slot.

What follows from "no hammer":
- The picked piece is a build hand that sits over the hotbar: while it is up, the ghost
  shows and right click places it; the hotbar item is put away.
- Assumed, to confirm: selecting any hotbar slot (number key or scroll) puts the build
  hand down. `R` brings the menu back.
- Left hold removes in every state, build hand or not; it never needed a tool.
- The first hotbar slot is free again. The hammer item, its slot rule, and the piece
  cycle key go.

### The four basics
| Piece | Cells | Shape | Cost (lean) | Break gives back |
|---|---|---|---|---|
| Block | 1 x 1 x 1 | Full 0.5 m cube | 2 wood | 2 wood |
| Half block | 1 x 1 x 1, lower half | 0.25 m slab. A second half block in the same cell makes it a block | 1 wood | 1 wood |
| Ramp | 1 x 1 x 1 | Slope up one cell, leans as today | 2 wood | 2 wood |
| Bed | 4 x 1 x 2 | 2 x 1 m, lies along its placement step | Today's bed cost | The same |

Open: the wood numbers (F4 asked for them; the leans above keep a half block at half a
block). A half block is the first piece that fills part of a cell; the cell still counts as
taken for placement, and the face rule treats its top as that cell's top face.

### Unlocks: how a non-basic piece becomes buildable
The shop is experimental, so the unlock path must not depend on it.

Standing user call (2026-10-05): technology unlocks through a lab staffed by creatures;
the player sets the direction, the discovery is random. The design below keeps that and
answers the two things it left open: where the first lab comes from, and where a
discovery shows up.

Prior art:
| Field practice | Source | Verdict |
|---|---|---|
| A recipe unlocks the first time its material is picked up | [Valheim recipes](https://game8.co/games/Valheim/archives/320286) | Cut: there are three materials here, so nothing is left to find after minute one, and it drops the user's lab |
| Standing near a research station lets you prototype; once prototyped, build anywhere | [Don't Starve: Science Machine](https://dontstarve.wiki.gg/wiki/Science_Machine) | Taken in part: unlock once, then build freely |
| Scan pieces of a thing found in the world to learn its blueprint | [Subnautica scanning](https://thegameswiki.com/subnautica-2/wiki/blueprints-and-scanning) | Cut for now: needs a new noun (wrecks) scattered on the map |

Candidates:
| # | Structure | Essence | Verdict |
|---|---|---|---|
| U1 | **The lab is part of the start set** (shop, 3 beds, 1 lab). **A discovery adds its piece to the build menu.** The piece is paid for on placing, like a basic | One way to get any placed thing: the build menu. Unlock is the menu growing | Recommended |
| U2 | The lab stays a hammer basic; discoveries go to the shop | Two ways to get a placed thing (hammer for basics, shop for the rest) | Cut: the user just took the lab off the hammer, and it leans on the shop |
| U3 | No lab. Pieces unlock on first pickup of a material, or from scanned wrecks | Unlock by exploring | Cut: see the prior-art verdicts |
| U4 | The lab hands over the discovered piece itself, once, as an item | The discovery is a single object, not a permission | Cut: one copy of a kitchen is a resource pile, and a second lab run for a second copy is a grind |

Why U1, on the end state: one build path instead of two, one owner of "what can I build"
(the build menu), and the shop is free to change or go without touching unlocks. It adds
no noun: the lab, the menu, and the start set all exist. The player's sacrifice stays where
it is today: a researcher is a creature not farming or fighting, and fuel thrown into the
lab is food, poop, or wood not spent elsewhere.

What U1 leaves open, for the user:
| # | Open call | Lean |
|---|---|---|
| U-a | What a discovered piece costs to place | Poop, at today's shop price for that card. Wood stays the cost of basics, so the two materials buy different things |
| U-b | Whether the shop keeps selling the same pieces while it exists | No: one source per thing. The shop keeps only what is not a placed piece (the van) |
| U-c | Can the player build a second lab | Yes, once: "lab" is the first thing the start lab can discover, so research speed is itself a choice |
| U-d | The start lab's place | In the row with the beds |

## Playtest: 1 m basics
1. `B`, `R`, Block: the ghost is a 1 m cube. It moves in 0.5 m steps as you aim.
2. Place one, then aim at its east, west, north, south, top faces: each new block sits
   flush against that face, never overlapping.
3. Half Block is 1 m wide and half as tall; two stacked are as tall as a block.
4. Place two ramps side by side against a 2-wide stack of blocks: creatures walk up. One
   ramp alone: they do not.
5. Hold left click on a block: gone in a quarter second, one wood drops.

## Playtest: combiner and block field
1. `F2`, `F1`, `R`: place a combiner. Carry two friendlies of one kind into it and put
   them down inside. Right click the combiner: one bigger creature comes out.
2. Hold left click on the combiner for a second: it comes out as an item.
3. `F4`: about 2,000 blocks appear ahead of you. Watch the frame rate while looking at
   them and while a wave walks through them. Press `F4` again somewhere else for more.

## Playtest: no well
1. Start a match: no well. The statue stands at the centre, you face it, and a frog appears
   beside it.
2. No goal bar on the HUD. Poop has two uses: placing a discovered piece, and nothing else.
3. Play past a night: the map does not grow and wild crops do not come back.

## Playtest: statue and wrecked basics
1. Start a match: a stone statue with a health bar stands west of the well.
2. `B` for wood; build a row of blocks and a bed between the map edge and the statue.
   `F1`, `F2`, place a kitchen beside them.
3. Wait for night (or `F12`): wilds walk in a straight line, through the blocks. Every
   block and the bed in their path breaks and drops wood. The kitchen stays.
4. With no defenders near, wilds reach the statue and its bar drops. At zero the run ends
   with "THE STATUE HAS FALLEN".
5. Survive a night with the statue hurt: over the next day its bar climbs by a quarter.
6. Let wilds hit the well: nothing happens to the run.

## Playtest: grab and bed rescue
1. `F10` spawns a herd. Left click a creature: it is carried in front of you. Left click
   again: it is put down.
2. While carrying, try to break, place, or use the hotbar: nothing happens.
3. `F12` starts a fight. Grab a live wild: it hits you within a moment, you are knocked
   back, it drops.
4. When a wild is downed (lying, blinking), grab it and put it down on a free start bed:
   it gets up friendly and sleeps there. Do the same with a downed friendly.
5. Put a downed body on a bed that already holds a sleeper: it stays down beside it.
6. Carry a friendly into the combiner and put it down inside: it is taken.

## Playtest: U1 discoveries in the build menu
1. `F1` for poop, `F2` unlocks every card (or research one: `F6`).
2. Press `R`: the menu now lists kitchen, library, clock, tent, combiner and the rest
   after the four basics, each with its poop price.
3. Pick Kitchen: the ghost shows with its price; red if you are short. Place one: poop is
   paid. Press `R` again: the kitchen's price has gone up.
4. Open the shop: only the van is for sale.

## Playtest: G build menu
1. Start a match: slot 1 is empty, no hammer. A lab stands by the beds.
2. `B` for wood. Press `R`: a menu shows Block, Half Block, Ramp, Bed with wood costs.
   Click Block: the ghost shows; right click places, hold to keep placing.
3. Press `R`, pick Half Block: it is half as tall. Aim at its top: the next piece goes
   in the cell above. Aim at a cell that holds one: refused.
4. Press a number key or scroll: the ghost goes away and the hotbar item is back.
5. Hold left click on a block: gone in a quarter second, one wood drops. On a bed: one
   second, five wood drop. On a kitchen: it drops as a kitchen.
6. Click outside the menu or press `Esc`: it closes with nothing picked.

## Playtest: F quarter cells, flat ground
1. Start a match: the ground is one flat plane. Trees and wild crops still stand on it.
2. `B` for wood. Hammer in hand, aim at the ground: the ghost is a 0.5 m cube. Place a
   few; they line up on one grid wherever you start.
3. Build a wall 4 cells high with a 3-cell gap: creatures walk through. Close it to 2
   cells: they stop.
4. Place a bed: it is 2 x 1 m and lies along the way you face. Turn 90 degrees and place
   another: it turns, and nothing can be built through either.
5. Buy and place a kitchen and a tent (`F2`, `F1`): same size as before, blocks snap
   against their sides.

## Playtest: D2d start beds, watering off
1. Start a match: the shop stands east of the well with 3 beds in a row beside it.
2. Hurt a friendly (`F12` starts a fight): it walks to one of the beds and sleeps.
3. Hold left click on a start bed for a second: it comes out like any bed; place it again.
4. Plant a seed or a sapling: it is not grey and grows without water.
5. Feed the frog its corn: no watering can drops, and the tips move on.

## Playtest: D2a hold to break
1. Left click a creature: nothing happens. No swing, no knockback.
2. Aim at a grown tree and hold left click: the axe shows and chops; after 1 second the
   whole tree breaks, logs lie at the stump, a sapling stands in the same cell.
3. Let go before the second is up, or look away: nothing breaks, and the next hold starts
   from zero.
4. `B` for wood, place a row of blocks with the hammer, then hold left click and sweep
   along them: one block per second comes out as an item where it stood.
5. Hold left click and sweep across ripe crops: each is harvested on contact.
6. Hold on a sapling for a second: it comes out as its item.

## Playtest: A + B + C + E
1. You start with the hammer in the hotbar. Cheats on: `B` gives 99 wood.
2. Hold the hammer and aim at the ground: a ghost fills the cell under the crosshair, with
   the piece name and wood cost above it. Right-click places; hold to keep placing.
3. `R` cycles block, ramp, fence, bed.
4. Aim at a block's top or side: the ghost sits in the cell touching that face.
5. Check the three pains: wrong cell or side, wrong height, misaligned neighbours.
6. Click a block's side with a ramp: it leans on that block. Walk up it; watch a creature
   use it.
7. Build on a slope; build a wall with a one-block gap and watch creatures use the gap.
8. Spend all your wood: the ghost goes red.
9. Place a bed. `F2` unlocks every card and `F1` gives poop: right-click near the shop
   (east of the well), buy a kitchen. It should be in your hand with the panel closed;
   aim and place it. Check creatures still rest and cook.
10b. Buy a clock, a tent, a combiner the same way: each lands in hand and places as a ghost.
   Wind the clock, breed in the tent, fuse in the combiner (axe hit fires the button).
10c. Fill the well's poop goal: no card panel opens; the next goal arms by itself.
11. Research: `F6` drops a fuelled lab beside you and makes the herd smart. Watch a creature
    put on goggles and work it; the bar fills and a card name appears. Or do it by hand:
    build a lab with the hammer, throw poop, crops, or wood at it.
10. Left-click a piece (axe) to pick it back up.
