# Research log

Design research for Assemblia, with sources. Started from the Dungeon Pets pivot; older pet-game
research is still in the dungeon-pets repo (docs/research.md).

## Playtest: too strong, unreadable, micromanagement (2026-10-31, user playtest)
- **Report:** the player is far too strong and never has to decide anything; too many creatures
  make the screen unreadable; managing each creature one by one is a chore.
- **Underlying problem (assumption, not measured):** all three come from one cause, an
  **unbounded pack**. Power grows with headcount, so taking every creature is always right (no
  decision). Every extra body adds noise on screen and one more thing to manage. Upkeep was meant
  to tax width but is too soft to stop it.
- **Research:** swarm games (Overlord, Swarm) steer the whole group with one input instead of each
  unit; players still lose track when units wander. DCSS's design puts clarity first. Roguelike
  writing: a choice with one dominant answer is a false choice, and a death should trace back to a
  decision.
- **Thesis:** reject every convention. **Antithesis:** breaking everything at once is high risk;
  you can't tell which break fixed or broke what. And the cure for "no decisions" is a convention,
  a hard limit that forces trade-offs. **Synthesis:** break one convention on purpose, fix the
  root with a hard cap, and treat the pack as one unit, not many.

Sources: [Gamewatcher: Overlord review](https://www.gamewatcher.com/overlord/review),
[N4G: Swarm review](https://n4g.com/news/730533/saving-content-swarm-review),
[Bloomwiki: Roguelike design](https://bloomwiki.org/index.php/Roguelike_(Game_Design)),
[Bugnet: roguelike fairness](https://bugnet.io/blog/how-to-make-a-roguelike-feel-fair),
[Wayline: rethinking challenge](https://www.wayline.io/blog/rethinking-challenge-in-roguelike-design).

## Pivot idea: an incremental game with creatures (proposal, 2026-10-31, user idea)
- **User premise:** incremental games have no strategy. **Checked (web):** partly false. Strategy in
  incrementals comes from (1) **formation/composition**: Idle Champions' positional buffs, with no
  single best lineup because the answer depends on the scenario, unlocks and gear; (2) **walls**
  that need a specific setup, not just bigger numbers; (3) **prestige choices**: when to reset
  and what to carry over; (4) **several currencies** that compete for spending. Weak spots: players
  report Idle Champions collapsing into "stack buffs on one carry", and multiplicative buffs stop
  mattering once there are enough of them.
- **Why it fits the playtest:** auto-combat removes the per-creature micromanagement; an abstract
  view removes screen clutter. "Too strong" doesn't go away by itself, though: numbers going up is
  the genre, so strategy has to come from **walls that need composition**, which the existing
  threats/reactions already are.
- **Thesis:** go incremental. **Antithesis:** incrementals drift into waiting and one dominant
  carry build; and dropping the 3D action throws away its controls and art work. **Synthesis:**
  keep threats, reactions, paths and gear as the strategy layer; make floors walls that need the
  right answer; let prestige be the run reset; keep the 3D scene as a view, not as controls.

Sources: [Game Developer: The math of idle games III](https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii),
[TV Tropes: Idle Game](https://tvtropes.org/pmwiki/pmwiki.php/Main/IdleGame),
[Idle Champions wiki: Formation strategy](https://idlechampions.fandom.com/wiki/Formation_strategy),
[Steam: Idle Champions formation discussion](https://steamcommunity.com/app/627690/discussions/0/3154186375137482396).

## Pivot idea: robots that join into a walking factory (proposal, 2026-10-31, user idea)
- **Idea:** robots join into one machine. Parts don't just add stats: they **process** things
  (one feeds another), protect, and deal damage, like a Factorio build that walks.
- **Underlying problem:** strategy comes from **layout plus flow**: where a part sits and what it
  feeds. One machine on screen fixes clarity, and auto-play fixes the micromanagement.
- **Checked (web):**
  - **Cosmoteer:** crew carry resources and power from producers to consumers. Distance between
    them decides performance; an unpowered section disables a weapon; good logistics win fights
    between otherwise equal ships. Complaint: crew management feels heavy.
  - **Backpack Battles:** adjacency on a limited grid is the whole decision. Players lose from good
    items in bad spots; auto combat makes the puzzle the game.
  - **Crowded niche:** Factory Reset (3x3 grids, neighbour effects), Workshop Rivals (modular
    machine auto-battler), Cats in the Shell (mech assembly with chain reactions), Rogue Voltage
    (wired modules, chain reactions), Cogmind (robot built from salvaged parts). Pure adjacency is
    taken; **flow between parts** (Cosmoteer-style) is the less common angle.
- **Thesis:** a walking factory: parts with inputs and outputs, routed into each other.
  **Antithesis:** free-form belts and routing are a big UI job on a gamepad, slow to build, and
  Cosmoteer players already call the logistics heavy; a full factory also crowds out the fighting.
  **Synthesis:** a small grid body where **flow goes only to neighbours** (no belts): a part takes
  its input from the part beside it. Layout is the factory; combat and walls stay automatic.
  Robots are rigid, so the art needs no rigging (cheaper than pets).

Sources: [Cosmoteer wiki: Crew](https://cosmoteer.wiki.gg/wiki/Crew),
[TV Tropes: Cosmoteer](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/Cosmoteer),
[Wikipedia: Backpack Battles](https://en.wikipedia.org/wiki/Backpack_Battles),
[Early Guides: Backpack Battles](https://earlyguides.com/backpack-battles/beginners-guide),
[Factory Reset](https://reidharry.itch.io/factory-reset),
[Workshop Rivals](https://workshoprivals.itch.io/workshop-rivals),
[Thinky Games: Rogue Voltage](https://thinkygames.com/news/tinker-with-wires-and-satisfying-chain-reactions-in-roguelike-adventure-rogue-voltage/),
[Nodal: Cogmind](https://nodal.gg/game/cogmind-722730).

### 2D or 3D for the walking factory? (2026-10-31)
- **User framing:** 3D gives up readability for layout and placement but maximizes action and
  visual cues. **Underlying problem:** layout and fighting are two different jobs with different
  needs, so it doesn't have to be one camera for both.
- **Checked (web):** Shapez 2 went 3D but planned a 2D/3D toggle at first; a player reported that
  a rotated 3D camera makes shapes look correct when they aren't. Players of 3D builders ask for:
  a camera locked during placement, a top-down build view, a ghost preview, highlighted valid
  cells, and an orientation cue; third-person views make distances and angles hard to judge.
- **Thesis:** 3D for action and spectacle. **Antithesis:** placement in 3D is the known pain point,
  and the layout is now the main decision. **Synthesis:** **2D logic, 3D rendering, two views**: a flat
  grid, a fixed top-down build view (locked camera, ghost, highlighted cells), and a fixed-angle 3D
  battle view of the same machine. That keeps the Godot 3D project and the Meshy pipeline.

Sources: [Wikipedia: Shapez 2](https://en.wikipedia.org/wiki/Shapez_2),
[GamingOnLinux: Shapez 2 announced](https://www.gamingonlinux.com/2022/11/shapez-2-an-automation-management-a-factory-building-game-announced),
[Steam: Shapez 2 discussion](https://steamcommunity.com/app/2162800/discussions/0/6929437211295508034),
[itch.io: grid-builder placement feedback](https://itch.io/post/7375925),
[Sengoku Dynasty: bird's-eye build view request](https://sengokudynasty.featureupvote.com/suggestions/662508/comment/736515).

### Walking factory in first person, no 3D building (2026-10-31, user correction)
- **Correction:** the user meant **first person**, not 3D rendering. Building must not happen in the
  3D world.
- **Underlying problem:** in first person you can't see a machine walking beside you, and a swarm
  of robots around you brings back the clutter from the playtest. So the factory has to be
  **something you carry or are**, built on a 2D screen and felt in first person.
- **Checked (web):**
  - **MechWarrior (mechlab ↔ cockpit):** the build happens in a menu and the fight in first person.
    Heat is a budget set in the mechlab (heat sinks take the space weapons would use) and
    managed live in the cockpit. A failed build sends you back to the mechlab to rework it, and that
    loop is why customization feels rewarding.
  - **Resident Evil 4 attaché case:** a 2D grid inventory inside a 3D action game. Critics say it
    turns a chore into a minigame; space is the tension.
- **Thesis:** the player is the walking factory: a rig/backpack built on a 2D grid between floors,
  used in first person. **Antithesis:** a lone first-person shooter with a loadout is a
  well-trodden genre, the "factory" can collapse into a stats loadout, and the player-too-strong
  problem moves into the player. **Synthesis:** keep **flow** as the core (parts feed neighbours,
  and producing things takes time and input). The rig's **outputs** include short-lived drones and
  turrets that are products, not pets (no individual management, capped by production rate).
  Show the flow on screen in first person: arms and weapons, gauges, and a HUD strip of the grid.

Sources: [PC Gamer: MechWarrior Online review](https://www.pcgamer.com/au/mechwarrior-online-review),
[MWO forums: Understanding heat](https://mwomercs.com/forums/topic/175656-understanding-heat/unread/),
[MWO Dev Blog 6: MechLab](https://smallcdn.mwomercs.com/news/2012/04/193-dev-blog-6-mechlab),
[Bloody Disgusting: RE4 inventory](https://bloody-disgusting.com/video-games/3658221/resident-evil-4-perfected-inventory-system-resident-evil-25/),
[Resident Evil wiki: Attaché Case](https://residentevil.fandom.com/wiki/Attache_Case).

### Precedents: first person with an army walking beside you (2026-10-31)
- **Checked (web):** FPS/RTS hybrids (Abatron, APOX, Silica, Nuclear Dawn, Eximius, Savage,
  Freeman: Guerrilla Warfare) mostly split a commander's top-down view from a first-person
  soldier, or let you possess one unit. Not confirmed that units follow your avatar.
- **From memory, not checked:** Mount & Blade (optional first person; a large army fights beside
  you; orders go to whole groups such as infantry or archers, never to individuals). Battlezone
  (1998): first-person tank, units follow and take orders. Republic Commando and Brothers in Arms:
  first person with a squad of about 3, given one context-sensitive order.
- **Pattern:** first person and an army work together when the army is **commanded as groups or
  a small squad**, and readable through **uniform, team-coloured units**. Many unique individuals
  each needing care, the playtest problem, is what none of them do.

### Core intention: a fun first-person walking army, as an auto battler (2026-10-31, user)
- **User goal:** make "first person + an army walking with you" fun; the army fights on its own
  (auto battler), with no Pikmin-style commands.
- **Checked (web):** the fun of auto battlers is many small build decisions without analysis
  paralysis, synergies paying off, and foresight; readability is the genre's known weak spot.
  Army games (Overlord, Mount & Blade) are praised for the feeling of raising and leading a
  mass; Army Corps of Hell "runs out of steam" once the strategy fades.
- **Underlying problem:** in an auto battler the decisions all happen **before** the fight, and
  the player is absent during it. First person puts the player **in** the fight. If the player's
  own action can win, the build stops mattering, and that is exactly what the playtest showed
  (player too strong, no decisions). This is already the current game's shape; what failed was
  discipline, not the genre: no size limit, unique individuals, a player who does the work.
- **Thesis:** first person, auto battle, the player fights too. **Antithesis:** a strong player
  makes the build irrelevant; an absent player makes first person pointless. **Synthesis:** the
  player is the army's **support, not its damage** (buffs, repairs, feeding the factory, choosing
  where and when to engage), the build decides fights, and the army is losable.

Sources: [Pocket Tactics: TFT design](https://www.pockettactics.com/teamfight-tactics-design),
[Quarter to Three: autobattler thread](https://forum.quartertothree.com/t/villages-dungeons-my-first-autobattler-i-dont-even-know-if-its-any-good/165180),
[80.lv: Sangokushi Bond interview](https://80.lv/articles/interview-the-sega-veteran-behind-get-wrapped-up-on-sangokushi-bond-and-the-future-of-auto-battlers),
[Empire: Overlord review](https://www.empireonline.com/gaming/reviews/overlord-review-2),
[PlayStation LifeStyle: Army Corps of Hell](https://www.playstationlifestyle.net/?p=161772).

### Crafted units, player-made links, self-organizing army (2026-10-31, user idea)
- **Checked (web):** Settlers-style games (The Settlers, Pioneers of Pagonia, Mini Settlers) make the
  economy readable because carriers move every good on screen; bottlenecks show up as slow traffic,
  and players call watching a working chain very satisfying. Oxygen Not Included sets work by
  priority, not by worker ("when everything is max priority, nothing is"). Factorio's logistic
  network has requesters and providers, not hand-routed items.
- **Thesis:** the player links robots, input to output, and they organize themselves.
  **Antithesis:** with no cap, linking each robot is micromanagement and a form of building, both
  ruled out. **Synthesis:** links are made **between types** (one link covers every Smelter → every
  Gunner); robots place themselves and visible carriers move goods (Settlers). Units are crafted from
  processed output, so production speed limits size, not a cap.

Sources: [Galaxus: Pioneers of Pagonia and the Settlers](https://www.galaxus.de/en/page/wuselfaktor-20-how-pioneers-of-pagonia-follows-in-the-footsteps-of-the-settlers-40810),
[Ubisoft: Settlers New Allies](https://news.ubisoft.com/en-au/article/54IHIBPSLbTyrtzQchvDQj/the-settlers-new-allies-out-now-on-pc),
[Game*Spark: Mini Settlers](https://www.gamespark.jp/article/2024/08/09/143997.html),
[ONI wiki: Priority](https://oxygennotincluded.wiki.gg/wiki/Priority),
[Klei forums: A matter of priority](https://forums.kleientertainment.com/forums/topic/85476-a-matter-of-priority/),
[Factorio API: LuaLogisticNetwork](https://lua-api.factorio.com/latest/classes/LuaLogisticNetwork.html).

### Why first person, if logistics reads better in 2D? (2026-10-31, user question)
- **Checked (web):** top-down favours the macro view (layouts, routes, relationships between
  objects); first person favours micro (presence, scale, a limited view that creates surprise
  and tension). Satisfactory players praise first person for scale and walking through their own
  factory, and criticise it as harder to plan in and fiddlier than Factorio's 2D map.
- **Underlying problem:** the camera should match where the decisions live. Link-type decisions
  are macro, so first person only earns its place if the **local decisions** happen in the 3D space.
- **First-person-only levers:** (1) the **limited view as information**: you know only what you
  look at (scouting, ambushes, checking the army); (2) **terrain and height** shape the army's
  flow (chokepoints, ramps, bridges, high ground); (3) **the player is the hub**: the army and
  its supply orbit your body, so where you stand is a decision (from memory, not checked:
  Factorio's personal roboport works only around the player); (4) **scale and spectacle** as the
  reward for a working build.
- **Thesis:** first person. **Antithesis:** every macro decision reads better in 2D; first person
  just costs clarity. **Synthesis:** macro choices (links, crafting) on a quick 2D screen, and
  micro choices (where, when, terrain, scouting) in first person, where the 2D view can't follow
  (the MechWarrior split).

Sources: [Unity: Camera 101](https://unity.com/blog/video-game-camera-perspectives),
[Aphyr: A satisfactory way of building](https://aphyr.com/posts/351-a-satisfactory-way-of-building),
[Tildes: Satisfactory discussion](https://tildes.net/~games/1ix9/satisfactory_is_the_best_automation_game_ever_made_and_i_seriously_cant_recommend_it_enough),
[PC Gamer: Satisfactory](https://www.pcgamer.com/au/satisfactory-is-a-factory-builder-that-echoes-ark-subnautica-factorio),
[Polycount: perspective discussion](https://polycount.com/discussion/comment/2771084).

### What makes this game "truly 3D", the way a shooter is? (proposal, 2026-10-31)
- **User ask:** 3D must make sense in every sense (positioning, vision, hearing, interaction), as
  it does in a shooter.
- **Underlying problem:** in a shooter the core verb (aim) **is** a 3D act: where you look is what
  you hit, what you hear tells you where to look, and where you stand decides who can see you.
  This game needs a core verb that is spatial in the same way, for a weak player who gives no orders.
- **Checked (web):** Battlefield spotting: players aim and mark enemies for the team; the designers
  kept marks short and active ("it can't be a fire-and-forget sweep") so that intel stays
  valuable; spotting also exposes the spotter. Players called passive auto-spotting overpowered.
  Dolby's game audio guidance: directional sound points players to things outside the limited
  field of view (incoming fire, allies, hidden items), and loud music masks it.
- **Proposal: "you are the army's eyes."** The army fights on its own but only knows what you
  have seen. Vision = spotting (marks fade, looking at a threat exposes you); position = you are
  the army's anchor and supply core; hearing = the army's state, and threats behind you, by sound;
  interaction = look at big things plus one button, forgiving, no precision.
- **Thesis:** gaze-as-intel makes every sense matter. **Antithesis:** "looking at things" can be
  passive; marks can drift into Pikmin orders (breaking auto battler); and auto-spotting was called
  overpowered in Battlefield. **Synthesis:** marks are **information, not orders** (the army
  decides what to do with them), they fade (you keep looking), and spotting costs you exposure.

Sources: [MP1st: Battlefield 6 auto-spot nerf](https://mp1st.com/news/battlefield-6-spot-nerf-devs-dont-want-to-make-open-vs-closed-decision),
[Gfinity: How spotting works in Battlefield 6](https://www.gfinityesports.com/article/how-spotting-works-in-battlefield-6),
[Gfinity: Battlefield 6 spotting reception](https://www.gfinityesports.com/article/battlefield-6s-spotting-mechanic-gets-mixed-reception-from-players),
[Dolby: game audio dynamic range](https://professional.dolby.com/en-in/gaming/downloads/dynamic-range).

### What actually separates a 2D shooter from a first-person shooter? (2026-10-31)
- **Checked (web):** most top-down shooters show everything around the character; limited vision
  is a deliberate add-on (ONSIGHT, Running With Rifles). First-person shooters run a 75–90° field of
  view, and their levels are built so you deal with what is in your current view; height gives
  awareness.
- **Definition (mine):** the difference isn't looking or instructing; both views have those. It is
  **who holds the camera**:
  - **2D:** the camera is outside you. You see all around you at once (allocentric, a map), and
    your knowledge doesn't depend on where you face. The challenge is reading and dodging what you
    can already see.
  - **First person:** the camera is your head. You see a ~90° cone, so **attention is scarce and
    directional**: turning costs time and leaves the rest of the world unwatched. What you see
    depends on **where you stand** (walls block *you*, not just units). Looking and acting are the
    same act (the crosshair is the centre of your view).
- **So, for this game:** first person only makes sense if the game is about **where the player
  points their limited attention and from which spot**. Threats and opportunities must come from
  more directions than you can watch, so turning is the action, not a chore.

Sources: [Steam: ONSIGHT](https://store.steampowered.com/app/5044050/),
[Running With Rifles wiki: Line of sight](https://runningwithrifles.gamepedia.com/Line_of_Sight,_Vision?oldid=7618),
[Game Developer: Level design compare FPS vs TPS](https://www.gamedeveloper.com/design/level-design-compare-fps-vs-tps-games),
[GDQuest: Field of view](https://www.gdquest.com/library/glossary/field_of_view),
[Game Developer: Better level design via line of sight](https://www.gamedeveloper.com/design/better-level-design-via-line-of-sight).

### Investigation: answering the attention questions (2026-10-31)
**Checked (web):**
- **Left 4 Dead director:** pacing cycles build-up → peak → relax; mobs spawn only in build-up.
  Evolve's developers on copying it: "You can't appreciate the action unless you have some inaction."
- **Orcs Must Die 2:** maps almost always send more than one stream, so you can only handle part of
  it yourself. Third person; the VR spin-off is first person.
- **Five Nights at Freddy's:** cameras cost power, so you choose what to view and when; sound
  tracks threats off-camera. (Mostly blog sources.)
- **Spinning plates (Chinese Juggler, Ocean):** plates slow down visibly before they fall, and you
  rush between them. "Manic panic" is the fun; it grows boring once levels stop escalating.
- **Apex Legends ping:** one button, whose meaning depends on what you aim at. Respawn tested it with
  voice chat banned.
- **Telegraphs (Bugnet):** a cue must be distinct and give enough time to react.
- **Brütal Legend (action + RTS):** criticised because you could win by hacking without commanding,
  commands were cumbersome, and the RTS parts halted momentum.
- **Sanctum (first-person tower defense):** your own gun felt secondary, building in first person
  was disorienting, and the hook was being in the fight, not watching.

**Answers (mine, from the above):**
1. **Verb:** one contextual button on what you look at (Apex ping). It sets a **priority**, not an
   order (Oxygen Not Included's model): the army shifts supply and fire toward what you look at.
   Looking at a starving line feeds it; looking at an enemy focuses it; looking at scrap harvests it.
2. **Demand:** several "plates" around you (sides of the army, streams of enemies, Orcs Must Die),
   paced in waves (L4D: build-up, peak, relax) so turning is urgent but not constant.
3. **Cost of not looking:** a slow, visible decline before a fall (plates): an unwatched part
   wobbles (supply thins, fire slows), then breaks if left alone.
4. **Signals:** a distinct sound per kind of problem (FNAF, Dolby), plus a cue at the screen
   edge, with time to react (telegraph rules).
5. **Position:** not answered. Only "height gives awareness" (earlier source). Open.
6. **The army in view:** not answered. Only see-through shaders for occlusion (top-down devlog). Open.
7. **Enemies against your attention:** partly. L4D's director targets stress; from memory, not
   checked: FNAF's animatronics move while unwatched. A candidate: enemies push where you aren't looking.
8. **Skill:** assumption: looking at the plate *before* it wobbles (shooters' pre-aim).
9. **Logistics in view:** partly. Settlers-style visible carriers (earlier). Open for one 90° glance.

**Warnings:** Brütal Legend and Sanctum show the two failures: the player can win without the army,
or the player's part feels secondary. The verb must decide fights without dealing damage, and work
mid-motion (no menus, no pausing).

Sources: [Valve: L4D2 director scripts](https://developer.valvesoftware.com/wiki/Left_4_Dead_2/Scripting/Director_Scripts),
[Shacknews: Evolve and the L4D director](https://shacknews.com/article/82787/how-evolve-assures-action-peaks-and-valleys),
[PC Gamer: Orcs Must Die 2 review](https://www.pcgamer.com/au/orcs-must-die-2-review),
[Geeks Under Grace: FNAF review](https://www.geeksundergrace.com/gaming/ccg-review-five-nights-at-freddys/),
[Everygamegoing: Chinese Juggler](https://www.everygamegoing.com/larticle/Chinese-Juggler-000/24949/),
[PC Gamer: Apex ping system](https://www.pcgamer.com/au/apex-legends-ping-system-is-a-tiny-miracle-for-fps-teamwork-and-communication/),
[UX Collective: Apex ping](https://uxdesign.cc/apex-legends-ping-system-gaming-ux-done-right-4661cd94954c),
[Bugnet: attack telegraphs](https://bugnet.io/blog/how-to-design-enemy-attack-telegraphs),
[Co-optimus: Brütal Legend](https://www.co-optimus.com/review/338/page/6/beyond-co-op-reviews-october-and-november-2009.html),
[PC Gamer: Brütal Legend review](https://www.pcgamer.com/uk/brutal-legend-review),
[GamesRadar: Sanctum review](https://www.gamesradar.com/uk/sanctum-review/),
[Destructoid: Sanctum review](https://destructoid.com/?p=80111).
- **Dropped (user, 2026-10-31):** "look sets a priority" as the verb. The user's reasoning: the
  army's automation should work by itself; needing a priority system means it has flaws and
  priorities only cover them. New rule for the verb: it must give the army something it
  **structurally lacks**, not correct its decisions.

### Player-made arrangement rules, emergence, and 2D again (2026-10-31, user idea)
- **User idea:** the player creates the army's arrangement system, "Game of Life"-like (far
  reference), for emergent play and personal expression. The gameplay sketch didn't convince;
  2D is back on the table.
- **Checked (web):**
  - **Carnage Heart:** you program robots by placing logic chips on a grid. The presets teach
    but don't win, and odd AI designs add fun.
  - **Gladiabots:** you never control the squad, you write its AI; Carnage Heart was a main reference.
  - **Boids:** flocking comes from three local rules (separation, alignment, cohesion), not group scripts.
  - **Game of Life:** each cell reacts only to its neighbours, and the results are hard to predict
    from the rules.
  - **Liquid War:** the only input is a cursor; fighters take the shortest path to it. Encirclement
    and map shape decide fights ("the whole point of the game").
  - All of these are viewed top-down.
- **Underlying problem:** emergence is a **pattern**, and patterns are read from above. First person
  shows a 90° slice at ground level, so the joy of watching your rules make shapes is mostly lost.
  The design now pulls two ways: **systems and expression** (want overview, 2D) and **presence and
  attention** (want first person).
- **Thesis:** player-written local rules per robot type, emergent formations. **Antithesis:**
  rule-writing UIs (Carnage Heart) are notoriously deep and slow, and emergence is hard to tune and
  hard to see in first person. **Synthesis:** test the riskiest unknown first, in the cheapest
  view: a small 2D prototype of a few rule cards per type and an emergent army. Decide the camera
  after the rules prove fun; if they aren't fun in 2D, first person won't save them.

Sources: [Pocket Gamer: Carnage Heart EXA developer](https://www.pocketgamer.com/carnage-heart-exa/carnage-heart-exa-developer-explains-the-joy-of-programming-robot-warriors/),
[Giant Bomb: Carnage Heart](https://www.giantbomb.com/games/3030-8497/),
[Pocket Gamer: Gladiabots](https://www.pocketgamer.com/gladiabots/gladiabots-combines-tactical-bot-combat-and-programming-puzzles/),
[Wikipedia: Boids](https://Www.Wikipedia.org/wiki/Boids),
[UQ: complex systems](https://www.maths.uq.edu.au/ClubInfinity/Newsletters/15/complex_systems.html),
[Liquid War rules](https://ufoot.org/liquidwar/v5/doc/rules/en/).

### Story: a robot rebel inside a robot empire (proposal, 2026-10-31, user idea)
- **User idea:** robots rule the world as a colonial, imperial power. The hero, a robot, wants to
  bring the whole system down: it hacks imperial robots to recruit them, or kills them for scrap to
  build its own robots (gathering, defense, attack, exploring, research, logistics). Roguelike: one
  run is the whole story, starting with nothing but perhaps one small companion bot, building an
  army inside the empire until the final boss room. The boss controls everything.
- **Checked (web):**
  - **FTL:** one run is the whole journey: start small, grow, and fight the rebel flagship as the
    final boss. A pursuing fleet forces you to choose which stops to take. One critic says the final
    turn to "destroy the flagship" undercuts the small-ship story.
  - **Cogmind (very close precedent):** a robot climbs out of a robot civilization, builds itself
    from salvaged parts, and hacks robots and machines. How you destroy a robot changes what salvage
    it leaves. Allies are "notoriously disposable, by design". Worker robots ignore you and go about
    their business. The story is uncovered over many runs.
  - **Hades:** death is a story beat. The story moves forward between runs at a hub; a lesson from
    Pyre was that linear endings hurt replay value.
- **Fit with the mechanics (mine):**
  - Hacking = claiming the world (the verb).
  - Kill-or-hack = a real trade-off: scrap now, or a ready unit.
  - Starting with one bot and no cap = a growth arc.
  - Theme matches mechanics: the empire runs on **rigid, uniform rules**, and the rebel army runs
    on the player's **own emergent rules**. The final boss is the rule-maker.
- **Thesis:** one run = the whole story (FTL). **Antithesis:** a fixed story wears out on replay
  (Pyre), and Cogmind already owns "rebel robot in a robot world, salvage and hack", so we need our
  own angle. **Synthesis:** fixed premise and finale, varied route (FTL); a thin story across runs
  (Hades-style hub, e.g. a rebel cell that reboots you); our angle is the **army and its player-made
  rules**, not one robot's body. Start with 3 roles, not 6.

Sources: [Wikipedia: FTL](https://en.wikipedia.org/wiki/FTL:_Faster_Than_Light),
[GameCritics: FTL review](https://gamecritics.com/sparky-clarkson/ftl-faster-than-light-review),
[PC Gamer: Cogmind](https://www.pcgamer.com/uk/cogmind-is-a-sci-fi-roguelike-about-building-yourself-from-salvaged-parts),
[ModDB: Cogmind robots](https://www.moddb.com/news/robots),
[Kill Screen: Cogmind](https://www.killscreen.com/cogmind-proves-roguelike-isnt-done-ascii-art-yet/),
[First Person Scholar: There is no escape](https://www.firstpersonscholar.com/there-is-no-escape/),
[itch.io: loops and arcs in Hades](https://itch.io/blog/774695/to-hell-and-back-again-a-look-at-loops-and-arcs-in-hades).

### Rule cards: how the player writes the army's rules (sketch, 2026-10-31)
- **Checked (web):**
  - **FF12 gambits:** each gambit is a condition plus an action, run top-down in list order. They
    exist because real-time control of everything was too hard. Praised as a mini AI built from
    simple blocks; criticised as "the game plays itself" and as limiting. Defenders say the depth
    is in tuning gambits for each fight.
  - **Gladiabots:** a visual AI editor, described as "simple to use but deep".
  - **Carnage Heart:** presets teach but don't win.
- **Sketch (mine):**
  - Each robot **type** has 3 ordered slots: *when I sense X → do Y*.
  - Conditions are **local** (what this robot senses nearby), so whole-army behaviour emerges
    (Game of Life, boids).
  - Cards are won in the run; hacking an imperial robot steals its rules (story tie).
  - Each type starts with a preset that works but isn't best.
  - Gamepad: d-pad picks a slot, left/right swaps the card, one button reorders.
- **Thesis:** gambit-style local rules per type. **Antithesis:** FF12's "plays itself" complaint,
  and emergence that the player can't predict or read. **Synthesis:** rules matter because floors
  change (a different threat needs a different emergent shape), the player still claims and hacks in
  real time, and the card list is small enough to reason about.

Sources: [PlayStation Blog: FF12 gambits](https://blog.playstation.com/?p=192698),
[StrategyWiki: FF12 gambits](https://strategywiki.org/wiki/Final_Fantasy_XII/Gambits),
[Obsidian: FF12 and the illusion of free will](https://publish.obsidian.md/taniynquest/Final+Fantasy+XII+and+the+Illusion+of+Free+Will),
[GamingOnLinux: Gladiabots](https://www.gamingonlinux.com/articles/13958/).

### Naming: Assemblia, with Automates as the unit name (2026-10-31)
- **Advice:** a name should be memorable, searchable, spellable from hearing, not taken, and sell
  the game's feel; avoid crowded patterns ("Shadow of…").
- **Checked (quick web search, not a trademark or Steam DB search):**
  - "Rebel Swarm" is an X-Wing miniatures term, and *Swarm* is already a robot-programming game.
  - Botstrap is buried under "Bootstrap" (the web framework).
  - *Compile & Defend* (2026) is a programming tower defense, too close to Compile & Conquer.
  - Unruled was rejected as too anarchic.
  - "Automata" is dominated by NieR: Automata.
  - **Assemblia: no game found** (the nearest is *Asemblance*, 2016).
- **Decision (user):** **Assemblia**, meaning you *assemble* an army, and an *assembly* is a
  gathering of people. "Automates" (automata + mates) doesn't work as a title (it reads as a verb,
  has two pronunciations, and its search results are flooded), so it became the in-game name for
  the player's robots.
- **To do before release:** a full Steam, trademark and social-handle check.

Sources: [PC Gamer: similar Steam names](https://pcgamer.com/games/why-so-many-steam-games-have-weirdly-similar-and-forgettable-names/),
[Bugnet: naming your indie game](https://bugnet.io/blog/how-do-you-name-your-indie-game),
[Epic: Asemblance](https://store.epicgames.com/p/asemblance?lang=cs),
[GG.deals: Compile & Defend](https://gg.deals/steam/app/4915240/),
[Steambase: NieR: Automata](https://steambase.io/games/nier-automata/info).

### Rule-card prototype: when rules are edited, and how robots get made (proposal, 2026-10-31)
- **Checked (web):**
  - **Auto battlers** (genre write-ups, a developer blog): fights are fully automatic, and the
    skill moves into the preparation phase. One developer (attribution not pinned to a page) tried
    live control first and found it worse, because it undercut the pre-fight decision; the same
    write-up says a loss must be explained by a replay, or it feels like a slot machine.
  - **Gladiabots:** the loop is watch a match, tweak the AI, send the robots back in; the AI
    editor opens from a finished match's replay. Nothing found about mid-match editing.
  - **Pikmin:** Pikmin carry pellets and enemies back to the Onion, which makes new Pikmin; more
    and matching-colour matter makes more. Growth is paid for by hauling.
  - **Cogmind:** fabricators build parts and robots from schematics, but need matter, which you
    bring (worker bots carry it).
  - **Mindustry:** a unit factory takes a chosen unit, resources and power, and outputs the unit.

#### When can rules be edited?
- **Abstract problem:** commitment vs adaptation. If rules change mid-fight, they become orders
  (or priorities) in disguise, and a loss can't be traced to a plan. If they never change, the
  player watches a loss they can't touch.
- **Thesis:** edit only between rooms (after a room is cleared), never during a fight, no pause menu.
- **Antithesis:** the FF12 and auto-battler risk: you watch your army lose with nothing to do,
  and you learn slowly because each fix waits for the next room.
- **Synthesis (recommended):** edit between rooms; the next room shows its threat before you enter,
  so you plan for it; during a fight the player acts by walking, dodging, hacking and salvaging.
  Rooms are short, so the watch → tweak → retry loop (Gladiabots) stays fast.
  In the prototype: edit between waves.
- **Risk/reward:** low risk (no in-fight UI), high reward (it decides whether rules are a plan).

#### How do robots get made?
- **Abstract problem:** two inputs (hack, salvage) fill one resource (army size), with no cap.
  The Dungeon Pets failure was growth with no pressure, so the input must be throttled by
  something the player's rules affect.
- **Thesis:** the hero is the assembler (a walking Onion). Salvaged enemies leave scrap;
  Gatherers pick it up, Carriers bring it to the hero; every N scrap the hero assembles one robot.
  The hero is a type with its own rule card that picks what to build (preset: the role with the
  fewest robots). Hacking gives a ready robot of the enemy's type, with its rules, but costs time
  standing next to the enemy and gives no scrap.
- **Antithesis:** everything centres on the hero (carriers chase a moving target, the hero is the
  bottleneck); picking builds by rule card feels indirect; a fixed factory (Cogmind, Mindustry)
  makes supply lines longer and more visible.
- **Synthesis (recommended):** the hero assembles, for the prototype: it keeps the 3 roles and
  needs no building. Hauling to a moving hero is the logistics test: if carriers can't keep up,
  the army stops growing, which is the size limit we want. Fallback if it feels hero-bound: an
  Assembler role (a 4th type) that the army protects.
- **Risk/reward:** medium risk (carrier pathing to a moving target), high reward (growth limit and
  visible logistics in one rule).

Sources: [Dinogame: what is an autobattler](https://dinogame.gg/blog/what-is-an-autobattler/),
[Solodevstack: a three-act auto-battler](https://solodevstack.com/blog/orchard-deck-deterministic-card-battler-keywords),
[Leiden thesis on auto battlers](https://theses.liacs.nl/pdf/2021-2022-KientzL.pdf),
[Gladiabots alpha 13](https://gfx47.itch.io/gladiabots/devlog/34211/gladiabots-alpha-13-is-live),
[Game Developer: Gladiabots inception](https://www.gamedeveloper.com/design/gladiabots-inception),
[Pikmin wiki: Pellet](https://pikminwiki.com/Pellet),
[Pikmin wiki: Onion](https://www.pikminwiki.com/Onion),
[ModDB: Cogmind scanalyzers and fabricators](https://www.moddb.com/news/scanalyzers-fabricators/),
[Steam: Mindustry unit factories](https://steamcommunity.com/app/1127400/discussions/0/3079890849085692956/?l=spanish).

### MVP scope: test only the rules (2026-10-31, user: "that prototype looks very expensive")
- **Cut:** the full prototype built every system at once (hero assembly, scrap, carriers, hacking).
  The riskiest unknown is narrower: does swapping 2–3 rule cards make a visibly different army
  shape, and does each shape beat a different wave? If one rule list wins every wave, the choice
  has one answer (the Dungeon Pets failure).
- **Thesis:** one type, a fixed army of 20, 3 slots, 8 cards, two wave kinds that want opposite
  shapes (rushers → a tight guard ring; turrets → a spread-out charge), edits between waves.
- **Antithesis:** with one type and no logistics it might feel like tuning boids, not running an
  army, and the hero walking to the enemy might replace the card choice entirely.
- **Synthesis:** accept it. The MVP is a test of rule choice, not of the whole game. If walking
  beats card choice, we learn that cheaply. Robot colour shows the slot each robot is running, so
  a loss can be read on screen.
- **Pass test (user playtest):** you change cards because the next wave needs it, and you can see
  why a wave was won or lost. **Risk/reward:** low risk, high reward.
- **Update (user, 2026-10-31):** the rule system is removed from the code because the rules are
  not designed yet; the 8 cards were my placeholder. Not a rejection of the idea. The sandbox keeps
  the hero, the fixed army (one placeholder behaviour: attack near, else return, else circle) and
  the two wave kinds.

### Idle robots roam instead of orbiting (2026-10-31, user: "they should look like they have a life of its own")
- **Checked (web):** a random new heading every frame looks robotic; capping the turn rate makes
  paths curve (Bugnet). Wander loops alternate walk → idle → new path, with tunable idle time and
  weighted walk/idle choice, kept near a home point by a small wander radius (STO forum, OpenMW,
  a Unity NavMesh asset).
- **Done:** each robot walks to its own random spot near the hero (the spot moves with the hero),
  at its own pace, with capped turning; 60% of the time it stops for 0.4–2 s and looks around.
  A dot shows where it faces.
- **Thesis/antithesis:** life-like roaming vs a readable, tight formation. A critic would say a
  wandering army is harder to read. **Synthesis:** roaming only when idle; the leash (hero far →
  return) and fighting stay as they were, so shape still changes when something happens.

Sources: [Bugnet: AI wander looking robotic](https://bugnet.io/blog/how-to-fix-pygame-ai-wander-looking-robotic),
[STO forum: ambient behaviour](https://forum.arcgames.com/startrekonline/discussion/992841/ambient-with-combat-behavior-explanation-of-variables),
[OpenMW aiwander.cpp](https://git.cijber.net/mirror/openmw/src/commit/f942db2b2761483b9e262fbdfd50302f9c2903b5/apps/openmw/mwmechanics/aiwander.cpp),
[Unity NPC wander asset](https://jess-makes-things.itch.io/simple-npc-wander-ai-unity-navmesh).

### Experiment: attack-move order (2026-10-31, user: "right click on where to attack")
- **Conflict:** breaks two solid constraints (no Pikmin-style orders; no priority systems).
  The user chose to test it as a labelled experiment rather than drop or skip it.
- **Checked (web):** attack-move = a move order plus a per-tick enemy scan: units fight what they
  meet on the way, then resume toward the point (Bugnet, SC2 guide). A plain move ignores ambushes,
  which is why attack-move is the safer group default. Players complain about poor target choice
  on arrival (Age of Empires forum).
- **Done:** right-click (gamepad: right stick moves a cursor, RT confirms) sends the whole army to
  the point. On the way it fights enemies within its normal reach; at the point it goes for enemies
  within 160 px; when none are left it stands down and returns to roaming. A ring marks the order.
- **Thesis:** an order makes the player's intent matter. **Antithesis:** it's the Pikmin/RTS lever
  the design ruled out; if the army needs it, the automation has a flaw (e.g. robots only react
  within 120 px, so they ignore turrets). **Synthesis:** test it; if the playtest shows you click
  constantly, it's micromanagement and patches the automation; if you click rarely and it creates
  decisions (where to commit), keep it and rewrite the constraint.

Sources: [Bugnet: attack-move ignoring enemies](https://bugnet.io/blog/how-to-fix-rts-attack-move-units-ignoring-enemies-along-the-path),
[Blizzard: SC2 basic unit controls](https://news.blizzard.com/en-us/article/4552956/game-guide-basic-unit-controls),
[AoE forum: attack move target choice](https://forums.ageofempires.com/t/attack-move-does-not-focus-enemy-units-but-attacks-buildings-instead/178540).

### Resource-gathering test (proposal, 2026-10-31, after the user played the fighting test)
- **Checked (web):**
  - **Pikmin:** heavy things need N carriers, and the game shows the count, so "more carriers =
    it moves" is readable at once. A developer: carrying defeated enemies home was meant to feel
    rewarding, and "if it looks heavy you need more Pikmin" is understood intuitively.
  - **The Settlers: New Allies:** carriers physically haul goods on screen; reviewers call watching
    them "mesmerising"; too few carriers (turned into soldiers) and goods "slow to a crawl", and
    jams make the flow legible. Critics call it repetitive and slow.
  - **StarCraft II mining:** distance to the drop-off matters until a patch is saturated; past
    saturation, extra workers add little, which is what pushes expansion.
- **Abstract problem:** one army, two jobs (fight, gather), one resource (robots' time). The
  decision should be where you walk (near scrap = faster income, but away from safety) and how
  much of the army is busy hauling when a wave hits.
- **Thesis:** one robot type with a fixed behaviour does both: fight if an enemy is near, else
  carry scrap to the hero if scrap is near, else roam. Scrap deposits sit around the map, and
  wrecks drop scrap. The hero assembles a robot every N scrap. No refill between waves: hauling is
  the only growth.
- **Antithesis:** one type doing everything isn't a logistics chain (no gather → carry handoff,
  agreed roles were gather/carry/fight); and with no rules, the player can't change who gathers.
- **Synthesis:** test the cheapest version first: does fight-vs-haul tension plus "where to walk"
  make decisions, and can the flow be read on screen? Split roles only if one type is too flat.
- **Built (2026-11-01, not yet playtested):** `scenes/gather.tscn`, chosen from the playtest menu
  (`scenes/menu.tscn`, now the main scene). Start with 8 robots; 6 scrap piles of 12, the right two
  inside turret range; wrecks drop 1 scrap. Robots fetch only piles inside the hero's scrap ring
  (260 px) and carry at 60% speed, so where you stand sets haul distance. 5 scrap = 1 robot. No
  refill, no wave time limit, 12 s calm between waves (15 s at start). The attack-move order is
  off here so walking is the only lever. Tuning knobs are the constants at the top of `gather.gd`.
- **Pass test (user playtest):** you choose where to walk because of scrap vs safety, and you can
  see on screen how much of the army is hauling when a wave hits.

### Three-roles test: fighter / hauler / builder (2026-11-01, user: "builder bots ... 3 types")
- **Checked (web):** worker designs split between one unit doing every job and a separate unit
  per job (Tropedia: Worker Unit). Colony games swing between fixed roles and flexible multi-job
  roles (Mercury Fallen devlog). Mindustry drones mine on their own, take no commands, and deliver
  only to the core, a single hub that keeps logistics readable (r/Mindustry FAQ).
- **Abstract problem:** a production chain (pile → hauler → builder → new bot) where each link can
  be cut. Losing builders stops growth; losing haulers starves builders; losing fighters exposes
  both. The questions are whether the chain reads on screen and whether protecting it creates decisions.
- **Built:** `scenes/roles.tscn`. Start with 5 fighters, 3 haulers and 1 builder. Haulers take
  scrap from piles inside the ring to the nearest builder; builders stay within 60 px of the hero
  and turn 5 scrap into 1 bot over 2 s. Only fighters fight. **Q / LB cycles the build type.**
  The attack-move order (RT / right-click) is on and sends fighters only (user, 2026-11-01).
- **Build choice (user picked the button over auto-by-need and a fixed cycle):** a labelled
  experiment. **Thesis:** the player shapes the army's mix, which is a real decision. **Antithesis:**
  a build-type setting is a priority system, which the constraints rule out; if the right mix is
  obvious, it's busywork that covers for missing automation. **Synthesis:** test it; if you set
  it once and forget, auto-by-need should replace it; if you switch it because of what the next
  wave or pile needs, keep it and rewrite the constraint.
- **Pass test (user playtest):** you can see the chain on screen, and losing one link changes
  what you do next.

Sources: [Tropedia: Worker Unit](https://tropedia.fandom.com/wiki/Worker_Unit),
[Mercury Fallen devlog: robots & job roles](https://nitrousbutterfly.itch.io/mercury-fallen/devlog/3268/developer-log-16-robots-job-roles),
[r/Mindustry: commonly asked questions](https://cal1.lr.ggtyler.dev/r/Mindustry/comments/d2jvl5/commonly_asked_questions).
- **Update (user, 2026-11-01): storage bot + build on demand.** A fourth type, storage (purple
  hexagon, holds 15, stays near the hero). Haulers deliver to the nearest storage with space,
  not to builders. Builders no longer build on their own: E / RB makes the free builder nearest the
  hero spend 5 stored scrap on the type picked with Q / LB (2 s build). A destroyed storage bot
  drops its scrap as a pile, so storage is a new link to protect. Start: 5F 3H 1B 1S.
  **Thesis:** storage separates income from spending, so you choose when to build (e.g. fighters
  just before a wave). **Antithesis:** two buttons for one action is more input, and it pulls the
  game further from "the army runs itself". **Synthesis:** test it; if you always press build the
  moment scrap reaches 5, on-demand adds nothing and auto-build should come back.
- **Update (user, 2026-11-01): storage bot dropped; the hero is the storage.** Haulers bring
  scrap to the hero; E / RB spends 5 of the hero's scrap through the nearest free builder.
  Build on demand stays. Start: 5F 3H 1B.

### Processing test: processor bots (2026-11-01, user: "take input and output ... can be anything")
- **Checked (web):** Factorio's core loop is raw resources → intermediate products, and the
  challenge is managing that flow; players say the game forgives inefficient layouts and that
  tweaking setups is half the fun (Factorio forum, StudioBinder guide). Not checked: sink design
  for intermediates (the search found nothing on it).
- **Abstract problem:** a processor is a recipe, inputs → outputs over time. An intermediate
  item only matters if something needs it (a sink); otherwise processors make nothing anyone uses.
- **Built:** `scenes/process.tscn`. A recipe is data (`RECIPES` in `process.gd`), so later recipes
  take any inputs and give any outputs; for now only "refine": 2 scrap → 1 processed, 3 s.
  Processors stay near the hero and trade with the hero's inventory (the hero is the only storage,
  user's choice over haulers feeding processors). Any of the 4 types builds on demand.
  **Costs (user's choice):** fighter and builder 3 processed; hauler and processor 5 scrap.
  Start: 4F 3H 1B 1P, no processed scrap.
- **Thesis:** split costs make raw scrap compete: more processors or haulers now (economy), or let
  processors refine it into fighters (defence). **Antithesis:** processors eat raw scrap
  automatically, so they can starve the raw-scrap builds and the player has no say over it (no
  rules yet); and one recipe makes the processor just a delay on the scrap. **Synthesis:** test
  whether raw vs processed spending creates a decision; if starvation feels unfair, the first
  rule card could be "processor: keep N raw scrap in reserve".
- **Pass test (user playtest):** you choose between growing the economy and the army, and you can
  see the chain pile → hauler → hero → processor → hero → builder on screen.

Sources: [Factorio forum: basic resource management](https://forums.factorio.com/viewtopic.php?p=31368),
[StudioBinder: Factorio guide](https://cache.studiobinder.com/factoio).
- **Update (user, 2026-11-01): builders and processors barely move.** They no longer roam; they
  stand still and only walk to a fixed slot 15–45 px beside the hero once the hero is over 90 px
  away, then stop (also applies to builders in the roles test).
- **Update (user, 2026-11-01): the hero mines by hand.** Hold A / Space within 26 px of a pile:
  1 scrap per 0.6 s into the hero's inventory (roles and processing tests). Slower than three
  haulers, so it helps early but doesn't replace them ("player is not strong").

### Can an RTS work on Switch? (2026-11-01, user question)
- **Checked (web):** yes, if designed for the gamepad from the start. Console-first RTS (Pikmin,
  Halo Wars) have the strongest controls (GamesRadar); Halo Wars' scheme was reused almost
  unchanged in Halo Wars 2 but dropped PC staples like custom unit groups (Wayward Strategy).
  Northgard was reworked for controllers and Switch handheld play (Gamereactor). Age of Empires II
  on Xbox needed automated villagers because fine micro is awkward on twin sticks (PC Gamer).
  Creative Assembly built Total War: Warhammer 40,000's controller support together with its
  battle system (TechRadar).
- **What follows for Assemblia:** the hard parts of PC RTS on a pad are box-selecting, free camera
  panning and per-unit orders. Our design already avoids them: the camera follows the hero, the
  army runs itself, and orders are army-wide (attack-move, build type). The rule is: every new
  command must be one button or one stick + one button, aimed from the hero's position.
- **Assumed (not checked):** Halo Wars' bumper "select all / select on screen" and radial menus;
  Pikmin's lock-on throw as a model for a single "point here" input.

Sources: [GamesRadar: Halo Wars interview](https://www.gamesradar.com/halo-wars-interview),
[Wayward Strategy: Halo Wars, the ultimate console RTS design](https://waywardstrategy.com/2020/03/23/halo-wars-the-ultimate-design-for-console-rts/),
[Gamereactor: Northgard console controls](https://www.gamereactor.eu/console-controls-for-northgard-intuitive-and-automatic/),
[PC Gamer: RTS with a controller](https://www.pcgamer.com/games/rts/playing-rts-with-a-controller-total-war-warhammer-40-000-dev-says-it-really-does-work-in-their-game-i-think-weve-landed-in-a-really-solid-spot/),
[TechRadar: Creative Assembly on controller RTS](https://techradar.com/gaming/were-all-keen-to-keep-evolving-creative-assembly-says-total-war-warhammer-40-000s-controller-support-was-developed-alongside-the-games-battle-system-and-doesnt-believe-the-myth-that-a-gamepad-cant-work-with-rts-games).
- **Update (user, 2026-11-01): one order button, read by context.** RT / right-click on a point
  with no enemies within 160 px but scrap there = **extract**: all haulers empty those piles
  (outside the scrap ring too) and bring the scrap to the hero, then go back to normal. With
  enemies there it stays attack-move (fighters). The cursor shows "attack" or "extract" before you
  press. **Thesis:** one context button keeps the pad layout small (see Switch notes) and reads
  the player's intent from the world. **Antithesis:** context buttons misfire when the context is
  ambiguous (an enemy wanders near a pile, and you get attack instead of extract). **Synthesis:**
  the cursor label shows the meaning before the press; if misfires happen in the playtest, split
  it onto two buttons.
- **Update (user, 2026-11-01): hero mining is automatic, at range.** No button: the hero pulls
  1 scrap per second from the nearest pile inside its scrap ring (a faint beam shows it). Replaces
  hold-A-next-to-a-pile; A is free again. Slower than before because it never stops.

### RTS-style unit creation (2026-11-01, user: "should be like rts, right now it's awkward")
- **Checked (web):** RTS production is a queue: Command & Conquer pauses an item on the first
  cancel click and refunds it on the second (StrategyWiki); players ask for hotkeys to remove one
  queued unit or clear the queue (AoE forum); StarCraft caps the queue at 5 per building (Giant
  Bomb). On console, Halo Wars solved build menus with a radial "circle menu" (Halopedia), which a
  review praised for avoiding modal menus. Not checked: pay-on-queue vs pay-on-start (nothing
  found; pay-on-queue is the StarCraft convention from memory).
- **Problem with the old input:** pick-then-build is two steps per unit and hides what's coming.
- **Options shown to the user:** D-pad direct, Halo Wars radial (hold LB + right stick), hold LB +
  face button. **User picked D-pad direct.**
- **Built:** D-pad up/left/right/down (keys 1-4) queue one fighter / hauler / builder /
  processor. Paid when queued, B / Backspace cancels the last queued for a full refund, shared
  queue of up to 8, every free builder takes the next item. The bottom bar shows each type's
  button and cost (greyed when you can't afford it) and the queue as coloured squares.
- **Thesis:** one press per unit, no menu, the queue on screen. **Antithesis:** only 4 D-pad
  directions; a 5th type breaks the scheme (the radial menu scales, the D-pad doesn't).
  **Synthesis:** use the D-pad while there are ≤4 types; move to the radial menu if a 5th arrives.

Sources: [StrategyWiki: C&C controls](https://strategywiki.org/wiki/Command_&_Conquer/Controls),
[AoE forum: hotkeys to cancel unit queues](https://forums.ageofempires.com/t/suggestion-hotkeys-to-cancel-unit-queues/72733),
[Giant Bomb: Build Queue](https://giantbomb.com/wiki/Concepts/Build_Queue),
[Halopedia: Circle Menu](https://halopedia.org/Circle_Menu),
[Co-Optimus: Halo Wars review](https://www.co-optimus.com/review/161/page/1/Halo_Wars.html).

### Processing was automatic: fixed with pull production (2026-11-01, user picked option 3)
- **Problem:** processors took raw scrap the moment they could, competing with raw-cost builds
  with no say from the player. Abstract shape: two consumers, one pool, no allocation.
- **Checked (web):** pull production "initiates production as a reaction to present demand",
  signalled downstream (kanban); push produces ahead of demand; most real systems are hybrids with
  a buffer at a "decoupling point" (Fabrico, Wikipedia push–pull). Not checked: game examples
  (the search returned only manufacturing sources; Factorio requester chests are from memory).
- **Options weighed:** process on demand (a second manual job, D-pad full, micromanagement);
  connections/links (real logistics but needs the undesigned rule system, gamepad-hostile);
  **pull from the build queue (picked).**
- **Built:** queuing a unit uses processed scrap in stock first; for the rest, the recipe inputs
  are set aside (2 scrap per processed) and the order waits ("waits 3 processed" on its queue
  button). Processors run only while waiting orders need their output and only from set-aside
  scrap; idle processors are drawn dark. Builders take the first order that is ready. Cancelling
  refunds the received part as stock and the waiting part as its set-aside scrap; output from a
  processor already running lands in stock. Recipes and the item→recipe map (`PRODUCER`) are
  data, so later chains reuse this.
- **Thesis/antithesis:** pull stops processors from stealing scrap with no new button; but you
  can't stockpile processed scrap ahead of a wave. **Synthesis:** test it; if stockpiling
  matters, add a small standing reserve (a later rule card: "keep N processed").

### Clickable build buttons (2026-11-01, user: "UI buttons to click on")
- **Built:** a row of buttons per bot type (name, D-pad direction / key, cost; faded when you
  can't afford it) and the queue as buttons above it; clicking a queued unit cancels it with a
  refund (the RTS convention, e.g. StarCraft/C&C queue icons). Buttons never take UI focus, so
  the D-pad keeps queuing units instead of moving focus.
- **Bug fixed in the same change:** the build queue was cleared every frame (a stray
  `build_queue.clear()` in `_process`), so the D-pad queue from the previous change never worked.

Sources: [Fabrico: pull vs push production](https://www.fabrico.io/blog/pull-vs-push-production/),
[Push vs pull: why pull wins](https://pananth.substack.com/p/push-vs-pull-production-why-pull),
[Wikipedia: push–pull strategy](https://www.wikipedia.com/wiki/Pull_strategy).
- **Update (user, 2026-11-01): build buttons are small icons in the bottom-right corner.** 36 px
  buttons drawn in each bot's map shape and colour with a tiny key number; name, cost and D-pad
  direction show on hover. Queued units are 22 px icons above them, faded while waiting for
  processing; click one to cancel it with a refund.
- **Update (user, 2026-11-01): haulers shoot scrap off piles.** A hauler stops 80 px from a pile,
  aims for 0.5 s, fires (a short yellow line and a spark on the pile), knocks off 1 scrap and
  carries it to the hero. Applies to normal hauling and to extract orders.
- **Update (user, 2026-11-01): the hero shoots scrap too.** Same automatic rate (1 per second
  from the nearest pile in the ring) but shown as a shot like the haulers' instead of a beam.
- **Update (user, 2026-11-01): the hero collects dropped scrap.** Wrecks and scrap dropped by a
  hauler killed while carrying are now *loose scrap* (small bright squares). Loose scrap within
  90 px slides toward the hero and is collected on contact, the pickup magnet used by survivor
  games for XP gems (from memory, not checked). Haulers grab loose scrap by touch instead of
  shooting it; the hero's automatic shots skip it.
- **Update (user, 2026-11-01): the hero builds; builders only add parallel capacity.** The hero
  takes ready orders from the same queue (2 s each, a coloured arc around the hero) and moves at
  50% speed while building, so building costs mobility. Builders are optional extra lines.
  Both tests now start with 0 builders (roles: 5F 3H; processing: 4F 3H 1P). Reading of "50%
  velocity or building" as "half speed while building" is an assumption.

### Hack or scrap (AFK experiment, 2026-11-01, built from the story's verb)
- **Checked (web):**
  - **Undead Horde** (10Tons, raise killed enemies as your army): reviewers call raising enemies
    "a lot of fun" and say the army has "strategy and tactical nuances"; complaints are fragile
    minions, a command cap, and a repetitive "kill enemies, raise their bodies" loop.
  - **Weaken-then-capture:** Pax Autocratica shows a capture rate so you know when to spend the
    capture; RimWorld players down enemies without killing them; Deltarune excludes bosses from
    recruiting. Capture RNG ("missed three times, lost all three") is reported as frustrating.
- **Abstract problem:** one event (an enemy falls) with two exclusive payoffs: a specialised
  unit (hack) or a generic resource (scrap). The cost of the better payoff is the hero's position:
  hacking needs the weak hero near the fight. That ties the "where you stand" question to growth.
- **Thesis:** hacking by standing next to a downed robot (no button, no RNG, visible progress
  arc and a 5 s expiry arc) makes the hero dive into fights at chosen moments; which type you
  hack shapes the army (rushers, gunners, shields), which is the "which robots join" lever.
- **Antithesis:** Undead Horde's critique: "kill, raise" becomes repetitive, and if hacking is
  always better than scrap the choice has one answer (just hack everything). A critic would also
  say proximity-hacking turns the hero into a vacuum, not a decision-maker.
- **Synthesis:** the decision is not hack-vs-scrap per se but *which* downed robot, *when*:
  several fall at once, hack time grows with value (rusher 1.2 s, gunner 2 s, shield 3 s), and
  the shield's 3 s is long enough to be dangerous mid-fight. Scrap is the safe fallback (6 scrap =
  1 basic rusher). No RNG, following the capture-frustration reports. Variety is the laws test's job.
- **Built:** `scenes/hack.tscn` ("AFK: Hack or scrap" in the menu). Start: hero + 3 rushers.
  Six escalating waves of imperial rushers / gunners / shields from all edges, 8 s calm between.
  Automate types: rusher (fast melee), gunner (ranged 170 px), shield (10 HP; enemies within 70 px
  attack it; bullets hit its larger body). Untested beyond a headless parse/run check.
- **Pass test (user playtest):** you walk into a fight on purpose to hack a gunner or shield, and
  the army you end up with differs from run to run because of what you chose to hack.

Sources: [Xbox Tavern: Undead Horde review](https://www.xboxtavern.com/undead-horde-review/),
[PlayStation Country: Undead Horde review](https://www.playstationcountry.com/undead-horde-ps4-review/),
[Pax Autocratica guide: capturing](https://www.whisperofthehouse.com/pax-autocratica/capture-enemies-prisoners),
[Deltarune wiki: Recruit](https://deltarune.wiki/w/Recruit),
[itch.io: capture mechanics thread](https://itch.io/t/3732614/capture-mechanics).

## Hack + shoot: hero verbs (2026-11-01, user decision)

**Decision (user):** the hero can shoot and hack; hacking makes the hero 50% slower. Picked with
the user: hold-to-hack (LT / Space), auto-fire at the nearest enemy, and no shooting while hacking.

**Research.**
- Slowdowns are a standard cost of power, like a heavy weapon that slows you or a weapon you can't
  fire while moving ([Giant Bomb: movement penalty](https://giantbomb.com/movement-penalty/3015-3265/)).
- Players resent slowdowns they didn't choose, or that make an action crawl
  ([ESO forum](https://forums.elderscrollsonline.com/en/discussion/comment/5416223/),
  [Conan Exiles forum](https://forums.funcom.com/t/a-thorough-suggestion-on-how-to-make-the-slower-movement-restrictions-work-without-frustrating-pvp-and-pve-players/98869)).
- On a gamepad, manual aim is hard. Auto-aim is common, and some games auto-aim by default and
  switch to manual aim while a button is held (Halls of Torment style)
  ([Game Developer: dual-stick controls](https://gamedeveloper.com/design/everything-i-learned-about-dual-stick-shooter-controls),
  [Giant Bomb: twin-stick](https://giantbomb.com/wiki/Concepts/Twin_Stick_Control)).

**Dialectic.**
- *Thesis:* a slowdown gives hacking a cost, so each hack is a decision mid-fight.
- *Antithesis:* in the old test you hacked by standing within 48 px, so you were already standing
  still and a slowdown changed nothing. If hacking started automatically, the slowdown would hit
  whenever you walked past a wreck, the kind of slow players hate.
- *Synthesis:* a beam with 130 px reach that you hold a button to use. You can keep moving at half
  speed while it hacks, so the slowdown matters and is always chosen. Auto-fire keeps attention on
  position and timing rather than aim. Hacking stops your shots, so diving to hack a gunner
  mid-fight is a real risk. The hero's gun is weak (1 damage every 0.45 s) so the army stays the main force.

**Risk/reward:** low risk (about 50 lines on top of the hack scene), high reward (it tests the
hero's core verb). **Tension:** constraints.md says the hero is weak. The gun is kept weak for
that reason; the playtest decides whether shooting crowds out hacking.

## Everything test: all mechanics in one scene (2026-11-01, user decision)

**Decision (user):** a test that always combines every mechanic on main: gathering, roles and
processing, plus hack + shoot. AFK experiments join only after the user approves them. Both robot
sources stay as they are, and the hack and build slowdowns don't stack (50% if either is active).

**Research.** A vertical slice is meant to show the core mechanics working together
([Wayline](https://www.wayline.io/blog/vertical-slice-vs-full-prototype),
[Rami Ismail](https://ltpf.ramiismail.com/prototypes-and-vertical-slice/)). Mechanics developed in
isolation are unlikely to fit together on their own, though that source is opinion, not data.
Isolated test rooms are still the norm for checking one feature
([GB Studio Central](https://gbstudiocentral.com/?p=1711)).

**Dialectic.**
- *Thesis:* play everything together early, so clashes between systems show up.
- *Antithesis:* in a combined scene you can't tell which system caused a problem, and every
  feature has to be built twice.
- *Synthesis:* keep the single-feature scenes for isolation, and make the Everything scene the
  default place new features land (CLAUDE.md rule). Clashes found while merging:
  - Two robot sources: hacks give combat types, the queue builds its 4 types. Kept both.
  - Two slowdowns on the hero (hack, build). The minimum applies, so they don't stack.
  - Two hero auto-shots (enemies, piles). Hacking pauses both.

**Risk/reward:** medium risk (the hack code is copied into a subclass of the processing test),
high reward (it shows whether the economy and the combat verb work together).

## Exploration in the Everything test (2026-11-01, user decision)

**Decision (user):** scrap and enemies scattered everywhere, a camera that follows the hero, an
**infinite** world, and enemy camps plus slow patrols in place of the timed waves.

**Research.**
- Camps pace the game by space (the player picks when to fight); waves pace it by time (the game
  sets the rhythm). Many top-down roguelites use both, with camps as set pieces and waves to fill
  the gaps or punish idling ([itch devlog: wave systems](https://itch.io/devlog/755554/build-5-roguelike-wave-system-update.amp)).
- Keep wake-up radii small and per camp, so one encounter doesn't pull the whole area
  ([bugnet: group aggro](https://bugnet.io/blog/how-to-fix-unreal-group-aggro-pulling-whole-room),
  [WoW aggro radius](https://warcraft.wiki.gg/wiki/Aggro_radius)).
- Godot's Camera2D has built-in position smoothing; use `get_screen_center_position()` for the
  real view center, and `reset_smoothing()` to snap
  ([Godot docs](https://docs.godotengine.org/es/4.3/classes/class_camera2d.html),
  [uhiyama-lab](https://uhiyama-lab.com/en/notes/godot/camera2d-techniques/)).

**Dialectic.**
- *Thesis:* camps let the player choose fights, which is where exploration becomes a decision.
- *Antithesis:* with camps alone, the player can farm safe scrap forever. And an infinite world
  grows without end, both in memory and in chasers piling up behind the hero.
- *Synthesis:*
  - A patrol every 45 s, growing slowly, so standing still costs something.
  - The world is made in 640 px chunks as the hero nears them, seeded per chunk.
  - Camps grow with distance from the start, so walking outward is the difficulty curve.
  - A 1400 px leash: camp members left far behind fall asleep where they stand, and patrols leave.

**Risk/reward:** medium risk (the arena clamps became overridable `_bound()` calls in mvp, gather
and roles, and the HUD is redrawn in screen space), high reward (it tests the "demand" open
question: what pulls the hero across the map).
**Known limit:** generated chunks are never unloaded. A headless walk of about 11,000 px held
about 440 enemies, mostly asleep, with no errors. Frame rate on a long run isn't measured.

## Universal rules instead of per-type rules (research, 2026-11-01, user question)

**User idea:** universal rules like the Game of Life, instead of a rule per robot type.

**Checked (web):**
- **Particle Life** (Mohr, Ventrella; many itch sandboxes such as Abiogenesis): one force rule for
  every particle, plus an attraction matrix with one number per pair of types (positive pulls,
  negative pushes). The matrix is asymmetric, and editing it gives predator/prey and creature-like
  shapes ([Tenstorrent cookbook](https://docs.tenstorrent.com/tt-vscode-toolkit/lessons/cookbook-particle-life/),
  [Abiogenesis](https://dylanrjohnston.itch.io/abiogenesis)).
- **Boids as gameplay:** a research game has the player tune the separation, cohesion and alignment
  weights to change the flock's formation, and so its success
  ([Mammen 2009](https://downloads.hci.informatik.uni-wuerzburg.de/Mammen2009yg.pdf)). Tuning
  advice: cohesion weakest, or the flock collapses into a blob
  ([bugnet](https://bugnet.io/blog/how-to-fix-boids-flocking-clumping-into-one-point)).
- **Baba Is You:** the level's rules are blocks in the world (WALL IS STOP). A rule applies to every
  object of that noun while its blocks stay intact
  ([Wikipedia](https://en.wikipedia.org/wiki/Baba_Is_You), [Unwinnable](https://unwinnable.com/2019/04/03/baba-is-you-rules/)).
- **Automata Empire:** a Game of Life–inspired strategy game where you herd hundreds of mindless
  automata ([Bottin](https://lebottinlinux.vps.a-lec.org/Bottin_0-C_files/Automata_Empire-15000.html)).
  **Rule 110 Hero Defense:** a 1D cellular automaton that the player edits to protect a pattern
  ([itch](https://ndry.itch.io/rule110-hero-defense-ppoc)).
- **Screeps:** one script runs every unit each tick; in practice players still split it into roles
  ([Overmind](https://github.com/bencbartlett/overmind)).
- **Liquid War** (already in this log): one rule for all (shortest path to the cursor).
- **Not found:** a commercial game where the player rewrites a Life-style rule set (like B3/S23) mid-battle.

**Abstract problem:** a universal rule is one function every unit runs on what it senses nearby.
It can't name a role ("haulers carry"), but it can name relations between kinds ("X keeps near Y,
X avoids Z"). Particle Life shows the middle ground: one rule, with parameters per pair of kinds.

### Universal rules: low-risk version built (2026-11-01, user: "build the low risk version")
- **Built in the Everything test:** 4 type-blind rules that every robot runs on what it senses (allies,
  meaning robots and the hero, within 80 px; awake enemies within 120 px), each with low / mid / high:
  - TETHER (150 / 300 / 500 px): farther than this from the hero, walk back. Haulers also fetch
    piles this far out.
  - LONELY (off / 1 / 2 allies): fewer allies nearby than this, move to the nearest ally.
  - CROWD (3 / 6 / 12): more allies nearby than this, step away from them.
  - COURAGE (0.5 / 1 / 2): enemies nearby above (allies + 1) × this, retreat to the hero.
  - **Fixed order** (part of the design, not set by the player): COURAGE > TETHER > LONELY >
    CROWD > the robot's job. A rule takes over only the movement; job timers and actions continue.
- **Controls:** hold LB / Q, then the D-pad or 1–4 cycles a rule (up TETHER, left LONELY, right CROWD,
  down COURAGE). Changes are live. Without LB the D-pad still queues builds.
- **Readable:** a panel top-left shows each rule's setting and how many robots it is driving now.
  Each robot shows the letter of the rule driving it (T / L / C / R).
- **Why low risk:** no editor and no pausing, just 4 dials. It reuses the jobs and adds one sensing pass
  (O(n²) over robots, fine below about 150). **Deferred:** a pause or between-fights editing, more
  rules, and per-pair rules (Particle Life style).
- **Pass test (user playtest):** you change a rule because the situation changed (far scrap, a camp,
  a patrol), the army's shape visibly changes, and no single setting is best everywhere.

## Why the universal rules feel non-strategic (2026-11-01)

The user's playtest verdict: "these rules don't have strategic value."

- **Interesting decision = a trade-off.** If one option is clearly best, the choice is just an evaluation, not a dilemma ([Game Developer](https://www.gamedeveloper.com/design/designing-interesting-decisions-in-games-and-when-not-to-), [Plymouth course](https://creatinggames.press.plymouth.edu/?p=113)).
- **FF12 Gambits:** each rule is condition → action on a target, in a priority order. The strategy is shaping *what* allies do, not micro-managing them ([StrategyWiki](https://strategywiki.org/wiki/Final_Fantasy_XII/Gambits), [PlayStation Blog](https://blog.playstation.com/?p=192698)).
- **Diagnosis of the current rules** (read from the code):
  - They are free knobs. There is a best setting, so you set it once and forget it.
  - They only change spacing and movement, never what a robot chooses to do (target, job, resource).
  - Nothing in the run flips which setting is right.

## Links → bot tree with auto-rebuild (idea, 2026-11-01)

The user proposed links between bots, then tree branches for input/output, with the builder automatically building into the tree.

- **Factorio ghosts:** a destroyed entity leaves a "ghost", and construction robots rebuild it, but only if the items are in stock and a robot is free. The player edits the plan; robots maintain the units ([wiki: Ghost](https://wiki.factorio.com/Ghost), [wiki: Construction robotics](https://wiki.factorio.com/Construction_robotics_(research))).
- **Why it fits Assemblia:**
  - A plan-level tree survives losses, so links don't die with bots.
  - It's edited once, not per unit, which is easier on a gamepad.
  - It replaces the manual build queue.
- **Built (user, 2026-11-01): "Links" test** (`scripts/links.gd`, extends Baseline). Everything was renamed to Baseline and its universal rules were removed. The user said a factory game is intended.
  - **The tree:** rooted at the hero, max 16 nodes.
  - **Link types:**
    - feed: a hauler brings scrap to its processor or the hero;
    - refine: a processor turns 2 scrap into 1 processed and pushes it up to the hero;
    - guard: a fighter stays by its parent;
    - build: a builder builds ghosts.
  - **Ghosts:** a ghost auto-queues in tree order and is refilled when its bot dies. Manual queueing is off.
  - **Editing:** the tree is edited while paused.
  - **Thesis:** the plan, not the units, is what the player shapes, and it survives losses.
  - **Antithesis:** the hero moves, so the "factory" moves with it, and a paused editor breaks flow.
  - **Synthesis (cheapest test):** everything follows the hero for now. Planted outposts come only if the playtest asks for them.

## Factorio feel in the Links test (2026-11-01)

The user asked: "how can we have factorio in the link playtest?"

**What the fun is**
- **Visible bottlenecks.** A starved belt, a stalled inserter or an empty chest shows where to look, and the player asks "why?" every few minutes ([supercraft](https://supercraft.host/article/factorio-automation-constraints/), [mental models](https://mjwest.notion.site/Strategy-games-can-teach-mental-models-e11631f479e14a679ab9963f890db454)).
- **Ratios can be eyeballed.** Add machines until it looks right; perfect math is optional ([forum](https://forums.factorio.com/viewtopic.php?p=259578)).
- **Automation is the core loop.** Inconvenience teaches you to automate; space limits push layout thinking ([OSU blog](https://blogs.oregonstate.edu/cgainesblog/2023/01/10/hello-world/)).
- **Mindustry is the closest hybrid.** Its supply lines feed turrets while waves attack the core ([Steam](https://store.steampowered.com/app/1127400/Mindustry/)).

**What Links lacks** (read from the code)
- **No space.** Everything follows the hero, so distance never limits throughput.
- **One recipe.** There are no ratios.
- **No bottleneck view.** You can't see which node is starved or backed up.
- **Removed (user, 2026-11-01):** the Links test was deleted before it was playtested. The code is not in git history (it was never committed).

## Mobile factory: what it needs beyond the Baseline (2026-11-01, user: "Mindustry/Factorio but non-settle")

**Checked (web):**
- **Factorio Space Age platforms** are the closest precedent: a factory that travels. Thrusters
  burn fuel the platform makes from asteroids it catches on the way; more thrust brings more
  asteroids, so turrets (fed from the same asteroids) go at the front, where hits come from
  ([wiki: Space platform](https://wiki.factorio.com/Space_platform), [wiki: Thruster](https://wiki.factorio.com/Thruster),
  [supercraft guide](https://supercraft.host/wiki/factorio/space_platform_optimization/), community advice).
- **Mindustry:** belts feed turrets with ammo, coolant and power; belts back up and stop accepting
  items, which is the visible bottleneck ([Steam](https://store.steampowered.com/app/1127400/Mindustry/),
  [devlog](https://anuke.itch.io/mindustry/devlog/8406/15)).
- **Moving-base games** (Steel Ark, Trainfort, Lost Heaven Station, Factorio "Factory Train" mod)
  exist but none is a roguelike mobile factory with an army
  ([Steel Ark](https://store.steampowered.com/app/3915840/Steel_Ark), [Factory Train](https://mods.factorio.com/mod/factory-train)).

**Abstract problem:** a factory game is a network that turns inflows into outflows under limits,
against a demand that keeps growing. Settled: inflow fixed (ore patch), player shapes the network.
Mobile: inflow is what you pass over, so the route is part of the network.

**Gaps in the Baseline** (read from the code): production only spends on building bots, so once
the army exists the factory idles (no continuous sink); one raw input, one recipe (no ratios);
nothing limits throughput but bot count; no starved/blocked view; patrols are the only push to move.

**Dialectic (continuous sink):**
- *Thesis:* fighters burn ammo that haulers deliver, as in Mindustry; the factory never idles.
- *Antithesis:* per-unit resupply reads as micromanagement and could make fights a supply chore.
- *Synthesis:* the army refills itself (haulers deliver, no player action); the player only sees
  dry fighters dim, and fixes it through composition and route, never per unit.

## Layout without settling (research, 2026-11-01, user: "we want layout")

**Abstract problem:** layout matters in a factory game because (1) distance costs throughput,
(2) position decides exposure, (3) space is scarce, so placement is a trade-off. To keep layout
while moving, positions must live in a frame that moves with you, not in the world. The open
choice is that frame's shape: a 2D grid, slots around the hero, or a 1D chain.

**Checked (web):**
- **Cosmoteer:** crew carry power and ammo by walking inside the ship, so distance between
  producer and weapon decides how many crew you need; players move reactors next to weapons and
  chain storages to shorten walks ([wiki: Crew](https://cosmoteer.wiki.gg/wiki/Crew),
  [forum guide](https://forum.cosmoteer.net/d/8610/650), [0.15.2 devlog](https://itch.io/devlog/100897/cosmoteer-0152-reactor-factory-assignments.amp)).
- **Factorio space platforms:** a real factory layout on a moving grid; turrets go at the front
  because that's where hits come from ([wiki](https://wiki.factorio.com/Space_platform),
  [supercraft](https://supercraft.host/wiki/factorio/space_platform_optimization/)).
- **SNKRX:** units are segments of a snake; class synergy plus position along the snake are the
  strategy, and a longer snake gets hit more, so placement matters
  ([Screenhub](https://www.screenhub.com.au/news/features/you-should-play-snkrx-1467299/),
  [Steam](https://store.steampowered.com/app/915310/SNKRX/)).
- **Backpack Battles:** in an auto battler the layout is the player's only input; adjacency
  triggers combos and limited space makes it a puzzle; complaint: too much time fiddling
  ([GamingOnLinux](https://gamingonlinux.com/2024/03/backpack-battles-is-another-clear-indie-steam-hit),
  [Playpile](https://playpile.gg/games/backpack-battles)).
- **TerraTech:** mobile refineries and fabricators bolted onto a driven vehicle
  ([dev diary](https://Www.moddb.com/games/terratech/news/terratech-dev-diary-building-your-base-in-space)).
  **Factorissimo:** "want a mobile base? put everything inside a building"
  ([mod page](https://mods.factorio.com/mod/Factorissimo)).

**Candidate frames:**
- **A. Grid on a carrier** (Cosmoteer, space platform, Backpack): proven factory layout. Conflicts
  with the solid "no grid editor" constraint.
- **B. Formation grid around the hero:** bots hold slots relative to the hero; haulers walk
  between slots, so distance = throughput; front faces the walking direction. Also a grid editor,
  but nothing placed in the world.
- **C. Chain / snake** (SNKRX, train wagons): 1D order; neighbours feed each other; head meets
  threats, tail gets chased. Fits the constraint, gamepad-easy, but shallow as a factory.
- **D. Tree / graph** (the deleted Links test): topology, no geometry, so no distance trade-off.
  Not really layout.

**Dialectic:**
- *Thesis:* B — Cosmoteer's lesson (distance = crew = throughput) carried on the hero, with the
  front set by walking direction, gives Factorio-style layout that never settles.
- *Antithesis:* B breaks "no grid editor"; Backpack players complain about fiddling; and when the
  hero turns, the whole layout rotates, so "front" may feel arbitrary.
- *Synthesis (proposed):* B with a small grid (about 5×5), edited by type per slot while paused,
  front locked to walking direction. The constraint was set for the old first-person army; asking
  the user to relax it. C is the fallback if they keep it.

### Layout without a grid editor (research, 2026-11-01, user asked alongside the grid test)

**Abstract problem:** without an editor, the layout has to be a by-product of something the
player already does in the world: where they are, what order they act in, or one coarse choice.

**Checked (web):**
- **Attach where it touches** (Katamari style): in Katamari Mech Spacey, parts from destroyed ships
  stick to your ship wherever you run into them; Captain Forever builds ships from parts torn off
  enemies ([Katamari Mech Spacey](https://dragonforge-development.itch.io/katamari-mech-spacey),
  [Captain Forever Remix](https://pixelsaurusgames.itch.io/captain-forever-remix)).
- **Formation presets** (Homeworld): sphere wraps a big ship and adds turret cover but costs
  maneuverability; wall works defensively; wedges punch through; in competitive RTS play
  formations are rarely used beyond a box, and need unit caps / overflow logic
  ([Homeworld forum](https://steamcommunity.com/app/244160/discussions/0/617329150702130464),
  [PA forum](https://forums.planetaryannihilation.com/threads/unit-formations.43933/page-2),
  [moddb dev update](https://www.moddb.com/news/fighters-and-heavy-frigate)).
- **Hardpoints** (MechWarrior Online): a few fixed mounts per body section (left/right torso,
  front/rear); players read and target sides, so side choice matters
  ([MWO wiki: Mech Lab](https://mwo.fandom.com/wiki/Mech_Lab),
  [MWO forum](https://mwomercs.com/forums/topic/247645-how-do-i-know-where-my-weapons-will-be/)).
- **Order as layout** (SNKRX, trains): already above.
- **Assignment as layout** (Cosmoteer storage chains): you link producer → storage and the crew
  routes follow; position comes from the links (above).

**Candidates without an editor:**
- **Dock where you touch:** a new bot docks to the formation at the edge where it meets it; you
  choose the side by how you walk. Fits "your position is the command". Needs a way to undo.
- **Side by build direction:** the D-pad direction you build with picks the side (front/left/
  right/back hardpoints). Very cheap; 4 lanes, not a grid.
- **Formation preset:** one shape choice (wedge / ring / column); roles placed by fixed rules.
  Shallow: one decision, and RTS players mostly ignore formations.
- **Chain order:** see SNKRX above.

**Dialectic:** *thesis:* dock-where-you-touch gives a real 2D layout with no editor. *Antithesis:*
it's imprecise and hard to correct, and it mixes layout with combat movement. *Synthesis:* test the
grid editor first (user's pick) to learn whether layout matters at all; if it does, try docking as
the no-editor version of the same grid.

## Walking machine: fixed grid, expandable, units + blocks (2026-11-01, user idea; replaces the rotating grid test)

**User idea:** a walking machine with a fixed grid that doesn't rotate; the grid grows by adding
blocks; the army has units (walk off) and blocks (sit on the grid).

**Does it exist? (web)** In parts, not combined:
- **The Wandering Village:** a city on the back of a walking creature; the limited space on its
  back makes layout and production chains matter more than in usual city builders
  ([Steam](https://store.steampowered.com/app/1121640/The_Wandering_Village), [PC Gamer](https://www.pcgamer.com/au/this-city-builder-takes-place-on-the-back-of-a-huge-wandering-creature)).
- **Wanderburg:** a roguelike castle on wheels that grows with modules and destroys what's in its
  path ([GamingOnLinux](https://www.gamingonlinux.com/2026/02/battling-castles-on-wheels-wanderburg-might-be-my-new-favourite-thing),
  [Steam](https://store.steampowered.com/app/4847340/)). **Castle Come:** a walking-fortress
  roguelike ([Gematsu](https://www.gematsu.com/2024/06/walking-fortress-roguelike-game-castle-come-announced-for-consoles-pc)).
  **Fortblox:** a walking tank built from blocks ([Pocket Gamer](https://www.pocketgamer.com/fortblox-mobile-fortress-go/official-launch/)).
- **Factorio space platforms:** a factory on foundation tiles you add one by one; mass matters
  (above). **Mindustry:** blocks (buildings) plus units, but on a settled map.
- **Not found:** a walking factory with a production chain on its grid *and* units that leave it.
  That combination is Assemblia's angle.

**Dialectic:**
- *Thesis:* a fixed grid reads clearly (no rotation), tiles make growth a visible choice, and
  splitting units from blocks gives each a clear job: blocks process, units fetch and fight.
- *Antithesis:* if the grid only holds processors and builders, layout only means "distance to the
  core" — one number, so the closest tile is always best. And an unlimited grid is no constraint.
- *Synthesis (built):* tiles cost scrap and each tile slows the machine (Factorio-platform mass),
  so growing trades speed for capacity. The distance cost stays. **Known gap:** layout depth needs
  blocks that care about neighbours or facing (e.g. turrets at the edge, adjacency); add next if
  the playtest shows layout is flat.

## Single player or multiplayer? (2026-11-01, user: "i feel this game is for single player")

**Checked (web, mostly developer opinion and third-party sales estimates):**
- Indie multiplayer often dies for lack of players; servers and netcode are an ongoing cost; a
  single-player game can be revived later, an empty multiplayer game rarely can
  ([MCV: Dan Marshall](https://www.mcvuk.com/development/why-indies-probably-shouldnt-make-a-multiplayer-game),
  [bugnet](https://bugnet.io/blog/single-player-vs-multiplayer-support-burden)).
- Co-op "friendslop" hits (Lethal Company, R.E.P.O., PEAK) sell huge, but they're built around
  shared chaos, voice chat and clip-able moments, with rough visuals
  ([AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)).
- Factorio-style sims need deterministic lockstep for multiplayer; it's hard, has to be designed in,
  and desyncs are a lasting cost; Factorio's multiplayer took years
  ([FFF #76](https://factorio.com/blog/post/fff-76), [FFF #188](https://factorio.com/blog/post/fff-188)).

**Dialectic:** *thesis:* co-op is where the 2025 money was. *Antithesis:* those hits are a different
genre (social chaos), and online co-op in a factory sim is the highest-risk work this project could
take on. *Synthesis:* single player. Local couch co-op (a second hero on the same machine, no netcode)
stays a possible cheap add-on later; decide only after the core loop is fun.

### 2026 indie hits: single player vs co-op (2026-11-01, user request)
Third-party estimates (Sensor Tower, Alinea, press), not Valve data.
- **Market:** Sep 2025–Aug 2026, indie games selling 500k+ in month one rose 13 → 33; friendslop
  co-op was 46% of indie first-month sales ([Sensor Tower](https://sensortower.com/blog/indie-and-new-ip-break-out-without-denting-aaa)).
- **Single player:** Slay the Spire 2 (~7M Steam units, ~$140M in 3 months), Mewgenics (~1.8M),
  Paralives, Cairn, Mina the Hollower; Stardew Valley at 50M lifetime
  ([Sensor Tower StS2](https://sensortower.com/blog/mega-crits-slay-the-spire-ii-slays-with-7-million-units-sold),
  [gamerempire](https://gamerempire.com/blog/best-new-indie-games-steam)).
- **Co-op:** MECCHA CHAMELEON (13.3M in 30 days, 2-person team), How to Fish (7.9M in 30 days),
  RV There Yet? (1.3M), Yapyap (500k+), Gamble With Your Friends (500k in 3 days)
  ([OpenCritic](https://opencritic.com/news/33920/viral-co-op-friendslop-game-sells-over-10-million-copies-since-june-9),
  [GamesRadar](https://www.gamesradar.com/games/co-op/another-friendslop-hit-prints-money-on-steam-as-gamble-with-your-friends-sells-500k-copies-in-3-days-speechless/)).
- **Our niche (factory/automation roguelike):** no 2026 breakout found; A Factory Roguelike is tiny,
  Alchemy Factory (89% of 1,470) is a tycoon sim, Beltfed (factory-defense roguelike) is due 2027
  ([Steam](https://store.steampowered.com/app/3669570/Alchemy_Factory/), [Rogueliker](https://rogueliker.com/beltfed-roguelike-factory-defense-announcement-trailer-steam/)).

### Cost to make: co-op hits vs single-player hits (2026-11-01, user: "effort/risk vs return")
- **Co-op hits are small and fast:** MECCHA CHAMELEON, 2 people, 2 months (4–5 counting reused
  systems), "make it exist first, perfect it later" + asset reuse
  ([Automaton](https://automaton-media.com/en/news/meccha-chameleon-developers-say-the-secret-behind-their-2-month-dev-cycle-is-asset-reuse-and-a-make-it-exist-first-perfect-it-later-approach/),
  [PC Gamer](https://pcgamer.com/games/sports/based-on-meccha-chameleons-incredibly-short-2-month-dev-cycle-its-creators-have-already-earned-usd1-million-per-day-of-work/)).
  Lethal Company: solo. How to Fish: a $5 game.
- **Single-player hits are slow:** Balatro, solo, ~3 years (Dec 2021 → Feb 2024)
  ([Nintendo Life](https://www.nintendolife.com/news/2025/03/i-felt-totally-overwhelmed-balatro-dev-releases-development-timeline));
  Slay the Spire 2, ~10 people, ~5 years ([Wikipedia](https://en.wikipedia.org/wiki/Slay_the_Spire_II)).
- **Hit rate:** no data found. Analysts call friendslop "random, hit driven"; some releases get no
  attention ([Game World Observer](https://gameworldobserver.com/2026/08/03/analyst-there-are-many-games-in-the-friendslap-niche-but-it-is-not-oversaturated),
  [Gamereactor](https://www.gamereactor.eu/arc-raiders-friendslop-games-continue-to-sell-huge-numbers-in-2026-1670383/)).
- **Reading:** the co-op hits are cheap because they're small toys whose content is the players'
  reactions, not because co-op is cheap. Adding co-op to a given game adds cost. Assemblia
  (systemic factory roguelike) is in the slow, deep category either way.

## Short-dev hits: co-op vs single player (2026-11-01, for the next project after Assemblia)
Sales are third-party estimates or press; dev times are from developer interviews where found.

| Game | Mode | Team | Dev time | Result |
|---|---|---|---|---|
| MECCHA CHAMELEON | co-op | 2 | 2 mo (4–5 with reuse) | 13–20M |
| PEAK | co-op | 7 (2 studios) | ~1 mo jam, ~4 mo total | 11M Steam |
| RV There Yet? | co-op | small studio | 8–9 weeks | 4.5M |
| Content Warning | co-op | 5 | ~2 mo | 1M paid (+6M free) |
| YAPYAP | co-op | ~10 | <1 yr | 1M in 6 weeks |
| How to Fish | co-op | 2 | ~1 yr | 7.9M month one ($5) |
| Gamble With Your Friends | co-op | ~9 | ? | 1M in <2 weeks ($8) |
| Lethal Company | co-op | 1 | ? | 19M |
| Schedule I | co-op | 1 + artists | ? | 3M+ month one |
| WEBFISHING | co-op | ? | ~5 mo | ? |
| Megabonk | single | 1 | ~8 mo | 1M in 2 weeks |
| A Short Hike | single | 1 (+composer) | ~7 mo | ~0.6–1.1M est. |
| Vampire Survivors | single | 1 (+friends) | ~1 yr to EA, £1,100 spent | millions |
| Buckshot Roulette | single | 1 | ? | 8–9M ($3) |
| CloverPit | single | 2 | ? | 1M in ~1 month |
| Mouthwashing | single | 5–7 | 15 mo | 800k |
| The Operator | single | 1 | ? | ~$1.2–1.6M |
| Nubby's Number Factory | single | 1 | 1.5–2 yr | 44k–638k (estimates conflict) |
| Balatro (reference) | single | 1 | ~3 yr | 5M+ |

**Base rate (survivorship check):** median Steam game earns ~$250 (2025) to ~$1,100 lifetime (2019
cohort); ~66% earn under $1,000 ([80.lv](https://80.lv/articles/analysts-report-drop-in-game-revenue-on-steam-despite-growing-number-of-releases),
[Gamalytic](https://gamedevreports.substack.com/p/gamalytic-67-of-games-on-steam-earned)).
**Co-op tail:** co-op sells 3.53× its week-one copies in year one vs 2.5× for non-co-op
([GameDiscoverCo via gamedevreports](https://gamedevreports.substack.com/p/gamediscoverco-the-long-tail-of-steam)).
**Co-op retention:** friendslop retains poorly (Content Warning D30 ~3%) ([AppMagic](https://appmagic.rocks/blog/friendslop-steam-games-2025)).
**Pattern:** short co-op hits are mostly 2–10 person teams, often studios with earlier hits (Landfall,
Aggro Crab) reusing tech; short single-player hits are often solo, on a proven loop with one sharp
twist (survivors-like, slot/poker roguelike, one-room horror).

## Next-game report (2026-11-01)
Full per-game analysis, co-op vs single comparison and genre ranking: `docs/next-game-report.md`.
Correction to the table above: Megabonk took ~13 months (Wikipedia), not 8.

## Co-op / furry friendslop report (2026-11-01)
User chose a furry friendslop next. Success vs failure patterns, subgenre map, open verbs and furry market: `docs/coop-report.html`. Key: no Steam Furry tag; sell as "cute animal chaos"; measured failures cluster at $20-30 and live-service matchmaking; open verbs: raise creature, move house, deliver, build, garden, dig.

## Upcoming radar + trends (2026-11-01)
- Radar (catalogue of ~75 upcoming/recent co-op games, open vs closing verbs, free species, potential ranking): `docs/upcoming-report.html`.
- Trends (buyers, sub-trend lifecycle since 2018, 2027 forecast): `docs/trends-report.html`.
- Key: animal co-op filling fast (Dumpster Gang, Haunted Paws, Fart Together, Among Paws); BOMBANANA! (monkeys) is an animal co-op hit led by its verb; open verbs: raise one creature together, babysitting, camping, band, beekeeping; job/format chaos climbing, horror and mic gimmicks fading; MECCHA "half on PlayStation" claim unverified.
- Web-search session cap (200) ran out mid-research; many upcoming rows lack price/traction.

## Red Button Experiment idea check (2026-11-02/03)
User dropped Hordeline (hard to find good ideas on a Vampire Survivors base) and chose **Red Button Experiment**:
2–8 friends, one room, one red button, press 1B times to escape; incremental upgrades + a Simon Says narrator
that changes the button; falling ceiling as timer; narrator memory across runs. Design: `~/Playground/red-button-experiment/docs/design.md`.
- Incremental + friendslop: only 2 of 572 friendslop games in the 2026-11-01 scan carry the Incremental tag
  (Stress Buddy, The Legendary Sortsmith; unreleased, 9 and 4 followers). Checked (Steam).
- Proof of parts (checked, Steam, 2026-11-02): Schedule I 294k reviews; A Game About Digging A Hole 19k ($4.99);
  PlateUp! 19k; Overcooked! 2 63k; Pummel Party 46k; PICO PARK 24k ($4.99); Stanley Parable UD 35k.
- Red-button rivals: mostly solo joke games, best 101 reviews / 772 followers. **Closest: Don't Press This Sh*t**
  (appid 5423880): co-op 1–4, room with 1,000 "fingers" with random effects, survival + journal; releases
  2026-11-11, 4 followers. Watch its launch.
- Name: Steam exact-title search free for "Red Button Experiment" (no trademark search).
- Voice: non-union indie VO ~$100–600/h (web rate guides, conflicting) → ~$1–4k for 300–500 lines; chose AI
  facility voice instead (Steam AI disclosure).
