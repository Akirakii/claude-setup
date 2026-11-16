# Game feel: patterns and anti-patterns

How a press, a hit or a rule change should *feel*, researched 2026-11-06 (user: "could you extract
patterns and antipatterns for game feel?" / "i need to record here to improve this game for
claude"). Check any new feedback (sound, motion, effect, camera) against this list.

Covers the moment-to-moment feel of actions. Interaction design (prompts, menus, floating text)
lives in `docs/ui-ux-anti-patterns.md`; this file does not repeat it.

Tags: *[source]* = backed by a linked source; *[read]* = checked in our code; *[opinion]* = design
judgment, not checked.

## Terms
- **Game feel** (Swink): real-time control of an object in a simulated space, with interactions
  emphasised by polish. Six parts: **input**, **response**, **context** (the space around the
  action), **polish** (effects that sell the interaction), **metaphor** (what it is meant to be),
  **rules** ([Swink, Game Developer](https://www.gamedeveloper.com/game-platforms/feature-game-feel---the-secret-ingredient-),
  [Wikipedia](https://en.wikipedia.org/wiki/Game_feel)). *[source]*
- **Juice**: extra feedback stacked on an action (flash, shake, particles, sound, floating
  numbers) beyond what the rules need. From Jonasson and Purho's 2012 talk "Juice it or lose it"
  ([summary](https://eastondev.com/blog/en/posts/dev/20260521-game-feedback-feel/)). *[source]*
- **Success-dependent feedback**: feedback whose size depends on how well the player did, versus
  the same burst for any input.

## The one-line diagnosis
**The research says feedback helps when it tracks what the player achieved, and hurts when it just
gets louder.** In the largest study (Kao et al., CHI 2024, 1,699 players), feedback that depended
on success raised every measured motive, while *amplifying* the feedback lowered them
([abstract](https://sciety.org/articles/activity/10.31234/osf.io/f83dp)). *[source]*

---

## Patterns (do)

### 1. Answer within 100 ms; predict locally
- **Rule:** response under ~100 ms reads as direct control; much past that, people feel lag.
  Widely attributed to Swink; the exact page is unverified
  ([lecture citing Swink](https://medienwissenschaft.uni-bayreuth.de/wp-content/uploads/GxD-07-Interfaces.pdf)).
  Online, show the result on the client before the host confirms (client-side prediction)
  ([SS14 prediction guide](https://docs.spacestation14.com/en/ss14-by-example/prediction-guide.html)). *[source]*
- **Catch:** a wrong prediction feels worse than lag. Knockout City predicted catches only when
  the client was confident ([summary via search](https://medium.com/velan-studios/catch-this-the-magic-behind-knockout-citys-satisfying-gameplay-9b3965717f7d);
  page itself was not readable). *[source, secondhand]*
- **Us:** the button cap and press sound are predicted, and only when the snapshot says the
  button is pressable and not locked (`scripts/game/room.gd:146`). *[read]* Keep that rule for
  every new local-player action: predict the body and the sound, never the count or the reward.
  *[opinion]*

### 2. Make feedback depend on success
- **Rule:** success-dependent feedback raised competence, effectance and curiosity; uncertain,
  graded success drives curiosity, the strongest predictor of enjoyment and the only predictor
  of playtime (Kao et al. 2024, above). *[source]*
- **Us:** the moment a press pays more, less or nothing should feel different from a plain press,
  so the crew can feel their way to the rule change (fits the Readability guardrail in
  `CLAUDE.md`: show *that* it changed, not *what* it does). *[opinion, built on source]*

### 3. Build a feedback hierarchy
- **Rule:** spend most polish on the core action and scale intensity to importance, so big moments
  stand out from routine ones ([Wayline: juice overload](https://www.wayline.io/blog/juice-overload-sensory-feedback-hurts-gameplay)). *[source]*
- **Us:** rough ladder: single press (light) < a rule change (clear, room-wide) < ceiling drop,
  wipe, escape (biggest). Each new effect names its rung. *[opinion]*

### 4. Let every channel agree, with anticipation and follow-through
- **Rule:** polish works when animation, sound and effects agree with the input (Swink). Borrowed
  animation principles: a wind-up before (anticipation), a settle after (follow-through)
  ([Mega Cat juice guide](https://megacatstudios.com/blogs/game-development/mega-cat-developer-juice-guide-v1-0-08-23-17)). *[source]*
- **Us:** the throw already has a wind-up (`player_body.gd`, `wind_up`). *[read]* The press is
  only a 5 cm cap drop plus a sound (`room.gd:562`); see `ui-ux-anti-patterns.md` #2. *[read]*

### 5. Keep impacts short and small: hitstop and trauma shake
- **Rule:** hitstop of about 2–5 frames adds weight; shake should be small, and a common method
  stores "trauma" 0–1 that decays and drives shake as trauma², so small hits barely move and big
  ones punch ([Wayline game-feel course](https://www.wayline.io/learn/game-feel/1),
  [Mega Cat](https://megacatstudios.com/blogs/game-development/mega-cat-developer-juice-guide-v1-0-08-23-17)). *[source]*
- **Us (built 2026-11-06):** `scripts/game/feel.gd` holds the ladder: trauma decays in 0.5 s and
  shakes as trauma²; a hand press adds none, a scoring tool or impact 0.05–0.2 and sinks the cap
  up to 2× deeper, a push 0.3, milestone/curse/lock/blackout 0.3, cannon/boom/room shake/win
  0.5–0.8, squish 1.0. No hitstop: the host runs the clock, so a local freeze would desync. *[read]* Reference code: `~/Playground/refs/juice/saltmire-juice`
  (trauma shake and hitstop autoload). *[read, index only]*

### 6. Vary what repeats
- **Rule:** stock, identical sounds make feedback less distinctive and less informative (Wayline,
  above). *[source]*
- **Us:** the press sound gets a random pitch of 0.9–1.15 and is throttled to one per 60 ms
  (`room.gd:151`). *[read]* Godot's `AudioStreamRandomizer` does this per stream. *[read, refs index]*

### 7. Use the space around the action
- **Rule:** "constraints define sensation": the same move feels different in a cramped or open
  space ("without a wall, there can be no wall kick") (Swink, above). *[source]*
- **Us:** the room itself (light, ceiling height, echo) is a feel channel the narrator can change
  without text. *[opinion]*

### 8. Offer reduce-shake and reduce-flash
- **Rule:** let players scale or turn off shake and flashing (Wayline, above). *[source]*
- **Us (built 2026-11-06):** the camera reads the `shake` setting (0..1); `reduce_flash` turns
  the full-screen flashes into a faint tint (`hud.gd`). *[read]*

---

## Anti-patterns (don't)

### 1. Don't turn the volume up instead of linking it to success
- Amplified feedback lowered competence, curiosity and enjoyment in Kao et al. 2024; the authors
  think it weakened the sense of agency. *[source]* A critique attributed to Brendan Keogh warns
  that "more is better" juice makes game feel a vague concept
  ([via slides](https://www2.slideshare.net/totter87/you-made-a-game-now-what-6-game-feel-juicing-your-game)). *[source, secondhand]*

### 2. Don't put full juice on a routine action
- Full shake and hitstop on every footstep causes fatigue and hides the real impacts
  ([summary](https://gamedo-live.pages.dev/news/game-feel-juice-guide-indie-devs)); players call
  shake on rapid-fire weapons obnoxious ([itch.io comments](https://itch.io/post/10267763)). *[source]*
- **Us:** the button is pressed thousands of times per run. A single press must stay light;
  weight goes to streaks, milestones and changes. *[opinion, built on source]*

### 3. Don't let juice hide the game state or bury the cues
- Diablo III's screen gets so cluttered with effects that players lose the action; loud effects
  drown the subtle sounds players read threats from (Wayline, above). *[source]*
- **Us:** the narrator's voice is the main rule channel; nothing should mask it. Keep effect sounds
  quiet (user, 2026-11-03: "set the volume at 10%, the sound"; `Sfx.MASTER_VOLUME = 0.1`). *[opinion]*

### 4. Don't flatten everything to one intensity
- With every action at the same strength, players cannot tell what matters (Wayline). *[source]*

### 5. Don't let predictions snap back
- A wrong prediction corrected abruptly reads as rubber-banding, choppy and unpleasant
  ([Wayline: latency compensation](https://www.wayline.io/blog/input-latency-compensation-online-game-feel)). *[source]*
- **Us:** never predict an outcome the host may refuse (a payout, a pickup someone else may win).
  *[opinion]*

### 6. Don't shake a first-person camera hard or long
- Big shake causes nausea; long, frequent hit pauses feel disruptive (Wayline course; itch.io
  comments, above). *[source]* We are first person, where camera motion is the whole view. *[read]*

---

## Checklist for any new feedback
1. Which rung of the hierarchy (pattern 3) is it, and is it smaller than the rung above?
2. Does its size depend on what the player achieved (pattern 2), or does it fire the same for any input?
3. Does it play within 100 ms for the player who acted, without predicting an outcome the host decides?
4. If it repeats often, is it light, varied and throttled?
5. Can the crew still hear the narrator and see the button through it?
6. Does it show *that* something changed without telling *what*?

## Gaps in this research
- Swink's 100 ms figure and his full definitions come from secondary sources; the book was not read.
- Jonasson/Purho and Nijman ("The Art of Screenshake") talks were not watched; only summaries.
- Kao et al. 2024: abstract only; effect sizes not checked. Juul and Begy found no difference
  between juicy and plain versions of a tile matcher, so effects are not guaranteed
  ([Hicks et al. 2019 context](https://bibtex.github.io/CHI-PLAY-2019-HicksGDA.html)).
- Juicy audio research (Hicks et al., CHI PLAY 2024,
  [PDF](https://eprints.staffs.ac.uk/8527/1/3677084.pdf)) found and not read; worth a pass before
  sound work.
- Many tips here come from blogs and courses, not studies. The user's playtest decides.
