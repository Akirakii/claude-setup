# Red Button Experiment: core design

The game in one page: the decided rules everything else hangs on. Detail lives in three docs:

| Doc | Covers | Its anti-patterns |
|---|---|---|
| `docs/gameplay-design.md` | runs, pressing, economy and hop, machines, events, rewards | `docs/gameplay-anti-patterns.md` |
| `docs/dialog-design.md` | the narrator: when it speaks, orders, memory, voice | `docs/dialog-anti-patterns.md` |
| `docs/ui-ux-design.md` | what is on screen and in the room, controls, feedback | `docs/ui-ux-anti-patterns.md` |

These docs hold current rules only. A rule the user decided carries a tag with the date and, where
it helps, their words: *(user, 2026-11-03: "…")*. Old versions live in git history. Open items:
`docs/questions.md`; agreed but unbuilt: `docs/todo.md`. Market research: `~/Playground/game-design-research`
and `~/Playground/assemblia/docs/research.md`.

## Pitch
A crew of 2–8 friends is locked in a blank testing room with one red button. To escape they must
press it **1,000,000,000** times. Toys hit it harder (a hammer, a bat, a cannon), but a narrator keeps changing what the
button does. Simple action, exponentially chaotic.

Tagline idea: "Press it one billion times. With friends. Probably."

## Fantasy
**Discoverability** (user, 2026-11-03: "this game fantasy is all about discoverability"). Nothing
tells the crew what a thing does: items, the room, the hatch, the exit and the button's rules are
found out by trying, and blamed until they prove their value. Test for any feature: does the
player find this out, or are they told?
- **Signal *that* something changed, never *what* it means** (user, 2026-11-03: "that
  recommendation make sense.. record that for future ideas"). A change gets a sound, a light and a
  visible change on the thing itself (the button turns a colour), with no explanation. The crew
  finds out what it does by trying, and whoever got caught gets blamed. Nobody is caught out by
  something invisible, and nothing is explained.
- **Full of mysteries; a stream spoils only a fraction** (user, 2026-11-03: "the game is full of
  mysteries.. watching your favorite streamer or youtuber will just spoil a fraction of surprises
  the game holds.. like stanley parable"). Many small hand-made mysteries, each rare, so one run
  shows a few and a viewer's crew still meets ones they never saw.
  - **Hand-made, each a different formula** (user, 2026-11-03: "hand made mysteries makes sense
    and different formula"): no generated variants; a new mystery changes *how* it surprises, not
    just its skin. Formulas so far: a world behind the door, a solo trap, a private reality
    (Freedom, the ghost), a hidden trigger, a personal callback, the game noticing a spoiler.

## Genre frame: a friendslop escape room
*(user, 2026-11-06: "record this", on the frame below)*
- **The button is the lock.** 1B is the clear goal; a hand press (+1) can't reach it, so "what
  will?" is the first aha. Each rule change is a new lock, shown but not explained. The narrator
  is the game master; the hatch, exit and door are the hidden compartments. Only half an escape
  room: borrow the craft (goal, flow, GM, hints, climax), not one-shot puzzles
  (`docs/escape-room-patterns.md`).
- **Fair aha, messy process.** Escape rooms cut the *process* (doing it once you know) as
  tedium; friendslop puts the comedy there. The answer stays fair and clean; carrying it out as a
  crew is chaotic ("STOP, Bo").
- **Needs:** a goat as well as a hero (blame), failure that is funny and unlocks something,
  puzzles that need talking, no single efficient route one player can run alone.
- **Test for any feature:** is the *answer* fair, and is the *attempt* funny with friends? Only
  the first is an escape room; only the second is just chaos.

## Pillars
1. **One button, one number.** Everything is something you do with, for or against the button.
   The button follows the crew into every world behind the door (user, 2026-11-03: "yes that is
   the idea.. you are right", to dropping "one room" for the door).
2. **Hands are the scarce resource.** Pressing, items, events and puzzles all compete for them.
3. **Fun to lose.** Losing is funny and unlocks something; winning takes a new crew ~3–5 runs (target).
4. **The game remembers.** The narrator remembers what each player did, this run and past runs.

## Core loop
- **Press:** a player presses the button by standing next to it; each hand press is +1.
- **One number:** the count is both progress and the crew's shared money. Buying spends it.
- **Milestones** every ×10 (eight stages to 1B) reset the ceiling, raise the button's sensitivity
  (items count ×10 more; a bare hand stays +1) and make the narrator meaner. From stage 3 an exam
  in the dark gates each one.
- **The ceiling** is the run's timer: it falls, and reaching the crew loses the run.
  It falls on its own (on again, user 2026-11-03: "turn ceiling timer back on"; see
  `docs/gameplay-design.md` → Run structure).
- **Win:** the count reaches 1B and the hidden exit opens, or one of five other endings (routes).
- **Five kinds of moment**, each a different question (design v2, `docs/design-v2.md`): items
  ("what is this for?"), moods ("what does the button want?"), chores ("who leaves the button?"),
  exams in the dark ("who can see?") and paths ("what if we do the weird thing?"). See
  `docs/gameplay-design.md`.

## Players and room
- 2–8 players online co-op; build and tune the MVP for 2–4. First person.
- A blank white testing room: the button in the centre, the narrator's eye set into the ceiling,
  a hidden shop hatch in the east wall, a hidden exit in the south wall. Details in
  `docs/ui-ux-design.md`.

## Tech
- Godot 4.7, GDScript; player-hosted, host-authoritative; Steam lobbies (GodotSteam) or join by address.
- Physics sync of many machines across players is the main tech risk; test early.
- 3D assets: Meshy AI (MCP), for a few props once the core works.

## The full game (design v2, built 2026-11-05)
User, 2026-11-05: "make a cohesive design.. enough for a finished game.. then try to implement
everything until finished". Settled through four thesis/antithesis rounds with a critic agent
(`docs/design-dialectic.md`); build notes, how to run and what is unchecked: `docs/build-v2.md`.
15 items, 5 moods + 2 room moods, 6 chores, 4 exams + the Greedy gate, 6 routes (endings), 5
loops, unlocks by loss and deed. **Test:** do 4 friends laugh within 5 minutes, and do they ask
for another run?
