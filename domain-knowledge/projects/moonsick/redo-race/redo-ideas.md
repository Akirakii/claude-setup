# Moonsick redo: the design (2026-11-15, chat with the user)

Tags: (user) = the user's words chose it; (Claude) = Claude's pick, not yet OK'd. Built = on main, untested unless said.

## The game in one line (user OK'd the logic, Claude's words)
**Grow into the werewolf first while everyone tries to shave you back to human.**
The feeling: a frantic, bloody scramble where you're always both the hunter and the hunted.
Every rule below should push toward that; anything that doesn't is a candidate to cut.

## The one turning point: the potion is finished (user 2026-11-15)
Until then everyone races to turn. Once the anti-werewolf potion exists, turning is suicide, so the race flips: the
furriest now begs to be shaved, and whoever still wants to win alone must steal or spill the potion first. It's
meant to be rare (user: "the weapon finished should be the rare case"), so most rounds stay a pure race.

## Stage 1: the race (built)
- Fur is your progress toward turning (user). It covers the whole body and grows longer and denser (user); every
  tuft is its own: the razor cuts the tufts along its line and leaves a hole the shape of its trace (user).
  No number on screen; you read fur on bodies and your own hands (Claude).
- Fur grows from 0 to 100% in 2 minutes (Claude, after the user's 1 minute: with the moon deadline, 1 minute let an
  unshaved player turn in ~45 s). Everyone starts at 0–30% (Claude).
- Everyone carries a razor in the right hand, infinite battery, reach 2.28 m (user); hold RMB. You can't shave
  yourself (Claude).
- The left hand holds one picked-up item, used with LMB (user: one item hand). Weapons, all brutal slapstick with
  lots of blood (user), no cooldowns (user):
  - frying pan (kitchen): knocks down, throws the target (user: junky physics and pushing); breaks when it hits
    someone (user; a miss keeps it), a new one turns up in the kitchen 20 s later (Claude);
  - croquet mallet (conservatory): half-second wind-up, limp at half speed for 8 s, a shove;
    breaks when it hits (user), a new one in the conservatory 20 s later (Claude);
  - potion bomb (potion lab): 6 m blast (user: 2x), knocks down and throws everyone in it;
  - bear trap (attic): holds whoever steps in for 4 s, the one who set it too.
  A knockdown: helpless 2 s, then 2 s of protection (Claude), and you drop your item (user OK). Weapons appear at random spots in their own room
  (Claude); bombs and traps come back later.
- The moon rises through the night and stands straight overhead at 4:00; then the furriest player turns (user).

## Stage 2: the hunt (built)
- The first player to reach 100% (or the furriest at 4:00) turns into the werewolf; it can't be undone (user).
- Everyone else's fur falls off (user OK); the moon stops and everything goes red (user).
- The werewolf has 3 minutes to eat everyone (user). Two attacks (user 2026-11-15): a hit knocks a moving player
  down (thrown, helpless 2 s, then 2 s of protection); it eats only a player who can't move: knocked down, trapped,
  or standing still for 0.5 s (Claude's threshold). Eating is instant (user 2026-11-15: the 5 s
  eating scene is cut). Growing stays passive for now (user: will think about making it active). If time runs out, the humans win (user). Humans' weapons still knock it down.

## Dead players (user 2026-11-15)
- Dead players are just spectators: they watch the living (click to switch who you follow) until the round ends.
  Built.

## Points and a shop (user 2026-11-15; not built)
- Each round's winners get 50 points each (user): the werewolf if it eats everyone; every surviving human if the
  hunt runs out or the potion cures the werewolf. Points add up across rounds, to spend in a future shop (user).
- Open (Claude): the shop's contents. Claude's caution: cosmetics only (hats, fur colours, razor skins), so points
  never make a player stronger in a free-for-all.

