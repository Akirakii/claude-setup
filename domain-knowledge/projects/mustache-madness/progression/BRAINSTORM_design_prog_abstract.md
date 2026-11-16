# BRAINSTORM: abstract model of the progression stack (PRs 1-7)

The `/abstract` layer for the progression relay: roles, a ledger of every counted resource
the 7 PRs move, the rules in force, and 3 framings. Design only. Every code claim cites the
worktree `mm-prog` at 6cb6d951 (branch feat/prog-tree). "Checked" = read in the code that
runs; "assumed" = not checked. Decisions tagged (user) come from
`docs/BRAINSTORM_design_progression.md` and `docs/HANDOFF_progression.md` in the main
checkout.

## 0. Purpose (user)
The player always knows what to do next and why; the run has an action curve (build-up,
siege, release); progression is "you do it by hand, then the city takes it over".

## 1. Restated without nouns

> **The player pays acts (by hand) to a gate, per act of kind K, when the act lands; the
> gate gives the player a capability (a card) that a worker then performs in the player's
> place. A periodic pressure source drains the herd every P cycles; an arrival source adds
> members of new kinds; one attention channel tells the player which gate to pay next.**

| Role | Takes in | Gives out | Connects to | Player sees / code name |
|---|---|---|---|---|
| Actor | input, time | acts of kind K (carry, chop, strike ore, jail, carry egg) | Gate | the player / `Player`, `AxeBehavior`, `Creature.grab` |
| Gate | act counts or research ticks | an opened card + its revealed children | Catalogue, Signal | a locked card with a requirement icon / `BlueprintRegistry` (new: requirement per card) |
| Catalogue | opened cards | what may be placed, at a price | Builder (player), Worker | the build menu tabs, Work tab / `BuildMenu`, `BuildHand.buildable` |
| Worker | a placed station + a creature whose stats fit | the same act K, done for the player | Gate (no longer needs the player), Economy | a creature in a hat / `Jobs`, `CreatureConfig.JOBS` |
| Pressure | the run clock (cycles) + a difficulty counter | hostile bodies on a schedule | Herd (drains), Economy (drops gems) | waves today, beasts every 3-5 nights later / `WaveSystem` |
| Arrival | a call (proposed: a pier), the tree | visitors of a species; stay or leave | Herd, Housing | a boat at the shore (new, PR 6) |
| Herd | arrivals, hatchings | workers, mouths, wants | Worker, Signal, Pressure | friendlies / `Creature.State.FRIENDLY` |
| Signal | wants, last night's damage, the frontier, the countdown | one line or a few icons | Actor | frog bubble, glance icons, countdown (PRs 2, 3, 5) |

Terms coined here: **frontier** = the locked cards whose parent is open, up to two steps
(PR 1). **Hand act** = a player action of the same kind a station's worker does (PR 1 list).
**Siege** = a night that spawns beasts; **calm night** = one that does not (PR 5).

## 2. How the current code works (checked)

### 2.1 Unlocks and the lab
- One registry holds every card, the open set, built counts and what opened each:
  `systems/progression/blueprint_registry.gd:20-24`. Saved: `unlocked_ids, _built,
  _opened_by` (:12).
- A card is open from the start when its `opens` list is empty (`seed_basics`, :288-293);
  `opens: ["lab"]` marks a lab-only card (BASICS rows :131, 172, 188, 197, 206, 215, 224,
  242). Pool cards default to `opens_when = ["lab"]` (`metadata/blueprint.gd:106`); 12 pool
  `.tres` in `systems/progression/content/` (10 loaded by `_build_default_pool`, :521-536;
  `clock` and `combiner` files exist but are not in the list).
- `brings` opens a second card with the first (registry :353-354): only `bank.tres:17`
  brings `police_box`.
