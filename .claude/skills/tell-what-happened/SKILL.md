---
name: tell-what-happened
description: Tell what happened in work the user didn't watch (a past session, a web session, an AFK run, a hand-off, a patch or report they haven't read), as the events in order. Use whenever the user asks "what happened", "could you tell me what happened", "how did the X session go" (or "went"), "report me how it went", "what was designed last session", "what happened in these sessions", or says "I didn't read those sessions", "I have no idea", "I'm not updated", "catch me up". Load it first, before reading the logs or docs.
---

# Tell what happened as the events in order

The user wasn't there, so a verdict alone leaves them lost.
A short answer with a few bullets was given first, and the user still couldn't tell which finding was which.
The same work told as numbered events, with the findings after them, was understood at once.

## Steps
1. **Read all of the work first,** to the end.
   A file that comes back cut off gets read to its last line before any answer.
2. **Fix a wrong idea first.**
   When the user's question holds one ("the critic is failing and it's about enemies?"), say in one line what is wrong with it, then tell the events.
3. **The events in order,** numbered, one event per sentence.
   Start from what the user asked for, in their words.
   Each event says who did it (the user, Claude, a critic) and what came out.
   Link an event to the one before it with "so" when one caused the other.
4. **Explain each new thing where it first appears,** inside the same sentence ("the critic, a second agent that attacks a design on paper").
   A thing the user has never seen gets its real content in a few words, not only its name ("an imp rides on each player's back, and only a friend can slap it off").
5. **The findings after the events,** each with one bold line and two or three sentences under it.
   Keep two findings apart, even when one led to the other.
6. **Where the work stands,** in bold: applied or not, built or not, played or not.
7. **Claude's own pick comes last and is marked as Claude's,** so it doesn't blend into what happened.
   Leave it out when the user only asked what happened.

## Format
```
<one line fixing a wrong idea, if there is one>

**What happened, in order**

1. <You asked for X, so Claude did Y.>
2. <one event>
3. <one event>

**Finding 1: <the finding in one line.>**

<two or three sentences>

**Finding 2: <the finding in one line.>**

<two or three sentences>

**<Where the work stands.>**
```

## Rules
- Plain words, and the user's own words for anything they already named.
- No file names, IDs, branch labels or version names from the work.
- Numbers only when they carry the event ("reworked 11 times", "12 severe problems").
- At most about ten events; group small steps into one event.
- No analogies; an example comes from the work itself.
- This is the full telling, so the output style's one-line limit doesn't apply here; one sentence per line still does.
- For why a project failed, with each decision judged by what was known then, use `project-postmortem` instead.
- For a result or an idea made simpler ("tl;dr", "explain simpler"), use `explain-simple` instead.
