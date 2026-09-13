# Digital Whiteboard

## Overview

A **Digital Whiteboard** is a shared, persistent, spatially free board that several people mark up and build on together — the digital counterpart of the meeting-room whiteboard. Participants draw and write directly on the surface, place sticky notes, shapes, text, and media anywhere on it, arrange and rearrange the content spatially, and do this at the same time, in the same place, with each person's contributions converging into one shared board that survives the session as a durable team artifact.

It solves a specific problem: when a group's thinking is visual and spatial — sketching a flow, clustering ideas, mapping a journey, working through options side by side — documents and slide decks force linear order, and a physical whiteboard cannot be shared with remote participants or kept afterwards. The digital whiteboard carries that room-surface experience online: anyone can pick up a pen or place a note, everyone sees it immediately, and the board is still there next week.

Its boundary: the whiteboard is a free-placement surface, not a structured model. Take away multi-user co-editing and it becomes a personal sketching application; impose fixed ordered pages and it becomes a document or presentation editor; impose strict shape-and-connector semantics and it becomes a diagramming tool; strip persistence entirely and it becomes an ephemeral live-meeting surface.

## Users & Context

Primary users are groups doing visual thinking work together:

- **Facilitators** — prepare a board for a brainstorm, workshop, or meeting (often from a template), guide participants' attention during the session (follow mode, laser pointer, timers), collect input, and run votes or grouping activities.
- **Contributors** — add and edit content on the board: writing and drawing freehand, placing and moving notes and shapes, connecting items, commenting, and voting. Contributors may be in the same room, fully remote, or both at once.
- **Viewers and stakeholders** — consult the board as a record of what was decided and produced, typically with view-only or commenting access.

Typical occasions: brainstorming and ideation, workshops and training sessions, team meetings and stand-ups, strategy and roadmap planning, user-journey and process mapping, research synthesis, retrospectives, and client-facing co-creation.

The context is deliberately hybrid. A distributed team co-edits live during a call (named cursors show who is doing what), and the same board is edited asynchronously between sessions. In meeting rooms, the board is frequently put on a large interactive display: people walk up and start drawing without logging in, remote colleagues join the same board from their laptops, and the session is saved to someone's account when it ends. Whiteboards are also embedded directly inside video-meeting and chat suites, where the board appears as one surface of the meeting.

## Core Model

### The defining core

```text
Board (shared, persistent, spatially free surface)
└── Direct marking + placed movable content (strokes, notes, shapes, text, media)
    └── Multi-user co-marking (several identified people, one shared artifact)
```

Three properties. If any one is removed, the product is no longer recognizable as a digital whiteboard:

- **Board as the unit of work** — one shared surface is the container of the work. A team keeps many boards side by side, each separately named, shared, owned, and returnable. The board — not a page, a message, or a file on disk — is what persists. Boards save themselves: in the standard form the board is preserved automatically and carries revision history, so the group can come back days later and find the work.
- **Direct marking and placed content** — content enters the board in two ways that mirror the physical whiteboard: by marking the surface directly (freehand strokes and handwriting with a pen, mouse, finger, or stylus) and by placing discrete objects (sticky notes, shapes, text, images and media, connector lines). Everything sits at a position on the surface and can be moved, resized, and rearranged. Nothing enforces structure: any object can sit anywhere and overlap anything; meaning comes from where the group puts things.
- **Multi-user co-marking** — several identified people add and edit content on the same board together. Live co-editing with named cursors and presence indicators is the standard presentation, and asynchronous editing of the same board between sessions is equally normal. Everyone's edits converge into one shared artifact.

The freehand mark is the whiteboard's inherited signature act — it is what makes the surface feel like a whiteboard rather than a form — but the Type is not defined by it alone: a board used mostly for notes and shapes is still a whiteboard, and minimal products that are almost entirely freehand are whiteboards too.

### Standard capabilities of mature products

These are common in current products and expected by the market, but they are not what makes the product a whiteboard:

- **Endless, zoomable surface** — the board extends far beyond any screen; people navigate by panning and zooming, often with a mini-map or overview.
- **Full object toolkit** — sticky notes, text, shapes, connector lines and arrows, images and media embeds, alongside the freehand pen.
- **Freehand depth** — pen styling (color, thickness), erasers at object and pixel level, and in some products automatic conversion of hand-drawn strokes into clean shapes.
- **Named regions** — frames, sections, or pages that divide a large board into navigable, movable, titleable areas, acting like pages without imposing reading order.
- **Template library** — pre-structured boards for common activities (standups, retrospectives, journey maps, prioritization matrices), plus team-internal custom templates.
- **Sharing and access model** — share by link, invitation, or join code; graded access per board (view / comment / edit); board ownership; guest or visitor access for people outside the team.
- **Facilitation set** — session timers, voting on objects with results revealed at the end, a follow/spotlight mode that brings every participant's viewport to the facilitator's view, a laser pointer for pointing out content, and presentation mode.
- **Conversation around the content** — comments and mentions on the board or its objects, notifications, in-board chat, and in several products in-board audio or video.
- **History** — revision history or board history, so changes can be reviewed and earlier versions restored.
- **Import and export** — bring in images, documents, and spreadsheets; export boards as images or documents; and, notably, migrate boards *from other whiteboard products* — vendors treat each other's boards as one migration family.
- **Team container** — a home area or workspace that lists boards and folders, separates personal drafts from shared work, and manages members.

### One structure, many implementations

The core model is conceptual; implementations differ in naming, surface, and depth:

```text
Concept:   Board              Implementations:  board, file, whiteboard, canvas
Concept:   Named regions      Implementations:  frames, sections, pages, containers
Concept:   Co-marking         Implementations:  live multiplayer editing with named cursors + async editing
Concept:   Access             Implementations:  link sharing, invitations, join codes, guests, open sessions
Concept:   Team container     Implementations:  workspace with board list and folders, project structure, or none in minimal forms
```

Minimal forms of the Type — a shared sketch surface with a pen and a few shapes — satisfy the defining core with almost none of the standard capabilities, which is why those capabilities are kept out of the definition.

## How It Works

### Create a board

```text
Create a new board (blank, or from a template)
→ the board lives in a personal draft or a team workspace
→ it is saved automatically from this moment on
```

Templates pre-place structured content (columns, matrices, mapped flows) so a session can start without setup; a blank board starts from an empty surface.

### Mark up and build the content

```text
Pick a tool (pen, sticky note, shape, text, connector, media)
→ draw or write directly on the surface, or place objects
→ move, resize, group, and align them
→ connect related items with lines and arrows
→ organize into named regions as the content grows
```

Arrangement is the primary expressive act: clustering similar items, ranking them spatially, sketching a flow between them. The system does not validate any of it — regions and tidy-up commands are conventions the group applies, not enforced schemas.

### Share and co-mark live

```text
Open the share dialog
→ invite by name/email, copy a link, or generate a join code
→ choose the access level for each audience (view / comment / edit)
→ collaborators open the same board
→ everyone marks the surface at once; named cursors show presence
→ the facilitator times activities, runs votes, and pulls attention with follow mode or a laser pointer
→ comments, chat, and reactions carry the conversation alongside the work
```

In meeting rooms, the same loop runs on a large interactive display: a person walks up and starts drawing without logging in, remote colleagues join the same board from their devices, and content from someone's laptop can be cast to the display with a short code.

### Close the loop

```text
Harvest outcomes (grouped conclusions, prioritized items, decisions)
→ keep the board as the persistent record, and/or
→ export it as an image or document
→ hand off outcomes to other tools (task trackers, documents) through imports, embeds, or integrations
```

In the walk-up device form, the ending is explicit: the session board is ephemeral until someone saves it to an account, and if nobody does, it is deleted after a timeout — the digital echo of wiping the physical whiteboard at the end of a meeting.

### Capability tiers

- **Defining core** — shared persistent spatially free board; direct marking and placed movable content; multi-user co-marking.
- **Standard in mature products** — endless zoomable surface; full object toolkit with freehand depth; named regions; templates; link/join-code sharing with graded access; facilitation set; comments/chat; revision history; import/export and cross-product board migration; team container.
- **Common variants and options** — embedded audio/video in the board; task cards, kanban templates, and work-tracker integrations on the board; tables, timelines, and mind-map organizers; presentation builders inside the board; AI assistance; interactive-display device programs; enterprise governance (SSO, administration, compliance hosting); education deployments; open-source self-hosted forms.

## Interfaces

### The board (primary surface)

- Purpose: the shared spatial workspace itself.
- Typical information: the placed content, other participants' named cursors and presence, the current viewport region.
- Primary actions: draw, write, place and edit objects, pan and zoom, select and arrange, connect.

### Tool tray / toolbar

