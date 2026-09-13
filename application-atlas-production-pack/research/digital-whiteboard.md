# Research Notes — Digital Whiteboard

## Research Goal

Understand what a Digital Whiteboard application is from real products: what the shared surface is, what people put on it, how they mark it up together, what the board's lifecycle and access model are, and — critically for this leaf — where "Digital Whiteboard" stands against the already-processed sibling leaves **Collaborative Canvas** (probable alias, flagged 2026-09-06) and **Diagramming Application** (boundary re-confirmed 2026-09-06). This pass was explicitly designed as the joint-review pass requested by the collaborative-canvas research notes.

## Initial Boundary (working hypothesis before research)

- Hypothesis: a digital whiteboard is the digital counterpart of the physical meeting-room whiteboard — a shared surface that several people draw on, write on, and place content on together, live, with the board persisting afterwards.
- Nearest neighbors: Collaborative Canvas (same directory section, flagged as probable alias), Diagramming Application (same section), Collaborative Design Platform (04.01), Collaborative Presentation Editor (03.04), Visual Note-taking Application (03.02), Virtual Office Workspace (03.12), meeting/webinar platforms, interactive-display classroom lesson software (outside the directory).
- Known risk carried in from STATUS.md: "Digital Whiteboard" and "Collaborative Canvas" may be two names for one market category. This pass must resolve or sharpen that with fresh evidence.

## Research Questions

1. What do vendors that sell "whiteboards" call their product, and what do they say it is? (Self-description evidence for the category name.)
2. Is freehand marking/drawing a defining property of the Type, or a common capability?
3. How does the live-session character present (facilitation tools, meeting embedding, interactive displays, walk-up devices)?
4. What is the board lifecycle — including the walk-up/device-session pattern where a board may be ephemeral until explicitly saved?
5. What is the object model (strokes, notes, shapes, text, media, connectors) and the organization model (frames/sections/pages/containers)?
6. What access/permission machinery exists (sharing, graded access, guests, join codes)?
7. Where is the boundary vs diagramming tools, design canvases, presentation tools, and meeting platforms?
8. Does the evidence support "Digital Whiteboard" and "Collaborative Canvas" as one Type or two?

## Representative Products

Selected for market representativeness, documentation depth, product philosophy, customer tier — and, deliberately, for whiteboard-lens coverage not already deep-covered by the collaborative-canvas pass:

| Product | Why selected | Evidence level reached (this pass) |
|---|---|---|
| Lucidspark (Lucid) | The whiteboard sibling of a vendor that ships diagramming and whiteboarding as separate products; rich help center; enterprise + device programs | Tier 1 (help center: FAQ, Welcome, Freehand drawing, Interactive whiteboard devices) |
| Conceptboard | Long-standing independent European vendor; "online whiteboard" self-description; enterprise/public-sector/compliance positioning | Tier 2 (official product pages only; help center unreachable ×2) |
| FigJam (Figma) | Design-suite-embedded board; vendor's own help center labels it "a digital whiteboard" — key alias evidence | Tier 1 (Guide to FigJam re-fetched this pass) |
| Miro | Market-leading platform; re-verified this pass for cross-check | Tier 1 ("What is Miro?" re-fetched; deeper detail from 2026-09-06 pass) |
| Microsoft Whiteboard | Platform-native / meeting-suite-embedded pole | Unreachable directly (microsoft.com blocks automated access per prior pass; learn.microsoft.com path 404 this pass). Secondary: competitor characterization on Conceptboard's official comparison page |
| Zoom Whiteboard | Meeting-native whiteboard pole | Unreachable (three URL attempts, 404s). Existence + meeting-suite embedding evidenced indirectly via Lucid's device-integration docs |
| Mural, Excalidraw, Google Jamboard | Cross-check + historical/platform-native checks | From the 2026-09-06 collaborative-canvas pass (Mural Tier 2; Excalidraw title-level; Jamboard indirect via migration guides) |

## Sources

Research date: 2026-09-07 (this pass). Prior-pass sources from 2026-09-06 are marked.

