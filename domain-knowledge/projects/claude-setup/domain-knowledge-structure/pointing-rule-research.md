# Research: is the pointing rule state of the art? (2026-11-16)

Question (user): CLAUDE.md names nothing, skills point at rules and knowledge, notes never name skills and point only at more general notes, an index lists what is below it. Is that how others do it?
Tags: [source] = said by the linked page; [read] = Claude's reading of it; [opinion] = Claude's own; [not found] = searched, nothing found.

## Where it matches
- A short always-loaded file, procedures moved to skills: "target under 200 lines per CLAUDE.md file"; a multi-step procedure moves to a skill. [source: https://code.claude.com/docs/en/memory]
- An index with one line per entry plus topic files is how Claude Code's own auto memory is built (`MEMORY.md` index, one topic file per memory). [source: same]
- A skill loads from its own name and description, read at startup (~100 tokens), so nothing else has to name it. [source: https://agentskills.io/specification.md]
- A pointer written in words is weak: a CLAUDE.md that tells Claude in words to read a file is read "only if it decides to open the file"; an `@` import is the strong form. [source: the memory page]
- No cycles, and depend toward what changes least: the Acyclic Dependencies and Stable Dependencies principles (Robert C. Martin). [source, secondary summaries: https://agileinaflash.blogspot.com/2009/04/principles-of-package-coupling.html, https://helix.sitecore.com/appendix/package-principles.html]
- "Keep file references one level deep from SKILL.md. Avoid deeply nested reference chains." [source: the spec] Applying it to notes, so no sideways "Related" links, is [read].

## Where it departs
- Common advice makes the root file a router with pointers to deeper docs. [source, community guides: https://dev.to/nishilbhave/claudemd-best-practices-the-complete-2026-guide-435j, https://www.mintlify.com/agentsmd/agents.md/guides/monorepos] Ours points at nothing and lets the index line and the skill descriptions route. [opinion]
- The spec expects a skill's reference files inside its own folder, by relative path. [source] Ours point at the shared knowledge by absolute path, so the skills are not portable. [read]
- Note-taking practice (Zettelkasten) treats links between notes as the main tool, with folders optional; others say folders and links can live together. [source, forum opinion: https://forum.zettelkasten.de/discussion/comment/11566/]
- "A note never names a skill" as a written rule: [not found].

## Warning from the one study found
A July 2026 preprint on agent-kept markdown memory: an organized store roughly halves retrieval cost where material is large, organization erodes as the store grows for all but the strongest managing agent, and no agent turned organization itself into better answers. [source, abstract-level only: https://www.alphaxiv.org/abs/2607.26637]
So the upkeep is the risk, more than the rule. [opinion]
