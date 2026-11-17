# Critic round 2 on Imps (version F3), blind, measured against the baseline

Read: `proposal-imps-r1.md`, `critic-baseline.md`, `design-anti-patterns.md`, `critic-anti-patterns.md` without its last section.
Numbers: the proposal states none, so the critic picked them and ran a toy script (`/tmp/claude-1000/-home-akiraki-claude-code/e55b81b3-a395-4223-a5b1-47dba7e160fd/scratchpad/imps.py`, a temp file).
The picked numbers: night 300 s, 1 fruit per 2 s, basket 10, tree to cart 10 s, slap 2 s, imp grows big in 60 s unmet, slap spills 1/3, a big imp tips the basket after 5 s.
The cited games were judged from memory, not searched (assumed); Cursed Companions is unchecked.

## 1. The problem underneath
The fantasy needs a friend: one picker can't be slapped and has nobody to be named, so the one-player test holds (checked on the rules as written).
No player wants and fears the same thing (checked).
The feelings are not backed by the cited games, and that is the base problem.
"Get it off me": the Snare Flea and the Jockey arrive by surprise and kill; this imp is always there, grows on a clock the friends read out loud, and costs a basket.
"Sorry, sorry": in the cited games the harm is an accident of aim under an enemy's pressure; here the spill is certain, known and agreed, so it is a tax and nobody says sorry.
"Mine wants you": the proposal's own row says ❌ no silence and no monsters, and still marks the feeling ✅; the only pressure left is a dawn clock with no number.

## 2. Against the baseline
Worse than the baseline: all four parts the critic couldn't break in the hit are missing, and a crew that walks together meets most of the list for free.

## 3. The four baseline parts
| Part | Present? | Why |
|---|---|---|
| A help with real prices that happens on good nights | ❌ | The slap has one price, it falls on the helped friend, and it is zero on an empty basket; the slapper pays 2 s; a perfect crew doesn't need the slap at all (finding 1). |
| A pressure that rises and breaks last night's plan | ❌ | No quota, no cart size, nothing grows from night to night; night 5 is night 1. |
| Two threats at once, so one pair can't cover both | ❌ | One kind of threat, on a visible clock; two big imps are the same slap done twice. |
| Something carries from one night to the next | ❌ | Nothing is written: no cash, no debt, the imp is new each night. |

## 4. Findings of this design alone

