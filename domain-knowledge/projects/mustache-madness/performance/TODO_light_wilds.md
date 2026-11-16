# TODO: light wilds (`/light_wilds`, off by default)

A wave wild as a light body (`entities/creatures/light_wild.gd`). Measured at wave 100,
headless: about -1.5 ms a frame with the flag on, and a wild fights the same in both tiers.

Open, in order:
- **Playtest with the flag on** (never seen in a window): `/light_wilds`, then `/100` or
  `/swarm`; grab, throw and aim a cheat at a light wild.
- **Default on:** a call for the user after the playtest.
- **A client does not see light wilds:** the flag is server only, a light body is not
  replicated.
- The right-click job panel opens on a full wild and not on a light one.
- `qa_watch`'s stuck and backwards checks skip light bodies.
- `/fight`, `/owl` and `/hedgehog` still spawn full wilds under the flag.
