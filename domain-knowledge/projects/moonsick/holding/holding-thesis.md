# Holding thesis: holding a friend (design session with the user, 2026-11-13)

**Built 2026-11-14 (user: "implement."), not committed, untested by the user.** Claude's picks below were taken as
asked: no time limit, the catch uses the same chain, every reach 20% shorter. Before: the click held a friend, the
friend froze and mashed Space to get free, the holder walked at 0.35.

## As built (Claude's numbers)
- Pull = the holder's input pointing away from the held one × their actual speed (full at 1 m/s), so keys pressed
  into a wall are no pull. The host sends [holder, chain length, pull] 20×/s; the held one's client caps its own
  speed away (walk × (1 − pull)) and adds a drag back toward the chain's length (10/s, at most 8 m/s; it trails
  ~0.4 m behind a walking holder). The host snaps it at chain length + 2 m + its 0.6 m lag allowance.
- 0.5 s grip at the start for both (the old catch link's grip); a 3 s guard after a snap.
- The grip spot: a ray march (2 cm steps) against the body's torso capsule and head sphere in the body's own space,
  packed to one int (1 cm steps) and sent with the grab or catch request; others draw the arm to it every frame.
- Bots: a healthy held bot walks off its holder; a sick one goes along; a catching bot walks straight away from its
  victim (into a wall it stops, so the victim can slip free).

## The user's words (verbatim)
- 2026-11-12: "also for restraining a player.. you can use one hand so it physically goes to the person to restrain.
  it just creates a link.. where you have to push back and hold the click to deaccelerate the player.. if you dont
  move then the other player can scape"
- 2026-11-13: "a player a holding b / if a pulls.. then b should be moved by a / if a is still and b tries to scape
  then the chain is broken" · "also hold should land on a part of the body and stick there instead of a fixed
  coordiante" · "also arm should be 20% shorter"

## The chain (sketch r1)
A holds B with one hand while the button stays down (user). The chain is a leash from A's hand to B.
- **The hand grips where you aim (user):** it lands on the spot of B's body under your aim (shoulder, arm, back,
  head) and stays stuck to that spot as B moves and turns. Today it always goes to a fixed chest point
  (`game.chest_of`). Claude: the grip spot is kept in B's body space and sent with the hold so everyone sees the same
  spot; the rules still measure feet to feet.
- **The arm is 20% shorter (user):** hold reach 1.8 → 1.44 m, chain length 1.5 → 1.2 m. Open: every reach
  (items 2.6 → 2.08 m, giving the same) or holding only; Claude's pick: every reach, one arm length.
| A does | B does | What happens |
|---|---|---|
| walks away from B (chain taut) | anything | B is dragged behind A (user) |
| stands still | walks away | the chain stretches and breaks (user), after B gets 2 m past the chain's length, about half a second at a walk (Claude, today's catch-link stretch) |
| walks toward or beside B | walks away | not a pull, so it stretches and breaks the same way (Claude) |
| anything | stays within the chain length (1.2 m) | slack: both move freely (Claude) |
- "Pull" = A's movement points away from B while the chain is taut (Claude). A can face any way: walking backward
  while watching B and turning to walk off both pull. No planted feet (replaces the catch link's planted S).
- A drags a resisting B at half a walk, a willing B at a full walk (Claude). B can't sprint while held (Claude).
- The held friend no longer freezes or mashes Space (the user's rule replaces it).

### What follows from it
- **A small duel:** B gets free by making A stop pulling, by darting past A so A ends up walking toward them.
  A keeps B behind by turning. Both decide at the same moment (co-op check point 7 passes when B resists).
- **The holder decides where to take B** (critic hands r1 #5 asked for this): to the person with the item, out of a
  werewolf's way, or toward it as bait (the user's bait pillar).

## Gaps (Claude's picks)
1. **A can drag B forever** by walking in loops (B trails behind, so A is always pulling). Critic hands r1 #4: a hold
   must end. Pick: no cap for the first playtest; A can't give, take or raise while holding, so a long drag costs A.
   If it shows up as griefing, add a cap.
2. **The werewolf's catch uses a different chain** (planted S brakes the victim). Pick: one chain rule for both; the
   werewolf drags its victim during the 2 s catch, and a friend's raised wolfsbane still breaks it.
3. **Why B would pull away in step 1 is still open** (questions.md 19). The drag gives B a reason only when A takes them
   somewhere bad (bait, away from help). Honest step-1 play still has no reason to resist.
4. **Lag (assumed):** B's client owns B's movement, so the drag runs on B's client from A's pose (20 Hz + half the
   round trip): B trails a little behind where the host thinks. Same path as the catch-link brake today.

## Anti-pattern check (`~/.claude/design-anti-patterns.md`)
B15 shallow choice: pass (where to drag, keep B behind) · B17 exploit: fail as is (gap 1, endless drag) · B19 not
specified: network and blame open (gap 4) · A5 unproven premise: fail (gap 3, no motive to resist in honest step-1
play) · state change mid-action: the half second of stretch is the grace when A pauses at a corner.
