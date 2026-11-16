# Escape rooms: patterns and anti-patterns

What makes a real-world (and video-game) escape room good or bad, mapped to our game. Written
2026-11-06 after the user said: "this game is basically a scape room but friendslop.. could you
research what makes a scape room good and what makes one bad.. research patterns and
antipatterns". Companion to `docs/discovery-patterns.md` (hidden method, hooks, moon logic),
which this doc does not repeat.

Each entry: **Rule** (the pattern, with source) · **Us** (where it shows up here). Tags:
*[source]* = backed by a linked source; *[read]* = checked in our docs this session;
*[opinion]* = design judgment, not checked.

## Terms
- **Gate**: anything the team must open or pass (a lock, a door, a puzzle). Escape room flow is
  a graph of gates and the clues that open them ([Codex: the player loop](https://thecodex.ca/?p=2924)). *[source]*
- **Player loop** (Elumir): identify gates → collect clues → pick a gate → solve it (the *aha*)
  → complete it (the *process*) → input the answer → repeat. Teammates can be on different steps
  ([Codex](https://thecodex.ca/?p=2924)). *[source]*
- **Aha vs process**: *aha* is working out how a puzzle works; *process* is the labour of
  carrying it out once you know (turning screws, entering digits). *[source, same]*
- **Game master (GM)**: the staff member who watches the team and gives hints. In our game the
  **narrator** sits in this seat. *[opinion]*
- **Bottleneck / choke point**: a moment where all progress goes through one gate. Good at the
  finale, bad mid-game ([CTU Prague lecture, Matoušek](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)). *[source]*
- **Red herring**: anything misleading. Room Escape Artist counts it whether or not the designer
  meant it ([REA: red herrings](https://roomescapeartist.com/2019/02/10/red-herrings/)). *[source]*
- **Climactic moment**: one unmissable, surprising high point near the end that players retell
  ([REA](https://roomescapeartist.com/2016/04/07/room-escapes-need-climactic-moments)). *[source]*

## Is it really an escape room?
Half. Matches: a clear goal (escape), a shared room, a hidden method, a GM who watches and talks,
a ticking threat (the ceiling). Differences that matter:
- **Escape rooms are played once.** Only a quarter of enthusiasts ever replayed a room
  ([2017 enthusiast survey, n=250](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
  We are built for ~3–5 runs per crew and more after (pillar 3). A solved escape-room puzzle is used
  up; ours must survive being known (see discovery anti-pattern 5). *[read + opinion]*
- **Escape rooms are mostly authored puzzles; ours is mostly a shifting toy** (moods, chores,
  exams) with hand-made mysteries on top. *[read]*
- **Escape rooms reward cooperation only; friendslop also needs the goat.** Getting a friend
  caught is part of the fun (blame, selling a friend). *[read]*

So take from escape rooms: goal clarity, flow, GM craft, hints, feedback, climax, group sizing.
Don't take: one-shot puzzles, searching, 60-minute length. *[opinion]*

## The one-line diagnosis
In the survey, what made best rooms best and worst rooms worst was the same thing, mentioned far
more than anything else: **game and puzzle design / flow** (147 best, 155 worst mentions), then
GM quality, then immersion and set ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
Bad rooms waste the team's time on things that aren't thinking (searching, tedium, broken props,
red herrings, idle bodies); good rooms keep every head busy on a fair *aha* and end on a high.
*[source + opinion]*

## Patterns (do)

### 1. More open gates than players
- **Rule:** start with more active puzzles than players so everyone has something; let them
  funnel down to fewer and end on one ([REA: players per room](https://roomescapeartist.com/2015/06/25/players-per-escape-room/)).
  Strictly linear rooms leave "part of team… bored"; branch to keep everyone busy, use linear parts
  for story ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)). *[source]*
- **Us:** chores run beside the button (one slot at 2–3 subjects, two at 4–8), items and routes
  are side gates. *[read]* Gap: stage 1 is silent with only the button, so 8 players get one verb
  for its first minute. Everyone can press at once, so it is not a padlock queue, but there is
  only one thing to *think* about. Fine as a warm-up if it is short. *[opinion]*

### 2. Every player gets a hero moment
- **Rule:** groups form a pecking order within minutes and the confident ones take over;
  Sherlocked designs so "everybody at some point can feel like the hero", with puzzles for
  different thinking styles, and solo so nobody hands it over
  ([Sherlocked](https://www.sherlocked.nl/blog/player-focused-escape-room-puzzle-design)). *[source]*
- **Us:** chores take 1–2 bodies off the button, exams in the dark ask "who can see?", private
  realities pick one player. *[read]* Friendslop twist: the moment can be a hero *or* goat moment
  (blame), and both count. *[opinion]*

### 3. Ask "why is this here?" of every element
- **Rule:** Nicholson: every puzzle, item and prop should have a reason inside the room's story;
  the opposite is "escape room logic" (a digital clock in a Victorian room, padlocks in a tomb),
  and inconsistency is "the bane of escape rooms"
  ([Meaningful Play 2016 paper](https://meaningfulplay.msu.edu/proceedings2016/abstract.php?paperid=29);
  [Tampere PlayLab](https://blogs.tuni.fi/playlab/features/inconsistency-is-the-bane-of-escape-rooms/)).
  Immersion through a cohesive theme/story/puzzles was the 2nd most mentioned trait of best rooms
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** our "why" is one sentence: *a narrator runs a test on you and is a troll about it.* A
  gelato machine, a squeaky hammer, a decoy button all pass that test if the narrator plausibly put
  them there to mess with the crew. Anything that only exists "because games have that" fails. *[opinion]*

### 4. The GM is a character, heard but not seen
- **Rule:** enthusiasts' most preferred hint channels were in-room video and in-room audio; the
  most hated were a GM entering or standing in the room
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)).
  A disembodied "God mic" works when the GM can act and the speaker sits in an in-world object
  ([REA: hint systems](https://roomescapeartist.com/2019/10/24/escape-room-hint-systems/)).
  Nicholson flags the out-of-story GM ("the guy who runs this game") as a consistency break
  ([Tampere PlayLab](https://blogs.tuni.fi/playlab/features/inconsistency-is-the-bane-of-escape-rooms/)). *[source]*
- **Us:** the narrator is exactly the in-character God mic, and its memory (pillar 4) is what the
  best GMs do: read the room. *[read + opinion]* Keep it a voice; never give it a body that walks in.

### 5. Read the room: hints by need, without penalty
- **Rule:** two thirds of enthusiasts want to *ask* for hints; they dislike hint penalties and
  prefer more hints ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)).
  "Do not let any team sit and stew for too long"; a GM's judgment is the best trigger when the GM
  is attentive; timed hints drag slow teams and repeat known info; a reader: "DON'T hard-limit
  hints" ([REA: hint systems](https://roomescapeartist.com/2019/10/24/escape-room-hint-systems/)).
  Automated hints pushed mid-solve made reviewers "rushed and annoyed"
  ([REA review](https://roomescapeartist.com/2017/07/21/outin60-insane-asylum-review/)). *[source]*
- **Us:** hints are two fixed flashlight writings per run, plus one more after a loss. *[read]*
  That is a timed/fixed system, the kind that can't tell a stuck crew from a busy one. An
  ask-for-help verb is parked in `docs/questions.md`. *[opinion]*

### 6. Feedback is never in doubt
- **Rule:** "there should never be uncertainty as to whether a puzzle has been solved"; small
  light/sound cues confirm right steps and flag wrong ones, stronger the further players stray
  ([Game Developer: guiding player interactions](https://gamedeveloper.com/design/-quot-i-can-t-see-what-i-have-to-do-quot---guiding-player-interactions-in-escape-room-games)).
  Sound should be background for mood and foreground for information: "you want players to hear
  locks unlocking" ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)). *[source]*
- **Us:** a mood's refused hit is a dead clack, a let-through scores ×3 with a number pop. *[read]*
  That is the right shape: right and wrong sound different.

### 7. Important things look important; affordances are honest
- **Rule:** use light and sound to point at key objects, remove or clearly mark irrelevant ones,
  prefer a *directed* search (players know what they're looking for, so it can end). False
  affordances (a handle on a fixed panel) frustrate like red herrings; hidden ones should be
  "discoverable but non-obvious", or players brute-force
  ([Game Developer](https://gamedeveloper.com/design/-quot-i-can-t-see-what-i-have-to-do-quot---guiding-player-interactions-in-escape-room-games)). *[source]*
- **Us:** the blank room is a gift here: few props, each stands out. The weak west panel is a
  hidden affordance; it needs a visible tell (a seam, a different tone when hit) besides the
  flashlight hint. *[opinion]*

### 8. Puzzles that need talking (asymmetric information)
- **Rule:** We Were Here splits two players so each sees what the other can't, and makes puzzles
  "extra hard" to describe, on purpose ([Escapist](https://www.escapistmagazine.com/?p=43661);
  [Game Developer: Road to the IGF](https://www.gamedeveloper.com/game-platforms/road-to-the-igf-total-mayhem-games-i-we-were-here-i-)).
  In an AR escape room study, successful pairs read the uneven information *as* the cue to
  cooperate ([ARctic Escape, arXiv](https://arxiv.org/pdf/2503.06345)). *[source]*
- **Us:** exams in the dark (one sees, others act) and private realities already do this. *[read]*
  It is the strongest friendslop fit in the whole field: talking is the gameplay, and botched
  descriptions are funny. *[opinion]*

### 9. End on a climactic moment
- **Rule:** players "forget nearly everything about your room" except one surprising, dramatic,
  unmissable moment near the end, and "the climactic moment markets itself"
  ([REA](https://roomescapeartist.com/2016/04/07/room-escapes-need-climactic-moments)). "Have a
  climax / finale" ([REA dos and don'ts](https://roomescapeartist.com/2016/07/17/the-room-escape-artist-dos-and-donts/)).
  The finale should have room for everyone to watch ([REA: players per room](https://roomescapeartist.com/2015/06/25/players-per-escape-room/)).
  Surprises, wow moments and secret rooms show up in the survey's best rooms
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** the routes have them (tractor beam, narrator stops mid-word, counter wraps). *[read]*
  The main Escape ending (count hits 1B) may be the weakest; for a streamed demo the clip is the
  trailer. *[opinion]*

### 10. Bonus secrets for the keen
- **Rule:** "extra bonus items/puzzles" was the enthusiasts' most preferred uncommon element
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** matches the Fantasy's "full of mysteries; a stream spoils only a fraction". *[read]*

## Anti-patterns (don't)

### 1. Don't slow players with tedium
- **Rule:** "Slow us down with more puzzles. Don't slow us down with tedium"; don't add process
  (more screws, more rings), don't make the answer input the challenge ([Codex](https://thecodex.ca/?p=2924)).
  "Don't make puzzles feel like homework", "don't make clue collecting tedious"
  ([REA dos and don'ts](https://roomescapeartist.com/2016/07/17/the-room-escape-artist-dos-and-donts/));
  "searching through all books in a library isn't fun" ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)). *[source]*
- **Us:** this is the premise risk: **pressing 1B times is pure process.** The design already
  answers it (a bare hand stays +1, sensitivity scales items, the real play is moods, chores and
  routes). *[read]* The test: a crew should never feel the count is the work. *[opinion]*

### 2. Don't put things in the room that lie
- **Rule:** fake puzzles are "demoralizing"; irrelevant cool objects are the most frustrating kind;
  "Escape rooms should not punish people for exploring interesting things"; Harshbarger: "I never
  design with red herrings. The players will create their own"
  ([REA: red herrings](https://roomescapeartist.com/2019/02/10/red-herrings/)). "The players are
  clueless already, don't make it worse" ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)).
  Too many red herrings is a named cause of worst rooms, and experienced players dislike them more
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** the decoy and cursed buttons are deliberate lies, but they *do* something when used
  (they are the narrator's prank, not dead ends). Rule for us: every odd thing answers when
  touched; nothing is inert decoration that looks like a clue. *[opinion]*

### 3. Don't make one gate hold the whole team
- **Rule:** "watch out for clue bottlenecks" ([REA](https://roomescapeartist.com/2016/07/17/the-room-escape-artist-dos-and-donts/));
  idle players often want to join but don't know what to do
  ([Nowescape](https://blog.nowescape.com/author/jeffimmersivetech-co/)); "insufficient puzzles
  for the group size" is a named worst-room cause ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** exams are choke points by design (fine: they gate milestones, like a finale). *[read]*
  Watch for a crew of 6–8 where the exam needs 2 and the rest stand in the dark with nothing. *[opinion]*

### 4. Don't scale up the headcount without scaling the design
- **Rule:** enthusiasts' ideal team is 4 (mean 4.27), experienced players want smaller
  ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf));
  "communication breaks down exponentially as a function of team size"
  ([REA](https://roomescapeartist.com/2015/06/25/players-per-escape-room/)). Escape Simulator
  recommends 2–3; its sequel allows 8 but a 4-player review found it "chaotic" and not designed for
  co-op ([Checkpoint review](https://checkpointgaming.net/reviews/2025/10/escape-simulator-2-review-a-puzzling-co-op-experience/);
  [Escape Roomer](https://theescaperoomer.com/escape-simulator-review/)). *[source]*
- **Us:** we sell 2–8 and tune for 2–4. *[read]* Friendslop chaos is wanted where escape rooms
  avoid it, but 8 needs its own playtest, not an assumption that 4 scales. *[opinion]*

### 5. Don't make the game master a buzzkill
- **Rule:** 79 worst-room mentions were customer service, 56 of them bad game mastering:
  inattentive, unenthusiastic, poor hinting ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** a narrator who repeats lines, talks over thinking, or ignores what the crew just did is
  the bad GM. Memory says: no noise lines; every line must matter for play. *[read]*

### 6. Don't fill the air with noise
- **Rule:** "Don't make the room constantly noisy… the environment shouldn't hinder player
  communication"; an annoying sound only if players can silence it; noisy rooms appear among worst
  experiences ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf);
  [survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)). *[source]*
- **Us:** friendslop runs on voice chat. Chore alarms and the narrator compete with friends
  talking; an alarm should be the *chore's* fault, silenced by fixing it. *[opinion]*

### 7. Don't let luck decide the answer
- **Rule:** "random elements" tied with an in-room GM as enthusiasts' most hated uncommon element,
  more so for experienced players ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf)).
  The survey does not define the term. *[source]*
- **Us:** we randomise *which* moods appear and their colours. *[read]* Rule: randomise the draw,
  never whether a correct action works. *[opinion]*

### 8. Don't require outside knowledge
- **Rule:** outside knowledge was the *least* allowable trope in the survey; "Don't require outside
  room knowledge and cultural references" ([survey](https://thecodex.ca/wp-content/uploads/2017/09/2017EscapeRoomEnthusiastSurveyV1.1.pdf);
  [CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf)). *[source]*
- **Us:** jokes can reference anything; solutions can't. *[opinion]*

### 9. Don't repeat the same puzzle type
- **Rule:** "Solving tenth crossword isn't fun"; too many of the same lock is a named mistake
  ([CTU](https://courses.fit.cvut.cz/NI-ESC/lectures/files/esc-room-design.pdf);
  [REA](https://roomescapeartist.com/2016/07/17/the-room-escape-artist-dos-and-donts/)). *[source]*
- **Us:** the five kinds of moment each ask a different question, and mysteries must be different
  formulas. *[read]* Already a rule; this backs it.

### 10. Don't ship a puzzle most teams need a hint for
- **Rule:** "If a puzzle almost always requires a hint, it's not hard; it's broken. Fix it"; over
  50% hint rate means refine it ([REA: hint systems](https://roomescapeartist.com/2019/10/24/escape-room-hint-systems/)).
  Sherlocked: "We don't design for you to feel dumb"; aim for "just frustrated enough that you feel
  the big win" ([Sherlocked](https://www.sherlocked.nl/blog/player-focused-escape-room-puzzle-design)). *[source]*
- **Us:** a playtest metric: for each mood and route, how many crews cracked it unhinted. *[opinion]*

## Checklist for any new room element, puzzle or event
1. **Why:** does the narrator-runs-a-troll-test story explain why it's here?
2. **Hands:** at 2, 4 and 8 players, does everyone have something to do while it runs?
3. **Hero/goat:** does it give one player a moment of their own?
4. **Aha, not process:** is the challenge in figuring it out, not in repeating it?
5. **Feedback:** is right vs wrong unmistakable by sound and light?
6. **Honest:** if it looks like a clue, does it answer when touched?
7. **Talk:** does it make the crew talk (ideally, one knows what another can't)?
8. **Quiet:** can friends still hear each other while it runs?
9. **Fair:** no luck in whether the right action works, no outside knowledge?
10. **Peak:** if it's an ending, is there one unmissable, clip-worthy moment everyone sees?

## Gaps in this research
- Elumir's "13 rules" post itself was not reached; only secondary mentions (fairness, consistency,
  "beta test and iterate", ~5 minutes per puzzle).
- Nicholson's 2016 paper text and his 2015 facility survey were read only via abstracts and summaries.
- The 2017 survey is enthusiasts only (median 25 rooms), not typical players; it says so itself.
- Most other sources are operator blogs and reviews: practitioner opinion, not studies.
- Nothing found on escape rooms built for *replay*, or that reward sabotage; that part of our
  design is our own ground (see `docs/gameplay-anti-patterns.md` for trolling).
