# Research Notes — Storyboard Application

Research date: 2026-09-10
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Storyboard Application really is from real products: the unit of record (panel? board? frame?), how narrative structure is organized, where panel images come from (drawing, libraries, AI, paper), what captions carry, how boards are reviewed and approved, what leaves the application, and — above all — how this Type is separated from the sibling leaf Previsualization Application, which shares the panel object, scene/sequence grouping, and increasingly the animatic. This pass also owns the JOINT REVIEW FLAG recorded by the previsualization-application pass (2026-09-08): candidate discriminator = center of gravity (drawn-board narrative craft vs staged-scene/camera-blocking planning); decision reserved for this pass.

## Initial Boundary (hypothesis before research)

- What: software for planning visual stories (film/TV/animation/commercials/video) as an ordered sequence of framed images with captions — the board — before production; used for pitching, approval, and on-set reference.
- Users: storyboard artists, directors, agency creatives/producers, animators, writers, educators/students.
- Nearest neighbors: Previsualization Application (sibling leaf — the animatic and "storyboard" labeling overlap), 2D Animation Application (both draw panels, but storyboards are static planning), Script Breakdown Application (script-driven pre-production, but inventories elements, not images), Production Scheduling / Call Sheet (consumes boards), Film Production Management (production office vs creative board), UX Prototyping (previsualization of interfaces, not scenes), generic design/template platforms.
- Open questions: Is the caption (dialogue/action/shot notes) definitional or common? Is playback/animatic part of this Type or the shared overlap zone with previz? Is drawing-in-product definitional (Boords/Storyboard That suggest not)? Where does the education/communication pole (storyboards as generic visual storytelling) sit relative to production storyboarding? Does a standalone "animatic assembly" product population exist (sibling pass secondary note)?

## Research Questions

1. What is the unit of record — panel, frame, board, cell? What does it contain (image + what text)?
2. How is narrative structure organized (scenes, sequences, shots, grids, groups)?
3. How do panel images come into existence (draw, compose from libraries, import/scan, photograph paper, AI generate)? Is drawing-in-product required?
4. What do captions carry (action, dialogue, camera/shot notes, timing)? Are captions definitional?
5. How does the review/approval loop work (links, comments, statuses, versions, sign-off)?
6. What leaves the application (PDF/print, images, movie/animatic, presentation links, shot lists, NLE files)?
7. What enters the application (scripts, paper worksheets, PSD, stock images)?
8. Does the animatic belong to the core, or is it an extension? Which sampled products lack it entirely?
9. Who uses it and at what tier (studio, agency, indie, education, corporate)?
10. Where exactly does the Storyboard/Previsualization seam run, and does a standalone animatic-assembly population exist?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Evidence quality |
|---|---|---|---|
| Toon Boom Storyboard Pro | board-first craft: drawn panels, captions, timeline animatic as extension; the industry-standard straddler | enterprise studios/animation/TV professionals | A (product page + Help Centre KB category fetched this pass; deep KB/articles first fetched by sibling previsualization pass 2026-09-08 and quoted there) |
| Boords | web SaaS: boards as client-review documents; scripts/shot lists/animatics/approval workflow around the board; no drawing canvas | video agencies & brand teams | A (homepage + storyboard-software feature page, richly functional) |
| Storyboarder (Wonder Unit) | free open-source desktop: "a drawing organizer" — draw, order, share; paper worksheet round-trip; Shot Generator as optional aid | indie filmmakers/writers/advertisers (free) | A (official product page is a full functional description) |
| Storyboard That | audience-variant pole: storyboard-form creator repurposed for education/comics/business communication; compose-from-art-library, no drawing | K-12 education (primary), personal, teams | A (homepage + creator description) |
| StudioBinder | suite-embedded module: storyboard inside a pre-production platform (script → breakdown → visualize → plan → shoot) | professional production teams, schools/enterprise | A (storyboard-software feature page + platform structure) |

