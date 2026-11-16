# Critic round 1: the mansion layout (layout-thesis.md, layout B / plan4.png)

Isolated critic, 2026-11-15. Numbers from `scratchpad/lay.py` (sketch scaled to 46 x 28 m; sprint 8.64, wolf 11.2,
gravity 12 so a 4 m drop is 0.8 s) and the code (brew.gd, brain.gd, world.gd, actor.gd, rules.gd). Checked = read in
code or computed; (assumed) = not checked.

## Verdict on the problem underneath
The stated problem ("make the potion visible and contested") is right, but the layout can't create a contest the
rules have already removed. Two built rules decide it, not the rooms:
1. Ingredients put in the cauldron stay forever (checked: `spill()` is never called; `hit_cauldron` does nothing).
   So the rat and the wolfsbane go in during the first ~15 s, and the pantry and the conservatory stop mattering
   for the rest of the night. The only contested things left are the bucket (120 s clock) and the 10 s stir.
2. The test crew can't play the contest at all: bots never sabotage or fetch, so with 1 human + 3 bots the potion is
   free (checked in brain.gd).
Fix these before tuning rooms; otherwise layout B is a nice picture of a contest that doesn't happen.

## Severe
S1. **Front-loaded ingredients kill the pantry and the conservatory.**
  Example: a builder grabs a rat at 0:05 and wolfsbane at 0:10 and drops both in. From then on, "the pantry is fought
  over for rats" (thesis, 8-player scene) never happens; the rat nest next to the cauldron has nothing to do.
  Fix direction: the rat has to go in last, e.g. a rat in the cauldron climbs out after 20 s unless the stir has
  started, so the rat fetch becomes the final sprint (pantry next door finally matters). Or ingredients spoil if the
  pot isn't stirred within N s. Either one adds a rule: count it.
S2. **The clock item sits in the least-watched room, and taking it is silent.**
  Checked: the bucket fills only within 1.3 m of the moonbeam. The leader picks up the half-full bucket and drops it
  down the attic hole into the pantry, or carries it off; the fill pauses and nobody on the ground sees it.
  This fails "seen" (healthy sabotage). The only counter is a builder standing in the attic for 2 minutes
  (anti-pattern B24, standing in places). The secret tunnel makes the approach even less visible.
  Fix direction: put the moonbeam where the hall can see it: on the north balcony above the sign, or a skylight
  inside the cauldron room; show the fill on the bucket (glow level), so a missing bucket is noticed.
S3. **Nothing in the test crew plays sabotage, so nothing about this layout can be tested.**
  1 human + 3 bots: the human drops rat + wolfsbane early, waits until 2:00, carries the bucket (window route 17 m,
  2.8 s), stirs; bots join only if they're within 20 m of the cauldron (checked). Potion at ~2:14, with 106 s of
  night left. A bot "pass" here is a warning, not a result (B23, critic note "voice-only game tested with bots" x6).
  Also a deadlock risk: the SW/SE corners and the far hall are 22–35 m away, so if every bot is fleeing there, the
  stir never starts and the human waits forever (critic note "test setups that deadlock").
  Fix direction: the furriest bot gets one sabotage verb before the layout is judged (grab the bucket out of the
  beam, or throw a bomb at two stirrers); the stir call reaches every bot, not 20 m.

## Medium
M1. **Two stirrers always fit in one bomb.** Stir range 2.2 m means stirrers are at most 4.4 m apart; a bomb blasts
  6 m. The study is 21 m (2.5 s) from the arch; the north balcony looks down into the open-topped cauldron room 4.9 m
  from the pot; a thrown bomb lands ~14 m away. So the leader's always-win line: hold a bomb on the north balcony,
  drop it on any pair stirring. 3 bombs, 20 s respawn, so the leader never runs out.
  Too exposed to bombs, fine against melee (arch + back door + window: no fortress for builders).
  Fix direction: stir range > 3 m so stirrers can stand on opposite sides and a bomb takes only one (a real
  positioning choice), or roof the cauldron room (no perch; keep the window from the attic).
M2. **Rats all respawning in the pantry is a spawn camp.** Built: rats roam the whole ground floor. The thesis moves
  their home and respawn into one room, so one bomb (6 m) kills all three every 30 s, and the study is 3 s away.
  This change isn't tagged. Fix direction: keep rats roaming; the pantry is where they're most common, not the only
  place, and respawn at random ground points.
