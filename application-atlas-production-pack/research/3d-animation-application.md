# Research Notes — 3D Animation Application

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a 3D Animation Application really is from real products: its core objects (scene, objects, transforms, cameras, lights), its animation methods (keyframes/interpolation, rigging, constraints, drivers, simulation), its canonical workflow, its interfaces (viewport, timeline/dope sheet, curve editor, outliner), its rules (keyframe semantics, parenting, preview vs render), and its boundaries against neighboring Types (3D Modeling, Procedural 3D Creation, 3D Rendering, Motion Graphics, 2D Animation, Game Engine, Character Animation, Video Editor).

## Initial Boundary (hypothesis before research)

- What: software that animates 3D content — objects placed in a 3D space whose properties change over time, played back and rendered to moving images.
- Users: 3D animators (film/VFX, games, motion design), technical artists, generalists, indie creators.
- Nearest neighbors: 3D Modeling Application, Digital Sculpting, Procedural 3D Creation Application, 3D Rendering Application, Motion Graphics Application, 2D Animation Application, Game Engine, Character Animation Application, Video Editor.
- Open questions: is modeling definitional? is rigging definitional? is rendering definitional? is the camera definitional? are keyframes definitional or just the dominant method? where exactly is the game-engine boundary? is the sibling leaf Character Animation Application an independent Type?

## Research Questions

1. What are the core objects (scene, object, transform, hierarchy/parenting, camera, light, material, timeline, keyframe, animation curve/track)?
2. Which animation methods are definitional vs variant: keyframe interpolation, rigging/skinning, constraints, drivers/expressions, simulation, motion capture?
3. How is animation data edited (dope sheet/timeline, graph/curve editor, per-property channels)?
4. What is the camera model (camera as scene object, camera animation, cuts between cameras)?
5. What is the rendering model (viewport preview vs final render; built-in vs bundled vs external renderers; is rendering definitional)?
6. Is 3D modeling part of the Type or a bundled capability?
7. How are scenes organized (outliner/hierarchy, parenting, collections/layers)?
8. What interfaces exist (3D viewport, timeline, dope sheet, curve editor, outliner, properties, node editors)?
9. What rules/behaviors matter (keyframe semantics, interpolation types, animation-state indicators, parenting inheritance, rig binding, frame rate/range as scene settings, preview vs render split)?
10. Where are the boundaries against each neighboring Type?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| SideFX Houdini 22 | procedural/node-based 3D; animation + character + VFX in one package | film/VFX studios (artist-to-studio editions) | A (full official help: animation, character, object nodes, rendering — multiple pages) |
| Maxon Cinema 4D 2026 | motion-design-first, approachable full 3D suite | motion designers, freelance → studio | A (official help: Timeline, tracks/keys pages, full doc tree; product page) |
| Blender | free/open-source full 3D creation suite | individuals/small studios → studios | B (official feature pages fetched; manual at docs.blender.org unreachable — 403 ×2) |
| Autodesk Maya | film/VFX/character animation industry standard | enterprise studios | C-degraded (help.autodesk.com SPA empty; autodesk.com 403 ×2 — abandoned per source-access rules) |
| Autodesk 3ds Max | games/archviz 3D | enterprise/prosumer | C-degraded (same Autodesk access failure) |

Maya is retained in the sample because SideFX's own official documentation cross-references it ("Converting animation key values between Houdini and Maya — Houdini stores key tangents using second-based slope and acceleration, while Maya uses frame-based angle and weight"), which is direct official evidence that Maya is a peer keyframe-animation product with key/tangent concepts. No internal Maya/3ds Max operational claims are made anywhere in this research.

## Sources

Fetched 2026-09-06:

- Houdini 22.0 help root: https://www.sidefx.com/docs/houdini/
- Houdini — Animation section: https://www.sidefx.com/docs/houdini/anim/index.html
- Houdini — Animation basics (keyframes, channel list, parameter color states): https://www.sidefx.com/docs/houdini/anim/basics.html
- Houdini — Animation styles (pose-to-pose blocking/posing, straight-ahead): https://www.sidefx.com/docs/houdini/anim/anim_styles.html
- Houdini — Playbar (playback, frame ranges, key markers, keyframing controls, auto-key/auto-commit): https://www.sidefx.com/docs/houdini/anim/playbar.html
- Houdini — Flipbook previews and blocking: https://www.sidefx.com/docs/houdini/anim/flipbook.html
- Houdini — Animate cameras and lights (keyframing, switcher camera cuts): https://www.sidefx.com/docs/houdini/anim/anim_camera.html
- Houdini — Character (KineFX procedural rigging, retargeting, pose library): https://www.sidefx.com/docs/houdini/character/index.html
- Houdini — Object nodes (/obj/ scene level, object types, parenting): https://www.sidefx.com/docs/houdini/nodes/obj/index.html
- Houdini — Mantra rendering (render nodes, render region, cameras, motion blur): https://www.sidefx.com/docs/houdini/render/index.html
- Cinema 4D — product page: https://www.maxon.net/en/cinema-4d
- Cinema 4D — Timeline (Dope Sheet) page: https://help.maxon.net/c4d/en-us/Content/html/10596.html
- Cinema 4D — Various Methods of Creating Tracks and Keys: https://help.maxon.net/c4d/en-us/Content/html/10592.html
- Cinema 4D — documentation tree (fetched via 33010.html index): Object Manager, Attribute Manager, Coordinate Manager, Material Manager, Tags (Animation/Rigging/Camera/MoGraph/Simulation/Render), Views and Viewports/Cameras, Scene settings, Timeline/Function Graph preferences, Import/Export (FBX/Alembic/USD/glTF/OBJ with Animation groups), Set Driven Keys
- Blender — Features page: https://www.blender.org/features/
- Blender — Animation & Rigging feature page: https://www.blender.org/features/animation/
- Attempted and abandoned: https://docs.blender.org/manual/... (403 ×2), https://help.autodesk.com/view/MAYAUL/2025/ENU/ (SPA, empty), https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/index.html (404), https://www.autodesk.com/products/maya/overview (403), https://www.autodesk.com/products/3ds-max/overview (403), https://help.maxon.net/c4d/2025/en-us/ (SPA shell; direct Content/html URLs work), https://web.archive.org/web/2025/https://docs.blender.org/... (timeout ×2), https://docs.lightwave3d.com/ (JS frameset, empty)

## Product Observations

### SideFX Houdini 22 (evidence layer A unless noted)

- Animation section exists as a first-class part of the product help: "How to create and keyframe animation in Houdini."
- Animation basics: "Keyframes define the start and end points of an animation sequence. You can add keyframes to specific parameters of an object to control the behavior of an animation. You can also specify the functions for Houdini to use to determine the behavior between keyframes." Keyframing happens on *parameters* of objects; selecting an object auto-populates a *channel list* with commonly animated parameters; keys are set on parameters in the channel list (K key / playbar button / menu).
- Parameter animation-state color coding: no tint = not animated; green = keyed at current frame; yellow = pending changes (changed but not keyed; must explicitly key if auto-commit off); blue = animated, between keyframes; gray-blue = muted from dopesheet; orange = overridden by CHOPs; dark green = empty channel.
- Animation editor (graph) shows/edits animation curves for keyframed parameters; channel list selects which parameters appear in the editor and on the timeline.
- Playbar: playback controls (first/backward/stop/forward/last, prev/next frame), current frame field, global vs current frame ranges (range slider plays a subset of the global range), loop modes (loop/play once/zig-zag/forever), real-time toggle (plays at set FPS vs as fast as possible), fractional-frame (substep) playback, audio panel, previous/next keyframe navigation, keyframe markers color-coded on the timeline, direct key editing on the timeline (move/scale/copy/paste/cycle/stretch keys, ripple tool), bookmarks (named frame ranges), keyframing controls (Global Set Key: key pending / key all channels / key selected), auto-key ("any parameter change is immediately keyed") and auto-commit preferences, simulation-cache and animation-cache display on the timeline.
- Animation styles: pose-to-pose ("keying the important poses where they occur in time, and then filling in the animation between these key poses. This is the common method for doing 3D computer-based animation") with two phases — blocking (key everything, constant/linear transitions, flipbook blocking to retime) and posing (clean up, convert transitions to ease/constant/spline, key finer controls); straight-ahead ("posing the character for every second ('on 2s'), third ('on 3s'), or fourth ('on 4s') frame... similar to how one animates in traditional 2D cel animation... considered fairly advanced; few CG animators work this way"). The page explicitly ties the pose-to-pose tradition to 1960s master-animator cel practice.
- Flipbook: "captures an image of the viewport at each frame and then plays the images as an animation. This is much faster than actually rendering the animation." Flipbook blocking: block a shot, drag keyframe ranges in the MPlay viewer, export blocking back to the scene.
- Cameras and lights: keyframable objects like any other (position with handles, K to key); cuts between cameras via a Switcher camera object whose "Switch camera" parameter can be keyed or expression-driven; render node's camera set to the switcher.
- Character: KineFX geometry-level procedural rigging (SOP-based rigs), animation, animation retargeting; object-level bone rigs deprecated; panes: rig tree view, character picker, pose library; APEX graphs for rigs.
- Object level (/obj/): "contains the 'top-level' objects of your scene (geometry objects, skeletons, lights, cameras) and lets you set up the spatial and hierarchical relationships between them... where you position the characters, props, cameras, and lights in a scene." Wiring object nodes together creates hierarchical ("parenting") relationships. Object types include: Geometry (SOP container), Camera ("You can view your scene through a camera, and render from its point of view"), lights (ambient/environment/indirect), Bone, Null ("place-holder... usually for parenting"), Fetch ("gets its transform by copying the transform of another object"), Blend ("switches or blends between the transformations of several input objects"), Sticky/Rivet (attach to surface), Instance, mocap imports (Acclaim/biped), DOP Network (simulation container), stereo/VR cameras, Switcher.
- Rendering: Mantra "How to render images and animation with the Mantra engine"; render nodes "render the scene or set up render dependency networks"; render region tool (drag a box in the viewer for an auto-updating preview); setting up cameras for rendering; motion blur; expressions in output filenames for numbered sequences; flipbook listed under rendering basics as the fast preview; HQueue distributed scheduling; Solaris/USD (LOP) scene building and Karma rendering as the newer layer.
- Reading: Houdini = full 3D animation world (scene of transformable objects + parameter keyframing + curve editing + playback + cameras/lights + rendering) with a procedural node-graph architecture on top; animation concepts are conventional even though the architecture is node-based.

