# LAW: needs and sleep beds

Standing law for the needs (hunger, sleep), the energy they leave, and the sleep Bed. User
decisions are tagged (user); the rest are proposals in this spec, open to the user's veto.
Rooms: `docs/LAW_rooms.md`.
Which kind a state is and how it shows: `docs/LAW_creature_state.md`.

## Rules
1. **Needs (user: hunger, sleep and mood are the dynamic variables).** A friendly creature
   has two needs, hunger and sleep, each 0..1 and 1 when met, with no bars (user): its
   balloon is the sign (Signs). Fun, a third need, stops nothing when it runs out. Mood keeps its own law (set-point and
   moodlets); no need feeds it. Where it sleeps does, as a place and not a need (user: beds
   per room): the beds in the room of its bed set a lasting centre term (`room_mood`). Hunger drains on the clock in every ally state (awake,
   asleep, breeding, downed). Sleep drains
   only while it does something productive: a job, training, fighting, socializing,
   rescuing. Idle roaming, eating and being carried do not drain it.
2. **Any food fills hunger (user; the room rule is an AFK pick).** Every food a friendly
   accepts adds `MEAL_FILL` to hunger, favorite or not (a taming treat stays a downed
   wild's). A favorite also cheers (😋) and a cooked dish gives the meal moodlet; a
   favorite, a dish or healing food also heals a wounded one. It eats for hunger only with
   room for a whole meal, so a fuller one leaves the food for others. Allies drop no gems
   (user). At hunger 0 with no food about, after `STARVE_SEC` (40 dilated s; red the whole
   time, so the player can feed it first) it takes the nearest crop ready to harvest, never
   an unripe one, and harvests it as the player would: it eats one fruit and the rest drops
   on the ground (user).
3. **Energy is hidden (user; the lower-need rule is an AFK pick):** it is the lower need,
   `min(hunger, sleep)`, with no state of its own and no sign; the balloon is the sign. With
   either need at 0 a creature is tired (user: 0 is the stop, no margin above it): it skips jobs, training (gym, treadmill),
   socializing and rescuing. Urgent work overrides every need, asleep or not: a medic keeps its
   post, and one matched to a downed patient goes first, then a fight; a body already in its
   arms comes before both (user). Any other job it lets go, so a rested one takes the post
   (AFK pick: a tired cook held the only kitchen and the herd starved), and drops what it
   carries for the job. A sleeper stays off work until it gets up. It still roams, eats,
   follows, sits in comfort places and can be carried. A tired creature never snaps (hits add no rampage), so an exhausted one never
   ends up brawling.
4. **Sleep only when sleepy (user).** A creature whose sleep is at 0 walks to a
   bed it may use, lies in it (💤) and gains sleep until full, then gets up; full at night,
   it stays in bed until dawn (user). Never by the clock. A creature tired from hunger only
   skips the bed and eats when food is in reach.
5. **A Bed (user).** Room-only, one owner, one sleeper at a time. It is used by its owner
   and by anyone close to the owner, with no number limit (user).
6. **Close (user: friends above 4).** Parent and child; a couple whose love is above
   `CLOSE_FRIEND` both ways ("married": love decays, so full love would hold for a moment
   only); two friends whose friendship is above `CLOSE_FRIEND` both ways. Once close, a pair
   stays close until it drops below `CLOSE_KEEP` (3), so a tired spell that pauses
   socializing does not cost the bed it needs to recover (no death spiral).
7. **No usable bed (user).** The creature keeps doing its things but stays tired, so it is
   unproductive until it is housed. It still starts a family (`docs/LAW_life.md` rule 6).
8. **Ownership (user: reassigned when it matters, not by the clock).** The server reassigns
   owners (below) at most once a second, and only after something it depends on changed: a
   bed or room, the herd, a closeness, or a tired creature that found no bed. Housed = owns
   a bed or is close to an owner. Between reassignments, a tired creature
   with no usable bed claims a working bed that has no owner (a new bed is used at once).
   A change of owner never wakes a sleeper. A bed it cannot reach does not count.
9. **Medic bed and nest stay separate (user).** A boat arrival comes as a stranger: it has
   no bonds, so it needs a bed of its own. A hatchling is close to its parents from birth.
10. **The start (user).** The starter house has two 6 x 6 m rooms: seen from the doorways,
   the left one holds 2 medic beds on its left wall (a hospital), the right one 3 Beds on its
   right wall (a bunkhouse); each bed is turned head to the wall, side by side in the back
   corner. The starting herd owns the Beds from the first second (user).

## Ownership reassignment (server, on change)
1. Keep every current owner whose bed still works and who is still in the herd: friendly,
   or fallen from friendly (user: a fall keeps the bed, so a fight reshuffles nothing).
2. Mark the kept owners and everyone close to them as housed.
3. While a free working bed is left: give it to the unhoused creature that would house the
   most unhoused creatures (itself plus its unhoused close ones; ties go to the oldest, so a
   baby never outranks its parents); prefer the free bed
   nearest a bed owned by one of its close ones (so close ones sleep near each other).
The greedy pick in step 3 is the standard approximation for this covering problem; step 1
keeps owners stable so the herd does not reshuffle on every change.

## Signs (existing verbs and visuals)
- 💤 while it sleeps.
- A dialog balloon over its head, with no text or emoji (user), holding a Bed's icon when it is
  sleepy or its favorite food's icon when it is tired from hunger. White while it can meet the
  need (walking to its bed, food or basket stock); red from `WARN_SEC` (20 dilated s) before
  the need hits 0 when, now, it could not meet it the normal way (no food on the ground or in
  a basket; no bed it may use with a spot it holds or a free one), shown in every mode, and red while it starves (a crop is no
  normal fix). Sleep's lead is counted at its working drain. `docs/LAW_creature_state.md`
  holds the priority with the mood balloon. A friend with no bed of its
  own or a close one's asks for one in a white bed balloon in its free time, when nothing else shows (user).
  Every balloon shows only when the fix is missing (user): no food, bed or free place for that
  need it would walk to; walking to a fix shows the act's glyph, not a balloon.
- Tired from hunger with nothing on the ground, it eats from the nearest basket's stock
  before harvesting a crop (user).
- A sleeper lies on its side in the bed, centred on it, head toward the pillow; a downed
  body lies the same way on the medic bed's sheet (both on the bed's `Lie` marker). Getting
  up, it stands centred past the bed's foot, clear of the frame (user).
