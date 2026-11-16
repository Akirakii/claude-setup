# MC: plan breaker first

## Method log
- **Steps.**
  1. Read `checks.md` only. Also read `~/.claude/design-anti-patterns.md`, as the user's global rule 11 asks, and checked every sketch against it: no co-location counted as co-op, no solo-able verb, no luck culprit.
  2. Listed 24 plan breakers, each one simple rule (list below, PB1–PB24).
  3. For each one, built a core verb that lands on one friend and makes the threat or rule pick a different friend each time. That gave 25 raw ideas, because PB24 gave two.
  4. Kept 8 with 8 different core rules, ranked P first, then the formula, then R.
  5. Ran one web search per kept idea. One swap.
- **Plan breakers listed (PB).**
  1. The threat chases whoever last helped.
  2. It chases whoever has stood still longest.
  3. It chases whoever carries most.
  4. A link or tile used twice breaks.
  5. The same action twice on the same friend flips from help to hurt.
  6. A who-acts-on-whom map is dealt mid-round.
  7. A private order goes to one player.
  8. It chases whoever has been untouched longest.
  9. It chases whoever was helped last.
  10. A random crown or VIP every 20 s.
  11. The monster sees through the eyes of whoever was touched last.
  12. A random pair gets linked every 15 s.
  13. Hidden drain rates per player.
  14. It chases whoever acted most in the last 10 s.
  15. What you do to a friend comes back to you.
  16. A curse jumps to whoever touched the carrier last.
  17. Private debts to one friend.
  18. The threat copies the team's most-used verb.
  19. Mid-round reveal of which player must end holding the prize.
  20. It chases the most common colour or state.
  21. Light sweeps to a random side.
  22. Infection jumps to whoever stands nearest the carrier.
  23. It chases whoever holds the voice.
  24. It chases the extreme of a body state (smallest, slowest, last mover).
- **Raw count:** 25.
- **Gates the raw ideas failed most:**
  - **R1 plan card (most):** a simple threat rule is predictable, so the crew can answer it with a fixed rotation (A→B→C). Examples: R10 twin spell, R11 pair lock, R16 bear (a cycling paceline), R21 hug rotation.
  - **P3 help or hurt:** verbs that can only help, or only hurt the named friend while helping a third. Examples: R13 decoy whistle, R17 crown.
  - **P2 answer:** the friend only obeys or sits still. Examples: R12 puppet ring, R20 called pairs.
  - **N, as a family:** most cores became "the threat chases whoever has X, and players move X onto each other". The cores differ in X, but it is one family, so the blind score may read them as close.
- **Novelty searches (one each).** Results by idea:
  - **MC-1 One Mic:** HUSHED and HUSH have monsters that hear players' voices, with proximity chat. Nothing found with one live mic passed by a player. Close family, the passing rule is new. ~
  - **MC-2 Storm Blessing:** nothing found where healing a friend marks them as the target. ✓
  - **MC-3 Clockwork Cat:** Winder Walkers (itch.io) is a co-op wind-up toy puzzle game with carrying. Not confirmed that the toys wind each other, and no cat. ~
  - **MC-4 Friend Hooks:** Grapples Galore lets you grapple onto other players, and Skyhook is a versus brawler with hooks at players. Nothing found with a brace or go-limp choice, or with breaking tiles. ~
  - **MC-5 Paint Prison:** Backrooms Splatter (paint reveals doors) and Color Blasters (colour switchers, enemies tied to colours). Nothing found with splashing friends or a chaser of the majority colour. ✓
  - **MC-6 Trade Places:** NOT SEARCHED. The session's web search budget ran out on this search. Unchecked.
  - **MC-7 Size Ray:** a R.E.P.O. shrink-gun mod hits anyone. Nothing found with friend-only resizing plus an owl. ✓
  - **MC-8 Lonely Boogeyman:** HUSH's monster follows the most afraid player. Nothing found that targets isolation time or uses hugs. ✓
