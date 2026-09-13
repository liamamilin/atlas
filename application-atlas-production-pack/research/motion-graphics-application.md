# Research Notes — Motion Graphics Application

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

This pass carries **two joint-review obligations** recorded in STATUS.md by earlier sibling passes:

1. `2d-animation-application` (2026-09-06): "gradient boundary, not a wall — both share keyframes, layers, and effects; the difference is center of gravity (authored drawings + character performance incl. frame-by-frame cels vs moving finished graphic/typographic material) — flagged for joint review when Motion Graphics Application is processed."
2. `3d-animation-application` (2026-09-08): "MoGraph-style procedural motion systems (cloners/effectors/fields) are 3D motion design inside a 3D animation suite, blurring the MG boundary from the 3D side — flagged for joint review when Motion Graphics Application is processed."

Both are discharged in §Boundary Findings (#1, #2).

## Research Goal

Understand what a Motion Graphics Application really is from real products: its core objects (composition, layers/nodes, properties, keyframes/behaviors), its animation paradigm (parametric property animation vs frame-by-frame drawing), its canonical workflow, its interfaces, its rules, and its boundaries against neighboring Types (2D Animation, 3D Animation, VFX Compositing, Video Compositing, Video Editor, UX Prototyping, Presentation, Graphic Design).

## Initial Boundary (hypothesis before research)

- What: software that creates animated graphic imagery — moving typography, titles, logos, animated infographics, broadcast graphics — by composing graphic/media elements and animating their properties over time, delivered as rendered moving images.
- Users: motion designers, broadcast designers, video editors doing titles, agencies, social content creators.
- Nearest neighbors: 2D Animation Application, 3D Animation Application, Visual Effects Compositing Application, Video Compositing Application, Video Editor, UX Prototyping Application, Presentation Application, Graphic Design Application.
- Open questions: is "layer-based" definitional (vs node graphs)? is keyframing definitional (vs behaviors/procedural)? is 2D definitional (vs 3D motion design)? is "graphic material not drawn per frame" the discriminator vs 2D animation? where does VFX compositing end and MG begin (same products serve both)?

## Research Questions

1. What are the core objects (project/composition, layer/node, element types, properties, keyframes, behaviors/effectors, effects/filters, masks, cameras)?
2. What animation paradigms exist (keyframe+interpolation, behaviors, expressions, procedural effectors, data-driven) and which are definitional?
3. What is the material model — is the graphic content composed/assembled from existing or generated material, or authored per frame?
4. What is the workflow (new composition → elements → animate → effects → preview → export/template)?
5. What interfaces exist (canvas/viewport, layer stack or node graph, timeline, keyframe/curve editor, inspector, library, export)?
6. How do products integrate with editors/NLEs (templates, dynamic link, round-trip)?
7. What rules matter (order of operations, composition settings, preview vs final render, alpha handling, template parameter exposure)?
8. Where is the boundary vs 2D animation (drawing/cel/character performance), vs 3D animation (volumetric scenes), vs VFX compositing (footage-first shot work), vs video editing (clip sequencing)?
9. Do older/regional/platform-native products (broadcast character generators, 30-year node compositors, platform-native tools) fit the same core?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| Adobe After Effects | layer-based composition + property keyframes + effects; the market's reference tool for motion graphics | professional standard, broad | **C-degraded** (helpx.adobe.com timeout ×2, adobe.com timeout ×1 — abandoned per source-access rules; included on market position only, no product-specific claims made) |
| Apple Motion | behavior-based + keyframe animation; template factory for Final Cut Pro; platform-native (Mac) | prosumer/pro Mac | **A** (full user guide: welcome, what-is, workflow, basic components, TOC structure) |
| Blackmagic Fusion (Studio + Resolve Fusion page) | node-based compositing-first; VFX + broadcast graphics + 3D in one toolset | film/broadcast, embedded-in-Resolve free + Studio paid | **B** (official product page, feature-level) |
| Maxon Cinema 4D | 3D suite with MoGraph procedural motion design as a first-class feature; 3D pole of motion design | 3D motion design studios | **B** (official product page + FAQ, feature-level) |
| Cavalry | procedural, data-driven, real-time 2D motion design; mesh/behaviour architecture; now Canva-owned, free for individuals | indie/designers/enterprise | **A** (official docs: welcome, shapes/meshes/paths; official product page) |

Rejected/considered: Maxon Autograph (newer MG+compositing tool; mentioned by Maxon's own pages as "2D Motion graphics, VFX compositing, and social media graphics" — retained as unverified market reference), Nuke (VFX-compositing pole, not sampled), web template tools (Canva-class; not sampled), Vizrt-class broadcast graphics authoring/playout (not sampled; boundary noted from Fusion's broadcast-graphics positioning).

## Sources

Fetched 2026-09-08:

- Apple — Motion User Guide welcome: https://support.apple.com/guide/motion/welcome/mac
- Apple — What is Motion?: https://support.apple.com/guide/motion/what-is-motion-motn8d17a294/6.3/mac/15.6
- Apple — Motion workflow: https://support.apple.com/guide/motion/motion-workflow-motn9ad2ed8e/6.3/mac/15.6
- Apple — Basic components of Motion: https://support.apple.com/guide/motion/basic-components-of-motion-motne16be788/6.3/mac/15.6
- Apple — Motion User Guide full TOC (sections: projects, templates/drop zones, media, playback, layers/groups, transforms, blend modes, 3D compositing/cameras/lights, timeline, behaviors [Basic Motion/Parameter/Retiming/Simulation], keyframing/Keyframe Editor, FCP templates, shapes/masks/paint, text, particles, replicators, generators, tracking, keying, retiming, export): https://support.apple.com/guide/motion/toc
- Blackmagic Design — Fusion 21 product page: https://www.blackmagicdesign.com/products/fusion
- Maxon — Cinema 4D product page + FAQ: https://www.maxon.net/en/cinema-4d
- Cavalry — product page: https://cavalry.scenegroup.co/ (and /en/)
- Cavalry — Documentation welcome: https://cavalry.studio/docs/
- Cavalry — Shapes (Layers) docs: https://cavalry.studio/docs/nodes/shapes/
- Adobe — attempted: https://helpx.adobe.com/after-effects/get-started.html (timeout), https://helpx.adobe.com/after-effects/user-guide.html (timeout), https://www.adobe.com/products/aftereffects.html (timeout) — abandoned per source-access rules; AE held at market-position evidence only.

## Product A — Apple Motion (evidence layer A)

Key observations (all from the official Motion User Guide):

- Vendor self-definition: "Motion is a powerful motion graphics tool that makes it easy to create and animate complex images, cinematic titles, fluid transitions, and realistic effects in real time."
- **Workflow (4 steps, vendor-documented)**: 1) Create a project (blank, preset composition, or template for Final Cut Pro); 2) Add media — "Typically, you import media to create a composition... Each media item added to your project becomes a layer in your composite"; can build entire projects from built-in content (preset particle emitters, text, generators); 3) Add or create effects — "applying filters, behaviors, and other built-in effects"; 4) Share — "export it as a QuickTime movie... or export it as an image sequence... a single frame."
- **Object model (vendor-documented)**: the composition you build/save/share is a *project*; components are *objects*: Groups (containers, nestable), Layers (images/video clips, shapes, 3D objects [USDZ], masks, paint strokes, text, particle systems, replicators, generators), Effects objects (cameras, lights, behaviors, filters — "not visible in the canvas on their own; rather, they modify the visual layers").
- **Two animation methods, both first-class**: behaviors ("Sophisticated animation and simulation effects that you can apply to the visual layers... e.g., the Spin behavior to make a shape rotate over time at a rate you specify") and keyframes (Keyframe Editor with curves, interpolation/extrapolation methods, Bezier conversion, curve drawing). Guide documents "Behaviors versus keyframes" and "Combining behaviors with keyframes" and "Convert behaviors to keyframes".
- Behavior taxonomy: Basic Motion (Move, Spin, Motion Path, Fade In/Out, Throw...), Parameter behaviors (Ramp, Oscillate, Randomize, Link, Audio...), Retiming behaviors (Loop, Ping Pong, Set Speed...), Simulation behaviors (Gravity, Attractor, Vortex, Wind...).
- Timeline: Timing pane with layers/tracks, keyframes in Timeline, markers, retiming media; RAM preview optimization; play range; project duration/frame size properties.
- Compositing machinery: layer opacity, blend modes (incl. alpha-channel blend modes), masks, drop shadow, crop; nesting groups; 2D groups vs 3D groups; 3D compositing with cameras (multiple cameras, camera behaviors: Dolly/Sweep/Framing), lights, shadows, reflections, depth of field.
- Content generation: particle systems, replicators ("patterns of repeating visual elements... cascading arrays"), generators (colors, stripes, gradients, patterns), Library content (royalty-free vector artwork, animated design elements, image generators).
- Text: add and animate text; transform text glyphs; per-glyph attributes.
- **Template factory role**: create effect/transition/title/generator templates for Final Cut Pro; drop zones (replaceable media wells); publish parameter controls to FCP; rigging ("map multiple parameters to a single control — e.g., a slider that simultaneously manipulates size, color, and rotation of text"); template markers for timing; multi-aspect-ratio templates.
- Other capabilities documented in TOC: tracking (stabilize, match move, corner-pin), keying (green/blue screen), retiming, Magnetic Mask (ML isolation), 360° video projects, HDR/SDR color management, export for Apple devices.
- Interface surfaces (from TOC): Canvas, Layers list, Inspector (Properties), HUD, Timing pane (Timeline/Keyframe Editor), Library, Media list, Project Browser.

