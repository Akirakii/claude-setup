# Pet the Cat: design

User, 2026-11-07: "lets replace the button but with a cat.. the name of the game is: pet the cat..
there is no narrator. only 5 minute timer.. players need to keep the cat calm.. they need to keep
petting.. if you stop.. the cat gets angry and can kill you and you can revive your friends.. you
have to survive 5 minutes and then you win.. there are parkour games.. no shop.. there are other
minigames.. like floor is lava".

Rules tagged (user) come from that message; (Claude) marks picks made while the user was away,
to confirm or change. Numbers live in `scripts/core/tuning.gd`.

## Pitch
2–8 friends, one room, one cat. Keep petting it for 5 minutes. Stop, and it kills someone.

## Rules
- **Win:** survive 5:00 with at least one player standing. (user)
- **Lose:** every player is down at once. (Claude)
- **Calm meter (0–100)** is the one number. It drains on its own; each player petting fills it. (user: keep petting)
  - Drain rises over the 5 minutes, so one petter holds it early and it takes two later. (Claude)
  - **Hands are scarce:** petting, reviving and the minigames all pull on the same few players. (Claude, carried from Red Button)
- **Moods**, shown on the cat (colour, ears, puffed fur, sound), never explained: content → grumpy → furious. (Claude)
- **Rage:** at 0 the cat leaps at a player and downs them on contact. (user: "can kill you")
  - Target = whoever stopped petting most recently, so blame is readable. Nobody petted: the nearest. (Claude)
  - A kill satisfies it (calm back to mid). Friends can also pet it mid-chase to calm it down. It gives up after a while. (Claude)
  - Sprinting outruns it; walking doesn't. (Claude)
- **Down and revive:** a downed player lies where they fell; a friend holds E on them for 3 s. (user)
  - The downed player floats as a slow ghost meanwhile, so they stay in play
    (gameplay-anti-patterns #2). Solo has no revive: practice mode. (Claude)
- **Crew size and difficulty** scale the drain: solo ×0.75 … 8 players ×2.8; Kitten ×0.75, Cat ×1,
  Lion ×1.3, picked by the host in the lobby. (Claude)
- **Report card** at the end names the best petter, who made the cat snap, the most clawed and the
  paramedic: blame with a face (gameplay-anti-patterns #7). (Claude)
- **No narrator, no shop.** (user) Minigames are announced with a klaxon and a title card only. (Claude)

## Minigames (user: parkour, floor is lava, "etc")
Each one changes where the cat is or what the room does, so keeping it petted needs the skill. (Claude)
- **The Floor Is Lava:** a 3 s warning, then touching the floor downs you. Stand on furniture;
  the cat's tower has ledges in reach. (user)
- **Top Shelf (parkour):** the cat jumps to a high shelf and floating platforms appear; climb to
  pet it. Falling only costs time. (user: parkour)
- **Zoomies:** the cat sprints laps round the room; you pet it by keeping up. (Claude)
- **Lights Out:** the room goes dark, each player gets a dim light, and the cat hides on top of
  some furniture; find it by the purr and its glowing eyes. (Claude)
- **Robot Vacuum:** a vacuum heads for the cat; reaching it scares the cat (−35 calm). A player
  standing in its way turns it back, which takes a pair of hands off the cat. (Claude)
- **Spilled Milk:** the floor is slippery; you slide past the cat. (Claude)
- **Belly Up:** the cat rolls over for 7 s. No drain, but the first hand on the belly sets it off
  at that player. The one moment petting is wrong (gameplay-anti-patterns #5). (Claude)

First minigame at ~0:25, then one every 32–44 s, never the same twice in a row, ~20 s each
(Belly Up 7 s), after a 3 s klaxon warning with a title card. (Claude)

## Test
Do 4 friends laugh within 5 minutes, and ask for another round? Fun is judged by the user's
playtest, not by automated runs.
