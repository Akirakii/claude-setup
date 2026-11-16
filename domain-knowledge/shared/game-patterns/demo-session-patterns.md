# The demo and the session: patterns and anti-patterns

Researched 2026-11-06 for the audit (`docs/audit.md`): what a Steam Next Fest demo should hold and
how it should end, and how a co-op session handles joining, leaving and the first run. The
roadmap ships a public demo in a month (`docs/roadmap.md`). Tags: *[source]*, *[read]*, *[opinion]*.

## Sources
- presskit.gg, "How to build a game demo" ([guide](https://presskit.gg/field-guides/how-to-build-game-demo)): length,
  endings, the end screen. One practitioner guide; its numbers are anecdotal by its own account.
- GMTK, "How to make a great Steam Next Fest demo" ([post](https://gmtk.substack.com/p/how-to-make-a-great-steam-next-fest)) and
  Unity's Next Fest tips ([blog](https://unity.com/blog/steam-next-fest-developer-tips-unity)): found, read only as summaries.
- Timing and wishlists: a 182-developer survey summary (pre-fest wishlists vs fest wishlists,
  Spearman r 0.825) via [howtomarketagame.com](https://howtomarketagame.com/?p=4587) and the
  [Next Fest guide](https://presskit.gg/field-guides/steam-next-fest-guide). *[source, secondary]*
- Drop-in co-op: [Co-Optimus terminology guide](https://co-optimus.com/editorial/1081/page/3/the-co-op-terminology-guide-2012-edition.html);
  friendslop onboarding: [AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025),
  [Creative Bloq](https://www.creativebloq.com/3d/video-game-design/what-is-friendslop-and-why-it-it-taking-over-gaming-in-2026).

## Patterns (do) and the game
1. **15-30 minutes of content.** Under 10 feels like "barely started"; over 45 is rarely finished
   on stream ([presskit.gg](https://presskit.gg/field-guides/how-to-build-game-demo)). *[source]*
   **Us:** a run is ~14 min for 4, ~23 for 2 (guess, `docs/gameplay-design.md`); losing and going
   again is the loop, so a session of 2 runs sits in the band. *[read + opinion]* Pass, to measure.
2. **End at peak engagement, not a neat stop;** a door onto something unexplored converts better
   than a complete experience (same source, "sometimes 2-3x", anecdotal). *[source]* **Us:** the
   exit room's blank plinths say more endings exist, never which (`docs/gameplay-design.md`) *[read]*:
   that is the open door. Pass.
3. **The end screen thanks, asks for the wishlist and points to feedback, at once** ("don't let it
   dissipate by giving them a cool-down period"). *[source]* **Us:** nothing asked. **Fixed:**
   `Tuning.DEMO` puts thanks, WISHLIST ON STEAM (Steam overlay) and a feedback link on the title
   screen players land on after leaving; in the room there is still no text (user, 2026-11-03).
4. **Include the core loop polished, the best set piece, the most unique mechanic; hold back
   tutorials over ~3 minutes, unfinished systems, anything buggy** ("Players won't file a report.
   They'll close the demo"). *[source]* **Us:** the roadmap already says the demo is the core room
   and "a feature enters the demo only after a playtest earns it" *[read]*. Pass (the playtest picks).
5. **Release the demo weeks to months before the fest;** pre-fest wishlists predict fest wishlists. *[source]*
   **Us:** the roadmap plans the demo ~3 weeks before Next Fest *[read]*; sources favour earlier.
   Parked: a roadmap choice for the user.
6. **Drop-in, drop-out:** a late friend fills an empty slot mid-session without losing progress
   ([Co-Optimus](https://co-optimus.com/editorial/1081/page/3/the-co-op-terminology-guide-2012-edition.html)). *[source]*
   **Us:** anyone joins a running run and shares the wallet; the lobby pools unlocks; a leaver's
   turn in an exam is skipped or passed on (audit 2026-11-06). *[read]* Pass.
7. **Almost no onboarding; learning happens mid-session, over voice**
   ([Creative Bloq](https://www.creativebloq.com/3d/video-game-design/what-is-friendslop-and-why-it-it-taking-over-gaming-in-2026)). *[source]*
   **Us:** the silent first stage and the Fantasy (find out by trying). *[read]* Pass.

## Anti-patterns (don't)
1. **Don't ship testing settings in the public build.** *[opinion]* **Us:** free shop, shop at
   start, Steam test app 480. Parked: release checklist in `docs/questions.md`.
2. **Don't let one player's leaving end everyone's run.** *[opinion, from 6]* **Us:** a host
   leaving ends it (player-hosted); a guest leaving never does (Sequence, Maze and the trap all
   pass on). Host migration: parked (tech risk, a month to ship).
3. **Don't make the restart a menu trip.** *[opinion]* **Us:** the host presses the button to go
   again; guests' presses thud (gap review). Pass.

## Checklist for the demo build
1. Does a fresh crew reach a "what was that?" moment inside the first 5 minutes? (roadmap test)
2. Does the session end on an open door (plinths), with the ask on the next screen?
3. Are the testing flags off and the links filled?
4. Can a friend join a run already going, and can anyone leave without stalling it?

## Gaps in this research
- Demo length and ending advice is practitioner opinion; no controlled data was found.
- No developer postmortem on first-session onboarding in friendslop games was found.
- Host migration patterns were not researched.
