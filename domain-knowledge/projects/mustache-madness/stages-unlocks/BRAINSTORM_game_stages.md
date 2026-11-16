# BRAINSTORM: game stages (stage 2 and stage 3)

An idea pile for the user to cut. Only lines tagged (user) are decided.
Tags: **[C: source]** = checked, with where; **[A]** = assumed, not verified.

## Seeds and decisions (user, 2026-10-20)
- **Frame (user): "productivity is the number one priority to survive each wave."**
- "It has to grow exponential"; the early game is good; stages 2 and 3 must not play like it.
- Stage 2: creatures learn to build, through studies, a university and more jobs; "we need
  architect and builders". **Decided (user):** "the player chooses where it can build, the
  architect designs how, and the builders build."
- Stage 3: "interconnected cities, with logistics, trains and traffic".
- Market arc: exchange, then creature businesses, then a stock market and startups with their
  own buildings and jobs, "to improve consumerism". Queued: wages into a creature's own pouch,
  shops (barber, furniture, gift, arcade, hot-tub spa, lottery, pawn), roommates feed mood,
  mood raises fertility.

## Decisions (user, 2026-10-21)
- **Stage 2 = Shape 1, anchor zones** (Q1): the player drags a zone and places one anchor that
  names its purpose; the architect designs the rest; builders build.
- Q3 architect style: **skill only for now** (how tight the shell is). Later: the architect
  copies the style of the player's own nearby buildings.
- Q4 builder materials: **a stockpile that a builder job fills, like the kitchen's.**
- Q5 stage 3 land: the player connects several cities they build. No reason to build a second
  one exists yet; later maps and levels give one, e.g. resources only some land has (ore, oil).
- Q6 trains carry **resources and creatures**.
- Q7 wilds and rails: **rails do not block wilds; wilds walk across them.**
- Q2 approval: **15 s after the player defines the zone, building starts** (the window to
  undo; no gem payment, no approve button).
- Q8: **university tuition in gems: yes.** A student pays from its own pouch to study.
- Q9 backing a startup: **needs more design** (not built).
- **Stage 3 = specialist cities joined by rail (user), needs more design.** Seed (user):
  "status or city tags that create their own mood or effects" (a city's tags shape how its
  creatures feel and what it does). Not built until designed.
- **Logistics jobs (user): stages 2 and 3 need more jobs that carry resources from x to y.**
  Stage 2: a hauler moves stock between stations (woodpile -> site stockpile, basket ->
  kitchen or bar); stage 3: loading and unloading trains between cities.

## 1. The frame
**Productivity** here = labor ticks per game day, summed over the herd (a labor tick is one
chop, dish or study tick [C: creature_config.gd:203, 436]); no herd-wide counter exists
[A: grep found none]. A wave tests it: what the herd made by dusk (walls, lamps, healed and
trained fighters, food) is what stands at night.
A later stage feels like growth, not more of the same, when three things move up one level
together: (a) the player's decision unit (a piece, then a zone, then a network), (b) the level
below runs itself where the player can watch it, (c) a threat arrives that attacks the new
level. **Exponential** = productivity per player decision multiplies: one zone yields a
building, one business yields a shop full of jobs, one rail line feeds a city. Body count must
not be the multiplier (fps). Every feature below states how it raises productivity, or is cut.

| Fact | Tag | What it says |
|---|---|---|
| Herd at dawn 47 (w20), 69 (w30), flat 55-60 w23-35, then 56 -> 147 in 5 waves | [C: brief] | Growth stalls then bursts unsteered |
| Lab: 7 finds w19-27, none for 10 waves; 11 blueprints exist | [C: brief; systems/progression/content] | The tech ladder runs dry mid-run (all found: [A]) |
| Median fps 58 at w20, 24 at w40 | [C: brief] | Count cannot grow exponentially on one map |
| Land 60 x 60 m; a herd of 60+ needs dense beds | [C: level_02.tscn:26; HANDOFF_playtest_tuning.md] | Home plot full by stage 2 |
| Player lays every piece by hand; jobs gate on INT; library raises INT | [C: brief; README] | Building is the verb to hand off; study -> job exists |
| Gems enter only from gem bushes the player builds; a sign takes 1 gem per 60 s shift on its own clock, 4 stacked at most; every creature holds a pouch | [C: wage.gd:4-13; blueprint_registry.gd gem_bush] | Stage 1 economy on main (0.237.0): what stage 2 founders and rail lines spend |
| Anchor names a room's type; a leaky shell shows 🏚; wild punches reset at dawn | [C: LAW_room_types rule 1; LAW_rooms rules 3-5] | An architect's mistakes and a raided site already read on sight |
| Wave budget quadratic in night number; creatures show wish balloons (🔥, 🍽) | [C: wave_config.gd; offer_place.gd:16] | Threat grows in count only; the herd's wants are visible |

