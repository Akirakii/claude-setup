---
name: afk-run
description: Run a long task while the user is away (AFK, asleep, or "for N hours") - keep the PC awake, keep a progress file, work headless, hand off clearly. Use whenever the user says "afk", "ill be afk", "ill go to sleep", "good luck!", "while I'm away", "for 2 hours straight", "work for N hours", "I'll be back", "avoid pc turning off", or leaves a build running unsupervised, even if they never say AFK. Not for a rule about how AFK runs should work (that is remember).
---

# AFK run

The rules behind this are in `~/.claude/CLAUDE.md` rule 11 (progress file, PC stays on) and, for games, in the `game-dev` skill (game runs, AFK builds, Meshy).
Paths are in `~/.claude/domain-knowledge/machine-setup.md`.

## Start
1. **Keep the PC awake.**
   If `pgrep -f claude-keepawake` finds nothing, start `~/.local/bin/claude-keepawake.sh` with `setsid`.
   The PC powers off after 60 idle minutes and ignores the usual blockers, so the script keeps restarting the idle timer.
2. **Make a progress file** in the task's folder: `HANDOFF_<topic>.md`.
   At the top, "Summary for the user (read this first)", empty for now.
   Then a table: each thing the user asked for (their words), its tasks, and their status.
   Then a log with real times.
3. **Plan the time** the user gave.
   Do the most important task first.
   Cut a task the moment it grows (rule 9).

## While working
- Update the progress file after every step: the task status and one log line with the time.
- Check games headless only (`--headless`).
  The screen locks and then draws about 1 frame a second, so there are no rendered performance numbers.
- Spend at most ~5% of the effort running the game; run the tests once, after the edits.
- Design decisions still go through the `critic-round` skill; tag Claude's own design calls "(Claude)".
- Meshy is allowed for hero art while AFK (the `game-dev` skill); log every generation and its credits.
- A message from the user mid-run goes into the task table, then carry on.

## Hand off
- Fill in the summary: what changed (in the user's words), how to try it (the exact key or launch config), what was checked and what wasn't, credits spent, and open choices (in the project's `questions.md`).
- Leave git alone unless the user asked for commits.
- Leave keep-awake running until the session ends.
- Final message: short, pointing to the handoff file.