## The anti-werewolf potion (designed, not built; Claude's picks unless tagged)
- Ingredients, each useful alone if the potion is never finished:
  | Ingredient | How you get it | Alone |
  |---|---|---|
  | Wolfsbane | pick in the conservatory; one at a time, regrows in 45 s | raised, shoves the werewolf back once |
  | Fur, 3 clumps | a clump drops at someone's feet each time they lose ~a quarter of a body's fur; anyone can grab it | thrown, lures the werewolf for 3 s |
  | Moon water | a bucket in the attic's moonbeam fills in 2 minutes; anyone can carry it off | splashed, slows the werewolf 10 s |
- The potion is reachable when nobody interferes (~3:00 with perfect teamwork); it's rare because of sabotage,
  not the clock (user yes, 2026-11-15).
- Fur clumps stack in your item hand, up to 3 (user asked stacks vs %; Claude: stacks). Dropped fur lands as one
  bundle showing 1–3 balls; picking up fur adds to your stack, the rest stays on the floor; picking up anything else
  swaps the whole stack out.
- Brewing: all three in the potion lab's cauldron, then two players stir together for 10 s; if either lets go, it
  starts over. Perfect teamwork finishes it around 3:30, so it's rare; moon water is the clock (raise its fill time
  before asking for more fur).
- The potion, thrown at the werewolf, cures it and the humans win. Thrown at a human before the turn: (open).
- A knockdown drops what you hold, so the potion and fur can be stolen (user OK 2026-11-15; built).
- The humans who survive win together; the werewolf wins alone (user OK 2026-11-15; built as "The humans win").

## Controls (built)
WASD, Shift sprint, Ctrl crouch / slide, Space jump, RMB hold to shave, LMB use item, E pick up (swaps), Q drop,
V third person, M menu. Start menu: Play (you + 3 bots) or the razor test area (a still bot at 99% fur, T refills,
every item nearby).

---

# Earlier ideas (kept for later; some superseded by the design above)

## Direction
- Redo the game from scratch: a new map, and items become stations (user).
- Aesthetic: an enchanted mansion, cartoonish, witch (user).
- Everyone wants to turn into the werewolf and wants to stop others turning first (user). The game becomes a
  free-for-all instead of co-op; curing someone is how you stop them turning first.
- Scoring (Claude): each kill as the werewolf scores 1; eaten players come back when the chase ends; most kills at
  dawn wins.

## Two stages (user)
1. **Curing.**
2. **Running away:** starts when a player turns into the werewolf. Every station is blocked and everyone's sickness
   pauses, until the werewolf dies or kills a player (then it turns back into a human).

## Map (user)
- 6 rooms on 2 floors, 1 station in each, joined by open spaces or corridors so players can run from the werewolf.
- Each room holds the items for its station, so a station can have several outputs; each station has 1 output that
  cures 1 symptom, so 6 cures for 6 symptoms.

## Stations
| Symptom | Station | Whose |
|---|---|---|
| Fur | barbershop: shaving foam, razor, chair | user |
| Nausea | kitchen: soup | user |
| Sleepiness | tea parlour: enchanted kettle, wake-up tea | Claude's pick |
| Walking on four legs | ballroom: gramophone, dance shoes | Claude's pick |
| Awoo | music room: piano, songbook, singing frog | Claude's pick |
| Wet-dog stink | bathroom: clawfoot tub, bubble potion, scrub brush | Claude's pick |