**Prior art** [C, sources below]: Factorio (ghosts built by robots from the nearest stock);
Anno 1800 (met needs climb residents a tier, each tier unlocks buildings and harder needs);
RimWorld (raids scale with wealth and head count, not the clock); Dwarf Fortress (migrants by
created wealth); Kingdom Two Crowns (player sails to a larger island when they choose; left
builds decay); Against the Storm (a second seasonal threat layer); Mini Metro (station crowding
ends the run); They Are Billions (every infected left alive joins the final horde).

## 2. Stage shapes (stage 2 split is decided; shapes differ on the open parts)
**Shared.** University: a room type whose anchor (lectern) names it [A: piece]. Drafting
table teaches the **architect** track (INT, after the library), workbench the **builder**
track (STR or DEX) [A]. A student takes the track its own top stat fits among the classrooms
that stand: study is raising; the player only places classrooms (Roles pillar holds). Hats:
architect a blueprint roll and pencil, builder a hard hat [A]. New jobs: architect, builder,
hauler, professor. **On screen:** the architect walks the zone with a tape measure and stakes;
the blue ghost appears behind its pencil; builders carry plank stacks from the woodpile frame
(walk-in pickup [C: README]) and hammer pieces in. **Productivity:** the player's build hours
turn into herd labor; one zone = a building. **Wave test:** wilds punch scaffolds; a site half
built at dawn stays half built. **Stage 3 entry (all):** home land full; a station at the edge.

### Shape 1: Anchor zones (the player's piece names the purpose)
- Player drags a flat zone and places one anchor (bed, kitchen, lab) in it; the anchor states
  the purpose, as it names a room's type today. An empty zone stays empty.
- Architect designs shell and fill (more beds for a Bunkhouse). INT sets how tight; personality
  sets style: low discipline = crooked roofs, high warmth = big shared rooms [A].
- Ghost stands one game minute; the player vetoes by breaking a ghost piece [A].
- Failure: a weak architect leaves a gap over 4 m, the room shows 🏚 with the existing caption.
- Productivity: every anchor the player places becomes a working room without the player's
  labor. Passive policy (no zones) builds nothing, so the choice is real.
- Essence: "the player names what and where in one placement." Survives all pillars checked
  (Natural on sight, Add connections, Sacrifice: builders and planks leave other work).

### Shape 2: Free zones, the architect reads the herd
- Player marks only where; the architect builds what the balloons and outdoor sleepers ask most.
- Failure: it builds what the herd wants, not what the night needs (no walls unless asked).
- Productivity: rises only as far as wants match work; walls never. Passive "zone everything"
  likely matches the active policy (MEMORY: a decision must beat the passive policy). Weak.

### Shape 3: Commissioned plans (the player funds one design)
- Each free architect drafts a rival ghost in the zone; the player throws gems (**Q**, the
  existing pay verb) into the one to build; the rest fade. The gem is the architect's wage [A].
  Superseded: Q2 (user) starts a build 15 s after the zone with no gem payment.
- Productivity: same as Shape 1 plus a gem sink. Bends "Sacrifice through occupied state, not
  a price" like the job-economy PRE-PILLAR, and adds a pick step Shape 1 gets in one placement.

### Track D: the wilds learn too (combines with any shape)
Stage 2 wilds bring ACME ladders and rams; stage 3 wilds sit on the rail and get flattened by
trains (sent flying). Threat grows in kind, so later nights need fewer bodies (fps) [A].