## Product B — Blackmagic Fusion (evidence layer B, product-page level)

Key observations (official product page):

- Vendor self-definition: "Fusion is the world's most advanced compositing software for visual effects artists, broadcast and motion graphic designers, and 3D animators... used on thousands of Hollywood blockbuster movies and television shows" over "the last 30 years."
- **Node-based architecture (vendor-positioned against layers)**: "a powerful node based interface that lets you quickly and easily create sophisticated effects by connecting different types of image processing tools together"; "Nodes are small icons that represent effects, filters and other image processing operations... That's much faster than a timeline based tool because you don't need to hunt through nested stacks of confusing layers and filters!" — the vendor explicitly frames nodes vs layer stacks as competing architectures for the same job.
- **Motion graphics face**: "Broadcast Graphics and Titles" section — "Powerful character generators let you create incredible animated 2D or 3D text and title sequences in any language"; "Create advanced motion graphics with incredible depth using Fusion's infinite 3D workspace to seamlessly combine vector graphics, live action and 3D objects"; 3D particle systems with physics.
- **VFX face (same product)**: keying (Delta/Ultra/Chroma/Luma/Differential keyers), motion tracking, vector paint and rotoscoping, optical flow, stereoscopic 3D, deep pixel compositing (OpenEXR XYZ), 3D model import/render.
- **Editor integration**: Fusion 21 — "Compositions you create on the Fusion page can now be saved as a template and used on the edit or cut page"; effect templates as macros with visible parameters ("build a composition, save it as a macro, define the parameters you want to make visible"); **animation curve modifiers that automatically retime animations when composition duration changes** ("add bounce, mirror or loop animations that automatically change when the duration of the composition changes"); audio playback with waveform display in the keyframe editor for precisely timed animations.
- Fusion Connect: editors select clips in DaVinci Resolve/Avid timelines → send to Fusion → "A new Fusion composition is automatically created and linked dynamically back to the timeline" → rendered shots update back in the timeline.
- Keyframe editors + spline editor mentioned; node tree bookmarks, customizable toolbars, vertical layouts.
- Scripting/automation: Lua and Python; extensible framework.
- Delivery: "world's fastest production quality render engine"; unlimited network render nodes (Fusion Studio); GPU acceleration (Metal/CUDA/OpenCL) for real-time feedback in client sessions.
- Packaging: Fusion page inside DaVinci Resolve (free); Fusion Studio standalone (paid, "activated using a DaVinci Resolve license").

