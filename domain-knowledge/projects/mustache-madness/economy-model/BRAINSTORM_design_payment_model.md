# BRAINSTORM: payment model (team-mode design, 2026-10-22)

User's problem: player-to-creature pays a wage for TIME; creature-to-creature pays for what is
PRODUCED; the two must share one system (or both contracts must exist for both payers).

## Synthesis (main session)
- **Survivors (auditor):** Firm (one sign per workplace; player buys hours, customer buys a
  serving, worker paid 1 gem per shift) and Coin-op (1 gem = 60 s open for everyone present).
  Piece rate cut: on-call jobs have no unit; breaks the sign's paid-time pre-pillar.
- **Only B's Firm rule keeps "pay ahead without limit":** a customer gem goes on the sign only
  while the sign is due, else to the worker.
- **Frame hit (challenger + auditor, code-checked):** creature gems move no productivity today.
  drive() ignores the pouch (creature.gd:1085), JobBoard ranks by discipline then distance
  (job_board.gd:289-291), labor pace is fixed per job and only tipsy slows it
  (job_component.gd:150). So "pay wave jobs more" can only mean more hours ahead.
- **Productivity option (challenger M2):** spare herd gems go to the vault, the existing payer
  tops up due signs; herd wealth then keeps open jobs open (the binding constraint). The
  player still picks which signs open.
- **Measure first:** R = bought / wages (balance_probe.gd:751) and the herd pouch total in one
  sim before pegging a price. The "20x" gap was capacity, not measured (sustained ~10x).
- **Keep:** broke creatures drink free (blocks the bad-wave mood spiral).
- **Parked answers:** supply/demand price: no (show demand as a queue); seniority wage: no (a
  wage cannot raise output here); unit vs time ratio: after the measurement.


## Raw: pay_a

## Payment model, diverger A (economics + other games lens)

**Frame:** time pay and unit pay don't clash. They are two different contracts held by
two different pairs. A *sale* (anyone -> workplace) is priced per unit. A *wage*
(workplace -> its worker) is priced per time. The player's thrown gem was never a wage. It
is a sale of open hours to the workplace. Real firms work the same way (Coase): customers
pay per unit, the firm pays staff per hour, and the till sits between them. The actual bug
is the exchange rate. Today 1 gem buys 60 s of a worker from the player but 3 s of a
bartender from a customer (1 gem per drink, about 20 drinks a minute, bar.gd:196). So
c2c pay runs about 20 times higher than p2c pay, and the player's pay stops mattering
wherever customers exist.

### 1. The abstract problem (no game nouns)
- Currency M is created only at faucets (enemy deaths, a fixed interest source). It is
  destroyed only at one sink, the outside funder F's construction spending.
- Producers P run sites. A site turns a worker's time into output. Some output is a
  public good: no single consumer uses it up (defense). Some is a private good: one
  consumer uses it up (a service).
- Two payers fund sites: F (outside, steers) and consumers C (inside, also producers).
- Two contract kinds exist: TIME (pay per duration of availability) and UNIT (pay per
  delivered item). Each kind sets its own exchange rate between M and labor.
- Needed: one rate between M and labor, so that a unit of M means the same labor whoever
  spends it; F still has a lever; M neither piles up nor runs dry.

### 2. Abstract solution, with sources
- **Contract by relationship, not by payer.** Wage contracts are time contracts. Sale
  contracts are unit contracts. A site's buffer (the till) turns unit revenue into time
  wages. That buffer is the theory of the firm in one object.
- **Peg the unit to time.** Price a sold unit by the worker-seconds it uses: price =
  wage rate x seconds per sale x (1 + markup). Then both contracts quote one rate.
- **Hybrid pay = time floor + piece top-up.** At Safelite (Lazear 2000), moving to piece
  rates *with an hourly guarantee* raised output per worker by 44%. About half came from
  incentive and half from sorting by ability. Here the floor is the shift gem and the top-up
  is the overflow. Pure piece rates push input risk onto the worker: no glass, no pay
  (Holmstrom risk-sharing). They also starve unmeasured tasks (Holmstrom-Milgrom
  multitask), and standing guard has no unit at all.
- **Prices: fixed and posted.** Real retail prices are sticky (menu costs, customer
  markets). Demand moves quantity first: the queue, the till, the overflow. In this game a
  floating price would be a hidden effect the player cannot steer. Supply and demand
  already reach the worker through overflow, with no price change.
- **Velocity and sinks (MV = PQ).** If the unit price is far below the time price, M turns
  over many times a minute inside C, and F's injections look tiny. Pegging bounds every
  site's turnover to about (1 + markup) gems a minute. A faucet with no sink inside C
  inflates savings until spending stops being a choice. This is the Ultima Online lesson
  that made MMOs design faucets and sinks together.
- **Games:** Tropico / Anno: the state pays public works, citizens pay for private goods
  (the F/C split). Two Point Hospital / Theme Park: unit fees in, time salaries out of one
  balance (the firm buffer). Dungeon Keeper: time payday scaled by level, gold recycled
  through the casino. Majesty: bounty flags, pure unit pay. Dwarf Fortress 0.31: wages,
  rent and shops turned off as broken and too complex, dwarves hauled coins all day (a
  closed loop with no player decision). RimWorld / Banished / Settlers: no wages; the fun
  sits in goods, not money.

### 3. Three whole-model shapes
Terms (each defined by what it takes in, gives out, and connects to):
- **Stack:** the gems on a workplace's sign. It takes thrown and carried gems, gives one gem
  to the worker per shift and its surplus to the worker's pouch, and connects the payers to
  the worker.
- **Shift:** 60 s of work, bought by one gem.
- **Sale:** a customer's one gem, put on the stack in person, for one serving.
- **Serving:** what a sale buys. It is a fixed slice of the worker's time, `SERVE_SEC`,
  shaped as a whole thing on screen (a stay at the bar, a meal, a haircut).
- **Reserve:** the stack size the workplace keeps for its next shifts.
- **Overflow:** a stack gem above the reserve. It goes to the worker's pouch.

#### Shape A: the workplace is a firm (sales in, shifts out) [rank 1]
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| open hours | player -> stack (thrown gem) | 60 s of open hours each | TIME | p2c | gem lands on sign, count +1 |
| sale | customer -> stack (walks up, sets gem down) | one serving (`SERVE_SEC` of the worker) | UNIT | c2c | customer flicks gem on sign, 💎 count +1 |
| delivery | payer creature -> stack (bank vault gem) | open hours, for the player | TIME | p2c by proxy | payer walks a gem over |
| shift wage | stack -> its worker (takes it in person) | the next 60 s of work | TIME | both (either payer funded it) | worker grabs gem, clock refills to 1:00 |
| overflow | stack -> worker's pouch, stack > reserve | being busy beyond needs | UNIT-driven | both | gem hops sign -> pouch, worker emotes 💎 |
| spill / police | knocked-down pouch or stack -> ground; stolen -> police | (not a trade) | none | both | gems pop out; marked gems glow |
- Scene: a goat pays 1 gem at the bar sign and sits for a stay of about 10 drinks. The
  bartender takes a sign gem each minute. A busy night stacks the sign to 2, and the third
  gem hops into the bartender's pouch. The player throws 3 gems on the cannon tower before
  the wave. Its sign reads 💎3 1:00.
- Price rule: always 1 gem a sale. The serving's size is set by `SERVE_SEC` =
  `GEM_SEC / (1 + MARKUP)` = 30 s of worker time. Fixed, not supply and demand.
- Wage rule: a flat 1 gem a shift plus overflow. Overflow rises with demand (a piece
  top-up). No seniority rule: a more skilled worker serves faster and sells more, so
  seniority pays through output.
- Money: player and bank feed the stacks of public jobs. Customers feed the stacks of
  private jobs. Everything ends in pouches. It leaves pouches only by sales, spills, police,
  or nothing. The only true sink is still the player's builds.
