# Dialog anti-patterns: narrator lines

Mistakes to avoid when writing narrator lines. Rules 2-7 come from games whose narrators or
talking companions players complained about, researched 2026-11-03 after the user asked for "bad
narrator games". Companion to `docs/gameplay-anti-patterns.md` and
`docs/ui-ux-anti-patterns.md`.

Each rule: **Don't** · **Evidence** · **Us** (where it shows up in this prototype) · **Do**.

Tags: *[user]* = the user's decision; *[source]* = backed by a linked source; *[read]* = checked
in our code; *[opinion]* = design judgment, not checked.

---

## 1. Don't name the mechanic: no "remember" or "memory" lines
- **Rule:** the user decided this on 2026-11-03: "remember and memory is too explicit". *[user]*
- **Evidence:** screenwriting calls this "on-the-nose" dialogue. The line says the point outright
  instead of letting the listener get it from what is said
  ([Helping Writers Become Authors](https://www.helpingwritersbecomeauthors.com/on-the-nose-dialogue/),
  [Final Draft: subtext](https://www.finaldraft.com/blog/how-to-write-subtext-in-dialogue)).
  These sources are about film and fiction. Nothing game-specific was found yet. *[source]*
- **Us:** the past cursed presser callback ("...pressed the cursed button. I remember. Everyone
  remembers.") and the past-run callback ("...pressed the least. I remember.") in
  `scripts/core/memory_director.gd`. The endings were cut first, then the user removed both lines
  completely (2026-11-03: "not just that part.. the whole thing"). Also cut: the stage-start
  "compressed %d crews in a row" streak line (a past-run recall) and "Remember:" in an idle taunt.
  *[read]*
- **Do:** never have the narrator talk about its own memory. Even with the word "remember" gone,
  the user also cut the bare past-run facts, so don't add a line whose only job is to recall a past
  run. *[user]*

## 2. Don't comment on everything
- **Evidence:** Biomutant's narrator was criticised for "commenting everything you do" and the
  developers patched in a way to mute it
  ([TechRaptor](https://techraptor.net/gaming/opinions/biomutant-narrator-stanley-parable),
  [Digit](https://www.digit.in/news/gaming/biomutant-patch-lets-you-mute-the-narrator-59650.html)).
  Forspoken's constant Frey/Cuff banter got a patch and a "Cuff Chat Frequency" setting
  ([Axios](https://www.axios.com/2023/05/25/forspoken-ai-character-dialogue),
  [Inverse](https://inverse.com/gaming/forspoken-cuff-chat-frequency-setting-banter-slider)).
  Fenyx Rising's two narrators "narrate every single moment"
  ([Laptop Mag](https://www.laptopmag.com/uk/reviews/immortals-fenyx-rising)). *[source]*
- **Us:** a reaction quip needs 4 s since the last line and `Tuning.QUIP_GAP` (9 s) since the
  last quip (`game_sim.gd:212`); the first stage is silent (`game_sim.gd:202`). *[read]* Whether
  that still feels like too much talking is for the playtest. *[opinion]*
- **Fixed (2026-11-03):** cut the "Subject X has left" announcement, the jump-count and kicking
  quips, and the idle "Progress report" (the HUD shows progress); idle taunts now wait 45 s of
  silence instead of 22 s (`Tuning.IDLE_TAUNT_AFTER`). *[read]*
- **Do:** keep silence the default. Speak when players must act (an order, a rule change, a fine)
  or when something worth laughing at just happened.

## 3. Don't repeat lines
- **Evidence:** Skyrim's guards repeat a few stock lines, which made "arrow in the knee" a meme
  ([Know Your Meme](https://amp.knowyourmeme.com/memes/i-took-an-arrow-in-the-knee)); PC Gamer
  lists barks that "make you wish you were deaf"
  ([PC Gamer](https://pcgamer.com/which-npc-bark-are-you-most-sick-of-hearing)). Navi's
  repeated "Hey! Listen!" is the standard example of an annoying companion
  ([Wikipedia: Navi](https://en.wikipedia.org/wiki/Navi_(The_Legend_of_Zelda))). In Getting Over
  It, a game played over and over, a player found the monologue repetitive after many wins, and the
  developer agreed ([Steam thread](https://steamcommunity.com/app/240720/discussions/0/2549465882933888781)).
  Hades limits each character to one conversation per visit
  ([Nintendo Wire](https://nintendowire.com/reviews/hades/)). *[source]*
- **Us:** fixed 2026-11-03: `Lines.pick` is now a shuffle bag, so no pooled line repeats until its
  pool is used up, across runs in one session; idle taunts use it too. Event intros and outros
  now rotate 3 variants each through `Lines` pools (MESS, FIRE_TAIL, DECOY_ON, ...); the instruction
  part stays fixed so the rule reads the same every time. *[read]*
- **Do:** don't repeat a line until its pool is used up, and keep that across runs if the crew
  plays several runs in one evening. *[opinion]*

## 4. Don't solve it for the players
- **Evidence:** Horizon Forbidden West's Aloy gives puzzle hints "seconds after" the quest updates;
  NME said it took away "the joy of working something out", and the Burning Shores DLC waits longer
  before hinting ([NME](https://www.nme.com/reviews/horizon-forbidden-west-review-3160861),
  [GamesRadar](https://www.gamesradar.com/horizon-forbidden-west-is-the-latest-aaa-game-to-realize-players-arent-idiots-who-immediately-need-puzzles-explained-to-them/)).
  Skyward Sword's Fi is criticised for stating the obvious, and the HD version cut back her
  interruptions ([Zelda Dungeon](https://www.zeldadungeon.net/daily-debate-was-there-still-too-much-hand-holding-in-skyward-sword-hd/)).
  *[source]*
- **Us:** the silent first stage leaves players to work out the room; the cursed button has no
  prompt (`docs/gameplay-design.md`). *[read]* I didn't check whether other events explain
  themselves too soon.
- **Do:** let the crew argue it out first. Only hint after a real stall, and hint at the rule, not
  the answer. *[opinion]*

## 5. Don't talk over the panic
- **Evidence:** a Forspoken reviewer argued that combat dialogue was a mistake because players
  need to focus on surviving ([Exputer](https://exputer.com/exputer/forspoken-biggest-problem/)).
  *[source]*
- **Us:** memory callbacks only fire at calm moments (stage start, after a blackout;
  `memory_director.gd:4`). Fixed 2026-11-03: quips are skipped during an order, a blackout minigame
  or the last 10% of ceiling (`game_sim.gd`, `quip`). *[read]*
- **Do:** during a countdown or the ceiling dropping, speak only lines players need to act.
  *[opinion]*

## 6. Don't let the narrator take the stage from the players
- **Evidence:** a Fenyx Rising preview said the narrators "completely dominated" the stage, with
  "not nearly enough Fenyx" ([Destructoid](https://www.destructoid.com/immortals-fenyx-rising-is-messy-but-has-potential/)).
  Borderlands 3's villains were called one-dimensional and annoying, and its humour dated
  ([Windows Central](https://windowscentral.com/borderlands-3-reviews-are-i-still-have-questions),
  [PC Gamer](https://www.pcgamer.com/borderlands-3-review/)). *[source]*
- **Us:** in friendslop the friends are the show (`docs/gameplay-anti-patterns.md`, the one-line
  diagnosis). *[read]*
- **Do:** make the narrator's line a setup for the crew's reaction, built on facts about what they
  did. Avoid internet jokes that will date. *[opinion]*
- **Fixed:** "Bold strategy." (a movie meme) became "It was doing its best." (2026-11-03). *[read]*

## 7. Don't lock the voice to all or nothing
- **Evidence:** Forspoken added a chat frequency slider, and Biomutant added a narration slider
  and a mute ([Inverse](https://inverse.com/gaming/forspoken-cuff-chat-frequency-setting-banter-slider),
  [Digit](https://www.digit.in/news/gaming/biomutant-patch-lets-you-mute-the-narrator-59650.html)).
  *[source]*
- **Us:** the Esc menu has a voice on/off toggle; subtitles and cue sounds stay on
  (`narrator.gd:27`). *[read]*
- **Do:** keep the toggle. Here the narrator *is* the game (orders, rules), so it's better to cut
  optional quips than to add a frequency setting. *[opinion]*

## Research gaps
- Most evidence is reviews and player threads, not developer postmortems.
- Studios reportedly built "dialogue exhaustion" systems after Skyrim; I found no developer
  source for that, so it isn't used here.
