# Roadmap (2026-11-03)

The user wants to ship in a month (user, 2026-11-03: "i want to ship this game in a month"). The
market research (`~/Playground/game-design-research/reports/playbook.html`) says a surprise launch with no
audience usually fails, so the month ships a **public demo and store page**, and the Early Access
launch follows February Next Fest (user, 2026-11-03: "lets record the plan").

This file holds the shape only: dates, gates, marketing. What goes into the game is experimental
and lives in the design docs (`docs/core-design.md` lists them); a feature enters the demo only
after a playtest earns it.
Each step ends with a "done when" check; if it fails, cut scope, don't slip the date.

## Dates that drive everything
- Steam Direct fee: pay at once. Third-party guides report a 21–30 day wait before release; Valve's
  fee page doesn't mention one (checked 2026-11-03). If it applies, paying Nov 3 makes Dec 3 the
  earliest release.
- Store page: submit ≥7 business days before it should go live; a new product's Coming Soon page
  must be up ≥2 weeks before release (Valve, checked 2026-11-03). Whether the 2-week rule covers a
  demo: not checked.
- Store page checklist: AI-content disclosure (assets are AI-made), trademark search for the name.
- Next Fest Feb 2027: **Feb 22 – Mar 1**; register by **Jan 10**; required items reviewed by
  **Feb 8** (Steamworks). A demo can join only one Next Fest.
- Playbook targets: demo live ~3 weeks before Next Fest; Popular Upcoming needs ~5–7k wishlists;
  launch at $5–10 with a 20–40% launch discount. Price rec: $7.99, ~$5 launch week (`docs/questions.md`).
- Wishlist checkpoints (estimates scaled back from the playbook target): **~1k by Dec 15,
  ~2.5k by Jan 10, ~5k by Feb 22.** Missing one means the marketing changes, not the dates.

## Month 1 (Nov 3 – Dec 3): the demo
Target, not a promise: one store-page rejection eats the slack. The demo is the core room; anything
experimental stays out unless a playtest shows it is fun, so the full game keeps its surprises.

**Week 1 (Nov 3–9): prove the fun, start the clocks**
- Commit the current work.
- Playtest with friends (Tailscale), **recorded with voices**; log laughs, silences, questions.
- Fix the top 3 problems the playtest shows.
- First clips: the best 15-second moments to TikTok.
- Steam: pay the fee; store page (art, logo, 5+ screenshots, checklist above), submitted by Nov 7.
- **Done when:** friends asked for another run; the store page is submitted.
- **Gate:** if the core room isn't fun yet, Weeks 2–3 fix it; nothing new is added.

**Week 2 (Nov 10–16): online works, read the rival**
- Steam end to end: 4 friends from home, with a second Steam account on another machine.
- Lag test with `tc netem` (100–200 ms); fix desync.
- Fixes from the Week 1 playtest.
- **Rival:** Don't Press This Sh*t (co-op button room) launches Nov 11; read its players and
  reviews, then sharpen the store page and clips against it.
- **Done when:** a 4-player Steam session runs from home without desync.

**Week 3 (Nov 17–23): the demo is fun from the first run**
- Online playtest #2 with friends who haven't played.
- Fix what they hit; settings menu; audio pass.
- Store page live (Coming Soon); more clips from the playtests.
- **Done when:** a fresh crew laughs within 5 minutes without being told what to do.

**Week 4 (Nov 24 – Dec 3): ship the demo**
- Bug fixing only. Demo build submitted to Steam, public demo live.
- Trailer cut like a streamer clip, with real voice reactions. Open a Discord.
- **Done when:** the demo is public and the store page collects wishlists.

## Dec – Feb: grow the audience, build the full game
- Creators: send the demo to 100–600 small and mid creators, a few big ones.
- Clips every week from playtests and creator videos.
- Build the full game from what playtests and demo feedback prove (design docs decide what).
- Update the demo from feedback; watch demo players at once (the playbook: launch ≈ 3× demo peak).
  The Winter Sale (about mid-Dec to early Jan, not checked) makes visibility hard: don't judge the
  demo's peak from December.
- **Jan 10:** register for Next Fest. **~Feb 1:** demo at its best, live 3 weeks before.
  **Feb 8:** required items reviewed.
- **Done when:** the wishlist checkpoints above are met.

## Feb 22 – Mar 1: Next Fest, then Early Access (~March 2027)
- Next Fest with the demo; streams during the fest.
- Early Access launch after the fest, $5–10 with a launch discount; big creators get keys
  weeks ahead; voice reporting and moderation ready.

## After launch
Content updates on a fast cadence; what they contain comes from the design docs and player data.
