# GOTCHAS: concrete domain traps (reusable "why", by domain)

Hard-won, engine/tooling-specific traps extracted from `MEMORY.md` (which now holds only
pillars/invariants). These are concrete lessons, not design law. Check the relevant block
before touching that domain.

---

**The engine traps (navigation, multiplayer, GUT, rendering, UI and input, GDScript) moved up to `~/.claude/domain-knowledge/shared/godot/godot-traps.md` (2026-11-16); what stays here is this repo's own tooling, conventions and worktrees.**

## CI / tooling
- **A Flathub build can change without a new version number.** Compare the installed and
  remote `Commit` (`flatpak info` vs `flatpak remote-info --system`), or run
  `flatpak update --no-deploy`, before saying the engine is current.
- `util/probe/presets/index.js` is tracked, but a local capture grows it past GitHub's
  100 MB limit: never `git commit -a` / `add -A` without unstaging it; stage by path.
- **Staging by path is not enough when the user has uncommitted edits in that same file**
  (`CLAUDE.md`, `MEMORY.md`): `git add <file>` sweeps theirs in. Check `git diff <file>`
  first; if it holds lines you did not write, stage only your hunks (a blob built from
  `HEAD` plus your change, via `git update-index --cacheinfo`).
- LFS: materialize via `.git/lfs` cache + `git lfs pull`, NOT `lfs:true` (quota blowout).
  LFS pointers cause Godot "Expected '['" errors.
- `gdformat` is stricter in CI than local and **silently aborts commits: check git log!**
  gdformat↔gdlint can chain-conflict. A multiline-chained `Autoload\n.method(` dodges
  line-based sed = runtime crash.
- After moving an **autoload** script, the first `--import` still reports the OLD path (the
  uid cache lags one run); a second import is clean. CI imports fresh.
- **A sim batch compiles scripts at each process start:** editing a `.gd` while
  `run_sims.sh` is launching gives some runs the half-edited code (a parse error there can
  break an autoload, so those runs play a broken game). Edit only docs until the batch ends,
  and grep the `.out` files for `SCRIPT ERROR` before reading the table.
- **A parse error in a script that autoloads use (`PerfLog`, `Herd`) never ends a headless
  run:** every frame logs the same `SCRIPT ERROR` and the sim loops forever. A comment put
  before a line's closing `:` is enough. Launch a run with a watchdog that kills it on the
  first `Parse Error`, and treat a run past its usual wall time as broken, not slow.
- **A headless run culls nothing:** with no renderer every `VisibleOnScreenNotifier3D` reports
  on screen, so every creature is `_seen` and the sim pays looks and animation for all of
  them (a 16:9 view holds ~35-40%). Read a headless look or animation cost as an upper bound.
- **The native extension builds only with `use_static_cpp=no`** (`cd native && scons
  platform=linux target=template_debug use_static_cpp=no`): Fedora has no static libstdc++.
  A plain `scons` deletes `bin/libcrowd.*.so` before its link fails, and every creature
  then loses its native base. Restore with `git checkout -- bin/` or rebuild with the flag.
- **A seeded sim replays only what no wall clock and no instance id decides.** Same-seed
  runs parted because of three things: an instance id used as a think stagger (ids differ
  run to run: stagger by `save_id` or spawn order), gameplay timers on `Time.get_ticks_msec`
  (use `GameTime.msec()`), and work cut by wall time or finished on a thread (a sliced job, the
  async navmesh bake, the nav map's async sync). `FrameBudget.exact` (on under `SIM_SEED`,
  off with `SIM_WALL=1`) runs that work whole and in step. To find a new source, diff two
  runs' `SIM_TRACE=1` lines and read the first frame that differs.
- CI shard dirs are hardcoded in `ci.yml`. Advisory-lint is non-blocking. **Direct push to
  main is BLOCKED (PR-only).**
- **A `Stop` hook emitting `additionalContext` re-wakes the model → infinite loop when no
  user input follows.** Turn reminders that must reach the MODEL go on `UserPromptSubmit`
  (fires once per real user turn), never `Stop`.

## Repo conventions
- **`TargetableMetadata.max_attackers` defaults to 3.** A target every hostile must reach
  (the statue) sets `-1`, or every hostile past the third idles where it spawned.
- **A creature faces +Z, the player -Z** (`Creature._face`). An offset written in the
  player's frame (`CARRY_OFFSET`) lands behind a creature: mirror z for a creature holder.
- Reuse the existing primitives before writing new ones: `MathUtil`, `Cooldown`,
  `LevelManager.terrain()`.
- Tuning constants live in module-root `*_config.gd` files (tuning only; don't add new
  config files). Physics is tuned only in `systems/physics/physics_config.gd`. `VisualConfig` is
  the single source for visuals.
- A `.tres` sub-resource shadows the script's export defaults: change the value in the
  `.tres`, or the script default never takes effect.
- Simulation runs in `_physics_process`. The scene tree and transforms are not
  thread-safe, and `_process` is render-paced and unsynced.
- Time-based gameplay uses `LocalClock`, `Cooldown`, or `TimeField.scale_at`; see
  `docs/LAW_time_dilation.md`.

## Worktrees
- In a worktree session, Write/Edit absolute paths must target
  `.../.claude/worktrees/<name>/`, not the main repo root (main may be a different branch);
  verify base symbols exist in the worktree first.
- A worktree has no `native/godot-cpp` checkout, so the native extension does not build there.
  Symlink the main checkout's in for the `scons` run, then put an empty dir back: git refuses a
  submodule path that is a symlink.