- Failures: piling (pouches grow with no sink inside the herd; measure first; a knockdown
  spill drains them); drought (an empty customer-funded stack opens only if a customer walks
  to a closed sign, G1); hoarding (a rich pouch shows 💰 and draws thieves); death spiral
  (a bad wave spills pouches, sales fall, private jobs close, but public jobs still run on
  the player's gems); lever loss: none on public jobs, private jobs leave the player's
  hands on purpose (the Tropico split).

#### Shape B: everything is time (coin-op meter) [rank 2]
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| open hours | player -> stack | 60 s per gem | TIME | p2c | sign count +1 |
| seat time | customer -> stack | 60 s of service at one seat | TIME | c2c | seat meter m:ss over the customer |
| shift wage | stack -> worker | 60 s of work | TIME | both | clock refills |
| overflow | stack -> pouch above reserve | parallel seats paying | TIME-driven | both | gem hops to pouch |
- Scene: a cow drops a gem in a bathhouse slot, and a 1:00 meter ticks over its tub. The
  same scene at a bar reads as a cover charge by the minute, which is odd on sight.
- Price rule: 1 gem = 60 s on every side. The simplest possible peg.
- Wage rule: flat. A workplace with N seats earns up to N gems a minute, and N - 1 of it
  overflows.
- Failures: unnatural for goods (a meal or haircut is a unit, so it fails the Natural on
  sight pillar for most shops); income scales with seat count, not with serving; nothing
  pays for productivity, which the user ranks first. It is fine for leisure that lasts
  (baths, naps).

#### Shape C: everything is units (piece rate, bounty) [rank 3]
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| bounty | player -> stack | N units of output (crops, blocks, kills) | UNIT | p2c | sign shows units left |
| sale | customer -> worker or stack | one serving | UNIT | c2c | gem on counter |
| piece wage | stack -> worker per finished unit | the unit | UNIT | both | gem pops per unit |
- Scene: the player throws 2 gems on the farm sign, which reads "🥕 x10". Each harvest
  pops a gem fragment to the farmer. This is Majesty's flag.
- Price rule: per-job units per gem, pegged to about one minute of typical output.
- Wage rule: pure piece rate, so seniority and skill pay automatically.
- Failures: standby jobs (guard, medic on call) have no unit, so it falls back to time and
  is no longer one system; input stalls push risk onto the worker (no crops, no pay); kill
  bounties cause kill-stealing; indivisible gems need fragments; it breaks the PRE-PILLAR
  "paid time sits on the station and burns down".

Ranking reason: A gives one rate (the peg), keeps both contracts where economics puts
them, matches every user decision, and keeps the player's lever on public jobs. B is
cleaner but looks wrong for goods. C fails on standby jobs and on the burn-down pillar.

### 4. SPECIFY for Shape A
#### Data dictionary
| name | type, range | owner | definition | lifecycle |
|---|---|---|---|---|
| `GEM_SEC` | float, 60 | constant (wage.gd) | seconds of work one shift gem buys | fixed |
| `MARKUP` | float, 0..2, prop. 1 | constant | extra a customer pays over the time rate | fixed |
| `SERVE_SEC` | float = GEM_SEC/(1+MARKUP) | derived constant | worker-seconds one sale buys | fixed |
| `serving` | authored per workplace | static metadata | what SERVE_SEC looks like (drinks per stay, etc.) | fixed |
| `RESERVE` | int, prop. 2 | constant | stack gems kept before overflow | fixed |
| `stack` | int 0..inf | per workplace | gems on the sign, not yet worked | +sale/throw, -shift/overflow, spill on knockdown |
| `shift_left` | s, 0..60 | per workplace | time left on the running shift | burns on dilated clock |
| `pouch` | int 0..inf | per creature | a creature's own gems | +shift wage, +overflow; -sale, spill, police |
| `g` | gems/min | measure | player plus delivery inflow to a stack | probe |
| `d` | sales/min, 0..1+MARKUP | measure | customer inflow to a stack | probe |
| `open` | 0..1 | derived | share of time the workplace runs = min(1, g + d) in steady state | none |

#### I/O pipeline (per workplace, per tick)
1. Pay in: a throw, delivery, or sale reads the gem carrier and writes `stack` +n.
2. Shift start: if `shift_left`=0 and `stack`>0, the worker on site does `stack`-1,
   `pouch`+1, `shift_left`=60. Otherwise the workplace is closed.
3. Serve: the worker works and each sale is served for `SERVE_SEC`. Reads `serving`,
   writes nothing monetary.
4. Overflow: while `stack` > `RESERVE`, `stack`-1 and the worker's `pouch`+1 (the gem
   hops on screen). Reads `stack` and `RESERVE`.
5. Spend: a creature with `pouch`>=1 that wants a serving walks to that sign, the sale
   goes to stage 1, and `pouch`-1.
6. Knockdown: `stack` and `pouch` spill to the ground, and `shift_left` is kept (existing
   refund).
Every read has a writer, every write a reader. Loop 5 -> 1 -> 2/4 -> pouch -> 5: bootstrap
by a throw or a customer at a closed sign (G1); ends as pouches and stacks drain; floor: a
broke herd lives on player-funded public jobs, whose wages refill pouches.

#### Interaction matrix (input x stage)
| input | pay in | shift start | serve | overflow | spend | knockdown |
|---|---|---|---|---|---|---|
| player throw | up | enables | 0 | up | 0 | 0 |
| sale | up | enables | up (a serving owed) | up | 0 | 0 |
| `RESERVE` | 0 | 0 | 0 | down (higher means later) | 0 | 0 |
| `MARKUP` | 0 | 0 | down (shorter serving) | up | 0 | 0 |
| `pouch` | 0 | 0 | 0 | 0 | enables | spills |
| wave hits | 0 | blocks (worker down) | blocks | 0 | down | up |

#### Chart: worker gems/min and open share at extremes (steady state, reserve full)
| case | g | d | open | worker gems/min | of which overflow |
|---|---|---|---|---|---|
| nobody pays | 0 | 0 | 0% | 0 | 0 |
| thin customers | 0 | 0.5 | 50% | 0.5 | 0 |
| customers at par | 0 | 1 | 100% | 1 | 0 |
| busy, capacity cap | 0 | 2 | 100% | 2 | 1 |
| player funds only | 1 | 0 | 100% | 1 | 0 |
| player + busy | 1 | 2 | 100% | 3 | 2 |
| wave overpay | 5 | 0 | 100% | 5 | 4 |
| today's bar (1 gem/drink) | 0 | 20 | 100% | 20 | (straight to pouch) |
The cap is d <= 60/SERVE_SEC = 1 + MARKUP. So c2c pay can be at most 2x p2c pay per
workplace, against 20x today. `open` clamps flat at 100% above g + d = 1. That is meant:
past 1 gem a minute, extra money buys pay, not hours.

#### Constant ledger
- `GEM_SEC` = 60: the pace. It is the one rate of the economy; everything is pegged to it.
- `MARKUP` = 1: a weight. A customer-funded job pays up to 2x a player-funded one, so
  private work is visibly richer and the player's overpay has room to compete. At 0, the
  overflow from customers vanishes.
- `RESERVE` = 2: a cap. It covers 2 min of hours before surplus reaches the worker. It is
  a limit, not a threshold that gates behavior.
- `serving` sizes are authored data per workplace (bar stay = SERVE_SEC / 3 s per drink
  = 10 drinks), not constants.

#### Answers to the user's three questions
- **Unit cost vs time:** one unit = 1 gem = SERVE_SEC (30 s) of the worker. The rate is
  1 gem per 60 s of labor, plus a 2x markup for customers.
- **Prices by supply and demand:** no. Prices are fixed and posted. Demand shows in the
  stack, the queue, and the overflow.
