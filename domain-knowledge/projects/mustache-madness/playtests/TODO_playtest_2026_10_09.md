# TODO: playtest 2026-10-09 follow-ups

Measured in the user's playtest (816 s, herd up to 50): 6 snaps, 50 recruits (revives), 2 eggs.
Standing law for rooms and drag building: `docs/LAW_rooms.md`.

## Done (this branch)
- [x] Hands stay "carrying" after the held creature perishes or is swallowed.
- [x] Crash in `get_next_point(null)`: a place's seat list is the truth.
- [x] Rampage lasts until jailed or knocked out; red HUD line names the rampager; 🤬 pops on each punch; the active sim bot jails.
- [x] Drag tools: Wall (an L, 5 blocks per cell), Platform (half-block rectangle), Stairs (rising). Whole-drag price.
- [x] Rooms: a built floor + 4 walls + roof, 10% open per side. Room-only: medic bed, nest, jail, games table, gym, treadmill, lab, kitchen, library (user confirmed). 🏚 over a switched-off piece.
- [x] Walls stop wilds; a wild punches the piece it bumps into (6 s), damage heals at dawn.
- [x] Starter hut around the start medic bed; `/hut` cheat; `/jail` puts its cell in a hut.
- [x] Planks (user): furniture costs logs; only building pieces cost planks (1 log = 4, paid automatically, leftovers kept, 4 picked up fold into a log). Trees and furniture keep their old values.
- [x] The axe breaks twice as fast (creature choppers too: they share the timer).
- [x] Stairs climb the way the player faced at the first click; the second click sets length and width.
- [x] Build tab: Wall, Platform, Stairs first; single pieces after. The menu keeps one size across tabs; R toggles it.
- [x] A room needs a built floor (user); the starter hut has one.

## AFK calls for the user to audit
- **Door allowance:** each wall may also have one 2 m doorway on top of its 10%. Why: walls are
  1 m columns and a creature needs 1.5 m, so a plain 10% allowed no walk-in door under 20 m.
- ~~Ground is a floor~~: reversed by the user; a room needs a built floor.
- **Taken cells are skipped** in a drag (dragging over an old wall fills the gaps), not refused.
- **Wilds punch any piece they bump into** (furniture too), else they stall forever on a bed.
- **Punch damage heals at dawn** (no hidden damage carried between nights).
- **A broken room:** occupants leave; a jailed creature leaves unreformed and calm.
- ~~One 5 m wall piece at 1 wood~~: reversed by the user; a wall cell is 5 real blocks, 5 wood. A hut is 95 planks (about 24 logs).
- **The old walk-through wreck switch was removed** (one way for a wild to break a piece).

## Still to build (decided by the user)
- [x] **Offspring inherit grown stats:** the baby's stats pull toward the parents' mid by heritability (already on main since #286: `StatsComponent.head_start`, STAT_HERITABILITY).
- [x] **Recruits stay wild-tempered:** a recruit joins RECRUIT_WARMTH_STEP colder (lower mood centre, so its history sinks sooner); a served jail warms it back.
- [x] **Recruiting holds the bed:** a wild mends at RECRUIT_MEND_MULT of the bed rate (over 4x an ally's time).
- [x] **Egg funnel:** measured; the dusk roll replaced the court trigger (`docs/LAW_life.md` rule 5).
- [ ] Counters to stacked wall layers (user: later).
- [x] **Energy and sleep beds:** built to `docs/LAW_beds.md` (one sleeper per bed, close ones share, dawn reassignment, tired = unproductive).
