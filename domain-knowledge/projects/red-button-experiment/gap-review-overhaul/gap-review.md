# Gap review: the overhaul (2026-11-06, user away)

User, 2026-11-06: "could you review then the gaps on this game? make a huge overhaul on this
game.. try to find 1000 gaps and fix all of them in a iterative manner.. many and many iterations
until there is 0 gaps from all designs. ill be afk."

**What a gap is here:** a place where the built game breaks a rule in the design docs, a checklist
item in a pattern doc fails for a piece of content, the game errors or misbehaves when run, or a
player hits a dead end (no answer, no way forward). A gap is **not** a decision the user still has
open (those stay in `docs/questions.md`); where fixing one needs a design choice, the fix is
Claude's pick, listed under "Claude's choices" to confirm.

**Status tags:** `fixed` (changed and checked), `no change` (looked, not a gap), `parked` (needs
the user or a playtest; noted in `docs/questions.md`).

**Checked vs assumed:** each round says what was run and what was only read.

## Rounds
(one section per round: the lens, what was found, what was fixed, what was checked)

### Round 1: run it, then rule by rule (sim, moods, chores, exams, paths, shipping)
Lens: a headless host + 3 bots (checked: ran it), then every content script read against
`docs/gameplay-design.md` and the pattern checklists (read only).

