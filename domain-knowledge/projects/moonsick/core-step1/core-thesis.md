# Core thesis r1: fewer rules, shown by bodies, not text (Claude, 2026-11-12 evening)

After the UX pass the user played practice (lesson 1; checked: no saved lesson, so they never saw dawn) and said
"i still have the same issue.. nothing has improved". Their 13 points, verbatim:
start of the game doesnt explain what to do · symptoms are too fast to follow or track and difficult to read · many
UI text explain what to do instead of game feedback · too many UI elements · guide of curing is messy and too
detailed, too much information · dont know the goal · dont know what a cure is and why · dont know if im
transforming or a friend is · dont know what to do with a object · dont know how to interact with a object · dont
know the actions i can do with other players · dont know any choices · dont know how to read what is happening.

Rules: `docs/design.md` (v2.4). Research: `docs/ux-research.md` + section "Research (r1)" below.

## Frame
The 13 points are 4 problems:
1. **No why:** goal, what a cure is, which choices exist (3 points).
2. **Can't read the state:** signs too fast and faint, who is turning, what is happening (3 points).
3. **Can't see the verbs:** what objects do, how to use them, what you can do to friends (3 points).
4. **Text instead of the game:** the start, UI text, too many UI elements, the cure guide (4 points).

Underneath all four [read, from design.md and code]: a new player meets about 25 rules (8 signs with visibility
conditions, veins, 3 cures, 2 tools, give, grab, pan, shove, 3 powers, 3 senses, 3 head starts, tricks, scars, the
pond, doubles, hunger, moonlight speed-up, curer protection, 8 quick-chat keys), and almost every piece of state is
invisible or tiny (eyeshine only out of moonlight or within 2.5 m; grey skin and drool only in moonlight or within
2 m; inner signs as faint screen effects that grow near triggers; odds hidden; a patient whose first sign is outer
doesn't know they're sick). So each rule needed words, the words became UI, and the UI is now problem 4.
Lesson 1 already cut tricks, scars, pans, powers and doubles and still failed, so cutting rules alone isn't enough;
the previous pass added words and failed, so words alone aren't enough. Both levers at once:
**(a) ≤ 3 rules a new player is told; (b) everything else shown by bodies, objects and sound, big and slow.**

Reframe of the user's pillar "signs hard to read": hard to **interpret** (one sign leaves two creatures; a friend may
lie), never hard to **see**.

## Three different answers
- **A. Loud core (recommended).** Keep the fiction and the core choice (which herb, now or after one more sign);
  cut every other system from the default night; show what's left on bodies, objects and sound; delete most UI.
- **B. One monster first.** Werewolf only: spot, fetch, give, survive. Cheapest. Against: it removes the only choice
  (which herb, now or later), and "dont know any choices" is one of the 13 points; it's a different game to tune.
- **C. Same rules, new channel.** Keep all ~25 rules, move every message from text into the world. Against: critic
  memory "stacked hidden rules, patched with words" (×3) and lesson 1's failure; 25 rules can't all have a body.

## A in detail (all Claude)

### The 3 rules (start card, 8 s, pictures + ≤ 25 words; also the whole of "How to play")
1. Friends will start turning into monsters. Their body shows which: each sign rules out one monster.
2. Give the matching herb before they turn. Sooner works better; the wrong herb makes it worse.
3. A turned friend must catch someone. Hold up its herb to push it back. Alive at dawn wins.

### Signs: on the body, big, slow, never fading
Same rule as today (each sign rules out one monster, so each monster has two of the three), now as pictures:
| Monster (herb) | Seen by others | Felt by the patient |
|---|---|---|
| Werewolf (wolfsbane) | glowing eyes + long claws | the dark looks lighter + craving meat |
| Vampire (garlic) | glowing eyes + grey stone skin | the dark looks lighter + moonlight burns |
| Troll (rowan) | grey stone skin + long claws | moonlight burns + craving meat |
(Claws replace drool: drool can't be seen past 2 m.)
- **Seen signs:** visible within 10 m in any light, from any side (glow is self-lit; skin and claws are big shape
  changes on the model). Once shown, a sign stays until cured.
- **Felt signs:** a constant screen effect, not one that only grows near a trigger (night sight: the view is
  brighter; moonlight burns: white bloom and a hiss whenever you're in moonlight; craving: the view drifts toward the
  nearest meat). When one starts, one line names it once, ≤ 6 words: "You feel: the dark looks lighter".
- **Knowing you're sick:** from the first second of a case your own first-person hands tremble and darken a little
  more each stage, with a slow heartbeat. You know *that* you're sick, never *which* monster (unless you feel a
  felt sign). Others see that only through seen signs. Hiding it (not telling) is your bluff.
