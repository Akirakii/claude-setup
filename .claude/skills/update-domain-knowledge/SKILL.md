---
name: update-domain-knowledge
description: Write what was learned into ~/.claude/domain-knowledge/ at the right level (task, project, every project, everything), and move the general part of a note up one level. Use whenever the user says "file it", "file this session", "save what we learned", a scoped task starts ("new task", a brief, a hand-off) or ends, a finding, decision or lesson should outlive the session, the user says "save this to the domain knowledge", "promote this", "where does this note go", or update-harness hands over a domain fact. Load it before writing any note.
---

# Notes start in the task and move up as they prove general

Knowledge is built from the bottom: most notes are only true for one task, a few hold for the project, fewer for every project.
The general levels are read and written the most, so they stay small and current.

## The levels (`~/.claude/domain-knowledge/`)
| Level | Folder | Holds what is true for |
|---|---|---|
| top | `*.md` | everything, or a whole domain (`game-idea-triad.md`, `machine-setup.md`) |
| every project | `projects/*.md` | the projects as a group (the project list) |
| one project | `projects/<project>/*.md` | all of that project |
| one task | `projects/<project>/<task>/*.md` | that task only |
| shared | `shared/<subject>/*.md` | more than one project, as a long doc (researched patterns, market reports) |

Every folder has an `INDEX.md`: one row per note or subfolder, with "what it holds" and "read when".
Only the top index loads by itself; the others are read on the way down (CLAUDE.md rule 27).
A project's design docs live here too (user): theses, critic rounds, research, briefs, reports and hand-offs go in the task folder they belong to, and a doc the whole project uses (the design, the open questions) sits at the project level.
The repo keeps only its `CLAUDE.md` and the docs about running the code (build notes, credits).
The domain knowledge is the only source of truth (user): when a repo's own skills or tools still need the docs at their old paths, the repo keeps an old copy, and every edit is made here.

**Where a skill's output goes (user):** other skills say only "the task's folder" or "the project's folder"; this skill is the one place that holds the real paths.
A skill that must read shared docs points at `shared/INDEX.md`, never at a single doc, so a doc can be renamed without touching a skill.

**A higher level never points down to a lower one (user),** the way a general module never imports a specific one.
A shared doc or a top-level note names no project, and a project-level doc names no task; where something came from is written at the lower level, pointing up.
The one exception is an `INDEX.md`, whose job is to list what is below it. (Claude)

## Two ways in
| Kind of work | When the task folders are made |
|---|---|
| Scoped up front: a brief, a hand-off, a research report | at the start (step 1) |
| Prototyping, with changes intertwined | afterwards, when the user says "file it" (next section) |

Claude can't tell when a thread settles or a session ends, so filing never waits for that: it runs when the user says so.
No hooks (user).

## Filing a session ("file it")
1. **Find what isn't filed:** read the date in `~/.claude/domain-knowledge/last-filed.txt`, then take the current session plus every session on the project since that date (`~/.claude/history.jsonl`, transcripts in `~/.claude/projects/`).
   Forgetting to file loses nothing; the next run catches up.
2. **Find the pull requests inside the work (user):** split what was done into pieces that each have one purpose and one output, the way the work would be split into good pull requests after the fact.
   Work that served two pieces goes with the one it mainly served, and the other gets a one-line pointer.
   Talk that produced no output and no lesson is not a piece.
3. **Show the split** as one small table (piece, its output, the folder name), then write after the user's OK.
4. **Write each piece** as a task folder (steps 2–3 below: notes, then promote), and add its row to the project's index.
5. **Write today's date** into `last-filed.txt`.

## Steps for a scoped task
1. **Starting a task:** read the indexes on the path, top down, then make `projects/<project>/<task>/` (a short name in the user's words) with a `notes.md`, and add a row to the project's index.
   Make the project folder and its index if they don't exist.
   A quick question or a small mechanical change is not a task; write nothing.
   **A task is scoped like a good pull request (user):** one purpose, one output (a report, a build, a decision, a skill), and a title that can be written before the work starts.
   The test is "what will exist when this is done?"; when that answer changes, a new task has started.
   Follow-up questions about the same output stay in its folder.
   A side branch with its own output gets its own folder, and the first folder keeps a one-line pointer to it.
   If it would be split into two pull requests, it is two tasks.
2. **While working:** put findings, decisions and dead ends in the task's notes, one sentence per line.
   Tag calls "(user)" or "(Claude)", checked or "(assumed)"; give the source for anything researched.
   Long outputs (reports, research) stay where the task put them; the note points to them.
3. **Ending a task, promote:** for each note, ask "would this still be true in another task of this project?", then "in another project?", then "outside this domain?".
   Move the part that passes up one level at a time, into the note that already covers it, else a new note with an index row.
   Move it, don't copy it: one home per fact, and the lower note keeps a one-line pointer.
   Write the promoted part as the general rule, with the case as one short example.
   A whole doc that more than one project uses (a pattern doc, a market report) moves to `shared/<subject>/` instead, with a row in `shared/INDEX.md`; when several promoted docs share a subject, they get their own folder there (user).
   A project never keeps its own copy of a shared doc.
4. **A fact that belongs higher from the start** (the user's model of games, a machine path) goes straight to its level.
5. **Not knowledge:** a rule for how Claude works goes to `update-harness`.
6. **Keep it findable:** every new file gets an index row with "read when"; a note over ~10 KB or a folder over ~12 notes goes to `refactor-domain-knowledge`.
7. **Report in one line:** what was written or moved, and where.
