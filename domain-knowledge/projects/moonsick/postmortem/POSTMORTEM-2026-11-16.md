# Moonsick postmortem (2026-11-16)

Method: the `project-postmortem` skill. Tags: (checked) = read in sessions or docs; (assumed) = Claude's reading.
Evidence: the user's messages from 25 sessions (Nov 11–16), transcripts cut at 5 key decisions, `critic-core-r1.md`, `questions.md`, `redo-ideas.md`.
Caveat: Claude ran these sessions and had already given its own explanation in chat before this postmortem, so the decision verdicts come from fresh agents, and a last agent checks the whole.

## Summary
(written last; see the end)

## 1. What was intended (user's words, per version)
| Version | Date | Intent (checked) |
|---|---|---|
| v0.1 "Full Moon" | Nov 11 | "a group of friends in a mansion... a random player becomes a legendary creature... symptoms are always different and difficult to analyse... you have to diagnose your friends before they become a legendary creature, and find the cure"; later "how to make this game more of a game of bluff?" |
| step 1 (cut-down v0.1) | Nov 12 | after "i dont understand what to do": fewer rules, big body signs, little UI, slower bots; werewolf only |
| bluff core | Nov 14 | "this game should be all about interaction of bluff.. and cooperating for survival"; "bluffing should be the core mechanic of the game now" |
| v2 redo, the race | Nov 15 | "everyone wants to transform into a werewolf and wants to avoid others from transforming first"; core line "Grow into the werewolf first while everyone tries to shave you back to human" |
| open question | Nov 15 | "this is basically pvp no? is this no longer a friendslop?" |

## 2. Rival explanations (written before the decision verdicts)
Claude had already read the user's messages for this session's chat answer, so these weren't written blind (checked: the earlier chat answer exists).

