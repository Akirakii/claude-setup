# BRAINSTORM: cluster c3, boat arrivals (PR 6)

Design only. Code claims cite the worktree `mm-prog` at 6cb6d951. Picks tagged (Claude) are
AFK picks the user may reverse; (user) picks come from `docs/BRAINSTORM_design_progression.md`.
Terms: **pier** = a new outdoor build piece on the island's edge. **Boat** = a visual that
sails to a pier and carries **visitors**. **Cargo** = the visitors' species. **Release dawn**
= the first dawn after a siege night (PR 5's word). **Stay** = the visitors step onto the
island as herd members.

### PR 6: Boat arrivals (like Animal Crossing)
> **Superseded in part (Round 3, built):** a boat docks at any dawn while 2 beds stand free, not only on a release dawn, and its pair steps off at once; "release dawn" and "stay if beds by dusk" below are the first-round design, not the build.
- **Frame:** taming is cut (PR 4), so the herd needs a new source of new species; the player
  should see a boat bring a pair of a new kind and know the one thing that makes them stay
  (a free bed each) before the boat leaves at dusk.
- **Assumptions to verify:**
  - [x] No water, shore or boat exists: grep of `world/`, `systems/level`, `systems/waves`
    and all `.tscn` finds none. The map is a 90 x 100 m plateau (`procedural_terrain.gd:21`);
    bodies off the edge fall and wrap back (`world_wrap.gd:3-9`).
  - [x] The terrain footprint is known at runtime: `game.gd:111-115` sets
    `WorldWrap.set_landing` to the terrain's half size.
  - [x] Join-by-bed contract exists: `Housing.vacancies` = free sleep beds less the unhoused
    (`housing.gd:11`, :203-209), `has_room` :256-257; a join takes one (`creature.gd:2971-2974`,
    with 🎉 emote).
  - [x] Bed balloon exists for "waits for a home": `creature.gd:1278-1279`;
    `StatusEmojiComponent` needs only a parent Node3D (`status_emoji_component.gd:77`, :147)
    and maps `💭🛏` to the bed icon (:13-19).
  - [x] A species' `friendly_scene` is meshes only, no script (`owl_friendly.tscn:73-127`):
    it can ride a deck as a passenger visual.
  - [x] `spawn_creature(meta, FRIENDLY, pos)` makes an adult (`spawn_coordinator.gd:44`,
    `is_baby` false); kin = same species name (`creature.gd:3230-3231`), so a pair can breed.
  - [x] Dawn and dusk hub: `game.gd:288-295` (dusk breeding, dawn greet), server only.
  - [x] Only autosave is at NIGHT start (`wave_system.gd:64-65`, the only call site), after
    dusk: a boat is never in a save. No save field needed.
  - [x] Placement already has a per-piece rule plus a hint: `needs_room` (`placed_behavior.gd:23`,
    :142-143, :69) and "· needs a floor" (`build_hand.gd:209`, :345-349).
  - [x] Bed card is open from the start (`blueprint_registry.gd:117-124`, no `opens`): the first stay is
    reachable from the start state (rule 16 bootstrap).
  - [ ] Open: what the player sees past the terrain edge today (void, sky?): judge the water
    plane in the first playtest screenshot.
  - [ ] Open: PR 5 exposes "last night was a siege" at dawn (shared, below).
  - [ ] Open: PR 4 moves the friendly species list off the wave pool (`intro_phase.gd:16-19`
    reads `creature_pool(1)`), shared, below.
- **Candidates:**
  - Pier + boat at each release dawn, pair stays on 2 free beds, else leaves at dusk: survives.
  - Boat every dawn while a pier stands (ACNH plot: build a bed, someone moves in): cut, the
    boat stops being an event and beds become a creature shop with no deadline.
  - Boat on its own clock every K dawns (ACNH campsite odds): cut, a second rhythm on top of
    the siege rhythm (abstract 3.4 flag) and a clock-gated capability (rule 7).
  - Visitors as real creatures in a new VISITOR state on the pier: cut, a fifth creature
    state touches every state ladder (`is_hostile`, `Housing.member`, groups) for a wait.
  - Visitors walk in from the map edge, no boat: cut, it is not a boat (user) and reads as
    the old wild walk-in.
  - Stay on a species wish (owl wants a lectern): cut, a species-to-place table to memorize,
    and a deadlock when that place needs the species' own stats (rule 16).
- **Recommendation:** The player builds a little wooden pier on the island's edge. The dawn
  after a siege, a boat sails in from the sea and bumps against it: two owls on the deck, a
  white bed balloon over the boat. The herd has one free bed. The player chops, places a
  second bed before dusk; the owls hop off onto the pier with 🎉 and wander in. Had the
  player not, at dusk the boat turns and sails off with them. Mechanism: one boat per release
  dawn docks at the oldest pier; cargo = a pair of one species, picked by `next_species`
  (below); while docked, each second the pier checks `Housing.vacancies >= BOAT_PAIR`; on
  yes it spawns the pair FRIENDLY at the pier's land end, takes 2 vacancies, marks Housing
  dirty, clears the cargo; at dusk any cargo leaves. No gem price (rule 10: stay is decided
  by beds built, never paid).
- **Build sketch:**
  - New `entities/builds/pier/` (`pier.gd`, `.tscn`, `.tres`, icon), copied from the chair
    layout (`entities/builds/chair/chair.tres`). `pier.gd extends GridObject`: replicated
    `cargo: String` (species .tres path, "" = no boat) via `ReplicationUtil.synchronizer`
    (as `offer_place.gd:56`); setter shows or hides a child `Boat` (hull box + mast + sail
    meshes, `cargo` species' `friendly_scene` x2 on deck, a `StatusEmojiComponent` set to
    `OfferPlace.THOUGHT + CreatureConfig.BED_GLYPH`) and tweens it in from offshore
    (cosmetic, local per peer). Static `dawn(tree, siege_ended)`, `dusk(tree)`,
    `next_species(tree)` (pure), tallies `boats`, `stayed`, `left` for BalanceProbe.
  - `game.gd:291-295`: DUSK calls `Pier.dusk`; DAWN calls `Pier.dawn(tree, <PR 5 fact>)`.
  - `placed_behavior.gd`: export `shore := false`; `can_place_block` (:136-145) rejects a
    footprint with no cell inside `PierConfig.SHORE_BAND` of the `WorldWrap.land_min/max`
    XZ edge; `build_preview` adds `"no_shore"`; `build_hand.gd:345-349` adds "· needs the shore".
  - Boat dock point = pier origin + the nearest edge's outward normal x `BOAT_DOCK_M`.
  - Registry BASICS row `pier` (beside `bed`, `blueprint_registry.gd:118`) (OUTDOORS, wood only, open at start unless c1 gates it).
  - Water: one `MeshInstance3D` PlaneMesh under the terrain in the level scene, flat toon
    blue, no collision (falls still wrap).
  - New config `entities/builds/pier/pier_config.gd`: `BOAT_PAIR := 2`, `SHORE_BAND`,
    `BOAT_DOCK_M`, `BOAT_SAIL_M`, `BOAT_SAIL_S`, `STAY_CHECK_S := 1.0`. Check on the pier's
    `LocalClock` (dilated, as `offer_place.gd:44`).
  - Reused: `SpawnCoordinator.spawn_creature`, `Housing.vacancies` / `mark_dirty`, `emote("🎉")`,
    `StatusEmojiComponent`, `friendly_scene`, the grid spawner (no new MultiplayerSpawner).
- **Tests + cheat key:** `test/ci/entities/builds/test_pier.gd`:
  `test_release_dawn_docks_a_pair` (cargo set, `boats` +1); `test_calm_dawn_brings_none`;
  `test_no_pier_no_boat`; `test_one_boat_for_two_piers` (oldest gets it);
  `test_pair_stays_on_two_free_beds` (2 FRIENDLY of cargo species, vacancies -2, cargo "");
  `test_pair_waits_on_one_bed` (no spawn, cargo kept); `test_boat_leaves_at_dusk` (cargo "",
  `left` +1, no spawn); `test_shore_rule` (inland false, edge band true).
  `test_next_species`: the wanted-stat species not in the herd first; else one not in the
  herd; else the herd's rarest. Cheat `/boat` (folder "world", `cheat_coordinator.gd:125`
  HELP table): dock a boat now at the oldest pier, putting one at the shore nearest the
  player when none stands; bind a free F/letter key if one is left (builder checks
  `cheat_coordinator.gd:6-32`).
