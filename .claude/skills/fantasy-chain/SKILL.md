---
name: fantasy-chain
description: Design a game from its fantasy (fantasy, then the feelings that sell it, then research on games that already cause each feeling, then the choices that cause those feelings), or check an idea, rule or change against the user's chain - logic and aesthetic cause actions, actions cause feelings, and the feelings sell the fantasy. Use whenever the user says "what should the fantasy be", "define the fantasy", "fantasy, feelings, choices", "choice lines", "brainstorm choices", "which games recreate this feeling", "games that make you feel X", "does this fit the fantasy", "why doesn't it feel like X", "check the chain", "fantasy, logic, aesthetic", or when a core choice, mechanic, rule or look is proposed or changed, or a playtest feels wrong ("there is no real fear", "it doesnt feel like a game of bluff").
---

# Start from the fantasy, and follow every rule to the feeling it causes

A rule can read fine and still cause the wrong action, and then the wrong feeling.
Moonsick's rules read fine, the best action was "cure at the first symptom", and nobody felt fear.
The chain is the user's own model; use their five words.

## The chain (picture: `chain.png` in this folder)
| Step | What it is | Leads to |
|---|---|---|
| Logic | the rules | actions |
| Aesthetic | look and sound | actions (it tells players what they can do), and feelings directly |
| Actions | what players do and expect, their own and other players' | feelings |
| Feelings | what players feel | fantasy |
| Fantasy | what the group of feelings sells | nothing: it only changes when an earlier step changes |

Logic has no direct line to feelings.
Players touch the rules through actions and see the rules through the aesthetic.

## Designing: fantasy, then feelings, then research, then choices
Use this order when a core is being found, before any rule exists.
Choices written without a fantasy got thrown out one by one, each for a different reason, because nothing said what they were for.

