# Fix 1 thesis r1: the core moment, "a friend starts turning" (Claude, 2026-11-12 night)

User: "lets start fixing one thing at a time". Order agreed in chat: 1 the core moment, 2 knowing you're turning,
3 seeing a friend turn, 4 knowing what you can do, 5 knowing what happened, 6 the start; art after.
Why first: both critics (`docs/critic-core-r1.md`, `docs/critic-examine-r1.md`) found the same foundation problems,
in v0.1 too: (a) the main choice has one best answer, (b) nobody has a reason to lie, (c) the sick friend just stands
there. Research (`docs/diagnosis-research.md`): games where friends turn in real time (No More Room in Hell 2, The
Thing, Zombie Panic) don't make *what it is* a logic puzzle; the drama is tell or hide, whom to trust or test, cure in
time, stop them before they turn. Current rules: `docs/design.md` + "Step 1 cuts" (tools, pans, tricks, scars, pond,
powers, doubles, head starts, curer protection, moonlight speed-up are off; `scripts/core/features.gd`).

## What the core moment must do (the bar)
1. Told in ≤ 3 short sentences; a new player gets it in the first case.
2. A real choice: each option wins in some visible situation (checked by a sim, not claimed).
3. Trust matters: someone can lie and it can pay sometimes, but curing still pays more on average (user: "betraying
   must never pay off more than curing"; "trust must matter until dawn"; "bluff from both sides").
4. The sick friend acts, not stands (critic memory: "a partner who only stands in place").
5. Works in the user's test (1 human + 5 bots) and with 4–8 friends.

## Three different answers

### A. The sick friend knows what they're becoming; the others decide whether to believe them (recommended)
- From the first second of a case, the sick player's own view shows *which* monster they're becoming (their own
  first-person hands change: fur and claws = werewolf, grey stone = troll, long pale nails = vampire; plus a
  heartbeat). Nobody else sees that.
- They can say it (quick chat: "I'm turning: werewolf / vampire / troll", "I'm fine") — truthfully, falsely, or not
  at all.
- Others see the body only later: stage 2 one seen sign (rules out one monster), stage 3 a second (names it). So
  waiting confirms the claim, at a price.
- **Cures are scarce:** one spot per kind, holding one cure, regrowing 90 s after use. Right cure: works with the
  odds 30% + 65% × (1 − p)^1.5 (95% at once, ~65% at stage 2, ~40% at stage 3). **Wrong cure: they turn at once.**
- **Why lie:** a turned friend must catch someone within its hunger time or starve; a catch makes them human again
  (a catch = a cure, user's rule). So lying to get a wrong cure is a gamble: eat a rival now, or starve. Curing
  stays safer for the liar (no starving risk). Also: friends lie for fun; the house's bots lie sometimes
  (`--liar-bots` exists).
- **The choice for the others:** believe the claim at stage 1 (strong cure, but if it's a lie the friend turns at
  once beside you) or wait for the body to confirm (weaker cure, the friend may turn anyway). Who said it, and what
  they've done tonight, decides it: trust.
- **The choice for the sick friend:** tell the truth, lie, or hide (hiding keeps friends from locking you... no
  locking exists; hiding just means no cure).
- Told: "Friends will start turning into monsters; only they know which. Give the right cure: a wrong cure turns
  them at once. Survive till dawn."

### B. A scarce test knows (The Thing)
- Body signs give a lean (one sign = 2 monsters). A silver mirror shows the kind at once, but the house has 3 uses
  per night, shared. Choice: spend a mirror or guess; who holds the mirror can lie about what it showed.
- Against: the sick friend still only stands; the liar is the mirror holder, not the patient (bluff from one side).

### C. The kind is easy; the hard part is getting the cure there
- Signs are obvious at once; the challenge is cures far apart, holding the patient, a creature out, two sick at once.
- Against: critic memory "one task at a time = a calm conveyor"; no lying; the choice is routing only.

## Scenes for A
- **1 human + 5 bots, practice:** 1:00 bot Bo says "I'm turning: vampire!". Garlic is in the kitchen, 20 m. You
  fetch it (25 s). Bo's body shows nothing yet (stage 1 lasts 50 s). Bots never lie in practice night 1 (assumed
  setting), so you give it: cured. Later nights `--liar-bots`: Cy says "troll", you give rowan at once, Cy turns into
  a werewolf beside you and chases Dee.
- **You are sick:** 3:00 your hands go grey and stony: troll. You say "I'm turning: troll". A bot brings rowan.
- **6 humans:** Ana says "werewolf". Bo, who Ana panned... (no pans) — Bo, who Ana let get caught earlier, says
  "she's lying, wait for the body". Wolfsbane is the only one in the house. Ana's case is at stage 2: grey skin
  appears (vampire or troll): she lied. Now garlic or rowan, at 65%.

## Pillars
- Bent: the diagnosis moves from "combine split signs with a % per sign" to "believe the sick friend or wait for the
  body" (the user's own choice line in design.md: "Believe what a friend says they feel, or what their body shows").
  The % per sign stays only in which body sign shows first.
- Kept: one night, dark, cure works only if right then with %, holding, catch or starve, catch = cure, betraying never
  pays more than curing (the starving risk), bluff (the patient now lies; the curer can still give a wrong cure on
  purpose), the hunter chooses freely, no ghosts.
- Still off from step 1: tools, pans, tricks, scars, powers, doubles.
