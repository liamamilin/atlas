# Research Notes — Collaborative Presentation Editor

## Research Goal

Understand what a Collaborative Presentation Editor is as an Application Type: the artifact grammar it edits (deck / slide / element), how multi-user collaboration is layered onto that grammar, how the deck is delivered to an audience, and where the boundary sits against the sibling Presentation Application, the Collaborative Document Editor, the Collaborative Design Platform, and the Digital Whiteboard.

## Initial Boundary

- The leaf sits under 03.04 Presentations, next to "Presentation Application".
- Working hypothesis: the type = presentation grammar (ordered slides, freeform spatial slide composition, delivery to an audience) + the collaboration layer (shared persistent deck, shared access, concurrent editing merged into one live version).
- Nearest neighbors: Presentation Application (same grammar, no shared-live layer), Collaborative Document Editor (same collaboration skeleton, different grammar — already processed; its STATUS entry records the seam as "same skeleton, different grammar"), Collaborative Design Platform (processed; shared design files, subject-agnostic), Digital Whiteboard (unprocessed; unbounded canvas), Collaborative Spreadsheet (same skeleton, table grammar).

## Research Questions

1. What is the core object model? (deck, slide, element, theme/master/layout, notes)
2. How does concurrent co-editing work on a slide-based artifact? (whole-deck live merge vs per-slide locking)
3. What sharing/permission models exist? (invites, links, roles, guests)
4. What does the delivery step look like? (slideshow, presenter view, co-presenting, web presentation)
5. How do review workflows work? (comments, slide status, track changes?)
6. What container/organization model holds decks? (drive files vs workspace-native)
7. What interchange exists? (PPTX import/export, PDF, embed)
8. Where is the line vs Collaborative Document Editor, Collaborative Design Platform, Whiteboard?

## Representative Products

| Product | Why selected | Evidence level reached |
|---|---|---|
| Microsoft PowerPoint (Microsoft 365 / web) | incumbent standard, .pptx ecosystem, enterprise tier | Tier-1 category taxonomy (4 category pages); deep articles unreachable |
| Pitch | collaboration-first standalone product, workspace-native | Tier-1 deep (help center, 7 pages) |
| Keynote for iCloud | platform-native check (§24), Apple ecosystem | Tier-1 deep (full user guide) |
| Google Slides | cloud-native suite, free/edu mass tier | market anchor only (fetch failed) |
| Canva Presentations | template/design-first mass-market straddler | market anchor only (fetch failed) |

## Sources

- Microsoft Support — PowerPoint help & learning hub: https://support.microsoft.com/en-us/powerpoint (fetched 2026-09-06)
- Microsoft Support — Collaborate and share (PowerPoint): https://support.microsoft.com/en-us/powerpoint/collaborate-and-share (fetched 2026-09-06)
- Microsoft Support — Slides and text (PowerPoint): https://support.microsoft.com/en-us/powerpoint/slides-and-text (fetched 2026-09-06)
- Microsoft Support — Print and present (PowerPoint): https://support.microsoft.com/en-us/powerpoint/print-and-present (fetched 2026-09-06)
- Pitch Help Center — home: https://help.pitch.com/ (fetched 2026-09-06)
- Pitch — Get started with Pitch: https://help.pitch.com/en/articles/8038180-getting-started-with-pitch (fetched 2026-09-06)
- Pitch — Get started collection: https://help.pitch.com/en/collections/2055837-get-started-with-pitch (fetched 2026-09-06)
- Pitch — Become a Pitch power user collection: https://help.pitch.com/en/collections/2056202-become-a-pitch-power-user (fetched 2026-09-06)
- Pitch — Present your ideas with your teammates: https://help.pitch.com/en/articles/11750406-present-your-ideas-with-your-teammates (fetched 2026-09-06)
- Apple — Keynote Support: https://www.apple.com/keynote/ (fetched 2026-09-06)
- Apple — Keynote User Guide for iCloud: https://support.apple.com/guide/keynote-icloud/welcome/icloud (fetched 2026-09-06)
- Google Slides — support.google.com/slides (timeout ×2), google.com/slides/about (timeout ×1) — abandoned per network rule; market anchor only
- Canva — canva.com/help (429), canva.com/help/presentations (browser-gated "Unsupported client") — abandoned; market anchor only

### Source-access limitations

