# Design anti-patterns: how Claude designs badly

Check every design sketch (mechanic, rule, flow, item, path) against this list before showing it.
It was pulled from the user's corrections and logs across projects.
Sources: RB = `~/Playground/red-button-experiment/CLAUDE.md`, RBD = `.../red-button-experiment/docs/design-dialectic.md`, DM = `~/Playground/mustache-madness/.claude/skills/design-idea/references/design_method.md`, DD = `.../mustache-madness/.claude/skills/design-dialogue/SKILL.md`, MM = `.../mustache-madness/CLAUDE.md`, DP = `~/Playground/dungeon-pets/POSTMORTEM.md`, P = `~/.claude/CLAUDE.md` rules 1–7, DRS = Deathly Reality Show v1.

## A. How Claude reasons badly
1. **The newest idea becomes the hub.** Claude stretches the latest idea into variants of itself.
   Fix: list the rules that govern the design first (newest first), and name the rule each part meets.
   A new idea starts from a different action (press, don't press, break, sell, leave), not the same action tweaked. (RB, RBD)
2. **Defending idea #1.** Everything already in the chat makes turning back costly, so Claude sticks to its first idea.
   Fix: at least 3 really different proposals, and drop one the moment a fact disproves it.
   Redo it in an isolated subagent, or ask the user to `/rewind`. (MM, DM)
3. **Length as evidence.** A long, confident rejection or justification sways everything after it.
   Fix: a one-line verdict, open to change. (DM)
4. **Detail before the problem underneath.** Bottom-up detail buries the check on the base idea.
   Fix: check the base idea first, and stop there if it's wrong. (DM)
5. **An unproven premise.** Designing on a guess.
   Fix: a checklist of assumptions; label checked vs assumed. (MM, P)
6. **Deciding for the user.** Making up pillars, deciding while the user is away, tagging Claude's pick "(user)".
   Fix: draft pillars for the user to confirm; tag picks "(Claude)" unless the user's own words chose them. (DM, MM, RBD round 2)
7. **Asking in the middle of designing.**
   Fix: recommend inline, and put open choices in the questions file.
   One line asking what an ambiguous request meant, with Claude's pick, is not this. (RB, P)
8. **A question taken as a pick.** "What about X" is the user thinking out loud.
   Fix: make the case against it first. (DD)
9. **Arguing with a playtest.**
   Fix: the playtest wins; ask what felt wrong. (DD, RB)
10. **References from memory.**
    Fix: search and cite; mark claims from memory. (DD)
11. **Vague amounts:** "high", "some", "more".
    Fix: a named variable with a range and a formula, tested at max, at 0, removed, and over a long middle stretch.
    (design-idea SPECIFY; RBD round 2: unchecked scaling math made stages last seconds)
12. **Undefined terms.**
    Fix: say what a term takes in, gives out and connects to before it carries reasoning. (P)

## B. What bad designs look like
13. **Layers instead of a core.** Strategy added as layers; content before the system. (DP, RB)
14. **Individuals instead of rules.** Caring for each unit instead of rules per type. (DP)
15. **A shallow choice, or fake agency.** An option with one obvious answer, or a verb that takes away commitment. (DM)
16. **Mechanics that are hidden or explain themselves.** You can't see it happen, or the name gives the answer away and kills discovery (Mop, Tape). (DM, RBD round 1)
17. **Exploits.** Co-op one player can solve alone, a free score machine, a player's own action winning alone. (RBD round 2, DP)
18. **A fix that breaks its neighbours.** Check every fix against every system it touches ("seat occupied" broke Hunt, Sequence and Maze). (RBD round 3)
19. **Rules not specified enough.** Nothing on network sync, who gets the blame, edge cases. (RBD rounds 2–3)
20. **Blame from luck.** Blame with no player's action behind it. (RBD round 2)
21. **Solved by the second run.** Variety that turns into a lookup table. (RBD round 1)
22. **Scale ignored.** 2 vs 8 players; early vs late numbers. (RBD round 1)
23. **Bots taken as fun.** Bot runs check the rules, never the fun.
    A bot clearing it fast is a warning that it's *too easy*, never a pass. (DP; DRS: bots cleared game 3 in 12 s, and it was ignored)
24. **Standing in places counted as co-op.** Two people standing in two places, or everyone doing the same job side by side, is playing in parallel, not cooperating. (DRS: plates and levers; the user found them too simple, too easy, and with no cooperation)
25. **A problem with the base idea set aside.** Fixing a critic's number findings and moving its main finding to a todo.
    A severe problem with the base idea gets fixed or taken to the user, never set aside. (DRS)
26. **Research copied in, not used.** Pattern docs sitting in the project without each feature checked against them. (DRS: gameplay-anti-patterns #12 would have rejected both minigames)

## C. Patterns that work
- **Essence test:** no purpose you can state → cut it; the same purpose as another → merge them; connects to nothing → drop it. (DM)
- **One mechanism that solves several open items** beats several features. (DM, DD)
- **Play one scene** per option: who stands where, what the player sees. (design-idea)
- **A critic agent each round** (proposal, isolated critic, merge); it caught ~30 problems in 3 rounds on Red Button. (RBD, DM)
- **Co-op check:** every co-op minigame passes all 7 points (from gameplay-anti-patterns #12 and its formula).
  1. Coupled: my action fails without yours.
  2. Split: information or roles split by position, and anyone can step in.
  3. Talk: time pressure that makes people speak.
  4. Blame: one visible person's failure, shown physically.
  5. Not easy: new players, with the fewest players, can lose, and it gets harder over time.
  6. Not solo: one player, or one fast carrier, can't clear it.
  7. Two-way: both ends of every coupling decide at the same moment.
     If one end only obeys or stands still, it's a pressure plate, not co-op; one player who knows everything is a quarterback.
  Also check the lone survivor (can they get stuck?) and whether dying on purpose makes it easier.
  (DRS; point 7 came from the critic, round 1)
