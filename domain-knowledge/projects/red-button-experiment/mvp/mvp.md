# MVP build notes (2026-11-03, built by Claude in two overnight sessions)

**Superseded in part (2026-11-05):** design v2 replaced the events, machines, upgrades, junk and
boxes described below; see `docs/build-v2.md`. The room, voice, Steam, hatch and beam still hold.

What exists, how to run it, and which choices were Claude's (not user decisions; confirm or change
them, then record the decided ones in the design docs, `docs/core-design.md`). Night 2's extras are listed separately so the
core MVP can still be judged on its own (guardrail: core loop before layers).

## Run it
- **Play:** `godot --path .` → menu: name, **Host**, or an IP + **Join** (LAN / Tailscale / ZeroTier,
  `ip` or `ip:port`). Default port 24680.
- **Steam** (user, 2026-11-03: "implement steam networking"): with the Steam client running, the
  menu's **Host on Steam** opens a friends-only lobby; friends join from the Esc menu's **Invite
  Steam friends** (Steam overlay) or **Join Game** on you in their Steam friends list. Dev app id
  480 (Valve's Spacewar test app) until the game has its own (`Net.STEAM_APP_ID` and
  `steam_appid.txt`). GodotSteam 4.21 lives in `addons/godotsteam` (git-ignored, copied from
  `~/Playground/mustache-madness`). Without Steam the button is greyed out and address play works.
- **VS Code:** F5 configs (Play / Host / Join) and tasks (host + 1 client, host + 2 bots, tests).
- **Alone with bots:** task "Play: host + 2 bot clients", or start a host and run
  `godot --headless --path . -- --join=127.0.0.1 --bot --name=Bo`.
- **Command line** (after `--`): `--host`, `--join=IP[:port]`, `--port=N`, `--name=NAME`,
  `--bot` (plays by itself) / `--bot=human` (rough human pace), `--event=NAME` (host: every event is
  NAME, e.g. `decoy`, `potato`, `fire`, `quiz`), `--stage=N` (host: runs start at stage N, 0-based),
  `--cam=x,y,z,yaw,pitch`, `--give=ITEM` (that item in your hand), `--quit-after=S`, `--shot=S` (screenshot to `logs/`), `--render=WxH`
  (3D renders at WxH in any window: 4K benchmarks). AI runs: `tools/ai_run.sh` (Hyprland: small,
  top-left, never takes focus).
- **Tests:** `godot --headless --path . -s addons/gut/gut_cmdln.gd` (rules, every event, shop, sim).
- **Controls:** WASD, Space jump, Ctrl/C crouch, **E or left click** (press, shop, kick boxes,
  slap people, take small items in hand, hold to carry big ones, use what is in hand), **G** drop,
  **F** (carry on the beam), Esc menu (volume, mouse sensitivity, narrator voice on/off, leave).
- **Volume** defaults to 10% (user request); the Esc menu changes and saves it.

## Core MVP (night 1, from core-design.md's MVP list)
| Design item | Built as |
|---|---|
| 3 stages to 1k | Goals 10 / 100 / 1,000; a milestone resets the ceiling and unlocks a shop tier |
| Button, counter, wallet | One number: the counter is the wallet. Wall display, pedestal and HUD |
| Shop terminal | Now a hatch per wall with an on-screen order menu (see the clutter pass below) |
| 3 upgrades | Bigger Finger (+1 per hand press), Lucky Finger (x5 crit chance), Buddy System (x1.5 when two players press within 0.45 s) |
| 2 machines + plug tier | Drinking Bird, Hamster Wheel; look + E to unplug/plug |
| Falling ceiling | Real slab; squish on loss (the red end line on the walls was removed, user 2026-11-03) |
| 6 events | Rule flip, falling-object mess (physics boxes), quiz, green light, PvP mash, don't-press trap |
| 3 minigames | Blackout events; their stakes are announced first (see night 2) |
| TTS narrator + orders | Voice (see below), subtitles, chime and green ORDER badge on every order (Simon Says removed 2026-11-03) |
| Stats + 2 memory callbacks | Director at calm moments, once each per run, 40 s apart |

