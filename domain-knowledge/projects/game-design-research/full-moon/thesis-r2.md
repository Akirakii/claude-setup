# Full Moon: thesis r2 (Claude, 2026-11-11, after critic r1)

Working title "Full Moon" (Claude). Online co-op, 3–6 friends, one developer, ~3–4 months.
The user's idea and pillars U1–U10 are quoted in `thesis-r1.md` (unchanged). The synthesis table at the end says what
changed from r1 and why.

## One sentence
Through one full-moon night in a mansion, friends keep starting to turn into legendary creatures: put together what
the sick friend feels and what everyone else sees, give them the right cure in time, because a friend who fully turns
must catch one of you to become human again, or die.

- **Job:** keep the house stocked with cures (wolfsbane, garlic, salt grow or turn up around the mansion, garden and
  tree house) and keep checking on each other.
- **Choice:** give the cure now on a guess while it's strong, or gather one more sign and give it later, weaker; hold
  the sick friend (they keep talking) or knock them out (slower case, but they go silent).
- **Goal:** be alive at dawn.

## Terms
- **Case:** one friend's sickness, from its first sign until they are cured or fully turned.
- **Stage:** a case runs through 3 stages, then the friend turns. Each stage brings more signs; the cure gets weaker.
- **Inner sign:** something only the sick player gets, on their own screen or in their own ears (a heartbeat, a craving).
- **Outer sign:** something only the others see on the sick player's body (yellow eyes, fur, grey skin).
- **Tool sign:** an outer sign that shows only through a tool (a thermometer reading, a reflection), seen by whoever holds the tool.
- **Cure item:** one per creature: wolfsbane (werewolf), garlic (vampire), salt (zombie). It cures when given, and held up
  it keeps that creature back. It does not test for anything.

## What a new player is taught (3 rules)
1. Friends will start turning into monsters. You can't see your own body's signs, and only you feel your inner ones,
   so tell each other.
2. Give a sick friend the right cure item to save them. The journal says which signs point to which creature. Sooner is stronger.
3. A friend who fully turns must catch someone or die. Hold up its cure item to keep it back.

Everything else is an object that explains itself (a pan, a thermometer, a mirror, grabbing a friend), something you
discover (knocking out slows a case; scars), or a number players never need to know. Ghost rules are taught only to
the dead, when they die.

## The hub
The sick friend's transformation (a hidden meter: stage 1 → 2 → 3 → turned). Every system acts on it and nothing else.
| System | Acts on the hub by |
|---|---|
| Signs (inner, outer, tool) | showing it, split between the patient, the watchers and the tool holder |
| Cure items | ending it, with the stage's odds; held up, keeping a turned creature back |
| Holding / knocking out | slowing it |
| Creature chase | finishing it: catch someone or die |
| Ghosts (not in the first build) | bringing a cure item to it |
| Night clock | setting when new cases start |

## Rules (named starting values, to tune toward the stated targets)
**Night.** NIGHT = 12 min. Everyone alive at dawn wins (revived ghosts count). No early dawn for a lone survivor (r1's
instant dawn rewarded letting your last friend die). A lone survivor who turns has nobody to catch and dies, so being
last alive is dangerous: you want your friends alive.

**Cases.** The first case starts at 1:00. Each next case starts GAP = 360 s ÷ (living players) after the last case ended
(3 alive → 120 s, 4 → 90 s, 6 → 60 s). Rarely (DOUBLE = 15% of cases) a second case starts 10–30 s into a running one
(U8: "2 at once, but rare"). Never more than 2 at once. Random living player; not one cured in the last 60 s.
Target: a crew that plays well loses about 1 player in 4 per night.

**Stages.** TURN = 75 s: stage 1 (0–25 s), stage 2 (25–50 s), stage 3 (50–75 s), then turned. Target: a good crew
cures about half its cases in stage 2. Cure odds by stage: 90% / 60% / 30% (U6's %, Claude's fall by stage).

