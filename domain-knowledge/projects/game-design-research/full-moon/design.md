# Full Moon: design (polished sketch for a first build)

Claude, 2026-11-11, after 4 critic rounds (`critic-r1.md` … `critic-r4.md`) and the user's questions on nights and
revives. Working title "Full Moon" (Claude). Online co-op, 3–6 friends, one developer, ~3–4 months. The user's own
words and pillars U1–U10 are in `thesis-r1.md`. Tags: (Claude) = Claude's call, free to change; untagged = from the
user's words. Not played: every number is a starting value with a target to tune toward. Scene numbers are computed
with a script from the tables below.

## The game in one sentence
Friends spend the nights up to the full moon in a mansion where they keep starting to turn into legendary creatures:
put together what the sick friend feels and what the others see, give the right cure in time, because a friend who
fully turns must catch one of you to become human again, or die.

- **Job:** tend the cures (they regrow in the garden, kitchen, greenhouse, cellar and tree house), keep a tool in hand,
  keep checking on each other.
- **Choice:** cure now on one sign (a lean, and a wrong cure makes it worse), or get another sign first while the cure
  weakens every second. For the patient: check a strange feeling yourself (walk to a lamp, the meat, a friend) or stay
  put to be grabbed and cured. For a turned friend: hunt (stay in the night, cost the crew a candle) or hold back.
- **Goal:** be alive at the 5th dawn.

## Terms
- **Case:** one friend's sickness, from its first sign until they are cured or fully turned (75 s if nobody acts).
- **Inner sign:** only the sick player gets it, on their own screen or in their own ears.
- **Outer sign:** only the others see it, on the sick player's neck, face or mouth. You can't see your own.
- **Tool sign:** shows only through a tool (thermometer, lantern), to whoever holds it; tools read others, never yourself.
- **Trick:** a fake inner sign the house plays on a healthy player (Claude).
- **Cure:** wolfsbane (werewolf), garlic (vampire), salt (zombie). Given, it cures; held up, it shoves its creature back.
  It never tests anything.
- **Run:** the 5 nights played together (Claude).
- **Candle:** one revive the whole crew shares (Claude).

## What a new player is taught (3 rules)
1. Friends will start turning into monsters. You can't see your own outer signs, and only you feel your inner ones:
   tell each other.
2. Every sign rules out one creature (the journal shows which). Give the right cure: sooner is stronger, and a wrong
   one makes it worse.
3. A friend who fully turns must catch someone or die. Hold up its cure to shove it back.

Found by playing, each shown in the world: a pan knocks a friend out; grabbing holds them; while held or out cold the
dark veins stop creeping; a real inner sign grows near its trigger and a trick doesn't; a cured friend keeps a scar;
the garden makes everyone read cold; cures regrow where they were picked. Taught when it happens: the dawn screen
(candles, omen), the lone survivor's self-cure, what ghosts can do (to the dead).

## The signs
Each sign rules out one creature: one sign leaves two, two signs from different rows leave one. The % is how often each
of the two creatures shows that sign. Two signs from the **same** row only lean (heartbeats, then fangs: vampire 58%).

| Rules out | Inner (patient only) · its trigger | Outer (others see) | Tool (holder sees) |
|---|---|---|---|
| **zombie** (werewolf or vampire) | you hear friends' heartbeats · louder close to a friend · W 50% V 70% | fangs when they talk · W 40% V 70% | lantern: eyes shine back · W 70% V 40% |
| **werewolf** (vampire or zombie) | lamps hurt, your screen blooms · worse at a lamp · V 70% Z 40% | grey skin · V 50% Z 70% | thermometer: cold · V 60% Z 60% |
| **vampire** (werewolf or zombie) | you crave raw meat, your view drifts to it · stronger in the kitchen · W 70% Z 50% | drooling · W 40% Z 70% | (none) |

**When signs appear** (one new sign per kind per stage, so neither side can name the creature alone before stage 3):
| Time in the case | First sign | Then | Tools |
|---|---|---|---|
| Stage 1 (0–25 s) | one sign: inner (half the cases) or outer (the other half) | | readable from the start, each by its % |
| Stage 2 (25–50 s) | one sign of the other kind | dark veins start up the neck | |
| Stage 3 (50–75 s) | second inner and second outer sign | veins reach the face | |
| 75 s | turns | | |
- When the first sign is outer, the patient doesn't know yet: a friend has to notice ("Bo, open your mouth").
- The first inner and first outer sign come from the same row about half the time; then a tool or stage 3 is needed.
- The dark veins are the same for every creature: they show how late the case is, never which creature. They're on the
  neck, so the patient can't see their own.
- The one-sign lean is 51–55% (computed): a coin flip with a slight edge, on purpose. The % spread is the dial if the
  journal's % should matter more.

**Look-alikes (Claude): each kind of sign can lie.**
- Inner: tricks. A healthy player sometimes hears heartbeats, flinches at a lamp or smells meat for ~8 s, then it fades
  (about once every 3 min per player, more each night). Tricks never hit a sick player, follow the same 60 s skip after a
  cure as real cases, and can start from 0:20. A trick doesn't grow near its trigger; a real sign does.
