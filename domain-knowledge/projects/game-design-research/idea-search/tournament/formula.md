# Method tournament: the target and the checks (2026-11-10)

User's ask (2026-11-10, their words): "you can try different agents try diferent methods.. evaluate
what what and what doesnt then again try different methods in parallel.. and survive only those that
are checking better against the formula. also another check is not duplicate an existing idea. dont
think about testing yet." Budget: 1 hour, user AFK.

## The target
An online co-op game for 3–6 friends on voice chat, made by one developer in about 3–4 months.
User's formula: "low content, low coupling but only high coupling on players". The fun should come
from what friends do to and with each other, so the game needs few hand-made parts and few features
that depend on each other, while the players depend on each other a lot.

Allowed shapes: **co-op** (everyone on one side against the world) or **semi-co-op** (one shared
goal plus a private stake, or one hidden traitor). Not team vs team, not free-for-all.

## Checks (score each: ✓ = 2, ~ = 1, ✗ = 0, n/a = 2)
- **F1 low content:** what works against the players is picked by humans, physics or one simple
  system, not hand-made levels, enemies or scripts. 10 fresh rounds need at most 3 arenas plus one
  short list (≤ 20 items). An NPC crowd that must pass as human is content (~).
- **F2 low feature coupling:** the core rule fits in one sentence; at most 2 extra rules sit on the
  hub (the one shared thing everything uses); no rule rewrites the hub.
- **F3 high player coupling:** my best move changes with what another player just did; players do
  different actions that fail without each other. Fails (✗) if: everyone adds to one pooled bar or
  sum; everyone does the same job side by side (parallel play); one end of a coupling only obeys or
  waits (a pressure plate); one player knows everything and directs (a quarterback).
- **F4 visible blame:** when a run fails, one visible person's action caused it, seen in the moment
  (not a hidden number, not luck).
- **F5 crew 3 and 6:** works at 3 and at 6, odd sizes too; no idle seat; nothing breaks at 3.
- **F6 hidden things:** if something is hidden, players have a verb to uncover it and a reason to
  hide it. n/a if nothing is hidden.
- **F7 tail:** something keeps round 50 new without hand-made content (the players, generated
  layouts, physics).
- **G co-op gate:** time pressure makes people talk; new players at 3 can lose; one player or one
  fast carrier can't clear it alone. (✓ all three, ~ one weak, ✗ one fails.)
- **N novelty:** no existing game (video, board, card, party, playground) has the same core rule.
  ✓ nothing close found; ~ a known game shares the core but this one changes who decides what;
  ✗ the same core rule exists (name it). A re-skin of an existing game is ✗.

Max score 18. **Pass** = no ✗. **Strict** = every check ✓ (n/a counts as ✓).
**Method fitness** = passes among its ideas, then mean score, then how many different families.

Left out on purpose (user, 2026-11-10: "dont think about testing yet"): whether bots or the
user's test crew can run it.

Not scored, recorded only: fantasy and look. The user's triad (fantasy + logic + aesthetic aligned)
can't be checked in the head (their own finding), so the score sees only the logic.

## Idea format (every generator uses it)
```
### <method id>-<n> <Name>
- Rule (one sentence):
- Hub (the one shared thing everyone uses):
- Coupling (how my best move depends on what a friend just did; who does which different action):
- Fantasy (who you are, what you're doing):
- Look (one line):
- At 3 / at 6:
- Hidden (what, how it's uncovered, why anyone hides it) or "none":
- A failed run (what happens, who is blamed):
```

## Gen 2 additions (2026-11-10, after gen 1 scoring)
Gen 1: F7 tail and N novelty were the checks almost every idea lost a point on. Gen 2 ideas add one
line to the format, and generators may run one web search per kept idea (after generating, never before):
```
- Tail (what makes round 50 different from round 2, with no hand-made content):
```
