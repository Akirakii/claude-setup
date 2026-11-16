# BRAINSTORM: gem ore and the pickaxe mine

Design only (/design-idea). Lines tagged (user) are decided; every other pick is proposed.
Tags: [C] checked this session, [M] from memory (not re-verified), [A] assumed.

## Decided (user, 2026-10-25)
- A gem ore in the map replaces the gem bush as the land's gem source.
- One ore on the map, 3,000 gems in total; its size shows the gems left; it shrinks to nothing.
- The player places a pickaxe mine by it: a workplace with one job, built for gems, paid like
  every other sign.

## Picks (user, 2026-10-25, Q&A round 1)
- **The mine works like the woodpile (user):** "infinite.. like we do with tree chopping job".
  Any number of mines; each is a job station with one miner and a reach ring; a mine whose ring
  reaches the ore can work it. [C: README: one chopper (INT 8) per woodpile, fells trees within
  its 24 m ring, logs stack in its frame, walk in to take them.]
- **Mined gems stack in the mine (user):** "a pile in the job, same as chop tree job". The miner
  carries what it struck back to the mine; the player walks into the frame to take them.
- **Ore away from home (user).**
- **After the ore is gone: nothing more (user).** Income falls to the kill bounty.
- **A mine's pile is not a theft mark (user):** thieves take loose ground gems, then pouches.
- **Haulers never carry gems (user):** gems leave a mine only by the player's hand, so mined gems
  fund nothing until the player throws them.
- So T2's MINE_SLOTS is cut: the drain rate is capped by miners (creatures) and sign gems, not by
  sides. The section 7 chart's "Mines" column still holds (each mine 4 gems/min at 15 s strikes).

## 1. Abstract
- **Roles:** a *deposit* (a finite stock in the land), a *converter* (a paid workplace), a
  *worker* (one creature), the *output* (gems that enter circulation), the *player* (funds the
  converter, decides how many converters and where the output goes).
- **The problem class:** turn a finite natural stock into circulating money through paid labor,
  so that (a) reinvesting is worth it, (b) the stock running out is felt, (c) nothing runs itself.
- **Ledger (gems):**

