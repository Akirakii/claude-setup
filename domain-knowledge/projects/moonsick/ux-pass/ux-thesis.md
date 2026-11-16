# UX thesis v1: show the loop, from each player's own knowledge (Claude, 2026-11-12)

User: "i dont understand what to do in the game.. could you improve about readability and UX?" (2 h run).
Research: `docs/ux-research.md`. Rules: `docs/design.md` (v2.3). No rule changes in this thesis.

## Frame
One loop must be learned: **a friend shows signs -> you collect them -> they leave 1–2 creatures -> fetch that cure
-> give it** (and when someone turns: raise its cure or stay with the group). Today every step's information is
spread, hidden or gone in seconds (claims are 4 s bubbles, faces are dark, the journal is a % table to multiply,
cure spots are unmarked, tool reads are a 3 s toast, the hands read `[—] —`, nothing says what to do now).
Fix: make the loop's state visible to each player **from what that player alone has heard, seen or read**, and teach
it at the moment of need. Replace text, don't add it.

Premise check: the user may be confused by the rule load, not only the screen. A new player meets 8 signs, veins,
3 cures, 3 creatures, tools, holding, pans, shoves, powers, head starts, tricks, scars, the pond. This thesis keeps
the rules but stages them (the loop first, the rest found in play). If the user still can't follow after this,
the next step is cutting rules, not more UI (critic memory: "stacked hidden rules, patched with words").

