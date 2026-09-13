# Collaborative Canvas

## Overview

A **Collaborative Canvas** is a shared, persistent, spatially free visual surface — usually called a board — that multiple identified people edit together as their unit of work. Content exists as movable objects placed on the surface (notes, shapes, text, media, drawings, connectors), several participants can edit the same board at the same time or at different times, and the board is automatically preserved as a durable shared artifact that the team returns to and builds on over time.

It solves a specific coordination problem: when a team's thinking is spatial — clustering ideas, mapping flows, arranging and rearranging options together — linear documents and slide decks cannot hold it, and physical whiteboards cannot be shared across locations. The collaborative canvas carries that spatial work into a shared digital artifact.

Its boundary: the canvas is a free-placement surface, not a structured model. Remove multi-user co-editing and it becomes a personal sketching application; impose fixed linear pages and it becomes a document or presentation editor; impose strict node–edge structure and it becomes a diagramming tool; strip persistence and it becomes an ephemeral live meeting surface.

## Users & Context

Primary users are teams doing visual thinking work together:

- **Facilitators** — run a brainstorming, planning, or workshop session on the board: prepare it from a template, guide participants' attention, time activities, collect input, and harvest outcomes.
- **Contributors** — place and edit content on the board during a live session or on their own schedule; typical activities include adding notes and ideas, grouping and sorting, drawing, connecting items, and commenting.
- **Viewers and stakeholders** — consult the board as a record of decisions and outcomes, with read-only or commenting access.

Typical occasions: brainstorming and ideation, workshops and team meetings, strategy and roadmap planning, user-journey and process mapping, research synthesis, critiques and feedback sessions, and client-facing co-creation sessions.

The work context is deliberately hybrid in time and space: distributed teams co-edit live during a session (named cursors show who is doing what), and the same board is later edited asynchronously across time zones. In-room participation through large interactive displays is a common extension, with the board serving as the shared surface between physical and remote participants.

## Core Model

### The defining core

```text
Board (shared, persistent, spatially free canvas)
└── Placed movable objects (notes, shapes, text, media, strokes, connectors)
    └── Multi-user co-editing (multiple identified participants, one shared artifact)
```

Three properties. If any one is removed, the product is no longer recognizable as a collaborative canvas:

- **Board as unit of work** — one shared surface is the container of the work; a team maintains many boards side by side, each separately addressable and shareable. The board, not a page or a message thread, is what gets named, shared, owned, and archived.
- **Placed movable objects** — everything on the board is a discrete object that sits at a position on the surface and can be moved, resized, grouped, and arranged. There is no fixed reading order; meaning comes from spatial arrangement.
- **Multi-user co-editing** — several identified participants edit the same board, and their edits converge into one shared artifact. Live co-editing with named cursors and avatars is the standard presentation; asynchronous continuation on the same board is equally supported.

The board persists automatically. Users do not save; the board's state survives sessions, closing the browser, and weeks of absence. This persistence is what turns a live session surface into a team artifact.

### Standard capabilities of mature products

These are common in current products and expected in the market, but they are not what makes the product a collaborative canvas:

- **Endless, zoomable surface** — the board extends far beyond any screen; users navigate by panning and zooming.
- **Named regions** — frames, sections, or pages divide a large board into navigable, movable, titleable areas, acting like pages without imposing order.
- **Object toolkit** — sticky notes, text, shapes, connectors and lines between objects, images and media embeds, documents and links with previews, and freehand drawing tools.
- **Template library** — pre-structured boards for common activities (standups, retrospectives, journey maps, prioritization matrices), plus the ability to publish team-internal custom templates.
- **Sharing and access model** — share by link or invitation; graded access per board (view / comment / edit); board ownership; guest or visitor access for people outside the team.
- **Comments and notifications** — discussion attached to the board or to specific objects; mentions; notification delivery through email and chat tools.
- **Organization aids** — align and tidy-up commands that arrange selected objects into clean grids and spacing.
- **Facilitation set** — a follow/spotlight mode that brings every participant's viewport to the facilitator's view, session timers, voting on objects, and lightweight in-canvas chat and reactions.
- **Import and export** — bring in images, documents, and spreadsheets (spreadsheets commonly convert into on-board tables or note grids); export boards in shareable formats; migrate content from other board products.
- **Team container** — a workspace or team area that lists boards, manages members, and separates personal drafts from shared work.

### One structure, many implementations

The core model is conceptual; implementations differ in surface size, naming, and depth:

```text
Concept:   Board                    Implementations:  board, file, canvas, whiteboard
Concept:   Named regions            Implementations:  frames, sections, pages
Concept:   Co-editing               Implementations:  live multiplayer editing with named cursors + async editing
Concept:   Access                   Implementations:  link sharing, invitations, guests, open sessions
Concept:   Team container           Implementations:  team workspace + dashboard, project folders, or none in minimal forms
```

Minimal forms of the Type (a shared sketch surface with a pen and shapes) satisfy the defining core with almost none of the standard capabilities — which is why those capabilities are kept out of the definition.

## How It Works

### Create a board

```text
Create a new board (blank or from a template)
→ the board exists inside a team workspace or personal drafts
→ it is saved automatically from this moment on
```

Templates pre-place structured content (columns, matrices, mapped flows) so a session can start without setup; a blank board starts from an empty surface.

### Place and arrange content

```text
Pick a tool (note, shape, text, pen, connector, media)
→ place objects on the surface
→ move, resize, group, and align them
→ connect related objects with lines and arrows
→ organize into named regions as the content grows
```

Arrangement is the primary expressive act: clustering similar items, ranking them spatially, drawing flows between them. Nothing enforces structure — regions and tidy-up commands are conventions the team applies.

### Share and co-edit

```text
Open the share dialog
→ invite by name/email or copy a link
→ choose the access level for each audience (view / comment / edit)
→ collaborators open the board
→ everyone edits the same surface; named cursors show presence
→ comments, mentions, and reactions carry the conversation alongside the work
```

Editing is concurrent. During a live session, a facilitator can bring all viewports to their own view, time activities, and run votes on the objects on the board; how votes are tallied and revealed varies by product. After the session, the same board remains open for asynchronous additions.

### Close the loop

```text
Harvest outcomes (decisions, grouped conclusions, prioritized items)
→ keep the board as the persistent record, and/or
→ export it as an image or document
→ hand off outcomes to other tools (task trackers, documents, tickets) through imports, embeds, or integrations
```

### Capability tiers

- **Defining core** — shared persistent board; placed movable objects; multi-user co-editing.
- **Standard in mature products** — endless zoomable surface; named regions; full object toolkit; templates; link-based sharing with graded access; comments/notifications; facilitation set; import/export; team container.
- **Common variants and options** — embedded audio/video calls; task-widget and chat integrations; AI assistance for generating, clustering, or summarizing content; interactive-display support; enterprise governance (SSO, administration); app and sticker ecosystems; open-source self-hosted forms.

## Interfaces

### The board (primary surface)

- Purpose: the shared spatial workspace itself.
- Typical information: the placed objects, other participants' named cursors, the current viewport region.
- Primary actions: place and edit objects, pan and zoom, select and arrange, draw, connect.

### Tool bar / object trays

- Purpose: create content.
- Typical information: tool icons for notes, shapes, text, connectors, pen, media, plus template and sticker/widget access.
- Primary actions: select a tool, drop an object onto the surface.

### Team dashboard / board list

- Purpose: the front door to the team's boards.
- Typical information: board names, thumbnails, membership, teams/projects/drafts.
- Primary actions: create a board, open a recent board, move or share boards.

### Share dialog

- Purpose: control who can reach the board and at what level.
- Typical information: link, invited people, access levels, guest/visitor options.
- Primary actions: invite, copy link, set view/comment/edit access.

### Facilitation controls

- Purpose: run a live session.
- Typical information: timer state, voting state, spotlight status, participant list.
- Primary actions: start/stop timer, run and reveal a vote, turn on follow/spotlight mode.

### Comments / notifications

- Purpose: conversation anchored to the board's content.
- Primary actions: comment on the board or an object, mention a person, resolve or reply.

## Important Rules / Behaviors

### Boards save themselves

Persistence is automatic and continuous. Recovery machinery (trash for deleted boards, restore of deleted objects) exists in mature products; who may restore a deleted board — for example, whether it is limited to the board's owner — depends on the product.

### Access is graded per board

Each board carries its own access state: owner, editors, commenters, viewers, and — depending on the product — guests or anonymous link visitors. Team membership grants a default; a specific board can always be shared more narrowly or more widely. Template publishing is typically gated to edit-level members.

### Spatial freedom is real freedom

The system does not validate structure: any object can sit anywhere and overlap anything. Frames, sections, and tidy-up commands are user-applied conventions, not enforced schemas. This is the structural opposite of diagramming tools, which treat node–edge relationships as data.

### Connectors follow their objects

Connectors attach to the objects they join and, in common implementations, follow them as content is rearranged, preserving expressed relationships.

