# Presentation v3: cameras, the home stage, the explanations

User verdict (2026-11-08, after the drone/opening build): "the camera shows the drone.. the default
main stage is ugly.. the explanation in dialog and written is not understandable"; "when the camera
changes seems like it has problems following to a moving drone, I see like a blue sphere from the
drone". Earlier verdicts on the same topic: "50% less text" (lines were cut), "I don't understand
the first game" (rules card added), "a longer introduction to appreciate the default stage",
"host one side and the other side the participants", "they are cooperating, do not split them",
"some wall behind the host and the participants", "a big screen", "a confirmation from the host".

## Checked (screenshots in `build/rv/`, code read)
**Cameras**
- The TV view copies the live drone's lens transform in `_physics_process`; drones move in
  `_process`. Right after a cut the live drone flies fast (exp follow 2.5/s: ~50 m/s on a 20 m
  move), gets ahead of the camera and the camera sees its own glowing blue lens (the user's "blue
  sphere"). Cause read in code; the user saw the symptom; not reproduced in a screenshot.
- The live drone is retargeted on air: game intro starts with drone A flying from the last
  contestant to the host; in play drone 0 picks a new subject at pt 14 while it is live.
- The other drone is visible in wide shots (b_36, c_31).
- Host close-up shot through his desk (giant "THE REAPER" letters, b_19); contestant intros shot
  through the crew desk (giant "CONTESTANTS", heads cut, c_12..c_16).

**Home stage** (a_02, a_09, c_21.8)
- Floor: the logo pattern is painted per 2 m tile: a blocky red cross and yellow squares on a grey
  checker. Reads as a placeholder.
- Host and crew are two small islands 14 m apart at the back corners; ~70% of every wide is empty
  floor. The people are not the focal point.
- Walls: the same neon strips all round (nightclub corridor); the big screen shows a feed of
  itself (screen in screen in screen) on most wides; desks carry text labels.

**Explanations**
- Switchboard lines: "THE SWITCHBOARD! Pull levers to stay alive." / "Each of you gets an order: a
  lever's name." / "You can't pull your own. Shout it!" / "Lever names only show from the edge." /
  "Wrong lever? You drop. Too slow? Nearest drops." / "21 orders together, and you live."
  Undefined nouns ("order", "the edge", "nearest"); rules without the loop (what do I do first?);
  the shot shows a generic wide, never the thing said (c_31: "names only show from the edge" over a
  wide where no plate is readable).
- Tilt line 3 "Grab keys: all of you on one at once, while it's level." says everyone on ONE key;
  the rule is one key each, all at the same moment. Wrong.
- Rules card: 5 text bullets after the host talks; the same abstractions with more words.
- Text was cut once and added once; neither worked. Assumed: text is the wrong main channel.

## Frame (the abstract problems)
1. **Cameras:** a cut must land on a shot that is already framed; a camera never sees its own rig.
   TV practice (from memory, not searched): the director cuts only to a ready camera; the off-air
   camera repositions.
2. **Stage:** in a wide shot the set must read as a TV show: one focal point, the people lit and
   grouped, a floor graphic that reads as one design. Constraint: the floor is 144 tiles that
   drop, rise and tilt, and every game starts from it.
3. **Teaching:** 3–6 people must learn a counterintuitive rule set (you can't do your own job; the
   information is somewhere else) in ~30 s, as a group, from a narrator whose voice is babble
   (subtitles are the only words). Cutting text made it cryptic; adding text wasn't read.

## Thesis 1: cameras (a bug; being fixed now, listed for the critic)
- Each drone carries its own camera at the lens; the TV view is the live drone's camera (same
  frame, no lag). The big screen copies the live camera in the same frame.
- Drones are drawn on their own render layer: TV and big-screen cameras skip it; first-person
  cameras still see drones (part of the show in play).
- A shot list: the live drone only holds its shot (slow push, tracking a walking player); the
  off-air drone flies to the next shot; a cut happens only at a shot change. In play a drone picks
  its next subject only while off air.
