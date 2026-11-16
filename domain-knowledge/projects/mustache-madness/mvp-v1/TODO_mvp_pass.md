# TODO: MVP readiness pass

The user asked (2026-10-08, AFK) for a review of every feature and a multistep pass toward
an MVP: UI, UX, performance, headless sims, balance, more creatures, more objects,
creature needs readability, and an intuitive build UI. Each step gets its own `/design`
pass; decisions made without the user are in the AFK log. Audit those.

## Baseline (measured before any change)
Headless sim, `turtle` bot (carries downed bodies to beds, nothing else), all four places
built at the start, 600 game s:
| Fact | Value |
|---|---|
| Nights survived | 13 of 13 (run ended by the time cap) |
| Lowest statue health | 2236 / 2500 (89%) |
| Herd | 3 at the start, 14 by night 13 |
| Downed bodies at dawn | 16 to 28 from night 10 on (3 beds) |
| Sim speed | 600 game s in 157 s wall (3.8x) |

Read: a player who does almost nothing never loses. The statue is never in danger, so no
choice the player makes matters to the outcome.

## Steps
| # | Step | Status |
|---|---|---|
| 1 | Sim harness: seeds, bot policies, one result line, a runner that aggregates | Done (a4eec0c) |
| 2 | Performance: measure, fix the hot paths | Done (a4eec0c): 63 creatures 12.9 ms to 4.4 ms |
| 3 | More creatures | Done (94c37c7): owl, goat |
| 4 | More objects (from `docs/TODO_object_catalogue.md`) | Done: medic bed, jail, woodpile, nest (one egg each); protein bar, breeding crops, death drops cut; gym shown as bench press |
| 5 | Balance with the sims | Done: wave block step 1.5 -> 2.6. Idle falls night 7-8, turtle falls night 10 in 2 of 3 seeds, active survives 13 (statue low 0.89). 2.25 was a pushover, 3.0 broke even the active bot: the herd snowballs once it clears the night-6 spike |
| 6 | Build UI | Done: category tabs (Build, Stay, Work, Free time, Gadgets; a Blueprint field) over a grid of picture cards (the piece's icon, name, price) |
| 7 | Creature readability | Done: the aim readout names the creature and, for a friend, shows how it feels and its biggest drag (hurt, lonely, cold temper), its moodlets, a steam bar, and the place it wants |
| 8 | HUD and menus | Done: the start menu has a wobbling title, tagline, sky and grass, a big Play button; the HUD shows wood beside gems |

## AFK decision log (audit these)
| Gate | Resolved as | Why |
|---|---|---|
| Step 4 objects | First-aid tent and jail (catalogue open calls 1 and 2 at their leans); protein bar removed (catalogue: VIT trainer rejected) | Both are "Decided" rows in `docs/TODO_object_catalogue.md`; see its AFK log |
| Start set | One start bed swapped for a tent | Rescue needs a recovery object from night 1, as it had the bed before |

## Asks added on 2026-10-09 (the user, while away; each gets a full /design, Team mode)
| Ask | Status |
|---|---|
| One chopper (one axe) per woodpile; one job per station | Done |
| No barn animals: the goat becomes a hedgehog; pet-type, uncommon creatures (no dogs); a cat may come as a special mid-price creature | Hedgehog done; cat proposed in docs/BRAINSTORM_crops_dishes_cat.md |
| Jail has a reason: long low mood makes a creature snap; a few are born with bad stats (bad mood, jail-prone); a social punch action with fighting back; fights heat things up | Done (docs/TODO_trouble_comfort.md) |
| Comfort: a housing system (bed, chair, table, games, decor) that lifts mood, work, eggs, and calm; own axis or existing | Done, first slice: a chair (lounge) and games table (docs/TODO_trouble_comfort.md) |
| Build UI: piece pictures, categories instead of a flat list | Done (step 6) |
| Game start menu | Done (step 8) |
| Think: more crops? Which kitchen dishes? | Proposal in docs/BRAINSTORM_crops_dishes_cat.md (with the cat) |
| Automated playtest QA run (the polish headless system) | Done: `SIM_QA=1` (util/debug/qa_watch.gd). First run found creatures knocked through the terrain (fixed: shared under-world rescue) |
| Start layout: only the statue and one medic bed | Done. The lab became a buildable basic (10 wood, 2 gems) so research stays reachable; this overrides roadmap call U1 (lab in the start set) |
