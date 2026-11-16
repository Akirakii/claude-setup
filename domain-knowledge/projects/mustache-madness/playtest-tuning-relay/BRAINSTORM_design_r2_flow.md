# BRAINSTORM: R2 economy flow (till, 18c, 18d, bar, 18g, vault)

Design only, no code. Picks tagged (user) are the user's own words; every other pick is
proposed. Line numbers are main @ c516194a unless a line says "branch" (feat/pickpocket @
c9d2c210, worktree mm-fixes). R2 owns payment rules 1-4 (user, 2026-10-22); other rounds
reuse the verbs below and do not redesign them.

## Round 3 changes
- The payment model is settled (user, 2026-10-22; docs/BRAINSTORM_design_payment_model.md
  "Synthesis", HANDOFF_playtest_tuning.md "Payment model picks"). New sections: "Terms",
  "Till" (rules 1-2), "Vault deposit" (rule 4). 18g becomes "bar sign pays basket sign per
  crop" (rule 3).
- Cut as moot: `Creature.tip`, the per-unit `makers` lists on bags, stacks, counters and saves,
  and pouch-to-pouch `buy()`. A gem a creature spends now lands on a sign or a worker's pouch
  by the till rule, never in another creature's pouch directly.
- 18d-bar fork closed: the bar becomes a Station with one sign (rule 1, user).
- Folded in from R6b and R7: supplier pay happens at delivery or at the worker's own take from
  a supplier stack, not at use; an empty paying sign pays nothing and the delivery goes on;
  thrown stock pays no one. From R6: spare = pouch above 1 (POUCH_KEEP 1).
- Round 3b, reconciled with R1 and R6: one gem ladder on a creature: loot (never spent),
  then R1's savings (toward its next home good), then free gems. Servings spend free gems;
  the deposit takes free gems above POUCH_KEEP 1. A sign that cannot pay its supplier takes
  only what it can pay for (R1's rule; round 3's "take goes on unpaid" is reversed, below).
  Broke (no free gems) pays nothing for drinks, meals and classes and is served free; broke
  blocks only goods that go home (R1). 18d tuition follows that.
- Payments are by role (funder, customer, sign), never by player versus creature (user
  correction, 2026-10-22); table below Terms.
- Stage 2 hook: a sign's funder is "the player or a creature owner"; no rule here names the
  player (note at the end).

## Round 2 changes (kept for the record)
- 18c merge as built, loot to the police (user). 18d board = Station, chairs facing it are
  desks, one per room (user). Bartender is a paid job (user).

## Terms (each by what it takes in and gives out)
- **Sign:** a workplace's one pay counter (a Station's `wage` + its 💎 label, station.gd:21-82).
  Takes in: thrown or carried gems (the player, the bank payer, a supplier pay), and sale gems
  while due. Gives out: one gem per shift to its worker, and supplier pay from its stack.
- **Stack:** the gems on a sign not yet worked (`wage.gems`, wage.gd:20). Each is 60 s of open
  time (GEM_SEC). Pay ahead without limit (user).
- **Shift:** 60 s on the sign's clock, started by the worker taking one stacked gem into its
  pouch in person (`punch_in`, station.gd:96-99; creature.gd:1212-1219).
- **Due:** the sign is on its last shift with nothing stacked (`due()`, station.gd:102-104). A
  closed sign (no shift, no stack) is never due.
- **Sale:** a creature's gem for its own serving (a drink, a lesson; meals in 18e). Takes in:
  the buyer's spendable gems (never loot). Gives out: the gem onto the seller's sign while due,
  else to the sign's surplus holder.
- **Surplus holder:** who keeps a sale gem the sign does not need: the sign's funding owner if
  it has one (stage 2), else the serving worker.
- **Supplier pay:** sign to sign. Takes in: units of stock a workplace takes from another
  workplace's stack. Gives out: 1 gem per unit from the taking sign's stack onto the source
  sign's stack, where the maker earns it as its next shift's wage.
- **Savings (R1 owns):** gems a creature keeps toward its next home good; 0 when it wants
  none. Takes in: its spendable gems, up to the good's price. Gives out: the buy of that good
  (R1, goods go home). Servings and the deposit never touch it.
- **Free gems:** `spendable() - savings()`, floored at 0. What a serving is paid from; with
  fewer than the price, the creature is broke for that serving and is served free.
- **Spare:** free gems above POUCH_KEEP (1). Takes in: wages and surplus. Gives out: a walk to
  the bank, where the spare goes into the vault; the kept gem pays its next serving.

