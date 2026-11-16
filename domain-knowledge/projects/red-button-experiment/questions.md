# Open questions

- **Design v2, open parts** (2026-11-05; built with Claude's choices while the user was away,
  listed in `docs/build-v2.md` → Claude's choices to confirm; don't ask, pick up when ready):
  - *The eye:* show it (`Tuning.EYE_VISIBLE`) so the batted-ball branch of Unwatched works? Rec:
    yes once the room is art-passed; the user hid it on 2026-11-03 "for now".
  - *Fire:* crouch to stamp (built) or E held (the design's wording)? Rec: crouch, judged by the
    playtest.
  - *Numbers:* sensitivity width (5,000 since 2026-11-06), ceiling seconds per stage, mood and chore gaps, VIP
    sale and buy-back prices. Rec: tune from the first 4-player playtest; bots can't judge them.
  - *Briefing:* with the sight split, the briefing could give only the stakes and leave the rule
    to be found. Rec: keep the full briefing (user, 2026-11-04) until the playtest says otherwise.
  - *Greedy at 1B:* the one gate with no sight split (the user's special, kept as decided).

- **Orders and the press rule** (2026-11-04; rule in `docs/gameplay-design.md` → Two modes: a
  press only fails in a blackout). Orders "hands off" and "only X presses" still punish a press in
  pressing mode. The rule was said about events; rec orders keep it (making the obvious move wrong
  is their job), unconfirmed.

- **Shop: picture grid or walk-in shelf?** (2026-11-03; user asked for "a grid of screenshots of
  the items" on a white background, then how other games do it.) Researched: Lethal Company is a
  text terminal plus a drop pod; Content Warning a kiosk between rounds; R.E.P.O. a walk-in shop
  where you grab an item to see its price, paid from shared cash. A picture grid is still a menu
  (`docs/ui-ux-anti-patterns.md` §3). Rec: the picture grid now (cheap, demo month), a shelf of
  real items behind the hatch as a post-demo option.

- **The door (??? item), open parts** (2026-11-03; design in `docs/gameplay-design.md`):
  - *Gate:* does setting the door in replace the 100/300 milestones as the stage change? Rec: yes.
  - *Price:* rec 500, so buying it empties the wallet.
  - *Free-shop flag:* rec the ??? stays locked until 500 even with `SHOP_ALL_FREE`.
  - *Does the crew split* between rooms in crew worlds? Rec: yes, free to come and go.
  - *Solo room reward:* rec a moment reward (points or ceiling time), never a rate.
  - *Rescue:* can the crew break a solo door open? Rec: no at first.
  - *Mix:* rec mostly crew worlds, an occasional solo trap.
  - *First world to build:* not chosen.

- **Private realities, open parts** (2026-11-03; design in `docs/gameplay-design.md`; user is still
  designing, don't ask): trigger (rare random vs hidden), Freedom's body (mirrors vs freezes), the
  souvenir, how the ghost disturbs, how rare. Not researched yet: other games' per-player
  hallucinations (research before writing a pattern list).

- **Loops, open parts** (2026-11-03; design in `docs/gameplay-design.md` → Loops; don't ask):
  what selling a friend pays and what buying back costs; whether the VIP can also leave alone;
  the door's "control room" world now overlaps the VIP room (TV of the crew + buttons to mess with
  them), so rec: drop the control room world.

- **Path items, open parts** (2026-11-03; design in `docs/gameplay-design.md` → Path items; user is
  still designing, don't ask):
  - *Unlocks:* how each item reaches the shop. Ideas, not researched: a count gate, a way of losing,
    found inside a loop, a behaviour (nobody presses for 30 s), coming back after a few runs.
    Rec: research co-op meta-unlocks (Risk of Rain, Lethal Company, R.E.P.O.) before writing rules.
  - *Whose save holds unlocks* in co-op: the host's or each player's.
  - *Flashlight:* what the walls show, and whether it only works in a blackout. Rec: the alien's
    clues are written there too, so the two items need each other (not agreed).
  - *Egg warmth:* rec players huddling (hands off the button, pillar 2); alternatives: held, or
    near a heat source.
  - *Egg breaking:* who can break it and how (a slap, a drop, the monkey car), and whether a broken
    egg is lost for the run or for good.
  - *Alien clues:* how it shares them with no text on screen (drawings, gestures, sounds).
  - *Moon route:* the ending, and how the button follows the crew there (pillar 1). Idea: the
    button launches the rocket.
  - *Egg across runs:* does it hatch within one run, or grow over several (pillar 4)?
  - *Other ideas, not liked yet:* Old Phone (call out), Crowbar (pry the hatch), Radio (other
    crews; high tech risk).

- **Look of players and room.** Recommendation: simple test subjects (capsule/blob figures in jumpsuits),
  clean white testing room; decide during the prototype.
- **Exact numbers:** ceiling speeds, minigame time effects, speed cap, milestone costs, per-group-size tuning.
- **Price.** Rec (2026-11-03): $7.99 with a 30–40% launch discount (~$5 launch week). Evidence: the
  playbook's $5–10 band, games over $10 convert wishlists worse; PEAK $8 → $5 at launch, R.E.P.O. €9.75.
- **Trademark search** for "Red Button Experiment" (only Steam exact-title check done, 2026-11-03).
- **GitHub repo** (private, like Hordeline): not created yet.
- **Stage pacing vs ×10 milestones** (found while building the MVP, 2026-11-03). Each player can press
  ~4×/s, so 3 players reach 10 and 100 in seconds; with fixed ×10 goals, early stages can't last
  4–5 min. Recommendation: keep the ×10 goals (they read well) and pace with the ceiling (now scaled
  by crew size) plus events; treat stages 1–2 as a fast warm-up. Alternative: start goals at 1,000.
- **Bot-tested balance only.** First numbers in `scripts/core/tuning.gd` / `economy.gd`; tune by playtest.
- **What if nobody discovers an item's use?** (2026-11-03, from the "shop doesn't say how to use it"
  rule.) A bat no one swings is a dead purchase. Recommendation: each item shows its use when
  handled (the hammer squeaks on any hit, the bat swings on E, the cannon's mouth opens when a held
  item comes close); judge in the playtest whether that's enough before adding any hint.
- **In-game proximity voice?** (2026-11-06, from `docs/visual-communication-patterns.md` C.) In
  Lethal Company it's the comedy engine (screams fade, the dead go silent); we have no voice, crews
  use Discord. Recommendation: not for the demo (new transport work, a month to ship); make bodies
  carry intent instead (readable held items, visible wind-ups) and revisit for Early Access.
- **Rename the fantasy "Discovery"?** (2026-11-06, from `docs/discovery-patterns.md`.) In UX,
  "discoverability" (Norman) means the player can easily see what they can do, the opposite of
  hiding. Our fantasy is finding out what things *do*. Recommendation: call the fantasy
  **Discovery** ("find out by trying") and keep "discoverability" for the rule that the goal and
  the verbs are always obvious.
- **An ask-for-help verb?** (2026-11-06, from `docs/escape-room-patterns.md` pattern 5.) Hints
  are two fixed flashlight writings per run; escape-room players most want to *ask* for hints,
  without penalty, and fixed/timed hints can't tell a stuck crew from a busy one. Idea: begging the
  narrator gets a grudging, mocking hint about *where to look* (it remembers who begged, pillar 4).
  Recommendation: not before the playtest; first measure how many crews crack each mood and route
  unhinted, then add it if any sits under half.
- **Is the 1B Escape ending a climax?** (2026-11-06, from `docs/escape-room-patterns.md` pattern
  9.) The routes end on a spectacle; the main ending is the count reaching a number. Escape rooms
  live on one unmissable final moment, and it is the clip that sells a streamed game.
  Recommendation: give the Escape ending its own staged moment everyone watches, sized after the
  playtest shows which route endings land.

- **Release checklist for the demo build** (2026-11-06, gap review; nothing changed, these are the
  user's current testing settings): before `tools/export.sh` makes the public demo,
  `Tuning.SHOP_ALL_FREE` (true: every item free, so no economy) and `Tuning.SHOP_AT_START` (true)
  are still the testing values; `Net.STEAM_APP_ID` and `steam_appid.txt` are 480 (Valve's
  Spacewar test app) until the Steam Direct app exists; the export needs Godot 4.7.2 export
  templates (only 4.7.1 are installed). Rec: flip the two flags for the demo build only, after
  the playtest says the prices feel right. Also for the demo: `Tuning.DEMO` true with
  `STORE_URL` and `DISCORD_URL` filled (the title menu then thanks, asks for a wishlist and
  links feedback; empty links hide their buttons).
