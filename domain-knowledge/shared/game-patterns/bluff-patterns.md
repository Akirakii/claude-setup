# Bluff: what makes lying work in a game

What a bluff needs, the elements bluff games use, bluffing without two sides, and whether co-op with bluffing exists as a genre.
Tags: [source] = said by the linked source; [read] = Claude's reading of it; [memory] = Claude's memory, not checked; [opinion] = Claude's own.

## What the sources say makes a bluff work
1. **Three parts: a means to bluff, a reason to bluff, and a penalty both for a caught lie and for a wrong
   accusation.** Sheriff of Nottingham fits it: merchants declare their goods, the sheriff chooses to inspect
   [source: Medium, "Negotiating with Sheriff of Nottingham"].
2. **A claim that can be checked, but checking costs.** Liar's Dice: anyone can call, all dice are shown, and the
   wrong side loses dice. Coup: a wrong challenge is punished hard, so people don't challenge everything
   [source: Mechanics of Magic, Coup].
3. **One player's secret is another player's puzzle,** with many small decisions that each give a bit away
   [source: Ragusa devlog, "How to make a bluffing game"].
4. **Honest play must not always win.** A Bullshit simulation: the player who never lied won ~51%, the one lying half
   the time ~2%. A designer: if players must be reminded they can lie, the game fails [source: Medium, "The Game
   Theory of Bullshit"; Mechanics of Magic].
5. **Lies tied to bodies and places.** Among Us ties deception to where you walked and visible tasks; Clocktower ties
   it to talk [source: Scienceline; Mechanics of Magic, Clocktower].
6. **A believable lie must fit the info a role could have** [source: Mechanics of Magic, Clocktower].

## Sources
- [Negotiating with Sheriff of Nottingham](https://medium.com/game-design-fundamentals/negotiating-with-sheriff-of-nottingham-620411eceec7)
- [Critical Play: Coup](https://mechanicsofmagic.com/2021/04/20/critical-play-bluffing-judging-and-getting-vulnerable-coup/)
- [How to make a bluffing game](https://zivan.itch.io/ragusa-trade-em/devlog/402953/how-to-make-a-bluffing-game)
- [The Game Theory of 'Bullshit'](https://medium.com/game-of-theories/the-game-theory-of-bullshit-aed0872251e8)
- [Critical Play: Coup (bluff payoffs)](https://mechanicsofmagic.com/2026/04/10/critical-play-bluffing-judging-and-getting-vulnerable-coup-3/)
- [Social Science, Scienceline](https://scienceline.org/2025/01/social-gaming/)
- [Critical Play: Blood on the Clocktower](https://mechanicsofmagic.com/2026/04/10/critical-play-bluffing-judging-and-getting-vulnerable-blood-on-the-clocktower/)

## Bluffing without two sides
- **Yes, every player for themselves:** poker, Liar's Dice, Skull, Coup, Cockroach Poker. No teams, and anyone may lie
  [source: Mechanics of Magic on Coup; bluffing lists]. A designer's split: a traitor game has one liar, a bluffing
  game has everyone possibly lying [source: search summary, Crab Fragment Labs / Zatu lists].
- **Everyone wins together and still lies:** none found in two searches. Closest: Coyote (deduction and bluffing
  without needing to lie), Mantis Falls ("sometimes cooperative", 2–3 players) [source: Zatu; search summary].
- **Keeping cooperation:** a Coup redesign dropped player elimination and found cooperation came back; when surviving
  needs others to lose, everyone is an enemy [source: Mechanics of Magic, competitive analysis].
- **Lies that stick:** Truth or Die makes credibility the only currency, because lying with no lasting cost is common
  in Survivor-style games [source: Mechanics of Magic].

Sources:
- [Critical Play: Competitive Analysis, Mechanics of Magic](https://mechanicsofmagic.com/2026/04/15/critical-play-competitive-analysis-117/)
- [Critical Play: Coup, Mechanics of Magic](https://mechanicsofmagic.com/2026/04/08/critical-play-coup-6/)
- [Best bluffing games, Zatu](https://zatu.com/best-bluffing-games/)
- [Bluffing Games, Crab Fragment Labs](https://crabfragmentlabs.com/lecture-hall/bluffing-games)

## Does this genre exist?
Pieces exist; the whole thing wasn't found as a named genre in three searches.
| Nearest | What it shares | What differs |
|---|---|---|
| Semi-cooperative board games (Dawn; "grand winner" format) [source: Game Sushi] | everyone needs each other, each also for themselves | usually one overall winner, or a traitor |
| Negotiation games (Diplomacy) [source: Wikipedia] | promises aren't binding, lying is part of the game, you need alliances; lying for a short gain usually backfires | one winner or a tie, everyone against everyone |
| Survival sandboxes (DayZ) [source: Carter, Treacherous Play, MIT Press; Pasanen 2015] | each for themselves, many can survive, trust strangers, proximity voice | hours long, no structure; killing on sight became the norm |
| Hoax (1981) [source: search summary] | no teams, anyone may be lying | a card game, one winner |

Sources:
- [Semi-Cooperative Games, Game Sushi](https://gamesushi.github.io/quartz/Game-Structure/Semi-Cooperative-Games)
- [Making semi-cooperative games work, League of Gamemakers](https://leagueofgamemakers.com/making-semi-cooperative-games-work)
- [Diplomacy (game), Wikipedia](https://ipfs.ssi.eecc.de/ipns/en.wikipedia-on-ipfs.org/wiki/Diplomacy_(game))
- [Treacherous Play, MIT Press](https://mitpressbookstore.mit.edu/book/9780262046312)
- [Pasanen 2015, a critical analysis of DayZ](https://www.pelitutkimus.fi/vuosikirja2015/ptvk2015-08.pdf)
- [DayZ review, GameGeeker](https://gamegeeker.com/it/games/dayz-221100/review)

## Elements bluff games usually use
| Element | Example | Tag |
|---|---|---|
| A secret only one player has | your hand in poker, your role in Coup | [source: pattern note, VU] |
| A claim about the secret | "I'm the Duke"; cards face down called a rank (Bluff King) | [source: Coup, Bluff King] |
| A call: anyone can challenge, and the wrong side pays | Coup, Liar's Dice | [source: Mechanics of Magic] |
| Something scarce to fight over (the reason to lie) | coins, influence | [source: Ragusa devlog] |
| Public actions as evidence | each policy in Secret Hitler; where you walked in Among Us | [source: search excerpts; Scienceline] |
| The secret comes out slowly, so old lies get caught | revealed cards over a game | [source: Raph Koster] |
| A vote or accusation that removes someone | Mafia/Werewolf; accusation cards in Salem 1692 | [source: game bootcamp module] |
| Lying about what you'll do, not what you have | Diplomacy | [source: pattern note, VU] |

Failure seen: players who play safe instead of bluffing weaken the game [source: Mechanics of Magic student post].

Sources:
- [Bluffing pattern, VU](https://www.math.vu.nl/~eliens/demo/pattern-bluffing.html)
- [Dishonest opponents, Raph Koster](https://www.raphkoster.com/?p=12507)
- [How to make a bluffing game](https://zivan.itch.io/ragusa-trade-em/devlog/402953/how-to-make-a-bluffing-game)
- [Bluff King rules](https://rulespal.com/bluff-king/rulebook)
- [Social deduction module](https://seanking11.github.io/gamebootcamp/modules/37-social-deduction)
- [Hidden Roles](https://gamesushi.github.io/quartz/Uncertainty/Hidden-Roles)
- [Critical Play, Mechanics of Magic](https://mechanicsofmagic.com/?p=58926)

