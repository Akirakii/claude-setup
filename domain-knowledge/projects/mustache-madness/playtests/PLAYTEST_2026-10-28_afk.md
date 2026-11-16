# PLAYTEST 2026-10-28: AFK for 10 nights

Source: `logs/godot.log` and the rotated logs from 15:15 to 15:26 (save `2026-10-28T15-15-28`),
BALANCE_TICK and PERF lines. A day lasted about 66 s of wall time and a night about 19 s.

## What happened
- Day 0 to night 2: the player is away. The starter herd of 3 breeds and a boat brings a
  pair each dawn: 6 by day 1, 9 by day 2.
- Night 3 (siege 1): 1 beast (budget 6) against 9 friends. It is downed in about 3 s.
- Days 3 to 6: the herd grows 14, 20, 23, 28. Nobody builds; 14 are hungry and 14 tired
  at a time, but no one snaps (snaps 0).
- Night 7 (siege 2): 12 beasts (budget 24) against 28 friends. All 12 are down within
  about 10 s; no friend is downed.
- Days 8 to 10: old age starts to take friends (13 by day 10), births keep pace. Day 10 ends
  at 34 friends; the next siege is night 12.

## What the story shows
- The herd grows on its own with no player: 33 births and about 9 boats in 9 days, so the
  herd outnumbers every siege 2 to 9 times over.
- A siege never reaches a friend or the statue: losses 0, ally downs 0 over the run.
- Unmet needs cost nothing that shows: hunger and tiredness ran unchecked for days with no
  snap, no loss, no fall in the herd.

## Changes made (Claude's picks unless tagged)
- Boats call on half the dawns (`PierConfig.BOAT_CHANCE` 0.5) (user: not every day).
- Births halved (`BREED_PACE` 8 to 4) (user: half the new creatures).
- Beasts 1.5x health and damage; siege budget factor 2 to 3 (user asked for stronger beasts).
- Creatures harder to handle: not built yet, sketched for the user.
