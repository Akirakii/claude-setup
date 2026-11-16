# Godot traps

Concrete engine and tooling traps, by area, each with why it happens.
Check the matching block before touching that area.
File and class names inside are from the game where the trap was hit; they are examples.

## Navigation (Godot NavMesh / Recast)
- **A region's `navigation_layers` changed at runtime may never reach path queries.** A
  query on the new layer came back empty for 120+ frames in test worlds. To judge a walk
  without the links, group the navmesh polygons by shared edges (`NavMeshProbe.island_at`)
  instead of filtering a query by layer.
- **A navigation map whose last region was freed still reports an iteration id.** Treat a
  map as ready only when it also has a region, or path queries on the empty map answer
  "unreachable" and leak test order into results.
- **Godot 4.7 async iterations drop updates.** A mesh set on a region while its async
  iteration builds is lost until the next set (the build's finish clears the sync request,
  the dirty flag stays): project.godot turns `region_use_async_iterations` off
  (`test_nav_region_sync.gd`). Turning a map's async off while its build runs freezes the
  map for good (the finish is checked only while async is on): set it before the first sync.
- **A ramp BAKES into the navmesh, not a NavigationLink3D** (a link = single-point funnel →
  night jam + side-slide). STRUCTURE layer, `cell_size 0.25`, `agent_radius` a multiple of
  the cell.
- Creatures-can't-reach root cause is usually **`agent_max_climb`, NOT `cell_size`** (coarse
  cells terrace smooth hill skirts). A 0.5 cell also rasterizes a thin ramp into a floating
  strip.
- Dense navmesh edges → Recast rasterization error; fix via level navmesh `cell_size
  0.25→0.5`. `agent_radius 0.7` breaks the level_02 bake (reverted).
- Nav respects creature body size via an `effective_radius()` getter; body height =
  2·radius to kill Godot's silent clamp; arrival radius scales with body.
- **A gap or ramp must be 2 m wide to carry a path** (agent radius 0.5, nav cell 0.25): 1 m
  bakes to zero walkable width. `Grid.BLOCK` is sized by this; `test_block_nav.gd` pins it.
- **A fixed body needs a navmesh hole** (group `nav_obstacle`, radius in the meta of the
  same name), or paths run through its collider and creatures jam on it. Godot has no
  runtime carve: the hole is a projected obstruction added at bake, so rebake after spawn.
- **Waypoint arrival is a flat radius plus a height band, never a sphere.** A body's origin
  is above the navmesh; on a bed a tall body (frog) sat 0.54 m over its path's first point,
  outside the 0.5 m sphere, and steered straight down forever.
- Creature nav overwrites `velocity.x/z` each frame, erasing horizontal knockback →
  `KnockbackComponent` hold window. Navlink jump-loops → path-intent gate + walk-off drop.
- **Nav TESTS:** mutating the SHARED nav map's `cell_size` pollutes later tests
  (save/restore). An isolated `map_create` map doesn't sync procedural regions (false
  0/16). Terrain reach-well flake = shared-map region merge lag → poll wells on-mesh, not
  fixed frames.

## Multiplayer / authority
- `NetworkManager._ready` MUST seed an `OfflineMultiplayerPeer` or `is_server()`-gated
  creatures/waves/spawn freeze in singleplayer + GUT.
- `multiplayer.is_server()` crashes on off-tree nodes (multiplayer is null) → gate authority
  at the in-tree RPC handler, never a leaf helper.
- A server entity hitting a client-authoritative player needs `rpc_id` to the owner;
  server-only visual state (creature animation, head glyph, effects) must be replicated:
  a client reads needs, mode and jail as their defaults. Replicate what the server picked,
  not its inputs. `test_client_view.gd` runs a host and a client in one tree.
- `GameRng` per-level seed drives all rolls and is NOT peer-synced. GUT players need name
  "1" for authority.
- Steam P2P: GodotSteam GDExtension + SteamManager autoload + appid 480; flatpak can't reach
  Steam; `host_with_lobby` needs a pre-made lobby; overlay needs a Steam launch.

