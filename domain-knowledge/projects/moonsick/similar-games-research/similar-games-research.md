# Similar games: who succeeded, why, and what Moonsick takes (2026-11-16)

**The general patterns and their sources moved up to `~/.claude/domain-knowledge/shared/game-market/friend-group-party-games.md` (2026-11-16); what stays here is what was specific to Moonsick.**

Brief: `BRIEF_similar-games.md`. Short version: `REPORT_similar-games.md`.
Tags: [source] = said by the linked source; [read] = Claude's reading across several sources; [opinion] = Claude's view;
(memory) = from Claude's memory, not searched this session. Numbers are third-party estimates unless the developer said them.

## What each game means for Moonsick
- **Lethal Company:** same "friends panicking together, then laughing at the death" feeling; Moonsick's threat is a friend, not an AI.
- **R.E.P.O.:** the closest look: a mansion, physics slapstick, items you carry and drop, 6 players.
- **Peak:** proof that a jam-sized scope sells if the friend comedy is there.
- **Content Warning:** the free launch day is a marketing pattern Moonsick can copy; the in-game camera is built-in streamability.
- **Among Us:** short rounds, one hidden threat, cheap, playable by anyone in seconds. Dead players still do tasks as ghosts (memory).
- **Goose Goose Duck:** proximity voice turns a known formula into a stream hit.
- **Deceit / Deceit 2:** the closest theme (a human who turns into the monster) and the clearest failure: it needed strangers to fill lobbies.
- **Evolve:** a warning against giving the werewolf its own game. Moonsick's werewolf uses human movement, sped up, which is the safer side of this.
- **Friday the 13th: The Game:** the same 1 vs 7 shape and a mansion-camp chase; it died from a licence and servers, not the design (opinion).
- **Secret Neighbor:** very close shape (a house, items to gather, one friend is the monster); a steady mid-seller, never a hit.
- **Murder Mystery 2:** the most played 1-vs-many game found; rounds of a few minutes and a random murderer each round (memory on round length).

## 4. How this fits Moonsick's limits

Limits from the user: co-op chosen, 4–8 friends, host on a friend's PC (no cloud), ship in under a year with ~3–4 months
of scope, prove the fun in days (`game-scope-lessons.md`).

| Pattern | Fits 4–8 friends? | Fits no servers? | Fits ~3–4 months scope? | Moonsick has it now? |
|---|---|---|---|---|
| Proximity voice | ✅ | ✅ | ✅ | ✅ voice is in the code map (project CLAUDE.md) |
| Friends on one side vs a threat | ✅ | ✅ | ✅ | ✅ in the hunt only; the race is FFA |
| Rounds of a few minutes | ✅ | ✅ | ✅ | ✅ ~7 min (4 + 3) |
| $5–10 price + free launch day / sale | ✅ | ✅ | ✅ | ❌ not decided |
| Clip moments (the turn, the eat, the cure) | ✅ | ✅ | ✅ | ✅ highlight reel exists (project CLAUDE.md) |
| Live service of new killers (DbD) | ✅ | ✅ | ❌ breaks scope | ❌ |
| Matchmaking with strangers | ❌ needs a large population | ❌ | ❌ | ❌ |
| Deep asymmetry (Evolve) | ✅ | ✅ | ❌ costly to balance | ❌ (werewolf uses human moves) |

## 5. Recommendations (ranked)

| # | Change | Backed by | Tag |
|---|---|---|---|
| 1 | **Make the hunt the main event and the race a short build-up** (race ~90 s–2 min, hunt 3 min). The hunt is where friends are on one side and the potion needs two stirrers; that's the shape every co-op hit has. | Lethal Company, R.E.P.O., Peak, Phasmophobia (friends vs a threat); Fall Guys, Party Animals (FFA fades fastest); Human: Fall Flat vs Gang Beasts | [read] |
| 2 | **Proximity voice on by default, heard through the mansion's walls.** Keep it in the race and the hunt. | Phasmophobia, Lethal Company, R.E.P.O., Goose Goose Duck | [source] |
| 3 | **Friends-only lobbies, hosted on a friend's PC; no matchmaking.** Bots fill a small group. | Deceit 2, Dread Hunger, Project Winter, Evolve (died without strangers); Dread Hunger, Friday the 13th (servers) | [source] |
| 4 | **Rounds under ~6 min, instant restart from the lobby.** Today 4 + 3 = 7 min; a shorter race gets there. | Among Us, Murder Mystery 2 | [read] |
| 5 | **Give eaten players something to do** besides watching for up to 3 min (e.g. ghosts that nudge rats or ingredients). | Among Us ghosts finish tasks (memory) | [opinion] |
| 6 | **Tune for 4–6 players, allow up to 8.** Hits sit at 4–6; 8 needs a bigger group to gather. | Lethal Company (4), Peak (4), R.E.P.O. (6) | [read] |
| 7 | **Price $7.99–9.99; plan a free launch day or a deep sale with an update.** | Content Warning (free day, still 2.2M sold), Peak ($4.95 sale surge), Among Us (75% sale) | [source] |
| 8 | **Keep the werewolf on the human's systems** (same moves, sped up), and add no separate werewolf levelling. | Evolve | [source] |
| 9 | **Keep the shop cosmetic only and skip deep progression;** plan for waves (updates + sales), not retention. | AppMagic (3% D30 is normal) | [source] |
| 10 | **Make the big moments clip-friendly:** the turn, an eat, the potion throw, a pan to the face. | Lethal Company, Content Warning (built-in camera) | [opinion] |

Scene played for #1 (6 friends) [opinion]: the race runs 90 s of pans and shaves, and one friend turns.
The five humans scatter, shout over proximity voice where the wolf is, and two of them dash for the cauldron.
The werewolf's best play is to hunt the stirrers, and the humans' best play is to guard them, so the hunt's best
play goes through the potion instead of skipping it. If the humans skip the potion and just run, they still have to
outlast a wolf 1.44x faster for 3 min, which holds only for the ones who use the crawl gaps.
