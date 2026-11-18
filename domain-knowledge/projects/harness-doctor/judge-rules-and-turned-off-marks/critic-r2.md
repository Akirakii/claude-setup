# Critic r2 (40 tests pass; tried on a copy of the data; real folder untouched)

## Severe
1. **Judge count keyed on when the session was judged, not when the mark was turned off.** harness_doctor.py:217 (`version_at(jf["versions"], e["at"])`), report :298. Checked: added judge-rules.md, turned off 2 marks in 8db9214a -> "turned off since: 0", card "No data". All 42 judged sessions land there once the first rule is written, so skill step 7 never fires for them. Fix: list by turn-off time (`o["t"]`); judged-at only for blaming a rule.
2. **own-skills.json flips between installed and dev copy.** reader.py:498 appends whenever the text differs from the last one. Installed server runs on the real data folder; dev SKILL.md differs. Each alternation: new full text, fake version, changed steps back to "No data". `--report` and `--turn-off` write it too (checked). Fix: reuse an already-seen text, or one list per plugin folder; only the server writes.

## Medium
3. **Turn-off still lost on re-judge when the mark has no Claude quote.** judge.py:104. Checked by sim: didn't-load marks (12 bad marks in the real store) and every uncovered problem come back red. Fix: fall back to `you`/line; a problem matches on topic.
4. **Stale turn-off can't be removed.** `--turn-on` goes through `find_mark` (judge.py:112), which needs the bad mark to still exist. (read)
5. **Turning off one of a 2-session problem removes the whole card** (harness_doctor.py:244); the struck tile isn't "on the page" as skill and README say. (read)
6. **Turn-off succeeds on marks the page hides** (session older than the file's `since`, log gone): says "stays on the page", shows nothing. (read)

## Minor
- Second `--turn-off` overwrites the reason silently (checked).
- Built-in rows titled `"pass"`, `"fail"`, `"unknown"`; 11 rows forever "No data".
- index.html:613 `ruleTip`: dead code with a local "This didn't go wrong" toggle.
- SKILL: `--turn-on` line lacks `--data`; step 7 needs `${CLAUDE_PLUGIN_DATA}` to expand in prose (assumed): say "the path the report prints". A problem name with `"` or `$` breaks the command.

## What I couldn't break
- Report with no judge-rules.md, empty folder, `{}` marks, garbage turned-off.json.
- Off then on: report identical to before; 6 -> 5 bad while off.
- Judge card never reaches the catalog or the judge's prompt.
- Every moment carries `wrong`; page JS handles kind "judge".
- r1 items 1, 2, 4, 6, 7, 11 done as decided.
