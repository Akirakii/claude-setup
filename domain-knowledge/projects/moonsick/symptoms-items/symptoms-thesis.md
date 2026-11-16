# Symptoms thesis r1: what a sick friend shows, and the item that treats each (Claude, 2026-11-13)

## The user's words (verbatim, 2026-11-12/13 chat)
- "im thinking the symptomps should define the cure.. perhpas players has to cook a potion with different ingredients"
- "should be like a potion with combined things and one final product? or should be like applying multiple items and
  solving the need of the infected and progressing until fully cured" → Claude recommended item by item → user: "then
  potion is not needed and less ways for a funny moment to mess up"
- "hunger and drooling is mixing.. perhaps no hunger" · feelings must be ones "only the sick" can feel ("how only the
  sick plyaer can see fleas or itching without anyone noticing.. weird") · "headache is not good since it can be
  interepreted as the transformation is about to happen" · "sleepness could be.. but the problem is that the player
  blinking is something everyone can see.. but i like that idea.. add sleepness" · "nausea should be one example" ·
  "freezing cold again.. that is something that others can notice" (cold dropped)
- 2026-11-13: "lets proceed with the design of symptons and items for the sick at moonsick game"
- Open from that chat: keep sleepiness as a third feeling next to double vision, or replace it.

## Decisions since r1 (2026-11-13 chat; they override the table below)
- Origin of the table: every symptom and item was Claude's first draft, except sleepiness (user: "add sleepness")
  and nausea (user: "nausea should be one example"). Glowing eyes, bloodshot eyes, fur and drooling were never
  confirmed or rejected by the user. Double vision was Claude's; after this file was written, the 2026-11-12 chat
  dropped it and Claude proposed a werewolf nose (smell trails on your screen, fixed by a clothespin), never answered.
- **Removed (user):** double vision + eyepatch ("double vision should be removed. i didnt add that"), cucumber
  slices, and wolfsbane from the item list ("remove als owolfsbane": from the game or only the list is unasked).
  Bloodshot red eyes removed too (user: "remove this one: bloodshot red eyes"), so glowing eyes is the only eye
  symptom left.
- **Sleepiness is seen by others (user):** "sleepiness is not fully private.. one can see the eyes".
- **Private symptoms parked (user):** "thinking about private symptoms is difficult lets skip for now".
  Claude's hallucination idea (the patient sees things that aren't there) waits with them.
- **Big shared items, no handles (user OK):** some items need two people: grab anywhere, alone you can only budge
  it, two lift it (`docs/items-research.md`). Claude's picks for which items (a pot of hot wax for fur, a giant bone
  for drool) were rejected: "those big items doesnt make sense". The user is choosing which current items get bigger.
