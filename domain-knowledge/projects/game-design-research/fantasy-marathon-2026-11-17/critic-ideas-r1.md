# Critic round 1 on the five fantasy-marathon ideas (2026-11-17)

Isolated critic, standing in for the user.
Verdict in one line: none of the five passes as written; two are worth a rework, three should be dropped.
Tags: (searched) = one of my 10 web searches; (paper) = played in my head, not run; (memory) = not searched.
Every scene result below is (paper).
Pass or fail only.

## 1. Dragon's Hoard

**Base: fail.** The best move in a game sold on voice is to stop talking, and nothing in the rules stops the crew from simply waiting for the dragon to fall back asleep.

Played scene (paper).
- 3 players: Ana and Ben lift the crown, Cy pockets coins. Ben kicks a goblet, the eye opens halfway. All three stand still for 40 seconds, the eye closes, they go on. Nobody loses anything by waiting.
- 6 players: three pairs carry at once, so the one shared meter fills three times as fast and nobody can tell whose step tipped it. The crew answers by sending one pair at a time; four players stand and watch.
- 1 human + bots: the bot partner carries without a word, so the "words are noise" cost is gone. The human pockets coins or carries in silence; there is no choice left to judge.

What each role gains and pays.
- Carriers: gain the order's piece, pay with risk of fire. They act.
- Pocketer (Cy): gains safe coins the order also needs. No cost, so the scene's "debt grows" complaint about Cy is false while the order asks for a sum in small loot.
- Cart holder (Dee): gains nothing, does nothing. Idle seat.

Best plan by night 5: one pair moves at a time, everyone freezes whenever the eye opens, and someone throws a goblet into a far corner just before the eye fills so the fire lands on nothing.
Best plan by night 20: the same, with soft shoes. The choice has one answer.

Co-op check: 1 coupled pass (two-person carry) · 2 split fail (no split information) · 3 talk fail (pressure makes people stop speaking) · 4 blame pass (rings) · 5 not easy fail (waiting is free) · 6 not solo fail (drag, wait, drag) · 7 two-way pass for the carry only · lone survivor pass (can drag and wait) · dying on purpose pass.

