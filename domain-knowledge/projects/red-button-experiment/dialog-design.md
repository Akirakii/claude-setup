# Dialog design: the narrator

What the narrator says, when and how. Core loop: `docs/core-design.md`. Check new lines against
`docs/dialog-anti-patterns.md`.

## Role
- The facility's computer: it runs the experiment, gives orders, changes the rules and comments.
- Style reference: The Stanley Parable's dry, polite, condescending narration.

## When it speaks
- **Silent in stage 1.** Its first word in a run is the first milestone ("100.").
- **Speaks often after that:** orders, rule flips, taunts, live reactions.
- **Routine acts get a quip at most** (audit 2026-11-06, ui-ux anti-pattern 7): a plain return's
  refund is said only sometimes; fines, sales and blame are always said (they name a culprit).
- **Every line must matter for play** (user, 2026-11-03: "those just add noise"): players act on
  it or laugh at it. No greetings, welcome-backs or "X has joined" lines.

## Orders
- **Every order is real** (user, 2026-11-03, Simon Says removed because the phrase does not
  travel internationally): shown on screen with a chime and a green ORDER badge; failing it is
  fined.
- Orders escalate with the count: faster, overlapping, per-player.
- The narrator may lie inside events, but the HUD and the button's light never do.

## Memory
- Track many stats per player and across runs (presses, answers, purchases, waste, fines,
  cigarettes, unplugs, deaths, holds, betrayals, streaks, records).
- **Memory is rare and precise.** An event director (like Left 4 Dead's) scores candidate
  callbacks (extremeness, freshness, relevance now, past-run callbacks) and fires only at good
  moments (calm, stage start, blackout; never mid-panic), from a small budget. Cites real numbers.
- Remembers records and nicknames. The past-run and past-cursed-presser callbacks were cut
  (user, 2026-11-03: "remember and memory is too explicit", "the whole thing").
- Balancing callbacks: the slacker and the hog (`docs/gameplay-design.md`).

## Voice
- An AI voice as the facility computer: in-fiction, so it can say real names and numbers. A
  licensed stock voice, never a clone of a real actor. Steam AI disclosure.
- **Piper** (offline neural TTS) at runtime, voice "joe" (US male, CC0) (user, 2026-11-03).
- Optional human actor later for a few key lines ("the person behind the machine").
- Game audio is quiet: master volume 10% by default (user, 2026-11-03).

## Languages
- English voice; every order, question and line is shown as a subtitle (translated later), so no
  gameplay needs understanding speech.
