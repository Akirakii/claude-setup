# BRAINSTORM: c4 businesses (PR 6 founders, PR 7 rent, PR 8 more shops)

AFK relay design, 2026-10-25. Every pick is Claude's unless tagged (user). Code refs are the
worktree mm-stage2 at 86fc5fb7 (main + PR 1 work, nothing of PR 2-5 yet). Shared model:
`/tmp/claude-layers/stage2.md` (framing B, money circuit). c4 owns flags F1, F2, F4, F5, F8,
F14, F19.

## Round 2 changes (2026-10-25)
- Picks (Claude, AFK): founder slot bought with gems allowed; stock money from the till, unspent
  change stays with the server; rent per lie-down; gift shop the one new shop; logs as stock.
- c2 picked a paid site (the player pays the site crate's sign), so PR 7's landlord source exists.
- Rename: my founder predicate is `foundable()`, not `sells()` (c3's `Station.sells()` means "a
  supplier that charges", Basket only). Bar, Kitchen, Shop: `foundable()` true.
- Handover (PR 7 owns, edits c2's `site.gd`): Site inherits PR 6's `proprietor` and `till` from
  GridObject; in Site builder labor, on the pieces `NetworkManager._place_laid([entry])` returns
  (the same loop that sets `creature_built`), a `Bed` gets `proprietor = self.proprietor`. Founder
  target adds `Site.foundable()` = every entry of `anchors` is a Bed and `anchors.size()` <=
  RoomSkins.BEDROOM_BEDS. No done-time hook needed.
- PR 8 stock uses c3's contract (PR 4 merges first): Shop `wants(LOG)` = `stock_room()`, the
  clerk fetch is `Carry.source_for(from, self, is_log, true)` then `source.hand(worker, LOG, n)`,
  like the kitchen after PR 4. Logs are free (c2 pick b): Woodpile `hand` is a free take. So
  PR 8 moves nothing: no `sell_into` move, no LOG_PRICE (PR 4 is the only mover). Haulers fill
  the shop by the same `wants`.
- PR 6's float reads `stock_room()`; after PR 4 that equals the stocker's `wants(meta)`: use
  `wants` (one name), the float = `wants(meta) * CROP_PRICE` for crop stockers, 0 for logs.
- Save VERSION: every bump here is "stack top + 1 at build time" (PR 3 sets 24, PR 10 gear later).
- Questions logged for the user, not changed by this run: main B1 turns the broke away unless
  treated vs r1 rule 5 "broke drink free" (user); the sign cap 4 (an earlier run's Claude pick on
  main) vs the MEMORY pre-pillar "paid ahead without limit (user)".

## Round 3 changes (cold review, 2026-10-25)
- SEVERE fix: only pieces with a wage join PAID (grid_object.gd:11, :65), so a Bed was never
  found. New group `GridObject.OWNED := &"owned"`: the `proprietor` setter joins it when set and
  leaves it when cleared. `held_by(c)`, the owner visit scan and "holds no piece" scan OWNED;
  the founder's target scan stays on PAID (only workplaces and sites are founded).
- Founder-funded site gems: a site that finishes or breaks spills its stacked sign gems on the
  floor (grid_object.gd:336-338), a player pickup. PR 7 edit: with a valid proprietor, those
  gems go to the till of the first Bed it laid instead (no bed laid yet: they drop as today).
- Rent once a day: Bed gets `rent_day` (saved int, -1), stamped with
  `LevelManager.day_cycle.cycle_index()` when rent is paid (the punch-day pattern,
  grid_object.gd:366-370). A lie-down pays only while `rent_day != cycle_index()`, so a sleeper
  that rises and lies down again the same night pays once (creature.gd:982-988).
- `buy(price, seller, into)`: `into` replaces the seller test (a till takes gems with no
  creature on its feet) rather than skipping past it; the aspire block stays one copy after it.
- A bed laid while the player paid the site, before a founder funds it: accepted, stays
  unowned (free). The player's gems built it, so it is the player's room, not the founder's.

## Frame (all three PRs)
One concept carries the cluster: the **proprietor**, a creature that holds the funder slot of
a piece (the slot the player holds today when it throws gems on a sign), plus that piece's
**till**, the gems buyers leave at it for the proprietor to collect in person. A shop owner
(PR 6), a landlord (PR 7) and the shops of PR 8 are the same slot on different pieces.

Pre-pillar proposals (unconfirmed, for the user's audit):
- PRE-PILLAR 1: a creature may hold any funder slot the player may hold, with the same pay
  verb and the same sign cap; it never gets a slot the player cannot pay (so a gem still only
  decides which workplaces stand open, never who works there).
- PRE-PILLAR 2: a gem a buyer pays at an owned piece waits at that piece (the till) until its
  proprietor walks there; no gem moves to a creature that is not standing there.

## Flag answers (c4 owns)
- F1, one price path: a founder pays its sign with the same `GridObject.pay` the thrown gem
  uses (grid_object.gd:101); gems per open hour (Wage.GEM_SEC 60 s, wage.gd:11). No lump capital.
- F2, sign cap: the cap is per sign, `Wage.MAX_GEMS` 4 stacked gems (wage.gd:12); there is no
  cap on the number of signs. A founder's sign has the same cap; the question "does it eat the
  player's slots" does not arise. The player may still throw gems on an owned sign (a gift).
- F4, wage payer: one payer, the sign. The worker takes the shift gem at punch-in
  (creature.gd:1327) whoever filled the sign.
- F5, sale payee: an unowned piece pays its server on shift (stage 1, creature.gd:1156); an
  owned piece pays its till, still only while a server is on shift (user: "customers pay the owner").
- F8, room owner: a Bed piece gets a proprietor when a founder funded the site that built it (PR 7).
- F14, bankruptcy leftovers: none by construction (the proprietor gives up only at a visit
  where the sign is due, so 0 stacked, and it has just taken the till). A dead proprietor's
  slot clears; its pouch goes by the heir rule (creature.gd:1650); the till stays on the piece.
- F19, full pouch: `spendable() >= FOUND_GEMS`, with `FOUND_GEMS := Wage.MAX_GEMS` (enough to
  fill one sign). No pouch cap is added. Loot never counts (creature.gd:1139-1145 reads spendable).

### PR 6: Creature businesses
- **Frame:** the player builds more workplaces than it can pay for; a creature with a full
  pouch sees a dark one where buyers are, funds its sign, and the shop runs on its gems until
  sales keep it or it goes broke and closes.
- **Assumptions to verify:**
  - [x] A sign is a per-piece stack, cap 4, a gem = one 60 s dilated shift (wage.gd:11-12, 27-31).
  - [x] The shift gem is the worker's wage at punch-in (creature.gd:1322-1330).
  - [x] A sale pays the server on shift, none = no sale (creature.gd:1155-1157, grid_object.gd:147-153).
  - [x] Servers buy stock from their own pouch (basket.gd:65-80, bar.gd:127-129, creature.gd:1344-1350).
  - [x] Who works a station comes from the job board by INT gate (creature_config.gd:234-315); no hire verb exists.
  - [x] A walk-to-a-spot-and-take-gems mode exists (Mode.INHERIT, creature.gd:843-846, 1629-1647).
  - [x] No pouch cap exists (grep POUCH: none).
  - [ ] Open: c3's job-from-stats rule (PR 3) leaves the job board as the only way a worker is
    matched to a site. Assumed yes.
- **Candidates:**
  - T1 a founder takes the funder slot of a dark, unowned, player-built workplace that sells,
    picked by buyers nearby; sales to a till it collects. **Survives.**
  - T2 the founder asks the architect for a shop zone (PR 2). Cut for now: needs PR 5 zone
    types and a site per shop; the skeleton would span 3 PRs. TODO.
  - T3 the founder sets down a counter it buys in an empty room (18f parcel path). Cut: the
    counter's price goes to a sink (breaks the closed circuit) or needs logs carried (c3). TODO.
  - T4 owner-operator only: it works its own shop, no till. Cut: its wage gem returns to
    itself, so founding costs nothing and can never fail; "hires" is empty.
  - T5 sales pay the sign (self-funding shop). Cut: a customer would open a workplace (user rule).
  - Field: Majesty (heroes with purses spend at the player's buildings), The Sims 2 Open for
    Business (an owner funds wages, the register is the owner's money); from memory.
- **Recommendation: T1.** Scene: the player built a bar and left it dark. Mo (6 gems) roams,
  walks to the bar, 🎩 pops, 4 gems hop onto the sign ("💎 4", under it "🎩 0"). Bo (INT 9)
  takes the bartender job from the board and punches in. Pip pays a drink: the gem hops onto
  the counter, "🎩 1". The bartender, out of crops, takes 2 gems from the counter and walks to
  the farm. When the sign is down to its last shift, Mo walks back, takes the counter's gems,
  tops the sign up. A later Mo with nothing left arrives, 💸, and leaves; the shift ends dark.
  Mechanism: one rule for every visit (found, refill, give up), `_tend(piece)`:
  1. unowned and dark: become proprietor, take the till (a previous owner's), pay
     `min(spendable, MAX_GEMS)`; 2. own piece: take the till into the pouch; if `due()`, pay
     what fits; if it paid nothing while due, the slot clears (bankrupt).
  Founder test (pure read, on a FOUND_SCAN_SEC dilated cooldown): FRIENDLY, free time
  (ROAM/BREAK), holds no piece, spendable >= FOUND_GEMS; target = unowned piece with
  `foundable()` and not `paid()` that has the most friends within FOUND_RADIUS holding a gem
  (founder excluded, at least 1), nearest on ties. Owner visit test: its piece `due()` or
  `till >= Wage.MAX_GEMS`.
- **Build sketch:**
  - systems/grid/grid_object.gd:7-9: SAVED += "proprietor", "till" (proprietor saved like
    `Bed.owner_creature`, bed.gd:17-23). New `var proprietor: Creature`, `var till := 0`,
    `func foundable() -> bool: return false`, `func take_till(n) -> int`, `static func held_by(c)`
    (scan PAID group). Sign (grid_object.gd:90-92 `_draw_sign`, wage.gd:68-73 `sign_text`):
    a second line `🎩 <till>` while owned (replicate `owned_till` like `paid_gems`).
  - Bar, Kitchen: `foundable()` true. Not Basket (a founder-funded gem bush farm would pump
    player gems), not Chalkboard (tuition payee is c3's, F7), not Bank.
  - creature.gd:1139 `buy(price, seller, into: GridObject = null)`: gems to `into.till` when
    given, else to the seller; the aspire block stays one copy. :1156 `buy_at`: pass `place`
    as `into` when `place.proprietor` is valid. Sales still need `server()`.
  - creature.gd:784 (restock decision, the worker stands at its site): at an owned stocker,
    `pouch += stocker.take_till(stocker.stock_room() * CROP_PRICE)` first (the float); Bar
    `stock_room()` = `_crop_room()` (bar.gd:109), Kitchen = MAX_CROPS - crops (kitchen.gd:59).
  - creature.gd:7-22 Mode += TEND; `_decide_mode` (:818) after the INHERIT block (:843): TEND
    when the visit or founder test holds; `_tend_tick` walks with `_walk_to` (:1355) and runs
    `_tend`. Death and leaving (`_spill_pouch`, :1650): clear `proprietor` on its piece.
  - creature_config.gd near :172: `FOUND_GEMS := Wage.MAX_GEMS`, `FOUND_RADIUS := 12.0` m,
    `FOUND_SCAN_SEC := 5.0` dilated, `OWNER_GLYPH := "🎩"`, `BROKE_GLYPH := "💸"`.
  - Probe (balance_probe.gd): `founded`, `bankrupt`, `till_gems` tallies. Save VERSION +1
    over the stack top. Knock-down refund (wage.gd:43-48 callers) also drops the till.
- **Tests + cheat key:** test/ci/entities/creatures/test_founder.gd:
  `test_a_founder_with_a_full_pouch_pays_a_dark_bars_sign` (proprietor set, paid_gems 4,
  founder pouch -4); `test_a_founder_picks_the_dark_bar_with_buyers`;
  `test_a_founder_never_takes_a_paid_or_owned_piece`; `test_a_sale_at_an_owned_bar_goes_to_its_till`
  (server pouch unchanged, till +1); `test_the_owner_collects_its_till_and_tops_up_its_sign`;
  `test_a_broke_owner_gives_up_and_the_bar_goes_dark` (proprietor null, `paid()` false after
  GEM_SEC); `test_loot_never_founds_a_shop`. Cheat `/founder` (folder "jobs"): a hut with a
  dark bar, an INT 10 friend, 3 friends with 2 gems each, a founder with FOUND_GEMS + 2 gems.
- **Shared with other clusters:** hiring = c3's job board rule, unchanged (F17: the founder
  never picks its worker); the proprietor slot and till are reused by PR 7 (rooms), PR 8
  (shops), and c2 if a creature may fund a site (F3); c5: loot never enters a sign, a till or
  rent (spendable only), so the stolen mark needs no carry through these flows (F15).
- **Open questions for the user:**
  1. The founder role is bought with gems (bends "roles from raising"). Pick: allowed, since
     the slot is only the funder slot the player already holds (pre-pillar 1); the worker
     still comes from its own stats.
  2. The stock float: the server takes stock money from the counter when it sets out. Pick: yes;
     the change it does not spend stays with it (goofy, keeps one payer path).

### PR 7: Rent
- **Frame:** a private room should cost its sleeper something once a creature paid to build
  it; the player sees rich creatures in Bedrooms paying a landlord, broke ones in the free
  bunkhouse.
- **Assumptions to verify:**
  - [x] Bedroom = 1-2 beds, Bunkhouse = 3+ (LAW_room_types.md:12, user; RoomSkins.BEDROOM_BEDS 2).
  - [x] `Bed.owner_creature` is the sleeper, set by Housing (bed.gd:17-23, housing.gd:112-136),
    so the landlord needs its own field (the proprietor of PR 6, on the Bed piece).
  - [x] Housing.assign is pure and keeps owners first (housing.gd:216-258); `bed_for` claims
    free beds at sleep time (housing.gd:82-104, creature.gd:984).
  - [x] c2 round 2: the site is a paid Station (crate sign), lays through `_place_laid`, which
    returns the pieces; its `anchors` list holds the room anchors before anything is built.
- **Candidates:**
  - L1 a founder funds a dark site whose ghost is a Bedroom; the built beds carry it as
    proprietor. **Survives** (capital pays builders, then owns the result).
  - L2 a founder claims a finished, player-built Bedroom for free. Cut on the scene: the room
    the player built for its herd is taken and charged for, with nothing paid by the taker.
  - L3 the founder buys the room from the player (gems drop at the door for the player). Cut
    here: a new player income from creature pouches is F16 (c6's tax and trade test).
  - L4 a creature that buys a bed at the furniture shop owns it (rule 6). Cut for now: needs
    beds as a home good (PR 8 and later); TODO.
  - L5 the oldest sleeper of a 2-bed room charges the other. Cut: no capital, a free rent claim.
  - Field: Dwarf Fortress 0.31 rent on basic needs made miserable homeless dwarves (memory),
    so the free bunkhouse floor (user) is the guard.
- **Recommendation: L1.** Scene: the player marks a one-bed zone and pays nothing. Mo (5
  gems) walks to the site sign, 🎩, the builders hammer on Mo's gems. The hut ends with Mo's
  🎩 on its bed. Pip (works, 3 gems) is housed there; at night it lies down, a gem hops onto
  the bed ("🎩 1"). Broke Bo is moved to the bunkhouse at the next reassign. After 4 nights
  Mo walks over and takes 4 gems. Mechanism: rent = RENT_PRICE at lie-down, once a day (`rent_day`, Round 3; one pay a
  day, Round 3), into the bed's till, from any sleeper that is not its proprietor, only
  in a Bedroom; a sleeper short of it may not own or use that bed. The proprietor's visit is
  PR 6's rule (`till >= Wage.MAX_GEMS`; a bed is never `due`, so a landlord never goes bankrupt).
- **Build sketch:**
  - Founder target (PR 6 `_tend`) also takes an unowned dark site with 1..BEDROOM_BEDS beds in
    its `anchors` (`Site.foundable()`, Round 2). Each Bed the builder lays copies the site's
    `proprietor` (Round 2 handover, in PR 7).
  - systems/housing/housing.gd: `static func rented(b) -> bool` = valid proprietor and the
    room's bed count <= RoomSkins.BEDROOM_BEDS (count from `_room_key`, :170-175);
    `may_pay(c, b)` = not rented, or c is its proprietor, or spendable >= RENT_PRICE.
    `assign` (:218) gets an optional `may_own: Callable` used in the keep pass (:223-227) and
    in `_bed_near_close`; `reassign` passes `may_pay`. `may_use` (:61) and `bed_for` (:82)
    also require `may_pay`.
  - Lie-down (the sleep path that calls `Housing.bed_for`, creature.gd:984): if rented and not
    its own, `buy(RENT_PRICE, null, bed)` (PR 6's `into` path, seller check skipped for a
    till), emote 💎. Bed sign: Bed has no Wage; add a Label3D "🎩 <till>" while owned.
  - creature_config.gd: `RENT_PRICE := 1`. Probe: `rent_paid` tally, `rented_beds` gauge.
- **Tests + cheat key:** test/ci/systems/housing/test_rent.gd:
  `test_a_tenant_pays_rent_into_its_bed_and_the_landlord_collects` (tenant pouch -1, landlord
  pouch +1 after the visit: the Done line); `test_a_bunkhouse_bed_is_free_even_when_owned`;
  `test_a_broke_creature_is_not_given_a_rented_bed`; `test_the_landlord_sleeps_free`;
  `test_a_built_bedroom_carries_its_funders_proprietor` (Site labor copies it). Cheat `/landlord`
  (folder "rooms"): a 1-bed hut owned by a landlord, a tenant with 3 gems, a broke friend,
  and a 3-bed bunkhouse; `/night` shows the gem hop and the broke one in the bunkhouse.
- **Shared with other clusters:** c2: site as a paid piece, its ghost's bed count, and a
  handover hook (F3, F8). c6: land purchase (L4 in the ledger) may later become a second
  landlord source; it must reuse the proprietor slot, not a new owner field.
- **Open questions for the user:**
  1. none (rent: at lie-down, once a day, Round 3).

### PR 8: More shops
Review of `feat/furniture-shop` (mm-fixes2, b6ee3c20 + 32fd0710, base 269839c5).
- **What it does:** a `Shop` OfferPlace (Kind.SHOP) where a friend with 5 gems whose room has
  fewer than FURNISH_MAX (2) pieces buys a lamp; it carries it home (📦 glyph, `parcel`,
  saved) in free time and sets it on a free wall cell of the room it sleeps in (`Shop.unpack`);
  the 5 gems drop on the counter for the player. Housing counts pieces per room
  (`room_pieces`, group "furniture" on table, chair, lamp). `Creature.spend` split out of `buy`.
- **Scene today:** Pip with 10 gems walks to the green counter, gems pop onto the counter, 📦
  over Pip, Pip walks to its bunkhouse bed and a lamp appears by the wall. The player scoops
  the 5 gems.
- **Gaps vs the pillars and current main:**
  1. Counter gems go to the player: a player income from creature buys (F16 test) and against
     main B1 "a sale pays whoever sells at the place now; none, no sale".
  2. No worker, no sign: the only workplace with no shift, against the stage 1 rule that a
     workplace is paid by the shift.
  3. The lamp is minted; every other good on main is made from bought stock (B2).
  4. Rule 6 (user) not met: a sharer buys for a bed not its own (`Housing.bed_of` falls back
     to a close owner's); the good has no owner; 📦 glyph, not the good "carried over the head"
     (user); no use seen (the lamp lights by the first-8 rule, not by its owner).
  5. `clear_footprints` in `unpack` duplicates #370 (spawn_grid_object pushes creatures out).
- **Rebase plan (main is 2 commits ahead: #370, #371):** do not rebase in mm-fixes2; on the PR
  7 branch top in mm-stage2, cherry-pick both commits and resolve: creature.gd SAVED keep
  "reported" and add "parcel"; drop the `spend()` split (the shop sells through `buy_at`);
  creature_config.gd: main renamed ASPIRE_RADIUS to SEE_RADIUS, add the 4 shop constants after
  it; offer_place.gd: Kind += SHOP, `visits` gets a sixth 0; save VERSION = stack top + 1;
  README, cheat_coordinator HELP/arms, balance_probe, blueprint_registry,
  headless_sim_driver: keep both sides. Then one rework commit (below).
- **Candidates (which shops):** barber (a mustache style): TODO, the mustache is the stat
  readout today (stats_component.gd:118-130), a style needs a worn-item look first ("Worn
  items: later", user). **Gift shop: survives**, a gift carried over the head to the friend it
  knows best jumps that bond (economy to bonds to bed sharing and couples: a new connection).
  Arcade: cut, same purpose as the bar (fun). Spa: cut, same purpose as comfort seats (the
  brewer cure). Lottery: cut, a resource-pile reward with no board change. Pawn: cut, a gem
  source outside gem bushes (rule 10) and there are no found items.
- **Recommendation: furniture shop on the stage 1 economy + gift shop as a second good of the
  same Shop.** Scene: the player pays the shop sign; Mo (INT 8) dons the clerk cap. Pip (own
  bed, 6 gems) buys a lamp: gem to Mo (or the till if a founder owns it), the lamp's mesh
  rides over Pip's head to Pip's own bed; at night Pip lies down and the lamp glows, dark when
  Pip gets up. At a second counter (gift kind) Bo buys a gift, carries it over its head to Kit,
  ❤ pops, their friendship jumps by GIFT_BOND. Mechanism: `Shop` gets a Wage, posts Job.SELL,
  sells through `buy_at` (server or till); stock = logs (LAMP_LOGS 3, GIFT_LOGS 1) bought like
  the bar's crops; `good` per counter (lamp: home good, gift: friend good).
- **Build sketch:** entities/builds/shop/shop.gd: `_init` wage = Wage.new(); `_ready`
  Jobs.post(self, Job.SELL); `foundable()` true; `_use` = `c.buy_at(self, price)` then parcel;
  stocker as the kitchen after PR 4: `wants(LOG)`, `Carry.source_for`, `source.hand`
  (Round 2; logs free, nothing moved here). game_enums.gd:8
  Job += SELL (append); creature_config.gd JOBS += SELL (req_int 8, interval 3.0, reach 1.8,
  anim "", hat: reuse an existing hat with a new tint until art exists). Lamp (lamp.gd):
  `buyer` (saved like Bed.owner_creature); lit when `is_lit()` and (no buyer or buyer asleep
  in its bed). Creature: `parcel` becomes the good's path (String, replicated); the head shows
  the good's mesh at HAT_SOCKET_OFFSET + up (creature_config.gd:233); `_carry_home` targets
  own bed only (drop the close-owner fallback in `Housing.bed_of`, housing.gd branch :83-93);
  gift: target = `social` best friend in reach, then `add_friendliness(GIFT_BOND)`
  (social_component.gd:91). Constants: FURNITURE_PRICE 5, GIFT_PRICE 3, GIFT_BOND 1.0, LAMP_LOGS 3.
- **Tests + cheat key:** keep test_shop.gd's 152 lines where they hold; add
  `test_no_clerk_on_shift_no_sale`, `test_a_sale_pays_the_clerk_or_the_owners_till`,
  `test_a_shop_short_of_logs_wants_them`, `test_a_sharer_without_its_own_bed_buys_no_lamp`,
  `test_an_owned_lamp_lights_only_while_its_buyer_sleeps`, `test_a_gift_jumps_the_bond_with_its_best_friend`.
  Cheat `/shop` (exists on the branch): add a paid sign, an INT 8 clerk, a woodpile with 6 logs,
  a gift counter and a friend pair.
- **Shared with other clusters:** PR 6 proprietor and till (a founder may own a shop);
  c3's `wants/spare/hand` and `Carry` (PR 4 owns them; haulers fill the shop too).
- **Open questions for the user:**
  none new (gift shop and logs picked, Round 2).
- **TODO (later):** rule 6 M2 (owner carries its lamp to a new bed), 34 room mood C (user),
  barber, a founder-built shop (T2/T3), beds as a home good (PR 7 L4).

## Old design updates (docs/BRAINSTORM_design_r1_shops.md, edited in place)
- Added a "Round 4 (stage 2 relay)" block under the title: what main's stage 1 economy
  superseded (R2's sign-to-sign supplier pay and vault deposit: the bank only relays now, A1;
  "broke drink free" rule 5: main B1 turns the broke away unless a friend treats them;
  savings: cut, no savings rule (user, founders) and nothing on main reads it), where each
  round 3 item went (18f to c4 PR 8, 34 and M2 to TODO, 18b closed by main B1/B3).
- The block notes that c4 now owns what the "Ownership (user)" line split between R1 and R2;
  that line itself stays verbatim, as does every other (user) line.
