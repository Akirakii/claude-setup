# Next game: what's cheap to make and still pays (report, 2026-11-01)

For a solo dev who wants a game shipped in under 1 year, judged on effort/risk vs return.
Built from 5 parallel research passes plus earlier searches. **Sales are mostly third-party
estimates** (Gamalytic, Raijin, VG Insights, AppMagic, Sensor Tower), often off by 2x or more;
developer-announced numbers are marked *(dev)*. This is a list of survivors: the base rates
below say what usually happens.

---

## 1. Summary

- **The usual outcome is near zero.** About 20,000 Steam releases in 2025; about 66% earned under
  $1,000; about 3% reached 1,000 reviews (roughly $150k gross).
- **Co-op hits are the fastest to make (2–5 months), but almost never by a solo first-timer.**
  They come from 2–10 person teams with earlier games, reused netcode, or an audience. The one
  true solo co-op hit (Lethal Company) came after 19 earlier games.
- **Short single-player hits are often solo,** in 2 weeks to 13 months, and always follow one
  formula: **a proven loop + one twist that reads in a 5-second clip, cheap stylized art, a $3–10
  price, and a demo or itch build before launch.**
- **Co-op sells more per hit and has a longer tail** (3.5x first-week copies in year one vs 2.5x),
  but has the worst retention (D30 ~3%) and adds netcode, griefing and hacker work. Solo devs
  report multiplayer makes everything take "5 times as long".
- **Almost every "quick" hit sat on years of practice.** The repeatable strategy is several
  small, cheap games, each killed or kept based on demo response, not one big bet.
- **Best genres for you (solo, <1 yr, gamepad):** survivors-like with a twist,
  Balatro-like "toy" roguelike, short anomaly/one-room horror. Avoid: puzzle, platformer, tower
  defense, extraction, farming/life sim, solo friendslop.

---

## 2. Base rates (what usually happens)

| Measure | Value | Source |
|---|---|---|
| Steam releases 2025 | 20,282 | howtomarketagame (HTMAG) |
| Share that reached 1,000 reviews | ~3% | HTMAG |
| Share earning under $1k | ~66% | wnhub / VG Insights write-up |
| Median Steam game revenue | ~$250 (2025) to ~$1,100 lifetime (2019 cohort) | 80.lv, Zukowski |
| Year-1 copies vs week 1 | co-op 3.53x, non-co-op 2.5x | GameDiscoverCo |
| Median co-op game vs median single-player game | ~6x the sales (estimate) | VG Insights |
| Friendslop retention | D1 ~20%, D7 ~4%, D30 ~3% (Content Warning) | AppMagic |

---

## 3. Co-op games (2023–2026)

| Game | Team | Dev time | Price | Result | Head start they had |
|---|---|---|---|---|---|
| MECCHA CHAMELEON | 2 | ~2 mo core, 4–5 with reuse | $5.99 | 20M in 63 days *(dev)*, ~$66M | ~30 UEFN games, reused assets + backend |
| PEAK | 7 (Aggro Crab + Landfall) | ~1 mo jam + months remote | $8 | 10M+ *(dev)* | two known studios, Content Warning's netcode/ragdolls |
| RV There Yet? | small studio | 8–9 weeks (jam) | $7.99 | 4.5M | studio team |
| Content Warning | 5 (Landfall) | ~2 mo | free 24h, then $7.99 | 6.2M free claims, 2.2M paid | big studio audience |
| Lethal Company | 1 | ~17 mo | $9.99 | 10–19M (est.) | 19 earlier games made for streamers |
| Schedule I | 1 + art help | ~3 yr | $19.99 | ~8M, ~$126M (est.) | ex-Roblox dev; deep sim |
| R.E.P.O. | ~7 | short ("fail fast") | ~$10 | 3–13M (est.) | second game, Photon netcode |
| YAPYAP | ~10 | <1 yr (aimed 3–6 mo) | $10 | 1.15M, ~$10M (est.) | studio, 900k wishlists, TikTok before mechanics |
| How to Fish | 2 | ~1 yr (2022 jam prototype) | €7.49 | >1M in 2 days *(dev)*, 7.9M month 1 | second co-op game |
| Gamble With Your Friends | ~9 | ? | $7.99 | 2M in ~5 weeks | team |
| WEBFISHING | 1 (likely) | ~5 mo from an 8-day jam | $4.99 | 1.3–5M (est.) | Godot + Steam P2P, cozy |
| Liar's Bar | animation studio | ? | $6.99 | ~2.2M (est.) | pro character animators |
| Chained Together | debut team | ? | $5 | claims 10M (unverified) | copied the Only Up! format |

