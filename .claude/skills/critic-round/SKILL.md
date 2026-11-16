---
name: critic-round
description: Run a design decision past an isolated critic before anything is built - Claude writes a proposal, a critic agent attacks it, Claude merges the two (CLAUDE.md rule 20). The critic stands in for the user while they're away. Use only in AFK runs, before each design decision (mechanic, rule, flow, item, symptom table, core loop), or when the user asks for a critic. Never while the user is designing in chat.
---

# Critic round

## Steps
1. **Read first:** `~/.claude/domain-knowledge/design-anti-patterns.md`, `~/.claude/domain-knowledge/critic-anti-patterns.md`, the project's `CLAUDE.md`, its design doc, the researched docs on the subject (listed in `~/.claude/domain-knowledge/shared/INDEX.md`), and the user's pillars and verdicts (tagged "(user)").
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
   - write short output to `critic-<topic>-r<N>.md` in the same folder: a verdict on the problem underneath, then findings marked severe / medium / minor (problem, example, fix direction).
4. **Merge:** a table under the proposal, with each finding and the decision on it.
   Fix each finding or bring it to the user; never set aside a severe problem with the base idea.
   Rerun the critic until no severe finding is left, at most 3 rounds.
5. **Log** what the critic caught in `~/.claude/domain-knowledge/critic-anti-patterns.md` (pattern · this case · fix).
   A repeat goes into its old entry with a count (×N).
6. **Show the user** the sketch: short, a small table, and open choices in the project's `questions.md`.
   Build only after their answer.
