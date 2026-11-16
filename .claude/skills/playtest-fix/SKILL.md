---
name: playtest-fix
description: Turn the user's playtest feedback into a quick tuning change - find the number or behaviour behind the feeling, change it, test once, log it. Use when the user reports how the game feels after playing ("feels bad", "too slow", "need more air control", "slide should be easier", "too dark"), or asks for a small gameplay or feel change.
---

# Playtest fix

The user's playtest is the real check (the `game-dev` skill); bots and tests only catch things that break.

## Steps
1. **Take the feeling literally.** Find the value or behaviour in the code behind it (grep the constants).
   If the words could mean opposite changes, ask in one line and say what you'd do (coworker style); otherwise act.
2. **Change the smallest thing:** one or two numbers, or one behaviour.
   Leave a comment with the user's words and the old value (`# user: "more air control"; was 6`).
3. **Check what else the change touches:** other systems using the value, network ranges, bots, exploits.
   If a guard test exists (e.g. "a slide chain never outruns a creature"), it must still pass.
   If the change breaks one, say so instead of quietly retuning it.
4. **Test once** after the edits: the project's test suite, plus one headless smoke run if the project has one.
   Add a test when the behaviour is new.
   Don't open the game window (the `game-dev` skill).
5. **Log** the change in the project's design doc as "(user)", with their words.
6. **Reply short:** what changed (old value and new value), what it affects, and "untested in play".