Stop condition reached at five products: the core model is stable, cross-product commonalities repeat, and additional products would mainly re-confirm existing evidence.

## Sources

Fetched 2026-09-10 (this pass):

- Toon Boom — Storyboard Pro product page: https://www.toonboom.com/products/storyboard-pro
- Toon Boom — Storyboard Pro Knowledge Base (category root; sections list): https://helpcentre.toonboom.com/hc/en-ca/categories/39971055086995
- Boords — homepage: https://boords.com/
- Boords — Storyboard software feature page: https://boords.com/storyboard-software
- Wonder Unit — Storyboarder product page: https://wonderunit.com/storyboarder/
- Storyboard That — homepage/creator description: https://www.storyboardthat.com/
- StudioBinder — Storyboard software feature page (incl. platform solution map + FAQ): https://www.studiobinder.com/storyboard-software/

Cited from sibling previsualization-application pass (fetched 2026-09-08, quoted in research/previsualization-application.md):

- Toon Boom — Storyboard Pro Online Help: https://docs.toonboom.com/help/storyboard-pro-27/storyboard/index.html
- Toon Boom — KB articles: panels/scenes/sequences; Animatic; About the 3D space; AAF/XML/EDL vs Conformation; About the Camera
- FrameForge / Shot Designer / Previs Pro official pages (used only for the seam adjudication from the previz side)

## Product Observations

### Toon Boom Storyboard Pro (evidence layer A)

- Positioning: "The only professional-grade solution designed from the ground up to support the craft of storyboarding. Whether you are thumbnailing your first pass, refining the visual storytelling on your project, pitching your boards or timing out camera moves in an animatic…" Audience: "independent storytellers, studios, agencies, videographers and video production teams."
- KB structure (this pass, category root): the narrative-structure section is titled "Panels, scenes and sequences — All about the building blocks that create the narrative structure of your storyboard"; thumbnails workflow ("How can I make a page of thumbnails for rough sketching?", "How do I turn my thumbnails page into panels?"); drawing tools (vector/bitmap); layers; onion skin; **Animatic** section: "Add movement, timing and camera motion to your storyboard using the Timeline view" (the animatic is presented as something added TO the storyboard); Effects; Sound; 3D (import/manipulate 3D models; vendor states elsewhere the product is "predominantly a software for creating 2D visuals" with optional 3D per scene); Project management and conformation ("share the workload, and conform your project to third-party softwares").
- New-feature page content (this pass): Panel Timer records panel timing live "by tapping while you perform dialogue and actions," two modes (Create New Panels / Apply to Selection), audio optionally recorded and imported into the Timeline; Photoshop import preserving clipping masks and 24 blending modes — evidence that boards are commonly finished/polished in external paint tools and imported.
- From sibling pass (Tier-1, 2026-09-08): camera as a frame matching project aspect ratio with keyframed moves per panel or per scene; sound editing with fades; AAF/XML/EDL export (one-way into NLEs) vs Conformation (round-trip: "Panels become clips… Panel captions become clip metadata… ideal for workflows that have a lot of back and forth between the storyboard and animatic processes").
- Reading: the industry-standard board tool centers on drawn panels + captions + scenes/sequences; the animatic timeline, sound, camera moves, and NLE conformance are the craft's professional extension layer — but the product's own KB organizes the animatic as an add-to-the-storyboard section, and the 3D space as optional.

### Boords (evidence layer A)

