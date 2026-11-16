# Fixing past games with the formula (2026-11-09)

Formula (user, 2026-11-09): **low content, low coupling, but high coupling between players.**
Players are coupled when one player's action changes another player's result through the hub, and
everyone can see who did it (see `research.md`, 2026-11-09 entries). The process follows the global
CLAUDE.md: thesis, then an isolated critic, then synthesis. These are rough directions, not builds.
The user's usual test crew is 1 human + 2 bots.

## Thesis (Claude, round 1)

### Red Button Experiment (2–8, press one button 1B times)
- Broke: the narrator rewrote what the button does (high feature coupling); everyone pressed the same
  button side by side (no player coupling).
- Fix: the button's rule never changes: a press adds to one shared counter. The narrator is only a voice.
  Upgrades change how much a press adds, never what pressing does. Player coupling: the counter is
  also the team's money. Anyone can spend it on upgrades at any time, so one player's purchase sets
  everyone back (Gamble With Your Friends' shared bank). The button only counts when two players press
  within the same half second, so the presses are pairs and both people decide at the same moment.
- Content: one room, ~6 upgrades.

### Pet the Cat (2–8, keep a huge cat calm by petting)
- Broke: everyone does the same job side by side (no player coupling). The user's reason for dropping
  it isn't recorded ("i dont like this one"), so the fix may miss what they disliked.
- Fix: the cat is the hub with three spots: head (scratch), belly (rub), tail (hold). Its calm is one
  shared bar. The cat wants one combination at a time, and only the player at the head sees its face
  (which spot it wants next); the others feel it only through the bar. A wrong spot touched drops the
  bar for everyone, and the cat attacks whoever touched it.
- Content: one living room, one cat, 3 spots.

### Deathly Reality Show (3–6, deadly TV game show; active project)
- Broke: v1 had no player coupling ("requires no cooperation at all"). v2 Switchboard got coupling
  from stacked hidden rules (secret names, edge reading, timers, shuffles); the user chose to replace it.
- Fix: one coupling for the whole show instead of new rules per minigame: contestants are chained in
  pairs (Chained Together's chain, as a show gimmick). Each minigame is a simple obstacle course
  (pit, blades, tilting floor) with no new rules; the chain makes every jump a two-person decision,
  and a fall drags the partner. Physical, visible, readable by bots.
- Content: 3 courses; no per-game rules.

### Hordeline (2–8, train defense with Vampire Survivors upgrades)
- Broke: solo chore loops, nobody steers (no player coupling); the upgrade layer added feature coupling
  and content. User: "hard to find good ideas on a Vampire Survivors base".
- Fix: the train is the hub (RV There Yet?'s one RV). One player drives (speed and junction choices) and
  can't shoot or shovel; shovelers feed the furnace that sets the driver's top speed; gunners protect
  the shovelers. Each role's result depends on another's. Cut the upgrade layer to a few pairs or drop it.
- Content: one track with junctions, ~3 weapons, one enemy type.

### Mustache Madness (assumed single-player; 4 genres mixed)
- Broke: four games' worth of features, all connected (high feature coupling + high scope).
- Fix: keep one of the four: the Overcooked part (frantic resource management under time pressure),
  made co-op: friends run one creature ranch through a night siege, jobs chained (feed -> harvest ->
  craft -> defend). Drop the farming, tech and colony parts.
- Content: one ranch, 2–3 creature types.

### Dungeon Pets (single-player, first-person creature pack)
- Broke: player too strong, screen unreadable, managing each creature was a chore, layers stacked.
- Fix: the friends are the pack. Each friend plays one creature type with one ability that only works
  on or with another creature (one carries, one heals, one stuns). No managing individuals: each friend
  manages themselves.
- Content: 3–4 creature types, one dungeon.

### Assemblia (single-player, robot army that emerges from rules)
- Broke: no recorded reason; its identity was emergence from coupled rules (high coupling on purpose).
- Fix: the formula says to get emergence from friends, not rules, which removes Assemblia's identity.
  Recommend not fixing it; if anything, friends hack and carry enemy robots back as a team (R.E.P.O.-like).

## Critic round 1 (summary)
Cross-cutting: the "Broke" lines were Claude's reading stated as fact; two fixes put the cue or the
decision in one seat (quarterback); none played the 1 human + 2 bots crew. Red Button: frame wrong (the
shared money already existed, `core-design.md`: "the count is both progress and the crew's shared
money"; a pair press is mashing). Pet the Cat: frame wrong (drop reason unknown; the head reader is a
quarterback; it ignores the user's own words: no narrator, no shop, keep petting, parkour and floor-is-lava
minigames). DRS: holds with fixes (pairs leave one solo at 3 players; anchor-and-hop; death rule
missing; ignores live work on Bomb Relay and The Tilt). Hordeline: drop the upgrade layer; the driver is an
idle seat; the fix mostly restates the game, which was never playtested. Mustache Madness: frame wrong
(it was multiplayer; "keep one of four" kept three, chained one way). Dungeon Pets: frame wrong (a new
game, inconsistent with the Assemblia call). Assemblia: holds (don't fix).

## Synthesis (round 1)
Rule applied to all: **if the formula removes what the game is, don't fix it; that's a new game.**
All "Broke" lines are Claude's reading [opinion] unless a user verdict is quoted.
- **Don't fix:** Assemblia (emergence from rules was its identity), Dungeon Pets (single-player pack
  management was its identity; a co-op class crawler is a new game), Mustache Madness (the four-genre mix
  was its identity; it was already multiplayer).
- **Red Button: don't fix.** Its shared money already existed. No coupling through one button found
  that passes the co-op gate for 2–8 players without mashing or a quarterback. Too small for the formula.
- **Pet the Cat: bring to the user.** A fix depends on why they disliked it. Their own words stay
  (no narrator, no shop, keep petting, parkour and floor-is-lava minigames).
- **Hordeline:** a fact first: it was never playtested, and the furnace and junction levers already
  exist, so there's no evidence its couplings failed. Fix: drop the Vampire Survivors upgrade layer
  (the user's own reason) and remove the driver seat. Then playtest what exists. Only if the playtest
  shows no player coupling, try one: the last carriage can be uncoupled to shed boarders. Whoever is at
  the coupling decides when; whoever is in the back decides whether to run forward; dropping a friend
  is visible.
- **Deathly Reality Show:** one coupling for the whole show, with fewer rules per game. Candidate: **one
  chain through every living contestant** (not pairs). Courses use the stage's dropping tiles, so standing
  still kills: nobody can anchor. When a contestant dies, the Reaper cuts them out and joins their two
  neighbours. The dead keep their ghost role. Position on the chain sets roles (the ends lead, the middle
  is pulled both ways). Test it on The Tilt's course first; leave Bomb Relay's rounds alone. Tech risk:
  chain physics on a player-hosted game.

## Critic round 2 (summary)
Don't-fix calls fair, but Red Button's reason was wrong (the checked reason: the user superseded it,
2026-11-07: "replace the button but with a cat"), and the rule needs "unless the user's own drop
reason is the part removed" (Hordeline). Hordeline: frame wrong as a plan (without the upgrade layer only
1 weapon is left, the chores are solo hold-E jobs that fail gates 1 and 7 on paper, there are no bots,
and uncoupling a carriage has no stakes because fallen players respawn on board). DRS chain: frame
wrong (Bomb Relay is games 1 and 3; anchoring is The Tilt's win action; chain + keys = stacked rules;
the middle of the chain is passive).

## Synthesis (round 2): verdicts for the user, no new sketches
- Rule: if the formula removes what the game is, don't fix it, unless the part removed is the user's
  own reason for dropping it.
- Red Button: don't fix; the user already replaced it with Pet the Cat.
- Hordeline: removing the upgrade layer leaves no game; a fix is a new co-op core for the train, a
  design job of its own. Recommend: don't fix unless the user wants a train game.
- DRS: the chain clashes with the current games. The user's choice: a chain show (replace the games
  with plain courses) or keep Bomb Relay + The Tilt and judge them at the playtest. Recommend keeping them.
- Pet the Cat: still needs the user's reason for dropping it.

## Mustache Madness, low scope and low coupling (user asked, 2026-11-09)
Its MEMORY.md pillars raise coupling on purpose ("Add connections, not things"; "Synergy comes from
independent axes sharing one space or pool"; creatures pass gems to each other; roles emerge from
raising; an exponentially growing city). A low-coupling version keeps the tone ("a Looney-Tunes goofy
tower-defense farm", a hard gate), the creatures, the night sieges and multiplayer; it drops the
economy, gems, city, farming, tech and crafting.

### Thesis (Claude, round 1)
- A round = one night (~3 min). It starts at dusk with the herd scattered over the farm; monsters come
  to grab creatures; at dawn, every creature inside the barn survives and breeds (the herd grows, so the
  next night there is more to carry). Lose: the herd is gone.
- Hub: the herd, the team's only value. Players carry creatures to the barn.
- Player coupling: small creatures need 1 carrier, big ones 2, huge ones 3. Carriers must lift and walk
  together; if one lets go, it drops, and a monster can grab it. Big creatures wander farthest, so the
  valuable ones are the riskiest (R.E.P.O.'s greedy run). A dropped or left-behind creature shows who did it.
- No towers, no farming, no shop. Content: one farm, 3 creature sizes, one monster type.

### Critic round 1 on the Mustache Madness sketch (summary)
SEVERE frame: it breaks MM's hard tone gate, "a Looney-Tunes goofy tower-defense farm" (no towers, no
farming, no defend verb), so it's a herd-rescue game, not MM. Other SEVERE: creature value undefined
(everyone carries smalls alone, which is parallel play); the barn is a safe end state (the night is won early);
huge creatures can't be saved at 2 players. MED: dropped pillars not named; who steers a joint carry; throwing
smalls is a solo machine; fixed barn = route memorised by run 2; monster vs player undefined; carrying
together has become Claude's default answer (newest idea as hub).

### Synthesis (round 1): frame to the user first (design-anti-patterns A4: frame before detail)
- The user's call: keep the tone gate by bringing back MM's throw as the defend verb (throwing stuns
  monsters; carriers have full hands, so they depend on throwers; anyone can switch), or reword the gate.
  Recommend keeping the gate with the throw.
- Pillars this version drops (for the user to confirm): roles emerge from raising; creatures hold gems;
  the city grows exponentially; add connections, not things; sacrifice through occupied shared state;
  a reward is a new rule, never a pile.
- Gate fixes ready if the frame holds: bigger creatures breed more at dawn (value by size); the barn isn't
  safe forever (monsters can break in, so someone guards it); sizes scale with the crew (the biggest needs
  all players but one); a joint carry moves by the sum of everyone's pull; only monsters can be thrown at,
  creatures can't be thrown; the barn door and the monsters' entry move each night. Critic round 2 runs
  after the user's frame call.

### User's verdict on the Mustache Madness sketch (2026-11-09)
"only carrying/throwing makes the game needing for more content for fun.. it is not like hide and seek..
which doesnt need much content". Carrying and throwing aren't enough on their own. Next: the verbs research
(`reports/Gameplay verbs and player coupling.md`), then a new sketch from its findings.
