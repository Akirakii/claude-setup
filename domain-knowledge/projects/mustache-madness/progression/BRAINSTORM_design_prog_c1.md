# BRAINSTORM: cluster c1 (PR 1 tree, PR 2 frog at dawn, PR 3 glance icons)

Design only (AFK). Picks are "(Claude)" with a one-line reason; the relay closes them, the
user reverses on return. Ledger, rules and framings: `docs/BRAINSTORM_design_abstract.md`
(cited as "abstract 3.x" / "rule N"). Code: worktree `mm-prog` at 6cb6d951. Prior art marked
"(memory)" is recalled, not fetched.

**Frame for c1 (framing A in the abstract):** one stock, the open cards; a hand act or the
lab pays a node; the frontier, the dawn line and the glance icons are three views of "what
to do next". PR 1 builds the stock, PR 2 and PR 3 read it.

### PR 1: Requirement tree (walking skeleton)
- **Frame:** a locked card opens when the player meets its one requirement (a hand act, or
  the lab), and the Work tab shows what is next, so the player sees "do this, get that".
- **Assumptions to verify:**
  - [x] Only the lab opens cards in play, at random: `lab.gd:41`, `blueprint_registry.gd:392-395`.
  - [x] Locked cards are never drawn: `build_menu.gd:110-116` reads `BuildHand.buildable()` (`build_hand.gd:29-32`).
  - [x] Requirement field exists: `Blueprint.opens_when` (`blueprint.gd:105-106`), BASICS key `opens` (`blueprint_registry.gd:311`).
  - [x] Cause text already routes per key: `CAUSES` (`:15-18`), `cause_text` (`:359-365`); banner reads it (`run_hud.gd:139`).
  - [x] Hand-act sites: axe RPC `network_manager.gd:414-422` (tree `WorldTree`, ore `GemOre`), `Creature.grab` `creature.gd:2484`, `_try_jail` `creature.gd:2694`, `Egg.grab` `egg.gd:121`.
  - [x] `known()` counts only `"lab"` keys (`:399-400`), so hand opens never raise the lab curve (answers abstract Q1).
  - [x] Godot 4 `Dictionary` keeps insertion order, so `_cards` order is the authored order (engine docs, Dictionary).
  - [x] No species hard-gates a job: every species' INT cap is above the top job need (architect INT 12; caps 20-38, `docs/LAW_life.md` species table; reqs `creature_config.gd:283+`). The tree needs no stat gate (answers abstract Q7).
  - [ ] A first-minute player chops before anything else (assumed; playtest).
- **Candidates:**
  - A. Hand act opens its card **at once** (first act). Survives.
  - B. Hand act opens after **N acts** (a hidden count). Cut: a counter the player cannot see (rule 11); N is a balance number.
  - C. Hand act **aims the lab** at the card; the lab still pays. Cut: two payers for one node, and the hand act does nothing you can see.
  - D. Lab picks **at random** among lab cards (today). Cut: rule 2 (one requirement, a known next step).
  - E. Lab researches the frontier lab cards **in authored order**. Survives (skeleton).
  - F. Lab aims at the card that answers the **herd's top want** (reads PR 3). Survives, lands in PR 3.
  - Prior art (memory): Factorio (mine by hand, then the drill), the Minecraft recipe book
    (picking up an item unlocks its recipes), Stardew crafting by skill level. All open on the act itself, at once.
- **Recommendation:** A + E, then F in PR 3 (Claude: the act and its reward meet in one
  moment, and the lab keeps a visible target instead of a dice roll).
  Scene: on minute one the Work tab shows a grey Woodpile with a ✋ and "chop a tree". The
  player fells a tree, the banner pops "🔓 Woodpile: you chopped a tree", and the card turns
  live with its yellow "new" mark. Beside it a grey Police Box shows ✋ "jail a friend" and,
  one step further, a dim Bank. The lab's counter reads "🔬 Kitchen 2/6", not "🔬 2/6".
  Mechanism: each card has one requirement `kind:arg` (`hand:<act>`, `lab`, or none) and one
  `after` parent id. A card is **reachable** when its parent is open (or it has none). A
  hand act opens every reachable locked card that has that act. The lab opens the first
  reachable `lab` card in `_cards` order. Frontier = reachable locked cards (step 1) plus
  locked cards whose parent is step 1 (step 2).
  Hand map (Claude): chop -> Woodpile; axe ore -> Mine; carry a downed friend -> Emergency
  Post (`med_kit`); jail a friend -> Police Box (after Jail); carry an egg -> Nest. Woodpile and
  Mine lose open-at-start (answers abstract Q2: rule 1 says every job starts by hand; both
  acts are the first things a player does). Every other locked card stays `lab`, after Lab.
  `bank.brings police_box` stays (a problem arrives with its answer).
