# Proposal: the fix skill can correct the judge (Claude, AFK 2026-11-19)

## The user's words
"not all issues are issues so im thinking harness doctor fix skill should be able to modify the harness doctor judge rules and also disable issue tiles"
"also judge skill should appear in harness doctor too" / "also fix skill too" / "that can improve" / "or fail"

## The problem underneath
The judge is a model, so some of its bad marks are wrong. Today a wrong mark stays red for 30 days and the same mistake is made in the next run, because nothing feeds back (the 2.0 design chose that on purpose).
Two things are missing: a way to take one wrong mark out, and a way to stop the judge from making that kind of wrong mark again.
The judge and the fix skill are also text that shapes results, so they should be visible and judged like every other file.

## Three answers
1. **Turn-off list + a judge-rules file (recommended).**
   - `<data>/dismissed.json`: one entry per mark turned off: session, rule id, the judged time of that session, the reason, and (optional) the judge rule that should have prevented it. Written only by `harness_doctor.py --dismiss` / `--restore`.
   - A turned-off mark stays on the page as a grey tile with its reason, and doesn't count in the rule's status or in the report. A re-judged session gets fresh marks (the entry is tied to the judged time).
   - `<data>/judge-rules.md`: the user's own rules for the judge, bullets with a bold title. The judge's prompt gets them after its built-in instructions, as "the user's rules for the judge, which win".
   - The fix skill: a wrong mark is turned off with its reason and said in one line; when the same kind of wrong mark shows twice, it proposes a judge rule and writes it after the user's yes.
   - The page gets a card "judge rules" (kind judge) under Everything. Its first row is fixed, "Marks turned off as wrong": every turned-off mark is a bad mark on the judge. A turned-off mark that names a judge rule lands on that rule instead. A judge rule has no good marks (nothing natural counts as one), so it is "No data" or "Failing".
   - The plugin's own skills (fix, open) get cards like any skill, named `harness-doctor:fix`, so the judge marks them from sessions.
2. **Only examples.** Save every turned-off mark and send the last N to the judge as "marks the user called wrong". No file to edit. Cheaper to build, but the prompt grows, examples over-fit, and the user can't read or edit what the judge was told.
3. **Edit the judge's built-in instructions in the plugin.** One place, but a plugin update overwrites it and every user of the plugin would share one person's taste.

## Scenes
- Smallest: one wrong mark. The fix skill reads the session, runs `--dismiss 8db9214a "Stay at the high level" --why "a setup-change line must name its file"`. The rule turns from Failing to Healthy if that was its only bad mark; the tile is grey; the judge card shows 1 bad mark on "Marks turned off as wrong".
- Largest: 12 wrong marks of 3 kinds across 40 sessions. The skill turns off 12, proposes 3 judge rules, the user says yes, later runs stop making them; a wrong mark made after a judge rule was written lands on that rule as a bad mark, so the page shows the judge rule failing.

## What it keeps, bends or drops from the 2.0 design
- Drops "Nothing feeds back" (the user asked for it).
- Keeps "No 'This mark is wrong' on the page": turning off happens in the conversation.
- Keeps "the page shows, a conversation judges and fixes".

## Known risk (Claude)
The fix skill is Claude correcting marks against Claude. Kept honest by: the grey tile and its reason stay visible, the count shows on the card, `--restore` undoes it, and judge-rule edits wait for the user's yes.

## Merge after critic round 1 (2026-11-19)
| Finding | Decision |
|---|---|
| Severe 1: a turn-off needs no yes, and Claude is correcting marks against itself | Fixed: the fix skill turns a mark off only after the user's yes (one yes can cover several) |
| Severe 2: a rule for the judge can hide real failures; "which win" overrode "judge the rule as written" | Partly fixed: the prompt now says the user's rules say how to read one kind of moment and the rule is still judged as written; the skill forbids "don't mark rule X" and rewords the user's rule when that is the unclear one. Not built: marks per judge rule before and after it (open) |
| Severe 3: the judge's rules and the plugin's skills had no versions | Fixed: the reader follows judge-rules.md, and the doctor keeps each text of its own skills it has seen |
| Severe 4: the judge card would be sent to the judge | Was already built in the page data only |
| Severe 5: a turn-off is lost when the session is judged again | Fixed: it also holds when the new mark quotes the same words |
| Medium 6: uncovered problems couldn't be turned off | Fixed |
| Medium 7: "Marks turned off as wrong" would be listed as failing in every report | Fixed: the judge has its own last part in the report |
| Medium 8: the scene was wrong (the rule turns to "No data", not "Healthy", when its only mark is turned off) | Scene corrected here; no code change |
| Medium 9: a title can name two rules | Was already handled: the command asks for the rule id, which the report prints |
| Medium 10: the judge can't see the turn-off command when judging the fix skill (tool lines are cut at 90 characters) | Left open |
| Medium 11: the built-in instructions weren't shown | Fixed: they are rows on the judge card |
| Medium 12: judge-rules.md lives in the data folder | Kept (a plugin update must not overwrite it); the README says to keep a copy before uninstalling |
| Minor 13: prompt length moves marks, so a judge rule's effect can't be told from noise | Left open, said in the README |
| Cut | Per-judge-rule blame is cut. The plugin's skill cards stay, because the user asked for them |

## Merge after critic round 2, on the built code (2026-11-19)
| Finding | Decision |
|---|---|
| Severe 1: the judge's count went by when the session was judged, so marks turned off after a rule was written never counted | Fixed: it goes by when the mark was turned off (checked with the critic's scene) |
| Severe 2: the installed plugin and the repo copy kept rewriting the history of the plugin's skills; a report wrote it too | Fixed: separate histories, and only the server records |
| Medium 3: a turn-off was lost on a second judging when the mark quoted none of Claude's words | Fixed: falls back to the user's words, then the mark's line; a problem goes by its name |
| Medium 4: a turn-off whose mark is gone couldn't be removed | Fixed |
| Medium 5: turning off one session of a 2-session problem removes the problem from the page | Kept; the skill and the README now say so |
| Medium 6: a turn-off works on a mark the page hides | Left open |
| Minor: a second turn-off overwrites the reason; built-in rows named "pass", "fail"; dead code in the page | Left open |
No third critic round was run: both severe findings were fixed and checked by rerunning the critic's own scenes (Claude).
