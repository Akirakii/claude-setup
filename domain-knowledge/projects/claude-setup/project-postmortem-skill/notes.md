# The project-postmortem skill (2026-11-16)

Output: `~/.claude/skills/project-postmortem/` (SKILL.md, categories.md) and the research report `~/claude-code/reports/Postmortem analysis methods.md` (notes in `~/claude-code/research_notes/Postmortem analysis methods/`).
First run: Moonsick (`../../moonsick/postmortem/`).

- Why the steps hide the outcome: knowing the ending makes every mistake look obvious, and warnings don't fix that. [source: the report, hindsight and outcome bias]
- Each key decision is judged by a fresh agent that reads the transcript only up to that decision (Claude, from the research); Claude took part in the sessions, so it doesn't judge them.
- Rival explanations are written before reading further, each with what must show up if it's true. [source: the report, process tracing]
- A last agent checks the whole with speakers relabelled A/B; on Moonsick it caught that Claude had left its own part out of the causes (checked).
- Categories for comparing projects come from Politowski's 20 problem types. [source: the report]
- Gap found on the first run (checked): all five judges recommended a test with real people, without knowing the user's limits, and the user rejected that lesson. Fixed: each judge now gets the user's known limits from the domain knowledge. (Claude, user's OK)
- For a game, the step on what went wrong now follows each playtest reaction backward with the `fantasy-chain` skill. (user's OK)
- Moved up: how to read mid-turn messages in transcripts, to this project's index.