**Per game: what worked / what didn't**
- **MECCHA CHAMELEON:** works: a visual hook you get at one glance (paint yourself to hide),
  very cheap. Doesn't: Workshop malware, Windows only. Lesson: "make it exist first, perfect
  it later" + reuse.
- **PEAK:** works: streamers after launch (only 29k wishlists at launch, store page up 4 days
  before), $5 launch week. Doesn't: share fell from ~50% to ~10% of the genre in months; the
  team chose not to run it as a live service.
- **RV There Yet?:** works: an absurd premise, physics fails make clips. Doesn't: "no clear
  objective" (Metacritic 72).
- **Content Warning:** works: the free day made it top of the charts. Doesn't: traded revenue for
  reach; retention collapsed (D30 ~3%).
- **Lethal Company:** works: proximity voice turns deaths into clips; growth came from streamers
  week by week. Doesn't: one dev couldn't keep up updates; a clone wave followed.
- **Schedule I:** works: a taboo power fantasy plus a real management loop, so it retains.
  Doesn't: 3+ years of work, not a short-dev game.
- **R.E.P.O.:** works: deliberate "fail fast" after a 6-year flop; physics hauling. Doesn't:
  hackers at scale.
- **YAPYAP:** works: voice-cast spells, marketed on TikTok before the mechanics existed.
  Doesn't: "needs more content", shallow spells.
- **How to Fish:** works: game feel, physics chaos, a cheap price. Doesn't: daily peak fell ~94%
  in a month; urgent anti-griefing patches.
- **Gamble With Your Friends:** works: a shared bank account means shared debt, which creates
  drama between friends; positioned as "a finished game, not a live service".
- **WEBFISHING:** works: a cozy social space, solo, Godot. Doesn't: griefing, ~99% fall from peak.
- **Liar's Bar:** works: expressive characters + bluffing need almost no content; streamers took
  it from 2k to 114k CCU. Doesn't: depended on studio-grade animation.
- **Chained Together:** works: a proven rage format + a chain that makes friends blame each
  other. Doesn't: support handed to a publisher.

**Co-op flops:** "dozens" of Lethal Company clones, only R.E.P.O. broke out. Overthrown ($25
complex co-op city builder) peaked at 350 CCU; the same studio's simple $8 Super Battle Golf sold
~800k. Developer quote: "for every successful friendslop game there are 10 no one has heard of".

**Netcode cost for a solo dev:** off-the-shelf stacks exist (Photon for Unity; GodotSteam with
Steam P2P for Godot, no server cost). Still: solo dev of Garden Wars said multiplayer "makes
everything take 5 times as long" (+3–4 months, first MP game). Plus launch-week griefing and
hacker fixes. Has to be in from the first prototype; adding it later costs months.

---

## 4. Single-player games

| Game | Team | Dev time | Price | Result | Head start |
|---|---|---|---|---|---|
| A Game About Digging a Hole | 1 | 2–3 weeks | €4.99 | 1.2M+ *(dev)* | licensed assets, publisher, 100k wishlists |
| Buckshot Roulette | 1 | ~1 mo prototype, 4–7 mo total | $2.99 | 8M+ *(dev)* | many 1–2 month itch horror games |
| Rusty's Retirement | 1 | ~6–9 mo (2-week prototype) | $6.99 | 550k *(dev)*, dev became a millionaire | shipped Haiku the Robot before |
| A Short Hike | 1 (+composer) | ~7–8 mo | ~$8 | ~430k Steam (est.), Switch sold more | years of skill; Humble funded it |
| Vampire Survivors | 1 (+friends) | ~1 yr to EA, £1,100 spent | $2.99 → $4.99 | 6–10M Steam (est.) | first mover |
| Megabonk | 1 | ~13 mo | $9.99 | 1M in 2 weeks *(dev)* | earlier games under other names |
| Nubby's Number Factory | 1 | ~1.5 yr (core loop 2 mo) | ~$5 | ~480k (est., sources conflict) | daily TikTok clips for months |
| CloverPit | 2 | ≤18 mo, "short cycle" | $9.99 | 1M+ *(dev)* | prior game, publisher Future Friends |
| Brotato | 1 | ? | ~$4.99 | 2M+ at 1.0, 10M players | 4th game; earlier potato games |
| Mouthwashing | 5–7 | ~15 mo | ~$13 | 800k+ *(dev)* | publisher, cancelled project reused |
| The Operator | 1 (+contract audio) | ~2.5 yr (est.) | $13.99 | ~158k, ~$1.3M (est.) | 4 years at a studio |
| Peglin | 4 part-time | ~2.5 yr | $17.99 EA | 400k EA year 1 *(dev)* | jam origin, long demo |
| Balatro (reference) | 1 | ~2+ yr part-time | $14.99 | 5M+ *(dev)* | none; outlier |
| Bongo Cat | 2 | weeks | free | huge CCU, $2–4k/month, not profitable | meme |

