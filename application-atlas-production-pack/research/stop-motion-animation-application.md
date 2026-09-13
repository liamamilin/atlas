# Research Notes — Stop-motion Animation Application

## Research Goal

Understand what a Stop-motion Animation Application really is from real products: what its central objects and loop are, what machinery is definitional vs common vs optional, and where its boundaries sit against the sibling animation Types (2D/3D/Character Animation), video editing, and time-lapse/photography capture. This pass completes the §04.08 Animation sibling cluster (2D, 3D, Character already processed) and discharges the stop-motion boundary note recorded by the character-animation pass ("physical capture vs digital rig").

## Initial Boundary

Working hypothesis before research:

- Core use: create stop-motion animation — photograph a physical scene (puppets, clay, objects, cutouts) one frame at a time, adjusting the physical scene between captures; the app assembles frames, plays them back, exports a movie.
- Likely users: hobbyists/children, students/teachers, indie filmmakers, professional stop-motion studios.
- Nearest neighbors: 2D Animation Application (authored digital frames vs captured physical frames), Character Animation Application (digital rig vs physical puppet), Video Editor (sequences captured footage vs produces it frame-by-frame), time-lapse capture (automatic vs deliberate per-frame control).
- Unknowns: whether camera capture is definitional (some tools import stills); whether scene/take hierarchy is definitional; whether onion skinning is definitional (it appears universal in modern products); the professional/consumer product split.

## Research Questions

1. What is the central persistent object — the frame, the shot/sequence, the project?
2. What exactly is the capture loop: live view → capture → adjust → capture? What assists it (onion skin, guides, stepping/toggling)?
3. How does playback work, and what role does it play in the workflow?
4. What frame-editing machinery exists (delete/reorder/copy/retime/freeze)?
5. What delivery forms exist (video, image sequence, GIF, RAW handoff)?
6. What separates professional products (camera control, X-sheet, dialogue track reading, lighting, motion control) from consumer ones?
7. Is scene/take structure definitional or a professional-heritage variant?
8. Where are the boundaries: vs 2D/3D/Character Animation, vs Video Editor, vs time-lapse, vs photo capture?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Dragonframe | Professional studio tool (feature-film industry standard) | The professional capture-and-control philosophy at its deepest |
| Stop Motion Studio (Cateater) | Consumer mobile-first app | The dominant consumer product; full official manual reachable |
| qStopMotion | Free open-source desktop tool | The minimal open-source pole; full manual reachable |
| Zu3D | Independent education-first software | Independent education product with its own philosophy ("designed with children for children") |
| HUE Animation Studio | Education kit channel (camera + software + book) | Documents the education-channel bundling structure; its software is a licensed Stop Motion Studio variant |
| Stop Motion Pro (Eclipse) | Mid-tier professional (now free) | Historical professional competitor; documents market consolidation |

## Sources

All fetched 2026-09-09. Evidence layers: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

- Dragonframe — homepage and "Dragonframe Software" feature page (Tier-1 product documentation): https://www.dragonframe.com/ , https://www.dragonframe.com/dragonframe-software/
- Stop Motion Studio (Cateater) — homepage and official manual (Tier-1): https://www.cateater.com/ , https://www.cateater.com/en/manual/The_Magic_of_Stop_Motion , https://www.cateater.com/en/manual/Start_Animating (full manual TOC captured)
- qStopMotion — site and full English manual (Tier-1): https://qstopmotion.org/ , https://www.qstopmotion.org/manual/manual_en.html
- Zu3D — homepage and Features page (Tier-2 product documentation): https://www.zu3d.com/ , https://zu3d.com/pages/features
- HUE Animation Studio — product page (Tier-2): https://huehd.com/products/hue-animation-studio/
- Stop Motion Pro — homepage and Eclipse product page (Tier-2): https://www.stopmotionpro.com/ , https://www.stopmotionpro.com/?page_id=42

No source failed; no fetch retries were needed. No numeric limits, prices (beyond what pages state), or defaults are asserted in the final document beyond what the sources directly state.

## Product Observations

### Dragonframe (professional pole) — evidence layer A

