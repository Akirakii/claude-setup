# Performance architecture: locality

**Frame.** Cost grows from three habits, not from the creature count itself: idle bodies do
full work every step, every neighbour question scans the whole population, and every local
build recomputes the whole world. The fix is three rules applied at each hot spot's root,
not three new subsystems: the challenger showed each subsystem breaks a premise in the code.

## Pre-pillars (unconfirmed, for the user)
1. **Idle costs nothing.** A body whose inputs did not change does no per-step work; an
   event or a timer wakes it.
2. **Ask only the neighbourhood.** One spatial index is the only way to find nearby
   creatures, beds, or targets; no runtime code scans a whole group per creature.
3. **An edit rebuilds only what it touched.** A build marks a dirty region; rooms, nav
   links, navmesh, and bed ownership recompute inside it, never the whole map.
4. **Same game.** Every change keeps gameplay identical (same choices, same timing); a
   speedup that changes a decision is a gameplay change and goes to the user.
5. **No job runs whole inside one frame.** Work over the frame's budget is sliced or cached
   (a room solve, a ledge scan, a bake input, a field of bodies expiring at dawn).
6. **Nothing grows with play time.** Every table has an owner that erases its dead keys.

Pre-pillars 5 and 6 and the work done under all six (wave 50 and wave 62 runs, 2026-10-11)
are in `docs/TODO_perf_wave50.md`.

## Evidence (headless, --fixed-fps 60)
| Cost | Measured | Class |
|---|---|---|
| Downed bodies (141): move 1.6, view/blink 2.0, behavior 2.4, other 1.2 | ~8 ms / step | idle |
| Ally mode choice (rescue scan O(A x D x A), ~190k checks / step) | 3.5 ms / step | scan |
| Status icon `carried_by` loops (fixed: O(1) table) | 2.1 ms / step | scan |
| Target selection in fights (O(subscribers x targets)) | 11-21 ms / frame | scan |
| Bed search: `map_get_path` per bed per think, uncached | not split | scan |
| Ledge link rescan per build | 205-220 ms | edit |
| Room re-solve per build (whole cache cleared) | ~40 ms x rooms | edit |
| Nav bake input per build | 7 ms | edit |
| Step after a fight (90 allies + 141 downed) | 18.6 ms vs 16.7 | all |

Creature body models are ruled out (box models changed nothing); the rest of rendering
is not: a rendered fight runs 11-16 fps with 45-90 ms of process time, headless 44-60 fps. Physics catch-up is capped at 4 steps
per frame (`project.godot`), so overload shows as 10-16 fps.

## Candidates and prunes
| Candidate | Verdict | Reason |
|---|---|---|
| **Root-local fast paths** (the three pillars applied in place, no new subsystem) | **front-runner** | removes the steady buckets in ~3 files; no wake registry, no clock catch-up, no index bookkeeping |
| Locality subsystems (dormant tier + timer heap, WorldIndex grid, DirtyRegion pipeline) | backtracked | dormancy freezes the dilated clock (day flip, TimeField, decay, recovery drain); the 8 m grid buys 2-3x at 20-40 m radii; dirty AABB misses far links and room rays |
| Data-oriented sim layer (creatures as rows, nodes as views) | long-term shape | same three pillars plus batching; rewrite of creature.gd (1646 lines) and its tests; drift risk |
| Central budget scheduler (think N per frame) | pruned | thinks already spread over 6 frames; demand exceeds budget, so more slicing lowers think rate (gameplay change) |
| Worker threads for creature logic | pruned | scene tree and `move_and_slide` are not thread-safe; still O(N^2) |
| GDExtension / C++ port | pruned | constant factor only; still O(N^2); splits the codebase |
| Lower physics tick rate | pruned | changes jump arcs and timing |
| MultiMesh / server rewrite | pruned | body models are not the bottleneck |
| Physics-server or Area3D neighbour queries | pruned | adds load to the over-budget physics step; cannot filter by game state |
| Exact branch-and-bound target scan | pruned | the HP term (`hp_weight` 1.0, unbounded with VIT) and `hit_me` (any range) break a distance bound |
| Collision layer off for downed bodies | pruned | build placement and AOE splash query that layer |
| Catch-up cap 4 -> 2 | pruned | players own their position; a server in slow motion desyncs from remote players |