1. **Fantasy.** One line, written by the user: the situation the players are in and what they want in it.
   Claude doesn't write it or reword it.
   For a co-op game the line itself says what one friend needs from another: something a friend has, sees or can do that I can't (user).
   Test: say the line with one player in it. If it still works, the friends are only in the same place, and the line fails here ("we are burglars in a dragon's cave" works with one burglar; "each of us is only brave next to a friend" doesn't).
   Why: nine ideas checked co-op only at the choices step; the fantasies said "we" without a need, so the choices built on them never needed a friend.
   Check it first for one player being asked to want and fear the same thing; where a game makes that work, the two sides are opponents.
   Search the premise now, before any choice: a shipped or announced game with it gets "taken" or "different because X", never just "near".
2. **Feelings.** The two to four feelings that sell that fantasy.
   Claude proposes them, tagged "(Claude)", and the user decides.
   For a co-op game every feeling is a feeling about a friend, and names that friend's part in it ("I trust what Ana says is behind me", "I let Ben down") (user).
   A feeling one player has alone (held breath, greed, dread) fails here, or is rewritten until a friend is in it ("greed" becomes "I want one more and Ben is the one who pays for it").
   These are the wanted feelings; the Feelings step of the chain is what play gives back, and the gap between the two is the finding.
3. **Research each feeling.** Before writing any choice, look up games that already cause that feeling well (the `design-research` skill, with the feeling said in general terms as the problem).
   Bring back what each game does, where it is used, and how it fails.
   Write the relation between the players next to each game (one crew, rivals, one against many); a game where the players are rivals doesn't back a feeling for a crew that wins together.
   Look for the feeling between friends, not the feeling alone: a game that causes dread in one player doesn't back "I fear for Ben".
   Write what forces the moment in that game (an enemy, level content, split information, a clock) in the same row, now and not at the choices step.
   Say so plainly when no game does it: a feeling nobody has built is a risk, not a free field.
   A game found for a feeling shows a rule that works somewhere; it is not a pass for the idea.
   Why: Claude wrote six ways from its head and each was thrown out, and one search then found shipped games that already answer the same question.
4. **Choices.** Lines a player faces ("do X, or do Y?"), each made to cause those feelings, starting from what the research found.
   Take the choice from the researched game: copy what forces the moment there first, and only then change the setting; a new rule that only sounds like it causes the feeling is a guess.
   The choice line names the friend from the fantasy's need ("pull it off Ben, or finish my own rope"); a line with no friend in it fails.
   Before any mark, find the best move at the fewest players, at the most, and with one human and bots, and the plan a crew settles into after five nights.
   Run the older checks too (the idea search's checks: something gets worse when nobody acts, no decoy, no threat that hunts whoever did the last thing, not a place to reach, lag).
   Run every reason an earlier idea was dropped for against every idea still standing, with the dropped list open; "none found" from memory was wrong three times.
   Write each rule the choice leans on in one sentence first; a check on an unwritten rule fails.
   Write what each end of the choice decides in the same second; an end that stands still, holds or follows fails.
   Assume the friends are on Discord: nothing may lean on who can hear whom, and speech can't be the price.
   Work out any ratio the choice turns on; "depends on the numbers" is a fail.
   Check each fix against the fantasy line and against the other fixes, not only against the finding it answers.
   Write the round a perfect crew plays; if the core act is a mistake they avoid, the idea doesn't happen in it and fails.
   When a person is put on the other side, write the act one friend does for another; with none, the cooperation is gone.
   A toy script counts only if it holds both sides of the written choice and the price of each.
   Next to each cited game, write what forces the moment there (an enemy, level content, split information), and check this idea has it.
   Then mark each line ✅ or ❌ per feeling: does the best move leave that feeling alive?
5. **When a check fails, go back, and write the path down** (user).
   Name the step that caused the fail: the choice, what forces the moment, a feeling, or the fantasy.
   Go back to that step, write a different option there, and run forward again; a rule added at the bottom to answer one finding is a patch, and patches were thrown out as bolted on.
   Keep one path file per idea: each branch gets a line with the step it changed, what it tried, where it failed and why, in the order tried, so no dead end is tried twice.
   Three tries at one step, then go back one step higher.
   When the same reason kills several branches, stop fixing that spot and try a different one (user): a different option one step up, and a different idea when the fantasy is what keeps failing.
   Two stages (user). Stage 1: Claude's own checks are the fail signal; they can kill a branch and can't pass one.
   Stage 2: a branch that survives stage 1 goes to an isolated critic, and each severe finding is the next fail to go back from, through stage 1 again.
   Repeat until a critic round has no severe finding, at most three critic rounds, and write the critic's round into the path file as its own rows.
   Count the fail reasons across branches at the end; a reason that ends every branch belongs to the limits, not to the idea, and goes to the user as that.
   Why: two runs marked every idea failed after one pass and never looked for a way through.

Hard rules:
- No rule, item or job is added until a choice passes every feeling.
- A choice that needs something the fantasy doesn't ask for fails there (a tool, a job or a resource carried over from an older version).
- A choice whose best move removes a feeling fails, even when the line reads well.
- A problem with the base (one seat making every call, a feeling with no game behind it) is a fail until fixed; only tuning questions may be listed as unproven.
- A critic's fail on paper doesn't show an idea is bad: the same critic failed a shipped hit's loop on its design alone (7 severe). Use a critic round for its concrete holes and for what it couldn't break, not as the pass gate; the pass gate is the user playing a small build.
- This order has only thrown choices out so far; it hasn't yet produced one that held in play, so a pass here is a pass on paper.
- In an AFK run where Claude wrote the fantasies, critics failed all nine ideas over four rounds, the idea pool's top-ranked one among them: the research ticks were read as passes, and the scenes were written to show the feeling.
- A fail is followed by going back (step 5), not by dropping the idea at once; an idea is dropped when its fantasy step has had three tries, or when one reason has ended every branch.

Reply for designing: the fantasy line with the need between friends marked, the feelings, the games found for each feeling, then one table of choice lines with one ✅/❌ column per feeling, and failed lines listed under it with what they failed.

## Checking: steps
1. **Write the fantasy** in one sentence, in the user's words.
2. **Say where the thing being checked sits:** logic or aesthetic.
3. **Follow it forward:** the action the best player takes, the feeling that follows, and whether that feeling matches the fantasy.
   Play the action out as one scene (the `game-dev` skill, design sketches); don't guess it from how the rule reads.
4. **For a playtest that feels wrong, follow it backward:** from the feeling, to the action, to the logic or aesthetic behind it.
   Find out which of the two it is before fixing anything.
5. **Cut test:** a rule that no action triggers and nothing on screen shows can go, since no player can feel it.
6. **Never split the chain to test a part alone;** the user turned that down (`~/.claude/domain-knowledge/game-idea-triad.md`).

## Reply for checking
One small table, one row per step of the chain: what it is here, and "Matches the fantasy?" with ✅ or ❌.
Then the first step that breaks, in one line (coworker style).
