# MA: action and answer (round 1)

## Method log

**Steps run**
1. Listed 30 acts one player does TO a friend: grab, throw, catch, carry, shove, pull up, tag, blind,
   swap places with, freeze, wake, mark, lift, drop, hide, call, trip, launch, yank, shrink, spin around,
   heal, steal from, hand an item to, shield, steer (take their controls), lock out one button of,
   light up (show) their view, mute, mirror (force them to copy my move).
2. Listed 20 answers made within seconds: grab back, steer mid-air, dodge, brace, let go, pass on, catch,
   call out, duck, jump, use it now, shake off, hold still, push back, reach out, roll, swap back, cling,
   follow, throw back.
3. Drew 22 pairs with `random.SystemRandom().choice` (act and answer drawn on their own). No pick, no
   re-roll. Pairs 17 and 18 came out the same (lock out → jump); both were built.
   Drawn: 1 mute→throw back · 2 freeze→cling · 3 launch→duck · 4 mark→roll · 5 mark→duck · 6 grab→brace ·
   7 pull up→brace · 8 tag→duck · 9 launch→throw back · 10 swap places→throw back · 11 light up view→hold
   still · 12 hand item→shake off · 13 tag→dodge · 14 mark→follow · 15 shield→duck · 16 trip→let go ·
   17 lock button→jump · 18 lock button→jump · 19 freeze→grab back · 20 pull up→grab back ·
   21 catch→reach out · 22 steer→brace.
4. Built one rule per pair where the act lands on one friend and the answer chains onward.
5. Added an in-round reveal to each that changes which friend to act on next.
6. Kept 8, ordered by player-with-player strength.

**Raw count:** 22.

**Gates the raw ideas failed most**
- N / taken list (6): human ladder and cliff pull-up (Heave Ho family), swap-only movement (Totem
  Madness), trapeze catch (Men on the Flying Trapeze), split body (one limb each), flash lighting a
  friend's view (see for others, not yourself).
- P2, the target can't answer (5): freeze, mark→follow, lock button, freeze-frame, possession. When
  the act freezes or steers the friend, they only obey: a pressure plate, not a back-and-forth.
- R plus F1 (4): course pairs (launch, catch, pull up) only vary by physics wobble and need hand-made
  levels.
- Core-rule overlap: acts `mark` and `tag` keep collapsing into one family, "point the threat at a
  chosen friend" (bait, duck shot, armor, lantern). `hand` and `trip` collapse into "pass the hot
  object". Only one or two per family could be kept as truly different rules.

**Swaps (novelty step, one web search per idea)**
1. Swap Only (raw 10) → Totem Madness (jam game: you are a totem that can't walk and moves only by
   swapping places with players or objects) has the same core rule. Swapped in Cursed Hands (raw 12).
2. Trapeze (raw 21) → Men on the Flying Trapeze (Kloonigames: 2-player co-op where you catch each other
   on trapezes) has the same core rule. Swapped in Lantern Pass (raw 8).
