# Moonsick: design (source of truth)

Online co-op with betrayal for 4–8 friends, with one player hosting.
One full-moon night in a mansion where friends keep starting to turn into legendary creatures.
The name is Moonsick (Claude); the runner-up was Turncoats.

Tags: **(user)** is the user's own words or decision; **(Claude)** is Claude's call and free to change.
Nobody has played it with people yet, so every number is a starting value to tune.
Sections marked **(off in step 1)** describe rules that are switched off for now.
The history is in the critic reports (`docs/critic-*.md`) and in `~/Playground/game-design-research/research_notes/Full Moon/`.
That folder holds the first version of this design (`design.md`) and the user's later pillars (`user-pillars-2026-11-12.md`).

## The core (user, 2026-11-14)
Bluffing is the core mechanic: "knowing when to bluff and how to keep cooperation", "a new type of game", "or genre" (user).
The design in progress for it: `docs/bluff-research.md` (everyone a little sick, the "act" key, rough veins, trading).

## The game in one sentence
(Claude's wording, rewritten 2026-11-15 for the symptoms design.)
Through one full-moon night in a dark mansion, everyone is a little sick, and friends keep starting to turn into werewolves.
Each symptom on a friend has its own item somewhere in the house; bring it in time, because nobody can treat themselves.
A friend who fully turns knocks friends down and eats whoever stops moving, then becomes human again.
Whoever is alive at dawn wins.

- **Job:** watch each other for symptoms, fetch the items (coffee, bucket, razor, bone...) and give them.
- **Choice:** go for a friend's item yourself, or promise to and not come back (the coffee lie saves you a trip, never points).
  With a werewolf out, stand still to give or save someone, or keep moving and stay safe.
- **Goal:** be alive at dawn, each player for themselves.

## Step 1 cuts (user)
Step 1 is a cut-down core version of the game (the plan is in `docs/core-thesis.md`).
It only removes things: everything below is off in every mode, practice and online.
The code and the sections further down stay, so each feature can come back one at a time.

- **Switches:** `scripts/core/features.gd` holds `RULES` and `GAME`.
  Each host NightSim copies `RULES` into `sim.rules`, and a test can turn one on for its own sim.
  Each peer reads `GAME` for the game and the screen.
  `--features=a,b` turns some back on for one run.
- **Rules off:**
  - tools: silver spoons and thermometers never spawn, and tool signs are never read (`tools`)
  - pans and knocking out (`pans`)
  - tricks (`tricks`), scars (`scars`) and the pond's cold reading (`pond_cold`)
  - creature powers (`powers`)
  - moonlight speeding up a case (`moon_speed`)
  - at the turn: the head start for those near (`near_head_start`), showing those far (`far_shown`), and the head start for whoever tried the right cure (`mark_head_start`)
  - the curer's 90 s protection (`curer_protection`)
  - two cases at once (`doubles`)
  - quick chat 5–8 (`chat_extra`); 1–4 stay
- **Practice:** one practice night with the online rules, 6 min long.
  There's no lesson picker, no staged rules and no next lesson at dawn (`lessons`), and no coach line or "New:" lines (`coach`).
- **Screen off:**
  - the notes log on Tab (`notes`)
  - the % sign table (`sign_odds`), so Tab shows a plain table of each monster's felt signs, seen signs and cure
  - the floor plan (`floor_plan`), the 3-line feed (`feed`) and the look readout (`look_readout`)
  - result banners (`banners`) and toasts (`toasts`), so refusals like "too far" are silent
  - the red danger edge (`danger_edge`); the heartbeat stays
  - the words next to the hand icons (`hand_text`)
- **No screen UI and no text during the night, not even the crosshair, item names or room names (user).**
  `screen_ui` off hides every on-screen element during the night: the crosshair, hand icons, bars, prompts, status lines and Tab.
  Full-screen effects stay (out cold, moonlight sting, the hunter's red view), and so do the Esc menu, the dawn screen, the reel and the main menu.
  `world_text` off removes item labels, doorway signs, name tags and speech bubbles.
  So nobody sees quick-chat claims any more, the bots' included.
  The creature's sense outlines lose their names, which bends the user's pillar of outlines with names.
- **Kept:** dark veins, holding, giving cures, shoving, senses, hunger, catching, dawn, the reel, voice and networking.
  In-world bursts and the creature's sense outlines stay too.
  Bots skip the steps for tools and pans, since they find none.
- **Items glow when you can pick them up (user).**
  The nearest item within reach (2.08 m, the host's range) and within 70° of where you look glows with a rim light.
  E or an empty hand's mouse button takes it (see "Hands").
- **Werewolf only (user).**
  The `vampire` and `troll` switches are off, so every case is a werewolf and only wolfsbane grows (in the pond beds).
  Bots cure on the first sign, since only one monster is left to guess.
  The vampire and troll code, signs and tests stay, and the tests switch them on.
- **Pillars step 1 bends:** tools to diagnose, knocking out, creature powers, and the % per sign on screen.
  The full list is in `docs/questions.md`.

## Movement (user asked; Claude's numbers, tuned to the user's feel)
`scripts/core/move.gd`, tested in `test/unit/test_move.gd`.

- **Speeds:** walk 4.32, sprint 8.64, crouch 2.16 m/s.
  Running is twice walking (user).
  Creatures run at sprint × their factor, and bots run a touch slower.
  The host allows 0.6 m of lag.
- **Speeding up and stopping:** 30 m/s² on the ground (a full walk in ~0.15 s), and friction 40 m/s².
  A sprint drops below 1.2 m/s in ~0.19 s, so holding still for a cure stays easy.
  Steering in the air is 20 m/s² (the user wanted more air control), with no air friction.
- **Crouch** (hold Ctrl or C): a 1.15 m body that fits under tables, with quiet steps.
  You stand up only when there's room above you, and a wall you lean on doesn't keep you crouched.
  No crouching in the air (user).
- **Slide:** crouch while faster than a walk, at 4.6 m/s or more (the user wanted it easier to start).
  Shift can already be let go.
  It starts at least at run speed and adds 1.2 m/s over 0.15 s, up to 11.5 m/s (the user wanted it smooth, with half the first boost).
  It slows only 2.5 m/s² (the user felt too much friction) and steers toward where you push at 1.6 rad/s.
  It ends below a walk, after 1.4 s, or as soon as you let go of crouch (user), and keeps its speed.
  The next slide waits 1 s.
  A slide makes noise like a sprint, and the view doesn't bob.
  Creatures never crouch or slide.
- **Jump** (Space): 4.2 m/s, about 0.9 m high.
  Coyote time is 0.1 s and the buffer 0.12 s (research says 80–150 ms).
  A jump out of a slide keeps its speed and adds 0.3 m/s (user).
  Speed above a run fades at 10 m/s² on the ground instead of snapping back.
  The best slide-and-jump chain stays slower than the slowest creature (troll 9.94 m/s), so a slide is a dodge, not an escape.
  A jump from a crouch needs room to stand.
- **Others see** you squat when you crouch and lean back low when you slide.
  The pose carries a mode: 0 stand, 1 crouch, 2 slide.
- **The ceiling** is 4.2 m (user).
- **Mouse look** uses screen pixels (`screen_relative`, as in Deathly Reality Show and Hordeline), so fullscreen at 4K keeps the same sensitivity.
- **A dropped item** falls from hand height to where the host put it, tumbling (looks only).

## Pillars (user)
All pillars are the user's, except the one line marked (Claude).
- Friends in a mansion with a garden and a tree house, through one full-moon night; whoever survives the night wins.
- Every now and then a random player starts turning into a legendary creature.
  The signs are always different and hard to read, with a common pattern and a % per sign.
  Tools are needed to diagnose.
  The cure works only if the diagnosis is right, and then only with a % chance.
- Holding or knocking out a friend is allowed.
  Holding no longer slows turning; it only pulls a friend so they can't escape (user, 2026-11-14; code still has the slow).
- Two can be turning at once, but rarely, and only one can be a creature at a time.
- Each creature has its own powers and its own ways to deal with it.
- A creature must catch a player or die; the caught player dies and the creature turns human again.
- The game is dark, with no flashlights, candles or lamps; moonlight is the only light.
  It isn't pitch black, because friends must see faces to read signs (Claude).
- Betraying must never pay more than curing, and trust must matter until dawn.
- Bluff from both sides: a sick player can lie about what they feel, and a curer can sabotage or leave someone as bait.
- Catching someone is the norm.
  Trust is lost by choices (chasing one particular friend, panning a friend as bait, lying), not by results the rules force.
- The hunter chooses its victim freely, with no takeover and no pull.
- No cloud servers: one player hosts.
- No ghosts, and the game never exposes liars, not even at the end.
- A highlight reel of the night at the end, from everyone's view.

## Terms
- **Case:** one friend's sickness, from its first sign until they are cured or fully turned.
- **Inner sign:** only the sick player feels it, on their own screen.
- **Outer sign:** only the others see it, on the sick player's face or neck.
- **Tool sign:** it shows only through a tool, to whoever holds it.
- **Trick:** a fake inner sign the house plays on a healthy player (Claude).
- **Cure:** wolfsbane (werewolf), garlic (vampire) or rowan (troll).
  Given to a friend, it cures with the case's odds; held up, it shoves its own creature back.
  It isn't meant to test anything, though a right cure that fails still shows the kind was right (known and accepted).

## Taught to a new player
The loading screen and the journal teach 3 rules:
1. Friends will start turning into monsters. You can't see your own face (except in a mirror), and only you feel your inner signs: tell each other.
2. Every sign rules out one creature (the journal shows which). Give the right cure: sooner is stronger; a wrong one makes it worse.
3. A friend who fully turns must catch someone or starve. Hold up its cure to shove it back.

Everything else is shown in the world or found by playing.

## The werewolf's attack (user, 2026-11-14; built 2026-11-15, untested by the user; replaces the catch below)
- Reach and aim (user 2026-11-15: "farther and bigger, with an attack animation"): the strike reaches 2.4 m (was 1.36) and hits a body up to 1 m off your aim (a friend's aim: 0.55) (Claude numbers). Each strike shows a 0.35 s claw swipe across the wolf's front with a forward lunge; your own strike kicks your view (Claude).
Code: `scripts/core/wolf_attack.gd` (tested in `test/unit/test_wolf_attack.gd`), switch `wolf_attack` in `features.gd` (on).
- The werewolf can't catch like a human (user).
- It attacks: a hit knocks the friend back with junky physics, and they can't use their body for a while, a
  recovery state (user).
- It can only eat a friend who stays still, and eating is immediate (user).
- "Not moving" means both: a friend standing still, and a knocked-down one (user).
- Follows (Claude): a friend standing still for a 2 s give can be eaten, so giving with a werewolf near is a risk.
- Follows (Claude): pulling a caught friend free (OK'd earlier the same day) is gone with the catch; dragging a
  knocked-down friend with a hold keeps them moving, so friends can still save them.
- **Not moving (bluff-research round B):** under 1 m of path in the last second; walking in a circle counts as moving.
- **Numbers (Claude):** the hit throws the friend away from the wolf at 11 m/s with a 4 m/s hop (about 2.4 m), and
  they're helpless for 3 s: no moving, no hands, a raised cure drops, a friend they held is let go. The wolf waits
  1.5 s between strikes, so a hit is never an eat a moment later: friends get about that long to grab and drag.
  The strike uses the old catch's reach (1.36 m); a raised wolfsbane still shoves it back.
- **Who sees it (Claude):** the knocked friend lies like a knocked-out one (eyes shut); everyone hears a bonk.
  An eat counts as the catch (back to human in 10 s).

## Symptoms and their items (built 2026-11-14, untested by the user; replaces the signs and curing below)
The user asked "implement all items and symptoms"; the table and whose idea each row is: `scripts/core/symptoms.gd`.
The design and its decisions: `docs/symptoms-thesis.md`. The switch `symptoms` in `features.gd` (on) turns it off.
- **A case (Claude, the thesis's answer A; the user never picked an answer):** three different symptoms of the eight,
  the next one every 30 s at dusk down to 8 s at dawn. Each one showing and untreated raises the curse 1/120 per
  second at dusk up to 1/40 at dawn; ~~held ×0.75~~ removed (user, 2026-11-14; removed from the code 2026-11-15). At 1 the friend turns (veins as before).
- **Treat (user):** give the symptom's item (the hands' give, 2 s). Its symptom ends at once; all three = cured.
  The sunglasses, the dog cone and the walker stay on until the case ends (Claude).
- **A wrong item (user 2026-11-14):** never speeds the curse. It's used up with a slapstick burst, and so is an
  item given before its symptom shows. Wolfsbane given to a patient is a wrong item; it stays the shove.
- **Who sees what (Claude unless tagged):** everything shows to others, nausea too (the friend retches and looks
  green; the user parked private symptoms). The patient feels sleepiness (the view dozes off on each yawn), nausea
  (a green, swaying view and a gurgle) and walking on four legs (a low view). The awoo is a friend's small voice,
  not the turned werewolf's howl (user). The host sends each yawn, retch, awoo, slurp and buzz, so everyone gets it
  at once.
- **Where the items are, two of each, back 60 s after use:** sunglasses on the hall coat rack, razor on the study
  desk, dog bone at the garden doghouse, coffee on the kitchen counter, bucket by the cellar crates (the thesis);
  perfume on the dining sideboard, walker in the conservatory, dog cone on the garden bench (Claude).
- **Bots (Claude):** they notice symptoms they can see (an awoo from 15 m), each takes a different symptom of the
  patient, fetches its item and gives it; up to three on one patient.

## The signs (user's %, Claude's table)
Each sign rules out one creature.
One sign leaves two creatures, and two signs from different rows leave one.
For inner and outer signs, the % is the chance that sign is the one of its pair that shows first; every case shows all four of its inner and outer signs by stage 3.
For tool signs, the % is the chance the sign is there at all in that case.

| Rules out | Inner (patient only) · grows near | Outer (others see) | Tool (holder sees) |
|---|---|---|---|
| **troll** (werewolf or vampire) | night sight: the dark looks lighter · in dark rooms · W 50% V 70% | eyes shine in the dark (same pale shine for both) · W 40% V 70% | silver spoon: the skin reddens · W 70% V 40% |
| **werewolf** (vampire or troll) | moonlight stings: your view blooms white · in moonlight · V 70% T 40% | grey skin with stony cracks (needs moonlight to see) · V 50% T 70% | thermometer: cold · V 60% T 60% |
| **vampire** (werewolf or troll) | you crave raw meat: your view drifts to it · in the kitchen · W 70% T 50% | drooling (needs moonlight to see) · W 40% T 70% | (none) |

- **What the signs tell you:** after one sign the likelier creature is 51–55%, after a second sign from the same row ~58%, and after signs from two rows it's certain.
- **Schedule:**
  Stage 1 (the first third) shows one sign, inner or outer at random.
  Stage 2 shows one sign of the other kind, and dark veins start up the neck.
  Stage 3 shows the second inner and the second outer sign, and the veins reach the face.
  Then the friend turns.
  Tool signs can be read from the start; each one is there or not for the whole case, by its %.
- **Dark veins** show how late a case is, the same for every creature.
  They're on the neck, so the sick player can't see their own.
- **Look-alikes (Claude; off in step 1):**
  - **Tricks:** when a real case starts with an inner sign, 70% of the time the house plays one fake inner sign on a healthy player within 40 s.
    The trick lasts a random 4–25 s and doesn't grow near its trigger.
    It never hits a sick player or anyone cured in the last 60 s.
  - **The pond:** anyone who stood in the pond beds in the last 30 s reads cold.
  - **Scars:** a friend cured after stage 1 keeps one outer sign for the rest of the night.

## The night (Claude's numbers)
- **Length:** 12 minutes.
  Pressure rises all night: cases come sooner, with more doubles and more tricks.
- **Cases:** the first starts at a random 0:20–1:30.
  The next starts GAP after the last case ended, where GAP = 90 s ÷ √(living) × random 0.25–1.75 × RAMP.
  RAMP goes from 1.3 at dusk to 0.7 at the end.
  Each death makes everyone left sick more often: the gaps alone come to about 1.5 min per person, or 3.7 min with 6 alive, plus case time.
  Each case picks a random living player, skipping anyone cured or turned back in the last 60 s.
- **Two at once (off in step 1):** 10% of cases early in the night and 20% late start a second case 10–30 s in, so it stays rare (user).
  Never more than 2 at once.
- **Case length:** 75 s at dusk, 60 s by the end.
  Moonlight on the sick player speeds the case ×1.5 (Claude).
  The curse comes from the moon, and you need a moonbeam to see grey skin and drool, so seeing them makes them worse.
- **Cure odds** slide with progress p from 0 to 1: 30% + 65% × (1 − p)^1.5.
  That's 95% at the start, 65% at a third and 30% at the end.

## Curing
- **Give a cure:** 2 s with one hand, on a friend who holds still, is held or is knocked out.
  The cure is used up.
  - A right cure works with the odds.
    A failed roll makes the sick friend shudder, which shows the kind was right.
  - A wrong cure jumps the case a third ahead, and the signs due in that time burst out.
    Past the end, the friend turns at once.
    Everyone sees whose cure it was.
  - A healthy player just eats it.
- Nobody cures themselves, except the last one alive (taught when it happens).
- **Cure spots (Claude):** wolfsbane ×2 (pond beds in the garden), garlic ×2 (kitchen, cellar), rowan ×2 (the tree house's tree, the wreath on the front door).
  A spot regrows 120 s after its cure is used up.
  Cures can be dropped, and at most 2 of a kind exist, held ones included.
- **Tools (Claude; off in step 1):** 2 silver spoons and 2 thermometers, at random spots each night.
  Reading one takes 1.5 s, on someone else.
- **Carrying (Claude):** each player has two hands, each holding one item (a cure, a tool or a pan).
  Knocked-out players keep their items, so panning someone never pays in loot; the dead drop theirs.
  A dropped cure keeps its spot from regrowing.

## Hands: one mouse button each (user; Claude's details)
Built, not committed yet: `scripts/core/hands.gd`, tested in `test/unit/test_hands.gd`.
The spec is the last synthesis in `docs/hands-thesis.md`.
- LMB is the left hand and RMB the right hand; there's no active hand.
- A press does what that hand and the world allow:
  - An empty hand reaches for the glowing item and comes back with it.
    E does the same, left hand first.
  - An empty hand aimed at the item in a friend's hand takes it from them, at a hold's reach (user 2026-11-14:
    "a player is able to steal other player if abel to aim to their object"; instant, Claude).
    If they hold their button on it (giving, charging a throw, raising), it's a tug instead (user: "players can fight
    for items.. only if the player is hodling click"): keep your button down, and the one who walks away while the
    other stands still gets it, as with holding (Claude: 1 m past where it started; both walking off, it flies loose;
    nobody pulling for 4 s, the owner keeps it). Letting go of your button gives it up. Bots never steal or hold on.
  - A hand with an item and nothing to do with it: hold to charge a throw, let go to throw; a quick click drops it
    (user 2026-11-14). Full charge in 1 s, 4.5 to 19.5 m/s, 10° above your aim (Claude; user: 50% stronger, more arc); the host stops the arc at the first wall or
    furniture and it falls to the floor; nobody can take it while it flies.
  - An empty hand aimed at a friend holds them while its button stays down (user).
    A friend under your aim beats a glowing item.
    The hand lands on the spot of their body you aim at and sticks there as they move (user).
- Every hand's reach is 20% shorter than before (user): hold 1.44 m, pick up 2.08 m, give 1.84 m, catch 1.36 m.
  - A cure is raised while its button is held, when a creature is out or turning.
  - Otherwise a cure is given by holding 2 s on a friend; the last one alive, with nobody near, eats it.
  - A creature catches with either button.
- Give and eat start only on a fresh press; the only switch while a button is held is into raise.
- One give and one raised cure at a time.
- G drops one item per press, left hand first (Claude).
- A hand shows only while it reaches, holds, gives or raises (Claude's reading of the user's wish).
- While you hold a friend, your other hand can't give, take or raise.

## Holding and knocking out (user; Claude's numbers)
- **Holding is a chain (user; spec `docs/holding-thesis.md`):** an empty hand on a friend within 1.44 m holds them (see "Hands").
  ~~Their case runs at half speed.~~ Removed: holding only pulls a friend so they can't escape (user, 2026-11-14; removed from the code 2026-11-15).
  The chain is as long as the gap when the hold began, at least 1.2 m.
  For the first 0.5 s the hand grips and the friend can't move; then they can walk (no sprint).
  When the holder walks away from the friend, the friend is dragged after them (user).
  When the holder stands still and the friend walks off, the chain snaps 2 m past its length (about half a second at a walk) with a loud noise (user).
  After a snap, that friend can't be held again for 3 s (Claude).
  The holder walks at most at a walk, and at half a walk while the friend pulls the other way (Claude).
  Nobody caps how long a hold lasts yet (Claude; watch for griefing in the playtest).
- **Knocking out (off in step 1):** a pan (2 in the house) knocks a friend out for 20 s.
  Their case runs at a third of the speed, their screen goes black (nothing to report), and their eyes close (eyeshine hidden).
  After waking, nobody can knock them out again for 20 s.
  Pans do nothing to creatures.

## Turning and the hunt
- **The turn:** at the end of a case the friend turns over 2 s.
  A holder is thrown off, and nobody can be caught during the turn.
  Every sign shows.
  A second case that reaches its end while a creature is out waits there, curable at 30%, until the creature is done.
- **Hunger (Claude):** (20 s + 60 s ÷ people left to catch) × the creature's factor (werewolf 0.75, vampire 1, troll 1.25).
  The body shows it: it thins and its eyes dim.
  Out of time, the creature starves and dies for good.
- **Catch:** the creature holds a player for 2 s, and the caught player dies.
  A friend breaks the catch by shoving with that creature's cure.
- **The catch is the same chain as holding (Claude, OK'd by the user; switch `catch_link`):** the creature's hand lands where it aims and holds the victim on a chain.
  For the first 0.5 s the hand grips and the victim can't move; then the victim can walk (no sprint).
  The creature pulls by walking away from the victim, which drags the victim along (no more planted feet).
  If the creature stands still or backs into a wall, the victim can walk off, and the chain snaps 2 m past its length; the victim is then safe from catches for 3 s.
  With the switch off, the victim can't move (the first catch).
- **Turning back:** after a catch the creature has 10 s to turn back (user), at people's speed, with no catches and no powers.
  A second catch could only reach the helpers next to the first, so it's off; `--multikill` turns it on for testing.
- **Shove (Claude):** holding up a creature's own cure shoves it 3 m back when it comes within 2.3 m in front of you.
  Then that cure waits 3 s.
  2.3 m reaches a catch that starts at its farthest.
  Holding a cure up halves your speed, so one armed player can't just walk backward forever; two armed players cover each other.
- **Speed (Claude):** werewolf 1.3×, vampire 1.2×, troll 1.15×.
- **Powers (Claude, Space; off in step 1):**
  - **Werewolf howl:** everyone hears it, and whoever moves within 30 m in the next 3 s shows, so the answer is to stand still. Every 25 s.
  - **Vampire leap:** a loud high jump that reaches the tree house. Every 10 s.
  - **Troll stomp:** everyone within 3.5 m is knocked back, and their raised cure is lowered for 1 s. Every 12 s.
  - No powers while holding someone or while turning back.
- **Senses (user: outlines with names; Claude: what shows you):** the hunter sees people as outlines with their names when they trigger its sense.
  - Everyone within 3 m shows, and so does any noise within 20 m for 3 s (sprinting, a pan hit, a dropped item).
  - **Werewolf smell:** footprints of the last 10 s within 20 m glow, the newest with a name; wading the pond leaves none.
  - **Vampire heartbeat:** anyone within 20 m whose heart races, because they sprinted in the last 5 s, were hit, are sick, or are within 6 m of the vampire.
  - **Troll sight:** anyone standing in moonlight within 25 m, outdoors or in a window's beam.
  - So each creature is dealt with differently: wade the pond and stand still (werewolf), stay calm (vampire), stay in the dark (troll).
  - Moonlight slows no creature, because a moonlit garden would be a fortress.
- **Helping beats fleeing (the user's ask; the critic's rule):** at the moment a friend turns,
  - everyone within 8 m of them gets a 5 s head start (they can't be caught);
  - everyone more than 15 m away shows to the creature anywhere for 10 s (the curse remembers who ran);
  - whoever tried the right cure on them (it shuddered) gets a 10 s head start.
  - A head start is never immunity, and the creature sees who has one (a blue outline).
  - A cure that works keeps the curer from getting sick for 90 s, and the curer is shown this.
- **After the catch or the starving,** the case is over.
  A catch gives exactly what a cure gives (back to human, 60 s skip), so nobody is ever safe and everyone needs friends until dawn (the user's trust pillar).

## Death, dawn and winning
- The dead watch from just behind a living human, at their eye height.
  They never watch from a creature or through anyone's eyes, so private signs stay private and the dead can't scout the hunter.
- **Dawn:** everyone alive wins, a creature still out included (the sun lifts the curse), and the dead lose.
  The end screen shows the night's toll ("4 of 6 saw dawn") and the story of the night.
- **Last one alive:** plays on, can cure themselves, and wins at dawn.
  If they turn, nobody is left to catch, so they starve.

## Trust and bluff (user's pillars; Claude's reading)
- There's no trust meter.
  Trust is what friends remember: claims that match the body, whose cure it was, who swung a pan at whom, whom a creature went out of its way to chase, and where people stood when a friend turned.
- Trust is spent on whose case goes first when two are sick, who gets the last cure of a kind, believing a claim or checking first, letting someone hold you, and standing near someone whose case is near its end.
- For the sick player, being cured (alive, trust kept) beats turning and catching someone (alive, trust maybe lost), which beats starving (dead).
  So curing always beats betraying, and once turned, hunting beats starving.
- Lies come from fear (a sick player hides a sign so they don't get panned) and from the turn moment (who gets eaten), never from a reward.
  Also from saving a trip: breaking "I'll get your coffee" saves time, never points (user OK 2026-11-15: "add it").
  Tricks make honest players look like liars.
- **Quick chat (Claude):** keys 1–4 say "I feel night sight / moonlight stings / I crave meat / I feel fine".
  5 says "look at <who you aim at>!", 6 and 7 say "my tool says YES / NO", and 8 says "RUN!", so watchers and tool holders can talk too.
  Speech bubbles show over your head.
  Anyone can lie, and quick chat works without voice and lets bots talk.
  It never shows in the story.
- **Bluff rules, stripped after critic round 1 (user 2026-11-15: "strip the rules"; not built):**
  The goal stays the job lie ("I'll get the coffee", then not coming back), but it's a goal, not a rule.
  - Bots: fear makes a bot bail late in a case; a bot trusts a friend by the gives it saw itself, and never tells anyone.
  - Bots offer deals in bubbles with item icons and words, no arrows: "[bucket icon] for [coffee icon]" (user). The human's way to offer a deal to a bot is open (questions.md Q-B4).
  - Cut: the chain snap and the wrong item (already built or the user's rules), holding back a cure as a trade (it's hoarding, and steal breaks it), the refilling spot (the item count shows what's gone), and the swap (already built, and the tug makes it unsafe).
  - Moved to questions.md: whether a friend thrown off at the turn can run (only matters for the new attack).
- **Everyone a little sick (Claude's numbers, user OK 2026-11-15: "add it"; built 2026-11-15, untested by the user;
  `sims/mild_sick.py`, `scripts/core/mild.gd`, switch `mild_sick` in `features.gd` (on), needs `symptoms`):**
  - Every living friend gets one mild symptom every 90–180 s, one of the 8, shown like a case symptom.
  - A mild symptom does nothing for 45 s; left untreated for 45 s, it starts a full case on that friend, with it as the first symptom.
  - A friend treats it with its item; nobody treats themselves (built). The random cases stay as they are.
  - About 5 mild symptoms per friend a night. The coffee lie lives here: 45 s fits a far trip (27 s) with 16 s spare, and a full case doesn't (19 s per item mid-night).
  - Built details (Claude): a friend's 90–180 s clock pauses during a case and for the 60 s after a cure, and starts
    again after each mild symptom ends. A mild symptom has no veins (it isn't a case yet). A wrong item bursts, as on a
    case. A random case on a friend with a mild symptom takes it as its first symptom. Bots treat mild symptoms like
    case symptoms, and a bot with one waits by a friend for help.

- **The rest of the bluff todo (built 2026-11-15, untested by the user; `docs/bluff-all-thesis.md`, critics
  `critic-bluff-all-r1..r3.md`):**
  - Items stay carried, two hands (Claude, simulated in the thesis): cures as places would drop steal/tug and the deal
    bubbles, both the user's; one hand would break the user's two-hand design. 8 items stay; empty spots at 8 friends
    are a playtest check.
  - You feel your symptoms, never your progress (already true). Two wall mirrors show you your own body, veins and
    symptoms: the study's south wall and the dining room's north wall, each beside a moonlit window (Claude; the user
    offered mirrors; switch `mirrors`). Moonlight costs nothing there, since `moon_speed` stays a step-1 cut.
    This bends taught rule 1 ("you can't see your own face"): except in a mirror.
  - Turning early: **cut, not built** (critic r1: it pays more than curing; questions.md Q-B6). The head start stays
    off (Q-B3 open).
  - Bots (Claude unless tagged): each bot has a nerve (veins 0.35–0.75) and walks off from a patient past it, whatever
    its trust (user OK: "fear makes a bot bail"). It trusts a friend +1 for each treat it saw in sight (12 m, a line of
    sight), helps trusted patients first, and never tells (user OK). A friend who broke a deal with it gets no help from it.
  - Deal bubbles (user): a sick bot holding the item a person near it (5 m) needs shows "[that item] for [the item it
    needs]", when the needed item lies within 25 m of that person. A bot that trusts you gives first, so you can take
    it and not pay back within 45 s (the coffee lie with a bot); then it never deals with or helps you again. A stranger
    pays first. Other bots leave that symptom to the deal.
  - The human's offer (Q-B4, Claude's pick built): holding out an item toward a sick bot (the give's reach) makes it
    stand still for it, only while no creature is out.

## The story of the night (user's highlight reel)
- **First version (Claude):** after dawn, a timeline of the night's moments with who did what ("3:05 Ana gave Bo garlic. Wrong.").
  It shows only what others could see: never inner signs, and never what a creature was.
- **Built:** an in-engine replay of up to 6 moments (catches, saves, wrong cures, pans, turns), recorded 5×/s.
  Each moment opens wide, then shows the actor's eyes, then the other's, with private screen effects off.
  When the host starts it, everyone in the night watches the same moment together, and the host moves everyone on, like Gartic Phone (user).
- **Later:** optional voice in the reel, with everyone's consent.

## Hosting and voice
- One player hosts over Steam P2P (a GodotSteam lobby) or by address (ENet), with no cloud (user).
- In-game proximity voice is built: creatures sound deeper, the knocked-out are silent, and the dead are heard flat.
- No rule depends on voice, and anything Discord allows, the game allows (Claude).
  Phasmophobia shows that punishing in-game voice pushes players to Discord.

## Look and feel (Claude)
- Funny-scary like Lethal Company and Content Warning, not real horror: deaths are slapstick and signs are big and readable.
- A moonlit blue palette, with very dark interiors, window beams and a silver-blue garden.
  No warm light anywhere.
- **Light (the user found it too dark):** compared with the first build, ambient is 2×, walls and ceilings 1.3×, floors 1.4× and the sky 1.3×, and window beams went from 4 to 5.5.
  Interiors are ~3× brighter on screen (mean luminance: hall 0.13, cellar 0.07), the garden 1.07×, and nothing clips.
  The see-through beam boxes are gone (user), and the lit floor patch shows the moonlight.
- **Characters:** one chunky stylized body with a big face, so eyes, mouth and neck read at 2–5 m.
- **Creatures:** static, hunched Meshy models with their own silhouettes (a shaggy werewolf, a thin caped vampire, a hulking mossy troll).
  The code look (fur, grey skin or tusks) is the fallback.

## The mansion (Claude)
- The hall has the front door with the rowan wreath.
- The kitchen has garlic and raw meat on the table.
- The dining room, the study and the conservatory.
- The cellar, down a ramp, has garlic.
- The garden has the pond with wolfsbane beds, and hedges.
- The tree house sits on a big rowan tree, up a ramp.

Every cure spot is within ~25 s walk of the hall.
Windows throw moonbeams into every room.

## Practice and bots (Claude)
- Practice mode is you plus bots.
  Sick bots say their inner signs in quick chat.
  Bot doctors read only what a player could (reported signs, outer signs they can see, tool readings) and pick by the journal's %.
  Bot creatures hunt by their senses.
- Practice doubles as the tutorial, and bots don't fill seats in online games.
- **First cases:** the first case lands on a bot at 25 s and the second on you.
  The house plays no tricks on you before your first real case.
- Bots are honest; `--liar-bots` makes sick bots lie sometimes.
- **Practice lessons (off in step 1):** practice stages the rules.
  Lesson 1 has signs, cures and the creature only (no tricks, scars, doubles, powers or pans).
  Lesson 2 adds tricks, scars and pans, and lesson 3 has every rule.
  Seeing dawn moves you to the next lesson, and the menu can pick any.
  A coach line (practice only) teaches each action once and never names which cure to give.
  It covers picking up, noticing, looking, opening notes and giving; for the sick player, telling and holding still; in a hunt, raising its cure and staying grouped.
  Online games are unchanged.

## Dawn awards (Claude)
- Awards are only for helping: Best doctor (cures that worked), Bodyguard (catches broken), Long shot (a cure that worked late).
- No awards for pans, wrong cures or catches, because those paid for betrayal.

## What each player is shown (Claude; mostly off in step 1)
The plan is in `docs/ux-thesis.md`.
- Each player sees only what they heard (claims within 15 m), saw (outer signs and veins, where distance and moonlight decide, as for bots; scars look like signs) or read (their own tool).
  Never who is sick, and never a conclusion.
- **Notes (Tab):** a log per friend, with each fact tagged with the creature it rules out ("said: craving raw meat (not vampire) 12 s ago").
  A claim fades after 35 s unless veins back it.
  The sign table with its % stays (user pillar).
- **Readout and feed:** a look readout under the crosshair and a 3-line feed.
  Cure results show as a banner for the giver and the sick friend, and as a feed line within 15 m only for results that show on the body.
  Item names show over items, and the hands say what each item does.
- **Map:** each room has its own floor, and signs over doorways name the room beyond and the cure that grows there.
  The room's name shows as you walk in, and a floor plan on Tab shows rooms, cure spots and you.
- **Feel:** bursts in the cure's colour, an FOV kick on a turn, and a red edge and heartbeat when a creature is near.

## Players
4–8 (Claude), tuned for 5–6.
Practice and the dev flag allow fewer.

## Build plan
1. **v0.1 (built):** everything above, including the in-engine replay, in-game voice and one power per creature.
2. **Next:** the user's playtest with 3+ humans, judged by the kill lines below.
3. **Later:** more powers (vampire flight, troll breaks doors) and the art pass (rigged Meshy models).

## Kill lines (Claude)
- By the 3rd night, the crew does the same thing in the first 10 s of every case, so the choice is dead.
- Fewer than a third of cures used an outer sign, so the watchers' half isn't needed.
- In a 4-human night nobody asks "is that real or the house?".
- Every turn ends with a pan, or the same player is bait most nights.
- A good crew loses nobody, or a new crew loses everyone, 3 nights in a row.

## Code rules (Claude, from the code review)
- Every range is measured feet to feet, with a 0.6 m allowance for lag on the host.
- The host syncs shield state, and sends events, snapshots and the reel only to players in the night.
- Nobody is ever told who got sick.
- Knocked-out players can't drop items or chat.
- A hand is locked during a give or a read.
