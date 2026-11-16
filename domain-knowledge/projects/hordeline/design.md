# Hordeline: design framework

Decided rules only. The weapon/part list is **not** decided yet (see Open questions).
Market research behind these choices lives in `~/Playground/game-design-research` (`research.md`, `data/`).

## Pitch
A co-op chaos train defense with roguelite builds, for 2–8 friends. The crew keeps one rickety train
alive through an endless horde: weapons fire on their own, every weapon brings a chore, and whoever
wears the captain's hat picks the next upgrade.

Positioning (user, 2026-11-02): "co-op chaos train defense with Vampire Survivors-style upgrades".
Name the build loop plainly (1-of-3 picks, weapon levels, evolutions); it is true and it is the hook
survivors fans know. Don't call the game "a survivors-like" or "bullet heaven": those promise dodging,
which Hordeline doesn't have.

## Pillars
1. **Multitasking chaos, not dodging.** The fun is keeping too many things running at once.
2. **The build is the workload.** Each upgrade adds power *and* a new job for the crew.
3. **Blame is built in.** Every failure is visible and traceable to a station, a pick or a person.
4. **No aiming skill needed.** The horde is dense; rough aim always hits something.

## Players and view
- 2–8 players, online co-op. Design and tune for 2–4 first; raise the cap once the core works.
- The train grows with the lobby (about one extra carriage per player pair) so there are always more
  jobs than players.
- First-person.
- Host-authoritative networking, **player-hosted** (user, 2026-11-02): one player's game is the server;
  no cloud or dedicated servers. Later, Steam lobbies and Steam's relay handle invites and NAT.
  If the host leaves, the session ends (saves at main stations soften this; no host migration).

## Art
- Goofy 3D: chunky, wobbly crew that ragdolls when hit.
- Simple round cute-creepy creatures with variety in the style of Vampire Survivors, made as our own
  creature set (not its gothic look). Variants come from size, colour and one silly trait.
- Stylized, flat colours, low-poly, so hundreds of enemies stay cheap to render.
- No furry/anthro framing.

## Structure
- **Run:** 4–6 levels, about 45–60 min, saved at each main station. A failed run returns to the depot;
  only unlocks are kept.
- **Level (stretch):** about 8–12 min of track from one main station to the next.
- **Goal:** reach the next main station alive. No quota and no fuel clock.
- **Fail:** the train is overrun or destroyed.
- **Pressure to move:** the horde spawns continuously; a stopped train piles it up. Stopping is always a
  choice, and it always has a cost.
- **Halts:** optional stops within a stretch. They give loot at the risk of jumping out while the horde
  closes in. Whether to stop is the captain's call.
- **Main stations:** safe, about 30–60 s. Repair, buy carriages with halt loot, choose the next line,
  let friends join, save.
- **Route:** a branching map between stations (gem-rich line, safe line, shop, boss tunnel), plus live
  switch levers at junctions within a stretch. No open world.
- **Final station:** the boss.

## The train
- Moves on rails. **Speed is set by the furnace only** (user, 2026-11-02): coal level = speed; no
  throttle lever in the prototype. A captain's brake for halts comes later.
- **Damage: HP per carriage** (user, 2026-11-02). A broken carriage loses its mounts until repaired;
  the engine at 0 HP = run lost.
- **Furnace:** the one universal chore. It sets speed (it never runs out or ends the run) and burns
  anything, including enemy corpses. If it is neglected, the train slows and the horde boards.
- **Carriages give mounts** (the weapon slots). Start: engine plus 2 carriages, 3 mounts. Buy
  carriages at stations to grow to about 6–8 mounts.
- **Parts** (the passive items) sit in engine slots, up to about 6.
- The build carries over between levels within a run.

## Skill system (the Vampire Survivors framework, translated)
- **Shared XP:** gems the train pulls in as it passes fill one team bar. There is one shared train build.
- **Nobody leaves the train to collect gems** (user, 2026-11-02). XP pickup is a crew job done from the deck.
- **EXPERIMENTAL: the gem net** (user, 2026-11-02; `--no-net` turns it off to compare). The problem it
  solves: on a train nobody steers, so VS's "where do I stand to pick up gems" has to become a crew job
  on board. A net post stands at the back of the last car. One crew member mans it (E), aims to sweep
  the net's mouth over the ground (3-14 m out), and holds click to reel it in. Only a landed catch pays
  XP. Leaving the post or going down spills the catch back on the ground. The net also tangles small
  creatures (by-catch): they land on the deck with the gems, so a greedy sweep brings boarders. The
  passive 6 m pull stays. Placement (last car) and by-catch were proposed by Claude, and the user said
  "add it as experimental". Numbers are ASSUMED: capacity 40 (gem 1, skitter 3), mouth radius 2.2 m,
  reel 0.8 s + 0.06 s per load (a full net takes about 3 s). Later idea, not built: the magnet part
  becomes a wider net, and its evolution reels in by itself.
