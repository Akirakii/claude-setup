# G1 formula batch 2: blind critic scores (2026-11-10)

Scored on F1–F7 and G from `../formula.md`; novelty not scored. Rules judged as written.
Consistency rules used: a route-shaped arena (course, cave, road, path) with no stated generation → F1 ~ and F7 ~;
F7 ✓ only for generated layouts/piles or a hidden human; hidden info with no one motivated to hide it → F6 ~;
a shared body steered by the sum of everyone's same input with all info public → F3 ✗ (pooled sum + quarterback);
no clock in the rule → G ~ (✗ if that also lets a set-up-then-wait strategy trivialise it); blame that needs a replay → F4 ~.

| ID | F1 | F2 | F3 | F4 | F5 | F6 | F7 | G | dominant strategy | why each ~ and ✗ (short) | same core as |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G101 | ✓ | ~ | ✗ | ✓ | ~ | ✓ | ✓ | ~ | each player steps 15 m out alone, memorises own lane, regroups to warm | F2 ~ traitor + cold + torch on top of tile rule; F3 ✗ walkers only obey the scout's calls (quarterback) and solo peeks bypass the scout; F5 ~ at 3 two walkers do one job, traitor only sometimes; G ~ no clock, a lone player sees every hole | — |
| G102 | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✓ | flocks parked apart, each pair hands over one straggler on a fixed rota | F3 ~ everyone has the same herding job, coupling is a fixed ring deal that becomes routine; F7 ~ one meadow, flocks only | — |
| G103 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | spread to separate logs, push only empty logs; key log still needs a two-sided push | — | G106 |
| G104 | ~ | ✓ | ~ | ✓ | ~ | ~ | ~ | ~ | freeze the chain, advance one mirror at a time; sun drift only touches mirror 1 | F1/F7 ~ cave route, generation unstated; F3 ~ middle relays hold still (pressure plates); F5 ~ at 6 middle seats near idle; F6 ~ dark ahead, no one hides it; G ~ no clock, caterpillar removes pressure | G146, G136 |
| G105 | ✓ | ~ | ~ | ✓ | ✓ | n/a | ✓ | ✓ | crew clusters mid-deck; one runner does jobs, one partner steps opposite | F2 ~ three job rules (pole, grab, bail) on the tilt hub; F3 ~ steering is a pooled sum of positions, counter-stepping is reactive | G114, G128, G150 |
| G106 | ✓ | ✓ | ✗ | ✓ | ✓ | n/a | ~ | ~ | each player owns a wall section and pulls only there | F3 ✗ everyone pulls and throws side by side, friends are only a hazard (parallel play); F7 ~ same wall and archers each round; G ~ one good thrower can carry | G103 |
| G107 | ~ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✓ | cab takes slow wide lines, brake rides early, trailers just follow | F1/F7 ~ road not stated generated; F3 ~ one-way follow chain, trailers obey the cab's line | G138 |
| G108 | ~ | ~ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | cross one at a time while the rest freeze for the crosser | F1 ~ trap course is level content, generation unstated; F2 ~ up to 6 trap kinds, each a rule on the hub; F7 ~ fixed courses | — |
| G109 | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ~ | ✓ | upward bucket brigade, never stomp | F6 ~ rooms hidden, no one motivated to hide; F7 ~ one house, only item placement varies | G110, G168 |
| G110 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | park tools evenly along the line, pass toward each alarm | F7 ~ one tunnel, random problem spawns only | G109, G168 |
| G111 | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✗ | swinger pre-lays a full row of stones along the arc (stones sink only once stepped on), then walkers walk | F3 ~ walkers wait on the swinger; F7 ~ one lake, arc only; G ✗ no clock, so pre-laying makes it build-then-walk | G124 |
| G112 | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ~ | ~ | walk as a tight blob so each sees the body they drive | F6 ~ no motive to hide; F7 ~ beach not generated, novelty is only the control swap; G ~ blob cuts the need to describe surroundings | G120 |
| G114 | ✓ | ✓ | ✗ | ✓ | ~ | ✓ | ✓ | ~ | one caller reads all edge heights and directs dips | F3 ✗ ball follows a pooled height sum, everyone same job, full info → quarterback; F5 ~ "best from 4", traitor exposed at 3; G ~ no clock | G105, G128, G150 |
| G116 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | cutter leaves big gaps, only the shift clock limits it | F7 ~ one yard, random car order (solved by run 2 risk) | — |
| G118 | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✓ | fixed formation per storm kind; non-immune players just tuck in | F3 ~ sheltered players only obey, at 3 the answer is forced; F7 ~ one flat, random storm order | G160 |
| G120 | ~ | ✓ | ✓ | ~ | ✓ | ~ | ~ | ✓ | tight circle so every borrowed view shows everyone | F1/F7 ~ temple route, generation unstated; F4 ~ blame needs a replay; F6 ~ no motive to hide | G112, G172 |
| G122 | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ✓ | ~ | fetchers stand still (steps eat floor), carriers walk straight on fresh tiles | F3 ~ fetchers mostly a hazard, carriers do one job; G ~ no clock, holes come only from own steps | — |
| G124 | ~ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ~ | one slimer walks a straight line just ahead, pushers follow | F1/F7 ~ garden route, generation unstated; F3 ~ pushers follow the slimer's path (obey); G ~ routine once learned | G111 |
| G126 | ✓ | ✓ | ✓ | ~ | ~ | ✓ | ✓ | ~ | deduce the haunt (fast at 3), then one player stares at them for good | F4 ~ sabotage unseen by design, blame via beam record; F5 ~ at 3 one sabotage narrows it to one; G ~ no elimination, a permanent watcher locks the haunt | — |
| G128 | ~ | ✓ | ✗ | ~ | ✓ | n/a | ~ | ✓ | one caller reads every push arrow and sequences the sails | F1/F7 ~ reef, generation unstated; F3 ✗ pooled push sum, same trim job, full info → quarterback; F4 ~ pooled steer blurs who should have countered | G105, G114, G150 |
| G130 | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | swap the bottom on a fixed timer | F1/F7 ~ lava field route, generation unstated; stack physics only | G142 |
| G132 | ✓ | ~ | ✓ | ✓ | ✓ | ~ | ~ | ✓ | pairs watch each other and shout colours; balloons rarely used | F2 ~ beams + balloons + mirrors + carts; F6 ~ no motive to hide; F7 ~ one floor, random beams | G172 |
| G134 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | ~ | one loud decoy (hot mic or soundboard) kites, everyone else stays silent | G ~ mic hardware or a soundboard lets one decoy carry, and silence cuts talk | G164 |
| G136 | ~ | ✓ | ✗ | ✓ | ✓ | n/a | ~ | ~ | fixed chute and pace → each finds a fixed station and angle, then holds still | F1/F7 ~ course, generation unstated; F3 ✗ static stations become pressure plates; G ~ talk stops after setup | G104, G146 |
| G138 | ✓ | ✓ | ✗ | ✓ | ~ | n/a | ~ | ~ | conga line one step behind the previous cleaner; only the first decides | F3 ✗ one-way chain, followers only follow; F5 ~ late seats wait; F7 ~ fixed manor; G ~ conga needs no talk | G107 |
| G140 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | sacrifice one player to the cage all night, never kick the can (that rule goes dead) | F7 ~ one yard, troll AI only | — |
| G142 | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✓ | climb slowly, bases counter-lean; the same build every round | F3 ~ bases and middles mostly react or hold (lean is a pooled sway); F7 ~ one build repeated with new heights | G130 |
| G144 | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | fixed leapfrog order | F1/F7 ~ ruins route, generation unstated | — |
| G146 | ~ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ✓ | fixed chain, only mirror 1 tracks the sun; creature dodges force re-routes | F1/F7 ~ canyon, generation unstated; F3 ~ middle relays mostly hold still | G104, G136 |
| G148 | ~ | ✓ | ~ | ✓ | ~ | n/a | ~ | ✓ | strict spoken turn queue for the battery | F1/F7 ~ cave, generation unstated; F3 ~ mutex turn-taking is mostly waiting; F5 ~ at 6, five of six gadgets dark at any moment | — |
| G150 | ~ | ✓ | ✗ | ✓ | ✓ | n/a | ~ | ✓ | one caller watching the whole street calls slack and pull | F1/F7 ~ street, generation unstated; F3 ✗ pooled pull sum, same rope job, full info → quarterback | G105, G114, G128 |
| G152 | ✓ | ✓ | ~ | ✓ | ~ | n/a | ~ | ✓ | holders stand still, flyer steers back onto the blanket | F3 ~ holders are one pooled body, can become pressure plates; F5 ~ at 6 five holders do one job; F7 ~ fixed forest | — |
| G154 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ✓ | fixed alternating rhythm, holder slides on the beat | F7 ~ ≤20 shapes in one smithy, learnable | — |
| G156 | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ~ | bell dog leads the flock like a pied piper, stare dog guards the edge, barker idles | F1/F7 ~ cliff path, generation unstated; G ~ bell dog may carry | — |
| G158 | ✓ | ~ | ~ | ✓ | ✓ | ✓ | ~ | ✓ | each carrier takes a fixed lane and calls once | F2 ~ fly bar + wagon + torch + applause on the hub; F3 ~ carriers do one job side by side; F7 ~ one stage, shuffled marks | — |
| G160 | ~ | ✓ | ~ | ✓ | ✓ | n/a | ~ | ~ | hop building shadows; carried shade only bridges gaps | F1/F7 ~ town, generation unstated; F3 ~ follow-the-leader convoy; G ~ building shadows may let one player solo | G118 |
| G162 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | ✓ | none found; settle into a fixed swing rhythm | — (note: ms timing on a host connection, anti-pattern #16) | G166 |
| G164 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | ~ | decoy mashes noise right after every hammer blow, horde never reaches the worker | G ~ a mashing decoy kites alone (anti-pattern #18) | G134 |
| G166 | ✓ | ✓ | ✓ | ~ | ✓ | n/a | ~ | ✓ | fixed leapfrog rhythm | F4 ~ needs a replay to split early release from late swing; F7 ~ bars not generated | G162 |
| G168 | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ~ | ~ | fixed assembly line in the commonest tool order | F7 ~ ≤20 recipes, solved by run 2; G ~ no clock in the rule | G109, G110 |
| G170 | ✓ | ✓ | ✓ | ✓ | ~ | n/a | ~ | ✓ | chase boats herd the school into a slow wide circle; winch waits for one press | F5 ~ at 3 the winch seat mostly waits; F7 ~ one sea, flocks only | — |
| G172 | ~ | ✓ | ✓ | ✓ | ✓ | ~ | ~ | ~ | back-to-back turtle facing out, fixed coverage | F1/F7 ~ cave, generation unstated; F6 ~ no motive to hide (idea says so); G ~ at 6 a turtle covers every side | G120, G132 |

Pass (no ✗): 34 of 42. Fail: G101, G106, G111, G114, G128, G136, G138, G150. Strict (all ✓/n/a): G103, G162.

## Patterns
- **Pooled steering is the top killer.** A shared body steered by the sum of everyone's same input (sheet, sails, balloon; raft only scraped by with distinct jobs) gives one pooled sum, and because every height, arrow and rope is public, one caller quarterbacks it.
- **Set-up-then-wait.** When the threat is a fixed stream or a fixed path (marble chute, wax arc, mess chain, mirror chain), players find fixed stations once and then hold still: pressure plates. One-way chains (road train, mess chain, sunbeam) let the back of the line only follow.
- **F7 is the batch-wide weak spot.** Most ideas run on a route-shaped arena (cave, road, path, course) with no stated generation, so round 50 is round 2. Only generated piles/layouts (log jam, piers, rivers, scrapyard) or a hidden human earned ✓.
- **Self-blind info splits cap F6 at ~.** "You can't see your own X, friends can" (eyes, lamps, paint, rooms) uncovers by asking, but nobody has a motive to hide, and a tight blob or turtle often dissolves the split.
- **What the best share (G103, G162, then G109, G110, G116, G154, G140):** two different verbs that must meet in the same instant (two-sided key-log push, release + catch, hammer commit + bar slide, knock + catch), a physical clock (water, music, cooling metal), and a culprit standing at the spot when it fails.