## GUT / testing
- **`--fixed-fps 60` makes a headless run step as fast as the CPU allows,** so a wait counted
  in frames is no longer a wait in time. `test_terrain_creatures_reach_centre.gd` is unstable
  inside the `physics` dir run (10 of 10 fails on commit b2e8e15 in fast mode, about half
  the runs on the perf branch, once in real time) and passes when run alone.
- **Two Godot processes share `logs/godot.log` and wreck each other's lines.** A launch
  rotates the file (copy, then truncate); a process already running keeps writing at its old
  offset, so its lines land in the new file behind a run of NUL bytes, and plain `grep` calls
  the file binary and prints nothing (`grep -a` reads it). Give a headless run its own log:
  `--log-file <project>/logs/sim.log` (inside the project: the flatpak sandbox cannot write
  to `/tmp`). An open game also takes a core, so a timing run reads about 15% high.
- **`-gdir` does not recurse**: a parent dir with only subdirs runs "Nothing was run" (and
  Godot may SIGABRT on teardown). A dir with its own tests is worse: it passes and silently
  skips its subdirs (`test/ci/ui` runs, `ui/hud` does not). Always add `-ginclude_subdirs`.
- A game-booting probe or sim must run INSIDE GUT (`test/local/`): a `-s` SceneTree script
  cannot see autoloads at compile time, so anything that touches `LevelManager` fails to
  parse.
- Flatpak Godot can write only inside the project (and its user dir): save screenshots to
  `res://logs/` and move them out.
- Flatpak `user://` (headless too) is `~/.var/app/org.godotengine.Godot/data/godot/app_userdata/Mustache Madness/`:
  writable, and shared by every worktree of the project (saves land in one place).
- **GUT hides parse-failed test scripts as "all passed."** New test files need `--import`.
- **A new git worktree has no `addons/` (ignored), so GUT fails to load.** Copy `addons/`
  from another checkout, `mkdir logs`, then run `--import` once.
- StubCreature without `_ready` has no parts bound (`bind_parts`), so `Herd` steps it through
  `_physics_process`: stub that too (no health/collision), else a nil surfaces in a LATER
  awaiting test. A double that binds its parts gets the native step, which calls the script
  only by name (`_think`, `_tick_state`, `_hold_in_world`, ...): stub those instead.
- `StatsComponent.setup()` does not publish: a stub that needs `stats.values` (job gates) must
  call `stats.publish()` after it.
- `-gtest`/`-gdir` only ADD to `.gutconfig.json`'s dirs (`res://test/ci/`), so alone they run
  the full suite. Pass an empty `-gconfig=` to drop that file: then `-gtest`/`-gdir` run
  exactly what they name.
- `get_tree().current_scene = node` needs `node` to be a direct child of the root (else an
  engine error and nothing spawns there); mount a test host with `get_tree().root.add_child`.
- Nested-array signal params crash GUT's diff → use `get_signal_parameters`.
- A new physics/nav test must be added BY NAME to a `ci.yml` shard or the unit leg's shard check
  fails.
- WorldWrap autoload must stay inert (zero bounds) until game.gd; a ±80 default broke the
  multi-map terrain test.

- **A rendered sim needs the screen awake.** With the screen locked or asleep a window draws
  about 1 frame a second, so a windowed perf run measures nothing; headless runs still work.
- **A creature double must turn its own physics callback off** (`set_physics_process(false)`):
  `Herd` is the only caller of a creature's step (`CrowdBody.step`; a real `Creature` has no
  `_physics_process`), and a stub that skips `_ready` and writes one is otherwise stepped by
  the engine as well.
- **A client's creature is told once** (`_remote`, in `_ready`): its step runs its clock and
  nothing else. A test of it needs the body to enter the tree under a peer that is not the
  server (`get_tree().set_multiplayer(api, path)`, `test_herd.gd`).
- **A wave cheat is only that wave if the night is as long:** `/33`, `/36`, `/50`, `/62` set the
  day counter too. With the first night's 7.5 s only ~74 of a late wave's enemies spawn.

