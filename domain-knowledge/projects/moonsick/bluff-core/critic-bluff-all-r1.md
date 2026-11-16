# Critic, round 1: `bluff-all-thesis.md` (parts 3–6), 2026-11-15

Read: the thesis, design.md, TODO_bluff, bluff-research 14–22 + chat, questions.md, both anti-pattern files; code in
`night_sim.gd`, `bot.gd`, `hands.gd`, `wolf_attack.gd`, `mild.gd`, `move.gd`, `curse_rules.gd`, `body.gd`, `features.gd`.
Numbers: a python script (strain 2 s + `TURN_TIME` 2 s, head start measured at hunt start, strike 1.36 + 0.6 m,
`STRIKE_CD` 1.5 s, `RECOVERY` 3 s, curse rate 1/120 → 1/40 per untreated symptom).

## Verdict on the problem underneath: partly wrong
The core lie (user: "I'll get your coffee", deals) lives in **mild symptoms**, and a mild symptom **has no veins**
(`public_state`: "no veins: it isn't a case yet"). So mirrors, key 9 and turning early all act only in full cases,
where design.md says trips mostly fail. They feed none of the coffee lie: they're a second bluff system bolted on.
The piece the test crew really lacks is missing: **a promise the human can break to a bot.** In part 6 the human
always gives first, so with 1 human + 3 bots the human can never bluff (TODO 7 "can the human bluff at all?" = no).
Need (2) contradicts itself too: "learn how bad you are only through others" and then a mirror that tells you alone.

