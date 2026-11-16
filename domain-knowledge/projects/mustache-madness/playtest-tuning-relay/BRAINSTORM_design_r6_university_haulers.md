# BRAINSTORM: design for R6 university and R6b haulers

Design only, for the user to cut. Only lines tagged (user) are decided. Stage 2 is Shape 1
(user, `docs/BRAINSTORM_game_stages.md` "Decisions"). Payment follows the user's model
(`docs/BRAINSTORM_design_payment_model.md` "Synthesis"; `docs/HANDOFF_playtest_tuning.md`
"Payment model picks"). R2's sign as till, sign-to-sign supplier pay and vault deposit were
not built; the stage 1 economy on main pays the worker on shift instead (below). Prior art: Prison Architect (education programs unlock a
workshop job), Two Point Hospital (training room, paid course, qualification), Oxygen Not
Included (a hat per learned skill), Factorio (requester and provider chests: demand pulls
stock; inserters later load trains), RimWorld and Banished (auto haulers by need), The
Settlers (carriers on player roads).

**Update 2026-10-25 (stage 2 relay, cluster c3), the stage 1 economy now on main:** a sign is
paid by time (1 gem = one 60 s shift, `Wage.GEM_SEC`) and stacks at most 4 unworked gems (the
sign cap, `Wage.MAX_GEMS`); its worker takes 1 gem per shift into its pouch. A sign is not a
till: tuition, crops and drinks are paid pouch to the worker on shift (`Creature.buy_at`).
There is no sign-to-sign supplier pay and no pouch-to-vault deposit; gems enter by gem bushes.
Lines not tagged (user) that say otherwise are updated below; (user) lines stay as written.
The stage 2 design that supersedes this doc: `docs/BRAINSTORM_design_c3_university_haulers.md`.

**Frame for both:** stage 2 hands the build verb to the creatures. R6 raises the people who
will build (who knows how), R6b moves the stuff they build with (what reaches where). Each
turns player hand-labor into herd labor.

**Terms (what each takes in and gives out):**
- **Sign:** a workplace's one till (user). In: the player's gems (1 gem = 60 s open, paid
  ahead without limit), customers' gems while it is due, supplier pay from other signs, the
  bank payer's top-ups. Out: 1 gem per shift to its worker; 1 gem per unit of stock it takes
  in, to the supplying workplace's sign. Shows 💎 and time left (station.gd:21-104 today).
