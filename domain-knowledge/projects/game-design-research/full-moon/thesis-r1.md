# Full Moon: thesis r1 (Claude, 2026-11-11)

Working title "Full Moon" (Claude). Online co-op, 3–6 friends, one developer, ~3–4 months.

## The user's idea (their words, 2026-11-11)
> a group of friends in a mansion. with garden and tree house. it is full moon and the survivors of the night win.
> there is a chance a random player becomes a legendary creature like a werewolf every now and then.. the symptoms
> are always different and difficult to analyse (just some common pattern and % to tell which creature it will
> become).. you need to have tools.. so you have to diagnose your friends before they become into a legendary
> creature.. and find the cure for it (% change of working and if the diagnose is correct). also physically holding
> or knocking out a player is allowed so making a friend inconcscous to prolongate the transformation is also valid.
> there can be 2 players transforming at same time but rare.. but only one can be transformed at a time.
> every legendary creature has different properties or powers or ways to deal with but the idea is that that
> creature needs to hunt a player or it will die in some time.. once it hunts a player, that player is dead and the
> creature becomes human again..

## The user's pillars (kept unless marked "changed")
- U1 Friends in a mansion with a garden and a tree house.
- U2 One full-moon night; whoever survives the night wins.
- U3 Every now and then a random player starts turning into a legendary creature (werewolf, ...).
- U4 Symptoms are always different and hard to read; a common pattern and % per symptom hint at the creature.
- U5 Tools are needed to diagnose friends before they turn.
- U6 A cure works only if the diagnosis is right, and then with a % chance.
- U7 Holding or knocking out a friend is allowed; an unconscious friend's transformation is prolonged.
- U8 Two players can be turning at once (rare), but only one can be a creature at a time.
- U9 Each creature has its own powers and its own way to deal with it.
- U10 A creature must catch a player before its time runs out, or it dies; the caught player dies and the creature turns human again.

## One sentence
Through one full-moon night in a mansion, friends keep starting to turn into legendary creatures: spot who is
turning, test them, and give them the right cure in time, because a friend who fully turns must catch one of you to
become human again, or die.

- **Job:** gather the creature items (wolfsbane, garlic, mirror) that appear around the mansion, garden and tree house,
  and keep an eye on each other's bodies and voices.
- **Choice:** cure now on a guess while the cure is strong, or test once more and cure later at lower odds; and: knock
  the sick friend out to buy time, at the cost of a pair of hands.
- **Goal:** be alive at dawn.

## Terms
- **Case:** one friend's sickness, from its first symptom until they are cured or fully turned.
- **Stage:** a case runs through 3 stages, then the friend turns. Each stage shows more symptoms; the cure gets weaker.
- **Creature item** (Claude): each creature has one item that does three things: tests for it, holds it off once
  turned, and cures it (used up when it cures). Wolfsbane = werewolf, garlic = vampire, a hand mirror = gorgon.

## The hub
The hub is **the sick friend's transformation** (a hidden meter: stage 1 → 2 → 3 → turned). Every system acts on it
and on nothing else:
| System | Acts on the hub by |
|---|---|
| Symptoms | showing it on the body and voice |
| Creature items, as tests | revealing which creature it is (from stage 2) |
| Creature items, as cures | ending it, with the stage's odds |
| Holding / knocking out | slowing it |
| Creature chase | finishing it: catch someone or die |
| The dead (ghosts) | small help around it (bring an item, slow a creature) |
| Night clock | setting how often new cases start |
That is 7 systems, inside the 4–8 of the short-dev hits (research.md 2026-11-09), all through one shared value.

