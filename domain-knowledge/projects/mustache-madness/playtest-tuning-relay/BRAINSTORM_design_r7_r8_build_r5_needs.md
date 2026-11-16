# BRAINSTORM: design for R7 zones, R8 build, needs fade, R5 physics bugs

Design only, for the user to pick. Tags: (user) = the user decided it; [C file:line] = checked in
code on main @ c516194a; [A] = assumed. R6 (university, architect and builder jobs), R6b (haulers)
and R2 (sign-to-sign pay) are designed by other agents; names used for them are guesses, marked [A].
Pillars used as lookups: Natural on sight, Add connections, Sacrifice through occupied shared
state, Roles emerge from raising, Black box, Ban hidden effects, a creature holds gems of its own;
antipatterns Menu-driven action, Micromanagement, Player god powers.

## Round 4 changes (stage 1 economy on main 86fc5fb7; the stage 2 build is now designed in docs/BRAINSTORM_design_c2_build.md)
- Main has no sign-to-sign pay: a supply is bought pouch to pouch from the seller on shift (a
  cook pays the farmer on shift 1 gem a crop), and a sign stacks at most 4 gems (`Wage.MAX_GEMS`).
  So `pay_supplier` and "a gem hops from the crate's sign to the woodpile's sign" below are cut;
  logs at a woodpile stay free, as they are for the player (log price: open, c4 owns gem flows).
- "A crate paid 5 gems" reads as a sign holding its cap of 4.
- The plan comes from PR 1's room tool (`BuildPattern.lay` ROOM case), not `hut_pieces`; the site
  stock counts planks (a log adds 6), priced per piece by `Blueprints.build_cost` like the player's.