- The only in-play opener is the lab: `lab.gd:32-44` adds one point per labor tick and, at
  `LabConfig.cost(known)` (`lab_config.gd:65-70`: 6 x 1.5^known ticks), opens a **random**
  card from `findable()` (registry :392-395, `GameRng.pick`, lab.gd:41). The lab posts the
  RESEARCH job only while something is findable (lab.gd:23-24, 34-36).
- Other opener: cheat "unlock" opens all (`cheat_coordinator.gd:365-366`).
- Cause text: `CAUSES` has only `lab` and `cheat` (registry :15-18); `cause_text` also
  supports `"your first X"` for a key that is a card id (:365), unused today.
- Readers of the open set: `BuildHand.buildable()` (`build_hand.gd:29-32`, the menu shows
  open cards only), the banner (`run_hud.gd:63`, `:139`), the menu's "new" mark and tooltip
  (`build_menu.gd:226-236`), the lab's job post, the probe (`balance_probe.gd:717`).
- Lab cost to build: 2 wood + 10 gems (registry :244-252), open from the start.

### 2.2 The Work tab
- `BuildMenu.TABS` (`build_menu.gd:16-22`) has a `WORK` tab ("🪓 Work"); tabs and cards
  come only from open cards (`_pieces_by_tab`, :110-116). A locked card is never drawn:
  there is no locked-card face, no requirement icon, no frontier today.

### 2.3 Which station takes over which hand act (checked map)
| Hand act (PR 1) | Code of the hand act | Job | Station card | Opens today |
|---|---|---|---|---|
| carry a downed friend | `Creature.grab` `creature.gd:2484` | TREAT | `med_kit` ("Emergency Post", `med_kit.gd:14`) / `medic_bed` | lab (registry :242, :131) |
| chop a tree | axe hold -> `_net_request_placeable_hit` `network_manager.gd:414-422` -> `Tree.hit_by_axe` `tree.gd:36` | CHOP | `woodpile` | start (:156-164) |
| axe the gem ore | same RPC -> `GemOre.hit_by_axe` `gem_ore.gd:55-58` (1 gem per break, :14) | MINE | `mine` (`mine.gd:42`) | start (:226-234) |
| jail a friend | put down near a jail bed -> `_try_jail` `creature.gd:2694-2702` | ARREST | `police_box` (`police_box.gd:11`) | lab pool, brought by bank |
| carry an egg | `Egg.grab` `egg.gd:121` | (none; nest is a bed kind, `bed.gd:9`) | `nest` | lab pool |
Jobs with no hand act today: RESEARCH, COOK, BARTEND, SELL, PAY, TEACH, FARM, HAUL,
ARCHITECT, BUILDER (`game_enums.gd:8-24`). FARM and HAUL have near acts (planting,
carrying a log), not listed by PR 1: open fork.

### 2.4 Herd sources
- Starter herd: 3 of one random night-1 species (`intro_phase.gd:15-25`,
  `intro_phase_config.gd:9`). Night-1 species = bunny, frog, fox (`default_wave_config.tres`;
  owl from night 2, hedgehog from night 4).
- **Taming/recruiting:** a wild that falls goes DOWN keeping `downed_from = WILD`
  (`creature.gd:188`, :613); in a bed it mends at `RECRUIT_MEND_MULT` 0.33
  (`creature.gd:2330-2332`, `creature_config.gd:62`), only while `Housing.has_room()`
  (`creature.gd:3424`, `housing.gd:256-257`); full recovery calls `revive_friendly`
  (`creature.gd:2966-2975`), which takes a vacancy (`Housing.vacancies -= 1`). A taming
  food type exists (`food_type.gd:7`, refused as a meal `food_purpose_service.gd:14`).
  Measured once (`docs/LAW_life.md:46-48`, playtest 2): 47 recruits in 5 waves, herd 67 to
  149. **Taming is the dominant inflow today.**
- Breeding: `Egg._hatch` spawns a FRIENDLY (`egg.gd:180-195`); a mate must be kin, same
  species (`creature.gd:2127`, :2164, `is_kin` :3230). LAW_life rule 5: about replacement.
