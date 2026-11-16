# REAPER + BBC Symphony Orchestra on Fedora/Hyprland — session notes

Session dates: 2026-09-30 to 2026-10-02.
Goal: run REAPER on Fedora 43 (Hyprland) and use Spitfire's free
BBC Symphony Orchestra Discover library in it.

## System

| Item | Value |
|---|---|
| OS | Fedora 43, kernel 7.1.10, x86_64 |
| Desktop | Hyprland, monitor DP-3 3840x2160 at scale 1.5, `xwayland { force_zero_scaling = true }` |
| GPU | NVIDIA GTX 1070 (proprietary driver 580) |
| Audio | PipeWire (Fedora default) |
| Close keybinds | `Super+W` = killactive, `Super+Shift+W` = forcekillactive |

## What is installed, and where

| Thing | Location | Notes |
|---|---|---|
| REAPER 7.81 (evaluation licence) | `~/.local/opt/REAPER/` | Installed from the official tarball with `install-reaper.sh` |
| REAPER launcher | `~/.local/bin/reaper` | Puts patched Wine first on `PATH`, sets `GDK_SCALE=2` |
| REAPER menu entry | `~/.local/share/applications/cockos-reaper.desktop` | `Exec` points at the launcher, so rofi/wofi use it too |
| System Wine | `/usr/bin/wine` (wine-staging 11.0, Fedora package) | Not used for audio. `wine-dxvk` was removed |
| Patched Wine | `/opt/wine-d2d1/` (wine-11.0) | Built from `giang17/wine`, branch `d2d1-dcomp-11.0`. Source in `~/src/wine-d2d1` |
| Wine prefix for Spitfire | `~/.wine-spitfire` | Fresh prefix, no DXVK. The old `~/.wine` is unused leftovers |
| Spitfire Audio app 3.4.18 | `~/.wine-spitfire/drive_c/Program Files/Spitfire Audio/` | |
| BBC SO Discover plugin | `~/.wine-spitfire/drive_c/Program Files/Common Files/VST3/BBC Symphony Orchestra (64 Bit).vst3` | |
| BBC SO Discover samples (230 MB) | `~/.wine-spitfire/drive_c/users/akiraki/Spitfire/Spitfire Audio - BBC Symphony Orchestra/` | |
| yabridge | `~/.local/share/yabridge/` | Built from branch `new-wine10-embedding` (commit `ba7022d`). Source in `~/src/yabridge` |
| yabridge 5.1.1 backup | `~/.local/share/yabridge-5.1.1-backup/` | The original release build; `yabridgectl` still comes from it |
| Bridged plugin | `~/.vst3/yabridge/BBC Symphony Orchestra (64 Bit).vst3` | Created by `yabridgectl sync` |
| REAPER extensions | `~/.config/REAPER/UserPlugins/` | ReaPack 1.2.6, SWS 2.14.0.7, js_ReaScriptAPI |
| Reaticulate 0.5.13 | `~/.config/REAPER/Scripts/Reaticulate/` | Installed through ReaPack, repository `https://reaticulate.com/index.xml` |
| Custom Reaticulate bank | `~/.config/REAPER/Data/Reaticulate.reabank` | Two banks for BBC SO Discover (see below) |
| Reapertips theme v1.95 | `~/.config/REAPER/ColorThemes/` | Main theme plus 5 variations. Fonts in `~/.local/share/fonts/reapertips/` |

## The main problem and how it was solved

The Spitfire Audio app (needed to download and authorise BBC SO Discover)
showed a blank window under Wine.

Cause: the app is built with JUCE 8.0.8, which draws through Direct2D 1.3 and
DirectComposition. Stock Wine and DXVK do not implement these. The tell-tale
log line is:

```
err:   DxgiFactory::CreateSwapChainForComposition: Not implemented
```

Things that did not help:

- `WINEDLLOVERRIDES="dxgi,d3d11,d3d10core=b"` — on Fedora, `wine-dxvk` replaces
  Wine's builtin DLLs through `alternatives`, so "builtin" still meant DXVK.
