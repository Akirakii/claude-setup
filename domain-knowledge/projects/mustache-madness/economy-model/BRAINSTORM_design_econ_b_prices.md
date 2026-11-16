# BRAINSTORM: cluster B design (B1 prices + buy gate, B2 maker pay + basket sale, B3 tuition + medic fee)

Design only, read from `/home/akiraki/Playground/mm-econ` @ c516194a (branch feat/econ-bank, no
B work on it). Picks are proposed (round) unless tagged (user). Nothing simulated, no tuning.
Decisions: `docs/BRAINSTORM_economy_model.md` "User decisions (2026-10-24)" on, and
`docs/BRAINSTORM_food_theft.md` "Picks". Prior art below is from memory unless a link is given.

## Round 2 changes (AFK, picks are the session's, not the user's)
- **A2 owns the bar and chalkboard pay signs** and `Bar.server()` / `Chalkboard.server()`,
  read off their shift worker like `Station.server()`. B builds on A2: B1 adds only
  `GridObject.server()` (null), `Station.server()` + `shift_worker` + `punch_in(worker)`,
  `buy_at`, `payer_for`, `is_friend`. Merge order puts A2 before B1; if A2 lands as a Station
  subclass for both, its `server()` is the Station one and needs no override.
- **B2 gains the cook restock:** the cook fetches crops from the nearest open basket on the
  bartender's path, pays the farmer 1 gem per crop, bags only what its pouch covers; the
  kitchen posts COOK while paid, not only while stocked.
- **Remote pay** (diner to cook, buyer to farmer): a `💎` emote at both ends. Flag for the
  user: LAW "a payment between a creature and an object is done on screen" is bent here.
- **Broke student refused** (U1); the library stays the free door.
- **Friend rule (cross-check, supersedes the round 2 `befriends`):** one function,
  `SocialComponent.is_friend(peer: Creature) -> bool` = `friendliness(peer) >= FRIEND_LINE`
  (`social_component.gd:45`). Liking gates; familiarity only ranks. B1 owns it and
  `CreatureConfig.FRIEND_LINE`; C1 (heir) and C2 reuse it.
- **`FRIEND_LINE = 2.0` (start).** Scale: friendliness is signed, clamped to
  `SOCIAL_FRIEND_MAX` 5.0 either way (`creature_config.gd:573`), so 2.0 is 40% of full liking.
  Decay: exponential at `SOCIAL_DECAY_RATE` 0.004 per dilated s times
  `warmth_decay_factor` (`social_component.gd:118-120`, `creature_config.gd:668`): half-life
  about 173 s at warmth 0, not the "~3 days" its comment says (`creature_config.gd:576`; a
  stale comment or a unit slip, worth one check). A positive beat adds about 0.3-0.5
  (`social_action.gd:116-151`). Holding 2.0 against that decay costs about 0.5 liking per
  minute, so about one good chat a minute: a friend means "a pal it is chatting with now",
  which suits a treat at a shared bar or table. For C1's heir (a death far from any chat) 2.0
  may pick almost no one; if the sim shows that, lower the line or fix the decay, not a
  second threshold.
- **Treat trigger:** the treat fires when the buyer cannot afford the cheapest food on sale
  (any open food place it could walk to: a dish, a raw crop), not when it lacks this good's
  price. At the bar, the drink's own price applies (a drink is not food).
- **Public reads cluster C reuses (B1 owns, B2 adds the basket case):**
  1. Buy gate answer: `GridObject.server() -> Creature` (null = closed, the buyer waits) and
     `Creature.buy_at(place: GridObject, price: int) -> bool`.
  2. Seller lookup: `static func Creature.seller_of(food: Node3D) -> GridObject`: a `Table`
     -> `Kitchen.serving(table)` (nearest Kitchen within `Table.SERVE_REACH` with a server);
     a stored `DroppedItem` -> `Basket.at(food.global_position, tree)`; else null (free food).
     `static func Kitchen.serving(table: Table) -> Kitchen`,
     `static func Basket.at(pos: Vector3, tree: SceneTree) -> Basket`.
  3. Treat finder: `Creature.treater(price: int) -> Creature`: the most familiar seated ally
     within `TREAT_RADIUS` that `is_friend(self)` in its own SocialComponent and has
     `spendable() >= price`; null = no treat. `Creature.payer_for(price) -> Creature` = self
     if it can pay, else `treater(price)`. `Creature.cheapest_food_price() -> int` (lowest
     price among open food places in reach; -1 when none is on sale) is the trigger
     C2's steal gate reads with them: steal = 0 spendable, hungry, and `treater(...) == null`.
