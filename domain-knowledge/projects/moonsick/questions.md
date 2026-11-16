# Open choices for the user

Claude's pick is in brackets after each choice.
Nothing here blocks playing.
Each choice is built Claude's way unless it says otherwise, and is easy to change.
The numbers stay fixed, because code comments point to them.

1. **Name:** Moonsick (the sickness from the moon) or Turncoats (turning plus traitors).
   Neither is on Steam. [Moonsick]
2. **Players:** 4–8, tuned for 5–6.
   2–3 are allowed with a warning, and the host can add practice bots. [keep]
3. **Creature powers (Claude):** werewolf howl (whoever moves within 30 m in the next 3 s shows), vampire leap (reaches the tree house), troll stomp (knocks back a pair holding it off). [keep; judge in a playtest]
4. **Helping beats fleeing (your ask; the critic's rule):** at the turn, those near get a 5 s head start, those far are shown for 10 s, and whoever tried the right cure gets a 10 s head start.
   [keep; Claude's first fix failed its critic]
5. **Curing a creature after it turned** would be a third ending, and it bends your "hunt or die". [no]
6. **In-game voice:** built, with proximity, deeper creature voices, the knocked-out silent and the dead heard flat.
   Discord still works, and no rule depends on voice. [keep; ask friends to use it]
7. **Liars exposed at the end?** Your call was never, and the reel shows only public facts. [done]
8. **Art:** items, props and creatures are Meshy models now, and the friends' bodies are still code shapes (see 14). [later]
9. **Night length:** 12 min. [test 10 and 15 with friends]
10. **Multikills:** you asked whether a creature should get more than one catch in its 10 s turn-back.
    It's off for now, because in play the second catch could only reach the helpers standing next to the first, which punished helping.
    `--multikill` turns it on to try. [off]
11. **Powers:** on, for your pillar that each creature has its own powers, though step 1 turns them off for now.
    If the first playtest feels busy, a `--no-powers` flag is easy to add. [on]
12. **Practice lessons (Claude, from the UX critic):** 3 lessons of 6, 8 and 12 min.
    Dawn moves you on, and the menu can pick any.
    Step 1 turns them off.
    [keep; tell me if lesson 1 still leaves you lost, because then the rules need cutting, not more UI]
13. **Notes never name the answer:** each fact says what it rules out, and you combine them.
    The critic's case is that naming the cure turns the night into obeying one line.
    Step 1 turns notes off.
    [keep; if it feels like homework, the smallest step is a "possible: werewolf or troll" line in lesson 1 only]
14. **Meshy next:** the creatures are static Meshy models with no rig, so they glide and lean.
    Rigging plus a walk and run animation (~5 credits each plus wiring) and the friends' own bodies come next.
    [after your playtest; check that the creatures read as werewolf, vampire and troll at a glance]
15. **The stove's painted embers** are a texture, not a light, to keep your "moonlight only". [keep; regenerate it cold if it reads as fire]
16. **The main choice is fake (critic):** giving a cure on the first sign always wins, 90% cured against 74% for waiting, in v0.1 too.
    A wrong cure costs about what waiting costs, and it tells you the answer.
    [step 1: a wrong cure turns the friend at once, so the best play becomes waiting for a second sign; a choice that changes with the situation (cures far away, two sick at once, a late second sign) comes after you play step 1]
17. **Why would anyone lie?** With pans cut, a sick friend has no reason to hide signs, and a fixed schedule exposes "I feel fine" from stage 2 on.
    [step 1 leaves betrayal thin on purpose; name the motive after step 1 reads]
18. **Pillars step 1 bends:** tools needed to diagnose, knocking out, each creature's powers, signs hard to read (now easy to see but hard to interpret), bluff from both sides, liars never exposed, signs always different, and the dark (only decor in step 1).
    [all come back one by one once the core reads]
19. **Hands: what makes a held friend pull away in step 1? (critic)** With werewolf only, holding halving the case and nobody lying, nobody wants out, so a stretch link only works on bait.
    [Claude: make the werewolf's catch the link, where the victim pulls away, the werewolf pulls back and a raised wolfsbane breaks it; holds between friends use the same rule when lying comes back; see `docs/hands-thesis.md`]
    Built this way, not committed yet: the switch is `catch_link` in `scripts/core/features.gd`, and off is the first frozen catch.
    Holding a friend is now your chain (walk away to drag, stand still and they slip free), and the catch uses the same chain; built, not committed yet (`docs/holding-thesis.md`).
    Still open: in honest step-1 play a held friend has no reason to pull away, so the chain only matters for bait, griefing and the hunt.
20. **Hands on screen (Claude's reading of your "not visible in screen"):** a hand shows only while reaching, holding, giving or raising, never while healthy and empty.
    The core plan also wanted your hands to tremble while you're sick, as the sign that you're sick. [not built; your call]
    The rest is built this way, not committed yet.
21. **Drop is G (Claude, from the critic):** one item per press, left hand first, and E stays pick up.
    Built, not committed yet.
22. **A shove could miss a catch it should break (critic; an older bug):** a catch starts at up to 2.3 m, a shove reached only 2.0 m, and a catching werewolf moves at 0.25 speed.
    [shove range at least the catch range plus lag]
    Built at 2.3 m, not committed yet.
23. **Should a hold have a time limit? (Claude, holding design)** A holder who keeps walking can drag a friend forever, because the friend trails behind and every step pulls.
    [no limit for the first playtest; the holder can't give, take or raise meanwhile; add a limit if people use it to grief]
    Built with no limit, not committed yet.

## Bluff rules review (2026-11-15, critic round 1; `bluff-rules-thesis.md`)
- Q-B1 Strip the bluff rules back to the pillars + built game and spec "everyone a little sick" with numbers first? **Claude: yes.**
- Q-B2 The lie needs fleeing late to beat helping, which bends "helping beats fleeing". Bend it, or find a lie that doesn't need it? **Claude: find another lie; the built steal/tug fake swap is the first to try.**
- Q-B3 Turn the head start back on so a far liar can be caught? **Claude: yes.**
- Q-B4 Give the human a physical offer verb bots can read? **Claude: yes, holding an item out toward a bot.**
- Q-B1 answered (user 2026-11-15: "strip the rules"): stripped in design.md.
- Q-B5 A friend thrown off at the turn: free to run, or knocked down? Only matters for the new attack. **Claude: free to run.**
- Q-B6 Turning early (TODO part 5): the critic found it pays more than curing (an unwarned friend next to you is struck at 5.0 s and eaten at 6.5 s, while your case is still curable for 17–41 s), and bots can't react to it. Cut it, or bring it back with a cost that makes an early turn end worse than a cure? **Claude: cut it; not built.**
- Q-B3 update (2026-11-15, critic r1 S2): the 5 s head start is measured after the 2 s turn, and a werewolf sprints at 11.2 m/s, so staying near still gets you struck at 5.0 s. Sizing it against the walk to the pond's wolfsbane comes first. **Claude: keep it off until then; not turned on.**
- Q-B4 built (Claude's pick): holding an item out toward a sick bot makes it stand still for your give; no new verb.
