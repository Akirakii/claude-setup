# Idea loop run 1 (2026-11-10, 20:35–~21:40, AFK)

Skill `~/.claude/skills/generate-ideas` (built at the start of this run). Gates: `checks.md`.
Research behind the new gates: `research/player-interaction.md`, `research/routine-failure.md`.

## Round 1: 6 methods, 48 ideas + 6 anchors (create 20:48–21:01, check 21:01–21:16)
| Method | Pass of 8 | Stopped at |
|---|---|---|
| F people handling people (lifeguards, stunt crews, crowd surfing) | **3** | G 3, R 1, F2 1 |
| B moments friends retell | 2 | G 3, R 3 |
| A action and answer (random act × answer pairs) | 2 | P 1, F5 1, G 2, R 2 |
| D shared goal, private reason | 2 | G 4, R 1, N 1 |
| E crossover of the best earlier ideas | 1 | P 1, G 2, R 4 |
| C plan breaker first | 0 | G 2, R 5, F5 1 |
| Anchors (Bull Relay, Striking Gang, Megalith Haul, Blind Spot, Shove Crew, Cage Eyes) | **0 of 6** | P 1 (Megalith Haul), G 3, R 2 |

- **The new gates are much harder.** No earlier idea survives them, including the tournament's best
  (Bull Relay, Striking Gang). Megalith Haul fails the player-with-player gate, as the user sensed.
- **10 of 48 pass with no ✗; none passes with no ~.** Where ideas stopped: the co-op gate 19 (by round 5
  one end only waits or obeys), no fixed plan 18, player-with-player 3.
- **Main killer of "no fixed plan":** about 12 ideas share "the threat hunts whoever holds / did / is most X".
  One lookup line beats it ("hand it to whoever is farthest", "rotate").
- **Raters agreed on 75% of shared checks** (lower than the tournament's 86–89%: the new tests take more
  judgment).
- **Novelty is mostly unchecked:** the session's web search budget (200 calls shared by all agents)
  ran out at the start of this round; 9 of 54 novelty rows were web-checked, the rest are memory.

## Best ideas
| Idea (method) | Rule | Weak spot |
|---|---|---|
| **Hooked on Friends** (A) | Your grapple hook sticks only to teammates; when it lands, whichever of you is braced stays put and the other is reeled in. | every formula check ✓ (one rater); novelty ~ (Dota's ally hooks, Heave Ho); lag on the brace read. Same core came from 3 methods (Hookline, Friend Hooks) |
| **Tread** (F) | In the water you push a named friend up for a breath, which pushes you under; air only comes from friends. | R ~ and F6 ~ |
| **Hookline** (D) | Your hook only sticks to friends; the hooked friend has one second to brace (you fly to them) or let go (they fly to you). | duplicate family of Hooked on Friends |
| **Swap Coats** (E) | You can't change your own clothes, only trade one piece with a friend you touch, and each guard hunts the look it last saw commit a crime. | F2 ~ (3 extras), G ~, R ~ |
| **One Take** (F) | A punch at a named friend only sells on film if they throw themselves back within half a second and the camera can't see the gap. | lag risk; F2 ~, F5 ~ |
| **Spoon-Fed** (D) | You can't eat what you pick up; you stuff it into a friend's mouth, and they get its power for 5 seconds. | F1 ~, F2 ~, R ~ |
| **Hush Stone** (A) | A blind beast hunts the loudest voice; the crew's one hush stone, thrown at a friend, silences them until they throw it on. | F1, F2, F4 ~ |

## Improve (done 21:18)
- **Sharpened gates** in `checks.md`: P gets a 4th question, "still two-way by round 5" (moves the top
  failure to the first gate, as the user asked); R gets a 5th, "no lookup line / safe spot / hunts-the-holder".
- **Failure research:** no new web search was possible (budget out). Used the two research files plus
  one search on Alien: Isolation's AI: a director that knows where players are, pacing a monster that must
  search for them ([Game Developer](https://www.gamedeveloper.com/design/the-perfect-organism-the-ai-of-alien-isolation)).
  That is a low-content answer to "the threat is a lookup line" [snippet, not read in full].
- **Round 2 methods, ready to run:** keep F, B, A, D; drop C (0/8) and E (1/8). New:
  - **Two-sided information:** each act-answer pair where the answerer knows something the actor
    doesn't, revealed during the round, so neither end can just obey.
  - **Searching threat:** a threat that must find the players from what they do to each other (noise,
    light, touch), paced by a simple director, with no safe spot.

## Round 2: 4 methods × 6 ideas + anchors (create 21:19–21:30, check 21:29–21:37; no novelty step, search budget out)
| Method | Pass of 6 | Stopped at |
|---|---|---|
| Two-sided information (new) | **2** | P 1, F2 1, R 2 |
| People handling people (rerun) | 1 | P 3, R 2 |
| Action and answer (rerun) | 0 | P 2, F2 1, R 3 |
| Searching threat (new) | 0 | P 2, R 4 |
| Anchors (round 1's best 3 + Megalith Haul) | 0 of 6 checks | P 2, R 4 |

- **Round 2 did worse than round 1** (3/24 = 13% vs 10/48 = 21%), because the gates got stricter faster than the
  methods improved. Round 1's best, Hooked on Friends, now fails R ("carrier hooks the..." settles into a lookup line).
- **The searching-threat fix failed:** threats that go to the last noise are beaten by a decoy noise (0/6).
- **Two-sided information helped:** 2 of 6 pass. Best:
  - **Glowball:** whoever holds the orb sees only the shadow hounds; only players without it see the goal rings;
    a catch flips who sees what (~ on F6, R).
  - **Glare Ice:** two touching players who both press push apart; each one's facing sets where the OTHER slides;
    nobody can read the ice near themselves (~ on F2, F6, G, R; lag risk).
  - **Push-Off** (people handling people): with dead jetpacks, two crew who both press kick off each other and fly
    apart; nothing else changes your course (~ on F5, G, R; lag risk).
- **R ("no fixed plan") is the wall:** across both rounds almost no idea got R ✓. Raters agreed on only 67% of
  shared checks this round and added their own rules ("two weak P answers = ✗"), so the gates as written are
  judgment-heavy.

## Where this leaves the search (Claude, opinion)
- Every simple threat rule has a one-line answer, so "the threat changes the plan" keeps failing. The research's
  other route is untried: **something dealt or revealed each round that changes which plan is best** (a deal, a
  layout, a private stake), with players acting on each other. Two-sided information was the closest to that.
- The R gate may be too hard to judge by reading alone (low agreement). That is where only play would tell,
  which the user parked for now.
