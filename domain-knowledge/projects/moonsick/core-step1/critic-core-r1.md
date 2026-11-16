# Critic: core thesis r1 (antithesis, 2026-11-12)

Target: `docs/core-thesis.md` (r1) against `docs/design.md` v2.4, the user's 13 points, pillars, pattern docs.
Tags: [ran] = computed by script; [read] = read in code/docs; [assumed] = not checked.
Scripts (scratchpad, not in the repo): `/tmp/claude-1000/-home-akiraki-claude-code/d3da34f0-115c-4b3f-9c35-cc389c307192/scratchpad/core_sim.py`
(sign leans, per-case strategies), `.../scratchpad/night.py` (whole nights), `.../scratchpad/jump.py` (wrong-herb cost sweep).

## Frame verdict
Frame is right about **reading**: "fewer told rules + state on bodies" answers most of the 13 points, partly (4 fixed, 8 partly).
It's wrong about **choosing**: point 12 is a rules problem, not a teaching problem. With the thesis's own numbers, "give a
herb on the first sign; if it's wrong, give the other" wins every time, so A's one remaining choice is dead. The felt and
seen signs never need combining, and the cuts leave nobody a reason to lie. Fix S1–S2 before building A's UI. Also check
the user's 1-human-plus-5-bots setup (S3): there, the bots leave the human nothing to do.

## Findings

### S (severe)
**S1. The kept choice is dead: give on the first sign wins every time; a wrong herb is a free test.**
- Case [ran, thesis numbers, 150 s case, herbs in hand, 8 s to give]: one sign leaves 2 monsters, and the best guess is
  right 52.8% of the time. Waiting one stage costs 1/3 of the case for sure, and the odds drop from 0.95 to 0.65. A wrong herb costs the same
  1/3 jump but only 47% of the time. It also pops the next sign and rules out one of the 2 monsters, which leaves exactly one.
  Cured: give-on-1st **0.90**, guess-at-2nd 0.79, wait-for-certain **0.74**. At 30 s delay: 0.79 vs 0.65. Same at 120 s.
- So the felt sign + seen sign combination (the game's one sentence: "put together what the sick friend feels and
  what the others see") is never used. Only the first sign matters, and its owner matters only when it's felt (50%).
- The % is hidden, so the 52.8% pick looks like a coin flip to the player (B15 shallow choice). Kill line "same thing in
  the first 10 s of every case" trips on night 1–2.
- A vs B was decided on "B removes the only choice". A's choice is dead too, so that reason doesn't separate them.
- Sweep [ran]: making the wrong-herb jump bigger barely helps. Jump 1/2: 0.85 vs 0.74. Jump 2/3: 0.81 vs 0.74. Only
  "wrong herb = turns at once" flips it (0.52 vs 0.74). The cause is structural: with 2 monsters left, a wrong herb is a
  perfect test, and waiting costs a steep 30 points of odds.
- Fix direction: give a wrong herb a cost that beats one stage of waiting in some situations (the herb supply, the giver,
  a turn from stage 2 on, ...). Re-run the script until each strategy wins somewhere. Then point 12 has a choice.

**S2. The betrayal half is hollow: no motive to lie or sabotage, and the visible stage exposes lies. The thesis says "kept".**
- Case: pans are cut, and pans were the only stated reason for a patient to hide ("so they don't get panned",
  design.md Trust). Per-player win means cured > turned. Hiding or lying only delays your own cure, and fewer people
  alive means you get sick more often, so nobody gains from a death.
- The curer's sabotage route (pan bait) is gone. A wrong herb is now normal play (S1), so it carries no meaning.
- Lie detector [read, `shown()`]: from stage 2 on, every case has a felt sign. A hunched friend saying "I feel fine" is
  lying for sure, and the thesis's own 8-player scene gets this wrong ("lying or early": it can't be early).
