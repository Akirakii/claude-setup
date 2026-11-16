# Dungeon Pets: Design Brief

A first-person, infinite dungeon crawler where a pack of creatures fights for you.
This brief covers rules and balance only. It is engine-agnostic and comes from a playtested prototype.
All numbers are starting values to tune, not fixed requirements.

Units: 1 tile = 1 world unit. Speeds are in tiles/sec, cooldowns (`cd`) in seconds, and ranges in tiles.

## Design rules

### Rule 1: thinking pays, not thinking fails (applies to every concept)

Every mechanic must reward the player who thinks about it and cost the player who doesn't. A
feature isn't designed until it answers these 4 questions:

1. **What does a careless player do?** (the default, the autopilot, "take everything")
2. **What does that cost them, and when?** The cost has to be real and bite at a known point (a
   floor, a boss, a threat), not "slightly worse numbers".
3. **What does a careful player do differently?** That needs information available *before* they
   commit: shown on the map, the pack screen, at the portal, or in the codex.
4. **What do they gain?** It has to be big and visible: new behaviour, or ×1.5 or more, not +10%.

And it has to pass these checks:
- **No free default.** If one option is fine everywhere, the choice is fake. Give each option a cost
  (Guard costs damage; feeding treats costs hunger; a bigger pack costs upkeep).
- **Soft, not hard, punishment.** The careless choice is slow and costly, never instantly fatal, and
  there are at least 2 ways to answer each test. A wall you couldn't prepare for is luck, not skill.
- **Readable failure.** When the cost bites, the game says what caused it and what would have answered it.
- **Measured.** Where the bot can play both ways (careless vs careful), the careful version must
  clearly win: a gap of several floors, not a few percent.