## 3. The market arc (mapped onto the stages)
| Step | Player does | Creatures decide | On sight (goofy) | Productivity | Failure |
|---|---|---|---|---|---|
| Stage 1: exchange + wages | Builds stations and gem bushes; pays signs by time (1 gem = one shift) | A worker's wage goes to its own 💰 pouch; it spends at the shop it wants | Walks out of the furniture store with a bed on its head | Wanting a thing drives work: more shifts taken while something is affordable [A] | Thieves (theft exists [C: README]); an empty pouch brews |
| Stage 2: creature businesses | Marks a shop zone (where) | A **founder** with a full pouch (the pouch is enough, user 2026-10-24) opens the shop its herd wants most; the architect designs it; it hires staff | A hedgehog in a tiny top hat flips the OPEN sign | New jobs appear without the player building them; spending pays wages back | **Bankruptcy:** no customers, boards on the windows, founder back to the herd, the shell waits for the next founder |
| Stage 3: stock market + startups | Backs a startup by paying its sign, like any sign (Claude, `docs/BRAINSTORM_design_c6_stage3.md`; an exchange board is cut as menu-driven) | Startups found their own buildings and jobs in any city; trains ship their goods | Ticker tape rains on a boom; a crash blows the hats off | Capital flows to the startups the player backs, so jobs and goods appear where the network needs them | **Crash:** a startup closes, its workers idle and brew; **monopoly:** one chain buys the shops, prices up, mood down |

**Pillar checks.** Roles: a founder emerges from its own traits, never from a purchase; a
full pouch gates founding, earned by work (raising), not bought by the player (settled: the
pouch is enough, user 2026-10-24). Sacrifice through occupied state: a shop occupies a zone, builders, staff and the
herd's gems; holds. Shares bend "never a resource pile" and risk menu-driven action unless the
exchange is a readout board only. **Essence vs the productivity frame:** stage 1-2 earn their
place (work drive, jobs from creatures); stage 3's stock market earns it only if backing a
startup changes which jobs exist where; as pure gem growth it is a resource pile: cut.

## 4. Ranked recommendation
1. **Shape 1 + Track D, market steps 1-2 in stage 2, startups ride the trains in stage 3.**
   Every player verb stays "what I place, and where"; productivity multiplies by delegation
   (zones, then businesses, then lines), not by body count.
2. Shape 3's payment inside Shape 1 if the economy wants a gem sink. 3. Shape 2: fails the
   passive-policy check.
**Proposed pre-pillars (unconfirmed):** each stage hands one hand-verb to the creatures and
gives the player one verb a level up; a stage opens by something the player builds or raises,
never the clock. **Walking skeleton:** one architect and one builder graduate, one bed zone,
one ghost hut built from woodpile planks, one wild punching the scaffold. Cheat `/architect`.

## 5. Questions only the user can answer
1. Zone purpose: an anchor the player places (1), or free for the architect (2)?
2. Before builders start: veto by breaking the ghost, fund it with gems (3), or no approval?
3. Architect style: visible taste (crooked, cozy, grand) or only skill (tight vs leaky)?
4. Builder materials: the woodpile as today, or a lumber stockpile per site?
5. Stage 3 land: one growing map or several plots you ride between? A city out of view:
   fights its own nights, or runs a cheap summary [A: cheaper for fps]? (Answered in part, see
   Decisions Q5; the rest is proposed in `docs/BRAINSTORM_design_c6_stage3.md`.)
6. What trains carry: creatures, eggs, crops, planks, gems, startup goods? (Answered: Q6.)
7. Wilds vs rail: block it, break it, ride it, get flattened? Traffic: a threat or a look?
   (Answered: Q7, wilds walk across.)
