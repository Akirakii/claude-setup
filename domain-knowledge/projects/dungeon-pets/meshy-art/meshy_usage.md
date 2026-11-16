# Meshy usage

How we make character art with Meshy AI, the shared style, and the design of every character.
Rules in DESIGN.md decide what exists; this file decides how it looks and how it is made.

## Pipeline

**Steps 1–4, the costs and the lessons moved up to `~/.claude/domain-knowledge/shared/meshy/meshy-pipeline.md` (2026-11-16); what stays here is this game's own wiring, style and characters.**

5. **Wire.** Save as `assets/models/creatures/<id>_s<N>_rigged.glb` (enemies: `assets/models/enemies/<id>_rigged.glb`)
   and list it in the species `.tres` (`stage_models`) or enemy `.tres` (`model`).

Concepts go to `art/concepts/<id>_s<N>.png` (`art/` is ignored by Godot).

### Costs

Full creature set: 12 species × 3 stages = 36 models ≈ 940 credits, plus ~15% for regenerations.

### Animations (shared)

All Meshy rigs use the same 24-bone humanoid skeleton, so a clip bought once plays on every rig.
In use (`AnimLib`): idle, attack (kick), attack2 (thrust), cast from `chibi_anims.glb`; hit and knockdown
from `shared_anims.glb`; walk and run from `emberpup_s1_walk.glb` / `_run.glb`.
The Hips track is absolute in its source rig's units, so `AnimLib` records each source rig's hip height and
scales the track per target rig (otherwise models crouch or float). New clips: `meshy_animate` on any rig, 3 credits each.
Candidates not bought yet: 92 Double Combo Attack, 224 Archery Shot, 127 Charged Ground Slam, 8 Dead.

### Expressions (parked)

Expressions (> < when carried, ^ ^ when petted, x x when fainted) must be **in the model's texture**
(a texture swap), never overlays drawn over the face. Test built for Bloomling stage 1 only:
`tools/paint_expression.py bloomling 1` paints `bloomling_s1_squint.png` (> < eyes) and
`ModelVisual.set_emote` swaps it in while carried. Other creatures keep no-op emotes.

### Lessons (this game's cases; the lessons themselves moved up)

- Neck accessories: the grey band was seen on Emberpup v16; the ban was lifted (user, 2026-10-31), watch for it in 3D.
- The chibi clips are in `assets/models/anims/chibi_anims.glb`, bought on the v16 Emberpup rig.
- Stormheart's loose lightning bolts were the floating parts that broke the rig.
- The game turns the models 180°, since they face +Z.

## Shared style (creatures)

Every creature is an **adult anthro monster girl** in one look: 2D anime concept (crisp lineart, cel shading)
turned into a 3D model, kawaii chibi (head half
her height), flat manga face, gentle glowing eyes half under the bangs, a thick curvy pear-shaped body with short
stubby arms and legs, strongly animal-like. Each species has its own expression, hairstyle and top
(user, 2026-10-31: hair and top are no longer shared). A prompt is three parts: style, species, framing.

### Variety rules (user, 2026-10-30)

The first set all wear the same crop top and read alike. From now on:
- **Distinct silhouette per species:** each creature must be recognizable from its black outline alone
  (ear and tail shape, hair mass, clothing outline, body build). Check by filling the concept art black.
- **Clothing varies by species:** no shared crop top. Each species gets its own kind of top or outfit
  that fits its theme (e.g. hoodie, vest, kimono-style wrap, tube top, harness, bandeau, poncho, apron).
  A bottom is optional, not banned; boots, leg wraps or socks are allowed.
- **Body shape varies a little:** keep the shared chibi head and soft adult build, but vary it per species
  (stockier, leaner, rounder, taller) so builds differ at a glance.
- **Evolution forms keep the species' outline language** (same ears and tail family) and change the
  outfit and silhouette enough that path A and path B are told apart at a distance.
