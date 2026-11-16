# idea-search-loop

The user's directions for the game idea search; the method itself is the `generate-ideas` skill.

Each direction is built into `~/.claude/skills/generate-ideas/` (SKILL.md, checks.md).
This note keeps the directions and where the search stands.

- **Check first that players act on each other.**
  Scorers were too easy on players working side by side on one object (Megalith Haul, log rollers); this is now checks.md sections 0–1.
- **Learn from failures with web research:** search to understand what's going wrong, and what real player-with-player interaction is.
- **An idea is fantasy + logic + aesthetic** (see [[game-idea-triad]]).
- **Small checks inline, no agents:** the user stopped 3 checker agents working on 14 fantasies.
  A short list gets checked in the main session; agents only for big rounds.
- **The skill works fantasy first, with no subagents:** a list of fantasies, why each one makes players interact, then the check against the formula.
- **A fantasy needs a force:** something that makes players need each other right now (the user couldn't see what forced vampires to feed on each other).
- **"Reach somewhere" means completing a level, which is medium to high content,** so goals are never places.
- **Show both lists,** passed and failed, and show each failed idea itself, not just its name.
- **The goal fits the fantasy,** and each idea also has a job.
- **The idea line:** [job] [struggle] [goal] worked much better, with physical actions instead of vague words ("fight it").
  Then it became [job] [choice] [goal]: the main choice a *player* makes in the game (Claude first misread it as variants for the user).
- **A living pool and a skill that improves itself:** keep improving the passing ideas, fixing the failing ones and adding more; keep learning how ideas work and how to improve the method; let the skill improve itself when it's working.

**Where it stands:** a 2-hour run (29 cycles) reached 32 passing ideas in 21 cores (the pool, in the shared game-ideas folder).
Each fantasy source gave 1–2 new cores, then only skins.
The user isn't thinking about testing yet: offer it, don't push.
The user says the pool feels like Mario Party minigames, not a full game; Claude's read is in research.md (the 2026-11-11 entry) and `Idea search/fix-minigame-feel.md`.
Next: sketch a between-rounds step for the skill before editing it (the skill has none yet, checked).
An AFK run on 2026-11-17 tried a different order (fantasy, feelings, research on shipped games, choices) with Claude writing the fantasies: nine ideas, four isolated critic rounds, none passed.
The pool's top-ranked core (Storm Sailors) was sent to an isolated critic for the first time in that run and failed on six severe findings, so the pool's ranking rests on Claude's own inline checks only.
What the critics found in common: a crew with one interest and the same facts has one answer, one end of each choice only obeyed, and a perfect crew's round was one where the idea didn't happen.

