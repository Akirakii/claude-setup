# TODO: progression follow-ups

Open items left by the progression stack (prog PRs 1-7). Design log:
`docs/BRAINSTORM_design_prog_{abstract,c1,c2,c3}.md` (each doc's Round 2 and Round 3
sections override its body).

- **Hand acts for FARM and HAUL (deferred, not decided).** Farming and the Cart Shed still
  open by the lab; the pre-pillar "every city job starts by hand" suggests harvest a crop and
  carry a log. Needs a design pass.
- **Recruit counters read 0.** `BalanceProbe.recruits` and its `rec_*` overlay, the sim
  driver's `recruits`, and the tracker's 🫱 count stay in place but nothing feeds them since
  taming was cut. Replace them with boat tallies (`Pier.boats`, `Pier.stayed`) or delete.
- **Spike bench saves land on calm nights.** `test/local/bench/saves/playtest_wave11/24`
  load nights 11 and 24, which are calm now: re-capture on siege nights or force a siege.
- **The sea past the edge.** A docked boat draws its own patch of water; judge in a playtest
  whether the island edge needs a real sea plane.
- **Lab aiming (cut idea).** The lab could aim at the frontier card that answers the herd's
  top want; cut as a hidden link for now.
- **Pillar wording (user).** A hand act is neither "built" nor "raised": the pre-pillar "a
  capability opens when something the player builds or raises makes it possible" needs
  "or does by hand" if the user confirms.
