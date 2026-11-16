# Brief: bluff base, todo parts 1 and 2 (2026-11-15)

User: "Could you start implementing in new tab session" (after "create a todo list for implementing in the game").
Scope: parts 1 and 2 of `TODO_bluff.md` only. Part 3 (cures as places vs carried) must be simulated and picked before anything later is built, so stop after part 2.

Project: `/home/akiraki/Playground/moonsick` (Godot). Work in place: the tree has uncommitted work (hands etc.); don't stash, reset or commit anything.

## Read first
- `/home/akiraki/Playground/moonsick/CLAUDE.md` (code map)
- `/home/akiraki/Playground/moonsick/docs/TODO_bluff.md` (the todo)
- `/home/akiraki/Playground/moonsick/docs/design.md`: "The werewolf's attack", "Symptoms and their items", "Holding and knocking out", "Turning and the hunt", "Trust and bluff" (the "Everyone a little sick" rule with its numbers)
- `/home/akiraki/Playground/moonsick/docs/sims/mild_sick.py` (the numbers)
- `/home/akiraki/Playground/moonsick/docs/build.md` (tests: `godot --headless --path . -s addons/gut/gut_cmdln.gd -gexit`, flags)
- `/home/akiraki/.claude/CLAUDE.md` rules 14, 15, 19 (no game runs to check work; Godot refs in `~/Playground/refs/`)

## Tasks
1. Remove holding's slowdown from the code (held ×0.75 on the curse, and any half-speed case while held). Holding only pulls. Update tests that expect the slow.
2. Rewrite "The game in one sentence" in design.md to match the current design (symptoms and items, everyone a little sick, promises/the coffee lie, the werewolf's attack). Keep it short; tag it (Claude) where it's Claude's wording.
3. The werewolf's new attack (user rules in design.md): a hit knocks the friend back, they're helpless for a recovery time, and it eats at once a friend who isn't moving (standing still or knocked down). "Not moving" = moved less than ~1 m in the last second (bluff-research round B). Pick numbers (knockback, recovery seconds), tag them (Claude) in design.md. Put it behind a switch in `features.gd` like the others.
4. Everyone a little sick: every living friend gets one mild symptom every 90–180 s (one of the 8, shown like a case symptom); it does nothing for 45 s; untreated for 45 s it starts a full case on that friend with it as the first symptom. A friend treats it with its item; nobody treats themselves except the last one alive. Random cases stay as they are. Behind a switch in `features.gd`. Bots should treat mild symptoms the way they treat case symptoms.
5. Pure logic goes in pure scripts with GUT tests (as `symptoms.gd` does). Run the test suite once at the end.

## Limits
- No commits. Don't run the game to check work (rule 14); headless tests only. If you must open it, muted, small, bottom-left, no focus (rule 15).
- A design question the docs don't answer: pick, tag (Claude) in design.md, and list it in the report. Don't stop to ask.
- Mark each todo item done in `TODO_bluff.md`.

## Report
Write `/home/akiraki/Playground/moonsick/docs/REPORT_bluff-base.md`: short, coworker style, a small table (task, done ✅/❌, tested ✅/❌), the test result, the (Claude) picks made, and anything left. Everything is untested by the user.
