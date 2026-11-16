# BRAINSTORM: economy frame (team-mode design, 2026-10-21)

The user's two asks (verbatim in docs/HANDOFF_playtest_tuning.md "Reframe"): creatures pay
workers instead of the player; bought goods are placed, worn, used and seen.

## Synthesis (main session)
- **Divergers A, B, C converged** on point of sale ("the till is the wage") + goods go home.
- **Auditor:** one real funding shape (P1 point of sale); bounty cut; purse only as a drain;
  goods home ranks first, worn items second, "claim not place" cut. Five code contradictions,
  incl. a customer cannot open a closed counter (buy needs the seller, creature.gd:1055).
- **Challenger:** F1 CRITICAL, a bar takes ~20 gems/min and pays out 1/min, so banking sales on
  the sign pulls gems out of circulation; F2 the 1-gem tip on a 1-gem drink leaves zero margin;
  F3 a self-funded bar takes the player's labor lever before a wave; frame may mean goods, not
  hours. Strongest alternatives: Alt-1 player keeps paying hours, creatures pay for goods;
  Alt-2 a sale keeps a dry place open, any extra goes to the server's pouch.
- **Open for the user:** the frame (hours or goods), overflow rule, margin, the player's lever,
  pillar rewordings. Answers recorded in the handoff.


## Raw: diverger_a

## Diverger A: fund workplaces like other management games, then fit

Frame: today the player is every workplace's only customer. The fix is to split who buys
what: creatures buy what creatures use up; the player buys only what the player orders.
Then the player's lever moves from "pay each station" to "where gems enter the herd".

### 1. The abstract problem (no game nouns)
- An outside agent (A) injects currency to keep producers running. Producers earn it and
  spend it with each other, so it circulates but never leaves.
- Goal: producers' running time is funded by the consumers of their output, not by A.
- Three questions: where does money enter (the faucet), where does it leave (the sink),
  and what does A steer once it no longer pays each producer?
- Risk: a closed loop with no faucet or sink gives A no decision (the passive policy wins);
  a loop with a faucet and no sink inflates until prices mean nothing.

### 2. Abstract solutions
- (a) **Revenue:** each producer is paid by whoever uses its output; A pays only for
  goods A itself orders (public goods). Faucet: A's purchases + an outside source.
- (b) **Treasury:** all money pools in one place; carriers pay producers from it;
  consumer spending is partly collected back. A steers the order of payment.
- (c) **Bounty:** A pays for outcomes (a target hit), never for hours; earners spend the
  rest; producers live off consumers.
- Sink options in all three: decay of goods, loss to enemies, a fee that leaves the loop.

### 3. How other games do it (from memory; the lead stays verifiable by the reader)
- **Two Point Hospital / Theme Park:** customers pay per service (treatment fee, ride
  ticket, shop price); staff salaries come out of one balance. The player sets prices and
  builds. Revenue model (a). Sink: salaries + upkeep leave the loop.
- **Tropico / Anno:** citizens pay rent, food and taxes into the treasury; the state pays
  wages and upkeep of public buildings. Clean split: private goods are bought by citizens,
  public works by the state. Treasury model (b).
- **Dungeon Keeper:** payday pulls gold from the treasury to every creature; a creature
  then gambles in the casino and the gold flows back to the treasury. Unpaid creatures
  sulk and leave. The visible recirculation is the charm.
- **Majesty:** the player never commands heroes; the player posts gold bounty flags.
  Heroes earn by killing, spend at the player's shops (potions, weapon upgrades they then
  visibly carry), and tax collectors walk to shops and carry gold back to the castle.
  Bounty model (c) + walking tax. Closest genre match: defense + autonomous agents + gold.
- **Dwarf Fortress (0.31):** dwarves had wages, rent and shops; it was disabled because
  it added bookkeeping with no player decision. Warning case for a closed loop.
- **RimWorld / Banished / Settlers / Oxygen Not Included:** no wages at all. Goods flow
  by need; rooms and items raise mood (RimWorld room impressiveness). Shows that the fun
  is in the goods and their visible use, not in the money.
- **The Sims / Animal Crossing:** money buys furniture that the owner places at home and
  is seen using; villagers display their stuff. Basis for ask 2.

### 4. Fit facts (main @ c516194a)
- Faucet today: a killed wild drops `WILD_GEM_DROP` = 1 gem (wild_drop_service.gd:15);
  the bank grows a flat gem per 20 banker ticks (bank.gd). Nothing else creates gems.
- Sinks today: none. Gems move world -> station stack -> worker pouch -> seller pouch;
  a knockdown spills them back on the ground (creature.gd:1349, station.gd:122).
- A PAY job already exists: a payer takes vault gems at the till to a station that is
  `due` (bank.gd:37, station.gd:102-104). So shape (b) is half built.
- `Creature.buy` moves pouch to seller pouch and makes onlookers aspire (creature.gd:1054).

### 5. Ask 1: three whole-economy shapes

#### S1. Customers pay the stack (revenue + public works) [rank 1]
- **Rule:** a buyer's gem lands on the seller station's wage stack, not in the clerk's
  pouch; the worker takes it as its next shift gem. A station that uses up stock pays its
  maker (the decided tip becomes the price of the stock). Anything the PLAYER orders (a
  build site crate, a defense, a med kit, the guard post) is a public good: the player's
  thrown gem pays it, as today.
- **Player's role and levers:** the state. Levers: which public works to fund; a thrown
  gem on any private station = a subsidy that opens it before customers come (seeding);
  and picking up wild gems and choosing where they land (a station, the bank, a creature).
- **Money in:** wild drops (combat), bank growth. **Out:** none by default; proposed sink:
  a wild that reaches a creature knocks gems out of its pouch (it spills, wilds scoop
  some). Ties the sink to the wave, natural on sight.
