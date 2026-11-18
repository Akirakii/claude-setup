# Hand-off: judge rules the fix skill can change, marks it can turn off, the judge and the fix skill on the page

## Summary for the user (read this first)
**Harness Doctor 2.0.5 is pushed and installed; you haven't tried it yet.**

- What changed, in your words: the fix skill can now "disable issue tiles" (turn a wrong mark off, with the reason) and "modify the judge rules" (a `judge-rules.md` the judge reads on every run); the judge and the fix skill "appear in harness doctor" as cards.
- How to try it: restart Claude Code (the update asks for it), open the page, and look for the red-striped card "judge rules" and the cards `harness-doctor:fix` and `harness-doctor:open`. Then run `/harness-doctor:fix`: for a wrong mark it now asks to turn it off.
- Checked: 40 tests pass; turning a mark off and on, the report and the page data were run on a copy of your marks; the installed 2.0.5 server serves the new cards.
- Not checked: the page with a turned-off mark was only looked at once, in a screenshot of the copy; no judge run was made with a rule for the judge in it (it costs usage); a third critic round.
- No mark of yours is turned off and no rule for the judge is written: both wait for your yes.
- Design calls are Claude's, checked by two critic rounds (`proposal.md`, `critic-r1.md`, `critic-r2.md`). The ones to look at: a turn-off needs your yes; a turned-off mark stays in sight; the judge card can only be "Failing" or "No data".
- Marks I'd turn off from today's report (wrong, in my reading): `suggest-skills` didn't load on "should we create a skill to update local plugin?" (that asks about one skill); `explain-concepts-plainly` wasn't read on "i dont understand older wording" (you asked to change a label, not for an explanation).
- The rule edits from the fix report are applied; the diff is `fix-report.diff` here, and the files as they were are in `~/.claude/backups/harness-doctor-fix-2026-11-19/`.

## What you asked for
| Your words | Tasks | Status |
|---|---|---|
| "work on all of it and then show the diff" (the fix report) | edit the rules, skills and notes; save a diff | done, diff at `fix-report.diff` in this folder |
| "fix skill should be able to modify the harness doctor judge rules" | a judge-rules file the judge reads; the fix skill edits it | done, not tried by you |
| "and also disable issue tiles" | a command that turns one mark off, with the reason; the page and report leave it out of the status | done, not tried by you |
| "judge skill should appear in harness doctor too" | a card for the judge's rules | done, not tried by you |
| "also fix skill too", "that can improve or fail" | cards for the plugin's own skills, judged like any skill | done, not tried by you |
| "push the changes and publish and update plugin" | tests, version bump, commit, push, plugin update | done: 2.0.5 pushed and installed |
| "also when finished publish setup" | copy the setup into the claude-setup repo and push | done |

## Log (local time)
- 01:24 rule edits from the fix report applied; backup in ~/.claude/backups/harness-doctor-fix-2026-11-19
- 01:31 critic round 1 merged; turn-off, judge rules, judge card, plugin skill cards built; 40 tests pass; critic round 2 running
- 01:40 critic round 2 merged, two severe fixes checked; 2.0.5 committed, pushed, plugin updated, server restarted on it
- 01:40 setup copied to the claude-setup repo and pushed (mom-trip and qv left out, as before)
