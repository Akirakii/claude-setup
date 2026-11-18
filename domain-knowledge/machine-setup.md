# machine-setup

Paths, scripts and flags behind ~/.claude/CLAUDE.md (game launches, AFK keep-awake, diagrams, Meshy, RunPod) on the user's Fedora + Hyprland machine.

The rules themselves are in `~/.claude/CLAUDE.md`.
Related: `projects/projects.md`.

**Games Claude opens**
- `tools/ai_run.sh [godot flags] -- [game args]` exists in `~/Playground/moonsick` (and `moonsick-hands`), `deathly-reality-show` and `red-button-experiment` (checked).
  It opens a 640x360 floating window, bottom-left, without focus (`noinitialfocus`), and muted (`--audio-driver Dummy`).
- Pass `--quit-after=S`.
  When hosting, pass `--port=24699`, since the user's own game may hold 24680.
  Keep benchmarks to ~6 s per config.
- **Mouse lock:** `noinitialfocus` doesn't stop a game from locking the pointer; Moonsick once grabbed the user's mouse when the night started.
  Moonsick's ai_run.sh adds `--no-capture`, and the game skips the capture with it.
  In any other project, add the same flag before a windowed run, or run headless.
- Godot's `--position` is ignored on Hyprland.
  Never add global `hyprctl keyword windowrule`s: they would change the user's own launches.
- Hyprland's exec doesn't have `~/.local/bin` on PATH.
- Projects without ai_run.sh: add `--audio-driver Dummy` yourself (Hordeline also has `--mute`).

**AFK keep-awake**
- The normal `~/.config/hypr/hypridle.conf` locks at 5 min, turns the screen off at 5.5 min, and runs `systemctl poweroff` at 60 idle minutes with `ignore_inhibit = true`, so `systemd-inhibit` can't stop it.
- Current method: `~/.local/bin/claude-keepawake.sh` restarts hypridle every 45 min.
  It stops when Claude's newest session log under `~/.claude/projects` is 30 min old (running out of usage makes Claude go silent, so this covers it). It no longer needs a status line; the old version is in `~/.claude/backups/`.
  Relaunch it with setsid if `pgrep -f claude-keepawake` finds nothing.
- Older method, kept on disk: `~/.config/hypr/hypridle-afk.conf` (no poweroff).
- On a locked screen, windowed Godot draws ~1 fps; `--headless --fixed-fps 60` runs normally.
- Progress file: `docs/TODO_*.md` or `HANDOFF_*.md` in the project, in case the PC shuts down.
  Turn every single thing the user asked for into a task row.

**Diagrams (the user called the first way ugly and this way nice, 2026-11-19):** write one SVG from a small Python script and render it with Chrome: `google-chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=W,H --screenshot=out.png file://in.svg`, then show it in qimgv (below).
`magick` renders SVG text badly (no real fonts, no text anchors); no d2, graphviz or mermaid is installed (checked).
How it's drawn:
- Only the mechanism goes in the picture: boxes, arrows and a few words each. Lists and explanations stay in the note or the reply.
- Every box comes from one grid computed in the script: same size, same gaps, text centered with `text-anchor`.
- Font Inter; a title, one muted line under it, then the picture.
- Near-white page, white boxes with thin grey borders, soft tinted bands for groups, dark ink only for the arrows the picture is about.
- Every arrow has a short label; arrowheads are SVG markers.
- Look at the PNG before showing it.
- Don't `pkill -f` a pattern that also appears in the same shell command: it kills the shell (exit 144).

**Showing the user an image: always in qimgv (user, 2026-11-19),** never in the terminal: `setsid -f qimgv <file> >/dev/null 2>&1`.
Older ways, kept only in case qimgv is missing: the image-pane mod's `show_image` tool (source `~/.claude/dev-mods/f62bc6a8-8e60-424c-afba-528cabcffa7e/image-pane/`), or a kitty split: `kitty @ --to "$KITTY_LISTEN_ON" launch --type=window --location=vsplit --keep-focus --hold --title <name> kitten icat --align left <file>`.

**Meshy:** the API key is in `~/.config/meshy/api_key` (MCP launcher `~/.config/meshy/run-mcp.sh`); never print it.
Costs: image-to-3D 15 credits, rigging 5.
Prompts for past concepts are saved next to them (`art/concepts/*/*.prompt.md` in older projects).
To redo a concept, rebuild its prompt and change only what the user asked.
Auto-rigging glues shoulder-length hair to T-posed arms when the head is wider than the shoulders, and prompt fixes (no side hair, a ponytail) didn't solve it (Dungeon Pets Emberpup; `~/.claude/domain-knowledge/projects/dungeon-pets/research.md:819`).

**RunPod:** after an interrupted `create-pod`, run `list-pods` first, since it may have made a pod (two pods were once left running).