Ideas cut (Claude): glowing eyes (alchemy lab eye drops) and drooling (attic dentist's chair).
A station must work on an unwilling patient, since the patient wants to turn (Claude, from the new direction).

## Forcing a cure on someone (user)
- **Throw** the cure at them (user). Claude: it flies in an arc and cures on a hit; a miss wastes it.
- **Up close**, like dressing someone (user). Claude: hold for 1.5 s within arm's reach.
- **Knock them down** first to make the other two easier (user). Claude: helpless for 2 s, then 6 s before you can
  knock again.

How the target gets away (user kept both, 2026-11-15):
- **Fight the hold** while someone cures you up close.
- **Bonk them first**, before they bonk you.
- Dodging a throw and stepping out of reach (Claude).

## Stations for the new direction (Claude's picks, recorded for later, 2026-11-15)
Every symptom shows only in short bursts; the sick player feels each burst a second early and can hide (Claude).
| Symptom | Burst others catch | Station | Cure | Thrown | Up close |
|---|---|---|---|---|---|
| Fur (user) | fur sprouts on the face | barbershop | shaving foam | hits the face like a pie | lather and shave |
| Nausea (user) | a loud retch | kitchen | soup | splashes into the mouth | spoon-feed |
| Sleepiness | a big yawn | tea parlour, enchanted kettle | fizzing wake-up tea | the cup splashes them awake | make them drink |
| Walking on four legs | drops to all fours | dressing room, magic wardrobe | a stiff starched coat | flies and wraps them upright | dress them |
| Awoo | a small "awoo" | greenhouse, enchanted beehive | a jar of honey | splats on the mouth | a spoonful |
| Wet-dog stink | a puff of stink and flies | bathroom | a bubble-bath bomb | bursts into suds | scrub them |

## The first MVP notes (superseded where the design above differs)
- Fur is your % progress toward turning into the werewolf (user).
- Everyone stops the others turning first by curing their fur, which lowers the % (user), and by knocking them down
  with brutal physical aggression: explosives, breaking knees, lots of blood (user).
- When one player turns, everyone else's progress pauses and they run for 1 minute (user).
- If the werewolf catches one, it survives and turns back into a human; if not, it dies (user).
- Razors have a battery instead of breaking (user, 2026-11-15). Claude: a full battery buzzes for 3 s (two full
  shaves, and a cut-off shave still drains it); it recharges only on the barbershop's charging dock, full in 10 s.
- Weapons (Claude, user discussing): frying pan (kitchen), potion bomb (potion lab), croquet mallet to the knees
  (conservatory), bear trap (cellar); 2 s of protection after getting up. Each weapon appears at a random spot inside
  its own room (Claude, after the user asked "should be random?").
- MVP without limbs (Claude): the werewolf kills with one touch; the mallet makes the target limp at half speed for
  8 s and the bomb knocks down everyone within 3 m for 2 s, as before.
- Fur covers the entire body and face at once and grows longer and thicker with the % (user, 2026-11-15: "entire
  body", not in stages). No number on screen (Claude); you see your own fur on your hands in first person (Claude).
- Shaving needs aiming at the fur parts (user, 2026-11-15). Claude: the body has 6 parts (head, torso, 2 arms,
  2 legs); you aim the razor at a part and hold to shave it bare, a patch at a time like a lawnmower, and the %
  drops by what you shaved. A moving or struggling target is hard to aim at, so knocking them down helps. Later, with
  limbs: a limb that comes off keeps its fur on the floor; the fur % is in the body, so a bandaged or reattached
  limb grows fur back to match it (so blowing off a furry leg doesn't cure anyone).


Later changes, now folded into the design above:
- The first turn starts a second stage that can't be undone (user, 2026-11-15): the werewolf must eat everyone else
  within 3 minutes to win; if time runs out, the humans win. Each eat is the 5 s scene everyone watches.
- Fur grows to 100% in 1 minute (user, 2026-11-15).
- At the turn, everyone else's fur falls off (user OK, 2026-11-15): only the werewolf is furry during the hunt.
- The moon (user, 2026-11-15): it rises through the night and stands straight overhead (90°) at 4:00; then whoever
  has the most fur turns. At the turn the moon stops and goes red for the second stage. Fur growth back to 2 min
  (Claude, so an unshaved player doesn't turn in 45 s).
- The silver weapon (Claude, not built): perfect teamwork finishes it at ~3:40, so it's the rare case (user: "the
  weapon finished should be the rare case"); each part helps alone (raw silver thrown stuns 3 s, silver dust slows
  10 s, the finished weapon kills in one hit).

## Later, not the MVP (user, 2026-11-15: "record the limbs mechanic for future")

### Limbs (user, 2026-11-15)
- The werewolf has 2 attacks: one breaks a player's limbs and cuts their movement; the other eats them, only when
  their movement is very low (under a threshold) (user).
- Healing a limb, 2 ways (user): a lost limb drops on the floor and anyone can pick it up and attach it, to
  themselves or to someone else (their own limb or anyone's); or a bandage regrows the missing limb without the
  dropped one.
- Claude's picks (not OK'd): 4 limbs. Legs set your top speed: both 100%, one 50% (hopping), none 20% (crawling on
  your arms). An arm lost = that hand can't hold anything. The werewolf can eat you below 25% (no legs). Attaching a
  limb takes 1.5 s; a bandage regrows one in 8 s while you hold still with both hands busy. The claw takes the limb
  nearest where it lands, so aiming low takes legs. The humans' weapons use the same limbs: the bomb blows off a
  random limb, the mallet takes a leg.

## The potion as built (2026-11-15)
- Ingredients: wolfsbane (conservatory, regrows 45 s after it's used up), a rat (3 roam the ground floor; E grabs
  one; it wriggles free after 20 s; a bomb kills them, back in 30 s), moon water (a bucket in the attic's moonbeam,
  2 minutes). Rats replace the fur clumps (user).
- LMB at the potion lab's cauldron puts in what you hold; with all three in, two players hold F for 10 s (fewer
  than two, it starts over). The flask pops out for anyone; thrown, it splashes 2.5 m and cures the werewolf: the
  humans win. A miss shatters it; the cauldron brews again, during the hunt too (user).
- Each alone: wolfsbane shoves the werewolf back, a thrown rat keeps it busy 3 s, a full bucket slows it 10 s.
- No direct sabotage (user): the cauldron can't be spilled. You slow the potion only by knocking players down
  (they drop what they carry; the bucket keeps its water), stealing ingredients, or killing rats.

## Lobby and points (built 2026-11-15)
- Play goes to a lobby first, and back there after each round (user: players wait in a lobby where the rules are
  taught). Taught by doing plus six numbered signs in plain words (Claude): a shaving dummy that grows back, every
  item to try, and a glowing door you walk through to start.
- Points: +50 to each winner, saved across sessions (user); shown in the menu. No shop yet (user: points code only).
- The moon-water bucket is heavy: whoever carries it can only walk (user 2026-11-15: carrying it off at a sprint was
  unfair). No rat climbing out of the cauldron for now (user).
- Bot sabotage (user asked; Claude's rules): a bot in the fur lead (within 8% of the top) knocks down whoever carries
  an ingredient or stirs, steals loose ingredients (a bucket once it's a third full) and drops them far from the
  cauldron.

## Changes approved 2026-11-15 (user: "proceed with all changes")
- Potion = wolfsbane + a rat + SILVER (replaces moon water; user picked the top werewolf myths). A silver candlestick
  melts in the attic furnace for 2 minutes and can't be taken until it's done; the ingot then waits at the furnace
  for anyone. Thrown at the werewolf, silver knocks it down.
- Stirring: a knockdown only pauses it; it resets after 5 s with fewer than two stirrers (critic r1).
- Rats run at 7 m/s (user: faster; was 6).
- The werewolf moves like a human (crouch, slide, jump, Shift to sprint), 1.44x faster (user); crouched it's still
  1.5 m tall, so the 1.4 m crawl gaps stay human-only.
- Humans 10% slower (user): walk 3.89, sprint 7.78 m/s; the werewolf keeps 11.2 m/s.
- Map rebuilt to the map critic's plan5 (docs/critic-layout-map-r1.md) with the attic furnace instead of a balcony
  moonbeam: kitchen NW, cauldron room N (roofed, 3 ground ways in), pantry NE (rats), conservatory SW (mallets,
  wolfsbane), great hall, witch's study SE (bombs), roofed south corridor ring, storeroom NW upstairs (traps), attic
  NE upstairs (furnace), second stair pantry-attic, crawl gaps for humans.
- Movement (user 2026-11-15): keep the existing movement (Shift sprint, crouch, slide while running, slide jump);
  from Deadlock only the werewolf's wall jump, 2 kicks per airtime (Claude). No dash, no stamina, no mantle (user).
- The croquet mallet is now a machete (user 2026-11-16): same rules (half-second wind-up, slashes the legs: half
  speed for 8 s, a shove, breaks on a hit, back in the conservatory 20 s later), more blood.
