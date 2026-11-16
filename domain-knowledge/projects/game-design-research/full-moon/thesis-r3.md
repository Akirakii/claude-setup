# Full Moon: thesis r3 (Claude, 2026-11-11, after critics r1 and r2)

Working title "Full Moon" (Claude). Online co-op, 3–6 friends, one developer, ~3–4 months.
The user's own words and pillars U1–U10 are in `thesis-r1.md` (unchanged). The table at the end says what changed
from r2 and why. Everything tagged (Claude) is Claude's call; untagged rules come from the user's words.

## One sentence
Through one full-moon night in a mansion, friends keep starting to turn into legendary creatures: put together what
the sick friend feels and what the others see, give them the right cure in time, because a friend who fully turns
must catch one of you to become human again, or die.

- **Job:** tend the cures (wolfsbane in the garden, garlic in the kitchen and greenhouse, salt in the cellar and the
  tree house regrow after picking), keep a tool in hand, and keep checking on each other.
- **Choice:** cure now on one sign (a coin flip, and a wrong cure makes it worse), or get a second sign first while the
  cure weakens; and for the patient: say what you feel (and maybe get panned for a trick of the house) or wait to be sure.
- **Goal:** be alive at dawn.

## Terms
- **Case:** one friend's sickness, from its first sign until they are cured or fully turned.
- **Stage:** a case runs through 3 stages, then the friend turns. Each stage brings more signs; the cure weakens.
- **Inner sign:** only the sick player gets it, on their own screen or in their own ears.
- **Outer sign:** only the others see it, on the sick player's body. You can't see your own.
- **Tool sign:** shows only through a tool (thermometer, lantern), to whoever holds it.
- **Look-alike:** a sign on a healthy player that comes from the house, not a curse (Claude).
- **Cure:** one per creature: wolfsbane (werewolf), garlic (vampire), salt (zombie). Given, it cures; held up, it
  shoves its creature back. It never tests anything.

## What a new player is taught (3 rules)
1. Friends will start turning into monsters. You can't see your own outer signs, and only you feel your inner ones:
   tell each other.
2. Every sign rules out one creature (the journal shows which). Give the right cure: sooner is stronger, and a wrong
   one makes it worse.
3. A friend who fully turns must catch someone or die. Hold up its cure to shove it back.

Things players find out by playing, each shown in the world: a pan knocks a friend out; grabbing holds them; while a
patient is held or out cold, their signs visibly stop spreading; a cured friend keeps a scar; the house plays tricks;
the garden makes everyone read cold; cures regrow where they were picked. Taught only when it happens: the lone
survivor's self-cure, and ghost rules (to the dead).

## The hub
The sick friend's transformation (stage 1 → 2 → 3 → turned), shown on their body as the signs spread. Every system
acts on it.
| System | Acts on the hub by |
|---|---|
| Signs (inner, outer, tool) and look-alikes | showing it, split between the patient, the watchers and the tool holder |
| Cures | ending it (stage odds), pushing it forward (wrong cure), shoving a turned creature back |
| Holding / knocking out | slowing it |
| Creature chase | finishing it: catch someone or die |
| Ghosts | pushing cures and tools toward it |
| Night clock | setting how often cases start, how often they double, how often the house tricks |

