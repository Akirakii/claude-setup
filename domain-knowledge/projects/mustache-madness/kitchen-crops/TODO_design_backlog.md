# Design backlog (needs /design before build)

Both items are design-first: don't code until the loop picks a shape.

## More crops = more danger to protect
Right now planting more crops is pure upside (more feed, more poop income) with
no rising defense cost. Goal: scale RISK with crop count/area so a big farm is
harder to protect (a sacrifice source: farm size vs defendability).
Open questions for /design:
- What draws danger to crops? (wilds path to ripe crops? crop density attracts a
  crop-eater enemy? bigger field = bigger patrol perimeter?)
- Is danger per-crop, per-cluster, or per-total-area?
- Must NOT become "fat farm -> bigger wave" (BANNED edge, flattens the arc).
- Ties into the crop nerf shipped 2026-09-04 (grow +25% time, yield -50%).

## Turn-based chaos item
A chaos-pool item that introduces a turn/round-based beat instead of the
real-time loop. Needs design: what "turn" means in a real-time TD-farm, how it
reads on the board (Looney-Tunes goofy), what the player decision is (P4 pillar),
and how it shares the flat draft-value parity of the pool. Pure idea pile stage.

## Creature home-point (anchored roam + battle leash) — DONE, playtest-tune open
SHIPPED as `LeashComponent` (components/leash_component.gd): each creature has a
home point + `LEASH_RADIUS` (12m). Roam clamps its wander onto the leash disc;
`is_entity_valid` gates creature-vs-creature targets to the disc (well/food/tent
exempt). Home re-anchors ONLY on knockback settle or bed sleep. Bundled with the
target-churn fix (deleted the aggro/force-target repoint). Open, needs playtest:
- Tune `LEASH_RADIUS` (12m guess) — too tight = passive, too loose = still drifts.
- Decide wild leash: today wilds share the same leash (home = spawn, re-anchored
  by player bats). They still march because the well is exempt. Confirm this
  reads right, or give wilds a larger radius / advancing re-anchor.

## Bunny mustache placement — IN-EDITOR eyeball pass
Bunny uses the shared `mustache.tres` ArrayMesh (was a placeholder BoxMesh), scaled 0.14 at
a guessed offset. Orientation/position need an in-editor pass (the Meshy model's baked facing
is unverified headless). (The retired daily-level aging is gone: combat + mustache size are
stats-driven now, see the creature code (`entities/creatures/`).)

## Social (Phase 9): more moodlet sources
Comfort is the set of active body-side moodlets (`CreatureConfig.EFFECTS`). Built: ate,
rested (woke healed from a bed), dawn, grief.
Next sources: a campfire aura as a situational moodlet (re-applied each tick while in range,
so it lapses on leaving), shelter. Each is one table row plus its trigger.
