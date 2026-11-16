# Research log

Dated notes on what was researched, sources, and conclusions. Newest at the bottom.

## 2026-11-01: project created
Reports moved from assemblia/docs. Steam endpoints verified: community memberslistxml (followers), ISteamUserStats/GetNumberOfCurrentPlayers (live players), storesearch + appdetails (appids, reviews); YouTube search HTML gives view counts.

## 2026-11-01: measured signals
`tools/signals.py` fetched followers, live players (game + demo), reviews and top-YouTube-trailer views for 74 games -> `data/signals-2026-11-01.json`. Radar potential section replaced by measured tiers. Big: Dear Passengers (102k followers), Family Time (49k), Haunted Paws (42k), Worst Class Ever (13.2k live demo), Fart Together (7k live demo). Most animal co-op entries tiny (Party Club 100, Among Paws 37). Mismatches: Digging a Hole Together and Pratfall matched older games; several YouTube tops were unrelated (yt_match=false).

## 2026-11-02: playbook
Design (hooks, review evidence from ~20 reviews x 17 games, dev quotes) and marketing (~15 case studies, thresholds, timeline) -> `reports/playbook.html`. Key: readable blame for failure; social friction; tempting dumb tools; 3-6h + replay layer; public lobbies; short video + demo before Next Fest; $5-10. Five idea directions (den parents, beaver dam, critter band, hive shift, burrow hotline) as options.

## 2026-11-02: furry theme dropped
User: forget the furry tone, keep it clean. Removed furry framing from radar, pulse and playbook; CLAUDE.md updated. coop-report.html keeps its old furry-market section as history.

