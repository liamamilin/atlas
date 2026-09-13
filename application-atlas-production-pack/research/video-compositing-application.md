# Research Notes — Video Compositing Application

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

This pass carries **one joint-review obligation** recorded in STATUS.md by the processed sibling `motion-graphics-application` (2026-09-08):

> "NEW flags for unprocessed 04.07 siblings: vs visual-effects-compositing-application and vs video-compositing-application — the same products (node compositors, layer tools) serve both jobs, seam = primary material and job (footage-first shot-based integration [keying/roto/tracking/cleanup] vs graphic-first creation of animated graphic material), flagged for joint review when those leaves are processed."

The MG pass's flag assumed this leaf and `visual-effects-compositing-application` share one seam. This pass's research **refines** that assumption: the compositing job splits into a **real-time program-production family** (this leaf's population) and an **offline shot-based pipeline family** (the VFX sibling's population), with the graphic-first MG family distinct from both. Discharged from this side in §Boundary Findings #1 and #2; the VFX-side joint review remains flagged for the `visual-effects-compositing-application` pass.

## Research Goal

Understand what a Video Compositing Application really is from real products: what "compositing video" means as a software job, what the core objects are (sources/inputs, the mix, scenes/presets, the program output), what the canonical workflow is, which interfaces exist, which rules matter (real-time constraint, alpha, preview/program), and where the boundaries sit against the neighboring Types (Visual Effects Compositing, Motion Graphics, Video Editor/NLE, Video Streaming Platform, Social Live Streaming Platform, Video Calling, Broadcast Management System).

## Initial Boundary (hypothesis before research)

- What: software that combines multiple video sources into a single video output. Hypothesis: the market realizes this as (a) a **real-time/live family** — software video mixers/switchers producing a continuous program (vMix, OBS, Wirecast class) — and (b) an **offline family** whose compositing act lives inside video editors (timeline layering) and film-VFX compositors (shot-based node graphs). The film-VFX pole is the pending sibling leaf's territory.
- Users: live production operators (broadcast, streaming, church/corporate AV, sports), creators and podcasters, marketers.
- Nearest neighbors: Visual Effects Compositing Application (sibling, pending), Motion Graphics Application (processed), Video Editor / NLE (04.06), Video Streaming Platform (§27), Social Live Streaming Platform (§01.08, processed), Video Calling (01.04), Broadcast Management System (§27).
- Open questions: is "video compositing" one Type or an alias of VFX compositing? does live mixing belong here? is real-time operation definitional? is streaming output definitional? is there a distinct offline "video compositing" population?

## Research Questions

1. What do products in the candidate families actually do — what are their core objects (inputs/sources, layers/overlays, scenes/presets, program/preview, outputs)?
2. Is there a distinct product population for "video compositing" vs "VFX compositing" vs "video editing"?
3. What is the mix model — selection/transition between sources, layering/keying/overlaying within the frame — and which parts are universal?
4. What is the workflow (add sources → build composites → rehearse → go live → output concurrently → recordings to post)?
5. What interfaces exist (input/scene grids, preview/program monitors, transition/overlay controls, audio mixer, per-source settings, output/stream settings, control surfaces)?
6. What rules matter (the program never stops; preview/program separation; alpha/transparency for overlays; keying quality; audio/video relationship; performance and latency)?
7. Where is the boundary vs VFX compositing (offline shot pipeline), vs motion graphics (graphic authoring), vs video editing (timeline sequencing), vs streaming platforms (distribution), vs social live platforms (broadcast economy)?
8. Do older/regional products (hardware vision mixers/switchers with keyers, early software switchers) fit the same core?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| vMix (StudioCoast) | commercial Windows live production software; full mixing/switching/keying/overlay feature set; broadcast/pro depth | broadcast / pro AV | **A** (official User Guide introduction page — full feature documentation; homepage + features page) |
| OBS Studio | free open-source scene/source compositor for recording and streaming; the creator/streamer standard | creator / streamer | **A** (official homepage features + KB Quick Start Guide) |
| Ecamm Live | Mac-native commercial studio; camera switcher + saved scenes; creator/podcast tier | creator / podcaster (Mac) | **B** (official product page, feature-level) |
| StreamYard | browser-based SaaS studio; branding/overlays/guests/multistream; non-technical tier | marketer / podcaster | **B** (official homepage, feature-level) |