### Maxon Cinema 4D 2026 (evidence layer A unless noted)

- Product page (Tier 2): "Model, animate, simulate, and render with a powerful tool"; FAQ: "Cinema 4D is a professional 3D animation and modeling software... combines modeling, animation, simulation, and rendering in a single application." Feature groups: Modeling, Animation, MoGraph, Simulation, Rendering (Redshift included). Animation features: "Build precise keyframe animations, speed up character rigging with ready-made templates, and control procedural motion with Cinema 4D's parametric animation tools. Add motion tracking, leverage motion capture data, and refine every detail with a professional timeline built for fast, flexible creative control."
- Timeline page (help): "The Timeline is a powerful tool with which you can control, edit and play your animations... The key element to all animations is the key frame (key). Keys contain movement (and other) information pertaining to an object at that particular time in the animation. Most animations will require the setting of at least two keys. The change in an object's property's values will be interpolated between these two keys (i.e. a rotation from 0° in key 1 to 90° in key 50). The movement can then be seen once the animation is played."
- Tracks: "each track represents the temporal change of one object property. This can range from a simple change in position to a change in the Phong rotation... Each track contains the corresponding keys, of which an unlimited number can be created." Each track has its own F-Curve controlling interpolation between keys; mini F-curves inline, full editing in F-Curve mode. Timeline modes: Dope Sheet, F-Curve, Motion (Tab switches). Spacebar plays when Timeline active. Layer system + filters + object locking for focusing animation work.
- Creating tracks and keys (help): Record button (Animation Palette) "records the current properties for all selected objects at that time in the animation and creates corresponding tracks and keys automatically"; Autokeying mode ("A" button) records all edited object properties automatically (warning: forgetting to disable it can overwrite the animation); every animatable property in the Attribute Manager has a keyframe circle button (solid red = key at current time; empty red = track but no key; yellow = temporary value that will be ignored once you move frames — interpolated/key values are used); manual track creation via Timeline's Create/Add Property Tracks menu.
- Documentation tree (Tier 1 structure): Object Manager (scene hierarchy with tags, layers, bookmarks), Attribute Manager (per-object properties incl. modeling/viewport settings), Coordinate Manager, Material Manager (materials/shaders), Views and Viewports (View, Cameras, Display, HUD, Redshift viewport rendering), Configuration → Scene (document settings incl. OCIO color management), Preferences (Play, Timeline/Function Graph, Renderer), Tags system: Animation Tags (align to path/spline, motions, track modifier, vibrate, field driver), Rigging Tags (Constraint with Parent/Transform/Aim/Spring/Up-Vector groups, IK, IK-Spline, Weight, Pose Morph, Delta Mush, Retarget Expression, Character Component, Visual Selector, Point Cache, Protection), Camera Tags (Motion Camera with splines/dynamics/footsteps/dolly-zoom, Camera Morph with morph tracks, Camera Crane, Look at Camera), MoGraph Tags (cache/selection/weightmap), Simulation Tags, Dynamics Body Tag (rigid body: mass/collision/forces/springs/cache), Render Tags (compositing, motion blur), Tracker Tags (Camera Calibrator), Programming Tags (XPresso, Python, User Data); Set Driven Keys page; Import/Export filters (FBX, Alembic, USD, glTF, OBJ, BVH — each with an Animation group); Takes system (override filters); Cineware (After Effects exchange); Moves by Maxon (mocap capture).
- Reading: C4D = object-hierarchy scene (Object Manager) + per-property tracks/keys/F-curves (Timeline in Dope Sheet/F-Curve modes) + record/autokey + cameras/lights/materials + rigging/simulation/MoGraph + Redshift rendering; motion-design emphasis (MoGraph procedural cloners/effectors/fields) layered on the same animation core.

