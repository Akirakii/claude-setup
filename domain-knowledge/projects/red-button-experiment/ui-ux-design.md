# UI/UX design

What players see, hear and touch. Core loop: `docs/core-design.md`. Check new features against
`docs/ui-ux-anti-patterns.md`.

## Rule
- **Every rule change is visible on screen and audible.**

## Title menu
User, 2026-11-03: "improve main menu to be more intuitive"; this shape, "yes that is right".
- Two big choices: **Start an experiment** (red; hosts on Steam when Steam runs, else by address)
  and **Join a friend** (with Steam: how to join from an invite or Join Game; without: the address
  form). Back returns to the two choices.
- Name is small, filled in from Steam.
- **Play by address ▸** folds away: host by address (port), join by address, host with 2 bots
  (testing). Status and errors show under the buttons; Quit sits small in the bottom-right.

## The room
- A blank white testing room; the button in the centre.
- **Pedestal:** the count on all four sides, with the goal under it ("40 / 100", discovery
  review 2026-11-06); nothing else.
- **Timer screen:** one wide black screen in the middle of the north wall, the ceiling seconds in
  red digits (with speed-up, "PAUSED" in a blackout); top at 1.9 m so the falling ceiling never
  covers it (user, 2026-11-03: "a monitor or TV screen ... showing the timer in red color"; a
  ceiling-hung four-sided one was tried and dropped: players at the button would have to look
  straight up; "one side is enough"). Only players facing north can read it, on purpose: one player
  reads it out to the rest (user, 2026-11-03: "one player can communicate the timer to the rest").
  Clock format MM:SS.cc, e.g. 02:33.01 (user, 2026-11-03: "00:00:00", then "use ." before the
  hundredths, the stopwatch standard, so it does not read as hours) in a seven-segment LED font (DSEG7),
  counting down smoothly between snapshots.
- **Red end line on the walls removed** (user, 2026-11-03); the monitor shows how close the loss is.
- **Narrator's eye** set into the ceiling, half sunk in, looking down; it comes down with the
  ceiling (user, 2026-11-03). It looks at whoever the narrator names; a spotlight finds them.
  Hidden for now (user, 2026-11-03: "hide for now the camera narrator"); the spotlight stays.
- **Shop hatch:** a prison-style food hatch in the east wall, hidden until it slides out with a
  low grind; no "SHOP" sign. One item-sized slot; it stays shut while you browse and spits the
  item out when bought (user, 2026-11-03).
- **Shop menu:** a grid of white cards, one per item: its picture (the item's own model rendered
  live on white, `scripts/ui/item_picture.gd`), name and price; no description, no hint of
  what it does (user, 2026-11-03: "a grid of screenshots of the items", "on white background") (user, 2026-11-03, see `docs/gameplay-design.md` → Economy and shop).
- **Exit:** a wall-white panel flush with the south wall, no "EXIT" sign; it lifts only on a win.
- **No wall display, no bench, no records board** (user, 2026-11-03: "the display is showing too
  much", "ok remove"; the bench spoiled the joke).

## Screen (HUD)
- **No corner UI** (user, 2026-11-03): no counter, goal, ceiling bar, crew list, controls hint or
  host info in the corners.
- **The centre stays:** the current order/event panel (with the ORDER badge), subtitles, personal status (cone, reversed controls, carrying), the end-of-run panel,
  and the shop and Esc menus.
- **No interaction text** (user, 2026-11-03: "remove all text for interaction", "like press"):
  nothing appears when you look at the button, a machine, the hatch or a player; no key letters
  in any hint. Objects must show their use themselves.
- **The crosshair answers without words** (Claude's pick, 2026-11-06, to confirm): faint over
  nothing, larger and solid over anything E acts on. It shows *that*, never *what*.

## Controls
- WASD move, Space jump, Ctrl/C crouch, Shift sprint.
- **Hold keys: toggle** (Options, off by default; audit 2026-11-06, accessibility): one press holds
  the valve, the crack, the cable or a carried thing, the next lets go.
- **The press has a body:** an empty hand pushes forward in your view; others see your arm push
  out (audit 2026-11-06, ui-ux anti-pattern 2).
- **E / left click does everything** (user, 2026-11-03: "E/click for interact, equip and carry if
  hold"). The item decides, so a press never waits to tell a tap from a hold:
  - empty hand by the button: press it; looking at the hatch, a player, a box: act on it;
  - looking at a small item (hammer, bat, ball): it goes in your hand (one hand, one item);
  - looking at a big item (monkey car, cannon): carried on the beam while E is held; a tap on a
    loaded cannon fires it; let go of E with it pushed into the hatch and it is sold;
  - item in hand: use it (hammer and bat swing; the ball winds up while held, thrown on release);
    looking at a cannon: load it; at the hatch: return it.
- **G** drops what is in your hand. Hold F still carries on the beam (for anyone who expects it).
- Esc menu: the options list (same as the title menu's Options: volume, effects, narrator and room
  hum volumes, narrator voice, subtitles (off by default; on, the narrator's lines and orders
  show on screen, gap review 2026-11-06), sensitivity, invert, field of view, camera shake, reduce flashing,
  full screen, v-sync, key rebinding), invite, leave. No honk and no laser pointer (user,
  2026-11-03: "remove laser with right click and remove honk").

## Feedback
- Each press: the cap sinks, a click, a floating "+1" (tools and impacts show their value).
- Game audio is quiet: master volume 10% by default; new sounds no louder than existing ones
  (user, 2026-11-03).
- **Visual dictionary** (one meaning each, never broken; `docs/visual-communication-patterns.md`
  #4). New signals reuse these or add an entry that clashes with none:
  - *colour change + chime on the cap*: the button's rule changed (never says to what);
  - *glow*: live, or changed; *brighter*: more important;
  - *grey*: locked; *a dark beat*: a dud (the hit did not count);
  - *red spotlight on a player*: the one blamed or named (also who moved, in Freeze);
  - *player colour*: who (Okabe-Ito colour-blind-safe set, `scripts/game/puppet.gd`);
  - *a red ring on the floor*: the area a blast will hit (lit dynamite, a hot box near its end,
    the valve near red), drawn at the real radius (audit 2026-11-06);
  - *a shape on a body*: who, again (each player colour has one: circle, triangle, square,
    cross, diamond, ring, hexagon, bars; on chest and back, and on the Sequence wall), so colour
    never carries a fact alone (audit 2026-11-06);
  - *orange glow on a body*: it carries something hot (the Hot Potato over a head, an ember at the
    feet; the potato holder sees it glow at the bottom of their own view, pulsing faster as time
    runs out) (gap review 2026-11-06);
  - *the same chime falling*: a mood ended, the button is back to normal; *a metal clank*:
    Contrary refused that hit (gap review 2026-11-06).
- **Sounds come from where they happen:** a player's action from their body, shop sounds from the
  hatch, the cannon from the cannon, a chore's start from its own wall (gap review 2026-11-06); only room-wide moments (mood, slam, lock, blackout,
  countdown, milestone) are flat.
