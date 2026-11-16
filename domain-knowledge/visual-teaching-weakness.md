# visual-teaching-weakness

Claude's own drawn teaching pictures (boards, icon strips) aren't readable to people; don't judge visual clarity yourself, copy a proven format, and let a human glance at it.

In Moonsick, Claude drew a wordless "how to play" board for the hall from code-drawn shapes: pill-shaped people, a circle for "look", a cure in a box for "its room", arrows chaining symbols.
The user found it unreadable for humans.

**Why:** Claude draws with code from basic shapes and judges an image by describing it to itself, so a puzzle of symbols passes its own check.
Vision-language models fail simple visual tasks that humans find trivial (Rahmanzadehgervi et al. 2024, "Vision language models are blind", arXiv 2407.06581).

**When:** any picture meant to teach players.
- Copy a format built and tested for strangers: airline safety cards and IKEA steps (numbered panels, one action each, a person doing it with the object, motion arrows, a red X for "don't").
- Draw people as people, not pills.
- Don't call a picture clear because each symbol "stands for" an idea.
- The check is a human's 5-second glance: "what does this tell you to do?"

Related: [[critic-anti-patterns]], [[explain-concepts-plainly]].
