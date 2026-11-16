# Hands thesis r1: one mouse button per hand, a stretch link to hold a friend (2026-11-12)

## The user's words (verbatim, 2026-11-12)
"lets add hands in the game like phyisical hands / right hand and left hand. / left hand and right hand is controled
with left and right click / but not vvisible in screen / when player is near an object.. press left click or right.. a
hand goes to the object and picks it up and now you have a hand holding the item.. / also for restraining a player..
you can use one hand so it physically goes to the person to restrain. it just creates a link.. where you have to push
back and hold the click to deaccelerate the player.. if you dont move then the other player can scape"

Reading (assumed): "not visible in screen" = no hand on screen while empty and no HUD hand panel; a hand shows only
while it reaches or holds something. "push back" = the holder moves away from the friend (S while facing them).

## Today [read: design.md "Hands", "Holding and knocking out"; player.gd; night_sim.gd]
- Two hand slots plus a hidden **active hand**, switched with R or the wheel. LMB uses the active hand (give, read,
  swing, or pick up when empty), RMB raises the active hand's cure, E picks up, G drops the active hand's item.
- F grabs a friend (both hands, design.md says from behind): their speed is 0, their case runs at half speed, the
  veins stop; they mash Space 12 times to get free (`STRUGGLE_PRESSES`). Holder walks at 0.35.
- First person: held items float at the bottom corners, no hand mesh; the HUD shows a hand panel (icons + labels).

## Frame
Two problems, both "two inputs fight over one thing":
1. **Hands.** Today a verb = (active hand) × (button) × (what's in front): three things to track, one of them hidden.
   User's change: a verb = (that button's hand) × (what's in front). The active hand, R, the wheel, E-pick, the HUD
   hand panel and F all go away. That's fewer rules and less UI, which is step 1's direction (core-thesis).
2. **Holding.** Two players set one number: the **stretch** = the distance from the holder's hand to the friend,
   minus the link's rest length. It takes in the friend's push away (adds stretch) and the holder's pull (slows the
   push). It gives out escape when it reaches the snap length. It's visible to everyone as the arm or link
   itself, so it needs no meter. It replaces mashing; Dead by Daylight dropped mashing for its wiggle escape
   (accessibility, wear) [source: mein-mmo.de 2022, wepc.com 5.5.1].

## Research
- Human: Fall Flat: LMB/RMB = left/right hand, hold to grip, release to let go; camera pitch raises the arms
  [source: rog.asus.com hands-on, ludo.guide]. Critique: "hard to get used to … a slow process" [source: keengamer].
  We take only button = hand, not the physics arms.
- Fall Guys grabbing: grief at the finish line, complaints about cheap disruption; escape by jumping [source:
  gamerevolution.com]. Lesson: a hold must cost the holder something and must end.
- Co-op tethers frustrate when direction disputes stop movement [source: giantbomb co-op tether].
- Dead by Daylight: carry wiggle "a mechanic to stop killers from being greedy and give teammates time to help"
  [source: forums.bhvr.com], i.e. a timed window for a third player, which is our hold's job too.

