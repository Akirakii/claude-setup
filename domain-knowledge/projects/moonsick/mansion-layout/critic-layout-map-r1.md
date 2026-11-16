# Critic: the mansion map (plan4 + agreed changes) — layout only, round 1

Isolated critic, 2026-11-15. Scope: rooms, doors, floors, sightlines, loops, chokepoints, distances. Not the potion
rules or bots, except where the layout causes the problem.
Input: scratchpad `plan4.svg` plus the agreed changes (pantry/rat nest NE, witch's study SE, pantry door into the
cauldron room, moonbeam + bucket on the north balcony above the sign).
Numbers: scratchpad `lay4.py` (plan4) and `lay5.py` (plan5); map 46 x 28 m (x 0.072 m/px, y 0.061 m/px); sprint
8.64, wolf 11.2 (closes 2.56 m/s), a 4 m drop adds 0.8 s. Straight lines between door centres, so real paths are
~10–20% longer (assumed). Checked in code: creatures never crouch (move.gd), the stand capsule is 1.85 m and the
crouch capsule 1.15 m for everyone (actor.gd), bot nav height 1.8 m.

## Verdict
The skeleton is right: a cauldron room off the hall's north side, item rooms in four corners, a double-height hall
with balconies. Three things fail the brief: (1) the cauldron room is open from above as well as on three sides, so
builders get no cover and the leader gets a bomb perch; (2) there are dead ends ("no dead ends" is a must);
(3) every route between the west and east halves crosses the open hall, and no loop gives a human anything against
a 1.3x wolf. Plan5 fixes all three without touching the user's decisions.

## Severe
S1. **The cauldron room is exposed from everywhere, including above.** Ways in on plan4 + agreed door: a 7.9 m
  arch, the back door, the pantry door, the attic window, the open top under the north balcony, and the tunnel's
  view. The north balcony now holds the bucket and stands right over the pot: dropping in from the beam takes
  4.9 m + the fall = 1.4 s, and a leader with a bomb up there is above the stirrers, out of their reach.
  "Builders get some cover" fails; "the leader is seen in person" passes only by accident.
  Fix: close the cauldron room's upper half (double height inside, skylight only). Cut the attic window and the
  tunnel. Narrow the arch to the thesis's 6 m. That leaves 3 ground ways in (arch, kitchen door, pantry door):
  a builder can't seal them (one bear trap covers one door for 4 s), and to bomb the stir the leader must stand in
  the hall within throwing range of the arch, where everyone sees them.
S2. **Dead ends.** The back door opens into a 1.4 m alley between the kitchen and the cauldron room, not into the
  kitchen, and the alley ends at the north wall (2.4 m stub). The side passages run 7.2 m past their doors to the
  outer wall (dead-end stubs, a free corner for the wolf). With the moonbeam gone, the attic's only ways out are
  its balcony door and a one-way hole: for bots (no jump links) it's a dead end, and for a human chased in, the
  hole is the only way out.
  Fix: the back door opens straight into the kitchen; the passage doors move to the far ends; a second stair
  pantry↔attic.
