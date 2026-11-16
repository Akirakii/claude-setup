# Game 1 v3: replacing The Switchboard

User verdict (2026-11-08, after the stage and text fixes): "the lever game still doesnt make
sense", "i still dont undersatnd". Asked what: all four of "what to do at all", "reading names",
"my own lever", "playing with bots". Direction (user): **replace it**. Game 3 was "Switchboard +
TOGETHER", so it is replaced too.

## Constraints (the user's words first)
- Understandable at once: the goal and the first thing to do clear in seconds; one sentence. (user)
- Works in practice with bots (the user's usual test is 1 human + 2 bots): the human's actions must
  visibly connect to the bots' (bots can't hear voice). (user: "playing with bots")
- Cooperation: v1 verdict "too simple and easy and requires no cooperation at all" (user). The
  co-op gate, design-anti-patterns C: 1 coupled, 2 split by position, 3 talk, 4 blame, 5 not
  easy, 6 not solo-able, 7 two-way; lone survivor; dying never helps.
- Brutal deaths with lots of blood (user). The dead join the crowd and move around outside the
  play area, keeping a role (user + synthesis in minigames-v2).
- The one 24 m stage of 2 m tiles that drop, rise and tilt, with the LED floor (user: one stage
  that transforms). 3–6 players (user).
- Different from game 2, The Tilt (split sight + balance).
- Taught by the presentation-v3 pattern: lines with matching shots, a rehearsal in game 1.

## Three theses (different verbs)
**A. Bomb Relay** (verb: throw and catch). "Pass the bomb to the furnace. You can't walk while you
hold it." Bombs drop from a chute at one end of the stage; the Reaper's furnace is at the other end
(20 m, farther than any throw). Holding a bomb you can turn and aim but not walk; after HOLD s in
your hands it blows. Throw (E) along your aim, range THROW_R; a living player within CATCH_R of
its path, facing it, catches it. A bomb on the floor rolls, then blows (BLAST_R). Tiles drop in
patterns announced by the LED floor, so the chain keeps re-forming. Deliver Q bombs in T s.
**B. The Coffin** (verb: carry together). "Carry the coffins to the grave together." A coffin needs
2+ hands; it moves by the sum of its carriers' pulls (both ends steer at once, like a couch carry,
from memory: Moving Out); the front sees the path, the back walks backwards. Holes open; drop it
in a hole and the carriers go with it.
**C. Simon Floor** (verb: remember and step). "Step on the lit tiles in order." The LED floor
flashes a colour-coded sequence; each player's colour is theirs to step on, in order across the
crew; a wrong tile drops you.

**Pick (Claude): A, Bomb Relay.**
- Readable at once: a bomb, a fuse, a furnace.
- With bots: they wave to catch and they throw back, so it stays physical and works without voice.
- The bombs give brutal deaths for free.
- It shares no verb with The Tilt.
- B is the strong alternative: a proven two-way carry, but bots on the other end feel like a tug,
  and at 6 it splits into pairs.
- C is solo-able by one good memory, and its two-way part is weak.

## A in numbers (to attack; Claude)
| Name | Value | Why |
|---|---|---|
| Path | chute at x = +10, furnace at x = -10 (the deck side) | longer than any throw |
| HOLD | 3 s in your hands, then it blows | no camping; forces passing |
| THROW_R | 6 m (flat arc, 0.8 s flight) | 20 m path = at least 4 throws |
| CATCH_R | 1.0 m from the path, facing it within 60° | the catcher picks spot and facing (two-way) |
| Floor bomb | rolls 1.5 s, then blows; BLAST_R 2.5 m | a miss kills nearby; blame the thrower |
| Quota Q | 2N + 2 bombs in T = 80 s | scales with hands |
| In flight | 1 bomb at N ≤ 4, 2 bombs at N ≥ 5 | 6 players must split into 2 chains |
| Tile drops | every 12 s the LED floor flashes a pattern 2 s ahead, then those tiles drop for 6 s | breaks a static bucket brigade |
- Blame: a blast names the last thrower (miss) or the holder (held too long).
- The dead (in the crowd): they can't hold bombs; they shout warnings. Being outside, they see
  the next drop pattern 4 s ahead instead of 2 s, so they get a real job calling it.
- Lone survivor: can carry the bomb by throwing it ahead of themselves and catching it on the run
  (a catch needs another player; alone, you may catch your own throw). Slow, near-impossible
  (dying never helps).
- Bots: a chain planner. Each bot takes the spot one THROW_R toward the furnace from the holder,
  faces the holder, raises its arms (visible "ready"), and throws to the teammate nearest the
  furnace that is within range.
