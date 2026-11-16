# Dungeon Pets: postmortem (status: FAILED, archived 2026-10-31)

A first-person dungeon roguelike where a pack of creatures (12 species, each with evolution paths)
fights alongside the player. About 9,400 lines of GDScript over 3 days (2026-10-29 to 10-31) and
19 Claude Code sessions. Work continues as a new game, **Assemblia** (`~/Playground/assemblia`, repo Akirakii/assemblia).

## Why it failed
**The user's final playtest (2026-10-31):**
1. **The player was far too strong and never needed to decide anything.**
2. **The screen couldn't be read:** too many creatures, no clarity.
3. **Managing each creature one by one was a chore.**

**Root causes** (analysis; the playtest is checked, the causes are reasoned, not measured):
- **No pressure on pack size.** Power grew with headcount, and the pack was later made unlimited.
  Taking every creature was always right, so the main choice had one answer. Upkeep was meant to
  stop this and was too weak.
- **Unique individuals instead of a system.** Each creature had its own diet, evolution path, gear
  and HP, so the work grew with every creature, and each one added clutter on screen.
- **The player could do the work.** The player's own fighting won fights, so the pack's build
  stopped mattering (the Brütal Legend failure).
- **Strategy was added as layers, not built into the core.** Relics, gear, evolution, reactions,
  threats, eggs and upkeep were stacked on before the core loop was fun. Each one was reasonable
  alone, and together they added bookkeeping, not decisions.
- **First person hid the systems.** The interesting part (the pack's composition and reactions)
  is read from above; first person showed a slice of it at ground level.
- **Effort went to art before the core was proven.** Several Meshy redesign rounds, including the v21
  Emberpup restyle, ran into rig and proportion problems and were dropped.
- **Bot measurements didn't measure fun.** Careless-vs-careful bot runs showed small differences
  (+0.8 floors) and couldn't see clarity or tedium; the user's playtest found those at once.

## Lessons carried into Assemblia
- **Prove the core loop first, in the cheapest form,** before art, content or meta systems.
- **Decisions must come from the core,** not from added layers.
- **Many units only work as a system:** rules per type, never care per unit.
- **The player supports the army; their own action can't win a fight.**
- **Pick the camera that shows where the decisions are.** For a systems game, that's top-down.
- **No priority systems to patch the automation;** the automation has to work by itself.

## Where things are
- **Design and rules:** `DESIGN.md`
- **Research log, including the pivot reasoning:** `docs/research.md` (from "Playtest: too strong")
- **The constraints that started the new game:** `docs/constraints.md`
