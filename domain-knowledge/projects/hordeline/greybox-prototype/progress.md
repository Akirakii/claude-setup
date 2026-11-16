# Progress

Last update: 2026-11-02 (AFK session; 44 rule tests + 10-step network self-test pass). Grey-box prototype; every mechanic in `docs/design.md` is in,
with AFK guesses tagged `ASSUMED` there and open choices in `docs/questions.md`.

## How to run

```sh
cd ~/Playground/hordeline
cp -r ~/Playground/mustache-madness/addons/gut addons/   # only on a fresh clone (addons/ is gitignored)
godot --path .                                              # menu: Host / Join
```

- **Host:** type a name, press Host, then "Start the run" when friends are in. The lobby shows the
  addresses friends can type (LAN, Tailscale `100.x`, ZeroTier). Port 24680 (UDP), change it in the menu.
- **Join:** type the host's address (any IP or hostname) and press Join. You can join mid-run.
- **Continue saved run:** the host's lobby shows it once a run reached a main station.

Quick local tests (several instances on one PC):

```sh
godot --path . -- --host --name=Ann --autostart=2     # starts when 2 players are in
godot --path . -- --join=127.0.0.1 --name=Bob
godot --path . -- --solo --fast                        # alone, 1.2 km stretch
```

Flags (after `--`): `--host`, `--join=IP`, `--port=N`, `--name=S`, `--autostart=N`, `--solo`,
`--stretch=METRES`, `--stretches=N` (run length), `--fast`, `--god` (engine can't die),
`--autopilot` (host does every chore: for headless checks), `--seed=N`, `--quit-after=S`,
`--mute` (no sound), `--no-net` (turn off the EXPERIMENTAL gem net), `--shot=S` + `--cam=x,y,z,yaw,pitch` (screenshots to `logs/`), `--selftest` (client runs scripted chores and prints PASS/FAIL).

### VS Code

Open the folder in VS Code (godot-tools extension, recommended in `.vscode/extensions.json`).
F5 picks a launch config in `.vscode/launch.json`: Menu, Solo (fast), Host, Join localhost, or the
compound "Host + 1 client" (two debugged windows). Breakpoints work in `.gd` files. Tests are tasks
(`Tasks: Run Test Task`): rules, balance probe, network self-test. The GDScript language server starts
headless, so the Godot editor need not be open.

## Controls

WASD move, Space jump, mouse look. **E**: tap to take / put / man a turret / pull the brake / flip the
lever; **hold** to unjam, crank, repair (red toolbox), revive. **Gem net** (EXPERIMENTAL, back of the last car): E to man it, aim to sweep, **hold click** to reel in, E to leave (spills the catch). **Left click**: shove with empty hands
(creatures and friends), throw what you carry, fire a manned turret. **Q** drop. **1/2/3** captain picks
a card. **Tab** crew sheet (who did what). **M** mute. **Esc** frees the mouse (station panel, menus).

## What works

- Train on rails (train frame: the world scrolls). Furnace sets speed; coal bin refills slowly;
  corpses burn too. Throwing coal or corpses into the furnace counts.
- Carriages with HP; a broken carriage's guns stop until repaired at its toolbox. Engine at 0 = run lost.
- 4 placeholder weapons with 4 different chores (ammo crates, jams, crank, manual turret), 4 parts,
  4 evolutions (two drop the chore, one swaps it for feeding corpses, one keeps manual but self-fires).
- Shared XP from gems the train pulls in (within 6 m), plus the EXPERIMENTAL gem net (sweep, reel in, by-catch
  of skitters lands on deck); level-ups queue; only the captain picks (1/2/3), no pause.
- Captain's hat: steal (E on the captain), knocked off by creatures or shoves, can fly off the train
  and be lost; a spare appears on the engine hook. No captain = picks wait.
- Horde: Skitters swarm, cling, climb aboard, bite crew, gnaw cars; Bruisers ram and swat crew.
  Fast engine plows creatures on the track. Surges from one side every 70 s.
- Crew: knockdown at 0 HP, revive by holding E, self-revive after 25 s, fall off = back aboard in 3 s.
- Readability: every station has a lamp (green/blinking red), a status label readable from anywhere,
  chore gauges, smoke from damaged cars, furnace glow and stack smoke by coal level, positional
  beeps for failing guns, a horn for a low furnace and badly hurt cars. Top-left board lists each
  station, how long it has been failing and who touched it last.
- Route layers: halts with loot (captain's brake), junction lever, main stations (repair, buy cars,
  pick the next line, 60 s), 4-stretch run, boss siege at the terminus (The Maw), save at stations.
- End screens with awards (Stoker, Butterfingers, Mutineer, Chew Toy...).
- Networking: host-authoritative over ENet; snapshots compressed and split under the MTU at 20 Hz.

## Tests

```sh
godot --headless --path . -s addons/gut/gut_cmdln.gd -gexit                                  # rules (CI set)
godot --headless --path . -s addons/gut/gut_cmdln.gd -gconfig= -gdir=res://test/probe -gexit  # balance probe (slow)
```

The balance probe only gives starting numbers. Fun is judged by the user's playtest.

Network self-test (two processes):

```sh
godot --headless --path . -- --host --port=24701 --autostart=2 --god --quit-after=40 &
godot --headless --path . -- --join=127.0.0.1 --port=24701 --selftest
```

## What is next

1. **User playtest** (2-4 players). Playtest questions in `docs/design.md`.
2. Tune from the playtest: spawn rate, boarding caps, chore timings, XP curve (all in `sim/tuning.gd`).
3. Answer `docs/questions.md`, then replace placeholders with the real weapon list.

## Known issues / limits

- Creatures don't physically block players (they bite and shove instead).
- Players are client-authoritative for movement (co-op trust); fine for friends.
- The host leaving ends the session (by design: no host migration).
- Balance is a first guess from a crude probe (scripted crew, no aiming): a kept-up 2-player crew
  holds about to the end of stretch 1 with damage; a neglected train dies in ~90 s; 4 players are
  comfortable. Stretches 2-4 and the boss are untuned. The user's playtest decides.
- With only 4 placeholder weapons, late runs run out of new cards (filler cards appear).
- Debug: `--xp=N` grants XP at start (to see the cards).
- Sounds are synthesized beeps and noise (placeholders).
- The network self-test's "steal the hat" step (and the brake step after it) fails in about 3 of 4
  runs, on the code before the gem net too. Cause not investigated yet.
