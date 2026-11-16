# Shared docs (true across projects)

Long researched docs that more than one project uses, one folder per subject.
A doc lands here when it holds for more than one project (`update-domain-knowledge` skill).
Nothing here points down into a project; a project's index points up to the shared doc it uses.

## `game-patterns/`: researched patterns and anti-patterns, with sources
| Doc | What it holds | Read when |
|---|---|---|
| `gameplay-anti-patterns.md` | rules, rewards and crew anti-patterns | designing or reviewing a mechanic or reward |
| `game-feel-patterns.md` | game feel patterns and anti-patterns | adding feedback, juice, sound or movement feel |
| `visual-communication-patterns.md` | how a game shows its state and teaches without text | anything the player must read on screen |
| `ui-ux-anti-patterns.md` | UI and UX mistakes to avoid | building a menu, HUD or prompt |
| `accessibility-patterns.md` | the basic accessibility guidelines | before a build others will play |
| `demo-session-patterns.md` | demos and session shape (Next Fest demos, drop-in play) | scoping a demo or a session length |
| `discovery-patterns.md` | games where the players discover the rules | a game built on finding out what things do |
| `escape-room-patterns.md` | escape room patterns: parallel work, clues, hints | co-op puzzle rooms |
| `dialog-anti-patterns.md` | narrator and dialog mistakes | writing a narrator or spoken lines |
| `bluff-patterns.md` | what a bluff needs, the elements bluff games use, bluffing without two sides, whether co-op with bluffing exists | any lying, hiding or bluff mechanic |
| `diagnose-a-friend-patterns.md` | games where players read signs on each other or on evidence, with patterns and anti-patterns | a mechanic built on reading another player's state |
| `team-item-delivery-patterns.md` | making "bring the right thing to the right place" need more than one player | items, carrying, fetching |
| `camping-on-the-fix-patterns.md` | stopping a crew from carrying every answer and waiting | a need-and-fix loop that the crew can pre-solve |
| `teaching-what-to-do-patterns.md` | what to do when players say they don't understand what to do | onboarding, HUD, the first minutes |
| `becoming-the-monster-patterns.md` | games where a player's own character turns on the team: five patterns for "it is me, but I am not in control", and what makes losing control acceptable | a player turns, gets infected, possessed or goes berserk; any rule that takes control away |
| `gameplay-verbs-and-player-coupling.md` | the report: hidden human choices replace authored content; thirty verbs ranked; what the formula needs | checking an idea against the formula; picking a core verb |

## `game-market/`: what sells and what is cheap to make
| Doc | What it holds | Read when |
|---|---|---|
| `next-game-report.md` (+ `.html`) | what is cheap to make and still pays, for a solo dev shipping in under a year | picking the next game |
| `coop-report.html`, `trends-report.html`, `upcoming-report.html`, `playbook.html` | co-op, trend and upcoming-release reports, and the playbook, from the same research | the same |
| `friend-group-party-games.md` | 19 online party games for friend groups: numbers, why each worked or died, a scoreboard, the shared formula | scope, price, lobby and round-length calls for a co-op game |

## `game-ideas/`: the living pool of game ideas
| Doc | What it holds | Read when |
|---|---|---|
| `pool.md` (+ `pool-history/`) | every idea with its pass or fail against the formula, and older versions | running or reviewing the idea search |

## `meshy/`: making 3D characters with Meshy
| Doc | What it holds | Read when |
|---|---|---|
| `meshy-pipeline.md` | the steps from prompt to rigged model, the cost of each, and the lessons | before any Meshy generation |

## `godot/`: the engine
| Doc | What it holds | Read when |
|---|---|---|
| `godot-traps.md` | traps in navigation, multiplayer, GUT tests, rendering, UI and input, GDScript | before touching that area in a Godot game |
