# Thesis: a new gameplay verb that works (2026-11-09, round 1)

User's ask (2026-11-09): "could you think about a new word? not used before that works?" Read as: a
gameplay verb no game has used yet, that scores well on the verbs report
(`reports/Gameplay verbs and player coupling.md`). Reading is Claude's [assumption].

Tags: [source] page found this session · [from memory] · [opinion] Claude's judgment.

## Frame (check this first)
- **What "works" means (from the report):** the verb acts on a human who picks a counter, something is
  hidden, content stays low, and in co-op it stops teammates acting as one mind. Best route in the
  report: one shared object in the hub that couples bodies + one hidden thing per player [opinion].
- **So a new verb = a new hidden thing.** The 30 verbs already hide: truth (bluff), identity (deduce,
  mimic), place (hide, seek), loyalty (betray), goals (negotiate), knowledge (signal), a word (draw),
  timing (The Mind). Not in the list: **who moved a shared object, how hard each player works, who is
  leading, who controls whom** [opinion].
- **Premise check:** "never used" can't be proven by search, only "not found". Most of these have
  real-world versions (Ouija, Find the Leader). The report also says a small rule set can't be owned
  (clones within weeks), so novelty buys the launch moment, not protection [opinion, from report].

## Candidate 1: Nudge (recommended, Claude)
**One-sentence rule:** everyone has a hand on one shared pointer; the game shows where it moves, never who pushed.
- Takes in: each player's push direction, all capped to the same strength.
- Gives out: the pointer's motion = the sum of all pushes.
- Connects to: the group's goal (spell the answer the host asks for, before a timer) and each player's
  secret letter (scores only for them if the pointer rests on it). Round end: a replay shows every
  player's push as an arrow (blame + the funny moment).
- Prior art: Ouija video games found use one ghost player who moves the pointer to talk to the living
  (WE ARE SO DEAD, Early Access 2026-08-17, 2–6 co-op [source](https://store.steampowered.com/app/4796830);
  My Friendly Soul [source](https://gugation.itch.io/my-friendly-soul)), which is the existing "signal"
  verb. Ouijably is a browser demo where everyone's mouse moves one shared pointer, with no goals
  [source](https://ably.com/blog/realtime-messaging-from-beyond-the-grave). Not found: a game with hidden
  summed pushes + private targets (4 searches; absence is not proof).
- Scene at 2 players: any push that isn't mine is yours, so nothing is hidden. **Fails at 2.**
- Scene at 3: the pointer drifts toward Q. A knows it isn't A, so B or C. Both deny. A stops pushing
  and watches the drift change while B says "I'm stopping" — does it? Mind coupling through one object.
- Scene at 6–8: each push is 1/6–1/8 of the motion; one player's secret letter barely moves it;
  individual intent drowns in the sum. Coupling per player falls [opinion].
- Dominant strategy: if the group goal pays more than a letter, everyone pushes for the word and the
  letters are ignored; if letters pay more, chaos. Needs stakes where sneaking wins more than it risks
  (report check 3) [opinion].
- Co-op gate: 1 coupled ✓ (pointer moves only by the sum) · 2 split ✓ (private letters) · 3 talk ✓
  (timer + "who's pulling?") · 4 blame: hidden during the round, shown in the replay (delayed) ·
  5 not easy: unknown · 6 not solo-able ✓ (equal caps) · 7 two-way ✓ (all push at once).
  Bots can push (physical, answers the "voice-only with bots" failure).
- Content: a word list and one board (low).
- Fantasy/logic/aesthetic: all three come from the real Ouija, where nobody knows who moves the
  pointer: séance (fantasy), hidden sum of pushes (logic), candlelit board and hands (aesthetic) [opinion].

## Candidate 2: Slack
**Rule:** the team's shared job shows only the total effort; each player secretly picks how hard to work,
and slacking fills a private reserve they keep.
- Takes in: each player's effort (hold a pump key, 0–100%). Gives out: team progress; private reserve.
  Connects to: a "check" action (inspect one teammate's effort, costs time) and the shared fail state.
- Game theory: this is an inspection game, which has a mixed equilibrium (inspect with some odds, shirk
  with some odds) [from memory]. People spotted a slacking partner with 78.6% accuracy in a lab study
  [source](https://oro.open.ac.uk/68461).
- Prior art: Work from Home (slack while hiding from an AI boss) [source](https://www.co-optimus.com/game/12544/xbox-one/work-from-home.html);
  Among Us impostors fake tasks [from memory]. Not found: teammates catching a slacking teammate.
- Scene at 2: total minus mine = yours, so nothing hidden. Fails at 2. At 3+: you know the others' sum, not who.
- Weakness: everyone does the same job side by side; the coupling is only through the total
  (design-anti-patterns 24, co-location) [opinion]. Effort has one number; a nudge carries a direction,
  which says what the player wants.

## Candidate 3: Copy (secret leader)
**Rule:** one secret player leads the moves, everyone copies, and a seeker must find the leader.
- Takes in: a small set of poses/emotes. Gives out: everyone's pose; the seeker's guesses (budget below
  "check everyone", report check 2). Connects to: the seeker's view (can't watch everyone at once).
- Prior art: an old camp game, Find the Leader / "who's changing the movement"
  [source](https://resources.trinitycollege.com/hubfs/Trinity%20Drama%20Games%20Resources/Drama%20games%20-%20Whos%20changing%20the%20movement%3F.pdf?hsLang=en);
  Secret Shuffle (phone party game: the faker hears no music and fakes the dance; 5 reviews, 2023)
  [source](https://store.steampowered.com/app/2431820). Not found as an online video game.
- Scene at 3 (seeker, leader, 1 copier): trivial. Needs ~5+. At 8: works like the camp game.
- It is versus (copiers vs a human seeker). With an AI seeker, the counter is AI and content need returns.

## Candidate 4: Puppet (dropped)
**Rule:** your controls move someone else's character, and nobody is told whose.
- With voice, "whoever drives me, go left" solves the mapping in seconds, every round. To stay hidden it
  needs a traitor, which makes it the existing betray/deduce verbs. Confusion risk like DRS Switchboard
  ("still doesn't understand"). Prior art: none exact; Shuffle and Seek scrambles controls as a sabotage
  [source](https://cogconnected.com/?p=392296).

## Recommendation (Claude)
Nudge. It is the report's formula in one rule: one shared object (body coupling) + one hidden thing per
player (mind coupling), low content, physical so bots can play. Known limits: needs 3+ players; the
sum drowns individuals at 6–8; the reveal is delayed to the replay.
Smallest test: one board, one pointer, 3 players, private letters, 60 s round, replay of pushes.
Kill if: at 3 players nobody asks "who's pulling?" in the first round, or players ignore their letters.

## Synthesis after critic round 1 (2026-11-09)
Frame failed; not rerun on this frame. All four candidates hide who did an input, already the report's
Sabotage row; in pure co-op nobody gains from hiding it, so voice reveals it; the summed push repeats
gameplay-anti-patterns #12 and DRS The Tilt (built, not playtested); hiding the pusher breaks gate 4.
Taken to the user: look for a new action for a proven pair (hide/seek, bluff/call, sabotage/accuse),
as MECCHA (paint), Prop Hunt (become a prop) and Liar's Bar (revolver) did. Log: `research.md`.
