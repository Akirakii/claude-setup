# BRAINSTORM: creature economy (PR 18)

User (2026-10-20): "create economy system to make creatures consumist and be willing to work
more if economy is well". Confirmed (user): a creature holds gems of its own (the gem pouch
pillar). Picks below marked (round) are this AFK round's, not the user's; each says how to
revert it.

## Frame
Gems already flow player -> station (a paid shift) and stop there. The economy is one new
hop: the shift's gem goes on into the worker's pouch, and the worker spends it where another
creature serves it, so the gem keeps moving creature to creature. "Work more" must never be a
role bought (pillar "Roles emerge from raising"). Measured below: the herd's work hours are
capped by how many creatures hold a job, not by how long each works a stretch, so "work
more" has to act on who takes a job (18i), not on the work stretch.

## Prior art
- **Majesty (Cyberlore, 2000):** heroes hold their own gold, earned from bounties, and spend
  it at the player's market, inn and blacksmith; a tax collector brings it back. The closest
  match: autonomous agents with purses, spending at player-placed buildings. Lesson kept:
  the buy is on screen at the building; the return to the player is a later, separate verb.
- **Dwarf Fortress 0.31 economy:** dwarves earned coin wages and paid rent and goods; it was
  switched off for hoarding and silly prices. Lesson: no rent on a basic need (a creature
  never pays to sleep or eat to survive), and a cap or a drain on every pile.
- **Tropico / Anno:** satisfying consumer wants raises output or unlocks tiers; wealth reads
  per citizen. Lesson: "the economy is well" is a per-creature state the player can read on
  the creature, not a hidden herd blob.