- **What the player SEES:** a tipsy creature waddles to the bar, drops a gem on the 💎
  sign, the bartender grabs it and the sign's clock refills; later the bartender walks to
  the farm and drops a gem for the crops it used up.
- **Failure modes:** deflation in a calm stretch (no kills, gems pile in pouches, private
  stations close: the loop stalls at its least-wanted station); hoarding by a saver (a
  frugal temperament never spends); runaway at one popular station (bar soaks up gems,
  farms starve). Remedies: the player's subsidy throw; spill-on-hit sink; a full pouch
  pulls to spending harder (want already scales with spendable).
- **Productivity before a wave:** production that feeds leisure pays itself; the player's
  gems go only to the wave-critical public works (builds, defenses, med kits). Fewer
  throws, each one a real choice. Matches Tropico/Anno's split.

#### S2. The vault and the payers (treasury + recirculation) [rank 2]
- **Rule:** every gem the player throws, and every gem a seller earns above its wage,
  goes to the bank vault; payers (existing PAY job) carry vault gems to due stations in a
  priority order. A seller station's takings are collected by the payer on its round
  (Majesty's tax collector, Dungeon Keeper's casino return).
- **Player's role and levers:** the treasurer. Lever: a gem thrown onto a station is a
  flag "pay this first", not its pay; the bank is the one place the player feeds.
- **Money in:** wild drops thrown into the bank, bank growth. **Out:** none; proposed
  sink: a wild raid on the bank (theft already exists for brewers).
- **What the player SEES:** a payer with a satchel trots from the till to the kitchen,
  drops a gem on its sign, trots to the bar, picks up its takings, trots back.
- **Failure modes:** one payer is a bottleneck (stations close in a row); the vault
  running dry closes everything at once (a cliff, no gradient); the flag drifts toward a
  hidden priority list (menu-ish).
- **Productivity:** the player steers which stations run before a wave with one throw;
  creature spending refills the vault, so the player's throws shrink over time.
- **Cost of the frame:** creatures still do not pay the workplace directly; the user's
  ask "other creatures pay" is met only through the vault.

#### S3. Bounties at the gate (Majesty) [rank 3]
- **Rule:** the player never pays hours. The player sets gems as a bounty on a target (a
  wild kind, a wave, a log pile goal); whoever meets it gets the gems in its pouch.
  Every station is customer-funded as in S1; public works are paid by a "town" crate the
  herd's spenders chip into.
- **Player's role and levers:** the patron. Lever: what to reward; money enters the herd
  only where the player points it.
- **Money in:** bounties (from wild drops the player picked up). **Out:** none.
- **What the player SEES:** a gem pile on a flag by the gate; the fighter who downs the
  wild picks it up, then spends it at the bar.
- **Failure modes:** bounty = flat reward pile (bends the reward pillar); a goal on a log
  pile reads as a role purchase; public works stall when spenders are stingy.
- **Productivity:** weakest. The lever points at combat, not at the stations that
  produce before a wave.

Rank reasons: S1 meets the ask literally (creatures pay workplaces), keeps the player's
gem for what the player decides (public works), and has a clean binary (who ordered it
pays). S2 has the best lever but keeps the player as the payer by proxy. S3 moves the
lever away from productivity. A hybrid worth naming: S1 + S2's rule that a station's
surplus beyond a cap flows to the vault (cures the runaway bar).

### 6. Ask 2: what bought things become

#### F1. Home goods (The Sims, Animal Crossing, RimWorld rooms) [rank 1]
- **Rule:** a bought piece is the buyer's. It carries it home and sets it on a free cell
  of the room its bed is in; it uses it there (a lamp lights its room, a chair it sits on
  in free time). The piece shows a small owner mark; the player can still pick it up.
- **Player's role:** builds the rooms; creatures furnish them. Lever: room size and beds
  (a cramped room has no free cell, so the creature buys nothing more).
- **What the player SEES:** a creature waddles from the shop with a lamp over its head,
  plonks it by its bed, and that evening reads under it.
- **Failure modes:** clutter on the player's grid (limit to its own room cells); an owned
  piece a stranger uses (owner first, others when free); no bed = nowhere to put it (it
  keeps it in the pouch-like hold, or does not buy).
- **Productivity:** room mood -> mood -> drive (work pace) is already a chain; furniture
  is the gem's way back into how much a creature works. A gem sink if pieces wear out
  (a lamp burns out after N nights, so demand renews).

#### F2. Worn and carried gear (Majesty heroes, DF equipment) [rank 2]
- **Rule:** a bought item is worn or held: a head lamp, a scarf, a mug, a better axe. It
  shows on the body and gives a NEW RULE, not a flat bonus: a head lamp lets its wearer
  work after dark, a scarf lets it work in rain, a mug lets it drink without the bar.
- **What the player SEES:** at night one chopper with a glowing head lamp keeps chopping
  while the rest sleep.
- **Failure modes:** a flat bonus in disguise (+pace axe) breaks the reward pillar; a
  tool that only fits one job reads as a role purchase (the tool must fit the job the
  creature already holds, never grant one); per-unit tracking of who has what.
- **Productivity:** strongest direct link (night shift before a dawn wave), but riskier on
  the pillars. Could pair with F1: home goods for mood, one worn item for a rule.

### 7. Assumptions to check (code cannot settle the starred ones)
- [ ] * Is a build site crate / defense a "public good" the player pays (S1 split)?
- [ ] * Does a sink belong in the game (pouch spill on wild hit, wear-out)?
- [x] A payer job carries vault gems to due stations (bank.gd:37, station.gd:102).
- [x] No gem sink exists today (only spills back to the ground).
- [ ] Do rooms expose free cells per bed's room for F1 placement (LAW_rooms)? Not read.

## Raw: diverger_b

## Diverger B: lead from the code (who funds workplaces)

**Frame:** today a creature's spending is a dead end. Gems flow player -> station -> worker
pouch -> another pouch, and never back into any station. Smallest fix: a buy pays the
seller's *station stack*, not the seller's pouch. The seller then gets it back as its next
shift wage (that path exists). The player funds production; the herd funds service.