### Blender (evidence layer B — official feature pages; manual unreachable)

- Features page: "Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game asset creation." Feature sections: Modeling, Sculpting, Animation & Rigging, Story Artist, Rendering (Cycles path tracer), Simulation, Video Editing, Scripting (Python API), VFX, Interface, Pipeline (glTF/USD/Alembic formats shown).
- Animation & Rigging page: "Whether it's simple keyframing or complex walk-cycles, Blender allows artists to turn their still characters into impressive animations." Animation toolset: character animation pose editor, Non Linear Animation (NLA) "for independent movements", forward/inverse kinematics "for fast poses", sound synchronization. Rigging: envelope/skeleton/automatic skinning, weight painting, mirror, bone layers/colored groups, B-spline interpolated bones. Constraints: "a way to control an object's properties (e.g. its location, rotation, scale), using either plain static values... or another object, called 'target'"; animating constraint targets indirectly animates the owner; constraint settings (e.g. Influence) are themselves animatable. Drivers: "control values of properties by means of a function, mathematical expression or small script", composed of a driver configuration + an animation F-Curve mapping the output to the driven property. Shape keys: "used to deform objects into new shapes for animation... may be called 'morph targets' or 'blend shapes'"; facial animation and rig refinement. Motion Paths: "visualize the motion of points as paths over a series of frames" (object origins and bone joints).
- Story Artist page title/description: "Push the boundaries of Story Art... by drawing in a 3D environment" (Grease Pencil tradition).
- Reading: Blender = same animation core (keyframes, F-curves, constraints, drivers, shape keys, rigging, NLA layers) inside a free full-pipeline suite; official manual (operational detail) could not be fetched, so no operational specifics are claimed.

### Autodesk Maya / 3ds Max (evidence layer C — degraded)

- Official documentation could not be fetched (help.autodesk.com renders empty SPA shell; autodesk.com returns 403; cloudhelp path 404). Per source-access rules, no operational claims are made from memory.
- Retained as market references: Maya (film/VFX character-animation standard) and 3ds Max (games/archviz). Direct official cross-evidence: Houdini's own docs document key-tangent conversion between Houdini and Maya, confirming Maya operates on the same key/tangent animation model. All Type-level findings below are supported by Houdini + Cinema 4D + Blender.

## Cross-product Comparison

