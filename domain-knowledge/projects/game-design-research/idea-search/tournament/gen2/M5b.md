# M5b: failure inversion, from less-known sources (gen 2, 2026-11-10)

## Method log

**Steps run**
1. From memory, listed 18 group activities that are not famous co-op video games (step 1 asked for 15; 3 extra came up while working). No web search during generation.
2. Named the check each one fails worst (table below).
3. Inverted each failure into a rule that passes that check. Every inversion changes two things: **who does what** and **what the shared object is**. Some sources gave two inversions.
4. Wrote 25 raw candidates and picked 8 with 8 different core rules.
5. Novelty step: one web search per kept idea, plus one per replacement (14 searches in all). Three kept ideas had an existing game with the same core rule and were swapped out.

| # | Source (kind) | Worst check | Why it fails |
|---|---|---|---|
| 1 | Tug of war (PE) | F3 | everyone adds to one rope: a pooled sum |
| 2 | Rainbow parachute (PE) | F4 | the ball rolls off and nobody did it; also pooled |
| 3 | Blindfold minefield walk (team-building) | F3 | the caller directs (quarterback), the walker only obeys |
| 4 | Human knot (team-building) | G | no time pressure, you can't really lose |
| 5 | Close-order drill (military) | F3 | one commander, everyone else obeys |
| 6 | Bucket brigade (fire drill) | F3 | everyone does the same job in a line |
| 7 | Club passing (circus) | F5 | each pattern is built for a fixed number of people |
| 8 | Human pyramid (circus, cheer) | F3 | the base sets up once and then just holds |
| 9 | Fort Boyard cell round (game show) | F5 | one person plays, the rest only shout |
| 10 | Asteroids 2-player, taking turns (arcade) | F5 | half the time your seat is idle |
| 11 | Relay race (PE) | F5 | you wait for the baton |
| 12 | Rowing eight with a cox (sport) | F3 | a pooled stroke plus a quarterback cox |
| 13 | Double Dutch (playground) | F3 | the turners only keep the beat |
| 14 | Telephone (party) | F4 | you can't see who garbled the message |
| 15 | Handbell choir (school music) | F3 | the conductor directs; the score is hand-made (F7) |
| 16 | Volleyball keep-up drill (PE) | F3 | everyone does the same bump |
| 17 | Pit-crew drill (motorsport) | F7 | every stop is the same script |
| 18 | Teeterboard (circus) | F7 | a fixed routine for a fixed troupe |
| + | Three-legged race, river-crossing "stepping stones", raising a tent pole on guy ropes (scouts), Hole in the Wall (game show), helium stick, Simon says | various | used for extra raw candidates |

**Raw count:** 25.

**Checks the raw candidates failed most (my estimate, before scoring)**
- **N (6 raw):** the real-world source often already *is* the game. R8 is the team-building "Chaotic Juggling Machine", R14 is plain long-rope skipping, and R20 is the river-crossing exercise. R19, R7 and R9 have video-game twins (see swaps).
- **F3 (5 raw):** pooled sums leaked back in (R11, R13, R21), along with "same job side by side" (R15) and obey-only (R25).
- **F7 (4 raw):** puzzle or routine shapes become a lookup table (R10, R16, R22, and partly R5).

**Swaps after the novelty search**
- **Kept R19 (seesaw ladder) → swapped for R3.** *The Seesaw Redemption* (game jam) has the same core: two dwarves take turns jumping on a seesaw to climb out of a mine as lava rises. The arcade game *Circus* (1977) also has clowns launching each other on a seesaw.
- **Kept R7 (cargo holder sinks into ice) → swapped for R2.** In *Don't Drop It* (Steam, 2-player online co-op) whoever holds the core can't jump, so it has to be thrown back and forth. Same core rule: holding the object handicaps you, so it keeps being passed.
- **Kept R8 (more balls in the air than players) → swapped for R23.** The team-building game *Chaotic Juggling Machine* has the same core: each person may hold one ball, and balls are added up to "players minus one".
- **Searched and rejected as replacements:**
  - R4 (you see traps only around the next player): *Watch My Step!* (each player sees different traps) and *Fly You Fools* are too close.
  - R9 (stacked players): *Two Kids Stacked In A Trench Coat* (bottom walks, top balances).
  - R14 (rope caravan): it is ordinary long-rope or "Zero 1, 2, 3" skipping.