### Concurrent edits converge

Multiple participants editing the same object is a normal case; the system resolves and merges these edits into one shared state. Very large boards and very many simultaneous editors are a known performance consideration for products of this Type.

### Session state versus artifact state

The board is simultaneously a live session surface (cursors, timers, votes, reactions) and a durable artifact (history, comments, decisions). Transient session elements disappear when the session ends; content changes persist.

## Variants

- **Enterprise collaboration platform** — the board at the center of a wider innovation/workspace platform with administration, security, integrations, and consulting/services layers; sold to large organizations.
- **Design-suite-embedded ideation board** — the canvas as a lightweight sibling inside a design tool's file system, optimized for idea exchange between design and non-design participants rather than production artifacts.
- **Facilitation-first platform** — positioned around structured workshop methods and facilitated programs, with methodology services attached.
- **Minimal open-source / individual form** — a lean shared sketch surface, often self-hostable and embeddable, with few objects and no team container.
- **Platform-native / communication-suite whiteboards** — a canvas embedded in a meeting or chat suite as one surface among video and messaging; fits the same core model in embedded form.
- **Education deployments** — classroom and student-group usage with education plan structures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Digital Whiteboard | nearest neighbor — the market largely treats the two as one product family | the whiteboard lens emphasizes the live session/facilitation surface during meetings; the collaborative canvas lens emphasizes the board as a persistent co-created work artifact; the same products serve both, and the two directory leaves overlap heavily (flagged for joint review) |
| Diagramming Application | adjacent | diagramming centers on structured node–edge models with diagram-aware semantics; canvas tools offer connectors as free objects, with no enforced diagram structure |
| Collaborative Design Platform | adjacent | design platforms produce production-grade artifacts with layers, components, and precision vector tools; ideation canvases deliberately omit layer systems |
| Collaborative Presentation Editor | adjacent | presentations impose ordered fixed pages with linear delivery; canvases are spatially free, with follow-mode navigation as an optional aid rather than a structure |
| Visual Note-taking Application | adjacent | note-taking centers on personal capture and organization; the canvas centers on shared team co-editing of one artifact |
| Virtual Office Workspace | adjacent | virtual offices organize persistent presence and informal encounters; canvases organize a shared artifact being co-edited |
| Kanban / Task boards | name collision only | a task board is card-in-column workflow structure; a canvas board is a free spatial surface — unrelated structures sharing a word |
| Meeting / Webinar Platforms | adjacent | meetings use a canvas as one surface among video and chat; the canvas Type makes the board itself the primary container of the work |

The boundary with **Digital Whiteboard** is the important one: in the researched market, vendor naming ("digital whiteboard", "infinite canvas", "endless board") and official migration paths between products show a single product family behind the two names. This document holds the canvas-as-persistent-artifact lens; the alias question is recorded in the atlas status for joint review.

## Representative Products

- Miro — standalone enterprise collaboration platform; board, frames, templates, teams
- FigJam (Figma) — design-suite-embedded ideation board; stickies, sections, facilitation set
- Mural — facilitation-first visual collaboration platform; shared infinite canvas, workshop methods
- Excalidraw — minimal open-source whiteboard, individual/self-host tier

Platform-native whiteboards embedded in communication suites (and the discontinued platform-native sample Google Jamboard, documented via competitors' official migration guides) were used to check that the definition does not over-fit to the standalone SaaS form.

## Sources

Research date: **2026-09-06**

- Miro Help Center — https://help.miro.com/hc/en-us (root & FAQ); "What is Miro?" (articles/360017730533); "How to start collaboration with Miro" (articles/360017571954); Getting Started category (categories/360001415214)
- Figma Learn — FigJam category (https://help.figma.com/hc/categories/360002051633); "Guide to FigJam" (articles/1500004362321)
- Mural — official product page https://www.mural.co/
- Excalidraw — https://excalidraw.com/ (page title only); developer docs https://docs.excalidraw.com/
- Google Jamboard — evidenced indirectly through official migration guides in Miro and FigJam documentation

> Sourcing limitation: Mural's support/help center was unreachable (repeated rendering errors; abandoned after two attempts), so Mural claims stay at official product-page positioning level. Excalidraw's site is an application shell and its public docs are developer-oriented, so only existence, self-description, and open-source posture are asserted for it. Miro's roles article was not reachable (403), so role names are described qualitatively from other reachable articles. Microsoft Whiteboard could not be reached and is not characterized here. No precise vendor limits, plan-gated figures, or numeric defaults are asserted in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