- Pillars bent and not listed: "bluff from both sides" (listed as kept), "trust must matter until dawn", "liars are never
  exposed by the game" (a fixed, visible schedule exposes them; critic memory "fixed schedule spots a fake" ×2),
  "signs always different" (fixed table, no tricks, scars, pond or tools: the same every night, B21).
- Only real betrayal left: the creature's free choice of victim, and the last herb on a double (rare: ~1.7 herbs per
  case against 6 herbs + regrowth).
- Fix direction: list these as dropped for step 1 and take that to the user, or name the motive to lie that survives the
  cuts before building. Never "kept" with no rule behind it.

**S3. In the user's test setup (1 human + 5 bots) the human gets no herb and no patient.**
- Case [read, `bot.gd _chores/_find_patient/_doctor`]: each idle bot fetches a herb within 22 m. With tools cut, 5 bots
  hold 5 of the 6 herbs within seconds, and up to 2 bot doctors take each patient. The thesis's scene has the human
  holding wolfsbane at 1:50, which the bots won't allow.
- The bot doctors' give rule uses vein thresholds (`veins >= 0.35` etc.). The thesis removes veins, so they give only at
  confidence ≥ 0.85 (waiting), which is a rewrite.
- [assumed, not run] The same herb hoarding (plus tools) was live in lesson 1. Part of "don't know what to do with an
  object / actions with other players / any choices" may come from bots doing everything, not from the UI. Repeat of
  "one player can skip or carry the learning" and "a game must make sense in the user's real test setup" (×3).
- Fix direction: in practice, bots leave herbs on their spots for the human and wait for the human's give (with a timeout
  fallback). Play the 1+5 scene through the bot code before building.

### M (major)
**M1. "≤ 3 rules" undercounts; the guide is back as pictures.**
- Case: the sign table is 6 signs × 2 monsters = 12 links plus 3 herbs, and A is unplayable without it. The Tab picture
  card holds the same information the user called "messy, too detailed" (point 5).
- The start card is 3 "rules" made of 8 sentences, **50 words** (claim: ≤ 25), shown for 8 s (~375 words/min).
- Rule 1, "Their body shows which", leaves out the felt half. The old "only you feel your inner signs: tell each other"
  is gone, so the core coupling is never told.
- Fix direction: count the table as taught content. Tie each seen sign to the creature models (claws on the werewolf and
  troll models, glow on werewolf and vampire, stone on vampire and troll), so a turn teaches the table. Make the card
  ≤ 25 words for real, and say "you feel signs nobody else can: tell them".

**M2. The kept systems that should change behaviour are hidden, so they can't.**
- Case: at a roar a new player runs to the garden (> 15 m) and is shown to the creature for 10 s (hidden) and caught;
  friends nearby had a 5 s head start (hidden). The user's U23 was about feel ("running away feels a lot more safer").
  A hidden rule doesn't change feel, and it adds luck culprits (B20).
- Grab's half speed is invisible (critic memory "effect on a hidden meter can't be discovered").
- Curer protection goes back to hidden, undoing critic v2.1 m1 ("fix that undoes an earlier fix" ×3).
- Fix direction: show each on a body (near friends glow at the turn; a held patient visibly slows), or cut it from
  step 1 and list that.

**M3. Felt claims still vanish in 4 s.**
- Case [read]: `SAY_LEN` is 4 s, bots say each felt sign once, notes are cut, and only seen signs persist. Under S1 the
  first sign decides everything, and half the time it's a felt claim. Miss that 4 s bubble and you know nothing.
- Point 2 ("track") is only half fixed.
- Fix direction: a claim stays over the head as a picture until the speaker changes it.

**M4. Shudder and convulse are both body jolts, with opposite next steps.**
- Case: "shudders hard" means give the same herb again; "convulses + red burst" means give the other one. Under S1 the
  whole next action rests on telling them apart. A new player sees "it jerked".