- The aim readout shows its bed (no hunger or sleep bars, user) ("own bed", "shares Pip's bed",
  "no bed").
- A bed's blanket is white while no one owns it and red once owned (user).
- A room-only piece whose room breaks goes grey and very dark, and shows through walls and
  other objects while staying solid (user), under its 🏚.
- The planks that close a working room wear its type's skin (`docs/LAW_room_types.md`).

## Data dictionary
| Name | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| `hunger` | float 0..1 | creature needs (server) | How fed it is | full at spawn; drains on the clock; +`MEAL_FILL` per food |
| `sleep` | float 0..1 | creature needs (server) | How rested it is | full at spawn; drains while productive; refills in a bed |
| energy | min(hunger, sleep) | derived | What it has left to work with | never stored |
| `owner` | Creature or null | Bed (server) | Who owns this bed | set by the reassignment |
| `parents` | [instance id] | creature (server) | Its parents, for closeness | set at hatch |
| `room_beds` | int, -1.. | creature (server) | Sleep beds in the room of its own bed, else the fewest a close owner offers; 0 no bed; -1 out of the herd | set by each reassign |
| `ROOM_ALONE_MOOD` | +0.5 | CreatureConfig | Centre lift of a bed alone in its room | constant (weight) |
| `ROOM_BED_MOOD` | 0.25 | CreatureConfig | Centre drag per bed past 2 | constant (weight) |
| `ROOM_MOOD_FLOOR` | -1.0 | CreatureConfig | Drag of 6+ beds, or of no bed | constant (weight) |
| `AWAKE_DAYS` | 2.0 days | CreatureConfig | Productive time from rested to sleep 0 |
| `HUNGER_DAYS` | 2.0 days | CreatureConfig | Clock time from full to hunger 0 | constant (pace) |
| `MEAL_FILL` | 0.5 | CreatureConfig | Hunger one food adds | constant (pace) | constant (pace) |
| `SLEEP_DAYS` | 0.25 day | CreatureConfig | Sleep from empty to full | constant (pace) |
| `CLOSE_FRIEND` | 4.0 of 5 | CreatureConfig | Friendship or love to become close | constant (user) |
| `CLOSE_KEEP` | 3.0 of 5 | CreatureConfig | Close ones stay close down to here | constant (limit) |

