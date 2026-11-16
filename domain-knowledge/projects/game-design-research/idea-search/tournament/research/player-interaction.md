# Player-with-player interaction vs side-by-side work (research, 2026-11-10)

Question: what counts as real player-with-player interaction in co-op, as opposed to players
working side by side on the same object? Trigger: Megalith Haul got "borderline" on F3, and the
user said "i can already sense that log rollers doesnt have player with player interaction".

Tags: **[source]** = I read the source text (or the passage in a source I read, named after "via").
**[snippet]** = search result or summary only. **[review]** = a secondary review of the paper, not
the paper itself. **[opinion]** = mine.

## Key findings (summary)

1. **A shared object is not what makes it fail.** The research counts acting through the world as
   real interaction when one player's act is aimed at one other player's next move: holding a gate
   open *for you* (Reuter et al. 2014), pushing a maze wall so *the collector* can reach a gem
   (Depping & Mandryk 2017). What fails is **pooling** (everyone's effort goes into one sum) and
   **parallel work** (work one player could do alone, split up only to go faster). Megalith Haul is
   both: pullers pool force, runners split a job one person could do.
2. **The social effect travels through talk and reply.** In Depping & Mandryk's experiment,
   interdependence raised trust *only through* the number of back-and-forth conversation turns
   (full mediation). Their design advice: dependence "should not be an addition of scores or damage
   or any other resource in the game, but be derived from a need to coordinate and interact during
   play."
3. **Someone named must be able to help or hurt me.** "A person is only vulnerable to a partner if
   they can be potentially hurt or helped by that person" (Depping 2018). The hits' best moments
   are all one named person acting on another: pulling a friend up a ledge, carrying a passed-out
   friend, carpet-bombing a friend, a friend's voice cutting out when he dies.

---

## Definitions and types

Terms used below:
- **Interdependence:** "the degree to which group members must rely on one another to perform
  their task effectively" (Depping 2018, citing Saavedra et al.). In: a task split among players.
  Out: how much each player's progress needs the others.
- **Task vs outcome interdependence:** task = "the necessity for each member to take action for
  other members to do any part of their work"; outcome = "the degree to which the outcomes an
  individual receives depend on the performance of others" (Johnson & Johnson, via Depping 2018).
  Outcome interdependence (a shared score) needs no interaction during play.
- **Coupling:** "the amount of work that one person can do before they require discussion,
  instruction, action, information, or consultation with another person" (Gutwin & Greenberg 2002).
  Loose = long solo stretches; tight = constant need for each other.
- **Reciprocation loop:** A acts on B, at some cost to A; B updates their view of A; B acts back on
  A (Cook 2016/2018).

### Research

- **Social interdependence theory (Johnson & Johnson).** Positive interdependence = I reach my goal
  only if the others reach theirs. Types: goal, resource ("each group member an essential piece of
  the puzzle"), role ("an interconnected role for each individual"), identity; grouped as outcome
  (goals, rewards), means (roles, resources, tasks) and boundary.
  [source: [Wikipedia, Positive interdependence](https://en.wikipedia.org/wiki/Positive_interdependence)]
  Some teaching lists add reward, task, environmental, fantasy and outside-enemy types. [snippet]
  Task vs outcome split, and the advice to prefer task interdependence:
  [source: [Depping 2018 dissertation](https://harvest.usask.ca/bitstream/10388/12093/1/DEPPING-DISSERTATION-2018.pdf), §3.7.3.2]
- **Depping & Mandryk 2017, "Cooperation and Interdependence" (CHI PLAY).** Two separate factors:
  cooperation (shared goal vs rival goals) and interdependence (dependent vs independent). Both
  raised trust, with no interaction between them. In their Labyrinth game, interdependence meant
  complementary roles: a "pusher" who can only shift maze walls and a "collector" who can only pick
  up gems. The pusher acts on the shared maze, not on the collector, and this still counted as high
  interdependence. The effect of interdependence on trust was fully carried by conversational turns;
  the effect of a shared goal was not (it works through group identity, "us against the game").
  Interdependence even raised closeness in the competitive version.
  [source: [Depping 2018 dissertation](https://harvest.usask.ca/bitstream/10388/12093/1/DEPPING-DISSERTATION-2018.pdf), ch. 3; [paper listing](https://bibtex.github.io/CHI-PLAY-2017-DeppingM.html)]
- **Depping's review of social-play design advice.** Roles, unique abilities, synergies and
  communication collapse into one thing, interdependence; "Roles can be implemented in ways that do
  not require any interactions between players." Example: in Diablo a fighter's and a caster's
  damage "do not affect each other but only accumulate" (no synergy), while some RPG spells make an
  enemy weaker to *another* player's attacks (synergy).
  [source: Depping 2018, §1.2.2]
- **Rocha, Mascarenhas & Prada 2008, "Game Mechanics for Cooperative Games".** Six patterns: shared
  goals, synergies between goals, complementarity (roles), synergies between abilities, "abilities
  that can only be used on another player", special rules for teammates.
  [source via Depping 2018, Table 1.1; paper not opened. [GAIPS listing](https://gaips.inesc-id.pt/component/gaips/publications/showPublication/3/87)]
- **Seif El-Nasr et al. 2010, "Understanding and Evaluating Cooperative Games" (CHI) + Aghabeigi
  2011 thesis.** New patterns: camera setting, interacting with the same object (Katamari, Little
  Big Planet), shared puzzles, shared characters, enemies that target the lone wolf (Left 4 Dead's
  Hunter, Smoker), automatic vocal call-outs. **Cooperative Performance Metrics (CPM)**, coded from
  video: laughter and excitement together, worked-out strategies, helping, global strategies
  (complementary roles), waited for each other, got in each other's way.
  [source: [Aghabeigi 2011 thesis (same study)](https://summit.sfu.ca/_flysystem/fedora/sfu_migrate/11576/etd6462_BAghabeigi.pdf), §4–5]
- **Reuter, Wendel, Göbel & Steinmetz 2014, "Game Design Patterns for Collaborative Player
  Interactions" (DiGRA).** Definition: "synchronous actions in which multiple players coordinate
  themselves ... Each action may be directed upon another player or the game world". They include
  world-directed acts on purpose: "a player holding a gate open while others move through it."
  Patterns: **Concurrency** (operating objects together "that could not be operated by a single
  player alone", e.g. carrying a palm by three), **Parallelization** ("Splitting work that could be
  done alone in order to speed it up"), Separation gate, Gathering gate, and **Support** ("one
  player directly benefits another"): Strengthening, Resupply, Protector, Savior, Sacrifice. Their
  diagnosis of tacked-on co-op: "players only interact with the game world as a single player would
  do". [source: [PDF](https://www.kom.tu-darmstadt.de/papers/RWGS14-1.pdf)]
- **Zagal, Rick & Hsi 2006, "Collaborative Games: Lessons Learned from Board Games".** Lessons:
  tension between individual and team utility; players act "without the consent of the team";
  "Players must be able to trace payoffs back to their decisions"; give "different abilities or
  responsibilities". Pitfalls: one player making the decisions for the team; players not caring
  about the outcome; the same experience every time.
  [review: [grdphil blog review](https://grdphil.blogspot.com/2010/11/review-collaborative-games-lessons.html); lessons also listed in Depping 2018 Table 1.1 [source]; [paper PDF](https://www.eng.utah.edu/~zagal/Papers/Zagal%20et%20al%20-%20Collaborative%20Games%20-%20Lessons%20learned%20from%20boardgames.pdf) blocked to me]
- **Harris & Hancock (2016 CHI PLAY; 2019 CHI "To Asymmetry and Beyond!").** Asymmetry types:
  ability, challenge, information, investment, goal/responsibility [source via Depping 2018,
  Table 1.1]. Asymmetric co-op beat symmetric co-op on connectedness and social engagement; more
  designed interdependence raised it further, through "cooperative action timing and direction of
  dependence" (one-way vs two-way) [snippet: [touchlab page](https://uwaterloo.ca/touchlab/references/asymmetry-and-beyond-improving-social-connectedness)].
  Dynamics named in Harris's thesis: directional dependence, synchronicity, necessity, leadership,
  primacy [snippet: [UWSpace record](https://uwspace.uwaterloo.ca/handle/10012/14710)]. Full texts
  blocked to me; exact conditions unchecked.
- **Beznosyk et al. 2012.** Closely coupled co-op patterns gave better player experience than
  loosely coupled ones; without a voice channel, close coupling got harder.
  [snippet: [IFIP/HAL listing](https://dl.ifip.org/IFIP-LNCS-7522/hal-01556174); [APCHI record](https://documentserver.uhasselt.be/handle/1942/13935)]
- **Coupling, from groupware research (Gutwin & Greenberg 2002).** Definition above.
  [source via [arXiv 1904.13364](https://arxiv.org/pdf/1904.13364), which quotes it]
- **Fullerton's player interaction patterns.** Single player vs game, **multiple individual players
  vs game** ("actions are directed towards the game system and interaction between players is
  limited"), player vs player, unilateral, multilateral, cooperative play, team competition. Games
  stuck in the second pattern are called "massively parallel single-player games" (Järvinen).
  [source via [Paavilainen, Alha & Korhonen, DiGRA](https://dl.digra.org/index.php/dl/article/download/784/784)]
- **Manninen 2002/2003, interaction forms.** "Interaction forms are perceivable actions that act as
  manifestations of the user-user and user-environment interactions."
  [source via Reuter 2014; [Game Studies article](https://www.gamestudies.org/0301/manninen) unreachable]
- **Board-game practice: direct vs indirect.** Direct = you act on another player's things or
  progress; indirect = you affect them only through shared systems (taking a resource they wanted,
  blocking a space). [snippet: [Gil Hova GDC talk](https://gdcvault.com/play/1025687/Board-Game-Design-Day-Why), [Game Developer, "Interaction in Games"](https://www.gamedeveloper.com/design/interaction-in-games)]

### Practitioners: who acts ON whom in friend co-op hits (2020–2026)

- **Dan Cook / Project Horseshoe, "Game design patterns for building friendships".** Four factors:
  proximity, similarity, reciprocity, disclosure. Reciprocity: "Player A performs an action that
  targets Player B" at a cost to A; B updates their view of A; B acts back; "there must be a
  bidirectional flow between both parties." Anti-pattern: "Large power gaps that make players
  useless to each other." [source: [Game Developer](https://gamedeveloper.com/design/game-design-patterns-for-building-friendships)]
- **PEAK (2025).** The grab: "Holding right mouse button with an empty hand will let a player pull
  a climbing friend up". Carrying a passed-out friend at a large weight cost gives "a very real
  feeling of camaraderie". Food and healing work on friends. Scoutmaster Meyers punishes anyone
  160 m ahead. The same review names the friendslop failure: in Lethal Company "the most efficient
  way to play is to split up almost immediately."
  [source: [GDC 2026 narrative review, Millman](https://media.gdcvault.com/gdc2026/GNR/Papers/Zac+Millman+-+GDCReview_2026_Peak_Millman.pdf)]
  Aftermath: "using handgrabs and hoisting other players up"; mechanics "inspire teamwork as much as
  pranking your friends". [source: [Aftermath](https://aftermath.site/peak-multiplayer-streamers/)]
  Footstool boosts. [snippet: [PEAK wiki](https://peak.wiki.gg/wiki/Climbing)]
- **Helldivers 2 (2024), Johan Pilestedt.** Friendly fire makes "the players a true interactable
  part of the game world"; "the chuckles that happen when you accidentally carpet bomb your
  friends." [source: [PlayStation Blog](https://blog.playstation.com/2024/03/12/helldivers-2-how-arrowhead-turned-the-twin-stick-shooter-original-into-a-bombastic-ps5-sequel/)]
  Reviewers' funniest moments are teammates killing teammates.
  [snippet: [Game Horizon review](https://gameshorizon.com/review/helldivers-2-review-a-benchmark-for-co-op)]
- **Lethal Company (2023), Zeekerss.** "it's actually a game about laughing at death"; proximity
  voice, so a friend's voice cuts off when he dies. [source: [Push To Talk](https://www.pushtotalk.gg/p/how-lethal-company-sold-10-million-copies)]
- **R.E.P.O. (2025).** Grab a teammate's head to give them health; carry a dead friend's head to
  extraction to revive them; bumping valuables into other players breaks them.
  [snippet: [PC Gamer guide](https://www.pcgamer.com/games/horror/repo-how-to-heal-and-revive/)]
- **Chained Together (2024).** Players are physically chained, so each jump pulls the others.
  [snippet: [PC Gamer](https://pcgamer.com/games/action/the-latest-friendship-ruining-co-op-game-on-steam-is-a-punishing-platformer-where-youre-chained-to-your-pals-and-its-about-to-crack-100000-concurrent-players)]
- **Overcooked (2016, the pre-2020 reference), Phil Duncan.** Co-op that "simply meant two avatars
  and twice as many enemies" was what they avoided; aim: "all players are equally responsible";
  under time pressure, "lots and lots of shouting".
  [source: [Game Developer, Road to the IGF](https://gamedeveloper.com/design/road-to-the-igf-ghost-town-games-i-overcooked-i-), [GoNintendo](https://www.gonintendo.com/archives/264687-overcooked-special-edition-devs-talk-about-building-a-deeply-cooperative-experience)]
  Moving Out reviews put the laughs in throwing furniture to each other and out of windows.
  [snippet: [OpenCritic reviews](https://opencritic.com/game/9246/view/reviews)]
- **Friendslop guides.** "Almost every successful friend slop game has proximity voice chat";
  "Design for comedic failure states. Make death spectatable. Let players laugh at each other."
  [source, opinion-grade: [Cinevva guide](https://app.cinevva.com/guides/co-op-game-design)]

**Pattern across the hits [opinion, from the items above]:** the moments players retell are one
named person acting on another named person's body or life: pull up, carry, feed, revive, shove,
shoot, drop. Shared-object work (carrying a couch, hauling loot) gets laughs mainly when it fails
*because of someone*: a throw, a bump, a yank.

---

## A short test

Ask these about the rule's core moment. **All three yes = real player-with-player interaction.**

1. **Aimed at a person:** does my action land on one specific teammate (their body, sight,
   options, danger, or the thing they hold right now), rather than on a pool everyone adds to?
   Sources: Depping 2018, dependence "should not be an addition of scores or damage or any other
   resource" [source]; Cook, "Player A performs an action that targets Player B" [source]; Rocha,
   "abilities that can only be used on another player" [source via Depping]; Fullerton's "multiple
   individual players vs game" as the failing pattern [source via Paavilainen].
   *Quick form [opinion]: in the one-sentence rule, is the object of the verb another player? "Carry
   logs" → no. "Shove a friend" → yes.*
   A shared object passes if it carries my act to one person's next move (a gate held open for you,
   a wall pushed for the collector: Reuter 2014, Depping 2017 [source]).
2. **They must answer within seconds:** does that teammate have to react to it, so that it turns
   into a back-and-forth, and does their move change my next move?
   Sources: Cook, "bidirectional flow" [source]; Reuter, "players cannot act without considering
   what the other players are doing" [source]; Depping, the trust effect is carried by
   conversational turns [source]; Gutwin & Greenberg's coupling [source via arXiv]; Harris &
   Hancock, two-way and same-time dependence raise connectedness [snippet].
3. **A named person to thank or blame:** can one specific teammate be helped or hurt by it, so that
   credit and fault land on a face?
   Sources: Depping 2018, "A person is only vulnerable to a partner if they can be potentially hurt
   or helped by that person" [source]; Zagal 2006, "trace payoffs back to their decisions" [review];
   Pilestedt on friendly fire [source].

Reading a fail: no on 1 = side-by-side work (pooled or parallel). Yes on 1, no on 2 = one-way help
or a pressure plate (one end only waits). No on 3 = no one to thank or blame.

---

## Apply the test

| Rule | 1 Aimed at a person | 2 Answer in seconds | 3 Named help/hurt | Verdict |
|---|---|---|---|---|
| (a) Megalith Haul | no | no | weak | **Fail** |
| (b) Bull relay | yes | yes | yes | **Pass** |
| (c) Traps seen around others only | yes (by voice) | yes | yes | **Pass, talk-only** |
| (d) Only shove a friend | yes | yes | yes | **Pass, strongest** |

- **(a) Megalith Haul: fail.** Pullers add force to one sum (Reuter's Concurrency in its pooled
  form, Depping's "addition of ... any other resource"). Runners do Reuter's Parallelization:
  carrying a log from back to front is a job one runner could do alone, split up only to go faster.
  No act aims at a teammate; no teammate has to answer. A late log hurts "the stone", so blame lands
  on "the runners", not on one face. This matches the user's sense; the reason is pooling plus
  parallel work, not the stone itself. *What would flip it [opinion]: make each log pass from one
  named hand to another at the moment the other is exposed (e.g. a placer under the front edge who
  only lives if the right runner's log arrives).*
- **(b) Bull relay: pass.** The act goes through the bull but lands on one person: my stepping out
  takes the charge off the teammate who just ducked (Reuter's Protector/Savior). They must duck the
  instant I step out, and the next player must step out as I duck: a chain of seconds-long replies.
  Step out late and one named friend gets gored. Watch for [opinion]: at 6 it may become a fixed
  rota where each player only ever deals with the next one, or one caller runs it.
- **(c) Traps seen around every teammate, never around yourself: pass, but talk-only.** My warning
  aims at one teammate's danger; they react within seconds and warn me back, since they see my
  traps; a missed warning hurts a named friend. Caveat [opinion]: the only act on the friend is
  voice. That is exactly what carries the social effect in Depping's study, but if the crew goes
  quiet nothing happens, and the game gives no verb that touches the friend. Gen 1 linked this
  family to Hanabi (a novelty issue, outside this test).
- **(d) No one can walk; you can only shove a friend away: pass, strongest.** Every act lands on a
  friend's body (Rocha's "abilities that can only be used on another player" in its purest form).
  The shoved friend can only move on by shoving someone in turn, so replies are forced. A shove into
  a pit has one name on it. Watch for [opinion]: the shoved friend is passive mid-flight (the
  pressure-plate trap, briefly), and one planner may end up directing every shove.

---

## What the sources say makes interaction feel social

- **Back-and-forth talk, not the shared goal alone.** Interdependence → more conversational turns →
  more trust (full mediation). A shared goal raises trust another way (group identity), without more
  talk. Give players a rich enough signal channel; "in-game actions can be interpreted as
  conversational turns." [source: Depping 2018]
- **Laughing together, helping, getting in each other's way.** The CPM list. In El-Nasr's videos,
  shared laughter came mostly from presentation (Lego Star Wars' falling-down animation, Little Big
  Planet's dancing and handshakes), then shared goals, complementary roles, shared puzzles and characters.
  "Got in each other's way" came 50% from a shared camera that drags players. [source: Aghabeigi 2011]
- **Reciprocity with a cost.** Small costly acts aimed at one person, repeated and returned, build
  friendships; design for ignored or harmful replies too. [source: Cook]
- **Visible blame and dark comedy.** Friendly fire ("carpet bomb your friends"), "laughing at
  death", spectatable failure. [source: Pilestedt, Zeekerss; opinion-grade: Cinevva]
- **Rescue at a price.** Carrying a passed-out friend costs weight, and that cost is what makes it
  feel like camaraderie. Reuter's Sacrifice pattern is the same shape: help that costs the helper,
  which "requires selflessness". [source: PEAK GDC review; Reuter 2014]
- **Needing each other beats running a race.** Co-op without dependence becomes "a race to see who
  could kill the next enemy or grab the next loot drop" (Duncan) [snippet: Game Developer interview
  excerpt]; efficient play that splits the crew kills the social part (PEAK review on Lethal
  Company) [source].
- **Two failure modes to guard against.** One player deciding for all (Zagal's pitfall
  [review]); large skill or power gaps that make players useless to each other (Cook [source]).

## Sources not reached
Zagal 2006 PDF (403), Harris & Hancock 2016/2019 full texts (paywall, bot wall), Manninen 2003
(connection refused), Beznosyk 2012 PDF, Rocha 2008 PDF. Their claims above are from secondary
sources and are tagged as such.
