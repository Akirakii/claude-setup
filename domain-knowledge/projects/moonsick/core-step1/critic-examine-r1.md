# Critic: examine thesis r1 (antithesis, 2026-11-12)

Target: `docs/examine-thesis.md`, on top of step 1 (`docs/core-thesis.md` synthesis), against `docs/design.md`, the 13
points, user pillars (U1–U23), `docs/diagnosis-research.md`, the anti-pattern lists. Code read as of now, being edited
by the removal pass; it was used for facts that pass doesn't touch (bot.gd, night_sim give/grab/speed, hud heartbeat).
Tags: [ran] = script; [read] = code/docs; [assumed] = not checked.
Scripts (scratchpad):
- `/tmp/claude-1000/-home-akiraki-claude-code/d3da34f0-115c-4b3f-9c35-cc389c307192/scratchpad/examine_sim.py` (one case, each strategy)
- `/tmp/claude-1000/-home-akiraki-claude-code/d3da34f0-115c-4b3f-9c35-cc389c307192/scratchpad/examine_night.py` (whole nights)
- `/tmp/claude-1000/-home-akiraki-claude-code/d3da34f0-115c-4b3f-9c35-cc389c307192/scratchpad/examine_lean.py` (lean strength × wrong-cure cost)
- `/tmp/claude-1000/-home-akiraki-claude-code/d3da34f0-115c-4b3f-9c35-cc389c307192/scratchpad/examine_fix.py` (random 2nd-sign time)

Model: 3 spots (eyes, skin, hands); each monster shows 2. Stage 1 shows 1 sign, stage 2 (p ≥ 1/3) shows both, which is
always certain. Being held = the case at half speed. A wrong cure turns them at once. Odds = 0.30 + 0.65(1−p)^1.5. A case
lasts 150 s at dusk, 120 s by dawn. Examine 4.5 s, give 2 s. Friends arrive and grab at 15–30 s. A cure trip is 40–60 s
there and back. 2 cures of each kind, regrow 120 s. The user's % is reused (eyes = eyeshine, skin = grey, hands = the
drool slot). GAP is 45/√n, no doubles. A turn kills 1 person with chance 0.9 [assumed].

## Frame verdict
The frame is right about reading: big signs, up close, on a friend who holds still. It is wrong about knowing. Anyone can
examine as often as they like, for free, and the answer is certain at a fixed moment (stage 2), so the examination is a
scanner with a 50 s delay, not a puzzle. Every listed choice then has one answer. The patient knows nothing and stands
frozen. The research's own sources of drama (tell or hide, test whom, cure in time) are all switched off. Point 12 is
still "not". Fix S1–S4 before building.

## Findings

### S (severe)
**S1. Every listed choice has one answer. The examination names the answer at stage 2. Wrong cure = turn kills guessing for good.**
- Case [ran, examine_sim]: cured rate, hold + wait for the 2nd sign vs give on the 1st sign.
  | Case length, herbs | Hold + wait | Give on 1st (coin) | Give on 1st (% known) |
  |---|---|---|---|
  | 150 s, herbs in hand | **0.88** | 0.48 | 0.50 |
  | 120 s, herbs in hand | 0.81 | 0.46 | 0.49 |
  | 150 s, both candidates fetched during stage 1 | 0.87 | 0.44 | 0.47 |
  - Not holding is worse: 0.77 with herbs in hand, 0.43 if the herb is fetched only after the diagnosis.
- No situation flips it.
  - Lean sweep [ran, examine_lean]: with wrong = turn, giving early loses even on a 90% lean (0.87 vs 0.90).
  - With a random 2nd-sign time and a coin-flip lean [ran, examine_fix], waiting still wins.
- By night 1 the whole game is: hold, wait for the veins, examine, and the plain spot names the herb (skin plain =
  werewolf, hands plain = vampire, eyes plain = troll). That is B21 (solved by run 2), B15 (shallow choice) and DRS #5
  (dominant strategy).
