# Gameplay anti-patterns: rules, rewards and the crew

Gameplay mistakes to avoid for a co-op friendslop party game: 2–8 friends, one shared goal, a
shared wallet, a narrator who changes the rules, minigames, a falling ceiling. Written 2026-11-03
after the user asked what the gameplay anti-patterns are for this game and genre. Companion to
`docs/ui-ux-anti-patterns.md` (feel and interaction); this file is about rules and incentives.

Each rule: **Don't** (the anti-pattern) · **Evidence** (where it is documented) · **Us** (where it
shows up in this prototype) · **Do** (the alternative, with an example).

Tags: *[source]* = backed by a linked source; *[read]* = checked in our code this session;
*[opinion]* = design judgment, not checked.

## The one-line diagnosis
Friendslop works when **mistakes are the content and everyone is in the mess together**:
"Playing well helps, but playing badly is even better", and "mistakes turn into stories, mostly
full of yelling, laughter, or both"
([AppMagic: Friendslop happened](https://appmagic.rocks/blog/friendslop-steam-games-2025)).
PEAK's lead calls the game a "scaffold to goof around with your friends"
([Inverse interview, Nick Kaman](https://www.inverse.com/gaming/peak-steam-landcrab-friendslop-update-interview-nick-kaman-pc)).
Every anti-pattern below either takes a friend out of the mess, lets one player or one machine
solve it, or makes the mess stop being funny. *[source]*

---

## 1. Don't let one player run the team
- **Evidence:** the "alpha player" or quarterbacking problem: one player takes implicit control of
  the team's decisions, and co-op games invite it because it gives the best chance to win
  ([Don't Eat the Meeples](https://donteatthemeeples.substack.com/p/mitigating-quarterbacking-cooperative-games),
  [Justin Gary](https://justingarydesign.substack.com/p/the-quarterback-problem)). Pandemic's
  designer Matt Leacock names hidden information and time pressure as fixes; one writer argues
  real-time play is the only sure cure
  ([Meeple Mountain](https://www.meeplemountain.com/articles/benching-the-quarterback-how-to-deal-with-alpha-players-in-co-op-games/)).
  Some designers say the real cause is a skill gap
  ([Keith Burgun](https://keithburgun.net/why-quarterbacking-isnt-a-problem-in-cooperative-games/)).
  In video co-op: Lovers in a Dangerous Spacetime's team saw "the experts ordered the other person
  around" ([Game Developer](https://gamedeveloper.com/design/co-op-communication-in-i-lovers-in-a-dangerous-spacetime-i-));
  Game Maker's Toolkit calls it "First to Fun": the fastest or most skilled player reaps the rewards
  (GMTK, "How Overcooked's Kitchens Force You to Communicate", seen only in search snippets).
  *[source]*
- **Us:** the game is real-time, which helps. But blackout minigames take presses from anyone, so
  one fast player can answer for everyone; that is why the hog callback exists (now super rare:
  80% of 40+ minigame presses) *[read]*. Whether one player can also carry pressing mode alone is a
  playtest question *[opinion]*.
- **Do:** jobs that need several bodies in different places at the same moment (unplug the machines
  *while* someone presses; "everyone press together"; "everyone stand next to Bo"). Real-time
  pressure does the rest.

## 2. Don't take players out of play
- **Evidence:** player elimination forces downtime on the players who are out, worst when it
  happens early ([Game Design Patterns: Player Elimination](https://math.vu.nl/~eliens/demo/pattern-playerelimination.html),
  [Early Elimination](https://math.vu.nl/~eliens/demo/pattern-earlyelimination.html)).
  Jackbox keeps everyone acting: one task at a time, always aware of what to do next
  ([Built In: the Jack Principles](https://builtin.com/media-gaming/jackbox-games-design-party-pack)).
  *[source]*
- **Us:** the arm holds the hog in place for 25 s; the user kept it but made it super rare
  (2026-11-03) *[read]*. Blackout minigames give non-pressers nothing to do while others answer
  *[opinion]*.
- **Do:** punish by changing *how* someone plays (reversed controls, the cone, a nickname), not
  *whether* they play. Keep any hold short and rare.

## 3. Don't let automation make the players irrelevant
- **Evidence:** idle games question the usual link between games and agency
  ([Interpassivity and the Joy of Delegated Play in Idle Games, ToDiGRA](https://todigra.org/index.php/todigra/article/view/1754),
  [Playing to wait: a taxonomy of idle games, CHI 2018](https://research.monash.edu/en/publications/playing-to-wait-a-taxonomy-of-idle-games/)).
  The genre's most persistent criticism: "Once the automation upgrades kick in, a player stops
  doing much of anything"
  ([Tech Times](https://www.techtimes.com/articles/325200/20260821/planet-harvester-inverts-idle-loop-you-drive-drones-handle-everything-else.htm)).
  *[source]*
- **Us:** the shop sells four auto-pressers (Drinking Bird, Hamster Wheel, Robot Arm, Cannon)
  *[read]*. Rewards are no longer machines or upgrades (user, 2026-11-03) *[read]*. In stage 3,
  machines may out-press hands *[opinion]*.
- **Do:** machines are a liability as much as an asset: rule flips make them cost points, fires
  make them explode, boxes jam them. Every machine should create a job for a human hand.

## 4. Don't let a lead or a loss compound
- **Evidence:** positive feedback loops magnify early decisions and make a match feel predetermined;
  the usual fixes are catch-up mechanics, caps, or short matches
  ([Bugnet: feedback loops](https://bugnet.io/blog/positive-and-negative-feedback-loops-in-game-design),
  [TUKE lecture: feedback loop](https://kurzy.kpi.fei.tuke.sk/gamedev/en/lectures/feedback-loop.html)).
  Mario Kart's rubber-banding is the classic negative loop. *[source]*
- **Us:** fixed on 2026-11-03: a lost minigame used to speed the ceiling up ×1.35, stacking to 3×;
  now it drops once by 10% and never below 5%. Rewards no longer raise the earning rate (no free
  upgrades, cursed bonus lasts 30 s, not the run) *[read]*. Fines are a share of the wallet, so
  they scale but do not compound *[read]*.
- **Do:** rewards and punishments change the moment (points, ceiling time, a short effect,
  something social), never the crew's rate for the rest of the run (`docs/gameplay-design.md`).

## 5. Don't leave a dominant strategy
- **Evidence:** "Given the opportunity, players will optimize the fun out of a game"
  ([Soren Johnson, Water Finds a Crack, 2011](https://www.designer-notes.com/?p=369)). A dominant
  strategy removes choice, and repetitive low-risk tactics drain the fun. *[source]*
- **Us:** in pressing mode, mashing the button is the default answer. Rule flips, decoys, orders
  ("hands off", "touch a wall") and Bro Science rules exist to break it *[read]*. Whether they break
  it often enough is a playtest question *[opinion]*.
- **Do:** make the obvious move wrong at unpredictable times, and make the switch readable (sound,
  light) so being caught out is funny, not unfair.

## 6. Don't let luck decide who wins
- **Evidence:** Mario Party's end-of-game bonus stars are a long-running complaint: luck overrides
  skill ([Worthplaying, Mario Party 8 review](https://worthplaying.com/article/2007/6/17/reviews/42800-wii-review-mario-party-8/),
  [Expert Beacon](https://expertbeacon.com/why-is-mario-party-so-infuriating/)). A counterpoint:
  the stars are usually predictable, and some reward minigame skill
  ([Brandon the Game Dev](https://brandonthegamedev.com/5-lessons-from-mario-party-for-board-game-developers/)).
  *[source]*
- **Us:** Greedy's hidden 20% ("the button lies") and Bro Science's placebo rules are hidden
  chance *[read]*. Both are one-off and story-sized *[opinion]*.
- **Do:** chance that makes a story ("the button lied to Bo"), never chance that decides the run.
  Hidden odds stay small and rare.

## 7. Don't punish without a culprit
- **Evidence:** friendslop humor comes from mistakes with a face ("mistakes turn into stories",
  [AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)). Jackbox's design aims at
  getting "the group to laugh" and responding to each player's specific choices
  ([Built In](https://builtin.com/media-gaming/jackbox-games-design-party-pack)). *[source]*
  That a named culprit is funnier than a crew-wide loss is *[opinion]*.
- **Us:** a lost minigame drops the ceiling for everyone with nobody named; the −15% stake hits
  the whole crew *[read]*. Already in `docs/todo.md`.
- **Do:** the narrator names who failed ("Bo pressed on red. The ceiling thanks Bo."), and personal
  stakes land on that person. The minigame must make a culprit possible in the first place (rule
  12), and the blame must stay cheap (rule 13).

## 8. Don't allow trolling with no comeback
- **Evidence:** griefing (ruining the game for others rather than winning) is worst on shared
  resources; fixes include protecting resources and giving the victim a response
  ([Inverse: griefing](https://www.inverse.com/gaming/griefing-meaning-online-video-games-overwatch-counterstrike),
  [Klei forums: preventative griefing](https://kleiforums.com/forums/topic/132086-preventative-griefing-solutions/)).
  Alan Meades' *Understanding Counterplay in Video Games* (Routledge, 2015) studies grief play;
  only its contents page was checked. *[source]*
- **Us:** anyone can spend the shared wallet ("who spent 50k on a disco ball?!" is a design joke),
  and nothing lets the crew stop or punish a spender beyond the narrator's "Big Spender" callout
  *[read]*. Slaps have counterplay (slap back) *[opinion]*.
- **Do:** keep the trolling, add the comeback: the spender is named on the spot, and the crew can
  get even (slap, potato, blame).

## 9. Don't pile up rules faster than people can follow
- **Evidence:** Jackbox: "The games never ask players to make multiple choices in a given moment";
  one task at a time, players always aware of what to do next
  ([Built In](https://builtin.com/media-gaming/jackbox-games-design-party-pack)). PEAK's team:
  "text is evil" ([Inverse](https://www.inverse.com/gaming/peak-steam-landcrab-friendslop-update-interview-nick-kaman-pc)).
  Friendslop players "didn't need to fully understand the game to have fun"
  ([AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)). *[source]*
- **Us:** stage 3 lets orders land on top of pressing events (`docs/mvp.md`) *[read]*.
- **Do:** one active rule at a time, announced by sound and light. Chaos comes from people
  colliding, not from a rule stack.

## 10. Don't let variety be oatmeal, or lines repeat
- **Evidence:** Kate Compton's "10,000 bowls of oatmeal": generated items can be mathematically
  distinct and still look the same; the test is *perceptual uniqueness*
  ([Emily Short: Bowls of Oatmeal and Text Generation](https://emshort.blog/2016/09/21/bowls-of-oatmeal-and-text-generation/)).
  Valve's dynamic dialog matches world facts against thousands of lines so speech fits the moment
  ([Elan Ruskin, GDC 2012](https://www.gdcvault.com/play/1015528/AI-driven-Dynamic-Dialog-through),
  [Valve Response System](https://developer.valvesoftware.com/wiki/Response_System)); how it avoids
  repeats was not found in this search. *[source]*
- **Us:** `docs/gameplay-design.md` plans ~30 templates × modifiers for 1,000+ events *[read]*. The size of
  the narrator's line pools was not checked this session.
- **Do:** fewer, hand-made events that each feel different; narrator lines tied to real facts
  (names, numbers), each with a "said already" limit.

## 11. Don't make the session too long to lose
- **Evidence:** friendslop is built "for a few intense sessions", and "almost all progress happens
  inside a single run" ([AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)).
  Long waits after an early loss are what make elimination hurt
  ([Early Elimination pattern](https://math.vu.nl/~eliens/demo/pattern-earlyelimination.html)).
  *[source]*
- **Us:** the target run is 30–45 min (`docs/gameplay-design.md`) *[read]*. Losing at minute 40 costs far
  more than losing at minute 5 *[opinion]*.
- **Do:** losses come early and often, or a late loss pays out something (a record, an unlock, a
  story the narrator retells).

---

## Co-op minigames (researched 2026-11-04)
Added after the user's playtest feel: the minigames "doesnt feel fun.. and they are not able to tell
who to blame" (user, 2026-11-04). Scope: full co-op minigames, no PvP. The positive formula, as
Claude's synthesis *[opinion]*: one simple verb + players need each other + time pressure that
makes people talk + a failure caused by one visible person, shown physically, quick to retry.

## 12. Don't run solo tests side by side
- **Evidence:** in co-op pattern research, closely coupled patterns (my action depends on yours)
  have the greatest effect on player experience; combining patterns added nothing measurable, in a
  few prototypes ([Bunker & Ryan, AUC 2017](https://auc.edu.au/2017/11/combining-cooperative-design-patterns-to-improve-player-experience/);
  pattern list incl. complementary roles, shared puzzles, encrypted information, in a
  [Chalmers thesis](https://odr.chalmers.se/items/7c133781-5540-46ab-8f25-399686df9b9b/full)).
  The co-op hits split something between players: information (Keep Talking: the defuser sees the
  bomb, the experts hold the manual, [GDC 2016](https://gdcvault.com/play/1023113/Designing-Asymmetric-Gameplay-For-Keep);
  Spaceteam: your instruction shows on someone else's screen, and the shouting was not planned,
  [Wikipedia](https://en.wikipedia.org/wiki/Spaceteam)) or roles through the layout (Overcooked:
  one interact button, the kitchen splits the jobs,
  [Super Jump](https://superjumpmagazine.com/overcooked-how-design-creates-teamwork)). Sellers
  calls games where others are present but play is solitary "parallel play"
  ([Game Developer](https://www.gamedeveloper.com/design/psychology-of-play-social-games-and-game-design)).
  *[source]*
- **Us:** green light, reaction, countdown, rhythm, quiz, audio quiz and decoys give every player
  the same information and the same job on one button; the result is pooled (the quiz sums the
  crew's presses) *[read, docs]*. So nobody needs anyone, and no single press causes the loss
  *[opinion]*.
- **Do:** each minigame splits something. Information: only the players away from the button see
  the signal, the one at the button presses blind ("NOW!"). Order: presses must come from different
  players in a sequence. Joint action: one holds the button down while another hits a target. The
  split makes a culprit exist by construction.

## 13. Don't make blame expensive
- **Evidence:** Michael Parker's team-mechanics rules: "Teams should never be better off without a
  player, no matter how bad he is"; make small failures common so success stands out; and make the
  "correct" action hard to calculate, so nobody can be blamed for missing it
  ([Game Developer, 2012](https://www.gamedeveloper.com/design/designing-multiplayer-team-based-mechanics-without-adding-frustration)).
  An arcade co-op editorial: on a shared pool of lives, a weaker player who dies often "is entirely
  capable of torpedoing their entire team's chances at fun"
  ([Co-Optimus](https://co-optimus.com/editorial/976/page/3/indie-ana-co-op-and-the-dev-stories-you-re-all-in-this-together.html)).
  A small Overcooked 2 study (N=23, work in progress): with an incompetent teammate, players
  strategised less, and interviews pinned frustration on the teammate more than the game
  ([arXiv 2025](https://arxiv.org/html/2508.19230v1)). *[source]*
- **Tension with rule 7:** friendslop wants a culprit; Parker warns against one. Reading
  *[opinion]*: blame for a visible slip (pressed on red, dropped the cannon) is a joke; blame for a
  wrong choice someone could have calculated becomes shaming and quarterbacking.
- **Us:** moving the −15% stake onto the culprit (`docs/todo.md`) is the right direction, but a
  weak player could then lose every minigame for the crew and get every punishment *[opinion]*.
- **Do:** blame lands on slips, not on choices. The punishment is moment-sized and funny (the cone,
  a nickname, the spotlight), never a share of the run. Rotate who stands in the culprit seat, so
  the same player isn't on the spot every time.

## 14. Don't hang a minigame on one player
- **Evidence:** "It must be possible to progress even if your teammates are really stupid"
  (Parker, above). If only one player can do an essential action and that player stalls or
  disconnects, the team "is facing a lockout", not a challenge (Parker; same point in
  [Co-Optimus](https://co-optimus.com/editorial/976/page/3/indie-ana-co-op-and-the-dev-stories-you-re-all-in-this-together.html)).
  *[source]*
- **Us:** the blind-presser sketch (rule 12) and solo door rooms put one player at the centre
  *[opinion]*. Online play adds drop-outs and AFK players.
- **Do:** a central role is a seat, not a person: whoever stands at the button is the presser, and
  anyone can step in. The minigame times out to a loss, never a stall.

## 15. Don't assign roles; let position decide them
- **Evidence:** Lovers in a Dangerous Spacetime's biggest design struggle was getting players into
  different roles; what made it coherent was better communication and letting players pick their
  own roles ([Game Developer](https://gamedeveloper.com/design/co-op-communication-in-i-lovers-in-a-dangerous-spacetime-i-)).
  Overcooked changes the layout mid-level and leaves chores (dishes) unowned, so roles keep moving
  ("No YOU wash the plates this time!",
  [Super Jump](https://superjumpmagazine.com/overcooked-how-design-creates-teamwork)). *[source]*
- **Us:** the minigames have no roles yet *[read, docs]*.
- **Do:** roles come from where you stand or what you hold (at the button, at the wall light,
  holding the hammer), so players sort themselves by shouting, and a minigame can move the seats
  halfway through.

## 16. Don't build millisecond timing tests on a player-hosted connection
- **Evidence:** a Mario Party-style game's players found its rhythm and timing minigames "pretty
  unfair" over remote play; the developer's answer was to let players remove them from the rotation
  ([itch.io](https://itch.io/post/9120163)). Latency fixes in shooters (adding delay so all players
  share the same lag) exist because uneven delay gives some players an unfair edge
  ([NVIDIA Research](https://research.nvidia.com/index.php/publication/2026-08_adaptive-time-delay-improving-player-experience-and-fairness-first-person)).
  *[source]*
- **Us:** reaction (everyone within 1.5 s), rhythm (on a metronome), countdown (press at exactly
  10 s) and "everyone press together within 1 s" are judged on the host *[read, docs]*; clients far
  from the host get blamed for lag *[opinion]*. Not measured.
- **Do:** judge timing on the client against its own local cue, with wide windows; prefer tests
  where the slow part is people talking (seconds), not reflexes (milliseconds). A loss blamed on lag
  is a culprit nobody believes.

## 17. Don't make the loss a number on a bar
- **Evidence:** the playbook's clearest review line: "In REPO it feels like it was my fault when I
  fail. Frog Sqwad feels like I fail by some unseen force"
  (`~/Playground/game-design-research/reports/playbook.html`). Friendslop failure is a moment
  "full of yelling, laughter, or both" ([AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)).
  Mario Party's worst minigames are the ones where players "struggle more with controls" than the
  goal ([Gaming Trend](https://gamingtrend.com/reviews/mario-party-10-review/)). *[source]*
- **Us:** a lost minigame drops the ceiling 10% and shows on the display's ceiling bar
  *[read, docs]*; whether the room animates and sounds it is open (`docs/todo.md`).
- **Do:** the loss happens to someone, in the room: the ceiling slams down over the culprit's spot
  first, the eye turns and the spotlight lands, the narrator says the name. Then the next thing
  starts fast.

## 18. Don't let a minigame be a mash
- **Evidence:** an N64-era Mario Party review criticises minigames built on "spinning the analogue
  stick as fast as possible" (seen in a search snippet; which page said it was not confirmed);
  a mash has no decision and no one to talk to *[opinion]*. *[source]*
- **Us:** pressing mode is already the mash; PvP mash and "last one" are mashes in the blackout too
  *[read, docs]*. Fast clicking is allowed up to 60/s, so a drag clicker wins any mash alone
  (`docs/gameplay-design.md`) *[read]*.
- **Do:** a blackout minigame is the break from mashing: the button becomes one careful press, at
  the right moment, by the right person.

---

## Checklist for any new rule, reward or punishment
1. Does it take anyone out of play? For how long?
2. Can one player (or one machine) handle it alone?
3. Does it change the moment, or the rate for the rest of the run?
4. Is there a named culprit, and a comeback for the victim?
5. Is it one rule at a time, announced by sound and light?
6. Does it make mashing wrong sometimes?

For a minigame, also:
7. What does it split between players: information, roles or one joint action?
8. Who exactly caused the loss, and can the room show it (rule 17)?
9. Is the blame for a slip, and is the punishment moment-sized?
10. Does it still work if one player is slow, AFK or 150 ms from the host?

## Gaps in this research
- Friendslop is new and informal; sources are trade press, market analysis and dev interviews, not
  studies. Rules 7, 8 and 11's friendslop claims rest on one market-analysis article.
- Sources on snowballing, griefing and quarterbacking are mostly blogs and forums.
- No direct developer statement found from Lethal Company's or R.E.P.O.'s developers on design
  rules.
- Minigame rules (12–18): no developer source found on co-op *minigames* specifically (Mario Party
  criticism is mostly about luck and controls, not co-op); the rules borrow from co-op games and
  team-mechanics writing. The Overcooked 2 study is N=23 and a work in progress. The latency rule
  rests on one player thread.
- None of this has been tested on our players. The playtest decides.
