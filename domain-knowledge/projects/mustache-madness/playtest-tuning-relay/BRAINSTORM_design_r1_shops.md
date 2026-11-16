# BRAINSTORM: R1 economy shops (rule 6 goods home, 18f clerk shop, 34, 18b)

Design round 3, 2026-10-22. Built: only 18f as it stood in round 1 (mm-fixes2,
feat/furniture-shop, b6ee3c20 + 32fd0710, merge base 269839c5, one behind main c516194a).
Picks tagged (user) are the user's own words (HANDOFF_playtest_tuning.md:36-44, 63-71); every
other pick is the round's, proposed. Line refs: `main` = mustache-madness @ c516194a; `18f` =
mm-fixes2. Ownership (user): R2 owns the sign, sign-to-sign supplier pay and the vault deposit
(rules 1-4); R1 owns rule 6 (goods go home). R1 calls R2's interfaces and does not redesign them.

## Round 4 (stage 2 relay, 2026-10-25): what the stage 1 economy on main changed
Current design: `docs/BRAINSTORM_design_c4_businesses.md` (c4 owns every gem flow into or out
of a sign or shop, replacing the R1/R2 split). Every (user) line below stays as written.
- Superseded by main (#371): R2's sign-to-sign supplier pay (servers now buy stock from their
  own pouch, B2); the vault deposit (the bank only relays gems to due signs, A1); rule 5 "broke
  creatures still drink and eat free" (main B1 turns a broke one away unless a seated friend
  treats it; confirm with the user). The sign is per shift, 1 gem = 60 s, stacked up to 4.
- Savings (round 3 pick) is cut: no savings rule (user, for founders), and nothing reads it.
- 18f moves to c4 PR 8 (clerk on a paid sign, sale through `buy_at`, logs as stock, rule 6
  minimum: own bed, owner on the good, carried over the head, lit in use). M2 (owner carries
  its lamp to a new bed) and 34 (pick C, user) move to a TODO. 18b is closed by main B1/B3.

