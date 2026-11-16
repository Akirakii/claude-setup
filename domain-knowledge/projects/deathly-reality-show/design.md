# Deathly Reality Show: design (v1, superseded)

> v1 minigames (Gauntlet, Crusher) were replaced after the user's playtest on 2026-11-08 ("too
> simple and easy and requires no cooperation at all"). Current games: `minigames-v2.md`. The show
> pillars below (user) still hold.

Tags: (user) = the user's own words chose it; (Claude) = picked while the user was away, to confirm.
Numbers live in `scripts/core/tuning.gd`. Rules in `scripts/core/show_sim.gd`.

## Pillars (user)
- A TV stage with an NPC audience; the host is the Reaper. (user)
- 3–6 players, cooperative, minigames. (user)
- First person while playing; a fixed third-person TV camera while the host explains and between
  games. (user)
- Brutal deaths with lots of blood. (user)
- A dead teammate comes back in the next minigame. At least one player must clear a minigame to
  advance; if all die in the same minigame, the team loses. (user)
- Levels: 3 for now, each a minigame. Build 2 minigames. (user)

## Show flow
1. **Intro** (10 s, TV camera): the Reaper explains the minigame (subtitles + babble voice);
   camera cuts from the host to an overview of the set. Players frozen. (Claude: lengths, cuts)
2. **Play** (first person) until cleared, failed or the time runs out.
3. **Result** (6 s, TV camera): the Reaper reacts; corpses stay on the set. (Claude)
4. Next level: every dead player is revived at the start. After level 3 cleared: win screen. (user)
- Dead players float as ghosts and watch (they stay in play, gameplay-anti-patterns #2). (Claude)

## Level order (Claude)
3 levels from 2 minigames: 1 = The Gauntlet, 2 = The Crusher, 3 = The Gauntlet, harder (faster
and more pendulums, less time). The user said 3 levels and 2 minigames; the third reuses one.

## Minigame 1: The Gauntlet (Claude)
A walkway (4 m wide, ~36 m long) over a spike pit; the audience watches from the side.
- **Grinders**: 3 walls of spinning blades across the walkway. A grinder stops only while
  someone stands on one of its two plates (2.2 m before it and 2.2 m after it). Walking into a
  running grinder: shredded to gibs.
- So nobody crosses alone: the first across a grinder needs a friend on the near plate; once across,
  they can stand on the far plate to let the friend through. A relay.
- **Scythe pendulums** (3; hard: 5) swing across the walkway between grinders. Hit: cut in half.
- **The pit**: fall off the side: impaled on spikes.
- **Clear**: everyone alive is past the finish line (safe there). **Time up** (80 s; hard: 70 s;
  once anyone is across, the rest have 25 s): the Reaper beheads everyone not across. Cleared if
  at least one made it. Last runner alive: plates hold 3 s after stepping off. Walk back past the
  finish and you can die again.

## Minigame 2: The Crusher (Claude)
A square cage (14 m). A spiked ceiling comes down over 75 s (it crushes at 1.9 m, ~59 s in).
- **Levers** in the 4 corners. Hold E at a lever. When enough levers are held at once
  (half the crew that started the level, rounded up: 3 -> 2, 6 -> 3) for 8 s in total, the
  ceiling stops. Progress drains 0.4/s while too few hold. A lever held 6 s burns out and locks
  for 4 s: swap to another.
- **Saw blades** sweep 3 lanes; two lanes run through the lever corners, every holder stands in
  a saw's path: let go, dodge, get back. Hit: cut in half.
- **Clear**: the ceiling stops (everyone alive clears). **Fail**: it reaches the bottom: everyone
  left is crushed flat -> the team loses.

## Deaths (user: brutal, lots of blood; Claude: the forms)
| Cause | What you see |
|---|---|
| Pendulum / saw | cut at the waist, top half flies, both halves spurt |
| Grinder | burst into gibs and a red mist |
| Pit | skewered on spikes, fountain |
| Time up | head flies off, neck fountain |
| Crush | flattened, gibs out the sides |
Blood: particle bursts, fountains, splat decals that stay on the set until the next level.
Option "Gore" off: dark smoke instead (Claude).
Crowd cheers and gasps on every death; the feed names who died and how (blame with a name).

## Other picks (Claude)
- Name: "Deathly Reality Show" (user). Alternative held: "Reaper Ratings".
- Solo and 2 players can start (for testing), with a warning.
- No shop, no upgrades, no score between levels; the report card at the end lists deaths and clears.

## Critic round 1 (2026-11-07): antithesis -> synthesis
An isolated critic agent attacked every (Claude) pick (rule: AFK builds, `~/.claude/CLAUDE.md`).
What changed (all (Claude), numbers in `tuning.gd`):
| Critic finding | Synthesis |
|---|---|
| Crusher trivial (4 s hold, saws miss holders) | holders stand inside a saw lane; levers burn out (6 s) and lock (4 s), so you must swap levers across the saws; 8 s of enough levers held. Checked by simulation (`tools/crusher_check.py`): two perfect players clear 200/200 phases, median 32 s of 59. The first numbers (4 s burn / 5 s lock) were unclearable even with perfect play. |
| Crusher got easier as people died | levers needed = half the crew that *started* the level (3 -> 2, 6 -> 3), fixed: deaths cost |
| Lone Gauntlet survivor soft-locked | last runner alive: a plate keeps its grinder stopped 3 s after they step off |
| Safe players invulnerable, could escort | walking back past the finish line makes you killable again |
| Hard pendulums inside plate zones | course rebuilt: grinders at z 10/0/-10, pendulums >= 1.5 m from every plate edge |
| Blame went to the victim | a grinder death names whoever stepped off that plate in the last 2.5 s ("Backstabber" award) |
| Timer didn't press; pendulums learnable | first one across -> everyone else has 25 s; pendulum phase random per show |
| Spawned inside a saw lane (found in testing) | Crusher spawn is a row on the safe strip |
Not taken (in `todo.md`): server-side position checks (friends-only game), ghosts doing something,
disconnect edge cases, a different level 3, a cost carried across levels (frame thesis B).
