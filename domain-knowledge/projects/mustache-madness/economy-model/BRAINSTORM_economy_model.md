# BRAINSTORM: the economy model (state on 2026-10-22, before the super design)

One place for every decision, rule and open problem of the gem economy, in game words. Older
working notes: `docs/BRAINSTORM_design_payment_model.md`, `docs/BRAINSTORM_design_economy_frame.md`,
the round docs `docs/BRAINSTORM_design_r*.md`, and the handoff's decision log.

## Why the economy exists (user)
- "Productivity is the number one priority to survive each wave." The economy serves the
  herd's productivity; a wave tests it.
- "Creatures should be consumerist and willing to work more if the economy is well."
- Creatures pay other creatures instead of the player paying for everything.

## The places a gem sits (defined by what each takes in and gives out)
- **Sign:** the gem counter on a workplace. Takes in gems (today only the player throws them).
  Gives out open time: each gem keeps the workplace open 60 s, and the worker on shift takes 1
  gem per shift as its salary.
- **Pouch:** a creature's own gems. Takes in salary and sales. Gives out payments for what the
  creature takes (a drink, a meal, a lesson, a lamp), hand to hand.
- **Vault:** the bank's gem store. Takes in deposits (and today it grows by itself and receives
  stolen gems the police recover). Gives out gems that the bank's worker, the payer, walks to
  workplace signs that are about to run out.
- **Savings:** the part of a pouch a creature keeps toward its next home good. Never spent on
  drinks or meals, never deposited.

## Where gems come from and go
- In: a wild's death drops a gem; the bank grows its vault.
- Out: only the player's building cost. Knocked-down creatures spill gems the player scoops up.

## Decided (user)
- Two contracts, each in its fixed place: a **funder** pays a sign for **time** (the player
  now; a creature that owns a business in stage 2); a **customer** pays **per unit** for what
  it takes. One creature can be both.
- **One unit per pile:** a sign holds time only; a pouch pays per unit, creature to creature;
  the vault is the one place per-unit gems turn back into time.
- **A maker is paid when its stock is taken or delivered,** 1 gem per unit; a workplace takes
  only the stock it can pay for ("pay or wait").
- **Broke creatures still drink and eat free.** Savings are protected.
- **"Pay wave jobs more" means paying more hours ahead.**
- **Spare creature gems keep jobs open** (through the vault), as the only tie between creature
  gems and productivity.
- **Bought goods go home:** carried over the head, set by the creature's own bed, used there.
- Creature businesses (owner funds its sign, hires staff, can go bankrupt): stage 2.

## The flow as it stands (one gem's trip)
1. The player throws a gem on the farm's sign: the farm is open 60 s.
2. A farmer starts its shift and takes that gem: salary (time).
3. The farmer buys a drink: 1 gem to the bartender, hand to hand (per unit).
4. The bartender buys a crop: 1 gem to the farmer (per unit); no gems, it waits.
5. The bartender walks spare gems to the vault.
6. The payer carries a vault gem to a sign about to run out (time again).

## Measured (one care run, 900 s, so a direction, not a size)
Wild drops 80 gems; the player bot paid 8 onto signs; wages 20; creature spending 18; 40 drinks,
about 22 of them free to broke creatures. The economy is starved, not flooded; today nearly every
wage ends in the bartender's pouch. A creature's work pace does not read its pouch.

## Problems found (two independent evaluations agree)
- Steps 1-4 are sound; steps 5-6 (vault and payer) are not.
- **The payer decides instead of the player:** nearest sign first; any open sign renews forever,
  so the player loses the "which workplaces stay open" decision. Savings spent on workplaces the
  saver never chose read as the bank taking its money.
- **The bar runs dry:** free drinks still use crops the bartender paid for.
- **The farmer is paid twice** (salary and crop sales); its gems pile up with no use.
- **A far workplace that runs out stays closed for good,** with no warning.
- **The bank grows gems** no one decided on.
- **The lamp has no seller** to pay.
- **Hand to hand at the basket** needs the farmer standing there.

## Ideas on the table for the vault step
- **The player's coffer:** creatures deposit; the player grabs and throws at signs (Majesty's
  tax collector shape). Risk: a chore late in the game.
- **Bank ring:** the payer refills only workplaces inside a coin ring around the bank; the
  player steers by placement.