- Purpose: create content.
- Typical information: tools for the pen, sticky notes, shapes, text, connectors, media, plus template, organizer, and widget access.
- Primary actions: select a tool, drop or draw content onto the surface.

### Share dialog

- Purpose: control who can reach the board and at what level.
- Typical information: link, join code, invited people, access levels, guest options.
- Primary actions: invite, copy link or code, set view/comment/edit access.

### Facilitation controls

- Purpose: run a live session.
- Typical information: timer state, voting state, follow/spotlight status, participant list.
- Primary actions: start/stop timer, run and reveal a vote, turn on follow mode, point with the laser pointer.

### Comments / chat

- Purpose: conversation anchored to the board's content.
- Primary actions: comment on the board or an object, mention a person, reply, resolve.

### Board list / home

- Purpose: the front door to the team's boards.
- Typical information: board names and thumbnails, folders, membership, drafts.
- Primary actions: create a board, open a recent board, organize, share or move boards.

## Important Rules / Behaviors

### Boards save themselves — with a walk-up exception

In the standard form, persistence is automatic and continuous: the board survives closing the browser and weeks of absence, and revision history lets the group review or restore earlier states. Some products add a walk-up device form with a different default: a board started on a shared interactive display without logging in is ephemeral until explicitly saved to an account, and is deleted if unclaimed — a bounded pattern that still routes into the persistent model through the save step.

### Access is graded per board

Each board carries its own access state: owner, editors, commenters, viewers, and — depending on the product — guests, anonymous link visitors, or join-code participants. Team membership grants a default; a specific board can always be shared more narrowly or more widely. Publishing a board as a team template is typically gated to edit-level members.

### Spatial freedom is real freedom

The system does not validate structure: any object can sit anywhere and overlap anything. Frames, sections, and tidy-up commands are user-applied conventions, not enforced schemas. This is the structural opposite of diagramming tools, which treat shape-and-connector relationships as data with routing behavior.

### Connectors follow their objects

Connector lines attach to the objects they join and, in common implementations, follow them as content is rearranged, preserving the relationships the group expressed.

### Concurrent edits converge

Multiple people editing the same object at the same time is a normal case; the system resolves and merges these edits into one shared state. Very large boards with very many simultaneous editors are a known performance consideration for products of this Type.

### Session state versus artifact state

The board is simultaneously a live session surface (cursors, timers, votes, laser pointers, reactions) and a durable artifact (history, comments, decisions). Transient session elements disappear when the session ends; content changes persist.

### Freehand strokes are objects

Drawings are not paint on a background: strokes are selectable, movable, styleable objects, and erase operations can be scoped — down to individual objects or pixel regions, and in some products a "clear all drawings" action removes only the drawings the current user created, not other people's.

## Variants

- **Standalone collaboration platform** — the whiteboard at the center of a wider visual-workspace product with administration, security, integrations, and services layers; sold to organizations of all sizes.
- **Design-suite-embedded board** — the whiteboard as a lightweight sibling inside a design tool's file system, optimized for idea exchange between design and non-design participants.
- **Meeting-suite-embedded whiteboard** — a whiteboard shipped inside a video-meeting or chat suite as one surface of the meeting; the same core model in embedded form.
- **Interactive-display / walk-up form** — the whiteboard anchored to meeting-room hardware: certified devices, no-login sessions, casting from personal devices, join codes for hybrid participation.
- **Facilitation-first platform** — positioned around structured workshop methods and facilitated programs, often with methodology services attached.
- **Minimal open-source / individual form** — a lean shared sketch surface, often self-hostable and embeddable, with few objects and no team container.
- **Compliance-hosting variants** — region-locked cloud, dedicated-server, or on-premises delivery for regulated and public-sector customers.
- **Education deployments** — classroom and student-group usage with education plan structures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Collaborative Canvas | same product family — the market runs one category behind the two names | vendors themselves use the names interchangeably (their products are marketed as "digital whiteboard", "virtual whiteboard", "online whiteboard", and "infinite canvas" at the same time), boards migrate freely between the products of both names, and no separate product population answers to one name but not the other. The whiteboard name emphasizes the live marking-up of a surface together; the canvas name emphasizes the board as a persistent co-created work artifact. The overlap is flagged in the atlas status for a taxonomy-level merge/alias decision |
| Diagramming Application | adjacent, structurally distinct | diagramming centers on structured shape-and-connector models with routing behavior and notation semantics; the whiteboard offers free placement where connectors are auxiliary objects. Vendors police the seam themselves: the same vendors ship diagram and whiteboard products separately, and their import flows treat diagram files and whiteboard boards as different families |
| Collaborative Design Platform | adjacent | design platforms produce production-grade artifacts with layers, components, and precision vector tools; whiteboards deliberately omit layer systems and position ideation, not production |
| Collaborative Presentation Editor | adjacent | presentations impose ordered fixed pages with linear delivery; whiteboards are spatially free, with follow/presentation mode as an optional aid rather than a structure |
| Meeting / Webinar Platform | adjacent | meeting tools treat the whiteboard as one surface among video and chat; the whiteboard Type makes the board itself the primary container of the work. Meeting-embedded whiteboards are a delivery variant of this Type |
| Visual Note-taking Application | adjacent | note-taking centers on personal capture and organization; the whiteboard centers on a shared team artifact being co-marked |
| Digital Painting / Raster Image Editor | adjacent | painting tools serve a single author creating an artwork with brushes and layers; the whiteboard serves multiple co-markers building a shared board with presence, sharing, and facilitation |
| Virtual Office Workspace | adjacent | virtual offices organize persistent presence and informal encounters (rooms, avatars); whiteboards organize a shared artifact being co-edited |
| Kanban / Task Board | name collision only | a task board is card-in-column workflow structure; a whiteboard board is a free spatial surface. Task machinery can live on a whiteboard as an added capability without changing the Type |

