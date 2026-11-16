# LAW: creature state (what kind it is, how it shows)

Run this rule on every creature state before it is built (user, 2026-10-15). It answers
"hidden, bar, card or sign?" the same way every time, because each question is a code
fact. Pillars: "a black box with a clear interface" and "ban hidden effects" (`MEMORY.md`).
Needs and beds: `docs/LAW_beds.md`.

"Visible or hidden" is not a kind of state; it is how a state is displayed. A sign is
never a state of its own: it is a view onto one (a bar, a glyph, the mustache curl, a
pose).

## Step 1: what is it? (ask in order, first yes wins)
| # | Question (a code fact) | Kind | Examples |
|---|---|---|---|
| 0 | Is it a want defined as the lack of an outcome ("has not had fun", "is not happy")? | **Banned.** Redefine it as a stock with its own drain and a direct filler, or drop it | - |
| 1 | Does an engine step, path or action-in-progress own it, with no meaning to the player? | Plumbing | motor, roam, combo, intent |
| 2 | Is it authored per species, or fixed for the whole run? | Static | species base stats, personality mean |
| 3 | Is it a stock that drains on its own clock and that a placed thing fills directly? | Need | hunger, sleep, fun |
| 4 | Is it a stock with no clock of its own: events push it down, care fills it, and it stays where they leave it? | Health | HP |
| 5 | Does an event start it, and does it end on a timer or a world act? | Effect | ate, meal, dawn, cozy, drink, hangover, grief, stun, groggy, tipsy, down, jailed, rampage, carried |
| 6 | Is it grown by raising over days, or rolled once, and kept? | Raised | stats, personality, friendship, love |
| 7 | Otherwise: only other states write it (derived now, or a slow sum of them). | Inner variable | mood, mood history, belonging, energy |

Why this order: each early question is the narrower one. A need is a stock with a clock,
so it is asked before health; health is also moved by events, so it is asked before
effect; a need is also a stock, so it is asked before inner variable. Question 0 runs
first because it is the pillar's ban.

**Grief's size:** its amount is a lifelong best friend's, scaled down by friendship x
familiarity, so a stranger's death barely registers.

**One effect kind (user, 2026-10-18).** A mood-only event mark and a behavior-changing one
are the same kind: an event starts it and a timer or a world act ends it. What it changes
(mood, behavior, or both) decides only how it shows (step 2), not what it is. In the code,
a timed effect is one `Effect` in `Creature.effects`, authored in `CreatureConfig.EFFECTS`.

**Mood is the box's output, not a need (user).** It is an inner variable: the headline
answer to "how are they doing?". A want may read it (user, 2026-10-19): question 0 still
bans a need for happiness, and a pull that reads mood starts only with a sign the player
sees ("Ban hidden effects").

## Step 2: how is it displayed?
Each channel carries one meaning, so the channel itself tells the player what kind of
thing they see before they read it. A kind never borrows another kind's channel.

| Channel | It means | Carries |
|---|---|---|
| **Flash:** a glyph pops over the head, then fades | "this just happened" | an effect landing, a social outcome |
| **Head glyph:** the one glyph that stays over the head | "this is what it does", or in a 💭 "this is what it wants and cannot reach" | the act in progress (plumbing with meaning: most acts have no animation), a need's wish |
| **Emanata:** cartoon marks that move on or around the body (stars, sweat drops, puffs) | "this changes how it acts" | an effect that changes behavior; an inner variable that warns of an output the player can still prevent |
| **Body:** shape, pose and the mustache | "who it is, and how it is overall" | mood (the curl), raised (mustache size and hue, packs), a pose (down, in bed) |
| **Bar** | "refill this in time" | health |
| **Inspector** (aim readout) | "everything, with numbers" | bars on the left, one card per active effect on the right |

