# Full Moon: critic r4 (isolated, short round, 2026-11-11)

Read: design.md, critic-r3, design-anti-patterns, fix-minigame-feel. Odds and option values below were computed in
python from the design's table, assuming each creature is equally likely, both candidate cures are in hand, reading a
tool takes ~5 s and giving a cure takes 2 s [checked: arithmetic]. Trick vs real-case rates, turns per night, and how
often an outer sign changes the cure picked are [assumed] from the stated GAP and trick rates.

## A. r3 fixes
- S1 (stepped odds): **fixed.** Waiting 8 s to see whether a sign is a trick now costs 95% → 85%. A wrong cure costs
  ~20–25 points wherever it lands.
- Option values for "heartbeats" (P that the first one or two cures work):
  - guess now: 0.77;
  - check with the other row's tool (the thermometer): 0.76;
  - check with a same-row tool (the lantern): 0.72;
  - wait for the stage-2 outer sign: 0.58.
- For "meat", checking wins: 0.78 against 0.76 for guessing.
- Choice alive: **yes at 3 players.**
  - Guessing wins when the sign is surely real and only a same-row tool is near.
  - Checking, or waiting 8 s, wins when a fresh sign may be a trick. That is ~40–60% of fresh signs at 3 players
    [assumed: ~1 trick a minute against ~0.6–1 case a minute].
  - Checking also wins when cures are short: guessing gives 0.45 wrong cures per case, checking 0.22.
  - Waiting for stage 2 is never chosen while a candidate cure is in hand. It is only what happens when no cure is near.
- At 6 players there is always a free pair of hands. A grab halves the case speed, which halves what checking costs:
  grab + check is 0.81 against 0.77 for guessing. "Grab, read, cure" is the likely 6-player routine, and kill line 1
  should catch it.
- M1 (two signs of one kind name the creature): **fixed.**
  - At stage 2, the creature is named in ~45–50% of cases, and only by putting the inner sign and the outer sign
    together.
  - From stage 3 either side can name it alone, but by then the cure is at 43%.
  - New hole: the outer sign now comes after the decision (Major 2).
- M2 (fixed case clock): **mostly fixed.** Some clock tells remain:
  - The GAP never drops below half its average, and anyone cured in the last 60 s is skipped. So for a while after
    each cure, any sign is surely a trick: roughly a third of tricks at 3 players [assumed].
  - Tricks before 0:40 are not ruled out in the rules.
- New hole from the fixes: the patient's half of the Choice is still dead, for a new reason (Major 1).

## Severe: none

## Major
1. **The patient's "say it now or wait to be sure" has one answer.**
   - Why: talking is free, and the patient can say "heartbeats, maybe a trick". Holding a sign back never helps a team
     that shares one goal, so whether to wait is the crew's call, not the patient's.
   - Build B's kill line ("reports every sign the moment it appears") will trip for certain, and gate 7 stays ✗.
   - Fix: give the patient a test that costs them something, e.g. stare into a lamp for 3 s or go sniff the kitchen.
     A real sign flares and a trick doesn't, but the patient's hands are busy and they walk away from the doctors.
     Otherwise, drop the patient's half from the Choice line and rest gate 7 on holding still or struggling.
2. **The outer signs come after the decision, so kill line 2 trips by design.**
   - Why: the odds fall fastest in the first 10 s, and tools work from second 0. With two creatures left, a wrong cure
     already names the right one.
   - So the stage-2 outer sign changes the cure picked in roughly <10% of cures [assumed]. The design's own "intended
     good play" (tool, check fast, cure) never uses it.
   - Taught rule 1 and kill line 2 describe a game the odds don't produce.
   - Fix: per case, pick at random which kind of sign shows first, inner or outer at 0 s, with the other at ~15 s.
     - Half the cases then open on the watchers' side, which gives "keep checking on each other" a reason.
     - A scar becomes the outer look-alike: "is that new, or his old scar?"
     - Or: one tool of each kind, read with a 3 s hold on a still patient.