- **Shared with other clusters:**
  - **Dawn hook (c1 PR 2, c2 PR 5):** `game.gd _on_day_phase` is the one dawn/dusk hub; the
    frog line, the countdown and the boat all hang off it. One owner: c2 (lands first).
  - **Siege-ended fact (c2):** a read at dawn, e.g. `WaveSystem.siege_last_night()`. Until
    PR 5 lands, every night is a siege, so every dawn is a release dawn.
  - **Friendly species roster (c2 PR 4):** intro and boat both need the friendly species once
    waves turn to beasts: one list (e.g. `CreatureConfig.FRIENDLY_SPECIES`), two readers.
  - **Tree's species pick (c1, abstract Q7):** c1 exposes the highest stat a frontier card's
    job asks that no herd member meets (`CreatureConfig.JOBS[*].req`, `creature_config.gd:283`);
    `next_species` maps it to the species with the top base in that stat (owl INT 13,
    hedgehog STR 11). Empty until c1 lands: fall back to a species not in the herd.
  - **Herd inflow (c2 PR 4):** PR 4 cuts the recruit branch of `revive_friendly`
    (`creature.gd:2971-2974`); the boat stay becomes the only vacancy taker besides bed
    claims. Keep `Housing.vacancies` semantics as is.
  - **Pier on the frontier (c1, PR 2):** the dawn line can name "build a pier" or "beds for
    the visitors"; the pier's own requirement is c1's call (recommend open at start).