- The big screen's camera skips the screen itself (no hall of mirrors).
- Framing: no shot through a desk (host close-up from above the desk line; contestant shots from
  in front and above the desk, head and shoulders).

## Thesis 2: the home stage (options)
- **A. One floor graphic.** A drawn floor (concentric rings, radial light lines, the show's skull
  logo in the middle) laid across all tiles, each tile showing its slice, glossy so neon reflects.
  When tiles drop, the graphic visibly breaks apart. Keep the layout.
- **B. Compact panel deck.** The host desk and the crew desk move off the game floor onto a raised,
  lit deck in front of the back wall (host one side, crew the other, as now), close enough that one
  medium shot holds both. The 24 m floor is the arena in front of them. At GO the crew drops onto
  the start row (as now). Desks no longer sink.
- **C. Show the danger.** Home look = tiles at different heights forming a relief, with a ring of
  tiles down so the lit spike pit shows: the premise visible on the default stage.
- **D. Bought/generated set art** (Meshy desks, trusses). Out for now: credits, style mismatch.
- **Pick (Claude): A + B,** plus: key lights on host and crew (house lights lower, colour beams as
  background only), neon reduced to frame the back wall, no text labels on desks (the screen strip
  names people).

## Thesis 3: the explanations (options)
- **E1. Show it, with names.** Each host line gets a shot that shows exactly that thing, and the
  lines walk through one worked example with the crew's real names. Switchboard sketch (6 lines):
  1. wide, levers rise: "Seven levers. Each one has a name."
  2. drone at a lever, plate reads "???": "Up close, you can't read it."
  3. drone glides out to the rim behind it, the name appears: "From out here, you can."
  4. on Bo; the big screen shows "BO: PULL BONE VALVE": "Bo needs BONE VALVE pulled. Not by Bo!"
  5. a lever's trapdoor drops open: "Pull the wrong one: you fall."
  6. wide: "Pull 21 levers for each other. GO!"
- **E2. Dress rehearsal.** After the talk the crew plays for real with no clock and no deaths:
  one order each (Switchboard) or one wave (Tilt); a wrong pull buzzes, a fall puts you back. It
  replaces the frozen wait: the host presses E to go live whenever the crew is ready (the user's
  "confirmation from the host" kept). At LIVE the names reshuffle / new keys, then the clock.
- **E3. Picture card.** The written rules become 3 panels (icon + up to 4 words each), e.g.
  Switchboard: [you, a speech bubble "BONE VALVE!"] -> [a friend at the edge reading a plate] ->
  [a friend pulling it]. Shown on the big screen during the rehearsal and as a small strip in the
  HUD corner for the first 20 s of play. No paragraphs.
