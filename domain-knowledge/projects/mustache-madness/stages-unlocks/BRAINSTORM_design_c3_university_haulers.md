# BRAINSTORM: design c3, university (PR 3) and haulers (PR 4)

AFK /explode design (stage 2 relay, 2026-10-25). Every pick here is Claude's unless tagged
(user). Code read on worktree mm-stage2 (`main` 86fc5fb7 plus PR 1 docs). Shared model:
`/tmp/claude-layers/stage2.md` (framing B, money circuit, with A's carry contract). Old design
updated in place: `docs/BRAINSTORM_design_r6_university_haulers.md` (list at the end).

**Frame for both:** a creature comes to hold a job only from its own state (stats, plus a
trade it earned in class), and stock moves between stations by one has -> wants carry that a
hauler, a cook, a bartender and a builder all walk on screen.

**Owned here (from the brief):** job-from-stats (F18, F21, the hiring rule c4 reuses, F17),
tuition payee (F7), the one carry contract (F9, F10, F6).
- **Job-from-stats, the rule today (job_board.gd:3-6, 79-96, 281-286):** a site posts a job; each
  poll the board seats the most disciplined jobless friend that is `apt` (INT gate, not
  resting), nearest breaks a tie; the board is the only writer of the hat. PR 3 adds one more
  input to `apt`: a learned trade. c4's founder hiring reuses this as is: the founder's shop
  posts its job, the board picks the worker; the founder never chooses who (F17).
- **Tuition payee (F7):** the professor on shift, pouch to pouch via `buy_at`, exactly as the
  chalkboard does today (chalkboard.gd:55-69). A founder-owned school's payee is c4's rule.
- **Carry contract (F9, F10):** a station that `spare(meta) > 0` (has) to a station that
  `wants(meta) > 0`; the stock moves in a worker's bag, bound for the sink. **Hauler pay (F6):**
  per shift from its own cart shed's sign, never per delivery (pre-pillar: a gem pays open
  hours, never a role).
- **Stolen gems (c5 contract):** every gem out of a pouch reads `spendable()` = `pouch - loot`
  (creature.gd:1190); `buy` refuses below the price (creature.gd:1143) and the class pull checks
  it (chalkboard.gd:44). Tuition rides `buy_at`, so loot is never spent on it; no new hook.

## Round 2 changes (relay picks, Claude, AFK; none is (user))
- PR 3 fork 1: the trade is required for ARCHITECT and BUILDER (Claude). Fork 2: track benches
  are a TODO (`docs/TODO_room_types.md` item), not this slice (Claude).
- PR 4 fork 1: HAUL `req_int 0` (Claude). Fork 2: (a) haulers skip sold stock now; crop hauls a
  TODO in `docs/TODO_job_economy.md` once c4 settles stock payment (Claude).
- PR 3 build sketch: the pre-pillar "a learned trade is kept for life" goes into MEMORY.md.
- PR 2 facts (c2 doc): ARCHITECT (req_int 12) and BUILDER (req_int 8) appended with hats
  `pencil_cap` and `hard_hat`; PR 3 swaps the gates, keeps the hats. PR 2 fixes the `_fetch_axe`
  Woodpile cast itself, so PR 4 drops that fix and its test.
- PR 4 replaces exactly PR 2's `Site.supplier(from)` and `Site.bag_from(source, worker)` (c2's
  "`takes/restocks/supplier/bag_from` as Kitchen" on site.gd); `takes` and `restocks` stay.
- Contract names fixed for c6: `accepts(meta)` = may store a delivery (a woodpile always does);
  `wants(meta)` = asks for more now (pull; RailLoader: TRAIN_LOAD minus held, 0 unpaid);
  `spare(meta)` = may give (RailUnloader: its stack count, no wage). Route and bound delivery read
  `wants`, never `accepts`.
- PR 1 (ed2ed0c9): its diff from 86fc5fb7 touches none of the files cited here; no cite moved.

## Round 3 changes (cold review mediums, Claude)
- `.:trade` replicated (client job panel reads `Jobs.apt`); `schooling` server-only.
- `below_gates` stated right: a graduate stops aspiring (intended); a hauler-only dull creature
  still aspires. Rows open to all = `req_int 0` and not `school`. Test added.
