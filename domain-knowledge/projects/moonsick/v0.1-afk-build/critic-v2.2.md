# Critic v2.2 (2026-11-12): powers, 10 s turn-back, dawn awards, practice

Read: `docs/design.md` (v2.2), `~/.claude/design-anti-patterns.md`. Nothing played; all reasoning from the doc's numbers.

## Severe

**S1. Three of the five dawn awards pay for betrayal.**
- Problem: Wrong-cure champion pays for sabotage (a wrong cure pushes a friend a third closer to turning). Pan enthusiast
  pays for panning anyone, healthy friends and bait included. Hungriest pays for catches. Every turned player gets one
  forced catch, so the tiebreak is whoever took the optional second catch in the 10 s window. Bodyguard counts raw
  shoves, so it pays for keeping the rowan and shoving after the friend turns instead of curing them.
- Why: awards are a second currency. A saboteur can earn two titles with no diagnosis at all; the best doctor earns
  one. That breaks the pillars "betraying must never pay off more than curing" and "lies come... never from a reward"
  (A6, B17: a free score machine).
- Fix: keep Best doctor (cures that worked). Change Bodyguard to count only catches broken. Replace the joke awards
  with results the rules force, never choices: Most tricked (most fake signs), Long shot (cured at the lowest odds),
  Moonstruck (most cases). Put the awards in design.md, which doesn't mention them yet.

**S2. The howl wipes out the werewolf's own counter, and it's always worth pressing.**
- Problem: the counter is "wade the pond and stand still". The howl shows everyone within 30 m, still or not.
  Werewolf hunger is 21–37 s (0.75 factor) and the cooldown is 25 s, so the howl gets about one use, pressed at the
  turn. On top of the turn rule (anyone further than 15 m shown for 10 s), the werewolf sees the whole crew at t=0.
- Why: against a werewolf, the only answers left are running or a wolfsbane shove. That breaks the pillar "each
  creature has its own ways to deal with it". After the cure, diagnosing a werewolf no longer changes how you hide.
- Fix: everyone hears the howl, and it shows only those who **move** in the 3 s after it, within 30 m. This keeps
  "stand still" as the counter and turns it into a shared freeze moment (it fits the funny-scary tone). It also forces
  a choice on players caught mid-flight: freeze or keep running.

## Major

**M1. A second catch in the 10 s window punishes the people who helped.**
- Problem: at people's speed, an awake human walks away at equal speed. So the people a second catch can actually
  reach are the ones next to the catch: unarmed helpers, rescuers whose cure is waiting its 3 s after a shove, and
  knocked-out friends (so panning someone as bait now pays twice). It works against "helping beats fleeing".
- Why: the bot night (one troll, 3 catches) is a bot artefact (B23), but the shape holds with humans too: the punished
  spot is the rescue spot. The user said only "transform to human after first kill but should take perhaps 10s". The
  "second catch is possible" part is Claude's, sitting next to a (user) tag (A6).
- Fix (smallest, keeps the 10 s): nobody can be caught during the 10 s turn-back, and powers are off (the same as the
  2 s turn-in). The creature visibly shrinks back over the 10 s.

**M2. Grab, then stomp, makes a catch unbreakable.**
- Problem: the doc doesn't say whether a power works during the 2 s catch hold. A troll that grabs and then stomps
  knocks back every rescuer within 3.5 m and lowers their rowan, so nobody can break the catch. Also unspecified: how
  long "lowered" lasts and how far the knockback reaches. If re-raising a cure triggers the shove's 3 s wait, a troll at
  1.15× closes 3.5 m in about 1 s and holds for 2 s, so a pair loses every time.
- Why: it kills the pair/rescue counter, the one cooperative answer to every creature (B19: an under-specified rule).
- Fix: no powers while holding someone. A lowered cure can be raised again after 1 s, which is shorter than the troll
  needs to close in and hold, so a pair that reacts still breaks the catch and a lone holder doesn't.

**M3. About 1 practice night in 3 never makes the player sick.**
- Problem: the first case is forced onto a bot, and the rest are random. In a 6-seat practice night there are about
  6 more cases, so the chance the player is never sick is (5/6)^6 ≈ 33%. That lesson is half of rules 1 and 2:
  feeling inner signs, telling others, quick chat 1–4, being panned out of fear.
- Why: practice is the only tutorial (bots never fill online seats).
- Fix: put the second case on the player. In practice, play no trick on the player before their first real case, so
  the first inner sign they ever feel is real. Honest bots by default is right, and `--liar-bots` is fine as a dev
  flag.

## Minor

**m1. The leap is an always-press chase boost, it breaks a counter nobody had, and the doc has slips.**
- Problem: every 6 s with no cost is close to the whole vampire hunt, so it's just extra speed. The tree house isn't
  any creature's stated counter (the doc's "each breaks one way of dealing with it" line doesn't match the counters it
  lists). Also unspecified: whether a leap that lands behind a lone armed player gets around the front-only shove.
- Doc slips: the build plan still says v0.1 has no powers beyond speed and senses, and it lists other powers (vampire
  flight, troll breaks doors). The practice rules (first case on a bot at 25 s, honest bots) aren't in design.md.
- Fix: leap every 10 s, with a loud landing that players hear within 20 m. The grab only starts after the vampire
  lands, so the target can turn and shove. Update the build plan, and ship powers behind a flag that is off for the
  user's first playtest, so the playtest checks the core first (RULES 2).

Verdict: not ready to build powers or awards. Fix S1 (awards) and S2 (howl), close M1 and M2 with the "no catch / no
power" rules; the core is untouched.
