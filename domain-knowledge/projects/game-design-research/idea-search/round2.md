# Idea search, round 2 (2026-11-10)

## Synthesis of critic round 1 (round1.md; pre-critic copy round1.pre-critic.md)
Every finding below was checked against the files the critic cited.
- **SEVERE frame 1, the triad was missing (fixed):** the shortlist was bare rules. In the user's model an
  idea is fantasy + logic + aesthetic aligned, and testing rules alone is the splitting the user rejected
  (game-idea-triad memory). Claude's 2026-11-09 sketch had promised "whole ideas (the action, what ties
  players, who answers, and its fantasy and look)" and then delivered rules. Fix: round 2 writes each idea
  whole (fantasy, rule, look and a 5-second clip in one go), and the weekly playtest gets a rough build of
  the whole thing, not a rules test. Limit: the formula checks still only see the rule.
- **SEVERE frame 2, the co-op ask was parked (fixed in part, the rest goes to the user):** 5 of 7 were
  team games, and "the user's call" parked the question (anti-pattern 25). At 3 players a team game is 1v2,
  and the user tests with 1 human + 2 bots, so in dev the counter is always a bot, an AI counter (B2 logic).
  Fix: round 2 generates in the co-op and semi families the grid missed (critic list D). Team games stay
  only as a branch, if the user counts friends split into teams as co-op.
- **MAJOR, the pool comparison meant nothing (retracted):** pool B's C and − moves are built to break the
  formula, so 33% vs 16% reflected the move mix, and counting ~ flipped the order. After the 15 rating
  fixes below, strict passes are **A: 1 of 18 (A13), B: 3 of 50 (B8, B11, B20)**, and two of B's are
  existing games. Claude told the user "the twists did better"; that claim is withdrawn.
- **MAJOR, the checks missed the twist, the tail and gates 3/5/6 (fixed):** checks below add F7, G and W.
- **MAJOR, same family twice (fixed):** Statues and Decoy Escort both hid "which look-alike is a player".
- **Rating fixes applied in round1.md:** A2 F3 ~, A3 F5 ✗, A8 F1 ~, A14 F1 ~ and F5 ✗, A18 F3 ✗, B5 F3 ~,
  B6 F1 ~, B24 T ~, B33 F3 ✗ and F6 ✗, B41 F3 ~ and T ~, B43 F3 ~ and T ~.
- **Cut (critic, agreed):** Statues (no goal for hiders: standing still wins; SCP-173 in SCP: Secret
  Laboratory plays the rule [critic, assumed]), Tripwire (defenders idle, gate 7; Deathrun exists),
  Silent steps (silence can't be enforced over Discord; a reskin of The Mind), Secret debts (pooled bank,
  no counter verb).

## Checks for round 2
F1–F6 and T as in round1.md, with the critic's readings: an NPC crowd that must pass as human is AI
content (F1 ~); teammates acting side by side or idle make F3 ~ or ✗; F5 checks the search budget against
the suspects at 3. Added:
- **F7 tail:** what keeps round 50 new (players, generated layouts, player-made maps, strangers).
- **G gates 3/5/6:** time pressure makes people talk · new players can lose at the smallest crew · one
  player can't clear it alone.
- **W whole:** fantasy, rule and look written together; the 5-second clip in one sentence.
- **T:** 1 human + 2 bots can run the rules, and the human's counter isn't only bots (else ~).

## Round 2 ideas (written whole)

### C1 Thin Ice (co-op): split view, two-way, plus a physical channel
- **Fantasy:** friends crossing a frozen lake at night to reach a cabin before dawn.
- **Rule:** you see the cracks under your friends' feet, never under your own, and every step weakens the
  ice for whoever comes next.
- **Look:** moonlit blue ice, a lantern each, cracks glowing gold only under friends.
- **Clip:** "I threw a pebble on his crack, he stepped on it anyway and went through."
- **Channel:** toss a glowing pebble where it's weak (bots throw and read pebbles). Voice is allowed.
- **Pre-check, dominant strategy (Claude):** single file in a scout's steps loses, because stepped ice
  is weaker; standing still loses, because ice weakens under a standing player too; spreading out loses
  information, because you see cracks only inside a friend's lantern light.