3. **Candles change no choice, so the run is a life counter (fix-minigame-feel's test fails).**
   - Why: nothing in the night trades survival for a reward. The best play is the same with 6 candles or 0.
     "Candles left over change how boldly the crew guesses" is false, and the 5-night recommendation to the user rests
     on it.
   - The dawn bed is a guess with nothing to go on, since creatures come at random. If not random, it becomes a lookup
     ("always the far salt"), which is A15/A21. It also breaks the "at most 2 of a kind" cap.
   - Fix: one mechanism.
     - At dawn the moon shows tomorrow's omen: one creature at 50%. That raises the one-sign lean toward it from 51–55%
       to 62–68%, so guessing early pays on omen nights.
     - Spare candles (beyond the dead) are what the bed, or a third tool, costs.
     - Few candles then means an unprepared night, and the omen moves the guess-or-check choice.
4. **A turn always costs exactly one death, so the chase only picks who dies. While candles last, the best answer is a
   volunteer.**
   - Why: a catch kills the victim, and running out of HUNGER kills the creature player. Each costs one candle.
   - Being caught costs only downtime until dawn, so the least-needed player walks into the creature and it is over in
     2 s. The chase and the shove, the costliest things to build, become a formality on nights 1–4.
   - A griefer who turns on purpose now burns a resource the whole run shares.
   - Fix: only a catch costs a candle. A creature that runs out of HUNGER collapses and wakes human at dawn, free.
     - With many candles, the crew lets it catch someone and gets it over with.
     - With few, they shove it until its time runs out.
     - The carried stake then changes the night's choice, and a griefer's turn costs only the griefer.
5. **The last night and the win aren't written, and the target depends on them.**
   - Does the 5th dawn bring the dead back with candles? Is the win each player's own ("survivors win") or the crew's
     (at least one alive)?
   - If the 5th dawn revives, a 6-player crew with spare candles plays the full moon with nothing at stake.
   - If it doesn't, leftover candles are worthless, and "the full moon decides" happens on its own.
   - Also unwritten: who comes back when there are more dead than candles. And a lone revived player plays a 6-minute
     night alone while 5 watch.
   - Fix: the 5th dawn lights no candles; each player alive wins (U2); the crew's score is how many are alive. When
     candles are short, the dead come back in order of death, and a crew of one at dawn ends the run.

## Minor
6. **3 vs 6 players, and no kill line for the run.** Candles scale with players, but the danger doesn't.
   - At 3, one death leaves one doctor per case, and the next turn is a 1-on-1, so deaths come in pairs.
   - At 3, a night with no deaths (+1 candle) is common (~60%, [assumed ~0.5 turns a night for a learned crew]). At 6
     it is rare.
   - Likely result:
     - a learned 3-player crew never runs out (no stakes);
     - a new 3-player crew runs out by night 3, then spirals;
     - at 6, six candles leave nights 1–3 with nothing at stake.
   - Fix: add a kill line ("1–2 candles left at dusk of night 5, at both 3 and 6, in at least half the runs"). Try
     ⌈n/2⌉+1 candles (3 players: 3, 6 players: 4).
7. **The dead wait, and the ghost rule assumes silence.**
   - Ghosts wait the rest of the night (≤5 min), and after the candles run out, the rest of the run (a night-4 death
     waits ~10 min). Their job is weak: push loose objects slowly.
   - "The living can't hear ghosts" can't hold on Discord ("silence assumed online", now ×3). Ghosts will call out
     outer signs and scout cures.
   - Fix: say so and make it the job: ghosts see outer signs and may talk, with no hands.
8. **Rules not written, and scene slips.**
   - A wrong cure after 50 s jumps past 75 s: does the friend turn at once? What does a wrong cure do to a case waiting
     at 75 s?
   - A cure on a healthy player looks the same as a failed roll. So "a failed roll tells you the kind was right" is
     false whenever the sign might be a trick, and "a cure never tests anything" is false too: a cure is a test with a
     price.
   - Scene 1: "waits 5 s: it doesn't fade, so it's real" is wrong. A trick lasts ~8 s, and at 5 s the odds are 89%, not
     82%. That makes three times a scene has misread its own rules.
   - Rule 4 makes 4 taught rules, over the cap of 3. Show the candles on the mantel instead of teaching them.

## Verdict
The night is close to buildable: S1, M1 and M2 are fixed, and the doctors' choice is alive at 3 players. But the
5-night structure doesn't yet do what it's recommended for: candles change no choice, and they turn the chase into a
volunteer. Fix Majors 3–5, ideally with the omen + spare-candle currency + "only a catch costs a candle", before it
goes to the user as the pick.
