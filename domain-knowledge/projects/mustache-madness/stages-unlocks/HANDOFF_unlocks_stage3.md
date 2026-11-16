# HANDOFF: unlock tree + stage 3 core (AFK relay, started 2026-10-25)

## Status (for the user's return)
- Relay 1 DONE up to the merge: PRs #387 (1), #388 (2), #389 (3), #390 (3b), #391 (4), #392 (5),
  #393 (6), #394 (7), #395 (8), #396 (9) open, stacked in that order. Full suite GREEN on the top
  fd06f271 (after merge-gate fixes): unit 1308, physics-misc 87, terrain 10, navlink 21. NEXT (main session): merge in
  order, tag, pull main, playtest. Worktree /home/akiraki/Playground/mm-unlock.
- Power: AFK idle config (no poweroff) until the user ends AFK.

## Purpose (user)
1. The Work tab starts with only the Mine and the Lab; everything else unlocks by what the player
   builds or raises, never on a clock (user). The mine costs wood, not gems (user).
2. Stage 3 core from `docs/TODO_stage3.md`: city tags, trade prices between cities, train loader
   jobs, riders. Startups, land purchase and the tax office stay designed only (user).

## Rules for the relay
- Worktree off `fix/ore-in-bounds` (e.g. `/home/akiraki/Playground/mm-unlock`), stacked branches.
  Never edit the main checkout except this file (live, uncommitted; update after each step).
- The unlock tree is a game design: run /design-idea in AFK (you close every fork, log it below),
  anchored on the MEMORY.md pillars, esp. "a capability opens when something the player builds or
  raises makes it possible, never on a clock or a stage line" and "a reward is a new rule, verb, or
  board change". Each unlock must read on sight (what opened it, and why).
- No balancing (no tuning, no sim batches to move a number); log balance questions below.
- Every playtestable PR ships a cheat key. Agent pool: at most 5 alive counting you, reused.
- The local full suite is the only gate (CI blocked by billing); its shards now match ci.yml.
- Final report: `MERGE #...` with the full-suite result, plus the /afk step 10 playtest report
  (what changed, what to test with each cheat key read from the code, what to watch out for).

## PR list
1. **Ore fix (built).** Open the PR for `fix/ore-in-bounds`: the ore at 0.7 of the map's real
   half-size (test over 200 seeds on 60x60 and 90x100); local physics shards synced with CI (9
   files were missing). Also delete `docs/HANDOFF_mine_job_quality.md` (served; carry its open
   items below). Done: PR open.
2. **Pre-existing red test.** `test/ci/physics/test_block_nav.gd`
   `test_a_bartender_skips_a_nearer_basket_it_cannot_walk_to` fails on main (it never ran
   locally). /debug-tdd in AFK: find why, fix the game or the test, log which. Done: file green.
3. **Mine costs wood (user).** Mine build cost in wood, not gems; pick the amount like the other
   wood basics (log it). Check the player can get wood with only Mine and Lab open. Done: test.
3b. **Room tool door faces the player (user: "the door in room build should look towards me").**
   Today `BuildPattern.door_side` (build_pattern.gd:94, called at build_hand.gd:221 and :426)
   picks the wall line nearest the player's block; in play the doorway lands on a wall not facing
   the player. /debug-tdd in AFK, hypotheses: player inside the rect picks a side wall; ties fall
   to LEFT; the side is read at a different moment than the lay. Target rule: the doorway is in
   the wall facing the player, by the direction from the room's centre to the player. Done: a
   test with the player outside each side and one inside near a corner; ghost and lay agree.
4. **Unlock tree.** Work tab opens with only Mine and Lab; design what else is locked and what
   build or raise opens each (e.g. first mined gems, a lab find, a graduate); reuse the lab's
   existing discovery/blueprint path where it fits. Visible unlock moment. Cheat to open all.
   Done: tests for the start set, two unlock triggers, and a save round trip of unlocks.
5. **City tags.** From TODO_stage3.md: a city's tags give it its own mood or effects. Cheat.
6. **Trade prices.** Prices differ by city, so shipping goods on the rail pays. Cheat.
7. **Train loader jobs.** Creatures load and unload trains (reuse the carry contract). Cheat.
8. **Riders.** Trains carry creatures between cities. Cheat.
9. **Stage 3 design log.** Startups, land purchase, tax office: designed, logged in
   TODO_stage3.md, not built.

