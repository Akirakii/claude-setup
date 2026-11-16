# Full Moon: critic r3 (isolated antithesis, 2026-11-11)

Read: thesis-r3, thesis-r1 top (U1–U10), critic-r1, critic-r2, design-anti-patterns, critic-anti-patterns, DRS
gameplay-anti-patterns, checks.md, triad / idea-search-loop / scope-lessons memory, Full Moon research.md, research.md
2026-11-11 (funny vs difficult). No sim. Numbers are hand math from the thesis's table, with an equal chance for each
creature [checked: arithmetic, python]. Walk speed 5 m/s and map runs of 10–25 s are [assumed].

## Round-2 fixes
- S1 name tags: **fixed.** One sign leaves two creatures, and two signs from different rows name one. The lean is
  51–55%, not 55–64% (m3). The same table opens a new hole: M1.
- S2 free test / pharmacy: **partly.** A wrong cure now costs a cure, a burst of signs and a visible culprit, and there
  are at most 2 cures of each kind. But the wrong cure jumps only to the *start* of the next stage, so late in a stage it
  costs almost nothing (S1). And "a picked cure regrows after 120 s", read literally, regrows while the first is still held (m1).
- M1 calm conveyor: **mostly fixed at 6** (a case every ~55 s, falling to ~43 s, plus doubles and refetch runs). At 3 a
  case is running about 25–35% of the night, and the 60 s gap is fixed, so players can learn it (M2).
- M2 patient decides nothing: **not, in effect.** Tricks exist, but they fade in 8 s inside a stage that doesn't decay
  (S1), and the case clock shows which signs are tricks (M2).
- M3 mirror: **fixed.** One leftover: the rules don't say whether you can use the thermometer on yourself (m2).
- M4 holding/knocking out invisible: **fixed** (the signs visibly stop, the eyes close, the inner sign is lost). But the
  stage-2 inner sign completes the patient's half on its own (M1).
- M5 one-sided first build: **fixed** (builds A and B). Build B has no kill line and its pick wheel has no timeout (m5).
- Fixes that undo fixes (critic pattern ×4):
  - r2-M4's stage-2 inner sign undoes r1-S1's split from stage 2 on (M1).
  - The regrow wording can reopen r2-S2 (m1).
  - Reading the thermometer on yourself reopens r2-M3 (m2).

## Frame: sign math
- **Stage 1, one inner sign "picked by its %"** (W heartbeats 42 / meat 58; V heartbeats 50 / lamps 50; Z lamps 44 /
  meat 56): P(V | heartbeats) 55%, P(V | lamps) 53%, P(W | meat) 51%. That is a coin flip; the % column changes nothing
  a player acts on.
- **Tools work from the start of a case.**
  - A tool from the other row names the creature when its sign shows (heartbeats + cold → V; meat + eyeshine → W;
    meat + cold → Z; lamps + eyeshine → V).
  - When the sign doesn't show, the absence still leans 60–76%.
  - Even a same-row lantern moves heartbeats to 59% / 71%.
  - Scene 1's "not cold proves nothing" is wrong: it makes werewolf 68%, and Ana then gives garlic against those odds.
- **Two signs from different rows: 100%.** The look-alikes barely touch this:
  - tricks hit only healthy players, so a sick player's inner signs never lie;
  - everyone knows each friend's scar;
  - "were you in the garden?" answers the garden's cold.
- **Two signs of the same kind always name the creature** (M1).
- **Options, with the same cure budget:**
  - check then guess: ~96%;
  - guess now: ~92% (the thesis says 78% because it allowed only one cure after a wrong guess, but two for waiting);
  - wait for stage 2: 84%.
  Waiting never wins (S1).
- **Readable in 25 s:** yes. The rows group by theme: teeth (heartbeats / fangs / eyeshine), dead (lamps / grey /
  cold), flesh (meat / drool). It is memorised by night 2. Teach it as pairs ("fangs: werewolf or vampire"), not as
  "rules out", because under pressure people think in what a sign *is*.
- **Funny or just difficult:**
  - Funny where it counts: the wrong-cure burst (a surprise, on a body, with a visible culprit, cheap), the pan, the
    trick false alarm, the drooling scar, the liar exposed by his own fangs.
  - Just difficult: the silent failed roll, and the victim's death.
