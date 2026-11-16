# music-setup

The user's Linux music tools (MuseScore + Muse Sounds chosen; REAPER + BBC SO installed, pipeline dropped) and findings that aren't obvious.

The user writes and plays music in MuseScore with Muse Sounds.
The scripted MuseScore-to-REAPER-to-BBC SO render pipeline was built, compared, and dropped at the user's request (files deleted).
They plan to come back to REAPER later, for piano-roll editing alongside MuseScore.

**Why:** Muse Sounds follows written dynamics and slurs by itself and plays inside the editor; the BBC route needed dynamics and articulations wired by hand.

**When:** default to MuseScore for anything about scores or playback, and don't rebuild the REAPER pipeline unless asked.
Use the facts below instead of finding them again.

- The official MuseScore 4.7.5 AppImage is in `~/.local/opt/musescore`, with the launcher `~/.local/bin/musescore`; it's the default app for score files.
  Fedora's `mscore` (4.6.0) is still installed but hidden: it can't start the Muse Sounds engine and can't open 4.7 files.
- MuseScore runs under XWayland.
  Hyprland has `force_zero_scaling = true` (a 4K monitor at 1.5x), so the launcher sets `QT_SCALE_FACTOR=1.5` to fix the tiny UI.
- Muse Sounds Manager (no-sudo tarball, no auto-update) is in `~/.local/opt/muse-sounds-manager`.
  Muse Strings is installed in `~/Muse Sounds` (it has solo violin, viola and cello).
- Command-line render with Muse Sounds: `QT_QPA_PLATFORM=offscreen musescore --sound-profile MuseSounds -o out.flac in.mscz` (the value is `MuseSounds`, no space).
- Headless conversion: `QT_QPA_PLATFORM=offscreen musescore -o out.musicxml in.mscz` (MusicXML to .mscz works too).
  `/usr/bin/mscore` silently exits with 40 and converts nothing (checked).
- REAPER: `~/.local/bin/reaper` (a wrapper using a patched Wine).
  BBC SO Discover lives in `~/.wine-spitfire`, bridged by yabridge and scanned by REAPER.
  `reaper -renderproject x.rpp` renders without interaction but needs the desktop session.
- BBC SO has no preset list a script can use, but its saved state is XML naming patches (e.g. `b - Violins 1 - Long`).
  Swapping the names for another Discover string section, and setting `rr_neighbourMin` to that instrument's lowest MIDI note, switches the instrument.
  Keep the byte length the same by padding with spaces.
- MuseScore's Linux build hosts no VST plugins, so BBC SO can't play inside MuseScore.
- The user's carpenter course `duo-form` (a two-voice sarabande in C# minor) lives in `~/Playground/music-claude/courses`, and scratch scores in `~/Playground/music-claude/render` (the old `~/claude-code/playground/` is empty, checked).
  Its exercises are written in MuseScore and graded from the saved `.mscz`, never as Python tasks (authoring rules: `~/Playground/music-claude/CLAUDE.md`).
