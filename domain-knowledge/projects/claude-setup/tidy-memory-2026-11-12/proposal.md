Applied 2026-11-12 except Q1–Q4, O1–O2
(To keep those lines word for word: `mustache-madness/docs/memory-archive.md` keeps its Q2 entry, lines 1-12; the new `game-idea-triad.md` keeps the Q1 and Q4 lines; `idea-search-loop.md` keeps the Q3 lines; `projects.md` keeps line 3 and the DRS row; `INDEX.md:10` is unchanged. Backups: `~/.claude/backups/*.bak-tidy-2026-11-12`.)

# Tidy-memory proposal, 2026-11-12 (nothing applied yet)

Proposal only: no existing file was changed. Rules are cited by their numbers in the merged `~/.claude/CLAUDE.md`
(1–7 = the old principles, 8–22 = the old rules 1–15). Checked = ls/grep/git run on 2026-11-12; assumed = not run.
Apply only after the user's OK. Before applying, copy each file you rewrite to `~/.claude/backups/` (tidy-memory step 3).
Delete this file once it is applied.

## Summary

| | Count |
|---|---|
| Archive entries reviewed (7 `docs/memory-archive.md` + `notes/archive/runpod-claude.md`) | 45 |
| → delete: already in a CLAUDE.md rule | 29 |
| → delete: already in a note or the repo's own docs | 6 |
| → delete: stale (project dropped, or path gone) | 9 |
| → move a few lines into a repo doc, then delete | 1 (+6 small moves out of the other 44) |
| → keep in an archive | 0 (all 8 archive files can go; the full old text stays in `~/.claude/backups/auto-memory-2026-11-12.tar.gz`, checked) |
| New CLAUDE.md rule | 1 (rule 23, "a failed check is a fail", from `drop-what-fails-a-check.md` + 2 repeats) |
| CLAUDE.md rule edits (wording from the archives) | 4 (rules 10, 16, 17, 20) + 2 small fixes (header, rule 19) |
| Notes shortened or fixed | 9 |
| Contradictions for the user | 4 (Q1–Q4), plus 2 open choices (O1–O2) |

| File | Before | After (proposed) |
|---|---|---|
| 7 `docs/memory-archive.md` + `notes/archive/runpod-claude.md` | 40.1 KB | 0 (deleted) |
| `notes/critic-anti-patterns.md` | 34.7 KB (121 entries) | 11.9 KB (104 entries, every pattern + fix + count kept) |
| `notes/game-idea-triad.md` | 6.5 KB | 3.0 KB |
| `notes/idea-search-loop.md` | 5.1 KB | 2.8 KB |
| `notes/drop-what-fails-a-check.md` | 1.2 KB | 0 (into CLAUDE.md rule 23) |
| `notes/projects.md` | 2.8 KB | 3.0 KB (stale rows fixed) |
| `notes/machine-setup.md` | 3.0 KB | ~3.5 KB (3 lines moved in) |
| `notes/INDEX.md` | 2.5 KB | ~2.2 KB |
| `~/.claude/CLAUDE.md` | 113 lines | ~127 lines (budget ~150) |

Critic note: 11.9 KB is ~2 KB over the ~10 KB budget. Cutting more would drop fixes or the user's quotes; I stopped there.

## Questions for the user (contradictions; your words decide, nothing resolved here)

- **Q1. Which game is active?** `notes/projects.md:3` and `notes/INDEX.md:10` say Moonsick is the active game;
  `notes/projects.md:11` says Deathly Reality Show is "**active** (since 2026-11-07)"; `notes/game-idea-triad.md:10` lists
  Deathly Reality Show among games "built and dropped". DRS's last commit is 2026-11-08 (checked); no doc says it
  was paused or dropped (checked DRS and Moonsick CLAUDE.md). Recommended (Claude): Moonsick active, DRS dropped or
  paused, in whichever word you use.
- **Q2. May the PC power off at the end of an AFK run?** CLAUDE.md rule 11 (2026-10-30): "shutdown near the session's
  end is fine". `mustache-madness/docs/memory-archive.md:8,12` (2026-10-25): "dont turn off machine" as a rule; keep the
  no-poweroff config until you say the AFK run is over ("a check-in or question is not that"). The keep-awake script
  stops at 5h usage ≥ 90% or 30 min of Claude silence, so it allows the power-off (`machine-setup.md:25-26`).
  Recommended (Claude): the newer rule 11 wins; the archive entry goes.
- **Q3. Does the critic subagent rule cover the idea search?** CLAUDE.md rule 20: "an isolated critic subagent" on every
  design decision. You said for the idea search (2026-11-10): "it no multiagent just here"; "the skill now should not work
  with multiagent" (`notes/idea-search-loop.md:22-26`), and `skills/generate-ideas/SKILL.md:8-9` makes the critic an inline
  pass. Rule 20 doesn't name that exception. Recommended (Claude): add to rule 20, "In the idea search
  (`generate-ideas`), the critic is an inline pass, no subagents (user, 2026-11-10)."
- **Q4. Analogies?** `notes/game-idea-triad.md:64` (2026-11-09): "Use the kitchen analogy (pantry = size, how spices
  affect each other = K)". `notes/explain-concepts-plainly.md:23-26` (2026-11-10): "dont use analogies"; and line 13 bans
  "pantry" as a coined label. Recommended (Claude): the later "dont use analogies" wins; the proposed triad text below
  drops the kitchen line.

Open choices (not contradictions; pick up when ready):
- **O1. Gamepad-first (Switch) for new games?** You asked for it on 2026-10-31 for Dungeon Pets and Assemblia (both repos'
  CLAUDE.md and `docs/constraints.md`, checked). No later game says it. If it holds for every game, it becomes a
  CLAUDE.md rule; if not, it stays in those two repos (proposal assumes the second).