## Godot rendering / engine
- **A body standing on a floor pays every depenetration pass of every motion test.** A
  `CharacterBody3D` rests at its safe margin above the floor, inside the band the Jolt
  recovery loop treats as contact, so each test (`move_and_slide` runs two on flat ground:
  the move, then the floor snap) ran all 4 passes at ~1.5 us each: a floor move cost ~20 us,
  one in the air ~2.5. `physics/jolt_physics_3d/motion_queries/recovery_iterations` is 1 in
  `project.godot` for that reason (a sunk body comes out over ~4 steps, was 2). A smaller
  safe margin does not help: the body rests at whatever the margin is.
- **A `Skeleton3D` runs its bone-modifier pass every frame, moving or not,** because the
  engine gives each one an inactive `PhysicalBoneSimulator3D`. About 3 us a skeleton a frame
  (1,100 still bodies: 3.5 ms). With no modifier in use, set `modifier_callback_mode_process`
  to `MODIFIER_CALLBACK_MODE_PROCESS_MANUAL`; clips still pose the bones.
- **`GeometryInstance3D.transparency` above 0 puts that mesh in the transparent pass,** where
  it is sorted and drawn alone. A field of bodies fading that way cost the frame more than
  their whole simulation. Show and hide, or keep it opaque.
- **At 60 Hz with vsync, one slow frame can lock the game at 30 fps.** The catch-up frame runs
  two physics steps, misses the refresh, and so needs two steps again. It only escapes when
  two steps fit in one refresh (`systems/engine/step_governor.gd` drops the debt).
- **`Performance.TIME_PHYSICS_PROCESS` is the longest step of the frame, not the mean.**
  `PerfLog`'s `step=` is the mean script time per step.
- **Emoji on a label with the default font costs ~2 ms per text change:** the engine
  searches the system fonts for a fallback each time. Give the label `EmojiService.font()`
  (emoji faces named first) and it drops under 0.2 ms.
- normal-map → tangent → NaN red; unbound sampler → magenta on Vulkan; emissive materials
  skip toon shading (kill the glow for the wild tint); emoji glyphs depend on the theme
  font's coverage. **Headless hides all of these: verify on GPU.**
- **NEVER call `GameRng` in `_draw`** (desync).
- `no_depth_test` moves a material to the transparent pass with no depth write: a multi-part
  model drawn that way paints its parts in distance order, so the biggest part hides the
  rest. For an x-ray look, keep the parts depth-tested and add one shared flat
  `material_overlay` with `no_depth_test`.
- **A node count is not a frame cost: A/B a node cut before building on it.** Wave 100, ~950
  bodies: 2 plain `Node3D`s fewer a body, or one hidden `MeshInstance3D` fewer, moved the
  headless mean by nothing. What did pay (~0.4-0.5 ms): no `Label3D` on a body until it shows
  text, and per-species data built once, not once a spawn.
- A RigidBody dropped AT `y=surface` with zero velocity spawns embedded in the thin floor
  collider → ~50% tunnels through (resolve direction is a coin flip). Spawn with upward
  clearance + a pop impulse (`DropService.drop_popped`), never `pos=global_position, vel=ZERO`.
- A ~400ms placement stall = a 3.6MB TEXT Meshy `.tres` lazy-loaded → convert to binary.

## UI / input
- **Cursor contract:** a UI that frees the mouse MUST route through `player.use_ui(self)` /
  `use_ui(null)`, NOT poke `Input.set_mouse_mode` or the player's fields directly. Direct
  poking desyncs the look-gate, so look never returns AND a left-click steals the cursor back.
- **Centralized dismiss (one owner = the player):** every open panel claims it via `use_ui`;
  the PLAYER closes it: E/Escape in `_unhandled_input` (so a focused `LineEdit` eats its
  keys first), a click OUTSIDE the box in `_input` (before GUI, beats a full-rect root).
  A UI implements a small duck-typed contract: `close()`, `contains_point()`; opt out with
  `is_dismissable()==false` (forced draft pick) or `blocks_dismiss()==true` (storage while a
  stack is on the cursor). Do NOT re-add per-UI Esc/E handlers or click-catchers.
