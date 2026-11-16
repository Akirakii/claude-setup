---
name: simulate
description: Play a game design out as scenes, round after round, to find holes, check whether each hole is real and whether each fix works, and keep fixing until a call needs the user. Use whenever the user says "simulate", "play it out", "would that work", "find holes", "keep simulating", "are those holes real", "does the fix work", or asks to test a mechanic, rule or flow in Claude's head before building it.
---

# Play the design out before anyone builds it

A sketch reads fine on paper and breaks the moment a player does the selfish thing.
Claude once offered a lock without playing it, and the user found in their head that it was boring and that killing beat curing.
This skill plays every sketch out, round after round, and stops only when a call is the user's.

Rules: don't run the game (the `game-dev` skill); a quick script for numbers is fine.
Check each fix against `~/.claude/domain-knowledge/design-anti-patterns.md` (the `game-dev` skill).

## Each round
1. **Write the rules as they stand, from the design doc, not from memory:** the user's and Claude's apart, with the newest decisions first.
   Any rule a scene leans on (who can stop a catch, what a group does) is read in the doc or code, or marked "assumed".
   Why: a scene once leaned on "a group protects you", which the game doesn't do.
2. **Pick the crews:** fewest players, most players, and the user's test crew (1 human + bots).
3. **Play scenes:** each player does their best selfish move, and say what the best play turns into.
   A rule nobody uses, or a best play that's dull, is a hole.
4. **Judge:** each hole is real or not, and each fix works or fails, with no "mostly" (rule 23).
   If the design has lies, check every kind of lie against the bluff formula; if it has shared jobs, check each against the co-op check (both in `formulas.md`). A line that fails is a hole.
   A verdict that rests on rates or timings is "assumed" until a script checks it.
5. **Fix the failures** with a new fix, tagged "(Claude)", and play it in the next round.
   Search by backtracking, not only by adding: a round may take back a rule an earlier round added, or remove a rule just to see what the game does without it.
   Try removing before adding when a hole sits on a rule Claude added, and when the rule list keeps growing.
   A removed rule is logged with the round that removed it, and design.md drops it too.
   Never remove a user's rule; play the game without it as a scene, and bring it to the user if the game is better.
   Why: each round only stacked fixes on fixes, so the rules grew and never got simpler.
6. **Save the round** in the project's docs (the doc for that design), before the next round starts.

## When to stop and hand over
Stop and show the user when any of these comes up:
- a fix bends one of the user's pillars or an earlier user verdict;
- the question is about fun or taste ("is this boring?"), which only the user's head or playtest can answer;
- two fixes both work and the choice between them changes the game;
- a round finds no new hole and no failing fix, and removing each Claude-added rule was tried;
- 5 rounds have passed.

## Reply
The user has to see what the scenes stood on, so the reply has four parts, in this order:
1. **The rules it ran on:** a short list, split into built, OK'd but not built, and Claude's picks, with anything assumed marked.
2. **The formulas it checked:** name each one (bluff, co-op) and its lines in a few words.
3. **The scenes and gaps:** each scene in one or two plain lines, then one table: hole, real ✅/❌, fix works ✅/❌, and one line of why.
   When the bluff was played, add a table of each lie against the formula's lines.
4. **Rules to add:** each fix written as a rule the design doc could hold, tagged "(Claude)", with the call that needs the user in bold as Claude's pick.
