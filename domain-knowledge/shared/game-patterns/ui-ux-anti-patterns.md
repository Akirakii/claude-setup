# UI/UX anti-patterns: game feel and interaction

Anti-patterns to avoid, with Roblox as the main bad example. Written 2026-11-03 after the user
said the prototype has a "Roblox feel": not the looks, but **unpolished interaction design**.
Target: a minimal, elegant, mysterious game.

Each rule: **Don't** (the anti-pattern) · **Roblox** (where it shows up there) · **Us** (where it
shows up in this prototype, checked by reading the code) · **Do** (the alternative, with a good
example).

Tags: *[source]* = backed by a linked source; *[read]* = checked in our code; *[opinion]* = design
judgment, not checked.

## The one-line diagnosis
The Roblox feel = **the game tells you what to do with text and numbers instead of the world
showing you, and gives you many shallow actions instead of a few with weight.**

Game feel, as Steve Swink defines it, is real-time control of objects in a simulated space,
*with interactions emphasized by polish*: animation, sound and effects in harmony with input
([Wikipedia: Game feel](https://en.wikipedia.org/wiki/Game_feel),
[review of Swink's book](https://lizengland.com/blog/review-game-feel-by-steve-swink/)).
Every anti-pattern below is a place where text or a menu stands in for that polish.

---

## 1. Don't label every object with "Press E"
- **Roblox:** the platform ships a ready-made `ProximityPrompt` ("E: Open"). Developers already hit
  its limits: running out of keys, objects with several actions, prompts fighting the camera
  ([DevForum beta thread](https://devforum.roblox.com/t/proximity-prompt-studio-beta/844107?page=6),
  [ClickableOnly request](https://devforum.roblox.com/t/clickableonly-property-for-proximityprompts/3936076)).
  *[source]*
- **Us (fixed 2026-11-03, prompts removed):** `RoomText.prompt` put text on everything: "E: PRESS", "E: shop", "E: unplug Drinking
  Bird · F: pick up", "E: kick the box", "E: slap Bo", "E: master switch (all machines on/off)".
  One key does seven different things. *[read]*
- **Do:** let the object show its use. Norman: *affordances* are what an object lets you do;
  *signifiers* are the cues that announce them, and the signifier is what the designer controls
  ([IxDF: signifiers](https://ixdf.org/literature/topics/signifiers)). Inside has physical buttons
  and switches where it is clear when you can and cannot interact, with no text
  ([PC Invasion](https://www.pcinvasion.com/?p=132125)). A lever looks pullable; a plug has a cable;
  a hatch has a slot. At most a subtle highlight, never a sentence.

## 2. Don't give the core action no body
- **Roblox:** clicker simulators reduce the core verb to a click that makes a number go up
  ([simulator design guide](https://kitemetric.com/blogs/simulator-clicker-game-design-a-comprehensive-guide)).
  *[source]*
- **Us:** a press moves the button cap 5 cm and plays a beep (`room.gd:408`). No hands. Other
  players are capsules with no press animation (`puppet.gd`). The one verb the whole game is about
  has the least weight of anything in it. *[read]*
- **Do:** spend most of the polish on the one core action. A hand that reaches, deep and slow
  travel, a heavy click you feel, a sound with body, and friends visibly pressing. Swink's polish
  = animation, sound and effects agreeing with the input. *[opinion, built on source]*

## 3. Don't use menus where an object could do the job
- **Roblox:** simulators stack screen menus: shop, pets, rebirth, index, inventory, gamepass store
  ([example simulator UI kit](https://builtbybit.com/resources/modern-cartoon-simulator-ui.109159/),
  [shop GUI kit](https://kwstudioorg.itch.io/roblox-shop-gui-custom-gamepass-store-monetization-system)).
  *[source]*
- **Us:** the hatch opens a panel of priced buttons: "Click to order · E or Esc to close · F on a
  machine picks it up: throw it in here for 50% back". *[read]*
- **Do:** physical exchange. Dead Space shows health on the character's back and the inventory as
  a projection in the world, not a HUD ([Game Developer: UI in video games](https://www.gamedeveloper.com/design/user-interface-design-in-video-games),
  [Fagerholt & Lorentzon, *Beyond the HUD*](https://publications.lib.chalmers.se/records/fulltext/111921.pdf)).
  Caveat: diegetic UI is not automatically more immersive; studies are mixed. Use it where it fits
  the fiction, not as a rule ([GEM 2015 study](https://www.yorku.ca/mack/ieee_gem2015.html)). *[source]*

## 4. Don't annotate the world with floating text
- **Roblox:** name tags over every avatar, floating "+1" numbers, status labels. *[opinion: common
  Roblox convention, no source]*
- **Us:** floating press numbers, crit pops and "?!" (`room_fx.gd`); name and title tags over
  players ("Employee of the Month", `puppet.gd`); "UNPLUGGED"/"JAMMED" over machines
  (`machine_view.gd`); colour-coded subtitles per line kind. *[read]*
- **Do:** let the world react instead of being labelled. A machine that is unplugged is dark and
  silent; a cursed player is marked by how the room treats them. Inside and Limbo use no on-screen
  text at all ([Time: Inside review](https://time.com/4380020/inside-review/)). *[source]*

## 5. Don't hand out many cheap verbs
- **Roblox:** emote kits and one-key gags (dance, wave, point). *[opinion]*
- **Us:** sprint, jump, crouch, honk (Q), laser (R), carry (F), kick, slap, smoke: nine verbs,
  most of them gags with little depth. *[read]*
- **Do:** few verbs, each meaning a lot. Journey gives co-op players one verb, a chime, with no
  text or voice chat, and players build their own language from it
  ([Wikipedia: Journey](https://en.wikipedia.org/wiki/Journey_(2012_video_game)),
  [Game Developer interview](https://www.gamedeveloper.com/game-platforms/in-depth-hunicke-and-chen-talk-tgc-s-intriguing-new-i-journey-i-)).
  *[source]*

## 6. Don't fake drama with physics shoves
- **Us:** slaps are impulse pushes, the cannon knocks people back, boxes rain down, gravity drops,
  a ceiling arm grabs a player in place. Jolts without build-up. *[read]*
- **Do:** tension through anticipation and consequence, not impulses. In Buckshot Roulette the
  drama is a slow choice with an unknown outcome, not a shove
  ([GameCritics review](https://gamecritics.com/eugene-sax/buckshot-roulette-video-review/)).
  The descending ceiling is already this kind of tension. *[source + opinion]*

## 7. Don't explain every system out loud
- **Roblox:** systems announce themselves: popups, reward screens, "x2!" banners. *[opinion]*
- **Us:** "Fined 12 points", "Refund: 40 points", "Stakes. Win: … Lose: …", "Plus 12 points",
  first-purchase explanations for each item. *[read]*
- **Do:** teach with the world and sound. Limbo decided on no tutorial text from the start; when
  players got stuck, the fix was sound cues, not words
  ([GDC Europe: Carlsen](https://www.gamedeveloper.com/game-platforms/gdc-europe-i-limbo-i-s-carlsen-on-making-players-your-worst-enemy-and-your-best-friend)).
  Mystery = what is held back. *[source]*

## 8. Don't build a clicker simulator and expect it not to feel like one
- **Roblox:** "simulator" is a staple genre: click, collect, reinvest in upgrades, multipliers,
  auto-clickers ([guide](https://kitemetric.com/blogs/simulator-clicker-game-design-a-comprehensive-guide)).
  *[source]*
- **Us:** button + counter + shop + upgrades + "x1.5" multipliers + auto-press machines is that
  loop. Polishing it will not remove the association. *[read + opinion]*
- **Do:** keep the billion as a goal, but make the interesting part *what the button does*, which
  players discover, not *how fast the number grows*. *[opinion]*

## 9. Don't confuse minimal with no feedback
"Juice" (Jonasson & Purho, *Juice it or lose it*, 2012) is right that feedback matters, but
overjuicing turns effects into background noise, and Folmer Kelly argued that polish can cost
immersion ([Wayline: the perils of over-juicing](https://www.wayline.io/blog/the-perils-of-over-juicing),
[Game Developer: squeezing more juice](https://gamedeveloper.com/design/squeezing-more-juice-out-of-your-game-design-)).
- **Do:** few, strong, physical responses that echo the core action; silence in between, so the
  responses carry. *[source + opinion]*

---

## Checklist for any new feature
1. Does it need text on screen or over an object? If yes, can the object or a sound say it instead?
2. Does it add a key or a menu? If yes, can an existing verb or object carry it?
3. Is the response physical (motion, sound, light) and in the room?
4. Does it explain something players could discover?
5. Would it fit in a quiet white room, or does it need a joke to land?

## Gaps in this research
- Roblox-specific criticism of interaction design is thin online; most hits are tutorials and SEO
  pages. Rules 4, 5 and 7's Roblox examples are my observation, not sourced.
- Diegetic-UI immersion results are mixed; treat rule 3 as fit-to-fiction, not a law.
- None of this has been tested on our players. The playtest decides.