- **O2. "No coined words" as a rule?** `notes/explain-concepts-plainly.md:11-14` (2026-11-09: "what is spokes? dont use coin
  words that i didnt use that you used") applies to every reply, but the note only loads when explaining. Rule 6
  allows a new term once defined. Option: add to rule 6, "Prefer the user's own words; coin a label only when none
  exists, and define it in the same sentence." Not proposed by default (one correction so far).

---

## 1. Archives vs CLAUDE.md, notes and the repos' docs

Every entry below is deleted with its whole file. "Quote dropped" = the user's words in that entry that won't be
anywhere else afterwards (they stay in the backup tarball). Rule numbers = merged CLAUDE.md.

### `~/Playground/assemblia/docs/memory-archive.md` (13.8 KB, 15 entries) → delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | afk-experiments-2026-11-01 | stale: project abandoned (`projects.md:15`); its one live fact, "4 untested exp/* branches kept", is already in `projects.md:15` (checked: `exp/hack`, `exp/laws`, `exp/slice`, `exp/supply` exist; `~/Playground/assemblia-wt/` is gone) |
| 13 | afk-mode | dup: rules 11, 14, 16 + `machine-setup.md:25-29` (keep-awake, checked) |
| 22 | assemblia-abandoned | dup: `notes/game-scope-lessons.md` (all points; "default to single player" already marked superseded there) |
| 37 | assemblia-origin | stale: project abandoned; `dungeon-pets/POSTMORTEM.md:31` "Lessons carried into Assemblia" (checked) |
| 51 | dialectic-rule | dup: rule 20 + `assemblia/CLAUDE.md:11`. Quote moves to rule 20 (edit below) |
| 59 | meshy-3d-needs-permission | dup: rule 17 ("Image-to-3D and rigging need an explicit OK each time"); the "iterate until right" clause moves to rule 17 |
| 69 | meshy-prompt-review | dup: rule 17; quote "show the diff and ask before doing" moves to rule 17 |
| 82 | next-game-direction | dup: `game-scope-lessons.md` (co-op chosen, GodotSteam) + `game-design-research/CLAUDE.md:39` (furry dropped); stale path `~/Playground/rival-radar` (checked: gone). Quote dropped: "keep it clean without that" |
| 92 | no-reference-edits | dup: rule 17 ("never edits of an existing image") + `machine-setup.md:40-41` (rebuild the saved prompt); the "a named id = its prompt" clause moves to rule 17. Quotes dropped: "no edit character. brand new", "create a brand new image" |
| 102 | rejected-approach-stop | dup: rule 8. Quote dropped: "never do that again" |
| 112 | risk-reward-first | dup: rule 9. Quotes dropped: "drop always high risk low reward"; "we are in first days stages of development.. literally nothing is set in stone so we prefer fast iteration. also low risk means low effort really." |
| 124 | rival-radar-project | stale: `~/Playground/rival-radar` gone (checked); it is `game-design-research` (first commit "Start rival-radar", checked); "measured signals" rule is in `game-design-research/CLAUDE.md:14` |
| 134 | switch-compatible | project-only, already in `assemblia/CLAUDE.md:22` and `docs/constraints.md:96` (checked); stale path `scripts/core/game_input.gd` (checked: no such file in assemblia). See O1 |
| 146 | testing-off-by-default | dup: rule 14 + `assemblia/CLAUDE.md:23`. Quotes dropped: "dont test"; "testing should be off by default. just enabled and occasionaly when afk"; "your test evaluation is worse than me just playtesting 10 seconds" |
| 155 | websearch-when-unsure | dup: rule 10 + `assemblia/CLAUDE.md:3-6`; the "research why a good X works" clause moves to rule 10 |

### `~/Playground/dungeon-pets/docs/memory-archive.md` (10.9 KB, 12 entries) → delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | afk-mode | dup (same as assemblia:13) |
| 14 | dialectic-rule | dup: rule 20 + `dungeon-pets/CLAUDE.md:11` |
| 22 | meshy-3d-needs-permission | dup: rule 17 |
| 32 | meshy-prompt-review | dup: rule 17 (style block in `dungeon-pets/docs/meshy_usage.md`, checked) |
| 45 | no-reference-edits | dup: rule 17 |
| 55 | rejected-approach-stop | dup: rule 8 |
| 65 | risk-reward-first | dup: rule 9 |
| 77 | robot-army-pivot | stale: both projects failed/abandoned; `POSTMORTEM.md:5` already points to Assemblia (checked) |
| 93 | switch-compatible | project-only, already in `docs/constraints.md:58` (checked); "No gamepad bindings exist yet" is stale (checked: `scripts/core/game_input.gd` has 26 joy lines) |
| 105 | testing-off-by-default | dup: rule 14 + `dungeon-pets/CLAUDE.md:17` |
| 114 | v21-restyle-dropped | stale: project failed; cause already in `docs/research.md:819` "Hair glued to arms" (checked). The Meshy lesson is cross-project (Moonsick uses Meshy) → one line into `machine-setup.md` (below). Quote dropped: "lets just forget this and keep with the old design and prompts, lets give up" |
| 129 | websearch-when-unsure | dup: rule 10 + `dungeon-pets/CLAUDE.md:3-6` |

### `~/Playground/game-design-research/docs/memory-archive.md` (3.2 KB, 3 entries) → move 2 bits, delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | autonomous-build-preferences | dup: rules 15, 16, 20. Two clauses not in rule 16 move there (keep useful docs; carry over pattern docs). Quotes kept in rule 16: "keep useful docs. learn them". Quotes dropped: "ill give you lots of freedom", "i expect a full game", "design features and implement if you think is missing.. or if there are gaps", "you can use meshy ai", "same as the red button game.. open the game in a corner" |
| 23 | current-game | stale: names DRS as current (see Q1). Move the competitor fact into `game-design-research/CLAUDE.md` (below) |
| 37 | indie-games-hub-source | mostly in `game-design-research/CLAUDE.md:56-59` (checked); the channel id, video titles and the finding are only here → move (below) |

Moves into `~/Playground/game-design-research/CLAUDE.md`:
- Line 55, old: `- **Pet the Cat** (user, 2026-11-07) replaces Red Button as the game: \`~/Playground/pet-the-cat\`.`
  New: `- **Pet the Cat** (user, 2026-11-07) replaces Red Button as the game: \`~/Playground/pet-the-cat\`. Then Deathly Reality Show (2026-11-07; nearest competitor found: 7 Minutes in Hell, a co-op horror game show), then Moonsick (2026-11-12, from the user's Full Moon idea). Current status: \`~/.claude/notes/projects.md\`.`
- Line 59, after "FINDINGS still empty)." add: `Channel UCt8CJiye87FMbEwt0npPMuQ posts "Top N Best Indie Games of <month>" (look-back) and "Top N New Indie Games in <month>" (upcoming); descriptions list Steam links, auto-captions hold the blurbs (and the names when the description hides the top 3). Finding: the picks are well-made single-player indies; weak for spotting friendslop competitors.`

### `~/Playground/hordeline/docs/memory-archive.md` (0.8 KB, 1 entry) → delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | mute-test-runs | dup: rule 15 + `hordeline/CLAUDE.md:61` + `machine-setup.md:20` (`--mute` checked in `docs/progress.md:30`). Quote dropped: "0 volume pls on playtest" |

### `~/Playground/music-claude/docs/memory-archive.md` (1.9 KB, 2 entries) → move 1 quote, delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | exercises-in-musescore | dup: `music-claude/CLAUDE.md:28-40` (all authoring rules, checked). Move the quote: line 30 old `- Every graded item is composed in MuseScore. No Python coding exercises.` → new `- Every graded item is composed in MuseScore (user, 2026-10-13: "exercises should be in musescore entirely"). No Python coding exercises.` |
| 15 | musescore-cli | dup: `music-claude/CLAUDE.md:43-44` + `notes/music-setup.md:15` |

### `~/Playground/mustache-madness/docs/memory-archive.md` (3.1 KB, 3 entries) → delete file (after Q2)
| Line | Entry | Verdict |
|---|---|---|
| 5 | afk-pc-poweroff-hypridle | stale method: replaced 2026-10-30 by `claude-keepawake.sh` (`machine-setup.md:25-30`; checked: script, `hypridle-afk.conf`, `.bak` all exist). Conflicts with rule 11 → Q2. Quote dropped (if Q2 goes to rule 11): "dont turn off machine" |
| 15 | afk-progress-on-disk | dup: rule 11 + `machine-setup.md:32-33`. Quotes move to `machine-setup.md:32` (below) |
| 25 | afk-screen-locked-no-rendered-runs | dup: rule 16 ("No rendered performance numbers") + `machine-setup.md:31` |

### `~/Playground/red-button-experiment/docs/memory-archive.md` (5.5 KB, 8 entries) → delete file
| Line | Entry | Verdict |
|---|---|---|
| 5 | ai-games-muted | dup: rule 15 + `machine-setup.md:12`. Quote dropped: "also on afk sessions. games opened by ai muted pls" |
| 16 | ai-runs-background | dup: rule 15 + `machine-setup.md:10-19`; its "top-left" is stale (checked: `tools/ai_run.sh:2` says bottom-left, user "open at the left bottom corner") |
| 26 | diagrams-as-images | dup: rule 13 + `machine-setup.md:35-37`; "(no matplotlib/rsvg)" moves to `machine-setup.md:35` (checked: neither installed). Quote dropped: "im using kitty you dont have to show text" |
| 35 | narrator-no-noise | project-only, already in `docs/dialog-design.md:15-16` with the quote (checked) |
| 44 | no-screenshot-every-change | dup: rule 14. Quotes dropped: "no need to take screenshots for everything.. i can do it on my own", "if its cheap" |
| 54 | patterns-need-research | dup: rule 10. Quotes move to rule 10 (below) |
| 64 | quiet-game-audio | project-only, already in code (`scripts/audio/sfx.gd:6` `MASTER_VOLUME := 0.1`) and `docs/audit.md:125` (checked). One doc cites "memory": `docs/game-feel-patterns.md:119` old `quiet (memory: master volume 10%). *[opinion]*` → new `quiet (user, 2026-11-03: "set the volume at 10%, the sound"; \`Sfx.MASTER_VOLUME = 0.1\`). *[opinion]*` |
| 73 | tests-once-at-end | dup: rule 14. Quote dropped: "never run tests until the very end and once" |

### `~/.claude/notes/archive/runpod-claude.md` (1.0 KB, 1 entry) → delete file (and `notes/archive/`)
| Line | Entry | Verdict |
|---|---|---|
| 5 | interrupted-create-pod | dup: rule 12 + `machine-setup.md:43-44`; project gone (checked: no `~/Playground/runpod-claude`). Quote dropped: "you have 2 open pods" |

### CLAUDE.md edits that carry archive content (exact text)

Rule 10 (lines 57-59), old:
```
10. **Research before planning or building.** Web search first; record findings with sources in the
   project's docs. Pattern and anti-pattern lists are always researched, each item tagged
   [source] / [read] / [opinion]; if research isn't possible, say up front the list is unresearched.
```
new:
```
10. **Research before planning or building.** Web search first; research why a good X works, not only how to
   build it; record findings with sources in the project's docs. Pattern and anti-pattern lists are always
   researched, each item tagged [source] / [read] / [opinion]; if research isn't possible, say up front the list
   is unresearched. Why: user, 2026-11-03: "are these studied? researched?", "when writing patterns.. research is
   always needed".
```

Rule 16 (lines 73-75), old:
```
16. **AFK game builds:** the user expects a full, runnable game and gives design freedom; tag
   Claude's own design calls "(Claude)" in the design doc. No rendered performance numbers (the
   screen locks); headless only. Meshy is allowed for hero art.
```
new:
```
16. **AFK game builds:** the user expects a full, runnable game and gives design freedom; tag
   Claude's own design calls "(Claude)" in the design doc. Carry over the researched pattern docs and check
   features against them; keep a build/run doc and a todo of gaps (user, 2026-11-07: "keep useful docs. learn
   them"). No rendered performance numbers (the screen locks); headless only. Meshy is allowed for hero art.
```

Rule 17 (lines 76-78), old:
```
17. **Meshy while the user is present:** before every generation, show the shared style prompt, the
    exact prompt and the diff from the last try, then wait for OK. Image-to-3D and rigging need an
    explicit OK each time. Concepts are always new text-to-image, never edits of an existing image.
```
new:
```
17. **Meshy while the user is present:** before every generation, show the shared style prompt, the
    exact prompt and the diff from the last try, then wait for OK. Image-to-3D and rigging need an
    explicit OK each time. Concepts are always new text-to-image, never edits of an existing image; an image
    the user names means "start from its saved prompt", never "feed it in". "Iterate until right" lifts
    none of this (user, 2026-10-31: "show the diff and ask before doing").
```

Rule 20, after line 96 ("into its entry and count it (user, 2026-11-08)."), add:
```
    - First asked 2026-10-30 as a rule for every decision: "dialectic is important. mark that as rule".
```
(If Q3 is answered yes, also add: `- In the idea search (\`generate-ideas\`), the critic is an inline pass, no subagents (user, 2026-11-10: "it no multiagent just here").`)

---

## 2. `~/.claude/notes/critic-anti-patterns.md`: 34.7 KB → 11.9 KB

Read as of 23:39 (336 lines, including the newest repeat "A state change in the middle of an action" ×2, Moonsick
hands r3). The main session is still adding to it: merge anything newer before applying.

What changed:
- Every one of the 121 entries is kept as a pattern, its count and its fix; 17 near-duplicates merged into 12 entries,
  so 104 lines. The stories (which round, which object, the numbers) are dropped; they live in each project's critic
  and synthesis files (paths checked: Moonsick `docs/ux-thesis.md`, `docs/critic-core-r1.md`; `research_notes/Full Moon/
  critic-r1..r5.md`; `Idea search/round1.md`, `tournament/results.md`, `loop1/results.md`, `fix-minigame-feel.md`;
  `Gameplay verbs.../new_verb_thesis.md`; `formula-fixes.md`).
- Regrouped by theme instead of by session, so one scan covers each kind of mistake.
- Every quote of the user's words is kept, except two that live elsewhere: "one seed, derive the other two" (kept in
  `game-idea-triad.md`) and "nobody needs anyone" (a DRS doc's words, not the user's).
