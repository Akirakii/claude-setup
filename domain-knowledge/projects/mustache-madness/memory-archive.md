# Memory archive (mustache-madness)

Moved 2026-11-12 from Claude's hidden per-project memory (`~/.claude/projects/-home-akiraki-Playground-mustache-madness/memory/`) at the user's request: project knowledge lives in this repo's docs. Cross-project rules from these notes were merged into `~/.claude/RULES.md` on 2026-11-09, so some entries repeat it; prune with the tidy-memory skill. Backup: `~/.claude/backups/auto-memory-2026-11-12.tar.gz`.

## afk-pc-poweroff-hypridle
_hypridle powers the PC off after 1 h idle; AFK runs use a no-poweroff config, kept until the user is back_

The user's normal `~/.config/hypr/hypridle.conf` has a 3600 s `systemctl poweroff` listener with `ignore_inhibit = true`, so a `systemd-inhibit` lock cannot stop it. `~/.config/hypr/hypridle-afk.conf` keeps lock and screen-off but has no poweroff (user, 2026-10-25: "dont turn off machine" in AFK, as a rule; the earlier 3 h poweroff killed a relay while it waited out a usage limit). Backup of the old 3 h version: `hypridle-afk.conf.bak`.

**Why:** a power-off mid AFK run kills the relay and wipes `/tmp`.

**How to apply:** at AFK start, `pkill -x hypridle; setsid -f hypridle -c ~/.config/hypr/hypridle-afk.conf`. Keep it on through the whole run, even after the relay ends or at the usage limit; restore the normal config (`pkill -x hypridle; setsid -f hypridle`) only when the user says the AFK run is over (a check-in or question is not that). A reboot resets to the normal config: re-check with `pgrep -a hypridle` after any wait. See [[afk-progress-on-disk]], [[afk-screen-locked-no-rendered-runs]].

Tidied 2026-11-12: the other two entries (afk-progress-on-disk, afk-screen-locked-no-rendered-runs) were deleted, already in `~/.claude/CLAUDE.md` rules 11 and 16 and `~/.claude/notes/machine-setup.md`. The entry above stays until the user answers tidy question Q2 (AFK power-off, `~/.claude/notes/tidy-proposal-2026-11-12.md`).
