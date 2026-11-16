# Diagnosing a friend: how games make reading another player's state work

Games where players read signs on each other or on evidence to work out a hidden state, with the patterns and anti-patterns they share.
Tags: [source] = said by the linked source; [read] = Claude's reading of it; [memory] = Claude's memory, not checked; [opinion] = Claude's own.
Most sources are guides, wikis and reviews, not developer statements.

## Games

### Co-op / multiplayer, infection among friends
- **No More Room in Hell 2** (co-op zombies) [source: https://allthings.how/no-more-room-in-hell-2-every-infection-stage-and-how-to-cure-it/]
  - The infected player's own screen tells them, in stages: none → white "god ray" lines at the edge, blur, echoing
    audio, coughing → pulsing red vein-like lines at the screen edge, whispers, stamina loss.
  - Teammates hear the cough over voice chat.
  - About five minutes from first symptoms to turning. Pills reset the timer (buy time); gene therapy is the only cure:
    draw blood, wait ~30 s, inject. Once turned: "an aggressive runner that will chase and attack your teammates".
  - Self-sacrifice key: die without turning.
  - [read] Nobody has to work out *what* it is: the patient knows, the drama is telling, curing in time, or dying.
- **The Thing (2002)** (squad with infection) [source: https://en.wikipedia.org/wiki/The_Thing_(video_game),
  https://thejimquisition.com/post/the-thing-remastered-trust-issues-review]
  - Blood test kits are scarce; testing a squadmate reveals infection; testing yourself proves you're human and raises
    their trust. Trust and fear meters per squadmate.
  - Criticism: a passed test didn't guarantee safety; turns often followed the script, not the system.
  - [read] The choice is *whom to test* with few tests; a test that lies or a turn the rules didn't cause feels unfair.
- **Zombie Panic! Source** [source: https://wiki.zombiepanicsource.com/Zombie,
  https://zombiepanic.fandom.com/wiki/Infection?oldid=8267]
  - Infection is invisible to survivors; players agree on signals (flicker a flashlight) and suspect anyone who
    stops; "kill off those who are infected before they can turn".
  - [read] When the sign is invisible, players invent rituals and kill early on suspicion.
- **Barotrauma** (co-op sub crew) [source: https://www.barotraumagame.com/wiki/Affliction,
  https://www.yekbot.com/barotrauma-the-medical-doctors-guide/, https://itemlevel.net/?p=15485]
  - A medic role with a health scanner: hover over a crewmate and see what's wrong as icons; the health screen lists
    treatments ranked by how much they heal.
  - Guides call medicine complex for new players and the medic "one of the harder classes".
  - [read] The tool names the answer; the work is treatment and logistics, not deduction.
- **Space Station 13** [source: https://wiki.novasector13.com/wiki/Medical_Doctor]
  - Hit someone with the health analyzer, get a readout of what's wrong. Same shape as Barotrauma.
- **Lethal Company, the Masked** [source: https://primagames.com/?p=218078, https://gamertweak.com/?p=291689]
  - A look-alike of a player. Tells: the mask stuck on the face, the eyes, the scanner can't scan it; voice callouts.
  - [read] A few big physical tells, learned in one encounter.

### Evidence puzzles (combine clues)
- **Phasmophobia** [source: https://primagames.com/gaming/how-to-gather-evidence-in-phasmophobia-and-use-it-to-identify-ghosts,
  https://cyanideronin.substack.com/p/phasmophobia-is-hauntingly-complex, https://vaporlens.app/app/739630/phasmophobia]
  - Each ghost = 3 pieces of evidence from a shared pool, found with tools (EMF, spirit box, thermometer); a journal
    crosses out what can't match. Wrong guesses allowed; failure is information. Some evidence shows only to a lone
    player (splits the party).
  - Complaint in review summaries: evidence unclear, so identification is "too easy or nearly impossible".
  - [read] The ghost stays in its room for minutes; the puzzle object holds still while you examine it.
- **Keep Talking and Nobody Explodes** [source: https://en.wikipedia.org/wiki/Keep_Talking_and_Nobody_Explodes,
  https://gamedeveloper.com/design/finding-the-fun-in-bomb-defusal-with-i-keep-talking-and-nobody-explodes-i-,
  https://mechanicsofmagic.com/2022/04/14/competitive-analysis-keep-talking-and-nobody-explodes/]
  - One player sees the bomb, the others hold the manual; the fun is describing what you see. Criticism: the manual
    holders who know it best dominate the talk.
- **Town of Salem, Investigator** [source: https://gamepretty.com/town-of-salem-will-formats-and-investigator-results/,
  https://commonsensegamer.com/town-of-salem-2-investigator-role-guide/]
  - A check returns a short list ("one of these 3 roles"); results narrow as fewer roles are left; disguises fool it.
  - [read] Ambiguity works when the message itself is plain: a list, not a % table.
- **Deception: Murder in Hong Kong** [source: https://www.shutupandsitdown.com/review-deception-murder-in-hong-kong]
  - One player knows the answer and may only point at clue tiles; the others deduce. (Mysterium works the same way
    with picture cards [memory].)

### Single-player inspection games (for how a sign reads)
- **Quarantine Zone: The Last Check** [source: https://pcgamer.com/games/sim/quarantine-zone-the-last-check-review,
  https://game8.co/articles/reviews/quarantine-zone-the-last-check-review,
  https://insider-gaming.com/quarantine-zone-the-last-check-symptoms-explained/,
  https://vaporlens.app/app/3419520/quarantine_zone_the_last_check]
  - A symptom table: some symptoms mean "possibly infected", some (bite marks, red eyes) mean "infected"; tools
    (thermometer, X-ray) reveal more. Praised: "clever and grisly medical examination". Complaints: "unclear and
    inconsistent symptoms", tools glitch, repetitive.
- **That's Not My Neighbor** [source: https://knowyourmeme.com/memes/subcultures/thats-not-my-neighbor-see-my-name-on-the-list-right,
  https://nachogames.itch.io/thats-not-my-neighbor/comments?after=2947]
  - Compare a visitor with a reference file and spot the difference. Players complain some differences are too
    subtle to see even on replay.

## Patterns
1. **Three shapes of "who knows"** [read]:
   - *The patient knows* (No More Room in Hell 2): the drama is telling or hiding, and curing in time.
   - *A tool knows* (Barotrauma, SS13, The Thing): the drama is who gets the scarce test or treatment.
   - *Clues must be combined* (Phasmophobia, Keep Talking, Town of Salem, Quarantine Zone): a puzzle with a
     reference (journal, manual, table).
2. **Signs that work are big and physical:** a mask on the face, a cough you can hear, red eyes, bite marks
   [source: Lethal Company, NMRiH2, Quarantine Zone]. Subtle signs are the most common complaint in every inspection
   game found [source: Quarantine Zone, That's Not My Neighbor, Phasmophobia summaries].
3. **The sick player's own screen tells them, stronger each stage** [source: NMRiH2]; friends notice through sound
   (the cough over voice).
4. **The cure is a short physical procedure with a wait** (draw blood, 30 s, inject) **and there's a way to buy
   time** (pills) [source: NMRiH2].
5. **A scarce test makes the choice** (whom to test; test yourself to earn trust) [source: The Thing].
6. **Invisible infection breeds rituals and early killing** [source: Zombie Panic].
7. **Puzzle-style diagnosis works when the subject holds still** (a ghost in its room for minutes, a bomb on a
   table, a person at a checkpoint) [read].
8. **A reference holder can become the boss of the talk** [source: Keep Talking criticism].

## Anti-patterns
- Unclear or subtle signs (Quarantine Zone, That's Not My Neighbor, Phasmophobia) [source].
- Diagnosis complex enough to need a class of its own (Barotrauma's medic) [source].
- A test or turn that ignores the rules (The Thing's scripted turns) [source].
- The manual holder runs the crew (Keep Talking) [source].