- **Kept, but flagged as N ~:**
  - M5b-5 (R10): the separated-rooms puzzle genre (*We Were Here*), plus the *Windows EXP* prototype, where a lever in one game opens a door in another. The "opens one, shuts another" ring was not found.
  - M5b-7 (R24): chain-tethered co-op exists (*Chained Together*, *Chained Up Together*). The "step only while your neighbours stand still" rule was not found.
  - M5b-2 (R2): *Tangled Together* has reeling, but both players walk; *Mountain Climbers* has launching. "You never climb yourself" was not found.

**What the method was good and bad at**
- **Good at F3 and F4.** The real-world sources are physical, so the inversions came out as body-to-body physics. Every action has a visible arc, which makes the blame visible, and the "two things change" rule removed the pooled rope and the conductor.
- **Good at F1.** Almost every idea runs on one physics rule plus a generated layout.
- **Bad at N.** Group games from the real world are already games, and video-game makers have mined circus acts and party games. 3 of the first 8 picks had twins, the worst being the juggling one, whose source practically *was* the idea.
- **Bad at family spread.** The picks cluster in "ropes and bodies" (R2, R5, R23, R24) and "send a friend upward" (R2, R3, R23).
- **F7 depends on physics and generated layouts more than on the players.** Only M5b-1 and M5b-4 draw much of their round-to-round difference from what the players did last.
- **F6 is mostly n/a.** The sources almost never hide anything.

**Sources (novelty searches, 2026-11-10)**
- The Seesaw Redemption: https://msbasilisk.itch.io/the-seesaw-redemption
- Don't Drop It (Steam app 5128000 / 4872470 in search results): https://store.steampowered.com/app/5128000
- Chaotic Juggling Machine: https://www.salto-youth.net/tools/toolbox/tool/the-chaotic-juggling-machine.3172/
- Give Us Back Gravity / Heavenly Bodies / OMG Oh My Gravity (zero-g search, no push-off-teammate rule): https://store.steampowered.com/app/5380530/ , https://destructoid.com/?p=296110 , https://www.playnews.gg/en/games/omg-oh-my-gravity
- Tangled Together: https://co-openly-studio.itch.io/tangled-together ; Mountain Climbers: https://josiro98.itch.io/mountain-climbers
- Watch My Step! (Steam 5087540): https://store.steampowered.com/app/5087540 ; Fly You Fools: https://stamen9.itch.io/fly-you-fools
- Two Kids Stacked In A Trench Coat: https://stacked.itch.io/twokidsinatrenchcoat
- Long rope / Zero 1, 2, 3: https://playworks.org/game-library/zero-1-2-3
- We Were Here: https://pcgamer.com/we-were-here-too-is-a-co-op-escape-game-that-aims-to-keeps-the-players-apart ; Windows EXP: https://benisaperson.itch.io/windows-exp
- Chained Together family: https://www.nintendo.com/us/store/products/chained-up-together-switch/
- Vikings on Trampolines (trampoline search, no "player is the ball" rule): https://www.co-op.gg/pc/game/vikings-on-trampolines
- Pole climb (team-building "High All Aboard", belay, not guy ropes): https://branchingoutadventures.cinolla.com/branchingoutadventures/course/high-all-aboardleap-of-faith

## Raw candidates

Format: id. name (source → inversion: who / object) — core rule.

