# Research Notes — 2D Animation Application

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a 2D Animation Application really is from real products: its core objects, its animation methods (frame-by-frame drawing vs keyframe/tween vs rigged cut-out), its canonical workflow, its interfaces, its rules, and its boundaries against neighboring Types (Motion Graphics, Video Editor, 3D Animation, Stop-motion, Digital Painting, Storyboarding).

## Initial Boundary (hypothesis before research)

- What: software that makes 2D artwork move over time using a frame-based timeline.
- Users: animators (indie → studio), motion designers, game artists, educators, hobbyists.
- Nearest neighbors: Motion Graphics Application, Video Editor, 3D Animation Application, Stop-motion Animation Application, Character Animation Application, Digital Painting Application, Storyboard Application.
- Open questions: is rigging definitional? is vector vs bitmap definitional? is tweening definitional? xsheet vs timeline? camera model? export targets?

## Research Questions

1. What are the core objects (scene/project, timeline/xsheet, layer/column, frame, drawing/cel/level, keyframe, rig/bone, camera)?
2. How do the three animation methods relate — frame-by-frame drawing, keyframe interpolation (tweening), rigged cut-out? Which are definitional, which are variants?
3. What is the exposure/hold model (how a drawing persists across frames without redrawing)?
4. How does playback work (onion skin, flip, real-time preview) and how does preview differ from final render?
5. What drawing substrate(s) do products use (bitmap, vector, hybrid)?
6. What is the rigging model where present (bones, deformers, IK, meshes, pegbars)?
7. What is the camera model (2D camera moves, multiplane/depth, multiple cameras)?
8. What are the export/render targets (video, image sequence, sprite/game output)?
9. What interfaces exist (canvas/camera view, timeline/xsheet, level strip, node/schematic view, function editor, library)?
10. What rules/behaviors matter (frame rate as scene setting, stacking order, keyframe semantics, preview vs render)?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| Toon Boom Harmony | all-in-one studio pipeline: hand-drawn + cut-out rigs + compositing | enterprise studios (editions Essentials/Advanced/Premium) | A (product page, release notes, docs index); deep user-guide pages unreachable |
| TVPaint Animation | bitmap hand-drawn tradition, reproduces paper workflow | professional boutique studios, schools | A (product page + full user manual, multiple pages) |
| OpenToonz | open-source traditional production pipeline (Toonz lineage), scan-based + paperless + cutout | studios/indie, free | A (full user manual, multiple pages) |
| Synfig Studio | tween-first: "eliminates the need to create animation frame-by-frame" | indie/free, open source | A (product page + user manual, multiple pages) |
| Adobe Animate | Flash lineage; vector + timeline tween; web/interactive export | broad prosumer/pro | C-degraded (helpx.adobe.com and adobe.com unreachable after 3 attempts) |

Moho (bones-first mid-market) was originally sampled but its official sites (moho.space, smithmicro.com) were unreachable (transport error ×2, 404); it was replaced by Synfig for rig-first coverage and is retained only as an unverified market reference.

## Sources

Fetched 2026-09-06:

- Toon Boom — Harmony product page: https://www.toonboom.com/products/harmony
- Toon Boom — Help Centre root: https://helpcentre.toonboom.com/hc/en-ca
- Toon Boom — Harmony 27 Premium docs index: https://docs.toonboom.com/help/harmony-27/premium/book/index.html
- Toon Boom — Harmony 27 release notes: https://docs.toonboom.com/help/harmony-27/premium/release-notes/harmony/harmony-27-release-notes.html
- Toon Boom — User Guide splash: https://docs.toonboom.com/help/harmony-27/premium/book/about-user-guide.html ; Reference splash: .../reference/about-reference.html ; Getting Started: .../getting-started/introduction.html
- TVPaint — product page: https://www.tvpaint.com/
- TVPaint — User Manual: https://doc.tvpaint.com/docs/doc-introduction ; animation-first-steps/introduction ; animation-first-steps/instances/instance-concept ; animation-advanced-functions/light-table/light-table-overview ; timesheet/timesheet-overview
- OpenToonz — User Manual index: https://opentoonz.readthedocs.io/en/latest/
- OpenToonz — Working in Xsheet/Timeline: https://opentoonz.readthedocs.io/en/latest/working_in_xsheet.html
- OpenToonz — Creating Movements: https://opentoonz.readthedocs.io/en/latest/creating_movements.html
- Synfig — product page: https://www.synfig.org/
- Synfig — User Manual index: https://synfig.readthedocs.io/en/latest/index.html ; main_concepts ; main_concepts/animation_mode
- Adobe — attempted: https://helpx.adobe.com/animate/get-started.html (timeout ×1), https://helpx.adobe.com/animate/user-guide.html (timeout ×1), https://www.adobe.com/products/animate.html (timeout ×1) — abandoned per source-access rules.

