# Critic v2.1: "Helping beats fleeing" (2026-11-12)

Scope: the fix to the user's note "running away from the one to transform feels a lot more safer than trying to
save them". The fix has three parts: (1) shudder mark: whoever gave the right kind of cure and saw it shudder can't
be caught by that friend; (2) lone reveal: anyone with no other human within 8 m shows to every hunter within
30 m; (3) a successful cure keeps the curer from getting sick for 90 s.
Read: design.md (turning/hunt, trust, curing, night, critic v2 table), design-anti-patterns.md. Assumed, not
checked: walking speed about 4 m/s, so a "25 s walk from the hall" makes the house about 100 m across.

## Severe

**S1. Fleeing still beats every helping job except giving the cure.**
- Why: the mark covers only the one or two people who gave the cure. Watchers (outer signs are read from 2–5 m),
  tool readers (1.5 s on the patient) and holders (thrown off at the turn) are still the nearest prey when the
  friend turns. The lone reveal is beaten two ways: flee in a pair, or flee more than 30 m away (about 7 s of
  walking, and the end of a case is visible well ahead).
  - At 8 players: 1–2 givers are marked and 5+ people gain nothing by staying. A selfish player flees with a
    buddy and is the safest person in the house.
  - At 4 players: the giver can read the face alone, so the third player still gains nothing by staying close.
  - The user's complaint stands for every job except giving the cure (A18: the fix doesn't reach its target).
- Fix: aim at distance, not at being alone.
  - (a) At the turn, everyone farther than about 15 m from the patient shows to the creature anywhere in the house
    for its first 10 s.
  - (b) Everyone within 8 m at the turn gets a 5 s head start (can't be caught).
  - Then being near is no worse than being far, and helping is the only thing that changes whether a creature
    comes out at all.

**S2. At 2–4 alive, the marks choose the victim, or leave nobody to catch. This breaks two user pillars.**
- Why: cures are capped at 2 of a kind, and a spot takes 120 s to regrow, which is longer than a case. So at most
  2 people can be marked, and the cap decides who can earn a mark.
  - 4 alive with 2 marked: the creature can catch only the one person left. The rules picked that victim, which
    breaks "the hunter chooses freely" and "trust is lost by choosing, not by results the rules force".
  - 3 alive with both givers marked, or 2 alive with the one giver marked: nobody can be caught, so the creature
    must starve. That breaks "catching is the norm" and "once turned, hunting beats starving".
  - Small crews are common: a 4-player night is at 3 alive after its first death.
  - Stretching a case raises the mark count. Holding runs the case at half speed and a pan at a third, which can
    push a case past 120 s; the cure spots regrow, and a third or fourth giver gets marked.
  - Unspecified (A19): does the mark last for this case only? Does the creature see it? Do marked players count in
    "people left to catch" for hunger? What happens when nobody is catchable?
- Fix: turn the mark into a head start: the giver can't be caught for the first 5–10 s of the hunt (the same tool
  as S1b). It never removes anyone from the creature's choices, so the creature never starves because of it.
  Show it to the creature (marked people's outlines are greyed while it lasts).

## Major

**M1. The mark pushes the giver to never guess, and gives stalling and bait a cover story.**
- Why: a right cure leaves the giver safe either way (cured, or marked). A wrong guess makes the case jump a third,
  points blame at the giver, and leaves them unmarked next to a patient who is now closer to turning.
  - So the giver always waits for a second sign, and the cost of waiting (cure odds 95%→65%→30%) moves onto the
    bystanders. That is the core choice going flat (kill line 1).
  - A late right cure looks like help and shields the giver, which makes it undetectable sabotage.
  - A marked giver can hold a friend next to the creature as bait at no risk. This doesn't pay more than curing,
    but it costs nothing.
- Fix: the head start from S2 fixes this too, because a short head start doesn't make the giver safe for the
  whole hunt.

**M2. The lone reveal punishes the most helpful thing you can do alone.**
- Why: during a hunt, the friend who runs to the garden or the tree house for the creature's own cure (to shove it
  back, or break a catch) is alone by necessity, so they get revealed. Fetching a cure during a case is often
  alone too.
- Fix: drop the lone reveal in favour of S1a (the reveal hits whoever was far from the patient at the turn, not
  whoever is alone), or exempt anyone holding a cure.

## Minor

**m1. The 90 s cure reward can't be seen or felt.**
- Why: nobody notices not getting sick (A16: hidden mechanics). Its value also swings with crew size.
  - At 8 alive it skips roughly 1 in 4 chances of being next.
  - At 4 alive it stacks with the patient's 60 s skip and drops the next case onto the 2 people who didn't help,
    which is good there.
- Fix: show it. A shown cue: the curer's journal shows a moon-proof icon with a timer, and others see a faint cue
  on the curer. A visible reward is what makes a selfish player choose to help.

**m2. The lone reveal makes the three creatures play the same against a lone player.**
- Why: wading the pond (werewolf), staying calm (vampire) and staying in the dark (troll) stop mattering for a
  lone player within 30 m. That weakens "each creature has its own ways to deal with it" (user pillar).
- Fix: S1a reveals only for the first 10 s of the hunt; after that, each creature's own sense takes over again.

Exploits checked and not found:
- Everyone feeding the same cure: not possible. A cure is used up, there are at most 2 of a kind, and spots take
  120 s to regrow; only a stretched case gets around this, covered in S2.
- Is the chase dull? Not at 8 players. At 2–4 players it can be decided before it starts (S2).
- "Betraying never pays more than curing" holds as written. Its weak spot is that stalling and bait cost the
  marked giver nothing (M1).

Verdict: the fix misses its target. Fleeing in a pair or more than 30 m away still beats every job but giving the
cure, and immunity-style marks break the free-choice and catching pillars in small crews. Replace all three parts
with one rule: the far are revealed and the near get a head start at the turn, and the giver's mark is a head
start too, never full immunity.
