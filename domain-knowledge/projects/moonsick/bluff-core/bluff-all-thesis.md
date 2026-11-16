# Thesis: the rest of the bluff todo, parts 3–6 (2026-11-15, Claude)

User: "implement all steps and then ill review" (after parts 1 and 2 were built, `REPORT_bluff-base.md`).
Todo: `docs/TODO_bluff.md`. Part 7 is the user's playtest. Everything here is (Claude) unless tagged (user).

## The problem underneath
The bluff (the coffee lie, deals) needs three things the game lacks: a reason to keep items in hand (to promise and
trade them), a way for the sick friend to learn how bad they are only through others (so others can lie), and a test
crew where bots both lie and can be dealt with by the human (1 human + 3 bots, critic log "voice-only game ×6").
Every new rule a player must know counts against the budget of ≤ 3 taught rules (critic log ×6), so each piece below
must be physical and discoverable, not taught.

## Built facts this leans on (read in the code, 2026-11-15)
- Items are carried, two hands (`hands.gd`, user); steal and tug are built (user: "a player is able to steal...").
- Bots read only public state and what's near (`bot.gd _observe`); bubbles and all world text are off (`world_text`, user).
- Veins are in the public state for everyone, the patient too; the client just doesn't show your own (neck).
- A give shows the giver's reaching arm to everyone (`reach`, `_reaching`).
- `moon_speed` (moonlight ×1.5 on a case) is a step-1 cut, off.
- `near_head_start` (5 s for friends within 8 m at the turn) is a step-1 cut, off; questions.md Q-B3 Claude: on.

## Part 3: cures as places vs carried
Answers:
- **A. Places:** you bring the patient to the coffee machine. Drops steal, tug, trading, hoarding; the lie becomes
  "meet me in the kitchen".
- **B. Carried, as built (recommended).**
- **C. Carried, one hand:** each friend carries one item.

