# Build notes: design v2 (2026-11-05, built by Claude while the user was away)

What exists, how to try every part of it, and which choices were Claude's (not user decisions;
confirm or change them, then record the decided ones in `docs/gameplay-design.md`). Design and
reasoning: `docs/design-v2.md` (settled) and `docs/design-dialectic.md` (four critic rounds).
Old MVP notes (`docs/mvp.md`) still hold for the room, the voice, Steam and the shop hatch; its
events, machines and upgrades are gone.

## Run it
- **Play:** `godot --path .` (menu as before). Alone with bots: `-- --host --bots=2`.
- **Tests:** `godot --headless --path . -s addons/gut/gut_cmdln.gd` (88: every mood, chore, exam,
  route, loop and the new items, on a fake host).
- **Try one thing** (host flags, after `--`):
  - `--stage=N --count=N`: start at stage N (0-based) with that count. Exams gate from stage 3:
    `--stage=2 --count=9900` and press a bit.
  - `--event=NAME`: force a mood (twins, patience, contrary, freeze, runaway, low_grav, reverse),
    a chore (valve, leak, hotbox, fire, stray, potato) or an exam (blink, hunt, maze, sequence).
  - `--path=NAME` (after 3 s): door (sets the ??? in the north wall), box / blocks (puts you in
    that world), vip (sells you), freedom (your city), breakout (panel open), unwatched (door
    open), moon (ceiling hatch open), overflow (two combos in).
  - `--give=ITEM`: any item (hand items go in your hand).
  - `SHOP_ALL_FREE` in `scripts/core/tuning.gd` is still true (every unlocked item free); set it
    false to feel prices and unlocks.

## What is in (all built, all grey boxes)
| Area | Built |
|---|---|
| Scale | 8 stages to 1B; sensitivity S; prices × S; floor lamps around the pedestal light per stage |
| Moods | Twins, Patience, Contrary, Freeze, Runaway + Low Gravity, Reversed; shuffled colours, duds with clues |
| Chores | Valve, Leak, Hot Box, Floor Fire, Stray, Hot Potato; 1–2 slots by crew size; slam over the culprit |
| Exams | Blink, Hunt, Maze, Sequence; the Greedy gate at 1B; seat glare and reader-only signals |
| Items | 15 (9 new: trampoline, cart, blower, tape, balloons, crowbar, dynamite, foil hat, the ??? door) |
| Routes | Escape, Strike, Moon, Breakout, Overflow, Unwatched; six plinths in the exit room |
| Loops | Outside the Box, Block World (solo trap + floor clue map), VIP Room (TV, six buttons, buy back), Freedom, Ghost |
| Meta | unlocks by loss and deed; the lobby pools everyone's unlocks; endings and ghosts saved |
| Narrator | new line pools for every fail, exam, route and the VIP; moods say nothing |
| Sound | 40 new synthesized effects, quiet like the rest |

## Claude's choices to confirm (assumptions, not decisions)
- Fire is stamped out by **crouching** on a tile (the design said E held; crouch is easier to find
  and needs no aiming at the floor).
- The eye stays hidden (`Tuning.EYE_VISIBLE` false, user 2026-11-03 "hide for now"); Unwatched
  works through foil hats alone until it is shown.