### Abstract problem (no game nouns)
Agents earn tokens only from funds the controller fills. Agents spend tokens on each other,
but spending refills no fund, so the controller pays every fund forever and agent savings
pool up dead. Needed: (1) a return edge from agent spending into funds, (2) a choice of which
funds the controller still fills (its lever), (3) a drain so idle savings don't stall.
Abstract answers: point-of-sale revenue (spending refills the seller's fund); a pooled
treasury redistributed by a rule; or a new outside source so agents earn without the
controller, who then only builds.

### The gem graph today (main @ c516194a)
Sources (mint): a wild that dies drops a gem on the ground (wild_drop_service.gd:15); a
banker grows a vault +1 gem per 20 labor ticks while it holds any (bank.gd:93-103).
Sink (destroyed): only the player's build cost (build_hand.gd:68, blueprint gem cost).
Holders and edges, all conserving:
- ground -> player pickup -> throw -> station stack (Station.pay_with, station.gd:196) or vault.
- vault -> payer's bag at the Till, only while some station is due (till.gd:10) -> nearest
  due station, else back to a vault (_deliver_carry, creature.gd:1167-1180).
- station stack -> worker pouch at punch-in, 1 gem = 60 s shift (_fetch_gem creature.gd:1212,
  Wage.start_shift wage.gd:29).
- pouch -> pouch: Creature.buy (creature.gd:1052), used only by the bar today (bar.gd:196),
  drinker pays the bartender's pouch. Bar is an OfferPlace with no wage (bar.gd:2).
- vault -> thief pouch as loot (_rob creature.gd:1324); loot -> cop's bag (:1337) -> the
  same _deliver_carry -> a due station. **The police path is already a pouch -> station edge.**
- pouch -> ground on death or drop (_spill_pouch :1349); station stack -> ground on knockdown.
Finding: every edge *into* a pouch exists; the only edges *out* to a station are theft+cop
and death. Spending never reaches a station. That is the whole missing structure.

### Prior art
- **Two Point Hospital, Theme Park:** a customer pays at the room or stall; staff salaries
  are paid from the till. Revenue lands where the service happened.
- **Majesty:** heroes earn, then spend gold at the player's market and inn; a tax collector
  walks it back to the treasury. The return is a separate visible walker.
- **Tropico, Anno:** citizens pay for services and taxes into one treasury; the player funds
  buildings from it. A pooled fund, the player allocates.
- **The Sims:** buy mode places owned objects in the home; the owner uses them on screen,
  they break and need repair (a demand that repeats).
- **Settlers, Banished, ONI, RimWorld:** no internal money; goods are the flow. Lesson:
  the binding limit should be stock, not cash. **Dwarf Fortress 0.31:** coin economy cut for
  hoarding. Lesson: every pile needs a drain.

### Ask 1: three whole-economy shapes

#### A. Takings to the till (point of sale) ... rank 1
- **Change:** Creature.buy pays `Jobs.station_of(seller).pay(price)` instead of
  `seller.pouch += price`. The gem lands on the counter's stack ("💎 2" on its sign); the
  worker takes it at its next punch-in as its wage. No new job, no new holder. Once bar,
  kitchen, chalkboard, shop and crate are Stations (decided), each sale funds its own hours.
- **Bootstrap for free:** Station.paid() is true while a gem waits (station.gd:94). A
  customer's gem on a closed counter opens the job, so the bartender walks in. A customer can
  open a place; the player never has to seed it.
- **Player's role and levers:** fund the base. Workplaces with no customers (woodpile,
  farm basket, lab, med kit, police box) still take thrown gems; service places live off
  sales. Levers: which producers to pay, what to build, and keeping stock flowing.
- **Money in / out:** in = player throws + bank growth + wild drops; out = build cost only.
  The tip (decided) moves service gems back to makers' pouches, who spend at service places.
- **Seen:** Pip sits at the bar, drops 💎 on the counter, sign goes "💎 1"; Bo the bartender
  (idle, nearby) puts on the apron, walks over, picks it up (💎 over Bo), pours.
- **Failure modes:** saturation: no sink inside the herd, so service stacks may pile up
  paid ahead (allowed by the pay-ahead pillar). Then the limit moves to stock: no crops, no
  drinks, however rich the bar. That is the wanted shape (Settlers' lesson). Hoarding: a
  creature with no wants holds gems forever (drain = shape B, later). Deflation: a herd with
  few producers earns little, sells little; the player's throw at producers fixes it.
  Runaway: none, gems are conserved.
- **Before a wave:** the player's gems go only to production (logs, crops, meds); fun,
  meals and training keep themselves open from the herd's own spending, so the player's
  attention goes to defense prep. Tuition funds the chalkboard, so more creatures cross INT
  gates and take jobs.
- **Open:** a sale when the seller has no station (an unhatted friend selling?) falls back
  to the pouch, or is refused. Assumption to verify: no buy today has a stationless seller.

#### B. The herd banks its savings (pooled treasury) ... rank 2
- **Change:** a creature with spare gems (pouch above a want's price) walks to the bank in
  free time and drops them in the vault (the vault already takes gems, bank.gd:66). The
  existing payer then carries vault gems to due stations (till.gd). Composes with A as the
  drain for hoarders.
- **Player's role:** banker-mayor. Levers: where the bank stands (the payer feeds the
  nearest due station, so placement picks who is funded), throws to override.
- **Money in / out:** in = savings + flat bank growth; out = payer to stations, theft.
- **Seen:** at dusk three workers queue at the bank, 💎 pops into the vault, "💰 9";
  next morning the purse-cap payer trots a gem to the farm.
- **Failure modes:** the herd, not the player, picks which stations open (bends the gem
  pre-pillar); bank growth on herd savings is a mint the player didn't earn (linear, capped
  by banker labor); a fat vault draws thieves (good tension, already wired to police).