- **Savings bank:** each creature withdraws only its own deposits; owners fund their own signs.
- **Workplace keeps its takings:** sales go to a jar on the sign; the place renews itself.

## Open questions
- Who spends the herd's savings? Who pays for a free drink's crop? Keep, cap or cut bank growth?
- Should the farmer be paid both salary and per crop? Who sells the lamp?
- Parked by the user: a unit's price relative to time; supply and demand prices; wages by
  seniority; "what they buy depends on their status".

## Super design result (AFK, 2026-10-22; every pick below is Claude's, not the user's)
Team: three blind divergers (research, player view, subtraction), a fresh essence auditor and a
fresh challenger. Working files in the session scratchpad (`sd/`), not kept.

### Checked in code (pillars for this design)
- A sign gem is never destroyed: each shift moves one sign gem into the worker's pouch (1 gem =
  1 shift = 60 s). So "keep a place open" and "pay its worker" are one act; the sign is a wage
  paid ahead.
- Gems leave the game only through the player's building cost (plus a rare loss of a gem in
  flight to a freed target, uncounted).
- The vault grows 1 gem per 20 labor ticks of the banker while it holds at least 1 gem, with no
  cap. The payer is the bank's own worker.
- The measured "player paid 8 of 80" comes from the sim's player bot, so it says how the bot
  throws, not how a person plays.

### Frame
Who decides which workplaces stay open, now that creatures hold most gems. Gems coming back to
signs is a hard constraint, not the goal.

### Recommended: the bank matches the player's throw (all three divergers proposed it independently)
- **Rule:** the payer carries vault gems only to a sign the player has just thrown on, 1 vault
  gem per player gem, oldest throw first, until the vault is empty. It never chooses a sign by
  itself.
- **Why:** it keeps every user decision (the sign holds time only, its funder is the player,
  spare creature gems keep jobs open) and gives the "which workplaces" call back to the player.
  A rich herd doubles the player's call; it never makes it.
- **Scene:** the player throws 4 gems on the guard post before a wave. The banker trots out
  with 4 gems held over its head and slaps them on the same sign. Empty vault: the banker stays
  in, and the sign shows only the player's 4.
- **Decision beats doing nothing:** a player who throws nothing gets no match, and the vault
  fills.
- **A full vault has a cost already in the game:** thieves rob the bank. A herd that saves
  much and a player who throws little make a fat target, so a pile pulls in the police loop.