## Pipeline (per creature tick, server)
1. **Drain:** `hunger -= dt / HUNGER_DAYS` always (any ally state); productive mode -> `sleep -= dt /
   AWAKE_DAYS` (dilated days).
2. **Decide:** after jail and rampage, a creature carrying a body or an egg carries it to the end; a medic on call works and a creature with a combat
   target fights; then a sleeper stays asleep until full and the night is over, and a tired
   creature never enters RESCUE, SOCIAL, WORK or a training OFFER: it follows the player if
   led, else if sleepy with a usable free bed it enters SLEEP, else it eats, sits in comfort,
   or roams. Days are the current cycle's length (the dilated clock).
3. **Sleep:** reserve the bed, walk there, lie down; `sleep += dt / SLEEP_DAYS`; at 1.0 get
   up and release the bed.
4. **Eat:** a food it accepts adds `MEAL_FILL` to hunger (capped at 1).
5. **On change:** reassign owners (above), at most once a second, then count each member's
   `room_beds`. A room solved again in slices counts as a change when its answer lands.

## Interaction matrix
| Input \ stage | Drain | Decide | Sleep | Eat | Reassign |
|---|---|---|---|---|---|
| `hunger` | output | gates (tired) | 0 | refills | 0 |
| `sleep` | output | gates (tired), sends to bed | refills | 0 | 0 |
| food in reach | 0 | FEED | 0 | input | 0 |
| `owner` | 0 | which beds are usable | which bed | 0 | output |
| closeness | 0 | which beds are usable | 0 | 0 | groups owners |
| beds in rooms | 0 | usable or not | where | 0 | pool |

## Chart (base cycle about 30 s; days are dilated)
| Herd activity | Time to sleepy from rested |
|---|---|
| Always productive | 1.6 days |
| Productive half the time | 3.2 days |
| Idle | never |
A sleepy creature in a bed is back to full in a quarter day. Unfed, any creature is hungry
enough to eat after 1 day and tired from hunger after 1.6 days; fed whenever it has room, it
eats one food a day.

## Constant ledger
- `AWAKE_DAYS` 2: pace; a busy creature needs a bed about every other day.
- `HUNGER_DAYS` 2: pace; with `MEAL_FILL` it sets the herd's food bill at one food per
  creature per day (user).
- `MEAL_FILL` 0.5: pace; two foods fill an empty creature, and it eats again once half
  empty.
- `SLEEP_DAYS` 0.25: pace; a nap costs a quarter day of that creature's work.
- `CLOSE_FRIEND` 4: limit (user).
- `CLOSE_KEEP` 3: limit; the gap to 4 is the hysteresis that stops housing flickering.
- Roommates +0.5 / 0 / -0.25 per bed past 2 / floor -1: weight; a quarter of bored's -4 at
  most, so a bunkhouse alone never puffs. A bored neutral creature (-4) in a 4+ bed room
  crosses the -4.25 brew start: boredom plus a crowded room is a snap risk. Care sims, 900 s,
  3 seeds: 9-bed bunkhouses mean term -0.79, slow centre -0.03; 1-bed rooms +0.29, +0.84.

## Balance check (20 creatures, 3 beds)
One sleep (0.2 to 1) takes 0.2 day, so a bed gives 5 sleeps a day and 3 beds give 15. A
herd that is productive half the time needs 6 a day, so the beds hold; the limit is who is
close to an owner, not the number of sleeps.

## Measurement (egg funnel, probe events)
`pair` (a couple starts breeding), `nest_wait` (no free nest), `egg` (laid), and `tired_skip`
(a tired creature skipped socializing), so the sims show which stage loses the eggs. Live
tick keys: `hun_<sp>` and `slp_<sp>` (mean hunger and sleep), `asleep`, `tired` (awake),
`hungry` and `nobed` (subsets of tired: hunger is the low need; no bed to go to).
