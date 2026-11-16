# Critic: bluff rules, round 1 (2026-11-15)

Isolated critic on `bluff-rules-thesis.md` and design.md "Trust and bluff" (rounds 15–21).
Numbers come from a script (`symptoms.gd` pacing, `curse_rules.gd` hunger, `move.gd` speeds, GAP formula), not guesses.
Code read: `night_sim.gd` (give, steal, tug), `body.gd` (held items drawn), `symptoms.gd`.

## Verdict on the problem underneath: wrong shape
"Add rules until one lie works" is the wrong shape, and the pile is partly an illusion.
- 5 of the 10 "rules" change nothing in play: the core-lie line is a goal, chain snap and wrong-item-wasted are already built or the user's rules, the swap is already possible in code (two gives at once), and the hostage trade is just "hoarding allowed".
- The real weight sits on two things that aren't rules in the list: the unbuilt, unspecified "everyone a little sick" (no rate, no fit with the case system), and an assumption that the turned friend hunts the liar.
- Whether the lie works depends on three numbers the rounds never ran: trip time vs symptom gap, how deadly "near at the turn" is vs "far", and how often a liar needs the same friends again.
- The rounds never played a built rule that matters most: steal and tug (user). It breaks two of the rules and already holds a bluff with no new rule (fake a swap, then snatch).
- Every round graded itself, and "(assumed)" counted as a pass.

Recommended: answer 3 (strip to pillars + built game), plus the numbers script, plus "everyone a little sick" specified with numbers before any bluff rule leans on it. Judge it with 3+ humans; the test crew can't carry this lie (S4).

## Numbers (script)
| Quantity | Value |
|---|---|
| Untreated case, start of night / middle / end | 58 s / 38 s / 23 s (it turns about when the 3rd symptom shows) |
| Middle of the night: every item arrives 15 s after its symptom | cured at 50 s |
| Same, 20 s after | turns at 54 s |
| Same, one item never comes (the lie) | turns at 49 s |
| Round trip to the farthest spot (108 m), sprinting, plus the 2 s give | 27 s |
| Werewolf closes on a sprinter at | 2.59 m/s (11.23 vs 8.64) |
| Hunger at 4 alive / 8 alive | 30 s / 21 s, so anyone farther than 78 m / 55 m at the turn can't be run down |
| Cases per night, 4 / 8 friends (case about 45 s) | 8.0 / 9.3, so 2.0 / 1.16 per friend; sick twice or more 63% / 33% |
| Item slots, 8 friends × 2 hands | 16, the same as all 16 items |

## Severe
**S1. The list hides where the weight is.**
Problem: see the verdict. A list of 10 looks like the design; the lie actually lives on an unbuilt system and an assumption.
Example: round 15 H3 and round 21's "caught costs ✅" both lean on "everyone a little sick (assumed)".
Fix direction: spec "everyone a little sick" (rate per friend, how it fits GAP and cases) and run the numbers before keeping any rule.

**S2. Steal and tug (user, built) were never played. They break rules 5 and 10 and hand the test crew a dominant move.**
Problem: `night_sim.steal` is instant on any item in a hand. If the owner is holding the button (giving, charging, raising), it becomes a tug that whoever walks 1 m away wins. Bots never steal and never hold on.
Example: the swap (rule 10). Ana starts giving the bucket, so she's standing still holding her button. Bo doesn't give; he aims his empty hand at the bucket, which starts a tug, and walks back 1.6 m. He has the bucket and the coffee. The swap isn't safe.
Example: the hostage (rule 5). Ana just steals Dee's coffee from Bo unless Bo keeps a button held the whole time.
Example: with bots, the human steals any item from any bot for free, so no trade with a bot ever happens.
Fix direction: replay the rounds with steal in. The fake swap is a better lie than the trip: it's built, the stakes are right there, and the body shows it. Bots need to hold on, or steal and trust have to interact.

**S3. Formula lines 3 and 4 fail for the core lie.**
Problem: being caught has to cost Bo, and there are two ways it could. (a) Dee turns and hunts him: but Bo bailed and is far away, past 78 m at 4 alive or 55 m at 8, so the werewolf eats whoever stayed, the honest helpers. (b) Bo needs these friends again: with the built cases that's 1.16 sicknesses per friend per night at 8, and only "everyone a little sick" (unbuilt) makes it real. A wrong doubt costs nothing for the same reason.
Example: 4 friends, middle of the night. Bo holds the coffee, sees Dee's veins at her face, and sprints to the tree house. Dee turns and Cy is 3 m away: Cy dies and Bo loses nothing.
Fix direction: make being near the turn pay, or make being far cost. The switches already exist (`near_head_start`, `far_shown`) and are off in step 1. Turn one back on rather than adding a rule.

**S4. The test crew (1 human + 3 bots) can't make the lie.**
Problem: the human can't promise anything to a bot. There's no voice to bots, the human's bubbles are hidden (`world_text` off), and quick chat 1–4 only says feelings. A bot werewolf hunts by its senses, not for revenge, so (a) in S3 fails as well. Bluffing goes one way only: bots lie and the human can't. This is "voice-only game tested with bots" a 6th time.
Fix direction: a physical offer verb that bots can read, such as holding an item out toward a friend. Otherwise say plainly that the lie is tested by humans only.

**S5. "Helping beats fleeing" (user) is bent without saying so.**
Problem: the lie's reason (line 2) is that late in a case, fleeing beats helping. Step 1 turned off the head starts that made helping pay. The thesis's pillars section doesn't list this.
Example (strategy that always wins): carry 2 items from dusk, never rely on anyone's trip, and when a patient's veins reach the face, scatter past 78 m (at 4 alive) or 55 m (at 8). With bots, also steal whatever you need. Bailing late is then the open norm, so not coming back isn't a lie.
Fix direction: bring this to the user. The core lie and this pillar pull in opposite directions.

