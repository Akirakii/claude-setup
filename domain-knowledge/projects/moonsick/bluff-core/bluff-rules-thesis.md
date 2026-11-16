# Bluff rules review (2026-11-15)

User: "what the rules look now and could you reveiw with a subagent?"
Earlier: "keep iterating simulations until no holes or gaps. keep adding the rules", then "iterating simulations should go in backtracking way... it can go back and remove added rules".

## The problem underneath
The user wants bluffing as the core: "knowing when to bluff and how to keep cooperation".
Simulation rounds 15–21 (in `bluff-research.md`) added 10 rules on top of the design to make one lie work: lying about what you'll do ("I'll get the coffee", then not coming back late in a case).
Every round added rules and none removed one, so the list may be bigger than the game needs.

## The rules under review
In `design.md`, section "Trust and bluff", the list "Bluff rules from simulation rounds 15–21". Also leaned on, OK'd but not built (in `bluff-research.md`): everyone a little sick all night, nobody treats themselves; promises can be broken, friends remember; items in hands show, hoarding allowed; bot speech bubbles; the dead watch.

## Three answers
1. **Keep all 10 rules** (what the rounds produced).
2. **Cut to the rules the core lie needs (recommended, Claude):** keep the job lie, items in hands show, the refilling spot, the swap, the chain snap and "thrown-off friend runs"; cut bot rules to one ("bots lie late, trust what they saw") and drop "hold back a cure as a trade" if it bends "lies never from a reward".
3. **Strip to the user's pillars and the built game, plus only "everyone a little sick"**, and see whether the job lie appears with no added rule at all.

## Scenes
- Fewest (user's test): 1 human + 3 bots, 4 friends, mid-night. Dee needs coffee; bot Bo bubbles "getting coffee" and doesn't return.
- Most: 8 friends, mid-night, two trades going at once, the werewolf out.

## Pillars
Keeps: hunter picks freely; never exposes liars (bots never tell); betraying never pays more than curing (assumed).
May bend: "lies come from fear and the turn moment, never from a reward" (holding back a cure for a trade).

## Critic round 1 merge (2026-11-15; critic: `critic-bluff-rules-r1.md`)
Checked by Claude [read]: steal and tug are in design.md (user, built; bots never steal or hold on); `near_head_start` / `far_shown` exist in `night_sim.gd`; "helping beats fleeing" is in design.md.

| Finding | Decision |
|---|---|
| Verdict: wrong shape, the list is padding and the weight sits on unbuilt "everyone a little sick" | To the user. Claude's pick: answer 3, strip to pillars + built game, and spec "everyone a little sick" with numbers first |
| S1 "everyone a little sick" has no numbers | Spec it (rate, how it fits the case system) before any rule leans on it (Claude) |
| S2 steal and tug break the swap and the hostage; the fake swap then snatch is a built bluff | Cut rules 5 and 10; play the built steal/tug bluff in the next simulation (Claude) |
| S3 a far liar can't be caught; lines 3 and 4 fail | Turn the head start back on (`near_head_start`, `far_shown`), no new rule (Claude); needs the user's OK, it was cut in step 1 |
| S4 the test crew can't make the lie: the human can't promise to bots | Needs a physical offer verb bots can read (Claude); to the user |
| S5 the lie needs fleeing to beat helping, which bends "helping beats fleeing" | To the user: a pillar |
| S6 trips are too slow mid-night, so everyone carries items ahead and the trip lie vanishes | Run the numbers with a script in the next round (Claude) |
| M1 the 8-friend scene can't happen (no doubles, no case while the werewolf is out) | Next rounds read the built case rules first |
| M2 bot rules contradict | Merge rules 2 and 8: fear makes a bot bail late; trust comes from gives it saw |
| M3 rules to know: 8 before, 10 after, 16 for the test crew | Cut 4, 5, 6, 9, 10; rule 1 becomes a goal |
| M4 "never from a reward" and "never pays more" bend | Goes with S3 and S5 |
| M5 the last minute still fails | Already the user's call |

Not applied to design.md yet: waiting for the user's answer.
