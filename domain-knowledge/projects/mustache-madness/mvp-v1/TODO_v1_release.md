# TODO: version 1

The user asked (2026-10-07, AFK) for a complete, fun, solid v1 that includes a shop and
exploration, with improved UI, an evaluation of the game, and a shipped PR. Each slice gets
its own `/design` pass. Decisions made without the user are in the AFK log; audit those.

## Removed (2026-10-07)
The barber (roles now emerge from raising, `docs/TODO_emergent_roles.md`), and the dens with
the 140 m map, den-sourced night waves, and the win screen: "exploration" in the request
meant exploring ideas, not the map. The rows below about them are history.

## Frame (as built AFK)
The statue sits at the centre. Every night's wilds come from dens you can see out on the
map. Each den is guarded by sleeping wilds that never leave it. By day or night you take
part of the herd out to beat a den's guards, recruit them in beds, and the den falls; the
rest of the herd guards the statue. A barber sells mustache styles that give one creature a
new verb. Break every den to win; the statue falling loses.

## Pieces
| Piece | Rule | Why it earns its place |
|---|---|---|
| Den | A mound on the map with a sign readable from far. Its guards sleep around it (💤) and are fought only by creatures put down near it; a hit wakes the whole den. A guard fights only near its den. Each dawn the standing guards lie down again and the den gains one. The den falls when no guard of it is standing (downed, recruited, or gone) | The threat is a place the player can go and end. Exploration and defense become one loop |
| Night marchers | Each night's wave (the existing budget curve) spawns at the living dens instead of a random ring spot, and walks at the statue | The player sees where the night comes from |
| Budget flow | The night's wave (the existing budget curve) sets out from the den of each group's species, or any standing den once that one fell | Every night still comes, from fewer places |
| Friends follow | Grabbing a creature takes the friendlies standing within 6 m along (👣): they walk after the player and, where the carried one is put down, that spot is their home too. A throw or an escape ends the walk with homes unchanged; a downed body pulls no one | A party moves without picking creatures one by one |
| Barber | A cart with one chair per style. A creature put down in a chair pays gems from the player and wears that style. A style takes the creature's job slot (no job while styled) | The shop turns gems into a verb, paid for with a worker |
| Styles | Medic: carries any downed body (friend or wild) to a free bed. Bodyguard: hostiles within 8 m target it first | Each is a new verb that links existing mechanics |
| Win | The last den falls: win screen | The run has an end that only exploration reaches |

Cut, with reasons:
- Breaking a den by hand: the player cannot be hurt and has no attack, so a hand break
  solves the run in about 30 s with no fight.
- Night sleepers march and leave the mound empty: a night visit would break dens for free.
- Hauler style (auto pick-up): a convenience, close to a flat bonus.
- Price rising per copy at the barber: a price, not occupied state; the job slot is the cost.
- Relic pieces as the win: a new noun; the dens already are the win.
- Touring circus, signpost expeditions: same purposes as the barber and friends-follow with a
  weaker read or an unbuilt chooser.
- Map reveal UI: menu-driven; dens are tall and visible from far.

Prior art: Dome Keeper (go out between waves, the run ends when the dome falls), Slime
Rancher (explore for new species, sell what the herd makes), Palworld (capture outside,
assign at base), Pikmin (lead a group, throw creatures at things).

