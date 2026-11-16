# projects

Where each of the user's projects lives (~/Playground) and its status; Moonsick is the active game (Nov 2026).

Claude is started in `~/claude-code` for every project, so a project's `CLAUDE.md` doesn't load: read it first.
Status comes from each project's docs and last commit (checked 2026-11-12).

| Project (`~/Playground/…`) | What | Status |
|---|---|---|
| `moonsick` (+ worktree `moonsick-hands`, branch `hands`) | the user's Full Moon idea: online co-op with betrayal for 4–8, one dark night (~12 min, deaths are final), diagnose friends turning into a werewolf, vampire or troll; GitHub Akirakii/moonsick (private) | **active.** Four versions in five days (v0.1, cut-down, bluff core, the race); current design in `moonsick/redo-race/redo-ideas.md`, postmortem in `moonsick/postmortem/`; open question: the race is PvP. Notes: `moonsick/INDEX.md`. Design history: `game-design-research/research_notes/Full Moon/` |
| `deathly-reality-show` | co-op friendslop for 3–6 players, a deadly TV game show hosted by the Reaper | **active**; its CLAUDE.md and `deathly-reality-show/` here are the source of truth |
| `pet-the-cat` | co-op friendslop, keep a huge cat calm | dropped (the user didn't like it) |
| `red-button-experiment` | co-op friendslop, press one red button | dropped before Pet the Cat; reference only |
| `hordeline` | co-op train defense with Vampire Survivors-style upgrades | dropped: good ideas were hard to find on a Vampire Survivors base; reference |
| `assemblia` | robot army auto battler | abandoned; 4 untested `exp/*` branches kept |
| `dungeon-pets` (+ `-base`, `-js-prototype`) | first-person creature-pack roguelike | failed; see `dungeon-pets/postmortem/` |
| `mustache-madness` | Godot game, performance work in Oct 2026 | core dropped in late Oct 2026 after ~6 months of loops (see [[game-idea-triad]]) |
| `game-design-research` (once `rival-radar`, then `competition-research`) | market and game design research | research only; rank on measured Steam/YouTube signals |
| `music-claude` | composition self-study (carpenter course `duo-form`) | see [[music-setup]] |

Each project's design docs, task notes and lessons live in this folder, one subfolder per project (moved out of the repos on 2026-11-16); a repo keeps its `CLAUDE.md` and the docs about running the code.
For Mustache Madness, `game-design-research` and the non-game projects an old copy of the docs is still in the repo, so their own skills and tools find their paths; this folder is the source of truth for those too (user).
Lessons for picking the next game: [[game-scope-lessons]].
