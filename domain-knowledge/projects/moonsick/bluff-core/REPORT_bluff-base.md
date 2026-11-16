# Report: bluff base, todo parts 1 and 2 (2026-11-15)

**Built, not committed, untested by the user.** Stopped before part 3 (cures as places vs carried), as the brief said.

| Task | Done? | Tested by the suite? |
|---|---|---|
| Holding no longer slows the curse | ✅ | ✅ |
| "The game in one sentence" rewritten | ✅ | ❌ (a doc) |
| The werewolf's new attack (switch `wolf_attack`) | ✅ | ✅ host rules · ❌ knockback feel, the lying-down look |
| Everyone a little sick (switch `mild_sick`) | ✅ | ✅ host rules · ❌ bots treating it |
| Nobody treats themselves, still true with mild symptoms | ✅ | ✅ |

Test run: **118 of 118 passed** (headless GUT, two new test files).

The game wasn't run.
The game scripts only got a compile check, and that check stops early on the sound autoload, so a game-side typo could still be hiding.

## Claude's picks (all tagged (Claude) in design.md)
- **Both new switches are on by default**, like `symptoms`.
- **The werewolf's hit** throws the friend about 2.4 m with a small hop, and they're helpless for 3 s.
  Helpless means no moving and no hands: a raised cure drops, and a friend they held is let go.
- **The werewolf waits 1.5 s between strikes**, so friends get about that long to grab and drag a knocked-down friend before it can eat them.
- **The strike reaches as far as the old catch** (1.36 m), and raised wolfsbane still shoves the werewolf back.
- **Not moving** is measured as the path walked over the last second, so walking in a circle counts as moving.
- **The knocked-down friend lies like a knocked-out one**, with eyes shut.
- **A friend's mild-symptom clock pauses** during a case and for the 60 s after a cure.
- **A mild symptom shows no veins**, and a wrong item on it bursts, the same as on a case.
- **A random case on a friend with a mild symptom** uses that symptom as its first one.
- **A bot with a mild symptom** waits by a friend for help, the way a sick bot does.

## Left
- The last part-1 item stays open: adding the chat picks to design.md waits until each one has been played in a simulation.
- Bots don't drag knocked-down friends and don't avoid standing still near the werewolf.
- The "Taught to a new player" section in design.md still describes the old signs and cures.
- Playtest checks: whether 1.5 s is enough time to save someone, and whether the knockback looks junky enough.
