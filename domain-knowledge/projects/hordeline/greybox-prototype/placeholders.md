# Placeholders

Everything listed here is a stand-in, chosen so the prototype exercises every rule at least once.
The real content list is an open design question (`docs/questions.md`). Data lives in
`data/weapons/`, `data/parts/`, `data/enemies/` (Godot resources) and `sim/tuning.gd` (`LINES`);
add or swap a `.tres` and register it in `data/content.gd`.

## Weapons (4) and their evolutions (4)

| Weapon | Fires | Chore | Mount use | Evolves with | Evolution | Chore after |
|---|---|---|---|---|---|---|
| Rattle Gun | fast hitscan, nearest | **ammo**: carry crates from the ammo locker (car 1) | any | Belt Feeder | Hellstorm | none (relief) |
| Steam Cannon | lobbed splash shell | **jam**: every 5-9 shots, hold E 1.5 s | any | Pressure Gauge | Gut Mortar | **corpses** as shells (swap: bigger, funnier) |
| Saw Arm | spinning blades around its mount, hits climbers and boarders | **crank**: hold E to wind; it unwinds in ~17 s | side mounts only reach their side | Flywheel | Perpetual Grinder | none (relief), wider |
| Blunderbuss Turret | **manual** turret, shotgun spread, soft auto-aim | someone mans it (E), clicks to fire | any | Iron Sights | Thunderbuss | still manual, but fires itself at half rate when unmanned |

Rules exercised: 4 chore types (carry, hold, crank, man), a manual turret, side vs roof mounts,
evolutions that drop a chore and one that swaps it, corpses as fuel and as ammo.

The train leaves the depot with one Rattle Gun on mount 1 (ASSUMED, like VS's starting weapon).

## Parts (4), levels 1-5

| Part | Effect per level | Evolves |
|---|---|---|
| Belt Feeder | all weapons fire 8% faster | Rattle Gun |
| Pressure Gauge | splash and blade reach +12% | Steam Cannon |
| Flywheel | furnace burns 10% slower | Saw Arm |
| Iron Sights | all weapons +12% damage | Blunderbuss |

## Creatures (2 + boss)

| Creature | Role | Exercises |
|---|---|---|
| Skitter | small, fast, swarms, climbs aboard (2 s climb), bites crew, gnaws cars | boarding, crew knockdown, corpses on deck, 20% hat knock per bite |
| Bruiser | big, slow, tanky, can't climb: rams a car's side, swats crew over the edge | carriage damage, knocking crew around, always knocks the hat off |
| The Maw (boss) | giant, waits at the terminus, spits skitters | final-station siege |

## Gem net (EXPERIMENTAL station)

One net post at the back of the last car (`--no-net` removes it). Numbers in `sim/tuning.gd` (`NET_*`).
No part upgrades it yet (the magnet stat exists but no placeholder part uses it).

## Lines (station choices)

Quiet Line, Gem Line, Market Line, Express Line (2 offered per station), then the Terminus Line.
Each scales the horde, the gems, the number of halts and the length (`sim/tuning.gd`, `LINES`).

## Art

Grey boxes and flat colours only (no art pass until the user has playtested the core).
