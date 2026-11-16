# BRAINSTORM: design cluster c2 (PR 4 beasts, PR 5 siege rhythm)

Design only. Code cites the worktree `mm-prog` at 6cb6d951. Picks tagged (user) come from
`docs/BRAINSTORM_design_progression.md` (main checkout); every other pick is (Claude), made in
AFK mode with `/design-idea` plus design-dialogue section 6, for the user to reverse.

## Forks closed (Claude), tldr each
1. **Beast kinds: two.** Bruiser (rams walls, marches on the statue) and Snatcher (climbs,
   goes for eggs and food on the ground). Reason: two kinds are the fewest that make the
   preview a decision (thicker walls and fighters at the wall, or a roof over the nest).
2. **What each attacks:** set by the existing targeting rules and wild gear, per kind, not by
   new code. Bruiser always carries a ram, Snatcher a ladder, once a creature-built piece
   stands. Reason: the gear on its back says on sight what it will do to your walls.
3. **Beast drops:** the existing wild drop (gem from the bounty, or its favorite crop while
   food runs low). No beast part. Reason: value enters by the wave (pillar); a part is a new
   noun only the user may add.
4. **Siege gap: growing, 3 then 4 then 5, then 5 forever** (sieges on nights 3, 7, 12, 17...).
   Reason: the first siege comes while the base is small and the threat is still remembered;
   later gaps grow with the build list. One constant.
5. **Nights between: calm** (no beasts). Reason: the curve needs contrast; nights already
   carry the herd's own trouble (rampagers, food thieves, sleep, eggs at dusk).
6. **Nights vs sieges:** one calendar (DayCycle night number); a siege is a pure function of
   it. Difficulty = the siege's night number, bounty per siege, autosave every nightfall,
   day stretch per night, forecast = the next siege only. Table in PR 5.
7. **Countdown + preview UI:** one clause on the existing top clock line, "⚔ siege in 2
   nights: 6 Bruisers", the next siege only. Reason: one forecast, never stacked layers.