- The vault payer still tops up a due sign (main keeps the bank's relay), so it may top up a site.

## Round 3 changes (payment model, user 2026-10-22)
- R7: the crate is a workplace sign like any other (rule 1): the player funds it for time, and its
  architect and builders take 1 gem a shift from it. Crate lots and per-log maker records are gone
  (rule 3): the crate counts logs as one number, and each log delivered from a woodpile moves 1 gem
  from the crate's sign to the woodpile's sign (R2's sign-to-sign verb). Pay is at delivery because
  only the delivery knows the source. A thrown log pays no one. Fork (b) restated: building starts at
  max(15 s window end, first paid shift).
- R8: no gem moves when a piece goes in; per-log tips are cut. An unpaid sign stops the builders, and
  the half hut waits. The vault payer may top up a due crate (rule 4), but never opens a closed one.
- R7 and R8 now define each concept (Zone, Site, Plan, Builder shift) by what it takes in and gives out.
- NF and R5: unchanged (the payment rules do not touch them).

## Round 2 changes
- NF: confirmed in the Godot docs that Sprite3D supports visibility ranges and alpha fade; gave the
  exact property set; the fade window is centred on `end` (end - margin to end + margin, engine source).
- R5: re-checked the dawn-rise idea against bed.gd, the bed scene and the creature's capsule. The
  capsule's centre is the body origin [C creature.gd:288-291]; rise and lie spots set that centre at the
  bed's base or mattress, so 0.13 to 0.74 m of capsule starts under the floor top. Split H1 into H1a
  (rise spot) and H1b (lie spot all night). New: 2 of the 4 playtest burst bodies showed no owned bed (🛏),
  which H1 must explain. Cheapest discriminating test now leads the plan (one GUT file, no sim).
- R7: haulers fill the crate, the builder fetches only as a fallback; the crate keeps each log's maker
  (a lot ledger) so the tip rule can pay the woodcutter; builders are STR, DEX or VIT top, architects
  INT top (R6). New fork: the crate is a Station, and the job board opens a Station's jobs only while it is
  paid [C job_board.gd:220], so a paid shift gates the architect and builders.
- R8: a builder opening a log tips its maker 1 gem (the general tip rule); a log from the player or one
  with no living maker tips no one. Tests and cheats refreshed for both.

### NF: Needs fade (white need balloons show only near the player)
- **Frame:** at herd 60+ a white need balloon over every creature clutters the view; the player wants
  them only on creatures close by, while a red one (a consequence is coming) still reads from afar.
- **Assumptions to verify:**
  - [x] "Needs in white" = the white dialog balloon plus its icon: two Sprite3Ds built in `_ask`
    [C status_emoji_component.gd:61-83]; red when `critical` [C :80; view_coordinator.gd:64].
  - [x] Sprite3D inherits GeometryInstance3D; the Godot "Visibility ranges" page lists Sprite3D and Label3D
    as supported, and says fading is alpha only (SELF forces transparent rendering; both sprites already are).
  - [x] `VISIBILITY_RANGE_FADE_SELF` works only on Forward+ (GeometryInstance3D docs); the project is
    Forward+ [C project.godot:19]. Distance is camera to the AABB centre; the camera is the player's own
    first-person Camera3D [C player.gd:48], so each peer judges its own.
  - [x] Fade window: `end - end_margin` to `end + end_margin` (engine `_update_instance_visibility_dependencies`).
  - [ ] Red balloons stay visible at any distance (my reading of "in white"): user.
- **Candidates:**
  1. Engine visibility range on both sprites, end set while white, 0 (no limit) while red. Survives.
  2. A script sets alpha by distance every frame. Cut: same output as 1, a per-frame loop at 180 bodies.
  3. Balloons only on the aimed creature (the show-on-aim hint). Cut: the user said "close", not "aimed".
  4. Shrink balloons with distance. Cut: still clutter; not asked.
  Prior art: MMO nameplates cull by distance; RimWorld hides need bubbles zoomed out, keeps alerts.
- **Recommendation:** walking through the herd, balloons are full within 9 m, fade out by 15 m; a
  starving creature's red balloon shows across the map. The state glyph and circling marks are not needs.
- **Build sketch:** `status_emoji_component.gd:_ask`, where `_balloon` and `_icon` are built (:65-77), set once
  on each: `visibility_range_begin = 0.0`, `visibility_range_begin_margin = 0.0`,
  `visibility_range_end_margin = NEED_FADE_M`, `visibility_range_fade_mode =
  GeometryInstance3D.VISIBILITY_RANGE_FADE_SELF`. On every call (:78-80): `visibility_range_end = 0.0 if
  emergency else NEED_SHOW_M` on both. Constants in that file: `NEED_SHOW_M := 12.0`, `NEED_FADE_M := 3.0`
  (limits). One write path covers both colours.
- **Tests + cheat key:** extend `test/ci/entities/creatures/test_suffering_signs.gd` (:69 sets the hunger
  glyph): white -> both sprites have end 12, margin 3, fade SELF; critical -> end 0; white again -> 12.
  Cheats exist: `/needy` (white on every friendly), `/starve` (red); walk away and back.
- **Open questions for the user:** (a) red balloons visible at any distance? Recommend yes. (b) full to 9 m,
  gone at 15 m? Recommend it, tune in playtest.

### R5: physics bugs (bodies under the ground; the "embedded" defect)
- **Frame:** "fell" mixes two things: about 95% are knocked bodies flying off the land's rim (no walls by
  design; put back), and the rest are bursts of walking friends 2 m under the floor inside the land, all at
  dawn. Run the cheapest test that splits the dawn causes, build the missing "embedded" probe, then diagnose.
- **Assumptions to verify:**
  - [x] Logs: playtest_2026_10_20.log 70 fell, 66 knocked with |x| or |z| > 30 (land 60 x 60 m
    [C level_02.tscn:26]), 4 unknocked ROAM at y -1 in one sample; godot2026-10-19T23.52.45.log 94 knocked
    off the rim, 11 unknocked in the land in 4 bursts; sims/active_1.log 9, all off the rim.
  - [x] All 5 in-land bursts come within 2 s after "Day phase: DAWN". 2 of the playtest 4 showed 🛏 (no owned
    bed, creature.gd:1047) at the sample; `_wake` clears `sleep_bed` [C creature.gd:976-979], so "bed": null says nothing.
  - [x] QA flags y < surface - 2 each sample [C qa_watch.gd:82]; rescue at surface - 1.5 runs only on a
    think [C game_physics.gd:120; crowd_body.cpp:207-210]. Ground is a thin trimesh [C procedural_terrain.gd:179].
  - [x] Body origin = capsule centre [C creature.gd:288-291]; capsules 0.76 to 1.484 m tall (species .tres).
    Asleep, the centre is held at the bed's Lie marker, 0.3 m over the bed origin [C creature.gd:2013-2014;
    sleep_bed.tscn:59]; waking by the bed it is set at `rise_spot`, the bed origin's height [C creature.gd:2019-2020;
    bed.gd:132-134]. So the capsule bottom starts 0.38 to 0.74 m under the bed origin.
  - [ ] Where the bed origin sits over the floor top (flush or 0.25 m up) [A]: decides 0.13 to 0.74 m under the floor.
  - [x] No "embedded" QA kind exists on main, mm-fixes or mm-fixes2 (grep), despite the HANDOFF line.