## Night 2 additions (all switchable; each is a small piece)
**Narrator and memory (pillar 4)**
- **Real voice:** Piper neural TTS (since 2026-11-03, user request for a more natural voice): one
  long-running Piper process on a worker thread, about 0.1 s per short line, cached in
  `user://voice/`. Voice: `en_US-joe-medium` (CC0; credited anyway in `docs/credits.md`;
  chosen by the user 2026-11-03 from five samples). Fallbacks: OS TTS, espeak-ng, babble. Urgent lines interrupt, others queue.
  Setup: `tools/get_piper.sh` (Piper for Linux + Windows and three licensed voices, git-ignored);
  the export copies Piper and the voice next to the game (zips grew to about 120 MB).
- **Eye + culprit spotlight:** when a line names someone, the eye looks at them and a red spotlight
  picks them out.
- **Lifetime memory:** per-name stats across runs (still recorded; the join greeting was removed
  2026-11-03 as noise, along with the lobby welcome and "Subject X has joined").
- **Record announcements:** fastest escape, most presses, most fines (the wall board was removed).
- **More callbacks:** hog (a ceiling arm grabs and holds them for 25 s; super rare: once per run, 80% of 40+ answers), smoker, slapper;
  slacker now also gets the cone of shame.
- **Reactions:** idle taunts (meaner in stage 3), first-purchase lines, crit/unplug/slap
  quips, ceiling warnings at 30% and 10%. Event lines rotate 3 joke variants (2026-11-03).
- **Line variety pools** for order outcomes.

**Design specials**
- **Cursed button** (once per run): a silent black button; +25% wallet, double presses for 30 s.
  No prompt, line or tag (redone 2026-11-03).
- **Greedy press** (finale, last stage): first press wins a third of the wallet, others pay;
  hidden 20% the button lies and only the presser loses.
- **Minigame stakes announced first:** win = ceiling back / +15%; lose = ceiling
  drops 10% once / cone of shame + nickname for one subject / -15%. Shown on the display.
- **Fast crews get a spicier next stage** (speed earns no power): ceiling starts x1.2, first event
  sooner, narrator notices.
- **Losing unlocks things** (pillar 3): hard hats, Ceiling Jack, Snooze Button; one unlock
  per loss (never machines or upgrades).
- **Escalation in stage 3:** orders can land on top of pressing events.

