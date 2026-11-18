# critic-anti-patterns

What isolated critics keep catching in Claude's design proposals (CLAUDE.md rule 20): pattern, ×count, fix.
Scan it before writing a proposal; after each merge, add an entry or raise a count.
A/B items are in `~/.claude/design-anti-patterns.md`.
The stories behind them are in each project's critic and merge files (Deathly Reality Show and Moonsick `docs/`, `game-design-research/research_notes/`).

## Caught by the user after the critics passed it
- **A reward that ends the need for others** ×1 (once cured for good, losing trust stopped mattering).
  Fix: no safe state; a catch gives what a cure gives.
- **A loss the numbers can't reach** ×1 (there was no way to lose a night).
  Fix: work out the worst one round can do before adding stakes across rounds; one long round carries final deaths.
- **A voice-only game tested with bots** ×7 (Moonsick bluff rules: the human can't promise to bots; a bot carries without a word, so "words are noise" cost nothing).
  Fix: it must work with the user's test crew (1 human + bots), using physical verbs bots can answer.
- **Hidden rules patched with words** ×3.
  Fix: if the one-sentence rule needs a second sentence, change the game, not the text; practice stages teach the rules.

## Teaching and text
- **Instructions written from the system's view** ×1.
  Fix: say what the player who sees it does.
- **Rules pile up uncounted** ×6 (Moonsick bluff rules: 21 rounds only added rules, half already built).
  Fix: ≤ 3 taught rules, the rest left to objects, discovery or hidden numbers.
  After a merge, count every switch a player must know, at both ends, before vs after; move extras to a later game.
- **Text piles up** ×3.
  Fix: one word budget for all short-lived text (HUD line ≤ 8 words); new teaching replaces old; one channel per fact.
- **A budget rule with no stated scope** ×1.
  Fix: name what it covers.
- **The dead get only a voice** ×3.
  Fix: a visible physical job bots can read; a ghost who helps a cure comes back.
- **An untaught rule breaks what players said** ×1.
  Fix: signal it ahead, or keep the said word valid.
- **Claiming ownership the rules don't have** ×2.
  Fix: word each line from the rules' real data.
- **The hardest rules get the least teaching** ×2.
  Fix: teach in proportion to difficulty.
- **A shared screen leaks the split information** ×1.
  Fix: shared displays show examples, never live secrets.
- **The game names the answer** ×3 (the signs the user found hard to read did nothing).
  Fix: tools show signs; guidance teaches each verb once, never the decision; notes log facts, and putting them together stays the player's job.
- **A teaching line sends everyone to one spot** ×1.
  Fix: only in a solo practice coach.
- **Only one side of a split built or taught** ×2.
  Fix: build and teach both sides (human patient + bot doctors).
- **Opposite next steps with alike feedback** ×1.
  Fix: make them differ in shape and direction, not strength.
- **Readability fixed, choice still dead** ×1 (the user saw no choices).
  Fix: simulate the core choice first; each option must win somewhere.

## Space, look and the code
- **A rule zone unmarked** ×1 **or marked wrong** ×1.
  Fix: draw the zone, exactly.
- **Decoration where the surface could carry rules** ×1.
  Fix: one mechanism for look and teaching.
- **A screen showing its own feed** ×1.
  Fix: graphics on the big screen; the TV view shows the same.
- **A claim about the build not checked in the code** ×7 (Moonsick bluff rounds never played the built steal and tug; bluff-all: the wolf sprints, it doesn't walk).
  Fix: read coordinates, data structures, ranges and the draw rule in the code before a proposal leans on them.
- **Copying bot perception copies its privileges** ×1.
  Fix: a player sees only by distance, light and earshot.
- **A map drawn without checking which way the axes go** ×1.
  Fix: take the axes from the engine (Godot +X right, −Z forward).
- **Danger feedback through walls works like a radar** ×1.
  Fix: it needs line of sight.
- **Art that doesn't match its collision** ×1.
  Fix: fit the art to the gameplay box.

## Phases, flow and time
- **Practice leaks into the live game** ×1.
  Fix: reset positions and hidden info; real pressure, minus the deaths.
- **Practice with no cost** ×1.
  Fix: a mistake resets progress.
- **One player skips or carries the learning** ×2.
  Fix: each player's own ticks gate the start; don't blame a side cause (like the bots) for the user's confusion.
- **Added phases × every level** ×1.
  Fix: count the seconds per show; teach once, forgive once.
- **One key with several jobs** ×1.
  Fix: a separate key for moving through the flow.
- **The rule changes per phase** ×1.
  Fix: one exception rule for every phase.
- **A state change in the middle of an action** ×2.
  Fix: freeze actions already in motion; a grace time; a held button flips once at most, toward safety; every other verb needs a fresh press.
- **A fix that undoes an earlier fix** ×6 (voices that count only while the eye is open contradicted "our voices stir it"; smoke meant to stop waiting sent the crew to a safe spot).
  Fix: check every earlier round's fixes again.
- **One task at a time = a calm conveyor belt** ×2.
  Fix: tasks overlap and speed up.
- **A limit that's never reached** ×4.
  Fix: check it against the real value; scale it with the people left.
- **An undefined failure state** ×1.
  Fix: write what each object does if nobody touches it.
- **Test setups that deadlock** ×3.
  Fix: every bot wait has a timeout and a fallback; play the test crew through each step.
- **A cost that jumps instead of sliding** ×1.
  Fix: slide it every second.
- **A fixed schedule gives away the fakes** ×2.
  Fix: random timing; tie tricks to real cases.

## Crew and coupling
- **One seat holds the cue or the decision (a quarterback)** ×7 (the head of a shared costume saw every stall first; a single wearer of ghost-seeing glasses called every move).
  Fix: everyone decides at once (co-op check point 7); split by position.
- **A partner who only stands in place** ×6 (a sailor whose only answer to a boom is to duck; a friend who only freezes when called, a companion whose help is standing near, neighbours who only hold poles).
  Fix: the receiver commits too, or holds half the information.
- **Equal speeds let one player do it all** ×1.
  Fix: compare solo and team speed.
- **Fixed endpoints make one best setup** ×1.
  Fix: move an endpoint each round.
- **Grouping that doesn't divide the crew** ×1.
  Fix: one coupling through everyone; check odd sizes.
- **A timed joint press counted as coupling** ×2.
  Fix: it needs a decision, not a rhythm; check lag (~0.2 s).
- **A pooled sum counted as coupling** ×4 (one wakefulness meter everyone's noise adds to).
  Fix: different actions that fail without each other.
- **Hidden info nobody gains from hiding** ×2.
  Fix: a counter verb and a reason to lie.
- **Blame moved to a replay** ×1.
  Fix: one body failing, visible as it happens (co-op check point 4).
- **Content that needs more than the fewest players** ×1.
  Fix: scale the needs with crew size.
- **A search budget not scaled to the fewest players** ×1.
  Fix: fewer searches than suspects at every size.
- **Bots as the counter in a team game** ×1.
  Fix: ask who the counter is in the test crew.
- **A side with no goal stands still** ×1.
  Fix: every side gets a goal that forces risk.
- **Silence assumed online** ×5 (a warning call priced through the game's mic is free on Discord; a dragon woken by voices: the best move was to stop talking).
  Fix: never build the core on silence (players are on Discord); talking is allowed and still not enough.
- **A rescue that needs two soft-locks the end** ×2 (a charred burglar needing two carriers, at 3 players).
  Fix: check joint actions with one survivor.
- **The crew settles into a routine** ×2.
  Fix: judge the plan by round 5; something keeps the routine moving.
- **A plan breaker bolted on** ×1.
  Fix: build it with the core.
- **A simple threat rule has a one-line answer** ×5 (fire at the last loud noise: throw a goblet; an owl that dives at the last squeak: one bat under a root squeaks all night; steadily rising water: one agreed water line).
  Fix: the threat searches, or what happens in a round changes the best plan; no safe spot.

## Rules, choices and stakes
- **An undefined value lets the cheapest option win** ×1 (A11).
  Fix: define it so the coupled option pays.
- **A carry-over trigger with no count** ×1 (A11).
  Fix: count it; apply it between rounds.
- **A safe state** ×4 (a cave mouth that reset the smoke and the dragon together; two kids next to each other with nothing that threatens a pair).
  Fix: nothing stays safe forever; a ghost sees nothing hidden.
- **An outer layer on closed rounds = a board game over minigames** ×2 (B13).
  Fix: a push choice that the carry-over changes next round, not just a score.
- **A carried harm with no way back = a death spiral** ×2 (rips that stay and make a sail slip faster, with nothing that mends one).
  Fix: an undo that needs a friend.
- **One verb strictly better than its sibling** ×1.
  Fix: a different cost for each.
- **A shared good that's really private** ×1.
  Fix: call it private, or share the outcome.
- **A rule or award that pays for betrayal** ×2.
  Fix: check the end rules with 2 alive; award only what the pillars want.
- **No carry cap = a super-player** ×1.
  Fix: a hand limit.
- **A % value that points to one option** ×1.
  Fix: share each value across 2+ options; P(option | sign) 50–65%.
- **A free retry turns a guess into a test** ×2.
  Fix: a wrong try costs more than waiting somewhere; simulate it.
- **An effect on a hidden meter** ×2 (running away felt safer: a feel problem).
  Fix: show it on the body.
- **A defence with no counter** ×2.
  Fix: it works once, then waits, or gives half speed while raised.
- **A split one side can finish alone** ×1.
  Fix: each side gets a new piece every step.
- **A scene's numbers not worked out** ×9 (a storm crew: a toy script over 54 settings found 1 that played as written; when dawn comes, how fast fear fills, when the parade ends: each idea turned on one ratio nobody worked out).
  Fix: work out every number with a script before writing.
- **A fixed cost per failure makes sacrifice the cheapest** ×1.
  Fix: the cost depends on how it ends.
- **A benefit with no rule that makes it** ×1.
  Fix: name the rule.
- **A "choice" with one free option** ×1 (B15).
  Fix: price it or drop it.
- **A weakness that makes a fortress** ×2.
  Fix: few lights, creatures put them out; no slows.
- **Spectators as free scouts** ×1.
  Fix: the dead watch from a living friend's eye height.
- **A protection for one helping role** ×1.
  Fix: protect by where you stood at the moment of danger.
- **Immunity with few players** ×1.
  Fix: a head start, never immunity.
- **A power that erases its own counter** ×1.
  Fix: make the counter matter more.
- **An extra kill window that only reaches helpers** ×1.
  Fix: check who a new danger can reach.
- **A contest nobody wants to win** ×1.
  Fix: name who wants each side with today's features.
- **Merged verbs collide under pressure** ×2.
  Fix: rank them by worst failure; lock at the press; switch on a visible world state, never a distance ring.

## The user's words and past work
- **A diagnosis stated as fact** ×1.
  Fix: give the user's verdict, or tag it [opinion].
- **A fix the failed game already had** ×1.
  Fix: read its design doc and README first.
- **A fix that is really a new game** ×2.
- **"One answer" fixed by dropping the cooperation** ×2 (Moonsick's race; a hide-and-seek where humans never help each other).
  Fix: after putting a person on the other side, write the act one human does for another; if there is none, it is not the user's co-op.
  Fix: say not to fix it.
- **Redesigning what was never playtested** ×3.
  Fix: playtest it; search the user's repos for the same shape.
- **A sketch that breaks the project's pillars** ×1 (a goofy cartoon tower-defense farm).
  Fix: read the pillars; take a conflict to the user (A4).
- **Pillars dropped silently** ×5 (places as goals, how rare a double event is, a % per sign).
  Fix: list every confirmed pillar a sketch drops.
- **The same answer reused across fixes** ×1 (A1).
  Fix: a different verb per game.
- **Candidates that differ only on the surface** ×4 (A2; four of five fantasies were "a thing reacts to our noise or presence while we fetch items").
  Fix: name what each one hides; if it's the same, they're one.
- **A gap claimed without checking** ×1.
  Fix: check the source row by row.
- **A method the user already turned down** ×5 ("the turned win if nobody is human at dawn" was "the werewolf wins small if nobody is human at morning", thrown out the same day).
  Fix: reread their verdicts first.
- **Claude's call passed off as the user's** ×3 (A6).
  Fix: build what the user said and tag Claude's additions; answer the request as given; a "to the user" finding goes to the questions file.
- **Research in the folder left unused** ×1 (B26).
  Fix: read the latest research entries first.
- **A check marked "weak"** ×1 (B25).
- **A base problem parked under "unproven"** ×3 (a quarterback seat, a silent routine, two feelings with no game behind them, each listed as an open risk and sent on).
  Fix: an open risk on the base is a fail until fixed; only tuning questions go under "unproven".
  Fix: pass or fail only; weak = fail (CLAUDE.md rule 23).

## Checks, raters and method
- **Pass rates of unlike samples compared** ×1.
  Fix: compare like with like, or call no winner.
- **Raters disagree or add rules** ×3.
  Fix: write down how to read each check, mixed answers included; measure agreement after each change to a check.
- **A check that can't fail, or doesn't split the field** ×3.
  Fix: drop it, and add missing ones (who holds the call, can the dev crew test it, build cost, lag); if one blocks everything, search for that directly.
- **A method built from the raters' own praise** ×1.
  Fix: judge it on checks they didn't write.
- **A rerun of the winning method** ×1.
  Fix: carry forward what the scores showed, not the method.
- **A scorer reading outside its brief** ×1.
  Fix: name the only files it may read.
- **A research tick read as a pass for the idea** ×1 (a ✅ that some game causes the feeling stood in for checking this idea's own rule).
  Fix: the research shows a rule that works somewhere; the idea's rule still gets the plan probe and the co-op check.
- **A feeling borrowed from a game where the players are rivals** ×3 (Clank!, Deep Sea Adventure, Who's Your Daddy, each cited for a shared-pay crew).
  Fix: write the relation between the players next to each cited game, and strike the row when it differs.
- **A drop reason not run against the survivors** ×3 (the decoy plan, shared pay with open facts, a premise already shipped).
  Fix: every reason in the dropped table is a check row for every idea still standing.
- **A scene written to show the feeling, at one crew size** ×1.
  Fix: find the best move at the fewest players, the most, and with bots, before any mark goes in.
- **Near games searched after the idea was fixed, and "near" with no verdict** ×1 (two announced games with the premise were missed).
  Fix: search the premise before writing the choice; a near game gets "taken" or "different because X".
- **A player asked to want and fear the same thing** ×2 (turning into the werewolf; a drunk who wants home and wants the kebab).
  Fix: check the fantasy for it before anything else; a game where it works makes the two sides opponents.
- **An author-filled check row says "none found" while the reason sits in the same file** ×3 (a freeze rule, a hold-it-for-me rule and a shared sum, each already a drop reason two sections down).
  Fix: the author lists the drop reasons; someone else, or a second pass with the dropped table open, fills the row.
- **A rule marked passed while not written** ×4 (seven rules of a storm crew, starting with what a haul is; where the eye looks, what a dare is, how fast fear fills).
  Fix: write the rule in one sentence before any check that leans on it; an unwritten rule fails the check.
- **"Depends on the numbers" used as a pass** ×3.
  Fix: work the ratio out, or mark the check failed.
- **Nobody asked what the other end of the choice does** ×3 (one end stood still, held or followed in all three ideas).
  Fix: write what each end decides, in the same second.
- **Severe findings that come back after their fix** ×1 (four severe, a rewrite, then six).
  Fix: drop the idea; no third version while the user is away.
- **A perfect crew's round is one where the idea doesn't happen** ×1 (hitting a friend with a boom was the idea, and good play never does it).
  Fix: write the round a perfect crew plays; if the core act is a mistake they avoid, the act must be made right some of the time by something outside the crew.
- **A feeling cited from a game where an enemy or level content forces it** ×3 (friendly fire under enemy pressure, shouting kept alive by kitchens that break habits, a rescue forced by an enemy that hunts stragglers).
  Fix: next to each cited game, write what forces the moment there, and check the idea has it.
- **An idea taken as checked because an earlier list ranked it first** ×1 (the idea pool's top core failed its first isolated critic on six severe findings).
  Fix: a pass from the author's own inline checks is not a pass from a critic.
- **A toy script that doesn't test the choice it was written for** ×1 (hiders never reacted to a hunter and moving carried no risk, so "it can be tuned" covered the clock only).
  Fix: the script must contain both sides of the written choice and the price of each.
- **Web search budget not planned** ×1.
  Fix: budget searches per step (~200 per session).

## Simulation
- **"(assumed)" graded as a pass** ×1 (Moonsick bluff rounds 15–21 never ran the numbers; trips were too slow for the lie).
  Fix: a verdict on rates or timings stays open until a script checks it.
- **Rules leaning on an unbuilt, unspecified direction** ×1 ("everyone a little sick" carried every bluff rule).
  Fix: spec the direction with numbers before simulating on it.

## Bluff (Moonsick bluff-all, 2026-11-15)
- **A betrayal verb that pays more than the honest path** ×1 (turning early: a sure catch next to a lone friend vs a chancy cure).
  Fix: script the betrayal's payoff against the cure's before proposing the verb.
- **A lie that costs nothing** ×1 (stiffing a bot lost only its bubbles; it still treated you).
  Fix: the one lied to must hold back something the liar needs.
- **Pieces bolted on beside the core lie** ×1 (mirrors, asking and turning early acted on full cases; the lie lives in mild symptoms).
  Fix: check each piece touches the moment the core lie happens in.

## Layout (Moonsick layout around the potion, 2026-11-15)
- **A contest designed into the map that a built rule already removes** ×1 (ingredients stay in the cauldron for good, so the rat and wolfsbane rooms go dead by 0:15).
  Fix: before placing rooms around a resource, check how long the resource stays contested under the current rules.
- **Sabotage that fails "seen" because the target sits where nobody looks** ×1 (the moon-water bucket alone in the attic).
  Fix: put the slow, stealable resource in a sightline from the main room.
- **Judging a design with a test crew that never plays one side** ×1 (bots never sabotage, so the potion was free at 2:14).
  Fix: give the bots each side's key move before using them to judge balance.

## Added 2026-11-17, critic round on Imps (`projects/game-design-research/fantasy-coop-2026-11-17/critic-imps-r1.md`)
- A help priced as a share of a pile the helped friend can empty first: the help is free at the empty moment (×2).
- A dealt list of small rules read as "no plan card": the list is a lookup table, one row per card (×2).
- A wish that "names a friend" where the friend does nothing: it wants something from me, measured against a friend (×1).
- A pair "that can't both be met" that is met by standing side by side, and is gone after one redeal (×2).
- Author's stage 1 passed eight rows the critic failed; its kills held, its passes didn't (×1).
- Wishes written as distances or places: a crew that walks together meets them for free (×1, second round on Imps, measured against the baseline).
- A help that also deals a new card: repeated for free until a cheap card comes up (×1).
- A harm that is certain and agreed read as "sorry": in the cited games the harm is an accident under pressure (×1).

## Added 2026-11-18, the comparing critic on five friendslop sheets (three rounds)
- A danger that moves only as fast as the crew chooses: the crew counts and stops short (×4: gold loaded onto a ship, fur under a cloak, a fever on a clock, a wolf's hunger).
  Fix: something that arrives by itself (a beam, a tide), written into the fantasy.
- A failure state that is on the crew's side tames itself (×1: the wolf-friend steered into the shade and lapped safely).
  Fix: the place it can go is the place the work is.
- A rescue that leaves the rescued better off than before the failure: failing on purpose becomes the best move (×2: a caught wolf back with no fur; a bite that reset the wolf's hunger).
  Fix: the rescued friend comes back no better than just before they failed.
- A help that works against the target it is paid from (×1: a cure flask that lowered the cauldron the night is measured on).
- One friend made the sink for everyone's harm (×2: the gold dump; the doorway guide).
- A full shield that costs nothing to hold (×1: any small piece of silver stopped a bite).
- A listed choice whose two ends lead to the same place, or with nothing at risk (×2).