- **Candidates (hypotheses for the dawn bursts, ranked):**
  1. H1a rise: the woken capsule starts under the floor top; recovery pushes it down through the thin
     slab and trimesh. Survives, rank 1.
  2. H1b lie: all night the capsule sits in the bed frame and floor; the first step after waking pushes it
     down before any rise. Survives, rank 2 (also fits a bed it does not own).
  3. H2 a dawn spawn spike moves bodies (spawn = 9-14 ms in 3 burst [PERF] lines). Rank 3.
  4. H3 a 57-73 ms frame lets one step pass the trimesh. Weak: walking bodies are on the floor.
  5. H4 push-out from a placed piece (#370). Cut: no placement at dawn; a burst spans 40 m.
- **Recommendation (investigation, no behavior change):**
  1. Cheapest discriminating test first: `test/ci/physics/test_dawn_rise.gd`, one boot: a floored 3 x 3 m hut
     with a sleep bed, the tallest (1.484 m) and the shortest capsule. Case A: asleep in the bed, then `_wake`,
     20 physics steps. Case B: the same body set at `rise_spot` with no night in bed. Assert lowest point >=
     floor top - 0.05. A fails, B passes: H1b. Both fail: H1a. Both pass: H1 out, go to H2.
  2. QA: split "fell" (inside `WorldWrap.land_min/max`) from "off_rim" (counted, quiet), qa_watch.gd:82.
  3. QA "embedded": once a second, a body centre whose block cell holds a STRUCTURE piece not in group
     `bed_piece` (`Grid.get_block(Grid.block_from_world(centre))`, grid_manager.gd:183); flagged once per episode.
  4. `[FALL]` in `rescue_under_world` (pos, velocity, knocked, mode, seconds since dawn, last bed) and `[RISE]`
     in `_settle_in_bed` (spot, floor top under it by a ray). One sim to dawn 3 only if step 1 clears H1.
- **Build sketch (fix candidates, after the user gates the diagnosis):** F1 one `GamePhysics.stand_at(body, point)`
  that rays down from above and puts the capsule bottom on the top surface hit (slab or ground); rise, lie
  release and push-out all land through it (one landing path). F2 lift only `rise_spot` by the half height
  (narrow). F3 rescue onto the support under, not terrain + 2 m (hides the cause). F4 the QA split alone (needed anyway).
- **Tests + cheat key:** test_dawn_rise.gd above, then green after the fix; `stand_at` on a slab and on bare
  ground (test_game_physics.gd). New cheat `/dawnbed`: a floored hut ahead, 4 sleepers of mixed species in beds,
  clock 5 s before dawn. `/knock` covers the rim class.
- **Open questions for the user:** (a) off-rim falls: keep as knock fun with QA counting them quietly, or a
  rim wall? Recommend keep. (b) approve test, then probe, then fix, before any fix lands.

### R7: zones (a zone and one anchor; the architect draws the ghost; the site crate)
- **Frame:** the player says what and where in one gesture and funds it; an architect turns it into a
  blue plan whose tightness shows its skill, and wood gathers in a crate on site.
- **Concepts (by what they take in and give out):**
  - *Zone:* takes the player's drag (a rectangle on the ground) and one anchor; gives a Site.
  - *Site* (a Station, the crate): takes the player's gems on its sign (time, 60 s a gem: rule 1),
    logs delivered by haulers or its builder, the architect's labor; gives shifts (1 gem each from its
    sign to its architect and builders: rule 1), and pieces onto the Grid (R8). (Round 4: no gem per
    log; main has no sign-to-sign pay.) Done, it spills spare wood and its sign's gems.
  - *Plan:* the ordered [meta, cell] pieces the architect draws; ghost = a drawn plan piece on a free cell.
