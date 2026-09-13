# Research Notes — Character Animation Application

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a dedicated Character Animation Application really is from real products: its central object (the rigged character), its rigging model, its animation methods (keyframed posing, performance capture, physics, motion libraries), its delivery targets (video vs runtime animation data vs live output), and — critically — whether this leaf is an independent Type or merely a capability/variant inside general 2D/3D animation products (the open flag left by both sibling leaves, 2d-animation-application and 3d-animation-application).

## Initial Boundary (hypothesis before research)

- What: software whose central object is an articulated character (appearance bound to a rig) and whose primary workflow is producing that character's motion.
- Users: character animators, game developers, VTubers/live performers, indie cartoon producers.
- Nearest neighbors: 2D Animation Application, 3D Animation Application (both siblings flagged this leaf as probable Variant/Capability), Motion Graphics, AI Avatar Video Generator, Digital Sculpting/3D Modeling (character creation), Stop-motion, live avatar/performance apps.
- Open questions: does a dedicated product category exist with its own world model, or is "character animation" only ever a capability? Is the rig the defining object? Are performance capture / physics / lip sync definitional? Is the output video, runtime data, or both? Where exactly is the line against general animation suites?

## Research Questions

1. What is the central persistent object (skeleton, puppet, rigged model, character)? How is it structured?
2. How is the character acquired (imported artwork/mesh, templates) and how is the rig built and bound (bones, deformers, parameters, weights, pins, sprites)?
3. By what means is motion produced: keyframed posing, performance capture (face/body/lip sync), physics, motion libraries, AI assistance? Which are definitional?
4. What is the time model (timeline, keyframes, interpolation, motion clips, live recording)?
5. What are the delivery targets: rendered video, runtime animation data for games/apps, live performance output?
6. What interfaces exist (rigging mode vs animation mode, viewport/stage, timeline, parameter panels, libraries)?
7. What rules/behaviors matter (binding/inheritance, keyframe semantics, clip sampling/flattening, rig compatibility for motion reuse, editor/runtime versioning)?
8. Where are the boundaries against 2D Animation, 3D Animation, and the other neighbors — and does the sibling "Variant/Capability" flag hold?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| Spine (Esoteric Software) | 2D skeletal animation for games; editor + runtimes; animation as data | game developers (indie → studio), perpetual licenses | A (user guide: skeletons, bones, animating, getting started; full doc tree) |
| Cascadeur (Nekki) | physics-assisted keyframe character animation "without motion capture" | game/film animators, free+pro tiers | A (help: introduction, workflow basics, rig structure; full doc tree) |
| Live2D Cubism (Live2D Inc.) | parameter-rigged 2D character models from illustrations; interactive/live use | VTuber/interactive market, app/game embedding (Japan-centric origin) | A (editor manual: production flow, parameters; full doc tree) |
| Cartoon Animator (Reallusion) | template/motion-library-driven 2D character content production | content creators, educators, indie studios | A (product pages: character creation, animation editing; official manual page) |
| Adobe Character Animator | real-time performance-driven puppet animation (webcam/mic) | creative prosumer/pro | C-degraded (helpx.adobe.com timeout ×2, adobe.com timeout ×1 — abandoned per source-access rules) |

Adobe Character Animator is retained as a market reference only (its performance-puppet positioning is well known), but no operational claim about it is made anywhere in this research or the final document. All Type-level findings are supported by the four fully-researched products.

## Sources

Fetched 2026-09-06:

- Spine — Getting started: https://esotericsoftware.com/spine-getting-started
- Spine — User Guide (TOC): https://esotericsoftware.com/spine-user-guide
- Spine — Skeletons: https://esotericsoftware.com/spine-skeletons
- Spine — Bones: https://esotericsoftware.com/spine-bones
- Spine — Animating: https://esotericsoftware.com/spine-animating
- Cascadeur — Introduction: https://cascadeur.com/help
- Cascadeur — Workflow Basics: https://cascadeur.com/help/getting_started/workflow_basics
- Cascadeur — Rig Structure: https://cascadeur.com/help/rig/rig_structure
- Live2D — Editor Manual top: https://docs.live2d.com/en/cubism-editor-manual/top/
- Live2D — Production Flow: https://docs.live2d.com/en/cubism-editor-manual/workflow/
- Live2D — About Parameters: https://docs.live2d.com/en/cubism-editor-manual/parameter/
- Reallusion — Cartoon Animator product page: https://www.reallusion.com/cartoon-animator/
- Reallusion — 2D Character Creation page: https://www.reallusion.com/cartoon-animator/2D-character-creation.html
- Reallusion — 2D Character Animation page: https://www.reallusion.com/cartoon-animator/2D-character-animation.html
- Reallusion — Cartoon Animator manual, Sampling and Flattening Keys: https://manual.reallusion.com/Cartoon-Animator/Content/Resources/4.2/09_Timeline/Sampling_and_Flattening.htm
- Attempted and abandoned: https://helpx.adobe.com/character-animator/user-guide.html (timeout), https://helpx.adobe.com/character-animator/get-started.html (timeout), https://www.adobe.com/products/character-animator.html (timeout)

## Product Observations

### Spine (evidence layer A unless noted)

- Positioning: 2D skeletal animation; the product is explicitly split into the **Spine editor** (authoring) and **Spine Runtimes** (code libraries that "load and render your animations" in games, apps, websites). Export is "efficient binary and JSON formats" plus packed textures; runtimes integrate with Unity, Unreal Engine, Cocos2d-x, PixiJS, GameMaker, plus generic/third-party runtimes. Runtime APIs "provide direct access to your skeletons and animations, allowing them to interact with your users and game world. You can also combine animations, crossfade them, and more."
- Central object: "A skeleton represents an animatable character or object. It has bones, slots, attachments, animations, and other parts." A project may hold multiple skeletons; draw order between skeletons is tree order.
- Bones: hierarchy with "always a single root bone"; each bone has rotation, translation, scale, shear ("the bone's transform"); "A bone's transform affects its child bones" (translating an arm bone also translates the hand bone); inheritance is configurable per component (Rotation/Scale/Reflection checkboxes, itself keyable). Bone length is "cosmetic" except for IK/path constraints and auto weights.
- Binding: "It's not enough just to animate bones, we need a way to attach images and other things to the bones" — attachments are grouped under a **slot**, the slot is attached to a bone; the slot controls which attachment is visible and its color. Attachment types: region, mesh (deformable, with weights), bounding box, clipping, path, point. Images are prepared in external image editors (Photoshop etc.) using official scripts/plugins that can even pre-create bones.
- Skins: named visual sets; skin bones are "only active when the skins are visible" — the swap mechanism for characters with interchangeable equipment/appearance.
- Constraints: IK, path, transform, physics (physics-based secondary motion), sliders.
- Animation: keys on bone transforms and other properties; dopesheet, graph view (curves), timeline, ghosting, playback view. Documented workflows: straight ahead, pose to pose ("blocking"; `Stepped` playback disables tweening so only key poses show), layered (animate subsets of parts in passes), combined. Curves "adjust the speed of a transition between keys."
- Import/export: PSD import; texture packing; image/video export; command-line interface; editor version must be kept in sync with runtime version ("ensures you won't accidentally use a newer editor version that is incompatible with the Spine Runtimes version you are using").
- Reading: Spine = the purest "character-as-data" product: the entire world model is skeleton + binding + keyed animation, delivered as runtime data for interactive use.

### Cascadeur (evidence layer A unless noted)