| Dimension | Houdini 22 | Cinema 4D 2026 | Blender | Maya / 3ds Max |
|---|---|---|---|---|
| Scene = objects in 3D space | /obj/ object level: geometry, skeletons, lights, cameras; spatial + hierarchical relationships | Object Manager hierarchy of objects (+ tags, layers) | scenes/objects (feature pages; manual n/a) | (not directly verified) |
| Animatable unit | parameters (channels) of objects/nodes | object properties → tracks | properties (F-curves, drivers) | keyframes on attributes (per Houdini cross-ref) |
| Keyframe + interpolation | keys on parameters; behavior between keys set by functions; curve editor | keys on tracks; F-Curve per track controls interpolation | F-curves; drivers map expressions to properties | key tangents (per Houdini cross-ref) |
| Auto-key | auto-key preference (immediate key on change) + auto-commit + pending state | Record button + Autokeying mode + temporary-value (yellow) state | (not verified in fetched pages) | (not verified) |
| Animation-state indicators | parameter background colors (keyed/pending/between/muted/overridden) | keyframe button colors (red solid/empty, yellow temporary) | (not verified) | (not verified) |
| Time editing surfaces | playbar timeline + dopesheet + animation editor (graph) + channel list | Timeline (Dope Sheet / F-Curve / Motion modes) | timeline/graph editor (manual n/a; F-curves confirmed) | (not verified) |
| Playback | playbar: loop modes, real-time toggle, substeps, frame ranges, audio | Spacebar play; Play preferences | (not verified) | (not verified) |
| Preview vs render | flipbook (viewport capture, "much faster than actually rendering") vs Mantra/Karma render; render region | viewport + Redshift IPR vs final render | viewport vs Cycles render | (not verified) |
| Camera | camera object; render from its POV; switcher camera for cuts (keyed parameter) | camera objects; Motion Camera/Camera Morph/Crane tags; camera calibrator | camera objects (pipeline pages) | (not verified) |
| Lights/materials | light objects (ambient/environment/indirect); materials/shaders | light objects; Material Manager; render tags | materials + Cycles | (not verified) |
| Rigging/characters | KineFX procedural rigs, retargeting, pose library, APEX; bones/nulls/handles | rigging tags: IK, IK-Spline, Weight, Pose Morph, Constraint, Delta Mush, Character Component | armatures, skinning, weight painting, FK/IK, B-spline bones | (market position only) |
| Constraints/indirect animation | Fetch (copy transform), Blend (blend transforms), Sticky/Rivet (surface attach), parenting | Constraint tag (Parent/Transform/Aim/Spring/Up-Vector) | constraints with targets; animatable Influence | (not verified) |
| Drivers/expressions | parameter expressions (Hscript/Python), CHOPs override | XPresso nodes, Python tags, User Data, Set Driven Keys, Field Driver | drivers (expression/script + F-curve) | (not verified) |
| Simulation as motion source | DOP networks (pyro, Vellum, fluids, grains, particles...); sim cache on playbar | Simulation tags + unified simulation; dynamics body tags with cache; MoGraph cache | simulation feature section (Bullet/MantaFlow per features page) | (not verified) |
| Mocap | mocap object imports (Acclaim/bipeds); retargeting | BVH import; Moves by Maxon capture | (not verified) | (not verified) |
| Non-linear/clip layers | animation layers pane; takes | Motion clips / Motions tags; Takes system | NLA | (not verified) |
| Shape/morph animation | (blend shapes via rigs; not confirmed in fetched pages) | Pose Morph tag; Alembic Morph tag | shape keys (morph targets/blend shapes) | (not verified) |
| Interchange with animation | FBX/Alembic/USD/glTF export groups incl. animation | FBX/Alembic/USD/glTF/OBJ/BVH import-export with Animation groups | glTF/USD/Alembic pipeline page | (not verified) |
| Render/delivery | render nodes → images/animation; HQueue farm | Redshift renderer included; Team Render nodes | Cycles renderer; video editor for finishing | (not verified) |
| Architecture | node-graph procedural (networks) on top of object scene | object hierarchy + tags + layer stack | object mode + modifier stack + editors | (not verified) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A 3D Animation Application is recognizable when all of the following hold:

1. **3D scene of positioned objects** — content exists as objects (at minimum geometry; in practice also cameras and lights) placed in a shared three-dimensional space, each carrying a transform (position/rotation/scale) and organized in hierarchies.
2. **User-authored change over time** — the user defines how object properties (at minimum the transforms) change across a frame-based timeline, by pinning values at frames (keyframes) with computed in-between values (interpolation), or by equivalent time-varying definitions (expressions, simulation, constraints driven over time).
3. **Playback** — the animated scene can be played back and scrubbed in a 3D viewport against the timeline.
4. **Delivery as rendered moving image** — the scene can be rendered from a defined viewpoint (virtual camera) across the frame range into an image sequence or video.

