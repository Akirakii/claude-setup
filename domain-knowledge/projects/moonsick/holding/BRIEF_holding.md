# Brief: design holding a friend

**Goal (user's words, 2026-11-13):** "create a separate session for desining holding". This is a design session
with the user present: design how holding a friend works in Moonsick, together with them.

**Project:** `~/Playground/moonsick` (main worktree). This session starts in `~/claude-code`, so read
`~/Playground/moonsick/CLAUDE.md` first (it doesn't load on its own).

## The user's original words on holding (2026-11-12, verbatim)
"also for restraining a player.. you can use one hand so it physically goes to the person to restrain. it just creates
a link.. where you have to push back and hold the click to deaccelerate the player.. if you dont move then the other
player can scape"

## Where things stand
- **Built today, untested by the user:** holding is the mouse click. Aim an empty hand at a friend close by and hold
  the button; let go to release. The held friend still freezes and mashes Space to get free (the old F grab), the
  holder walks at 0.35 speed and can't give, take or raise while holding, and holding halves the curse.
  Code: `scripts/game/player.gd` (`_hold_hand`), `scripts/core/hands.gd` ("hold"), `night_sim.gd` `grab` / `release`.
- **The werewolf's catch is already a stretch link** (the victim walks away, the werewolf holds S to pull back, 2 m
  of stretch snaps it). That's the user's link idea, built for the creature only.
- **The open problem (`docs/questions.md` 19, critic hands r1, severe):** in step 1 nobody wants out of a hold
  (werewolf only, nobody lies), so the friend-on-friend link only works on bait, and the holder's side is "always
  pull" (co-op check point 7 fails). The user hasn't answered it.
- **Holding meets the symptoms design**, which the main session is working on (`docs/symptoms-thesis.md`): there,
  holding slows the curse ×0.75, and the first pick failed the co-op check (one player can handle every case alone
  for the first two thirds of the night). Hallucinations as private symptoms were just proposed, not yet accepted.
  A good holding design can help here: a reason to hold someone, or to pull away.

## Read first (absolute paths)
1. `~/Playground/moonsick/CLAUDE.md`, then `~/Playground/moonsick/docs/design.md` ("Hands", "Holding and knocking
   out", "Step 1 cuts").
2. `~/Playground/moonsick/docs/hands-thesis.md` (r1 "The link", the co-op gate, synthesis r3) and
   `~/Playground/moonsick/docs/critic-hands-r1.md`, `r2.md`, `r3.md`.
3. `~/Playground/moonsick/docs/questions.md` 16–22 and `~/Playground/moonsick/docs/REPORT_hands.md`.
4. `~/Playground/moonsick/docs/symptoms-thesis.md` (read only, see limits).
5. `~/.claude/design-anti-patterns.md` before showing any sketch (rule 18), and `~/.claude/notes/critic-anti-patterns.md`.

## Limits
- Design with the user: question the premise, sketch before building, look for existing solutions with a web search
  first (rules 4, 5, 10). No critic round unless the user asks (rule 20: the user is the critic).
- Write the design to `~/Playground/moonsick/docs/holding-thesis.md`. Don't edit `docs/symptoms-thesis.md`: the main
  session owns it. Put open choices in `docs/questions.md` (append, don't renumber).
- Build code only if the user says so. No commits, no push.
- Rules 14–15 for any game run: don't run the game to check work; if something must launch, headless, or muted,
  small, bottom-left, never taking focus.

## Result
When the user is done, write `~/Playground/moonsick/docs/REPORT_holding.md`: short, small ✅/❌ tables (coworker
style). Include what was decided (tag the user's calls "(user)" and Claude's "(Claude)"), what's still open, the
files changed, and anything that touches the symptoms design.