## Resume here
- Worktree `/home/akiraki/Playground/mm-unlock` (the old mm-mine, moved; imported, addons in).
- PR 1 DONE: PR #387 open (`fix/ore-in-bounds` 7a7346f0). Mine handoff moved to the session
  scratchpad (served; its open items are below).
- Clusters (explode step 1): c1 = PR 2 (debug, inline, no design agent); c2 = PR 3+4
  (`docs/BRAINSTORM_design_unlocks.md`); c3 = PR 5+6+9 (`docs/BRAINSTORM_design_s3_cities.md`);
  c4 = PR 7+8 (`docs/BRAINSTORM_design_s3_rail.md`). Merge order 1..9, stacked.
- PR 2 DONE: branch `fix/block-nav-bartender-test` 182eddbb (off PR 1). The test was stale, not
  the game: a basket sells only through a farmer on shift since #371; test now puts one on each.
  test_block_nav 11/11.
- PR 3 DONE: `feat/mine-costs-wood` e3cd5632. Mine 4 wood (like woodpile, cart shed). The axe
  gets wood with nothing built (covered by test_tree_chop's felling test). test_mine, build_hand green.
- PR 3b DONE: `fix/room-door-faces-player` 79b313d4. Cause (repro test red 4/5): door_side took
  the nearest infinite wall line, so a player beside a long wall near its end got the end wall.
  Fix: way from the centre scaled by half-size. Ghost and lay share `_drag_args`/door_side.
- /abstract DONE: `/tmp/claude-layers/unlocks_stage3.md` (framings A2 enable-by-inputs, B2 city =
  holdings, C2 stop = workplace; flags F-*). Branches 2, 3, 3b pushed.
- PR 3 fixup 6cabacf9 (sim bot pays the mine in wood; comment tag); 3b restacked 1ce34fb4.
- Design round 1 DONE (docs in the worktree, untracked: BRAINSTORM_design_unlocks / _s3_cities /
  _s3_rail). Round 2 sent to c2 and c4 (cross fixes); c3 needs none. NEXT: cold review by the
  abstract agent, then build PR 4.
- Cold reviews DONE. Unlock: 1 severe (anchor path untallied), fixed by picks below; c2 folds
  them in (round 3). Cities/rail: 1 severe (`_wait` put-back undoes porter loads) -> one-shot
  `_restore_after_load()`; c3, c4 round 3 done. Designs SOLID.
- PR 4 DONE: `feat/unlock-tree` 1fcc0d3d (tests: unlock_tree 9, registry, mine, site, lab, save,
  menu, build_hand, room_gates, cheat_tree green). Test files that read the start menu reset it.
- PR 5 DONE: `feat/city-tags` 3f5e5b55 (test_city 6/6 + save, cheat_tree, tipsy, housing, rail).
  Party pieces = FREE_TIME (bar and kitchen are WORK cards). Label: shared `CityLabel`.
- PR 6 DONE: `feat/trade-prices` f0cff285 (test_rail 13/13, shop, site, haul, city, save, cheat
  tree). Dock has no has_till override (it would add a PaySign); `buy(into=dock)` fills its till.
  Fare banks in `_wait` until PR 7 moves it to `_restore_after_load()`.
- PR 7 DONE: `feat/rail-porters` b63a5074 (test_rail 17/17, cheat tree, save, haul, job board).
- PR 8 DONE: `feat/rail-riders` 27868729 (test_rail 21/21). PR 9 DONE: `docs/stage3-design-log`
  549d772e (TODO_stage3: startups, land, tax office; built items ticked). All pushed.
- Full suite run 1 red: `_spot` missing from the stops' field lists (save list test); fixed in
  PR 7 (d5edeb53), PR 8 d1a2e871 and PR 9 1131671b restacked. Run 2 GREEN on 1131671b: unit
  1302, physics-misc 87, terrain 10, navlink 21.
- Code review fixes DONE (PR 4 33c3bef3, PR 5 bd8a5d40, PR 7 11e9e159, PR 8 0e41c326); run 3
  green; PRs opened. Design docs `docs/BRAINSTORM_design_{unlocks,s3_cities,s3_rail}.md` are
  untracked in the worktree (served; delete after the merge).
- Merge-gate review (1 severe + 5 medium) fixed as fixups, autosquashed with --update-refs:
  broke stocker skips a dock (PR 6), route only to a paid dock + dock posts only for a docked
  load + porter test via the job board (PR 7), server checks the tallied id lays that meta
  (PR 4), work-town test drives _fetch_gem (PR 5). Top fd06f271: touched files 117/117 green;
  full suite run 4 GREEN (unit 1308, physics-misc 87, terrain 10, navlink 21). Force-pushed.
  NEXT (main session): MERGE #387..#396 in order.
- (history) Code review: 3 severe (stuck rider; one dock slot overwritten by a 2nd line; loader knockdown
  loses fare/aboard), 2 major (axe stops for an unpaid mine; stocker walks to a porterless dock),
  minors. Fixing per PR and restacking (PR 4 33c3bef3, PR 5 bd8a5d40, PR 7 in progress, PR 8
  next); then full suite run 3, open PRs, report MERGE.

## Decisions for audit
- Purpose, unlock rule (by build or raise), merge allowed (user, picked options).
- Mine costs wood (user); 4 logs (Claude: the Work-station wood price; no gem).
- PR 2 (Claude): fixed the test, not the game (no farmer on shift = no sale, by design #371).
- Unlock scope (Claude): the gate covers the Work tab; other tabs open unless a pillar reason.
- Lab random finds stay for pool cards; Work basics open by an "opens when" rule (Claude).
- c3 owns the shipped-unit payment contract; c4 owns who works a stop (Claude).
- Unlocks (Claude, c2 doc): one `opens_when` key list per card, one `Blueprints.open_by(key)`;
  woodpile <- first mined gem; cart shed <- first woodpile; rail + stops <- first cart shed (PR 5
  re-points to the first City Stone); lectern <- first zone; Farming <- first Kitchen or Bar;
  Emergency Post <- first Medic Bed (not a downed friend: an event, not a build); the axe on
  the ore knocks 1 gem loose (start bootstrap, no kill gate); lab pick stays random.
- Cities (Claude, c3 doc): City Stone (Build tab, open) + nearest heart; tag = strict plurality
  of WORK/FREE_TIME/STAY pieces, each one standing mood rule; resident = city of its bed. Price:
  the dock sells logs at its city's logs-per-gem from the buyer's pouch; the cart carries the
  till home as fare to the loader's sign. No Trade.landed hook (payment at the sale).
- Rail (Claude, c4 doc): porter = Job.HAUL on a stop SiteSpot (one role with the shed hauler);
  no gem burn without a worker; dock without porter stalls; two signs per line; commuters ride
  when the line saves >= 20 m to their job; a rider = one bag of room; no fare. PR 7: the dock
  sells only through its porter on shift.
- Save: PR 4 bumps VERSION 33 -> 34 (`_opened_by`); PR 5-8 reuse it (one stack, one bump).
- Review picks (Claude): an anchor set in a zone tallies its card; place RPCs carry the card id
  (`tallied_id`), so a Half Block never counts as "your first Zone"; the axe gets an ore gem only
  while no Mine stands (bounded hand income; alt: 3 loose gems at the ore, for the user); peer
  join gets one quiet bulk unlock rpc (server only).
- City tag effect readouts 💪/🎉/😴 + stone label are invented (Claude); /towns party = 2
  campfires + games table.
- Review picks (Claude): axe stops only for a paid mine; a dock serves one docked cart at a
  time (others wait); a free anchor still tallies (opens Farming; pool card price ramps, kept).
- Tags count every piece (home reads sleepy town from the start set; said in the scene).
- PR 3b rule (Claude): the side is by the centre-to-player way scaled by the room's half-size
  (a plain unscaled way would give a long room's end wall to a player by its long side).

## Open for the user
- Sign cap 4 vs "paid ahead without limit"; B1 broke turned away vs "broke drink free"; whether
  the 💎 emote shows when a worker took no gem (main's behavior, kept).

## Balance questions for the user
- Unlocks: ORE_AXE gem rate, idle INT timing to miner/researcher gates, Farming delay.
- Cities/rail: PRICE_STEP, PER_GEM_MAX, City Stone wood, LOAD_PER_LABOR, SEAT_LOGS, RIDE_SAVE_M,
  RIDE_WAIT_SEC, two 1-gem signs per line; stage-3 log: BRANCH_SHIFTS, LAND_PRICE, office ring.
- Early ramp (first mine, first gems); mine strike 15 s, 1 gem; skilled signs 2-3 gems/shift.
- Stage 2: theft share, ram/ladder numbers, architect gaps, train load.