- Microsoft deep help articles: 3 guessed article URLs returned 404 (article IDs not discoverable from category pages). Evidence for Microsoft is therefore at the official category-taxonomy level: feature existence and official feature naming, not operational detail. No precise co-authoring requirements (storage location, AutoSave behavior, editor limits) are asserted anywhere.
- Google Slides and Canva: no operational claims; used only as market anchors (both are universally recognized collaborative presentation surfaces).
- No numeric limits (deck size, slide count, collaborator counts, revision windows) are asserted for any product.

## Product A — Microsoft PowerPoint (Microsoft 365 / web)

### Key observations (category-taxonomy level, evidence A for feature existence)

Official help taxonomy (PowerPoint help & learning hub):

- Top-level sections: Get started / Collaborate / Design / Animations / Pictures & charts / **Present** / Slides & text / Copilot in PowerPoint.
- **Collaborate and share** section contains: "Save PowerPoint presentations as PDF", "Share your PowerPoint presentation with others", "Work together on PowerPoint presentations on your PC" (co-authoring), "Add, change, hide, or delete comments in a presentation", "Track changes in your presentation", digital signatures, inspect/remove hidden data.
- **Slides and text** section: "Add, rearrange, duplicate and delete slides", "Change the size of your slides", "Change the page orientation", "Reuse (import) slides from another presentation", "Organize your slides into sections", "Select individual objects on a slide", hyperlinks, text formatting.
- **Print and present** section: "Add speaker notes to your slides", "Start the presentation and see your notes in Presenter view", "View your speaker notes privately, while delivering a presentation on multiple monitors", "Create a self-running presentation", "Rehearse and time the delivery of a presentation", "Turn your mouse into a laser pointer", print handouts/notes.
- Prepare/Present highlights on the hub: speaker notes, presenting with Cameo, rehearse with Speaker Coach, Live Presentations ("engage your audience"), Presenter view, Zoom for PowerPoint.
- Animations section: transitions between slides, Morph transition, multiple animation effects per object.
- Copilot in PowerPoint: "Create a new presentation with Copilot".

Interpretation: PowerPoint carries the full presentation grammar (slides, objects, sections, transitions, presenter machinery) plus the collaboration layer (share, co-author, comments, track changes) plus delivery machinery (presenter view, rehearsal, live audience features). Track changes and digital signatures are desktop-lineage governance features — not observed in the web-native products.

## Product B — Pitch

### Key observations (deep, evidence A)

From "Getting started with Pitch":

- Terms: **Pitch account** (per-user profile, can join multiple workspaces) → **Workspace** (hub with members; encompasses templates, library content, presentations, rooms) → **Teamspace** (subsection of workspace; contains folders and presentations; can be limited to a subset of members) → **Folders / subfolders** → **Presentation** ("also known as decks, pitches, or even slideshows").
- Dashboard: per-member overview; Recents toggle "By me" / "By everyone"; Private space contains presentations visible only to the member; Library holds workspace assets (images, videos, fonts, templates, collections); quick menu (cmd/ctrl-K) search.
- Creation entry points: start with a template, start with AI, or **import an existing PowerPoint file**.

From the Get started collection:

- Slide grammar: add and edit **text blocks**, images, **shapes and lines**, **group blocks**, guides/margins/**layers**, slide numbers, **skip a slide**, **link to slides**, **recover a deleted slide**, **work offline**, find and replace, recolor SVGs, image editing incl. AI, color gradients, video recordings.
- Collaboration: **collaborate with comments**, **set a status and assignees for a slide**, in-app notifications, Slack app, commenter role, guest workspace concept, teamspaces, approved email domains.
- Mobile apps: review presentations, share and invite collaborators on mobile.

From the power-user collection:

- Templates and styles: find/use templates, create a template, **create your own slide style**, work with slide styles, upload custom fonts, move a template between workspaces.
- Connect and display data: create/edit **tables**, create/edit **charts**, import a spreadsheet to create charts, integrate **Google Analytics** / **ChartMogul** / **HubSpot** to create charts.
- Present and share: **add speaker notes**, **present using speaker view**, **follow collaborators**, present your slides, **share an external link to your presentation**, export to PDF, **share live presentations in Notion**, add animations, **export to PowerPoint**, "see all your team's links in one place", **invite guests to collaborate on presentations**, **share Pitch rooms with prospects or clients**, **present your ideas with your teammates** (co-presenter).
- Workflow: align blocks, smart formatting, keyboard shortcuts, quick menu, **embed content into slides**, **add variables to your presentation**, **batch create presentations**, Pitch's AI actions.

From "Present your ideas with your teammates" (co-presenter, premium feature):

- Multiple teammates enter the **Player**; the current presenter is listed at the top; the presenter controls slide advance/back and animation/focus-effect controls; others see slides advance and animations trigger in their own Player; control handoff via a **"Take over"** button.

Interpretation: Pitch is workspace-native (decks live in teamspaces/folders, not a file drive), collaboration-first (comments, slide status/assignees, notifications, guests, co-presenting), and sales-oriented in its extensions (rooms for prospects, analytics, live links). Its grammar is block-based ("blocks" rather than "objects") but structurally the same: bounded slide canvas + placed elements.

## Product C — Keynote for iCloud

### Key observations (deep, evidence A)

From the Keynote User Guide for iCloud:

- "All presentations begin with a **theme**—a set of predesigned slide layouts you can use as a starting point. Replace the theme's images and text with your own, then add more slides as needed."
- "Add **objects** like images, video, audio, charts, shapes, or tables to any slide. You can layer objects, resize them, and link them to webpages or other slides in your presentation."
- Slide organization: add or delete slides, **reorder slides**, **group or ungroup slides**, **skip or unskip slides**, slide numbers, slide background, **advance slides on click or automatically**.
- Presenter notes; **presenter display** (separate window: slide navigator, current and next slides, presenter notes, timing).
- Play: "Play your presentation on your computer, on a separate display, or **over the internet**."
- Collaboration: "Invite others to work with you on your presentation. **Everyone you invite can see changes as they're made, but you control who can edit or only view** the presentation." Sub-pages: intro to collaboration, invite others, collaborate on a presentation, change shared presentation settings, stop sharing, **shared folders and collaboration**, **use Box to collaborate**.
- Manage: save/name/duplicate, delete/recover, **restore earlier versions**, organize presentations, **password-protect presentations**, download.
- Writing/editing tools: spell-check, find and replace, **add or reply to comments**, **set your author name and color**.
- Animate: slide transitions, animate objects (build in/out).
- Tables (with formulas), charts (editable data), image galleries, shapes (combine/break apart), text inside shapes.
- Troubleshooting: "Resolve presentation conflicts" (evidence that concurrent editing can produce conflicts needing resolution).
- Publishing: "Post presentations in a blog" (embed).
- Upload a presentation / sync a presentation (interchange with native Keynote files).

Interpretation: Keynote for iCloud is the platform-native check. It carries the same grammar (theme → slides → objects) and the same collaboration layer (invite, edit/view roles, live changes, shared folders, version restore, comments with author colors). It confirms the type without any workspace concept — the container is iCloud files + shared folders. "Present over the internet" and "resolve presentation conflicts" are notable: delivery-over-web and conflict handling are part of the live-deck reality.

## Market anchors (no claims)

- **Google Slides** — cloud-native collaborative presentation editor inside Google Workspace; universally recognized; real-time multi-user editing, sharing links, comments, present mode, PPTX interchange. No operational detail asserted (docs unreachable).
- **Canva Presentations** — presentations as one artifact type inside a template-first design platform; straddles Collaborative Design Platform. No operational detail asserted (docs unreachable).

## Cross-product Comparison

| Dimension | PowerPoint (M365) | Pitch | Keynote for iCloud |
|---|---|---|---|
| Artifact | presentation file (cloud-stored for co-authoring) | presentation ("deck") in workspace | presentation file in iCloud |
| Grammar unit | slide; objects; sections | slide; blocks; layers/guides | slide; objects; groups |
| Theme layer | design themes (Design section) | templates + slide styles | themes = predesigned slide layouts |
| Co-editing | "work together on PowerPoint presentations" (co-authoring) | real-time collaboration; follow collaborators | "everyone… can see changes as they're made" |
| Access roles | share with others (roles not detailed at category level) | members, commenter role, guests | edit or view-only, per invite |
| Comments | yes (add/change/hide/delete) | yes (+ slide status/assignees) | yes (+ author name/color) |
| Presence | co-authoring presence (implied by co-authoring docs; not detailed) | follow collaborators; presenter list | collaboration menu shows collaborator names |
| Review governance | track changes; digital signatures; inspect document | slide status + assignees | — |
| Delivery | slideshow, presenter view, self-running, rehearsal, laser pointer, Live Presentations | Player, speaker view, co-presenter with take-over, live in Notion | present on computer / separate display / over the internet; presenter display |
| Notes | speaker notes (add, print, presenter view) | speaker notes + speaker view | presenter notes + presenter display |
| Versioning | (not at category level) | recover deleted slide | restore earlier versions; resolve conflicts |
| Container | Microsoft 365 storage (OneDrive/SharePoint implied; not asserted) | workspace → teamspaces → folders; private space; rooms | iCloud files; shared folders; Box option |
| Interchange | save as PDF; reuse slides from other presentations | import PPTX; export PPTX; export PDF | upload/download; post in blog (embed) |
| Data | charts (Pictures & charts section) | tables/charts from spreadsheets, GA/ChartMogul/HubSpot | tables with formulas; charts with editable data |
| AI | Copilot in PowerPoint | Pitch Agent, AI actions, AI image editing | — (not in fetched guide) |
| Org extras | — | analytics, batch create, variables, brand tone | password protection |

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Shared persistent deck** — the presentation is held by the product as one live current version; no save/download/pass-around loop.
2. **Presentation grammar** — the deck is an ordered sequence of slides; each slide is a bounded canvas on which elements (text, shapes, images, media) are freely placed; the deck is composed as a sequential unit for delivery to an audience.
3. **Shared access beyond one author** — multiple participants reach the deck through the product's sharing mechanism (identity invites and/or links), with at least an edit/view distinction.
4. **Concurrent multi-user editing merged into a single live current version** — participants' changes land in the same deck without a merge-by-file step.

Remove #1–2 → not a presentation tool. Remove #3–4 → a (single-author) Presentation Application, not a *collaborative* one. Remove the ordered-slide grammar (keep shared concurrent canvas) → Collaborative Design Platform / Whiteboard territory. Remove the bounded-slide grammar (keep linear text flow) → Collaborative Document Editor.

### L1 — Common Mature Structure

- Slide organization machinery: add/duplicate/reorder/delete slides, slide navigator/thumbnails, grouping/sections, skip slides, slide numbers.
- Element palette: text boxes, shapes/lines, images, video/audio, tables, charts; layering, grouping, alignment, guides; links between slides or to the web.
- Theme/template layer: themes with predesigned layouts (Keynote), design themes (PowerPoint), templates + slide styles (Pitch); masters/layouts as the reusable slide furniture.
- Speaker notes + presenter view (presenter display / speaker view): private notes and controls while the audience sees slides.
- Present/deliver: full-screen slideshow, transitions and object animations, auto-advance, self-running options.
- Comments with replies and authorship attribution (author name/color in Keynote; commenter role in Pitch).
- Sharing machinery: invite by identity, share links, edit/view roles, guests (Pitch), anyone-with-link settings (Keynote shared presentation settings).
- Live presence: collaborator names visible (Keynote collaboration menu), follow collaborators (Pitch), co-authoring presence (PowerPoint).
- Version safety: restore earlier versions (Keynote), recover deleted slides (Pitch), conflict resolution (Keynote).
- Interchange: PPTX import/export (Pitch; PowerPoint native; Keynote upload/download), PDF export (all three), embed/publish (Keynote blog posting, Pitch live in Notion).
- Container + organization: folders (all), workspace teamspaces (Pitch), shared folders (Keynote), search, notifications (Pitch).
- AI assistance: deck generation/drafting (Copilot in PowerPoint, Pitch Agent/AI actions) — increasingly common across the market.

### L2 — Variant / Optional Structure

- Container philosophy: file-in-cloud-drive (PowerPoint/Keynote/Google) vs workspace-native (Pitch teamspaces, private space, rooms).
- Co-presenting machinery: multi-presenter Player with control handoff (Pitch, premium) — only Pitch documents it in the sample; PowerPoint's Live Presentations and Keynote's present-over-internet address the audience side instead.
- Deck analytics (Pitch) — product-specific, sales-oriented.
- Data connectivity: live charts fed from spreadsheets or SaaS integrations (Pitch: GA/ChartMogul/HubSpot; Keynote charts have editable data but no fetched evidence of live SaaS feeds).
- Variables / batch deck creation (Pitch) — template-merge posture.
- Offline editing (Pitch documents "work offline"; native desktop/mobile apps are offline-capable by nature; web-first products vary) — posture variant.
- Governance extras: track changes, digital signatures, document inspection (PowerPoint desktop lineage) — office-suite governance variant.
- Password protection of decks (Keynote).
- Third-party storage collaboration (Keynote via Box).
- Video recording of a deck (Pitch create video recordings).
- Print/handouts (PowerPoint print handouts/notes; Keynote print).
- Mobile collaboration surface (Pitch mobile review/share).
- Rooms shared with prospects/clients (Pitch) — sales-room container variant.

### L3 — Vendor-specific (Research Notes only)

- Pitch: teamspaces, private space, rooms, "Next slide please" sticker, slide status/assignees, brand tone, approved email domains, ChartMogul/HubSpot/Google Analytics integrations, variables, batch create, Pitch Agent + Claude MCP + API, premium co-presenter, presentation analytics, library, smart formatting, recolor SVGs, commenter role, guest workspaces, "see all your team's links in one place".
- Microsoft: Copilot, Cameo, Speaker Coach, Zoom for PowerPoint, Morph transition, Live Presentations, sections, track changes, digital signatures, inspect document, F5/Shift+F5, laser pointer, rehearse-and-time, print handouts.
- Keynote: theme terminology, presenter display, skip slides, author colors, image galleries, drop caps, combine/break-apart shapes, iCloud sync, resolve-conflicts flow, Box collaboration, post-in-blog.
- Google Slides / Canva: no vendor claims (unfetched).

## Boundary Findings

1. **vs Presentation Application (sibling, unprocessed)** — sharpest seam, same as Document Editor vs Collaborative Document Editor: single-author file with save/pass-around vs shared live deck with concurrent merge. The grammar (deck/slides) is identical; the collaboration layer is the discriminator. Historical check: pre-cloud PowerPoint/Keynote are Presentation Applications, not members of this type — confirming the collaboration layer (not the grammar) defines this leaf.
2. **vs Collaborative Document Editor (processed)** — same collaboration skeleton (shared persistent artifact + shared access + concurrent merge into one live version), different grammar: document = continuous linear text flow with optional pagination; presentation = discrete ordered slides, each a bounded spatial canvas, composed for sequential delivery. The CDE pass already recorded this seam ("same skeleton, different grammar"); this pass confirms it from the presentation side.
3. **vs Collaborative Design Platform (processed)** — design platform files are subject-agnostic design surfaces (frames/boards, prototyping, dev handoff); presentation decks are ordered delivery units. Straddlers exist: Canva (presentations inside a design platform) and suite expansion (design platforms adding slides). Test: is the artifact an ordered deck whose primary job is sequential delivery, or a design file whose primary job is visual production?
4. **vs Digital Whiteboard (unprocessed)** — whiteboard = unbounded (or frame-optional) canvas for free spatial exploration; presentation = bounded ordered slides for delivery. A whiteboard's frames can resemble slides, but the delivery sequence is not the organizing principle.
5. **vs Collaborative Spreadsheet (unprocessed)** — same skeleton, table/cell grammar; decks may embed charts fed by spreadsheets but the spreadsheet remains the data artifact.
6. **vs Webinar / Virtual Meeting Platform** — those deliver live meetings; this type edits the deck artifact. Live-presenting features (Pitch co-presenter, Keynote over-the-internet, PowerPoint Live Presentations) are delivery aids for the deck, not meeting infrastructure.

## Uncertainties

- Google Slides and Canva operational behavior unfetched; the canonical model rests on 3 documented products (one at category level). Given the near-identical structure across all three documented products plus the two anchors' universally known shape, confidence in the L0/L1 split is high, but no Google/Canva-specific claims are made.
- PowerPoint co-authoring operational requirements (storage location, AutoSave, per-element merge granularity) not verified — kept qualitative.
- Whether co-presenting (multi-presenter control handoff) exists beyond Pitch — unverified; treated as optional/product-specific.
- Whether deck-level analytics exist beyond Pitch — unverified; product-specific.
- Exact role ladders vary (PowerPoint roles not detailed at category level; Keynote edit/view; Pitch member/commenter/guest) — described qualitatively.

## Final Synthesis

The Collaborative Presentation Editor is the presentation grammar (ordered bounded slides, freeform element placement, delivery to an audience) carried by a shared, live, concurrently-edited deck with shared access roles. Everything else — themes/masters, notes, presenter views, comments, version history, interchange, AI, analytics, co-presenting — is mature market structure layered on that core, with container philosophy (file-in-drive vs workspace-native) and governance extras (track changes, signatures) as the main variant axes. The type is the intersection of the Presentation Application grammar and the collaboration structure already canonicalized for Collaborative Document Editors; its boundaries are held by the grammar (vs documents, whiteboards, design files) and by the collaboration layer (vs single-author Presentation Application).