- **Level-up:** the **captain** picks 1 of 3 cards. The game does **not** pause; the captain picks
  while playing, and the crew sees the cards and shouts advice.
- **Card types:** a new weapon on a free mount, +1 level to an existing weapon, or a part.
- **Weapon levels:** up to 8.
- **Evolutions:** 1:1, as in Vampire Survivors. A weapon at level 8 plus its partner part offers the
  evolved weapon as a card.
- **Limited mounts and part slots** force choices. One greedy pick can block another evolution.
- **Every weapon fires on its own but brings its own chore** (it jams, needs ammo, cranking, a valve,
  untangling...). Picking a card means picking a job for the crew.
- **Evolutions ease or swap chores.** An evolved weapon can drop its chore (a reward of relief), or swap
  it for a bigger, funnier one.
- **Manual turrets** can be offered as cards: a player fires them, with rough aim (big spread, shotgun,
  soft auto-aim). This is the light shooter layer.

## Captain's hat
- Whoever wears the hat is captain: they make level-up picks and decide halts.
- The host starts with it.
- It can be **stolen**: grab it off the captain's head.
- It can be **lost**: enemies knock it off, and it can fly out of the train.
- Possible grab cooldown (about 10 s) if playtests show endless stealing.

## Crew actions
- **Chores are physical** (user, 2026-11-02): pick up coal, ammo and corpses, carry them, drop them
  in; jams and repairs are a short hold-interact.
- **Crew health (prototype, user, 2026-11-02):** at 0 HP you are knocked down; a friend revives you
  with a hold-interact. Falling off the train respawns you on board after a few seconds.
- Run between stations and keep the train's chores going (furnace, weapon chores).
- Fire manual turrets.
- Haul corpses and loot to the furnace.
- Jump out at halts for loot, then get back on before the captain leaves.
- Steal or protect the captain's hat.

## Economy (one of each, no overlap)
- **Level-ups** give weapons, weapon levels and parts.
- **Halt loot** buys carriages and repairs at main stations.

## Open questions
- Weapon, part and evolution list, and each weapon's chore.
- Setting and world: where the line runs and why there is a horde.
- Crew health beyond the prototype rule (knockdown + revive): permanent deaths? penalties?
- Exact scaling of carriages, enemies and XP with 2–8 players.
- Hat grab cooldown: needed or not.
- Price (cheap hits sit at about $5–8; an assumption to check).

## Smallest prototype (proposal)
Grey boxes, 2–4 players: one train with 3 mounts, furnace, 4 weapons with chores, 4 parts with
evolutions, captain's hat, one creature type, one stretch from station to station.

Playtest questions: Are players who are not captain busy and laughing? Does the captain's greed create
blame? Does anyone ask for one more run?

## Rules invented while building the prototype (ASSUMED (AFK, 2026-11-02))
Each line is a guess made so the prototype could run. Confirm or reject; numbers live in
`sim/tuning.gd`, content in `data/` (see `docs/placeholders.md`).

**Train and furnace**
- ASSUMED (AFK, 2026-11-02): furnace holds 0-100 coal and burns 1.5/s; a coal lump adds 16, a corpse 10.
  Speed = 16 m/s x (coal/100)^0.7, eased at 2 m/s². Empty furnace = the train stops.
- ASSUMED (AFK, 2026-11-02): the coal bin on the engine holds 6 lumps and refills 1 every 3.5 s, so
  corpses matter as fuel when the bin runs dry.
- ASSUMED (AFK, 2026-11-02): the furnace burns anything: ammo crates (8, with a bang), loot (6),
  even the captain's hat (2; the hat is lost and a spare comes in 12 s). The feed says who did it.
