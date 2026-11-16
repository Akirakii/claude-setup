# Visual communication: patterns and anti-patterns

How the game *shows* things to the crew: what is important, what is dangerous, where to look,
what changed, and how players signal each other. Researched 2026-11-06 (user: "could you research
all antipatterns and patterns for game communication? i mean like visual communication"). Check
any new object, colour, effect, light or signal against the checklist at the end.

Scope: what the eye reads. How an action *feels* (shake, hitstop, juice size) lives in
`docs/game-feel-patterns.md`; prompts, menus and floating text live in
`docs/ui-ux-anti-patterns.md`. This file does not repeat them.

Tags: *[source]* = backed by a linked source; *[read]* = checked in our code; *[opinion]* = design
judgment, not checked.

## Terms
- **Readability**: how fast a player can tell what a thing is and what it is doing, at play
  speed and distance. Read order, per Valve and later art guides: **silhouette** (outline) first,
  then **value** (light/dark), then **hue**, then detail
  ([Valve, Illustrative Rendering in TF2](https://www.valvearchive.com/archive/Other%20Files/Publications/Mitchell-IllustrativeRenderingInTF2%28Siggraph07%29.pdf),
  [Game Developer: reduce visual confusion](https://www.gamedeveloper.com/design/how-to-reduce-visual-confusion-in-your-game)). *[source]*
- **Visual hierarchy**: the most important thing on screen draws the most attention; attention
  scales with importance ([Riot: Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)). *[source]*
- **Signposting**: in-world marks that tell the player where to go or what to use (ledge paint,
  lit doors, landmarks). "Yellow paint" is the critics' name for the heavy-handed kind
  ([Wikipedia: Yellow paint debate](https://en.wikipedia.org/wiki/Yellow_paint_debate)). *[source]*
- **Telegraph**: a cue *before* something happens (wind-up, glow, sound) so the player can react.
- **Diegetic**: shown inside the world (a light on the machine) rather than on a screen overlay.
- **Double-coding**: the same fact carried by two channels (colour *and* shape, light *and* sound).

## The one-line diagnosis
**Every source agrees: one clear thing at a time, said the same way every time, in more than one
channel.** Noise, inconsistency and colour-only signals are the three ways visual communication
fails. *[source: summary of the items below]*

---

## Patterns (do)

### 1. Shape first, then value, then colour
- **Rule:** Valve split TF2's read into *team* (colour) and *class* (silhouette, proportions,
  weapon, hats, clothing folds), and used rim light and value instead of outlines
  ([Valve slides, NPAR 2007](https://cdn.fastly.steamstatic.com/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2_Slides.pdf),
  [paper](https://www.valvearchive.com/archive/Other%20Files/Publications/Mitchell-IllustrativeRenderingInTF2%28Siggraph07%29.pdf)).
  Riot: a champion's main silhouette feature must never be removed by a skin
  ([Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)). *[source]*
- **Test:** desaturate a screenshot; if you can still parse it at a glance, it reads
  ([Game Developer](https://www.gamedeveloper.com/design/how-to-reduce-visual-confusion-in-your-game)). *[source]*
- **Us:** players are colour-coded capsules from an 8-colour list (`scripts/game/puppet.gd:7`);
  identity is colour plus a name label. Hats, tape, balloons already change the silhouette
  (`puppet.gd:131-201`). *[read]* Each new item or machine should have a shape you can name from
  across the room in grey. *[opinion]*

### 2. Plan a value structure: gameplay pops, background recedes
- **Rule:** DOTA 2 keeps ground detail low-contrast and darker than units, so heroes are the
  brightest, highest-contrast things on screen; Limbo inverts it (light background, dark actors).
  Either works if chosen and kept. "If everything is drawing attention, nothing will."
  ([Game Developer](https://www.gamedeveloper.com/design/how-to-reduce-visual-confusion-in-your-game)). *[source]*
- **Riot VFX guide:** avoid pure black and pure white; save the brightest value for the impact
  moment; effects get a higher saturation ceiling than the environment
  ([VFX Apprentice summary of Riot's style guide](https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips),
  [guide PDF](https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf)). *[source]*
- **Us:** the blank testing room is a gift here: a low-contrast white/grey room makes the red cap
  the brightest, most saturated thing by default. Keep the room's value range narrow and let only
  gameplay things (button, machines, held items, players) carry saturation. *[opinion]*

### 3. Attention scales with importance
- **Rule:** Riot ranks attention by damage, crowd control, dodgeability and impact on play; a
  weak attack must not look like an ultimate
  ([Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/),
  [VFX tips](https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips)). *[source]*
- **Us:** same ladder as `game-feel-patterns.md` #3 (press < rule change < ceiling drop / wipe /
  escape), applied to light and colour: a rule change should be the second-brightest event in the
  room, never matched by a routine press. *[opinion]*

### 4. One visual language, kept for the whole game
- **Rule:** consistent visual language is called the most important tool for talking to players;
  red barrels work because they always explode. Breaking a convention without first making the new
  meaning readable makes players stop trusting the visuals
  ([Sumsion: Communicating with your player](https://n8sumsion.blogspot.com/2018/04/communication-in-game-design-part-3.html),
  [Giant Bomb: Exploding barrel](https://giantbomb.com/wiki/Concepts/Exploding_Barrel)). A
  student playtest found red walls you could walk through read as "forbidden" and hurt the puzzles
  ([Tiltfactor](https://tiltfactor.org/student-perspectives-patrick-matlin-redondo/)). *[source]*
- **Us:** define a small dictionary and never break it: e.g. *glow = live/changed*, *grey = locked*,
  *dark beat = dud*. The cap already uses grey for locked and a dark beat for a dud
  (`scripts/game/room_views.gd:214-219`). *[read]* Write the dictionary into `ui-ux-design.md`
  so new features reuse it. *[opinion]*
- **Fit to our Fantasy:** a consistent *that-it-changed* signal does not spoil *what* it does
  (core-design: "Signal that something changed, never what it means"). Consistency lives in the
  alert; mystery lives in the meaning. *[opinion]*

### 5. Telegraph before, and keep the promise after
- **Rule:** readability is two halves: the cue *before* an event and the expectation of what
  follows; mismatches between the two are the main source of frustration. Telegraph salience should
  match danger. Sekiro's single danger symbol is the classic consistent marker
  ([Game Developer: enemy attacks and telegraphing](https://gamedeveloper.com/design/enemy-attacks-and-telegraphing),
  [Bugnet: attack telegraphs](https://bugnet.io/blog/how-to-design-enemy-attack-telegraphs)). Riot
  gives dangerous abilities an audio wind-up and demands hitboxes match their visuals
  ([Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)). *[source]*
- **Us:** anything that can catch a player (ceiling drop, a trap, an event that wipes) gets a
  wind-up the whole crew can see and hear; the *area* it affects is drawn on the floor/thing, not
  guessed. Being blamed is fun only if the warning was there. *[opinion, built on source]*

### 6. Guide with the world: landmarks, light, leading lines
- **Rule:** a "weenie" (Disney's term) is a distant landmark that pulls the player (HL2's
  Citadel, Journey's mountain); corridors, light beams and edges are leading lines
  ([GMTK: Why Nathan Drake doesn't need a compass, transcript](https://amara.org/subtitles/xwcncEJkgSYU/en/2/download/Why%20Nathan%20Drake%20Doesnt%20Need%20a%20Compass%20%20Game%20Makers%20Toolkit.en.txt),
  [Game Developer: how designers turn heads](https://gamedeveloper.com/design/how-designers-turn-heads)). HL2 put a battery at the end of a
  dark hall and marked ammo caches yellow; it used birds flying off to point at a threat
  ([Parsons: Light and levels](https://games.parsons.edu/light-and-levels/)). *[source]*
- **Catch:** light alone does not guarantee a look: "players gravitate toward light like moths" is
  called a fallacy; a bright space can be ignored ([same Parsons page](https://games.parsons.edu/light-and-levels/)). *[source]*
- **Us:** the room is small, so "where to go" matters less than "what to look at". Use the same
  tools for *that*: a machine that wakes up lights itself, a hatch that opens throws light on the
  floor, motion (a twitching object) beats colour for catching an eye. *[opinion]*

### 7. Teach by placement, not text
- **Rule:** World 1-1 taught jumping, enemies and power-ups with no written instruction, by putting
  a Goomba (clearly an enemy) and a mushroom where the player meets them first
  ([Game Developer: How Miyamoto built 1-1](https://gamedeveloper.com/design/how-miyamoto-built-i-super-mario-bros-i-legendary-world-1-1)). *[source]*
- **Us:** fits "No interaction text" (`ui-ux-design.md`) and the Discoverability fantasy: the first
  time a new object appears, put it where a crew member will bump into it, not in a corner. *[opinion]*

### 8. Never let colour carry a fact alone
- **Rule:** "Color alone should never be used to represent information." Pair colour with shape,
  pattern, icon or text; greyed-out also needs a second cue (Sea of Thieves adds a lock); if colour
  is primary, let players pick the colours
  ([Xbox Accessibility Guideline 103](https://learn.microsoft.com/en-gb/gaming/accessibility/xbox-accessibility-guidelines/103),
  [GAG: colour alone](http://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-a-colour-alone)).
  Critical cues should also have a non-visual channel (sound, haptics). Colour-blind *modes* alone
  do not fix it; redundant cues do ([Bugnet: QA for colourblind modes](https://bugnet.io/blog/qa-testing-for-colorblind-modes)). *[source]*
- **Us:** a mood change is cap colour + glow energy + a 3-note chime (`scripts/audio/sfx.gd:107`),
  so it is double-coded. *[read]* But Freeze flashes the cap in the *mover's* colour
  (`room_views.gd:206-210`), and the player list has red, orange, green and brown next to each other
  (`puppet.gd:7-9`): simulated, green-red, red-brown and orange-yellow were close (dE < 20).
  **Fixed 2026-11-06:** the Okabe-Ito set (vermillion swapped for navy and wine; worst pair dE 16 across
  deuteranopia, protanopia and tritanopia, by a simulation script) and the culprit spotlight on the
  mover as a second cue. *[ran: simulation; not tested with colour-blind players]*

### 9. Diegetic where it fits the fiction, and still obvious
- **Rule:** Dead Space put health on the suit's spine so the screen stays clear and tension stays
  high; it works because the fiction (a survival suit) motivates it and it sits near the centre of
  the gaze; the lead designer's aim was "obvious but not obtrusive". It also limits what you can
  show ([Unity: immersive UI](https://unity.com/blog/games/how-to-immerse-your-players-through-effective-ui-and-game-design),
  [Game Developer: trimming the UI fat](https://www.gamedeveloper.com/design/seamless-ui-design-or-trimming-the-ui-fat),
  [Wayline: diegetic interfaces](https://www.wayline.io/blog/diegetic-interfaces-game-design)). *[source]*
- **Us:** "No corner UI" (`ui-ux-design.md`) already commits to this. The testing-room fiction
  motivates lights, dials, warning lamps and printouts on the walls. Anything a player must not
  miss sits where they already look (the button), not on a far wall. *[opinion]*

### 10. Give players a wordless way to point
- **Rule:** Apex's ping (one button marks a spot on teammates' screens and the character says a
  callout) was tuned by playtesting for a month with mics muted; it lets people play without voice
  and reduces toxicity ([Game Developer: muted mics](https://gamedeveloper.com/design/respawn-played-with-muted-mics-to-get-i-apex-legends-i-smart-comms-system-just-right),
  [PC Gamer](https://www.pcgamer.com/apex-legends-ping-system-is-a-tiny-miracle-for-fps-teamwork-and-communication)).
  Journey gave strangers only movement and a chime; players invented signals ("quick chimes = look",
  "long chime = follow me"), and Chris Bell argued text "introduces all sorts of unwanted verbs"
  ([Game Developer: GDC 2012, Journey](https://gamedeveloper.com/audio/gdc-2012-how-i-journey-i-was-designed-to-facilitate-friendship)). *[source]*
- **Us:** friendslop crews are usually on voice, so a ping matters less than in Apex. The laser
  pointer and honk were removed by the user (`ui-ux-design.md`, 2026-11-03), so any pointing tool
  is the user's call; parked, not proposed. *[read, opinion]*

---

## Anti-patterns (don't)

### 1. Don't let effects drown the game
- Visual noise "can make it difficult to react properly in teamfights" (Riot); Overwatch players
  complain of accumulated clutter and unclear AoE areas
  ([Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/),
  [Blizzard forum](https://us.forums.blizzard.com/en/overwatch/t/something-needs-to-be-done-about-the-visual-noise-in-the-game/399146),
  [Dexerto](https://www.dexerto.com/overwatch/overwatch-players-want-visual-changes-to-aoe-ability-range-1407078/)).
  Riot: "FX aren't supposed to tell the story; they're supposed to support and enhance it"; keep
  them short and fading ([VFX tips](https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips)). *[source]*
- **Us:** with 8 players, machines and items all pressing at once, count the effects alive at peak.
  Floating "+1" per press is the obvious multiplier (`ui-ux-design.md` Feedback). *[opinion]*

### 2. Don't make everything high-contrast
- "Contrast draws attention, and if everything is drawing attention, nothing will"
  ([Game Developer](https://www.gamedeveloper.com/design/how-to-reduce-visual-confusion-in-your-game)). *[source]*

### 3. Don't paint the answer on the wall
- Heavy signposting makes players feel the game chose their path (Control's director); defenders
  say it keeps players in the mechanics; Kotaku called the debate unsolvable
  ([Game Developer: Control Resonant director](https://www.gamedeveloper.com/design/control-resonant-director-lays-out-case-for-avoiding-excessive-yellow-paint-),
  [GamesRadar: defence](https://www.gamesradar.com/ignore-the-yellow-paint-detractors-visual-cues-are-great-for-games),
  [Wikipedia](https://en.wikipedia.org/wiki/Yellow_paint_debate)). Giant Bomb argued cues get more
  cartoonish as fidelity rises, because realistic scenes hide the path (same Wikipedia page). *[source]*
- **Us:** our version of yellow paint is marking *what* a hidden route does. Signal that a thing is
  interesting (it reacts, glows, moves); never mark the solution. Grey-box art helps: low detail
  means small cues stand out without paint. *[opinion]*

### 4. Don't cover the world in icons and markers
- The tower-reveals-icons open world was criticised as a checklist; BotW dropped most markers and
  used towers and landmarks as pulls instead
  ([GamesRadar](https://www.gamesradar.com/finally-zelda-breath-of-the-wild-fixes-open-worlds-by-not-telling-you-anything),
  [Engadget](https://www.engadget.com/2017-04-04-zelda-breath-of-the-wild-open-world-games.html),
  [GMTK](https://gmtk.substack.com/p/how-nintendo-solved-zeldas-open-world)). *[source]*
- **Us:** already ruled: no interaction text, no corner UI. Applies also to billboards over players
  (name, title, nickname: `puppet.gd:88-89`): keep them few. *[read, opinion]*

### 5. Don't break your own visual rule silently
- A barrel that looks different from the others, or red that means "go", teaches players the
  visuals lie (anti-pattern side of pattern #4; sources there). *[source]*
- **Us:** the narrator can *lie in words*, that is the fun; the *room's* visual signals should
  never lie, or "nobody is caught out by something invisible" (core-design Fantasy) fails.
  *[opinion]*

### 6. Don't let the visual and the hit disagree
- Riot calls hitbox/visual mismatches a major source of frustration
  ([Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)). *[source]*
- **Us:** the drawn area of a falling ceiling, a cannon blast or a trap equals the area it acts
  on. *[opinion]*

### 7. Don't trust that players looked
- Players focused on a task miss cues outside it: in a racing-game study they did not look at the
  guide arrows; Destiny 2's HUD and world sometimes said different things and confused players
  ([UXPA: insights from eye tracking](https://oldmagazine.uxpa.org/?p=98),
  [Strubberg & Horn papers](https://shsu.academia.edu/BrandonStrubberg)). *[source, small studies]*
- **Us:** players stare at the button. Put rule-change signals *on the button* (already so: cap
  colour) and back them with sound for anyone looking away. *[read: room_views.gd cap, sfx mood]*

### 8. Don't ship colour-only or colour-mode-only fixes
- See pattern #8. A colour-blind toggle bolted on later does not fix a signal that only exists as
  colour. *[source]*

---

## Multiplayer feedback and communication
Added 2026-11-06 (user: "does this cover feedback and communication?" / "fix then"). *Feedback*
here = the game's response to an action; *communication* = the game telling the crew, and players
telling each other. Own-action feel stays in `game-feel-patterns.md`.

### A. Attribution: show who did it
- **Rule:** in Among Us, spatial evidence (who stood where, who moved) is what lifts it above
  Werewolf's talk-only deduction; visible tasks give hard proof of innocence, which critics call
  both a strength and a shortcut past the social play
  ([Critical Play: Among Us](https://mechanicsofmagic.com/?p=58911),
  [Critical Play: social deduction](https://mechanicsofmagic.com/2024/04/09/critical-play-social-deduction-4/)). *[source, commentary]*
- **Rule:** people blame others' character, not the situation (fundamental attribution error), and
  bad outcomes draw more blame than good ones earn credit
  ([Cognitive Science Society paper](https://escholarship.org/content/qt7w56k8ft/qt7w56k8ft.pdf?t=op2lxb),
  [Gaming psych essay](https://tarpon-arugula-th46.squarespace.com/gaming-psych/fundamental-attribution-error-in-multiplayerpvp-video-games-a-cognitive-bias-in-digital-competition)). *[source; the paper is not about games]*
- **Us:** a red culprit spotlight picks out whoever the narrator names (`scripts/game/room_world.gd:289`);
  Freeze flashes the mover's colour on the cap (`room_views.gd:206`). *[read]* Pattern: every
  event that can be blamed leaves a *visible trace on the person who caused it* for a moment
  (light, colour flash, soot, a held item), so the crew blames with evidence. Blame without a trace
  turns into "the game screwed us". Keep evidence partial (who, not why) so arguing stays fun, the
  Among Us lesson: full proof ends the argument. *[opinion, built on source]*
- **Don't:** let attribution depend on colour alone (pattern #8), or on a name in text (no
  interaction text, `ui-ux-design.md`). *[read]*

### B. State and progress from the room, not a HUD
- **Terms:** Fagerholt & Lorentzon's *Beyond the HUD* (2009) splits interfaces into **diegetic**
  (in the world, the character can see it), **non-diegetic** (overlay), **spatial** (in 3D but not
  in the fiction, e.g. an outline) and **meta** (overlay effects like a blood-splatter screen)
  ([summary](https://yuting-jiang.blogspot.com/2011/12/creating-immersive-experiences-with.html),
  [TV Tropes: diegetic interface](https://www.tvtropes.org/pmwiki/pmwiki.php/Main/DiegeticInterface)). *[source]*
- **Rule:** diegetic is not automatically better. In one experiment HUD ammo was less disruptive
  than in-world ammo, but a number right in front of the gun needed less glancing
  ([Carleton GI 2015 poster](https://www.csit.carleton.ca/~rteather/pdfs/GI2015_poster2.pdf)). The
  winner is *where the eye already is*, not the fiction. Metro 2033 shows a full diegetic UI is
  possible ([Game Developer: UI in video games](https://www.gamedeveloper.com/design/user-interface-design-in-video-games)). *[source]*
- **Us:** the count sits on all four sides of the pedestal, right under the button the crew stares
  at: the "in front of the gun" case. The timer is one north-facing monitor *on purpose* so one
  player calls it out (`ui-ux-design.md` The room, user 2026-11-03). *[read]* That's a
  communication design: information split so players must talk. Use it again knowingly, not by
  accident: a fact only one spot can see becomes something a player has to say out loud. *[opinion]*
- **Do:** for slow state (ceiling height, heat, a machine running hot) let the room itself change:
  light colour, hum pitch, a lamp's blink rate. Players read *a change* better than a level, so
  step the signal when crossing a threshold rather than fading it smoothly. *[opinion]*

### C. Player to player: bodies, gestures and voice
- **Rule:** players use movement, item use and UI signals to say intent and avoid conflict, and in
  shooters invent meanings designers never planned; pings mostly keep their intended meaning
  ([NVIDIA research, 2026: emergent non-verbal communication](https://research.nvidia.com/publication/2026-07_understanding-emergent-non-verbal-communication-delta-force-competitive-video.md)).
  Free gestures were preferred over a fixed emote menu in a study, though some players felt exposed
  ([UMD thesis: mirrored gestures](https://drum.lib.umd.edu/items/6ea6f68a-77ec-4c52-81cd-8015177c658e/full)).
  Journey's chime became a made-up language (pattern #10). *[source]*
- **Rule (friendslop):** in Lethal Company proximity voice is the comedy engine: a scream fades
  with distance, voices echo in rooms, the dead go silent; the fun "depends on your group more
  than the game" ([Acer: what are friendslop games](https://blog.acer.com/en/discussion/3477/what-are-friendslop-games),
  [Windows Central: viral clip](https://www.windowscentral.com/gaming/pc-gaming/this-viral-lethal-company-clip-perfectly-illustrates-why-this-pc-game-is-blowing-up-right-now)). *[source, press/blogs]*
- **Us:** no in-game voice (crews use Discord). *[read: no voice code in `scripts/net/net.gd`]*
  Then the body has to carry intent: a wind-up visible to others (the throw has one,
  `player_body.gd`), what is in your hand readable from across the room, where you are looking.
  Proximity voice is a bigger, separate decision, parked in `docs/questions.md`. *[opinion]*

### D. Sound as a channel of its own
- **Rule:** Overwatch was built so people could "play by sound": a clean mix, sounds you can
  pinpoint, unique footsteps per hero, and an importance system that boosts sounds from whoever is
  aiming at or near you and ducks the rest; voice lines are cut to the most informative ones
  ([PC Gamer](https://pcgamer.com/how-overwatch-uses-sound-to-pinpoint-threats-you-cant-see),
  [Game Developer: GDC video](https://gamedeveloper.com/audio/video-how-i-overwatch-i-was-designed-so-people-could-play-by-sound-)).
  Hunt: Showdown defines audio readability as understanding essential information "by listening
  alone", e.g. footsteps above vs below sound different
  ([Hunt dev insight](https://www.huntshowdown.com/news/dev-insight-audio-design-recap-what-s-new-in-update-24)). *[source]*
- **Us:** `play_at` existed (`scripts/audio/sfx.gd:25`) but nothing used it; every sound was flat.
  **Fixed 2026-11-06:** player actions, the hatch, the cannon and impacts now play from their
  source; room-wide moments stay flat. *[read]*
  Rules for new sounds: one sound per kind of event, so it is learnable without looking; place it
  at the thing that caused it (`play_at`), never flat; important sounds win the mix, routine presses
  duck. All inside the quiet-audio rule (master 10%). *[opinion]*

---

## Checklist for any new visual signal
1. **Grey test:** does it read in a desaturated screenshot? (shape/value, not hue)
2. **Rung:** where on the importance ladder is it, and is it dimmer than everything above it?
3. **Dictionary:** does it reuse an existing meaning (glow, grey, dark beat), or add a new entry
   that never clashes with an old one?
4. **Second channel:** is it also a sound (or shape/motion) for those who miss the colour or
   are looking away?
5. **Where eyes are:** is it on or near the button / the thing that changed, not a far wall?
6. **Telegraph:** if it can catch a player, is there a wind-up and a drawn area that matches the
   real one?
7. **Fantasy:** does it say *that* something changed without saying *what* it does?
8. **Noise:** at 8 players and peak chaos, does it still stand out, and does it fade fast?
9. **Who:** if someone can be blamed for it, does it leave a brief visible trace on that person?
10. **By ear:** can a player looking away tell what happened and where, from its sound alone?

## Gaps in this research
- Primary GDC talks were not readable (Valve's 2008 "Stylization with a Purpose" PDF, GDC 2017
  "Artistic Principles of VFX" by Riot/Blizzard, Dead Space's 2013 UI talk); points above come
  from the 2007 Valve paper/slides and secondary write-ups.
- The GAG colour page and the Miyamoto Eurogamer interview were cited via secondary sources.
- Eye-tracking evidence is from small studies and practitioner reports.
- Nothing found specific to *rule-change* readability in party games; the patterns are borrowed
  from combat and level design.
- Our colour-blind risk (#8) is read from code, not tested in a simulator.
- Attribution and blame: no studies on co-op/friendslop blame; sources are critique blogs plus one
  non-game cognitive science paper. Lethal Company sources are press/blogs, no developer statement.
- No developer sources found for diegetic progress in Inside, Firewatch or Lethal Company.