**Signs (U4).** Each case draws its signs from its creature's % row. Stage 1: 1 inner sign. Stage 2: +1–2 outer signs.
Stage 3: everything drawn, obvious. Signs overlap between creatures, so a single sign is only a lean.
| Sign | Kind | Werewolf | Vampire | Zombie |
|---|---|---|---|---|
| Heartbeat you hear: racing / slow / none | inner | 70% racing | 60% slow | 60% none |
| Craving: your view drifts to raw meat / to friends' necks / to anyone | inner | 50% meat | 60% necks | 50% anyone |
| Light hurts: your screen blooms near lamps | inner | 0% | 60% | 20% |
| Yellow eyes | outer | 60% | 30% | 20% |
| Grey skin | outer | 10% | 60% | 70% |
| Fur on the face and neck | outer | 70% | 0% | 0% |
| Shuffling walk | outer | 0% | 10% | 60% |
| Temperature (thermometer): fever / cold | tool | 70% fever | 70% cold | 60% cold |
| Reflection (mirror): eyes glow / faint / normal | tool | 50% glow | 70% faint | 0% (normal) |
The journal (an in-game book) prints this table. No tool ever says the creature's name.

**Scars (Claude, carried state).** A cured friend keeps one outer sign from their case for the rest of the night. Later,
that sign means nothing on them: a false lead the crew made, and it piles up as the night goes on.

**Cure (U6).** Give a sick friend a cure item: 2 s, one hand, they must hold still, be held, or be unconscious. The item
is used up. Right item: cured with the stage's odds. Wrong item or failed roll: nothing else; the case goes on, retry
with another item. A friend gives it; you can't cure yourself (Claude).

**Holding and knocking out (U7).** Grab a friend (both hands): their case runs at half speed while held; they can
struggle free in 3 s. Hit them with a pan or candlestick: knocked out KO = 20 s, case at a third of the speed. An
unconscious friend can't talk or hear (as in PEAK), so their inner signs go silent: knocking out buys time and costs
information. After waking, a friend can't be knocked out again for 20 s. The pan does nothing to a creature.

**One creature at a time (U8).** A second case that reaches the end of stage 3 while a creature is out waits there
(still curable at 30%) until the creature catches someone or dies; then it turns.

**Turned (U9, U10).** First build: one shared creature body (the player's own body with its creature's look: fur,
grey skin, fangs), 20% faster than people, no powers. HUNGER = 45 s to catch someone. A catch = holding a player for 2
s; a friend breaks it by pushing that creature's cure item into its face. Caught = that player dies and the creature
turns human. Out of time = the creature player dies. Held up, a cure item keeps its creature out of a 90° cone, 2 m
deep, in front of the holder; it can come around. Target: about half of creatures catch someone.
Later: one power per creature (werewolf tracks footprints, vampire flies to the tree house, zombie... TBD).

