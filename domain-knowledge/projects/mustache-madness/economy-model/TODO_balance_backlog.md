# TODO — Balance backlog

Carried over from the retired calibration/rebuild handoffs (2026-07-19).

## Next: wage and bank (user, 2026-10-17)
- Banker uptime: the bank cheat in a 300 s idle sim grows 2 gems at 10 or 1,000 locked, so
  its banker works about 40 of 300 s. Find where the rest goes.
- Check the 60 s gem (`Wage.GEM_SEC`) against job pace in a playtest.

## Next playtest checklist (first run of the tick+event toolkit)
- 10+ nights with `DebugConfig.probe_log` on → `node util/probe/extract_playtest.js`.
- Verify the stream lands: `BALANCE_TICK` every ~2s with `phase=` flipping,
  `BALANCE_EV` spawn/feed/death rows with origins, and — since the config
  fix — a `BALANCE_CONFIG` line on the FIRST tick (report `config:` non-null,
  no longer dropped by `_ready`-timing). Report shows a populated `per_day`
  table, `cohorts` per-cycle arrays, and a `currency` block.
- Verify in-game feel (from PR #158, still unmeasured): AOE knockback 80/20
  split (big CC nerf vs old full-force), crops bouncing off the well don't
  soft-lock the poop-goal loop, `BalancePanel` renders (fw_real row only).
- Bunny anti-frog buff (dmg 5→7, rates halved) was shipped UNMEASURED —
  judge from the b→g / g→b duel sparklines and bunny dmg/unit-night.

## Social (Phase 9)
Tuning accepted as shipped (2026-10-01); no open numeric targets.
- Feel still unverified in play: turn share, gathering arcs, how fumbles read.

## Standing watch items
- PROC bypass audit: poop reward pool (3/4 processed) may bypass the favorite-food gate.
  **Evidence-gated (2026-08-29):** suspected balance leak, NOT a confirmed bug — no code fix
  without a measured capture. Confirm/deny from a 10-night `probe_log` run (poop income vs
  favorite-feed counts) before touching the gate.
- Swarm dominance: watch `entropy` in captures.
- ~~`level_04/05_waves.tres` old difficulty scores~~ — STALE: PR #184 trimmed to a single level
  (level_02). Dead unless multi-level returns.

## Docs
- Fold shipped balance outcomes into the creature code (`entities/creatures/`) /
  the crop code (`entities/crops/`) (IMPL docs retired).

## Breeding (measured 2026-10-09, turtle bot, 10-creature start, 600 s, 2 seeds)
- Superseded 2026-10-18 by the dusk roll (`docs/LAW_life.md` rule 5): every species lays
  2.2-2.6 eggs per finished life (active bot, 2400 s). Beds no longer bound it (user: a
  creature with no Bed breeds and only stays tired), so the herd again grows without a limit.
  Watch herd size and frame time in a long playtest.
- The probe's rescue split by carrier (`rescued_<by>` keys, `rescues:` block) has no chart
  on the hosted page yet.

## Wave ramp (measured 2026-10-09, 3 seeds, 600 s, `SCALE_STEP_AMOUNT`)
| Step | idle | turtle | active |
|---|---|---|---|
| 1.5 (was) | falls n7-8 | survives, statue >= 0.82 | survives, statue >= 0.91 |
| 2.25 | falls n7-8 | survives, 0.79 | survives, 0.94 |
| 2.6 (now) | falls n7-8 | falls n10 in 2 of 3 | survives, 0.89 |
| 3.0 | falls n7 | falls n9-13 | falls n10-11 |
The curve has a cliff: a herd that clears the night-6 spike recruits ahead of the waves.