- One count raised: "A voice-only game tested with bots" ×4 → ×5, adding the Pet the Cat head-reader repeat that the
  quarterback entry noted but didn't count.
- "A gate marked weak" now points to the proposed rule 23 instead of `[[drop-what-fails-a-check]]`.

Merged near-duplicates (old entries → new entry):
1. "Fixing each finding by adding a rule" ×2 + "'4–8 systems' read as room for 18 rules" ×2 + "A rule count that counts
   only what changed" ×1 → **Rules pile up uncounted** ×5
2. "Fixing each finding by adding text" ×2 + "One fact shown twice blows the word budget" ×1 → **Text piles up** ×3
3. "A tool that names the answer" + "A 'do this now' line that makes the core choice" + "An auto-filled conclusion turns
   deduction into a checklist" (×1 each) → **The game names the answer** ×3
4. "A first build that tests one side of the coupling" + "Teaching only one side of a split" → **One side of a split
   built or taught** ×2
5. "A doc claim the code never had" ×2 + "Layout move without measuring" + "A mechanism the data model can't carry" + "A %
   column whose meaning doesn't match the draw rule" → **A claim about the build not checked in code** ×5
6. "A coordination game that settles into a protocol" + "Two-way at round 1, one-way by round 5" → **The crew settles
   into a protocol** ×2
