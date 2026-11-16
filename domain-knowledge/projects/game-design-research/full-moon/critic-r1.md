# Full Moon: critic r1 (isolated antithesis, 2026-11-11)

Read: thesis-r1, design-anti-patterns, critic-anti-patterns, DRS gameplay-anti-patterns, checks.md, triad / idea-search-loop /
scope-lessons memory, Full Moon research.md, research.md 2026-11-11 (Mario Party feel; funny vs difficult).
Numbers marked (sim) come from a rough simulation the critic wrote:
`/tmp/claude-1000/-home-akiraki-claude-code/af38afdd-afdf-46d2-af17-ecc332518f6b/scratchpad/fm_sim.py`. It assumes play that favours
the crew (cases noticed at once, items found the moment they spawn, perfect tests, knockout chains, no midnight speed-up, no
hoarding), so real death counts would be higher. Everything else is reading, not play.

## Severe

**S1. The cure loop is one-way: the patient just stands there.**
- Why: the patient isn't told, can't test or cure themselves, and only has to "stand still, be held, or be unconscious". Their one choice is "don't struggle". This fails gate 7 and checks.md 1.4. Under the knockout chain (M2) they lie face-down for 20–180 s on every case (DRS #2). Their hidden state gives them no reason to hide anything (critic "hidden info nobody gains from hiding" ×2). Everyone nearby sees the same signs, so whoever holds the journal runs the crew (quarterback ×3). The chase is the only two-way part, and the chase is the failure state.
- Fix (changes Claude's "sick player isn't told"): split the signs. Inner signs only the patient gets (a screen tint, a heartbeat, a craving, their own hands); outer signs only the others see (eyes, voice, skin). Reading the case then needs both sides to talk. Keep U4's % on both kinds.

**S2. The item test makes U4 (signs that are hard to read) dead weight.**
- Why: a test is free, takes 2 s, can be repeated, never reacts to the wrong item, and reacts 85% for the right one. So any reaction is certain, and three swipes settle the creature in about 6–10 s from stage 2. Signs are left only for noticing. Logic and fantasy split here: the user's fantasy is "difficult to analyse", the logic is "swipe three items". The research note's Phasmophobia lesson (between obvious and impossible) lands on obvious. Breaks A15 (shallow choice), A21 (solved by run 2), and critic "a limit that never binds" ×2: 85% means nothing when retests are free.
- Fix (keeps U5, changes the Claude-made "creature item = test"): tools show signs, never the answer. A thermometer shows cold breath, a mirror shows no reflection, a UV torch shows the eyes. The journal % stays the only way to the creature. Items keep 2 jobs (hold off, cure).

**S3. A new player must learn 18 rules (count below).**
- Why: the user's checks allow one sentence plus at most 2 extra rules. Critic anti-patterns ("4–8 systems read as 4–8 rules", ×2) set at most 3 taught rules, with the rest as things in the world. The thesis cites the hits' "4–8 systems" as licence and then writes 18 rules. Other problems in the same rules: one item with 3 jobs (critic "one key with several jobs"); test and cure are two near-identical 2 s actions with the same item; there are hidden stages, hidden odds and a hidden case clock.
- Fix: teach 3 rules: (1) a friend shows signs, so read them; (2) feed them the right item; (3) a fully turned friend must catch someone. The pan and the grab are objects in the world. The 60 s skip, the stage-3 queue and the moon speed-up stay hidden. Cut the gorgon and the ghost rules from v1.

## Major

**M1. Scale is ignored, and U8 (user pillar) is bent without saying so.**
- Why: GAP = 300/living players makes overlap grow with crew size. At 6 players (sim), 2 or more cases run at once for about 380 s of the 720 s night; at 3, about 65 s. U8 says "rare". Supply is 14 items a night, fixed. At 6, the clinic plan (see "Dominant strategy") needs about 24, so 3.5 of 6 die even under perfect play, and only 1% of nights have no deaths. At 3, 0.8 of 3 die, and 42% of nights have no deaths. Deaths at 3 come mostly from which item type spawned, so it's luck with no culprit (A20, DRS #6, #17).
- Fix: cap overlap (at most 2 cases, and set GAP so 2 at once happens in ≤ 10% of the night). Spawn items per living player. Make the spawned type the type that's short, or mark spawns in the world. Scaling supply alone still leaves 2.1 deaths at 6 (sim).

**M2. Knocking out beats holding every time; U7's hold is a dead verb.**
- Why: a knockout runs the case at 1/3 speed (holding gives 1/2). It frees your hands, makes the cure easy, and can be chained every 20 s at no cost. One nurse can keep 2 patients down. Chaining saves about 0.26 deaths a night at 3 (sim), so you pan every case. Breaks A15, DRS #2, and critic "a limit that never binds" (KO = 20 s).
- Fix: a friend who wakes can't be knocked out again for 20 s (about 2/3 speed on average, so holding competes). Or a knockout hides the patient's outer signs while they're down.

**M3. The chase only picks who dies, never how many.**
- Why: under U10, a turned case costs exactly 1 life whether the crew holds it off or not. So the thesis's "feeding your last garlic leaves the crew bare" is false for the crew. A shield only protects whoever holds it, so each player hoards one of each type. The creature then catches whoever lacks the item (critic "threat hunts whoever lacks X", a one-line answer; checks.md 4.5).
- Fix: either say plainly that it's a private stake, or let a held-off creature still be cured at 30% within HUNGER. That second option bends U10 (it adds a third way out), so take it to the user.

**M4. "Dawn at one survivor" (Claude's) rewards betraying your last friend.**
- Why: at 2 alive, the healthy player wins at once by not curing and holding the right item up for 60 s. The sick one wins by running from the cure and catching. Letting a friend die helps you (gate C "dying on purpose"; critic "restrictions added beyond the user's words").
- Fix: drop the instant dawn. Let a ghost push an item into the lone survivor (a ghost cure), so a lone survivor can still be cured.

**M5. The dead sit out 4–10 minutes, cut off from voice, with no stake.**
- Why: under U2 the dead have already lost. At 6, about half the crew are ghosts by minute 8 (sim). This is R.E.P.O.'s "dead watching" complaint (research.md), DRS #2, #11, and critic "the dead get only a voice" ×2. A bored ghost can push the last mirror into the pond, and nobody can answer back (DRS #8).
- Fix: a ghost who pushes in the item that cures someone comes back alive. That gives them a stake, a physical job that bots can also do, and a check on the losing streak.

**M6. One 12-minute night with nothing carried over is still one long round.**
- Why: research.md 2026-11-11 names this as the Mario Party feel, and the thesis didn't use it (A26). The journal and the clinic routine are learned by about night 3 (A21).
- Fix: a 3-night moon cycle. Unused items carry over. Cured friends keep one sign as a scar, a false lead the next night. One new creature each night.

**M7. The user's test crew (1 human + 2 bots) can't play the core.**
- Why: the voice sign, the gorgon's "move by voices" and voice-cut ghosts all need humans. A human patient needs scripted bot doctors that read the hidden meter. This repeats critic "voice-only tested with bots" ×2 and "test setup deadlocks" ×3, and the thesis admits "the fun needs humans".
- Fix: show every sign on the body, including voice as a visible puff or ring. Bots read the same visible data and have timeouts. First build: a human doctor and 2 bot patients, which can be tested today.

**M8. Full scope is over 3–4 months, and the smallest build can't test U4.**
- Why: the full build means 3 creature bodies, 6 per-player sign visuals, a live voice filter, flight, a gaze check, ghost mode, grab and knockout netcode, 3 bot AIs, and a hedge maze, greenhouse and tree house. Online work costs about 5× (scope-lessons). The smallest playable has 2 creatures, so diagnosis is a coin flip: feed both items at stage 1 for a 90% cure, at 2 items.
- Fix: v1 = 3 creatures that are only sign rows plus one item each, and one shared chase body (no powers, no flight, no gaze, no ghosts). Ground floor and garden only.

## Minor

**m1. Some rules are left unspecified.**
- Why: no carry cap, so one "pharmacist" can hold every item, test, cure and be immune to all creatures (checks.md 4.7; gate 6). Also unstated: where the 6 starting items are; whether spawns are announced; whether "held up" works all the way round; whether a creature can be knocked out (if so, chain it until it starves); whether a failed cure can be retried at once (as written, yes, so two copies give 84% at stage 2) (A19).
- Fix: carry 1 item. A creature can't be knocked out. Spawns make a sound. Write each one down.

## Dominant strategy
The "kitchen clinic", settled by night 3. At 0:00 all 6 items go to one room. Everyone stands in a ring facing inward. Anyone with any sign is panned on sight and again every 20 s. Nobody guesses at stage 1 unless 2 or more of the likelier type are in stock. At stage 2 the doctor swipes the three items (≤ 6 s), feeds the one that flinches, and repeats with any copies. One runner loops the ~20 spawn spots. Everyone keeps one shield of each type. In a chase they back into a corner with the right item up and let the creature starve. Nobody opens the journal after night 2. Result (sim, play that favours the crew): at 3, about 0.8 deaths a night (42% of nights with none); at 6, about 3.5 deaths, set by which item types spawned, not by skill.

## Co-op gate
1. Coupled: ~. You can't test or cure yourself, but one healthy player can do the whole job on a patient who stands still.
2. Split: ✗. Everyone nearby sees the same signs; the test gives the answer to whoever holds the item; roles are chosen, not set by where you stand.
3. Talk: ✓. You can't see your own face, so someone has to say "Bo, your eyes."
4. Blame: ✗. Most deaths come from a hidden 40% roll or the wrong item spawning; only the unshielded victim or a slow runner has a face.
5. Not easy: ~. New crews lose, but the clinic beats 3-player nights, and the night gets easier after midnight (GAP lengthens again), so it isn't harder over time.
6. Not solo-able: ~. With no carry cap, one pharmacist tests, cures and is immune.
7. Two-way: ✗. The patient stands still or lies knocked out (S1).
- Lone survivor: no soft-lock, but instant dawn rewards letting your last friend turn (M4).

## Rule count: 18
1. Survive 12 min; dawn comes at once if one player is left.
2. A random friend starts turning; you can't see your own signs (except your hands).
3. Signs map to creatures through a 6 × 3 % journal.
4. 3 stages of 30 s; cure odds 90/60/30%.
5. Test = hold an item to a friend for 2 s; it reacts only from stage 2, 85% of the time.
6. Cure = give the item for 2 s; the friend is still, held or knocked out; the item is used up; a wrong item does nothing.
7. Grab from behind = half speed; mash for 3 s to break free.
8. Pan = knocked out for 20 s, case at 1/3 speed.
9. A friend cured less than 60 s ago is skipped.
10. One creature at a time; a second case waits at the end of stage 3.
11. A creature must catch someone (a 2 s hold) within 60 s or die; the caught player dies and the creature turns human.
12. Break a catch by pushing the item into its face.
13. An item held up keeps its creature 2 m back.
14. Werewolf: fast, sees footprints, climbs the ladder slowly, slowed by doors.
15. Vampire: flies over walls.
16. Gorgon: its gaze turns you to stone in 1 s; a mirror or looking away counters it.
17. Supply: 2 of each item at the start, one random item every 90 s at about 20 spots.
18. Ghosts: no voice to the living; can push objects and chill a creature for 1 s every 20 s.

## Scenes played by the critic (night 5, the crew knows the clinic)
**3 players.**
- 0:00–1:40: items are carried to the kitchen. Bo pans Cy for a laugh. No case comes until about 1:40, so two players stand and stare.
- 1:40: Bo shows yellow eyes. He is panned and lies down for about 70 s. The item swipe finds wolfsbane; the first cure fails at 60%, the second works.
- 3:00–4:20: idle. Cy, alone in the hedge maze, starts turning; nobody sees or hears it until stage 2. It's a vampire and there's no garlic. A 3-minute knockout chain follows while Ana searches 20 spots. Cy turns, flies in and catches Bo, who has no garlic.
- About 8:00: Bo's ghost watches for 4 minutes with no voice.
- Endgame: Ana starts turning. Cy sees that holding wolfsbane up for 60 s wins the night alone.
- What happened: the patients were objects, there was a minute of idling between cases, and the death came from which item spawned.

**6 players.**
- From 0:50: a case every ~50 s, often two at once. One or two friends always lie on the kitchen floor. The doctor decides; two nurses re-pan on a timer; two runners loop the map for one item every 90 s.
- About 5:00: the type the crew needs runs out. Turns come back to back. In each chase, whoever lacks the item dies in seconds.
- A gorgon turning in the inward-facing ring stones 4 players at once.
- Fae pans the doctor mid-cure as a joke. That one is fine: slapstick with a comeback.
- About 8:00: 3 ghosts. By dawn, about 2.5 of 6 are alive.

## Numbers checked
- **Guess at stage 1:** the most likely creature for one sign is right 46–58% of the time (from the journal table). Times 90% that gives 0.41–0.52 per item, about 2.1 items per cure.
- **Wait for stage 2:** the creature is certain within about 10 s; each right item cures 60%, about 1.67 items per cure; 2 copies give 84%.
- **Feed all 3 items at stage 1:** 90% for 3 items, about 3.3 items per cure.
- **Sim, deaths per night, guess vs wait:** 3 players 0.73 vs 0.83; 6 players 3.67 vs 3.51. Close, as the thesis intends, but stock decides it, not reading the signs.
- **Limits that don't bind:**
  - stage time (about 8 s of work in a 30/60/90 s window);
  - 85% (free retests);
  - KO 20 s (chainable);
  - HUNGER 60 s (the werewolf needs about 2 s to catch someone without the item);
  - mash 3 s against a 2 s cure (a held patient can never escape).
- **Limits that bind:** GAP and SUPPLY, at 6 players only.

## What is strong (keep)
- The patient can't see their own face or hear their own growl, so friends have to tell them. That is a built-in reason to talk, and a funny "wrong but okay" moment shown on a body (research.md, "funny vs difficult").
- Fantasy, logic and look meet on the body: fur, eyes and voice show the state with no bar (checks.md 2b ✓), and "survive the full moon" fits the fantasy.
- Panning a friend to buy time (U7), and a friend's own body hunting you (U10), are slapstick with a reason. Keep both.
