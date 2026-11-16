# Constraints and open questions (new direction, 2026-10-31)

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
- **The pet game is archived as failed** (see POSTMORTEM.md); the new game is **Assemblia** (`~/Playground/assemblia`, repo Akirakii/assemblia).
- **Story (agreed 2026-10-31):** a robot rebel inside a robot empire; roguelike, one run = the
  whole story; final boss = the rule-maker.
  - **Structure:** FTL-style, with a fixed premise and finale and a varied route, plus a thin
    story across runs (a Hades-style hub).
  - **Our angle vs Cogmind:** the army and its player-made rules.
  - **Roles:** start with 3: gather, carry, fight.
  - **Tone:** darker, which also changes the art.
- **Next:** sketch the rule cards (proposal in research.md).

## Solid constraints (fixed by the user)
- **Army auto battler.** An army walks with you and fights on its own, with no Pikmin-style orders.
  Making this fun is the main goal.
- **Top-down view with 3D rendering** (decided 2026-10-31; replaces first person). Emergent
  patterns, a large army and logistics read from above. The hero stays on screen, with the army
  flowing around it.
- **No building.** Nothing is placed in the 3D world, and there is no grid editor.
- **No cap.** The army can grow large.
- **Player is not strong.** The player's own action can't win a fight.
- **No micromanagement.** Nothing is handled one unit at a time: no per-unit feeding, equipping
  or orders.
- **Auto organization.** The army arranges and manages itself. **No priority systems:** if the army
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
  feed Gunners"), so a new robot joins its chain on its own (no micromanagement).
  You make a link in first person by aiming at one robot, holding a button and pulling a cable
  to another. [proposed]
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

### Attention: the core question
**What does the army need from your attention, so that what you see is what you act on?**
- **The verb:** what does acting on what you see *do*? One look, one button: does it spot, feed,
  link, rally, repair or protect? Is it one verb or several?
- **Demand:** what makes you turn? What happens off-screen that pulls your attention, and how
  often? (Too rare and turning is a chore; too often and it's chaos.)
- **Cost of not looking:** what goes wrong in the part of the world you aren't watching? Does it
  fail slowly (starving) or quickly (a breach)?
- **Signals:** how do you learn something needs you before you see it? (Sound, light at the edge
  of the screen, the army's own reactions.)
- **Where you stand:** what does your position change about what you can see? Does high ground
  pay, does cover blind you?
- **The army vs your view:** with no cap, the army fills your view. How does it stay something
  to look *through*, not a wall in front of you?
- **Enemies and your view:** do enemies use your attention against you (feints, flanks, hiding
  behind your own army)?
- **Skill:** what does a skilled player do differently with the same view? (In shooters: they
  look at the right place before the threat appears.)
- **Logistics in view:** can you see a supply chain working, or failing, within one 90° glance?


### The hardest one: the triangle
- **Where does the player's strategy come from?** No building, no micromanagement and no direct orders
  remove the usual levers. What is left?
  - Candidates [proposed]:
    - which units join
    - where you walk (the army arranges itself around your path or the terrain)
    - army-wide policies (rules, not orders)
    - what you feed into the army
    - when and where to fight

### Why 3D at all?
- **2D is back on the table** (user, unsure). Emergent patterns read best from above. [user]
- **User goal for 3D:** an action feel, without 2D's precision, heavy building or micromanagement. [user]
- **Proposed picks** (from the "what 3D brings" list):
  - **Core:**
    - your position is the command (the army forms around you and goes where you go)
    - a vulnerable player (dodging is the action)
    - terrain that shapes the army's flow
  - **Readability:**
    - motion and light show the logistics working (glowing lines, carriers, firing)
  - **Payoff:**
    - scale and cinematic moments
    - companions beside you, and losses that happen close to you
  - **Maybe:**
    - line of sight and cover
    - surprise
  - **Dropped:**
    - limited view, scouting and checking behind you (slow and careful, and the army gets lost behind you)
    - layers and tunnels (pathing risk)
    - physics and volume (cost, clutter)
    - precise aiming as selection (precision)
  - [proposed]

### Clarity
- **How do we avoid visual clutter with an uncapped army in first person?**
- **How does the logistics show in first person,** when you can only see what's in front of you?
- **How does a player tell unit roles apart at a glance?** Silhouette, colour, motion?

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
- **What does the player do moment to moment,** if they're weak and give no orders?
- **What does the player's body or tool do,** if it isn't a weapon?

### Enemies and runs
- **What do enemies attack,** the army, its supply lines, or the player?
- **What makes floors differ** so that no single army plan always works?
- **Run structure:** roguelike runs, an incremental/prestige layer, or both?
- **What does losing cost?**

### Project
- **What existing code and art carry over** (first-person player, threats, reactions, Meshy pipeline)?
- **Do the creatures go entirely, or do they become part of the robot army?**
