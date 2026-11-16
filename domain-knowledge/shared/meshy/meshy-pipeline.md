# Meshy pipeline: from a text prompt to a rigged model

How a character is made with Meshy AI, what each step costs, and what went wrong before.
The approvals Claude needs before each generation are in the `game-dev` skill.

## Steps
1. **Concept: text-to-image only.** `meshy_text_to_image`, model `nano-banana-2` (6 credits), `pose_mode: t-pose`.
   Every image comes from a full text prompt; no image-to-image, because edits drift the style, so a later version restates the character's identity in text.
2. **Review** the concept (downscaled) before paying for 3D.
   Regenerate at most once if it is off-style, not a T-pose, or has extra views or background props.
   A bad concept costs 6 credits; a bad model costs 15 or more.
3. **Model: image-to-3D.** `meshy_image_to_3d` with `input_task_id` = the concept task, `ai_model: meshy-t2.5`, `model_type: smart-topology`, `target_polycount: 8000`, `pose_mode: t-pose`, `target_formats: ["glb"]` (15 credits).
4. **Rig.** `meshy_rig` with `input_task_id` = the model task and `height_meters` = the character's height (5 credits).
   Download the rigged GLB from the returned URL.

## Costs
| Step | Credits |
|---|---|
| Concept (text-to-image, nano-banana-2) | 6 |
| Image-to-3D (meshy-t2.5, textured) | 15 |
| Rig | 5 |
| **One model, start to finish** | **26** |
| One animation clip (`meshy_animate`), bought once for all rigs | 3 |

## Animations
All Meshy rigs use the same 24-bone humanoid skeleton, so a clip bought once plays on every rig.
The Hips track is absolute in its source rig's units, so scale it by hip height per target rig, or models crouch or float.

## Lessons
- **Neck accessories** (neckerchiefs, collars, scarves) on a chibi build: when the big head tilts in idle, the collar mesh rises in front of the chin as a grey band.
- **Chibi animations:** clips made for normal proportions (Combat Stance, Attack) raise the paws in front of the oversized face.
  Clips that worked on a chibi rig: Idle (0), Simple Kick (103), Thrust Slash (240), Mage Spell Cast (129); walk, run, Hit Reaction and Knock Down are fine as they come.
- Keep effects **attached to the body** (flames on ears, wisps touching the hair); floating parts become stray geometry in 3D and break the rig.
- Say "single character only": the image model sometimes adds a back-view inset.
- Say "plain white background": halos and swirls end up in the mesh.
- Meshy models face +Z.