- Positioning: "The pre-production platform loved by video agencies & their clients. Create Scripts, Storyboards and Animatics with your team. Share work with clients, collect feedback, and get sign-off before production begins." Tagline: "The most painful part of video production, made painless."
- Review loop as the product's center of gravity: secure presentation links with passphrase protection and no-login client review; frame-level comments and annotations; approval/status labels on frames ("Know what's approved at a glance"); version history ("Create new versions with comments intact and quickly restore previous work"; activity feed of status changes); 1M+ projects shared with clients, 12M+ comments (vendor figures — not independently verified).
- Planning around the board: script editor side-by-side with frames; "Convert storyboards into detailed shot lists with custom fields"; custom metadata fields per frame saved as team templates; shot list view "with camera angles and scene descriptions generated from a storyboard."
- Panel images without drawing: "Bring your own images, or use AI-powered tools to turn text prompts into consistent storyboard images… build a consistent cast of characters"; 3M+ stock images/icons; upload team assets; AI doodle→polished-frame generation.
- Animatic as one-click extension: "Boords turns the board into a timed animatic in one click, so pacing gets signed off before anyone opens an editor"; animatic player with audio; MP4 export.
- Exports: "PDFs, images, shot lists, scripts, and more."
- Public API object model (from homepage API listing): projects → storyboards → frames → comments; teams/members; webhooks ("Storyboard updated" events).
- Founder origin: built in 2015 at an animation studio because boards were previously made in "Photoshop. Or Google Slides. Or InDesign" with version chaos — i.e., the product exists to turn the board into a managed, reviewable document.
- Reading: the board is a structured document (ordered captioned frames) whose value loop is review/approval; no drawing canvas, no staging space, no camera machinery beyond shot-list fields; animatic = one-click timing preview of the board.

### Storyboarder / Wonder Unit (evidence layer A)

- Positioning: "The best way to visualize your story… Storyboarder makes it easy to visualize a story as fast you can draw stick figures. Quickly draw to test if a story idea works. Create and show animatics to others. Express your story idea without making a movie." Free and open source.
- Founder's own reduction: "Storyboarder, at the highest level, is a drawing organizer. It makes drawing and ordering drawings simpler. You could do this with a stack of paper and a pencil."
- Board mechanics: six drawing tools (light pencil, hard pencil, pen, brush, note pen, eraser); "Add a board. Draw. Add another. Draw. Duplicate. Copy. Paste. Rearrange."; per-board metadata panel: "Enter dialogue and action… You can also enter timing information and shot type"; onion skin; reference layer; guides; track changes; comprehensive key commands.
- Paper round-trip: print storyboard worksheets → draw on paper → photograph with phone → automatic import into the project (the analog-to-digital bridge).
- External-editor round-trip: "Edit in Photoshop… Once you save, it will automatically update in Storyboarder" — the board as an organizing layer over external craft tools.
- Shot Generator: type a description → generated shots "meant to be drawn over so they can be used as a guide," placed in the reference layer — generative imagery as drawing aid, not as blocked scene.
- Exports: Premiere, Final Cut, Avid, PDF (contact sheet), Animated GIF; Fountain script support ("Works with Fountain"); Sketch Sprint timed drawing with timelapse GIF for sharing.
- Reading: the purest board-first pole — organizing drawings into an ordered, captioned, shareable sequence; animatics exist ("Create and show animatics to others") as a share output; no staging space, no camera blocking; the "shot" appears as metadata (shot type/timing), not as a staged camera view.

### Storyboard That (evidence layer A)

- Positioning: "Free Storyboarding Software — Online Storyboard Creator… Digital Storytelling — Powerful Visual Communication, Made Easy." Primary market: education (Teacher Edition, 3,000+ lesson plans, FERPA/CCPA/COPPA/GDPR compliance, LMS rostering with Google Classroom/Clever/Canvas/ClassLink/Schoology, ESSA Level IV efficacy review); also Personal and Teams/Business editions.
- Creator: drag-and-drop composition; free tier "3 Cells"; building blocks: scenes, characters, items, speech bubbles, shapes, infographics, web & wireframes; vast art library, no drawing required ("makes it easy to create storyboards even without being an artist").
- The storyboard form extends to adjacent artifacts from the same creator: comics/graphic novels, book maker, posters, worksheets, timelines, plot diagrams — evidence that at the audience pole the storyboard grid is a general visual-storytelling document.
- Output: "Share your storyboard with others online, or download it as a high resolution image or PDF"; real-time collaboration (students in pairs/groups; teacher views student work in real time); assignment workflows.
- Reading: the panel-grid narrative form survives far outside production — classrooms use the same structure (ordered framed cells with text) to plan/retell stories. No animatic, no camera/shot machinery, no production loop; the "board as shareable artifact" leg persists (share online, download, present).

