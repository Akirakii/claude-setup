# Design v2: the finished game (round 4: settled, being built)

> 2026-11-06: some numbers here are superseded by the anti-pattern review fixes (stage width,
> mood length, hints, foil hat deed); current rules are in `docs/gameplay-design.md`.

Working draft for the dialectic (log: `docs/design-dialectic.md`). When settled it is folded into
`docs/gameplay-design.md` and friends. User brief (2026-11-05): "a solid understanding of what
works and doesnt work on 5 things: (minigame) non blackout events, (minigame) blackout events, non
minigame event, items, story paths.. enough for a finished game.. a polished game.. no worries
with the risks".

## Changes in round 4 (answers to the critic's round 3; the design is settled here)
- **The seat is a person, not a place.** Whoever stands in the spotlit circle at "go" is the
  seat: the glare follows them until they press or the exam ends, and the signal is hidden on
  their screen wherever they walk. Readers are players more than 4 m *from the seat*. Sequence
  passes the seat to whoever steps into the circle next.
- **Vertical pushes:** the knockback RPC already sets `velocity.y = max(vy, v.y)` (checked:
  `PlayerBody.push`), so it carries launches; a `launch` flag sets it outright for the trampoline.
- **The Maze's walls are the seat's alone**: client-local collision for the walker; everyone else
  sees glowing outlines on the floor plus the hazard tiles. Items and other bodies pass through.
