# TODO: the creature black box

A design, not yet built. Each slice at the end gets its own `/design` pass before code.
"Lean" marks a recommendation; the user picks.

## Frame
The game is a funnel. The player does a few simple things. Each one changes the herd, and
the change escalates through the creatures. The strategy lives in how the creatures
develop, not in what the player's hands do.

The creatures are a black box (`MEMORY.md`). The inside may stay opaque. The interface
must read on sight, and the player acts on many creatures at once, never one at a time.

| Part | Meaning |
|---|---|
| Input | What the player does to the box |
| Dial | What the box gives back that the game runs on |
| Communication | The signs that tell the player the box's state. A sign is not a dial |
| The box | What has to change inside for the three above to work |

## The one idea: an offer
A placed thing makes an **offer** (rest, company, play, a meal, training, a kind of work)
to every creature in its reach. In its free time a creature picks one offer.

- **Input:** the player places things. No input names a creature.
- **Box:** the creature chooses among offers from what it already feels.
- **Dial:** how the herd feels changes what it delivers.
- **Communication:** the creature's body shows how it feels and what it could not find.

## What the code does today
| Area | Fact | Where |
|---|---|---|
| Choosing | A creature follows a fixed ladder: fight, then bed if wounded, then a food drop it targets, then a gathering it is in, then work or break if it has a job, then roam | `Creature._decide_mode` |
| Choosing | On break or roaming it may start or join a gathering; otherwise it wanders, drifting toward those it likes | `Creature._combat_tick`, `SteeringService` |
| Social | Creatures gather and act on each other (chat, joke, play, comfort, court, squabble, bully, embarrass). An action writes only mood, friendship, and love | `SocialAction`, `Gathering` |
| Social | Mood settles toward a centre set by health, number of friends, and the species' warmth. Meals, sleep, dawn, and grief shift it | `MoodComponent`, `CreatureConfig.EFFECTS` |
| Social | Nothing the player builds feeds the social system. It reads only who stands within 8 m | search of builds, machines, items, jobs |
| Output | Mood adds or removes up to 2 points on every stat, which changes fight numbers only | `StatsComponent.effective` |
| Output | Friendship is read by who gathers with whom and by how much a death hurts. A couple at full love lays an egg | `SocialCoordinator` |
| Work | Four jobs (chop, cook, study, research), all gated on smarts. A free site goes to a fit idle creature. A work stretch is 60 s and a break 30 s, leaned by the species' discipline | `JobBoard`, `JobComponent` |
| Signs | One status glyph per creature, by priority: baby, stunned, asleep, breeding, eating, groggy, grieving. A social action flashes a felt glyph. Mood has no lasting sign | `EmojiService`, `SocialCoordinator._flash_felt` |
| Signs | Mustache size and tint show earned stats (user decision, 2026-09-16) | `StatsComponent` |
| Signs | Herd counts show while TAB is held; one creature's stats show while aiming at it. The game has no sound | `ui/hud/`, search of the tree |
| Unused | Three training stations (strength, toughness, speed) are in the code and cannot be obtained. No weapon can be obtained | `stat_station.gd`, search of the tree |

Mood itself is server-only (it ticks after the client early-return in `CrowdBody.step`).
Clients see it only through the mustache step (slice 1).

So today the box works, but the player has no input into its social side and gets almost
nothing visible back from it.