## Product Observations

### Toon Boom Harmony (evidence layer A unless noted)

- Positioning: "all-in-one animation solution"; studios collaborate "using the same programs and project files, from drawing roughs to rigging characters and compositing. Whether you work with hand drawn animation or character rigs…" (product page).
- Editions ladder maps to workflow depth: Essentials = "fundamental drawing, painting, and animation tools"; Advanced = "full traditional, paperless style animation… features for simple cut-out style animation"; Premium = "sophisticated cut-out rigs, very natural and realistic character movement plus unlimited special effects" (product page).
- Structure visible in release notes/docs: Node view (compositing/rig graph with nodes: composites, effects, controllers, selection lock), Timeline view (keyframes, collapsed groups), Xsheet (3D animation exposed in Xsheet mentioned), Camera view (selection, posing, OGL preview), Drawing views (multiple, with art layers, snapping across drawing layers), Reference view (mirror/flip).
- Rigging: "rigs", "Master Controllers" (store keyframe data to pose rigs), new "Attribute Controllers" (add offsets non-destructively, four interpolator types, Setup Mode training, can be trained from existing timeline keyframes), "bone deformer" (fix list), cut-in textures/gradients in complex rigs.
- Animation: keyframes on timeline; "Stop Motion Keyframe Mode"; baking animation ("Bake to Subnode Override"); 3D subnode overrides; USD/ATOM export; camera with scene FOV override.
- Effects/compositing: effect nodes (Blur-Radial-Zoom, Lens Flare), Pass Through composite, Colour-Override, particles ("Particle effects"), premultiply/transparency types, 16/32-bit rendering, colour space (working colour space, sRGB), ProRes export via scripting, Render Write Nodes (movie export).
- Library/templates: "template imports", Library view with templates, Master Controllers in templates.
- Drawing: textured eraser, pencil lines, "Preserve Line Thickness", snapping on drawing layers.
- Reading: Harmony = pipeline product spanning drawing → rigging → animation → effects → render, with a node-graph compositing layer on top of a timeline/xsheet animation core.

### TVPaint Animation (evidence layer A)