**Supply.** STOCK = living players + 1 cure items lie around the house at any time (held items don't count). When one
is used, a new one turns up within 30 s at a random spot away from the crew, of the type the crew holds least
(Claude: so deaths come from slowness or misreading, not from which item spawned).

**Hands (Claude).** Two hands: each holds one thing (a tool, a cure item, a pan). Holding a friend takes both. Nobody
can carry the whole pharmacy.

**Ghosts (full game, not the first build).** A caught or starved player becomes a ghost. Ghosts can't be heard by the
living. A ghost can push one small object slowly. A ghost who pushes the right cure item into a sick friend, when that
cure works, comes back alive (fixes R.E.P.O.'s "2–3 dead players watching", research.md). The push is also the only
way a ghost can point at an answer, so ghosts help without talking.

## Scenes
**3 players (Ana, Bo, Cy), night 1, minute 3.** Bo hears a slow heartbeat (inner, stage 1) and says so. Slow = 60%
vampire; it's only a lean. Ana has garlic and a mirror; Cy is fetching in the garden. Choice: give garlic now (90% if
it's a vampire, so about 55% overall), or wait for outer signs. Ana grabs Bo to hold and look: grey skin appears at
stage 2 (vampire or zombie). Ana's hands are full holding Bo, so she can't use the mirror. She lets go, holds the mirror
up to Bo: faint reflection. Vampire. Garlic at stage 2: 60%. It fails. Cy runs back with salt, which is useless here.
Bo turns at stage 3's end. Ana holds the last garlic up. Bo, a vampire, goes around her and catches Cy. Cy dies.
Two left, and every case from here needs both of them.

**6 players, minute 6.** A double case: Dee (craving necks: vampire or zombie lean) and Eli (Fae sees fur on his neck; Eli
can't see it himself). The crew splits into two clinics. Gus knocks Eli out
to buy time, but now Eli can't report his inner signs; with fur showing (only werewolves grow fur) it doesn't matter, and
wolfsbane cures him in stage 2. Dee is held and talks: "my heart's... not beating?" A zombie or a vampire's lean. Hal's
thermometer: cold (no help). Dee's earlier scar (grey skin from a case at minute 2) means nothing. Hal guesses salt: zombie, cured.

## Dominant-strategy check (Claude, in words)
- **r1's "kitchen clinic"** (swipe all items, feed the one that flinches): gone. Items don't test anything.
- **Knock out every sick friend, chain it:** the 20 s wake rule breaks the chain, and a silent patient loses the inner
  signs, which is the only stage 1 information.
- **Wait for stage 3, when it's obvious:** 30% cure.
- **Everyone holds a cure item as a shield:** STOCK = living + 1 across 3 types, so most players hold the wrong one;
  and the cone covers only your front.
- **Huddle in one room:** cures turn up away from the crew, so someone has to go out; the one who goes out may get sick
  where nobody can see their outer signs.
- **Cure on any sign at once:** scars make old signs lie, and a wrong item is wasted.

## What changed from r1 (synthesis table)
| Critic r1 finding | Decision |
|---|---|
| S1 the patient only waits, everyone sees the same | Fixed: signs split into inner (patient only), outer (others), tool (holder). Diagnosing needs the patient and a watcher to talk. |
| S2 item test gave the answer | Fixed: items don't test; tools show signs only; the journal % is the only route to a name (U5 kept: tools still needed). |
| S3 18 rules | Fixed: 3 taught rules; the rest is self-explaining objects, discovery, hidden numbers; ghost rules taught at death; gorgon cut. |
| M1 overlap at 6 bends U8, deaths set by spawns | Fixed: next case starts after the last ends, 15% doubles, cap 2; supply follows use, short type spawns. |
| M2 knockout beats holding | Fixed: knocked out = silent (no inner signs), and 20 s before another knockout. |
| M3 the chase only picks who dies | Kept U10 as the user wrote it: the chase is a private stake (each survivor wins alone), like the user's "survivors of the night win". Shields are scarce and cover your front only. Removed r1's false "leaves the crew bare". The other option, curing a turned creature, bends U10: put to the user, not built. |
| M4 instant dawn rewards betrayal | Fixed: removed (it was Claude's). A lone survivor who turns dies, so you need your friends. |
| M5 the dead sit out | Fixed in the full game: a ghost who pushes in a working cure comes back. Not in the first build (nights are short). |
| M6 one night = Mario Party feel | Partly kept U2 (one night). Reasoning: the minigame feel was one rule in a 1–2 min round; this is a 12 min match with ~4–6 cases, deaths and scars carried inside it (an Among Us or Deceit-length match). Between nights, new creatures join the pool as crews survive (Phasmophobia's ghost list growing). A 3-night moon would bend U2: put to the user. |
| M7 test crew can't play the core | Fixed: first build = human doctor + 2 bot patients (bots speak their inner signs in a text bubble). The voice sign is cut. |
| M8 scope; 2 creatures = coin flip | Fixed: first build = 3 creatures as sign rows + one cure item each, one shared creature body, no powers, no ghosts, ground floor + garden. |
| m1 carry cap, unspecified rules | Fixed: two hands; held-up cone 90° × 2 m; spawns unannounced, away from the crew; the pan does nothing to creatures; retries allowed (each costs an item). |

## For the user (not built; recommendation in brackets)
- Cure a turned creature too (a third ending, bends U10). [Keep U10: the chase as "save yourself" is the user's
  "survivors win", and panic among friends is the funny part.]
- Three nights to the full moon (bends U2). [Keep one night; grow the creature list between nights instead.]

## First build (smallest the user can try)
Ground floor (kitchen, hall, study, ~5 rooms) + garden. 3 creatures as sign rows. Thermometer, mirror, pan. Three cure
items. Holding, knocking out, the shared creature chase. Human doctor + 2 bot patients, then 3 humans.
Kill line (Claude): if 3 humans finish a night without asking each other "what do you feel?" more than twice, the split
signs aren't doing their job.