7. "The threat hunts whoever holds / did / is most X" + "A threat that goes to the last noise" → **A simple threat rule
   has a one-line answer** ×2
8. "A safe end state ends the round early" + "A safe state that gives extra information rewards sacrifice" → **A safe
   state** ×2
9. "A Claude end-rule that rewards betrayal" + "Awards that pay for betrayal" → **A rule or award that pays for
   betrayal** ×2
10. "Restrictions added beyond the user's words" + "A different shape for the user's ask, labelled 'the user's call'" +
    "A fix that decides what the critic said to ask" → **Claude's call passed off as the user's** ×3 (A6)
11. "The same case rated two ways" ×2 + "Raters adding their own rules" ×1 → **Raters disagree or add rules** ×3
12. "A check that can't fail" ×1 + "Checks that don't tell ideas apart" ×2 → **A check that can't fail or doesn't split
    the field** ×3

Also noticed: the old entry "A different shape for the user's ask" cites "A25", but design-anti-patterns 25 is "Frame
finding parked"; the pattern matches A6 "Deciding for the user" (assumed), so the new text cites A6.

Full proposed new text:

```markdown
# critic-anti-patterns

What isolated critics keep catching in Claude's design theses (CLAUDE.md rule 20): pattern, ×count, fix. Scan before
a thesis; after each synthesis add or merge (raise the count). A/B items = `~/.claude/design-anti-patterns.md`.
Stories: each project's critic/synthesis files (DRS and Moonsick `docs/`, `game-design-research/research_notes/`).

## Caught by the user after the critics passed it
- **A reward that ends the need for others** ×1 ("you no longer need someone to help you since you wont transform
  again.. so loosing trust is not that important"). Fix: no safe state; a catch gives what a cure gives.
- **A loss the numbers can't reach** ×1 ("how is it possible to lose on a night?"). Fix: compute the worst one round
  can do before adding stakes across rounds; one long round carries final deaths.
- **A voice-only game tested with bots** ×5 ("still doesn't understand"). Fix: it must work with the user's test crew
  (1 human + bots); physical verbs bots can answer.
- **Hidden rules patched with words** ×3 ("replace it"; "I don't understand what to do"). Fix: if the one-sentence
  rule needs a second sentence, change the game, not the text; practice stages the rules.

## Teaching and text
- **Instruction from the system's view** ×1. Fix: say what the player who sees it does.
- **Rules pile up uncounted** ×5 ("too detailed"). Fix: ≤ 3 taught rules, the rest objects, discovery or hidden
  numbers; after a synthesis count every switch a player must know, at both ends, before vs after; move riders to a later game.
- **Text piles up** ×3 ("50% less text"). Fix: one word budget for all transient text (HUD line ≤ 8); new teaching
  replaces old; one channel per fact.
- **A budget rule with no stated scope** ×1. Fix: name what it covers.
- **The dead get only a voice** ×3. Fix: a visible physical job bots can read; a ghost who helps a cure comes back.
- **An untaught rule breaks what players said** ×1. Fix: telegraph it, or keep the said word valid.
- **Claiming ownership the rules don't have** ×2. Fix: word each line from the rules' real data.
- **The hardest rules get the least teaching** ×2. Fix: teach in proportion to difficulty.
- **A shared screen leaks the split information** ×1. Fix: shared displays show examples, never live secrets.
- **The game names the answer** ×3 (the user's "hard to read" signs did nothing). Fix: tools show signs; guidance
  teaches each verb once, never the decision; notes log facts, combining stays the player's.
- **A teaching line sends everyone to one spot** ×1. Fix: only in a solo practice coach.
- **One side of a split built or taught** ×2. Fix: build and teach both sides (human patient + bot doctors).
- **Opposite next steps, alike feedback** ×1. Fix: differ in shape and direction, not strength.
- **Readability fixed, choice left dead** ×1 ("dont know any choices"). Fix: sim the core choice first; each option
  must win somewhere.

## Space, look and the code
- **A rule zone unmarked** ×1 **or marked wrong** ×1. Fix: draw the zone, exactly.
- **Decoration where the surface could carry rules** ×1. Fix: one mechanism for look and teaching.
- **A screen showing its own feed** ×1. Fix: graphics on the big screen; the TV view shows the same.
- **A claim about the build not checked in code** ×5. Fix: read coordinates, data structures, ranges and the draw rule
  in code before a thesis leans on them.
- **Copying bot perception copies its privileges** ×1. Fix: a player sees only by distance, light, earshot.
- **A map drawn without checking handedness** ×1. Fix: axes from the engine (Godot +X right, −Z forward).
- **Danger feedback through walls = a radar** ×1. Fix: needs line of sight.
- **Art that doesn't match its collision** ×1. Fix: fit the art to the gameplay box.

## Phases, flow and time
- **Practice leaks into live** ×1. Fix: reset positions and hidden info; real pressure minus deaths.
- **Practice with no cost** ×1. Fix: a mistake resets progress.
- **One player skips or carries the learning** ×2 ("i wouldnt say that the bots are the issue.. everything is
  wrong"). Fix: per-player ticks gate the start; don't blame a side cause for the user's confusion.
- **Added phases × every level** ×1. Fix: count seconds per show; teach once, forgive once.
- **One key with several jobs** ×1. Fix: a separate flow-control key.
- **The rule changes per phase** ×1. Fix: one exception rule for every phase.
- **A state change mid-action** ×2. Fix: freeze actions in flight; grace time; a held button flips once at most,
  toward safety; every other verb needs a fresh press.
- **A fix that undoes an earlier fix** ×4. Fix: re-check every earlier round's fixes.
- **One task at a time = a calm conveyor** ×2. Fix: tasks overlap and speed up.
- **A limit that never binds** ×4. Fix: check it against the real value; scale with people left.
- **An undefined failure state** ×1. Fix: write what each object does if nobody touches it.
- **Test setup deadlocks** ×3. Fix: every bot wait has a timeout and fallback; play the test crew through each gate.
- **A cost that steps, not slides** ×1. Fix: slide it every second.
- **A fixed schedule exposes fakes** ×2. Fix: random timing; tie tricks to real cases.

## Crew and coupling
- **One seat holds the cue or decision (quarterback)** ×5. Fix: all decide at once (gate 7); split by position.
- **A partner who only stands in place** ×2. Fix: the receiver commits too, or holds half the information.
- **Speed parity lets one player do it all** ×1. Fix: compare solo and team speed.
- **Fixed endpoints make a static optimum** ×1. Fix: move an endpoint each round.
- **Grouping that doesn't divide the crew** ×1. Fix: one coupling through everyone; check odd sizes.
- **A timed joint press counted as coupling** ×2. Fix: needs a decision, not a rhythm; check lag (~0.2 s).
- **A pooled sum counted as coupling** ×3. Fix: different actions that fail without each other.
- **Hidden info nobody gains from hiding** ×2. Fix: a counter verb and a reason to lie.
- **Blame moved to a replay** ×1. Fix: one body failing, visible in the moment (gate 4).
- **Content needing more than the smallest crew** ×1. Fix: scale requirements with crew size.
- **A search budget not scaled to the smallest crew** ×1. Fix: fewer searches than suspects at every size.
- **Bots as the counter in a team game** ×1. Fix: ask who the counter is in the test crew.
- **A side with no goal stands still** ×1. Fix: every side gets a goal that forces risk.
- **Silence assumed online** ×3. Fix: never the core (Discord); talking allowed and still not enough.
- **A rescue that needs two soft-locks the end** ×1. Fix: check joint actions with one survivor.
- **The crew settles into a protocol** ×2. Fix: judge the plan by round 5; something keeps the routine moving.
- **A plan breaker bolted on** ×1. Fix: build it with the core.
- **A simple threat rule has a one-line answer** ×2. Fix: the threat searches, or round info changes the best plan; no safe spot.

## Rules, choices and stakes
- **An undefined value lets the cheapest option win** ×1 (A11). Fix: define it so the coupled option pays.
- **A carry-over trigger with no count** ×1 (A11). Fix: count it; apply between rounds.
- **A safe state** ×2. Fix: nothing safe forever; a ghost sees nothing hidden.
- **An outer layer on a closed round = a board over minigames** ×2 (B13). Fix: a push choice that the carry-over
  changes next round, not just a score.
- **A carried harm with no way back = a death spiral** ×1. Fix: an undo that needs a friend.
- **One verb strictly better than its sibling** ×1. Fix: a different cost each.
- **A shared good that is really private** ×1. Fix: call it private, or share the outcome.
- **A rule or award that pays for betrayal** ×2. Fix: check end rules at 2 alive; award only what the pillars want.
- **No carry cap = a super-player** ×1. Fix: a hand limit.
- **A % value that names one option** ×1. Fix: share each value across 2+ options; P(option | sign) 50–65%.
- **A free retry turns a guess into a test** ×2. Fix: a wrong try costs more than waiting somewhere; sim it.
- **An effect on a hidden meter** ×2 ("running away feels safer" is a feel problem). Fix: show it on the body.
- **A defence with no counter** ×2. Fix: works once, then waits, or half speed while raised.
- **A split one side can finish alone** ×1. Fix: each side gets a new piece per step.
- **A scene's numbers not worked out** ×5. Fix: compute every number with a script before writing.
- **A fixed cost per failure makes sacrifice cheapest** ×1. Fix: the cost depends on how it ends.
- **A benefit with no rule that makes it** ×1. Fix: name the rule.
- **A "choice" with one free option** ×1 (B15). Fix: price it or drop it.
- **A weakness that makes a fortress** ×2. Fix: few lights, creatures put them out; no slows.
- **Spectators as free scouts** ×1. Fix: the dead watch from a living friend's eye height.
- **A protection for one helping role** ×1. Fix: protect by where you stood at the danger moment.
- **Immunity at small crews** ×1. Fix: a head start, never immunity.
- **A power that erases its own counter** ×1. Fix: make the counter matter more.
- **An extra kill window that reaches only helpers** ×1. Fix: check who a new danger can reach.
- **A contest nobody wants to win** ×1. Fix: name who wants each side with today's features.
- **Merged verbs collide under pressure** ×2. Fix: rank by worst failure; lock at the press; switch on a visible
  world state, never a distance ring.

## The user's words and past work
- **A diagnosis stated as fact** ×1. Fix: quote the user's verdict, or tag [opinion].
- **A fix the failed game already had** ×1. Fix: read its design doc and README first.
- **A fix that is a new game** ×2. Fix: say don't fix.
- **Redesigning what was never playtested** ×3. Fix: playtest it; search the user's repos for the shape.
- **A sketch that breaks the project's gate** ×1 ("a Looney-Tunes goofy tower-defense farm"). Fix: read the pillars;
  take a conflict to the user (A4).
- **Pillars dropped silently** ×5 ("reach somewhere = a level", "2 at once, but rare", "a % per sign"). Fix: list every
  confirmed pillar a sketch drops.
- **The same answer reused across fixes** ×1 (A1). Fix: a different verb per game.
- **Candidates that differ only on the surface** ×3 (A2). Fix: name each one's hidden thing; same = one.
- **A gap claimed unchecked** ×1. Fix: check the source row by row.
- **A method the user already rejected** ×4 ("start of the game doesnt explain"). Fix: re-read their verdicts first.
- **Claude's call passed off as the user's** ×3 (A6; "not visible in screen"). Fix: build the user's words, tag Claude
  additions; answer the ask as given; a "to the user" finding goes to the questions file.
- **Research in the folder left unused** ×1 (B26). Fix: read the latest research entries first.
- **A gate marked "weak"** ×1 (B25). Fix: pass/fail only; weak = fail (CLAUDE.md rule 23, proposed).

## Checks, raters and method
- **Pass rates of unlike samples compared** ×1. Fix: like with like, or no winner.
- **Raters disagree or add rules** ×3. Fix: a written reading of each check, mixed answers included; measure agreement
  after each gate change.
- **A check that can't fail or doesn't split the field** ×3. Fix: drop it; add missing ones (caller seat, dev-crew
  testability, build cost, lag); if one blocks everything, search for it directly.
- **A method built from the raters' own praise** ×1. Fix: judge it on checks they didn't write.
- **A rerun of the winning method** ×1. Fix: carry forward what the scores showed, not the method.
- **A scorer reading outside its brief** ×1. Fix: name the only files it may read.
- **Web search budget not planned** ×1. Fix: budget searches per step (~200 per session).
```

