# Method tournament results (2026-11-10, AFK run, 1 h)

User's ask: try different methods with different agents, score what checks the formula, keep the
methods that check better, try again in parallel; also check the idea isn't a duplicate of an existing
game; don't think about testing yet. Target and checks: `formula.md`. Raw scores: `eval/`.

Process per generation: each method runs in its own agent (no web while generating, no earlier notes),
keeps 8 ideas. The ideas are shuffled and given blind IDs. 2 formula raters (isolated critics, 6–12
shared ideas to measure agreement) score F1–F7 + G; 3 novelty checkers search the web for each core
rule (N). Score: ✓ 2, ~ 1, ✗ 0, max 18. Pass = no ✗. Strict = all ✓.

## Gen 1: 9 methods, 72 ideas (19:15–19:35)

| Method | Pass of 8 | Novel ✓/~/✗ | Mean of 18 | What it was good / bad at (generator's log, checked against the scores) |
|---|---|---|---|---|
| M2 real-world joint activities | **7** | 1/6/1 | **15.6** | blame and fantasy come free (a real slip is physical); raw ideas lean to pooled effort or one caller |
| M8 tabletop & playground translation | 5 | 0/6/2 | 14.5 | physical playground rules translate easily; novelty capped at ~ (the source shares the core) |
| M5 failure inversion (famous co-op games) | 5 | 2/5/1 | 14.4 | "whose fault was it?" pushes F3/F4; the source game anchors the shape |
| M4 random stimulus (noun × verb) | 5 | **3**/2/3 | 13.1 | most novel; every idea came out body-and-physics co-op; time pressure added by hand |
| M6 systems analogy (nature, science) | 4 | **3**/1/4 | 14.4 | low content; famous structures already gamed (circuit = hand-holding chain, mimicry = Among Us) |
| M7 contradictions (TRIZ) | 4 | 1/5/2 | 13.9 | "you can X only while a friend does Y" ties players best; gives no threat; 5 of 8 limit sight/speech |
| M9 single-player graft | 4 | 1/3/4 | 13.8 | F1/F7 free; first graft is "split one avatar" or "stations", both taken |
| M1 grid (control, the old method) | 3 | 1/3/4 | 14.6 | coverage; traitor column copies social deduction; pot row gives pooled bars |
| M3 split one thing | 3 | 1/3/4 | 13.6 | coupling and blame free; goal and threat bolted on; chain shapes |

- **No idea passed strictly.** 40 of 72 pass (no ✗). Almost every passing idea lost its point on
  **F7 tail** (round-shaped arenas with no stated generation) or **N novelty** (~: shares a core).
- **The checks that sort methods are F3 and N.** F1, F2, F4 almost never failed (the generators
  self-checked against them). Hard fails were F3 (pooled steering, set-up-then-wait, one end only
  obeys) and N.
- **The old grid method came last** (with M3), the real-world method first. With 8 ideas per method
  and noisy raters, gaps of 1–2 passes are noise; M2's lead and M1/M3 at the bottom are the clear part.
- **Noise (checked):** formula raters agreed on 86% of checks over 12 shared ideas. The three novelty
  checkers differed a lot in harshness (✓/✗: 2/12, 1/9, 10/4 per 24 ideas), and two of them disagreed
  about whether "others see what you can't" ideas are taken. Treat N as noisy.
- **Attractors:** several methods produced the same idea independently: Sunbeam Relay ×2, Human
  Tower ×2, trapeze catch ×2, saboteur-who-acts-unwatched ×2, steer-the-next-body ring ×2, and the
  "you help only others, never yourself" family ×7 (Blind Spot, Light Bridge, Shade, Blind Lamps, Wet
  Paint, Unseen Keys, Borrowed Eyes; same family as Thin Ice / The Tilt). The novelty checkers tied
  that family to Hanabi; rater 1 capped its F6 at ~ (hidden by the game, nobody wants to hide it).
- **What the best ideas share (both raters, independently):** two different actions by two players
  that must meet in the same instant (release + catch, hammer swing + sliding the bar), a physical
  clock (water, cooling metal, a beat), and one culprit at the spot. Physics or one spawn rule carries
  the content.

Top gen-1 ideas (score of 18): Striking Gang 17 (M2: a holder slides a glowing bar while strikers'
hammers land 1 s after the swing starts; cold blows crack it), Log Jam 16, Tool Line 16, Balloon
Basket 16, Hump Yard 16, Salt Flat Crossing 16, Cage Eyes 16, Drop Relay 16, Passing Troupe 16,
Heavy Boots 16, Pull Tower 16.

## Gen 2 design (19:36)
Survivors: M2 (rerun, aimed at activities not yet games), M8 → M8b (less-known folk and parlour
games), M5 → M5b (less-known sources, invert two things). M4 lives on through a crossbreed.
New: **M10** random crew × material (M2 × M4: best score × most novel); **M11** meet in the instant
(built from what the best ideas shared, with random action pairs); **M12** idea crossover (children of
the 10 best gen-1 ideas). Dropped: M1, M3, M6, M7, M9.
All gen-2 generators add a Tail line and run one web search per kept idea after generating, swapping
out clear duplicates (the user's no-duplicate check, moved into the method). 6 gen-1 ideas go back in
blind as anchors, to measure rater drift between generations.

## Gen 2: 6 methods, 48 ideas + 6 anchors (19:36–20:04)

| Method | Pass of 8 | Novel ✓/~/✗ | Mean of 18 | Note |
|---|---|---|---|---|
| M11 meet in the instant (new, built from gen 1's best pattern) | **8** | **7**/1/0 | 15.0 | all 8 came out historical work crews; raters flag lag risk on most |
| M10 random crew × material (new, M2 × M4) | **8** | 3/5/0 | 14.2 | material physics carries blame and tail; heavy simulation to build |
| M8b folk & parlour translation (M8 mutated) | 7 | 0/7/1 | 14.1 | folk sources (tinikling, maypole, kho kho) cap novelty at ~ |
| M12 crossover of the 10 best gen-1 ideas (new) | 6 | 5/3/0 | 14.8 | best single idea (Bull Relay 17); 7 raw children were one parent re-skinned |
| M2b real-world activities (gen 1 winner, rerun) | 5 | 3/4/1 | 14.6 | repeated its own gen-1 ideas (Hump Yard, club passing) |
| M5b failure inversion (M5 mutated) | 4 | 2/4/2 | 14.1 | repeated its own gen-1 idea (Shove Crew, now in zero gravity) |
| Anchors (6 gen-1 ideas, re-scored blind) | 2 of 6 | 3/2/1 | 13.8 | same scores ±1 except F7 (see below) |

- **Gen 2 beat gen 1, and the raters didn't go easier.** Pass 38/48 (79%) vs 40/72 (56%); novel ✓
  20/48 (42%) vs 13/72 (18%). The 6 anchors kept 7–8 of 9 checks the same and lost 1–2 points, never
  gained. Formula raters agreed on 89% of checks over 12 shared ideas.
- **The new methods won; the reruns of gen 1's winners came last.** A method rerun repeats its own
  ideas, so it decays. What carried over was what the scores *showed* (gen 1's best pattern became
  M11; the best ideas were crossed in M12; the best two methods were crossed in M10), not the method.
- **Caveat: M11 is built from the raters' own description of a good idea**, so part of its 8/8 is
  teaching to the test. The same raters flag its weak spot: "same-instant handoffs collapse to a
  protocol" (one end acts on a call), and lag risk.
- **The novelty jump has two causes that this run can't separate:** the new methods, and the web
  search each generator ran on its kept ideas (8 swaps logged across 6 methods).
- **F7 was read more strictly in gen 2** (6 of 54 ✓ vs 20 of 72), because gen-2 ideas stated a Tail
  line and the raters were told to test it. Anchors with no Tail line dropped to F7 ✗. F7 totals are
  not comparable across generations; passes mostly are.

## What the tournament found (both generations)

1. **No idea passed every check in 126.** Almost every passing idea loses its point on **F7 tail**.
   Raters' reading, independently in both generations: physical coordination ideas settle into one
   routine ("new layout, same routine"; "generated layouts sit on a procedure the crew solves early").
   F7 ✓ came from a hidden human (saboteur, private stake), physics that the crew's own actions keep
   changing (cracks, foam, ice floes), or rules about who sees whom.
2. **Synthesis (Claude, opinion): F3 and F7 fail for the same reason.** Once the crew finds a protocol
   ("slider calls set, holder releases"; "ring rhythm, hammer on a count"), coupling turns into
   obeying the protocol and replay turns into the same routine. The user's premise, "friends are always
   unique", holds only if the rules leave friends room to differ. The ideas that came closest have a
   threat that reacts to the players themselves (Bull Relay: the bull charges the nearest player it
   can see) or a floor the players change as they act (Crack Loop Roof).
3. **Lag (not scored, assumed):** raters flagged "lag risk" ~30 times in gen 2. The best pattern of
   gen 1, two actions meeting in the same instant, needs two online inputs within ~0.2 s. An older
   critic catch already says a timed simultaneous press is mashing, not coupling (critic memory).
4. **The "help only others, never yourself" family is taken** (Hanabi; Watch My Step!). It came out of
   7 methods in gen 1 and scored N ✗ twice (Blind Spot as an anchor). This is The Tilt / Thin Ice's family.
5. **Methods converge.** Across methods: Sunbeam Relay, Human Tower, trapeze, Stone on Rollers =
   Megalith Haul, Hot Rivets = Rivet Gang. Within a method: reruns repeat themselves.
6. **The look converges too:** M2, M10 and M11 mostly gave historical work crews (forges, mills,
   rails, quarries). Fantasy and look were recorded, never scored.

## Best ideas (formula ≥ 16 of 18 and novel ✓; F7 ~ on all)

| Idea (method) | Rule | Closest existing (novelty checker) | Raters' main doubt |
|---|---|---|---|
| **Bull Relay** 17 (M12) | The bull charges the nearest player it can see, so the crew passes it from one to another by stepping out of cover just as the last one ducks behind it. | Moomoo.io bull (not close) | the pass settles into a relay plan; lag on the duck/step-out instant |
| **Striking Gang** 17 / 16 (M2, anchor) | The holder slides a glowing bar on the anvil while strikers' hammers land 1 s after the swing starts; a blow on cold metal cracks it. | Smithworks (solo) | strikers' timing can become a count |
| **Bed Board Tunnel** 16 (M12) | In a one-person-wide tunnel the only props are the boards already holding up the roof, so every board moved to a new crack leaves bare roof over somebody else. | Sub Terra (board) | same board-shuffle routine each round |
| **Ore Carts** 16 (M12) | Brakeless ore carts coast farther the more people ride them, so the crew stops each cart at its chute by jumping on and off. | Minecart mod (not close) | one rider per cart = parallel play |
| **Stone on Rollers / Megalith Haul** 16 (M11, M2b) | A huge stone slides only over logs, and each log that rolls out behind must be carried round and laid in front. | Monumental Failure (different) | runners shuttle side by side; rope crew obeys |
| **Trapper Doors** 16 (M11) | An ore cart runs through air doors, and each must be pulled open only in the instant the cart passes: early lets mine-fire smoke creep a section closer, late smashes the door. | Supermassive cart scene | keepers do the same job; lag |
| **Salt Flat Crossing** 16 (M6) | Each player is immune to one kind of storm and shelters the friends behind them, so each storm needs the right friend in front. | Elemental Fury (not close) | F3 ~ |
| **Balloon Basket** 16 (M1) | The balloon rises for every person who climbs out of the basket and sinks for every one who climbs back in. | Cloud 9 (card game, different) | F3 ~, F5 ~ at 3 |
| **Heavy Boots** 16 (M6) | In a tumbling zero-g station any player can turn heavy, anchoring themselves and pulling every light player toward them. | OMG: Oh My Gravity (not close) | F3 ~ |

Full scores: `eval/G1_summary.txt`, `eval/G2_summary.txt`, `eval/scores_G*.json`; ideas: `gen1/`, `gen2/`
(blind IDs → methods: `eval/G*_key.json`).

## If there is a gen 3 (not run; budget was 1 h)
Aim at the check that blocks everything: methods that keep the crew's routine from settling
(threats that react to what the players do, floors the players change, a stake that differs per
player without a traitor). Add a lag check to the formula before scoring. Score the 9 best ideas
above as anchors again.