## Changes (all Claude)
1. **Case notes replace the journal table** (Tab, plus a small card when you aim at that friend). One row per friend
   you have evidence on, filled automatically only from:
   - *said*: their quick-chat claims you heard (within 15 m, the bots' range), with how long ago;
   - *seen*: outer signs and veins your look readout (2) showed you;
   - *tool*: your own spoon / thermometer reads.
   The row ends with what's left: "werewolf or vampire -> wolfsbane or garlic", or "vampire -> garlic", or "doesn't
   fit: a trick, a lie, or a scar?". Never a %, never "is lying". Claims stay "said". Notes clear when the friend is
   cured, turns or dies. A small sign legend (no %) stays at the bottom: sign -> the creature it rules out.
   Not synced between players (each has their own; talk shares them).
2. **Look readout:** aim at a friend within 5 m: one line under the crosshair, e.g. "Bo: eyes shine · veins on neck",
   "Bo: nothing on the face", "Bo: too dark to see skin". Same visibility rule the bots use (eyeshine: out of
   moonlight or within 2.5 m; grey skin and drool: in moonlight or within 2 m; veins: within 4 m). Writes into (1).
   Scars look like signs (unchanged ambiguity).
3. **Now line** (one line, ≤ 8 words, top centre), chosen by priority from your own state and notes:
   creature / caught / held / knocked out (exists) > "Werewolf out! Raise wolfsbane or stay grouped" > you feel an
   inner sign: "You feel night sight: press 1 to tell" > you hold a cure that fits a noted friend: "Give Bo the
   garlic: hold LMB on Bo" > a noted friend with 1–2 creatures left: "Bo: get garlic (kitchen, cellar)" > only a
   claim: "Bo said a sign: go look at Bo" > empty hands: "Pick up a tool or a cure (E)" > "Watch your friends' faces".
   On in every mode; "Hints" toggle in the Esc menu.
4. **Hands:** "Left: garlic (cures vampire)  ·  Right: empty", the active one bright; tools say what they read
   ("silver spoon: reddens skin?").
5. **Labels on items in the world:** within 10 m, a small name over each item ("garlic", "pan").
6. **Feed** (top left, 4 lines, 10 s each): public moments you could witness: claims within 15 m, cures given /
   checks / grabs / pans within 15 m (the story's own lines), and every turn and death (everyone hears them).
7. **Practice coach** (practice nights only): a 5-step list top left, ticked by doing: 1 pick up a tool or cure (E) ·
   2 when a friend says a sign, look at them · 3 check them with your tool (hold LMB) · 4 get the cure your notes
   name · 5 give it (hold LMB; they hold still). Then: "Soon you'll feel a sign: tell them (1–4)."
8. **How to play** rewritten as the loop in 3 steps; the old 4-instruction tip line is removed (3 replaces it).

Word budget: the now line ≤ 8 words, the readout ≤ 6, feed lines ≤ 9, coach steps ≤ 8. Removed: the tip line,
the journal's 3-line footnote and its % cells.

## Scenes
- **Practice, 1 human + 5 bots, 0:25:** a bot says "I crave raw meat". Feed: "Cy: I crave raw meat". Now line: "Cy said
  a sign: go look at Cy". Coach step 2 lit. You walk up: readout "Cy: eyes shine · veins on neck". Notes: Cy — said
  craving, seen eyeshine -> werewolf -> wolfsbane. Now line: "Cy: get wolfsbane (pond)". You fetch it; "Give Cy the
  wolfsbane: hold LMB on Cy".
- **8 humans online, 6:00:** two friends sick at once. Ana heard Bo's claim but never saw Bo's face; Cy saw Bo's
  grey skin in a moonbeam. Ana's notes: Bo — werewolf or troll. Cy's: Bo — vampire or troll... they talk: troll ->
  rowan. Each player's notes differ by where they stood.
- **Smallest (2 humans, practice off):** same, no coach.

## Pillar check
Liars never exposed (notes say "said", "doesn't fit" names no one); trust until dawn (unchanged rules); signs hard to
read (the ambiguity stays: tricks, lies, scars, pond cold, the one-sign lean; only the bookkeeping goes); helping
beats fleeing (unchanged).

## Critic round 1 synthesis (2026-11-12 13:30; critic report summarised here)
| Finding | Decision |
|---|---|
| S1 the now line plays the game (names the cure on a one-sign lean; "obey the line" wins; kills the cure-now-or-wait choice) | Fixed: no always-on line. A practice coach teaches each verb once and never names a cure or says which to give. |
| S2 frame parked: rule load answered with UI only | Fixed: practice lessons stage the rules themselves. Lesson 1: signs, cures, the creature (no tricks, scars, doubles, powers, pans). Lesson 2: + tricks, scars, pans. Lesson 3+: everything. Online is unchanged. |
| M1 auto "what's left -> cure" = a checklist (the user's "too easy") | Fixed: notes are a log (said / seen / tool, with ages), each fact tagged with the creature it rules out; combining stays the player's act. |
| M2 "go look at Bo" pulls 8 players to one friend; gates 2, 3, 6, 7 weaken | Fixed: only the coach says it, only in practice. |
| M3 stale notes nag (tricks, scars, healthy friends) | Fixed: the bots' fading: a claim fades after 35 s unless veins back it, "I feel fine" takes claims back, no veins up close clears veins. |
| M4 copying the bots' rule leaks scars and far cures | Fixed: distance and light only; scars read as signs; notes clear on a cure only within earshot; `trick` never read. |
| M5 no total word budget | Fixed: transient text (coach, feed, readout, toasts, banners) ≤ ~25 words at once; feed 3 lines (critic said 2; Claude kept 3 since claims are 4 s bubbles); hands, aim prompts and item labels not counted. |
| M6 the % per sign (user pillar) silently dropped | Fixed: the % table stays in Tab under the notes. |
| M7 the patient's side missing | Fixed: the coach tells a sick player to stay by a friend and hold still; "press 1" only in practice. |
| m2 the feed's "Nothing happened" is a public test | Fixed: the feed only reports results that show on the body (cured, shudder, burst); "ate" says only who gave what. |
| m3 labels through walls | Already: Label3D is depth-tested (walls hide it). |
| m1, m4 | m1 stale (hands built mid-run); m4 gone with S1. |

## Critic round 2 synthesis (built code checked, 2026-11-12 ~12:58)
Clean: no cure named on partial evidence; no `trick`, scar or far-cure leak; lessons gated; no soft-lock with 1 human +
bots; all 9 doorway signs and cure rooms right; the floor plan shows only fixed facts and you.
| Finding | Decision |
|---|---|
| S1 the floor plan was a mirror image (+x drawn right with the garden up) | Fixed: +x drawn left, arrow `(-f.x, -f.z)`. |
| M1 the danger edge was a creature radar through walls | Fixed: only a creature in line of sight (or within 3 m). |
| M2 ~45 words at a turn; facts shown twice | Fixed: banner subs ≤ 4 words; tool reads and deaths in the feed only (no toast); feed and readout hide while a banner shows. |
| M3 lessons 2–3 untaught; the 5 steps repeat forever | Fixed: lesson 2–3 show one "New tonight" line per added rule, 9 s apart, then nothing. |
| M4 the patient doesn't know which key matches what they feel | Fixed: "You feel: moonlight stings (say it: 2)" (the key in practice only). |
| m1 cure feed through walls | Fixed: within 4 m or in line of sight. |
| m2–m7, m9, m10 | Fixed: "You gave"; "nothing seen"; no hunt line while fed; Tab step only after looking; tree house by radius only; Tab 1100 px; practice nights 6 / 8 / 12 min. |
| m8 `no_trick` vs `no_tricks`, dead `_tip` | Kept (cosmetic). |

## Critic round 3 (verification, ~13:05): no severe left
All round-2 fixes checked correct (map is a true rotation; banner subs ≤ 4 words; no leaks, runtime errors or
soft-locks). Fixed: M1 props stretched to fill their collision boxes (items sit on the desk/table top, no invisible
table ends); m1 coming within 4 m ticks the coach's "look" step; m2 lesson lines ≤ 7 words; m3 readout drops "too
dark" when a sign shows; m4 no hunt line under a banner; m5 "You gave yourself"; m6 east bookshelf turned to face the
room (glTF faces +Z); m7 statues fit inside their box; m8 freed a model on a failed load.
