# Report: holding a friend (2026-11-13/14, main worktree, uncommitted)

**Built, untested by the user.** Claude ran the unit tests once (90/90 pass) and a 5 s headless practice night to check
that the scripts load. It never played the game. Spec: `docs/holding-thesis.md`.

## Decided
| Call | Who |
|---|---|
| Holding is a chain: the holder walks away and the friend is dragged; the holder stands still and the friend can walk off and snap it | (user) |
| The hand lands on the spot of the body you aim at and sticks there | (user) |
| The arm is 20% shorter | (user) |
| Every reach is 20% shorter: hold 1.44, pick up 2.08, give 1.84, catch 1.36 m; chain at least 1.2 m | (Claude, user said "implement") |
| The werewolf's catch uses the same chain (no more planted S) | (Claude, user said "implement") |
| No time limit on a hold for the first playtest | (Claude, user said "implement") |
| A 0.5 s grip at the start, a snap 2 m past the chain's length, a 3 s guard after a snap | (Claude) |
| "Pulling" needs real movement away (1 m/s), so pushing into a wall is no pull | (Claude) |
| The holder walks at most at a walk, half a walk while the friend pulls the other way; held friends can't sprint | (Claude) |
| Space no longer struggles; mashing is gone | follows from the user's rule |

## Still open
| Open | Where |
|---|---|
| ❌ Why a held friend would pull away in honest step-1 play | questions.md 19 |
| ❌ A hold can last forever (the holder keeps walking) | questions.md 23 |
| ❌ Nothing teaches "walk away to drag" or "walk off when they stop" (no on-screen text in step 1) | |
| ❌ The drag runs on the held player's client, so a laggy holder may make the friend trail or jerk | `docs/holding-thesis.md` gap 4 |

## Tests
| Thing | Unit-tested |
|---|---|
| Walking away pulls; still, sideways, toward, or into a wall is no pull | ✅ |
| A friend slips free from a still holder, with a guard after; letting go is no snap | ✅ |
| A resisting friend slows the holder | ✅ |
| The grip spot is sent and comes back the same | ✅ |
| A dragged friend trails inside the snap; a still holder loses a walking friend in under 0.7 s | ✅ |
| The hand drawn on the body spot, the drag feel, bots holding and catching | ❌ (needs a playtest) |

## Files changed
- Code: `night_sim.gd` (chain rules, reaches, grab/catch grip), `move.gd` (`chain_cap`, `chain_drag`; `link_brake` gone), `player.gd` (drag, no sprint, grip on press, hand on the spot), `game.gd` (chain in poses, grip point, snap sound), `body.gd` (grip spot), `bot.gd` (held and catching bots), `hud.gd` (one hidden hint).
- Tests: `test_night_sim.gd`, `test_move.gd`.
- Docs: `holding-thesis.md`, `design.md`, `build.md`, `questions.md` (19, new 23), `CLAUDE.md` (code map).

## Touches the symptoms design
- Give range is now 1.84 m and pick-up range 2.08 m (both 20% shorter). This barely changes the symptoms sims' fetch-and-give times.
- A held friend still counts as still for a give, so holding someone while another gives still works.
- A held friend can now walk, and a sick one may be dragged to the person with the item.
