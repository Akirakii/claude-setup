# Game theory of hide, seek and bluff: why a human counter-chooser makes endless variety

Tag legend. [read] = I opened the page and read the claim there (quotes came back through a page-reading tool, so wording may be a few characters off; check against the page before printing them). [snippet] = taken from a search-result summary only, page not opened, lower confidence. [opinion] = a practitioner's view or my own inference, not a formal result.

Terms used below. "Pure strategy" = always making the same choice in a given spot. "Mixed strategy" = choosing between options by a fixed set of odds (for example 50/50). "Equilibrium" = a pair of plans where neither side gains by changing alone. "Coupling" here means how much one player's best choice depends on what another player chooses (my reading of the user's term).

The mechanism in four lines [opinion, built from the findings below]:
1. Against a fixed environment the best move does not depend on you, so it can be found once and repeated forever (a dominant line). The game is a puzzle and it gets solved.
2. In hide/seek-shaped games (matching pennies, rock-paper-scissors, search games) every fixed choice can be beaten. The only safe plan is a spread of odds over many options, so every option stays in use. Variety comes from the rules, not from authored content.
3. Humans do not play that spread well. They fall into patterns, so the real game becomes reading the other person and being read (Sirlin's "yomi"). Each read changes the best answer, so the loop never settles.
4. Hidden information (bluffing) and simultaneous choices are the two tools that create this structure. Coordination games (rendezvous, Schelling points) create the same "I think that you think" loop between teammates, but they tend to settle once a shared answer is found.

## 1. What search games and hide-and-seek theory say, and the role of mixed strategies

### Takeaway
Formal search games are a known class where no fixed (pure) plan is safe. The solution is a probability spread over hiding spots and search routes, and a well-tuned version uses every spot. Pursuit games with full information, by contrast, are solved with a single fixed plan. The difference is exactly hidden information plus an opponent who picks the counter.

### Cited Findings
- Alpern and Gal's *The Theory of Search Games and Rendezvous* (Springer, 2003) is split into two books. Book I covers search games, which are zero-sum: the hider wants to avoid being found. Book II covers rendezvous, where the target wants to be found. — [Springer](https://link.springer.com/book/10.1007/b100809) [snippet]
- Alpern and Lee (2019): "Pursuit games are usually of perfect information and are solved in pure strategies using techniques involving differential equations. Search games, on the other hand, typically require mixed strategies." Both kinds were first modelled and solved by Rufus Isaacs (1965). — [Alpern & Lee, "A Normal Form Game Model of Search and Pursuit", arXiv 1811.09538](https://arxiv.org/pdf/1811.09538.pdf) [read]
- Gal and Casas (2014) predator-prey model: the hider picks one of several spots and the searcher can inspect k of them. Each spot has its own capture chance. If k is high enough (for example the searcher can inspect every spot), the hider uses a pure strategy: always the spot with the lowest capture chance. If k is below a threshold (for example k = 1), the hider mixes so that (chance of being at a spot) x (capture chance there) is the same for every spot. — [Alpern & Lee, summarising Gal & Casas](https://arxiv.org/pdf/1811.09538.pdf) [read]
- Alpern, Gal and Casas (2015) extended this to repeated play after a failed capture: "the hider should choose his location more randomly when the pursuing searcher is more persistent." — [Alpern & Lee lit review](https://arxiv.org/pdf/1811.09538.pdf) [read]
- Lidbetter and Hellerstein (2017) solve search games with a method like fictitious play: the searcher keeps updating his best plan after seeing the opponent's response. — [Alpern & Lee lit review](https://arxiv.org/pdf/1811.09538.pdf) [read]
- In a related search-game paper, any optimal mixed hiding plan hides in every location with a chance above zero. — [arXiv 2103.09310](https://arxiv.org/pdf/2103.09310) [snippet]
- Von Neumann (1953), "A certain zero-sum two-person game equivalent to the optimal assignment problem" (*Contributions to the Theory of Games II*, pp. 5-12): one player hides in a cell of a grid, the other guesses a row or column. The game is equivalent to the assignment problem; the best mixed plans for both players come from the two sides of a linear program. — [Adler, Bullinger & Vazirani, arXiv 2410.10767](https://arxiv.org/html/2410.10767v3) [snippet]
- Merrill Flood computed optimal strategies for this game directly, "The Hide and Seek Game of Von Neumann", *Management Science* 18(5). Sources disagree on the date (one says a 1968 report; the journal volume is from 1972). — [INFORMS](https://pubsonline.informs.org/doi/10.1287/mnsc.18.5.107) [snippet]
- Matching pennies (one player wins on a match, the other on a mismatch) has no pure-strategy equilibrium "since there is no pure strategy (heads or tails) that is a best response to a best response". The only equilibrium is 50/50 for both. — [Wikipedia: Matching pennies](https://en.wikipedia.org/wiki/Matching_pennies) [snippet]
- Each mixer picks odds that make the opponent indifferent between their options, so neither side gains by switching. Every finite game with no pure equilibrium has a mixed one. — [Game Theory 101](https://gametheory101.com/?p=55) [snippet]
- Penalty kicks in football have been found to look like a mixed-strategy equilibrium. In lab play, people often stray from the equilibrium, especially in repeated play. — [Wikipedia: Matching pennies](https://en.wikipedia.org/wiki/Matching_pennies) [snippet]
- Rock-paper-scissors counts as "solved" only in the mixed sense: the Solved game article says perfect play "can be generalized to non-perfect information games," and uses rock-paper-scissors as its example. — [Wikipedia: Solved game](https://en.wikipedia.org/wiki/Solved_game) [read]
- Real players are not random. Wang, Xu & Zhou (2014, *Scientific Reports* 4:5830) found group-level cycling in rock-paper-scissors that contradicts the equilibrium prediction. A simple win-lose-tie response rule explains it. — [arXiv 1404.5199](https://arxiv.org/pdf/1404.5199) [snippet]
- Press coverage of that study: winners tend to repeat their move, and losers shift to the next move in the cycle. — [Phys.org](https://m.phys.org/news/2014-05-reveals-chances-rock-paper-scissors.html) [snippet]
- Win-stay/lose-shift has the most empirical support of the human rules, though Forder and Dyson (2016) found people rely more on lose-shift than on win-stay. — [Zhang, Moisan & Gonzalez, CMU](https://www.cmu.edu/dietrich/sds/ddmlab/papers/ZhangMoisanGonzalez2020.pdf) [snippet]

### Inferences
- [opinion] Variety per unit of content: n hiding spots plus a searcher who picks the counter give a mixed equilibrium spread over all n spots. Each spot is one piece of content, but it gets re-chosen every round for a different reason, so content is reused instead of used up. A puzzle with n spots is used up once the right one is known.
- [opinion] Gal-Casas gives two tuning rules. (a) Search budget: if the seeker can check almost everything, the hider's best plan goes pure (one safest spot) and variety collapses. Keep the seeker's budget below the "check everything" line. (b) Unequal spots are fine: the indifference rule means a risky spot is used less often but still used. Good and bad spots can coexist without one dominating, as long as the budget stays below the line.
- [opinion] "More random when the searcher is persistent" means pressure (repeat attempts, chases) pushes hiders toward more varied play. Longer chases breed more variety.
- [opinion] The equilibrium is the floor, not the experience. Real humans fall into patterns like win-stay/lose-shift, and the fun is in spotting and punishing those patterns. That is the bridge to yomi (section 2).

### Gaps
- I did not read von Neumann's 1953 paper or Alpern & Gal's book directly. Details come from later papers that summarise them.
- I found no clean worked value for a simple textbook hide-and-seek game.
- The Stanford Encyclopedia entry's section on mixed strategies was beyond the part I could read (first 100k characters only).
- The sample size of the Wang et al. study (360 players, 300 rounds, groups of six) appears only in a pop-science article, so it is unverified.

## 2. Simultaneous hidden decisions and prediction loops (yomi, Sirlin)

### Takeaway
Sirlin's claim is that a game's strategic depth is "almost entirely" its ability to support and reward reading the opponent. Double-blind (simultaneous, hidden) choices are his main tool "in fighting against solvability". The prediction loop wraps around after a few layers, so it never resolves into a fixed answer. Depth needs more than bare rock-paper-scissors: unclear payoffs, information to read, and losses you can recover from.

### Cited Findings
- Sirlin, *Playing to Win*, ch. 7 "Spies of the Mind": "In competitive games, there is little more valuable than knowing the mind of the opponent". — [Sirlin.net](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read]
- "Yomi" is Japanese for "reading", as in reading the mind of the opponent. — [Wikipedia: Yomi (card game)](https://en.wikipedia.org/wiki/Yomi_(card_game)) [snippet]
- Sirlin: "All the complicated decisions in game theory go away if you know exactly what the opponent will do next." — [Sirlin.net ch. 7](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read]
- Sirlin: "the 'strategic depth' of a game should be defined almost entirely on its ability to support and reward yomi." — [Sirlin.net ch. 7](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read] [opinion: practitioner]
- The layers. Layer 0: "discovering how good that move is and doing it all the time". Layer 1: the opponent catches on that you'll use it a lot. Layer 2: "You knew what he would do (yomi), but he knew that you knew". Layer 3: "you know that he knows that you know what he will do". — [Sirlin.net ch. 7](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read]
- The loop wraps: "there need only be support up to yomi layer 3, as yomi layer 4 loops back around to layer 0." — [Sirlin.net ch. 7](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read]
- Sirlin on habit: "It's really conditioning, not strategy, that tells Pai she needs to do a throw escape here". Players are trained by the opponent's past behaviour, which the opponent can then exploit. — [Sirlin.net ch. 7](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) [read]
- Sirlin, "Designing Yomi" (21 Aug 2014): "Double blind decisions are a very useful tool in fighting against solvability in games." — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- Same article: "Fighting games are actually double blind though because of the speed of the gameplay." Moves are technically in sequence, but reaction time makes them effectively simultaneous. — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- Same article: bare rock-paper-scissors is thin: "if you literally play a game of rock, paper, scissors, you have very little to go on when you decide which move to use." Counters themselves are not a flaw: "All that means is that things beat each other and everything has a counter." — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- Same article on payoffs: "It's a lot better if the payoffs for each option are unclear." "Ideally these judgments are so complicated that you must use your intuition to solve them". — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- Same article: "high level Yomi play always involves reading the opponent". Sirlin also argues that perfect-information games tend to "break" (get solved) sooner than games with "some hidden information, randomness, or something to break up the rigidity." — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- The Yomi card game was built to boil fighting-game mind games down to a card game in which you pick your move double-blind with your opponent. — [Sirlin.net](https://www.sirlin.net/articles/designing-yomi) [read]
- Caleb Compton (Game Developer, 11 Feb 2019) lists what a game needs for yomi: several workable options per player, counters for everything, and different attacks needing different counters. Otherwise there is "no need to predict what they are about to do." He also argues "any combo is escapable", so one wrong guess must not mean certain death. — [Game Developer: Know Thy Enemy](https://www.gamedeveloper.com/design/know-thy-enemy-designing-for-yomi-in-games) [read] [opinion: practitioner]
- A Magic: The Gathering commentator says most players never get past yomi layer 2. — [StarCityGames](https://articles.starcitygames.com/articles/analyzing-and-dissecting-yomi-1/) [snippet] [opinion]

### Inferences
- [opinion] The yomi loop is matching pennies played repeatedly by people with memory. Equilibrium play would make history useless, but humans leave patterns (section 1), so history becomes the content. Every match writes new "content" (habits, reads) at zero authoring cost.
- [opinion] Why it is not solved: the best move is a function of the opponent's current habits, and the opponent's habits react to your moves. The target keeps moving. The wrap at layer 4 keeps the loop small enough for casual players to enter, while most players live at layers 0-2.
- [opinion] Sirlin's "double blind because of speed" matters for real-time co-op/versus games: you do not need turn-based simultaneous reveal. If reacting is slower than committing (a hider's dash, a seeker's lunge), you already have hidden simultaneous choices.
- [opinion] Recipe for a verb pair that stays alive: every option has a counter, the payoffs are not equal (so it is not pure 1/3-1/3-1/3), there is something to read (positions, voice, body language), and a lost guess costs a round, not the match.

### Gaps
- I found no GDC talk transcript or fighting-game designer quotes on mind games beyond Sirlin and Compton. Searches surfaced only fan and blog commentary.
- The ch. 7 page I read did not mention rock-paper-scissors or random play directly. Sirlin's view on how strong pure random play is was not found in what I read.

## 3. Rendezvous and coordination (Schelling points): coupling minds without opposition

### Takeaway
Rendezvous search (Alpern) and focal points (Schelling) are the cooperative mirror of hide-and-seek. Both players want to meet but cannot talk, so each must model what the other expects them to expect. This couples minds without an opponent. The hard version is the symmetric one, where no one has a pre-assigned role. Once roles or a shared answer exist, the problem becomes trivial.

### Cited Findings
- Rendezvous problem: "Two people have a date in a park they have never been to before." Each must choose to wait or search, to maximise the chance of meeting. Steve Alpern posed it informally in 1976 and formalised the continuous version in 1995. — [Wikipedia: Rendezvous problem](https://en.wikipedia.org/wiki/Rendezvous_problem) [read]
- The asymmetric version (roles can be assigned) has a simple optimal answer: one player stays put while the other visits the locations in random order. — [Wikipedia: Rendezvous problem](https://en.wikipedia.org/wiki/Rendezvous_problem) [read]
- The symmetric version (same choices, no roles) is hard. Anderson and Weber conjectured the optimal plan in 1990. Weber proved it for three locations in 2012, calling it the first non-trivial symmetric rendezvous problem fully solved. — [Wikipedia: Rendezvous problem](https://en.wikipedia.org/wiki/Rendezvous_problem) [read]
- Focal point: "a solution that people tend to choose by default in the absence of communication in order to avoid coordination failure", introduced by Thomas Schelling in *The Strategy of Conflict* (1960). — [Wikipedia: Focal point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) [read]
- Schelling (p. 57): "[p]eople can often concert their intentions or expectations with others" "if each knows that the other is trying to do the same." — [Wikipedia: Focal point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) [read]
- Schelling's New York question (meet a stranger, no prior contact): the most common student answer was noon at the information booth at Grand Central. It was picked because it was a known meeting place (salience), not because it paid more. — [Wikipedia: Focal point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) [read]
- Schelling's own explanation, 2005 interview: in that era all trains went to Grand Central, so you met at the information desk. — [Richmond Fed interview](https://www.richmondfed.org/publications/research/econ_focus/2005/spring/full_interview) [snippet]
- Schelling's informal results: 36 of 40 people claimed $50 in a split-$100 game. In a heads/tails matching game, 16 of 22 A-players and 15 of 22 B-players chose "heads". — [Wikipedia: Focal point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) [read]
- Mehta, Starmer & Sugden (1994, *American Economic Review* 84(3):658-673) repeated Schelling's informal tests under controlled conditions with money at stake. — [Wikipedia: Focal point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) [read]
- Crawford, Gneezy & Rottenstreich ran a "Chicago skyscrapers" version of the New York game. Only 60% of 99 subjects chose Sears Tower, so the focal point was weaker there. — [Gneezy, focal points PDF](https://Rady.ucsd.edu/_files/faculty-research/uri-gneezy/focal-points.pdf) [snippet]
- Stanford Encyclopedia of Philosophy, on the Hi-Lo coordination game: "surely sensible players with perfect information would converge on s1-t1?". Standard equilibrium analysis alone does not guarantee that they do. — [SEP: Game Theory](https://plato.stanford.edu/entries/game-theory/) [read]

### Inferences
- [opinion] Coordination couples teammates through the same "I think that you think" loop as yomi, but with the sign flipped: you want to be predictable to your partner, and only to your partner. Real-world precedent sits in the theory itself: Book I (hide) and Book II (meet) of Alpern & Gal share the same machinery.
- [opinion] Free communication or pre-assigned roles kill the problem. The asymmetric rendezvous is trivial ("one waits, one walks"). For co-op design, the coupling lives in limited channels: no voice for a moment, one-word pings, split views.
- [opinion] Focal points are cultural. Grand Central worked because of the trains, and Sears Tower worked less well. In a friend group, shared history and in-jokes become the focal points, so each group grows its own content.
- [opinion] Pure coordination has a weaker engine than opposition. Once a focal point is found, nobody has a reason to leave it, so repeated play tends to settle. Coordination stays fresh only if the map changes, the channel is cut again, or an opponent punishes predictable meeting spots. A seeker who exploits the team's focal points brings back the hide-and-seek loop: hiders must coordinate with each other while staying unpredictable to the seeker.

### Gaps
- I did not retrieve Mehta, Starmer & Sugden's success rates (with versus without money), or the main result of Crawford et al. I believe from background knowledge that small payoff differences between options weaken focal points, but I did not verify it here.
- I found no source on how fast repeated coordination games lock into a habit (convention). Lewis's *Convention* (1969) would be the place to check; not read.

## 4. What makes a game "solved" or lets a dominant strategy appear; fixed environments versus adapting humans

### Takeaway
"Solved" means two different things. In full-information games it means a known move list (checkers, Connect Four). In hidden-information games it means a known recipe of odds (rock-paper-scissors, heads-up limit hold'em), which still produces varied play every game. A fixed environment does not react to your plan, so the best plan against it is fixed and can be learned. A human opponent re-optimises against you, so your best plan keeps moving.

### Cited Findings
- Allis (1994) levels of solution. Ultra-weak: prove the result from the start position with perfect play. Weak: "Provide one algorithm for each of the two players, such that the player using it can achieve at least the optimal outcome." Strong: an algorithm with reasonable resources that "finds optimal plays for both players" from any position. — [Wikipedia: Solved game](https://en.wikipedia.org/wiki/Solved_game) [read]
- Connect Four was solved in 1988 (Allen; Allis), and the first player wins. Checkers was weakly solved on 29 April 2007 by Schaeffer's team (a draw). Tic-tac-toe is a draw. Solved games usually have full information and no chance. — [Wikipedia: Solved game](https://en.wikipedia.org/wiki/Solved_game) [read]
- Heads-up limit Texas hold'em was declared "essentially weakly solved" by Bowling, Burch, Johanson & Tammelin (*Science* 347:145-149, Jan 2015). "Essentially solved" means a lifetime of play could not tell it apart from perfect at 95% confidence. Bowling: "We're not quite perfect, but we're so close that even after a lifetime of playing against it, you wouldn't know it wasn't perfect." — [Bowling publications page](https://webdocs.cs.ualberta.ca/~bowling/publications/b2hd-15science.html); [CS Monitor](https://csmonitor.com/Science/2015/0108/How-a-computer-program-took-the-gambling-out-of-poker) [snippet]
- Stanford Encyclopedia of Philosophy draws the core line between "acting parametrically on a passive world and acting non-parametrically on a world" that reacts. Of a natural obstacle: "the environment is not interested in your plans." A game is defined as any situation where an agent can only maximise her payoff "through anticipating" others' responses. — [SEP: Game Theory](https://plato.stanford.edu/entries/game-theory/) [read]
- Pursuit games with full information are solved in pure strategies, while search games (hidden location) need mixed ones. — [Alpern & Lee](https://arxiv.org/pdf/1811.09538.pdf) [read]
- Sirlin: perfect-information games tend to "break" sooner than ones with hidden information or randomness. Double-blind choices fight solvability. — [Sirlin: Designing Yomi](https://www.sirlin.net/articles/designing-yomi) [read] [opinion: practitioner]
- Game-dev commentary: players enter a boss arena, assess the enemy's attack pattern, then "systematically exploit its weaknesses". A student prototype reports that modes against CPU actors "are often mastered when certain rules or patterns are known." Adaptive AI (enemies that start wearing helmets if you keep landing headshots) is the usual proposed fix, but skilled players can still exploit its patterns. — [Wayline: over-designed enemies](https://www.wayline.io/blog/predictability-problem-over-designed-enemies); [Wayline: stealth AI](https://www.wayline.io/blog/predictable-problem-stealth-game-ai-overhaul) [snippet] [opinion; low-quality sources]
- Counter-view: "Good AI is predictable" argues that good AI should be "interesting to engage" rather than "hard to beat", and that challenge should come from the player's imperfect information, not from outguessing the AI. — [Game Developer: Good AI is predictable](https://www.gamedeveloper.com/design/good-ai-is-predictable) [snippet] [opinion]
- Open research problem in poker AI: among equilibria, how to compute one "that optimally exploits opponent errors". Equilibrium bots are safe but do not by default read and punish a specific opponent. — [Neller, Intro to CFR](https://cupola.gettysburg.edu/csfac/19) [snippet]

### Inferences
- [opinion] A dominant strategy appears when the best response does not depend on anyone else's choice: puzzles, scripted bosses, and full-information pursuit. Then exploring finds it once, and everyone copies it. This matches the parametric/strategic line in the SEP.
- [opinion] A human opponent who picks the counter turns every fixed plan into a losing plan within a few rounds (layer 1 of yomi). That forces mixing, and the mix is spread across the authored options. This is where "high coupling between players" pays for "low content".
- [opinion] Even a "solved" hidden-information game keeps varying, because its solution is a set of odds. An equilibrium bot (like Cepheus) is unbeatable but does not read you, so playing it lacks the yomi layer. A human is beatable but reads you, and that is the source of the mind game. For friendslop, the other humans are the AI.
- [opinion] Adaptive AI moves a fixed environment partway toward an opponent, but its adaptation rule is itself fixed, so it can be learned (one level up). Humans change their rule too.
- [opinion] Design check for a co-op game: list each player's choices and ask "does my best choice change depending on what a teammate or opponent just chose?" If no, that node is a puzzle and will be solved. If yes, and the choice is hidden or simultaneous, it will keep producing variety.

### Gaps
- I found no rigorous study that measures how fast players solve a scripted AI versus a human opponent. The available sources are blog and opinion pieces.
- Libratus and Pluribus (no-limit poker AIs) were not checked in this pass.

## 5. Bluffing (poker, Liar's Dice): why hidden information plus a human reader creates depth

### Takeaway
Bluffing is not just psychology. Von Neumann and Kuhn showed that in even the simplest poker models, optimal play requires betting some of your weakest hands. If you bet only strong hands, your bet reveals your hand and earns nothing. Hidden information turns your own hand into the "hiding spot" and your bet into a signal that has to be noisy. A human reader adds a second, exploitative layer (tells, history) that the formal model leaves out.

### Cited Findings
- Von Neumann and Morgenstern's *Theory of Games and Economic Behavior* (1944) gives a large section to bluffing in simplified poker. It notes that bluffing is practised by all experienced players. — [arXiv 0901.3365, "The emergence of bluff in poker-like games"](https://arxiv.org/pdf/0901.3365) [snippet]
- In von Neumann's model (each player antes 1), player I's optimal plan is to bet with hands below a cutoff a or above a cutoff b and check in between. In other words, bet the strongest hands and bluff with the weakest, not the middle ones. The game's value is 1/9. — [Ferguson & Ferguson, UCLA](https://www.math.ucla.edu/~tom/papers/poker2.pdf); [arXiv 2407.16155](https://ar5iv.labs.arxiv.org/html/2407.16155) [snippet]
- Kuhn showed that in a simplified poker game the optimal strategy uses randomisation, and that bluffing, which seems to come from human psychology, is game-theoretically optimal. — [arXiv 0901.3365](https://arxiv.org/pdf/0901.3365) [snippet]
- In a three-player Kuhn poker variant, the third player bluffs at equilibrium for most pot sizes above 2. When the pot is 2 or less, the equilibrium is unique and trivial (no bluff). — [arXiv 1704.08124](https://arxiv.org/pdf/1704.08124) [snippet]
- Liar's Dice: the one-die-each version is small enough to solve exactly with linear programming, but that method does not scale to multiple dice. For full two-player Dudo (a Liar's Dice variant), standard counterfactual regret minimisation (CFR, the main method for hidden-information equilibria) "proves impractical". Neller and Hnath reached an approximate equilibrium for the first time by merging information sets. — [Towards Data Science: Liar's Dice by self-play](https://towardsdatascience.com/lairs-dice-by-self-play-3bbed6addde0/); [Neller & Hnath, Dudo](https://typeset.io/pdf/approximating-optimal-dudo-play-with-fixed-strategy-41layck1j0.pdf) [snippet]
- Compton on poker: "In Poker you never know what your opponents have," so reads based on behaviour and past play matter. — [Game Developer: Know Thy Enemy](https://www.gamedeveloper.com/design/know-thy-enemy-designing-for-yomi-in-games) [read] [opinion: practitioner]

### Inferences
- [opinion] Bluffing is hide-and-seek on information. Your hand is the hider. The opponent's call/fold is the seeker's guess. If your bet pattern is pure (bet = strong), the seeker always finds you. The equilibrium mixes bluffs into bets so that every bet is ambiguous. The same indifference logic as matching pennies applies.
- [opinion] Stakes control whether bluffing exists at all: in three-player Kuhn, a pot of 2 or less leaves no bluff. A design knob: if lying costs more than it can win, players stop lying and the mind game dies. Reward size has to make the bluff worth it.
- [opinion] Tiny rule sets with hidden information get hard to solve fast (Dudo needed special methods), while staying easy to learn. That is a good ratio of depth to rules.
- [opinion] Human readers add what the formal model leaves out: voice, hesitation, history, table talk. In a friendslop game with proximity voice, every player is a live source of tells and a live tell-faker. That is coupling between players with no authored content.
- [opinion] Liar's Dice-style claims ("I have X") are a cheap verb to add: one claim plus a challenge, resolved against hidden state. It needs hidden private state per player and a cost for being caught.

### Gaps
- Exact Kuhn poker bluff frequencies (my background knowledge: player 1 bluffs the Jack at a rate between 0 and 1/3) were not confirmed from a source.
- Von Neumann's 1944 text was not read directly; the cutoff and value details come from later papers.
- I found no academic study measuring how much reading human tells adds over equilibrium play in poker or Liar's Dice.
