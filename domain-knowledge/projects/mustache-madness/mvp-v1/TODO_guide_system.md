# TODO: guide tip system

Event-driven guide shipped: `GuideBus` (server game-state event bus) → `GuideDirector`
(pure primary/secondary policy) → `TutorialGuide` (view on the frog). See
the guide code (`systems/guide/`).

Remaining:

- **Remote-peer view replication.** The `TutorialGuide` view is still added server-side
  only (as before this change), so on a listen-server only the HOST sees the bubble.
  The game-state logic is already server-authoritative + identical for all, but remote
  clients render nothing. To fix: replicate a `guide_line` string to every peer and
  spawn the view on all peers (e.g. a replicated `is_guide` flag on the guide creature,
  each peer adds the view + a MultiplayerSynchronizer(auth=1) on `guide_line`, mirroring
  how `Crop` adds its sync in `_ready`). Deferred: MP is not live-tested and singleplayer
  (host) is the primary path.