| # | Gap | Where | Status |
|---|---|---|---|
| 1 | Props packet over the MTU with 4 players (1,398 B; build notes said fixed) | `room.gd` rpc_things | fixed: chunks under 1,100 B, applied when a frame is whole |
| 2 | A mood ending is silent (rule changes must be heard both ways) | `game_sim.gd` | fixed: `mood_off` falling chime |
| 3 | Contrary's clue (a metal clank) never built: plain dud | `game_sim.gd` `_dud` | fixed: `clank` |
| 4 | Chore start sounds flat, room-wide (only room-wide moments are flat) | `start_chore` | fixed: `GameEvent.origin()` per chore |
| 5 | A solo crew can draw the Hot Box (20 kg, one lifts 12 kg: always failed) | `_pick_chore` | fixed: 2+ only |
| 6 | Exam stakes said only by Blink ("rule and stakes said and shown") | exams | fixed: shared, once per run |
| 7 | Sequence stalls 40 s and fails on nobody when a subject in the order leaves | `sequence_exam.gd` | fixed: absent turns skipped |
| 8 | Points from no hit (sold friend, cursed button, refund) cross the goal and nothing happens until the next hit | sim | fixed: `gain()` lands the milestone |
| 9 | A VIP low-gravity prank outlives its 6 s if any mood starts meanwhile (two rules at once) | `vip_loop.gd` | fixed |
| 10 | Hot Potato fines 15% of the wallet, 3x a failed exam (biggest loss in the game from a party chore) | `tuning.gd` | fixed: 5% (Claude's pick) |
| 11 | No subtitles at all with `SCREEN_TEXT` off: orders and exam rules voice-only (deaf players, muted narrator, loud Discord) | HUD, Options | fixed: Options → Subtitles, off by default (keeps the user's no-text call) |
| 12 | Shipped builds are from 2026-11-03 (pre design v2); nothing rebuilds them with Piper beside the exe | `tools/` | fixed: `tools/export.sh` (not run: no 4.7.2 export templates installed) |
| 13 | Credits lack Godot's MIT notice and GodotSteam's licence (required in a shipped build) | `docs/credits.md` | fixed |
| 14 | Bots never use an item that scores by impact (agreed in `docs/todo.md`) | `room_bot.gd` | fixed (part): bots throw balls at the button; bat, cannon, trampoline still not |
| 15 | AI-opened game windows play sound (user, mid-round) | `tools/ai_run.sh` | fixed: dummy audio driver |
| - | Ceiling vs target rate: at 4 players a stage's ceiling (300 s x 0.4 = 120 s) about equals the designed 4,500 units at 40/s (112 s): no slack; at 8, 67 s | `tuning.gd` | parked: tune by playtest (numbers are open in `docs/questions.md`) |
| - | Order fines stack per subject: "together" failed by 4 takes ~12% of the wallet at once | `tuning.gd` | fixed in round 8 (#33) |

Checked: 115 tests pass (8 new); two headless host + 3 bot runs (stage 1 and stage 3), no script
errors, no MTU warning after the fix. Not checked: how the new sounds sound; the export script.

### Round 2: what each player sees and hears (client, multiplayer, docs against docs)
Lens: `room.gd`, the HUD, the views and the item physics read for "does the player get an
answer?", plus the design docs read against each other.

| # | Gap | Where | Status |
|---|---|---|---|
| 16 | The Hot Potato holder can't tell it's them (others see it over their head; the first-person view shows nothing) | HUD | fixed: a glowing potato at the bottom of the holder's view, pulsing faster as time runs out |
| 17 | After a run, a guest's press gets no answer (only the host restarts) | `press` | fixed: a thud |
| 18 | E on a thing with something in hand is silent unless it's an empty cannon (a loaded cannon, any other thing); a big thing in hand could be "loaded" | `_item_interact` | fixed: a thud; big things never load |
| 19 | Orders "shown with an ORDER badge" (dialog design) but the panel sat in the hidden layer | HUD | fixed: shown with Subtitles on |
| 20 | A repeated hello re-adds a player and uses up a colour | `add_player` | fixed |
| 21 | core-design said the ceiling doesn't fall (the user turned it back on) | `docs/core-design.md` | fixed |
| 22 | gameplay-design said "one press every 0.22 s" (now 60/s) and still sold cigarettes and insurance | `docs/gameplay-design.md` | fixed |
| 23 | ui-ux said the pedestal shows "nothing else" (it shows the goal since the discovery review) and "machine presses" | `docs/ui-ux-design.md` | fixed |
| 24 | questions.md quoted the old sensitivity width (10,000) | `docs/questions.md` | fixed |
| - | Items falling out of the world | `things.gd` | no change: already sent back out of the hatch |
| - | Player cap, host leaving, connection failed | `net.gd` | no change: capped at 8, both send you to the menu |
| - | Lag test (roadmap week 2: `tc netem`) | - | parked: needs root; the user's Week 2 step |

Checked: 118 tests pass (3 new); a headless host + 2 bots with the potato forced, no script
errors. Not checked: how the potato overlay looks.

### Round 3: the checklist matrix (discovery, escape room, visual communication) per element
Lens: each of the 15 items, 7 moods, 6 chores, 5 exam gates and 9 paths against the discovery
checklist (verb, hook, answer, chain, record), the escape-room checklist (hands, feedback, honest,
talk) and visual-communication 9 (the blamed carries a trace). Read only, from the scripts above.

| # | Gap | Where | Status |
|---|---|---|---|
| 25 | Crowbar on the weak panel before 4 cracks: nothing, no sound (a try with no answer) | `breakout_route.gd` | fixed: the hollow thud |
| 26 | Floor Fire blames whoever spread it, but carrying an ember left no trace on them | fire, puppet | fixed: a crackle from their feet when they catch it, glowing feet while they carry it |
| 27 | A demo built today would ship the testing flags (shop free and open, Steam test app 480) | release | parked: release checklist in `docs/questions.md` |
| - | Every other element: verb visible, tries answered, culprit traced (valve turner at the wheel, leak holder at the crack, hot box soot, potato, seat glare), found endings on the plinths | - | no change |
| - | Hidden verbs (crouch on fire, E-E dynamite, cart tap) | - | parked already (playtest) |

### Round 4: soak (robustness by running, not reading)
Lens: a new soak test (`test/unit/test_soak.gd`) drives the sim with four random subjects for
240 s from the start and from stage 5, 60 s under every forced mood/chore/exam, 60 s in every
path's debug state, and 90 s at the 1B Greedy gate; someone leaves and rejoins at random.
Invariants: count never negative, valid mode and stage, unique thing ids, an exam only in a
blackout, at most two chores, a snapshot that splits, packs and merges back.

| # | Gap | Status |
|---|---|---|
| - | 33 soak runs (22k asserts): no crash, no broken invariant | no change |

Checked: 123 tests pass (5 soak). Not checked: balance (the random subjects are not players).

### Round 5: the unread code, then a networked run with items
Lens: `player_body.gd` input and the narrator against `docs/dialog-anti-patterns.md` (read),
then a host + 3 bots from stage 3 with balls in play (ran it).

| # | Gap | Where | Status |
|---|---|---|---|
| 28 | Strike armed while the crew was throwing at the button (a throw, swing, shot, gust or bounce wasn't a "try"), then broke the same second: "I notice nobody is pressing" + "Host caved" | `game_sim.gd` | fixed: `tried()` on every item attempt (checklist 6: not by accident) |
| 29 | Contrary's memory of recent hits survives a restart (could refuse an item for last run's hits) | `restart` | fixed |
| - | Narrator lines naming the memory mechanic (dialog anti-pattern 1) | lines | no change: none |
| - | Thin line pools | lines | no change: only exam briefings (2 each, heard about once a run) |
| - | Bots with balls still lose stage 3: a thrown ball scores +1 or +2 by design (user, 2026-11-03); the bat is the multiplier | balance | parked: playtest |

Checked: 124 tests pass (1 new); the bot run, no script errors.

### Round 6: the render side, and the narrator over a long run
Lens: a windowed run (muted, `tools/ai_run.sh`) with bots and Floor Fire, for render-side errors
headless can't show; then a long host + 3 bot run with the ceiling held, every line tallied
(`docs/todo.md`: "check in a long run whether that is enough").

| # | Gap | Where | Status |
|---|---|---|---|
| 30 | Selling a friend, buying them back and the potato's end are one fixed line each, said word for word every time (dialog anti-pattern 3) | lines | fixed: pools of 3-4 (shuffle bag) |
| 31 | The same order kind can come twice in a row ("Everyone stand next to X" 3x in 4 minutes) | `narrator_order.gd` | fixed: never the last kind again (like moods and chores) |
| - | Render-side errors in a real window (materials, the potato and ember drawing) | - | no change: none |
| - | Pooled lines over a long run | - | no change: none repeated |

Checked: 125 tests pass (1 new); windowed run, no errors; long run tallied.

### Round 7: the whole run, end to end, three times
Lens: a soak where points flow in fast and every exam passes as it goes, so all eight stages,
every gate, the Greedy press and the escape happen, then the host restarts (ran it).

| # | Gap | Status |
|---|---|---|
| - | Stage chain 1 to 8, the Greedy gate, the escape ending, restart to an empty lobby, three times | no change: works |

### Round 8: save data and the size of a single loss
| # | Gap | Where | Status |
|---|---|---|---|
| 32 | A hand-edited, cut-off or older `archive.cfg` with a wrong type raised a script error on every load | `archive.gd` | fixed: each field type-checked, the rest still loads |
| 33 | One failed order fined every subject 3%: 12% of the wallet at 4 players, 24% at 8 (a single loss scaled by crew size) | `tuning.gd`, `_resolve_order` | fixed: an order's fines capped at 6% together, split (Claude's pick) |
| - | Only the host's save gains unlocks; a guest keeps none from runs they didn't host | `archive.gd` | parked: already open ("whose save holds unlocks", `docs/questions.md`) |

Checked: 128 tests pass (3 new across rounds 7-8).

### Round 9: the fixes against the rules
Lens: each change above checked against the rule it touches, and written into the design docs
(they hold current rules only). Rules updated in `docs/gameplay-design.md` (Strike tries, fine
sizes, Hot Box 2+, Sequence leavers, exam stakes) and `docs/ui-ux-design.md` (Subtitles option,
chore sounds from their walls, three new visual-dictionary entries: orange glow on a body, the
falling chime, the clank; none clashes: orange already reads "hot" from Floor Fire).

## Claude's choices to confirm (not user decisions)
- Hot Potato fine 15% → 5% of the wallet; one order's fines capped at 6% together.
- Subtitles (narrator lines and orders) as an option, **off by default**, keeping "no text on screen".
- Exam stakes said on the run's first exam only.
- The Hot Box is never drawn for a solo crew.
- The potato holder's cue is a glow at the bottom of their view (no text).

## Where it stands
After nine rounds the reading and running lenses come back clean: 33 gaps fixed, the rest parked
because they need a person (balance, feel, hidden verbs, the user's open design questions) or the
user's hand (release flags, export templates, the lag test). "Zero gaps" is not something a review
can reach for a game whose fun is judged by a playtest: the next gaps come from watching people
play (`docs/roadmap.md`, Week 1).
