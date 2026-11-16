# TODO: needs bundles

The user picked all 9 needs-visibility proposals on 2026-10-15 (options 4b, 5b; 8c was an
AFK pick in that blanket yes, and the user reversed it on 2026-10-18: mood buffs every stat
±3). Proposal 1 is `docs/LAW_creature_state.md`; leisure (4b, 2b, 3b, 9) and signs (6) are
built, and drunk (5b) landed in #282; 7 (the tired tick) was dropped with the 0.2 line (user: 0 is the stop). This file holds the state display leftovers.

## Facts the bundles build on
- The free-time chooser: `OfferPlace.want` in `entities/builds/places/offer_place.gd`,
  `g = 0.5`; a place must beat `ROAM_PULL = 0.3`.
- Leisure want (fire, bar, seat): `FUN_GAIN x (1 - fun) x lean`, lean `1 + g x sociability`
  (fire, bar) or `1 - g x sociability` (seat). Fun drains `0.002/s` free and awake, `+0.008/s`
  working, fills `0.01` per use (1 s) where the place keeps it.
- Mood history follows the value over `HISTORY_SEC` 60 s; a brewing creature wants the
  comfort seat by `CURE_GAIN x strain`; one puff, three from strain 0.75.

## State display leftovers (`docs/LAW_creature_state.md` step 2)
- [ ] The wish (💭) PR: hunger's icon shows the need (🍎) while sleep and fun show the place
  (🛏 🍺 🔥 🛋), and hunger and sleep fire at empty while fun fires while low. Candidate:
  every wish is 💭 + the place that fixes it, from one "wants a fix it cannot reach" test.
- [ ] Grief has no lasting world sign now (flash, curl, card). If the playtest misses it,
  add it as marks (a rain cloud), not the head glyph.
