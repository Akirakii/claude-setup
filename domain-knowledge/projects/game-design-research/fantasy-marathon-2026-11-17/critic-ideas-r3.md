# Critic round 3 on Storm Sailors (2026-11-17)

Isolated critic, standing in for the user.
Tags: (searched) = one of my 7 web searches; (paper) = played in my head; (script) = a toy simulation I ran; (memory) = not searched.
Pass or fail only.

**Verdict on the base: fail.** Hitting a friend is never the right move for a crew with one interest, so good play has no contact at all, and what is left is "tap your rope when it slips, in turns".

## The plan that wins (paper, then script)
Numbers I used: a sail slips every 4 s, a haul takes 0.5 s, a flap rips after 2 s (the only number the idea writes).
- Everyone stays crouched by default and stands only for the half second of their own haul.
- Before standing, look whether a friend you cross is standing; if so, wait for them to crouch.
- Crouching while your sail is trimmed costs nothing, because "can't haul" only matters when there is something to haul.
- The half-second duck under a swing is gone, so no reflex and no call is needed.

## Played storm
- **3 players, storm 1 (paper).** Ana's main slips; Ben and Cy are already crouched; Ana stands, hauls, crouches. Ben's jib slips at 1.2 s; he hauls. Cy's slips at 1.4 s while Ben stands; Cy waits 0.3 s, then hauls. Longest flap 0.8 s. Whole storm: 0 rips, 0 knock-downs.
  - The hauler decides: now or 0.3 s later. Later is always right, because a wait under 2 s costs nothing.
  - The one in the arc decides: nothing. He is already crouched.
- **3 players, the pool's reading (stand by default, duck on a call).** Ana says "main!", Ben taps crouch, Ana hauls. Ben obeys; ducking always beats being knocked flat, so he has no second option.
- **6 players (paper + script).** Same plan with longer queues. Either the queue fits inside 2 s and the season has 0 rips, or it does not and a sail is torn off in storm 1 or 2 whatever anyone chooses.
- **1 human + bots.** Bots crouch by default and haul on a timer; the human waits for a bot to crouch. If a bot hauls through the human, the human gets no call (bots do not talk), so it is a reflex test against a tell that is not written.
- **Storm 20.** Ten seconds of "which arcs cross my rope", then the same plan. Rigging the ropes anew moves the numbers, not the plan.

## Findings

**Severe 1: the choice has one answer.**
Problem: a knock-down costs the victim's rope time, plus the slide, plus a grabber's rope time; a wait costs the hauler a fraction of a second.
One crew, one interest, every boom in plain sight: this is the reason Low Tide and Overloaded were dropped, and the file's drop-reason row did not run it.
Example: Cy waiting 0.3 s for Ben. In the script, hauling through a friend when your own sail is about to rip never lost fewer seasons than waiting, in any of 54 settings (script).
Fix direction: something outside the crew must make hauling through a friend right some of the time, and it must cost more than one rip to wait.

**Severe 2: the one in the arc decides nothing (co-op check point 7).**
Problem: "duck" is the only answer to a boom, and "stay crouched" removes even that.
Rounds 1 and 2 dropped Dragon's Hoard v2 (freeze), Sleepover (stand near) and Parade Dragon (hold) for an end that only obeys; this is the same end.
Example: Ben in both 3-player scenes.
Fix direction: the friend in the arc needs a second option with its own price (take the hit to finish something, or block the boom at a cost).

**Severe 3: it is the user's dropped family.**
Problem: the file's claim "my job lands on a friend's body" is true in storm 1 only.
By storm 5 the best play is the family's own line from postmortem-rows.md: "everyone does the same simple job side by side".
The ship is the one machine, the slipping sails are the dealt events, and Hordeline's question stands: "how these games make the one machine running fun?".
Contact with a friend is a mistake to avoid, not an act to choose, so the better the crew, the less the idea exists.
"The grabber leaves their own rope" is "hands are scarce", the rule Claude carried from Red Button into Pet the Cat.
Example: the 0-rip, 0-hit storm above.
Fix direction: none found that keeps "keep the sails trimmed" as the job.