- Removing `wine-dxvk` (`sudo dnf remove wine-dxvk`) — DXVK gone, window still blank.
- Wine virtual desktop (`wine explorer /desktop=...`) — only showed the blue background.
- `WINE_D3D_CONFIG="renderer=vulkan"` — no change.
- Per-app Windows 7 mode — no change.
- `WINEDLLOVERRIDES="d2d1=d"` — the app needs `d2d1.dll` and refuses to start.

What fixed it: a patched Wine, `giang17/wine` branch `d2d1-dcomp-11.0`, which
adds the missing Direct2D and DirectComposition support.

- A ready-made Fedora package exists (COPR `patrickl/wine-staging-dev`), but it
  is built only for Fedora 44. On Fedora 43 it had to be built from source.
- `sudo dnf builddep wine` failed on an `ocl-icd-devel` / `OpenCL-ICD-Loader`
  conflict, so the build packages were installed by name without the OpenCL one.
- The patch author's rules: use a fresh prefix, do not install DXVK into it,
  and set `HideWineVersion=Y` for JUCE 8 programs.

Build commands used:

```bash
git clone --branch d2d1-dcomp-11.0 --depth 1 https://github.com/giang17/wine.git ~/src/wine-d2d1
cd ~/src/wine-d2d1
./configure --prefix=/opt/wine-d2d1 --enable-archs=i386,x86_64
make -j$(nproc)
sudo make install
```

Prefix settings applied in `~/.wine-spitfire`:

| Registry key | Value | Why |
|---|---|---|
| `HKCU\Software\Wine\AppDefaults\Spitfire Audio.exe` → `HideWineVersion` | `Y` | Lets the JUCE 8 app use the Direct2D path |
| `HKCU\Software\Wine\AppDefaults\yabridge-host.exe` → `HideWineVersion` | `Y` | Same, for the plugin inside REAPER |
| `HKCU\Software\Wine\AppDefaults\yabridge-host-32.exe` → `HideWineVersion` | `Y` | Same, 32-bit host |
| `HKCU\Control Panel\Desktop` → `LogPixels` | `192` | Plugin window at 2x size (144 = 1.5x, 96 = 1x) |

## Second problem: mouse cursor offset in the plugin window

yabridge 5.1.1 has a known click-offset problem with Wine 10 and newer. The
fix is the `new-wine10-embedding` branch of yabridge, built against the
patched Wine:

```bash
export PATH=/opt/wine-d2d1/bin:$PATH
git clone --branch new-wine10-embedding --depth 1 https://github.com/robbert-vdh/yabridge.git ~/src/yabridge
cd ~/src/yabridge
meson setup build --buildtype=release --cross-file=cross-wine.conf --unity=on --unity-size=1000
ninja -C build
cp -f build/libyabridge-*.so build/yabridge-host.exe build/yabridge-host.exe.so ~/.local/share/yabridge/
yabridgectl sync
```

The new build is installed (files dated 2026-10-01 23:06). Whether the cursor
now lands correctly has not been confirmed yet.

To go back to yabridge 5.1.1:

```bash
rm -rf ~/.local/share/yabridge
mv ~/.local/share/yabridge-5.1.1-backup ~/.local/share/yabridge
~/.local/share/yabridge/yabridgectl sync
```

## Everyday commands

Start REAPER (always through the launcher, or the BBC plugin window is blank):

```bash
reaper
```

Start the Spitfire Audio app (for updates or more libraries):

```bash
WINEPREFIX=~/.wine-spitfire /opt/wine-d2d1/bin/wine "$HOME/.wine-spitfire/drive_c/Program Files/Spitfire Audio/Spitfire Audio.exe"
```

Re-sync plugins after installing a new one:

```bash
export PATH="/opt/wine-d2d1/bin:$HOME/.local/share/yabridge:$PATH"
yabridgectl sync
yabridgectl status
```

Kill a frozen REAPER and its Wine processes:

```bash
pkill -9 -f REAPER/reaper; pkill -9 -f yabridge-host; /opt/wine-d2d1/bin/wineserver -k
```

## REAPER basics covered