- **Added: wet-dog stink → perfume (user OK, 2026-11-14; both were Claude's ideas):** green stink lines and buzzing
  flies around the patient, seen by others; a spray of perfume fixes it (user: "stink and perfume is good add that").
  Room not picked.
- **Walking on four legs → granny walker (user's symptom; item Claude's, user OK 2026-11-14: "granny walker is
  funny"):** the walker makes them stand up and shuffle; it's naturally big. Room not picked. Watch: it must not look
  like the turn (the werewolf model is hunched; assumed it stands on two legs).
- **The awoooo (user's idea, 2026-11-14):** fails "looks like the turn" as is: the turned werewolf's power is a howl
  (`design.md` "Werewolf howl") and a wrong item already plays a short howl. Claude's fix: the sick awoo is the
  friend's own voice cracking into a small, short "awoo-oo"; the werewolf keeps the big deep howl. User OK: "normal
  awoo instead of the special turned werewolf".
  Item (user, replaces Claude's pacifier): a dog cone, "that item should never have penalty". The penalty meant the
  wrong-item jump; the user then said "no nevermind.. i thought that giving wrong item accelerates the process"
  (it does: `design.md` "A wrong cure jumps the case a third ahead", and this draft's +0.2). Open: does the cone
  skip the jump? Claude's pick: yes, since the awoo is heard more than seen, so the crew will often cone the wrong
  friend.
- **No penalty for any item in step 1 (user asked "should we make all items no penalty?"; Claude's pick, user:
  "proceed", 2026-11-14).** This replaces the +0.2 wrong-item jump below. A wrong item skips the curse jump but keeps the slapstick burst (shows who messed up) and is used up
  (the lost trip is the cost). Catch: an item given before its symptom shows does nothing, or everyone wears
  sunglasses and a cone from the start. The jump is also how a liar would speed a turn, so it may come back when
  lying does. The dog cone question above is settled by this. Case against (Claude): real cones stop licking and scratching, not howling, so it's less obvious than bone
  for drool. Watch (Claude): with no penalty, everyone could wear one from the start; Claude's fix is that it falls
  off once the awoo is cured.
- **Built (user: "implement all items and symptoms", 2026-11-14; untested by the user):** all eight symptoms and
  items, as `docs/design.md` "Symptoms and their items" says. Claude's picks in it: answer A's pacing (the user
  never picked an answer), the perfume, walker and cone rooms, nausea shown to others (retching, a green face)
  while private symptoms are parked, worn items staying on until the case ends, and the bots' split.
- Answer A's case shape fails the co-op check (one player can handle every case alone for the first two thirds of
  the night) (Claude, 2026-11-13).

Context: step 1 (`docs/design.md` "Step 1 cuts"): werewolf only, no screen UI, no world text, tools/pans/tricks/
doubles off, bots slower (user). Hands: `docs/hands-thesis.md` synthesis r3 (one button per hand, give 2 s, raise
wolfsbane when a creature is out). Code facts used below [read]: rooms are a 3×2 grid of 10 m rooms
(x −15…15, z −10…10), garden south (pond z 24, tree 14,34), `mansion.gd:35`; sprint 8.64 m/s (`move.gd`);
`CASE_LEN` 75 → 60 s and `HELD_RATE` 0.5 (`curse_rules.gd:35-39`); spot `REGROW` 120 s (`night_sim.gd:32`).

## The problem underneath
The user chose obvious fixes (drool → bone), so "which item?" is never the question: with one monster there's
nothing left to deduce. Sims on the real map (`docs/sims/`) show a human fetches and gives any item in ~10 s.
So a case that shows one symptom at a time **can't be lost**: 0% turns for a lone player even at 20 s between
symptoms (`symptoms_sim.py`). The tension has to come from **more needs at once than one pair of hands can meet**,
and the design choice is where those needs come from. Readability (the user's main complaint) has to survive it.

## The table (shared by all three answers)
Seven symptoms in three groups; a case gets one from each group. Every fix is common sense, so nothing needs text.
| Group | Symptom | Who notices | Item | Where | After |
|---|---|---|---|---|---|
| Eyes | glowing yellow eyes (self-lit, seen in any light within 10 m) | others | sunglasses | hall coat rack | wears them |
| Eyes | bloodshot red eyes (red whites, big, within 6 m) | others | cucumber slices | conservatory | slices on the eyes 3 s (they can't see) |
| Body | fur sprouting on neck and face | others | razor | study desk | shaved in patches |
| Body | drooling: long strings, a puddle, a slurp heard within 6 m (not by the patient) | others | dog bone | garden doghouse | chews it 3 s |
| Feeling | sleepiness: your view fades to black and snaps back, a yawn | the patient; others see small yawns | coffee | kitchen | sips |
| Feeling | nausea: green tint, wobbling screen edges, a gurgle only you hear | the patient only | bucket | cellar | throws up into it |
| Feeling | double vision: a faint ghost copy of the view, offset sideways (static, no sway) | the patient only | eyepatch | dining room | wears it |
- **Sleepiness and double vision both stay (Claude).** With only sleepiness and nausea, half of all feelings would
  show through yawns; with three, two in three are fully private, so the patient's word matters more often.
- **Fur moved off the hands (Claude):** hands show in first person while reaching (hands r1 #22: the mitten never
  takes skin, veins or claws), so fur sits on neck and face, where the patient can't see their own.
- **Telling a feeling without text or voice (Claude):** keys 1–3 act it out, a gesture and a sound everyone near
  sees: rub your eyes and yawn (sleepy), hold your belly and gag (nauseous), cover one eye (seeing double); 4 is a
  thumbs-up ("I'm fine"). Bots use the same gestures, so it works with the user's test crew. Anyone can act out a
  lie. This replaces the quick-chat bubbles that `world_text` already hides.
- **Wolfsbane stops being a cure.** It stays the shove against a turned werewolf (raise). Given to a patient it's a
  wrong item.
- **The % per sign (user pillar)** = which symptom of its group a case gets: eyes 50/50, body 50/50, feelings 1/3
  each (Claude, equal for now).

## Rules shared by all three answers (Claude unless tagged)
- **Curse c, 0 → 1, one number per patient.** It rises R per second for each showing, untreated symptom. At 1 the
  friend turns (today's turn and hunt rules). Shown on the body: veins on the neck at c ≥ 0.33, on the face at ≥ 0.66;
  the patient hears the heartbeat at ≥ 0.66 (the user's "about to turn" signal; nothing else uses it).
- **Treat:** give the matching item (the hands' give: 2 s, friend still or held). That symptom ends at once with its
  "after". When all three are treated: cured (c drains to 0 in 3 s, 60 s before they can get sick again: today's skip).
- **Wrong item:** c jumps +0.2, a slapstick burst on the spot (ears pop out, a short howl), the item is used up.
  Everyone near sees whose item it was. On a healthy friend: harmless and used up (they wear the sunglasses).
- **Nobody treats themselves** (today's rule; last one alive excepted). The patient may fetch their own items and
  hand them to a friend to give.
- **Holding:** the curse runs at ×0.75 while held (was ×0.5: the sim shows ×0.5 makes a held patient never turn,
  0% at every setting; ×0.75 still matters: see answer A's table).
- **Items:** each spot holds 2; a used item comes back to its spot 60 s later (was 120 s for herbs).

## Three different answers

### A. One friend at a time; the needs bunch up as the night goes on (recommended)
A case is as today: one random friend. Spacing S between their three symptoms (random group order) and the rate R
slide with the night fraction f (0 at dusk, 1 at dawn): **S = 30 → 8 s, R = 1/120 → 1/40 per second per symptom.**
Ignored, a case turns ~70 s after its first symptom at dusk, ~18 s at dawn. Case gaps: today's formula.
Doubles (user: "two at once, rarely") come back for the last third of the night, 20%, only while ≥ 6 are alive, so
big crews get a second patient and small crews never do (critic memory: scale needs with crew size).

Sim (`ramp_sim.py`; perfect assignment of runners, hold ×0.75; % of cases that turn):
| Night f | S | R | 1 human | 1 runs + 1 holds | 2 run | 2 run + 1 holds | 3 run | human + 3 bots (17 s late), a bot holds | human sick, 3 bots (6 s late) |
|---|---|---|---|---|---|---|---|---|---|
| 0–0.65 | 30–16 s | 1/120–1/68 | 0% | 0% | 0% | 0% | 0% | 0% | 0% |
| 0.8 | 12 s | 1/56 | 20% | 0% | 6% | 0% | 8% | 0% | 30% |
| 1.0 | 8 s | 1/40 | 95% | 26% | 87% | 4% | 71% | 38% | 89% |
- What it hides: which symptom comes next, the felt one (only the patient), and how late it is (veins).
- Decisions: who runs where (split by where you stand), who holds, what you carry in your two hands between cases
  (wolfsbane for the hunt or two treatment items for the next case), believe a gesture or not.
- Early cases teach the table and can only be lost by ignoring them; the last fifth needs a holder and two runners.

### B. Symptoms land on anyone (spinning plates)
No cases. Each living friend gets a new symptom every I0 ≈ 40 s on average, in a group they don't have showing.
Each friend's curse rises R = 1/60 per untreated symptom and drains at R while they have none; at 1 they turn.
Everyone is a patient and a helper at once, and nobody can treat themselves.
Sim (`spin_sim.py`): turns per 10 min: 4 humans 0.87, 6 humans 1.32, 8 humans 1.52; 1 human + 5 slow bots 7.1
(the bots drown). At I0 25 s: 3.1 / 4.1 / 4.5.
- What it hides: everyone's felt symptom; decisions: whose symptom first, trade help ("shave me, I'll get your
  coffee"), when to stop helping and get yourself treated.
- Against: bends "a random player starts turning every now and then" and "fully cured" (nobody is ever done);
  many symptoms on many people at once is the least readable; a turn kills someone, so a losing crew spirals.

### C. Everything at once, three runners needed (an order rush)
A case shows all three symptoms within 10 s (S = 5 s) and R = 1/40: ignored, it turns at 18 s. All night.
Sim (`burst_sim.py`, hold ×0.5): 1 human 92% turn, 2 run 64%, 3 run 20%, 1 runs + 1 holds 0%.
- What it hides: almost nothing (all three show at once); decision: split three items between runners.
- Against: a cliff, not a curve: one runner always loses, a holder makes it unlosable; nothing to learn on the first
  cases; the user's "too fast to follow".

## Scenes (answer A)
- **Fewest players (the user's test: 1 human + 5 bots, practice, 6 min):** 0:40 bot Bo's eyes glow yellow in the
  dark hall (two lamps). You take sunglasses from the coat rack 4 m away and give them (2 s): Bo wears them. 1:10
  Bo rubs his eyes and yawns (gesture): coffee, kitchen, 12 m. A bot sets off 17 s later; you're back first.
  1:40 fur on Bo's neck: razor, study. Cured at ~1:50 (c ≈ 0.3). 3:30 your own view turns green (nausea): you press
  2, a bot brings the bucket from the cellar ~25 s later; meanwhile a bot comes at you with sunglasses (your eyes
  glow, you couldn't see it). 5:20 (f ≈ 0.9) bot Cy: drool, 10 s later red eyes, 10 s later a cover-one-eye
  gesture. A bot holds Cy; you run for the bone; one bot gets cucumbers; nobody has the eyepatch yet. Turns at 5:45?
- **Most players (8 humans, 10:30, f ≈ 0.88, S ≈ 11 s):** Ana: red eyes, then drool, then she holds her belly.
  Dan grabs her. Cleo runs for cucumbers, Ed for the bone, Fay down to the cellar. Bo is carrying coffee and a razor
  (the wrong two) and argues. A double (≥ 6 alive) starts on Gus in the kitchen: glowing eyes, and the sunglasses
  are at the far end of the hall. Two guard with wolfsbane up in case either turns.

## Pillars
- **Kept:** one night; dark; a random friend starts turning now and then (A); the % per sign (which symptom per
  group); holding slows the turn (weaker: ×0.75); a turned friend must catch or starve, a catch = a cure; betraying
  never pays more than curing (a wrong item only hurts, no reward); bluff from both sides (act out a false feeling;
  give a wrong item on purpose, seen by all); no reveal; the reel (wrong-item slapstick is reel material); two at
  once but rarely (A: late, ≥ 6 alive).
- **Bent:** "the cure works only if the diagnosis is right, and then with a % chance" → the right item always
  works, the risk moves to time. "Signs always different and hard to read" → easy to read, hard to keep up with;
  7 symptoms make 12 combinations. "Tools are needed to diagnose": still off. "A sick player can lie about what they
  feel": now by gesture. The core-thesis choice ("cure now on one sign or wait") is gone: nothing left to deduce.
- **Dropped:** herbs as cures (wolfsbane = shove only); the old signs (night sight, craving, grey skin, drool as a
  vampire/troll tell) and the cure-odds formula, until vampire and troll come back.

## What this changes in the code (for the size, not built)
curse_rules.gd (table, c, S/R ramp), night_sim.gd (per-symptom treat, wrong item, item kinds, 2 per spot, 60 s
return), mansion.gd (7 item spots), body.gd (eyes, fur, drool, worn items, gestures), player.gd (3 screen effects),
bot.gd (notice, fetch, gesture), hands (any item gives; wolfsbane raise unchanged), 7 item models (Meshy or code).