- **R1.** Shove Crew (tug of war → everyone is anchor and mover / bodies instead of a rope): in zero-g you can only move by shoving a crewmate, and you both drift apart.
- **R2.** Fling Rope (tug of war → the anchor works, the flyer picks the hold / a rope web instead of one rope): you never climb yourself; an anchored friend reels you so hard you fly past them, and you grab a hold at the top of the flight.
- **R3.** Jump Sheet (parachute + keep-up → one friend is the ball, the others are separate sheets / a person instead of a ball): one player flies and only steers in the air; the others run under them with small jump sheets and tilt to send them on.
- **R4.** Ring Sight (minefield walk → everyone walks and everyone watches / a sight ring instead of one guide): you see the traps only around the next player in the ring, never around yourself.
- **R5.** Braid Gang (human knot → tie instead of untie, under a clock / strands instead of arms): each player trails one strand, and crossing over or under a friend braids them; match the called braid before the load snaps.
- **R6.** Ring Remote (close-order drill → everyone commands one other / the controls instead of the formation): your stick moves the next player in the ring, never you, and you see only through your own eyes.
- **R7.** Sinking Courier (bucket brigade → the holder sinks, runners scout / ice floes instead of a line): whoever holds the cargo sinks, so it must keep being thrown to a friend on fresh ice.
- **R8.** Crowded Air (club passing → open patterns / a ball count instead of a pattern): always one more ball in the air than players, nobody holds two.
- **R9.** Totem Walker (human pyramid → the base decides / a body stack as the vehicle): the bottom player walks, the top player grabs, the middle players lean to balance.
- **R10.** Flood Cells (Fort Boyard cell → everyone locked in at once / a wiring ring instead of one cell): each lever opens one friend's door and shuts another's, and the wiring is unknown.
- **R11.** Shield Ring (Asteroids turns → everyone at once / bodies as the shield): players orbit one core and are its only shield.
- **R12.** Lantern Relay (relay race → no waiting / light as the baton): only lit ground is solid, and the lantern holder can't jump.
- **R13.** Backward Rowers (rowing eight → no cox / a spinning raft): each sees only the way they face and paddles their own side.
- **R14.** Rope Caravan (Double Dutch → jumpers set the pace / a moving rope): two walk a turning rope across a field while the others jump it carrying cargo.
- **R15.** Echo Line (telephone → visible links / a pose instead of words): each copies the pose of the previous player with a delay.
- **R16.** Bell Field (handbell choir → no conductor / bells scattered on a map): a generated tune; only the last ringer can point at who rings next.
- **R17.** Human Keep-up (volleyball drill → the ball is a player): merged into R3.
- **R18.** Rolling Repair (pit crew → repairs while driving / a cart that sheds parts): one holds the part, one bolts it, while the cart drives.
- **R19.** Seesaw Ladder (teeterboard → open climbing / a tower of seesaws): you gain height only when a friend lands on the other end, and the lander stays low.
- **R20.** Touch or Sink (stepping stones → the front player throws stones / drifting stones): any stone nobody touches sinks.
- **R21.** Plank Bearers (helium stick → each hand shown / a long plank): carry a plank level over bumps.
- **R22.** Gate Makers (Hole in the Wall → the bodies are the hole): half the crew forms a gap that a rolling boulder must pass through.
- **R23.** Guy-Rope Mast (tent-pole raising → one climbs, the rest only pull / a mast instead of a tent): a climber's moves tip a mast that stands only on ropes the others pull; ropes pull, never push.
- **R24.** Ankle Chain (three-legged race → the whole crew in a line / a stepping rhythm instead of a pair): each ankle is tied to its neighbours', and you can only step while your neighbours stand still.
- **R25.** Ring Simon (Simon says → each person orders one other): each gives orders to one and obeys another.

## Kept ideas

### M5b-1 Shove Crew
- **Rule (one sentence):** In zero gravity the only way to move is to shove a crewmate, which sends you both drifting apart in opposite directions.
- **Hub (the one shared thing everyone uses):** the crew's own bodies and their momentum: one push rule where a heavier body drifts slower. Extra rule 1: hull rails let you grab and stop, but never push off. Extra rule 2: a patch plate you carry makes you heavier.
- **Coupling (how my best move depends on what a friend just did; who does which different action):**
  - To reach a leak I need a friend on the far side of me, and my shove decides where *they* end up.
  - They line themselves up before the shove so their drift lands on a rail or a third player. Either of you can trigger it, and both of you set the line by where you float.
  - The friend I just sent away is now the only anchor someone else can use.
- **Fantasy:** a salvage crew with no jetpacks on a leaking, tumbling station.
- **Look:** chunky suits drifting through a slowly turning wreck, with air hissing from glowing cracks.
- **At 3 / at 6:**
  - At 3, every shove leaves exactly one possible catcher, so it is tight and new players can lose.
  - At 6, relay catches (catch, then shove onward) cross the wreck fast, but more bodies drift off.
  - A lone drifter can throw a plate away to recoil, at the cost of the plate, so nobody gets stuck.
- **Hidden:** none.
- **A failed run:** Mia shoves Tom toward the last leak at the wrong angle. Tom sails out of the open bay with the final plate. Everyone watched his drift line leave from Mia's push.
- **Tail:** the wreck tumbles and leaks open at random spots. Each crossing starts from wherever the last shoves scattered the crew, so the positions are the players' own mess.

