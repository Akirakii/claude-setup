# Todo: the bluff design (2026-11-15)

From `design.md` (Trust and bluff) and `bluff-research.md` (rounds 14–22 and the chat after).
User: "based on all of this.. create a todo list for implementing in the game".
Tags: (user) = the user's words chose it; (Claude) = Claude's pick from the chat, not yet in design.md.
**Parts 1–6 are built or cut (2026-11-15, untested by the user; `docs/REPORT_bluff-base.md`, `docs/HANDOFF_bluff-all.md`). Part 7 is your playtest.**

## 1. Clean up what's already decided
- [x] Remove holding's slowdown from the code: holding only pulls (user).
- [x] Rewrite "The game in one sentence" in design.md: it still describes the old signs and cures.
- [x] Add the chat picks below to design.md once each one is played in a simulation (thesis + 3 critic rounds).

## 2. The base the bluff stands on
- [x] The werewolf's new attack: knockback, a helpless recovery, and it eats a friend who isn't moving at once (user).
- [x] Everyone a little sick: one mild symptom per friend every 90–180 s; untreated for 45 s, it starts a full case (user OK, numbers in `sims/mild_sick.py`).
- [x] Nobody treats themselves, the last one alive excepted (built; check it still holds with mild symptoms: it does, tested).

## 3. Simulate first, then pick one (decides parts 4–6: deal bubbles, bot fetching and trades change with it)
- [x] Cures as places vs carried items: carried (Claude, simulated: places drops two user features). Places would drop steal/tug, trading and hoarding's job.
- [x] One hand instead of two: no (it breaks the user's two-hand design).

## 4. Knowing your own state
- [x] The sick friend feels their symptoms (yawns, nausea) but not their progress (already true).
- [x] Mirrors in the mansion show your own veins: two, study and dining room, by moonlit windows.
  Claude: put them in moonbeams, so looking costs something: moonlight speeds a case ×1.5 (design.md, The night).
- [x] Others see your veins roughly, as now (built).

## 5. Turning early
- [ ] ~~The sick friend can choose to turn early~~ cut: it pays more than curing (critic r1; questions.md Q-B6).
- [ ] ~~When "late" starts~~ cut with it.
- [ ] The head start: kept off; the critic's numbers are in questions.md Q-B3 (yours).

## 6. Bots and talking
- [x] Bot fear: a bot bails late in a case (user OK).
- [x] Bot trust: a bot trusts a friend by the gives it saw itself, and never tells anyone (user OK).
- [x] Bot deal bubbles with item icons and words, no arrows: "[bucket icon] for [coffee icon]" (user; small item models).
- [x] A way for the human to offer a deal to a bot: hold an item out toward the bot (Q-B4, Claude's pick).
- [ ] ~~Bots answer "how bad are my veins?"~~ cut: the lie had no motive and the mirror answers it (critic r1).

## 7. Check in playtest
- [ ] Do friends really remember broken promises and refuse each other? (bluff lines 3 and 4 are assumed)
- [ ] At 8 friends, do item spots go empty?
- [ ] The test crew (1 human + 3 bots): can the human bluff at all?
- [ ] The last minute before dawn: lies cost nothing there (user's call; Claude: keep it as the run for dawn).
