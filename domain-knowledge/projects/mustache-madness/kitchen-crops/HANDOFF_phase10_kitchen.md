# Handoff: Phase 10 slice 1, job board + kitchen

Built AFK on 2026-10-02. This file holds the decided design, the gates closed without the
user, and what did not ship.

## Decided by the user
- Kitchen = a stronger meal, made by a creature as a job.
- One worker per work site: 1 kitchen = 1 cook, 3 grown trees = 3 choppers.
- A kitchen is workable only while it holds crops; the player loads it.
- The kitchen is a held placeable (2026-10-05): the shop spits the item, the player
  grid-places it. It is static, takes one ground cell, and is not pushable.
- Moodlets are not per species, so there is one dish and one `meal` moodlet.
- A central job board matches creatures to sites (chosen over claim state on each site).
- Door / gate card dropped.

## Gates closed AFK (audit these)
| Gate | Resolution | Why |
|---|---|---|
| Does a worker keep its site during a break? | Yes | Releasing on break swaps hats every minute and the site changes hands constantly. |
| Who eats a dish? | Any species | Follows "not per species". Raw crops stay species-locked. |
| What does a dish do? | `meal` moodlet + the flat crop heal. No poop. | Raw crop keeps poop income; each crop is a choice between economy and mood. |
| When does a creature seek a dish? | Friendly, and wounded or without an active `meal` | `meal` stacks once, so a second dish would be wasted. |
| Corpses as ingredient? | Out | Unanswered; tone risk (grim sacrifice). Crops only. |
| Who drives matching? | The board, on one poll | Pillar: one driver per shared interaction, not N pollers. |
| Player picks a job with no free site? | Nothing changes | The user's rule: no taking a held site. |
| Can stored crops be knocked back out? | No | Loading the kitchen is a commitment. |
| Cook INT requirement | 8, same as Chop | Frogs cook from the start; others grow into it. |
| Axe hit on a placed kitchen? | Picks it back up as an item; loaded crops are lost | Same pickup as other pieces; crops stay a commitment (unconfirmed). |

## Spec

### Data dictionary
| Name | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| site job | `site id -> Job` | JobBoard | A site that can be worked now | Set by `post`, cleared by `withdraw` or when the site is freed |
| worker | `site id -> creature id` | JobBoard | Who holds the site | Set on match or request; cleared on release, on withdraw, or when the worker stops being FRIENDLY |
| hat path | String, replicated | Creature (JobComponent) | The visible job; written only by the board | Follows the worker entry |
| kitchen crops | int >= 0 | Kitchen | Crops waiting to be cooked | +n per thrown crop stack, -1 per cook tick |
| `meal` moodlet | amount 2.0, 0.5 day, stack 1 | Creature (MoodComponent) | Mood lift from a dish | Fades linearly to 0 |

### Pipeline
1. Player throws crops into the kitchen. Kitchen stores them and posts a COOK site.
2. Board poll: a free site takes the nearest jobless FRIENDLY creature whose INT clears the job.
   The creature gets the hat.
3. Worker in WORK phase walks to its site; each job interval it calls the site's `labor`.
4. Kitchen `labor`: crops -1, one dish spat out. At 0 crops the kitchen withdraws the site and
   the cook loses the hat.
5. A creature seeks the dish, eats it, gains `meal`.
6. The `meal` moodlet lifts mood (and with it every stat, ±3 at the limits).

Trees use steps 2 to 4 with `labor` = fell the tree; a grown tree posts, a felled one withdraws.

### Interaction matrix
| Input | Site posted | Match | Labor | Eat |
|---|---|---|---|---|
| kitchen crops | posts when > 0 | 0 | -1 per tick | 0 |
| creature INT | 0 | gates eligibility | 0 | 0 |
| distance to site | 0 | nearest wins | reach gate | 0 |
| work/break phase | 0 | 0 | labor only in WORK | 0 |
| local clock zone | 0 | 0 | shortens interval | shortens moodlet |
| active `meal` | 0 | 0 | 0 | blocks seeking |

### Loop check
- Bootstrap: needs one creature with INT >= 8 (a frog at start). No dependence on its own output.
- Termination: cooking stops at 0 crops; `meal` stacks once.
- No feedback edge: mood does not speed cooking.

### Constants
| Constant | Value | Kind |
|---|---|---|
| `JOBS[COOK].interval` | 3.0 s dilated | pace |
| `JOBS[COOK].reach` | 1.8 m | radius |
| `JOBS[*].req_int` | 8 | gate on eligibility (existing rule) |
| `JOB_BOARD_POLL_SEC` | 0.5 s | pace |
| `MOODLETS.meal` | +2.0, 0.5 day, stack 1 | weight + lifetime |
| kitchen card | tier 2, poop 10, growth 4 | placeholder until final calibration |

## Not shipped
- A client cannot see whether a job has a free site, so the job panel greys a job only for
  aptitude. A no-op click needs a visible "no free site" readout.
- Kitchen model, chef hat art, dish art are primitive placeholders; the kitchen icon is a
  drawn placeholder.
- Feel is unverified in play: cook pacing, dish pickup contention, mood carry into the night.