| # | Explanation | Must show up if true | Would show up only if true |
|---|---|---|---|
| R1 | **No moment where helping and betraying are both tempting**; each version had one dominant side (Claude's chat answer) | a finding that honesty always wins in v0.1, and that helping has no payoff in v2 | the user naming both problems back to back |
| R2 | **Too much at once** (user's guess) | playtest complaints about too many rules or too much UI | cutting parts fixing the confusion |
| R3 | **The fun was never tested before big builds**: the core was played for the first time after a 5-hour AFK build of a full game | first play came after the full build; each pivot was designed in chat, then built | a small prototype of the core never being made before adding content |
| R4 | **The game couldn't show its state** (Claude's known visual-teaching weakness), so the core was never really seen | complaints about not seeing or reading what's happening | the user still lost after readability fixes |
| R5 | **The core was a puzzle with a lookup answer**: diagnosis + cure is solvable, so there's nothing to play once you know the table | the critic finding one best strategy; "the game can be countered by having all items in hand" | the fix needing a rule that hides or randomizes the answer |

## 3. Timeline (checked unless tagged)
| Date | Event or decision | Proposed by | User's reaction |
|---|---|---|---|
| Nov 11 | the idea pitched: diagnose friends, cure, hold or knock out | user | — |
| Nov 11 | long Q&A on how to lose, bluff motives, punishing a creature that won't hunt | user asks, Claude answers | "how to make hunting more rewarding? since not hunting is more rewarding" |
| Nov 11 | **D1: build the whole game in Godot AFK, ~5 hours** (3 creatures, symptoms, tools, bluff, voice, replay, network) | user ("create the game in godot, from start to finish... like 5 hours") | "also running away from the one to transform feels a lot more safer than trying to safe them" (sent during the build) |
| Nov 12 | **first play of the core** | — | "i dont understand what to do in the game" |
| Nov 12 | **D2: a 2-hour AFK readability, feel, map and Meshy pass** | user | "i still have the same issue.. nothing has improved"; 13 points incl. "dont know any choices i have to choose or make" |
| Nov 12 | core proposal + critic: "the kept choice is dead: give on the first sign wins every time" (critic-core-r1 S1) | Claude | — |
| Nov 12 | "should i start the game from scratch? everything is wrong" | user | — |
| Nov 12–13 | **D3: fix one thing at a time**: movement, no UI, werewolf only, hands, holding, symptoms and items, Meshy models | user ("lets start fixing one thing at a time"), Claude's picks inside | movement tuning feedback; "these characters are so bad" |
| Nov 14 | "the game can be countered by having all people around the sick one with all items in hand"; "there is no real fear"; "our game is binary" | user | — |
| Nov 14 | **D4: make bluff the core**, simulate rounds of rules | user | "i dont think that game can be fun to play"; "it doesnt sound like a game of bluff" |
| Nov 15 | **D5: redo from scratch**: everyone wants to turn; then the race + hunt | user | many tuning requests; "this is basically pvp no? is this no longer a friendslop?" |

## 4. The five key decisions, judged by fresh agents (each read only up to its decision)
| Decision | Reasonable then? | Missing information cheap to get? | Did it work? |
|---|---|---|---|
| D1: build the whole game AFK, ~5 h | partly: fine as a code bet, but every check was on paper and the core is bluff between humans, which a solo AFK run can't test | ✅ a 30-min paper playtest with sign cards and one friend; the existing cure-odds script already hinted that guessing at once wins (0.77 vs 0.76) | ❌ "i dont understand what to do"; core choice dead |
| D2: a 2-hour readability, feel, map and Meshy pass | partly: what the user asked for, but "don't understand what to do" fits two causes (can't read it, or no choice worth making) | ✅ one question: "what moment didn't you know what to do?"; counting help vs flee in the existing bot traces | ❌ "nothing has improved"; "dont know any choices i have to choose" |
| D3: fix one thing at a time, starting with movement | partly: cutting scope is right, but the only checked finding (critic S1, "point 12 is a rules problem") was a rules flaw movement can't touch; Claude's own last advice was "freeze, build the smallest core, test with 2–3 friends" | ✅ the user's answer to "the idea or how it's shown?" (asked, never answered); rerunning the critic's sim on rule tweaks | ❌ 2 days on movement, UI, hands, holding, items, models; then the same core flaw |
| D4: make bluff the core | weak: the premise gave nobody a reason to lie ("a sick friend who wants to live always gains from telling the truth"), and research found no co-op game where everyone wins together and people still lie | ✅ a playtest of the current build; designing the private symptoms bluff needed first | ❌ "i dont think that game can be fun to play" |
| D5: redo from scratch | partly: the restart was reasonable; the race fixed "no reason to lie" but dropped the co-op the user chose, with no sign the trade was made on purpose | ✅ one check against the pillar: "is this still co-op friendslop?" | ❌ "this is basically pvp no?" |

All five agents named the same cheap step that was skipped: **a test with real people before the build** (checked: every agent's answer to question 3).

## 5. What went wrong, what went right (after the independent check)
### Rival explanations tested
| # | "Must show up" evidence present? | Verdict |
|---|---|---|
| R1 (one dominant side) | ✅ "a sick friend who wants to live always gains from telling the truth" (D4); "no motive to lie" (critic r1); then "this is basically pvp" | **survives** |
| R5 (the core was a lookup puzzle) | ✅ "countered by having all people around the sick one with all items in hand"; give-first wins (r4: 0.77 vs 0.76 before the build; core-r1: 0.90 vs 0.74 after the step-1 cuts) | **survives**, separate from R1: it needs hidden or random information, not a motive |
| R3 (the fun was never tested before big builds) | ✅ first play came after the 5-hour build; no test with real people ever happened | **survives**, strongest |
| R2 (too much at once) | ✅ "too many UI elements"; ❌ cutting parts didn't fix it | **partly**: explains the confusion, not the failure |
| R4 (the game couldn't show its state) | ✅ readability complaints; ❌ "no choices" stayed after the readability pass | **partly**: it hid the rules problem |

### Went wrong (checked unless tagged)
1. **The premise asked for something no game the research found does:** co-op where everyone wins together, plus bluffing (D4 research: "I didn't find one where everyone wins together and people still lie"). It went unquestioned until D4.
2. **Nobody had a reason to lie, partly because of a rule Claude proposed.** Claude suggested "betraying must never pay more than curing" on Nov 11, the user agreed, and later Claude called it "your rule" (checker, D1 and D4 transcripts). That rule removes the payoff of a lie.
3. **The core was a lookup puzzle:** curing at the first sign won, and holding every item countered the game.
4. **Claude built before anyone played the core.** Claude's own advice before D1 was to build only "after the first 3-human test proves the night is fun", and it ran the 5-hour build anyway. When the user skipped the open questions ("analyze it yourself"), Claude settled them alone.
5. **Claude followed the literal request over its own evidence.** D2: a readability pass when the bot traces pointed at the rules. D3: Claude advised "freeze, build the smallest core, test with 2–3 friends", asked "the idea or how it's shown?" once, got no answer, then built movement, UI and Meshy models.
6. **No test with real people at any point.** The checks were critics, simulations and bots. The bots can't bluff, and in practice nights they did the human's job (core-r1 S3: "the bots leave the human nothing to do").
7. **The critics flagged the core every time, but not always as severe.** r4 rated it "nothing severe" while its own numbers showed guessing at once tied with checking, and Claude accepted that.
8. **The redo traded the co-op pillar for a lie motive, unflagged.** The race gives a reason to lie and makes the game PvP ("this is basically pvp no?"); evidence that helping has no payoff in v2 is only that remark (assumed beyond it). The critic brief for the bluff build checked the betrayal pillar, not co-op (checker's reading, assumed).
9. Claude's early enthusiasm ("beats everything in the pool") may have pushed the build forward (assumed, checker's reading).

### Went right
- The critics found the flaw early and with numbers (checked: r1–r4, core-r1).
- The user's own head-simulation found real holes fast: locking is boring, killing beats curing, it's PvP (checked).
- Claude's D3 advice (freeze, smallest core, friends test) was right (checked); it just wasn't followed.
- Pivots were quick, and the existing movement carried into v2 (checked: redo-ideas.md, "keep the existing movement").

## 6. The independent check
A fresh agent read the intent, rivals, timeline and verdicts with speakers hidden, wrote its own answer, then compared.
| Its finding | Settled |
|---|---|
| R1 and R5 shouldn't be merged | ✅ split |
| the "betraying never pays" rule was Claude's proposal, left out | ✅ added as cause 2 (checked: the user's reply "i totaly agree with betraying must never pay off more than curing them") |
| "the critics found it every time" overclaims; r4 said "nothing severe" | ✅ cause 7 |
| causes were written with no actor; Claude ran the builds | ✅ causes 4 and 5 name Claude |
| missing: the premise itself; bots doing the player's job | ✅ causes 1 and 6 |
| "movement carried over" unverified | ❌ kept: checked in redo-ideas.md, which the checker didn't have |
| 0.90 vs 0.74 and 0.77 vs 0.76 not reconciled | ✅ both shown: different critics, different versions |

## 7. Lessons
1. **Play the core with real people, in the cheapest form, before any build.** A 30-minute paper test with one friend was available before D1, and every judge named it.
   **Rejected by the user (Nov 16):** a stripped test doesn't work for them. One friend can't judge the idea without content, models and movement feel, friends are 14 hours away, and their earlier stripped prototypes failed anyway. The judges didn't know these limits.
2. **When Claude's own advice says "test first", Claude doesn't start the build without saying so plainly and getting a yes.**
3. **When the user says "I don't understand", ask which moment before any pass.**
4. **Check each pivot against the chosen pillars out loud** (here: co-op friendslop).
5. **A rule Claude proposes stays tagged (Claude)**, so it doesn't later read as the user's own.

## 8. Second pass on the lessons (2026-11-16, later session)
Asked by the user: "what can I really learn from it?", after lesson 1 was rejected.
Caveat: Claude wrote this pass alone, knowing the ending; no fresh agent checked it.
The counts come from each critic file's severe headings and its dominant-strategy section, not from a full read of every file.

### The critic rounds on the rules of the first foundation (versions 1–3), in order (checked)
"Best move" = one strategy that always wins, or a move that costs nothing.
Times are local. The hands and layout critics are left out (they judged other things).
| # | Critic file | When | Best move it found |
|---|---|---|---|
| 1 | full-moon critic-r1 | Nov 11 22:16 | "kitchen clinic": all items in one room, everyone in a ring, feed whatever the item test shows |
| 2 | full-moon critic-r2 | Nov 11 22:31 | "walking pharmacy": the crew carries every cure and feeds in turn at stage 1; a feed is a free test |
| 3 | full-moon critic-r3 | Nov 11 22:48 | "the stated choice has one answer" (stepped odds); every cure and tool in hand at 6 players |
| 4 | full-moon critic-r4 | Nov 11 23:00 | none severe ("close to buildable") |
| 5 | full-moon critic-r5 | Nov 11 23:22 | turning and starving on purpose buys a free ghost spotter |
| 6 | v0.1 critic-v2 | Nov 12 01:11 | the moonlit garden beats two creatures ("the r5 fortress is back") |
| 7 | v0.1 critic-v2.1 | Nov 12 01:29 | "fleeing still beats every helping job except giving the cure" |
| 8 | v0.1 critic-v2.2 | Nov 12 01:46 | three of five awards pay for betrayal; the howl is always worth pressing |
| 9 | core-step1 critic-core-r1 | Nov 12 19:29 | "give on the first sign wins every time" |
| 10 | core-step1 critic-examine-r1 | Nov 12 20:22 | "every listed choice has one answer"; betrayal has nothing to bite on ("critic r1 S2, back again") |
| 11 | bluff-core critic-bluff-rules-r1 | Nov 15 02:38 | steal and tug hand the test crew a dominant move; "'add rules until one lie works' is the wrong shape" |
| 12 | bluff-core critic-bluff-all-r1 | Nov 15 03:40 | "turning early pays more than curing" |
| 13 | bluff-core critic-bluff-all-r2 | Nov 15 03:43 | "the lie is free and worth ~5 s" |
| 14 | bluff-core critic-bluff-all-r3 | Nov 15 03:49 | "the S1 fix doesn't hold: stiffing is still free" |

- 13 of 14 rounds found a best move; each ended in a fix on paper, and the next round found another (checked).
- Three rounds say in their own words that an earlier hole returned: 6, 10 and 14 (checked).
- Rounds 1–2 describe the counter the user found by playing on Nov 14 15:22 ("having all people around the sick one with all items in hand"), before the first build started (checked).
- This corrects "went right: the critics found the flaw early": they found it, each finding was treated as a bug to fix, and nobody counted the rounds against the foundation (Claude's reading).

### The restart question on Nov 12 (checked: transcript of session d3da34f0)
- User, Nov 12 ~21:04: "what should we do? should i start the game from scratch? everything is wrong and not working.."
- Claude: "No, don't start from scratch. Rewriting the code wouldn't fix anything, because the code isn't what's broken", then: freeze, write the smallest core, "play it with 2–3 friends within a few days".
- Claude read "from scratch" as rewriting the code and kept the same foundation; the test it offered needs friends the user can't gather (the user said so on Nov 16).
- User, a few minutes later: "lets start fixing one thing at a time". The first foundation ran until the redo on Nov 15.
- By that question, 10 rounds had run and 9 had found a best move (rows 1–10).
- The timeline in section 3 lists the question with no reply; this is the reply.

### Why the user's own stop rule had nothing to count (Claude's reading)
- The user's rule since Mustache Madness: stop when a foundation needs too many loops, where a loop is a playtest and then a change (`game-idea-triad.md`).
- A critic round is not a playtest, so 14 rounds of "find a best move, change the rules" counted as zero loops.

### Lesson offered (Claude; no verdict from the user yet)
- A best move that comes back after its fix is the "too many loops" signal, and it shows on paper before the build and the polish.
- Sketch: one list per foundation of every best move a critic or the user's head finds, each as one line the user can play in their head, marked when it is an earlier one back; Claude recommends dropping when a fix fails twice, and answers "start from scratch?" from that list.
- Checked against the user's rejections: needs no friends ✅, no stripped test ✅, doesn't split the chain ✅, keeps the polish for a foundation that survives ✅.
- Limits: it shortens the time spent on a failing foundation and does not find a fun one, since no Moonsick version was fun; and there is no threshold with evidence behind it, because none of the user's foundations passed, so there is nothing to compare the count against.
- Dropped as a lesson (fails the user's rejection "I already do 1, 2 and 4"): "check that the player wants two things that pull against each other". Claude's reading of why the hole kept returning (players only wanted safety, so the safest move was the best move, and every fix punished safe play by rule) stays an explanation, not a lesson (assumed).
- Same event once in Dungeon Pets: upkeep was the fix for "take every creature" and didn't hold (its postmortem). 2 of 2 postmortems, under the bar of 3.

## Summary
Moonsick went through four versions in five days, and none had a core choice worth making. In v0.1 honesty always won and the cure was a lookup; the bluff core still gave nobody a reason to lie; the redo gave a reason to lie but dropped co-op. Critics flagged the core before each build, and Claude itself advised a test with real people first, but every version was built and polished before anyone played it with people. Claude's share: it proposed the rule that removed the lie motive, ran the builds against its own test-first advice, and answered literal requests instead of the rules problem.
