# Discovery: patterns and anti-patterns

How games built on "nobody tells you, you figure it out" stay clear and fun instead of confusing
or boring. Written 2026-11-06 after the user asked: "there has to be a clear goal.. if no one
knows what to do then it is not fun no? my game is about that.. not knowing what to do.. and figure
out.. how this games achieve that without being boring and confusing?" Companion to the Fantasy in
`docs/core-design.md`.

Each entry: **Rule** (the pattern, with source) · **Us** (where it shows up here). Tags:
*[source]* = backed by a linked source; *[read]* = checked in our docs this session;
*[opinion]* = design judgment, not checked.

## Terms
- **Discoverability** (Don Norman, UX): how easily a person can tell *which actions are possible*
  and *what state the thing is in*. It is a property of the interface, and good design makes it
  high ([Zivtech on Norman's principles](https://www.zivtech.com/blog/ux-principles-constraints-discoverability-feedback-and-more);
  [UX Psychology](https://uxpsychology.substack.com/p/unlocking-features-the-importance)). *[source]*
- **Discovery**: the player's act of finding out something the game did not say. This is what
  the fantasy means. *[opinion]*
- **Knowledge gate**: progress blocked by understanding, not by an item or skill. Outer Wilds is
  the reference: places are reachable at any time if you know how
  ([Thinky Games: metroidbrainias](https://thinkygames.com/lists/best-metroidbrainia-games/)). *[source]*
- **Information gap** (Loewenstein): curiosity comes from a gap the player notices between what
  they know and what they want to know; it must be visible, challenging and look solvable, and a
  gap that is too large kills curiosity instead of raising it
  ([Outbreak, DiGRA](https://dl.digra.org/index.php/dl/article/download/923/923/920);
  [Radboud thesis](https://theses.ubn.ru.nl/server/api/core/bitstreams/8ce524af-48e0-4998-a1f6-0e2cdb2df020/content)). *[source]*
- **Moon logic**: a solution that follows no logic the world showed
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/MoonLogic)). *[source]*

## Is "discoverability" the right word?
Half right. In UX, discoverability means the opposite of hiding: the player can see *what they can
do*. Our fantasy is **discovery**: the crew finds out *what it does*. The two fit together, and
the split is the answer to "how is not-knowing still fun":
- **Verbs and goal: high discoverability.** The crew can always see the goal (escape: 1B), what
  can be touched (button, items, walls) and *that* something changed.
- **Effects and secrets: discovery.** What a change does, what an item is for, where the other
  exits are: found by trying.

Recommendation: call the fantasy **Discovery** ("find out by trying") and keep "discoverability"
for the UX rule that the verbs and the goal are always obvious. Parked in `docs/questions.md`.
*[opinion]*

## The one-line diagnosis
Fun is learning (Koster, after Crawford: "fun is the emotional response to learning"), and a game
turns boring once there is nothing left to learn and confusing when the learning has no handle
([Koster, Theory of Fun 10 years later](https://www.raphkoster.com/wp-content/uploads/2026/07/Theory-of-Fun-10-Years-Later.pdf);
[Engadget on the keynote](https://www.engadget.com/2012-10-10-gdc-online-2012-raph-kosters-keynote-on-a-theory-of-fun-10-ye.html)).
Discovery games survive by **hiding the method, never the goal or the verbs**, and by making every
try answer fast. Confusion = no goal, no verb, or no answer. Boredom = only one thing to try and it
always does the same. *[source + opinion]*

## Patterns (do)

### 1. Clear goal, hidden method
- **Rule:** Untitled Goose Game gives a to-do list ("get the gardener wet") and never says how; the
  list exists "to nudge people towards larger interactions", while messing around is fun on its
  own ([Red Bull interview](https://www.redbull.com/us-en/untitled-goose-game-interview);
  [Game Developer Q&A](https://gamedeveloper.com/design/behind-the-honk-an-i-untitled-goose-game-i-q-a)).
  Hitman names the target and hides dozens of ways to reach it. *[source]*
- **Us:** the goal is clear in words ("press it 1B times to escape") but `docs/questions.md` notes
  the goal and stage are **shown nowhere** in the room, only the count. *[read]* A crew that can't
  see "how far to go" has lost the one fixed thing. Recommendation stays: goal under the count.

### 2. Always one obvious thing to try
- **Rule:** the gap must look solvable (Loewenstein, Terms). The Stanley Parable's first moment
  is two doors and a narrator saying which one to take: one clear choice, then disobey or obey
  ([Kill Screen](https://killscreen.com/inside-stanley-parable-game-no-one-can-describe)). *[source]*
- **Us:** the button is the always-available verb: when lost, press. This is the game's best
  defence against confusion. *[opinion]*

### 3. Every try answers, fast and visibly
- **Rule:** a secret feels clever when the player noticed a cue and investigated; found by luck or
  brute force it feels arbitrary ([Bugnet: secrets](https://bugnet.io/blog/how-to-design-secrets-and-hidden-areas)).
  The worst failure is opaque, expensive and repetitive; arbitrary failure leaves nothing to learn
  ([Bugnet: failure](https://bugnet.io/blog/designing-failure-how-to-make-losing-fun);
  [Wayline](https://www.wayline.io/blog/fail-forward-interview-cipher-meaningful-loss)). Adventure
  players complain most when wrong actions return "just generic answers"
  ([Legend of Skye thread](https://www.adventuregamestudio.co.uk/forums/completed-game-announcements/the-legend-of-skye/20)). *[source]*
- **Us:** "signal *that* it changed" covers changes. The gap is **wrong tries**: a wrong use of an
  item should give a distinct, funny answer, not nothing. *[opinion]*

### 4. Show the odd thing before it means anything (the hook)
- **Rule:** Outer Wilds was built on curiosity alone, with no upgrades or collectibles; its design
  started from "reading about a rumoured distant place and then being able to go explore it"
  ([GamingBolt interview](https://gamingbolt.com/outer-wilds-interview-into-the-unknown);
  [Edge via PressReader](https://www.pressreader.com/australia/edge/20190104/281505047327666)).
  Hooks are rumours: something seen, not explained. *[source]*
- **Us:** flashlight writing from "past crews" gives two hand-made route hints per run, the first
  always for a route whose item the shop offers (`docs/gameplay-design.md`). *[read]* That is the
  right shape; check every route has a hook a crew can find *without* the flashlight. *[opinion]*

### 5. Keep a record of what was learned
- **Rule:** Outer Wilds' ship log tracks found clues as a web of rumours instead of quest markers,
  split into "curiosity webs" solvable in any order
  ([SFRA Review](https://sfrareview.org/2020/12/13/50-4-32/)). Knowledge is the progress, so the
  game shows it. *[source]*
- **Us:** the count shows pressing progress; nothing shows "what we figured out". Ending plinths
  light in the exit room (`docs/gameplay-design.md`) *[read]*; the narrator's memory (pillar 4)
  could carry the rest ("Last time you hit it with a fish."). *[opinion]*

### 6. Teach with the thing itself, not words
- **Rule:** The Witness never explains its rules in words; puzzles teach them, aiming for
  "miniature epiphanies over and over again"; one solved panel carries "a paragraph or two of
  information" ([Game Informer](https://gameinformer.com/games/the_witness/b/playstation4/archive/2013/06/14/five-features-that-define-the-game.aspx);
  [Gamereactor](https://www.gamereactor.eu/shared-epiphany-jonathan-blow-reflects-on-the-witness)). *[source]*
- **Us:** items show their use when handled (squeak, swing, cannon mouth opens) is the open
  recommendation in `docs/questions.md`. *[read]*

### 7. Build the twist on something players think they know
- **Rule:** the strongest gates are *application* gates (a new use for a known mechanic), stronger
  than *information* gates (a fact to find); build the key on something players think they already
  understand ([Öoo game log](https://12oi3.github.io/article/2026-03-04-Öoo-GameLog%236/)). *[source]*
- **Us:** the button is the known mechanic, and moods change what it wants. A mystery like "don't
  press" is an application gate on the most familiar verb. *[opinion]*

### 8. Layer secrets: most players see layer one
- **Rule:** Animal Well is designed in three layers; the third expects guides and community, and
  one puzzle needs ~50 players' pieces to solve ([Kotaku](https://kotaku.com/animal-well-guide-tips-layers-explained-1851532515);
  [Push Square](https://pushsquare.com/news/2024/05/single-player-animal-well-has-a-secret-puzzle-that-requires-50-players-to-solve)).
  Hitman lets players choose how much the Opportunities system tells them, after user research
  found the learning curve "way too steep" ([GDC Vault](https://gdcvault.com/play/1023849/Level-Design-in-HITMAN-Guiding);
  [PC Gamer](https://pcgamer.com/hitman-the-complete-first-season-review)). *[source]*
- **Us:** matches "a stream spoils only a fraction" (Fantasy). Layer one: moods and items any crew
  meets. Layer two: routes, hinted. Layer three: rare hand-made mysteries meant for the community.
  *[opinion]*

### 9. Make dying (or losing) the teacher, and make it a story
- **Rule:** Lethal Company has no tutorial; "be prepared to die, a lot"; each monster's gimmick is
  learnt at the first, frightening encounter, then recorded by scanning into a bestiary
  ([Destructoid](https://destructoid.com/?p=433008);
  [Chantilly News](https://chantillynews.org/14045/multimedia/lethal-company-sets-a-higher-standard-for-early-access-games/)). *[source]*
- **Us:** pillar 3, fun to lose: a loss unlocks something and leaves a hint. A friendslop crew
  learns by one friend getting caught in front of the others. *[read + opinion]*

## Anti-patterns (don't)

### 1. Don't hide the goal or the verbs
- **Rule:** Norman: people must be able to tell what actions are possible and the current state
  (Terms). *[source]*
- **Us:** goal not shown in the room (pattern 1). Any item whose verb isn't visible when held.

### 2. Don't make the key too obscure: moon logic
- **Rule:** an obscure key becomes "a permanent wall"
  ([Öoo game log](https://12oi3.github.io/article/2026-03-04-Öoo-GameLog%236/)); moon logic is a
  solution from logic the world never showed ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/MoonLogic)).
  Absurd solutions can read as humour in light games, but only if reachable by reasoning
  ([intfiction](https://intfiction.org/t/what-is-moon-logic/79054)). *[source]*
- **Us:** a comedy game is tempted to make solutions random because random is funny. Every route
  needs a chain of cues the room showed first. *[opinion]*

### 3. Don't make the key too obvious
- **Rule:** an obvious key gets used by accident "before it ever functions as a gate"
  ([Öoo game log](https://12oi3.github.io/article/2026-03-04-Öoo-GameLog%236/)). *[source]*
- **Us:** a mystery that 4 people mashing everything trigger by chance is never *discovered*, just
  stumbled into. Mass button-mashing crews will hit anything one press away. *[opinion]*

### 4. Don't answer a wrong try with nothing
- **Rule:** generic or silent replies to wrong actions are the top complaint in obscure adventure
  games (pattern 3). *[source]*

### 5. Don't run out of things to learn
- **Rule:** boredom sets in once the patterns are mastered; games stay fun with "enough variables to
  keep the new data flowing" (Koster, via [Bumbling Through Dungeons](https://bumblingthroughdungeons.com/theory-fun-game-design-raph-koster/)). *[source]*
- **Us:** the critic already found mood colours turning into "a lookup table by run 2"
  (`docs/design-dialectic.md`). *[read]* Once known, a mystery must turn into a tool or a choice,
  or it is used up.

### 6. Don't hand-hold so much the discovery is gone
- **Rule:** Hitman reviewers called full hints "self-defeating" and "overbearing"; veterans disliked
  them ([PC Gamer](https://pcgamer.com/hitman-the-complete-first-season-review)). *[source]*
- **Us:** a hint says *where to look*, never *what to do* (Fantasy: *that*, not *what*). *[opinion]*

### 7. Don't confuse curiosity with exploration
- **Rule:** practitioners often treat curiosity as just exploring space; the research separates
  them ([White Rose framework study](https://eprints.whiterose.ac.uk/210197/1/Exploring_Curiosity_in_Games_A_Framework_and_Questionnaire_Study_of_Player_Perspectives.pdf)). *[source]*
- **Us:** the room is small; our curiosity is about *rules and objects*, not places. Adding rooms
  doesn't add mystery. *[opinion]*

## Checklist for any new mystery, item or rule
1. **Goal:** can the crew still see what they are trying to reach?
2. **Verb:** is the thing you can do with it visible the moment you see or hold it?
3. **Hook:** is there something odd the crew notices *before* they understand it?
4. **Answer:** does every try, right or wrong, get a fast, visible, distinct reply?
5. **Chain:** can a crew reason its way there from cues the room showed (no moon logic)?
6. **Not by accident:** would mashing everything trigger it without anyone noticing why?
7. **Record:** once found, does the game show it was found (plinth, narrator memory)?
8. **Afterlife:** once known, does it become a tool or a choice, or is it used up?
9. **Fantasy:** does any hint say *where to look*, never *what to do*?
10. **Crew:** is someone caught or blamed when they get it wrong, so the mistake is a story?

## Gaps in this research
- No primary talk text: the Outer Wilds GDC 2020 talk, Hitman's GDC talk and Randy Smith's "Helping
  Your Players Feel Smart" (GDC 2009) were found only as titles or summaries.
- Several sources are blogs and forums (Bugnet, Öoo log, intfiction); treat as practitioner opinion.
- Nothing found on discovery in *co-op* specifically, beyond Animal Well's community puzzle and
  Lethal Company; how a crew shares and argues over a guess is our own design ground.