## Product C — Maxon Cinema 4D (evidence layer B, product-page level)

Key observations (official product page + FAQ):

- Vendor self-definition: "Turn ideas into sophisticated visuals with the industry-leading 3D software built for seamless, intuitive motion graphics workflows. Model, animate, simulate, and render..."
- FAQ: "Cinema 4D is a professional 3D animation and modeling software for motion designers, 3D generalists, and creative studios. It combines modeling, animation, simulation, and rendering in a single application... From broadcast graphics and brand animation to product visualisation and VFX."
- **Motion Designers audience block**: "Iterate fast under tight deadlines. MoGraph, procedural animation, and native After Effects integration... Best for: Broadcast graphics, brand animation, title sequences, kinetic typography."
- **MoGraph**: "The industry standard for procedural motion design. Cloners, effectors, fields, and advanced distributions give you systematic control over complex motion. MoGraph is the ideal tool for creating everything from abstract brand animations to broadcast title sequences." (2026.3 release notes: new Cloner distributions — clones on edges, polygon outlines, UV-based surface placement.)
- Animation: "Build precise keyframe animations... control procedural motion with Cinema 4D's parametric animation tools... professional timeline."
- Simulation: unified system (cloth, rigid/soft bodies, particles, smoke, flames, liquids); "combining and blending between force-based simulations and traditional keyframes."
- Rendering: Redshift GPU renderer included; multi-pass rendering for compositing.
- **AE integration**: Cineware — "Seamlessly transfer Cinema 4D scenes into Adobe applications with live updates and native asset support"; VFX Artists block: "Motion tracking, multi-pass rendering, and Cineware integration with After Effects make Cinema 4D a fast compositing partner."
- Ecosystem: Maxon One bundle (ZBrush, Red Giant ["motion graphics finishing for Autograph, After Effects, Premiere Pro"], Universe ["text animation... for motion graphics and video editing"], Capsules asset library, Autograph ["2D Motion graphics, VFX compositing, and social media graphics... optimized for speed and automation"], Moves mocap).
- Solutions taxonomy on Maxon's own site lists BOTH "3D MOTION DESIGN" and "MOTION GRAPHICS" and "KINETIC TYPOGRAPHY" as separate solution pages — the vendor itself treats 3D motion design and (2D) motion graphics as related-but-distinct jobs.