- **Build sketch:**
  - `blueprint.gd:105-108`: keep `opens_when` (one entry); add `@export var after := ""`.
  - `blueprint_registry.gd`: BASICS woodpile `:156-164` add `"opens": ["hand:chop"]`; mine
    `:226-234` `["hand:mine"]`; med_kit `:242` `["hand:carry_down"]`; `_basic` `:311` reads `after`.
    Pool: `police_box.tres` `opens_when=["hand:jail"]`, `after="jail"`; `nest.tres` `["hand:egg"]`;
    the other pool cards `after="lab"`.
  - Registry new: `hand_act(act: StringName)` (server; calls `unlock(id, "hand:"+act)` for each
    reachable match), `reachable(bp)`, `frontier() -> Array` ([bp, step]). `findable()` `:392`
    adds `reachable`. `CAUSES` gains `hand:chop` "you chopped a tree", `hand:mine` "you
    axed the ore", `hand:carry_down` "you carried a downed friend", `hand:jail` "you jailed a
    friend", `hand:egg` "you carried an egg".
  - Act sites (server, player holder only): `network_manager.gd:420` after `hit_by_axe`
    (`WorldTree` -> chop, `GemOre` -> mine); `creature.gd:2484` when `holder is Player` and DOWN
    from FRIENDLY; `_try_jail` `creature.gd:2702` when `holder is Player`; `egg.gd:121` when `holder is Player`.
  - `lab.gd:41` `pool[0]` in place of `GameRng.pick`; `lab.gd:52-58` shows the target name.
  - `build_menu.gd:110-116` adds frontier cards to their tab (their own category; most are
    Work); `_card` `:202` draws a locked face (grey picture, requirement icon ✋/🔬/🔨 + one
    words line in place of the price, step 2 dimmer); `_pick` `:264` ignores a locked card.
    Q/E and the hotbar keep `buildable()` only.
  - New config: none (icons and words live beside `CAUSES`).
- **Tests + cheat key:** `test/ci/systems/progression/test_requirement_tree.gd`:
  `test_chop_opens_woodpile` (hand_act chop: open, cause "hand:chop"); `test_hand_act_needs_parent`
  (jail act with Jail locked: Police Box stays locked); `test_lab_opens_first_reachable`
  (two lab cards: first in order opens); `test_frontier_two_steps` (steps 1 and 2, nothing at 3);
  `test_known_ignores_hand`; `test_save_round_trip_keeps_hand_cause`. Cheat: `unlock` (kept,
  `cheat_coordinator.gd:365`).
- **Shared with other clusters:** `hand_act` is the **open-card trigger** c3 can call for a
  species arrival (`hand_act(&"arrive_owl")` or a sibling `trigger(key)`): name one owner, the registry.
- **Open questions for the user:**
  1. Hand act opens at once (rec) or after N acts.
  2. FARM and HAUL get hand acts later (harvest a crop, carry a log) or stay lab (rec: lab for now).

### PR 2: Frog guide at dawn
- **Frame:** at each dawn one frog line names last night's worst problem and the card that
  answers it, so the player starts every day with a reason and a next act.
- **Assumptions to verify:**
  - [x] No guide is spawned: `TutorialGuide.new` left in #235 (d09fc993); grep finds no caller. The old guide rode a herd frog (`intro_phase.gd`, pre-#235).
  - [x] The director's corn ask locks the line until the frog is fed (`guide_director.gd:95-96`): any new speaker must drop it.
  - [x] Stale lines: van `:28,:42,:49`, Fuse Cube `:41,:48`, well `:58,:63`, tame `:63`, beds with crops `:27`, "lab discovers" `:22,:24`; HUD tip `run_hud.gd:22` ("wilds join").
  - [x] Night events exist on the bus: `creature_down` per friend (`creature_guide_watcher.gd:66-71`); a friend lost = despawn while DOWN (`:40-44`). Statue hits are not on the bus (`statue.gd` health only).
  - [x] Dawn hook exists: `DayCycle.phase_changed` DAWN (`wave_system.gd:67`, `run_hud.gd:130`).
  - [ ] The bubble shows only on the host (`docs/TODO_guide_system.md`); single player is the main path (assumed fine).
