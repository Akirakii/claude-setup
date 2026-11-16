# Idea search, round 1 (2026-11-10)

User's ask (2026-11-10): "lets try the method.. also another idea i have is from each successful game
that checks the formula try to create 5 variations.. and see what checks the formula and what doesnt".

Method (agreed 2026-11-09/10): many whole ideas spread across the grid, cut with the formula checks,
critic round, 3 to a weekly side-by-side session with friends, each with a kill line.
- **Pool A (twists first):** written from the grid's cells (what ties players together × what reacts),
  without picking a game to vary. Fixation fix (Jansson & Smith 1991, research.md). Caveat: Claude had
  already read the hits, so pool A is "not built from a hit", not truly blind.
- **Pool B (user's idea):** 10 hits that pass or nearly pass the formula, 5 variations each, one per move:
  **S** swap the action (keep the pair) · **C** move the column · **R** add one row (one more tie) ·
  **X** combine with another hit · **−** cut one thing (shows which part carries the formula).

Tags: every check is [opinion, Claude]. Prior art is [from memory] unless a link is given.
✓ pass · ✗ fail · ~ borderline · n/a.

## The formula checks (user's formula: "low content, low coupling but only high coupling on players")
- **F1 content:** a human or physics picks the counter, and 10 fresh rounds need ≤ 3 arenas + one short list.
- **F2 feature coupling:** the rule fits in one sentence; ≤ 2 rules on top of the hub; nothing rewrites the hub.
- **F3 player coupling:** my best move changes with what another player just did, through different
  actions that fail without each other (not a pooled sum, DRS anti-pattern #12); both ends decide (gate 7).
- **F4 blame:** one visible body fails, in the moment.
- **F5 crew:** works at 3 and at 6 (odd sizes included).
- **F6 hidden:** if something is hidden, there is a counter verb and a reason to hide it.
- **T test crew (practical, not formula):** 1 human + 2 bots can run the rules (no voice-only part).
  Bots never check fun (design-anti-patterns 23).

Shape: **co-op** · **semi** (co-op with a private stake or traitor) · **teams** (friends split into two
sides) · **FFA** (everyone for themselves).

## Pool A: twists from the grid (18)

| # | Name | One-sentence rule | Cell (row × column) | Hidden thing / tie | Shape | F1 | F2 | F3 | F4 | F5 | F6 | T | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Sardines | One player hides; each seeker who finds the spot must squeeze in and hide there too; the last one still searching loses. | hidden × bodies × rival | the spot; each finder's body makes it bigger | FFA | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | old party game; at 3 it ends fast |
| A2 | Statues | Hiders may move only while no seeker is looking at them; a seeker who sees a statue move tags it. | hidden × timer × rival | which statues are players; the seeker's gaze is the hider's clock | teams | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | playground "Statues"; the gaze rule exists as AI monsters |
| A3 | Smuggle | One team passes a single item hand to hand in a crowded room; inspectors get 3 frisks a round to find who holds it. | hidden × handoff × rival | who holds it; every pass is a visible risk | teams | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | "button, button, who's got the button" |
| A4 | Limbs | Each player controls one limb of one shared creature that must climb out. | bodies × teammate × physics | one body | co-op | ~ | ✓ | ✓ | ✓ | ~ | n/a | ~ | courses = content; 6 limbs gets mushy; bots as limbs are hard |
| A5 | Echo | Seekers are blind and see only the rings hiders make when they move; hiders must cross the map. | split info × rival | position | teams | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | hiders act side by side (anti-pattern 24) |
| A6 | Lifeline | One player hangs on a rope and grabs loot; the holders raise and lower but can't see down. | split info × teammate × physics | — | co-op | ~ | ✓ | ✗ | ✓ | ✓ | n/a | ✗ | holders only obey (gate 7); voice-only cue |
| A7 | Lantern | The crew shares one light; only lit ground is visible. | shared object × world | — | co-op | ✗ | ✓ | ✗ | ✓ | ✓ | n/a | ~ | one seat holds the cue; monsters = content |
| A8 | Pickpocket Party | In a crowd of look-alike guests, each player lifts a token from one secret target while guarding their own. | hidden × bodies × rival | who targets whom, who is a player | FFA | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | The Ship (2006), AC Brotherhood "Wanted" |
| A9 | Two Halves | Each player sees the safe tiles for a friend, never their own. | split info × teammate | own safe tiles | co-op | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✗ | voice-only with bots; near DRS Blind Floor |
| A10 | Heist Split | The crew robs one vault; each keeps only what they carry out; the alarm ends it for all. | shared pot × teammate × physics | greed is visible; loot is private | semi | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | vaults = content; R.E.P.O. family |
| A11 | Ventriloquist | Your voice comes out of a random teammate's body; seekers hunt the speaker. | split info × rival | whose voice | teams | ✓ | ✗ | ✓ | ~ | ✓ | ✓ | ✗ | voice-only; mapping is confusing |
| A12 | Elevator | The crew rides one lift with a weight limit; each secretly carries loot weight. | shared pot × teammate | who is heavy | co-op | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | pooled sum + "who did it" in pure co-op = round-1 failure |
| A13 | Hostage Tag | A tagged player is carried by the tagger and can still grab things or trip them. | bodies × rival | — | teams | ✓ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | carry exists in Gang Beasts, DbD |
| A14 | Decoy Escort | One team escorts a VIP who looks like every guest; guarding the VIP too closely gives them away. | hidden × bodies × rival | who the VIP is; protecting reveals it | teams | ~ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | VIP modes (CS as_ maps), Hidden in Plain Sight |
| A15 | Cuffed Tag | Teams of two, cuffed together, play tag. | bodies × rival | — | teams | ✓ | ✓ | ✓ | ✓ | ✗ | n/a | ✓ | odd crews leave one solo |
| A16 | Trust Fall | Players fall off ledges at will and must be caught by a friend. | bodies × teammate × physics | — | co-op | ✗ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | needs levels |
| A17 | Mole Map | Each player draws part of the map from memory; one secret mole draws it wrong. | split info × traitor | the mole | semi | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✗ | bots can't draw |
| A18 | Tripwire | Defenders secretly place 3 tripwires in a room; runners must cross. | hidden × rival (players build the traps) | trap spots | teams | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | traps for each other (Ultimate Chicken Horse) |

Pass all six formula checks + T: **A1~, A2, A3, A8, A13, A14, A18** (7 of 18; A1 borderline at 3).

## Pool B: 5 variations of 10 hits (50)

Hits picked: pass or nearly pass the formula in research.md (2026-11-09 tables). R.E.P.O. and Gamble
With Your Friends are near-passes (medium content), kept to see if a variation lowers content.

| # | Hit · move | One-sentence rule | Shape | F1 | F2 | F3 | F4 | F5 | F6 | T | What it shows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B1 | MECCHA · S | Hiders sculpt their body (stretch, squash, bend) to match furniture shapes. | teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | new action, same pair: passes |
| B2 | MECCHA · C | The crew hides from an AI seeker. | co-op | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | AI counter = content; hiders side by side |
| B3 | MECCHA · R | You can't paint yourself: a friend paints you while you paint them. | teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | adds coupling inside the hider team |
| B4 | MECCHA · X Liar's Bar | A seeker who points at the wrong prop faces the roulette. | teams | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | stakes on the search budget |
| B5 | MECCHA · − paint | Plain hide-and-seek with a fixed look. | teams | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | **passes without the twist: the formula doesn't see the twist** |
| B6 | Prop Hunt · S | Hiders are sheep in an AI herd; the wolf finds players by how they behave. | teams | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | passes; SpyParty-like |
| B7 | Prop Hunt · C | One player secretly moves 3 props while the others look away; they must spot the changes. | teams | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | finders act side by side |
| B8 | Prop Hunt · R | Every 60 s each prop must move to a new spot. | teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | a timer forces risk; Prop Hunt mods have taunts |
| B9 | Prop Hunt · X Among Us | One prop is secretly on the seekers' side. | teams | ✓ | ~ | ✓ | ✓ | ~ | ✓ | ✓ | 2 rules; at 3 the traitor is obvious |
| B10 | Prop Hunt · − wrong-shot cost | Seekers can hit every prop freely. | teams | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | **the search budget carries it (report check 2)** |
| B11 | Liar's Bar · S | Pass a sealed box, claiming what's inside; the next player accepts or opens it. | FFA | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | that's Cockroach Poker (board game) |
| B12 | Liar's Bar · C | Teammates bluff an AI dealer together. | co-op | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | an AI can't be read; Buckshot is solo for a reason |
| B13 | Liar's Bar · R | Each player sees the card of the player to their left. | FFA | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | partial truth makes calls readable |
| B14 | Liar's Bar · X Chained Together | Everyone is chained on a ledge; a caught liar falls and drags their neighbours. | FFA | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | bluff + bodies |
| B15 | Liar's Bar · − roulette | Bluff and call for points only. | FFA | ✓ | ✓ | ~ | ✗ | ✓ | ✗ | ✓ | **low stakes: lying drops out (report check 3)** |
| B16 | Among Us · S | The impostor swaps bodies instead of killing. | semi | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ~ | rewrites the hub; who is who gets confusing |
| B17 | Among Us · C | No impostor: just tasks. | co-op | ~ | ✓ | ✗ | ✗ | ✓ | n/a | ✓ | **the traitor carries the coupling** |
| B18 | Among Us · R | Every task needs two players (one holds, one works). | semi | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | the impostor fakes partner tasks |
| B19 | Among Us · X Liar's Bar | Instead of a vote, an accuser points; a wrong accusation means the roulette. | semi | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | stakes on accusing |
| B20 | Among Us · − meetings | Anyone can shoot anyone; a wrong shot kills the shooter. | semi | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Sheriff role in Among Us mods |
| B21 | Chained Together · S | Players attract each other like magnets when close. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | climbs = content |
| B22 | Chained Together · C | Two chained teams climb one tower and can cut the other team's chain. | teams | ~ | ~ | ✓ | ✓ | ✗ | n/a | ✓ | odd crews; still climb content |
| B23 | Chained Together · R | Only the bottom player sees the next platforms. | co-op | ~ | ✓ | ✗ | ✓ | ✓ | n/a | ✗ | **one seat holds the cue = quarterback** |
| B24 | Chained Together · X Prop Hunt | All hiders are on one chain and must hide together. | teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | couples the hider team |
| B25 | Chained Together · − climb | Chained on flat ground. | co-op | ✓ | ✓ | ✗ | ✗ | ✓ | n/a | ✓ | **the world (physics climb) is the counter** |
| B26 | RV There Yet? · S | One hot-air balloon: one fires the burner, one works the vents, one drops ballast. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | terrain still content |
| B27 | RV There Yet? · C | Two crews race RVs and can sabotage each other. | teams | ~ | ~ | ✓ | ✓ | ✗ | n/a | ✓ | odd crews |
| B28 | RV There Yet? · R | One passenger is a secret hitchhiker who wants the RV to crash. | semi | ~ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | Feed the Kraken on wheels |
| B29 | RV There Yet? · X Liar's Bar | The driver is blindfolded; the navigator may lie. | semi | ~ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | driver only obeys; voice-only |
| B30 | RV There Yet? · − terrain | A flat road. | co-op | ✓ | ✓ | ✗ | ✗ | ✓ | n/a | ✓ | **the terrain is the counter** |
| B31 | Gamble · S | Instead of chance games, players do physical dares and the team bets on each. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | dares list = content |
| B32 | Gamble · C | Private banks; players lend to each other. | FFA | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | negotiate and betray |
| B33 | Gamble · R | Each player also has a secret personal debt. | semi | ~ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | private stake in the shared bank (report route 2) |
| B34 | Gamble · X Liar's Bar | Wins are claimed, not shown; others may audit a claim. | semi | ~ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | |
| B35 | Gamble · − quota | No shared quota. | co-op | ~ | ✓ | ✗ | ✗ | ✓ | n/a | ✓ | **the quota carries the coupling** |
| B36 | Keep Talking · S | One player operates on a patient; the others read the chart. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✗ | voice-only |
| B37 | Keep Talking · C | One manual reader is a secret saboteur. | semi | ~ | ~ | ✓ | ~ | ✓ | ✓ | ✗ | voice-only |
| B38 | Keep Talking · R | The defuser must hold wires with both hands while a reader points. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✗ | |
| B39 | Keep Talking · X Statues | The defuser may touch the bomb only while the reader isn't looking. | co-op | ~ | ~ | ✓ | ✓ | ✗ | n/a | ✗ | 2-player shape |
| B40 | Keep Talking · − manual | The defuser sees everything. | solo | ✓ | ✓ | ✗ | ✗ | ✗ | n/a | ✓ | **split information carries it** |
| B41 | The Mind · S | Players step onto numbered tiles in rising order, without talking. | co-op | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | physical, so bots can play |
| B42 | The Mind · C | One hidden player tries to break the order. | semi | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | |
| B43 | The Mind · R | One shared token passes hand to hand in rising order. | co-op | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ~ | |
| B44 | The Mind · X Chained Together | Chained players must step onto tiles in order. | co-op | ~ | ~ | ✓ | ✓ | ✓ | n/a | ✓ | |
| B45 | The Mind · − silence | Players may talk. | co-op | ✓ | ✓ | ✗ | ✓ | ✓ | n/a | ✓ | **the narrow channel carries it** |
| B46 | R.E.P.O. · S | The monsters are the other team, who steal your loot. | teams | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | **a human counter drops the content (column rule)** |
| B47 | R.E.P.O. · C | One carrier is secretly a thief who pockets value. | semi | ~ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | monsters still content |
| B48 | R.E.P.O. · R | Valuables only count if two players carry them out. | co-op | ~ | ✓ | ✓ | ✓ | ✓ | n/a | ✓ | |
| B49 | R.E.P.O. · X Prop Hunt | Some loot is players in disguise; carriers must find and drop the fakes. | teams | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | |
| B50 | R.E.P.O. · − monsters | Physics carrying + quota, no monsters. | co-op | ✓ | ✓ | ~ | ✓ | ✓ | n/a | ✓ | threat gone; needs a timer |

## What the checks show [opinion; counted by script from the tables above]

- **Pass rate, every check ✓ (or n/a):** pool A **6 of 18 (33%)** · pool B **8 of 50 (16%)**.
  Counting ~ as a pass: pool A 10/18 (56%), pool B 31/50 (62%).
  - Pool A strict passes: A2 Statues, A3 Smuggle, A8 Pickpocket Party, A13 Hostage Tag, A14 Decoy Escort, A18 Tripwire.
  - Pool B strict passes: B5, B6, B8, B11, B20, B24, B41, B43. **Three already exist as games:** B5 is plain
    hide-and-seek, B11 is Cockroach Poker, B20 is the Sheriff role from Among Us mods. That fits the
    fixation risk: variations of hits drift back into known games.
  - Caveat: Claude wrote and rated both pools, so the rater may favour its own twists.
- **By move (pool B, strict / with ~, of 10):** S 3/8 · C 0/4 · R 2/8 · X 1/8 · − 2/3.
  - **C (move the column) never passes strictly:** an AI counter brings content back (B2, B12); pure co-op
    removes the coupling (B17). The best C-like change went the other way: R.E.P.O.'s monsters became
    the other team (B46, F5 ~).
  - **− (cut) teaches the most:** each cut names the part that carries the formula: search budget (B10),
    stakes (B15), traitor (B17), the physics world (B25, B30), the quota (B35), split info (B40),
    silence (B45).
- **The formula can't see the twist.** Plain hide-and-seek (B5) passes as well as MECCHA. The twist needs
  its own check (the next-game-report's 5-second clip).
- **Pure co-op rarely passes.** Strict co-op passes: B41, B43 (both The Mind family). With no human picking
  the counter, co-op needs a physics world (content ~) or talk (voice fails the test crew). Most passes are
  **teams**. Whether friends split into teams counts as the user's "co-op" is the user's call.
- **Same hidden thing, different skin:** many passes hide *which body is a player* (A2, A8, B1, B3, B6) or
  *where someone is* (A1, B5, B24). Per the critic lesson, each group is one family.

## Prior art for the shortlist (web, 2026-11-10; one search each, absence is not proof)
- **Statues:** not found with human players. The rule exists for NPCs and monsters (MineFun NPCs move when you
  look away, [guide](https://minefun-f0j.pages.dev/guides/hide-and-seek-guide); Weeping Angels [from memory]).
- **Smuggle:** close: Airport Security Sucks! (one player is a TSA agent hunting smugglers who blend in;
  search summary only); Checkpoint, a 10–40 player street game of smugglers and guards
  ([ludocity](https://ludocity.org/wiki/Checkpoint)); Contraband (1950 card game, [kallax](https://kallax.io/boardgame/B82N1-Contraband)).
  Not found: passing one item among a team under a frisk budget.
- **Decoy Escort:** close: Crossfire (board game: agents protect a VIP, assassins deduce who it is,
  [Plaid Hat](https://plaidhatgames.com/games/crossfire)); Among Us 3D's VIP event
  ([PC Gamer](https://www.pcgamer.com/games/action/among-us-3d-is-adding-a-new-limited-time-feature-i-havent-thought-about-in-20-years-vip-mode));
  players hidden among NPCs: Who Is Real, Assassins Arena (search summary only). Not found: a crowd-VIP
  escort where guarding gives the VIP away.
- **Tripwire:** close: Trapper's Delight (everyone builds traps, then everyone runs; symmetric,
  [rawg](https://rawg.io/games/trappers-delight)); Oh Trap! ([rawg](https://rawg.io/games/oh-trap)).
- **Chain-gang hiders:** not found (physics hide-and-seek exists: Kick and Hide, 2026,
  [dekudeals](https://www.dekudeals.com/items/kick-and-hide)).
- **Silent steps:** The Mind has an official app with online play (search summary only); a physical
  tile version not found.
- **Secret debts:** Gamble With Your Friends has one shared bank and no personal wallet
  ([allkeyshop](https://www.allkeyshop.com/blog/gamble-with-your-friends-shared-debt-lb/)); no secret debt found.

## Shortlist for the critic (thesis, Claude)
Picked: passes all checks (or one ~, named), one per family, physical so bots can run the rules.

| # | Name | One-sentence rule | Hidden thing (family) | Shape | Smallest test |
|---|---|---|---|---|---|
| 1 | Statues (A2) | Hiders may move only while no seeker is looking at them; a seeker who sees a statue move tags it. | which statue is a player (identity) + gaze as the clock | teams | a gallery room, 10 statue poses |
| 2 | Smuggle (A3) | One team passes a single item hand to hand in a crowded room; inspectors get 3 frisks a round to find who holds it. | who holds it (possession) | teams | one room, one item |
| 3 | Decoy Escort (A14) | One team walks a VIP who looks like every guest to the exit; attackers get one shot; guarding too closely gives the VIP away. | who the VIP is (identity, protecting reveals it) | teams | one plaza, an NPC crowd |
| 4 | Tripwire (A18) | Before each round the defenders secretly place 3 tripwires; the runners must cross the room. | where the traps are (location, made by players) | teams | one room, one trap type |
| 5 | Chain-gang hiders (B24) | All hiders are on one physics chain and must hide together. | where the hiders are (location) + one body tie | teams | Prop Hunt-style room + a chain |
| 6 | Silent steps (B41) | Players step onto numbered tiles in rising order without talking. | nothing hidden; the narrow channel (timing) | co-op | one floor of tiles |
| 7 | Secret debts (B33) | The crew shares one bank and quota; each player also owes a secret personal debt. | each player's private stake (goals) | semi | F1 ~: needs a few money games |

Kill lines and cheapest tests come after the critic.
