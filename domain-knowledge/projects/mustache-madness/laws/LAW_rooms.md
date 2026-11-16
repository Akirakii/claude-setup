# LAW: rooms, drag building, and walls that wilds punch

Standing law for enclosed rooms. User decisions are tagged (user); everything else is an AFK
call, logged in `docs/TODO_playtest_2026_10_09.md`, for the user to audit.

## Rules
1. **Drag tools (user).** The menu's Building tab: Build, Room, Stairs, Half Block. Every drag piece is
   held: right press sets one end, release the other. Half Block lays a rectangle of half
   blocks at the start's height (released in place, one). Stairs: ramps rising 1 m per cell
   along the longer axis; one ramp at the first point, and once the drag runs, 2 steps more
   past its end (user). Wall, Block and Ramp left the menu (user); Build and the starter hut
   lay them. A wall: a diagonal drag makes an L (the X leg first, then the Z leg), 5 blocks
   stacked (5 m) on each ground cell; while a Build drag reads as a wall, the wheel sets its
   height from 1 to 7 blocks, kept for the next wall (user).
   **Room tool (user):** a drag's corners are the outer wall corners; it lays the 4 walls,
   a half-block floor inside and a half-block roof over the whole ring, each wall column
   rising from its settled foot to the roof. Ctrl + wheel sets the walls' height (1 to 7
   blocks, kept for the next room; mid-drag the plain wheel does too, Claude). A doorway sits
   in the middle 2 columns of the side nearest the player, `DOOR_HEIGHT` open under a
   one-block lintel (none at 1 high, Claude). A rect with no inside, or one Rooms would call
   too big, lays nothing. The starter hut is a Room drag with its door on -X.
   **Build tool (user):** hold right click on one corner and release on
   the other. A straight drag reads as a wall (full blocks, 5 high), a diagonal one as a floor
   or roof of half blocks; Tab flips the reading, and the ghost and caption show it first. A
   press on the upper half of a 1 m slot (a ceiling's underside) lays the floor in that upper
   half, as a ceiling (user). A right click released in place puts one piece: a half block
   where 2 or more half blocks flank the spot, else a block. Left click puts the tool away,
   as with every piece (user); so does the wheel, except while a wall drag sets its height (user).
2. **Price (user: refuse unless affordable).** A drag costs the sum of its pieces' prices over
   the cells that are free; the preview shows that total, red when short, and a short click
   builds nothing. Occupied cells are skipped, not refused (AFK: dragging over an old wall
   just fills the gaps). A wall dragged onto a platform replaces the half blocks it stands on, and
   they drop their planks (user).
3. **A room (user).** Any enclosed pocket of air, any shape (L, U, two storeys joined by a
   stairwell): floor, walls and roof built from basic pieces; furniture does not count. Bare
   ground blocks a room but is no floor: at least 90% of the floor must be built (user).
   **Openings (user):** a hole up to 4 m across in a thin shell (a door, a window, a roof
   hole) is an opening, not a leak; a wider hole leaks and there is no room. Doors and
   windows share one budget: 1 opening per 8 m² of floor, at least 1 (user). A gap the room
   surrounds (between two pillars) is part of the room, not an opening.
   **Corners (user):** a room is closed by the pieces that touch its air face to face; a
   corner column touches none, so it may be left out. A corner beside a doorway is a jamb: left
   out, the doorway opens onto the outside on two faces and leaks.
4. **Room-only pieces (user).** Medic bed, nest, jail, games table, gym, treadmill,
   lab, kitchen, library; table and chair (AFK pick, #269); bar (AFK pick, #270); chalkboard (AFK pick, teacher job). They stand only on built floor, a platform or block under the whole
   piece (user; red ghost "needs a floor"), and may otherwise be placed anywhere (user); outside a room the ghost is yellow and its caption names the first thing missing ("no roof", "the north wall has too many gaps"). Placed, they work only while
   their room stands: a broken room switches them off (occupants leave, no new users, no
   labor) and they show `🏚` until it is whole again. A room no walk from the statue gets into switches them off the
   same way, with `🚪` (AFK, a researcher stalled 10 waves at a sealed lab): a sealed room, a
   door that leads nowhere, a room with only windows (creatures need a door), and every room
   when the statue is walled in. The server judges it once per navmesh change. Outside pieces: campfire, woodpile,
   statue.
5. **Walls stop wilds (user).** Player pieces are solid to every creature. A wild takes the
   quicker way to its target (user, RimWorld-style): the navmesh path around, or straight
   through what is built, where a piece costs its punch time left; a path that stops short
   (a sealed room) goes straight on from its end. Whatever piece a wild bumps into (wall,
   block, or furniture: AFK, else it stalls forever on a bed) is the piece it punches. A
   light wild (`/light_wilds`) 1 m before a piece punches it, and turns full only when an
   open way in is quicker (AFK). A wild that stands still without punching takes the path
   (terrain is in its way). Punch time accumulates on the piece (every puncher adds to it)
   and resets at dawn (AFK: no hidden damage carried between nights); a punch does not
   change the piece (user), so the count is unseen and the piece looks whole; at
   `WALL_PUNCH_SEC` it breaks in one step (user) and drops what a player's axe would drop.
6. **The start (user).** The start medic beds sit in a starter house: two 6 x 6 m rooms side
   by side, split by one shared wall, each with a 2 m doorway on the same side, floored, 4
   blocks tall under the wall's top block (user), and a roof. The rule reads on sight from
   the first second and recruiting still works.
7. **A room breaking (AFK).** The server checks on each piece's own tick; occupants leave
   (a jailed creature leaves unreformed and calm). Clients only draw the `🏚` sign.
8. **A changed room is solved again a slice per frame (AFK).** In the running game a room
   whose shell changed keeps its old verdict until the new solve is whole (`Rooms.tick`,
   `SLICE_USEC` of work a frame, up to ~0.5 s for the largest room); a cell never asked
   before is solved at once. Why: one solve floods every air cell, 16 to 80 ms in one frame.
9. **A zone builds itself (user).** The Zone tool drags a free rect (its outer wall corners);
   a crate (a Site, one paid sign) lands outside its door-side corner, the door on the side
   nearest the player (Claude). A room piece set inside it is its anchor, free; the plan is
   the Room tool's own pieces plus the anchor, laid floor, anchor, walls by course, roof. The
   architect draws the plan as a blue ghost; once drawn and `Site.UNDO_SEC` (15 s, user) after
   the zone, the builder lays each ghost piece from the crate's logs and planks, priced as
   the player's pieces (frozen when the plan is made). One shift at a time, so the phases
   follow each other. A piece already standing in a plan cell counts as built. Every piece a
   builder lays is `creature_built`. All laid: the crate spills its stock and is gone;
   knocked down, it spills its gems and stock and the zone is gone.
   Coverage (PR 5, Claude): any room piece is an anchor and several may be set, none on another
   (one kind gives that type, 3 beds a Bunkhouse, mixed kinds Plain, per LAW_room_types); one set
   after drawing joins the drawn plan. No scaffold: a laid piece is the player's own piece. A
   punched-out piece is a ghost again and is laid again; nothing happens at dawn. A finished
   room is not kept up. An architect's skill is how tight the shell is (user): below
   `Site.TIGHT_INT` INT it leaves one wall column undrawn per `INT_PER_GAP`, never beside the
   door, the same columns for that zone every time; the player may plug them by hand.
10. **One carry contract (user: haulers).** A station `accepts` a delivery it may store, `wants`
   what it asks for now (a zone's crate: the logs its drawn pieces still need), and has `spare`
   it gives free (a woodpile's logs; never a seller's stock, Claude). A Cart Shed's hauler
   (a paid sign, `HAUL`, no INT gate) takes the neediest sink in its ring and the source with
   spare (`Carry.route`), fills its bag there bound for the sink, and delivers it; the shed posts
   only while such a route exists. A builder fetches from the same sources (`Carry.source_for`)
   when its crate cannot pay the next piece. Holding only jobs open to all still counts as
   below the gates (aspire).

## Data dictionary
| Name | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| `pattern` | enum SINGLE, WALL, FLOOR, STAIRS, AUTO, ROOM | Blueprint (static) | How a click or drag lays pieces | authored |
| `drag_start` | Vector3i or none | BuildHand (per player) | The first click of a drag | set on click 1, cleared on click 2 or piece change |
| `needs_room` | bool | PlacedBehavior (static) | The piece works only inside a room | authored |
| `Grid.revision` | int | Grid (every peer) | Bumps on every lattice change | monotonic |
| room cache | {cell: room} | Rooms (every peer) | each solve's answer for the cells it covers | a solve is dropped when a cell it read changes kind; `Rooms.revision` moves when an answer changes |
| `punched` | float s, 0..`WALL_PUNCH_SEC` | GridObject (per piece, server) | Punch time taken tonight | grows while punched, zero at dawn; the piece breaks at the cap |
| `FLOOR_PER_OPENING` | 8 m² | Rooms | Floor per allowed door or window | constant (user) |
| `ROOM_MAX_CELLS` | 750 m³ | Rooms | Largest room flooded | constant (limit) |
| `ROOM_MAX_SPAN` | 24 m | RoomConfig | Largest room edge searched | constant (limit) |
| `WALL_BLOCKS` | 5 | BuildPattern | Blocks stacked per wall cell | constant (user) |
| `room_height` | 1..7 blocks | BuildHand (per player) | The Room tool's wall height | Ctrl + wheel; kept between rooms |
| `DOOR_HEIGHT` | 4 m | BuildPattern | A Room or hut doorway's open height | constant (user) |
| `DOOR_CELLS` | 4 m | Rooms | Widest opening that is not a leak | constant (user) |
| `PINCH_DEPTH` | 2 m | Rooms | An opening is wider on both sides within this | constant (limit) |
| `REACH_CELLS` | 3000 m³ | Rooms | Air flooded past a room's openings, looking for a way around an obstacle | constant (limit) |
| `WALL_PUNCH_SEC` | 6 dilated s | CreatureConfig | One wild's punch time to break a piece | constant (pace) |

## Ownership
- Static: `pattern`, `needs_room`, the constants.
- Per player: `drag_start`.
- Derived, never stored per piece: whether a piece is in a room is pulled from `Rooms.find`
  (cached per `Grid.revision`); the Grid is the one owner of what stands where, so every
  peer computes the same answer and nothing replicates.
- Per piece: `punched` (server).

## Pipeline
1. **Lay:** pattern(start, end) -> cells and steps -> skip occupied -> price -> preview.
2. **Commit:** client pays the previewed price and sends `(blueprint, start, end)`; the server
   recomputes the same pattern and places every still-free cell.
3. **Grid change:** each piece placed or removed bumps `Grid.revision`.
4. **Gate:** beds, places and stations ask `works()` (= not `needs_room`, or `Rooms.find`
   finds a room) before any use or labor; the server evicts occupants on the piece's tick.
5. **Punch:** a wild's move collides with a piece -> `punched += dt` -> at the cap the piece
   breaks -> step 3.

Reads with no writer: none. Writes with no reader: none (`punched` is read by the break test).

## Interaction matrix
| Input \ stage | Lay | Commit | Room check | Gate | Punch |
|---|---|---|---|---|---|
| `pattern` | shapes | shapes | 0 | 0 | 0 |
| `drag_start` | anchors | anchors | 0 | 0 | 0 |
| `needs_room` | warns (yellow) outside | 0 | runs it | switches | 0 |
| room | 0 | 0 | output | on/off | 0 |
| `FLOOR_PER_OPENING` | 0 | 0 | openings allowed | 0 | 0 |
| `WALL_PUNCH_SEC` | 0 | 0 | 0 | 0 | break pace |
| `punched` | 0 | 0 | 0 | 0 | accumulates |

## Room detection (pure, testable)
`Rooms.find(cell, kind) -> {cells, openings, allowed}` or `{}`, on the 0.5 m lattice, where
`kind(c)` is AIR, BUILT (a basic piece's cell) or GROUND (under the terrain).
1. **Flood:** spread from the cell through AIR (6 face neighbours, never diagonal). A pinch stops the flood and is
   kept: an air cell whose run across x or z is at most `DOOR_CELLS` between solids, and that
   is wider on both sides within `PINCH_DEPTH` (so a corridor meeting a hall is no pinch).
2. **Leak:** a reached cell under open sky with no wall on some side means no room: "no
   roof" when reached going up, else "open to the <side>". Past `ROOM_MAX_CELLS` or
   `ROOM_MAX_SPAN`: "too big".
3. **Regions (AFK, PR 14):** group the pinches; the air past each group is flooded the same
   way, as its own region, until every enclosed region in reach is found (`REACH_CELLS`).
   Regions joined by a cycle of groups are one room: an obstacle stands between them (a
   pillar, a courtyard), so the air goes around it. Why: a pillar to the ceiling made two
   pinch bands that split a 6 x 6 m room in two, each refused for "2 openings". A group with
   enclosed air both above and below (a stairwell) joins its storeys too (rule 3, user).
4. **Openings:** any other group on no cycle (it leads outside, or is the one doorway to
   another room) is one opening; a group the room surrounds joins the room.
5. **Verify:** 90% of the room's columns stand on BUILT ("no floor"); openings <= allowed ("3 openings, a room this size allows 2").
One solve answers every room it found; the result is cached per `Grid.revision`.

Chart of the opening budget (`FLOOR_PER_OPENING` 8 m²):

| Floor | Openings allowed |
|---|---|
| up to 2 x 4 m | 1 |
| 3 x 3 m, 4 x 4 m | 2 |
| 5 x 5 m | 4 |
| 6 x 6 m | 5 |
| 8 x 8 m | 8 |

## Constant ledger
- `FLOOR_PER_OPENING` 8 m²: limit, user-set (twice the openings of the first 16 m²).
- `ROOM_MAX_CELLS` 750 m³: limit on the flood (a 12 x 12 m hall, 5 m tall).
- `PINCH_DEPTH` 2 m: limit; an opening deeper than this (a tunnel) is no doorway.
- `ROOM_MAX_SPAN` 24 m: limit on the search, about a third of the map.
- `WALL_BLOCKS` 5: limit, user-set; 5 m is taller than any creature can hop.
- `WALL_PUNCH_SEC` 6 dilated s: pace. A lone wild breaks one block in 6 s; a wave of 8 at one
  spot breaks it in under 1 s, so walls delay, they never seal (no god powers).
- `DOOR_CELLS` 4 m: limit, user-set (twice the first 2 m, the smallest gap a creature fits
  through rounded up).
- Two units (user): furniture and stations cost whole logs; only the basic building pieces
  (block, half block, ramp, and the Wall, Platform and Stairs drags) cost planks. A log is 6
  planks (user), turned into planks only when paying for a building piece; every 6 planks picked up
  fold back into a log (the Minecraft way, no crafting step).
- Wall price: 5 blocks = 5 planks per cell (user). Refund equals price (whole logs, then
  planks), so there is no wood loop. A 3 x 3 m hut costs 95 planks (14 cells x 5 blocks + 25
  roof half blocks), about 16 logs, about 4 oaks at 3 to 5 logs each.

## Known gaps
- A wall dragged around a friendly can seal it in; friendlies never punch, so the player
  breaks it out with the axe.
- Multiplayer: the client pays the previewed price; if another player filled cells first it
  overpays (the same client-pays convention as single pieces).

## Not in this slice
Counters to stacked wall layers (user: later), per-creature beds, energy.