- **Before a wave:** savings auto-fund whatever is due nearest the bank; less steering.

#### C. Bounty pay (the wave is the source) ... rank 3
- **Change:** a wild's gem drop goes into the pouch of the creature that landed the kill
  (picked up on screen) instead of lying for the player. Needs A for the return edge.
- **Player's role:** builder and general only; the player's gems come from its own kills.
  Levers: where fighters stand, what to build.
- **Money in / out:** in = kills; out = build cost. The herd's income tracks defense.
- **Seen:** Rex flattens a wild, scoops the 💎, swaggers to the bar.
- **Failure modes:** no wave, no income (deflation between waves); a strong herd snowballs;
  removes the player's throw lever (bends the gem pre-pillar hard); fighters richer than
  makers may read as paying for a role.
- **Before a wave:** last wave's kills fund this wave's service places. Ties defense to
  economy, but the player loses the pre-wave lever.

**Rank:** A (one call redirected, matches the cop path, keeps the player's throw for
production) > B (good later drain for hoarders, costs player choice) > C (new source, kills
the lever). A + B can stack; C cannot without reopening the gem pre-pillar.

### Ask 2: owning and using what they buy

#### X. Belongings at home ... rank 1
- A bought piece (the 18f lamp first) is carried home on the head (the carry glyph exists,
  creature.gd:1037) and set on a free cell in its bed's room (beds have one owner, LAW_beds.md).
  It is a GridObject the owner uses in free time: under its lamp it reads at night, on its
  own chair it sits. Room mood (PR 17, pick 34: lift split by beds) carries the effect.
- Sacrifice through occupied state: the piece takes room cells that another bed or a path
  needed. Natural on sight: a lamp by a bed is used by whoever sleeps there.
- **Seen:** Mo walks home with a lamp on its head, sets it by its bed; at night Mo sits in
  the lamplight with a book.