- **No formula.** The best answer depends on the situation (this floor's threats, these offers),
  so careful play is judgment, not a memorized recipe. One answer that's always right is a solved
  puzzle, and the choice dies.
- **The best path is the fun path.** Players will "optimize the fun out" of a game: if a boring
  method (grinding, waiting for regen, taking everything) is the most efficient, they'll use it.
  Make the boring method weak, not just discouraged.
- **Don't make everything a decision.** A choice that rarely changes the outcome, or that always
  resolves the same way, is friction: automate it (auto-feed for hunger is fine; the decisions live in
  treats and who grows). Too many options at once cause analysis paralysis.

How the existing concepts answer the 4 questions:

| Concept | Careless | Cost | Careful | Gain |
|---|---|---|---|---|
| Food | auto-feeds everything, hand-feeds no one | starving and run-aways when food runs out mid-floor | rations, decides who grows, keeps a reserve for revives | survives famine floors, grows chosen creatures |
| Evolution diet | throws any treat | random path that fits nothing | feeds the flavor that fits the pack's plan | a path ability that completes a combo |
| Stance | leaves it on Guard | slower fights, more hunger, more hits overall | Aggressive on trash, Guard on bosses, Sneak past rooms | faster floors, less damage where it matters |
| Composition | takes every creature | upkeep, no combos, fails the floor's checks | picks for combos and answers | see Rule 2 |

### Rule 2: composition must matter (Rule 1 applied to the pack)

A player who builds the pack carefully should go much deeper than one who takes whatever comes. Every
feature that touches the pack (recruiting, eggs, evolution, traits, relics, enemies, floors) is checked
against these six parts. Why, and the research: `docs/research.md`, "Rewarding careful composition".

1. **Checks.** From floor 3, floors bring threats that a pack without an answer handles badly:
   armored, flying, healing or regenerating, swarms, burst bosses. Each threat has **at least 2
   answers** (for example, armored: earth, stun or poison), and a missing answer makes a fight slow and
   costly, never impossible (soft counters, not walls).
2. **Synergy pays big, raw numbers pay little.** A combo (one creature sets a status, another pays it
   off) or a trait breakpoint gives a big, visible effect: new behaviour, or ×1.5 or more. One more
   off-plan creature adds only its own stats. Flat +10% bonuses don't count as synergy rewards.
3. **Carelessness costs.** Every creature eats, and pack upkeep rises with pack size, so a creature
   that fits no combo still costs full upkeep. Taking everyone dilutes the pack, like a bloated deck.
4. **Thinking needs information.** Every check is visible before it bites: the next floor's threats
   at the portal, enemy types on the scouted map, weaknesses in the codex, and combos on the pack
   screen and the egg pick. If the player couldn't have known, it's luck, not a test.
5. **Failure names its cause.** A death recap says what beat you and what would have answered it
   (for example, "Armored Golems: nothing in your pack hits armor").
6. **Enough choice to aim.** Offers are random but plentiful: about 6 or more picks (eggs, 1 of 3)
   by floor 5, so a careful player can steer toward a plan and a bad roll isn't the end of the run.

**Target, checked by the bot:** a pack picked at random stalls around floor 5. A pack picked for
combos and answers goes at least 3 floors deeper. If the gap is smaller, the checks or payoffs are
too weak; if the random pack dies on floor 2–3, they're too harsh.

## Core loop

- The player explores floor after floor. Each floor is a set of rooms connected by corridors.
  A boss guards the exit portal. Floors never run out.
- The player starts each run with **3 random creatures** (distinct species, rarity 1–2, Lv 1).
- Creatures **follow** the player, **roam** near the player while the player stands still, and **fight on their own**.
- New creatures come from **eggs** (egg carriers, chests, the boss chest): hatch one for 3 food and pick 1 of 3 species.
- **No pack cap: every recruit fights.** There is no bench. Food is the limit on pack size: each
  creature drains hunger, so a big pack costs more to keep fed.
- Creatures **need food**, and food management is the main pressure of a run.
- A run ends when the player dies. The pack never ends a run on its own.

## The player

- HP is 100 on floor 1 and +10 per floor (was 130 / +15: the player should be vulnerable). Descending
  heals 30% of max HP. Out of combat, the player regenerates 0.6% of max HP per second (was 1.2%).
- Base speed is 3.6, and running is ×1.35.
- **Movement** is Quake-style: ground acceleration and friction, jumping, and air strafing.
  Chaining jumps on landing keeps speed and air strafing adds to it (bunny hopping), so skilled
  players can move well above run speed.
- **Sword:** damage 9 + 2.5 × (floor − 1). Cooldown 0.45s. Reach 2.0 in a forward arc of about ±43°.
  Other weapons: axe 2.1, hammer 2.0, dagger 1.6, spear 2.8. The hit lands on the press, and the
  viewmodel thrusts forward by an amount set by the reach.
- **Carrying** a creature: it is held in the world at full size, straight ahead of the player,
  upright, keeping the facing it had when picked up (relative to the player), with its top 0.3 below eye level (it blocks the lower part of the
  view). Only the player's yaw turns it; looking up or down doesn't move it. Near a wall it is held
  closer, but never nearer than 0.45 + its radius. Set down and thrown from where it is held.
  The sword is put away until the creature is set down or thrown.
  - **Throw:** hold LMB to charge, release to throw. A tap is a short toss (20% power); full power
    after 0.8 s. While charging, the creature is drawn back up to 0.3 toward the player.
  - **Still fights:** a held creature attacks the nearest enemy in its own reach (the Sic 'em focus
    first) without moving, and a healer heals allies in range. It can be hit while held.
- **Feeding by throwing (no menu):** the player holds one throwable: food, one of the 4 flavor
  treats, or an elixir. **C** (gamepad **L**) cycles to the next one the player has; empty ones are
  skipped (Pikmin-style). **1–6** pick one directly on keyboard. **RMB** (gamepad **R**) throws one at
  the pack creature aimed at (within 12 tiles, up to 6° off the crosshair, in sight). It has its own
  button so the sword never turns into a throw when the pack crosses the crosshair. At most one
  throw per 0.3 s.
  - The item flies in a parabola to the creature's mouth, ending wherever the mouth is by then, so a
    moving creature still catches it. The creature stops and faces the player until it arrives. Food
    eats like a hand-feed (+45 hunger, +3 bond); a treat or elixir works like gifting it. If the
    creature faints or leaves mid-flight, the item goes back to the pouch or inventory.
  - **Watching the treat:** while the player holds a treat whose flavor is one of a creature's 2
    favorites and its path isn't chosen yet (stage 1), the creature stops roaming and turns to
    watch the player (within 12 tiles, not while fighting or moving).
- **Combat sounds:** hits on enemies are low thuds and hits on the pack are higher yelps. They play
  as 3D sound with at most 3 copies of one sound at once.
- **Commands:**
  - *Sic 'em*: the whole pack focuses the enemy under the crosshair.
  - *Heel*: the pack drops its fights and regroups on the player for 2.5s.
  - *Potion*: heals the player and every conscious creature by 50%.
  - *Stance* (cycles, see Stances): Aggressive / Guard / Sneak.
- The player is a valid enemy target. Enemies prefer creatures, but only slightly: the player's distance counts ×1.3
  (was ×1.8) when they pick a target.

## Creatures

### Behaviour by role

| Role | Behaviour |
|---|---|
| melee | Closes in and bites. |
| tank | Melee. Taunts: enemies within 4 tiles treat its distance as ×0.25 when picking targets. The Crystal Jelly path taunts too. |
| ranged | Keeps distance (backs off inside 2.2 tiles), needs line of sight, fires projectiles. |
| healer | Heals the most-hurt ally under 72% HP (the player included) with a projectile. An `aoeHeal` healer pulses heal to all allies under 85% HP in range. |

- **Following:**
  - Turning the camera doesn't move the pack. It follows once the player has moved away from a
    creature for 1 s in total (moving toward it counts back down; standing still resets it), or
    once the player is beyond its roaming range (7 tiles, 4 for Loyal). Then it
    heads for its follow slot at the player's speed + 0.8 × its distance from the slot (at least
    sprint speed, at most 9.5), until the player has stopped and it is back within roaming range.
    Heel sends it to its slot at once.
  - Follow slots are behind the player: 2.2 tiles back from the walking direction (facing, when
    standing), on alternating sides (±25°, ±40°, ±55°, ±70° off straight back).
  - Only while the player and an aggro'd enemy within 10 tiles see each other (the enemy is in the
    player's view and nothing blocks the line between them) do the slots move in front: 2.6 tiles
    out, on alternating sides of the crosshair (±20°, ±32°, ±44°, ±56°), never on it.
  - While the player stands still, it roams to random visible spots 2.5–7 tiles away on any side
    (4 for the Loyal trait).
  - It sprints when more than 7 tiles behind.
- **Frontline:** while the player and an aggro'd enemy within 10 tiles see each other, the whole pack holds a
  line in front of the player toward the threat: melee and tank creatures about 2 tiles out, ranged creatures
  and healers about 1 tile out. Without mutual sight, the pack keeps following behind.
  Frontliners measure engage range from themselves or the player, whichever is closer, and go first for enemies attacking the player.
- **Combat speed:** creatures move 2× faster while getting to their combat-line spot in front of the player.
- **Catch-up:** a sprinting creature moves at least 1.1× the player's current speed, so the pack keeps up with a bunny-hopping player.
- **Targeting:**
  - Creatures engage aggro'd enemies within 7.5 tiles in line of sight. They engage idle enemies only within 4 tiles.
  - They never chase farther than 11 tiles (the leash) from the player.
  - Among foes in range they pick the nearest, but a foe **weak to their element** counts ×0.6 distance and
    one that **resists** it ×1.6, so each creature goes for what it's good against. Frontliners (and
    Devoted creatures) count foes attacking the player ×0.5. A foe carrying a status the creature's
    element **reacts with** counts ×0.5, and a creature ready to attack whose target can't react
    switches to a foe in reach that can, so setters and payoffs meet on one target (without this,
    reactions were rare: creatures kept their first target). Sic 'em overrides all of this.