The boundary with **Diagramming Application** is the sharpest structural seam in this section of the atlas: free placement versus enforced node–edge semantics. The relationship with **Collaborative Canvas** is the opposite case — not a seam but an overlap: one market family, two directory names, recorded for taxonomy review.

## Representative Products

- **Miro** — standalone visual-collaboration platform; endless auto-saved boards, frames, templates, teams, interactive-display support
- **FigJam (Figma)** — design-suite-embedded board; stickies, sections, facilitation set; self-described by its vendor as "digital whiteboards"
- **Lucidspark (Lucid)** — the whiteboard sibling of a diagramming vendor; virtual-whiteboard positioning, full facilitation set, walk-up support on interactive-display devices
- **Conceptboard** — independent European vendor; online-whiteboard positioning with task management on the board and compliance/on-premises delivery
- **Microsoft Whiteboard** — platform-native whiteboard embedded in the Microsoft 365 / Teams ecosystem (included as the meeting-suite pole; not directly characterized from vendor documentation in this research)
- **Excalidraw** — minimal open-source whiteboard, individual/self-host tier

The discontinued, platform-native **Google Jamboard** (documented through competitors' official migration guides) was used to check that the definition does not over-fit to the current standalone-SaaS form.

## Sources

Research date: **2026-09-07** (with prior-pass evidence from 2026-09-06 where marked)

- Lucid Help Center — https://help.lucid.co/hc/en-us (root FAQ); Lucidspark category; "Welcome to Lucidspark"; "Freehand drawing in Lucidspark"; "Use Lucidspark on interactive whiteboard devices"
- Conceptboard — https://conceptboard.com/ ; https://conceptboard.com/conceptboard-vs-microsoft-whiteboard/
- Figma Learn — "Guide to FigJam" https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam
- Miro Help Center — "What is Miro?" https://help.miro.com/hc/en-us/articles/360017730533-What-is-Miro (plus 2026-09-06 pass: collaboration start guide, Getting Started category)
- 2026-09-06 pass: Mural product page (https://www.mural.co/); Excalidraw (https://excalidraw.com/, title-level); Google Jamboard evidenced via official migration guides in Miro and FigJam documentation

> Sourcing limitations: Microsoft Whiteboard could not be reached directly (automated access to the vendor's sites blocked; documentation path returned 404), so it is included at name-and-positioning level only, with a competitor's official comparison page as secondary characterization — no behavioral claims are made. Zoom Whiteboard could not be reached (product/support URLs returned 404) and is not characterized. Conceptboard's help center was unreachable after repeated attempts, so its observations stay at official product-page level. Miro's roles article was not reachable (403) in the prior pass, so role names are described qualitatively. Mural's support center was unreachable in the prior pass. No precise vendor limits, numeric defaults, or plan-gated figures are asserted in this document; product-specific behaviors are marked as such where they appear.

Detailed evidence, product-by-product observations, cross-product comparison, abstraction analysis, and boundary reasoning are recorded in the paired Research Notes.