**New events** (13 regular + 2 specials now): double points, low gravity (boxes too), runaway
button (it drives around the room), reversed controls (one subject), machine fire (3x speed,
explodes unless unplugged), hot potato (holder's presses cost points; slap to pass), decoy shell
game (4 identical buttons, decoys cost points), audio quiz (count the beeps in the dark).

**New orders:** look at the ceiling, everyone press together (within 1 s), "only Bo presses",
"everyone stand next to Bo".

**Don't-press trap** (2026-11-03, after removing Simon Says): the button glows red; the narrator
shouts "PRESS IT NOW!" (a lie); the real signal is the button turning green with a chime.

**Shop:** east terminal adds Robot Arm (fast; slaps bystanders) and Cannon (12-point shots; 20%
hit a subject instead) at stage 3, and the Smart Plug (machines pause on rule flips, 15% rebel;
pulls a burning machine). West wall "Junk & Bro Science" machine: Bro Science pamphlet (reveals a
secret rule; each run some rules are real, some placebo; "?!" on press numbers when one fires),
Cigarette (smoking near the button is fined: you pay twice), Insurance (absorbs a fine),
Master Switch (lever: all machines on/off), plus the two loss unlocks.

**Friendslop:** slap (E on a subject: knockback, passes the potato), cone of
shame vignette when you wear it, cigarettes with smoke, pancakes on a loss, confetti and an exit
room on a win ("ONE BILLION MORE?" button), awards on the end screen.

**Readability:** floating press numbers (gold crits, purple costs, "?!" secret rules), stage decor
(red beacon and floor strips at stage 3), effects list on the display, how-to-play on the display in the lobby,
ceiling beeps in the last 12 s.

## Late additions (end of night 2)
- **4 more blackout minigames:** countdown (press at exactly 10 s; the display goes dark after 3),
  reaction (wait for the light, then everyone presses within 1.5 s), last one (PvP, 2+: the last
  to press pays), rhythm (presses on a metronome beat; three off-beat presses lose).
- **Ambience:** a quiet room hum (drops in blackouts) and a ceiling grind that gets louder and
  higher as the ceiling falls.
- **Builds:** `build/red_button_experiment_linux.zip` and `_windows.zip` (VS Code task "Export
  builds"); the Windows build joined a Linux host in a test.

## Clutter pass and shop hatch (2026-11-03, after the user's first look)
- **Shop hatch:** one item-sized slot in the east wall (no junk machine, no terminal). E opens the
  shop menu on your screen: shop items left, junk and bro science right; click to order. The hatch
  stays shut while you browse, then pops open and spits the item itself into the room. The host
  still checks range.
- **Returns:** hold something near the hatch and it opens; E throws it in for 50% (machines: of
  what the last one cost, so the next one costs that price again). Burning machines are refused.
- **Ceiling arm instead of the bench:** no glass cage in the room (it spoiled the joke). The hog
  is grabbed where they stand by an arm that drops from the ceiling, lifted a little and held
  (can look, cannot move or press) for 25 s, then dropped in place. Title "Held".
- **No records board:** records are still kept and announced by the narrator.
- **Wall display:** count, "OF goal · STAGE n", a ceiling bar with seconds, and one status (order,
  event, rule, or lasting effects). Removed: experiment number, the mirrored subtitle, the separate
  effects column, the FACILITY label.
- **Less noise:** press numbers keep one small size on screen and quick plain presses merge into
  one number (crits, costs and "?!" stay separate); name tags keep one small size; machine labels
  appear only when unplugged or jammed; the controls hint shows in the lobby and fades once a run
  starts; the rumors board is gone (Bro Science is off the shop).
- **Physical items:** the hatch spits the item itself; hold F to grab it (heavy ones need several
  players); machines press only when aimed at the button; E uses jack, snooze and switch; the
  smart plug goes into one machine. Bots haul items to the button and aim machines.
- **Debug:** `--shop` opens the shop menu after 2 s, `--spit=S` (host) makes the hatch spit a Drinking Bird,
  `--grab=S` (host) has the ceiling arm grab the newest player.

## Item ladder (2026-11-03, design: `docs/gameplay-design.md` → Items)
The shop sells only Squeaky Hammer (15), Ball + Bat (60, spits both), Monkey Car (150) and Cannon
(300); the old items stay in code, unsold. The menu shows name and price only. Hits on the button
score `(speed − 5) × weight kg` (a ball off the bat × 8), with a bigger orange number and a
louder thunk. Checked: unit tests (8 new) and a headless physics probe (an 18 m/s ball scored 25; a
cannon-fired hammer 66). Not checked: how it feels with people.
- **How to use them (Claude's choices, not your decisions; the game never says):**
  - Hand items (since the E/click change): E on the hammer, bat or ball puts it in your hand;
    G drops it; a slap knocks it out of someone's hand.
  - Hammer in hand: E by the button swings it in: +5 and a squeak; at someone: a bonk.
  - Ball in hand: hold E to wind up (1 s to full), release to throw at 3–20 m/s. Beam-carried
    things still keep their speed when let go (swing the view and let go).
  - Bat in hand: E swings at a ball within 1.8 m. A pitch over 6 m/s flies off where you look,
    ~(8 + 1.2 × pitch) × 0.75–1.3 m/s; a slower one drops (a bunt).
  - Cannon: E on it with something in hand loads it, and so does letting go of a carried thing
    by its mouth (a gold plug shows in the barrel). A tap of E on the cannon fires along the
    barrel; so does E while carrying it with F. The load lands whole.
  - Hits are judged by a bounce right by the button (fast things move ~0.3 m a frame, so the
    contact is rarely sampled). Checked: an aimed full throw scored 30 in 4 of 5 probe runs (the
    miss was the probe teleporting the player onto the ball).
  - Small items never block players (a player standing on the ball was flung ~1 km up once).
  - Monkey Car: drives at 3 m/s, bounces off walls, the pedestal and people (runs them over),
    and slaps the button on 50% of passes within 1.1 m (scores as a 9 m/s hit).
  - Anything flying at 6 m/s or more knocks over whoever it hits.
- **Gaps:** shop rows have no picture yet; bots only buy, haul and drop the toys (no throwing,
  batting or cannon use), so bot runs don't exercise the ladder's scoring; prices and the impact
  formula are guesses; the old machine code (rule flips, fire, smart plug) has nothing to act on.

## Path items (2026-11-04, design: `docs/gameplay-design.md` → Path items)
On sale after the ladder: Flashlight (40) and Egg (200, one per run). Both go in the hand (E), G drops.
- **Flashlight:** E switches it on and off (a spotlight from its lens). Each run starts with hidden
  writing on the walls (red): past experiments with their counts as tally marks, past subjects'
  names ("BO WAS HERE"), and "IT GOT COLD" (the egg hint). It fades in only inside a lit beam
  (9 m, 24°). It works any time, not only in a blackout: blackouts are off with the narrator.
- **Egg:** warms while 2+ players stand within 1.8 m of it (a huddle); it cools at half that
  pace otherwise. Its shell turns orange and glows as it warms, it cracks (a sound) at half and
  near the end, and it rocks just before hatching. 45 s of huddling hatches it. It breaks on a hit at
  7 m/s or more (thrown, fired, hit while flying; a hand drop or the hatch spit is fine) or a
  hammer swing; a yolk splat stays on the floor and it is gone for the run.
- **Alien:** stands where the egg hatched, wanders at 1 m/s, can be carried on the beam. At a wall
  it draws its next sign (green, every 15 s at most, never on the hatch), with a chirp. The signs
  are hidden writing too: only the flashlight shows them. Five placeholder signs (moon, up,
  stars, button × 3, "moon = button × 3"); the moon route itself isn't built.
- **Claude's choices to confirm:** warmth = huddle; break = hard hit or hammer, lost for the run;
  the alien's clues are flashlight writing (links the two items); prices; the crew-mark texts.
- **Checked:** 6 new unit tests (91 pass); a headless host + client + bots run with no script
  errors. **Not checked:** how it looks (beam strength in the white room, mark legibility) and
  feels; physics of the egg break threshold.

## Balance (bot-measured only)
- Perfect bots win easily; a `--bot=human` trio (about 3 presses/s, walks to the shop, hesitates)
  won 2 of 3 runs after tuning. Stage 3 lasts about 70-90 s; a run about 2 minutes.
- The knobs: `scripts/core/tuning.gd` (stage seconds, crew scaling, fines, events) and
  `scripts/core/economy.gd` (prices). Fun is still your playtest's call.

## Claude's choices to confirm (assumptions, not decisions)
- Ceiling time scales with crew size (1: 1.0x, 2: 0.67x, 3: 0.5x, 4: 0.4x).
- Spending can drop the counter below a reached milestone; the stage stays.
- Machines press for 1 (cannon 12); Bigger Finger only boosts hands.
- Blackout presses add nothing to the counter; the run starts on the first press; the host
  restarts.
- Box physics runs on the host only; clients mirror positions.
- Bro science secret rules apply even before anyone reads about them.
- The cursed presser's advantage: double presses for 30 s.

## Known gaps
- Voice is espeak (robotic); the plan is a licensed AI voice (open question).
- Players don't collide with each other; machines are static (only explosions knock people).
- Steam play not tested end to end: it needs the Steam client running and a second Steam account
  on another machine (one account cannot join its own lobby). Checked: the extension loads, the
  peer class exists, the game falls back cleanly when Steam is not running.
