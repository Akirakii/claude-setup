# TODO: emergent roles (rescue, guard, own personality)

A design, not yet built. Pillar: roles emerge from raising, never from a purchase
(`MEMORY.md`). The barber goes; rescue and guard fall out of each creature's own bonds,
stats, mood, and personality.

## Decided (user, 2026-10-07)
- Remove the barber.
- Personality has 3 axes: sociability, warmth (its cold side is the temper that picks
  fights), discipline. Built.
- Rescue: friendship always picks who goes. Warmth sets the bar a creature must clear to
  go; with low friendship, mood helps clear it. Friends only, never wilds.
- Guard: the healthiest friendly draws wild hits (exists) + a friendly prefers the wild
  hitting a weaker friend.
- A species defines only the average personality; each creature owns its own.

## Data
| Variable | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| species mean (soc, warm, disc) | float -1..1 each | Species metadata (authored) | The stereotype | Static |
| personality (soc, warm, disc) | float -1..1 each | Creature (server picks, rides the spawn data to every peer) | This creature's own axes | Set once at spawn, never changes |
| temper | float -1..1 | Computed | `-warm` | Not stored |
| f | float 0..1 | Computed per rescuer and patient | `max(0, friendliness) / SOCIAL_FRIEND_MAX` | Not stored |
| m | float -1.5..0.5 | Computed | `(mood - MOOD_NORMAL) / MOOD_MAX`, the lean social rolls already use | Not stored |
| will | float | Computed | `f + (1 - f) * RESCUE_MOOD_W * m`: mood counts only as far as friendship is missing | Not stored |
| bar | float | Computed | `RESCUE_BAR * (1 - PERSONALITY_GAIN * warm)` | Not stored |
| near | float 0..1 | Computed | `1 - distance / RESCUE_RADIUS`, floored at 0 | Not stored |
| guard pull | float, metres | Computed per friendly and wild | `GUARD_W * f_T * clamp((hp_self - hp_T) / max_hp_self, 0, 1)`, T = the friend the wild is hitting | Not stored |

## Pipeline
| Stage | Reads | Writes |
|---|---|---|
| Spawn | Species mean, spread, (parents, if inheritance is picked) | personality |
| Downed | A friendly goes DOWN, lying loose | Becomes a patient |
| Rescue pick | Each free friendly within RESCUE_RADIUS: f, m, warm | The one rescuer: willing (`will >= bar`, f > 0) and highest `f * near` among the willing |
| Carry | Rescuer, nearest free bed | Patient in bed; ⛑ flash while carrying |
| Guard pick | Friendly scoring wilds: the wild's target, f to it, both HPs | Target score minus guard pull |
| Draw (exists) | Wild scoring friendlies within 20 m: live HP; fight-back on whoever hit it | The guard takes the hits |

Rescue rung: below fight and own bed, above follow, feed, social, work (the slot the
medic used).

## What moves what
| | Who rescues | Whether it goes | Guard target | Draws hits |
|---|---|---|---|---|
| Friendship | Picks (`f * near`) | Raises will | Scales pull | 0 |
| Mood | 0 | Raises or lowers will when f is low | 0 | 0 |
| Warmth | 0 | Lowers the bar | 0 | 0 |
| VIT / live HP | 0 | 0 | HP margin | Picks |
| Distance | near | Inside RESCUE_RADIUS | Existing distance term | Existing distance term |

## Charts
Bar by warmth (`RESCUE_BAR` 0.4):
| warm | -1 | 0 | 1 |
|---|---|---|---|
| bar | 0.6 | 0.4 | 0.2 |

Will (`RESCUE_MOOD_W` 1.0):
| f \ mood | -5 (m -1.5) | 2.5 (m 0) | 5 (m 0.5) |
|---|---|---|---|
| 0.1 | -1.25 | 0.1 | 0.55 |
| 0.4 | -0.5 | 0.4 | 0.7 |
| 1.0 | 1.0 | 1.0 | 1.0 |

So a best friend always goes; a weak friend goes when happy, or when warm; a sad,
cold, weak friend stays away.

Personality spread (`PERSONALITY_SPREAD` 0.35, normal, clamped): a bunny's warmth
(mean 0.6) lands between 0.25 and 0.95 two times in three; one bunny in about 20 is
colder than 0.

## Loop checks
| Loop | Start | End | Floor |
|---|---|---|---|
| Rescue, bed, life, more time together, more friendship, more rescues | Any f > 0 with good mood or warmth | Bonds decay (half-life ~3 days) | A loner is never rescued: the player carries it |
| Guard tanks, VIT XP per hit, more HP, draws more | A high-VIT friendly near a friend | Its live HP falls, so it stops drawing and goes to bed | Others fight as before |

## Constants
| Constant | Kind | Note |
|---|---|---|
| RESCUE_BAR | Threshold, user-chosen | Warmth moves it per creature |
| RESCUE_MOOD_W | Weight | How far mood fills missing friendship |
| RESCUE_RADIUS | Limit | 25 m, the old medic reach |
| GUARD_W | Weight, metres | How far a friendly goes out of its way to cover a friend |
| PERSONALITY_SPREAD | Limit | One spread for every axis and species |
| PERSONALITY_GAIN | Weight | Exists, reused |

## Slices
- [x] Personality down to 3 axes.
- [x] Each creature owns its personality (spawn data); species keep the mean; a baby
  inherits.
- [x] Remove the barber.
- [x] Rescue. Cheats: `bond`, then `down` on a creature.
- [x] Guard. Cheats: `bond`, wound one creature, then `fight`.
- [ ] Playtest; balance probe on frog courting (Court now leans on warmth, not wit) and the
  rescue O(n^2) scan with many downed bodies.

## Open calls (user)
| # | Call | Lean |
|---|---|---|
| 1 | A baby inherits personality: `species mean + 0.5 * (parents' mid - species mean) + noise`. Built on the lean when the user said "build"; confirm | Yes: breeding becomes how the player raises temperaments |
| 2 | Spread 0.35 | Playtest |
| 3 | A fused creature (combiner) rolls a fresh personality from its species | - |