| Kind | World | Inspector |
|---|---|---|
| Need | Every need: the **wish** (a balloon with its icon, white) in the head glyph when it wants a fix it cannot reach: only while no place that fills that need has a free spot it would walk to (user: it can go, no balloon). **Red means a consequence is coming, shown before it happens (user):** hunger and sleep turn red `WARN_SEC` before 0 (sleep at its working drain) when, now, it could not meet the need the normal way (no food anywhere; no usable bed), and mood turns red with the cure seat (🪑) in it while it brews with no free seat it would walk to (the puffs stay the snap warning). One balloon, in every mode; priority brewing, hunger, sleep, except that a tired creature (which cannot snap) shows its need first. Fun stays white: its 0 only makes it bored. No need bars in the world (user) | Fun bar; the bed line |
| Health | A **bar** | Bar |
| Effect | A **flash** when it lands. If it changes behavior, also **emanata or a pose for as long as it lasts**: an effect with no sign is a hidden effect | A **card** while it lasts: glyph, name, time left, what it changes |
| Raised | **On the body**, named in the inspector | Named |
| Inner variable | A **body sign** if it is the headline output (mood: the curl); **emanata** if it warns of a preventable output (mood history: puffs while it brews, thicker as the hold nears the snap); otherwise **hidden**, because its inputs already show | Bar |
| Plumbing, static | Nothing, except the act in progress in the head glyph (static species data shows as the species' look) | The act as a line |

Why: the player gets a bar only for health; a need they must meet in time (build food,
build beds) warns with its red balloon before the consequence. Everything else shows as the
act itself, a body change, or a glyph at the moment it matters. A mood-only effect needs no lasting world sign: its flash
says it landed, the curl shows its sum, and its card names it. An effect of a state must
show somewhere: a hidden value with an effect needs a sign on what does show (energy: the red
balloon warns before work stops). A gauge never takes a glyph in the world: a glyph
reads as an event or an act, never as a level.

The inspector may show any state with its number. It is a readout for whoever looks,
never needed to play.

## Why these kinds
- **Need:** the only state the player times an input against. A placed thing fills it, so
  the fix is always a build.
- **Health:** the body's damage. Harm and care move it, so it is the one stock that tells
  what the world did to a creature.
- **Effect:** the only way one event leaves a mark that lasts. One kind for every mark keeps
  one life cycle (start, timer or world act, end) and one card.
- **Raised:** what raising buys, kept for life. It shows on the body because it is who the
  creature is.
- **Inner variable:** what the box computes from the rest. It shows only when it is the
  answer (mood) or a warning (the puffs); otherwise its inputs already show.
- **Plumbing, static:** engine work and authored data. Nothing for the player to read.

## How the field does it
Colony and life sims split state about the same way: meters (needs), timed event marks
summed into mood (The Sims' moodlets, RimWorld's and Dwarf Fortress's thoughts), an
aggregate mood or stress with a breaking point, and permanent traits. They differ on
display:
- **One aggregate glyph** (The Sims' plumbob color): hides the cause. Players ask where a
  moodlet came from. Here the curl is the aggregate and the cards give the cause.
- **Icons over the head that cycle** (Dwarf Fortress status icons): two states at once hide
  each other. Here each kind has its own channel, so nothing cycles.
- **A panel split by kind** (RimWorld needs and health tabs, ONI status, Planet Coaster
  guests): detail on demand. Here that is the inspector, never needed to play.
- **A buff bar** (MMO icons with timer sweeps): clutters at scale. Here it lives only in the
  inspector, never over every head.
- **Cartoon emanata** (comics' sweat drops and seeing stars, Animal Crossing's reaction
  marks): reads at a glance and fits the tone, but shows no number or timer. Here the card
  holds the number.
- **Three reads** (Zach Gage, GDC 2018): the first read is the glanceable essential, detail
  comes on the second and third. World channels are the first read; the inspector is the
  rest.

Sources: [Sims plumbob](https://sims.fandom.com/wiki/Plumbob),
[an untraceable moodlet](https://forums.ea.com/idea/the-sims-4-bug-reports-en/sim-has-grouch-moodlet-without-grouch-trait/12395224),
[RimWorld mood](https://rimworldwiki.com/wiki/Mood),
[DF status icons](https://dwarffortresswiki.org/index.php/Status_icon),
[ONI duplicant profile](https://www.gamepressure.com/oxygen-not-included/profile/z59d44),
[Planet Coaster guests](https://planetcoaster.com/player-guides/guests),
[Lexicon of Comicana](https://en.wikipedia.org/wiki/The_Lexicon_of_Comicana),
[Animal Crossing emotions](https://nookipedia.com/wiki/Emotions),
[Three reads](https://rymdkraftverk.itch.io/tails/devlog/86052/applying-zach-gages-three-reads-to-our-ui).

## Rejected (do not re-propose)
- A bar for every need (The Sims): per-unit tracking at herd scale.
- Stages (RimWorld's warm, tipsy, drunk) and hidden tolerance or addiction: a memorization
  table and a hidden effect. One effect per state.
- A number for stress in the world (Oxygen Not Included): mood history shows there only as
  emanata.
- Sorting by "which player question it answers": one state answers two (grief is both
  "what did that" and "how are they").
- A row of typed slots over every head (activity, mood, effects): clutter at herd scale and
  a HUD, not natural on sight.
- One slot that cycles through the states: two states at once hide each other.
- A tint per effect: one hue channel, and the mustache hue already carries raised.
