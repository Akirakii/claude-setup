# Gameplay design

Rules, numbers' shape and incentives. Core loop: `docs/core-design.md`. Check new features against
`docs/gameplay-anti-patterns.md`. Exact numbers live in `scripts/core/tuning.gd` and
`scripts/core/economy.gd` and are tuned by playtest.

## Pressing
- **A bare-hand press is always +1** (user, 2026-11-03: "+1 on each press.. instead of summing up").
  No upgrade, crit, bonus or event makes it worth more. Narrator rules may flip it to −1 (rule
  flip "pressing costs points", the hot potato holder).
- **Fast clicks count, drag clicking included** (user, 2026-11-03: "one person gets the chance to
  shine in a clicking game .. but only at the start.. later to get points is to wire machines and
  upgrades rather than just clicking fast"; "yes proceed"): bare-hand presses count up to 60 a
  second, 6 saved up so network bunching drops none; only macros hit the cap. Research (3 s): one
  finger ~6–7/s, jitter ~10–14/s, butterfly ~24–27/s, drag up to ~50/s (unverified).
  - Tools keep their own pace: the hammer hits once per swing (0.5 s), however fast the click, so a
    fast clicker shines bare-handed only and items still take over.
  - The press thump plays at most ~16 times a second, so fast clicking is not a buzz.
  - Caveat: with the MVP goal at 1,000, a drag clicker at 50/s finishes alone in ~20 s; clicking
    only fades once the goal is big (1B). Judge it in a playtest.
- **A held tool hits harder than a hand** (user, 2026-11-03: "yes" to "the bare hand stays +1, a
  held tool hits harder"). The bonus is visible: someone holds the tool, it can be stolen, and
  it's gone when dropped. Today's only tool is the Squeaky Hammer.
- **Things that hit the button score by impact speed × weight** (user, 2026-11-03: "speed hitting
  the button should define the points gained", "keep the same universal rule but multiplied with
  weight"). One rule for anything thrown, batted, driven or fired: light things score little
  however they fly, heavy things a lot. A bigger hit gets a bigger number pop and a louder thunk.
  Too slow scores nothing but still thuds, so no try is met with silence (discovery review,
  2026-11-06); a soft hit on the weak panel sounds hollow without cracking it. All of it is × the stage's sensitivity (see Run structure).
- **The only exception: object-to-object pairs** (user, 2026-11-03: "ball only gets a multiplier
  with the bat"). A ball sent by the bat gets a pair bonus; nothing else has one yet.
- **Press by standing next to the button** (user, 2026-11-03: "I should be close to it, not look at
  it"): E presses the nearest button within 1.5 m (real, decoy, cursed, exit). Looking at
  something else (a machine, a player) wins, so you can still slap at the button.
- The host checks the rate: up to 60 bare-hand presses a second, 6 saved up (see above).

## Run structure
- **Eight stages to one billion** (design v2): goals 100, 1k, 10k, 100k, 1M, 10M, 100M, 1B. First
  milestone 100 (user, 2026-11-03). Reaching one resets the ceiling to the top, lights one more
  lamp around the pedestal and makes the narrator meaner. From stage 3 an exam gates it (see Five
  kinds of moment); the first milestone spits a free Squeaky Hammer (the hatch gives things).
- **Sensitivity S = max(1, goal / 5,000)** (design v2; halved (user, 2026-11-06: "apply", to the anti-pattern review fixes) so a run is
  short enough to lose, gameplay AP11): impacts, tools, slams and blasts are worth S times their
  base; a bare hand stays +1 (user, 2026-11-03). Stages 1–2 are a warm-up; stages 3–8 are each
  ~4,500 base units wide, about 2 min for a 4-player crew at ~40 units/s, with ceilings of
  300–360 s: a run of ~14 min for 4, ~23 min for 2 (guess; tune by playtest). Prices scale with S;
  fines are a share of the wallet.
- **Quiet opening, discovered not told** (user, 2026-11-03: "the start should be more silent",
  "autodiscovery and mystery", "time for the player to process"):
  - Stage 1 is silent: no narrator, no orders, a slow ceiling (240 s). The narrator's first word
    is the milestone ("100."); orders begin after it.
  - The shop hatch slides out of the east wall 40 s into a run (user: "the shop should be hidden
    and open after some time").
  - The exit is hidden and shows itself only on a win.
- **The pedestal shows the goal under the count** ("40 / 100") (discovery review, 2026-11-06, user:
  "review this game and fix it"; was the open question "goal shown nowhere"): the goal is never
  hidden, only the way to reach it.
- **Lose:** the ceiling reaches head height. Squish + narrator line.
- **The ceiling timer is on again** (user, 2026-11-03: chose "turn ceiling timer back on" for the
  red timer monitor; it had been off after "remove the timer for now"): the ceiling falls on its own
  (`Tuning.CEILING_FALLS`), so a run can be lost.
- **Narrator on** (user, 2026-11-04: "enable the narrator boolean"; off since 2026-11-03):
  `Tuning.NARRATOR` turns on every line, narrator orders and every event, game and minigame;
  false mutes them all.
- **Shop open from the start** (user, 2026-11-03: "start with the shop. for now true"):
  `Tuning.SHOP_AT_START` true skips the 40 s hatch delay.
- **Whole shop unlocked and free** (user, 2026-11-03: "a boolean to have all shop unlocked", then
  "all unlocked + and everything free"): `Tuning.SHOP_ALL_FREE` true ignores stage tiers and loss
  unlocks and makes every price 0 (refunds 0 too); level caps and the machine limit stay.
- **No text on screen** (user, 2026-11-03: "remove all text inscreen. just the +1 points is
  enough"; chose to keep the pedestal counter and ceiling timer): `Tuning.SCREEN_TEXT` false hides
  the overlay text and the floating labels; floating press numbers stay.
- **Spit pushes** (user, 2026-11-03: "instead of teleporting the player when spiting the item.. it
  should push the player"): whoever stands where the item comes out is pushed into the room
  (`Tuning.SPIT_PUSH`, 6 m/s within 1.8 m); the fresh item does not block bodies for 0.5 s.
- **Sell only up close** (user, 2026-11-03: "to sell someone has to be super close with the
  item", then "not you as the player but the item should be super close"): a held thing goes
  back through the hatch only when the item itself is within `Tuning.SELL_RANGE` (0.8 m) of it.
- **Speed earns no power.** Leftover time gives fame only (narrator records); a fast crew gets a
  spicier next stage.

## Rewards and losses
- **Rewards are never machines or upgrades** (user, 2026-11-03: "no machines and upgrades as
  rewards"). Those are only bought. Test for any reward or punishment: it changes the moment
  (points, ceiling time, a short effect, something social), never the crew's earning rate for the
  rest of the run.
- **Losing a run unlocks something** (pillar 3): the next scorer (trampoline, cart, blower,
  balloons). Once all four are out, a loss leaves one more flashlight hint on the walls of the next
  run (user, 2026-11-06: "apply", to the anti-pattern review fixes). Deeds unlock path items (see Items). Endings found light plinths in the exit room.

## Economy and shop
- **The count is both progress and money.** Buying spends presses and moves you away from the goal.
- **One shared wallet;** anyone can buy anything ("who spent 50k on a disco ball?!").
- **Fines:** the narrator fines bad or funny behaviour from the wallet (failed orders, the hot
  potato, prying the hatch). Nothing absorbs them (cigarettes and insurance went with design v2).
  One order's fines together take at most 6% of the wallet, split among those who failed; the hot
  potato's holder pays 5% (gap review 2026-11-06, Claude's picks: one loss never scales with the
  crew, and never outweighs a failed exam).
- **Buying is a physical act** at the shop hatch (a visible culprit): E opens it, you order from
  an on-screen menu, the item is spat out of the slot. Unwanted things are carried back and
  pushed into the hatch for 50% of their price.
- **The spender has a face, and the crew a comeback** (user, 2026-11-06: "apply", to the anti-pattern review fixes), gameplay AP8: a bought
  thing wears a band in its buyer's colour (no text). Thrown back within 20 s it refunds in full
  and the narrator names the buyer ("Ana's cannon. Back within seconds."); later, 50%.
- **Items are physical things** (user, 2026-11-03: "literally spit the item itself and the
  player has to carry the item.. no fixed position for items"). The hatch spits the item itself;
  it stays wherever it lands or is put. No machine slots, no fixed Master Switch.
- **Holding, R.E.P.O.-style** (user, 2026-11-03: "there should be heavy items that the player will
  have difficulties.. like repo.. we should have repo holding mechanics"): hold F to grab with a
  beam, let go to drop. Each holder adds lifting force; too heavy for the holders, it only drags.
  The beam holds the spot it hit on the surface, not the centre (user, 2026-11-03: "the repo
  grab.. that works by hitting a surface.. not from the center"): each holder pulls their spot, so
  it hangs from where it was grabbed. It keeps the turn it had when grabbed and turns with the
  first holder (that aims the cannon). Weights: hammer, ball and bat are light;
  monkey car slow alone; cannon needs two (barely) or three. The beam is green (easy), yellow
  (slow) or red (too heavy, get help). Numbers in `scripts/core/tuning.gd`, guessed (no official
  R.E.P.O. figures found).
- **The shop shows only each item's look, name and price, never how to use it** (user, 2026-11-03:
  "the shop just display items and their names.. and doesnt show how to use it.. the fun is to
  let them blame on something apparently useless until proven its value"). Points buy items
  directly (no boxes, no tickets: the crew's real decision is what to spend on). Players find out
  each item's use by trying it; the impact-speed number pop is how an item proves itself.
- **Every item needs people** (user, 2026-11-03, after choosing items that make the crew do
  something over idle auto-pressers): each one scores only through a hand, a team play or herding,
  never on a timer. Anything held by the hatch can be thrown back: E, 50%.
- **On sale:** see Items (design v2). Everything sold before is gone from the game: machines,
  upgrades, junk, insurance, the old loss unlocks (user, 2026-11-03: "lets remove all current
  items"; their code was removed with design v2). Fines stay; nothing absorbs them.

## Items
Design v2 (`docs/design-v2.md`, Claude's design 2026-11-05 from the user's brief "lots of items,
events and story paths.. enough for a finished game"; built, numbers to tune by playtest). Every
item is a physics thing spat from the hatch with **one verb nobody explains**, a way to hurt
friends, and no item is the counter to one event (it can help or make a chore worse).
- **Hammer, bat and ball go in the hand** (user, 2026-11-03: "bat, ball and the hjammer should be
  equiped in the hand"); so do the other small items. Big items are carried on the beam.
- **A slap knocks the item out of someone's hand** (Claude's choice, to confirm).
- **A ball ×bat is the only object pair** (user, 2026-11-03: "ball only gets a multiplier with the
  bat"); a thrown ball alone scores "very small like +1 or +2" (user, 2026-11-03).
- **The cannon doesn't burn its load** (user, 2026-11-03: "it shouldnt burn the item.. just shoot it").

| Item | Verb | Scores | Hurts friends | Also |
|---|---|---|---|---|
| Squeaky Hammer | swing | +5 × S per hit | bonk | breaks eggs |
| Ball + Bat | pitch / bat | impact × 8 off the bat | knocks over | blinds the eye (if shown) |
| Monkey Car | herd | slaps the button in passing, scoring only within 10 s of someone steering it (audit 2026-11-06: never on its own) | runs people over | carries taped things (Overflow) |
| Cannon | load / fire | fires anything by impact | point-blank | fires the alien home (Moon) |
| Trampoline | bounce | a body slam onto the button (80 kg) | launches into others | |
| Shopping Cart | ride / push (E tap) | cart + rider by impact | rams | with a rider, cracks the weak wall |
| Leaf Blower | blow | blows things into the button | blows people off it | fans Floor Fire |
| Duct Tape (3 strips) | stick | - | tapes a friend's hands 8 s (a slap frees) | holds the Leak shut; tapes thing to thing |
| Balloons (3) | lift | - | floats a friend 6 s | lightens a heavy thing |
| Crowbar | pry | - | - | the hatch (a free item, a fine); the weak panel |
| Dynamite | blast (E lights, E throws) | a blast by the button | knocks everyone | cracks the weak panel |
| Tin Foil Hat | hide | - | - | the narrator can't name you ("Someone in a hat") |
| Flashlight | reveal | - | blinds the seat | hidden writing, the Hunt |
| Egg | raise | - | anyone can break it | the Moon |
| ??? (door) | open | - | - | the door worlds (from 500, user 2026-11-03) |
- **Unlocks** (pillar 3, 4): a fresh save sells hammer, ball + bat, monkey car, cannon,
  flashlight, tape and the ???. Each lost run unlocks one scorer (trampoline, cart, blower,
  balloons). Path items unlock by a deed in any run: crowbar (a wall cracked), dynamite (the
  crowbar opened something), foil hat (one subject blamed three times; was five, (user, 2026-11-06: "apply", to the anti-pattern review fixes)),
  egg (any run ended).
  **The lobby pools unlocks:** the shop offers anything any connected player has unlocked.
- **Prices scale with the stage** (× S), so a buy always means something.

## The ??? item and the door
- **The shop shows a ??? slot** (user, 2026-11-03: "a ??? item that you cannot buy until the first
  500 points"): a dark silhouette, locked until the count reaches 500.
- **The ??? is a door** (user, 2026-11-03: "the game should kinda feel like the unlimitless of
  imagination like stanley parable.. like all of a sudden inside a minecraft world"). Carried on
  the beam; let go against a wall (not the hatch, the exit or the weak panel) and it sets in.
  Walking into its frame goes through; the world's own door comes back. E on it shuts or opens it.
- **One world per run** (Claude's design, built):
  - **Outside the Box** (action: shake): the testing room seen from outside, a cube on a table.
    E on the cube flings everything and everyone in the real room; hits during a shake score
    nothing. The crew can shut the door on the shaker.
  - **Block World** (action: dig) is the **solo room** (user, 2026-11-03: "only one player can
    enter that room and then closes and the player gets trapped in the other room until finishes
    the task there"): the first one through is locked in a blocky copy with its own button
    (pillar 1) until they dig up a gold block. **The rooms need each other** (user, 2026-11-03:
    "the second room needs clues from the first room"): the gold map is drawn only on the main
    room's floor by the door, so the crew talks the digger to it. Each gold block is worth 3% of
    the stage. The lock gives up on its own after 90 s, so the trap never stalls (gameplay AP14;
    (user, 2026-11-06: "apply", to the anti-pattern review fixes)).
- **The ceiling is shared:** one clock over every room.

## Path items
- **Flashlight: reveal** (user, 2026-11-03: "i like the flashlight one. record that"). Its beam
  shows writing on the walls that is otherwise invisible: marks of past crews, one hand-made route
  hint per run, the alien's signs, and the Hunt's answer.
- **Egg: raise** (user, 2026-11-03: "it should need warm and avoid from other players breaking it").
  It warms while 2+ subjects stand close (45 s), cools otherwise; a hard hit or a hammer breaks it
  for the run (Claude's choices, to confirm).
  - **It hatches into an alien** (user, 2026-11-03: "it needs to return to the moon.. the clues or
    fomulra to go to the moon"): see the Moon route.

## Private realities
- **Surprises only one player sees** (user, 2026-11-03: "surprises where friends cannot believe").
  **Rare** (user, 2026-11-03: "lets not abuse").
- **Freedom** (user, 2026-11-03: "a player gets teleported to freedom.. is outside in the city but
  only that player can see that"). Built: armed in 1 of 4 runs; a subject alone in a corner (all
  others 8 m away) for 15 s sees a city street for 15 s, drawn over the room's own walls; they come
  back holding a hot dog (a real item, the only proof).
- **The ghost of a friend who left** (user, 2026-11-03: "can reappear as a ghost that only one of the
  players can see"). Built: the game records each path (the last 30 s); a leaver's ghost replays it
  for one other subject 20 s later, or 60 s into a later run they miss.

## Loops
- **Paths are closed loops, not storylines** (user, 2026-11-03); a route ends the run its own way.
- **Each loop opens from a different action** (`CLAUDE.md`, "Before sketching"): open (the door
  worlds: shake, dig), sell a friend (VIP room), isolate (Freedom), leave (the ghost).
- **VIP room** (user, 2026-11-03: "selling a friend.. that friend should go into a vip room that has
  many buttons to mess with your friends. a couch, tv, gaming setup, disco ball, pop corn, etc.
  gelato machine"). Built: a subject slapped or knocked into the east wall by the open hatch is
  sold (the crew gets 4% of the stage). Inside: couch, popcorn, gelato machine, gaming setup, disco
  ball, a TV of the main room, and six unlabeled buttons (low gravity, reverse someone, flickering
  lights, a free toy from the hatch, a blinking button, a taunt). The crew buys them back at the
  hatch (the shop's second column, 8% of the stage): the comeback to the trolling (anti-pattern 8).
  Unbought, the lounge sends them back after 90 s (gameplay AP2; (user, 2026-11-06: "apply", to the anti-pattern review fixes)).
- **Paths don't come from the old items** (user, 2026-11-03: "with current items no"): the routes
  use new items; the old scorers only help (the ball blinds the eye, the cannon fires the alien).

## Routes
- **A route runs to its own end of the game** (user, 2026-11-03: "those kind of things that will
  open a new story route.. with their own tasks and secrets until finishing the game"). Six
  endings; each lights a blank plinth in the exit room (says *that* more exist, never which).
- **Escape** (press): the count reaches 1B through the Greedy gate.
- **Strike** (refuse): from stage 2, no mood running, every subject within 3 m of the button and
  nobody tries a hit for 20 s (a throw, swing, shot, gust or bounce counts as a try, hit or miss:
  a crew busy trying is never on strike by accident; gap review 2026-11-06). The narrator stalls, then bargains three times (a free item; "one
  press and I lift the ceiling", kept if someone caves; the ceiling at ×2). Any hit names who
  caved. 90 s and it gives up: the exit opens.
- **Moon** (raise; user, 2026-11-03): the alien draws signs only the flashlight shows, one ahead
  of its task: a ball (it eats one), the button (carried there, it presses three times; pillar 1),
  the cannon (loaded, the ceiling's maintenance hatch opens). Fired up: a tractor beam lifts the crew.
- **Breakout** (break; user, 2026-11-03: "a wall starts to show some crack.. and players needs to
  open that until a new side is discovered"): hard hits (a fast thing, dynamite, the cart) on the
  weak panel in the west wall (a faint seam round it, its only tell besides the hollow sound;
  audit 2026-11-06) crack it; four cracks and the crowbar pries it open; behind it the
  narrator's server; three subjects holding the cable for 2 s pull it. The narrator stops mid-word.
- **Overflow** (glitch; user, 2026-11-03: "player does some wierd combination with the items.. like
  a infinite glitch"): three different items hit the button within 1.5 s (a combo); three combos
  wrap the counter to 999,999,999; the next hit reads one billion. "That doesn't count."
- **Unwatched** (hide): every subject in a tin foil hat for 3 s (or, with the eye shown, a batted
  ball in the eye) and the narrator sends cleanup: a service door opens in the north wall; everyone
  through it walks out. A hit gives them away; an unhatted subject in the room when the eye comes
  back (20 s) closes it.
- **Hints are found, then read** (discovery review, 2026-11-06, user: "review this game and fix
  it"): every past crew's writing leaves a faint stain on the wall seen without a light (*that*
  something is there), and a hint whose item the shop doesn't offer yet only fills in when no
  takeable hint is left (no pointing at what the crew can't reach).
- **Hints** are hand-made flashlight writing from "past crews", two per run (was one; (user, 2026-11-06: "apply", to the anti-pattern review fixes)),
  the first always for a route whose item the shop offers ("WE STOPPED. IT
  BEGGED.", "THIN HERE" on the weak panel, "IT CAN'T SEE WHAT IT CAN'T SEE", "IT GOT COLD",
  "THREE AT ONCE", "THE BOX IS A BOX").

## Five kinds of moment
Design v2 (`docs/design-v2.md`, settled through four critic rounds, `docs/design-dialectic.md`).
Each kind asks the crew a different question, so they never blur: items (what is this for?),
moods (what does the button want?), chores (who leaves the button?), exams in the dark (who can
see?), paths (what if we do the weird thing?).
- **A press only fails in a blackout** (user, 2026-11-04: "the non blackout event shouldnt fail on
  pressing the button.. since blackout is for preventing that"). A mood's refused hit is a dud: a
  dead clack, never a cost. (The Stray's nibbles take points without a press costing them.)
- **One button rule at a time** (anti-pattern 9): a mood or an order. Chores run alongside (they
  never touch the button): one chore slot for 2–3 present subjects, two for 4–8; each chore type
  owns a wall, a sound and a light; two fails resolve 3 s apart.
- **Live games are the default; blackouts are rare** (user, 2026-11-04: "ok makes sense"). Built:
  the only blackouts are the exams that gate milestones (one per stage from stage 3).
- **Moods** (non-minigame events), 40 s (was 25), no line: the cap takes a colour shuffled per run
  (colour says THAT, never WHAT) and a chime; each dud is a clue to which way is wrong. A hit a
  picky mood (Twins, Patience, Contrary, Freeze) lets through scores ×3 (tools and impacts; a bare
  hand stays +1), so cracking it pays and mashing doesn't; a dud still costs nothing. While a mood
  runs only one chore runs, so there is room to read it (all three: (user, 2026-11-06: "apply", to the anti-pattern review fixes)). Twins (place: a
  second button, hits count in pairs within 1.5 s; the other blinks), Patience (tempo: 2 s of rest
  between hits; the glow refills), Contrary (kind: refuses the item that scored most in the last
  30 s; a clank), Freeze (stillness: counts only while every other present subject stands still;
  the cap flashes the mover's colour; a shove blames its owner; skipped at 7–8), Runaway
  (location). Room moods: Low Gravity, Reversed. Each run draws 4 of the 5.
- **Chores** (live minigames): a fail nobody touched is blamed on whoever stood nearest ("Bo was
  closest"; audit 2026-11-06: no punishment without a culprit). Each needs 1–2 bodies off the button, gets worse while ignored,
  fails in the room with a culprit for a slip, and ends with a slam over the culprit. Pressure
  Valve (gauge by the button, wheel on the west wall: E held turns; red bursts, dry is a fail
  too; the last turner), The Leak (a crack wandering the north wall: E held keeps it shut; tape
  holds it 10 s; a full puddle ices the floor; whoever let go), Hot Box (2+ subjects only: one can't lift it; an unordered box, two to
  carry, back into the hatch; bursts on the last holder, who wears soot), Floor Fire (spreads tile
  by tile; crouching on a tile stamps it, walking through carries an ember; the blower fans it;
  whoever spread it), The Stray (a critter nibbling the count; two close at once catch it; whoever
  it slipped past), Hot Potato (user, 2026-11-04: "hot potato only fines whoever holds it at the
  end"). Each run draws 4 of the 6; each gets meaner per stage.
- **Exams** (blackouts) gate the milestone from stage 3: at the goal the count freezes ("full"
  clanks), the lights die and the exam runs. Pass: the milestone lands. Fail: the ceiling slams
  over the culprit, the count drops 5%, it replays 30 s later. Solo crews skip them.
  - **The stakes are said with the run's first exam** ("Pass, and the milestone is yours. Fail,
    and the ceiling visits whoever failed."), not repeated on replays (gap review 2026-11-06).
  - **A blackout starts with a briefing** (user, 2026-11-04: "the instruciton is so fast i cannot
    process in time"): cover down, the rule and stakes said and shown, 3-2-1.
  - **The seat is a person:** whoever stands in the spotlit circle at "go" (else the nearest) gets
    a white glare until they press; the signal is drawn only on the screens of readers, more than
    4 m from the seat.
  - Blink Count (how many: a far lamp blinks N times; press exactly N), The Hunt (which: four
    buttons by the walls, the answer written where only a flashlight shows it; two free
    flashlights), The Maze (which path; a walker who leaves is replaced by the nearest subject, from the start; user, 2026-11-03: "blackout can bend the room shape": the
    seat is moved to a corner; walls only they collide with; readers see the outline and three
    hazard cells; two zaps lose), Sequence (who, in order: a subject who leaves loses their turn; colours light up; presses must come from
    those subjects in order, each stepping into the circle). Each run draws 3 of the 4.
  - **Greedy Press** is the stage-8 gate (user, 2026-11-03: "whoever presses in the first 10 s
    wins, the rest lose", with a hidden 20% chance only the presser loses): the first press opens
    the exit; if the button lies the ceiling slams on the presser and it replays.
- **Cursed button** (user): a black second button appears in silence once per run (50%); pressing
  it adds a quarter of the wallet. No prompt, no announcement, no tag (user, 2026-11-03: "fix it").
- **Hog and slacker:** a subject who answers most exam presses is grabbed by an arm from the
  ceiling (once per run); a slacker gets the cone (user, 2026-11-03).
