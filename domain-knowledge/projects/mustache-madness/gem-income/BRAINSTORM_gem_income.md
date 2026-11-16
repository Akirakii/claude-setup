# BRAINSTORM: where the player's gems come from, and how income grows

Super design (Team mode, 2026-10-25): three blind divergers (research, player view,
subtraction), an essence auditor, a challenger. Every pick below is Claude's until the user
confirms it. Working files: session scratchpad, not kept.

## The problem (user)
- Income turns exponential and the player has to keep up spending it.
- Gems are for sacrifice and choosing one thing over another.
- The city should grow exponentially, from the player's outcome, not from killing.
- Asked: where gems come from, how income grows, what it rewards, what it punishes.

## Frame (two causes, check the second first)
1. **Size:** income grows faster than the number of real choices.
2. **Ratio:** once income reaches the cost of keeping every workplace open, no choice is left,
   only the chore of throwing gems. "A sign may be paid ahead without limit" makes the chore
   endless: a gem can always go on a sign, so an unspent gem always feels owed.
Check: per night, gems earned vs gems needed to keep every workplace open all night. If the
ratio crosses 1 near the night the pain started, cause 2 is the main fault.

## Flat vs compounding (the team split, resolved)
- Flat purse ("the city already compounds in herd, builds and pouches") is false under today's
  rules: only player gems open workplaces and build pieces, and creature gems enter only as
  wages from those signs. A flat purse makes the city plateau while waves keep growing.
- Automatic compounding (kills, shipped surplus, visitors) is a hidden rate on the city and
  outruns choices again: today's pain.
- So income must grow, but only by **a step the player builds, which occupies something another
  use wanted.** It never grows on its own.

## Recommended
- **Source: gem plots.** A farm plot can grow gems instead of food (a plot is food OR gems).
  The farmer picks the gem bush and walks the gems to the player's side. Kill drops are cut, or
  kept small and flat.
- **Growth:** step by step, as the player turns more plots and farm shifts to gems. Capped by
  plots built, held below "open everything".
- **Rewards:** investing capacity in income at the cost of food or defense; defending the
  fields; a well-raised farmer.
- **Punishes:** over-converting (hunger, theft, fewer births); undefended gem fields (wilds
  raid the glitter); neglect.
- **Partner rule:** remove the obligation. Either cap prepaid sign time, or let a full purse
  spill to creatures, so an unspent gem is a choice, not a debt.

## Runner-up
Customers' gems fund the sign they buy at (reverses "signs are funded by the player alone").
The city then funds its own throughput, and the player's purse can stay a flat choice budget.

## Cut (reason)
- Export cart: a rate on output; "always ship surplus" is the passive policy.
- Gem seed with a yield per gem sown: interest with a lag (3^n, or a dead mechanic).
- Guest beds: new noun, runs itself, same purpose as the herd's own customers.
- Floor decides who keeps a kill gem: total still on the wave clock; "fight far" dominates.
- Scale the sinks: today's pain with bigger numbers.
- Night purse sized by night number: a clock, rewards nothing the player did.

## Pre-pillar candidates (the user promotes or rejects)
1. Player income grows only through something the player built or placed, never on the night
   clock or the kill count alone.
2. Any growing income is capped by occupied shared state the player chose, never by a price.
3. The player can never afford to open every workplace at once.

## Picks (user, 2026-10-25, AskUserQuestion)
- Measure first: per night, gems earned vs gems to keep every workplace open all night.
- Source: gem plots (a farm plot grows gems OR food).
- Kill gems: small and flat (a fixed bounty, not per kill on the wave clock).
- Obligation: cap prepaid sign time (reverses "a sign may be paid ahead without limit").

## Measured (care bot, 2 seeds, 1800 s to night 20, this session's tuning; n=2, a direction)
- The bot keeps only 3 paid workplaces all run, so "open all" stays 2-7 gems a night.
- Kill income is a switch, not a curve: a wild drops a gem only while food is plentiful, else a
  crop. Seed 2 earned ~0 gems on all 20 nights; seed 1 earned 0-4 until night 14, then 15-39 a
  night (2.8-6.9x the cost of opening all 3 workplaces). Seed 1's purse reached 144 unspent.
- Not yet measured: the ratio with a player's real number of workplaces (the next playtest
  captures `paid_posts`, `sign_gems`, `purse_gems` in BALANCE_TICK).

## Closed-system frame (user, 2026-10-25)
No outside world. Givens: incoming enemies and taming; creatures work to survive; cities grow
exponentially. Value enters only from the wave (outside), the land, and new creatures (labor).
- First source: the wave. A downed wild is "gems now (kill) or a worker later (tame)".
- Growth: labor turns land into gems at a piece the player builds, reinvested; capped by land,
  workers and defense; the next ceiling is a new city.
- The user said yes and asked to build it AFK, one PR.

## SPECIFY (AFK, every pick Claude's)
- **Gem bush (new crop):** built from the build menu (Work tab, 💎 3), on soil like any crop. It
  grows on the crop clock (`growth_duration` 120 s, half speed at night). Ripe, it posts a FARM
  job; a farmer (or the player's sweep) shakes it and `HARVEST_YIELD` 2 gems pop onto the ground;
  the bush regrows from its first stage instead of leaving. Only the player picks gems up.
  Not food: no crop meal, not counted as food for the wild drop.
- **Night bounty:** a wild that dies for good drops a gem only for the first `NIGHT_GEM_BOUNTY` (3)
  such deaths each night; later ones drop nothing (the food-low crop drop is unchanged).
- **Sign cap:** a workplace sign stacks at most `Wage.MAX_GEMS` (4) unworked gems; a thrown gem
  past that stays on the ground. The bank's vault is not a sign and takes any number.
- **Loop:** gems -> bushes (3 each) -> 2 gems per ripe bush per ~120 s of day -> more bushes.
  Payback about 1.5 harvests. Compounds only by the player's builds; capped by soil in reach of
  farmers, farm shifts (1 gem / 60 s), and wilds that break bushes (crops are targetable).
- **Probe:** `bush_gems` (cumulative gems shaken from bushes), `bushes` (gauge).
- Out of this slice (TODO): gem-crop poop as the payout look, a new city as the next ceiling.

## Measured after the build (care bot, SIM_BUSHES=1, 2 seeds, 1800 s; n=2, a direction)
- Kill gems now stop at the bounty: 3 a night at most (seed 1, nights 15-20: 3 each).
- The unspent purse stays at 6 or less (before the build: 144 by night 20 in seed 1).
- The bot affords its first gem bush only on night 17 (seed 1) and 20 (seed 2): kill gems are
  mostly crops while food runs low, so early income is near 0. Bushes paid 4 gems by night 19.
- Tuning risk for the playtest: the ramp may be too slow (bush cost 3, yield 2 per ~3 days).
  Knobs: `NIGHT_GEM_BOUNTY`, the bush's `gem` cost, `HARVEST_YIELD["Gem Bush"]`,
  `growth_duration` in `gem_bush_crop.tres`.