- Self-positioning: "the industry standard for stop motion animation software… the choice of major movie studios and independent filmmakers"; feature films listed (Kubo, Isle of Dogs, Wallace & Gromit, etc.).
- Animation tools: "Step directly between live view and captured frames or switch to auto-toggle. Loop playback…"; step-to-live; onionskin ("Blend the live view over any frame in your animation"); toggle on keypress; Nav-Line navigation; high-res playback (video assist frames or proxies); short play (last N frames, configurable); difference mode ("useful for re-lining up a shot if camera or set is bumped"); rotoscope layers (import images/movies/scenes as line-up layers); chromakey for line-up; play/loop markers; drawing tools to mark motion paths with an increment editor.
- Timeline: "Frame-based editing as simple as drag and drop. Adjust timing, reshoot sequences, and even restore deleted frames."
- Cinematography: graphical camera control (shutter speed, aperture, ISO sliders); depth-of-field slider; exposure lock; save camera settings in scene; integrated test-shot system; image review at full resolution; clipping view; Digital Densitometer; multiple exposures (sub-frames) with linked settings; composition guides (aspect-ratio masks, TV-safe, grids, push-in mask); live view magnification (punch-in); capture black-out (darken monitor during capture); automatic live view rest (overheating avoidance); folder watching for unsupported cameras.
- X-Sheet: "Plan your scene and track your progress in the X-Sheet side panel"; customizable printable X-sheet (dope sheet) that updates automatically as exposures, audio phonemes, camera moves, and scene length change; pop-up notes at capture time.
- Audio: multi-track editing; dialogue track reading (create characters, scrub audio, assign words and phonetics; view in X-Sheet/Timeline/Audio HUD); waveform views; reference-track audio; time-warp (audio locked to project frame rate); custom face sets as layered Photoshop files.
- DMX lighting: exposure-based lighting board via DDMX-512 hardware; keyframed lighting programs; work-light ("bash light") for the animator; front/back light programming.
- Motion control: integrated motion control (program camera moves; move tests capture video-assist frames only; rig repositioning for reshoots); jogpad; virtual cartesian axes; 3D data exchange with Maya/Kuper; feathering; markers.
- Project management: production/scene/take naming ("classic clapboard naming convention"); multiple takes per scene carrying camera settings, exposures, moves, notes; copy/rename scenes and takes.
- Stereoscopic 3D tools: integrated 3D shooting with a stereo slider; anaglyph review; 3D export.
- Time-lapse: interval, start/end time, total frames, high precision.
- Export: direct access to source RAW/JPG/TIFF files in an accessible directory; movie export (QuickTime/AVI/MP4 with options); composite export ("rough composite to communicate with post-production"); image-sequence export with naming customization; After Effects import from scene source location.
- Hardware ecosystem sold alongside: Bluetooth/USB controller keypad, DDMX-512 lighting, DMC-32 motion control.

### Stop Motion Studio (consumer pole) — evidence layer A

- Self-positioning: consumer app "for beginners and pros alike" across iPhone/iPad/macOS/Android/Windows/Chromebook/Fire; one-time purchase; 25M+ downloads claim; education/classroom presence (MDM deployment docs).
- Manual's own definition of the technique: "The object is moved or manipulated slightly in small increments and captured in individually photographed frames. This creates the illusion of movement when a series of frames is played as a continuous sequence."
- Capture: device camera or external cameras (USB webcam, DSLR with live view and in-app control of shutter speed/ISO/aperture, GoPro); automatic or full manual camera control (focus, exposure, ISO, white balance); RAW/ProRAW capture; remote camera (second device as camera); remote shutter (headphone volume button, Apple Watch, Bluetooth remote); keyboard/keypad capture; timelapse interval capture; record live video to mix with animation.
- Animation aids: onion skin; composition guides (grids, aspect-ratio masks, safe guides); path layer for motion planning; paint tool to mark positions; reference images/videos; in/out points for looped playback of a section; shooting on twos documented.
- Frame-by-frame editor: frame counter, playhead, capture frame; delete/copy/paste; select sequences; rearrange frames; freeze/pause a frame; retime a sequence; thumbnail symbols; zoomable timeline; scrub video; undo/redo; cut/copy/paste between projects.
- Movie editor: adjust movie speed; preview playback settings; audio (record voiceover, import music/SFX from library or cloud drives, trim/fade/volume, audio effects); titles and credits templates; foreground/background layers; fade in/out; movie effects; aspect-ratio mask; text on frames; draw and erase on frames (multi-layer image editor, Apple Pencil); merge images; masking tool to remove objects ("strings"); green screen (chroma key) with color/sensitivity controls; LEGO figure face overlays.
- Import: images from photo library/files (batch); video clips for rotoscoping ("create animations from a video clip by painting over it, frame by frame").
- Projects: project browser; rename/duplicate/merge/import; transfer between devices (iCloud/Dropbox/AirDrop/iTunes); files-app integration; iCloud sync.
- Export/share: video (4K), GIF, iMessage sticker, flipbook; export all frames in order for external editing; export project; share to YouTube/social.
- Education: classroom guide, shared-iPad setup, MDM configuration, ChromeOS/Windows deployment docs.

