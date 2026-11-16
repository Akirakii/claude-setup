# Postmortem categories

Shared tags for `~/.claude/domain-knowledge/postmortem-rows.md`, so problems from different projects can be compared.
Seeded from the 20 problem types in Politowski et al. 2020 (200 game postmortems, https://arxiv.org/pdf/2001.00491).
Add a sub-type under a category when a problem needs a finer name; add a category only when nothing fits, with a line on why.

| Category | One line |
|---|---|
| Design | the game's design itself (core choice, balance, rules), not a technical detail |
| Prototyping | no prototype, or the gameplay wasn't checked before building on it |
| Unrealistic scope | more planned than the time allows |
| Feature creep | unplanned features added during the build |
| Cutting features | features cut, and what that broke |
| Planning | order of work, estimates |
| Delays | things took longer than planned |
| Crunch | overwork to catch up |
| Communication | between the user and Claude, or among people |
| Team | who did the work: setup, handoffs, agents |
| Tools | engine, APIs, plugins, generators (Meshy etc.) |
| Technical | code and asset infrastructure |
| Testing | how work was checked |
| Bugs | defects |
| Documentation | docs missing, stale or misleading |
| Over budget | money or credits |
| Multiple projects | attention split across projects |
| Marketing | reaching players |
| Monetization | price, business model |
| Security | leaks |
| Other | review at the end |

Sub-types added so far (Moonsick, 2026-11-16): Design: core choice has one answer, no reason to lie, premise with no precedent, pivot dropped a pillar; Prototyping: core never played with people before builds; Communication: followed the literal request over its own evidence; Testing: bots can't test bluff, critics with numbers.
Added in the second pass (Moonsick, 2026-11-16): Planning: foundation patched, not dropped; Communication: Claude argued against the user's restart.
Added in the comparison across games (2026-11-16): Design: rules carried over from the dropped game, two known loops glued together, fun placed in authored content, side-by-side work counted as co-op, fun in the player's own action; Unrealistic scope: fun only in the first stage, deep single-player strategy; Testing: can't tell communication from gameplay, judged solo.
