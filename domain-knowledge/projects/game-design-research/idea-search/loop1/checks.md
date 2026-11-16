# Checks for loop1 (2026-11-10 night)

Tests for P and R come from `research/player-interaction.md` and `research/routine-failure.md`.

## The target
An online co-op game for 3–6 friends on voice chat, made by one developer in about 3–4 months.
User's formula: "low content, low coupling but only high coupling on players". The fun should come
from what friends do to and with each other: few hand-made parts, few features that depend on each
other, players who depend on each other a lot.
Allowed shapes: co-op, or semi-co-op (one shared goal plus a private stake, or one hidden traitor).

## Gates (in order; the first ✗ stops the idea; ✓ = 2, ~ = 1, ✗ = 0, n/a = 2, — = not scored)
1. **P player-with-player interaction** (all must be yes; ✓ all clearly yes, ~ one is weak, ✗ any is no):
   1. My action lands on **one specific teammate** (their body, view, options or next move), not on a pool
      everyone adds to, and not on a job I could do alone, only faster with help (Depping & Mandryk 2017;
      Reuter et al. 2014: pooling and parallel work are the failures, a shared object is fine).
   2. That teammate must **answer within seconds**, so it becomes a back-and-forth where both decide
      (Cook's reciprocation loop; Depping 2018: the social effect rides on back-and-forth).
   3. **One named teammate can be helped or hurt** by it (Depping 2018: "only vulnerable to a partner if
      they can be potentially hurt or helped by that person").
   4. **Still two-way by round 5** (added after round 1, where 19 of 54 ideas failed this at the co-op gate):
      in the plan the crew will settle into, do both ends still decide? ✗ if one end only waits, holds,
      obeys a call, or is moved like a puck; ✗ if the friend act is optional and worse than a solo move.
2. **Formula:**
   - **F1 low content:** humans, physics or one simple system make the opposition; 10 fresh rounds
     need ≤ 3 arenas + one short list.
   - **F2 low feature coupling:** the rule fits one sentence; ≤ 2 extra rules on the hub; nothing rewrites it.
   - **F4 visible blame:** a failure is one visible person's action, seen in the moment.
   - **F5 crew 3 and 6:** works at both, odd sizes too, no idle seat.
   - **F6 hidden things:** a verb to uncover and a reason to hide (n/a if nothing is hidden).
   - **G co-op gate:** time pressure makes people talk; new players at 3 can lose; one player can't carry it.
3. **R no fixed plan** (✓ = question 1 is no and 2–4 are yes; ~ = one of 2–4 is weak; ✗ = question 1 is yes):
   1. **Plan card:** could the team write one plan on a card before round 2 that still wins round 50?
   2. **Which, not whether:** does something revealed at the start of or during a round (a deal, a layout,
      a threat's choice) change *which* plan is best, not only *whether* it works? Physics wobble alone
      is a no (Elias, Garfield & Gutschera: chance after the decision keeps the same strategy).
   3. **Pushback:** does something answer the team's habit: a threat that targets what the team keeps
      doing, a rule that isn't fully predictable, or a player with a private reason to break the plan?
   4. **Still talking:** by round 20, does each player still need to hear something from a teammate that
      they couldn't have known before the round?
   5. **No lookup line** (added after round 1, where 15 of 17 ideas reaching R failed): ✗ if one line beats
      the threat ("act from cover", "hand it to whoever is farthest", "rotate"), if a safe spot cancels it,
      or if it simply hunts whoever holds / did / is most X (fully predictable, so steerable).
4. **N not an existing game:** ✓ nothing close; ~ a known game shares the core but this changes who
   decides what; ✗ same core rule (a re-skin is ✗).

Recorded, not scored: fantasy, aesthetic. Not checked yet: online lag on same-moment actions (note it).

## Idea format
```
### <method id>-<n> <Name>
- Rule (one sentence):
- Fantasy (who you are, what you're doing):
- Aesthetic (one line):
- Player on player (what my action does to a friend, and what they decide back):
- Why the plan can't settle (what changes round to round because of the players):
- Hub (the one shared thing everyone uses):
- At 3 / at 6:
- Hidden (what, how uncovered, why hide) or "none":
- A failed run (what happens, who is blamed):
```
