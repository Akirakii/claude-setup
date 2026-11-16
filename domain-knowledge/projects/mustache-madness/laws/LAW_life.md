# LAW: lifespan, stat caps, and species identity

Standing law for how long a creature lives and how strong it may grow. User decisions are
tagged (user).

## Rules
1. **A lifespan per creature (user).** Each species has a base in days; each creature rolls
   ±`LIFE_SPREAD` (20%) around it at birth. A hatchling starts at age 0; any other creature
   (the starting herd, a boat arrival) starts up to `START_AGE_MAX` (30%) into its life. Allies
   age on the game clock; wilds do not.
2. **Its last day shows (user):** a grey mustache and `OLD_SPEED_MULT` (0.8) walk.
3. **A goofy farewell, not a grim death (user).** When its time is up it shows 😇, floats up
   `FAREWELL_RISE` m over `FAREWELL_SEC` and is gone. Its bag drops; every friend familiar
   with it gets the light `farewell` moodlet (🥲); no grief.
4. **Stat caps per creature (user).** Each stat stops at a cap: the species' cap rolled
   ±`CAP_SPREAD` (15%), or for a hatchling its parents' mean cap plus a roll from
   `CAP_DRIFT_MIN` to `CAP_DRIFT_MAX` (-1 to +3), so families drift stronger. At its cap a
   stat banks no more XP.
5. **PRE-PILLAR (unconfirmed): the herd replaces itself at base.** Every species' mean lifetime
   eggs per creature is at least 2.1 (each egg counts for both parents, so 2 replaces the
   herd; the 0.1 covers lives cut short). The one trigger: at each dusk every free adult pairs
   with its mate and the couple rolls once. Its first chance is `BREED_PACE` over its
   species' `lifespan_days`, scaled by the couple's mutual love from `BREED_LOVELESS` to
   `BREED_LOVED` (user: love, not mood, drives births; about 2.1 eggs per life with no love, and
   full love well above replacement so care grows the herd, user 2026-10-25), at most 1, so a short life breeds fast and a long one slow; each
   egg the busier parent has laid multiplies it by `BREED_CHILD_FALLOFF`, so a family levels
   off near the same size in every species, and a creature that found a mate late still
   catches up. Its mate is its love when the love is returned, else the kin it likes best
   among those that don't dislike it (a stranger will do). No rest between eggs.
6. **A creature with no Bed still breeds (user).** Its cost is sleep, not family: it stays
   tired and unproductive until it is housed (`docs/LAW_beds.md` rule 7). The probe measures
   rule 5 (`fertility` in the report: generations hatched, eggs per finished life vs running
   ones, `kids_housed` for lives that had a bed at half their dusks or more, the herd's
   last-day share per third of the run, and the egg funnel from dusk rolls to eggs laid).

7. **New species come by boat, never by taming (user).** A downed beast never takes a bed
   and a bed never mends one. A pier calls a boat at dawn while two beds stand free; its
   pair of one friendly species steps off and takes them (`Housing.vacancies` -2). Births
   stay free of beds (rule 6). The old taming inflow (playtest 2: 47 recruits in 5 waves)
   is gone; how fast boats plus breeding grow the herd is a balance question.

## Species identity (user)
| Species | Identity | Life | Start STR/VIT/DEX/INT | Cap STR/VIT/DEX/INT | Also |
|---|---|---|---|---|---|
| Fox | all-round | 10 d | 6/6/7/6 | 24/24/26/24 | |
| Bunny | fragile, breeds fast | 8 d | 3/3/7/5 | 12/14/28/20 | 45 HP |
| Frog | tank, grumpy, breeds slow | 12 d | 5/9/4/6 | 18/34/16/22 | 180 HP; warmth -0.7 |
| Owl | smart | 14 d | 3/4/6/13 | 14/18/22/38 | |
| Hedgehog | attack | 9 d | 11/6/5/3 | 34/22/18/14 | |

## Data
| Name | Type, range | Owner | Lifecycle |
|---|---|---|---|
| `lifespan_days`, `stat_caps` | float, 4 ints | CreatureMetadata (species) | authored |
| `age`, `span`, `caps` | dilated s, dilated s, 4 ints | LifeComponent (per creature) | rolled once, saved; age grows on the clock |
| `eggs_laid` | int >= 0 | BreedComponent (per creature) | +1 per egg it parents, saved, never reset |
| `BREED_PACE`, `BREED_CHILD_FALLOFF` | float, float in (0, 1) | CreatureConfig | weights: first chance x lifespan in days; the cut per egg laid |