**Severe 4: the one ratio has a knife edge, and past it there is a spiral with no way back.**
The ratio: (friends whose arcs I share + 1) × haul time, against the 2-second rip time.
Script, 54 settings (3 and 6 sailors; slip 3, 4, 6 s; haul 0.3, 0.6, 1.0 s; arcs crossing 2, 4 or 5 friends; a rip speeding the slip by 15% or 30%):
- 24 settings: 0 rips and 0 hits in all five storms. Free.
- 27 settings: a sail is torn off by storm 2 in every season. Lost, with no choice involved.
- 2 settings: a sail is lost in half or more of the seasons.
- 1 setting (6 sailors, slip 6 s, haul 0.6 s, 4 crossings, 15%): about one rip per storm and no sail lost. That is the game the file describes.
Problem: a ripped sail slips faster, which makes more waits, which makes more rips, and nothing repairs a rip.
This is "a carried harm with no way back = a death spiral" (critic-anti-patterns), which the same fix file caught for Hermit Crabs and not for this idea.
The pool's line "ducking costs your own sail" is false whenever a duck is shorter than the 2-second allowance.
The script is a toy: no walking, no overboard, no wind. It shows the shape, not real numbers.
Fix direction: a way to mend a rip that needs a friend, and a cost for crouching that does not depend on timing.

**Severe 5: rules the idea leans on are not written, and no reading saves the choice.**
- What a haul is (a tap, or a hold, and how long). Everything above turns on it. If it is a tap, a sailor can also stand one step outside the arc and step in to haul, so "every rope stands inside another arc" does not close the safe spot.
- Whether a boom gives a warning. Without one, ducking is only possible on a call. With one, it is a reflex.
- How long a knock-down lasts, and whether every knock ends at the rail.
- What the wind deals. The pool says "which sails need which ropes"; the file says "which sails matter". If some sails do not matter, their sailors are idle. If ropes are remapped, it is a memory quiz. Neither touches the crouch plan.
- What a flapping sail costs inside a storm. Nothing is written, so a storm cannot be lost; "keep the ship on course" has no rule behind it.
- What a torn-off sail means. The pool's goal is "every sail still on its yard"; the file's scene has the crew "choose whose sail they let go". If a lost sail loses the season, nobody can let one go. If it does not, tearing off the boom that crosses the most ropes in storm 1 is the plan, and its sailor becomes the full-time grabber.
- The waves an overboard sailor "calls". Waves do nothing in the rules, so the job in the water is empty.
Fix direction: write these seven before any more scenes.

**Severe 6: the research rows show the feeling, not this rule.**
- Helldivers 2: the quote and the green laser are real; the laser point is a PC Gamer writer's, not the director's (searched). Friendly fire there is a side effect of fighting enemies who force mistakes "under pressure" (searched). Storm Sailors has no enemy; its only pressure is a timer the crew can schedule around. Fail.
- Overcooked: Game Maker's Toolkit says its kitchens "disrupt these comfortable patterns", and PC Gamer's reviewer "fell into regular roles" (searched). The shouting is kept alive by level content, which this idea rules out. Fail.
- Keep Talking: talk is forced by split information. Everyone here sees every boom. Fail.
- Left 4 Dead: the pin comes from an enemy that hunts stragglers. Here it comes from a mistake the plan removes, and any friend can grab, which checks.md 0.2 marks as a fail ("anyone being able to do it") and which got Hold the Door dropped. Fail.
- Same relation between players (one crew): pass.
Fix direction: mark the three rows as "feeling exists, rule not borrowed".