### StudioBinder (evidence layer A)

- Positioning: storyboard module inside "the industry's leading video, film, and TV production platform"; the platform's solution map runs Write (screenplays/AV scripts) → Breakdown (script breakdowns/sides/stripboards) → **Visualize (Storyboards / Shot Lists / Mood Boards)** → Plan (contacts/calendars/tasks) → Shoot (call sheets/locations). "Visualize the script to get everyone on the same page."
- Script-to-board machinery: import screenplay; "StudioBinder's storyboarder software links each scene to its own board"; **Shot Tagger**: "Highlight a line of action or dialogue and instantly generate a matching storyboard panel."
- Shot specs on panels: "a full set of built-in shot specs and layout options. From camera movement to framing and shot type"; aspect ratios; shot numbering (digits/letters/custom); column layouts.
- Image workflow: "Scan or upload sketches, enhance them with filters, and add arrows, shapes, or text" (image editor); image library to "reuse storyboard panels from previous projects."
- Organization: "Storyboards based on location, scene, or shoot day"; storyboard archive "to keep an accessible history"; color-coded specialty shots.
- Collaboration/output: real-time team editing, feedback, task assignment; view-only share links; customizable PDF export (headers, layouts, padding, colors, watermarks, password protection).
- FAQ positioning: storyboards as "a shorthand for your crew"; lists Boords, Storyboarder, Canva as the storyboard-artist alternatives.
- Reading: the board is one planning document inside the production chain — script on one side, shot lists/scheduling/call sheets on the other; no animatic playback evidenced on the page (unknown, not asserted absent); no staging space.

## Cross-product Comparison

| Dimension | Storyboard Pro | Boords | Storyboarder | Storyboard That | StudioBinder |
|---|---|---|---|---|---|
| Unit of record | Panel (drawn frame) + caption fields | Frame (image + caption/custom fields) | Board (drawing + dialogue/action/timing/shot type) | Cell (art-library scene + speech/text) | Panel (image + shot specs) |
| Narrative structure | Panels → scenes → sequences | Ordered frames in storyboard (script scenes alongside) | Ordered boards; Fountain script scenes | Ordered cells in templates/grids (scene templates, plot diagrams) | Boards linked to script scenes; groups by location/scene/shoot day |
| Panel image source | Draw in-product (vector/bitmap); PSD import; 3D models optional | Upload, stock library (3M+), AI generate, AI doodle→polish | Draw in-product; Photoshop round-trip; paper photo import; AI Shot Generator as reference | Compose from art library (drag-and-drop); no drawing | Scan/upload sketches + annotate; image library reuse |
| Captions | panel captions (become clip metadata in conformance) | captions + custom metadata fields | dialogue + action (+ timing, shot type) | speech bubbles, text blocks | shot specs (movement, framing, shot type) |
| Ordered-sequence machinery | panel strip + thumbnails→panels workflow | drag-to-reorder frames; versioning | add/duplicate/copy/paste/rearrange boards | cell layouts, copyable templates | scene-linked panels; groups; numbering |
| Review/present | pitch boards; project management + conformation to share workload | center of gravity: links, frame comments, statuses, approvals, versions, activity | export GIF/PDF; Sketch Sprint timelapse share | share online, download, present; real-time collaboration; assignments | view-only links; team feedback; task assignment; PDF w/ watermark/password |
| Animatic/playback | full: Timeline view, camera moves, sound, movie export (+Panel Timer live timing) | one-click timed animatic w/ audio; MP4 | "create and show animatics"; GIF export | none | none evidenced (unknown) |
| Script integration | script-based scenes/captions; (conformation context) | script editor side-by-side; scripts as objects | Fountain support | none | screenplay import; Shot Tagger line→panel |
| Production artifacts out | PDF boards; movie w/ burn-ins; AAF/XML/EDL; Conformation | PDF, images, shot lists, scripts, MP4 | Premiere/FCP/Avid, PDF contact sheet, GIF | high-res image, PDF, social/PPT | PDF (styled), shot lists, view links |
| Staging space / camera blocking | none (camera = aspect-ratio frame; optional 3D model import) | none | none (Shot Generator = reference images) | none | none (shot specs are fields, not staged views) |
| Audience | studios/agencies/professional board artists | video agencies & brand teams (client review) | indie/writers/advertisers (free) | education (primary), personal, business | production teams, schools/enterprise |
| Platform | Windows/macOS desktop | web SaaS (+API/webhooks) | desktop, free/open-source | web | web (suite) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Storyboard Application is recognizable when all three of the following hold:

1. **The panel as the unit of record — a framed image plus its caption.** The board cell pairs a picture (drawn in-product, composed from artwork, imported/photographed, or generated) with text (action notes, dialogue, shot/camera notes — the exact fields vary). Remove the image → a script or outline; remove the caption → a picture strip; either fragment stops being a storyboard cell.
2. **Ordered narrative sequence organized above the panel.** Panels sit in story order, grouped by an organizing layer (scenes/sequences, script scenes, template grids). The board reads as the story played out frame by frame. Remove → an image gallery or a strip of unordered frames.
3. **The board as a reviewable, distributable artifact.** The sequence leaves the application — presented, shared, printed, or exported (PDF/images/movie/link) — for people outside the tool to read, comment on, and approve. Remove → a private thumbnail sketchbook; a slideshow tool with no panels.

Jointly-held is load-bearing: 1 alone = a drawing canvas or comic-cell editor; 2 alone = a shot list/outline; 3 alone = a presentation tool; 1+2 without 3 = a thumbnail notebook below the application bar; 1+3 without 2 = a photo collage; 2+3 without 1 = a slide deck. The three legs constitute one loop: make panels → arrange the story → show the board for review before production.

### L1 — Common Mature Structure

Present across most of the sample, not definitional:

- **animatic/playback** — timing the board into a rough moving preview (Storyboard Pro full timeline+camera+sound; Boords one-click with audio; Storyboarder animatics/GIF). Absent at the audience pole (Storyboard That) and unevidenced in StudioBinder — so common, not invariant. This is the shared overlap zone with Previsualization.
- **script integration** — script scenes as the board's organizing skeleton (StudioBinder import+Shot Tagger; Boords side-by-side; Storyboarder Fountain; Storyboard Pro captions/scenes). Absent in Storyboard That.
- **shot/camera notes as fields** — shot type, framing, aspect ratio, movement recorded per panel (StudioBinder, Storyboarder, Boords shot lists, Storyboard Pro aspect frames). Storyboard That lacks them.
- **asset sources & image workflow** — art/stock libraries, upload/scan, external-editor round-trips (Photoshop), reuse libraries, paper-photo import.
- **sharing/review/approval** — links, comments, statuses, versions, real-time collaboration; the intensity varies from Boords' approval workflow to Storyboarder's export-only.
- **templates** — storyboard templates (layouts, aspect ratios, column counts, education templates).
- **PDF/print as the canonical artifact format** — every sampled product prints or exports PDF/images (worksheets, contact sheets, styled PDFs).

### L2 — Variant / Optional Structure

