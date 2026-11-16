---
name: generate-ideas
description: Keep a living pool of game ideas that pass the user's formula (low content, low coupling between features, high coupling between players). Each cycle fixes failing ideas, improves passing ones, adds new fantasy-first ideas written as job / choice / goal, checks them, and grows the understanding of how ideas work and how to improve the method. Main session only, no subagents. Use for "generate ideas", "find game ideas", "idea search", "keep improving the ideas".
---

# Generate ideas (a living pool, fantasy first, no subagents)

Everything runs in the main session, with **no subagents** (the user's call).
The critic from `~/.claude/CLAUDE.md` rule 20 is a pass inside the checks here.
Read `lessons.md` first: it holds how ideas work, why they fail or pass, and every method change.

The work is a **cycle** over a **living pool**, repeated as long as the user wants: fix the failing ideas, improve the passing ones, add new ones, and keep learning how ideas work and how to improve the method.

## The pool
One file: `~/.claude/domain-knowledge/shared/game-ideas/pool.md` (older versions in `pool-history/` next to it).
- **Ranking** (Claude's pick, with reasons) and the shape tags, at the top.
- **Passed**, grouped by **core** (ideas whose rule is the same): the [job] [choice] [goal] line, its look, its shape and its weak spots (~).
  Skins (new fantasies on an old core) are listed under their core.
- **Rules**, **Scenes** (3 and 6 players) and **Long scenes** (rounds 1, 5 and 20, and second looks after fixes).
- **Failed:** the idea itself, the check where it stopped and why, and how many fixes it has had.
- **Dropped:** ideas out of fixes, with the reason, kept so they don't get made up again.
- **Cycle log** at the end: one short entry per cycle (what was fixed, improved, added, learned, changed).

## The cycle (each step in order; one cycle per run unless the user says more)
1. **Fix the failing ones.**
   For each failed idea, write one fix aimed at the exact check it failed (change the job, the choice, the goal or the setup), then check it again.
   After 2 failed fixes, move it to Dropped.
   An idea that died at the fixed-plan probe (B) gets **one** fix only: 1 of 8 such fixes passed, while ideas that failed later checks were fixed 4 of 4.
2. **Improve the passing ones.**
   Take away one ~ per idea: sharpen the choice (section C), or remove the content or lag risk behind the ~.
   Check again whatever the change touches.
   First apply the fixes the rule critics named for ideas leaning ✗.
   After any fix that moves the danger, check that the job still pulls the danger in (a wandering moonbeam once let the crew relax while it was elsewhere).
   - A content fix that worked: freeze the opposition or give it one rule (ghosts stand still, guests sit, raiders walk straight).
     The cheapest opposition is a cursed friend.
   - **Rule step:** for 2 older passing ideas still marked "needs a rule", write the one-sentence rule (at most 2 extra rules) in the pool's Rules section, then run the critic on it (`checks.md` 4.6).
     A rule can demote an idea, or show it's a skin of a core.
   - **Sweeps:** once a cycle, over every core, run every probe lesson again.
     A solo exit (a way out without the friend), a safe spot (a place the threat can't reach), a dump (one player soaking up the harm), help that costs only time (one player becomes the helper), one resource handed around, identical players, anyone idle at 6, harm decided by a dice roll, a goal that rules out one side of the choice.
     Old passes are older than later lessons.
     It's cheap, and catches most holes before a scene does.
   - **Scene step:** for 4 cores a cycle, play one scene in words at 3 players and one at 6: who stands where, what each one sees and says, the choice each makes, what goes wrong.
     Write it under the core in the pool's Scenes section, and fix or mark what it shows (`design-anti-patterns.md` C: play one scene).
   - **Long scene:** for the 3 top cores a cycle, play round 1, round 5 and round 20 in words: what the crew does differently by round 20, and what stops them settling into a habit (`checks.md` 4.4).
     After a fix, play it again, up to 3 times, until no new habit shows.
3. **Add new ideas.**
   6–10 new fantasies through sections A–D, aimed at the failure the pool shows most, and at a choice shape and a look the pool has few of (count the Shape column; the pool has leaned toward night-time curses).
   - **Rule at birth:** every new idea that passes gets its rule, and the critic on it, in the same cycle.
   - **When nothing new comes:** after 5 cycles with 0 new cores, write full lines for skins of the strongest cores instead (new fantasies for a rule that works).
     Go back to new fantasies after 3 cycles, or when the user asks for new cores.
   - **Taken skeletons:** when 3 or more pool ideas share one skeleton, add it to the taken list in `lessons.md` and aim away from it.
   - **Cores:** a new idea on an old core is a skin.
     List it under that core and don't count it as new; the cycle's score is new cores.
4. **Grow the understanding.**
   Write into `lessons.md` what this cycle showed about how ideas work: which fixes worked and why, what the passing ideas share, which choice shapes hold up.
   If the search budget allows, research one open question about it and cite the sources.
5. **Improve the method** (automatic; the user approved it).
   - **Measure last cycle's changes first.**
     Each open entry under "Method changes" in `lessons.md` names the failure it targets.
     Compare that failure's count with the cycle before, **counting only ideas made or changed after the change** (old ideas it never touched don't measure it).
     Fewer: mark it **kept**.
     Same or more: **revert** it (copy back from `history/`) and mark it **reverted**, with the numbers.
   - **Then make new changes.**
     If a lesson shows a gap (a check missed something, a step keeps giving the same failure), copy `SKILL.md` and `checks.md` to `history/<name>-<date><letter>.md`, edit them, and log the change: date, what changed, the gap it targets, the count to beat, and "result: pending".
   - Gaps noticed but not fixed this cycle go under "Open gaps" in `lessons.md`.
   - Tell the user what changed and what was kept or reverted, one line each.

## How to make and check an idea (used in steps 1–3)
### A. Fantasy
- One line: who you are and what you're doing, where the story puts players' bodies, lives or abilities in each other's hands.
  Lean toward help that **spreads** harm (curses, taints, infections, scratches).
  Skip families `lessons.md` lists as taken.
- **"My X does Y to you":** write how two friends act on each other in space first (my steps turn your floor, my gaze freezes you, my voice pushes you, my shadow is your floor), then a fantasy where that's natural.
  This gave 2 new cores in 6 tries, after 5 cycles of at most 1.
  The player's own camera and microphone count as tools.
- **Space** (who stands where; every move frees or blocks a friend) has held up best.
  Meters (cold, fur, fever) need something dealt each round to stop "share evenly".
  Space fails when it makes one queue or one slot.
- **Other starting points** (each tried for one cycle; none beat the others): a friend-verb the pool lacks (new cores so far came from new verbs: push off, swap places, carry for sight, unbolt a part, make room); real animal or human rituals (the hermit crab line-up for shells); researched folklore (gave harms, not verbs).
  Note which one each fantasy came from.

### B. Why interact (the force)
**What makes me need a friend right now?**
- **A pressure that grows on its own** (air, hunger, cold, fire, a sinking floor).
  Without it, nothing forces the interaction ("a vampire family feeds only on each other" says where the blood comes from, not why now).
- **Only a specific friend's act relieves it,** not the world or an item.
- **Relieving it costs or risks that friend**, best when **the harm spreads onto the helper**.
- **Something new is dealt each round:** who gets hit, which harm, how strong.
- **Fixed-plan probe (now, not at the end):** write the plan the crew would use by round 5.
  Drop or rework the idea if it's "take turns", "share evenly", "nearest helps", "hand it to whoever is farthest", "decoy", or a **threshold** ("pass it at half", "stop at three").
  A threshold is fine only if something dealt each round, or what a friend just did, moves where the right threshold is.
  Also a **role split** ("one wrapper, everyone else digs", "one guard with scissors"): when helping costs only time, one player becomes the helper, so the help must cost the helper's body.
  And **players who are all the same take turns**: if every player is alike, "swap when blue" wins, so players must differ by what the crew did to them.

### C. The idea line: [job] [choice] [goal], in natural sentences
This is the user's format.
- **Job:** what you do when nobody is in trouble.
  Best when the job itself pulls the danger in, so more progress means more danger.
- **Choice:** the main decision a player makes again and again, written as "X, or Y".
  Both sides cost something.
  **A friend must be in the choice:** one side is an act on a specific friend, or letting a friend act on you (three ideas lost their friend when first written this way).
  Prefer a choice only this fantasy can give; most ideas share "push your luck, or pass the harm to a friend".
- **Goal:** what these people want in the story.
  Not a generic timer, and not a place to reach (a level means content).
- Concrete words: physical actions and named things, never "fight it", "help" or "deal with".
  Never "risk", "may" or "might" for a harm without saying what decides it; those words hid dice rolls in 3 lines.
  Adding detail to the same line is not an improvement.
- You may change a fantasy's setup to make the goal fit; say so.
- **Shape tag:** P push or pass · T two ways to help · U use a friend · S swap harms · W where to put it (on which part of the friend).
  A new shape gets a new letter in the pool's list.
- **Look:** one line on what the screen shows.
  It must show the state the choice depends on (`checks.md` 2b).

Example: *Storm Sailors: Haul the ropes that keep the sails trimmed as they slip loose every few seconds and the storm's wind keeps changing; every rope you haul swings a boom across the deck. Haul now and knock flat any friend in the boom's path, who slides toward the low rail, or wait for them to duck, which stops their own hauling and lets their sail flap. Keep the ship on course until the storm blows out.*

### D. Check
- Run `checks.md` here, in order; the first ✗ stops the idea.
  Score what the line gives, and mark "needs a rule" instead of making one up.
  Give a short reason for every ~ and ✗.
- **Critic pass:** for each idea still standing, write the plan the crew settles into by round 5 and the one-line trick that beats it.
  If there is such a trick, "no fixed plan" is ✗.
- **Honest labels:** Claude writes and scores, so it isn't blind.
  For novelty, search the theme as well as the mechanic (3 themes were already on stores with other mechanics).
  Novelty is checked by web search within the budget (200 WebSearch calls per session, shared, about 100 more each hour; never work around the limit); otherwise mark it "memory (unchecked)".

## Files and report
- **Where things are saved:**
  - Ideas: the pool file (above), with its cycle log.
  - Understanding, method changes (with results) and open gaps: `lessons.md` here.
  - Old versions of the skill: `history/` here.
  - One line per cycle: the project's `research.md`.
  Files, because the chat gets summarized and a new session can't see it.
- Report with the `explain-simple` skill: answer first, plain words, no analogies.
  Then:
  - **Passed:** each [job] [choice] [goal] line, marking what changed this cycle.
  - **Failed:** the idea itself, then the check where it stopped and why; never just a name.
  - **Learned** and **method changes:** one line each.
