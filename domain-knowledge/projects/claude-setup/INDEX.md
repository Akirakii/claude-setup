# Claude setup (`~/.claude`)

How the user's harness is structured, and the tasks that changed it.

| Folder | What it was | Read when |
|---|---|---|
| `domain-knowledge-structure/` | the move from flat notes to levels, and the three skills around it | changing where knowledge or rules live |
| `project-postmortem-skill/` | why the postmortem skill hides the outcome and uses fresh judges; the gap found on its first run | changing the postmortem skill, or running it on a new project |
| `fantasy-chain-skill/` | where the chain model came from, and who chose each part | changing the chain or the fantasy-chain skill |
| `super-design-skill/` | where the super-design skill came from | changing the super-design skill |
| `tidy-memory-2026-11-12/` | the big tidy proposal for the old memory; its question Q2 is still open | the Mustache Madness memory archive comes up |

## True for the whole setup
- Three places, three jobs (user): CLAUDE.md holds rules for any kind of work, the output style holds speech rules, skills hold the rules of one domain.
- Knowledge is in `~/.claude/domain-knowledge/`, built from the task up (user).
- In session transcripts, a message the user sends while Claude is working is stored as a `queue-operation` entry with `operation: enqueue`, not as a user message; a script that reads transcripts has to count those as the user's words (checked).