### M5b-2 Fling Rope
- **Rule (one sentence):** Nobody can climb on their own; an anchored friend reels you in so hard that you fly up past them, and you must grab a hold at the top of your flight.
- **Hub:** the ropes between players, a single physics rule: a fast reel flings, a slow reel drags. Extra rule: a used hold crumbles a few seconds after you let go.
- **Coupling:**
  - The anchor picks reel speed and timing.
  - The flyer picks the lean and which hold to grab, and shouts which hold they want.
  - Once they grab, the flyer becomes the anchor for the next person. The anchor's flight is already wasted if the flyer is late.
  - Each player is roped to two others, so who can fling whom changes as the crew climbs.
- **Fantasy:** a mountain rescue team climbing a collapsing cliff before the tide comes in.
- **Look:** bright ropes zig-zagging up a dark, crumbling sea cliff.
- **At 3 / at 6:**
  - At 3 it is a chain of three: every fling uses one of only two ropes.
  - At 6 the ropes form a web, giving more routes, but tangles block flings.
- **Hidden:** none.
- **A failed run:** Ana reels too hard and Leo overshoots into an overhang, falls, and drags the chain down. His flight arc showed Ana's reel speed.
- **Tail:** the wall is generated from rock chunks, holds crumble after use, and the order of the rope web changes every run.
- **Novelty:** ~. *Tangled Together* has reeling but both players walk; *Mountain Climbers* has launching.

### M5b-3 Jump Sheet
- **Rule (one sentence):** One player is the "ball" and can only steer in the air, while each other player runs with a small jump sheet and tilts it on the catch to send the ball to the next catcher.
- **Hub:** the flying player, one physics body. Extra rule: a tilt locks onto one named catcher and shows an arrow.
- **Coupling:**
  - Where the ball goes depends on the catcher's tilt *and* the ball's mid-air steering. The flyer shouts what they want to grab.
  - The named next catcher has to already be running.
  - The flyer can hand the ball role to the catcher at any landing, which changes who runs.
- **Fantasy:** firefighters bouncing one brave friend up a burning tower block to pull people out of high windows.
- **Look:** a yellow-coated crew darting about the street with round sheets, under a big burning facade.
- **At 3 / at 6:**
  - At 3: one flyer and two catchers, so every catch is followed by a long sprint.
  - At 6: two flyers in the air at once (crew ÷ 3), so the catchers split up and the two arrows can cross.
- **Hidden:** none.
- **A failed run:** Jo tilts to send Sam to Kim, but Kim is under the other flyer, and Sam hits the pavement at the end of Jo's arrow. The arrow showed whose call it was.
- **Tail:** windows light up at random, bounces are physics, and at 6 two bodies share one street, so each run's paths come from the crew.

### M5b-4 Braid Gang
- **Rule (one sentence):** Each player trails one strand from a shared anchor, and crossing over or under a friend braids the strands, so the crew must walk the braid that is called before the hanging load snaps it.
- **Hub:** the braid, the strands' crossings counted left to right. Extra rule: a strand that crosses the same friend twice in a row knots, and a knot is a weak spot.
- **Coupling:**
  - Every crossing takes two people at the same moment: one jumps over and the other ducks under, and they decide on the spot who does which.
  - My next crossing depends on where the last crossing left me in the row.
- **Fantasy:** riggers braiding a rescue rope live while a crate of people swings over a gorge.
- **Look:** each player in their own strand colour, with the braid growing behind them like a ribbon.
- **At 3 / at 6:** at 3 a plain plait with one crossing at a time; at 6 a six-strand braid with two or three crossings at once.
- **Hidden:** none.
- **A failed run:** Rui ducks when he should have jumped, the strands knot at his crossing, and the load tears the rope at that red spot.
- **Tail:** braid patterns are generated, so there is no hand-made list. Weak point: a practised crew may learn the dance, so F7 is ~.
- **Novelty:** no braid-by-walking game found.

### M5b-5 Flood Cells
- **Rule (one sentence):** Each player is locked in a flooding cell whose door opens only from a lever in some friend's cell, and every lever pull opens one door and shuts another.
- **Hub:** the wiring ring of levers and doors, regenerated each round. Extra rule: water rises faster in a cell whose door has just been shut.
- **Coupling:**
  - My pull frees one friend and dooms another, so I must hear first whose water is highest.
  - Everyone pulls and everyone gets hit by someone else's pull. Nobody sees the whole wiring, so there is no quarterback.
