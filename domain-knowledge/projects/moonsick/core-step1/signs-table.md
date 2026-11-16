# Signs of each transformation

**Werewolf only for now (user):** vampire and troll are switched off.
A sick werewolf feels the dark looking lighter and a craving for raw meat.
The others see glowing eyes and drooling, and the cure is wolfsbane.
The full table below stays for when the vampire and troll come back.

The source of truth is "The signs" in `docs/design.md`.
Tools are switched off by step 1 (`scripts/core/features.gd`).

| Turning into | The sick player feels (only they know) | Everyone else can see | Tool (now off) | Cure |
|---|---|---|---|---|
| **Werewolf** | the dark looks lighter (stronger in dark rooms) · craving raw meat (the view drifts toward it, stronger in the kitchen) | glowing eyes · drooling | silver spoon: the skin reddens | wolfsbane |
| **Vampire** | the dark looks lighter · moonlight stings (the view flares white in moonlight) | glowing eyes · grey stony skin | silver spoon reddens · thermometer reads cold | garlic |
| **Troll** | moonlight stings · craving raw meat | grey stony skin · drooling | thermometer reads cold | rowan |

## Over a case (75 s at dusk, 60 s by the end)
- **First third:** one sign, felt or seen, at random (the % per sign decides which).
  If it's a seen one, the sick player doesn't know they're sick.
- **Second third:** one sign of the other kind, and dark veins start up the neck.
  Others see the veins within 4 m, and the sick player never sees their own.
- **Last third:** the remaining felt sign and seen sign, and the veins reach the face.
  Then the friend turns.

## Why it's hard to read
- Glowing eyes show only in the dark or within 2.5 m.
- Grey skin and drool show only in moonlight or within 2 m.
- Each sign fits two monsters, and two signs from different rows name it for sure.
- Nothing on screen explains this any more, since step 1 has no screen UI and no text.
