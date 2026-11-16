# Examine thesis r1: diagnose a friend by examining them up close (Claude, 2026-11-12 evening)

User: after `docs/diagnosis-research.md`, Claude's read ("keep diagnosis but give it the conditions that make it
work: grab a friend, examine them up close, eyes, teeth, skin, each a big sign; their own screen tells them they're
sick; pick one shape, drop the other two"); user: "makes sense.. lets implement that".
Builds on step 1 (`docs/core-thesis.md`, synthesis table): tools, pans, tricks, scars, pond, powers, moonlight
speed-up, head starts, curer protection, doubles, quick chat 5–8, notes/feed/coach/readout/banners/floor plan are
being switched off by a separate removal pass. Bots keep their behaviour, slower (user).

## Frame
Research: games that make diagnosis work pick ONE way of knowing (the patient knows / a tool knows / clues are
combined). Puzzle-style diagnosis (combine clues) works when the subject holds still (Phasmophobia's ghost room,
Keep Talking's bomb, Quarantine Zone's checkpoint); signs that work are big and physical; subtle signs are the top
complaint. Moonsick asked for a clue puzzle on a friend walking in the dark with faint signs, using three ways of
knowing at once. The shape: **clues combined, gathered by examining a held or still friend up close**. The patient
knows only *that* they're sick, never *what*.

## Rules (all Claude unless tagged)
1. **You know you're sick, not what.** From the first second of a case, your own screen changes by stage
   (research: No More Room in Hell 2): stage 1 a slow heartbeat and a dark pulse at the screen edge; stage 2 the
   edge pulses faster with dark vein lines; stage 3 red veins, breathing heavy. Felt signs (night sight, moonlight
   stings, craving) are switched off. Quick chat: 1 "I'm sick!", 2 "I feel fine", 3 "Hold me", 4 "Help!".
2. **Signs only show up close, on examination.** Three spots, each a yes/no sign that rules out one monster; each
   monster has two of the three:
   | Spot | Sign | Rules out | Monsters |
   |---|---|---|---|
   | Eyes | glowing | troll | werewolf, vampire |
   | Skin (neck and cheek) | grey stone | werewolf | vampire, troll |
   | Hands | hairy, long nails | vampire | werewolf, troll |
   - Stage 1: one of the monster's two signs (random, the user's % per sign decides which). Stage 2: the second.
     Stage 3: nothing new; the body shakes. Then it turns.
   - From afar a sick friend shows nothing but the dark neck veins (kept; within 4 m) and, at stage 3, shaking.
3. **Examine:** stand within 1.5 m of a friend who is held by someone or standing still, hold F: the camera zooms in
   on their eyes, then hands, then skin, 1.5 s each (4.5 s; you can stop early). Each spot shows its sign big or
   plain. Anyone can examine; what you saw is only on your screen (tell the others). A friend can walk away from an
   examination unless held.
4. **Hold (unchanged):** grab from behind with empty hands: case at half speed; they can struggle free (3 s mashing).
   The holder can't examine or give (both hands busy): holding is a second player's job.
5. **Give a cure (unchanged, 2 s):** on a held or still friend. Right cure: works with the odds
   (30% + 65% × (1 − p)^1.5); a failed roll: they shudder (right kind). **Wrong cure: they turn at once** (critic
   core r1 S1: a wrong cure was a free test).
6. **Case length** 150 s at dusk → 120 s by the end (step 1).
7. **The Tab card**: the table above as pictures (eye, hand, skin; each monster with its two and its cure). No %.
8. **Start card (≤ 25 words):** "Friends will turn into monsters. Hold them, examine eyes, hands and skin, give the
   right cure. Wrong cure: instant monster. Survive till dawn."
9. **Bots:** examine instead of reading signs from afar; hold a sick friend when another bot or the human is near;
   react ~15–20 s slower than now (user: slower).

## Choices this creates
- **Patient:** tell ("I'm sick!", "Hold me") and let someone hold you, or keep quiet (afraid of a wrong cure from
  someone you don't trust: it turns you at once).
- **Doctor:** cure now on one sign (2 monsters left, a coin flip; wrong = instant monster) or hold on and wait for
  the second sign (held = half speed, the odds slide).
- **Crew:** who holds, who examines, who fetches which cure; whom you let near you.

## Scenes
- **1 human + 5 bots (the user's test):** Bo's (bot) case starts at 1:00; at 1:15 Bo says "I'm sick!". You walk
  over; at 1:25 Cy grabs Bo from behind. You hold F: eyes glowing, hands plain, skin plain: werewolf or vampire.
  Garlic is in the kitchen, 20 m; wolfsbane at the pond, 30 m. You wait; stage 1 has 25 s left, at half speed 50 s,
  so at 2:15 you examine again: hands hairy: werewolf.
  You run to the pond, come back, give wolfsbane.
- **You are sick:** 3:00 your screen edge pulses, heartbeat. Press 1 "I'm sick!". A bot comes, another grabs you.
- **8 humans:** two holders, three examiners shouting what they saw, two runners for cures; someone says "hands
  plain" when they were hairy.

## Pillars
- Kept: one night, dark, diagnosis with a % per sign (which sign first), cure works only if right then with %, hold,
  creature must catch or die, betraying never pays more than curing, the hunter chooses freely, no cloud, no ghosts,
  reel.
- Bent: "a sick player can lie about what they feel" becomes "a sick player can hide that they're sick"; an examiner
  can lie about what they saw. Tools (user: "tools are needed to diagnose") stay off: examining by hand replaces them.
