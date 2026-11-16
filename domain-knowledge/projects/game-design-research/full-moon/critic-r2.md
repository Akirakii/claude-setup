# Full Moon: critic r2 (isolated antithesis, 2026-11-11)

Read: thesis-r2, thesis-r1 (user words, U1–U10), critic-r1, design-anti-patterns, critic-anti-patterns, DRS
gameplay-anti-patterns, checks.md, triad / idea-search-loop / scope-lessons memory, Full Moon research.md, research.md
2026-11-11 (Mario Party feel; funny vs difficult), fix-minigame-feel.md. No sim this round: numbers are hand math from
the thesis's own table and rules, and an equal chance for each creature [checked: arithmetic]. Map distances, walk speed and
mouse turn speed are [assumed].

## Round-1 fixes
- S1 patient only waits: **partly.** The split exists, but the patient's half alone names the creature in most cases (S1
  below), the mirror shows the patient their own outer signs (M3), and the patient still decides nothing (M2).
- S2 item test gave the answer: **not, in effect.** Tools no longer name it. But the journal does (10 of ~16 sign values
  belong to one creature), and a stage-1 feed is a 90%-reliable test that costs nothing (S2).
- S3 18 rules: **partly.** 3 taught rules (7 clauses), about 12 more to discover, and one of them (holding or knocking out
  slows the case) can't be discovered (M4).
- M1 overlap and spawn luck: **fixed** for U8 and for luck. New holes: the calm conveyor (M1 below) and free items (S2).
- M2 knockout beats holding: **partly.** The 20 s wake rule breaks the chain. Going silent costs almost nothing, because
  stage 2 adds only outer signs: report, then pan (M4).
- M3 the chase only picks who dies: **kept on purpose** (U10, a private stake). Accepted. See m2 for the cone.
- M4 instant dawn rewards betrayal: **fixed.** At 2 alive, not curing gains nothing. New: in the first build a lone
  survivor waits for a certain death (m3).
- M5 the dead sit out: **put off to the full game.** The first 3-human test still has the dead watching (m3).
- M6 one night = minigame feel: **partly.** Scars and deaths carry over inside a night. Between nights, only new creatures
  are added (more content), which doesn't change the in-round push choice (fix-minigame-feel synthesis 1). And the push
  choice (guess or wait) is dead anyway under S1/S2.
- M7 test crew can't play the core: **partly.** The doctor seat can be tested; the coupling and the patient seat can't (M5).
- M8 scope: **fixed.** 3 sign rows, one creature body, no powers: buildable.
- m1 carry cap and unspecified rules: **partly.** Two hands per player, but the crew together carries every cure (S2);
  new gaps in m1.
- Fixes that undo fixes (critic pattern ×2 → ×4): supply follows use → items are free → feeding is a test (undoes S2);
  the mirror tool → the patient sees their own face (undoes S1).