- Positioning: "2D animation software based on bitmap technology… aims to reproduce the traditional, paper-based, drawing experience with the utmost accuracy" (product page). FAQ explains bitmap vs vector trade-offs (bitmap = closer to traditional drawing; vector = transform without quality loss).
- Editions: Standard (modular interface, layer folders, custom brushes, dual papers, light table with Out of Pegs, scan cleaner, essential FX); Professional adds TVPaint Converter, storyboarding tools, 2D Camera, Bitmap Rigging (Puppet Layers), Smart Colorization (CTG Layers), Image Library, complete FX (product page).
- Core animation model (manual): "create your own virtual film rolls and project them onto your Canvas… we refer to this roll as: Animation layers, and these images (the drawings you will create), we will name them Images and Instances."
- Traditional workflow taught in manual: draw key images → identify/draw most important frames → draw inbetweens → add more inbetweens until smooth; "In TVPaint, you will need to create subdivisions on a layer to draw inbetweens and adjust the timing."
- Instance model (manual): "An Instance can be thought as a container for an image in an Animation Layer." Instance = Head Cell + Exposure Cells (duplicates of the head's content). Extending duration = adding Exposure Cells; handles adjust exposure count; Auto Break Instance splits an instance when an exposure is edited. Editing a Head affects its exposures; editing an exposure either splits (auto-break on) or propagates to head (auto-break off).
- Light Table (manual): toned-down display of preceding/following images for inbetweening; per-frame on/off; previous frames green / following orange by default (configurable color/gradient/image-color); opacity falloff by distance; modes: Instance/Frame/Bookmark/Rig Key/Image Mark; Out-of-Pegs feature (off-registration drawing).
- Timesheet (manual): digital exposure sheet panel; Japanese layout (columns: Image number, Action, Audio, Dialogues/Notes, Cell, Camera — genga/douga roles) vs Occidental layout (Layers column instead of Action/Cell); Page View (72 images/page) vs Scroll View; camera keys column (Position, Rotation, Zoom, Movement Type); audio waveform column; memo panel for scene metadata.
- Other: FX Stack (per-layer effect stack), Keyframer (advanced tool), Puppet Layer (bitmap rigging), 2D Camera, sound tracks, storyboarding tools, George scripting, project templates, import/export.
- Reading: TVPaint = frame-by-frame cel tradition digitalized; timing via instances/exposures; rigging exists but as an optional Professional feature (Puppet Layers), not the core.

### OpenToonz (evidence layer A)

- Positioning: "open-source full-featured 2D animation creation software"; manual derived from Toonz Harlequin 7.1 (Digital Video S.p.A.) — long production lineage.
- Production workflows (manual): "Traditional Workflow" (scan paper drawings → cleanup → paint) and "Paperless Workflow" (draw digitally).
- Scene = container with settings: frame rate, camera settings (size/resolution), working units, color calibration LUTs, undo memory.
- Levels: "animation levels" (Toonz Vector PLI, Toonz Raster TLV), raster images/sequences, video clips, PSD (as single image / frames / columns), audio, palettes; other scenes load as Sub-Xsheets (nesting).
- Xsheet/Timeline (manual): "The Xsheet, the digital version of the traditional exposure sheet… organized in columns and rows: each column contains a layer of the animation and each row represents a frame contents. Columns are divided into cells, representing the content of that column in a particular frame." Timeline = horizontal counterpart, same functionality. Levels are "exposed" into columns from the Scene Cast; Level Strip shows the sequence of drawings inside a level; cells reference drawings; replacing levels preserves edited sequences.
- Movement (manual): "Each scene has a series of objects that can be transformed; they can be Xsheet columns (or Timeline layers), pegbars, cameras, or the table. Every transformation you set for an object at a specific frame automatically defines a keyframe. When keyframes are defined at several frames, in-between positions are automatically interpolated."
- Stage Schematic: node hierarchy (table → pegbars → columns; cameras), linking for shared/relative movement, hooks (per-level reference points, e.g. foot tracking to avoid moon-walking), Tracker (auto-generates hooks from image regions), motion paths (drawn vector paths, % parameterization, optional auto-orientation).
- Animate tool: position/rotation/scale/shear/center (+Z depth for 3D environment; SO stacking order animatable); Global Key option (key all transformations at once); Set Key; keys visible as icons in Xsheet with ease in/out arrows; cycling keys; Function Editor for curves/interpolation.
- Cutout animation: Skeleton tool (build skeleton, IK, models with hooks), Plastic tool (mesh + skeleton deformation, rigidity, multiple skeletons).
- FX: FX Schematic (node graph), effects list, macro FX, particles effect.
- Preview/Render: preview mode renders as final; flipbook; rendering to movie/image sequence; Toonz Farm (network render farm); version control; ToonzScript.
- Reading: OpenToonz = the traditional studio pipeline made explicit: scene → levels → xsheet exposure → object animation with keys → cutout optional → FX → render (incl. farm).

### Synfig Studio (evidence layer A)

- Positioning: "free and open-source 2D animation software… using a vector and bitmap artwork. It eliminates the need to create animation frame-by frame, allowing you to produce 2D animation of a higher quality with fewer people and resources" (product page).
- Features (product page): Vector tweening ("Just set the key positions and inbetween frames will be calculated automatically"); 50+ layer types (geometric, gradients, filters, distortions, transformations, fractals); Bones ("Full-featured bone system allows to create cutout animation using bitmap images or control your vector artwork. Use additional Skeleton Distortion layer…"); Advanced controls (link parameters directly or through mathematical expressions; "create advanced character puppets").
- Manual concepts: Animation Mode (canvas-level toggle). ON: "each time you edit a parameter… a Waypoint is created to remember the change, and the position on the Timetrack… you are creating an animation." OFF: "changes to a parameter will be applied throughout the entire timeline"; editing a parameter that already has waypoints triggers a warning offering to apply an offset instead.
- Keyframes vs Waypoints: Keyframes = global time markers on the timetrack; Waypoints = per-parameter value markers with interpolation; Lock Keyframes setting can propagate waypoints to neighboring keyframes.
- ValueNode system: parameters are nodes that can be linked, converted (converters), exported (exported parameters), reused across layers; exported canvases (nested compositions); static parameters.
- Interface: Toolbox, Canvas window, Timetrack panel, Parameters panel, Layers panel; tools include Draw, Spline (which disable timetrack).
- Reading: Synfig = parametric tween-first model: artwork (vector/bitmap) + parameters + waypoints + interpolation; bones for cutout; minimal cel/exposure machinery.

### Adobe Animate (evidence layer C — degraded)

- Official documentation could not be fetched (helpx.adobe.com and adobe.com timed out repeatedly on 2026-09-06). Per source-access rules, no precise operational claims are made from memory.
- Retained in the sample as the market-representative Flash-lineage product (vector + timeline tween tradition, web/interactive export). Its inclusion rests on market position, not on fetched evidence; all Type-level findings below are supported by the four fully-researched products instead.

## Cross-product Comparison

| Dimension | Harmony | TVPaint | OpenToonz | Synfig |
|---|---|---|---|---|
| Frame-based timeline | Timeline view + Xsheet | Timeline (instances/exposures) | Xsheet/Timeline (cells) | Timetrack + keyframes |
| Scene/project container with frame rate | yes (scene) | yes (project) | yes (scene settings: frame rate, camera) | yes (canvas settings) |
| Layer/column stacking | layers + node compositing | layer stack + folders | columns/layers + SO value | layer stack (50+ types) |
| Drawing substrate | bitmap + vector (hybrid) | bitmap (raster) | Toonz Raster + Toonz Vector + imported raster | vector + bitmap |
| Frame-by-frame drawing | yes (hand-drawn) | primary | primary (traditional + paperless) | possible but de-emphasized |
| Exposure/hold of drawings | yes (exposure in timeline) | yes (Instances: Head + Exposure Cells) | yes (cells expose drawings across frames) | n/a (parametric model) |
| Keyframes + interpolation | yes (timeline keyframes, controllers) | Keyframer (advanced), camera keys | yes (auto keyframes, ease in/out, Function Editor) | yes (waypoints, auto inbetweens) |
| Rigging | yes (cut-out rigs, deformers, controllers) | optional (Puppet Layers, Pro) | optional (Skeleton/IK, Plastic mesh) | yes (bones, Skeleton Distortion) |
| Onion skin | yes (drawing views/reference) | yes (Light Table, out-of-pegs) | yes (onion skin mode) | (not confirmed in fetched pages) |
| Camera | Camera view; camera nodes; FOV | 2D Camera + camera keys in timesheet | cameras (multiple, animatable), 3D environment | (canvas transform; not confirmed) |
| Sound/lip sync | (not in fetched pages) | audio tracks + waveform column | soundtrack + lip syncing | (not in fetched pages) |
| Effects | effect nodes, particles | FX Stack per layer | FX Schematic, particles | filters/distortion layers |
| Node/schematic graph | Node view | no (stack-based) | Stage + FX Schematics | parameter linking (ValueNodes) |
| Reuse/library | templates, Library | Image Library, templates | Scene Cast, libraries | exported canvases/parameters |
| Render/preview split | OpenGL preview vs soft render; Render Write Nodes | preview vs export | preview mode vs render; Toonz Farm | render/export dialog |
| Scripting | yes (JS scripting) | George | ToonzScript | (plugins) |
| Render farm | (studio infrastructure) | no | Toonz Farm | no |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A 2D Animation Application is recognizable when all of the following hold:

1. **Frame-based temporal axis** — time is discretized into frames at a frame rate, manipulated on a timeline/xsheet surface.
2. **User-defined per-frame visual content** — the user controls what is visible in each frame, either by drawing/assigning different images per frame, or by posing/transforming artwork whose values are keyed at frames and interpolated between them.
3. **Playback** — the frame sequence can be played back as motion (flip/preview).
4. **Delivery as a moving image** — the sequence can be rendered/exported as a video or image sequence.

Remove the frame axis → static image editor. Remove user-defined per-frame content (content is captured footage) → video editor. Remove playback/delivery → planning artifact (storyboard). This core is substrate-agnostic (bitmap or vector), method-agnostic (drawn, tweened, or rigged), and era-agnostic (paper-scan era Toonz, Flash-era web animation, and modern rigged productions all satisfy it).

### L1 — Common Mature Structure

Present in most mature products; not required for recognition:

- layered composition (layers/columns with stacking order; animatable stacking in some)
- drawing tools (brush engine; bitmap and/or vector) and imported artwork
- onion skin / light table for inbetweening
- exposure/hold mechanics (a drawing held across frames: TVPaint instances, OpenToonz cells, Harmony exposures)
- keyframes + interpolation curves (tweening of transforms/parameters)
- rigging (bones/deformers/IK/meshes) for cut-out character animation
- 2D camera with animatable position/rotation/zoom (multiplane/depth in some)
- sound track + lip-sync support
- palettes/color management
- effects (per-layer stacks or node graphs)
- library/templates/scene-cast reuse
- preview vs final render distinction; export to video/image sequence
- undo/history; project/scene files

### L2 — Variant / Optional Structure

- substrate: bitmap-only (TVPaint), vector-first (Synfig, Animate tradition), hybrid (Harmony, OpenToonz)
- timeline presentation: vertical xsheet (traditional exposure sheet) vs horizontal timeline — same model, two presentations (OpenToonz ships both)
- workflow posture: traditional/scan-based, paperless, cut-out-rig-first, tween-first
- compositing architecture: node graph (Harmony Node view, OpenToonz FX Schematic) vs layer-stack FX (TVPaint FX Stack, Synfig layers)
- 3D integration depth: none → fake 3D/multiplane → true 3D environment/3D model integration (OpenToonz 3D view, Harmony 3D/subnodes)
- target market/output: film/TV episodes, web/interactive (Flash lineage), games (sprite/rig export), education
- team/production infrastructure: render farms, version control, studio databases (OpenToonz Farm/VCS; Harmony server ecosystem)
- scripting/automation: George (TVPaint), ToonzScript (OpenToonz), JS scripting (Harmony), plugins (Synfig)
- licensing: subscription editions (Harmony), perpetual (TVPaint), free/open source (OpenToonz, Synfig)

### L3 — Vendor-specific (research notes only)

- Harmony: Master Controllers / Attribute Controllers (pose libraries with offset semantics), Selection Lock node, Pass Through composite, art layers, Render Write Nodes, WebCC/server, ATOM/USD export, Stop Motion Keyframe Mode.
- TVPaint: Instances/Head Cells/Exposure Cells terminology, Auto Break Instance, CTG layers / Smart Colorization, Out-of-Pegs, George scripting, Japanese/Occidental timesheet layouts (genga/douga columns), Dual Papers.
- OpenToonz: PLI/TLV level formats, Scene Cast, Level Strip, pegbars/table/hook centers (8-inch letter offsets), Toonz Farm, ToonzScript, Plastic tool, Sub-Xsheets.
- Synfig: Waypoints/ValueNodes/Converters/Exported Parameters/Exported Canvases, Timetrack panel, Animation Mode red-border UI.
- Animate: (unverified here) HTML5 Canvas/web export tradition, symbols/library, motion tweens vs frame-by-frame.

## Rejected Findings (not promoted to core)

- "Rigging/bones are part of 2D animation" — rejected for L0: TVPaint Standard and hand-drawn workflows have no rigging; OpenToonz cutout is optional. Rigging = L1 capability, cut-out = L2 workflow variant.
- "Vector artwork is the medium" — rejected: TVPaint is bitmap-only by philosophy; OpenToonz supports both; substrate = L2.
- "Tweening/auto-inbetweening defines the Type" — rejected: the hand-drawn tradition (TVPaint, OpenToonz traditional) defines content per frame manually; Synfig's whole pitch is eliminating that. Tweening = L1 method, tween-first = L2 posture.
- "Node-graph compositing is the structure" — rejected: only some products expose it; others use layer stacks. L2.
- "Phone/mobile-first" — n/a here; all sampled products are desktop. Mobile flipbook apps exist (not sampled) but the desktop sample is representative of the professional Type.
- "Multiplane/3D environment" — L2 depth option, not core (planar 2D animation predates and exists without it).

## Boundary Findings

- **vs Motion Graphics Application**: gradient, not wall. MG centers on composing imported/typographic/graphic layers with keyframed parameters and effects; 2D animation centers on creating the artwork (drawing) and character performance, including frame-by-frame drawing that MG does not do. Overlap zone: Harmony and Animate both do motion-graphics-style work; After Effects does character animation via plugins. Test: remove drawing/cel content creation and character performance → MG; remove graphic/typographic composition emphasis → 2D animation. Flagged for joint review when Motion Graphics Application is processed.
- **vs Video Editor**: clear. Video editor's timeline units are captured media clips; content per frame is not user-defined artwork. 2D animation may import video as reference/backdrop (OpenToonz loads video clips as levels) but its defining content is authored.
- **vs 3D Animation Application**: clear at L0 (planar frames vs 3D scene/objects/cameras), but products blur at the edges (OpenToonz 3D environment, Harmony 3D integration, Blender Grease Pencil = 2D animation inside a 3D app). Depth features are L2.
- **vs Stop-motion Animation Application**: shared frame+playback skeleton, different content acquisition (camera capture of physical media vs drawn/posed digital artwork). Stop-motion apps are capture-and-sequence tools; 2D animation apps are authoring tools.
- **vs Character Animation Application (sibling leaf 04.08)**: in the researched sample, character rig animation is an L1 capability/L2 workflow inside general 2D animation products (Harmony Premium cut-out rigs, TVPaint Puppet Layers, OpenToonz Skeleton/Plastic, Synfig bones). A standalone "Character Animation Application" leaf likely behaves as a Variant/Capability — flagged for joint review; no taxonomy change made unilaterally.
- **vs Digital Painting Application**: painting has no temporal axis; animation products embed painting tools (TVPaint's brush engine) but add the frame axis.
- **vs Storyboard Application**: storyboards are static planning panels; some storyboard products add animatics (Toon Boom ships Storyboard Pro separately from Harmony), confirming the market treats them as different tools.

## Uncertainties

- Adobe Animate evidence is degraded (docs unreachable); its inclusion as representative product rests on market position. No precise Animate claims appear in the final document.
- Harmony deep user-guide pages (rigging/animation chapters) were not reachable; Harmony observations are limited to product page + release notes + docs index (still Tier 1/2, but not full operational depth).
- Synfig onion-skin and camera capabilities were not confirmed in fetched pages (likely present, unverified) — not claimed in final document.
- Moho was not verified at all (sites unreachable); mentioned only as an unverified market reference in research notes, not in the final document's evidence.
- Exact frame-rate defaults, export format lists per product, and numeric limits were deliberately not documented (precision not supported by fetched evidence).

## Final Synthesis

The 2D Animation Application is defined by a minimal core: a frame-based timeline on which the user defines what is visible in each frame — by drawing images per frame, or by keyframing/interpolating transformations of layered artwork — with playback and delivery as a moving image. Around this core, mature products converge on a standard structure: layered composition, drawing tools, onion skin, exposure/hold mechanics, keyframe interpolation, optional rigging, a 2D camera, sound, effects, reuse libraries, and a preview/render split. Products differentiate along substrate (bitmap/vector), timeline presentation (xsheet vs timeline), workflow posture (hand-drawn, tween-first, rig-first, scan-based), compositing architecture (nodes vs stacks), and production infrastructure (farms, version control, scripting). The Type's boundaries are clear against video editing (authored vs captured content), 3D animation (planar vs volumetric), stop-motion (authored vs captured physical frames), painting (no time axis), and storyboarding (no playback). The closest gradient is Motion Graphics, which shares keyframed parametric animation but lacks the drawing/cel/character-performance center; the sibling leaf Character Animation Application appears to be a workflow variant of this Type rather than an independent structure.