- **panel-image substrate as product philosophy**: craft-drawn (Storyboard Pro, Storyboarder) vs composed-from-library (Storyboard That) vs sourced/uploaded/AI (Boords, StudioBinder); external-editor round-trips and paper scanning as bridges.
- **animatic depth**: none → timed playback with audio → camera-move timeline + sound + NLE conformance.
- **AI assistance**: prompt-to-image panels, consistent characters, doodle→polish, Shot Generator (Boords, Storyboarder, Toon Boom Ember add-on) — era-current optional.
- **audience variant**: production boards (film/TV/commercials) vs education/visual-storytelling boards vs corporate communication (Storyboard That's lesson plans; Storyboard That business templates) — the form survives without the production loop.
- **collaboration model**: client-approval workflow vs team editing vs classroom assignment vs single-user export.
- **packaging/tier**: standalone web SaaS (Boords), standalone desktop craft tool (Storyboard Pro), free open-source (Storyboarder), suite module (StudioBinder), education platform (Storyboard That); free-tier gating varies.

### L3 — Vendor-specific (research notes only)

- Storyboard Pro: Panel Timer modes (Create New Panels / Apply to Selection), thumbnails→panels workflow, PSD clipping-mask/blending-mode import (24 modes mapped to Effect Stack), Ember AI add-on, Conformation round-trip field mapping, 3D multiplane.
- Boords: approval statuses/no-login client review, version tree with comment retention, public API object model (project→storyboard→frame→comment) + webhooks + Slack, Script Timer, cast-consistency AI, founder origin story (Animade; "Photoshop/Slides/InDesign" pain), vendor usage figures (1M+ projects, 12M+ comments).
- Storyboarder: paper worksheet photo-import, Sketch Sprint + timelapse GIF, line-mileage measuring, track changes, Command+K, free-software manifesto/positioning attacks on paid rivals.
- Storyboard That: comic maker/book maker/poster/worksheet/timeline siblings from one creator, 3-cell free tier, LMS rostering, ESSA Level IV evidence, FERPA/COPPA/SOC-2 posture.
- StudioBinder: Shot Tagger (script line → panel), groups by shoot day, PDF watermark/password, archive, color-coded shots, shot-numbering schemes, suite integration (breakdown/stripboard/call sheets).

## Rejected Findings (not promoted to core)

- "A staging space / camera blocking defines the Type" — **rejected**: no sampled storyboard product stages a scene in space. Storyboard Pro's camera is an aspect-ratio frame (3D models optional); Boords/StudioBinder/Storyboard That have no spatial staging at all; Storyboarder's Shot Generator produces reference images to draw over, not a blocked set. This is the decisive evidence for the previz seam (see Boundary Findings).
- "Animatic playback defines the Type" — rejected: absent in Storyboard That, unevidenced in StudioBinder; products remain clearly storyboard tools without it. Common mature structure (L1) and the previz overlap zone.
- "Script binding defines the Type" — rejected: Storyboard That has none; Boords side-by-side is optional. L1.
- "Drawing-in-product defines the Type" — rejected: Boords and StudioBinder ship no drawing canvas (upload/scan/compose/AI), Storyboard That composes from art. The panel image is definitional; how it is produced is a variant (L2).
- "Aspect-ratio camera frames define the Type" — rejected as invariant: widespread (Storyboard Pro, StudioBinder, Boords templates, Storyboarder shot types) but Storyboard That's cells are free-layout comic-style cells. L1.
- "Client approval workflow defines the Type" — rejected: only Boords centers it; Storyboarder exports files. L1/L2.
- "AI generation defines the Type" — rejected: era-current optional in 3/5, absent in 2/5.
- "The caption is always dialogue+action" — the fields vary by product (action/dialogue vs shot specs vs speech bubbles); the caption's existence is L0, its taxonomy is L1/L2.

## Boundary Findings

- **vs Previsualization Application (sibling leaf §04.19) — JOINT REVIEW DISPOSITION**. The flag from the previz pass (candidate discriminator = center of gravity; keep-both recommended) is **RATIFIED from this side; keep-both**:
  - Storyboard-side evidence: across five storyboard products there is **no representational staging space and no camera-blocking machinery** — the exact L0 leg-2 of previz is absent from this Type's sample. Conversely, all five order captioned panels and ship boards as review artifacts — previz's outputs.
  - Previz-side evidence (sibling pass): previz products center on the blocked scene (staged space, snapped camera setups, coverage) and playback as the evaluation act, with boards as one output among several (FrameForge exports PDF storyboards; Previs Pro self-labels "Storyboard Software").
  - Center-of-gravity test applied to the straddler: Storyboard Pro carries a full animatic timeline + camera + sound + conformation, yet its own KB organizes everything as "Panels, scenes and sequences — the building blocks that create the narrative structure of your storyboard," the animatic section is phrased as something added *to* the storyboard, the vendor positions it as "the craft of storyboarding," and it has no staging space. Board-centered → Storyboard Type, with deep animatic extension. Previs Pro's "Storyboard Software" self-label is marketing straddle; its center (staged 3D scene, camera setups, LiDAR/AR) is previz.
  - Recorded seam test from the sibling pass — "remove staging/camera-blocking machinery and playback → a board layout tool (storyboard)": **confirmed**; the sampled storyboard products live exactly there. The converse ("remove drawn-panel authoring as the center → previs") is consistent.
  - Secondary note (2) of the sibling pass — standalone "animatic assembly" software (arbitrary imported frames timed into playback, seam test 1+3 without 2): **no such product population surfaced in this pass's sample**; every sampled playback machinery builds on the board itself (Boords: "turns the board into a timed animatic in one click"). The test was not triggered by a real product; the question stays open at the market frontier.
  - The animatic is declared the **shared overlap zone**: L1 in both Types; its depth (one-click timing vs camera-move timeline with conformance) is where individual products straddle, not where the Types divide.
- **vs 2D Animation Application** — storyboards are static planning panels with captions; animation adds the frame-by-frame authored performance and delivers a moving work. The 2D-animation pass already recorded the same seam from their side ("storyboards are static planning panels… market treats them as different tools"). A storyboard product's animatic is a timing preview of the board, not an authored performance.
- **vs Script Breakdown Application** — breakdown inventories production elements per scene (cast/props/wardrobe); storyboards picture the shots. Complementary script-driven pre-production deliverables; StudioBinder ships both as modules of one platform, which is bundling, not identity. The script-breakdown pass recorded the same seam from their side.
- **vs Production Scheduling / Call Sheet Application & Film Production Management** — boards feed the schedule (StudioBinder groups storyboards by shoot day; call-sheet workflows attach storyboards as reference); the production office consumes boards but does not author them. Different objects (shoot days/scenes/call sheets vs panels).
- **vs comic/graphic-novel creation tools (no directory leaf)** — Storyboard That's creator makes comics, posters, books from the same cell machinery; at the audience pole the storyboard grid and the comic page converge. The production distinction (planning artifact vs published work, shot semantics vs speech-balloon layout) holds at the professional pole but is genuinely porous at the education/consumer pole. No taxonomy action (no comic-maker leaf exists to collide with).
- **vs general design/template platforms** — StudioBinder's own FAQ lists Canva among storyboard-artist alternatives: a layout tool can assemble framed images, but lacks panel/scene/shot semantics, script linkage, and the production review loop. The storyboard objects, not the layout capability, define this Type.
- **vs UX Prototyping Application** — both previsualize before building; the storyboard's panels picture filmed/animated scenes for a production audience, the prototype simulates an interactive interface. No shared machinery beyond the general idea (same conclusion as the previz pass).
- **vs shot-list-only tools (no directory leaf)** — both sampled suite products ship shot lists as companion/derived artifacts (Boords: storyboard → shot list conversion; StudioBinder: Shot Lists as a sibling solution). The shot list alone (no panels) sits below this Type — mirrors the previz pass's below-Type note.

## Historical / Market-Sample Check

Analog storyboarding practice (conceptual, per §24):

- **Paper boards (the tradition since the 1930s studio system)**: framed drawings with captions (action/dialogue underneath or beside), pinned/paged in scene order, presented to the room, revised, and shipped as the production's plan of record. Leg 1 (framed image + caption), leg 2 (ordered scenes), leg 3 (the board shown to readers/approvers) — all satisfied without any digital machinery.
- **Thumbnail passes**: rough sketchbook stages are working drafts *within* the practice; the analog equivalent of leg 3 is the board that eventually gets pinned/presented. The check confirms leg 3 as the application-level bar (a notebook of thumbnails is storyboarding practice but not yet the artifact of record).
- **Playback as optional then too**: the Leica reel (timed boards filmed with temp sound) was the analog animatic — an extension made *from* the board for timing/pitch purposes, exactly the L1 relationship this pass found in digital products. Its historical presence as optional supports keeping playback out of the definition.
- Modern digital forms (craft-drawn desktop, web SaaS review boards, library-composed education boards, AI-assisted panels) all satisfy the three legs; the definition names no era machinery (no drawing engine, no web, no AI, no cloud).

Historical check: **passed** — the analog practice satisfies the core, so the definition is substrate- and era-agnostic.

## Uncertainties

- StudioBinder's animatic/playback capability is unevidenced on the fetched page — recorded as unknown; no claim either way is made in the final document.
- Boords evidence is product/feature pages, not the in-app help center; the API object model was read from the homepage's API listing. No precise limits (frame counts, plan caps) were researched or asserted.
- Storyboard That's deep creator behavior (exact cell/scene semantics for storyboard-templates vs comics) was not fetched beyond the homepage/creator description; treated as the audience-variant pole at description strength.
- Toon Boom deep KB article content is cited from the sibling previsualization pass (fetched 2026-09-08, quotes recorded there); this pass re-verified the product page and the KB category structure first-hand (2026-09-10). Assertion strength kept at the recorded quote level.
- The standalone animatic-assembly population (sibling pass secondary note) was not found in this sample; the market frontier remains unchecked rather than confirmed empty.
- Dedicated storyboard products not sampled (e.g., PowerProduction Storyboard Artist/Quick, Plot): five-product stop condition reached on stable evidence; they are not claimed to contradict any finding.
- Vendor usage figures on Boords' homepage (1M+ projects, 12M+ comments, 3M+ stock images) are marketing numbers, recorded but not relied upon.

## Final Synthesis

The Storyboard Application is the board-maker of pre-production and visual storytelling: its unit of record is the panel — a framed image paired with a caption — panels are arranged in story order under a scene/sequence organizing layer, and the finished board leaves the application as a shareable, reviewable artifact (presented, printed, exported) that clients, crews, studios, or classrooms read and approve before production. Mature products commonly add the animatic (timing the board into a rough moving preview — the shared overlap zone with previsualization), script integration, per-panel shot/camera notes, asset sources (drawing tools, libraries, AI generation, paper import), review/approval workflows with versions, templates, and PDF/print export. Products differ by panel-image substrate (drawn, composed, uploaded, generated), animatic depth, collaboration model, audience (production teams, agencies, education), and packaging (web SaaS, desktop craft tool, free open-source, suite module). The boundaries: Previsualization Application (the sibling seam — ratified keep-both on center of gravity: the storyboard centers on the captioned board as narrative/review document with no staging space; previz centers on the blocked scene in space with playback as the evaluation act; the animatic belongs to both), 2D Animation (static planning vs authored frame performance), Script Breakdown (pictures shots vs inventories elements), production scheduling/management (boards feed the shoot; the office consumes them), comic/design tools (porous at the audience pole, distinct at the professional pole), and shot-list-only tools below the Type. The analog paper-board tradition satisfies the same core, so the definition carries no era, substrate, or collaboration machinery.
