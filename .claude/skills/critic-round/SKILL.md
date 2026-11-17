---
name: critic-round
description: Judge whether a co-op game idea is fun with friends by comparing it to shipped games (the comparing critic), or run a design decision past an isolated critic that finds holes before anything is built (CLAUDE.md rule 20). Use when the user asks "is this idea fun", "would this be fun with friends", "run the critic on this idea", "compare it to the hits", or asks for a critic; and in AFK runs before each design decision (mechanic, rule, flow, item, symptom table, core loop), where the critic stands in for the user. Never while the user is designing in chat, unless they ask.
---

# Critic round

Two critics, for two different questions.
- **Is a co-op game idea fun with friends?** The comparing critic: one isolated judge reads the idea next to ten shipped co-op games whose audience is known and says yes, maybe or no.
  Its brief, the ladder and the game sheets are in the fun-with-friends folder listed in `~/.claude/domain-knowledge/shared/INDEX.md`; `~/.claude/domain-knowledge/critic-baseline.md` says how it was checked and how far to trust it.
  It judges fun only: popularity moves with time and trends, and novelty is reported on its own line.
- **Does a design decision hold?** (a mechanic, a rule, a flow, numbers) The hole-finding critic, in the steps below.
  It finds concrete holes; its fail is not a verdict on fun, since it fails shipped hits too.

Whether the fantasy, its feelings and its choices fit together is checked by Claude itself, not by either critic (the `fantasy-chain` skill).

## The comparing critic: steps
1. **Write the idea as a sheet** with the same headings as the shipped games' sheets (the template is in that folder), in the task's folder.
   Rules one sentence each; lines Claude guessed are marked as guesses.
2. **Run one isolated general-purpose subagent** with the brief from that folder, the sheet's path and an output path in the task's folder.
   Several ideas go to one judge in one run, each judged on its own.
   Tell it the author knows the seven traits, and ask for the plan a crew settles into and which feelings survive it.
3. **Read the verdict:** yes, maybe or no, the two shipped games it sits between, the holes, and what it couldn't break.
4. **Go back from each hole** to the rule that caused it and rewrite the sheet (the `fantasy-chain` skill, going back); at most 3 rounds, earlier versions kept.
5. **A "yes" is a yes on paper.** The pass gate is the user playing a small build.

## The hole-finding critic: steps
1. **Read first:** `~/.claude/domain-knowledge/design-anti-patterns.md`, `~/.claude/domain-knowledge/critic-anti-patterns.md`, `~/.claude/domain-knowledge/critic-baseline.md`, the project's `CLAUDE.md`, its design doc, the researched docs on the subject (listed in `~/.claude/domain-knowledge/shared/INDEX.md`), and the user's pillars and verdicts (tagged "(user)").
2. **Write the proposal** in the task's folder (e.g. `<topic>-thesis.md`):
   - the user's words that started it, quoted;
   - the problem underneath, in 2–4 lines;
   - at least 3 really different answers, one recommended, with real numbers (ranges, formulas), never "more" or "some";
   - one scene with the fewest players (the user's test: 1 human + bots) and one with the most;
   - each pillar it keeps, bends or drops.
3. **Run the critic:** an isolated general-purpose subagent.
   Its brief:
   - check the problem underneath before the numbers, and say first if it's wrong;
   - check item by item against the files in step 1;
   - play both scenes second by second, and work numbers out with a script instead of guessing;
   - name the strategy that always wins, and pass or fail each point of the co-op check (design-anti-patterns C);
   - list pillars dropped or bent without saying so;
   - for a co-op game, mark each finding "a shipped hit has this too" (from the baseline note) or "only this design"; a finding a hit has too is listed and never severe by itself;
   - a breach of the user's limits stays a finding whatever the hits do;
   - write short output to `critic-<topic>-r<N>.md` in the same folder: a verdict on the problem underneath, then findings marked severe / medium / minor (problem, example, fix direction), then what it couldn't break.
4. **Merge:** a table under the proposal, with each finding and the decision on it.
   Fix each finding or bring it to the user; never set aside a severe problem with the base idea.
   Rerun the critic until no severe finding is left, at most 3 rounds; only a finding of this design alone or a breached limit can be severe.
   A paper verdict is for holes, not the pass gate: the pass gate is the user playing a small build.
5. **Log** what the critic caught in `~/.claude/domain-knowledge/critic-anti-patterns.md` (pattern · this case · fix).
   A repeat goes into its old entry with a count (×N).
6. **Show the user** the sketch: short, a small table, and open choices in the project's `questions.md`.
   Build only after their answer.
