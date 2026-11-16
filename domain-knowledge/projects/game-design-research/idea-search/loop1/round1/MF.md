# MF: method F "people handling people" (round 1)

## Method log

**Steps run**
1. Read `checks.md` (and `~/.claude/design-anti-patterns.md`, which RULES.md says to read before any design sketch). Read nothing else under `research_notes/` or `reports/`.
2. Listed 25 real activities where people physically handle other people under time pressure (table below), with who handles whom, what the handled person decides back, and what changes moment to moment.
3. Turned each into one or more co-op rules with a plan breaker: 29 raw ideas.
4. Ran the gates in order (P, then formula, then R, then N from memory) and kept 8 with 8 different core rules.
5. Novelty step: **not done.** The first 4 web searches came back "session web search budget used up (200 calls shared by all agents)". The tool said not to wait or work around it, so no searches ran and no swaps were made. N for each kept idea below is from memory and tagged [memory], unchecked. A later round must still run one search per kept idea.

**Activity table (who handles whom / what the handled person decides back / what changes)**
1. Lifeguard rescue: lifeguard tows swimmer / go limp or grab / panic, waves.
2. Stunt ratchet pull: rigger yanks performer on a cable / hit the mark, brace / the shot changes take to take.
3. Cheer basket toss: bases throw flyer / which trick, body shape / flyer balance, judges' taste.
4. Rugby lineout: lifters hoist jumper, thrower lobs / jump moment, catch or tap down / opponents read the call.
5. Trapeze catch: catcher swings, flyer lets go / release moment / swing phase.
6. Course camarguaise (snatching ribbons off a bull): teammates pull a snatcher clear / how late to reach / the bull's charges and fakes.
7. Crowd surfing: crowd passes the surfer / lean, kick, dive back down / crowd gaps, security.
8. Patient transfer: nurses lift on a count / help or resist / pain, confusion.
9. Bouncers: walk a drunk out / go limp or break free / crowd, mood.
10. Barn-dance swing and dance lifts: partner spins or lifts partner / when to let go / music, the caller's call.
11. Treading water / water polo: push someone up or down / kick up, breathe / air left, position.
12. Sumo: push the other / lean, sidestep / balance (opponent only).
13. Crowd evacuation marshals: push and point crowds / which exit / crush points.
14. Firefighter carry: carrier lifts victim / hold on / smoke, stairs.
15. Bodyguard detail: guards shove the protected person / go with it or resist, where to go / threat angle.
16. Formation skydiving: divers grip each other's wrists / hold or let go / fall rate, spin, next shape.
17. Castells (human towers): base holds climbers / when to climb, lean / sway.
18. Roller derby whip: blocker slings the jammer forward / take the whip, which line / the opposing pack's wall.
19. Stage combat: attacker throws a fake punch / the victim sells it, which way to fall / camera angle.
20. Bouldering spotting: spotter guides a falling climber / which hold, when to jump / holds, fall line.
21. Synchronized swimming lift: bases push a flyer up / pose / breath.
22. Tag-team wrestling: partner tags in / come in now / opponent's state, referee.
23. Rodeo pickup rider: pickup rider pulls the rider off a bronc / when to let go / the horse's bucking.
24. Ice rescue: rescuers lie flat and grab the fallen / grab, kick / ice cracking.
25. Team-building wall: boosters lift climbers, the top pulls the last one up / when to jump / who is left below.

**Raw count:** 29 raw ideas from 25 activities.

