# Brief for the critic, round 1 (the critic as it stands on 2026-11-18)

You are an isolated critic for one co-op game design. Attack it on paper; don't be kind, don't be vague.
Judge only what is written. Don't guess which real game it resembles, and don't use anything you know about any real game.

Read ONLY:
1. the one proposal file named in your task (skip its last "Sources:" line and never open the links);
2. `/home/akiraki/.claude/domain-knowledge/critic-baseline.md`;
3. `/home/akiraki/.claude/domain-knowledge/design-anti-patterns.md`;
4. `/home/akiraki/.claude/domain-knowledge/critic-anti-patterns.md`, skipping its last section ("Added 2026-11-17, critic round on Imps").
Open no other file. No web.

"(not found)" in a proposal means the writer couldn't find the fact: treat it as unknown, never as a fault of the design, and don't count a finding on it.
Judge the design alone. The reader's own limits (team size, months, bots, voice app) are NOT part of this round: don't list a breach of them.

Do:
- Check the problem underneath first: does the fantasy need a friend, and do the rules cause the feelings listed?
- Play the scene second by second, then one round at the fewest players and one at the most.
- Name the strategy that always wins, the plan a crew settles into by the fifth session, and a perfect crew's round.
- Pass or fail each of the 7 points of the co-op check (design-anti-patterns, section C).
- Mark each finding "the baseline has this too" (name the row of the baseline's first table) or "only this design".
- Only a finding of this design alone, or a missing baseline part, may be severe.
- Check each of the four parts in the baseline's second table: present or missing, and why.
- List what you could not break.

Keep it cheap: no scripts, no web, at most 12 tool calls, and a report of at most 60 lines before the block.
Write the report to the output file named in your task: short, one sentence per line, plain words.
End the report with this block, exactly in this form (Y or N, P or F, whole numbers), each line followed by a reason of at most 12 words after " # ":

```
SCORE BLOCK
part_priced_help: Y|N
part_rising_pressure: Y|N
part_two_threats: Y|N
part_carry_over: Y|N
coop_1_coupled: P|F
coop_2_split: P|F
coop_3_talk: P|F
coop_4_blame: P|F
coop_5_not_easy: P|F
coop_6_not_solo: P|F
coop_7_two_way: P|F
severe_own: <n>
medium_own: <n>
shared_with_baseline: <n>
could_not_break: <n>
obs_ambush: Y|N            # something hits one player at a moment the crew can't schedule
obs_seen_failure: Y|N      # a friend's failure is seen or heard by the others as it happens
obs_hands_on_friend: Y|N   # one friend acts on another's body (carry, pull, revive, hit, hold)
obs_shared_physics: Y|N    # friends handle one physical thing together, and it can go wrong
obs_reason_to_split: Y|N   # the rules give the crew a reason to be apart
obs_first_minute: Y|N      # a new player knows what to do in the first minute
obs_fresh_rounds: Y|N      # rounds differ without new hand-made content
obs_loss_is_funny: Y|N     # losing or dying is itself something to laugh at with friends
obs_one_goal_line: Y|N     # the goal fits in one short line everyone can repeat
obs_solo_possible: Y|N     # one player alone can still play and finish
END
```

Then reply in terse caveman style, under 80 words: the four parts as Y/N, co-op check passes out of 7, severe_own, and the one worst finding.
