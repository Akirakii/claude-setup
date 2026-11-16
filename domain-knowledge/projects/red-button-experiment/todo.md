# To do

Work agreed with the user but not built yet. Newest first; move an item to the matching design doc
(`docs/core-design.md` lists them) once it is decided and built.

Built 2026-11-05 with design v2 (`docs/build-v2.md`), so removed from here: live games first and one
exam per stage, the door and its solo room, the blackout arena (now the Maze; the parkour tower was
dropped: it had no sight split), blame on a culprit (every chore and exam fail names one and slams
the ceiling over them), shop pictures, and the machine-event question (machines are gone).

## From the gameplay anti-patterns review (added 2026-11-03)
See `docs/gameplay-anti-patterns.md`. Not decided yet: each needs a design proposal first.
- **Narrator line repetition (rule 10):** the per-stage pools now hold 5–6 lines each
  (2026-11-06); exam fail lines are single lines with the run's facts in them. Checked in a long
  bot run (2026-11-06, gap review): pooled lines did not repeat; the fixed sold / bought back /
  potato lines did, so they are pools now. Left to check with people: orders repeat by kind
  ("Everyone stand next to X" 3x in 4 minutes). (Wallet trolling got its comeback 2026-11-06: buyer stripe, quick refund.)

## Bots (testing only)
- Bots press by hand and barely use items, so automated runs cannot reach late stages or test
  balance; teach them to throw, bat, fire the cannon and use the trampoline. Throwing done
  (2026-11-06, gap review): bots throw balls at the button; bat, cannon and trampoline not yet.
