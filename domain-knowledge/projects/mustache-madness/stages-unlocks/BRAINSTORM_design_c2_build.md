# BRAINSTORM: c2_build design (PR 2 zone -> hut, PR 5 build coverage)

Design only (AFK /explode run, 2026-10-25). Tags: (user) = the user decided it; [C file:line] =
read in the worktree mm-stage2 (feat/room-tool f6de1965: main 86fc5fb7 plus PR 1); [A] = assumed. Shared model: `/tmp/claude-layers/stage2.md` (flags F3, F9, F11, F20 are
c2's). User decisions used: "the player chooses where it can build, the architect designs how, and
the builders build"; Shape 1 anchor zones; architect skill only (how tight the shell is); a
stockpile a builder job fills, like the kitchen's (Q4); building starts 15 s after the zone, no gem
payment, no approve button (Q2) (all user, `docs/BRAINSTORM_game_stages.md` Decisions).

## Round 2 changes (2026-10-25)
- Cites re-read on PR 1 as committed (feat/room-tool f6de1965): `BuildHand.lay:81` (adds `meta`,
  `replaces`), `laid_cost:106`, `placed_of:115`, `fits(e, space):127`, `NetworkManager._place_laid(entries):204`,
  `BuildPreview._new_ghost(scene):63`, `BuildPattern.door_side`, `DOOR_HEIGHT` in BuildPattern.
- The builder lays a piece through `NetworkManager._place_laid([entry])`, the room tool's own server
  path (fits, push-out, replaces, spawn), not a second spawn path. `_place_laid` returns the spawned pieces.
- Every piece a builder lays sets `creature_built = true` (a GridObject SAVED bool) and joins group
  `&"creature_built"` in `_ready` (c5's wild gear gate); the flag survives a save, a group alone would not.
- Stockpile "wants" vs "accepts": the site's `accepts()` stays false, so `Station.taking(LOG)` never finds
  it and choppers keep stacking at woodpiles (I do not allow a site to draw choppers' logs: a chopper
  out with a woodpile's axe would lose it at the site). The site exposes `wants(meta) -> int` (planks short,
  in logs) for c3's PR 4 contract; a builder's own logs and a player throw go in by `add_stack` / CaptureArea.
- Hazard fix in PR 2 (c3 found it): `creature.gd:1336` `_fetch_axe` casts `Station.taking(LOG)` to
  Woodpile; it becomes a Woodpile-only lookup (`GridObject.by_distance(pos, Station.GROUP, is Woodpile)`).
- ARCHITECT, BUILDER append at the end of `GameEnums.Job` (PR 4 then appends HAUL). Their JOBS rows carry
  only `req_int` as the gate, so PR 3's swap to `"school": true` + a learned trade is one edit per row;
  PR 3 also sets the trade in `/architect` and the integration test.
- Pouches: the site moves no gem out of any pouch. Its only gem flows are the player's throw onto its
  sign and the existing punch-in wage into the worker's pouch; logs are free. So no `spendable()` read
  (main has `Creature.spendable() = pouch - loot` [C creature.gd:1190]) is needed here.
- Picks (Claude, AFK): PR 2 (a) paid site, (b) free logs, (c) readouts as written; PR 5 (a) no scaffolds,
  (b) a finished room is not kept up, (c) mixed anchors give Plain per the room law.

## Round 3 changes (cold review, 2026-10-25; PR 1 is feat/room-tool f6de1965, cites re-checked there)
- Plan save: `plan` holds only {cell, step, piece, meta, cost}; `replaces` (live GridObject refs,
  build_hand.gd:96-102) is never saved. Extract `static func replaces_of(e) -> Array` from `BuildHand.lay`
  (the loop at :96-102, used by lay and by Site labor); the builder rebuilds it right before `_place_laid([e])`.
- Price: each entry's `cost` {wood, planks} is frozen from `Blueprints.build_cost(piece)` when the plan
  is made, so later builds (growth, :349) do not move it. `_net_request_anchor` refuses an anchor whose
  blueprint is locked (`build_cost` reads 0 for it, :342-344) or costs gems.
- Stock unit: the site holds `logs` and `planks`, as the player's hand does. A wood cost spends logs; a
  plank cost spends planks, then opens a log into `BuildHand.PLANKS_PER_LOG` (6) planks. One pure helper
  `BuildHand.split_pay(logs, planks, cost) -> {logs, planks}` is extracted from `BuildHand.pay` (:59) and
  used by the player and the site, so both pay one way. `need()` and `wants(LOG)` are counted in logs.
- Builder stock: labor draws the crate's stock directly (no armful of planks). The builder's own fill
  takes logs from a woodpile's `stack_of(LOG)` into `job.hold`, delivers with `site.add_stack`, no gem;
  no `bag_from(basket: Basket)` and no farmer pay.
- One site, one shift (punch_in only when not `wage.paid()`, grid_object.gd:131-137): the phases run
  one after the other: BUILDER posts only once `drawn == plan.size()`. So one worker holds the site at a
  time. A shift is the site's open time: a builder that starts while the architect's shift still runs works
  out that shift, then punches in for the next gem (a gem pays open hours, not a role).
- Save/load: `window` lives in `SITE_SAVED` as a Cooldown (`_until`, cooldown.gd:12) on `wage.clock`,
  whose `time` Wage already saves (wage.gd:7), so the time left survives a load. `_ready` calls `_repost`.
- Integration test: zone 8 x 6 cells, walls 3 high (67 pieces), stock pre-filled, window cleared, cap
  120 s real; the builder's woodpile fetch gets its own short test.
- Confirmed (build_pattern.gd `_room`): a ring wall never sits on the site's own floor. Floor half blocks
  are only off the ring or in the doorway, where walls start at `door_top`, so `replaces` never axes them.
- For PR 7 (c4's handover): a finished or broken site with a valid `proprietor` sends its stacked sign
  gems to the first built Bed's till instead of the floor, so a founder's capital never becomes a player pickup.

Frame for both PRs: a site is one more workplace (a Station with a sign) whose work happens at a
moving spot, and whose plan is the room tool's own piece list. Nothing new prices a piece, pays a
worker, or carries stock: each reuses the stage 1 path that already does it.

### PR 2: Stage 2 skeleton, zone -> hut
- **Frame:** the player says "a bedroom here" with one drag and one bed, and watches the herd turn
  it into a closed pink room with no piece laid by hand.
- **Assumptions to verify:**
  - [x] A job is held by an INT gate today, no top-stat rule: `eligible_jobs` reads `req_int` only
    [C game_enums.gd:26-32]; the board seats the most disciplined apt idle creature [C job_board.gd:281, `_better`].
    So PR 2 adds ARCHITECT and BUILDER rows gated by `req_int`; PR 3 swaps the gate for top stat.
  - [x] A job is read back from its hat (`job_of(hat)` [C job_component.gd:90]): each new job needs its own hat item.
  - [x] A non-GridObject site (a child node) is open whenever posted; its pay station is its parent
    [C job_board.gd:189, :215]. So the site must post only while paid (the kitchen's `_repost` [C kitchen.gd:29]).
  - [x] A worker punches in at its station for 1 gem a 60 s shift, the gem into its pouch
    [C creature.gd:1323-1327; wage.gd]; a sign stacks at most 4 gems (`Wage.MAX_GEMS`).
  - [x] The stocker path (restock, deliver, labor) exists for Kitchen and Bar [C creature.gd:774, :1344, :1280].
  - [x] A piece the game sets down pushes bodies out (`spawn_grid_object` with `block_cell` [C spawn_coordinator.gd:150]).
  - [x] PR 1's `BuildHand.lay(room_bp, a, b, door, height)` gives entries {cell, step, piece, meta};
    floor half blocks at `start.y`, walls of `block`, roof half blocks at `start.y + 2*height`
    [C build_pattern.gd `_room`; game.gd `hut_pieces`]. `BuildPattern.door_side(a, b, at)` exists.
  - [x] A bed needs a BuildPiece under each low cell (`on_floor` [C placed_behavior.gd:218]); its cost is
    2 wood [C blueprint_registry.gd "bed"]; a block piece costs 1 plank.
  - [x] Breaking a station spills its sign's gems (`_yeet_drops` [C grid_object.gd:332]).
  - [ ] Headless GUT at `Engine.time_scale = 4` (the game's top speed) keeps creature walking stable for the integration test.
  - [ ] The bed anchor sits at `floor_y + 1` (a half block is 1 cell tall [C half_block.tres:12]) and fits a 3 x 2 m inside.
- **Candidates (idea):**
  1. The site is a workplace: the player pays its sign like any; the 15 s is the only approval. Survives.
  2. An unpaid site; architect and builder work free. Cut: "a creature earns by working" (user pillar) and the board's one open gate.
  3. The bed's price paid by the player funds the site. Cut: a price as approval, against Q2 (user).
- **Candidates (structure):**
  A. Site Station (the crate) + two child work spots + one ordered plan with a "drawn" cursor; ghost =
     drawn plan piece on a free cell; stock = a plank count. Survives.
  B. Each ghost a real GridObject in a ghost state (RimWorld blueprints, from memory). Cut: Rooms, Grid,
     nav and wild pathing would each need a ghost check; many paths.
  C. Each ghost piece posted as a ringed job site (the woodpile's trees). Cut for now: the ring rule still
     seats one worker per station, so it buys nothing but a node per piece; kept as the many-builders TODO.
  D. The builder lays the whole room in one request once stock covers it (Factorio bots). Cut: no rise to
     watch, and PR 5's half-built state cannot exist.
  Prior art (from memory): Settlers II construction sites (carriers stock a site, a builder hammers),
  RimWorld blueprint -> frame, Factorio ghosts. A is the Settlers shape.
- **Recommendation:** A. Scene: the player picks Zone in the Build tab and right-drags a 4 x 3 m
  rectangle; a crate lands outside the side nearest the player, its label "⏱ 15". The player picks Bed
  and aims inside: the ghost is blue, caption "zone anchor"; the click spends nothing. The player throws
  2 gems on the crate. A goggled architect walks to the crate, punches in, then walks the zone: blue
  floor, the bed, then walls course by course, then roof appear a few pieces a tick. At 0 the label
  reads "🪵 0/17" (logs in stock / logs still needed, planks counted as parts of a log). A hard-hatted
  builder walks to the woodpile, bags logs, drops them in the crate (label "🪵 15/17"), walks to the
  lowest blue piece and hammers it; it turns to plank and the crate count drops. Walls rise, the roof closes, the room turns pink. The crate
  spills its spare planks and is gone. Breaking the crate in the window takes the zone back, gems pop out.
  Mechanism:
  - Plan: on the anchor, `BuildHand.lay(room, a, b, door, WALL_BLOCKS)` sorted floor, anchor, walls by y,
    roof; `drawn` counts drawn entries. A plan cell already taken (a player block) counts as built.
  - Architect spot: posted ARCHITECT while paid, anchor set, `drawn < plan.size()`; each labor tick
    `drawn += ARCHITECT_PIECES_PER_TICK` and the spot moves to the next entry. Draws during the window.
  - Builder spot: posted BUILDER while paid, the window over, `drawn == plan.size()` (phases run one
    after the other, Round 3), and a ghost left; it stands at the first ghost. Labor: if the crate's
    stock covers the entry's price, spend it (`BuildHand.split_pay`) and lay the piece; next ghost.
  - Builder fill (Q4, user): stock short and bag empty -> walk to the nearest woodpile with a
    `stack_of(LOG)`, `job.hold(log, stack.take(n))`, walk back, `site.add_stack(log, n)`. No gem, no Basket.
  - Window (F20): a `Cooldown` on the crate's own `wage.clock` (dilated, LAW_time_dilation), armed when the zone lands.
  - Price (F11): each entry's `cost` {wood, planks} is frozen from `Blueprints.build_cost(entry.piece)`
    when the plan is made (Round 3), spent like the player's (`split_pay`); a site-built bed registers as built.
- **Build sketch:**
  - `systems/engine/game_enums.gd:8` Job: append ARCHITECT, BUILDER (append keeps saved ints).
  - `entities/creatures/creature_config.gd:237` JOBS: ARCHITECT {hat pencil cap, req_int 12, interval 1.0,
    reach 1.8, anim ""}; BUILDER {hat hard hat, req_int 8, interval 1.0, reach 2.5 (flat: the roof is
    hammered from the ground [C job_component.gd:145-147])}. Hats: copy `items/content/straw_hat/` to
    `hard_hat/` and `goggles/` to `pencil_cap/` with a tint and their JobBehavior job; PR 3 restyles.
  - New `entities/builds/site/site.gd` (extends Station), `site.tscn` from kitchen.tscn (CaptureArea,
    CounterLabel, sign), `site.tres` (2x2x2 cells, not in the menu), `site_spot.gd` (Node3D, `job`,
    `labor(dir, worker)` forwards to the parent). Site state: `rect_lo`, `rect_hi`, `door`, `anchor`
    {id, cell, step}, `plan` ({cell, step, piece, meta, cost} only), `drawn`, `logs`, `planks`, `window`
    (SAVED; ghosts DERIVED). `accepts()` false (Round 2); `wants(meta) -> int`: logs short of `need()`.
    `add_stack`: log -> `logs += count`. Labor: `e["replaces"] = BuildHand.replaces_of(e)` then
    `NetworkManager._place_laid([e])`, marks the result `creature_built`. Stocker duck type: `takes(job)`
    (bag holds logs: false, deliver), `restocks()` (stock short of the first ghost, bag empty), `supplier(from)`
    (nearest Woodpile whose `stack_of(LOG)` has logs), `bag_from(pile, worker)` (free take into `job.hold`).
    `_ready`: super, then `_repost()` (a loaded site re-posts its jobs, as Kitchen). `_yeet_drops`: super,
    spill logs and planks, free the ghosts. Done (no ghost): `Jobs.release` its builder, spill stock,
    `queue_free`. Static `Site.zone_at(cell)` for the anchor test.
  - `creature.gd:1336` `_fetch_axe`: Woodpile-only lookup (Round 2). `grid_object.gd:7` SAVED: add
    `creature_built`; `_ready` joins `&"creature_built"` when set. `network_manager.gd:204` `_place_laid` returns its pieces.
  - Ghost: extract `BuildPreview._new_ghost(scene):63` + `_make_ghostly` into a static `BuildPreview.ghost(scene, mat)`
    (2 uses); `GHOST_PLAN` blue beside `GHOST_OK` [C build_preview.gd:7]. Each peer rebuilds the site's ghost
    nodes when `drawn` or `Grid.revision` changes; `plan`, `drawn`, `planks` replicate via
    `ReplicationUtil.synchronizer` (as Kitchen `crops`).
  - `creature.gd:774`: stocker also when `site is SiteSpot and site.job == BUILDER` (its parent Site);
    `:1348` drop the `as Basket` cast (stocker is Variant; Kitchen and Bar keep their typed `bag_from`);
    `_deliver_carry:1285`: a builder delivers to
    its own site (`add_stack`) before any `Station.taking` lookup, which would hand them to a woodpile.
  - `systems/progression/blueprint_registry.gd` BASICS: `{"id": "zone", "name": "Zone", "meta":
    half_block.tres, "pattern": FLOOR}` (price 0). `build_hand.gd` `_place_drag`: for "zone" send
    `_net_request_zone(start, end, door_side(start, end, player cell))`, pay nothing. `build()`: when
    `Site.zone_at(cell)` takes the piece as anchor, send `_net_request_anchor(cell, id, step)`, pay nothing.
  - `network_manager.gd`: `_net_request_zone` (server: span inside PR 1's room bounds, no overlap with a
    site rect, crate cell free outside the doorway, then `spawn_grid_object` the crate and `Site.mark`);
    `_net_request_anchor` (inside the inner floor, anchor not yet set, `room_type` non-empty, cost gem 0).
  - Config: `ZONE_UNDO_SEC 15.0` (user), `ARCHITECT_PIECES_PER_TICK 4` (weight: drawing pace).
  - `docs/LAW_time_dilation.md` registry: add "a site's undo window (on the site's clock)". Save: Site lists.
- **Tests + cheat key:**
  - `test/ci/entities/builds/test_site.gd`: plan order (floor, bed, walls by y, roof); a taken plan
    cell is not a ghost; an anchor outside the inner floor is refused, a second one too; unpaid -> no post;
    paid, BUILDER not posted before 15 s on the site clock nor while the architect draws; `wants(log)` 0
    once covered; a bed costs 2 logs, a block 1 plank (a log opened for it leaves 5 planks); entry prices
    stay as drawn after another bed is built; a locked anchor is refused; a saved and loaded site keeps its
    window's time left and re-posts; a saved plan holds no `replaces`; labor with short stock lays nothing; done spills planks and frees the crate; breaking it in
    the window spills the gems and leaves no piece; a laid piece is in `&"creature_built"`;
    `Station.taking(LOG)` never returns a site; a chopper next to a site fetches its axe at the woodpile.
  - `test_site_integration.gd` `test_one_bed_zone_ends_as_a_closed_bedroom`: time_scale 4 (restored in
    after_each), a site 8 x 6 cells with walls 3 high (67 pieces: a 2 m doorway, the bed fits the 3 x 2 m
    inside), a bed anchor, `ZONE_UNDO_SEC` window cleared, stock pre-filled, 4 gems on its sign re-paid when
    due, an INT 12 and an INT 8 creature; `wait_until` the crate is gone, cap 120 s real; assert `Rooms.find`
    at the bed is a Bedroom, every plan cell holds a piece, the player's inventory unchanged.
    `test_a_builder_fetches_logs_from_a_woodpile`: an empty site, a woodpile with 3 logs; cap 60 s; the
    crate's `logs` rises, the woodpile's stack falls, no pouch changes.
  - Cheat `/architect` ("build" folder or "jobs"): a 4 x 3 m zone ahead with a bed anchor, 4 gems on its
    sign, its full bill stocked (the simple fill until PR 4), an architect (INT 12) and a builder (INT 8).
    `/architect` registers in `HELP` [C cheat_coordinator.gd:212] and `run` [C :289] like `/gembush`.
- **Shared with other clusters:**
  - c3 (PR 3): the ARCHITECT and BUILDER rows and hats; PR 3 replaces their `req_int` gate with top stat.
  - c3 (PR 4, F9): the site wants logs through `wants(meta)`, never `accepts` (Round 2); `add_stack` is the
    delivery. PR 4 folds the builder's kitchen-stocker fetch into `Carry.source_for`; once a hauler is
    seated on a carry to the site, the builder skips its own fetch (c3's call).
  - c5 (PR 10): `creature_built` flag + group on every builder-laid piece.
  - c4: a site sign is an ordinary workplace sign (player funder slot, cap 4); a log price, if ever, is c4's.
  - c1: `BuildHand.lay` ROOM entries, `door_side`, and the ghost scene per entry piece.
- **Open questions for the user:**
  - (a) The site is a paid workplace like any (recommended), so build starts at max(15 s, first paid
    shift); or an unpaid site with unpaid workers?
  - (b) Logs at the woodpile stay free for a builder, as for the player (recommended), or a log costs its
    pouch 1 gem to the chopper on shift (stage 1's crop rule; a builder earns 1 gem a minute, so it stalls)?
  - (c) Invented readouts: "⏱ 15" then "🪵 stock/need" on the crate, a blue ghost, the "zone anchor" caption. Keep?

### PR 5: R8 build coverage
- **Frame:** a site keeps working whatever the world does to it: other room types, a night of wilds,
  a dawn mid-build; each rule gets a test so the player can trust what a half hut will do.
- **Assumptions to verify:**
  - [x] An anchor names a room type; 1-2 beds a Bedroom, 3+ a Bunkhouse, two kinds a Plain room
    (LAW_room_types rules 1-2); room-only anchors: bed, kitchen, bar, lab, library, chalkboard, jail,
    medic bed, nest, gym, treadmill, games table (`needs_room = true` in their .tres).
  - [x] A wild punches a structure piece on its way; it breaks at `WALL_PUNCH_SEC` and drops its planks;
    punch time resets each day [C grid_object.gd:355-372; creature.gd:672].
  - [x] A broken piece frees its cells, so its plan entry is a ghost again with no new state (PR 2 rule).
  - [x] Dawn calls `greet_dawn` on creatures only [C game.gd:231]; nothing at dawn touches pieces.
  - [ ] "Wilds punch scaffolds" and "half built stays half built" are brainstorm lines, not (user).
  - [ ] Architect skill (user Q3) sits here, not in PR 2: gaps from INT need PR 3's architects to matter.
- **Candidates:**
  1. Plain pieces at once, no scaffold; any one-kind room anchor; more anchors of that kind allowed while
     the site stands; nothing at dawn; a broken piece is a ghost again. Survives.
  2. A scaffold state: a frame for N ticks that breaks in one punch (RimWorld frames). Cut for now: one more
     piece state every Grid reader must know, and the blue ghost already shows "not built".
  3. Unfinished sites decay at dawn (Kingdom Two Crowns, from memory). Cut: a hidden loss the player
     cannot steer, and it punishes a slow builder twice.
  4. Sites lure wilds at night. Cut: a new targeting rule; c5 owns wilds vs builds (PR 10).
- **Recommendation:** 1. Scene: the player drags a 6 x 4 m zone and drops three beds in it: blue beds,
  and the room turns tan when it closes (a Bunkhouse). A kitchen in another zone builds a red one. Night
  falls with the roof half laid; a wild cuts across, punches a wall block out, planks drop, the hole shows
  blue. Dawn: the half roof stands as it was; the builder fills the hole, then the roof. A dull architect
  (INT 8) leaves two wall columns undrawn; the crate's caption shows the room law's own words and the
  player may plug them by hand (a taken plan cell counts as built).
  Mechanism: anchors list instead of one (`anchors: Array`), each one-kind check delegated to the room law
  (a second kind is allowed and yields Plain, as LAW_room_types rule 2 says; no new refusal). Gaps =
  `clampi((ARCHITECT_TIGHT_INT - INT) / INT_PER_GAP, 0, ...)` wall columns, seeded by site, never beside the
  door, decided when the architect draws them (its INT then). After done the site is gone: a finished
  room is not kept up (the player repairs, or a later rule).
- **Build sketch:**
  - `site.gd`: `anchor` -> `anchors` (save list), `_net_request_anchor` accepts any `needs_room` piece with a
    room type that fits the inner floor; plan sorts anchors after the floor.
  - `site.gd` architect labor: skip a wall column whose (x, z) is in `gaps(int)`; `Rooms.why_not` caption on
    the crate label when the room is refused.
  - Config: `ARCHITECT_TIGHT_INT 20` (limit), `INT_PER_GAP 4` (weight). No other code: the ghost refill,
    the dawn and the punch rules already hold by PR 2's design; PR 5 pins them with tests.
- **Tests + cheat key:** `test/ci/entities/builds/test_site_rules.gd`:
  - `test_three_bed_anchors_build_a_bunkhouse`, `test_a_kitchen_anchor_builds_a_restaurant` (plan
    driven by direct labor calls, then `RoomSkins` type).
  - `test_a_laid_piece_is_an_ordinary_piece` (no scaffold: same scene, same punch time).
  - `test_a_punched_out_piece_turns_ghost_and_is_refilled` (`take_punch` past the cap, then one labor).
  - `test_a_new_day_leaves_a_half_built_site_as_it_was` (advance `day_cycle`, pieces and `drawn` same).
  - `test_a_finished_room_is_not_rebuilt` (crate gone, a broken wall stays broken).
  - `test_architect_gaps_by_int` (INT 20: 0 gaps; INT 12: 2; never beside the door).
  - Cheat `/site`: a half-built 6 x 4 m bunkhouse site (3 beds, walls 2 high), a builder, 30 planks; then
    `/night` shows a wild punching it.
- **Shared with other clusters:** c5 (PR 10): ladders and rams act on any piece; a site only needs "a
  broken piece frees its cell". c3 (PR 3): architect INT is the only skill read here.
- **Open questions for the user:**
  - (a) No scaffolds, pieces go in whole (recommended), or a weak frame stage a wild breaks in one punch?
  - (b) A finished room is not kept up by its site (recommended), or the plan stays and builders refill
    holes forever (Factorio ghosts)?
  - (c) Mixed anchors make a Plain room as the room law says (recommended), or the zone refuses a second kind?

### Old design updates (docs/BRAINSTORM_design_r7_r8_build_r5_needs.md, edited in place)
- Added "Round 4 changes" at the top: main has no sign-to-sign pay (a supply is bought pouch to pouch
  from the seller on shift), a sign stacks at most 4 gems, the plan comes from PR 1's room tool, the
  stock counts planks priced by `Blueprints.build_cost`, the vault payer still tops up a due sign.
- R7 Site concept: cut "1 gem from its sign to the supplying woodpile's sign per log delivered (rule 3)".
- R7 scene: "with each log a gem hops from the crate's sign to the woodpile's sign" -> free, no gem moves.
- R7 mechanism: cut the per-log `pay_supplier` and its "paid at delivery" line.
- R8 Builder shift: "the woodpile was paid at delivery" -> no gem moves at placement or delivery.
- Every (user) line kept verbatim (Shape 1, Payment rules 1-4 citation, `ZONE_UNDO_SEC 15`, `/architect`).