- **Sink:** a workplace that uses stock (kitchen, bar, R7's site crate). In: stock units.
  Out: `wants(meta) -> int`, how many it would take now (0 while its sign is closed).
- **Source:** a workplace whose worker stores stock it does not use (basket, woodpile). In:
  its worker's harvest. Out: `spare(meta) -> int`, how many a carrier may take.
- **Cart shed:** a workplace whose sign pays one hauler by time. In: gems on its sign. Out:
  an open HAUL job and a ring (SHED_REACH) holding the sources and sinks its hauler serves.
- **Haul trip:** in: one source and one sink in a shed's ring. Out: up to the sink's want
  moved from the source's stacks to the sink's stock. Stage 1: no gem moves at delivery
  (sign-to-sign pay is not built); sold stock (a basket's crops) is an open fork in the c3 doc.

## Round 3 changes (2026-10-22, payment model, all user)
- Every workplace has one sign, paid by time; its worker is paid per shift from it (user).
  The lectern and the cart shed are plain signs; nothing new to build there.
- A creature's gem buys its own serving: on the seller's sign while due, else in the serving
  worker's pouch; no pouch-to-pouch sale (user). Tuition now goes this way: lesson gem to the
  lectern's sign while due, else to the professor (R2's sale call, not `Creature.buy`).
- Maker pay is sign to sign: the using workplace's sign pays the supplier's sign 1 gem per
  unit (user). The round 2 MakerLedger is dropped, with every per-unit maker record. A haul
  trip carries only which source it filled from; at delivery the sink's sign pays the source's
  sign. The hauler earns only its cart shed wage.
- Spare pouch gems go to the bank vault; the bank payer tops up due signs, never opens a
  closed one (user). Cross-PR fork: "spare" must leave a student its tuition gem (below).
- Broke creatures still drink and eat free (user); whether a broke student studies free is
  18d's rule, reused here.
- Bought goods go home (user): no effect on R6 or R6b.

## Round 2 changes (2026-10-21, still standing unless round 3 says otherwise)
- VIT top goes builder: body stats (STR, DEX, VIT) -> builder, INT -> architect (user).
- The university is its own room type (user). The 📐 / 🔨 head sign is cut (user); a graduate
  reads in the job panel, its Architect or Builder row lit (creature_job_panel.gd:176 `_apt_for`).
- 18d (user): the chalkboard is a Station; chairs facing it are desks; one board per room. The
  lectern is that board shape with university desks (drafting tables, workbenches).
- `Job.BUILDER` (matches R7's doc). Crate filler: haulers fill, the builder self-fetches as
  the fallback.

### R6: University (architect and builder tracks)
- **Frame:** nothing makes an architect or a builder yet; the player should see a student
  pay a gem, sit at the bench its body suits, and leave with a trade that R7 and R8 use.
- **Assumptions to verify:**
  - [x] Job gates read INT only: `eligible_jobs` (game_enums.gd:26-32), `apt` (job_board.gd:281-286).
  - [x] Pieces may share one type name (gym, treadmill): room_skins.gd:79-92.
  - [x] Today's chalkboard: OfferPlace with desks, `_taught` armed by the teacher's labor tick
    (chalkboard.gd:28-53). R2's 18d interface: a teaching Station in group `class_board` with
    `teaches(c)`, `lesson(c, first_of_stay)`, a `one_per_room` key (BRAINSTORM_design_r2_flow.md:87-90).
    Built on main as `Chalkboard` (chalkboard.gd:1-76): OfferPlace desks, TEACH posted at itself,
    tuition paid once per stay to the teacher on shift (`buy_at`); no `one_per_room` key.
  - [x] The job panel greys jobs a creature is not apt for (creature_job_panel.gd:176).
  - [x] No pouch-to-vault deposit exists on main, so nothing empties a student's pouch (fork 2 moot).
- **Candidates:**
  1. Stat-only: benches are fast TRAIN places, jobs gate on stats. Cut: same purpose as
     library, gym, treadmill.
  2. Self-study benches, no professor. Cut: the student's gem has no sign or server to reach.
  3. Lectern = an 18d teaching Station (own scene, `room_type` university, one per room);
     drafting tables and workbenches are its desks; a student earns a trade after GRAD_SEC of
     class. Survives (Prison Architect, Two Point).
  4. Chairs facing the lectern as desks. Cut: a chair reads as an audience, not a trade bench.
  5. The professor must hold the trade it teaches. Cut: no first graduate (bootstrap deadlock).
- **Recommendation (3).** Scene: a hall with a lectern, two drafting tables, two workbenches;
  the lectern's sign reads 💎?. The player throws a gem; a mortarboard creature takes its
  shift gem and lectures. A clever fox (INT top) sits a drafting table and a 💎 hops to the
  professor; a burly bunny (STR, DEX or VIT top) takes a workbench and hammers air. Some
  days later the fox's job panel lights Architect, the bunny's Builder. Mechanism: track by
  top stat at the first class (INT: architect; any body stat: builder; ties go to INT), fixed
  for life; a bench draws only students of its track. Each TRAIN tick while `teaches(c)` banks
  `schooling`; at GRAD_SEC it holds its trade and no bench draws it again. The stay's tuition
  gem goes to the professor on shift (`buy_at`, as at the chalkboard). ARCHITECT (INT 12) and
  BUILDER (INT 8) gate on INT plus trade; no site posts them until R7 and R8.
- **Build sketch:**
  - `GameEnums.Job` += ARCHITECT, BUILDER; `enum Trade { NONE, ARCHITECT, BUILDER }`;
    `eligible_jobs(stats, trade)` honours a JOBS row's `"trade"` key (game_enums.gd:26).
  - creature_config.gd:215 JOBS rows (hats: blueprint roll and pencil; hard hat); new
    `GRAD_SEC 180.0` (dilated: about 4 cycles of about 45 s), sized to the clock, not tuned.
  - Creature: saved `trade`, `schooling` beside `pouch` (creature.gd:46, VERSION bump);
    `apt` passes `trade` (job_board.gd:285); the job panel's `_apt_for` follows.
  - `entities/builds/lectern/`: lectern.tscn + .tres on the Chalkboard script, `room_type =
    &"university"`, its own `one_per_room` key, desks = benches (an export), `teaches(c)` with
    no stat cap (the trade is the lesson, not INT).
  - `entities/builds/bench/bench.gd` (OfferPlace TRAIN, `@export var trade`): a desk while the
    one lectern of its room (`Rooms.room_at`) `teaches(c)`; calls `lesson(c, first_of_stay)`;
    drafting_table.tres, workbench.tres, `room_type = &"university"`, `needs_room = true`.
  - Hue row in room_skins.gd:31; LAW_room_types.md table; research cards in
    systems/progression/content/.
- **Tests + cheat key:** test_university.gd: INT-top draws to the drafting table only; STR-,
  DEX- and VIT-top to the workbench only; lectern off shift, no `schooling`; a stay's tuition
  gem lands in the professor's pouch; GRAD_SEC sets `trade`,
  then no bench draws it; `apt(ARCHITECT)` false before, true after; a second lectern in the
  room does not work; save keeps `trade` and `schooling`. Cheat `/university` (typed; no free
  letter key): a hall with a lectern paid 3 gems, 2 drafting tables, 2 workbenches, a
  professor (INT 14), an INT-top and a VIT-top student with 3 gems each, one broke student.
- **Open questions for the user:**
  1. Answered by code on main: a broke student is not pulled to class (chalkboard.gd `draw_for`);
     the lectern reuses it.
  2. Moot: no vault walk exists on main.

### R6b: Haulers (one carry route from a source to a sink)
- **Frame:** a kitchen today cooks only crops the player throws in; the player should place
  a cart shed, pay its sign, and watch a hauler ferry crates from the basket to the kitchen.
- **Assumptions to verify:**
  - [x] No haul code exists. Carry today: the bag, path -> count (job_component.gd:16-82),
    `_deliver_carry` to the nearest `Station.taking` (creature.gd:1169-1190), the farmer's
    `sow_from` bag bound for its basket (job_component.gd:30, creature.gd:1193).
  - [x] The bartender self-restocks: `Bar.supplier` + `bag_from` (bar.gd:110-140), called from
    `_restock` (creature.gd:1233); it ignores the basket's `owed` sowing share.
  - [x] Stage 1: the cook, like the bartender, buys crops at the nearest selling basket from the
    farmer on shift (kitchen.gd `supplier`/`bag_from`, basket.gd `sell_into`); throws still fill it.
  - [x] One job per site (`_job_at`, job_board.gd:10, 34): a kitchen cannot also post HAUL.
    A Station site pays its worker by shift (creature.gd:1212; job_board.gd:179-189).
  - [x] Without maker records the carry path needs no per-unit data: units stay plain counts
    in DroppedItem (dropped_item.gd:19-28), the bag and the kitchen. The only new datum is the
    sink the bag is bound for (no sign-to-sign pay in stage 1).
  - [x] The bar is a Station with a sign on main; R7's crate is c2's site stockpile (PR 2).
- **Candidates:**
  1. Sink-posted (each wanting workplace posts HAUL; Factorio requester). Cut: one job per site,
     and no sign pays the hauler.
  2. Source-posted push (a full woodpile posts "take this away"). Cut: carries with no taker.
  3. Player-laid routes (Settlers roads). Cut: per-route wiring is micromanagement; stage 3's
     rails are where the player draws lines.
  4. Cart shed: a sign that pays one hauler by time, with a ring; each trip pairs the ring's
     neediest sink with the nearest source that has spare. Survives.
  5. Every worker restocks itself. Cut as the main path (spends skilled time); kept as the
     fallback (bartender, builder) on the same trip code.
- **Recommendation (4).** Scene: the player sets a wheelbarrow shed between farm and
  restaurant; its ring shows; a gem lands on its sign. A porter-cap creature takes its shift
  gem, scoops carrots at the basket (🧺 over it), trots into the restaurant and the counter
  reads 🧺 x10. Mechanism: a trip picks the ring's sink with the largest `wants` that a ring
  source can fill, fills the bag up to it from one source, binds the bag to the sink, and
  delivers. A closed sink wants 0. Stage 1 update: who pays the farmer for hauled crops has no
  answer yet (no sign-to-sign pay); the c3 doc hauls free stock (logs) first.
- **Build sketch:**
  - `systems/jobs/haul.gd` (static): `route(shed) -> [source, sink]`, `fill(job, source, sink)`
    (sets `bound_from`), `deliver(job, sink)` (`sink.receive`; no supplier pay in stage 1). Bar's `supplier` and `bag_from`
    (bar.gd:110-140) become `route`/`fill` calls; R7's builder fallback is the third user.
  - JobComponent: `sow_from` -> `bound_for` (job_component.gd:30, 51, 64-84), plus `bound_from`;
    both saved with the bag. `_deliver_carry` (creature.gd:1169) delivers to `bound_for` first:
    a basket sows (`_sow`, 1193), a sink takes `Haul.deliver`.
  - creature.gd:716-723: a HAUL worker with an empty bag runs `_haul(shed)` beside `_restock`.
  - `wants/receive`: Kitchen (crops below `HAUL_STOCK`, 0 while closed), Bar (`_room()`);
    `spare`: Basket (stacks minus `owed`), Woodpile (all logs).
  - `entities/builds/cart_shed/` (Station: `serves(HAUL)`, `reach() = SHED_REACH`), card,
    `Job.HAUL` row (porter cap), `SHED_REACH 20.0` (limit), `HAUL_STOCK 10` (limit).
- **Tests + cheat key:** test_haul.gd: paid shed, paid kitchen, basket 12 carrots (owed 0) in
  ring: after the trip kitchen.crops == 10, basket holds 2; owed crops stay; a sink outside the
  ring or with a closed sign gets nothing; an unpaid shed gets no hauler; a bar fills to
  `_room()`; a source knocked down mid-trip: delivery still lands. test_bar's restock cases pass through
  `Haul`. Cheat `/haul` (typed): a paid shed, a basket with 12 carrots, a paid kitchen with a
  cook, a paid bar with a bartender, 2 friends.
- **Open questions for the user:**
  1. Hauler gate: INT 8 like the chopper, or open to the dull (INT 0, a first rung)? INT 0
     empties `below_gates` (creature.gd:1075), which aspiration reads, so it needs a "below the
     skilled gates" redefinition. Rec: INT 0 with that redefinition.
  2. Crate filler: haulers fill R7's crate, the builder self-fetches only with no shed serving
     it (rec; R7's agent asks the same fork). Or the builder alone, as Q4 first said.
  3. Moot in stage 1: the cook and bartender pay the farmer on shift per crop from their own
     pouch (`sell_into`); no sign pays a sign.