- Positioning: "Cascadeur is a software for creating character animation without motion capture. Using physics-based approach, it allows for creating expressive and realistic animations for movies and video games."
- Documented workflow (Workflow Basics): 1. **Prepare the scene** — import a character (FBX/DAE; also USD, GLB/GLTF/VRM; from Unreal, Blender, Daz Studio, Mixamo rigs, Character Creator, MetaHumans) and **rig** it (Quick Rigging Tool; rigging tools; advanced rigging chapters). 2. **Set poses** — "Animation in Cascadeur is made up of poses." AutoPosing: "you only have to move one or two controllers — big green points on the character — and the rest of the body would move on its own, creating a realistic pose." For more control: Point Controller mode (manual, precise) and Box Controller mode (rotations, small details), all adjusted with manipulators. 3. **Manage keyframes** — "Poses are stored in Keyframes"; place them manually on the timeline or enable "Set key on change" (auto-key on pose change); "You don't need keys for each and every frame — you only have to set a pose for every crucial point." 4. **Add interpolations** — intervals between keyframes produce "a rough animation draft." 5. **Further improvement** — "Applying Physics Tools to make character movement physically accurate" and "Polishing resulting animation using tools such as Filters and Trajectories."
- Rig: "A rig is made up of several components that make character animation possible." "An object without a rig can still be animated, but possibilities for its animation are limited. Also, Cascadeur needs a rig to calculate physically correct movements. So, physics tools such as Ballistic Trajectories can only be applied to rigged characters." Rig elements: point controllers, box controllers, rigid bodies, joints, meshes, edges, direction controllers, collision shapes, center of mass; created during rigging by attaching prototype objects to joints; behaviors define handling.
- Physics toolset: Center of Mass, Ballistic Trajectory (+ ghosts), Fulcrum Points, AutoPhysics (with compensation motion, corrector, geometrical constraint, nonlinear solver, rotation smoothness), Ragdoll, Secondary Motion, Interaction with Environment, collision-penetration and fulcrum-motion cleaning.
- Other animation machinery: Tween Machine, Graph Editor, trajectories (with rotation/direction variants), ghosts, silhouette, interval edit mode, mirror/copy tools, retargeting, animation unbaking, blend shapes, inbetweening, easing, additive layers (alpha), mocap (alpha), Motion Generation (AI), Python scripting/API, node editor, spline IK, root constraint, Live Link for Unreal Engine.
- Scene: multiple characters per scene; non-humanoid characters; riggable props; camera tools (first-person camera); lights; outliner; scene/physics settings; Teams Management System.
- Delivery: export FBX/DAE to Unreal Engine, Unity, Blender, Roblox Studio, Daz Studio; USD; GLB/GLTF.
- Reading: Cascadeur = character animation as a dedicated discipline: the mesh is imported (not modeled), the rig is the product's central structure, and the entire toolset exists to produce believable character motion (poses → keys → physics → polish), delivered as animation data for engines.

### Live2D Cubism (evidence layer A unless noted)

