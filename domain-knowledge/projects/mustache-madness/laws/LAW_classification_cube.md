# Law: classification cube (where every file goes)

Standing law for placing files by scope and role: the role and dependency rules and the
concrete layout (`MEMORY.md` Architecture principles points here).

- **Classification cube v3 (place every file): recursive scope levels.** Every level (entity,
  system, nested sub-scope) has the same slots, each present only if non-empty: its **coordinator**
  (+ its own `.tscn`) at the level root · `components/` · `services/` · `metadata/` (data schemas;
  tuning `*_config.gd` stays at the level root) · `content/<name>/` (one named piece of authored
  content, a variant or a shared piece: scenes + `.tres` + meshes; never a `scenes/`/`assets/`
  type folder) · nested sub-scopes. **Nest iff the domain needs its own coordinator** (control
  flow over ≥2 own parts); else it's a leaf in the parent's `components/`. A shared part or piece
  of content sits at the lowest level covering all its users (root `components/` = cross-entity).
  `util/` is global only (domain-agnostic + stateless); a stateful domain-agnostic primitive
  (`Cooldown`, `LocalClock`) lives in root `components/`. Components exist by ROLE, not reuse: the
  2+-use rule governs helpers/utils, never role placement. Folder = scope + role slot (browsing);
  class suffix = role at the call site (Godot `class_name` is global).
- **Roles:** **Coordinator** (imperative shell: holds ONLY refs to its children + control flow +
  wiring; domain vars live in components, domain functions in services, repeated wiring in utils;
  replaces "Manager"/"Host") · **Component** (stateful model + self-scoped behavior, rich
  not anemic) · **Service** (pure domain core, value in/out) · **Util** (pure domain-agnostic
  primitive). **Aggregate** = Coordinator whose model IS the domain (`Gathering`); don't fabricate
  a coordinator if nothing enumerates the set.
- **Role DAG (load-bearing):** parent Coordinator→its Components + child Coordinators (ONLY place
  state mutates), Coordinator→Service/Util, Component→Util, Service→Util. FORBIDDEN: any child→
  parent call or back-ref (tell: `var creature` in a component), sibling→sibling (the parent
  mediates), Component→Service, Service→Component. **Every parent→child edge = facts in, intents
  out:** the child decides from args and RETURNS intents; the parent executes. Tell of a smuggled
  back-ref: the facts bundle carries the whole entity. Guard: coordinator BREADTH is the point;
  DEPTH (inline "how") moves down. **Cross-scope (not parent/child):** a scope may connect
  to another's signals and read its PUBLIC getters; it mutates only through the owner's public
  verbs. A cross-scope observer lives with the OBSERVER (guide watcher → `systems/guide/`). The cross-scope rule
  covers every file in a scope (a component may call `bed.reserve()`); only parent/sibling edges
  are banned, so parent effects leave a child as intents or signals.
  **Queries direct, commands via coordinator:** child refs are public (no underscore) so readers
  call the component's getters; no pass-through query facades. State-changing verbs stay on the
  coordinator. Grounded: Godot `best_practices/scene_organization` ("an
  ancestor mediates" siblings) + `project_organization` (group by feature, not type).

## Placement rulings
- A coordinator's own scenes/resources sit at its scope root; `content/<name>/` is for
  multi-variant scopes, and a single-file piece may be `content/<name>.tres`.
- An item lives with the scope that defines it: crop foods, seeds and transformed variants
  under `crops/content/<crop>/`; tools under `tools/content/`; build pieces with their build.
- Capabilities other scopes use are owner verbs, duck-typed: `knock()`, `hurt()`; every
  damageable exposes `health`. Rigid stations share `Station` over `PushableBody`.
- Item behaviors are items-scope and receive the acting player as a fact.

## Scopes that stay whole (verdicts; don't re-pitch without new evidence)
- **Aggregates** (the model IS the domain, so the registry lives on the coordinator):
  `TargetManager`, `NavigationCoordinator`, `Grid`, `Gathering`, `BalanceProbe` (a flat
  telemetry aggregator).
- **NetworkManager**: the peer boundary + its wire-protocol RPCs are one concern; splitting
  the RPCs off separates the protocol from the peer that carries it.
- **ProceduralTerrain nav bake**: "terrain is the nav authority" is a load-bearing coupling
  (its nav API is polled by grid objects, ledge linker and tests).
- **Engine-node parents**: a script composing its ENGINE parent (AutoLedgeLinker under a
  NavigationRegion3D) is not a child→parent role edge; only script coordinators count.
- **Scene host ≠ role parent**: HUD panels hosted under the local player are ui-scope views;
  they read player getters and call its verbs, never write its fields.
