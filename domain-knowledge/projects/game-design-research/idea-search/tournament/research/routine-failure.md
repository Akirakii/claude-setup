# Why co-op games settle into a routine, and what stops it (research, 2026-11-10)

Question from the tournament: almost all of 126 ideas failed "round 50 still plays differently from
round 2". The raters said physical teamwork ideas settle into one plan ("you say go, I release"), and
then players stop reacting to each other. Unchecked guess: in pure co-op nobody pushes against the
plan. This file collects what the web says about why games settle and what stops it with little
hand-made content.

Tags: **[source]** = I read the page or the text itself. **[snippet]** = only a search result or
an abstract seen through a search. **[opinion]** = my own inference from the sources, not a finding.

Words used below:
- **Plan / convention:** the habit a team settles on ("you say go, I release"). In research on
  coordination this is called a convention: an arbitrary way to coordinate that sticks because
  everyone expects everyone else to keep using it.
- **Input randomness:** chance that happens *before* players decide (a shuffled deal, a new layout).
  **Output randomness:** chance that happens *after* players commit (a dice roll to hit, a physics
  bounce). Definitions from [Skeleton Code Machine](https://www.skeletoncodemachine.com/p/input-output-randomness-part-1) [source] and
  [Game Developer, "Sources of uncertainty"](https://www.gamedeveloper.com/design/sources-of-uncertainty) [source]. I did not find these two terms in
  *Characteristics of Games* itself; the book has the same idea (see cause 4).

---

## Causes of settling into a routine

1. **Once the best plan is known, the game is "solved" and stops being a game.** Elias, Garfield
   & Gutschera: some games have rules of thumb "of sufficient quality that, once known, players can
   play perfectly (the game is 'solved')"; for Nim it is "impossible to play an interesting game
   once both players know it". Rules of thumb must not be all easy to find, "if they are all easy,
   eventually they will all be discovered and the game will be exhausted". Solved parts of chess
   "become busywork". *Characteristics of Games* (MIT Press 2012), pp. 34–35 and 157.
   [Publisher page](https://penguinrandomhouse.com/books/655769/characteristics-of-games-by-george-skaff-elias-richard-garfield-and-k-robert-gutschera-foreword-by-eric-zimmerman-and-peter-whitley) [source: read the book text]

2. **Players actively push the game toward a routine.** Koster: you play a game "until you master
   the pattern ... The game becomes boring." Players "will try to make the gameplay as predictable
   as possible. Which then means it becomes boring". He names it: "routine".
   [Koster, *A Theory of Fun* slides](https://www.raphkoster.com/gaming/atof/theoryoffun.pdf) [source]

3. **Fixed content gets memorized, and memorizing kills cooperation.** Booth (Left 4 Dead, GDC
   2009): hand-placed scripts "Kills replayability ... Players learn all script locations quickly"
   and "Kills cooperation ... Players expect everyone to have memorized all encounters ... Becomes a
   race". [Booth, "Replayable Cooperative Game Design: Left 4 Dead"](https://cdn.fastly.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf) [source];
   same point in [Booth, "The AI Systems of Left 4 Dead"](https://www.readkong.com/page/the-ai-systems-of-left-4-dead-michael-booth-valve-9664541) [source]. Juul: games of
   *progression* (a fixed series of challenges) have "very low" replayability; games of *emergence*
   (few rules that combine) "tend to be replayable".
   [Juul, "The Open and the Closed"](https://jesperjuul.net/text/openandtheclosed.html) [source]

4. **Chance that comes after the decision does not stop solving.** Elias et al. invent "rando-Nim":
   play Nim, then roll a die to pick the winner. "Its strategy and its heuristics are the same as
   those of Nim." Randomness only fights stagnation when it creates new situations to decide about
   ("Chess960 ... using randomness to solve this problem of stagnation"; randomized dungeons give
   NetHack its replay). The book lists physics ("ball bounces") as one source of chance.
   *Characteristics of Games* pp. 35, 145, 147–148 [source]. → **[opinion]** Physics wobble in a
   carry or a catch is mostly output randomness: it changes *whether* the plan works, not *which*
   plan is best. That fits the raters' reading of the tournament's physical ideas.

5. **One-sided games lack the biggest source of surprise: an opponent.** Elias et al.: "a human
   opponent provides much uncertainty"; without one, "uncertainty needs to come from somewhere
   else", so "single-player games are more prone to exhaustion". Co-op games "are simply
   single-sided games with more than one player", "An opponent provides so much, in terms of
   uncertainty of outcome and repeat play value", and single-sided games are prone to "limited
   replayability". *Characteristics of Games* pp. 26–27, 68–70 [source]. Koster: "Most
   long-lasting games in the past have been competitive, because they lead to an endless supply of
   similar yet subtly varied puzzles." [Koster slides](https://www.raphkoster.com/gaming/atof/theoryoffun.pdf) [source]

6. **A team's habit is stable because nobody gains by breaking it.** Lewis: a convention is
   "self-perpetuating", each person has no reason to deviate while the others conform, and a habit
   "gradually becomes more salient through precedent, until eventually it becomes a convention".
   [Stanford Encyclopedia, "Convention"](https://plato.stanford.edu/entries/convention/) [source]. Lab evidence: pairs who repeat the
   same task reach "idiosyncratic but efficient and stable solutions", and their messages shrink to
   short labels. [Hawkins, Frank & Goodman 2020](https://arxiv.org/abs/1912.07199) [source: abstract]. Teams with a shared picture of the
   task switch from explicit to *implicit* coordination and talk less.
   [Entin & Serfaty 1999, *Human Factors*](https://api.crossref.org/works/10.1518%2F001872099779591196) [snippet: abstract only]. → This is the "players stop
   reacting to each other" symptom: once the habit is shared, there is nothing left to say.

7. **Pure co-op timing games get solved by a counting habit.** *The Mind* (play cards in rising
   order, no talking) is pure co-op timing, close to "you say go, I release". If everyone counts
   seconds, "there is one strategy that 'solves' the game", which the author calls "a bit boring".
   [Ross, "The Mind analysis"](https://magnusross.github.io/posts/mind-game-analysis) [source]. A reviewer finds the counting version "not that enjoyable doing
   it time after time after time"; another "would never choose to play it again" after finding it.
   [Opinionated Gamers review + comments](https://opinionatedgamers.com/2018/03/13/the-mind-game-review-by-chris-wray/) [source]. The rulebook has to forbid it ("There is no counting").

8. **One plan → one planner (the quarterback).** When a co-op game can be solved, one player
   solves it for everyone: "they're really solo problem-solving games that are masquerading as
   games for multiple players". [The Alexandrian](https://thealexandrian.net/wordpress/35063/board-games/thought-of-the-day-quarterbacking-in-co-op-games) [source]. In co-op "there are no
   opponents to object when one player directs another". *Characteristics of Games* p. 69 [source].
   Gary: "One dominant player at the table figures out the optimal play and starts directing
   everyone else." [Justin Gary](https://justingarydesign.substack.com/p/the-quarterback-problem) [source: free part only]

9. **A dominant strategy can cut the players apart.** In Lethal-Company-style games "the most
   efficient way to play is to split up almost immediately", because more ground means more loot.
   [Millman, GDC 2026 game review of *Peak*](https://media.gdcvault.com/gdc2026/GNR/Papers/Zac+Millman+-+GDCReview_2026_Peak_Millman.pdf) [source: student review paper]. Overcooked
   playtesters "quickly caught onto how to manage their characters efficiently"; the team answered
   with tasks that take time and with layout disruptions.
   [Wikipedia, Overcooked, summarizing Duncan's 2016 Gamasutra deep dive](https://en.wikipedia.org/wiki/Overcooked) [source: secondary]

10. **A threat with a fixed rule is learnable too.** Even "the ghosts in Pac-Man can provide a lot
    of uncertainty (although good players will eventually learn the patterns involved if there's no
    randomness in the system — in a sense, Pac-Man changes from a game to a puzzle as you get better
    at it)". *Characteristics of Games* p. 27 [source]. → **[opinion]** This applies to the bull
    ("charges the nearest player it can see"): if the team can always control who is nearest, the
    bull becomes a rule to exploit ("one bait, the rest work"), and the round settles again.

---

## Known fixes

Content cost = how much hand-made material it needs for one developer: **low** (one rule or
generator, a list of ≤ 20 items), **medium** (a kit of parts, a set of authored behaviours),
**high** (hand-built levels, scripts, ongoing updates).

| Fix | What it does to the routine | Evidence | Content |
|---|---|---|---|
| **Input randomness** (new deal, layout or goal shown at round start) | changes *which* plan is best each round, so no single habit wins | Elias et al. pp. 147–148 (Chess960, NetHack) [source]; Hanabi: random deal plus hidden cards keeps convention-heavy play going ([Hanabi convention docs](https://hanabi.github.io/summary)) [snippet]; Spaceteam's instruction words are all randomly generated ([Spaceteam](https://en.wikipedia.org/wiki/Spaceteam)) [snippet] | **low** (a generator + short lists) |
| **AI director / "structured unpredictability"** | changes *when* and *where* pressure comes, reacting to how stressed the team is; "Same scenario, often the same map, yet different and compelling experience each round" | Booth GDC 2009 slides [source]: "Collections of interesting possibilities selected at runtime", "Simple algorithms can generate compelling pacing schedules", director "adjusts pacing, not difficulty" | **low–medium** (a few enemy types + candidate spots; L4D still had hand-made maps) |
| **Threat that reacts to the players** (targets, flees, chases based on what players do) | the team's positions feed the threat, so the plan must answer the moment | L4D special infected exist to break the "homogeneity/predictability" of the horde and "create dramatic cooperative moments" (Booth slides) [source]; Lethal Company: Bracken "stalks its prey" but "runs away when spotted", Jester follows a player once it spots one ([Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company)) [source]; Peak's Scoutmaster grabs anyone 160 m above the next climber (Millman review) [source] | **low** per threat. Caveat: a fixed rule is learnable (cause 10) |
| **Opponent that counters the team's habit** | punishes the most-used tactic, so the habit stops paying | Alien: Isolation unlocks locker-searching and vent behaviour after the player escapes repeatedly, "providing the illusion that the creature is learning" ([Game Developer](https://www.gamedeveloper.com/design/revisiting-the-ai-of-alien-isolation)) [source, single-player]; Phasmophobia patched ghosts to "ignore old tricks" ([PCGamesN](https://www.pcgamesn.com/phasmophobia/update-corners)) [snippet] | **medium** (each counter is an authored behaviour) |
| **Hidden information with a reason to hide** | no one player sees the whole plan, so it cannot be fixed in advance | Elias et al. p. 69 box "Limiting Experts' Ability to Play the Game for Beginners": skilled control, time pressure, communication limits, hidden information, role playing [source]; Alexandrian (paraphrase): hidden info often fails because nothing motivates keeping it hidden; Hanabi works because it is built around it [source] | **low** |
| **Traitor, hidden role, private goal** | someone in the team has a reason to break the plan; the plan itself becomes suspect | Hidden traitors raise "paranoia and distrust between players" ([Shi & Tambasco 2015](https://press-start.gla.ac.uk/press-start/article/view/6)) [source: abstract]; semi-co-op makes it "much easier to shrug off" a quarterback's suggestions "when you can't be sure of their motives" (quote seen in a search summary of alpha-player articles, e.g. [Meeple Mountain](https://www.meeplemountain.com/articles/benching-the-quarterback-how-to-deal-with-alpha-players-in-co-op-games/); exact page not opened) [snippet]; Zagal et al. 2006 lesson 1: add "a tension between perceived individual utility and team utility" ([blog summary of the paper](https://grdphil.blogspot.com/2010/11/review-collaborative-games-lessons.html), DOI 10.1177/1046878105282279) [source: secondary] | **low** (cost is design: it is no longer pure co-op) |
| **Human opposition** (versus team, one human hunter) | the opponent reads and answers the habit | Elias et al.: opponents give "repeat play value" [source]; Weibel et al. 2008: higher presence, flow and enjoyment against human than computer opponents ([BORIS record](https://boris.unibe.ch/33920)) [snippet]; but Evolve's 4v1 "caused more problems than we ever imagined" and shut down ([PC Gamer](https://www.pcgamer.com/au/evolve-dev-says-4v1-caused-more-problems-than-we-ever-imagined)) [snippet] | **low** content, **high** balance work; outside the brief (no team vs team) |
| **Real time + limited talk** | stops one player from directing all; does not by itself stop a habit | Alexandrian: real time "seems to be the only surefire solution to the quarterbacking problem" [source] | **low** |
| **Procedural layouts from a kit** | new space each round, so routes and roles must be re-decided | Deep Rock Galactic: 119 hand-made room templates + generator; "The game owes a great deal of its replayability to the limitless pool of possible caves" ([Ghost Ship dev blog](https://devtrackers.gg/deep-rock-galactic/p/8cd5ca9c-below-decks-at-ghost-ship-cave-generation-in-deep-rock-galactic)) [source]; Lethal Company "procedurally-generated rooms" plus random weather [source]; Peak: daily map from a small set plus procedural parts ([HackerNoon, third party](https://hackernoon.com/lite/inside-peaks-daily-map-generation-system)) [snippet] | **medium** (a room kit; a new map alone does not change a habit that ignores the map) |
| **Systemic rules / friendly fire / physics** | one rule set applies to everyone, so players' own actions create new situations | Helldivers 2: design is "inherently systematic", friendly fire stays, combat thinking "not in a 'solve the puzzle' way", "Maintaining the sense of chaos was one of the largest challenges" ([PlayStation Blog](https://blog.playstation.com/2024/03/12/helldivers-2-how-arrowhead-turned-the-twin-stick-shooter-original-into-a-bombastic-ps5-sequel/)) [source]; Sea of Thieves "Tools Not Rules" (paraphrase of design director Mike Chapman): how players use the tools and each other makes each session play differently ([Xbox Wire](https://news.xbox.com/en-us/?p=191429)) [snippet]; Koster: emergent play and player-made content are "ways of increasing the possibility space, making self-refreshing puzzles" [source] | **low**. Caveat (cause 4): chaos that only changes outcomes is output randomness |
| **Proximity / open voice** | adds drama and comedy between players | Booth: "Hearing friend's reactions increases drama and camaraderie" [source]; DayZ study: proximity and all-to-all voice "enable novel and enjoyable game play" ([OzCHI 2012](https://www.doi.org/10.1145/2414536.2414548)) [snippet] | **low**. [opinion] Makes rounds feel different; does not change the best plan |
| **Hand-made level disruptions** | each level breaks last level's habit | Overcooked: shift "from focusing the game on the various recipes to more interesting level designs"; layout disruptions to force talk (Wikipedia summary) [source: secondary] | **high** |
| **Content updates** | new monsters, maps, rules over time | Phasmophobia, Among Us, Peak updates; Peak devs: "not going to be a forever game" ([GamesRadar headline](https://www.gamesradar.com/games/co-op/peak-is-not-going-to-be-a-forever-game-but-the-viral-co-op-climbing-games-devs-dont-want-to-leave-anything-on-the-table-either)) [snippet] | **high** |

Friend co-op hits 2020–2026, what keeps their rounds apart (from the rows above):
Lethal Company = procedural rooms + random weather + reactive monsters + proximity voice;
Deep Rock Galactic = room kit generator + biomes; Peak = daily map + an anti-split threat + items
that work on friends; Helldivers 2 = systemic rules + friendly fire; Phasmophobia = random hidden
ghost type + patched ghost AI. None of them relies on physics alone. [opinion, from the sources above]

---

## Our guess, checked

Guess: "In pure co-op nobody pushes against the plan, so it settles."

**Verdict: mixed. The mechanism is supported; the implied fix (it needs a human pushing back) is
not.**

Supports the guess:
- Single-sided games lack an opponent's uncertainty and are prone to limited replay; an opponent
  gives "repeat play value" (Elias et al. pp. 26–27, 68–70) [source]. Long-lasting games have
  mostly been competitive (Koster) [source].
- A shared habit is stable because no one gains by breaking it (Lewis via SEP) [source]; repeated
  pairs lock into stable, short conventions (Hawkins et al.) [source: abstract]. Inside a pure co-op
  team, the teammates are the last people who would push against the plan.
- Pure co-op timing (*The Mind*) is solved by a counting habit [source]; L4D with fixed spawns
  "Becomes a race" (Booth) [source]; Overcooked playtesters got efficient fast [source: secondary].

Against the guess (the push need not be a human opponent):
- Left 4 Dead is pure co-op and replayable because a system, not a person, decides when and where
  pressure comes (Booth) [source]. Deep Rock Galactic is pure co-op and replayable through generated
  caves [source]. Hanabi is pure co-op and lives on a random deal plus hidden cards [snippet].
- A human opponent is not enough on its own: Evolve's 4v1 failed [snippet].
- A reactive AI threat can be enough, but only if its rule is not fully learnable (Pac-Man note,
  Elias p. 27) [source], or it counters the habit (Alien: Isolation) [source].

Sharper version **[opinion]**: *a plan settles when nothing in the round changes which plan is
best.* In pure co-op, teammates never change it (conventions are stable), so it must come from
the game: input randomness revealed in the round, or a threat that reads and answers the team's
habit. Physics and voice make rounds *feel* different but mostly change whether the plan works,
not which plan to use.

Side note on the premise **[snippet]**: the friend co-op hits are not all built for a long tail.
Peak's devs say it is "not going to be a forever game", and Among Us, Phasmophobia and Lethal
Company lean on content updates and mods. "Round 50 plays differently" is a stricter bar than most
of these hits meet without new content.

---

## Yes/no questions for a checker

1. **Plan card:** Could the team write one plan on a card before round 2 that still wins round 50?
   (Yes → it will settle.)
2. **Which, not whether:** Does something revealed at the start of or during a round (a deal, a
   layout, a threat's choice) change *which* plan is best, not only *whether* the plan succeeds?
   (No → it will settle; physics wobble alone is a "no".)
3. **Pushback:** Does anything in the round answer the team's habit — a threat that targets what the
   team keeps doing, a rule that is not fully predictable, or a player with a private reason to break
   the plan? (No → it will settle.)
4. **Still talking:** By round 20, does each player still need to hear something from a teammate
   that they could not have known before the round? (No → players have stopped reacting; it has
   settled.)
