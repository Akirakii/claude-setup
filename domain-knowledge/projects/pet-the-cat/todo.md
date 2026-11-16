# Todo and gaps (2026-11-07)

Each item: what, why, recommendation. Fun questions wait for the user's playtest.

## Needs the user
- **Playtest with friends** (recorded with voices): do 4 friends laugh within 5 minutes and ask for
  another round? Everything below is tuning until this happens.
- **Confirm the (Claude) rules** in `docs/design.md`, especially: rage target = whoever stopped last;
  a kill satisfies the cat; ghosts while down; Belly Up.
- **Export templates for Godot 4.7.2**, then `tools/export.sh`.

## Gaps found while building
- **Bots don't die in lava** (they skip the lava check). Only matters for automated tests.
- **No proximity voice chat.** The playbook ranks it high for friendslop; GodotSteam has voice
  (https://godotsteam.com/tutorials/voice/). Recommend: after the first playtest.
- **The cat ignores furniture while moving** (it flies through the cabinet during Zoomies and
  chases). Reads as leaping; fix with a path or a radius that clears furniture if playtests notice.
- **Art is grey boxes plus the Meshy cat.** Recommend Meshy hero props (cat tower, sofa, vacuum)
  only after the playtest says the loop is fun (Dungeon Pets guardrail).
- **Steam lobbies untested end to end** (code from Red Button, where it worked with Spacewar 480).
- **More minigames** (ideas, each a different action): Laser Pointer (one player aims, the cat
  follows), Cucumber (don't let it see the cucumber), Bath Time (carry the cat), Treat Toss.
- **Accessibility pass** against `docs/accessibility-patterns.md`: hold-to-toggle for petting,
  subtitles for the sound cues (klaxon, purr, hiss), colour-blind check of the calm bar.