## Shape (Claude unless tagged)
### Per hand: left click = left hand, right click = right hand (user)
| That hand holds | In front (crosshair) | Click | Hold the button |
|---|---|---|---|
| nothing | an item within 2.6 m | the hand reaches out (0.15 s), takes it, comes back with it (user) | |
| nothing | a friend within 1.8 m | the hand reaches to their shoulder: a link (user) | keeps the link; let go = release (user) |
| a cure | a friend within 2.3 m who holds still or is linked | | give, 2 s (today's rule) |
| a cure | anything else | | raise it (shoves its creature, you walk at half speed: today's rule) |
| a tool | a friend | | read, 1.5 s (today) |
| a pan | a friend | swing (today) | |
- Drop: Q drops the left hand's item, E the right's. (Today E picks up; clicks do that now.)
- Creatures: either button catches (today LMB).
- Hands on screen: none while empty (user); a simple mitten mesh (code shape) while reaching or holding, item in it.
  The HUD hand panel goes.

### The link (holding a friend)
- Needs one empty hand (user: one hand). The other hand keeps its item. Humans only, not creatures (today's rule).
  Any side, not only from behind (Claude: the stretch replaces the surprise).
- Rest length 1.5 m, snap length 3.5 m. Inside 1.5 m nothing happens; both move freely.
- **Pull** p ∈ [0, 1] = the holder's movement input pointing away from the friend (hold S while facing them). While
  pulling, the holder's feet are planted: the input becomes pull, not motion. Moving sideways or toward: half speed.
- **Friend's speed away from the holder** × (1 − 0.85 p). Sideways and toward: free. A linked friend can't sprint
  (walk 4.32 m/s at most).
  - Holder idle (p = 0): 2 m of stretch at 4.32 m/s → snap in **~0.5 s** (user: "if you dont move … scape").
  - Holder pulling fully: 0.65 m/s → snap in **~3 s** of steady pushing. The hold buys time, never holds forever.
  - Two holders (one hand each): pulls add, capped at 1 → the friend can't leave until one lets go.
- Snap: the hand flies back, a loud snap sound (it's noise: hunters sense it), that friend can't be linked again
  for 3 s.
- While linked: case at half speed, veins stop (today's held effect).
- Ends: release, snap, the friend turns (holder thrown off: today), a creature catches either one.
- **Solo cure check (physics, no new rule):** the holder's other hand could give, but a pushing friend goes from
  1.5 m to past the 2.3 m give range in ~1.2 s, under the 2 s give. So one player can cure a resisting friend only
  if the friend stops resisting, which is today's situation anyway.

## Scene: smallest crew (4) and largest (8)
- 4: Ada's veins show. Ben links her from 1.5 m with his empty left hand, holds S. Ada pushes for the door; the link
  stretches. Cleo runs in with garlic, has ~3 s. Ada circles Ben (sideways is free) to put Ben between her and Cleo.
  Dan is across the house. Snap or cure.
- 8: two holders on Ada: she can't leave; the herb choice is now the only question; the others argue it.

## Co-op gate (holding scene: holder, patient, giver)
1 coupled: the give needs the patient in range, which needs the pull: pass. 2 split: roles by position, anyone
steps in: pass. 3 talk: ~3 s window ("hold her!", "which herb?"): pass. 4 blame: the snap shows whose hand let go:
pass. 5 not easy: a pushing patient escapes one holder in ~3 s: assumed pass. 6 not solo-able: physics above: pass
(assumed numbers). 7 two-way: **weak for the holder**: holding S is always right while linked; the holder's real
choice is earlier (keeping one hand empty instead of carrying two items).

## Dominant strategy
Holder: always pull. Patient: always push unless sure the herb is right. So each one-holder hold lasts ~3 s; two
holders = an unbreakable hold.

## Network (host runs the sim; clients own their movement)
- Poses carry the movement input (2D wish vector) too. Host computes p per link and sends the friend
  {holder id, brake 0.85 p} in its private view; the friend's client scales its outward speed. Host checks the
  distance (snap length + `LAG`) and announces snaps. Brake lag ~100–150 ms (assumed fine).
- Reach/pick: the hand animates on the client at once; the host confirms the pick; a refused pick returns empty.
- Others see the link: public state already carries `holding`; body.gd draws an arm from holder to friend.

## Removed / added
- Removed: active hand, R, wheel switch, E-pick, F, Space struggle (12 presses), both-hands grab, HUD hand panel.
- Added: Q/E drop, the link (pull, stretch, snap), the wish vector in poses, the hand mesh.
- Rules a player must know: "each click is a hand" and "hold a friend; pull back or they slip away" (was: active
  hand, R, E, G, F, Space).

## Bots
Practice bots must escape links (walk away from the holder) and, ideally, link a sick bot so the player can give
(today bots mash Space). Assumed: escaping is a small change in bot.gd.

## Smallest build
1. Per-button hands, reach animation + mitten mesh, Q/E drop; cut active hand, R, wheel, E-pick, HUD panel.
2. The link: sim (pull, brake, stretch, snap), pose wish vector, friend's client brake, link drawn; cut F, Space struggle.
3. Bots escape links; GUT tests for link, brake, snap.

## Open (Claude's picks, to the questions file after synthesis)
Q/E drop; any side vs from behind; brake 0.85 (escape ~3 s) vs a full stop; can a linked friend sprint.

---

## Synthesis r1 (after `docs/critic-hands-r1.md`, 2026-11-12)
Checked by Claude in code: step 1 is werewolf only (design.md "Werewolf only", features.gd `vampire`/`troll` false);
a held bot with a case stops, a holding bot releases at once (bot.gd:191-197); questions.md 17 parks the motive to lie.
Other critic evidence (ranges 2.6/2.9 m, lag chain) is the critic's read, not rechecked.

### Split: the hands half goes on; the link half waits on the user
- **Link (SEVERE #1, #2, taken to the user, not parked):** in step 1 nobody wants out of a hold: any herb is the
  right one, being held halves the case, and there is no motive to lie. The stretch only runs on bait. Bots never
  link or pull away. Building the stretch now = a mechanic nobody uses. Claude's frame candidate (not yet
  critic-checked): **the werewolf's catch becomes the link** (its hand links a victim; the victim pulls away; the
  werewolf must pull back; a friend's raised wolfsbane breaks it). Every hunt uses it, and bots already flee hunters.
  Friend-on-friend links use the same rule once a motive to resist comes back (vampire/troll, lying).
- Dropped claims: the solo-cure block (#7: real give range 2.6/2.9 m, a give can start before the link); "two
  holders can't leave" (#4: endless pin; also wrong under the cap-1 math). Gate 7 for the holder: **fail** (not weak).

### Hands half, fixed
| That hand holds | Press | Hold |
|---|---|---|
| nothing | takes the glowing thing: an item, or a friend (link, once the link half is decided) | |
| wolfsbane | | creature within 8 m: raise it (shove); else a friend in reach: give, 2 s; else last alive: eat it |
| a tool / pan | | read / swing (off in step 1) |
- **Raise beats give when a creature is within 8 m** (#3: today a give on a friend being caught counts as still,
  night_sim.gd:649, so the shove never happens and the herb is wasted). The verb locks at the press (#19).
- **One glow = what your click hits** (#8): the crosshair is cut, so the friend or item your empty hand would take
  gets the rim glow items have today; a friend under your aim wins over an item.
- **E stays pick up** (#9, user: "pickup with left click or E"), into the empty hand, left first. **Drop: hold G and
  click that hand's button.**
- **Self-cure kept** (#10): last alive, wolfsbane hand, nobody in reach, hold = eat it.
- **On screen:** no hands while healthy and empty (user). A mitten shows while reaching, while holding, and (Claude,
  core-thesis "knowing you're sick") trembling while you're sick: the patient's own signal. The mitten never takes
  skin, veins or claws (#22). The hand waits at the item until the host answers (#25).
- **Honest rule count (#13):** the gain is losing the hidden active hand, R and the wheel; each button now does
  pick, give, raise, eat (step 1). Same number of verbs, one hidden mode fewer.

## Synthesis r2 (after `docs/critic-hands-r2.md`)
Checked by Claude in code: `_active_cases()` counts creatures and turning friends (night_sim.gd:183-189), so no case
starts during a hunt (doubles off, features.gd:21); `self_cure` = last human alive, nothing else (night_sim.gd:954).

### Hands half, r2 (replaces the r1 table)
| That hand holds | Press | Hold |
|---|---|---|
| nothing | takes the glowing item (E too) | |
| wolfsbane, a creature out or turning | | raise it, any distance (as RMB today) |
| wolfsbane, no creature | | a friend in reach: give, 2 s (verb locks for the give only) |
| wolfsbane, last alive, sick, no creature | | eat it |
- **Raise = whenever a creature is out or turning** (r2 #1, #2): no 8 m ring; in step 1 nobody needs a herb then.
- A friend who turns mid-give ends the give; the still-held button raises at once (r2 #4).
- **Interim until the link is decided** (r2 #5): friends don't glow or beat items; F grab and Space struggle stay.
- **The mitten is the feedback** (r2 #6): during a give it reaches to the friend and closes over the 2 s; it pulls
  back when the give breaks; raising lifts it high.
- **Trembling hands while sick: open** (r2 #7, questions.md 20); not built: the user said hands don't show.
- **Drop:** G drops the only item; with two items, hold G and click that hand (r2 #9).
- One herb up at a time: the last button held wins (one shield slot, night_sim.gd:119). E skips friends. "pick"
  carries the hand (r2 #12); a refused pick gets a refusal event so the mitten comes back empty (r2 #13).
- **Rule count (r2 #8, honest):** each button: take / give / raise / eat. Unseen switches: "a creature is out"
  (shown by the turn's 2 s and the hunt), "last alive". Before: the same verbs plus the hidden active hand and R.
  The gain is small: one hidden mode and three keys (R, wheel, RMB-as-raise) fewer.

### Open: Claude's calls (r2 #15)
Raise on creature-out (critic's direction); the give lock; G-only / G+click drop; E into the left hand first;
mitten reach 0.15 s; one herb up at a time; the link half as a whole (questions.md 19).

## Synthesis r3 (after `docs/critic-hands-r3.md`: no severe left; the sketch to show the user)
| That hand holds | Fresh press (and hold) | While held |
|---|---|---|
| nothing | take the glowing item (E too) | |
| wolfsbane, no creature out | a friend in reach (2.6 m): give, 2 s; last alive, nobody in reach: eat | |
| wolfsbane, a creature out or turning | raise it | a creature appears mid-hold: raises at once |
| anything, you're the creature | catch (either button) | |
- **Only one automatic flip: into raise** (r3 #1). Give and eat start only on a fresh press; a hunt ending lowers a
  raised herb, never turns it into a give; a broken give never re-arms while held. One give at a time (r3 #5).
- **The hunt's end is heard** (r3 #2): turn-back plays a sound for everyone (the `human_again` event has no client
  handler today); a starve gets its own sound, not the catch scream.
- **Drop: G drops one item per press, left first** (r3 #3, no chord).
- Others see the giver's arm reach (body.gd) (r3 #4). Eat = last alive + no creature, not "sick" (r3 #6). Any turn
  ends every give (r3 #7). A note on the `doubles` switch: back on, a waiting double needs a give during a hunt (r3 #8).
- **Honest count** (r3 #10): about 10 things to know + 5 unseen switches, vs 8 + the hidden active hand today. The
  change is about feel (a hand that reaches) and one button per hand, not fewer rules.
- Open (r3 #9): Claude's reading of "not visible in screen" = a mitten shows while reaching, holding, giving,
  raising; never while healthy and empty. Pre-existing, outside the hands half: shove range 2.0 m < catch start
  2.3 m (r3 #12, questions.md 22).