Remove the 3D scene → 2D animation or compositing. Remove time → 3D modeling/rendering. Remove playback → a batch scene-description pipeline, not an animator's application. Remove rendered moving image delivery → a real-time interactive runtime (game engine) or a modeling tool. The core is architecture-agnostic (layer stacks or node graphs), method-agnostic (keyframes, rigs, simulation, expressions all satisfy #2), and era-stable (the key/track/interpolation model is documented identically in a 2026 motion-design suite and a procedural VFX package, and cross-referenced to a 1990s-lineage peer).

### L1 — Common Mature Structure

Present across the researched sample; not required for recognition:

- 3D viewport as the central working surface (navigation, selection, transform gizmos/handles, display modes)
- scene hierarchy/outliner with parenting (transform inheritance)
- per-object property inspection (attribute/parameter panels) — the properties that get keyed
- dope-sheet/timeline view of keys per object/property track; curve/graph editor for interpolation (F-curves)
- auto-key (record) modes and visible animation-state indicators on properties (keyed / pending / between keys)
- camera as a manipulable scene object; render from camera; camera animation; cuts/blends between cameras
- lights and materials/shading as scene content
- character rigging (bones/joints, IK/FK, skinning/weights) and pose libraries
- constraints (drive properties from target objects) and drivers/expressions (compute properties from functions/scripts)
- shape keys / morph targets / pose morphs
- simulation (rigid body, cloth, particles, fluids, hair) as a motion source, usually cached/baked
- motion capture import and retargeting
- non-linear animation layers / clips / takes
- sound track and sync support
- motion-path visualization
- preview vs final render split (viewport/flipbook/IPR vs full render) and render settings/output (frame range, format, sequences)
- asset libraries/presets; scripting; interchange formats carrying animation (FBX/Alembic/USD/glTF)
- modeling/sculpting/texturing tools bundled in the same application (suite pattern)

### L2 — Variant / Optional Structure

- market focus: film/VFX character animation, motion design/broadcast, games/archviz asset animation, procedural VFX
- architecture: object hierarchy + tags/stack (C4D, Blender) vs node-graph procedural (Houdini)
- render engine posture: built-in engine, bundled GPU engine (Redshift with C4D), third-party engines, network farms
- procedural motion systems for motion design (cloners/effectors/fields pattern)
- real-time/interactive delivery vs linear rendered delivery (game-engine boundary; game-asset export as an output)
- 2D integration depth (drawing in 3D space; vector import; toon/npr render styles)
- team/pipeline infrastructure: USD scene building, render farms, versioning, take/variant management
- mocap capture hardware integration vs import-only
- licensing: subscription suites, perpetual, free/open source, learning editions

### L3 — Vendor-specific (research notes only)

- Houdini: CHOPs (channel nodes overriding parameters), KineFX/APEX rig graphs, Solaris/LOP USD layer, Karma/Mantra, MPlay viewer, HQueue, PDG/TOPs, digital assets (HDA), flipbook blocking export, second-based key tangents.
- Cinema 4D: MoGraph (Cloners, Effectors, Fields), Takes system, Cineware (After Effects live link), XPresso, Pose Morph/Delta Mush/Character Component tags, Motion Camera/Camera Morph/Camera Crane tags, Moves by Maxon, Team Render, Capsules, Redshift bundle.
- Blender: NLA (Non Linear Animation), Grease Pencil (drawing in 3D), drivers, shape keys terminology, Cycles, asset browser/extensions.
- Maya/3ds Max: not documented here (sources unreachable).

## Rejected Findings (not promoted to core)

- "Modeling tools define the Type" — rejected: modeling is a bundled capability in all sampled suites, but the defining center is time-varying scene state; modeling products (separate leaf) have no time axis. Modeling = L1 bundled capability.
- "Rigging defines the Type" — rejected: rigging serves character work; camera moves, motion design, and simulated shots need no rig. L1.
- "Simulation defines the Type" — rejected: simulation is one motion source among several; heavily product-dependent. L1/L2.
- "Node graphs define the Type" — rejected: only part of the sample is node-based; others use hierarchies/stacks. L2.
- "Built-in renderer defines the Type" — rejected: what is definitional is rendered moving-image delivery; the engine can be built-in, bundled, or external. L2 posture.
- "Real-time playback = game engine" — rejected: viewport playback is preview inside an authoring loop whose delivery is linear; game engines center on the interactive runtime itself.
- "Auto-key is definitional" — rejected: it is a workflow convenience (though universally present in the sample); keyframing works without it. L1.

