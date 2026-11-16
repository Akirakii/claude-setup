# Minigames v2

User verdict on v1 (playtest, 2026-11-08): "too simple and easy and requires no cooperation at all".
Gate: the co-op gate in `~/.claude/design-anti-patterns.md` C (7 points, incl. 7 two-way).

## Round 1 (thesis -> critic -> synthesis)
Thesis: A Blind Floor (one spotter in a booth sees fake tiles), B Tilt (counterweight for one
grabber), level 3 = A+B. Critic: A = quarterback machine, a 2-player game with spectators, safe
seat; B's counterweight is v1's plate again; both soft-lock with a lone survivor; A+B stacks rules
and breaks blame; C Switchboard (Spaceteam) is the only two-way candidate. Synthesis: A cut, B
reframed (everyone grabs at once), C promoted, level 3 = one new rule on the stronger game.

## Round 2 (thesis -> critic -> synthesis)
Thesis: Switchboard (shout your order, someone else pulls), reframed Tilt (one key per player at
once), level 3 = Switchboard with half the stage dropping. Critic: Switchboard = phone tree by run 3
(big numbers, everyone camps a lever), too easy (12 orders in ~32 s of 75), timeout blames the
shouter (luck culprit), dropped lever tiles soft-lock; Tilt = random keys rarely oppose so it
collapses to one grabber + counterweights (gate 7 fails) and no split (gate 2: a quarterback can
direct), the slide feeds itself (faster than walking above 28°), lone survivor near-locked;
level 3 adds a hazard, not a coupling. Synthesis below.

## Round 3 (thesis -> critic -> synthesis): the sketch for the user
Critic r3: Switchboard frame holds, but levers 16 m apart beat the timer (S1); Tilt leaks through
the odd third player (counterweight again), the beacon trick (viewer walks to the key), and dying
on purpose (fewer keys); TOGETHER orders soft-lock at 2 alive and are a lag race. All fixed below.
Remaining risks are for the playtest (bottom).