### Species (level-1 stats)

| id | stage names | role | rarity | hp | atk | range | cd | speed | hunger | on-hit | extra |
|---|---|---|---|---|---|---|---|---|---|---|---|
| emberpup | Emberpup / Blazehound / Infernus | melee | 1 | 46 | 9 | 1.0 | 0.9 | 3.4 | 1.1 | burn | |
| mossback | Mossback / Grovetortle / Elderwood | tank | 1 | 90 | 5 | 1.0 | 1.2 | 2.4 | 1.3 | | armor 0.30 |
| sparkwisp | Sparkwisp / Voltwisp / Stormheart | ranged | 1 | 30 | 8 | 5.5 | 1.3 | 3.2 | 0.8 | chain | |
| bloomling | Bloomling / Petalmend / Verdance | healer | 2 | 36 | 4 | 5.0 | 1.6 | 2.9 | 0.9 | | heal 9 |
| gloomowl | Gloomowl / Duskhoot / Nightseer | ranged | 2 | 32 | 11 | 6.5 | 1.5 | 3.6 | 1.0 | | crit +0.25 |
| frostkit | Frostkit / Frostfang / Glacierlord | melee | 2 | 50 | 8 | 1.0 | 1.0 | 3.3 | 1.1 | slow | |
| venomoth | Venomoth / Toxwing / Plaguemoth | ranged | 2 | 30 | 5 | 5.0 | 1.1 | 3.8 | 0.9 | poison | |
| pebblit | Pebblit / Bouldron / Monolith | tank | 1 | 105 | 7 | 1.0 | 1.5 | 2.1 | 1.5 | stun | armor 0.35 |
| jellow | Jellow / Jellossus / Gelatitan | melee | 1 | 60 | 7 | 1.1 | 1.2 | 2.8 | 1.4 | splash | |
| shadekit | Shadekit / Umbracat / Voidpanther | melee | 3 | 40 | 13 | 1.0 | 0.75 | 4.2 | 1.2 | | crit +0.30 |
| sproutle | Sproutle / Fernguard / Mother Oak | healer | 3 | 55 | 5 | 4.5 | 2.4 | 2.6 | 1.0 | | heal 6, aoeHeal |
| cindermite | Cindermite / Magmite / Volcanox | ranged | 3 | 38 | 9 | 5.0 | 1.8 | 3.0 | 1.3 | blast | |

Looks are in the prototype's colours: emberpup is a fire pup, mossback a shell turtle, sparkwisp an electric orb,
bloomling a flower, gloomowl an owl, frostkit an ice fox, venomoth a moth, pebblit a rock,
jellow a jelly, shadekit a shadow cat, sproutle a tree, and cindermite a lava bug.
Every species has 3 visual stages, and each stage looks bigger and fancier than the last.

### Growth

- **Level = stage.** Lv 1, 2 and 3 are the three forms; there are no small levels in between. Each
  level past 3 is a **star** (shown Lv3★2): +8% HP, attack and healing, so the infinite dungeon keeps
  a reason to grow.
  - HP = base × stage multiplier × (1 + 0.08·stars); ATK and Heal the same way.
  - Stage multipliers: HP ×1 / 2.0 / 3.6, ATK ×1 / 1.8 / 3.0, Heal ×1 / 1.65 / 2.4 (about the old Lv 6 and
    Lv 12 totals, now arriving all at once).
- **XP to fill the bar:** Lv 1→2 350, Lv 2→3 1100, then 500 + 100 per star. Pacing goal: Lv 2 near
  floor 3, Lv 3 near floor 6, then a star about every 2 floors (first guesses; check with bot runs).
  - Kill XP is shared with every conscious creature within 15 tiles of the player.
  - The killer gets 100% of the XP; the others get 70%.
- **Evolution** is each level-up to Lv 2 and Lv 3. Evolving fully heals the creature.
  - Visual size: 1.33 tiles tall at every stage; evolution does not grow a creature (tanks are ×1.08), measured from the feet to the top of the skull; ears, antennae and crowns add on top, so big-eared species aren't shrunk. Creatures are anthro monster girls, so they stand near player height.
- A star also heals 30% of max HP.

### Growth, eating and evolution paths (approved redesign; paths and path abilities built, Growth not yet)

- **XP is renamed Growth.** Food is the main source of Growth; kills give only a little.
- **Food covers hunger and growth; health stays separate** (potions, petting, regen).
  - Plain rations: auto-feed uses them for hunger. Given by hand as a treat, they give some Growth.
  - **Four treat flavors**, each with one fixed meaning for every species:
    🍖 Meat = Fang (offense), 🪨 Rock candy = Guard (defense), 🌶️ Spice = Wild (element unleashed: area,
    spreading effects), 🍯 Honey = Kind (support).
  - **Soft preference:** every creature eats every food. Each species has **2 favorite flavors**, which give
    extra Growth and push its evolution form. The pack screen shows a creature's 2 favorites with a diet bar.
- **Two paths per species.** At Lv 2 the favorite flavor it ate more decides form A or B; stage 3 at Lv 3
  follows that branch. Later: perk picks (1 of 2) at milestone levels, which need no new art.
  - **Built:** the 4 flavor treats (Meat Chunk, Rock Candy, Fire Spice, Honeycomb) replace the old
    per-species treats. Each treat given counts toward the creature's diet. A tie at Lv 2 (or no
    favorite eaten) picks a path at random; a creature recruited at Lv 2+ gets a random path.
    The pack screen shows both favorites with their counts, what each path becomes, and the current
    leaning; after Lv 2 it shows the path taken. Same models for both paths (no visual change yet).
  - **Path abilities:** each path unlocks one behaviour at stage 2, ×1.5 stronger at stage 3 (the
    table below). They reuse existing hooks (on-hit effects, heals, taunt, armor), so no new art.

