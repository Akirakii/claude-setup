# TODO: gem income (AFK run, started 2026-10-25)

User: "lets proceed and design the implementation and then the design code and implement
afterwards, all afk, one pr and merged all updates into main". Design: `docs/BRAINSTORM_gem_income.md`.
AFK: Claude closes every gate; every pick below is Claude's, not "(user)". hypridle on the AFK
config (restore `pkill -x hypridle; setsid -f hypridle` at the end).

## Tasks (one per phrase of the request)
- [x] 1. Design the implementation (/design-idea SPECIFY: rules, numbers, data dictionary, loops)
- [x] 2. Design the code (/design-code)
- [x] 3. Implement (tests, cheat key `/gembush`, probe `bush_gems` + `bushes`, sim `SIM_BUSHES=1`)
- [x] 4. Verify (touched tests, one full suite, a care sim)
- [x] 5. One PR (#371) with all pending updates (econ stack C1-C2 + B1-B3 + A1-A2, this session's balance
      tuning, the gem probe, the skills/CLAUDE.md rewrite in the working tree, docs), merged to main
- [x] 6. Restore hypridle, final report

## Gate log (Claude's picks)
- Design: gem bush = a perennial crop the player builds (💎 3), farmer shakes 2 gems onto the
  ground per ripe bush, it regrows. Night bounty 3 kill gems. Sign cap 4 gems. Claude.
- Payout look: plain gems popping out of the bush now; gem-crop poop deferred (needs a poop
  system the game no longer has). Claude.
- Harvested gems go on the ground, not into the farmer's bag: a carried gem would walk to a due
  sign by itself (creature delivery pays signs), a loop that funds signs without the player. Claude.
- Code structure (/design-code): (A) a `regrows` flag on CropMetadata, one branch in
  `Crop.harvest` [chosen: reuses crop growth, job posting, rings, save, visuals]; (B) a new
  GemBush GridObject [rejected: duplicates crop growth and job code]; (C) a gem-mine Station
  with its own sign [rejected: a second paid piece per farm, new verb]. Claude.
- Tests run 1: 104/106 on 12 files; the 2 failures asserted the old rules (no sign cap, menu
  order without Gem Bush): updated, rerunning.
- Sim bot: `SIM_BUSHES=1` reinvests spare gems above a 4-gem reserve into gem bushes at dawn;
  the active bot already shakes ripe crops at dawn and picks up the gems. Claude.
- Found in review: a player's sweep on a ripe crop yeets it, so it would have destroyed a ripe
  bush. Fix: the player-hit handler shakes a ripe bush (harvest) instead; wild punches and a
  piece built over it still remove it. Test added. Claude.
- Commit plan for the one PR (branch feat/econ-food-theft, on top of the 8 stack commits):
  chore(skills) for the working-tree skills/CLAUDE.md rewrite; feat(balance); feat(economy) gem
  income; docs. Squash-merge (GitHub Actions blocked by billing: local full suite is the gate).
- Sim with bushes done (numbers in BRAINSTORM_gem_income.md "Measured after the build"): bounty
  holds, surplus gone, early ramp slow. Left as is for the user's playtest (tuning, not design).
- Full local suite: running.
