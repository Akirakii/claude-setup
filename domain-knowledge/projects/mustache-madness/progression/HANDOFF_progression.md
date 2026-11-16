# HANDOFF: guided progression, beasts, sieges, boat arrivals (AFK relay, started 2026-10-27)

## Status (for the user's return)
- DONE, waiting on the user: PRs #406-#412 reviewed cold, 8 fixes in, full suite 1448/1448
  on 897e97e5. Merge was blocked by the permission classifier: the user squash-merges in order
  (#406..#412, each retargeted to feat/tabs-lab-unlocks). Main checkout is on feat/prog-7-docs
  (uncommitted rule edits carried); mm-prog worktree detached.
- Relay 1 done: PRs #406-#412 (prog 1-7) open, stacked on feat/tabs-lab-unlocks, suite
  green. Worktree /home/akiraki/Playground/mm-prog (branches feat/prog-1-tree ..
  feat/prog-7-docs). Main checkout not touched except this file and the BRAINSTORM doc.
- Power: AFK idle config (no poweroff) until the user ends AFK.

## Purpose (user)
The player always knows what to do next and why, and the run has an action curve: build-up,
siege, release. Progression is "you do it by hand, then the city takes it over".

## Design source
`docs/BRAINSTORM_design_progression.md` (decided (user), proposed, open forks; main checkout,
untracked). Close every open fork with `.claude/skills/design-dialogue/SKILL.md` AFK mode
(section 6) plus `/design-idea`, and log each pick in that doc and below. Read both skill files
from the main checkout path (/home/akiraki/Playground/mustache-madness/.claude/skills/...):
the worktree lacks the uncommitted skill edits.

## Rules for the relay
- Stacked branches in the worktree, one PR each, base of the stack = feat/tabs-lab-unlocks.
  Never edit the main checkout except this file and the BRAINSTORM doc.
- No balancing (no tuning, no sim batches to move a number); log balance questions below.
- Every playtestable PR ships a cheat key. Pool: at most 5 agents alive counting you, reused.
- The local full suite is the only gate; run it once on the stack top.
- Write each decision "(Claude)" with a one-line reason; the user reverses on return.
- Final report: `MERGE #...` with the full-suite result, plus the /afk step 10 playtest report.

## PR list
1. **Requirement tree (walking skeleton).** Locked cards open by a requirement, not a random
   lab find; meeting it opens the card and reveals its children. Hand jobs open by the hand
   act (carry a downed friend, chop, axe the ore, jail a friend, carry an egg); jobs with no
   hand act by the lab (pick how, fork). The Work tab shows the frontier up to two steps
   ahead, each locked card with its requirement icon (hand, build, lab). Unlock banner kept.
   Cheat to open all kept. Done: tests for a hand-act open, a lab open, frontier reveal, save
   round trip.
2. **Frog guide at dawn.** Delete the stale lines (Fuse Cube, van, well, beds with crops). At
   dawn the frog says one line about the worst thing last night and the card that answers it;
   first-time lines once only. Done: tests on the dawn pick; cheat to force a dawn line.
3. **Glance icons for herd wants.** The herd's top 2-3 unmet wants as small HUD icons (rolled
   up from wish balloons). Done: test on the roll-up; cheat.
4. **Beasts replace wilds; taming cut (user).** Enemies are beast species, never friendly
   species, never tamed; a downed beast does not join. Medic beds serve friends only. Few
   beast kinds (fork: how many, what each attacks). Done: tests that a downed beast never
   joins and friendlies never spawn hostile; cheat to spawn a beast.
5. **Siege rhythm (user).** Beasts come every 3, 4 or 5 nights, not every night (fork: fixed,
   growing, window; nights between calm or small trouble). A visible countdown and a preview
   of the coming beasts. Done: tests on the schedule and countdown; cheat to skip to siege.
