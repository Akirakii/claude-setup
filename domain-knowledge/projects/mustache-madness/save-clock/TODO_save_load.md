# TODO: save and load

Law: `docs/LAW_save.md`. Load a wave headless:
`SIM_LOAD=user://saves/<session>/wave_<N>.save flatpak run org.godotengine.Godot --headless --fixed-fps 60 --path . -s res://util/debug/headless_sim.gd`
(`SIM_RESULT` carries `frame_ms_median`, `frame_ms_p95`, `frame_ms_p99`). Add `SIM_SECONDS=n`
to run on past the wave's dawn (`run_sims.sh` sets it: the feature table from a save). In
the game: the start menu's Load, or the `I` cheat (newest autosave).

## Next
- [ ] **Build stalls (the playtest's worst lag):** save a large built base, place pieces on
  the loaded save headless, time each suspect: navmesh rebake and its geometry parse
  (`world/procedural_terrain.gd`), ledge links (`world/components/auto_ledge_linker.gd`),
  placement check (`entities/items/components/placed_behavior.gd`). The 12 worst ticks of the
  2026-10-13 playtest (4 to 9 s) all carried `[BUILD]` lines, 10 a rebake.
- [ ] **Autosave hitch:** 86 to 98 ms on the main thread per wave (2,250 grid objects, ~90
  creatures). Time `capture` vs `store_var` + write; move the write to a `WorkerThreadPool`
  task. Target under 16 ms on the main thread.

## Later slices (each with its round-trip test)
- [ ] Inventory and ground items (`weapon`, `feed`; player items are client-side).
- [ ] Machines: grid objects get save ids, so `jail_cell`, `_jail_until`, `sleep_bed`, `rest`,
  `offer_place`, `breed.bed`, `Jobs` sites, the woodpile `holder` and `job.axe` can be saved
  (today a jailed creature loads free). GridObject subclasses without lists are not scanned
  by the forgotten-field test yet.
- [ ] Light wilds (`Herd._lights`) are not saved.
- [ ] Sessions written by sims before sims got `user://sim_saves` still sit in
  `user://saves` among the player's (the menu lists the newest 12 that hold a wave).

## Known, not this feature
- A load fires `grid_object_placed` per restored piece: the balance probe counts them as placed.
