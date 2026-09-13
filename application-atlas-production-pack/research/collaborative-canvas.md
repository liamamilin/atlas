# Research Notes — Collaborative Canvas

## Research Goal

Understand what a Collaborative Canvas application is from real products: what the shared surface is, what exists on it, how multiple people edit it together, what lifecycle and permissions apply, and where its boundary runs against Digital Whiteboard, Diagramming Application, Collaborative Design Platform, and presentation tools.

## Initial Boundary (working hypothesis before research)

- Hypothesis: a shared, spatially free (in practice "endless"/infinite) canvas board that multiple identified participants co-edit with placed movable objects, persisting as a durable team artifact.
- Nearest neighbors: Digital Whiteboard (same section 03.05), Diagramming Application (same section), Collaborative Design Platform (04.01), Collaborative Presentation Editor (03.04), Visual Note-taking Application (03.02), Virtual Office Workspace (03.12).
- Known risk: "Collaborative Canvas" and "Digital Whiteboard" may be two names for one market category. This was flagged as a question to resolve with evidence.

## Research Questions

1. What is the unit of work (board / mural / file / canvas)? Is it spatially bounded?
2. What objects exist on the surface? Is any object type defining?
3. How does multi-user co-editing present (presence, cursors, simultaneity)?
4. How is an unbounded space organized (frames, sections, pages, navigation)?
5. What is the board lifecycle (create → share → co-edit → persist/restore/export)?
6. What roles/permissions exist on a board?
7. Which capabilities are facilitation features (timers, voting, spotlight) vs core structure?
8. Where is the boundary vs diagramming tools, design canvases, and whiteboards?

## Representative Products

Selected for market representativeness, documentation depth, product philosophy, and customer tier:

| Product | Why selected | Evidence level reached |
|---|---|---|
| Miro | Market-leading collaborative canvas/whiteboard platform, enterprise tier, richest help center | Tier 1 (help center articles + category pages fetched) |
| FigJam (Figma) | Design-suite-embedded ideation canvas; different philosophy (lightweight, design-adjacent) | Tier 1 (Figma Learn category + Guide to FigJam fetched) |
| Mural | Facilitation-first positioning, enterprise workshops | Tier 2 only (official product page; support center unreachable) |
| Excalidraw | Minimal/open-source philosophy, individual tier | Minimal (page title + developer docs only) |
| Google Jamboard | Platform-native historical check (discontinued) | Indirect (existence + migration guides in Miro/FigJam docs) |
| Microsoft Whiteboard | Platform-native check (attempted) | Unreachable — abandoned per network rules |

## Sources

Research date: 2026-09-06

- Miro Help Center — https://help.miro.com/hc/en-us (root, FAQ) — fetched
- Miro Help Center — "What is Miro?" https://help.miro.com/hc/en-us/articles/360017730533-What-is-Miro — fetched
- Miro Help Center — "How to start collaboration with Miro" https://help.miro.com/hc/en-us/articles/360017571954-How-to-start-collaboration-with-Miro — fetched
- Miro Help Center — Getting Started category https://help.miro.com/hc/en-us/categories/360001415214-Getting-Started — fetched
- Figma Learn — FigJam category https://help.figma.com/hc/categories/360002051633 — fetched
- Figma Learn — "Guide to FigJam" https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam — fetched
- Mural — official product page https://www.mural.co/ — fetched (Tier 2)
- Mural support center https://support.mural.co/s/ — **failed twice (Salesforce Lightning "CSS Error"), abandoned per network rules**
- Excalidraw — https://excalidraw.com/ — JS shell; page title "Excalidraw Whiteboard" only
- Excalidraw — https://docs.excalidraw.com/ — developer/contributor docs only (fetched)
- Microsoft Whiteboard — microsoft.com product page blocked (automated-UA block), learn.microsoft.com path 404 — **abandoned**
- Miro "Roles in Miro" article — **403**, not fetched; role evidence taken from other reachable articles

## Product Observations

### Miro (evidence layer A — official help center)