- **`Input.is_action_just_pressed` polling ignores `set_input_as_handled`.** A UI that
  self-closes on a key can't stop a *polled* opener from re-firing the same frame. Fix: make
  the opener event-based in `_unhandled_input` and mark the close event handled (`_input`
  runs before `_unhandled_input`).
- **The click that dismisses a UI is still physically held** when `_physics_process` runs, so
  a `show_mouse_mode` gate alone leaks that click into a world tool-swing the frame the panel
  closes. Swallow world use until release (`_await_click_release` in `player.gd`).
- **Off-screen indicator (guide bubble):** do it in 2D SCREEN space, not 3D world. Get the
  target's screen point (`unproject_position`; mirror across center when `is_position_behind`),
  scale center→target until it hits the border (`min(bounds.x/|dir.x|, bounds.y/|dir.y|)`;
  per-axis clamp distorts direction), pin via `project_position(edge, depth)`. A 3D world-up
  offset drifts under camera pitch; screen-space stays stuck. See `tutorial_guide.gd`.
- **Center overlays with a full-rect `CenterContainer`**, not `PRESET_CENTER` on a
  content-sized box (that pins top-left to center, growing off-axis). Resolution scaling is
  one `window.content_scale_factor` (`util/ui/ui_scale.gd`): 1080p ×1, 4K ×1.5.

## GDScript
- **An `ItemBehavior` resource is shared by every copy of its item:** per-instance state
  goes in `item.state` (and a stateful item stacks to 1), never in the behavior's vars.
- A subclass `_init` needs `super()`. gdlint bans class-scope `preload` vars.
- **A subclass cannot redeclare its parent's `const`** (parse error), and
  `get_script_constant_map()` returns only the script's own constants: walk
  `get_base_script()` for inherited ones (why a subclass's save list is `CROP_SAVED`).
- `:=` inferred from a dynamic method call can parse-fail → autoload nil → cascade failures;
  use an explicit type.
- **A new `class_name` is invisible to headless GUT until a reimport** (`--headless --import`).
  Moving a `class_name` file: `git mv` the `.gd` AND its `.uid`; callers using the class name
  resolve globally (no path edit), but `.tscn`/`preload` refs by `path=` MUST be updated.
- **Extracting a domain into an `XComponent` (driven via a back-ref):** preserve side-effecting
  calls that ran UNCONDITIONALLY. Making one conditional silently broke navlink arming (the
  creature suite stayed green; the physics/navlink suite caught it). Diff the ORDER +
  unconditional-ness, not just the logic.
- **Off-tree nodes** (`X.new()`, no `_ready`, not in a tree) have a NULL `multiplayer`: guard
  reads with `is_inside_tree()`. Field-initialized components exist off-tree; nodes built in
  `_ready` (health, collision) do not.
- **A method named like a builtin shadows it:** `move_toward` inside a class hides the global
  (misleading "cannot return float" parse errors); `show` overrides `Node3D.show`.
- **Shared ready logic in a base class without `super()`:** handle `NOTIFICATION_READY` in the
  base `_notification` (it runs for every script level); an overridden `_ready` does not chain.
- **A static helper call costs ~5× inline math** (measured: `MathUtil.within` ≈150 ns vs
  inline `distance_squared_to` ≈30 ns per call). Fine at per-tick sites; inline in hot loops.

- **A packed array is shared, not copied, on assignment:** a dictionary holding
  `PackedFloat32Array` sees a later `clear()` of the source. `duplicate()` it when the source
  keeps changing (`SaveGame.capture` baseline).
- **A Dictionary method is not a Callable to bind:** `dict.erase.bind(key)` fails at run time
  ("Invalid access to property or key 'erase'"). Connect a lambda that calls it.
- **A lambda an engine singleton still holds at quit corrupts the heap** (exit 134, "double
  free or corruption"): `Performance` frees its custom monitors after GDScript is gone, and
  the lambda's destructor locks its freed script. Register monitors through `PerfLog.monitor`
  (dropped when the root exits); `test_clean_quit.gd` boots and quits headless to catch it.
- **Two `bind`s of one Callable count as one connection:** `sig.connect(f.bind(a))` then
  `sig.connect(f.bind(b))` fails "already connected". Connect one handler that walks a list.