- Breaks one visual language (visual-communication #4, anti-pattern 5).
- Fix direction: make them differ in shape and direction (lean toward you / recoil away, herb colour / red), not in
  strength.

**M5. The first-person hands may leak the split.**
- Case: hands that "tremble and darken" plus claws and stone skin, which sit on the hands, would let the patient see 2 of
  their own 3 seen signs. Felt signs plus own hands give a solo diagnosis. If the hands hide them instead, "darken" reads
  as grey skin.
- Repeat of "a mirror let the patient see their own outer signs".
- Fix direction: seen signs only where the patient can't see them (face, back), and the hands only tremble.

**M6. At 8 humans: one patient, 1–2 givers, about 5 idle; the same information for every watcher.**
- Case: signs show at 10 m in any light, from any side, and never fade, so position no longer splits information. One
  player who knows the card calls "wolfsbane; if it bursts, garlic" for everyone (quarterback ×4).
- [ran] Gap is 45/√8 ≈ 16 s, and cases end at mean p 0.27 (~40 s) under S1. One case at a time, doubles 10–20%: a calm
  conveyor (×2).
- Fix direction: bring back a position-set split (some sign only from behind / up close / in a moonbeam), or more cases
  in parallel at large crews.

**M7. Not a small first step.**
- Case: about 12 build tasks with no order: sign meshes (claws are new), first-person hands, felt-effect rework,
  hunch/twitch, outline + key system, picture start card and Tab card, a scripted 4-bot demo (new bot scripting; it
  kills Dee), HUD removal, cut flags, pace, the bot doctor rewrite (S3), tests.
- Fix direction: step 1 = cut flags + pace + 10 m any-light seen signs on existing meshes + hide the HUD + start card +
  bot herb fix. The user plays that; the demo, hands, felt effects and cards come later.

**M8. Text comes back by the side door, and online teaching is the lever that already failed.**
- Case: online gets "the start card only". That is the rules-on-the-loading-screen / How to play lever the user already
  answered with "start of the game doesn't explain".
- RMB (hold up) and 1–4 (say) have no prompt at any target. The "(say it: 2)" key hint from UX critic r2 M4 is removed,
  so a legend has to come back.
- The bubbles are sentences. A picture of "the dark looks lighter" will fall back to a caption.
- Fix direction: teach online through the first case itself (what the world does), not a card. Give every verb a prompt
  at its target, or cut the verb.

### m (minor)
- **m1. The scenes break their own schedule (repeat ×5, "scene numbers not computed").**
  - 1:00: Bo shows eyes + a bubble, but stage 1 shows one sign.
  - Claws at 1:50: if the eyes came first, claws (a seen sign) arrive only at stage 3 = 2:40, odds 0.43, not 1:50.
  - You: felt-first → 3:30 / 4:20. Seen-first → grey skin visible at 3:30. The scene's 4:00 / 4:50 matches neither.
  - Fix: compute scenes with the script.
- **m2. Cases per night** [ran]. The thesis says 4–5 at 6 alive [assumed]. Actual: ~9.8 for a crew that gives on the
  first sign (good crew, herbs in hand), 6.2 for a crew that waits for certainty, 4.9 for a new crew fetching herbs.
  Deaths per night, if each turn costs one life: 1.3–1.5 (good crew), 1.6–1.7 (waiting), 2.6–2.8 (new).
  The slow stage-2/3 body signs (hunch, twitch) will rarely be seen.
- **m3. No "I'm sick" key.** The trembling tells a seen-first patient they're sick, but 1–4 offers only a felt sign or
  "I feel fine", and "look at…" was cut. Fix: a "something's wrong" line.
- **m4. Felt effects.**
  - "View drifts toward the nearest meat", always on for up to 150 s, fights aiming at a give or a raised herb, and
    comfort.
  - "Moonlight burns" only works in moonlight, which contradicts "constant, not trigger-based".
  - Night sight is a buff.
  - Fix: a constant cue that doesn't move the camera.
- **m5. Practice now has doubles** (lesson 1 had none). That is a new load in the user's test. Either keep them off in
  practice, or list them as new.
- **m6. Kill lines go stale.** "Nobody asks real or the house?" is moot without tricks; "same thing in the first 10 s"
  trips by S1. Replace both.
- **m7. Dark pillar is now decor.** The moonlight-only dark pillar (user) loses its gameplay job: signs read in any
  light, so only the troll's sense uses it. List it.
- **m8. The demo is under-specified.** It kills bot Dee: is the practice night then 5 alive? It also teaches the
  certain-two-sign path, which S1 makes the losing one.

## The 13 points

| # | User's point | Verdict | Why |
|---|---|---|---|
| 1 | Start doesn't explain what to do | partly | New in-game card + practice demo; the card is 50 words in 8 s; online gets only the card (M8). |
| 2 | Symptoms too fast, hard to read or track | partly | 150 s cases, seen signs big, persistent, any light; felt claims are still 4 s bubbles (M3). |
| 3 | UI text instead of game feedback | fixed | Results on bodies and in sound; text left is small (card, felt line, bubbles, key icons). |
| 4 | Too many UI elements | fixed | ~6 elements; notes, feed, banners, coach, map cut. |
| 5 | Cure guide messy, too detailed | partly | Same 12-link table, now in pictures (M1). |
| 6 | Don't know the goal | partly | Rule 3 + the demo's catch; online text only. |
| 7 | Don't know what a cure is and why | partly | The demo shows that a herb cures and a turn kills; the reasoning from sign to monster to herb is never shown (Bo just runs off). |
| 8 | Am I turning, or a friend? | fixed | Trembling + heartbeat for self; big seen signs on friends (watch M5). |
| 9 | Don't know what to do with an object | partly | Herbs only + outline; but in 1+5 the bots hold 5 of 6 herbs (S3). |
| 10 | Don't know how to interact with an object | fixed | Outline + key at the target. |
| 11 | Don't know the actions with other players | partly | Give and grab shown at the target; RMB and 1–4 unprompted; grab's effect invisible; "tell" not taught (M1, M2, M8). |
| 12 | Don't know any choices | **not** | The one kept choice is dominated (S1); lying has no motive (S2). |
| 13 | Don't know how to read what is happening | partly | Roar, chime, burst, scream; the next step depends on telling shudder from convulse (M4); the feed is gone, so out of sight = only the roar. |

## Co-op gate (core loop after the cuts)

| # | Gate | Verdict | Why |
|---|---|---|---|
| 1 | Coupled | pass (weak) | No self-cure; the patient must stand still; their felt sign is needed in ~50% of first signs. |
| 2 | Split | partial | The felt/seen role split stays; the position split is gone (10 m, any light, persistent); M5 leak risk. |
| 3 | Talk | partial | At most one claim per case; a coin flip needs no debate; bubbles carry it for bots. |
| 4 | Blame | pass | Wrong herb: burst on the body, giver seen; turn = roar; catch = scream. |
| 5 | Not easy | pass [ran, rough] | P(no death) 0.12–0.17 for good crews; new crews lose 2.6–2.8 of 4–8. |
| 6 | Not solo-able | **fail** | One herb carrier using give-now clears cases next to a patient who only stands; in 1+5, two bot doctors do it all. |
| 7 | Two-way | **fail** | The patient's end only tells and stands still (S2); the curer's end is a coin flip with a free test (S1). |

- **Lone survivor:** unchanged (self-cure on felt signs). OK.
- **Dying on purpose:** no gain. OK.

## Numbers checked
- Herb odds [ran]: 0.92 at p 0.03, 0.65 at 1/3, 0.60 at 0.40, 0.43 at 2/3.
- Lean after one sign: 52.8%.
- Stage 2 is certain in 50.1% of cases; when it isn't, the best guess is right 53.6% of the time.
- Night model: herbs held, 2 per kind regrowing 120 s after use, each turn = one death (catch or starve).
- Ignored: holds, head starts, curer skip.
