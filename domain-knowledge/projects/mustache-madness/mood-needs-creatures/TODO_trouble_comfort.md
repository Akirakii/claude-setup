# TODO: trouble (steam, snap, punch) and comfort places

Designed AFK on 2026-10-09 (Team mode: a diverger and a challenger, blind to each other).
Every call below is Claude's pick for the user's two asks: audit them.

## Frame
Mood stays the one feeling dial. Trouble is pressure that builds from lasting low mood and
from fights, and it releases in a snap the player answers with the jail. Comfort is not a
new axis: it is a kind of place whose output drains that pressure, with mood only as a side
effect. So the user's chain holds (comfort -> calm -> fewer fights -> less jail; calm ->
better mood -> longer work stretches and more courting), through state the player sees.

## Data dictionary
| Variable | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| `steam` | float 0..1 | creature (server) | Built-up pressure | Fills from low mood and hits; drains from good mood and comfort seats; empties on a snap's end or a served jail |
| `rampage` | Cooldown | creature (server) | A snapped creature punching whoever is near | Armed at steam 1; ends only when jailed or downed (user, 2026-10-09) |
| `grump` | bool | creature (spawn data) | Born hot-tempered and weak | Rolled once at spawn with `GRUMP_CHANCE`; never changes |
| COMFORT place | `OfferPlace.Kind` | placed piece | A seat that drains steam | Spots as usual |

## Pipeline (each creature tick on its dilated clock)
1. `steam += dt * (STEAM_FILL * max(0, -mood) - STEAM_COOL * max(0, mood)) / MOOD_MAX`.
2. Seated on a COMFORT spot: `steam -= dt * STEAM_SEAT_DRAIN`, plus the `cozy` moodlet.
3. A punch landed or taken: `steam += STEAM_PER_HIT` for both.
4. `steam >= 1` and not jailed: arm `rampage`.
5. Rampage: walk to the nearest friendly within `RAMPAGE_REACH` and punch it; no job, no
   social, no places.
6. Jail served or downed: `steam = 0`, rampage off.

## Interaction matrix (rows feed columns)
| | steam | rampage | punches | mood |
|---|---|---|---|---|
| low mood | up | 0 | up (bully odds) | - |
| good mood | down | 0 | down | - |
| comfort seat | down | 0 | 0 | up (cozy) |
| punch taken | up | 0 | up (fight back) | down (hurt) |
| grump | up (cold set-point) | 0 | up (temper) | down |
| jail | resets | ends | 0 | 0 |

## Constants
| Constant | Value | Kind |
|---|---|---|
| `STEAM_FILL` | 0.004 /s per mood point below 0 | pace: about two game days at mood -3 to snap |
| `STEAM_COOL` | 0.01 /s per mood point above 0 | pace: good mood lets steam off faster than misery builds it |
| `STEAM_PER_HIT` | 0.1 | weight |
| `RAMPAGE_PUNCH_SEC` | 1.5 dilated s | pace: a rampager throws the light social punch, never a full strike |
| `PUNCH_DAMAGE` | 4, never below 1 hp | limit: a punch never knocks anyone out |
| `STEAM_SEAT_DRAIN` | 0.1 /s | pace |
| `RAMPAGE_REACH` | 12 m | limit |
| `GRUMP_CHANCE` | 0.08 | weight |
| `GRUMP_STAT_MULT` | 0.6 | weight |

## Signs
- 😠 over a creature from a quarter of steam, 😡 from three quarters, 🤬 while it rampages (user).
- "Grumpy" in front of a grump's name.
- The punch is the existing 👊 action with a real hit and a hit back.

## Slices
Superseded by #326: mood history and brewing replaced steam; slices 1, 2 and 4 describe the old model (design: `docs/BRAINSTORM_mood_fun_steam.md`).
1. [x] Steam, snap, rampage, jail ends it; punch with fight back; grumps; cheats `/snap`, `/grump`.
   Measured (turtle bot never jails, 10-creature start, 600 s): 0 and 6 snaps; a first cut
   with full-strike rampages and 5x faster steam spiralled (statue fell, 17 friends lost).
2. [x] Comfort places: chair (1 spot, when no meal waits), games table (2 spots), kind COMFORT; want leans on
   laziness (low discipline), output drains steam, cozy moodlet once per stay.
3. [x] Cop job: a paid police box's cop carries a rampager in its 15 m ring to a free jail
   cell, the player's jail answer without the player's hands.
4. [ ] Measure in sims: snaps per night, jail use; tune.

## Open calls (user)
- Jail's lasting +0.2 warmth reads as a flat bonus (challenger). Keep it, or let jail only
  release steam?
- Decor with no output was left out; does the user want pure decoration anyway?