## Boundary Findings

- **vs 3D Modeling Application**: modeling centers on creating/editing static geometry; animation centers on time-varying scene state. Test: remove the time axis → modeling; remove geometry authoring (import models, animate them) → still animation. Suites bundle both, which is why the leaves are adjacent; the center of gravity differs.
- **vs Procedural 3D Creation Application**: gradient, not wall. Houdini is the canonical procedural product and also a full animation application; its animation section is conventional (keys/tracks/curves/playback). The procedural leaf centers on node-network content generation; this leaf centers on time-varying scene state. Flagged for joint review when Procedural 3D Creation Application is processed.
- **vs 3D Rendering Application**: rendering-only products take prepared scenes and produce images; no time authoring. Test: remove keyframes/timeline → rendering application. Render management (farms) is a further separate leaf.
- **vs Game Engine / Game Development Platform**: game engines center on a real-time interactive runtime (logic, input, gameplay); 3D animation centers on linear rendered output. Overlap: real-time viewports, game-asset export (Blender "game asset creation", C4D↔Unreal/Cineware). Test: remove interactivity/runtime → animation; remove linear delivery → engine.
- **vs Motion Graphics Application**: MG centers on 2D graphic/typographic layer animation; 3D animation centers on volumetric scenes. C4D blurs the line (MoGraph is 3D motion design inside a 3D animation suite). Flagged for joint review when Motion Graphics Application is processed.
- **vs 2D Animation Application**: planar frame content vs 3D space; Grease Pencil-style "drawing in a 3D environment" and 2D-depth features blur the edge (see research/2d-animation-application.md §Boundary Findings for the mirror-image finding).
- **vs Character Animation Application (sibling leaf 04.08)**: in the researched sample, character rigging/animation is a capability inside general 3D animation products (Blender rigging section, C4D rigging tags, Houdini character section) — probable Variant/Capability rather than independent Type; flagged for joint review; no taxonomy change made unilaterally.
- **vs Video Editor**: video editors sequence captured media clips; 3D animation authors the content itself and renders to video that editors consume. 3D animation products may bundle editing (Blender VSE) but that is a bundled capability, not the core.

## Uncertainties

- Maya and 3ds Max official documentation was unreachable (SPA/403); their inclusion rests on market position plus SideFX's official cross-reference to Maya's key/tangent model. No internal claims about either product appear in the final document.
- Blender's official manual (docs.blender.org) was unreachable (403 ×2; archive.org timeout ×2); Blender evidence is limited to official feature pages (positioning + capability lists). Operational specifics (defaults, exact editor behaviors) are not claimed.
- Exact defaults (frame rates, default interpolation, numeric limits) were deliberately not documented — fetched evidence does not support that precision.
- Historical products (1990s-era packages) were not directly sampled; era-stability of the core model is inferred from the C4D/Houdini documentation (both describe the identical key/track/interpolation model today) and the Houdini↔Maya conversion page, not from direct observation of old products.
- Synfig-style parametric-first animation or game-engine-native animation workflows were not sampled; the sample is desktop DCC-centric, which matches the professional market for this leaf.

## Final Synthesis

The 3D Animation Application is defined by a minimal core: a 3D scene of positioned, transformable objects; user-authored change of object properties over a frame-based timeline (keyframes + interpolation, or equivalent time-varying definitions); playback in a 3D viewport; and delivery as a rendered moving image from a virtual camera. Around this core, mature products converge on a standard structure: viewport + outliner + property inspector + dope sheet + curve editor; auto-key with visible animation-state indicators; cameras, lights, and materials as scene content; rigging, constraints, drivers, shape keys, simulation, and mocap as motion sources; non-linear clip layers; sound sync; a strict preview-vs-final-render split; and animation-carrying interchange formats. Products differentiate by market focus (film/VFX, motion design, games), architecture (hierarchy+stack vs node-graph procedural), render engine posture, procedural motion systems, and pipeline infrastructure. The boundaries are clear against 3D modeling (no time axis), 3D rendering (no time authoring), game engines (interactive runtime vs linear delivery), video editing (captured vs authored content), and 2D animation (planar vs volumetric); the gradients worth joint review are Procedural 3D Creation (Houdini's other identity), Motion Graphics (C4D's MoGraph), and the sibling Character Animation Application (a capability inside every sampled product).