## Who pays whom, by role (one creature can hold several roles)
| Role | Pays | For | Through | Lands |
|---|---|---|---|---|
| Funder (the player now; a creature owner in stage 2) | salary: time, 1 gem = 60 s, ahead without limit | open hours | a throw, a carry, or the bank payer onto the sign | the stack; the worker takes 1 gem a shift |
| Customer (any creature) | per unit, from its free gems; broke is served free | its own serving (drink, lesson, meal) | the till (`sell`) | the sign while due, else the surplus holder |
| Sign (a workplace taking stock) | per unit, 1 gem | stock taken from another workplace | `pay_supplier`, at the take or the delivery | the source sign's stack, the maker's next wage |
An owner in stage 2 funds its staff's salary as a funder and buys drinks elsewhere as a customer.

### Till: one sign per workplace; a sale lands on the sign while due (rules 1-2)
- **Frame:** a creature's gem buys its own serving and should keep the workplace open when the
  sign runs low, else reward the worker; today it goes pouch to pouch and pools in the
  bartender (measured care seed 1: wages 20, bought 18, ~22 of 40 drinks free).
- **Assumptions to verify:**
  - [x] Every gem spent today goes through `Creature.buy(price, seller)` (creature.gd:1054-1072),
    called only by the bar (bar.gd:196). It also arms aspire on onlookers (:1067-1070).
  - [x] `due()` already means "last shift, nothing stacked" and the payer reads it
    (station.gd:102-104; till.gd:11), so a closed sign is never due.
  - [x] The bank overrides `due()` false and `paid()` true (bank.gd:70-84): it never takes sales.
  - [x] A sale stacking 1 gem while due makes `due()` false at once, so a customer funds one
    shift at a time and never stacks hours ahead: pay-ahead stays the funder's.
