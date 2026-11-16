---
name: game-dev
description: The standing rules for game work - don't run the game to check, keep opened games silent, AFK game builds, Meshy approvals, check every design sketch against the anti-patterns, copy Godot reference repos. Use whenever work touches a game - a game repo in ~/Playground (Godot), "run the game", "build the game", a mechanic, rule, item or flow sketch, "meshy", a model or concept generation, or a playtest. Load it before reading the project.
---

# Game work: the rules that hold in every game project

These were CLAUDE.md's game rules; they moved here so CLAUDE.md stays free of any one domain.
Each came from something that went wrong.
Paths and scripts are in `~/.claude/domain-knowledge/machine-setup.md`.
The researched docs for games (patterns, the market, Meshy, Godot) are listed in `~/.claude/domain-knowledge/shared/INDEX.md`: read the ones its "read when" column names for the work at hand.

## Running and checking
- **Don't run the game to check your work** unless the user asks (in AFK runs, at most ~5% of the effort).
  No screenshot loops; one cheap shot is fine.
  Run the test suite once, after all edits.
  The user's playtest is the real check, so report changes as untested.
- **Games Claude opens stay silent and out of the way:** muted, small, bottom-left corner, never taking focus.
  Headless when no window is needed.

## AFK game builds
- The user expects a full, runnable game and gives design freedom.
- Tag Claude's own design calls "(Claude)" in the design doc.
- Check features against the researched pattern docs (listed in the shared index, never copied into the repo); keep a build/run doc in the repo and a todo of gaps in the project's folder.
- No rendered performance numbers (the screen locks); headless only.
- Meshy is allowed for hero art.
- The rest of an AFK run is the `afk-run` skill.

## Meshy while the user is here
- Before the first generation, read the Meshy pipeline doc (steps, costs, lessons) from the shared index.
- Before every generation, show the shared style prompt, the exact prompt and the diff from the last try, then wait for OK.
- Image-to-3D and rigging need an OK each time.
- Concepts are always new text-to-image, never edits of an existing image; an image the user names means "start from its saved prompt", never "feed it in".
- "Iterate until right" lifts none of this.
- Why: generations cost credits, and the user wants to see each change before it runs.

## Design sketches
- **Before showing any game-design sketch** (mechanic, rule, flow, item, path), or a list of what's designed so far, read `~/.claude/domain-knowledge/design-anti-patterns.md` and check it against it.
- In a list, every part Claude picked keeps its "(Claude)" tag, so the user sees what they never chose.
- Every sketch, even a one-line "I'd add X" in a quick back-and-forth, first gets one scene played in my head: each player's choice, and what the best play turns into.
  Drop the sketch if the best play is dull or skips the mechanic.
- In that scene, name for every role what it gains and what it costs to act, counting how the friends treat that player in the next round.
  A role that gains nothing won't act, and hurting a friend for no gain earns a grudge.
- A ❌ becomes a ✅ only after a new scene, never because the user pushed back on a different point.
- Before giving lessons or a process for making games, read `~/.claude/domain-knowledge/game-idea-triad.md`: it lists advice the user already turned down.
- Why: the same design failures repeated across projects; Claude listed its own symptom as if the user had chosen it; a lock offered without playing it turned out boring; turned-down advice was offered again.
  A werewolf with no reward for killing was passed, because the scene covered one round and never asked what the kill cost that player with their friends.
- Related skills: `fantasy-chain` (follow a rule to the feeling it causes), `simulate`, `super-design`, `critic-round`.

## Godot
- Reference repos live in `~/Playground/refs/` (index in its `README.md`, by category: movement, items, menus/UI, multiplayer, Steam lobby, juice, VFX, animation, audio, dialogue).
- Before building one of those features in a Godot game, read the matching repo and copy its pattern.
- Before touching navigation, multiplayer, tests, rendering, UI or input in Godot, read the Godot traps doc from the shared index.
