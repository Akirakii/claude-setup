---
name: write-skill
description: Write or change one of the user's skills in their own style, and test or tune when it triggers (skill-creator only for trigger tests). Use whenever the user says "create a skill", "make a skill for X", "write a skill", "turn this into a skill", "update the X skill", "improve the trigger", "are the skills being triggered", or after suggest-skills gets an OK.
---

# Write skills the user's way

`skill-creator` is generic and synced from claude.ai, so this skill wraps it instead of copying it.
The way of writing comes from the user's own skills (design-research, generate-ideas, explain-simple).

## How a skill is written
| Part | How |
|---|---|
| `description` | what it does in one sentence, then "Use for/when" and trigger phrases in quotes, in the user's words |
| Title | the idea in one line ("Design from patterns, not from the code") |
| Opening | a short why, then any hard rule |
| Reasons | a few plain words on what went wrong; no quotes or dates |
| Words | plain everyday words, no labels Claude made up, one sentence per line |
| Links | point to `~/.claude/CLAUDE.md` rules by number and to notes in `~/.claude/domain-knowledge/`; never copy them. Rules for one domain live in that domain's skill (`game-dev`), never in CLAUDE.md |
| Length | short steps; a long skill puts detail in side files next to SKILL.md |
| Living skills | side files (`lessons.md`, `checks.md`) and a `history/` folder: before each change, copy SKILL.md to `history/SKILL-YYYY-MM-DDx.md` |
| Output it asks for | short, small tables, ✅/❌ (coworker style) |

## Steps
1. **Check it's new:** search existing skills (`~/.claude/skills/`, the skill list, plugins); extend one if it fits.
2. **Sketch first:** show the name, the description and the step titles in a few lines, and write after the user's OK (rule 5).
   Skip this only when the user already gave the content.
   A one-line change to an existing skill gets shown first too.
3. **Write** `~/.claude/skills/<name>/SKILL.md` the way the table says.
   For a living skill, copy it to `history/` first.
4. **Test triggers only when it matters** (several similar skills, or it must fire reliably): use `skill-creator` for that part.
5. **Report** what was written and where (coworker style); new skills show up from the next session.