- Save VERSION: each of PR 3 (trade, schooling) and PR 4 (`sow_from` -> `bound_for`) bumps to
  stack top + 1 at build time.
- `/haul` and the stockpile test pre-draw the plan and run out the 15 s window first.
- New test: a shed ring with only basket -> kitchen posts no HAUL, burns no shift gem.
- `_haul` sits below `_fetch_gem` in the WORK branch.
- PR 1 is committed as feat/room-tool f6de1965.

### PR 3: R6 university (lectern, architect and builder trades, tuition, hats)
- **Frame:** nothing makes an architect or a builder from a creature's own state; the player
  should see a student pay its professor a gem, sit the lectern's desks, and graduate into the
  job its top stat fits: INT -> architect, STR/DEX/VIT -> builder (user).
- **Assumptions to verify:**
  - [x] Job gates read INT only: `eligible_jobs` (game_enums.gd:26-32), `apt` (job_board.gd:281-286).
  - [x] A teaching OfferPlace with desks, TEACH posted at itself, tuition once per stay to the
    teacher on shift, broke student not pulled: chalkboard.gd:41-76.
  - [x] Hats: one JOBS row per job with a hat `.tres` whose JobBehavior stores the job's enum
    int (mortarboard.tres `job = 7`), so new jobs must be appended to `enum Job` (game_enums.gd:8).
  - [x] Room type comes from an anchor's `room_type` (chalkboard.tres:14, LAW_room_types.md);
    hue rows in room_skins.gd:31.
  - [x] `below_gates` = no eligible job (creature.gd:1186), read by aspire (creature.gd:1149, 1183).
  - [x] PR 2 appends `Job.ARCHITECT` (req_int 12, pencil_cap), `Job.BUILDER` (req_int 8,
    hard_hat) (BRAINSTORM_design_c2_build.md:76-80).
  - [x] The trade is required (round 2, Claude).
- **Candidates:**
  1. Stat gate only (architect = INT top past a gate, builder = body top): the lectern just
     trains a stat fast. Cut: same purpose as gym and library; nothing "graduates".
  2. Lectern grants a saved trade at graduation, picked by the top stat then; trade-marked JOBS
     rows need it. Survives (Prison Architect programs, Two Point qualifications, ONI skill hats).
  3. Track benches: drafting tables draw INT-top students, workbenches body-top, track fixed at
     the first class (old R6 pick). Survives as the later look; cut from this slice: per-spot
     filtering adds a second seat rule for the same graduate.
  4. The diploma as a held item or a kept hat. Cut: the hat is job-holding state the board
     writes and clears; a second hat meaning breaks it.
  5. Graduation seats the creature in a job directly. Cut: a role handed out by a slot; the
     board must still match it to a posted site (roles pillar).
- **Recommendation (2).** Scene: the player puts a lectern in a hut (desks drawn as two
  drafting tables and two workbenches, user 18d); the walls take the University hue. A gem lands
  on its sign; a mortarboard professor takes its shift gem. A driven fox and a burly bunny sit
  down; 💎 hops from each to the professor. After about 3 shifts of class the fox's job panel
  lights Architect, the bunny's Builder; when PR 2's zone posts a site, the board seats them and
  the hard hat or pencil hat appears. Mechanism: `Lectern extends Chalkboard`; its class is on
  while its teacher teaches (no INT cap: the trade is the lesson); each TRAIN use banks
  `schooling += TRAIN_INTERVAL` on the place's dilated clock; at `GRAD_SEC` it sets
  `trade = TRADE_OF_STAT[top stat]` (ties go to INT) and the creature leaves the desk; a creature
  with a trade is not drawn again. Tuition reuses the chalkboard's one `buy_at` path.