---

## 3. Other notes, INDEX.md and CLAUDE.md

### `notes/INDEX.md` (2.5 KB)
- Line 13: delete the `drop-what-fails-a-check.md` row (it becomes rule 23).
- Line 18, old what/read-when: `player-with-player gate first, failure-focused research each round` → new: `the user's
  directions for the idea search, in their words (the method is the generate-ideas skill)`.
- Line 20: delete the `archive/runpod-claude.md` row (file deleted).
- Lines 22-24, old: "Per-project notes moved 2026-11-12 into each repo: `docs/memory-archive.md` in assemblia, ...
  Backup of the old hidden folders: ..." → new: `The 2026-11-12 per-project memory archives were folded into each
  repo's docs and CLAUDE.md, then deleted. Full copy of the old hidden memory: \`~/.claude/backups/auto-memory-2026-11-12.tar.gz\`.`
- Every row has a "read when" (checked).

### `notes/projects.md` (2.8 KB): stale rows → full new text below
- Line 3 vs 11: two active games → Q1.
- Lines 5-7: "each project's own memory folder ... don't load" is stale (checked: no `~/.claude/projects/*/memory` left).
- Line 14 Hordeline "status not recorded": stale; `game-design-research/CLAUDE.md:52` says "Hordeline dropped (user,
  2026-11-03: hard to find good ideas on a Vampire Survivors base)" (checked).
