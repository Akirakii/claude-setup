# TODO: job economy follow-ups (stations, jobs, wild drops)

Left over from the AFK feature batch (#262 to #277, 2026-10-14/15).

## Experimental pillar clashes (the user decides after playtests)
The user kept these as EXPERIMENTAL on 2026-10-15: each stays in the game, and its pillar
edit stays a PRE-PILLAR (unconfirmed) in `MEMORY.md` until the user promotes it or cuts
the feature.
- [ ] **Job economy (#267, for automation at scale):** a gem pays a station's open hours.
  Bends "Sacrifice through occupied shared state, not a price" and "Roles emerge from
  raising, never from a purchase". PRE-PILLAR: "a gem pays a workplace's open hours".
- [ ] **Bank growth (#273):** a banker grows the vault (`vault x 0.005` a labor tick, cap
  20). Bends "a reward is never a flat bonus or a resource pile" and the job-economy
  PRE-PILLAR's own "a cap keeps it from being banked". No PRE-PILLAR written for it yet.
  The user also said yes to a bank paying its own hours from its vault: check that it
  does.
- [ ] **Wild crop drops (#265, a run can die without crops):** a dying wild drops crops
  when the player runs low. Bends "a reward is a new rule, verb, or board change".
  PRE-PILLAR: "a resource pile is allowed as the forgone side of a choice".

## Bugs
- [ ] `Crop.harvest` by a worker: the same-frame double-harvest hazard the tree had.

## Performance (not benched)
- [ ] `JobBoard._move_to_nearer_sites` scans every site per worker (about 2 ms at 6
  baskets, 160 sites).
- [ ] Every hurt ally posts a job site; the patient ring lookup per poll is not benched
  with many paid med kits.
- [ ] `Chair._table` scans the whole table group on each use.
- [ ] Wild drops: the death path has no wave-100 bench (night window).

## Sim coverage (the active sim bot)
- [ ] It never builds a basket, so sims do not measure farming.
- [ ] It never affords the 104 hut planks (0 beds in 3 seeds x 900 s), so sims do not
  exercise medic beds.
- [ ] It never places a med kit, so sims do not measure the medic under waves.

## Flaky tests
- [ ] `test_nav_obstacle_carve` (line 116) fails on CI now and then (twice in PR 8's runs);
  passes locally and on rerun.
- [ ] A physics navmesh ring test fails locally under `--fixed-fps` and passes on CI (seen
  in PR 10).