- **Assumptions to verify:**
  - [x] Shape 1, skill only, building starts 15 s after the zone, a crate a builder job fills (user,
    BRAINSTORM_game_stages.md Decisions). Payment rules 1-4 (user, HANDOFF "Payment model picks").
  - [x] `Game.hut_pieces(low, size)` gives floor, walls with a 2 m door, roof [C game.gd:285]; 3 callers
    [C game.gd:249, cheat_coordinator.gd:815, headless_sim_driver.gd:789]. Square only.
  - [x] A missing wall column is an opening, 1 per 8 m² allowed; more refuses the room with its caption (LAW_rooms rule 3).
  - [x] Kitchen store: a count shown "🧺 xN", posting its job while > 0 [C kitchen.gd:17-29], fed by a throw [C :60-66].
  - [x] A room-only anchor needs built floor under it [C placed_behavior.gd:218; LAW_rooms rule 4].
  - [x] A Station's jobs open only while its sign is paid [C job_board.gd:220]; the sign is `Wage` (60 s a gem,
    a gem per shift) [C wage.gd:10, station.gd:96-99]; a removed station spills its gems [C station.gd:118-122].
  - [ ] R2 owns sign-to-sign pay: `Station.pay_supplier(supplier, n)` and what an empty paying sign does [A].
  - [ ] R6: `Job.ARCHITECT` (INT top), `Job.BUILDER` (STR, DEX or VIT top), hats, no head sign [A].
  - [ ] R6b: a hauler carries stock from a station that has it to one whose `accepts()` wants it, and the
    delivery names its source station [A]; the hauler is paid by its own sign, not the crate.
- **Candidates:**
  1. A Site station (crate by the planned door) owning zone, anchor, plan, log count and the 15 s timer;
     the plan from `hut_pieces` made rectangular. Survives.
  2. Per-piece frames, each its own stockpile (RimWorld). Cut: user picked one stockpile; hundreds of sites.
  3. A bare Grid overlay with no object. Cut: nothing to undo, fund or throw logs at; state with no owner.
  4. Robots build from the player's pack (Factorio). Cut: no herd labor; a god power.
  Cut by round 3: crate lots and per-log maker records (rule 3 drops them).
- **Recommendation:** the player picks Zone in the Build tab and drags a 4 x 3 m rectangle: blue stakes and
  a rope, a crate by the door side, its sign "⏱ 15". The player places a bed inside (a blue ghost bed; the
  item leaves the hand) and throws 3 gems on the crate: the sign shows paid time like any workplace. An
  architect with a pencil walks the zone corner to corner; blue walls and roof appear a side at a time; a weak
  one leaves a hole and the crate's caption says what the room law says ("3 openings, a room this size allows
  2"); the player may plug it by hand. At 0 the sign reads "🪵 0/16": a hauler carries logs in from the
  woodpile (Round 4: free, no gem moves); with no hauler free, the
  builder fetches. Breaking the crate in the window takes the zone back: the bed and the gems pop out.
  Mechanism: ARCHITECT posted until drawn, one side per labor tick; gaps = max(0, (ARCHITECT_TIGHT_INT - INT) /
  INT_PER_GAP) wall columns, seeded, never beside the door; logs counted as one number; `accepts(log)` while
  logs * 6 + loose planks < planks still needed. (Round 4: the per-log `pay_supplier` is cut.)
  The vault payer (rule 4) may top up the crate when due; it never opens a closed one.
