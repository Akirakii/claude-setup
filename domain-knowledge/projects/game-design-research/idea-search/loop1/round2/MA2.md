# MA2: action and answer (round 2)

## Method log
- Listed 25 things one player does directly to another (push, pull, throw, lift and carry, swap places, blind, tag, tie a rope to, hand an item to, shrink, freeze, ride on, launch, steer, shield, paint, whisper a secret to, mirror, stack on, trip, heal, charge up, swing by the hand, handcuff to self, summon) and 15 answers a target can give within a second (brace, go limp, jump, duck, grab back, spin, pass it on, shake off, let go, sprint, curl up, ping a spot, match it back, drop what you hold, look away).
- Drew 16 pairs with `random.SystemRandom`, no picking and no re-rolls. "Paint -> jump" came up twice, so it got two different rules. "Summon -> brace" was close to round 1's hook, so the brace sends an object instead of deciding who moves.
- For each pair: the target's answer changes the result for both players. Then I added a round-changer that comes from a random deal, a visible shift in the arena or the players' own past moves, never "the threat hunts whoever holds X".
- Dropped ideas where one end ends up only holding or obeying: Ant Plank (the bridge just holds), Gorgon Hands (the covered player follows calls), Statue Cuffs. Also dropped ideas that copy a known game: Hammer Throw is too close to Heave Ho.
- Kept 6 with 6 different core rules: push apart, summon or send, paint the body or the floor, open or pass a sealed note, joint hold that stops a fuse, and a beam that bounces off a friend.

## Raw candidates
1. push -> grab back: Newton's Crew. In zero gravity a push sends both of you apart. If the pushed friend grabs back, you whirl and swap directions.
2. paint -> jump: Splash or Floor. You stand only on your own color. A splashed friend takes your color, or jumps and lets the paint color the tile under them.
3. summon -> brace: Summon or Send. You call a friend to your side. If they brace, the nearest loose thing beside them comes to you instead.
4. handcuff to self -> look away: Statue Cuffs. A cuffed pair shares one camera that the target controls. Statues move when the pair isn't looking, and looking away hands the view to the other player.
5. heal -> sprint: Borrowed Legs. Your life flows into a friend. If they stand still they heal. If they sprint, your life becomes their speed and you slow down.
6. paint -> jump (second draw): Sticky Coat. A splashed friend turns sticky, so friends and crates cling to them. If they jump, the floor under them becomes a sticky trap patch instead.
7. lift and carry -> brace: Ant Plank. A carried ant either goes stiff to become a bridge or ram, or stays loose with free jaws to grab crumbs.
8. launch -> grab back: Cannon Mates. You fire a crewmate from the deck cannon. If they grab the gunner as it fires, both fly half as far.
9. whisper a secret to -> pass it on: Sealed Orders. A sealed note handed to you must be opened, so only you know it, or passed on within 2 s. One crewmate is a saboteur.
10. hand an item to -> grab back: Goblin Keg. A fuse burns while one goblin holds the keg and freezes while two do. A friend you hand it to takes it, or grabs your wrist and you walk as a slow pair.
11. heal -> brace: Defib Bump. You heal by body-slam. If the friend braces, they heal fully and you bounce far away. If not, they fly off half-healed.
12. summon -> grab back: Hand-Chain Call. Summoning a friend also brings whatever they grab in that second: a friend, a crate or a guardian.
13. handcuff to self -> match it back: Fused Pair. If the friend cuffs back within a second, you share one health bar and one double jump. If not, you just drag them.
14. swing by the hand -> ping a spot: Hammer Throw. You spin a friend and they let go when they choose (too close to Heave Ho).
15. blind -> let go: Gorgon Hands. You cover a friend's eyes so the gorgon's gaze can't turn them to stone. You see for both, and they can pull your hands away to look.
16. mirror -> ping a spot: Prism Crew. A beam does nothing until it bounces off a friend. The friend aims the bounce by facing, or steps out of it, and every bounce scorches them.

## Kept ideas

