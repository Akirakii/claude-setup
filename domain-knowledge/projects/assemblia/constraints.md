# Constraints and open questions (Assemblia, 2026-10-31)

The rules for the next version of the game, and the questions they leave open.
**Solid** = fixed by the user. **Not solid** = open to change. Tags in the not-solid part:
**[user]** = you said it; **[earlier]** = from an earlier session or memory;
**[proposed]** = my suggestion, not agreed yet.

## Where we are (2026-10-31)
- **Playtest verdict:** the pet game is too easy, gives no decisions, can't be read on screen and
  has too much micromanagement. Moving to a new direction.
- **Explored and dropped:**
  - small pack cap (user: no cap)
  - incremental game (no strategy)
  - "look sets a priority" as the verb (patches automation flaws)
- **Current core:**
  - an auto-battling robot army with logistics and processing
  - the player writes the army's arrangement rules, so the army organizes itself (emergent, Game of Life–like)
  - the player claims things in the world (hack, salvage)
- **Camera decided:** top-down, rendered in 3D.
- **Name decided:** the game is **Assemblia**. The player's robots are called **Automates**
  (automata + mates): hacked or built machines that become your companions.
- **The pet game is archived as failed** (see POSTMORTEM.md in the dungeon-pets repo); this repo is the new game.
- **Story (agreed 2026-10-31):** a robot rebel inside a robot empire; roguelike, one run = the
  whole story; final boss = the rule-maker.
  - **Structure:** FTL-style, with a fixed premise and finale and a varied route, plus a thin
    story across runs (a Hades-style hub).
  - **Our angle vs Cogmind:** the army and its player-made rules.
  - **Roles:** start with 3: gather, carry, fight.
  - **Tone:** darker, which also changes the art.
- **MVP sandbox (2026-10-31, not yet playtested):** `scenes/mvp.tscn`, 2D circles, a hero you
  walk, a fixed 20 robots of one type, rushers vs turrets.
- **Rule system removed from the code (user, 2026-10-31):** the rules are not designed yet. The
  idea stays open (not rejected); robots run one fixed placeholder behaviour.
- **Gathering test built (2026-11-01, not yet playtested):** `scenes/gather.tscn`, picked from the
  playtest menu (`scenes/menu.tscn`). Fight-vs-haul with one robot type; see docs/research.md.
- **Three-roles test built (2026-11-01, not yet playtested):** `scenes/roles.tscn`: fighter, hauler
  and builder bots; the hero holds the scrap (no storage bot, user). **Under test (user):** building
  is on demand through an RTS-style queue: D-pad / 1-4 queues one bot of a type. The hero builds
  (at half speed while building); builders only add parallel capacity. This is a priority
  setting, so the playtest decides it, like attack-move.
- **Processing test built (2026-11-01, not yet playtested):** `scenes/process.tscn`, adds processor
  bots that run a recipe (any inputs → outputs; for now 2 scrap → 1 processed). Fighters and
  builders cost processed scrap; haulers and processors cost raw scrap.
- **Baseline + Links tests (2026-11-01, not yet playtested):** the old tests were merged into
  `scenes/baseline.tscn` (every mechanic on main, endless world, no rules). A Links test (the
  army as a tree rooted at the hero, auto-built) was made and removed (user, 2026-11-01). The universal Game of Life–style rules were tried and
  dropped (user: "no strategic value").
- **Direction set (user, 2026-11-01):** a mobile factory that has to keep moving to progress
  and fight bosses (see the solid constraints). Planted outposts (my earlier proposal) are out.
- **Layout without settling (user, 2026-11-01):** layout is wanted. **Walking machine test**
  (replaced the rotating grid test, not yet playtested): the hero is a machine with a fixed,
  non-rotating grid that grows by buying tiles; **blocks** (processor, builder) sit on tiles,
  **units** (fighter, hauler) walk off it. No-editor options are in docs/research.md.