- **Habit formation (Duesenberry's ratchet, the Diderot effect):** having bought raises the
  want for more. This is the "consumist" half: the drive comes from buying, not from holding.
- Rejected from the field: **target-income earners** (a worker stops once its target is met):
  a broke creature would then work hardest, the opposite of the user's line.

## Candidates
Work drive (what "willing to work more" reads):
- **A. Taste: a fading memory of its paid buys adds to `drive()` (longer WORK, shorter
  BREAK).** Built in round 1, measured, **cut in round 2** (below).
- **B. Purse target:** drive up while its pouch is below the price of a wanted good. Cut:
  a broke herd with a shop would out-work a rich one (contradicts the user's line).
- **B'. Holding:** drive up with gems held. Prototyped in round 2 (min(pouch, 3) / 3): work
  hours 873 / 1035 / 854 against broke 1017 / 1098 / 838. No gain; not built.
- **C. Herd prosperity index:** gems moved per minute herd-wide lean everyone's drive. Cut:
  a herd-level blob erases per-unit clarity (rejected antipattern), and no creature shows it.
- **D. A price gate:** a broke creature is turned away, so fun and mood carry the effect.
  Deferred to 18b: it changes the care balance (the bar is a snap cure).
- **E. Participation, buyer studies (proposed, 18i):** a creature that has bought leans to the
  library. Cut in 18i: only workers and bartenders earn gems, and both clear INT 8 already, so
  it would only push them toward INT 12 jobs (what they work at, not how much).
- **E'. Aspiration, the demonstration effect (built, 18i, round's pick):** a friend below every
  job gate that sees another pay (any `Creature.buy`, within ASPIRE_RADIUS) aspires for
  ASPIRE_SEC: 💭💎 over it, and a library pulls it ASPIRE_GAIN harder, so it studies into a
  job. A broke herd never pays, so it never aspires; a creature past a gate never aspires, so a
  gem never picks what it works at. Field: Duesenberry's demonstration effect (seeing others
  consume raises one's own want); Anno's prosperity ladder (supplied wants lift residents into
  a skilled tier). Revert: ASPIRE_GAIN 0. Effect on hatted time: unmeasured (user, 2026-10-21:
  "forget balancing for AFK; feature-based and fast").
- **Rejected for 18i:** rested-more from buys (rest is ~9% of adult time: too small a cap);
  seating aspirers past their gate (a role from a purchase).

Where held gems live:
- **P1. One pouch, with its stolen part counted (picked, round):** `pouch` = every gem held;
  `loot` <= pouch = the stolen ones. A cop takes `loot`; only `loot` makes it wanted. Loot is
  never spent (round 3, from the pillar "stolen gems stay marked as stolen"): moving it into
  the seller's loot would mark an honest bartender as a thief, and spending it as plain gems
  would let a thief shed `wanted` by drinking.
- **Theft gate (round 3):** a puffing creature may rob while it holds wages; only loot of its
  own stops it (one haul at a time). The puffs, not the purse, drive a theft.
- **P2. Two holdings (purse + pouch).** Cut: two variables, one purpose (gems on a creature).
- **P3. Gems in the job bag.** Cut: the bag empties when a job ends; wrong lifecycle.

What it can buy (round): a gem in the pouch adds SPEND_GAIN to the bar's pull, so a creature
with a gem walks to spend it even with its fun full. Without it only 0-8 of 16-21 wages were
spent per 900 s run; with it 6-12 of 16-22.

## Data dictionary
| name | type, range | owner | definition | lifecycle |
|---|---|---|---|---|
| `pouch` | int >= 0 | creature, saved | gems it holds | +1 per shift's gem, +price per drink it serves, -price per drink it buys; spilled on death/combine |
| `loot` | int, 0..pouch | creature, saved (save VERSION 20) | the stolen part of `pouch` | +THEFT_GEMS per theft (a vault, or up to that from a friend's spendable gems); a cop or a jail takes it; never spent |
| `DRINK_PRICE` | int 1 | constant | gems a served drink costs its drinker, paid to the bartender | |
| `SPEND_GAIN` | 1.0 | constant | pull of a bar on a creature that can pay (beats roaming within 14 m) | |
| `_aspire` | Cooldown | creature, transient | it saw a friend pay while below every job gate | armed ASPIRE_SEC by a buy within ASPIRE_RADIUS; read only while still below the gates |
| `ASPIRE_GAIN` | 1.0 | constant | extra library (TRAIN) pull on an aspiring creature, the size of SPEND_GAIN | |
| `ASPIRE_SEC` | 120 s dilated | constant | how long the urge lasts | |
| `ASPIRE_RADIUS` | 8 m | constant | how far a paid buy is seen (a bar room and its doorway) | |
| `parcel` | bool | creature, saved (VERSION 21) | a bought lamp it carries home | set at the shop; cleared when set down, dropped or spilled |
| `room_pieces` | int >= 0 | creature, derived | furniture pieces in the room where it sleeps | each housing reassign |
| `FURNITURE_PRICE` | int 5 | constant | gems a shop piece costs, left on the counter | |
| `SHOP_GAIN` | 1.0 | constant | pull of a shop on a creature that can buy, the size of SPEND_GAIN | |
| `FURNISH_MAX` | int 2 | constant | furniture a room takes before its sleepers stop buying | |

## I/O pipeline
1. **Wage:** a worker with no shift under way picks up a station's gem (`_fetch_gem`):
   station gems -1, worker `pouch` +1. Shown: the 💎 emote (exists).
2. **Pull:** a gem in its pouch adds SPEND_GAIN to the bar's want (`OfferPlace.want`).
3. **Buy:** the bartender serves it (`Bar._serve`): DRINK_PRICE of its own gems moves to the
   bartender's pouch, 💎 over the bartender, only while the bartender is a friend on its feet
   (else no gem moves). A broke drinker is served free, as today.
4. **Police:** a thief's `loot` (not its earned gems) goes to the cop; `wanted()` reads `loot`.

Known gaps (cold review): the bartender cannot buy at its own bar, so its takings pile up in a
one-bar herd (18g); a ring station's shift gem goes to whoever punches in first.
Knock-down refund (round): only stacked gems come back; the running shift's gem is its
worker's wage (before: the shift's time left came back too, which would now mint a gem).

## Measured (care, 3 seeds x 900 s, SIM_WALL=0, SIM_WAGES=10 in every arm)
| arm | work_s per seed | shifts | wages | bought |
|---|---|---|---|---|
| rich, taste (round 1) | 1042 / 1053 / 842 | 22 / 20 / 16 | 22 / 20 / 16 | 12 / 11 / 8 |
| broke (SIM_BROKE=1) | 1017 / 1098 / 838 | 21 / 18 / 16 | 21 / 18 / 16 | 0 |
| broke, taste pinned at 1 for all | 1164 / 1115 / 913 | 22 / 21 / 17 | | 0 |
| rich, TASTE_SEC 3600 | 1019 / 1098 / 834 | 22 / 19 / 17 | | 12 / 12 / 6 |
Round 3, rebased on cf6a4b6c (PR 32), same seeds and settings:
| arm | work_s per seed | bought | hatted gem-holders at a leisure place (s) |
|---|---|---|---|
| broke (SIM_BROKE=1) | 931 / 994 / 921 (2846; seed 1 fell) | 0 | 0 |
| **shipped** | 978 / 1158 / 928 (3064) | 9 / 10 / 9 | 174 / 95 / 138 |
- Shipped >= broke on every seed. Round 2's shipped run (984 / 1036 / 685, -8%) was batch
  spread: the broke arm alone moved from 2953 to 2846 with main's change, and the statue
  falls in both arms.
- The spend pull is not gated further: a hatted worker only picks a leisure place in its
  BREAK phase (the WORK phase comes first in `_decide_mode` and pulls it off the seat), so
  the 174/95/138 s are break time. Gating it off for workers would leave no buyers: the
  workers hold the gems.
- The care herd holds ~2 jobs at a time (hatted 1700-1900 s per 900 s run) and runs ~20
  shifts per run whatever the pay: the jobs open, not the gems, cap the work.
- The lever alone, at full strength for every creature: +8% work hours (3192 vs 2953 summed),
  a hatted worker's WORK share 0.56-0.66 against 0.44-0.60.
- In the real economy the taste of workers at work was 0.03-0.12: the main worker is the
  bartender, who sells and cannot buy, and other workers spend few gems. Keen vs plain
  hatted workers in the same run: WORK share 0.39 / 0.57 / 0.48 against 0.60 / 0.55 / 0.44.
- **Verdict (round 2): taste is cut.** Its ceiling (+8% with everyone at full taste) is below
  the batch spread, and the economy never gets near that ceiling. The skeleton keeps wage ->
  pouch -> pull -> paid drink; "work more" moves to participation (18i).

## What "the economy is well" reads, and how the player sees it
- Per creature: its pouch, on the inspector line `💎 3`.
- On sight: the 💎 hop at the station (exists) and at the bar counter (new emote).
- Herd level (later, 18e): a TAB balance row "gems moved / min".
- Stolen gems keep the 💰 head sign; honest gems show no head sign (round: the thief marker
  must stay readable for the cop chase; revert by showing 💰 on any `pouch`).

## Sinks and prices (later slices, relative to a 1-gem minute of work)
Drink 1 (built), meal at a table 1 (to the cook), barber 2 (a mustache style, a mood lift),
furniture store 5 (an own-room item: ties to PR 17's room mood), gift shop 3 (a gift jumps a
bond), arcade 1 a play (fast fun; loud: neighbours sleep worse), hot-tub spa 2 (drains
strain), lottery booth 1 a ticket (the pot pays one winner), pawn shop (a source: sells found
items for gems). No price on a basic need (sleep, survival food): DF's lesson.

## Theft and police hooks (#331)
- Built: the cop takes only `loot`; earned gems stay with their owner.
- Built (18c): a pickpocket theft. A brewer's mark is the nearer of a vault with gems and a
  friend within PICKPOCKET_REACH with spendable gems (not loot, not jailed); a lifted haul is
  loot like a vault's. Round's pick: an arrest sends it the way of any loot (the cop's bag, then
  a station or the bank), not back to the victim: one loot path, and no victim to track
  through saves. Revert to vault-only: PICKPOCKET_REACH 0.

## Skilled jobs and wages (open audit item from #351)
TEACH lost its station pay in #351. Pick (round): skilled jobs earn from the creatures they
serve, not from a station wage: the bartender earns from drinks (built), the teacher from a
pupil's tuition gem (18d), the cook from meals. A gem still never buys a role: it pays the
server who already holds the role.

## Later slices (proposed PRs, each measurable)
- **18b price gate:** a broke drinker is turned away. Done: care 3 seeds x 900 s, snaps and
  care herd within the batch spread of main; broke-drinker refusals > 0.
- **18c pickpocket:** Done: thefts from pouches > 0 per seed under neglect with a bar; arrests
  return `loot` to its owner.
- **18d tuition:** a pupil with a gem pays the teacher a tuition gem per class. Done: teach
  ticks unchanged within spread; teacher pouch income > 0 per seed.
- **18e meals and the herd readout:** cook paid per dish; TAB row gems moved/min. Done: row
  shows; meals bought > 0 per care seed.
- **18g the bartender buys its crops:** it drops a gem into the basket it takes crops from,
  paying that basket's farm shift. Closes the loop (station -> farmer -> bar -> bartender ->
  station). Done: bartender pouch at 900 s <= 2 per seed; basket shifts paid by bartenders > 0.
