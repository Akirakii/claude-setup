# Social deduction, hide-and-seek and party games with tiny rule sets and long lives

Current as of 2026-11-09. Tags: **[source](link)** = said on that page (pages marked "snippet" were seen only as a search-result summary, not opened). **[read]** = I pulled the number myself from a primary data feed on 2026-11-09 (Steam Charts monthly table, Steam Web API live count, Steam store API), so it shows what the game does, not what someone claims. **[opinion]** = my inference. Steam numbers cover Steam only. Mobile, console, VR and tabletop play is not in them.

Terms used: **content** = authored stuff a player can use up (maps, words, questions, ghost types, locations). **coupling between players** = how much one player's action changes what another player can know or do. **loop** = one round, start to finish.

---

## 1. How small is each game's rule set and content, and what makes each round different?

### Takeaway
Every game here fits its rules on one card and ships with almost no content (0 to about 30 items). Each round differs because of three cheap generators: a secret role shuffle, the other players' minds and voices, and a random pick from a small pool. Where the small pool is itself the puzzle (Spyfall locations, Fibbage questions), players use it up. Where the pool is only a stage for talk (Werewolf, Codenames grid, Prop Hunt props), they do not.

### Cited Findings

**Summary table** (facts from the findings below; "variety source" column is [opinion])

| Game (year) | Rules, in one line | Content at launch | Variety source each round [opinion] |
|---|---|---|---|
| Mafia/Werewolf (1986/87; Werewolf 1997) | Night: hidden team kills one. Day: talk, vote one out. | 0 (cards or hand signs; original had no special roles) | Secret role shuffle + players' lies |
| Among Us (2018) | Crew do tasks or vote out impostors; impostors kill/sabotage; any body or button calls a meeting and vote | 1 map | Secret roles + who saw what + talk |
| Prop Hunt (TF2 2009; Gmod) | Hiders become props until timer ends; hunters lose health for wrong shots | 0 new (reuses map clutter) | Hider choice of object and spot vs seeker eye |
| MECCHA CHAMELEON (2026) | Hiders paint white bodies to match the stage; seekers must find all in time | small map set + Steam Workshop maps | Each hider's painting and pose |
| Liar's Bar (2024) | Claim cards/dice, call "liar", loser plays Russian roulette or drinks poison | 2 tables (dice, deck) | Bluffs of 3 opponents |
| The Resistance (2010) / Avalon (2012) | Leader picks a team, all vote, team secretly plays Success/Fail; best of 5 | 0 (Avalon adds 6 roles) | Secret roles + voting record |
| Spyfall (2014) | All but one know the location; ask questions; find the spy, or spy guesses place | 24–30 locations (sources disagree) | Random location + improvised Q&A |
| Codenames (2015) | Spymaster gives one word + number; team guesses on a 5x5 grid; avoid assassin | word cards (count not found) | Random 25 words x spymaster's mind |
| Spaceteam (2012) | Read the order on your screen, shout it; whoever has that control acts | generated technobabble controls | Random controls + shouting |
| Keep Talking and Nobody Explodes (2015) | Defuser sees bomb not manual; experts see manual not bomb | manual of modules; bombs generated | Random bomb + talk quality |
| Jackbox Quiplash/Fibbage (2014–) | Everyone writes an answer (or a lie) to a prompt; everyone votes | fixed prompt bank | Players' own writing |
| Lethal Company (2023) | Collect scrap in a monster facility, meet a quota, talk only by proximity or walkie | moons, monsters | Monsters + proximity voice + masked mimics |
| Phasmophobia (2020) | Find evidence, name the ghost type out of ~29–30 | maps, ~29–30 ghost types, 7 evidence types | Random ghost + voice-reactive ghost + team fear |

