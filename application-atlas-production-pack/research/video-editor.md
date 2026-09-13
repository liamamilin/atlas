# Research Notes — Video Editor

## Research Goal

Understand what a "Video Editor" is as an Application Type at the **general market** level: what object model video editing applications share from consumer to professional, whether the consumer/mobile/platform-native pole implements the same editing paradigm as the professional cluster, what the general market adds on top of the paradigm (templates, stock/music libraries, direct social export, AI assistance), and where the Type boundaries run — above all discharging the joint review delegated by the non-linear-editing-system-nle pass (Video Editor vs NLE) and ratifying the seams recorded by the collaborative-video-editor, ai-video-editing-application, video-compositing-application, and stop-motion-animation-application passes.

## Initial Boundary

- Hypothesis going in: a Video Editor is an application that assembles recorded footage into a finished video program — media imported as clips, arranged on a timeline in arbitrary order and in layers, trimmed and adjusted non-destructively, previewed continuously, exported as a deliverable. The directory's §04.06 holds three leaves (Video Editor, NLE, Collaborative Video Editor); the processed NLE pass concluded the editing paradigm is shared across professional AND consumer editors and flagged the two leaves as likely one underlying Type with a segment gradient.
- Nearest neighbors: Non-linear Editing System / NLE (§04.06 sibling, processed — joint review delegated to this pass), Collaborative Video Editor (§04.06 sibling, processed — shared-project seam), AI Video Editing Application (§04.21, processed — locus-of-execution seam), Motion Graphics Application, Visual Effects Compositing Application / Video Compositing Application, Digital Audio Workstation, Media Asset Management, plus uncatalogued neighbors (slideshow/photo-to-video tools, standalone clip trimmers, social platforms' built-in creation tools).
- Known fuzziness going in: template-driven mobile editors (do they still have a timeline?); platform-native consumer editors (do they satisfy the paradigm?); where "editor" ends and "slideshow maker" begins.

## Research Questions

1. What is the core object model at the general level? (project/draft, media/clips, timeline, tracks, effects, export)
2. Do consumer, mobile-first, and platform-native editors implement the non-linear paradigm (addressable clips, arbitrary-order layered timeline, non-destructive trim, preview, export)?
3. What does the general market add beyond the paradigm? (themes/templates, stock and music libraries, one-tap enhance, direct social export, aspect-ratio handling, AI assistance)
4. How do template/storyboard-driven workflows relate to the timeline? (fill-slots flows; conversion paths between template and timeline modes)
5. What trim/edit vocabulary exists at the consumer level? (drag-edge trim, trimmers, precision editors, split edits)
6. How does audio participate? (music/voiceover/sound effects, volume, fades, separation)
7. What are the export targets and formats across the market?
8. What rules/behaviors matter? (non-destructive editing, project persistence, media links, project settings/conform, render as terminal step)
9. Where are the boundaries? (vs NLE — joint review; vs Collaborative Video Editor; vs AI Video Editing; vs Motion Graphics; vs Compositing; vs DAW; vs MAM; vs slideshow/trimmer tools; vs social platform creation tools)
10. Does the historical check hold? (2000s consumer editors, tape-era lineage, regional products)

## Representative Products

Selected for market representability, documentation completeness, different product philosophies, and different customer levels — deliberately weighted toward the general/consumer pole because the professional cluster was already sampled at Layer A by the NLE pass:

1. **Apple iMovie** — platform-native consumer editor; the canonical "free with the platform" pole; full official user guide. Source: official user guide (welcome, what-is, work-with-projects, trim-clips pages + full TOC).
2. **CapCut / 剪映专业版** (ByteDance) — mobile-first consumer/creator editor, template- and AI-forward philosophy; the mass-market pole. Source: official product page (capcut.com geo-redirected to the official 剪映专业版 page at capcut.cn).
3. **Kdenlive** (KDE) — free open-source desktop editor; the community/distribution pole; complete official manual. Sources: official manual (introduction, quick start, TOC).
4. **DaVinci Resolve** (Blackmagic Design) — professional all-in-one suite with a free tier; the professional anchor tying this pass to the NLE pass's sample. Source: official product overview page.

Named market anchors (not sampled this pass): Adobe Premiere Pro (unreachable ×2 in two prior passes; not retried per network rules — no claims made), Final Cut Pro and Avid Media Composer (Layer A evidence in the NLE pass), WeVideo (collaborative pass), Descript/OpusClip/Runway (AI pass), VSDC (video-compositing pass — classified as video-editor territory).

## Sources

- Apple — iMovie User Guide for Mac (welcome; "What is iMovie"; "Work with projects"; "Trim clips"; full table of contents) — https://support.apple.com/guide/imovie/welcome/mac , https://support.apple.com/guide/imovie/what-is-imovie-mov5ec96da08/mac , https://support.apple.com/guide/imovie/work-with-projects-mov79fa23112/mac , https://support.apple.com/guide/imovie/trim-clips-movf8b8fc9b2/mac — fetched 2026-09-09 (Layer A)
- 剪映 / CapCut — 剪映专业版 official product page — https://www.capcut.cn/ (fetched via https://www.capcut.com/ geo-redirect) — fetched 2026-09-09 (Layer A)
- KDE — Kdenlive 26.08 Manual (index; Introduction; Quick Start) — https://docs.kdenlive.org/ , https://docs.kdenlive.org/getting_started/introduction.html , https://docs.kdenlive.org/getting_started/quickstart.html — fetched 2026-09-09 (Layer A)
- Blackmagic Design — DaVinci Resolve 21 overview — https://www.blackmagicdesign.com/products/davinciresolve — fetched 2026-09-09 (Layer A)
- Prior passes (internal consistency): research/non-linear-editing-system-nle.md + applications/non-linear-editing-system-nle.md (2026-09-08); research/collaborative-video-editor.md (2026-09-06); research/ai-video-editing-application.md; research/video-compositing-application.md; research/stop-motion-animation-application.md (2026-09-09)

Source-access limitations:
- International CapCut (capcut.com) surfaced only via geo-redirect to the official 剪映专业版 (Chinese desktop) page; a direct fetch of https://www.capcut.com/video-editor/ returned 404. Evidence for CapCut is therefore the official Chinese desktop product page; international/mobile feature parity is unverified (same uncertainty recorded by the ai-video-editing-application pass).
- Adobe Premiere Pro official documentation was unreachable in two prior passes (timeouts ×2 each on adobe.com and helpx.adobe.com); not retried this pass per network rules. No product-specific claims about Premiere Pro are made; it is retained as a named market anchor in interchange evidence (Resolve's own page names it).
- iMovie's iOS/iPadOS user guide was not fetched (Mac guide fetched); mobile-iMovie specifics are not claimed.

## Product A — Apple iMovie

### Key observations (Layer A — official user guide)

- Self-description: "With iMovie, you can view, edit, and share movies on your Mac."
- Object model: **Projects view** (browse, search, open all movie and trailer projects in the library); **libraries** containing **events** (media organization; multiple libraries supported; consolidate projects and events; locate source files for clips); **movie projects** and **trailer projects**; **clips** (select, select part of a clip, add, trim, move, split).
- Main window: browser (upper left), viewer (upper right), timeline (bottom).
- Import: photo library, iPhone/iPad, file-based cameras, tape-based cameras, recording directly into iMovie, Mac filesystem.
- Clip review: play or skim video, sort and search clips, rate clips (favorites/rejected).
- Editing: add clips; **trim clips** — drag the clip's edge to extend/shorten ("To extend a clip, there must be unused portions of the clip available"); **clip trimmer** (shows unused portion dimmed; drag edges or shift content within the clip); **precision editor** (expanded view of outgoing/incoming clips around the edit point; adjust transition duration; move audio edit points independently of video — **split edits**); trim-to-selection; move and split clips.
- Transitions: add/modify; **automatic transitions** can be turned off (i.e., they can be on by default).
- Titles: add/modify; maps and backgrounds.
- Audio: add music and sound clips (from music library or included sound effects); record voiceover; extract audio from video clips; change volume; fade audio; correct and enhance audio; audio effects.
- Themes: Apple-designed themes applied to a movie project ("add an Apple-designed theme to give your movie a unique visual style"); **trailers**: template projects ("Choose from a range of Apple-designed templates in almost any genre, then add your own photos and videos to the storyboard"); **convert a trailer to a movie** (template mode → timeline mode conversion path).
- Video effects: automatically enhance clips; adjust clip color; crop/rotate; Ken Burns effect; stabilize shaky clips; clip filters; freeze frames; speed change; instant replay; copy effects between clips.
- Multi-clip effects: cutaway, green-screen (chroma key), split-screen, picture-in-picture ("connected clip effects").
- Share/export: email; **share to social platforms**; export as file; export an image; create App Preview exports.
- Project management: play, open, share, copy/move project to another library, convert trailer to movie, rename, duplicate, delete (deleting a project preserves its media by creating an event with the project's media).
- Cross-surface: import projects created on iPhone or iPad; **send projects to Final Cut Pro** (documented upgrade path to the professional sibling).
- Project settings; window layout customization; keyboard shortcuts and gestures.

## Product B — CapCut / 剪映专业版

### Key observations (Layer A — official product page, Chinese desktop)

- Positioning: "剪映AI — 创作无限可能 — AI生成与专业剪辑，让创意轻松成片" (AI generation + professional editing, easy finished videos); separate desktop ("电脑端 专业版") and mobile ("移动端") editions; a "创作课堂" (creation classroom) learning surface; companion AI tools (即梦AI image generation, 图片设计 graphic design).
- AI tool layer (one-tap operations): 美颜美体 (beauty/body retouching, single and multi-person), 超清画质 (one-tap quality restore/enhance), 智能抠像 (smart chroma-key of people), 智能调色 (one-tap color), AI补帧 (frame interpolation), 人声分离 (voice/background separation), AI音效 (AI-matched sound effects), 音频降噪 (denoise), 人声美化 (voice beautify), 响度统一 (loudness normalization to industry standard), 智能剪口播 (AI removes filler words from talking-head footage, edit against text), 智能解说粗剪 (auto narration rough-cut), 数字人 (digital humans with custom avatars), 文本朗读 (text-to-speech incl. voice cloning), 智能搜索素材 (smart material search).
- Professional editing layer: 蒙版 masks (linear, circular, text, pen — for creative transitions, keying, partial effects); 关键帧 keyframes (set start and end points, smooth transitions auto-generated — movement, scale, fades); 调色 color (color wheels, HSL, hue-saturation curves, float color, RGB curves); 多机位 multicam (auto or audio-based alignment, 4- and 9-camera modes, smooth angle switching); 多时间线 multi-timeline (multiple timelines inside one draft/草稿, stated ceiling of 50, for partitioned editing); 音频剪辑 audio editing (pitch shift, voice separation, stereo balance, audio creation layout).
- Use-case packaging: 自媒体口播 (creator talking-head: beauty, smart cut, voice beautify, smart keying), 影视综二创 (film/TV secondary creation: smart shot splitting, voice separation, TTS, AI music), 政企宣传 (government/enterprise promotion: voice clone, AI music, digital humans, templates), 营销推广 (marketing: digital humans, smart packaging, 营销成片 marketing-video generation, smart copywriting), 专业剪辑 (professional editing: pen masks, keyframes, multicam, audio editing).
- Hardware note: GPU acceleration, 4:2:2 hardware codec support, faster multi-encoder export.
- Note: the fetched page documents the editing model (drafts, timelines, clips, masks, keyframes, color, multicam) but does not document export targets or the mobile template flow in detail; no claims made about those.

## Product C — Kdenlive

### Key observations (Layer A — official manual)

- Self-description: "**Kdenlive** is an acronym for KDE **N**on-**Li**near **V**ideo **E**ditor"; "the free and open source video editor"; GPL; Linux-primary, Windows/macOS/BSD ports; built on Qt and the MLT framework.
- Stated feature set: "Multitrack editing with a timeline and virtually unlimited number of video and audio tracks, plus the ability to split audio and video from a clip in multiple tracks"; **3-point editing**; **non-blocking rendering** ("You can keep working on a project at the same time a project is being transformed into a video file"); dozens of effects and transitions, saveable as custom effects; keyframeable effects with linear or smooth curves; simple tools for color/text/image clips; automatic clip creation from picture directories with crossfades; configurable shortcuts/toolbars/layouts; audio and video scopes; **proxy editing for 4K+ footage**; themable interface.
- Format model: "There is no need to import or convert footage prior to editing"; mix different sources in one project; any resolution (source adapted to project resolution); any frame rate (frames duplicated/removed as needed); wide image import; export to any ffmpeg-supported format incl. DVD/MPEG-2/MP4/Matroska/ProRes; image-sequence and alpha exports.
- Quick Start workflow (canonical loop, verbatim structure): create a project folder + project file with a **project profile** (resolution/frame rate; Kdenlive suggests one from the first clip) → **add clips** to the **Project Bin** (video, audio, images, other Kdenlive projects) → dual monitors (**clip monitor** shows original clips; **project monitor** shows the output with all effects/transitions applied) → **timeline** with video and audio tracks (a video file dropped on an audio track contributes only its audio) → drag clips onto tracks, arrange order → **trim** by dragging clip borders (snaps to the timeline cursor) → **transitions** by overlapping clips on adjacent tracks and inserting a composition (e.g., wipe) → **effects** via the Effect/Composition Stack (searchable list; per-effect enable/disable eye icon; parameters by slider or numeric entry; **keyframes** for parameters over time) → **music** on an audio track with fade-out via a shaded triangle handle → **rendering** ("The process of creating the final video is called *Rendering*"; the saved project "can *not* be played" — render dialog, choose MP4, render to file).
- Manual structure confirms the workflow map: Project and Asset Management → Cutting and assembling → Effects and Filters (incl. titles, subtitles, AI speech-to-text, color correction) → Transitions and Compositions → Titles and Graphics (Glaxnimate vector-animation integration) → Exporting ("Render out your final video for distributing").
- Nested timelines ("sequences", new in 23.04) — a timeline can be used as a clip inside another timeline.

## Product D — DaVinci Resolve

### Key observations (Layer A — official product overview)

- Positioning: "Professional Editing, Color, Effects and Audio Post!" — "the world's only solution that combines editing, color correction, visual effects, motion graphics, audio post production and now photo editing all in one software tool"; "like having your own post production studio in a single app"; Hollywood professionals named as the reference users.
- Page model: Media, Photo, Cut, Edit, Fusion, Color, Fairlight, Deliver — "each of which gives you a dedicated workspace and tools for a specific task… single click to switch between tasks."
- Edit page: "the world's most advanced professional non-linear editor. The familiar track layout, dual monitor design and traditional workflow… drag and drop editing, context sensitive automatic trimming tools… a library full of hundreds of titles, transitions, and effects… complete media management, organization and timeline management tools." (The vendor itself uses "professional non-linear editor" as the category term — the professional qualifier, not the paradigm, is the differentiator.)
- Cut page: speed-oriented streamlined surface (source tape, dual timelines, fast review, sync bin, source overwrite, multicam, broadcast replay, voice-over palette) — "Everything on the cut page is action based."
- Media page: prepare footage, sync clips, organize into bins, add metadata; clone palette for camera-card backup. Deliver page: "total control over all encoding options and formats, along with a render queue"; quick export to YouTube/Vimeo/X from any page.
- Color page (flagship grading), Fusion page (node-based VFX/motion graphics), Fairlight page (DAW-class audio post, up to 2,000 tracks, ADR/Foley, immersive formats), ResolveFX (100+ GPU effects), Neural Engine AI (facial recognition, object detection, smart reframing, speed warp, super scale, auto color/match; IntelliSearch; CineFocus; text-based editing and magic mask in Studio).
- Collaboration: project libraries "built for real time local and remote collaboration"; bin/clip locking, multi-user timelines, update notifications, Blackmagic Cloud; **the free version includes multi-user collaboration and HDR grading**.
- Business model: free version (8-bit up to 60fps/UHD) + Studio one-time purchase ($295, 10-bit/120fps/beyond-4K, Neural Engine, text-based editing); dedicated hardware (Speed Editor/Editor Keyboard, color panels, Fairlight consoles).
- Interchange: "works with all major file formats and post production software, making it easy to move files between DaVinci Resolve, Final Cut Pro, Media Composer, and Premiere Pro." (Names the professional cluster.)

## Cross-product Comparison

| Dimension | iMovie | CapCut/剪映专业版 | Kdenlive | DaVinci Resolve | Evidence |
|---|---|---|---|---|---|
| Self-description | "view, edit, and share movies" | "AI生成与专业剪辑" (AI generation + professional editing) | "KDE Non-Linear Video Editor" | "professional non-linear editor" (edit page) | A×4 |
| Persistent container | Project (movie/trailer) in libraries | Draft (草稿) with multiple timelines | Project file + project folder + profile | Project in project libraries | A×4 |
| Media as addressable clips | clips in events/libraries; rate/search/skim | material/素材 with smart search | Project Bin (video/audio/images/other projects) | bins, metadata, sync clips | A×4 |
| Timeline assembly, arbitrary order | timeline (bottom of window); add/move/split clips | multi-timeline drafts; clips on tracks | timeline with video/audio tracks; drag-and-drop | track layout, drag-and-drop; cut page alternative | A×4 |
| Layered simultaneous elements | connected clips (cutaway/PiP/split-screen/green-screen); audio below video | masks, multi-track, multi-timeline | video + audio tracks; overlap for transitions | track layout; dedicated audio pages | A×4 |
| Non-destructive trim | drag edges; unused portions remain available; clip trimmer; precision editor; split edits | (editing model documented; trim UI detail not on fetched page) | drag clip borders; snap to cursor; multiple cutting ways documented | context-sensitive automatic trimming | A×3 (+B for CapCut editing model) |
| Preview | viewer; play/skim | (preview implied by editing model; not detailed on fetched page) | clip monitor + project monitor; space to play | dual monitor design; fast review | A×3 (+B) |
| Render/export as terminal step | share to social platforms; export file/email/image | (export not detailed on fetched page) | rendering ("the process of creating the final video"); non-blocking; ffmpeg formats | deliver page; render queue; quick export to YouTube/Vimeo/X | A×3 (+B) |
| Transitions | add/modify; automatic transitions toggle | masks for creative transitions | overlap + insert composition (wipe default) | library of hundreds of transitions | A×4 |
| Titles | add/modify titles; maps/backgrounds | (text tools implied; not detailed) | title editor; subtitles; speech-to-text | hundreds of titles; 3D via Fusion | A×3 (+B) |
| Audio layer | music/sound effects/voiceover; volume/fade/enhance | audio editing (pitch, separation, stereo, loudness) | audio tracks; fade handles; audio effects | Fairlight page (DAW-class) | A×4 |
| Color correction | adjust color; auto enhance | color wheels/HSL/curves/RGB | color correction section; scopes | dedicated Color page (flagship) | A×4 |
| Keyframe animation | (not documented as general keyframes; Ken Burns/speed instead) | keyframes (start/end → auto smooth transitions) | keyframeable effects, curves | keyframe editor window; animation | A×3 (iMovie absent) |
| Multicam | — | 4/9-camera, auto/audio sync | — | sync bin, multicam editing | A×2 |
| Proxy editing | — | — | proxy editing for 4K+ | robust proxy editing | A×2 |
| Templates/themes | themes; trailer storyboards; convert to movie | templates; 营销成片 marketing-video generation | — | — | A×2 (consumer-segment) |
| AI assistance | auto enhance; stabilize; cinematic adjust | extensive one-tap AI layer; digital humans; auto rough-cut | AI speech-to-text | Neural Engine; text-based editing (Studio) | A×4 |
| Direct platform export | share to social platforms | (not documented on fetched page) | — | quick export YouTube/Vimeo/X | A×2 |
| Upgrade/interop path | send projects to Final Cut Pro | (not documented) | other Kdenlive projects as clips; ffmpeg export | interchange with FCP/MC/Premiere | A×3 |
| Business model | free with platform | free + paid AI services (implied; not detailed) | free open source (GPL) | free tier + one-time Studio | A×4 |
| Form factor | Mac desktop (+ iPhone/iPad projects import) | desktop 专业版 + mobile edition | Linux/Windows/macOS desktop | Mac/Windows/Linux desktop | A×4 |

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which a product stops being recognizable as a Video Editor:

```text
Project (persistent editing container)
└── Source media imported as individually addressable clips
    └── Timeline sequence — clips placed along a time axis
        in arbitrary order, layered for simultaneous picture/sound
        └── Non-destructive trim & arrange operations
            (the edit changes; the source media never does)
            └── Preview playback of the assembled program
                └── Render / export of the finished program
```

Four properties, each tested with "remove it — what does it become?":

1. **Source media as individually addressable clips** — any imported shot can be opened, skimmed, marked, and used at any point. Remove → a slideshow/photo-to-video tool or a fixed-output converter.
2. **Timeline sequencing in arbitrary order, layered** — clip instances placed along a time axis in any order, layered so picture, dialogue, music, and graphics play simultaneously. Remove → a clip trimmer/one-shot cutter or a linear chain of filters.
3. **Non-destructive editing** — trim/cut/arrange operations change the edit's references, never the source files; unused portions remain available (documented verbatim at the consumer pole: iMovie's trimmer dims "the unused portions of the clips that are available for trimming"). Remove → destructive file processing.
4. **Render/export of a finished program** — the assembled sequence becomes a deliverable (file, platform upload, disc image). Remove → a preview/skimming tool.

The persistent project container is the substrate (project / draft / project file / project library — all four sampled products have one).

**Joint-review consequence (vs NLE):** this Level 0 is *identical* to the NLE pass's Level 0. That is the finding, not an oversight: the professional cluster and the general market share one editing paradigm. See Boundary Findings.

### Level 1 — Common Mature Structure

Present across the sampled products; expected in any current video editor but not required to recognize the Type:

- Media organization layer: libraries/events/bins with search, ratings, metadata (iMovie events/libraries; Kdenlive Project Bin; Resolve bins/metadata; CapCut smart material search)
- Dual monitoring: a source/clip surface and a program/project surface (Kdenlive documents both monitors explicitly; Resolve's "dual monitor design"; iMovie's browser+viewer)
- Transitions between clips; titles; generated elements (color/text/image clips in Kdenlive; maps/backgrounds in iMovie)
- Multi-track audio: music, voiceover, sound effects; volume, fades, enhancement (all four)
- Color correction in-product (all four, from one-tap enhance to dedicated grading pages)
- Keyframe animation of effect parameters (Kdenlive, CapCut, Resolve; iMovie exposes motion effects without a general keyframe editor — 3/4, held as common-not-universal)
- Project settings (resolution/frame rate) with conform of mismatched media (Kdenlive adapts any source to the project profile; Resolve media conform; iMovie project settings)
- Export machinery: presets, file formats, direct platform upload where present (iMovie social sharing; Resolve quick export; Kdenlive ffmpeg)
- AI-era assistance: one-tap enhance, speech-to-text, auto subtitles, smart search (all four in some form; depth varies from aids to auto-rough-cut)
- Non-blocking/background rendering (Kdenlive documents it; Resolve background rendering heritage; iMovie background processing implied by share-while-editing — held common, not universal)

### Level 2 — Variant / Optional Structure

Depends on segment, philosophy, platform, or business model:

- Segment packaging: consumer (iMovie, CapCut), prosumer/creator (CapCut professional layer), professional cluster (Resolve/Avid/FCP — the market's "NLE" term)
- Philosophy: timeline-first (Kdenlive, Resolve edit page) vs template/AI-first with a timeline beneath (CapCut 营销成片/templates; iMovie trailer storyboards — with a documented conversion path from template mode to timeline mode in iMovie)
- Form factor: desktop, mobile, platform-native (iMovie bound to Apple platforms + iOS project interchange), cross-platform, open source
- Suite packaging: focused editor + round-trips (iMovie → Final Cut Pro; Kdenlive → Glaxnimate) vs all-in-one pages (Resolve) — both patterns in-market
- Multicam editing, proxy/optimized-media pipelines (pro-leaning; 2/4 sampled)
- Direct social-platform export (2/4 sampled; consumer/creator-leaning)
- Business model: bundled-free, GPL open source, free tier + paid, subscription (market-wide spread)
- AI posture depth: aids (enhance, transcription) → auto-rough-cut (CapCut 智能解说粗剪) → the separate AI Video Editing Type where the system executes edits as the primary interaction

### Level 3 — Vendor-specific Structure

Remains in Research Notes only:

- Apple: themes/trailer storyboards, precision editor, connected-clip effect naming, Ken Burns, App Preview export, Send-to-Final-Cut-Pro path, iMovie Theater legacy
- ByteDance/剪映: 数字人 digital humans, 营销成片 marketing-video generation, 智能剪口播/智能解说粗剪 naming, 50-timeline draft ceiling, 4/9-camera modes, voice cloning, 即梦AI companion, 创作课堂
- KDE/Kdenlive: MLT framework, melt CLI playback footnote, Glaxnimate integration, sequences/nested timelines versioning, Breeze theming
- Blackmagic: page naming (Cut/Edit/Color/Fusion/Fairlight/Deliver/Photo), Neural Engine, IntelliSearch, ResolveFX, Speed Editor/panels/consoles, free-vs-Studio feature split, $295 price point

## Vendor-specific Findings

- The template-first philosophy (fill slots in a storyboard/template, get a finished cut) is documented at the consumer pole (iMovie trailers, CapCut 营销成片) with a documented conversion path to the timeline (iMovie "Convert Trailer to Movie"). It is a philosophy variant, not a separate Type: the timeline model persists beneath, and the same products also offer direct timeline editing.
- The one-tap AI layer (beauty, keying, denoise, loudness, auto rough-cut) is most developed in the mass-market product (CapCut) but exists in some form in all four samples — era-current common structure, depth varies.
- The "draft with multiple timelines" model (CapCut) and "library of events and projects" model (iMovie) and "project file + folder structure" model (Kdenlive) are three container implementations of the same persistent-project concept.

## Rejected Findings

- **"Video Editor = professional production machinery"** — rejected as definitional. Proxy/conform pipelines, professional camera formats, broadcast delivery, facility interop are the professional cluster's standard capabilities (NLE pass), not the Type's invariant; consumer editors are fully in-Type without them.
- **"Video Editor = templates and one-tap AI"** — rejected as definitional. Template flows are a consumer-segment philosophy variant; Kdenlive and Resolve ship no template-first mode and are squarely in-Type.
- **"Video Editor = multi-track timeline with rigid tracks"** — rejected; tracks are the common implementation of layering, not the invariant (the NLE pass already established the trackless magnetic variant; iMovie's connected-clip model and CapCut's multi-timeline drafts show further container variation).
- **"Video Editor = keyframe animation"** — rejected as universal; 3/4 sampled products document general keyframes (iMovie exposes motion effects without a general keyframe editor). Held common, not invariant.
- **"Video Editor = direct social export"** — rejected as definitional; 2/4 sampled document it; export-to-file satisfies the terminal step.
- **"Video Editor = subscription software"** — rejected; business model spans bundled-free, GPL, free-tier, one-time, subscription.
- **"Mobile template editors are a different Type"** — rejected on the evidence: the sampled mobile-first product documents drafts, multi-timelines, clips, masks, keyframes, multicam — the paradigm is intact beneath the template layer.

## Boundary Findings

**vs Non-linear Editing System / NLE (§04.06 sibling — JOINT REVIEW DISCHARGED from this side).** The NLE pass recorded: "the non-linear editing paradigm is shared by professional AND general/consumer timeline editors alike… the two leaves likely denote one underlying Type with a segment gradient (possible alias/variant relationship rather than two independent Types); joint review recommended when the Video Editor leaf is processed." This pass's independent evidence **confirms** that reading from the general-market side:

1. The Level 0 abstraction derived from four general-market products (consumer, mobile-first, open-source, free-tier professional) is *identical* to the NLE pass's Level 0 derived from three professional products — same four properties, same remove-tests.
2. Lexical evidence runs both directions: the open-source general editor self-labels "KDE **Non-Linear** Video Editor" (the paradigm term is not professional-exclusive), while the professional suite self-labels "**professional** non-linear editor" (the *professional qualifier*, not the paradigm, is the differentiator).
3. The consumer pole implements the paradigm fully: iMovie documents addressable clips, arbitrary-order timeline, non-destructive trim with unused-portion preservation, split edits, preview, export; CapCut documents drafts, multi-timelines, masks, keyframes, multicam.
4. What differs is production machinery and segment context (proxy/conform, professional formats, finishing depth, facility interop, hardware I/O, long-form scale) — exactly the NLE pass's finding, now confirmed from the other side.

**Resolution recorded:** the two directory leaves denote **one underlying Application Type** — the timeline-based non-linear video editor — with a segment gradient. "Video Editor" is the general term (this document defines the Type on the paradigm and documents the professional machinery as the professional cluster's standard capabilities); "NLE" is the market's professional-cluster term for the same Type. Recommendation for the taxonomy owner: consolidate at the next §04.06 review — either merge the leaves (alias) or hold NLE explicitly as the professional-segment variant of Video Editor. No directory change made from this side.

**vs Collaborative Video Editor (§04.06 sibling, processed)** — the prior pass's seam holds from this side: a shared persistent project with identified members and coordinated multi-user editing. Remove the shared-project coordination → a complete single-user editor (this Type). Notably, Resolve's *free* version includes multi-user collaboration — collaboration is a capability gradient inside editing products, which is why the collaborative pass held the seam on products *centered* on the team workflow.

**vs AI Video Editing Application (§04.21, processed)** — the locus-of-execution seam holds: in this Type the human executes every edit (AI features are one-tap aids inside a human-executed workflow — all four sampled products conform); in the AI Type the system executes edits as the primary interaction. The sampled CapCut's auto rough-cut (智能解说粗剪) is the deepest AI posture observed inside this Type and still leaves the timeline as the user's working surface.

**vs Motion Graphics Application** — this Type assembles existing footage into a program; motion graphics creates animated graphic content. Titles/effects/generators appear inside editors as timeline elements — support, not the primary object.

**vs Visual Effects Compositing / Video Compositing Application** — compositing constructs shots from layers/node graphs at shot level; this Type assembles programs from shots at program level. The video-compositing pass itself classified VSDC (a compositing-capable non-linear editor) as video-editor territory — consistent with this seam.

**vs Digital Audio Workstation** — a DAW's timeline is audio-centric with mixing as the primary job; this Type's timeline is program-centric with audio in support. Suites embed DAW-class audio pages (Fairlight) as distinct workspaces — the market itself treats them as distinct disciplines.

**vs Media Asset Management (§27)** — MAM is custody/metadata/lifecycle of media collections without timeline editing; the editor's media layer exists to serve the edit. Remove the timeline edit → MAM territory.

**vs slideshow / photo-to-video tools** — a slideshow maker arranges stills into a fixed-output sequence without addressable clip editing (no trim of arbitrary footage, no layered program assembly). Kdenlive documents automatic clip creation from picture directories *as a capability inside* the editor — capability presence does not collapse the boundary; the absence of the clip-trim-timeline model does. Remove addressable-clip editing → slideshow territory.

**vs standalone clip trimmers / quick-cut tools** — no layered timeline, no program assembly; single-clip in/out marking and export. Remove layered assembly → trimmer territory.

**vs social platforms' built-in creation tools (Short-form Video Social Platform, processed)** — the platform's creation loop serves publication into a feed (the short-form pass documented capture+edit as the feed's supply machinery); this Type's deliverable is the program file itself, platform-neutral. Products drift toward the social Type when the feed, profile, and circulation become the primary surface.

**vs linear tape editing (historical)** — fails the defining core by design (no addressable clips, no arbitrary-order assembly, destructive). The Type is defined against it; the historical check below confirms era-robustness.

## Historical / Market-Sample Check

- **2000s consumer editors** (the iMovie/Windows-Movie-Maker generation): project, clip shelf, timeline with a couple of tracks, drag-edge trim, titles/transitions, share-to-web/file export — all satisfy the defining core. The core is era-robust at the consumer pole.
- **Early-1990s professional NLEs** (the founding generation, per the NLE pass): bins, timeline, non-destructive trim, rendered output — same core. The paradigm has been the Type's spine across both segments for three decades.
- **Tape-era linear editing**: fails the core — correctly outside the Type (this is what "non-linear" named the break from).
- **Platform-native and regional products**: iMovie (platform-native) and 剪映 (China-market-first, with an international sibling) both satisfy the core — no region- or platform-specific requirement survives the check.
- **Mobile-first template editors**: satisfy the core structurally (drafts, timelines, clips, keyframes documented) — the template layer is philosophy, not paradigm.
- No cloud/AI/subscription/track-count/social-export requirement survives the check; none is in the defining core.

## Uncertainties

- CapCut international (capcut.com) feature parity with 剪映 is unverified (geo-redirect + 404; same limitation as the ai-video-editing-application pass). Claims about CapCut rest on the official Chinese desktop product page.
- CapCut's export targets and mobile template-flow mechanics are not documented on the fetched page — no claims made.
- iMovie's iOS/iPadOS edition was not fetched; mobile-iMovie specifics (e.g., Magic Movie/storyboard modes) are not claimed.
- Adobe Premiere Pro remains unverified (unreachable in two prior passes; not retried) — no claims.
- iMovie's exact keyframing depth is not documented in the fetched pages (motion effects documented; a general keyframe editor not mentioned) — keyframes held common-not-universal on 3/4 evidence.
- Whether the taxonomy owner will consolidate the Video Editor and NLE leaves (merge/alias/variant) is deferred — recorded as the discharged joint review, no directory change made.
- The exact boundary behavior of hybrid products that bundle generation + editing (CapCut's 营销成片) is a gradient; classified by primary interaction (human-executed timeline editing present → in-Type; system-executed generation as the primary flow → AI Video Generator territory).

## Final Synthesis

A **Video Editor** is an application that assembles recorded footage into a finished video program. Its defining core is the non-linear editing paradigm held in a persistent project: source media is imported as individually addressable clips; the editor places clip instances along a timeline in arbitrary order, layered so picture and sound play simultaneously; every trim, cut, and arrangement operation is non-destructive — it changes the edit, never the source media, and unused portions of clips remain available; the assembled program is previewed in real time and rendered out as a deliverable (file, platform upload, or disc/master output). Around that spine, mature products across the market share a recognizable capability set: a media organization layer (libraries/bins with search and ratings), dual source/program monitoring, transitions, titles, multi-track audio with fades and enhancement, color correction, keyframe animation, project settings with media conform, and export machinery — with AI-era assistance (one-tap enhance, transcription, smart search, auto rough-cut) now common across segments.

The market realizes this one Type as a segment gradient: consumer platform-native editors (free with the platform), mobile-first template/AI-forward editors, open-source desktop editors, free-tier professional suites, and the professional cluster the market calls "NLE" — all implementing the same paradigm, differing in production machinery, philosophy (timeline-first vs template-first), form factor, and business model. The joint review delegated by the NLE pass is discharged: the two leaves denote one underlying Type; the professional machinery, not the editing model, is what the market treats as the difference.
