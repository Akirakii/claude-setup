# Critic r1 (read code: checked; nothing run)

**Verdict on the problem:** half right. It treats "turned off" as "known wrong", but it is only Claude's claim about marks against Claude. And (c) is misread: "can improve or fail" needs good marks and history; answer 1 gives judge rules neither.

## Severe
1. **Turn-off needs no yes, and is booked as the judge's fault.** Scene 1: Claude dismisses in one line, rule leaves the report, judge card goes red. Bends SKILL.md "the user is the check". Fix: user's yes per turn-off (one yes for a batch is fine).
2. **A judge rule hides real fails with no trace.** Card counts only wrong marks made despite the rule, never fails it suppressed; a too-broad rule reads "No data". "Which win" also overrides "judge the rule as written" (judge.py:37): the scene's `--why` is an unclear user rule, which fix step 4 says to reword. Fix: judge rule only when the user's rule is clear; show marks per rule before/after it.
3. **Judge rules and plugin skills have no versions.** `row_of` reader.py:56 returns None for anything else under `~/.claude/` (data folder, `plugins/cache/.../2.0.4/skills/fix`); `parse_log` :224 drops their edits. So one epoch, never Regression, no History. Plugin update = new path, `born` = install time, `then()` rules.py:160 skips older sessions and page_data :172 hides their marks: fix card empties each update. "Made after the rule was written" can't be computed.
4. **Judge card is sent to the judge as rules.** `catalog` feeds `judge_session` (judge.py:163); kind "judge" has `trigger` False, so `in_play` rules.py:315 sends it in full. Fix: build the card in page_data only.
5. **Third scene: turn-off lost.** Judged T1, mark off, session grows, `pending` judge.py:192 re-judges, `keep` :268 overwrites `at`. Same quote comes back red; old entry has no tile, so the judge count drops or counts a ghost. Fix: key on session + rule + quote.

## Medium
6. **Uncovered problems can't be turned off.** Key is a rule id; "Not covered yet" has only a topic. The user said "issue tiles".
7. **"Marks turned off as wrong" is Failing forever** (no good marks, `status` :130), so `report` :212 lists it every run.
8. **Scene 1 wrong:** only mark turned off gives `now` empty = "No data", not Healthy. `unused` :249 then lists the rule for removal, unless grey moments stay in `d["moments"]`; then `report` :214-217 must filter too.
9. **`--dismiss` by title is ambiguous:** id is file + title; "Output", "Steps" exist per skill.
10. **Judge can't see the turn-off when judging the fix skill:** `brief` rules.py:254 cuts a tool line at 90 characters; the script path eats them.
11. **Built-in INSTRUCTIONS not shown,** though the user said "judge skill should appear".
12. **judge-rules.md lives in the plugin data folder:** unversioned, likely lost on uninstall (assumed).

## Minor
13. Prompt length moves marks (design: 7, 4, 1), so "later runs stop making them" can't be told from noise.

## Bent without saying
- Four statuses (judge rules get two); grey tile is a new mark state; new kind "judge".
- "A rule has its own history": not for the new cards.
- "Not 'which rule is to blame'": the entry's judge-rule field is that, answered by Claude.
- v1's dropped "judge them again" banner: marks from before and after a judge rule now mix unmarked.
- "Page and report can't disagree": report recounts bad/good itself.

## Cut from first version
- Per-judge-rule attribution; keep one count.
- Plugin-skill cards (needs `row_of` work); ship turn-off + judge-rules file first.

## Couldn't break
- Answers 2 and 3 are rightly rejected.
- marks.json and dismissed.json share a folder, so they move together.
- Name `harness-doctor:fix` matches what `transcript` records, so loading is detected.
- `--restore` plus a visible reason is sound once a yes gates it.
