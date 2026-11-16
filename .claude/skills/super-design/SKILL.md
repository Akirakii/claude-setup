---
name: super-design
description: Design an idea from concepts, logic and research, never code, with isolated agents writing rival answers and a critic attacking them before the user picks. Use whenever the user says "super design", "super design this", "super design and decide", "super design and proceed", "super design at each stage", for a game mechanic, an economy, a harness, a plan or any other idea. Mustache Madness has its own design-idea skill; use that one there.
---

# Super design: rival answers, attacked, before anyone builds

One mind can't test its own frame, so the answers come from agents that never see my favourite.
Design from concepts, logic and research: never read or name the project's code while designing.
Code pulls the idea toward what already exists.

## Steps
1. **Say the problem without project nouns:** what goes in, what comes out, what must hold.
   List the rules in force: the user's decisions (tagged "(user)"), the pillars, and `~/.claude/domain-knowledge/design-anti-patterns.md` for game designs.
2. **Research** how others solve the general problem, with the `design-research` method (cite sources, mark anything from memory).
3. **Three rival answers.** Spawn 3 isolated general-purpose agents, each with a different lens (the research, the player's or user's view, the user's own method).
   Each brief gives the problem, the rules and the research in plain domain words, never code and never my pick.
   Each agent writes one really different answer with real numbers, never "more" or "some", and reports in caveman (rule 7).
4. **Attack them** with the `critic-round` skill's critic, one critic for all three answers.
   A severe problem with an answer's base idea gets fixed or kills that answer, never set aside.
5. **Play one scene** of each survivor: who does what, and what the best play turns into (the `game-dev` skill, design sketches).
   For a non-game idea, walk one real example through it instead.
   Drop a survivor whose best play is dull or skips the point of the idea.
6. **Merge and recommend one.** Prefer one mechanism that solves several needs.
   Write it in the project's docs with every pick tagged "(Claude)", and say what the runner-up does better.
   With the user here: show the sketch short and wait for their pick (rule 5); open choices go to the project's questions file.
   In an AFK run: use my pick, go on, and log it in the progress file.

## When it runs more than once
"Super design at each stage" means one round per design decision, not one for the whole run.
A small decision with an obvious answer gets one line in the design doc instead of a round.
