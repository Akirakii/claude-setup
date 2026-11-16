# Accessibility: patterns and anti-patterns

Researched 2026-11-06 for the audit (`docs/audit.md`), after the user asked for "more research"
on top of every existing pattern doc. Yardstick: the **basic tier** of the Game Accessibility
Guidelines ([GAG basic](https://gameaccessibilityguidelines.com/basic/)), the features that cost
little and reach the most players, plus Microsoft's Xbox Accessibility Guidelines on input
([XAG feature tags](https://devdocs.xbox.com/build/game-principles/accessibility/accessibility-feature-tags.md))
and Unity's summary ([Unity: accessibility basics](https://unity.com/blog/video-game-accessibility-basics)).

Each line: **Rule** (the guideline, quoted from GAG unless marked) · **Us** (the game, checked
in code 2026-11-06) · verdict. Tags: *[source]*, *[read]* = checked in our code, *[opinion]*.

## The one-line diagnosis
The game's fantasy (find out by trying, no text) and accessibility pull the same way on most
lines: one key does everything, the goal is on the pedestal, signals are double-coded. They pull
apart in three places: **speech-only rules** (the narrator), **held keys** (valve, leak, cable,
carrying) and **colour-coded people** (Sequence). Each now has an option or a second channel that
leaves the default game as the user designed it. *[read + opinion]*

## Motor
| Rule | Us | Verdict |
|---|---|---|
| "Allow controls to be remapped / reconfigured" | every action rebindable (Options → Keys) | pass |
| "Include an option to adjust the sensitivity of controls" | mouse sensitivity, invert | pass |
| "Ensure controls are as simple as possible, or provide a simpler alternative" | E / click does everything | pass |
| "Ensure that all areas of the user interface can be accessed using the same input method as the gameplay" | menus by mouse, the same as play | pass |
| Avoid holds, or offer a toggle (GAG motor; Xbox XAG 107: "Provide options for toggle vs. hold") *[source]* | valve, leak, cable and carrying needed a held key | **fixed**: Options → "Hold keys: toggle" (off by default) |
| Avoid rapid mashing (Unity) *[source]* | mashing is never required: moods reward a careful hit (Patience), fast clicks are allowed, not needed | pass |
| "Include an option to adjust the game speed" | a real-time online game shared by a crew: one speed for everyone | n/a (multiplayer) |
| "Include toggle/slider for any haptics"; large touch controls | no controller rumble, PC only | n/a |

## Cognitive
| Rule | Us | Verdict |
|---|---|---|
| "Avoid flickering images and repetitive patterns" | the VIP "flicker" prank cut the room light on a random 40% of frames (a strobe); the Overflow glitch flashed the whole screen magenta at 10 Hz | **fixed**: a ~2.5 Hz stutter and one glitch flash then a ~1 Hz breath (under the common 3 flashes a second limit), both faint with Reduce flashing |
| "Allow the game to be started without the need to navigate through multiple levels of menus" | title → START AN EXPERIMENT | pass |
| "Use simple clear language" | narrator lines are short; exam briefings state the rule plainly | pass |
| "Include interactive tutorials" | none on purpose: the silent first stage is the tutorial, by trying (Fantasy, user 2026-11-03) | by design |
| "Allow players to progress through text prompts at their own pace" | no text prompts | n/a |

## Vision
| Rule | Us | Verdict |
|---|---|---|
| "Ensure no essential information is conveyed by a fixed colour alone" | mood = colour + chime + glow; Freeze mover = colour + spotlight; **Sequence = colour only** | **fixed**: every player colour has a shape (circle, triangle, square, cross, diamond, ring, hexagon, bars) on chest and back, shown on the Sequence wall |
| "Provide high contrast between text/UI and background" | subtitles white with a 6 px black outline; menus dark ink on paper | pass |
| "Use an easily readable default font size" | subtitles 22 px, orders 26 px | pass *[opinion: not tested on a TV]* |
| FOV: "set an appropriate default" | 80°, slider 65-110 | pass |
| Colour-blind-safe palette (not GAG basic; visual-communication #8) | Okabe-Ito set, simulated | pass |

## Hearing
| Rule | Us | Verdict |
|---|---|---|
| "Provide subtitles for all important speech" | orders and exam rules were voice-only (`SCREEN_TEXT` off) | **fixed** (gap review): Options → Subtitles, lines and orders |
| "If any subtitles / captions are used, present them in a clear, easy to read way" | outlined, centred, bottom, fade after 6 s | pass |
| "Ensure no essential information is conveyed by sounds alone" | mood chime + cap colour; ceiling beeps + timer screen; with Subtitles on, orders show | pass with Subtitles on |
| "Provide separate volume controls or mutes for effects, speech and background / music" | master, effects, narrator, room hum | pass |

## Speech and general
| Rule | Us | Verdict |
|---|---|---|
| Speech input not required | no voice input | pass |
| "Ensure that all settings are saved/remembered" | `user://settings.cfg` | pass |
| "Provide details of accessibility features in-game" | all are named switches in Options | pass |
| "Provide details … on packaging and/or website" | the store page isn't written yet | parked: store page checklist (`docs/roadmap.md`) |
| "Solicit accessibility feedback" | the demo build links feedback (`Tuning.DISCORD_URL`) | pass once the link exists |
| "Offer a wide choice of difficulty levels" | none: the crew is the difficulty; balance is the playtest's | parked (user's design) |

## Checklist for any new feature
1. Does it need a held key? Then it works under "Hold keys: toggle".
2. Does a colour carry a fact? Then a shape, a sound or a spotlight carries it too.
3. Is something only said? Then it shows with Subtitles on.
4. Does anything flash? No more than 3 times a second, and only a dip with Reduce flashing.
5. Does it need fast or precise input from one person? Then a crew can share it.

## Gaps in this research
- Only the GAG basic tier and one Xbox input guideline were checked; GAG intermediate and advanced
  (e.g. subtitle size options, screen-reader menus) were not.
- The 3-flashes-a-second limit is the common photosensitivity guidance (WCAG/Ofcom-style); the
  primary text was not read this session.
- Nothing was tested with disabled players.
