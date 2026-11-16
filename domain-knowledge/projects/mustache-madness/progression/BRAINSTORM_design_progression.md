# BRAINSTORM: progression, discoverability, arrivals, siege rhythm

An idea pile for the user to cut. Only lines tagged (user) are decided.

## Decided (user)
- Every city job starts as something the player does by hand; its building opens once the
  player has done it, and the building takes that work off the player's hands (pre-pillar).
- Unlocks form a requirement tree: each node asks one requirement; meeting it opens the node
  and reveals its children.
- Friendlies are always friendly species. Beasts are a new enemy kind that can never be tamed.
- Taming is cut: it is the main herd source today and it is not fun.
- New species arrive by boat to the island, like Animal Crossing (shape to design).
- Beasts come every 3, 4 or 5 nights, not every night: a build-up, a peak, a release.

## Proposed (Claude, open)
- Tree frontier shows at most two steps ahead, in the Work tab, each locked card with its
  requirement icon; each requirement is the need its card serves; a card with no natural
  requirement goes to the lab.
- A visible siege countdown with a preview of the coming beasts.

## Open forks
- Nights between sieges: fully calm or small trouble.
- Siege gap: a fixed 3, 4 or 5, a growing gap (3, 4, 5), or a window.
- How a hand act opens its card (at once, after N, or by aiming the lab).
- Jobs with no hand version: how they open.
- Arrivals by boat: what calls a boat, who stays, and what it costs.

## Closed forks (Claude, AFK relay; the user may reverse)
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