- **Build sketch:** `game.gd:285 hut_pieces(low, size)` -> `(low, size_x, size_z)`, 3 callers pass size twice.
  New `entities/builds/site/` (site.gd extends Station, crate .tscn with the kitchen's CaptureArea): rect,
  anchor {meta, cell, step}, plan, drawn, logs, loose, a Cooldown on the site's LocalClock (LAW_time_dilation).
  `add_stack` override: logs += count, then `pay_supplier(source, count)` when the delivery names one (a
  player throw names none: no pay). Ghost: one MultiMeshInstance3D per site, blue unshaded alpha (`GHOST_PLAN`
  beside build_preview.gd:7-9), an instance per drawn plan piece on a free cell; peers draw from replicated plan
  + drawn. Blueprint "zone" (Pattern FLOOR, price 0): `build_hand.gd:322 _drag` release sends
  `_net_request_zone`. `placed_behavior.gd:272 place()`: an anchor aimed into a zone becomes `site.set_anchor`;
  a second is refused ("the zone has its anchor"). BUILDER fetch: only while the crate is short and no hauler is
  seated on a carry to it [A: R6b]. Config: ZONE_UNDO_SEC 15 (user), ZONE_MIN_M 2, ZONE_MAX_M 12 (ROOM_MAX_CELLS at
  5 m tall), ARCHITECT_TIGHT_INT 20, INT_PER_GAP 4. Saved (LAW_save).
- **Tests + cheat key:** `test_site.gd`: `hut_pieces` on 2 x 2, 4 x 3, 6 x 6 m gives a room `Rooms.find`
  accepts; gaps 0 at INT 20, 2 at INT 12; an anchor into a zone sets it and spends the item; an unpaid crate
  posts no ARCHITECT or BUILDER; paid, no BUILDER before 15 s on the site clock; breaking it in the window
  returns the anchor and the gems; a delivered log from a woodpile moves 1 gem crate sign -> woodpile sign, a
  thrown log moves none; `accepts(log)` false once covered; the builder fetches only with no hauler seated.
  `/architect` (user): a 4 x 3 m zone ahead with a bed anchor, a crate paid 5 gems, an architect (INT 12: one
  gap), a hauler, a builder (VIT top), a paid woodpile with 20 logs stacked.
- **Open questions for the user:**
  (a) the 15 s counts from the drag or the anchor? Recommend the anchor (an empty zone stays empty).
  (b) the crate is a workplace like any other: its jobs open only while the player has paid its sign, so
  building starts at max(15 s window end, first paid shift). Recommend yes; the alternative is an unpaid
  crate that breaks rule 1 and the job board's one gate.
  (c) the anchor goes in as a ghost placed into the zone (recommended), or the floor must come first?
  (d) fill pieces (more beds for a Bunkhouse) in a later slice? Recommend later.

### R8: build (builders hammer the plan in; wilds; dawn)
- **Frame:** the blue plan becomes a real hut by paid herd labor, and a night can knock part of it out; the
  player watches walls rise course by course and holes go back to blue.
- **Concepts:** *Builder shift:* takes 1 gem from the crate's sign (rule 1); gives labor ticks that turn crate
  wood into plan pieces. No gem moves when a piece is placed or a log is delivered (Round 4).
- **Assumptions to verify:**
  - [x] A piece the game sets down pushes bodies out of its cells [C spawn_coordinator.gd:150-154, #370].
  - [x] A wild punches the STRUCTURE piece it bumps; at WALL_PUNCH_SEC it breaks and drops its planks; punch
    time resets at dawn [C creature.gd:630-640; grid_object.gd:204-221]; only pieces on its way (LAW_rooms rule 5).
  - [x] A broken piece frees its cell, so a plan piece on a free cell is simply ghost again: no new state.
  - [x] Labor hook: `labor(dir, worker)` [C kitchen.gd:41]; a worker punches in for 1 gem a shift [C station.gd:96-99].
  - [ ] "Wilds punch scaffolds" and "half built stays half built" are brainstorm [A] lines, not (user).
- **Candidates:**
  1. One piece per labor tick in order (floor, anchor, wall courses bottom up, roof), planks from the crate;
     ordinary pieces at once; wilds punch them only on their way. Survives.
  2. A scaffold state: a frame for N ticks that breaks in one punch. Survives as a fork: a look and a stake, one more piece state.
  3. Sites lure wilds at night. Cut for now: a new targeting rule the player cannot steer.
  4. An unfinished site decays at dawn (Kingdom Two Crowns). Cut: contradicts "half built stays half built".
  Cut by round 3: per-log tips to the chopper at use (rule 3 pays sign to sign, at delivery in R7).
  Prior art: RimWorld blueprint -> frame -> built, frames damageable; Factorio ghosts rebuilt after damage.
- **Recommendation:** a builder in a hard hat punches in at the crate (a gem off its sign), takes a log, and
  swings at the lowest blue piece: it turns to plank. Floor, then the bed, walls course by course, roof last;
  the room turns pink (Bedroom) as it closes. The sign runs dry: the builder stops, the half hut waits until
  the player (or the vault payer, once due) pays more. Night falls with the roof half done; a wild cutting
  across the yard punches a block out: planks drop, the hole shows blue. At dawn the half roof stands; the
  builder fills the hole. Mechanism: candidate 1. BUILDER labor tick: next drawn plan piece on a free cell; walk
  within SITE_REACH (flat); if loose planks < its cost, open a log (logs -1, loose += 6); spawn via
  `SpawnCoordinator.spawn_grid_object`; loose -= cost. No free plan piece left: done; the crate spills spare
  wood and its sign's gems (the existing refund path).
- **Build sketch:** site.gd `next_piece()`, `labor(dir, worker)` (the cook's labor path); the BUILDER branch
  picks hammer vs fetch (R7) by whether the crate covers the next piece. JOBS row BUILDER [A, R6]: interval 1.0,
  reach 2.5 flat (the roof at 5 m is hit from the ground), "attack" swing as the hammer. Done = `_yeet_drops`-like
  spill (station.gd:118-122) then free. RoomSkins needs no change. Constants: SITE_REACH (limit), the BUILDER interval (pace).
- **Tests + cheat key:** `test_site_build.gd`: with enough logs and a paid sign, ticks = pieces leave the plan on
  the Grid and `Rooms.find` gives a Bedroom; placing a piece moves no gem; an unpaid sign stops the builder; a
  broken piece's cell returns to the ghost list and the next tick refills it; a new day leaves pieces as they are;
  short crate -> no placement; done spills spare wood and gems. One headless skeleton run (not a batch): woodpile,
  chopper, hauler, architect, builder, paid crate, a 4 x 3 m bed zone -> a Bedroom, the woodpile's sign up 1 gem
  per log delivered. Cheat `/site`: a drawn 4 x 3 m bed zone ahead, a crate paid 5 gems with 16 logs, a builder;
  `/night` then shows wilds punching it.
- **Open questions for the user:**
  (a) scaffold frames (2) or plain pieces at once (1)? Recommend 1 for the skeleton.
  (b) should sites draw wilds at night (3)? Recommend no.
  (c) more than one builder per site: JobBoard seats one per site; wall sides as ring sites later? Recommend one now.
  (d) spare wood when done: spilled at the crate (recommended), or hauled back to the woodpile?
