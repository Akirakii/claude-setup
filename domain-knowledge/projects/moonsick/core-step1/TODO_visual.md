# TODO: visual communication

How the game shows things to the player.
The sources are the user's 13 points (top of `docs/core-thesis.md`), the critics (`docs/critic-core-r1.md`, `docs/critic-examine-r1.md`), the removal pass report and the screenshots in `build/`.

Tags: (user) is the user's own point, (critic) a critic finding, (shot) seen in a screenshot, (code) read in code, and (assumed) not checked.
Status: **open**, **in progress**, **done, untested**, or **blocked**.
Blocked items wait on how diagnosis works, because the critic found the core choice still has one answer.

Check every new signal against the 10-point checklist in `~/Playground/deathly-reality-show/docs/visual-communication-patterns.md`.
The checklist covers the grey test, importance, one meaning per look, a second channel by sound, near the thing, wind-up, says that not what, stands out at 8 players, who did it, and by ear.

**No screen UI and no text during the night (user):** `screen_ui` and `world_text` are off.
Items glow when they're in reach and in front of you (E or LMB).
So item 10 is done for items (not yet for friends), and items 20 and 22 are done.
Items 3, 11 and 21 change: speech bubbles (claims) are gone, and refusals and Tab are silent.
Quick chat now reaches nobody by sight, the bots' claims included.

## A. Seeing the scene
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 1 | The whole game is too dark | (user); (shot) `build/base30.png`, `ux30.png` | **done, untested**: rooms are 2.6–3.1× brighter (hall mean luminance 0.128), the garden is unchanged and nothing clips. The beam boxes are gone, so moonlight shows only as lit floor patches (check they're still findable). Shots `build/bright_{before,after}_*.png`; flags `--light-shots`, `--light-try` |
| 2 | Signs on a friend are faint and tiny: glowing eyes show only out of moonlight or within 2.5 m, grey skin and drool only in moonlight or within 2 m | (user) point 2; (code) | **blocked**: seen from afar or examined up close |
| 3 | Signs and claims go by too fast: speech bubbles last 4 s | (user) point 2; (code) `SAY_LEN`; (critic) | **open**: a claim stays over the head until the speaker changes it |
| 4 | Creatures are static models that glide, so which creature it is may not read at a glance | (code); the Meshy question in `docs/questions.md` | **open**: rig and animate after the human models |
| 5 | The new human models must carry the signs (eyes, skin) on their own faces and read at ~8 m | (assumed) | **open**: after the concepts are approved |

## B. Knowing who is turning
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 6 | You don't know you're turning when your first sign is one only others can see | (user) point 8; (code) the stage 1 schedule | **open**: your own screen changes by stage, from the first second (as in No More Room in Hell 2) |
| 7 | The heartbeat means a creature is near; reusing it for "you're sick" would give one sound two meanings | (critic); (code) `hud.gd` | **open**: a separate sound for each |
| 8 | A friend turning shows from afar only as neck veins within 4 m | (user) point 8; (code) | **blocked** |
| 9 | How late a case is shows only on the neck veins | (critic); (code) | **open**: the body shows the stages (a hunch, then shaking) |

## C. Knowing what you can do
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 10 | Nothing in the world shows what's usable or which key does it (E, LMB, RMB, 1–4) | (user) points 9, 10, 11; (critic) | **open**: an outline plus a key icon on the thing you aim at |
| 11 | A refused action gives no feedback now that toasts are off ("too far", "they must hold still") | the removal report | **open**: show it at the target (the friend shakes their head) plus a sound |
| 12 | Which cure beats which monster isn't shown anywhere in the world | (user) point 7 | **open**: a monster carving over each cure spot, and the picture card on Tab |
| 13 | Actions with friends can't be discovered: holding, giving only when they hold still, raising a cure to shove | (user) point 11 | **open**: prompts at the friend (as in item 10), shown once in the first case |

## D. Knowing what happened
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 14 | Cure results: the banners are off and the body reactions aren't built | the removal report; (critic) | **open**: a cure that works glows; a right kind that failed leans toward the giver in the cure's colour; a wrong cure looks different in shape, not just strength |
| 15 | What happened elsewhere: the feed is off | (user) point 13 | **open**: a sound for each event (turn, catch, cure), readable by ear |
| 16 | Holding a friend slows their case, but nothing shows it | (critic) | **open**: the held friend visibly slows (breathing, the veins pause) |
| 17 | The turn and the catch: roar, scream, camera kick | (code) | **done, untested**: check by ear once rooms are brighter |

## E. The start and the goal
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 18 | The start doesn't say the goal or what to do | (user) points 1, 6 | **open**: a board in the hall. Claude's first drawing failed (the user found it not made for humans to understand). Redo it in an airline-safety-card style drawn by an image model, then a critic pass |
| 19 | What a cure is, and why | (user) point 7 | **open**: the first case happens near the hall; a wrong cure turns the friend on the spot (a step 1 rule, not built yet) |

## F. Too much on screen
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 20 | Too many UI elements and too much text | (user) points 3, 4 | **done, untested**: the notes, feed, coach, readout, banners, toasts, floor plan, danger edge and hand text are off |
| 21 | The cure guide on Tab is too detailed | (user) point 5 | **partly**: the % and notes are off, so Tab is a plain table; a picture card later |
| 22 | Text still on screen that was never counted: the room name on entering, item labels, doorway signs, bubbles, the night bar, "You feel:", "the curse leaves you alone for N s" | (code) | **open**: count the words on screen at the busiest moment, then cut them or turn them into pictures |

## G. Tools
| # | Issue | Evidence | Status / next |
|---|---|---|---|
| 23 | There's no measured check before the user plays (dark screens and tiny signs went unflagged) | (shot) the last pass's shots were near black | **partly**: the brightness agent measures luminance on 3 fixed views; extend it to sign size in pixels and words on screen |

## Not visual, tracked elsewhere
The main choice has one answer, and nobody has a reason to lie (both critics; the open questions on a fake main choice and on why anyone would lie, in `docs/questions.md`).
This decides items 2 and 8, and parts of items 6, 9, 12 and 14.
