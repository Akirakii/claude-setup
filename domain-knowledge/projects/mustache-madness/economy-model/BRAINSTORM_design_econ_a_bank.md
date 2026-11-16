# BRAINSTORM: cluster A (bank) design, stage 1 economy

Design only. Code read in the worktree `/home/akiraki/Playground/mm-econ` at c516194a. Line numbers
are from that tree.

### A1: cut vault growth and the banker; the payer is paid like any job
- **Frame:** the bank mints gems (a banker grows the vault) and its payer works for free; the
  goal is a bank that only relays the player's own gems to due signs, costing 1 gem per 60 s
  shift of relaying, taken where every worker takes its wage: its own workplace's pile.
- **Assumptions to verify:**
  - [x] Growth lives only in `Bank.labor` + `ticks` + `TICKS_PER_GEM` + `grown` (bank.gd:7-12,99-108).
  - [x] The banker is the `Job.BANK` site posted at the bank itself (bank.gd:36); the payer's
    site is the till, its station the bank (job_board.gd:179-189, `PAY` has `ring`, creature_config.gd:291).
  - [x] Today `Bank.on_shift()` is always true (bank.gd:82) and `paid()` always true (bank.gd:74),
    so the payer never fetches a gem (creature.gd:718) and the till never closes.
  - [x] A worker's wage is `_fetch_gem` -> `punch_in` -> `pouch += 1` (creature.gd:1212-1219,
    station.gd:96-99). Reused unchanged.
  - [x] Every throw, payer return and cop seizure lands in the vault via `Bank.pay` -> `stow`
    (station.gd:196-203, creature.gd:1170-1180, bank.gd:70). Kept: the bank route (user).
  - [x] Any open station seats a worker who burns 1 gem per shift whether or not there is work
    (job_board.gd:215-221; the till site always exists). So an ungated bank drains its vault.
  - [x] A site that closes mid-carry lets its worker finish the delivery (`_unseat` keeps the bag,
    job_board.gd:59-72,101), so gating the bank loses no gem.
  - [x] Hats are not saved (job_component.gd:7; the board re-hats on load). Saves refuse another
    `version` (save_game.gd:5,125; LAW_save.md item 4: bump on any saved-field change).
  - [x] Hat `.tres` files store the job as an int (visor 8, purse_cap 9, bartender_hat 10), and
    `Job.keys()[job]` assumes a dense enum (qa_watch.gd:199,227, creature_job_panel.gd:128).
  - [x] Readers of growth: BalanceProbe `bank_grown` (balance_probe.gd:746), sim `SIM_BANK`
    (headless_sim_driver.gd:34-35,363-368,927-929), probe_guide.md:73-75, TODO_room_types.md:36-37,
    LAW_time_dilation.md:34-35, README.md:92-94. The bot (`_pay_stations`, `_restock`) only pays
    the bank like any station (vault); it never reads growth.
  - [ ] Open: the user's assumption "the bank's own sign counts as a due sign" (F4); see the pick.