- **Wage by seniority, supply, and demand:** a flat time floor plus a demand-driven
  overflow. Seniority comes only through skill, which means faster serving and more sales.
  No seniority rule: Dungeon Keeper-style raises turn a role into a purchase over time.
### 5. Gates the code cannot settle (user)
- G1: does a creature walk to a *closed* sign to buy? If not, customer-funded jobs never
  bootstrap (creature.gd:1055 buy needs the seller there).
- G2: what does overflow change? The pillar says "how much it works, never at what". The
  PR 18 work-drive lever was measured and cut. So "pay wave jobs more" can mean deeper
  prepay (open through the wave) plus a richer pouch. It must not mean pulling workers
  between jobs, which would bend the pillar.
- G3: the bar change. The sale moves from the bartender's pouch to the stack, the price
  moves from per drink to per stay, and "a broke one drinks free" either stays or goes.
- G4: is a sink inside the herd needed? Probe the total of all pouches over 900 s first.

Sources (other game facts from memory, unchecked): [Lazear, Performance Pay and Productivity](https://www.gsb.stanford.edu/faculty-research/publications/performance-pay-productivity),
[HKCER reprint (half incentive, half sorting)](https://hkcer.hku.hk/Letters/v61/lazear.htm),
[McGill note (hourly guarantee)](https://www.mcgill.ca/economics/files/economics/SortingAndIncentiveEffects.pdf),
[DF wiki v0.31 Coin](https://dwarffortresswiki.org/index.php/v0.31:Coin),
[DF wiki 23a Economy](https://dwarffortresswiki.org/index.php/23a:Economy).

## Raw: pay_b

## Payment model, diverger B (lens: the gem paths in the code that runs)

**Frame.** Time and units are not two rival systems; they sit on two different edges. Every
workplace is a small firm: whoever *funds* it (the player, a customer) puts gems on its sign;
the sign always pays its worker *for time* (one gem a shift). A customer's gem is counted per
*unit* served, the player's per *minute* bought, but both land on the same sign. That is how
real firms work (Coase: time contracts inside the firm, prices across it) and how Two Point
Hospital works (patients pay per treatment, staff draw salaries from the same account).

### 1. The gem paths that exist today (checked in the source)
Holders (a holder takes gems in and gives them out; each is a separate counter today):
player inventory; a floor gem (`DroppedItem`); a sign stack (`Wage.gems`, on every `Station`);
a bank vault (`Bank.vault`); a creature's pouch (`Creature.pouch`, with `loot` the stolen part);
a creature's bag (`JobComponent.bag[GEM_PATH]`).

| # | path | from -> to | code |
|---|---|---|---|
| 1 | wild dies | nothing -> floor | `wild_drop_service.gd:15` |
| 2 | banker grows | nothing -> vault, 1 per 20 ticks | `bank.gd labor` |
| 3 | player picks up | floor -> inventory | `dropped_item.gd` |
| 4 | player throws | inventory -> floor -> sign or vault | `Station.pay_with`, only a thrown gem pays |
| 5 | punch in | sign -> worker pouch, 1 per 60 s shift | `Creature._fetch_gem`, `Wage.start_shift` |
| 6 | till | vault -> payer bag, only while a station is due | `till.gd` |
| 7 | carry pay | bag -> nearest due sign, else bank vault | `Creature._deliver_carry` |
| 8 | bar sale | drinker pouch -> bartender pouch, 1 per drink | `bar.gd:196`, `Creature.buy` |
| 9 | rob | vault -> thief pouch, marked | `Creature._rob` |
| 10 | arrest | marked pouch -> cop bag (then path 7) | `Creature._hand_over_loot` |
| 11 | knockdown | pouch, sign, vault -> floor | `_spill_pouch`, `Station._yeet_drops`, `Bank._yeet_drops` |
| 12 | build | inventory -> gone (the only sink) | `build_hand.gd:68` |

Facts that shape the model: the bar and chalkboard are `OfferPlace`s, not `Station`s, so
their workers are never paid by time; a broke drinker drinks free; `JobBoard` opens a site
only while its sign is paid and picks the most disciplined apt idle friend, nearest breaking a
tie (pay never ranks a worker); labor interval is fixed per job (a stat never speeds output);
path 7 already holds a routing rule ("due sign first, else the bank").

### 2. The abstract problem (no game nouns)
Agents hold integer currency. Two kinds of payer (an external sponsor, internal consumers) want
work done by internal workers. Currency enters only from outside faucets into the sponsor's
hands and leaves only by the sponsor's spending. Find one contract that both payers can use,
such that: (a) the sponsor keeps a lever (where work happens), (b) money keeps moving between
consumers instead of piling in one holder, (c) every transfer is a local handoff, (d) the
smallest unit is 1 and cannot be divided.

**Abstract answer.** Put an account between payer and worker. Payers fund the account by
whatever trigger fits them (sponsor: buys time ahead; consumer: pays per unit at handover).
The account pays workers one contract only (time). Money that the account does not need
overflows to the worker, and a holder past a cap overflows to the floor, where the sponsor
recaptures it. Economics: a time wage fits work whose output is hard to measure or that must
stand ready (police, medic: Holmström and Milgrom 1991 multitask); a piece rate fits measured
private output (Lazear 2000, Safelite). Velocity (MV = PQ): with a fixed price P = 1 and a
fixed wage, the only health knob is how much consumers buy per minute against what they earn.
Games: Settlers and Banished avoid money (no velocity problem); Dwarf Fortress shipped coins
with nothing to buy and they piled until the system was cut; Majesty pays heroes by bounty
(units) and sends a tax collector to walk shop gold back to the palace (on-screen recapture);
Two Point Hospital and The Sims pay time wages and charge per unit; Tropico and Anno fix prices.

### 3. Three whole-model shapes

#### Shape A. The sign is a firm's till (time wages, unit prices, one account)
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| hours | player -> sign | open hours, 60 s a gem | TIME | p2c | gem lands on the sign, `💎 n m:ss` |
| wage | sign -> worker pouch | one shift | TIME | both | worker walks to the sign, `💎` pops over it |
| price | customer -> worker's hand -> sign if due, else worker pouch | one unit served | UNIT | c2c | `💎` hops drinker to bartender; sign ticks up when it was out |
| delivery | payer or cop bag -> sign if due, else vault | keeping a sign open | TIME | both | payer walks gems to an empty sign |
| overflow | worker pouch past cap -> floor stack at its workplace | nothing, it is surplus | none | c2p (creature to player) | a gem pile grows on the bar counter; the player walks in to scoop it |
Scene: before a wave the player throws ten gems on the police box (ten minutes ahead) and
none on the woodpile; the bar keeps itself open on drink money; mid-wave the bartender's pouch
is full and gems pile on the counter; the player runs past and scoops them for the next build.
Price rule: fixed per kind in config, 1 gem now. Wage rule: flat, 1 gem per shift; no seniority,
no supply and demand (a wage that drew workers would change *at what* a creature works, which
the gem pillar forbids; stats already pay by opening jobs). Money in: wild drops, bank growth.
Out: build cost; recaptured by overflow and spills. Failures: piling (bartender) is capped by
overflow; drought (herd broke) closes the bar until the player funds it, and broke drinkers
still drink free so fun survives; a bad wave spills pouches to the floor, so money comes back
to the player, not lost; the player keeps the lever because no creature path puts gems on a
sign that is not due (one gem keeps it barely open, only the player stacks hours ahead).

#### Shape B. Bounty for everything (unit for both)
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| bounty pot | player -> sign | K units of output | UNIT | p2c | sign shows `💎 n` and units left |
| piece pay | sign -> worker pouch | each K units (logs in, arrest, rescue) | UNIT | p2c | `💎` pops each delivery |
| price | customer -> worker | one unit served | UNIT | c2c | as today |
Scene: before a wave the player loads the police box and med kit with bounty; between waves
they cost nothing because nothing is arrested. Price: fixed. Wage: per unit; seniority would be
automatic only if stats sped labor, and they do not. Failures: breaks the user's open-hours
pre-pillar (no time on the sign); every job needs an authored unit (payer, banker, teacher have
none clean); idle ready-jobs earn nothing so the sign never closes and never signals; piling
at the bartender is unchanged.

#### Shape C. Rounds: every payer buys time (time for both)
| payment | who pays -> who gets | for what | TIME or UNIT | p2c / c2c | what the player sees |
|---|---|---|---|---|---|
| hours | player -> sign | 60 s open | TIME | p2c | as today |
| a round | customer -> sign, only when due | 60 s open, for every seat | TIME | c2c | a drinker walks a gem to the bar sign; "a round on me" |
| wage | sign -> worker | one shift | TIME | both | as today |
Scene: the bar's sign runs out; a creature with gems walks up and pays it; for a minute
everyone seated drinks, payers and free riders alike. Price = wage = 1 gem a minute, so no
surplus exists and nothing piles. Path count is lowest: `Creature.buy` is deleted and the
customer reuses path 7 (carry to a due sign). Failures: the decided rule "gems beyond its needs
go to the worker" becomes empty; a drinker's gem no longer maps to its drink; the bartender's
wage has only one place to go (another bar), so it piles there.

### 4. Rank and prune log
1. **A**: keeps every user decision, gives each payer the natural trigger, and needs one new
   rule (route a customer's gem by "due") that path 7 already runs; overflow reuses the spill
   spawn. 2. **C**: fewest paths, but voids a decided row; offer it if the user prefers pure
   time. 3. **B**: breaks a user pre-pillar and has no unit for half the jobs.
Prune log: cut "wage rises with stack depth" (deep stack burns faster, and a higher wage only
buys more bar trips since gems no longer change drive: less work, not more); cut "pay ranks the
job board" (gem picks at what a creature works: pillar); cut "rich creatures deposit at the
bank" (the payer walks vault gems to due signs, so the herd self-funds every sign and the
player loses the lever; the floor overflow leaks to the player instead).

### 5. SPECIFY for Shape A

**Data dictionary**
| name | type, range | owner | definition | lifecycle |
|---|---|---|---|---|
| `sign.gems` | int >= 0 | per workplace (`Wage`) | gems stacked, not yet worked | +throw, +due price, +delivery; -1 per punch in; spills on knockdown |
| `sign.shift` | s, 0..GEM_SEC | per workplace | the shift under way | armed at punch in, runs on dilated clock |
| `due` | bool | derived | on its last shift with 0 stacked (`Station.due`) | read each route |
| `pouch` | int >= 0 | per creature | its gems, wages and takings | +wage, +price; -price; overflow, spill |
| `loot` | int, 0..pouch | per creature | the marked (stolen) part, never spent | +rob; -arrest |
| `bag gems` | int, 0..BAG_CAP | per creature | gems carried to a sign | +till, +arrest; -delivery |
| `vault` | int >= 0 | per bank | the bank's sign; needs no shift | +throw, +grow, +delivery; -till, -rob |
| `price[kind]` | int >= 1 | config | gems one served unit costs | constant |
| `R` | float >= 0 | probe | `Creature.bought / Creature.wages` over a window | measured |

**I/O pipeline (one served unit, then the money's way home)**
| stage | reads | writes | passes on |
|---|---|---|---|
| 1 fund | player inventory | `sign.gems` | an open sign to `JobBoard` |
| 2 hire | `sign` open, discipline, apt | site worker | a worker walking to the sign |
| 3 punch in | `sign.shift`, `sign.gems` | `sign.gems -1`, `pouch +1` | a shift |
| 4 serve | customer `pouch - loot >= price` | customer `pouch -price` | the gem in the worker's hand |
| 5 route | `due` | `sign.gems +price` if due, else worker `pouch +price` | a funded sign or a richer worker |
| 6 overflow | `pouch - loot > POUCH_CAP` | `pouch` to cap; floor stack at the workplace | a pickup for the player |
| 7 recapture | floor stack | player inventory | gems for stage 1 or a build |
Stage 5 is the same function as path 7's choice ("due sign, else a fallback holder"); only the
fallback differs (worker pouch, or the bank vault). Every stage reads something a stage wrote.

**Interaction matrix** (row raises `+`, lowers `-`, `0` none)
| input \ holder | sign | pouch | vault | floor | player |
|---|---|---|---|---|---|
| player throw | + | 0 | + | 0 | - |
| punch in | - | + | 0 | 0 | 0 |
| customer price | + if due | +seller -buyer | 0 | 0 | 0 |
| payer delivery | + | 0 | - | 0 | 0 |
| overflow | 0 | - | 0 | + | 0 |
| pickup | 0 | 0 | 0 | - | + |
| knockdown | - | - | - | + | 0 |
| build | 0 | 0 | 0 | 0 | - |
No row is all `0`, no column is all `0`.

**Chart: one bar, per game minute** (N paid workers each earn 1 gem a minute; each spends d
drinks a minute while it has gems; a bar serves at most 20 a minute; the bar needs 1 a minute)
| case | N | d | sold | bar funded by | bartender gain | each worker gain | R |
|---|---|---|---|---|---|---|---|
| tiny herd | 3 | 0.2 | 0.6 | player tops 0.4 | 0 | +0.8 | 0.2 |
| mid | 10 | 0.5 | 5 | itself | +4 | +0.5 | 0.5 |
| thirsty | 10 | 1.0 | 10 | itself | +9 | 0 | 1.0 |
| crowded | 30 | 1.0 | 20 (cap) | itself | +19 | +0.33 | 0.67 |
| broke after a wave | 10 | any | 0 paid | player, or it closes | 0 | +1 | 0 |
Reading: with price 1 and wage 1 a minute, any herd past 2 drinks a minute makes the bartender
the herd's pile; without a cap it is Dwarf Fortress coins. With `POUCH_CAP` the pile turns into
a counter stack the player scoops, so a busy bar is a gem source for the player (Majesty's tax
collector, walked by the player). Healthy target: R between 0.5 and 1 (workers neither pile nor
go broke); R is read from tallies that already exist. Below 0.5 the fix is more things to buy,
not a lower price (price cannot go below 1).

**Constant ledger**
| constant | value | kind | why |
|---|---|---|---|
| `GEM_SEC` | 60 s | pace | one gem buys one shift; the wage rate |
| `price[kind]` (`DRINK_PRICE`) | 1 | weight | integer floor; a unit costs a gem |
| `POUCH_CAP` | 5 (proposed, tune on R) | cap | most a pouch holds before overflow |
| `TICKS_PER_GEM` | 20 | pace | bank growth, the faucet floor |
| `THEFT_GEMS` | 3 | cap | one haul |
| `WILD_GEM_DROP` | 1 | weight | wave faucet |

**Walking skeleton.** The bar gets a sign (a `Wage`), its bartender punches in like any worker,
the sale routes by `due`, and the cap overflows to a counter stack. Measure R on the sims
(`SIM_WAGES`) before tuning the cap.

### 6. Open questions for the user (code cannot settle these)
- "Pay wave jobs more": in A it means more hours ahead on their signs, not a bigger wage per
  shift (a bigger wage cannot raise work under the current drive, and drawing workers by wage
  breaks "never at what"). Is that the lever you meant?
- Overflow to a counter stack adds a cap to your rule "surplus goes to the worker". Keep the
  cap, or let pouches grow without bound (then the bartender hoards)?
- The bar would need the player's first gem to open (bootstrap). Fine, or should the first
  customer's gem open it?
- Chalkboard teacher and banker stay unpaid in A (no sign need). Make them sign-paid too?

## Raw: pay_c

## Payment model: diverger C (lens: what the player places and watches)

### Frame
The clash is not time vs unit. It is the payee: the player pays a **workplace** (gem on its
sign), a creature pays a **creature** (drinker to bartender). Two payees means two
economies. Fix the payee first: every payment lands on a workplace's sign, and every wage
leaves a sign. Then "time or unit" is one choice the sign makes for everyone.

Second fact that frames everything: creatures here do not optimize income. `drive()` reads
discipline and mood only (creature.gd:1085), never the pouch. So the textbook argument for
piece rate (faster work for more pay) has no lever in this game unless we code one. The
choice between time and unit is about what the player reads and where gems pile up.

### Code facts (checked)
- Sign: thrown gems stack with no cap; a worker at its station takes 1 gem per 60 s shift
  into its pouch (wage.gd `start_shift`, creature.gd:1216 `_fetch_gem`).
- Bar is not a Station: it is an OfferPlace with no sign. A drinker pays `DRINK_PRICE` = 1
  gem per drink straight to the bartender (bar.gd:196, creature.gd:1054).
- A spendable gem pulls its creature to the bar (offer_place.gd:164 `SPEND_GAIN`).
- A bank payer carries vault gems to a sign that is `due` (till.gd); knockdown spills the
  whole pouch on the ground (creature.gd:1349). Wild death drops 1 gem.
- Day cycle: first cycle about 28 s real (15 s daylight), +10% per wave.

**Measured contradiction in the built game:** a worker earns 1 gem/min. A bar serving 1
drink per 3 s can take 20 gems/min. So the bar can absorb the whole herd's wages, and the
bartender earns up to 20x any other worker, and cannot spend at its own bar. Every gem the
herd earns flows to one pouch and stops. This is the piling failure, built in today.

### Abstract problem (no game nouns)
A principal with outside income funds service points. Agents earn currency at service
points and spend it at other service points. Currency enters from outside (a source), the
principal destroys it (the only sink), and shocks spill agent holdings back to the ground.
Two contract types exist: a **time contract** (the payer buys a span during which a point
is open; the worker is paid per span) and a **unit contract** (the payer buys output; the
worker is paid per output). Want: one rule for both payer classes, a stable money stock in
agents (no pile, no drought), and the principal keeps a lever.

### Abstract answer, with the field
- **The firm (Coase):** real economies use both contracts, but on different edges. Customers
  pay the firm per unit; the firm pays workers per time. The firm's till joins them; its
  surplus is profit. So "both" is coherent only with a till in the middle.
- **Piece rate vs wage (Lazear, Safelite 2000; Holmstrom-Milgrom multitask):** piece rate
  fits output the worker controls and can count. It fails for on-call work (guard, medic,
  cop): no wild, no unit, no pay. Our wave jobs are on-call.
- **Time banking (Ithaca HOURS, time dollars):** one credit = one hour of anyone's work. A
  single unit of account kills price setting entirely; readable, no arbitrage.
- **Velocity (Fisher, MV = PQ):** with no agent-side sink, agent money grows by every injection.
- **Sticky prices:** fixed menus are the norm; demand shows as a line, not a price.
- **Backward-bending labor supply:** richer workers take more leisure (here: a gem pulls to the bar).
- **Games:** Settlers, Banished, RimWorld: no wages, flows are goods. Anno: fixed prices,
  demand as satisfaction. Tropico: per-building wage the player sets (pay raises
  happiness, a time wage). Two Point Hospital: wage rises with level (seniority); a
  well-known payroll death spiral. Majesty: bounties pay per result and pull heroes to
  targets (pulls "at what": breaks our gem pillar). Dwarf Fortress: coin economy
  disabled; dwarves hoarded, nothing to buy. The Sims: hourly job pay.

### Three shapes
Terms used below:
- **Sign**: a workplace's pay board. Takes in gems from anyone who throws or sets them on
  it; gives out wages to its own worker; connects payers to one worker.
- **Fill line**: the number of gems a sign holds ahead. Takes in nothing; it decides when a
  landing gem overflows to the worker on duty instead of stacking.
- **Shift**: 60 s (game clock) a worker works after taking 1 gem off its sign.

#### Shape A: Coin-op (everything is TIME, sign is the only payee)
A gem on any sign buys 60 s of open hours, whoever drops it. A creature that wants a closed
service walks up and slaps a gem on its sign, like a coin in a jukebox; while open, the
station serves everyone. "Drinks on me" is the scene: one creature opens the tap, the
whole counter cheers.

| payment | who pays -> who gets | for what | TIME/UNIT | p2c/c2c | what the player sees |
|---|---|---|---|---|---|
| fund | player -> sign | open hours | TIME | p2c | gem lands on sign, timer grows |
| coin-in | creature -> sign | open hours | TIME | c2c | creature slaps gem on sign, cheer |
| payroll fetch | bank payer -> sign | open hours | TIME | both | payer trots gem from vault to sign |
| wage | sign -> its worker | a shift | TIME | both | worker pockets gem, 💎 pop |
| overflow tip | sign -> worker on duty | gems past fill line | TIME | both | gem tumbles off sign onto its head |
| spill | creature -> ground | knockdown | none | both | gems burst from a bonked creature |
| build | player -> world | a piece | sink | p2c | gems vanish into the build |

- **Price rule:** fixed, 1 gem = 60 s, for all payers. Unit cost is emergent: 60 s divided
  by seconds per unit (a drink is 1/20 gem). No supply/demand price; demand shows as a crowd
  at a closed sign.
- **Wage rule:** flat 1 gem per shift. No seniority multiplier: raising shows as pace, so a
  skilled worker gives the player more output per gem (raising pays the player, visibly).
- **Money in/out:** in from wilds and bank; out only through builds. A customer gem funds
  one worker-minute: c2c recycles at 1:1. Herd pouches grow by exactly the
  player-funded shifts.
- **Failures:** piling (herd grows rich if the player funds a lot; spill on knockdown is
  the slapstick return, scooped by the player); free riding (one coin opens for all, so
  spend per creature falls; harmless, it is a cheer); drought after a bad wave (fewer wild
  gems; herd savings still fund leisure, so the floor is the herd's own pouches); player
  loses lever (no: production and wave signs have no creature customer, only the player
  and the bank payer fund them).
- **Gap to flag:** the fill line conflicts with "may be paid ahead without limit".

#### Shape B: Shop and payroll (UNIT in from customers, TIME out to workers, one till)
The sign is a till. A customer pays per unit into it; the player pays it for time; the
worker always takes 1 gem per shift; gems past the fill line are the worker's profit share.
Integer gems force bundles: the sign reads `💎 = 🍺x5`, a jug for the table.

| payment | who pays -> who gets | for what | TIME/UNIT | p2c/c2c | what the player sees |
|---|---|---|---|---|---|
| fund | player -> till | open hours | TIME | p2c | gem on sign, timer grows |
| buy | creature -> till | a bundle of k units | UNIT | c2c | gem on counter, jug comes back |
| wage | till -> worker | a shift | TIME | both | worker pockets gem |
| profit share | till -> worker | gems past fill line | TIME | both | gem tumbles to worker |
| spill, build | as in A | | | | |

- **Price rule:** k = (60 s / seconds per unit) / m, markup m >= 1. Fixed per station; a
  floating k (cheaper when the till is full) is possible but a moving menu is unreadable.
- **Wage rule:** flat 1/shift plus profit share; busy stations pay their workers more
  (demand, earned by traffic, not seniority).
- **Failures:** two contracts on one sign (the player must read two numbers); a high m
  rebuilds today's bartender pile; bundles of k units a creature cannot use alone.

#### Shape C: Hand to hand (everything is UNIT, the worker is the payee)
The sign holds the player's gems in escrow; the worker gets 1 gem each time it finishes a
batch of B units (B logs, B harvests, B knockdowns for a guard). Customers pay the worker
per unit, as the bar does now. Scene: a guard whacks a wild, a gem pings off the post into
its pouch.

- **Price rule:** B set so an average worker finishes B in about 60 s; skilled = richer.
- **Wage rule:** pure piece rate; seniority and supply emerge as pace.
- **Failures (disqualifying):** on-call jobs (guard, medic, cop) earn nothing before a wave,
  so "productivity before each wave" goes unpaid; a fast worker grows rich and drinks
  (backward bend); keeps today's bartender pile.

### Rank
1. **A, Coin-op.** One verb (gem on sign), one meaning (60 s open), same for player and
   creature. Natural on sight (coin in a jukebox), funny ("drinks on me"), no price table,
   and the only shape where c2c money cannot pile on one creature. The player's real
   decision: fund leisure yourself, or let the herd fund it from wages and spend your gems
   on wave signs.
2. **B, Shop and payroll.** Truest to real firms, but two numbers on one sign, and once k is
   set fair it turns into A with bundles.
3. **C, Hand to hand.** Cut: on-call wave jobs earn nothing before the wave.

Prune log: C cut (on-call work has no unit). Floating prices cut (moving menu breaks
readability; Majesty-style pull on job choice breaks "never at what"). Seniority cut (a
hidden multiplier; pace already shows raising).

### Answers to the user's three questions (under A)
- **Unit vs time:** price time only, 1 gem = 60 s; a unit's cost falls out of pace.
  Healthy = herd income (player-funded shifts/min) about equal to herd want (closed
  services it walks to). Watch herd pouch total per dawn.
- **Supply vs demand prices:** no. Demand shows as a crowd at a closed sign; supply as an
  open timer. The player reads both without a number.
- **Seniority + supply/demand wage:** no. Flat wage; skill shows as pace, busy signs
  overflow tips to their worker, so a wanted station pays more by traffic.

### SPECIFY (Shape A)

#### Data dictionary
| name | type, range | owner | definition | lifecycle |
|---|---|---|---|---|
| sign.stack | int 0..F | per station | gems waiting on the sign | +1 per gem landed, -1 per shift; spills on knockdown |
| sign.shift_left | s 0..60 | per station | open time left on this shift | armed 60 at punch-in, burns on station clock |
| creature.pouch | int >= 0 | per creature | gems held (wages, tips, loot) | +wage, +tip, -coin-in; 0 on knockdown spill |
| creature.loot | int 0..pouch | per creature | stolen part, never spent | to police on arrest |
| want(kind) | float >= 0 | derived | existing OfferPlace pull for a service | recomputed per decision |
| herd_pouch | int | metric | sum of pouch over herd | probe at dawn |

#### Constant ledger
| constant | value | kind | why |
|---|---|---|---|
| GEM_SEC | 60 | pace | one gem buys one minute; the single unit of account |
| FILL_LINE (F) | 3 (proposed) | cap | gems a sign holds ahead; past it, tips. Conflicts with unlimited pay-ahead: user call |
| WILD_GEM_DROP | 1 | limit | source rate per wild death |
| DRINK_PRICE | removed | | replaced by coin-in on the bar's sign |

#### I/O pipeline
| stage | in | out | reads | writes |
|---|---|---|---|---|
| 1 inject | wild death, bank vault | gem on ground / in vault | WILD_GEM_DROP | ground |
| 2 carry | player pickup, bank payer | gem in hand | sign due | hand |
| 3 land | gem on a sign | stack +1 or tip | sign.stack, F | sign.stack or worker pouch |
| 4 punch-in | worker at sign, stack >= 1 | shift armed, wage | sign.stack | sign.stack, shift_left, pouch |
| 5 serve | shift_left > 0 | service to anyone present | shift_left | needs of customers |
| 6 coin-in | creature want, sign closed, spendable >= 1 | walks, slaps gem (to 3) | want, pouch, shift_left | pouch |
| 7 spill | knockdown | gems on ground (to 2) | pouch | pouch = 0 |
| 8 sink | player build | gems destroyed | cost | player gems |

Check: every read has a writer; stage 6 writes back into stage 3, closing the c2c loop at
1 gem in = 1 worker-minute out. Bootstrap: a creature with 0 gems starts from a
player-funded wage (stage 4). Termination: coin-in needs a closed sign and a want, so it
stops when needs are met. Floor: a broke herd still gets served at player-funded signs.

#### Interaction matrix (input by output)
| input \ output | stack | shift_left | worker pouch | customer pouch | ground | player gems |
|---|---|---|---|---|---|---|
| player throw | up | 0 | up past F | 0 | 0 | down |
| creature coin-in | up | 0 | up past F | down | 0 | 0 |
| bank payer | up | 0 | up past F | 0 | 0 | 0 |
| punch-in | down | up | up | 0 | 0 | 0 |
| knockdown | down (station) | clear | down (creature) | down | up | 0 |
| wild death | 0 | 0 | 0 | 0 | up | up on pickup |
| build | 0 | 0 | 0 | 0 | 0 | down |

#### Chart: formulas at extremes
Unit cost = 1 gem per (60 / t) units; herd pouch drift per minute = P (player-funded
shifts/min) + T (tips/min) - S (spill/min). Coin-in moves gems customer to worker: net 0.

| case | t (s/unit) | units per gem | drift inputs | herd drift/min |
|---|---|---|---|---|
| fast service (bar today) | 3 | 20 | P=0, T=0, S=0 | 0 (closed loop) |
| slow service | 30 | 2 | P=3, T=0, S=0 | +3 (pile) |
| mid | 10 | 6 | P=3, T=1, S=4 (wave) | 0 |
| bad wave | any | any | P=0, T=0, S=6 | -6 (gems to ground, player scoops) |
| built game today, bar | 3 | 1 drink = 1 gem | W workers | bartender +W, others 0 |

Read: in A no income depends on a station's pace (the bar today: 20x). Herd stock rises
with player funding, falls with wave chaos: fund by day, spill at night, scoop, fund again.

### Open questions for the user
1. Fill line vs unlimited pay-ahead: cap at F (overflow tips) or keep unlimited (no
   tips from the sign)?
2. "Pay wave jobs more": under A it means more hours and more open wave signs. A faster
   pace for a tipped worker needs `drive()` to read the pouch, a new link. Want it?
3. Should the bar become a sign-carrying workplace (needed for coin-in)?

## Raw: auditor_pay

## Payment model: essence audit (cold read of pay_a, pay_b, pay_c)

**Frame.** The nine shapes reduce to two survivors and one cut. The real fork is not
"time or unit". It is **who a creature's gem serves**: itself alone (firm) or everyone
present (coin-op). Under both survivors sits one gap that no diverger closes: the user's
"gems beyond its needs" has no defined "needs", and every answer except one caps the
player's unlimited pay-ahead.

### 1. Essences and merges
| group | members | one-sentence essence | verdict |
|---|---|---|---|
| Firm | A-A, B-A, C-B | Every workplace has one sign; the player buys hours on it, a customer buys one serving into it, and it pays its worker 1 gem a shift. | survives |
| Coin-op | A-B, B-C, C-A | A gem on any sign buys 60 s open for everyone present, whoever paid. | survives |
| Piece rate | A-C, B-B, C-C | Pay per finished unit of output. | cut: on-call jobs (guard, medic, cop) have no unit before a wave, and it removes the paid time that burns down on the sign (pre-pillar). Same reason in all three. |

Firm vs coin-op is a real difference, not a duplicate: in the firm a gem is a private
purchase (one drinker's stay); in coin-op it is a shared one (one creature opens the tap,
free riders drink). Different sacrifice, so different purpose.

Firm members differ on two knobs only, so they merge into one shape with two forks:
- **Price peg.** A: 1 gem = one stay of SERVE_SEC (30 s) of worker time. B: 1 gem a drink,
  no peg. C-B: 1 gem = a bundle of k drinks. B without a peg keeps the user's complaint
  as is (c2c pays about 10x p2c), so it does not answer the question asked.
- **Where surplus goes.** A: stack above RESERVE (2) hops to the worker. C-B: above a fill
  line. B: a customer gem goes to the sign only when the sign is `due`, else to the worker;
  a pouch above POUCH_CAP spills to a counter pile the player scoops.

### 2. Pillar test, cold (P = pass, F = fails, ? = needs the user)
| pillar | Firm (peg + RESERVE, A) | Firm (due routing, B) | Coin-op |
|---|---|---|---|
| Gem pays open hours, burns down, paid ahead without limit (pre) | F: RESERVE 2 turns a 3rd thrown gem into pouch money. A's own scene ("throws 3, sign reads 💎3") contradicts its rule. | P: player gems always stack; only customer gems route. | F with fill line, P without (then no surplus at all). |
| Creature holds gems; changes how much it works, never at what | ? "how much" is unbuilt: drive() ignores the pouch. | ? same | ? same |
| Roles emerge, never bought | P (pay never ranks the job board) | P | P |
| Natural on sight | P at a bar ("cover for a stay"); a stay of 10 drinks is new behavior | P (pay per drink, as today) | P at a bar ("drinks on me"); F for a meal or haircut (a minute of kitchen?) |
| Add connections, not things | 4 new constants + "serving" per workplace | 1 cap + a floor pile | 1 new verb (coin-in), deletes buy |
| Reward is a rule, never a resource pile | P | ? the counter pile is a steady gem drip back to the player, not a choice on one object | P |
| Black box, clear interface | ? two rates on one sign (hours, and gems per stay) | ? same gem lands in two places by sign state (visible hop, so legal) | P one number |
| Frictionless hoarding (antipattern) | F: pouches grow, no herd sink | P: POUCH_CAP | F at scale (see 30 drinkers) |
| Tone | P | P | P (best gag) |
| User decisions: customers + player both fund; surplus to worker; lever = pay wave jobs more | surplus P, lever weakened by RESERVE | all P; adds a cap (B flags it) | surplus row is empty unless a fill line, which breaks pay-ahead (C flags it) |

**Cross-shape finding:** "pay wave jobs more" can only mean "more hours ahead" in every
shape. A bigger wage does nothing: drive() reads discipline and mood only
(creature.gd:1085-1087), and JobBoard ranks discipline then distance, never pay
(job_board.gd:289-291). A richer pouch adds bar pull (SPEND_GAIN, offer_place.gd:162-166),
so if anything it pulls a worker away on its breaks. Any shape that caps the sign (A
RESERVE, C fill line) shrinks the player's one working lever.

### 3. Extremes (real bar: 3 seats, bar.tscn Spot1-3; 1 labor tick per 3 s that serves OR mixes)
| case | Firm A (peg) | Firm B (due routing) | Coin-op |
|---|---|---|---|
| herd gems 0 | bar closes unless player funds it; today it opens unpaid and broke drink free | same, unless "broke drinks free" is kept (B keeps it) | bar closes unless player funds it |
| herd gems huge | pouches pile, nothing to buy beyond ~2 sales/min a shop | bartender hits POUCH_CAP, counter pile grows for the player | creatures only pay closed signs, so most gems sit idle in pouches |
| player throws 0 | no wages anywhere, so no c2c money; bank vault grows only while it holds a gem | same | same |
| workplace, no customers | open only if the player funds it; fine for wave jobs | same | same |
| busy bar, 30 drinkers | 3 seated, 27 wait; peg caps the bar at ~2 gems/min while 30 workers earn ~30/min: herd piles | sold ~10/min sustained, ~20 burst; bartender earns ~10x others, cap spills it to the player | 1 gem/min opens the bar for all; ~29 gems/min pile in pouches |

**Core trade the extremes expose:** pegging (A, coin-op) fixes the unfair exchange rate but
leaves the herd almost nowhere to spend, so pouches pile. Not pegging (B) gives the herd a
fast spend but piles on the bartender, which B fixes only by draining to the player. Health
needs one of: a shop count that scales with workers, more things to buy, or a herd-side
sink. No shape names one inside the herd. This is the question to put to the user.

### 4. Undefined concepts (by what they take in and give out)
- **"needs"** in "gems beyond its needs go to the worker" (user decision): no shape defines
  it except B, where need = the sign is `due` (shift running, 0 stacked, station.gd:103).
  A and C define it as a fixed stack size, which caps pay-ahead.
- **A "serving" / "stay"**: what ends a stay of 10 drinks? Today a stay ends on the fun need;
  a fixed-length stay is a new rule nobody defined.
- **A "private vs public job"**: no list of which workplaces customers fund.
- **A "seniority pays through output"** and **C "skill shows as pace"**: the link does not
  exist (see facts).
- **C "coin-in at a closed sign"**: which want level makes a creature walk to a closed sign
  and pay? New behavior, no trigger.
- **C "service to anyone present"** for a workplace without seats (meal, haircut): undefined.
- **B "counter pile"**: defined, but whether it is recapture (player income) or a sink is not
  stated; it makes a busy bar a gem faucet for the player.

### 5. Code facts re-checked
Correct: drive() ignores the pouch (creature.gd:1085-1087). Bar and Chalkboard extend
OfferPlace, not Station (bar.gd:2, chalkboard.gd:2), so bartender and teacher are unpaid and
the bar opens with no gem (JobBoard._open returns true for a non-Station site,
job_board.gd:220). JobBoard ranks discipline, then nearest (job_board.gd:289-291), never pay.
_deliver_carry sends a gem to Station.due_near, else Station.taking (the bank)
(creature.gd:1169-1176); Till hands a gem only while some station is due (till.gd:10).
buy() is the only c2c sale and bar.gd:196 its only caller; the bartender drinks free at its
own bar. Build is the only sink (build_hand.gd:68). Bank grows 1 gem per 20 ticks
(bank.gd:10). Spill empties the whole pouch (creature.gd:1349-1354).

Wrong or loose:
1. **Bar rate (brief, A, C):** "1 drink / 3 s, 20 gems/min" is the burst. Each 3 s tick
   serves OR mixes a crop (bar.gd:74-81; BARTEND interval 3.0, creature_config.gd:231-236),
   so once the 8-drink stock runs out it is ~1 drink / 6 s (~10/min), crop-limited, 3 seats.
   The gap is about 10x, not 20x. A's "10 drinks = SERVE_SEC 30 s" is then ~60 s of
   bartender time, so A's markup is really 0.
2. **A: "shift_left kept on knockdown (existing refund)".** Wrong: Wage.refund() clears the
   shift window (wage.gd refund); only the shift's gem, already in the worker's pouch, is kept.
3. **A and C: a skilled worker serves faster.** Wrong: the labor interval is fixed per job;
   only tipsy slows it (job_component.gd:150-151). drive() lengthens WORK sessions, not
   tick speed (job_component.gd:125-129). Stats gate jobs; they never speed output (B is right).
4. **A: "buy needs the seller there" (creature.gd:1055).** buy() at creature.gd:1054 checks
   the seller is FRIENDLY and not leaving, not distance. Distance comes from the bar seat.
5. **Not stated by anyone, matters:** `due` is false on a fully closed sign. No creature path
   reopens a closed sign today; A's G1 and C's coin-in both need a new path.
6. Stale comment (not a diverger error): job_board.gd:212-214 calls a chalkboard a ring
   site, but TEACH has no "ring" key (creature_config.gd:275-282).

## Raw: challenger_pay

## Challenger: the payment model (attacks A + B till, C coin-op)

**Frame attack.** All three solve "one exchange rate" (a gem means the same labor whoever
spends it). The user's frame is productivity first. In the code a creature's gem changes no
measured productivity: work is capped by open jobs, not stretch length (PR 18h measured,
`docs/HANDOFF_playtest_tuning.md:378`), `drive()` reads discipline and mood only
(`creature.gd:1085`), and labor pace is fixed per job, slowed only by tipsy
(`job_component.gd:150`). So a pegged rate tunes *who holds gems*, which feeds nothing that
wins a wave. Pick the model by where c2c gems connect to open jobs, not by its rate.

### Code facts the divergers got wrong or skipped
- **F1. Skill does not pay through output.** A ("a more skilled worker serves faster and
  sells more") and C ("skill shows as pace") both rest their "no seniority rule" answer on
  this. False: `spec.interval * slow`, slow from `is_tipsy()` only (`job_component.gd:150`).
  B says it right. Severity high: the seniority answer in A and C has no mechanism.
- **F2. Spending lowers productivity today.** A drink while the drink effect is still on
  makes the drinker tipsy (`creature.gd:2328`), and tipsy slows labor
  (`TIPSY_LABOR_SLOW`). A gem pulls a creature to the bar (`offer_place.gd:164`). So a richer
  worker drinks more and works slower; the mood moodlet is the only plus. Net sign unmeasured.
- **F3. "20x" is capacity, not measured.** The bar serves owed drinks: one per stay plus a
  round per chat, at most 2 owed at once (`bar.gd:7,14`), and each drink needs a crop
  (`bar.gd:8`). Real sales per minute are bounded by stays and crops, not 1 per 3 s. A's peg
  and C's "built-in pile" both lean on 20x. The tally exists: `Creature.bought` vs
  `Creature.wages` (`balance_probe.gd:751`). Measure R = bought / wages before any peg.
- **F4. A closed sign is never `due`.** `due()` = `wage.paid() and gems == 0`
  (`station.gd:103`): only a running last shift. B routes a customer gem to the sign only
  when due, so one quiet last minute closes the bar for good until the player throws again.
  Closing is absorbing. A has the same hole (gate G1).
- **F5. The only c2c-to-productivity link is aspire (18i):** a paid buy seen by a jobless
  friend sends it to study (`creature.gd:1062`). It reads the *event* of a buy, not the
  amount or price. Shipped unmeasured (`HANDOFF:560`).

### Failure scenarios
| # | scenario | hits | severity | fix |
|---|---|---|---|---|
| 1 | Player saves gems for builds two days. Herd income = player-funded shifts only, so pouches drain to 0, the bar closes (A, B) or no one coins in (C). Gem drought, and the c2c loop is dead with nothing in it to restart. | A B C | high | A faucet the herd owns: the bank's grow (`bank.gd`, 1 per 20 ticks) pays into the herd, or "broke drinks free" stays as the floor |
| 2 | Player throws 5 gems on the cannon before a wave (the lever). A: RESERVE 2, so 3 hop to the gunner's pouch at once; C: same past FILL_LINE 3. Paying a wave job "more" turns hours into pouch, and a pouch does nothing (frame). The lever leaks into decoration. | A C | high | Overflow only from customer gems, never thrown ones; or no reserve on a sign with no customers |
| 3 | A and C caps break the pillar "may be paid ahead without limit" (`MEMORY.md:12`). C flags it; A does not. | A C | high | B's shape: cap the pouch, not the sign |
| 4 | Sign reads `💎3 1:00` with player gems (60 s each) and customer gems (one 30 s serving each) mixed. The player cannot read how long it stays open. | A | med | Two piles on the sign, or B's route (customer gem lands only when due) |
| 5 | Bad wave: knockdowns spill every pouch (`creature.gd:1349`) and stack. A, C: herd broke, the bar closes, no drinks, mood sinks, snaps rise. A mood spiral, not a gem one. Today "a broke one drinks free" (`bar.gd:192`) blocks it; A (G3) and C delete it. | A C | high | Keep broke-drinks-free; a sale is extra, never the gate on fun |
| 6 | B: pouch cap 5, gems pile on the counter, player walks over to scoop each pile. Per-unit chore, the rejected "micromanagement" pattern (`MEMORY.md:54`). Also cuts the decided "surplus to the worker". | B | med | Let a capped worker spend (a shop, 18f) before any floor spill |
| 7 | Integer gems: A's serving = 30 s = "10 drinks" a stay, but a stay gives 1 drink + rounds (F3). C's bar coin-in = 20 drinks of service for 1 gem. Bundles fit no real stay. | A C | med | Price the visit (one stay, one gem), which is how the bar already counts |
| 8 | Hoarding: theft hits only the vault (`Creature._rob`); A's "rich pouch draws thieves" is unbuilt (18c). Shy creatures lean away from the bar (`offer_place.gd:155`) and sit on gems. | A | low | Measure herd pouch total first (A's own G4) |
| 9 | C: one coin opens the tap for all; the payer sees no more value than a free rider, and SPEND_GAIN pulls every holder to a sign already open. Gems stop moving while it runs. | C | med | Coin-in only on a closed sign (C's stage 6 says so; keep it hard) |

### Q2: what do creature gems do for productivity?
Measured nothing; one unmeasured plus (aspire, F5); one plausible minus (tipsy, F2). So
today the c2c economy is decoration plus one lever. Three honest options:
- **M1 Minimal (keep today):** wage to pouch, 1 gem a visit, broke drinks free, aspire. No
  peg, no till, no reserve. The rate question vanishes because nothing reads the pouch size.
- **M2 Connect gems to open jobs (the binding constraint).** The herd puts spare gems in
  the bank vault; the payer already walks vault gems to due signs (`till.gd`). Herd wealth
  then keeps production open: real productivity. B pruned this for "the player loses the
  lever". Challenge: the payer tops up only *due* signs, one gem at a time (F4: never opens a
  closed one), so the player still picks which signs exist, which open, and how far ahead.
  It is the only shape where "the economy is well" makes more work happen.
- **M3 Make the pouch read work:** cut in PR 18h (no effect); do not reopen.
Recommend M2 on M1. A and B's till is worth building only if M2 is rejected.

### Q3: the parked questions, answered honestly
- **Unit vs time ratio:** no shape can answer it until R is measured (F3). Under M2 the
  answer is "1 gem = 60 s everywhere, a visit costs 1": the vault turns surplus into hours.
- **Supply and demand prices:** no, for the readable reason all three gave. But A's "demand
  reaches the worker via overflow" pays a pouch that does nothing. Demand should show as
  the queue at the sign.
- **Seniority wage:** A and C's "pays through output" is false (F1). Honest answer: a wage
  cannot raise output here, so a seniority wage is pure decoration and breaks nothing only
  if it buys nothing that matters. Say "no" for that reason, not for "skill shows as pace".

### Backtrack candidates in the user's decisions
- **"Gems beyond a busy workplace's needs go to the worker's pouch."** Given the frame,
  this sends surplus to the one holder with no productivity use. Candidate: surplus goes to
  the bank vault (M2), where the payer turns it into open hours. Ask the user.
- **"Customers can fund a workplace."** Only leisure has customers today (bar, OfferPlaces
  with no sign, B's fact). Funding a bar does not win waves. Keep it, but it is not the
  productivity path.
- **PRE-PILLAR "paid ahead without limit"** vs any reserve or fill line: one must give. B
  keeps it; A and C silently break it.
- **"Pay wave jobs more" as the lever:** under every shape it means more hours ahead, not
  more pay. Confirm the user means hours; if they mean pay, there is no mechanism (F1, 18h).

### Verdict
Front-runner (A till) fails on #2, #3, #5, F1, F3: high. Runner-up (B till) is the safest
till, fails on F4 and #6. C fails on #2, #5, #7. Before choosing any: measure R and herd
pouch total in one sim (tallies exist), then decide M1 vs M2. If M2 wins, the time/unit split
collapses to one rule: every gem ends as open hours on a sign.