### The stage and the show flow (user, 2026-11-08)
A **panel-show set** (user: "like a Panel Game Shows", "the host should look to the public", "some
wall behind the host and the participants", "a big screen"). Facing the audience bank (+x):
- **Back wall** upstage: a **big screen** (16 × 7 m) with a live feed of the stage, a text strip
  under it (game title, then live status, a dead contestant's name), the neon logo, two entrance
  arches.
- **Host desk on one side** (user: "host one side and the other side the participants"): the
  Reaper behind it on a riser in the upstage corner, facing the audience, turned toward the crew.
  It sits outside every game's play area, so he presides during play too.
- **One crew desk on the other side** (user: "they are cooperating, do not split them"):
  contestants stand behind it on marks, facing the audience.
- 24 × 24 m stage of 2 m tiles over the spike pit, crimson/gold home pattern.
**Show opening, game 1 only** (user: "a longer introduction to appreciate the default stage"):
a drone sweeps in over the audience, the big screen and logo, the panel wide, then a drone visits
each contestant as the host calls their name (name on the screen strip): ~17 s at 3, ~24 s at 6.
**Each game** (user: "while he explains the game the stage transforms"): close-up on the host,
then the audience's wide view of the panel (about 5 s), then each further line he says transforms
the stage one step on a wide shot (desks sink; Switchboard: levers rise, trapdoors light; Tilt:
floor falls to the slab, landmarks rise). Play starts from a balanced row mid-stage. After the
game the props sink and the home stage comes back. Lines kept short (user: "50% less text"),
in teaching order (what it is, your part, how to win), 50% slower for reading (one line every
3.2 s), plus a **rules card** shown after he has finished talking (user: "I don't understand the first game"). After the explanation the show **waits for
the host** ("Press E when everyone's ready"; user: "a confirmation from the host").
**Two camera drones** (user): they fly the intro shots (A: host close-up; B: the audience's wide
of the panel; then wides of the transformation); the TV view and the big screen show the live
drone. During play each drone follows a random living player or circles the stage (switching
every 7 s) and the big screen cuts between them every 5 s, from the seed and shared clock so all
peers see the same.
Layout from a studio guide's five zones (contestants, host mark at the hinge, board, audience bank
opposite, cameras on the audience side: lacastlestudios.com game-show stage design guide); panel
details from general knowledge, not verified. (Claude: the look, the shots, line timing.)

### Game 1: Switchboard (Claude) — split information, everyone gives and takes
- Levers = N + 3 on a ring mid-stage (~5 m apart; see Scaling), each on a trapdoor tile.
- **Names you can't read up close:** each lever has a nonsense name (THE GRIMSHAW, BONE VALVE...) on
  a plate facing *outward*, readable only from the rim strip (11 m or more from the centre) inside
  a 30° cone behind that lever. Pullers at the ring can't see names; a reader at the rim sees at
  most 1–2 plates (checked by the critic's sight-line grid). Names shuffle every 20 s.
- **Orders:** every player (ghosts too) holds one order on their HUD ("PULL THE GRIMSHAW"), never two
  orders on one lever. **You can't pull your own order.** So everyone is shouting their order,
  reading names for others, and pulling for others, all at once. The dead keep holding and
  shouting orders and can read plates; only pulling needs a living body. Ghosts stay over the
  stage square, move at walking speed, no higher than 2 m, and read through the same cone (no
  all-seeing ghost: dying never helps).
- Pull: hold E 0.5 s; a gripped lever visibly locks so two can't grab it. A pull on a lever with
  no order (or your own) = wrong pull: your trapdoor drops.
- Order timer 11 s, shrinking to 9 s as the quota fills. Runs out: the screen names the holder and
  the nearest player; the nearest drops (only one claimed puller, heading to it within 3 m, is spared).
- Dropped tiles rise after 3 s. **Clear:** 7 orders per starting player within 80 s. Simulated with
  readers walking to the rim and pullers to the ring (`tools/switchboard_check.py`, assumed human
  timings): sharp crew 96–97% (~38 s), typical 63–68% (~48 s), sloppy 8–15%, flat from N = 3 to 6. Time up: the stage drops. Lone survivor may pull their own orders;
  the quota stays (dying never helps).

### Game 2: The Tilt (Claude) — split sight, everyone moves at once
- Tiles drop until a 12 × 12 m slab is left on a pivot; tilts on 2 axes toward the crew's weight
  (3.5° per metre of summed offset, 0.6 s lag, cap 18°). Slide above 6°: 0.3 m/s per degree over 6.
- Shape landmarks on the 4 edges: the Reaper's throne, the camera crane, the band, the audience.
- **Keys:** each wave places one key per *starting* player, spread so their offsets sum to zero and
  no smaller group of keys sums under 3 m (no self-cancelling pairs: the whole crew is one
  balance). Grab = the whole crew stands on the wave's keys at once **while the slab is near level (under
  6°)** for 1 s; they fill together (bot test: one-by-one filling stranded a lone key) (bot test showed you could
  otherwise grab by walking against the slide, making balance optional); a grabbed key is spent and its grabber may move on, so after
  deaths the living can take keys one by one with counterweights.
- **Split sight:** each key is visible to exactly one other player (you never see your own); who
  sees whose key is one loop through the whole crew (A sees B's, B sees C's... last sees A's), and it
  fades as its viewer comes near (flat distance, from 8 m to gone at 5 m; no walking or hovering
  over it as a beacon): you must describe it from
  afar ("Bo: behind the crane, far edge"). Dead players' ghosts keep seeing their keys and keep
  calling them out (the dead still play; dying never removes keys).
- 4 waves in 75 s. Time up: the slab flips. Blame on a fall: whose own walking (not sliding) added
  most tilt in the last 2 s.

### Level 3: Switchboard II (Claude)
Switchboard plus TOGETHER orders ("GRIMSHAW + BONE VALVE TOGETHER"): two levers held at the same
moment for 0.5 s, by two players other than the holder; only while 3+ are alive.

### Scaling with the crew (user 2026-11-08: "resizeable with amount of players"; min 3 to start)
N = players at the start of the show (3–6; the show can't start with fewer).
- Switchboard: levers = N + 3; ring radius = levers × 5 m / 2π (levers ~5 m apart: 4.8 m at 6,
  7.2 m at 9); quota = 7 × N in 80 s; orders in flight = N (ghosts hold orders too).
- The Tilt: slab side = 8 + 4N/3 m (12 at 3, 16 at 6); keys up to slab half − 0.5 m out;
  tilt per metre = 3.5° × √(3/N) (2.47° at 6: random errors of N people add like √N).
- Switchboard II: TOGETHER orders = 1 in 4 at N ≤ 4, 1 in 3 at N ≥ 5; at most floor(living / 3) in
  flight and never more levers than are free.

### Scaling critic (round 1)
Critic: Tilt splits into pairs at 6, Switchboard centre hub at N ≥ 5, death spiral against the
quota, TOGETHER overflow, 3/N over-corrects. All fixed above.

### Scaling critic (round 2)
Critic: plates unreadable at N ≥ 5 (rim spots off the stage), ghost quarterback (free flight),
ghost beacon over keys, sim had no readers. Fixed above; sim rebuilt with readers and re-tuned.
Tilt key generation: generate the next wave during the current one (rejection rate ~0.1% at 6).

### Risks for the playtest (not severe on paper)
- Switchboard with 6 shouting at once: chaos (fun?) or noise.
- The Tilt alone at the end is near-impossible (an edge key alone tips 13–18°): a lone survivor
  loses. Kept on purpose (dying must never help); watch it in the playtest.
- Voice load at 6 (6 orders, 6 key descriptions): fallback 3 Tilt waves at N ≥ 5.
- Switchboard: a holder far out may read their own lever and just steer a puller (gate 7 weak);
  it holds only because everyone juggles several jobs. Watch it.
- Lag over the internet: kill checks are on the host.

### Kept as alternatives
- Split Sight floor (critic r1). The Coffin (carry by 2+).

### The dead join the crowd (user, 2026-11-08): thesis
User: "when a player dies.. should appear with the crowd.. and they can move around".
Now (checked, `player.gd:172`, `course.ghost_bounds`): the dead float as a see-through sphere,
clamped over the stage square and ≤ 2 m above it, at walking speed; they keep their jobs
(Switchboard: hold and shout orders, read plates through the same cone; Tilt: see their key and
call it out).
Thesis (Claude, from the user's words):
- On death the gore stays on the set; ~1.5 s later the dead contestant appears in the audience
  stands (x 19–27, rows rising 1 m per 1.6 m), in a free spot in the front rows, as their own bean
  made see-through, name tag on; the fans next to them cheer.
- They float freely at walking speed inside the stands volume (x 18–28, z -18..18, up to 2 m above
  the rows); never over the stage or the pit. First person, watching the show from the crowd.
- Jobs kept: Switchboard: hold and shout orders; read any plate whose 30° cone reaches the stands
  (the levers facing the audience, 1–3 at N = 3..6); Tilt: see their key (no fade from that far)
  and call it out by the landmarks.
- Revived at the next game, as now.
Effects to check: dead readers lose the rim (dying costs more); the stands as a reading perch for
the audience-facing levers; the lone survivor; Tilt calls from the side view; the drones film the
dead among the crowd; clients clamp their own position (friends-only trust, as now).

### The dead join the crowd: critic -> synthesis
| Critic finding | Synthesis |
|---|---|
| SEVERE: from the stands a dead player can read only the 3 audience-facing plates at any N (old ghost: all N+3); the dead mostly just shout their own order; at N=6 with 3 dead the living must read the rest (death spiral, gameplay #4). "Never over the stage or the pit" was Claude's addition, not the user's | The dead **appear in the stands** among the fans (an empty seat, one per id, see-through bean) and **move around freely outside the play area**: the stands, the rim band and over the pit, ≤ 2 m above stage level; never inside it (Switchboard: flat r < 11; Tilt: the slab + 1 m). Same 30° reading cone, so every plate is readable from somewhere, as before |
| Tilt from the stands turns the throne↔audience axis into depth | Same zone: they circle the slab from outside (the 5 m fade still blocks a beacon) |
| SEVERE, already in the code: after a death the Tilt needs min(open, living) on keys at once (`tilt_rules.gd:129`, checked), but any smaller set of keys sums ≥ 3 m off-centre, so the slab is rarely level (critic's calc: ~35% of waves at N=3 with 2 alive); the doc's "one by one with counterweights" was never built | need = living − 1 after a death (≥ 1): one living player can counterweight while the others grab; spent keys stay spent. Bot test + unit test when built |
| Play footage follows the dead, orbit clips into the stands | Drones follow the living; after a death, one reaction shot of the stands on the big screen |
| Box clamp sinks into the rising rows; fans have no collision | The stands zone has a sloped floor; spawn in an empty seat |
| Edge cases | The move happens 1.5 s after death only if still dead and same level; a teleport, no swoop; the "first fall is on me" spare never sets dead; ghost bots placed by the host; dead bots read plates through `can_read` |
| Plates from 11–25 m at 30° unverified | Screenshot from the back row (`--at`) when built |