- Positioning: "online collaborative workspace"; "AI-first online workspace for innovation"; targets distributed teams of any size; explicit meeting/workshop use ("organize meetings and workshops", video chat, presentation mode, sharing boards).
- Quick-start path: register a profile → create a board → start collaboration.
- Canonical canvas statement (Layer A, direct quote): "**Every board is saved automatically. Each board is endless, and frames act like pages.**" Navigation uses frames; templates from a library ("no need to start from scratch"); different content types addable.
- Sharing: "To share your board, click the **Share** button in the top right corner." Invite coworkers and remote colleagues; **real-time** brainstorming sessions **or async** work "with people from different time zones".
- Comment discussions; notifications of comments and mentions via email, browser, or Slack.
- Content types addable to a board (root FAQ): documents, spreadsheets, images, presentations, links with preview images, icons, embedded videos and other media; drag-and-drop, clipboard paste, file upload from computer or cloud storage.
- Board lifecycle: boards can be moved between teams and between profiles; deleted boards restorable **by board owners only** (via board link or trash bin); deleted **content** restorable via the board's Activity list ("Content Recovery" available on all plans).
- People model: team members vs **guests**; guests can be given access to specific boards to "view or comment" (root FAQ). A "Roles in Miro" article exists (fetch failed 403 — exact role vocabulary unverified).
- Containers: profile + **teams**; a **dashboard** surfaces boards per team; plan tiers Free / Team / Consultant / Business / Education / Enterprise; admin sections for team and enterprise administration.
- Competitive set as evidenced by official migration tooling: "Import Mural boards", "Import Conceptboard", "Import FigJam boards", "Import Jamboards" (called *boards*) vs "Import Draw.io diagrams", "Import Lucidchart diagrams", "Bulk import diagrams" (called *diagrams*). The vendor's own article titles separate the board family from the diagram family.
- Device surfaces: desktop app, mobile/tablet app, **interactive displays** for hybrid meetings, EMM configuration for managed mobile devices.
- Use-case intros maintained in help: ideation & brainstorming; strategy & planning; workshops & meetings.
- Performance FAQ: boards degrade with "a growing number of users and during intensive activity" and when "too heavy with content" — indirect evidence that many simultaneous co-editors on one board is a designed-for常态 and a real scaling concern.

### FigJam / Figma (evidence layer A — official Figma Learn)