## The fast paths (front-runner)
| Pillar | Hot spot | Root-local change | Keeps gameplay because |
|---|---|---|---|
| Idle costs nothing | downed body step | **rest fast path**: DOWN, not held, on floor, still, no knockback -> skip gravity and `move_and_slide`; floor and under-world check at think rate; clock and think unchanged | `knock()` sets velocity, so the body leaves the path by itself; the clock still advances |
| Idle costs nothing | status icon every think | write the glyph and bars **only on change** | same glyph, fewer writes |
| Idle costs nothing | blink | blink at think rate (or a shader time uniform) | same fade curve |
| Ask only the neighbourhood | rescue O(A x D x A) | **bed-first guard**: no free recovery bed -> skip the patient scan | the scan's result is unused without a bed |
| Ask only the neighbourhood | carry check O(N) | O(1) table (done) | same answer |
| Ask only the neighbourhood | target pair loop | **cheapest test first**: squared distance before `_hit_me`, `has_method`, and the candidate Dictionary | same filter, same argmin |
| Ask only the neighbourhood | bed search path per bed | reachability cached per bed until the navmesh changes | same reachable set |
| An edit rebuilds only what it touched | ledge links (205 ms) | **bounded reachability**: `_already_reachable` caps path length (e.g. 3x straight line), so a link depends only on its neighbourhood; then rescan only the dirty area plus jump reach | a link no longer depends on a ramp across the map |
| An edit rebuilds only what it touched | rooms (40 ms each) | **memoize `_sky` / `_walled` rays** per solve (each cell re-casts up to 5 x 48 steps today) | same flood, same verdict |

## Data dictionary
| Name | Type, range | Owner | Definition | Lifecycle |
|---|---|---|---|---|
| `resting` | bool | per creature (derived each step) | DOWN, not held, on floor, horizontal speed < `REST_SPEED`, no knockback | recomputed every step, no stored state |
| `REST_SPEED` | float, m/s | system constant | speed under which a downed body counts as still | fixed |
| `_status_key` | Array | per creature | last glyph and bar values written to the view | rewritten when it differs |
| `_reach_cache` | Dictionary[bed id, bool] | per creature or Bed | reachability of a bed | cleared on `nav_baked` |
| `REACH_PATH_MULT` | float | system constant | max path length / straight distance for a ledge "already reachable" | fixed |
| `_ray_memo` | Dictionary[Vector3i, bool] x2 | per `_solve` call | `_sky` and `_walled` results | dropped when the solve returns |
| `_carried` | Dictionary[holder id, Creature] | Creature (static) | who carries whom | written on grab, erased on release |

## Ownership taxonomy
- **System constants:** `REST_SPEED`, `REACH_PATH_MULT`, `RESCAN_BUDGET_USEC`.
- **Dynamic per-entity:** `_status_key`, `_reach_cache`.
- **Derived each step or call, never stored:** `resting`, `_ray_memo`.
- **Dynamic relational:** `_carried`.

## Interaction matrix (input x fast path)
| Input | rest path | status | rescue guard | target loop | bed cache | ledge bound | room memo |
|---|---|---|---|---|---|---|---|
| velocity / knockback | exits | 0 | 0 | 0 | 0 | 0 | 0 |
| held / grabbed | exits | changes | 0 | 0 | 0 | 0 | 0 |
| floor under body removed | exits (think check) | 0 | 0 | 0 | 0 | 0 | 0 |
| free recovery bed count | 0 | 0 | gates | 0 | 0 | 0 | 0 |
| positions | 0 | 0 | 0 | filters | 0 | 0 | 0 |
| navmesh baked | 0 | 0 | 0 | 0 | clears | regenerates | 0 |
| lattice edit | 0 | 0 | 0 | 0 | 0 | dirty area | per solve |

Every row and column has a non-zero cell.

## Constant ledger
| Constant | Kind | Value | Justification |
|---|---|---|---|
| `REST_SPEED` | limit | ~0.05 m/s (open) | below visible motion; any knock is far above |
| `REACH_PATH_MULT` | limit | ~3 (open) | a detour longer than this is not "already reachable" for a hop |
| `RESCAN_BUDGET_USEC` | pace | 3000 | wall-clock slice, used only if a dirty rescan still spikes |

## Deferred (add only if the measured fight still exceeds budget)
- A shared spatial grid for targets: 2-3x at the current radii (allies scan 40 m on a 90 x
  100 m map), so it waits for the post-fast-path measurement.
- Godot navmesh chunk regions: removes the 7 ms bake input; not a steady cost.
- Transform sync for still bodies (`REPLICATION_MODE_ALWAYS` streams 141 still transforms):
  a network cost, out of this scope.

## Forks for the user
1. **Front-runner vs subsystems:** root-local fast paths now (front-runner), or the full
   locality subsystems with the challenger's fixes (wake events for day flip, TimeField,
   clock catch-up; bounded reachability anyway).
2. **Build spikes in this round or the next:** bounded ledge reachability + room ray memo
   now, or after the steady-state fix is measured.

## Walking skeleton
Rest fast path + status-on-change + rescue bed-first guard, measured on
`test/debug/test_dbg_calm.gd` (90 allies + 141 downed) without instrumentation. Done when
the step is clearly under 16.7 ms and the creatures suite stays green.

## Open assumptions
1. The clean baseline (instrumentation removed) is still over budget; earlier splits were
   inflated by ~1,600 string formats per step from the timers.
2. Late-game recovery beds are usually full, so the bed-first guard skips most rescue scans.
3. Every way a downed body moves goes through velocity (`knock`, carry, gravity on floor loss).
4. Bounded reachability (`REACH_PATH_MULT`) does not drop a link a creature needs.