- Lucid Help Center — https://help.lucid.co/hc/en-us (root FAQ) — fetched
- Lucid Help Center — Lucidspark category https://help.lucid.co/hc/en-us/categories/14652573187476 — fetched
- Lucid Help Center — "Welcome to Lucidspark" (articles/11973407023636) — fetched
- Lucid Help Center — "Freehand drawing in Lucidspark" (articles/14591300224404) — fetched
- Lucid Help Center — "Use Lucidspark on interactive whiteboard devices" (articles/32050106028948) — fetched
- Conceptboard — https://conceptboard.com/ — fetched
- Conceptboard — https://conceptboard.com/conceptboard-vs-microsoft-whiteboard/ — fetched (competitor characterization of Microsoft Whiteboard — secondary evidence, treated accordingly)
- Conceptboard Help Center — https://help.conceptboard.com/hc/en-us — **failed twice (timeout, transport error), abandoned per network rules**
- Figma Learn — "Guide to FigJam" https://help.figma.com/hc/en-us/articles/1500004362321 — fetched (re-verification)
- Miro Help Center — "What is Miro?" https://help.miro.com/hc/en-us/articles/360017730533 — fetched (re-verification)
- Lucidspark product page https://lucidspark.com/ — **403, abandoned** (help center used instead)
- Zoom — explore.zoom.us/en/products/whiteboard/ 404; zoom.us/en/products/whiteboard/ 404; zoom.com/en/products/zoom-whiteboard/ 404 — **abandoned per network rules**
- Microsoft — learn.microsoft.com/en-us/microsoftwhiteboard/ 404 — **abandoned** (microsoft.com already known to block automated access from the 2026-09-06 pass)
- Prior pass (2026-09-06): Miro Help Center (What is Miro; How to start collaboration; Getting Started category), Figma Learn (FigJam category; Guide to FigJam), Mural product page, Excalidraw (title + developer docs), Miro/FigJam migration guides evidencing Google Jamboard

## Product Observations

### Lucidspark (Lucid) — evidence layer A (official help center, this pass)

- Self-description (direct quote): "Welcome to Lucidspark, **a virtual whiteboard** for freeform ideation, group brainstorming, and real-time hybrid collaboration!"
- Category positioning from the help-center FAQ (direct quote): plans may include licenses for "Lucidchart (**to build intelligent diagrams**), Lucidspark (**to collaborate in a virtual whiteboard**), or the Lucid Suite (with access to both)." The vendor's own FAQ separates the diagram product from the whiteboard product in one sentence.
- Import taxonomy (direct quotes): "In Lucidchart, you can import: Microsoft Visio, Gliffy, Draw.io, and OmniGraffle files… In Lucidspark, you can import: **Miro, MURAL, and FigJam boards**." Boards migrate as one family; diagram files are a different family.
- Home page: view and organize **boards**, create and manage **folders**, access **templates**; account settings, admin panel, integrations marketplace.
- Board creation: **Blank Board**, **Create from Template** (Template Gallery), or **Join ID** ("quickly access a document when the owner has provided the code").
- Workspace anatomy: **Board Controls** (switch between Lucid products using the **universal canvas**, rename, star, **Revision History**, Search incl. Advanced search / find & replace); **Collaboration Tools** (**Timer, Voting, Facilitator Tools, Collaborator Colors, Color Legend, Follow Collaborator, Invite others to me, Chat, Comment, Presentation Builder, Record a video, Share**); **Primary Toolbar** (Templates, Visual Activities, **Breakout Boards**, Import, Selection tools incl. **Laser Pointer** and **Freehand Select**, Text, **Sticky notes**, Shapes, Lines, **Organizers** — **Frames, Paths, Containers, Dynamic Tables, Tables, Timelines, Mind Maps** — Images, **Freehand drawing**, AI, **Lucid Cards**, Notes, Jira/Smartsheet/Azure DevOps integrations); the **canvas**; **Canvas View Controls** (Table of Contents, **Mini Map**, zoom, full screen).
- Freehand drawing (dedicated article): Pen tool with color, thickness, transparency; drawings are selectable, styleable objects; **Magic Shapes** converts freehand strokes into perfect shapes (circles, diamonds, stars, **stickies**, squares, triangles, rectangles, lines); erasers: **Object Eraser, Pixel Eraser, Erase All** — with the multi-user detail that Erase All "will clear only drawings that **you** have created." Available on all plans including FedRAMP environments.
- Collaboration section: **Guest Collaborators**, **Breakout Boards** ("Collaborate with Breakout Boards"), **Voting sessions**, **private mode** ("Brainstorm with private mode"), **timer**.
- Organization section: **Sort objects**, **Gather sticky notes**, **Containers** ("organize and hide content"), **Frames**, saved queries and planning shapes, dependency mapping.
- Interactive whiteboard devices (dedicated article — the whiteboard-lens centerpiece):
  - "Seamlessly use Lucidspark on any supported whiteboard device **without logging in — simply walk up and whiteboard**."
  - Supported devices: **Avocor** (H Series, Lucid pre-installed), **Google Meet Hardware** (Avocor Board 65 / Desk 27), **Neat**, **Webex**, **Zoom Rooms**, **Microsoft Surface Hub** (via browser/PWA), other web-enabled devices.
  - **Cast an existing Lucid document** to the device from phone/laptop/tablet via an **8-digit code**; editing on the device uses Lucidspark features ("optimized for interactive whiteboard devices") even when casting a Lucidchart document.
  - Curated device feature set: sticky notes (tag, sort), **freehand drawing ("Write or draw with your finger or a whiteboard pen")**, magic shapes, freehand select, visual activities, templates, timer, **laser pointer**.
  - Share from the device via a **6-digit Join ID** ("Enable Collaboration") for hybrid collaboration ("work with colleagues in a meeting room, engage with remote teammates in real time, or blend both").
  - **Session lifecycle on shared devices**: if the board is not shared, after inactivity the user is prompted to keep the session open; with no response "the session will time out and **the document and progress will be deleted**." Saving = sending the board to Lucid accounts by email (up to five addresses; "the first user to claim the board becomes the document owner"); the board must be **claimed within 24 hours** or Lucid deletes it.
  - Device program not available on FedRAMP environments (web-browser fallback possible).