## AFK decision log
| Decision | Resolved as | Evidence or reason |
|---|---|---|
| Clock | Kept at the user's 15 s first daylight | The user set it on 2026-10-06. Dens do not depend on day or night, so the loop works on this clock. Offered below as an open call |
| Den guards vs marchers | Separate: guards sleep at the den and never leave it; the night's marchers walk at the statue | One kind doing both lets a night visit empty a den for free |
| What wakes a guard | A hit. A sleeping den is a target only for friendlies whose home is within reach of it (put down there) | Measured: with proximity waking, home defenders chasing marchers woke dens and won the run with no raid |
| A recruited guard | Its home becomes where it got up (its bed) | Measured: keeping the den as home made every recruit walk back and raid its old den |
| Den growth | Each dawn a standing den's guards lie down again and it gains 1 guard, up to 3 over its start | Measured: static dens fell to a turtling herd by night 5; growth makes waiting cost |
| Den rows | Bunny 6 guards at 45 m, fox 5 at 52 m, frog 4 at 60 m | A rising ladder: the bunny den is the first raid, the frog den the last |
| Marchers | Spawn on the den's far side (away from the statue) | Home fights stayed out of the guards' reach |
| Map | 140 x 140 m (was 60 x 60) | Exploration needs room; at 60 m every den sat inside a defender's notice radius |
| Starter herd | One of each species (was one frog) | One frog died to the first den it wandered near; three species show the range axis from the start |
| Statue attackers | Every hostile may attack it (was 3) | Measured: past the third, marchers stood idle at their den, so 173 wilds piled up with the statue full |
| Statue health | 2500 (was 1000) | With every marcher attacking, one bad night erased 1000 in about 6 s |
| Barber place | Fixed, 22 m out | A cart that moves each dawn is a forced trek on a 15 s day |
| Barber payment | The client pays its own gems when it puts a creature down at a chair; the server seats any non-hostile | Same trust model as build placement (the hotbar is the client's) |
| Medic | Carries the nearest loose downed body, friend or wild, to the nearest free bed | Merges rescue and recruit into one verb |
| Bodyguard | Within 8 m, hostiles score it like a creature that hit them | One rule in the target score |
| Run HUD | Clock with seconds to night or dawn (red in the last 5 s), statue health, dens busted, gems; a rotating tip line for the first 3 days | The game had no clock, no statue readout away from it, and no onboarding for the new loop |
| Old guide frog | Left in the code, still not spawned | Its tips name the removed well; the HUD tip line covers onboarding for now |

## Evaluation (headless bot runs, `test/local/sim/test_sim_v1.gd`)
Bots: `turtle` only carries downed bodies to beds; `raid` also sends half the herd to the
nearest den each dawn. No bot throws, builds, or uses the barber, so a human has far more
tools. Before the last tuning (statue 1000, growth to 9 guards):
| Run | Result |
|---|---|
| turtle 1 | Won on night 12: the home herd drifted into the dens |
| turtle 2 | Lost on night 10, 1 den busted |
| raid 1 | Lost on night 9, 2 dens busted |
| raid 2 | Lost on night 5, 0 dens busted |

After the tuning (statue 2500, growth to 3 over the start):
| Run | Result |
|---|---|
| turtle | Lost on night 11 with 2 dens busted by drift; 29 wilds reached the statue at once |
| raid 1 | Lost on night 10 with 2 dens busted |
| raid 2 | Won on night 9, statue at full health |

Read: the run has a shape (early dens fall, the last den and the night waves press), and
raiding busts dens a turtle does not. Two things still blunt the raid decision: a home
herd drifts toward dens because knockback moves a creature's home to where it lands, and a
dumb raid feeds the den. A human playtest is the next gate.

## Open calls (user)
| # | Call | Lean |
|---|---|---|
| 1 | First daylight is 15 s | 30 to 60 s, so a free stretch at a place fits inside one day |
| 3 | Knockback moves a creature's home to where it lands, so fights drift homes outward | Drop it: home follows the hand only |
| 5 | The old guide frog and its tips | Delete it, or rewrite it for the places loop |
| 6 | The run has no win condition since the dens left | Leave it endless until the loop is fun |

## Slices
- [x] 1-2: three dens with guards, marchers set out from them, win screen.
- [x] 3: friends follow the carried creature.
- [x] 4-5: barber with the Medic and Bodyguard chairs.
- [x] 6: run HUD and onboarding tips.
- [x] 7: evaluation runs and tuning.
- [ ] Human playtest: cheat console `den`, `bust`, `style`, `gems` (F1), `sad` (F3).