## Severe
Frame verdict: the shape is fun and two-way on paper. The patient feels, friends see, both talk, then guess or wait, cure,
or the friend hunts you. As written, though, the numbers turn it into a lookup with free retries. So the best images of
the fantasy (fur spreading on a friend who doesn't know, the friend hunting you) and U7's pan rarely show up: the logic
cures the friend before the look has a chance to appear.

**S1. The sign table is a list of name tags, so the patient's first sign names the creature.**
- Why: every heartbeat value (racing / slow / none) and every craving (meat / necks / anyone) belongs to exactly one
  creature in the table. Fur, fever, glowing eyes and a faint reflection are also one-creature signs. Stage 1 shows 1 inner
  sign, and 6 of the 7 inner values are name tags. Hand math: about 73% of cases are named by the first sign, 14% show
  "light hurts" (75% vampire), and 12% draw no inner sign at all. The first feed at stage 1 cures about 75% of all cases.
  The thesis's own scene reads the table backwards: "Slow = 60% vampire, so about 55%". 60% is how often a vampire shows a
  slow heartbeat. It is not the chance that a slow heartbeat means vampire, and by the table slow means vampire 100% of the
  time, so a cure is 90%. This breaks U4 ("difficult to analyse"), A21 (solved by run 2: about 10 tags to memorise), the
  Phasmophobia lesson in research.md ("between obvious and impossible"; this lands on obvious), and checks 3.4 (waiting is
  never right). Outer signs and tools are rarely needed, so the split collapses into the patient's own report.
- Fix: give every value to at least 2 creatures. Aim for the best one-sign guess to be right 50–65% of the time, and for 2
  signs together to give ≥ 80%. In the thesis, print P(creature | sign) for every value next to the table, and recheck the
  scenes. Give healthy players inner look-alikes: a sprint raises the heartbeat, lamps glare for everyone now and then,
  food pulls your eye when you're near it. Then "am I sick?" is a judgment, not a beep (this also feeds M2).

**S2. Feeding a cure is a free test, and the crew carries the whole pharmacy, so "feed in turn at stage 1" solves every case.**
- Why: a right cure works 90% of the time at stage 1, so a feed that does nothing rules that creature out 9 times in 10.
  That is r1's swipe test, now paid for with one item. Items are effectively free:
  - STOCK says "held items don't count", so as worded every pickup brings a respawn and hoarding is unlimited.
  - Even if STOCK counts held items, 4 items at 3 players fit in 6 hands (7 items in 12 hands at 6). "Nobody can carry the
    whole pharmacy" is true for one player and false for the crew.
  - A used item comes back within 30 s, and the next case is 120 s away.
  Even with S1's table fixed (best guess 60%, next 30%, last 10%), 3 feeds in about 6 s cure about 93% at stage 1. Waiting
  for stage 2 tops out at 60% a feed. Critic patterns: "a limit that never binds" (STOCK, now ×4), "a fix that undoes an
  earlier fix" (S2), "no carry cap makes a super-player" (now the whole crew). The thesis's "a wrong item is wasted" costs
  nothing.
- Fix (Claude's rules only; U6 holds):
  - A wrong item pushes the patient to the next stage at once. New signs burst out on their body: that is a cost, a visible
    culprit ("Ana fed me salt and now I have fur") and a body gag.
  - STOCK counts held items and doesn't refill on use. Each cure regrows at its own spot on its own clock (wolfsbane in the
    garden bed, garlic in the cellar, salt in the kitchen). That makes the job real (M1).

## Major
**M1. Calm conveyor: most of the night nothing is happening, and at 6 players most of the crew watches.**
- Why: the next case starts 120 s (3 alive) or 60 s (6 alive) after the last one ends, and cases end in about 10–25 s
  (S1/S2). At 3, a case is running roughly 10–20% of the night. At 6, a case needs a patient and a feeder, so 4 stand around.
  The job ("keep the house stocked") is empty, because STOCK refills itself. This breaks critic "one task at a time = a calm
  conveyor", DRS #2, checks 2 "3 and 6: nobody idle" (✗ at 6), and A24 (watchers standing around count as co-op). DOUBLE
  rarely fires, because the first case is usually over before the 10–30 s mark, so U8's "2 at once" mostly disappears too.
- Fix: make tending the cures the job (S2's regrowing spots, out in the garden, where a sick friend's outer signs go unseen).
  Halve GAP (180 s ÷ living), still counted from the end of the last case (keeps U8's rare doubles). Count DOUBLE from the
  first case's start, whether or not it has ended. Let GAP shrink toward midnight (the user's full moon).

**M2. The patient still decides nothing (gate 7, checks 1.4).**
- Why: the patient hears a clear, labelled effect, says it, and stands still. They never doubt it, have no reason to hide or
  lie (checks 2 "hidden things" ✗: no reason to hide), and have no choice in the cure. By night 5 the patient announces the
  sign before anyone asks. Critic "a partner who only stands in place" (×3 now), only now they talk.
- Fix: S1's healthy look-alikes make the patient's call a real decision. "Is this the sickness, or did I just sprint?" A
  false alarm costs a cure (S2), a missed sign costs a stage. Optional: the patient swallows the cure themselves, from what
  friends hold out, so the watchers pick what to offer and the patient picks what to take.

**M3. The mirror shows the patient their own outer signs.**
- Why: in first person a mirror shows your own face: eyes, grey skin, fur. A patient with a mirror (or at a wall mirror, or
  a dark window at night: it's a mansion) holds both halves of the case, which undoes S1's split. Fantasy and logic clash: the
  one object made for seeing yourself is the one you aren't allowed to use on yourself. "Tools on others only" is unstated
  (A19).
- Fix: swap the mirror for a tool that only works pointed at others. For example a lantern: werewolf eyes shine back in its
  light (eyeshine), a vampire casts no shadow, a zombie looks normal. Put no mirrors and no reflective glass on the map.

**M4. Holding and knocking out work invisibly, and going silent costs almost nothing.**
- Why: the meter is hidden and the signs come on a hidden clock, so players can't see that a held or knocked-out patient
  slows down. U7's "prolong" (the user's pillar) can't be discovered, only taught (A16; so this is a 4th rule). Once the
  patient has said their stage-1 sign, knocking them out loses nothing, because stage 2 adds only outer signs. In the dominant
  strategy nobody holds or pans at all (cures are in hand).
- Fix: show the slowing on the body. While held or knocked out, the fur stops spreading and the heartbeat on the patient's
  screen drags. Give stage 2 a new inner sign, so silence costs something. If the slowing can't be shown, add it to rule 2
  ("hold or knock them out to buy time").

**M5. The first build tests the doctor's lookup, not the coupling, and the kill line can't catch the real failure.**
- Why: 2 bot patients are pressure plates by construction (r1's S1, rebuilt for the test). The human never feels the inner
  signs, and whether a person can tell racing from slow, or "necks" from "anyone" in first person, is the patient's whole
  job. The kill line ("asked 'what do you feel?' more than twice") passes under the name-tag lookup. It fails only if
  patients speak up without being asked, which is the split working (critic "a check that can't fail"; "voice-only tested
  with bots" ×3; A23).
- Fix: also build the reverse seat: a human patient with bot doctors that ask through a radial "what do you feel?" pick
  (with a timeout) and feed from that answer plus the outer signs. It's cheap, and it tests whether the inner signs can be
  read. Replace the kill lines:
  - In a 3-human night, if fewer than half the cures needed both an inner sign and an outer or tool sign, the split isn't
    working.
  - If a crew on its 3rd night loses nobody, it's too easy.

## Minor
**m1. Rules not written down (A19).**
- What "W 70% racing" means for the other 30%.
- Whether healthy players hear a heartbeat at all. If they don't, "none" is silent: Dee's line "my heart's not beating?"
  assumes they do.
- What stage 1 shows when no inner sign is drawn (about 15% of werewolf and zombie cases).
- Whether the journal is one book (a quarterback seat that also takes a hand) or one per player.
- What happens when a patient turns while held (do they catch the holder at once?) or while knocked out.
- Whether a creature that just turned human again can get the next case at once.
- Whether "shuffling walk" slows the patient's own controls, which would make it an inner sign.

**m2. The cone makes an alert, armed human impossible to catch from the front.**
- Why: a creature 1.2× faster circling at 2 m turns about 170°/s around you [assumed 5 m/s walk]. A mouse turns 500°/s or
  more. So catches land only on the unarmed or the inattentive: the threat hunts whoever lacks the item (critic ×1; checks
  4.5). The target "half of creatures catch someone" fails for a crew that stays together. A client lagging 150 ms will
  argue about the cone's edges (DRS #16).
- Fix: the creature gets a short lunge (1 s, once every 10 s), or the cone shoves it back instead of walling it off.
  U10 is unchanged.

**m3. In the first build, failure is expensive and quiet.**
- Why: with no ghosts, a death at minute 3 means 9 minutes of watching (DRS #2, #11; R.E.P.O.'s complaint in
  research.md). A lone survivor gets an incurable case within 360 s and waits for a certain death with nothing to do. The
  funny moment (your friend's body hunts you) costs the victim the whole night, which the funny-vs-difficult research files
  under "just difficult".
- Fix for the test build: the dead get a spectator view plus a slow push (the cheap ghost). The lone survivor may cure
  themselves (harder, since they see no outer signs, and it doesn't reward betrayal). Or shorten test nights to 8 min.

## Dominant strategy
The walking pharmacy, settled by night 2:
- In minute 1 the crew picks up a cure of every type (all the stock, or 2 per player if pickups respawn) and stays on
  voice.
- The patient announces their first inner sign the moment it plays. Racing, slow, none, meat, necks and anyone each name
  one creature.
- The nearest friend feeds that cure at stage 1 (90%). On "light hurts", or a craving that could be necks or anyone, they
  feed garlic, then salt, then wolfsbane, 2 s each, and a feed that does nothing rules that type out.
- Whoever's hand emptied walks to the respawn. Nobody holds or pans (no need), nobody opens the journal after night 1,
  outer signs and tools go unused (cases end before stage 2), and scars don't matter (they only hide outer signs).
- A turn is rare. Its type is obvious by then, the armed players face it, the unarmed one stands behind them, and it starves.
- Then 120 s of wandering (60 s at 6) until the next sick friend.

Deaths for a learned crew: close to 0 a night (hand math: about 75% of cases cured by the first feed, nearly all by stage
2). The plan card holds (checks 4.1, 4.5, 4.6 ✗).

## Scenes played by the critic (night 5)
- **3 players.**
  - 0:00–1:00: the crew grabs the cures. Bo pans Cy for a laugh, and Cy pans him back 20 s later (a fine comeback).
  - 1:00: Cy says "racing!". Ana feeds wolfsbane: cured by 1:06, and no fur ever shows.
  - 1:06–3:06: nothing happens. Ana walks to the respawn.
  - 3:06: Ana is a zombie with the "none" heartbeat and feels nothing (m1). At stage 2 Bo sees her grey skin and shuffle and
    feeds salt (60%): it fails. Cy runs to the garden while Bo holds Ana. Cured near the end of stage 2. This was the night's
    only real case, and it was an accident of the unclear baseline.
  - 5:30: Bo: "my view keeps going to Cy... his neck?" Garlic does nothing, salt cures. 4 s.
  - Over the night: 5 cases, 0 turns, about 2 minutes with a case running. The kill line passes.
- **6 players, minute 6.**
  - Dee: "light hurts". Garlic does nothing, salt cures.
  - Eli, fetching in the garden, says "racing heart" on Discord, walks back, and is cured at stage 1.
  - Four players stand and watch. Fae pans Hal as a joke.
  - If Eli is AFK out there, he turns alone, runs in, meets armed faces and starves. That death has a fair culprit.
  - 60 s of nothing until the next case.

## Co-op gate
1. Coupled: ✓. You can't cure yourself, and the patient's report is needed.
2. Split: ~. The inner/outer split exists, but the inner sign alone names about 73% of cases, and the mirror gives the patient their outer signs.
3. Talk: ✓. The patient must say what they feel (on Discord from anywhere, so distance adds nothing).
4. Blame: ~. A death has a face (the turned friend, the unarmed victim), but a misread or a wrong item shows nothing, and failures are mostly a hidden 60% or 30% roll.
5. Not easy: ✗. New crews can lose; a crew that has learned the tags loses about 0; nothing rises over the night.
6. Not solo-able: ~. At 3, one doctor who knows the tags and holds 2 cures handles every case; the rest are spare.
7. Two-way: ~. The patient talks but decides nothing (M2).
- Lone survivor: no soft-lock, but a certain death with nothing to do (m3). Dying on purpose: no gain. Lying about inner
  signs: no gain (you turn and die about half the time). It appeals only to a griefer who wants to be the creature, and the
  crew's comeback is the pan.

## Rule count
Taught: 3 rules, 7 clauses:
- you can't see your own signs;
- only you feel the inner ones;
- tell each other;
- the right cure saves;
- the journal maps signs to creatures;
- sooner is stronger;
- a turned friend must catch someone or die, and its cure held up keeps it back.

To play decently a player must also discover about 12 things:
- how long a stage is, and when "sooner" stops paying;
- how to read a 27-cell % journal;
- what each inner sign feels like compared with normal;
- a cure needs the patient still, takes 2 s, and is used up;
- you can't cure yourself;
- a wrong item and a failed roll look the same (and at stage 1 a feed that does nothing rules that type out);
- holding or knocking out slows the case (can't be discovered: M4);
- a knocked-out patient goes silent;
- 20 s before the same friend can be knocked out again;
- push the cure into the creature's face to break a catch;
- the cone covers only your front;
- scars mean nothing;
- a lone survivor's case is fatal.

The 3 taught rules are honest as text to teach, but by the user's check (one sentence + ≤ 2) the game is about 3 + 12.

## What is strong (keep)
- The inner / outer / tool split. "Bo, you've got fur" against "my heart's not beating?" is the right two-sided shape;
  only its numbers are wrong.
- Knocking out costs something: the patient goes silent and can't be panned again for 20 s, the PEAK lesson that a pause
  needs a cost and a limit. Holding takes both hands, so the holder can't use a tool at the same time (Ana's scene).
- Instant dawn is gone, and a lone survivor who turns has nobody to catch, so your friends' lives are your stake. Plus the
  first-build cut: 3 sign rows and one creature body.