- Line 17 `rival-radar`: stale; the folder is gone and `game-design-research`'s first commit is "Start rival-radar"
  (checked), so it is the same repo, renamed twice (assumed from the commit).
- Line 19 Mustache Madness "status not recorded": `game-idea-triad.md:9,47-49` records the core dropped late Oct 2026
  after 6 months of loops.
- Line 20 Moonsick: worktree `~/Playground/moonsick-hands` on branch `hands` is missing (checked `git worktree list`).
- Lines 22-24: "stay in each project's memory folder under `~/.claude/projects/`" is stale (checked: gone). Where those
  facts live now (checked): narrator lines `red-button-experiment/docs/dialog-design.md:15`; 10% volume
  `scripts/audio/sfx.gd:6`; Switch mapping `assemblia/docs/constraints.md:96`; duo-form exercises
  `music-claude/CLAUDE.md:28-40`; Emberpup redo `dungeon-pets/docs/research.md:819` (project failed).
- Lines 26-28 Full Moon: "4 critic rounds" is stale (checked: `critic-r1..r5.md`, 5 rounds); the open "5 nights or one
  long night" is settled: `Full Moon/user-pillars-2026-11-12.md:3` "U2 kept as one night" (checked). Folded into the
  Moonsick row.
- Not listed: `dungeon-pets-js-prototype` (assumed part of Dungeon Pets, added to its row); non-game folders (Carpenter,
  CV, qv, finance-tracking, mom-trip, token, claude-code-reaper) are out of the table's scope.

