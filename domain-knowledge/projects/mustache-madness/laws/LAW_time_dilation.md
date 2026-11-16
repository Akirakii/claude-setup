# Law: time dilation (what runs on local time)

The Standing-Clock station (`entities/machines/clock_zone/`) speeds up LOCAL time inside a
zone. This is the standing law for which code honors it; `/rate` item 7 checks new sites
against the registry below.

## Primitives
- `LocalClock` (`components/local_clock.gd`): per-entity dilated time. `advance()` reads
  `TimeField.scale_at(pos)` each frame and accumulates `time` at that rate.
- `TimeField.scale_at(pos)` (`systems/engine/time_field.gd`): the composed rate at a world
  point (1.0 outside zones; overlapping zones STACK multiplicatively, two ×2 = ×4).
  It has no floor: it is >= 1 only because every `ClockZone.factor` is >= 1. A factor of 0
  would freeze a clock, and a window armed on it (a care or class window) would never close.
- `Cooldown` (`components/cooldown.gd`): a one-shot window on a `LocalClock`.
- `Effect` (`entities/creatures/components/effect.gd`): a creature effect, ending at a time on its `LocalClock`.

## The law
- Any rate, duration, cooldown, or accumulator a player experiences runs on `LocalClock` /
  `TimeField`, never raw `delta` / `GameTime`. Wall-clock features silently ignore zones.
- Physics scales s/s²: speeds and impulses ×s, acceleration and gravity ×s² (same arc,
  s× faster, not heavier).
- Real time stays real: input debounce, logging (`RateLimiter`), UI, network, target TTL.
- Global pacing (day/night, wave spawn pacing, `Engine.time_scale`) is not per-zone.

## Site registry (keep current when time code changes)
**Dilated:**
- Player: move / accel / friction, jump + gravity, axe swing + cooldown, watering rate,
  place / drop rate, throw wind-up.
- Creature: move / attack / roam, animation speed, gravity + navlink launch, downed rot +
  blink, every effect (groggy, throw stun, tipsy, the mood effects), the hiccup, breeding night grace, eat delay, baby maturation,
  hunger, sleep and fun (their red lead and the starve wait too), knockback launch + hold, regen and the medic-bed recovery bar, a medic's
  care window (on the medic's clock), a teacher's class window at a chalkboard (on the
  teacher's clock), stat idle floor, social edge decay + pair cooldown, mood
  drift, jail time-out, an heir's claim, a food thief's walk and eat wait, chop felling time (on the chopper's clock), a mine's strike time (on the miner's clock), mood
  history and the puffs (brewing, its count and its rest), the
  rampage and its punch pace, a ladder wild's climb time (`LADDER_CLIMB_SEC`, on the punch's
  dilated dt).
- Rail: a train's ride and dwell (on the cart's own clock, at the cart).
- Crop: growth + drying. Items: dropped bob + pickup. Grid: yeet arc.
- Stations / world: transformer cook, water-droplet flight (×s velocity,
  ×s² gravity), stat-station training, a leisure place's fun fill and the dine seat's meal (a chair), the bar's drink and seated chats, job labor interval (chop, cook),
  a station's paid time (`Wage`, on the station's clock), a site's undo window (on its sign's clock), a lectern student's schooling (on the place's clock).

**Not dilated (intentional):** day/night cycle (and the hangover, counted in dawns), wave spawn pacing, `Engine.time_scale` +
`GameTime`, `RateLimiter`, target aggro TTL, balance probe (stamps game time, `GameTime.total_time`, so rates hold under fast-forward), HUD `_process`, nav
coordinator, world wrap, job board matching poll. **Won't fix:** a RigidBody station's knockback uses global gravity,
so its arc can't be dilated.