- Fuse Cube: `combiner.gd:109` spawns a friendly (card not in the pool, :523-534).
- Wilds are the same species as friendlies: one `CreatureMetadata`, state picks the profile
  (`creature_metadata.gd:113`, :150); `is_hostile` = WILD or DOWN-from-WILD (:3273-3276).

### 2.5 Waves and nights
- Every NIGHT phase starts a wave; every DAWN ends it and refills the forecast
  (`wave_system.gd:60-69`, :89-116). No skip exists.
- Difficulty = wave number (:90-91); budget `budget_for` steps up every 5 nights
  (`wave_config.gd:23-38`).
- Forecast: 5 waves pre-rolled (`wave_config.gd:78`, `forecast_component.gd:14-17`), sent
  by `forecast_changed` (:6, :86). **No UI reads it** (grep of `ui/`, `systems/level`: none).
- Night gem bounty: the first 3 permanent wild deaths per night drop a gem
  (`wild_drop_service.gd:8-23`, `creature_config.gd:498-500`); `start_night` resets it
  (`wave_system.gd:92`).
- Day length stretches 10% per elapsed cycle, documented as "one per wave, since a wave
  starts each NIGHT" (`world/day_night_config.gd:21-27`).
- Autosave keys on the wave number (`wave_system.gd:64-65`). Siege gear rolls once a
  creature-built piece stands (`wave_system.gd:177-183`).
- Cheats: skip to a night sets `current_wave_number` (`cheat_coordinator.gd:1130`).

### 2.6 The frog guide
- `GuideDirector` (`systems/guide/guide_director.gd`) is a pure line picker: locks (corn ask
  :95-96, watering can :97-98), URGENT (:55-70), a timed reveal, a rotating base pool
  (:200-210).
- **The guide frog is not in play:** nothing instantiates `TutorialGuide` (grep of all
  `.gd`/`.tscn`: no hit); `TutorialGuide.new` was removed in #235 (d09fc993, "the well
  leaves the level"). `GuideBus` (autoload, `project.godot:32`) still reports events; only
  tests listen.
- Stale lines (PR 2 deletes): Fuse Cube :41, :48; van :28, :42, :49; well :58, :63;
  "beds with a crop" :27; "tame" :63. `Blueprints.unlocked` is wired to `on_chaos`
  (`tutorial_guide.gd:78`), so any lab find would add "New chaos item drafted." (:209).
- No per-night tally of "the worst thing last night" exists (assumed from grep of the guide
  and probe hooks; not checked across the probe).

### 2.7 Wish balloons
- Per creature, per tick: `_doing_glyph` (`creature.gd:1277-1316`) picks one sign; free time
  shows `OfferPlace.wish_glyph` (`offer_place.gd:98-106`): `💭` + the place glyph it wants
  when no such place has a free spot it would walk to; no bed shows the bed glyph (:1313).
- Red balloon = a consequence is coming (`creature.gd:24`, `WARN_SEC` 20 s,
  `creature_config.gd:124`).
- The view turns a glyph into a balloon icon (`status_emoji_component.gd:13-19`, :46-54;
  `OfferPlace.wish_icon` :131-139). No herd-level roll-up exists.

## 3. Ledger

Number sources: `measured` (log or probe named), `cap` (a set constant), `guess`.

### 3.1 Open cards (stock: `BlueprintRegistry._unlocked`)
| From | To | Contract (price per unit) | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| start | open | free | `seed_basics` | cap (`opens` empty) | `build_hand.gd:29` |
| lab ticks | open | 6 x 1.5^known ticks per card, random card | labor tick, `lab.gd:37-43` | cap (`lab_config.gd:65-66`); ~5.5 s per tick "measured" in a comment, no log cited | menu, banner, guide (dead) |
| another card | open | free with its parent | `brings`, registry :353 | cap | same |
| cheat | open | free | cheat key | cap | same |
| **new: hand acts** | open | N acts of kind K per card (N open: 1, N, or aims the lab) | act lands (sites in 2.3) | guess | menu, frontier, banner, frog |
| **new: lab, aimed** | open | ticks per card, card chosen (fork) | labor tick | cap today, curve open | same |
- **FLAG units differ:** two inflows to one stock priced in different units (player acts vs
  worker ticks on a 1.5^known curve). The lab curve counts all lab finds (`known()`
  :399-400); once hand acts open cards, decide whether `known` counts them.