## Severe
**S1. Turning early pays more than curing (pillar).** A catch gives exactly what a cure gives (back to human, 60 s
skip; design.md). Unwarned victim next to you: the head start ends at 5.0 s, the wolf (sprint × 1.3 = 11.2 m/s, always
sprinting, `move.gd` l.52; not "1.3× a walk") is in reach the whole time, strike at 5.0 s, eat at 6.5 s (down = still).
At curse 0.6 with one symptom untreated there are still 17–41 s left (curable). So T beside a lone friend swaps a
chancy cure for a near-sure one. In the test crew the cost is zero: bots count only gives (trust), and nothing makes a
bot react to the strain. Always-win strategy: case late, cure unsure → hold T next to a bot.
Fix direction: cut part 5 (T was a Claude pick in the chat, not the user's) and take "turning early" back to the
user with these numbers; if it stays, an early turn must end worse than a cure (e.g. the friends within 8 m can't be
struck for 10 s, longer than the wolf needs to reach them), checked with a script first.

**S2. "Helping beats fleeing (the head start comes back)" is false in the numbers.** The head start is measured at
hunt start (`_start_hunt`), after the 2 s strain and 2 s turn. A friend who stays near (≤ 8 m) is struck at 5.0 s. A
friend who runs at the strain is 18–33 m off by then (no head start) and is struck at 6.3–12.0 s on open ground. The
thesis's own scene is wrong: Bo ran, so Bo has no 5 s. Fleeing beats helping; the 5 s only delays against a faster wolf.
Fix direction: don't list it as "kept"; a head start must let a helper reach the wolfsbane or a drag, so check it with
the map's distances (pond beds) before turning `near_head_start` on, and keep that user step-1 cut behind Q-B3.

**S3. The test crew has no human lie.** Deal: the human gives first, the bot pays within 3 s. Offer by reach: the bot
stands still, then pays. In both the bot only reacts (co-op point 7: a pressure plate) and the human can't break a
promise. Fix direction: a bot that trusts you ≥ 1 **goes first** (gives its coffee, expects the perfume): now the human
can take it and not come back, the bot's trust drops, and that's the coffee lie in physical form, no new verb.

## Medium
**M1. The bot's vein lie has no motive.** An afraid bot shows 0 marks: it gains nothing by it (critic log "hidden info
nobody gains from hiding" ×2), and the hall mirror refutes it in a 3.5 s sprint round trip. Fix: cut key 9; mirrors,
the ask and the T probe are three channels of one fact (essence test: merge into the mirror).

**M2. The mild deal barely fits the clock.** Human chain: reach Bo + read (~4 s) + far trip 27 + give 2 + bot delay ≤3
+ bot give 2 = 38 of 45 s; Bo also needs 33 s on his own clock. Both fit: 19% with a far item, 47% at an 18 s trip,
65% at 10 s (assumed: Bo's clock already 0–45 s used, the human's 0–10 s). The scene only works when Bo's symptom is
fresh. Fix: deal bubbles only for items within a near trip, or bot pays first (S3) which halves the chain.

**M3. Reach freezes a bot = bait verb.** "A bot that sees a human reach toward it stands still": with the wolf near,
standing still is death (`is_still`). A human can feint a reach (2.5 s `REACH_LEN`, repeatable) to feed a bot.
Fix: bots ignore a reach while a creature is out; say what wins, the stand-still or `_evade`.

**M4. Trust through walls.** "12 m, line of sight not checked" gives bots a sense players lack (critic log: copying bot
perception copies privileges; design: bots see only what a player could). Fix: a line-of-sight ray.

**M5. T is unspecified at its edges and undiscoverable.** What does T do for a healthy friend, or one with only a mild
symptom (curse 0, always "too early": a free fake "I'm turning" tell every 20 s)? With `screen_ui` off, "T in the
controls table" means `docs/build.md`: nobody in the night finds it (anti-pattern 16).

**M6. Decides for the user.** `near_head_start` is a user step-1 cut, Q-B3 and Q-B4 are still "waiting" in
questions.md. "Implement all steps" covers building, not answering open questions; tag them (Claude) and keep both
behind switches.

## Minor
- One scale for "late": the thesis mixes curse 0.6 and veins 0.6 (`veins(p)` is 0 below p = 1/3; veins 0.6 = curse
  0.73), and `body.gd` grows the neck mark smoothly, with no "on the face" step. Bot nerve 0.55–0.85: say which scale.
- A second bubble kind (vein marks) contradicts "only this bubble shows"; the user asked only for deal bubbles.
- "Bots stop dropping their items when sick" (they drop today, `bot.gd _patient`) raises hoarding; with 16 hands for
  16 items at 8 friends, check empty spots in the playtest.
- Mirrors drop taught rule 1 "you can't see your own face" without saying so (the user offered mirrors; still list it).
- Trust +2 for the human's give but +1 for any seen give: an unexplained special case.
- Part 3 (pick B, nothing to build) and the one-hand rejection: pass (steal/tug, deal bubble, two hands are user's).

## Co-op check (deal + turn early)
1 coupled pass · 2 split fail (the mirror makes your own state solo) · 3 talk pass at 8, fail in the test crew (bots
can't be talked to) · 4 blame pass (kept item, strain) · 5 not easy fail (assumed: idle bots fetch the human's item
for free, so a deal is rarely needed) · 6 not solo pass · 7 two-way fail (the bot only reacts).
Turning on purpose makes it easier (S1): fail.

## Pillars bent without saying so
Betraying never pays more than curing (S1); helping beats fleeing, listed as kept (S2); bluff from both sides (S3,
the test crew); "you can't see your own face" (mirrors); bots see only what a player could (M4).

## Rules a player must know
Before ~10: two hands, pick, give 2 s on a still friend, hold, steal/tug, throw/drop, symptom ↔ item, nobody treats
themselves, mild turns into a case, wolf (moving = knocked, still = eaten, raise wolfsbane).
After ~15: + T and when it works, the strain tell, key 9 and the marks, mirrors, the deal bubble (give first, get
theirs); the head start is invisible to the human. Taught: none, and T can't be found in the night.
Cutting T and 9 (S1, M1) leaves +2: mirrors (found) and the deal bubble (reads itself).