```markdown
# projects

Where each of the user's game and research projects lives (~/Playground) and its status; Moonsick is the active game (Nov 2026)

Claude is started in `~/claude-code` for every project (user, 2026-11-09), so a project's `CLAUDE.md` doesn't load:
read it first. Status from each project's docs and last commit, checked 2026-11-12.

| Project (`~/Playground/…`) | What | Status |
|---|---|---|
| `moonsick` (+ worktree `moonsick-hands`, branch `hands`) | the user's Full Moon idea: online co-op with betrayal for 4–8, one dark night (~12 min, deaths final), diagnose friends turning into werewolf/vampire/troll; GitHub Akirakii/moonsick (private) | **active**: v0.1 AFK build 2026-11-12; user "i dont understand what to do" → readability/feel/map/Meshy pass (`docs/HANDOFF_ux.md`); user "nothing has improved", 13 points → core thesis + critic r1 (`docs/core-thesis.md`): step 1 = fewer rules, big body signs, little UI, bots slower (user); waiting on the user's go; uncommitted work on main. Design history: `game-design-research/research_notes/Full Moon/` (5 critic rounds; one night settled in `user-pillars-2026-11-12.md`) |
| `deathly-reality-show` | co-op friendslop, 3–6 players, deadly TV game show hosted by the Reaper | (status: see tidy question Q1) active from 2026-11-07, last commit 2026-11-08; its CLAUDE.md and docs/design.md are the source of truth |
| `pet-the-cat` | co-op friendslop, keep a huge cat calm | dropped 2026-11-07 ("i dont like this one") |
| `red-button-experiment` | co-op friendslop, press one red button | dropped before Pet the Cat; reference only |
| `hordeline` | co-op train defense, Vampire Survivors-style upgrades | dropped (user, 2026-11-03: hard to find good ideas on a Vampire Survivors base; game-design-research CLAUDE.md); reference |
| `assemblia` | robot army auto battler | abandoned 2026-11-01; 4 untested `exp/*` branches kept |
| `dungeon-pets` (+ `-base`, `-js-prototype`) | first-person creature-pack roguelike | failed 2026-10-31; see its POSTMORTEM.md |
| `mustache-madness` | Godot game, perf work Oct 2026 | core dropped late Oct 2026 after ~6 months of loops (user, see [[game-idea-triad]]); last commit 2026-10-28 |
| `game-design-research` (started as `rival-radar`, then `competition-research`, renamed 2026-11-09) | market and game design research | research only; rank on measured Steam/YouTube signals |
| `music-claude` | composition self-study (carpenter course `duo-form`) | see [[music-setup]] |

Project-only notes live in each repo's `docs/` and `CLAUDE.md`. Lessons for picking the next game: [[game-scope-lessons]].
```

### `notes/machine-setup.md` (3.0 KB): checks and 4 edits
Checked: `ai_run.sh` bottom-left, 640x360, `noinitialfocus`, `--audio-driver Dummy` (RB, DRS, Moonsick); Moonsick's
`--no-capture` (`tools/ai_run.sh:14`, `scripts/game/game.gd:154`); Hordeline `--mute`; `hypridle.conf` lock 300 s, dpms
330 s, poweroff 3600 s with `ignore_inhibit = true`; `hypridle-afk.conf` has no poweroff; `claude-keepawake.sh`;
`statusline-command.sh:3` writes `claude-statusline-last.json`; `.bak-afk`; the image-pane mod path; `magick`;
`art/concepts/*/*.prompt.md` (dungeon-pets). Assumed: `--position` ignored on Hyprland, PATH in Hyprland exec, ~1 fps
on a locked screen (not re-run). Overlap: `skills/afk-run/SKILL.md:12-13` repeats the keep-awake steps (fine: the
skill holds the steps, this note the facts).
- Lines 10-12, old: ``exists in `~/Playground/deathly-reality-show` and `~/Playground/red-button-experiment`: ... (checked 2026-11-09)``
  → new: ``exists in `~/Playground/moonsick` (+ `moonsick-hands`), `deathly-reality-show` and `red-button-experiment`: ... (checked 2026-11-12)``
- Lines 32-33, old: `... map each thing the user asked for to a task row.` → new: `... map each thing the user asked
  for to a task row (user, 2026-10-11: "also record your progress for any case this computer shut downs"; "evaluate
  every single word i mentioned and create tasks").`
- Line 35, old: ``render with `magick`, show`` → new: ``render with `magick` (no matplotlib, no rsvg-convert; checked
  2026-11-12), show``
- Lines 39-41, old: `**Meshy**: API key from its key file, never printed.` → new: ``**Meshy**: API key in
  `~/.config/meshy/api_key` (MCP launcher `~/.config/meshy/run-mcp.sh`; both checked), never printed.`` And add after
  line 41: `Auto-rig glues shoulder-length hair to T-posed arms when the head is wider than the shoulders; prompt fixes
  (no side hair, ponytail) didn't solve it (Dungeon Pets Emberpup, 2026-10-31; \`~/Playground/dungeon-pets/docs/research.md:819\`).`
- Lines 43-44 RunPod: same fact as rule 12; keep (it holds the concrete `list-pods` command).

### `notes/music-setup.md` (2.7 KB)
Checked: `~/.local/opt/musescore`, `~/.local/bin/musescore` (`QT_SCALE_FACTOR=1.5`), `/usr/bin/mscore` still installed,
`~/.local/opt/muse-sounds-manager`, `~/Muse Sounds`, `~/.local/bin/reaper`, `~/.wine-spitfire`, yabridgectl in
`~/.local/share/yabridge`. Assumed: the render commands (not run). Line 15 repeats `music-claude/CLAUDE.md:43-44`
(both short; keep, this is the machine fact).
- Line 19, old: `(the old \`~/claude-code/playground/\` path is gone, checked 2026-11-09)` → new: `(the old
  \`~/claude-code/playground/\` is empty, checked 2026-11-12)` (checked: it exists, empty).
- Line 19, old: `(details in that project's memory folder)` → new: `(authoring rules: \`~/Playground/music-claude/CLAUDE.md\`)`.
- Placement: only music-claude uses it today, but it is machine setup (could serve game audio). Keep in notes (Claude).

### `notes/game-scope-lessons.md` (1.1 KB)
- Lines 15-16, old: `The earlier "default to single player" from the Assemblia note is superseded by the co-op choice.`
  → new: `Assemblia's earlier "default to single player" (2026-11-01) is superseded by the co-op choice.` (the Assemblia
  note is deleted).

### `notes/drop-what-fails-a-check.md` (1.2 KB) → promote to CLAUDE.md rule 23, delete the note
Ready to promote: the same lesson three times: freezing cold offered twice after itching was rejected for the same
reason (this note), a co-op gate written "weak" (critic note, Moonsick hands r1), a frame finding parked
(design-anti-patterns 25, DRS v1). Add under `### Output` as rule 23, so rules 14–22 keep their numbers (rule 20 is
cited in skills and notes):
```
23. **A failed check is a fail.** Before showing candidates against a test (Claude's own, a gate, the user's), mark
    each pass or fail; drop a fail or show it as "fails X", never softened ("or a tiny", "mostly", "weak"). After the
    user rejects one item for a reason, re-check every other item against that reason first.
    Why: 2026-11-12, Moonsick symptom table: freezing cold offered twice as "felt only" after itching was rejected
    for the same reason (user: "freezing cold again.. that is something that others can notice.. you cannot check
    yourself? or are you not thinking before answering?"); same shape as a gate written "weak" and a parked frame
    finding. When: proposing options against any rule, gate or test.
```

### `notes/game-idea-triad.md`: 6.5 KB → 3.0 KB (full new text below)
Kept: the model, their history, all four rejections with quotes, their constraints, their graph model, their formula,
and Claude's replies with no verdict yet (one line). Dropped: the kitchen analogy (Q4); Claude's coined labels (keystone,
swap test, joints, spokes, which `explain-concepts-plainly.md:13` bans); the "test the joints" method (the user's
"everything is related and interconnected" rejects it); Claude's long replies (wicked problems, NK details: in
`game-design-research/research.md:55-102`, checked); the user's 2026-11-09 restated model (their own later graph
model replaces it; it had no direct quote).

