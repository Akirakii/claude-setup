# Domain-knowledge structure (2026-11-16)

What changed and who chose it.

- Flat `~/.claude/notes/` became `~/.claude/domain-knowledge/` with levels: top, `projects/`, `projects/<project>/`, `projects/<project>/<task>/` (user's tree).
- A new task is a new folder; the general part of a note moves up one level at a time (user).
- `projects/` holds every project, not only games, so notes true for every game are files at the top level (user).
- An `INDEX.md` in every folder, read top down on the way into a project (Claude).
- A project's design docs stay in its repo; the folder here holds task notes and lessons (Claude, the user didn't object).
- `projects/claude-setup/` treats the setup as a project, to give the tidy proposal a home (Claude).
- Skills: `remember` became `update-harness` (CLAUDE.md, output style, hands skills to `write-skill`); new `update-domain-knowledge`; `tidy-memory` became `refactor-domain-knowledge` (user's names, except `update-harness`, which Claude proposed and the user accepted).
- CLAUDE.md's game rules 14–19 moved to the new `game-dev` skill; rule 20 (critic in AFK runs) stayed, since it is about any design decision (Claude).
- New CLAUDE.md rules 27 (use this structure) and 28 (domain rules live in skills).
- Old paths were fixed in the skills, the output style and five project CLAUDE.md files; older briefs and critic files in the repos still name `~/.claude/notes/` (left as history).
- Backup of the setup before the change: `~/.claude/backups/pre-domain-knowledge-2026-11-16.tar.gz`.
- Why it was needed: a note that wasn't on the path went unread, and advice the user had turned down was offered again.
- A task is scoped like a good pull request: one purpose, one output (user).
- Prototyping can't be scoped up front, so the tasks are found afterwards: the user says "file it", and the skill splits the session into the pull requests it contains (user).
- Dropped on the way: a running log per project (it copies the transcript), and filing by hook at the start of the next session (the user wants no hooks). (Claude's ideas, turned down)
- Claude can't tell when a thread settles or a session ends, so nothing depends on that (user).
- The split is shown before writing (Claude).

## 2026-11-16: project docs moved in, and a shared folder
- The user chose one place: a project's design docs now live in `projects/<project>/`, in task folders, and the repo keeps only the docs about running its code (user). Keeping them in the repo had been Claude's call.
- Reason (Claude, the user agreed): the games get dropped within days and the design thinking is what carries over; the split had already left stale copies in the `moonsick-hands` worktree.
- Moved: Moonsick, Deathly Reality Show, Pet the Cat, Red Button Experiment, Hordeline, Assemblia, Dungeon Pets. Each repo has `docs/MOVED.md` with the old path of every doc, and a note at the top of its `CLAUDE.md`.
- `shared/<subject>/` holds long docs that more than one project uses (user's idea): `game-patterns/` (the pattern docs three repos each carried a copy of) and `game-market/`.
- Copied, originals left in place (user asked for copies; their skills were not touched): Mustache Madness, `game-design-research`, Carpenter, qv, harness-doctor, mom-trip, claude-code-reaper, and the postmortem-methods report from `~/claude-code`. The domain knowledge is the source of truth for these too, and the repo's docs are the stale copy (user corrected Claude, who had written it the other way round).
- A higher level never points down to a lower one, like programming (user); the indexes are the exception (Claude). The global CLAUDE.md stays generic (user): the game names were taken out of its Whys.
- Not swept yet: older top-level notes that name projects (`game-idea-triad.md`, `game-scope-lessons.md`, the top `INDEX.md` line about the Mustache Madness memory archive).
- Not done: the repos' moved files are uncommitted deletions; the domain knowledge is not under git, so the moved docs have no history from here on (the old history stays in each repo).
- Backup of everything before the move: `~/.claude/backups/project-docs-2026-11-16.tar.gz`.
- Promotions done with the `update-domain-knowledge` skill (2026-11-16): the general sections of six Moonsick research docs went up to `shared/game-patterns/` and `shared/game-market/`, the Meshy steps, costs and lessons to `shared/meshy/`, the engine traps to `shared/godot/`, the finished market and verbs reports to `shared/`, and Dungeon Pets' postmortem causes to `postmortem-rows.md`. Each lower doc keeps a pointer up and its own project-specific part.
- Not promoted: the `Reasoning invariants` and `Model cognition and collaboration` parts of Mustache Madness's `MEMORY.md` look like rules for how Claude works, which is `update-harness` work and needs the user's OK first (Claude).
- `shared/godot/godot-traps.md` was moved by section and not cleaned line by line, so it still carries that game's file and class names as examples (checked: no doc paths in it).
- The pointing rule became CLAUDE.md rule 29 (user, 2026-11-16): every file points only at something as general or more general; CLAUDE.md names no skill and no note; skills are the controllers and the knowledge is the service; a note never names a skill; an index is the exception. The skill and note names were taken out of CLAUDE.md the same day.
- Still breaking rule 29 (not fixed yet): notes that name skills or link sideways with "Related" lines, top-level notes that name projects, and the idea-search skill pointing at one project's idea pool.
- Reading and writing split (user agreed, 2026-11-16): a skill names what it must read, pointing at the shared index and never at a single shared doc; for writing it says only "the task's folder", and the knowledge skill alone holds the real paths. CLAUDE.md names only the root of the domain knowledge (user).
- Moved for that: the idea pool and its history to the shared game-ideas folder, and the postmortem methods research into the postmortem skill's own folder as `research.md`.