- In game, model height is fitted feet-to-skull (the rig's `head_end` bone), so ears no longer shrink a creature.

### Style block

> [Name], a kawaii chibi anthropomorphic [animal] monster girl, adult. 2D anime illustration style:
> bold urban street-fashion anime style: thick confident black outlines, high-contrast cel shading with
> hard-edged shadow shapes, saturated colors with a few small neon accents, clean graphic shapes; the eyes
> are the one softly painted, glowing area. Huge oversized chibi head, even bigger than her whole body below the neck:
> the head is more than half of her total height and much wider than her shoulders. Highly stylized manga face: flat cute
> anime face with only a tiny button snout and [nose] instead of a long muzzle. Enormous, slightly wide,
> gentle anime eyes that fill most of her face, from just under the bangs down to the top of her cheeks,
> each eye wider than the gap between them, with a soft, slightly heavy upper lid: huge, very thick, heavy eyelashes: a bold, very
> dark [lash color] upper lash line on each eye ending in two or three huge, long, thick winged lashes
> that fan far outward and upward past the outer corner, each nearly as long as the eye is wide, plus a
> few smaller thick lashes along the lid and a short lower lash line; the lashes stay big and clearly
> visible in front of the bangs. Glowing galaxy
> irises: each iris looks like a tiny galaxy, deep [iris dark] at the top fading to a bright, luminous
> [iris light] in the lower half, with soft swirling nebula clouds of lighter color and many scattered tiny
> star specks inside it, a dark pupil, one soft white highlight and a few four-point star sparkles. No eyeshadow and no
> colored shading around the eyes. Clearly visible blush: a light rosy blush on each cheek with three short,
> bold, diagonal pink blush lines drawn over it. Simple thin line mouth. Hair: [hairstyle, colors and
> streaks]. Her bangs are big, thick and heavy: a full, dense fringe of thick
> pointed locks that falls over the top of her eyes and partly covers them, with the eyes and lashes
> visible between the locks. Expression: [expression]. A super-deformed (SD) chibi, only 2 heads
> tall, like a plush toy: tiny nub arms, so short that the paw hands come right out of the sleeve ends;
> tiny nub legs, so short that her wide hips sit almost directly on her feet. Her body is pear-shaped:
> narrow shoulders and a small upper body with a round bust, a small waist, then a much wider bottom: her
> round hips are the widest part of her body, far wider than her shoulders. Big chunky paws, exaggerated
> proportions.

Eyes (user, 2026-10-31): replaced the bold black single winged lash with a soft reference style (thin
colored lash line, small outer flicks, glowing gradient iris, star sparkles, pink under-eye shadow).
Bangs partly cover the eyes. Limbs: v21 t1-t4 stayed long under every wording. v21 A/B (2026-10-31): A dropped `pose_mode`, kept
the "curvy hourglass adult figure ... thick thighs" body: limbs unchanged, so pose_mode is not the cause.
B kept `pose_mode: t-pose` with "SD chibi, only 2 heads tall ... like a plush toy" and no adult/hourglass
words: limbs clearly short, head bigger. Cause: the adult-figure words pulled the limbs long. Cost: the
curves are milder in B. v21 p1/p2: the big winged lash is back (in deep color) and the hips are wider
(pear), but the legs grew a little longer again than B.

Wording notes:
- The image model ignores fractions like "one third of her height"; describe proportions it can see
  ("as big as her whole body below the neck", "paw feet almost directly under her hips"). v21 t1/t2:
  "legs a third as long as her head" still gave head-length legs.
- Hair is not too short (user, 2026-10-31): a pixie cut is too short; shoulder length or longer is fine.
- Clothes are plain: v21 put a flame stamp on the hoodie, so the species block bans prints.
- It ignores "digitigrade" at chunky scale, so the line doesn't ask for it.
- Name the ear shape per species; it drifts otherwise.
- Hair is per species now (no shared hairstyle). "chunky sculpted locks" makes few thick blocks; "voluminous" alone grows a long mane. Describe the
  strands (many thin, pointed, uneven) and where each part falls (bangs, center lock, side locks).
- Half-lidded expressions shrink the eyes, and the bangs hide the eyebrows, so expressions live in the mouth.
- "Extra-long eyelashes" gives many small lashes (v16 note; the 2026-10-31 eye style wants a few small outer flicks).
- The animal reads through ears, nose, fur pattern and tail; the face itself stays manga-flat.
- Style words: "2D anime illustration" beats "low-poly 3D render" for faces. Painted features (lashes,
  blush, eye shine) and the lineart bake into the texture and stay crisp in 3D, giving a toon look.
- 2D wording pulls proportions toward a slimmer, smaller-headed figure; keep the head and body wording strong.
- From flat 2D art Meshy guesses depth: wispy hair can grow a swept-back mane in 3D. Accepted for now
  (v16); add "no hair at the back of the head" if it gets too big.

### Species block

> Strongly animal-like: [ears], [colors] [surface] everywhere, paw hands and paw feet,
> [tail]. [Accessory] and [top] in plain solid colors, slightly fitted so the round shape of her bust
> shows a little, with no print, logo or pattern; no bottom clothing,
> [surface] covers the lower body with smooth, non-detailed anatomy.

`[surface]` is fur for mammals; non-mammals use their own (listed per species below).

### Framing block

> Cute and cheerful. Single character only, full body, front view, T-pose with both arms straight out,
> plain white background, game character asset.

Later style tests (v17-v19, Bloomling and Emberpup only, no model made from them) keep their prompts in
`art/concepts/v17|v18|v19|v20/*.prompt.md` and their reasoning in `docs/research.md`.

### Stages

Each stage is its own text-to-image prompt: style block + species block with that stage's description
+ framing block. Stage 2 has the element more pronounced and one extra piece; stage 3 is the grandest
form. Evolution does not change size (user, 2026-10-31): every stage keeps the same height and proportions.
Head ratio, face, expression and base colors stay the same so the line reads as one creature.
In game every stage stands 1.33 tiles feet-to-skull (tanks ×1.08; DESIGN.md "Visual size").

### Example: Emberpup, stage 1 (v21 t3/t4 prompt; predates the new eyes and bangs)

> Emberpup, a kawaii chibi anthropomorphic fire-puppy monster girl, adult. 2D anime illustration style:
> clean digital anime art with crisp lineart, cel shading and flat colors, simple shapes. Oversized chibi
> head, as big as her whole body below the neck: the head is half of her total height and wider than her
> shoulders and hips. Highly stylized manga face: flat cute anime face with only a tiny button snout and
> small black nose instead of a long muzzle, huge wide-open energetic manga eyes, bright and sparkling with
> big white shine highlights and color-gradient irises, a thick bold black upper eyelid line on each eye
> ending in one single long winged lash: a dramatic winged-eyeliner flick that sweeps far outward and
> upward past the outer corner of the eye, no separate small lashes, simple thin line mouth, pink blush
> marks on the cheeks. Hair: shoulder-length layered hair with a few flame-shaped spikes on top and the
> ends flicking outward at her shoulders; thick straight bangs cover her eyebrows down to the top of her
> lash line; fiery orange-red with lighter yellow-orange flame streaks. Expression: energetic and
> confident, a cheeky smirk with a tiny fang. Short, thick, sturdy body with soft chunky proportions: a
> curvy hourglass adult figure with a fuller, rounded chest, a narrow defined waist, and a wide
> pear-shaped lower body with broad hips and thick thighs. Very short stubby arms. Tiny stumpy legs: her
> paw feet sit almost directly under her hips, and each leg is a short round stub barely longer than her
> paw. Big chunky paws, exaggerated proportions. Strongly animal-like: big upright pointed puppy ears with
> little flame tips, orange-red and cream fur everywhere, paw hands and paw feet, fluffy tail ending in a
> small flame. A cropped zip-up sports hoodie with short sleeves, hood down behind her head, in plain
> solid red, with no print, logo or pattern; no bottom clothing, fur covers the lower body with smooth,
> non-detailed anatomy. Nothing worn around the neck. Cute and cheerful. Single character only, full
> body, front view, T-pose with both arms straight out, plain white background, game character asset.

The previous (v16) Emberpup look is `art/concepts/v16/emberpup_s1.png`, 3D `assets/models/tests/emberpup_v16.glb`.
Stage 2 and 3 prompts name the form ("Blazehound, the evolved second form of a …") and add the
stage's changes to the species block; see `art/concepts/v16/` for the Emberpup set.

## Outfits (recommendation, 2026-10-31)

ZZZ pattern without the techwear/1990s street look (research: docs/research.md): one job uniform per
species line for shape, made from the element, plain solid colors, no print, logo, pattern, stripes or straps.
Stages add pieces to the same uniform. Prompt recipe: "[top] shaped like a chibi [job] uniform, made of
[element material], in plain solid colors with no print, logo or pattern".

| Species | Job uniform | Element twist |
|---|---|---|
| Emberpup | firefighter: cropped turnout jacket, chunky boots | ember-glow buckles |
| Mossback | construction crew: bib overalls, hard hat | moss overalls, shell-dome hat |
| Sparkwisp | rock stage idol: short stage jacket, flared mini skirt | lightning-bolt hem, spark buttons |
| Bloomling | nurse: short dress, cap | petal skirt, leaf cap |
| Gloomowl | detective: cropped trench, short cape | feather-edged cape, crescent buttons |
| Frostkit | figure skater: leotard dress, skates | ice-crystal skirt edge, blades on paws |
| Venomoth | lab chemist: cropped lab coat, goggles on head | moth-wing coat tails, lime vial belt |
| Pebblit | security guard: boxy jacket, cap | stone-plate shoulders, slate badge shape |
| Jellow | dessert-café maid: apron dress, headband | jelly frills, bubble buttons |
| Shadekit | stage magician / phantom thief: cropped tailcoat, top hat | smoky shadow coat tails |
| Sproutle | park ranger: short vest, ranger hat | leaf vest, acorn buttons |
| Cindermite | blacksmith: leather apron, heavy gloves | obsidian apron plates, glowing seams |

## Creature designs

Per species: what fills the species block, plus its expression. Stage lines say only what changes from stage 1;
the expression stays the same through all three stages.

### Emberpup / Blazehound / Infernus (melee, fire)
- **Expression:** energetic and confident: a cheeky smirk with a tiny fang.
- **Animal:** fire puppy. Puppy muzzle with a small black nose; big pointed ears with flame tips; fluffy tail ending in a flame.
- **Surface:** orange-red and cream fur. **Hair:** shoulder-length layered hair, flame-shaped spikes on top, ends flicking out, bangs over the brows; fiery orange-red with lighter yellow-orange flame streaks.
- **Top:** firefighter (see Outfits): cropped plain red turnout jacket, closed and fastened up to the collar, no stripes, bands or straps, glowing ember-orange buckles; chunky black-and-red firefighter boots (v21 f1). Earlier test: techwear bomber + sneaker boots (v21 z1/z2) (v16 model: orange crop top + tiny brown neckerchief).
- **Stage 2 Blazehound:** hair grows into a wild flaming mane over the shoulders, flames burst from both ears, small bronze shoulder guard.
- **Stage 3 Infernus:** long blazing hair turning to fire at the ends, deep crimson fur with glowing gold ember markings, obsidian-and-gold chest plate, large flaming tail.

### Mossback / Grovetortle / Elderwood (tank, earth)
- **Expression:** sleepy and content: drowsy half-closed eyes, a small relaxed smile.
- **Animal:** turtle. Rounded turtle beak-snout; small round ear-flaps; short thick tail.
- **Surface:** smooth green scaly skin; a big domed mossy shell on her back whose rim shows around the shoulders from the front.
- **Hair:** short mossy-green bob with leaf clips. **Accessory:** leaf headband; bark-brown crop top.
- **Stage 2 Grovetortle:** saplings and small flowers grow on the shell, bark bracers on the forearms.
- **Stage 3 Elderwood:** the shell is an ancient grove with a small tree, branch-like antlers in the hair, root-and-bark chest armor.

### Sparkwisp / Voltwisp / Stormheart (ranged, electric)
- **Expression:** hyper-excited: wide sparkly eyes, a big open grin.
- **Animal:** electric ferret. Small ferret muzzle; round ears; long zigzag tail with a spark at the tip.
- **Surface:** yellow and white fur. **Hair:** spiky yellow twin-tails with lightning-blue streaks.
- **Accessory:** copper goggles on the head, a small glowing spark orb clipped to each twin-tail; yellow crop top.
- **Stage 2 Voltwisp:** hair crackles with attached lightning, four spark orbs clipped in the hair, blue electric fur markings.
- **Stage 3 Stormheart:** storm-cloud crown attached to the head, long lightning mane, glowing blue eyes, storm-grey crop top with bolt patterns.

### Bloomling / Petalmend / Verdance (healer, flower)
- **Expression:** shy and sweet: blushing cheeks, a gentle closed-mouth smile.
- **Animal:** flower rabbit. Small bunny nose; long bunny ears with petal tips; puffball tail.
- **Surface:** pink and cream fur. **Hair:** soft pink wavy bob with a flower crown.
- **Accessory:** leaf armbands; pale green crop top.
- **Stage 2 Petalmend:** bigger blossoms in the hair, petal shawl over the shoulders.
- **Stage 3 Verdance:** radiant floral crown, long flowing pink hair woven with vines, petal cape attached at the shoulders.

### Gloomowl / Duskhoot / Nightseer (ranged, dusk)
- **Expression:** mysterious: calm narrowed eyes, a knowing half-smile.
- **Animal:** owl. Small hooked beak-muzzle; feathery ear tufts; fan of tail feathers.
- **Surface:** indigo and lavender plumage; forearms with wing-feather sleeves.
- **Hair:** layered dark purple hair with feather tips. **Accessory:** crescent-moon hairclip, indigo armbands; indigo crop top.
- **Stage 2 Duskhoot:** star-speckled feather sleeves, a feathered hood.
- **Stage 3 Nightseer:** large folded wings on the back, crescent-moon circlet, starry feather mantle.

### Frostkit / Frostfang / Glacierlord (melee, ice)
- **Expression:** cool and aloof: unimpressed half-lidded eyes, a flat little mouth.
- **Animal:** ice fox. Fox muzzle with a small nose; big pointed ears with frosty tips; huge fluffy tail with ice crystals.
- **Surface:** pale icy-blue and white fur. **Hair:** long icy-white side ponytail with pale blue streaks and frosty bangs.
- **Accessory:** snowflake hairclip, ice bracers; pale blue crop top.
- **Stage 2 Frostfang:** ice-crystal shoulder spikes, icicles hanging from the ponytail.
- **Stage 3 Glacierlord:** ice crown, crystal chest armor, a huge glacier tail.

### Venomoth / Toxwing / Plaguemoth (ranged, poison)
- **Expression:** mischievous: a playful wink with the tongue poking out.
- **Animal:** moth. Tiny muzzle; feathery moth antennae; small fluffy abdomen-tail.
- **Surface:** fuzzy lavender moth fluff with fluffy chest fluff; moth wings attached flat to the back, purple with green eyespots.
- **Hair:** lime-green fluffy bob. **Accessory:** lavender armbands; lavender crop top.
- **Stage 2 Toxwing:** larger wings with toxic swirl patterns, green-tipped antennae.
- **Stage 3 Plaguemoth:** huge dark purple and acid-green wings, mask-like markings around the eyes.

### Pebblit / Bouldron / Monolith (tank, stone)
- **Expression:** determined grump: furrowed brows, a puffed-cheek pout.
- **Animal:** stone armadillo. Short armadillo snout; small rounded ears; short plated tail.
- **Surface:** smooth grey stone skin with armadillo-like stone plates on the back and shoulders.
- **Hair:** short slate-grey bob with small crystal pins. **Accessory:** rope belt sash; grey crop top.
- **Stage 2 Bouldron:** bigger stone plates, boulder shoulder pads.
- **Stage 3 Monolith:** towering plated back with glowing blue runes, crystal crown.

### Jellow / Jellossus / Gelatitan (melee, jelly)
- **Expression:** goofy and happy: big round eyes, a wide open smile.
- **Animal:** jelly cat. Small cat nose; jelly cat ears; wobbly jelly tail.
- **Surface:** glossy translucent mint-teal jelly skin.
- **Hair:** a bob made of jelly droplets. **Accessory:** bubble hairclips, bubble armbands; teal crop top.
- **Stage 2 Jellossus:** bigger, with floating bubbles inside the body.
- **Stage 3 Gelatitan:** jelly crown, a softly glowing core in the chest.

### Shadekit / Umbracat / Voidpanther (melee, shadow, rare)
- **Expression:** sly: narrowed cat eyes, a wide Cheshire-cat grin.
- **Animal:** shadow cat. Small cat muzzle; tall cat ears; wispy shadow tail.
- **Surface:** black-purple fur. **Hair:** long black hair with a violet streak; glowing violet eyes.
- **Accessory:** moon-charm hairclip, dark violet armbands; dark violet crop top.
- **Stage 2 Umbracat:** shadow-wisp bracers on the forearms.
- **Stage 3 Voidpanther:** starry void patterns across the fur, shadow-flame mane.

### Sproutle / Fernguard / Mother Oak (healer, nature, rare)
- **Expression:** serene and motherly: soft closed-eye smile.
- **Animal:** fawn dryad. Small deer nose; fawn ears; short leafy tail.
- **Surface:** soft bark-brown fur with moss patches; small leafy antler-branches.
- **Hair:** leafy green hair with tiny flowers. **Accessory:** acorn hairpin, vine armbands; moss-green crop top.
- **Stage 2 Fernguard:** fern cape attached at the shoulders, bigger antler-branches.
- **Stage 3 Mother Oak:** large branching antlers with blossoms, bark chest armor, long vine hair.

### Cindermite / Magmite / Volcanox (ranged, lava, rare)
- **Expression:** cocky and fiery: one eye squinted, a toothy grin.
- **Animal:** lava beetle. Small mandible-muzzle; beetle antennae; short armored tail.
- **Surface:** glossy black carapace plates with glowing orange lava cracks.
- **Hair:** dark red hair with ember-glowing tips. **Accessory:** obsidian shard earrings, obsidian bracers; charcoal crop top.
- **Stage 2 Magmite:** a small horn on the forehead, brighter lava cracks.
- **Stage 3 Volcanox:** a volcano-shaped horn crown glowing with lava, molten shoulder plates.

## Enemies and bosses (proposal, not yet generated)

Same smooth low-poly, chunky look, but **spooky-cute monsters**, not monster girls, so they read as the
other side at a glance. Humanoid ones (skeleton, archer, cultist, wraith, Bone King, Warlord, Lich) get
rigged and share the animations; the others animate in code.

- **Cave Bat:** round fuzzy bat, huge ears, tiny fangs, wings spread.
- **Skeleton:** big-skulled chunky skeleton with a rusty sword and round shield (pilot model, older style).
- **Gloop:** green slime blob with a goofy face.
- **Goblin Archer:** small green goblin, oversized hood, short bow.
- **Crypt Spider:** round purple spider with many eyes and stubby legs.
- **Cultist:** hooded red robe, glowing eyes in the hood shadow, small staff.
- **Stone Golem:** blocky boulder golem with mossy shoulders and a glowing core.
- **Wraith:** pale blue hooded ghost with trailing tatters.
- **Mimic:** treasure chest with a tongue and teeth.
- **The Bone King:** giant skeleton with a crown and a bone cape.
- **Gloop Matriarch:** huge slime with a crown and smaller slimes inside.
- **Goblin Warlord:** big armored goblin with a war banner on the back.
- **Hollow Lich:** tall floating robed skeleton with a glowing staff.

## Asset status

| Asset | State |
|---|---|
| All 12 species × 3 stages (36 models) | **v16 style**, rigged, in `assets/models/creatures/<id>_s<N>_rigged.glb`; concepts in `art/concepts/v16/` |
| Old-style creature models (pilot/chunk 1) | Moved to `assets/models/legacy/<id>_s<N>_rigged_v1.glb` |
| Skeleton | In game, old style |
| Enemies, bosses | Not generated (proposal above) |

Rollout notes (2026-10-30): prompts were built from the style/species/framing blocks with "Nothing worn around
the neck" appended. One regeneration (Venomoth s1 came out with purple hair; stage line needs lime). Meshy's queue
holds about 10 pending tasks; submit in waves. Rig heights were 1.0 / 1.25 / 1.5 m (tanks Mossback, Pebblit ×1.08); now 1.0 m for every stage.
