# Research Notes — Previsualization Application

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Previsualization Application really is from real products: the objects it manages (scenes, shots, sets, cameras, panels), the realization substrates (drawn panels, 3D sets, floor-plan diagrams), the animatic/playback machinery, the planning artifacts it produces, and its boundaries against neighboring Types — above all the sibling leaf Storyboard Application, but also 3D Animation, Video Editor, Film Production Management, and pure shot-list tools.

## Initial Boundary (hypothesis before research)

- What: software for planning filmed or animated scenes before production — blocking, camera placement, shot sequencing, animatics — "see it before you shoot it."
- Users: directors, cinematographers, previs artists, storyboard artists, production planners, film educators.
- Nearest neighbors: Storyboard Application (sibling leaf §04.19 — the animatic overlap), 3D Animation Application (a 3D tool used for previs is still an animation tool), Video Editor (works on captured footage; previs output feeds it), Film Production Management (logistics of the production office vs creative shot planning), shot-list-only tools (below the Type if no visualization).
- Open questions: is a spatial (3D/floor-plan) scene model definitional, or is the board tradition in-type? Is "animatic playback" the defining act? Are shot lists/camera data part of the core or an add-on? Where exactly does the Storyboard/Previsualization seam run? Are techvis/postvis/virtual-scouting part of this Type?

## Research Questions