- **Thrown crops stay free stock** (session pick): a crop the player throws into a bar or a
  kitchen pays no farmer.

## Built today (checked)
- **Mate's treat at the bar (18b): not built.** A broke drinker drinks free: `bar.gd:193-198`
  (`_serve` pours, then `buy` may fail), asserted by `test_social_bar.gd:358`.
- **Chalkboard a paid Station: no.** `Chalkboard extends OfferPlace` (`chalkboard.gd:2`); TEACH
  is "unpaid, like the bartender" (`creature_config.gd:275`). The bar is the same
  (`bar.gd:2`, `creature_config.gd:231`). So bartender and teacher earn no wage today (R8 gap).
- **Medic treatment event: yes, two once-per-care points.** `Creature.labor` TREAT branch:
  the grab to a free medic bed (`creature.gd:2621-2624`) and "care starting"
  (`if not rest.is_tended()`, `creature.gd:2626-2628`). Every later tend tick re-arms care and
  counts `MedKit.tends` again (`creature.gd:2629-2631`), so it is not a fee point.
- **Dish relieves more hunger than a raw crop: yes, double.** Chair eats with fill 1.0
  (`chair.gd:36`); any other food fills `MEAL_FILL` 0.5 (`creature_config.gd:121`,
  `creature.gd:2243-2248`). At 2 gems vs 1 gem: 0.5 hunger per gem both ways.
- **One transfer exists:** `Creature.buy(price, seller)` (`creature.gd:1054-1067`): checks the
  seller is a FRIENDLY not leaving, pays from `spendable()` (loot never spent), tallies
  `bought`, arms 18i aspire on onlookers. Only the bar calls it (`bar.gd:196`).
- **Kitchen stock comes only from throws** (`kitchen.gd:61-66`); the cook never visits a
  basket. The bartender restocks from the nearest basket (`creature.gd:1233`, `bar.gd:136`).
- **Basket stock is eaten free** by a creature tired from hunger (`creature.gd:809, 820-831`);
  a creature starving `STARVE_SEC` harvests a ripe field crop free (`creature.gd:811, 835`).

## Shared mechanism: the one buy gate (B1 owns; A, B2, B3, C reuse)
Rule (user): a creature buys only from an open workplace with its worker on shift; else it
waits. Candidates: G1 each workplace answers `server() -> Creature` and one `buy_at` pays it
(survives, pick); G2 a central `Jobs.server_at(place)` from the job board's tables (cut: a
farmer between ripe crops loses its site and hat, `job_board.gd:194-209`, while its shift
still runs, so the farm reads closed mid-shift; and bar and chalkboard need special cases
anyway); G3 each sale checks its own conditions inline, today's bar pattern (cut: five copies
of one rule); G4 a Counter node with price and good on each workplace (cut: a new noun for a
constant). Field: Theme Hospital and Two Point Hospital queue patients at a room until its
staff member is in it (memory); same rule, the room waits, the patient waits.

Interface (GDScript, server side):
- `GridObject.server() -> Creature`: null (closed). Overrides:
  `Station.server()`: `shift_worker` while `on_shift()` and it is FRIENDLY, awake, not leaving.
  `Bar.server()` and `Chalkboard.server()`: A2 builds them off the shift worker (round 2).
  B3 still checks the class is on (`_teaches`) before it charges tuition.
- `Station.shift_worker: Creature` (transient): set by `punch_in(worker)` (`station.gd:96`, the
  one call `creature.gd:1215` passes `self`). "On shift" = the creature that took this shift's
  gem, while that shift runs. After a load it is null until the next punch-in (at most one
  60 s shift closed): accepted, named here so no one calls it a bug.
- `Creature.buy_at(place, price) -> bool`: `buy(price, place.server() if place else null)`.
- `Creature.payer_for(price) -> Creature`: itself if `spendable() >= price`, else the most
  familiar ally seated within `TREAT_RADIUS` (its `offer_place.on_spot`) that `is_friend(self)`
  and can pay; else null. A treat is `payer != buyer`.
- `SocialComponent.is_friend(peer) -> bool`: `friendliness(peer) >= FRIEND_LINE` (Round 2).
  C1's heir pick reads the same predicate (F5).
"Waits" means the pull is 0: a place whose `server()` is null, or whose price no payer covers,
draws nothing, so the chooser never walks there. The pay sign (`💎?`) is the state sign.

