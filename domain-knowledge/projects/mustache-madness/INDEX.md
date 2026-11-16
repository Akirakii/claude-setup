# Mustache Madness

Godot game, about 6 months of work; core dropped in late October 2026. Repo `~/Playground/mustache-madness`.
**This folder is the source of truth** since 2026-11-16 (user); the docs left in the repo are an old copy, kept only so the repo's own skills and tools still find their paths.
Edit here, never there.
The repo's own skills (`.claude/skills/`) read and write `docs/` there and were not copied.

## At the project level
| Doc | What it holds | Read when |
|---|---|---|
| `MEMORY.md` | the pillars and invariants every idea was judged against | judging a design from this game |
| `GOTCHAS.md` | engine and tooling traps, by domain | hitting a Godot or tooling problem |
| `memory-archive.md` | the old hidden memory, one entry still waiting on a tidy question | that tidy question |
| `laws/` | the standing laws: beds, rooms, room types, save, life, creature state, time dilation, file layout, design anchors | how a system was meant to work |

## Tasks
| Folder | What it was | Read when |
|---|---|---|
| `economy-model/` | the creature economy: frame, payment model, bank, prices, heirs, food theft, job quality | any economy design |
| `gem-income/` | where the player's gems come from; gem ore and the mine | player income |
| `playtest-tuning-relay/` | the long AFK tuning relay and its design rounds (shops, flow, meals, university, build) | how a relay of rounds was run |
| `stages-unlocks/` | game stages 2 and 3, the unlock and challenge tree, design clusters c1–c6 | staged progression |
| `progression/` | guided progression, beasts, sieges, boat arrivals | progression and discoverability |
| `performance/` | the locality architecture, lag spikes, light wilds | performance with many creatures |
| `playtests/` | the 10-night AFK playtest and the 2026-10-09 follow-ups | playtest numbers |
| `mood-needs-creatures/` | mood, steam and snap; needs; the creature black box; the object catalogue; emergent roles; creature stats | creature behaviour design |
| `block-build-rooms/` | the block-build roadmap, room types, nav and creature size | building and navigation |
| `kitchen-crops/` | the job board and kitchen, crops and dishes | food systems |
| `mvp-v1/` | the MVP passes, the v1 release list, the guide system | scoping a release |
| `save-clock/` | save and load, the standing clock backlog | saves |
