# Handoff: lag spikes (AFK relay)

## Status for the user's return
- Started 2026-10-26 ~03:00. Base: `feat/tabs-lab-unlocks` at `68c7d691` (the playtest round,
  3 commits ahead of `main`). Machine on the AFK idle config (no power-off).
- MERGED 2026-10-26 into `feat/tabs-lab-unlocks` (#398, #405 = old #399, #400-#404), after a cold
  review whose 6 findings were fixed. Gate: w24 600 s worst 45.6 ms, 0 over 50; suite 1431/1431.
  Worktree mm-lag removed; its bench logs are in `logs/bench/`. Open: user gates below.

## Purpose
No frame over the game's 50 ms spike line (`PerfLog.SPIKE_MS`) in a headless run of a mid-game
state like the user's playtest, and the per-second frame time back to its level before this
session's changes (user pick).

## Known facts
- The user saw lag spikes in a windowed playtest on `68c7d691` (uncommitted then).
- `logs/godot.log` from that run has no `[PERF]` lines although `DebugConfig.log_perf` is
  `true` by default: find out why before trusting any "no spike" result.
- The screen locks while the user is away: windowed runs draw ~1 fps, so only headless numbers
  are valid in this run. A spike that only shows when rendering needs the user present: log it.
- Suspects added this session (unmeasured, do not fix on suspicion):
  `Chair._process` polls `Rooms.revision`/`Grid.revision` every frame per chair;
  `RoomSkins` now watches every placed furniture piece (`grid_object.gd` `_enter_tree`);
  `Housing.reassign` builds `pair_of` with a beds x beds loop calling `paired()`;
  `JobBoard.tick` stand-in search calls `CreatureConfig.shortfall` per idle creature per open
  site each poll; `Jobs.slowdown` runs `eligible_jobs` on every labor tick and `work_done`;
  `Game.start_houses` / two huts at level start (one-off).

## PR list
1. **Spike bench (walking skeleton).** A headless bench (extend `test/local/bench` or
   `util/perf_bench`) that loads a state matching the playtest (herd ~18, both start houses,
   paid woodpile + mine + lab with workers, crops planted, a few chairs and tables in and out
   of rooms) and prints the worst frame ms, the count of frames over 50 ms, and each spike's
   named spans (`PerfLog`). Done: one command prints those three, and `[PERF]` lines appear
   in `logs/godot.log` for a normal launch again (or the reason they don't is fixed).
2. **Fix each spike source the bench names**, one PR per cause, biggest first. Done per PR:
   the bench shows that cause's span gone from spike lines and its per-second ms back down.
3. **Gate.** Done: bench over 10 headless minutes reports 0 frames over 50 ms; full local
   suite passes once on the stack top.

No tuning of game numbers in this relay.

## Resume here
Worktree `/home/akiraki/Playground/mm-lag`, branch `perf/spike-bench`:
`c6142ffe` PR 1 (bench, fixtures, GOTCHAS log note, per-shard `--log-file`), `be2ef18c` WIP
PR 2a (autosave). No PR opened yet. Main checkout untouched (still `feat/tabs-lab-unlocks`).

**Bench:** `util/scripts/spike_bench.sh [save] [game_secs]` (background).
Saves: `res://test/local/bench/saves/playtest_wave11.save` (herd ~18) and
`playtest_wave24.save` (herd ~48). Prints `worst / over_50 / p99 / mean`, then each spike
line after load. Log: `logs/bench/spike_<save>.log`. Refuses on a SCRIPT ERROR (an earlier
run printed numbers from a broken build: always check `herd` is ~49 on w24).
Baselines kept: `logs/bench/base_w24.{txt,log}`, `base_w11.{txt,log}`.

**Measured (playtest, recovered log):** the playtest ran 02:13:53-02:53, herd 3 -> 50.
Its [PERF] lines were not missing: test launches rotated `logs/godot.log` (copy + truncate)
under the open game, which kept writing at its old offset behind NUL bytes; plain `grep`
calls the file binary (`grep -a` reads it). Recovered 2713 second lines + 307 spikes
(rebuild: `grep -a '\[PERF\]'` over `logs/godot2026-10-26T*.log` + `godot.log`, keep lines
without `gpu=0.0 `). 270 of 307 spikes have script < 25 ms (70-330 ms frames, from herd 3):
not script, invisible headless: **user gate** (render / OS / other processes; 6 GUT shards ran
during the playtest). 37 script spikes: (a) autosave at each night, 40-137 ms proc;
(b) one physics step 40-111 ms, twice named `rooms=40-60`, else unnamed; (c) herd 45+:
20-30 proc + 10 step + housing 2-3.
Playtest autosave ms by wave: 1:9, 5:11, 10:18, 15:35, 20:60, 24:81.

**Measured (bench):**
- Baseline 600 s: w24 worst 96.7, over_50 4 (3 autosave frames proc ~84 + spawn 1.5; one
  55 ms at DAWN t=2312.8: proc 25, step 8, ai 3.6, spawn 2.0). w11 worst 41.8, over_50 0
  (the idle bot lets the herd die to 5, so w11 later minutes are light).
- Autosave split w24: grid capture ~45 ms (2332 blocks ~27, 400 crops ~11), creatures ~10,
  store_var + write ~10. Micro: SaveFields.capture on 2332 blocks 27 ms; bare get loop 7.5.
- With the capture plan (be2ef18c part 1): blocks 27 -> 18 ms micro; bench w24 330 s worst
  82.2, over_50 3; autosave 67 (load) / 54 / 59 ms. DAWN spike now seen twice (t=2312.8,
  2465.6: 57 and 54 ms, proc 27-33 unnamed, spawn 2.2-2.6).
- With the block cache (be2ef18c part 2): **unmeasured**. Last run launched: w24 330 s, output
  was in a session task file (lost); rerun it.

**Now (relay 2):** stack on `perf/spike-bench` (mm-lag): `c6142ffe` PR 1 bench,
`3c6121b5` PR 2a autosave, `48d3559b` PR 2b banner, `825c5cf0` PR 2c dawn greet pacing,
`e4c79f15` PR 2d Grid.objects held-cell counts, `ba74d1f5` PR 2e nested capture fast path,
`c53e7e83` docs(save) worker write. Measured w24 (200 s unless noted):
- 2a: autosave on the frame 41-43 -> 26-31 ms (store_var+write ~12 on a worker); night
  frames 65-69 -> 50-55. Save tests 24/24.
- 2b: banner `add_theme_color_override` 3.0 + font size 2.2-2.7 ms per phase change ->
  LabelSettings swap; phase frames -~6 ms. hud tests 27/27.
- 2c: greet_dawn 7.2 ms (moodlet -> `_refresh_status` -> `_glyph` 6.5: wish_glyph scans every
  offer place per friend) -> 8 friends per physics step. First dawn 50-57 -> 43. 22/22.
- 2d: Grid.objects() 4.3 ms (16428 block cells -> 2863 pieces) -> held-cell counts. Autosave
  26 -> 23, night 51 -> 49. grid/save/city tests 68/68.
- 2e: `_encode` remembers scripts it captured in place. Autosave 23 -> 20, night 49 -> 47.
  save folder 31/31.
- **Gate (600 s, full stack): w24 worst 45.1, over_50 0 (baseline 96.7, 4); w11 worst 28.6,
  over_50 0 (baseline 41.8, 0).** Autosave 20 ms steady (load autosave 45).
- Mean frame ms unchanged by the stack (every 200 s variant 9.1-9.4). Not measured: the
  purpose's "per-second ms back to before this session's changes" (vs pre-68c7d691).
- Unexplained, under 50: first-dawn non-script excess ~15 ms; a 42-45 ms frame at t=2333
  (proc ~35, unnamed, not a phase change).
- Full suite on the stack top: 5 shards pass; unit-fast 1 failure, pre-existing from
  68c7d691 (crop nerf left `test_place_clears_footprint` expecting 2-3 berries; yield 1.4).
  Fixed in `99cac47b` (bound 1-2), file rerun 17/17.
- **Review round (coordinator, 6 findings), fixed as fixups + autosquash, force-pushed:**
  1. #399 block cache could go stale (public proprietor/takings setters, shove). /design-code:
     A recheck on hit (autosave 20 -> 22-26 ms; 600 s gate worst 50.26, 1 over: rejected),
     B push invalidation `SaveGame.forget` from the proprietor/takings setters and
     `play_shove_fx` (picked; autosave 19-22, 600 s w24 worst 45.6, 0 over), C no cache.
     Regression test `test_a_cached_block_saves_what_changed_since_the_last_autosave` fails
     with forget as a no-op, passes with it. (Today no path reaches a plain block: _to_found
     scans PAID, tills take takings, the axe frees blocks.)
  2. #399 sessions()/waves()/read()/write() flush a pending write first (newest via sessions).
  3. #399 docs read: handling_quit_requests (quit() sends no WM_CLOSE_REQUEST to nodes, says
     nothing on _exit_tree) and class_workerthreadpool (every task must be waited; nothing on
     shutdown). Not certain -> Game flushes on NOTIFICATION_WM_CLOSE_REQUEST, sim driver
     flushes before quit(); main menu quit runs after Game left (its _exit_tree flushed).
  4. #401 a new DAWN greets the last dawn's stragglers first; queued-for-deletion skipped.
  5. #404 assert message names the nerfed yield.
  6. #398 spike_bench.sh exits 1 with "bench save refused: ..." on any `ERROR: Load:` line
     (checked on a fake log), even when a SIM_RESULT exists.
- **PRs opened (stacked, not merged): #398 bench <- #399 autosave <- #400 banner <- #401 dawn
  <- #402 grid <- #403 encode <- #404 berry test.** Branches `perf/lag-*` (restacked after review: 84a44882 e587a992 8d8c6e5a 412db251 fe4bd16c 98144f55 e6aa6ec4; full suite 1431/1431). Waiting on the
  user: MERGE.
- Remote `feat/tabs-lab-unlocks` is at 47651804; local 68c7d691 unpushed and not pushed by
  the relay (main checkout branch untouched): PR 1's diff shows the playtest round until the
  user pushes it.

**Next:**
1. Rerun `util/scripts/spike_bench.sh res://test/local/bench/saves/playtest_wave24.save 330`;
   expect autosave ~38 ms. Run `test/ci/systems/save/test_save_game.gd` (one boot).
   If an autosave frame still tops 50: move `store_var` + rename in `autosave()` to a
   WorkerThreadPool task (the data is plain values); `test_an_autosave_holds_the_frame_times`
   reads the file right after, so it needs a wait. Then /prune, /rate, commit as PR 2a.
2. DAWN spike (PR 2b): add `PerfLog.span("phase", t0)` around `phase_changed.emit` in
   `world/day_cycle.gd:112` and measure. Dawn runs `greet_dawn()` per friendly (one
   BALANCE_EV moodlet line each), WaveSystem `_end_night`/`_refill_forecast`, egg and lamp
   handlers, balance_probe. Unverified which one costs.
3. Class (b) step spikes (rooms full solve in `Rooms.room_at` from a physics caller) need a
   building action in the bench; the idle bot builds nothing. Unverified in headless.
4. Gate: 600 s on both saves, 0 over 50; full suite once (`util/scripts/run_tests_parallel.sh`).

## Decisions for audit
- Purpose, commit-first and merge-after-review picked by the user (2026-10-26).
- (AFK pick) Bench = the sim driver loading the playtest's own wave saves (wave 11, 24),
  idle policy, not a hand-built state: the saves are the playtest state exactly.
- (AFK pick) The 270 non-script playtest spikes are out of headless reach: left for the user.
- (AFK pick) Per-shard `--log-file` only in run_tests_parallel.sh; run_tests_dynamic.sh has a
  wrong ROOT (`..` from util/scripts) and is left alone.
- (AFK pick) Explode design fan-out skipped: PR 2 causes come from measurement, one at a time;
  each fix designed inline (3 candidates) and logged here.
- (AFK pick) Autosave fix: a per-script capture plan (generic, no consistency risk), then a
  cache of plain block captures (`BuildPiece` with cells, no wage, proprietor or takings:
  placed blocks never change, an axe removes them). Rejected: slicing the capture over
  frames (gems and items could double between slices); a dirty-tracked cache of every piece.
- (AFK pick) Block cache kept after review: a piece with `block_cells` is freed by the axe
  (`hit_by_axe`), never shoved, so its saved fields cannot change while it stands.
- (AFK pick) Autosave frame fix: capture stays on the frame (must precede `_start_night`),
  only the file write goes to a worker. Rejected: deferring the autosave a frame (saves a
  state after the night starts); slicing capture (consistency). Worker logs nothing itself
  (ConsoleLogger uses a RateLimiter static): it sets `_store_error`, the main thread logs.
- (AFK pick) Banner: one cached LabelSettings per [color, size] over write-on-change
  overrides (night and dawn colours alternate, so the colour override would still run each
  phase). Rendering identical by construction (same font, colour, size, outline); not
  seen on screen (screen locked): user playtest gate.
- (AFK pick) Dawn greet: paced like Herd.PERISH_PER_STEP (8 per step) over making moodlet's
  status refresh lazy (~30 call sites refresh at once by design) or speeding wish_glyph.
- Session work committed without `CLAUDE.md` and `docs/HANDOFF_unlocks_stage3.md` (user).