References (research rings 4-5): 7 Days to Die horde night, a fixed gap (default 7) with an
optional random range, the sky turns red at the warning hour
([wiki](https://7daystodie.wiki.gg/wiki/Blood_Moon_Horde),
[config](https://xgamingserver.com/docs/7-days-to-die/blood-moon)); Don't Starve hounds, a
hidden gap that shrinks over days, announced by growls a minute before
([wiki](https://dontstarve.wiki.gg/wiki/Hound)); They Are Billions wave info shows when the
next wave comes and what it is ([changelog](https://steamcommunity.com/sharedfiles/filedetails/changelog/3037838563?l=danish));
Kingdom Two Crowns blood moons scale with the day count
([forum](https://steamcommunity.com/app/701160/discussions/0/1743355067112584456)). Shared
lesson: a big night on a known calendar plus a short visible warning; hidden windows suit a
survival game with no build-up promise, which this game has.

### PR 4: Beasts replace wilds; taming cut
- **Frame:** enemies today are the herd's own species and a downed one joins (taming, the main
  herd inflow); the player should instead face a distinct enemy kind that never joins.
- **Assumptions to verify:**
  - [x] Every wave species is a friendly species: `systems/waves/content/default_wave_config.tres` (bunny, frog, fox, owl, hedgehog).
  - [x] The starter herd reads the wave pool: `systems/level/components/intro_phase.gd:15-18` (`creature_pool(1)`). Cutting friendly species from the pool breaks it.
  - [x] A downed body lies in a free medic bed in reach, any side: `entities/creatures/creature.gd:719-720`, `:2779-2787` (`_take_bed_in_reach`, no hostile check).
  - [x] A wild mends in a bed only with housing room, then joins: `creature.gd:2330-2332`, `:3423-3424`, `:2966-2975` (`revive_friendly`, `Housing.vacancies -= 1`).
  - [x] Medic workers never treat a hostile: `creature.gd:3381` (`care` needs `not is_hostile()`).
  - [x] What a wild attacks is data: `creature_metadata.gd:159-182` (egg rule from `hunts_eggs`, food rule from `favorite_foods`, statue rank 0, allies rank 5; `creature_config.gd:239-243`).
  - [x] Gear is one random roll per spawn: `systems/waves/wave_system.gd:170-183`; it shows on the body (`weapon_component.gd:66-85`).
  - [x] A drop needs no friendly: `wild_drop_service.gd:15-23`, called from `perish` `creature.gd:3129-3130` and `light_wild.gd:208-210`.
  - [x] Friendly and hostile looks differ only by a mustache and tint: `content/bunny/bunny.tscn` vs `bunny_friendly.tscn` (diff: `Mustache` node, fur color). Primitive-mesh scenes exist to copy.
  - [x] Cheats spawn friendly species as WILD: `systems/cheats/cheat_coordinator.gd:425-445` (fight, owl, hedgehog), `:555-570` (drops), `:1042-1043` (lamp), `:1089-1100` (siege, swarm), list `:89-95`.
  - [ ] A TAMING food item is still placed anywhere (open: grep `.tres` for food type 2; `food_purpose_service.gd:14` only refuses it).
  - [ ] No other site turns a hostile body FRIENDLY (open: grep `update_state(State.FRIENDLY)` callers; only `revive_friendly` and calm-in-arms `creature.gd:2627-2628`, which needs FRIENDLY already).
- **Candidates:**
  - A. A beast dies at once (no DOWN body). Cut: loses the thrown-body stun verb (README "a thrown body stuns") and the beat of a fallen enemy on the field.
  - B. Keep beasts as friendly species with a "never tame" flag. Cut: breaks (user) "beasts are a new enemy kind, never friendly species".
  - C. Three kinds (add a herd hunter that picks friends over the statue). Cut for now: its prep (keep friends home, beds in rooms) overlaps the Snatcher's "inside" answer; log as a later kind.
  - D. One kind, sizes only. Cut: the preview then says only "how many", no prep decision.
  - E. **Two new kinds with their own look, kind-bound gear; a downed beast lies on the ground, never in a bed, and rots into its drop.** Survives.
- **Recommendation:** Scene: night 3, a hulking dark horned Bruiser with a battering ram on
  its back stomps at the wall; a friend knocks it down; it lies grey on the grass. The player
  carries it to the medic bed by habit: put down, it slides off and lies on the floor (no
  bed glow), blinks out a minute later and pops a gem. Night 7, lean striped Snatchers with
  ladders hop the low wall and run for the egg in the nest. No beast has a mustache: a
  mustache means a friend. Mechanism: the wave pool holds only beasts; a hostile body never
  takes a bed (one guard), so the recruit path is dead and is deleted; what each kind attacks
  is its targeting rules plus its gear.
- **Build sketch:**
  - New `entities/creatures/content/bruiser/{bruiser.tres,bruiser.tscn}` and `snatcher/...`:
    `.tscn` built from primitives like `bunny.tscn` (Bruiser: big dark capsule, two cone
    horns; Snatcher: small lean capsule, tall ears, striped tail). No `friendly_scene`
    (`creature_metadata.gd:140` already falls back). Stats copied, not tuned: Bruiser from
    `frog.tres` (180 HP, 26 dmg, speed 3.5, score 6), Snatcher from `bunny.tres` (45 HP,
    10 dmg, speed 6.5, score 2), `hunts_eggs = true`, `favorite_foods = [carrot]`. Targeting
    sub-resources copied from `fox.tres` (allies 20 m, statue 600 m).
  - `creature_metadata.gd`: `@export var gear: StringName = &""` (Identity group).
    `wave_system.gd:177-183` `gear_roll(tree, species)` returns `species.gear` once a
    creature-built piece stands, else `&""`; drop `WaveConfig.GEAR_SHARE` (`wave_config.gd:11`).
  - `default_wave_config.tres`: pool = Bruiser (`first_night` 1), Snatcher (`first_night` 7).
  - `creature.gd:2779` `_take_bed_in_reach`: return when `is_hostile()`. Then delete the dead
    recruit path: `:2330-2332` branch (use `ALLY_MEND_MULT`), `:3424` housing clause,
    `:2967-2974` `recruited` branch, `creature_config.gd:62` `RECRUIT_MEND_MULT`, `:221`
    `RECRUIT_WARMTH_STEP` (built: all deleted, `Housing.has_room` too). Keep `Housing.vacancies` (the boat stay pays it).
  - Starter herd: `intro_phase_config.gd` `START_SPECIES` = bunny, frog, fox paths (today's
    night-1 trio, so the (user) "random night-1 species" stays as built); `intro_phase.gd:15-18`
    picks from it. Drop `@export var wave_system` there if nothing else reads it.
  - Cheats: `BEAST_SPECIES` beside `HERD_SPECIES` (`cheat_coordinator.gd:89`); every WILD spawn
    (fight, owl/hedgehog second spawn, drops, lamp, wall/rampart, siege, swarm) uses it; HELP
    lines say "beast".
  - Counters that only read recruits go: `creature_tracker_ui.gd` 🫱, `balance_probe.gd:484-488`
    `recruits`, `headless_sim_driver.gd:86, 468, 856`.
  - Text: `run_hud.gd:21-22` tips, README lines 20-22, 107-111, 188 ("wild joins").
- **Tests + cheat key:**
  - `test_beasts.gd::test_a_downed_beast_never_takes_a_bed`: beast DOWN beside a free RECOVERY bed, tick behavior; assert not `_in_bed()`, state DOWN.
  - `::test_a_downed_beast_never_joins`: same, run past a full mend time (dilated clock); assert never FRIENDLY; on timeout it perishes and drops.
  - `::test_wave_pool_holds_no_friendly_species`: every pool entry not in `IntroPhaseConfig.START_SPECIES` nor the cheat `HERD_SPECIES`.
  - `::test_beast_gear_waits_for_a_built_piece`: `gear_roll` gives `&""` with no `CREATURE_BUILT` node, then the species' gear.
  - `test_intro_phase`: the starter herd is one species from `START_SPECIES`.
  - Delete `test_creature_down_state.gd:74-...` (recruit warmth). Cheat: F12 `/fight` spawns a beast; `/swarm` ten.
- **Shared with other clusters:** herd inflow: PR 4 removes the recruit inflow; PR 6 (c3) adds
  the boat stay, which pays `Housing.vacancies` (built: -2 per pair; `revive_friendly` no longer takes one). Friendly
  species list: `IntroPhaseConfig.START_SPECIES` is the first owner; c3 may move it to an
  arrival roster. PR 2 (c1) deletes the guide's "tame" line (`tutorial_guide.gd:63`).
- **Open questions for the user:**
  1. Kind-bound gear (every Bruiser a ram) replaces the 25% random roll: take it? Rec: yes, the gear is the kind's sign.
  2. Names Bruiser and Snatcher: rec keep (invented, so never a future friendly species).

### PR 5: Siege rhythm
- **Frame:** a wave every night gives no build-up or release; the player should see beasts
  come on a known schedule, every few nights, and see which beasts and when.
- **Assumptions to verify:**
  - [x] Every NIGHT starts a wave; DAWN ends it and refills the forecast: `wave_system.gd:60-69`.
  - [x] Wave number equals night number in play: `wave_system.gd:89-91` (+1 per night), DayCycle `world/day_cycle.gd:84-90, 104-106`; the `/33` cheat sets both alike (`cheat_coordinator.gd:1128-1135`).
  - [x] The forecast pre-rolls 5 waves at difficulty `wave + depth`: `wave_system.gd:72-79`, `forecast_component.gd:14-17`, `wave_config.gd:78`; synced to every peer with `first_night` (`:82-86`); `Wave.summary()` gives counts per kind (`metadata/wave.gd:14-23`). No UI reads it.
  - [x] Pool entries gate on difficulty as a night number: `wave_system.gd:207-213`.
  - [x] Bounty resets in `_start_night` only: `wave_system.gd:92`, `wild_drop_service.gd:11-12`.
  - [x] Autosave keys on the wave number at nightfall: `wave_system.gd:64-65`, `save_game.gd:34-36`.
  - [x] Day stretch reads the cycle index, not the wave: `day_night_config.gd:21-27`, `day_cycle.gd:104`.
  - [x] HUD clock line and banners: `run_hud.gd:73-84` (red warning before nightfall), `:167-173`, `:188-196`.
  - [x] Cheat name `siege` is taken (ring of walls, `cheat_coordinator.gd:1080-1093`).
  - [ ] Spike bench saves (`test/local/bench/saves/playtest_wave11/24.save`) land on calm nights 11 and 24 after this PR (open: bench then measures no wave; see questions).
- **Candidates:**
  - Gap: A. fixed 4. Survives as runner-up (simplest). B. **growing 3, 4, 5, then 5.** Survives. C. hidden window 3-5 with a late warning (Don't Starve). Cut: breaks the countdown the PR promises. D. random 3-5 rolled at the last siege, shown exactly. Cut: variety with no decision attached.
  - Calm nights: E. **fully calm.** Survives. F. a lone scout per coming kind the night before. Cut: a second forecast surface (stacked forecast). G. a small wave. Cut: flattens the peak.
  - Difficulty unit: H. **the siege's night number.** Survives: a longer gap brings a bigger siege, and the budget curve over the calendar stays as built. I. siege count. Cut: load falls behind a herd that grows every night, and every per-wave counter needs a second meaning.
- **Recommendation:** Scene: dawn of night 4. The top line reads "☀ Day 5 · night in 40s ·
  ⚔ siege in 3 nights: 8 Bruisers". The player builds walls. Night 5 falls with no banner and
  no beasts; the herd sleeps. Day 7 the clause turns "⚔ SIEGE TONIGHT: 8 Bruisers, 6
  Snatchers" and the clock goes red before dusk. Night 7: "🌙 NIGHT 7: SIEGE!" and the beasts
  march. Dawn: "🌅 SIEGE SURVIVED!" and the clause shows the next one, 5 nights out.
  Mechanism: one calendar (DayCycle). `WaveConfig.is_siege_night(n)` is pure; at each
  nightfall WaveSystem autosaves, then starts a siege only on a siege night (or a forced one).
  The forecast holds one pre-rolled wave for the next siege night.
- **Nights vs sieges (SPECIFY, one owner each):**
  | Value | Counts | Owner, lifecycle |
  |---|---|---|
  | night number n | nights | `DayCycle.cycle_index()+1`, saved there |
  | siege night | pure f(n) from `SIEGE_GAPS` | `WaveConfig`, no state |
  | difficulty | n of the siege | `WaveSystem.current_difficulty`, set at siege start |
  | `current_wave_number` | nights (= n) | WaveSystem, set each nightfall; probe and save key read it |
  | bounty | per siege | reset at siege start (no beasts spawn on calm nights) |
  | autosave | every nightfall, key n | `SaveGame.autosave(n)` |
  | day stretch | nights | `DayNightConfig`, unchanged |
  | forecast | next siege only | `ForecastComponent`, depth 1, refilled at DAWN when empty |
- **Build sketch:**
  - `wave_config.gd`: `const SIEGE_GAPS := [3, 4, 5]` (last repeats); `static func
    is_siege_night(n) -> bool`, `static func next_siege_night(after_n) -> int` (first siege
    night > after_n). `FORECAST_WAVES := 1`. Fix the "spike nights" comment (`:30-32`).
  - `wave_system.gd`: `var force_siege := false` (TRANSIENT). `_on_phase_changed` NIGHT:
    `current_wave_number = night`; autosave; `if force_siege or is_siege_night(n):
    _start_siege()`. `_start_siege` = today's `_start_night` minus the `+= 1`; a forced siege
    generates fresh at difficulty n and leaves the queue. DAWN: `_end_night()`, refill.
    `_wave_at(_)`: `current_difficulty = next_siege_night(n_now)`; sync `first_night` = that
    night. `static func siege_line(night_now, summaries, siege_night) -> String`.
  - `run_hud.gd`: clock line appends `siege_line` (`:80`); red warning (`:76`) only on a siege
    day; `banner_text(phase, night, siege)` (`:167-173`): siege night and its dawn only.
  - Cheat `"raid"` (folder world): `force_siege = true`, then `run(player, "night")`. The
    `/33`-style cheats set `force_siege` too (`:1128-1135`), so their budget stays wave N's.
  - Docs: `LAW_save.md` rule 2 "every wave" becomes "every nightfall"; README night lines.
- **Tests + cheat key:**
  - `test_siege_schedule.gd::test_siege_nights_follow_the_gaps`: `is_siege_night` true at 3, 7, 12, 17, 22, false at 1, 2, 4, 6, 8, 13.
  - `::test_next_siege_night`: from 0 is 3, from 3 is 7, from 12 is 17.
  - `::test_a_calm_night_spawns_nothing`: NIGHT on n=2: `current_wave == null`, bounty untouched.
  - `::test_a_siege_night_starts_a_wave_at_its_night`: n=7: wave set, `current_difficulty == 7`.
  - `::test_force_siege_on_a_calm_night`: flag set, n=5: wave at difficulty 5, queue kept.
  - `::test_forecast_holds_the_next_siege`: after DAWN of night 3, one queued wave, `first_night == 7`.
  - `test_run_hud.gd::test_siege_line`: "siege in 2 nights", "SIEGE TONIGHT", names with counts; calm-night banner empty.
  - Update `test_wave_budget.gd` / `test_wave_generation.gd` for depth 1. Cheat: `/world raid`.
- **Shared with other clusters:**
  - **Dawn hook:** `DayCycle.phase_changed(DAWN)`, no new signal. WaveSystem refills there; a
    reader of the preview (the frog, PR 2) calls deferred so the refill lands first.
  - **Next siege readout:** `WaveSystem.siege_line(...)`, pure, client-safe (forecast is
    synced). The frog (PR 2) speaks it; boats (PR 6) may key "a calm day" on
    `!is_siege_night`.
  - **Calendar owner:** DayCycle night number; boat timing (c3) should read it, not count.
- **Open questions for the user:**
  1. Gap: growing 3, 4, 5 (rec) or fixed 4?
  2. Spike bench saves (nights 11, 24) now load calm: re-capture after the stack (rec) or add a force flag to `spike_bench.sh`?

## Balance questions (log only, no tuning)
- Kill gems fall from 3 a night to 3 a siege (about a quarter): keep, or scale the bounty with the gap?
- Beast stats are copied from frog and bunny; with taming cut the herd grows only by eggs (and boats after PR 6): siege budget vs herd size needs a playtest.
- Calm night length: nights keep their full length with nothing to fight.

## Prune log
- Beast flag on the species: cut; "never friendly" holds from data (pool disjoint from the friendly lists, a test) plus the state guard.
- `first_night` rename to `first_siege`: cut; difficulty stays a night number, so the name stays true.
- Siege counter state: cut; the schedule is a pure function of the night number.

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
