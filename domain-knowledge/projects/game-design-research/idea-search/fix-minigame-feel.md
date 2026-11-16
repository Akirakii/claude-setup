# Fix for "feels like a Mario Party minigame" and "difficult, not funny" (2026-11-11)

Thesis → inline critic → synthesis (RULES 13; inline because the user said no subagents for idea work).
Diagnosis: `research.md` 2026-11-11 entries. Status: sketch shown to the user, skill not edited.

## Thesis (v1, Claude)
Add a between-rounds layer to every idea (a stake that carries over and grows, a slower choice between rounds),
raise the systems cap from "≤ 2 extra rules" to 4–8, allow generated places, replace "nobody idle" with "someone
free to watch", move the cost out of the round, add funny checks (mishap on a body, seen cause, cheap, watched).

## Critic (frame first; design-anti-patterns.md, critic-anti-patterns.md, user verdicts)
1. **Severe, frame (B13 layers instead of core).** A between-rounds layer on a one-rule round is Mario Party
   itself: minigames + a board. In Lethal Company the outer stake matters because it changes what you do inside
   the round (behind on quota → riskier moon, stay longer). A layer that only adds to a score fixes nothing.
2. **Severe, user's pillar.** "Reach somewhere = completing a level = medium to high content" (user, 2026-11-10).
   "Allow generated places" drops it, and a generator is real work (Harbor Jam's weak spot).
3. **Severe, user's verdict (B24).** If the friend rule becomes "one moment among others", the round can drift into
   parallel play with occasional contact: DRS v1, "requires no cooperation at all".
4. **Medium.** "Someone free to watch" brings back idle players at 6. Critic memory: "the dead get only a voice".
5. **Medium (fixing each finding by adding a rule).** 4–8 systems can mean 4–8 rules to teach.
6. **Medium (dominant strategy between rounds).** With a quota, "always play safe" or "always max greed" can win
   (a Lethal Company guide: five safe runs beat one greedy run).
7. **Honest label.** Funny can't be judged in words (Quinn: a joke lands once; game-idea-triad memory).

## Synthesis
1. The round is a situation, not a closed contest: it has a **push choice** (how far, how long, how much to take).
   The carry-over must **change that push choice next round**. Test: "if the round's result only adds to a score,
   it is still a minigame."
2. Keep the user's rule: one place, ≤ 3 arenas, no levels, no generated places. The between-rounds layer is a
   stake (a debt, a quota, a season), and the port or camp between rounds is a menu, not a level.
3. The friend rule stays the hub and the round's main danger; every other system only makes the hub riskier or
   easier, never changes what it does (the user's graph model). The player gate is unchanged.
4. "Nobody idle" becomes "an out player has a physical job" (e.g. overboard: sees the next wave from the water,
   calls it, grabs the thrown rope). The time out is short and is itself a friend moment (the rescue).
5. Systems: hub + up to ~6 things in the world; the rules a player must be taught stay ≤ 3.
6. No fixed plan at both levels: the stake rises each round (safe play falls behind) and something dealt each
   round (storm, cargo) moves the right amount of greed.
7. Funny checks are marked "~ at best in words"; the real check is a tiny build (offer, don't push).
No severe finding left after this round: 1 is the new first check, 2 keeps the user's rule, 3 keeps the gate.

## Example: Storm Sailors as a full game (Claude)
- **Run goal:** the crew owes the ship's owner; each voyage the owner wants a bigger share. Miss it and the ship is
  taken.
- **Round (one storm, a few minutes, the same deck every time):** haul ropes to trim sails, lash sliding crates,
  plug leaks. Hub: every haul swings a boom; haul now and knock a friend flat toward the rail, or wait for them to
  duck. **Push choice:** full sail (faster through the storm, more booms swinging) or reefed (fewer booms, the storm
  lasts longer and the leaks pile up).
- **Carry-over:** crates lost overboard, torn sails and holes stay. In port: spend the money on repairs, or pay the
  owner, and choose how much cargo to load. More cargo = more value and a more crowded deck = more sweeps. Behind on
  the debt → you load more → next storm is harder.
- **Funny:** knocked flat, sliding, flipped over the rail (on a body, the hauler seen); overboard is 10–20 s in the
  water, yelling the next wave, then pulled up by a friend's rope (cheap, watched, a rescue).
- **Systems (7):** booms (hub), crates, leaks, overboard + rope, port choice, rising debt, dealt storm. Each makes
  the boom moment riskier; none changes what a haul does. Taught rules: haul swings the boom; duck; throw the rope.
- **Scenes:** 3 players: one overboard leaves two, one stops hauling to throw the rope, sails flap. 6 players: a
  crowded deck, more knockdowns, one in the water calling waves. Lone survivor can still bail and haul to port.
- **Co-op gate:** coupled ✓, split ~ (only the overboard view), talk ✓, blame ✓, not easy at 3 (assumed), not solo ✓,
  two-way ✓. Dominant strategy: unknown until played (how much cargo is right).
- **Pillars touched:** "≤ 2 extra rules" (Claude's check, not the user's words) becomes ≤ 3 taught rules + world
  things; "nobody idle" and "both sides cost" (Claude's checks) change as above. Scope grows from 1 rule to ~7
  systems: closer to Content Warning (~2 months, 5 people) than to a jam game; netcode cost not counted.

## Second look (user: "is this too biased to this current session worriness?")
Claude's view: partly yes. The minigame shape is in the check text (not a mood), but the cure above (debt + port +
7 systems) copies Lethal Company, the game just researched. Smaller hits show a smaller minimum: Liar's Bar is one
rule with a stake that rises over the match (each pull of your own revolver is likelier to fire; from memory).
"Funny" came from one question and can't be checked in words. Recommendation: no skill rewrite; write a "what
rises over the match" line by hand for 2–3 top hubs; keep funny as a note, not a check; keep "nobody idle" and
"both sides cost" until play says otherwise.

## Over the match: test lines for the top 3 (2026-11-11, user: "ok proceed")
A match is a few rounds in a row. Each line adds one rule: a stake the crew's own play raises, which changes the
choice next round (the Liar's Bar minimum). No push choice, no economy, no new place. Numbers are starting values
(Claude). Funny notes are notes, not checks.

### Thesis
- Storm Sailors: a sail that flaps tears, tears stay, a torn sail slips faster.
- Hermit Crabs: a gull that catches a bare crab takes a leg; legs stay lost.
- Swap Wizards: islands that fire covered tonight crumble before the next night.

### Critic (inline; frame first, then each line)
1. Frame, medium: a rising stake without a push choice may still feel like the same round five times, harder.
   Kept on purpose as the smallest test; if it still feels like a minigame, the push choice is the next thing to add.
2. Swap Wizards, severe: "covered tonight" is vague, and fire spreads, so most islands would fall at once. Fixed:
   each crossing leaves a crack; three cracks and the island falls, between nights.
3. Hermit Crabs, severe: a crab missing legs is slower, so it gets caught more: a spiral with no way back that ends
   with one player useless. Fixed: a lost leg grows back when the crab moves into a bigger shell, which takes the
   friends' chain.
4. Storm Sailors, medium: "spread the rips evenly" (share evenly) could be the card. Bends: the dealt wind says which
   sails need hauling and the ropes are rigged anew, so the crew can't pick which sails flap. ~
5. All three: does playing the first rounds safe keep the stake low? No: each round's goal still forces the risky
   act (haul, chain, swap).
6. Storm Sailors, open (older gap, not this test): what going over the rail costs is not defined; funny needs it cheap.
No severe finding left.

### Synthesis (the lines)
- **Storm Sailors, over the match:** A sail that flaps for more than two seconds gets a rip, and rips stay from storm
  to storm; a ripped sail slips loose faster, so its rope must be hauled more often and its boom swings more often.
  In the first storm, waiting for a friend to duck costs a little canvas; by the fourth, the ripped sails slip so fast
  that every wait rips more, and the crew has to choose whose sail they let go. Bring the ship through the season's
  five storms with every sail still on its yard (five rips tear a sail off).
  *Funny note:* knocked flat by a friend's boom, you slide down the tilting deck toward the rail, arms flailing, until
  someone grabs your ankle; everyone on deck sees the boom, the slide and who hauled.
- **Hermit Crabs, over the match:** A gull that catches a bare crab takes one of its legs, and a lost leg grows back
  only when that crab moves into a bigger shell; at its third lost leg the gull carries the crab off, and the week is
  lost. A three-legged crab runs bare in a lopsided zigzag, so at the next tide the crew must move it up first, and
  whoever is next in size has to climb out early to make room. Keep the whole colony through the week's five tides.
  *Funny note:* a three-legged crab zigzags across the sand under a growing gull shadow while the colony watches from
  their shells, yelling which way to turn.
- **Swap Wizards, over the match:** Each time fire crosses an island it leaves a crack in the stone, and between
  nights every island with three cracks falls away into the dark; the sparks your swaps leave make most of the
  cracks. Each night there's less floor for two wizards per island, so a swap that was cheap on the first night can
  cost the crew an island on the fourth. Relight the great lamp, night by night, before the islands left can't hold
  the whole crew.
  *Funny note:* you swap a friend onto the island next to a spark, and they hop from foot to foot as the flames reach
  their robe, while the two-color flash shows everyone who did it.

### Scenes (smallest and largest crew)
- Storm Sailors at 3: by storm 4 the jib has three rips and slips every second; Cy hauls it nonstop and its boom
  sweeps the bow where Ana's rope is. At 6: two ripped sails make two "hot" booms; the crew argues whose to let go.
- Hermit Crabs at 3: S lost a leg at tide 2; at tide 3 M climbs out early so S can move up and regrow, and M runs bare.
  At 6: a three-legged crab in the middle of the chain holds up everyone below it.
- Swap Wizards at 3 (needs 2 islands of 5): the floor lasts; cracks decide which islands are safe to swap from. At 6
  (needs 3 of 8): by night 4 the crew is down to 4 islands, and every swap's spark is on ground they can't lose.
- Co-op gate: unchanged from each idea's pass (the new rule adds no new act, only raises the stake of the old one).