- **A fall:** the fallen friend is fished out by two others (costs time, nobody leaves play, DRS rule 2).
- **Scene at 3 (Claude):** A sees cracks under B and C; B pebbles a crack in front of A; A trusts it, C
  doubts B's aim. **At 6:** six lanterns, more light, more cracks seen; risk: one player calls everything.
- F1 ✓ (generated crack fields) · F2 ✓ · F3 ✓ (two-way) · F4 ✓ · F5 ✓ · F6 n/a · F7 ~ · G ✓✓✓ · W ✓ · T ✓
- **Prior art:** not found (1 search). Ice Lake is a board game where skaters leave cracks
  ([rulespal](https://rulespal.com/ice-lake/rulebook)); Frostbite Frenzy has ice breaking under weight
  ([vgdb](https://www.vgdb.co/games/frostbite-frenzy)). Near DRS Blind Floor, which was one-way (one
  spotter in a booth, `deathly-reality-show/docs/minigames-v2.md:7`).

### C2 Mirror Mansion (semi): a hidden crewmate plus split view by position
- **Fantasy:** friends exorcising a haunted mansion; one of them is secretly possessed.
- **Rule:** one friend is possessed and only mirrors show it; the crew carries lit candles to the ritual
  circle while the possessed snuffs them.
- **Counter verb:** each player has one splash of holy water; a wrong splash puts out your own candle.
- **Look:** candlelit Victorian halls, tall mirrors; in a reflection the possessed has a goat's skull.
- **Clip:** "In the mirror behind us, Jake had a goat's skull."
- **Pre-check:** everyone camping one mirror loses, because candles start in far rooms and burn down;
  random splashing loses, because a wrong splash costs a candle.
- F1 ✓ (one mansion; mirrors and candle rooms shuffled) · F2 ~ (candles + mirrors + splash) · F3 ✓ ·
  F4 ✓ · F5 ~ (at 3: 1 vs 2, thin) · F6 ✓ · F7 ~ · G ✓✓✓ · W ✓ · T ~ (a bot possessed is an AI traitor)
- **Prior art: crowded family.** Horror House on Spook St. (4–6 online, exorcise a house, one player
  possessed, [itch](https://omoriarty.itch.io/horror-house-on-spook-st)), Masks of Deception
  ([playpile](https://playpile.gg/games/masks-of-deception)), Deceit II ([gematsu](https://www.gematsu.com/games/deceit-ii)),
  Secret Neighbor. The mirror reveal: not found (1 search).

### C3 Getaway Van (semi): a hidden faction in one shared vehicle
- **Fantasy:** clumsy bank robbers escaping in one van; one of them is an undercover cop.
- **Rule:** one robber in the van is an undercover cop; seats rotate at every red light, and only the
  map seat knows the way.
- **Counter verb:** two robbers together can shove a suspect out of the van.
- **Seats (Claude):** driver, map (sets a dashboard arrow, physical), and cash windows (loot bags fall out
  if nobody holds them). The cop wins if the van reaches the police station or the loot is gone.
- **Look:** 70s cop-show city, chunky van, siren colours.
- **Clip:** "We shoved Mia out, then Leo drove us straight into the police station."
- **Pre-check:** "always shove the map seat" fails because the cop can sabotage from any seat (crash,
  drop bags); a wrong shove costs a pair of hands for the rest of the run.
- F1 ~ (generated grid city, siren timer, no police AI) · F2 ~ · F3 ✓ (advice from a suspect seat is
  doubted, so no quarterback) · F4 ✓ · F5 ✓ · F6 ✓ · F7 ~ · G ✓✓✓ · W ✓ · T ~ (bot cop)
- **Prior art:** not found (1 search). Feed the Kraken is the board-game cousin (hidden factions on one
  ship, checked in research.md 2026-11-09).

### C4 Well Divers (co-op): split view, two-way, plus bodies on one rope
- **Fantasy:** friends fishing lost treasure out of a deep, dark well.
- **Rule:** one friend dangles down the well and sees the eels; the friends holding the rope see the
  treasure through a periscope.
- **Channel:** voice is allowed; rope tugs are the physical signal bots use.
- **Look:** a stone well, torchlight, eels glowing green, gold glinting.
- **Clip:** "They yanked me up straight into the eel's mouth."
- **Pre-check:** the diver decides grabs and dodges, the holders decide depth and when to pull, so both
  ends decide (gate 7); the air runs out, so talk is under pressure.
- F1 ✓ (generated shafts) · F2 ✓ · F3 ✓ · F4 ✓ · F5 ~ (at 6: two ropes, or idle holders) · F6 n/a ·
  F7 ~ · G ✓✓✓ · W ✓ · T ✓
- **Prior art:** not found (1 search). Nearby: Brains & Brawn (each player sees the level slightly
  differently, [BAFTA YGD](https://ygd.bafta.org/competition/competition-news/2021/brains-brawn)),
  Barrow Bros (well co-op, no rope, [moddb](https://www.moddb.com/games/barrow-bros)).

### C5 Paper Boat (co-op): jobs > hands (the proven juggling family, as a control)
- **Fantasy:** tiny friends sailing a paper boat down a rain gutter to the sea.
- **Rule:** the paper soaks wherever water sits, so someone always has to bail, hold the folds or
  steer, and there are always more jobs than people.
- **Look:** giant raindrops, floating leaves, a gutter at ankle height.
- **Clip:** "The bow went soggy and folded over with Sam inside."
- F1 ~ (gutter courses) · F2 ~ (3 jobs, all plugged into one boat) · F3 ✓ · F4 ✓ · F5 ✓ · F6 n/a ·
  F7 ~ · G ✓✓✓ · W ✓ · T ✓
- **Prior art:** the family is proven and crowded (Overcooked, RV There Yet?, Sea of Thieves holes).

### Teams branch (only if the user counts teams as co-op); fantasy added after the rule, flagged
- **Ring Thieves (Smuggle, fixed):** at a wedding, a gang of guests must pass the stolen ring hand to hand
  during the circle dance and get it out the door before the last song; the in-laws get one frisk fewer
  than there are thieves. F1 ~ (NPC dancers needed at 3) · F5 ~ · T ~.
- **Star in Disguise (Decoy Escort, fixed):** walk a pop star out through a crowd of identical mascots;
  the paparazzi get three photos, and guarding too closely gives the star away. F1 ~ · F5 ✗ at 3.

## Shortlist for the playtest (thesis, Claude)
1. **Thin Ice (C1):** cleanest pass (no ✗, one ~), co-op, physical channel, not found as a game.
2. **Well Divers (C4):** co-op, two-way split view on one rope; ~ at 6.
3. **Getaway Van (C3):** the semi option, a hidden faction in one vehicle; not found as a game.
Kept as alternatives: Mirror Mansion (crowded family), Paper Boat (control from the proven family).
Kill lines and the cheapest test form come after the critic.

## Synthesis of critic round 2 (2026-11-10): stopped, frame goes to the user
Checked by Claude: The Tilt's split sight, "you never see your own" key in a loop
(`deathly-reality-show/docs/minigames-v2.md:91`); its human playtest is still the top todo
(`docs/todo.md:3-5`); Blind Floor was cut as a quarterback machine (`minigames-v2.md:7-10`).
- **SEVERE frame, not fixable inside this method:** every round-2 idea is a round-1 rule with a fantasy
  and look added (C1 = A9, C4 = A6, C3 = B28 + B29, C5 = B26, C2 = the Among Us family). That is the
  user's rejected "one seed, derive the other two". The method is logic-first by construction: the grid
  makes rules and the formula checks rules. W (whole) passed all five, so it was a format check that
  can't fail; dropped. Only C1's "stepped ice weakens" and C5's "paper soaks" came back from the fantasy
  into the rule. **Taken to the user.**
- **MAJOR:** C1 and C4 are one family (danger near me that only a friend sees), and that family is
  already built as The Tilt and has never been playtested. Recommendation (Claude): playtest The Tilt
  before building anything in this family.
- **MAJOR:** the checks can't see the caller seat under Discord, how much of the core the dev crew can
  test, or the build cost per week; F7 and G rate every idea the same.
- **Per idea (critic):** C2 cut (1 vs 2 at 3, same as Horror House on Spook St.); C3 has a quarterback
  map seat and nobody shoves at 3 (F5 ✗); C4 holders are one mind on one rope (F3 ~, F5 ✗); C5 turns into
  station camping (F3 ~); C1 grows a caller at 6, soft-locks when two are in the water, F1/F2/F5 ~.
- **Round 3 not run:** its frame finding is a question about the method itself, which only the user can answer.