- **Build sketch:**
  - chalkboard.gd:55-76: split `_use` into the shared pay step then a virtual `_learn(c)`
    (Chalkboard: `super._use(c)`, grows INT), and `_teaches(c)` into `_class_on()` plus a
    virtual `_can_learn(c)` (Chalkboard: INT below the teacher's). One tuition path, two learners.
  - New `entities/builds/lectern/`: lectern.gd (`_can_learn`: `c.trade == Job.NONE`; `_learn`:
    bank and graduate), lectern.tscn (chalkboard.tscn with the lectern and 4 desk meshes, 4
    spots), lectern.tres (`needs_room = true`, `room_type = &"university"`, chalkboard's size).
  - Creature (creature.gd:37-63 SAVED): `trade := GameEnums.Job.NONE` and `schooling := 0.0`
    beside `pouch`; save_game.gd:5 VERSION = stack top + 1 at build time. Add `".:trade"` to the
    creature synchronizer (creature.gd:349-370): the client job panel calls `Jobs.apt`
    (creature_job_panel.gd:176); `schooling` stays server-only (no client reads it).
  - game_enums.gd:26: `eligible_jobs(stats, trade := Job.NONE)`; a row with `"school": true`
    needs `trade == job` and skips its INT gate. Callers: job_board.gd:285 passes
    `creature.trade`; creature.gd:1187 `below_gates` passes it too, so a graduate stops aspiring
    (it has a job path; aspire is for a creature that cannot earn).
  - creature_config.gd:237: ARCHITECT and BUILDER rows (PR 2's) get `"school": true`; new
    `GRAD_SEC := 3 * Wage.GEM_SEC` (limit: three paid shifts of class, sized to the sign clock,
    not tuned); `TRADE_OF_STAT := {INT: ARCHITECT, STR: BUILDER, DEX: BUILDER, VIT: BUILDER}`.
  - Hats: keep PR 2's `hard_hat` and `pencil_cap` (restyle only if the look is off).
  - MEMORY.md: at the top of the pillar list, "PRE-PILLAR (unconfirmed): a job is learned once
    and kept; the stat that was highest when learning ended picks it, so later training never
    flips a creature's trade." `docs/TODO_room_types.md`: track benches item.
  - room_skins.gd:31 hue row `&"university"`; LAW_room_types.md Types row (University,
    lectern, a new hue not used by another type); blueprint_registry.gd menu entry "Lectern" (WORK tab, wood like the
    chalkboard's card) beside "woodpile" (blueprint_registry.gd:~140).
  - LAW_time_dilation.md registry: schooling banks on the place's dilated clock.
  - PR 2's `/architect` cheat and integration test: set `trade` on the spawned architect and builder.
- **Tests + cheat key:** `test/ci/entities/builds/test_lectern.gd` (helpers copied from
  test_chalkboard.gd:22-62): `test_an_int_top_student_graduates_architect` (after GRAD_SEC of
  taught ticks: `trade == ARCHITECT`, `Jobs.apt(c, ARCHITECT)`); `test_a_body_top_student_graduates_builder`
  (STR, DEX, VIT each); `test_a_tie_goes_to_architect`; `test_tuition_leaves_the_pouch_once_per_stay`
  (pouch -1, professor +1); `test_a_graduate_is_not_drawn_again`; `test_no_teacher_no_schooling`;
  `test_a_graduate_takes_a_posted_site` (post a stub Node3D for BUILDER, `Jobs.tick()`, hat on);
  `test_untrained_is_not_apt_for_school_jobs`; save round trip keeps `trade` and `schooling`.
  Chalkboard tests stay green (the split is behavior-preserving). Cheat `/university` (jobs
  folder, HELP at cheat_coordinator.gd:105, branch beside "teach" at :690): a hut with a lectern
  paid 3 gems, a professor (INT 14), an INT-top and a VIT-top student with 3 gems each, one
  broke student.
- **Shared with other clusters:** `eligible_jobs(stats, trade)` + the board's pick is THE
  job-from-state rule (c2 for architect and builder, c4 founder hiring). Job enum append order
  (PR 2 ARCHITECT, BUILDER; PR 4 HAUL) fixes the hat ints. c4: tuition at a founder's school.
- **Open questions for the user:** none left in this slice. Picked by Claude (round 2), for
  audit: trade required (a city needs a university before zones build; hand building stays);
  track benches a TODO.

### PR 4: R6b haulers (one has -> wants carry route)
- **Frame:** a site stockpile fills only by the builder's own fetch or the player's hands; the
  player should place and pay a cart shed, and watch a hauler wheel logs from the woodpile to
  the stockpile inside the shed's ring, on the same route the cook and bartender restock by.
- **Assumptions to verify:**
  - [x] Carry today: the bag `path -> count`, `sow_from` binds a farmer's bag to its basket
    (job_component.gd:16-84); `_deliver_carry` goes to the nearest `Station.taking`
    (creature.gd:1280-1301); WORK branch at creature.gd:768-800.
  - [x] Cook and bartender self-restock by buying at the nearest selling basket, paying the
    farmer on shift (kitchen.gd `supplier`/`bag_from`, bar.gd:115-130, basket.gd:41-83).
  - [x] Woodpile logs are free stacks at the station (woodpile.gd, station.gd `stacks()`).
  - [x] One job per site (job_board.gd:10); a non-ring site that has a wage pays its own worker
    (job_board.gd:179-189 `station_of`); a sign takes one gem per shift (wage.gd:34-43).
  - [x] Hazard: `_fetch_axe` casts `Station.taking(LOG)` to Woodpile (creature.gd:1334-1341);
    PR 2 fixes it (round 2).
  - [x] PR 2's Site is a Station: `accepts(log)` while `planks < need()`, `add_stack` log -> 6
    planks, `supplier` = its own planks else the nearest woodpile (c2 doc:68-69, 83).
  - [x] Crop hauls: haulers skip sold stock (round 2, Claude).
- **Candidates:**
  1. Sink-posted HAUL (on a child node, like the bank's Till). Cut: two workers on one sign
     share one shift gem (wage.gd:34), a second wage payer (F4, c4's).
  2. Source-posted push. Cut: carries with no taker; same shared-sign problem.
  3. Producer delivers to the nearest wanting station (choppers already use `Station.taking`).
     Cut as the hauler (moves no stored stock, user picked a carry job); it happens anyway once
     a stockpile accepts logs, so it stays as a free side filler (hazard fixed below).
  4. Cart shed (Factorio roboport: a ring that serves requesters from providers): its own
     sign pays one hauler per shift; each trip pairs the ring's neediest sink with the nearest
     source that has spare. Survives.
  5. RimWorld/Banished: any idle creature hauls, no building. Cut: no sign pays it (F6), and
     no placement decision for the player.
- **Recommendation (4).** Scene: the player sets a wheelbarrow shed between the woodpile and
  a zone; its ring shows on focus; a gem lands on its sign. A dull bunny in a porter cap takes
  its shift gem, scoops 15 logs at the woodpile, trots into the zone and the stockpile counter
  climbs; the builder keeps hammering instead of walking. Mechanism: the shed posts HAUL at
  itself only while a route exists in its ring (checked each `JOB_BOARD_POLL_SEC`, like the
  kitchen's `_repost`), so a hauler never burns a shift idle. `Carry.route(shed)` returns the
  pair with the largest `wants` (ties nearest), n = min(wants, spare, bag room); the hauler
  takes n via `source.hand`, its bag is bound for the sink, and delivery prefers the bound
  sink. The builder fetches itself only when the stockpile is empty, like the cook (user Q4),
  so neither filler checks the other.
- **Build sketch:**
  - station.gd: `wants(meta) -> int` (0), `spare(meta) -> int` (0), `sells() -> bool` (false),
    `hand(worker, meta, n) -> int` (free take from `stack_of(meta)` into the bag). Woodpile:
    `spare(LOG)` = its log stack count. Basket: `spare` = matching stacks while `server()`,
    `sells()` true, `hand` = `sell_into`. Kitchen, bar: `wants` from `MAX_CROPS - crops` and
    `_crop_room()`. Site: `wants(log)` = logs still short, `ceil((need() - planks) / 6)`.
    RailLoader and RailUnloader (c6, PR 11) override `wants` and `spare` the same way.
  - New `systems/jobs/carry.gd` (static): `source_for(from, sink, meta_test, free_only)` (the
    nearest reachable station with spare, via `NavigationCoordinator.reachable` as basket.gd:58)
    and `route(shed)` (sources and sinks within `shed.reach()`, free sources only). Kitchen and
    bar `supplier()` become `Carry.source_for(...)`, `bag_from` becomes `source.hand(...)`;
    third user: PR 2's `Site.supplier(from)` keeps its first branch (own planks, not a carry)
    and its woodpile branch becomes `Carry.source_for(from, self, is_log, true)`;
    `Site.bag_from(source, worker)` becomes `source.hand(worker, LOG, wants(LOG))`.
  - job_component.gd:30: rename `sow_from` -> `bound_for` (SAVED list, `hold`, `take`,
    `unload`, `drop_carry`; save VERSION = stack top + 1, no load alias); creature.gd:776: `_sow()` only for a FARM bag, else `_deliver_carry`;
    `_deliver_carry` (creature.gd:1285) uses the station at `bound_for` while it still `wants`
    the kind, else `Station.taking` as today.
  - creature.gd:784 WORK: `site is CartShed` -> `_haul(site)` (walk to source, `hand`, bind;
    `[]` -> `_wander`), below the `_fetch_gem` branch so a shift gem comes first. PR 2's `_deliver_carry` "builder to its own site first" branch folds
    into the `bound_for` rule (the builder's fetch binds its bag to its site).
  - New `entities/builds/cart_shed/` (Station; `reach()` = `SHED_REACH 20.0`, limit; posts HAUL
    at itself while `Carry.route(self)` is non-empty), .tres in the menu WORK tab, ReachRing
    like the woodpile's. `enum Job` += HAUL (after PR 2's), JOBS row (`porter_cap` hat,
    `req_int 0`, interval 1.0, reach 1.8, `anim ""`). creature.gd:1186 `below_gates`: no
    eligible job except rows open to all (`req_int 0` and not `school`), so aspire still fires for
    the dull and stops for a graduate. Tests `test_a_dull_hauler_still_aspires`,
    `test_a_graduate_stops_aspiring`.
- **Tests + cheat key:** `test/ci/systems/jobs/test_haul.gd` with a test-local sink Station
  (wants N logs): `test_a_hauler_fills_a_wanting_sink_from_a_woodpile` (sink +N, pile -N, no
  player carry); `test_an_unpaid_shed_seats_no_hauler`; `test_no_route_no_post` (no shift gem
  taken); `test_a_sink_outside_the_ring_gets_nothing`; `test_a_hauler_skips_a_selling_basket`;
  `test_a_bound_bag_goes_to_its_sink_not_the_nearest`; `test_a_dull_hauler_still_aspires`;
  `test_a_woodpile_accepts_but_never_wants` (route skips it as a sink); one integration with PR 2's stockpile:
  `test_a_site_stockpile_fills_with_no_player_carry` (plan pre-drawn, 15 s window run out on the
  site clock, else `Site.wants` is 0); `test_a_shed_with_only_basket_to_kitchen_posts_no_haul`
  (no HAUL posted, no shift gem taken). test_bar and kitchen restock tests pass
  through `Carry`. Cheat `/haul` (jobs folder): PR 2's zone and site with its plan pre-drawn and the window run out, no builder, a paid
  woodpile with 20 logs, a paid cart shed between them, a dull hauler (INT 0).
- **Shared with other clusters:** the `wants/spare/hand` contract and `Carry.route`/`source_for`
  (c2's stockpile is a sink, its builder fetch a `source_for` user; c6's rail loader is a sink
  in city A and a source in city B). c2: a stockpile that `accepts(log)` draws choppers' logs
  too (candidate 3). c4: who pays for sold stock.
- **Open questions for the user:** none left in this slice. Picked by Claude (round 2), for
  audit: HAUL INT 0; crop hauls (a) now, while (b) the cook buys the bag from the hauler
  (against the round 3 (user) "no pouch-to-pouch sale") and (c) free hauled crops stay in the
  TODO for the user.

## Old design updates (`docs/BRAINSTORM_design_r6_university_haulers.md`, doc edits only)
- Header: R2's till, sign-to-sign pay and vault deposit marked not built; new "Update
  2026-10-25" paragraph with the stage 1 rules (signs by time, sign cap 4, pouch to the worker
  on shift, gem bushes) and a pointer here. Every (user) line kept as written.
- Terms, haul trip: sign-to-sign pay at delivery replaced by "no gem moves; sold stock is a fork".
- R6: 18d marked built as `Chalkboard`; vault assumption marked moot; tuition gem goes to the
  professor (scene, mechanism, tests); build sketch on the Chalkboard script; Q1 answered by
  code (broke student not pulled), Q2 moot.
- R6b: kitchen fill corrected (the cook buys at the basket); bar marked a Station; the bag binds
  its sink, not a source; supplier pay dropped from scene, mechanism, sketch, tests; Q3 moot.

## PRE-PILLAR candidates (unconfirmed)
- PRE-PILLAR (unconfirmed): a job is learned once and kept; the stat that was highest when
  learning ended picks it, so later training never flips a creature's trade.
