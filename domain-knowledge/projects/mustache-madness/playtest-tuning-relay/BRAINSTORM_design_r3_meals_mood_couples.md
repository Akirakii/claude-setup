# BRAINSTORM: design for round R3 + R3b (18e paid meals, 19 mood fertility, couples to bed)

Design only, from main @ c516194a plus the built branches feat/furniture-shop (18f, mm-fixes2)
and feat/pickpocket (18c, mm-fixes). Picks are proposed (round) unless tagged (user). Nothing
was simulated. Payment model: docs/BRAINSTORM_design_payment_model.md "Synthesis" and
docs/HANDOFF_playtest_tuning.md "Payment model picks" (user, 2026-10-22).

## Round 3 changes (2026-10-22)
- 18e follows the user's payment model (user, rules 1-5 below) and reuses R2's interfaces; it
  designs none of them. Cut as moot: the pouch-to-pouch meal sale (`buy(MEAL_PRICE, cook)`),
  the diner -> cook -> farmer chain, the cook's tip per crop, `table.cook`, and the 💎 emote
  fold into `buy` (the sale is R2's path now).
- 18e: broke diners eat free (user, rule 5). 18b's "one gate, no free fallback" does not apply
  to meals or drinks.
- HUD readout re-checked: with spare pouch gems walked to the vault (rule 4), a pouch-only
  total would sit near 0. It now shows pouches + vaults: the gems the herd holds that no sign
  has taken yet.
- 19 and R3b: checked against the five rules, untouched (neither moves a gem).
- Round 2 notes kept below only where still true.

## The user's payment model, as 18e uses it (user, 2026-10-22)
- **Sign:** each workplace's one pay sign. In: the player's gems (1 gem = 60 s open, paid ahead
  with no cap), a buyer's gem while the sign is due, and supplier pay from a sign that uses its
  stock. Out: 1 gem per shift to its worker (wage), and 1 gem per unit of stock it uses to the
  supplier's sign. "Due" = on its last shift with no gem stacked (`station.gd:102-104`).
- **Sale (R2 owns):** in: a buyer, the seller's workplace, a price. If the buyer has the
  spendable gems, they go onto the seller's sign while it is due, else into the serving
  worker's pouch. A broke buyer is served free and nothing moves.
- **Supplier pay (R2 owns):** in: the using workplace, the stock used, the supplier's
  workplace. Out: 1 gem from the user's sign to the supplier's sign per unit. No per-unit
  maker record.
- **Vault deposit (R2 owns):** spare pouch gems are walked to a bank vault. The bank's payer
  carries vault gems to due signs (`till.gd:10-13`), and never opens a closed sign.

### 18e: Paid meals and a herd gem readout
- **Frame:** a dish is the one served good with no price, so a diner's gems never reach the
  kitchen. The player has no herd-level view of the gems the herd holds.
- **Assumptions to verify:**
  - [x] The cook serves into a table, not to a diner: `kitchen.gd:43-51`. The diner eats at
    `chair.gd:34-42`. So the sale happens at the chair, and the seller is the kitchen that
    filled the table.
  - [x] The table does not record which kitchen filled it: `table.gd:13` (`servings` is only
    an int). A table is served by the nearest kitchen in 10 m (`table.gd:11`, `kitchen.gd:48`).
  - [x] The kitchen is already a workplace with a sign (`kitchen.gd:2`, Station). The cook
    takes 1 wage gem per shift (`creature.gd:1212-1219`). Rule 1 is met as it stands.
  - [x] Crops reach a kitchen only by a throw (`kitchen.gd:62-65`, `station.gd:134`). No
    worker carries them in, so the kitchen has no supplier sign to pay yet. Supplier pay fires
    only once R6b haulers (or a cook restock) bring crops from a basket.
  - [x] A dish is not survival food: basket stock (`creature.gd:809`) and a starving harvest
    (LAW_beds rule 2) stay free.
  - [x] Pouches are server-only (`creature.gd:162`, sync list `:310-326`). The vault is
    replicated (`bank.gd:31-35`) and shown on the bank as `💰 n` (`bank.gd:22`). So the HUD
    total is host-only, like the TAB panel (`balance_panel.gd:6`).
  - [x] `Creature.bought` is a probe counter (`balance_probe.gd:752`), so a nightly "spent" row
    is a diff in `dawn_record` (`:1005`).
  - [ ] Open (R2): the name and signature of the sale call and the supplier-pay call. 18e
    builds after them.
- **Candidates (who the diner pays):**
  - K1: the kitchen that served the table, through R2's sale (sign while due, else the cook).
    Survives, and is the user's rule 2.
  - K2: the nearest kitchen to the table at eating time. Cut: a second kitchen built nearby
    would take a sale for a dish it never cooked.
  - K3: the table as its own workplace with a sign. Cut: a table has no worker, so a gem landing
    on it has no shift to pay (rule 1).
- **Candidates (HUD readout):**
  - R1: pouches only. Cut: rule 4 drains pouches to the vault, so it stays near 0.
  - R2: pouches + vaults. Survives. It counts the gems the herd holds that no sign has taken
    yet: what the payer can still use to keep jobs open.
  - R3: R2 + every sign's stacked gems. Cut: the signs also hold the player's own gems, and
    each sign already shows its time.
  - R4: total time paid ahead over all signs. Survives as a fork. It is the productivity number
    ("how long do my jobs stay open"), but a different purpose from R2.
  - TAB "spent" row (gems bought per night): kept. It is flow, while the HUD shows stock.
- **Recommendation:** the scene. Three hungry friends sit at the table and eat. One has gems.
  If the kitchen's sign reads 💎? (due), its gem hops onto the sign and the time ticks up;
  otherwise 💎 pops over the cook. The two broke friends eat free. Later, when crops come in
  from a basket, each crop the cook uses moves 1 gem from the kitchen sign to that basket's
  sign. The HUD reads `💎 12   🪵 30   herd 💎 23`.
  Mechanism: the kitchen stamps `table.kitchen = self` when it serves a dish. `Chair._use`
  calls R2's sale with (diner, `table.kitchen`, `MEAL_PRICE`). `Kitchen.labor` calls R2's
  supplier pay once per crop used, if a supplier is known.
- **Build sketch:**
  - `table.gd`: `var kitchen: Kitchen` (transient; the kitchen that last served this table).
  - `kitchen.gd:47-49`: set `table.kitchen = self` when a dish lands on a table. Call R2's
    supplier pay per crop used.
  - `chair.gd:36-41`: after `try_feed`, call R2's sale. The cook eating its own dish is free.
  - `creature_config.gd:158`: `MEAL_PRICE := 1` (gems a dish costs its diner).
  - Probe: a `Chair.paid_meals` tally, listed in `balance_probe.gd:752`.
  - `run_hud.gd:96-104`: add `herd 💎 %d` (pouch `spendable()` over the friendlies, plus every
    bank's `vault`), on the server only.
  - `balance_panel.gd:10`: a ROWS entry `spent`, plus `dawn_record` key `spent` = the diff of
    `bought`.
- **Tests + cheat key:**
  - `test_job_economy.gd`: `test_a_diner_pays_a_due_kitchen_sign` (sign gems +1, cook pouch
    unchanged), `test_a_diner_pays_the_cook_when_the_sign_is_not_due`,
    `test_a_broke_diner_eats_free`, `test_the_cook_eats_its_own_dish_free`,
    `test_a_thrown_dish_is_free`.
  - Kitchen: `test_a_cooked_crop_pays_its_supplier_sign` (with a known supplier: basket sign
    +1 per dish; with none, no gem moves).
  - `test_run_hud`: the herd total counts pouches + vaults, not loot.
  - `test_balance_probe.gd`: `dawn_record` has `spent`.
  - Cheat: `/restaurant` (`cheat_coordinator.gd:539`) gives 2 of its 3 hungry friends 2 gems
    each and pays the kitchen 1 gem only, so its sign goes due mid-meal and both sale paths
    show.
- **Open forks for the user:**
  - HUD: R2 alone (pouches + vaults), or also R4 (minutes paid ahead)? Recommend R2 now, with
    R4 as a separate readout later.
  - Should the cook restock its kitchen from a basket, as the bartender does (`bar.gd:104-128`)?
    Without it, supplier pay at the kitchen waits for R6b haulers. Recommend wait for R6b: it
    is the general carry route.
  - The HUD wording `herd 💎 23` is invented. Recommend it over `💎 12 (herd 23)`.

### 19: Good mood raises fertility
- **Frame:** a happy herd lays more eggs (user, 2026-10-20). Today only love scales the roll.
- **Assumptions to verify:** all checked in round 1 (`social_coordinator.gd:276-295`,
  `social_formulas.gd:133-142`, `creature_config.gd:76-79,617-620`, `mood_component.gd:9`,
  `LAW_life.md:19-29`). Round 3: no gem path touches it.
- **Candidates:** A, a couple mood factor (picked, floor 1.0, user). B (gate), C (extra
  roll), D (twins) and E (via love) were cut in round 1.
- **Recommendation (user):** `glad = max(0, mood_lean(min of both parents' mood.history))`, and
  the roll is multiplied by `1 + BREED_GLAD * glad`. Below neutral the factor stays 1 (user).
  Chart (fox; loveless / loved):

  | eggs laid | neutral mood | full mood (history 5) |
  |---|---|---|
  | 0 | 0.59 / 1.0 (capped) | 0.89 / 1.0 (capped) |
  | 1 | 0.33 / 0.57 | 0.49 / 0.86 |
  | 2 | 0.18 / 0.31 | 0.27 / 0.47 |
  | 3 | 0.10 / 0.17 | 0.15 / 0.26 |

  `BREED_GLAD` 0.67 makes full mood 1.5x neutral. Estimate, not measured: about +0.5 eggs
  per life.
- **Build sketch:**
  - `social_formulas.gd:139`: add a `glad := 0.0` parameter.
  - `social_coordinator.gd:293`: pass the min of both parents' history.
  - `creature_config.gd:76-79`: add `BREED_GLAD := 0.67` and rewrite the comment.
  - `LAW_life.md` rule 5: mood scales the roll beside love, floored at neutral (user).
- **Tests + cheat key:**
  - `test_breeding_nest.gd`: `test_neutral_mood_leaves_the_roll`,
    `test_full_mood_lifts_it_by_breed_glad`, `test_bad_mood_floors_at_neutral`,
    `test_the_glummer_parent_sets_the_lift`.
  - Cheat `/glad`, then `/dusk`.
- **Open questions for the user:** none.

### R3b: Couples go to bed together
- **Frame:** a couple sleeps on two clocks. The user wants them to turn in together when they
  can (user, 2026-10-21).
- **Assumptions to verify:** all checked in rounds 1-2 (`creature.gd:786-805,887,902,1391`,
  `housing.gd:40,82-102`, `bed.gd:37-49,95`, `job_board.gd:284`, 18f's `bed_of` and parcel
  lines). Round 3: rule 6 sets bought goods by the owner's own bed. The follower picks a bed
  near its mate's, which may not be its own; the goods stay by its own bed. That is R1's
  concern, and its interface is not changed here.
- **Candidates:** S1, the follower reads its mate's state (survives). S2 (invite flag), S3
  (shared sleep need), S4 (waits up) and S5 (joint social action) were cut in round 1.
- **Recommendation:** a mate that is free, not brewing, with sleep at or under
  `COUPLE_BED_SLEEP` 0.5 turns in when its love partner is `_sleeping()`. It takes the mate's
  bed if that has a free spot, else the free bed nearest it. Existing code keeps it in bed
  until full.
- **Build sketch:**
  - `creature.gd:786-789`: `if _turns_in(): return Mode.SLEEP`.
  - `housing.gd:82`: `bed_for(c, near: Creature = null)`.
  - `creature_config.gd`: `COUPLE_BED_SLEEP := 0.5`.
  - `LAW_beds.md` rule 4: add the follow rule (user).
- **Tests + cheat key:**
  - `test_couple_bed.gd`: follows, rested stays up, a working mate keeps working, a friend
    asleep is no call, takes a free spot in its mate's bed.
  - Cheat `/bedtime`.
- **Open questions for the user:**
  - Add a double sleep bed? Recommend not in this PR.
  - Show a sign when the mate follows? Recommend none.
  - Follow line 0.5, or any sleep below 1? Recommend 0.5.

## Merge order
18f with 34 and rule 6 (R1) -> R2 (sign as till, supplier pay, vault deposit, the chalkboard
as a Station, the bartender's wage) -> 18e (it calls R2's sale and supplier pay). 19 can land
at any time. R3b needs only 18f first (it edits lines next to 18f's in `housing.gd` and
`creature.gd`).
