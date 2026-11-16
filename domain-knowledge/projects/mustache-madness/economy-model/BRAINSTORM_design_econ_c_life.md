# BRAINSTORM: cluster C design, heir and food theft (design only, 2026-10-24)

Picks here are Claude's, proposed, until tagged "(user)". Code read in `/home/akiraki/Playground/mm-econ`
at c516194a. Clock used for every size below: one day = `DayNightConfig.CYCLE_SECONDS` = 28.1 s
at wave 0 (15 s daylight / 0.533), +10% per wave; hunger runs full to 0 in 2 days (56 s); the
warn line is 20 s before 0 (hunger 0.36).

## Round 2 changes (AFK, picks are the session's, not the user's)
- **Accepted (session):** player may grab the gems before the heir; a combiner swallow counts as
  a death; a 1-gem creature never steals; the jail meal comes from nothing; the field starve
  harvest stays unwitnessed; theft moves mood only; the signs 🍗 📢 🥣 😤 stay, flagged for the user.
- **B1 owns the friend predicate and its constant; C defines neither.** B's Round 2 names them
  `Creature.befriends(peer)` and `FRIEND_LEVEL` 2.0 (BRAINSTORM_design_econ_b_prices.md
  "Round 2 changes"). C1 drops its `SocialComponent.is_friend` and `FRIEND_LINE`; the heir gate
  is `c.befriends(dead) or Housing.close(c, dead)`, ranked by `c.social.familiarity(dead)`.
  Conflict, new fork 1 below: B's `befriends` gates on familiarity (>= 2.0) plus friendliness
  >= 0, not on friendliness >= 2.0 as this doc's round 1 and the coordinator's note say.
- **C2 reuses B1's gate names:** the owner who can witness is `src.server()`: for basket stock
  `Basket.at(drop.global_position, tree).server()`, for a table `Kitchen.serving(table).server()`
  (null when no open kitchen). "No treat came" is `payer_for(price) == null` at the source
  (`DISH_PRICE` at a table, the crop price at a basket). "The gate says no" is that same null.
  `_food_to_steal()` takes only sources B's gate covers (a basket stack or a table dish).
- **Consequence:** `server()` is null off shift, so a closed shop has no witness: theft there is
  unseen and eaten. Read for the player: pay the sign and the stock is guarded. New fork 2.
- **C owns the `SEE_RADIUS` rename** of `ASPIRE_RADIUS` (`creature_config.gd:164`): rename the
  constant and its readers in the aspire path (`creature.gd:1063` `Herd.allies_within`) in C2's
  PR; B and 18i keep reading it under the new name.
