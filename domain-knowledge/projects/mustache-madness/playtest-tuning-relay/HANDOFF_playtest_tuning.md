# HANDOFF: playtest tuning (AFK relay, 2026-10-19)

## Status for the user's return
- **Economy decisions (user, 2026-10-24):** no deposits (pouch gems never reach the vault), vault
  growth cut, drink costs 2, honesty-box crop basket; see `docs/BRAINSTORM_economy_model.md`.
- **Economy super design done (AFK, 2026-10-22):** result and 7 questions in
  `docs/BRAINSTORM_economy_model.md` ("Super design result"). Recommended: the bank matches the
  player's throw 1:1, never picks a sign itself; cut vault growth. Nothing built.
- **Session handoff (2026-10-21, relay at ~96% of the session's usage):** 21 PRs merged this
  session (#349-#370 less #356, which landed as #357); main @ c516194a, tag 0.236.1, local main pulled.
  Running when cut: **R1** in mm-fixes2 (feat/furniture-shop, 1 commit, unpushed, behind
  main by 1: rebase first; then 34 own-room furniture, 18b price gate). **R2** in mm-fixes
  (feat/pickpocket, no commits yet; then 18d **teacher is a paid job** (user, 2026-10-21:
  "teachers should be paid, it is a job"; reverses #351's unpaid TEACH): its chalkboard takes
  station wages like any workplace, plus tuition from learners; then 18g bartender buys crops). Next
  session: resume both rounds (SendMessage the same agents, or new rounds from these
  branches), review + merge each PR on local CI (Actions still blocked by billing), then R6
  university, R6b haulers, R7 zones, R8 build, R5 physics, R4 perf (alone on the CPU).
  Normal idle config (power-off after 1 h) put back at this point (afk SKILL step 11).
- **Decided (user, 2026-10-21): "caring more should grow a way bigger herd; bunkhouses should
  grow less."** A balance task, so not for an AFK relay (user rule): do it in a session with
  the user. Was (PR 41, measured): once land binds, housing density beats care. With
  medic beds equal, neglect in 9-bed bunkhouses holds 43.8 herd-days vs care's 26.8 (1-bed
  rooms fill the 60x60 m land at ~30 beds); care's clear win is survival (statue fell 1 of 12
  vs 5 of 12). The room-mood drag (#363) hurts mood, not numbers. Options: (a) crowding costs
  births or health, not only mood; (b) more land or stacked rooms so care is not land-capped;
  (c) accept: density is a valid strategy, care buys safety.
  Sharper after #368 (bots now get free medic beds), 18 seeds: herd_days care 26.3 (sd 3.1)
  vs neglect 55.9 (sd 5.4); herd at 900 s 55.8 vs 177.1; neither statue fell. Neglect's
  bunkhouses leave land for ~17 medic beds vs care's ~5.
- Relay started 2026-10-19 from the user's playtest of main @ #337 (0.228.1).
- Picks (user, AskUserQuestion): merge after a cold review + green CI; probe first, then fixes
  ranked by what it measures; bar becomes a job; library goes through /design.
- Final report: written by the relay at the end, one page with every measured number.

## Designs for review (2026-10-21, design only, user reviews each before any build)
docs/BRAINSTORM_design_r1_shops.md, _r2_flow.md, _r3_meals_mood_couples.md,
_r6_university_haulers.md, _r7_r8_build_r5_needs.md. Built branches 18f (mm-fixes2) and 18c
(mm-fixes) are reviewed there, not merged.

### Design picks (user, 2026-10-21, AskUserQuestion)
- 18f: a clerk job takes the shop's gems (not the player). 34: lift split by beds (pick C).
- 18b: broke sits at the bar, no drink; a paying round mate may stand it one. 18c: loot to police, merge as built.
- 18d: the chalkboard becomes a workplace (Station); chairs facing it become desks; one chalkboard
  per room; no chair limit beyond room size. Bartender is a paid job (station wages).
- 18g generalized (user asked "restaurants too? any job that requires another job?"): one rule,
  a worker who uses up stock another worker made tips the maker 1 gem per unit, on top of the
  maker's wage; a hauler earns its own wage, the tip still goes to the maker.
- 19: good mood up to 1.5x, floor 1.0 (no drag below).
- R6: VIT-top goes builder (body stats STR/DEX/VIT -> builder, INT -> architect); own university
  room; no head sign for trades (cut).
- Round 2 cross-check picks (user): every paid place (shop, chalkboard, bar, R7 crate) is a full
  Station, built once by R2; maker record = [maker, count] runs oldest first, owned by R2 and
  reused by R6b/R7; the 18f clerk makes a lamp from 3 woodpile logs. Tip delivery (user): "both
  creatures should meet and one should drop the gem payment and the other should receive"
  (an on-screen hand-over, not a remote jump); R2 designs the meeting.
- Round 2 Q&A (user): a broke payer OWES the tip and pays at the next meeting once it has gems;
  sowing another farmer's crop owes no tip; a second chalkboard in a room stays grey (warn ghost).
- **Reframe (user, 2026-10-21), round 3 paused for it:** (1) "the player already pays them; we
  have to design how to manage things that other creatures pay instead of the player having to
  pay them; super design this" (who funds a workplace's hours once creatures pay each other);
  (2) "if creatures can buy stuff, they can place furniture in their house, wear it or use it,
  and we see them using it" (owned goods are visible and used). Team-mode design:
  docs/BRAINSTORM_design_economy_frame.md.
- Parked economy questions (user, 2026-10-22, "answer later"): how much a unit should cost
  relative to time for a healthy economy; or should every price follow supply vs demand; should
  a wage follow seniority + supply/demand.
- **Payment model picks (user, 2026-10-22; docs/BRAINSTORM_design_payment_model.md):** creature
  gems keep jobs open (spare pouch gems go to the vault, the bank payer tops up due signs);
  a creature's gem buys its own serving ("shop"): it lands on the seller's sign while the sign
  is due, else in the worker's pouch. Measured (care seed 1, 900 s, n=1): wages 20, bought 18,
  40 drinks poured of which ~22 free; the herd's wages pool in the bartender.
- Payment Q&A (user, 2026-10-22): a maker is paid sign to sign (the using workplace's sign pays
  the supplier's sign 1 gem per unit; the maker earns it as wage), replacing tip-on-meeting and
  per-unit maker records; broke creatures still drink and eat free; "pay wave jobs more" means
  more hours paid ahead; bought goods: home goods first (carried home, set by its own bed, used).
- Creature businesses (user, 2026-10-22): stage 2, but shape the payment model now: the funder
  slot of a sign is "the player or a creature (owner)"; sales beyond the sign's needs go to the
  owner (none for a player-funded sign: the serving worker keeps them, as before). Founder,
  hiring and bankruptcy come with stage 2 (docs/BRAINSTORM_game_stages.md market arc, Q9).
- Round 3 Q&A (user, 2026-10-22): pay or wait (a workplace takes only stock its sign can pay
  the supplier for); the maker is paid at take or delivery. Savings are protected (user:
  "savers makes sense"); open: is a saver "not broke" and so pays for servings? New idea (user):
  "what they buy depends on their status".
- **Unit-clean model (user, 2026-10-22), supersedes "sign pays sign" and "customer gem to the
  sign while due":** a sign holds TIME only (funders: player, later a creature owner; out:
  salary per shift). Per-unit payments go pouch to pouch: customer -> serving worker; worker ->
  maker per unit of stock (pay or wait: takes only what its pouch can pay for). Spare pouch gems
  go to the vault; the bank payer carries them to due signs (the one visible unit->time step).
- Still open: R7 timer start, crate filler; R8 scaffold, lure, builders per site; R5 off-rim; NF red balloons.

## Game frame (user, 2026-10-20)
"Productivity is the number one priority to survive each wave." Economy, consumption, mood,
studies and stages all serve the herd's productivity; a wave tests it.

## Purpose
Every built feature shows up in a normal run at a rate that makes sense (snaps, thefts,
births, research pace), with no lag spike, and each claim in the final report is measured.

## Where to work
Never in the main checkout (`/home/akiraki/Playground/mustache-madness`): it holds the
user's uncommitted edit (ENEMY_POWER_MULT 0.85) and a running game. Run no git command
there. Use the worktree `/home/akiraki/Playground/mm-fixes`: `git fetch`, `git checkout -B
<branch> origin/main`, then a `--import` boot before tests. This handoff lives at the main
checkout path; edit it there. Screen may be locked: headless runs only.

## Speed rules (user, 2026-10-20: "be faster; why 1 h; avoid losing time on non-productive stuff")
- Two rounds may run at once, each in its own worktree (`mm-fixes`, `mm-fixes2`); a PR whose
  done line is a timing number runs alone.
- Tests: only the files that cover the change, one boot. A sim batch only when the done
  line needs a number: one before, one after. No exploratory batches.
- One /prune + /rate pass, not a loop; fix only what it finds severe.
- Push as soon as the done line holds; the relay reviews while CI runs.

## User's playtest report (2026-10-19, verbatim gist)
"I see no snap." "Population maintains 2.1 even though I'm providing better conditions."
"Lag spikes." "Bar should be a job." "Why is library a job?" "Lab is very easy and cheap;
it should take more time after each unlock." "I don't see creatures stealing gems or having
status." "etc.: evaluate until all makes sense 10/10."

## Rounds from 2026-10-21 (user: "forget balancing for AFK; feature-based and fast; 3 related
PRs per agent"; "never afk relay balancing tasks")
Dropped from the relay as balancing: 10 (final evaluation), 35 (room-term probe key), 39's
couples tuning, 18i's rich-vs-broke batch, the done lines that name a sim median. Balance
questions stay listed under "Status" for the user. Each round below builds its PRs as
features: tests green, a cheat key for a playtestable one.
- **R1 economy shops:** 18f furniture shop (own-room items), 34 own-room furniture lifts the
  room term, 18b price gate (a creature buys only what its pouch covers).
- **R2 economy flow:** 18c pickpocket, 18d teacher tuition (learner pays the teacher),
  18g bartender buys its crops (its gems pile up today).
- **R3 economy + mood:** 18e paid meals + a herd gem readout on the HUD, 19 good mood raises
  the breed roll (curve unit-tested, no sim done line).
- **R4 perf, alone on the CPU:** 36 Housing.reassign cost, 43 frame time at ~180 creatures,
  16 autosave < 50 ms.
- Running at the switch: 18i (aspire lever, told to ship as a feature with no batch), 39
  (narrowed to the body wedged in a floor slab).
- **R3b couples (user, 2026-10-21: "couples should try to sleep at the same time if possible"):**
  a bonded couple goes to bed together: when one heads to sleep, its partner (if awake, free,
  and tired enough or close to its own bedtime) follows; they sleep in the same room or a
  shared bed where one exists. Feature: tests + a cheat that sets up a tired couple.
- **Needs fade (user, 2026-10-21: "needs in white should only be visible when player is close"):**
  the white need labels over creatures show only near the camera/player. Small feature PR.
- **R5 physics bugs:** knocked bodies fall through the terrain ("fell" alerts at y -1 to -2,
  PR 32's seed-2 logs); a QA "embedded" defect kind (a body's centre inside a non-bed
  STRUCTURE piece, sampled once a second; not in the code yet: #370 only pushes bodies out of a placed piece).
- Merged at the switch: #369 aspire (0.236.0), #370 slab push-out (0.236.1).
- **Stage 2 (user picked Shape 1, docs/BRAINSTORM_game_stages.md "Decisions"), 3 rounds:**
  - **R6 university:** a university room type (lectern anchor); drafting table teaches the
    architect track (INT), workbench the builder track (STR or DEX), each student takes the
    track its own top stat fits; tuition paid from its pouch (user); architect and builder
    hats and jobs; cheat `/university`.
  - **R7 zones:** the player drags a zone and places one anchor; the architect walks it and
    draws a blue ghost (skill sets how tight, no style); building starts 15 s after the zone
    (user); a builder job fills a site stockpile, like the kitchen's (user); cheat `/architect`.
  - **R6b haulers (user: "more logistics jobs to carry resources from x to y"):** a hauler job
    that carries stock from a station that has it to one that wants it (woodpile -> site
    stockpile, basket -> kitchen or bar), one general carry route the later train loaders
    reuse; runs before R7 so the stockpile is filled by haulers.
  - **R8 build:** builders carry from the stockpile and hammer ghost pieces in; wilds punch
    scaffolds, a half-built site stays half built at dawn; the walking skeleton end to end
    (one bed zone -> one hut).
- Needs a design session with the user (not a relay round): stage 3 (specialist cities by
  rail, picked; city tags/status with their own mood or effects, user seed); Q9 backing a
  startup.

## PR list (history; items above supersede its order)
1. **Feature probe (walking skeleton).** One headless command (extend `run_sims.sh` /
   SIM_RESULT) that prints, per seed, for a neglect policy and a care policy (good food,
   beds, leisure): snaps, puff spells, bored share, thefts, arrests, births, deaths,
   population over time, research unlock times, egg lays/hatches, frame time p50/p99/max
   and count of frames > 50 ms. Find what "population 2.1" means in the HUD and probe it.
   Done: the table for 3 seeds x 900 s is pasted into "Measured baseline" below; each
   feature the user said they never see is marked seen / unseen with its gating cause.
2. **Snap reachable.** From PR 1's cause. Done: neglect policy >= 1 snap per seed in 900 s
   after >= 60 s of puffs; care policy 0 snaps; unit test on the fixed gate.
3. **Population responds to care.** Done: care policy's population at 900 s beats neglect's
   by a margin the PR names; the HUD number the user read is explained.
4. **Thefts and the creature status visible.** No cheat: a puffing creature steals at a
   rate the PR names; 💰 and the status line show on it. Done: probe counts thefts > 0 per
   seed under neglect; test for the visible status.
5. **Lag spikes.** Bench state matches a playtest (herd size, objects, session age). Done:
   frames > 50 ms counted before and after; the top offender fixed with its measured gain.
   Also (user, 2026-10-19: "30 min in 5 minutes"): one 1800 s care sim finishes in <= 300 s
   wall at full play precision (60 steps/s). Measure a lone run first, then cut per-frame
   cost; if still over, add a coarser-step "long run" mode validated against a 60 steps/s
   run on snaps, herd and thefts.
6. **Lab pacing.** Each unlock costs more time and/or gems than the last. Done: a test pins
   the growing cost; probe shows unlock times spread over the run, not front-loaded.
7. **Bar is a job (user).** /design: a creature staffs the bar, drinks are served by it.
   Done: a worker staffs the bar in a sim; tests; cheat key if needed.
8. **Library: job or leisure.** /design against "Natural on sight"; build the pick. Done:
   the pick and its reason in the PR body; tests.
9. **Client job panel mood line** reads server-only `mood.value` on a client; replicate or
   hide. Done: two-peer test.
10. **Final evaluation.** Rerun PR 1's probe, a cold review of every feature vs its design,
    /rate to 10; fix rounds until nothing severe. Done: the before/after table.
11. **Load a save in the game and in the sim (user, 2026-10-20).** `docs/TODO_save_load.md`
    "Load in the game": a start-menu load button + a cheat key that loads the newest
    autosave; SIM_LOAD keeps running for SIM_SECONDS instead of ending at the saved wave's
    dawn, so the probe can start from the user's playtest
    (`saves/2026-10-19T21-02-25/wave_46.save`); sims write autosaves to their own folder,
    not the player's (435 sim sessions bury the real ones). Note what the save still drops
    (eggs, inventory, jail machines, light wilds). Done: the user's wave_46 loads in both;
    a probe run from it prints the feature table; tests.
12. **A balloon only when the fix is missing (user, 2026-10-20: "dialog should only appear if
    the need is not met; if they want campfire and they can go, no dialog").** Applies to
    every balloon, the red mood one too (user, AskUserQuestion: puffs stay the snap warning).
    Today `OfferPlace.wish_glyph` (offer_place.gd:97) shows a place's balloon whenever its
    `pull_for` is 0 though the place exists, and `Red.MOOD` shows the seat for the whole brew.
    Rule: a balloon shows only when no place of that kind is free and reachable for it. Update
    LAW_creature_state.md row "Need" and LAW_beds.md Signs to match. Done: tests for "free
    reachable campfire: no balloon", "none / all full: balloon", brewing with a free seat: no
    red; CI green.
    Also (user, 2026-10-20: "why in chair they have the fork and plate emoji?"): the chair's
    glyph is 🍽 (chair.tscn:13, from the restaurant #269, when a chair was only for meals);
    it is now the COMFORT seat too, so a creature resting in it reads as eating. Show 🪑 for
    a comfort sit (and in the comfort wish, WISH_GLYPHS) and keep 🍽 only for a seated meal;
    check Noto Color Emoji draws 🪑. Test: a comfort sit shows 🪑, a meal shows 🍽.
13. **Farm sows only a ring, not the whole circle (user, 2026-10-20).** Code: `Basket._offsets`
    (basket.gd:137) takes cells 3..6 m out (CLEAR 2 keeps a 5x5 hole so its stacks stay in
    reach), nearest first, and sows only SOW_SHARE 0.65 of each crop that comes in. Suspects
    (unconfirmed): the hole, too few seeds to reach the outer band, cells blocked by
    decoration/blocks. Measure on the user's farm in `saves/2026-10-19T21-02-25/wave_46.save`
    (after PR 11, or read the save's crop cells) before choosing a fix; the user's picture is
    "use the whole circle". Done: the cause measured; a test that a basket with enough seeds
    fills every free cell of its circle; the circle the player sees matches the sown area.
14. **A non-square room got refused (user, 2026-10-20: "rooms can have multiple shapes, not
    just square; as long as the air doesn't escape too much it's ok").** LAW_rooms rule 3
    already says any shape; only an L is tested (test_rooms.gd:72). Shape unknown: build a
    table of shapes (round/octagon, stepped diagonal wall, T, U, plus-sign, courtyard ring,
    two storeys by a stairwell, walls of mixed heights) and find which `Rooms._solve` refuses
    and why (`why_not` caption). Check the user's save for rooms that read as no room. Fix
    each wrong refusal; keep the leak rule (openings up to 4 m, 1 per 8 m²). Done: a test per
    shape; any caption the fix changes is listed.
15. **Wilds never seen targeting eggs (user, 2026-10-20).** #328 gave wilds an EGG rule
    (creature_metadata.gd:158: radius 20 m, `needs_sight`, rank 5 = ALLY_PRIORITY_RANK; base
    rank 0, food 1). Suspects (unconfirmed): the rank loses to the base/allies every time;
    `Egg.seen_from` (egg.gd:92) blocked by the nest's room or the egg's own mesh; eggs out of
    the 20 m radius of where wilds walk. Add a probe count (wild picks of an egg target, egg
    hits, eggs broken) and measure on the user's save and a neglect run first. The design
    intent (#328): eggs are a real loss the player guards by moving them somewhere safe; an
    egg in the open and in sight should draw wilds. Done: the cause measured; open eggs in
    sight get targeted in a sim (count > 0); eggs out of sight stay safe; tests.
    Also: test_egg `test_hatches_at_dawn_after_surviving_a_night` failed once on CI (#341
    run 1, passed on rerun): likely flaky since #340 spread hatches across frames; fix it.
16. **Autosave under 50 ms + a 30-min sim in 5 min (split from PR 5).** PR 5 measured: user's
    wave 46 autosave 105 ms (grid 53, creatures 34, store 16); a lone 1800 s care sim 574 s
    wall. Cache each block's save record at placement (blocks never change after; extend
    LAW_save), store_var on a worker thread (deep copies first: PR 5 review); then cut
    per-frame cost ~2x or add a coarse-step long-run mode validated against 60 steps/s on
    snaps, herd and thefts. Done: wave 46 autosave < 50 ms; one 1800 s care sim <= 300 s wall.
17. **Roommates feed mood (user, 2026-10-20: "how many beds inside a room should matter in
    mood"; picked beds per room over floor per bed, AskUserQuestion).** A lasting centre term
    from how many beds share the room its own bed stands in: alone best, 2 fine, a Bunkhouse
    (3+) drags (LAW_room_types split). LAW_beds rule 1 ("no need feeds mood") holds: it is a
    place, not a need; say so in the law. /design picks: the values per count and their size
    against the other centre parts (bored -4; the doc's open fork "place lift size"), no bed =
    0 or a drag, the inspector card, and how it meets the open fork "alone in its own Bedroom
    as the cure". Picks in the PR body and the design doc. Done: tests per bed count; a care
    sim with 9-bed bunkhouses vs 1-bed rooms shows the centre gap; the card shows; CI green.
18. **Creature economy (user, 2026-10-20: "create economy system to make creatures consumist
    and be willing to work more if economy is well").** User picks (AskUserQuestion): the gem
    pouch PRE-PILLAR in MEMORY.md is CONFIRMED (user): promote it to a pillar in this PR. A
    creature spends its own gems on bar drinks + meals (paid to the worker who serves, so gems
    circulate), its own room upgrades (ties to PR 17 roommates), treats and toys at a stall,
    "and moreeee" (user: more sinks welcome). Shops the user picked (2026-10-20): mustache
    barber, furniture store (own-room items), gift shop (bond jump), arcade (loud: neighbours
    sleep worse), hot-tub spa (drains strain), lottery booth, pawn shop (sell found items).
    Not picked: snack cart. Wages (wage.gd, a station's thrown gems) land in
    the worker's pouch. "Work more when the economy is well": a work drive that rises with
    what it can buy and has bought, never a role bought (pillar "Roles emerge from raising"
    holds: gems change how much it works, not at what). Run /design first (BRAINSTORM doc:
    sinks list, prices, what "economy is well" reads, how the player sees it, theft and police
    hooks from #331), then build the walking skeleton: wage -> pouch -> one buy (a bar drink)
    -> work drive. Later slices as follow-up PRs the relay adds. Done: a sim shows gems
    circulating (earned, spent, earned again) and more work hours in a rich herd than a broke
    one; tests; CI green.
19. **Good mood raises fertility (user, 2026-10-20: "fertility rate should increase if there
    is prosperity, I mean good mood").** This reverses the earlier user call "love, not mood,
    drives births" (creature_config.gd:76; LAW_life.md rule 5): the newer word wins; update
    both. Scale the couple's breed roll (social_formulas.gd:140) by both parents' mood, on
    top of love; /design the curve (neutral 1.0, good mood up, bad mood down or floor) and
    its size against BREED_LOVELESS/LOVED. Note: "lifetime eggs ~2.1 to ~2.8 per creature in
    play" in that comment may be the "2.1" the user read (PR 3). Done: test on the curve; a
    care sim (good mood) births more than neglect at 900 s by a named margin; CI green.
20. **Stages 2 and 3 grow, not repeat (user, 2026-10-20: "game right now is good at the early
    game; it shouldn't last like that for the second and third stage; it has to grow
    exponential").** /design first, in a clean subagent: what marks each stage (herd size,
    waves, unlocks), what changes at each (new threats, new verbs, bigger stakes, scale), and
    what "exponential" means for the player (herd, economy PR 18, enemies, base). Read
    playtest 2: herd stalled 55-60 w23-35 then 56 -> 147 in 5 waves; lab stalled 10 waves;
    fps fell to 24. User seed (2026-10-20): "second stage, creatures should learn to build"
    (a build verb that moves from the player to the herd, learned through raising, fits
    "Roles emerge from raising"); "third stage: interconnected cities with logistics,
    trains and traffic" (user); "for creatures to build they need studies and a university and
    more jobs"; "we need architect and builders"; decided (user): "the player chooses where it
    can build, the architect designs how, and the builders build"; the market evolves (user):
    exchange -> creature-founded businesses -> stock market and startups with own buildings
    and jobs, to grow consumption. A design agent is writing docs/BRAINSTORM_game_stages.md.
    Output a BRAINSTORM doc with 3+ stage shapes ranked for the user's pick;
    build nothing until the user picks.
21. **Why no snap in real play (from playtest 2).** 14 creatures sampled mood <= -4 (min -5)
    and snaps stayed 0 (logs/playtest_2026_10_20.log; saves 2026-10-20T00-18-32). Load the
    user's waves (SIM_LOAD runs one wave each) and log, per low-mood creature, which brewing
    or snap gate fails (history vs WARN_LINE, slow_centre, tired, asleep, jailed, REST_SEC,
    brew_sec reset). Fix the gate that is wrong for play; keep "rare and earned" and care = 0.
    Done: the failing gate named with counts; a test on it; a snap reached on the user's save.
22. **Nav region race in the game + honest farm alerts (from PR 13).** Godot 4.7 NavRegion3D
    drops a mesh change that arrives while its async build runs (PR 13 found it in a test).
    Check after a level load and after a save load whether the terrain navmesh stays stale
    until the next rebake; fix if so. qa_watch: skip ring sites closed by the one-farmer rule
    or off shift, so FARM waiting counts only real stalls. basket.tres card says "sows half";
    the share is 65%. From #344 review: test_nav_obstacle_carve turns async off on the region
    only; also call map_set_use_async_iterations(map, false) as production does
    (procedural_terrain.gd:209-210); check no nav region has scale != 1 (carve radius unscaled).
    Done: a test or headless check on the race; alert counts on wave_40.
23. **Eggs too harsh since #347 (measured by PR 3).** EGG_PRIORITY_RANK -1 dropped care's
    900 s herd from ~55-66 to 1-19 (11-22 eggs broken per run); care's statue fell 1 of 3.
    Goal: an egg left in the open and in sight is a real risk, an egg the player guarded
    (nest in a room, moved away) is safe, and care's herd comes back near its pre-#347 level.
    /design the lever (detection radius, max attackers, egg HP, eggs in a nest/room never
    picked, only a wild already near) and measure "turtle care" 3 x 900 s before/after, same
    seeds, with egg_picks/eggs_broken. Done: care herd median >= 40 at 900 s, eggs broken
    > 0 under neglect, the guarded-egg test still green.
24. **Care herd collapsed on main (PR 7 round, 2026-10-20).** `turtle care`/care 3 x 900 s on
    main @ b0fe3ef3 (after #349: only foxes and hedgehogs hunt eggs) gave care herd 5-13,
    egg_picks 89-134, eggs broken 11-13: PR 23's done line (care median >= 40) still fails,
    and the bar (PR 7) never gets an INT 8 bartender in so small a herd. Measure first which
    loss dominates (eggs broken, deaths by cause, births) against PR 1's baseline (55-66);
    then fix the top cause. Done: care median herd >= 40 at 900 s, 3 seeds; neglect still
    breaks eggs > 0; tests.
25. **Sealed-room check, follow-ups from #350's re-review.** (a) an empty path mid-bake seals
    every room and evicts sleepers until the next nav change: judge only on a settled nav
    version or ignore empty paths while a bake is pending; (b) check_walk runs every piece in
    one frame under 2 ms (FrameBudget.claim_uncut): cap checks per frame or fix the claim;
    (c) a build spree re-walks every room piece per placement: measure; (d) README lab line:
    "the last takes about 20 minutes". Done: a test that a mid-bake empty path seals nothing;
    build-spree cost measured; CI shards green.
26. **Bar stays open through its bartender's trip (from #352).** The bar closes 10 s after its
    last labor tick, so drinkers get up while the bartender restocks or takes a break. Natural
    on sight: a bar with stock keeps its drinkers seated while its bartender is on a short
    errand. /design the rule (open while the bartender holds the BARTEND job, or a longer
    grace). Done: a test that a restock trip keeps drinkers seated; a closed bar still seats
    no one; CI shards green. Also from #352's re-review: a full bar + a bag no station takes
    locks the bartender holding it (spill at the bar, test the no-acceptor case); supplier()
    picks the nearest basket by straight line, no path check (skip unreachable); the cached
    basket still runs Station.stacks() per tick and takes() load()s per tick (cache).
27. **Chair errors on load (from #353's round).** Every wave_40 load prints 16 SCRIPT ERRORs
    "Chair._table get_nodes_in_group on null" (chair.gd:48), on main too. Done: a load test
    with a chair prints no error; cause named in the PR.
28. **#353 leftovers (re-review).** (a) test_nav_region_sync's "race dropped" test waits 2
    frames and never checks the big build is still in flight: assert in-flight at the set or
    drop the claim (CI flake risk); (b) client job panel reads feel_wire default [0,...] as
    "grumpy" before any feel arrives or after a creature leaves FRIENDLY: show no band then;
    (c) qa_watch `held` counts time, not stall: ARREST/TREAT long chases/carries false-flag,
    and re-seats re-arm without bound; (d) PR text of #353's timing table overclaims at n=2
    (nothing to edit after merge; note only). Done: tests for (a)-(c); CI shards green.
    Proposal from the round (built in round 2): reset feel_wire on the server when a creature leaves
    FRIENDLY, so a client never shows a stale feel when it turns FRIENDLY again.
29. **A mixed bag delivers to the wrong station (from #356).** `_deliver_carry` picks its
    station by carry_path (the bag's first kind) and adds every kind to it, so a mixed bag can
    put logs in a basket. Done: a test that each kind lands at a station that takes it.
    Also: README's PR 26 line is tagged #356, merged as #357; test_social_bar's basket-fetch
    test fails when test_block_nav runs first in one boot (a nav map left behind makes
    reachable() false): free the map in block_nav's after_each or make the bar test own it.
30. **test_save_game order leak (from #358).** "a crop keeps its growth" fails when
    test_woodpile, test_basket, test_payer and test_tree_chop run before it in one boot; it
    passes alone and in the unit shard. Done: the leak's cause named and fixed; the five files
    pass in one boot.
31. **Every headless sim aborts at quit (from #359).** Exit code 134, "double free or
    corruption" at quit, on main too. Done: the freed-twice object named; a sim exits 0.
32. **Nested couples still fail (from #360).** Per care run 2-3 couples sit a whole night without
    reaching their nest, 3-4 are cancelled by hits, 1-2 lose a partner. Check nest
    reachability and the spot check first; fallback lever: a smaller EGG_DETECTION_RADIUS
    (eggs never hunted: care median 48). Tried and dropped in #360: a hit not cancelling a
    couple heading to its nest. Done: breed_faded halves vs #360 on seeds 1-3 (SIM_WALL=0);
    care median >= 40 on seeds 1-6.
33. **17b: roommates vs snaps (from #363).** The bunkhouse drag plus boredom can now cross the
    -4.25 brew start in a 4+ bed room, and no bed = -1. Done: neglect and care snap counts
    before/after #363, 3 seeds each (SIM_WALL=0); care stays at 0 snaps or the PR names why.
34. **17c: own-room furniture lifts the room term** (the open "alone in its own Bedroom as the
    cure" fork; ties to PR 18's furniture store). Done: a 1-bed room with a table/lamp shows a
    bigger lift; tests.
35. **17d: BalanceProbe live key for the mean room term.** Done: the key shows in a capture.
36. **Housing.reassign costs 16-19 ms and runs ~every second (from #363).** On wave_46 (herd
    ~180, 39 beds) it ran in 148 of 180 s, 2.3 s total; most is assign and close_map, and
    bed_for marks Housing dirty on every bedless call. Profile, dirty only on a real change,
    spread or cut the cost. Done: wave_46 reassign ms and runs per minute before/after; no
    frame over 16 ms from it.
37. **Neglect snaps 0 again (from PR 33).** 6 of 6 neglect runs on main @ 144368ee snap 0
    (PR 2's done line: neglect >= 1 snap in most runs); likely PR 3's population brake drops
    the turtle herd by night 8-11 before mood falls. Also log each snap with the snapper's
    centre parts (room, bored, health, belonging) so "earned" can be checked, and set the
    care sim's default room size so care means full care after #363. Done: neglect snaps in
    >= 2 of 3 seeds (SIM_WALL=0); care 0; per-snap log line in SIM_RESULT.
38. **Splash hits allies (from #364).** DamageService.splash_neighbors hurts the herd's own
    creatures (deaths_by friendly_* rows). /design whether splash spares allies (tone: goofy
    slapstick may want it). Done: the pick with a test; friendly_* deaths before/after.
39. **Late-night couples and a body stuck in a slab (from #364).** Night-1 couples pair late
    and far apart (pairing distance or time gate); one body wedged inside a floor slab on
    seed 450 (physics penetration). Done: each cause logged with counts, a fix and a test.
40. **Economy follow-ups (from #365; done lines in docs/BRAINSTORM_creature_economy.md):** 18b
    price gate, 18c pickpocket, 18d teacher tuition, 18e paid meals + a herd readout, 18f one
    shop (furniture first; ties to 34), 18g bartender buys its crops (its gems pile up today).
    18h done in #365 round 2: the taste lever was cut (no effect: open jobs cap work, not
    stretch length). New 18i (the user's "work more"): more of the herd holds a job; a
    creature that has bought leans to the library to clear INT job gates, plus a care variant
    with more paid stations. Done: hatted creature-seconds rich > broke by >= 20% (3 seeds).
41. **Care herd limit, measured honestly (from #364).** Fades halved (12 seeds 92 -> 32) but the
    care herd median did not move (seeds 1-6: 35.5 vs main 40; 12 seeds 36.5 vs 39); one seed
    swings 15-20 between small code changes, so n=6 cannot see a 5-creature effect. First
    pick a herd metric that resolves 5 (more seeds, or herd-days instead of the 900 s count),
    then find what caps the care herd now (beds, land 60x60, joins, deaths). Done: the metric's
    seed-to-seed spread stated; the top cap named with counts.
42. **Sim medic beds + herd-days metric (from PR 41).** The bots' medic buy never fires (a
    medic bed needs a 104-plank hut, the bot fells one tree a dawn), so 2 starter medic beds
    cap recruits (full 57% of the time, 30-80 bodies loose at dawn 17). Both bots place free
    medic beds while loose bodies outnumber free spots; add herd_days (mean herd over dawns)
    to SIM_RESULT and sim_report; herd PRs judge on it at >= 18 seeds (SD 3.2 care, 5.5
    neglect). Done: beds_bought > 0 in both bots; herd_days printed; 18-seed table.
43. **Frame time at ~180 creatures (from #368).** Neglect's frame p95 is 16.7 ms at about 180
    creatures (care 10.6). Bench on the neglect 900 s state (SIM_WALL=1, alone on the CPU);
    name the top cost. Done: p95 before/after with the top offender cut, or named with its ms.
Order of 2-8 and 11-43 may change by PR 1's numbers (relay's call).

## Playtest 2 (2026-10-20 00:18-01:18, waves 1-40, main @ 6edfe296: snap fix, no lag fix)
User verdict (2026-10-20): "it was fun"; the main idea is good, fresh and original; the early
game is good; the rest is tuning. The second and third stage must not play like the early
game: the game has to grow exponentially (PR 20).
Read from logs/godot.log by an agent; line numbers are that log's (it is overwritten by the
next game run: copy it to logs/playtest_2026_10_20.log before any rendered run).
- Snaps 0, though 14 creatures sampled mood <= -4 (min -5): check the gate on this save (PR 2
  follow-up, before PR 4).
- Thefts 5 (first w31), cop_arrests 0; 6 `[ALERT] waiting ... job=ARREST open=false` (PR 4).
- Eggs: lays 274, hatches 273; no egg hit in BALANCE_HITS; egg.gd logs nothing (PR 15).
- Herd at dawn: w20 47, w30 69, w35 56, w40 147 (56 -> 147 in 5 waves); entr 2.0-2.27 (PR 3).
- Lag: median fps w20 58, w30 42, w40 24; node count 2.2k -> 38.5k; autosave w40 201 ms;
  worst spikes right after an autosave; 160 of 215 spikes > 100 ms untagged (PR 16).
- Lab: 7 discoveries w19-27, none for 10 waves, 11 `Stuck RESEARCH WORK` at one goal (PR 6).
- Bar placed (w28), bar_visits 0 (PR 7). Fire visits 1442 vs seat visits 19.
- Rooms refused: "4 openings, a room this size allows 2", "open to the south/north", "no
  roof" (PR 14). FARM waiting open=false 632 alerts (PR 13). 24 `material is null` errors,
  each after a nav rebake.

## Measured baseline
PR 1 (#338), `util/scripts/run_sims.sh "turtle care" 3 900` on origin/main @ 69fceaef (ENEMY_POWER_MULT
0.7, not the user's 0.85). Neglect = `turtle` (carries the downed, nothing else); care = `active`
plus a free restaurant, bar + games table, campfire and lab, restocked and paid each dawn, and
free 9-bed bunkhouses while anyone is unhoused (every care dawn housed all). SIM_WALL=1, 6 sims
in parallel on 12 cores; no Godot game was running at 22:54 (pgrep), load avg 2-5. Runs do not
replay under SIM_WALL=1: herd at 900 s moved by up to 40 between batches of the same seed.

| policy | seed | snaps | spells | puff_s | strain | brew_s | bored | thefts | arrests | banks | lays | hatch | deaths | herd | p50 | p99 | max | >50ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| care | 244 | 0 | 0 | 0 | 0.0 | 0.0 | 0.05 | 0 | 0 | 0 | 61 | 59 | 39 | 55 | 3.00 | 13.72 | 318 | 35 |
| care | 497 | 0 | 0 | 0 | 0.0 | 0.0 | 0.03 | 0 | 0 | 0 | 70 | 70 | 39 | 66 | 3.03 | 13.13 | 351 | 35 |
| care | 450 | 0 | 0 | 0 | 0.0 | 0.0 | 0.11 | 0 | 0 | 0 | 57 | 57 | 30 | 64 | 3.02 | 12.30 | 333 | 35 |
| neglect | 244 | 0 | 1 | 9 | 0.72 | 0.0 | 0.39 | 0 | 0 | 0 | 22 | 22 | 21 | 24 | 1.83 | 14.41 | 58 | 1 |
| neglect | 497 | 0 | 0 | 0 | 0.0 | 0.0 | 0.38 | 0 | 0 | 0 | 47 | 47 | 33 | 50 | 2.40 | 12.40 | 56 | 4 |
| neglect | 450 | 0 | 0 | 0 | 0.0 | 0.0 | 0.38 | 0 | 0 | 0 | 64 | 64 | 34 | 65 | 2.72 | 12.57 | 64 | 7 |

Columns: spells = puff spells; puff_s = friend-seconds puffing; strain = peak (1 = history at
SNAP_LINE); brew_s = longest spell count (a snap needs 60); bored = share of adult-friend time
with fun under BORED_LINE; deaths = herd members gone for good, counted once; frame ms past the
setup frame.
- Herd/entropy by dawn, care 450: 3/0.00 ... 19/1.89 23/2.14 26/2.18 26/2.12 34/2.13 38/1.91
  45/2.01 48/1.97 57/1.94. Late-run entropy: care 1.65-2.18, neglect 1.4-2.1.
- Research (care only; neglect has no lab): unlocks at s 536 717 836 / none / 420 494 599 716
  864. An earlier batch: 4-6 unlocks, the first at 230-370 s. Gaps 75-190 s.
- Care's places work: cooked 85-99, dined 10-36, poured 0-44.
- Hitches (game s:ms): frames over 50 ms land at the same game s on every seed, two per day
  cycle (dawn and dusk likely), e.g. care 497: 3:178 18:72 25:128 56:101 90:210 ... 645:234
  712:224 856:351. In care they grow with the run (about 130 ms at 100 s, 220-350 ms by 850 s).
  In neglect they are 50-64 ms and start after 445-503 s. The 3 s one comes after care's setup
  frame, which is no longer sampled, so the max is not the load frame.

Seen / unseen (the user's complaints):
- **Snap: unseen** (0 snaps in 18 runs, 3 batches). Gate: mood history almost never reaches
  WARN_LINE (-3), so puffs almost never start (1 neglect run of 3 per batch: 1-2 spells, strain
  0.57-1.0, longest count 6-16.5 s of the 60 s HOLD_SEC). Neglect is bored 38-39% of the time,
  but BORED_MOOD 2.0 alone rests a creature at -0.75 by design (creature_config.gd comment).
- **"Population 2.1" is most likely the species entropy row** (`entr`, bits, max
  log2(5)=2.32) of the TAB balance panel, not the herd. Only `entr` prints a decimal that can
  read 2.1 (herd is %d; wave is a 0-1 ratio), and it sits at 1.7-2.2 while the herd climbs
  from 10 to 66.
- **Population vs care: no stable margin.** Herd at 900 s care 55/66/64 vs neglect 24/50/65 in
  this batch; earlier batches had neglect ahead on 2 of 3 seeds. The batch-to-batch spread is
  as large as the policy gap.
- **Thefts and the 💰 status: unseen.** Two gates are closed: neither policy has a bank (a
  theft needs `Bank.with_loot`), and a theft needs a puffing creature (the snap gate above).
- **Lab pace:** the cost already grows (LabConfig 6 + 4 per known). Unlocks come every 1-3 min
  once the first lands.
- **The land is 60 x 60 m** (WorldWrap land ±30): a herd of 60+ needs dense beds; one-bed huts
  ran out of room.

## Resume here
- PR 1 merged (#338, 0.228.2). PR 2 merged (#339, 0.228.3): neglect snaps in 9 of 15 runs,
  care 0 of 9; per-seed guarantee left open (starving puffers stop; belonging averages out).
- PR 5 open as #340 (branch fix/lag-spikes, worktree mm-fixes), review round 2 fixed, CI green, ready to merge. Left open:
  the user's wave 46 autosave is still 105 ms (grid 53, creatures 34, store 16), and the
  1800 s care sim takes wall_s 574 against the 300 s goal. Both are proposed as follow-up PRs.
  Then 12 (balloons, small), then 11 (load), then 13 (farm circle), then 14 (room shapes), then 15 (eggs targeted), so later PRs measure on the user's own playtest state.
- PR 12 open as #341 (branch fix/balloon-only-when-missing, worktree mm-fixes2), rebased on
  #340, CI green, ready for review and merge. Nothing left in it.
- PR 11 open as #342 (branch feat/load-save, worktree mm-fixes2). Nothing left in it once CI
  is green. Load a playtest wave: `SIM_LOAD=user://saves/<session>/wave_<N>.save` plus
  `SIM_SECONDS` (or through `run_sims.sh`); sims now autosave to `user://sim_saves`.
- PR 21 open as #343 (branch fix/snap-real-play, worktree mm-fixes). Nothing left in it once
  CI is green. Its `spell_stops` SIM_RESULT field may conflict with #342's driver edits on rebase.
- PR 13 open as #344 (branch fix/farm-full-circle, worktree mm-fixes2), CI green, ready for
  review and merge. Nothing left in it.
- PR 14 open as #346 (branch fix/room-shapes, worktree mm-fixes2), CI green, ready for review
  and merge. Nothing left in it (stairwell join and cold-review fixes in).
- PR 4 open as #345 (branch fix/thefts-visible, worktree mm-fixes), CI green. Nothing left in it.
  Arrests 0 in playtest 2 was no police box (the lab drew the bank first); now the bank brings it.
- PR 15 open as #347 (branch fix/eggs-targeted, worktree mm-fixes2), CI green. Nothing left
  in it. Not measured: eggs broken over a full 900 s run (population effect, PR 3).
- PR 3 open as #348 (branch fix/population-brake, worktree mm-fixes), review round 2 fixed, CI
  green. Nothing left in it. Open for the user: neglect (no sleep beds built) now falls by night
  8-10 in sims (before: 2 of 3 fell, nights 15-17); care falls 1 of 3 before and after.
- Merged 2026-10-20 on local CI (Actions blocked): #349 (0.231.1), #350 (0.232.0), #352
  (0.233.0), #351 (0.233.1). Care herd >= 40 (PR 23's done line) still fails: PR 24.
- #351 merged (0.233.1). #353 merged (0.233.2); #354 (PR 28) merged (0.233.3). PR 25 open as #355 (fix/sealed-room-followups, worktree mm-fixes2), rebased on #354; three CI shards passed locally on 1413350e (totals in the PR body). Nothing left in it; rebase if main moved.
- PR 24 open as #360 (branch fix/care-herd, worktree mm-fixes3, rebased on 5b1a64a2), three
  CI shards green locally (totals in the PR body). Care median 44 (32/46/44), neglect breaks
  eggs 1/0/1. Nothing left in it; rebase if main moved. The batch spread is large (the same
  branch before the rebase gave median 34), so care >= 40 is fragile.
- PR 27 open as #359 (fix/chair-load-errors, worktree mm-fixes2, on 5b1a64a2): Chair._table
  guards out-of-tree; three CI shards green locally (1107 + 85 + 31). Nothing left in it.
- PR 28 open as #354 (branch fix/nav-alert-leftovers, worktree mm-fixes). Round 2 fixed every
  cold-review finding plus the feel_wire reset; three CI shards passed locally on 1c84627e
  (totals in the PR body). Nothing left in it; rebase if main moved.
- PR 22 (+9) open as #353 (fix/nav-race-farm-alerts, worktree mm-fixes). Round 2 fixed every
  cold-review finding (no rebake hitch measured; .uid already on main via #350). Three CI shards
  passed locally on 2ac05635 (totals in the PR body). Nothing left in it; rebase if main moved.
- #352 merged (0.233.0); its leftovers are in PR 26. Fork kept: a bar with no free INT 8
  friend stays closed.
- PR 26 open as #356 (branch fix/bar-open-trip, worktree mm-fixes). Three CI shards passed
  locally on 44c3b142 (totals in the PR body). Nothing left in it; rebase if main moved.
- PR 29 open as #358 (branch fix/mixed-bag-delivery, worktree mm-fixes). Three CI shards passed
  locally on 0d9983e1 (totals in the PR body; the later commit is README only). Nothing left in it; rebase if main moved.
- PR 30 open as #361 (fix/save-test-leak, worktree mm-fixes, on 8acddadc). Three CI shards
  passed locally on e54eeef5 (totals in the PR body; the later commit is README only). Nothing
  left in it; rebase if main moved.
- PR 31 open as #362 (fix/sim-quit-abort, worktree mm-fixes2, on 8acddadc). Three CI shards
  passed locally on f2b73091, every one exit 0 (the later commit is README only). Nothing
  left in it; rebase if main moved.
- PR 17 open as #363 (feat/roommates-mood, worktree mm-fixes, on 811cf51a). Review round 2
  fixed (sliced room recount, O(B) count, sharer card, tests); three CI shards green locally on
  dc24d93f (1118 + 85 + 31). Nothing left in it; rebase if main moved. Later slices proposed in
  the round's report (17b-17d).
- PR 33 measured, no code change, no PR (branch fix/roommates-snaps in mm-fixes is main
  unchanged). 900 s, SIM_WALL=0, seeds 1-3: before #363's term care snaps 0/0/0, neglect
  0/0/0; after care 0/0/1 (strain 0.36 -> 1.0 on 2 seeds, slow centre ~0.6 -> ~0), neglect
  0/0/0. Care with SIM_ROOM_BEDS=2: 0/0/0. Kept (round's pick): the care snap comes from
  9-bed bunkhouses, the crowding risk #363 designed. Raw output: the round's scratchpad pr33/.
- PR 32 open as #364 (fix/nested-couples, worktree mm-fixes3, on #363). Round 2 fixed every
  cold-review finding; three CI shards green locally on d6e17358 (87 + 31 + 1121).
  Faded halves (seeds 1-3: 30 -> 13; 12 seeds 92 -> 32), but care median on seeds 1-6 is 35.5
  (main 40; 12 seeds 36.5 vs 39, within per-seed noise of 15-20): relay decides on that half.
- PR 18 open as #365 (feat/economy-skeleton, worktree mm-fixes2, on cf6a4b6c), round 3 fix
  pass done: loot never spent, seller guarded, save VERSION 20, theft gate kept (wages do not
  stop a theft). Shipped work_s 978/1158/928 >= broke 931/994/921. Three CI shards green
  locally on 0501d88c (1126 + 87 + 31). Nothing left in it; rebase if main moved.
- PR 37 open as #366 (fix/neglect-snaps, worktree mm-fixes, on cf6a4b6c). Three CI shards green
  locally (1121 + 87 + 31). New sim policy `neglect` (housed in 9-bed bunkhouses, nothing else);
  care defaults to 1 bed per room; SPARE_BEDS 4. Neglect snaps 6/4/7, care 0/0/0. Sim
  baselines move: use `neglect`, not `turtle`, as the neglect row. Care herd 46/52/63 now. Raw
  output: scratchpad pr37/. Nothing left in it; rebase if main moved.
- PR 41 measured on main @ 9f8f7763, no code change, no PR (branch fix/care-herd-cap in
  mm-fixes3 is main unchanged). Metric: herd-days = mean herd over the 17 dawns of a 900 s
  run; seed SD care 3.2 (CV 19%), neglect 5.5; herd_end SD 14-23. Seeds decorrelate under any
  code change (paired SD >= unpaired), so ~18 seeds per arm resolve 5 end creatures. Top cap:
  the 2 starter medic beds (full 57% of the time, 30-80 loose bodies at dawn 17; the bot's
  medic buy never fires: a 104-plank hut). +4 medic beds: care herd-days 17.3 -> 26.8, then
  care's 1-bed rooms run out of land at ~30 sleep beds (no room 39% of the time) and neglect
  (84 beds in bunkhouses) reaches 43.8. Proposals in the round's report. Probe diff and raw
  output: scratchpad pr41/.
- PR 42 open as #368 (fix/sim-medic-herddays, worktree mm-fixes3, on 9f8f7763), sim only. Three
  CI shards green locally on 0da9cd3b (87 + 31 + 1126; later commit README only). 18 seeds:
  care herd_days 17.2 -> 26.3 (sd 3.1), neglect 14.6 -> 55.9 (sd 5.4), falls 1/8 -> 0/0; new
  herd baseline. Nothing left in it; rebase if main moved. Raw output: scratchpad pr42/.
- PR 38 open as #367 (fix/splash-allies, worktree mm-fixes, on 9f8f7763 #365). Round's pick: a
  herd swing's splash spares the herd; a wild's still splashes its pack. friendly_* deaths were 0
  before and after (6 runs); about 1300-1900 herd-on-herd splash hits per run removed. Three CI
  shards green locally on 02e789f7 (87 + 31 + 1127). Nothing left in it; rebase if main moved.
- PR 18i open as #369 (feat/economy-work-more, worktree mm-fixes2, on 73c47770). Built as a
  feature, effect unmeasured (user, 2026-10-21: "forget balancing for AFK"). Three CI shards
  green locally (1128 + 87 + 31). Cheat `/aspire`. Nothing left in it; rebase if main moved.
- PR 39 open as #370 (fix/late-couples-slab, worktree mm-fixes, on 73c47770), slab half only
  (user, 2026-10-21); the late-night couples half is dropped. Three CI shards green locally on
  cd90bccf (87 + 31 + 1129; later commit README only). Nothing left in it; rebase if main moved.
- Order from here (user, 2026-10-20): 7, 22, then (relay) 18i, 39, then alone on the CPU 36 and 43, then 19, 34, 35, 17, 18, 16, 10. The relay adds new
  PRs when a round finds needed scope (user, 2026-10-20: "create new PRs if necessary, specially for those that are not very
  defined and need more design"): a loosely defined item (17, 18, 19 curve, 20) is split into
  smaller PRs, each with a measurable done line, once its /design picks a shape.

## Decisions for audit
- 2026-10-21 (user) reverses #351's round pick: the teacher is a paid job again. /rule not run
  this session (usage at the limit): next session, diagnose why a round's pick that took a
  job's pay away (flagged here as "check against PR 18") shipped before the user saw it.
- #367 merged (0.235.1): a herd swing's splash spares the herd; wilds still splash each other.
  #368 merged (0.235.2): free medic beds in both bots, herd_days metric; herd baselines from
  before #368 are stale (use #368's 18-seed table).
- 2026-10-20 night: the auto-mode safety check gave no verdict for a while; PR 18i's round
  stopped with work uncommitted in mm-fixes2 (resumed after).
- #365 merged (0.235.0) after a fix pass: shipped work_s >= broke on every seed (3064 vs
  2846); loot is never spendable; save VERSION 19 -> 20 (LAW_save: refuse, never migrate), so
  the user's playtest saves (wave_40, wave_46) no longer load in the game or SIM_LOAD. A PR
  that needs the user's state must use a save made after 0.235.0.
- #366 merged (0.234.2), sim only: neglect = housed in 9-bed bunkhouses, nothing else; care =
  1-bed rooms; SPARE_BEDS 4. Neglect snaps 6/4/7, care 0. New baseline for herd numbers:
  care 46/52/63, neglect 55/28/60 (housed neglect matches care: PR 41 now asks whether care
  beats neglect). Older care medians (PR 24, 32) used 9-bed huts + 1 spare: not comparable.
- #365 gets a third, fix-only pass (relay, against the "two rounds then ship" rule): its
  shipped spend pull cut work 8% (seed 3: 18%), against the game frame "productivity first";
  plus a lost gem at a leaving bartender, loot not versioned in saves, stolen gems laundered
  by drinking (breaks the pouch pillar), and a mis-aimed test.
- #364 merged on fades alone after 2 rounds (relay): its care-herd half (median >= 40) was
  not met (35.5 on seeds 1-6) and is not caused by fades; carried to PR 41.
- PR 33 (measured, no code, relay accepted the round's pick): #363 tuning kept. Care with
  9-bed bunkhouses snapped once in 3 runs (seed 450; room term about -0.8); care with 1- or
  2-bed rooms 0. Crowding is meant to drag. Revert path if the user wants care = 0 with
  bunkhouses: ROOM_MOOD_FLOOR -0.5. Tables in scratchpad pr33/.
- 2026-10-20 relay slip: a `;`-chained merge+tag+branch-delete ran on after #356's merge
  failed (conflict), so the branch was deleted (PR closed) and 0.233.5 was put on #355. The
  tag was removed, the branch rebased (both tests kept) and landed as #357. Since then the
  relay chains merge steps with `&&`.
- 2026-10-20 (user): Actions blocked by billing, so merge on a cold review + all three CI
  shards passing locally (as ci.yml runs them), rebased on the current main.
- #351 (round's pick): the library became free-time INT reading (not a job), and TEACH lost its
  pay (a chalkboard takes one INT-12 friend). Check against PR 18 economy: skilled jobs may
  want wages again (user wants "work more if economy is well").
- 2026-10-20 (user): no poweroff for this relay; hypridle runs a copy of the AFK config
  without the poweroff listener (scratchpad hypridle-nopoweroff.conf). At the relay's end:
  `pkill -x hypridle; setsid -f hypridle` (normal 1 h config).
- The old HANDOFF_mood_redesign.md (relay done) was deleted; its open items carried: PR 9
  here; the design doc's open forks (discipline drain, place lift size, alone-in-bedroom
  cure, bar role, energy->mood) stay unbuilt except the bar role (PR 7, user); the gem pouch
  PRE-PILLAR in MEMORY.md still waits for the user.
- 2026-10-19: restored docs/BRAINSTORM_mood_fun_steam.md to HEAD in the main checkout (a
  stash pop had left conflict markers; the other side, an old draft, stays in stash@{0}).