- **18i work more (built as E', unmeasured):** sim tools in place: `hatted_s`, `jobless_s`
  {int, rest, free}, `aspire_s`, `SIM_STATIONS=n`. Pre-#368 no-lever runs: rich = broke
  (19768 vs 19773 hatted s, 8 kitchens), and jobless "free" stayed 0.07-0.19 even with 12
  paid kitchens: open jobs still cap part of the time.
- **18j reinvest (proposed):** in real play open jobs cap work (free 0.27 at 8 stations), so a
  participation lever does little there; a creature paying a station shift from its pouch
  (Majesty's circulation back to work) would act on that cap.
- **18f furniture shop (built, round's picks):** an OfferPlace (Kind.SHOP, one counter spot).
  A friend with FURNITURE_PRICE spendable gems, a bed in a room, no parcel, and fewer than
  FURNISH_MAX furniture pieces in the room where it sleeps is pulled (SHOP_GAIN). On its spot it
  pays and carries a parcel (📦, saved, VERSION 21); in free time (ROAM/BREAK) it walks to its
  bed (`Housing.bed_of`: its own, else a close owner's) and sets a lamp down in that room on the
  floor nearest the bed, against a wall, a cell clear of other pieces and 2 cells clear of any
  opening; no such spot: the lamp drops by the bed as an item. Death spills it as an item.
  Furniture = the pieces that fit any room (LAW_room_types rule 1: table, chair, lamp), the
  `furniture` group; Housing counts them per room at each reassign (`room_pieces`).
  Picks: (a) **the gems go to the counter as a stack for the player** (Majesty's market: the
  return to the player is its own verb), not to a shopkeeper job; revert: a `buy` to a worker.
  (b) **it sells a lamp** (fits any room, reads as bedroom furniture; lights its room at
  night, within Lamp.MAX_LIT); a chair would add a cure seat in bedrooms (fork 3, open), a
  table needs a kitchen. Revert: `Shop.PIECE`. (c) **it walks home at once in free time**, not
  at its next sleep: a jobless roamer's sleep never drains, so a bedtime unpack could wait
  forever. (d) a cap per room, not per bed: a bunkhouse gets 2 pieces for all its sleepers.
  Rejected: a remote spawn at the sale (a payment or item never moves off screen); a
  player-placed parcel (the player's lamp, not the creature's room). Cheat `/shop`; SIM_SHOP=1.