## Round 3 changes
- **Payment model (user, rules 1-5) replaces round 2's pay design.** Cut as moot: the K3/K4
  pay-component fork (the sign is R2's), the tip jar and every tip (rule 3: sign to sign),
  "a buyer pays the clerk" pouch to pouch (rule 2: the buyer's gem lands on the shop's sign
  while it is due, else in the clerk's pouch).
- **18b pick B + C is cut (user rule 5: broke creatures still drink and eat free).** 18b shrinks
  to one rule: a good that goes home needs its price; a serving used up in place stays free to
  the broke. No standalone PR: the gate already holds in 18f's code.
- **New concept, savings (round pick):** the gems a creature keeps toward the good it wants.
  R2's vault deposit and the bar's pay take only gems above it. Interface request to R2.
- **Rule 6 (R1 owns) defined below:** a bought good is carried over the head, set by its own
  bed, owned by the creature (not the bed), used there and seen in use. 18f is reworked on it:
  only a creature with its own bed buys; a lamp follows its owner to a new bed; the owner
  switches it on at bedtime.
- Kept from round 2: the clerk job; lamps made from 3 woodpile logs; player lamps light first;
  18f + 34 land as one PR; 34 pick C (user).

## Rule 6: goods go home (user; R1 owns)
Concepts, each by what it takes in, gives out, and connects to:
- **Home good:** takes in one purchase at a shop (its price, paid by its buyer); gives out a use
  its owner makes at home, plus one furniture piece in that room (34's lift); connects one
  owner to the room of that owner's own bed. Today: the lamp. Worn items: later (user).
- **Owner:** the buyer, held on the good (saved), never on the bed. A bed changing hands
  leaves the good with its owner; an owner whose own bed moves to another room carries the
  good there. Owner gone (death, combine): the good stays as plain, ownerless furniture.
- **Parcel:** the good in transit: takes in a sale (or a move), gives out the good set down by
  its owner's own bed; shown as the good's mesh held over the owner's head (user: "carried
  over the head"), on every peer. Its owner downed or dead: it drops as the good's item.
- **Use:** the owner's visible act with its good at home. Lamp: lying down in its own bed at
  night it switches its lamp on (💡, glass lit), and off when it gets up or at dawn. Lit, it
  is a lamp like any (daytime at night within 6 m), but only in a free light slot.
- **Savings:** takes in wages; gives out a purchase; connects the pouch to the good it wants
  next (the cheapest good it can still own: a lamp while it owns none and its room is under
  FURNISH_MAX). Zero when it wants nothing. Spendable at the bar and depositable at the vault
  = pouch - loot - savings.

### 18f: furniture shop (clerk, goods home)
- **Frame:** a clerk works the shop like any workplace; a creature with its own bed saves,
  buys a lamp, carries it home over its head, and lights it at bedtime.
- **Assumptions to verify:**
  - [x] Round 1 shop: no worker, the 5 gems drop on the counter for the player
    (18f shop.gd:15-23); the lamp is minted, no stock used.
  - [x] The lamp goes to `Housing.bed_of`: its own bed, else a close owner's (18f
    housing.gd:83-93), so a sharer buys today; rule 6 says its own bed.
  - [x] Beds hold `owner_creature`, saved (bed.gd:17-23); nothing owns a lamp today.
  - [x] Carried goods show only as a head glyph today (main creature.gd:1036-1039); a carried
    body is pinned at CARRY_OFFSET in front (creature_config.gd:91, creature.gd:2131-2140).
    No item is held over a head: a new visual.
  - [x] Only 8 lamps light, first come (main lamp.gd:9,14-33); README: "a ninth stays dark".
  - [x] The bartender's restock walk is reusable: `restocks`, `supplier`, `bag_from` (main
    bar.gd:106-141), `_restock` (creature.gd:1233-1241). A player lamp costs 3 logs (main
    blueprint_registry.gd:110-114).
  - [x] Measured (user, care seed 1, 900 s, n=1): wages 20, bought 18; wages pool in the
    bartender. A 5-gem lamp needs a creature to keep 5 gems: with every gem pulled to the bar
    (main offer_place.gd:160-165) and spare gems sent to the vault (rule 4), no one may.
  - [ ] Open, R2: the sign interface names (sell to the sign while due, pay a supplier sign,
    the payer never opens a closed sign) and what the shop does when its sign cannot pay a log.
  - [ ] Open: no clerk hat among the job hats (creature_config.gd:215-300): a new hat.
- **Candidates (carried over the head):** H1 the good's head glyph only (📦, the carry
  convention). Cut: the user said over the head, and a glyph does not say which good. H2 the
  good's mesh held over the head (survives). H3 the good worn as the hat. Cut: a worker on a
  break wears its job hat.
- **Candidates (owner moves):** M1 the good stays in the old room (cut: then it is the bed's,
  against "owned by the creature, not the bed"); M2 the owner carries it to its new bed in free
  time, the same carry home path (survives); M3 it moves at once (cut: off screen).