- **New forks:**
  1. Heir and treat gate on familiarity (B's `befriends`) or on liking (round 1 here)? Session
     pick: B's, since B owns it and one predicate serves both; a familiar creature with
     friendliness below 0 is already excluded, which removes the "known enemy inherits" case
     that drove the round 1 pick.
  2. A closed shop is an unguarded pantry for the broke. Session pick: accept (the witness is
     the worker on shift; off shift it is not watching). The alternative, the assigned worker
     witnessing off shift too, needs a lookup B cut (G2: the job board drops a farmer's site
     between crops).

Forks closed or recommended (round 1):
- **F5 (one familiarity threshold or two):** one. Superseded in round 2 (B1's `befriends`). Round 1: a single line on friendliness (the
  liked side), read by the heir and by B's treat; familiarity only ranks, it never gates. Why:
  familiarity is confidence, not liking (`creature_config.gd:603`), so a known enemy would pass
  a familiarity gate; one line gives the player one thing to read ("friends"). Value 2.0.
- **F6 (1 gem, hungry, only a dish at 2):** it does not steal (the user's gate says 0 gems). It
  may be treated (B: the treat gate is "cannot afford the cheapest food on sale", not "0 gems"),
  else it waits; the existing starve harvest (`creature.gd:811`) feeds it after STARVE_SEC. Open
  question 1 below.
- **F7 (jail meal source):** from nothing, like the free library: the jail is a piece the
  player built. One plain meal (`MEAL_FILL`) when it enters the cell. Open question 2.
- **F11 (constants):** in each Build sketch; every one sized on the clock above.

### C1: heir: a dead creature's gems go to its most familiar friend, on foot
- **Frame:** a pouch now spills to the floor on every death; the goal is that a friend walks
  over and picks the gems up on screen, so a gem keeps passing creature to creature.
- **Assumptions to verify:**
  - [x] The pouch drops only in `_spill_pouch` via `_drop_all`, from farewell, despawn and perish (`creature.gd:927`, `:2289`, `:2362`, `:1349`).
  - [x] `perish` runs `_drop_all` before `SocialCoordinator.mourn`, which calls `forget(dead)` and wipes the edges (`creature.gd:2362-2364`, `social_coordinator.gd:311`): the heir pick must run inside `_spill_pouch`.
  - [x] Familiarity and friendliness are directed per-pair values (`social_component.gd:45`, `:71`); no "friend level" constant exists. "Closer" exists: `Housing.close` = parent/child, love, or a mutual bond over CLOSE_FRIEND 4.0 (`housing.gd:40`).
  - [x] Only players pick up dropped gems (`dropped_item.gd:165-210`); the drop spawns through a MultiplayerSpawner, so the server gets no node ref at death (`spawn_coordinator.gd:205`).
  - [x] Loot (stolen gems) is part of the pouch (`creature.gd:163`, `spendable()` `:1079`).
  - [ ] open: a combiner swallow (`despawn`) counts as a death for the heir. Recommended yes (one path).
- **Candidates:**
  - A. Claim on the heir: the gems drop as today; the heir stores the spot and the count and walks there; at the spot it takes gem stacks in reach into its pouch. Survives.
  - B. Straight into the heir's pouch at death. Cut: LAW_game_design ("a payment walks there, never a remote counter change").
  - C. The DroppedItem carries an heir id and offers itself to the heir in reach, like a player pickup. Cut: no node ref at spawn, and items would read creature social state (wrong altitude).
  - D. Post a job on the job board at the death spot. Cut: the board matches by hat, discipline and distance, never familiarity; an heir is no job.
- **Recommendation (A):** an old fox floats up and its 4 gems tumble onto the floor. Across
  the yard its friend the frog stops chatting, waddles over with a 💎 glyph, and the stack
  flies into it. A loner's gems just lie there for the player. Mechanism: in `_spill_pouch`
  pick the heir among FRIENDLY allies not jailed, held or leaving: gate
  `c.befriends(dead) or Housing.close(c, dead)` (B1's predicate, round 2), rank by
  `c.social.familiarity(dead)` (the heir's side, as mourn reads it), nearest breaks a tie.
  It inherits `spendable()` only; the loot part stays a plain floor drop (pillar: stolen gems
  are the police's, never an heir's). The claim lapses after HEIR_SEC (jailed, downed, or
  blocked): the gems are plain floor gems.
- **Build sketch:**
  - `creature.gd`: new transient `inherit_at := Vector3.INF`, `inherit_gems := 0`, `_inherit_until := Cooldown.new()` (add to TRANSIENT `:65`; a load drops the claim, the gems stay on the floor).
  - `_spill_pouch` (`:1349`): before `pouch = 0`, `var heir := _heir()`; if heir: `heir.inherit_at = global_position; heir.inherit_gems = spendable(); heir._inherit_until.arm(heir.clock, HEIR_SEC)`. Spawn stays one stack as today.
  - New `_heir() -> Creature` beside `_spill_pouch`: loop `"creatures"` group, gate and rank as above.
  - `_decide_mode` (`:756`): after `_rescue_has_work()` (`:775`), `if inherit_gems > 0 and _inherit_until.active(clock): return Mode.INHERIT`; else clear the claim. New `Mode.INHERIT` in the enum (`:7`).
  - Mode branch: `Intent.move_to(inherit_at)`; within HEIR_REACH, for each node in `DroppedItem.kind_group(gem meta)` within HEIR_REACH: `pouch += drop.take(inherit_gems)`, reduce `inherit_gems`; emote `Wage.GLYPH`; clear the claim. A stack the player took first leaves nothing: the claim clears.
  - `_doing_glyph`: INHERIT shows `Wage.GLYPH` (the gem it walks to; existing glyph).
  - Friend gate: B1's `Creature.befriends(peer)` and `FRIEND_LEVEL` (round 2); C1 defines neither.
  - Constants (`creature_config.gd`, next to CLOSE_FRIEND `:128`): `HEIR_SEC := 60.0` (limit, dilated, about 2 days: at 3.5 m/s, the slowest walker, 210 m, any map); `HEIR_REACH := 2.0` (limit, m: the stack lands under the death spot, a small bounce).
  - Dilated: `_inherit_until` on the heir's clock; add "heir claim" to `docs/LAW_time_dilation.md` registry.
- **Tests + cheat key:** new `test/ci/entities/creatures/test_heir.gd`:
  - `test_a_dead_creatures_gems_go_to_its_most_familiar_friend`: A pouch 4, B and C friends of A (2.5), B more familiar; A.perish(); B claims 4, C none.
  - `test_the_heir_walks_over_and_takes_the_stack`: run frames; B.pouch == 4, no gem DroppedItem left.
  - `test_no_friend_no_heir_the_gems_lie_on_the_floor`: friendliness 1.0 only; a stack of 4, no claim.
  - `test_a_child_inherits_below_the_friend_line` (parents id, friendliness 0).
  - `test_loot_stays_on_the_floor`: pouch 5, loot 3; heir gets 2, a stack of 3 remains.
  - `test_a_lapsed_claim_leaves_the_gems`: heir jailed; after HEIR_SEC the claim is clear.
  - Keep `test_police_box.gd:378`, `:384` green (no friend there).
  - Cheat `heir` (creature group): the aimed creature gets 5 gems, a friendly of its kind spawns 6 m away bonded both ways (`befriend` 3.0, familiarity 4.0), and the aimed one says farewell.
- **Shared with other clusters:** reads B1's `befriends` + `FRIEND_LEVEL` (round 2). A creature picking up floor gems (`Mode.INHERIT`) is the first creature gem pickup; no other PR needs it yet.
- **Open questions for the user:**
  1. Can the player grab the gems before the heir arrives? Recommend yes: one pickup rule, and a real choice (take the gems back, or let them circulate).
  2. Moved to round 2 fork 1 (B1's `befriends` gates on familiarity; session pick: B's).

### C2: food theft: the hungry broke grab one unit; the owner fights or calls a cop
- **Frame:** a creature with 0 gems that cluster B's buy gate refuses has no way to eat until
  STARVE_SEC; the goal is the user's scene: it grabs one food unit and runs, and a witnessing
  owner scuffles (hot) or calls the police (timid).
- **Assumptions to verify:**
  - [x] `Mode.STEAL` exists: walk to a target, grab, rethink (`creature.gd:676`, `:786`, `_rob` `:1325`).
  - [x] A cop catches whatever `wanted()` says, anywhere, and carries it to a free cell (`:1320`, `_ask_care` `:2598`, `labor` `:2614`, `_rescue_tick` `:1895-1901`); `_try_jail` arms JAIL_SEC 30 s and hands over loot (`:1964`).
  - [x] `punch` caps damage at hp-1 and a target with `temper > 0` swings back once (`:1378-1387`): a scuffle with no knockdown already exists. Temper is `-warmth` (`personality_component.gd:17`).
  - [x] RAMPAGE mode has the chase-then-punch shape to reuse (`:669-675`).
  - [x] Food on sale: basket stock (stored DroppedItems, `basket.gd:26`) and table dishes (`table.gd:13` servings). Today tired creatures eat basket stock free (`_take_stock_meal` `:815`); chairs serve dishes (`chair.gd:34`).
  - [x] Hunger warn line: `needs.hunger_warns(day)` (`needs_component.gd:49`); the starve harvest stays the last valve (`:811`).
  - [x] Head signs: LOOT_SIGN 💰 bit for stolen gems (`:17`, `_refresh_status` `:1625`).
  - [x] B1 names (round 2): `server()` (null when closed), `Basket.at`, `Kitchen.serving(table)`, `payer_for(price)`.
- **Candidates:**
  - A. Widen `Mode.STEAL`: one theft mode, two triggers (brewer + vault, hungry broke + food); the witness check sits at the grab, owner = the source's `server()`. Survives.
  - B. A flag on the food paths: `_take_stock_meal` and the chair pass the gate when broke and mark it stolen. Cut: a chair meal is a seated meal, never "grab and run"; the owner never sees a run.
  - C. A thief component (approach, grab, flee, eat) of its own. Cut: one user, a new subsystem beside a mode that does it (wrong altitude).
  - D. The station watches its stock and fires on an unpaid take. Cut: stations would read creature temper and police; kept only as the owner lookup B already needs.
  - Prior art (memory, unchecked): RimWorld food binge, Prison Architect guards; BRAINSTORM_food_theft theses 2-4 cut there.
- **Recommendation (A):** the cook sets a dish on the table. A skinny broke frog with the red
  💭🍎 creeps up, takes one, and waddles off at half speed with 🍗 over its head. A hot cook
  in 8 m drops its ladle and chases; on contact a puff of dust (the existing poof), a punch or
  two, the dish flies back to the table, and both sulk (😤). A timid cook shouts 📢; the frog,
  now wanted, gets carried to a cell by the cop, where it eats a plain meal 🥣. Seen by no
  one, the frog eats it 8 s later. One try per hunger dip: a frog that lost its dish waits
  for the starve harvest or a treat.
- **Build sketch:**
  - Gate, one predicate `_steals_food() -> bool` in `creature.gd`: `needs.hunger_warns(_days(1))` and `spendable() == 0` and not `_tried_theft` and `payer_for(price)` at the source is null and `_food_to_steal()` finds a source. `_tried_theft` resets inside the predicate whenever hunger is above the warn line. Called at `:786` (`if _steals_food(): return Mode.STEAL`) and in `_tired_mode` before the starve harvest (`:811`): 2 callers.
  - `_food_to_steal() -> Node3D`: the nearest basket holding stock or table with `servings > 0` (sources B refused).
  - `Mode.STEAL` branch (`:676`): if `stolen_food`: when `_eat_at` is done, `feed.begin(stolen_food, ...)` and clear the mark (the chew is the species' eat delay, `_finish_meal` `:1587`); else walk away from the source at `THIEF_SPEED_MULT`. Else walk to the vault (today) or the food source; on reach `_grab_food(src)`.
  - `_grab_food(src)`: take one (`stack.take(1)` or `table.servings -= 1`), set `stolen_food`, `_stolen_from = src`, `_tried_theft = true`, arm `_eat_at` EAT_SEC; then the owner (`src.server()`, see round 2): if valid, FRIENDLY, awake and within `SEE_RADIUS` of the thief: `temper > 0.0` sets `owner.chasing = self`, else `reported = true` and the owner emotes 📢.
  - `wanted()` (`:1320`): `... or (reported and current_state == State.FRIENDLY)`. `_try_jail` clears `reported`, calls `_return_stolen()`, then `needs.eat(MEAL_FILL)` + emote 🥣 (no moodlet: a plain meal). `reported` joins SAVED (like `loot`).
  - Owner: `chasing: Creature` (transient), new `Mode.CHASE` after `on_call()` in `_decide_mode`, while `chasing.stolen_food` is set; the branch reuses the RAMPAGE chase lines (`:669-675`, extract `_chase_punch(victim)` for 2 uses). On contact: `punch(thief)`, `thief._return_stolen()`, `moodlet(&"scuffle")` on both, `broadcast_fx(&"poof")`, clear `chasing`. The food eaten first: the owner gives up with 😤.
  - `_return_stolen()`: a dish goes back as `table.servings += 1` (if the table stands and has room), a raw crop as `DroppedItem.spawn` at the basket (it restocks as stock, `dropped_item.gd:125`); with no source, a plain floor drop. Also called from `_drop_all` (a thief dies holding it).
  - Head sign: new `STOLEN_SIGN := 64` bit and glyph `STOLEN_GLYPH := "🍗"` (invented, see questions), shown like LOOT_SIGN.
  - Constants (`creature_config.gd`): rename `ASPIRE_RADIUS` (`:164`) to `SEE_RADIUS := 8.0` (limit, m: "a room and its doorway sees it", now 2 readers; a table sits up to 10 m from its kitchen, so a cook at the stove may miss a grab at the far table: fine, it reads). `EAT_SEC := 8.0` (limit, dilated, 0.28 day: with `THIEF_SPEED_MULT := 0.5` a 5 m/s cook closes 8 m on a 5 m/s thief in 3.2 s, a 3.5 m/s frog cook on a bunny thief never: species decide). `&"scuffle"` effect `{amount -1.0, days 0.25, brief}` (weight, like hangover). Temper line: reuse `temper > 0.0` (no new constant). JAIL_SEC 30 s kept (1.07 days: a thief caught at the warn line would hit hunger 0 in the cell in 20 s; the entry meal covers it).
  - Dilated: `_eat_at` on the thief's clock; add "a stolen food's eat wait" to the time-dilation registry.
- **Tests + cheat key:** new `test/ci/entities/creatures/test_food_theft.gd`:
  - `test_a_hungry_broke_creature_steals_one_dish` (servings 2 to 1, `stolen_food` set, STOLEN_SIGN on).
  - `test_one_gem_or_a_treat_means_no_theft`; `test_above_the_warn_line_no_theft`.
  - `test_unseen_theft_is_eaten_after_eat_sec` (hunger rises, mark clears).
  - `test_a_hot_owner_chases_scuffles_and_the_dish_returns` (servings back to 2, both have &"scuffle", thief hp > 0, still FRIENDLY).
  - `test_a_timid_owner_reports_and_a_cop_jails_the_thief` (wanted, cop carries it, cell entry feeds it, `reported` false).
  - `test_an_owner_out_of_sight_does_nothing`; `test_one_try_per_hunger_dip`.
  - `test_police_box.gd`: `test_a_reported_thief_round_trips_a_save` beside `test_save_game.gd:214`.
  - Cheat `thief` (rooms group): the "restaurant" hut (`cheat_coordinator.gd:539`) with a hot cook (warmth -0.5) and one creature at 0 gems on the warn line next to the table; `thief_cop` the same with a timid cook (warmth 0.5), a police box, a cop and a jail cell (reuse the "jail" builder `:424`).
- **Shared with other clusters:** B1's `server()`, `Basket.at`, `Kitchen.serving`, `payer_for`: C2 only reads them. C2 owns the `SEE_RADIUS` rename, shared with aspire (PR 18i). `_return_stolen` could serve pickpocket (`feat/pickpocket`, not merged) if gems ever return to a victim.
- **Open questions for the user:**
  1. F6: a creature with 1 gem facing only a 2-gem dish never steals and waits (treat, then the starve harvest). Recommend yes: "broke" stays 0 gems, as picked.
  2. F7: the jail meal comes from nothing (the jail feeds, like the free library). Recommend yes; the alternative is a cop fetching basket stock, which fails exactly when food is short.
  3. The starve harvest of a field crop stays free and unwitnessed. Recommend yes for this stage; it is the last valve.
  4. Invented interface: 🍗 over a thief's head, 📢 for a call, 🥣 for the jail meal, 😤 for a lost chase. Recommend these, or name your glyphs.
  5. Theft moves mood only, never friendliness between thief and owner. Recommend yes (stated nowhere; a grudge is a later idea).