- Plan structure: Free / Individual / Team / Enterprise; admin panel; integrations marketplace.

### Conceptboard — evidence layer Tier 2 (official product pages; help center unreachable)

- Self-description (direct quote): "**The online whiteboard** for ideas, tasks, and projects." Positioning: "From idea to execution, Conceptboard combines visual collaboration with digital task management in one space."
- Framing triad: **Visualise** (develop ideas/concepts/strategies collaboratively), **Organise** (manage tasks/responsibilities/workflows "directly on the whiteboard"), **Execute** (plan/visualise/complete projects).
- **Tasks on the board**: "turn any board content into concrete to‑dos. Assignees can be added, deadlines set, tags applied, and content can then be searched based on these tags." Kanban-style visual workflows on the board; **Cards** feature (organize/prioritize content with progress, people responsible, due dates).
- Use cases: brainstorming, visual project management, remote collaboration ("Align in real time or asynchronously"), product management/roadmapping, wireframing, design thinking, agile practices, meetings & workshops.
- Enterprise/public-sector posture: GDPR-compliant, ISO 27001/27017/27018, hosting in Germany; **cloud / dedicated server / on-premises** hosting options; role- and permission-based access control; German Administrative Cloud (DVC) availability; tender/procurement support.
- Comparison page vs Microsoft Whiteboard (competitor characterization — **secondary evidence about Microsoft**, treated as such):
  - Microsoft Whiteboard characterized as: "ideal for quick sketches and spontaneous ideas"; "Simple whiteboard for quick sketches"; "Integrated into Microsoft 365"; "Microsoft Cloud (USA)"; "Suitable for smaller groups"; "does not offer comparable access control."
  - Conceptboard's contrast set (its own features): roles and access rights, **board history** with version recovery, guest access, **chat and video conferencing within the board**, **presentation mode with slides** created inside the board, brand color codes, PNG export, a **freeze function** for facilitators, board switching/search across projects, password protection for boards, SSO, audit log.
- Recently highlighted features: **laser pointer** ("present with precision… keep your audience focused"), rounded corners for shapes, Cards.

### FigJam (Figma) — evidence layer A (re-verified this pass)