M3. **Thesis numbers don't match the sketch.** The pantry has no door into the cauldron room, so the rat trip is 22 m
  through the arch (thesis: 12 m). Window bucket route 17 m (thesis: 8 m). Ramps 60 m, 6.9 s. Wolfsbane 27 m. Every
  trip is 2.5–4 s against a 120 s bucket wait: fetching is never the hard part, the bucket timer is. Also the sketch
  still says "Library", shows one door each for the conservatory and the library (thesis: 2+ exits each), and no ring
  corridor around the hall (thesis claims one); the side corridors dead-end at the outer wall.
M4. **The hunt: the map can't save anyone; items do.** The wolf closes 2.56 m/s: from 10 m it catches a runner in
  3.9 s (34 m of running). The hall–kitchen–cauldron-room loop is 30 m, so a loop buys one lap at most. A pan hit buys
  ~9 s (2 s down, 17 m head start, wolf closes again). So survival = item supply, and the bomb room and the
  conservatory are dead ends on the sketch: going for the best anti-wolf items is a trap. Fine if meant; say it.
  Jump-downs: a bot wolf can't follow (no nav links), so a human vs a bot wolf can loop ramp up, jump down forever
  (assumed: needs the nav detour measured). A human wolf jumps down after bots, who never use gaps.
M5. **Brewing during the hunt is a death spot.** Any stirrer standing still 0.5 s is edible (checked: `still_t`).
  The wolf reaches the cauldron from anywhere on the ground in ≤2.5 s, and from the attic by the window in 2.4 s.
  A 10 s stir needs ~3 knockdowns (each 2 s + 2 s wolf protection) from guards, so it only works with 6+ humans.
  Untaught: players will stand still to stir and get eaten. Fix direction: teach "keep moving" or let stirring
  walk around the pot (it already counts while moving within 2.2 m; say so on the sign).
M6. **The rarity pillar bends further than stated.** redo-ideas.md still says "meant to be rare" (user) and "moon
  water is the clock, perfect teamwork ~3:30". Uninterrupted, layout B gives ~2:14 (106 s spare). The thesis says the
  user OK'd "reachable when uninterrupted", but that OK isn't recorded in redo-ideas.md. With S1 and S2, the only
  interference left is bombs on the stir, so rarity rests on one weapon. Record the OK, or move the clock back.

## Minor
m1. **Secret tunnel fails the essence test.** The balcony ring already joins the storeroom and the attic at about the
  same length; the tunnel only adds a hidden way to the bucket (worse for S2). Cut it.
m2. **Potion sign.** Text above the arch is unreadable while sprinting and from the north balcony (behind it). Make
  it three picture slots (wolfsbane, rat, bucket) that light up as each goes in, plus "2 x F": one mechanism for
  teaching and state (critic note "decoration where the surface could carry rules"; visual-teaching-weakness note).
m3. **Traps moved from the attic to the storeroom, bombs from the potion lab to the study:** untagged moves. Traps
  don't stop stirring (a trapped player still counts, checked), so traps can only guard the arch/back door.
m4. **The flask after brewing.** Brewed at ~2:14, it must survive ~100 s of knockdowns until the turn; a thrown miss
  shatters it and the empty bucket needs 120 s more, so one theft ends the potion for the night. The layout gives the
  holder no place to hide it. Probably fine (stealing is allowed); say it in the scenes.

## Co-op check (building the potion)
1 Coupled: pass (the stir fails without a partner). 2 Split: fail (no split information or role; anyone fetches
anything). 3 Talk: fail for 0:15–2:00 (nothing to do but wait for the bucket), pass during the stir under bombs.
4 Blame: pass (a stirrer letting go is visible). 5 Not easy at fewest players: fail (bots, S3). 6 Not solo: fail
(one human does every fetch; the bot partner auto-joins). 7 Two-way: fail (the second stirrer only holds F: a pressure
plate; critic note "a timed joint press counted as coupling").
Most fails are the potion's rules, not the layout; the layout must not claim to fix them.

## Strategies that always win
- Builders: drop rat + wolfsbane at once, guard nothing until 1:55, one builder grabs the bucket from the beam, two
  stir at ~2:14 while a third pans whoever holds a bomb.
- Leader: carry the bucket out of the beam early (silent), or bomb the pair from the north balcony.
- Werewolf: chase the nearest; no loop beats 1.3x; avoid the knockdown items' rooms; a human wolf just jumps down.

## Pillars dropped or bent without saying so
- Rare potion (M6). Healthy sabotage "seen" (S2). Rats roam the ground floor (M2). Item rooms (m3).
- Kept: the hall as a running space, in-person sabotage (melee, stealing), brewing during the hunt (works only at 6+).