- **Candidates:**
  - A. `Station.sell(n, server)`: each gem onto the stack while due, else to the surplus holder.
    Survives: the user's rule, one verb.
  - B. Coin-op: each sale buys 60 s for everyone present. Cut by the user's pick (Firm).
  - C. Sales always onto the stack. Cut: customers would stack hours ahead, and the worker
    never sees a sale (the synthesis's "only B keeps pay ahead without limit").
- **Recommendation:** A. Scene: the bar's sign reads 💎 0:12. A grump drinks; 💎 hops onto the
  sign, now 💎 1 0:12. The next drinker's gem pops over the bartender instead. Mechanism:
  `buy(price, station, server)` takes `price` from free gems, calls `station.sell`, arms aspire
  as today; false = too few free gems (served free, rule 5).
- **Interface other rounds call:** `Creature.buy(price, station, server) -> bool` (a serving;
  R1's shop sale is the same call with its clerk as server), `Station.sell(n, server)`,
  `Station.pay_supplier(source, n) -> int` and `Station.can_supply(n) -> int` (18g),
  `Creature.free_gems()` (savings come from R1's `savings()`).
- **Build sketch:** creature.gd:1054 `buy(price: int, station: Station, server: Creature)`;
  `free_gems()` beside `spendable()` (:1079), reading R1's `savings()` (0 until R1 lands).
  station.gd: `sell(n, server)` and `surplus_holder(server) -> Creature` (owner if valid, else
  server; owner is the stage 2 slot, always null now). Tallies: `Station.sales_to_sign`,
  `Creature.bought` kept (balance_probe.gd:752), sim driver, sim_report.
- **Tests + cheat key:** test_payer.gd: `test_a_sale_goes_on_a_due_sign`,
  `test_a_sale_goes_to_the_worker_when_not_due`, `test_a_sale_never_opens_a_closed_sign`
  (closed: no serving at all), `test_loot_never_buys`, `test_savings_never_buy_a_serving`. Cheat: `/bar` (below).
- **Open questions for the user:** none.

### 18c: pickpocket (built, merge as built)
- **Frame:** a brewer robs the nearer of a vault or a friend's pouch; merge as built (user).
- **Assumptions to verify:**
  - [x] Mark, haul and loot as built (branch creature.gd `_theft_mark`, `_rob`); loot goes to
    the police on arrest (user).
  - [x] After the vault deposit, pouches hold about POUCH_KEEP (1) spendable gem, so most
    pickpocket hauls are 1 gem and the fat vault becomes the usual mark. No change needed.
- **Candidates:** loot to the victim: cut (user). Richest mark: cut (honest gems show no sign).
- **Recommendation:** merge. Scene: a grumpy turtle lifts a gem off a sleeping farmer (😱, 💰);
  a cop hat carries it to a cell.
- **Build sketch:** one fix: branch cheat_coordinator.gd:793 doc line back over `spawn_paid`
  (:813). Note: the vault deposit section touches `_decide_mode` next to STEAL (:793-795).
- **Tests + cheat key:** built (two tests); `/pickpocket` (console).
- **Open questions for the user:** none.

### 18d: the chalkboard is a workplace, chairs facing it are desks
- **Frame:** a teacher works a paid job (user): the board is a Station with one sign, any chair
  facing it in its room is a desk, one board per room (user); a learner's gem buys its lesson.
- **Assumptions to verify:**
  - [x] Today the board is an OfferPlace with 3 desks (chalkboard.gd:2; chalkboard.tscn:47-53),
    no wage, always open (job_board.gd:220), teacher never fetches a gem (:180-189).
  - [x] A Station site is open only while paid and its worker punches in (job_board.gd:220;
    creature.gd:719). A chair already reads its neighbours (a table, chair.gd:17-27).
  - [x] Chairs face the player when placed (chair.tres `faces`, placed_behavior.gd:16-20).
  - [x] Room rules are soft (warn ghost, then off with a sign; build_hand.gd:154-170,
    grid_object.gd:57-59), and rooms merge after placement, so one-per-room must be checked
    at run time anyway. Room size cap: rooms.gd:11, 442.
  - [ ] When two boards share a room, the first in group order stays on: verify load keeps it.
- **Candidates:** board = Station + chairs facing it (user); one per room soft (warn + off),
  survives; hard refusal cut (rooms change after placement); any chair in the room cut (user
  said facing).
- **Recommendation:** Scene: a teal room; the board's sign 💎?; you throw a gem, a mortarboard
  friend takes it (💎), 📖 lights. Chairs facing the board fill with dull friends; a woodcutter
  with 2 gems pays its lesson: the board is due, so 💎 hops onto the sign. A broke friend learns
  free. A second board in the room sits grey. Mechanism: chair offers TRAIN while
  `_faced(&"class_board")` teaches; first lesson of a stay runs `buy(TUITION_PRICE, board,
  teacher)`; with no free gems it learns free (R1's broke rule: classes are free to the broke,
  confirmed), and its savings for a home good are never touched.
- **Interface R6 reuses:** a teaching piece is a Station in group `class_board` with `@export
  stat`, `teaches(c) -> bool`, `lesson(c, first_of_stay)`; its .tres sets `one_per_room =
  &"class"`; tuition through the till verb `buy(price, station, server)`.
- **Build sketch:** chalkboard.gd `extends Station`, drop OfferPlace parts, add `teaches`,
  `lesson`; chalkboard.tscn drop Spot1-3. placed_behavior.gd:23 `@export one_per_room`;
  resolve_placement (:60) `"crowded"` warn; grid_object.gd:57 `works()` off for a later twin.
  chair.gd `_faced(group)` (same room, front within DESK_CONE, nearest) + TRAIN; transient
  `_lessoned` cleared in `leave`. Config: `TUITION_PRICE 1`, `DESK_CONE 0.5`. Save VERSION bump.
- **Tests + cheat key:** `test_a_board_opens_teach_only_while_paid`,
  `test_a_chair_facing_a_class_is_a_desk_and_one_facing_away_is_not`,
  `test_a_chair_in_another_room_is_no_desk`, `test_tuition_goes_on_a_due_board`,
  `test_tuition_goes_to_the_teacher_when_not_due`, `test_a_broke_learner_learns_free`,
  `test_a_second_board_in_a_room_stays_off`. Cheat `/teach` (KEY_T): hut, board paid 1 gem,
  4 chairs facing it, 1 facing away, a teacher (INT 14), 3 dull friends, one holding 2 gems.
- **Open questions for the user:**
  1. Sign on a second board in a room: invented readout, propose "📖x2". Pick or name one.

### 18d-bar: the bar is a workplace with one sign
- **Frame:** the bartender works a paid job (user): the counter is a Station, its sign pays
  shifts, chairs facing it are bar seats, and a drink is a sale through the till.
- **Assumptions to verify:**
  - [x] The bar opens today from its bartender's first labor tick with no gem (bar.gd:63-66,
    86-94); stools and the owed-drink and round logic live on it (bar.gd:171-215).
  - [x] One script cannot be both Station and OfferPlace (both extend GridObject).
- **Candidates:** A, counter = Station + chairs facing it (same shape as the board): survives,
  picked (rule 1, user). B, a pay part on the old bar: cut (two ways to be a paid workplace).
- **Recommendation:** Scene: a purple room, counter sign 💎?; you throw a gem, a bartender hat
  takes it, restocks, mixes; grumps in chairs facing the counter drink and chat in pairs.
  Mechanism: `_serve` runs `buy(DRINK_PRICE, self, _bartender)`; broke drinks free (rule 5);
  open = on shift and bartender awake.
- **Build sketch:** bar.gd `extends Station`; seats = chairs `_faced(&"bar")` in its room;
  `_next_seated` walks that list; bar.tscn drop the stools; chair.gd DRINK branch; SPEND_GAIN
  unchanged (offer_place.gd:161-165). Save VERSION bump (one bump with 18d if landed together).
- **Tests + cheat key:** test_social_bar.gd moves to chairs; add `test_a_bar_opens_only_while_
  paid`, `test_a_drink_on_a_due_bar_goes_on_its_sign`. Cheat `/bar` (KEY_O): bar paid 1 gem,
  4 chairs facing it, 2 grumps with 3 gems each, a basket with 6 carrots and a farmer (INT 8).
- **Open questions for the user:** none.

### 18g: the bar's sign pays the basket's sign per crop (rule 3)
- **Frame:** a workplace that takes stock another workplace made pays that workplace's sign 1
  gem per unit, sign to sign; the maker earns it as the wage of its next shift (user).
- **Assumptions to verify:**
  - [x] The bartender takes crops in person from the nearest basket stack (creature.gd:1233-1239,
    bar.gd:136-141); this take knows both signs, so no per-unit record is needed.
  - [x] R6b's haul delivery knows its source by the bag's saved `bound_from` and calls the same
    verb per unit (R6b design); the bartender's own restock is the same rule.
  - [x] A gem added to a basket's stack becomes a farmer's shift gem (station.gd:70, 96-99).
  - [x] Stock the player throws (kitchen.gd `_on_body_entered`, bar.gd:229-236) has no source
    sign, so it pays no one.
  - [x] A farmer sowing from its own basket takes from its own sign: nothing to pay.
- **Candidates:**
  - A. Pay at the take or delivery: `sink.pay_supplier(source, n)`. Survives: the only moment
    that knows both signs (rule 3 bans per-unit records).
  - B. Pay at use (mixing, cooking). Cut: the unit no longer knows its source.
  - Short paying stack: (a) take all, pay what the stack covers, rest unpaid; (b) take only
    as many units as the stack pays for (R1's clerk rule). (b) survives: every unit taken is
    paid, so the maker always earns; the reason for a wait shows on the sign (💎? or 0
    stacked); paying a workplace ahead now also buys its supplies, a real use for pay-ahead;
    and a customer's gem on a due bar becomes one crop's pay, so sales fund supply one unit at
    a time. (a) cut: stock leaks out unpaid and the maker's wage depends on luck. Reverses
    round 3's pick and R6b's rec; one rule for every taker.
- **Recommendation:** A with (b). Scene: the bar's sign 💎 3; the bartender scoops 2 carrots at
  the basket; 💎 hops off the bar's sign (now 💎 1) and onto the basket's (💎? to 💎 2); a
  straw-hat friend walks over and takes its shift gem. With 💎 0 stacked the bartender takes
  nothing and waits at the bar until a gem lands on its sign. Mechanism: the taker asks
  `can_supply(n)` = min(n, stack) and takes that many; `pay_supplier(source, n)` moves n
  stacked gems to `source.pay()`. It never touches the running shift (the worker's wage) and
  never opens the sink. A hauler (R6b) sizes its pickup by its bound sink's `can_supply` and
  pays at delivery; if the sink's stack fell during the walk, the short units are unpaid (a
  race, not a rule). Thrown stock skips all of this and stays free.
- **Build sketch:** station.gd `can_supply(n) -> int` and `pay_supplier(source: Station, n: int)
  -> int` (paid count; source == self pays 0 and is never capped); bar.gd:136 `bag_from` caps
  its room by `can_supply`, then pays for what it took; `restocks()` (bar.gd:106) false while
  `can_supply(1)` is 0, so the bartender stays at the counter. `SUPPLY_PRICE:
  int = 1`. Tally `Station.supplied` in balance_probe.gd counters, sim driver, sim_report.
- **Tests + cheat key:** `test_the_bar_pays_the_basket_per_crop_taken`,
  `test_a_bar_takes_only_the_crops_its_stack_pays_for`, `test_an_empty_bar_stack_does_not_
  restock`, `test_a_sale_on_a_due_bar_buys_one_crop`, `test_the_running_shift_is_never_paid_out`,
  `test_a_take_from_its_own_sign_pays_nothing`, `test_thrown_crops_pay_no_one`. Cheat `/bar`.
- **Open questions for the user:**
  1. A supplier gem lands on a closed basket (no shift, no stack) and opens it, so a busy bar
     can open its own farm. Rule 3 says "pays the supplier's sign", so the draft keeps it.
     Keep, or route it only while the basket is open? Recommend keep.
  2. With (b), a bar the funder does not pay ahead restocks one crop per due sale, so an
     unfunded busy bar may run dry between sales (thrown crops still work). Intended pressure
     to fund it, or too tight? Measure before pricing (synthesis "measure first").

### Vault deposit: spare gems walk to the bank (rule 4)
- **Frame:** gems that pool in pouches move no work; a creature walks its spare gems to the
  bank vault, and the existing payer carries them to due signs, so herd wealth keeps open jobs
  open while the funder still picks which signs open (user).
- **Assumptions to verify:**
  - [x] `Bank.pay` stows into the vault, no cap (bank.gd:70-91); the vault label shows 💰 n.
  - [x] The payer takes one vault gem per labor tick only while some sign is due (till.gd:11)
    and pays the nearest due sign (creature.gd:1169-1177). `due()` needs a running shift, so the
    payer never opens a closed sign (user rule 4, already true).
  - [x] A banker grows the vault 1 gem per 20 ticks while it holds any (bank.gd:99-109); a fuller
    vault is also the brewer's usual mark (`Bank.with_loot`, bank.gd:41-57).
  - [x] STEAL already walks a creature to a bank with `_walk_to` (creature.gd:676-680, 1244).
- **Candidates:**
  - A. A free-time errand: in `_decide_mode`, after STEAL and before OFFER, a friend with spare
    gems and a reachable bank walks there and stows the spare. Survives.
  - B. The payer collects from pouches (Majesty's tax collector). Cut: a new verb on the payer,
    and gems leave creatures by a remote pull.
  - C. Spare gems pay due signs straight from the pouch (a creature-run payer). Cut: rule 4
    names the vault, and it skips the bank's growth and the thief's mark.
  - Spare = free gems above 1 (R6 + R1): survives; every creature keeps a gem for its own
    serving, and its savings for a home good stay in the pouch.
- **Recommendation:** A. Scene: after its shift a woodcutter with 💎 4 waddles into the gold
  bank, 💎 pops, the vault reads 💰 13, it keeps 1. The purse-cap payer takes a gem to the
  woodpile whose sign just went due. Mechanism: spare = free_gems() - POUCH_KEEP; loot and
  savings never go in; no bank, no walk (the gems stay).
- **Build sketch:** creature.gd:7 `Mode.DEPOSIT`; `_decide_mode` (:793) branch; `_combat_tick`
  or the free-time tick runs `_walk_to(Bank.nearest(pos))` then `bank.pay(spare)`, `pouch -=
  spare`, `emote(Wage.GLYPH)`. Bank gets `nearest(pos)` beside `with_loot`. Config `POUCH_KEEP:
  int = 1`. Tally `Bank.deposits` in probe, sim driver, sim_report.
- **Tests + cheat key:** `test_a_friend_with_spare_gems_walks_them_to_the_vault`,
  `test_it_keeps_one_gem`, `test_loot_is_never_deposited`, `test_savings_are_never_deposited`, `test_no_bank_no_walk`,
  `test_the_payer_never_opens_a_closed_sign`. Cheat `/vault` (console): a bank, a payer
  (INT 8), a friend holding 5 gems, a woodpile on its last shift.
- **Open questions for the user:**
  1. Deposit before or after the bar in a creature's free time? The ladder puts it before
     leisure, but it keeps 1 gem, so a drink is still bought. Recommend before.

### Stage 2 hook (no design, only no blockers)
A sign's funder slot is "the player or a creature owner" (docs/BRAINSTORM_game_stages.md
market arc, Q9). Here: `Station.surplus_holder` returns the owner if one is set, else the
serving worker, so a sale's surplus can go to an owner later; `pay()`, `due()`, the payer and
`pay_supplier` read only the sign, never who funds it, so an owner paying from its pouch is the
same `pay()` call. No rule here says "the player". Founder, hiring and bankruptcy: stage 2.