S3. **The hall is the only crossing, and no loop helps a human.** From the hall's centre the wolf is ≤10.8 m (1.0 s)
  from all five ground doorways, and the only west↔east routes are the hall or the balconies above it. Plan4's
  loops are 23–36 m (wolf lap 2.0–3.2 s); a 5 m head start lasts 2 s, so the wolf just follows. Jump-downs help only
  against a bot wolf (a human wolf jumps too) and are no use to bot humans (no jump links). The brief's "loops,
  jump-down escapes and line-of-sight breaks" is unmet.
  Fix: (a) a roofed south corridor conservatory↔study, which with the agreed pantry door makes an outer ring that
  never enters the open hall (102 m, 9 s wolf lap, 4 doors into the hall: the wolf must guess);
  (b) human-only crawl/slide gaps (1.4 m high; checked: the wolf can't crouch and is 1.85 m tall): under each
  ramp and at both ends of the south corridor. Each gives a human 0.7–1.2 s per pass (wolf detour 10–14 m),
  enough to reach an item or a door. Cost: bots can't use them either (nav height 1.8 m).

## Medium
M1. **The north balcony is 1.3 m deep** and now holds the bucket, the beam, the leader and anyone passing. Widen
  it to 3 m and put a jump-down gap in its rail right over the arch: bucket→pot 10 m, 2.0 s by the drop, 35.7 m
  (4.1 s) walking via the storeroom stair (the bot route). Everyone in the hall sees the bucket leave.
M2. **Ramps clash with the balconies:** the west ramp runs under the west balcony for 3 m of its length (head
  height). Free-standing ramps in the hall fix it and add a tile loop round each (24 m) plus side jump-offs.
M3. **The back stair is 4.3 m long for a 4 m rise (43°)**: too steep to walk or for a navmesh. 7 m long in plan5.
M4. **Fights cluster in front of the arch.** With the agreed changes, rats (18 m, 2.1 s) and moon water
  (2.0 s) are next to the pot; only wolfsbane is a trip (28.6 m, 3.3 s through the hall, or 34.9 m, 4.0 s out of
  sight via the west passage and the kitchen). The three directions hold, but only the wolfsbane run crosses the
  map. Probably fine (the visible heart is the point); say it in the thesis. The bomb shelf is 25.6 m (3.0 s)
  from the arch, so the leader's bomb run crosses the hall in full view.
M5. **What the wolf can camp.** Plan4: the hall centre (S3), the alley (S2), the attic (S2). Plan5: the
  cauldron room sits on the outer ring, so stirring in the hunt is on the wolf's path (by design: risky). No
  room in plan5 has fewer than 3 ways out.

## Minor
m1. Attic has no role once the beam moved. Plan5 keeps it as a run-through room (stair + drop hole). Could hold a
  second trap spawn later; or shrink it.
m2. The potion sign hangs on the north balcony's front rail, facing the hall: readable from the hall floor and
  from the south gallery, and it points at the arch below.
m3. Readability: plan5 mirrors west↔east (kitchen/pantry, conservatory/study, storeroom/attic, two stairs, two
  ramps), so "north = potion, corners = items, south = gallery" reads at a glance.
m4. Plan4's ramp top meets the south gallery inside its footprint; plan5's ramps rise southward to the gallery's
  north edge.

## Loop table (lengths in m; lap time at sprint / at wolf speed)
| Loop | plan | m | human s | wolf s |
|---|---|---|---|---|
| arch–pot–back door–alley–hall | 4 | 24.8 | 2.9 | 2.2 |
| hall–kitchen–passage–hall | 4 | 22.8 | 2.6 | 2.0 |
| hall–conservatory–passage–hall | 4 | 28.3 | 3.3 | 2.5 |
| kitchen–passage–conservatory–hall | 4 | 35.1 | 4.1 | 3.1 |
| arch–pot–pantry door–pantry–hall | 4 | 35.8 | 4.1 | 3.2 |
| ramp up–gallery–west balcony–drop | 4 | 30.8 | 3.6 | 2.8 |
| upper ring round the hall void | 4 | 55.1 | 6.4 | 4.9 |
| storeroom–tunnel–attic–balconies | 4 | 51.3 | 5.9 | 4.6 |
| arch–pot–kitchen door–kitchen–hall | 5 | 34.1 | 4.0 | 3.0 |
| north: kitchen–cauldron room–pantry–hall | 5 | 58.2 | 6.7 | 5.2 |
| west: hall–kitchen–passage–conservatory–hall | 5 | 44.5 | 5.2 | 4.0 |
| south: conservatory–south corridor–study–hall | 5 | 67.8 | 7.8 | 6.1 |
| **outer ring, never in the open hall** | 5 | 101.7 | 11.8 | 9.1 |
| tile round one ramp (crawl gap under it) | 5 | 24.1 | 2.8 | 2.2 |
| ramp up–gallery–west balcony–drop | 5 | 19.9 | 2.3 | 1.8 |
| kitchen stair–storeroom–N balcony–drop at arch | 5 | 39.1 | 4.5 | 3.5 |
| both stairs: storeroom–N balcony–attic–pantry–cauldron room | 5 | 71.3 | 8.3 | 6.4 |
| W ramp up–gallery–E ramp down | 5 | 32.1 | 3.7 | 2.9 |
No loop outruns the wolf by length alone (it closes 2.56 m/s on any of them); what helps is many exits (the wolf
must guess), the crawl/slide gaps and the drops (against a bot wolf), and items on the way.

## What changed in plan5 (scratchpad `plan5.svg` / `plan5.png`, red numbers)
1. Back door opens straight into the kitchen (alley removed). (S2)
2. Pantry door into the cauldron room (agreed). (brief)
3. Arch 7.9 → 6 m; 3 ground ways in, none from above. (S1)
4. Passage doors at the far ends; no stubs. (S2)
5. Roofed south corridor conservatory↔study, door to the hall in the middle: outer ring 102 m. (S3)
6. Ramps free-standing in the hall, a crawl/slide gap under each; pillars for line-of-sight breaks. (S3, M2)
7. Stairs 7 m long; a second stair pantry↔attic. (M3, S2)
8. Cauldron room closed above (skylight only); tunnel and attic window cut. (S1; the tunnel was optional)
9. North balcony 3 m deep with the moonbeam; jump-down gap in its rail over the arch; sign on the rail. (M1, m2)
10. Attic kept as a run-through with stair + drop hole. (m1)
Orange marks = crawl/slide gaps (humans only), at the ramps and the south corridor's ends. (S3)
Kept from the user: cauldron room off the hall's north side, the six room roles, two floors, double-height hall with
ramps. Untested; the distances are straight-line estimates.
