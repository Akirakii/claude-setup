---
name: suggest-skills
description: Find repeated work that should become a skill, a hook or a rule, and propose it. Use when the user asks "do we need more skills?", "what do I keep repeating?", "what should be automatic?", after Claude notices doing the same multi-step procedure for the third time, or when the start-of-session reminder says it's due (weekly).
---

# Suggest skills

## Steps
1. **Gather evidence:**
   - What the user asks for most: `python3 -I ~/.claude/skills/suggest-skills/history_counts.py` (top phrases), then with regexes for suspected topics (`... history_counts.py 'meshy' 'afk' 'playtest|i played'`).
     The counts are keyword hits, so call them rough.
   - This session: steps done 3 or more times, or briefs written by hand more than once.
   - `~/.claude/CLAUDE.md`: a rule that describes steps (not a habit) could be a skill.
   - Existing skills (the skill list, `~/.claude/skills/`, plugins): never propose a copy; propose extending one.
2. **Sort each candidate:**

   | Kind | When |
   |---|---|
   | skill | steps Claude should notice and follow |
   | hook | it must happen every time, whatever Claude notices (block, launch, check) |
   | rule (CLAUDE.md) | a short habit for every reply |
   | nothing | rare, or already covered |
3. **Show a small table:** name · when it fires · evidence (counts, or "N times today").
   Recommend the top 2–3.
   Write nothing before the user's OK.
4. **Write after the OK** with the `write-skill` skill (the user's way of writing skills; `skill-creator` only for trigger tests).
5. **Report** what was written and where (coworker style); new skills show up from the next session.
6. **Mark it done:** `touch ~/.claude/hooks/suggest-skills.last-run`, so the weekly start-of-session reminder resets.
   Do this even when the user OKs nothing.