**Per game: what worked / what didn't**
- **Digging a Hole:** works: the title is the pitch, a satisfying loop, an impulse price. Doesn't:
  52% OpenCritic, no longevity; it's a lottery ticket.
- **Buckshot Roulette:** works: you understand the premise instantly, the tension is great for
  streamer reactions, $3, itch proved it first. Doesn't: thin content (later fixed with a free
  multiplayer update).
- **Rusty's Retirement:** works: a new form factor (sits at the bottom of the screen) in a proven
  genre, launched into Farming Fest, 11 languages, China = 26% of sales. Doesn't: low revenue per
  unit, sales fall fast.
- **A Short Hike:** works: a complete cozy experience at a tiny scope; Switch gave it a long tail.
  Doesn't: depends on craft that's hard to repeat by formula.
- **Vampire Survivors:** works: invented the feel (almost no input, huge power), $3. Doesn't
  apply anymore: the first-mover advantage is gone.
- **Megabonk:** works: proven genre + 3D movement + meme humor; "breaking" builds for streamers.
  Doesn't: only 2 maps, repetitive.
- **Nubby's:** works: daily 7–10 s clips, kept the "broken" builds players loved. Doesn't: week 1
  sold only ~1k before streamers found it; the dev burned out.
- **CloverPit:** works: a familiar object (slot machine), "Balatro meets Buckshot" pitch, a viral
  demo (+100k wishlists in a week), VTubers, refund rate below median. Doesn't: luck feels like
  low agency.
- **Brotato:** works: short dense runs + a shop phase add decisions. Doesn't: post-launch handed
  to another studio.
- **Mouthwashing:** works: a shocking story built for YouTube theories. Doesn't: rests on writing,
  which is the least predictable input.
- **The Operator:** works: all-UI art for a dev who can't draw; a proven deduction niche. Doesn't:
  content is costly, no replay.
- **Bongo Cat:** being popular isn't the same as making money.

**Single-player flops:** survivors-likes reaching 1,000 reviews: 10 (2022), 17 (2023), **1**
(2024); only big twists broke through in 2025. Bramble Royale (deckbuilder): $8k first week,
"no marketable hook", "people are fatigued on deckbuilders". JokerJack: "derivative copycat".
Archetype: Portal to Hell (solo, <1 yr): 24 copies, no hook, store page up only weeks before
launch.

---

## 5. Co-op vs single player, side by side

| | Co-op (friendslop) | Single player (short-dev) |
|---|---|---|
| Typical dev time of hits | 2–5 months | 2 weeks – 13 months |
| Typical team of hits | 2–10, rarely solo | often solo or 2 |
| Size of a hit | 1M–20M | 0.5M–8M |
| Price | $5–10 | $3–14 |
| Long tail | stronger (3.5x) | weaker (2.5x), but ports and DLC help |
| Retention | very poor (D30 ~3%, -90% in months) | roguelikes replay well; story games are one-and-done |
| Extra work | netcode, multiplayer QA, griefing, hackers, lobbies | none |
| Solo-friendly | low (only practised devs) | high |
| Switch / gamepad | poor (PC + Discord) | excellent |
| Marketing engine | streamers, voice-chat clips | streamers, clips, demo, Next Fest |
| Risk shape | rare, huge hits | rare, medium hits |

**Reading:** for a solo dev, single player has the better effort/risk ratio. Co-op's speed comes
from teams and reused tech, which a solo first project doesn't have. Co-op stays an option only as
a tiny jam-sized game built on a Steam P2P template from day one.

---

## 6. Genres ranked for a solo dev, <1 year

Hit rate = share of recent releases reaching 1,000 reviews (two sources, SPA and HTMAG, which
differ; treat as ranges). Effort, risk and Switch fit are judgments, not measurements.