6. **Boat arrivals (user: like Animal Crossing).** New species come by boat to the island
   (proposed: a pier the player builds calls boats; the tree decides which species; a
   visitor's wish balloon decides if it stays). Replaces taming as the herd source with
   breeding. Done: tests on arrival, stay, leave; cheat to call a boat.
7. **Docs.** README How to play, LAW or TODO updates, the design log.

## Resume here
- Merge-gate review fixes done (8 items, fixups autosquashed into PRs 4-7, restacked,
  force-pushed). Top 897e97e5: full suite 1448/1448 green. PRs #406-#412 ready; relay
  reported MERGE again, never merges. Known: an ad hoc file order (housing + feeding before
  suffering_signs) fails 2 tests on the old top too (state leak, pre-existing, not fixed).

## Decisions for audit
- Purpose, PR list, AFK go-ahead (user: "proceed afk"). Merge target (Claude): the stack merges
  into feat/tabs-lab-unlocks, the batch branch the main checkout plays, not main, since #397
  is still open; the user merges #397 to main.
- PR 1 (Claude): a hand act opens its card at once. Why: cause and effect read on sight; a hidden count of N is a memorization table.
- PR 1 (Claude): FARM and HAUL stay on the lab; woodpile and mine become hand-gated (chop, axe ore). Why: walking skeleton, only the 5 acts the PR list names.
- PR 1 (Claude): the lab opens the first reachable lab card in authored order, not at random and not aimed at the top want. Why: predictable, one path; aiming is a hidden link (TODO).
- PR 2 (Claude): the frog sits on the statue and speaks there. Why: it cannot die and stands where the player defends.
- PR 2 (Claude): dawn problems ranked friend lost > friend down > statue hit; quiet night names the next frontier card. Why: the three the code already reports; hunger and theft later.
- PR 3 (Claude): 3 glance icons, count per want, red first. Why: PR list allows 2-3; counts, not means.
- PR 4 (Claude): 2 beast kinds, Bruiser (ram, statue) and Snatcher (ladder, eggs and dropped food, from night 7); gear bound to the kind, not rolled. Why: few kinds, each attack reads from its gear.
- PR 4 (Claude): beast drops stay the WildDropService gem/crop; no beast part. Why: no new noun.
- PR 4 (Claude): one friendly species list owned by PR 4 (FRIENDLY_SPECIES, starter subset START_SPECIES); boats read it. Why: one owner.
- PR 5 (Claude): growing gap 3, 4, 5 then 5 (sieges on nights 3, 7, 12, 17, ...); nights between are calm. Why: a clear build-up, peak, release; calm reads as the build window.
- PR 5 (Claude): difficulty = the siege's night number; bounty per siege; autosave every nightfall; forecast shows the next siege only (one HUD clause). Why: budget curve unchanged; avoids stacked forecasts.
- PR 5 (Claude): PR 5 adds the next-siege line to the frog's dawn pick (PR 2 lands first and cannot read it).
- PR 6 (Claude): a pier on the shore (wood, open at start) docks one boat with a pair of one species at each release dawn (first dawn after a siege); they stay only if 2 free beds by dusk, else the boat leaves. Why: Animal Crossing visitor, a pair founds a lineage, beds are the occupied shared state.
- PR 6 (Claude): species = one not yet in the herd, else the rarest; no frontier stat link. Why: c1 checked there is no stat gate, so the link would be invisible.
- PR 6 (Claude): once all species are in, keep sending pairs of the rarest. Strict one bed each.
- Process (Claude): relay wrote round 2 picks into each design doc itself instead of a designer round. Why: picks were small, saves three agent rounds.
- Cold review fix, PR 6 (Claude): a boat no longer keys on the siege calendar (a clock, against the "never on a clock" pre-pillar). At dawn, a pier with 2 free beds calls one boat with a pair; the pair takes the beds. No free beds, no boat; the pier shows the bed wish balloon. Why: arrivals follow beds the player built.
- Cold review fix, PR 1 (Claude): the tree has real parents (built): medic_bed after med_kit; cart_shed after woodpile; rail after cart_shed; rail_loader, rail_unloader after rail; lectern after library; chalkboard after library; treadmill after gym; bar after kitchen; shop after bar; bank after shop; police_box hand:jail after jail; nest hand:egg; woodpile hand:chop; mine hand:mine; med_kit hand:carry_down. Other lab cards have no parent.
- PR 1: lab re-posts RESEARCH when a card opens (findable can grow); tested.
- PR 2 + PR 5 (Claude): on a calm dawn the frog names the frontier card only; the siege line is spoken only on siege eve. PR 2 owns the guide text, PR 4 the run_hud taming tips.
- PR 3 / PR 6: lab aiming at the top want and "wanted-stat first" species pick are cut (not built).
- PR 4: guard the mend path too (a hostile in a bed never mends); FRIENDLY_SPECIES lives in CreatureConfig, intro and cheats read it.
- PR 5: on load, a forecast queue longer than the forecast depth is dropped.
- PR 7: TODO item for FARM and HAUL hand acts (deferred, not decided).

## Open for the user
- Pillar wording: "a capability opens when the player builds or raises something" vs "do it by hand first". Proposal (Claude): widen it to "builds, raises, or does by hand". Not written to MEMORY.md.
- Spike bench saves (nights 11, 24) load into calm nights after PR 5: re-capture or add a force flag.

## Balance questions for the user
- Emergency Post (hand: carry a downed friend) stays locked until the first siege downs a friend.
- Kill gems fall from 3 per night to 3 per siege.
- Herd inflow: a pair per siege plus breeding vs the old taming (47 recruits in 5 waves).
- Beast stats copied from frog/bunny vs a herd with no taming; calm night length.
