# UX run 2026-11-12 (2 h, from ~12:30): progress

## Summary for the user (read this first)
**Try it:** VS Code F5 ("Practice with 5 bots"), or the menu: How to play, then Practice (lesson 1 is preselected).
**Nothing is committed** (not asked); `git status` shows every change. Not run by Claude beyond 3 small screenshots and
headless bot nights.

What changed, in your words:
- **"I don't understand what to do":** practice is now 3 lessons. Lesson 1 has only signs, cures and the creature
  (no tricks, scars, pans, powers or two-at-once), a 6-min night, and a coach line that walks you through it once:
  pick up, notice, look, open notes, give; and when you're sick: tell (it names what you feel and its key), hold still.
  Lessons 2–3 add the other rules with one line each. Tab is now **your notes**: everything you heard, saw and read
  about each friend, each fact saying which creature it rules out (you still combine them; the critic made sure the
  game never says which cure to give). Aim at a friend: one line says what your eyes can read on them right now.
- **Feedback and feel:** a cure's result is a big banner for the giver and the patient (CURED / RIGHT KIND, DIDN'T
  TAKE / WRONG CURE) plus a burst of the cure's colour; shoves and pan hits burst too; a turn kicks the view; a red edge
  and heartbeat when you can see a creature near; the crosshair rings when you can act; items pop into your hand.
  A 3-line feed (top left) keeps claims and results you witnessed.
- **The map:** every room has its own floor (checkered kitchen, red-carpet hall, green study...), signs over each
  doorway name the room beyond and the cure that grows there, the room's name shows as you walk in, and Tab has a
  floor plan with the cure spots and you.
- **Meshy:** 6 item models (3 cures, 2 tools, the pan) and 7 furniture props (stove, desk, dining table, clock,
  barrels, bookshelves, cherub statues), stretched to fit the old shapes' collision, and the 3 creatures as static
  models with their own silhouettes (shaggy werewolf, thin caped vampire, hulking mossy troll), so you can tell which
  one hunts and raise the right cure. Not rigged: they glide with the body's lean. 336 credits; balance 1433. Prompts: `art/concepts/PROMPTS.md`.
- **Icons:** each item's picture (cut from its Meshy concept) next to your hands, on the Tab page and on How to play;
  the give/check bar says what's happening ("Giving Bo the garlic... hold").
- **Your mouse:** Claude's runs never lock it any more.

Checked: 39/39 tests (1030 asserts, incl. the new notes); headless nights (lesson 1 with 6, full rules with 8) end at
dawn with no errors; screenshots: the coach line, the hall's floor, a doorway sign, the bookshelf and thermometer models.
Not checked: how any of it feels, the floor plan, notes page and icons on screen (the screen locked while you were
away, and a locked screen draws ~1 frame/s, so no more shots; `--tab` opens the page for a shot later), banners, the danger edge, the item models
on the floor, voice/online with the new HUD, performance with the models.
Open choices: `docs/questions.md` (12–15).

User's asks: "i dont understand what to do in the game.. could you improve about readability and UX?" "for 2 hours
straight". Mid-run: "unfocus", "my mouse shouldnt be focusing the game".

| Ask | Task | Status |
|---|---|---|
| mouse | Claude's runs never lock the mouse (`--no-capture`, added by tools/ai_run.sh) | done |
| readability / UX | research (`docs/ux-research.md`) | done |
| | thesis (`docs/ux-thesis.md`) -> critic -> synthesis | 3 rounds; no severe left |
| | build: hands, item labels, look readout, case notes (log), feed, practice coach, practice lessons, Tab page, How to play | done (untested by play) |
| feedback + game feel (mid-run ask) | cure result banners + bursts, shove/pan bursts, FOV kick, danger vignette + heartbeat, crosshair ring | done (untested) |
| map (mid-run ask) | room floors, doorway signs, "you are here" line, floor plan on Tab | done (untested) |
| Meshy (mid-run: "you can use meshyai") | 6 items, 7 props, 3 creatures (static): concepts reviewed, then 3D | done: 16 models in |
| | tests at the end + headless bot nights | done |

Rules: no commits (not asked); game not run to check work beyond one baseline shot; keep-awake running.

## Log
- 12:31 keep-awake started. 12:33 one baseline screenshot (practice 0:30). It took the user's mouse -> fixed.
- 12:45 research (Phasmophobia journal, teach at the moment of need, guided mock round, keep the centre clear).
- 12:37 thesis written; critic launched. Mid-run asks: feedback + game feel, the map, Meshy.
- 12:42 critic r1: S1 the now line plays the game; S2 rule load parked. Synthesis: no now line, practice coach,
  practice lessons stage the rules, notes are a log. HUD, feel and map built. 12:46 headless lesson-1 night ok.
- 12:47 user AFK. Meshy: 6 item concepts (36 credits), reviewed, image-to-3D (90 credits); critic r2 launched.
- 12:49 6 item models in assets/items/, imported (body.gd loads them; code shapes are the fallback).
- 12:50 screenshot: coach line, hall floor, door sign ok. 12:53 7 furniture concepts, reviewed; 12:55 3D.
- 12:58 critic r2: S1 mirrored floor plan + 4 major -> fixed. Tests 39/39; headless nights (lesson 1, 8 players) ok.
- 13:00 screenshot: bookshelf and thermometer models ok. 13:05 critic r3: no severe; M1 props vs collision -> fixed.
- 13:08 icons from the concepts (hands, Tab, How to play), give/check bar text, `--tab` flag. A Tab screenshot hung
  (screen locked: ~1 fps); the 3 stuck game windows closed. 13:15 tests 39/39; headless lesson-1 night with Tab open ok.
- 13:18 3 creature concepts (shared creature style), reviewed, 3D (8000 poly); body.gd swaps them in over the code
  look (fallback kept, name tag raised). 13:21 headless nights forcing each creature: turn, catch, back to human, no
  errors; tests 39/39.
- 13:08 tests 39/39 (1030 asserts); headless nights lesson 2 (6 players) and full rules (8) end at dawn, no errors.
