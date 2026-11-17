# Domain knowledge index (loaded every session through ~/.claude/CLAUDE.md)

Claude's knowledge in visible files the user owns; it replaces Claude Code's hidden auto memory, which is off.
Notes start in a task folder and the part that proves general moves up one level (CLAUDE.md rule 27).
Only this index loads by itself: read a note when its "read when" applies, and read the lower indexes on the way into a project.
Write with the `update-domain-knowledge` skill, clean with `refactor-domain-knowledge`.
`last-filed.txt` holds the date sessions were last filed ("file it").

## Levels
| Level | Where | Index |
|---|---|---|
| top: true for everything, or for a whole domain | this folder | this file |
| every project | `projects/` | `projects/INDEX.md` |
| one project | `projects/<project>/` | its `INDEX.md` |
| one task | `projects/<project>/<task>/` | listed in the project's index |
| shared: long docs promoted out of projects | `shared/<subject>/` | `shared/INDEX.md` |

## Domain skills (load first when work enters the domain, CLAUDE.md rule 28)
| Domain | Skill | Work that enters it |
|---|---|---|
| games | `game-dev` | a game repo, running or building a game, a mechanic or rule sketch, Meshy, a playtest |

## Notes at the top level
| Note | Domain | What it holds | Read when |
|---|---|---|---|
| `machine-setup.md` | everything | paths, scripts and flags: ai_run.sh, AFK keep-awake, diagrams, showing images (kitty split), Meshy, RunPod | running a game, an AFK job, Meshy, RunPod, or drawing a diagram |
| `explain-concepts-plainly.md` | everything | plain words and a real example, no analogies, the user's own words, no made-up labels | the user asks what something means or asks to hear it again ("what does X mean", "could you elaborate", "I didn't understand", "explain again", "how does X work") |
| `chat-style.md` | everything | research behind the `coworker` output style | changing how replies are written |
| `visual-teaching-weakness.md` | everything | Claude's drawn teaching pictures aren't readable; copy airline-card/IKEA formats and let a human glance at it | making any picture, board or icon meant to teach |
| `game-idea-triad.md` | games | the user's model: fantasy, logic, aesthetic, aligned; their creativity block; advice they turned down | discussing game ideas or how to find them; before giving lessons or a process for making games |
| `game-scope-lessons.md` | games | ship in under a year, ~3–4 months of scope, prove the fun in days; co-op chosen | scoping a game or a feature |
| `design-anti-patterns.md` | games | the design failures that repeated across projects, and the co-op check | before showing any game-design sketch (the `game-dev` skill) |
| `critic-anti-patterns.md` | games | what critic agents keep catching in Claude's design proposals | before writing a design proposal; after each critic merge (add or count) |
| `critic-baseline.md` | games | what the critics for co-op ideas are measured against: shipped games as the examples of fun, the seven things the judge looks for, how it was checked, and the problems a hit has too | before a critic round on a game idea, or when reading a critic's verdict |
| `idea-search-loop.md` | games | the user's directions for the idea search (the method is the `generate-ideas` skill) | running the idea search |
| `postmortem-rows.md` | games | one tagged row per problem or success from each game, and the comparison across the eight games (three sets of rules, eight themes) | running a postmortem, comparing why projects failed, or starting a new game from a dropped one |
| `music-setup.md` | music | MuseScore + Muse Sounds chosen; REAPER/BBC installed, pipeline dropped | music work |

The old per-project memory archives were folded into each repo's docs and CLAUDE.md, then deleted.
Only `mustache-madness/docs/memory-archive.md` remains, with one entry waiting on question Q2 of `projects/claude-setup/tidy-memory-2026-11-12/proposal.md`.
A full copy of the old hidden memory: `~/.claude/backups/auto-memory-2026-11-12.tar.gz`.