- **Fantasy:** a crew trapped in the compartments of a sinking ship.
- **Look:** one small lit room per player, with water lines shown on a shared hull cutaway.
- **At 3 / at 6:** at 3 a ring of 3 cells; at 6 the ring has short-cut wires (one lever reaches two doors).
- **Hidden:** the wiring. You uncover it by pulling and asking "whose door moved?". Nobody hides it on purpose, so F6 is ~.
- **A failed run:** Eva pulls while Ian's water is at the ceiling; her lever shuts his door and he drowns. The pull is marked with her name.
- **Tail:** the wiring is generated and the order of pulls is the players' own, but a systematic crew can solve it, so F7 is ~.
- **Novelty:** ~. The *We Were Here* genre and the *Windows EXP* lever-to-door prototype are close.

### M5b-6 Ring Remote
- **Rule (one sentence):** Your controls move the next player in the ring, never yourself, and you see only through your own eyes.
- **Hub:** the control ring (who drives whom), shuffled when someone dies. Extra rule: an obstacle course built from a short list of trap types.
- **Coupling:**
  - I steer Bo from Bo's spoken description of what Bo sees, while Ann steers me from mine. Everyone talks and drives at once.
  - My best move depends on what the player steering me just did to me, because it changes what I can report to the one I'm steering.
- **Fantasy:** a cursed crew whose bodies got swapped around a circle, trying to get out of a trap-filled temple.
- **Look:** each player has a coloured thread from their hands to the body they drive.
- **At 3 / at 6:** at 3 a ring of 3, odd sizes fine; at 6 a ring of 6, with longer delays in what gets passed on.
- **Hidden:** what the player you steer can see. You uncover it by asking them. Nobody hides it on purpose, so F6 is ~.
- **A failed run:** Kai walks Mo into a spike pit, and Mo's thread runs straight to Kai.
- **Tail:** the course is generated from the short list of traps, and the ring reshuffles after each death, so the order is always new.
- **Novelty:** no ring-swap control game found.

### M5b-7 Ankle Chain
- **Rule (one sentence):** Every player's ankles are tied to their neighbours' in one line, and you can only take a step while both your neighbours are standing still.
- **Hub:** the line of ties. Extra rule: stepping while a neighbour is mid-step trips you both.
- **Coupling:**
  - My step waits on my neighbours, and theirs waits on me, so the line has to call a rhythm.
  - The two ends steer, and the middle carries the pace.
  - The terrain forces breaks in the rhythm: one person must hop a gap while the others freeze.
- **Fantasy:** a chain gang escaping over a collapsing rope bridge.
- **Look:** a little shuffling line of prisoners in stripes on swaying planks.
- **At 3 / at 6:** at 3 one middle player and two ends; at 6 four middles, so the rhythm takes longer to pass down the line.
- **Hidden:** none.
- **A failed run:** Liv steps while Ola is mid-hop, and both go off the bridge. The trip flashes on Liv.
- **Tail:** generated bridges and planks, physics sway, and a different order in the line each run.
- **Novelty:** ~. *Chained Together* and similar tethered games exist; the step-only-while-neighbours-are-still rule was not found.

### M5b-8 Guy-Rope Mast
- **Rule (one sentence):** One player climbs a tall mast that stands only because the others hold its guy ropes, and ropes can only pull, so each lean of the climber must be caught by whoever holds the rope on the opposite side.
- **Hub:** the mast, a single physics body. Extra rule: wind gusts from a random side.
- **Coupling:**
  - The climber picks which way to reach; only the holder opposite that lean can save the mast.
  - Pulling the wrong rope tips it.
  - Holders call gusts they feel and the climber calls reaches, so both ends decide.
  - At the top the climber hangs a lantern and slides down, and a holder swaps in.
- **Fantasy:** shipwrecked sailors raising a signal mast on a rock in a storm.
- **Look:** a thin mast whipping in the rain with taut ropes fanned out to the crew.
- **At 3 / at 6:**
  - At 3: two holders run between four rope pegs.
  - At 6: two climbers at once (one high, one low) and four holders.
- **Hidden:** none.
- **A failed run:** Tim pulls into a lean instead of against it and the mast cracks. His rope was the one that went taut.
- **Tail:** wind gusts and the climber's route change every run. Weak point: the holders' job leans toward parallel pulling, so F3 is ~ and F7 is ~.
- **Novelty:** no guy-rope climbing game found (the closest is a team-building pole climb on belay ropes).