| Species | Path A | Path B |
|---|---|---|
| Emberpup | 🍖 Searing: burn deals 70% atk/s (×2) | 🌶️ Wildfire: hits also burn the nearest foe within 2 tiles (2 foes within 3 at stage 3) |
| Mossback | 🪨 Fortress: +0.15 armor, taunts from 6 tiles | 🍯 Grove warden: heals allies within 3 tiles 2% max HP/s |
| Sparkwisp | 🌶️ Tempest: chain hits 3 extra foes (4 at stage 3) | 🍖 Overload (payoff): its Electrocute and Conduct ×2 |
| Bloomling | 🍯 Bloom: heals become area heals | 🌶️ Thorn medic: attack ×1.8; 30% of its damage heals the most-hurt ally |
| Gloomowl | 🍖 Night sniper: +40% crit on the Sic 'em target, +15% on others | 🍯 Dream seer: hits hex foes for 4s (+20% damage taken) |
| Frostkit | 🍖 Deep freeze (payoff): its Freeze lasts 3 s instead of 2 (3.5 s at stage 3) | 🪨 Glacier guard: +0.15 armor; attackers are slowed 2s |
| Venomoth | 🌶️ Plague cloud: poison spreads to foes within 1.5 tiles | 🍯 Pollen: 40% of its damage heals the most-hurt ally |
| Pebblit | 🪨 Monolith: stun chance 60%, +0.1 armor | 🍖 Rockslide (payoff): its Shatter ×2 (bonus damage +100% instead of +50%) |
| Jellow | 🌶️ Tidal: splash radius 2.2, 75% damage | 🪨 Crystal jelly: +0.25 armor and taunts |
| Shadekit | 🍖 Assassin: +60% damage on foes not targeting it | 🌶️ Phantom: each hit also strikes a second foe for 70% |
| Sproutle | 🍯 Mother Oak: heals ×1.5 | 🪨 Root warden: healed allies are warded 3s (−30% damage taken) |
| Cindermite | 🌶️ Volcano: blast radius 2.4, everything hit burns | 🪨 Obsidian cannon: attack ×1.6, cooldown ×1.4, +0.2 armor |