Findings.
- **Severe: no clock.** Quiet drains the dragon and nothing else gets worse, so "freeze until the eye closes" beats every other move. Example: the 40-second stand-still above. Fix direction: something must get worse while the crew is quiet (checks.md 0.1), built into the dragon rule, not bolted on.
- **Severe: the fire goes to the last loud noise.** That is the banned "threat hunts whoever did the most recent X", and its one-line answer is the banned decoy noise (checks.md 4.5). Example: the thrown goblet. Fix direction: the dragon searches, or aims at something a throw cannot fake.
- **Severe: the core is built on silence.** This repeats "silence assumed online" (caught 3 times) and "a voice-only game tested with bots" (caught 6 times). The file says "nobody speaks" fails the two-person carry; it does not, because R.E.P.O. crews carry by watching each other's bodies (memory). Example: by night 5 the crew carries with crouch signals and the voice channel is dead. Fix direction: talking must be needed and paid for, not just punished.
- **Severe: greed has no rule.** The order names the pieces and the sum, so the amount to take is given and "one more goblet" never comes up. Clank! is a competitive game where the extra goblet beats a rival, so it does not back greed in a shared-pay crew (memory for Clank!'s rules). Fix direction: a reason to take more than the order that the crew can argue about.
- Medium: the wakefulness meter is one pile everyone adds to ("a pooled sum counted as coupling", caught 3 times).
- Medium: what the fire does to a burglar is not written. If it kills, a dead burglar's voice is free and they direct the living.
- Medium: two-person physics carry needs both players to move in the same half second; checks.md marks that lag case "~", which is a fail.
- Minor: the theme is not new. Golden Hoard and Dragon's Hoard (tabletop), and Draculae and Hoard Hunter (itch.io) all steal from a sleeping dragon with noise (searched). No Steam co-op game with it was found in two searches.

Carried rules: none of the three families. It is the Lethal Company and R.E.P.O. loop with a noise meter.
Minigame or game: pass, the order, debt and shop are a real layer between nights.
Scope: pass for the smallest version in days (one cave, a meter, rings, mic loudness). Costliest part: netcode for the two-person carry.

## 2. Low Tide

**Base: fail.** Everyone on the crew wants the same thing and can see the same water, so "leave or wait" is a sum the crew does together, and the premise shipped five months ago.

Played scene (paper).
- 3 players: Ana in the hold, Ben on deck, Cy bailing. Ana says "ten seconds". Cy looks at the boat, says "fine". Nobody is torn, because Cy's interest and Ana's are the same.
- 6 players: two bail, so the boat never fills and waiting costs nothing. Four loot side by side, each alone.
- 1 human + bots: the bot at the boat leaves by a rule. The human learns the rule on night 1 and times the swim to it.

What each role gains and pays.
- Diver: gains the listed piece, pays with the risk of being stranded. What being stranded costs is not written.
- Boat keeper: bails all night, a chore. The file says Cy "gains nothing by waiting except the bell", but the bell is the crew's whole goal.

Best plan by night 5: nobody stays at the boat, everyone calls their distance, the boat leaves at a fixed fill.
Best plan by night 20: the same fill line with a known water line per deck. One answer, moved only by the deal.

Co-op check: 1 coupled fail (looting and the swim are solo) · 2 split fail (everyone sees the same water) · 3 talk pass · 4 blame pass · 5 not easy fail (two bailers cancel the swell) · 6 not solo fail · 7 two-way fail (two ends, one interest, same facts) · lone survivor pass · dying on purpose: not written, so fail.

Findings.
- **Severe: one interest, so one answer.** The dropped idea Overloaded was cut because it "only bites when each friend owns their own haul" and with shared pay is "one waterline to agree on". Low Tide has shared pay and one waterline. The same reason was not run against it (CLAUDE.md rule 23). Fix direction: none inside co-op with open information; the file already found that.
- **Severe: the research row is misused.** "The agony of the one at the boat" cites Lethal Company's early-leave vote, which is cast by dead players who have nothing to lose. The file's own source lists it as a way to strand people, not as agony. Deep Sea Adventure backs greed only because each diver keeps their own treasure. Fix direction: mark both rows ❌ and search again.
- **Severe: the work is parallel.** Each diver loots alone and the keeper bails alone; that is "standing in places counted as co-op" (design-anti-patterns B24), the user's own complaint about Deathly Reality Show. Fix direction: a job in the wreck that fails without a second body.
- **Severe: the premise is taken.** Mudventure is 4-player online co-op where caves show at low tide and the crew must reach high ground before the water returns; trackers list it released in June 2026 (searched). The file calls it "near" and gives no verdict, while Mimic and Dead Weight were dropped for the same reason.
- Medium: steady rising water is a clock everyone reads ("a simple threat rule has a one-line answer", caught twice). Lethal Company's tension comes from monsters and a maze, which this leaves out.
- Medium: the goal is leaving the arena, and each night uncovers a deeper deck. Both fail "not a place to reach"; the decks are levels.
- Medium: bailing one boat is a small copy of "friends keep one shared thing going".
- Minor: every sourced feeling comes from one game.

Carried rules: fail, the bailed boat (see medium).
Minigame or game: pass on paper (debt, list, deeper decks), paid for with level content.
Scope: pass for days (a rising plane and boxes). Costliest part: flooded interiors with swimming, and one deck per night.

## 3. The Glasses

**Base: fail.** The file says so itself: one seat holds every call. Worse, the ghosts only move because someone wears the glasses, so the seer makes the danger.

Played scene (paper).
- 3 players: Ana wears, Ben guides, Cy is alone with a piano that needs two. Nothing can be carried. The idea does not run at 3.
- 6 players: Ana wears, Ben guides, four movers carry two pianos and wait for Ana's calls. Four players obey one voice.
- Any size, night 3: Ana stands in the doorway, far enough that the ghosts stay still, and points at each one. Each shows to everyone for a second. The movers remember them and walk around.
- Any size, night 5: someone lays the glasses on the floor in the far room. The ghosts drift to the glasses and stay. The house is clear.
- 1 human + bots: a human wearer is walked through grey fog by a bot. A human mover follows a bot's marks.

What each role gains and pays.
- Wearer: gains nothing, pays frost, sees fog, and is walked by someone else. The file says so. Nobody will want the seat.
- Guide: holds a hand. A partner who only stands in place.
- Movers: gain the piano, pay nothing, decide nothing.

Best plan by night 5 and night 20: wearer far away and pointing, or glasses on the floor as bait. The wearer's "stay close or walk away" has one answer: away.

Co-op check: 1 coupled pass · 2 split pass (the only idea with a real split) · 3 talk pass · 4 blame pass · 5 not easy fail (the bait) · 6 not solo pass · 7 two-way fail (movers obey; the file admits it) · lone survivor fail (cannot carry, cannot see both) · dying on purpose: full frost is not written, so fail.

Findings.
- **Severe: quarterback.** Caught 5 times before and listed in the file's own "Unproven", then shipped to the critic anyway (B25: a base problem set aside). Fix direction: every body sees something the others need, at the same moment.
- **Severe: the glasses cause the threat.** Ghosts stand still until the glasses are near, so the far-away wearer and the bait on the floor both end the danger. Fix direction: ghosts act on their own, and sight only reveals them.
- **Severe: the bot fix leaks the split.** "A pointed-at ghost shows to everyone" removes the trust the fantasy is about; it is "a fix that breaks its neighbours" and "a shared screen leaks the split information". Fix direction: do not patch a voice core for bots; pick a core that is physical from the start.
- **Severe: fails at 3 and with one survivor.** Wearer, guide and two movers is four bodies ("content that needs more than the fewest players").
- **Severe: The Blackout Club is misused.** Any player there can close their own eyes to see the monster, so it has no fixed seer and no "your left!" (Steam description, searched; the "any player" part is memory). The file turns its documented failure, jokes lowering the fear, into a ✅ "for comedy".
- Medium: the split is announced elsewhere. ByeByeObake! is a solo-developer online co-op game for 2 to 8 where an exorcist cannot see spirits and a companion who can must call them out; its Steam page went up on 9 October 2026 (searched). A second Steam page has one dead player who sees the demon and guides the living through a Ouija board (searched). The file found neither.
- Medium: frost is a harm meter passed from body to body with a swap at half. That is Moonsick's sickness under a new name.
- Medium: Keep Talking gives both sides a job at once (one reads, one acts on a bomb in hand). Here the movers hold no manual; they hold a piano.

Carried rules: fail, the frost meter (friends against a sickness).
Minigame or game: fail, "more ghosts, longer list" is the same night with bigger numbers.
Scope: pass for days without the piano. Costliest part: hand-leading plus a two-person piano carry over the network.

## 4. Echo Bats

**Base: fail.** The two feelings that make it a co-op game have no shipped game behind them, and the file's own night-5 plan is the decoy that the checks ban.

Played scene (paper).
- 3 players: each bat hunts alone and must squeak to see, so the owl's target changes every second. Whoever it hits was simply the last to squeak. Blame comes from luck.
- 3 players, night 5: Cy sits under a root and taps the squeak key without pause. The owl hovers over a bat it cannot reach. Ana and Ben hunt in the light of Cy's rings.
- Without a root: Ana and Ben squeak in turn from opposite ends, and the owl flies back and forth and never arrives.
- 6 players: six bats squeaking keep the whole cave lit. Nobody is lost in the dark, so the fantasy is gone.
- With mics: talking is squeaking, so a crew on voice chat lights the cave by chatting.
- 1 human + bots: works mechanically, and the bots squeak on a timer the human learns.

What each role gains and pays.
- Squeaker for a friend (Ben): gains nothing, takes the owl. He will do it once.
- The friend (Ana): receives light and decides nothing in return. The file calls every squeak "a gift", which means one end only receives.
- Hunter: can squeak for themselves, so no friend is needed.

Best plan by night 5 and night 20: one decoy under cover, or two bats taking turns. The file says a hunter's squeak pulls the owl off the decoy; the decoy just squeaks again.

Co-op check: 1 coupled fail · 2 split fail · 3 talk fail (talking is the cheat) · 4 blame fail (luck of timing) · 5 not easy fail · 6 not solo fail · 7 two-way fail · lone survivor pass · dying on purpose pass.

Findings.
- **Severe: the base has no precedent.** "Relief from a friend's squeak" and "a laugh that lights the cave" are marked ❌ by the file, and the two ✅ rows come from a single-player game and from monster-hears-mic horror. The skill says a feeling nobody built is a risk; Moonsick died of "premise with no precedent". Fix direction: drop, or find a shipped co-op game that causes the relief.
- **Severe: "dives at the most recent squeak" is the banned threat with the banned answer.** Toys was dropped because "the crew's plan is one decoy"; this idea states the same plan and stays in (rule 23). Fix direction: none with this owl rule.
- **Severe: the hunting is parallel and the help is one-way.** Moths go on a shared count, a pile. Fix direction: a catch that needs a second bat.
- **Severe: it breaks with size and with voice.** Dark at 3, lit at 6, lit whenever friends talk. Fix direction: none found.
- Medium: one player both needs and fears every squeak. Stifled makes that work alone; with friends the fear is handed to the decoy.
- Medium: wind, rain and a second owl are a content list added because the core does not change by itself.
- Minor: a multiplayer game already uses the name "Echo Bats", and "Echo" on itch.io is a two-bat co-op thorn maze with echolocation (searched). The Echolocation Killer and The Warden are unreleased versus games with sound-sight (searched).

Carried rules: pass, none.
Minigame or game: fail, one verb and a count.
Scope: fail. Flying in the dark, readable and synced, is months of feel work before the rule can be judged; the file's own fallback is to put it on foot.

## 5. Last Round

**Base: fail.** The drunk is asked to want to get home and to want the kebab, the only game behind the feelings is one where the two sides are enemies, and the rules are Pet the Cat with a person as the cat.

Played scene (paper).
- 3 players: Dee is drunk. She sees a taxi and asks on voice "is that real?". Ana says "police". Dee walks on. The hidden danger is undone by one question, and the drunk obeys.
- 3 players, night 5: Dee lets her urge meter fill at the start and sits down. Ana and Ben carry her home at a known speed, past every temptation, because a passed-out drunk wants nothing.
- 6 players: one drunk, five escorts. Two hold her arms and three walk beside them.
- 1 human + bots: with a bot drunk it is a solo escort mission. With a human drunk the bots drag by a rule. Mischief cannot be tested either way.

What each role gains and pays.
- Drunk: gains "fun" only by making her own crew lose. If she wants the win, she holds every urge until the meter forces one.
- Escorts: gain speed by dragging, pay with the carry. Which is cheaper is one sum.

Best plan by night 5: either the carry reaches home before sunrise, and the crew knocks the drunk out at once, or it does not, and dragging is never right. One answer either way.
Best plan by night 20: a known price for each item on the short temptation list. A lookup table (B21).

Co-op check: 1 coupled fail (the carry is the only joint act and it is the fallback) · 2 split fail (voice undoes it) · 3 talk pass · 4 blame pass · 5 not easy: numbers not written, so fail · 6 not solo pass · 7 two-way fail (the drunk obeys or griefs) · lone survivor fail (one escort cannot carry) · dying on purpose fail (passing out on purpose is the plan).

Findings.
- **Severe: one player fears and wants the same thing.** Who's Your Daddy works because the baby wins by dying. Here the drunk wins with the crew, so mischief is self-harm. This is Moonsick's "win together plus a reason to work against the crew", which had no precedent. Fix direction: none inside full co-op.
- **Severe: the rules are carried over.** One shared thing with a meter, kept going while events are dealt from a list: Red Button, Pet the Cat, Deathly Reality Show. The user's words for that family: "too simple and easy and requires no cooperation at all".
- **Severe: one answer, and passing out on purpose is it.** See the night-5 plan.
- **Severe: it does not scale and one side holds every call.** Five escorts for one drunk at 6; the sober side sees the truth and decides.
- Medium: the fun sits in written content (temptations, police, passers-by on a street), Red Button's failure, and the goal is a place to reach.
- Medium: the premise is crowded. Friendly Steps was listed for 3 September 2026 with 1 to 4 players roped together going home after a night out; Hobble-Wobble has a Steam demo where up to eight players share one drunk who must get home; Groggers! did it in 2016 (searched). Whether Friendly Steps shipped and how it sold was not checked by the file or by me.
- Medium: grab and drag between two player bodies is contact physics over the network, a lag fail.
- Minor: one feeling was never searched, and two rest on one game.

Carried rules: fail (family two).
Minigame or game: fail, the file says so.
Scope: fail. Costliest part: the street's content and the people on it.

## Ranking

1. **Dragon's Hoard.** The only one with a real layer between nights and feelings a co-op hit has caused; it needs a clock, a dragon that cannot be decoyed, and a reason to speak.
2. **The Glasses.** The only real split of information; the ghost rule and the single seer both have to go, which leaves little of the idea.
3. **Low Tide.** Cheap to build and it would run, but the crew has nothing to disagree about and Mudventure shipped it.
4. **Echo Bats.** A good picture with no co-op game under it, and flight eats the schedule.
5. **Last Round.** The user's most-repeated failed family in a new costume.

Drop: Last Round, Echo Bats, Low Tide.
Rework or drop: Dragon's Hoard and The Glasses; neither passes as written, and each needs a new rule for its threat, not new numbers.

## What the method let through

- A ✅ in the research column was read as a pass for the idea; it only shows that some game causes the feeling, by a rule this idea may not have.
- Feelings were borrowed from games where players are rivals (Clank!, Deep Sea Adventure, Who's Your Daddy) and nothing asked "same relation between the players?".
- Each scene was written to show the feeling, at 4 players only; no step asked for the best move at 3, at 6 and with bots before the marks went in.
- The reasons in the Dropped table were not run against the survivors: the decoy (Toys) hits Echo Bats, shared pay (Overloaded) hits Low Tide, a shipped premise (Dead Weight, Mimic) hits Low Tide.
- The older checks were skipped: no force when idle, decoy noise, "hunts the last X", a place to reach, 3 and 6, lag. Four of the five ideas fail one of them on the first line.
- The fantasy step is the user's in the skill; here Claude wrote all five, and four of the five are "a thing that reacts to our noise or presence while we fetch items", so they differ on the surface.
- Near games were searched after the idea was fixed and "near" never led to a drop; two more were missed (ByeByeObake!, Hobble-Wobble).
- Problems the file lists under "Unproven" (quarterback, silent routine, two unbacked feelings) are base problems that were set aside instead of fixed.

## Sources for the searched claims

- Mudventure: https://store.steampowered.com/app/4290170 and https://steambase.io/games/mudventure/info
- ByeByeObake!: https://store.steampowered.com/app/5385170 and https://automaton-media.com/articles/newsjp/20261009-472723/
- The séance game with a dead seer: https://store.steampowered.com/app/4796830
- Friendly Steps: https://store.steampowered.com/app/4279630 · Hobble-Wobble demo: https://store.steampowered.com/app/4445310 · Groggers!: https://indigostudios.itch.io/groggers
- Dragon themes: https://www.thegamecrafter.com/games/golden-hoard · https://crislayb.itch.io/draculae · https://alixxir.itch.io/hoardhunter
- Bats and sound-sight: https://amir-bayareh.itch.io/echo · https://sites.google.com/view/echo-bats/home · https://store.steampowered.com/app/4936650/ · https://store.steampowered.com/app/5270220/
- The Blackout Club: https://www.mobygames.com/game/blackout-club
