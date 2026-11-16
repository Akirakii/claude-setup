---
name: refactor-domain-knowledge
description: Review and clean ~/.claude/domain-knowledge/ - merge duplicates, settle contradictions, remove stale facts, shrink oversized notes, move notes to the right level, promote what proved general, fix the indexes. Use whenever the user says "refactor domain knowledge", "tidy memory", "clean up notes", "memory is messy", "better memory management", "I don't like memory all around", or when update-domain-knowledge finds a note or folder too big. Load it before reading the files.
---

# Refactor the domain knowledge

`update-domain-knowledge` sets the levels: top, `projects/`, `projects/<project>/`, `projects/<project>/<task>/`, each with an `INDEX.md`, plus `shared/<subject>/` for long docs that more than one project uses.
Cleaning CLAUDE.md and the output style is the `update-harness` skill.

## Steps
1. **Pick the scope:** the whole tree, one project folder, or the one file `update-domain-knowledge` sends.
   Ask only if the request doesn't say.
2. **Read everything in scope,** then list what you find, each with `file:line`:
   - **Duplicate:** the same fact in two places, so keep the one at the higher level.
   - **Contradiction:** two entries disagree, so ask the user which wins; their words decide.
   - **Stale:** a path, flag, script, file or status that no longer holds, so check it (ls, grep), then fix or remove it.
     Say "checked" or "assumed" for each.
   - **Too big:** a note over ~10 KB, a folder over ~12 notes, so shorten or split it: keep each lesson, drop the story around it.
   - **Wrong level:** a note true for more than its level (move it up), or a general note that only one project uses (move it down).
   - **Ready to move up:** the same lesson in 2 or more tasks or projects, so merge it one level up; the same doc copied into 2 or more projects, so keep one in `shared/`.
   - **Index:** a file with no index row, a row with no file, or a row with no "read when".
   - **Old style:** quotes or dates in a Why, labels Claude made up, long sentences, so rewrite in plain words, one sentence per line.
   - **Ready to be a rule:** a lesson that came up 3 or more times, so hand it to `update-harness`.
3. **Show the list and the exact edits,** grouped by file.
   Apply them only after the user's OK.
   Copy a file to `~/.claude/backups/` before rewriting more than a few lines of it.
   Keep what the user's words meant, even when the quote itself goes.
4. **Report:** what changed, and each file's size before and after.