8. University tuition in gems? Does saving gems gate a founder (Roles pillar)? (Answered: Q8;
   founders' capital is the pouch, user 2026-10-24.)
9. Stock market: how does the player back a startup on sight, and what does backing change?
   (Open, Q9; proposed in `docs/BRAINSTORM_design_c6_stage3.md`.)
10. Do the productivity counter and the two pre-pillars hold?

## Sources
[Factorio wiki](https://wiki.factorio.com/construction_robot) ·
[Anno-Union tiers](https://www.anno-union.com/en/devblog-residential-tiers/) ·
[RimWorld raid points](https://rimworldwiki.com/wiki/Raid_points) ·
[DF migrant](https://dwarffortresswiki.org/index.php/DF2014:Migrant) ·
[Kingdom islands](https://kingdomthegame.fandom.com/wiki/Islands_in_Two_Crowns), [boat](https://www.magicgameworld.com/kingdom-two-crowns-the-boat/) ·
[Blightrot](https://eremitegames.com/experimental-blightrot-revamp) ·
[Mini Metro](https://igf.com/mini-metro), [Mini Motorways](https://www.nme.com/features/to-every-commuter-in-my-mini-motorway-cities-i-am-sorry-3013239) ·
[They Are Billions](https://they-are-billions.fandom.com/wiki/The_Goddess_of_Destiny)

## Economy as automation (design pass, 2026-10-24; picks are Claude's until tagged "(user)")
User frame (user): stage 1 is manual (the player does everything); stage 2 is more automated,
creatures start doing what the player does, and the player orchestrates a whole city
(logistics, housing with rent, urban planning); stage 3 is several cities, the hardest
logistics, creatures make bigger calls (buy land), and the player keeps control in the chaos.

### How an economy raises productivity (abstract)
- Fields' answer (memory): specialization plus exchange (Smith); prices carry what each agent
  knows to everyone else, so no planner has to know it (Hayek's knowledge problem); wages and
  profit point each agent's effort; savings become capital (tools, buildings).
- Here the player is the central planner, and the planner's attention is the bottleneck: every
  open shift is one player decision. Productivity per player decision is the number that must
  multiply (the frame of section 1).
- So creature gems are not there to make a stage 1 creature work harder (measured, cut). They
  are the channel that lets creatures take over allocation calls: a gem spent says where demand
  is; a gem saved is capital a creature can invest. Stage 1 seeds the channel; stage 2 cashes it.

### By stage
| | Who allocates | Creature gems do | Player's verb | Productivity per decision |
|---|---|---|---|---|
| Stage 1 (manual) | the player, gem by gem | wages, buying, the broke state: demand shows on sight | throw gems on signs, place pieces | 1 decision = 1 shift |
| Stage 2 (city) | creatures, inside the player's zones | a founder with a fat pouch opens and funds a shop where buyers are; rent sorts who lives where; haulers paid per delivery | zones, rules, fixing failures (bankrupt shop, homeless, crime) | 1 zone = a self-funding street |
| Stage 3 (cities) | creatures across cities | prices differ by city, so trade on rails pays; creatures buy land | rails, city tags, policy levers | 1 line = a city fed |

### What this changes in today's decisions (checks)
- PRE-PILLAR "which workplaces stay open is always the player's call" holds for stage 1 only; a
  stage 2 founder funds its own shop (matches the funder slot "player or a creature owner",
  user 2026-10-22). "A customer never opens a workplace" (user) still holds: an owner funds it,
  customers pay the owner.
- The pouch is stage 2's capital: a founder emerges from the gems it earned (user 2026-10-24:
  the pouch is enough). So no sink is needed for it.
- Rent (user idea): rent on a basic need is the Dwarf Fortress warning (homeless, miserable).
  Candidate: free bunkhouse beds stay the floor; a private room costs rent. Ties to "caring more
  should grow a bigger herd; bunkhouses should grow less" (user 2026-10-21).
- Tax, rejected for stage 1 as a rate, may return in stage 3 as a policy lever over an economy
  the player no longer runs by hand. Proposed as a placed tax office, not a rate menu
  (`docs/BRAINSTORM_design_c6_stage3.md`).

### Picks (user, 2026-10-24)
- Frame confirmed (user): creature gems exist so creatures can take over the player's calls
  (where shops open, who lives where, what ships); each stage is judged on productivity per
  player decision.
- Stages have no hard edges (user): "they are just happening". So no rule names a stage; a
  capability starts when what enables it emerges (a founder with a full pouch, a landlord).
- Rent (user): bunkhouse beds stay free; a private room costs rent, paid to its owner, once
  creature landlords exist.
- Founders' capital (user): the pouch is enough; no savings rule.