## Rules (numbers are named starting values, to tune)
**Night.** NIGHT = 12 min. At dawn, everyone alive wins. If only one player is left alive, dawn breaks at once (Claude:
a lone survivor can't be diagnosed or cured by anyone, so a case would be a certain death with nobody to catch).

**Cases.** A new case starts on a random living player every GAP = 300 s ÷ (living players) ± 25%, so each player gets
sick about once every 5 min at any crew size. A player cured less than 60 s ago is skipped. Cases can overlap (U8); the
moon's height bends GAP (shorter around midnight).

**Stages.** TURN = 90 s: stage 1 (0–30 s), stage 2 (30–60 s), stage 3 (60–90 s), then turned.
| Stage | Symptoms showing | Creature item test | Cure odds |
|---|---|---|---|
| 1 | 1 subtle symptom | no reaction yet | 90% |
| 2 | 2–3 symptoms | reacts 85% of the time for the right creature | 60% |
| 3 | all drawn symptoms (3–4), obvious | reacts 85% | 30% |
The sick player isn't told. In first person you can't see your own face or eyes, and your own changed voice sounds
normal to you; you may notice fur on your own hands.

**Symptoms (U4).** Each case draws its symptoms from the creature's % table, so two werewolf cases can look different.
Symptoms overlap between creatures. The in-game journal lists the % (Phasmophobia-style journal).
| Symptom | Werewolf | Vampire | Gorgon |
|---|---|---|---|
| Yellow eyes | 60% | 30% | 40% |
| Grey, pale skin | 10% | 70% | 60% |
| Hair grows / moves | 70% (fur) | 0% | 50% (it writhes) |
| Voice changes (others hear it on proximity voice) | 60% growl | 30% whisper echo | 40% hiss |
| Drooling, hungry looks | 50% | 60% | 10% |
| Cold breath | 0% | 50% | 50% |

**Testing (U5).** Hold a creature item to a sick friend for 2 s: from stage 2 on, the right one reacts 85% of the time
(the friend flinches, coughs, smokes). Items don't react at stage 1, so testing everyone all the time gains nothing early.
You can't test yourself.

**Cure (U6).** Give the sick friend the creature item for 2 s (they must stand still, be held, or be unconscious). The
item is used up. Right item: the case ends with the stage's odds. Wrong item or a failed roll: nothing else happens; the
case goes on. Odds fall with the stage (Claude), so the % blames slowness more than luck.

**Holding and knocking out (U7).** Grab a friend from behind to hold them; they can struggle free in 3 s of mashing.
A held case runs at half speed. Hit a friend with a heavy object (pan, candlestick) to knock them out for KO = 20 s; an
unconscious case runs at a third of the speed (Claude: slows, doesn't stop, so it prolongs as U7 says but can't freeze
the case). Holding or a knockout also makes the cure easy to give. Cost: the holder's hands, and a longer case
overlaps more with the next one.

**One creature at a time (U8).** If a second case reaches the end of stage 3 while a creature is out, it waits at the
end of stage 3 (still curable at 30%) until the creature catches someone or dies; then it turns.

**Turned creatures (U9, U10).** A creature has HUNGER = 60 s to catch someone. A catch = holding a player for 2 s; a
friend breaks it by pushing the creature item into its face. Caught = that player dies, the creature turns human. Out
of time = the creature player dies. A creature item held up toward a creature keeps it 2 m back (it isn't used up).
| Creature | Power | Way to deal with it |
|---|---|---|
| Werewolf | fastest; sees footprints from the last 10 s; climbs the tree house ladder slowly | wolfsbane held up; doors slow it |
| Vampire | flies over walls and up to the tree house | garlic held up |
| Gorgon | slow; whoever has it in the middle of their view for 1 s turns to stone for 5 s | the mirror held up turns the gaze back; or look away and move by friends' voices |

**Creature items as supply.** SUPPLY = 2 of each item at the start, plus one new random item every 90 s at a random spot
among ~20 (kitchen, chapel, greenhouse, hedge maze, tree house). Each item is a defence and a cure: feeding your last
garlic to a friend on a guess may leave the crew bare if a vampire comes out.

**The dead (Claude).** A caught or starved player becomes a ghost: cut off from the living's voice (they can talk to
other ghosts), they can push small objects (bring an item toward friends) and chill a creature for 1 s (once every
20 s). Why: R.E.P.O.'s players asked for the dead to help, and its update did that (research.md).

## Scenes
**3 players (Ana, Bo, Cy), minute 3.** Ana hears Bo's voice drop into a growl (stage 1). Nobody holds wolfsbane; the
only one was in the garden. Choice: guess werewolf now and have Cy run for it (90% if right, and growl is 60% werewolf,
40% gorgon), or wait for stage 2 and test. Cy runs. Ana grabs Bo to slow the case; Bo can't help. Cy comes back at stage
2 (cure 60%), feeds it, fails. Bo turns at 90 s + slowing. Ana and Cy hold the garlic and mirror, not wolfsbane: the
werewolf runs them down. One of the three dies. Next case in ~150 s on the two left.

**6 players, minute 6 (midnight).** Two cases at once: Dee (pale, cold breath: vampire or gorgon) and Eli (fur on his
hands, he noticed himself). Four healthy players for two cases: two hold and test, two fetch. Fae knocks Eli out to
slow him (a third of the speed, 20 s) while Gus brings wolfsbane; Dee's mirror test reacts (gorgon), cured at 60%.
Eli was knocked out twice, so his case ran long, and overlapped with the next case (Hal). The crew splits three ways.

## Checks I ran (Claude, in words, not played)
- Player-with-player: diagnose, hold, knock out, cure, catch, break a catch: all done to one specific friend. ✓
- Force: the transformation grows on its own; only a friend can test, hold or cure you. ✓
- Dominant strategies tried: (1) knock out every sick friend: slows to a third but never stops, and ties up a player per
  case; (2) test everyone constantly: items don't react at stage 1; (3) carry all items and cure on stage 2 every time:
  supply is short and each item is also the defence; (4) huddle with items held up: the job (new items at random spots)
  makes you split; the gorgon punishes huddles looking the same way; (5) hide in the tree house: every creature reaches it.
- Lone survivor: dawn breaks. Two left: one cures the other, or a 1-on-1 chase.
- Lag: grabs and catches are 2–3 s holds, not split-second timing. Melee knockouts are normal host-authoritative hits.

## Pillars changed or added (all Claude)
- U6: the % now falls by stage (90/60/30).
- U7: unconscious slows the case to a third instead of stopping it.
- U8: read as "a second full turn waits at the end of stage 3".
- Added: tests react only from stage 2; one creature item = test + hold off + cure; ghosts; dawn at one survivor;
  case rate per living player.

## Content and build
- One hand-made map (mansion ground floor ~8 rooms, garden with hedges and greenhouse, tree house), random item spots.
- Smallest playable: 2 creatures (werewolf, vampire), the 2 items, holding, knocking out, one chase each.
- Per creature: a transformed body (fur/fangs/snake hair on the player rig), one power, a symptom row, one item.
- Tech: proximity voice with a filter for the voice symptom (needs friends on in-game voice, not Discord).
- Test crew 1 human + 2 bots: bots can be patients (the human reads symptoms on them and cures them) and creatures
  (a chase AI); the human being diagnosed by bots needs scripted bot tests. The fun (watching each other) needs humans.

## Open
- Why ghosts help (the dead have already lost).
- The gorgon's gaze rule needs a camera-direction check online.
- Whether a guess at stage 1 is ever worth it (the numbers above make guess vs wait close, on purpose).