- Positioning (direct quote): "FigJam is an online collaboration tool you and your team can use to brainstorm, develop, and organize ideas… Think of them as **digital whiteboards** where you and your team discover, explore, and execute on ideas." Help nav label: "FigJam — Collaborate with a digital whiteboard."
- Use cases listed: brainstorm and explore ideas; create decision trees, diagrams, and mind maps; run critiques or feedback sessions on designs; collect ideas/feedback/research; plan and run meetings/tutorials/interactive sessions; align stakeholders.
- File model: a FigJam file is a file type inside Figma, living alongside design files in **teams, projects, and drafts**; created from the file browser or `figjam.new`; iPad app exists; files have three regions: **the board**, the file toolbar, the tools-and-objects bar.
- Structure primitives: **pages** ("an extra layer of organization within your files"; separate activities/work streams/recurring meetings); **sections** ("cluster, contain, and move objects together on your board"); object toolkit: **stickies** ("the core for any FigJam board, along with shapes and connectors"; sticky carries the author's name by default), **shapes** (basic/flowchart/misc), **connectors** (elbow/straight; endpoints re-draggable between objects), **text** (point/area), drawing tools (marker, highlighter, washi tape).
- Organization aids: "tidy up" (rearranges selected objects into a uniform grid with even spacing).
- **No layers panel in FigJam files** (stated explicitly in the paste-from-Figma section) — a sharp structural contrast with Figma's design canvas.
- Templates: community template library ("Daily standup", "Prioritization matrix"); **custom templates** publishable by any member with **can edit** access to team or organization.
- Import: direct board import from **Google Jamboard, Miro, Mural, Lucid**; image import (PNG/JPEG/HEIC/GIF/TIFF/WEBP); paste from Figma Design; CSV import converts cells into a FigJam **table** (500-cell limit — product-specific precision, kept out of the final document); table-to-stickies conversion; **widgets** embed external app data (Asana, Jira tasks) as board objects.
- Meeting/facilitation set: **voting sessions** (participant choices hidden while voting, responses and tally revealed at end); meeting boards; comments/mentions; **cursor chat** (temporary message in the multiplayer cursor); **stamps** (stickers placed on the board or an object); **emotes** (temporary emoji bursts that fade); **audio conversations** (join an active call on the file); **spotlight** ("all collaborators… are notified you've requested they follow you" — everyone's viewport follows the facilitator); stickers and team/component libraries.
- Access control observed: "can edit" access gates template publishing; visitors can be invited to **open sessions** (article title "Invite visitors to an open session").

### Mural (evidence layer A-lite/B — official product page only; support docs unreachable)

- Positioning (direct quotes): "Mural is the visual AI platform that turns alignment into an ongoing way of working, connecting strategy to execution… in one shared workspace." "Reach your global team's outcomes faster with our **shared infinite canvas**" for "real-time collaborative workspaces."
- Use cases: brainstorming & ideation, agile practices, product development, strategic planning, customer journey mapping, process mapping, research & analysis, client collaboration, team building.
- Feature surface claimed on the product page: templates ("expert-designed methods"), Mural AI, integrations, **LUMA Institute** facilitation methodology (wholly-owned subsidiary), enterprise tier, Microsoft Teams app, Surface Hub app.
- Customer tiers: free signup for "Teams & individuals"; "Book a demo" for Enterprise.
- Limitation: operational detail (board internals, sections, timer, voting mechanics) could not be verified — support center failed twice with Lightning CSS errors. All Mural claims below the positioning level are unstated.

### Excalidraw (evidence layer A-minimal)

- The product's own page title: "**Excalidraw Whiteboard**" (page body is a JS app; no textual content retrievable).
- docs.excalidraw.com is developer documentation only: "For Excalidraw contributors or those integrating the Excalidraw editor"; "build your own app powered by Excalidraw" — evidence of open-source, embeddable posture.
- User-level behavior could not be verified from official sources. Used only to establish that a minimal, individual-first, open-source form exists in the same market and self-identifies as a whiteboard.

### Google Jamboard (indirect evidence, via competitors' official migration guides)

- Miro maintains "Import Jamboards to Miro"; FigJam maintains "Migrate Google Jamboards to FigJam". This establishes (a) Jamboard existed as a board product in this market, (b) it is discontinued/migrating, and (c) the market treats it as part of the same migration family as Mural/Miro/Conceptboard boards.
- Used for the historical/platform-native check: a discontinued, platform-native (Google account/device) whiteboard belongs to this Type.

### Microsoft Whiteboard

- Unreachable this pass (microsoft.com blocked automated access; learn.microsoft.com path 404). No claims made beyond the fact that the product exists.

## Cross-product Comparison

| Aspect | Miro | FigJam | Mural | Excalidraw |
|---|---|---|---|---|
| Unit of work | board ("endless", auto-saved) | FigJam file containing a board | mural on a "shared infinite canvas" | whiteboard (title-level evidence) |
| Self-description | "online collaborative workspace" | "digital whiteboard" | "visual AI platform… shared infinite canvas" | "Whiteboard" |
| Core objects | content items incl. docs, spreadsheets, images, presentations, links, icons, embedded video (FAQ) | stickies ("the core"), shapes, connectors, text, drawings | (positioning level only) | (not verified) |
| Organization | frames ("act like pages") | pages + sections + tidy up | (not verified) | (not verified) |
| Facilitation | video chat, presentation mode, workshop/meeting use cases | voting, timer, spotlight, audio, cursor chat, stamps, emotes | LUMA methodology positioning | none evidenced |
| Sharing/roles | Share button; guests with view/comment; board owners | can-edit access; open-session visitors; template publishing gated | free tier vs enterprise | link-based (not verified in detail) |
| Containers | profile + teams + dashboard | Figma teams/projects/drafts | enterprise workspace (positioning) | minimal/none evidenced |
| Migration family | imports Mural/FigJam/Jamboard/Conceptboard boards; Lucidchart/draw.io diagrams | imports Jamboard/Miro/Mural/Lucid | — | — |
| Delivery form | standalone SaaS + desktop/mobile/interactive display apps | embedded in Figma suite | standalone SaaS + Teams/Surface Hub apps | open-source web app + embeddable |

### Stable commonalities observed across the sample

1. One shared, spatially free surface is the unit of work, named board/mural/file/canvas by different vendors (Layer A for Miro/FigJam, positioning-level for Mural, title-level for Excalidraw).
2. Content is placed as movable discrete objects on that surface.
3. Multiple identified people edit the same surface together; real-time co-presence is the dominant mode, with async continuation explicitly supported (Miro states both modes; FigJam multiplayer mechanics pervasive).
4. The board persists automatically as a durable artifact (Miro auto-save statement; FigJam files in teams/projects).
5. Sharing by link/invite with graded access, and ownership of boards (Miro guests view/comment + owners; FigJam can-edit + visitors).
6. Templates and a library of starting structures (Layer A for Miro and FigJam; Mural positioning).

### Named-convergence check (anti-overfitting)

- "Infinite/endless" is claimed by Miro ("endless") and Mural ("infinite canvas") but not verbatim by FigJam in fetched text → treat unboundedness as a common implementation of "spatially free", not a defining invariant.
- Stickies are called "the core" by FigJam but are not present in minimal forms → L1, not defining.
- Facilitation kit (timer/voting/spotlight/audio) is present in FigJam (A), Miro (A, workshop positioning + video chat/presentation mode), Mural (positioning) but absent in Excalidraw → L1/L2.
- Team containers/dashboards absent in minimal forms → L1.
- AI assistance and integrations are current-market additions, not structure → L2.

## Canonical Model (with abstraction levels)

### L0 — Defining Invariant (smallest stable structure)

1. **Shared board/canvas** — one persistent, spatially free visual surface is the unit of work; multiple boards can exist side by side as separately addressable artifacts.
2. **Placed movable objects** — content exists as discrete, positioned, user-movable elements on the surface (notes, shapes, text, media, strokes, connectors).
3. **Multi-user co-editing** — multiple identified participants can edit the same board, with their edits converging into one shared artifact.

Removal tests: remove co-editing → personal sketching/image application; remove the free spatial canvas (fixed linear pages) → document/presentation editor; remove placed-object model → video surface or shared screen; remove persistence → ephemeral live meeting surface.

### L1 — Common Mature Structure

- Endless/zoomable surface with pan/zoom navigation
- Named regions for organization: frames / sections / pages (vendor terms vary)
- Object toolkit: sticky notes, text, shapes, connectors/lines, images & media, freehand drawing
- Template library + custom/team templates
- Sharing by link/invite; graded per-board access (view / comment / edit); board ownership; guests/visitors
- Comments, mentions, notifications
- Alignment/tidy-up aids
- Facilitation set: presentation/follow mode, timer, voting, in-canvas chat/reactions
- Import/export (images, documents; migration from other boards)
- Team/workspace container listing boards (dashboard)
- Real-time presence (named cursors/avatars) as the standard co-editing presentation

### L2 — Variant / Optional Structure

- Embedded audio/video conferencing on the board
- Integrations and embeds (task widgets, chat notifications, file-source imports)
- AI assistance (generate/summarize/cluster content)
- Delivery form: standalone SaaS / design-suite-embedded / platform-native / open-source self-host / embeddable component
- Enterprise governance (SSO, domain control, admin/EMM, plan tiers)
- Interactive-display / hybrid-room hardware support
- App/widget/sticker ecosystems
- Structured-content affordances (tables from spreadsheets, mind-map helpers)
- Visual-style philosophies (hand-drawn vs clean vector)
- Education deployments

### L3 — Vendor-specific (research notes only)

- Miro: "frames act like pages"; deleted-board restore is owner-only; content recovery via Activity list; plan names (Free/Team/Consultant/Business/Education/Enterprise); Slack notification delivery; EMM configuration articles.
- FigJam: `figjam.new` shortcut; washi tape; emotes fade back to select tool; spotlight's "ignore request" grace window; 500-cell CSV table limit; author-name default on stickies; template publish to team vs organization.
- Mural: LUMA Institute methodology services; Mural Accelerate; MCP server listing; Surface Hub app.
- Excalidraw: open-source contribution model; npm/embedding integration path.

## Rejected Findings

- **"A collaborative canvas is defined by sticky notes."** Rejected: FigJam calls stickies core, but the defining structure survives with only shapes/text/pen (minimal forms). Stickies = L1.
- **"The canvas must be infinite."** Rejected as invariant: claimed by two of four products in fetched text; the invariant is spatial freedom, not literal infinity.
- **"Facilitation tools (timer/voting/spotlight) define the Type."** Rejected: absent in minimal forms; L1/L2.
- **"A team workspace/dashboard is part of the definition."** Rejected: minimal and platform-native forms lack it; L1.
- **"Layers are part of the object model."** Rejected: FigJam explicitly has no layers panel; layer systems belong to design canvases — actually useful as a boundary marker.
- **"Real-time named cursors are definitional."** Held at L1: co-editing is the invariant; named real-time cursors are its dominant but implementation-level presentation (§24 historical check: even older and platform-native shared canvases already had live presence, so the distinction is conservative).

## Boundary Findings

1. **vs Digital Whiteboard — probable alias / single market category.** The researched market does not split the two names: Figma's own help center labels FigJam "a digital whiteboard"; Excalidraw self-titles "Whiteboard"; Mural sells "shared infinite canvas"; Miro's board is "endless". Products migrate freely among each other (Miro/FigJam migration tooling treats Mural/FigJam/Jamboard/Conceptboard as one family). Working distinction recorded for the two directory leaves: **whiteboard** lens emphasizes the live session/facilitation surface (marking up together during a meeting); **collaborative canvas** lens emphasizes the board as a persistent co-created work artifact with structured organization (frames/sections/pages, templates, integration into the team's artifact estate). Products straddle both; this document is written so that it remains valid under either lens, and the alias question is flagged for joint review.
2. **vs Diagramming Application.** Diagramming centers on structured node–edge semantics with diagram-aware behavior; the canvas Type centers on free placement where connectors are objects between objects. Market evidence: Miro's own migration titles separate "Import Lucidchart diagrams" / "Import Draw.io diagrams" from "Import Mural boards" / "Import FigJam boards" — the vendors themselves classify the two families differently. Removal test: impose strict node-edge structure with diagram-type semantics → diagramming application.
3. **vs Collaborative Design Platform (04.01).** Design canvases produce production-grade design artifacts with layers, components, and precision vector tooling; FigJam explicitly has **no layers panel** and positions ideation, not production design. Removal test: add layers/components/production fidelity → design platform.
4. **vs Collaborative Presentation Editor.** Presentations are ordered fixed pages with a linear delivery model; canvases are spatially free with follow/spotlight as an *optional* navigation mode rather than a structure.
5. **vs Visual Note-taking Application.** Note-taking is personal capture-centered; the canvas Type is team co-editing-centered on a shared artifact.
6. **vs Virtual Office Workspace.** Virtual offices organize persistent presence and serendipitous encounters (rooms/avatars); canvases organize a shared artifact being co-edited.
7. **vs Kanban/Task boards (name collision).** "Board" in task tools means card-in-column workflow structure; here "board" means a spatial canvas. Different Types despite the shared word.
8. **vs Virtual Meeting/Webinar platforms.** Meetings use a canvas as one shared surface among several (video, chat); the canvas Type makes the shared board the primary artifact and container of the work.

## Historical / Market-Sample Check

- Google Jamboard (platform-native, discontinued, evidenced via official migration guides) satisfies the L0 structure without templates, AI, integrations, or frames — definition holds.
- Excalidraw (minimal, open-source) satisfies L0 with almost none of the L1 set — definition holds.
- Mural's pre-AI positioning and Miro's pre-rebrand "RealtimeBoard" naming (visible in the help center's underlying realtimeboard domains) show the category predates current AI-era marketing — definition is not era-bound.
- Platform-native whiteboards embedded in communication suites (Teams-class) exist as a delivery variant (Mural ships Teams/Surface Hub apps; Miro documents interactive displays and hybrid meetings); they fit L0 as embedded forms.

## Uncertainties

- Mural's operational model (sections, timer, voting, board internals) unverified — support center unreachable ×2. All Mural statements kept at positioning level.
- Excalidraw's user-level collaboration behavior unverified (JS app + developer-only docs). Only existence/positioning/minimal-philosophy claims made.
- Miro's exact role vocabulary ("Roles in Miro" article 403). Roles asserted qualitatively (owner/guest view-comment observed in other articles).
- No distinct product family answering to "collaborative canvas" separate from digital whiteboards was found in this pass. The leaf is treated as the canvas-artifact lens on one market; alias question flagged.
- Microsoft Whiteboard unreachable — platform-native pole described conceptually only.

## Final Synthesis

A Collaborative Canvas is a shared, persistent, spatially free canvas board — the unit of work — on which multiple identified participants co-edit content as placed movable objects, with the board automatically preserved as a durable team artifact. Mature products typically add an endless/zoomable surface with named regions (frames/sections/pages), a toolkit of notes/text/shapes/connectors/media/freehand drawing, template libraries, link-based sharing with graded access and ownership, comments/notifications, facilitation controls (follow mode, timer, voting), import/export, and a team container listing boards. Delivery spans standalone platforms, design-suite-embedded ideation boards, platform-native whiteboards, and minimal open-source forms. The market research could not distinguish "Collaborative Canvas" from "Digital Whiteboard" as separate product categories — the two names cover the same products — and this is flagged for taxonomy joint review.
