# Calibrating the critic against shipped co-op games (2026-11-18)

Asked by the user: "run the critic on all top friendslop games and see if the score matches their popularity", "adjust the critic against the list and their popularity as the baseline.. it should roughly match".
Added by Claude, OK'd by the user: games that sold badly, and games kept aside until the end.
Output: a critic whose score roughly follows popularity, or the finding that a paper critic can't.

- The list and the numbers: `key.md` (14 co-op games, 687k reviews down to 139).
- Popularity measure: Steam review count, on a log scale (checked, one fetch).
- Limit known before the run (Claude): popularity also comes from timing, price, streamers and how well the game is built; a write-up of the rules can't show those.

## Round 1 score, fixed before the run (Claude)
score = 2 × (baseline parts present, 0–4) + (co-op check points passed, 0–7) − 2 × (severe findings of this design alone).
Compared to log10 of the review count by rank (Spearman), on the 10 tuning games only.
The critic also answers ten yes/no observations per game (`critic-brief-r1.md`), collected for the adjusting step and not part of the round 1 score.
The user's limits are left out of this run: the hits break them, and they are checked separately in a real critic round.
- Kept cheap (user): one critic run per game, 14 runs in all; the adjusting is done from the collected table with no reruns; the 4 held-aside games get one run with the adjusted brief.
- Limit seen while the write-ups came in (Claude): the less popular a game, the less is written about it, so its write-up has more "(not found)". The brief tells the critic to treat those as unknown, but a thin write-up can still read as a thin design.

## Round 1 result (10 tuning games, one critic each)
- The score fixed before the run follows the review counts weakly: Spearman 0.20 (checked, script).
- Highest: R.E.P.O. 13; then Content Warning and The Headliners 10; Murky Divers 9; delivery pals 7; Lethal Company and PEAK 6; Chained Together 3; Subterror 0; PANICORE −1.
- So Lethal Company and PEAK score below three games with under 10k reviews: the checklist doesn't separate a hit from a game with the same rules.
- Lines that say nothing because every game got the same mark: blame seen, not solo (all fail), loss is funny, one goal line, solo possible, carry-over.
- Lines that follow popularity a little: rising pressure 0.43, a friend's failure seen 0.41, first minute 0.29, priced help 0.28.
- "Severe findings of this design alone" doesn't follow popularity (−0.16), and the two-way point runs the wrong way (−0.27).
- Simple sums tried after the fact (so they count for less): "a friend acts on a friend" lines + rising pressure + talk + first minute reach 0.53.
- All ten critics read the whole critic-anti-patterns file, the skipped Imps section included (they said so); none used it (their word).

## The comparing critic (one judge, all sheets side by side)
- One blind judge ranked the 10 tuning sheets: g02 > g01 > g03 > g04 > g05 = g07 > g08 > g06 > g10 > g09 (`critics/rank-r1.md`).
- Against the review counts that is Spearman about 0.94 (worked by hand: sum of squared rank gaps 10 over 10 games), against 0.20 for the checklist score.
- The judge named seven traits it used; they are now the questions in `critic-brief-r2.md`.
- The 4 games kept aside, placed on the ladder by a second blind judge that had never seen them (`critics/place-heldaside.md`): Phasmophobia A (true A), RV There Yet? B (true B), Zort C (true C), Unsafe Express D (true D). 4 of 4 tiers right.
- Two leaks that could explain part of this (Claude, not ruled out):
  1. The judge may recognise famous games from their rules, fake names or not.
  2. Less popular games have thinner sheets (3–5 missing facts for the hits, 10–14 for the flops). Against this: Zort and Unsafe Express both have 14 missing facts and were still placed in different, correct tiers.
- A new idea written by Claude has neither leak, so its place on the ladder is softer than these numbers suggest.

## Date and novelty (user: "add into consideration the date it was created and novelty")
- Added to `ladder.md`: when each game came out and whether its core act was new then.
- In all 14 games, every one with a new core act is in tier A or B, and every one that follows an earlier game is in tier C or D (Claude's marking of "new", made after seeing the counts).
- So the critic now starts with novelty: a design that follows an existing game can't be placed above tier C.

## What the critic is for (user, 2026-11-18)
- Not popularity: it "changes through time and trends", so the critic isn't trying to be accurate on it.
- The critic answers one question: is this idea fun with friends or not.
- So the verdict is yes / maybe / no, the shipped games are the examples of fun it compares against, and novelty is reported on its own line without changing the verdict.

## Where the critic lives now
The brief, the ladder, the 14 sheets and the key moved up to the shared fun-with-friends folder, since any project can use them; how it was checked moved to the top-level note `critic-baseline.md`.
This folder keeps the run: the round 1 checklist brief, the critics' reports, and the handoff.