Scene, 1 human + 3 bots, A: the human yawns; a bot says nothing it can say (no voice), walks off; the human must walk
to the kitchen alone; a trade can't exist because nobody holds anything. The deal bubble "[bucket] for [coffee]"
(user) has nothing to point at. **A fails** two user-chosen features (steal/tug, the deal bubble).
Scene, 8 friends, B: 16 hands for 16 items; one friend holding two coffees blocks two yawns. That's hoarding as a
trade chip, which round 15 allowed (user's call: "a held item can be kept as a trade"). Steal/tug is the answer to it.
Scene, C: one hand halves hoarding but breaks the user's two-hand design (LMB left, RMB right, user) and the
"hold a friend with one hand, give with the other" rule.
**Pick B: nothing to build.** One hand: no (C fails the user's hands design). Empty spots at 8 friends stay a playtest check.

## Part 4: knowing your own state
- **Feel symptoms, not progress:** already true (FELT symptoms on your screen; veins on your neck; no progress UI with
  `screen_ui` off). Nothing to build.
- **Mirrors** show your own veins. Answers:
  - **A. A reflection (recommended):** a mirror on a wall; standing within 3 m in front of it, you see a copy of your own
    body behind the glass, drawn from the host's public state (veins and symptoms included). Two mirrors: the hall
    (beside the east window beam) and the study. Each stands in a moonbeam, so it's lit enough to read.
  - **B. A mirror card:** looking at it shows a 0–3 vein meter. Fails "no screen UI" (user).
  - **C. No mirrors, ask friends only.** Then the human alone with bots can't check a bot's answer at all.
  - Cost of looking: Claude earlier said moonbeams cost ×1.5 curse. That needs `moon_speed`, a user cut. Claude: keep
    it off; the cost of a mirror is the walk and the time away from the group (the hall mirror is ~15 m from the kitchen).
- **Others see your veins roughly:** built.

## Part 5: turning early
Rule (Claude, from the chat): the sick friend can choose to turn early, only late in a case, never delay it.
- **When "late" starts:** the curse at 0.6 or more (veins on the face; `CurseRules.veins`).
- **The verb:** hold **T** for 2 s while sick. Others see you strain (the body shakes, a growl everyone near hears).
- **Too early:** answers:
  - **A. Nothing but the strain, then 20 s before you can try again (recommended).** Everyone near saw you try: that's
    the cost (you were caught wanting to turn). You learn only "not yet past 0.6".
  - **B. Too early pushes the curse +0.15.** A punishment for a choice the patient can't measure; anti-pattern 20 (blame from luck).
  - **C. Too early turns you anyway at half hunger.** Lets anyone turn at will; breaks "only late".
- **Why turn early (the trap):** you pick the moment and the victim (next to one lone friend, away from wolfsbane),
  and the near head start doesn't help a friend who wasn't warned. It never beats curing: a turned friend loses trust.
- **Head start back on (Q-B3):** `near_head_start` on: friends within 8 m of a turn can't be struck for 5 s. A friend
  who turns early next to someone gives that someone 5 s, so turning early next to your victim doesn't pay at once;
  you must turn near nobody and then hunt (the wolf's speed is 1.3× a walk).

Scene, 4 friends: Dee's veins reach her face; Ana is fetching her razor. Dee holds T next to Bo alone in the cellar.
Bo sees her shake and hears the growl in the 2 s: he runs. Dee turns; Bo has 5 s; Dee knocks him down at 6 s if she
catches up. Best play for Dee: turn far from everyone, then hunt. Best play for friends: watch who strains. The choice
is live because the strain is seen.
Scene, 1 human + 3 bots: bots never turn early (Claude: the test crew's bots stay honest about turning; their bluff is
the deal and fear).

## Part 6: bots and talking
- **Fear (user OK):** a bot doctor bails when its patient's veins pass its nerve (each bot 0.55–0.85, random per bot):
  it walks off to the nearest other friend, even mid-promise. A bot never bails from a friend it has seen give 3+ times? No:
  round 16, "fear beats trust".
- **Trust (user OK):** each bot counts the gives it saw itself (any friend giving any friend, within 12 m and line of
  sight not checked: Claude, 12 m only). It treats the most trusted patient first, and keeps its deals only with a
  friend it trusts at 1+ (0 at start: a stranger's first deal gets an honest try). It never tells.
- **Deal bubbles (user):** a sick bot holding an item a friend near it (≤ 5 m) needs shows "[that item] for [the item
  it needs]" over its head, icons and the word "for", no arrows. If the friend gives it what it needs, it gives its item
  within 3 s (if it trusts them, or if trust is 0; a bot whose trust in you went below 0 because you took its item and
  never paid keeps it). Only this bubble shows, despite `world_text` off (user asked for it).
  Bots stop dropping their items when sick if a friend near needs one.
- **The human's offer (Q-B4):** holding an item out toward a bot = the existing give reach. A bot that sees a human
  reach toward it with the item it needs stands still for it (as patients do) and, after the give, trusts the human +2
  and fetches the human's needed item first. No new verb.
- **"How bad are my veins?" (Claude):** key **9** asks the friend you aim at (within 6 m). A bot answers with a bubble of
  0–3 red vein marks. Honest bots round the truth; a bot lies (shows 0) when it's afraid of you (your veins past its
  nerve) — fear, never a reward. Humans answer by voice.
  The ask is a quick-chat line the asker's body says, so it works without world text: the asked bot answers with icons only.

Scene, 1 human + 3 bots: the human yawns (mild). Bot Bo has stink (mild) and holds a coffee. Bo shows
"[coffee] for [perfume]". The human fetches perfume (27 s far trip, 45 s grace) and gives it; Bo gives the coffee.
Next night-minute, Bo's own case gets late; Bo promised nothing, but bot Cy, doctoring Bo, bails at veins 0.6.
The human sees Cy walk off and must finish Bo alone. The human asks Cy (key 9) "how bad am I?": Cy, afraid of the human
(late), shows 0 marks. The hall mirror says otherwise.
Scene, 8 friends: humans make deals by voice; the bubbles only come from bots. Mirrors are a 15 m walk; the turn-early
strain is the new tell.

## Pillars
- Keeps: betraying never pays more than curing; helping beats fleeing (the head start comes back); no screen UI
  (mirrors and bubbles are in the world).
- Bends: "no text in the world" (the word "for" in bot bubbles; the user asked for it).
- Bends: "lies come from fear" — a bot's veins lie is fear (kept); the deal is a trade, a reward-shaped thing the user
  already allowed (saving a trip).

## New things a player must know
Before: hands, give, hold, steal/tug, symptoms ↔ items, nobody treats themselves, the wolf's strike.
Added: T to turn early (only the sick need it), 9 to ask (optional), mirrors (found, not taught), bubbles (bots show them).
Taught: none of these; T and 9 go in the controls table.

## Merge (filled after the critic)
Critic: `docs/critic-bluff-all-r1.md`.

| Finding | Decision |
|---|---|
| Problem underneath: the lies live in mild symptoms, which have no veins, so mirrors, asking and turning early only matter in full cases | Accepted: cut asking (key 9) and turning early; mirrors stay (the user offered them) as the one way to see your own veins |
| S1 Turning early pays more than curing: an unwarned friend next to you is struck at 5.0 s, eaten at 6.5 s (the wolf sprints at 11.2 m/s), while the case is still curable 17–41 s | **Cut part 5, not built.** It breaks the user's pillar "betraying never pays more than curing". Taken to the user: questions.md Q-B6 |
| S2 The head start doesn't make helping beat fleeing: it's measured at the hunt start, after 4 s | **Not turned on.** Q-B3 stays the user's, now with the critic's numbers |
| S3 The test crew still has no human lie: the human always gives first | Fixed: a bot that trusts you (1+) gives first in a deal; you can then not pay, and its trust in you drops below 0, so it never deals with you again |
| M1 The bot's "0 marks" lie has no motive and the mirror refutes it | Cut key 9 |
| M2 A deal for a far item fits the 45 s only sometimes | Bots offer a deal only when the item they need is within 15 m of the friend (Claude) |
| M3 A reach freezes a bot, a bait verb with the wolf out | Bots stand still for a reach only while no creature is out |
| M4 Trust sees through walls | Bots count only gives they can see (a ray to the giver) |
| M5 T undefined for healthy friends | Moot: T cut |
| M6 Q-B3 / Q-B4 answered for the user | Q-B3 left open; Q-B4 built with no new verb (the existing give reach), recorded as Claude's pick in questions.md |

Left to build: part 3 nothing; part 4 mirrors; part 6 fear, trust, deal bubbles (bots give first when they trust you), bots reading a reach.

Critic round 2 (`critic-bluff-all-r2.md`) → built: a bot whose trust in you is below 0 never treats you; the needed
item may lie up to 25 m away; healthy bots leave the symptom a dealing bot offers to the deal.
Critic round 3 (`critic-bluff-all-r3.md`, on the built code) → fixed: an unpaid deal is broken however it ends (a
doctor curing the bot first no longer wipes the debt); the last fallback in a bot's treat skips a deal's symptom; a bot
paid first hands its item over even once it's cured; a broken deal is for good; a bot owed an item waits by its
doctors instead of trailing the friend. Three rounds done; round 3's severe findings were bugs, fixed, not re-checked.