- **Swap log.** Giant Toss (raw R7) was kept 6th, then dropped. Titan Hunters (fire teammates from a catapult at giant monsters) and Little Thorns (throw teammates at a boss's weak points) share the core rule. Replaced by the next-best raw idea, Trade Places (R6). Its search could not run (budget), so its novelty is unchecked.
- **Good:** starting from the plan breaker forced every core to answer "which friend now?". All 8 make the threat's choice depend on what players just did to each other, so blame is visible: the HUD shows who passed, blessed, wound, splashed or swapped.
- **Bad:**
  - The method converges on one family: a threat chases property X, and players push X onto each other.
  - Threats with one deterministic rule invite rotation plans. The ideas lean on positions and a random layout for the "which", which is weaker than a private reason.
  - The private-reason breakers (PB7, PB17) gave weak ideas. Nothing hidden had a reason to hide in pure co-op, so none were kept.
  - Online lag: same-moment answers (MC-4 brace or limp in 1 s, MC-8 hug back in 1.5 s) need lag tolerance. Not checked.

## Raw candidates
1. **R1 Kind Ghost (PB1):** in a sinking bog, lift a friend out or step on them to climb, and a ghost hunts whoever lifted last.
2. **R2 Clockwork Cat (PB24, last mover):** toys can't wind themselves, you wind a friend and they run, and the cat pounces at the last toy that moved. → kept as MC-3.
3. **R3 Storm Blessing (PB9):** heal only friends, and lightning strikes whoever was blessed last, 2 s later. → kept as MC-2.
4. **R4 Heavy Purse (PB3):** throw stolen coins onto friends, and the dogs chase whoever carries most. Same family as R5, weaker.
5. **R5 One Mic (PB23):** only one live mic, you hand it to a named friend, and the blind beast walks to whoever holds it. → kept as MC-1.
6. **R6 Trade Places (PB1 variant):** swap places with a friend you can see, and the golem hunts whoever started the last swap. → kept as MC-6, after the swap.
7. **R7 Giant Toss (PB1 variant):** throw a friend at a giant, and it grabs whoever hit it last until someone else hits it. Kept, then swapped out (Titan Hunters, Little Thorns).
8. **R8 Paint Prison (PB20):** splash a friend your colour, gates match colours, and the guard drone chases the most common colour. → kept as MC-5.
9. **R9 Friend Hooks (PB4):** hooks only latch onto friends, the hooked one braces or goes limp, and tiles break on the second landing. → kept as MC-4.
10. **R10 Twin Spell (PB5):** the same spell on the same friend twice in a row flips to harm. Rotation solves it (R1 ✗).
11. **R11 Pair Lock (PB4):** a zipline between the same two players snaps on second use. Rotation solves it.
12. **R12 Puppet Ring (PB6):** a map of who steers whose body, re-dealt every 30 s. The steered friend only talks (P2 ✗).
13. **R13 Decoy Whistle (PB14):** point at a friend to send the monster to them. It only hurts the named friend (P3 weak).
14. **R14 Lonely Lantern (PB8):** touch a friend to give or take lamp oil, and the shadow takes the dimmest. Leads to "keep lamps even" (R1 weak).
15. **R15 Mirror Curse (PB15):** what you do to a friend happens to you 3 s later. No reason to act on a friend.
16. **R16 Bear Run (PB24, slowest):** shove a friend from behind to boost them or from the side to trip them, and the bear chases the slowest. A paceline rotation solves it.
17. **R17 Hot Crown (PB16):** the crown shields its wearer but burns them, so pass it to whoever is attacked. Same family as R5.
18. **R18 Fever Ring (PB22):** the fever jumps to whoever stands nearest the carrier. Proximity is a weak verb.
19. **R19 Size Ray (PB24, smallest):** you only shrink or grow friends, and the owl dives at the smallest. → kept as MC-7.
20. **R20 Called Pairs (PB12):** the band calls a random pair every 15 s, who must do a lift. The friend is set by fiat, not chosen.
21. **R21 Lonely Boogeyman (PB8 + PB5):** it takes whoever has gone longest without a hug, and a hug only counts with a new friend. → kept as MC-8.
22. **R22 Wanted Name (PB10):** slap your name tag onto a friend, and the guards chase the wanted name. Same family as R5.
23. **R23 Mimic Face (PB11):** helping a friend makes a mimic wear their face, so friends test "is that you?". Too random.
24. **R24 Debt Cards (PB17):** a private card names the friend you score for saving. No reason to hide in co-op.
25. **R25 Immune Giant (PB18):** the boss becomes immune to whichever friend hit it last. Rotation solves it, and it is close to R7.

## Kept ideas

### MC-1 One Mic
- **Rule (one sentence):** Only one player's microphone is live at a time. You hand it to a friend by tapping their name, and the blind beast always walks toward whoever holds it.
- **Fantasy:** You are miners trapped in a flooded, pitch-black mine with a blind beast that hunts by sound. You share one working radio, and whoever talks gives away where they are.
- **Aesthetic:** Black caves with each miner a small helmet-lamp circle. A crackling "LIVE" glow sits over the speaker's head. The beast is a pale shape at the edge of someone's light.
- **Player on player:**
  - I hand Ana the mic. From that moment everyone hears her and the beast turns toward her.
  - She must hold it at least 3 s. In that time she says what her lamp shows ("beast's left of me, fuse is right"), then picks who gets it next.
  - I help her if I hand it over when she has news and the beast is far. I hurt her if I hand it over while the beast is two steps away.
  - Her answer is the same choice, aimed at the next friend.
- **Why the plan can't settle:** The beast walks to the holder, so the safest receiver changes after every pass. The friend who has news (they saw the fuse, the beast or a dead end) is a different person each time, and often not the safe one. Each pass trades "who knows something" against "who can afford to be hunted". Cave layout comes from 3 maps, with random fuse and lift spots.
- **Hub:** the one live mic.
- **At 3 / at 6:** At 3, every pass is a forced pick between two friends and the beast is never far from someone. At 6, more people hold news and wait for the mic, so who gets it is the hard part. The beast's speed stays the same, so more players means more distance to cover.
- **Hidden:** What each lamp shows. It is uncovered by getting the mic and saying it. Reason to hide: holding the mic draws the beast, so a player may sit on news or pass the mic on without speaking.
- **A failed run:** Kai hands the mic to Ana while the beast is right behind her. Everyone sees the LIVE glow jump to her and the beast turn. She is caught before her 3 s are up. Blame: Kai.

### MC-2 Storm Blessing
- **Rule (one sentence):** You can only heal a friend, never yourself, and 2 s after every blessing, lightning strikes whoever was blessed most recently.
- **Fantasy:** You are pilgrim monks crossing a mountain pass in a god's storm. The cold eats you, a friend's blessing warms you, and the jealous storm strikes whoever was blessed.
- **Aesthetic:** A slate-grey mountain path lit by flashes. A white charge crackles over the last-blessed head. Monks huddle under rock overhangs.
- **Player on player:**
  - Health drains in the open (1/s) but not under rock. I hold bless on Bo for 1 s, and his health refills.
  - A strike is now coming at him in 2 s, so he must reach a rock or move the strike. He moves it by blessing someone else, which re-aims every pending strike at that person.
  - The help (heal) and the hurt (the mark) come in one act.
  - Bo's answer, within 2 s, is to run for a rock or pass the mark by blessing a friend who is already under cover.
- **Why the plan can't settle:**
  - Rock positions along the path are random per round, from a short list.
  - Who is dying changes each moment, and progress forces people into the open.
  - Whom to bless depends on who is near cover right now. The mark can be bounced off a friend crossing the open by blessing a friend under a rock.
  - The storm always aims at the team's latest choice, so it answers what the team just did.
- **Hub:** the strike, which always aims at the last-blessed.
- **At 3 / at 6:** At 3, each blessing leaves one friend unblessed and draining, so it is tight. At 6, more people are in the open and the bounce chains grow longer. Drain is per player, so it scales.
- **Hidden:** Exact health is shown only to its owner, as frost creeping over the screen. It is uncovered by saying it. Reason to hide: being blessed in the open is dangerous, so a player may play down how low they are.
- **A failed run:** Ana blesses Cid in the middle of the open slope, 4 m from any rock. The white charge appears over Cid, he runs, and he is struck 1 m short. Blame: Ana (seen at the moment of her bless glow).

### MC-3 Clockwork Cat
- **Rule (one sentence):** Wind-up toys can't wind themselves: you wind a friend's key and they run, and the cat always stalks the toy that moved last.
- **Fantasy:** You are tin toys crossing a child's bedroom at night to reach the toy box. The house cat thinks you're mice.
- **Aesthetic:** A warm lamp-lit bedroom seen from toy height. Springs tick, keys turn, and the cat's eyes glow under the bed.
- **Player on player:**
  - I hold Bo's key, and each second I wind gives him 3 s of running, up to 9 s. While I wind, I stand still next to him.
  - Bo steers where he runs, and he must reach another stopped toy and wind it before his spring dies.
  - Help: a long wind aimed at the toy box. Hurt: winding him while the cat sits nearby, because he becomes the last mover and the cat comes for him. Bo answers by choosing route and whom to wind next, within his few seconds.
- **Why the plan can't settle:** The cat goes for whoever moved last, so every wind is also "who gets hunted now". The team winds the toy farthest from the cat, or winds a decoy across the room to pull the cat off a friend near the goal. The cat's spot after each pounce, and furniture from 3 rooms, change which friend should be wound next.
- **Hub:** the cat, which always goes for the last mover.
- **At 3 / at 6:** At 3, one runs, one winds and one waits, so every toy matters. At 6, there are more choices and more stopped toys to keep fetching. All toys must reach the box, so no one can be left behind.
- **Hidden:** none.
- **A failed run:** Mia winds Leo while the cat sits on the bed right above them. Leo is the last mover, the cat pounces, and Leo's spring is knocked empty. Everyone saw Mia's key turn. Blame: Mia.

### MC-4 Friend Hooks
- **Rule (one sentence):** Your grapple only latches onto friends: the hooked friend chooses to brace (you fly to them) or go limp (they fly to you), and every floor tile breaks the second time anyone lands on it.
- **Fantasy:** You are steeplejacks crossing a crumbling chain of floating stone tiles to reach a beacon above the clouds.
- **Aesthetic:** Bright floating stones over a sea of cloud, glowing hook ropes zipping between people, and cracks that glow after the first landing.
- **Player on player:**
  - I hook Bo, and he has about 1 s to brace or go limp.
  - If I'm on a cracked tile, his brace saves me. If he is on one, going limp saves him.
  - The wrong pick hurts. If he goes limp onto my cracked tile, it is a second landing and we both drop. Hooking him mid-jump yanks him off course.
  - Both decide in the same second.
- **Why the plan can't settle:**
  - Every tile the team lands on once is half-spent, and twice is gone, so the team's own route closes behind them.
  - Which friend you can hook (in range, with a clear line) changes after every landing.
  - Some tiles start cracked: random each round, and revealed only up close.
- **Hub:** the tile field, which breaks where the team has been.
- **At 3 / at 6:** At 3, there are few anchors, so each brace or limp call is life or death. At 6, there are more anchors but tiles get used up faster. The island is a bit bigger at 6.
- **Hidden:** Pre-cracked tiles show only within 2 m. They are uncovered by someone getting close and calling it. Reason to hide: none, so this is information only.
- **A failed run:** Kai hooks Ana while standing on a cracked tile. Ana goes limp, lands on Kai's tile, it breaks, and both fall. The ragdoll "limp" pose shows it was Ana's call. Blame: Ana (or Kai for hooking from a cracked tile).

### MC-5 Paint Prison
- **Rule (one sentence):** You splash friends with your paint colour, never yourself: coloured gates only open for that colour, and the guard drone always chases the colour most prisoners wear.
- **Fantasy:** You are prisoners breaking out of a colour-coded prison, where each wing's doors read uniform colour.
- **Aesthetic:** A clean white prison with fat splashes of red, blue and yellow. A drone's searchlight takes the colour it is hunting.
- **Player on player:**
  - Each player gets one paint colour per round: one of each at 3, two of each at 6. I splash Bo red, and he can now pass red gates (help).
  - If red becomes the most worn colour, the drone hunts the red wearers, Bo included (hurt).
  - Within seconds, Bo must use the red gate, get re-splashed by a friend to change the count, or run.
  - Ties go to the last colour splashed.
- **Why the plan can't settle:**
  - The gate order on the route is random per round, from 3 prison wings.
  - The drone hunts whatever colour the team is crowding into, so "everyone go red for the red wing" gets punished.
  - Which friend to repaint depends on the next gate, the current count, and who is nearest the drone.
- **Hub:** the colour count, which aims the drone.
- **At 3 / at 6:** At 3, any one splash makes a majority, so each splash is a big call. At 6, the count needs two or three splashes to flip, and more friends to choose from. Odd sizes are fine because ties have a rule.
- **Hidden:** none.
- **A failed run:** Kai splashes Ana blue for the blue gate, which makes blue the majority. The drone turns blue and catches Ana at the gate. The splash and the count change are on screen. Blame: Kai.

### MC-6 Trade Places
- **Rule (one sentence):** You can swap places with any friend you can see, and the tower golem always hunts whoever started the last swap.
- **Fantasy:** You are apprentice wizards trapped in a collapsing tower. The only spell you learned is "trade places", and the tower's golem is angered by magic.
- **Aesthetic:** A dusty spiral tower with a purple flash line between the two who swapped. The golem's single eye swings to the caster.
- **Player on player:**
  - I swap with Bo. He is suddenly where I was: next to the lever I couldn't reach, or on the floor that is about to fall. I am where he was, and now the golem hunts me.
  - Help: take his place out of a closing trap. Hurt: drop him somewhere bad or next to the golem.
  - Bo has seconds to act from his new spot (pull the lever, run), or he can start a swap himself and take the golem.
  - Each player has a 4 s cooldown, so no one chains swaps alone.
- **Why the plan can't settle:**
  - Levers and the stairs key appear at random spots on 3 tower floors.
  - Each swap is both "who goes where" and "who takes the golem". Who should start it depends on who can afford to be hunted right now.
  - A player who keeps doing the swaps gets hunted all the time.
- **Hub:** the golem, which follows the last caster.
- **At 3 / at 6:** At 3, there are few lines of sight, and each swap leaves one friend to fend alone. At 6, there are more swap partners and more people to dodge the golem's path.
- **Hidden:** none.
- **A failed run:** Ana swaps with Kai, which drops him onto the cracking floor while she takes the lever. The floor goes, and the purple line showed who cast. Blame: Ana.

### MC-7 Size Ray
- **Rule (one sentence):** You can only shrink or grow a friend, never yourself, and the owl always dives at the smallest player.
- **Fantasy:** You are tiny explorers crossing a backyard at dusk with a ray gun that works only on others, under an owl's eye.
- **Aesthetic:** A golden-hour garden at bug scale, with grass like trees and flowerpots like buildings. The owl's shadow sweeps across the lawn.
- **Player on player:**
  - There are 3 sizes: small, normal and big. I shrink Bo, and he can slip under the fence or into a burrow (help), but he is now the smallest, so the owl starts its 3 s dive (hurt).
  - Bo must reach a burrow within 3 s, or shout for someone to grow him back.
  - If I grow Ana, she can push a pot but moves slowly. Ties go to whoever was shrunk last.
- **Why the plan can't settle:**
  - Garden layout comes from 3 yards, with random pot and hole spots, so which friend must be small (for a hole) or big (for a pot) changes per obstacle.
  - The owl punishes keeping someone small, so sizes must keep moving between friends.
  - Who to shrink depends on who is near a burrow when the owl is overhead.
- **Hub:** the owl, which always dives at the smallest.
- **At 3 / at 6:** At 3, each shrink makes a sure target. At 6, the team can stage several small players, but only one is the target, so it is the timing that counts.
- **Hidden:** none.
- **A failed run:** Mia shrinks Leo in open grass, 5 m from a burrow, and the owl dives and takes him. The ray beam showed who fired. Blame: Mia.

### MC-8 Lonely Boogeyman
- **Rule (one sentence):** The boogeyman goes after whoever has gone longest without a hug, and a hug only counts with a different friend than your last one.
- **Fantasy:** You are kids at a sleepover sneaking across a dark house to the blanket fort while the boogeyman takes the lonely kid.
- **Aesthetic:** Moonlit blue hallways, flashlight cones, pyjamas and bunny slippers. A tall shadow sits at the end of the hall.
- **Player on player:**
  - I run to Bo and press hug, and he must hug back within 1.5 s. We both freeze for 1 s, and both our "alone" clocks reset.
  - It doesn't count if we were each other's last hug.
  - He hurts me if he refuses, because I stay the loneliest. A hug near the boogeyman freezes us both in its path.
  - Bo's answer is accept or refuse, then who he hugs next.
- **Why the plan can't settle:**
  - The target is always the most-ignored kid, and no repeat partner means fixed pairs fail.
  - The boogeyman's charges scatter the kids through 3 house layouts, so who is reachable for a hug keeps changing.
  - Weak point: at 3, a triangle rotation (A-B, B-C, C-A) is close to a plan card.
- **Hub:** the alone clocks, which aim the boogeyman.
- **At 3 / at 6:** At 3, someone is always waiting for a hug. At 6, the pairs reshuffle and someone gets forgotten. Odd sizes leave one kid alone, which is the point.
- **Hidden:** Your own clock is seen only by you, as the screen edges darken. It is uncovered by saying "I'm at 20!". Reason to hide: none, so this is information only.
- **A failed run:** Leo refuses Mia's hug to run for Kai instead. Mia's clock maxes out and the boogeyman takes her, and everyone saw her hug arms left hanging. Blame: Leo.
