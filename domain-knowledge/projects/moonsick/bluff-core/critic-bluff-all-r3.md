# Critic, round 3: bluff-all fixes in code, 2026-11-15

Read: critic r2, thesis merge table, `bot_mind.gd`, `bot.gd` (`_find_patient`, `_afraid_of`, `_bail`, `saw_give`,
`_deal`, `_someone_needs`, `_patient`, `_treat`), plus `night_sim.gd` (`_tick_mild`, `_treat_mild`) and
`game.gd` (`_bots_saw_give`) to follow the calls.

## Verdict: both fixes are in the code, and both are cancelled by other lines next to them
- S1 fix (trust below 0 = no treatment; 25 m cap): written, but the penalty almost never fires. Stiffing is still free.
- S2 fix (healthy bots leave the deal's symptom alone): written, but a fallback line takes that symptom back whenever
  it's the only one showing, and a mild symptom is always just one.
- Pillar "betraying never pays more than curing": holds. Stiffing a bot saves a trip (time), never points.

## Scene, 1 human + 3 bots (Bo, Cy, Di), second by second
- Before: the human treated Cy in Bo's sight, so Bo trusts them at 1, and `who_first` gives "bot".
- 0 s: the human yawns (mild). Bo has stink (mild, already 10 s old) and holds a coffee; a perfume lies 20 m from the
  human. Bo is 4 m away, so `_deal` opens "[coffee] for [perfume]" with stage `bot_first`.
- 0 s: Di is healthy, 6 m away, and sees the yawn. `_treat` puts "yawn" in `taken` (Bo's deal)... then
  `if want == "" and not sym.is_empty(): want = sym[0]` picks yawn anyway. Di heads off to fetch a coffee (80 m reach).
- 1–3 s: Bo walks up and gives the coffee. The yawn ends. Stage `owed`, t = 3.
- 3 s: honest = sprint 20 m, pick up, sprint back, give: done at ~10 s. Lie = walk off. Bo follows the human (`owed`
  falls through to `go(f)`).
- 3–20 s: Bo, sick, trails the human. Cy or Di sees the stink within 7 m and treats Bo (bots treat bots; nothing
  leaves Bo's stink to the human). Bo is cured around 15–25 s.
- Next think: `_my_needs()` is empty, so `_deal` calls `_end_deal()` with no `broke_deal`. Bo's trust in the human
  stays 1. **The lie cost nothing, again.**
- Only if no one treats Bo for 45 s (PAY_WAIT) does trust drop to −1. Bo's mild started 10 s earlier, so it turns
  into a full case at 35 s; Bo still needs the perfume, so the penalty would fire at 48 s.
- Same scene at trust 0 (stage `friend_first`): the human fetches and gives the perfume. `_treat_mild` clears Bo's
  mild on the spot, so on the next think Bo isn't sick any more: `_patient` takes the not-sick branch and calls
  `_end_deal()` before stage `pay` ever runs. Bo keeps the coffee. It's saved only because Bo, now healthy and
  trusting the human at 1, picks the human as a patient and gives the coffee as a doctor.

## Severe
- **S1. The S1 fix doesn't hold: stiffing is still free in most nights.** The penalty fires only if the bot is still
  sick with the wanted symptom 45 s later, and with 2 healthy bots someone treats it first. Then `_deal` ends the deal
  with no penalty, either at its top (`needs.is_empty()`) or in the `owed` branch (`not needs.has(want)`). So "always
  take first, never pay" always wins the deal. Fix: once the human owes, any end of the deal other than being paid
  counts as broken (call `broke_deal` in `_end_deal` when stage is `owed`, cured by someone else or not). Or set
  PAY_WAIT to about 15 s, well under the time a bot doctor takes.
- **S2. The S2 fix doesn't hold for one symptom.** `_treat`'s last fallback (`want = sym[0]`) ignores `taken`, and a
  mild symptom is always one symptom, so the healthy bot still races the deal. Fix: make the fallback skip symptoms
  left to a deal. If nothing else is left, stand by the patient without fetching, or skip the patient in
  `_find_patient`.

## Medium
- **M1. A trust-0 deal never pays out as a deal.** After the friend pays first, the cure clears the bot's mild, and
  `_patient` ends the deal before stage `pay`. The bot keeps its item, and it reaches the human only by luck (Bo then
  treats the human as a doctor; this fails if another bot is already doctoring that symptom, or if Bo is afraid).
  Fix: run stage `pay` before the not-sick check (finish a `pay` deal even when healthy).
- **M2. The penalty is undone by one give.** `broke_deal` sets −1, and any give the bot sees adds +1, which puts
  trust back to 0: the bot treats you and deals with you again. A betrayal costs one give in the bot's sight. Fix:
  make a broken deal −3, or only let a give to that same bot count back.
- **M3. In the `owed` stage, a sick bot follows the human for up to 45 s.** That drags it away from its own doctors,
  and the human can lead it out of their 7 m sight range. Fix: while owed, the bot stays put or goes back to its doctors.

## Minor
- The nerve range in the code (0.35–0.75) doesn't match the thesis (0.55–0.85). Pick one and change the other.
- `_someone_needs` uses 10 m (OFFER_RANGE × 2) and the offer uses 5 m, so a bot holds its chip in the 5–10 m band
  without offering it. That's fine; just say so in the code comment.
- Fear (`_afraid_of`, `_bail`) now reads public veins within 7 m, which closes r2 M3. It passes.
- M2 from r2 (trust farming): only `treated` and `cured` events count, so bursts don't farm trust. It passes.