**Medium.**
- "Shout a countdown, everyone ducks": wins and is free on Discord. Fail. The crouch plan is stronger still.
- "The one nearest the rail grabs": wins; five seconds is long and anyone can do it. Fail.
- "Spread the rips evenly": harm grows faster the more rips one sail has, so even is right, from facts all can see. In the script there is nothing to spread: rips are zero or a runaway. Fail.
- "Sacrifice one sail early": see severe 5. Fail while the rule is unwritten.
- Minigame or game: fail. Nothing is chosen between storms, and the fix file's own test is "the carry-over must change a push choice next round"; there is no push choice.
- More friends make my job harder, not possible. A lone sailor at one rope has no hazard. That is the reverse of "my action fails without yours".
- "Being the one everyone saw do it" is listed as the hauler's price. It is not a cost in the rules.
- The file's write-up drops two pool rules: "every rope stands inside another rope's arc" and the 20-second wind. The season rule and the scenes match the pool.
- The file's "works at 3 and 6 with nobody idle ✅" rests on two one-line pool scenes that never asked what the other end decides.
- Lag, as written: fail. A half-second duck against a boom timed on another machine loses a third of its window at 150 ms, and one of the two players sees a wrong result (the boom passes through a standing friend, or knocks a crouched one). That breaks the visible blame.

**Minor.**
- Co-op boats are a crowded shelf: Mayday Vacay (tilting boat, sliding cargo, oars that knock a friend overboard, in playtest), Barely Afloat, Are We Sinking Yet?, Water You Doing, In the Same Boat, Rock the Boom, Shore (searched).
- Shore is a raft with paddles, not sails; the file's use of it as a neighbour is fair (searched).

## What is sound
- The fantasy does not ask one player to want and fear the same thing. Pass.
- The premise is free: three searches found no game where the crew's own rope work sweeps the deck (searched). Pass.
- Blame is one visible body doing one visible thing. Pass, and it is the best part of the idea.
- No monster, one deck, physical verbs, bots that can do every job. Pass.
- Scope: pass for a test build in days and for 3 to 4 months, if booms are timed arcs with a tell (not physics) and the deck's tilt is faked. Costliest part: the knock-down and slide reading the same on every screen.
- Lone survivor: pass, nobody dies. Dying on purpose: pass, the water gives nothing.

## Co-op check
1 coupled fail · 2 split fail (same view, same role) · 3 talk fail by storm 5 (pass in storm 1) · 4 blame pass · 5 not easy fail (a storm cannot be lost; a season is free or lost by the tuning) · 6 not solo fail (not written whether one runner can haul three ropes) · 7 two-way fail.

## The checks in the brief, marked
1 base: fantasy pass, cited games fail, premise pass · 2 rules written: fail · 3 nobody only obeys: fail · 4 roles gain and pay: fail · 5 no winning plan: fail · 6 the ratio holds across numbers: fail · 7 co-op check: fail (1 of 7) · 8 not the dropped family: fail · 9 scope pass, lag fail as written.

## What the method let through this time
- An idea from the pool was taken as already checked; its scenes are one line each and its critic lines carry no numbers.
- The drop-reason row found one reason and missed three (Low Tide's one interest, Hold the Door's nearest friend, the obeying end from round 2).
- Nothing asked "what does a perfect crew's storm look like?"; here the answer is a storm in which the idea does not happen.

## Sources
- Helldivers 2: https://pcgamer.com/helldivers-2-friendly-fire · https://pcgamer.com/games/third-person-shooter/helldivers-2s-friendly-fire-and-killer-bugs-show-the-fragility-of-humans-and-are-also-just-funny-creative-director-says · https://gamertweak.com/why-helldivers-2-makes-team-mistakes-fun
- Overcooked: https://www.pcgamer.com/overcooked-review · Game Maker's Toolkit transcript https://amara.org/videos/1kyGmzeQjsv6/en/2301030
- Boats: https://store.steampowered.com/app/4588510 · https://store.steampowered.com/app/4466930/Are_We_Sinking_Yet/ · https://store.steampowered.com/app/4429930/Water_You_Doing/ · https://store.steampowered.com/app/2548410 · Shore https://store.steampowered.com/app/4280880
- Script: /tmp/claude-1000/-home-akiraki-claude-code/0ad3d467-42c9-44fe-bdb6-4b4ce51d7d54/scratchpad/storm2.py (a temporary folder; rerun or copy it if the numbers matter).

**Final: drop as written (6 severe, all on the base). Worth five minutes of the user's time, for one reason: it is the only idea of the eight with a free premise, visible blame and a days-long test build, and its storm-1 slapstick is the part a shipped game backs; a rework would need a new haul rule and an outside force, which is the user's call, not a version 2 on paper.**