Boundary anchors (fetched for seam evidence, **not** representative products of this Type):

- **Nuke (Foundry)** — the VFX pole: "powerful node-based compositing toolkit with over 200 nodes", "industry-standard compositing tool" for VFX artists working "shots and sequences" in film/TV pipelines. Evidence **B** (official product family page). Belongs to `visual-effects-compositing-application`.
- **VSDC Free Video Editor** — the offline creator pole: non-linear editor where "objects [are] placed in any position on the timeline", with blending modes, masking, motion tracking. Evidence **B** (official product page). Its primary identity is a video editor (`video-editor` territory); compositing appears as capability, not the product's job.

Rejected/considered: Wirecast (Telestream) — telestream.net wirecast URLs 404 ×2, abandoned per source-access rules; retained as an unverified market member of the live production family, no claims. HitFilm (FXhome) — fxhome.com transport error ×1, abandoned; the offline creator-compositing hybrid tier is therefore evidenced only through VSDC. TriCaster/Vizrt-class hardware-software production systems — not sampled; held as the hardware lineage context. Zero Density/Viz Engine-class real-time broadcast compositing engines — not sampled; adjacent surface noted.

## Sources

Fetched 2026-09-09:

- vMix — homepage: https://www.vmix.com/
- vMix — features page: https://www.vmix.com/software/features.aspx
- vMix — User Guide, Introduction and Features (full feature documentation incl. Live Video Mixing Effects, Layer Designer, Overlay, keying, outputs): https://www.vmix.com/help/ (Introduction.html)
- OBS Studio — homepage (features: scenes/sources, Studio Mode, Multiview, audio mixer, transitions, hotkeys, API): https://obsproject.com/
- OBS Studio — Knowledge Base index: https://obsproject.com/kb
- OBS Studio — Quick Start Guide (sources, scenes, audio mixer, start streaming/recording): https://obsproject.com/kb/quick-start-guide
- Ecamm Live — product page (switcher, scenes, green screen, overlays, guests, ISO recording, multistream, virtual camera): https://www.ecamm.com/mac/ecammlive/
- StreamYard — homepage (browser studio, multistream, branding/overlays, guests, local recordings): https://streamyard.com/
- Nuke Family — product page (node-based compositing, VFX artists, shots/sequences): https://www.foundry.com/products/nuke-family
- VSDC Free Video Editor — product page (non-linear editor, blending modes, masking, motion tracking): https://www.videosoftdev.com/free-video-editor

Unreachable (recorded per source-access rules): Wirecast https://www.telestream.net/wirecast/overview.htm and https://www.telestream.net/wirecast/ (404 ×2); HitFilm https://fxhome.com/hitfilm (transport error ×1).

## Product A — vMix (evidence layer A: User Guide + B: product pages)

Key observations:

- Vendor self-definition (User Guide): "vMix is feature rich live production software that allows you to record and stream professional productions all from a single PC or Laptop." Homepage: "Create, mix, switch, record and live stream professional live productions."
- **Input sources (User Guide)**: video capture (HDMI/HD-SDI/SDI/Component/S-Video up to 4K), NDI/OMT, video files (AVI/WMV/MPEG/MXF/MP4/QuickTime), **Virtual Sets — "Use live chroma keying to place talent in animated 3D virtual sets"**, lists (multiple files as one input), DVDs, CGI Titles (lower thirds, scoreboards), PowerPoint, audio files/devices, photos, remote desktop capture, RTSP/TS/RTMP/SRT streams, video delay/replay, solid colour/colour bars, web browser, video call/remote guests (vMix Call), Zoom meetings.
- **"Live Video Mixing Effects" (User Guide's own section title)**: Cross Fade, Cut, 3D Zoom, Slide, Wipe, Cube, FlyRotate, Fly, CrossZoom, Merge, **"Colour Keying and Chroma Keying with Auto Green or Blue Screen"**, Stinger Transitions.
- **"Live Video Filters"**: Colour Correction, Black/White Level Adjustments, Colour Keying and Chroma Keying (Blue or Green screen), **Luma Key**, **Key and Fill sources**, Deinterlacing and Sharpen, Zoom/Rotate/Pan/Crop.
- **Layer Designer**: "Combine eleven (11) inputs (1 background and 10 foreground) to create layouts in many configurations including split-screen and picture-in-picture."
- **Overlay**: "Overlay any Input with alpha channel transparency as either a full overlay or PIP (Picture In Picture). Eight (8) Overlay Inputs supported at a time in HD, 4K, Pro and Max Editions."
- **Output (User Guide)**: "Output 4 formats simultaneously (Screen, Recording, External Output, Streaming)"; output over NDI/OMT/SRT; optional output to AJA/BlueFish/Blackmagic cards; output to streaming applications. Live streaming: "Built in RTMP live streaming to three providers simultaneously."
- Recording: MP4/AVI/WMV/FFMPEG; **MultiCorder** records raw outputs from multiple capture inputs simultaneously (ISO for post).
- Audio: full mixer per input, up to eight independent audio mixes, VST3 plugins, audio bus manager with flow diagram.
- Control: custom shortcuts on keyboard/MIDI/control surfaces; Activators (MIDI lights/faders); Web Controller (switcher, title editor, telestrator, tally); PTZ camera control; scripting (VB.NET); HTTP/TCP APIs.
- Structure notes: Presets (New/Open/Save — saved production setups); per-input buttons (Cut, Loop, Overlay 1–8, GO, Audio, Preview, Live Pause); Input Settings include Colour Adjust, **Colour Key**, Colour Correction, Effects, **Layers**, **Layer Designer**, Position, Triggers; Transitions menu (Cut, Fade, Merge, Stinger, FTB); Production Clocks; Categories; Fade Bar; Undo; Waveform/Vectorscope monitors; Safe Areas; Data Sources (map spreadsheets to titles); GT Title Designer; Instant Replay; PlayList (automated playback with per-item start/duration/transition).
- Latency posture (User Guide): "vMix introduces approximately 2 frames of delay between input and output. This is similar in performance to standard HD switchers."

## Product B — OBS Studio (evidence layer A: homepage + KB)

Key observations:

- Vendor self-definition: "Free and open source software for video recording and live streaming."
- **Core model (homepage)**: "High performance real time video/audio capturing and mixing. Create scenes made up of multiple sources including window captures, images, text, browser windows, webcams, capture cards and more." — the scene is a named composite of sources; sources are the inputs.
- **Scenes switched with transitions**: "Set up an unlimited number of scenes you can switch between seamlessly via custom transitions." Stinger video files as transitions.
- **Studio Mode**: "lets you preview your scenes and sources before pushing them live. Adjust your scenes and sources or create new ones and ensure they're perfect before your viewers ever see them." — explicit preview/program separation.
- **Multiview**: "Monitor 8 different scenes and easily cue or transition to any of them."
- Audio mixer with per-source filters (noise gate, noise suppression, gain), VST plugin support.
- Hotkeys for scene switching, start/stop stream/record, muting, push-to-talk.
- Modular 'Dock' UI; powerful API with native plugins and Lua/Python scripts.
- Quick Start Guide workflow: auto-configuration wizard (optimizes for streaming/recording intent, hardware, network) → add sources to scenes → set up audio → test settings → Start Recording / Start Streaming.
- KB categories include Sources & Filters, Streaming, Recording, Post-Production.

## Product C — Ecamm Live (evidence layer B: product page)

Key observations:

- Vendor self-definition: "The leading live streaming & video production studio built for Mac."
- **Switcher**: "A live camera switcher lets you direct the show in real time."
- **Scenes**: "Saved scenes means you can compose scenes in advance, complete with on-screen titles and split screens." — the compose-in-advance vocabulary, realized as scenes.
- **Camera effects**: "green screen backdrops, even videos. Get the perfect shot with digital pan and zoom, image adjustments and even color LUTs."
- **Overlays/branding**: "Add your logo and graphics with drag-and-drop elegance. Animations, titles, countdowns, scrolling tickers... even viewer comments."
- **Audience participation**: comments from Facebook/YouTube/Instagram/X/Amazon Live/Twitch "showcase[d] by adding them to your broadcast" — audience content as a composite element.
- **Guests**: "Add up to ten video guests for an instant split-screen, or create a custom layout. Remote guests join from any web browser."
- Inputs: screen/audio capture, HDMI capture (Elgato Cam Link up to 4K), video playback, iOS devices via USB, NDI, Blackmagic DeckLink, DSLR via USB.
- Outputs: local recording ("Every broadcast is automatically saved to your Mac"), **record isolated audio & video** (ISO tracks for post), multistreaming, custom RTMP, NDI output, realtime monitoring, **virtual camera & mic** ("Send Ecamm's output to apps like Zoom and Chrome").
- Control: Elgato Stream Deck support; live scheduling; web widgets (StreamLabs/StreamElements).

## Product D — StreamYard (evidence layer B: homepage)

Key observations:

- Vendor self-definition: "StreamYard is a professional live streaming and recording studio in your browser. Record your content, or stream live to Facebook, YouTube, and other platforms."
- **Multistream**: "Multistream to all platforms at once."
- **Recording**: "Studio quality recordings on any connection. With local recordings, a separate audio and video file is recorded on each user's device."
- **Branding**: "Make your show unique with your own logo, colors, overlays and videos (intro, outro, etc.)." — "No design skills required."
- **Guests**: "Go live or record podcasts with remote guests. It's easy for guests to join from their browser or phone in a few clicks. No software downloads."
- Feature carousel: Recording / Multistream / Guests / Branding. Navigation: Multistreaming, Branded Streams, Recordings, Guest Interviews.
- The browser delivery model and the non-technical audience are the differentiators; the underlying structure (sources → composed show → concurrent outputs) matches the family.

## Boundary anchor — Nuke (evidence layer B)

- "Nuke lives at the heart of the Nuke Family, offering a powerful node-based compositing toolkit with over 200 nodes available in its scalable node graph. Its Deep compositing tools... integrated 3D environment... As the industry-standard compositing tool, Nuke gives artists everything they need to tackle diverse compositing challenges at any scale and resolution."
- Audience: "Compositing, Editorial and Review for VFX artists"; NukeX "giving you unprecedented control over your shots and sequences"; Nuke Studio "multi-shot management, editorial and compositing in a single application."
- This is the **offline, shot-based, film/TV VFX pipeline** pole of "compositing" — the population of `visual-effects-compositing-application`. None of the live-family products describe themselves this way, and Nuke's page never describes live program production.

## Boundary anchor — VSDC (evidence layer B)

- "Our editor is a non-linear tool... objects [can] be placed in any position on the timeline and have any size. Besides, various parameters, shape and position of objects can change arbitrarily over time."
- Blending modes, masking ("hide, blur, or highlight specific elements"), motion tracking ("assign the resulted trajectory to other elements – titles, captions, icons, images, masks").
- Self-identity: "Free Video Editor... best software for video editing on PC." The compositing act (layering/blending/masking) exists **inside an editor whose job is timeline sequencing** — evidence that offline video compositing is realized as a capability of editor-Type products, not as this leaf's product family.

## Cross-product Comparison

| Dimension | vMix | OBS Studio | Ecamm Live | StreamYard |
|---|---|---|---|---|
| Self-label | "live production software... record and stream" | "video recording and live streaming" | "live streaming & video production studio" | "live streaming and recording studio in your browser" |
| Unit of composition | inputs arranged via Layers/Layer Designer + 8 Overlay channels; Presets save whole setups | Scenes = named composites of Sources | Saved scenes composed in advance (titles, split screens) | Show layouts + brands (logo/colors/overlays/intros) |
| Source types | cameras/capture cards, NDI/OMT, files, DVDs, lists, titles, PowerPoint, audio, photos, desktop capture, RTSP/RTMP/SRT, browser, video calls, Zoom, replay, colour generators | window/display/game/video capture, images, text, browser windows, webcams, capture cards | cameras (HDMI/SDI/USB/DSLR), screen/audio capture, video playback, iOS via USB, NDI, DeckLink | camera/mic via browser, remote guests, media/overlays (page-level) |
| Mix act | transitions (cut/fade/wipe/zoom/stinger/merge) + layering + chroma/luma keying + key/fill | scene switching with custom transitions + multi-source scenes layered in the canvas | camera switching + scenes + split screens + green screen + overlays | guest/layout switching + overlays/branding |
| Preview before live | preview input + transitions to program (User Guide structure) | Studio Mode (explicit) | switcher directs in real time (scene-based) | (not observed at page level) |
| Audio | full mixer, buses, VST3, meters | audio mixer, per-source filters, VST | stereo mix, echo cancellation, isolated tracks | (implied, not detailed) |
| Outputs | 4 simultaneous formats (screen/record/external/stream); NDI/OMT/SRT out; AJA/Blackmagic cards; RTMP ×3 | streaming + recording controls; (multistream via plugins — not claimed) | multistream, RTMP, local recording, ISO tracks, NDI out, virtual camera, realtime monitoring | multistream, local recordings (per guest), recording-only mode |
| Graphics in program | CGI titles, scoreboards, tickers, GT Title Designer, stingers, virtual sets | text sources, image sources, browser sources | titles, tickers, countdowns, animations, viewer comments | overlays, intros/outros, branded frames |
| Guests/calls | vMix Call (browser guests), Zoom integration | (not observed on fetched pages) | up to ten browser guests, custom layouts | browser/phone guests |
| Control surfaces | keyboard/MIDI/control surface shortcuts, Activators, Web Controller, PTZ | hotkeys, docks | Stream Deck | (web UI is the surface) |
| Post handoff | MultiCorder ISO recording | recording files | isolated audio/video tracks | local per-guest recordings |
| Business model | paid editions (HD/4K/Pro/Max), 60-day trial | free open source | paid, 14-day trial | freemium SaaS |

Stable across all sampled products (cross-product commonality, layer B unless noted):

1. **Multiple video sources ingested as inputs** — cameras/captures, files, screens, calls/guests, graphics; the material of the Type (all four).
2. **Named, saved composites** — scenes/presets/layouts/brands prepared in advance and recalled during the show (all four).
3. **Real-time operator-directed mix** — selecting/transitioning between sources and combining them in the frame (layering, positioning, split screens, overlays) while the program runs (all four; keying documented in vMix [A] and Ecamm [B]).
4. **A single continuous program output delivered concurrently to multiple destinations** — streaming, recording, external output/virtual camera (all four; vMix documents four simultaneous output formats [A]).
5. **Integrated audio mixing alongside the video mix** (all four at some depth; depth varies).
6. **Graphics as elements inside the program** — titles, tickers, scoreboards, overlays, stingers, branded frames (all four).
7. **Recording of the program (and often of isolated sources) for post-production** (all four).
8. **Live streaming to external platforms as a first-class output** (all four).
9. **Remote guests/calls ingested as sources** (vMix, Ecamm, StreamYard; not observed for OBS on fetched pages).
10. **Control surfaces/shortcuts for live operation** (vMix, OBS, Ecamm; StreamYard's surface is the web UI itself).

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **Multiple video sources as live inputs** — the application ingests several simultaneous video sources (cameras and captures, files, screens, remote calls, graphics) as its working material. Remove → a single-camera app or a media player, not a compositing application.
2. **The real-time mix into one program picture** — while the sources run, the operator directs them into a single continuously-produced picture: selecting and transitioning between sources, and combining them inside the frame (layering, positioning, split screens/picture-in-picture, overlays, keying for transparency). The composite is produced live, under operator control, not rendered offline. Remove the combination → a bare source switcher below the Type; remove real-time operation → offline compositing (VFX-compositing / video-editing territory).
3. **The continuous program output to concurrent destinations** — the composite leaves the application as one running video, delivered simultaneously to one or more outputs (live stream, recording, external monitor/card output, virtual camera). Remove → a preview toy; remove the concurrency → a simple recorder.

Jointly-held is load-bearing: 1 alone = an input hub/capture manager; 2 without 1 = a graphics generator with nothing to mix; 3 without 2 = a player/recorder; 1+2 without 3 = rehearsal with no show; 1+3 without 2 = selection-only switching (the degenerate pole — a bare cut switcher is the family's hardware ancestry but not a *compositing* application).

### L1 — Common Mature Structure

- **Saved composites** — scenes/presets/layouts/brands built in advance and recalled live (all four products).
- **Preview/program separation** — rehearse and adjust the next state before it goes to air (OBS Studio Mode explicit; vMix preview + transition model; Multiview cueing in OBS/vMix).
- **Transitions** — cut, fade, wipe, zoom-class moves, stinger transitions (vMix's documented list is the fullest; OBS custom transitions + stingers; all four switch sources somehow).
- **Layered composition controls** — per-source position/scale/crop/rotate; split-screen and picture-in-picture layouts; overlay channels; alpha-channel handling (vMix Layer Designer/Overlays [A]; OBS multi-source scenes [A]; Ecamm split screens/custom layouts [B]; StreamYard layouts [B]).
- **Keying** — chroma key (green/blue) and luma key extracting transparency from a source (vMix [A: Colour Key, auto green/blue, luma key, key/fill]; Ecamm [B: green screen backdrops]; not directly observed for OBS/StreamYard in fetched pages — held as common-in-family with product-specific documentation).
- **Integrated audio mixing** — per-source levels/filters, buses, meters (all four at varying depth).
- **Graphics as program elements** — titles/lower thirds, scoreboards, tickers, countdowns, overlays, branded frames, stingers (all four).
- **Remote guest ingestion** — browser/call-based guests composited into the program (vMix Call/Zoom, Ecamm guests, StreamYard guests).
- **Recording for post** — program recording; ISO/isolated-track recording in mature products (vMix MultiCorder, Ecamm isolated tracks, StreamYard local per-guest recordings).
- **Live streaming output** — RTMP-class streaming, commonly to multiple destinations simultaneously (all four).
- **Real-time per-source processing** — colour correction, crop/zoom/pan, deinterlace, LUTs (vMix [A], Ecamm [B]; OBS per-source filters observed for audio [A]).
- **Network I/O** — NDI/SRT-class source ingestion and output (vMix [A], Ecamm [B]).
- **Control surfaces** — hotkeys, MIDI/controller surfaces, web/touch controllers, Stream Deck-class pads (vMix, OBS, Ecamm).
- **Monitoring** — multiview, waveform/vectorscope-class scopes in pro products (OBS Multiview [A], vMix scopes [A]).

### L2 — Variant / Optional Structure

- Delivery model: installed desktop software (vMix/Windows, Ecamm/Mac) vs browser SaaS (StreamYard) vs free open-source (OBS).
- Customer tier: broadcast/pro AV (vMix), creator/streamer (OBS, Ecamm), marketer/podcaster (StreamYard).
- Production depth: sports instant replay, virtual sets, PTZ camera control, data-driven titles (vMix); audience-comment overlays (Ecamm, StreamYard); multistreaming breadth.
- Platform specialization (Mac-only vs Windows-only vs browser).
- Streaming-centric vs recording-centric posture (StreamYard records without going live; OBS records without streaming).
- Open-source extensibility (OBS plugins/scripts) vs closed commercial.
- Hardware-tied lineage (professional switchers paired with capture cards/SDI infrastructure).

### L3 — Vendor-specific (research notes only)

- vMix: editions (HD/4K/Pro/Max) gating overlay counts and features; 8 overlay channels; 11-input Layer Designer; GT Title Designer; vMix Call; Zoom input; MultiCorder; Instant Replay; Data Sources (Google Sheets mapping); VB.NET scripting; Activators; HTTP/TCP APIs; ~2-frame input-to-output delay claim; "similar in performance to standard HD switchers" positioning; PlayList automation; Production Clocks; Tally Lights; Safe Areas; Vertical Video Production.
- OBS: Auto-Configuration Wizard; Studio Mode; Multiview (8 scenes); dock UI; Lua/Python scripting + native plugin API; stinger transitions; per-source audio filters (noise gate/suppression/gain).
- Ecamm: Stream Deck integration; iOS devices as cameras/screens via USB; isolated-track recording; virtual camera & mic; NDI I/O; viewer-comment overlays; live scheduling; 14-day trial.
- StreamYard: browser-based operation; guests join from browser/phone without downloads; local per-guest recordings; brand kits (logo/colors/overlays/intros/outros); freemium SaaS.

## Rejected Findings (not promoted to core)

- **"Streaming output is definitional"** — rejected: the L0's output structure is "continuous program to concurrent destinations"; streaming is the dominant modern destination but recording/external output satisfy the core (StreamYard records without streaming; hardware-lineage switchers output to SDI, not RTMP). Streaming = L1.
- **"Scenes are the definitional structure"** — rejected: vMix realizes saved composites as presets + layers/overlays rather than OBS-style scenes; the abstraction is "named, saved composite recalled live". Scene/preset/layout = implementations.
- **"Layer stacks are the definitional composition architecture"** — rejected as phrased: the sampled products combine sources through a mix of layer/overlay channels (vMix), scene-internal source stacking (OBS), and layout templates (StreamYard). The invariant is the *combination into one picture*, not a specific architecture widget.
- **"Keying is definitional"** — rejected at L0: a compositing application can combine sources with opaque layering (PiP, split screen) without keying; keying is the standard route to transparency and is documented in only part of the sample. Held at L1.
- **"This Type = VFX compositing for video"** — rejected: the offline shot-based compositing population (Nuke-class) is a distinct family with a different operating mode (offline render, shot/sequence pipeline, film-grade tooling) — the pending sibling leaf's territory. The live family never describes itself in shot/pipeline terms.
- **"This Type = video editing"** — rejected: editors sequence recorded clips on a timeline into a finished file; this Type produces a continuous program live from running sources. Compositing features inside editors (VSDC) are capability, not this Type's product family.
- **"Multi-camera only"** — rejected: sources include files, screens, calls, graphics — not just cameras.
- **"Browser/SaaS is definitional"** — rejected: installed desktop software dominates the professional tier; delivery model = L2.

## Boundary Findings

1. **vs Motion Graphics Application (04.07 sibling, processed — JOINT REVIEW DISCHARGED from this side)**: the MG pass flagged "the same products (node compositors, layer tools) serve both jobs" and expected this leaf to share the VFX seam. This pass's research **refines** the flag: the compositing job splits into two product families — the **real-time program-production family** (this leaf: vMix/OBS/Ecamm/StreamYard) and the **offline shot-based pipeline family** (VFX sibling: Nuke/Flame/Fusion class) — and the MG family (After Effects/Motion/Cavalry) is distinct from both. The populations are largely **disjoint at their centers of gravity**: no sampled live-mixing product positions itself as a motion graphics tool, and the MG pass's sampled products are not live mixers. The real overlap is **element-level**: animated graphics (titles, tickers, stingers, lower thirds) appear *inside* the live program as sources/overlays — authored by MG tools (delivered e.g. over NDI, per vMix's own NDI positioning "connect... Caspar CG, NewBlue Titler, Adobe CC") or by built-in title editors — and composited live by this Type. Test (both directions): remove live program operation and source mixing → MG remains a rendering/authoring tool; remove graphic authoring → this Type remains a mixer of sources. **Ratification: keep both Types (indeed keep all three 04.07 leaves); the MG pass's "same products" observation holds only for the offline compositing pole, which belongs to the VFX sibling's seam, not to this leaf's population.**
2. **vs Visual Effects Compositing Application (04.07 sibling, unprocessed — joint review flagged for that pass)**: both Types are "compositing" and share primitives (keying, layering, alpha). The proposed seam from this side: **operating mode and job** — this Type produces a *continuous program in real time* under operator control for live distribution (stream/record/output simultaneously); VFX compositing produces *finished shots offline* in a film/TV pipeline (shot/sequence versioning, node graphs, roto/tracking/cleanup/CG integration, render delivery). Product populations at the centers of gravity are disjoint (live mixers vs Nuke/Flame/Fusion). Test: remove real-time program operation → offline compositing (VFX/editing territory); remove the shot/pipeline context and add live operation → this Type. **Flagged for joint review when visual-effects-compositing-application is processed; this side's evidence and proposed seam are recorded here.**
3. **vs Video Editor / NLE (04.06)**: the editor's unit of work is the timeline sequence of recorded clips, rendered to a finished file; this Type's unit of work is the running program assembled live from sources. The bridge is explicit in the sample: compositors record ISO/isolated tracks *for* post (vMix MultiCorder, Ecamm isolated tracks, StreamYard local recordings), and editors consume those recordings. Offline compositing features inside editors (VSDC's blending/masking/motion tracking) are editor capabilities. Test: remove real-time program operation → editor territory; remove timeline sequencing → this Type.
4. **vs Video Streaming Platform (§27)**: the streaming platform is the distribution venue (audience, catalog, player); this Type is the production tool that creates the program feed the platform distributes. vMix/OBS/Ecamm/StreamYard all *stream to* platforms; none operates one.
5. **vs Social Live Streaming Platform (§01.08, processed)**: that Type is the creator-broadcast economy (audience, chat, monetization on a platform); this Type is the pre-platform production layer that assembles the program. Audience comments may be *ingested as elements* (Ecamm/StreamYard), but the audience relationship lives on the platform side.
6. **vs Video Calling / Conferencing Applications (01.04)**: calls appear in this Type as *sources* (vMix Call, Zoom input, Ecamm guests, StreamYard guests) — the call application mediates conversation; the compositing application produces the program that the call feeds into.
7. **vs Broadcast Management System (§27)**: station-wide scheduling/traffic/automation across a broadcast day vs per-program live production. Different granularity, different objects.
8. **vs AI Video Generator (04.21)**: prompt-generated footage vs real-time combination of running sources; no structural overlap in the operating model.
9. **Naming note (recorded, no taxonomy change)**: the phrase "video compositing" is used in the market for both the live mixing family and offline post-production compositing. This leaf is documented as the **real-time program-production Type**; the offline compositing act remains distributed across Video Editor (timeline compositing) and Visual Effects Compositing (shot pipeline) Types. If the VFX pass concludes its leaf and this leaf are one Type, the alias should be resolved there with this pass's evidence in view.

## Historical / Market-Sample Check

- The hardware lineage — broadcast vision mixers/switchers with mix effects and keyers (chroma key, downstream key) — satisfies the L0 exactly: multiple sources in, operator-directed real-time mix/key into one program, continuous program out. vMix's own latency note ("similar in performance to standard HD switchers") and its Key/Fill output support document the software products' continuity with that lineage.
- Early software switchers and streaming-era tools (OBS's decade of open-source history per its site copyright line) satisfy the same core without modern additions.
- The core requires none of: streaming destinations, NDI/SRT, browser delivery, guest browsers, multistreaming, virtual sets, replay, PTZ, scopes, control surfaces — all era-current additions held at L1/L2.
- Conclusion: the definition is not over-fitted to the current streaming-era market.

## Uncertainties

- Wirecast unreachable (404 ×2) — retained as an unverified market member; no claims.
- HitFilm unreachable (transport error ×1) — the offline creator-compositing hybrid tier is evidenced only through VSDC; HitFilm's exact positioning unverified.
- OBS chroma-key/video filters not directly observed in fetched pages (audio filters observed); keying claims attributed to vMix and Ecamm specifically.
- StreamYard evidence is homepage-level; its layout/brand editors' internals not claimed.
- Ecamm evidence is product-page level (Tier 2); operational specifics not claimed.
- Whether the market phrase "video compositing" attaches more strongly to the offline post-production family in some communities — possible; recorded as the naming note in Boundary Findings #9 rather than resolved unilaterally.
- TriCaster/Vizrt-class hardware-software production systems and Zero Density-class real-time broadcast compositing engines not sampled; the hardware lineage is used as historical context only.

## Final Synthesis

The Video Compositing Application is defined by a minimal core: multiple video sources ingested as live inputs; a real-time, operator-directed mix that selects, transitions, and combines those sources into one continuously-produced picture (layering, positioning, split screens, overlays, keying); and that single composite delivered as a continuous program to concurrent destinations — live stream, recording, external output, virtual camera. Around this core, mature products converge on a standard structure: named saved composites (scenes/presets/layouts/brands) recalled live; preview/program separation; transitions including stingers; layered composition controls with alpha handling; chroma/luma keying; integrated audio mixing; graphics as program elements (titles, tickers, scoreboards, overlays); remote guest ingestion; ISO/isolated recording for post; multistreaming; per-source real-time processing; network I/O (NDI/SRT); control surfaces; and monitoring/scopes. Products differentiate along delivery model (desktop/browser/open-source), customer tier (broadcast/pro, creator, marketer), production depth (replay, virtual sets, PTZ, data-driven titles), and streaming-vs-recording posture. The boundaries are clear against motion graphics (authored animated graphics vs live program production; graphics appear as elements inside the program), against VFX compositing (real-time continuous program vs offline shot-based pipeline — flagged for that sibling's joint review), against video editing (timeline sequencing of recorded clips vs live mixing of running sources), against streaming platforms (production tool vs distribution venue), and against social live platforms (production layer vs broadcast economy). The historical check holds: the hardware vision mixer with keyers — the Type's direct ancestry — satisfies the same core with no streaming-era additions.