- Teaching: 1 a bomb drops from the chute: "Bombs!" / 2 "Hold one and you can't move." / 3 "Throw
  it to a friend before it blows." / 4 the furnace roars: "Feed the furnace: %d bombs!" Rehearsal:
  one bomb with a long fuse, no deaths.
- Game 3: Bomb Relay II: bombs come from two chutes at once and the furnace moves along the back
  edge.

## Round 1: critic -> synthesis
Critic: A is the right one of the three (B fails the 1 human + 2 bots test: a tug against bots;
C is solo-able), but A as written is a static bucket brigade.
| Critic finding | Synthesis |
|---|---|
| SEVERE: fixed chute and furnace = a static line at N=4 (holder spots +10/+4/-2/-8), silent conveyor at N=6; tile drops are a hazard, not a coupling (0.4 s sidestep) | **Both ends move.** Each bomb lands on a random spot in the far half (x +3..+10), lit 1 s ahead on the LED floor. **The furnace is a 2×2 hole in the stage with fire below** (the stage drops those tiles) that slides along the deck-side edge (x ≈ -10, 1 m/s, turning at random); throw it in. Every bomb needs a new route. Tile-drop patterns are cut |
| SEVERE: two-way fails: the catcher just stands in a cone | **Hands up to catch:** hold E with empty hands = arms up, and you can't walk while they're up. A bomb that reaches raised hands is caught; one that hits you without them drops and blows. Judged on the catcher's client, with a wide window (#16). Both ends commit: the thrower picks moment and aim, the catcher picks spot, facing and when to stop |
| SEVERE: alone you chase your own throws at sprint speed (bomb 7.5 m/s = SPRINT): dying helps | No self-catch. Alone you may walk with the bomb at 1.5 m/s with its fuse paused (~13 s per bomb vs ~8–10 s for two) |
| HOLD 3 s never binds; a per-hand fuse contradicts "a bomb, a fuse" | **One fuse per bomb**, lit when it lands, shown on the bomb (F = 14 s; tune by sim) |
| Pickup undefined; an unattended bomb deadlocks the bots | Pick up: hold E on it. The fuse runs from landing, so an untouched bomb blows on its spot |
| 1 human + 2 bots: bots do 3 of 4 throws and nearly clear alone | Bots take distinct spots, leave the pickup and the furnace throw to a nearer human, react after 0.4 s, and raise their hands only when someone aims at them |
| The dead's job is decorative | The living see the next landing spot 1 s ahead; **the dead see it 3 s ahead, and where the furnace will turn** (a marker only ghosts see), so they are the callers |
| A miss blames the thrower even if the catcher dodged | Blame whoever left the aim line in the last 0.5 s |
| Feasibility: client-side movement, bomb lag, toggle_use on E | The host snaps a holder who moves; the bomb is interpolated; throwing ignores toggle_use |
| Long-fuse rehearsal teaches a calm game | Rehearsal: real fuse, no deaths |
| Uneven scale (N=4 easiest) | Random ends make it N-agnostic; recompute by sim before tuning: Q, F, 2 bombs at N ≥ 5 |

### The rules after round 1 (what a player must know)
1. Bombs land on lit spots. Hold E on one to pick it up.
2. Holding a bomb you can't walk: aim and press E to throw.
3. Catch: hold E (hands up) as it reaches you.
4. Throw it into the furnace (the fire hole on the far side, moving) before its fuse ends.
Misses and blown fuses explode (BLAST_R 2.5 m). Deliver Q bombs in T s.
Lines: "Bombs!" / "Holding one, you can't walk." / "Hands up to catch!" / "Into the fire, before it
blows: %d bombs!"

## Round 2: critic -> synthesis
| Critic finding | Synthesis |
|---|---|
| Rules stacked again (4 rules + 5 riders; E does 3 things; hands-up adds no decision once in place) | **3 rules.** Pickup merges into hands-up. The moving fire goes to game 3. The lone-survivor exception becomes "holding a bomb you shuffle at 0.8 m/s" for everyone. A thrown bomb flies at 10 m/s (faster than sprint 7.5), so you can't run under your own throw: no self-catch rule needed. A thrown bomb that hits the floor blows at once |
| SEVERE: the dead only have a voice (fails with bots, like the Switchboard) | **Ghost spotlight:** a dead player's look casts a crowd spotlight onto the stage that everyone sees. The dead see the next landing spot 3 s ahead (the living: the LED ring 1 s ahead) and point their light at it. Bots, living or dead, use it: dead bots point at the next spot, living bots walk to a lit spot. Prerequisite: the dead-in-the-crowd zone |
| Gate 5 fails (nothing ramps); next-bomb timing undefined | The next bomb lands 2 s after the last one is gone. The fuse shrinks 14 → 9 s as the quota fills. Q in 80 s: 6/8/9/11 at N = 3..6; a second bomb in flight only at N = 6. Simulate before tuning |
| Path is 13–29 m (z counts), so "N-agnostic" is false | Accepted; the sim tunes Q per N |
| 1 human + 2 bots: the human throws once and watches | Bots route every chain through the human's raised hands, take the pickup only when the human is mid-stage, and throw only at raised hands |
| N=6: one miss kills 2–3 bunched players | A blast kills the nearest one; others within 2.5 m are knocked down 1 s and splattered |
| Moving 2×2 hole: 2 m hops, bounces off rising tiles, falls without warning | **A fixed fire** at x -12..-8, z 0, in front of the Reaper's deck ("the Reaper's fire"). Landing judged against the hole at release, with 0.8 s grace |
| "Far side" is wrong; the drones see backs | "The Reaper's fire"; play is filmed from the deck end |
| Rehearsal ticks | "caught one" and "fed the fire" per player |
| Feasibility | Bombs as scripted arcs from a release event + the shared clock (like the hazards); "can't walk" through a course hook in player.gd (like the slide), host snap only as backup |
| Game 3 | **Bomb Relay II: "The fire moves!"** (LED floor telegraphs each move; ghost spotlights show where next) |