- Outer: scars. A friend cured after stage 1 keeps one outer sign from their case for the rest of the run, at most one
  scar per player (a new one replaces the old). Cured in stage 1 = no scar.
- Tool: anyone who was in the garden in the last 30 s reads cold.

## Rules
**Cases (U3, U8).** The first case of a night starts at a random time between 0:20 and 1:30. The next starts GAP =
180 s ÷ (living players) × a random 0.25–1.75 after the last case ended. Sometimes a second case starts 10–30 s after a
case starts (DOUBLE: 10% of cases on night 1, up to 30% on night 5). Never more than 2 at once. The player is random,
skipping anyone cured or turned back in the last 60 s.

**Cure odds (U6, Claude's curve).** They slide down every second, fastest at the start:
| Seconds into the case | 0 | 10 | 25 | 50 | 75 |
|---|---|---|---|---|---|
| Right cure works | 95% | 82% | 65% | 43% | 30% |
(Formula: 30% + 65% × (1 − t/75)^1.5.) Each early second costs about 1–1.5 points.

**Giving a cure.** 2 s, one hand; the patient holds still, is held, or is out cold. The cure is used up.
- Right cure: works with the current odds. A failed roll makes the patient shudder: the kind was right.
- Wrong cure (Claude): the case jumps 25 s ahead, and every sign due in those 25 s bursts out at once; past 75 s, they
  turn on the spot. Everyone sees whose cure it was.
- On a healthy player: they just eat it. No shudder, no burst.
- A friend gives it; you can't cure yourself unless you're the last one alive.

**Holding and knocking out (U7).** Grab a friend (both hands): their case runs at half speed and the veins stop; they
can struggle free in 3 s. A pan or candlestick knocks them out for 20 s: the case at a third of the speed, their
screen black (no inner signs to report, even on Discord), their eyes closed (the lantern reads nothing). After waking,
nobody can knock them out again for 20 s. The pan does nothing to creatures.

**Turning (U8, U9, U10).** At 75 s the friend turns over 2 s: a holder is thrown off, nobody can be caught during it,
and every sign of that creature shows. A second case that reaches 75 s while a creature is out waits there (curable at
30%) until that creature catches someone or dies. First build: the creature is the player's own body in its creature's
look, 20% faster than people, no powers. HUNGER = 20 s + 60 s ÷ (people left to catch) (1 left: 80 s; 2: 50 s; 5: 32 s).
A catch = holding a player for 2 s; a friend breaks it by shoving with its cure. Caught = that player dies and the
creature turns human. Out of time = the creature player dies. Full game: one power each (werewolf tracks footprints,
vampire flies to the tree house, zombie: TBD).

**Shoving (Claude).** Holding up a creature's own cure shoves it 3 m back when it comes within 2 m in front of you; that
cure then can't shove for 3 s. Two armed players cover each other's gap; one alone can't hold out.

**Cures and tools (Claude).** Six cure spots: wolfsbane ×2 (garden beds), garlic ×2 (kitchen, greenhouse), salt ×2
(cellar, tree house). A spot regrows 120 s after its cure is used up (given right or wrong). Cures can be dropped and
picked up; at most 2 of a kind exist, held ones included. Two thermometers and two lanterns lie at random spots each
night. Two hands each (a cure, a tool, a pan); holding a friend takes both.

**The dead (Claude).** A dead player is a ghost until dawn. Ghosts can talk (on Discord nobody can stop them), push small
loose objects slowly (never held ones), and see the dark veins glow from the first second of every case: they know who
is sick, never which creature. Dying makes you a spotter, but a catch costs the crew a candle.

## The run: 5 nights to the full moon (Claude's recommendation; bends U2, the user is weighing it)
- 5 nights of ~6 min (first build: one 8-minute night). The moon grows each night: cases come faster (GAP ×1.3 on
  night 1 down to ×0.6 on night 5), doubles and tricks get more common, cures regrow more slowly (120 s → 160 s).
- **Candles:** ⌈players ÷ 2⌉ + 1 at the start (3 players: 3; 4: 3; 5–6: 4), in a row in the hall.
- **Only a catch costs a candle.** A caught player comes back at dawn only by using one. A creature that ran out of time
  wakes human at dawn for free. So a turn is a fight to make the creature starve, not a volunteer walking into it, and a
  turned friend chooses: hunt (stay in the night, cost the crew a candle) or hold back.
- More caught than candles: the living choose who comes back. A night where nobody is caught relights one candle (up to
  the starting count).
- **Dawn (taught when it happens):** the moon shows an omen: tomorrow's likeliest creature (half the next night's cases;
  the other two a quarter each), which moves the one-sign lean to ~62–68% toward it. The crew may spend a spare candle on
  one thing for the next night: a third cure bed of one kind (that kind's cap becomes 3) or a third tool. Candles are
  lives or gear: a safe crew keeps them, a bold one buys an edge.
- **Night 5:** no dawn after it. Every player alive at the 5th dawn wins (U2's "survivors win", moved to the last night).
  The run is lost if, after a dawn's candles, nobody is alive.
- Target (Claude): a good crew reaches night 5 with 0–1 candles, so the full moon decides the run.
- Why: the dead wait one short night at most (R.E.P.O.'s "2–3 dead players watching"); spare candles become a choice
  (keep a life, or buy a bed or a tool); the hits carry a growing stake across rounds (research.md 2026-11-11).
- One-night version (if the user keeps U2): one 12-minute night with the same rules, no candles; a ghost who pushes the
  right cure into a sick friend, when it works, comes back alive.

## Scenes
**3 players (Ana, Bo, Cy), night 2, minute 2.** Bo: "I hear heartbeats. Yours." Werewolf or vampire, or a trick. He
steps up to Ana: louder, so it's real (4 s in: 90%). Ana has the thermometer and garlic; Cy is in the garden picking
wolfsbane. Ana reads Bo: not cold. With heartbeats, not cold leans werewolf 68%, so garlic would be a bad bet. Ana grabs
Bo to slow it (half speed) and shouts for Cy. Cy runs in 26 s later; Bo's case is only at 17 s (74%). Wolfsbane: it
works. Cured in stage 1, so no scar. Last night's omen said werewolf, which is why Cy was in the garden.

**6 players, night 5 (full moon), 1 candle left.** A double: Dee hears heartbeats; nobody has noticed Eli's grey skin yet.
Fae says she smells meat: she walks into the kitchen and it doesn't get stronger, a trick. The ghost of Gus (caught on
night 4, no candle for him) says "Eli's veins are glowing". Hal pans Eli to slow him, so now Eli's screen is black and
the lantern can't read his closed eyes. Dee's thermometer reads cold, but she just came in from the garden. Ivy gives
Dee garlic on a guess: wrong. Her case jumps 25 s, and drool bursts out: heartbeats and drool, so werewolf. The
wolfsbane is in the tree house. Eli wakes and turns first: grey skin and drool, a zombie. Two players hold garlic, which
can't shove it. Eli hunts: there's no dawn after tonight.

## Dominant-strategy notes (Claude; critic r4 computed the first two)
- Inside a case the choice is alive at 3 players: guessing wins on a sure-real sign with only a same-row tool near;
  checking wins when the sign may be a trick or cures are short. Waiting for stage 2 is never chosen with a cure in hand.
- At 6 players, "grab, read, cure" may become the routine (free hands make grabbing cheap). The first kill line below
  watches for it.
- Across the run: candles are now lives or gear, so a crew's plan should change with what it has left. Not yet checked by
  a critic.

## First builds and kill lines
- **Build A (~3–4 weeks, critic r3):** ground floor + garden, 3 creatures as sign rows, one shared creature body,
  thermometer, lantern, pan, the 3 cures, holding, knocking out, tricks, one 8-minute night. Human doctor + 2 bot
  patients (bots say their inner signs in a speech bubble). Online code wired in from the start.
- **Build B (+1–2 weeks):** a human patient + 2 bot doctors who ask "what do you feel?" through a pick wheel (it times
  out after 5 s, as a silent patient).
- Then 3 humans, then the 5-night run.
- **Kill lines (Claude):**
  - By the 3rd night, the crew does the same thing in the first 10 s of every case: the choice is dead.
  - Fewer than a third of cures used an outer sign: the watchers' half isn't needed.
  - Build B: the human patient always self-checks, or never does: the patient isn't deciding.
  - In a 3-human night nobody asks "is that real or the house?".
  - Run: a crew that knows the signs ends 3 runs in a row with candles to spare, or a new crew loses before night 3.

## For the user (not built; Claude's recommendation in brackets)
- 5 nights with candles, or one long night. [5 nights.]
- Cure a turned creature too (a third ending; bends U10). [Keep U10.]

## What changed from critic r4 (synthesis)
| Critic r4 finding | Decision |
|---|---|
| A: r3's S1, M1, M2 fixed; leftover clock tells | Fixed the tells: GAP × 0.25–1.75; first case and tricks from 0:20; tricks follow the 60 s skip after a cure. |
| M1 the patient's "say it or wait" had one answer | Changed: dropped "say it or wait"; real inner signs grow near their trigger, so the patient decides whether to walk off and check or stay put to be cured. |
| M2 outer signs came too late | Fixed: the first sign is inner or outer at random; scars are the outer look-alike. |
| M3 candles changed no choice | Fixed: the dawn omen (one creature at half the cases) and spending spare candles on a bed or a tool. |
| M4 a volunteer made the chase a formality | Fixed: only a catch costs a candle; a starved creature wakes free at dawn; the turned friend chooses to hunt or hold back. |
| M5 last night and win unwritten | Fixed: no dawn after night 5; each player alive wins; the living pick who comes back when candles are short. |
| Minor: crew-size scaling, no run kill line | Fixed: ⌈n/2⌉+1 candles; a run kill line. |
| Minor: ghost silence fails on Discord | Fixed: ghosts can talk; their job is spotting who is sick. |
| Minor: wrong cure after 50 s; healthy cure vs failed roll; scene slips; 4 taught rules | Fixed: past 75 s they turn on the spot; a failed roll shudders, a healthy player just eats it; scenes computed by script; candles taught at dawn, so 3 rules. |