- **Candidates:**
  - A. **A frog sitting on the statue** hosts `TutorialGuide`: never dies, always at the centre, frog mesh reused. Survives.
  - B. Host on a starter-herd creature (as before #235). Cut: the herd is one random species, rarely a frog, and the guide dies with it.
  - C. A HUD banner at dawn, no frog. Cut: the user named a frog; loses the one existing speaker visual.
  - D. A 4th starter frog in the herd. Cut: a lone frog can never breed (kin rule, `creature.gd:2127`).
  - Prior art (memory): Animal Crossing New Horizons, Isabelle's morning announcement (one daily line at a fixed spot); Don't Starve's opening Maxwell line.
- **Recommendation:** A (Claude: a speaker that cannot die, at the place the player
  returns to, in the existing bubble). Scene: dawn breaks, the gold "Dawn" banner pops, and
  the frog on the statue says "❗ 2 friends went down last night. Build an Emergency Post
  (✋ carry a downed friend)." The line holds through the morning; a live urgent tip
  (hurt friend) still cuts in. On a quiet night it says the next frontier card instead.
  Mechanism: a **night log** counts bus events from NIGHT to DAWN by kind. At DAWN the
  director ranks problems (friend lost > friend down > statue hit), takes the top non-zero
  one, and maps it to a fixed answer list (lost/down -> med_kit, medic_bed; statue hit ->
  wall). It names the first answer not yet built: an open card says "build X", a locked one
  says its requirement (from PR 1 `frontier`). No problem -> the first step-1 frontier card.
  A **first-time line** (a problem's long explanation) shows once per run, then the short form.
  Director layers become: urgent > dawn line > chore > base pool. Corn ask, watering can,
  chaos reveal, van, well and breed tips are deleted.
- **Build sketch:**
  - `statue.gd` `_build_body`: add a frog `MeshInstance3D` (`entities/creatures/content/frog/frog_mesh.tres`) on top and, on the server, `TutorialGuide.new(frog)`.
  - `guide_director.gd`: delete `:17-28` stale consts (keep `HURT_*`, `COLLECT_GEM`, `PLANT_CROPS`), `CHAOS_*` `:38-50`, `enemy_down` `:62-63`; reword `creature_down` `:58` ("carry it to a medic bed"); drop `_corn_fed`/`_watercan_pending` locks `:95-98`, `on_corn_fed`, `on_chaos`. Add `night_log: Dictionary`, `on_night()`, `on_dawn(answer: Callable)` and `DAWN_RANK`, `ANSWERS` consts.
  - `tutorial_guide.gd:76-82`: drop `Blueprints.unlocked` and `fed` wiring; connect `LevelManager.day_cycle.phase_changed` to `on_night`/`on_dawn`; the answer callable reads `Blueprints.frontier()`, `is_unlocked`, `built_count`, `cause_text`-style requirement words.
  - `guide_bus.gd:30-37`: report `statue_hit` from `Statue.health.damaged` (server).
  - `run_hud.gd:22`: drop the taming tip (c2 PR 4 may own it; flag).
  - New config: `GuideDirector.DAWN_HOLD_SEC` (how long the dawn line leads, real clock, UI pacing).
- **Tests + cheat key:** `test_guide_director.gd` (exists): `test_dawn_picks_worst`
  (2 downs + 1 statue hit -> down line); `test_dawn_names_requirement_when_locked`;
  `test_dawn_quiet_night_names_frontier`; `test_first_time_line_once`; `test_no_corn_lock`.
  Cheat `dawn`: logs one friend down and fires `on_dawn` now.
- **Shared with other clusters:** the **dawn hook** (one DAWN listener that also refreshes
  c2's countdown and c3's boat call); the **next-siege readout**: on a quiet night before a
  siege the line says "Beasts in N nights" (c2 owns the count, PR 2 reads it); the **night
  log** is the per-night tally c2's siege report could reuse.
- **Open questions for the user:**
  1. Speaker: a frog on the statue (rec) or back on a herd creature.
  2. Problem set for the skeleton: lost, down, statue hit (rec); hunger and theft later.

### PR 3: Glance icons for herd wants
- **Frame:** the herd's top 2-3 unmet wants show as small HUD icons, so the player reads
  what the city lacks without walking the herd.
- **Assumptions to verify:**
  - [x] Each creature's head glyph is replicated (`creature.gd:264-269`, sync `:415`, set `:2366`), red sign too (`:256-262`), so every peer can roll up.
  - [x] Glyph to icon exists: `StatusEmojiComponent.BALLOONS` + `_want` (`status_emoji_component.gd:13-19,46-54`), `OfferPlace.wish_icon` (`offer_place.gd:131-139`).
  - [x] A wish shows only when no place it would walk to has room (`offer_place.gd:98-106`), so a wish is already "unmet".
  - [x] HUD has a readout column to extend (`run_hud.gd:44-58`).
- **Candidates:**
  - A. **Count per want**, top 3 by count, red ones first, icon + count, under the status line. Survives.
  - B. Mean need level per kind as bars. Cut: a mean falls when a content creature joins (rule 15), and bars are not wants.
  - C. A list of named creatures. Cut: per-unit tracking (antipattern).
  - D. A single "worst want" icon. Cut: user asked for 2-3.
  - Prior art (memory): RimWorld's alert stack, The Sims needs panel, Two Point Hospital's
    patient-complaint summary: counts of a complaint, not averages.
- **Recommendation:** A (Claude: a fixed-scale count never drops when a weak member joins,
  and it reuses the balloons the player already knows). Scene: three small balloons sit
  under the gem and wood line: a red 🍎 "4", a white 🛏 "2", a white dining balloon "1". The
  player builds a bed; at the next refresh 🛏 drops out. Lab tie-in (PR 1 candidate F): the
  lab's next target is the frontier lab card whose place glyph matches the top want, else
  authored order (Claude: the tree's requirement becomes "the need its card serves").
  Mechanism: every 1 s, count FRIENDLY creatures by want key (glyph without `💭`, red
  counted separately), sort red first then by count, keep 3.
- **Build sketch:**
  - New pure util `ui/hud/want_rollup.gd` `static func top(glyphs: Array, reds: Array, n) -> Array` (unit-testable).
  - `run_hud.gd`: an `HBoxContainer` under `_status` (`:50-56`); a `REFRESH_SEC` timer reads the `"creatures"` group's `head_glyph` and `red_sign()`; icons from a static form of `StatusEmojiComponent._want` (food -> favorite of the most common hungry species).
  - `blueprint_registry.gd` `findable`/lab target: a `top_want` reader for candidate F (place glyph from the card's `place_meta` behaviour, as `build_menu.gd:237`).
  - New config: `RunHud.WANT_ICONS := 3`, `WANT_REFRESH_SEC := 1.0` (UI pacing).
- **Tests + cheat key:** `test_want_rollup.gd`: `test_counts_not_mean` (adding a content
  creature never lowers a count); `test_red_first`; `test_top_n_cap`; `test_no_wants_empty`.
  Lab: `test_lab_aims_top_want`. Cheat: `needy` (exists, `cheat_coordinator.gd:541`: hunger and sleep to 0, so 🍎 and 🛏 show).
- **Shared with other clusters:** the **want roll-up** is the reader c3's "does the visitor
  stay" test can share (a visitor's wish met = its key not in its own balloon).
- **Open questions for the user:**
  1. Icon count 3 (rec) or 2.
  2. Lab aims at the top want (rec) or keeps authored order only.

## Shared mechanisms (one owner each)
| Mechanism | Users | Proposed owner |
|---|---|---|
| Dawn hook (one DAWN listener fan-out) | PR 2 line, c2 countdown and siege preview, c3 boat call | `DayCycle.phase_changed` as is; each reader connects, no new hub |
| Next-siege readout ("beasts in N nights") | c2 countdown HUD, PR 2 quiet-night line | c2 (`WaveSystem`), PR 2 reads |
| Open-card trigger (`hand_act` / `trigger(key)`) | PR 1 hand acts, c3 species arrival | `BlueprintRegistry` |
| Night log (per-night tally) | PR 2 dawn pick, c2 siege report | `GuideDirector` for now; move down if c2 needs it |
| Want roll-up | PR 3 HUD, PR 1 lab aim, c3 visitor stay | `want_rollup.gd` util |

## Forks closed (Claude), for the relay log
- Hand act opens at once: the act and its reward meet in one moment.
- No-hand-act jobs: lab, first reachable in order, aimed by the top want after PR 3.
- Woodpile and Mine become hand-gated: rule 1, and both acts come first anyway.
- Speaker: a frog on the statue: cannot die, always at the centre, no new verb.
- Tree ignores species stats: no species hard-gates a job.

## Round 2 changes (relay picks, AFK; these override the doc above)
- PR 1 (Claude): a hand act opens its card at once. Why: cause and effect read on sight; a hidden count of N is a memorization table.
- PR 1 (Claude): FARM and HAUL stay on the lab; woodpile and mine become hand-gated (chop, axe ore). Why: walking skeleton, only the 5 acts the PR list names.
- PR 1 (Claude): the lab opens the first reachable lab card in authored order, not at random and not aimed at the top want. Why: predictable, one path; aiming is a hidden link (TODO).
- PR 2 (Claude): the frog sits on the statue and speaks there. Why: it cannot die and stands where the player defends.
- PR 2 (Claude): dawn problems ranked friend lost > friend down > statue hit; quiet night names the next frontier card. Why: the three the code already reports; hunger and theft later.
- PR 3 (Claude): 3 glance icons, count per want, red first. Why: PR list allows 2-3; counts, not means.
- PR 4 (Claude): 2 beast kinds, Bruiser (ram, statue) and Snatcher (ladder, eggs and dropped food, from night 7); gear bound to the kind, not rolled. Why: few kinds, each attack reads from its gear.
- PR 4 (Claude): beast drops stay the WildDropService gem/crop; no beast part. Why: no new noun.
- PR 4 (Claude): one friendly species list owned by PR 4 (FRIENDLY_SPECIES, starter subset START_SPECIES); boats read it. Why: one owner.
- PR 5 (Claude): growing gap 3, 4, 5 then 5 (sieges on nights 3, 7, 12, 17, ...); nights between are calm. Why: a clear build-up, peak, release; calm reads as the build window.
- PR 5 (Claude): difficulty = the siege's night number; bounty per siege; autosave every nightfall; forecast shows the next siege only (one HUD clause). Why: budget curve unchanged; avoids stacked forecasts.
- PR 5 (Claude): PR 5 adds the next-siege line to the frog's dawn pick (PR 2 lands first and cannot read it).
- PR 6 (Claude): a pier on the shore (wood, open at start); at any dawn while 2 beds stand free, the oldest pier docks one boat with a pair of one species, which steps off and takes the beds; no free beds, no boat (Round 3 replaced "release dawn only, stay if beds by dusk"). Why: Animal Crossing visitor, a pair founds a lineage, beds are the occupied shared state.
- PR 6 (Claude): species = one not yet in the herd, else the rarest; no frontier stat link. Why: c1 checked there is no stat gate, so the link would be invisible.
- PR 6 (Claude): once all species are in, keep sending pairs of the rarest. Strict one bed each.
- Process (Claude): relay wrote round 2 picks into each design doc itself instead of a designer round. Why: picks were small, saves three agent rounds.

## Round 3 changes (cold review; override all above)
- Cold review fix, PR 6 (Claude): a boat no longer keys on the siege calendar (a clock, against the "never on a clock" pre-pillar). At dawn, a pier with 2 free beds calls one boat with a pair; the pair takes the beds. No free beds, no boat; the pier shows the bed wish balloon. Why: arrivals follow beds the player built.
- Cold review fix, PR 1 (Claude): the tree has real parents (built): medic_bed after med_kit; cart_shed after woodpile; rail after cart_shed; rail_loader, rail_unloader after rail; lectern after library; chalkboard after library; treadmill after gym; bar after kitchen; shop after bar; bank after shop; police_box hand:jail after jail; nest hand:egg; woodpile hand:chop; mine hand:mine; med_kit hand:carry_down. Other lab cards have no parent.
- PR 1: lab re-posts RESEARCH when a card opens (findable can grow); tested.
- PR 2 + PR 5 (Claude): on a calm dawn the frog names the frontier card only; the siege line is spoken only on siege eve. PR 2 owns the guide text, PR 4 the run_hud taming tips.
- PR 3 / PR 6: lab aiming at the top want and "wanted-stat first" species pick are cut (not built).
- PR 4: guard the mend path too (a hostile in a bed never mends); FRIENDLY_SPECIES lives in CreatureConfig, intro and cheats read it.
- PR 5: on load, a forecast queue longer than the forecast depth is dropped.
- PR 7: TODO item for FARM and HAUL hand acts (deferred, not decided).