- Self-description (direct quotes): "FigJam is an online collaboration tool you and your team can use to brainstorm, develop, and organize ideas… Think of them as **digital whiteboards** where you and your team discover, explore, and execute on ideas." Help-center navigation label: "FigJam — **Collaborate with a digital whiteboard**."
- File model: a FigJam file is a file type inside Figma (teams, projects, drafts); three regions: the board, the file toolbar, the tools-and-objects bar; iPad app.
- Structure primitives: **pages** ("an extra layer of organization"), **sections** ("cluster, contain, and move objects together"), **stickies** ("the core for any FigJam board, along with shapes and connectors"; author's name shown by default), **shapes** (basic/flowchart/misc), **connectors** (elbow/straight; endpoints re-draggable between objects), **text**, drawing tools (**marker, highlighter, washi tape**), **tidy up** (uniform grid arrangement).
- Templates: community library + custom templates publishable by any member with **can edit** access (publish to team or organization).
- Import: boards directly from **Google Jamboard, Miro, Mural, Lucid** ("Import from other whiteboard tools"); images; CSV → FigJam **table** (500-cell limit — product-specific precision, kept out of the final document); paste from Figma Design (explicitly **no layers panel** in FigJam); **widgets** (Asana, Jira tasks as board objects).
- Meeting/facilitation: **voting sessions** (choices hidden while voting, tally revealed at end), meeting boards, card-sorting exercises, comments/mentions/**cursor chat**, **stamps** and **emotes** (temporary, fading), **audio conversations** on the file, **spotlight** ("all collaborators… are notified you've requested they follow you", with a grace window to ignore).
- Use cases listed: brainstorm; decision trees, diagrams, mind maps; critiques/feedback; research synthesis; meetings/tutorials/interactive sessions; stakeholder alignment.

### Miro — evidence layer A (re-verified this pass; deeper detail from 2026-09-06 pass)

- Self-description (direct quote, this pass): "Miro is the **AI-first online workspace for innovation** that enables distributed teams of any size to dream, design, and build the future together." Meetings/workshops named explicitly, with video chat, presentation mode, and board sharing.
- Quick start: register a profile → create a board → start collaboration.
- From the 2026-09-06 pass (layer A): "Every board is saved automatically. Each board is **endless**, and **frames act like pages**"; Share button with invite/link; real-time **or async** collaboration "with people from different time zones"; content types include documents, spreadsheets, images, presentations, links, icons, embedded video; guests with view/comment access; deleted boards restorable by owners; content recovery via Activity list; teams + dashboard; plan tiers incl. Education/Enterprise; **interactive displays** for hybrid meetings; migration tooling separating "Import Mural/FigJam/Jamboard/Conceptboard **boards**" from "Import Lucidchart/draw.io **diagrams**"; performance FAQ acknowledging degradation with many simultaneous users and heavy boards.

### Microsoft Whiteboard — not directly reachable; secondary characterization only

- Direct fetches failed (microsoft.com blocks automated access — established in the 2026-09-06 pass; learn.microsoft.com path 404 this pass).
- What can be asserted: the product's **name itself** ("Microsoft Whiteboard") is category self-identification by a major platform vendor; it is embedded in the Microsoft 365 / Teams ecosystem; and a competitor's official comparison page characterizes it as a simple, individual/small-team-oriented whiteboard integrated into Microsoft 365. All Microsoft behavior claims below positioning level remain unstated.

### Zoom Whiteboard — not reachable

- Three official URL attempts returned 404. Existence and meeting-suite embedding are evidenced indirectly: Lucid's device documentation describes enabling the Lucid app for **Zoom Rooms**-configured devices and opening Lucidspark from within a Zoom meeting. No Zoom Whiteboard behavior claims are made.

### Mural / Excalidraw / Google Jamboard — from the 2026-09-06 pass

- Mural: "shared infinite canvas", facilitation-first positioning, LUMA methodology (product-page level; support center unreachable).
- Excalidraw: page title "**Excalidraw Whiteboard**"; open-source, embeddable, minimal.
- Google Jamboard: platform-native (Google account/hardware) board product, discontinued; evidenced via official migration guides on Miro and FigJam; member of the same board-migration family as Mural/FigJam/Conceptboard.

## Cross-product Comparison

| Aspect | Lucidspark | Conceptboard | FigJam | Miro | Microsoft Whiteboard (secondary) |
|---|---|---|---|---|---|
| Self-description | "a virtual whiteboard" | "the online whiteboard" | "digital whiteboards" | "online workspace" (boards endless) | "Whiteboard" (name) |
| Vendor family | diagram vendor's whiteboard sibling (Lucidchart separate) | independent | design-suite-embedded | standalone platform | platform-suite-embedded |
| Unit of work | board (home page lists boards/folders) | board | FigJam file containing a board | board ("endless", auto-saved) | board (positioning level) |
| Freehand marking | Pen tool, styling, Magic Shapes, object/pixel erasers, per-user Erase All | (not verified at this depth) | marker, highlighter, washi tape | pen/drawing tools (prior pass) | characterized as sketch-first |
| Placed objects | stickies, shapes, lines, text, images, cards, notes, tables, timelines, mind maps | sticky notes, cards, tasks, shapes (positioning level) | stickies, shapes, connectors, text, tables, widgets | docs, spreadsheets, images, presentations, links, video, icons | (not verified) |
| Organization | frames, containers, paths, tables of contents, mini map | (positioning level) | pages, sections, tidy up | frames ("act like pages") | (not verified) |
| Facilitation | timer, voting, facilitator tools, laser pointer, private mode, breakout boards, follow, presentation builder | freeze, laser pointer, presentation slides in board, chat & call in board | voting, spotlight, audio, stamps/emotes, cursor chat | video chat, presentation mode, workshop use cases | (not verified) |
| Access | share, Join ID, guest collaborators, admin panel | roles/permissions, password protection, guests | can-edit gating, visitors/open sessions | share button, guests view/comment | (not verified) |
| Persistence | revision history; device sessions ephemeral until saved/claimed (24h claim window) | board history with version recovery | files auto-persist in Figma | "saved automatically" | (not verified) |
| Migration family | imports Miro/MURAL boards; Lucidchart imports diagram files | compared against Miro and Microsoft Whiteboard as peers | imports Jamboard/Miro/Mural/Lucid boards | imports Mural/FigJam/Jamboard/Conceptboard boards; diagrams separate | — |
| Device/display story | walk-up whiteboarding on Avocor/Google Meet/Neat/Webex/Zoom Rooms/Surface Hub; casting via 8-digit code | (not evidenced) | iPad app | interactive displays (prior pass) | (not verified) |
| Delivery | standalone SaaS in the Lucid Suite; FedRAMP environment exists | cloud / dedicated / on-premises; EU hosting | embedded in Figma | standalone SaaS + desktop/mobile/display apps | embedded in Microsoft 365 |

### Stable commonalities observed across the sample

1. The **board** — one shared, spatially free visual surface — is the unit of work in every sampled product, whatever the vendor calls it (board / file / whiteboard / canvas). (Layer A for Lucidspark/FigJam/Miro; positioning for Conceptboard; name-level for Microsoft.)
2. Content enters as **freehand marking** (pen/marker/highlighter strokes) and as **discrete placed objects** (sticky notes, shapes, text, images/media, connectors). Every product with operational evidence carries both. (Layer A ×3; Conceptboard positioning.)
3. **Multiple identified people co-edit the same board** — live with named presence (cursors, collaborator colors, follow) and asynchronously on the same artifact. (Layer A ×3 + prior pass.)
4. The board **persists as a durable artifact** (auto-save, revision/board history) in the standard account-held form; one documented exception pattern exists for walk-up device sessions (ephemeral until explicitly saved/claimed). (Layer A.)
5. **Sharing with graded access** (view/comment/edit), guests/visitors, and join codes/links. (Layer A ×3; Conceptboard positioning.)
6. **Facilitation machinery** for live sessions: timer, voting, follow/spotlight, laser pointer, presentation mode. (Layer A ×3; Conceptboard positioning.)
7. **Templates** and custom/team templates. (Layer A ×3; Conceptboard positioning.)
8. **Board migration as a family**: vendors import each other's *boards* (Miro↔FigJam↔Mural↔Jamboard↔Conceptboard↔Lucidspark) while treating *diagram files* as a separate import class. (Layer A — Miro, FigJam, Lucid.)
9. The **whiteboard name is the market's dominant category self-description**: Figma ("digital whiteboards"), Lucid ("virtual whiteboard"), Conceptboard ("online whiteboard"), Microsoft ("Whiteboard"), Excalidraw ("Whiteboard"). "Infinite/endless canvas" appears as a *surface* description (Miro, Mural), not as a competing category name.

### Named-convergence check (anti-overfitting)

- **"Whiteboard" vs "canvas" naming**: not a product split. The same products carry both words (Miro: endless *board* on an infinite *canvas*; Mural: "shared infinite canvas" selling whiteboarding; FigJam: "digital whiteboard" made of a *board*). One family, two names — the alias hypothesis is confirmed, not refuted.
- **Freehand drawing**: universal in the sample but not load-bearing — FigJam calls *stickies, shapes, connectors* the core; minimal forms (Excalidraw) are nearly freehand-only; both fit. Freehand is the Type's inherited signature act (L1, near-universal), not the invariant.
- **Facilitation kit**: present in all facilitation-positioned products, absent in minimal forms → L1/L2.
- **Walk-up device sessions**: documented at one product (Lucidspark) → treat the *pattern* (device-embedded sessions, explicit save) as a variant behavior, not an invariant or a universal claim.
- **Task machinery on the board** (cards, kanban, tracker widgets): present in several products but absent in minimal forms → L2.
- **"AI-first" positioning**: current-era marketing layer (Miro), not structure → L2.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant (smallest stable structure)

1. **Shared, persistent, spatially free board** — one visual surface, free of fixed page structure, is the unit of work; boards are durable, separately addressable, shareable artifacts. (Remove the shared board as unit → messaging/feed surfaces; remove spatial freedom → document/presentation editors; remove persistence → ephemeral live-meeting surfaces.)
2. **Direct marking and placed content** — participants add content by marking the surface directly (freehand strokes, writing) and by placing discrete movable objects (notes, shapes, text, media); content sits at positions and meaning comes from spatial arrangement, with no enforced structure. (Impose node–edge semantics with routing and notation behavior → diagramming application; remove placed objects and co-marking → personal painting/sketching application.)
3. **Multi-user co-marking** — multiple identified participants add and edit content on the same board together, live and/or asynchronously, their edits converging into one shared artifact. (Remove → personal infinite-canvas sketchbook / visual note-taking.)

This L0 is intentionally identical in structure to the Collaborative Canvas L0 (2026-09-06 pass) — because the evidence shows one product family, not two Types. The whiteboard name contributes an *emphasis* (the live marking-up of a surface together), not a separate invariant.

### L1 — Common Mature Structure

- Endless/zoomable surface with pan/zoom navigation, mini-maps, tables of contents
- Object toolkit: sticky notes, text, shapes, lines/connectors, images & media embeds
- Freehand pen with styling (color/thickness), erasers (object-level and pixel-level), and in some products stroke-to-shape recognition and highlighter/marker modes
- Named regions: frames / sections / pages / containers (vendor terms vary)
- Template libraries + custom/team templates
- Sharing by link/invite/join code; graded per-board access (view / comment / edit); guests/visitors; board ownership
- Facilitation set: timer, voting, follow/spotlight, laser pointer, presentation mode; private brainstorming modes and breakout boards in several products
- Comments, mentions, notifications; in-board chat; in-board audio/video in several products
- Revision history / board history with version recovery
- Import/export; cross-product **board** migration as a family (diagram files handled as a separate class)
- Team container: home/board list, folders, teams/projects/drafts
- Real-time presence: named cursors/avatars, collaborator colors, follow mode

### L2 — Variant / Optional Structure

- Delivery form: standalone platform / design-suite-embedded / meeting-suite-embedded (platform-native) / device-embedded walk-up / open-source self-hostable / embeddable
- Interactive-display hardware programs: certified devices, walk-up sessions, casting, join codes, finger-or-pen input
- Task/project machinery on the board: cards with assignees/due dates, kanban templates, task widgets, work-tracker integrations
- Structured organizers: tables, timelines, mind maps, presentation builders/slides inside the board
- Enterprise governance: SSO, admin panels, audit logs, plan tiers, compliance environments (e.g., FedRAMP-class), region-locked/on-premises hosting
- AI assistance (generate, cluster, summarize; AI-first positioning)
- Education deployments and education plans
- Visual-style philosophies (hand-drawn vs clean vector)
- Regional/compliance positioning (GDPR/EU hosting, public-sector procurement)

### L3 — Vendor-specific (research notes only; not for the final document)

- **Lucidspark**: Magic Shapes; Breakout Boards; private mode; Collaborator Colors/Color Legend; Join ID (create + 6-digit share); 8-digit casting code; walk-up session timeout with deletion; save-to-email (≤5 addresses; first claimer becomes owner; 24-hour claim window); universal canvas switching between Lucid products; Presentation Builder; Record a video; Lucid Cards; Notes tool; Dynamic Tables; Paths; find & replace; FedRAMP availability (freehand yes, device program no); customizable Primary Toolbar.
- **FigJam**: `figjam.new` shortcut; washi tape; emotes fade back to select; stamps; cursor chat; author-name default on stickies; 500-cell CSV table limit; open-session visitors; template publish to team vs organization; spotlight ignore grace window.
- **Miro**: "frames act like pages"; owner-only deleted-board restore; content recovery via Activity list; plan names (Free/Team/Consultant/Business/Education/Enterprise); "AI-first workspace" positioning; RealtimeBoard heritage visible in help-center domains.
- **Conceptboard**: freeze function; password-protected boards; board history version recovery; presentation slides created inside the board; brand color codes; German/EU hosting, dedicated server, on-premises; DVC availability; Cards feature; laser pointer and rounded corners as highlighted new features.
- **Mural**: LUMA Institute methodology services; Mural Accelerate; Surface Hub app.
- **Excalidraw**: open-source contribution model; embeddable editor positioning.
- **Microsoft Whiteboard**: (competitor-characterized only) M365 integration; simple/sketch-first positioning; no comparable granular access control per Conceptboard's claims — **not verified against Microsoft's own documentation**.

## Rejected Findings

- **"Freehand drawing is the defining invariant of the digital whiteboard."** Rejected as invariant: universal in the sampled products, but the Type's structure survives in object-first boards with modest freehand (FigJam treats stickies/shapes/connectors as core) and in nearly-freehand minimal forms (Excalidraw). Freehand is the inherited signature act — L1, near-universal — and the whiteboard name's characteristic emphasis.
- **"A digital whiteboard is ephemeral — it is wiped after the session, like a physical whiteboard."** Rejected as the modern default: account-held boards auto-persist with revision history across the sample. The ephemeral posture survives only as a documented device-embedded pattern (walk-up sessions that expire unless saved/claimed — evidenced at one product). Kept as a variant behavior.
- **"Sticky notes define the Type."** Rejected: FigJam calls stickies core, but minimal and platform-native forms satisfy the Type without them. L1.
- **"The canvas must be literally infinite."** Rejected: "endless/infinite" is a surface description at some vendors; the invariant is spatial freedom, not literal infinity.
- **"Digital Whiteboard and Collaborative Canvas are two distinct Application Types."** Rejected by the evidence: shared self-descriptions (Figma, Lucid, Conceptboard, Microsoft, Excalidraw all say "whiteboard"), shared migration family, shared object model, shared facilitation set, and no observed product population answering to "collaborative canvas" but not "whiteboard". The two directory leaves cover one market family; recorded as a Type Boundary Problem for taxonomy review.
- **"Digital whiteboard = interactive-whiteboard classroom lesson software."** Rejected: lesson authoring/delivery for teaching is a different job with different primary users; general-purpose whiteboards *run on* interactive displays (Lucidspark device program) but the Type is defined by shared visual co-creation, not curriculum delivery. Education *deployments* of whiteboards are a variant, not the definition.
- **"Meeting-suite whiteboards are a different Type because they live inside meeting tools."** Rejected: the embedded form (Microsoft Whiteboard in M365/Teams; Zoom Rooms whiteboard apps; Lucidspark inside Zoom/Meet meetings) satisfies the same core model; embedding is a delivery variant.

## Boundary Findings

1. **vs Collaborative Canvas — ALIAS (resolved to the extent this pass can resolve it).** The 2026-09-06 pass flagged "probable alias" from Figma/Excalidraw/Mural/Miro naming and migration evidence. This pass adds: Lucid's own help center defines Lucidspark as "a virtual whiteboard" (and separates it from Lucidchart, the *diagram* product, in the same FAQ); Conceptboard self-titles "the online whiteboard"; Conceptboard ships official head-to-head comparison pages against other *whiteboards* (Microsoft Whiteboard, Miro) — vendors in this space compare whiteboard-to-whiteboard; and the board-migration family (Miro/FigJam/Mural/Jamboard/Conceptboard/Lucidspark) is closed under the whiteboard name. No product population was found that answers to "collaborative canvas" but not "whiteboard", or vice versa. **Conclusion: one Application Type behind two directory names.** The working lens split remains descriptive, not structural: the *whiteboard* lens emphasizes the live session/facilitation surface (marking up together during a meeting, walk-up devices); the *collaborative canvas* lens emphasizes the board as a persistent co-created work artifact (frames/sections, templates, artifact estate). Products straddle both. Recommendation for taxonomy review: merge the leaves or declare one canonical name with the other as an alias; this document is written to stand alone while stating the relationship plainly.
2. **vs Diagramming Application — distinct Types (re-confirmed on this pass's evidence).** Lucid's own FAQ separates "Lucidchart (to build intelligent diagrams)" from "Lucidspark (to collaborate in a virtual whiteboard)"; Lucidchart imports Visio/Gliffy/draw.io/OmniGraffle *diagram files* while Lucidspark imports Miro/MURAL *boards*; FigJam's import list likewise separates boards from diagrams (consistent with the 2026-09-06 diagramming pass: Lucid ships two products; Miro's migration titles split boards vs diagrams; SmartDraw sells Diagramming and Whiteboarding separately). Structural discriminator: in diagramming, the shape+connector graph with routing behavior and notation semantics IS the artifact; in the whiteboard, free placement and marking are the artifact and connectors are auxiliary objects. Removal test: impose strict node–edge structure with diagram-type semantics → diagramming application.
3. **vs Collaborative Design Platform (04.01).** Design canvases produce production-grade artifacts with layers, components, precision vector tools; FigJam explicitly has **no layers panel** and positions ideation. Removal test: add layers/components/production fidelity → design platform.
4. **vs Collaborative Presentation Editor (03.04).** Presentations impose ordered fixed pages with linear delivery; whiteboards are spatially free, with presentation/follow mode as an *optional* navigation aid (and, at some vendors, slides built *inside* the board — a bridge feature, not a structure change). Removal test: make ordered pages the primary structure → presentation editor.
5. **vs Meeting / Webinar platforms.** Meeting tools treat the whiteboard as one surface among video/chat; whiteboard products make the board the primary container of the work. The embedded whiteboard inside a meeting suite is a delivery variant of this Type, not a separate one.
6. **vs Visual Note-taking Application (03.02).** Note-taking centers on personal capture and organization; the whiteboard centers on a shared team artifact being co-marked.
7. **vs Digital Painting Application / Raster Image Editor (04.02).** Painting tools serve a single author creating an artwork (canvas, brushes, layers, export as image); the whiteboard serves multiple co-markers building a shared board (presence, sharing, facilitation). Different users, different artifact, different workflow.
8. **vs Virtual Office Workspace (03.12).** Virtual offices organize persistent presence and encounters (rooms/avatars); whiteboards organize a shared artifact being co-marked.
9. **vs Kanban / Task boards (name collision).** "Board" in task tools means card-in-column workflow structure; here it means a spatial surface. Task machinery can live *on* a whiteboard (cards, kanban templates) as L2 without changing the Type.
10. **vs Interactive-display classroom lesson software (outside the directory).** Teacher-facing lesson authoring/delivery on interactive displays is a distinct job; the whiteboard Type is general-purpose visual co-creation that merely *runs on* the same hardware category. Kept conceptual — no lesson-software products were researched this pass.

## Historical / Market-Sample Check

- **Google Jamboard** (platform-native, hardware-anchored, discontinued; evidenced via official migration guides) satisfies the L0 structure without AI, integrations, or task machinery — definition holds.
- **Excalidraw** (minimal, open-source, individual tier) satisfies L0 with almost none of the L1 set — definition holds.
- **Conceptboard** (long-standing independent European vendor, compliance/on-premises posture) satisfies L0 with a regional/compliance emphasis — the definition is not bound to the US SaaS pattern.
- **Miro's RealtimeBoard heritage** (visible in the help center's underlying domains) shows the category predates the current AI-era marketing — the definition is not era-bound.
- **Walk-up device sessions** (Lucidspark on shared displays) show the Type's physical-whiteboard inheritance (walk up, mark, wipe) surviving *inside* a modern product as a bounded mode with explicit save — the persistent-artifact posture remains the standard form, and the ephemeral mode routes back into it via save/claim. The definition accommodates both without making either the invariant.
- The physical-whiteboard inheritance itself (meeting-room surface, markers, erasing) is the naming anchor of the category — every vendor name in the sample invokes it — which supports defining the Type as the digital counterpart of the shared marking surface rather than as any particular feature bundle.

## Uncertainties

- **Microsoft Whiteboard**: unreachable directly this pass and the prior pass; only name-level plus competitor characterization evidence. No Microsoft behavior claims are made anywhere in the outputs.
- **Zoom Whiteboard**: unreachable (three 404s); existence and meeting-suite embedding evidenced only indirectly through Lucid's device docs. Not characterized.
- **Conceptboard operational depth**: help center failed twice (timeout, transport error); all Conceptboard observations stay at official product-page level, and its self-described feature list (roles, board history, freeze, slides-in-board) is positioning-level, not operationally verified.
- **Miro role vocabulary**: "Roles in Miro" article returned 403 in the prior pass; roles asserted qualitatively from other reachable articles.
- **Mural operational depth**: support center unreachable in the prior pass; positioning-level only.
- **Historical session-scoped conferencing whiteboards** (early web-conferencing whiteboard surfaces): not directly evidenced in either pass; the persistence posture is modeled from the modern sample plus the Jamboard/Excalidraw checks. If such historical forms were ephemeral-only, the "persistent" property would need re-examination — flagged here rather than resolved by assumption.
- **Taxonomy decision**: whether DIRECTORY.md should merge "Digital Whiteboard" and "Collaborative Canvas" (or name one as alias of the other) is a taxonomy-level decision recorded in STATUS.md Boundary Issues; this pass does not modify the directory.

## Final Synthesis

A Digital Whiteboard is a shared, persistent, spatially free board — the digital counterpart of the meeting-room whiteboard — on which multiple identified people mark up and build content together: drawing and writing freehand, placing sticky notes, shapes, text, and media, arranging them spatially, and returning to the board afterwards as a durable team artifact. Mature products add an endless zoomable surface, named regions, template libraries, link/join-code sharing with graded access and guests, a facilitation set (timer, voting, follow/spotlight, laser pointer), comments and in-board chat/audio, revision history, import/export with cross-product board migration, and a team container listing boards. Delivery spans standalone platforms, design-suite-embedded boards, meeting-suite-embedded whiteboards, walk-up interactive-display sessions (ephemeral until saved), and minimal open-source forms. The market evidence — vendor self-descriptions, migration families, and feature structure — shows one product family behind the names "digital whiteboard" and "collaborative canvas"; the alias is recorded for taxonomy review, and the diagramming boundary (node–edge semantics vs free placement) remains the sharp structural seam of the section.
