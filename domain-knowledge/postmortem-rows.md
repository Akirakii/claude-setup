# Postmortem rows (all projects)

One row per problem or thing that went right, written by the `project-postmortem` skill, so patterns across projects can be counted.
Categories come from `~/.claude/skills/project-postmortem/categories.md`.

| Project | Date | Went right? | Category | Sub-type | Item | Quote (user's words) | Source |
|---|---|---|---|---|---|---|---|
| Moonsick | 2026-11-16 | ❌ | Design | core choice has one answer | cure at the first sign always won; holding every item countered the game | "the game can be countered by having all people around the sick one with all items in hand" | projects/moonsick/postmortem/POSTMORTEM-2026-11-16.md |
| Moonsick | 2026-11-16 | ❌ | Design | no reason to lie | co-op where everyone wins left no payoff for bluffing; Claude's "betraying never pays" rule removed it | "there is no room for lying effectivly" | same |
| Moonsick | 2026-11-16 | ❌ | Design | premise with no precedent | co-op win-together + bluff: research found no game that does both | "this game should be all about interaction of bluff.. and cooperating for survival" | same |
| Moonsick | 2026-11-16 | ❌ | Prototyping | core never played with people before builds | 5 h AFK build, then 2 h pass, then 2 days polish, before any human test | "i dont understand what to do in the game" | same |
| Moonsick | 2026-11-16 | ❌ | Communication | Claude followed literal request over its own evidence | readability pass and movement work while critics pointed at the rules | "i still have the same issue.. nothing has improved" | same |
| Moonsick | 2026-11-16 | ❌ | Testing | bots can't test bluff | all checks by critics, sims and bots; bots did the player's job | — | same |
| Moonsick | 2026-11-16 | ❌ | Design | pivot dropped a pillar unflagged | the race fixed the lie motive by dropping co-op | "this is basically pvp no? is this no longer a friendslop?" | same |
| Moonsick | 2026-11-16 | ✅ | Testing | critics with numbers | critics found the core flaw before each build | — | same |
| Moonsick | 2026-11-16 | ✅ | Design | user's head-simulation | the user found real holes fast in their head | "im right now simulating in my head and i notice that locking is a boring mechanic" | same |
| Moonsick | 2026-11-16 | ❌ | Planning | foundation patched, not dropped | 13 of 14 critic rounds on the first foundation's rules found a new best move; each was fixed on paper and the next round found another | "should i start the game from scratch? everything is wrong and not working.." | same, section 8 |
| Moonsick | 2026-11-16 | ❌ | Communication | Claude argued against the user's restart | on Nov 12 Claude answered "No, don't start from scratch" and offered a friends test the user couldn't run; three more days went into the same foundation | "lets start fixing one thing at a time" | same, section 8 |
| Mustache Madness | 2026-11-16 | ❌ | Design | core choice has one answer | more allies made the game easier, and nothing pulled against it | "when you have lots of allies, the game is easy" (Jul 16) | light pass: the user's messages in `~/.claude/history.jsonl` |
| Mustache Madness | 2026-11-16 | ❌ | Design | core choice has one answer | exponential income removed the choice gems were for | "gems are for sacrificing and taking decisions one over the other.. but right now it feels like player needs to keep up with all the income" (Oct 25) | same |
| Mustache Madness | 2026-11-16 | ❌ | Unrealistic scope | fun only in the first stage | the later stages never held up, after about 6 months of loops | "game right now it is good at the early game.. shouldnt last like that for the second stage and third stage" (Oct 20) | same |
| Mustache Madness | 2026-11-16 | ✅ | Design | fun in the player's own action | the only "fun" verdict from play in any of the eight games | "building and bed is the most fun i had.. more than the other systems" (Sep 9); "it was fun" (Oct 20) | same |
| Dungeon Pets | 2026-11-16 | ❌ | Design | rules carried over from the dropped game | "creatures that fight for you" came over from Mustache Madness, with its more-units-is-easier flaw | "a dungeon crawler but with creatures pokemon like and they fight for you" (Oct 28) | same |
| Assemblia | 2026-11-16 | ❌ | Design | core choice has one answer | the rules gave nothing to decide | "I feel these ruels doesnt have strategic value" (Nov 1) | same |
| Assemblia | 2026-11-16 | ❌ | Design | rules carried over from the dropped game | the army was kept, and a cap on it was turned down | "I just to make a first person with walking army fun. that is my main intention."; "i don agree with cap, no small army" (Oct 31) | same |
| Assemblia | 2026-11-16 | ❌ | Unrealistic scope | deep single-player strategy | dropped for scope before a core existed | "i want a more feasable game that works with less than 1 year of development" (Nov 1) | same |
| Hordeline | 2026-11-16 | ❌ | Design | two known loops glued together | a crew keeping one machine running, plus Vampire Survivors upgrades | "how these games make the one machine running fun? ... right now it is not"; "i dont see that working" (Nov 2) | same |
| Red Button | 2026-11-16 | ❌ | Design | fun placed in authored content | surprises, events, items and story paths each had to be written | "it required too much loops and found nothing" (Nov 9) | same |
| Red Button | 2026-11-16 | ❌ | Testing | can't tell communication from gameplay | — | "i dont know if it is not fun because of lack of good visual communication and feedback? or is it because the gameplay?" (Nov 6) | same |
| Pet the Cat | 2026-11-16 | ❌ | Design | rules carried over from the dropped game | the button swapped for a cat; Claude carried "hands are scarce" over from Red Button (its design doc) | "lets replace the button but with a cat" (Nov 7); "i dont like this one" (Nov 7) | same, and `projects/pet-the-cat/design.md` |
| Deathly Reality Show | 2026-11-16 | ❌ | Design | side-by-side work counted as co-op | Claude's minigames needed no cooperation | "were too simple and easy and requires no cooperation at all" (Nov 8) | same |
| Deathly Reality Show | 2026-11-16 | ❌ | Design | rules carried over from the dropped game | minigames kept from Red Button and Pet the Cat | "i dont like this one.. use the same instructions" (Nov 7) | same |
| the five co-op games | 2026-11-16 | ❌ | Testing | judged solo | Hordeline, Red Button, Pet the Cat, Deathly Reality Show and Moonsick: no message in the history reports a play with friends (assumed from absence) | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Design | core choice has one answer | power grew with pack size and the pack was unlimited, so taking every creature was always right | — | projects/dungeon-pets/postmortem/POSTMORTEM.md |
| Dungeon Pets | 2026-10-31 | ❌ | Design | work grows with every unit | each creature had its own diet, evolution, gear and HP, so managing them one by one was a chore | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Design | the player can do the work | the player's own fighting won fights, so the pack's build stopped mattering | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Feature creep | layers added before the core was fun | relics, gear, evolution, reactions, threats, eggs and upkeep stacked on; bookkeeping, not decisions | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Design | camera hides where the decisions are | first person showed a slice of a pack that is read from above; the screen couldn't be read | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Planning | art before the core was proven | several Meshy redesign rounds ran into rig and proportion problems and were dropped | — | same |
| Dungeon Pets | 2026-10-31 | ❌ | Testing | bots can't measure fun | careless-vs-careful bot runs differed by +0.8 floors and couldn't see clarity or tedium; the user's playtest found both at once | — | same |

## Comparison across the eight games (2026-11-16, light pass)
Asked by the user: "what can we learn from those and what makes each one different".
Light pass: rows above come from the user's own messages and each project's docs; no fresh agents judged the decisions, and Claude knows the endings.
Only Moonsick and Dungeon Pets have a full postmortem.

### Three sets of rules, eight themes (checked from the pitches; the grouping is Claude's)
| Family (the rules) | Games, in order | What each new game kept | The one best way to play | The user's words |
|---|---|---|---|---|
| an army that fights for you | Mustache Madness (Jun–Oct), Dungeon Pets (Oct 29–31), Assemblia (Oct 31–Nov 2) | the army; more units = more power | get more units | "when you have lots of allies, the game is easy" (Jul 16); "player is too strong and desnt ned to make any decisiosn at all" (Oct 31) |
| friends keep one shared thing going, with events or minigames | Hordeline (Nov 2), Red Button (Nov 3–6), Pet the Cat (Nov 7), Deathly Reality Show (Nov 7–8) | the shared thing, then the minigames | everyone does the same simple job side by side | "were too simple and easy and requires no cooperation at all" (Nov 8) |
| friends against a sickness, then against each other | Moonsick versions 1–3, then version 4 (Nov 11–16) | versions 1–3 kept the sickness rules | play safe; then never help | "the game can be countered by having all people around the sick one with all items in hand" (Nov 14) |

- Counted with the sub-types: "rules carried over from the dropped game" 4 of 8 games (Dungeon Pets, Assemblia, Pet the Cat, Deathly Reality Show), and Moonsick did it between its own versions; "core choice has one answer" 4 of 8 in the user's words (Mustache Madness, Dungeon Pets, Assemblia, Moonsick).
- The link from Hordeline to Red Button is weaker: the user's "a simple incremental action with friends.. but gets exponentially chaotic" (Nov 2) came right after Hordeline (assumed).
- The condition that didn't fail: only Mustache Madness got a "fun" verdict from play. It differs from the other seven in three ways at once (the user wrote its rules over months, it is solo so the user could judge it alone, it had months of loops), so the eight can't say which of the three mattered.
- The seven games after it took 19 days (Oct 29 to Nov 16), 1 to 5 days each, and the first rules of most were written by Claude in one AFK night from a short pitch (checked for Hordeline, Red Button, Pet the Cat, Deathly Reality Show, Moonsick; Dungeon Pets partly).

### What Claude takes from it (no verdict from the user yet)
- A new theme on kept rules fails the same way: the flaw lives in the rules, and the rules were the part that carried over.
  In the user's chain: the same logic gives the same actions, so the same feelings, whatever the fantasy and aesthetic.
- Sketch: before a new pitch is built, Claude names what it keeps from the last game's rules and whether the last game's flaw lives in that part.
- Limits: one fun verdict in eight, so this shows what to stop repeating, not what works; the families are Claude's grouping, made knowing the endings.

### The lesson chain (2026-11-16; the user: "i thought i learned from previous failure X so i did Y.. and did that several times")
Light pass from the user's messages; "turned the complaint around" is Claude's reading.
| From | Complaint | Lesson taken (Y) | Next game | Lesson held? | How the next one failed |
|---|---|---|---|---|---|
| Mustache Madness | too big, 6 months of loops | start tiny: "just the basics... for iterating ideas" | Dungeon Pets | ✅ small | on the kept part: the army, more units = easier |
| Dungeon Pets | no decisions, unreadable, a chore | rules per type, top-down, player supports the army | Assemblia | ✅ readable | "no strategic value"; scope over a year |
| Assemblia | deep solo strategy takes years | cheap co-op, friends make the fun | Hordeline | ✅ scope | co-op glued onto a solo loop; "i dont see that working" |
| Hordeline | too many parts to make one machine fun | one simple shared action (one hub) | Red Button | ❌ the user later: one hub "required too much loops and found nothing" | the fun moved into written surprises |
| Red Button | narrator and shop, confusing | "no narrator... no shop", just keep the cat calm | Pet the Cat | ✅ clear | nothing left to decide; "i dont like this one" |
| Pet the Cat | one action is too thin | many minigames with a host | Deathly Reality Show | ❌ | "too simple and easy and requires no cooperation at all" |
| Deathly Reality Show | no cooperation; feels like minigames | the formula: fun comes from friends, so pick the idea with the most acting on each other (bluff) | Moonsick | ❌ in play: honest play won | nobody had a reason to lie |
| Moonsick 1–3 | nobody has a reason to lie | everyone wants the same prize | Moonsick 4 | ✅ reason to lie | "this is basically pvp no?" |

- 5 of 8 lessons held: each fixed the complaint it was made for.
- 8 of 8 next games failed on something the lesson didn't cover: a kept part (2), or a new gap the fix opened (6).
- Every lesson came from one failure and turned its complaint around; none was checked before a game was built on it.
- Claude's reading (no verdict yet): the lessons were right and too narrow. Each said what to remove; none said what makes the game fun, so removing the last flaw left the next one. The only positive evidence in eight games is Mustache Madness's early game.

### The method behind the chain (2026-11-16; the user: "you are looking at the outcome. not at the methodology i followed")
The loop the user ran eight times (checked from the messages; the reading is Claude's, no verdict yet):
| Step | What was done | Changed across the eight games? |
|---|---|---|
| 1. Idea | a pitch from imagination: a situation and a job | ❌ (the choice was added to the idea line on Nov 11) |
| 2. Rules | filled in fast, mostly by Claude in one AFK night since Dungeon Pets | ❌ |
| 3. Judge | the user plays alone | ❌ |
| 4. Lesson | one lesson from one failure, the complaint turned around | ❌ |
| 5. Apply | a whole new game, so many things change at once | ❌ |
| 6. Tools | each failure also added a filter: anti-pattern docs, critics, the formula, checks | ✅ grew every time |
| Speed | 6 months, then 3 days, then about 1 day per game | ✅ |
- The lessons changed the game each time and never the loop: steps 1–5 are the same in all eight.
- Every lesson became a filter (what to avoid); nothing in the loop adds a positive example of what is fun.
- Step 5 changes everything at once, so no game could show whether its lesson was right.
- No step looks back: this chain is the first time a lesson was checked against the game built on it.