- **Failure modes:** clutter blocks paths (PR 39 push-out exists); a bed reassigned leaves
  the piece ownerless (it becomes the room's); the lamp lit cap (8, lamp.gd:9).

#### Y. Worn and carried items ... rank 2
- A bought item sits on the body, beside the job hat: sunglasses, a scarf, a ball it kicks
  around in free time. Each gives a small new rule on that creature, never a flat bonus
  (sunglasses: no dawn squint; ball: invites a play chat). It wears out, so the want repeats
  (the Sims breakage): steady demand keeps gems moving under A.
- **Seen:** Pip struts out of the shop in pink shades, kicks a ball to Bo, they chat.
- **Failure modes:** a body item read as a role (hat slot confusion); per-creature effect
  tracking; new nouns instead of connections.

**Rank:** X (adds links to rooms, beds, lamps, the grid) > Y (new nouns, hat clutter).

### Assumptions to verify
- [x] Bar is not a Station today; its sales go pouch to pouch (bar.gd:2, :196).
- [x] A gem waiting on a stack opens the station's job (station.gd:94, job_board.gd:215-222).
- [x] The cop's loot already goes to a due station (creature.gd:1337 -> :1167-1180).
- [x] The only gem destroyed is the player's build cost.
- [ ] Every buy's seller holds a station once 18d/18f land (else A needs a fallback).
- [ ] A customer's gem on a closed counter pulls an idle worker fast enough to serve it.

## Raw: diverger_c

## Diverger C: the player's moment + owned goods (asks 1 and 2)

Frame: the player stops paying for the work its herd consumes and pays only for the work
that faces the wave. Everything the herd buys for itself funds itself, and the goods it buys
stay in the world as things you can see, bump into, and see smashed.

### Abstract problem (no game nouns)
One outside source mints value (the player, who harvests it from attackers). Today it funds
every producer's operating time directly. Agents also hold value and pay each other for
services, so a service is now paid twice (source + customer). Ask 1: move the funding of
customer-facing producers from the source to their customers, and give the source a lever
that is not "fund everything". The loop among agents conserves value, so it needs one
visible inflow and at least one visible outflow, or it hoards (inflow, no outflow) or
stalls (no inflow to a sub-loop: no customers, no wages, no customers).

### Abstract solution
Whoever consumes a producer's output funds it: agents fund what agents consume, the source
funds what serves its goal (defense, building, raw stock). The source's lever becomes
where inflow enters plus kickstarting a stalled sub-loop. Outflow: goods attackers destroy
and pouches spilled on knockdown, so the wave is the economy's drain.

### Prior art
- Majesty (Cyberlore 2000): the closest match. The king never pays heroes a wage; he posts
  gold bounties, heroes spend their gold at his shops (blacksmith, marketplace), and a tax
  collector walks the shops and carries gold back to the castle, killable on the way. The
  player's lever is where gold enters (bounties) and what to build; circulation is visible
  and raidable.
- Tropico / Anno: ruler pays wages or upkeep, residents pay fees back; money is a number,
  not a carried thing (the part not to copy).
- RollerCoaster Tycoon: guests wear or carry bought hats, balloons, umbrellas: a walking sign.
- The Sims / Animal Crossing / Tomodachi Life: bought or gifted furniture lands in the
  owner's house and is used on screen; worn clothes show who owns what.
- Dwarf Fortress (0.31 to 0.34 economy, later disabled): dwarves paid rent and bought goods
  with coins; it broke from hoarding and coins piling with no sink. The lesson: a
  conserved loop needs a drain. DF's claimed items and room value (RimWorld's room
  impressiveness, ONI's decor) show ownership read as a room's worth, a mood input.
- Settlers II / Banished: no wages; the lever is placement and routes (goods walk roads).

### Facts from the code (main @ c516194a)
- Wage stacks gems, no cap; the worker takes 1 per 60 s shift into its pouch (wage.gd,
  station.gd punch_in). A bank payer already carries vault gems to `due` stations (till.gd).
- The drinker pays the bartender directly (bar.gd:196, creature.buy). Lamp shop, tuition,
  tips are in round branches, not main.
- Inflow: wild drops the player picks up, bank growth (minted). Outflow: player build gem
  costs only; a creature has no sink but a knockdown spill (_spill_pouch) and cop'd loot.
- drive() = discipline + mood lean: mood is work pace. Room furniture mood is R1's PR 34.

### Ask 1: three whole-economy shapes

#### A. "The till is the wage" (customers fill the sign). Rank 1.
Rule: a purchase price lands on the selling station's wage stack, the same stack a player's
thrown gem lands on; the worker still takes 1 gem per shift from it. One pool, two
fillers. The player pays only stations no creature buys from (woodpile, farm, guard
posts, builders, the bank's payer route), and may still throw onto any sign to kickstart it.
- Player levers: which producers to fund (the wave-facing ones), kickstart a dry shop,
  and placement (a bar next to the woodpile gets the choppers' gems on their break).
- Money in: player throws on producers + wild drops. Out: goods smashed in waves, pouches
  spilled on knockdown, which the player scoops up (see ask 2).
- Scene: the bar sign reads 💎 4 2:10. Three choppers on break each slap a gem on the
  counter, 💎 hops onto the sign: 💎 7. Across the yard the kitchen sign blinks 💎? because
  no one ate there all evening; the player lobs one gem on it and a chef waddles in.
- Failure: stall (no customers, so no shift, so no customers) is seen as a 💎? sign and
  fixed by one throw. Hoarding: a creature that never wishes keeps gems; the wave drains it.
  Runaway: a popular bar stacks without cap (fine: paid ahead is decided law).
- Productivity: every gem the player throws goes to work that faces the wave; the herd's
  comforts pay for themselves, so before a wave the player's hands are on defense.
- Note: this moves the drink price from bartender pouch to bar stack. The bartender still
  earns it, one shift per gem. Check against the decided "buyer pays the clerk" wording.

#### B. "Town purse" (Majesty's tax collector). Rank 2.
Rule: the bank's payer already carries vault gems to due stations; add the reverse walk.
A purchase price drops on the counter as a floating 💎 stack; a collector (the same payer
job, both directions) carries takings back to the vault. The player throws only into the
vault. Everything is paid from the one purse.
- Player levers: one deposit spot, and where banks stand (route length = how long a dry
  station waits; a second bank near the bar row).
- Money in: player deposit, bank growth. Out: brewers rob the vault (built), wilds bonk a
  walking payer and gems spray.
- Scene: a purse-capped payer trots a gem to the gym while another trudges back from the
  bar with 3 gems over its head; a wild clobbers it, gems fly like a piñata, a brewer
  sneaks to grab one, a cop chases.
- Failure: the purse empties and every station starves at once (one point of failure);
  bank growth is a mint with no matching drain, so inflation in long runs.
- Productivity: one pre-wave throw; risk is route exposure. Weakness: the player still
  funds the bar via the vault, so it answers "less clicking", not ask 1.

#### C. "Patrons" (creatures throw on signs themselves). Rank 3.
Rule: a creature with gems whose wished place is closed walks to its sign and throws a
gem on it, the player's own verb. Purchases go to the worker as today. Lever: the player
funds what it wants, the herd funds what it wants. Money in/out as today.
- Scene: Pip, thirsty, lobs a gem at the dark bar's sign, misses, bonks the bartender awake.
- Failure: two payers per sign, so the player cannot tell if a sign needs it (interface
  legibility fails). Productivity weak: the herd funds the bar while the woodpile sits dry.

### Ask 2: two shapes for owned goods

#### D. "Stuff comes home" (the buyer carries it home and places it). Rank 1.
Rule: a bought piece is a real grid object. The buyer carries it overhead (a lamp, a chair,
a rug) to the room of its own bed and sets it on a free floor cell beside the bed, the way
a worker sets a stack on a station. A bought wearable goes on its face or neck, never the
head (head = job hat = role sign): a mustache, a monocle, a bow tie, a balloon.
- Use on screen: owned pieces keep their normal rule (a lamp lights the room at night, a
  chair is a seat its owner sits in first). The owner uses them in free time; a close one
  (bed sharer) may too.
- Player's role and lever: builds the rooms. A 1-bed hut has floor for stuff; a bunkhouse
  has none, so the buyer comes home and stands there holding the lamp, ? over it
  (sign: no floor). This is the shared-space sacrifice the "care should beat bunkhouses"
  balance task wants: room floor goes to beds or to stuff.
- Money out (the drain A needs): a wave that breaks a room yeets its stuff; smashed pieces
  are gone and their owners want them again. A knocked-down wearer drops its mustache.
- Scene: Mo carries a lamp home over its head, wobbling; it plops it by its bed; at night
  the hut glows and Mo reads under it. Next wave a wild punches the wall in, the lamp
  flies out the hole and shatters; Mo wails, then marches back to the shop.
- Failure: clutter blocks paths (place only on cells beside its bed, max a few per owner);
  lamp light cap (MAX_LIT 8: bought lamps light only free slots, round R1's rule).
- Productivity: owned pieces lift room mood, mood lifts drive, drive is work pace. The
  wave drain keeps demand alive so gems keep circling to makers.

#### E. "Claim, not place" (the player places, the creature buys its name on it). Rank 2.
Rule: the player places all furniture. A creature buys a placed, unclaimed piece from the
clerk; its name tag and colour appear on it; it uses it first. Wearables hang on a rack the
player places; a buyer takes one and wears it (the weapon pickup pattern).
- Lever: every placement stays the player's (a chair by the workshop keeps its owner near
  work). Money out: same wave drain as D.
- Scene: the player drops 3 chairs in the bar; Pip buys the middle one, 🏷 Pip pops on it,
  and Pip shoos a hatchling off it with a goofy huff.
- Failure: build cost plus clerk price reads as a double charge; claims strand others.
  "Place furniture in their house" (ask 2's words) is not the creature's act here.

### Ranking and why
Ask 1: A > B > C. A answers the ask literally (the customers pay), keeps one pool and one
verb, and leaves the player's gems on wave-facing work. B is a good later layer (it runs
already one way) but keeps the player as the bar's real payer. C blurs who pays a sign.
Ask 2: D > E. D is the ask in its own words, gives the economy its drain (waves smash
stuff), and creates the room-floor sacrifice the care-vs-bunkhouse task needs. E keeps
layout with the player but double-charges and drops the creature's own act.
Best pair: A + D: work a funded producer, spend at a customer-funded shop, tip the maker,
carry the piece home, the wave smashes it, buy again.

### Pre-pillars (unconfirmed)
- PRE-PILLAR (unconfirmed): whoever consumes a station's output pays its hours; the player
  pays only for output the herd does not consume.
- PRE-PILLAR (unconfirmed): a bought thing stays visible in the world (placed, worn, or
  carried) and can be lost in a wave; a gem never vanishes into a number.

### Open questions for the user
1. A: purchase onto the station's sign (A needs it) or straight to the worker (bar today)?
2. D: may a creature place an object itself, or must every placed object be the player's (E)?
3. Wearables on face and neck only (mustache, monocle, bow tie), head kept for job hats?
4. Is "waves smash owned stuff" slapstick loss, or too grim for a creature's own lamp?

## Raw: auditor

## Essence auditor: who pays workplaces (ask 1) + owned goods (ask 2)

Frame: all three divergers converge. Ask 1 has one real shape (a buyer's gem lands on the
seller's workplace sign) plus two layers that are drains or variants, not rivals. Ask 2 has
one real shape (the piece goes home) plus wearables as a second axis. The open questions are
not "which shape" but three pillar edits and one missing sink.

### Code facts checked (main @ c516194a)
- Correct: bar.gd:2 `extends OfferPlace` (not a Station); bar.gd:196 drinker `c.buy(DRINK_PRICE,
  _bartender)`; creature.gd:1054-1066 `buy` moves pouch to seller pouch, needs a FRIENDLY seller
  on its feet, spends only `spendable()` = pouch - loot (:1079), arms aspire on onlookers.
- creature.gd:1212-1220 `_fetch_gem`: punch-in gives the worker 1 gem into its pouch.
- wage.gd:26-40: stack has no cap; 1 gem = one GEM_SEC (60 s) shift; refund on knockdown
  returns the stack, the running shift's gem stays the worker's (:48-53).
- bank.gd:37 posts the Till as PAY; till.gd:10-13 hands the payer a vault gem only while
  `Station.due_near` finds a due station; creature.gd:1169-1192 `_deliver_carry` pays the
  nearest due station, else back to a vault. Cop loot joins that path (creature.gd:1336-1343).
- station.gd:196 `pay_with` = a landed player throw. Line fixes: `paid()` is :85 (not :94),
  `due()` :103-104, bank growth :99-108 (not :93-103), `buy` :1054 (not :1052).
- Sinks: the only gem destroyed is the player's build cost (build_hand.gd:68). Mint: wild
  drop 1 (wild_drop_service.gd:15) + bank growth 1 per 20 banker ticks while vault > 0.

### Contradictions the divergers missed
1. **B's "a customer's gem opens a closed counter" is false as specced.** `buy` needs a seller
   present (creature.gd:1055); a closed bar has no bartender. Pay-at-serve cannot open a closed
   place. Only a prepay (C's "Patron": the creature drops a gem on the sign first) can. So the
   Patron is not a rival shape, it is the bootstrap Point-of-sale needs, or the player keeps it.
2. **The payer never opens anything.** `due()` = a shift running with an empty stack
   (station.gd:103). Every "vault funds stations" shape only extends running ones.
3. **Price vs shift rate makes signs a dead pile.** A busy bar takes 1 gem per drink but burns
   1 gem per 60 s. Customer gems pile on the sign, out of circulation, while pouches drain.
   "Paid ahead without limit (user)" was set for player throws; for customer gems it becomes
   the "Frictionless hoarding" antipattern. Needs an outflow (overflow to vault, or the
   payer collects surplus) or a user call.
4. **"The wave is the drain" (C) is not a gem sink.** A knockdown spill goes to the ground,
   then to the player's hand: a transfer back to the faucet. Smashed goods renew demand but
   destroy no gems. The real sink stays the build cost.
5. **Owned piece "by its bed" drifts.** Bed owners are reassigned on change (LAW_beds.md:49);
   ownership of a piece must sit on the creature, not on the bed.

### Ask 1 essences and merges
- **P1 Point of sale** (A-S1, B-A, C-A, + C-C Patron as its bootstrap): a buyer's gem lands
  on the selling workplace's sign; the worker gets it as its next shift's wage; the player
  pays only workplaces no creature buys from, and may kickstart any sign.
- **P2 Pooled purse** (A-S2, B-B, C-B): gems pool in a vault and walkers carry them out (and,
  in C, takings back). Essence: a drain/router, not a funder. Survives only as P1's outflow.
- **P3 Bounty** (A-S3, B-C): kills pay creatures directly. Cut (pillars below).

### Ask 2 essences and merges
- **G1 Goes home** (A-F1, B-X, C-D): a bought piece is a grid object the buyer carries to its
  bed's room, sets on a free cell, and uses there; others close to it may use it too.
- **G2 Worn** (A-F2, B-Y, C-D wearables): a bought item shows on the body (face/neck, the
  head is the job hat) and gives a new rule. Second axis; composes with G1.
- **G3 Claim, not place** (C-E): cut on literal fidelity, ask 2 says "they can place
  furniture in their house". Raise only as a question.

### Extremes
| Variable | P1 Point of sale | P2 Purse alone | P3 Bounty |
|---|---|---|---|
| Herd gems 0 | service signs show 💎?; producers run on player throws, wages refill pouches | vault 0 = every station starves at once (cliff) | no kills between waves = no income |
| Herd gems huge | every service sign paid far ahead; gem no longer changes how much anyone works; limit moves to stock | herd interest from bank growth = inflation | fighters snowball |
| Player throws 0 | producers close, herd gems drain into service signs, loop stalls: lever is real | payer still refills running stations from deposits: passive nearly wins | herd self-funds: lever dead, decision fake |
| Station with no customers | 💎? until one player throw or one Patron drop | never opens (contradiction 2) | n/a |
Ask 2: huge gems = every room full of stuff, so cap by free cells beside the bed (C's rule);
0 gems or a closed shop = nothing to place, no stake lost. Rows differ: both axes earn a place.

### Pillar test (survivors P1, P2-as-drain, G1, G2)
- **PRE "a gem pays a workplace's open hours":** P1 keeps "a gem pays hours" but bends "the gem
  only decides which workplaces stand open" from the player's call to the herd's for service
  places, and bends "paid ahead without limit" (contradiction 3). P3 breaks it (the player's
  throw is gone).
- **"A creature holds gems... a gem keeps passing creature to creature":** P1 bends it, the gem
  now passes through a sign and reaches whoever punches in next, not the server who poured.
  Tips stay direct (decided). P2 bends it harder (a pool between creatures).
- **"Roles emerge from raising":** P1 safe if `buy` still arms aspire. P3 bends it (combat pays,
  so the gem steers at-what). G2 breaks it if an item grants a job or fits only one job; safe
  if the rule is job-free (sunglasses, scarf) or only extends the job it already holds.
- **"A reward is a new rule, never a pile":** P3 bounty is a pile: break. G1's lamp lights a room
  (a rule); its mood lift is a scale chain (piece -> mood -> drive): mild bend of "never one piece
  scaling another"; legal only if the lift is seen (lamplight, owner sitting there).
- **"Sacrifice through occupied shared state":** G1 fits it best of all: room floor goes to beds
  or to stuff (the bunkhouse-vs-care stake).
- **Natural on sight / tone:** P1 slap a gem on the counter: yes. Patron lobbing a gem at a dark
  sign: yes, goofy. P2 payer piñata: yes. G1 lamp on its head home: yes. G2 mustache/monocle:
  strong tone fit (title of the game).
- **Black box interface:** P1 sign has two fillers but one readout (💎 n m:ss); legible. C's
  objection to Patron ("can't tell who paid") applies to P1 equally and fails for both: the sign
  reports state, not source. P2's priority order is hidden: bends it, risks menu-ish.
- **Add connections, not things:** P1, G1 add links only. G2 adds nouns (items). P2 reuses.
- **Frictionless hoarding (antipattern):** P1 without an outflow trips it (contradiction 3);
  a creature that never buys trips it per pouch. Remedy is a judgment call for the user.
- **Decision beats passive:** P1 passes (throws 0 stalls); P2 alone fails; P3 fails.

### Survivors
- Ask 1: **P1 Point of sale with Patron prepay as bootstrap**, plus **P2's surplus walk as the
  drain** for over-full signs. P3 cut.
- Ask 2: **G1 Goes home** first, **G2 Worn** (face/neck, job-free rule) as second axis. G3 cut.

### Pillar rewordings the user must confirm
1. PRE gem pillar: "A gem pays a workplace's open hours, whoever drops it on the sign: a
   customer pays for what the herd buys, the player for what it does not. Never a role..."
   plus a call: does "paid ahead without limit" hold for customer gems, or does surplus flow on?
2. Gems pillar: "...spends them where another creature serves it; the gem reaches the server as
   its next shift's wage (a tip passes hand to hand)." Or keep direct pay and drop P1.
3. New PRE-PILLAR (C): "A bought thing stays visible in the world (placed or worn) and can be
   lost in a wave." Open: is a smashed own lamp slapstick or grim (tone gate)?
4. Gem sink: confirm the build cost is the only drain, or name a second one (a decision, not
   a code fact).

## Raw: challenger

## Challenger: attack "the till is the wage" + "stuff comes home"

Verdict up front: the shared pick has one critical flaw in the code's own units (F1), costs the
player the lever that steers labor before a wave (F3), and may answer a question the user did
not ask (Frame). Strongest alternative: the player keeps paying hours, creatures pay for goods
(Alt-1). Strongest backtrack: "every paid place is a full Station with wages" (B1).

### Code facts the divergers did not weigh (main @ c516194a)
- A stack gem buys 60 s of shift and a worker takes one only at punch-in
  (wage.gd:6 GEM_SEC 60, wage.gd:30-38 start_shift; creature.gd:1211-1218 _fetch_gem).
- A bartender serves one drink per labor tick, interval 3 s (creature_config.gd:231-236,
  bar.gd:192-199); price 1 gem (creature_config.gd:158); one crop makes one drink (bar.gd:79-80).
- So a busy bar takes in up to about 20 gems a minute and pays out 1 a minute.
- A closed station frees its worker's hat for another job (job_board.gd:203-206, :215-221).
- Today the bartender and the teacher are UNPAID jobs (creature_config.gd:231, "TEACH ... unpaid,
  like the bartender"): the player pays nothing for comforts now. The Station decision made the bill.
- A knocked-down station spills its whole stack to the ground (station.gd:122-126, wage.gd:48-52);
  a knocked-down creature spills its pouch (creature.gd:1343-1352). Both land where the player
  scoops them: a herd-to-player drain already exists. Diverger B's "out = build cost only" misses it.

### Failure scenarios
F1. Gems pool on service signs (CRITICAL). Under "till is the wage", every drink adds 1 gem to the
bar's stack but the bartender withdraws 1 per 60 s. A lively evening parks 10-20 gems on the bar
sign per minute. Those gems leave circulation: pouches empty, tuition and lamp buys stall, the
aspire-to-study chain (creature.gd:1063-1066) dies. The bar shows "💎 140" and the farm is broke.
"Paid ahead without limit" makes this legal, which is why no one flagged it.
Fix: a sale lands on the sign only while the station is due or dry (Station.due(), station.gd:102);
otherwise it goes to the clerk's pouch (today's path, bar.gd:196). The stack holds at most the next
shift from customers; the rest stays circulating.

F2. The tip leaves the server permanently in debt (HIGH). Price 1 per drink, tip 1 per crop used,
1 crop per drink: the bartender's margin is zero even when it pockets every sale. Under pure F1
pooling it earns 1 a minute while owing up to 20: debt grows without bound, makers never get paid,
and "pays at the next meeting" becomes a ledger of who owes whom (per-unit tracking antipattern).
Fix: price above the stock tip (drink 2, crop tip 1), or the tip drops on the stock pile the crop
came from (the basket stack) at pickup, no meeting and no debt record.

F3. The player loses the labor lever (HIGH, hits "productivity first"). Today an unpaid sign closes
the station, the worker's hat comes off, and a smart creature drifts to research or the woodpile.
Under customer funding the bar reopens itself every time a drinker drops a gem, so an INT 8
creature stays a bartender through the pre-wave rush. The only off switch is picking the bar up.
Fix: the player's throw stays the open switch (Alt-1), or a sale opens a station only while the
player has paid it at least once this day (customers keep it alive, the player decides it exists).

F4. Bad-wave spiral (MEDIUM). A wave knocks down the bar (stack spills) and several creatures
(pouches spill). The player scoops the gems. Now the bar is dry and the herd is broke, so no one
reopens it, mood sags exactly when the herd needs recovery, drive drops. Recovery needs the player
to throw on the bar: the comfort bill the redesign promised to remove comes back at the worst time.
Fix: accept it as the lever (fund mood or fund defense after a wave) and say so to the user; or
spilled stack gems land on the sign's own cell and re-pay it when no one scoops them.

F5. Hoarding with nothing to buy (MEDIUM, "frictionless hoarding" antipattern). Stuff-comes-home
caps buys by free cells beside the bed. A bunkhouse has none, so its sleepers stop buying and their
pouches grow forever. The more cramped the herd, the dead-er the shops. Wave-smash as the only sink
ties demand to losses the player tries to prevent.
Fix: a consumable sink that needs no floor (a meal, a drink, a lesson) is the base demand;
furniture is the luxury tier. Or wear-out by nights used (Diverger A's burnt-out lamp).

F6. Creature-placed clutter fights the player's grid (MEDIUM). A creature sets a lamp on the cell
the player planned a wall or a second bed; a reassigned or dead owner (LAW_beds, LAW_life) leaves an
ownerless piece. Each piece carries an owner: per-unit tracking.
Fix: only on cells inside the owner's room AND marked free by the player's build hand; ownerless
piece becomes the room's (Diverger B). Or Diverger C's E (player places, creature claims).

F7. Two fillers on one sign (LOW-MEDIUM, legibility). With customers and the player both filling
the stack, "💎?" no longer tells the player "this needs you"; a customer may refill it a second
later. Diverger C rejected its own shape C for exactly this, then kept it inside shape A.
Fix: different glyphs for customer gems and thrown gems, or Alt-1 (one filler per sign).

### Frame attack
The ask: "I forgot that the player already pays them, so we have to design how to manage things
that other creatures pay instead of the player having to pay them." All three read "them" as the
service stations' hours. Two other readings fit the words as well:
- R2: "things that other creatures pay" = the GOODS (lamp, meal, lesson, furniture) that the
  player would otherwise build or stock. Ask 2 backs this: creatures buying furniture for their
  house replaces the player placing and paying for it. Hours stay the player's.
- R3: "manage" = the player's interface over creature spending: what the player can steer once
  creatures pay (which places open, prices, where shops stand), not who pays.
The pre-pillar says "the gem only decides which workplaces stand open" (MEMORY.md:9-13). The
player throwing is that decision. Moving service hours to customers moves the decision to the herd.
That may be fine, but it is a pillar change, and the user must say so. Ask the user before building.

### Strongest alternative (under-ranked or missed)
Alt-1. "The player pays hours, creatures pay goods." The player's throw opens a place (lever kept,
F3 and F7 gone). A sale goes to the clerk's pouch (today's code, bar.gd:196) and the clerk's tip
goes to the maker; the price funds the goods chain, not the hours. What creatures pay "instead of
the player" is the stuff: room furniture, meals, lessons that the player no longer builds or
stocks. Answers R2 literally, keeps the money circulating in pouches (no F1), and needs no new edge.
Weakness: the player still pays the bar's hours; if the user meant R1, it misses.
Alt-2 (F1's fix promoted): "a customer keeps a dry place open, never banks it". Sale to the sign
only when due, else to the clerk. Meets R1 with bounded pooling. Best if the user confirms R1.

### Backtrack candidates in decisions made
B1. "Every paid place is a full Station with wages." The bar and chalkboard are unpaid today; this
decision is what created the double bill the user now wants removed. If service places stay
sale-funded OfferPlaces (clerk lives off sales, no hours), the problem disappears. Cost: two kinds
of workplace (paid vs. sale-funded); the user picked uniformity once, so ask, do not reopen alone.
B2. "Tip handed when the two MEET on screen." Pairwise debt is a ledger (per-unit tracking) and a
meeting between a bartender and a field farmer is rare, so debts pile; a dedicated walk costs
labor before a wave. A tip dropped on the source stock pile reads as clearly with no memory.

### Questions for the user (yes / no)
1. Does "instead of the player" mean the hours of service places (R1) or the goods (R2)?
2. Should the player still choose which service places stand open before a wave?
3. May a creature set an object on the grid by itself, or only claim one the player placed?
4. Is "a wave smashes my lamp" goofy loss or grim?