- ASSUMED (AFK, 2026-11-02): engine 500 HP, cars 300 HP. Hold E at a car's red toolbox to repair it
  (45 HP/s, free). A fast engine (>5 m/s) plows creatures on the track and takes 0.3 damage each.
- ASSUMED (AFK, 2026-11-02): car types: flatbed (1 roof mount, fires all round) and gun wagon
  (2 side mounts, each fires only to its own side). Start: engine + flatbed + gun wagon (3 mounts);
  each extra pair of players adds a flatbed.
- ASSUMED (AFK, 2026-11-02): only so many creatures fit on a car: 8 can cling to its sides, 5 can
  be on its deck. The rest jostle on the ground. Without the cap the deck filled with hundreds.

**Build**
- ASSUMED (AFK, 2026-11-02): the train starts with one Rattle Gun on mount 1.
- ASSUMED (AFK, 2026-11-02): a new-weapon card goes on the first free mount (the card says which).
- ASSUMED (AFK, 2026-11-02): parts level 1-5; 6 part slots. One copy of each weapon.
- ASSUMED (AFK, 2026-11-02): XP to next level = 5 + 4 x level + level²/10. Kills on the deck pay XP straight
  into the bar; kills on the ground drop gems the train pulls in within 6 m.
- ASSUMED (AFK, 2026-11-02): when nothing is left to offer, filler cards: Coal Rush (full furnace),
  Duct Tape (+40% HP to all cars), Lucky Gem (half a level).

**Crew**
- ASSUMED (AFK, 2026-11-02): left click with empty hands = shove (hurts and knocks creatures, flings
  boarders off the deck). It also shoves crewmates, and shoving the captain knocks the hat off 50% of the time.
- ASSUMED (AFK, 2026-11-02): left click while carrying = throw. A thrown item that lands in a
  receiver (furnace, a gun's hopper, the strongbox) counts as handed in.
- ASSUMED (AFK, 2026-11-02): crew HP 100, regen 3/s after 5 s unhurt. Revive = 2 s hold to 50 HP.
  Nobody comes: you get up alone after 25 s (so solo play works).
- ASSUMED (AFK, 2026-11-02): more than 18 m off the train = fell off: you drop what you carry and
  are back on the engine after 3 s.

**Captain's hat**
- ASSUMED (AFK, 2026-11-02): grab cooldown 3 s after any change of hands.
- ASSUMED (AFK, 2026-11-02): a creature hit knocks the hat off by chance (skitter 20%, bruiser 100%);
  a downed captain drops it. A hat 70 m behind the train is lost; a spare appears on the engine's
  hook after 12 s. While nobody wears it, level-ups queue up unpicked.
- ASSUMED (AFK, 2026-11-02): only the captain can pull the brake and spend loot at stations.

**Horde**
- ASSUMED (AFK, 2026-11-02): spawn rate 1.0/s + 0.3/s per minute, x(1 + 0.35 per extra player),
  x1.6 while the train is stopped, x the line's horde factor. A surge of 22+ from one side every 70 s.
  Bruisers from 75 s. Creatures gain +100% HP per 10 min. The ramp restarts each stretch, but every
  finished stretch starts it 3 minutes further in.

**Route (layers on top of the stretch)**
- ASSUMED (AFK, 2026-11-02): halts are platforms with 5 loot crates. The captain pulls the brake
  lever (engine, right side) to stop; crew jump out, carry crates back and bank them in the
  strongbox (car 1). Crates left behind are lost.
- ASSUMED (AFK, 2026-11-02): one junction per stretch at half way. Anyone flips the lever (engine,
  left side): LEFT = 15% shorter, horde x1.4; RIGHT = 8% longer, horde x0.85.
- ASSUMED (AFK, 2026-11-02): main stations: safe, 60 s then the train leaves on its own. The captain
  spends loot: repair every car 2, flatbed 3, gun wagon 5 (+2 per car bought, max 7 cars), and
  picks the next line from 2 of 4 (Quiet, Gem, Market, Express). The Market Line ends at a market
  station: carriages 2 loot cheaper (the design's "shop"). The run is saved here.
- ASSUMED (AFK, 2026-11-02): a run is 4 stretches; the last ends at the Terminus, where the train
  stops and The Maw (boss) attacks with the horde. Kill it to win.
- ASSUMED (AFK, 2026-11-02): friends can join at any time (not only at stations); they appear on the engine.