### MA2-1 Newton's Crew
- Rule (one sentence): In zero gravity the only way to move is to push off a teammate, which sends you both apart (the lighter one faster). If the pushed teammate grabs back in that second, you whirl around each other once and fly off in swapped directions.
- Fantasy (who you are, what you're doing): You are a repair crew with no jetpacks, floating in the wreck of a space station and patching hull breaches before the air runs out.
- Aesthetic (one line): Bulky cartoon spacesuits tumbling through silent debris, lit by welding sparks and a blue planet below.
- Player on player (what my action does to a friend, and what they decide back): I push Dan toward a breach, and that also sends me the other way. In the same second Dan decides: let go (he goes to the breach and I drift back), or grab back (I go to the breach and he drifts back along my old line). Every move I make spends a friend's position, and the friend picks which of us pays.
- Why the plan can't settle (what changes round to round because of the players): Breaches open at random spots on the slowly turning station, shown by sparks 3 s ahead, so the needed direction changes mid-round. A patch kit makes its carrier heavy and slow, so who holds a kit changes who should push whom. Anyone sent outward needs someone to come out and push them home, and that costs a third person's position. So the crew's own last few pushes set the next puzzle, and no fixed order of pushes survives.
- Hub (the one shared thing everyone uses): Momentum split between two bodies on every push.
- At 3 / at 6: At 3, every push strands someone and there are few left to fetch them. At 6, people can push in chains, but there are more drifters to bring home and more breaches open at once (breaches scale with crew size).
- Hidden (what, how uncovered, why hide) or "none": none
- A failed run (what happens, who is blamed): Mia pushes off Dan to reach a breach. Dan grabs back late, the whirl flings Mia into open space where nobody is left to push her home, and the breach stays open until the air runs out. Everyone saw Dan's grab.

### MA2-2 Summon or Send
- Rule (one sentence): You can summon one teammate to your side, but if they brace in that second, the nearest loose thing beside them (a relic, a lit bomb, a crate, a stone guardian) is pulled to you instead.
- Fantasy (who you are, what you're doing): You are apprentice mages looting a sealed vault while its clay guardians wake up.
- Aesthetic (one line): Candle-lit stone rooms, chunky clay guardians, and a purple swirl and pop on every summon.
- Player on player (what my action does to a friend, and what they decide back): I call Jo when I need hands. Jo sees what is beside her, and I don't. In one second she decides whether to come herself or send me what is next to her: the relic I need, the bomb for the door I'm at, or the guardian chasing her, dropped on top of me. I choose when and whom to call; she chooses what arrives.
- Why the plan can't settle (what changes round to round because of the players): Vault rooms slide to new grid spots every 20 s, shown 3 s ahead, and the relic list is dealt fresh each round. Guardians follow a simple visible walk (straight ahead, turn at walls), but players keep sending them across the vault, so where the danger stands now comes from what friends did a minute ago. The same call can be a rescue or a trap, depending on what happens to be beside the friend.
- Hub (the one shared thing everyone uses): The summon: one call with two possible answers.
- At 3 / at 6: Each player has one summon per 8 s. At 3, every call is precious and an empty room is common. At 6, there are more callers, more things beside people, and more guardians to scatter. At every size each call reaches one named friend.
- Hidden (what, how uncovered, why hide) or "none": none (what is beside the called friend is off the caller's screen, so they ask over voice before calling)
- A failed run (what happens, who is blamed): Sam summons Lee to help lift the altar. Lee braces to send the relic, but the nearest thing was the guardian, which lands on Sam and grabs him. Lee's brace is seen by all.

### MA2-3 Splash or Floor
- Rule (one sentence): Each player can stand only on floor tiles of their own color. When you splash a teammate with your paint they turn your color, unless they jump in that second, and then the paint colors the tile under them instead.
- Fantasy (who you are, what you're doing): You are a troupe of paint sprites crossing a giant mural that is being wiped clean behind you.
- Aesthetic (one line): Bold flat colors, a mosaic floor, wet splashes and round little sprites.
- Player on player (what my action does to a friend, and what they decide back): I splash Kai. Kai can take my color, which lets Kai walk my tiles but costs Kai the old ones. Or Kai can jump, so the tile under Kai becomes mine: a stepping stone for me and anyone else my color. But Kai must then land on a nearby tile of Kai's own color or fall. Either way the floor or the friend changes for both of us.
- Why the plan can't settle (what changes round to round because of the players): Every 10 s a wave recolors random tiles (the pattern shows 2 s ahead), and body paint wears off after 8 s. The floor ahead is the leftover of everyone's last splashes. Whether "take it" or "jump" is right depends on which colors happen to be around each player at that moment, so no fixed rule like "always jump" holds.
- Hub (the one shared thing everyone uses): The colored floor.
- At 3 / at 6: Always 3 colors. At 3, each player owns one color. At 6, two players share each color, so a splash can help or strand your color-mate too. At odd sizes one color has an extra player.
- Hidden (what, how uncovered, why hide) or "none": none
- A failed run (what happens, who is blamed): Ari splashes Bo to bring Bo onto blue. Bo jumps at the last moment, the tile under Bo turns blue, Bo lands on red with no red left near, and drops off the mural. Bo's jump is seen by all.

### MA2-4 Sealed Orders
- Rule (one sentence): A sealed note handed to you must, within 2 seconds, be opened (only you see it, it burns, and only you may carry out its order) or passed unopened to another teammate.
- Fantasy (who you are, what you're doing): You are a bomb squad defusing devices around a moving train car while one of you is secretly working for the bomber.
- Aesthetic (one line): Rattling train car, red emergency light, paper notes with wax seals and ticking brass devices.
- Player on player (what my action does to a friend, and what they decide back): A printer spits a note near me. Its seal shows the device (A–F); the inside says which wire. I hand it to Rae. Rae decides: open it, which commits her to running to that device, speaking the wire aloud and cutting it, or pass it to someone she trusts more or who is closer. Whoever opens is the only one who knows, so everyone else must trust what they say.
- Why the plan can't settle (what changes round to round because of the players): The saboteur is new each round. Devices sit in shuffled spots, and the train lurches to shift them mid-round. Who opened what, and whether their cuts held, changes trust during the round, so "give it to whoever is closest" breaks as soon as the closest player is suspect. The saboteur has a private reason to break any plan, and can cut right early to earn trust.
- Hub (the one shared thing everyone uses): The note stream (one printer, one note at a time).
- At 3 / at 6: At 3, there is 1 saboteur among 3 and every pass is a real trust bet. At 6, there is 1 saboteur, more devices and longer pass chains. The note never sits with an idle seat, because everyone is either holding, cutting or watching a cut.
- Hidden (what, how uncovered, why hide) or "none": The saboteur, and each note's inside. Uncovered by a cut that sparks (a wrong wire is visible to all) and by checking claims against later notes for the same device. The saboteur hides to keep being handed notes.
- A failed run (what happens, who is blamed): Rae opens the note for device C, says "blue" and cuts red. The device sparks and the car fills with smoke. Everyone saw Rae's cut, and the argument is whether she misread or lied.

### MA2-5 Goblin Keg
- Rule (one sentence): A lit keg's fuse burns while one goblin holds it, freezes while two hold it, and races while it sits on the ground. When you hand it over, the friend either takes it (you are free, fuse burning) or grabs your wrist (both hold, fuse frozen, you walk as a slow pair steered by both sticks).
- Fantasy (who you are, what you're doing): You are goblin sappers blowing holes in a castle wall during a siege.
- Aesthetic (one line): Muddy field, crooked ladders, a sizzling fuse, green goblins in oversized helmets.
- Player on player (what my action does to a friend, and what they decide back): I hand the keg to Pip. Pip decides: take it and sprint (fast, fuse burning), or grab my wrist (fuse frozen, but we're a slow pair and both of us must agree on where to walk). In a pair either of us can let go at any moment, which leaves the other holding a live keg.
- Why the plan can't settle (what changes round to round because of the players): The weak spot in the wall is marked by the captain's flag, which moves to a random section mid-round. Boiling oil falls at random spots shown by shadows 2 s ahead, and a slow pair can't dodge it together, so at that moment one of them must let go, and that one chooses who keeps the keg. Kegs roll off the cart at random times. "Pair up, then let go near the wall" breaks whenever the oil or the flag moves first.
- Hub (the one shared thing everyone uses): The keg's fuse (held by one, frozen by two).
- At 3 / at 6: At 3, there is one keg: a pair plus a runner. At 6, there are two or three kegs, and pairs swap partners across them. At odd sizes there is always one free goblin who decides whom to relieve.
- Hidden (what, how uncovered, why hide) or "none": none
- A failed run (what happens, who is blamed): A shadow shows up over Pip and Mo, and Mo lets go to dodge without warning. Pip is left holding the keg with a racing fuse, can't reach the wall, and it blows in the trench. Everyone saw Mo let go.

### MA2-6 Prism Crew
- Rule (one sentence): Your light beam does nothing until it bounces off a teammate. The teammate it hits chooses where the bounce goes by where they face, or steps out of it, and every bounce scorches them a little.
- Fantasy (who you are, what you're doing): You are lantern spirits in a cave, relighting old crystals before the dark swallows the cave for good.
- Aesthetic (one line): A black cave, glowing beams zig-zagging between small glowing figures, crystals bursting into stained-glass color.
- Player on player (what my action does to a friend, and what they decide back): I fire at Ana. In that second Ana decides where to send it: straight at a crystal, on to another friend for a longer chain that reaches around a wall, or nowhere, by stepping aside to save her own light. I choose whom to fire at; she chooses where it goes and whether to pay for it.
- Why the plan can't settle (what changes round to round because of the players): Crystals wake at random spots each round. Every lit crystal grows a glass wall that blocks beams, so the team's own successes keep changing the lines of sight. Lit crystals fade back to dark over time, starting from a random tunnel each round (shown at the start), so the team must keep re-angling chains through a map it keeps changing. Each player's scorch level is different, so who can afford the next bounce changes from moment to moment.
- Hub (the one shared thing everyone uses): The beam (it needs a friend to land anywhere).
- At 3 / at 6: At 3, chains are short and every bounce costs a lot of light. At 6, there are long chains around walls, but every link is a friend who can step out. Scorch heals slowly near a lit crystal, so nobody is benched.
- Hidden (what, how uncovered, why hide) or "none": none
- A failed run (what happens, who is blamed): Ana steps out of Leo's beam to save her light just as the last crystal fades. The chain breaks and the cave goes dark. Everyone saw Ana step aside.