| # | Genre | Hit rate | Effort | Risk | Switch | Note |
|---|---|---|---|---|---|---|
| 1 | Survivors-like / bullet heaven | high (new tag) | low–med | med | excellent | plain clones dead (2024: 1 hit); needs a big twist |
| 2 | Balatro-like / toy roguelike | 5–8% | low art, high design | med | excellent | needs a fresh "toy" (slots, dice, pachinko) |
| 3 | Short horror / anomaly | 5–6% | low | med | good | cheapest; biggest streamer magnet; launch Q3/Q4 |
| 4 | Job / shopkeeper / physics sim | 4–13% | med | med | ok | theme is everything; clone flood |
| 5 | Idle / incremental | 3–6% | low | med–high | weak (desktop idlers) | supply up 5x in 2 years |
| 6 | Cozy / farming / life | 8–11% | high | med | excellent | players expect 30+ h content |
| 7 | Deduction / detective | n/a | med (writing) | med | good | narrative had the most hits in 2025 |
| 8 | Auto-battler | n/a | med | med–high | good | async PvP needs a backend |
| 9 | Friendslop co-op | huge ceiling | med–high | high | poor | netcode, binary outcomes |
| 10 | Narrative / VN | ~4% | med | med–high | good | median $10–40k |
| 11 | Tower defense | 2–3.5% | med | high | good | median game <10 reviews |
| 12 | Extraction | winner-takes-all | high | very high | poor | avoid |
| 13 | Puzzle | 0.3% | low–med | very high | good | avoid |
| 14 | Platformer / fighter | 0.2–1.4% | med–high | very high | good | avoid |

---

## 7. Lessons across all games

1. **One proven loop + one twist.** Peggle → Peglin/Nubby, Balatro → CloverPit, Vampire
   Survivors → Megabonk, Motherload → Digging a Hole, idle + farm → Rusty's. Nobody invented a
   genre except Vampire Survivors.
2. **The 5-second clip test.** If a short clip doesn't explain the game and show a funny, tense or
   "broken" moment, streamers won't pick it up. Hard-to-learn-looking games die (Bramble).
3. **Cheap stylized art, $3–10 price.** PS1 low-poly, pixel, UI-only, licensed assets. A low price
   excuses short length.
4. **Prove demand before finishing.** itch build, demo, Next Fest, daily short clips. Weak demo
   numbers are the cheapest kill signal.
5. **Expect a spike, then a drop.** Revenue is up front; plan a "finished game", not a live
   service.
6. **Practice is the hidden ingredient.** Almost every quick hit came after many earlier games.
   The repeatable strategy is several small games, not one big one.

---

## 8. What this means for your choice (judgment, not data)

- **Format:** single player, 3–6 months of scope (which becomes ~1 year in reality), $5–10.
- **Shortlist:**
  1. **Survivors-like with a big twist.** Gamepad-native, Switch fit, clips well. Could reuse the
     Automate-swarm idea from Assemblia.
  2. **Toy roguelike (Balatro-like) around a familiar object.** Cheap art; risk is design and
     balance, not content.
  3. **Short anomaly / one-room horror.** Cheapest (3–4 months), PS1 style suits Meshy, the
     biggest streamer magnet; could be a first release before a bigger game.
- **My recommendation:** treat this as a series of small bets. Start with the cheapest option that
  you'd enjoy making, prove the clip and the demo in weeks, and keep going only if the demo pulls
  players.

---

