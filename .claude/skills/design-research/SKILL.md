---
name: design-research
description: Research patterns and anti-patterns on the web - how others solve a problem, what makes it good or bad - and design from them, ignoring the current source code. Use whenever the user says "research" ("research patterns", "research how X is done", "antipatterns"), asks "what makes X good or bad", "find references from other games", "how is X usually done", "best pattern for X", "design X from scratch", or to write or update a patterns / anti-patterns doc. Not for a brief or a quick brainstorm that never asks for research.
---

# Design from patterns, not from the code

Existing code pulls a design toward what's already there.
This skill looks at how others solve the problem well, then fits the best answer to the user's limits.

Rule: never read, grep or name the project's source code.
Limits come only from the user's words; if one is missing, ask the user instead of checking the code.

1. **Say the problem in general terms.** One sentence with no project nouns: what goes in, what comes out, what must hold.
   Search terms come from this sentence, not from the project.
   Keep the scope the user set earlier in the chat, and check each result against it before showing it.
2. **Read what is already researched.** Open `~/.claude/domain-knowledge/shared/INDEX.md` and read every doc on this problem before any search.
   Search only for what those docs don't answer, and say which doc already covered the rest.
   Why: the same subject was researched from zero while its patterns were already written down.
3. **Search wide.** Run several web searches at once: the general problem, its known patterns, known failures ("X pitfalls", "X postmortem"), and other fields with the same problem.
   Prefer primary sources, cite each claim, and mark anything from memory.
4. **List 3 or more patterns.** For each: what it is, where it's used (cited), what it's good at, how it fails.
5. **Fit to the limits.** A table of pattern × limit with ✅/❌, naming the limit each pattern breaks.
6. **Recommend one.** The pick and why, plus what the runner-up does better.
   Recommend the pattern the way the sources do it; any detail I add on top is tagged "(Claude)" and kept apart.
   Why: a guessed detail once slipped in with a cited pattern and read as if the sources did it.
   The user picks; nothing gets built here.
7. **Save it** in the task's folder; the part that holds for more than one project goes up to the shared docs (the `update-domain-knowledge` skill).

Reply: the recommendation first, then the table and the sources.
