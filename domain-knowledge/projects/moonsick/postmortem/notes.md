# Postmortem of versions 1–4 (2026-11-16)

Output: `POSTMORTEM-2026-11-16.md` in this folder; rows in `~/.claude/domain-knowledge/postmortem-rows.md`.
Method: the `project-postmortem` skill; its research is in `~/claude-code/reports/Postmortem analysis methods.md`.

- Verdict: versions 1–3 had cooperation and no reason to lie; version 4 has a reason to lie and no cooperation.
- The postmortem's first lesson ("play the core with real people, in the cheapest form, before any build") was rejected by the user: a stripped test cuts the aesthetic and the fantasy, so the friend judges a different game.
- The lesson kept (Claude, the user didn't object): the logic was known to be broken from free checks (critic numbers, the user's head-simulation) before each build, and we built on it anyway.
- Moved up: the turned-down advice went to `game-idea-triad.md`; the chain (logic and aesthetic cause actions, actions cause feelings, feelings sell the fantasy) became the `fantasy-chain` skill.

## Open (user)
What can really be learned from the postmortem, given the user's feedback?
- A stripped test with people is off the table: it cuts the aesthetic and the fantasy.
- Friends are 14 hours away, so a test with four people is rare.
- The user already did the head-simulation and the small prototypes on earlier games, and those still failed.
- The polish (aesthetic, movement, feel) was how the user got to judge the logic, not waste (user, 2026-11-16); the rule is in `game-idea-triad.md`, Limits.
- Claude's proposed lesson, no verdict yet: free checks (critic numbers, head-simulation) can prove a core broken but not fun, so use them as a gate before a build.
- Read first: `~/.claude/domain-knowledge/game-idea-triad.md` (the advice already turned down) and the `fantasy-chain` skill.

## Where the lessons talk stopped (2026-11-16)
- Claude's second pick, no verdict yet: keep one ready base (movement, characters, feel) and swap only the logic on top, so each new core reaches the point where the user can judge it in a day. It follows from the user's correction that the polish is how they judge the logic, and from the redo, which kept the movement and was judged within a day (checked: `redo-race/redo-ideas.md`).
- Open, asked and not answered: is a critic's number enough for the user to call the logic broken, or does only their own play count? The critic said "give on the first sign wins every time" on Nov 12 (`core-step1/critic-core-r1.md`, S1), two days before the user saw the same flaw by playing. Claude's pick: the number is enough to stop a build.
- Third session (2026-11-16), written into section 8 of the postmortem: 13 of 14 critic rounds on the first foundation's rules found a new best move, the first two (Nov 11) described the counter the user found by playing on Nov 14, and on Nov 12 Claude answered the user's "should i start the game from scratch?" with "No" (all checked).
- Claude's third pick, no verdict yet: a best move that comes back after its fix is the user's "too many loops" signal; keep one list of best moves per foundation and recommend dropping when a fix fails twice. It replaces "the critic's number is enough to stop a build": one finding isn't, a finding that returns is.
- Said to the user as the limit: this only shortens the time on a failing foundation; Moonsick can't teach how to find a fun one.
- Found while filing the other projects: Dungeon Pets failed on the same two things, a core choice with one answer and bots that couldn't measure the fun (rows in the postmortem rows note at the top level). That is 2 of 2 projects with a postmortem, so not yet a pattern by the skill's own bar of 3.
- The comparison across all eight games (asked next by the user) is in the postmortem rows note at the top level, with its own section.
