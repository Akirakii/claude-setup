# BRAINSTORM: food theft (design only, 2026-10-24; picks are Claude's until tagged "(user)")

User idea (user): a broke creature that is very hungry steals food; the one it stole from gets angry
and fights it or calls the police. Context: `docs/BRAINSTORM_economy_model.md` (dish 2 gems, raw
crop 1 gem, a creature with 0 gems eats only if a friend treats it, or steals).

## Abstract
- Roles: a needy taker (0 gems, unmet need), an owner (made or sells the food), an enforcer
  (police), the player (places food, police, jobs).
- Ledger: food units move taker <- owner; no gem moves (the taker has none). The owner loses one
  sale (1 gem raw, 2 gems dish). Mood moves on both. Jail time on the taker.
- Framings: (1) a floor valve: no creature starves only because it is broke; (2) a drama the
  player reads; (3) a sign that the economy fails someone (broke and jobless), which the player
  answers with jobs, a class, or food placement.

## Research (all from memory, not checked)
- RimWorld: hunger drives mental breaks (food binge); theft is by outsiders, not colonists.
- Oxygen Not Included: stress responses (binge eating) are a need's failure shown on sight.
- Prison Architect: theft and contraband draw guards; punishment is a place (solitary).
- Dwarf Fortress: grudges between citizens lead to fist fights; fights can turn lethal (a tone
  warning for us).

## Theses
1. **Grab and run (recommended):** a hungry broke creature grabs one food unit from a basket or a
   table and runs with it held over its head, shown as stolen, then eats it. If the owner sees
   it, the owner reacts: fights it or calls the police.
2. **Starving snap:** reuse the mood snap; a starving creature snaps and its theft target is food,
   not a vault. Same purpose as 1 with an indirect trigger the player cannot read as hunger. Cut:
   the trigger hides the need.
3. **Tab:** the broke eats and owes the owner; the owner is angry until repaid. Cut: a hidden debt
   is per-unit tracking (antipattern).
4. **Beg only:** the hungry broke begs at the table and a friend treats it (already decided). Kept
   as the step before theft, not a replacement: with no rich friend near, it starves.

## Socratic and antithesis (thesis 1)
- Why must it exist: without it a broke, jobless creature with no rich friend starves, a grim end
  the tone forbids.
- Loop: broke -> steal -> jail -> still broke -> steal again. Termination needs a way out: a wage
  (a job), a treat, or the library (for a creature too weak for any job). The repeat thief is the
  player's sign that someone needs a job.
- Failure: thefts nobody sees are free meals, so a basket far from its farmer feeds thieves for
  free. Arguably fine: placing baskets is the player's call.
- Failure: a fight that knocks the thief down risks its death (down too long = death), a hungry
  creature dying for a crop. Tone breaks. The fight must be a cartoon scuffle, not a knockdown.
- Passive policy: a player who does nothing sees thefts, fights and jail time, which cost food,
  mood and work hours. So it is a real cost the player can act on.

## Scene
The cook sets a steaming dish on the table. A skinny broke frog with a 🍗? thought creeps up,
snatches the dish and waddles off with it over its head. The cook spots it: a hot-headed cook
chases it into a dust cloud of fists and the frog drops the dish; a timid cook points and
shouts, and a cop runs the frog to jail.

## SPECIFY (proposed)
- **Steal gate:** hunger at or below its warn line (the hunger thought already shown), spendable
  gems 0, and no treat came. One unit only.
- **Stolen food:** held over the head, marked stolen, until eaten (EAT_SEC after the grab).
- **Owner reaction:** only when the owner sees the grab (within SEE_RADIUS). Its temperament picks:
  fight (chase; on contact a scuffle, the thief drops the food, both lose mood; no knockdown) or
  call (the nearest cop arrests the thief to jail).
- **Jail:** the thief sits out JAIL_SEC; open: is it fed there.
- **Constants:** SEE_RADIUS, EAT_SEC, JAIL_SEC (limits); mood dips (weights).

## Picks (user, 2026-10-24)
- Steal gate: hunger thought showing + 0 spendable gems + no treat came; one unit (user).
- Reaction by temperament (user): hot-headed fights (chase, scuffle), timid calls the nearest cop.
  Checked: personality has a `temper` value (derived; `personality_component.gd`).
- Outcome (user): a cartoon scuffle, no knockdown; the thief drops the food, both lose mood. A
  jailed thief gets a plain meal, so the loop cannot starve it.
- Basket (user): raw crops sell only while the farm is open (paid time, farmer on shift).
- Still open: SEE_RADIUS, EAT_SEC, JAIL_SEC values; the temper line between fight and call.