- **Payoff paths** (built 2026-10-31): the three Fang paths above that said only "more damage" now
  multiply the reactions the creature triggers by its **reaction power**: ×2 at stage 2, ×2.5 at
  stage 3. A damage reaction scales its bonus (Thermal Shock ×(1 + power), Shatter +50% × power,
  Execute's crit bonus × power, Ignite and Electrocute and Conduct damage × power); a control
  reaction lasts 1 + power seconds (Freeze, Overgrowth). With no setter in the pack, a payoff path
  does nothing extra: that's the cost of evolving without a plan. Flavor meanings stay fixed:
  🍖 Fang pays off, 🌶️ Wild spreads statuses.

Why (research and dialectic in `docs/research.md`): one resource with two uses makes each bite a choice;
a hard diet restriction would turn bad drops into starvation; fixed flavor meanings stay learnable
while the pairs keep species distinct.
- Base crit is 5%; a crit deals ×1.8 damage. Each hit's damage varies by ±15%.

### Traits (1 trait, or 2 with a 35% chance; Glutton and Dainty never appear together)

| Trait | Effect |
|---|---|
| Brave | +15% attack |
| Sturdy | +20% max HP |
| Swift | +20% move speed, attack cooldown ×0.85 |
| Glutton | Eats 60% more, +25% HP and attack |
| Dainty | Eats 40% less, −10% attack |
| Feisty | +25% attack, −10% HP |
| Lucky | +15% crit chance |
| Loyal | Stays closer to the player, +10% damage while within 4 tiles of the player |
| Hardy | Takes 15% less damage |
| Quick | +30% XP |

| Playful | Likes being thrown (bond +2 instead of −1), thrown hits ×1.3 |

**Shiny**: 5% of captives (12% in boss-room cages) are recolored and get +15% HP and attack.

### Bond

- Affection 0–100. Tiers: Wary < 25, Friendly, Close ≥ 60, Devoted ≥ 90. Starting creatures begin at
  40, recruits at 20.
- Gains: petting (up to 10 per floor), hand-feeding +3, gifts, level-ups +2, campfire rest +5.
  Losses: fainting −2, being thrown −1, starving −0.2/s, a resting creature with no food −10.
- Effects: Wary ignores Sic 'em half the time. Close: +10% damage and speed within 5 tiles of the
  player. Devoted: peels foes off the player, gets up 1.6× faster, holds out twice as long starving.

### Red health and petting

- 60% of each hit taken becomes **red health**: recoverable, fading after 4s untouched. Petting (hold
  E on a creature) turns it back into HP at 25% max HP/s.

### Knockback

- Every hit pushes the target away from the attacker: melee 4.4, the player's sword 7, ranged hits at 40%, and crits ×1.5.
  The target is also launched upward at half the push speed and falls back under gravity.
  The push is divided by the target's **mass**. Tanks and golems are heavy, bats and wisps light, and creatures get 25% heavier per stage.
- A pushed unit flies without friction while airborne, then slides and slows by 8 tiles/s² (push capped at 14).
  While it is airborne or moving faster than 1 tile/s it is **staggered** and can't steer.
- The player gets the push as movement velocity with a hop of 3 tiles/s, so big hits can launch you.

### On-hit effects

| Effect | Rule |
|---|---|
| burn | 3s damage over time at 35% of the attacker's atk per second |
| poison | 4s, stacks +25% atk/s, capped at 100% of atk/s |
| slow | 2s, target moves at ×0.55 (the player at ×0.65) |
| stun | 30% chance to stun for 0.8s |
| splash | Melee hit also deals 50% damage to foes within 1.4 tiles |
| blast | Ranged version of splash, radius 1.6 |
| chain | 60% damage arcs to the nearest second foe within 3.5 tiles |

## Elements

- Every species has one of 8 elements: fire (Emberpup, Cindermite), nature (Mossback, Bloomling,
  Sproutle), storm (Sparkwisp), shadow (Gloomowl, Shadekit), frost (Frostkit), toxic (Venomoth),
  earth (Pebblit), water (Jellow). Its attacks deal that element.
- Every enemy is **weak** to one element (×1.5) and **resists** one (×0.5), shown in the Enemies table.
  The first weak or resisted hit records it in the **codex**, which persists across runs; known
  weaknesses show on the enemy's intent line.
- **Combos** on a status already on the target: fire on a slowed foe = Thermal Shock (×1.5, ends
  the slow); earth on a burning foe = Shatter (stun 0.8s); storm on a poisoned foe = Conduct (arcs
  50% atk to 2 more foes).
- **Element gates** seal 1 optional dead-end room per floor (2 from floor 4, 3 from floor 7). Only a
  creature of the gate's element opens it (ask one standing near, or throw one at it). 60% of gates
  use an element the pack has.

## Reactions, threats, upkeep, eggs (built as a first playable pass, 2026-10-31)

**Built:** all 5 statuses (each element's attacks set its status), the 8 reactions, threat tags and
rules (armored, flying, regenerating; swarm and brute are tags only), champion threat affixes, the
upkeep curve with its HUD readout, eggs (carriers, chests, boss chest, hatch screen with the
guaranteed reaction option, merge, release), the pack screen's Reactions and "Threats with no answer"
lines, the death recap, and the careless and careful bot pickers (`--careful-bot`).
**Simplified:** threats are shown as text tags over enemies and a "Threats on this floor" message on
arrival; no portal preview or map icons yet. **Not built:** reactions in the codex, re-tuning path
abilities, and the bot measurement run. Element bonds are still on beside reactions.

This section applies Rules 1 and 2. It replaces element bonds as the main synergy and cages as the way
to recruit. Build order and risks are at the end. Research: `docs/research.md`, "Reactions and threats".

### Statuses (the shared language)

Each status is applied by one element's attacks and shown above the foe as an icon. A foe can carry
several.

| Status | Applied by | Effect alone |
|---|---|---|
| Burn | fire (Emberpup, Cindermite) | 35% atk/s for 3s; stops the foe healing |
| Chill | frost (Frostkit) | slowed to ×0.55 for 2s |
| Poison | toxic (Venomoth) | stacking damage over 4s; ignores armor |
| Soak | water (Jellow) | 4s; puts out Burn and blocks new Burn (water and fire clash) |
| Daze | earth (Pebblit) | 30% chance: stunned 0.8s |

### Reactions (a hit of one element on a foe carrying a status)

| Reaction | Trigger | Effect |
|---|---|---|
| Thermal Shock | fire on Chill | ×2 damage, ends the Chill |
| Ignite | fire on Poison | the remaining poison bursts at once on every foe within 2 tiles |
| Electrocute | storm on Soak | arcs to every Soaked foe within 5 tiles and stuns 0.5s |
| Conduct | storm on Poison | arcs 50% atk to 2 more foes |
| Freeze | frost on Soak | frozen 2s (can't act); the next hit on it deals ×1.5 |
| Shatter | earth on Burn or Freeze | stun 1s and ×1.5 damage; also breaks armor for 4s |
| Execute | shadow on Daze or Freeze | guaranteed crit |
| Overgrowth | nature on Soak | rooted 2s (can't move) |

- **Setters and payoffs:** fire, frost, water, toxic and earth set statuses; fire, storm, frost,
  earth, shadow and nature pay them off. Every element has a part to play, and some do both.
- **Clash:** water puts out fire, so a careless fire + water pack wastes its burns (Rule 1:
  carelessness costs). A careful pack uses water for Electrocute, Freeze and Overgrowth instead.
- Reactions are ×1.5 or more, or new behaviour (Rule 1). Each first trigger goes into the codex.
- **Paths pick a side:** each path ability either sets more (wider, longer statuses) or pays off
  harder (stronger reactions). Built path abilities are re-tuned to this later; no new art.

### Threats (the checks)

From floor 3, some enemies carry a threat tag. A champion gains one threat affix (a tint and an icon
over its head; no new models). Each threat has at least 2 answers; with no answer, the fight is slow
and costly, never impossible.

| Threat | Rule | Answers |
|---|---|---|
| Armored | takes ×0.5 damage | Shatter (breaks armor), Poison (ignores armor), Freeze (frozen foes take full damage) |
| Flying | melee can't reach it while airborne | ranged creatures, Soak or Overgrowth (grounds it) |
| Regenerating | heals 3% max HP/s | Burn (stops healing), burst (Execute, Thermal Shock, Sic 'em) |
| Swarm | many weak foes, or splits and summons | splash, blast, chain, Ignite, Electrocute |
| Brute | big telegraphed hits | a tank's taunt, Freeze or Daze to interrupt, a healer |

- Existing enemies get tags: bat (flying, swarm), slime (swarm), wraith (flying), golem (armored,
  brute), cultist (regenerating: heals allies), and the Warlord and Bone King are brutes.
- **Floors announce their threats:** the portal shows the next floor's 1–2 threat icons (with the
  modifier rumour), and scouted rooms show their enemies' icons on the map (Rule 1: information
  before commitment).

### Pack upkeep (the brake on "take everyone")

- Every creature drains hunger × (1 + 0.1 × max(0, pack size − 4)). With 4 the upkeep is ×1; with 8
  every creature eats ×1.4, so 8 creatures cost as much as 11.
- The HUD shows "Upkeep ×1.4" beside the food count. Releasing a creature (pack screen) brings it down.

### Eggs (replace cages and prison rooms)

- **Sources:** an egg carrier (an enemy with an egg on its back, which drops when it dies) on most
  floors (always on floors 1–2, 70% later), chests (plain 5%, rich 25%), and the boss chest (always,
  replacing the lair's bonus cage). Prison rooms and cages are removed.
- **Pouch:** up to 2 eggs. The egg is the last item in the held cycle; **R** (pad **R**) with an egg
  held hatches it.
- **Hatching:** out of combat (no aggro'd enemy within 12 tiles), costs **3 food**. The egg cracks
  and shows **3 species** at the floor's level, each card listing its element, role, statuses it
  sets, reactions it pays off, and threats it answers. A card that would complete a reaction with
  the current pack is highlighted. **At least one of the 3 always completes a reaction** (Rule 2.6:
  enough choice to aim).
- **Choose one:** it hatches beside the player. A species already in the pack merges into it as
  60% of its XP bar instead. Or **release the egg:** every creature gets 25% of its bar.
- **Gamepad:** the egg screen uses ← / → and A, so it works on Switch.
- Pacing check: about 1.5 eggs per floor, so about 7 picks by floor 5 (Rule 2.6 wants 6 or more).

### Information and failure

- **Pack screen:** a "Reactions" panel lists what the pack can trigger now and which threats it
  answers, with gaps marked ("Armored: no answer").
- **Death recap:** what dealt the last 10 seconds of damage, their threat tags, and the answers the
  pack lacked (Rule 1: readable failure).

### Bot measurement (Rule 1: measured)

- A **careless bot** always takes the first egg option and never releases. A **careful bot** picks by
  score (+2 per reaction completed, +2 per announced threat answered, −1 if upkeep rises) and
  releases creatures that are part of no reaction once the pack passes 6.
- Target: careful reaches at least 3 floors deeper than careless; careless stalls around floor 5.

### Build order (risk / reward)

1. Statuses and reactions (unit combat code, data). Medium / high.
2. Threat tags, champion affixes, portal and map icons. Medium / high.
3. Upkeep and its HUD readout. Low / medium.
4. Eggs: items, carriers, chests, the hatch screen, removing prisons. Medium / high.
5. Reactions panel and death recap. Low / medium.
6. Careless and careful bots, then measure. Low / high.
7. Re-tune the 24 path abilities to setter and payoff roles. Medium / medium.

## Pack synergies (fielded creatures only)

- **Element bond:** 2 fielded creatures of one element deal +10% damage, 3+ deal +20%.
- **Balanced pack:** a melee, tank, ranged and healer all fielded gives everyone +10% max HP.

## Pack size

- **No cap, no bench** (user call, 2026-10-31). Every freed captive joins and fights. Release (pack
  screen) still exists.
- Follow slots past 8 repeat the 8 angles on a ring 1.2 tiles farther out per 8.
- Trade-off accepted: with no slot limit, composition is no longer a choice; food is the only brake.

## Stances

| Stance | Damage dealt | Damage taken | Behaviour |
|---|---|---|---|
| Aggressive | ×1.2 | ×1.15 | Engage range ×1.4; frontline stands 1.6× farther out |
| Guard (default) | ×0.85 | ×0.8 | Engage only within 4 tiles |
| Sneak | ×0.9 | ×1 | Only fight back; idle enemies notice the pack at 4 tiles, not 6; no front line |

- Each stance pays for its edge: Guard is safer but fights last longer (more hunger, more hits).

## Food, hunger, fainting

- Hunger runs from 100 (full) to 0.
  - Drain per second = 0.65 × species hunger × trait multiplier × (0.85 + 0.15 × stage index, where stage index is 0/1/2).
- **Auto-feed** (on by default, can be turned off): when a creature's hunger drops below 40, it eats 1 food from the pouch.
  1 food restores 45 hunger.
- **Starving** (hunger 0):
  - The creature deals half damage and loses 1% of max HP per second.
  - After **50s** of starving it **runs away for good**.
- **Pouch:** holds 40 food (60 with the Deep Pouch relic). The run starts with 6 food and 1 potion.
- **Fainting:** a creature at 0 HP faints.
  - With no aggro'd enemy within 8 tiles, it gets back up after 6s with 40% HP. Getting up costs **1 food**.
  - With no food, it stays down.
- **Food sources:**
  - Enemy drops: 10% chance of food (2) or a berry (1); 4% chance of a potion.
  - Chests and larder rooms.
  - Shrines of Plenty.
- Recruited creatures arrive hungry (hunger 45–70).
- **No pack cap** (see Pack size): food is the brake on how many creatures you keep.

## Enemies

Scaling on floor f: HP × (1 + 0.28(f−1) + 0.025(f−1)²) and ATK × (1 + 0.16(f−1) + 0.012(f−1)²).
XP × (1 + 0.25(f−1)).

| id | name | hp | atk | range | cd | speed | xp | from floor | spawn weight | weak / resists | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bat | Cave Bat | 16 | 4 | 0.9 | 0.8 | 4.4 | 4 | 1 | 3 | storm / earth | flies, small |
| skeleton | Skeleton | 34 | 7 | 1.0 | 1.1 | 2.7 | 7 | 1 | 4 | earth / toxic | |
| slime | Gloop | 40 | 5 | 0.9 | 1.2 | 2.0 | 7 | 1 | 3 | frost / water | splits into 2 half-size slimes on death |
| archer | Goblin Archer | 26 | 7 | 6 | 1.6 | 2.9 | 8 | 2 | 3 | fire / shadow | ranged |
| spider | Crypt Spider | 30 | 6 | 1.0 | 0.9 | 3.6 | 8 | 2 | 3 | fire / toxic | poison |
| cultist | Cultist | 34 | 9 | 5.5 | 1.9 | 2.5 | 10 | 3 | 2 | storm / shadow | ranged; heals a hurt ally 25% every 4s |
| golem | Stone Golem | 110 | 13 | 1.2 | 1.8 | 1.8 | 18 | 4 | 1.5 | water / fire | armor 0.30, large |
| wraith | Wraith | 40 | 11 | 1.0 | 1.0 | 3.8 | 14 | 5 | 2 | nature / frost | flies, slow |
| mimic | Mimic | 70 | 12 | 1.1 | 1.1 | 3.0 | 25 | — | — | earth / storm | disguised as a chest (see Chests) |

- **Idle:** enemies wander near their spawn point.
  - They aggro when an ally comes within 6 tiles in line of sight (4 in Sneak stance), or when they are hit.
  - When one enemy aggros, the whole room aggros.
- **Giving up:** enemies drop aggro beyond 18 tiles and walk home.
- **Room themes:** 25% of rooms use a single enemy type.
- **Intent:** each aggro'd enemy shows its target, its attack timer and (once learned) its weakness.
- **Champions:** from floor 3, 8% of enemies are champions: HP ×2.2, attack ×1.3, size ×1.3, XP ×2.5,
  and they drop an item.

## Bosses (they rotate by floor; each full cycle of 4 adds +25% HP)

| Boss | hp | atk | range | cd | speed | abilities |
|---|---|---|---|---|---|---|
| The Bone King | 420 | 14 | 1.4 | 1.4 | 2.3 | summon skeletons, slam |
| Gloop Matriarch | 520 | 11 | 1.4 | 1.3 | 1.9 | slam, spawn small slimes |
| Goblin Warlord | 460 | 16 | 1.3 | 1.2 | 2.6 | charge, arrow volley |
| Hollow Lich | 400 | 12 | 6.5 | 1.6 | 2.2 | projectile nova, blink, summon wraiths |

- **Cadence:** a boss uses one ability every 6s (every 4s once enraged) and cycles through its list.
  At 50% HP it becomes **enraged**: cooldown ×0.8, speed ×1.15, and bigger abilities.
- **Abilities:**
  - *Slam*: a telegraphed circle (radius 2.6, 1.1s warning) that deals 160% damage and can stun.
  - *Charge*: a 0.7s telegraphed wind-up, then a dash that hits for 140%.
  - *Volley*: a fan of 5 arrows (7 when enraged).
  - *Nova*: a ring of 12 projectiles (16 when enraged).
  - *Blink*: teleports to a spot far from its target.
  - *Summon*: 2 minions (3 when enraged).
- **Boss death:** leftover minions die, a boss chest appears, 3 food drops, and the portal down opens.

## Floors and rooms

- **Layout:**
  - The map is about (44 + 3f) tiles square, capped at 84.
  - Rooms: min(9 + 0.8f, 20). Normal rooms are 5–10 tiles per side; the boss lair is 11–13 per side.
  - Rooms are connected by a minimum spanning tree plus about 25% extra loops, so there are cycles.
- **Fixed rooms:**
  - The lair has a single entrance.
  - The entrance room is the room farthest from the lair.
- **Theme:** changes every 3 floors and cycles through 5:
  - Forgotten Crypt, Mossy Warrens, Frozen Halls, Ember Depths, The Abyss.

| Room | Contents |
|---|---|
| Entrance | Safe start. |
| Chamber | Fight. 25% chance of a chest. |
| Prison | Removed (eggs replace cages). The Cage code is kept but no longer spawned. |
| Vault | 1–2 rich chests plus guards. |
| Larder | 1–3 food items (2 food each) on the floor plus a few weak guards (1–2 rooms). |
| Shrine | 60% chance per floor. One random blessing: **Plenty** (pack fully fed, +3 food), **Vigor** (everyone fully healed, fainted creatures revived), or **Kinship** (every creature gets 30% of its XP bar). |
| Lair | Boss and sealed portal. The boss chest always holds an egg. |
| Camp | From floor 2, 40%. A campfire: Rest once (everyone heals 50% and red health, fainted get up, +5 bond), then Cook 3 food into a random treat, twice. |
| Trap hall | From floor 2, 35%. 5–9 spike traps (2.4s rest, 0.8s glowing warning, 0.5s up) that hurt enemies too, guarding a rich chest. |
| Watchtower | 30%. Using it scouts every room on the floor. |

- **Scouting:** rooms within 7 tiles of the player (16 with a Gloomowl line in the pack) are marked on
  the map with their type, enemies and loot.
- **Vaults** can hold chests sealed by a pressure plate: set a creature down on the plate to open them.
- **Floor modifiers:** from floor 2, 70% of floors get one, announced at the previous floor's portal:
  Bloodlust (enemies +20% attack, loot ×2), Calm (no traps, a shrine), Champions (×3 champions),
  Darkness (torches out, XP +30%), Famine (half food, XP +25%), Swarm (+50% enemies at −25% HP),
  Treasure Trove (extra chests, twice the Mimics).

- **Enemy count:** min(2 + 0.6f + rand(0–2), 9), and never more than room area / 6.
- **Captive species weights:** rarity 1 → 5, rarity 2 → 3, rarity 3 → 0.8 + 0.25f.

## Chests and loot

- **Food:** a plain chest gives 1–2, a rich chest 2–4, a boss chest 3–5. The Deep Pouch relic adds +2.
- **Potion:** 30% chance (50% in rich chests).
- **Relic:** 12% chance in plain chests, 60% in rich chests, 100% in boss chests. A duplicate relic gives +3 food instead.
- **Elixir** (fills half of a creature's XP bar): 8% chance in plain chests, 35% in rich chests, 100% in boss chests.
- **Mimic:** from floor 2 on, 15% of plain chests are Mimics.
  A Mimic wakes when anything touches it and drops 2 food plus a relic or an elixir.

## Creature gear (one slot each)

Gear comes from chests and drops (30% of gift loot). It goes in the held cycle after the egg
(reached with C / L, no number key) and is **equipped by throwing it at a creature**, like a treat;
its old gear goes back to the inventory. The pack screen can also gift it.

| Gear | Effect | Fits |
|---|---|---|
| Ember Claws | hits Burn | sets up Shatter; answers Regenerating |
| Frost Fang | hits Chill (slow) | sets up Thermal Shock |
| Venom Stinger | hits Poison (through armor) | sets up Ignite, Conduct; answers Armored |
| Tide Charm | hits Soak (puts out Burn) | sets up Electrocute, Freeze, Overgrowth; answers Flying |
| Catalyst Band | reaction power ×2 | a payoff creature: on a payoff path, ×4–5 |
| Feather Harness | melee hits on Flying land in full, +10% speed | a melee creature; answers Flying |
| Tower Shell | taunts like a tank, +25% HP, −20% attack | a sturdy non-tank; answers Brute |
| Mender Leaf | regenerates 1% max HP/s | filler |
| Lucky Bell | +15% crit | filler |

- **Rule 1:** the careless player puts gear on whoever's bare and gets little (a setter on a
  creature with no partner, a Catalyst Band on one that triggers nothing). The careful player puts
  a setter where a payoff partner exists, the band on the payoff creature, and patches the floor's
  threat gap without adding a mouth to feed. The reactions panel and threat answers count gear.
- Gear replaces three flat +20% items (Power Band, Swift Ribbon, Spiked Shell); flat bonuses don't
  count as rewards (Rule 2).

## Relics (permanent for the run)

| Relic | Effect |
|---|---|
| Feast Bowl | Food restores 50% more |
| Iron Collars | Creatures +20% max HP |
| War Drum | Creatures +15% damage |
| Slow Belly Charm | Creatures get hungry 25% slower |
| Vampire Fang | Creatures heal 8% of damage dealt |
| Swift Boots | Player +15% speed |
| Herding Whistle | Creatures +20% speed |
| Lucky Coin | Loot drops ×1.5 |
| Thorn Mail | Attackers take 30% of the damage back |
| Bond Charm | Creatures +30% XP |
| Smelling Salts | Fainted creatures get back up twice as fast |
| Whetstone | Sword +40% damage |
| Bright Lantern | See farther in the dark |
| Deep Pouch | Pouch holds 60 food; chests hold +2 |

**Build-around relics** change a rule instead of adding a number (same drop pool):

| Relic | Effect |
|---|---|
| Ravenous Bell | Starving creatures deal double damage instead of half (they still lose HP and can run away) |
| Prism Collar | No element bonds; each different element on the field gives every creature +4% damage |
| Comet Harness | A thrown creature bursts on impact, hitting every foe within 2 tiles for 80% |

## UI

- **HUD:** player HP, food and potions, the held-throwable boxes, the pack
  list (portrait, name, level, HP bar, hunger and status tags), messages, an interaction prompt, a
  minimap and the boss bar.
- **Held throwable (bottom right, Pikmin-style):** a big framed box with the current item's icon
  and count, its name underneath and a "[C] / R next" hint above; smaller boxes on each side show
  the previous and next items in the cycle. Icons are drawn in code: loaf (food), drumstick (meat),
  crystal (rock candy), chili (spice), honeycomb (honey), flask (elixir), egg, and a charm on a ring in the item's color (gear).
- **Look-at tag:** the creature the player aims at shows hunger and its evolution path (favorites
  and leaning, or the path taken) under its name tag.
- **Volume:** master volume defaults to 25%. Every synthesized sound is loudness-matched at startup
  (K-weighted RMS as in ITU-R BS.1770, short sounds averaged over 0.2 s) to the median of the set,
  then mixed on purpose: attack starts −8 dB (ranged shot −6), swing −3, throw −4, pet −3; call
  sites add per-event emphasis (boss +4, gate +3). Before matching, raw levels spanned 13 dB.
- **Controls** (Switch layout after Splatoon 3; Godot binds pad buttons by position):

  | Action | Keyboard | Switch |
  |---|---|---|
  | Move / look | WASD / mouse | left / right stick |
  | Jump | Space, mouse wheel | B |
  | Walk | hold Shift | L3 (toggle) |
  | Sword; hold to charge-throw a carried creature | LMB | ZR |
  | Throw held item at the aimed creature | RMB | R |
  | Cycle held item (1–6 direct on keyboard) | C | L |
  | Interact; on a creature: tap = pick up, hold 0.25 s = pet | E | A |
  | Sic 'em (aimed enemy) | Q | ZL |
  | Potion | F | Y |
  | Heel | R | D-pad down |
  | Stance | T | D-pad up |
  | Map | M | X |
  | Pack screen | Tab | + |
  | Release mouse / close screen | Esc | − |

  Free on the pad for later: D-pad left/right, R3. Prompts still name keyboard keys only, and the
  pack screen needs the mouse.
- **Pack screen:** the fighting and resting lists, each creature's stats, traits and path, plus feed,
  gift, rename, Rest / Field (at a rest spot) and release. It also shows the weapon, relics,
  synergies, stance, the auto-feed toggle and the next floor's rumored modifier.
- **Floor card:** the floor number and theme name appear on arrival.

## Balance reference (prototype autopilot bot, which walks room to room and never dodges)

- The pack reaches 8 creatures around floor 4 (measured before the bench; the bot never swaps and
  fields 5 now, so these numbers need a fresh run).
- With a full pack, food holds between 20 and 60.
- Runs end around floors 7–10.
- Real players are slower than the bot, so hunger bites harder for them.

## Ideas for later

- Per-creature commands beyond setting one down to guard a spot.
- Merchant rooms and save/continue.
- Gamepad navigation for the pack screen (it still needs the mouse).
