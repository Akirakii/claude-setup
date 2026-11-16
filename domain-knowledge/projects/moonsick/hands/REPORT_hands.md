# Report: hands (2026-11-13, branch `hands`, uncommitted)

Everything here is **untested by the user**. Claude never ran the game: it ran one parse check, a one-frame headless start to compile, and the test suite.

## What works (in code)
| Thing | Built | Unit-tested |
|---|---|---|
| LMB = left hand, RMB = right hand; no active hand, R and wheel gone | ✅ | ✅ `test_hands.gd` |
| Empty hand: the mitten reaches to the glowing item, waits there for the host, comes back with it | ✅ | ❌ (visual) |
| The host puts the item in the hand that reached | ✅ | ✅ |
| Cure + creature out or turning → hold to raise (one cure up; last button pressed wins) | ✅ | ✅ |
| Cure, no creature → hold 2 s on a friend to give (mitten reaches and closes); last alive → eat | ✅ | ✅ (the table) |
| Give/eat only on a fresh press; a turn ends every give; a held cure button then raises | ✅ | ✅ (the table) ❌ (the client flow) |
| Others see a giver's arm reach and a creature's arm on its victim | ✅ | ✅ (the host's reach state) |
| A hand shows only while reaching, holding, giving, raising or catching (Q20) | ✅ | ❌ |
| E picks up into the empty hand, left first; G drops one item, left first (Q21) | ✅ | ✅ |
| Catch link (Q19): 0.5 s grip, then the victim may walk away; the creature holds S to pull back; 2 m of stretch snaps it; 3 s guard after a snap; a raised wolfsbane still breaks it | ✅ | ✅ |
| Bots: a catching bot pulls fully; a caught bot is braked; bots pick into the first empty hand | ✅ | ❌ |
| Shove range 2.0 → 2.3 m (Q22, one constant) | ✅ | ✅ |
| New sounds: snap, turn-back (calm), starve (no longer the catch scream) | ✅ | ❌ |

## Test result
✅ 70/70 GUT tests pass, 1157 asserts (`godot --headless --path . -s addons/gut/gut_cmdln.gd -gexit`).

The suite ran twice: after the first pass, a review found that a fleeing bot escaped before a human werewolf could react, so Claude added the 0.5 s grip and ran it again.

## Files changed
- New: `scripts/core/hands.gd` (what each button's hand does), `test/unit/test_hands.gd`.
- Code: `night_sim.gd` (catch link, `pick_up` by hand, give reach, shove range), `move.gd` (`link_brake`), `features.gd` (`catch_link` switch, doubles note), `player.gd` (buttons, mittens, reach, planted pull, brake), `game.gd` (wish in poses, brake at 20 Hz, events, arms), `body.gd` (arms), `bot.gd`, `hud.gd` (hidden texts), `sfx.gd`.
- Tests: `test_night_sim.gd`, `test_move.gd`.
- Docs: `design.md`, `build.md` (controls), `questions.md` 19–22, `CLAUDE.md` (code map).

## Gaps cut
| Gap | Why |
|---|---|
| ❌ Friend-on-friend link: holding is now the click (2026-11-13, user asked), but the held friend still freezes and mashes Space | the r2 interim; waits on Q19's friend half |
| ❌ Trembling hands while sick | Q20 open, not built |
| ❌ Nothing teaches "hold S to pull" or "walk away to get free" | no on-screen text in step 1 |
| ❌ Mitten and arm are code shapes (a wool sphere and a cylinder) | no art pass |
| ❌ A refused pick has no refusal event: the hand comes back after 0.8 s, or sooner if the item is gone | smallest version |
| ❌ Bots still skip input rules (they call the sim directly) | already the case before this change |

## Against or beyond the thesis
- **The catch link was never critic-checked.** Synthesis r1 calls it "not yet critic-checked", and the brief said to build it. It reuses r1's link numbers (brake 0.85, 2 m stretch, 3 s guard), but the stretch counts from where the catch began, not from a fixed 1.5 m. The 0.5 s grip is new (Claude).
- **Balance is unplayed.** A bot werewolf always pulls fully, so a human can't pull free of a bot alone; only a friend's herb saves them, as before. A human werewolf has to hold S within about 0.5 s of the click and keep it pointed straight back, or a bot slips free. Werewolves may starve more often.
- **The creature's feet stay planted while it pulls.** S pulls instead of moving it (Claude, as in r1). Critic r1 #6 left planted vs tow open.
- **The pick hand flies the whole way to the item** (up to 2.6 m, on a stretchy arm). This is Claude's reading of the user's "a hand goes to the object". The thesis only said it "reaches out".
- `catch_link` is on in `features.gd`, even though that file is otherwise all cuts that are off. Set it to false to get the old frozen catch back.

## Reference repos read (rule 19)
- Cogito: the press and the release both go to the held item, and input is blocked while it animates. Copied as: the hand waits at the item, and the same hand can't start a second pick.
- 3D multiplayer template: the client asks the host with `rpc_id(1)`, and the host owns the inventory. Moonsick already worked this way, so nothing changed.