## 2026-11-02: idea checks and scan results (handoff)
- **Drill idea (user):** friends in a drill truck heading to the Earth's core; mine/extract energy outside on each layer, repair and upgrade the drill, go deeper; layers hold mysteries, dinosaurs, conspiracy theories. Verdict: promising. Structure = Lethal Company / R.E.P.O. hub-and-level loop (drill is the hub room; descending is a transition, not live vehicle physics, so networking stays cheap). Split crew (inside keeps drill alive, outside mines) gives readable blame. Conspiracy layer = clip hook + replay layer; use harmless ones (Hollow Earth, Atlantis, dinosaurs, moon-landing set, Area 51, Bigfoot), avoid ones with hateful roots (reptilian elites). Biggest risk: scope. Same-premise rivals are tiny: Drill Crew (Jul 2026, 22 followers, 0 players), BORE to the CORE (Q4 2026, 18), BORE (horror, Nov 24, 581); Volcanoids old (95k followers, quiet); Core Diggers (6p co-op digging, TBA); A Game About Digging a Hole Together (Dec 4, Game Pass).
- **Submarine variant:** more crowded. S.O.N.A.R. (Oct 29 2026, $8.49, 95% of 184 reviews, 8,023 followers, ~2,000 live on day 4: healthy, not failed), Barotrauma (5.4k live), Murky Divers, We Need To Go Deeper, Deeper (upcoming). Recommended the drill over the sub.
- **Friendslop scan** (`data/friendslop-2026-11-01.json`, 398 friendslop games): CRACK (Oct 26, $6.79, co-op incremental mystery about cracking a giant egg) had 6,777 live players: the best live evidence for the drill idea and its closest spirit-rival; study it first. School-cheating microtrend: Finals Week (Oct 29, 2,590 live), CheatCheat, Worst Class Ever. New names: Too Deep To Quit, Night Shift Hospital, Hold My Thing, Safari-TV, Totally Safe Moon Project (Oct 30, build up to the moon), Another Door, DungeonBox. Scan limits: wishlist_rank is per tag list; followers mostly missing (rate limit); old giants (TF2, Garry's Mod) slipped in, filter to 2024+.
- **Rocket idea check (2026-11-02, user: "rocket engineering with friends"):** crowded with tiny entries, no breakout. Data: `data/signals-rocket-2026-11-02.json` (checked, Steam, Nov 2). Totally Safe Moon Project is tower stacking, not rockets ($4.49, 1,799 followers, 140 live on day 3: modest). Closest to the pitch: Junkyard Astronauts (Oct 27, $4.97, weld scrap into a rocket, 25 followers, 0 live: a near-exact attempt that got no traction), Actually Rocket Science (crew flies a rocket with ~400 switches, TBA, 68 followers), Rocket Together (assemble during countdown, 1 follower), Astronimo (2023, $14.99, build/break to escape, 1,314 followers, 0 live). Same-theme stacking: Stack Together: To the Moon, Climb to the Moon. Review counts not fetched (appreviews endpoint returned empty). Verdict: no proven demand signal like CRACK gives the drill; drill stays ahead.
- **Tycoon friendslop (2026-11-02, user question):** works when the business is physical and the money layer thin. Live now (checked, Steam): Schedule I 12,661, Supermarket Together 7,468, TCG Card Shop Sim 5,863, Gamble With Your Friends 4,066, Overcooked 2 3,247, PlateUp 2,548; slower spreadsheet-style management sims 140-180 (Car Dealership Sim 2, Drug Dealer Sim 2, Restaurats). Scan has ~10 upcoming chaos shop/job sims (Shark Mart, Hellterns, Worst Airline Ever, Night Shift Hospital, Witch/Butcher Shop Sim, No Refunds...).
- **Hotel idea (user: one hotel, add rooms, maintain):** many co-op hotel/motel sims, all weak. Data `data/signals-hotel-2026-11-02.json` (checked, Steam): Tropical Resort Sim (May 2026, $13.99, 1,592 fol, 173 rev, 9 live), Miami Hotel Sim (2025, 1,349 fol, 144 rev, 4 live), Crazy Hotel Together (Mar 2026, co-op, 211 fol, 2 live), Arcade & Motel Sim Together (Oct 30 2026, 151 fol, 34 live), Your Own Cozy Motel (0 live); upcoming Road Motel Sim (223), Inn Keeper (559), Hotel Manager: Together, One Star Hotel, Hotel BOOM! (all <35). Verdict: theme is taken and has not paid as a "simulator"; only viable with a strong chaos hook.
- **Chaotic hotel friendslop (user clarified):** tag-checked against the friendslop definition (Steam, Nov 2). Chaotic job sims have demand: Night Shift Hospital (5,076 followers, friendslop wishlist rank #9), Shark Mart (Nov 26, 2,929 followers, rank #24; sharks secretly kidnapping fish), Worst Airline Ever (243). Chaotic hotels are weak: Crazy Hotel Together (friendslop, released Mar 2026, 211 followers, 2 live = failed attempt with a generic "unusual hotel" pitch), One Star Hotel (23), Midnight Hotel (17, night-shift horror), Ghost'Inn (8). Supermarket Together is free-to-play and not friendslop by tags (no chaos tag). Reading: the lane wants a sharp twist (Shark Mart's secret, Night Shift's bizarre patients), not "chaotic X".
- **Space hotel for impossible alien guests (user pick, 2026-11-02):** no co-op chaotic alien hotel found. Data `data/signals-spacehotel-2026-11-02.json` (checked, Steam). Theme proven single-player only: Hotel Galactic (cozy hotel, EA Jul 2025, $34.99, 15,865 followers, 611 reviews, 21 live), Galacticare (alien hospital, 2024, 10,081 followers, 605 reviews), Spacebase Startopia (13,357). Closest co-op: Snack Station Co-op Simulator (space snack bar, oddball customers, 212 followers, not friendslop by tags). Warning: "keep a failing spaceship alive" chaos lane is weak (Space Chaos 0 live, SpaceBuddies 0, Crewed 223 followers); the hook must be the guests, not ship repair. Scope risk: every alien species = new model + needs + behaviours.
- **3D survivors-like friendslop (user question, 2026-11-02):** scanned 162 Steam games tagged Bullet Heaven + Online Co-Op (`data/bulletheaven-coop-2026-11-02.json`, checked Nov 2). The genre hits have no Online Co-Op tag: Vampire Survivors 4,175 live, Brotato 7,743, Megabonk 3,860 (3D, 101k reviews), DRG: Survivor 1,966. The one online co-op hit: The Spell Brigade (3D, $12.99, released Apr 2026 after a demo in May 2024, 49,010 followers, 15,037 reviews, 1,566 live); next is Sineus Arena Survivors (110 live). Only ~5 have a chaos tag (Entropy Survivors 9 live, Co-op Chaos in Berlin 2 followers, GrindFall 6, Furmageddon, Donauts): open but unproven. Reading: survivors co-op is usually parallel play (each builds own power), so it lacks friendslop's interdependence and blame; the genre also needs content depth (weapons, synergies, balance), against the cheap-toy model. Viable only with a mechanic that ties players together.
- **Crew-one-machine friendslop (user question, 2026-11-02):** checked (Steam, Nov 2). Friendslop by tags: RV There Yet? (2–4 players, one RV, 7,911 live, 76,777 reviews, 136k followers), S.O.N.A.R. (1–6, sub, 1,952 live day 4). Crew-machine hits not friendslop by tags: Barotrauma 4,941 live, Sea of Thieves 4,785, Drive Beyond Horizons 1,894; weak: Void Crew 96, Unrailed 2 111, Volcanoids 53, We Need To Go Deeper 15. Upcoming friendslop crew-machine: Emergency Buddies (ambulance, 4,272 followers), RV (941), Tower Tanks (co-op vehicle combat roguelike, 573: closest to survivors-on-a-machine), Ship or Burn! (train, 390), Fish & Ships (airship, 328). Closest mechanic to a machine survivors game: Lovers in a Dangerous Spacetime (2015, stations on a ship vs enemy waves, more stations than players, 3,379 reviews, 24 live, no Online Co-Op tag). Works at 2 players when stations outnumber players.
- **Survivors-machine sketch + names (2026-11-02):** first-person, 2–8 (machine grows a section per player pair), stations > players, gem runs outside, level-up parts add stations. Name candidates free on Steam store search (trademark/web not checked): Get Back In The Truck! (recommended), Swarm Wagon, Nobody's Driving, Junk Fortress, Fire In The Back. Taken: Who's Driving?, Keep It Rolling, RIG Riot, Hordebreaker.
- **Art decision (user, 2026-11-02): goofy 3D** (Megabonk-like), simple round creatures. Setting check: survivors hits split fantasy (VS, Halls of Torment, Spell Brigade) vs sci-fi (Brotato, DRG: Survivor) vs neither (Megabonk); setting does not decide success, 67/162 co-op survivors are fantasy/dark fantasy.
- **Train as the machine + names (2026-11-02):** no co-op train survivors among 162 co-op Bullet Heaven games. Train rivals (checked, Steam): Voidtrain (co-op survival-craft train, 125,321 followers, 488 live, not friendslop), All Aboard! The Train Defense Express (single-player train bullet heaven, 755 followers, 9 live), Choo-Choo Charles (single, 16,580 reviews, 131 live), Heat Death: Survival Train (14,520 followers, 18 live), Fright Train, Apocalypse Express, Dreadline Express (all single-player, weak). Naming patterns: "X Survivors" is 23/162 co-op survivors names with no hit; train games overuse "X Express"/"X Train"; friendslop hits use one punchy word (PEAK, CRACK, R.E.P.O., LORT) or a plain-speech phrase (RV There Yet?, How to Fish, Gamble With Your Friends). Names free on Steam store search (trademark/web not checked): Get Back On The Train! (recommended), CABOOSE, Choo Chew, Don't Stop The Train, Last Car Is On Fire, Doom Caboose. Taken: Mind The Gap, Off The Rails, All Aboard!, Loco.
- **Inside-the-train names (2026-11-02, user: most play is inside, no get-back mechanic):** free on Steam store search: Mind The Horde (recommended), Who's On Coal?!, Nobody's Driving The Train, They're On The Roof!, Back Car's On Fire!, Who Pulled The Brake?!, Shovel Faster!, Keep Her Moving!, Next Stop: Doom. Taken: Pull The Lever, Last Stop, We Need More Steam!. New rival found: DON'T LET THEM BOARD! (friendslop co-op commuter-train party game, Oct 23 2026, 3 followers, 0 live).
- **Line/station + protect names (2026-11-02):** free on Steam store search: Hordeline (recommended), Blobline, The Doom Line, Junction 13, Night Line, Protect The Train, Save The Train, Hold The Train, Defend The Train, Protect The Choo Choo, Keep It On Track. Taken: Platform 13, Platform 0, End of the Line, Terminus (Zombie Survivors), Last Line (Zombie Horde), Stay On Track, Rail Guard. Near-clash: Horde Line vs Last Line: Zombie Horde.
- **Roblox train defense (checked, YouTube, 2026-11-02):** Dead Rails (Roblox, co-op train ride through zombie/vampire/werewolf hordes, classes, updates) has videos up to 4.87M views ("ROBLOX DEAD RAILS") and 885k (solo guide): strongest proof found that co-op train-vs-horde appeals, though on Roblox (younger, free). Roblox also has "Defend The Train" (guide videos 8-33k views), so "Protect/Defend The Train" names collide in search. Not checked: Dead Rails player counts (Roblox has no tool here).
- **Name chosen: Hordeline (user, 2026-11-02).** Web check: no game or trademark named Hordeline found (2 web searches; formal USPTO/EUIPO search not done). Near names in the genre (checked, Steam): HORDELIGHT (dark-fantasy bullet heaven, Sep 2026, 13 followers, 0 live), Hordelord (FPS horde shooter, Aug 2025, 586 followers, 0 live). The "Horde-" prefix is common in the genre.
- **Survivors skill systems (web, 2026-11-02, for Hordeline):** Vampire Survivors: auto-fire weapons, level-up = pick 1 of 3 (4 with Luck) new weapon / passive / upgrade; weapons max level 8, passives 5, ~6 slots each; evolution = max weapon + its passive (+ chest) -> evolved weapon; reroll/skip/banish (Prima, Dot Esports, wiki). Megabonk: weapons + 23 "tomes" (global stat buffs) + chest items; upgrades roll rarity (common->legendary); banish/skip/refresh (Gfinity, Dexerto). The Spell Brigade (co-op): shared XP, each level pick 1 of 3; spells get elemental infusions at levels 7 and 14; effects overlap in shared space, friendly fire; reviews split: PlayStation Country says co-op lacks players augmenting each other's attacks, TheSixthAxis calls co-op the highlight. Dead Rails (Roblox): train furnace burns any item incl. coal, chairs, enemy corpses; classes bought in lobby (Miner/Conductor = fuel, Alamo = defense); armored train slower and hungrier.
- **Hordeline skill system decided (user, 2026-11-02):** shared train build and XP; captain's hat holder picks 1 of 3 each level, no pause; host starts with the hat, it can be stolen and lost (playtest whether a grab cooldown is needed); VS-style 1:1 evolutions; limited mounts; furnace as the one chore.
- **Hordeline structure decided (user, 2026-11-02):** stages, each stretch a level ending at a safe main station; build carries over; goal = reach alive (no quota, no fuel clock); halts = optional loot risk; furnace sets speed; standing still piles up the horde. One economy: level-ups for weapons/parts, halt loot buys carriages/repairs.
- **Friendslop families by formula + live snapshot (2026-11-02, for Hordeline):** grouped the co-op report's subgenres into 7 families by what ties friends together (grouping and formulas = assumption, Claude's synthesis); live players checked (Steam, Nov 2 21:53 JST, one snapshot, just after Halloween), data `data/families-live-2026-11-02.json`. Top game per family: horror extraction (split information, proximity voice) R.E.P.O. 40,554 / Phasmophobia 8,496 / Lethal Company 1,758; physics traverse (bodies tied, one slip drags all) PEAK 13,566 / Chained Together 3,784; chill hangout How to Fish 8,607; party PvP Party Animals 7,170; station juggling (jobs > hands, jobs decay, jobs chain) Supermarket Together 5,652, Schedule I 5,223, Overcooked 2 5,098, Barotrauma 3,392, RV There Yet? 3,221, Sea of Thieves 2,054, S.O.N.A.R. 1,208, Unrailed 2 132; social bluff Gamble With Your Friends 3,486, Among Us 3,511 (Steam only); niches CRACK 2,941, MECCHA CHAMELEON 2,765, Finals Week 2,303. Reading: "maintain a machine" = station juggling, same formula as kitchens and shops; no giant but the most mid-tier hits (7 games at 1-6k). The two biggest families couple friends via split information or physical ties, which Hordeline lacks; none has a survivors build layer. Caveat: the families mix in neighbours that fail this repo's friendslop tag definition (checked earlier: Barotrauma, Sea of Thieves, Supermarket Together; others not tag-checked). Steam appreviews returned empty again, so no review counts.
- **Crew-machine fun formula (web, 2026-11-02, for Hordeline):** more jobs than hands + every job decays + failure escalates visibly (Sea of Thieves holes -> water -> rats leave) + jobs coupled by chain (Unrailed, Overcooked, Void Crew batteries), scarce hands (Lovers, SoT), split information (SoT lookout, Barotrauma sonar) or joint action + pressure in waves (Void Crew: big swarms kill communication, so they cluster them; Overcooked: lives-based survival bogged down, a timer fixed it; Lovers: forced roles confused, free roles worked). Sources: Void Crew NGJ 2024 talk (voidcrew.wiki.gg), Game Developer on Lovers co-op communication, MCV Develop postmortem of Overcooked, SoT wiki, Unrailed reviews. Hordeline gap (assumed, from its docs): solo chore loops, hold-E bars, slow HP attrition, constant spawns, nobody steers.
- **Friendslop by formula, not theme (2026-11-02, for Hordeline):** formula = pressure source + what ties friends together + where the laugh comes from; theme is skin. Seven formulas (grouping = assumption, Claude's synthesis; live = same Steam snapshot, `data/families-live-2026-11-02.json`), ranked by top game live: greedy run (go out, grab value, deeper = richer and worse, split up so info splits; R.E.P.O. 40,554, Phasmophobia 8,496, Lethal Company 1,758) > tethered bodies (my body moves yours; PEAK 13,566, Chained Together 3,784) > shared hangout (easy verb, mouth free; How to Fish 8,607) > slapstick rivalry (Party Animals 7,170) > growth loop (earn, reinvest, expand; Supermarket Together 5,652, Schedule I 5,223, CRACK 2,941) > juggling (jobs > hands, decay, escalate, coupled; Overcooked 2 5,098, Barotrauma 3,392, RV There Yet? 3,221) > hidden information (Among Us 3,511, Gamble With Your Friends 3,486, MECCHA CHAMELEON 2,765). Hits combine two: R.E.P.O. = greedy run + tethered (carry fragile loot with physics); Supermarket Together = juggling + growth; RV There Yet? = juggling + tethered. Voice is a coupling, not a formula. Hordeline today = juggling + growth, with greedy run only in halts; open question for the user: make halts/gems a real greedy run.

## 2026-11-04: what makes a full-co-op minigame fun (for Red Button Experiment)
- **Question (user):** what makes a non-PvP friendslop minigame fun; Red Button's minigames don't feel fun and players can't tell who to blame.
- **Sources (web, 2026-11-04):** co-op pattern research (Rocchi et al. patterns as listed in a Chalmers thesis; Bunker & Ryan, AUC 2017: closely coupled patterns affect player experience most, combining patterns showed no extra effect, few prototypes); Overcooked (Super Jump; GMTK video; Ghost Town interviews: one interact button, layouts split roles, chores with no owner, fire forces role swaps); Spaceteam (Henry Smith: different panel per player, instructions show on someone else's screen, shouting emerged unplanned); Keep Talking (Ben Kane GDC 2016: defuser sees, experts know); AppMagic friendslop 2025 ("playing badly is even better", "one bad decision can turn into a group problem in seconds"); playbook's Frog Sqwad vs R.E.P.O. review line (fault vs "unseen force").
- **Formula (Claude's synthesis, assumption):** fun co-op minigame = one simple verb + players need each other (split roles, split information, or one action that takes several) + time pressure that makes people talk + failure caused by one visible person, shown physically, and fast to retry.
- **Red Button diagnosis (read from its docs, not playtested by Claude):** green light, reaction, countdown, rhythm, quiz, audio quiz and decoys are parallel solo reflex tests on one shared button (same role, same information for all); the result is pooled (quiz sums presses) and failure is a ceiling drop with nobody named (todo.md "Make the blame clearer"). Rec: rebuild minigames on split roles or split information so a culprit exists by construction, and land the loss on that person.

## 2026-11-07: how incremental games are doing
- **Data (checked, Steam, 2026-11-07, one snapshot, Saturday):** `data/incremental-2026-11-07.json`, 385 games from Steam's Incremental tag (and Incremental + Online Co-Op), taken from top sellers, popular new releases, most wishlisted and popular upcoming; live players, reviews, price, top tags. Lists are sorted by popularity, so games that flopped are under-represented.
- **Findings:** (1) cheap ($3–9) first-person "chore + numbers go up" sims dominate new releases: Moon Sweepers (Oct 23) 23.7K live / 6.6K reviews; Potato Please 5.2K; Find The Needle 3.1K on day 1; Can 'Em All, Dirt Clicker, Playrooms 1.2–1.8K. (2) Free desktop idlers are the biggest: Bongo Cat 173K, TBH: Task Bar Hero 62K. (3) Long-tail hits by reviews: Scritchy Scratchy 17.3K, Bills Must Be Paid 13.5K, Leaf it Alone 7.6K. (4) Co-op incremental: few released hits (Brick by Brick, a co-op tidy-up, 1.3K live); a November wave is upcoming: Carve The Cave Together (Nov 10), Find The Needle Together (Nov 16, a co-op spin-off), SHRED A BILLION (Nov 24), Punch Your Way Out, Gamble Hunters (Jan 2027). (5) CRACK went from 6,777 live (Nov 1) to 1,792 (Nov 7); time of day differs, so treat the drop as rough.
- **Web (2026-11-07):** no reliable genre-wide figures; Steam H1 2026 $11.1B, +14.5%, 79% from older games (Alinea).
- **Incremental farming (checked, Steam, 2026-11-07):** `data/incremental-farming-2026-11-07.json`, 145 games (Incremental + Farming Sim/Farming/Agriculture, plus name matches). Released leaders: Berry Bury Berry 9.1K reviews (first-person, horror), Tiny Pasture 7.1K (idle desktop pasture), Farmer Against Potatoes Idle (F2P, 1.1K live). About 100 upcoming, mostly idle or cozy. Co-op: Shake it Co! (Aug 2026, 168 reviews), Find the Four Leaf Clover (Nov 15), Harvest Bliss (TBA).
- **Skill incrementals (checked, Steam, 2026-11-07):** `data/incremental-skill-2026-11-07.json`. Most demanding hit is IGTAP (precision platformer, 1.3K reviews); bullet-heaven incrementals mostly about 200 reviews; chore incrementals outsell them.

## 2026-11-09: how to find a good game idea (design research, session in ~/claude-code)
Context: since dropping Mustache Madness's core (6 months of loops), the user tried a new foundation
per day (4 so far). They learned when to stop a foundation, but not what its foundational problem is.
- **User's model:** a good idea needs fantasy, logic and aesthetic aligned. You can't fix one first and
  derive the others: each one redefines the others (chicken and egg), and spark depends on understanding.
- **No proven method exists for finding a good game idea.** Game design method research is mostly single
  case studies (checked: [NTNU thesis](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2402676?show=full)).
  Schools teach craft: the loop of prototype, playtest, revise (Fullerton's *Game Design Workshop*, Zimmerman's
  ["Play as Research"](https://jayisgames.com/games/loop/iterativedesign.html), Schell's lenses, MIT CMS.611).
  GDC teaches through postmortems, which carry survivorship bias (Claude's view).
- **Evidence from nearby fields (checked):**
  - Parallel beats serial: 3 versions at once, feedback on all, then refine
    ([Dow 2010](https://hci.stanford.edu/publications/2010/parallel-prototyping/ParallelPrototyping2010-submitted.pdf); banner ads, novices).
  - Hypothesis first (write the expected result and the kill result before building): startups did better
    ([Camuffo 2020 RCT](https://www.gwern.net/doc/economics/2019-camuffo.pdf); [replication, 759 firms](https://causalclaims.trfetzer.com/paper/DP15972.html)).
  - Rough prototypes find usability problems as well as polished ones ([Walker 2002](https://measuringu.com/prototype-fidelity/)),
    but are unreliable for player experience ([Gothenburg](https://gupea.ub.gu.se/items/40842b32-98cc-489f-b53d-3392f579728e)).
  - RITE: fix after each tester, so few testers go far ([Age of Empires II case](https://measuringu.com/rite-method/)).
  - Incubation: work hard, then a light break (one where the mind can wander), then return; small to medium
    gain, strongest for idea generation ([Sio & Ormerod 2009](https://eprints.lancs.ac.uk/id/eprint/56211)).
    Switching to another design project is not light. About 4 h of deep work a day is a rule of thumb, not a limit.
  - Trap, design fixation: seeing examples makes designers copy their features, even flawed ones
    ([Jansson & Smith 1991, via](https://strathprints.strath.ac.uk/79504)). Generate ideas first, research after.
- **Design theory (checked):** wicked problems: no definitive formulation, no stopping rule, only better or
  worse ([Rittel & Webber 1973](https://medium.com/homeland-security/ten-properties-of-wicked-problems-a8a9ff67ccdb));
  problem and solution evolve together ([Dorst & Cross 2001](https://oro.open.ac.uk/3278)); Schön: move, the
  situation talks back, reframe ([Schön](https://hci.stanford.edu/publications/bds/9-schon.html)).
- **User's graph model (approved 2026-11-09):** scope = number of nodes; coupling = number of connections
  (how sparse); high scope = more content and polish loops; high coupling = more loops to establish the core
  identity; a loop = playtest, then change the graph's structure or elements. Claude's additions:
  - Connections have a direction. A hub lowers coupling only if the other features use it without changing
    it. Red Button's narrator rules each changed the button, so coupling stayed high.
  - When scope and coupling are both high, their costs multiply (Mustache Madness, Claude's read).
- **NK model research (checked):** a design of N parts, each depending on K others. With K ≥ 2, finding a
  combination above a given quality is NP-complete ([Weinberger 1996](https://ideas.repec.org/p/wop/safiwp/96-02-003.html)).
  Fun is not cheap to check, so in practice it's harder. Higher K gives shorter climbs to lower peaks
  ([Kauffman & Weinberger 1989](https://embed.cocalc.com/share/download/943c068a27466910dfee6f6258d6a7d012683819/cocalc-examples/think-complexity-2ed/papers/kauffman89nk.pdf));
  the best results come at low but nonzero K ([source](https://eprints.soton.ac.uk/265781/2/ALIFExi_pp234-241.pdf)).
  Intermediate interdependence did best in technology ([Watanabe & Takagi 2022](https://ideas.repec.org/a/spr/eaiere/v19y2022i1d10.1007_s40844-021-00220-6.html)).
  Constraints help creativity "within limits" ([Acar 2019 review](https://openaccess.city.ac.uk/id/eprint/20459/)).
  Simon: systems that hold up are nearly decomposable ([1962](https://homes.cs.washington.edu/~ztatlock/599z-17sp/papers/complexity-simon-62.pdf)).
- **Prototyping practice (checked, secondhand):** Experimental Gameplay Project, 7-day prototypes, 50 games
  ([Game Developer](https://www.gamedeveloper.com/game-platforms/how-to-prototype-a-game-in-under-7-days));
  Content Warning came mostly from a month-long internal jam ([Landfall](https://landfall.se/content-warning-press-kit));
  Supercell kills projects early, on the team's gut ([GamesBeat](https://gamesbeat.com/how-supercell-kills-its-darlings-to-focus-on-potential-hits/)).
- **Open:** a log across the past foundations (Mustache Madness, Red Button, Pet the Cat, Deathly Reality Show,
  ...) with the same key choices for each, to find what the failures share (offered, not done).

## 2026-11-09: scope and coupling of the short-dev hits
The successful short-dev games from `reports/next-game-report.md` (dev time about a year or less), read
through the user's graph model: nodes = systems the player touches; content = how much hand-made stuff
fills them; coupling = connections where changing one node changes how another plays. The hub is the
core action. "Rewrites the hub" means a feature changes what the core action does, not just how hard it is.
Tags: dev time and team [source: next-game-report]; features [read: Steam store pages, fetched
2026-11-09], * = from memory, not on the store page; node counts and coupling [opinion].

| Game | Dev time, team | Hub | Nodes (systems) | Content | Coupling |
|---|---|---|---|---|---|
| MECCHA CHAMELEON | ~2 mo core, 2 | paint your body to match the stage | ~5: paint, pose, hide-and-seek rules, seeker search, stages | low | low |
| RV There Yet? | 8–9 wk, small studio | one RV driven together | ~6: driving, winch, RV damage, survival items, terrain, proximity chat | low | low |
| Content Warning | ~2 mo, 5 | the camera: filmed scares = views | ~7: camera, monsters, oxygen/battery, diving bell, 3-day views target, upload, shop | medium (monsters) | low–medium: monsters act on the camera and on danger, not on each other |
| PEAK | ~1 mo jam + months, 7 | climbing on a stamina bar | ~7: climb/stamina, injuries, food, items, hands and ropes, 4 biomes, daily map | medium | medium, all through stamina |
| R.E.P.O. | short, ~7 | carrying fragile physics valuables | ~7: grab tool, valuables, monsters, staying quiet, quota*, shop, levels | medium | low–medium |
| Gamble With Your Friends | ?, ~9 | one shared bank + 5-min daily quota | ~5: bank, quota, 17 chance games, 15+ items, 4 floors | medium (17 small games) | low: each game plugs into the bank |
| Liar's Bar | ?, animation studio | bluff, get called, Russian roulette | ~4: bluff rules, call, roulette, characters | low | low (one short chain) |
| Chained Together | ?, debut team | the chain between players | ~4: jump, chain physics, layers, modes | low–medium | low between systems, high between players |
| WEBFISHING | ~5 mo, 1 | hanging out; fishing as the activity | ~6: fishing, ~100 creatures, journal, upgrades, cosmetics, toys | medium | low |
| YAPYAP | <1 yr, ~10 | voice-cast spells | ~5: spells, vandalism points, tower, monsters, escape | medium | medium (spells combine); reviews: "needs more content" |
| How to Fish | ~1 yr, 2 | physics fishing | ~7: fishing, fish variants, selling, gear, quests, bosses, islands | medium–high | low–medium: one progression chain |
| Super Battle Golf | ?, Brimstone | golf swing, everyone at once, race to the hole | ~5: swing, sabotage items, courses, points, cosmetics | medium | low–medium |
| A Game About Digging a Hole | 2–3 wk, 1 | dig | ~4: dig, resources, sell, upgrades | low | low (one loop) |
| Buckshot Roulette | 4–7 mo, 1 | the shotgun's hidden shell order | ~5: shells, shoot-self-or-dealer turn rule*, items (~9*), health, dealer AI | low | medium: every item acts on the shells or the turn |
| Rusty's Retirement | 6–9 mo, 1 | a farm worked by bots at the screen's bottom | ~5: crops, bots, biofuel, selling, expansion | medium | low (one production chain) |
| A Short Hike | 7–8 mo, 1 | climbing and gliding, limited by golden feathers* | ~5: movement, feathers, NPC quests, fishing, items | medium (hand-made island) | low–medium |
| Vampire Survivors | ~1 yr, 1 | auto-attack through a horde + level-up pick | ~7: movement, weapons, passives, level-up, evolutions, enemies, meta gold | high (cheap 2D) | medium, in pairs: each weapon evolves with one passive [source: 2026-11-02 entry] |
| Megabonk | ~13 mo, 1 | 3D movement through a horde + level-up | ~8: movement, weapons, tomes, 70+ items, 20 characters, 240 quests, 2 maps | high | medium–high: tomes and items act on everything through stats |
| Brotato | ?, 1 | 20–90 s waves + a shop between | ~6: waves, 6 weapon slots, characters, items, shop, stats | high (hundreds of items) | medium, through shared stats |

Findings [opinion, from the table]:
- **No hit rewrites its hub.** Features make the core action harder, easier or riskier; none changes what
  it does. Red Button's narrator did ("keeps changing what the button does").
- **Few systems: about 4–8 nodes in every game.** Scope differences are mostly content.
- **Dev time follows content more than systems.** Shortest (Digging 2–3 wk, RV 8–9 wk, MECCHA and Content
  Warning ~2 mo) have little content; the ~1-year ones (Vampire Survivors, Megabonk, How to Fish, A Short
  Hike) have a lot. Fits "high scope = more manual work".
- **When features connect, they connect through one shared resource** (one value many features act on):
  stamina (PEAK), stats (Brotato, Megabonk), the bank (Gamble), views (Content Warning). Features rarely
  touch each other directly, so the number of connections stays low even with many features.
- **Where coupling ran higher, it was limited to pairs:** Vampire Survivors' evolutions are one weapon + one
  passive, not everything with everything.
- **Co-op hits put the coupling between players into the hub:** one chain, one RV, one bank, one camera,
  one fragile object carried together, a hand to pull a friend up. Players are tightly connected; features stay loose.
Limits: only hits (survivorship); most quick co-op hits had a team and reused tech (next-game-report);
node counts and coupling are a reading of store pages, not measured.
- **User's conclusion (2026-11-09, user):** "I assumed really hard that for low content to be fun requires
  high coupling for true emergence, but the true fun comes from the emergence of social interaction with
  your friends, and friends are always unique without me having to implement. That's why friendslop works."
  Claude's additions: friends only create that emergence when the hub connects them (parallel play gives
  none; DRS v1 "requires no cooperation at all"). Friends' reactions are also the marketing (clips, streamers).
  The limit is retention (D30 ~3%, peaks fall 90%+ in a month [source: next-game-report]): fine for a cheap
  finished game, weak for a live service.
- **Past foundations vs the formula (2026-11-09, user: "all my previous games failed because of the high
  coupling problem").** Claude's reading [opinion, from each project's docs and the user's verdicts, not played]:
  two couplings got mixed. Coupling between features: wanted low. Coupling between players: wanted high,
  through the hub. Most past games had it backwards.
  - Mustache Madness: four games' worth of features, all connected (high feature coupling + high scope).
  - Dungeon Pets: features stacked before the core was fun (POSTMORTEM); first person hid the systems (readability, not coupling).
  - Red Button: the narrator rewrote the hub (high feature coupling); everyone pressed the same button (low player coupling).
  - Pet the Cat: everyone pets the same cat (likely low player coupling); the user's reason for dropping it isn't recorded.
  - Deathly Reality Show: v1 "requires no cooperation at all" (low player coupling); Switchboard later stacked hidden rules (high feature coupling).
  - Hordeline: "solo chore loops, nobody steers" (low player coupling).
  - Assemblia: reason not recorded.

## 2026-11-09: how players are coupled in the short-dev co-op hits
Tags: [read] = Steam store page (fetched 2026-11-09); * = from memory; [source] = earlier entries/reports; patterns [opinion].

| Game | How one player changes another's result | Who affects whom | When |
|---|---|---|---|
| Chained Together | the chain: every jump pulls or holds everyone [read] | everyone ↔ everyone | constant |
| RV There Yet? | one RV: one drives, one works the winch, all keep each other fed and alive; "the driver will have a hard time completing this journey alone" [read] | role ↔ role | constant |
| PEAK | hands pull a friend up a ledge; a placed rope or spike helps everyone after you [read]; carrying a fallen friend* | one → one, one → all after | moments; ropes last |
| R.E.P.O. | heavy valuables need several carriers ("use teamwork") [read]; one loud player draws monsters to all ("know when to stay quiet") [read]; one shared quota* | carriers ↔ each other; one → all | while carrying |
| Gamble With Your Friends | one shared bank: "one bad all-in can ruin the run for everyone"; one daily quota [read] | one → all | every bet |
| Content Warning | one player films, the others are the show; views go to the whole team [read]; one camera at first* | camera holder ↔ the filmed | while filming |
| Liar's Bar | I claim a card, you choose to call it; whoever was wrong faces the roulette [read] | one ↔ one, by turns | every turn |
| MECCHA CHAMELEON | hiders vs seekers: my paint job is judged by your eyes [read] | two opposed teams | whole round |
| Super Battle Golf | sabotage: my ball, cart or orbital laser wrecks your shot [read] | one → one, opposed | moments |
| YAPYAP | spells push, pull, clone or disguise teammates*; one shared vandalism target [read] | one → one; all → one goal | moments |
| WEBFISHING, How to Fish | almost none in the rules: an easy action leaves the mouth free; friends connect by talking (and punching, in WEBFISHING) [read] [source: 2026-11-02 "shared hangout"] | — | — |

Patterns [opinion]:
- **The connection runs through the hub:** the chain, the RV, the bank, the camera, the valuables. The hub is the thing players share.
- **One player's action changes another's result, and everyone sees who did it:** the bet that emptied the
  bank, the jump that dragged everyone down, the one who missed the monster on camera. That visible "who did
  it" is where laughs and blame come from [source: playbook, "readable blame for failure"].
- **Opposed connections count too:** hiders vs seekers, golf sabotage, bluffing.
- **The hangout games are the exception:** almost no connection in the rules, so talk does it all. They are
  the purest form of the user's formula, and they lost players fastest (WEBFISHING ~99% from peak, How to
  Fish ~94% in a month [source: next-game-report]).
- **Is the formula new? (2026-11-09)** The pieces are known [source]: "fun that depends almost entirely on who
  you are playing with" (press on friendslop, [Creative Bloq](https://creativebloq.com/3d/video-game-design/what-is-friendslop-and-why-it-it-taking-over-gaming-in-2026));
  positive interdependence, where people must depend on each other and "simply placing students in groups is not
  enough", with four types: goal, resource, role, identity ([Johnson & Johnson, after Deutsch](https://en.wikipedia.org/wiki/Positive_interdependence));
  co-op game design pattern catalogues ([Rocha et al. 2008](https://gaips.inesc-id.pt/component/gaips/publications/showPublication/3/87);
  [El-Nasr et al. 2010, from 215 games](https://kksgandhi.github.io/personal_site/Cooperative_Game_Design_Patterns-El-Nasr.html); full lists not read yet).
  Not found written down: the combination of low coupling between features and high coupling between players
  through the hub, as the reason short-dev, low-content games can be fun. One round of searching can't prove absence.
- **The formula, user's words (2026-11-09): "low content, low coupling but only high coupling on players."**
  Second, targeted novelty search: the closest statements are "live social interaction is much more important
  than gameplay or game art" and "simple mechanics and chaotic group play" ([GamesMarket](https://www.gamesmarket.global/the-rise-of-friendslop-why-low-fidelity-social-chaos-is-shaking-up-the-games-industry/)),
  and emergence "produces content without content creation costs" ([Metavert](https://metavert.io/emergent-gameplay)).
  The three parts together as one structure were still not found. Status: the user's synthesis, a hypothesis from
  19 hits read by Claude (survivorship); the next foundation is its test.

## 2026-11-09: user's question that started the verbs research
- **User (2026-11-09):** carrying and throwing need more content to be fun, unlike hide and seek, which
  needs very little; "perhaps hide and seek makes the highest coupling between players". They asked for big
  research on gameplay verbs, ranked by how much they couple players. Report (in progress):
  `reports/Gameplay verbs and player coupling.md`; notes in `research_notes/Gameplay verbs and player coupling/`.

## 2026-11-09: gameplay verbs and player coupling (report done)
Report: `reports/Gameplay verbs and player coupling.md` (30 verbs ranked; notes in
`research_notes/Gameplay verbs and player coupling/`). Tags as in the report: [source] = page found this
session, [read] = Steam data pulled this session, [from memory], [opinion].
- **Why hide/bluff/deduce need almost no content:** the verb acts on a human who picks a counter and can't
  see everything, so no fixed best move exists. Hidden-target search games need spread-out (mixed) choices,
  while chase games where both sides see everything are solved by one plan ([source](https://arxiv.org/pdf/1811.09538.pdf)).
  Environment verbs (carry, throw at enemies, shoot enemies, build) face a world that doesn't react, so the
  best move gets found and must be replaced with content or connected systems (physics, AI director,
  generated maps) [opinion].
- **Content need follows who picks the counter, not the verb [opinion]:** seek human hiders (MECCHA, about
  2 months of work) vs seek an AI ghost (Phasmophobia, 14 maps, 30 ghost types) [source]; uneven sides bring
  content back (Dead by Daylight, about 42 killers) [source].
- **Ranking [opinion]:** the top 10 all act on another player's mind (bluff, deduce, hide, seek, betray,
  negotiate, signal across split info, draw/guess, coordinate without talking, vote); the bottom 4 act on
  the environment (race, shoot enemies, collect, build). Hide-and-seek ties with bluff/deduce. Its coupling
  runs between the two teams; inside the hider team players act side by side.
- **Co-op with no enemy team:** stop teammates acting as one mind (the quarterback problem). Ways: split
  information (Keep Talking, Spaceteam), narrow the channel (The Mind, proximity voice), private stakes in
  one shared node (shared bank, Dead of Winter), time pressure (Overcooked) [source]; or a monster that
  borrows the mimic verb (Lethal Company's Masked) [source, summary only]. Same object + limited shared
  resource was the only co-op pattern pair that raised engagement in a lab test [source].
- **Limits:** friendslop D30 about 3% (AppMagic) [source]. Social-deduction short-dev hits kept no more of
  their best month than co-op-vs-environment ones (median about 3.4% vs 5.9%) [read; rough, ages differ].
  The tail came from updates during the wave (R.E.P.O. 16.6%, PEAK 21.4%), strangers + skill + mods
  (CS 71%, TF2 63%, GMod 58%), player-made maps and generated layouts [read]. "Players are the content"
  quotes come from worlds full of strangers; whether it holds for a closed friend group is unmeasured
  [opinion].
- **For the formula [opinion]:** body coupling through one shared hub node + one hidden thing per player;
  plan the tail source (lobbies, Workshop maps, generated layouts, updates on the wave) or price for a
  short life ($5–8). Expect clones: a rule set this small can't be owned.

## 2026-11-09: a new gameplay verb (round 1 failed its critic)
- **User (2026-11-09):** "could you think about a new word? not used before that works?" Read as a gameplay verb
  no game has used that scores well in the verbs report [assumption, Claude].
- **Thesis** (`research_notes/Gameplay verbs and player coupling/new_verb_thesis.md`): Nudge (everyone pushes one
  shared pointer, nobody sees who pushed, private letters), Slack (hidden effort on a shared job), Copy (secret
  leader), Puppet (secret controller). Prior art found: Ouija video games use one ghost player who moves the
  pointer ([WE ARE SO DEAD](https://store.steampowered.com/app/4796830), [My Friendly Soul](https://gugation.itch.io/my-friendly-soul));
  a shared-pointer browser demo with no goals ([Ouijably](https://ably.com/blog/realtime-messaging-from-beyond-the-grave));
  slacking hidden from an AI boss ([Work from Home](https://www.co-optimus.com/game/12544/xbox-one/work-from-home.html));
  people spot a slacking partner 78.6% of the time ([lab study](https://oro.open.ac.uk/68461)); Find the Leader is
  an old camp game ([drama games PDF](https://resources.trinitycollege.com/hubfs/Trinity%20Drama%20Games%20Resources/Drama%20games%20-%20Whos%20changing%20the%20movement%3F.pdf?hsLang=en));
  Secret Shuffle's faker fakes a dance without music ([Steam](https://store.steampowered.com/app/2431820), 5 reviews).
- **Critic, severe frame findings (verified by Claude in the files):** all four hide the same thing, *who did it*,
  which the report already lists under Sabotage ("yes (who did it)"); pure co-op gives no reason to hide it, so
  voice chat reveals it in seconds; a pooled push is gameplay-anti-patterns #12 ("nobody needs anyone"); Nudge is
  close to DRS's The Tilt (summed tilt, one private key each, `docs/minigames-v2.md`), built and not yet
  playtested; hiding who pushed breaks visible blame (gate 4). Critic's prior art: Battlestar Galactica board game
  (cards added face down to a shared check, [review](https://islaythedragon.com/game-reviews/so-say-we-all-a-review-of-battlestar-galactica-the-board-game/));
  Feed the Kraken (hidden course cards steer one ship, factions want different ports, [Wikipedia](https://en.wikipedia.org/wiki/Feed_the_Kraken)).
- **Synthesis [opinion]:** no new hidden thing was found that works; nearly every hidden thing listed (truth,
  identity, place, loyalty, goals, knowledge, a word, timing, who did it, attention, own cards) is already a
  verb. The hits found new *actions* for old pairs instead: MECCHA CHAMELEON hides by painting your own body,
  Prop Hunt hides by becoming a prop, Liar's Bar bluffs with a revolver on the table. Taken to the user
  (frame change: new action for a proven pair, not a new structure). Also: playtest The Tilt first.

## 2026-11-10: idea search with the formula (2 critic rounds, stopped on a frame question)
Notes: `research_notes/Idea search/round1.md` (68 ideas: 18 grid twists + the user's 5 variations of 10
hits), `round2.md` (5 whole ideas). Ratings are [opinion, Claude], corrected by two critic rounds.
- **User (2026-11-10):** "lets try the method.. also ... from each successful game that checks the formula
  try to create 5 variations.. and see what checks the formula and what doesnt".
- **Strict passes after the critic's fixes: 4 of 68** (Hostage Tag; Prop Hunt with forced moves; Cockroach
  Poker; Among Us's Sheriff role), and three of them already exist. Comparing pool A with pool B said
  nothing (B's moves were built to break the formula).
- **What the cuts showed (user's idea):** the part that carries the formula is the search budget, the
  stakes, the traitor, the physics world, the shared quota, split information or silence.
- **The formula can't see the twist:** plain hide-and-seek passes like MECCHA CHAMELEON.
- **Pure co-op rarely passes:** with no human picking the counter, co-op needs a physics world or talk,
  and talk fails the 1 human + 2 bots dev crew. Team games pass more, but at 3 players they are 1 vs 2.
- **Frame (critic r2, checked):** the method is logic-first (the grid makes rules, the formula checks
  rules), so a fantasy added afterwards is the rejected "one seed, derive the other two". Taken to the user.
- **Best surviving family:** split view where you can't see your own (Thin Ice), already built as DRS's
  The Tilt and not yet playtested. Prior art for the round-2 ideas: one search each, not found except
  Mirror Mansion (Horror House on Spook St.).

## 2026-11-10 (evening): method tournament, 2 generations, 126 ideas (AFK, 1 h)
User: "try different agents try diferent methods.. evaluate what what and what doesnt then again try
different methods in parallel.. and survive only those that are checking better against the formula.
also another check is not duplicate an existing idea. dont think about testing yet."
Full write-up: `research_notes/Idea search/tournament/results.md` (target and checks: `formula.md`).
- **Setup:** each method in its own agent (no web while generating), 8 ideas each; ideas shuffled and
  scored blind by 2 formula raters (F1–F7 + co-op gate) and 3 web novelty checkers (N). Gen 2 put 6
  gen-1 ideas back in blind as anchors.
- **Gen 1 (9 methods, 72 ideas):** real-world group work passed 7/8; the old grid and "split one
  thing" came last (3/8). 40/72 pass, 13/72 novel. Novelty checkers differed a lot in harshness.
- **Gen 2 (6 methods, 48 ideas):** 38/48 pass, 20/48 novel; anchors scored the same or lower, so the
  raters didn't go easier. New methods built from what gen 1's scores showed (best pattern, crossover of
  the best ideas, crossing the best two methods) beat the reruns of gen 1's winners, which repeated
  their own ideas.
- **No idea passed every check (0 of 126).** F7 tail blocks almost all: physical coordination ideas
  settle into one routine. Claude's synthesis [opinion]: F3 and F7 fail together, because once a crew
  finds a protocol, coupling turns into obeying it and replay into the same routine; "friends are always
  unique" needs rules that leave friends room to differ.
- **Unscored risk [assumed]:** gen 1's best pattern (two actions meeting in the same instant) carries
  lag risk online (~30 rater flags in gen 2).
- **The "help only others, never yourself" family (The Tilt, Thin Ice) is taken** (Hanabi, Watch My Step!).
- Best ideas: Bull Relay, Striking Gang, Bed Board Tunnel, Ore Carts, Stone on Rollers, Trapper Doors,
  Salt Flat Crossing, Balloon Basket, Heavy Boots (all 16–17 of 18, novel, F7 ~).

## 2026-11-10 (night): idea loop run 1 with the new skill (AFK, 1 h)
User: "create a skill for generating ideas" (create / check / improve the method), then "proceed to again
generate ideas for 1 hour". Skill: `~/.claude/skills/generate-ideas`. Write-up:
`research_notes/Idea search/loop1/results.md`.
- **Failure research first (web, sourced in `loop1/research/`):** real player-with-player interaction means
  my act lands on one named friend, they answer within seconds, and it can help or hurt them; a shared object
  is fine, pooling and parallel work are the failures (Depping & Mandryk 2017; Reuter et al. 2014; Cook).
  A plan stays fresh only if something revealed in the round changes *which* plan is best; physics wobble
  doesn't (Elias, Garfield & Gutschera); co-op is prone to limited replay without an opponent or a
  director (Booth, Left 4 Dead).
- **Round 1 (6 methods, 48 ideas, research-based gates):** 10 pass with no ✗, 0 with no ~. All 6 earlier
  best ideas fail the new gates; Megalith Haul fails player-with-player, as the user sensed. Top failures:
  by round 5 one end only obeys (19), the threat is beaten by one lookup line (18).
- **Best:** Hooked on Friends (grapple sticks only to teammates; whoever is braced stays, the other is
  reeled in), reached by 3 methods; novelty ~ (ally hooks in Dota, Heave Ho).
- **Web search budget:** 200 calls per session shared by all agents ran out at the start of round 1, so
  novelty is mostly unchecked and round 2's failure research couldn't search.
- **Round 2 (4 methods × 6, sharpened gates):** 3/24 pass. Two-sided information did best (Glowball: the orb
  holder sees only the hounds, the others only the goals, a catch flips it). A threat that searches by noise
  failed (beaten by a decoy). "No fixed plan" is the wall, and raters agreed on only 67% of shared checks.

## 2026-11-10 (late): fantasy-first run 1 (skill rebuilt: fantasies → why interact → formula, no subagents)
User: "the skill now should not work with multiagent.. should do first: list of fantasies, reason of why
interact with other player, check against the formula", then "proceed". Write-up: `research_notes/Idea search/fantasy1.md`.
- 16 fantasies, each with a growing pressure that only a friend can relieve. 11 stopped at "no fixed plan":
  moving a resource or rescuing settles into rotate / share evenly / nearest helps.
- Survivors (all ~ on "no fixed plan"): Werewolf Pack, Coven, Plague Doctors, Possession. Shared trait: the help
  moves the harm onto the helper, so the crew's own choices change each round.
- Not blind (Claude wrote and scored); novelty web-checked for 3 survivors only.
- 2026-11-10 late: fantasy-first run 2 (`research_notes/Idea search/fantasy2.md`): 5 of 16 passed; the early probe dropped 8 to one-line plans; survivors cluster on "restrain a struggling friend, harm spreads"; new shape: a harm that changes how you behave (Sin Eaters).
- 2026-11-10 late: fantasy-first run 3 (`research_notes/Idea search/fantasy3.md`): 6 of 15 passed, all ~ on "no fixed plan"; new attractor "pass a behavior curse by helping"; the fantasy stage can't pass that check without a rule.
- 2026-11-10 late: second pass on the 16 passing lines (`research_notes/Idea search/passing-lines.md`): vague words replaced by physical actions; 7 ideas got stronger on a recheck (Coven now acts on a friend, Sleepwalkers' sleeper got a job, Burning Set's force fixed).
- 2026-11-11: idea pool cycle 1 (`research_notes/Idea search/pool.md`): 4 of 4 failures fixed, 5 improved, 3 added (1 passed); skill now runs as a living pool and changes itself, measured each cycle (`~/.claude/skills/generate-ideas/lessons.md`).
- 2026-11-11 00:26 · Idea pool cycle 2 (`research_notes/Idea search/pool.md`): 19 pass, 8 failed; content fixes by freezing the opposition; new shapes W (Midas) and U-by-physics (Zero-G); rule step shows every idea has a short plan card, so the check now asks whether crew-made state breaks it.
- 2026-11-11 00:33 · Idea pool cycle 3: 22 pass, 10 failed, 2 dropped (Lifeboat, Cursed Gallery); the rule step demoted Hypnotist's Show; 3 new daytime passes (Scrap Robots, Helium Clowns, Living Dough Bakers); T became a second attractor.
- 2026-11-11 00:39 · Idea pool cycle 4: 23 pass as 12 cores (3 cores hold 14 ideas); 1 of 6 new passed (Fever Visions); memory-made fantasies are running out of new cores, so the skill now draws half its fantasies from researched folklore and jobs.
- 2026-11-11 00:43 · Idea pool cycle 5: 24 pass as 13 cores; Swap Wizards is a new core; new cores come from new friend-verbs, not new harms; the folklore-sources change was reverted (0 of 4 passed).
- 2026-11-11 00:45 · Idea pool cycle 6: 25 pass as 14 cores; Hermit Crabs (real vacancy chain) is a new core; about 1 new core per cycle whatever the method; verb-first reverted; scene step added.
- 2026-11-11 00:48 · Idea pool cycle 7: 26 pass as 15 cores; scenes at 3 and 6 players found a hole in 4 of 4 ideas (mostly a solo way out); Harbor Jam new core; checks now ask for solo exits.
- 2026-11-11 00:51 · Idea pool cycle 8: 27 pass as 16 cores; scenes found 4 more holes, mostly one player soaking up everything (cap added to checks); spatial couplings hold up best; Egg Ledges new core.
- 2026-11-11 00:52 · Idea pool cycle 9: 28 pass as 17 cores; scenes found 2 safe spots, a dump and a free harm (all fixed); Storm Sailors new core (your work sweeps a friend); safe-spot sweep added.
- 2026-11-11 00:55 · Idea pool cycle 10: 28 pass as 17 cores + 13 skins; sweeps and scenes found 8 holes (all fixed); 0 new cores in 6 (saturated, skins on spatial cores); sweeps now re-run every probe lesson on old passes.
- 2026-11-11 00:57 · Idea pool cycle 11: 28 pass as 17 cores + 14 skins; 6 holes fixed by sweep and scenes; hit-game verbs (pull up, carry, hand off) gave 0 new cores: the formula asks for acts that help one friend and cost another, which the hits mostly lack.
- 2026-11-11 00:59 · Idea pool cycle 12: 28 pass as 17 cores + 16 skins; scenes on the last skins fixed 5 holes (3 were dice rolls hidden in words like 'risk' and 'may'); new domains gave 0 new cores; best version picked per core.
- 2026-11-11 01:01 · Idea pool cycle 13: 28 pass as 17 cores + 17 skins; the sweep fixed 3 impossible goals and 3 hidden dice rolls; novelty: 3 themes already on stores (grave robbing, plague curing, dough baking); 0 new cores from playground games.
- 2026-11-11 01:03 · Idea pool cycle 14: long scenes (rounds 1, 5, 20) showed all 3 top spatial cores settling into a habit by round 20; fixed with dealt rigging, two-wizard islands and tide-thrown seaweed; 4 skins, 0 new cores.
- 2026-11-11 01:04 · Idea pool cycle 15: long scenes on Zero-G, Egg Ledges, Harbor Jam each settled by round 20 (solo return, moving as a block, a quarterback), all fixed; by round 20 a crew avoids the coupling or scripts it; step 3 switched to writing skins after 5 cycles of 0 new cores.
- 2026-11-11 01:05 · Idea pool cycle 16: long scenes on cores 1–3's best versions found 3 more round-20 habits (9 of 9 so far), one created by an earlier fix; skin lines for core 16.
- 2026-11-11 01:05 · Idea pool cycle 17: long scenes on Coven, Vampire Family, Possession found round-20 habits (12 of 12 so far), all fixed; skin lines for core 11; the skill now rechecks that the job pulls the danger after fixes.
- 2026-11-11 01:07 · Idea pool cycle 18: 29 pass as 18 cores; long scenes found habits in Plague Doctors, Midas, Sandstorm (15 of 15 so far), all fixed; new core Gear Tower Mice (my steps turn your gear).
- 2026-11-11 01:08 · Idea pool cycle 19: every core has now been played to round 20 and fixed; Gear Tower Mice's whole-clock coupling was a pile (fixed with short trains); mechanisms gave 0 new cores.
- 2026-11-11 01:09 · Idea pool cycle 20: second long scenes on 4 fixed cores: 2 fixes held, 2 showed new holes (free swaps, a gull beat), fixed; the skill now replays a long scene after each fix, up to 3 times.
- 2026-11-11 01:10 · Idea pool cycle 21: third looks held; second looks fixed 3 more holes (optional coupling, free passing spots, a state lookup); 0 new cores from everyday places.
- 2026-11-11 01:11 · Idea pool cycle 22: second looks fixed 3 more (even sharing, a ring, a lookup); ranked the pool: top 5 Storm Sailors, Hermit Crabs, Swap Wizards, Zero-G Salvagers, Sin Eaters.
- 2026-11-11 01:12 · Idea pool cycle 23: second looks mostly hold (1 hole fixed); core 17 is in the friendly-fire family (Magicka, Helldivers 2); no hermit-crab chain or boom-sweeping game found; 0 new cores.
- 2026-11-11 01:14 · Idea pool cycle 24: starting from 'my X does Y to you' gave 2 new cores in 6 (Storm Gaze Sorcerers: my gaze holds you; Banshee Sisters: my voice pushes you); 31 pass as 20 cores.
- 2026-11-11 01:15 · Idea pool cycle 25: 'my X does Y to you' again gave 1 new core (Escher Burglars: my gaze sets your gravity) and 3 skins; 32 pass as 21 cores.
- 2026-11-11 01:16 · Idea pool cycle 26: long scenes fixed round-20 habits in the 3 newest cores; relation-first gave 0 new cores this time (2, 1, 0).
- 2026-11-11 01:17 · Idea pool cycle 27: relation-first ran dry (2, 1, 0, 0); every source gives 1–2 new cores then skins; 3 skin lines for Hermit Crabs (Moving Day, Royal Court, Nest Boxes).
- 2026-11-11 01:19 · Idea pool cycle 28: third looks on 10 cores found 6 new holes (unsaid rule corners and 'the least X helps'), fixed by making the harm also the power.
- 2026-11-11 01:20 · Idea pool cycle 29: fourth looks found nothing new; 2-hour run ends with 32 passing ideas in 21 cores, ranked (top 5: Storm Sailors, Hermit Crabs, Swap Wizards, Zero-G Salvagers, Sin Eaters); all sources of new fantasies saturate after 1–2 cores; long scenes with repeated looks were the most productive check.
- 2026-11-11 01:20 · Idea pool cycle 30: fantasies in the user's own game worlds gave 0 new cores; run stopped at 1h10m because new sources and word-checks had both converged.
- 2026-11-11 01:24 · Idea pool cycle 31 (user AFK): all 32 backlog fantasies retried with this run's fixes: 0 new cores, 13 skins, 17 dropped; the 21 cores look like most of what the checks let through.

## 2026-11-11: why the pool's ideas feel like Mario Party minigames (user's question)
User: "most games feel like a mario party minigame.. instead of being a full game.. and i dont know why".
Tags: [source] web; [read] Claude read the skill's checks / this file's earlier tables; [opinion] Claude's reading.
- **What a Mario Party minigame is:** one arena, one verb, learned in seconds, short rounds; the board (coins →
  stars) is what gives it stakes [source: Wikipedia "Party video game"]. A minigame plays apart from the game's
  core loop and is optional [source: DiGRA paper, dl.digra.org/index.php/dl/article/download/1911/1910].
- **What the pool's ideas are:** one arena, one rule (≤ 2 extra), one repeated "X, or Y" choice, a goal of the form
  "before Z happens", nothing carried into the next round [read: SKILL.md C, checks.md 2–3]. The same shape.
- **What the short-dev hits add on top of their hub** [read: the 2026-11-09 tables above; LC quota from Wikipedia]:
  a stake that carries across rounds and grows (Lethal Company's quota every 3 days, rising; Content Warning's
  3-day views target; Gamble With Your Friends' daily quota; R.E.P.O.'s quota); a slower choice between rounds
  (which moon, when to go back, what to buy); 4–8 systems around the hub; generated places instead of hand-made
  levels (procedural facilities, PEAK's daily mountain [source: co-optimus / gamesradar Peak pieces]).
- **Theory** [source, practitioner opinion, no controlled evidence]: the core loop holds a player for minutes, the
  loop across sessions for months (GameAnalytics core-loop articles); fun stops once the pattern is learned, so one
  rule is learned fast (Koster, Theory of Fun); "fun at first but gets old quickly" means the mechanic needs depth
  (Stout, Game Developer "Evaluating game mechanics for depth"); changing the setting adds no depth, like a reskin
  (Hayward, Game Developer "System fatigue").
- **Why the method makes minigames** [read + opinion]: (1) "≤ 2 extra rules" caps the number of nodes, which is
  scope, not coupling (the user's graph model keeps them apart; the hits have 4–8 nodes with few connections);
  (2) "not a place to reach" also bans generated places, the hits' cheapest outer structure (PEAK, Chained
  Together, RV There Yet?); (3) the [job] [choice] [goal] line has no slot above one round; (4) the player gate
  dropped the hits' own couplings: Danger Vloggers (Content Warning's filming), Downed Carriers (carrying a fallen
  friend), Vase Movers (R.E.P.O.'s shared carry), tied-together (Chained Together). So the friend act must carry
  the whole game alone, which is what a minigame does; (5) 60 fantasies on 21 rules read as a minigame collection.
- **Not checked:** that the missing between-rounds layer is the main cause of the feeling (no play, no players).
- **Recommendation [opinion]:** keep the cores as hubs; give each idea a between-rounds line (what carries over and
  grows, and the slower choice it creates); let the systems count rise to the hits' 4–8 as long as each only acts
  on the hub; allow generated places. Sketch the skill change before editing it.

## 2026-11-11: what makes trouble funny instead of just difficult (user's question)
User: "what makes a situation just difficult vs a situation funny from friends?"
Tags: [source] web; [opinion] Claude's reading; no play test.
- **Benign violation theory** [source: McGraw & Warren 2010 Psych. Science; Warren & McGraw 2016 JPSP, 6 studies,
  beat plain incongruity at telling funny from not funny]: funny = something seems wrong and okay at the same time.
  Ways it becomes okay: it's clearly play, you don't care much about the rule broken, or it happens at a distance
  (to someone else). Slapstick: we laugh because the hit person isn't really hurt. Humour in general, not games.
- **Bodies** [source: Douglas Wilson on Johann Sebastian Joust, Game Developer]: motion control is "the slapstick
  comedy of games"; players "look ridiculous", others in the room laugh.
- **Voice** [source, reviews = opinion]: Lethal Company's comedy is credited to proximity voice (a dead player is cut
  off; a shriek fades into the distance).
- **Low stakes** [source: Landfall in Game Developer]: "If everyone doesn't take the game so seriously we can have a
  lot more fun with it".
- **Jokes wear out** [source: Zoe Quinn GDC 2015, via Game Developer]: "You can only test a joke once."
- **Context changes laughter** [source: Rychlowska et al. 2022, 50 pairs of strangers]: more laughs in a co-op quiz
  than a competitive one, but more in a competitive timed chip hunt than a co-op one. Small study.
- **Levers for games [opinion]:** wrong = a surprise, shown on a body, caused by a person you can see; okay = cheap for
  the one it happens to (or they still get to talk and play), and someone not in the trouble is watching. Just
  difficult = the cause is a number or a timer, the victim loses a lot and goes quiet, everyone is too busy to watch,
  or the same failure repeats until it's predictable.
- 2026-11-11 · Over-the-match test lines for Storm Sailors, Hermit Crabs, Swap Wizards (rising crew-made stake, 1 rule each; inline critic fixed a vague trigger and a death spiral): `research_notes/Idea search/fix-minigame-feel.md`.

## 2026-11-11: Full Moon (user's idea) researched and polished
User's idea: friends in a mansion on a full moon; random players start turning into legendary creatures; diagnose them
with tools and cure them, or knock them out to slow it; a fully turned friend must catch someone or die. Research
(Phasmophobia evidence, Deceit, R.E.P.O. dead downtime, PEAK carrying) with sources: `research_notes/Full Moon/research.md`.
Four isolated critic rounds; the design sketch is `research_notes/Full Moon/design.md`. Main turns: signs split between
the patient (inner) and the watchers (outer); every sign rules out one creature; cure odds slide every second; a wrong
cure jumps the case 25 s; tricks, scars and the garden's cold as look-alikes; 5 nights with shared candles (Claude's
recommendation, bends the user's one-night pillar). Not played.
- 2026-11-17 · AFK fantasy marathon (fantasy, feelings, research, choices): nine ideas, four isolated critic rounds, none passed; the pool's top core Storm Sailors failed its first isolated critic: `fantasy-marathon-2026-11-17/HANDOFF_fantasy-marathon.md`.
