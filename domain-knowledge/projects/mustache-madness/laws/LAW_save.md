# LAW: the save system

Standing law for game saves. User decisions are tagged (user); the rest were picked by the AFK
relay on 2026-10-14 from the recommended options and stay open to the user's veto.

## Purpose (user)
Autosave the whole game state at every wave start, so any wave of a playtest can be loaded
and replayed headless to reproduce what happened there (lag above all).

## Frame
1. **A save holds only source-of-truth state.** Anything the game rebuilds from that state
   (navmesh, rooms, housing, target lists, grid index, ledge links) is not saved; it
   rebuilds through the one path it already uses.
2. **Loading runs the normal spawn path.** Every entity is created by its
   `SpawnCoordinator` spawn function from a plain dictionary, then its saved fields are
   applied. No second construction path exists.
3. **Transient state is dropped:** paths in flight, knockback, gatherings in flight, hit
   memory, anything timed in wall msec or in absolute physics frames (native `CrowdBody`
   step fields start at 0, as on any mid-game spawn).
4. **A reproduction is statistical, not frame-exact.** The game is not deterministic, so a
   wave is run several times from its save and judged by frame-time median and p99.

## Field marking (one generic saver)
1. Every script whose state is saved declares each of its vars in exactly one of three
   lists: `SAVED` (written and restored), `DERIVED` (rebuilt after load), `TRANSIENT`
   (dropped). One generic saver reads and writes the `SAVED` lists; no script writes its
   own `save()` / `load()`. A subclass lists only its own vars, under its prefix
   (`CROP_SAVED`, `CROP_DERIVED`, `CROP_TRANSIENT`: GDScript forbids redeclaring a parent's
   constant); the saver joins the lists of the whole script chain, base first.
2. A test finds every script that declares a marking list and fails on any of its script
   vars in none of the lists or in two, and on a listed name that is no property. A new
   field cannot be forgotten silently.
3. A saved value is a plain Variant: numbers, strings, vectors, arrays, dictionaries. A
   resource is saved as its `res://` path. An object or node reference is saved as a save id
   (below), never as an engine instance id. An object the save owns (a marked component, a
   pre-rolled wave) nests as a record whose `_script` key names its class, so a null var or
   an array of them rebuilds on load.
4. A SAVED field that holds engine instance ids of entities (an array of them, or a
   dictionary keyed by them: `parents`, the social maps) is also listed in `INSTANCE_IDS`.
   The saver writes those ids as save ids and the link step turns them back; the test fails
   on an `INSTANCE_IDS` name that is not `SAVED`.
5. State with no plain form is saved through a property whose getter and setter convert it
   (`GameRng.state`, `Blueprints.unlocked_ids`); applying a value always runs the setter.

## Save ids and references
1. Every saved entity gets a save id: an int minted by the game from one counter at spawn.
   The counter's next value is saved, so ids stay unique after a load. The id rides in the
   spawn data (a load passes the saved one), so it is final before `_ready`.
2. Every cross reference (social maps, `parents`, bed owner, carried body) is written as save ids and resolved after all entities exist, through
   one id map built during the load. A reference whose target is gone is dropped. A
   field holding an entity (a node with a `save_id`) is always such a reference, never a
   nested record.
3. A reference the game rebuilds by its own rule is derived, not saved: the job board's
   worker-to-site map and the job hat (the board re-hands them on its first poll),
   `close_ids` (the housing scan).

## Load order
1. Start the level from the saved world seed, skipping the start set
   (`game.gd` `_place_start_set`), the tree and crop scatter, and the `IntroPhase` herd.
2. Restore the globals. `LevelManager.load_level` resets `Grid`, `TargetManager`, `Jobs`,
   `NavigationCoordinator` and reseeds `GameRng`, but not `GameTime` or `Blueprints`
   (they set themselves only in their autoload `_ready`), so the loader sets every
   global it restores explicitly: `GameTime` (`total_time`, `current_day`), `Blueprints`
   (`_unlocked` ids, `_built`), `DayCycle`, `WaveSystem` (wave number, difficulty, forecast
   queue, generator history), `GameRng` state, `MatchConfig` difficulty, terrain size.
3. Spawn structures, crops, dropped items, stations and eggs, then creatures, each with its
   save id.
4. Link references through the id map.
5. Set what spawning advanced: `GameRng` state (spawns roll names and grumps) and the
   save id counter, last.
6. Let derived state rebuild. Spawn the statue (a station, not saved) and set `DayCycle`
   to DUSK: its next tick enters NIGHT through `phase_changed`, so every listener starts
   the wave as in play (the loaded session writes its own `wave_<N>` file there).

## Files
1. **Host only (for now).** Only the server writes saves. A remote player's items live on
   their client and are not in the host's save.
2. **Path:** `user://saves/<session>/wave_<N>.save`, written at every nightfall (N = the
   night number, siege or calm), by `WaveSystem` just before night N starts (no wave runs
   yet; `DayCycle` already reads NIGHT). `<session>` is the stamp of the level load. Every
   night's file of a session is
   kept. A headless sim writes under `user://sim_saves` instead, so its sessions never
   bury the player's.
3. **Format:** one dictionary written with `FileAccess.store_var` (objects off), read with
   `get_var`. It is written to `<path>.tmp` and renamed, so a crash never leaves a cut file.
   The night frame only captures: `store_var` and the rename run on a `WorkerThreadPool`
   task (`SaveGame.flush` waits for it; the level's exit flushes).
   A save that cannot be read starts no world: the menu shows why (a sim quits).
4. **Version stamp:** the dictionary carries `version` (int). A file with another version is
   refused with an error, not migrated; bump the version on any change to what is saved.
   It only goes up: a branch rebased onto a newer version bumps above it, never lower.
5. **Baseline:** each autosave also holds `baseline`, the host's wall-clock ms of every frame
   since the previous autosave (or the level load): the wave before it and the day after.
   A headless reproduction is checked against its median and p99. The loader ignores it.
