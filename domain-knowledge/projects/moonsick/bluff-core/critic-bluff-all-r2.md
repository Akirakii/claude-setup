# Critic, round 2: `bluff-all-thesis.md` after the merge, 2026-11-15

Read: the thesis + Merge table, round 1, design-anti-patterns, design.md (Pillars, Trust and bluff, Symptoms, bots);
code `bot.gd` (`_find_patient`, `_treat`, `_patient`, `_observe`, `SEE_RANGE` 7 m), `night_sim.gd` (`public_state`),
`move.gd` (WALK 4.32, SPRINT 8.64 m/s).

## Verdict: round 1 fixed on paper; the human's lie now exists but costs nothing and gains a few seconds
S1 (turning early) and M1/M5 cut: fixed. S2 (head start) taken to the user as Q-B3: fixed by not claiming it.
S3: the human can now break a promise to a bot. But the lie it makes is nearly empty (S1 below), and the moment it
needs almost never comes up with 3 bots (S2 below). No pillar breaks: breaking a deal saves a trip, which the user
allowed ("saves time, never points"). Turning, the only way to cash a betrayal in points, is cut.

## Scene, 1 human + 3 bots, second by second
- Before: the human treated Cy's yawn in Bo's sight, so Bo trusts them at 1.
- 0 s: the human yawns (mild, 45 s). Bo has stink (mild) and holds a coffee; the perfume is 12 m away (inside 15 m).
  Bo, 4 m off, shows "[coffee] for [perfume]" and walks up.
- 0–2 s: the human stands still; Bo gives the coffee. The yawn ends.
- 2 s: honest = sprint 12 m, pick up, sprint back, give 2 s: done at ~7 s. Lie = walk off.
- Lie: Bo waits (for how long isn't written), trust in the human drops below 0. Di, healthy, drifting near
  (`_chores` walks to a friend 60% of the time), sees the stink within 7 m and fetches the perfume herself
  (`_treat` fetches from 80 m). Bo is cured at ~20 s anyway.
- Cost to the human: Bo shows them no more bubbles. Bo still treats them for free when healthy (`_find_patient` has no
  trust check), Cy and Di never learn (bots never tell, and a non-payment isn't a give they count).
- Had Di been within 7 m of the human at 0 s, she'd have fetched the human's coffee unasked, and no deal was needed.

## Severe
- **S1. The lie is free and worth ~5 s: a shallow choice (anti-pattern 15).** 15 m cap → the trip saved is 3.5 s
  sprinting, 7 s walking, + 2 s give; the cost is one bot's bubbles, while it and the other bots keep treating you.
  The human can stiff each of the 3 bots once with no downside. Fix: a bot with trust < 0 also won't treat you (skip
  you in `_find_patient`), so the cost is real; and size the cap so the saved trip matters (e.g. 25 m ≈ 6–12 s),
  checked against the 45 s clock with the sim.
- **S2. The deal almost never fires in the test crew.** It needs five things at once: Bo sick, Bo holding the
  human's item, the human within 5 m, Bo's item within 15 m of the human, trust 1+; and any healthy bot within 7 m
  treats the human for free first (checked in `bot.gd`). Playtest step 7 ("can the human bluff?") then can't be
  tested. Fix: healthy bots treat for free only a friend they trust 1+ (or only when nobody sick near holds the item),
  so the deal is the normal way to get help; count how often it fires in a headless bot run before the playtest.

## Medium
- **M1. "Not paying back" is undefined (anti-pattern 19).** No deadline, nothing on what Bo does meanwhile (stand,
  follow, take it back by tug?), what "below 0" is (−1, or minus the trust it had), or a late payment. Fix: the
  deadline = Bo's own mild clock or 20 s; Bo follows the human; −1; a late pay brings it back to 0.
- **M2. Trust can be farmed.** Any give counts, and an item given to a healthy friend or before its symptom is
  "used up with a burst": 2 s per give, in a bot's sight, buys 1 trust. Fix: count only gives that end a symptom.
- **M3. Fear reads the curse, which no player can see.** Bots see veins only within 4 m (`_observe`), and the curse
  isn't in `public_state`. Fix: nerve on the veins scale, read as a player would (seen within 4 m).
- **M4. Mirrors show what for a mild symptom?** Mild has no veins, so in the coffee lie the mirror adds nothing;
  it only matters in full cases. Fine as the user's offer, but build it cheaply (a mirrored copy of the local body)
  and say it breaks taught rule 1 "you can't see your own face".

## Minor
- Trust +2 for the human's give vs +1 for any seen give: still unexplained; one number.
- A bot giving first needs the human to stand still 2 s: the human must learn that receiving needs stillness (it's
  the existing give rule, so fine, but say it in the scene).
- Standing still for a reach only with no creature out: pass. Sick bots already stop by a friend (`_patient`), so
  it changes little; keep it.
- Part 3 (nothing built): pass.