### qStopMotion (open-source pole) — evidence layer A

- Manual's own definition: "a program for creating stop motion animation movies from pictures you already have on your harddrive and from pictures you import live from a camera. A stop motion animation is an animation which is built by taking many pictures of some objects while moving it a little between each picture. When these pictures are run you get an animation."
- Project structure: project → scenes → takes → frames (explicit tree; scene/take/frame insert/add/delete buttons).
- GUI: bottom timeline of pictures; center image view (closer look at pictures, webcam view, animation preview); toolbar (navigate, take pictures, play); right tool tabs (Recording, Project).
- Capture: select video device, start camera, capture button takes a frame from the video stream; camera on/off toggle; frames can also be added from disk (add-frames dialog).
- Three camera view modes: (1) image mixing/onionskinning — up to five previous pictures over the camera, count adjustable; (2) image differentiation — difference between selected frame and camera, "move the figure until the picture is black" to restore a bumped position; (3) playback — continuously runs recorded frames with the camera input as the final frame, backward window and FPS configurable.
- Camera controller window (for capable cameras): video-quality controls (brightness/contrast/saturation/hue/gamma/sharpness/backlight/white balance/gain) and camera controls (exposure/zoom/focus/pan/tilt/iris/roll), auto/manual switch.
- External editor integration: open a frame in GIMP (or another painting program), save in place, qStopMotion auto-detects the change.
- Export: video export via an external encoder (mplayer-class), format/size/frame-rate configurable in preferences; project directory exposes the image files; export to a "Cinerella" project format.
- Keyboard-driven workflow (extensive shortcut table); play/loop toggle.

### Zu3D (independent education pole) — evidence layer B (product-page level)

- Self-positioning: "Powerful, intuitive, user friendly stop motion animation software for PC, Mac & iPad"; "originally designed with children for children"; used in thousands of schools; site licenses; animation kit (software + resources).
- Capture: webcam; phone or tablet as a wireless camera; automatic frame capture; time-lapse.
- Features list: green-screen/chroma key (automatic); drawn animations and drawing onto captured frames; rig removal; copy/edit/move/delete frames or clips; zoom between frame view and clip view; onion skinning; import sound effects/music or record; import images & video; video editor combining imported video with animations; import animated GIFs/effects; unlimited audio & video tracks; titles, credits, speech bubbles; time-lapse; instantly change the framerate of the whole film or individual clips; fade transitions between scenes; per-clip/per-track transparency; export MP4 and upload to YouTube or the Zu3D Gallery.
- Education framing: curriculum coverage (storytelling, modeling processes, animate algorithms), skills framing, EAL/SEN accessibility.

### HUE Animation Studio (education kit channel) — evidence layer B (product-page level)

- Kit structure: HUE HD USB camera + software + 64-page book + box-as-mini-stage with green screen + downloadable backgrounds/cutouts/sounds. School bundles (10-kit packs).
- Software: "Stop Motion Studio for HUE" — a licensed variant of Cateater's Stop Motion Studio for Windows/macOS (perpetual single-user license); legacy "HUE Animation" software (formerly SAM Animation) for older systems.
- Documented 5-step workflow: set up → take pictures (capture each frame as you move the character; onion skin shows a "ghost" of the previous frame) → add sound (record voice, import SFX/music, move/trim/volume) → edit frames (text/effects, copy/edit/move/delete, group and reverse frame order, chroma key) → play the movie (in timeline, upload to YouTube).
- Software feature list: playback at any time; onion skinning; time-lapse; reverse; chroma key; frame copy/edit/move/delete; text/effects; YouTube share; 17 languages.
- Market-structure observation: the education channel distributes stop-motion capability as hardware+software+curriculum bundles; the software inside a leading education kit is a branded edition of the consumer pole's product.

### Stop Motion Pro Eclipse (mid-tier professional, now free) — evidence layer B (product-page level)

