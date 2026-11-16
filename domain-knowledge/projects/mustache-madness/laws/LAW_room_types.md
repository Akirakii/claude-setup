# LAW: room types and skins

Standing law for what a room is, by what stands in it. User decisions are tagged (user).
Rooms themselves: `docs/LAW_rooms.md`. Per-type rules, mixed rooms and status:
`docs/TODO_room_types.md`.

## Rules
1. **The pieces decide (user).** A room's type falls out of the pieces standing in its air;
   there is no designation verb. An anchor piece names the type it makes; table, chair
   and lamp name none and fit any room (user).
2. **One kind of anchor gives that type; none or two kinds give a Plain room (user).** Beds:
   1 or 2 make a Bedroom, 3 or more a Bunkhouse (user).
3. **The type sets the look (user).** Every basic piece that closes the room (wall, floor,
   ceiling) wears the type's skin. A piece that closes only rooms of one look wears it on
   every face, the outside included, so the type reads from outside. A piece between two
   looks (a wall between a bar and a bedroom, a floor over another room) stays bare plank
   and gets a lining on each side: a thin skin on the face toward each room (user).
4. **Role by face.** A piece under the room's air is floor, over it is ceiling, beside it is
   wall; each role has its own pattern and shade. A piece the air meets only at an edge or a
   corner (a corner column, a doorway's floor, the roof's rim) is part of the shell too (user):
   it reads as wall when it touches the air beside it, else as floor or ceiling.
5. **Plain keeps the old look:** a Plain room's planks read 15% more saturated (user). A room
   with no watched piece in it (anchor or room-only) is not drawn: bare plank.
6. **Placeholder art (user).** Skins are images generated at run time: one hue per type, a
   pattern per role, and per-pixel noise. Real textures replace them later.
7. **Every peer draws its own.** The type is derived from the replicated Grid; nothing new
   is saved or replicated.

## Types
| Type | Anchor | Hue |
|---|---|---|
| Bedroom | 1–2 Beds | pink |
| Bunkhouse | 3+ Beds | tan |
| Hospital | medic bed | white-cyan |
| Nursery | nest | yellow |
| Prison | jail | grey |
| Restaurant | kitchen | brick red |
| Bar | bar | purple |
| Arcade | games table | magenta |
| Gym | gym, treadmill | orange |
| Lab | lab | green |
| Library | library | blue |
| School | chalkboard | teal |
| University | lectern | violet, brick walls |
| Bank | bank | gold |
| Plain | none, or mixed | saturated plank |

## Data
| Name | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| `room_type` | StringName or empty | PlacedBehavior (static) | The type an anchor makes | authored |
| type | StringName | derived | The room's type | recomputed on any lattice or room change, never stored |
| `BEDROOM_BEDS` | 2 | RoomSkins | Most Beds a Bedroom holds | constant (user) |
| `SHELL_SATURATE` | 1.15 | RoomSkins | A Plain room's plank saturation | constant (user) |

## Pipeline (`RoomSkins.tick`, once a frame from `Rooms.tick`)
1. **Key:** `(Rooms.revision, Grid.revision)`; unchanged means nothing to do. Placing
   furniture moves `Grid.revision` only, so both are needed.
2. **Rooms:** each watched piece (an anchor or a room-only piece) asks `Rooms.room_at`; each
   room is handled once per key.
3. **Type:** count the anchor kinds on the room's cells (rule 2).
4. **Faces:** every basic piece next to the room's air gets `{face: [type, role]}`.
5. **Draw:** only pieces whose faces changed since the last draw are redrawn (rule 3); a
   piece no room claims any more goes bare.

## Cheat
`/skins` (rooms folder): a hut of every type ahead, 2 rows of 7.
