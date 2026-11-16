# Items research: how other games make delivering an item a team job (2026-11-13)

**The general patterns and their sources moved up to `~/.claude/domain-knowledge/shared/game-patterns/team-item-delivery-patterns.md` (2026-11-16); what stays here is what was specific to Moonsick.**

Tags: [source] = a cited page, [read] = read in a cited page and summed up, [opinion] = Claude's own.
Done with the design-research skill (no project code read).

## The user's limits (their words)
- The symptoms define the cure, item by item, no potion (user, 2026-11-12/13).
- Funny moments to mess up: "less ways for a funny moment to mess up" was the user's worry about item by item (user).
- Two hands, one mouse button each (user).
- No screen UI and no world text in step 1 (user).
- Cooperation, not parallel play: Deathly Reality Show's minigames were "too simple, too easy, and with no
  cooperation" (user, from `~/.claude/design-anti-patterns.md` #24).
- 4–8 friends (user); the fewest-players test is 1 human + bots (Claude's practice setup).

## Fit to the limits
| Pattern | Item by item | Funny mess-ups | Two hands | No text | Needs a team | Few players / bots |
|---|---|---|---|---|---|---|
| Prep before use | ✅ | ✅ | ✅ | ✅ | ❌ one player can do the chain | ✅ |
| Big shared items | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ assumed: bots must take the other handle |
| Fragile items | ✅ | ✅ | ✅ | ✅ | ❌ a careful player does it alone | ✅ |
| Heavy, two-handed | ✅ | ❌ | ✅ | ✅ | ❌ alone it's just slower | ✅ |

## Recommendation (Claude)
**Big shared items**: the only pattern that passes "needs a team". The sources use weight (too heavy for one
person), not handles; handles were Claude's own guess and are dropped: grab anywhere, alone you drag it slowly, two
lift it (Claude, waiting on the user). R.E.P.O. also makes its big loot fragile, which brings in the runner-up's funny mess-ups: the item spills or
breaks when one carrier lets go or they hit a doorway. Fragile items do the mess-ups better and cost nothing to
learn, but alone they don't need a team.
Watch for: one player lifting it with both hands (weight counts per person, not per hand), and the follower who
only obeys (both carriers must matter, e.g. the item tips when they pull different ways).

