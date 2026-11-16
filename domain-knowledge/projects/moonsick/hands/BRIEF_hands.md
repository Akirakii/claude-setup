# Brief: build the hands

**Goal (user's words):** "i click left or right but still no hand appearing and no holding player mechanic" →
"ok then implement in a worktree". Only the design exists; no hands code yet.

**Where:** the worktree `~/Playground/moonsick-hands` only (branch `hands`). This session starts in `~/claude-code`; all paths below are in the worktree. Never touch `~/Playground/moonsick`
(the main worktree). No commits, no push; leave changes uncommitted.

## Read first
1. `CLAUDE.md` and the build/run docs it points to.
2. `docs/hands-thesis.md`, especially "Smallest build", and `docs/critic-hands-r1.md`, `r2.md`, `r3.md`. The
   synthesis in the thesis is the spec.
3. `docs/questions.md` items 19–22. The user hasn't answered them yet, so build Claude's pick for each and keep it
   easy to change:
   - 19: the werewolf's catch is the hold link. The victim pulls away, the werewolf pulls back, and a raised
     wolfsbane breaks it.
   - 20: a hand shows only while reaching, holding, giving or raising, never while healthy and empty.
   - 21: G drops one item per press, left hand first, and E stays pick up.
   - 22: shove range ≥ catch range + LAG. Fix it only if it's a one-line constant.
4. `~/Playground/refs/README.md`: read the matching reference repos (items, movement, multiplayer, animation) before
   building, and copy their patterns (CLAUDE.md rule 19).
5. `~/.claude/notes/machine-setup.md` for how to run the tests and the game headless.

## Limits
- Smallest version the user can try: one mouse button per hand, a hand that reaches, take/give/raise/eat by world
  state, G drop, the werewolf catch link. Cut anything that grows past that and list it as a gap.
- Multiplayer: follow the repo's existing networking pattern.
- Rules 14–15: don't run the game to check your work. Run the test suite once, after all edits. If anything must
  launch, run it headless, or muted, small, bottom-left, never taking focus.

## Result
Write `~/Playground/moonsick-hands/docs/REPORT_hands.md`: short, small tables with ✅/❌ (rule 21). Include the files changed, what works, the
test result (with the output if it fails), the gaps cut, and anything that goes against the thesis. Mark everything
as untested by the user.