1. What is the unit of planning — panel? shot? scene? How are they organized (scene/sequence/shot hierarchy)?
2. How is the planned scene represented (drawn panels, 3D set, floor plan)? What is staged (actors, props, environment, lights)?
3. How is a shot defined (camera position, framing, lens/format, movement)? How realistic are camera controls?
4. How does playback work (animatic, sequencing, timing, sound)? Is rough fidelity deliberate?
5. What planning artifacts leave the application (boards, shot lists, camera diagrams, NLE sequences)?
6. What enters the application (scripts, drawings, LiDAR, templates)?
7. How do revisions work (re-snapping shots, propagating set changes into old shots, diagram↔shot-list sync)?
8. Who uses it and at what production stage?
9. What distinguishes this Type from Storyboard Application, 3D Animation, Video Editor, and production-management software?
10. What would the analog pre-history of this Type look like (Leica reels, floor-plan blocking, director's viewfinders)?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| Toon Boom Storyboard Pro | board-first: drawn panels → animatic timeline; studio pre-production pipeline | enterprise studios, animation/TV; industry standard | A (product page, Help Centre KB incl. 3D-space & Conformation articles, docs.toonboom.com camera chapter) |
| FrameForge Studio (previz pole) | 3D virtual sets + real camera semantics; "fix it in prep" | directors/DPs/VFX supervisors, indie→pro desktop | A (product page + Help Scout KB: Sets/Shots/Scenes, Cameras, Shot Manager, Tweening, Exporting) |
| Shot Designer (Hollywood Camera Work) | floor-plan blocking; diagram + shot list + viewfinder fused; speed-first | directors/DPs, students; free+pro, desktop+mobile | A (official product page is a full functional description; feature pages) |
| Previs Pro | mobile/Apple-first 3D previs with full timeline and NLE export | film/video professionals, TV productions | A (product page + Help Scout KB: Quick Start, Animatics, Camera/Lights categories) |

Cine Tracer (Unreal-engine virtual-cinematography previs) was considered as a fifth, game-engine pole, but its official sources were unreachable (cinetracer.com domain squatted/parked; Steam store page not locatable under the attempted app ID — 2 failed attempts). Per source-access rules it is retained only as an unverified market reference; no claims in this research rely on it and it does not appear in the final document.

## Sources

Fetched 2026-09-08:

- Toon Boom — Storyboard Pro product page: https://www.toonboom.com/products/storyboard-pro
- Toon Boom — Storyboard Pro 27 Online Help root: https://docs.toonboom.com/help/storyboard-pro-27/storyboard/index.html ; User Guide splash: .../book/user-guide/about-user-guide.html
- Toon Boom — Storyboard Pro Knowledge Base: https://helpcentre.toonboom.com/hc/en-ca/categories/39971055086995 (sections: Panels-scenes-sequences; Animatic; 3D; Sound; Import-export-and-library; Project management and conformation)
- Toon Boom — About the 3D space in Storyboard Pro: https://helpcentre.toonboom.com/hc/en-ca/articles/51906021125395
- Toon Boom — AAF/XML/EDL export vs Conformation: https://helpcentre.toonboom.com/hc/en-ca/articles/44802882653843
- Toon Boom — About the Camera (docs): https://docs.toonboom.com/help/storyboard-pro-25/storyboard/camera/about-camera.html
- FrameForge — product page: https://frameforge.com/
- FrameForge Knowledge Base: https://support.frameforge.com/ — categories: Actors, Cameras, Lights and Shadows, Sets, Shot Manager and Snapped Shots, Tweening, Relationships, Exporting, Printing, Percolation
- FrameForge — Difference between SETS, SHOTS and SCENES: https://support.frameforge.com/article/349-difference-between-sets-shots-and-shots
- FrameForge — Physical/Floating/Prop cameras: https://support.frameforge.com/article/40-what-are-the-differences-between-physical-floating-and-prop-cameras
- FrameForge — Shot Preview Area: https://support.frameforge.com/article/343-shot-preview-area
- FrameForge — Exporting Images, Auto-generated HTML or Shot Lists: https://support.frameforge.com/article/299-exporting-images-auto-generated-html-or-shot-lists
- Hollywood Camera Work — Shot Designer product page: https://www.hollywoodcamerawork.com/shot-designer.html
- Previs Pro — product page: https://previspro.com/
- Previs Pro Knowledge Base: https://support.previspro.com/ (categories: Quick Start, Animatics, Camera/Lights, Characters, Props, Prop Types, Storyboards, Walls, Save/Share)
- Attempted, abandoned: cinetracer.com (squatted domain), Steam store page for Cine Tracer (wrong app id; not retried further).

## Product Observations

### Toon Boom Storyboard Pro (evidence layer A unless noted)

- Positioning: "The only professional-grade solution designed from the ground up to support the craft of storyboarding. Whether you are thumbnailing your first pass, refining the visual storytelling on your project, pitching your boards or timing out camera moves in an animatic, Storyboard Pro is built to support your creative work throughout the preproduction process." Vendor self-describes as "global leader in pre-production and 2D animation software"; Storyboard Pro labeled "(storyboarding and layout)".
- Structure (KB sections): "Panels, scenes and sequences — All about the building blocks that create the narrative structure of your storyboard." Thumbnails pages → panels workflow ("How do I turn my thumbnails page into panels?"); drawing tools (vector/bitmap), layers, onion skin; Panel Timer (new in 27) records panel timing live "by tapping while you perform dialogue and actions," optionally importing audio recorded during the session.
- Animatic (KB): "Add movement, timing and camera motion to your storyboard using the Timeline view." Docs camera chapter: the camera displays as a frame matching the project resolution's aspect ratio; camera movements can be restricted to one panel or "spread it out across an entire scene/shot"; camera moves are keyframed in the Timeline view with the Camera tool (e.g., wide shot zooming to close-up).
- 3D (article "About the 3D space"): "Storyboard Pro is predominantly a software for creating 2D visuals, however it also allows the use of a 3D space." 3D can be enabled per scene: multiplane/parallax on 2D layers, 3D camera movements, importing/manipulating/animating 3D models, combining 2D and 3D.
- Sound (KB): record, edit, add effects/fades to sound — animatics carry audio.
- Export/handoff (article "AAF/XML/EDL vs Conformation"): AAF/XML/EDL export "renders video files of all scenes, copies sound files, creates a sequence file… with the same timing as the storyboard file" for Final Cut Pro / Avid / Premiere / Vegas; changes cannot flow back. **Conformation** is the round-trip solution: "Panels become clips… Camera motion as clip animation… Panel captions become clip metadata"; on import back "Panel order and duration, duplication and deletion of panels, added clips become panels… changes to transition type and duration… sound duration, timing… " are reapplied — "ideal for workflows that have a lot of back and forth between the storyboard and animatic processes." Movie export supports timestamp/subtitle/burn-in overlays.
- Reading: the board tradition's previs machinery = panel drawings + per-panel/scene camera + timeline timing + sound + animatic export conforming into the edit.

### FrameForge Studio (evidence layer A)

- Positioning: "FRAMEFORGE STUDIO is not just a better program for creating storyboards, it's actually a better solution to the real problem, which is how to get the most out of your time on set, and get the shots that will make your project absolutely sing." Tagline: "The only software designed to Fix it in Prep." Audience pages: Directors, Cinematographers, VFX Supervisors, Educators.
- Core objects (article "Difference between SETS, SHOTS and SCENES"):
  - **Sets** = "dressed locations," designed for generic reuse when starting a new scene in a given location; FrameForge auto-updates the stored set on exit.
  - **Shots** = "specific camera setups," located in a given set, including actors, cameras, lighting; a reloaded shot is "exactly as it was when you snapped it," regardless of later set changes.
  - **Scenes** = "in FrameForge terms, there is no difference between a scene or sequence, as both are defined as a series of contiguous shots located in a given set."
- Views: **Blueprint View** (overhead plan; double-click to place a camera at a spot), **Control Room** (working view with color-coded per-camera monitors), **Shot Preview Area** (article 343: the ordered frame strip behaves "like a cursor in a word processor" — INSERT vs APPEND vs REPLACE semantics for where the next snapped frame goes), **Shot Manager** (article titles: modify existing shots, delete/restore, "Shot Sequencer and Tree"), plus "Edit in Paint Program" hand-off of snapped frames.
- Cameras (article 40 + category): **Floating** (virtual camera, properties-defined, not visible on set), **Prop** (dressing object that "shoots nothing"), **Physical** (Pro/Stereo: shoots AND appears on set). Camera article titles: aspect ratio setting, film/frame size, anamorphic lenses, camera targets, leveling, camera multi-throttles, adjustable supports (tripod/dolly class), multiple camera types per set, see-through objects.
- Staging: object library (props/camera equipment), sets built/shared/re-used (28 articles), object importing (18), textures, lights & shadows (18 articles incl. Master Dimmer), actors (posing, 23 articles), **Relationships** (9 articles; spatial relationships exportable), **Tweening** (16 articles; tweens animate objects/cameras between key frames — a troubleshooting article confirms tweens "show objects in motion between Key Frames"), game controller support.
- **Percolation** (3 articles, e.g. "Percolate Rerender Camera View"): propagate later set changes into already-snapped shots — the revision discipline around immutable shot records.
- Export (category + article 299): storyboard as PDF, video animation (tween-based motion render), images, **auto-generated HTML or Shot Lists**, overhead blueprints printing, sharing storyboards "with my production staff," exporting sets/poses/relationships as reusable collections; audio export article exists.
- Reading: the previz tradition = build the location, stage actors/cameras in space, snap shots into an ordered sequence, animate motion via tweens, then ship the plan as boards + data.

### Shot Designer (evidence layer A — official product page is a full functional description)

- Positioning: "The industry-standard app for camera blocking." Hook: "Can you block a scene in 30 seconds?" "Neither Camera Diagrams, Shot Lists, Storyboards, or Animation by themselves give you a satisfying understanding of camera-blocking — you have to use them together."
- Connectedness as the core idea: "Everything in the app is connected. Any changes you make in the diagram update the shot list, and any changes you make in the shot list change the diagram." "A Camera Diagram That Makes Itself… automatically moving cameras when you move characters." "A Shot List That Writes Itself… Edit shots intuitively in the diagram, not in a spreadsheet."
- Animation: "Animate your characters and cameras to move around your diagram in real-time. Previsualize the rhythm of a scene by seeing it play out."
- Storyboards inside blocking: "you can bring one of the main benefits of storyboards back into your camera diagram, which is seeing what camera-angles look like"; recommends drawing keyframes rather than full sequences.
- **Director's Viewfinder**: "as both a storyboard replacement, and the ultimate location-scouting tool"; "supports all major camera formats, so you get a perfect record of the exact lens used for a shot."
- Other: Integrated Set Designer (floor plans), Lighting Designer, import production drawings as backgrounds, factory templates of pre-made camera setups, prop/furniture library, **Scene Freeze** snapshots ("Experiment easily by taking snapshots you can return to"), PDF/JPG/Excel export of diagrams and shot lists, Sync & Team Sharing (Pro), unlimited folder structure (Pro).
- Packaging: free version for a single scene; €19.99 Pro; Mac/PC/iOS/Android.
- Explicit roadmap (i.e., capabilities NOT yet present): "3D Animation — a 3D layer for Shot Designer is in development… will render your blocking in 3D in real-time"; "Script Integration / Voice Recording / Speech Synthesis… time camera and character action to the script… deeper timeline."
- Reading: the blocking tradition = floor plan as the scene; cameras + characters as movable symbols; the shot list and the diagram are two views of one model; playback = animated diagram. No 3D, no script import today.

### Previs Pro (evidence layer A)

- Positioning: "Previs Pro — Storyboard Software for Mac, iPhone, and iPad." "See it before you shoot it." "Fix it in Pre." "Brings a full timeline that lives inside a previs tool, that exports cleanly to your editing software. See your storyboard like you edit your film." Claimed first on the timeline point. Trust logos target film/TV professionals and film schools.
- Model (KB article titles): Projects → **Scenes** → **Shots**: "How do I add a shot?", "How do I change the order of my shots?", "How do I change the order of my scenes?", "How do I change the scene settings?", duplicate/delete scene. Camera/Lights category (10 articles) incl. "How do I adjust Depth of Field?"; product page: "Dial in your camera settings from full frame 35mm to Micro 4/3, to ensure your gear aligns with your creative vision."
- Staging: prop library + "Prop Gen with 3D Props" (AI generation), prop types, walls, ceilings, characters with posing + PoseCap (map poses on camera to character models), lights; set design (pre-made sets, import); LiDAR scan import ("get a fully accurate model of a set build or location… design all my camera set-ups, knowing they'll work perfectly in the real world" — director quote); AR virtual camera ("Instantly drop your characters and props into real world locations").
- Animatics (KB): "With Previs Pro you can animate your storyboards and create animatics" — "Capture exact camera, actor and object movements using the full Animatics feature." Timeline: "until you can actually watch the scene play back, with audio, animatics and boards you don't really know if it works."
- Input: "Import your Screenplay… from slug lines to descriptions, cast members… Auto-generate a full storyboard outline" — Final Draft, Fountain, Celtx, open format.
- Output: "Storyboards, animatics, NLE timeline. Print out for cast and crew. Share password protected online weblinks. Make MP4s, or export to Premiere, DaVinci, FinalCut, etc."
- AI-era extras (product page): prop/actor generation, "Enhance" (photorealistic or ink-sketch rendering of the 3D scene, instant video generation), directors markup.
- Reading: the mobile previs = script-derived scene/shot outline staged on a 3D (or AR/LiDAR) set, animated into an animatic on a full timeline, delivered to the shoot and the NLE.

### Cine Tracer (unverified market reference only)

- Official sources unreachable on 2026-09-08 (squatted domain; Steam page not located). Known in the market as an Unreal-Engine-based virtual cinematography/previz tool, but no claim in this research or the final document rests on it.

## Cross-product Comparison

| Dimension | Storyboard Pro | FrameForge | Shot Designer | Previs Pro |
|---|---|---|---|---|
| Unit of planning | Panel (drawn frame) inside scenes/sequences | Shot (snapped camera setup) inside scenes/sets | Shot (camera symbol in diagram) | Shot inside scenes |
| Ordered sequence machinery | Panel strip + Timeline (animatic) | Shot Preview Area (insert/replace), Shot Manager, Shot Sequencer | Shot list ↔ diagram two-way sync | Shots list + full timeline ("see your storyboard like you edit your film") |
| Staging substrate | drawn panels; optional 3D space (per scene) | 3D set + Blueprint overhead view | 2D floor plan diagram | 3D set; AR; LiDAR scans |
| Camera semantics | camera frame with project aspect ratio; per-panel or per-scene camera moves (keyframed); 3D camera optional | floating/prop/physical cameras; film/frame size; anamorphic; supports; multi-throttles | camera symbols auto-follow characters; Director's Viewfinder records exact lens/format | camera formats (full-frame 35mm→M4/3), depth of field |
| Motion within/between shots | camera moves + layer animation in animatic; multiplane | tweens animate objects/cameras between key frames; video animation export | real-time character/camera animation on the diagram | animatics capture camera/actor/object movement |
| Sound | sound tracks, editing, fades; animatics with audio | audio export article exists (secondary) | not present (roadmap: voice recording/soundtrack) | playback "with audio"; animatics + audio |
| Planning artifacts out | PDF boards; movie w/ burn-ins; AAF/XML/EDL; Conformation round-trip | shot lists, HTML, PDF boards, blueprints, images, video | PDF/JPG/Excel diagrams + shot lists | storyboards, animatics, NLE timelines, MP4, printouts, web links |
| Planning input | thumbnails/drawings; script captions (script integration) | script scenes ("in my script I have three scenes…"); sets; object import | production drawings as backgrounds; templates | Final Draft/Fountain/Celtx script import → auto outline |
| Revision discipline | panel-level edit, layer edit across panels | shots immutable once snapped; percolation propagates set changes | diagram↔shot-list always in sync | scene/shot reorder, project settings |
| Team/sharing | project management + conformation (share workload) | share storyboards with production staff | Sync & Team Sharing (Pro) | password-protected web links |
| Platform | Windows/macOS desktop | Windows/macOS desktop | Mac/PC/iOS/Android | Mac/iPhone/iPad |
| Fidelity posture | deliberately rough boards (craft drawings) | mannequin actors, symbolic sets | symbols on plan | stylized 3D; optional AI enhance |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Previsualization Application is recognizable when all four of the following hold:

1. **The shot sequence as the plan of record.** The scene-to-be exists in the application as an ordered, revisable sequence of shots, grouped into scenes/sequences; a shot is a planned camera view of a moment that has not been produced. Remove → a shot-list app or spreadsheet (no visualization), or generic scene planning.
2. **A representational staging space.** The user stages the scene's subjects and environment and defines each shot's view from that staging — whether the substrate is drawn panels with camera frames, a 2D floor plan with camera/actor symbols, or a 3D set. Remove → shot lists / documents with nothing staged to look at.
3. **Timed rough playback (animatic).** The planned sequence plays back as a moving picture with durations — watching it is the evaluation act — at deliberately lower fidelity than the final production. Remove → a static board/layout tool (the Storyboard Application side of the seam).
4. **Production-facing artifacts.** The plan leaves the application as documents the shoot and the edit consume: storyboards/boards, shot lists, camera diagrams/setup data, and edit-ready animatic sequences (movie files or NLE interchange). Remove → a creative 3D/diagram toy with no production loop.

Jointly-held is load-bearing: 1 alone = shot list; 2 alone = set builder/diagram tool; 3 without 1+2 = a video player/editor over already-existing footage; 4 without 1–3 = office documents; 1+2 without 3 = static boards (storyboard territory); 2+3 without 1 = a 3D animation/diagram tool used creatively, not a production plan.

### L1 — Common Mature Structure

Present across the sample, not definitional:

- camera realism machinery: formats/film sizes, lens character (anamorphic etc.), depth of field, supports/movement rigs (3/4 strongly; Storyboard Pro carries aspect-ratio camera frames rather than lens catalogs)
- motion machinery inside the staging: tween/keyframe animation of cameras and subjects (3D pole and board pole both animate; Shot Designer animates on the plan)
- sound/dialogue in the animatic (Storyboard Pro, Previs Pro documented; Shot Designer lacks it today)
- script as upstream input: script import/auto-outline (Previs Pro, and script-based scene organization evidenced in FrameForge and Storyboard Pro captions/integration); Shot Designer explicitly lacks it (roadmap)
- NLE interchange: edit-ready sequences (Storyboard Pro AAF/XML/EDL + Conformation; Previs Pro NLE export; FrameForge video export; Shot Designer PDF/Excel only — gradient)
- sharing/collaboration of the plan with crew (all four in some form)
- libraries/templates of sets, props, camera setups; reusable collections (FrameForge set/pose/relationship export, Shot Designer factory templates, Previs Pro set saving)
- lighting tools in the staging space (FrameForge, Previs Pro, Shot Designer lighting designer; Storyboard Pro via effects — gradient)
- print surfaces for the shoot (all four)

### L2 — Variant / Optional Structure

- realization substrate as product philosophy: drawn-panel-first vs 3D-set-first vs floor-plan-first (a product may offer several; Storyboard Pro adds optional 3D; Shot Designer plans 3D)
- device posture: desktop studio vs mobile/on-location (Shot Designer, Previs Pro) vs desktop-only
- capture-adjacent input: LiDAR scans, AR virtual camera (Previs Pro only — optional, era-current)
- AI assistance: prop/actor generation, style enhancement, generated video (Previs Pro only — optional)
- animatic polish features: burn-ins/subtitles/timestamps on export (Storyboard Pro), transitions, panel-timing capture tools (Panel Timer)
- team sync/sharing packaging (free/pro gating varies)
- edition laddering (FrameForge Core vs Pro/Stereo camera capabilities; Storyboard Pro editions)

### L3 — Vendor-specific (research notes only)

- FrameForge: Sets/Shots/Scenes triad naming, snapping semantics, Shot Preview Area insert/replace "word-processor cursor," Percolation, Floating/Prop/Physical camera taxonomy, Blueprint View/Control Room, Relationships export, "Fix it in Prep" branding.
- Storyboard Pro: Conformation round-trip machinery and its exact export/import feature mapping, Panel Timer recording modes, thumbnails→panels workflow, multiplane, Ember AI add-on.
- Shot Designer: diagram↔shot-list automatic two-way sync, auto-moving cameras, Scene Freeze, Director's Viewfinder as "storyboard replacement + location scouting," single-scene free tier.
- Previs Pro: "full timeline inside a previs tool" industry-first claim, PoseCap, LiDAR import, prop/actor AI generation, Enhance, AR virtual camera.

## Rejected Findings (not promoted to core)

- "A 3D set/virtual actors are what makes it previs" — rejected: Shot Designer is a 2D floor plan (3D is roadmap), Storyboard Pro is predominantly 2D panels, and the analog pre-history had no 3D. Substrate = L2 philosophy.
- "Lens/format realism defines the Type" — rejected: strong in 3/4 (FrameForge, Previs Pro, Shot Designer viewfinder) but Storyboard Pro's camera is an aspect-ratio frame; historical floor-plan blocking managed camera positions without format catalogs. L1 common.
- "NLE round-trip (Conformation-class) is definitional" — rejected: only Storyboard Pro documents a bidirectional conform; others export movies/files. Edit-ready export = L1; one-way vs round-trip = L2/L3.
- "Script import defines the Type" — rejected: Shot Designer explicitly lacks it; script-based organization is common but not universal. L1.
- "Sound is definitional" — rejected: Shot Designer ships without it today. L1.
- "AI generation is definitional" — rejected: single product. Optional/era.
- "Team collaboration defines the Type" — all four share in some form but the shape varies from Pro-gated sync to conform workflows; the single-user creative loop is fully functional without it. Standard capability, not invariant.

## Boundary Findings

- **vs Storyboard Application (sibling leaf §04.19, unprocessed)** — the hardest seam; they share the panel/shot object, the scene/sequence grouping, and increasingly the animatic. Evidence of the straddle: Storyboard Pro (a storyboard product) ships a full animatic timeline, camera moves, sound, and edit conformance; FrameForge (a previz product) exports PDF storyboards and calls its output storyboards; Previs Pro self-labels "Storyboard Software." Candidate discriminator — **center of gravity**: storyboard products center on the drawn board (static narrative panels, drawing craft, captions/script context) with animatic as an extension; previs products center on the blocked scene (staged space, camera setups, coverage, shot sequencing) with boards as one output. Removal tests: remove staging/camera-blocking machinery and playback → a board layout tool (storyboard); remove drawn-panel authoring as the center → previs. Recommendation: keep-both with center-of-gravity seam, joint review when storyboard-application is processed; flag recorded in STATUS.md.
- **vs 3D Animation Application** — a previs tool may manipulate 3D models and keyframe cameras, but its output is a plan (animatic + planning documents), not a finished animated work; fidelity is deliberately rough; the objects are production shots, not performable characters. Conversely 3D animation tools are frequently *used* for previs (and game engines serve virtual-production previz — Cine Tracer tradition) without becoming this Type: usage does not move the Type boundary.
- **vs Video Editor / NLE** — the editor's units are captured/generated footage; the previs tool's units are planned shots. The relationship is directional: the animatic is exported *into* the edit (Conformation, NLE timelines). The previs application holds no footage and finishes nothing.
- **vs Film Production Management (§27, processed)** — that Type is the production office's system of record (schedule, call sheets, breakdown, budget); previs is the creative shot-planning surface. Outputs cross over (boards/shot lists inform scheduling) but neither contains the other's core.
- **vs shot-list-only tools (no directory leaf)** — an ordered shot list with camera notes but no staged visualization and no playback satisfies only leg 1 (and part of 4): below this Type. Shot Designer's own pitch makes the same claim ("shot lists by themselves don't give you a satisfying understanding of camera-blocking").
- **vs UX Prototyping Application** — both "previsualize before building," but the staging object is a filmable scene with cameras vs an interactive interface; no shared machinery beyond the general idea of a prototype.
- Extended forms noted in market discourse (techvis, postvis, virtual scouting on game engines) were not evidenced from official sources this pass and are recorded here as unverified terminology only.

## Historical / Market-Sample Check

Pre-digital previsualization practice (conceptual, per §24):

- **Leica reels / animatics**: timed storyboard boards filmed and cut against temp dialogue/music (Hollywood animation tradition since the 1930s; advertising animatics) — shots as timed framed images (leg 1), the board as framing (leg 2), filmed playback (leg 3), the reel as the planning deliverable for the unit (leg 4). Satisfies the core at analog level.
- **Floor-plan blocking**: ground plans with standees/pawns for actors, marked camera positions and lens notes, the director's viewfinder (a physical analog device for previsualizing framing/lens) — staging space (leg 2), shot definitions with camera semantics (legs 1–2), shot notes as artifacts (leg 4); playback existed as live rehearsal, and was materialized in the Leica reel. Combined practice satisfies all four legs.
- Modern digital forms (desktop 3D previz, mobile AR previs, board-animatic pipelines) all satisfy the four legs; the definition names none of the era-specific machinery (no 3D engine, no LiDAR, no AI, no cloud).

Historical check: passed (conceptual; no single analog artifact carried all four legs, but the combined analog practice did, which is the same pattern previous passes accepted for analog pre-history).

## Uncertainties

- Cine Tracer and the game-engine/virtual-production previs pole are unevidenced this pass (sources unreachable); the Type definition does not depend on them, but the "extended forms" frontier (techvis/postvis/virtual scouting) is recorded only as unverified market terminology.
- FrameForge script-import depth (exact formats/behavior) was not fetched; script-related evidence for FrameForge rests on the Sets/Shots/Scenes article's script-based example ("In my script I have three scenes…"). Assertion kept at "script-based scene organization" strength.
- Shot Designer evidence is its official product page (functional description) rather than a separate help-center KB; the page is detailed, but operational specifics beyond it (e.g., exact export formats list internals) were not verified deeper.
- Previs Pro operational depth comes from KB category/article titles + product page; no long-form manual was fetched. Exact limits (scene counts, pricing tiers, format lists) deliberately not documented.
- Whether pure "animatic software" exists as a standalone below-Type category (animatic assembly from arbitrary imported frames) was not researched directly; the seam test recorded in Boundary Findings is inferred from the sampled products' machinery.
- Audio in FrameForge (single "Can audio be exported?" article) suggests animatic audio exists but was not confirmed in depth.

## Final Synthesis

The Previsualization Application is the shot-planning machine of screen production: the scene-to-be is held as an ordered, revisable sequence of shots; each shot fixes a planned camera view of a staged, representational scene (drawn panels with camera frames, a floor plan with camera/actor symbols, or a 3D set); the sequence plays back as a deliberately rough timed animatic (commonly with sound) that the team watches to judge the scene before production; and the plan leaves the application as the documents the shoot and the edit consume — boards, shot lists, camera/setup data, and edit-ready animatic sequences. Mature products add camera realism (formats, lenses, depth of field), motion machinery (tweens/keyframes for cameras and subjects), script input, lighting, libraries/templates, sharing, and print surfaces. Products differ by realization substrate (board-first, 3D-set-first, floor-plan-first) and device posture (desktop, mobile, on-location). The boundaries are: Storyboard Application (the shared panel/animatic zone — seam = center of gravity: drawn board craft vs blocked-scene planning; joint review flagged), 3D Animation (plan vs finished performance; usage of 3D tools for previs does not change the Type), Video Editor (planned shots vs captured footage; animatic flows into the edit), Film Production Management (creative shot planning vs production-office logistics), and shot-list tools below the Type (no staging, no playback). The analog pre-history (Leica reels, floor-plan blocking with director's viewfinders) satisfies the same core, so the definition is deliberately substrate- and era-agnostic.
