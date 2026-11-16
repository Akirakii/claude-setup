---
name: spawn-tab
description: Hand a task to a separate Claude Code session in a new kitty tab - use this instead of the Agent tool for any hand-off (CLAUDE.md rule 25). Use whenever the user asks to do work "in a separate agent", "in an agent", "on a sub agent", "in a sub session", "in a separate session", "in a new tab", "in parallel", or hands off a build, an implementation in a worktree, or any long independent task. Load it before reading the project.
---

# Spawn a session in a new kitty tab

The user wants handed-off work in its own visible session, not only in subagents.
Tool: `~/.local/bin/claude-tab` (kitty remote control, set in `~/.config/kitty/kitty.conf`).

## Steps
1. **Write a brief** to the task's folder: `BRIEF_<topic>.md` (no project: the scratchpad).
   It holds the goal in the user's words, the project path, the files to read (absolute paths), the limits (no commits; the domain skill's rules for running things), and where the result goes: `REPORT_<topic>.md` in the same folder, short, with small tables (coworker style).
2. **Open the tab:** `claude-tab -t <short title> -f <brief path>`.
   Every session starts in `~/claude-code` (the user's call), so the brief names the project path.
   Focus stays on the user's tab.
   If it says remote control isn't on, tell the user kitty needs one restart.
3. **Follow up:** read the report when the user asks or the session goes idle (`ListAgents`, then `SendMessage` with `notify_when_idle`).
   Don't poll.
4. **Tell the user** in one line: the tab title, and the brief and report paths.