- **FLAG gate on a start card:** woodpile and mine are open from the start today; a
  hand-act gate makes them locked at start. The starter hut places 2 medic beds the player
  never unlocked (LAW_beds rule 10): a placed-not-opened case the tree must allow.
- **FLAG reader none:** the frog reader of `unlocked` is dead code (2.6).

### 3.2 Herd members (stock: FRIENDLY group)
| From | To | Contract | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| intro | herd | 3 of one species | level start | cap (`intro_phase_config.gd:9`, user) | `Housing.reassign` |
| downed wild | herd | 1 bed vacancy + mend time x 1/0.33 | full recovery | measured (LAW_life:46-48) | Housing, food check |
| egg | herd | a kin pair + a nest or ground | hatch at dawn | measured (LAW_life rule 5, ~replacement) | same |
| combiner | herd | 3 in, 1 out | fuse | cap | same (card not in pool) |
| herd | gone | lifespan 8-14 days per species | age | cap (LAW_life species table) | same |
| **new: boat** | herd | visitors per boat; stay if wish served (proposed) | boat calls | guess | Housing (vacancy), Signal |
| **cut: downed wild** | herd | removed by PR 4 | | | |
- **FLAG largest inflow removed:** the only measured growth flow (+82 in 5 waves) is cut;
  the boat flow replacing it has no unit yet (per night? per pier? per boat?).
- **FLAG same-kind pair:** breeding needs kin (`creature.gd:2127`, :2164). A boat bringing
  one visitor of a new species founds no lineage (MEMORY: a mechanic needing a same-kind
  pair must make pairs meet). Unit must be a pair or more, or a second boat of the kind.
- **FLAG shared stock:** `Housing.vacancies` is paid by both recruits and (proposed) boat
  stays; with taming cut, the boat contract should pay it the same way (`creature.gd:2971`).

### 3.3 Species present (stock: set of species in the herd)
| From | To | Contract | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| wave pool by night | herd | a species marches from `first_night` (owl 2, hedgehog 4) and can be tamed | night N | cap (wave .tres) | job eligibility by stats (`game_enums.gd:42-48`) |
| **new: boat** | herd | which species: the tree decides (proposed) | boat | guess | same |
- **FLAG unit change:** species today enter on the night clock through the enemy pool; after
  PR 4 they enter only by boat. Species carry stat identity (owl INT 13, LAW_life table) and
  jobs gate on stats (architect INT 12, `creature_config.gd:309`), so **species arrival is a
  capability gate**: a card can open while no creature can work it.

### 3.4 Hostile pressure (stock: wave budget per siege)
| From | To | Contract | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| difficulty | spawns | `budget_for(d)`, factor +1.5 every 5 | each NIGHT | cap (`wave_config.gd:19-38`) | `WaveSystem._spawn_creature` |
| **new: siege period** | spawns | one siege per 3, 4 or 5 nights (fork) | night count | cap (user range) | countdown, preview |
- **FLAG unit change per night -> per siege:** `current_wave_number` drives difficulty
  (:90-91), autosave (:65), cycle stretch comment (`day_night_config.gd:23-27`, reads cycle
  index, so it keeps stretching on calm nights), budget block of 5 (`wave_config.gd:25`),
  bounty reset (:92), the forecast depth (:77-79). Each must say whether it counts nights or
  sieges.
- **FLAG budget spike rhythm:** `SCALE_STEP_EVERY` 5 already spikes every 5th wave; a 3-5
  night siege gap stacks a second rhythm on the first.

