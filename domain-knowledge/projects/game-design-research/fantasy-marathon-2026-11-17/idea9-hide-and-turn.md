## 9. Hide and Turn (written after all three critic rounds, from what they agreed on)

Why this one exists: eight ideas failed for the same few reasons.
A crew with one interest and the same facts has one answer; one end of each choice only obeyed; each threat was a pile or a rule with a one-line answer; and a perfect crew's round was a round where the idea didn't happen.
The saved research on verbs says the cheapest thing that answers all four is a person on the other side with something hidden.
This idea is that, on the mansion, werewolf and weapons the Moonsick repo already has (from its design doc; the code was not read).
It is close to the user's own project, so it is offered as a candidate and changes nothing in Moonsick's docs.

**Fantasy (Claude's; close to the user's first Moonsick line, not theirs):** it is a full moon, we are friends hiding in a mansion, and the friends the moon has already taken are hunting us.

**The fantasy, checked first**
- Does one player want and fear the same thing? A human wants to stay human, and a turned friend wants to find the rest; nobody holds both at once. This gives up "I fear turning into something powerful and it's still me", the feeling the user and Claude could not make work on 2026-11-17.
- The premise, searched earlier in this run and on 2026-11-16: the family is old and crowded (hide-and-seek, infection modes, Zombie Panic! Source, Secret Neighbor, Deceit 2, Wolfsbane, Far From The Darkness). Different because: nothing found. It is a known loop in the user's setting.

**Feelings, and the games that already cause them**
| Feeling | Games that cause it | The players are | How they do it | How it fails there | A shipped game causes it? |
|---|---|---|---|---|---|
| Hiding while a friend searches the room | MECCHA CHAMELEON; Prop Hunt | friends on two sides | hiders against human seekers; the whole rule set is "the seekers win if they find everyone within the time limit" | sold on a short life at a low price; public servers vanish when the host leaves | ✅ |
| Fear of the friend next to me | Zombie Panic! Source | one crew that loses members to the other side | an infected survivor turns after about a minute and can't tell the team; teammates may shoot them first | the infected often starts helping the other side before turning | ✅ |
| Being caught isn't the end: I get to hunt | Resident Evil Outbreak; Zombie Panic! Source | the same | a player whose gauge fills becomes a zombie they control and goes after former teammates | in Outbreak it lasts only a short time | ✅ |
| I fear being the one who turns | none found: in Zombie Panic! Source the wiki says the infected may help or hinder | | | | ❌ |
| Panic and laughing at the moment someone turns | not searched | | | | ❌ |

Sources: the verbs report and the becoming-the-monster patterns (both listed in the shared index) hold the links for MECCHA CHAMELEON, Zombie Panic! Source and Resident Evil Outbreak.

**The rules, one sentence each**
1. At a hidden moment in the first two minutes, the moon turns one friend, picked at random.
2. A turned friend who touches a human turns them on the spot.
3. If anyone is still human at dawn (five minutes), the humans win together; each friend's own number is how long they stayed human.
4. If nobody is human at dawn, the turned win.
5. Humans hide in the mansion's furniture and can move to another spot whenever they dare.
(Not in the rules on purpose: the cure potion, weapons and the race from the Moonsick design. Each would be a separate decision.)

**The choice:** stay in the wardrobe I'm in, which a hunter may open next, or run for another room while they're searching elsewhere, where I may be seen crossing the hall.
**What the other end decides, in the same second:** the hunter chooses to finish searching this room, or to stand still in the hall and listen for a door.

**Scene, 4 friends**
- The moon takes Dee at 0:50. Ana is in the kitchen cupboard, Ben under the stairs, Cy behind the attic trunk.
- Dee searches the kitchen and opens the cupboard next to Ana's. Ana decides to stay.
- Ben hears the kitchen doors and runs for the attic; Dee, who had stopped to listen, hears the stairs and goes up.
- Dee finds Ben at 2:10. Now Dee and Ben search, and Ben knows where he saw Cy go.
- Ana gains time by staying; Ben spent his hiding place for a better one and lost it; Dee gains a second hunter.
- Next round: "Ben led them straight to me" is teasing, and Ben was caught fairly by a friend playing the role the moon gave her, so no grudge.

**Scene, 3 friends (the fewest):** one hunter against two; it is plain hide-and-seek, and a caught friend leaves one human against two hunters.
**Scene, 6 friends:** one hunter against five; the first catches come slowly and the last minute has several hunters closing rooms together.

**What a perfect side's round looks like:** perfect hiders still have to guess where a person will look, and a perfect hunter still has to guess where people hid, so the idea happens every round.
The research behind this: search games with a hidden target have no fixed best plan and need mixed choices (the verbs report, with its source).

**The ratio, worked out (`scripts/hide-and-turn-ratio.py`, a toy with no walking, chases or sound)**
- 54 settings: 3, 4 or 6 friends; 12, 24 or 40 hiding spots; a hunter checks a spot every 4, 8 or 12 seconds; hiders stay put or move every 45 seconds.
- Humans nearly always win in 0 settings, nearly never in 29, and somewhere in between in 25.
- In 15 settings the humans win between a quarter and three quarters of nights, at all three crew sizes.
- The result slides with the number of spots and the search speed and has no cliff, so it can be tuned; the toy says nothing about whether it is fun.

**Older checks, run with the dropped table open**
| Check | Pass? |
|---|---|
| Something gets worse when nobody acts | ✅ the hunters keep searching and grow in number |
| A decoy beats the threat | ✅ a decoy against a person is a guess the person can answer |
| The threat hunts whoever did the last thing | ✅ no rule does; a person chooses |
| The goal is a place to reach | ✅ no |
| Each rule is written | ✅ five sentences above |
| Each end of the choice decides something | ✅ hider and hunter, above |
| One interest with open facts | ✅ two sides, and where people hide is not known |
| Leans on who can hear whom, with friends on Discord | ❌ hunters on the same Discord call hear the hiders' voices; it works only if hiders stay quiet or the two sides split calls, as Prop Hunt groups do (memory) |
| Works at 3 and at 6 | ❌ at 3 it is one hunter against two, and whether that holds a night is not shown |
| The developer can judge it alone with bots | ❌ the point of the idea is a person on the other side; a bot hunter shows the rules work and not the fun, the failure the postmortem lists as "bots can't test bluff" and "judged solo" |
| Lag | ✅ a touch is the only joint act |
| Carried from a dropped family | ✅ none of the three; it keeps the mansion and the werewolf from Moonsick, and drops the sickness, the cure and the race |
| A drop reason from this file applies | ❌ "the premise is shipped" (Mimic, Dead Weight, Low Tide): this is a public, crowded family with only the setting as its difference |
| Still cooperative | ❌ after the first turn it is friends against friends, the thing the user questioned on Moonsick's race ("this is basically pvp no?") |

**Marks:** hiding while a friend searches ✅ · fear of the friend next to me ✅ · being caught isn't the end ✅ · I fear being the one who turns ❌ · panic and laughing at the turn ❌.

**Still failing**
- It can't be judged by the user alone with bots, and their friends are rarely online.
- It is not cooperative after the first turn.
- It is a crowded family with a thin difference.
- Discord.
- Three friends.

None of these is the "one answer" failure that took the other eight.
They are the price of a person on the other side.
