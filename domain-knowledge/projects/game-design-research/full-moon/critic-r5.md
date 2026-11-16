# Full Moon: critic r5 (isolated critic, 2026-11-11)

Read: thesis-r5.md, design.md, ~/.claude/design-anti-patterns.md. Nothing played; all reasoning from the text.

## Severe
1. **Turning and starving on purpose buys a free ghost spotter.** · A starved creature becomes a ghost until dawn and
   wakes free (rule 2). Ghosts see the veins from second 0 of every case (design.md). So by night 2 a min-maxing crew at
   4–6 players lets one friend's first case run out every night. It costs them one pair of hands and a 24–40 s chase
   (HUNGER at 5 left × the creature's factor). In return they get: (a) every trick exposed on the spot ("no veins on Fae,
   it's the house"), which kills the "is that real or the house?" check, a core patient choice and a kill line; (b) every
   outer-first case spotted at 95% odds; (c) fewer cases, since GAP = 180 s ÷ *living* players and ghosts never get sick.
   The pull adds a little risk, not enough. This was already a hole in r4; r5's rule 2 keeps it. (Anti-patterns 17 and
   15; co-op gate: "dying on purpose makes it easier".) · **Fix:** the starved creature's "deathly sleep" doesn't see
   veins (only the caught, the real dead, do). It can talk and push things, but it can't spot. Then turning on purpose
   buys nothing but the cost.

## Major
2. **The pull's outcome depends on unstated numbers and on walls.** · If the pull points in a straight line, a creature
   that wants to resist puts a wall between itself and the nearest person and stays pinned there: the corner-starve is
   back. If the pull is stronger than the player's steering, the creature player is a puppet. If going with the pull adds
   speed on top of the creature's 1.2×, an unarmed person can't get away, so the hunt is decided before it starts. If
   resisting makes the creature slower than people, the nearest person can lead it around the house the whole time.
   Online: "touching grabs" by collision will feel unfair under lag. · **Fix:** pull along the walking path (navmesh),
   never through walls. The pull only bends the creature's direction and slows moves away from people; it never adds
   speed past 1.2×. Grabbing is the host checking a radius (~0.8 m) that starts the existing 2 s hold, so a shove can
   still break it and lag is forgiven. State a target: "a resisting creature that nobody acts on touches someone in ~60%
   of turns; a crew keeping 2 armed players is caught in <20%".
3. **"Hunt or hold back" is still a fake choice; the pull makes it a struggle, not a decision.** · On nights 1–4,
   starving beats catching every time: the crew has one fewer living player either way (the starver, or the victim) and
   only a catch costs a candle. On night 5, hunting always wins for the creature itself. The thesis's "social payback"
   isn't real either: a griefer who catches someone is human again, and "the living choose who comes back" punishes the
   victim, not the griefer. Co-op gate 7: the creature's side of the chase only resists. · **Fix:** give the creature a
   real decision with the pull: it picks *whom* to drag itself toward. Steering at an armed pair gets it shoved back
   safely while it starves; at the lone unarmed friend it's a risk. Teach that as the friendly play. Rewrite design.md's
   Choice line to match, and drop the payback claim (friends police griefers; force-feeding already handles them).
4. **Lit rooms make a fortress against 2 of the 3 creatures (full game).** · The vampire avoids lit rooms and the troll
   freezes in lamplight, so for vampire and troll turns the crew just stands in a lit room until the creature starves.
   The troll is slow *and* has the longest HUNGER (40–100 s), so a troll turn is a dull wait, and a lone survivor can
   outwalk a slow troll forever. Only werewolf turns stay a chase. · **Fix:** a few lamps only, and creatures can put
   them out (the troll smashes them, the vampire snuffs them from the doorway in 3 s). Make the troll slow to start but
   at people's speed once moving, or have it freeze only in a held lantern's beam (aiming is a skill and costs a hand).

## Minor
5. **More cure spots outdoors spoil the thermometer.** · 4 of 6 cure spots are now outside (garden beds ×2, the tree
   house tree, the hedge maze). Anyone back from fetching wolfsbane or rowan reads cold, so cold, the werewolf row's only
   tool sign, is mostly noise. The hedge maze is also a new level to build. · **Fix:** move one rowan indoors (a rowan
   branch over the hall hearth, or in the greenhouse). Garden cold only for the garden beds, or after 20 s outside. Drop
   the maze for Build A.
6. **Random case length leaves rules counted in seconds.** · The wrong-cure jump (25 s), the DOUBLE offset (10–30 s), the
   held-at-75 s wait and the computed scenes are all in seconds. When stage 2 appears it shows the case's length anyway.
   The veins already show progress, so the purpose is thin. Shorter night-5 cases stack on GAP ×0.6, doubles up to 30%
   and the slower regrow: about 2 points of cure odds lost per second at night 5. · **Fix:** turn the jumps into shares
   ("a third of the case"). Or simpler: one fixed length per night (75 → 60 s) with no per-case dice, which also answers
   the user's "is it always the same time?". Recompute the scenes.
7. **The troll mostly lines up, with 2 snags.** · Logic and look are good: sunlight to stone, grey stony skin, cold,
   craving raw meat, rowan. But (a) in folklore nobody *catches* trollhood from a bite, unlike werewolves and vampires,
   so "your friend is turning into a troll" needs a line of story (a troll's curse, a changeling). (b) Trolls are usually
   drawn with tusks, so "fangs when they talk" (the row that rules out the troll) can read as a troll sign. · **Fix:**
   make the troll's teeth flat and blunt, keep the fangs thin and needle-like, and add one line of story (the house's
   curse makes all three).
8. **The creature roster is scope creep for a 3–4 month solo build.** · A 4th creature breaks the 2-of-3 sign logic
   ("one sign leaves two"), the stage schedule and the journal. The gargoyle (moves only while unwatched) and the banshee
   (a stunning wail) are each a new system. · **Fix:** call it post-launch, not "full game". Ship 3 creatures, each with
   one power.

Verdict: the pull is the right direction once it follows walking paths and has a target; fix S1 (no vein sight for a starved sleeper) before building, since as written the best play is to sacrifice a friend every night.
