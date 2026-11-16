# Moonsick: critic v2 (isolated, 2026-11-12)

Read: design.md (v2), design-anti-patterns, critic-anti-patterns, Full Moon critic-r4 and r5. Nothing played. The
numbers were [computed] in python from the doc's table and formulas. Walking speed, grab range and how long a cure
takes to reach the patient are [assumed] where marked.

**Frame:** the light/dark sign table makes fantasy, logic and look line up well. You step a friend into a moonbeam to
read grey skin and back into the dark for eyeshine, and every second in the beam costs case time. Betraying never pays
more than curing, for the patient, the curer, a bystander or the creature: each death makes everyone left sick more
often, and a second catch gains nothing. Trust matters until dawn, because the next creature chooses its own victim.

**Came back from earlier rounds:**
- the fortress (r5 M4), now the moonlit garden;
- the clock tell (r3), now the trick's fixed length;
- the defence with no counter (r2), now backing away;
- "silence assumed online", now through the dead.

**Nights played:**
- **4 friends.**
  - Each takes a cure and a tool (8 hands, 12 items), and they wait in a dark room next to a window beam.
  - Ana says "I crave meat". The crew waits 8 s, since 2 in 3 claims are the house. The spoon and the thermometer
    read in 3 s, and the cure goes in at ~80–85%.
  - The two tools alone give a 63–100% lean in 69% of cases [computed].
  - Turns come from a failed roll when the second dose is across the house: ~1–2 a night [assumed].
  - A werewolf turn (30 s hunger, 3 targets) is a real chase. A vampire or troll turn ends with everyone in the
    garden and the creature starving (S1).
  - The dead watch for 4–6 min and call out where the creature is on Discord (M5).
  - At 2 alive, curing still beats letting the other friend turn: alone, you could cure yourself on inner signs only.
- **8 friends.**
  - 16 hands, 12 items. Seven watchers see every outer sign at once, so "grab, read both tools, cure" in ~5 s becomes
    the routine. Kill line 1 trips at 8 long before it trips at 4.
  - Hunger is 21–36 s with 7 targets, so werewolf turns always catch someone. Vampire and troll turns still go to the
    garden.
  - A friend who pans someone as bait pays only in trust. The real payback is the next creature choosing them.

## Severe
1. **The moonlit garden beats the vampire and the troll (the r5 fortress is back).**
   - Why:
     - The whole garden is moonlight, and in moonlight both creatures move at people's speed.
     - At equal speed, a friend who walks away in the open is never caught up with. Hunger is 32/40 s at 6 alive and
       80/100 s at 2 alive [computed].
     - So "vampire or troll: everyone outside" answers 2 of the 3 creatures in one line. The troll's own counter
       ("stay in the dark", where it runs at 1.15×) is the worse play.
     - In most of those turns the creature player jogs after friends, starves, and spectates for the rest of the night.
       The turn-moment choices (whom to chase, who is bait) never happen.
     - This breaks the user's pillar "each creature has its own ways to deal with it".
   - Fix:
     - Cut "moonbeams slow the vampire and the troll". Keep moonlight as what the troll sees by, and keep the ×1.5
       case speed.
     - Then each creature has a different answer: the garden is a trap against the troll (it sees you at 25 m),
       neutral against the vampire, and the pond is the answer to the werewolf.
     - If a weakness is wanted, use a flinch: a 0.5 s stop on entering a beam, then 5 s before it can flinch again.

## Major
2. **One armed friend walking backward can't be caught.**
   - Why:
     - A shove throws the creature to ~5 m away. Getting back into grab range (~1 m) at 1.15–1.3× takes longer than
       the cure's 3 s wait whenever walking speed is under 4.4 m/s (werewolf), 6.7 m/s (vampire) or 8.9 m/s (troll)
       [computed; assumed: grab at 1 m, the friend backs straight away].
     - So "two armed players cover each other" only holds against a wall. A lone friend holding rowan or garlic in the
       open is safe.
   - Fix:
     - Holding up a cure slows you to half speed, so the friend holding it commits.
     - State a target: "a lone armed friend in the open is caught in about half of tries; a covered pair in under 20%".
3. **Tricks outnumber real inner signs about 3 to 1, and they end on a fixed ~8 s clock.**
   - Why:
     - One trick every 3 min per healthy friend, against a case every GAP + ~15–25 s, half of which start with an inner
       sign. That makes 67–70% of fresh "I feel…" claims the house at 4 players, 74–77% at 6 and 78–82% at 8, and more
       late in the night [computed].
     - So every claim gets "wait 8 s" (95% odds drop to 85%), which is r3's "spot the fake by the clock" again.
     - The patient's half of the information becomes noise. Kill line 3's question gets asked, then answered by a timer.
   - Fix:
     - Aim for about one trick per real case that starts with an inner sign: at 6 alive, ~1 per healthy friend every
       7 min.
     - Make the trick's length random (4–25 s, mostly short). Then the test is going to the sign's trigger or reading a
       tool, not the clock.
4. **The sign table's sentence and its numbers disagree, so the build can't tell how signs are drawn.**
   - Why:
     - The doc says the % is "how often each creature shows that sign in a case". Built that way:
       - a werewolf shows no outer sign in 36% of cases and no inner sign in 15%; a troll shows no inner sign in 30%;
       - the stage schedule has nothing to show at stages 2–3, and the watchers' half is missing (kill line 2);
       - one-sign leans are 50–64%.
     - The doc's own 51–55% and ~58% come out only if every case shows all four of its signs and the % only sets which
       comes first [computed both ways].
   - Fix:
     - Write the rule: "each case has its creature's two inner and two outer signs; within a kind, which comes first is
       weighted by the %; tool signs are present by their %."
     - Rename the column "chance it comes first".
     - Under that rule, drool alone gives 50/50 (no lean).
