# Handoff: critic calibration, then new ideas (AFK run, 2026-11-18)

## Summary for the user (read this first)

**The critic now answers "is this idea fun with friends?", two ideas came out "yes", and Moonsick did not pass.**

### What happened, in order
1. You asked to run the critic on the top friendslop games and adjust it until its score roughly matched their popularity.
2. Claude added games that sold badly (you OK'd it), since a critic that passes everything would match a list of hits perfectly. The list is 14 co-op games, from Phasmophobia (687,000 Steam reviews) down to delivery pals (139).
3. Each game's rules were researched and written as a sheet under a made-up name, so the critic couldn't use the name.
4. The old critic, which counts severe problems, scored 10 of them. Its score barely followed the review counts (0.20, where 1 is a perfect match): it put Lethal Company and PEAK below three games with under 10,000 reviews.
5. Claude tried a second kind of critic: one judge that reads all the sheets side by side and ranks them. Its order followed the review counts closely (about 0.94).
6. That judge then placed the 4 games kept aside, which it had never seen, into the right tier, 4 of 4.
7. You asked to add date and novelty. In all 14 games, every one that brought a new core act is a hit, and every one that followed an earlier game found few players.
8. You said popularity changes with time and trends, and the critic should only tell whether an idea is fun with friends. The verdict became yes / maybe / no, with the shipped games as its examples of fun and novelty on its own line.
9. You asked Claude to check fantasy, feelings and choices itself. That check is its own file, apart from the critic.
10. Claude wrote five idea sheets and sent them through the critic, rewriting each from the holes it found: three rounds for most, five for Moonsick A.

### Where the ideas ended (the critic's verdict, on paper)
| Idea | In one line | Fun with friends? |
|---|---|---|
| Hold On | we rob a deep well by hanging from each other's ankles, and every piece the bottom friend takes is weight on everyone above | ✅ yes |
| Gold Fever | everything we touch turns to gold and the gold climbs our bodies; only a friend's grip takes some off me | ✅ yes, narrowly |
| Moonsick A | a moonbeam that touches me starts a ten-second fit; two friends holding me end it; if they don't reach me I turn, and I can only steer | ❌ maybe, five versions |
| Moonsick B | the silver is behind doors only a wolf can break, so one of us turns on purpose and the wolf obeys less with every door | ❌ maybe |
| Piggyback | only the sick see the herbs, so they ride on a healthy friend's back and point | ❌ maybe, dropped |

**You asked for at least 3 good ideas with Moonsick as one of them. There are 2, and Moonsick is not one of them.**

### Why Moonsick stayed at "maybe"
In all five versions a careful crew can keep its distance from the thing that turns them, so the turn rarely happens and the night is quiet.
In the hits the danger comes to the crew; in every Moonsick here the crew goes to the danger.
The critic could not break three things: the turned friend is the busiest player, the catch needs the wolf's own steering and voice, and "the furry friend sees the blooms but only clean hands can pick them".
Claude's pick for the next try is in the questions file: let the moon come to the friends.

### What changed in your setup
- The `critic-round` skill now has two critics: the comparing one (fun with friends) and the older hole-finding one.
- New shared folder `fun-with-friends-critic`: the judge's brief, the ladder of shipped games, their 14 sheets, the template for a new idea's sheet.
- `critic-baseline.md` rewritten: how the critic was checked, the seven things it looks for, how far to trust it.
- `critic-anti-patterns.md`: what the critic kept catching in the five sheets.
- New skill `tell-what-happened`; its triggers taken out of `explain-simple` and `project-postmortem`.
- The web session's patch is applied (the `fantasy-chain` skill and the notes of that session).

### What was checked and what wasn't
- Checked: the review counts (one fetch from Steam's store API); the rank match of the checklist score (a script); the 4 of 4 placement (the judge's report against the key).
- Worked by hand: the 0.94.
- Not ruled out: the judge may recognise famous games from their rules, and less popular games have thinner sheets. A new idea has neither, so a "yes" for a new idea is softer than those numbers.
- "New core act" was marked by Claude after seeing the review counts.
- Nothing was built or played. Every "yes" is a yes on paper; the real test is you playing a small build.
- Every idea is Claude's, the Moonsick fantasy line apart, which joins your own lines.
- No idea has a voice rule, because the friends are on Discord; every huge hit has one.

### Cost
About 30 agent runs: 5 for the write-ups, 10 for the checklist critic, 2 for the ranking and the kept-aside check, 7 for the idea rounds, and the first critic on the imps. After you asked to keep it cheap, each critic run got a short brief and no scripts, and the planned reruns of the 10 games were dropped.

### Where things are
- This run: `projects/game-design-research/critic-calibration-2026-11-18/` (notes, the critics' reports).
- The ideas: `projects/game-design-research/friendslop-ideas-2026-11-18/` (`sheets/`, `critics/`, `chain-check.md`, `notes.md`, and the open choices in `questions.md`).
- Moonsick: `projects/moonsick/friendslop-sheets-2026-11-18/notes.md`.

## What you asked for
| Your words | Tasks | Status |
|---|---|---|
| "run the critic on all top friendslop games and see if the score matches their popularity" | list + review counts; blind write-ups; one critic per game | done: 14 games, 10 scored by the old critic, all 14 by the comparing judge |
| "adjust the critic against the list and their popularity as the baseline.. it should roughly match" | score vs reviews; adjust from the table; check on the 4 held-aside games; update the critic skill and the baseline note | done: the comparing critic follows the list; skill and baseline note updated |
| "could you keep it cheap?" | 14 critic runs in all, short reports, no scripts | applied |
| "when you are finished. could you then come up with new ideas?" | new ideas with the adjusted critic, kept cheap | done: five sheets |
| "try to run until we have at least 3 good ideas" | keep making and checking ideas until 3 hold under the adjusted critic | **not reached: 2 hold** |
| "remember that we are trying to create friendslops" | the new ideas are friendslop: built from what the friendslop hits share in the table, not from what a strict critic likes | done |
| "i want to make moonsick work maintaining the idea of friends that has to survive the night and they can convert to werewolf as a friendshop. moonsick has to pass as one of the ideas" | rework Moonsick as a friendslop (friends survive the night, a friend can turn werewolf) until it holds under the adjusted critic; it counts as one of the 3 | **not reached: maybe after five versions** |
| "would be appreciated if its possible a moonsick variant as a 4th.. and appreciated if it is possible to make converting into werewolf the fear" | read as (Claude): 3 new ideas, and Moonsick as a 4th on top; in Moonsick the fear is turning into the werewolf (the fantasy line in moonsick/fantasy-first) | written; the fear of turning is the fantasy line, but a careful crew avoids the turn |
| "when finished even if it worked or not.. i need at the end publish to my github to an existing repo" | push the results to the existing GitHub repo at the end, whether it worked or not | not started |
| "also add into consideration the date it was created and novelty" | ladder now has release date and whether the core act was new; the critic checks novelty first | done |
| "popularity is a variable that changes through time and trends.. we are not trying to be accurate on that"; "we just want a critic skill to be able to tell if this idea is fun with friends or not" | the critic's verdict is now "fun with friends: yes / maybe / no"; the shipped games are its examples; novelty is a separate line | done |
| "moonsick B and moonsick A i except"; "moonsick A being the standard people are feared of transforming and need to help each other" | Moonsick A = sheet i04 (fear of turning, friends hold and cure each other); Moonsick B = sheet i05 (the wolf we need) | both written; both judged "maybe" |
| "critic is only to know if the game is fun.. i think we forgot to check if the fanatasy+feelings+choices make sense.. i believe you can check that on your own" | Claude checks fantasy, feelings and choices for each idea itself, apart from the critic (chain-check.md in the ideas folder) | done for the second versions |

## Log
- 01:24 AFK started; keep-awake on; 3 of 5 write-up agents done.
- 01:25 4 of 5 write-up agents done (11 of 14 games); critics started on g02 g03 g05 g07 g10, then g04 g06. New ask logged: run until 3 good ideas.
- 01:26 all 14 write-ups in; all 10 tuning critics launched (r1).
- 01:26 critics g05, g07 back. Moonsick ask logged.
- 01:27 critics back: g03 g04 g05 g06 g07 g10. Moonsick-as-4th ask logged.
- 01:28 all 10 tuning critics back; tabulating.
- 01:28 round-1 score vs reviews: Spearman 0.20 (weak). Simple sums from the table reach 0.53 at best. Publish ask logged.
- 01:30 ranking judge back: its order of the 10 tuning sheets follows the review counts closely (Spearman ~0.94, by hand; g01/g02 swapped, g06 two places low). Possible leak: missing-fact counts also follow popularity. Writing the comparing-critic brief; next the 4 held-aside games.
- 01:35 held-aside test: 4 of 4 tiers right. Date + novelty added to ladder and brief. Next: write the 4 idea sheets (3 new + Moonsick).
- 01:37 critic re-aimed at 'fun with friends' (user); idea sheets i01, i02 written.
- 01:38 4 idea sheets written (i01–i04); sending all four to one comparing critic.
- 01:44 user asked where the Moonsick variant is; wrote i05 (the wolf we need) as a second Moonsick.
- 01:45 critic r1 on 4 ideas: Hold On yes (conditional), Moonsick A / Piggyback / Gold Fever maybe. Writing v2 sheets.
- 01:46 v2 sheets written for all four; next my own fantasy/feelings/choices check, then critic r2.
- 01:48 Moonsick B r1: maybe (bite was a free reset); fixed. chain-check.md written for all five v2 sheets. Launching critic r2 on five sheets.
- 01:49 critic-round skill rewritten around two critics (comparing: fun with friends; hole-finding); critic-baseline note rewritten.
- 01:54 critic r2: Hold On yes; Moonsick A, Moonsick B, Gold Fever, Piggyback maybe. Piggyback dropped. v3 sheets written for the other four; launching critic r3 (last round).
- 02:02 critic r3: Hold On yes, Gold Fever yes (narrow), Moonsick A maybe (top C), Moonsick B maybe. One more targeted round on Moonsick A.
- 02:07 critic r4 on Moonsick A: still maybe (waiting in shade; turn-on-purpose). Went one step higher: v5 has no fur meter (beam = 10 s fit, two friends hold). Launching r5 on it; this is the last run.
- 02:11 critic r5 on Moonsick A: maybe. Stopped. Critic files moved to shared/fun-with-friends-critic. Summary written. Next: push to claude-setup.
