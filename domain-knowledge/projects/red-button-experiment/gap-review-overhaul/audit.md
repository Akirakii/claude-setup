# Audit: every rule, mapped to the game

The final trace for presenting the design (user, 2026-11-06: "0 gaps even against every pattern
and antipattern from every doc and also with more research? imagine this is a thesis and we have
to present the final final version", then "multiple passes until 0 gaps"). It extends
`docs/gap-review.md` (33 gaps fixed in nine lens-by-lens rounds) to **every numbered pattern and
anti-pattern in every pattern doc** (106), plus two new researched docs
(`docs/accessibility-patterns.md`, `docs/demo-session-patterns.md`).

## Method
- **Verdicts.** `pass`: the game does what the rule asks (evidence named). `fixed (Pn)`: it
  didn't, and pass n changed it. `by design`: the rule conflicts with a user decision, which wins
  (the decision cited). `parked`: needs a person (playtest, the user's open question, the user's
  hand); the reason is given and the item sits in `docs/questions.md`. `n/a`: the rule's subject
  isn't in this game.
- **Zero gaps, defined.** A pass reads every rule below against the current code (and runs the
  suite, a headless bot run and a windowed run). The audit is at zero when a full pass changes
  nothing: every rule is pass, by design, n/a, or parked with a reason. Parked items are not
  hidden gaps: each is a question a review cannot answer.
- **Evidence tags.** *[ran]* checked by running (tests, soak, bot runs); *[read]* checked in code;
  *[opinion]* judgment. The pattern docs' own "Us:" lines are dated diagnoses, many from the MVP
  (machines, Bro Science, decoys): this table supersedes them.

## Passes
| Pass | Read | Changed | Checked |
|---|---|---|---|
| P1 | all 106 rules + new research (accessibility, demo/session) | 14 fixes (below) | 133 tests, headless + windowed runs |
| P2 | all rules again, after P1's changes | 2: the shape badges glowed (glow means "live / changed": broke the visual dictionary, VC A5), now plain; P1's rules written into the design docs (Monkey herding, nearest culprit, Maze re-seat, panel seam, blast rings and shapes in the dictionary, hold toggle, press body, routine quips) | 133 tests |
| P3 | all rules again, each checklist question taken literally against the new pieces | 4: shape badges failed the grey test on light bodies (dark ink there now, test: every shape ≥ 0.48 contrast in grey); the Overflow glitch was a full-screen 10 Hz magenta strobe and a ~5 Hz pulse (now one flash, a ~1 Hz breath, faint with Reduce flashing); the hot box's end glow capped under 3 Hz; **a bug**: the glitch jitter set the pedestal labels' x outright, sinking the east and west counts into the pedestal for the rest of the run (now shaken around their own spot) | 134 tests, windowed Overflow run |
| P4 | all rules again; every verdict resting on thin evidence re-checked in code (one-shot alarms, cannon load shown, pops capped, billboards hidden, sound variety, one chore under a mood, no glowing badges, no other overwrite jitter or per-frame flicker) | **0** | 134 tests; headless host + 3 bots from stage 3; windowed run with fire and dynamite: no errors |

**Result: zero by the definition above** after P4: every one of the 106 rules, and every line of
the two new researched docs, is pass, by design, n/a, or parked with its reason (the list at the end).

P1 fixes: the Monkey Car scores only when herded; an unowned chore fail names whoever stood
nearest; the Maze re-seats a walker who left; blast areas drawn on the floor (dynamite, hot box,
valve steam); routine refunds became quips; the weak panel has a faint seam; the press has a body
(a local hand, a remote arm); colour-matched shapes on every player and the Sequence wall; the
flicker prank is no strobe; hold keys can be toggles; the demo build asks for a wishlist.

## Gameplay anti-patterns (`docs/gameplay-anti-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | One player runs the team | pass | real time; exams split sight; the hog arm (rare) *[read]*; carrying alone is a playtest question |
| 2 | Taking players out of play | pass | bench 25 s, rare; VIP and trap let go at 90 s with things to do there; leavers' turns pass on *[read, ran]* |
| 3 | Automation makes players irrelevant | fixed (P1) | machines gone; the Monkey Car scored on its own: now only within 10 s of someone steering it *[ran: tests]* |
| 4 | A lead or loss compounds | pass | losses one-off, floor 5%; rewards never raise the rate *[read]* |
| 5 | A dominant strategy | pass, to measure | picky moods refuse the mash (Patience, Contrary); playtest decides how often *[read]* |
| 6 | Luck decides who wins | by design | Greedy's 20% lie is the user's special (2026-11-03) |
| 7 | Punishment without a culprit | fixed (P1) | every chore and exam fail names one; nobody touched it: the nearest ("Bo was closest") *[ran]* |
| 8 | Trolling with no comeback | pass | buyer stripe, 20 s full refund naming the buyer, buy-back of a sold friend *[read]* |
| 9 | Rules faster than people follow | pass | one button rule at a time; one chore while a mood runs *[read]* |
| 10 | Oatmeal variety, repeated lines | pass | per-run draws; shuffle-bag pools; orders never back to back (gap review) *[ran: long run]* |
| 11 | Session too long to lose | pass, to measure | ~14 min for 4 (guess) *[read]* |
| 12 | Solo tests side by side | pass | exams split seat and readers *[read]* |
| 13 | Blame is expensive | pass | slam 6% ceiling; exam 5% of goal; potato 5%; an order ≤ 6% (gap review) *[read]* |
| 14 | A minigame hangs on one player | fixed (P1) | Sequence skips a leaver (gap review); the Maze re-seats a walker who left *[ran]*; an AFK seat still fails: parked (playtest) |
| 15 | Roles assigned, not by position | pass | the seat is whoever stands in the circle *[read]* |
| 16 | Millisecond timing on a player host | pass, to measure | windows are 1-1.5 s ("together", Twins), Freeze uses host poses; lag test parked (roadmap week 2) |
| 17 | The loss is a number on a bar | pass | the ceiling slams over the culprit in the room *[read]* |
| 18 | A minigame is a mash | pass | Blink punishes one too many; Patience a mash *[read]* |

## UI/UX anti-patterns (`docs/ui-ux-anti-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | "Press E" labels | pass | no interaction text; the crosshair grows over usable things *[read]* |
| 2 | The core action has no body | fixed (P1) | a hand pushes forward on a press; others see your arm push out *[ran: windowed, no errors; look not checked]* |
| 3 | Menus where an object could do | parked | the shop is a picture grid; a walk-in shelf is the post-demo option (`docs/questions.md`) |
| 4 | Floating text over the world | pass | name tags and labels hidden (`SCREEN_TEXT`); only the press numbers stay (user, 2026-11-03) |
| 5 | Many cheap verbs | pass | honk, laser, smoking removed; E does everything |
| 6 | Drama by physics shoves | by design | slaps, blasts and launches are the friendslop toys (user's item rules); blasts now telegraphed (P1) |
| 7 | Explaining every system aloud | fixed (P1) | routine refunds are a quip at most; fines keep their number (the narrator cites real numbers, `docs/dialog-design.md`) |
| 8 | A clicker simulator | pass | no upgrades, no auto-pressers, a bare hand stays +1 |
| 9 | Minimal confused with no feedback | pass | every try answers (gap review: 6 silent tries fixed) *[ran: tests]* |

## Dialog anti-patterns (`docs/dialog-anti-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Naming the memory mechanic | pass | no "remember" lines *[read: grep]* |
| 2 | Commenting on everything | pass | quip gaps 4 s / 9 s, silent first stage; ~5 lines a minute in a bot run *[ran]* |
| 3 | Repeating lines | fixed (gap review) | sold / bought / potato pools *[ran]* |
| 4 | Solving it for the players | pass | moods silent; hints say where, not what *[read]* |
| 5 | Talking over the panic | pass | no quips during orders, exams, last 10% *[read]* |
| 6 | The narrator takes the stage | pass | lines fire on the crew's acts; friends are the show *[opinion]* |
| 7 | Voice all or nothing | pass | voice switch, narrator volume, Subtitles (gap review) |

## Discovery (`docs/discovery-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| P1 | Clear goal, hidden method | pass | "count / goal" on the pedestal |
| P2 | One obvious thing to try | pass | the button |
| P3 | Every try answers | pass | gap review + P1 (crowbar, held hand, guest after a run, wild monkey thud) |
| P4 | A hook before meaning | pass | stains seen without a light; the panel's seam (P1) and hollow thud; "Someone in a hat"; the egg wobbles |
| P5 | A record of what was learned | pass | plinths per ending; recalling past runs aloud was cut by the user (2026-11-03) |
| P6 | Teach with the thing | pass | hammer squeaks, bat swings, the cannon's mouth shows a load |
| P7 | Twist on the known | pass | moods change what the button wants |
| P8 | Layered secrets | pass | moods → hinted routes → rare private realities |
| P9 | Losing teaches | pass | a loss unlocks a scorer or a hint |
| A1 | Hidden goal or verbs | pass, parked part | goal shown; three hidden verbs parked for the playtest (crouch on fire, E-E dynamite, cart tap) |
| A2 | Moon logic | pass | every route has a chain: item in the shop → hint → reaction *[read]* |
| A3 | Key too obvious | pass | Overflow needs three combos, each glitches the counter first |
| A4 | Wrong try met with nothing | pass | see P3 |
| A5 | Running out of things to learn | pass | colours reshuffle per run; draws vary |
| A6 | Hand-holding | pass | no tutorial text |
| A7 | Curiosity mistaken for exploration | pass | one room, rules and objects |

## Escape room (`docs/escape-room-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| P1 | More open gates than players | pass | chores, items, routes beside the button; stage 1 is short (100) |
| P2 | A hero moment each | pass | seat, walker, digger, VIP, private realities, blame |
| P3 | "Why is this here?" | pass | the narrator's troll test explains every prop *[opinion]* |
| P4 | The GM is a voice | pass | eye hidden, voice only |
| P5 | Hints by need | parked | the ask-for-help verb (`docs/questions.md`, user's call after the playtest) |
| P6 | Feedback never in doubt | pass | dud dark beat + clack/clank vs a pop |
| P7 | Honest affordances | fixed (P1) | the weak panel has a seam |
| P8 | Puzzles that need talking | pass | exams, the gold map, the timer screen |
| P9 | A climax | pass for routes, parked for Escape | `docs/questions.md` (Escape ending) |
| P10 | Bonus secrets | pass | private realities, ghosts |
| A1 | Tedium | pass, to measure | sensitivity scales items; the count is never the work *[opinion]* |
| A2 | Things that lie | pass | the cursed button and Hunt's fakes answer when used |
| A3 | One gate holds the team | pass | exams are the finale-style gates; readers talk |
| A4 | Headcount not scaled | parked | 8 players need their own playtest |
| A5 | A buzzkill GM | pass | see dialog |
| A6 | Noise in the air | pass | one-shot chore alarms; quiet mix (master 10%) |
| A7 | Luck decides the answer | pass | the draw is random, a right action always works (Greedy: by design) |
| A8 | Outside knowledge | pass | none needed |
| A9 | One puzzle type repeated | pass | five kinds, each a different question |
| A10 | Most teams need a hint | parked | a playtest metric |

## Game feel (`docs/game-feel-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| P1 | Answer within 100 ms, predict locally | pass | press cap, sound and now the hand predicted; never the count |
| P2 | Feedback depends on success | pass | burst and pop scale with points; duds go dark |
| P3 | A hierarchy | pass | press < rule change < slam / milestone < win |
| P4 | Channels agree, anticipation | pass | throw wind-up seen by all; press hand (P1); blast rings before a blast (P1) |
| P5 | Short impacts, trauma shake | pass | `Feel` ladder |
| P6 | Vary what repeats | pass | ±5% pitch, 35 ms dedupe |
| P7 | Use the space | pass | ceiling grind, lamps per stage, room light |
| P8 | Reduce shake and flash | fixed (P1, P3) | both options; the flicker prank and the Overflow glitch obey Reduce flashing, and nothing full-screen flashes over ~3 Hz |
| A1 | Volume instead of success | pass | sizes follow points |
| A2 | Full juice on routine | pass | hand presses get no burst |
| A3 | Juice hides state | pass | quiet effects, narrator on its own bus |
| A4 | One intensity | pass | see P3 |
| A5 | Predictions snap back | pass | only the body and sound are predicted |
| A6 | Hard first-person shake | pass | small, short, a slider to 0 |

## Visual communication (`docs/visual-communication-patterns.md`)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| P1 | Shape, value, colour | fixed (P1, P3) | every player now also has a shape, inked to read in grey (test); items are distinct grey boxes |
| P2 | Value structure | pass | white room, red cap brightest |
| P3 | Attention by importance | pass | see game feel P3 |
| P4 | One visual language | pass | the dictionary in `docs/ui-ux-design.md` (3 entries added) |
| P5 | Telegraph, keep the promise | fixed (P1) | blast rings for dynamite, hot box, valve steam |
| P6 | Guide with the world | pass | the hatch slides out lit; chores on their walls |
| P7 | Teach by placement | pass | things come out of the hatch where the crew stands |
| P8 | Never colour alone | fixed (P1) | Sequence: shapes beside colours |
| P9 | Diegetic and obvious | pass | count on the pedestal, timer screen |
| P10 | A wordless way to point | by design | laser and honk removed (user, 2026-11-03) |
| A1 | Effects drown the game | pass | pops capped and merged |
| A2 | Everything high contrast | pass | |
| A3 | The answer painted on | pass | hints say where |
| A4 | Icons everywhere | pass | none |
| A5 | Breaking your own rule | pass | room signals never lie; the narrator may |
| A6 | Visual and hit disagree | fixed (P1) | rings drawn at the real radius (4 m, 3.5 m, 5 m) |
| A7 | Trusting that players looked | pass | signals on the button plus sound |
| A8 | Colour-only fixes | fixed (P1) | shapes, not just a palette |
| A | Attribution | pass | spotlight, ember feet, soot, potato, buyer stripe |
| B | State from the room | pass | pedestal, timer screen, lamps |
| C | Bodies carry intent | fixed (P1) part | wind-up, and now the press arm |
| D | Sound as a channel | pass | sounds from their source; chores from their walls |

## Accessibility (`docs/accessibility-patterns.md`, new) and the demo (`docs/demo-session-patterns.md`, new)
Every line of both has its verdict in its own doc. P1 fixed: hold-key toggle, colour shapes, the
flicker strobe, the demo's wishlist ask. Parked: accessibility on the store page, difficulty
levels (user's design), demo timing vs Next Fest (roadmap), host migration (tech risk).

## Parked, in one list (why a review stops here)
Playtest: balance and ceiling slack, crews of 8, hint need per mood and route, hidden verbs, an
AFK seat, whether mashing still wins. The user's open calls: ask-for-help hints, the Escape
climax, the shop as a shelf, whose save keeps unlocks, release flags and links. The user's hand:
the lag test, export templates, the store page.
