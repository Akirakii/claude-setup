---
name: project-postmortem
description: Find why a project or design failed, from its past sessions and docs, judging each decision by what was known then. Use whenever the user says "what happened in these sessions", "why did X fail", "extract the problem from my sessions", "postmortem", "detailed analysis of the sessions", "what went wrong", or a project is dropped or redone from scratch.
---

# Judge each decision by what was known then

Knowing how it ended makes every mistake look obvious, and warnings don't fix that, so the steps hide the outcome.
Claude took part in these sessions and already knows the ending, so the judging goes to fresh agents that weren't there.
Full research: `research.md`, next to this file.

## Steps
1. **Collect** the user's messages from every session on the project (`~/.claude/history.jsonl`, grouped by session), the transcripts around key moments (`~/.claude/projects/`), and the design docs, critic verdicts and questions file.
2. **Write what was intended,** in the user's words from the first session.
   Write it again at each pivot (a redo, a flipped core), and judge each version against its own goal.
   **Write the lesson that started this project:** what the user took from the project before ("X failed, so now Y"), in their words, and what Y changed and what it kept.
   Judge it at the end like any decision: did the lesson hold, and did this project fail on the part that changed or on the part that was kept?
3. **Write 3–5 rival explanations before reading further.**
   The user's explanation and any Claude already gave in chat each count as just one of them.
   For each: what must show up if it's true, and what would show up only if it's true.
4. **Timeline:** date, decision, who proposed it, options dropped, reason given.
   Mark when the core was first played, and each playtest reaction in the user's words.
5. **Pick the 3–5 key decisions** and give each to a fresh general-purpose agent with the transcript cut off at that decision.
   It answers separately: reasonable on what was known? / was the missing information cheap to get (a prototype, a playtest)? / did it work? (the last one after it sees the outcome)
   Give each agent the user's known limits from the domain knowledge (who can test, what was already tried and turned down), so "cheap to get" means cheap for this user.
6. **What went wrong and what went right,** each with several causes, found with "how" questions, not "who".
   Test the rival explanations against the timeline: keep the ones whose "must show up" evidence is there.
   Flag "should have" and "if only" in my own wording.
   For a game, follow each playtest reaction backward with the `fantasy-chain` skill: from the feeling, to the action, to the logic or aesthetic behind it.
7. **Check:** one more fresh agent gets steps 4–6 with speakers relabelled A/B and no verdicts, and writes where it disagrees.
   Settle each disagreement with a reason; the user's playtest beats any agent.
8. **Write** `POSTMORTEM-YYYY-MM-DD.md` in the project's `postmortem` task folder: summary first, then the steps, every claim tagged checked or assumed.
   Add one row per problem and per thing that went right to `~/.claude/domain-knowledge/postmortem-rows.md`, tagged from `categories.md` (add a category when nothing fits, and note why).

Reply with the short version: events in order, then the verdict (coworker style).

## Comparing projects (later)
Once 3 or more projects have rows: count each category as "k of n projects", look for projects with the same condition that didn't fail, and keep only the patterns that survive.
Then lay the projects out as one chain, oldest first: the failure, the lesson taken from it, what the next project did because of it, and how that one failed.
Mark each lesson: held or not, and whether it only turned the last complaint around (too big, so tiny; nobody lies, so everyone fights).
A lesson drawn from one failure is a guess until a project built on it works, so write it as a guess.
**Then judge the method, not the outcomes:** write the steps the user followed from one project to the next as one loop (where the idea came from, who wrote the rules, how it was judged, how the lesson was drawn, how many things changed at once), and which steps were the same in every project.
A step that never changed across the projects is the first suspect, because the lessons never touched it.
