# BRAINSTORM: design c1, room tool (PR 1)

Design only (AFK /explode, relay 1). Lattice reminder: a cell is 0.5 m; a block is 2x2x2 cells
(1 m), a half block 2x1x2 (`entities/builds/half_block/half_block.tres:12`).

### PR 1: Room tool (user)
- **Frame:** a closed room today costs four wall drags, a floor drag and a roof drag lined up by
  eye; the player wants one drag, corner to corner, that stands a usable room (walls, half-block
  floor and roof), with Ctrl + wheel setting its wall height (user).
- **Assumptions to verify:**
  - [x] "Half Block" in the catalogue is two cards on one piece: `floor` (menu, Pattern.FLOOR,
    named "Half Block") and `half_block` (single, off menu); both lay `half_block.tres`, 1 plank
    (`systems/progression/blueprint_registry.gd:61-84`). Walls are `block.tres`, 1 plank (`:44-52`).
  - [x] A pure "rectangle -> pieces" already exists, twice: `BuildPattern.lay` (pure, takes a
    `settle` Callable, `entities/player/components/build_pattern.gd:11`) and the starter hut's
    `Game.hut_pieces` (`systems/level/game.gd:285`): walls on the outer ring 1 m outside the
    floor, a floored 2 m doorway `DOOR_HEIGHT` 8 cells high on -X (`game.gd:12`), roof at +10
    cells. The room tool is the same shape with a height and a door side as inputs.
  - [x] The plain wheel sets a wall drag's height and is otherwise "put the piece away"
    (`entities/player/player.gd:558-572`, `build_hand.gd:211`). Ctrl + wheel is bound to nothing:
    no camera zoom exists; Ctrl is read only by the axe's fast break (`axe_behavior.gd:19`);
    `project.godot` has no Ctrl action. The wheel event is an `InputEventMouseButton`, which
    carries `ctrl_pressed` (Godot `InputEventWithModifiers`); the open build menu eats the wheel
    first (`ui/hud/build_menu.gd:176`, `player.gd:558` checks `active_ui == null`).
  - [x] A drag sends one RPC with `facing` and `height` (`systems/net/network_manager.gd:185`);
    `_place_laid` spawns every entry as ONE meta (`:204`), and the ghost draws every pose as ONE
    scene (`entities/player/components/build_preview.gd:36-46`). Both must learn mixed pieces.
  - [x] Roof: no gap needed. Openings are optional (`docs/LAW_rooms.md` rule 3); creatures need a
    walk-in door or every room-only piece switches off with the door sign (rule 4).
  - [x] `DRAG_MAX_PIECES` 400 slices a drag (`build_hand.gd:12,89`); a 9 x 9 m room at 5 high is
    about 400 pieces, so the slice would cut the roof off silently.
  - [ ] Open: preview cost of a large room. Each re-lay runs one physics query per piece
    (`_drag_preview`, `build_hand.gd:248`); a 24 m room is about 1800. Check frame time on a
    `/room` drag at full span before merging.
  - [x] Chores already staged in the worktree: `docs/HANDOFF_economy_stage1.md` deleted, task 6 of
    `docs/TODO_gem_income.md` ticked (`git status`). The builder only commits them.
- **Candidates:**
  - A. Room card in the Build tab; one drag lays a ROOM pattern with a 2 m doorway in the wall
    nearest the player, shown in the ghost. Survives.
  - B. Room as a third reading of the Build tool (Tab cycles wall, floor, room). Cut: one-verb
    multiplex, and the user asked for a menu entry.
  - C. Sealed room, no door (The Sims 4 room tool, Prison Architect foundations: from memory, the
    door is a separate piece there). Cut as default: this game has no door piece, so the first
    scene is the player chopping 8 blocks out of a fresh room, and a sealed room shows the door
    sign. Kept as an open fork.
  - D. Three requests (wall, floor, roof) chained like `hut_pieces` does today. Cut: three
    payments break "the whole drag or nothing" (rule 2), no door cut, the ghost shows three tools.
  - E. One prefab "room" object. Cut: walls must stay single pieces a wild punches (rule 5) and an
    axe breaks.
