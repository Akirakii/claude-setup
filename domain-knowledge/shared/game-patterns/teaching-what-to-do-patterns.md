# Teaching the player what to do

Patterns for a game whose players say "I don't understand what to do".
Tags: [source] = said by the linked source; [read] = Claude's reading of it; [memory] = Claude's memory, not checked; [opinion] = Claude's own.

## Patterns
1. **An evidence journal that crosses out what can't match** [source: Phasmophobia: ticking evidence removes
   incompatible ghosts; later the journal synced evidence across the lobby and highlighted a ghost's evidence when
   selected — [NME](https://www.nme.com/news/phasmophobia-devs-share-improvements-to-the-journal-system-3158844),
   [v0.19 patch](https://patched.gg/games/phasmophobia/phasmophobia-v01900-quality-of-life-part-2)]. [read] Phasmophobia's journal is filled by hand; behaviours it can't hold stay the
   players' skill.
2. **Teach at the moment of need; hints vanish once done** [source: [Roblox onboarding](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md)
   (contextual, triggered by play; text pop-ups get skipped), [Wayline](https://www.wayline.io/blog/ux-game-tutorials-player-retention)].
3. **Do, don't read** [source: [GDevelop: text-based tutorials don't work](https://gdevelop.io/blog/improve-game-tutorials)];
   core loop learned in the first 60–90 s [source: Roblox doc above].
4. **A guided mock round** for social deduction newcomers [source: [Critical Play: Among Us](https://mechanicsofmagic.com/2022/04/08/critical-play-among-us-12/):
   a critic who struggled suggests a mock game with guided text and tasks].
5. **Anti-pattern: a task list pulls attention off the social game** [source: Among Us players "playing Task
   Simulator", [crewmate mistakes](https://jonathanliu.pages.dev/blog/common-crewmate-mistakes-in-among-us)].
   [opinion] So a "do this now" line must point at people (look at Bo, give Bo), not at chores.
6. **Centre of screen clear except crosshair, interaction prompts and critical alerts** [source:
   [gamedev.net, 7 UX lessons](https://ehe.gamedev.net/articles/game-design/ux-for-games/7-ux-lessons-from-the-trenches-r4969),
   [HUD patterns](https://cdn.jsdelivr.net/npm/@hegemonart/get-design-done@1.60.4/reference/domains/gaming-patterns.md)];
   colour plus a word or icon, never colour alone [source: same].
7. **The user's own verdicts on text** [source: critic memory]: an earlier game needed \"50% less text\"; two rounds of better wording
   didn't save a game with stacked hidden rules ("if the one-sentence rule needs a second sentence, change the game").
   [opinion] So readability work here must replace text, not add it, and say plainly if the game itself is too
   much to learn.
