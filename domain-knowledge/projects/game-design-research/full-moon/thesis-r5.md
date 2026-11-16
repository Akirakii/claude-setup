# Full Moon: thesis r5 (Claude, 2026-11-11): answers to the user's 7 questions

Builds on `design.md`. Only the new or changed parts are here.

## User's questions (their words)
"what happens if the time runs out on the creature? what the humans should do when a creature gets converted? what
happens if the human about to be converted doesnt want to cooperate and wants to hunt? what happens if a creature wants
to cooperate with humans and decide not to hunt? how long should a conversion take? is it alwasy the same time? time to
convert and time to stay as creature. what should players do after the night? does it skip time? what creatures should
we define apart from werewolf and vampire? i dont like zombie"

## Hole found in design.md
Since r4, a starved creature wakes free at dawn. So on nights 1–4 a friendly creature's best play is to stand in a
corner and starve: no candle spent. A crew that plays to win agrees "creatures never hunt" by night 2, and the chase
(the costliest thing to build) only happens on night 5 or with a griefer.

## New rules (all Claude)
1. **The curse pulls (fixes the hole).** A turned creature's body is pulled toward the nearest person, gently at first
   and harder as its HUNGER runs out. In the last 10 s, touching anyone grabs them on its own. A creature that wants to
   hunt goes with the pull (faster); one that wants to spare its friends steers against it. Everyone sees it strain
   ("I can't hold it, run!"). A creature that holds out until it starves still saves the candle.
2. **Out of time.** The creature collapses into a deathly sleep: a ghost until dawn (talks, pushes loose objects, sees
   who is sick), then wakes human for free (nights 1–4). On night 5 there is no dawn after, so a starved creature loses.
3. **Wants to turn on purpose.** Allowed. They can hide an inner first sign for stage 1, but outer signs and veins come
   at stage 2, ghosts see the veins, and friends can grab, pan and force-feed them. If they turn and catch someone, the
   victim needs a candle. At dawn the living choose who comes back, which is the social payback.
4. **Case length varies.** Each case lasts a random 60–90 s on night 1, shrinking to 50–75 s on night 5. Cure odds and
   the veins follow how far along the case is (its share of its own length), not seconds, so counting seconds doesn't help.
   The odds curve is the same: 95% at the start → 30% at the end, fastest early.
5. **Creature time.** HUNGER = (20 s + 60 s ÷ people left to catch) × the creature's own factor: werewolf ×0.75 (fast,
   short), vampire ×1, troll ×1.25 (slow, long). The creature's body shows its hunger (it thins, its eyes dim).
6. **After the night.** Dawn is a ~60 s scene in the hall: candles bring back the caught (the living choose if there
   are too few), the moon's omen shows tomorrow's likeliest creature, spare candles buy a third cure bed or tool. Then
   the day is skipped ("Night 2. The moon is fuller."). Each night starts with every cure regrown, tools at new random
   spots, scars kept, and ~20 s of calm before any case. Run ≈ 5 × 6 min + 4 × 1 min ≈ 34 min.
7. **Third creature: troll, not zombie.** The troll takes the zombie's exact sign column, so the sign table and its
   computed leans don't change: lamps hurt (sunlight turns trolls to stone), grey stony skin, cold, craves raw meat,
   drools. Its cure is **rowan** (rowan wood wards off trolls in Scandinavian folklore). All three cures become plants
   (wolfsbane, garlic, rowan): the garden is the pharmacy. Spots: wolfsbane ×2 (garden beds), garlic ×2 (kitchen,
   cellar), rowan ×2 (the tree house's own tree, the hedge maze). The tree house gets a reason to exist (U1).
   Full-game powers (one each): werewolf fastest and tracks footprints; vampire flies to the tree house and avoids lit
   rooms; troll slow, breaks doors, freezes in lamplight. So "lamps hurt" (the sign row vampire and troll share) is
   also what keeps both of them back.
8. **More creatures later (full game).** Candidates: gargoyle (moves only while nobody looks at it: a co-op chase
   where someone must keep watching), fae changeling (iron; pointed ears; craves milk and honey), banshee (you hear
   crying; a wail that stuns). A 4th creature means redrawing the sign table so each sign still leaves a small group
   (check it with a script); each night would then use 3 creatures from the roster, which the omen hints at.

## What humans do when a friend turns (from design.md, unchanged)
Everyone now sees all of its signs, so they know what it is. Grab its cure, stand in pairs back to back (one cure
shoves, then waits 3 s), keep the unarmed between the armed, break a catch within 2 s by shoving, and make it starve.
New: use its weakness (lit rooms against vampire and troll; outrun the slow troll).
