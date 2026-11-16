# DESIGN: challenge tree with fog of war (no Lab)

Temporary design doc. Only lines tagged (user) are decided; the rest is a proposal.

## Decided (user)
- The discovery reveal: a card is hidden until something near it makes it relevant.
- A literal UI graph shows the progression.
- The Lab is out of this test: every card opens by a challenge (user: "i want to see how it
  works without it").

- Hand deed + built parent as the two requirement kinds; medic bed before the emergency post;
  new hand deeds where the hook is small; the rest built (user: "proceed with all
  recommended").

- A deed may be the herd's, done through what the player built (user: "creature plants 10
  times"); the order between cards falls out of the deeds, never a hand-written build order
  (user).
- A herd deed shows its count on the card ("3/10"); a hand deed opens at once (user).
- A card is revealed only when its parent opens (user).
- Deeds climb in ladders per activity, by tens: produce 10 meals, then 100, then 1k; harvest
  10, 100, 1000 crops; mine 1, 10 gems. Each rung opens more cards (user). Counts are
  placeholders until a balance pass.
- Herd deed table (Claude draft, accepted on a blanket yes; counts are placeholders, not
  tuned): Cart Shed: chopper brings logs x10. Rail: hauler deliveries x10. Rail stops: lay a
  rail. Kitchen: farmer plants x10. Bar: cook serves meals x10. Shop: gems spent at the bar
  x10. Bank: clerk sells goods x10. Treadmill: bench press trainings x10. Library: a station
  waits for a worker no friend is smart enough for. Chalkboard: library reads x10. Open:
  the Lectern's deed; what Shop and Bank answer.
- The menu stays minimal first, filtered only if still big; stage 3 cards (rails, city stone)
  hide; one grey next card per tab; the Progress tab is one row per ladder (user: "proceed
  with all recommended").
- Built this round (Claude picks): ladders fell, crops, meals, gems, train, reads, saved per
  run; Lectern opens at 100 reads (not the zone idea: no small hook); Games Table, Campfire
  and Half Block hidden. Kept, not merged yet: Bar (needs the Kitchen to serve drinks) and
  Library (friends must still reach INT 12 to teach); rungs that upgrade a building and the
  Bank are a later pass.
- Upper-right: one bar per resource ladder, filling to its next milestone and emptying when
  it opens; wood and gems always, the rest as they unlock; the aim readout's stats and effect
  cards move into the creature panel (user). Built (Claude picks): wood and gems count what is
  gathered (logs off a felled tree, gems off the ore), not spent; a name + HP glance stays
  under the crosshair; the Progress tab stays; a ladder with every card open leaves the
  corner; the panel's readout is a new first tab, "Now".
- The first 10 wood opens the Woodpile (user); a run starts with only the first wood and gem
  rungs shown, everything else behind them (user: "too many bars"). The corner shows one bar
  per shown locked card (user). Claude picks: Mine at 10 gems, Cart Shed 100 wood, Shop 100
  gems, Bank 1000; Farming, Nest, Medic Bed, Police Box hang under the Woodpile; Bench Press
  and Library under the Mine; the chop and axe-the-ore hand deeds are gone.
- The Cart Shed is out; a zone takes its wood from the woodpile and from logs the player
  drops in (user). The Zone and the Stairs are locked behind something (user). Claude picks:
  the Zone hangs under the Lectern (its builders graduate there) and opens on a Room built by
  hand; the Stairs are the wood ladder's second rung (100).
- The frog is parked: it needs polish and is secondary to the core design (user). A guide
  like Valheim's Hugin breaks this game's pace (user).
- No unproven shapes: copy a pattern a shipped game uses, never one nobody has done (user:
  "lets not try something that wasnt done before").
- The build UI is not a bottom-of-screen toolbar (user); references come from action games,
  not building games (user: "timberborn way is more like a building game").
- The Progress tab as a separate screen hurts discoverability (user, 2026-10-27); reversed
  2026-10-28: the tree moves out of the build menu onto T (user); the tree-as-menu
  sketch is dropped (unproven).

## Milestones v2: three axes, a healthy run (Claude, user asked for fewer axes)
Axes are what the player gathers by hand first and the herd later: 🪵 wood, 💎 gems, 🌾 crops.
Each rung roughly x2.5 (10, 30, 80, 200, 500): x10 rungs leave long dead stretches. Care
cards open by the hand deed they automate; furniture opens by building its parent (a bed
once a room stands). Training, reading and meals are no longer axes.

| Axis | Rung | Opens | Why then |
|---|---|---|---|
| 🪵 | 10 | Woodpile | day 1: a chopper takes the axe off you |
| 🪵 | 30 | Build (walls, floors) | before the siege on night 3: fortify the statue |
| 🪵 | 80 | Room | night 3-6: house the herd yourself |
| 🪵 | 200 | Stairs | late: build up when the ground runs out |
| 💎 | 10 | Mine | day 1-2: a miner takes the ore off you |
| 💎 | 30 | Bench Press | before the bigger sieges: fighters train STR |
| 💎 | 80 | Library | jobs need INT 8: friends read up to it |
| 💎 | 200 | Furniture shop | gems pile up: friends buy lamps and gifts |
| 💎 | 500 | Bank | late: gems need a vault (and thieves a target) |
| 🌾 | hand | Farming (pick a ripe crop) | day 1: the farmer takes picking off you |
| 🌾 | 10 | Table | a place to eat |
| 🌾 | 30 | Kitchen | crops become meals at the tables |
| 🌾 | 80 | Bar | crops become drinks, a second gem sink |

Built chains (open when the parent is built): Room → Bed, Lamp; Bed → Jail; Table → Chair;
Bench Press → Treadmill; Library → Chalkboard → Lectern → Zone.
Hand deeds: Medic Bed (carry a downed friend, after Woodpile), Emergency Post (lay one in a
medic bed), Nest (carry an egg, after Woodpile), Police Box (jail a friend, after Jail).
Scene: a run opens with two bars, Woodpile 0/10 and Mine 0/10. By dusk of day 1 both open;
the next bars are Build 10/30 and Bench Press 10/30, plus Farming (✋) once the woodpile
stands. The first siege finds walls up; its downed friend opens the Medic Bed.

- The Pier is not a card: nature places one on the shore at the start, and a boat comes each
  dawn with no free-bed rule (user).

## Milestones v3: rungs matched to costs (Claude, user: "unlocks don't meet what they cost")
Every card costs 1-6 wood or up to 10 gems, so a rung sits at 1.5-6x its card's cost. The run
starts with food: picking, feeding, harvesting (user), then beds and building.
- Start: Farming (pick a ripe crop), Woodpile (5 wood), Mine (5 gems).
- Food: Farming → Table (feed a friend by hand) → Kitchen (15 crops) → Bar (40 crops);
  Table → Chair (built).
- Wood: Woodpile → Build (10) → Bed (15) → Room (25) → Jail (40), Stairs (60); Room → Lamp
  (built); Bed → Medic Bed (carry a downed friend) → Emergency Post; Bed → Nest (carry an
  egg); Jail → Police Box (jail a friend).
- Gems: Mine → Bench Press (15) → Library (25) → Shop (40) → Bank (60); Bench Press →
  Treadmill; Library → Chalkboard → Lectern → Zone (each built).

### Roadmap v3 (estimated from config rates, unmeasured)
Rates: first daylight 24 s; a tree falls in 2 s for ~4.8 logs; the axe knocks 1 gem per 5 s;
a miner 1 gem per 8.5 s; sieges on nights 3, 7, 12.
| When | The player does | Opens |
|---|---|---|
| Day 1 | picks wild crops, feeds a friend, fells 2-3 trees, axes the ore | Farming, Table, Woodpile, Build |
| Day 2 | chopper and farmer start; 5 gems | Bed, Room, Mine |
| Day 3 | walls round the statue; a room | Lamp, Kitchen (15 crops) |
| Night 3 | carries a downed friend to a bed | Medic Bed, Emergency Post |
| Days 4-6 | miner + axe ~6-8 gems a day; eggs | Bench Press, Nest, Jail |
| Night 7 | trained fighters | Treadmill |
| Days 8-11 | gems pile up; a friend snaps | Library, Stairs, Police Box, Bar |
| Day 12+ | economy, school | Shop, Bank, Chalkboard, Lectern, Zone |

## Built on `feat/challenge-tree` (Claude picks, reverse freely)
- Checked: jail, games table, city stone, campfire, pier and the basics were already open at
  the start, so they stay open; clock and combiner are not in the card pool (not in play).
- Seen is derived from the open set (open, or parent open, or no parent): no new save field.
- New hand deeds: pick a ripe crop (Farming), lay a downed friend at a free medic bed
  (Emergency Post), a thrown friend hits a beast (Bench Press). Cart shed: built woodpile
  (taking wood by hand had no small hook).
- Library: built any job station, as a root. Kitchen hangs under Farming.
- The tree is a "🌱 Progress" tab in the build menu (no new key). It shows only cards that
  ask something or have a child; free basics stay off it. No pulse on new cards yet.
- The Lab card is out of the menu; its code and tests stay (tests inject their own lab cards).
- Unverified: the thrown-hit hook runs in the creature's physics; assumed server-side only.

## 1. Abstract (no domain nouns)
- **Roles:** a set of nodes; each node has one parent and one requirement. The player emits
  events. A node is hidden, seen, or open.
- **Rules:** a seen node opens when its requirement event fires. A node becomes seen when
  its parent opens (roots are seen from the start). Hidden nodes show only as an anonymous
  stub count under an open parent.
- **Ledger:** no resource moves. The only counted state is two growing sets (seen, open);
  neither ever shrinks, so there is no drain and no loop.
- **Three framings:** (a) a map with fog (exploring reveals the next region); (b) a tutorial
  that teaches one verb, then hands it to the city; (c) an achievement list whose rewards
  are buildings.

## 2. Research (from memory, not looked up this session)
- **Minecraft advancements:** a node graph in tabs; a child stays hidden until its parent is
  done, then shows with its goal. Closest match to the fog graph.
- **Subnautica:** a blueprint is unknown until you scan a fragment of it in the world; the
  PDA lists only what you have met. Reveal by touching the world.
- **Terraria NPCs:** a townsperson moves in when a condition you met holds (you hold a gun,
  you built a house). Unlock by a deed, no research.
- **Factorio / Civilization:** the full tree shows from the start. Rejected: it is the wall of
  locks the user turned down.

## 3. Theses for "what is a challenge"
1. **Hand deed (the pillar):** a job card opens when the player does that job by hand once
   (chop, so the woodpile opens). Purpose: teach the verb, then hand it to the city.
2. **Build milestone:** a card opens when its parent stands built ("build a kitchen" opens
   the bar). Purpose: the city grows by what the player built.
3. **Herd need seen:** a card opens when the herd first shows the need it serves (no friend
   is smart enough for a job, so the library opens). Purpose: the answer appears when the
   question does.

### Socratic pass + antithesis
- T1 fails for cards with no hand verb (bar, bank, rail, clock). Inventing a hand verb only
  to open a card breaks "natural on sight".
- T2 alone becomes "build everything in order": a list, not a challenge. It is still legible
  and cheap, and it never stalls.
- T3 can stall (if the need never shows, the card never opens) and can fire with nobody
  noticing. It reads well only when a balloon or the frog points at it.
- Opposite case (show everything locked): already rejected (user).

### Scene (T1 + T2 mixed)
The player axes the ore by hand, and a banner says "Mine opened: you axed the gem ore". In
the graph, the Mine lights up and a "?" stub hangs under it. The player builds the Mine,
and the stub turns into a new card ("needs: Mine built"). Reads right.

### Synthesis (recommended)
**One requirement key per card, of 2 kinds in the MVP:** `hand:<act>` where a hand verb
exists (T1), else `built:<parent>` (T2). T3 (`herd:<need>`) is the next step after the MVP,
one card at a time, each with a sign that points to it.

## 4. Proposed tree (edit me)
Roots, open at the start: basics (room, zone, wall, stairs, floor, block, half block, ramp,
bed, table, chair, lamp), pier, campfire. ASSUMPTION: these are open at the start today.

| Card | Parent | Requirement | Kind | Note |
|---|---|---|---|---|
| woodpile | (root, seen) | chop a tree | hand | exists |
| mine | (root, seen) | axe the gem ore | hand | exists |
| nest | (root, seen) | carry an egg | hand | exists |
| medic bed | (root, seen) | carry a downed friend | hand | swap: hand-carrying a body comes first |
| emergency post (med kit) | medic bed | put a downed friend in a medic bed | hand | the post's medic then does it |
| jail | (root, seen) | pick up a rampaging friend | hand | new act |
| police box | jail | jail a friend | hand | exists |
| basket (farm) | (root, seen) | pick a ripe crop by hand | hand | new act; ASSUMPTION: the player can pick crops |
| kitchen | basket | build a basket | built | T3 later: "a friend is hungry" |
| bar | kitchen | build a kitchen | built | |
| shop | bar | build a bar | built | |
| bank | shop | build a shop | built | |
| cart shed | woodpile | take wood from a woodpile | hand | hauling by hand |
| rail | cart shed | build a cart shed | built | |
| rail loader | rail | build a rail | built | |
| rail unloader | rail | build a rail | built | |
| gym | (root, seen) | knock down a beast with a thrown body | hand | new act |
| treadmill | gym | build a gym | built | |
| library | (root, seen) | build any job station | built | T3 later: "no friend is smart enough" |
| chalkboard | library | build a library | built | |
| lectern | library | build a library | built | |
| games table | (root, seen) | ? | open | role unclear to me |
| clock | ? | ? | open | role unclear to me |
| combiner | ? | ? | open | role unclear to me |
| city stone | ? | ? | open | role unclear to me |
| lab | hidden | none | out | excluded (user) |

## 5. Spec
**Data dictionary**
- `parent` (card id or none, authored, fixed): where the card hangs in the graph.
- `requirement` (one key, authored, fixed): `hand:<act>` or `built:<card>`.
- `seen` (set of card ids, saved, only grows): cards shown in the graph and the Work tab.
- `open` (set of card ids, saved, only grows): cards the player can build. Open implies seen.
- `opened_by` (card id to key, saved): the banner's and the graph's "why".

**Ownership:** all five live in the blueprint registry; the graph and the Work tab only read.

**Pipeline**
1. An event fires: a hand act, or a piece is built.
2. Every seen, not-yet-open card whose requirement matches opens; `opened_by` records why.
3. Each child of the opened card becomes seen.
4. The graph and Work tab redraw; the banner names the card and the deed.

**Interaction matrix:** event to open (yes), open to seen children (yes), seen to the event
(no). No loop, no drain; the Contradiction Check is clean.

**Charts / constants:** no formulas. One constant: the number of start roots (a limit on
first-screen clutter; about 8 seen job cards with the table above).

**Failure modes**
- Stall: a hand act the player never thinks of (pick up a rampager). Mitigation: the frog's
  dawn line names one seen card's deed. Cheat: open all / reveal all.
- Piling: many reveals at once (building a basket reveals the kitchen only, one child each).
- A `built:` chain reads as a list. Accepted for the MVP; T3 keys replace links later.

## 6. Graph UI
- A panel on a key: columns by depth, a line from each parent to each child.
- Node states: open (full colour, built count), seen (grey, requirement icon and words),
  hidden ("?" stub, count only).
- A newly seen node pulses until the panel opens. Clicking an open node selects it in the
  Work tab.
- The Work tab lists open and seen cards only; the "two steps ahead" rule is dropped.

## 7. MVP scope
In: the seen set + save, `built:` keys, the 5 existing hand acts, the new tree table (cards
with an open row stay hidden), the graph panel, the lab hidden, a reveal-all cheat, and
tests (reveal on parent open, a hidden card stays hidden, a `built:` open, a save round
trip). Out: the new hand acts (pick up a rampager, pick a crop, take wood, a thrown
knockdown) unless each is a small hook; T3 need keys; the Lab's new role.

## Hard to handle, first goal, goal cleanup (2026-10-28, fast iteration)
- Hunger or sleep under 0.3 pulls the mood centre down, to -4 each at 0, so an unfed or
  unrested friend snaps (Claude; user picked "needs bite").
- A friend dies of hunger 3 days after a full meal (user); `perish`, so friends grieve.
- A bad mood slows every work swing, to 0.4 pace at mood -5 (user: a downward spiral).
- Feeding a friend by hand is the run's one first goal: Table is the only root card, and
  Farming, Woodpile and Mine hang under it (user).
- Goals that did not fit what they open (Claude, user: reuse the same goals): Jail opens on
  carrying a downed friend (was 40 wood), Bench Press on throwing a friend into a beast (was
  15 gems), Library moves under the Mine.

## Counted goals v4 (Claude, user: "3 -> 10 -> 50", "feed and harvest are conflicts")
User asks (user): every goal is a counted bar; rungs reuse one act (3, 10, 50); several bars
at once; each act has its own emoji; the bar does not name the card.

### Abstract
- **Roles:** the player (acts by hand), the herd (acts on its own), one counter per act, rungs
  on the counter.
- **Ledger:** one supply per act. Feed draws a friend's hunger room (drains 0.5 a day, filled
  0.5 by any meal; a friend takes food only at 0.5 or below). Pick draws ripe crops (grown on
  plants, taken by any picker).
- **Rule in force:** the counter counts only the player's draws, but the herd draws the same
  supply first. The starter herd starts at 0.4 and eats a berry off a plant at 12 s, so no
  friend has room for a hand feed on day 1.
- **Framings:** (1) a race over a shared pool; (2) a counter that counts the wrong actor;
  (3) the herd already does the job with no building, though the pillar says the herd takes
  a job over only through a building.

### Research
- Satisfactory: hand-craft first, milestones open the machines that automate it
  ([guide](https://xgamingserver.com/blog/satisfactory-beginners-guide/)).
- Cult of the Lamb: follower hunger fills only from meals the player cooks; the Kitchen lets
  followers cook on their own ([wiki](https://cult-of-the-lamb.fandom.com/wiki/Kitchen),
  [guide](https://primagames.com/gaming/cult-of-the-lamb-cooking-hunger-guide)). From memory,
  unchecked: followers never forage on their own.
- Stardew Valley: count goals on one act at two sizes, 15 and 300 crops
  ([wiki](https://stardewvalleywiki.com/Achievements)).

### Theses
| # | Shape | Verdict |
|---|---|---|
| T1 | Count every meal eaten, hand or herd | Cut: the herd fills it alone (3 meals in 12 s); no hand act, breaks the pillar |
| T2 | A hand feed is a treat that needs no room; only hand feeds count | Weak: 50 is a berry-spam; full friends eating hides the hunger rule; the pick race stays |
| T3 | The herd takes no food off plants until a building lets it; one counter per act counts the hand first, the building later | Recommended |
| T4 | Merge feed into the crops counter | Cut: feeding and picking are two jobs with two buildings, so two acts (pillar) |

### T3, the recommendation
- **Before the Table, only the hand draws the supply.** Friends eat only from the hand; they
  do not chase food on the ground. The starving valve (hunger 0 for 40 s, then a ripe crop)
  stays. Once the Table opens, they forage again.
- **After the building, both add to one counter.** The race is gone: whoever draws, it counts.
- **Ladders that reuse one act:** 🍓 meals eaten (hand, then any meal): 3 Table, 10 Kitchen,
  50 Bar. 🧺 crops picked (every harvest, hand or farmer): 3 Basket. 🪵 and 💎 stay as
  they are. Built (Claude pick): the four roots (Table, Basket, Woodpile, Mine) start seen.
- **One-card acts stay one rung (3) for now:** 🚑 carry a downed friend (Medic Bed 3, Jail 10),
  🛏️ lay one in a medic bed (Med Kit), 🔒 jail (Police Box), 🥚 egg (Nest), 🎯 throw (Gym).
- **Scene:** day 1, three friends show 🍎. The player picks a berry off a bush (🧺 1/3) and
  feeds a friend (🍓 1/3). After three, the Table opens; friends now eat berries off the
  ground and every meal keeps counting (🍓 4/10).
- **Antithesis:** a player who ignores food starves the herd. That pressure is the day-1
  decision (feed or chop). Open: what a friend at hunger 0 does today.

## Sieges from night 1 (user: "bruiser should happen in first night")
- Sieges on nights 1, 3, 7, 12, 17 (gaps 1, 2, 4, 5) (Claude): adds night 1, keeps the rest.
- Every wave's budget +3 (Claude): night 1 affords one Bruiser (6); night 3 now affords two.

## Berries only (user: "berries the only fruit and everyone's favorite")
- The world scatters only berry bushes; carrots and corn stay in the files and in cheat scenes
  (Claude: hide before delete).
- Every species' favorite is the berry; the kitchen's crop is the berry (Claude).
- First wood goal 8, not 10 (Claude): two felled trees reach 8 in 91% of runs, 10 in 54%.