- **Next:** design what forces movement (bosses, depleting scrap, pressure on idling).

## Solid constraints (fixed by the user)
- **A mobile factory (user, 2026-11-01).** A factory-plus-defense game in the spirit of Mindustry,
  but you never settle: the factory (the robot tree) travels with you. No bases, no planted
  outposts.
- **Progress means moving (user, 2026-11-01).** You advance through the world with your factory
  to progress and defeat bosses.
- **Idling loses (user, 2026-11-01).** Staying in one place leads to defeat; standing still is
  never a safe strategy.
- **Army auto battler.** An army walks with you and fights on its own, with no Pikmin-style orders.
  **Under test (user, 2026-10-31):** an attack-move order (right-click / right stick + RT) is in
  the MVP as an experiment; the playtest decides whether this constraint stays.
  Making this fun is the main goal.
- **Top-down view with 3D rendering** (decided 2026-10-31; replaces first person). Emergent
  patterns, a large army and logistics read from above. The hero stays on screen, with the army
  flowing around it.
- **No building.** Nothing is placed in the 3D world. **Under test (user, 2026-11-01):** a grid
  editor on the hero's walking machine (`scenes/machine.tscn`); the playtest decides
  whether "no grid editor" stays.
- **No cap.** The army can grow large.
- **Player is not strong.** The player's own action can't win a fight.
- **No micromanagement.** Nothing is handled one unit at a time: no per-unit feeding, equipping
  or orders.
- **Auto organization.** The army arranges and manages itself (also under test by the attack-move
  experiment). **No priority systems:** if the army
  needs a priority from the player, the automation has a flaw, and the priority only covers it up.

## Not solid (open to change)

### Strategy
- **Logistics and processing, not just damage.** Units make, carry, process, protect and attack.
  The army works like a factory, not a pile of stats. [user]
- **You can see the strategy working.** Resources visibly flow between units, so you see why a
  fight is being won or lost, not just numbers and hitting. [user]
- **Units join into something bigger,** more than stats adding up or units merging. [user]
- **Careful play is rewarded and careless play is punished.** A choice with one obvious answer
  doesn't count. [earlier]
- **Fair failure.** A loss can be traced back to a choice the player made. [earlier]

### Clarity and controls
- **The screen stays readable** even with a big army. [user, playtest]
- **Gamepad-first** (Switch-compatible). Every action needs a controller mapping. [earlier, memory]

### Player ideas (2026-10-31)
- **Units are crafted.** [user idea]
- **The player connects robots, input to output.** [user idea]
- **The player creates the arrangement system:** local rules that make the army organize itself,
  emergent like the Game of Life (far reference), with room for personal style. [user idea]