### 3.5 Gems (stock: player and creature purses, ground drops)
| From | To | Contract | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| wild death | ground | 1 gem, first 3 per night | permanent death | cap (`creature_config.gd:498-500`) | pickup |
| ore, by axe | ground | 1 gem per break | axe hold | cap, "untuned" (`gem_ore.gd:14`) | pickup |
| ore, by miner | mine stack | 1 per strike | labor | cap (`mine.gd:8`) | stations |
| purse | card | `build_cost` (lab 10, kitchen 10, ...) | placing | cap | `BuildHand.affords` |
- **FLAG income on the siege clock:** the bounty is "per night"; with sieges every 3-5 nights
  kill income falls to 3 per siege unless the unit changes. The income pillar allows it
  (income grows only by what the player built), but a drop to a third is a decision, not a
  side effect. Beasts need a drop rule: `WildDropService.drop` drops the species'
  favorite crop (:17-19); a beast may have none.

### 3.6 Attention (stock: one bubble line; a few HUD slots)
| From | To | Contract | Trigger | Number source | Reader |
|---|---|---|---|---|---|
| events | frog line | one line, priority layers | `GuideDirector.line` | cap | none in play (2.6) |
| **new: dawn pick** | frog line | 1 line per dawn, first-time lines once | DAWN | cap | the player |
| **new: wants roll-up** | HUD | top 2-3 unmet wants | herd tick | cap (user range) | the player |
| **new: countdown + preview** | HUD | nights left, beast kinds | DAWN | cap | the player |
| banner | HUD | one pop per opened card | `opened` | cap | the player |
- **FLAG no speaker:** PR 2 needs a guide frog that is not spawned today.
- **FLAG roll-up rule:** count wants on a fixed scale (how many creatures hold each), never
  a mean (MEMORY: an aggregate must not fall when a weak item joins).
- **FLAG "worst thing last night":** needs a per-night tally that does not exist; reader of
  that stock is the dawn pick only.

### 3.7 Nights (stock: calendar)
`GameTime.current_day` (`game_time.gd:31`) and `DayCycle._cycle_index` (`day_cycle.gd:90`)
count cycles; the siege schedule, countdown, dawn line, boat timing (assumed) and day
stretch all read it. One counter, many readers: keep one owner.

## 4. Rules in force
1. (user) Every city job starts as a hand act; its building opens once the player has done
   it; the building takes the work off the player's hands (pre-pillar).
2. (user) Unlocks form a requirement tree: one requirement per node; meeting it opens the
   node and reveals its children.
3. (user) Friendlies are always friendly species; beasts are a new enemy kind, never tamed.
4. (user) Taming is cut.
5. (user) New species arrive by boat, like Animal Crossing.
6. (user) Beasts come every 3, 4 or 5 nights: build-up, peak, release.
7. Pre-pillar: a capability opens when something the player builds or raises makes it
   possible, never on a clock or a stage line.
8. Pre-pillar: value enters only by the wave, the land, and new creatures; income grows
   only through what the player built.
9. Pillar: a reward is a new rule, verb, or board change, never a flat bonus or pile.
10. Pillar: roles emerge from raising, never from a purchase.
11. Pillar: black box with a clear interface; ban hidden effects; menu UI is readout only.
12. Pillar: add connections, not things; natural on sight; tone gate.
13. Antipatterns: stacked forecast constraints; micromanagement; memorization tables.
14. Invariant: a same-kind mechanic must make same-kind pairs meet.
15. Invariant: an aggregate that drives visible state sums on a fixed scale, never a mean.
16. Invariant: every self-reinforcing loop needs a bootstrap, a termination, a floor.
17. Invariant: time-based progression runs on the dilated clock.
18. LAW_life 7: a wild joins only with bed room (retired by rule 4; its vacancy contract
    remains for any arrival).

