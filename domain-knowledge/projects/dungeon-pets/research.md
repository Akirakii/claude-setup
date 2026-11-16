# Design research

Reference games and what we take from each, collected while building. Each section names the
game system it informed. Sources are listed at the bottom of each section.

## Reference games

| Game | Why it's relevant | What we take |
|---|---|---|
| **Slay the Spire** | Roguelike runs, map planning, enemy intents | Enemy intent shown before it acts; route choice on a visible map |
| **Into the Breach** | Perfect-information tactics | Telegraphed attacks the player can redirect (carry/throw/taunt) |
| **Darkest Dungeon** | Party management, provisions, scouting | Scouting reveals rooms ahead; provisioning for the next area; party bonds/stress |
| **Pikmin** | Throwing and carrying your crew | Throwing creatures at enemies; carrying as a core verb; crew assignment to tasks |
| **Hades** | Room-by-room rewards | Reward preview before entering, so the route is a choice |
| **Enter the Gungeon** | Procedural floors from hand-made rooms | Room templates per role (combat, hub, reward, boss), structured "flows" |
| **Spelunky** | Procedural levels with readable rules | Room templates with variation; consistent hazards that interact (traps hit enemies too) |
| **Pokémon / Dragon Quest Monsters** | Creature collecting, evolution, types | Elemental matchups, evolution as visible growth |
| **Palworld** | Creatures as companions and workers | Creature personality and utility outside combat |
| **FTL** | Crew + resource management under pressure | Every resource (food, HP, time) is spent on a choice; floor events |

## Knowledge to plan (strategy layer)

Strategy comes from information the player can act on before committing.

- Slay the Spire shows each enemy's next move (attack damage, block, buff) above it, which turns
  combat into planning. Into the Breach telegraphs every enemy move and lets the player redirect it.
- Darkest Dungeon's scouting reveals nearby rooms and corridors, so players reroute around threats
  or skip empty rooms to save supplies; provisioning depends on the area ahead.
- Hades shows the next room's reward on its door, so players weigh reward against danger.

**Applied:** enemy intent markers (target + attack timer), a floor map with scouting (Gloomowl scouts
far), room reward icons on the map once scouted, a persistent codex of enemy weaknesses, the portal
previewing the next floor's modifier, pack stances (Aggressive / Guard / Sneak) to choose which rooms
to fight.

