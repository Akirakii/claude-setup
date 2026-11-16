# TODO: MVP feedback polish

The user asked (2026-10-08, AFK) for polished feedback, UI/UX, and interactivity to reach a
polished MVP. Frame: every verb the player does gets an answer they can see at once, every
control is shown where it is used, and every state the game runs on reads without the
README. Signs only: no item changes gameplay (a sign is not an output).

## Built (2026-10-08)
- [x] **Crosshair prompt and reach.** The crosshair names what a click does (put down and
  throw, place, pick up, details, break, use), turns gold over a creature in grab reach,
  says "walk closer" past it, and has a black outline so it reads at night.
- [x] **Break ring.** Holding left click on a piece fills the same ring as the throw charge.
- [x] **The ghost says why it is red** ("no room" or "need more"); the build menu shows
  pieces you can't pay for in red (still pickable) and how to place.
- [x] **Night and dawn banners;** the statue line turns red with "UNDER ATTACK" for 2 s
  after each hit; the clock shows the speed when sped up (P).
- [x] **Juice.** Squash on landing and when put down; stretch when grabbed or recruited; a
  thrown body hitting a wild shows 💥, a puff, and a camera shake nearby; the throw kicks
  the camera. Puffs on placing, on death, and on hatching.
- [x] **Moment signs.** 🏠 over a creature put down (its home
  moved); 🎉 when a wild joins the herd; 🥚 over both parents when an egg is laid.

- [x] **Esc menu:** resume, retry, main menu, and the controls card, in the end screen's look.
  It pauses only in single player; online Retry is hidden (a host cannot restart under its
  guests). An open panel or the cheat console takes Esc first.

- [x] **A client sees the host's head and cards.** The server picks the glyph and replicates
  it with the sign (red, puffs, loot, jail) and the effect list, so a client draws the same
  balloons, marks and effect cards; warmth and an egg's HP and night replicate too. HP,
  state, the inspector's feelings, the recovery bar and the HUD's rampager name too (#337).

Cheats: `/night` (just before nightfall) and `/dawn` for the banners; F10 herd and F12
fight for the juice; F1 gems for the build menu.

## Next
- [ ] **Sound.** None exists; the SFX and Music sliders drive silent buses. Procedural
  synth (boing, bonk, pop, gong) or wait for assets and hide the sliders: the user's call.
- [ ] Arrows toward the wave spawns (spawn points are server-only), an off-screen pointer to
  the statue, tips that fire on the player's first actions instead of a 7 s rotation.
- [ ] A camera shake toggle in settings.
- [ ] Playtest tooling: each cheat's name lives twice (`CheatCoordinator.HELP` and the
  `match` arms of `run`), and no test catches a cheat without a help line. One registry
  entry per command holding its help and its action would close it.

## AFK decision log (audit these)
| Gate | Resolved as | Why |
|---|---|---|
| Sound in this slice | Deferred | A synth's sound is a taste call; no assets exist |
| Esc menu (PR 9) | Pause only offline; Retry hidden online; controls card always shown beside the buttons | The TODO line's spec; a restart would drop a host's guests; one screen, no sub-page |
| Gate the C no-clip behind cheats | Not done | `DebugConfig.CHEATS` is a constant `true`, so a gate would change nothing |
| Death: 👻 or a plain puff | Plain puff | Fewer parts; the puff already reads as a cartoon exit |
| Crosshair prompts always on, or only the first days | Always on | Short, and shown only when a click would do something |
| Fx paths | A creature reaction rides the existing `emote` RPC (glyph + optional squash); world puffs and the impact shake go through one `NetworkManager.broadcast_fx` | Two paths, one per owner: a creature that lives on, and a point in the world (a dead creature cannot carry its own puff) |
| Shake | Camera `h_offset`/`v_offset` | Projection offsets: the aim ray, a camera child, does not move |