### The rules after round 2
1. **Hands up** (hold E) to catch a bomb: from the sky or from a friend.
2. **Holding a bomb you can barely move.** Aim and press E to throw.
3. **Throw it into the Reaper's fire before its fuse ends.**
Misses blow up. The dead in the crowd point a spotlight at where the next bomb will land.
Lines: "Bombs!" / "Hands up to catch!" / "Holding one, you can barely move: throw it on!" /
"Into the Reaper's fire before it blows: %d bombs!"

## Round 3 (last): critic -> synthesis
Critic: understood in seconds; gates 1, 4, 6, 7 and the lone survivor pass; dominant strategy is a
"spoke" (one feeder by the fire, one relay mid-stage, the nearest takes the ring), calm and silent.
| Critic finding | Synthesis |
|---|---|
| SEVERE: one bomb at a time = a calm conveyor (gates 3 talk, 5 not easy weak); the test human only catches-turns-throws, v1's "too simple" again | **Bomb clock:** a bomb lands every K s whether or not the last is gone (overlap allowed); K shrinks as the quota fills; K and Q per N from a sim. Replaces "2 s after the last" and "2nd bomb only at N=6". Bots rotate roles: after the human relays, the next pickup is theirs; the human gets feeds too. No new rule to teach |
| An uncaught sky bomb: undefined | It lands on its ring and sits; its fuse runs from release at the chute. Rule 1: "grab one off its ring or from a friend" |
| The fuse doesn't bind (shuffle 0.8 × 14 s = 11 m, half the path) | Fuse tuned by sim so a 3-throw chain uses ≥ 60% of it (around 7 → 5 s); shuffle 0.5 m/s |
| Game 3's moving fire brings back the rejected moving hole | Game 3: **three fixed pits** along the deck edge; the fire burns in one at a time and jumps every ~10 s, lit 2 s ahead. Pits never move |
| Bots throw only at the human's raised hands: a human who doesn't raise them gets the bot blown up | A bot faces the human and pumps the bomb for 1 s; no hands up, it throws to the other bot |
| The spotlight needs the crowd zone (not built: ghosts still over the stage; dead in-process bots don't move) | Build the crowd zone first; the host places and steers dead bots |
| A 6 m throw from close overshoots the fire | A throw whose path crosses the pit counts |
| Lines never show the ring, the spare, the fresh press of E | Line 1's shot shows a bomb landing on its ring; ON AIR says "First blast is on me" |
The one severe finding is fixed here; no fourth critic round (max 3). Numbers (K, Q, fuse) are
set by a sim (like `tools/switchboard_check.py`) before the build, then by the playtest.

## The sketch for the user
**Bomb Relay** (games 1 and 3), one sentence: *catch the bombs and throw them on into the
Reaper's fire before they blow.*
1. **Hands up** (hold E) to grab a bomb: off its lit ring, or out of the air from a friend.
2. **Holding one you can barely move** (0.5 m/s): aim and press E to throw it (6 m).
3. **Into the Reaper's fire** (a pit in front of his deck) before its fuse ends. A new bomb
   falls every few seconds, faster as you score. Misses blow up (the nearest dies, others knocked down).
The dead in the crowd point a spotlight at where the next bomb will land (they see it sooner).
Bots: raise hands, pump the bomb at you, rotate roles, follow ghost spotlights.
Game 3: the fire jumps between three pits.
Lines: "BOMB RELAY! %d bombs to survive." / "Bombs fall from the sky. Hands up to grab one!" /
"Holding one, you can barely move. Throw it on!" / "Feed them to my fire before they blow!"