- **Stages show how late it is** on the body for everyone (replaces neck veins): stage 2 the patient hunches, stage
  3 they twitch and growl softly.
- **Pace:** case 150 s at dusk → 120 s by the end (was 75 → 60); one new sign per stage (stage 1: one sign, felt or
  seen at random; 2: one of the other kind; 3: the remaining felt and seen sign; then the turn). GAP base 90 s → 45 s
  so a 12-min night at 6 alive still has about 4–5 cases (was ~6) [assumed: rough estimate, check in the sim].
  Doubles stay at 10 → 20% (user's "two at once, rarely"; readable without teaching: two friends visibly turning).
- **The % per sign (user pillar)** stays as the rule for which sign shows first; it's not on screen.

### Verbs: 4, shown at the target
- **E** pick up / drop (herbs only; tools and pans cut). **Hold LMB on a friend:** with a herb in hand, give it
  (2 s; they hold still); with empty hands, grab them (case at half speed). **RMB:** hold your herb up (pushes its
  monster back). **1–4:** say a felt sign or "I feel fine" (speech bubble over your head; the bots use it too).
- Aim at anything you can use within reach: it gets a white outline and a small key icon at the thing
  ("E", "hold LMB"). Nothing in the HUD.
- The herb in your hand is its 3D model in first person (Meshy models exist); no hand text.

### Feedback: bodies and sound, not banners
- Right herb works: the friend glows the herb's colour, signs drop off, they straighten; a chime.
- Right herb, failed roll: the friend shudders hard (visible jolt + groan): "right kind, try again".
- Wrong herb: the friend convulses, the next sign pops out at once, a red burst.
- A turn: a roar everyone hears from anywhere, the monster model, a camera kick for those within 10 m.
- A catch: a scream, the body drops. The dead see from behind a living friend (unchanged).

### The goal and the cure, shown once (practice only, ~40 s, you can walk around)
In the hall at the start: bot Ana's eyes start to glow (you see it: werewolf or vampire); she says "I crave
meat" (werewolf or troll); bot Bo runs to the garden, comes back with wolfsbane, gives it; Ana glows green and
straightens. Then bot Cy turns into a troll with nobody curing him (roar), catches bot Dee (scream), turns back.
The night starts; the first real case is a bot at ~60 s, the second is you.
Online: the start card only.

### UI after A (5 things)
The night (a moon moving across a small arc, top), the outline + key at what you aim at, speech bubbles, the start
card, and Tab: one picture card (3 monsters, each with its 2 seen + 2 felt sign pictures and its herb; no %, no
text table). The felt-sign line (once per sign). Removed: notes page, % table, feed, coach line, look readout,
banners, toasts, floor plan, danger edge, hands text. Doorway signs stay (in the world), herb picture instead of
the word.

### Kept as hidden numbers (not taught)
Cure odds slide with progress; head starts at the turn and the shown-if-far rule (user: helping beats fleeing);
curer protection 90 s; hunger (the body thins); creature senses (the creature's own screen shows them).

### Cut from the default night (back later only if the core reads; flags keep them)
Tools (spoon, thermometer), pans / knockout, tricks, scars, pond cold, powers, moonlight speed-up, veins, quick chat
5–8, notes and the sign table. Practice lessons collapse to one practice night (same rules as online).

### User pillars this drops or bends (must be confirmed by the user)
- "tools are needed to diagnose": dropped for now (seen + felt signs are the split).
- "holding **or knocking out**": knocking out dropped for now; holding stays.
- "each creature has its own powers": powers dropped for now; "its own ways to deal with it" stays (senses, speed).
- "signs always different and hard to read, with a % per sign": bent: hard to interpret, easy to see; % hidden.
- "bluff from both sides": kept (patient hides or lies about felt signs; curer can give the wrong herb), but the
  sabotage-by-pan route is gone with pans.

## Scenes
- **Smallest (the user's setup: 1 human + 5 bots, practice):** 0:00 card. 0:08–0:50 the hall demo. 1:00 Bo's eyes
  glow (seen from 8 m in the dark hall); Bo's bubble: "the dark looks lighter". Both rule out only the troll, so
  it's still werewolf or vampire: you choose, wolfsbane or garlic now (a coin flip at full strength), or wait.
  1:50 Bo grows claws: werewolf. Wolfsbane: outline + "hold LMB" on Bo; Bo glows green and straightens.
  3:30 your hands tremble; 4:00 your view brightens ("You feel: the dark looks lighter"); you press 1; a bot looks at
  you, sees grey skin at 4:50: vampire; gives you garlic.
- **Largest (8 humans online, 9:00):** two friends hunched (stage 2) in the kitchen; one has glowing eyes, one
  claws; one says "moonlight burns", the other says "I feel fine" (lying or early). Four herbs left in the house;
  someone grabs the liar-or-not; arguing about who gets the last garlic.

## Research (r1)
- Infection made readable through what it does to you: Barotrauma's husk infection changes your speech (garbled
  radio, shorter chat range) at its "active" stage [source: Attack of the Fanboy guide,
  https://attackofthefanboy.com/?p=909422]. [read] Supports "you know you're sick by what your body does".
- One reveal card that states your goal before play: Among Us flashes your role and the impostor count at the start
  [source: https://uxdesign.cc/from-tasks-to-tricks-the-ux-of-among-us-d469b45dba22]; its UX makes it easy for new
  players to know what they can interact with [same source].
- Teach by the level, not text; Portal's first chambers teach with no pop-ups; removing all teaching backfires
  [source: https://gamedeveloper.com/design/methods-of-creating-invisible-tutorials,
  https://www.wayline.io/blog/silent-tutorials-player-learning]. A study found HUD elements less disruptive than
  diegetic ones and clarity valued over looks [source: https://www.csit.carleton.ca/~rteather/pdfs/GEM2015_HUDs.pdf].
  [read] So: diegetic where it's clearer, a key icon at the target is fine.
- Social deduction newcomers struggle with too many roles; the accessible ones keep the set small [source:
  https://www.wargamer.com/blood-on-the-clocktower/review,
  https://bumblingthroughdungeons.com/the-problem-with-social-deduction-board-games].
- Lethal Company: objective clear and easy to follow; complexity grows from items and the bestiary later
  [source: https://cogconnected.com/feature/what-makes-lethal-company-so-good/]. [read] Simple core first, depth by
  discovery.

## Critic r1 synthesis (2026-11-12 evening; report `docs/critic-core-r1.md`)
| Finding | Decision |
|---|---|
| S1 the kept choice is dead (give on 1st sign 0.90 vs wait 0.74; also true of v0.1) | To the user. Step 1: a wrong cure turns the friend at once (critic sweep: wait-for-certain 0.74 vs give-on-1st 0.52; a Claude sim with a random 2nd-sign time puts the best stop at p ≈ 0.5–0.65). Still one best answer, but it now needs felt + seen combined. A real situational choice is open (questions 16). |
| S2 betrayal hollow once pans go; bent pillars unlisted | To the user: listed below; the motive to lie is open (questions 17). |
| S3 bots take the herbs and the patients from the human (checked by reading bot.gd: tool within 18 m, cure within 22 m, 2 doctors per patient) | User (2026-11-12): "i wouldnt say that the bots are the issue.. i would say that everything is wrong and can let the bots do what they do but slower". Step 1: bots keep their behaviour, slower (Claude's reading: they react ~15–20 s later to signs and to items, so the human usually gets there first). |
| M1 "3 rules" undercounts; card 50 words | Fixed: card ≤ 25 words for real, says "only you feel your signs: tell them"; the sign table counted as taught; the monster models carry their own signs (claws on werewolf and troll, glow on werewolf and vampire, stone on vampire and troll). |
| M2 hidden behaviour rules | Fixed: head starts, shown-if-far and curer protection off in step 1 (listed). |
| M3 claims vanish in 4 s | Fixed: a claim stays over the head as a picture until the speaker changes it. |
| M4 shudder vs convulse look alike | Gone with S1's step-1 rule (wrong = turns); a failed right cure leans toward the giver in the cure's colour. |
| M5 hands leak seen signs | Fixed: hands only tremble; every seen sign sits where the patient can't see it. Claws on the fingers would show in first person, so the third seen sign becomes a bristling back (werewolf and troll) instead of claws. |
| M6 8 humans: same facts for all (quarterback) | Parked for after step 1 (the user's test is 1 + 5 bots); listed. |
| M7 not a small step | Fixed: step 1 = bot fix, cut flags, wrong = turn, pace, bigger seen signs on existing meshes, trembling hands + heartbeat, HUD trimmed, start card, outline + key, Tab picture card. Demo, felt-effect rework and reel changes later. |
| M8 online teaching = card only; RMB and 1–4 unprompted | Partly: every verb gets a prompt at its target; online learning through the first case is parked. |
| m1 scenes vs schedule | Redo scenes with the script before building. |
| m5 doubles in practice | Off in practice for step 1. |
| m2, m3, m4, m6, m7, m8 | m3 adds "something's wrong" to quick chat; m4 craving = a stomach growl, not a camera drift; m6 kill lines rewritten after step 1; m7 dark pillar listed; m8 no demo in step 1. |
