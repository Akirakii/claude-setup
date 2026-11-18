---
name: spot-gap
description: Stop and research when something keeps failing or Claude's understanding has a gap, and close the gap before going on. Use whenever the user says "this isn't working", "everything is wrong", "something is wrong", "clearly X isn't working", "why didn't X trigger", "really? no X?", "should I start from scratch?", when the user corrects the same thing twice or turns down the same kind of idea twice, when a fix keeps failing, or when Claude is about to state something it can't back up.
---

# Spot the gap, then learn

Guessing again after a miss repeats the miss.
When something keeps failing, stop and learn why before trying again.

## Signs of a gap
| Sign | Example |
|---|---|
| The user corrects the same thing twice | reply style rewritten 5 times in one evening |
| A fix keeps failing | the third tweak of the same number or rule |
| The user turns down the same kind of idea twice | a new version of an idea, rejected for the reason the last one was |
| The user doesn't understand Claude's words | "what does this even mean?" |
| Claude can't say why something works | a rule written from habit, with no source |
| A new topic for this user or project | a tool, a field, a design area never researched |

## Steps
1. **Stop patching.** Say the gap in one plain line: "I don't know why X keeps failing."
2. **Research it** (rule 10): web search for how others solve it and why it fails; tag [source] / [read] / [opinion].
3. **Save what you learned** where it belongs (`update-domain-knowledge` skill).
4. **Fix from what you found,** not from the old guess: change the rule, skill or code it points to.
5. **Tell the user** in 1–3 sentences: the gap, what you learned, what changed.