## Product D — Cavalry (evidence layer A docs + B product page)

Key observations:

- Product page: "Motion design reinvented. Professional, real-time animation software." / "Free 2D animation & motion graphics software." Value props: "Change it once, watch it ripple — Adjust a single value, watch entire systems respond" (procedural); "Design in real-time — Full-speed, real-time rendering. No waiting. No preview lag"; "Your data, in motion — Connect a spreadsheet. Animate at scale" (data-driven).
- Feature list: Rig control, Rubber Hose, Connect shapes, Color Palettes, Magic Easing, Text Animation, Duplicator, Data Import, Lottie Export, Forge Dynamics, Falloffs, Quad Tree.
- Docs welcome: "Cavalry is a powerful 2D Animation software for macOS and Windows making waves in the worlds of animation, motion design, creative coding, film, generative art, data visualisation, experiential and advertising." — note the vendor uses BOTH labels ("2D Animation software" in docs, "motion design"/"motion graphics" in marketing): the market itself treats the MG/2D-animation boundary as a gradient.
- Docs structure model (Tier 1): Layers section = Shapes, Behaviours, Utilities, Effects, General (blend modes).
  - "Shapes are Layers that can be drawn in the viewport and animated using keyframes and/or Behaviours."
  - Shape = Layer containing a **Mesh** styled with Fill and Stroke; Mesh = Transform (Position/Rotation/Scale/Pivot) + Fill + Stroke + Path + Child Meshes; meshes form hierarchies — Text Shape → Line → Word → Character — "this is what makes it possible to animate Text on a per line/word/character basis."
  - Procedural Shapes (attribute-driven: Rectangle Size, Ellipse Radius) vs Editable Shapes (point-editable paths for direct manipulation and path animation).
  - Shape-layer catalog: Basic Shape, Text Shape, Duplicator, Particle Shape, Composition (nesting), Footage Shape, Group, Merge, SVG, JavaScript Shape, Image to Shapes, Layouts, Trails, Forge Dynamics, Quad Tree, Cel Animation Shape (frame-by-frame capability exists as one layer type among many).
  - Behaviours as a first-class layer category (parallel to Motion's behaviors).
- Ownership: "Cavalry is now brought to you by Canva"; free for individuals; Enterprise via Canva accounts (SSO). Cavalry Player (Applications section) for playout.
- Export: Lottie (web/UI motion format) listed on product page.

## Product E — Adobe After Effects (evidence layer C-degraded)

- Official documentation unreachable from the research environment (helpx.adobe.com timeout ×2; adobe.com timeout ×1). Per source-access rules: no product-specific operational claims are made anywhere in this pass; AE is retained as a representative product on market position (it is the reference tool the other vendors position against — Motion/C4D/Fusion pages all name it as the integration target).
- Cross-confirmation from other vendors' official pages (layer B): C4D advertises "native After Effects integration" and Cineware; Maxon Red Giant sells "motion graphics finishing for Autograph, After Effects, Premiere Pro"; the 2d-animation pass recorded "After Effects does character animation via plugins" as market knowledge (unverified here).

## Cross-product Comparison

| Dimension | Motion | Fusion | Cinema 4D | Cavalry | After Effects (degraded) |
|---|---|---|---|---|---|
| Unit of authoring | Project (composition) | Composition (node tree) | 3D scene (motion design use) | Scene with Layers | Composition (market knowledge, unverified) |
| Composition architecture | Layer stack + groups (2D/3D groups) | Node graph (vendor explicitly anti-layer-stack) | Object hierarchy in 3D | Layer list with typed layers (Shapes/Behaviours/Utilities/Effects) | Layer stack (market knowledge, unverified) |
| Element types | images/video, shapes, text, masks, paint, particles, replicators, generators, 3D objects | image processing tools as nodes; vector shapes; text/character generators; 3D models; particles | 3D objects, splines, MoGraph clones, particles, cameras/lights | Shapes (basic/text/duplicator/particle/SVG/JS...), Footage, Composition | (unverified) |
| Animation paradigm | keyframes + behaviors (both first-class; convertible) | keyframes + spline editor + curve modifiers (auto-retiming) | keyframes + procedural MoGraph effectors/fields + simulation | keyframes + Behaviours + procedural attributes + data-driven | keyframes + expressions (market knowledge, unverified) |
| Effects | filters, blend modes, masks | hundreds of node tools; Resolve FX | deformers, fields, Redshift rendering | Effects category; falloffs | (unverified) |
| Text machinery | text layers, glyph transforms | character generators, 2D/3D text | (via 3D text/MoText — not confirmed on page) | Text Shape with line/word/character mesh hierarchy | (unverified) |
| 3D | 3D groups, cameras, lights, USDZ objects | true 3D workspace | native 3D | extrude (limited) | (unverified) |
| Editor/NLE integration | FCP templates (titles/effects/transitions/generators, drop zones, published controls, rigging) | Fusion page in Resolve; templates to edit/cut page; Fusion Connect to Resolve/Avid | Cineware → After Effects live scenes | Lottie export (web); Cavalry Player | (unverified) |
| Templates | first-class (Project Browser, drop zones) | macro templates with exposed parameters | Capsules asset library | presets | (unverified) |
| Delivery | QuickTime movie, image sequence, single frame, Apple devices | render engine + network render; back to edit timeline | Redshift render → compositing-ready passes | real-time; Lottie; video | (unverified) |
| Business model | paid (Mac, FCP ecosystem) | free in Resolve; Studio paid | subscription (Maxon One) | free for individuals (Canva); enterprise | subscription |

Stable across all sampled products (cross-product commonality, layer B unless noted):

1. A **composition/project** as the unit of authoring with defined frame size/duration/frame rate.
2. An **ordered arrangement of graphic elements** — realized as a layer stack (Motion, Cavalry, AE-per-market-position) or a node graph (Fusion), or a 3D object hierarchy (C4D).
3. **Parametric property animation over time** — keyframes + interpolation curves in every product; plus rule-based/procedural animation (behaviors in Motion/Cavalry, effectors/fields in C4D, curve modifiers in Fusion, expressions in AE-per-market-position). No sampled product centers on per-frame content authoring.
4. **Effects/filters applied to elements** and **compositing controls** (opacity, blend modes, masks).
5. **Motion preview inside the application** (Motion RAM preview; Fusion GPU real-time feedback; Cavalry real-time rendering; C4D viewport).
6. **Delivery as rendered moving image** (video file / image sequence / single frame / back into an edit timeline / live render), commonly with alpha.
7. **Text as a first-class animated element** (Motion text layers, Fusion character generators, Cavalry text mesh hierarchy, C4D kinetic-typography positioning).
8. **Editor/NLE integration** — every sampled product has a documented bridge to an editing environment (FCP templates, Resolve edit page/Fusion Connect, Cineware→AE, Lottie/web).
9. **Reusable animation assets**: templates/presets/libraries (Motion templates+Library, Fusion macros, C4D Capsules, Cavalry presets).

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

Four jointly-held structures:

1. **The animated graphic composition** — a persistent project/document whose content is an ordered arrangement of graphic elements (typography, shapes, images, video, generated patterns), held as a layer stack, node graph, or equivalent ordered structure. Remove → a static design tool (layered graphic design), not motion graphics.
2. **Parametric time-animation of element properties** — the user defines how properties (transform, opacity, text, effect parameters) change over time by setting keyframes/interpolation curves or by applying rule-based animation (behaviors/expressions/procedural effectors) — the content per frame is computed from parameters, not authored frame-by-frame. Remove → static design; replace with per-frame content authoring → 2D animation.
3. **Motion preview** — the composition plays back in motion inside the application before delivery. Remove → no real product shape; the loop collapses.
4. **Delivery as rendered moving image** — export to video/image sequence (or live-rendered output), typically with alpha, for use in other media (edits, broadcast, web, screens). Remove → interactive prototype tool (UX prototyping) or presentation tool.

Jointly-held is load-bearing: 1 alone = layered graphic design tool; 2 without 1 = animation-curve calculator; 1+2 without 3 = unjudgeable motion (no product shape); 1+2+3 without 4 = interactive prototyping; 2+3+4 without 1 = single-element animation toy, not the professional Type.

### L1 — Common Mature Structure

- Element-type set: text, shapes, images, video footage, generated content (solids/generators/patterns), nested compositions/groups.
- Effects/filters on elements; blend modes; masks/alpha.
- Text animation machinery (per-character/word/line granularity in multiple products).
- Timeline with keyframe editing; curve/graph editor with interpolation control; easing.
- Rule-based/procedural animation layer (behaviors/effectors/expressions) alongside keyframes.
- Nesting (composition inside composition; groups; macros).
- Particles/replication systems (Motion particles+replicators, C4D MoGraph cloners, Cavalry Duplicator/Particle Shape, Fusion particles).
- 2.5D/3D layer depth (3D groups/cameras/lights in Motion and Fusion; native 3D in C4D).
- Audio import + timing sync (Motion audio behavior; Fusion audio waveforms in keyframe editor).
- Motion blur / project settings (frame rate, resolution, duration).
- Render/export with codec and alpha-channel options.
- Editor/NLE bridges and template publishing (FCP templates, Resolve edit-page templates + Fusion Connect, Cineware→AE, Lottie).
- Presets/library content (Motion Library, C4D Capsules, Cavalry presets).
- Tracking/keying/roto present in the same products (Motion, Fusion) — but these are VFX-compositing capabilities appearing in shared products, not MG-defining (see Boundary #3).

### L2 — Variant / Optional Structure

- Composition architecture: layer stack vs node graph (Fusion positions nodes as its identity; Motion/Cavalry use layer lists).
- Animation posture: keyframe-first vs behavior-first (Motion's pitch) vs procedural/effector-first (C4D MoGraph) vs data-driven (Cavalry spreadsheet import).
- Dimensionality: 2D composition vs 2.5D (3D layers/cameras) vs full 3D motion design (C4D; Fusion's 3D workspace).
- Template-driven democratized motion graphics (brand-kit web tools; not directly sampled).
- Broadcast graphics authoring with live playout (Fusion's broadcast-graphics positioning; Vizrt-class tools not sampled).
- Platform-native packaging (Motion inside the Apple/FCP ecosystem; Fusion inside Resolve).
- Business-model variants: free-in-suite (Fusion in Resolve), free-forever (Cavalry), subscription suite (Maxon One, Adobe CC).
- Scripting/automation depth (Fusion Lua/Python; Cavalry JavaScript Shape).

### L3 — Vendor-specific (research notes only)

- Motion: behaviors taxonomy (Basic Motion/Parameter/Retiming/Simulation), replicators, drop zones, published controls + rigging for FCP templates, 360° environments, USDZ 3D objects, Magnetic Mask (ML), Apple device export targets.
- Fusion: node-tool catalog, Delta keyer, macro templates with exposed parameters, animation curve modifiers with auto-retiming on duration change, Fusion Connect dynamic link, bin server, Lua/Python scripting, unlimited render nodes.
- Cinema 4D: MoGraph cloners/effectors/fields + distributions (edges/outline/UV), Take System, Team Render nodes, Redshift inclusion, Cineware live AE scenes, Capsules, Moves mocap, iPad version.
- Cavalry: Mesh hierarchy (line/word/character), data import (spreadsheet-driven animation), Lottie export, Forge Dynamics, JavaScript Shape, Quad Tree, Cavalry Player, Canva ownership/SSO.
- After Effects: no claims (evidence degraded).

## Rejected Findings (not promoted to core)

- "Layer-based composition is the defining structure" — rejected: Fusion is node-based by explicit design and is a motion graphics tool by its own positioning. The abstraction is "ordered arrangement of graphic elements" (stack OR graph). Architecture = L2 variant.
- "Keyframes are the defining animation method" — rejected: Motion's whole pitch includes behaviors as an alternative to keyframes ("Behaviors versus keyframes"), C4D's MoGraph is procedural, Cavalry is data-driven. The abstraction is "parametric time-animation" with keyframes as the dominant implementation.
- "2D is definitional" — rejected: C4D (3D) and Fusion's 3D workspace are motion graphics tools by their own positioning; "3D motion design" is a recognized market job (Maxon has a dedicated solution page). Dimensionality = L2.
- "Motion graphics = titles/lower thirds only" — rejected: sampled products span brand animation, infographics, generative art, data visualization, experiential (Cavalry docs), broadcast packages, FUI (C4D). Titles are the historical core job, not the boundary.
- "Real-time rendering is definitional" — rejected: preview-vs-final-render split persists in every product; real-time is a performance characteristic (Cavalry/Fusion GPU era), not the definition.
- "VFX compositing capabilities (keying/roto/tracking) define the Type" — rejected: they appear in shared products (Motion, Fusion) but belong to the VFX-compositing job; MG survives without them (Cavalry has none of the three on its feature list).
- "Web/social delivery is definitional" — rejected: delivery targets are L2 (broadcast, film, web, experiential all documented).

## Boundary Findings

1. **vs 2D Animation Application (04.08 sibling — JOINT REVIEW DISCHARGED, ratifying research/2d-animation-application.md)**: gradient confirmed from this side. The discriminator is the **center of gravity of the material**: MG composes finished graphic/typographic material (imported media, typed text, drawn shapes, generated patterns) and animates it parametrically; 2D animation creates the artwork itself (drawing, cels) and delivers character performance, including frame-by-frame authoring that MG does not center on. The overlap zone is real and bidirectional: Motion/Cavalry can draw shapes and paint strokes (Cavalry even ships a Cel Animation Shape layer); animation products do MG-style moves (Harmony/Animate per the sibling pass); Cavalry self-labels both ways ("2D Animation software" in docs, "motion design" in marketing). Test (both directions): remove drawing/cel content creation and character performance → Motion Graphics; remove graphic/typographic composition emphasis → 2D Animation. **Ratification: keep both as separate Types; the gradient is documented on both sides.** No taxonomy change.
2. **vs 3D Animation Application (04.08 sibling — JOINT REVIEW DISCHARGED, ratifying research/3d-animation-application.md)**: MoGraph-style procedural motion systems are 3D motion design **inside a 3D animation suite**. C4D's own page frames MoGraph as one feature category ("What you can do with Cinema 4D: Modeling / Animation / Motion Graphics (MoGraph) / Simulation / Rendering") of a suite whose FAQ definition is "professional 3D animation and modeling software." The MG Type's center is graphic/typographic composition for delivery; the 3D pole is a variant (3D motion design) realized inside 3D suites (C4D; Fusion's 3D workspace; Motion's 3D groups). Maxon's own site separates "3D Motion Design" and "Motion Graphics" solution pages — the market treats them as related but distinct jobs. **Ratification: keep both Types; C4D belongs to 3D Animation with an MG variant; this leaf's core stays dimension-neutral (2D-dominant, 2.5D/3D-capable).**
3. **vs Visual Effects Compositing Application (04.07 sibling, unprocessed)**: the same products serve both jobs (Fusion's own page: "compositing software for visual effects artists, broadcast and motion graphic designers"; Motion documents keying/tracking/roto). The seam is the **primary material and the job**: VFX compositing is footage-first, shot-based integration of live action with elements (keying, roto, tracking, cleanup, CG integration); MG is graphic-first creation of animated graphic material. Test: remove footage-integration machinery → MG remains; remove graphic/typographic creation → VFX compositing remains. **Flagged for joint review when Visual Effects Compositing Application is processed.**
4. **vs Video Compositing Application (04.07 sibling, unprocessed)**: same seam as #3 from the compositing side; expected to resolve with the VFX pass. Flagged for that pass.
5. **vs Video Editor (04.06)**: clear. The editor's timeline units are captured media clips sequenced for delivery; MG authors animated graphic material that editors consume (titles, lower thirds, bumpers, transitions). The bundling is deep and bidirectional (Fusion page inside Resolve; Motion templates for FCP; NLE title tools) — product bundling, not Type identity. Test: remove clip sequencing → MG; remove graphic authoring → editor.
6. **vs UX Prototyping Application (04.15)**: both animate screens/graphic elements over time; the deliverable differs — prototypes deliver interactive artifacts, MG delivers rendered moving images. Test: remove rendered-moving-image delivery → prototyping.
7. **vs Presentation Application (03.04)**: both compose visual material with motion; the unit and deliverable differ — slides presented live vs a continuous composition rendered as video. Presentation motion is decoration of a document; MG motion IS the document.
8. **vs Graphic Design Application (04.01) / Illustration (04.03)**: no time axis in design tools; MG adds the time axis and the delivery-as-moving-image loop.
9. **vs AI Video Generator (04.21)**: prompt-generated footage vs parametric composition authoring; era-current adjacency, no structural overlap in the authoring model.
10. **vs Character Animation Application (04.08 sibling)**: per the 2d/3d-animation passes, character rig animation is a capability inside general animation products; MG products reach it only via plugins/adjacent tools (AE-per-market-position). Character performance is not part of this Type's core.
11. **Broadcast graphics playout (no directory leaf)**: authoring animated broadcast graphics fits this Type's core; the live playout engine (rendering to air) is an adjacent surface not represented in the directory. Recorded as an observation; no taxonomy change.

## Historical / Market-Sample Check

- Fusion's vendor page claims a 30-year product lineage ("Over the last 30 years... thousands of Hollywood blockbuster movies") — the node-based composition + parametric animation + render core is stable across that lineage.
- Broadcast character generators (animated text over video — the historical ancestor of motion graphics; Fusion still sells "character generators" for animated text) satisfy the L0 with a minimal composition (text layer over background) — the core does not require modern element variety.
- Platform-native packaging (Motion inside the Apple/FCP ecosystem) satisfies the core.
- The core requires none of: 3D, particles, expressions, templates, GPU real-time, cloud, AI, Lottie — all era-current additions held at L1/L2.
- Conclusion: the definition is not over-fitted to the current market.

## Uncertainties

- After Effects official documentation unreachable (3 timeouts across 2 Adobe hosts); AE-specific claims are absent from both files; AE's role as market reference rests on other vendors' official cross-references (Cineware, Red Giant compatibility) plus market position.
- Fusion and C4D evidence is product-page level (Tier 2); operational specifics (exact tool behaviors, defaults, limits) are not claimed.
- Cavalry's exact export format list beyond Lottie, and its collaboration features, were not verified.
- Live broadcast graphics playout systems (Vizrt-class) were not sampled; the broadcast-graphics boundary rests on Fusion's positioning language.
- Web-based template motion graphics tools (Canva-class) were not sampled; the democratized tier is inferred from Cavalry's Canva ownership and market structure, not direct observation.
- AE's expressions language, shape-layer animators, and Essential Graphics machinery are market knowledge only — deliberately unclaimed.

## Final Synthesis

The Motion Graphics Application is defined by a minimal core: a composition — an ordered arrangement of graphic elements (typography, shapes, images, footage, generated patterns) held as a layer stack or node graph — whose element properties are animated over time parametrically (keyframes + interpolation, or rule-based behaviors/effectors/expressions), with in-application motion preview and delivery as a rendered moving image (video/sequence, commonly with alpha) for use in other media. Around this core, mature products converge on a standard structure: a rich element-type set (text, shapes, media, generators, nested compositions), effects and compositing controls (blend modes, masks), text animation machinery, a timeline with keyframe/curve editing, procedural animation systems alongside keyframes, particles/replication, 2.5D/3D depth, audio sync, render/export with alpha, editor/NLE bridges and template publishing, and preset libraries. Products differentiate along composition architecture (layers vs nodes), animation posture (keyframe vs behavior vs procedural vs data-driven), dimensionality (2D/2.5D/3D motion design), template-driven democratization, broadcast-graphics authoring, and platform packaging. The boundaries are clear against video editing (captured clips vs authored graphics), UX prototyping (interactive deliverable vs rendered moving image), presentation (slides vs continuous composition), and graphic design (no time axis). The two flagged gradients are resolved as documented gradients, not walls: vs 2D animation the discriminator is the material's center of gravity (composed finished graphics vs authored drawings/character performance), and vs 3D animation the 3D motion-design pole is a variant realized inside 3D suites. The remaining open seam — vs Visual Effects/Video Compositing (same products, footage-first vs graphic-first jobs) — is flagged for those sibling passes.
