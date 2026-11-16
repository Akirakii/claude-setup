# BRAINSTORM: design for c6 stage 3 (PR 11 skeleton, PR 12 design log)

Design only. Lines tagged (user) are the user's; every other pick is Claude's, proposed.
Model: `/tmp/claude-layers/stage2.md` (framing B, money circuit, with A's carry contract as its
stock half). Prior art is from memory unless linked: Minecraft minecarts (rails are blocks, a
cart reads the next rail block), OpenTTD (track tiles, two stations, "full load" orders),
Factorio (train stops, inserters load wagons, wait "until full or inactive"), Transport Fever
(lines between towns), Mini Metro (the player draws lines), Anno (off-screen trade routes).

## Design pass: what stage 3 rests on (resolves Q5's rest, F12, F13, F16)
- **Q5 land (user part):** "the player connects several cities they build"; no reason for a
  second one yet; later maps give one (ore, oil). **Proposed rest:** one continuous map, every
  city simulated live (no off-screen summary: a summary city breaks "cities they build" and
  rule 20, items move on screen). Land grows only when the player builds toward it (a track
  reaching the map edge grows that side; `ProceduralTerrain.grow_by` re-meshes and rebakes,
  procedural_terrain.gd:107, used by the old map growth, #174). PR 12 logs it, PR 11 does not
  need it: the 60 x 60 m map fits a 30 to 40 m line (level_02.tscn:26).
- **What a city is (PR 11):** not an object yet. City A is the land a loading stop serves, city
  B the land an unloading stop serves. A city object is only needed once tags exist (PR 12).
- **F12, rail vs the carry contract:** one contract. The loading stop is a sink (wants X), the
  unloading stop is a source (has X); c3's haulers and today's delivery path feed and empty them.
  The train is a second carrier between one sink and one source, never a second contract.
- **F13, land claims:** one rule from a (user) line: "the player chooses where it can build".
  A creature (founder, buyer) claims only land inside a player zone, never outside; inside a
  zone the first claim holds the cell; the player's own pieces and zones always win.
- **F16, tax and trade vs pre-pillar 1:** both pass only if they move gems that exist (pouch to
  sign, pouch to player) and never mint. So no outside market buys goods for new gems; trade
  pays creature gems city to city, and a tax is collected by a piece the player places.

### PR 11: Stage 3 skeleton (a second city site, one rail line moving logs A -> B)
- **Frame:** goods cross distance only in a hauler's 15-item bag today; the player should lay a
  track between two stops and see a cart carry a pile of logs from city A to city B on its own.
- **Assumptions to verify:**
  - [x] No path-follow exists (no Path3D/PathFollow3D/Curve3D in the repo); a cart is new.
  - [x] Stock is floating DroppedItem stacks at a Station; `accepts` = takes a delivery,
    `add_stack` stacks it (station.gd:54-80). Choppers deliver to the nearest `Station.taking`
    (creature.gd:1285). PR 4 (merged before PR 11) adds Station `wants/spare/sells/hand` and
    `Carry.route(shed)` / `Carry.source_for` (c3 doc, PR 4 build sketch), and keeps the axe
    fetch at the nearest Woodpile only, so a loader beside the pile takes logs, not the axe.
  - [x] Every Station gets a `Wage` sign (station.gd:19-21); `wage = null` means no sign and no
    PAID group (grid_object.gd:62-65). `punch_in` takes a gem and starts a 60 s shift on the
    station's dilated clock (grid_object.gd:128-137, wage.gd:5, 33-41).
  - [x] Pieces sit on a 0.5 m lattice; a half block is block_size (2,1,2), 1 x 0.5 x 1 m, layer
    132 = INTERACTABLE + STRUCTURE (half_block.tres, half_block_placed.tscn); `Grid.get_block`
    finds a piece by cell (grid_manager.gd:183), with or without a collider.
  - [x] Walking over the track is set by its collision layer, not its height: creatures collide
    with WORLD | STRUCTURE only (creature.gd:570); a punch (and c5's ram) needs a slide hit on a
    STRUCTURE piece (creature.gd:672-679); the navmesh bakes static colliders on mask 129 = WORLD
    | STRUCTURE (level_02_navigation_mesh.tres: parsed_geometry_type 1, collision_mask 129); the
    hand's aim ray hits WORLD | INTERACTABLE (aim_component.gd:16, layers.gd:3-13). So a track
    on INTERACTABLE only is aimed at and broken by the player, never bumped, punched, rammed or
    baked: wilds and creatures walk over it (Q7, user). Its 0.1 m look is also under the navmesh
    agent_max_climb 0.5 m, so even a mistaken STRUCTURE layer would not cut a path.
  - [x] PR 1 is committed (feat/room-tool f6de1965): `BuildPattern.lay` match at
    build_pattern.gd:22, WALL L-drag :23-32, ROOM :49, default :51; room entries carry "piece"
    (:83-89) and `BuildHand.lay` turns "piece" into "meta" (build_hand.gd:93-94); Pattern enum
    blueprint.gd:8.
  - [x] A `wage = null` Station crashes today: `Station._physics_process` calls `_tick_pay`
    every frame (station.gd:29-32) and `_tick_pay` calls `wage.advance` unguarded
    (grid_object.gd:95-97). OfferPlace already guards it (`if wage:`, offer_place.gd:254).
    Save: a null field encodes as null and `apply` sets it back (save_fields.gd:29-43, 113-131);
    a round-trip test pins it.
  - [x] Rooms and skins read the Grid, not colliders: `Grid.room_cell` returns BUILT for any
    `BuildPiece` in `_blocks` (grid_manager.gd:230-234), and RoomSkins skins only BuildPieces
    (room_skins.gd:104, 110). A BuildPiece rail would count as built cells (a floor inside a
    room, a low lump in a doorway). `block.gd` is only `extends GridObject` + `class_name
    BuildPiece`, so a rail script that extends GridObject directly reads as AIR to Rooms, is no
    platform for the build hand (build_hand.gd:133), and breaks at the plain rate
    (grid_object.gd:396), while `Grid.get_block` still finds it by cell.
- **Candidates:**
  1. Track pieces on the block lattice, a breadth-first route from stop to stop, a cart riding
     the cell centres (Minecraft, OpenTTD). Survives.
  2. A spline drawn between two stops (Transport Fever). Cut: a new placing verb off the
     lattice (LAW_game_design: build the interface from verbs the game has).
  3. Goods vanish at A and appear at B after a timer (Anno). Cut: rule 20, a remote counter.
  4. The cart as a nav agent on the navmesh. Cut: it ignores the track the player laid.
  5. No rail, haulers walk the distance. Cut as the PR; it is the baseline rail must beat.
  Departure: full load only (cut: a trickle never ships), a timetable (cut: a clock rule), leave
  after a short dwell with any load while the line is paid (survives, Factorio's "or inactive").
- **Recommendation (1).** Scene: by the woodpile the player sets a hopper (Rail Loader) and
  drags a track 35 m across the meadow to a plank dock (Rail Unloader). A chopper drops its logs
  into the hopper; later a porter from a cart shed tops it up from the pile. The player throws a
  gem at the hopper's sign; the cart takes it, a log pile pops onto the cart, it rattles down the
  line, tips the logs onto the dock as a floating stack and rolls back. A wild trots across the
  rails without a bump. The player walks into the stack and takes the logs, or a city B porter
  carries them on. No gem: the cart waits and the sign asks for one. Mechanism: the loader owns
  one Train; idle at the loader with logs stacked and the line open (`on_shift()` or
  `punch_in(null)`), after TRAIN_DWELL it takes up to TRAIN_LOAD logs, finds the route, rides
  to the unloader, `add_stack`s the load there, rides back. A trip under way finishes even if
  the shift ends. A track piece gone mid-ride: the load spills as a DroppedItem where the cart
  stands and the cart resets to the loader. No route: the cart stays.
- **Build sketch:**
  - `entities/builds/rail/rail.gd` (`class_name RailPiece extends GridObject`, not BuildPiece:
    Rooms and RoomSkins skip it), `rail.tres` + `rail_placed.tscn`, block_size (2,1,2), mesh 1 x 0.1 x 1 m (sleepers and two rails), collision box of the same size on
    `collision_layer = 4` (INTERACTABLE only, never STRUCTURE).
  - station.gd:29-32: `if wage: _tick_pay(delta)` (as offer_place.gd:254), so a sign-less
    Station runs.
  - `blueprint.gd:8` add `Pattern.LINE`; build_pattern.gd:22 match gets `Blueprint.Pattern.LINE:`
    beside ROOM (:49), reusing the WALL branch's feet with `height = 1` (no "piece" key: every
    entry is the rail's own meta via build_hand.gd:93).
  - `entities/builds/rail_stop/rail_loader.gd` (RailLoader extends Station): `accepts(meta)` =
    LOG (choppers via `Station.taking`); `wants(meta)` = LOG ? TRAIN_LOAD minus logs held : 0,
    and 0 while not `paid()` (haulers via `Carry.route`); `spare` 0. Owns `train` (child,
    `top_level`); `LOADER_SAVED := ["aboard"]` (the load restarts at the loader).
    `rail_unloader.gd` (RailUnloader extends Station): `_init` sets `wage = null`; `accepts`
    false, `wants` 0, `spare(LOG)` = its log stack count, `sells()` false, `hand` the base free
    take, so `Carry.route` and `Carry.source_for` treat it as a free source. A .tres + .tscn
    each, copying woodpile's.
  - `entities/builds/rail_stop/train.gd` (Train extends Node3D): own LocalClock, advanced every
    physics frame; speed TRAIN_SPEED x clock modifier. `static func route(loader) -> Array`
    breadth-first over `RailPiece` cells (step 2 cells on x/z, same y, cap RAIL_MAX_CELLS), seeds =
    rail cells within STOP_REACH of the loader, ends at the first cell within STOP_REACH of a
    RailUnloader; returns [points, unloader] or []. Log pile mesh visible while `aboard` > 0.
    Replicate position + aboard count (ReplicationUtil.synchronizer, as statue.gd does).
  - Constants on Train: TRAIN_LOAD 45 (limit, 3 bags), TRAIN_SPEED 6.0 m/s (weight), TRAIN_DWELL
    3.0 s (limit), STOP_REACH 1.5 m (limit), RAIL_MAX_CELLS 4000 (limit). Probe tally `static
    var shipped` (units unloaded), read at balance_probe.gd:737 as "rail_shipped".
  - `blueprint_registry.gd` BASICS: "rail" (BUILD, LINE, 1 plank), "rail_loader" and
    "rail_unloader" (WORK, logs like the woodpile's entry), all in the menu from the start.
  - `docs/LAW_time_dilation.md` registry: add "a train's ride and dwell (on the train's clock)".
  - README feature checklist: one line, rail line.
- **Tests + cheat key:** `test/ci/entities/builds/test_rail.gd` (scaffold as test_woodpile.gd):
  - `test_goods_leave_city_a_and_arrive_in_city_b` (Done): loader paid 1 gem, 20 logs stacked
    at it by `add_stack` (no filler, so the test isolates the rail; the fillers have their own
    tests below), a straight track 30 m to an unloader; step `train._physics_process(0.1)` until
    back or a cap; loader holds 0 logs, unloader a 20 log stack, train aboard 0, `Train.shipped`
    +20, loader-unloader distance >= 24 m.
  - `test_a_chopper_drops_logs_in_the_loader`: loader nearer than the pile: `_deliver_carry`
    stacks at the loader; `Station.taking` never returns an unloader.
  - `test_a_hauler_fills_the_loader`: paid cart shed, woodpile with 20 logs and a paid loader in
    its ring: `Carry.route(shed)` returns [woodpile, loader]; an unpaid loader wants 0, no route.
  - `test_the_unloader_is_a_free_source`: unloader holding 10 logs: `spare(LOG)` 10, `sells()`
    false, `Carry.source_for` finds it for a sink wanting logs.
  - `test_an_unpaid_line_waits`: no gem: logs stay, train at the loader.
  - `test_route_turns_corners_and_a_gap_has_none`: an L track routes end to end; one piece
    removed: `route` returns [].
  - `test_a_broken_track_spills_the_load`: remove a piece mid-ride: a DroppedItem of the load.
  - `test_track_is_walked_over_not_punched`: the rail's `collision_layer & Layers.STRUCTURE`
    is 0 and `& Layers.INTERACTABLE` is not; a wild pushed across a rail cell gets no slide
    hit on it (`_punch_bumped` leaves the piece's `punched` at 0).
  - `test_a_signless_unloader_ticks_and_saves`: an unloader runs `_physics_process` without
    error; `SaveFields.capture` then `apply` on a fresh one leaves `wage` null (no sign, not in
    `GridObject.PAID`).
  - `test_rail_is_not_a_room_cell`: a rail cell gives `Grid.room_cell` AIR; a hut with a rail
    laid through its doorway and across its floor keeps the same room result as without it.
  - `test_a_drag_lays_a_one_high_line`: `BuildPattern.lay(LINE, ...)` = L feet, 1 high, no
    "piece" keys.
  - Cheat `/rail` (world folder, cheat_coordinator.gd HELP + `run` match): a paid loader with 30
    logs ahead, a woodpile and a chopper (INT 8) beside it, a straight 30 m track along +X, an
    unloader at its end (city B's site), and 20 planks to drag more track. A blocked cell prints
    which cell refused.
- **Shared with other clusters:**
  - c3 carry contract, names as c3 owns them: the loader overrides `wants`, the unloader `spare`
    (with the base `hand` and `sells()` false); haulers reach both through `Carry.route` and
    `Carry.source_for`. The train is c6's carrier between them, not a second contract.
  - c1 `BuildPattern`: LINE is one more case in the match PR 1 extended (build_pattern.gd:22).
  - c4 gem flows: the line's gem is a shift with no worker, so it leaves the economy (a sink);
    c4 rules any sign cap (see c4's doc, F2).
  - c2 zones and c4 founders: the F13 rule above (creatures claim only zoned land).
  - c5 threats (rams and ladders hit every piece): consistent by shape, no skip rule; a wild
    never touches the track (INTERACTABLE only, above), so there is nothing to ram.
- **Picks (Claude, AFK, round 2):** the line needs a paid sign on the loader; rail is in the
  menu from the start (its gate is a TODO line); the loader takes logs only.

### PR 12: Stage 3 design for later (content of `docs/TODO_stage3.md`, not built)
- **Frame:** stage 3 hands "what ships where" to creatures; each later piece must raise
  productivity per player decision (one line feeds a city) and pass "no rule names a stage".
- **Assumptions to verify:** [ ] PR 11 merged (route, stops, train); [ ] c3 haulers merged
  (`wants`/`spare`); [ ] c4 founders and rent merged (owner, landlord); [x] prices are fixed
  constants today (`CreatureConfig.CROP_PRICE`, basket.gd:65); [x] `grow_by` grows every side
  at once (procedural_terrain.gd:107); one-sided growth is new.
- **Candidates (city holder, the fork every later item rests on):** 1. a city stone the player
  places, its city = stations nearer it than any other heart (survives); 2. the rail stop is the
  city (cut: home has no stop until rail, a city must exist first); 3. a statue per city (cut:
  doubles the run-loss object); 4. navmesh islands joined only by rail (survives as the later
  map shape, "later maps give one", user Q5).
- **Recommendation:** the TODO below; each item names its pick.
- **Build sketch:** none (TODO only). The builder copies the block below verbatim.
- **Tests + cheat key:** none until an item is built; each item lists its Done line.
- **Shared with other clusters:** c3 (carry jobs), c4 (sign and pouch flows, landlords), c2 (zones).
- **Picks (Claude, AFK, round 2):** City Stone (not navmesh islands), the branch reward (not a
  dividend), land-sale gems to the player (not a sink), the Tax Office (not a toll). The TODO
  block below carries them as picks.

```
# TODO: stage 3 (designed, not built; picks are Claude's until tagged (user))
Design: docs/BRAINSTORM_design_c6_stage3.md. Rules: a capability opens when what enables it
exists (user); trains carry resources and creatures (user Q6); wilds walk across rails (user Q7).

- [ ] City heart. A City Stone the player places names a city; a station belongs to the
  nearest heart (the statue for home). No health, not a raid target. Fork: stone, or navmesh
  islands on later maps (Claude picked the stone). Done: stations report their city in a test.
- [ ] City tags (user seed: "status or city tags that create their own mood or effects"). A tag
  derives from the city's stations, as an anchor names a room's type: most WORK -> work town,
  most FREE_TIME -> party town, most STAY -> sleepy town. Each tag: one moodlet on its
  residents + one effect (work town: shifts longer; party town: fun fills faster). Shown on the
  stone. Done: a party town's resident gets the moodlet.
- [ ] Land growth (Q5 rest). A track piece laid at the map edge grows the land on that side
  (one-sided `grow_by`); every city stays live, no summary. fps risk logged per growth.
- [ ] Train loader jobs (user: "loading and unloading trains"). Reuse c3's hauler: a cart shed
  whose ring holds a stop loads it (stop = sink) or empties it (stop = source). No new job.
- [ ] Trade prices. A city's price for a kind rises as its stations hold less of it; a shipped
  unit is paid sign to sign (receiving workplace pays the shipping one) at the receiving city's
  price. No outside market, no minted gem (pre-pillar 1). Fork with c4's payee rules.
- [ ] Creatures ride (user Q6). A creature with a job in another city rides the train to it; a
  car seat is the shared space (sacrifice: seats vs cargo). Fork: commuters vs movers only.
- [ ] Startups (Q9, needs design, user). Rec: a startup is a founder's shop (c4) the player backs
  by paying its sign; backed past N shifts it opens a branch in another city on its line (a board
  change, no dividend, no shares, no exchange board: resource pile + menu-driven).
- [ ] Land purchase (user frame: creatures buy land). A creature with a full pouch buys an
  unclaimed cell group inside a player zone (F13: creatures claim only zoned land) and owns it
  (the landlord c4's rent needs). It walks its gems to a Land Office the player placed; the gems
  go to the player (Claude pick, not a sink).
- [ ] Tax lever. A Tax Office the player places: residents in its ring above a full pouch walk
  in one gem per day. The lever is where and how many offices (placement), never a rate menu.
  Income is capped by the creatures in rings (pre-pillar 2).
- [ ] Wilds vs trains (Track D). A wild on the track is sent flying by a cart (goofy, no block).
- [ ] Rail gate: what enables rail (rail is in the menu from the start for the skeleton). Rec:
  it opens when a second city's land exists (a City Stone placed, or the land grown).
- [ ] Rail later: slopes and bridges, more carts per line, switches, a stop that loads any kind.
- Balance questions (log, no tuning): TRAIN_LOAD 45, TRAIN_SPEED 6, the line's gem as a sink.
```

## Round 2 changes (2026-10-25, from the relay)
- Picks recorded (Claude, AFK): loader sign; rail in the menu from the start with a gate TODO;
  logs only; PR 12: City Stone, branch reward, land-sale gems to the player, Tax Office.
- c3 names used exactly: Station `wants/spare/sells/hand`, `Carry.route`/`Carry.source_for`;
  the Done test fills the loader by `add_stack` (rail isolated); chopper (`Station.taking`) and
  hauler (`Carry.route`) fills get their own tests.
- Track vs rams resolved by shape: collision on INTERACTABLE only, so creatures never collide,
  punch or ram it and the navmesh never bakes it (creature.gd:570, 672-679; nav mask 129;
  aim_component.gd:16); the c5 skip rule is dropped.
- PR 1 lines cited from f6de1965 (build_pattern.gd:22, 49, 83-89; build_hand.gd:93-94).
- The sign cap clash is c4's; this doc keeps only a pointer.
- New tests: hauler fill, unloader as a free source, track walked over not punched.

## Round 3 changes (2026-10-25, cold review)
- SEVERE fixed: a `wage = null` unloader crashed `_tick_pay`; station.gd:29-32 gets the
  `if wage:` guard OfferPlace already has (offer_place.gd:254); a tick + save round-trip test.
- MED fixed: a rail piece is a `RailPiece extends GridObject`, not a BuildPiece, so
  `Grid.room_cell` reads it as AIR (grid_manager.gd:231) and RoomSkins skips it
  (room_skins.gd:104, 110); a test keeps a hut's room result with rail through it.
- PR 1 cites re-checked against f6de1965 (the real commit): build_pattern.gd:22, 23, 49, 51,
  83-89; build_hand.gd:93-94; blueprint.gd:8 all hold.

## Old design updates (`docs/BRAINSTORM_game_stages.md`, every (user) line kept verbatim)
- Section 1 fact table: added a row for the stage 1 economy (gem bushes, 1 gem per 60 s shift, 4
  stacked, pouches) [C: wage.gd:4-13].
- Shape 3: noted the gem-as-architect-wage is superseded by Q2 (user, no gem payment).
- Market arc: stage 1 row "builds stations and gem bushes; pays signs by time"; stage 2 founder
  "with a full pouch (the pouch is enough, user 2026-10-24)" replaces "traits, savings"; stage 3
  row: backing = paying the startup's sign, the exchange board cut as menu-driven (Claude).
- Pillar checks: the savings question marked settled by the user's "pouch is enough".
- Section 5: Q5 marked answered in part, Q6, Q7, Q8 answered, Q9 open, each pointing here.
- Economy section: the pouch-pile line now says the pouch is the capital (user); the tax line
  now points to the proposed Tax Office here.