- **Risks:** (1) one payer and many throws before a wave means late matches (the payer's laps);
  (2) the challenger reads a 1:1 match as close to a flat bonus; (3) the match must show on the
  sign, or the payer looks like it ignores a blinking sign.

### Runner-up (needs the user, changes the decision "a sign's funder is the player")
**A creature reopens a dark sign it wants:** a creature standing at a closed place it wanted
pays one spare gem onto that sign; the player alone pays ahead for production (farms, guard
posts). It got the challenger's top rank: lowest chore at 40 creatures, a far closed place
shows itself on sight (a crowd at a dark door), no new noun. Against it: creatures become sign
funders; when the herd is broke the consumer side goes dark at once; and 60 s openings flicker
at the bar.

### Cut (reason)
- Tax heap (creature gems pile at the bank for the player to scoop): same job as a wild drop,
  plus a throwing chore.
- Patron pays the sign, worker pays its own sign: the bar funds itself forever, and the player
  loses the bar decision (the Dwarf Fortress warning). Parked as the seed of creature-owned
  businesses, stage 2.
- Bank reach ring: a one-time choice; inside the ring every sign renews forever.
- Salary only (all serving free): kills "consumerist"; kept as the floor to beat.

### The other open questions (Claude's picks)
- **Vault growth:** cut. A pile from nothing that no one decides. Watch: today it pays most
  wages (wages 20 vs bot throws 8), so check that wages don't run dry with a bot that throws.
- **Who pays a free drink's crop:** the bartender, as today. "The bar runs dry" was never
  measured; the measured fact is the opposite (the bartender's pouch collects nearly every
  wage). Measure first; if it does run dry, the bank refunds a free drink's crop.
- **Farmer paid twice:** keep both. Salary and crop sales come from different payers for
  different things (the player pays its open time; the bartender pays per crop), so they are
  not duplicates. Its pile is not dead: spare gems reach the vault and so the player's
  matched signs.
- **Who sells the lamp:** the shop clerk, already decided (18f: the clerk makes the lamp from
  3 logs and serves it). Closed by an existing decision.
- **A far place closes for good unseen:** under the match rule only the player keeps a place
  open, so it closing is the player's call; it still needs a warning. Pick: its worker waits
  idle at its dark sign. Invented detail, needs the user (LAW: verbs and visuals the game has).
- **Hand to hand at the crop basket:** an honesty box: the buyer drops its gem in the basket,
  the farmer pockets basket gems at its next unload. Needs the user: they asked that the payer
  and payee meet on screen for a tip.

### Backtrack candidates the challenger raised (the user's calls; kept, not acted on)
- "Customer pays the serving worker per unit" makes the bartender's pile.
- "Worker pays the maker per unit" causes the free-drink crop, double pay and basket problems.
- "1 gem = 60 s" may be too small at 40 creatures and 10 signs (many throws, many payer laps).

### Questions for the user (recommendation first)
1. Vault step: the bank matches your throw 1:1 (rec), or a creature reopens a dark sign it
   wants (creatures become sign funders)?
2. Is a 1:1 match a new rule you want, or a flat bonus you banned?
3. Cut vault growth (rec)?
4. Keep the farmer's salary plus crop sales (rec), or one of them?
5. Crop basket: honesty box (rec), or must the farmer and the buyer meet?
6. A closing far place: its worker waits at the dark sign (rec), or the sign blinks in its
   last 60 s?
7. Any of the challenger's backtrack candidates worth reopening?

### SPECIFY (for the recommended rule)
- **Data:** `vault` (gems, 0..unbounded, bank; no growth; drained only by matches, theft and a
  knocked-down bank's spill). `owed_match` per sign (gems, 0..unbounded; += n on a player throw
  of n, -1 per delivered vault gem; cleared when the sign is knocked down). Savings and spare: as
  decided (spare = pouch minus savings; only spare is deposited).
- **Pipeline:** player throws n on sign S, S.owed_match += n -> payer takes the oldest sign with
  owed_match > 0, carries min(owed_match, vault) gems, lays them on S as time -> each shift, a
  sign gem goes to the worker's pouch -> per-unit buys pouch to pouch -> spare to the vault.
- **Loop (closed):** every gem a creature deposits returns to a sign only through a player
  throw. Pile check: vault rises when deposits exceed throws; brake = thieves. Drought check:
  creature income = player throws + matches, at most 2x the player's own throws, so it can
  never run without the player. Contradiction check: no rule above breaks R1-R17 in the layers
  model (sign holds time only, funder is the player, unit to time happens only in the vault).
- **Constants:** match ratio 1:1 (a weight, the user's call in question 2).

## User decisions (2026-10-24, AskUserQuestion)
- **No deposits (user):** creature gems stay in pouches; they move only by buying, theft, or a
  spill. Signs are funded by the player alone; the bank is the player's tool (throw there, the
  payer feeds due signs). Supersedes "spare pouch gems go to the vault" (2026-10-22). So the vault
  step (questions 1-2: match vs creature reopens) is moot.
- **Vault growth: cut (user).**
- **Drink costs 2 (user):** 1 to the farmer for the crop, 1 margin to the bartender. Checked: 1 crop
  = 1 drink, so at price 1 maker pay left the bartender at 0 per paid drink, -1 per free one.
- **Farmer keeps wage plus crop pay** (follows from the drink price; the user asked if it is
  unbalanced: the loser was the bartender, now fixed).
- **Crop basket: honesty box (user).**
- Still open: question 6 (a closing far place's warning), question 7 (backtrack candidates), and
  whether savings still mean anything with no deposit.
- **Bank route (user):** gems thrown on the bank go to any due sign (today's rule), the player's
  chosen hand-off. **No closing warning (user):** question 6 closed. **Savings cut (user).**
- Open (user, "maybe not drinks free"): does a broke creature still drink free? Open (user): how to
  balance costs when gems are whole numbers.
- **Whole gems: ratios in goods (user):** prices stay 1-2 gems; recipes carry the fractions (1 crop
  makes 2 drinks, drink back to 1 gem, same bartender margin). Supersedes "drink costs 2".
- **Player income: kills, measure first (user):** wild kills only (1 gem each, checked
  `WildDropService`); measure whether that keeps workplaces open between waves before adding any.
  The user then raised **tax** (creature gems back to the player) as the other option: open.
- **Broke drink (user):** no drink; a mate with gems may treat it (18b). Supersedes "broke drink free".

## Tax super design (2026-10-24, Team mode; working files in the session scratchpad, not kept)
Question (user): whether a return of creature gems to the player should exist, given the one-way
flow; not how. Three blind divergers (research, player view, subtraction), then an essence auditor
and a challenger, all said no tax.
- **No tax (user).** Every shape tried was a rate (a share of what creatures earn or spend): it
  breaks "never one piece reading or scaling another" and loses to the passive policy (always
  collect, always rethrow). Note: "passive income is banned" is not written law; it came from
  the brief.
- **Sink: measure first (user).** Probe gems per pouch by job over session age, and kill income
  against the gems the chosen signs need (early, mid, late). The tax question reopens if kill
  income runs short. With the work-drive lever cut (PR 18), a full pouch costs no productivity.
- **Pre-pillar "player gems come from the board, never a rate": no (user).**
- **A pouch drops only when its creature dies (user):** not on a knockdown. A creature familiar
  with it collects the gems; with none, they lie on the floor (the player can pick them up).
  Checked: today the pouch already drops only on death (DOWN timer out), old-age farewell, or a
  combiner; never on knockdown. Earlier session claims of a "knockdown spill" were wrong.
  Checked: familiarity is a per-pair value; only players pick up dropped gems; police carry
  seized gems to the nearest due sign, else a bank vault.
- Challenger's open idea (not picked): creatures toss spare gems onto a building the player
  placed; needs a reason for creatures to want it.
- **Heir (user):** the most familiar creature at friend level or closer walks over and collects
  a dead creature's gems; with none, they stay on the floor. Assumption: "friend level" has no
  threshold in the code yet (familiarity and friendliness are plain values); a tuning value to set.
- **Banker cut (user):** its labor only grew the vault (checked `Bank.labor`), and growth is cut.
  The bank keeps one job, the payer.
- **Payer paid like any job (user):** the bank gets a pay sign; the payer takes 1 gem per shift.
  Checked: today `Bank.on_shift()` is always true, so bank workers never take a wage. Assumption:
  the bank's own sign counts as a due sign, so the payer may top it up from the vault (the
  player's own bank throws pay the payer).
- **Services with a price (user, 2026-10-24):** a meal is 1 gem to the cook (1 crop makes 2 dishes;
  checked: today 1 crop makes 1 dish, meals free). A broke creature pays for a raw crop instead
  (user). Class: 1 gem per class to the teacher (user). Medic: 1 gem per treatment (user); a broke
  patient still gets treated (the option's text, assumption until confirmed). Library stays free
  (no server).
- **New mechanic (user, to design):** a broke creature that is very hungry steals food; the one it
  stole from gets angry and fights it or calls the police. Checked: hunger and a starving timer
  exist (`needs_component.gd`); theft today comes only from a mood snap robbing a bank vault.
- **Wage + tip (user, 2026-10-24):** every job earns its wage for open time; a job that serves a
  customer also gets 1 gem per unit served (bartender, cook, teacher, medic, shop clerk, farmer
  by crop). Jobs with no customer (guard, chopper, builder, researcher, payer, hauler) earn the
  wage only. Settled by the pillar "a creature earns by working and serving ... a gem keeps
  passing creature to creature"; "buying drains the gem" was the rejected option.
- Open: broke meal reading (a: dish 2, raw crop 1; or b: both 1, raw only when no cook); then
  design food theft (hungry broke steals, victim fights or calls police).
- **Broke meal, reading (a) (user):** a dish costs 2, a raw crop costs 1 (bought from the farmer's
  basket); a creature with 0 gems eats only if a friend treats it, or steals. Supersedes "meal 1 gem".
- **Dish ratio (user):** 1 crop makes 1 dish (today's code); dish 2 gems, cook keeps 1, same as the bartender.
- **A customer never opens a workplace (user):** a customer gem never lands on a sign; a creature
  buys only from an open workplace with its worker on shift. No open job, no sale: the customer
  waits (stalls). Open: the honesty-box basket sells raw crops only while the farm is open?