- **E4. Just-in-time hints.** HUD lines that fire on the situation ("Names can't be read here: go
  to the edge" when you stand at the ring for 3 s). Out: more text, ui-ux anti-pattern 1/7.
- **Pick (Claude): E1 + E2 + E3.** E1 shows, E2 lets them do it once safely, E3 is the written
  part the user asked about, as pictures.
- Tilt in the same pattern: "Stand here, the floor tips toward you" (drone on a dummy weight on
  one side) / "Too steep: you slide off" / "Each of you has a key" (keys shown) / "You can't see
  your own; a friend can" (split view on the big screen) / "All of you on your keys, same moment,
  floor level" / "Four rounds. GO!".
- Switchboard II: one new line with its shot ("TOGETHER: two levers at the same moment").

## Round 1: critic -> synthesis
Thesis 1 (cameras) built and committed (`338ac4d`): the lens rides the drone on a level gimbal;
drones and first-person hands are hidden from show cameras; your own body is drawn for the TV;
the off-air drone flies to the next shot and cuts land on it; the big screen skips itself.
Checked by screenshots (`build/rv/d_*`, `e_*`). Critic: "sound as written".

Critic findings and what changed (checked = read in code by Claude too):
| Critic finding | Synthesis |
|---|---|
| SEVERE: the HUD says "YOUR ORDER: PULL THE GRIMSHAW" (checked, `switchboard.gd:335`): it tells you to make the move that kills you; E1 line 4 repeats it | One HUD line that follows the situation, no word "order": holding: `SHOUT "GRIMSHAW!" — a friend pulls it  9 s`; at the ring: "Can't read names here: ask someone at the edge"; in the reading zone: "Shout the names you can read". Screen strip: "BO NEEDS: BONE VALVE". Tilt: "You see BO's key: tell Bo where" / "CY sees your key: listen to Cy" |
| The reading zone can't be seen (checked: radius ≥ 11 m on a 24 m square: a 1 m strip mid-side) | **LED floor** (replaces option A): the floor is one big screen; each tile shows its slice of a drawn 2D canvas (local triplanar + per-tile UV offset, so it survives drop and tilt). Home look: the show's rings and logo, animated. Switchboard: the reading zone lit as a band outside the 11 m circle, the lever ring drawn. Tilt: the slab outline. The explanation uses it too (the band lights up when the host talks about it) |
| The big screen still shows the TV picture | Big screen = graphics during intro and rehearsal (logo, name cards, "BO NEEDS: BONE VALVE", the picture panels); live feed only in play |
| B (deck) doesn't fit: 1.8 m between stage edge and back wall | Back wall to x ≈ -18 (screen, arches, strip, logo move with it); deck 4 m deep at x -17..-13, 0.6 m high, out of bounds in play |
| B makes people smaller in an audience wide | Intro wides from mid-stage, 4–6 m high, looking at the deck; floor ≤ ~30% of the frame; the audience-end wide only for the opening sweep |
| Rehearsal: names carry into LIVE (`names_now` = seed + t/20) | At LIVE the name seed changes (+ unit test); Tilt rehearsal keys are thrown away |
| Rehearsal with no timers = a calm quarterback routine; nobody sees "nearest drops" | Rehearsal = LIVE rules with order timers, minus deaths and minus the 80 s clock: a wrong pull opens the trapdoor (you climb back at the start row); a timeout buzzes and flashes the player who would have dropped |
| Readers parked at the rim at LIVE | Everyone back on the start row at LIVE |
| Host skips; one player does all; bots pull the human's order | Each player has two ticks on the HUD ("pulled for a friend", "got yours pulled"); the host's E lights when all have both (hold E 2 s skips anyway: a stuck crew isn't trapped). Bots don't pull in the rehearsal until every human has pulled once |
| Picture card on the far wall, behind readers | The picture strip sits on the HUD during the rehearsal, and small for the first 20 s of LIVE; also on the big screen |
| Tilt HUD never says whose key | see the HUD row above |
| E1 line 3 can't show the plate: readability follows `game.me` | During the intro, plates read from the live camera; Tilt "split view" = two point-of-view shots in a row |
| Clock "1:20" during the intro | Clock hidden until LIVE; "REHEARSAL" tag; going live = ON AIR light + 3-2-1 + gong |
| E1 numbers and names hardcoded; subtitle covers the lower middle | Numbers from N (N+3 levers, 7N pulls), real names; shot subjects in the upper two-thirds |

### The show flow per game after round 1
Host close-up -> panel wide -> E1 (each line + its shot, the stage transforms, the LED floor shows
what the line says) -> REHEARSAL (no clock, no deaths, order timers on, ticks, picture strip,
big screen graphics) -> host presses E when all ticks are in -> back to the start row, names
reshuffle -> ON AIR 3-2-1 -> LIVE (clock, deaths). Game 3: rehearsal = one TOGETHER order.

### Switchboard E1 after round 1 (N = 3: 6 levers, 21 pulls; example names are the real crew)
1. levers rise (wide from mid-stage): "Six levers. Each has a name."
2. at a lever, the plate shows "???": "Up close, you can't read it."
3. the drone glides out over the lit band, the plate reads BONE VALVE: "From the edge, you can."
4. on Bo; screen "BO NEEDS: BONE VALVE": "Bo needs BONE VALVE pulled. Bo can't pull it!"
5. Cy at the edge; screen "CY: IT'S THAT ONE!": "Cy reads it. Ann pulls it."
6. a trapdoor drops open: "Wrong lever? You drop. Too slow? Someone drops."
7. wide: "21 pulls for each other. Let's rehearse!"

## Round 2: critic -> synthesis
| Critic finding | Synthesis |
|---|---|
| SEVERE: teaching stacked in layers, ~35 words on the HUD in rehearsal (against "50% less text") | **Word budget: the HUD shows at most one line of ≤ 8 words while you play.** E1 back to 4 lines. Rehearsal ticks = two small icons next to each name in the roster, no labels. The picture strip lives on the big screen only (intro and rehearsal), never on the HUD, never in LIVE. No position hints: plates show "???" up close and the floor lights where you can read |
| SEVERE: the 20 s name shuffle is taught nowhere and silently renames a live order's lever (checked: `names_now`, orders are lever indices) | **An order follows its name:** when names shuffle, every live order moves to the lever that now carries that name (rules: remap by the shuffle, unit test), so a shouted name never goes stale; only *where* it is changes. Telegraphed: plates flicker and a tick-tock plays 2 s before, the new plates flash. The first shuffle in the rehearsal: the host says "Names shuffle!" |
| Time: ~2.2–3.2 min per game, LIVE at 80–110 s; Tilt rehearsal = a full hard round | Rehearsal in **game 1 only**. Games 2 and 3: **the Reaper spares each contestant once** (first death: his scythe hooks you back to the start row, the crowd laughs) |
| Deck only a box; ugly not shown fixed | Deck spec: one podium per contestant (1.3 m apart, lit fascia in their colour, their name on it), host desk ≤ 3 m from the nearest podium. **A still of the new stage goes to the user before any teaching is built** |
| E does three jobs; a held pull or toggle-use skips the rehearsal | Going live = its own key (Enter), never E or Space; no hold-to-skip on E |
| A wrong pull is free in rehearsal, so guessing wins | A wrong pull in rehearsal: the trapdoor opens, a loud "you'd be dead" sting, your ticks reset |
| 1 human + 2 bots deadlocks (TOGETHER, Tilt) | Gone with rehearsal in game 1 only (no TOGETHER, no Tilt). Bots wait for the human's first pull; reader bots walk to the lit wedge before naming a lever |
| Tilt keys have no owners (checked claim: any non-viewer may grab) | No owners on the HUD: "You see a key: talk someone onto it" / "Listen: friends see your keys" |
| Lone survivor told "a friend pulls it" | Alone: `PULL "BONE VALVE" YOURSELF  9s` |
| The lit band lies (cones leave dead spots) | The floor lights each lever's real reading wedge (its 30° cone ∩ r ≥ 11) |
| LED floor during play | Static in play, darker than players and plates, no gold (keys), red only for trapdoors |
| 1 m jumpable gap deck–stage = a safe reading balcony | Invisible play wall at the stage edge facing the deck |
| Tilt throne blocks the mid-stage wide | Tilt shots re-aimed when built |
| "Bo (bot)" in lines; Bo never shouts; quota said once | Strip "(bot)"; line 3 has Bo shout; the quota is said again at ON AIR |
| Idle bots time out orders in rehearsal | Rehearsal order timers start at the first human pull; the big screen never shows live orders |

### Flow per game after round 2
Game 1: opening -> host close-up -> 4 lines with shots (the stage transforms, the floor lights what
the line says) -> REHEARSAL (no clock, no deaths, roster ticks, picture strip on the big screen)
-> host presses Enter when all ticks are in -> start row, names reshuffle -> ON AIR 3-2-1 ("21
pulls. Too slow: someone drops.") -> LIVE. Games 2–3: host close-up -> 4 lines (Tilt) / 2 lines
(II) -> host presses Enter -> ON AIR -> LIVE with one spare per contestant.

### Lines after round 2 (N = 3)
Switchboard: 1 levers rise, a plate shows "???": "Six levers. Each has a secret name." / 2 the drone
glides out over a lit wedge, the name appears: "You can only read it from out here." / 3 on Bo,
screen "BO NEEDS: BONE VALVE": "Bo needs BONE VALVE. Bo can't pull it. Shout, Bo!" / 4 a trapdoor
drops: "Wrong lever? You drop. Let's rehearse!"
HUD: `SHOUT "BONE VALVE!" — a friend pulls it  9s`.
Tilt: 1 the floor falls to the slab: "The floor is a seesaw. Lean too far, you slide." / 2 keys
appear, POV of one player: "You see keys for your friends, never your own." / 3 POV of another: "Talk
everyone onto a key at once, floor level." / 4 "Four rounds. Your first fall is on me."
Switchboard II: "Same game, plus TOGETHER: two levers at the same moment." / "First fall is on me."

## Round 3 (last): critic -> synthesis
| Critic finding | Synthesis |
|---|---|
| SEVERE: the Tilt (hardest rules) gets the least teaching; L2 wrong twice (you see ONE key; keys have no owner, `tilt_rules.gd:123`); the 5 m fade never taught; "level", "lean", "rounds" undefined | Tilt lines: 1 "The floor tips toward where you all stand." / 2 (POV backs off, a key fades in) "Each of you sees one key, only from afar." / 3 "Someone else must stand on it." / 4 "Every key at once, floor flat. Four waves!" The slab rim lights while tilt < 6° (shows "flat"). **Wave 1 is practice**: the clock starts after wave 1 is grabbed; a fall in wave 1 hooks you back. HUD: "You see a key: talk someone onto it" |
| A spare per contestant = the death rule changes 3 times; N free blind pulls | **One spare per crew per game, in all 3 games** ("First fall is on me": the game's first death is undone, the strip shows SPARE USED). Rerun `switchboard_check.py` with it when built |
| "Order follows its name" impossible: `names_now` draws N+3 of 12 names per block (checked) | Each game fixes its N+3 names at build; a shuffle only reorders them. Orders and the snapshot carry a name id |
| A shuffle mid-grip kills (TOGETHER hold becomes a single wrong pull) | A shuffle clears all grips; levers lock for the 2 s tick-tock; lamps flicker |
| An order with 1 s left jumps at a shuffle: "nearest" kills a bystander | Every live order gets at least 4 s left at a shuffle |
| Tilt hook-back to an end mark lands sliding (9.3° alone at N=6) | Hook-back lands at the slab centre, 2 s without slide |
| Enter waits for all ticks: an away player blocks the show (undoes round 1) | Enter works anytime; the ticks only make it glow |
| Word budget read literally kills bot speech and blame | The budget covers the instruction line only. Event lines (feed, banners) ≤ 5 words, 3 s. TOGETHER: `SHOUT "GRIMSHAW + BONE VALVE" TOGETHER  9s` |
| "BO NEEDS" on the screen strip would make shouting optional | Orders on the strip only during intro line 3; never live orders |
| The rehearsal may never reach a shuffle | Force one shuffle after the first completed pull in the rehearsal |
| Ghosts hold orders, HUD says "Float around and watch" | The dead see their order line too, prefixed "GHOST:" |
| L3 never says who pulls | "Shout it, Bo: someone else pulls!" |
The one severe finding was fixed here; no fourth critic round (max 3). Not checked by a critic: the
new Tilt lines and wave-1 practice.

## The still (stage spike, branch `stage-look-spike`, worktree `../drs-stage-spike`)
Built to show the look before any teaching: panel deck at x -17.7..-13 (back wall at -18),
one podium per contestant (lit in their colour, name on the front), host 3 m from the crew,
LED floor (the show emblem, chasing rings, hazard border at the pit edge; local triplanar UVs
per tile, emission multiplied), warm key lights on host and crew, half the neon strips, name tags
off the TV. Screenshots: `../drs-stage-spike/build/sheet_f.png`, `sheet_s2.png`, `floor.png`.
