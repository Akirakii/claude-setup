---
name: explain-simple
description: Report how a session, run or piece of work went, or explain a result or idea, at a high level in simple, concise words. Use whenever the user asks "how did the X session go" (or "went"), "report me how it went", "what was designed last session", "explain simpler", "in simple terms", "I don't understand X", "short version", "tl;dr", or when reporting the outcome of a long run. Load it first, before reading the logs or docs.
---

# Explain at a high level, in few words

The user wants the shape of the answer, not the details.
Detail comes only when they ask.

## Format
```
**<The answer in one sentence.>**

- <Why, or what happened: one short sentence.>
- <one short sentence>
- <one short sentence, optional>

**Next:** <one sentence, optional>
```

## Rules
- **Under 100 words**, at most 4 bullets, one sentence each.
- **Answer first.** The first line alone should be enough.
- **Plain words.** No names from the work (check names, IDs, file names, method names).
  Use the user's own words; if a new word can't be avoided, explain it in the same sentence.
- **No analogies.** If an example helps, take it from the real thing.
- **At most 2 numbers**, and only if they carry the point.
- **At most one warning**, and only if it changes what the user would do.
- **No file paths, sources or lists of caveats** unless asked.
  Checked or assumed stays a short tag: "(not checked)".
- **No closing question.**
- If the user asks for more, go one level deeper on that part only.