**Ledger rows tested against the rules:**
- 3.1 hand-act inflow vs rule 7: a hand act is neither "built" nor "raised". Rule 1 (user,
  newer) widens rule 7. **Narrow rule 7:** "or the player has done by hand". Raise to the
  user as a wording fix.
- 3.1 random lab find vs rule 2: a random pick has no requirement. Rule 2 retires
  randomness; the lab stays only as the requirement for cards with no hand act.
- 3.2 boat stay vs rule 10: if a pier is paid with gems and a species brings stat identity,
  the player buys a role (an owl = a future architect). Holds only if the stay is decided by
  what the player built (a served wish), not by the payment. Flag for c3.
- 3.2 boat vs rule 16: a visitor stays when its wish is served; serving needs stations,
  stations need workers. Bootstrap: the first boat must be satisfiable from the start state
  (start herd, open basics). Flag for c3.
- 3.2 boat vs rule 14: one visitor of a new kind cannot breed. Pair or more per arrival.
- 3.4 siege vs rule 7: the siege schedule is a clock, but it gates pressure, not a
  capability; consistent. A card that opens "after the first siege" would break rule 7.
- 3.4 countdown + preview + 5-wave forecast vs rule 13: show one forecast (the next siege),
  not three layers.
- 3.5 bounty per night vs rule 8: falls on the siege clock; allowed, but the loss is
  unmeasured (no balancing in this relay: log it as a balance question).
- 3.6 roll-up vs rule 15: counts, not means.
- 3.6 dawn line vs rule 11: the line must name the card that answers the problem, so the
  link is seen, not inferred.
- 3.3 vs rule 7: species arrival gates jobs by stats; a card opened before any creature can
  work it reads as a broken promise. The tree should know the stat gate (fork for c1/c3).

## 5. Three framings

**A. A gate graph over one stock (open cards).** The problem is a dependency graph whose
nodes are paid by counted events (acts, ticks, arrivals); every PR either pays a node or
reads the frontier. Makes easy: one save stock, one reader set, tests per node; PR 2 and 3
become views of the frontier. Hides: the action curve and the herd supply.

**B. A pressure cycle with a build window (period P, load L, capacity C).** The run is a
periodic load (siege every P nights) against a capacity the player builds in the calm
window; every other PR fills the window with the next useful act. Makes easy: the action
curve, and it exposes every counter that silently assumed "one wave per night" (difficulty,
bounty, stretch, autosave, forecast). Hides: what the player should do in the window.

**C. One attention channel ranking "next act" candidates.** Sources (frontier, last night's
damage, herd wants, countdown, a boat at the pier) compete for one bubble plus a few icons;
the problem is ranking and de-duplicating them. Makes easy: the purpose sentence ("always
knows what to do next and why"), PRs 2, 3 and 5's UI. Hides: whether the candidates exist
(it assumes the tree and the schedule).

**Pick: B for the stack, A inside c1.** Reason: the flagged breaks with the widest blast
cluster on one unit change (per night to per siege: 3.4, 3.5, 3.7) and on the herd inflow
swap (3.2, 3.3), both B's axes; A is the cleanest frame for PR 1 alone, and C is a view
layer that can be designed last once A and B fix what it ranks. C stays the acceptance test
for the purpose: at any dawn, one line names the next act and its reason.

## 6. Open questions this model raises (for the cluster designs)
1. Does `known` (lab curve) count hand-act opens? (c1)
2. Woodpile and mine are open at start; do they become hand-gated? (c1)
3. Who speaks at dawn: respawn a guide frog, or a different speaker? (c1)
4. What counts nights vs sieges: difficulty, bounty, autosave key, stretch, forecast? (c2)
5. Beast drops: gem, nothing, or a beast part? (c2)
6. Boat unit: visitors per boat (a pair or more), boats per what, and what pays the
   vacancy? (c3)
7. Does the tree know the stat gate, so a card opens only with a creature able to work it? (c1/c3)
