# Visual Note-taking Application

## Overview

A **Visual Note-taking Application** is a personal knowledge tool whose primary working surface is a persistent, free two-dimensional **board** on which the user places pieces of their own notes and materials, and composes meaning by *arranging* them — position, grouping, and connecting lines carry the structure, instead of lists, folders, or tags.

The defining structure is small:

```text
Board (persistent free 2D space)
└── Authored content pieces placed freely on it
    └── Spatial arrangement as the primary organization
        └── Personal, private-by-default notes library
```

Everything commonly associated with modern products — infinite zoomable canvases, web clippers, templates, tags, search, cloud sync, real-time collaboration, AI assistance, freehand drawing — is widespread today but is not what makes the product a visual note-taking tool. A single-user desktop program whose boards are plain local files satisfies the definition completely.

When the working surface stops being a personal notes library — when boards become a team's shared co-marking surface, a notation-driven diagram, or a tree the application lays out itself — the product has drifted into a neighboring Application Type (Digital Whiteboard, Diagramming Application, Outliner / mind mapping).

## Users & Context

The primary user is an individual thinking through material that does not fit a linear page: a creative professional collecting visual references for a project, a student or researcher spreading readings and ideas across a surface to see how they relate, a writer mapping characters and plot lines, a planner clustering tasks and priorities on a wall of notes.

Typical reasons to open the application:

- spread notes, images, files, and links out side by side to see patterns and connections
- cluster related pieces into groups and rearrange them as understanding changes
- draw a line between two pieces to record that they relate
- break a big topic into sub-boards and move between them
- capture material from the web or quick thoughts, then place it where it belongs

The context is personal knowledge work: the boards are the individual's own accumulating notes, private by default. Sharing exists — a board can be sent to a colleague for feedback or, in some products, edited together — but collaboration is a delegated capability, not the default posture. This is the structural difference from team whiteboards, where multi-user co-marking is the point.

## Core Model

### The Defining Core

```text
Board (persistent free 2D space)
└── Authored content pieces placed freely on it
    └── Spatial arrangement as the primary organization
        └── Personal, private-by-default notes library
```

Four properties. If any one is removed, the product is no longer recognizable as a visual note-taking application:

- **Board as the unit of record** — a persistent, individually addressable two-dimensional space the user keeps and returns to. Boards accumulate over time into the user's working library, and mature products let boards contain other boards. Without persistence and accumulation, the surface is a scratchpad, not a notes tool.
- **Authored content pieces placed freely** — the content is the user's own notes and materials: text notes and cards, images, files, links, sketches — self-contained pieces the user places wherever they choose. The content is not drawn from an application-supplied vocabulary of notation shapes; that is the diagram editor's model.
- **Spatial arrangement as the primary organization** — meaning is composed and read through placement. Where a piece sits, what it sits next to, what group encloses it, and which pieces are joined by a line — these carry the structure. The layout is the organization itself, not a rendering computed from an underlying list or tree. This is the property that separates the Type from list-based note apps (which organize through containers, tags, and search) and from mind mappers (which compute the layout from a tree the user defines).
- **Personal knowledge-notes posture** — the boards hold the individual's own accumulating notes and materials, private by default; sharing and collaboration are capabilities the user grants, not the co-creation default. Remove this and the product is a team whiteboard.

### What Lives on the Board

Content pieces vary in richness across products, but mature products converge on a broad set:

- **Notes and cards** — the basic authored piece: a text note that can grow from a one-line thought into a long-form document.
- **Visual material** — images, videos, audio, color swatches; for creative work the board often holds more imagery than text.
- **Files and documents** — PDFs and other files placed on the board, in some products with annotation.
- **Links and web content** — saved pages and clippings, usually captured with a browser clipper.
- **Structured pieces** — to-do lists, tables, and occasionally map or embed cards.
- **Sketches** — freehand drawing directly on the board, where supported.

### How the Board Is Organized

- **Grouping containers** — sections, background shapes, columns, and similar regions that enclose related pieces. Containment by proximity is a first-class organizing act.
- **Connecting lines** — lines and arrows drawn between pieces. In every researched product these are an added layer of meaning over free placement, not a required structure: pieces do not need connections to belong on the board.
- **Board hierarchy** — boards commonly nest inside boards (a main project board holding sub-boards per section or subtopic), with breadcrumb-style navigation showing the path. One product instead keeps each board as a standalone document file; the nesting habit is common, not definitional.
- **Library-level retrieval** — search across boards and pieces, plus labels, tags, or properties, so that material placed long ago can be found again. Some products add an inbox: material captured before it has been placed lands in an "unsorted" area until the user files it onto a board.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ on a stable set of axes:

```text
Concept:            Board as unit of record
Implementations:    cloud-synced boards, local document files, project files containing many boards

Concept:            Content pieces
Implementations:    free-standing cards, cards held in a library and placed on boards by reference,
                    figures inside project files, plain text notes

Concept:            Arrangement
Implementations:    drag-and-drop free placement everywhere; grouping by sections, background
                    shapes, columns, or compositions; connections as drawn lines/arrows

Concept:            Personal posture
Implementations:    single-user desktop files, private cloud workspace with share-on-demand,
                    personal knowledge base with optional real-time co-editing
```

A reader who has only seen one implementation — say, a cloud canvas for creative teams — should still be able to recognize a single-user desktop "sheet of paper" product as the same Type from the core model.

## How It Works

### Set up a space and fill it

```text
Create a board (or open an existing one)
→ place pieces on it: write a note, drop in an image or file, save a link
→ position each piece where it makes sense
→ group related pieces (section, background shape, column)
→ connect pieces with lines where a relationship matters
```

There is no outline to maintain and no schema to obey. The board starts empty and takes shape as the user works; the arrangement is built up piece by piece, and rearranging is a normal, expected act — unlike paper, nothing is ever in the wrong place permanently.

### Grow the library

```text
Create sub-boards for subtopics (or keep boards as separate documents)
→ capture material from anywhere: web clipper, quick-capture inbox, file drag-in
→ place captured material onto the board where it belongs
→ return later: navigate boards (breadcrumbs / board list), search, browse tags
```

The capture-and-return loop mirrors other note tools — get material in quickly, find it reliably later — but the "filing" step is placement: deciding *where on the spatial map* a piece belongs, not which folder it goes in.

### Think in the arrangement

The characteristic working loop of the Type is iterative recomposition: spread the material out, read the layout, move pieces, regroup, redraw connections. The board is both the working surface and the artifact — a user can come back weeks later and re-enter the thinking context simply by seeing what sits next to what. Some products reinforce this by letting the same piece of content appear on several boards, so one idea can participate in multiple topic arrangements.

### Share or deliver

```text
Share a board (commonly with everything nested under it) for view or comment
→ or export: print, PDF, images, or document formats
```

Sharing is on demand. Export turns the arrangement into a static artifact for people outside the tool.

### Core vs Common vs Optional

**Defining core** — without these, not a visual note-taking application:

- persistent board as the unit of record
- authored content pieces placed freely on it
- spatial arrangement as the primary organization
- personal, private-by-default notes posture

**Common mature structure** — present in most modern products:

- content-type breadth (images, files, links, to-dos, tables, media)
- connecting lines/arrows as an added layer
- grouping containers (sections, shapes, columns)
- board nesting / hierarchy above the canvas
- capture surfaces (web clipper, quick-capture inbox)
- library search, tags/labels
- templates
- zoom/pan navigation with orientation aids
- export/print/share outputs
- multi-device sync

**Variant / optional** — depends on product philosophy and segment:

- storage substrate: cloud service vs local files
- purpose emphasis: creative project boards vs learning/research vs writing/thinking
- collaboration depth: none → share-for-comment → real-time co-editing
- freehand sketching/drawing
- structured organizers inside the canvas (mind-map objects, kanban stacks, tables)
- AI assistance
- business model: subscription vs one-time purchase

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### The board (canvas)

The primary surface — an open two-dimensional space.

- the placed pieces themselves, at their positions, with their grouping and connections
- primary actions: create a piece, drag to position, resize, group, connect, color/style

### Board navigation

How the user moves among boards.

- breadcrumb path of nested boards, or a board list / project organizer
- primary actions: open a board, create a sub-board, move a board, jump home

### Capture surfaces

How material gets in.

- web clipper (save text/images/links from the browser straight onto a board)
- quick-capture inbox or companion app (material lands "unsorted" until placed)
- drag-and-drop of files from the desktop

### Library retrieval

- search across boards and piece content
- tags/labels/properties; sometimes saved filters

### Piece editor

The inside of a content piece.

- text formatting (deliberately restrained in most products), lists, checklists, embedded media
- primary actions: edit content, convert note to long-form document, duplicate, move to another board

### Share / export

- share dialog (view/comment/edit grants, cascading to nested boards)
- export to PDF/image/print/document formats

## Important Rules / Behaviors

### Placement is meaningful and persistent

Where a piece sits is content, not cosmetics. Moving a piece changes the board's meaning; the application preserves positions exactly as left. This is the behavior that makes the board a thinking artifact rather than a formatting surface.

### Connections are optional and non-structural

Pieces do not need connections to exist on the board, and connections do not constrain placement. A piece with no lines is a full citizen of the board. (In diagram editors, by contrast, the connector is load-bearing.)

### Boards accumulate; nothing is ephemeral

The board and its pieces persist across sessions indefinitely. There is no "session end" that clears the surface — that behavior belongs to meeting whiteboards.

