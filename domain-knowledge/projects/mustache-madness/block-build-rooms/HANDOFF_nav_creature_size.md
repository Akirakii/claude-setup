# HANDOFF: authored navmesh for structures (DEFERRED — needs live show_navmesh)

Companion backlog: `docs/TODO_nav_creature_size.md`. Step 0 + items 1 & 3 SHIPPED (see the
TODO's SHIPPED section). What remains needs a LIVE session (visual eyeball) and was NOT
attempted AFK. This file holds the design facts for that session.

## Measured nav facts (verified against Godot docs + repo)
1. `NavigationPathQueryParameters3D` has NO per-agent radius. Clearance comes only from the
   baked mesh. ONE mesh = ONE body size. BUT `map` IS a query param and Godot supports
   multiple maps (`map_create`, `region_set_map`, `map_get_path(map,…)`) → per-size pathing
   = one map per size class. Feasible if the giant tail ever needs it (TODO item 1 tail).
2. Bigger `agent_radius` bakes fine; it quantizes UP to a `cell_size` (0.25) multiple, so
   clean values only: 0.25 / 0.50 / 0.75… (0.50 shipped, `test_level_navmesh_reachability`
   green, stairs still walkable).
3. Nav bakes from COLLISION, not visual: `PARSED_GEOMETRY_STATIC_COLLIDERS`, mask 129 =
   `WORLD(1)|STRUCTURE(128)`. Structures merged into the terrain bake via
   `procedural_terrain.gd _compose_bake_source` (parses `grid_objects` colliders).
4. Fuse size is UNBOUNDED (`fuse_power` sums, no cap, `combiner.gd`). Collision does NOT
   scale with size today (only the visual does) — the giant tail + floor-sink both stem here.

## Authored-navmesh direction (the deferred task)
Replace "merge structure colliders into the Recast terrain bake" with a per-piece AUTHORED
`NavigationRegion3D` (hand-built `NavigationMesh` via `set_vertices` + `add_polygon`, NO
bake) for player-built floors/stairs. Terrain stays Recast-baked. Goal: exact walkable shape,
no `agent_radius` erosion at the thin stair-wedge toe, per-shape clearance.

Key facts:
- `add_polygon` needs CONVEX, ordered vertices. Floor = 1 quad. Stair ramp top = 1 sloped quad.
- Regions connect ONLY by shared edges within `edge_connection_margin`
  (`NavigationServer3D.map_set_edge_connection_margin`); overlap alone does NOT connect. Main
  risk = stitching authored floor/stair edges to the IRREGULAR baked-terrain edges.
- Authored polygons get NO erosion → author them already inset if wall clearance wanted.
- Touch points: `procedural_terrain.gd _compose_bake_source` (STOP merging structures),
  structure spawn path (`grid_object` / `architect_table` / `SpawnCoordinator`), the stair & floor
  `builds/scenes`, `auto_ledge_linker.gd` (rescans on `nav_baked`).
- SCOPE: prove on the FLOOR piece first (one quad), eyeball show_navmesh.

## Contradiction to respect
Raising `agent_radius` WORSENS Recast erosion at the stair foot. The 0.50 quick-win passes the
reachability test, but the authored-mesh direction is the real fix for the thin-wedge toe
(authored polygons get no erosion).

## Floor-sink (TODO item 2, deferred)
`_apply_visual_scale` scales only the visual child around its local origin; the collision
capsule stays base size. Suspected: a scaled-up visual extends below the collision floor
contact → the bigger the body, the deeper it sinks. Likely fix = offset the visual up by
(scale−1)·half_height, or scale from the feet not the center. INSTRUMENT + eyeball before
architecting — this is a rendering artifact only visible live.

## Design-process note
Headless nav probes here are FLAKY (shared-map sync/pollution) — do NOT trust them. Prefer the
live show_navmesh overlay or the proven single-bake `physics_world_builder.build_region`
harness, one bake per test. Instrument/verify against docs+repo BEFORE asserting a mechanism.