- Self-positioning: "Fresh, brilliant software for stop motion animation… developed with studios, schools and independent animators"; testimonial framing "feature rich, high res stop motion animation program".
- Features: smooth playback at up to 30 fps; markers to track and plan movement; record audio while playing back animation; capture multiple frames with one click; customizable shortcuts; compatibility with "dozens of cameras" (webcams, Canon/Nikon DSLRs documented on camera pages); advanced project management tools; thumbnail editor; onionskinning ("move puppets with precision"); multi-track audio editor; rig-removal tool; import images and videos; timelapse capture.
- Companion product: Lip Sync Pro (separate lip-sync tool). Network licenses for studios/schools.
- Market-structure observation: the site now states "Stop Motion Pro is now FREE" with download/unlock pages — the commercial operation appears to have ended; the professional market has consolidated around Dragonframe. Treated as market-structure evidence, not asserted as a definitive company-status claim.

## Cross-product Comparison

| Structure / capability | Dragonframe | Stop Motion Studio | qStopMotion | Zu3D | HUE (kit) | Stop Motion Pro | Layer |
|---|---|---|---|---|---|---|---|
| Live camera view as working surface | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Single-frame capture control | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (multi-frame option too) | B |
| Frames accumulate in ordered sequence | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Playback of captured frames as animation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Export/deliver as moving image | ✓ (movie/image seq/composite) | ✓ (video/GIF/sticker/flipbook) | ✓ (via external encoder) | ✓ (MP4) | ✓ (YouTube) | not stated on reachable page | B |
| Onion skinning / live-view blending | ✓ | ✓ | ✓ (mixing mode) | ✓ | ✓ | ✓ | B (6/6) |
| Frame editing (delete/copy/reorder/retime) | ✓ | ✓ | ✓ (cut/copy/paste) | ✓ | ✓ | ✓ | B |
| Camera settings control | ✓ (deep: shutter/aperture/ISO/DoF) | ✓ (auto/manual; DSLR controls) | ✓ (controller window) | not detailed | manual-focus camera hardware | ✓ (DSLR control) | B, depth varies |
| Import stills from disk | ✓ (any images) | ✓ | ✓ (first-class path) | ✓ | — | ✓ | B |
| Import video / rotoscope | ✓ (rotoscope layers) | ✓ | — | ✓ | — | ✓ | B |
| Audio: record/import, multi-track | ✓ (+ dialogue track reading) | ✓ | — | ✓ | ✓ | ✓ | B |
| Time-lapse mode | ✓ | ✓ | — | ✓ | ✓ | ✓ | B |
| Green screen / chroma key | ✓ (line-up chromakey) | ✓ | — | ✓ | ✓ | — | B |
| Rig removal / object masking | — | ✓ | — | ✓ | — | ✓ | B |
| Titles/credits/effects | — | ✓ | — | ✓ | ✓ | — | B |
| Guides (grids/masks/markers/paths) | ✓ | ✓ | — | — | — | ✓ (markers) | B |
| Scene/take hierarchy | ✓ (production/scene/take) | — (flat movie) | ✓ (project/scene/take) | — (clips/tracks) | — | "project management tools" (unspecified) | B |
| X-sheet / dope sheet | ✓ | — | — | — | — | — | A, single product |
| Dialogue track reading / phonemes / face sets | ✓ | — | — | — | — | companion Lip Sync Pro | A/B |
| DMX lighting control | ✓ | — | — | — | — | — | A, single product |
| Motion control | ✓ | — | — | — | — | — | A, single product |
| Multiple exposures (sub-frames) | ✓ | — | — | — | — | — | A, single product |
| Test shots / image review (clipping, densitometer) | ✓ | — | — | — | — | — | A, single product |
| Stereoscopic 3D | ✓ | — | — | — | — | — | A, single product |
| Difference mode (re-align bumped set) | ✓ | — | ✓ (differentiation mode) | — | — | — | B (2 products) |
| External-editor handoff | ✓ (After Effects) | ✓ (export all images) | ✓ (GIMP round-trip) | ✓ (MP4 out) | — | — | B |
| Remote camera / remote shutter | — | ✓ | — | ✓ (phone as camera) | — | — | B |
| Education packaging (kits, site licenses, MDM) | edu pricing | ✓ (MDM docs) | — | ✓ (site licenses, kit) | ✓ (kit, school bundles) | ✓ (network licenses) | B |
| Platform | Mac/Win/Linux desktop | mobile + desktop, cross-platform | Linux/Windows desktop | PC/Mac/iPad | Win/macOS (bundled SW) | Win/Mac | B |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product is not recognizable as a stop-motion animation application:

1. **Camera capture of a physical scene as the source of frames.** The content of each frame is a still image of the physical world in front of a lens, taken by the application from a live camera view. (Remove → the frames are authored digitally → 2D/3D/character animation territory; or a photo editor.)
2. **The deliberate per-frame capture loop.** The animator captures one frame at a time and changes the physical scene between captures; each capture appends to an ordered sequence that constitutes the work-in-progress. (Remove the deliberateness → time-lapse/burst capture; remove the accumulation → single stills.)
3. **Playback of the captured sequence as a moving image.** The assembled frames play at a chosen frame rate; watching the playback is how the animator judges the motion. (Remove → a photo sequence/gallery.)
4. **Delivery as a moving image.** The sequence leaves the application as a video (or as an ordered image sequence for external finishing). (Remove → a capture utility with no product.)

Jointly load-bearing: capture without accumulation/playback = stills; accumulation without the capture loop = slideshow/video assembly (video-editor territory); playback/delivery without camera capture = animation from imported/digital frames (2D-animation territory).

Historical check (film-era pole): an animation stand with a single-frame-exposure film camera satisfies all four legs — frames are photographs of a physically adjusted scene, accumulated in order on film, projected (delayed playback) as a moving image, delivered as film. Instant playback, onion skinning, and digital frame editing are era machinery, NOT in the core. The definition therefore does not over-fit to modern instant-feedback products.

Import path check: qStopMotion defines itself as working "from pictures you already have on your harddrive and from pictures you import live from a camera", and several products import stills/video. Importing previously captured stills is a documented secondary input path that does not redefine the Type — the defining path remains camera capture of a physical scene (the manual of the same product calls direct camera work "the real value").

### L1 — Common Mature Structure

Present across the sample (most products) but not definitional:

- Onion skinning / live-view blending (6/6 sampled — yet the film-era pole lacks it, so it stays L1)
- Frame editing: delete, copy/paste, reorder, retime, freeze/hold, restore deleted frames
- Camera connection breadth (webcam / DSLR / USB / device camera) and camera-settings control (exposure, ISO, white balance, focus)
- Frame-rate control at playback/export; shooting on twos as a documented technique
- Audio: record voiceover, import music/SFX, multi-track editing
- Time-lapse interval capture as a mode
- Green screen / chroma key
- Import of stills and video; rotoscoping (painting over video frames)
- Rig removal / object masking
- Titles, credits, effects (consumer pole)
- Composition guides: grids, aspect-ratio masks, safe areas, motion-path markers
- Project management: project browser, device-to-device transfer, scene/take naming (professional heritage)
- Export options: video formats, image-sequence export, direct access to source image files, external-editor handoff
- Difference mode for re-aligning a bumped set (2/6 sampled, both capture-centric)

### L2 — Variant / Optional Structure

- Scene/take hierarchy (Dragonframe, qStopMotion) vs flat single-movie timeline (Stop Motion Studio, Zu3D)
- Professional cinematography machinery: multiple exposures/sub-frames, test-shot system, image-review tools (clipping view, densitometer), stereoscopic 3D
- Dialogue track reading with phonemes and face sets (Dragonframe; Stop Motion Pro ships it as a companion product)
- DMX lighting control and motion-control rig integration (Dragonframe only in-sample)
- Remote camera (second device) and remote shutter releases (Stop Motion Studio)
- RAW capture (Dragonframe, Stop Motion Studio)
- Drawing on frames / drawn animation inside the stop-motion app (Stop Motion Studio, Zu3D)
- Education packaging: hardware+software+curriculum kits, site/network licenses, MDM deployment
- Business models: one-time purchase, free open-source, perpetual professional license, free-after-discontinuation

### L3 — Vendor-specific (kept out of the final document)

- Dragonframe: DDMX-512/DMC-32 hardware line, Arc motion-control workspace, Digital Densitometer, Nav-Line, Short Play, Audio HUD, Time-Warp, folder watching, capture black-out, EOS live-view correction cap, clapboard naming convention
- Stop Motion Studio: iMessage stickers, Apple Watch shutter, LEGO face overlays, flipbook export, Creator Camp partnership
- qStopMotion: external grabber-program configuration (prepoll/deamon command lines), Cinerella project export, GIMP round-trip
- Zu3D: Zu3D Gallery, speech bubbles, phone-as-wireless-camera implementation
- Stop Motion Pro: Eclipse/Lip Sync Pro product names, "now FREE" wind-down posture
- HUE: kit box-as-stage design, Book of Animation, branded Stop Motion Studio edition

## Rejected Findings