**Mafia / Werewolf**
- Day/night loop: night = secret kills, day = discussion and a vote to eliminate. Minimum about 6 players (10 for classic). Davidoff's original rules: about a third of players are mafia, no special roles. Plotkin (Werewolf) recommends exactly two wolves and an odd player count to avoid ties. Special roles (detective, doctor etc.) are optional add-ons — [source](https://en.wikipedia.org/wiki/Mafia_(party_game))
- Basic rules take about a minute to explain; needs a moderator and 7+ players; day phases about 15 minutes; a round about 30 minutes — [source: Wired UK, 4 Feb 2010, mirror](https://wirednews.pages.dev/story/werewolf)
- Davidoff frames it as "the uninformed majority versus the informed minority" — [source](https://wirednews.pages.dev/story/werewolf)

**Among Us**
- 4–15 players, 1–3 secret impostors. Crew wins by tasks or by ejecting all impostors. Impostors win by kills, ejections or a critical sabotage. Any living player calls a meeting (body report or button); plurality vote ejects — [source](https://en.wikipedia.org/wiki/Among_Us)
- Launched with one map (The Skeld); MIRA HQ Aug 2019, Polus Nov 2019, Airship Mar 2021, Fungle Oct 2023 → five maps by 2026 — [source](https://en.wikipedia.org/wiki/Among_Us)
- Tasks were added to stop players roaming "around a house aimlessly"; the core "of creating and reporting dead bodies" came from the childhood Mafia-like game — [source: Forest Willard, Nintendo.com, 12 Jan 2021](https://nintendo.com/whatsnew/among-us-dev-recounts-how-the-game-took-flight)

**Prop Hunt**
- TF2 Prop Hunt (Luke "Darkimmortal" Foreman, first release 22 Oct 2009): BLU Pyros lose health when they fire; RED Scouts disguised as props survive until the timer runs out — [source: Robert Yang, 27 May 2017](https://www.blog.radiator.debacle.us/2017/05/from-modders-to-mimics-peoples-history.html)
- Uses a set of community maps with the `ph_` prefix, i.e. ordinary maps full of props — [source, snippet](https://wiki.teamfortress.com/wiki/PropHunt)
- Prop Hunt worked in TF2 because its maps already had lots of clutter and flat cartoon lighting made a disguised prop hard to tell from a real one — [source](https://www.blog.radiator.debacle.us/2017/05/from-modders-to-mimics-peoples-history.html)

**MECCHA CHAMELEON**
- Store text: "The rules are simple. Split into the Seeker team and the Hider team... The Seekers win if they find everyone within the time limit." "Paint your pure white body to blend into the stage." "The hiding spot, the pose, and above all, your artistic skills are the key!" 2–10 players recommended; public servers; streamers can host viewer games — [read: Steam store API](https://store.steampowered.com/app/4704690/)
- Store categories include Steam Workshop; many Workshop map mods exist (e.g. Minecraft-style maps); host can set paint time — [read](https://store.steampowered.com/app/4704690/); [source](https://www.gamingonlinux.com/2026/06/meccha-chameleon-is-a-hide-and-seek-body-painting-game-taking-over-steam/)
- I found no reliable count of official maps. One low-quality patch-note site says a July 2026 patch reworked an "Osaka" map; not checked.

**Liar's Bar**
- Four animal characters at a table. Liar's Dice: roll six dice, bet, accuse; caught liar drinks poison. Liar's Deck: play cards matching the table's ace/queen/king, accuse; caught liar plays Russian roulette with one bullet in six chambers — [source](https://en.wikipedia.org/wiki/Liar%27s_Bar)
- Later updates added a new location and a "Chaos" ruleset — [source, snippet](https://www.pcgamesn.com/liars-bar/update-chaos-mode)

**The Resistance / Avalon**
- 5–10 players; spies are a third (rounded up). Leader proposes a team; everyone votes in public; 5 rejections in a row = spies win. Team members secretly play Success/Fail; one Fail sinks the mission (two on mission 4 at 7+ players). First to 3 missions wins. Nobody is eliminated — [source](https://en.wikipedia.org/wiki/The_Resistance_(game))
- Avalon (2012) adds six roles: Merlin (knows evil, must stay hidden from the Assassin), Percival, Morgana, Mordred, Oberon, Assassin — [source](https://en.wikipedia.org/wiki/The_Resistance_(game))

**Spyfall**
- 3–8 players, 6–10 minutes. Everyone gets the same location card except one spy. Players question each other; anyone may accuse at any time; the spy may reveal and guess the location — [source](https://en.wikipedia.org/wiki/Spyfall_(card_game))
- Location count conflict: 24 locations listed in the manual, eight-minute rounds — [source: Meeple Like Us, 2018](https://www.meeplelikeus.co.uk/spyfall-2014/); a retailer summary says 30 locations, with Spyfall 2 adding 20 (snippet only, page not identified).

**Codenames**
- 25 word cards in a 5x5 grid; two teams, each with a spymaster; clue = one word + a number; one black assassin card loses the game; 4–8+ players; 15–30 minutes — [source](https://en.wikipedia.org/wiki/Codenames_(board_game))
- First prototype: scribbled words on paper torn by hand ("I didn't even have a pair of scissors"); first game played within a few hours — [source: Tabletop Gaming, 19 Aug 2024](https://www.tabletopgaming.co.uk/?p=4157)

**Spaceteam**
- 2–8 players on phones over Wi-Fi/Bluetooth. Each has a panel of knobs and dials labelled with technobabble. Orders on your screen are for someone else's controls, so you call them out. Mistakes break panels; some events need you to shake or flip the device — [source](https://en.wikipedia.org/wiki/Spaceteam)
- Core idea: "having something on one screen that you had to react to on another screen" — [source: Game Developer, 9 Feb 2016](https://www.gamedeveloper.com/design/everybody-shake-the-making-of-spaceteam---chapter-1-of-3)

**Keep Talking and Nobody Explodes**
- Defuser sees the bomb but not the manual; experts read the manual but cannot see the bomb. Modules to disarm, "needy" modules to tend, timer and strike limit. Bombs and modules are procedurally generated — [source](https://en.wikipedia.org/wiki/Keep_Talking_and_Nobody_Explodes)
- No module count or page count found (bombmanual.com lists "Version 1" only).

**Jackbox (Quiplash / Fibbage)**
- Phones as controllers via a room code on a web page, no app; limited input types (draw, buttons, text); private info sent to each phone — [source: Built In, 19 Jun 2020](https://builtin.com/articles/jackbox-games-design-party-pack)
- Quiplash: players write answers to a prompt, others vote for a favourite — [source](https://wsvn.com/entertainment/jackbox-games-wants-to-take-family-game-night-online/)
- Fibbage XL: Steam reviewers note questions start repeating after a few hours — [source, snippet: review aggregator](https://vaporlens.app/app/448080/fibbage_xl.md)

**Lethal Company**
- Players talk by proximity voice (and proximity text) and can talk at range only with walkie-talkies — [source](https://en.wikipedia.org/wiki/Lethal_Company); [source, snippet](https://primagames.com/gaming/what-led-to-lethal-company-exploding-in-popularity-how-developers-can-learn-from-its-success)
- Voice echoes to match the room; a caught player's scream is heard nearby and cut off — [source](https://www.windowscentral.com/gaming/pc-gaming/this-viral-lethal-company-clip-perfectly-illustrates-why-this-pc-game-is-blowing-up-right-now); [source, snippet](https://primagames.com/gaming/what-led-to-lethal-company-exploding-in-popularity-how-developers-can-learn-from-its-success)
- The Masked (the official "mimic") arrived in v45 "Frosty Update", Dec 2023: holding a mask can possess a player and turn them into a Masked monster that looks like a crewmate — [source, snippet](https://esports.gg/news/gaming/lethal-company-releases-first-major-update-v45-patch-notes); [source, snippet](https://destructoid.com/?p=438178)
- Voice-mimic is a mod, not base game: Skinwalkers records voice-chat clips and replays them from monsters' bodies — [source](https://primagames.com/tips/are-there-skinwalkers-in-lethal-company-answered); Mirage lets every enemy mimic any player's voice — [source, snippet](https://github.com/qwbarch/mirage)

**Phasmophobia**
- Up to 4 players identify the ghost type. Each ghost has 3 evidence types from a pool of 7 (fewer shown on Nightmare+). Ghost list: 30 types as of Sept 2026 (gameplay section says 29) — [source](https://en.wikipedia.org/wiki/Phasmophobia_(video_game))
- Speech recognition: equipment, Cursed Possessions and the ghost react to spoken key words; players talk by proximity voice or walkie-talkies — [source](https://en.wikipedia.org/wiki/Phasmophobia_(video_game))

### Inferences
- [opinion] Three generators make all the variety: (1) a **secret role shuffle** (Werewolf, Among Us, Resistance, Spyfall, Masked in Lethal Company); (2) **asymmetric information split across players** so they must talk (KTANE manual/bomb, Spaceteam screens, Codenames key card, Jackbox private phones); (3) **player-made output** others judge (Quiplash answers, Fibbage lies, MECCHA paint jobs, Prop Hunt object choice). None of the three costs content.
- [opinion] Content works as a **stage**, not as the puzzle, in the long-lived ones: Werewolf has none, Codenames draws 25 random words, Prop Hunt reuses map clutter. In Spyfall and Fibbage the small pool *is* the thing to deduce or guess, and reviewers report it wears out (see Q3).
- [opinion] Hide-and-seek games (Prop Hunt, MECCHA) turn map art into content for free: every prop or texture is a possible hiding spot. That is why Workshop maps matter to MECCHA.
- [opinion] Lethal Company and Phasmophobia carry more authored content (monsters, ghost types, maps) than any other game here. Their player coupling comes from voice rules (proximity, walkie, ghost hears you), not from roles.

### Gaps
- Codenames base-game word count, KTANE module count and manual page count: not found in sources I could open.
- Spyfall location count: 24 (Meeple Like Us) vs 30 (unidentified retailer). Not resolved.
- MECCHA CHAMELEON official map count and round timer defaults: no reliable source.
- Jackbox prompt counts per game: not found.

---

## 2. What did the designers say about why it works?

### Takeaway
Designers say the same thing in different words: the fun lives in the talk between players, not in the game's objects. Several also say the core was found by accident or cut down from something bigger (Spaceteam's shouting, Among Us dropping a constant-crisis version, Phasmophobia starting as a co-op puzzle game, KTANE dropping the bomb theme to a "communications game").

### Cited Findings

**Mafia / Werewolf**
- Davidoff, a Moscow State University psychology student, built it to mix psychology research with teaching high-school students; first game spring 1987 by his account (Wikipedia lead says 1986) — [source](https://en.wikipedia.org/wiki/Mafia_(party_game))
- Davidoff: "Past connections will always lose to future collaborations." He says the game favours freedom: education and experience do not carry over. Hasbro looked at it and judged it "unprotectable" — [source: Wired UK 2010](https://wirednews.pages.dev/story/werewolf)
- Andrew Plotkin (Werewolf, 1997): "It shouldn't have worked, but it did." "I thought the rules were brilliant, but the theme felt arbitrary." — [source](https://wirednews.pages.dev/story/werewolf)
- Davidoff (2025, on The Traitors): "If you do any kind of due diligence, you see that Mafia is my game"; "Game designers' work deserves recognition and reward." — [source: AOL citing Vulture, 2 Jul 2025](https://www.aol.com/lifestyle/mafia-creator-claims-traitors-producers-010131669.html)

**Among Us (Innersloth)**
- Marcus Bromander: "I really liked the concept of someone hiding in plain sight and you don't know who you can trust", then "what if you could link that to a Jackbox-type of mobile experience" — [source: Game World Observer citing Noclip documentary, 20 Apr 2022](https://gameworldobserver.com/2022/04/20/how-the-thing-inspired-innersloth-to-make-among-us)
- Forest Willard: a version where the ship was always in crisis was "too stressful and didn't leave much time for detective work and informed meeting conversations." Team of four, about seven months to make — [source: Nintendo.com, 12 Jan 2021](https://nintendo.com/whatsnew/among-us-dev-recounts-how-the-game-took-flight)
- Willard: the team "stuck with [the game] a lot longer than we probably should have from a pure business standpoint." Bromander credits studio savings for surviving slow sales — [source](https://en.wikipedia.org/wiki/Among_Us)
- Bromander: "We were basically done with (Among Us) at the start of 2019" — [source, snippet](https://www.gamesradar.com/among-us-team-was-basically-done-and-almost-canceled-in-2019)

**Prop Hunt (modders)**
- Robert Yang (designer/critic, not the mod author): flipping the older format (hiders ambush seekers → seekers flush out hiders) made it "more replayable" and slapstick rather than scary. Lineage: CrateDM (Quake 2, 1998) → Boxwar (Half-Life, 2002) → Suicide Survival (HL2DM, 2008) → Prop Hunt (TF2, 2009). CrateDM's author called his crate "nothing more than a crate, period" and the mod "just good fun with a dumb idea" — [source](https://www.blog.radiator.debacle.us/2017/05/from-modders-to-mimics-peoples-history.html)

**MECCHA CHAMELEON**
- Two developers in Japan (creator lemorion_1224, programmer Haganeiro) who met in the Fortnite custom-map creator community; two months of development; no marketing budget; growth from Twitch clips and word of mouth — [source: Hitmarker, 8 Jul 2026](https://hitmarker.net/news/indie-hit-meccha-chameleon-is-now-the-best-selling-game-of-2026-1944965)
- No design interview found.

**The Resistance / Avalon (Don Eskridge)**
- Secondary sources say it was built to avoid player elimination and give players more information for decisions — [source, snippet](https://mechanicsofmagic.com/2024/04/09/the-resistance-critical-analysis/)
- Eskridge discussed social-deduction design on Board Game Design Lab ep. 58 (10 Jan 2018, 55 min); only show notes are online, no transcript — [source](https://boardgamedesignlab.com/designing-social-deduction-games-with-don-eskridge/)

**Codenames (Vlaada Chvátil)**
- "one of the great things is the way the game tailors itself to the personality of the group that's playing." "I was surprised by how much it appealed to non-gamers." — [source: Tabletop Gaming, 19 Aug 2024](https://www.tabletopgaming.co.uk/?p=4157)
- "With Codenames, everyone is thinking at the same time" — [source, snippet](https://inkl.com/news/everyone-is-thinking-at-the-same-time-how-codenames-became-the-board-game-of-the-decade)

**Spaceteam (Henry Smith)**
- The constant shouting was not designed; it appeared because shouting was the only way to be heard in hard levels — [source](https://en.wikipedia.org/wiki/Spaceteam)
- The idea came from a dream of shouting at his brother who didn't understand how to play — [source](https://www.gamedeveloper.com/design/everybody-shake-the-making-of-spaceteam---chapter-1-of-3)
- Inspirations: co-op board game Space Alert; made as a project to learn iOS/Android coding; profit was never the goal — [source](https://en.wikipedia.org/wiki/Spaceteam)

**Keep Talking and Nobody Explodes (Ben Kane, Steel Crate Games, GDC 2016)**
- "The fun really lives between players." "we're making a communications-based party game, it just happens to have bombs in it." — [source: Game Developer, 14 Mar 2016](https://gamedeveloper.com/design/finding-the-fun-in-bomb-defusal-with-i-keep-talking-and-nobody-explodes-i-)
- "It starts with balance": both sides must hold unique information to trade. "The rules have to be totally unambiguous": if players must guess, they feel cheated. "Our game involves talking, so our job involved eavesdropping" on playtests — that is how they caught that "cut the second wire" was ambiguous — [source](https://gamedeveloper.com/design/finding-the-fun-in-bomb-defusal-with-i-keep-talking-and-nobody-explodes-i-)
- Random events "might seem totally random, but they're actually not; under the hood, we have a little pacing system." — [source](https://gamedeveloper.com/design/finding-the-fun-in-bomb-defusal-with-i-keep-talking-and-nobody-explodes-i-)

**Jackbox**
- Allard Laban (CCO): "If I find it difficult, then, you know, my aunt's going to find it very difficult." Games never ask for several choices at once. A "weird hybrid of passive and active media." Chase McClure: "We try to keep it pretty simple" (few input types); phone-only games work because each player can get private info. Studio keeps ~50 concepts in backlog, ships 5 per pack; paper-tests first; lineage: Drawful = Fibbage with drawing — [source: Built In, 19 Jun 2020](https://builtin.com/articles/jackbox-games-design-party-pack)
- CEO Mike Bilder: only one player needs to own the game; no fast reactions needed — [source: CNN via WSVN, 17 Oct 2020](https://wsvn.com/entertainment/jackbox-games-wants-to-take-family-game-night-online/)

**Lethal Company (Zeekerss)**
- Development was first planned to finish in six months; Zeekerss wants updates to feel like breaking into an "alien zoo" (paraphrase) — [source](https://en.wikipedia.org/wiki/Lethal_Company)
- No Zeekerss quote found on proximity chat or the Masked. Analysts credit proximity chat for turning near-deaths into shared jokes — [source, snippet](https://primagames.com/gaming/what-led-to-lethal-company-exploding-in-popularity-how-developers-can-learn-from-its-success)

**Phasmophobia (Daniel Knight)**
- "I don't actually play horror games"; he did not set out to make a horror game — [source: PC Gamer headline](https://www.pcgamer.com/games/horror/i-dont-actually-play-horror-games-phasmophobias-lead-developer-had-no-intention-of-making-a-horror-game-but-still-kicked-off-a-whole-new-genre); he set out to make a co-op puzzle game — [source, snippet](https://www.gamespark.jp/article/2025/06/13/153981.html)
- A Witcher 3 prologue quest gave him the ghost-type idea — [source](https://opencritic.com/news/18562/phasmophobias-development-was-saved-by-a-witcher-3-prologue-quest-of-all-things)

### Inferences
- [opinion] The shared claim is **information split across people**: Davidoff's "informed minority", Kane's "both sides need unique information", McClure's "private info to each phone", Bromander's "you don't know who you can trust". The game hands out secrets; players turn secrets into talk. That is high coupling between players at near-zero content cost.
- [opinion] Several designers reached the core by **removing** things: Innersloth cut the always-in-crisis version to leave time for meetings; Steel Crate cut the bomb seriousness; Plotkin changed only the theme; Smith left shouting unexplained in rules and let players find it. Fits the user's "low coupling between features" idea: one loop, few systems.
- [opinion] Kane's "rules must be totally unambiguous" matters most for voice games: arguments should be about *people*, not about what the rules mean.
- [opinion] Davidoff's "unprotectable" and the Traitors dispute show the flip side: a rule set this small cannot be owned. Prop Hunt spread engine to engine, Among Us drew on Mafia, MECCHA came from Fortnite custom maps. A solo dev should expect clones within weeks.

### Gaps
- No primary Innersloth statement on *why* meetings/voting work beyond Willard's "detective work and informed meeting conversations"; Among Us GDC talk not found.
- Eskridge's own words: podcast audio only; no transcript found.
- Zeekerss on the Masked/mimic and on proximity chat: none found. PC Gamer and Windows Central articles on his update philosophy would not load (truncated).
- MECCHA CHAMELEON, Liar's Bar (Curve Animation) and Spyfall (Ushan): no designer interviews found.
- Prop Hunt author (Darkimmortal / Andrew Theis): no interview found; only Robert Yang's history.

---

## 3. How long did they stay popular, and did they need content updates? Which faded fast and why?

### Takeaway
The tabletop games (Mafia ~39 years, Codenames 11 years and 16M+ copies) last with no content updates because they live in social habits (camps, conferences, game nights) and need no servers. Online hits all crash 90–99% from their peak; what is left depends on group play with friends and steady updates. Phasmophobia keeps the most (about 10% of peak after six years). Liar's Bar and MECCHA CHAMELEON fell fastest (about 1% of peak within 5 months to 2 years).

### Cited Findings

**Peak vs now on Steam** ([read] = Steam Charts monthly table and Steam Web API, 2026-11-09)

| Game | All-time Steam peak | Oct 2026 avg / peak | Live count 2026-11-09 | Avg as % of peak [opinion: arithmetic] |
|---|---|---|---|---|
| Among Us | 438,524 (Sep 2020) | 7,050 / 16,190 | 6,913 | 1.6% |
| Phasmophobia | 112,241 (Oct 2020) | 10,703 / 24,235 | 11,942 | 9.5% |
| Lethal Company | 239,369 (Dec 2023) | 2,733 / 6,243 | 3,857 | 1.1% |
| Liar's Bar | 109,419 (Oct 2024) | 542 / 1,268 | 736 | 0.5% |
| MECCHA CHAMELEON | 340,534 (Jun 2026, per GamingOnLinux) | not on Steam Charts | 3,395 | ~1.0% (live/peak) |
| Garry's Mod (Prop Hunt's host) | 73,750 (Jan 2015) | 22,382 / 38,977 | — | 30% |
| Keep Talking | 3,359 (Dec 2024 sale) | 112 / 271 | — | 3.3% |

Sources: [Among Us](https://steamcharts.com/app/945360), [Phasmophobia](https://steamcharts.com/app/739630), [Lethal Company](https://steamcharts.com/app/1966720), [Liar's Bar](https://steamcharts.com/app/3097560), [Garry's Mod](https://steamcharts.com/app/4000), [KTANE](https://steamcharts.com/app/341800), [MECCHA live count, Steam Web API](https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=4704690), [MECCHA peak](https://www.gamingonlinux.com/2026/06/meccha-chameleon-is-a-hide-and-seek-body-painting-game-taking-over-steam/). A single live count depends on time of day.

**Mafia / Werewolf — ~39 years, no owner, no updates needed**
- Spread from psychology classrooms to dorms and summer camps, Soviet schools, Europe and the US in the 1990s; Werewolf theme (1997) spread through GDC, ETech, Foo Camp, SXSW — [source](https://en.wikipedia.org/wiki/Mafia_(party_game))
- One all-night session drew almost a third of Foo Camp 2008; used by Mensa groups, theatre improv, summer camps, Chinese late-night clubs — [source](https://wirednews.pages.dev/story/werewolf)
- Many commercial versions (Ultimate Werewolf, Werewolves of Millers Hollow, One Night, Town of Salem; Town of Salem 2 in 2023) — [source](https://en.wikipedia.org/wiki/Mafia_(party_game))
- The Traitors TV format (Dutch De Verraders 2021, US 2023) is "nearly identical" — [source](https://www.aol.com/lifestyle/mafia-creator-claims-traitors-producers-010131669.html)

**Among Us — slow start, one huge spike, long flat tail, steady updates**
- Mobile June 2018, Steam Nov 2018; weak launch ("really bad at marketing"); nearly abandoned more than once — [source](https://en.wikipedia.org/wiki/Among_Us)
- Steam monthly average under 120 players through Jan 2020 — [read](https://steamcharts.com/app/945360)
- Sodapoppin streamed it July 2020; pandemic distancing often cited; 3.8M concurrent (all platforms) late Sept 2020; SuperData ~500M players by Nov 2020; Switch 3.2M digital units Dec 2020 — [source](https://en.wikipedia.org/wiki/Among_Us)
- Steam average since 2021 has stayed in a 4,500–9,500 band (Oct 2021 6,362; Oct 2023 4,786; Oct 2024 4,512; Oct 2026 7,050) — [read](https://steamcharts.com/app/945360)
- Kept adding maps (5 by 2026), roles (2021–2026) and Hide & Seek mode (Dec 2022). Cancelled Among Us 2 (Sept 2020) to rework the original codebase, which was "outdated and not built to support adding so much new content" — [source](https://en.wikipedia.org/wiki/Among_Us)

**Prop Hunt — 17+ years as a mode, moved across engines**
- TF2 version 2009, replaced by PropHunt Redux late 2013 — [source, snippet](https://wiki.teamfortress.com/wiki/PropHunt)
- Garry's Mod version: Facepunch wiki says created 2012 (from CS:S, ported by Andrew Theis); Robert Yang notes a 2007 Gmod version; Vice says it took off on Gmod in 2013. Dates conflict — [source, snippet](https://wiki.facepunch.com/gmod/gamemodes:PropHunt~diff:564495); [source](https://www.blog.radiator.debacle.us/2017/05/from-modders-to-mimics-peoples-history.html); [source, snippet](https://vice.com/en/article/what-is-fortnite-prop-hunt)
- Garry's Mod (which hosts Prop Hunt among many modes) still averaged 22,382 players in Oct 2026, about the same as Oct 2015 (25,704) — [read](https://steamcharts.com/app/4000)

**MECCHA CHAMELEON — fastest seller of 2026, then a steep fall**
- Released 9 June 2026, $5.99 — [read](https://store.steampowered.com/app/4704690/)
- 1M sold in 4 days, 3M in a week, 10M in 16 days, 15M in 25 days; peak ~340k concurrent; called best-selling game of 2026 — [source](https://hitmarker.net/news/indie-hit-meccha-chameleon-is-now-the-best-selling-game-of-2026-1944965)
- 340,534 peak; 7M sold by 22 June; public servers vanish when the host leaves — [source](https://www.gamingonlinux.com/2026/06/meccha-chameleon-is-a-hide-and-seek-body-painting-game-taking-over-steam/)
- Live count 2026-11-09: 3,395 players — [read](https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=4704690)
- An undated aggregator snapshot showed 137,834 (60% below peak); an Aug 1 Steam post promised ongoing support with no dated major update — [source, snippet](https://datahumble.com/meccha-chameleon-4704690)

**Liar's Bar — viral spike, halved each month**
- Early access 2 Oct 2024; ~2,000 at launch → 113,798 by 21 Oct 2024 (SteamDB), driven by streamers; 12th highest-grossing on Steam 8–15 Oct — [source](https://gameworldobserver.com/2024/10/21/liars-bar-100k-ccu-steam-curve-animation-turkey-success)
- Monthly average: Oct 2024 19,758 → Nov 8,789 (−55%) → Dec 4,734 (−46%) → Oct 2026 542 — [read](https://steamcharts.com/app/3097560)
- 2024 Steam Award, Most Innovative Gameplay — [source](https://en.wikipedia.org/wiki/Liar%27s_Bar)
- Steam forum threads Nov–Dec 2024 report cheat DLLs and hacked public lobbies (user reports, not measured) — [source](https://steamcommunity.com/app/3097560/discussions/0/4625853071149253012)

**The Resistance / Avalon — 16 years in print**
- Resistance 2010, Avalon 2012 — [source](https://en.wikipedia.org/wiki/The_Resistance_(game))
- No Avalon-only sales number found; publisher Indie Boards & Cards says it has sold "several million games" across its line — [source](https://backerkit.com/c/users/2118053)

**Spyfall — awards, sequels, wears out with one group**
- 2016 Spiel des Jahres nominee, 2016 Årets Spil winner; sequels Spyfall 2 (2017, multiple spies), DC Spyfall (2018), Spycon (2019) — [source](https://en.wikipedia.org/wiki/Spyfall_(card_game))
- Reviewer: play converges on "local optima"; experienced players learn the question bank and the 24 locations; adding a new player to an experienced group "adds solvability" rather than variety; can happen within one evening — [source: Meeple Like Us, 2018](https://www.meeplelikeus.co.uk/spyfall-2014/)

**Codenames — 11 years, 16M+ copies, no content needed (spin-offs sold anyway)**
- Over 16M copies in 10 years, 45 languages (June 2025) — [source](https://www.expats.cz/czech-news/article/this-czech-board-game-has-outsold-kingdom-come-and-turns-10-with-a-new-edition); earlier 14M, over 7M in the US — [source, snippet](https://itradenews.cz/stories-in-english/1475/czech-republic-has-global-leaders-in-board-games)
- 2016 Spiel des Jahres; spin-offs Duet, Pictures, themed editions; official web version 2022, paid app Sept 2024 — [source](https://en.wikipedia.org/wiki/Codenames_(board_game))

**Spaceteam — free, 3M+ downloads, small income**
- Released 1 Dec 2012; 3M+ downloads by Nov 2015; earned $49,700 directly plus $25,000 in prizes; card-game Kickstarter raised $181,600 on a $7,500 goal (Sept 2015) — [source](https://en.wikipedia.org/wiki/Spaceteam)

**Keep Talking and Nobody Explodes — 11 years, small but steady, spikes on sale**
- 200,000 copies by March 2016; released on 14 platforms over 11 release dates, 2015–2019 (VR, PC, consoles, mobile); 2018 free update removed the VR need — [source](https://en.wikipedia.org/wiki/Keep_Talking_and_Nobody_Explodes)
- Steam monthly average stayed about 65–515 in every October/January sample 2016–2026; all-time Steam peak came in Dec 2024 (3,359) during a cheap sale — [read](https://steamcharts.com/app/341800); sale context — [source, snippet](https://vandal.elespanol.com/noticia/1350776858/salio-hace-casi-10-anos-y-acaba-de-romper-su-record-de-jugadores-en-steam-porque-esta-rebajado-a-menos-de-2-euros/)
- Third-party estimate of up to 1.6M Steam units is unverified — [source, snippet](https://edge-test.steampulse.org/game/341800)

**Jackbox — 12 years, a new pack every year**
- ~100M players in 2019, ~200M expected in 2020, 110M in the first three months of lockdown (CEO Mike Bilder) — [source](https://wsvn.com/entertainment/jackbox-games-wants-to-take-family-game-night-online/)
- Party Pack yearly; six-year run as of 2020 — [source](https://builtin.com/articles/jackbox-games-design-party-pack)
- Quiplash standalone Steam peak 2,855 (19 Apr 2020) — [source, snippet](https://steamdb.info/app/351510/charts)

**Lethal Company — spike, then held up by big rare updates**
- Early access 23 Oct 2023; ~642k units by mid-Nov 2023 (GameDiscoverCo estimate) — [source](https://gameworldobserver.com/2023/11/16/lethal-company-sales-640k-copies-57k-ccu-new-indie-hit-zeekerss); ~10M by Jan 2024 (estimate) — [source](https://en.wikipedia.org/wiki/Lethal_Company)
- Steam monthly average: Jan 2024 94,513 → Oct 2024 13,526 → Jan 2025 17,512 → Oct 2025 4,077 → Oct 2026 2,733 — [read](https://steamcharts.com/app/1966720)
- Updates: v45 Dec 2023 (Masked), v50 2024, v70 June 2025, v80 beta with three new creatures — [source, snippet](https://esports.gg/news/gaming/lethal-company-releases-first-major-update-v45-patch-notes); [source, snippet](https://www.inkl.com/news/after-nearly-1-year-viral-steam-horror-hit-lethal-company-is-back-with-another-big-update-boasting-3-new-creatures-that-are-sure-to-leave-my-pals-and-me-screaming)

**Phasmophobia — best retention of the online games, most content**
- Early access 18 Sept 2020; peak ~86k (GitHyp) Oct 2020; ~22M sold by Dec 2024; console Oct 2024; content updates for about three years; Chronicle update June 2025 — [source](https://en.wikipedia.org/wiki/Phasmophobia_(video_game))
- Over 25M sold across platforms (July 2025) — [source](https://worthplaying.com/article/2025/7/1/news/146702-phasmophobia-surpasses-25-million-sales-across-all-platforms)
- 1.0 planned for 2027: "It's an overhaul of the horror experience"; every ghost gets a new model — [source: Shacknews, 2 Jul 2026](https://www.shacknews.com/article/149878/phasmophobia-1-0-interview-e4-2026)
- Steam monthly average stayed about 8,400–22,200 in every month I sampled 2021–2026 — [read](https://steamcharts.com/app/739630)

### Inferences
- [opinion] **Two survival paths.** (a) *Social habit, no server*: Mafia, Codenames, Resistance, Spyfall live wherever people meet, need no updates, and sell to new groups for decades. (b) *Online, needs a group*: every online game here lost 90–99% of its peak. The tail that stays is friends who play together.
- [opinion] **Content updates help the tail but don't replace the core.** Phasmophobia (most content, steady updates, co-op) keeps ~10% of peak. Among Us (5 maps, many roles) keeps ~1.6% but has been flat for five years. Lethal Company (big rare updates) shows each update as a bump (Jan 2025 > Oct 2024) then decline. This weakens a pure "low content" rule: co-op horror with more content holds better than pure PvP bluffing with little content.
- [opinion] **Fast faders share four traits**: (1) the loop is one short bluff or hide with no role memory between rounds (Liar's Bar, MECCHA); (2) public lobbies with strangers carry most play (cheaters in Liar's Bar; host-leaves crashes in MECCHA); (3) the spike came from streamers, not from friend groups; (4) the variety generator is narrow (one bluff type; one hide skill). Not proven, but the pattern repeats.
- [opinion] **Fixed pool as the puzzle wears out.** Spyfall's 24 locations and Fibbage's question bank get learned; Codenames' random 25 words and Werewolf's zero content do not, because the puzzle is the other mind, not the list.
- [opinion] **Mode-not-product lasts longest online.** Prop Hunt never needed its own sales: it rode on Garry's Mod/TF2, whose players stayed for 15+ years. A small mode inside a hub of modes (the user's "hub") may outlive a standalone small game.
- [opinion] **Viral speed did not predict life.** Among Us had near-zero players for two years before its spike and then kept a tail; MECCHA sold 15M in 25 days then fell ~99% in five months.

### Gaps
- No Steam Charts page for MECCHA CHAMELEON; only one live snapshot (3,395). No monthly curve, no dated decline reporting after August 2026.
- No measured cause for Liar's Bar's drop (cheaters are user reports only).
- No Prop Hunt-specific player count (Garry's Mod total covers all modes).
- Jackbox totals after 2020, Avalon sales, Spyfall sales, Werewolf commercial sales: not found.
- Among Us mobile retention after 2020: not found.

---

## 4. Which verbs do they use?

### Takeaway
The talk verbs (accuse, vote, describe, deduce, lie) carry the coupling in every social-deduction and party game; the body verbs (hide, seek, paint, carry, shoot) carry it in hide-and-seek and co-op horror. Most games have 3–5 verbs, and only one or two of them are secret.

### Cited Findings
Verbs below are taken from the rule descriptions already cited; the verb labels are mine.

| Game | Verbs | Secret verb | Rule source |
|---|---|---|---|
| Mafia/Werewolf | kill (night), discuss, accuse, defend, vote | kill | [source](https://en.wikipedia.org/wiki/Mafia_(party_game)) |
| Among Us | do task, kill, sabotage, report, call meeting, discuss, vote, eject | kill, sabotage | [source](https://en.wikipedia.org/wiki/Among_Us) |
| Prop Hunt | disguise as object, hide, wait out timer, seek, shoot (costs health) | disguise | [source](https://www.blog.radiator.debacle.us/2017/05/from-modders-to-mimics-peoples-history.html) |
| MECCHA CHAMELEON | paint, pose, hide, seek, shoot/find | paint | [read](https://store.steampowered.com/app/4704690/); [source](https://hitmarker.net/news/indie-hit-meccha-chameleon-is-now-the-best-selling-game-of-2026-1944965) |
| Liar's Bar | claim (bet/play cards), bluff, call liar, take punishment | bluff | [source](https://en.wikipedia.org/wiki/Liar%27s_Bar) |
| Resistance/Avalon | propose team, vote, play success/fail, (Avalon) assassinate | play fail | [source](https://en.wikipedia.org/wiki/The_Resistance_(game)) |
| Spyfall | ask, answer, bluff, accuse, guess location | bluff (spy) | [source](https://en.wikipedia.org/wiki/Spyfall_(card_game)) |
| Codenames | describe (one-word clue), interpret, guess | — (key card is secret info) | [source](https://en.wikipedia.org/wiki/Codenames_(board_game)) |
| Spaceteam | read, shout, operate control, shake/flip device | — | [source](https://en.wikipedia.org/wiki/Spaceteam) |
| Keep Talking | describe (bomb), look up (manual), instruct, cut/press | — (split info) | [source](https://en.wikipedia.org/wiki/Keep_Talking_and_Nobody_Explodes) |
| Jackbox Quiplash/Fibbage | write answer / write lie, vote, guess truth | lie (Fibbage) | [source](https://builtin.com/articles/jackbox-games-design-party-pack) |
| Lethal Company | scavenge, carry, talk (proximity), radio, flee; enemy: mimic (Masked) | mimic | [source](https://en.wikipedia.org/wiki/Lethal_Company); [source, snippet](https://destructoid.com/?p=438178) |
| Phasmophobia | investigate, use tool, speak to ghost, deduce type, hide, radio | — (ghost is hidden) | [source](https://en.wikipedia.org/wiki/Phasmophobia_(video_game)) |

- Phasmophobia makes speech itself an input to the world: equipment and the ghost react to spoken key words — [source](https://en.wikipedia.org/wiki/Phasmophobia_(video_game))
- Lethal Company mods turn speech into enemy content: monsters replay recorded player voice — [source](https://primagames.com/tips/are-there-skinwalkers-in-lethal-company-answered)
- Spaceteam's main verb (shout) was never in the rules; players invented it — [source](https://en.wikipedia.org/wiki/Spaceteam)

### Inferences
- [opinion] **Verb families**: *talk verbs* (accuse, vote, describe, ask, claim) couple players through words; *body verbs* (hide, seek, paint, carry) couple them through space and sight; *voice-as-world verbs* (Phasmophobia's ghost hearing you, Lethal Company proximity, mimics) couple them through sound the game itself listens to.
- [opinion] **One secret verb is enough.** Werewolf (kill), Resistance (play fail), Spyfall (bluff), Prop Hunt (disguise), MECCHA (paint) each have one hidden action; every other verb exists to expose it.
- [opinion] **Mimic is the hide verb turned into an enemy.** Prop Hunt's disguise → Prey's mimic (per Yang) → Lethal Company's Masked → voice-mimic mods. A co-op game can borrow social-deduction suspicion without a human traitor by giving a monster the hide verb.
- [opinion] **The verb that lasts is one players can do with their own voice or hands at any skill level**: talking (Werewolf, Codenames), shouting (Spaceteam), describing (KTANE). Verbs that need game-specific skill (painting well in MECCHA, quick bluff with cards in Liar's Bar) may flatten once the skill gap shows.

### Gaps
- No source compares verb counts across these games; the verb lists are my reading of the cited rules.
- No designer statement found on choosing verbs (except Kane's "communications-based party game" and Smith's unplanned shouting).
