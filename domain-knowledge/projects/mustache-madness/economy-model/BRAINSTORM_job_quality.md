# BRAINSTORM: job quality (pay by qualification, stress)

Design only (/design-idea). Lines tagged (user) are decided; every other pick is proposed.
Tags: [C] checked this session, [A] assumed (gate values are checked in /design-code).

## Decided (user, 2026-10-25)
- Jobs differ in pay and in stress; pay is based on the job's qualifications (user).
- A creature still takes the job its stats fit; pay follows the job, never steers who takes it
  (user). Keeps the pillar "a gem changes how much a creature works, never at what".
- A better-paid job's sign burns faster: the extra gems per open minute are the worker's wage
  (user). So a skilled workplace costs the player more per minute.
- A stressful job drains the worker's mood (user), feeding the existing low-mood chain (puffing,
  theft, snaps); leisure repairs it.
- The stressful jobs are miner, cop, medic, builder (user).
- Stress has two levels, calm or stressful (user).
- Build in AFK with the gem ore, code design to merge (user).

## Why it exists (essence)
- **Pay:** links raising to wealth. Training and the university make a creature richer; rich
  creatures are where founders and landlords come from (stage 2). Without it every shift pays 1.
- **Stress:** gives work a cost to the creature, so tough jobs need leisure nearby. Without it,
  work never touches mood [C: README: only needs tire a creature].
- Neither is a flat bonus: pay moves gems creature to creature, stress moves mood; both read on
  the job panel.

## Rule (proposed)
- **Wage per open minute** = 1 + qualification steps, where a step is each 4 INT the job's gate
  sits above the base gate 8, plus 1 for a learned trade (architect, builder). The sign burns that
  many gems per minute; all of it goes to the worker's pouch.
- **Stress** per job: calm 0, stressful 1. Each shift of a stressful job takes STRESS_MOOD from
  the worker's mood (one shift = one game minute). Calm jobs take nothing.
- Shown on sight: the sign reads its burn (💎 2/min), the job panel reads pay and a stress mark.

## Sketch table (gates [A], from README; checked in /design-code)

| Job | Gate | Wage/min | Stress |
|---|---|---|---|
| chopper, farmer, clerk, payer, bartender, cook | INT 8 | 1 | calm |
| hauler | INT 0 | 1 | calm |
| miner | INT 8 | 1 | stressful |
| cop, medic | INT 8 | 1 | stressful |
| teacher, professor | INT 14 | 2 | calm |
| lab | INT 20 [A] | 4 | calm |
| architect | trade + INT top | 2+ | calm |
| builder | trade | 2 | stressful |

## Loops
- Pay: skilled sign burns faster -> skilled creatures richer -> they buy more (gems pass to
  servers) and found shops sooner. Capped by how many skilled places the player keeps open.
- Stress: stressful shift -> mood down -> work slower (mood sets work pace up to 1.5x, floor 1.0
  [C: pick 19]) and more puffing -> player adds leisure. Balancing.

## Constants
STRESS_MOOD (weight), INT_PER_STEP 4 (weight), TRADE_STEP 1 (weight). No hidden thresholds.

## Open
- Balance: skilled signs may cost too much to open early; playtest.