- **"Onion skinning is definitional"** — rejected. 6/6 sampled, but the film-era pole (no video assist, no onion skin) satisfies the L0 without it. It is the strongest common-mature capability, not an invariant.
- **"Scene/take hierarchy is definitional"** — rejected. Two products implement it; the consumer pole flattens to a single movie timeline and remains fully in-type.
- **"Camera-settings control depth is definitional"** — rejected. Depth varies from full DSLR control to simple webcam capture; the invariant is capture from a live camera, not the depth of control.
- **"Stop-motion apps are mobile apps" / "are desktop apps"** — rejected. The sample spans mobile-first, desktop, and open-source Linux; platform is a variant.
- **"Time-lapse is a separate Type"** — rejected as a Type claim; it appears as a mode inside 5/6 sampled stop-motion products. The discriminator is animator control between frames.
- **"Rotoscoping makes it a 2D animation app"** — rejected. Rotoscoping over imported video is a documented capability inside stop-motion products (painting over captured/imported frames); the center remains the capture loop.

## Boundary Findings

1. **vs 2D Animation Application** (sibling, §04.08): 2D animation authors frame content digitally — drawn cels or keyframed/interpolated artwork; stop-motion captures physical reality per frame. Remove the camera/physical capture → 2D animation. Overlap: consumer stop-motion products let users draw frames digitally (drawn animation inside a stop-motion app) — capability, not reclassification. Ratifies the 2D pass's recorded seam ("authored vs captured physical frames") from this side.
2. **vs Character Animation Application** (sibling, §04.08): character animation deforms a digital rig over time; stop-motion poses a physical puppet between captures. Remove the physical capture loop → character animation; remove the digital rig → stop-motion. DISCHARGES the character pass's recorded boundary note ("physical capture vs digital rig") from this side.
3. **vs 3D Animation Application** (sibling, §04.08): 3D animation computes frames from a virtual scene of objects; stop-motion photographs a real one. Same authored-vs-captured discriminator as #1, in the 3D substrate.
4. **vs Video Editor**: a video editor sequences already-captured footage; a stop-motion application's capture loop produces the footage frame-by-frame under the animator's control. Stop-motion products include editing surfaces (the consumer pole ships a full movie editor), but the capture loop is the center; remove the capture loop → video editor.
5. **vs Time-lapse capture**: time-lapse captures automatically on an interval without per-frame animator adjustment; stop-motion is deliberate per-frame capture with adjustment between frames. Time-lapse ships as a mode inside 5/6 sampled products — a capability of this Type, not a separate Type.
6. **vs Photo/camera applications**: burst or continuous shooting lacks the frame-assembly, playback-as-animation, and delivery loop.
7. **Heritage boundary (not a Type)**: the film-era animation stand (rostrum camera + single-frame exposure + exposure sheet) is the analog ancestor; the application digitizes the camera/single-frame-exposure/accumulation loop and adds instant playback and onion skinning that film-era practice lacked.

## Uncertainties

- Stop Motion Pro's exact current company status: the site states the software is "now FREE"; treated as market-structure evidence only.
- HUE's licensing terms for its Stop Motion Studio edition: the bundling relationship is stated on the product page; exact license terms not verified.
- Stop Motion Pro Eclipse's export formats: not stated on the reachable page; no claims made.
- Whether bare capture-only stop-motion apps (no editing at all) exist in the market: plausible and allowed by the L0 floor, but not sampled; the final document does not assert their existence or prevalence.
- Dragonframe edition/pricing structure: not researched; not needed for the Type model.

## Final Synthesis

A Stop-motion Animation Application is defined by a small capture-centric core: it takes still frames of a physical scene through a camera, one deliberate frame at a time while the animator adjusts the scene between captures, accumulates the frames into an ordered sequence, plays that sequence back as a moving image, and delivers it as a video. Everything else — onion skinning, frame editing, camera control depth, audio, time-lapse, green screen, titles, scene/take hierarchy, X-sheets, dialogue track reading, lighting and motion control — is standard, variant, or vendor-specific structure layered on that loop. The Type sits in the §04.08 animation cluster as the captured-physical-frames member: 2D animation authors frames digitally, 3D animation computes them from a virtual scene, character animation drives a digital rig, and stop-motion photographs the physical world. The market realizes the Type across a professional capture-and-control pole, a consumer all-in-one movie-maker pole, a minimal open-source pole, and an education kit channel, with the professional market consolidated around a single industry-standard product and the education channel largely distributing branded editions of consumer software.