- Open the Actions list with `?`. Reaticulate opens with the action `Reaticulate_Main`.
- New MIDI item: drag a time selection on the track, then Insert → New MIDI item.
  Double-click the item to open the piano roll.
- Virtual MIDI keyboard: View → Virtual MIDI keyboard (`Alt+B`).
- Record with `Ctrl+R`, play and stop with `Space`.
- Themes: Options → Themes → Reapertips Theme.
- In BBC SO, the mod wheel (CC1) controls dynamics.

## Reaticulate and articulations

Reaticulate's factory banks have no BBC Symphony Orchestra bank, so a custom
file was written with two banks under the group `Spitfire/BBC SO Discover`:

| Bank | Articulations (program number) |
|---|---|
| Strings (`Bank 70 1`) | Long (1), Spiccato (42), Pizzicato (56), Tremolo (11) |
| Brass and Woodwinds (`Bank 70 2`) | Long (1), Staccatissimo (40) |

Unverified: the keyswitch notes. The plugin's preset files are encrypted, so
the bank assumes keyswitches start at the plugin's lowest C and go up one key
per articulation. Each articulation sends the note in two octaves (MIDI 12+
and MIDI 0+) to cover both octave-naming conventions. If switching does not
work, read the keyswitch notes from the BBC plugin's articulation list and
correct the `o=note:` values in the bank file.

How it works: clicking an articulation writes a program-change marker on the
track; Reaticulate's JSFX (placed before the BBC plugin) turns it into the
keyswitch. Markers apply from their position until the next marker. Two
articulations cannot sound at the same time on one track.

Alternative discussed: one track per articulation, with no Reaticulate. This
is simpler for a small library like Discover and was the suggested starting
point. Reaticulate pays off with larger libraries or lines that change style
often.

## Open items

- Confirm the cursor offset is fixed with the new yabridge build.
- Confirm the Reaticulate keyswitch notes actually switch articulations.
- The Reapertips theme is installed; `reaper.ini` still listed the default
  theme when last checked, so it may not have been selected yet.
- The `solopasha/hyprland` COPR returns 404 for Fedora 43 and no longer gets
  updates. Fedora's own repositories also carry Hyprland.
- The font setup script reported `DejaVuSans.ttf` missing. If plugin text looks
  wrong: `sudo dnf install -y dejavu-sans-fonts google-noto-sans-symbols-2-fonts`,
  then `bash ~/src/wine-d2d1/scripts/wine-font-setup.sh --prefix ~/.wine-spitfire`.
- Fedora 43 reaches end of life around the end of 2026. After upgrading to
  Fedora 44, the COPR `patrickl/wine-staging-dev` can replace the hand-built
  Wine and yabridge. Rebuild or replace both after any upgrade.
- The patched Wine and yabridge do not update on their own; rebuild from
  `~/src/wine-d2d1` and `~/src/yabridge` to update.
- `wine-dxvk` was removed from the system. Reinstall with
  `sudo dnf install wine-dxvk` if needed for games (keep it out of `~/.wine-spitfire`).

## Fallback options considered

- Linux-native orchestra: Virtual Playing Orchestra (SFZ) in the `sfizz`
  plugin, with Dragonfly Hall Reverb. Free, no Wine, less polished sound.
- Dual-boot Windows for orchestral work; REAPER projects move between systems.
- Install on Windows and copy the files into Wine — not needed in the end.

## Sources

- giang17/wine: https://github.com/giang17/wine
- Patch notes: https://github.com/giang17/wine/blob/d2d1-dcomp-11.0/PATCHES.md
- mklnln/wine-d2d1-dcomp: https://github.com/mklnln/wine-d2d1-dcomp
- yabridge issue 386 (JUCE 8 black screen): https://github.com/robbert-vdh/yabridge/issues/386
- JUCE forum thread: https://forum.juce.com/t/juce8-direct2d-wine-yabridge/64298
- COPR patrickl/wine-staging-dev: https://copr.fedorainfracloud.org/coprs/patrickl/wine-staging-dev/
- Reaticulate: https://reaticulate.com/
- Virtual Playing Orchestra: https://virtualplaying.com/virtual-playing-orchestra/