## The signs (U4)
Each sign rules out one creature, so one sign leaves two creatures and two signs from different rows leave one.
The % (U4's "common pattern and %") says how often each of the two shows that sign.
| Rules out | Inner (patient only) | Outer (others see) | Tool (holder sees) |
|---|---|---|---|
| **zombie** (so werewolf or vampire) | you hear your friends' heartbeats · W 50% V 70% | fangs when they talk · W 40% V 70% | lantern: their eyes shine back · W 70% V 40% |
| **werewolf** (so vampire or zombie) | lamps hurt: your screen blooms near light · V 70% Z 40% | grey skin · V 50% Z 70% | thermometer: cold · V 60% Z 60% |
| **vampire** (so werewolf or zombie) | you crave raw meat: your view drifts to it · W 70% Z 50% | drooling · W 40% Z 70% | (none) |

- Each creature has 2 inner signs; a case's stage 1 always shows exactly one of them, picked by its %. So the
  first sign is always a lean between two creatures (55–64% for the likelier one), never a name.
- Tool signs can be read from the start of a case (each shows with its %). Outer signs appear at stage 2 and
  spread over stage 3 (grey creeps up from the neck), so the body shows how late it is. Stage 3 shows all of the
  creature's signs, full size.
- No tool, sign or journal line ever names the creature.

**Look-alikes (Claude): every kind of sign has one, so a single sign can lie.**
- Inner: the house plays tricks. A healthy player sometimes hears heartbeats, flinches at a lamp or smells meat
  for ~8 s (FAKE: about once every 3 min per player, rising toward dawn). A real inner sign stays and others follow;
  a trick fades.
- Tool: anyone who was in the garden in the last 30 s reads cold.
- Outer: scars. A cured friend keeps one outer sign from their case for the rest of the night.

## Rules (named starting values; tune toward the targets)
**Night.** NIGHT = 12 min (first build: 8 min). Everyone alive at dawn wins (revived ghosts count). The pressure rises
all night: cases come faster, doubles and tricks get more common. No early dawn. A lone survivor can give themselves a
cure (taught when it happens), so being last alive is a fight, not a wait.

**Cases (U3, U8).** The first case starts at 1:00. The next starts GAP = 180 s ÷ (living players) after the last
case ended (3 alive → 60 s, 6 → 30 s), shrinking to 60% of that by dawn. Rarely, a second case starts 10–30 s after a
case starts (DOUBLE: 10% of cases early in the night, 30% in the last third). Never more than 2 at once. The player is
random, skipping anyone cured or just turned back in the last 60 s.

**Stages.** TURN = 75 s: stage 1 (0–25 s), stage 2 (25–50 s), stage 3 (50–75 s), then turned. Cure odds: 90% / 60%
/ 30% (U6's %, falling by stage: Claude).

**Cure (U6).** Give a cure: 2 s, one hand; the patient must hold still, be held, or be out cold. It's used up.
- Right cure: cured with the stage's odds; a failed roll changes nothing else.
- Wrong cure (Claude): the case jumps to the start of the next stage and its new signs burst out at once. A guess has
  a price, and everyone sees whose cure it was.
- On a healthy player: wasted.
A friend gives it (Claude); you can't cure yourself, except as the last one alive.

**Holding and knocking out (U7).** Grab a friend (both hands): their case runs at half speed and its signs visibly
stop spreading; they can struggle free in 3 s. Hit them with a pan or candlestick: out cold for KO = 20 s, the case at
a third of the speed. Someone out cold can't talk or hear (as in PEAK), so their inner signs, including stage 2's
second inner sign, go silent. After waking, nobody can knock them out again for 20 s. The pan does nothing to creatures.

**Turning (U8, U9, U10).** At the end of stage 3 the friend turns, which takes 2 s; whoever held them is thrown off,
and nobody can be caught during it. A second case that reaches the end of stage 3 while a creature is out waits there
(still curable at 30%) until that creature catches someone or dies, then turns. First build: the creature is the
player's own body in its creature's look, 20% faster than people, no powers. HUNGER = 45 s to catch someone. A catch =
holding a player for 2 s; a friend breaks it by shoving the creature with its cure. Caught = that player dies and the
creature turns human. Out of time = the creature player dies.

**Shoving (Claude).** Holding up a creature's own cure shoves it 3 m back when it comes within 2 m in front of you;
then that cure can't shove for 3 s. One armed player can't hold a creature off forever; two cover each other's gap.
Full game: one power per creature (werewolf tracks footprints, vampire flies to the tree house, zombie TBD).

**Cures in the house (Claude).** Six spots: wolfsbane ×2 (garden beds), garlic ×2 (kitchen, greenhouse), salt ×2
(cellar, tree house). A picked cure regrows at its spot after REGROW = 120 s. So at most 2 of a kind exist, and the
crew has to walk the house to keep them. Two hands each (a cure, a tool, a pan); holding a friend takes both.

**Ghosts.** A dead player becomes a ghost the living can't hear. First build: a ghost can push small objects (bring a
cure or a tool closer). Full game: a ghost who pushes the right cure into a sick friend, when it works, comes back
alive (R.E.P.O.'s "2–3 dead players watching", research.md).

## The choice in numbers (Claude, from the table; equal chance of each creature)
- Stage 1, one inner sign: the likelier creature is right 55–64% of the time.
- **Guess now:** right ~60% × 90% = 54% cured. Wrong ~40%: the case jumps to stage 2, new signs burst out and now
  name it, cure at 60%: +24%. Total ~78%, using up to 2 cures, with a visible "you made it worse".
- **Check a tool first** (~5–10 s if one is in hand and it's from the other row): the tool sign shows ~60% of the time;
  then the creature is known and the cure is 90% → about 0.6 × 90% + 0.4 × (guess) ≈ 85%. With the wrong tool in hand
  (same row as the inner sign) it tells you nothing.
- **Wait for stage 2:** 2+ signs, known (unless a scar or the garden lies), 60% per cure, ~84% with two right cures.
- So the best move depends on which inner sign showed, which tool is in your hand, which cures are ripe, and whether the
  sign is a trick. That changes every case.

## Scenes
**3 players (Ana, Bo, Cy), minute 3.** Bo: "I hear heartbeats. Yours." That's a werewolf or a vampire, or the house.
Ana has the thermometer and garlic; Cy is in the garden picking wolfsbane. Ana reads Bo: normal, not cold, which proves
nothing (cold shows only 60% on vampires). Bo's heartbeats don't fade, so it's real. Ana guesses vampire and gives the
garlic: it's wrong. Bo jumps to stage 2: fangs and drool burst out. Drool rules out vampire, and heartbeats
already ruled out zombie: werewolf. Cy is running back with wolfsbane, and it's 60% now. Ana grabs Bo; his fangs stop growing. The cure works.
Bo keeps the drool as a scar. Ten minutes later Bo drools at everyone and nobody trusts him.

**6 players, minute 9 (late, pressure up).** A double: Dee hears heartbeats; Eli says lamps hurt. Fae says she smells
meat too: a trick (it fades). Gus knocks Eli out to slow him, so now nobody hears what Eli feels; Hal has the lantern
but Eli's eyes are closed. Dee's thermometer reads cold, but she just came in from the garden. The crew splits: two on
Dee, two on Eli, one runs to the cellar for salt, one stands at the door with garlic in case. Eli turns first: a zombie
(grey skin bursts out). Two players hold garlic, which is useless. The zombie catches Fae.

## Dominant-strategy check (Claude, in words)
- r2's "walking pharmacy" (carry all cures, feed on the first sign): at most 2 of a kind, two hands each, and a wrong
  cure pushes the case a stage. Feeding on a trick wastes a cure.
- Pan anyone with a sign: tricks make you pan healthy friends, who are out for 20 s; a patient out cold loses their
  second inner sign.
- Huddle in the clinic: cures regrow in the garden, cellar and tree house; tools from the right row must be fetched.
- Wait for stage 3: 30%.
- Ignore the journal: one sign is a coin flip, and players will learn the 8 signs over a few nights, like Phasmophobia's
  evidence; the tricks, the garden's cold and scars keep "is this sign real?" open after the table is learned.
- Remaining risk: a crew that knows the table, keeps one tool from each row in hand, and confirms before curing. That's
  the intended good play; whether it gets too easy at night 5 is a playtest question (kill line below).

## What changed from r2 (synthesis table)
| Critic r2 finding | Decision |
|---|---|
| S1 sign values were name tags | Fixed: every sign rules out exactly one creature (rows of two); one sign = 55–64%, two from different rows = known. |
| S2 a feed was a free test; carry every cure | Fixed: a wrong cure jumps the case a stage and bursts its signs out (visible culprit); cures are 6 spots that regrow in 120 s, at most 2 per kind, held ones included. |
| M1 calm conveyor | Fixed: GAP halved (180 s ÷ living), shrinking to 60% by dawn; doubles counted from the first case's start, 10% → 30%; pressure rises all night (no easy after-midnight). |
| M2 the patient decides nothing | Fixed: look-alikes (the house's tricks) make "am I sick, and do I say it?" the patient's call; saying it can get you panned or waste a cure. They can also struggle out of a hold. |
| M3 the mirror showed the patient their own signs | Fixed: no mirror; a lantern (eyes shine back). No mirrors on the map. |
| M4 holding/knocking out invisible; silence free | Fixed: held or out cold, signs visibly stop spreading; stage 2 adds a second inner sign, which an out-cold patient can't report. |
| M5 first build tests only the doctor's lookup | Fixed: two first builds: a human doctor + 2 bot patients, and a human patient + 2 bot doctors who ask through a "what do you feel?" pick wheel. New kill lines below. |
| m1 unwritten rules | Fixed: % = how often that creature shows that sign; healthy players get heartbeats only as a trick; stage 1 always shows one inner sign; one journal per player; turning throws a holder off, 2 s safe; just-turned-back players skip cases for 60 s; the shuffling walk is cut. |
| m2 the cone made an armed player uncatchable | Fixed: the cure shoves, then waits 3 s; two armed players cover each other. |
| m3 quiet, long failure in the first build | Fixed: 8 min test nights; ghosts push objects in the first build; the lone survivor can self-cure. |

## For the user (not built; Claude's recommendation in brackets)
- Cure a turned creature too (a third ending, bends U10). [Keep U10.]
- Three nights to the full moon (bends U2). [Keep one night; add creatures between nights later. A 4th creature needs
  the journal's rows redrawn: each sign would then leave two or three creatures.]

## First builds and kill lines
- **Build A:** ground floor + garden, 3 creatures as sign rows, one shared creature body, thermometer, lantern, pan,
  the 3 cures, holding, knocking out, look-alikes, 8 min night. Human doctor + 2 bot patients (bots say their inner
  signs in a speech bubble).
- **Build B:** the same with a human patient + 2 bot doctors who ask "what do you feel?" through a pick wheel.
- Then 3 humans.
- **Kill lines (Claude):** fewer than half of the cures needed both an inner sign and an outer or tool sign; or a crew
  on its 3rd night loses nobody; or in a 3-human night nobody asks "is that real or the house?".
