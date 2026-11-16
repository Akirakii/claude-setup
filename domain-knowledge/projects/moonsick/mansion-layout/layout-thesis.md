# Thesis: the mansion layout around the potion (2026-11-15, Claude)

User: "lets redo the layout so the cauldron potion making is centered and more important with a cartel that says the
ingredients needed", then "should cauldron be at center? or should we have a room that is straight from the hall",
then "why barbershop?" (no reason left: razors are carried and never run out), "why bombs at library?" (no reason),
then "run a subagent to super review the sketches".
Sketches: scratchpad plan.png (A), plan2.png, plan3.png, plan4.png (B, latest). Design: docs/redo-ideas.md.

## The problem underneath
The potion is the game's one turning point (user), but it sits in a side room upstairs nobody passes. The layout
must make the potion visible and contested: builders need some cover to finish it sometimes, while the leader (the
furriest, who dies at 4:00 if the potion exists) and betrayers must be able to reach it in person and be seen doing
so (healthy sabotage, docs/redo-ideas.md: no direct sabotage; only knockdowns, stealing, killing rats).
The same map must also work for the 3-minute hunt (running loops, jump-downs).

## Fixed facts (built or user-decided)
- 4–8 players; MVP test crew is 1 human + 3 bots. Sprint 8.64 m/s, walk 4.32; werewolf 1.3x sprint (11.2 m/s).
- Night 4:00 (moon overhead: furriest turns); hunt 3:00. Fur 0→100% in 120 s; start 0–30%.
- Potion: wolfsbane (regrows 45 s after use) + a rat (3 roam; wriggles free after 20 s in hand) + moon water
  (bucket fills by itself in 120 s while in the moonbeam) in the cauldron, then 2 players hold F for 10 s within
  2.2 m. Flask pops out for anyone; thrown, 2.5 m splash cures the werewolf. Brewing allowed during the hunt (user).
- A knockdown drops what you hold. Bombs 6 m blast. Pans/mallets break on hit. No cooldowns.
- Bots don't use jump-downs (no nav links).

## Answers
- **A. Cauldron on a raised platform in the middle of the great hall**, sign above, open on all sides.
- **B. A cauldron room straight off the hall (recommended)**: north end of the hall, centred, double height,
  6 m wide arch onto the hall with the potion sign above it, a back door toward the kitchen side, a high window from
  the attic side (watch, or jump in). Footprint ~9 x 7.5 m.
- **C. Cauldron upstairs on the north balcony overlooking the hall**: visible from below, reachable only by the
  ramps/back stair; sabotage by jumping up is impossible, so the leader must climb.

Layout B in full (map ~46 x 28 m, two floors, ground y 0, upper y 4):
- Ground: kitchen NW (pans; back stair up), cauldron room N-centre, pantry NE (rat nest: rats live and respawn here;
  shelves and sacks; a hole from the attic drops in), conservatory SW (mallets, wolfsbane; open sky), great hall
  centre (double height, pillars, sofas, twin ramps to the south gallery), witch's study SE (shelves of potion
  bombs; replaces the library). Doors: each side room 2+ exits; corridor ring around the hall.
- Upper: storeroom NW (bear traps; back stair down), attic NE (moon-water bucket in a moonbeam; hole down into the
  pantry; high window into the cauldron room), secret bookshelf tunnel behind the cauldron room joining storeroom and
  attic, balconies on three sides of the hall (north balcony over the sign; jump-down gaps), south gallery where the
  ramps arrive.
- Trips to the cauldron at sprint (Claude's estimates, straight-line + doors): rat from the pantry ~12 m (1.5 s +
  catching), wolfsbane from the conservatory ~22 m (2.5 s), moon water from the attic via the gallery ramps ~45 m
  (5–6 s) or the window jump ~8 m (1 s + 4 m drop).

## Scenes
- 1 human + 3 bots (fewest): the human must do the potion mostly alone: bots only come to stir when someone stirs
  (built); bots don't fetch ingredients (built). The human fetches a rat (pantry next door), wolfsbane, the bucket
  after 2:00, then stirs with a bot at ~2:30. The furriest bot doesn't sabotage (bots don't), so with bots the potion
  is free once the bucket is full.
- 8 players (most): 3 builders split jobs; the leader watches from the north balcony, jumps down at the stir;
  others pass through the hall constantly; the pantry is fought over for rats; the attic bucket is carried off once.

## Pillars
- Keeps: the one line ("grow into the werewolf first while everyone tries to shave you back to human"), healthy
  sabotage (in person, seen, recoverable), the hall as a running space.
- Bends: the potion's rarity now depends on players interfering, not the clock (user OK'd: reachable when uninterrupted).

## Merge (filled after the critic)
Critic: `docs/critic-layout-r1.md`.

| Finding | Decision (Claude's proposal; waits on the user) |
|---|---|
| S1 Ingredients stay in the cauldron for good: rat and wolfsbane go in by 0:15, then the pantry and conservatory are dead | A rat in the cauldron climbs out after 20 s unless the stir has started, so the rat goes in last and the pantry stays live |
| S2 The bucket fills only in the attic moonbeam; the leader can carry it off unseen, and only a 2-minute guard stops that | Move the moonbeam onto the north balcony over the potion sign, in plain sight of the hall; the bucket shows its water level |
| S3 With 1 human + 3 bots nobody sabotages, so the potion is free at ~2:14; the stir call reaches bots only within 20 m | The furriest bot sabotages (knocks down whoever carries an ingredient or stirs, grabs it, runs); every bot answers a stir call |
| M Two stirrers fit in one 6 m bomb; bombing them is the leader's always-win | A knockdown pauses the stir instead of resetting it; it resets only after 5 s with fewer than two stirrers |
| M Rats respawn only in the pantry, so one bomb kills all three | Rats respawn at random points across the ground floor |
| M Thesis distances wrong (rat trip 22 m, window route 17 m); sketch and thesis disagree on exits and names | Fix the numbers; add a door from the pantry into the cauldron room |
| M In the hunt no loop beats a 1.3x werewolf; items decide | Kept: the humans' answer is items and the potion, by design |
| M Stirring during the hunt is a death spot (standing still 0.5 s = edible) | Kept as a risky, heroic choice; the 2.5 s knock-down-then-eat window gives a partner time to react |
| M The "rare" pillar's bend isn't recorded | Record the user's yes ("reachable when nobody interferes") in redo-ideas.md |
