# TODO — Standing-Clock / map-growth backlog

Pending work after the time-dilation clock + map-growth ship. Detail:
`docs/LAW_time_dilation.md`.

Status swept 2026-08-29: axe targeting + crank-depth shipped; remaining items are
live-gated (2-peer / playtest tuning) or cosmetic. MP crank-authority + map-growth
late-join shipped but need a 2-peer live confirm.

## Live-gated (need a real session — cannot verify headless)
- [ ] **Clock value & balance pass** — tune `CRANK_MAX_SEC` (25), `CRANK_WIND_RATIO` (5),
      `factor` (2×), `radius` (8), look cone (0.84) against actual play; where the clock sits in
      the chaos draft economy.
- [ ] **Creature-only knockback feel** — impulse ×s + hold ×s on CharacterBody; verify in play.
- [x] **Crank authority in MP — DONE (2026-08-29, needs 2-peer live confirm).** `ClockZone` now
      server-authoritative: non-server peers RPC their crank edge (`_report_crank`); the server ORs
      all votes (host + `_crank_peers`), owns `_charge`/`_active`/`_charge_rate`, and replicates via
      `_sync_clock` (on the active flip + every 3rd frame). Singleplayer unchanged (server = only
      peer, no RPCs). Stale votes dropped on `peer_disconnected`.
- [x] **Map-growth late-join — DONE (2026-08-29, needs 2-peer live confirm).** `game.gd._on_peer_joined`
      `rpc_id`s the grow-count (`_crop_respawns`) to the newcomer, which replays `grow_by` in one
      deterministic step (`_net_catch_up_growth`). Chunked seeding is map-size independent, so one
      catch-up grow == the N incremental grows.

## Won't-fix (documented)
- Station (well/tent) knockback dilation — RigidBody global gravity can't be arc-corrected.
- Charging-station scan poll (0.15 s) — cosmetic, stays real-time.

## Cosmetic / deferred (low value)
- [ ] **Cog facing** — cog sits on one body face; reads backward from the far side. Crank already
      works from any approach within the look cone, so this is a pure tell. Mirror the cog to both
      faces or make it radial if it bugs you.
- [ ] Richer crank feedback (sound, particle, HUD charge meter) beyond the sphere-alpha tell.
- [ ] Prune debug/tuning consts once values settle.