**Severe 1: walking together meets the list, and the "pair that can't both be met" can be met.**
Four of the six shown wishes are distances or places (arm's reach, same tree, nearer the cart twice).
"Ana never nearer the cart than Ben" and "Ben never nearer than Ana" are both met at equal distance; the proposal's own scene says so ("walk beside him step for step").
Played at 3: Ben takes Cy's basket, Ana walks beside Ben, Cy has no basket and walks along; every wish is met, no imp grows, no slap happens.
So the perfect crew's round has no slap, and the proposal's ✅ on that line is wrong.
If equal distance does not count, lag (~0.2 s) flips the wish many times a second and nobody can meet it; either reading fails.
This is "standing in places counted as co-op" (B24) and "a perfect crew's round is one where the idea doesn't happen".
Fix direction: wishes that take an act from the named friend at a price, never a distance; the forced growth must come from outside the crew's control.

**Severe 2: the three feelings have no cause in the rules (section 1).**
Example from play: Ana says "yours is nearly big, empty your basket first"; Ben empties it, Ana slaps, nothing spills, nobody shouts.
Fix direction: the harm in the help must be chancy and land on something that can't be put down; the moment must come unannounced.

**Medium 3: three big imps at once lock the night at 3 players.**
A big imp takes the legs, so if all three are big nobody can slap.
Script: 3 players, nobody obeys, equal start: all big at 60 s, 241 of 300 s locked, cart 30 of 210.
Fix direction: write what happens when nobody can slap (a big carrier can still slap, or the imp drops off after the tip).

**Medium 4: rules not written, checks marked passed on them.**
Can a small imp be slapped? What does Cy do with no basket? Do ties count? How fast does it grow? How big is the cart? Can a night be lost?
If a small imp can be slapped: slapping at the cart on empty baskets keeps 99.9% of a no-imp night (script), and the imps do nothing.
If only a big one can: ignoring every wish as a group keeps 89% at 3 and 90% at 6; obeying "carry my basket" keeps 79% at 3.
Slapping beats obeying a costly wish in both readings, so "take the basket or slap" has one answer.
The loss only bites with fast growth: at 20 s to big the group keeps 56%, at 120 s it keeps 97%; this ratio decides the game and isn't in the proposal.

**Medium 5: rule 5 (hear the wish, can't see the size) does no work.**
On Discord the carrier reads the wish out at the deal and friends call the size, both free and both wanted by everyone.
The proposal says itself that no feeling leans on the size; by the essence test the rule is cut.

**Medium 6: the slap is a free draw from the list.**
On an empty basket a slap costs 2 s and deals a new wish, so the crew slaps until a distance wish comes up.
Fix direction: the new wish costs more than the old one, or the slap can't be repeated for a while.

**Minor 7: blame from luck.**
The deal decides whose imp grows; the walked friend did nothing wrong.

**Minor 8: scale at 6.**
Six wishes name six friends unevenly: one friend is named three times, another never, and the unnamed one with a distance wish just picks fruit.
Six wishes read out at once at the deal is 20 s of talk, then quiet.

## 5. Findings the baseline has too
- The slap is free once the friend empties their basket (row: a help is free when the helped friend puts their load down first).
- By night 5 the crew holds a card, one row per wish (row: the crew settles into fixed roles with a card of answers).
- The slapped friend only turns their back, and the friend named by a distance wish only gets followed (row: one end of a choice only stands); co-op check point 7 fails.
- "Obey or slap" is one sum of fruit lost (row: a choice is one sum for the whole crew).

## 6. Breached limits
- **At most ~3 taught rules (severe):** six numbered rules plus about fifteen wishes, each a rule the carrier and the named friend must both understand.
- **Goals are never places to reach (severe):** the job is carrying fruit to the cart, and most shown wishes are places or distances.
- **Testable by 1 human + bots (medium):** the wish and the size cross only by voice; a bot can't hear the human's wish or tell the human their size, so bots must read the game's data or get a new sign verb.
  The slap, the carry and the walking are physical and bots can do them.
- Low content holds as one list, but rule 6 needs every pair of fifteen wishes sorted into "can both be met" by hand (105 pairs, times who is named), with a bot habit per wish.
- Speech is not the price ✅; no joint physics ✅ (distance wishes need a lag margin).

## Co-op check (design-anti-patterns C)
1. Coupled: pass for the slap; fail for distance wishes, which the carrier meets alone by following.
2. Split: pass (anyone can slap), though the hear/see split is undone by one sentence.
3. Talk: fail; one reading at the deal, then "yours is big", and no number for the clock.
4. Blame: pass; a walked friend and a tipped basket are seen as they happen.
5. Not easy: fail; no way to lose is written and nothing gets harder.
6. Not solo: pass; nobody can slap their own imp.
7. Two-way: fail; one end turns their back or gets followed.
Lone survivor: fail (finding 3).
Dying on purpose: letting the imp go big on an empty basket is the cheap move.

## The three asked-for plays
- **The strategy that always wins:** everyone picks from one tree, walks to the cart side by side, and slaps there on empty baskets.
- **The plan by night 5:** read the wishes at the deal; a distance wish is met by the group walk; any other wish is slapped at the cart until a distance wish comes.
- **The perfect crew's round:** no imp gets big, no fruit spills, about 100% of a no-imp night.
- **6 players:** the same group walk; six abreast on the way to the cart meets every "nearer the cart" wish at once; 90% kept even while ignoring all wishes.
- **1 human + bots:** bots slap the instant an imp is big and never misjudge, so the night is clean; the human learns their imp is big when their legs go, because no bot can say it.

## 7. What I could not break
- The one-player test: the imp only comes off by a friend's hand.
- Nothing is priced in speech, and nothing needs joint physics.
- The slap, the carry and the spill are verbs a bot can do and a friend can see.
- One arena and one list.
- The new wish after a slap is a real surprise inside a night; it just costs nothing to draw again.

## 8. The smallest change that would move the verdict up (the critic's opinion)
Put the slap's price on the slapper and on something that can't be put down: the slapped imp lands on the slapper's back as a second rider, so every help makes the helper the next one in need.
Replace distance wishes with acts the named friend pays for, and add a cart quota that rises each night so last night's walk stops paying.
That gives back two of the four parts (a priced help on good nights, a rising pressure); the other two would still be missing.