- Selling a friend pays 4% of the stage; buying back costs 8%.
- Order fines dropped from 8% to 3% of the wallet per subject (one missed order took ~24% of the
  wallet with 3 subjects, more than a failed exam's 5%).
- Strike counts any tried hit (duds and "full" clanks too) as breaking the quiet, so a crew
  waiting at a frozen gate is not on strike by accident.
- The hot box weighs 20 kg (two lift it; three was the old 30 kg).
- Stage ceiling seconds, sensitivity width, mood and chore gaps: all first guesses in `tuning.gd`.

## Anti-pattern review fixes (2026-11-06, user: "apply")
Review against the three anti-pattern lists, then fixes, all numbers guesses for the playtest:
half-size stages (`SENSITIVITY_WIDTH` 5,000, ceilings 300–360 s); moods 40 s, ×3 for a hit a picky
mood lets through (`MOOD_BONUS`), one chore while a mood runs; two hints per run, the first always
takeable, plus one per loss once the scorers are all unlocked; foil hat after 3 blames; a buyer
stripe and a full refund within 20 s with the buyer named; Block World and the VIP room let go
after 90 s; line pools grown to 5–6. Not changed: hands fading late (user's rule, 11-03). Tests:
101 pass (13 new). The VIP is returned to the room, not walked out by a door (cheaper, no art).

## Visual communication fixes (2026-11-06, user: "apply all fixes")
Against `docs/visual-communication-patterns.md`: sounds of player actions, the hatch, cannon and
impacts play in 3D from their source (`GameSim.sfx(name, at)` / `sfx_by(name, pid)`); every blame
spotlights the blamed player, named or not (snapshot `blame`); Freeze's mover gets the spotlight
too, not colour alone; player colours are now the Okabe-Ito set (colour-blind simulation: worst
pair dE 16); other players' swings and ball wind-up show on everyone's screen (`"wind"` interact).
Checked, no change: popups already merge and cap; the ceiling already beeps under 12 s for all
(a room-wide light would undo "one player reads the timer out"). Visual dictionary written in
`docs/ui-ux-design.md` → Feedback.

## Discovery review fixes (2026-11-06, user: "review this game and fix it")
Against `docs/discovery-patterns.md`: the pedestal shows "count / goal"; hint stains visible
without a flashlight; unreachable hints (item not offered) only fill in last; a too-slow hit on
the button thuds, a soft hit on the weak panel sounds hollow. Checked, no change: Overflow combos
already glitch the screen and counter with a sound and a line. Not changed (playtest): hidden
verbs (crouch on fire, E-E dynamite, cart tap); the 6-hint pool.

## Gap review overhaul (2026-11-06, user away: "find 1000 gaps and fix all of them")
Nine rounds of review and fixes, each with what was run: `docs/gap-review.md` (33 gaps fixed, the
rest parked with reasons, and Claude's choices to confirm). Tests: 128 pass (soak tests added).

## Checked vs not
- **Reviewed:** a reviewer agent went over the whole diff three times; 14 defects found and fixed
  (among them: the block world could not be entered, maze walls never blocked the walker, buying
  at the hatch could sell you to the VIP room, snapshots above the MTU; now split and compressed,
  8 players ~0.7 KB). Its last round: clean.
- **Checked (ran it):** 88 unit tests; headless host + bot clients through every exam (blink, hunt,
  maze, sequence passed end to end), chores and moods firing, VIP sale and buy-back, every
  `--path` view, and a host + separate client with no script errors on either side.
- **Checked (one screenshot):** the room renders with the valve, the twin button and a trampoline;
  the sensitivity rings hid the counter, so they became floor lamps (not re-shot).
- **Not checked:** how any of it looks or feels with people; physics feel of the trampoline, cart
  riding, blower and dynamite; the maze walls for a real walker; the VIP TV picture; the city
  overlay; balance across 8 stages (bots press by hand and barely use items, so they cannot
  reach late stages). Fun is the user's playtest.

## Polish batch from the reference repos (2026-11-06, user: "do until 5")
Patterns copied from `~/Playground/refs/` (index in its README), adapted, no addons imported.
- **Options** (Maaack's template): `GameOptions` (`scripts/core/options.gd`) owns defaults, saving
  and applying; `OptionsPanel` is one list for the title menu (new Options link) and the Esc menu.
  Adds effects / narrator / room-hum volumes (new SFX, Voice, Ambience buses), invert mouse,
  field of view, full screen, v-sync and key rebinding (click, press a key, Esc cancels; Reset
  keys). Window options apply only on a plain launch, so bots and AI runs keep their window.
- **Sound variety:** every effect except tuned cues (countdowns, chimes, alarms) gets ±5% pitch
  and up to 1.5 dB quieter each play; the same sound twice within 35 ms is dropped.
- **Item feel** (COGITO, minus its prompt text): the crosshair grows and goes solid over what E
  acts on; the hand item lags the look, bobs with the walk and rises into view when equipped.
- **Effects:** dust squeezes out when a ceiling slam lands, and it shakes players within 8 m;
  smoke hangs after a blast; fire tiles throw embers.
- **Camera shake** stays the other session's `Feel` ladder; the slam uses it (`Feel.SLAM`).
- **Checked:** 105 tests pass; a host + bot run with fire and a hammer, no script errors.
  **Not checked:** how any of it looks or feels; all numbers (sway, bob, dust, ember counts) are
  first guesses.

## Visible polish (2026-11-06, user: "this is experimental game.. use them of course")
- **One menu theme** (`scripts/ui/game_theme.gd`, Maaack / official GUI demos pattern): the title
  screen's palette (paper, white cards, red, dark ink) for the title menu, Options, the Esc menu
  (now a white card centred on screen) and the shop (paper behind white cards, red edge on hover).
  Toggles are drawn switches, sliders fill red. In-room HUD text keeps white with an outline.
- **Options** is a bordered button on the title screen.
- **Impact burst on the button** (GDQuest 3D effects pattern) for any tool, impact, slam or blast
  hit: a light flash, streaked sparks and a shockwave ring, all scaled by the hit's value. Hand
  presses get none (the routine action stays light).
- New flags for screenshots: `--esc` (Esc menu after 2 s), `--options` (title Options open).
- **Checked:** 107 tests pass; one screenshot each of Options and the Esc menu.
  **Not checked:** the shop and the impact burst on screen; burst sizes are guesses.