- **Fantasy, logic and look aligned:** mostly, with two splits:
  - "the cure weakens" against odds that step by stage (S1);
  - "friends see what you can't" (taught rule 1) against outer signs that a learned crew never needs (M1).
- **Patient as decider (gate 7):** no (S1, M2).

## Severe
**S1. The cure doesn't weaken inside a stage, and a wrong cure only jumps to the start of the next stage, so the
stated choice has one answer.**
- Why:
  - The odds are 90/60/30 by stage: a step, not a slope. Inside stage 1's 25 s, waiting 8 s for a trick to fade and
    reading a tool (5–10 s) cost 0%.
  - A wrong cure at 20 s lands you at 25 s with the signs out: the same state as waiting, minus one cure of the wrong kind.
  - So checking first beats guessing now, a late guess beats waiting, and waiting is never right.
  - The patient's "say it now or wait to be sure" is free in the same way.
  - Both halves of the idea line's Choice are dead. What's left is a routine: "tool, then cure before the fangs".
  - Breaks: A15; checks 3.4 (waiting is always wrong) and 4.5 (a fixed threshold); critic "a limit that never binds"
    (×4: a 25 s stage against ~12 s of work).
  - No kill line catches it: the routine uses inner + tool, so kill line 1 passes.
- Fix (Claude's rules only; U6 holds, and "sooner is stronger" becomes true):
  - Cure odds fall smoothly across the case (e.g. 95% → 30% over 75 s, faster early).
  - A wrong cure adds a fixed +25 s, wherever in the case it lands.
  - Show the lateness on the body from second 0 with a sign every creature shares (flush, sweat, reddening eyes). It
    says how late, never which creature.
  - Then every second spent checking, or waiting out a trick, costs a few %. Which option wins depends on the sign, the
    tool in hand, the ripe cures and how often the house is tricking, which is what the thesis already claims.
  - Kill line: if more than 80% of cures land in the same window of the case, the choice has become a routine.

## Major
**M1. Two signs of one kind always name the creature, so from stage 2 nobody needs anybody, and the outer signs are
never needed.**
- Why:
  - Each kind of sign has one entry per row, and each creature sits in two rows, so its two inner signs always come from
    different rows: W heartbeats + meat, V heartbeats + lamps, Z lamps + meat. Its two outer signs do too: W fangs +
    drool, V fangs + grey, Z grey + drool.
  - Stage 2 adds the second inner sign (r2-M4's fix) and, as scene 1 plays it, both outer signs. So the patient alone
    knows, and the watchers alone know. In scene 1, fangs + drool already said werewolf before anyone used heartbeats.
  - The split lives only at stage 1, and there it is inner + tool, not inner + outer.
  - Taught rule 1 ("you can't see your own outer signs: tell each other") describes signs a learned crew uses only after
    a wrong guess. r2's frame verdict ("the logic cures the friend before the look appears") still holds.
  - S1's fix makes stage 2 common, so this hole grows.
  - Breaks: critic "a fix that undoes an earlier fix" (×4), gate 2 from stage 2 on, A18.
- Fix:
  - At most one new sign of each kind per stage. Stage 2 adds one outer sign (picked by its %), not both; the second
    inner and second outer signs come at stage 3.
  - Stage 2 then shows one inner and one outer sign:
    - From different rows (about half the cases): named, but only by putting both sides together.
    - From the same row: you need a tool, or more time.
  - The lone survivor still copes: two self-cures by elimination, ~75%.
  - Knocking out still costs: closed eyes block the lantern, and the patient misses the stage-3 sign.
  - Kill line: the share of cures where an outer sign changed which cure was picked.

**M2. The case clock is fixed, so by night 3 a trick is a lookup and the patient loses their only decision.**
- Why:
  - The first case starts at 1:00. Each next one starts exactly GAP after the last ended (60 s at 3 players, 30 s at
    6), shrinking on a known curve.
  - So a sign before 1:00, or inside the gap, is surely a trick; a sign at the mark is real.
  - That empties the inner look-alike, which was r2-M2's whole fix for gate 7.
  - The 3-human kill line ("nobody asks 'is that real?'") runs on night 1, too early to see this.
  - Breaks: critic "a coordination game that settles into a protocol"; checks 4.5.
- Fix:
  - GAP × a random 0.5–1.5, and the first case anywhere in 0:40–1:30. U3's "every now and then" fits this better.
  - Keep DOUBLE's random 10–30 s.
  - With S1's decay, waiting 8 s on a sign costs something, so "say it now or wait" becomes a real bet for the patient.

## Minor
- **m1. The regrow wording reopens r2-S2.** "A picked cure regrows after 120 s, so at most 2 exist" is false as
  written: a held cure plus its regrown twin makes 3 or more. Write "a spot regrows 120 s after its cure is used up".
  Also say whether cures can be dropped (a clinic stash).
- **m2. The thermometer on yourself is r2-M3's mirror again.** A thermometer is the one tool people use on themselves.
  With it, the patient holds inner sign + tool sign alone at stage 1. Write "tools only read someone else": you hold
  the thermometer to a friend's forehead, and the lantern needs a friend's eyes.
- **m3. The % column is decoration, and a thesis scene misreads its own table again** (×2).
  - The one-sign lean is 51–55%; the "picked by its %" rule normalises the numbers, and the thesis forgot that.
  - "Not cold" means 68% werewolf, yet scene 1 gives garlic.
  - Fix: print P(creature | sign), and P when a tool sign is absent, next to the table. If the lean should matter for
    guessing early under S1's decay, widen the inner % (e.g. 30/70) to get a 65–70% lean.
- **m4. Rules not written down (A19):**
  - Does stage 2 show both outer signs, or each with its %?
  - Which scar does a friend keep if cured before any outer sign showed?
  - Can tricks hit sick players, or come before 1:00?
  - What happens to what's in a grabber's hands?
  - At 2 alive, with one a creature and one waiting at the end of stage 3, does the waiter count as the lone survivor
    for self-cure?
  - Does the lantern fail on closed eyes? (Only the scene says so.)
  - How many thermometers and lanterns are there?
  - "Out cold can't talk" can't be enforced on Discord (critic "silence assumed online" ×2). Rest the cost on in-game
    effects instead: no inner signs while out cold, and closed eyes block the lantern.
- **m5. The kill lines don't test the core.**
  - Kill line 1 passes under S1's routine and under M1's unused outer signs.
  - In build B the bots decide, so kill line 1 measures the bots' policy.
  - Build B needs its own kill line (e.g. the human patient sometimes waits out a sign and is right to; fewer than 20%
    wrong picks on the wheel).
  - The wheel needs a timeout (critic "test setup deadlocks" ×3).
- **m6. The chase numbers are knife-edge** [assumed 5 m/s].
  - A creature shoved back to 5 m closes in ~0.8 s and must hold 2 s, so it catches at ~2.8 s, just inside the 3 s gap
    before the next shove.
  - A player walking backwards in the open survives forever.
  - At 6 players HUNGER never binds: an unarmed player is caught in ~5–10 s.
  - Tune these in the playtest, and judge the shove on the shover's client (DRS #16).
- **m7. Ghosts.**
  - Full game: dying early can pay. A ghost gets no cases, and near dawn, when cases come fast, it can revive by
    pushing a cure. That means alive at dawn without the night's risk.
  - Build A: a ghost can push the last salt into the pond, and nobody can answer it (DRS #8).
  - Fix: a revived player starts a case at once, or revival works only before 10:00.

## Dominant strategy
"Screen and lean", settled by night 3:
- **Minute 0, everyone grabs.** At 3 players, the two tools ride with two different players and the cures are split.
  At 6, every cure, both tools and a pan are in hand.
- **Signs inside the known gap** are tricks and get ignored.
- **A sign at the mark** (or after 8 s, if unsure):
  - whoever holds the other row's tool reads the patient and asks "garden?";
  - a tool sign names the creature, otherwise the crew takes the lean (60–76%);
  - the cure goes in within ~15 s, and nobody waits for fangs.
- **A wrong cure:** the burst names the creature; cure at 60%.
- **A failed roll with no burst** means the kind was right; give the same kind again.
- **Right cure far away:** grab the patient and send the nearest runner. Pan only a patient who won't hold still.
- **Whoever used a cure** walks back to its spot 120 s later.
- **In a chase,** the two holding the creature's cure stand back to back with the unarmed player between them.

Hand-math result:
- ~95% of cases are cured in stage 1 or 2: about 0.5 turns a night at 3 players, about 1 at 6.
- The patient only reports; the outer signs and the % column go unused.

What still varies is logistics: which tool is near, which cures are ripe, doubles, griefers. It is a routine with
errands, not a choice.

## Scenes (night 5, a learned crew)
**3 players (Ana, Bo, Cy), 12 min:**
- **0:00–1:00:** Ana takes the thermometer and garlic, Bo the lantern and salt, Cy two wolfsbane (Cy reads cold for
  30 s). Bo pans Cy; Cy pans him back. At 0:50 Cy smells meat: "before one, trick". Nobody moves.
- **1:00:** Bo: "lamps hurt". His lantern goes to Ana: no eyeshine, so zombie at 60%. Salt at 10 s: cured by 1:12.
  Scar: drool.
- **1:12–2:12:** dead time. Bo drools on Ana and she pans him. A trick in the gap gets ignored.
- **2:12:** Cy: "heartbeats". The thermometer reads cold, but "you were in the garden", so it's ignored. Eyeshine:
  werewolf 59%. Wolfsbane: wrong. Fangs and grey skin burst out, so vampire. Garlic at 60% fails, and the second garlic
  is in the greenhouse. Bo grabs Cy, and Cy's fangs stop spreading. Cy struggles free "to be a vampire", so Bo pans
  him. Ana is back at 20 s, and garlic on the out-cold Cy works.
  This is the night's one real case: ~70 s, everyone in it, two culprits. Funny.
- **3:20–10:00:** the same 15 s routine every ~70 s, with the gap shrinking. At 8:00 a double: Bo and Cy cure each
  other, a scramble.
- **10:30:** Cy turns vampire after two failed garlic rolls. Nobody holds garlic, and he catches Bo in ~5 s. Bo's
  ghost pushes the regrown garlic toward Ana.
- **Dawn:** 2 of 3 alive.
- **What happened:** of 9 cases, 1 went wrong. The others were a 10–15 s routine. Nobody waited for stage 2 on purpose,
  and the outer signs showed only in the wrong-cure burst. A luckier night loses nobody.

**6 players (Dee, Eli, Fae, Gus, Hal, Ivy):**
- **0:40:** everything is in hand. Hal hides the lantern in the oven; Gus pans him.
- **1:00:** Eli: heartbeats, not cold, so werewolf at 68%. Wolfsbane: cured.
- **1:30:** Dee: meat. Hal smells meat too, but this time it is inside the double window, so the crew waits 8 s and it
  fades. Eyeshine on Dee: werewolf. Cured. Both wolfsbane are now used up, so Ivy and Gus loiter in the garden (and read
  cold).
- **2:30:** Gus: "lamps hurt", while in the garden. The thermometer is useless (same row, and garden cold anyway). He
  runs 15 s to the lantern: vampire. Cured.
- **A case every ~50 s,** with 3–4 people on it and 2 fetching or goofing.
- **6:00:** a double, Fae and Hal. Hal lies ("meat"; it is really lamps). Eyeshine plus "meat" points to werewolf, so
  wolfsbane: wrong. Fangs and grey burst out: "Hal lied!" He runs, Gus pans him, garlic. Funny, and the comeback works.
- **9:00:** Eli turns zombie. One salt is in hand and one is regrowing. Dee is alone in the tree house and gets caught
  in ~6 s. HUNGER never bound.
- **10:00–12:00:** the gap is ~20 s and doubles come at 30%, so cases run almost nonstop. REGROW finally binds (no
  garlic for 40 s).
- **Dawn:** 4 of 6 alive.
- **What happened:** busier and more fun than the 3-player night. Two players are idle per case. The outer signs
  mattered only on wrong guesses and on the liar. Nobody waited for stage 2.

## Numbers
- **TURN 75 s:** binds on errands (a 10–25 s fetch), not on reading (~12 s of free work in a 25 s stage: S1).
- **GAP:** binds as pressure, and the per-player rate holds as players die ✓. It is fixed, so players can predict it
  (M2).
- **DOUBLE:** binds. Two cases run at once for ~5–8% of the night, inside r1's ≤ 10% for U8's "rare" ✓. At 2–3 alive the
  two patients cure each other ✓.
- **FAKE:** the rate is fine (~1 a minute at 3 players, ~2 at 6), but it doesn't bind: 8 s inside a stepped stage costs
  nothing (S1), and the clock gives tricks away (M2).
- **REGROW:** binds at 6 late in the night (~1.7 cures a minute needed, against 1 a minute of each kind) and after wrong
  guesses; barely at 3. Wording problem: m1.
- **HUNGER:** binds at 3 (two armed players cover the third); not at 6.
- **KO:** binds. KO and holding cost different things:
  - Holding: half speed and both hands, but the patient keeps talking, keeps their eyes open and can struggle.
  - Knocking out: a third of the speed and free hands, but the patient goes silent, their eyes close, and there's a
    20 s lockout.
- **Shove:** knife-edge (m6).
- **2 alive** ✓: betrayal is a 1-on-1 duel that loses more often than curing does.
- **Lone survivor** ✓: self-cure; the second inner sign makes it fair (~75% under M1's fix).
- **Lying to turn:** the stage-2 body exposes it, and the pan or the grab answers it ✓.
- **Dying on purpose:** no gain in build A; it can pay in the full game (m7).

## Scope
- **Build A:** ~3–4 weeks for one developer [opinion]: a first-person body with 2 hand slots, 6 regrowing spots, 2 tool
  readings, 3 outer effects and the burst on one shared body, bots that wander and talk in speech bubbles, grab, pan,
  cure, the stage clock, the journal, one creature with chase AI, shove and catch, ground floor and garden. That is past
  the 2-week end of the range, inside 4 weeks.
- **Build B:** +1–2 weeks: 3 first-person inner effects, bot doctors that fetch, read and cure, and a wheel with a timeout.
- **Full game in 3–4 months:** tight but plausible, if:
  - each creature keeps one power (the vampire's flight is the costly one, and the zombie's is still TBD, so U9 is open);
  - the online code for grab, pan, catch and shove is wired in from build A. Both first builds run offline, so the
    online risk (~5× time, per scope-lessons) would otherwise land last.

## Co-op gate
1. Coupled ✓: nobody can cure themselves, and at stage 1 a cure needs the patient's sign plus a friend's tool.
2. Split ~: ✓ at stage 1 (inner sign vs tool, and a tool belongs to whoever holds it); ✗ from stage 2 (either side alone
   names the creature: M1).
3. Talk ✓: the inner sign has to be said, and the tool reading called out.
4. Blame ✓: a wrong cure bursts out on the patient's body with the giver's face on it, and a turned friend has a face.
   Only the failed roll has no culprit.
5. Not easy ~: new crews lose, and the pressure rises all night ✓. A learned 3-player crew may lose nobody (kill line 2
   watches for it).
6. Not solo-able ✓: two hands each and no self-cure. At 3 the tool holder leans toward quarterbacking, but the curer
   and the grabber are other people.
7. Two-way ✗: the patient's only choice is free (S1) or a lookup (M2). Holding still is a formality, and struggling or
   lying only serve griefers.

## Rule count
- **Taught:** 3 rules, about 10 clauses, plus 2 taught when they happen (the lone survivor's self-cure, ghost rules).
- **Must discover to play decently** (about 13, the same as r2's 3 + 12; most are visible in the world):
  - "cure before the fangs" (the stepped odds);
  - a failed roll with no burst means the kind was right;
  - a wrong cure bursts the signs out;
  - only the other row's tool helps, and an absent tool sign still leans;
  - the lantern needs open eyes;
  - tricks fade in ~8 s;
  - the garden reads cold for 30 s;
  - scars;
  - a cure needs the patient still, held or out cold, and takes 2 s;
  - cures regrow at fixed spots, 2 of each kind;
  - KO 20 s plus a 20 s lockout; a grab runs the case at half speed, and the patient can struggle free in 3 s;
  - the shove's 3 s gap;
  - turning throws the holder off; a second case waits at the end of stage 3.
- **The hidden ones that change play:** the stepped odds (S1) and the fixed clock (M2).

**Keep:**
- the wrong-cure burst;
- the liar exposed by his own body;
- "spend the last wolfsbane on a 30% stage-3 cure, or keep it to shove";
- tools as seats anyone can take;
- the cap of 2 cures per kind;
- no reward for betrayal at 2 alive.

## Verdict
No, not ready yet. One rule shape (stepped odds, and a wrong cure that jumps only to the next stage's start) kills the
stated choice and the patient's decision. And the table lets either side name the creature alone from stage 2. Three
small rule changes fix it: smooth decay with a fixed +25 s for a wrong cure; one new sign of each kind per stage; a
random GAP. After those, it is a polished sketch for build A.
