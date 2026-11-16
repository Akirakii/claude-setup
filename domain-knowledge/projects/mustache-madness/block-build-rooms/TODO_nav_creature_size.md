# TODO: creature size in nav + floor-sink

SHIPPED (PR #196, nav respects body size): Step 0 `effective_radius()` getter,
Item 1 agent_radius 0.25→0.50 + base collision bumps, Item 3 arrival radius scales
with body (`test_nav_arrival_body_size.gd`). See `/MEMORY.md` (nav gotchas).

## STILL DEFERRED (need LIVE visual verification — impossible AFK/headless)

- **Item 2 (floor-sink)** below — a fix is a visual-only offset that can only be judged by
  eye in-game. Left for a live-playtest session.
- **Authored-navmesh for structures** — big; needs the show_navmesh overlay to confirm
  stitching. Live session only.
- **Item 1 tail (giants)** — a fused giant is still wider than the 0.50 inset; it wedges.
  Options A (crush-through) / B (size-class multi-map) below, unchanged. Do after a playtest
  shows whether the 0.50 quick-win is enough for the sizes that actually spawn.

## Background: why the old single-mesh nav ignored size (context for the tail work)

Live nav is a SINGLE navmesh; before this PR it was baked at `agent_radius = 0.25` that every
creature shares. The 0.50 bump fixes base species but not the dynamic tail:
- Collision shape never scales with fuse/baby (only the visual does) → nav footprint is the
  same for a base creature and a giant. Giants wedge.
- Big creatures sink into the floor (#2, still open).

## 1 (tail). Nav respects creature size for the DYNAMIC/giant band

**MEASURED FACTS (corrected — an earlier draft got two of these wrong):**
- `NavigationPathQueryParameters3D` has NO per-agent radius/clearance param (confirmed vs
  Godot docs). Path clearance comes ENTIRELY from the baked mesh inset. So a SINGLE shared
  mesh can only serve ONE body size at a time.
- BUT `map` IS a query param, and Godot supports MULTIPLE navigation maps
  (`NavigationServer3D.map_create`, `region_set_map(region, map)`,
  `map_get_path(map, ...)`). So per-size pathing = bake one map per size class and route
  each creature's query to its class map. This is the supported escape from the "one size"
  limit.
- Bigger `agent_radius` DOES bake fine (earlier "won't bake above 0.25" was WRONG — it was
  a GUT test failing on a precision WARNING, not a bake crash). Caveat: `agent_radius` is
  quantized UP to a multiple of `cell_size` (0.25), so only clean multiples avoid the
  warning: 0.25 / 0.50 / 0.75 / 1.0 … VERIFIED: at `agent_radius = 0.50`, level_02 bakes
  clean and `test_level_navmesh_reachability` passes 3/3 (stairs still walkable). cell_size
  stays 0.25 (stairs need it).
- Footprint is DYNAMIC and UNBOUNDED: fuse (`fuse_power` unbounded int, size =
  `1+(fuse_power-1)*0.25`, `combiner.gd:97` sums with no cap) grows infinitely; baby
  (BABY_SCALE 0.5) shrinks. Collision must scale with size (today it doesn't).

**Options (re-open — B is now viable):**
- **Quick win (independent of the fork): bump the single mesh 0.25 → 0.50.** VERIFIED to
  bake + stay reachable. Instantly gives every base species (≤0.30) real clearance so they
  stop skimming. Cost: 0.50 inset is more conservative (paths hug walls less; may block a
  genuinely narrow gap) — playtest. Does NOT solve dynamic size, but a strict improvement.
- **A. Crush/plow-through.** One mesh (at 0.50). Giants are wider than the corridor → PUSH
  creatures / shove light obstacles via physics (reuse knockback) instead of pathing around.
  Fits toon vision. Handles the infinite tail for free. Simplest for the unbounded case.
- **B. Size-class multi-map (now feasible — Wall 2 was false).** Bake N maps at 0.25 / 0.50
  / 0.75 / 1.0; route each creature's `map_get_path` to its class by `effective_radius()`;
  re-register on fuse/mature/baby. Genuinely per-size pathing. Infinite tail: clamp giants
  above the top class to the biggest map + crush-through. Heavier (multi-map coordinator +
  re-register hook + N bakes on structure change).

**Recommendation:** ship the 0.50 quick win first (tested, cheap, fixes the base-species
skim now), then A (crush-through) for the giant tail. Add B only if a middle band of sizes
genuinely needs to path through gaps that 0.50 blocks but 0.25 allows.

REJECTED: per-agent radius in one query (no such Godot param — confirmed docs); RVO
avoidance radius (dynamic agent-agent only, does NOT fix static tight-corner pathing);
post-path clearance re-route (reinvents the engine).

## 2. Bigger creature sinks deeper into floor

**Suspected mechanism (not yet confirmed):** `_apply_visual_scale` scales ONLY the visual
child around its local origin; the collision capsule stays base size. CharacterBody3D floor
contact is held by the collision bottom, so a scaled-up visual extends BELOW the collision
floor contact → visual sinks into the ground the bigger it gets. Fix likely = offset the
visual up by (scale-1)*half_height, or scale from the feet not the center. Instrument
before architecting.

## 3. Big creatures oscillate on the navpath (forward/backward limit cycle)

**Suspected mechanism (not yet confirmed):** waypoint arrival in
`NavigationCoordinator._next_waypoint` advances the cursor only when
`dist_sq(from, path[cursor]) < NAV_WAYPOINT_ARRIVAL_SQ`. A big creature (bigger body,
maybe higher speed/step) can OVERSHOOT the waypoint each frame without ever landing inside
the arrival radius → it turns back, overshoots again → forward/back oscillation. The stuck
watchdog then forces a fresh path to the same waypoint, sustaining the limit cycle.
Likely fix = scale NAV_WAYPOINT_ARRIVAL_SQ (or the steering slowdown) with body radius, or
switch to "advance when we pass the waypoint plane" instead of a fixed arrival sphere.
Instrument: log cursor + dist + velocity for a big creature to confirm overshoot before
fixing. May be the SAME root as item 1 (body wider than nav corridor) — verify.