- **Candidates (F4: where the payer's wage comes from):**
  - (a) At punch-in the bank moves 1 vault gem onto its own sign; the payer picks it up like any
    worker. The bank opens only while a shift runs, or the vault holds gems and some sign is due. **Survives.**
  - (b) The user's assumption: the bank sign is a due sign, the payer carries a vault gem to it.
    Cut: deadlock (no shift, job closed, no payer to carry the first gem; needs (a) to start),
    the bank is always the till's nearest due sign so it pays itself before anyone, and the walk
    is 0.5 m: a carry no one can see.
  - (c) Two feeders on one object: a throw near the sign pays the bank's hours, a throw on the
    vault feeds the relay. Cut: two targets on one throw is a hidden rule (natural on sight).
  - (d) One pile: the vault is the bank sign's gem stack. Cut: the sign would read "💎 10" as 10
    bank shifts while most go to other signs; the sign lies (black box: a sign reports state).
  - (e) Like (a) but ungated (open whenever the vault holds gems). Cut: the payer burns 1 gem a
    minute with nothing due, so stocking the bank ahead leaks; it fights "paid ahead without limit".
  - Prior art (from memory): Factorio and RimWorld haulers cost upkeep only while hauling;
    Settlers carriers idle for free. A relay that costs only while it relays is the common shape.
- **Recommendation:** (a) gated.
  Scene: the player throws 10 gems on the bank (💰 10). Nothing is due, so the purse cap hangs
  unused. A basket's last shift starts with no gem stacked: a creature puts on the purse cap,
  walks to the bank, 💎 pops, 💰 9, the bank sign shows 💎 0:59. It takes a gem from the till
  (💰 8), walks it to the basket, comes back. When the minute ends and no sign is due, the cap
  comes off and the bank sign goes blank. No banker, no visor, no gem from nowhere.
  Mechanism: the payer is a worker whose station's pile is the vault. Payer pays itself? Yes,
  from player gems (R2 holds), at the same punch-in every job uses; the bank is never `due()`,
  so a payer never carries to it.
- **Build sketch:**
  - `entities/builds/bank/bank.gd`: delete `TICKS_PER_GEM`, `grown`, `ticks`, `labor`, the
    `on_shift` override, `Jobs.post(self, BANK)` (36), `Jobs.withdraw(self)` (113), `ticks = 0`
    (123); `BANK_SAVED := ["vault"]`; delete the PaySign hide (28). New:
    `paid()`: `return wage.paid() or (vault > 0 and Station.due_near(global_position) != null)`.
    `punch_in()`: `if not wage.paid() and wage.gems == 0: wage.pay(take(1))` then `return super()`.
    `_draw_sign()`: `super()`, then `_sign.visible = paid_sec > 0` (guard `_sign`): shift time
    only, never "💎?" (throws feed the vault, so "a gem wanted" would mislead). New tally
    `static var shifts := 0`, `+= 1` in `punch_in` when a vault gem moved. Header: one line
    ("the player's gems wait in the vault; its payer relays them to due signs and takes its own
    shift gem from it, only while a sign is due").
  - `systems/engine/game_enums.gd:8`: drop `BANK`. Renumber `purse_cap.tres:10` 9 -> 8,
    `bartender_hat.tres:10` 10 -> 9. Delete `entities/items/content/visor/` (2 files, no other user).
  - `creature_config.gd:283-290`: delete the `BANK` entry. `creature_inspector_ui.gd:324-325`: delete the case.
  - `save_game.gd:5`: `VERSION := 21` (BANK_SAVED changed). Old saves are refused, per LAW_save; no migration.
  - `balance_probe.gd:746`: `"bank_grown": Bank.grown` -> `"bank_shifts": Bank.shifts`.
  - `headless_sim_driver.gd`: delete `SIM_BANK` (doc 34-35, 363-368, 927-929); SIM_PAY line 931
    prints `handed=%d shifts=%d paid=%d`.
  - `cheat_coordinator.gd`: delete the `bank` cheat (`KEY_V` at 30, help 187, body 494-505);
    `pay` help (188): "...a payer (INT 8) that takes its shift gem from the vault".
  - Docs: README.md:92-94 (bank: gems wait in the vault, payer relays to due signs and takes 1 gem
    per shift from it only while one is due; sign shows the shift), README.md:179 `/jobs pay`;
    LAW_time_dilation.md:34-35 drop the vault growth entry; probe_guide.md:73-75 swap to
    `bank_shifts` (compare with `pay_handed`: gems relayed per gem of upkeep); TODO_room_types.md:36-37 delete.
  - Reused as is: `Station.punch_in`, `Wage`, `_fetch_gem`, `Till.labor`, `due_near`, the board's
    `_open`/`_unseat`, `with_loot` (thefts), seizure delivery.
- **Tests + cheat key:**
  - test_bank.gd: delete the 4 growth tests (64-100) and 2 banker tests (48-61); drop `ticks`
    from `test_the_vault_is_saved`; `test_every_gem...` drops `assert_true(bank.paid())`. Add
    `test_a_bank_opens_only_to_relay` (vault 0 + due: false; vault 5 + none due: false; vault 5 +
    due woodpile: true; shift running + vault 0: true), `test_the_payer_takes_its_shift_gem_from_the_vault`
    (vault 5, `punch_in()` true, vault 4, `on_shift()`, `wage.gems == 0`, `Bank.shifts` +1),
    `test_an_empty_vault_pays_no_shift` (`punch_in()` false), `test_the_sign_shows_only_a_shift`.
  - test_payer.gd: `test_a_bank_needs_no_pay_to_seat_a_payer` (100) -> `test_an_empty_vault_seats_no_payer`;
    add `test_nothing_due_seats_no_payer`; add `test_a_payer_fetches_its_wage_then_hands` (`_fetch_gem(bank)`:
    pouch +1, vault -1; then `till.labor`: vault -2, carry 1).
  - test_police_box.gd:332: its control needs a due woodpile beside the bank, else the till is closed.
  - Cheat: `Y` (`/jobs pay`): bank with 10 gems, a basket 30 s from unpaid, a payer.
- **Shared with other clusters:**
  - Buy gate (B owns): it reads `Station.on_shift()`. A1 makes the bank's honest (it was always
    true); the bank sells nothing, so A1 adds no gate.
  - Save `VERSION` bump: B and C also change saved fields; give one owner the rule "each PR that
    changes a SAVED list bumps by 1 on the stack".
  - `GameEnums.Job` renumber: any stacked PR adding a job or a hat `.tres` must build on A1's numbering.
  - "Open only while there is work" gate in `paid()`: if another job gets an always-present site
    (a basket clerk, a hauler), it needs the same shape; name it then, not now (1 user).
- **Open questions for the user:**
  - F4: the payer takes its shift gem from the vault at punch-in (recommended), instead of
    carrying it to the bank's own sign (your stated assumption)? Same gems, no deadlock.
  - Relay only while a sign is due (recommended) vs payer on whenever the vault holds gems
    (1 gem a minute even with nothing due)?
  - Invented interface detail: the bank's sign shows only the shift's m:ss, and is blank between
    shifts (no "💎?"). OK?

## Round 2 changes
A1 picks accepted by the session (vault wage at punch-in, relay only while due, A1 owns
`VERSION := 21`); the blank bank sign stays a user question. Merge order stays A1 then A2: A1 overrides the
Station API as it is today; A2 moves that API to `GridObject` and changes `Bank.punch_in` to
the new `punch_in(worker)` signature in the same diff.

### A2: the bar and the chalkboard are paid workplaces
- **Frame:** the bartender and the teacher work for free because their pieces are not
  Stations (`Bar`, `Chalkboard` extend `OfferPlace`); the goal (user, 2026-10-21) is the same
  pay sign, thrown gem, 60 s shift and punch-in wage as every workplace, so no gem, no bar, no class.
- **Assumptions to verify:**
  - [x] The whole pay layer is on `Station` (station.gd:9-10,21-31,47-54,57-104,107-109,118-123,
    186-203): `wage`, sign, sync, `pay/paid/on_shift/punch_in/due`, `pay_with`, `due_near`.
  - [x] `Bar` and `Chalkboard` extend `OfferPlace extends GridObject` (bar.gd:2, chalkboard.gd:2,
    offer_place.gd:2); 4 scripts extend OfferPlace. GDScript has one parent: they cannot also be Stations.
  - [x] Every pay caller is typed `Station`: job_board.gd:180-189 (`station_of`), 220 (`_open`),
    creature.gd:714-719 (fetch gem), 1155, 1173-1174, 1212, 1244 (`_walk_to`), till.gd:11,
    dropped_item.gd:182 (`pay_with`), sim 590,601, cheat 792.
  - [x] Today `_open` treats a non-Station site as always open (job_board.gd:220), and
    `station_of` returns null for a bar or board (189), so their workers never fetch a gem.
  - [x] Bar serves and mixes only in `labor` (bar.gd:63-81), and a worker labors only on shift
    (creature.gd:718-731); so a shift gate on the job gates sales with no new check.
  - [x] `Bar.open` holds while the bartender keeps the site and is awake (bar.gd:87-93), which
    includes the walk back to punch in. Drinkers are pulled while `open` (bar.gd:159).
  - [x] `GridObject` already adds an opt-in child node per piece in `_enter_tree` (RoomSign +
    WalkSync, grid_object.gd:32-45): repo precedent for an opt-in layer at this altitude.
  - [x] `GridObject` defines no `_physics_process`; adding one would wake every block. Station
    and OfferPlace each have one (station.gd:62, offer_place.gd:250).
  - [x] LAW_save Field marking 1-2: a var lives in the lists of the script that declares it;
    test_forgotten_fields enforces it.
  - [x] The sim bot pays only `Station.GROUP` (headless_sim_driver.gd:587-592 `_pay_stations`,
    599-601 `_restock`); the care policy places a bar (681). So today the bot never pays a bar.
  - [ ] Open: a worker swapped in mid-shift never punches in, so `shift_worker` is stale until
    the next shift (see Shared).
- **Candidates:**
  - (a) Lift the pay layer to `GridObject`, opt-in by `wage != null` (Station, Bar, Chalkboard
    create one in `_init`); a `GridObject.PAID` group for `pay_with`/`due_near`. **Survives:** one
    copy of the path; GridObject is the lowest common parent of all three users.
  - (b) A `PayPost` child node (component) on each paid piece. Cut: callers need owner-level
    `paid()` so the Bank gate override still works, so each of 3 owners re-declares 6 delegates
    and the setup lines: 3 copies of one path.
  - (c) `OfferPlace extends Station`. Cut: every bed, chair and gym joins `Station.GROUP` (rings,
    `taking`, stacks) and gets a wage it must switch off; `GROUP` constants clash.
  - (d) Bar and Chalkboard become Stations with an OfferPlace component. Cut: rewrites the seat
    logic all 4 places share.
  - (e) Copy the wage code into Bar and Chalkboard. Cut: 3 copies.
  - Prior art (from memory): Godot docs favor composition (b) for behavior many unrelated nodes
    share; here the users already share one parent and the repo's RoomSign uses opt-in on that parent.
- **Recommendation:** (a).
  Scene: the player builds a bar; it shows 💎? and stays dark. A thrown gem lands on it (💎 1);
  a creature puts on the bartender hat, walks over, 💎 pops (its wage), the sign reads 💎 0:59,
  drinks pour. At 0:00 with no gem it hangs up the hat; the bar goes dark, drinkers get up. The
  chalkboard does the same with the mortarboard: no gem, no class. The bank's payer feeds a bar
  or board on its last shift like any sign.
- **Build sketch:**
  - `systems/grid/grid_object.gd`: move from station.gd: `PAY_RADIUS`, `PAY_HEIGHT`,
    `SIGN_HEIGHT`, `var wage: Wage = null` (SAVED), `paid_sec`/`paid_gems` with setters, `_sign`
    (DERIVED), new `shift_worker: Creature = null` (TRANSIENT), `_draw_sign`, `_show_paid`, `pay`,
    `paid`, `on_shift`, `punch_in`, `due`, `_holds`, `pay_with`, `due_near`. Defaults with no wage:
    `pay` returns all gems, `paid`/`on_shift` true, `punch_in` false, `due` false. `punch_in(worker:
    Creature)` sets `shift_worker = worker` when it took a gem. New `const PAID := &"paid_post"`;
    `_enter_tree`: `if wage and not has_node(^"PaySign")`: add the sign + PaySync (the RoomSign
    pattern), `add_to_group(PAID)`. New `func _tick_pay(delta)`: `wage.advance` + `_show_paid`.
    `_yeet_drops` (187): `if wage`: leave PAID, spill `wage.refund()`, `_show_paid()`. A generic
    `static func by_distance(pos, group, test) -> Array[GridObject]`; Station's `_by_distance`
    `assign`s from it (no second sort loop).
  - `station.gd`: `_init()`: `super()`; `wage = Wage.new()`. `_physics_process` calls `_tick_pay`.
    `STATION_SAVED := []`, `STATION_DERIVED := []`. Delete the moved code and the sign build in `_ready`.
  - `bar.gd`, `chalkboard.gd`: same `_init`. `offer_place.gd:250`: after the server check,
    `if wage: _tick_pay(delta)`. `bar.gd:87`: `open` also needs `on_shift()` (no pull between shifts).
  - `job_board.gd:180-189`: `station_of -> GridObject`, `if site is GridObject and site.wage: return
    site`; 220: `not site is GridObject or (site as GridObject).paid()`.
  - `creature.gd`: `_fetch_gem(station: GridObject)` passes `self` to `punch_in`; `_walk_to` takes
    and returns `GridObject`; in `_deliver_carry` cast the `taking` result `as Station` for
    `accepts`/`add_stack`. `till.gd:11`, `dropped_item.gd:182`: `GridObject.due_near`/`pay_with`.
  - `save_game.gd:5`: `VERSION := 22` (GridObject gains a SAVED field; Bar and Chalkboard save a wage).
  - Sim bot: `_pay_stations` and `_restock` iterate `GridObject.PAID` (bars and boards get paid).
  - Cheats: `bar` (O), `leisure`: `bar.pay(2)` after placing; `teach` (T): `board.pay(2)`;
    `spawn_paid` returns `GridObject`. Help lines say "paid".
  - Docs: README bar and chalkboard bullets (gem sign, shift, wage), creature_config.gd:275
    comment ("unpaid, like the bartender") goes.
- **Tests + cheat key:**
  - test_social_bar.gd `_bar` helper: `bar.pay(1)` before `Jobs.request`. New:
    `test_an_unpaid_bar_seats_no_bartender`; `test_a_gem_on_the_bar_pays_its_bartender_a_shift`
    (`_fetch_gem(bar)`: pouch +1, `on_shift()`, `shift_worker == tender`, `wage.gems == 0`);
    `test_a_bar_closes_when_its_shift_ends_with_no_gem` (advance 60 s, `Jobs.tick`: job off, `open` false).
  - test_chalkboard.gd: `test_a_board_takes_a_smart_teacher_with_no_station_or_gem` (61) becomes
    `test_an_unpaid_board_seats_no_teacher` + `test_a_paid_board_seats_a_smart_teacher`;
    `_board` helper pays 1; `test_a_teacher_takes_a_shift_gem_as_its_wage`.
  - test_payer.gd: `test_a_payer_carries_a_gem_to_a_due_bar`.
  - test_broken_station.gd:71: assert the bar's stacked gems spill too.
  - test_save_game.gd: `test_a_bar_keeps_its_paid_time_on_load` (gems + window left).
  - test_job_economy.gd: a blocked piece (no wage) stays open (`paid()` true, `pay(1)` refused).
  - Cheats: `O` (`/rooms bar`) and `T` (`/jobs teach`) start paid.
- **Shared with other clusters:**
  - B's buy gate: A2 owns the base `GridObject.server()`: `shift_worker if on_shift() and
    is_instance_valid(shift_worker) and Jobs.station_of(shift_worker) == self else null`. B owns
    the Bar (`_bartender if open`) and Chalkboard (`_teacher` while the class is on) overrides.
    Edge: a worker swapped in mid-shift does not punch in, so `server()` is null until the next
    shift (at most 60 s with no sales). Fine, or have `_fetch_gem`'s on-shift branch also set it?
  - The pay API moves from `Station` to `GridObject`: A2 updates A1's `Bank.punch_in` signature;
    any B or C code typed `Station` for pay builds on A2's types.
  - `VERSION`: A1 21, A2 22; each later PR that changes a SAVED list adds 1.
- **Open questions for the user:**
  - A bar or chalkboard with no gem stands closed (no drinks, no class) like any workplace.
    Recommended: yes, as your 2026-10-21 decisions say. It makes early fun and INT growth cost gems.