- **Recommendation: H2 + M2 + savings.** Scene: the player throws 2 gems at the shop's sign
  ("💎 2"). Mo (INT 8) puts on the clerk cap and punches in. The counter is bare, so Mo walks
  to the woodpile and takes 3 logs; the shop's sign pays the woodpile's sign 3 gems (rule 3,
  R2's call), and a lamp stands on the counter. Pip, a worker that owns its bed and kept 5
  gems, walks up and pays: gems hop to the shop's sign while it is due, the rest to Mo (rule 2).
  Pip walks home with the lamp over its head and sets it by its bed. At night Pip lies down,
  💡, the lamp glows; at dawn it goes dark. Later Pip's bed changes rooms: Pip carries the lamp
  over its head to the new bed.
  Mechanism: `can_furnish` = owns a bed, owns no lamp, room under FURNISH_MAX, spendable +
  savings >= FURNITURE_PRICE. Sale on the clerk's labor tick, through R2's sign. The clerk
  restocks only what the sign can pay for. Owned lamp: lit only in use and only in a free slot;
  a player lamp takes the slot of a bought one (round 2 pick).
- **Build sketch:** 18f shop.gd: drop the counter gem drop (:21-22) and `clear_footprints`
  (:42, #370 pushes creatures out in `spawn_grid_object`); `logs` saved; clerk `labor()` sells
  or restocks via R2's sign. `GameEnums.Job.SELL` appended (game_enums.gd:8); JOBS entry
  req_int 8, interval 3.0, reach 1.8, anim "", new clerk hat. Lamp (main lamp.gd): `owner`
  (saved, instance id like Bed), `bought`; `_ready`/`_exit_tree` slot logic (:14-33) prefers
  unbought; `_show` (:49) lit = slot and (unowned or in use). Creature (18f creature.gd):
  `parcel` becomes the good's path (replicated, for the head mesh); `_carry_home` (:1101-1113)
  targets the owner's own bed and also serves M2 (picks up an owned lamp outside its bed's
  room); `can_furnish` (:1117) as above; new `savings()`; `spendable()` (:1095) subtracts it
  for the bar (offer_place.gd:160-165, bar.gd:196) and for R2's deposit. Use: the sleep path
  sets the lamp on at lie-down, off at get-up. Housing: `bed_of` (:83) own bed only for goods.
- **Tests + cheat key:** test_shop: `test_a_sale_goes_to_the_sign_while_due_else_the_clerk`;
  `test_no_clerk_on_shift_no_sale`; `test_the_clerk_restocks_only_the_logs_its_sign_can_pay`;
  `test_a_sale_uses_a_lamps_logs`; `test_a_sharer_without_its_own_bed_buys_nothing`;
  `test_the_lamp_is_its_buyers_not_its_beds`; `test_an_owner_moved_to_another_room_carries_its_lamp_there`;
  `test_a_dead_owners_lamp_stays_as_plain_furniture`. test_lamp:
  `test_an_owned_lamp_lights_only_while_its_owner_sleeps_by_it`;
  `test_a_player_lamp_takes_the_light_from_a_bought_one`. test_creature: `test_savings_are_not_spent_at_the_bar`.
  Cheat `/shop`: a hut with a bed owned by a friend with 10 gems, a shop with a paid sign, an
  INT 8 friend, a woodpile with 6 logs; `/night` shows the lamp lit by the bed. `/move_bed`
  (new, or extend `/shop`): moves the owner's bed to a second hut to show M2.
- **Open questions for the user:**
  1. Savings: a creature saving for a lamp drinks free like the broke (pick), or pays for
     drinks and may never reach 5 gems?
  2. A sharer without its own bed: buys nothing (pick, literal rule 6), or buys for the bed it
     sleeps in?
  3. Lamps from woodpile logs (pick) or minted (no stock, no supplier pay)?
  4. Lamp light: an owned lamp lights only in use and player lamps first (pick), or a lamp in a
     room lights only that room and takes no slot?

### 34: own-room furniture lifts the room term
- **Frame:** a furnished room feels better to sleep in, best when the sleeper has it alone:
  a 1-bed room with a lamp beats a bunkhouse with the same lamp.
- **Assumptions to verify:**
  - [x] The room term is one lasting centre term from the bed count: main creature.gd:2419-2423,
    creature_config.gd:719-726 (+0.5 alone, 0 at 2, -0.25 a bed past 2, floor -1).
  - [x] Pieces per room are counted on 18f (housing.gd:159-184): table, chair, lamp, owned or
    not; rule 6 changes who owns a piece, not where it stands.
  - [x] Placing or removing a block piece marks Housing dirty: grid_manager.gd:26-30, 44-49,
    73-76 emit `structure_changed`; game.gd:116-117 connects it to `Housing.mark_dirty`. A lamp
    carried to a new room (M2) recounts both rooms.
  - [x] The card names a 2-bed room "bunkhouse" (18f creature_inspector_ui.gd:13, 208,
    `mini(beds, 2)`); hidden today (lift 0), shown once furniture lifts a 2-bed room.
  - [ ] Open: whether the lift moves care snaps or herd size (no sims this round).
- **Candidates:** A flat lift per piece (cut: bunkhouses gain as much); B pieces lift only a
  Bedroom (survived, a cliff at 3 beds); **C comforts per sleeper (user)**; D a wake moodlet
  (cut: a second path for the room term); E the lamp as a cure seat (cut: not a seat); F the
  lift only for a good's owner while in use (cut by the user's pick C; rule 6's use stays
  visible, the lift stays per room).