- The night-1 cliff [ran, examine_night]:
  - A new crew that guesses (as the card invites) loses 3.7 of 6 a night; P(nobody dies) ≈ 0.
  - Once a crew learns "never guess", 0.42 deaths a night.
  - Blame lands on a choice, not a slip (DRS #13), and the price is a friend's death.
- Research contradicted:
  - Phasmophobia, the thesis's own model, allows wrong guesses ("failure is information"). The evidence also comes at
    uncertain times.
  - Pattern 5 (a scarce test makes the choice) is unused: the examination costs nothing.
- Repeats:
  - "Readability fixed, choice left dead" (now ×2).
  - "A tool that names the answer makes the reading pointless".
  - Critic r1 S1 is parked a 2nd time (B25; questions 16 still unanswered).
- Fix direction: a per-case variable must flip the best answer, checked by script until each strategy wins somewhere.
  - [ran] A visible, varied lean (the user's % per sign, shown, spread 50–90%) with a wrong cure costing a +1/2 jump: a
    guess wins at a lean ≥ 0.8.
  - Or a scarce examination.

**S2. The patient and the holder are pressure plates, and the game's one sentence is gone, unlisted.**
- Case: the patient knows only "I'm sick". Held means speed 0 [read, `speed_of`]. Their whole case is: press 1, get
  grabbed, stand frozen.
  - Frozen time per case [ran]: 107 s (150 s case), 83 s (120 s case), 170 s if the herb is fetched after diagnosis.
  - About 500–600 s of frozen patients per night.
- The holder: LMB held, 0.35 speed, about 100 s, and an invisible effect.
  - The half speed shows nowhere: critic r1 M2, "an effect on a hidden meter can't be discovered".
  - Holding in stage 1 doesn't change the odds at all (they slide by progress p); it only stretches the clock.
- "Put together what the sick friend feels and what the others see" (design.md's one sentence) is deleted, and the
  thesis doesn't say so.
- In 1+5 practice the human's own case (the 2nd, by design) is 50–155 s frozen, watching bots (scene below).
- Hits: gate 7, memory "a partner who only stands in place" (now ×3), DRS #2 (taking players out of play).
- Fix direction: give each end a piece only it holds, or a call to make while held. For example, one spot readable only
  by the patient, or only from the holder's position behind.

**S3. Betrayal and trust have nothing to bite on (critic r1 S2, back again).**
- Hiding gains nothing [ran + assumed P(catch | turn) = 0.9]:
  - Patient's own survival: tell ≈ 0.88 + 0.12 × 0.9 ≈ 0.99; hide (found at p 0.55) ≈ 0.63 + 0.37 × 0.9 ≈ 0.96.
  - Expected friend deaths: 0.11 vs 0.33.
  - A turned patient catches a helper standing next to them, so a wrong cure barely hurts the patient. The thesis's
    "afraid of a wrong cure" fear is empty.
  - Under good play wrong cures never happen, and the giver examines before giving (they are within 1.5 m anyway).
- Lies are exposed by the rules within seconds:
  - "Hands plain" when they were hairy is disproved by any second 4.5 s examination. The thesis's own 8-human scene has
    two more examiners standing there.
  - Hiding is exposed by veins (stage 2, 4 m) and shaking (stage 3).
  - The second sign comes on a fixed schedule: memory "a fixed schedule lets players spot a fake" (now ×3).
- Nobody ever lies; "hidden info nobody gains from hiding" (now ×3).
- U13 (trust), U14 (bluff) and U22 (liars never exposed) are bent. The thesis lists only U14, as a rewording.
- Fix direction: name the stake a lie wins before building, or tell the user plainly that bluff and trust are off in this
  step.

**S4. Pillars dropped or bent that the thesis doesn't list (memory ×6).**
- **U23, helping beats fleeing (user, today: "we should fix that"): made worse.**
  - The loop puts the holder at 0 m and the examiner within 1.5 m for 100+ s.
  - A wrong cure turns the patient right beside them.
  - Head starts are off (step 1).
  - Fleeing is the safe seat and holding is the bait seat. It isn't in questions 18 either.
- **U8, two at once, rarely:**
  - Doubles are off for every mode (`features.gd`), while core-thesis said "doubles stay".
  - Listed nowhere (not here, not in questions 18).
- **U4, "always different":** every werewolf is eyes + hands; only the order varies.
- **U4, "% per sign":** listed as "kept", but the Tab card has no %, and the lean is a coin to the player (0.50 vs 0.527).
- **U4, "hard to read":** now certain at stage 2.
- **U11, dark:** listed as "kept", but it has no job (eyes glow on their own, the zoom is at 1.5 m).
- **U7 knock-out and U9 powers:** dropped in step 1 and missing from this thesis's list.
- **The approved words:** the user OK'd "eyes, teeth, skin". The thesis uses hands, untagged (A6). See M4 for why that
  matters.
- Fix direction: list each one for the user, U23 first. Don't build a loop that makes U23 worse without the user's OK.

### M (major)
**M1. A calm conveyor and a safe night.**
- Case [ran, examine_night]: with the hold and one case at a time:
  - About 5 cases a night at 4, 6 and 8 alive alike (5.2 / 5.3 / 5.4).
  - Cases fill 79% of the night; about 216 s per night is pure waiting (diagnosed, herbs in hand, nothing changes until
    stage 2).
- Deaths per night:
  | Crew | Deaths | P(nobody dies) |
  |---|---|---|
  | Good | 0.42 | 0.60 |
  | New | 0.61 | 0.43 |
- At 8 [ran, rough]: 1 patient, 1 holder and 1 examiner-giver are busy; about 5 stand around. About half the players never
  get sick (0.875^5.4 ≈ 0.49).
- The clock never binds: about 57 s of work against a 300 s held case.
- Holding every patient from second 1 is free [ran, 6 alive]: 5.9 → 5.3 cases and 0.88 → 0.42 deaths. The hold is a
  brake on the night's clock that costs nobody anything.
- Memory: "calm conveyor" (×3), "a limit that never binds" (×5), "a loss the numbers can't reach" (the user's "how is it
  possible to lose?").
- Kill line "a good crew loses nobody 3 nights in a row" trips about 22% of the time (0.6³).
- The user's "too fast to follow" swings to "nothing happens for 50–100 s".
- Fix direction: a clock that binds the held case, and overlap that grows with the crew. Re-run examine_night.py.

**M2. Telling is voice-only, and the user tests with bots (memory ×4).**
- Case: quick chat is 1 "I'm sick!", 2 "fine", 3 "Hold me", 4 "Help!". No line says what you saw.
- Rule 9 has the bots examine for themselves.
- In 1 human + 5 bots, the human's findings reach no bot and the bots' findings reach no human. Zero information passes
  between players; each examiner is self-sufficient.
- Fix direction: picture bubbles (eye / hand / skin, yes or no) that bots both say and read.

**M3. No split, so whoever examines runs the crew (memory "quarterback" ×6, DRS #1, #12).**
- Case: anyone can examine, the result is the same for everyone, and it's certain at stage 2. Information converges at
  1.5 m.
- The 8-human scene has 3 examiners shouting the same thing.
- The runners only obey, and they can skip even that by fetching both candidates.
- The visual-communication pattern "a fact only one spot can see becomes something a player has to say" is unused.
- Fix direction: make each spot readable from one position only (e.g. behind, where the holder stands, vs in front).

**M4. Earlier fixes undone (memory ×5) and one cue with two meanings.**
- **Hands as a sign spot reverses core r1 M5** ("hands only tremble; seen signs sit where the patient can't see them").
  If first-person hands exist (step 1 planned trembling hands), the patient sees 1 of their own 3 spots. The approved
  "teeth" had no such leak.
- **The heartbeat means two things.** Stage 1's "slow heartbeat" is the creature-near heartbeat that step 1 keeps
  [read, `hud.gd` 409–426] (visual-communication #4).
- **The card never says you may be the sick one** ("Friends will turn into monsters"), so the pulse reads as danger
  (point 8).
- **Veins:** "kept" here vs "cut" in core-thesis.
- Fix direction: re-check every core r1 and v2.1 fix after this synthesis; give the sick cue its own sound and shape.

**M5. Not a small step, text comes back by the side door, and the bots need about 7 new behaviours.**
- **Step 1 is still being built and unplayed.** Stacking a new sign system on it confounds two redesigns in one playtest
  (memory "redesigning what was never playtested", now ×4).
- **Build:**
  - New spots, schedule, posterior and %, plus tests (`curse_rules.gd`).
  - Hand meshes (`body.gd` has eyes, grey skin + cracks, drool, veins; no hands).
  - Signs drawn only up close or in the zoom (`public_state` sends "outer" to every client).
  - The examine verb: F, 4.5 s hold, cancel, a private result. It can reuse the tool-read path (`read_tool`, 2.3 m).
  - A new zoom camera.
  - The sick screen by stage, new quick chat, the Tab card, the start card.
- **Text by the side door:**
  - A first-timer can't tell a "plain" hand from a sign without a label or a side-by-side.
  - A result strip, to remember 3 spots.
  - A "you're turning" line, or the pulse reads as a creature near.
  - The bubbles' words.
  - The card's 23 words carry the wrong-cure rule.
- **Bots [read, bot.gd]:**
  1. `_patient` says inner signs; it must say "I'm sick!".
  2. `_observe` reads outer signs from 7 m and claims as INNER; it must become examine-only.
  3. `_find_patient` needs a sign or fresh veins; "I'm sick!" must count as evidence.
  4. A new examine action: walk to ≤ 1.5 m, wait for held or still, 4.5 s, note the result.
  5. Grabbing is brand new: bot.gd never grabs. Pick one holder, release on a cure or a turn, never re-grab a human who
     struggles free.
  6. A timeout: a bot holding the human while both doctor slots (max 2 per patient) are busy elsewhere freezes the human
     until the turn (memory "test setup deadlocks", ×3).
  7. Slower reactions (step 1).
  - The give rule (confidence ≥ 0.85) already waits for stage 2: the bots play the dominant strategy.
- Fix direction: the smallest probe first. New spots + examine on the tool-read path (no zoom) + "I'm sick!" + bot
  examine. Holding and the zoom come later.

### m (minor)
- **m1. The scenes break their own rules (memory ×6).**
  - The 8-human "two holders" is impossible: doubles are off and `held_by` holds one id.
  - The 1+5 scene: "you wait" for 48 s instead of fetching both candidates, then run to the pond after the diagnosis.
    That means a give at about 3:10, p ≈ 0.54, odds ≈ 0.50, against about 2:20 and 0.63 had you fetched during the wait.
  - Rule 9 + `_fetch_any(60 m)` sends 2 bot doctors racing you for the same 2 wolfsbane; one already carrying a herb
    from chores gives at about 2:30.
  - Practice's first case is at 25 s (design.md), not 1:00.
- **m2. Last one alive and 2 alive.**
  - Nobody can examine themselves, so the lone survivor's self-cure is a blind 1-in-3 (wrong = turns with nobody to
    catch = starves; B20).
  - At 2 alive the doctor can't hold and give at once, so there's no slowdown.
- **m3. Undefined %.** The hands spot has no user % (the table has eyeshine, grey and drool). "React 15–20 s slower" has
  no rule (A11).
- **m4. "I'm sick!" sends everyone to one spot.** At 8, a crowd around one frozen friend. The first 10 s of every case is
  the same (kill line).
- **m5. Under-specified.**
  - Examining someone held from behind: front access, pinned hands?
  - What the examined patient sees.
  - A 4.5 s zoom that blinds the examiner if a creature is out.
- **m6. A2 and B26.**
  - One shape, no rivals compared.
  - The research's own opinion says real-time friend games keep "what it is" easy and put the drama in tell or hide,
    test whom, cure in time. The thesis kept "easy" and switched off all three.
  - Research patterns 5, 6 and 8 are unused.

## Scenes [ran / computed]
### 1 human + 5 bots, practice
- **You as the doctor:**
  - 1:00 Bo's case starts (L = 147.5 s, so stage 1 = 49 s).
  - 1:15 Bo says "I'm sick!".
  - 1:25 Cy grabs Bo (p 0.17).
  - 1:30 you finish examining: eyes. Werewolf or vampire.
  - 1:30–2:13 nothing changes on Bo. Held, the 24 s left of stage 1 becomes 48 s.
  - Meanwhile two bot doctors come and examine (they have no way to tell you what they saw), and bots already carry
    herbs from chores.
  - 2:13 veins + the 2nd sign. Whoever examines first and holds wolfsbane gives at about 2:20 (odds 0.63).
  - 37%: a shudder, then a 50 s trip for the 2nd wolfsbane (odds about 0.52).
- **You as the patient (case 2):**
  - About 3:30 your screen pulses and you hear a heartbeat (the same sound as a creature near). You press 1.
  - About 3:50–3:55 a bot arrives and another grabs you (p 0.18). You're frozen.
  - 4:39 stage 2. A bot examines and gives if it carries the right herb, at about 4:46. Otherwise it fetches (5:35,
    odds 0.51), and one retry means about 6:30.
  - Frozen 50–155 s. You decide nothing and see nothing about yourself.

### 4 humans online
- 0:40 Ana's screen pulses; she says "I'm sick". 0:45 Bo grabs her.
- 0:50 Cy examines: eyes. Dee runs for garlic, Cy for wolfsbane.
- About 1:50 both are back.
- 1:50–2:14 four people stand around a frozen Ana, waiting for veins.
- 2:14 Cy examines: hands, so werewolf. He gives at 2:21 (odds 0.64); 36% it needs a 2nd pond trip (about 3:18, 0.52).
- Talk: one call ("eyes! get both!", "hands!"), one-way. Ana and Bo decide nothing for about 95 s.

### 8 humans online
- One patient (no doubles), 1 holder, 1–3 examiners with identical results, 0–2 runners. About 4 idle for about 80% of
  the night.
- About 5 cases a night, so about half the crew is never sick.
- The thesis's liar ("hands plain") is disproved by the two other examiners standing there.

## Dominant strategy
- **Doctor:** hold at once, examine, fetch both candidates, wait for the veins, examine, give. Never give on one sign (0.88
  vs 0.48).
- **Patient:** tell at once and stand still. Hiding gains nothing, and the fear of a wrong cure never comes true.
- **Crew:** hold every patient from second 1 (5.3 cases instead of 5.9; deaths halved, 0.88 → 0.42).
- **Liars:** none. No motive, and disproved in 4.5 s.

## The 13 points (the examine thesis on top of step 1)
| # | Point | Verdict | Why |
|---|---|---|---|
| 1 | Start doesn't explain | partly | 23-word card. It doesn't say you may be the sick one, what a monster does or how to push it back. Online gets the card only (r1 M8). |
| 2 | Symptoms too fast / hard to read or track | fixed (reading) | Big, up close, held, 150–300 s. Overshoots: 50–100 s with nothing new. |
| 3 | UI text instead of feedback | partly | Plain vs sign needs a readout; bubbles; a sick line (M5). |
| 4 | Too many UI elements | fixed | Step 1's trim; the zoom and result strip are added. |
| 5 | Cure guide messy | fixed | 3 spots × 3 monsters, as pictures. It costs the user's % (S4). |
| 6 | Goal | partly | "Survive till dawn" on the card; why a monster matters isn't shown. |
| 7 | What a cure is, why | partly | "Give the right cure; wrong: instant monster"; no why. |
| 8 | Me or a friend turning | partly | Self: the pulse, which sounds like danger (M4). A friend: invisible from afar in stage 1 (veins from stage 2, 4 m), known only from "I'm sick!". |
| 9 | What to do with an object | partly | Herbs only (step 1); bots hold most herbs. |
| 10 | How to interact with an object | fixed | Outline + key (step 1). |
| 11 | Actions with other players | partly | LMB grabs or gives depending on your hands, plus F. Struggle and RMB unprompted. The hold's effect is invisible. |
| 12 | Choices | **not** | Every listed choice has one answer (S1, S3). |
| 13 | Reading what's happening | partly | Only the examiner knows. Others learn by voice (in 1+5: never). From afar, stage 1 shows nothing. |

Fixed 4, partly 8, not 1.

## Co-op gate (core loop: hold + examine + fetch + give)
| # | Gate | Verdict | Why |
|---|---|---|---|
| 1 | Coupled | weak pass | The patient must stand still or be held. A holder is optional (0.77 without vs 0.88 with). |
| 2 | Split | **fail** | No information split: anyone examines and gets the same result. Roles come only from position. |
| 3 | Talk | **fail (1+5)** / partial (4–8) | No chat line for findings. Online: one one-way call. |
| 4 | Blame | partial | A wrong cure has a visible culprit, but good play never guesses. Turns come from failed rolls, with no culprit (B20). |
| 5 | Not easy | weak pass | Guessing crews lose 3.7 of 6. Once "wait" is learned, 0.42–0.61 deaths a night at any size. |
| 6 | Not solo-able | **fail** | One doctor + a still patient cures 0.77. In 1+5 the bots do it all. |
| 7 | Two-way | **fail** | The patient and the holder only stand; the examiner reads a lookup. |

- Lone survivor: a blind 1-in-3 (m2).
- Dying on purpose: no gain.
- **Gate: FAIL** (2, 6, 7; and 3 in the user's test setup).

## Item by item
- **design-anti-patterns.md:**
  - Hits: A2 (m6), A5 (choices claimed without a sim; S1), A6 (teeth → hands; S4), A11 (m3), B15 + B21 (S1), B16 (hold
    and % invisible; S2), B17 (the hold brakes the night; solo doctor; M1, gate 6), B18 (wrong = turn × adjacent helpers ×
    head starts off; S4), B19 (m5), B20 (gate 4), B22 (M1, m2), B23 (M2), B24 (M3), B25 (r1 S1/S2 back; S1, S3), B26 (S1,
    m6).
  - OK: A1, A3, A4, A7–A10, A12, B13, B14.
- **Memory list:**
  - Hits: "partner only stands" (S2), "tool names the answer", which is the flip side of "a free retry turns a guess into
    a test": here the free, unlimited test is the examination (S1), quarterback (M3), pillars dropped (S4), fixed schedule
    (S3), readability fixed / choice dead (S1), text added (M5), voice-only with bots (M2), calm conveyor (M1), a fix
    undoes a fix (M4), a limit never binds (M1), scene numbers (m1), test deadlocks (M5).
- **DRS pattern docs:**
  - Gameplay #1 (M3), #2 (S2), #5 (S1), #6/#7 (gate 4), #12 (M3), #13 (S1).
  - Visual communication #4 (M4) and "a fact one spot sees" (M3).
  - UI-UX OK (key icon at the target, few verbs).