## Sources (main)
- Base rates: [HTMAG 2025](https://howtomarketagame.com/2026/01/27/what-the-hell-happened-in-2025/), [SPA niches](https://www.steampageanalyzer.com/niches), [80.lv](https://80.lv/articles/analysts-report-drop-in-game-revenue-on-steam-despite-growing-number-of-releases), [GameDiscoverCo long tail](https://gamedevreports.substack.com/p/gamediscoverco-the-long-tail-of-steam), [AppMagic friendslop](https://appmagic.rocks/blog/friendslop-steam-games-2025), [Sensor Tower 2026](https://sensortower.com/blog/indie-and-new-ip-break-out-without-denting-aaa)
- Co-op: [MECCHA (Unreal interview)](https://www.unrealengine.com/developer-interviews/meccha-chameleon-how-two-devs-built-the-indie-smash-hit-of-the-summer), [MECCHA (Automaton)](https://automaton-media.com/en/news/meccha-chameleon-developers-say-the-secret-behind-their-2-month-dev-cycle-is-asset-reuse-and-a-make-it-exist-first-perfect-it-later-approach/), [PEAK (GameDiscoverCo)](https://newsletter.gamediscover.co/p/how-peak-sold-45m-copies-in-less), [RV There Yet?](https://en.wikipedia.org/wiki/RV_There_Yet%3F), [Content Warning](https://gameworldobserver.com/2024/04/02/content-warning-140k-ccu-4-5-million-downloads-landfall), [Lethal Company (pushtotalk)](https://www.pushtotalk.gg/p/how-lethal-company-sold-10-million-copies), [Schedule I (Alinea)](https://gamedevreports.substack.com/p/alinea-analytics-top-steam-games), [R.E.P.O.](https://tech.yahoo.com/gaming/articles/lets-just-fail-quickly-repo-142853084.html), [YAPYAP (GameDiscoverCo)](https://newsletter.gamediscover.co/p/how-yapyap-jammed-its-way-to-1-million), [How to Fish](https://game8.co/articles/latest/how-to-fish-catches-10-million-players-and-teases-whats-next), [GWYF](https://wnhub.io/news/finance/item-51060), [WEBFISHING](https://raijin.gg/app/3146520/WEBFISHING), [Liar's Bar](https://gameworldobserver.com/2024/10/21/liars-bar-100k-ccu-steam-curve-animation-turkey-success), [Chained Together](https://gameworldobserver.com/2024/06/25/chained-together-85k-concurrent-players-launch-steam), [Overthrown vs Super Battle Golf](https://newsletter.gamediscover.co/p/how-two-friendslop-hits-got-the-audience), [Garden Wars postmortem](https://www.gamedeveloper.com/design/valuable-but-not-profitable-garden-wars-postmortem), [Photon / R.E.P.O.](https://blog.photonengine.com/r-e-p-o-multiplayer-success-powered-by-photon/)
- Single player: [Megabonk](https://en.wikipedia.org/wiki/Megabonk), [Vampire Survivors](https://en.wikipedia.org/wiki/Vampire_Survivors), [Brotato](https://www.gamespress.com/Brotato-10-Release), [Buckshot Roulette](https://www.kitguru.net/gaming/joao-silva/buckshot-roulette-hits-8-million-sales-console-port-gets-delayed/), [CloverPit (GameDiscoverCo)](https://newsletter.gamediscover.co/p/real-data-how-cloverpit-hit-750k), [Balatro timeline](https://www.nintendolife.com/news/2025/03/i-felt-totally-overwhelmed-balatro-dev-releases-development-timeline), [A Short Hike](https://en.wikipedia.org/wiki/A_Short_Hike), [Mouthwashing](https://www.gamesradar.com/games/horror/this-is-incredibly-rare-how-mouthwashing-quietly-became-2024s-breakout-horror-hit/), [The Operator](https://www.gamesradar.com/games/puzzle/in-a-huge-win-for-niche-games-this-solo-devs-4-hour-software-adventure-has-racked-up-usd1-million-in-revenue/), [Nubby's (GameMaker blog)](https://gamemaker.io/en/blog/following-the-fun-nubbys-number-factory), [Digging a Hole](https://en.wikipedia.org/wiki/A_Game_About_Digging_a_Hole), [Bongo Cat](https://wnhub.io/news/stores-and-publishing/item-48117), [Rusty's Retirement (GameDiscoverCo)](https://newsletter.gamediscover.co/p/how-rustys-retirement-idle-farmed), [Peglin](https://howtomarketagame.com/2022/05/04/how-peglin-made-1049413-in-1-week/), [Bramble Royale flop](https://newsletter.gamediscover.co/i/160824287), [Archetype retrospective](https://serfofcinder.itch.io/archetype-portal-to-hell/devlog/866477/a-retrospective)
- Genres: [survivors-like decline (HTMAG)](https://howtomarketagame.com/?p=5658), [hit games early 2025](https://howtomarketagame.com/2025/04/11/the-hit-games-of-early-2025/), [friendslop saturation](https://howtomarketagame.com/2026/07/30/is-friendslop-saturated), [The Exit 8](https://www.gematsu.com/2026/09/the-exit-8-sales-top-three-million), [Ball x Pit](https://www.pushsquare.com/news/2026/08/devolvers-brilliant-roguelite-dopamine-factory-ball-x-pit-is-a-smash-hit-at-2-million-sales), [cozy niche](https://www.steampageanalyzer.com/niches/cozy), [genre revenue](https://www.steampageanalyzer.com/blog/steam-revenue-by-genre)
