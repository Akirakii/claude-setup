# TODO: stage 3 (designed, not built; picks are Claude's until tagged (user))
Design: docs/BRAINSTORM_design_c6_stage3.md. Rules: a capability opens when what enables it
exists (user); trains carry resources and creatures (user Q6); wilds walk across rails (user Q7).

- [x] City heart (built, unlock PR 5: City Stone + statue, nearest heart). A City Stone the player places names a city; a station belongs to the
  nearest heart (the statue for home). No health, not a raid target. Fork: stone, or navmesh
  islands on later maps (Claude picked the stone). Done: stations report their city in a test.
- [x] City tags (built, unlock PR 5: three standing mood rules, no flat mood; user seed: "status or city tags that create their own mood or effects"). A tag
  derives from the city's stations, as an anchor names a room's type: most WORK -> work town,
  most FREE_TIME -> party town, most STAY -> sleepy town. Each tag: one moodlet on its
  residents + one effect (work town: shifts longer; party town: fun fills faster). Shown on the
  stone. Done: a party town's resident gets the moodlet.
- [ ] Land growth (Q5 rest). A track piece laid at the map edge grows the land on that side
  (one-sided `grow_by`); every city stays live, no summary. fps risk logged per growth.
- [x] Train loader jobs (built, unlock PR 7: a porter, Job.HAUL, at each stop; the cart waits docked). Was: reuse c3's hauler: a cart shed
  whose ring holds a stop loads it (stop = sink) or empties it (stop = source). No new job.
- [x] Trade prices (built, unlock PR 6: the dock sells at its city's logs per gem; the cart brings the till home). A city's price for a kind rises as its stations hold less of it; a shipped
  unit is paid sign to sign (receiving workplace pays the shipping one) at the receiving city's
  price. No outside market, no minted gem (pre-pillar 1). Fork with c4's payee rules.
- [x] Creatures ride (user Q6; built, unlock PR 8: commuters, a bag of room each). A creature with a job in another city rides the train to it; a
  car seat is the shared space (sacrifice: seats vs cargo). Fork: commuters vs movers only.
- [ ] Startups (Q9). A founder's shop (c4) the player backs by paying its sign; once its sign
  has paid BRANCH_SHIFTS shifts (a count on the piece, not a clock) and a rail line runs from
  its city, a dark copy of it appears on the nearest free cell inside a player zone (F13) by
  the line's far dock: a board change any creature there may found. No dividend, no shares,
  no exchange board. Done: a backed shop past N shifts gives one dark branch in city B.
- [ ] Land purchase (user frame: creatures buy land). A creature in free time with LAND_PRICE
  gems of its own (more than a full pouch, FOUND_GEMS) walks them to a Land Office the player
  placed and claims an unclaimed LAND_PLOT inside a player zone (F13); the gems stack at the
  office for the player (not a sink). It becomes proprietor of every sleep bed on its plot and
  takes their rent (RENT_PRICE). Done: a buyer's gems at the office, beds on its plot rented.
- [ ] Tax Office (replaces "one gem per day"). A resident (its bed's city) whose bed lies in an
  office's ring and whose pouch passes a full pouch (FOUND_GEMS) walks each gem over it to the
  office in its free time; the gems stack there for the player. The lever is where and how many
  offices (placement), never a rate menu. Income is capped by the residents in rings
  (pre-pillar). A taxed ring never saves LAND_PRICE: tax and land compete for one pouch.
  Done: a resident at FOUND_GEMS + 2 walks 2 gems in and keeps FOUND_GEMS.
- [ ] Wilds vs trains (Track D). A wild on the track is sent flying by a cart (goofy, no block).
- [x] Rail gate (built, unlock PR 5: rail and stops open on the first City Stone): what enables rail (rail is in the menu from the start for the skeleton). Rec:
  it opens when a second city's land exists (a City Stone placed, or the land grown).
- [ ] Rail later: slopes and bridges, more carts per line, switches, a stop that loads any kind.
- [ ] Train class: PR 11 kept the trip on the RailLoader (one cart per line); a Train node
  of its own once a line runs more carts.
- Balance questions (log, no tuning): TRAIN_LOAD 45, TRAIN_SPEED 6, the line's gem as a sink.
- [ ] Rail polish (PR 11 review, logged): the cart checks every route cell each tick (check on
  a grid change); two drags offset by one cell sit on different 2-cell lattices and do not join
  (snap LINE feet to even cells); `_unloader_at` scans every station per route cell; an unpaid
  loader still takes choppers' logs; STOP_REACH is 2 m (the design said 1.5).