Sources: [Into the Breach's UX makes you feel smart](https://blog.prototypr.io/into-the-breachs-ux-makes-you-feel-smart-a9cb03210757),
[Slay the Spire review (Nintendo Life)](https://nintendolife.com/reviews/switch-eshop/slay_the_spire),
[Into the Breach review (Destructoid)](https://www.destructoid.com/review-into-the-breach/),
[Darkest Dungeon: Scouting](https://darkestdungeon.wiki.gg/wiki/Scouting),
[Darkest Dungeon: Expeditions Guide](https://darkestdungeon.wiki.gg/wiki/Expeditions_Guide),
[Hades door symbol meanings (Shacknews)](https://shacknews.com/article/122186/door-symbol-meanings-hades).

## Throwing and carrying the crew

- Pikmin's developers found throwing alone wasn't interesting until they asked "what happens after
  the throw?"; sticking to enemies and carrying things home gave the verb its depth.

**Applied:** a throw has a consequence on landing (impact damage, knockback, the creature engages that
enemy, a dizzy moment), and carrying has jobs: rescue a fainted creature from a fight so it can get up,
and place creatures on pressure plates.

Sources: [Ask the Developer: Pikmin 4 (Nintendo)](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-10-pikmin-4-part-1/).

## Dungeon layout and room variety

- Enter the Gungeon hand-designs and playtests rooms, then assembles them procedurally along a handful
  of structured layouts ("flows") per floor; rooms have roles (normal, hub, reward, boss), and many
  chests sit behind loops. The developers found hand-made rooms more fun and fair.

**Applied:** room *templates* (pillared hall, ring, cross, garden, flooded, collapsed, arena) stamped
into generated rooms, room roles beyond combat, and rewards placed off the main path.

Sources: [Dungeon Generation in Enter the Gungeon (Boris the Brave)](https://www.boristhebrave.com/2019/07/28/dungeon-generation-in-enter-the-gungeon),
[Studying dungeon generation in Enter the Gungeon (80.lv)](https://80.lv/articles/studying-dungeon-generation-in-enter-the-gungeon/),
[Q&A: the guns and dungeons of Enter the Gungeon](https://gamedeveloper.com/design/q-a-the-guns-and-dungeons-of-i-enter-the-gungeon-i-).

## Expression swaps on 3D anime models (the "> <" eyes)

- Anime-style models switch expressions with hard swaps rather than smooth blending: either a
  **texture swap** of the face/eye texture, or **floating alpha eyes**: small eye planes with alpha
  textures sitting on the face (the Twilight Princess method). Some models swap geometry instead
  ("blendshapes without the blendshape"). The known downside of alpha planes is a visible edge where
  the plane meets the face.
- Our Meshy models bake the eyes into the single base-color texture, so the expression must live in
  that texture: **texture swap**. Overlays drawn on top of the face (billboards, alpha patches) were
  tried and rejected by the user: they read as stickers, not the character's own eyes.
- Plan: paint an expression copy of the base-color texture at the eyes' UV coordinates (found by
  ray-casting the T-pose mesh at the eye positions taken from the concept image), then swap the
  material's albedo texture while the emote is active.

- **Painting the copy (test: Bloomling stage 1, `tools/paint_expression.py`).** Thesis: use Blender's
  projection painting ("project from view" / stencil), the standard tool for painting across UV
  patches. Antithesis: it is an interactive viewport tool with no documented headless path, and the
  installed Blender build doesn't start (MaterialX library mismatch); hand-painting flat on the atlas
  fails because the eyes are cut into many patches at different sizes and rotations. Synthesis: the
  per-texel method the search pointed to: rasterize each triangle in UV space, interpolate each
  texel's 3D point with barycentric weights, keep texels that face a front orthographic camera and
  pass its z-buffer, and draw the expression as a function of the front-view 2D point. Every patch
  gets the same drawing at the same 3D spot, so it lines up across seams by construction; a 1.5-texel
  bleed past patch edges keeps filtering clean. Pure numpy, no Blender. Note: the game uses the
  rigged GLB's embedded texture (extracted as `<id>_s<N>_rigged_Image_0.jpg`), whose atlas layout
  differs from `<id>_s<N>_base_color.png`.

Sources: [Blender manual: texture painting (projection onto UVs)](https://wiki.blender.jp/Doc:2.6/Manual/Textures/Painting),
[Blender API: ImagePaint](https://docs.blender.org/api/blender_python_api_current/bpy.types.ImagePaint.html),
[Blender Artists: projecting an image onto geometry from the camera](https://blenderartists.org/t/is-it-possible-to-project-an-image-onto-geometry-from-the-camera/646809),
[Polycount: recreating Nintendo's eye method](https://polycount.com/discussion/comment/2658493),
[Polycount thread (geometry swap)](https://polycount.com/discussion/comment/2658311),
[Blender Artists: texture for facial animation](https://blenderartists.org/t/texture-for-facial-animation-how/395575).

## Room shapes and organic variety (generation upgrade)

- Common pattern: a structured method (BSP, Poisson sampling or a room-and-corridor graph) guarantees
  rooms, connectivity and playability; then cellular automata roughen edges for organic shapes.
  Cellular automata alone weren't enough for controlled designs in one study. Square rooms look
  unnatural, so generators add noise to room outlines.

**Applied:** keep the MST + loops room graph and A* corridors (guaranteed connectivity), stamp shape
templates into rooms (pillars, round, cross, ring, split, cave-roughened), then flood-fill from the
entrance and fill any disconnected pocket so every spawn point is reachable.

Sources: [Cave dungeon generation devlog](https://teamconcode.itch.io/the-way-home/devlog/266612/cave-dungeon-generation),
[PCG book: dungeons](https://antoniosliapis.com/articles/pcgbook_dungeons.php),
[Hybrid approach to roguelike level generation (ANU)](https://openresearch-repository.anu.edu.au/items/abb3546d-81e0-4d12-aefa-714b1c29cff6),
[Cellular automata + Poisson disk room generation](https://scholar.its.ac.id/en/publications/dungeons-room-generation-using-cellular-automata-and-poisson-disk/).

## Boss telegraphs

- Readability (telegraph before, expectation after) is the biggest driver of frustration. Telegraph with
  large gestures, color coding and consistent cues (the same cue always means the same attack); draw
  danger areas directly on the ground when needed. Escalate at phase changes, but never by making
  telegraphs less readable; shortening counterattack windows is the fairer lever.

**Applied:** red ground markers (circle for Slam, lane for Charge) that fill up until impact; the boss
flashes during wind-up; enrage at 50% HP speeds up the cadence (6 s → 4 s) and adds projectiles/minions,
while telegraph durations stay the same.

Sources: [Designing for difficulty readability in ARPGs](https://www.gamedeveloper.com/game-platforms/designing-for-difficulty-readability-in-arpgs),
[Enemy attacks and telegraphing](https://gamedeveloper.com/design/enemy-attacks-and-telegraphing),
[Crafting legendary boss battles](https://www.wayline.io/blog/crafting-legendary-boss-battles),
[Sight-reading RuneScape boss fights](https://informer.rsbandb.com/?p=11837).

## Why crew strategy works (party composition)

- A good party system makes each member distinct and valuable, creates interesting decisions about
  composition, and rewards using the party's combined strengths. Roguelike synergies are best when
  discovered through play and recorded (a codex). Randomized offers make the same class play
  differently across runs. Cost to watch: a party multiplies management overhead, so keep each
  member's management light.
- Sid Meier's principle (from memory, not verified here): a good game is a series of interesting
  decisions; a decision is interesting when options have legible trade-offs.

**Applied:** every species gets a job beyond combat through **Element Gates** (fire burns brambles,
earth smashes boulders, storm powers spark-locks…) that seal optional treasure rooms; recruiting and
releasing become route planning. Synergies are listed in the pack screen; weaknesses go into the codex.
Per-creature management stays light (one gear slot, auto-feed on by default).

Sources: [How to design an RPG party system](https://bugnet.io/blog/how-to-design-an-rpg-party-system),
[Mewgenics review](https://www.theskylineview.com/arts-entertainment/reviews/2026/03/22/mewgenics-is-dangerously-addictive/),
[Rogue Lords review](https://www.softpedia.com/reviews/games/pc/rogue-lords-review-536841.shtml),
[Quarter to Three roguelike thread](https://forum.quartertothree.com/t/the-thread-for-traditional-roguelikes/50736?page=93).

## Why game feel works

- Steve Swink defines game feel as real-time control of virtual objects in a simulated space, with
  interactions emphasized by polish. "Juice" gives generous feedback so actions feel significant and
  results are unambiguous. Hit-stop (a ~50–100 ms freeze on heavy hits) sells force; screen shake sells
  impact but big shake is uncomfortable. Responsiveness comes first: effects can't fix laggy controls.

**Applied:** responsive Quake movement first (done); then hit-stop on crits and heavy hits, light camera
shake when the player is hit, floating damage numbers (crit/weak colored), synthesized sound effects.

Sources: [Game feel (Wikipedia)](https://Www.wikipedia.org/wiki/Game_feel),
[Impact feel study (UW)](https://faculty.washington.edu/zkwen/articles/lin22features.pdf),
[Game Feel & Juice course](https://www.wayline.io/learn/game-feel/1),
[When juice becomes a crutch](https://www.wayline.io/blog/the-seductive-squeeze-when-juice-in-game-development-becomes-a-crutch).

## Why level design works (roguelike rooms)

- Pre-designed room roles connected procedurally (combat, reward, event, rest, boss); clearing a room is
  the reward trigger; difficulty from scarcity and randomness rather than scripted escalation; avoid
  unfair generation (dead-end starts, impossible encounters); optional risk for optional reward.

**Applied:** safe entrance, room roles (prison, vault, larder, shrine, camp, trap hall, watchtower, lair),
gated optional treasure rooms, champions and floor modifiers for scarcity and variety.

Sources: [Roguelike (game design) wiki](https://bloomwiki.org/index.php/Roguelike_(Game_Design)),
[Roguelike game designer skill](https://skillsmp.com/creators/hanjo92/roguelike-game-designer-skill/skill),
[Roboquest vs Gunfire Reborn discussion](https://steamcommunity.com/app/692890/discussions/1/3115896179304403534),
[Level design of a roguelike (gamedev.net)](https://gamedev.net/forums/topic/669376-level-design-of-a-34roguelike34-set-in-outer-space/5236004/).

## Navmesh agent radius (why units snag on corners)

- A navmesh only describes where an agent's *center* may go; agent radius is ignored at runtime, so the
  mesh must be baked eroded by at least the collision radius plus a margin for physics sliding and the
  path's desired distance. The radius rounds up to a multiple of `cell_size`. Too small a cell size
  explodes the voxel count.
- **Found here:** baked at 0.25 while the player capsule is 0.3. Paths hugged walls closer than the body
  fits, so the bot pinned itself on box corners (hundreds of "stuck" events per run on most seeds).
- **Dialectic:** thesis, keep 0.25 so the mesh reaches every nook. Antithesis, a 0.3 body can't follow
  those paths (measured). Synthesis: 0.5 (0.3 + 0.2 margin, a cell multiple). Corridors are 2 tiles, so a
  1 m lane remains; nooks nobody fits through drop out. Result: stuck 200+ → 1–26 per 2 runs, floors
  reached in 1000 s rose from ~3 to ~6.5, bake time unchanged.
- Also fixed: an opened element gate stayed in the rebake because `queue_free` runs after the deferred
  bake, which left the treasure room off the navmesh. Its collision layer is now cleared first.

Sources: [Godot docs: using navigation meshes](https://docs.godotengine.org/en/4.2/tutorials/navigation/navigation_using_navigationmeshes.html),
[Godot NavigationMesh class](https://docs.godotengine.org/en/4.2/classes/class_navigationmesh.html),
[Forum: collider gets stuck on corners](https://forum.godotengine.org/t/collider-from-navagents-parent-gets-stuck-on-corners/83831).

## Companions out of the player's view

- Naughty Dog's buddy-AI rule for Ellie: the companion must never break the player's relationship with
  them (e.g. by giving the player away); being unobtrusive beats being "smart". Player reports on other
  games: good companions fight from the sides, not in front of the player's target; bad ones crowd the
  player's spot.
- **Found here:** a screenshot showed a creature parked about 1.4 m in front of the camera, covering a
  third of the view. Roam points avoided the camera front only when picked; follow slots were fixed
  *world* angles, so walking toward a slot put that creature in front.
- **Dialectic:** thesis, random roaming makes the pack feel alive. Antithesis: at near player height, a pet
  in front blocks a first-person game. Synthesis: keep roaming, add a give-way rule (out of combat, within
  3.5 m and ±35° of the view, step out to the nearer side), and make follow slots player-relative over
  the back and sides (±100° from behind). Measured with a scripted turn/walk/idle test on 3 seeds:
  samples with a pet in view fell from 8.8–12.8% to 6.2–7.3%. Most of what remains is the first 0.17 s
  after a sharp turn; idle is about 3%. The combat frontline still stands in front, by design.

Sources: [GDC: Ellie, Buddy AI in The Last of Us](https://gdcvault.com/play/1020364/Ellie-Buddy-AI-in-The),
[Game Developer: Ellie's buddy AI](https://gamedeveloper.com/design/video-ellie-s-buddy-ai-in-i-the-last-of-us-i-),
[Thinking about Elizabeth](https://www.gamedeveloper.com/design/thinking-about-elizabeth-part-2),
[Companion crowding bug report](https://bitbucket.org/anomalymod/anomaly-bugs/issues/439/love-starved-companions).

**Update (user direction): the pack stays in front.** The user rejected the back-and-sides layout:
pets behind the view feel absent, and roaming within ~3 m looked unnatural. The give-way rule and the
rear follow slots are dropped. Out of combat the pack now stays within ±60° of the view; follow slots
sit 2.6 tiles ahead on alternating sides of the crosshair (never on it, so aiming stays clear), and
idle roaming goes 2.5–7 tiles out in front. Antithesis kept in mind: a pet near the camera blocks the
view, which is why slots avoid the crosshair and roaming starts at 2.5 tiles. The combat line (ranged
and healers behind the player) is unchanged.
Second update (user direction): turning the camera must not move the pack. It now follows only after
the player has kept moving away from it for 2 s, then runs to its front slot until the player stops;
idle roaming is around the player on any side (2.5–7 tiles), no longer tied to the view.

## Charged throw

Practitioner posts on charge inputs: a tap and a hold must be told apart cleanly; show the charge
from its first frame (feedback that starts late feels broken); give a visible minimum power; players
often hold too long, so full charge should hold steady rather than punish.
- Thesis: hold LMB to charge, release to throw; power 20% (tap = short toss) to 100% over 0.8 s.
- Antithesis: a charge delays every throw, and without an arc preview players can't aim the power.
- Synthesis: the throw still fires on release with no minimum hold. As charge feedback from the first
  frame, the held creature is drawn back toward the player (up to 0.3), in the world. Full charge
  holds without decay. A landing-arc preview is left out for now (more work, unclear payoff).
Sources: [Kalia and the charged attack (input design)](https://gdn001.itch.io/kalia-and-the-fire-staff/devlog/525674/kalia-and-the-charged-attack-and-why-input-design-is-important),
[Deadlock forum: hold to throw](https://forums.playdeadlock.com/threads/let-us-throw-the-urn-like-a-football-playable-demo-included.106739/post-202786),
[GameDev SE: charge attacks](https://backiee.wasmer.app/https_gamedev_stackexchange_com/a/3169).

**Held creatures still fight (user direction).** Thesis: a held creature attacks enemies in its own
reach without moving, so carrying is positioning, not benching. Antithesis: if it also couldn't be
hurt, carrying the best ranged pet would be a safe turret every fight. Synthesis: it can be hit while
held (it's in front of the player, so it shields them), and the sword stays put away.

## Why evolution is satisfying (for a future evolution redesign)

- The best-loved systems make the result depend on *how you raised the creature* (Digimon's care-driven
  branches) or on a *choice at the moment* (Cassette Beasts asks at 5 stars, e.g. "Honor or Victory", and
  each answer gives a different evolution). Hidden branches with in-world clues add discovery. Fixed,
  automatic evolution (ours now: stat multiplier, size and name at Lv 6/12) gives none of that.
- Art cost decides scope: Cassette Beasts built every monster twice (once modular) so fusion could mix
  parts. Each extra branch here means another Meshy model per species.
- Not yet applied: needs the user's direction (sketch in the session report).

Sources: [Wireframe: Cassette Beasts](https://wireframe.raspberrypi.com/articles/creature-collecting-gets-an-analogue-upgrade-in-cassette-beasts),
[GameLuster review](https://gameluster.com/cassette-beasts-review/),
[RPG Site: fusion trailer](https://www.rpgsite.net/news/12902-monster-taming-rpg-cassette-beasts-shows-combinations-in-new-fusion-trailer),
[TouchArcade: Creature Chaos thread](https://toucharcade.com/community/threads/creature-chaos-pokemon-digimon-inspired-game.199073/).

## Leveling by eating instead of by fighting (proposal, not applied)

- Raising sims tie growth to feeding: Monster Rancher's early games raise stats through food (better
  when the monster is hungry); Digimon World's feeding, weight and care mistakes decide which forms are
  reachable; Pikmin's nectar matures a Pikmin to a flower (stronger), and in Pikmin Bloom the nectar's
  color sets the flower type.
- Combat XP rewards fighting every time, which turns play into fighting and grinding. Spending a resource to
  grow ties growth to choices and risk. Having all progression hinge on a single resource is clearer than
  two currencies, but it feels exploitable or like a chore if it's the only route (forum views, not
  developer postmortems).
- **Thesis:** food becomes both survival and growth, so every bite is a choice (keep a reserve for hunger
  and revives, or grow someone now) and the player decides who grows.
- **Antithesis:** fights would give nothing directly, so players may skip them; feeding the strongest
  snowballs; auto-feed would blur the choice; food is already tight (20–60 held with a full pack).
- **Synthesis (proposed):** fights still pay in food (drops); growth comes from *extra* feeding beyond
  hunger, a manual choice; what a creature eats steers its evolution form.

Sources: [Monster Rancher beginner's guide](https://www.legendcup.com/MRM/discus/messages/13920/14701cf12.php),
[Pikmin wiki: Nectar](https://www.pikminwiki.com/Nectar),
[V-Pet evolution chart](https://lcd.withthewill.net/VpetEvo4),
[Roguelike design: should I remove leveling?](https://rpgmaker.net/forums/topics/23474),
[XP for Gold](https://kateplays.substack.com/p/xp-for-gold).

## Holding a creature, a longer sword swing, and combat sounds

**Carrying = a viewmodel.** First-person games keep a held item fixed relative to the camera by
recomputing its transform from the camera every frame (or parenting it to the camera).
Found by running the game: the creature turned in the player's hands because the shared **Idle clip
swings the Hips ±40° of yaw** (Hips yaw −81°…+3° over 4 s), and it only followed yaw, not pitch.
- Thesis: lock the creature to the camera (yaw + pitch) and play a "carry" clip = idle with the
  trunk bones (Hips, Spine*, neck, Head) pinned to rest; arms and legs still idle so it looks alive.
- Antithesis: a stiff, camera-locked body reads as a sticker; and a world-space body still sinks
  into walls (true viewmodels draw on top with a second camera or no depth test).
- Synthesis: keep the limbs animated so it isn't a sticker. Near a wall, pull it toward the eye and
  scale it by the same factor, so it keeps the same size and spot on screen. No second camera or
  material override (high risk vs the expression-texture work, low reward). The sword drops out
  of view while carrying (0.18 s) and comes back after.

**Carrying, rebuilt: a world object, not a viewmodel** (replaces the above at the user's request:
the viewmodel read as a 2D sticker that turned with the camera). Physics-carry games (Half-Life 2's
gravity gun, Amnesia, Portal) hold the object at a target point in front of the player in world
space, keep it upright, and turn it only by the change in the player's yaw. Held objects that
ignore collision sink into walls; the usual fix is to pull the hold point in with a ray.
- Thesis: full size, world space, upright, yaw-only, centered, fixed height (pitch ignored);
  pulled in near walls without scaling; eases into the hands on pickup.
- Antithesis: a full-size creature can fill the view, and with no scaling trick something must
  give at a wall (it sinks into the wall or into the camera).
- Synthesis: its top sits 0.3 below the eye, so it blocks only the lower part of the view. At a
  wall it stops at 0.45 + radius, so its back pokes into the wall rather than filling the camera.
  The pickup ease is relative to the player, so it never trails behind at bunny-hop speed. Set
  down and thrown from the held spot (it is already clear of walls).
Sources: [Godot forum: HL2/Amnesia-style manipulation](https://forum.godotengine.org/t/hl2-amnesia-style-physics-object-manipulation/133886),
[Portal-style grabbing (upright)](https://community.gamedev.tv/t/portal-style-grabbing-rotate-with-you-and-make-upright/39075),
[Unity: held object through walls](https://discussions.unity.com/t/how-to-make-an-object-your-carrying-with-your-gravity-gun-not-pass-through-a-wall/121108),
[Godot forum: pick up & carry](https://forum.godotengine.org/t/how-to-pick-up-carry-an-object-with-a-player-character/11812).

**Swing reach.** Practitioner advice: respond to the attack press within a frame or two and spend
the animation on follow-through, not wind-up (too much anticipation feels like input lag, too
much recovery feels sticky); a swing that stops dead looks weightless, while overshoot-and-settle
reads as weight; animators stretch the weapon/arm slightly at full extension to sell reach;
players judge a hit by where the weapon visibly goes, so the hitbox must match the animation.
- Thesis: reach 1.5 → 2.0 (+33%) for the sword, with a matching forward thrust in the viewmodel.
- Antithesis: more reach lets the player hit from outside enemy melee range (~1.0), which trivializes
  dodging and can unbalance the bot; very long reach in first person feels like the hit came from
  nowhere if the blade visibly stops short.
- Synthesis: 2.0 tiles keeps the sword inside "one step" range. Every swinging weapon gets +0.5,
  the dagger +0.35 and the spear +0.3, so the order of weapon reach stays the same. The arcs are
  unchanged. The hit lands on the press (no wind-up). The blade crosses in 22% of the cooldown with
  an ease-out, overshoots 12%, then settles. It thrusts forward by an amount set by the weapon's
  reach and stretches 25% at full extension. Checked with a 4-seed bot run before and after.

**Combat sounds.** Common advice for frequent sounds: vary pitch (about ±10%) and volume on every
play and round-robin through variations; limit voices per sound category (for example, 4–8) and
steal the oldest when all are busy; then accept some loss of density.
- Thesis: a positional (3D) voice pool, at most 3 copies of one sound at once, a 30 ms gap that
  merges hits from the same tick, ±8% pitch and ±1.5 dB per play, and a far-distance low-pass.
- Antithesis: strict limits make big fights sound thin, and with synthesized sounds the variation
  is only per-play, not per-sample (no round-robin set).
- Synthesis: the player's own sword hits stay 2D and are never culled (they are feedback for the
  player's own input). Pack and enemy sounds go through the limited 3D pool. **Ally vs enemy** is
  told apart by timbre and pitch direction: a hit on an enemy is a low thud plus a falling noise
  crunch (good news); a hit on the pack is a higher yelp that falls in pitch (bad news). Attack
  starts are short and quiet ("atk_ally" whoosh, "atk_enemy" low growl-swish, "shoot" for ranged)
  so they set up the hit without covering it. All sounds are synthesized in `Feel`, so there are
  no assets and no licenses.

Sources: [Bevy first-person view model](https://bevyengine.org/examples/camera/first-person-view-model),
[Viewmodel per-frame transform (CSE 125)](https://cse125.ucsd.edu/2026/cse125g2/docs/structWeaponViewmodel.html),
[Sword/melee animation guide](https://mocaponline.com/blogs/mocap-news/sword-melee-animation-guide),
[Animation basics: follow-through](https://bugnet.io/blog/animation-basics-that-make-your-game-feel-alive),
[Polycount: elongate at max extent](https://polycount.com/discussion/comment/2670243),
[Aztez: anatomy of an attack](https://aztez.com/?p=8443),
[Roblox: hit where the animation went](https://devforum.roblox.com/t/melee-combat-hit-registration/1762164),
[Why is my game audio repetitive (IRPR)](https://sounddesign.irpr.agency/guides/why-is-my-game-audio-repetitive/),
[Per-category voice pools (Unity TD audio README)](https://git.marlboro-bc.duckdns.org/yeahweregames/UnityTowerDefense/src/branch/main/Assets/_Project/Scripts/Audio),
[Automatic weapons audio design](https://game-audio.notion.site/Automatic-Weapons-in-Games-Audio-Systems-Design-2dfb117030d2802192a3c343fc995f2f).

## Evolution paths: two branches or a tree (Bloons-style)? (proposal)

- Bloons TD 6: 3 upgrade paths × 5 tiers per tower; only 2 paths per tower, and only one may pass tier 2
  (crosspathing). Picking the pair that fits the situation is the main skill; some low-tier upgrades
  matter for how they combine with the other path. Its upgrades are mostly numbers and abilities on
  cheap 2D art.
- Digimon uses wide branching trees; Temtem branches only some species, by a condition.
- User decision (2026-10-30): kills give a little growth, food is the main source; XP is renamed Growth.
- **Thesis:** a tree gives the most build expression. **Antithesis:** here every visual form is a Meshy
  model (12 species × 3 stages = 36 now); a 2→4 tree adds about 48 models, 2 branches add about 24.
- **Synthesis (proposed):** split *form* (expensive art: 2 branches at stage 2, each with its own stage 3)
  from *perks* (free: a Bloons-like pick at milestone levels, no new art).

Sources: [Bloons wiki: Crosspathing](https://bloons.fandom.com/wiki/Crosspathing/Engineer_Monkey),
[bloonswiki: Upgrades](https://www.bloonswiki.com/Upgrades),
[Temtem wiki: Evolution](https://temtem.wiki.gg/wiki/Evolution).

## Which treat picks which path? (proposal)

- Pokémon's Eevee: each elemental stone gives the matching element's form, a rule players learn once.
  Slime Rancher: each slime has a diet group and its own favorite food, shown in its Slimepedia entry,
  so per-species preferences are discoverable without memorizing.
- **Thesis (universal):** treat A always gives path A for every species. It's easy to learn, but every
  species' two paths become the same two archetypes, so species feel alike.
- **Antithesis (per-species):** each species has its own two foods. That's rich, but many food types clutter
  the pouch and players must memorize 24 pairings.
- **Synthesis (hybrid):** 4 treat flavors with one fixed meaning each (Meat = Fang/offense,
  Rock candy = Guard/defense, Spice = Wild/element unleashed, Honey = Kind/support). Each species
  reacts to the 2 flavors that fit it, and the pack screen shows those 2 with a diet bar, so nothing has to be
  remembered. The meaning is learnable, and the pairs differ per species.

Sources: [Bulbapedia: Pokémon Evolution](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Evolution),
[Slime Rancher wiki: Food](https://slimerancher.fandom.com/wiki/Food),
[Prima: Slime Rancher 2 favorite foods](https://primagames.com/tips/slime-rancher-2-all-slime-types-and-their-favorite-foods).

## Hard diet restriction vs soft preference

- Hard restriction is proven but costly. In Don't Starve Together, Wigfrid eats only meat. Players treat it as a
  real weakness that deters some of them; Wurt's vegetarian diet is mild because she gets more from veg.
  In Slime Rancher, slimes eat only their diet group (a logistics layer that is praised but called
  monotonous over time), and the favorite food doubles output (a soft bonus).
- Both games give restrictions to characters you *choose* (DST) or to a farm with no death pressure
  (Slime Rancher). Here food is also survival, so a hard restriction turns bad drops into starvation.
- **Synthesis:** every creature eats every food for hunger; each species has 2 favorite flavors that
  give extra Growth and push its form (soft preference, like Slime Rancher favorites).

Sources: [Klei forums: Wurt and leafy meat](https://kleiforums.com/forums/topic/139388-suggestion-let-wurt-eat-leafy-meat-too/),
[DST character perks](https://blog.berrybyte.net/dont-starve-together-characters-perks-playstyles/),
[Slime Rancher wiki: Food](https://slimerancher.fandom.com/wiki/Food),
[Everyeye review](https://www.everyeye.it/articoli/recensione-slime-rancher-34757.html),
[Nintendo Life review](https://www.nintendolife.com/games/switch-eshop/slime_rancher_plortable_edition/review).

## Bloomling species specifics under the v17 SD style (2026-10-30)

- Shape language: round shapes read friendly/approachable; pick one dominant shape and build around it;
  a strong silhouette reads at thumbnail size; a secondary shape accent shifts the read
  ([cg-wire](https://blog.cg-wire.com/character-shape-language/),
  [rocketbrush](https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent),
  [3dsense](https://3dsense.net/blogs/shape-language-in-character-design-communicating-through-geometry)).
- Applied to Bloomling (healer): dominant shape round (head, bust, thighs, puffball tail); the accent is
  asymmetry (one flopped ear, one-sided flower) so her outline differs from the other tall-eared species.
- Thesis: keep the all-pink palette, it is her identity. Antithesis: with flat plain eyes, pink-on-pink
  eyes lose contrast and the face reads blank at game distance. Synthesis: keep pink fur and hair, give the
  eyes a contrasting color (leaf green) so the one flat iris still pops.
- Thesis: crop top is simplest for 3D. Antithesis: the variety rule bans the shared crop top; every species
  in a crop top reads alike. Synthesis: a species-specific outfit that also tells the role (herb satchel =
  healer) and changes the outline.

## v18 style test: painterly chibi reference + enamel-pin palette (2026-10-31)

User references: (1) a soft painterly chibi illustration (style, brush, proportions), (2) a sheet of chibi
enamel-pin designs (palette only; fan art of an existing game's cast, so only colors are taken, no characters).
Measured by median-cut quantization (24 colors, white dropped):
- Ref 2 palette: warm creams for skin and light areas (#e7ddce, #f0dec6, #e0ceba), gold-bronze lines
  (#caa076, #be8c65, #b9734f), dusty accents (brick red #b63d42, navy #2e435a, dusk indigo #302c4a,
  sage #93b29a, pale mint #c7d7cb), warm grey #686771. Nearly every fill has saturation under 0.5; the
  most saturated (brick red) is 0.66 and used small.
- Ref 1 palette: warm browns and creams (#594030, #775c45, #e0cfbb, #f1eade), shadows tinted warm.
- Thesis: copy the reference rendering (soft paint, thin brown varied lines, muted palette).
  Antithesis: our flat cel style was chosen because it bakes into a Meshy texture cleanly; soft painting
  and fine line weight blur at texture resolution and Godot lighting double-shades painted shadows.
  Synthesis: test it once (9 credits) and judge in 3D before rolling it to the roster.

### Reference 3: coloring breakdown (pastel bunny chibi, user's liked coloring)
Measured (median-cut, 28 colors) and checked on 3x zoom crops:
- One hue family: nearly every color, including the "blacks" (#342526) and greys (#6a5c5d), sits at hue
  355-19 (rose). Even neutrals are rose-tinted, which ties the whole image together.
- White-pink base (#f2e6e6, #fbe6e3) with rose shadows (#e4a8a7, #cf9e9d): shadows shift hue/saturation
  instead of just darkening, so white hair never reads grey.
- Shadows are cel shapes with soft airbrushed edges where they meet the light (hybrid cel + soft).
- Cool bounce light: lavender-blue gradient at the lower edges of the tail and hair.
- Complementary accent: tiny saturated cyan/turquoise spots in hair partings and crevices, the only cool
  saturated color. Pink + cyan pairing is a known anime hair trick
  ([Clip Studio hair guide](https://www.clipstudio.net/how-to-draw/archives/161517),
  [hair tutorial](https://art.cleberg.net/post/kyoukaraa/HAIR-Tutorial-669505294)).
- Colored lineart: thin dark-rose/red-brown lines (#b46769, #603537), never black; a thin white inner
  line runs inside some outlines.
- Finishing: glitter/sparkle dots, small heart and drop shapes as decoration, a white sticker border,
  soft glow. Highlights painted over color, not left white
  ([AnimeOutline](https://www.animeoutline.com/?p=3457)); shadow pass as a clipped Multiply layer
  ([MediBang](https://medibangpaint.com/en/use/2019/12/create-glossy-hair-with-anime-glossing)).
- Ref 2 vs ref 3 conflict: ref 2 is a multi-hue muted palette, ref 3 a one-hue pastel scheme. Synthesis:
  ref 3 gives the method (hue-tinted neutrals, rose shadows on pale base, cool bounce, one complementary
  glint, colored lines); ref 2 gives each species' muted base colors.
- 3D carry-over (assumed): base/shadow colors, colored lines and cyan spots bake into the texture;
  glitter, glow, sticker border and the lavender bounce depend on view/lighting and will be lost or
  must be rebuilt in the Godot shader (rim light, bloom).

## What a healer should wear (Bloomling, 2026-10-31)

Web results were thin on healer costumes specifically; checked points:
- Red cross: the emblem is protected under the Geneva Conventions; the ICRC has asked developers to remove
  it, and games swapped it for green crosses, hearts, an "H", or redesigned shapes (Prison Architect,
  Skullgirls) ([PCWorld](https://www.pcworld.com/article/1989513/did-you-know-that-this-symbol-is-forbidden-in-video-games.html),
  [esportslegal](https://esportslegal.news/2023/11/11/good-to-know-navigating-the-legalities-of-the-red-cross-symbol-in-video-gaming/),
  [Opinio Juris 2026](https://opiniojuris.org/2026/08/20/from-medkits-to-punk-rock-pop-culture-and-the-non-negotiable-protection-of-the-red-cross-emblem/)).
  Rule: never a red cross; use a heart or leaf-heart emblem.
- Role must read at thumbnail / silhouette size; one or two memorable details beat clutter; rounded
  shapes read caring ([rocketbrush](https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent),
  [3dsense](https://3dsense.net/blogs/shape-language-in-character-design-communicating-through-geometry)).
- A student cleric-healer study used calm green-blue (herbs, renewal) with gold accents
  ([Ulster](https://blogs.ulster.ac.uk/meitingwang/?p=492)).
Assumed (genre knowledge, not sourced here): game healers draw on four archetypes: nurse (cream/white,
cap, apron), cleric (white robe, gold trim, staff), herbalist/druid (apron, pouches, herbs) and shrine
maiden (white and red). Common signals: a light dominant color, soft rounded shapes, a life symbol, a tool.
- Thesis: nurse look (cap + apron), reads "healer" instantly. Antithesis: a nurse is a human-world uniform
  and clashes with a flower-rabbit monster; herbalist alone (satchel) did not read as healer in v18c.
  Synthesis: herbalist-nurse hybrid: a nurse-style cap with a leaf-heart emblem (the one strong signal)
  and an apron whose pocket holds herbs, in the creature's own palette.

### Palette consistency (v18c lost it)
v18c mixed large deep forest green, vivid red and brown with the rose family, so it no longer read as one
scheme. Ref 3's rule: every color, darks included, sits in one hue family, plus one complementary accent
used small. Bloomling: rose family (pale blush base, dusty rose shadows, wine-red darks and lines),
cream as the light neutral, mint as the only complement (eyes, hair glints, herb sprigs, emblem).

### Nun vs nurse-herbalist vs moon-rabbit apothecary (Bloomling outfit, 2026-10-31)
- Moon rabbit folklore: in Chinese tradition the rabbit pounds the elixir of life (or medicine for
  mortals) with a mortar and pestle; a Han-dynasty poem has the white rabbit "pound medicine"; Japan and
  Korea swap in rice cake ([Wikipedia: Moon rabbit](https://en.wikipedia.org/wiki/Moon_rabbit),
  [JAXA](https://www.isas.jaxa.jp/home/research-portal/en/gateway/2022/0203)). So "rabbit = medicine
  maker" is an existing, old association.
- Thesis (user): nun / cleric. Strong fantasy-RPG healer read; the veil is a big distinct silhouette.
  Antithesis: a veil covers the hair we just fought to get; real religious garb invites real symbols
  (crosses) and, paired with the body dials and no bottom, the sexualized-nun trope, which some players
  find offensive; a black habit breaks the pale rose palette. Nothing ties a nun to a rabbit.
- Counter-thesis: moon-rabbit apothecary. The healer link is native to rabbits, a mortar-and-pestle prop
  says "makes medicine" in one shape, and it stays secular.
- Synthesis (proposed): keep a cleric-like soft cream hooded capelet for the holy-healer silhouette
  (ears through slits, hair and bangs visible), add the moon-rabbit cues: a crescent-moon emblem and a
  small mortar and pestle on the apron/hip. No cross.

### Minimal healer silhouette + toy look (Bloomling v18f, 2026-10-31)
- Silhouette carries role; a key feature can vanish in black fill; fix the robe outline as one shape first
  ([Catalyst devlog](https://just-write-studios.itch.io/catalyst-blind-faith/devlog/791509/devlog-character-design-silhouettes-shape-language-and-weird-fashion)).
  A healer's staff was swapped for glowing gauntlets for clarity ([ModDB: Cherub](https://www.moddb.com/news/conceptualizing-a-healer-cherub-design-process)).
  Common healer pattern: light robe + hood + glowing focal point ([itch priestess](https://pompack.itch.io/priestess-healer-sprite)).
- v18e read cluttered: capelet, top, apron, pocket, herbs, mortar, flower cluster = seven small parts and
  no single healer shape. Thesis: one big shape, a hooded A-line robe-dress (bell outline + hood with ears
  through it). Antithesis: a long robe hides the thick legs (body dials) and the hood hides the hair.
  Synthesis: short A-line robe-dress to mid-thigh (bell outline, thighs visible), hood up with the ears
  through slits and the bob and bangs framing the face; one focal point (glowing crescent emblem); no
  staff (a held prop merges with the hand in Meshy and fights the pick-up/throw poses).
- Toy look: the shared "big round paws" makes mitten blobs; cylinder legs + round belly + soft shading
  read as a plush. Fix: small paw-hands with short rounded fingers, thighs that taper to slim ankles and
  slim rabbit feet, and "anime character illustration, not a plush toy, not a mascot".

## Clothing design: personality, shape and form (Bloomling outfit, 2026-10-31)

Sources: [Proko drapery lessons](https://www.proko.com/lesson/batman-drapery-studies),
[Clip Studio: Notes on Character Outfit Design](https://tips.clip-studio.com/es-es/articles/9640?org=1),
[Clip Studio: Designing Clothes for Characters](https://tips.clip-studio.com/en-us/articles/4487),
[concept artist methodology](https://civarchive.com/articles/33926/how-to-design-character-appearance-methodologies-from-a-professional-concept-artist),
[21-draw: unique fantasy character](https://www.21-draw.com/tr/designing-a-unique-fantasy-character/),
[GCSE costume design: colour, shape, fit](https://www.pastpaperhero.com/resources/aqa-gcse-drama-8261-costume-design-skills-colour-shape-fit-and-period-detail),
[Catalyst devlog](https://just-write-studios.itch.io/catalyst-blind-faith/devlog/791509/devlog-character-design-silhouettes-shape-language-and-weird-fashion),
[SoraNews24: anime high-waist skirts](https://soranews24.com/2016/11/25/japans-anime-waist-skirts-have-become-a-line-of-femininely-fashionable-one-piece-dresses/amp/).
- Costume tells story (role, origin, personality) without words; shape and fit define occupation and style.
- Shape rhythm: one dominant shape (~60%), a secondary (~30%), a small accent (~10%); mix big, medium and
  small so it is not monotonous.
- One focal point: lead the eye with fabric lines, belts or accessories; put the strongest value/color
  contrast there; simplify the rest.
- Perfect symmetry reads generic; managed asymmetry makes a design feel alive.
- Feminine read: a defined waist (cinch, corset, high waist), a flared or layered skirt, softened shoulders
  and sleeves (puff, bell), frills and bows used sparingly.
Diagnosis of v18/bloomling_s6.png: the robe is ~100% one shape (no secondary/accent rhythm), symmetric,
no waist definition, straight hem, and nothing in it tells her story (flower, rabbit, moon healer), so it
reads as a generic hoodie. Thesis: keep minimal. Antithesis: minimal is not the same as blank; personality
needs rhythm, a focal point and story. Synthesis: few parts, but each with a job: dominant skirt shape that
tells "flower", a cinched waist (feminine), healer sleeves, one asymmetric piece, one glowing focal point.

## Why the Bloomling generations keep dropping features (2026-10-31)

Checked (our own runs, art/concepts/v18/*.prompt.md):
- s1: long style text first -> ears, flower, lashes, bust lost. s2: character first -> most kept, style drifted.
  s3: style first again -> bust lost. s4: "fluffy fur tufts at the cheeks" -> hair lost (animal head won).
  s7: head-size + long outfit text, ears line after the body -> ears lost, hands became flippers.
- Each try changed several things at once and used one random sample, so no single cause is proven.
Sources:
- Google's Nano Banana guide: describe narratively, not as a keyword list; use positive framing
  ("empty street", not "no cars"); be specific; use reference images for character consistency
  (up to 14); iterate conversationally
  ([Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)).
- Research on text-to-image models: attributes bind to the wrong object and objects get omitted, more so
  with many attributes and ambiguous references ([scene-graph hallucination eval](https://arxiv.org/pdf/2412.05722),
  [Magnet, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/688ffe062732aabd87dfe57bcb0bf3ae-Abstract.html),
  [EBAMA](https://par.nsf.gov//servlets/purl/10561829), [CoBind](https://arxiv.org/abs/2607.16307)).
Diagnosis (assumed, consistent with both): (1) ~600 words and ~40 attributes per prompt: past a point
the model drops some; (2) conflicting cues (SD toddler body vs big bust; "rabbit" + "anime girl face";
"flower" + petal-tipped ears read as hair ornaments) get resolved toward the model's prior (a plain chibi
girl); (3) many "no X / not Y" phrases name the unwanted thing; (4) keyword-list structure, not a narrative.
Fix: identity features in the first sentence, narrative paragraphs, positive framing only, cut
redundant words, keep the style text that made the texture. Change fewer things per try.

### v19 style regression vs v18 s6/s7 (2026-10-31)
Measured (median saturation of non-white pixels): s6 0.16, s7 0.17, v19 0.13; side-by-side face crops:
s6/s7 are warm (peachy rose hair, warm rose shading on the face, heavy warm blush, soft edges); v19 is
cool and whiter (near-white hair with cyan sheen, flatter face, crisper sticker-like lash shapes).
Cause (assumed): v19 pushed "pale, almost white" for hair and base plus cyan glints; s6/s7 had drifted
warmer than asked and that drift is what the user liked. Fix: warm peachy rose hair, warm rose shading
and blush named explicitly, cyan glints kept tiny.

## Evolution paths, slice 1: diet decides the branch (built)

- Monster Rancher 3 shows nutrition as a 4-block gauge that says *something* is lacking but not
  *which* attribute; players work it out through community testing. Monster Rancher 2's sub-breed
  evolution needs a breed-specific food fed 2–6 times before a growth spurt, with a random element.
  Digimon World players ask what happens when several branches qualify; community answers point to
  stat or priority order, with no clear rule shown in-game.
- **Thesis:** a hidden diet makes evolution a discovery, like Digimon's care branches.
- **Antithesis:** hidden branch rules are what these games' players complain about: they need wikis to
  get the form they want, and a long-term choice they can't steer feels random.
- **Synthesis:** the pack screen shows the 2 favorite flavors, the count eaten, what each path
  becomes, and the current leaning, so every treat is a visible step toward a chosen form. A tie
  (or an unfed creature) is decided at random at Lv 6 and the screen says so. Discovery stays in
  *what* each form does in play (path abilities, slice 2), not in hidden rules.
- Risk: low (data and stats only, same models). Reward: high (treats become a steering choice).

Sources: [LegendCup: Monster Rancher 3 items](https://www.legendcup.com/faqmr3items.php),
[LegendCup: promoting and preventing evolution](https://www.legendcup.com/MRM/discus/messages/3503/5767694c.php),
[Steam: Digimon World Next Order, multiple paths met](https://steamcommunity.com/app/1530160/discussions/0/3829789648150562995).

## Does T-pose + front view hurt the style? (2026-10-31)
User suspicion: T-pose + front-facing wording contaminates the style. Checked:
- Our runs: every v18/v19 image used pose_mode t-pose, so pose is not isolated yet. Adding "faces straight
  forward, front-on" (s12, s13) gave a smaller head and stiffer, less cute figure than s8 (one sample each).
- T-pose is a rigging calibration stance, chosen for skeleton detection, not appeal
  ([Meshy Pose Control](https://www.meshy.ai/features/custom-pose)). Meshy notes a custom art style cannot be
  applied in the same generation as a pose, a hint that pose and style compete.
- Meshy image-to-3D has pose_mode a-pose / t-pose / none; its guide says to set T/A-pose for rigging
  ([Meshy image-to-3D guide](https://docs.meshy.ai/en/webapp/image-to-3d),
  [API](https://docs.meshy.ai/api/image-to-3d.md)); a third-party playground says with a-pose/t-pose
  "the model is forced into a standard pose" ([muapi](https://muapi.ai/playground/meshy-6-image-to-3d)).
Hypothesis (assumed): T-pose / front-view are "reference sheet" cues that pull the image model toward stiff
asset art. Thesis: draw the concept in a natural cute pose and let image-to-3D force the T-pose.
Antithesis: re-posing is unverified on our chibi; arms crossing the body may fuse to the torso in 3D.
Synthesis: test in 2D first (natural pose, arms slightly away from the body so they stay separable), then
one 3D test with pose_mode t-pose only on the user's OK.
Result (checked, 2026-10-31): image-to-3D (meshy-t2.5, pose_mode t-pose) from the natural-pose concept
v19/bloomling_s14.png re-posed her into a T-pose with arms straight out (`assets/models/tests/bloomling_v19_natural.glb`,
task 01a18d9b-547d-776e-81fb-04d238e7cdb0). Face, lashes, heart cheeks, outfit survived. So concepts can be drawn
in a natural pose; the T-pose is applied at the 3D step. Note: without pose_mode the image comes out 1:1 with a
small figure; pass aspect_ratio 3:4 and "she fills most of the frame".

## In-world feeding and item choice without menus (proposal)

- Diegetic UI (Fagerholt & Lorentzon's taxonomy): info and actions that exist in the game world —
  Dead Space's inventory and health, Fallout's Pip-Boy, Alone in the Dark's jacket pockets. Caution
  from the same sources: going fully diegetic limits how much information you can show.
- Slime Rancher: the Vacpack is the one tool for everything; you pick a slot (bumpers / keys) and
  shoot the food at a slime to feed it, and preferred food matters. Feeding is aiming and firing,
  not a menu.
- Hotbar vs radial: a hotbar is fastest for a few fixed slots used often; a hold-to-open radial
  suits immersion-first games with a clean screen. Common hybrid: hotbar for the frequent few.
- **Thesis:** everything in-world: select an item, aim at a creature, it flies there.
- **Antithesis:** rare, info-heavy tasks (release, rename, reading traits) get worse without a
  screen; and swapping the sword out for food mid-fight is clunky.
- **Synthesis (proposed):** frequent actions in-world (feed, treat, gift), info as a world-space tag
  over the creature you look at; rare management stays on the pack screen. The selected item sits in
  the off hand, so the sword never leaves; LMB on a pack creature throws it, LMB elsewhere swings.

Sources: [Wayline: diegetic interfaces](https://www.wayline.io/blog/diegetic-interfaces-game-design),
[Slime Rancher wiki: Vacpack](https://slimerancher.fandom.com/wiki/Vacpack_(Slime_Rancher_2)),
[Slime Rancher controls](https://www.magicgameworld.com/?p=8360),
[Quick-use wheel modes](https://docs.nextgenfivem.com/inventory/features/quick-wheel).

### How other games pick what to throw or use (patterns)

- **Cycle button:** Pikmin swaps the Pikmin type to throw with one button (R on Switch); the HUD
  shows the current type with the neighbours beside it. Halo 3 cycles grenade types with one input.
- **Directional picker:** Halo 4 gives each grenade type its own D-pad direction.
- **Hold-and-pick:** Zelda: Tears of the Kingdom: hold R to ready a throw, hold Up to open an item
  strip, pick with the stick, release; then aim and throw. RDR2 feeds the horse through the item wheel
  (hold, pick horse food). Monster Hunter Wilds: hold a modifier for a radial; players report misinputs.
- **Number keys / hotbar:** Monster Hunter Wilds on PC mirrors its radial as an item bar on the
  number keys; Minecraft, Valheim, Slime Rancher on PC (from memory, not checked) use a numbered
  hotbar plus the wheel.

Sources: [Pikmin wiki: Controls](https://www.pikminwiki.com/Controls),
[Halopedia: Halo 4 control schemes](https://halopedia.org/H4:Control_schemes),
[Halopedia: Halo 3 control schemes](https://halopedia.org/H3:Control_schemes),
[Nintendo Life: TotK throwing items](https://nintendolife.com/guides/zelda-tears-of-the-kingdom-how-to-throw-items-and-best-throwable-items),
[Twinfinite: RDR2 feed your horse](https://twinfinite.net/guides/red-dead-redemption-2-how-to-feed-your-horse/),
[Destructoid: MH Wilds radial menu](https://www.destructoid.com/how-and-why-to-customize-your-radial-menu-in-monster-hunter-wilds/).

### Held-item HUD: icons in boxes, not text (built)

- Pikmin 3/4 show what will be thrown next as the biggest of three icons, with the neighbours in the
  cycle smaller on each side and a count beside each; size makes the hierarchy, icons carry the type,
  color carries status (a design essay on Pikmin 3 calls out this size hierarchy).
- **Thesis:** text ("Holding Meat Chunk ×3, next: …") is exact and cheap.
- **Antithesis:** text has to be read, not glanced at, mid-fight; it sits in the top-left status
  block where the eye doesn't go when throwing.
- **Synthesis:** a framed big box (current) between two small boxes (previous, next), bottom right,
  each with an icon and count, the name under the big box. Icons are drawn in code (silhouette first,
  color second: loaf, drumstick, crystal, chili, honeycomb, flask), so no art cost; they can be
  swapped for painted icons later behind the same `ItemIcons.draw`.

Sources: [Pikmin wiki: HUD](https://pikminwiki.com/HUD),
[Mechanics of Magic: Visual design of Pikmin 3](https://mechanicsofmagic.com/?p=734).

## Key layout, keyboard and Switch (proposal)

- Splatoon 3 (the reference Switch shooter): ZR main weapon, R throw sub weapon (hold to pick the
  landing spot), ZL squid form, B jump, X map/menu, Y reset camera, sticks move and look.
- Metroid Prime Remastered defaults to dual stick (move + look), like modern shooters; gyro aiming
  is optional (also in Doom Eternal on Switch).
- **Thesis (current):** LMB is context-sensitive: it throws the held item at a pack creature under
  the crosshair and swings otherwise.
- **Antithesis:** since the combat line puts the pack in front of the player, a creature crosses
  the crosshair mid-fight and a swing turns into a treat throw. Splatoon keeps the throw on its own
  button for this reason: the main attack never changes meaning.
- **Synthesis (proposed):** throwing the held item gets its own button (RMB / R, Splatoon's sub
  weapon slot); petting moves to holding interact (tap E/A = pick up, hold = pet), since both act on
  the creature you look at. Sic 'em goes on ZL (both triggers are "aim and act").

Sources: [Samurai Gamers: Splatoon 3 controls](https://samurai-gamers.com/splatoon-3/game-controls-50/),
[Game8 (JP): Splatoon 3 controls](https://game8.jp/splatoon3/479910),
[GGRecon: Metroid Prime Remastered controls](https://www.ggrecon.com/guides/metroid-prime-remastered-controls-explained/),
[GamingBolt: Doom Eternal Switch gyro](https://gamingbolt.com/doom-eternal-on-switch-supports-gyroscopic-controls-battlemode-confirmed).

## Sound loudness matching (built)

- Measured raw levels of the 17 synthesized sounds spanned 13 dB (attack swooshes −9.8 dB, chest
  jingle +3.3 dB vs the median), and beeps at 0.6–1.3 kHz sit where the ear is most sensitive while
  thuds at 55–140 Hz sit where it is least, so equal signal level ≠ equal loudness.
- ITU-R BS.1770 (LUFS) measures loudness as the RMS of a K-weighted signal: a high shelf of about
  +4 dB above ~1.7 kHz and a high-pass near 38 Hz. Its published coefficients are for 48 kHz; at
  other rates they must be recomputed (here from the shelf/high-pass parameters with RBJ biquads;
  the parameter values are from memory of libebur128/pyloudnorm, not checked against the PDF).
- Gating and integration in BS.1770 are for programme-length audio; for sub-second effects the
  ear's temporal integration (~200 ms) matters, so energy is averaged over at least 0.2 s.
- **Thesis:** normalize every sound to one loudness. **Antithesis:** the combat design wanted
  attack starts quiet under the hits; flat normalization erases that. **Synthesis:** normalize,
  then apply an explicit mix table (attack starts −8 dB, etc.), so loudness differences are only
  the ones chosen on purpose. After matching, all sounds sit within 1.6 dB (some are peak-limited).

Sources: [ITU-R BS.1770](https://itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-1-200709-S!!PDF-F.pdf),
[cacophony.js: K-weighting stage 1](https://cacophony.js.org/variables/K_WEIGHTING_STAGE1_48K.html),
[Hydrogenaudio: BS.1770 at other sample rates](https://hydrogenaudio.org/index.php?msg=669848),
[JUCE forum: LUFS filter coefficients](https://forum.juce.com/t/iir-filter-coefficients-for-lufs-calculation/59111).

## Strategy review fixes (2026-10-31)

A review found that the strategy systems existed, but few of their choices had any bite. The
problem underneath: a decision is only interesting when its options cost something and the
player can act on what they know. Each fix below gives a choice a cost, or makes a piece of
knowledge usable.

### Active pack + bench (pack cap 8 → 5 active + 3 resting)
- Darkest Dungeon caps a party at 4 out of a larger roster, and its slots carry meaning. Most
  party games field 4–8 at most. Community view: a small field party keeps each member's value high
  enough for the choice to matter. No developer postmortem found.
- **Thesis:** a big swarm is the Pikmin fantasy; keep 8.
- **Antithesis:** with 8 of 12 species fielded by floor 4, the role and element bonuses come free
  and composition stops being a choice. Food, the intended limit, holds at 20–60 even with a full
  pack (bot).
- **Synthesis:** 5 fight and 3 rest on the bench. You swap at a rest spot (the entrance room or a
  campfire), and only there, with the floor's gates, map and modifier in view. Resting creatures
  don't eat over time, gain no XP, and heal fully on each descent. Each costs 1 food per floor
  descended (no food: −10 bond). The bench becomes recovery too: rest the hurt, field the fresh.
- Risk: medium (balance: 5 fighters, not 8, against enemies tuned for 8; untested). Reward: high.

### Weaknesses steer creature targeting
- FF12's gambits let players write "Foe: fire-weak → Fire", so element knowledge becomes AI
  behaviour.
- **Thesis:** let the player assign targets by element. **Antithesis:** per-creature orders in
  real time add the management overhead research already warned about. **Synthesis:** creatures
  prefer foes weak to their element (×0.6 distance score) and avoid ones that resist it (×1.6).
  The player's lever is who is fielded (the bench); Sic 'em still overrides.
- Risk: low. Reward: medium.

### Stances: Guard had no cost
- Design-course notes: a dominant strategy removes the choice; fix it by giving each option a
  direct cost. Players report "no point to ever use" a stance whose trade is lopsided.
- Old: Guard took −20% damage at no cost. **New:** Aggressive ×1.2 dealt / ×1.15 taken, engage
  range ×1.4; Guard ×0.85 dealt / ×0.8 taken, engage ≤4; Sneak ×0.9 dealt, only fights back, and
  idle enemies notice the pack at 4 tiles instead of 6 (so rooms can really be slipped past).
- Risk: low. Reward: medium.

### Path abilities (slice 2) replace the placeholder leanings
- From the evolution research: forms should differ in *what they do*, not by +8%. Each of the 24
  paths gets one behaviour built from existing hooks (on-hit effects, heals, taunt, armor), at full
  strength from stage 2 and ×1.5 at stage 3. No new art.
- Risk: medium (24 small behaviours, untested). Reward: high.

### Rule-changing relics
- Slay the Spire players rank effects that change how every fight plays above flat stat boosts.
  "Build-around" relics are strong only if the run supports them, and that is where their interest
  comes from.
- **Synthesis:** keep the flat relics as the common baseline and add 4 build-arounds that tie to
  other systems: Ravenous Bell (starving creatures deal double, not half: tempts you to let hunger
  run), Prism Collar (no element bonds; each distinct element gives everyone +4%: diversity
  vs bonds), Comet Harness (thrown creatures burst on impact, area hit plus on-hit effects),
  Kennel Bell (resting creatures get half the shared kill XP: makes the bench a nursery).
- Risk: low. Reward: medium.

Sources: [Party Size, Seeding, and the Bench](https://www.worldanvil.com/w/grimdar-gmgilbert451/a/party-size2C-seeding2C-and-the-bench-article),
[Darkest Dungeon wiki: Size](https://darkestdungeon.fandom.com/wiki/Size),
[Quarter to Three roguelike thread](https://forum.quartertothree.com/t/what-is-your-current-favorite-roguelike-or-all-things-roguelike/50736?page=93),
[Jegged: FF12 Gambits](https://jegged.com/Games/Final-Fantasy-XII/Gambits/),
[StrategyWiki: FF12 Gambits](https://strategywiki.org/wiki/Final_Fantasy_XII/Gambits),
[G54GAM lecture 7 (dominant strategies)](https://people.cs.nott.ac.uk/pszmdf/g54gam/g54gam_lecture07.pdf),
[Paizo: Combat Stances](https://paizo.com/threads/rzs2i86a),
[metabot.gg: StS2 relics](https://metabot.gg/en/slay-the-spire-2/guides/relics-how-they-work-and-evaluate),
[Steam: Nuclear Battery discussion](https://steamcommunity.com/app/646570/discussions/0/1694914735989892966),
[untapped.gg: directional relic signals](https://sts2.untapped.gg/articles/directional-relic-signals).

### "ZZZ vibes" style test (2026-10-31)
Sources: Siliconera interview with ZZZ producer Zhenyu Li (https://www.siliconera.com/interview-preparing-zenless-zone-zero-2-0-and-its-characters/),
Gfinity on the style (https://www.gfinityesports.com/article/style-skill-and-persona-vibes-why-zenless-zone-zero-is-the-only-gacha-ill-take-seriously),
Pocket Tactics on redesign sameness (https://www.pockettactics.com/zenless-zone-zero/redesign).
- Why it works (dev): outfits come from modern clothing, and each outfit carries its faction's identity so it
  aids recognition. Fan/press reading (interpretation): 80s-90s urban street fashion, techwear (straps,
  big buckles, layers), bold graphic street-art feel.
- Thesis: borrow the vibe through words (street fashion, techwear, bold graphic cel look, neon accents),
  never the game's name or its characters.
- Antithesis: a harsh, cool urban look fights our kawaii plush chibi; and critics note ZZZ outfits start to
  look alike, which breaks our per-species silhouette rule.
- Synthesis: keep the chibi body and face; take the street-fashion outfit language and bold graphic
  rendering only; the outfit still differs per species (techwear piece chosen to fit the element).

### ZZZ clothing, without techwear / 1990s street (2026-10-31)
Sources: Wikipedia character list (https://en.wikipedia.org/wiki/List_of_Zenless_Zone_Zero_characters),
ONE Esports on Caesar/Burnice (https://www.oneesports.gg/zenless-zone-zero/caesar-king-burnice-white/),
Destructoid faction list (https://www.destructoid.com/all-factions-in-zenless-zone-zero-and-what-characters-are-included/).
- Pattern (checked for Victoria Housekeeping: Victorian butlers/maids + horror-movie tropes; press for the
  rest): each faction = one recognizable job or uniform (maids, bikers, construction crew) + one twist.
  The uniform tells who they are at a glance; the twist makes it theirs.
- Thesis: give each species a job uniform that fits its role, twisted by its element.
- Antithesis: real-world uniforms make them read as humans in costume, not monster pets, and clash with a
  fantasy dungeon; several uniforms (miner, construction) share one outline.
- Synthesis: uniform as shape language only, built from the element (moss, ice, petals) in plain colors;
  pick jobs with clearly different outlines; one uniform per species line, stages add pieces to it.

## Hair glued to arms in Meshy auto-rig (2026-10-31)

Emberpup v21 l2 rig: side hair touching the T-posed arms got arm weights and moves with them.
- Auto-weighting bleeds between parts that touch or sit close; the usual fixes are bind hair to the head
  bone or its own chain, or hand-paint weights ([SkinKit docs](https://superhivemarket.com/products/skinkit/docs),
  [Blender Artists: rigging hair](https://blenderartists.org/t/rigging-hair-problem/571142),
  [Blender Artists: long hair](https://blenderartists.org/t/im-having-trouble-rigging-long-hair/1596531)).
- Meshy's rigger has no hair option or weight painting; its guide blames heavy limb deformation on
  unusual proportions ([Meshy auto-rigging tutorial](https://www.meshy.ai/vi/tutorials/character-auto-rigging-workflow)).
- Thesis: fix weights after rigging (Blender script moving hair verts to the head bone).
  Antithesis: hair and body are one mesh with no hair label, so picking hair verts is guesswork per model,
  ×36 models; high risk. Synthesis: prevent it in the concept: no hair beside the shoulders or over the
  arms in the T-pose, hair falls behind the shoulders, with a visible gap to the arms. Cheap (one concept)
  and fixes every species at once through the shared style block.
- Stage 2/3 drift bigger than stage 1 (v21 l2): "the evolved second form" / "final evolved form" likely
  pulls toward a grown-up figure; dropped from the name line, stages stated through their pieces only.

## Levels as stages, scarcer food, a vulnerable player (2026-10-31, user direction)

- **Levels = stages (1, 2, 3), then stars.** "Level" did two jobs: a frequent stat drip and the
  decision points (evolution, path pick). Only the second makes choices, so levels now *are* the
  stages, like Pikmin's leaf, bud, flower. **Antithesis:** an infinite dungeon needs endless growth,
  and a 3-level cap stalls. **Synthesis:** each full bar past Lv 3 gives a star (+8% HP, attack,
  healing); perk picks per star can come later. Captive levels, elixirs (half a bar) and Kinship
  (30% of a bar) changed to match. Risk: low (numbers). Reward: medium; the pacing is a guess.
- **Food about a third scarcer** (enemy drops 15% → 10%, chests 1–2 / 2–4 / 3–5, larders 1–3
  pickups). The bench, feeding for paths and Ravenous Bell only matter if food is tight; the old
  bot data (20–60 held) said it wasn't.
- **Vulnerable player** (HP 100 + 10 per floor, regen 0.6%/s, enemy preference for creatures ×1.3
  instead of ×1.8). A player who can't be hurt has no reason to act; pressure on the player is
  what makes positioning and pack orders matter. Source: the user's playtest ("I just walk").
- Open question this raised: the player still has few decisions in a fight, because creatures
  choose everything themselves (see the commander-model proposal, next).
- v21 h1 result: the "no hair beside the shoulders / clear space" wording failed on all three stages; hair
  still hangs at the sides behind the arms. Image models handle negation poorly (they see the words
  "hair beside her shoulders"). Next: describe a positive shape that has no side hair (e.g. hair gathered up).

## Commander model: the player decides who fights (proposal, 2026-10-31)

Playtest (user): "there is no strategy... I just walk and unlock new creatures and feed them."
The abstract problem: a decision the game makes for you isn't strategy. The pack picks its own
targets, engages, eats and revives, so the player's only frequent inputs are walking and bookkeeping.

- **Pikmin:** the developers found that letting Pikmin act freely "would frustrate players", so
  they mostly wait for orders, with only a hint of free will. Throwing became deep once the throw
  had a consequence (sticking to weak points). Miyamoto rejected a touch-pen version because pure
  "unit management" didn't feel like Pikmin: orders must be direct, physical actions.
- **Overlord:** you sweep or send minions by colour, and each colour is a role (blues revive, reds
  fire). The strategy is *which colour to send where*. Reviewers praise the right-stick send and
  fault imprecise control and minions that wander off to loot.
- **Little King's Story:** whoever stands right behind the king is sent next, so the *order of the
  line* is the selection. Only 5 citizens follow early on; classes decide what each one can do.
- **Companion design writing:** bounded autonomy (rules that set limits, not exact behaviours) keeps
  companions alive without competing with the player's agency. Companions work best as
  *extensions of the player's decisions*. High-level mode switching (Dragon Age II's aggressive
  modes; our stances) is the weakest form of control.

**Thesis (now):** autonomous pets feel alive and cost no attention.
**Antithesis:** the playtest shows the result: autonomy leaves the player nothing to decide. Pikmin's
developers reached the same conclusion.
**Synthesis:** bounded autonomy. Creatures follow and *defend* (they hit back at whatever attacks
them or the player), but they only *start* fights when sent. Sending is one direct action at the
crosshair, and the choice of *who* to send (element, role, HP) is the strategy. The old autonomy
stays available as a stance with a cost, so it's a choice, not the default.

Risk: medium (rewrites creature fight AI; one new control). Reward: high (it is the core loop).

Sources: [Siliconera: Miyamoto discusses Pikmin design](https://www.siliconera.com/shigeru-miyamoto-discusses-pikmin-design/),
[Ask the Developer: Pikmin 4](https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-10-pikmin-4-part-1/),
[Unseen64: Pikmin beta](https://www.unseen64.net/?p=728),
[Fullcleared: why Pikmin isn't on 3DS](https://fullcleared.com/news/why-pikmin-isnt-on-3ds/),
[Expert Reviews: Overlord II](https://www.expertreviews.co.uk/technology/gaming/codemasters-overlord-ii-review),
[GameBanshee: Overlord review](https://gamebanshee.com/x6c6),
[Engadget: Little King's Story review](https://www.engadget.com/2009-07-23-review-little-kings-story-wii.html),
[RPGFan: Little King's Story](https://www.rpgfan.com/review/little-kings-story/),
[Game Developer: Thinking about Elizabeth, part 2](https://www.gamedeveloper.com/design/thinking-about-elizabeth-part-2),
[Adaptive Companions in FPS Games](https://www.cs.mcgill.ca/~jtremb59/Papers/Adaptive%20Companions%20in%20FPS%20Games.pdf).
- v21 p3 (high ponytail): side hair gone and stage proportions now match, but in a front view the image
  model swings a long ponytail out to one side so it shows, where it hangs behind an arm. A hanging
  ponytail longer than the neck will always land at arm height on a chibi; the hair has to end above the
  shoulders (short upswept ponytail or bun).

### Does a command model work in first person? (2026-10-31)
- **Pikmin 3:** hold a Pikmin and throw the currently selected type; a button cycles the type; lock
  on to a target and "charge" sends the whole group (Deluxe allows charging without a lock).
  That's third person, built for an overview of up to 100 units.
- **Republic Commando** is first-person with a 4-member squad: aim the crosshair at a spot or
  target and one button orders the squad there; context spots highlight under the crosshair. Reviews
  call it simple but effective once missions give orders real context.
- **Fit:** our pack is 5 named individuals, not a swarm, which is the Republic Commando scale, and
  crosshair aiming is more precise than Pikmin's cursor. The first-person cost is losing sight of
  the pack: the HUD pack list must show who's next, HP and who is busy.

Sources: [Pikmin wiki: Lock-on](https://www.pikminwiki.com/Lock-on), [Pikmin wiki: Charge](https://www.pikminwiki.com/Charge),
[Pikmin 3 electronic manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/wii_u_6/pikmin_5/ElectronicManual_WiiU_Pikmin3_EN.pdf),
[Wikipedia: Republic Commando](https://en.wikipedia.org/wiki/Star_Wars:_Republic_Commando),
[StrategyWiki: Republic Commando gameplay](https://strategywiki.org/wiki/Star_Wars:_Republic_Commando/Gameplay),
[GameSpot: Republic Commando hands-on](https://www.gamespot.com/articles/star-wars-republic-commando-hands-on/1100-6098140/).
- **Dropped (user, 2026-10-31):** the whole v21 eye/hair/rig redo (l1, l2, h1, p3 and the new stage 1
  model). Back to the previous design and prompts; the v16 Emberpup models stay in game. Cause found for
  the record: shoulder-length hair + a head wider than the shoulders puts hair on the T-posed arms.

## How creatures are acquired, for planned combinations (proposal, 2026-10-31)

The question (user): should recruiting go, with creatures coming some other way? The abstract
problem: combinations are only planned if acquisition is a *choice*. Today a cage holds one random
captive: take it or leave it, so the pack is what the dice gave you.

- **Slay the Spire:** every card reward is 1 of 3, or skip. Skipping is a real deck-building choice,
  because adding a card dilutes the plan. Advice: take a card only if it fits your plan or fills a gap.
- **Super Auto Pets:** a shop of random pets; you roll (pay to refresh) and freeze (keep an offer).
  Two copies of the same pet combine into one with more XP, so duplicates are progress, not clutter.
  Higher-level pets usually win, which makes chasing duplicates a strategy of its own.
- **Dragon Quest Monsters:** synthesis fuses two monsters into a new one that inherits skills; some
  monsters exist only as specific combinations, which makes experimenting with recipes the appeal.
  (No developer statement on intent found.)

**Thesis:** drop recruiting, give creatures through a shop or draft. **Antithesis:** freeing a
captive is a good in-world moment (a fight with a payoff), and the cage room gives the map a goal;
the problem is the lack of choice, not recruiting itself. **Synthesis (proposed):** keep cages but
make each one a pick of 1 of 3 (the rest flee), shown on the map once scouted so you can route for
the creature you need; same-species duplicates merge into Growth (Super Auto Pets), so a pick
that doesn't fit the plan still pays. Cross-species fusion is dropped: every hybrid would need new
art (high risk, cost not worth it now).

Sources: [Slay the Spire wiki: Card Rewards](https://slay-the-spire.fandom.com/wiki/Card_Rewards),
[Switchblade Gaming: StS2 tips](https://www.switchbladegaming.com/strategy-games/slay-the-spire-2-tips/),
[Super Auto Pets wiki: The Basics](https://superautopets.wiki.gg/wiki/The_Basics),
[Super Auto Pets wiki: Experience](https://superautopets.wiki.gg/wiki/Experience),
[Two Average Gamers: SAP mechanics](https://www.twoaveragegamers.com/ultimate-guide-to-super-auto-pets-game-mechanics/),
[Dragon Quest wiki: Monster synthesis](https://dragon-quest.org/wiki/Monster_synthesis),
[Gematsu: DQM Joker 3 synthesis](https://gematsu.com/2016/01/dragon-quest-monsters-joker-3-details-monster-synthesis).

## Synergies: TFT traits or Bloons-like? (proposal, 2026-10-31)

- **Teamfight Tactics:** every unit has an origin and a class (2–3 traits). A trait pays at
  breakpoints (2/4/6), and the bonus grows at each tier. The core tension is *vertical* (stack one
  trait deep) against *horizontal* (many traits at low tiers), and units that carry two wanted traits
  are worth more. Riot interview: a unit with a unique synergy makes the build path obvious; shared
  traits keep it flexible. Emblems add a trait to a unit.
- **Bloons TD 6:** each tower answers threats (camo, lead, ceramics), so a build needs *coverage*.
  Support towers (Monkey Village, Alchemist) buff towers in range; buffs stacked on one strong tower
  beat spreading them thin. Placement is the synergy.
- **What we have:** each creature already carries two tags, element (8, like an origin) and role
  (4, like a class). But the bonuses are flat percentages (element pair +10/+20%, all 4 roles +10%
  HP), and with 12 species most elements have only 1 species, so going vertical on an element is
  impossible.
- **Thesis (TFT):** trait breakpoints that change behaviour, not numbers. **Antithesis:** a
  5-slot pack and 12 species leave little room for breakpoints; 4/6 tiers can't be reached.
  **Synthesis (proposed):** breakpoints at 2 and 3 only; give each species a second, overlapping
  family tag (Beast, Spirit, Plant…) so verticals are reachable; each tier changes behaviour.
  Borrow Bloons *coverage*: enemy types that need an answer (flying, armored, hidden), so a
  composition has to cover threats as well as stack bonuses.

Sources: [Esports Tales: TFT origins and classes](https://esportstales.com/teamfight-tactics/origins-and-classes-trait-bonuses),
[Inven Global: TFT traits](https://www.invenglobal.com/teamfighttactics/articles/8426/teamfight-tactics-whats-known-whats-different-traits-of-origins-and-classes),
[Inven Global: TFT developers interview](https://www.invenglobal.com/articles/23690/tft-developers-unreal-engine-is-just-the-beginning),
[esports.gg: TFT emblems and traits](https://esports.gg/news/teamfight-tactics/tft-emblems-and-traits-explained),
[Bloons wiki: Alchemist crosspathing](https://bloons.fandom.com/wiki/Crosspathing/Alchemist),
[Bloons wiki: Tower buffs](https://bloons.fandom.com/wiki/Tower_Buffs),
[bloonswiki: Alchemist strategy](https://www.bloonswiki.com/Strategy:Alchemist_(BTD6)).

### Recruiting procedure: cage, shop, or both? (proposal, 2026-10-31)
- Recruiting must give (a) a choice, (b) a cost, (c) a way to aim at a planned trait, and (d) enough
  chances per run. TFT's and Super Auto Pets' shops give all four through gold, rolls and freezes.
  A cage pick gives choice and a cost (the fight) but aims only through scouting.
- **Thesis (shop only):** best aim, the TFT feel. **Antithesis:** a first-person dungeon run
  becomes a menu game between corridors, and a shop needs a currency. **Synthesis (proposed):**
  cages stay the earned source (pick 1 of 3), and a trader room on most floors sells 3 creatures
  for food, with a reroll for food and one freeze that carries to the next floor. Food as the
  currency keeps the run's one-resource tension (feed, grow, or recruit).

### Rescued eggs: the player decides what hatches (proposal, 2026-10-31, user idea)
- **Monster Sanctuary:** monsters drop eggs in combat, and you hatch them from the menu when you choose.
  Hatchlings start near the party's level, so a new member never needs grinding.
- **Randomness vs control** (thesis and blog sources): randomness gives variety and replay value;
  too much control "breeds monotony" (the same best team every run). Recommended: pockets of
  randomness with agency inside them.
- **Thesis (user):** rescue eggs instead of captives and let the player decide what they become, the
  strongest way to aim at traits. **Antithesis:** if every egg can be anything, every run builds the
  same best team. **Synthesis (proposed):** each egg shows 3 possible species (random, like a 1-of-3
  pick), and the player picks one by *feeding*: each candidate is tied to one flavor, and the flavor
  fed most when the egg hatches (3 treats) decides it. That reuses the diet mechanic, makes recruiting
  cost food, and keeps the choice bounded by the egg's random three. Eggs come from guarded nests (the
  old prison rooms) and wait in the pouch until fed, so they also store a decision until the floor
  shows what's needed.

Sources: [Siliconera: Monster Sanctuary](https://www.siliconera.com/monster-sanctuary-players-collect-monsters-unique-battle-parties/),
[Use a Potion: Monster Sanctuary review](https://useapotion.com/2020/12/monster-sanctuary-review),
[Zelda Dungeon forum: Monster Sanctuary](https://www.zeldadungeon.net/forum/threads/monster-sanctuary.69435/),
[Theseus: Balancing randomness in action roguelikes](https://www.theseus.fi/handle/10024/886802),
[Wayline: roguelike itemization](https://www.wayline.io/blog/roguelike-itemization-balancing-randomness-player-agency),
[Game Developer: purposes of randomization](https://www.gamedeveloper.com/design/analysis-purposes-for-randomization-in-game-design).

## Rewarding careful composition (design rule, 2026-10-31)

User goal: punish a player who doesn't think about composition and reward one who does.

- **Slay the Spire's elites and bosses are "checks":** a Slay the Spire 2 guide calls elites a test
  "waiting to severely punish players who haven't drafted a cohesive deck". Players name specific
  checks: front-loaded damage, AoE, scaling over a long fight. **The criticism:** checks you
  couldn't foresee or counter feel like unfair deck punishment, not a skill test.
- **Multiplicative vs additive:** multiplicative bonuses reward pushing one build further, while
  additive ones give diminishing returns (forum and dev posts). So synergy should multiply and
  raw head count should add.
- **Bounded randomness** (earlier section): randomness gives variety; agency inside it keeps losses
  fair.

**Thesis:** hard counters (immunities) make careless packs fail. **Antithesis:** random offers can
deny the answer, and a wall you couldn't prepare for is luck, not skill; StS players complain about
exactly that. **Synthesis (the rule in DESIGN.md):** soft counters with at least 2 answers each, every
check announced before it bites, multiplicative synergy, rising upkeep so taking everyone dilutes,
a death recap that names the cause, and enough picks to aim. The bot measures the gap between a random
pack and a planned one.

Sources: [untapped.gg: Elites in StS2](https://sts2.untapped.gg/guides/elites-intro),
[Mobalytics: StS2 beginner guide](https://mobalytics.gg/slay-the-spire-2/guides/beginner-guide),
[Steam: StS discussion on elite checks](https://steamcommunity.com/app/646570/discussions/0/1797403972751796670),
[Steam: StS discussion on unfair counters](https://steamcommunity.com/app/646570/discussions/0/4522261847580260177),
[rpgmaker.net: additive vs multiplicative buffs](https://rpgmaker.net/users/Rine/posts/?p=10),
[StraySpark: roguelike progression](https://www.strayspark.studio/blog/building-roguelike-ue5-procedural-progression).

### Generalized: "thinking pays" for every concept (2026-10-31)
User: the same principle must hold for any concept or design, not just composition. The
composition findings generalize: a choice only matters if the careless option has a real cost
that bites at a known point (checks), the careful player could see it coming (information before
commitment), the reward is big and visible (multiplicative, new behaviour), and failure is soft and
readable. Recorded as Rule 1 in DESIGN.md, with a 4-question test every feature must answer.

### Investigation: what makes thinking pay, in general (2026-10-31)
- **Sid Meier:** "a game is a series of interesting decisions" (GDC 1989, revisited in his GDC 2012
  talk "Interesting Decisions").
- **Interesting decisions** (Game Developer article): the choice must have **consequences** (or the
  decision doesn't matter), be **predictable enough** (opaque outcomes frustrate), and be
  **non-obvious** (if one option is clearly better, there's no decision). **When not to:** too many
  options or too much information cause analysis paralysis; a choice that rarely matters or always
  resolves the same way should be removed or automated.
- **Salen & Zimmerman, meaningful play:** the link between action and outcome must be
  **discernible** (the player sees the system shift) and **integrated** (it affects play later on).
  That's our "readable failure" and "bites at a known point".
- **Soren Johnson:** "Given the opportunity, players will optimize the fun out of a game." A single
  dominant strategy drowns out the rest (Koster). Fix: make the boring, efficient method weak, not
  merely discouraged (GMTK, "How Game Designers Protect Players From Themselves").
- **Keith Burgun:** strategy needs *ambiguous* decisions ("should I", not "can I"); a system that's
  too solvable becomes a puzzle with one answer. So careful play must depend on the situation.

Applied: Rule 1 in DESIGN.md gained "No formula", "The best path is the fun path" and "Don't make
everything a decision".

Sources: [Game Developer: Sid Meier explores interesting decisions](https://gamedeveloper.com/design/video-sid-meier-explores-interesting-decisions-in-gameplay),
[Game Developer: Designing interesting decisions (and when not to)](https://www.gamedeveloper.com/design/designing-interesting-decisions-in-games-and-when-not-to-),
[Wikipedia: Meaningful play](https://en.wikipedia.org/wiki/Meaningful_play),
[Designer Notes: Water Finds a Crack](https://designer-notes.com/game-developer-column-17-water-finds-a-crack),
[TheGamer: players optimize fun out of games](https://www.thegamer.com/players-optimize-fun-out-of-games),
[Game Developer: There's cheese in your game](https://www.gamedeveloper.com/design/there-s-cheese-in-your-game-),
[GMTK: How Game Designers Protect Players From Themselves](https://amara.org/v/C3BEs),
[Game Developer: What makes a game? (Burgun)](https://www.gamedeveloper.com/design/what-makes-a-game-),
[Keith Burgun: Solvability in games](https://keithburgun.net/solvability-vs-depth/),
[Game Developer: Three perspectives on strategy game design](https://www.gamedeveloper.com/design/three-perspectives-on-strategy-game-design).

## Reactions and threats (design for Rule 2, 2026-10-31)

- **Genshin Impact:** team building revolves around *elemental reactions*. One element leaves an
  aura on the enemy, and a second element triggers a reaction on it (Vaporize, Melt,
  Electro-Charged, Swirl, Superconduct); some reactions set up follow-ups (Quicken → Spread or
  Aggravate). Teams are built from pairs of elements that react. (Sources here are thin guides;
  the mechanic is well known.)
- **Divinity: Original Sin 2:** surfaces combine: water + electricity electrifies, fire + poison
  explodes, water + fire makes steam; players call electrified water among the most damaging
  interactions. Mixing elements carelessly can also cancel your own effects.
- **Thesis:** reactions make two creatures worth more together than apart, so composition is
  planning ("I have a soaker, I want storm"). **Antithesis:** too many statuses and reactions
  become unreadable in a real-time first-person fight. **Synthesis:** 5 statuses, 8 reactions, icons
  over foes, every first trigger recorded in the codex, and a pack-screen panel that lists what you
  can trigger. Water vs fire is a deliberate clash, so mixing everything carelessly costs.
- **Threats as checks** follow Slay the Spire's elites (see "Rewarding careful composition"), with
  at least 2 answers each and announced ahead, so they test thinking, not luck.

Sources: [Sportskeeda: Genshin Quicken reactions](https://www.sportskeeda.com/esports/genshin-impact-quicken-reaction-guide-team-recommendations),
[KeenGamer: Genshin team building tips](https://www.keengamer.com/articles/guides/genshin-impact-tips-for-team-building/),
[Fextralife: DOS2 Elemental Affinity](https://divinityoriginalsin2.wiki.fextralife.com/Elemental+Affinity),
[Steam: DOS EE surface combinations](https://steamcommunity.com/app/373420/discussions/0/601898034735931327/),
[Steam: DOS2 electrified water discussion](https://steamcommunity.com/app/435150/discussions/0/2425614361137675556),
[GameBanshee: Divinity: Original Sin review](https://www.gamebanshee.com/kuprh).

## Rewards and punishment: composition, gear, evolution (proposal, 2026-10-31)

User goal: reward good creature composition, good gear and good evolution; decide how to punish.

- **TFT items:** most boards put items on 1–2 carries, matched to role (attack items on attackers,
  spell items on casters). Early "item holders" carry items until the real carry arrives. The
  decision is *who carries it*, and an item fixes a specific unit's weak point.
- **Lootbound:** companions follow the hero's gear rules (only equipped items count), so gear shapes
  party behaviour. A player disliked tradeoff items ("very few situations I'd take them"); the dev
  answered that advantage-only items make the game too easy.
- **Roguelike item design (Game Developer):** a small pool of items with several interactions beats
  many single-purpose or purely bad ones.
- From memory, not checked this session: Darkest Dungeon trinkets carry a downside and are class
  locked; Pokémon held items are one slot per creature.

**Thesis:** per-creature gear (one held charm each) adds a "who carries it" decision that ties gear
to composition. **Antithesis:** another inventory and menu in a first-person action game; relics
already give run-wide numbers; "don't make everything a decision". **Synthesis:** one slot, equipped
by throwing the charm at a creature (reuses the feeding throw, no menu, works on a gamepad); few
charms, each tied to a status, reaction or threat answer, so the right carrier gets ×1.5+ or new
behaviour and the wrong one gets almost nothing. Misplacing it costs the opportunity, not HP (soft).

Sources: [metabot: TFT items guide](https://metabot.gg/en/TFT/guides/tft-items-components-recipes-how-to-combine),
[bamboogaming: TFT items](https://www.bamboogaming.net/tft/items),
[playtester.io: Lootbound](https://playtester.io/lootbound),
[Steam: Lootbound](https://store.steampowered.com/app/3091140/Lootbound),
[Game Developer: Roguelike item and monster design revisited](https://www.gamedeveloper.com/design/roguelike-item-and-monster-design-revisited).

### Built: payoff paths, reaction power, reworked gear (2026-10-31, AFK)
- **The underlying problem:** the pack is a portfolio pulled two ways. **Depth** (a setter and a
  payoff that react) wants a narrow, specific pack; **coverage** (answers to the 5 threats) wants
  a wide one. Upkeep taxes width. So the three systems take separate jobs: composition picks the
  core, **evolution adds depth** (payoff paths need a setter partner), and **gear adds coverage
  without a mouth to feed** (setters and threat answers on one slot, no upkeep).
- **Thin-deck lesson (Roguebook designers):** when trimming to a lean combo always wins, every run
  plays the same. Here the counter is built in: a lean reaction pack with no coverage hits the
  floor's announced threat (soft walls), and threats change per floor, so there's no single
  answer (Rule 1, "no formula").
- **Fairness (Bugnet; Game Developer, "How punishment systems hurt gameplay"):** a loss feels fair
  when the player understands why and believes they could have done better; extra penalties stacked
  on top of losing make it worse. Matches "readable failure" and "soft punishment".
- **Loss aversion (U. Saskatchewan thesis, 2021, a Zelda-like game):** prospective losses weigh
  more than equal gains. So a careless choice should cost **missed gain** where possible (a payoff
  path with no partner does nothing extra; misplaced gear does little) rather than taking things
  away. From memory, not checked: WoW's rested XP was reframed from an "overplay penalty" into a
  bonus with the same math, and players accepted it.

**Thesis:** make every careless choice cost something. **Antithesis:** taking things away feels
worse than the same size missed gain, and stacked penalties drive players off. **Synthesis:** gear
and evolution punish carelessness only as missed gain (×1 instead of ×2–5); the hard costs stay where
they already are (upkeep, hunger, fainting), all in one channel (time → hunger → HP).

Sources: [Bugnet: how to make a roguelike feel fair](https://bugnet.io/blog/how-to-make-a-roguelike-feel-fair),
[Game Developer: How punishment systems hurt gameplay](https://www.gamedeveloper.com/design/how-punishment-systems-hurt-gameplay),
[Game Developer: Making failure fun](https://www.gamedeveloper.com/design/making-failure-fun),
[USask: Loss aversion in an adventure video game](https://harvest.usask.ca/handle/10388/13478),
[Film Stories: Roguebook preview](https://filmstories.co.uk/gaming/roguebook-we-want-players-to-break-the-game/),
[Gamasutra: Roguebook deckbuilding design](https://gamasutra.com/design/tackling-deckbuilding-design-in-abrakam-s-roguebook).

### Measured: does thinking pay? (arena, 2026-10-31, AFK)
Arena: 4 creatures at Lv 2, 10 seeds each, the player standing still (`--test=arena`, `--pack`
now takes `species:level:path:gear`).

| Setup | vs 3 Golems (armored), floor 5 | vs 8 Skeletons, floor 6 |
|---|---|---|
| Unplanned (fire + water clash, no answer) | 1/10 wins | 7/10, 38 s |
| Planned, defensive paths | 7/10, 51 s | 10/10, 18 s |
| Planned, payoff paths | 8/10, 42 s | 8/10, 33 s |
| Payoff + Catalyst Band on the payoff creature | 8/10, 44 s | 10/10, 19 s |
| Payoff + Catalyst Band on a setter (misplaced) | 8/10, 43 s | 6/10, 47 s |

- Composition pays big against a check (1/10 → 8/10). Gear placement pays: the right wearer
  is about 2.5× faster than the wrong one on the swarm. Paths have no dominant answer (payoff
  wins against armor, defensive paths against a swarm), as Rule 1's "no formula" wants.
- The first full-bot batch (12 runs each, before the targeting fix) showed only +0.8 floors for the
  careful bot: runs vary from floor 1 to 12, and the bot never dodges, so player deaths drown the
  signal. Reactions were rare (about one per two kills) because creatures kept their first target;
  fixed by reaction-seeking targeting (DESIGN.md, Targeting).

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