**S6. Trips are too slow in the middle of the night, so the best play removes trips.**
Problem: in the middle of the night each item has to arrive within about 15 s of its symptom, and a far trip is 27 s. So everyone carries items ahead of time: 16 slots for 16 items at 8 friends. Help then happens face to face, which rule 10 makes the default. Round 21 already says it: "being a known liar now only costs on trips".
Fix direction: decide whether trips should be the core. If they should, check item distances against `spacing()`. If not, move the lie to the meeting (S2).

## Medium
- **M1. The 8-friend scene can't happen in the built game.** Doubles are off and the next case waits for the werewolf to finish, so while the werewolf is out nobody is sick and nobody trades. The scene only exists with "everyone a little sick". With it, a 2 s give within about 22 m of the werewolf is a meal, all trades stop for about 30 s, and "the wolf was in the kitchen" is an excuse nobody can check.
- **M2. The bot rules contradict each other.** "Lie only late" vs "keep promises by how much they trust you": a bot that trusts you little and breaks a promise early is lying early.
- **M3. Rules pile up (×6).** Before: 8 things a player must know (symptom→item table, 2 s give on a friend standing still, no treating yourself, the chain, steal and tug, throw and drop, turn/hunger/catch, the wolfsbane shove). The 3 taught rules still describe the old signs and cures. After: 10 for an all-human crew (+ everyone a little sick, + reading the refill), 16 for the test crew (+ 5 bot behaviours, + reading deal bubbles).
- **M4. "Lies never from a reward" and "betraying never pays more" both bend.** In round 17 Bo gets the bucket and keeps the coffee. Its fix is "Dee hunts Bo", which S3 breaks with numbers. The thesis marks "never pays more" as kept (assumed); it isn't.
- **M5. The last minute still fails line 3.** Round 21's all-pass table leaves it out.

## Minor
- m1. Deal bubbles bend "no text at night" (user OK'd them for bots).
- m2. Rules 4 and 6 are already built, so they only make the list longer.
- m3. Rounds 15–21 graded "(assumed)" as a pass (CLAUDE.md rule 23).

## Checks for the core lie ("I'll get the coffee", then not coming back late), with today's rules + the 10
| Co-op point | | Why |
|---|---|---|
| 1 Coupled | pass | nobody treats themselves |
| 2 Split | pass | only Bo knows his intent, and anyone can fetch |
| 3 Talk | fail | passes for humans on voice; the test crew can't talk to bots |
| 4 Blame | fail | a broken promise is an absence, the same as an honest 27 s trip that came too late |
| 5 Not easy | pass | a case lasts 23 s at the end |
| 6 Not solo | pass | 3 items, 2 hands |
| 7 Two-way | fail | the patient only stands still and waits |

| Bluff line | | Why |
|---|---|---|
| 1 Only one knows | pass | intent |
| 2 A reason | pass | being far at the turn (78 m / 55 m) |
| 3 Caught costs | fail | S3 |
| 4 A wrong call costs | fail | same dependence on an unbuilt system |
| 5 Checking costs | pass | a trip |
| 6 Honest not always best | pass | late in a case |
| 7 Again and again | pass | about 8–9 cases × 3 items a night |

## Playing without each rule (backtrack)
All 10 are Claude's picks, OK'd by the user in bulk ("add the rules").
| # | Without it | Real hole? |
|---|---|---|
| 1 Core lie is jobs | nothing changes in play | no |
| 2 Bots lie late, trust, fear | bots are honest, so the test crew never sees a lie | yes, but one rule covers it |
| 3 Thrown-off friend runs | built catch: already free, nobody can be caught in the 2 s turn | only in the user's unbuilt attack, so a question for the user |
| 4 Chain snaps | built | no (removing it would be a change) |
| 5 Cure held as a trade | "hoarding allowed" already says it | no |
| 6 Wrong item only wasted | the user's rule, built | no |
| 7 Bot deal bubbles | bots can't offer deals | no while the human can steal from bots |
| 8 Bots trust what they saw, never tell | bots would tell, so the game exposes a liar | yes |
| 9 Refilling spot | 2 items per spot: the count already shows what's gone for 60 s; after 60 s the refill shows nothing either way | no |
| 10 The swap | two gives at once already work in code | no, and its "safe" claim is false (S2) |

## Keep / cut / change
| # | Rule | Call | Note |
|---|---|---|---|
| 1 | The core lie is about jobs | change | a design goal, not a rule; check it with the trip numbers (S6) |
| 2 | Bots lie late, trust by kept promises, fear beats trust | change | one rule: late in a case, fear makes a bot bail; trust comes from gives it saw (the human can't promise) |
| 3 | A thrown-off friend runs | keep, as a question | only matters for the unbuilt attack; goes to questions.md |
| 4 | The chain still snaps | cut from the list | built, nothing to learn |
| 5 | A held cure can be a trade | cut | follows from hoarding; steal breaks it; bends "never from a reward" (user's call) |
| 6 | A wrong item is only wasted | cut from the list | the user's rule, built |
| 7 | Bot deal bubbles | change | only with a physical offer verb for the human that bots read (S4) |
| 8 | Bots trust only what they saw, never tell | keep | protects "never exposes liars"; merge into 2 |
| 9 | The refilling spot | cut | the count at the spot already checks it |
| 10 | Giving to each other at once | cut | already built; "safe" is false under the tug |
