# TODO: room types

A room's type falls out of the room-only pieces inside it; the type sets its look (1.1) and
one rule (1.2). The type and its look: `docs/LAW_room_types.md`.

## 1.2: one rule per type
- Each type gets a rule, never a flat stat bonus (pillar: a reward is a new rule).
- Proposed first pair: Bedroom = today's bed rule (owner + close ones, full sleep refill).
  Bunkhouse = no owners, anyone takes any free bed, slower sleep refill. The trade is floor
  space against rest quality.
- The other types (hospital, nursery, prison, restaurant, bar, arcade, gym, lab, library,
  school, bank) each need their own rule, designed one at a time.

## Later: mixed contents
Proposed: two anchor kinds in one room make a Plain room. Every station keeps working; only
the type, skin and rule are lost. Rejected so far: disabling the room (same 🏚 sign as a
broken room for a different cause, and a bed beside a games table looks natural); the
most-common-kind-wins scoring (a fuzzy taxonomy).

## Later: creature status
Open question: what status is for. Its job is a reason to build better rooms and a choice
of who gets them. Options:
- A. No status: the Bedroom vs Bunkhouse trade is the choice; who gets a bedroom falls out
  of bed ownership.
- B. Status from raising (Dwarf Fortress style): top skill or seniority sets what a
  creature expects; housed below it, it gets a bad moodlet.
- C. Wallet economy (user's first idea): wages per creature, the rich afford better rooms.
  Conflicts with the pre-pillar "a gem pays a workplace, never a creature", with
  per-unit tracking and with frictionless hoarding; needs that pre-pillar dropped first.

## Next: creature economy (user, 2026-10-17)
- Creatures hold gems in their own storage: earned as pay, stolen, found.
- What they spend gems on is still to design (better rooms, food, fun), and an incentive
  rule: the more there is to buy, the more they work; with plenty of gems and nothing to
  buy, they stop working and just live.
- Stealing: a creature may steal gems. Catching thieves becomes the police's second job,
  beside catching rampagers (user).
- Supersedes option C above once designed; the pre-pillar "a gem pays a workplace, never a
  creature" (MEMORY.md) falls with it and needs the user's word.
- [x] Slice 1, thieves (PR 6, AFK picks): `Creature.pouch` (int, server, saved; save 18)
  holds stolen gems. A brewer (puffs: the sign the law asks a mood pull to start with) with
  an empty pouch walks to the nearest bank with gems (`Mode.STEAL`) and takes
  `THEFT_GEMS` 3 (a limit: one haul); the haul ends its puffs with `RELEASE_BUMP`, as a
  rampage's end does (RimWorld's catharsis after a break). A wanted creature (a rampager, or
  a friend on its feet with a pouch) is the cop's ARREST site; jailed, the pouch goes into
  the cop's bag (it delivers it like a payer: a due station, else the bank), or drops at the
  cell from a player's hand; a thief that perishes, leaves at old age or is despawned drops it. 💰 head glyph from a `head_sign`
  bit. A free arrest takes an empty-handed payer off its till (JOBS "bumps"). Measured:
  `SIM_THIEF=1`, 240 s: thefts 1, arrests 1. Pre-pillar in MEMORY.md.
- [ ] What a pouch buys, pay into pouches, the banker's share (above).

## Later: university track benches (stage 2 PR 3, Claude)
- [ ] Desks by track: drafting tables seat INT-top students, workbenches body-top ones, the track
  fixed at the first class. Today any desk seats any student; the top stat at graduation picks.