- Positioning: "Live2D Cubism Editor is a 2D modeling tool that creates three-dimensional expressions from illustrations."
- Production flow (official): STEP 1 — prepare source images: "Separate the illustration into pieces for each part to be moved. Add the parts of the illustration that are visible when the illustration is moved" (e.g. closed eyelids, open mouth — states that don't exist in the original art). STEP 2 — modeling: import into the editor; "editing functions such as 'Deformer,' 'Parameter,' and 'Glue' can be used to efficiently add a range of motion"; template function partially automates rigging. STEP 3 — animation: "Import the model with motion added in STEP 2 into the Animation Workspace and create an animation. Using the 'Dope Sheet' and 'Graph Editor,' you can create subtle and smooth animations by specifying keyframes along the timeline." STEP 4 — export: video, GIF, numbered stills, "or file for applications and games" (iOS, Android, Unity, OpenGL, DirectX, web browsers, home game consoles).
- Model structure: Parts (hierarchical containers), ArtMeshes (auto-generated meshes over each part's texture), Deformers (Warp Deformer, Rotation Deformer, organized in parent-child hierarchies), draw order, clipping masks, Glue (attaching objects to each other).
- Parameters (the distinctive control model): "A parameter is a setting that expresses a specific movement, such as [Angle X] or [Mouth Open/Close]... two keys are created for the parameter [Mouth Open/Close], and 'closed' and 'open' are assigned to each, respectively. The shape is automatically interpolated between the keys." Parameters carry minimum/default/maximum values; a "Standard Parameter List" recommends common parameter IDs "since motion data created in the Animation Workspace can be easily shared later" across models; parameter groups; blend-shape parameters. Keyforms = the deformed shapes stored at parameter keys. "Record Parameter Operations and Generate Animations" — recording slider manipulation as animation.
- Animation workspace: scenes; timeline palette; dope sheet; graph editor; eye-blink settings; pose switching; form animation (FA); image-sequence tracks; frame step (limited animation); animation templates; fade values (for runtime blending); loop editing; parameter controller; bake animation from physics; motion-sync (audio-driven) with bake.
- Physics: "sway model parts with physics" (hair, clothes, accessories); physics can be baked into animation.
- Delivery/embedding: moc3/motion3 "Data for Embedded Use"; Cubism SDK manuals; Cubism Viewer (for OW) and Viewer for Unity; expressions; playlists; user data/events; external application integration + external API; After Effects plugin (model display, motion import/export, physics, **tracking function**); nizima LIVE — "Official Live2D tracking app" (face-tracking live avatar performance); nizima marketplace for model data.
- Reading: Live2D = the parameter-rig pole of the Type: the character is a rigged illustration whose "range of motion" is authored as named parameters with interpolated keyforms; motion is produced by keyframing parameters over time, recording parameter manipulation, or driving parameters live (face tracking / SDK input) — and the same model file is delivered both as video and as an interactive embedded asset.

### Cartoon Animator 5 / CTA (evidence layer A unless noted)

- Positioning: "Cartoon Animator is a 2D animation software and a versatile animation maker designed for ease of entry and productivity. Turn images into animated characters, drive facial animations with your expressions, generate lip-sync animation from audio, create 3D parallax scenes, and produce 2D visual effects."
- Character acquisition & rigging (2D Character Creation page): import images/photos → **2D Bone Editor**: "structure sophisticated bone rigs... use pins to constrain areas to selected bones, and optimize subdivision topology for smoother bending effects"; "The easiest way of 2D character creation is by simply aligning bones along an image shape." Spring bones (v5): characters "jiggle and react to simple movements with secondary motion." **Mask Editor** cuts images into separate sprite layers; **Sprite Editor** manages multiple sprites per body part ("various hand gestures and mouth shapes"); **Layer Order Manager** sets display priority; **Sprite Sequences** import SVG/PSD/bitmap sequences for "smooth transitions in gestures, eye movements, and lip sync" (loop / play once / split into sprites); sprite+smooth hybrid (v5.33) blends sprite swaps with vector deformation. **Character templates**: "full facial and body rigged character templates... shared bones structures while enjoying a huge library of cartoon motions"; custom templates let unique creatures (T-REX ↔ Red Dragon) "share the same structured motion assets." Character families include G3 Human/Animal/Spine/Wings (sprite hand vs bone hand distinction).
- Animation (2D Character Animation page + manual): "Add your preferred 2D and 3D motions from the extensive motion library"; motion libraries for humans, quadrupeds, spine/wings with Start(1S)/Loop(2L)/End(3E) structure; "directly drag motions to animate your character." Timeline model (manual, Sampling and Flattening Keys): "A **Motion** is the combination of the **Motion Clip** and the **Layer Keys**." **Sample** turns a motion clip's keys into editable layer keys per body part (e.g. sample LHand/RHand, then edit hand poses in the Hand Pose Editor, reposition via tracks); **Flatten** merges layer keys back into the clip, which "can then be reused on different characters" (exported as .ctBMotion). Motion Curve Editor combines "pose keys with curve motion." IK/FK control; 2D Motion Key Editor with Reset keys to counteract clip transitions; spring-bone secondary motion; exaggeration tools (squash & stretch, anticipation, follow through).
- Performance input: "drive facial animations with your expressions" (facial tracking), "generate lip-sync animation from audio," 2D motion capture, 3D motions converted to 2D (ActorCore mocap library), Motion Pilot puppet animation, motion-path animation.
- Live output (v5.3): "Puppet Stage and Live Camera System... Integrate animation blending, voice sync, and motion capture for quick 2D production and live streaming"; trigger animations in realtime with premade motions, facial tracking, VFX; "live camera controls, hotkeyed camera cuts, and smooth camera transitions."
- Content economy: 1700+ free resources, Smart Content Manager, Content Store, ActorCore, Marketplace; animated accessories attachable to body parts with grouped/individual animation triggers; Quick Perform List (right-click action menu of voice/facial/body motions).
- Reading: CTA = the content-production pole: rigged characters as reusable assets, motion libraries and templates as the engine of productivity, performance capture and lip sync as input, timeline clip/layer-key editing for polish, and both video and live streaming as delivery.

### Adobe Character Animator (evidence layer C — degraded)

- Official documentation could not be fetched (helpx.adobe.com timed out twice; adobe.com timed out once). Per source-access rules, no operational claims are made from memory.
- Retained as the market-representative performance-driven puppet product (real-time face/mic-driven character animation, part of a creative suite). Its inclusion rests on market position; all Type-level findings are supported by the four fully-researched products.

## Cross-product Comparison

| Dimension | Spine | Cascadeur | Live2D Cubism | Cartoon Animator |
|---|---|---|---|---|
| Central object | skeleton ("an animatable character or object": bones + slots + attachments) | rigged character (rig: controllers, joints, rigid bodies, meshes) | model (parts + art meshes + deformers + parameters) | character (bone rig + sprites + spring bones) |
| Appearance source | images prepared in external editors (PSD import + scripts) | imported mesh (FBX/DAE/USD/GLB/VRM; Mixamo/CC/MetaHuman) | separated illustration (PSD layers, incl. hidden states) | imported images/photos (mask/sprite cutout) |
| Rigging stage | build skeleton, create slots, attach images/meshes, weights | rig mode: quick rigging, prototype objects on joints | modeling workspace: deformers + parameters + keyforms | 2D Bone Editor: bones + pins + springs; sprite setup |
| Control surface | bones + constraints (IK/path/transform/physics) | controllers (AutoPosing / point / box) | named parameters with value ranges (Angle X, Mouth Open/Close) | bones (IK/FK) + motion clips + sprite switches |
| Deformation model | bones transform attachments; meshes with weights deform | joints/rigid bodies drive mesh; physics solver | deformers warp art meshes; keyforms interpolate per parameter | bones bend image regions (pins constrain); sprite swap sequences |
| Motion authoring | keyframes on bone transforms; straight-ahead / pose-to-pose / layered | poses → keyframes ("set key on change") → interpolation intervals | keyframes on parameters (dope sheet + graph editor); record parameter operations | motion clips from library + layer keys; motion curve editor |
| Performance capture | not a feature | mocap (alpha) + retargeting | face tracking via companion app (nizima LIVE); motion-sync (audio lip sync); AE plugin tracking | facial tracking ("drive facial animations with your expressions"); lip-sync from audio; 2D mocap; Motion Pilot puppeteering |
| Physics | physics constraints (secondary motion) | core identity: AutoPhysics, ballistic trajectories, fulcrum points, center of mass, ragdoll | sway physics (hair/clothes), bakeable | spring bones (secondary motion) |
| Motion reuse | skins (visual variants); template skeletons | retargeting; animation transfer between characters | standard parameter IDs → motion data shared across models | motion library; character templates with shared bone structures; motion clip export (.ctBMotion) |
| Time model | frame timeline; dopesheet; graph; stepped playback | frame timeline; keyframes; interpolation intervals; playback tools | timeline; dope sheet; graph editor; frame step | timeline; motion clips + layer keys; reset keys |
| Delivery | JSON/binary + textures → runtimes (Unity/Unreal/Cocos2d-x/PixiJS/GameMaker); also image/video | FBX/DAE/USD/GLB → UE/Unity/Blender/Roblox/Daz; Live Link UE | video/GIF/stills; moc3/motion3 for SDK embedding (apps/games/consoles); AE plugin | video (incl. transparent for compositing); AE script; live streaming (Puppet Stage) |
| Live/interactive use | runtimes combine/crossfade animations interactively | Live Link into UE | SDK-driven interactive models; face-tracked live avatars | Puppet Stage realtime shows; live camera cuts |
| Scene scope | multiple skeletons per project; draw order | multi-character scenes, props, cameras, lights | scenes with model + background + audio | scenes with characters, props, 3D parallax scenes |
| Drawing/modeling in-product | no (imports artwork) | no (imports meshes) | no (imports PSD; mesh generation over art only) | no (imports images; mask/sprite cutout) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Character Animation Application is recognizable when all of the following hold:

1. **Articulated character as the central persistent object** — the application's unit of work is a character figure whose appearance (layered artwork or mesh) is bound to an animatable control structure (skeleton/rig/parameter set). The character is built, refined, and reused across sessions as an asset — it is not one element among many in a scene or frame composition.
2. **Rig-driven deformation** — the user animates by manipulating the control structure (bones, controllers, parameters); the bound appearance follows and deforms accordingly. Per-frame redrawing of the character is not the method.
3. **Time-based performance** — motion is authored over a timeline: poses/parameter states pinned at frames with computed in-betweens, and/or captured from live performance input (face/body tracking, lip sync, puppeteering) recorded onto the timeline.
4. **Delivery of the animated character** — as a rendered moving image and/or as animation data consumed by a runtime (game engine, application, live avatar system).

Remove #1 → general 2D/3D animation (scene/frame world). Remove #2 → hand-drawn frame animation or stop-motion (content defined per frame, not via a rig). Remove #3 → static character creation/rigging (modeling/sculpting territory). Remove #4 → a rigging utility, not an animation application.

The core is dimension-agnostic (2D artwork rigs and 3D mesh rigs both satisfy it), method-agnostic (keyframes, performance capture, physics, motion libraries all satisfy #3), and delivery-agnostic (video, runtime data, live output all satisfy #4).

### L1 — Common Mature Structure

Present across the researched sample; not required for recognition:

- a distinct rigging/setup stage with its own tools and often its own workspace/mode (bone editor, deformer/parameter setup, weight/pin binding, sprite setup)
- import of the character's appearance from external authoring tools (layered PSD; meshes FBX/DAE; images), with layer/part separation guidance
- keyframe timeline with dope-sheet and curve/graph editing; auto-key ("set key on change") modes
- pose-to-pose / straight-ahead / layered animation workflows (documented by products as standard practice)
- constraints (IK/FK, path, transform) shaping how controls drive the figure
- physics-driven secondary motion (spring bones, sway, ragdoll, ballistic/fulcrum correction), often bakeable
- performance capture: facial tracking, lip sync from audio, body mocap, mouse puppeteering — recorded onto the timeline as editable keys/clips
- motion libraries, pose libraries, character/rig templates; motion transfer between characters (retargeting; standardized parameter IDs; shared bone structures)
- sprite/attachment swapping for expressions, hand gestures, mouth shapes (visual state sets; skins)
- motion clips as reusable units with layer keys for per-part refinement (sample/flatten pattern)
- preview/playback vs final export split
- multi-character scenes; riggable props
- export to game engines/applications as runtime animation data (JSON/binary + textures; FBX/DAE; moc3/motion3) alongside video/image output
- live output surfaces (streaming puppet stages; face-tracked live avatars via companion apps)

### L2 — Variant / Optional Structure

- dimension/substrate: 2D artwork rigs (layered images + bones/deformers) vs 3D mesh rigs (joints + skinning)
- control philosophy: bone-skeleton rigs vs named-parameter rigs (slider axes with value ranges and interpolated keyforms)
- animation posture: hand-keyframe skeletal animation (Spine), physics-assisted keyframing (Cascadeur), motion-library/template-first content production (Cartoon Animator), parameter/interactive-first modeling (Live2D), performance-first puppeteering (Adobe Character Animator positioning)
- primary delivery: game/runtime data (Spine, Cascadeur, Live2D SDK), video production (Cartoon Animator, Live2D), live performance (Puppet Stage, nizima LIVE)
- market: game developers, VTuber/interactive avatar creators, cartoon/edu content producers, film/game animators
- AI assistance (motion generation, assisted posing), mocap depth (alpha features to full pipelines)
- content economy (asset stores, marketplaces, template ecosystems)
- licensing (perpetual tiers, free+pro, subscription suites)

### L3 — Vendor-specific (research notes only)

- Spine: slots/attachments terminology, skins, runtime versioning lockstep, texture packer, CLI, ghosting/metrics/weights views, editor-version launcher.
- Cascadeur: AutoPosing, AutoPhysics family, fulcrum points, ballistic trajectories + ghosts, center-of-mass tool, interval edit, Tween Machine, quick rigging, prototype objects/behaviors, Teams Management System, Motion Generation.
- Live2D: parameters/keyforms/deformers (warp/rotation), ArtMesh/ArtPath, Glue, Standard Parameter List, motion-sync, playlists, form animation (FA), Cubism Viewer (for OW / for Unity), nizima ecosystem, material-separation Photoshop plugin, AE plugin.
- Cartoon Animator: G3 character families (Human/Animal/Spine/Wings), sprite vs bone hands, Motion Clip/Layer Key sample-flatten model, .ctBMotion format, Puppet Stage, Motion Pilot, 360 Head Creator, ActorCore pipeline, Quick Perform List, Smart Content Manager.
- Adobe Character Animator: not documented here (sources unreachable).

## Rejected Findings (not promoted to core)

- "Performance capture defines the Type" — rejected: Spine and Cascadeur center on keyframed posing; capture is a common input method (L1), performance-first is a posture (L2).
- "Physics defines the Type" — rejected: only some products make physics central; others offer only secondary-motion springs or nothing beyond constraints. L1/L2.
- "Lip sync defines the Type" — rejected: common and heavily marketed, but absent from core skeletal workflows. L1.
- "Game-engine output defines the Type" — rejected: video production and live output are equally first-class deliveries in the sample. Runtime-data delivery is L1 common, not invariant.
- "2D-only or 3D-only" — rejected: the core holds across both dimensions; dimension is L2.
- "A character animation application must also draw/model the character" — rejected: every sampled product imports the appearance from external tools; in-product authoring of appearance is not part of the pattern (mask/sprite cutout in CTA is preparation of imported images, not drawing).
- "Character animation is only a capability, not a Type" — partially rejected: the sibling leaves' observation is confirmed as fact (general animation products include character rigging/animation as a capability), but dedicated products exist in numbers and variety, with a distinct center of gravity: the character rig as the persistent central object and rig-driven performance as the whole workflow. The honest resolution is a Type with a gradient boundary (see Boundary Findings).

## Boundary Findings

- **vs 2D Animation Application (sibling, flagged for joint review)**: 2D animation centers on authoring frame content in a composition (drawing cels, tweening layered artwork, cameras, effects); character animation centers on the rigged character itself. Overlap is real and wide: rig-first 2D products (rigged cut-out workflow) satisfy both cores, and every general 2D animation product in the siblings' sample ships rigging as a capability. Test: remove the character-as-central-persistent-object (animate scenes, effects, typography, drawn frames) → 2D animation; remove general frame/scene composition (only the character and its motion matter; appearance is imported, not drawn) → character animation. The dedicated products sampled here all fail the 2D-animation center in one respect: none offers frame-by-frame drawing or general scene/effects composition as a primary surface. Joint review of the three 04.08 siblings recommended; no unilateral taxonomy change.
- **vs 3D Animation Application (sibling, flagged for joint review)**: same structure at the 3D end. Cascadeur is the cleanest discriminator: it imports meshes (no modeling), rigs them, animates with poses/keys/physics, and exports animation data — no scene-composition/rendering pipeline as first-class surfaces. A general 3D animation application contains character animation as a capability; a dedicated character animation application is organized around the character as its only first-class object. Test: cameras/lights/materials/scene composition as first-class → 3D animation; character rig as the sole first-class object → character animation.
- **vs Motion Capture (capability, not a leaf here)**: capture is an input method recorded onto the same timeline; products range from alpha features (Cascadeur) to companion apps (nizima LIVE) to core marketing (CTA facial tracking). Not a boundary against a Type.
- **vs AI Avatar Video Generator**: avatar generators produce talking-avatar video from scripts/text with minimal user control over the performance; character animation applications give the user direct control of the rig/poses/performance. Test: who authors the performance — the user (character animation) or the system from text (avatar generator).
- **vs Digital Sculpting / 3D Modeling / character creation**: static character creation has no time axis and no performance; character animation applications import rather than author appearance (confirmed across all four sampled products).
- **vs live avatar/performance applications** (e.g. face-tracking live drivers): these drive pre-built models in real time; they are a delivery/consumption surface of this Type (Live2D ships one as a companion product; CTA embeds a live stage). The authoring application is the Type; the live driver alone is adjacent.
- **vs Stop-motion Animation Application**: shared "pose a figure over time" spirit, but stop-motion captures physical media per frame; character animation deforms a digital rig. Remove the rig → stop-motion; remove the physical capture → character animation.
- **vs Video Editor**: video editors sequence captured media; character animation authors the character motion that editors may consume (CTA explicitly exports transparent video for compositing).

## Uncertainties

- Adobe Character Animator evidence is degraded (all Adobe hosts unreachable); its inclusion rests on market position. No operational claims about it appear in the final document.
- Live2D's interactive/live side is documented via the manual's structure (nizima LIVE as "official tracking app", SDK embedding, AE tracking function) but the live-driver apps themselves were not fetched in depth; live-mode claims are kept qualitative.
- Cartoon Animator evidence combines product pages (Tier 2) with one manual page (Tier 1); deeper manual chapters (bone editor internals, facial rigging) were not fetched. Claims kept to what fetched pages state.
- Spine physics constraints and Live2D physics were observed only at the level of feature presence; no numeric behavior claimed.
- Historical products (Flash bone tool era, early Moho, early puppet tools) were not directly sampled; era-stability of the core is argued structurally (rig + pose + timeline + delivery), not from direct observation of old products.
- Exact numeric limits, format lists per version, and default values were deliberately not documented — fetched evidence does not support that precision.

## Final Synthesis

The dedicated Character Animation Application is a real, market-recognizable Type defined by a minimal core: an articulated character — appearance bound to a control structure — as the central persistent object; rig-driven deformation as the animation method; time-based performance authored by keyframing poses/parameters and/or capturing live performance; and delivery as rendered video and/or runtime animation data. Around this core, mature products converge on a standard structure: a rigging stage (bones/deformers/parameters + binding), keyframe timeline with curve editing, constraints, physics-based secondary motion, performance capture (face/lip/body), motion/pose libraries and templates with cross-character motion transfer, sprite/attachment swapping, and dual delivery (video + engine/app data). Products differentiate along dimension (2D artwork rigs vs 3D mesh rigs), control philosophy (bone skeletons vs named parameters), animation posture (hand-keyframed, physics-assisted, library-first, parameter-first, performance-first), and delivery emphasis (runtime data, video, live). The sibling leaves' flag is confirmed and refined: character animation is simultaneously a capability inside general 2D/3D animation products AND an independent Type whose dedicated products are organized around the character as the only first-class object; the boundary is a gradient, and the discriminating test is whether the character rig (not the scene or the frame) is the application's persistent unit of work.