- **Proposed link rule:** links are made between **types**, not individual units ("Smelters
  feed Gunners"), so a new robot joins its chain on its own (no micromanagement). A link is
  written as a rule card ("when carrying ore → bring it to the nearest Smelter"), not drawn in
  the world. [proposed]
- **Proposed growth limit:** robots are crafted from what the army processes, so production speed,
  not a cap, limits army size. [proposed]

### Story (user idea, 2026-10-31)
- **Robots rule the world** as a colonial, imperial power; the hero is a rebel robot who wants to
  bring the system down. [user idea]
- **Recruit or salvage:** hack imperial robots to recruit them, or kill them for scrap to build your
  own (gathering, defense, attack, exploring, research, logistics). [user idea]
- **Roguelike, one run = the whole story.** Start with nothing but one small companion bot; the end
  goal is the final boss who controls everything. [user idea]

### Process
- **Break conventions where it helps.** [user]
- **Robots are mechanical, not just a theme:** they are what gives the army logistics. [user]

## Open questions
Answered and removed (2026-10-31): run structure (FTL-style roguelike with a thin Hades-style
hub), the creatures (gone; the army is robots), and the player's verb (hack or salvage).

### Rule-card prototype
- **When can rules be edited?** Between waves only, in the MVP (proposal in research.md). [proposed]
- **How do robots get made?** Proposed: the hero assembles them from hauled scrap. Deferred:
  the MVP uses a fixed army. [proposed]

### Attention: the core question
**What does the army need from you, so that what you see from above is what you act on?**
- **Demand:** what pulls the hero to another part of the map? What happens away from the hero
  (at the army's edge, or off-screen), and how often? (Too rare and walking there is a chore; too
  often and it's chaos.)
- **Cost of not being there:** what goes wrong in the part of the army the hero isn't near?
  Does it fail slowly (a supply line thins) or quickly (a breach)?
- **Signals:** how do you learn about something off-screen? (Edge-of-screen markers, sound, the
  army's own reactions.)
- **Where you stand:** with the camera on the hero, what does your position change? Terrain the
  army flows through, what is on screen, what the army forms around.
- **The army vs the hero:** with no cap, the army can cover the hero and the threats around it.
  How does the hero stay visible inside its own army?
- **Enemies and your position:** do enemies play on where you are (flanks, attacks on the far
  end of a supply line, baiting the hero away)?
- **Skill:** what does a skilled player do differently? (A guess: they walk to where the army
  will need them before it does.)
- **Logistics in view:** can you see a supply chain working, or failing, on one screen?
- **Hack/salvage in motion:** the verb is decided; how does it work without menus or pausing,
  and does it decide fights without dealing damage?

### The hardest one: the triangle
- **Where does the player's strategy come from?** No building, no micromanagement and no direct
  orders remove the usual levers.
  - **Chosen direction:** the player's rules (rule cards), plus hack or salvage.
  - **Other candidates** [proposed]:
    - which robots join (what you hack, what you salvage)
    - where you walk (the army arranges itself around your path or the terrain)
    - when and where to fight
  - **Open:** is that enough decision per minute, or does the game "play itself" (FF12's critique)?

### What 3D rendering adds from above
- **Proposed picks** (what still applies after the move to top-down) [proposed]:
  - **Core:**
    - your position is the command (the army forms around you and goes where you go)
    - a vulnerable player (dodging is the action)
    - terrain that shapes the army's flow
  - **Readability:**
    - motion and light show the logistics working (glowing lines, carriers, firing)
  - **Payoff:**
    - scale and cinematic moments (camera height, lighting)
  - **Maybe:**
    - line of sight and cover (walls that block fire, not the camera)
  - **Dropped:**
    - limited view and scouting (first-person ideas)
    - layers and tunnels (pathing risk)
    - physics and volume (cost, clutter)
    - precise aiming as selection (precision)

### Clarity
- **How do we avoid visual clutter with an uncapped army seen from above?**
- **How does a player tell robot roles apart at a glance?** Silhouette, colour, motion?
- **How does the camera handle a big army?** Fixed height, or zoom out as the army grows?

### Scale and balance
- **What limits army size, if not a cap?** Upkeep, supply, logistics itself (an army only
  grows as far as it can be supplied)?
- **How many units can the engine run?** Performance target?
- **How do we stop a big army from making the player win without deciding?** That was the playtest problem.

### Logistics
- **What flows, and what is processed?** Resources, ammo, power, scrap, repairs?
- **How do units join?** By being near each other, in chains, or into fixed formations?
- **What happens when a supply line breaks** (a carrier dies, a link is cut)?

### The player
- **Is hack, salvage and walking enough for moment-to-moment play,** for a hero that is weak
  and gives no orders?

### Enemies and runs
- **What do enemies attack,** the army, its supply lines, or the player?
- **What makes floors differ** so that no single army plan always works?
- **What does losing cost?** (Death is a story beat at the hub; what carries over is open.)

### Project
- **What existing code and art carry over from Dungeon Pets** (threats, reactions, the Meshy
  pipeline)?
