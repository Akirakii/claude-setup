# This repo is a copy of the user's `~/.claude` setup

It exists so a Claude Code session on the web has the same rules, skills and notes as the user's PC.

Where things are here:

| On the PC | In this repo |
|---|---|
| `~/.claude/CLAUDE.md` | `CLAUDE.md` |
| `~/.claude/domain-knowledge/` | `domain-knowledge/` (a session-start hook links `~/.claude/domain-knowledge` to it) |
| `~/.claude/skills/` | `.claude/skills/` |
| `~/.claude/output-styles/` | `.claude/output-styles/` |

Edit the files in this repo, never a copy under `~/.claude`.
Commit and push every change to the rules, skills or notes, so the user can pull it back to the PC.
This repo is public: never write a key, a token, an address or a travel date into it.

Not available in a web session: kitty tabs and splits, Hyprland, Godot, the game repos in `~/Playground`, Meshy, the keep-awake script.
Rules and skills that need them (new kitty tab for hand-offs, running a game, AFK keep-awake) don't apply here; say so instead of trying.
Design work on paper needs none of them.

Two folders were left out because they are personal: `projects/mom-trip/` and `projects/qv/`.

Last hand-off: `domain-knowledge/projects/game-design-research/critic-calibration-2026-11-18/HANDOFF_critic-calibration.md` (start with the summary at its top).
