# Notes: judge rules, turned-off marks, the judge and the plugin's skills on the page

- The user asked for it mid-run on 2026-11-19 and went AFK; the design is Claude's, checked by two critic rounds (`proposal.md`, `critic-r1.md`, `critic-r2.md`).
- This reverses "Nothing feeds back" from the 2.0 design (user).
- What the first critic caught (Claude's own misses): a way for Claude to turn off marks against itself with no yes; a judge rule worded so it overrode the user's rules; cards with no versions; a turn-off tied only to one judging; a status that could never be anything but failing.
- The page already had a "marked wrong" tile style left from version 1, so a turned-off mark needed no new drawing (checked).
- `pkill -f <pattern>` in the same shell command killed the shell again (exit 144); stop a test server by its port instead: `kill $(lsof -ti tcp:PORT)`.