5. **The dead are free scouts on Discord.**
   - Why:
     - The spectator camera sits behind any living friend, the creature included, and sees round corners. A dead friend
       calls out "werewolf's in the hall, heading for the garden" ("silence assumed online", now ×4).
     - Whenever anyone is dead, the creature's senses stop mattering, and so do the counters built on them (stand
       still, stay calm, stay dark).
     - The dead have nothing else to do for ~4–9 min.
   - Fix (keeps the user's "no ghosts"):
     - The dead watch from a living friend's eye height with private screen effects off, never from the creature.
     - The creature's outline view never reaches them.
6. **v0.1 is not a 2-week build for one developer.**
   - Why:
     - As listed, v0.1 holds:
       - two network paths;
       - 8 areas with ramps;
       - moonbeam volumes that the rules check;
       - 6 face signs plus veins and scars;
       - 3 screen effects;
       - 3 senses, including named footprints;
       - the hunt, a journal and a timeline story;
       - bots in three roles: doctors that weigh the %, hunters that use the senses, and pathfinding over ramps.
     - The bots and the network alone fill the two weeks.
   - Fix (the first test is 3+ humans):
     - Cut for v0.1:
       - the bots (keep one dev-flag bot patient);
       - one of the two network paths: keep the Steam lobby or ENet, not both;
       - the study, the dining room and the conservatory;
       - scars;
       - doubles (a user pillar: say so, and bring it back in v0.2);
       - named footprints: the werewolf's sense becomes "anyone who moved in the last 3 s within 20 m";
       - the timeline, replaced by a plain text log.
     - Keep: signs, tools, cures, hold and pan, turning, catch, shove, hunger.

## Minor
7. **DOUBLE at 30% late bends the user's "two at once, but rarely".**
   - Why: at ~1 case a minute late in the night, that is a double every ~3 cases, 1–2 a night [assumed].
   - Fix: tell the user, or cap it at 15% or one a night.
8. **Grey skin is a colour sign in a world with no colour.**
   - Why: with a moonlit blue palette and no warm light, telling grey skin from normal skin at 2–5 m is the hardest
     read in the table, and it carries a whole row's outer sign.
   - Fix: give it a shape as well (stony cracks, matte instead of shiny), and keep healthy skin saturated in beams.
9. **Quick chat only carries inner signs.**
   - Why: watchers and tool holders have no lines for what they see, so without voice the talk runs one way, and a bot
     doctor can't tell a human patient anything.
   - Fix: add two keys: "look at X" (a ping on a friend) and "tool: yes / no".
10. **Two slips in the doc.**
    - "6 alive: every 3.7 min" leaves out the time a case lasts. It is ~5–6 min per person at 6 and ~4–5 at 4
      [computed].
    - "It never tests anything" (Terms) is still false (r4 m8). Given to a suspect, a cure shows nothing, a shudder or a
      burst: healthy or cured, right kind, wrong kind.
    - Fix: correct the text. The price of the test (one cure) is fine.

## Edge cases to specify:
- A knocked-out friend whose case ends: they turn and wake, and the knockout ends.
- A catch during the 10 s turn-back: it doesn't restart the 10 s. Shoves still work during it.
- A cure given to a creature: does nothing, or can't be given.
- A second case that reaches its end during the turn-back: it waits until the 10 s are over, then turns.
- Two cases that reach their end in the same tick (a wrong-cure jump): the first in order turns, the other waits.
- A wrong cure on a case already waiting at its end: no jump; it keeps waiting, curable at 30%.
- Who a new case or a DOUBLE can pick: skip anyone sick, the creature and the dead. Say whether a DOUBLE still starts if
  the first case is cured before its start time.
- With two cases, GAP counts from whichever case ended later.
- Hunger's "people left to catch": fixed at the turn; counts knocked-out and sick friends.
- Speed modifiers multiply (moonlight ×1.5, held ×0.5, knocked out ×⅓). Say whether the veins stop while a friend is
  held in moonlight.
- "People's speed": walking or sprinting? Is there stamina? Can creatures sprint?
- Does the creature see the world normally, or only the outlines?
- A friend in the 2 s turn: can't be cured, panned or held.
- Grabbing or panning a creature does nothing. Does the pan's noise still count?
- A knockout drops what you hold. Otherwise one friend who pockets both garlics can't be stopped, since held cures
  count toward the cap of 2.
- A cure dropped on the floor and left there: it wilts after ~60 s so its spot can regrow.
- Reading a tool on yourself: allowed or not? It matters for the last one alive.
- Giving a cure (2 s) gets interrupted when the target moves, or when the giver is grabbed, panned or caught.
- Shoves are blocked by walls; say what happens when a creature is shoved into a wall, and that only one shove fires
  when two holders are in range.
- Quick-chat bubbles: seen through walls? Do they count as noise for the creature?
- At dawn: a creature still out lives or dies at sunrise? A sick friend at dawn wins. Cases that can't end before dawn
  make the last ~minute safe: intended?
- The host as patient or creature: the host checks catch and shove distances with lag allowance, so the host's zero lag
  doesn't win chases. The host leaving ends the night.
- A friend who disconnects: counts as dead? What happens to their case and the cures they hold?
- Scars: one per friend (the latest), or do they stack?
- A trick running when its player gets sick ends at once.
- The story timeline shows no quick-chat lines or tool readings. Otherwise it becomes a record that exposes liars.
- The last one alive: does the 60 s skip still apply? Nobody is left to hold them or pan them, so nothing can slow
  their case.

Verdict: close but not ready to build. Cut the moonbeam slow (S1) and fix M2–M4 first. M6 is the cut list; the rest is
spec.