**Gates the raw ideas failed most**
- P1 pooling: several hands on one body or one stretcher add up to one push (basket toss, stretcher, synchro lift), or the action lands on AI people instead of a friend (marshals). 5 ideas.
- Same verb as a kept idea: passing, catching or yanking a person came up again and again (Big Top, Ratchet, Spotter, Zero-G, Pickup Rider). 5 ideas. This is the method's main weakness: handling people collapses into about 4 verbs (pass, lift, yank, hold).
- R plan settles: a sorting rule like "strongest at the bottom" or "go limp when the rescuer is close" wins every round (Castell, Rip, Wall, Leapfrog). 4 ideas.
- Already taken: chains of grips read as rope-tied crews; rider/carrier read as one limb each or stations (Ice Chain, Kabaddi, Piggyback, Fireman's Carry). 4 ideas.
- F5: fixed pairs break at odd sizes, or bench players sit idle (Pairs Throw, Tag Team). 2 ideas.

**Swaps:** none. Web search was blocked (see step 5).

**Good / bad**
- Good: P passes almost for free. When the thing you act on is a friend's body, "lands on one named friend", "they answer within seconds" and "help or hurt" all come from the activity itself. The handled person always decides something back (when to let go, how late to reach, which way to fall), which gives the two-way loop.
- Good: real activities bring their own plan breakers: an opponent that reads the call (lineout), an animal that learns (bull), a camera that moves (stunt fight), a chaperone that splits pairs (barn dance).
- Bad: few distinct verbs (see above), so the 8 kept ideas share a family look. Every kept idea needs split-second timing, so online lag is a real risk for all 8 (noted per idea).
- Bad: R often needs an AI that reacts to habit (bull, security, snipers, shark, rival pack). That is one simple system each, but it is the part to tune.

## Raw candidates
1. Pit: crowd-surf your friends over a festival crowd; only the surfer sees the stage's calls, only the crowd sees security, and security moves to the lanes you use most. [kept MF-1]
2. Big Top: throw the teammate you hold to a named catcher; a ringmaster calls tricks; a lion walks to where catches happen most. [cut: same "pass a person" verb as Pit]
3. Ceilidh: nobody can run; you move only by spinning with a partner and letting go; a chaperone splits pairs who keep dancing together. [kept MF-2]
4. Rosette: you can't dodge the bull yourself, only a teammate's yank moves you clear; the bull learns the team's yank timing. [kept MF-3]
5. One Take: a fake punch only sells if the named victim throws themselves back within half a second and the moving camera can't see the gap. [kept MF-4]
6. Escort: guards move the star only by shoving; only the star knows the route and a secret errand; snipers aim from the side the guards leave open most. [kept MF-5]
7. Lineout: lift a jumper on a call while the thrower lobs; the AI pack marks the spot you threw to most. [kept MF-6]
8. Tread: push a friend up for a breath and you sink; the shark comes to the splash rhythm. [kept MF-7]
9. Freefall: gripping a friend's wrist joins your spins; the next formation shows only when the current one locks. [kept MF-8]
10. Derby Whip: the jammer speeds up only when a blocker slings her; the AI pack walls the side you whip on. [backup: close to Ceilidh's hand-fling verb]
11. Rip: a panicking swimmer drags under whoever grabs from the front; the panicking player chooses limp or flail. [cut R: "go limp when the rescuer is close" settles it]
12. Hold Me Back: a heckler insults one friend, who lunges; only friends grabbing their arms hold them back. [cut P3: the insulted player has no reason to strain]
13. Ratchet: a stunt rigger yanks the performer on the director's live cue. [cut: same yank verb as Rosette; the cue is an order, not a choice]
14. Basket Toss: two bases throw a flyer; judges punish repeated tricks. [cut P1: two bases pool one throw]
15. Castell Walk: a walking human tower; each lower player steps under the lean above. [cut R: "strongest at the bottom" plan card; near stations on one vehicle]
16. Stretcher: carriers carry a player-patient who sees the ceiling crack. [cut P1: carriers pool on one stretcher; the patient "sees for others"]
17. Spotter: climbers fall; only the spotter they shout for can catch; holds crumble on touch. [cut: same catch verb as Pit; spotters wait idle]
18. Tag Team: only one player fights an adaptive boss; a tag swaps instantly. [cut F5: idle bench at 6; WWE tag mode]
19. Over the Wall: climb only by stepping on a teammate's hands; the last one is pulled up. [cut R and N: "tallest last" plan card; PEAK-style boosting]
20. Ice Chain: lie flat in a grip chain to reach a friend through the ice. [cut: a rope-tied crew in another shape]
21. Zero-G Push: in zero gravity you move only by pushing off a teammate, and both fly apart. [cut: same family as Ceilidh; push-off exists in Echo VR [memory]]
22. Piggyback: climb on a friend's shoulders; the bottom one walks, the top one uses hands. [cut: one limb each / stations]
23. Marshals: push and point AI crowds to the exits. [cut P1: acts on AI people, not friends]
24. Fireman's Carry: the carried player holds the hose while the carrier walks. [cut: station split; dragging downed players is common in shooters]
25. Pickup Rider: ride alongside and pull a teammate off a bucking horse; the rider chooses when to let go. [cut: same yank verb as Rosette; pairs]
26. Synchro Lift: underwater bases push a flyer up and run out of breath. [cut P1: bases pool; the flyer waits]
27. Pairs Throw: throw your partner on ice; they choose how many turns. [cut F5: fixed pairs, odd sizes fail]
28. Kabaddi Chain: defenders hold hands to trap an AI raider. [cut: chain reads as rope-tied]
29. Leapfrog: move only by vaulting a crouched teammate, who chooses when to pop up. [cut R: no plan breaker found]

## Kept ideas

### MF-1 Pit
- Rule (one sentence): A crowd-surfer can't move alone; the friend under them shoves them toward another friend, who must get their hands under the landing spot within a second or the surfer drops.
- Fantasy (who you are, what you're doing): A gang of friends at a festival passing each other over the crowd to get to the spots the singer points at before the last song ends.
- Aesthetic (one line): A sweaty night crowd from above, strobes, a sea of raised hands, security in yellow vests.
- Player on player (what my action does to a friend, and what they decide back): My shove sends Mira gliding 3 m toward Sam. Mira can kick once to bend her path, or dive down and pull the friend under her up to surf in her place. Sam must run under the landing spot in time. A good shove gets her to the spot; a bad one drops her in front of security.
- Why the plan can't settle (what changes round to round because of the players): Only a surfer, lying on their back, sees the stage. The singer points at a new spot mid-song (the barrier, the sound desk, a flare), so the surfer has to call it. Only the crowd sees the floor, so they have to call where security is. Security walks to the lanes the team used most this song, so yesterday's route is today's trap.
- Hub (the one shared thing everyone uses): The surfer's body.
- At 3 / at 6: At 3, one surfer and two catchers sprinting under every glide. At 6, two surfers and four catchers who must choose which surfer to serve, so lanes cross and catchers get double-booked.
- Hidden (what, how uncovered, why hide): The stage call (only surfers see it) and security's spot (only the crowd sees it). Uncovered by swapping who surfs or by calling it out. No reason to hide, since it comes from where your body is (F6 weak).
- A failed run (what happens, who is blamed): Theo shoves Mira left; Sam is half a step late; Mira drops by the barrier and security drags her out. The landing marker shows the empty spot, so it was Sam's late run or Theo's shove toward nobody. Both are visible.
- Lag note: catch timing within ~1 s; tolerable if the server decides the landing spot at the shove.
- N [memory, unchecked]: no co-op game known where a teammate is passed over a crowd. Knockout City's "ball form" (throwing a curled-up teammate, PvP) is the nearest.

### MF-2 Ceilidh
- Rule (one sentence): Nobody can run on the dance floor; you move fast only by grabbing a friend's hands and spinning, and you both fly off when either of you lets go.
- Fantasy (who you are, what you're doing): Guests at a rowdy village barn dance, flinging each other across the floor to land in the spots the caller shouts.
- Aesthetic (one line): A warm wooden barn seen from above, a fiddle band, swirling skirts, a cake table to avoid.
- Player on player (what my action does to a friend, and what they decide back): I grab Lea and we spin. Each of us decides when to let go, and the first to let go sets the moment for both. We fly opposite ways, so where she lands depends on my timing as much as hers. Let go well and she lands in the spotlight; let go badly and she lands in the cake.
- Why the plan can't settle (what changes round to round because of the players): The caller lights a new spot every few seconds ("one to the fiddler!"), so who must land where changes live. The chaperone walks toward any pair that spins together twice in a row and freezes them for 3 s ("change partners!"), so the team can't keep its best pair and has to rotate.
- Hub (the one shared thing everyone uses): The dance floor and the caller's spotlights.
- At 3 / at 6: At 3, one pair spins while the third walks to where the next flier will land to grab them. The chaperone forces rotation, so nobody stays out. At 6, three pairs spin at once and flights cross mid-floor.
- Hidden (what, how uncovered, why hide): none.
- A failed run (what happens, who is blamed): Kai lets go early; Lea flies into the cake; the spotlight goes out empty. The replay shows Kai's hand opening first.
- Lag note: both players' release inputs must be judged on one clock; the server takes the first release.
- N [memory, unchecked]: no known game where movement comes only from partner spins. Heave Ho and Human: Fall Flat grab-and-swing are the nearest.

### MF-3 Rosette
- Rule (one sentence): You can't dodge the bull yourself; the only way out of a charge is a friend yanking you a step toward them, which roots them in place for a second.
- Fantasy (who you are, what you're doing): A crew of ribbon-snatchers in a sunny southern arena, reaching for the rosettes on a bull's horns as it charges.
- Aesthetic (one line): A white-washed arena, dust clouds, red rosettes, a roaring crowd.
- Player on player (what my action does to a friend, and what they decide back): Mira stands in the charge to reach for a rosette. She decides how late to reach (later means more rosettes). I decide when to yank her. Too early and she misses the rosette; too late and she's tossed. After my yank I'm rooted, so the bull may turn on me and Sam has to yank me next.
- Why the plan can't settle (what changes round to round because of the players): The bull learns the team's habit. If yanks always come at the same distance it stops short and hooks toward the rooted yanker. If the same friend always yanks, it charges that friend first. Each charge's target is the bull's choice, revealed as it lowers its head.
- Hub (the one shared thing everyone uses): The bull.
- At 3 / at 6: At 3, every charge involves a snatcher, a yanker and the one who must cover the rooted yanker. Nobody rests. At 6, two bulls in one arena; yank chains cross between them.
- Hidden (what, how uncovered, why hide): none (the bull's fake is visible if you watch its head).
- A failed run (what happens, who is blamed): Sam yanks Mira a quarter-second late and she's tossed out for 10 s. The replay shows the horn arriving before Sam's yank.
- Lag note: the yank window is tight (~0.3 s); the server must judge it.
- N [memory, unchecked]: no known course camarguaise game; "only a teammate can dodge for you" not known as a core rule.

### MF-4 One Take
- Rule (one sentence): A punch you throw at a named friend only sells on film if they throw themselves back within half a second and the moving camera can't see the gap between fist and face.
- Fantasy (who you are, what you're doing): A stunt team shooting the big bar-brawl scene of an action movie in one unbroken take.
- Aesthetic (one line): A saloon set with the film crew visible, a camera dolly on rails, film grain, slapstick crashes.
- Player on player (what my action does to a friend, and what they decide back): I swing at Lea. She decides within half a second which way to fall: back over the table, into the window, onto Kai. A good sell scores big; a late sell is a real hit and she's "injured" for the take. Falling onto Kai hands him the next beat.
- Why the plan can't settle (what changes round to round because of the players): The camera rolls along a path revealed as it goes, so which side a punch must come from changes every few seconds. The director shouts open goals live ("somebody through the window!", "two hits on the same guy!"), and the team picks who. The director gets bored of repeats ("seen it, give me something new"), so the team's favorite combo stops scoring.
- Hub (the one shared thing everyone uses): The camera and its frame (drawn on the floor).
- At 3 / at 6: At 3, triangle fights (one holds, one hits, one sells). At 6, two fights in the room and the camera chooses which one it's on, so the other fight must reposition into frame.
- Hidden (what, how uncovered, why hide): none (the camera frame is shown on the floor).
- A failed run (what happens, who is blamed): The camera swings to Theo's side; his punch at Lea shows a clear gap; "CUT!" The replay shows the gap from the lens and who was out of line.
- Lag note: half-second sell windows; the server judges each beat.
- N [memory, unchecked]: no known co-op game where the victim sells a fake hit for a moving camera. Stuntman (2002) is solo driving.

### MF-5 Escort
- Rule (one sentence): Guards can move the star only by shoving them, and only the star knows where to go.
- Fantasy (who you are, what you're doing): A security detail rushing a pop star from the car to the stage door through fans and snipers.
- Aesthetic (one line): A red carpet at night, camera flashes, black suits and sunglasses, red laser dots.
- Player on player (what my action does to a friend, and what they decide back): I shove the star 2 m out of a laser line. The star decides to go with it or push back toward their route. The star can also grab a guard by the arm and pull them in as a shield. My shove can save them, or push them into a second laser.
- Why the plan can't settle (what changes round to round because of the players): The star's route can change mid-walk (a phone call only the star hears). The star also has a secret errand (a selfie with a fan, a hot dog) for a private bonus, so guards can't tell a real turn from a selfish one. Snipers aim from the side the guards left open most this run, and fake from the covered side.
- Hub (the one shared thing everyone uses): The star's body.
- At 3 / at 6: At 3, one star and two guards who can't cover everything. At 6, one star and five guards with more snipers, or two stars who must stay close.
- Hidden (what, how uncovered, why hide): The route and the secret errand, uncovered by the star saying it or by reading where they push. The star hides the errand for the private bonus.
- A failed run (what happens, who is blamed): Theo shoves the star left out of one laser into another; the star is shot. The replay shows Theo's shove and the second dot.
- Lag note: shoves are physics pushes; moderate lag risk.
- N [memory, unchecked]: escort missions are common, and Counter-Strike's old VIP mode has a player VIP (PvP). Guards moving the VIP only by shoving while the VIP holds the route is not known to me. Likely ~ (shares escort core, changes who decides).

### MF-6 Lineout
- Rule (one sentence): A jumper only gets up when a teammate lifts them on the call, and the thrower lobs to whoever is up while the AI opponents try to read the call.
- Fantasy (who you are, what you're doing): A rugby pack in the rain stealing lineouts from a rival team that seems to read your mind.
- Aesthetic (one line): A muddy floodlit pitch, rain, steam rising off the players.
- Player on player (what my action does to a friend, and what they decide back): I lift Kai. He decides the jump moment and whether to catch or tap the ball down to a named teammate, who must run with it. Lift him a beat late and the ball sails over his hands.
- Why the plan can't settle (what changes round to round because of the players): The AI pack lifts its own jumper at the spot the team threw to most in the last 5 lineouts, and jumps early if a lifter crouches early. The thrower must pick live, after seeing where the AI went, and the pods can fake (dummy lift) to drag the AI.
- Hub (the one shared thing everyone uses): The ball in the air.
- At 3 / at 6: At 3, thrower, lifter and jumper with two possible spots; the pair picks a spot after the call and the thrower must follow. At 6, thrower, two pods, and a receiver for the tap-down. At 5, thrower and two pods.
- Hidden (what, how uncovered, why hide): The call is said on voice; the AI reads only past throws and early crouches. None hidden between players.
- A failed run (what happens, who is blamed): Mira lifts Kai a beat late; the AI jumper steals it. The replay shows the late lift.
- Lag note: lift and throw timing within ~0.5 s.
- N [memory, unchecked]: rugby games (e.g., Rugby 22) have lineouts, but one person controls them. A co-op lineout where each friend is a lifter or jumper vs an AI that reads habits is ~ (shares the core, changes who decides).

### MF-7 Tread
- Rule (one sentence): In the water you can push a named friend up for a breath, which pushes you under; air only comes from friends.
- Fantasy (who you are, what you're doing): Shipwreck survivors at night keeping each other's heads above water until the rescue boat arrives.
- Aesthetic (one line): A black sea, lifejacket lights, the sweep of a searchlight, a fin in the beam.
- Player on player (what my action does to a friend, and what they decide back): I push Lea up; she must take the breath now (press to breathe) or waste it. Then she decides whether to push me back up or save her strength for Sam. A push at the wrong time lifts her into the shark's view.
- Why the plan can't settle (what changes round to round because of the players): The shark goes for the friend who was just lifted and learns the team's rhythm, so a steady ring of pushes gets punished and the order must change live. Floating crates drift in (one free breath, one person), and who gets it changes who needs pushing next.
- Hub (the one shared thing everyone uses): Each other's air, traded body to body.
- At 3 / at 6: At 3, a tight ring where every push matters. At 6, two rings that can swap members, and the shark picks between them.
- Hidden (what, how uncovered, why hide): Each player's exact air is shown only as their face color; you must ask or watch. No reason to hide (F6 weak).
- A failed run (what happens, who is blamed): Sam pushes Lea up right as the shark turns to her; she's bitten and out. The replay shows Sam's push and the shark's turn.
- Lag note: low; pushes and breaths are not split-second.
- N [memory, unchecked]: no known co-op game with body-to-body air trade.

### MF-8 Freefall
- Rule (one sentence): When you grab a friend's wrist in freefall, you two spin and fall as one, and the next formation is shown only once the current one locks.
- Fantasy (who you are, what you're doing): A formation skydiving team in competition, building shapes in the sky before the altimeter beeps.
- Aesthetic (one line): Clouds far below, bright jumpsuits, roaring wind, a sky-camera frame.
- Player on player (what my action does to a friend, and what they decide back): I grab Sam's wrist; my spin becomes his. He must grip back or let go within a second. A clean grab steadies him; a hard one sends us both tumbling out of the shape.
- Why the plan can't settle (what changes round to round because of the players): Each jump draws 4 to 6 formations from a short list, shown one at a time. The best way into the next shape depends on who is holding whom right now, which is only known when the current shape locks. Each diver also gets a private photo card ("be in the middle when shape 3 locks") for a personal bonus, so someone may drift toward a spot the team didn't plan.
- Hub (the one shared thing everyone uses): The formation in the sky.
- At 3 / at 6: Shape lists for each crew size (about 10 each). At 3 shapes are lines and triangles; at 6, stars and rings with more grips to break and make.
- Hidden (what, how uncovered, why hide): The private photo card, uncovered by watching who drifts where. Hidden for the personal bonus.
- A failed run (what happens, who is blamed): Kai grabs Sam's wrist too hard and the pair tumbles away; the shape doesn't lock before pull altitude. The sky-cam replay shows Kai's grab.
- Lag note: grabs on moving bodies; moderate risk.
- N [memory, unchecked]: skydiving games exist (solo or PvP wingsuit); no known co-op formation builder. R is the weakest of the 8 (the formation draw is the main plan breaker).