- **Recommendation: C (user).** Scene: Pip owns the only bed in a small hut; its lamp lands
  by the bed; the card goes from "Bedroom, mood +0.5" to "+0.75", +1.0 with a second piece.
  Next door 9 share a bunkhouse with 2 lamps: +0.06. Mechanism: `room_mood(beds, pieces) =
  max(bed term, floor) + ROOM_PIECE_MOOD x min(pieces, FURNISH_MAX) / beds`; no bed = floor.
  ROOM_PIECE_MOOD 0.25 (round pick: one piece offsets one bed past a Bedroom).
  | beds | 0 pieces | 2 pieces |
  |---|---|---|
  | 1 | +0.50 | +1.00 |
  | 2 | 0.00 | +0.25 |
  | 4 | -0.50 | -0.38 |
  | 9 | -1.00 | -0.94 |
- **Build sketch:** same branch and PR as 18f. 18f creature_config.gd:723 `room_mood(beds,
  pieces := 0)`, `ROOM_PIECE_MOOD := 0.25` beside ROOM_* (:489-491); 18f creature.gd:2468 and
  headless_sim_driver.gd:280 pass `room_pieces`; 18f creature_inspector_ui.gd:190-208: pack
  pieces into `_card_bits` (beds + 1 in bits 13-17, pieces at 18-19), `room_card(beds_plus_one,
  pieces)`, name by type (Bedroom 1-2 beds, bunkhouse 3+), add "n pieces of furniture" to the
  why. LAW_beds.md rule 1: "the beds and the furniture in the room of its bed". Close fork 3
  in BRAINSTORM_mood_fun_steam.md.
- **Tests + cheat key:** 18f test_housing.gd:328 room-mood test gains a pieces column (the
  table; pieces 5 = pieces 2); new: a lamp spawned in its room raises `mood_center` after one
  reassign; test_creature_inspector.gd:119: `room_card(2, 2)` says "+1.0", `room_card(3, 1)`
  names a Bedroom. Cheat `/cozy`: a 1-bed hut with 2 lamps and its owner beside a 4-bed hut
  with 2 lamps; inspect both. `/shop` then `/night` shows the card move live.
- **Open questions for the user:** none (C is the user's; 0.25 is a proposed size).

### 18b: price gate (now a rule, no PR)
- **Frame:** under rule 5 (user) the broke still drink and eat free; the gate decides only what
  being broke blocks, so the player sees wages buy things a creature keeps, never its comfort.
- **Assumptions to verify:**
  - [x] Every place a gem changes hands: the bar drink (main bar.gd:193-198) and the 18f shop
    (shop.gd:15-23). Library, fire, chair, meals, medic beds and theft (18c) take no gems.
  - [x] A broke drinker drinks free today (main bar.gd:194-197; test_social_bar.gd:358): kept.
  - [x] The shop is gated already: `can_furnish` and `spend` read `spendable()` (18f
    creature.gd:1074, 1095, 1117); loot never counts.
  - [x] 18i's aspirers are below every job gate, so jobless, so broke (main creature.gd:1071-1076).
  - [ ] Open, R2 (18d): tuition at the paid chalkboard.
- **Candidates (what broke blocks):** G1 nothing (cut: then a gem buys nothing a creature
  cannot get free, and the shop never needs savings); **G2 goods that go home only (survives,
  pick)**; G3 goods and classes (cut: tuition would bar exactly 18i's broke aspirers from the
  class, and a gem would decide how fast a creature reaches a job, against the pillar "a gem
  changes how much a creature works, never at what"); G4 goods, classes and drinks (cut by
  rule 5).
- **Recommendation: G2.** One rule: a home good (rule 6) needs its price from spendable +
  savings; a serving used up in place (drink, meal, class) is paid when the creature has
  spendable gems and free when it has none. Scene: a broke jobless friend sits at the bar and
  drinks free; it sees a worker pay and goes to study; it never gets a lamp until it works.
- **Build sketch:** no code beyond 18f (its `can_furnish` and `savings`). Write the rule into
  docs/BRAINSTORM_creature_economy.md "Sinks and prices". Hand G2's class answer to R2 for 18d.
- **Tests + cheat key:** covered by 18f's `test_it_buys_only_with_the_price...` and
  `test_savings_are_not_spent_at_the_bar`; test_social_bar.gd:358 stays as is. Cheat: `/aspire`.
- **Open questions for the user:** class tuition free to the broke (G2, pick) or gated (G3)?