```markdown
# game-idea-triad

The user's own model of a good game idea (fantasy + logic + aesthetic, aligned), in their words, and what they rejected

**Model (user, 2026-11-08):** a good idea needs a good **fantasy**, **logic** and **aesthetic**, all three **aligned**.
Each alone is easy to imagine; aligning them is the hard part. Use their three words.

**Their history:** 6 months of loops on Mustache Madness until a foundational problem made the fun fall apart (late Oct
2026). Since then they stop when a foundation needs too many loops, and try a new foundation about once a day (Red
Button, Pet the Cat, ...), to spot the foundational problem faster. They don't know what that problem is; a slight
foundational change moves the whole structure ("like NP complete? fun is easy to check").

**Rejected by the user; don't offer again (all 2026-11-08):**
- "One seed, derive the other two": they already do it; "chicken and egg... changing the aesthetic or logic redefines
  the fantasy".
- "Anchor on one moment of play": "that is just exactly my problem.. that exact moment can fit for one of the pillars..
  when i try to fit 2 or 3.. it falls apart". No more ways to align the three in the head.
- Testing the parts separately: "everything is related and interconnected.. spark and understanding.. fantasy,
  aesthetic and logic..". Don't split the whole.
- Restating the search loop: it is already clear to them.

**Constraints (user, 2026-11-08):** playtesting is expensive and testers aren't always there, so they fall back on
imagination; a locked-in build "feels wrong from the start, not repairable with tuning."

**Graph model (user, 2026-11-09; use their words):** scope = number of nodes; coupling = number of connections; high
scope = more content and polish loops; high coupling = more loops to establish the core identity; loop = playtest, then
change the graph's structure or its elements. Claude's two additions, approved: connections have a direction (a hub
works when it changes the features but they don't change it; Red Button failed that: "a narrator keeps changing what
the button does"); when scope and coupling are both high their costs multiply (Mustache Madness, Claude's read).

**Formula (user, 2026-11-09):** low content can be fun without high coupling because "the true fun comes from the
emergence of social interaction with your friends.. friends are always unique without me having to implement.. thats
why friendslop works". Claude added: friends only create emergence when the hub connects them; retention is the limit.

**Claude's replies with no verdict yet (Claude, 2026-11-08/09):** check alignment after playing a tiny build with
people, not bots; 3 seeds built in parallel, each with a hypothesis and a kill line, then one side-by-side session;
learn across foundations from a log of the same key choices. Evidence and sources: `~/Playground/game-design-research/
research.md`, entry "2026-11-09: how to find a good game idea". Related: [[idea-search-loop]], [[explain-concepts-plainly]].
```

### `notes/idea-search-loop.md`: 5.1 KB → 2.8 KB (full new text below)
Most of it is now built into the skill (checked: `generate-ideas/SKILL.md:8-9` no subagents, `:23,151` failed list shows
the idea, `:109-119` [job] [choice] [goal] and concrete words; `checks.md:8-23` force and player gates first, `:27,46`
no places). Kept: every user quote, and where the search stands. Dropped: "show its shape before building it" (the
skill exists, checked); "use agents only for big rounds" (replaced by the user's later "no subagents"); the 126-idea
story.

```markdown
# idea-search-loop

The user's directions for the game idea search, in their words (2026-11-10/11); the method lives in the `generate-ideas` skill

Each direction is built into `~/.claude/skills/generate-ideas/` (SKILL.md, checks.md). This note keeps the user's
words and where the search stands.

- **Players act on each other, checked first:** "the check should see if there is high player coupling first.. i can
  already sense that log rollers doesnt have player with player interaction" (scorers were too lenient on players side
  by side on one object, Megalith Haul). Now checks.md gates 0–1.
- **Learn from failures with web research:** "add websearch but to understand what is going wrong and improve.. or
  understand what is truly player with player interaction.. a learning websearch research from failure focus".
- **An idea is fantasy + logic + aesthetic:** "perhaps we are missing here those elements?" (see [[game-idea-triad]]).
- **No subagents:** "it no multiagent just here"; "the skill now should not work with multiagent.. should do first:
  list of fantasies, reason of why interact with other player, check against the formula".
- **A fantasy needs a force:** "i dont understand what forces the need to suck blood from each other?"
- **"Reach somewhere" = completing a level = medium to high content:** objectives are never places.
- **Show both lists:** "always display the lists those that passed and those that didnt"; "when displaying the failed
  list.. i want to see the actual idea".
- **The goal fits the fantasy:** "the goal doesnt fit the theme"; each idea also has a job.
- **Idea line:** [job] [struggle] [goal] landed ("this is way much beter"), with physical actions instead of vague
  words ("fight it"); then [job] [choice] [goal]: "include some sort of main choice to make in the game.. [job] [choice]
  [goal]" (the main choice a *player* makes; Claude first misread it as variants for the user).
- **Living pool, self-improving skill (2026-11-11):** "keep improving the passing ones and keep fixing the failing
  ones and keep adding more.. keep expanding understanding.. how to improve methodology"; "could you also auto improve
  the skill itself if it is working?"

**Where it stands (2026-11-11):** a 2-hour run (29 cycles) reached 32 passing ideas in 21 cores
(`~/Playground/game-design-research/research_notes/Idea search/pool.md`); each fantasy source gave 1–2 new cores, then
only skins. User: "dont think about testing yet" (offer, don't push). User on the pool: it "feels like a Mario Party
minigame, not a full game"; Claude's read is in research.md (2026-11-11) and `Idea search/fix-minigame-feel.md`. Next:
sketch a between-rounds step for the skill before editing it (the skill has none yet, checked 2026-11-12).
```

### `notes/explain-concepts-plainly.md` and `notes/visual-teaching-weakness.md`
Fine as they are (2.3 KB, 1.2 KB). See Q4 and O2.

### `~/.claude/design-anti-patterns.md`
- Line 65, old: `(every co-op minigame passes all 6,` → new: `(every co-op minigame passes all 7,` (checked: lines 66-71
  list points 1-7).
- Items 23-26 overlap critic entries (bots, pooled sum, gate marked weak, unused research); the critic text cites them
  as B23-B26 instead of repeating.

### `~/.claude/CLAUDE.md` (113 lines)
- Lines 4-5, old: `Rules 8–22: concrete rules, each from a past incident or request (merged 2026-11-09 from per-project memory
  notes).` → new: `Rules 8–23: concrete rules, each from a past incident or request (8–20 merged 2026-11-09 from per-project
  memory notes; 21–23 added 2026-11-12).`
- Line 48, old: `## Concrete rules (8–22)` → new: `## Concrete rules (8–23)`.
- Rule 19 (lines 82-84), old: `by category: movement, items, menus, UI, multiplayer, juice, VFX, audio, dialogue` → new:
  `by category: movement, items, menus/UI, multiplayer, Steam lobby, juice, VFX, animation, audio, dialogue` (checked:
  folders `movement-camera`, `items-interaction`, `menus-settings`, `multiplayer-gameplay`, `steam-lobby`, `juice`,
  `vfx`, `animation-ragdoll`, `audio`, `dialogue-subtitles`, `engine-demos`; no `UI` folder).
- Rule 7's `/caveman off` is right (checked: the caveman plugin's `commands/caveman.toml` lists it).
- Rules 10, 16, 17, 20 and the new 23: see section 1 and above. Result ~127 lines (budget ~150).

Seen, out of scope: `~/.claude/skills/generate-ideas/lessons.md` is 53 KB.
