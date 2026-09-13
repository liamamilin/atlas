# Research Notes — Presentation Application

## Research Goal

Understand what a Presentation Application is as an Application Type — the base Type under 03.04 Presentations, whose sibling leaf "Collaborative Presentation Editor" is already processed: the artifact grammar it edits (deck / slide / element), the authoring workflow it supports, how the deck is delivered to an audience, and — most importantly, because the sibling pass pre-hung a joint-review flag — where the boundary sits against the Collaborative Presentation Editor, the Document Editor family, Desktop Publishing, the Digital Whiteboard, Diagramming, design platforms, and the eLearning Authoring Tool.

## Initial Boundary

- The leaf is the presentation-grammar base Type. The sibling pass's Boundary Finding #1 pre-hung the seam: "single-author file with save/pass-around vs shared live deck with concurrent merge. The grammar (deck/slides) is identical; the collaboration layer is the discriminator. Historical check: pre-cloud PowerPoint/Keynote are Presentation Applications, not members of this type." This pass holds the boundary from this side.
- The document-editor / collaborative-document-editor pair is the family precedent: the document-editor pass defined the core as "a self-contained document artifact the author creates/keeps/revisits" and recorded the seam as porous in one direction, with the discriminator "whether the shared live merged document is the primary object." The collaborative-document-editor pass explicitly predicted the same shape for presentations ("Collaborative Spreadsheet/Presentation (same skeleton, different grammar)").
- Working hypothesis: the Type = presentation grammar (ordered slides, bounded spatial slide canvas, delivery to an audience) + the authored-deck document model — with collaboration an added layer in modern products, not a defining property.
- Nearest neighbors: Collaborative Presentation Editor (sharpest seam), Document Editor / Collaborative Document Editor (same authored-artifact skeleton, different grammar), Desktop Publishing / Page Layout (fixed pages, different delivery mode), Digital Whiteboard (unbounded canvas), Diagramming Application (shape+connector semantics), Graphic Design / Template-based Design Platform (deliverable difference; Canva straddle), eLearning Authoring Tool (presenter-driven vs learner-driven — that pass's own recorded discriminator).

## Research Questions

1. What is the core object model? (deck, slide, element, theme/layout, notes)
2. What is the authoring workflow? (create → compose slides → arrange → refine → keep → deliver)
3. Is the deck an authored document (file/cloud document) or a live shared object? (boundary vs sibling)
4. What delivery machinery exists? (slideshow playback, presenter support, export/print/publish/record outputs)
5. What is the theme/template layer and how does it sit relative to slides?
6. What interchange standards exist? (PowerPoint format, PDF, print, HTML, video/GIF)
7. Is collaboration core or layered? What sharing exists in base-Type products?
8. Historical check: do file-era, platform-native, and open-source products satisfy the same core without cloud/collaboration/AI?
9. Where are the boundaries? (documents, DTP, whiteboards, diagrams, design platforms, eLearning, video)

## Representative Products

| Product | Why selected | Evidence level reached |
|---|---|---|
| Microsoft PowerPoint | incumbent standard, office-suite, file-based desktop lineage + cloud-era additions | Tier-1 first-hand this pass: help hub, "Create a presentation" training article, "Print and present" category page (deep article bodies partially reachable — hub links give real article URLs); sibling pass additionally documented collaborate-and-share / slides-and-text category taxonomy |
| Apple Keynote (Mac) | platform-native check, file-first single-author model, deep official docs | Tier-1 deep: full user guide TOC + "Create a presentation" article body |
| LibreOffice Impress | open-source, file-based, no collaboration layer, OpenOffice.org heritage | Tier-1 first-hand: Impress help welcome, Features page, guide index |
| Google Slides | cloud-collaborative-first suite member — sibling-pole anchor | Market anchor only (support.google.com/slides timeout ×1 this pass; sibling pass timeout ×2 + ×1) — no operational claims |
| Canva Presentations | template-first design-platform straddler | Market anchor only (sibling pass: 429 / browser-gated) — no operational claims |

Selection rationale: market coverage across office-suite incumbent / platform-native / open-source poles with three fully documented products; Google Slides and Canva retained as boundary anchors consistent with the sibling pass's treatment.

## Sources

Fetched 2026-09-08 (this pass):

- Apple — Keynote User Guide for Mac (welcome + full TOC): https://support.apple.com/guide/keynote/welcome/mac
- Apple — Create a presentation in Keynote on Mac: https://support.apple.com/guide/keynote/create-a-presentation-tan317e80e8c/15.3/mac/1.0
- Microsoft — PowerPoint help & learning hub: https://support.microsoft.com/en-us/powerpoint
- Microsoft — Create a presentation in PowerPoint: https://support.microsoft.com/en-us/powerpoint/training/create-a-presentation-in-powerpoint
- Microsoft — Print and present (PowerPoint category): https://support.microsoft.com/en-us/powerpoint/print-and-present
- LibreOffice — Impress Help welcome: https://help.libreoffice.org/latest/en-US/text/simpress/main0000.html
- LibreOffice — Impress Features: https://help.libreoffice.org/latest/en-US/text/simpress/main0503.html
- LibreOffice — Instructions for Using LibreOffice Impress (guide index): https://help.libreoffice.org/latest/en-US/text/simpress/guide/main.html

From the sibling pass (research/collaborative-presentation-editor.md, fetched 2026-09-06, cited for cross-leaf consistency):

- Microsoft PowerPoint category pages: collaborate-and-share, slides-and-text, print-and-present
- Pitch help center (collaborative pole); Keynote for iCloud user guide

Attempted and abandoned (network rule):

- https://en.wikipedia.org/wiki/Presentation_program — timeout ×2 (historical external check unavailable)
- https://support.google.com/slides — timeout ×1 this pass (sibling: timeout ×2); Google Slides kept as market anchor only
- Canva — not retried this pass (sibling pass failed twice: 429 + browser gate)
- wiki.documentfoundation.org — bot-gated (Anubis), wrong target anyway; help.libreoffice.org used instead

### Source-access limitations

- No Wikipedia/external historical source reachable: the historical check for the pre-cloud generation (Harvard-Graphics / Lotus-Freelance / WordPerfect-Presentations class) is kept **conceptual** — supported by the Type's own documented continuity (PowerPoint's Applies-To lines span PowerPoint 2016–2024 perpetual editions; LibreOffice's own footer states it "was based on OpenOffice.org") rather than by direct historical sources. No named historical product is claimed beyond this.
- Google Slides and Canva: no operational claims anywhere; used only as universally recognized anchors for the collaborative-first and template-first realizations.
- No numeric limits (slide counts, file sizes, durations, deck dimensions, collaborator counts) are asserted for any product.
- Keynote subscription features (Apple Creator Studio) are documented as subscription-gated in Apple's own text; treated as optional structure.

## Product A — Microsoft PowerPoint

### Key observations (first-hand this pass, evidence A)

Help hub structure (top-level): Get started / Collaborate / Design / Animations / Pictures & charts / **Present** / Slides & text / Copilot in PowerPoint. "Prepare" and "Present" highlight groups: speaker notes, presenting with Cameo, rehearse with Speaker Coach, Live Presentations, Presenter view, Zoom for PowerPoint.

"Create a presentation in PowerPoint" (Applies to: PowerPoint for Microsoft 365, 2024, 2021, 2019, 2016 — the perpetual desktop line is a still-supported current product):

- Creation: Open PowerPoint → side pane **New** → **Blank Presentation** (scratch) or a prepared template, or "Take a Tour".
- Slides: thumbnails in the side pane; select the slide the new one follows → **New Slide**; **Slide Layout** picker for layout choice.
- Text: click inside a text box and type; Font section of the Home tab (font, size, bold/italic/underline); Bullets/Numbering.
- Insert: Pictures (with source picker), Shapes, Icons, 3D Models, SmartArt, Chart.
- Copilot can help create a presentation, add slides or images (separate Copilot article).

"Print and present" category (Applies to: M365 Windows/Mac, 2024, 2021, 2019, 2016):

- Delivery start: "press F5 to start from the beginning, or press Shift+F5 to start from the current slide."
- Articles: Create a self-running presentation; View speaker notes privately while delivering on multiple monitors; Presenter view; Turn your mouse into a laser pointer; Add speaker notes; Print speaker notes; Rehearse and time the delivery; Print slides/handouts/notes.

From the sibling pass (category taxonomy, evidence A for feature existence): Collaborate and share section (share, co-author, comments, track changes, digital signatures, inspect); Slides and text section (add/rearrange/duplicate/delete slides, slide size, orientation, reuse slides, sections, object selection, hyperlinks); Animations section (transitions, Morph, multiple effects per object).

Interpretation: PowerPoint carries the full presentation grammar with an authored-document model (perpetual desktop editions without any cloud dependency remain current products) plus — in the M365 realization — a collaboration layer (co-authoring, comments) as an added section among eight. Delivery machinery (presenter view, rehearsal, laser pointer, self-running) is deep and first-class.

## Product B — Apple Keynote (Mac)

### Key observations (first-hand this pass, evidence A)

Full user guide TOC (Keynote 15.3 on Mac) — section inventory:

- Keynote basics: Get started; Intro to images, charts, and other objects; **Create a presentation**; Choose how to navigate; **Open or close a presentation**; **Save and name a presentation**; Find a presentation; Print a presentation; undo/redo, sidebars, views, zoom.
- Add, edit, and organize slides: Add or delete slides; presenter notes; Organize slides (**Reorder**, **Group or ungroup**, **Skip or unskip**); Change the slide size; slide background; border around a slide; show/hide text placeholders; slide numbers; **Apply a slide layout**; **Add and edit slide layouts**; **Change a theme**; Clean up a slide.
- Objects: images (incl. image gallery), shapes (combine/break apart, draw, shapes library), 3D objects, lines and arrows, video and audio (record audio, live video), movie/image formats.
- Position and style: rulers, position/align, alignment guides, place objects inside text box/shape, **layer, group, and lock objects**, transparency, fills, borders, captions, reflection/shadow, object styles, resize/rotate/flip, object list, **linked objects for interactive presentations**.
- Text: full typography machinery incl. bidirectional/vertical text, equations; links.
- Tables with formulas; charts with editable data and chart styles.
- Animate: animate objects onto/off a slide, animate on a slide, **build order and timing**, **transitions**.
- **Play presentations**: Present on your Mac; Present on a separate display; Present during a FaceTime call; Use a remote; **Make a presentation advance automatically**; **Require a password to exit a presentation**; **Play a slideshow with multiple presenters**; Rehearse on your Mac; **Record presentations**.
- Writing/editing tools: spelling, find/replace, author name and comment color, highlight, **add and print comments**.
- Share and collaborate: **Send a presentation**; intro to collaboration; invite; collaborate on a shared presentation; latest activity; shared settings; stop sharing; shared folders; **Use Box to collaborate**; animated GIF; **Post your presentation in a blog**.
- Manage and organize: iCloud Drive; **Export to PowerPoint or another file format**; reduce file size; **package file**; **restore an earlier version**; move/delete; **password-protect**; **lock**; custom themes; **Transfer presentations between devices (AirDrop / Handoff / Finder)**.

"Create a presentation in Keynote on Mac" article body:

- "All presentations begin with a **theme**—a set of predesigned slide layouts you can use as a starting point. Replace the theme's images and text with your own, then add more slides as needed." Themes include **placeholders**.
- Workflow: theme chooser (categories, Standard/Wide size pop-up) → double-click theme → optionally switch the first slide's **slide layout** → **Add Slide** from layouts → double-click placeholder text to type → drag/replace placeholder images → **File > Save, enter a name, choose a location** ("Keynote automatically saves your changes as you work"; iCloud Drive default if set up) → **Play button in the toolbar, then press the arrow keys to advance through the slides. To end the presentation, press the Esc (Escape) key** → close the window.
- AI (subscription-gated, Apple Creator Studio, macOS 26+): generate a new presentation from a plain-text outline (Overview + Key Points fields, "complete with titles, bullet points, and a consistent theme"), or generate slides to add to an existing presentation.

Interpretation: the Mac Keynote documents the **authored-deck loop in full** — create from theme, compose on slide layouts, save/name/move/transfer as a document, play full-screen with keys, end with Esc — while collaboration is one section among many ("Share and collaborate", "Invite others... you control who can edit or only view"). Platform-native check satisfied: the file/document model (Save and name, Open or close, transfer with AirDrop/Handoff/Finder, package files, password-protect, lock) is the dominant documented model, with cloud storage (iCloud Drive) as the default location rather than as a collaboration substrate.

## Product C — LibreOffice Impress

### Key observations (first-hand this pass, evidence A)

Features page (LibreOffice 26.8):

- "LibreOffice Impress lets you create professional slide shows that can include charts, drawing objects, text, multimedia and a variety of other items. If you want, you can even **import and modify Microsoft PowerPoint presentations**."
- Creating Vector Graphics: "Many of the tools for creating vector graphics in LibreOffice Draw are available in LibreOffice Impress."
- Creating Slides: "templates to create professional-looking slides"; "dynamic effects... including animation and transition effects."
- Creating Presentations: "Several views or pages are available when you design a slide show. For example, the **Slide Sorter** displays an overview of your slides in thumbnail form, while the **Handout** page contains both the slide and the text you want to distribute to the audience." "Rehearse the timing of your slide show."
- Publishing Presentations: "publish your slides on-screen, as handouts, or as HTML documents."
- Giving Presentations: "the choice of running a slide show automatically or manually."

Guide index (article titles, evidence A for feature existence): Showing a Slide Show; Changing the Slide Order; Animating Slide Transitions; Changing the Slide/Page Background Fill; **Creating a Custom Slide Show**; Rehearse Timings of Slide Changes; Animating Objects; Animated GIF create/export; 2D→curves/polygons/3D conversion; import/export (HTML import, opening documents saved in other formats, saving in other formats, printing, print-to-fit); grouping objects; header/footer for all slides; Fontwork; gluepoints; **Insert Slide from File**; tables and spreadsheets in slides; bitmap→vector conversion.

Footer note: "LibreOffice was based on OpenOffice.org." (heritage line — OpenOffice Impress lineage, itself a StarOffice/OpenOffice.org descendant).

Interpretation: Impress is the open-source, file-based, single-author pole. The entire documented feature surface is grammar + authoring + delivery + publish; **no collaboration, no cloud, no AI appears anywhere in the Impress documentation**. It confirms the Type stands complete without the collaboration layer. It also documents the industry interchange posture (import and modify PowerPoint files) and alternative publish outputs (handouts, HTML).

## Market anchors (no claims)

- **Google Slides** — cloud-native presentation editor inside Google Workspace; the market's canonical collaborative-first realization (sibling pole). Docs unreachable (timeout ×1 this pass; sibling timeout ×2 + ×1). No operational claims.
- **Canva Presentations** — presentations as one artifact type inside a template-first design platform; the straddler anchor toward Graphic Design / Template-based Design Platform. Docs unreachable. No operational claims.

## Cross-product Comparison

| Dimension | PowerPoint (M365 + desktop) | Keynote (Mac) | Impress |
|---|---|---|---|
| Artifact | presentation document (blank or template start); perpetual desktop editions current | presentation document; File > Save, name, location; auto-save as you work | presentation document (file-based; import/modify PowerPoint format) |
| Grammar | slides + slide layouts; thumbnails side pane; sections (sibling) | ordered slides; slide navigator; layouts; placeholders | slides; Slide Sorter view; Handout page |
| Theme layer | prepared templates ("professionally designed, fully customizable") | themes = coordinated fonts/colors + layouts + placeholders; change a theme; custom themes | templates for professional-looking slides |
| Elements | text boxes, pictures, shapes, icons, 3D models, SmartArt, charts; video/audio (hub) | text boxes, images/galleries, shapes, 3D objects, lines/arrows, video/audio/live video, tables (formulas), charts (editable data), equations | charts, drawing objects, text, multimedia; vector tools from Draw; tables/spreadsheets in slides |
| Composition aids | font/bullets formatting (training article) | rulers, alignment guides, layer/group/lock, object list | grouping, gluepoints, clone formatting |
| Slide organization | New Slide after selected; Slide Layout | add/delete, reorder, group/ungroup, skip/unskip, slide size, numbers | change slide order; insert slide from file |
| Notes | speaker notes (add; presenter view; print) | presenter notes; presenter display | rehearse timings |
| Delivery | F5 / Shift+F5; Presenter view; self-running; laser pointer; rehearse + time; Live Presentations; Cameo; Speaker Coach | Play button + arrow keys; Esc to end; separate display; FaceTime call; remote; auto-advance; password-to-exit; multi-presenter; rehearse; record | slide show automatic or manual; custom slide show |
| Animation | transitions; Morph; multiple effects per object | transitions; builds (in/out/on); build order and timing | animation + transition effects; animated objects |
| Keep/file | (perpetual editions; file formats) | save/name; restore earlier version; package file; reduce file size; password-protect; lock | print; print-to-fit; reduced data for faster printing |
| Interchange/outputs | print slides/handouts/notes; PDF save (sibling); reuse slides | **Export to PowerPoint or another file format**; animated GIF; post in blog; send | **import and modify Microsoft PowerPoint presentations**; publish on-screen / handouts / HTML; GIF export; save in other formats |
| Review | comments; track changes; digital signatures (sibling, office-suite lineage) | comments with author name/color; print comments | — (not documented) |
| Sharing/collaboration | Collaborate and share section: co-authoring, share (sibling) | invite others (edit/view), shared settings, Box, stop sharing — one section among many | **none documented** |
| AI | Copilot: create presentation, add slides/images | Creator Studio (subscription): outline→presentation generation; Slide Clean Up; image generation | none |
| Container | Microsoft 365 storage in cloud realization; local files in desktop editions | iCloud Drive default; local; transfer via AirDrop/Handoff/Finder | local files |

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **The deck as an authored presentation artifact** — one persistent, self-contained unit of work the author creates, keeps, revisits, and hands off: content and design travel together as one whole (named file, device-stored document, or cloud-stored document — the substrate varies; "one authored work" does not). Remove → a live-only surface (whiteboard / meeting canvas territory).
2. **Presentation grammar** — the deck is an ordered sequence of slides; slide order is a first-class structure (add, reorder, delete) and is the order delivery follows. Remove → document/DTP/poster territory.
3. **Slide as bounded fixed-shape canvas with freeform element placement** — each slide is a page of fixed shape on which text, shapes, images, media, tables, and charts are placed, layered, sized, and aligned at will; composition is spatial, not a linear text flow, and bounded, not an endless canvas. Remove → document editor (flow) or whiteboard (unbounded).
4. **Audience delivery as the composing purpose** — the deck is composed as a sequential unit meant to be shown to an audience; the standard realization is in-product full-screen sequential playback (presenter-paced or timed), with export/print/publish/recorded outputs as alternative realizations of the same purpose. Remove → a graphic/page composition tool with no delivery semantics.

Jointly-held is load-bearing: 1+2 without 3 = slide-list; 3 without 1–2 = drawing canvas; 4 without 1–3 = playback of foreign content. The discriminator against the sibling: make the **shared live merged deck the primary object** (concurrent multi-user editing as the defining requirement) → Collaborative Presentation Editor; keep the authored deck as the unit of work with collaboration at most a layered capability → this Type. Porous in one direction: all three sampled modern products layer sharing/collaboration onto the authored deck (PowerPoint co-authoring, Keynote invite with edit/view, Google Slides by repute) — matching the document-editor/CDE precedent.

### L1 — Common Mature Structure

- Theme/template/layout layer: presentations begin from a theme or template ("a set of predesigned slide layouts" — Keynote; "professionally designed, fully customizable template" — PowerPoint; "templates to create professional-looking slides" — Impress); slides start from layouts with replaceable placeholders; themes can be changed under an existing deck; custom themes creatable (Keynote).
- Element palette: text boxes, shapes/lines, images, video/audio, tables, charts; product extensions: icons, 3D models, SmartArt, image galleries, equations, live video (PowerPoint/Keynote); layering, grouping, locking, alignment guides, rulers, object lists; hyperlinks (web or slide-to-slide).
- Slide organization machinery: slide navigator/thumbnail pane/Slide Sorter; add/duplicate/delete/reorder; group slides (Keynote) / sections (PowerPoint, sibling); skip slides (Keynote); slide numbers; slide size/orientation (deck-level properties).
- Speaker notes + presenter support: presenter notes; presenter view/display showing notes privately (PowerPoint multiple-monitors notes; Keynote presenter display; Impress rehearse); rehearse with timing (all three); remote control (Keynote); laser pointer (PowerPoint).
- Delivery machinery: full-screen slideshow (F5/Shift+F5 — PowerPoint; Play + arrow keys + Esc — Keynote; automatic or manual — Impress); transitions between slides; object animations/builds with ordering; auto-advance; self-running/kiosk-style options (PowerPoint self-running; Keynote auto-advance + password-to-exit); custom slide shows (Impress); multiple presenters (Keynote).
- Keep/file machinery: save and name (Keynote auto-save; PowerPoint/Impress file model), open/close, find, restore earlier version (Keynote), file-size reduction/package (Keynote), password protection (Keynote), print machinery (slides/handouts/notes).
- Interchange and alternative outputs: the PowerPoint format as the industry exchange standard (Impress "import and modify Microsoft PowerPoint presentations"; Keynote "Export to PowerPoint or another file format"; Pitch import/export — sibling); PDF export; print handouts/notes; HTML publish (Impress); animated GIF (Keynote, Impress); blog posting/embedding (Keynote); recorded presentation with narration (Keynote record presentations).
- Review loop: comments with authorship (Keynote author name/color; PowerPoint comments; Pitch commenter role — sibling); track changes as an office-suite lineage extra (PowerPoint, sibling).
- Working views: normal editing view + overview views (Slide Sorter, Handout page — Impress; slide navigator — Keynote; thumbnails side pane — PowerPoint).
- Sharing/collaboration as a modern added layer: co-authoring (PowerPoint), invite with edit/view roles (Keynote), full live co-editing as the primary object (Google Slides; Pitch — sibling). Common in current products; not definitional for this Type.
- AI assistance: deck generation/drafting (Copilot — PowerPoint; outline-to-presentation — Keynote, subscription-gated); increasingly common, era-current.

### L2 — Variant / Optional Structure

- Packaging: office-suite member (PowerPoint in Microsoft 365; Impress in LibreOffice) vs platform-native standalone (Keynote on Apple platforms) vs design-platform module (Canva) vs web-first collaborative-first suite member (Google Slides — the sibling pole) vs collaboration-first standalone (Pitch — sibling).
- Surface: desktop app / web app / mobile; offline behavior varies (Pitch documents offline work — sibling).
- Storage posture: local file vs device-platform cloud (iCloud Drive) vs suite cloud storage; auto-save semantics vary.
- Business model: perpetual desktop editions (PowerPoint 2016–2024), subscription (Microsoft 365; Apple Creator Studio for AI features), free open-source (LibreOffice), freemium (web-first products).
- Delivery-realization emphasis: live in-room slideshow vs video-conference presenting (Keynote FaceTime; PowerPoint Teams-era features — sibling's Live Presentations) vs recorded movie/narration vs kiosk/self-running vs print handouts vs HTML/published.
- Governance extras: password-protect/lock (Keynote), track changes/digital signatures/document inspection (PowerPoint office-suite lineage — sibling), conflict resolution when collaboration is on (Keynote — sibling).
- AI depth: sidebar drafting vs full outline→deck generation; subscription gating.

### L3 — Vendor-specific (Research Notes only)

- PowerPoint: F5/Shift+F5 convention; "Take a Tour"; Microsoft Create template source; Copilot chat entry points; Cameo; Speaker Coach; Live Presentations; Zoom for PowerPoint; Morph transition; SmartArt; 3D Models; Designer-era features (sibling); sections; track changes; digital signatures; inspect document; laser pointer; print handouts/notes.
- Keynote: theme chooser with Standard/Wide size pop-up; Apple Creator Studio subscription features (Generate Presentation dialog with Overview/Key Points fields, Slide Clean Up, autogenerated presenter notes, image generation; macOS 26+ requirement); presenter display; skip/unskip; author comment colors; package files; Handoff/AirDrop/Finder transfer; password-to-exit; multi-presenter slideshow; FaceTime presenting; linked interactive objects; Box collaboration; blog posting; reduce-file-size; custom themes.
- Impress: Slide Sorter; Handout page; custom slide show; HTML import/publish; gluepoints; 2D→3D conversion; Fontwork; Clone Formatting; vector tools shared with Draw; OpenOffice.org heritage; print-to-fit; reduced-data printing.
- Google Slides / Canva: none (unfetched — no claims).

## Rejected Findings

- **"A presentation application is an office-suite module"** — rejected: Keynote is a platform-native application outside an office suite; Canva embeds presentations in a design platform; the grammar does not require suite membership.
- **"PowerPoint format compatibility is definitional"** — rejected: it is the industry interchange standard (import/export documented in all sampled products' realizations), but Keynote's native format is its own, and the Type predates the format. Interchange = L1.
- **"Themes/templates are definitional"** — rejected: PowerPoint's first-class "Blank Presentation" path and template-free composition show the grammar stands without them; template layers are L1.
- **"Widescreen/slide dimensions are part of the definition"** — rejected: slide size is a deck-level, changeable property (Keynote "Change the slide size"; PowerPoint "Change the size of your slides" — sibling); no dimension asserted anywhere.
- **"Presenter view / transitions / animations are definitional"** — rejected: delivery machinery depth varies (Impress documents none of presenter-view-style private notes beyond rehearsal; historical slide-based tools delivered statically); the invariant is delivery purpose + sequential playback, not specific machinery.
- **"Collaboration is definitional"** — rejected for this leaf (it is the sibling's defining property); collaboration is a modern layered capability here.
- **"AI deck generation is definitional"** — rejected: subscription-gated (Keynote Creator Studio), era-current; Impress has none.

## Boundary Findings

1. **vs Collaborative Presentation Editor (sibling, processed) — DISCHARGES that pass's pre-hung joint-review flag from this side.** Same presentation grammar on both sides. Seam: this Type's unit of work is the **authored deck artifact** (create → keep → deliver; save/name/transfer documented as the dominant model in Keynote Mac and Impress, and in PowerPoint's perpetual editions), with collaboration at most a layered capability; the sibling's defining requirement is the **shared live merged deck** with concurrent multi-user editing. Porous in one direction (modern products layer sharing/co-authoring onto the authored deck); the adopted discriminator on both sides is whether the shared live merged deck is the primary object — directly parallel to the document-editor/CDE precedent, which explicitly predicted this seam for presentations. Keep-both ratified with this seam; no directory change.
2. **vs Document Editor (processed)** — same authored-artifact skeleton, different grammar: continuous linear prose flow paginated for reading vs ordered bounded slides composed for sequential delivery. Document-editor's own L0 (document artifact + inline editing + formatting model + page model) does not admit slide decks; the boundary is the grammar.
3. **vs Collaborative Document Editor (processed)** — same conclusion on the shared-live side: the grammar (slides vs text flow) separates the Types where collaboration exists on both.
4. **vs Desktop Publishing / Page Layout (§04.17)** — both compose fixed pages, but the delivery mode is the seam: pages composed for print reproduction vs slides composed for sequential on-screen delivery. Printing handouts is an output of the deck, not the center. A deck exported to PDF remains a presentation; a print brochure is DTP.
5. **vs Digital Whiteboard (processed)** — bounded ordered slides vs an unbounded persistent spatial board; the delivery sequence is not the whiteboard's organizing principle (that pass's own presentation-mode feature confirms the seam — whiteboards add presenting; presentations are composed for it).
6. **vs Diagramming Application (processed)** — slides may contain shapes, but shapes-with-connectors under a notation vocabulary are not this Type's organizing structure; no connector semantics anywhere in the sampled presentation documentation.
7. **vs Graphic Design Application / Template-based Design Platform (§04.01)** — deliverable difference: design deliverables (posters, social assets) vs the ordered delivery deck. Canva is the documented straddler (presentations as one artifact type inside a design platform); test: is the ordered-deck-for-delivery the product's center or one artifact kind among many?
8. **vs eLearning Authoring Tool (processed)** — ratifies that pass's recorded discriminator from this side: eLearning authoring produces **learner-driven** interactive content (questions, branching) handed to a delivery system; presentations produce **presenter-driven** sequential slide decks delivered by the presenter. Slide-based composition surfaces overlap; the interactivity/deliverable-to-LMS machinery does not exist in the sampled presentation docs, and delivery-to-audience (not learner navigation) is this Type's purpose.
9. **vs Video Editor (§04.06)** — recording a narrated movie of the deck (Keynote "Record presentations") is an output realization of the deck, not timeline editing of footage; no timeline/track/clip grammar here.
10. **vs Worship Presentation Software (§25, unprocessed)** — advance note: live lyric/scripture display for worship services shares slide-display mechanics; expected to be defined by its live-display/liturgy/service semantics when processed; the generic grammar documented here should not absorb it.

## Uncertainties

- Google Slides and Canva operational behavior unfetched (network rule applied); canonical model rests on three documented products + the sibling pass's Pitch/Keynote-iCloud evidence. Confidence in the L0/L1 split is high given the three-pole agreement (suite incumbent / platform-native / open-source) plus the sibling's collaborative-pole evidence; no Google/Canva-specific claims made.
- Historical check kept conceptual (Wikipedia unreachable ×2): the pre-cloud generation (Harvard-Graphics-class, Lotus-Freelance-class) is asserted to satisfy the core by the Type's own documented continuity (perpetual PowerPoint editions still current; Impress's OpenOffice.org lineage), not by direct historical sources. Recorded as a limitation, not a verified claim.
- PowerPoint outline view / outline-based composition not fetched this pass — not asserted.
- Multi-presenter, kiosk password-to-exit, FaceTime presenting documented only in Keynote — treated as optional/product-specific (L2/L3), not generalized.
- Whether offline authoring exists in web-first products — unverified; no claims.
- Precise limits (deck size, slide counts, media sizes, durations) — none asserted for any product.

## Final Synthesis

The Presentation Application is the presentation grammar carried by an authored deck artifact: one persistent unit of work the author creates, keeps, revisits, and delivers — an ordered sequence of slides, each slide a bounded fixed-shape canvas with freeform element placement, composed for sequential delivery to an audience, with in-product full-screen playback as the standard realization and export/print/publish/record as alternative outputs. The theme/template layer, element palette, notes, presenter support, transitions, file machinery, interchange (PowerPoint format as the exchange standard), review furniture, and AI drafting are mature market structure on top. The Type is defined independently of collaboration: sharing and co-editing are common modern layers (porous seam toward the Collaborative Presentation Editor, whose defining requirement is the shared live merged deck as primary object — the same seam shape the document-editor/CDE pair established and which that pair explicitly predicted for this family). The boundaries are held by the grammar (vs documents, DTP, whiteboards, diagrams, design deliverables), by the delivery purpose (vs graphics and page tools), and by the authored-artifact model (vs the collaborative sibling). Historical continuity holds: file-based, platform-native, and open-source realizations satisfy the core with no cloud, collaboration, templates, or AI in the definition.
