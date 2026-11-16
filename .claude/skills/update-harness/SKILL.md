---
name: update-harness
description: Save a lesson, rule, preference or correction so later sessions follow it - decide whether it belongs in CLAUDE.md, the output style, a skill or the domain knowledge, then write it there or hand it on. Also cleans CLAUDE.md and the output style. Use whenever the user says how Claude should work from now on ("always ...", "never ...", "dont ...", "tell me always ...", "note it", "remember", "save this", "don't do that again"), after a correction worth keeping, or says "review my rules", "clean claude md". Not for recalling things ("I remember..."). Load it before editing CLAUDE.md or the output style.
---

# Put each lesson in the one place that will load it

The harness is what shapes every session: `~/.claude/CLAUDE.md`, the output style, and the skills.
Each has one job, so a lesson has one home.
Hidden auto memory is off; never write to `~/.claude/projects/*/memory/`.

## Where it goes
| The lesson is about | Home | Written by |
|---|---|---|
| How Claude works in any domain | `~/.claude/CLAUDE.md`, a numbered rule (the rule, **Why:**, **When:**) | this skill |
| How replies are written | `~/.claude/output-styles/coworker.md`, by its own "Adding to this file" steps | this skill |
| How to work in one domain (games, music, ...), or a procedure with steps | a skill | hand to `write-skill` |
| A fact, a model, a decision or a lesson about a domain, a project or a task | `~/.claude/domain-knowledge/` | hand to `update-domain-knowledge` |

CLAUDE.md names no domain: a rule that only holds for games goes in the `game-dev` skill, never in CLAUDE.md.

## Steps
1. **Find the home** (table above), and search it for an entry on the same thing.
   If one exists, update or merge it (count a repeat: "×2") instead of adding a second.
   If a written rule already covered the moment and still failed, fix why it failed (CLAUDE.md rule 26).
2. **Write the entry short,** one sentence per line:
   - the general rule, not the one case that taught it; the case can go under it as one short example;
   - **Why:** what happened, in a few plain words, never a quote or a date;
   - **When:** the moment it applies.
   Tag calls "(user)" or "(Claude)", and mark anything not checked "(assumed)".
   Use the user's words, not labels Claude made up.
3. **Show it:**
   - The user asked for it: write it, then show the file and the exact lines.
   - Claude's own idea: show the file and the exact lines first, and write after the user's OK.
4. **Report in one line:** what was saved, and where.

## Cleaning CLAUDE.md and the output style
When the user asks, or CLAUDE.md passes ~150 lines:
- list duplicates, contradictions (the user's words decide), stale paths (check them), old-style text, and domain rules that belong in a skill, each with `file:line`;
- show the exact edits and apply them after the user's OK;
- copy the file to `~/.claude/backups/` before rewriting more than a few lines;
- keep rule numbers stable, since skills point to them.
A lesson that came up 3 or more times in the domain knowledge is ready to be proposed as a rule.
