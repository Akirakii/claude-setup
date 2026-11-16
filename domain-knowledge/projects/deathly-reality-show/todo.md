# Todo (each with a recommendation)

- **Playtest v2 with 3–6 people.** The only real check. Watch: does Switchboard make everyone shout
  and listen, or does one person run it? In The Tilt, do people describe keys by the landmarks?
  Rec: play both before adding anything.
- **Bots cheat** (they read orders and keys from the state). They prove rules and netcode, never
  difficulty. Rec: never tune from bot runs; tune from the playtest and `tools/switchboard_check.py`.
- **The Tilt alone is near-impossible** (on purpose: dying must never help). Rec: watch whether
  lone survivors feel cheated.
- **Voice load at 6** (6 orders or 6 key descriptions at once). Rec: if it's noise, 3 Tilt waves
  and orders in flight = min(N, 5) at N ≥ 5.
- **Switchboard: holder steers the puller** (gate 7 weak). Rec: watch; if the holder just reads
  their own lever from the rim, make your own lever's plate unreadable to you too.
- **Positions are client-reported** (a modified client could cheat). Rec: fine for friends; host
  speed cap before any public release.
- **Lag:** kills are judged on the host. Rec: test over Tailscale.
- **Tilt key generation** can take ~0.1 s at 6 (rejection sampling). Rec: if it hitches, generate
  the next wave during the current one.
- **The Reaper is static.** Rec: Meshy auto-rig for gestures.
- **Export templates 4.7.2** missing (build.md).
