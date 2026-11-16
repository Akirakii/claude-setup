# BRAINSTORM: c5 crime and threats (PR 9 pickpocket review, PR 10 wild gear)

Design only, AFK /explode run. Line numbers are `main` 86fc5fb7 in the mm-stage2 worktree unless
a branch is named. Every pick here is Claude's (proposed), except lines tagged (user).

### PR 9: Pickpocket (18c) review and rebase plan
- **Frame:** a puffing friend may lift gems from a nearer friend's pouch instead of a vault, so
  wealth draws thieves; the user picked "merge as built" (user), so this is a review plus a
  rebase, not a redesign.
- **What it does (branch `feat/pickpocket` c9d2c210, 9 files, +116 -34):** `_theft_mark()`
  picks the nearer of `Bank.with_loot` and a friend within `PICKPOCKET_REACH` 12 m with
  `spendable() > 0`, not jailed. STEAL walks to it (`Intent.move_to_node`), at `PILE_REACH`
  `_rob` takes `min(THEFT_GEMS, spendable)` from the victim into the thief's `loot` (😱 over the
  victim, 💰 over the thief). Arrest sends it the one loot path (cop's bag). Cheat `/pickpocket`,
  shared `_thief_scene` helper, probe `pickpockets` in BalanceProbe, sim driver and sim_report.
- **Scene:** a bored hedgehog puffs 💨 by the bar; a rich bartender (5 gems) stands 4 m off, the
  bank 20 m. It trots to the bartender, 😱 pops over the bartender, 💰 over the hedgehog, which
  calms. The cop walks over, jails it, and carries 3 gems off to a sign due a gem.
- **Gaps vs pillars (none blocks the merge; log as TODO):**
  - Holds: stolen gems stay marked (`loot`), shown on the thief, only the police's (user).
    Holds: the item moves by a walk (LAW_game_design rule 20).
  - Natural on sight, add connections: the victim only shouts 😱. Main now has the C2 food
    theft rule "the owner who sees it chases (hot) or calls the police (timid)"
    (creature.gd:1437-1560). A robbed friend is that owner. Reusing it is the obvious next link:
    `docs/TODO_` item, not this PR.
  - Economy drift: main's A1 cut vault growth, so a vault rarely holds gems and the pouch is now
    the usual mark. Theft share and arrests shift: balance question for the user, no tuning.
- **Assumptions to verify:**
  - [x] Main's only base change since the branch is 86fc5fb7 (`git log`, merge base c516194a).
  - [x] Predicted conflicts (`git merge-tree`): 2 files. creature.gd static tallies (main added
    `food_thefts`, `inherited`; branch added `pickpockets`) and the `Mode.STEAL` arm (main split it
    into food theft vs vault, creature.gd:718-725). headless_sim_driver.gd `_finish` dict (main
    added 9 keys, branch 1). README, config, cheats, probe, test, sim_report auto-merge.
  - [x] Auto-merged call sites land right: `_decide_mode` (merged :875) and `_tick_snap`
    (merged :1409) read `_theft_mark()`; main's `Bank.with_loot` and `take` are unchanged
    (bank.gd:37, :102).
  - [x] Test helpers `_ally`, `_bank`, `_brewer`, `_cell` exist on main with compatible
    signatures (test_police_box.gd:41, :50, :244, :251).
  - [x] A bug the branch carries: its `_thief_scene` extraction left `## A station with one
    gem's time paid.` above `_thief_scene`, so `spawn_paid` lost its comment and the helper has
    two (branch diff at cheat_coordinator.gd ~791).
  - [ ] open: `wanted()` on main also reads `reported` (creature.gd:1432); the branch test only
    asserts loot. Expected fine, confirm in the run.
- **Candidates:** 1. rebase as built, fix the two conflicts and the comment: survives (user pick).
  2. Rebase and add the victim chase/report: cut, a redesign the user ruled out. 3. Squash onto
  main by hand: cut, loses the commit and gains nothing.
- **Recommendation:** candidate 1.
- **Build sketch (rebase plan, worktree /home/akiraki/Playground/mm-fixes):**
  1. `git rebase main` on `feat/pickpocket` (or rebase it onto the stack top per merge order).
  2. creature.gd tallies: keep all three lines (`food_thefts`, `inherited`, `pickpockets`).
  3. creature.gd `Mode.STEAL`: keep main's outer split and put the branch body in the else:
     `if stolen_food != null or is_instance_valid(_theft_src): _steal_food_tick()` `else:` the
     `_theft_mark()` walk-or-rob block. Keep main's `Mode.CHASE` and `Mode.INHERIT` arms.
  4. headless_sim_driver.gd `_finish`: keep main's 9 keys, add `"pickpockets"` after them.
  5. cheat_coordinator.gd: move `## A station with one gem's time paid.` back above
     `spawn_paid`; one comment line on `_thief_scene`.
  6. README: move the checklist line `pickpocket: ...` from after `aspire` to the end of the
     done list (after `gem income`), add the PR tag at ship.
  7. Re-check: `_steals_food()` still runs after the gem steal check in `_decide_mode`; the heir
     path (`_spill_pouch`, creature.gd:1650) still passes only `spendable()`, so a robbed
     victim's or a thief's loot never inherits.
- **Tests + cheat key:** run in one boot `-gtest=` test_police_box.gd, test_food_theft.gd,
  test_heir.gd. Branch tests: `test_a_brewer_lifts_the_nearer_friends_gems_as_loot`,
  `test_a_friend_with_only_loot_or_in_jail_is_no_mark`. Cheat `/pickpocket` (built).
- **Shared with other clusters (F15, c5 owns the stolen mark):** the contract is "loot is never
  spent": every gem flow out of a pouch reads `spendable()` (creature.gd:1190, `buy` :1139),
  every inflow adds to `pouch` only; `loot` grows only in `_rob` and leaves only by arrest
  (cop's bag), jail drop or death spill (floor, no heir). c3 tuition, c4 founder capital and
  "full pouch" threshold (F19), rent, wages; c6 tax and trade must read `spendable()`, never
  `pouch`. No second mark field.
- **Open questions for the user:** none on the merge. Later: should a robbed friend chase or
  call the cop like a food owner? Recommend yes, as its own TODO.

### PR 10: Stage 2 threats: wilds with rams and ladders
- **Frame:** once the herd builds for itself, walls cost the player little, so the night must
  answer walls: some wilds bring an ACME ram (breaks a piece fast) or a ladder (climbs a wall
  instead of punching it), and the player's answer is how the walls are shaped.
- **Assumptions to verify:**
  - [x] A wild punches the piece it bumps: native `CrowdBody` calls `_punch_bumped(dt)` for a
    WILD that did not step up (native/src/crowd_body.cpp:348, :396; creature.gd:672-681).
  - [x] Punch time pools on the piece, breaks at `WALL_PUNCH_SEC` 6 dilated s, resets at dawn
    (grid_object.gd:355-372; LAW_rooms rule 5).
  - [x] A wild picks straight-through vs navmesh by time: walk s + `punch_left` sum
    (navigation_coordinator.gd:403-420, `_walk_sec` :423, `_punch` :436).
  - [x] Waves spawn every wild through `WaveSystem.spawn_wild` (wave_system.gd:174); light wilds
    are a debug tier off by default (debug_config.gd:34).
  - [x] Carried props: the weapon socket shows a scene at `WEAPON_SOCKET_OFFSET`
    (weapon_component.gd:46-57); replicated fields sit in one synchronizer (creature.gd:349-370).
  - [x] Walls: `BuildPattern.lay(WALL)` stacks `WALL_BLOCKS` 5 pieces, wheel 1..7
    (build_pattern.gd:5-7, :22-31); the room tool lays a roof (PR 1, `ROOM`).
  - [ ] open: a wild teleported onto a 1 m wall top stands, then walks off and drops inside
    (gravity in CrowdBody). Check in the first test.
  - [ ] open: c2's builder marks the pieces it lays (interface below).
- **Candidates:**
  1. Gear on a wild: a ram multiplies its punch rate; a ladder turns its punch at a low enough,
     unroofed wall into a climb onto the top. Prior art: Stronghold (tall walls vs ladders),
     AoE rams (strong vs buildings, weak vs units), Mount and Blade siege ladders. Survives.
  2. Siege engines as their own objects (a ram cart pushed by 3 wilds, a ladder left at the wall
     that any wild uses, a NavigationLink3D): cut for the slice (new entity, runtime nav links,
     replication); kept as TODO.
  3. Sappers dig under walls (RimWorld): cut, terrain is not editable and not in the PR.
  4. Wilds target creature-built pieces or sites: cut, a hidden targeting rule (R8 said no).
  5. Punch strength grows with the wave number: cut, a flat bonus on a clock gate.
- **Gate (no stage line, user):** gear opens once a creature-built piece stands ("the wilds learn
  from your builders"). Cut: by wave count (clock); once any wall stands (punishes the first
  wall of stage 1); per wild if its target is sealed (gear is fixed at the ring, far out).
- **Recommendation (candidate 1):** night, a ring of 5-high walls the builders raised. A fox
  lumbers in with a log under its arm, bonks the wall: one piece flies out in 1.5 s, not 6 (hole
  shows). A bunny with a ladder hits the wall, stands a beat, and pops onto the wall top, then
  hops down inside. Next night the player raises the wheel to 7 high on one side and the room
  tool roofs the bedroom: the ladder bunny punches there like any wild; the herd meets the ram
  fox at the gap. Mechanism: `gear` on the wild; a ram's punch and path cost run at
  `RAM_PUNCH_MULT`; a ladder wild's bump on a column at most `LADDER_BLOCKS` high with free cells
  above pools climb time, and at `LADDER_CLIMB_SEC` it is set on the column's top. Rams and
  ladders hit any built piece, player or creature laid: a wall is a wall (natural on sight).
- **Build sketch:**
  - creature.gd: `var gear := &""` (&"ram" / &"ladder"), add to SAVED (:55-65) and the
    synchronizer as `".:gear"` (:349-370); setter calls `weapon.show_gear(gear)`. Bump
    save_game.gd:5 VERSION (to whatever the stack holds, +1). `func punch_rate() -> float`
    (RAM_PUNCH_MULT if ram else 1.0).
  - creature.gd:672 `_punch_bumped`: per hit, call new `_hit_piece(piece, contact, dilated)`
    (also the unit-test seam). Ladder: `top := Grid.climb_top(contact_cell, LADDER_BLOCKS)`; if
    found, `_climbed += dilated`; at `LADDER_CLIMB_SEC` set `global_position = top`, zero
    `_climbed`, `ladder_climbs += 1`, `NavigationCoordinator.note_punch(self)`; no punch. Else
    `piece.take_punch(dilated * punch_rate(), dir)`; a ram break bumps `rammed`.
    `contact_cell = Grid.block_from_world(hit.get_position() - hit.get_normal() * 0.05)`.
  - grid_manager.gd (near :222): `climb_top(cell, max_pieces) -> Vector3`: walk up from the cell
    while `get_block` is STRUCTURE; too tall (> max_pieces block heights) or a piece in the 2
    cells above the top (roof): `Vector3.INF`; else `block_to_world(first free cell)`.
  - navigation_coordinator.gd: `wild_next_point` (:258) passes `agent.punch_rate()` (1.0 if not
    a Creature) into `get_next_point_pos` (:294) -> `_recompute` (:389) -> `_punch` and
    `_walk_sec`, which divide punch time by it. Ladders keep the plain cost (TODO).
  - weapon_component.gd: `show_gear(kind)` reuses `_refresh_visual`'s socket; scenes
    `entities/creatures/gear/ram.tscn`, `ladder.tscn` (box meshes). `mult()` is untouched.
  - wave_system.gd:174 `spawn_wild`: after the full-body spawn, `wild.gear = gear_roll()`:
    `&""` with no draw when `get_tree().get_node_count_in_group(&"creature_built") == 0` (so
    today's sims keep their rolls); else ram under `GEAR_SHARE / 2`, ladder under `GEAR_SHARE`.
  - Config: CreatureConfig `RAM_PUNCH_MULT` 4.0, `LADDER_BLOCKS` 5, `LADDER_CLIMB_SEC` 1.5
    (dilated, the `dilated` arg already is); WaveConfig `GEAR_SHARE` 0.25. Placeholders, logged.
  - Probe: static `Creature.rammed`, `Creature.ladder_climbs` in balance_probe.gd
    `counters_snapshot` (~:739) and headless_sim_driver.gd `_finish` (~:876).
- **Tests + cheat key:** new test/ci/entities/creatures/test_wild_gear.gd:
  `test_a_ram_breaks_a_piece_in_a_share_of_the_punch_time` (queued for deletion after
  WALL_PUNCH_SEC / RAM_PUNCH_MULT; a plain wild's piece stands);
  `test_a_ladder_wild_climbs_a_wall_of_ladder_height_onto_its_top` (y at the top, `punched` 0);
  `test_a_roof_or_a_taller_wall_makes_a_ladder_wild_punch` (`climb_top` INF for 6 high and for a
  roofed column; `punched` > 0); `test_gear_rolls_nothing_and_draws_nothing_until_a_creature_
  built_piece_stands` (GameRng state unchanged, then a seeded roll gives a gear).
  test_wild_pathing.gd: `test_a_ram_wild_goes_straight_where_a_plain_wild_walks_round`.
  Cheat `/siege` (HELP "spawn" row, `run` beside `"swarm"` ~:789): a sealed roofless ring of
  5-high walls 6 m ahead (two `BuildPattern.lay(WALL)` L legs through `_piece`), a friend
  inside, a ram wild and a ladder wild 8 m out, gear set directly (skips the gate).
  **Done:** these 5 tests green; `/siege` shows a hole rammed and a ladder hop.
- **Later (docs/TODO_wild_gear.md):** a ladder left at the wall for every wild, knocked down by a
  friend or the axe; ladder path cost; ram splinters to logs after N pieces; a slow ram carrier;
  light-wild gear; trains flatten rail-sitters (stage 3, game_stages Track D).
- **Shared with other clusters:** c2 (builder, PR 2/5): every piece a builder lays joins group
  `&"creature_built"` (the one thing PR 10 reads); c2's "wilds vs a site" (PR 5) treats a site's
  built pieces as ordinary pieces, so rams and ladders apply with no site rule; ghosts have no
  collision. c1 room tool: its roof and Ctrl+wheel height are the ladder counters, no change.
- **Open questions for the user:**
  1. Gate: gear once a creature-built piece stands (recommended) vs once any wall stands?
  2. Rams and ladders against every piece (recommended) or only creature-built ones?
  3. Balance (no tuning here): GEAR_SHARE, RAM_PUNCH_MULT, LADDER_BLOCKS 5 vs the default wall 5.

### Round 2 changes
- Picks (Claude, AFK, proposed): gear opens once a creature-built piece stands; rams and ladders
  hit every piece. These close PR 10 open questions 1 and 2; 3 stays a balance log.
- c2 owns the mark: PR 2's builder adds every piece it lays to group `&"creature_built"`; PR 10
  only reads the group's node count.
- Rail (c6) needs no skip rule. A wild hurts only a piece that blocks it: `_punch_bumped` takes a
  slide collision with a STRUCTURE-layer piece whose normal is not floor-like
  (`absf(normal.y) < 0.7`, creature.gd:676), and native CrowdBody calls it only when the step did
  not climb (crowd_body.cpp:395-396). The path cost counts only STRUCTURE pieces on the line
  (grid_manager.gd:215, `pieces_between`). A ram only scales that same punch, so a track it walks
  over is never rammed. c6's condition: the track is lower than `PhysicsConfig.STEP_HEIGHT` 0.75
  (physics_config.gd:89, it steps up) or is not on the STRUCTURE layer.
- PR 9 now rebases onto the stack top after PR 2-8. The pickpocket diff touches: creature.gd
  static tallies, the STEAL arm, `_decide_mode`, `_tick_snap`, `_theft_mark`/`_rob`;
  creature_config theft consts; cheat HELP, `run` "thief"/"pickpocket", `_thief_scene` beside
  `spawn_paid`; probe `counters_snapshot`; sim driver `_finish`; sim_report; test_police_box;
  README; BRAINSTORM_creature_economy.
  - Job enum rows ARCHITECT, BUILDER, HAUL appended: no overlap, the diff reads no Job.
  - `trade` SAVED field + VERSION 23->24 (PR 3): no overlap, pickpocket adds no saved field and no
    bump. PR 10's `gear` takes the stack's VERSION +1 (25 if nothing else bumps).
  - creature.gd stocker changes (around `_walk_to`, creature.gd:1336-1355): no textual overlap;
    re-check the STEAL arm keeps no `_walk_to` call (the branch replaced it).
  - Likely new conflicts, all append-style, keep both sides: the static tally block, the
    `counters_snapshot` and `_finish` keys, cheat HELP rows and `run` cases (`/architect`,
    `/university`, ...), the README done list. Plus round 1's 2 conflicts with main.

### Old design updates
None. No old BRAINSTORM doc is named for c5; `BRAINSTORM_game_stages.md` Track D (line 105) is
read, not edited (it holds no (user) line to keep and nothing stage 1 changed).

### Round 3 changes (cold review fixes, PR 10)
- SEVERE fixed: `WaveSystem.spawn_wild` (wave_system.gd:174) is static, so no `get_tree()` there.
  Roll gear in the instance caller `_spawn_creature` (:161-170): `var wild := spawn_wild(...)`,
  then `if wild is Creature: wild.gear = _gear_roll()`, with `_gear_roll()` an instance method
  that reads `get_tree().get_node_count_in_group(&"creature_built")`. `/siege` sets gear directly.
- SEVERE fixed: `spawn_wild` returns a LightWild under `DebugConfig.light_wilds` or null on a
  failed spawn: the `wild is Creature` guard covers both (light wilds carry no gear, TODO).
- MED: `_punch_bumped` runs only inside native `move_on`'s `awake` block (crowd_body.cpp:390-398).
  A settled wild pressed on a wall neither punches nor climbs today; the ladder follows the punch
  rule, no new hook (a resting wild has no wish to cross, and settling needs its motor at rest).
  The ladder and ram tests drive `_hit_piece` directly; the `/siege` check keeps the wild chasing
  a friend inside the ring, so it stays awake against the wall.
- MED: PR 10 adds to docs/LAW_time_dilation.md "Dilated", Creature row, after "the rampage and
  its punch pace": "a ladder wild's climb time (`LADDER_CLIMB_SEC`, on the punch's dilated dt)".
  The ram needs no line: it scales the punch dt already listed with the wall punch.
- MED: gear gets its own child node "Gear" under the weapon socket, built by `show_gear(kind)`;
  never "EquippedWeapon", which `_refresh_visual` frees and rebuilds (weapon_component.gd:43-55).
- LOW, for the user's audit: the gate (gear once a creature-built piece stands) is a link the
  player cannot see (black-box pillar: input -> output must read on sight). Candidate readouts
  for a later TODO: the night forecast lists "🪜 ladders, 🪵 rams" once gear is on; or the first
  gear wave shows a banner. Logged as an open question, not built in PR 10.

### Round 4 changes (PR 9 targets, user pick)
- **User pick (user):** a thief takes loose gems on the ground first; it goes for a creature's
  pouch only when no loose gem is in reach. Signs and the vault are not "unowned" targets.
  Loose gems it takes become marked loot, as today. This overrides "merge as built" on targets
  only; the rebase plan above stands.
- **Reading (Claude, proposed):** the vault stays a mark as on the branch (the nearer of the vault
  and a pouch), but only after the loose-gem tier comes up empty. "Not unowned" means a gem
  lying on a sign's or a vault's pay spot is that piece's, not loose.
- **Which function:** `Creature._theft_mark()` (branch creature.gd:1330). It becomes two tiers:
  1. the nearest loose gem within `PICKPOCKET_REACH` (12 m, creature_config.gd:157, the same
     radius a pouch is spotted in; no new constant). If one exists, it is the mark;
  2. else the branch's nearer of `Bank.with_loot` and a friend with `spendable() > 0`.
  Its callers stay the same: `_decide_mode` (:794), `_tick_snap` roll (:1287) and the STEAL walk
  (:677-687). `Intent.move_to_node` takes any Node3D, so a drop works as a target.
- **Loose gem:** walk `get_tree().get_nodes_in_group(DroppedItem.kind_group(load(ItemMetadata.GEM_PATH)))`
  (the heir's lookup, creature.gd:1690). Skip a drop that is null, `is_queued_for_deletion()`,
  or held by a pay post. A pay post is a PAID piece whose `_holds(drop.global_position)` is true
  (grid_object.gd:161, `PAY_RADIUS` 1.5 m flat). The bank has a wage, so it is in `PAID` too.
  Add `static func held_at(at: Vector3) -> bool` on GridObject next to `pay_with` (:173), returning
  `not by_distance(at, PAID, func(o): return o._holds(at)).is_empty()`, the same scan `pay_with`
  runs (`pay_with` keeps its loop, since it needs the pieces). A dead friend's
  spilled gems are loose: a thief may beat the heir to them (the heir takes what is left,
  creature.gd:1702).
- **Taking it:** `_rob(mark)` gets a third branch: `var drop := mark as DroppedItem`, then
  `loot = drop.take(CreatureConfig.THEFT_GEMS)` (dropped_item.gd:230 frees an empty stack) and
  `gem_grabs += 1`. The shared tail stays the same: `pouch += loot` (so pouch and loot both rise
  by n), `snap.stop`, 💰. No victim glyph. New static tally `Creature.gem_grabs` in
  balance_probe `counters_snapshot`, the sim driver `_finish` and sim_report, beside
  `pickpockets`.
- **Tests (test_police_box.gd, helpers `_ally`, `_brewer`, `_bank`):**
  - `test_a_brewer_takes_loose_gems_before_a_nearer_pouch`: thief at (3,0,0), a friend with
    pouch 5 at (3.5,0,0), 2 gems spawned by `DroppedItem.spawn(GEM_PATH, 2, (4.5,0,0))`.
    Assert `_theft_mark()` is the drop. One `_combat_tick()` at reach gives
    `[thief.pouch, thief.loot] == [2, 2]`, friend pouch still 5, the drop is queued for
    deletion, and `thief.wanted()` is true.
  - `test_a_gem_on_a_pay_post_is_no_loose_mark_so_the_pouch_is`: a paid station whose sign
    is full (`Wage.MAX_GEMS`), 1 gem lying within `PAY_RADIUS` of it, and a friend with pouch 5
    at 4 m. Assert `_theft_mark()` is the friend. Control: move the gem 3 m off the post and
    assert the mark is the drop.
- **Cheat:** `/pickpocket` and `/thief` stay as they are; the two tests cover both tiers. To see
  tier 1 in play, throw a gem on open ground near a `/pickpocket` thief.