## Forks (cluster B closes or recommends)
- **F1 closed:** margin is per crop (bar 2 drinks x 1 gem - 1 crop pay = 1; kitchen 2 - 1 = 1),
  not per unit; user-set ratios, nothing to change.
- **F2 closed (with the brief's reading):** the tip IS the price. The customer pays the server
  the full price into its pouch; the server pays its farmer from that pouch. One rule for every
  serving job: "a server keeps what its customers pay and pays 1 gem per crop it takes".
  Teacher and medic take no crop, so they keep all of it.
- **F3 pick: at restock.** The farmer is paid when crops leave its basket into a server's bag,
  the server on screen at the basket. At-sale cut: a 1-gem drink cannot split 1 gem per crop
  without a carry, and a thrown crop has no farmer to pay. Consequence: the cook pays no
  farmer until it fetches its own crops (B2 open question 1).
- **F5 pick: one threshold.** `FRIEND_LINE` (on liking, `is_friend`) serves treat and heir; "a mate" and "friend level"
  are the same bond in plain words. Value: open (tuning).
- **F6 pick: it waits.** A 1-gem hungry creature with only a kitchen open buys nothing and is
  not broke (steal needs 0 gems, user). A seated friend may treat it: the cheapest food on
  sale (2) is past its pouch. With a raw crop also on sale it buys that and gets no treat. Past `STARVE_SEC` today's free ripe-crop harvest still feeds it
  (`creature.gd:811`); C2 decides whether that stays foraging.
- **F8 closed:** a dish fills 1.0, a raw crop 0.5: equal hunger per gem. The drink fills fun
  (`bar.gd`, `FUN_PER_USE`) and tipsiness, never hunger.
- **F9 pick: per student per stay,** paid on its first class tick, like the bar's once-a-stay
  drink (`_drunk`).
- **F10 closed:** the honesty box means no clerk walk; the gate still needs the farmer on
  shift. The gem goes pouch to pouch to the shift's farmer, which shows `💎`.

### B1: prices, recipe ratios, the buy gate, and the treat
- **Frame:** today a broke creature drinks free and every meal is free; the player should see
  a gem buy a drink or a dish only at a workplace that is open, and a broke one get it only
  when a friend beside it pays.
- **Assumptions to verify:**
  - [x] One transfer, `buy`, only the bar calls it (`creature.gd:1054`, `bar.gd:196`).
  - [x] Broke drinks free today (`bar.gd:193-198`, `test_social_bar.gd:358`): changes.
  - [x] Bar mixes 1 crop to 1 drink (`bar.gd:79-81`); room counts crops 1:1 (`bar.gd:101`);
    a knocked bar spills `drinks + crops` as crops (`bar.gd:225`).
  - [x] Meals: the chair eats any dish on a table within 1.5 m (`chair.gd:34-45`); the table
    has no link to its kitchen (`table.gd`); the kitchen serves the nearest table in 10 m
    (`kitchen.gd:43-51`, `Table.SERVE_REACH`).
  - [x] Dine pull ignores gems (`offer_place.gd:149-151`); drink pull adds `SPEND_GAIN` for
    a payer (`offer_place.gd:162-166`).
  - [x] No friend threshold exists (familiarity is a plain 0-5 value).
  - [x] Closed round 2: a disliked mate does not treat (`friendliness >= 0`).
- **Candidates:** T1 the seated friend pays the whole price (survives, pick); T2 the friend
  hands over gems to the broke one's pouch (cut: R1 no deposits, gems move only by buying);
  T3 the bartender pours on credit, paid back later (cut: a hidden per-creature ledger);
  T4 a broke diner begs at any table and any friend in the herd pays remotely (cut: natural on
  sight fails, the friend is not there).
- **Recommendation: T1 on the shared gate.** Scene: two friends sit at the bar; the bartender
  pours, one pays (`💎` over the bartender), the broke one gets nothing and chats; when the pair
  chats a round, the friend pays both drinks and a `💎` floats over the friend too. A broke
  creature alone at the bar sits for fun and gets no drink. At the table, a diner with 2 gems
  eats and the cook in the kitchen shows `💎`; a broke one only sits down when a friend with
  gems is seated at a chair there. Mechanism: every sale is `payer_for(price).buy_at(place)`;
  the good goes to the buyer only when it returns true.
- **Build sketch:**
  - `creature_config.gd:158`: keep `DRINK_PRICE = 1`; add `DISH_PRICE = 2`,
    `DRINKS_PER_CROP = 2`, `FRIEND_LINE = 2.0` (start), `TREAT_RADIUS` (seat
    neighbourhood, about 2.5 m, guess).
  - Gate pieces above: `GridObject.server()`, `Station.server()` + `shift_worker` +
    `punch_in(worker)` (`station.gd:96`, caller `creature.gd:1215`, tests
    `test_basket.gd:35`, `test_job_economy.gd:75`), `Creature.buy_at`, `payer_for`,
    `is_friend`, `treater`, `seller_of`, `Kitchen.serving`. `Bar.server()` and `Chalkboard.server()` come from A2.
  - `bar.gd:193 _serve`: `var p := c.payer_for(DRINK_PRICE)`; if `p and p.buy_at(self, ...)`
    then `drinks -= 1`, pour, `c.drink()`; else `refused += 1`, no pour. A bartender drinking at
    its own bar stays free (today's `_bartender != c`). `p != c`: `treats += 1`, `p.emote(💎)`.
  - `bar.gd:79-81`: one crop mixes into `DRINKS_PER_CROP` drinks; `_room()` counts a crop as
    `DRINKS_PER_CROP` slots; `_yeet_drops` spills `crops + drinks / DRINKS_PER_CROP` crops (no
    crop duplication by knocking a bar).
  - `chair.gd:13 draw_for`: dine counts only when `_table()` has an open kitchen
    (`Kitchen.serving(table)`: nearest Kitchen within `Table.SERVE_REACH` whose `server()` is
    not null) and `c.payer_for(DISH_PRICE)` is not null. `chair.gd:36 _use`: pay first, then
    `try_feed`. A table with only thrown dishes and no open kitchen sells nothing (waits).
  - `offer_place.gd:162-166`: the bar's spend pull reads `payer_for(DRINK_PRICE)` (self only
    in practice; a treat pull needs the friend seated already, which is the scene we want).
- **Tests + cheat key:** `test_social_bar.gd:358` becomes
  `test_a_drinker_pays_its_bartender_and_a_broke_one_gets_no_drink` (drinks unchanged, mood
  not lifted by a drink, `Bar.refused` 1). New in `test_social_bar.gd`:
  `test_a_seated_friend_treats_a_broke_mate` (friend pouch -1, bartender +1, broke pouch 0,
  broke drank); `test_a_familiar_stranger_below_friend_level_treats_no_one`;
  `test_one_crop_mixes_two_drinks_and_a_knocked_bar_spills_no_extra_crop`. New in
  `test_restaurant.gd`: `test_a_diner_pays_the_cook_on_shift_two_gems`,
  `test_no_cook_on_shift_no_meal_and_no_pull`, `test_a_broke_diner_sits_only_beside_a_paying_friend`.
  New in `test_job_economy.gd`: `test_the_server_is_the_creature_that_took_the_shift_gem`
  (null after the shift ends, null when it sleeps). Cheat `/treat` (rooms): a hut, a bar with 4
  drinks and a bartender, a table with 2 dishes beside a paid kitchen and its cook, two
  befriended friends (one 4 gems, one 0) and a lone broke friend.
- **Shared with other clusters:** the gate (`server`, `buy_at`, `shift_worker`); `payer_for`
  (C2's steal gate "no treat came" = `payer_for(price) == null` at every open food place);
  `is_friend` + `FRIEND_LINE` (C1 heir), `seller_of`, `treater`. A1: the payer's `punch_in` passes `self` too, and a
  bank that gets a sign gets `Station.server()` for free.
- **Open questions for the user:**
  1. Closed round 2: A2 gives bar and chalkboard a sign and their `server()`.
  2. Closed round 2: treat at the table too.
  3. Open: `FRIEND_LINE` 2.0 against a 173 s liking half-life (Round 2); lower it if treats
     or heirs rarely fire.

### B2: maker pay, the honesty box, and the raw-crop sale
- **Frame:** a farmer today is paid only its wage, and basket stock feeds a tired creature
  free; the player should see a server buy its crops at the basket, and a hungry creature
  pay 1 gem for a raw crop there, both only while the farm is open.
- **Assumptions to verify:**
  - [x] Bartender restock path: `_restock` (`creature.gd:1233`) -> `bar.supplier`
    (`bar.gd:112`, nearest basket with mixable crops, cached 2 s) -> `bag_from` (`bar.gd:136`).
  - [x] Basket stock is eaten free when tired from hunger (`creature.gd:809, 820-831`), via
    `feed.seek` which takes the drop on the first bite (`feed_coordinator.gd` `seek`).
  - [x] "Stored" = a drop lying at a basket (`dropped_item.gd:28, 128`, `basket.gd:26`).
  - [x] A basket is a Station with a shift (`basket.gd:2`), so the B1 gate covers it.
  - [x] The cook never takes crops from a basket (`kitchen.gd:17-28, 61-66`).
  - [ ] Open: whether the starving free field harvest (`creature.gd:811`) stays (C2's call).
- **Candidates:** M1 the server buys crops at the basket at 1 gem each, the same sale a
  hungry creature makes (survives, pick); M2 the customer's gem is split at the sale and part
  carried to the farmer (cut: F3, needs a carry and a remote transfer); M3 a literal box on
  the basket that holds the gems until the farmer passes (cut: a new noun and saved state; a
  box of gems on a basket also reads as a till the player could throw into, which R6 forbids);
  M4 the farmer walks over to serve each buyer (cut: the user's honesty box, no clerk walk).
- **Recommendation: M1, one basket sale for both buyers.** Scene: the bartender walks to the
  basket, bags 3 carrots, a `💎` hops over the farmer in the field; at night with the farm
  unpaid the basket sells nothing and the bar runs dry. A tired, hungry friend with 1 gem walks
  to the basket, bites a carrot, the farmer shows `💎`; with 0 gems it does not go (C2 picks up
  from there). Mechanism: `buy_at(basket, n * CROP_PRICE)`; the restock bags only what its
  pouch covers.
- **Build sketch:**
  - `creature_config.gd`: `CROP_PRICE = 1`.
  - `Basket.at(pos, tree) -> Basket` (the basket a drop lies at); `Basket.stocks`
    (`basket.gd:26`) becomes `at(...) != null`.
  - `bar.gd:131 _supplies`: also `basket.server() != null`. `bar.gd:136 bag_from(basket,
    worker)`: room capped by `worker.spendable() / CROP_PRICE`; after `job.hold`,
    `worker.buy_at(basket, n * CROP_PRICE)`. Caller `creature.gd:1233` passes `self`.
  - `creature.gd:820 _take_stock_meal`: skip a drop whose `Basket.at` has no `server()` or
    whose price `payer_for` cannot cover (self only: no seats at a basket).
  - `creature.gd:701` Mode.FEED: when `target.node.stored`, re-check the gate each tick (drop
    the target if it closed); on `feed.seek` true, `buy_at(basket, CROP_PRICE)` the same tick.
  - Cook restock (round 2): generalize `_restock(bar)` (`creature.gd:1233`) to a server
    interface both Bar and Kitchen answer: `restocks()`, `supplier(from)`, `bag_from(basket,
    worker)`, `takes(job)`. Kitchen copies the bar's: `restocks()` = `crops == 0`, room
    `Table.MAX_SERVINGS`-sized cap (a `MAX_CROPS` constant), supplier = nearest open basket
    with a `NORMAL` food stack (the kitchen's throw filter, `kitchen.gd:61-66`). Move the bar's
    `supplier`/`_supplies`/`bag_from` up to a shared static helper (2 users now) taking the
    filter. `creature.gd:723`: `var server := Jobs.site_of(self)` as Bar or Kitchen, then the
    same line. Delivery: the cook's carry goes into its kitchen (`add_crops`), as the bar's
    `takes` path does (`creature.gd:716`).
  - Kitchen posting (`kitchen.gd:23-28`): post COOK while `paid()` or `crops > 0`; withdraw
    only when neither. Re-check in `_physics_process` when the sign changes (today posting
    runs only in the `crops` setter).
  - Tally `Basket.sold` (crops sold, all buyers) into `balance_probe.gd` near `:729`.
- **Tests + cheat key:** `test_med_kit.gd:215` becomes
  `test_a_starving_friend_buys_basket_stock_from_the_farmer_on_shift` (pouch -1, farmer +1).
  New in `test_basket.gd`: `test_no_farmer_on_shift_no_crop_sale`,
  `test_a_broke_tired_friend_does_not_walk_to_the_basket`. New in `test_social_bar.gd`:
  `test_a_bartender_pays_the_farmer_one_gem_per_crop_it_bags`,
  `test_a_broke_bartender_bags_nothing_and_a_closed_farm_sells_nothing`. New in
  `test_kitchen.gd`: `test_a_cook_with_no_crops_buys_them_at_the_basket` (cook pouch -n,
  farmer +n, kitchen.crops n), `test_a_paid_empty_kitchen_still_posts_its_cook`. Cheat `/stand`
  (jobs): a paid basket with 6 carrots and its farmer on shift, an empty bar with a bartender
  holding 2 gems, a tired hungry friend with 1 gem.
- **Shared with other clusters:** `Basket.at`; the basket sale is C2's "food on sale" door (a
  broke creature finds it closed to it, so the steal gate fires). Any future hauler (old r6)
  that carries crops is a buyer at the basket through the same `buy_at`.
- **Open questions for the user:**
  1. Closed round 2: the cook restocks (build steps above).
  2. Closed round 2: `💎` at both ends, flagged to the user as a LAW conflict.
  3. Closed (session): thrown crops stay free stock, the player's gift.

### B3: class tuition and the medic fee
- **Frame:** a class and a treatment are served for free today; the player should see a
  student pay its teacher 1 gem per class and a downed patient pay its medic 1 gem per
  treatment, and a broke patient still treated.
- **Assumptions to verify:**
  - [x] The class runs while `_taught` is armed by the teacher's labor (`chalkboard.gd:29-31,
    47-53`); a student sits as at a training place (`chalkboard.gd:39-45`).
  - [x] Chalkboard is TRAIN kind like the library (`chalkboard.tscn:27`, `library.tscn:28`),
    so 18i aspirers are pulled to both (`offer_place.gd:152-154`); the library stays free (R11).
  - [x] Medic works only on shift: WORK fetches a gem first (`creature.gd:718-719`); the
    patient is a site, the medic arrives as `worker` (`creature.gd:2614`).
  - [x] `buy` does not check the buyer's state, so a downed patient can pay.
  - [ ] Open: does a broke student get the class? (pick below: no).
- **Candidates:** U1 tuition per student per stay, broke refused, library the free door
  (survives, pick); U2 per class held, split across students (cut: fractions of a gem, R5);
  U3 tuition per INT point gained (cut: a rate, and a price nobody can read on sight);
  U4 broke students taught free like the medic (survives as the user's alternative: 18i
  aspirers are mostly broke, but they still have the free library). Medic: D1 fee at care
  start, once per treatment (pick); D2 per tend tick (cut: `tends` counts every tick,
  `creature.gd:2629-2631`, so a long care drains a pouch).
- **Recommendation: U1 + D1.** Scene: the teacher writes, three friends with gems sit, each
  pays once as the class starts (`💎` over the teacher); a broke dull friend walks past to the
  library instead. A medic runs to a downed friend and lifts it; the friend's pouch pays 1
  (`💎` over the medic); a broke friend is carried just the same.
- **Build sketch:**
  - `creature_config.gd`: `TUITION_PRICE = 1`, `MEDIC_FEE = 1`.
  - `Chalkboard.server()` (A2). `_paid: Array[Creature]` (transient, like `_drunk`),
    erased in `leave`. `chalkboard.gd:34 draw_for`: 0 unless `c in _paid` or
    `c.payer_for(TUITION_PRICE) == c` (no treat at class). `chalkboard.gd:39 _use`: on the
    first tick, `c.buy_at(self, TUITION_PRICE)` else `leave(c)`; tally `Chalkboard.tuition`.
  - `creature.gd:2621-2628 labor` (TREAT): on the grab and on care starting only,
    `buy_at(Jobs.station_of(worker), MEDIC_FEE)`; the result is ignored (broke still treated).
    Tally `MedKit.fees`.
- **Tests + cheat key:** `test_chalkboard.gd`: `test_a_student_pays_the_teacher_once_per_class_stay`,
  `test_a_broke_student_is_not_pulled_and_the_library_still_is`,
  `test_no_teacher_no_class_no_tuition`. `test_med_kit.gd`:
  `test_a_downed_patient_pays_the_medic_once_per_treatment` (pouch -1 after many tend ticks),
  `test_a_broke_patient_is_treated_free`. Cheats: `/teach` gains gems on 2 of its 3 friends;
  `/medic` gives its downed friend 2 gems.
- **Shared with other clusters:** the gate; the 18i aspire armed by every `buy` now fires at
  the chalkboard and at a downed patient too (side effect of the one transfer, worth a probe).
- **Open questions for the user:**
  1. Closed round 2: broke student refused (U1).
  2. Closed round 2: A2 owns the chalkboard sign.