| Flow | Unit | Source of the number | Reader |
|---|---|---|---|
| Ore -> loose gems | gems per strike | MINE_YIELD | ore size, ground |
| Sign -> open time | 1 gem = 60 s, cap 4 [C: #371] | sign rule | miner shift |
| Build a mine | gems once | MINE_COST | player |
| Kill bounty | 3 per night [C: #371] | NIGHT_GEM_BOUNTY | the floor income when the ore is gone |

- **Net per mine, in the player's units:** gems per paid minute = 60 / MINE_STRIKE_SEC x
  MINE_YIELD - 1. At 15 s per strike and 1 gem a strike: 4 mined - 1 paid = **+3 gems a minute**.
  At 60 s per strike the mine only pays for itself (0 net): the strike time is the profit knob.
- **Pillars it must meet (lookups):** value enters by the wave, the land and new creatures
  (PRE); income grows only through what the player built and reinvests (PRE); income is capped by
  space or committed creatures, never by a price (PRE); a gem pays open hours, never a role (PRE);
  no hidden mechanics; natural on sight.

## 2. Research [M]
- **Age of Empires gold and stone mines:** a finite pile, villagers mine it, the pile visibly
  shrinks, its amount shows on hover; running dry pushes players to claim the next mine, often far
  from home. Closest match to the user's picture.
- **StarCraft minerals / expansions:** finite patches near the base force an expansion to a new
  patch; the expansion is exposed and must be defended.
- **Factorio ore patches:** each tile shows a count; drills on a patch, the patch depletes; output
  goes on belts to processing. Several drills share one patch (more drills, faster drain).
- **The Settlers mines:** a mine building on a deposit, one miner, the deposit runs out and the
  mine reports "exhausted".
Lesson across all four: finite deposits make *map control and expansion* the decision; the drain
rate is the player's choice (how many extractors), the total is fixed.

## 3. Theses
1. **Mine beside the ore (the user's shape).** A pickaxe mine stands next to the ore; its miner
   strikes the ore, each strike knocks MINE_YIELD gems loose onto the ground and shrinks the ore.
2. **Several mines around one ore.** As 1, but up to MINE_SLOTS mines (one per side of the ore),
   each with its one job. The player's reinvest lever is "open another mine", capped by the ore's
   sides (space) and miners (creatures); more mines drain the ore faster.
3. **Ore chunks and a cutter.** The miner breaks off ore chunks (an item); a hauler carries them
   to a gem cutter (a second paid workplace) that turns each into gems. A production chain.
4. **Claimed ore.** Whoever holds the ore's claim gets its gems; a founder could buy it (stage 2).

## 4. Socratic pass and antithesis (short, provisional)
- **T1** takes in sign gems + one miner, gives out loose gems; must exist: it is the user's ask.
  Breaks when: one job means income is flat (+3 a minute forever), so there is no reinvest
  decision at the mine itself; the reinvest goes only into other workplaces. Fine, but thin.
- **T2** adds the one decision T1 lacks: how fast to drain a finite stock. More mines = more gems
  now, a shorter life. Capped by space (sides) and creatures (miners): matches the cap pre-pillar.
  Failure: max mines is always right (gems now beat gems later)? Not if the sign cost is paid per
  mine and the gems pile up loose for thieves: draining fast floods the ground with theft bait.
- **T3** adds logistics (haulers, later rail) but two new pieces (chunk item, cutter) for one
  purpose. Redundant with the haul contract's purpose today; cut for now, logged for stage 3
  (ship chunks from a far city).
- **T4** depends on founders buying land, which is stage 3 design. Cut for now, logged.
- **Ore at 0:** the ore is gone and income falls to the kill bounty (3 a night). That is the
  user's "it should finish", and it is the felt end of the stock; the open question is what the
  player does next (Q4).

## 5. Scenes
- **T1/T2:** the ore is a knobbly crystal lump the size of a hut, 40 m from home past the woods.
  The player drops a pickaxe mine on its east side and throws 3 gems at its sign. A mole-ish
  friend with a pickaxe walks out, *tink*, two gems hop onto the grass, the lump shrinks a hair.
  By dusk a little pile glitters by the mine; a bored hedgehog sidles up and pockets one; the
  player sweeps the rest home. Night: wilds cross the ore field; the miner runs home. Weeks later
  the lump is a pebble, then gone, and the mines stand idle with an "empty" mark.
- **T3:** the same, plus a cart rolling chunks to a cutter by the bank. Reads fine; more parts.

## 6. Synthesis (recommended)
**T1 + T2:** one ore, up to MINE_SLOTS mines around it (each one job, each built for MINE_COST
and paid by its own sign); each strike knocks gems loose onto the ground by the mine; the ore
shrinks with the gems left and is removed at 0, leaving its mines idle. The ore sits away from the
start, so reaching it is a defence and expansion call. T3 and T4 go to `docs/TODO_stage3.md`.

## 7. Specify
**Data dictionary**

| Name | Range | Owner | Definition | Lifecycle |
|---|---|---|---|---|
| ORE_GEMS | 3000 (user) | config | gems an ore starts with | constant |
| ore.left | 0..3000 | the ore | gems still in it | -MINE_YIELD per strike; 0 removes the ore; saved |
| ore scale | 0.2..1.0 | the ore (derived) | visual size | (left / ORE_GEMS)^(1/3), floored at 0.2 until 0 |
| MINE_COST | gems, start 3 | config | one-off build price | constant (weight) |
| MINE_STRIKE_SEC | dilated s, start 15 | config | time per strike while on shift | constant (weight, profit knob) |
| MINE_YIELD | gems, 1 | config | gems loosed per strike | constant |
| MINE_SLOTS | 4 | config | mines one ore can feed (one per side) | constant (limit) |
| mine sign | 0..4 gems | the mine | its paid open time, 1 gem = 60 s | existing sign rule |

**Pipeline:** player pays MINE_COST -> mine stands on a free side -> player funds its sign -> a
creature takes the miner job (gate as other jobs) -> each MINE_STRIKE_SEC on shift: ore.left -=
MINE_YIELD, MINE_YIELD gems spawn loose by the mine, ore rescales -> at ore.left 0: ore removed,
each mine shows empty and stops taking pay.

**Interaction matrix** (input -> output): sign gems -> shift time; mines count -> drain rate and
loose-gem rate; ore.left -> scale and whether mines work; loose gems -> theft marks and player
pickup. No all-zero row.

**Charts (one ore, 15 s strikes, 1 gem each = 4 gems/min/mine):**

| Mines | Gems/min mined | Net/min after signs | Ore lasts (paid minutes) |
|---|---|---|---|
| 1 | 4 | +3 | 750 |
| 2 | 8 | +6 | 375 |
| 4 | 16 | +12 | 188 |

Ore scale: 3000 -> 1.00, 1500 -> 0.79, 300 -> 0.46, 30 -> 0.22, 0 -> gone.

**Loops:** (1) reinvest, positive: gems -> more mines and more open workplaces -> more gems; capped
by MINE_SLOTS (space), miners (creatures) and the 3,000 stock. (2) depletion, balancing: more
mines drain faster. (3) theft, balancing: loose gems pile, thieves take them first [C: PR 9], the
cop returns them. Contradiction check vs the pre-pillars: income capped by space and creatures,
not price: holds; value from the land: holds; nothing runs itself: holds, since mined gems lie on
the ground and fund nothing until the player throws them (no carry-to-sign).

**Constants:** MINE_SLOTS and ORE_GEMS are limits; MINE_STRIKE_SEC, MINE_YIELD, MINE_COST are
weights. No hidden thresholds.

## 8. Open questions for the user
1. One mine per ore, or up to 4 around it (recommended)?
2. Mined gems: loose on the ground (recommended) or a pile on the mine the player empties?
3. Ore placement: away from home (recommended) or next to the start?
4. After the ore is gone: income falls to the kill bounty (as asked), a new ore appears elsewhere,
   or the next ore lies in a second city's land (the stage 3 reason, later)?
- Balance (playtest, not design): the early ramp. With bushes gone, the first MINE_COST comes
  only from kill gems (3 a night) [C: #371 sim: first bush on night 17-20].