## Prior art
| Game | What it teaches here | Source |
|---|---|---|
| The Sims | An object tells nearby sims what it offers and they choose. The player's input is placing objects | [Wikipedia](https://en.wikipedia.org/wiki/The_Sims_(video_game)), [lecture outline](https://users.cs.northwestern.edu/~forbus/c95-gd/lectures/The_Sims_Under_the_Hood_files/outline.htm) |
| Viva Pinata | Shape the garden; a creature arrives when it suits it, and stays when it suits it more | [Wikipedia](https://en.wikipedia.org/wiki/Viva_Pi%C3%B1ata_(video_game)) |
| Majesty | Heroes act by themselves and leave if they have nowhere to stay | [Wikipedia](https://en.wikipedia.org/wiki/Majesty:_The_Fantasy_Kingdom_Sim) |
| Dwarf Fortress | Strong dials with weak signs: one death can end a fortress and the player cannot tell why | [Tantrum](https://dwarffortresswiki.org/index.php/Tantrum) |
| RimWorld | The player sets conditions; the colonists' moods and bonds make the events | [GDC talk](https://gdcvault.com/play/1024232/-RimWorld-Contrarian-Ridiculous-and) |

## 1. Input
| # | Candidate | Verdict |
|---|---|---|
| a | **Every build is a place with offers.** A job site is a place that offers work | Lean. One kind of thing; a new build or job is one authored row |
| b | Rooms: a walled space typed by what stands in it | Later, on top of (a). Gives blocks a job in the box. The room must show its type |
| c | Painted zones and flags ("gather here") | Cut: a command, and a second way to say what a place already says |
| d | Reward or scold one creature | Cut: per creature |

Where the strategy is: a creature takes one offer at a time, and a place has a number of
seats. Places compete for the herd's free time; creatures compete for seats.

Catalogue to pick from (each is one row):
| Offer | Places | Feeds |
|---|---|---|
| Rest | Bed (exists) | Health, the rested mood |
| Company | Campfire, long table | Bonds, mood |
| Play | Toy, trampoline | Mood; bonds among whoever plays |
| Meal | Kitchen (exists); a shared trough the player fills | The meal mood, toughness |
| Training | Gym, treadmill, protein bar (in code) | Strength, speed, toughness |
| Learning | Library (exists) | Smarts |
| Work | Tree, kitchen, lab (exist); guard post, infirmary, forge, nursery | What the herd produces |

The new work gives a role to every body, not only the smart one: guard (strength), medic
who carries the downed to beds (speed), smith who makes weapons (strength), nanny for eggs
and babies (toughness). Each is close to the rejected "a station per action".

## 2. Dial
The box delivers four things: **work, fight, growth, staying**.

| # | Candidate | Reads | Delivers | Verdict |
|---|---|---|---|---|
| a | Stat bonus in a fight | Mood | Fight | Exists |
| b | **A happier creature works longer and rests shorter** | Mood | Work | Lean |
| c | A couple lays an egg | Love | Growth | Exists |
| d | **A friend carries a downed friend to a bed** | Friendship | Fight, staying | Lean |
| e | A friendless, miserable creature packs up and leaves | Mood, friendship | Staying | User's call. Needs a floor so one exit does not start a chain |
| f | Scenes at mood extremes: a tantrum that kicks a block over, a burst of double work | Mood | Work | User's call. By a chance that grows with mood, never a fixed line |

With (b) and (d), each of the three social values has a visible job.

## 3. Communication
The player must be able to answer four things by looking, and nothing more.

| Moment | Question | Sign | Today |
|---|---|---|---|
| Now | "Did my input land?" | Creatures in reach turn toward a new place. The ghost shows its reach before placing | Missing |
| Always | "How are they doing?" | **The mustache droops or perks with mood.** Friends keep together | Mood: missing. Packs: in the steering code, unmeasured in play |
| At a change | "What did that?" | One glyph flashes when mood moves: ate, rested, grief, a social act | Exists |
| When stuck | "What do they lack?" | The turned-away bubble: `💭` and the glyph of the place it would pick, shown while that place is full and it roams | Built |

Never shown: numbers, and how the box works. The right-click panel keeps them for whoever
wants to look; it is not needed to play.

| # | Level | Verdict |
|---|---|---|
| a | Body language only | Cut: the player cannot tell why |
| b | **Body language, plus the cause at the moment of change** | Lean |
| c | Bars and numbers per creature | Cut: granular |

Herd-level signs come from the same pieces: a field of droopy mustaches, a crowd at one
fire, many of the same bubble.

## 4. The box
| # | Candidate | Verdict |
|---|---|---|
| a | No change: the fixed ladder | Cut: with more places every idle creature does the same thing, so more builds change nothing |
| b | Needs that drain over time (hunger, fun, rest, company) | Tried as two stored needs, then dropped (see Needs: superseded) |
| c | **A chooser on the free-time rung, reading values the box already holds** | Lean |
| d | A rare wish from one creature, a gift if granted | Later: per creature, but rare and optional |

The chooser stays: on break or roaming, a creature scores the places in reach and picks
one; fight, bed, and food stay above it on the ladder. What each place offers is set by
`docs/TODO_object_catalogue.md`.

## Spec

### Data
| Variable | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| offer | row: kind, reach in metres, seats, effect | Place (authored) | What a place gives and to how many | Static |
| seats taken | int 0 to seats | Place (server) | Creatures using it now | Up on arrive, down on leave |
| need | float 0 to 1, per offer kind | Creature, stored | See Needs | See Needs |
| pull | float >= 0 | Computed per creature and offer | `need x lean x nearness`; zero when no seat is free | Not stored |
| chosen offer | place or none | Creature (server) | Where it spends this stretch of free time | Set by the chooser; cleared by a higher rung or when the stretch ends |
| unmet kind | offer kind or none | Computed | The kind with the highest need and no pull in reach | Drives the bubble |
| mustache angle | degrees | Creature view | Sign of mood | Recomputed; stores nothing |
| mood, friendship, love | exist | Creature | Unchanged | Unchanged |

`lean = 1 + g x axis`, with the one gain the personality code already uses
(`PERSONALITY_GAIN`, 0.5). `nearness = 1 - distance / reach`, floored at 0.

### Pipeline
| Stage | Reads | Writes | Passes on |
|---|---|---|---|
| Place | The player's click | A place with its offer | Reach, seats |
| Acknowledge | New place, creatures in reach | A head turn | The "now" sign |
| Choose (new) | Offers in reach, need, temper, seats | Chosen offer, seats taken | Where creatures are |
| Use | Chosen offer | The offer's effect: a mood lift, a stat gain, work done | The three values, outputs |
| Social (unchanged) | Who is near | Mood, friendship, love | The three values |
| Deliver | Mood, friendship, love | Work pace, fight bonus, eggs, rescues | The dial |
| Show | Mood, bonds, unmet kind | Mustache, packs, glyph, bubble | The other signs |

No stage reads a value nothing writes.

### What moves what
Row affects column. `0` = no effect.
| | Chooser | Work | Fight | Growth | Signs |
|---|---|---|---|---|---|
| Mood | Play pull | Pace | Stat bonus | 0 | Mustache |
| Friendship | Company pull | 0 | Rescues | 0 | Packs |
| Love | 0 | 0 | 0 | Eggs | The egg |
| Temper | Leans every pull | Stretch length | 0 | 0 | 0 |
| Seats | Zeroes a full place | Workers per site | 0 | A free bed for an egg | Crowds |

### Charts
Work and break with mood added to the existing lean (mood as a fraction, -1 to 1):
`work = 60 s x (1 + g x (discipline + mood))`, `break = 30 s x (1 - g x (discipline + mood))`
| Discipline + mood | -1 | 0 | 1 | 1.5 |
|---|---|---|---|---|
| Work | 30 s | 60 s | 90 s | 105 s |
| Break | 45 s | 30 s | 15 s | 7.5 s |

The break reaches zero at a sum of 2, so it needs a floor.

Mustache: `angle = lerp(-DROOP_MAX, PERK_MAX, (mood + 5) / 10)`
| Mood | -5 | 0 | 5 |
|---|---|---|---|
| Position | Full droop | Flat | Full perk |

Harm moves only the centre (health), so mood follows a wound at the decay pace.

### Loop checks
| Loop | Start | End | Floor |
|---|---|---|---|
| Company place, bonds, more friends, less company pull | A friendless creature has the highest pull | The pull falls as friends grow | Strangers still go |
| Meal, mood, longer work, more meals | A cook and crops | The meal mood stacks once | A sad cook still works 30 s stretches |
| Death, grief, lower mood, slower work and weaker fight, more deaths | A death | Grief fades over 3 days | Open: stacked grief is unmeasured. Play and company pull rise as mood falls, which pushes back |

### Constants
| Constant | Kind | Note |
|---|---|---|
| Offer reach, per kind | Limit | New |
| Seats, per place | Limit | New |
| Offer effect rows | Weight and lifetime | New mood rows, authored |
| `PERSONALITY_GAIN` | Weight | Exists; reused for every lean |
| Break floor | Limit | New |
| `DROOP_MAX`, `PERK_MAX` | Limit | New, art |

## Offers + chooser: decided (user, 2026-10-07), built AFK
The user picked offers + a chooser. Words the player sees: a **place** offers something to
the creatures near it; each creature's **chooser** (how it spends free time) scores every
place in reach and walks to the best one.
Every need value, pull, and loop row below (and in Spec above) that reads belonging or
`TRAIN_NEED` is superseded by `docs/TODO_object_catalogue.md`.

### AFK decision log (audit these)
| Gate | Resolved as | Why |
|---|---|---|
| Work as an offer (A2) or jobs stay on the board (A1) | A1 for now: the board keeps work; places fill free time (break and roam). A2 is the next slice | Whether creatures pick work often enough is a tuning question (work need vs `ROAM_PULL` and `TRAIN_NEED`) that needs a playtest of A1 first; the board's "most disciplined gets the site" rule works today |
| Throw aim | The throw follows the look: `angle = clamp(pitch + 15, -30, 80)` degrees | User request mid-AFK |
| Company need | `1 - clamp(belonging, 0, 1)`: a creature with no friends is the loneliest (was `(1 - belonging) / 2`, which gave it 0.5, the same as training, so the fire never won) | Measured in the headless sim (SIM_PLACES=1): fire users 0 before, 1 to 3 after |
| Hangouts never started in real play | Three fixes: (1) an approach to a partner holds until arrival (roaming or standing used to undo it between social beats); (2) `MOOD_NORMAL` 2.5 to 1.25, the resting mood of a healthy friendless creature, so an ordinary creature's invite is a fair roll; (3) sitting at a campfire gives a cozy mood lift once per stay | Measured, same 200 s run: chats 1 to 23, hangouts formed 2 to 15, herd belonging -0.02 to +0.05. Without bonds, rescue and guard never fire. Balance probe on a human playtest should confirm |
| Catalogue | Campfire (company) and three training places (gym STR, protein VIT, treadmill DEX) | Each grows a different axis the roles read: bonds (rescue, guard), VIT (guard), STR and DEX (fight). Toy cut: same purpose as the campfire (bonds and mood through hangouts). Nursery and watchtower wait for the user: new nouns |
| The old training stations | Removed: they trained everyone in range with no choice (candidate D, cut) | The training places replace them through the chooser |
| What a campfire does | Nothing of its own: it gathers creatures, and the existing hangouts make the bonds | Adds a connection, not a new effect |
| How a place is had | Campfire: a basic (5 wood) in the R menu. Training places: found by lab research, paid in gems | "More things in the shop": the build menu is the shop |
| Doing nothing | Roam scores a flat pull; a place must beat it | Flighty creatures still wander instead of training |

### Data
| Variable | Type, range | Owner | Meaning | Lifecycle |
|---|---|---|---|---|
| kind | COMPANY or TRAIN | Place (authored) | What it offers | Static |
| stat | STR, VIT, DEX | Place (authored, TRAIN only) | Which stat it trains | Static |
| seats | int | Place (authored) | How many can use it | Static |
| users | creatures | Place (server) | Who holds a seat now | Taken on choosing, freed on leaving or at the stretch end |
| need | 0..1 | Computed | COMPANY: `1 - clamp(belonging, 0, 1)`; TRAIN: `TRAIN_NEED`. Superseded by `docs/TODO_object_catalogue.md` | Not stored |
| lean | 0.5..1.5 | Computed | `1 + PERSONALITY_GAIN * axis`: sociability for COMPANY, discipline for TRAIN | Not stored |
| near | 0..1 | Computed | `1 - distance / OFFER_REACH` | Not stored |
| pull | >= 0 | Computed | `need * lean * near`; 0 when no seat is free | Not stored |
| chosen place, stretch | place, timer | Creature (server) | Where it spends this stretch | Set on choosing; cleared by a higher rung or after `OFFER_STRETCH_SEC` |

### Pipeline
| Stage | Reads | Writes |
|---|---|---|
| Place | The player's build | A place in the group of places |
| Choose | Free creature (no fight, bed, rescue, follow, food, hangout, work shift): pulls of places in reach, `ROAM_PULL` | Chosen place, a seat |
| Use | Chosen place | COMPANY: stands there, gets the cozy lift once per stay, and the hangout system runs; TRAIN: the place grows its stat each `TRAIN_INTERVAL` |
| Leave | A higher rung, or the stretch ends | Seat freed; the next free stretch chooses again |
| Show | Chosen place | 🔥 or 💪 glyph |

### Charts
| | Low | Mid | High |
|---|---|---|---|
| COMPANY pull at the fire, outgoing (+1), beside it | belonging 1: 0 | belonging 0.5: 0.75 | belonging <= 0: 1.5 |
| TRAIN pull at the gym, by discipline | -1: 0.25 (ties roam: wanders) | 0: 0.5 | +1: 0.75 |

### Constants
| Constant | Kind | Value |
|---|---|---|
| OFFER_REACH | Limit | 20 m |
| OFFER_STRETCH_SEC | Pace | 30 s dilated, a break's length |
| ROAM_PULL | Weight of doing nothing | 0.3 |
| TRAIN_NEED | Weight | 0.5 |
| Seats | Limit, per place | Campfire 4, training 2 |
| TRAIN_RATE, TRAIN_INTERVAL, OFFER_USE_RADIUS | Pace, limit | 0.3 XP/s, 1 s, 2.5 m |
| cozy moodlet | Weight, lifetime | +1.5 mood for 0.3 days |

### Loop checks
| Loop | Start | End | Floor |
|---|---|---|---|
| Fire, hangouts, bonds, belonging up, company pull down | A lonely creature pulls hardest | Pull falls as friends grow | Bonds decay, so the fire stays useful |
| Bonds, belonging, mood centre, accept chance, more bonds | The resting mood is `MOOD_NORMAL`, so a stranger's invite lands about half the time; the fire's cozy lift helps | Belonging saturates at 3 best friends | A refused invite stings; measured belonging still climbs |
| Training, stat up, nothing reads it back into pull | Discipline | The stretch | No runaway |

## Needs: superseded
The stored-needs design (company and restlessness meters) was dropped on 2026-10-08: the
meters only copied the work schedule, one personality axis cancelled itself, and an unmet
need cost nothing. Its replacement is `docs/TODO_object_catalogue.md`.

## Slices
- [x] **1: the mood sign.** The mustache tips curl up with good mood and droop with bad
  mood: a per-instance `curl` bend in the toon shader (`VERTEX.y += curl * x^2`, mesh
  local Y is world up on all three species, measured). Reads live mood, the value the
  fight bonus reads. Replicated as a step (`View/Body:mood_step`, 1/10 of full mood).
  Cheats: `F5` happy, `F3` sad (mood settles back within seconds).
- [x] **2: the chooser, the campfire, and three training places.** Cheat: F8 places them
  beside you.
- [ ] **2b: work as an offer (A2):** moved to `docs/TODO_object_catalogue.md` (rule 4).
- [x] **2c: the "did it land?" sign.** A new place flashes its glyph over every creature it
  will draw (a flash, not a head turn: the walk would override a turn at once).
- [x] **3: mood leans work pace.** `drive = clamp(discipline + mood lean, -1, 1.5)`; work
  `60 s x (1 + 0.5 drive)` (30 to 105 s), break `30 s x (1 - 0.5 drive)` (45 to 7.5 s). Mood
  lean is `(mood - MOOD_NORMAL) / MOOD_MAX`, the one the social rolls use.
- [x] **4: the turned-away bubble.** A creature whose best place (by draw, spots aside) is
  full shows `💭` and that place's glyph while it roams. It reports contention for spots,
  never a need: no place built, no bubble. The chooser, the bubble, and the "did it land?"
  flash share one scorer (`OfferPlace.best_for`); the flash now fires only over creatures
  the new place becomes the best pick for.
- [x] **5: friends rescue friends.** A rule for every creature (`docs/TODO_emergent_roles.md`).
- [ ] **6: the catalogue:** moved to `docs/TODO_object_catalogue.md`.
- **7: needs.** Dropped, never built; see Needs: superseded.

## Open calls (user)
| # | Call | Lean |
|---|---|---|
| 1 | Offers plus a chooser as the structure | Yes |
| 2 | Which places and jobs from the catalogue | - |
| 3 | A couple needs a free bed to lay an egg, so beds are the handle on growth | Yes |
| 4 | The mustache reads live mood or the mood centre | AFK-resolved: live. The sign reports what the fight bonus reads; harm lowers mood only through health in the centre (no per-hit drop, user); mood moves at an even pace (linear, +5 to normal in ~60 s, user). Measured spread (16 captures): 5th to 95th percentile 0.5 to 4.5, so the mustache mostly curls up and a droop is rare and means something. Species sets most of the spread (bunny ~3, fox ~1.7, frog ~0.7) |
| 5 | The job panel | A readout only; jobs come from sites |
| 6 | Creatures that leave when friendless and miserable | - |
| 7 | Scenes at mood extremes | - |
| 8 | Sound as a herd sign | Yes |
| 9 | Pillars "ban hidden effects" and "if the player can't see the link, it is illegal": read as the effect must surface, the mechanism need not | Yes |

## Parked
Ideas and findings from earlier passes, kept so they are not lost.
- **Diet builds the body:** one crop feeds one stat, one meal a day. Today stats also grow
  by themselves, so feeding barely steers a body.
- **Inheritance:** a baby starts from a share of its parents' earned stats. Today it takes
  nothing.
- **A weapon source:** wave elites that drop what they carry.
- **The clock:** night 1 lasts 7.5 s and a downed body lasts 45 s, longer than the whole
  first day and night (28 s). No choice made during a fight can cost a body. The social
  tuning (grief for 3 days, a pair familiar in about 15 minutes) was sized for a longer day.
- **The throw:** a thrown creature lands and nothing happens. Wilds target friendlies
  before the statue, so a landing spot could pull a fight. The three species throw almost
  alike (weights 0.45, 0.5, 0.55).