### Privacy is the default; sharing is granted

Boards are private to the user until explicitly shared. Where nesting exists, sharing a parent board commonly grants access to its nested sub-boards, and permission changes cascade downward.

### The arrangement tolerates mess

Products deliberately avoid forcing structure: no required hierarchy, no auto-tidying of positions, no schema. Structure emerges from the user's arrangement and can stay loose indefinitely. Products that *do* compute layout from an underlying structure have crossed into mind-mapping/outliner territory.

## Variants

- **Creative project boards** — mood boards, storyboards, creative briefs; image-heavy, template-assisted, cloud-based, aimed at designers, filmmakers, marketers, writers.
- **Learning and research boards** — cards holding reading notes and highlights arranged on whiteboards per topic; PDF annotation and reference-tool integration; aimed at students and researchers.
- **Writer's idea sheets** — freeform "virtual paper" for capturing thoughts and joining them up; single-user desktop, one-time purchase; often feeds a separate writing application.
- **Freeform project notebooks** — a project file containing many freeform spaces plus structured collections (lists, mind maps, index cards, tables) and rich metadata; local-first, power-user oriented.
- **Mind-map-adjacent tools** — products that capture ideas on a canvas but lay the map out automatically from a tree structure, often with an outline mode. These sit at the boundary of this Type, the outliner, and diagramming; the auto-computed layout (rather than user arrangement) is the tell.

A variant remains a variant unless it changes the core model: if arrangement stops being the organization (auto-layout trees), the surface stops being personal (team co-marking), or the content stops being the user's own pieces (notation shapes), a different Application Type has begun.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Note-taking Application | closest sibling | organizes a personal library of note records through containers/tags/search; here the spatial arrangement itself is the organization — its own vendors draw this line ("traditional notes apps separate your notes into silos accessed by tags and search terms… arrange your notes side by side") |
| Personal Knowledge Management Application | closest sibling | the point is the growing cross-note link network (connections as the structure); here the point is the arrangement (placement and grouping), with connections an added layer |
| Outliner | sibling | the point is the indentation tree operated on directly; here pieces are placed in 2D, not nested in a tree |
| Digital Whiteboard / Collaborative Canvas | adjacent | multi-user co-marking converging on a shared team artifact is the point; here boards are personal notes, private by default, sharing delegated |
| Diagramming Application | adjacent | shapes from a notation vocabulary with connectors that route and stay attached are the artifact; here content is authored notes/materials and lines are auxiliary |
| Mind mapping (no dedicated directory leaf) | boundary population | tree structure with auto-computed layout and usually an outline mode; structure-first rather than arrangement-first |
| Presentation Application | adjacent | bounded, ordered slides for sequential delivery vs an open, unordered, personally navigated space |
| Bookmark Manager / Read-it-later | adjacent | records that point at external resources vs authored pieces; the web clipper is the hinge between them |

The boundary with Note-taking and PKM is the most important one, because all three are personal knowledge tools over accumulated notes. The structural test is *what carries the organization*: containers/tags/search (note-taking), the link network (PKM), or the spatial arrangement itself (this Type). Products can straddle; center of gravity decides.

## Representative Products

- **Milanote** — visual boards for creative work; self-describes as a visual note-taking app; boards nest, private by default, web clipper, template library
- **Heptabase** — visual knowledge base for learning and research; cards held in a library and placed on whiteboards; sub-whiteboards, PDF annotation, bi-directional links
- **Scapple** — freeform "sheet of paper" for writers; notes anywhere, connections optional, desktop one-time purchase
- **Curio** — freeform project notebook with idea spaces, collections, and rich metadata; local project files; long-established desktop lineage

The core model was checked against a mind-map-first product (MindNode) as a boundary probe, and against the paper-era analogs (corkboard, mood board, scrapbook, hand-drawn idea map) to avoid over-fitting to the current cloud-canvas generation.

## Sources

Research date: **2026-09-09**

- Milanote — product page (visual note-taking positioning): https://milanote.com/product/note-taking · guide index: https://milanote.com/guide · help center (content/organizing collections; nesting boards article): https://help.milanote.com/
- Heptabase — product page: https://heptabase.com/ · public wiki (Fundamental Elements): https://wiki.heptabase.com/
- Scapple (Literature & Latte) — product page: https://www.literatureandlatte.com/scapple
- Curio (Zengobi) — product page and edition comparison: https://zengobi.com/curio/
- MindNode — product page (boundary probe, positioning level only): https://www.mindnode.com/

> Sourcing limitation: evidence is drawn from official product pages, help centers, and public documentation wikis fetched on 2026-09-09. MindNode was characterized at positioning level only (support documentation not fetched), and no precise numeric limits, plan restrictions, or default settings are asserted anywhere in this document. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