- **Recommendation:** A. Scene: the player picks Room, holds right click on a corner, walks to
  the far corner. A green ghost shows four walls, a half-block floor, a roof, and a doorway in
  the wall the player stands nearest; walking around the ghost moves the doorway. Ctrl + wheel
  raises the walls (caption "ctrl+wheel: 4 high"); release pays and builds. The next room starts
  4 high. Mechanism: drag corners are the outer wall corners; walls on the ring, floor inside it
  at the start's height (plus under the doorway), roof over the whole ring at `start.y + 2 *
  height`. Each wall column rises from its settled foot to the roof, so a slope leaves no gap.
  Door: the middle 2 columns of that side (1 if the side has only 1), open `min(DOOR_HEIGHT, 2 *
  height - 2)` cells, so the top block stays as a lintel; no door at height 1. A rect with no
  inside (either span under 4 cells) or past `Rooms.MAX_SPAN` lays nothing.
- **Build sketch:**
  - `systems/progression/metadata/blueprint.gd:8`: add `ROOM` to `Pattern`.
  - `blueprint_registry.gd:44`: a basic after `build`: `{"id": "room", "name": "Room", "meta":
    block.tres, "icon": <existing png, see open question>, "planks": 1, "pattern": ROOM}`.
  - `build_pattern.gd`: move `DOOR_HEIGHT` here from `game.gd:12`; add a `Pattern.ROOM` branch to
    `lay` where `facing` is the door side and `height` the wall blocks. Each entry gets
    `"piece": "block"` or `"half_block"` and `"part"`: wall, floor or roof. No duplicate corners.
    Add pure `static func door_side(a, b: Vector3i, at: Vector2) -> Vector2i` (the side whose wall
    line is nearest `at`, ties to X).
  - `build_hand.gd`: `var room_height := BuildPattern.WALL_BLOCKS` (kept, like `wall_height:21`).
    `lay` (`:80`): compute `replaces` for WALL entries and ROOM wall entries; skip the 400 slice for
    ROOM (its bound is `Rooms.MAX_SPAN`). `_drag_preview` (`:248`) and `fits`: use each entry's
    own placed behavior (`Blueprints.blueprint_by_id(e.piece).place_meta`) and put it on the pose
    (`pose["piece"]`). One helper `laid_cost(entries)` sums `Blueprints.build_cost` per entry, used
    by the preview price and `_place_drag:347` (2 uses). `_place_drag` sends `door_side(...)` of
    the player's xz as `facing` and `room_height` as `height` for ROOM. `wheel_wall_height:211`
    becomes `wheel_height(player, up, ctrl)`: a ROOM drag steps `room_height` (clamp
    `WALL_MIN_BLOCKS..WALL_MAX_BLOCKS`) and returns true; the AUTO wall case stays. `drag_hint`:
    "right drag: corner to corner" / "release: build · ctrl+wheel: %d high".
  - `player.gd:564`: pass `event.ctrl_pressed`.
  - `network_manager.gd:204` `_place_laid`: entries may carry `piece`; pick each entry's behavior
    and meta from it (default the drag's meta). Harvest crops per entry and call
    `PlacedBehavior.push_out` once with the mixed `[behavior, cell, step]` list (it already takes
    one behavior per piece, `placed_behavior.gd:160`), so a creature leaves the whole room at once.
  - `build_preview.gd:36`: a pose's `piece` overrides `info["piece"]`; keep ghosts in a pool per
    scene instead of one `_ghost_scene`.
  - `game.gd:285` `hut_pieces`: becomes `BuildHand.lay(room, low - (2,0,2), low + (size,0,size),
    Vector2i(-1, 0), WALL_BLOCKS)` mapped to `[meta, cell]`. Same pieces on flat ground; the
    room-gate and bed tests guard it. One path for the hut, the tool and PR 2.
  - `docs/LAW_rooms.md` rule 1: add the Room tool line; data dictionary: `room_height`, move
    `DOOR_HEIGHT`. README feature checklist: one line.
- **Tests + cheat key:**
  - `test/ci/entities/player/test_build_pattern.gd`:
    `test_a_room_drag_lays_4_walls_a_half_block_floor_and_a_roof`: `lay(ROOM, (0,0,0), (8,0,8),
    ONE_M, identity, Vector2i(-1,0), 5)`: 16 ring feet x 5 blocks minus the doorway's 2 x 4, floor
    9 + 2 doorway cells at y 0 as half_block, roof 25 cells at y 10 as half_block, lintel at (0,8,z).
    `test_a_room_wall_rises_to_the_roof_from_a_lower_foot` (a settle that drops one foot 2 cells:
    6 blocks there). `test_a_room_with_no_inside_lays_nothing`. `test_the_door_faces_the_nearest_
    side` (`door_side` inside and outside the rect).
    `test_a_server_room_drag_is_a_room`: `_net_request_place_pattern("room", ...)`, then
    `Grid.get_block` kinds per part and `Rooms.find(inside)` not empty.
  - `test/ci/ui/hud/test_build_menu.gd`: `test_ctrl_wheel_sets_the_room_height_and_keeps_it`:
    room in hand, `drag_start` set, `_unhandled_input(wheel up, ctrl)`: `room_height` 6, piece
    still in hand, `wall_height` unchanged; after a new drag it is still 6.
  - `test_build_hand.gd:36` `test_the_menu_starts_with_the_basics`: Room in the Build tab.
  - Cheat `/room` (stock): the Room tool in hand (`player._raise_build_hand`, `player.gd:453`) and
    60 wood, as `/hut` does (`cheat_coordinator.gd:517`).
- **Shared with other clusters:** `BuildPattern.lay(Pattern.ROOM, a, b, size, settle, door_side,
  height)` is the pure "room footprint -> pieces" step PR 2's architect ghost needs (it picks the
  door side itself, e.g. toward the bed anchor's way in); per-entry `piece` in `_place_laid` and
  mixed-scene ghosts in `BuildPreview` serve PR 2's blue ghost and its builders' per-piece
  hammering; `laid_cost` is the site's bill of materials for PR 2 and PR 4's stockpile.
- **Open questions for the user:**
  - Door: auto doorway in the wall nearest you (recommended), or a sealed room you chop open?
  - Plain wheel during a room drag: also sets the height (recommended: else it drops the tool
    mid-drag), or Ctrl only, as written?
  - Card icon: reuse the Build tool icon for now (recommended), or a new picture?
