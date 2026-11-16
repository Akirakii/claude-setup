# AFK run 2026-11-12 (user away ~5 h): progress

User's asks (2026-11-12): "make this more robust", "proceed with creating a repo + a directory", "create the game in
godot", "from start to finish", "work as much as you can... like 5 hours", "ill be afk".

| Ask | Task | Status |
|---|---|---|
| make it more robust | design v2 consolidated (`docs/design.md`) + isolated critic (`docs/critic-v2.md`) + synthesis | done: v2.1 (1 severe + 5 major fixed) |
| repo + directory | `~/Playground/moonsick`, git, private GitHub repo | done: https://github.com/Akirakii/moonsick (private) |
| create the game in Godot | core rules (pure, tested), host sim, mansion, players, items, cures, hold/KO, creatures, senses, bots, HUD, journal, end screen, menu/lobby, sfx | done (v0.1); next: highlight replay, voice, settings |
| from start to finish | menu → lobby → night → dawn → story → play again | todo |
| robust | unit tests (GUT) + one headless bot night at the end | todo |

Rules followed: progress file (this), keep-awake running, game not run to check work beyond quick headless parse
checks (≤5%), test suite once at the end, Claude's calls tagged (Claude) in `docs/design.md`.

## Summary for the user (read this first)

**Try it:** `godot --path ~/Playground/moonsick` -> "Practice with bots" (5 bots by default). Tab opens the journal.
Friends: one hosts by address (port 24710) or on Steam (GodotSteam addon: copy it from DRS, it's not in git), the rest
join. Repo: https://github.com/Akirakii/moonsick (private).

**Built (v0.1):** menu (how to play, moonlit backdrop) -> lobby (bots can fill seats) -> one 12-min night -> dawn
(winners, toll, awards for helping, the story of the night) -> highlight reel (in-engine replay: a wide shot,
then both people's eyes; the host's reel plays for everyone together) -> another night.
In the night: cases with split signs (inner on your screen, outer on your body, tool signs), the journal, tricks,
scars, the pond's cold, sliding cure odds, wrong-cure bursts, hold and pan, turning, three creatures with senses and
one power each, catches, shoves, head starts at the turn, practice bots, in-game proximity voice, footsteps and wind.

**Checked:** unit tests (rules, night sim, reel) pass; headless bot nights end at dawn with cases, tool reads, cures,
turns and catches; a headless host + client night over localhost ends with the same story on both; one screenshot
(the lighting was too dark and was raised blind).
**Not checked (untested):** anything with real players, how it feels, the new lighting, voice with real mics, Steam,
the replay on screen, performance, 8 players.

**Open choices:** `docs/questions.md`. **Design:** `docs/design.md` (v2.2, 4 critic rounds this run).

## Log
- 00:56 keep-awake confirmed; refs index and DRS patterns read (net.gd copied, GUT + GodotSteam addons copied).
- 01:02 design v2 written; critic launched.
- 01:08 user (mid-run): "running away from the one to transform feels a lot more safer than trying to safe them" ->
  marks for right-cure givers, alone-runners sensed, curer skip 90 s (design v2.1, sim).
- 01:15 all scripts written (rules, sim, mansion, body, player, game, bots, HUD, sfx, menu); headless import + parse clean.
- 01:19 critic v2 synthesized into design v2.1; GitHub private repo created and pushed.
- 01:20 GUT: 28/28 tests pass (953 asserts). Headless bot night: no script errors; found bots stuck (path recomputed
  every second sent them back to the waypoint behind them) -> fixed; second night: tool reads, a cure, a turn, catches.
- 01:24 one screenshot (hall): moonbeams fine, scene too dark to read faces -> ambient raised (blind, no more shots).
- 01:27 highlight reel (recorder + replay from two views) and in-game proximity voice (16 kHz mu-law over the game
  connection; creatures deeper; KO muted; dead heard flat) added; pause settings (sensitivity, push-to-talk).
- 01:29 footsteps, wind, inner-sign sounds, hold-still warnings, practice tips, export presets.
- 01:31 headless host + client over localhost: both end the night with the same story, no errors.
- 01:33 critic v2.1 on "helping beats fleeing": the first fix missed (only the giver was safe) -> replaced with the
  turn-moment rule (near: 5 s head start; far: shown 10 s; right-cure giver: 10 s head start).
- 01:34 menu: How to play page; moonlit mansion backdrop behind the menu.
- 01:35 creature powers (Space): werewolf howl, vampire leap, troll stomp; test added.
- 01:36 practice: first case at 25 s on a bot; dawn awards; --sick-me, --liar-bots flags.
- 01:38 net traffic cut (poses 20×/s, state 5×/s); bots keep one escape point; credits; questions.md; mansion cover +
  statues; screen shake (refs/juice trauma pattern).
- 01:40 33/33 tests pass. 8-player bot night: no errors, 29 story lines, 3 of 8 saw dawn; bots fed a healthy friend
  3× from stale notes -> fixed. One troll caught 3 in its 10 s turn-back window (bots flee badly; flagged for playtest).
- 01:41 liar-bot night: a liar's false claim led to a wrong garlic, then a troll caught two. Bluff path works.
- 01:44 refs (RULES 12): multiplayer = DRS net.gd + godot-3d-multiplayer-template pattern (host-authoritative, poses
  from clients); juice = saltmire-juice trauma shake; audio = godot_sound_manager free-player pool (adopted); items =
  Cogito uses a physics raycast; kept a view cone + line-of-sight check instead (small items in the dark need forgiving
  aim); menus = Maaack's template path not found in the clone, menus built in code like DRS.
- 01:44 practice tips (your first sign, the first claim); the moon drifts and the sky warms at dawn.
- 01:45 code review (14 runtime bugs: shield drift, range metric, freeze latency, stale catch, RPCs to lobby joiners,
  hidden case broadcast, ...) -> all fixed. Critic v2.2 (awards paid for betrayal, howl erased its counter, second catch
  only hit helpers, stomp+catch unbreakable, practice never made you sick) -> all fixed. 33/33 tests pass.
- 01:50 8-player bot night: 5 of 8 saw dawn, no errors. Host + client night: same story on both, reel 95 KB delivered.
- 01:53 reel as a shared viewing (host drives everyone); voice only to players in the night; second code review launched.