- **Open questions for the user:**
  1. Boats only on release dawns (Claude, recommended: the reward of the release beat) or
     also on calm dawns at a slower rate?
  2. Once all five species live on the island, keep sending pairs of the rarest species
     (Claude, recommended: refounds a lineage a siege wiped out) or stop boats?
  3. Strict one bed each for the pair (Claude, recommended: "two beds, they stay" reads on
     sight) or keep LAW_life 7's slack of one?
  4. Herd growth after taming is cut: pairs per siege plus breeding may grow slower than the
     "exponential city" pre-pillar; a balance question, not tuned here.

## Forks closed in AFK mode (/design-idea + design-dialogue section 6)

Each: pick (Claude), one-line reason; then the steering moves played.
1. **What calls a boat:** a pier the player builds, plus a release dawn. Reason: rule 7 needs
   a built thing to gate a capability (species carry stat identity), and the release beat
   (user's action curve) gets a visible reward. Identity filter: a calm day is the build
   window, so the deadline (dusk) lands in it. Implication: no pier, no new species ever;
   the dawn line (PR 2) must name the pier.
2. **How often:** one boat per release dawn, whatever the pier count. Reason: one rhythm
   (the siege), never a second clock; more piers buying more boats would be a purchase.
3. **Who stays:** the pair, when the herd has a free bed for each, checked all day until
   dusk. Reason: reuses the bed vacancy contract and bed balloon, the player's one act is
   "build beds", and the do-nothing policy differs (boat leaves), so the choice is real.
   Duplication: the same balloon as a bedless friend, same meaning (a bed is lacking).
4. **What it costs:** the pier in wood; the stay costs two beds (space plus wood). No gems.
   Reason: rule 10 (roles from raising, not purchase) and the sacrifice pillar (beds occupy
   room).
5. **Pair vs single:** a pair of one species, all or none. Reason: rule 14, a lone visitor
   founds no lineage; a split pair would leave one stranded.
6. **How the tree picks species:** frontier stat need first, then any absent species, then
   the rarest. Reason: the arrival answers what the player is trying to open, so "why owls?"
   reads off the frontier; fallbacks keep it working before c1 lands.
7. **Visual:** boat as a hidden child of the pier, passengers are species mesh scenes, water
   one flat plane. Reason: no physics boat, no new spawner or creature state; legible.

tldr: build a pier on the shore; after each siege a boat brings a pair of a species the
frontier wants; two free beds by dusk and they join, else they sail off.

## References (rings 1 to 4)
- **Animal Crossing: New Horizons (ring 1, user).** A camper visits the campsite every few
  days (odds rise from 0 on days 1-2 to 20% from day 6); it moves in only if a housing plot
  is free. Works there: a visitor is a rare event and the plot is the player's prepared
  answer. Here: the bed is the plot; the release dawn replaces the odds.
- **Banished (ring 2, city builders).** A Town Hall must stand before nomads come; groups are
  10-30% of the town; they arrive with no shelter and bring disease risk. Works: a building
  opens the inflow and housing is the player's job. Here: the pier is the town hall; we drop
  the disease cost (tone) and group scaling (balance).
- **Dwarf Fortress (ring 2).** Migrant waves sized by created wealth; deaths scare migrants
  away. Works: growth rewards what you built. Here: rejected as hidden math (black-box
  pillar: the player cannot see the formula); a fixed pair reads on sight.
- **Frostpunk (ring 3, siege pressure).** Survivors come when you build a beacon and send
  scouts; refugees arrive after story beats. Works: arrivals are earned after a pressure
  peak. Here: supports tying boats to the release after a siege.
- **RimWorld (ring 3, from memory, unchecked):** wanderers join and refugee events, paced by
  the storyteller between raids. Same lesson: newcomers land in the calm after a raid.
- **Stardew Valley (ring 3, from memory):** no recruitment; Willy's boat to Ginger Island is
  repaired once. Rejected for the inflow; only the "boat at the dock" picture carries over.
- **Novelty (ring 4, assumed):** none of these tie the arrival's kind to what the player is
  trying to unlock; that link (the frontier picks the species) is the new part here.

Sources: [ACNH villagers, StrategyWiki](https://strategywiki.org/wiki/Animal_Crossing:_New_Horizons/Villagers),
[ACNH campsite, Nintendo Wire](https://nintendowire.com/guides/animal-crossing-new-horizons/campsite/),
[ACNH recruiting, How-To Geek](https://www.howtogeek.com/664191/how-to-recruit-new-villagers-in-animal-crossing-new-horizons/),
[Banished Nomad wiki](https://banished-wiki.com/wiki/Nomad),
[Banished Town Hall wiki](https://banished-wiki.com/wiki/Town_Hall),
[DF Migrant wiki](https://dwarffortresswiki.org/index.php/DF2014:Migrant),
[Frostpunk workers guide, Twinfinite](https://twinfinite.net/guides/frostpunk-workers-engineers-children-how-get/),
[Frostpunk, Wikipedia](https://en.wikipedia.org/wiki/Frostpunk).

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
