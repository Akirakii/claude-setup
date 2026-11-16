# Design dialectic log (2026-11-05)

Thesis by the main session, antithesis by one teammate agent ("critic"), synthesis by the main
session; each round's synthesis is the next thesis. The current text is `docs/design-v2.md`.

## Round 1
**Thesis:** five kinds of moment, each a different crew question (items: what is it for; moods:
what does the button want; live games: who leaves the button; blackouts: who can see; paths: what
if we do the weird thing). 17 items, 10 moods, 8 live games, 5 blackouts, 6 routes, 5 loops.

**Antithesis (critic), ranked:**
1. Nothing scales the count from 1,000 to 1B (+1 hands, no rate rewards).
2. The blackout "exam at 90%" has no stakes (a milestone resets the ceiling) and fires in the
   first seconds of silent stage 1.
3. The blind seat isn't blind: pressing is by proximity, so the presser just turns around.
4. Moods are parallel play; Shy/Low/Airborne and Lonely/Crowded are variants; a dud gives no clue;
   colours become a lookup table by run 2; "Adjusting." repeats.
5. Item answers (Mop, Extinguisher, Tape) turn chores into shopping and their names explain them.
6. Fixed loss-order unlocks lock routes behind 8–11 lost runs; host's save punishes rotating hosts.
7. One slot starves 8 players and swamps 2; Strike triggers by accident while shopping.
8. The Lie is green light again; The Tower has no sight split; Greedy is luck + PvP.
9. The eye is hidden (user, 11-03), but two paths need it.
Variants: Leak/Sinking Button, Hot Box/Fragile Delivery, Unwatched/Blind the Eye, Giant Room/
Trampoline. Gaps: onboarding, ending hints, per-run variety, per-player tasks by crew size.
Must survive: the five questions, in-room culprit losses, the dud, Strike, Overflow, VIP room.

**Synthesis (round 2):** see the "Changes in round 2" list at the top of `docs/design-v2.md`.

## Round 2
**Antithesis:** the scale math made stages last seconds; Blink Count was solo-able by walking
out and back; moods ignored impacts once hands fade; Outside the Box was a free score machine; no
host→client spec for moving bodies; the Maze was under-specified; three chores at once unreadable;
luck culprits (fire, potato); the eye reversal decided for an AFK user. Variants: Sequence/Taking
Turns, Blink/Hunt both "press N", Twins/Crowded, Block World with no action.
**Synthesis (round 3):** S = goal/10,000 with a seconds table; the signal only runs while the seat
is occupied; moods gate impacts; Contrary; the shake scores nothing; one channel spec; chores cap
at 2 with a wall each; fire blames who spread it; the eye stays hidden behind a flag; Patience,
Fair, Hunt answers *which*, Maze avoids hazards, Block World digs.

## Round 3
**Antithesis:** "seat occupied" broke Hunt, Sequence and Maze; vertical pushes questioned; Maze walls
would collide with items; Contrary dead from stage 4; Greedy meaningless at a frozen gate; foil
hat = blame immunity; no attribution rule for impacts. Specs missing for Patience, Twins, cart
riding, tape, Freedom, Block World. Variant: Fair ≈ Sequence; Leak is the weakest chore.
**Synthesis (round 4, settled):** the seat is a person; knockback already lifts (checked);
walker-only Maze walls; Contrary refuses the top item; Greedy is the stage-8 gate with the exit as
stake; anonymised hat blame; last-toucher attribution; Freeze replaces Fair; the Leak wanders.