3. Lantern Pass (raw 8) → search found Pass The Light (2 teams of 2 share one flashlight they pass in a
   maze): N ~ only. But its rule ("touch passes the state, the enemy targets its holder, the receiver
   dodges") was the same core as MA-4 One Suit, so it broke the 8-different-rules rule. Swapped in Jump
   Pearls (raw 17).

**Novelty results for the kept 8**
- MA-1 Hush Stone: In Silence and HUSHED have a monster that hears your voice; no game found where you
  silence a friend. N ~.
- MA-2 Hooked on Friends: Skyhook's team mode lets you hook teammates to swing; no brace-decides-who-moves
  rule found. N ~.
- MA-3 Duck Shot: nothing close (nearest: Color Cannon Co-op, where you deflect turret shots). N ✓.
- MA-4 One Suit: nothing close. N ✓.
- MA-5 Shield for Others: shields that skip the caster exist as MMO team buffs (City of Heroes); no game
  built on a physical shield that can't cover you. N ✓ to ~.
- MA-6 Fumble: nothing close (a Lethal Company mod has a "can't drop items" curse, no trip release). N ✓.
- MA-7 Cursed Hands: the same Lethal Company mod puts curses on items; no hand-off-and-refuse rule
  found. N ~.
- MA-8 Jump Pearls: Duet (2-player jam game) lets partners trade mechanics, jump included, by agreement.
  Here you take a jump by touch and leave the friend stranded, at 3 to 6 players. N ~.

**Good / bad**
- Good: building every rule from "act on a friend + their answer" made P1 and P3 hold almost by
  default, and P2 held whenever the answer was a real choice (brace or not, duck or step out, keep or
  shake off).
- Bad: random pairs often gave an act that removes the target's choice (freeze, lock, steer), which
  breaks P2. Step 5, the in-round reveal, was bolted on. It is mostly "spawns move + the threat punishes
  the team's habit", so R is the weakest part of most ideas. Two verb families ate most of the space.
- Not checked (assumed): online lag on 1-second answers (brace, duck, catch). Every kept idea needs a
  server-decided window of about 0.5 to 1 s.

## Raw candidates

1. mute→throw back · **Hush Stone**: a blind beast hunts the loudest voice; throw the one hush stone at a friend to silence them (safe, but they can't share what's in their room) until they throw it on. Kept MA-1.
2. freeze→cling · **Gale Ridge**: freeze a friend into a rooted anchor before a gust, and others cling to the frozen friend. Fails P2 (a frozen friend can't answer).
3. launch→duck · **Cannon Crew**: fire a friend from your body-cannon through blade gates; the flyer ducks mid-flight, lands, and becomes the next cannon. Fails F1 and R (hand-made courses, wobble only).
4. mark→roll · **Bait**: mark a friend and the beast chases them; they roll-dodge, lead it into traps, then pass the mark. Strong P; same family as Duck Shot, so not kept.
5. mark→duck · **Duck Shot**: the turret fires at the friend you dot; they duck at the last instant so the shot hits the fuse box behind them. Kept MA-3.
6. grab→brace · **Human Ladder**: climb up braced friends to reach ledges; brace late and the climber falls. Fails N (Heave Ho, PICO PARK).
7. pull up→brace · **Hooked on Friends**: hooks stick only to teammates; whoever is braced stays and the other is reeled in. Kept MA-2.
8. tag→duck · **Lantern Pass**: one lamp shows traps around its holder and passes by touch; sentries shoot the holder, who must duck behind cover. Kept, then swapped out (same core as MA-4).
9. launch→throw back · **Over the Wall**: launch a friend over a wall to grab loot and throw it back before the guard turns. Fails R (the best thrower always goes) and F1.
10. swap places→throw back · **Swap Only**: nobody walks; you move only by swapping places with a friend you can see, who lands in your trouble. Kept, then swapped out (Totem Madness).
11. light up view→hold still · **Flash**: your flash lights only the friend you aim at; they see, but the stalker sees them, so they must hold still. Fails the taken list (see for others, not yourself).
12. hand item→shake off · **Cursed Hands**: push a cursed relic into a friend's hands; they keep its curse or shake it off and crack it. Swapped in as MA-7.
13. tag→dodge · **One Suit**: only the friend wearing the armor can hit the giant or be hit; touching a friend jumps the armor to them. Kept MA-4.
14. mark→follow · **Ghost Trail**: mark a friend and your body auto-walks their path 2 s behind. Fails P2 (the follower only obeys).
15. shield→duck · **Shield for Others**: your shield can't cover you, only the friend you raise it in front of, who must crouch behind it before the volley. Kept MA-5.
16. trip→let go · **Fumble**: a burning idol sticks to its holder; only a friend's trip knocks it loose, and the holder aims the throw as they fall. Kept MA-6.
17. lock button→jump · **Jump Pearls**: each player's jump is a pearl a friend can take by touch, leaving them grounded while the water rises. Swapped in as MA-8.
18. lock button→jump · **Split Body**: lock a friend's walk so they keep only jump; one walks, one jumps. Fails the taken list (one limb each).
19. freeze→grab back · **Freeze-Frame**: freeze a friend mid-air as a step; when they thaw they fall and must grab back. Fails P2 (frozen means no answer) and F1.
20. pull up→grab back · **Cliff Chain**: reach down to pull up a friend who must grab back as holds crumble. Fails N (Heave Ho, Tied Up) and R (wobble only).
21. catch→reach out · **Trapeze**: flyers let go, catchers hanging by their knees catch; burning bars change the route. Kept, then swapped out (Men on the Flying Trapeze).
22. steer→brace · **Puppeteer**: grab a friend's controls for 2 s; they brace to throw you off. Fails G (one player who sees most quarterbacks) and needs a see-for-others reason (taken).

## Kept ideas

### MA-1 Hush Stone
- Rule (one sentence): A blind beast hunts the loudest voice in a dark house, and the crew's one hush stone, thrown at a friend, silences that friend's voice and steps until they throw it at someone else.
- Fantasy (who you are, what you're doing): Thieves robbing a blind watch-beast's den, each with a candle that lights only their own room, piecing together where the vault is.
- Aesthetic (one line): Candle-lit rooms in black, sound drawn as ripples the beast follows, a blue stone that leaves a glowing trail when thrown.
- Player on player (what my action does to a friend, and what they decide back): The beast turns toward Jun because he's talking. I throw the stone at Jun: he goes silent and the beast loses him, but now he can't tell us what's in his room. Within seconds Jun decides whether to hold the stone and stay safe, or throw it at the next friend the beast turns to, which gives him his voice back. A bad throw silences the friend who was mid-sentence with the clue, or misses, and the beast hears the stone land.
- Why the plan can't settle (what changes round to round because of the players): The beast goes to the last loud voice, so whoever the team leans on as caller gets hunted and the caller must change. The clue pieces (which door, which code) show up in different players' rooms each round, so who must talk, and who must not hold the stone, changes mid-round.
- Hub (the one shared thing everyone uses): The hush stone (always on exactly one person).
- At 3 / at 6: At 3, each player holds a third of the clues and every silence costs a lot. At 6, more voices make the beast switch targets faster, and there is still only one stone.
- Hidden (what, how uncovered, why hide) or "none": Each player's room (clue marks, beast tracks). Uncovered only by saying it out loud. Reason to hide: talking draws the beast. Note: needs in-game proximity voice, since the game must cut a mic.
- A failed run (what happens, who is blamed): Lena hushes Max mid-sentence; nobody hears the door number; Ana guesses, opens the wrong door, and the beast hears the creak. Blame: Lena's throw, seen by its blue trail.

### MA-2 Hooked on Friends
- Rule (one sentence): Your grapple hook sticks only to teammates, and when it lands, whichever of you is braced stays put and the other one gets reeled in.
- Fantasy (who you are, what you're doing): Salvagers crossing a chain of crumbling sky islands where the only solid anchor is each other, carrying a shard to the exit island.
- Aesthetic (one line): Chunky rock islands over a pink sky, bright chains, crack-and-tumble sounds.
- Player on player (what my action does to a friend, and what they decide back): I hook Sam. Within about a second Sam decides: brace (I fly to Sam) or stay loose (Sam flies to me). If Sam's tile is cracking, he stays loose and I pull him out; if I'm the one falling, he braces and saves me. Both braced: nothing happens. Both loose: we meet in mid-air and drop.
- Why the plan can't settle (what changes round to round because of the players): Tiles crack under whoever braced last and longest, so the floor punishes the team's usual anchor. New islands rise in random spots and the shard spawns beside a random player, so which friend to hook changes every few seconds.
- Hub (the one shared thing everyone uses): The hook-and-brace rule (each player is everyone's anchor point).
- At 3 / at 6: At 3, there are few anchors and every hook is a big call. At 6, hooks cross, and two people can hook the same braced friend at once.
- Hidden (what, how uncovered, why hide) or "none": none.
- A failed run (what happens, who is blamed): Ana hooks Ben while Ben braces on a cracking tile; the tile drops and both fall. Blame: Ben's brace on a tile everyone saw crack.

### MA-3 Duck Shot
- Rule (one sentence): The team's only weapon is the factory's own turret, which fires at whichever teammate you put the red dot on, so you dot a friend standing in front of a target and they duck at the last instant so the shot hits what's behind them.
- Fantasy (who you are, what you're doing): Unarmed saboteurs in a robot factory, turning its security turret against its own fuse boxes.
- Aesthetic (one line): Clean white factory, a red laser dot on someone's chest, a rising beep, a slow-motion duck.
- Player on player (what my action does to a friend, and what they decide back): I put the dot on Mia and the turret charges for 1.5 s. Mia decides: stay in line and duck at the end of the beep (the shot hits the fuse box behind her), or step out if she isn't lined up (the shot is wasted). Duck early and the turret re-aims down and hits her; duck late and she's knocked out for 10 s. After the shot, the marker gun jumps to Mia.
- Why the plan can't settle (what changes round to round because of the players): Fuse boxes open in random spots and slide along rails. After two ducks in a row the turret aims low and the friend must jump instead. Patrol robots shove people out of line. Which friend is lined up changes every shot, and the marker role moves with every shot.
- Hub (the one shared thing everyone uses): The turret and its marker gun.
- At 3 / at 6: One turret per 3 players (1 at 3, 2 at 6), each with its own marker. At 6, two dots can land on one friend at once.
- Hidden (what, how uncovered, why hide) or "none": The turret's aim height shows on its barrel, which the dotted friend faces away from. The marker sees it and calls "duck" or "jump". No reason to hide.
- A failed run (what happens, who is blamed): Leo dots Mia while she's still walking; she ducks late and is knocked out, and the last fuse box slides away. Blame: Leo's dot, which everyone saw.

### MA-4 One Suit
- Rule (one sentence): Only one teammate at a time wears the armor and can hit the giant or be hit by it; touching a friend jumps the armor onto them, and everyone else is a ghost.
- Fantasy (who you are, what you're doing): Spirit knights sharing one suit of armor to bring down a giant.
- Aesthetic (one line): Gold armor flickering from body to body, see-through blue ghosts, a giant with slow, huge swings.
- Player on player (what my action does to a friend, and what they decide back): The giant's fist is coming down on me, so I touch Eli, who's standing by its knee. The armor jumps to him and the swing turns toward him. He has under a second to dodge, then strikes the weak spot. Pass it as the fist lands and he's crushed. Eli then decides when to pass it on, and to whom.
- Why the plan can't settle (what changes round to round because of the players): The weak spot moves after each hit and shows for only a few seconds. The giant attacks the side where the ghosts gather most. The armor cracks with each hit taken, so the next wearer must be whoever is near the new weak spot, not the team's best fighter.
- Hub (the one shared thing everyone uses): The armor (always on exactly one person).
- At 3 / at 6: At 3, there are two ghosts to choose from. At 6, five ghosts spread out to cover weak spots. Risk: at 6, ghosts only position and wait (idle seat).
- Hidden (what, how uncovered, why hide) or "none": none.
- A failed run (what happens, who is blamed): Kim passes the armor to Eli mid-swing; Eli is crushed and the armor breaks. Blame: Kim's touch.

### MA-5 Shield for Others
- Rule (one sentence): Everyone carries a big shield that can't cover its holder, only the friend it's raised in front of, while archers fire volleys at the crew crossing a courtyard to open the gate.
- Fantasy (who you are, what you're doing): A peasant militia storming a castle courtyard with door-sized shields.
- Aesthetic (one line): Wooden shields with painted faces, torch-lit archers on the walls, arrows thunking into wood.
- Player on player (what my action does to a friend, and what they decide back): I raise my shield in front of Ola (it snaps to the friend I face within 2 m). She must crouch behind it before the volley lands, because standing leaves her head out. She can also step away from my cover to shield someone else. While I cover her I'm open, so I'm counting on someone covering me.
- Why the plan can't settle (what changes round to round because of the players): Archers light torches 2 s before a volley, which shows its direction. They aim at whoever was left open last time and flank pairs that keep shielding each other. The gate lever needs one person standing in the open, and who that is changes the cover pattern.
- Hub (the one shared thing everyone uses): The shields (each one useful only to someone else).
- At 3 / at 6: At 3, a triangle of cover works until arrows come from two sides. At 6, there are more shields but crossfire from more walls.
- Hidden (what, how uncovered, why hide) or "none": none.
- A failed run (what happens, who is blamed): Rui swings his shield to Pia as the volley comes from his left; Tom is left open and falls. Blame: Rui's swing.

### MA-6 Fumble
- Rule (one sentence): The cursed idol sticks to whoever holds it and burns them, and the only way to pass it is for a teammate to trip the holder, who throws it as they fall.
- Fantasy (who you are, what you're doing): Tomb raiders running a cursed idol out of a temple that wakes up behind them.
- Aesthetic (one line): Torch-lit stone halls, a glowing red idol, rolling stone guardians, pratfall tumbles.
- Player on player (what my action does to a friend, and what they decide back): The idol is burning Nia's health down. I slide-tackle her: she falls and is stunned for 2 s, and as she falls she aims the throw at one friend. That friend must catch it, or it hits the floor and sounds the guardian alarm. I hurt her (stun, guardians close in) to save her (the burn stops).
- Why the plan can't settle (what changes round to round because of the players): Guardians chase the idol and block the hall it's in. Doors open and shut in a pattern shown only during the run. Each player's health differs, so who should carry it next, and who trips whom, changes.
- Hub (the one shared thing everyone uses): The idol.
- At 3 / at 6: At 3, there is a short chain of trips and every stun hurts. At 6, there are more catchers but more guardians.
- Hidden (what, how uncovered, why hide) or "none": none.
- A failed run (what happens, who is blamed): Ian trips Nia at the bridge edge; she throws short and the idol drops into the pit. Blame: Ian's trip and Nia's throw, both seen.

### MA-7 Cursed Hands
- Rule (one sentence): The crew carries cursed relics to an altar, each relic puts its own curse on whoever holds it, and you pass one by pushing it into a friend's hands, which they can shake off within a second.
- Fantasy (who you are, what you're doing): Acolytes rushing cursed relics through a haunted abbey to seal them before the midnight bell.
- Aesthetic (one line): Candle-lit cloisters, relics glowing in their curse's colour, the holder's screen blurred, flipped or slowed.
- Player on player (what my action does to a friend, and what they decide back): I'm holding the Mirror Skull, so my controls are flipped. I push it into Tess's hands, and she has one second: keep it (she's flipped, I'm free) or shake it off (it drops and cracks; three cracks and it's lost). She decides by where she stands: on the narrow stairs, flipped controls kill her.
- Why the plan can't settle (what changes round to round because of the players): A relic's curse is unknown until someone picks it up (one of: blind, flipped, slow, heavy, mute, giant). Relics appear in random rooms and the altar moves at each bell, so which friend should carry which relic changes every time.
- Hub (the one shared thing everyone uses): The relics and the altar.
- At 3 / at 6: Relics = crew size − 1, so one person is always free to scout (2 at 3, 5 at 6).
- Hidden (what, how uncovered, why hide) or "none": The relic's curse, felt only by its holder (their screen and controls). Uncovered by the holder saying it, or by others watching them stumble. No reason to hide.
- A failed run (what happens, who is blamed): Tess shakes off the Heavy Bell on the last stairs; it cracks for the third time and is lost. Blame: Tess's shake-off.

### MA-8 Jump Pearls
- Rule (one sentence): Each player's jump is a glowing pearl that a friend can take by touching them, which gives the taker a double jump and leaves the owner unable to jump until a pearl comes back.
- Fantasy (who you are, what you're doing): A crew of small frogs climbing out of a flooding well, lending and stealing each other's hops.
- Aesthetic (one line): Mossy well walls, glowing pearls arcing between frogs, water surging up in bubbles.
- Player on player (what my action does to a friend, and what they decide back): I touch Bo and take his pearl, and double-jump to the high ledge. Bo is grounded and the water is at his feet. He shouts, and within seconds I either throw his pearl down to him or keep it for the next ledge and trust someone else to lend him one. Bo can also snatch a pearl from any frog who passes him.
- Why the plan can't settle (what changes round to round because of the players): Ledges grow out of the walls at random heights each round. The water surges up one side in pulses, shown a few seconds before by bubbles, so who is in danger and who can spare a pearl changes with every pulse.
- Hub (the one shared thing everyone uses): The pearls (one per player).
- At 3 / at 6: 3 pearls at 3, 6 at 6. At 6, pearls fly around more and the well is wider.
- Hidden (what, how uncovered, why hide) or "none": none.
- A failed run (what happens, who is blamed): Ada takes Bo's pearl and keeps climbing; the surge hits Bo's side and he drowns. Blame: Ada, carrying his pearl.