- **Contrary refuses the *item* that scored most** in the last 30 s (bare hands count as one).
- **Greedy Press is the stage-8 gate** (the user's special): stake = the exit. Pass: the exit
  lifts; the lie: the ceiling slams on the presser and it replays.
- **Tin Foil Hat:** blame still lands, anonymised ("Someone in a hat."); the slam hits the hat.
- **Attribution:** an impact belongs to its last toucher (holder, thrower, firer, taper). A
  free-roaming Monkey Car slap belongs to nobody: it never breaks Strike, never counts for Freeze's culprit.
- Specs: Patience duds reset the rest, ownerless hits don't; Twins counts both hits as a pair;
  riding the cart is seated-attached (a snapshot flag; the client follows the cart); Duct Tape is
  E on thing A then E on thing B (a host joint), and a taped ball still counts as its own item
  (ball on the Monkey Car is the intended Overflow find); Freedom's city is drawn over the room's
  own colliders; Block World is an off-map area with its own copy of the button (pillar 1), five
  gold blocks each worth 3% of the stage; Egg unlocks after any finished run.
- Variants: **Fair → Freeze** (counts only while every other player stands still; the cap flashes
  the colour of whoever moved); **the Leak wanders** along the north wall.

## Changes in round 3 (answers to the critic's round 2)
- A. Scale by **target rate**, not exponent: S = max(1, goal / 10,000); a table of seconds.
- B. Blackout signals play **only while someone stands at the seat**, and re-roll when it empties.
- C. Moods gate **impacts too**; Heavy becomes **Contrary** (it refuses whatever scored most);
  Strike counts impacts.
- D. Outside the Box **scores nothing**: the shake is a troll with a comeback (shut the door).
- E. **One host→client channel spec** (impulse, teleport, local effect flags); body slams judged
  from the trampoline's own launch, never from client speed.
- F. **The Maze is real walls in the real room**, built from a seed on every peer.
- G. Chores cap at **2**; each chore type owns one wall and one sound; fails resolve one at a time.
- H. Floor Fire blames **whoever walked through a burning tile** (it spreads by feet). Hot Potato
  stays as the user set it (11-04: "only fines whoever holds it at the end").
- I. The eye stays **hidden by default** (user, 11-03); `Tuning.EYE_VISIBLE` turns it on. The
  Unwatched route works with or without it (foil hats). Parked in `docs/questions.md`.
- Variants: Taking Turns → **Patience**; Crowded → Fair (round 4: Freeze); The Hunt answers a *where*; the Maze
  avoids *hazards*; Block World gets its own action (**dig**).

## The abstract problem
One verb (press), one number. Everything else changes *what that verb means now*, *who can do
it*, or *what else a body should be doing*. The old content asked one question ("press
correctly, all together") with the same information for everyone. So **each kind of moment asks
a different question**:

| Kind | The crew's question | What it splits | How it fails |
|---|---|---|---|
| Items | "What is this thing for?" | verbs between people | it just doesn't score |
| Moods (non-minigame events) | "What does the button want now?" | which hits count | a dud, never a cost |
| Chores (live minigames) | "Who leaves the button?" | **hands**: bodies in places | its own task, in the room |
| Blackouts (dark minigames) | "Who can see?" | **sight**: seat vs reader | one wrong press, a named seat |
| Paths | "What if we do the weird thing?" | the crew's plan vs the narrator's | a route ends the run its own way |

Rules every part keeps: one active *button rule* at a time (AP9); signal *that*, never *what*
(Fantasy); a press only fails in a blackout (user, 11-04); hands are scarce (pillar 2); items need
people, never timers (user, 11-03); losses moment-sized, on a culprit, for a slip (AP7, 13, 17);
roles by position (AP14, 15); timing in seconds (AP16).

## Scale: eight stages to one billion
- Goals: 100, 1k, 10k, 100k, 1M, 10M, 100M, 1B.
- **Sensitivity** S = max(1, goal / 10,000): stages 1–3 S = 1, then 10, 100, 1k, 10k, 100k.
  Every impact and tool press is × S; **a bare hand stays +1** (user, 11-03).
- Target: a 4-player crew with a few items makes ~40 base units/s (hammer ~10/s, a batted ball
  ~30 per hit, a cannon shot 100–150), so stages 3–8 each take ~10,000/40 ≈ 4 min. Stages 1–2
  are the warm-up (100 by hand ≈ 10 s; 1k ≈ 1 min with the first items).

| Crew | base units/s (guess) | stage 3–8 each | run (8 stages) |
|---|---|---|---|
| 2 | ~22 | ~7.5 min | ~45 min |
| 4 | ~40 | ~4 min | ~27 min |
| 8 | ~70 | ~2.5 min | ~17 min |
  The ceiling's seconds already scale with crew size; tune S-width by playtest.
- Shown, not told: each milestone the pedestal grows a ring and one more digit lamp lights;
  impact pops grow. Prices × S, so the shop stays meaningful. Fines are a share, so they scale.

## Host→client channel (one spec for everything that moves a player)
- **Impulses** (slap, steam blast, dynamite, blower, shake, trampoline launch, spit push): the host
  sends the existing `knockback` RPC; the client adds it to its velocity.
- **Teleports** (VIP room, door worlds, Freedom return): the existing `teleport` RPC.
- **Continuous local effects** (ice floor, balloon float, taped hands, low gravity, reversed,
  glare): flags in the snapshot, applied by each client to its own body (like low gravity today).
- **Body slam:** the host gave the launch, so it knows it: a player launched by a trampoline
  within the last 2 s whose pose comes within 1.0 m above the button top scores an impact at the
  launch speed × 80 kg (once per launch). Clients never report speeds.

## Rhythm: the stage director
- **One button rule at a time** (a mood or an order). **Chores run alongside** (they never touch
  the button): 1 slot for 2–3 players, 2 for 4–8. Each chore type owns one wall, one sound and one
  light colour, so two at once stay readable; fails resolve one at a time (3 s apart).
- Stage 1: silent, no events. If the hatch is still hidden, the first milestone ("100.") opens it
  and spits a free Squeaky Hammer: the hatch gives things.
- Stage 2+: a mood every ~45 s (25 s long), a chore every ~35 s per slot, an order in the gaps;
  15 s of calm after each before the next of the same kind.
- **Stage 3+: the blackout gates the milestone.** At the goal the count freezes (more hits clank,
  "full"), the lights die, the exam runs. Pass: the milestone lands (ceiling resets, fanfare).
  Fail: the ceiling slams over the culprit's spot first, the count drops 5%, and the exam replays
  30 s later. Crews of one: no blackout.
- Per-run variety: each run draws 4 of 5 moods, 4 of 6 chores, 3 of 4 blackouts, 1 of 2 door
  worlds; one run shows part of the catalogue.

### What each player does
- 2: one scores, one runs the chore; Twins and Freeze take both; blackouts: a seat and a reader.
- 4: two scoring, one or two on chores, someone shopping; blackouts: a seat, three readers.
- 8: two chores, a mood, the shop, items needing two (bat, cart, cannon); Sequence takes all.

## 1. Items: one verb each
Physics things spat from the hatch; one verb nobody explains; a way to hurt friends; no item is
the counter for one event. Hand items: E take, E use, G drop. Big items: the beam.

| # | Item | Verb | Scores how | Hurts friends | Also |
|---|---|---|---|---|---|
| 1 | Squeaky Hammer | swing | +5×S on the button | bonk | breaks eggs |
| 2 | Ball + Bat | pitch / bat | impact × pair bonus | knocks over | blinds the eye (Unwatched) |
| 3 | Monkey Car | herd | slaps the button in passing | runs people over | combos (Overflow) |
| 4 | Cannon | load / fire | fires anything by impact | point-blank | fires the alien (Moon) |
| 5 | Trampoline | bounce | a body landing on the button (body slam) | launches people into each other | reaches the ceiling hatch |
| 6 | Shopping Cart | ride / push | cart + rider by impact (host-judged from the cart's body) | rams | cracks the weak wall |
| 7 | Leaf Blower | blow | blows things into the button | blows people off it | fans Floor Fire (spreads it) |
| 8 | Duct Tape | stick | tape a thing to a thing (ball on the Monkey Car rides it) | tape a friend's hands (8 s, a slap frees) | holds the Leak shut, no hand |
| 9 | Balloons | lift | - | tie to a friend: they float 6 s | one balloon: one player carries a heavy thing |
| 10 | Crowbar | pry | - | - | the hatch (a free item, a fine); the cracked wall |
| 11 | Dynamite | blast | a blast by the button: a big impact | knocks everyone | cracks walls, flings items |
| 12 | Tin Foil Hat | hide | - | - | the narrator can't see or name the wearer; blame still lands, anonymised ("Someone in a hat.") |
| 13 | Flashlight | reveal | - | blinds the seat in the dark | hidden writing, The Hunt |
| 14 | Egg | raise | - | anyone can break it | Moon |
| 15 | ??? Door | open | - | - | the door worlds (from 500, user 11-03) |

- **Unlocks**: a fresh save sells 1–4, Flashlight and Duct Tape. Scorers unlock one per lost run
  (Trampoline, Cart, Leaf Blower, Balloons). Path items unlock by a deed in any run: Crowbar after
  a wall cracks; Dynamite after the Crowbar opens something; Tin Foil Hat after one player is
  blamed 5 times in a run; Egg after the crew's first finished run. **The lobby pools unlocks**:
  the shop offers anything any connected player has unlocked.

## 2. Moods (non-minigame events): "what does the button want?"
The pitch's promise. A mood changes which hits count (hands, tools and impacts alike). One that
doesn't count is a **dud**: a dead clack, no number, never a cost. Signal: the cap takes a colour
(shuffled per run: colour says THAT, never WHAT) and a chime. No line. 25 s. **Each dud is a
clue** to which way is wrong, never the rule. Five, each on a different axis:

| Mood | Axis | Counts when | The dud's clue |
|---|---|---|---|
| Twins | place | a second button appears across the room; a hit on one counts if the other was hit within 1.5 s | the other button blinks |
| Patience | tempo | the button rested 2 s since the last hit (one careful hit, not a mash) | the cap's glow drains and refills over 2 s |
| Contrary | kind | it refuses the item that scored most in the last 30 s (bare hands count as one) | a metal clank, the cap doesn't sink |
| Freeze | stillness | every other player stands still: host pose speed under 0.5 m/s (looking around is fine; players away in the VIP room, Freedom, a door world or held by the arm don't count; a shove counts as moving and its owner is the culprit); skipped at 7–8 players | the cap flashes the colour of whoever moved |
| Runaway | location | it drives around the room (existing) | - |
- Room moods (same slot): Low Gravity, Reversed (one subject's controls).
- Patience and Freeze are the friendslop ones: one friend ruins it for all ("STOP, Bo").

## 3. Chores (live minigames, lights on): "who leaves the button?"
Start: its own wall's sound and light, a visible change; nothing explained. Takes 1–2 bodies
(never all); worse while ignored; fails in the room; a culprit for a slip; items help or hurt.

| Chore | Wall | Split | Fail (in the room) | Culprit |
|---|---|---|---|---|
| Pressure Valve | west | info: the gauge by the button, the wheel at the west wall (turned by E-hold) | pipe bursts: steam blasts people, ceiling lurch | the turner (over or under) |
| The Leak | north | hold a spot: stand at the crack with E held | the floor ices for 10 s; everyone slides | whoever let go |
| Hot Box | east (hatch) | joint carry back into the hatch | it bursts: knocks everyone near | the last holder (soot) |
| Floor Fire | south | contain: fire spreads tile by tile; stamping (walking) on a tile *with E held* puts it out; walking through without E spreads it | burns items on it, ceiling lurch | whoever spread it |
| The Stray | vent (corner) | corner: a critter nibbles the count; it flees players and slips past one | it escapes with 2% | whoever it slipped past |
| Hot Potato | - | pass by slap (2+ players) | the holder pays, the cone | the holder (user, 11-04) |
- Meaner per stage: a faster gauge, two cracks, a bigger box, a quicker critter, more tiles.
- 1-player crews skip Valve and Potato.

## 4. Blackouts (dark minigames): "who can see?"
Stage 3+, the milestone's gate. Lights out, the ceiling pauses, items stop scoring. **The seat
is a person**: whoever stands in the spotlit circle at "go" (else the player nearest it). The seat
gets a white glare on screen that follows them until they press or the exam ends, and the signal
is never drawn on their screen. **Readers** are players more than 4 m from the seat; only their
screens draw the signal (in the Hunt, a reader who walks within 4 m of the seat loses the mark
too: on purpose, readers must keep away). Briefing stays (user, 11-04). Needs 2+ players.

| Blackout | Formula | Readers see | The seat must | Culprit |
|---|---|---|---|---|
| Blink Count | how many | a far lamp blinks N (3–9) times | press exactly N | the presser who went over |
| The Hunt | which | two free flashlights; four buttons in the dark by the walls; a mark hidden on one wall, seen only in a beam, says which | walk to that button and press it (glare follows the seat) | whoever pressed a wrong one |
| The Maze | which path | at "go" the seat is teleported to a start corner; a seeded maze between it and the button, whose walls collide for the seat only (client-local); readers see the walls as floor outlines plus 3 hazard cells | reach the button and press it; a hazard cell (checked on the host from the seat's pose) zaps them back to the start; 2 zaps lose | the seat (each zap) |
| Sequence | who, in order | player colours light on the wall in an order (4–6 steps) | presses come from those players in that order; the glare ends on each press and passes to the next player to enter the circle; entering out of turn is fine until they press | whoever pressed out of turn |
| Greedy Press (stage-8 gate, user's) | - | - | the first press in 10 s opens the exit; 20% the button lies: the ceiling slams on the presser and it replays | the presser |
- Dropped: green light, reaction, countdown, rhythm, quiz, PvP, last one, The Lie, The Tower.

## 5. Paths: loops and routes
Each opens from a **different action**. Loops return; routes end the run (an ending). The exit
room has six blank plinths; each ending found lights one (says that more exist, never what).
Hints: hand-made flashlight writing from "past crews", one per run: "WE STOPPED. IT BEGGED.",
"THIN HERE" on the weak wall, "IT CAN'T SEE WHAT IT CAN'T SEE", "IT GOT COLD", "THREE AT ONCE".

### Routes (endings)
| Route | Action | Opens when | Steps | Ending |
|---|---|---|---|---|
| **Escape** | press | the count reaches 1B | - | the exit lifts (existing) |
| **Strike** | refuse | stage 2+, no mood running, every player within 3 m of the button, nothing scores for 20 s | the narrator stalls, then bargains three times (a free item; "one press and I lift the ceiling"; the ceiling at ×2); any score breaks it and names who caved; 90 s total | "Fine. I'll find better subjects." The exit opens |
| **Moon** | raise | the Egg hatches (2+ players within 1.8 m for 45 s) | three signs in flashlight writing, each a task: a ball (hand it one), the button (carry it there: it presses 3 times), the cannon (load it); loading it opens the ceiling's maintenance hatch; fire | a tractor beam lifts the crew out |
| **Breakout** | break | a heavy hit (cannon shot, dynamite, cart at 6+ m/s) on the weak wall panel (south-west) | 4 cracks, then the Crowbar pries it; behind: the narrator's server and its cable; 3 on the beam pull it | the narrator dies mid-sentence; the wall falls |
| **Overflow** | glitch | three hits by three different items within 1.5 s (a combo) | three combos; the counter glitches each time; the third wraps it to 999,999,999 | one press: 1,000,000,000 in a glitched room. "That doesn't count." |
| **Unwatched** | hide | the narrator sees nobody: everyone wears a Tin Foil Hat, or (eye visible) a batted ball blinds the eye | "Room empty. Sending cleanup." A service door opens in the north wall; a cleaning robot rolls in; all crew must be through within 20 s; anyone unhatted and outside when the eye returns closes it | the crew rides out with the robot |

### Loops (closed)
| Loop | Action | Opens | Inside | Closes |
|---|---|---|---|---|
| Outside the Box | shake (door world 1) | the ??? door set in a wall | the testing room as a cube on a table; pick it up and shake it: everything and everyone in the real room is flung; hits during a shake score nothing | walk back; the crew can shut the door on the shaker |
| Block World | dig (door world 2) | the door set in a wall | a blocky copy of the room with a block floor; E breaks blocks; an off-map copy with its own button (pillar 1); five buried gold blocks each worth 3% of the stage; finite per run | walk back |
| VIP Room | sell a friend | a player slapped or bonked into the hatch wall while the hatch is open (within 0.9 m of the east wall, |z| < 1) | couch, a TV of the main room, six unlabeled buttons that fire moods and room moods in the main room | the crew buys them back at the hatch (today's price) |
| Freedom | isolate | rare (1 in 4 chance once per run): a player alone in a corner, 8 m from all, 15 s | a city street only they see; their body walks in the room | 15 s; they come back holding a hot dog (a real item) |
| Ghost | leave | a player left the game | one other player sees their ghost replay their recorded path | fades after 30 s |

## Narrator
3+ lines per piece, never explaining (dialog AP1–7). Moods: no line. Chore fails name the
culprit. Route steps have their own lines. Strike is mostly narrator.

## Stays the same
Press +1, impact scoring, the hatch, the beam, the ceiling, milestones, orders, memory director,
hog/slacker, cursed button, Greedy Press.
