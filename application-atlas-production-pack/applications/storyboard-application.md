# Storyboard Application

## Overview

A **Storyboard Application** is the tool for making *boards* — the framed, captioned, ordered picture sequences that plan a visual story before it is produced. Its unit of record is the **panel**: a framed image paired with a caption. Panels are arranged in story order under a scene-level organizing layer, and the finished board leaves the application as a shareable artifact — presented, printed, or exported — for clients, crews, studios, or classrooms to read, comment on, and approve before production begins.

The defining structure is small:

```text
Panel (framed image + caption)
└── Ordered narrative sequence (panels grouped into scenes / story order)
    └── The board as a reviewable, distributable artifact
```

Everything else commonly associated with storyboarding software — animatic playback, script import, per-panel camera notes, asset libraries, AI image generation, client approval workflows — is widespread in current products but is not what makes the product a storyboard application. The paper boards pinned on a studio wall satisfy the same structure without any of it.

When the center of the product shifts from the captioned board to a staged scene in space — sets, camera setups, blocked coverage — the product is drifting toward the neighboring Previsualization Application.

## Users & Context

The primary users are the people who must show a story visually before it is made:

- **storyboard artists** — draw or assemble the panels; the board is their craft deliverable
- **directors and agency creatives** — sketch shot ideas, arrange the story, and pitch the board
- **producers and account teams** — put the board in front of clients for feedback and sign-off
- **writers** — visualize a script or story idea without making a movie
- **educators and students** — use the same panel-grid form to plan and retell stories in class

The characteristic moment of use is the pre-production review loop: a board is drafted, shared, commented on frame by frame, revised, re-versioned, and finally approved — because revising a board is cheap while reshooting is not. Boards also travel to the shoot itself as the crew's visual shorthand.

## Core Model

### The Defining Core

```text
Panel (framed image + caption)
└── Ordered narrative sequence (panels grouped into scenes / story order)
    └── The board as a reviewable, distributable artifact
```

Three properties. If any one is removed, the product is no longer recognizable as a storyboard application:

- **The panel as the unit of record** — a framed image plus its caption. The image may be drawn in the product, composed from artwork, uploaded or scanned, photographed from paper, or generated; the caption carries what the picture alone cannot — action notes, dialogue, shot or camera notes (the exact fields vary by product). Remove the image and only a script remains; remove the caption and only a picture strip remains; either fragment stops being a storyboard cell.
- **Ordered narrative sequence organized above the panel** — panels sit in story order, grouped by an organizing layer: scenes and sequences, script scenes, template grids, or shoot-day groups. The board reads as the story played out frame by frame. Without the ordering and grouping, the product is an image gallery.
- **The board as a reviewable, distributable artifact** — the sequence is made to leave the application: presented in a review view, shared by link, printed, or exported as PDF, images, or movie. Boards exist to be read and approved by people outside the tool. Without this, the product is a private sketchbook; without the panels, a slide deck.

The three properties form one loop: make panels → arrange the story → show the board for review before production.

### Standard Capabilities of Mature Products

These are common in current products and make the board practical, but they do not define the Type:

- **Animatic playback** — timing the board into a rough moving preview, commonly with sound, so pacing can be judged before an editor is ever opened. Depth varies widely: some products offer a one-click timed playback of the board; professional craft tools add a full timeline with camera moves, sound editing, and edit-ready export; some products have no playback at all.
- **Script integration** — the screenplay as the board's skeleton: script scenes organizing the panels, script text shown alongside frames, or a highlighted line of action or dialogue generating a matching panel.
- **Shot and camera notes** — per-panel fields for shot type, framing, aspect ratio, and camera movement. These are recorded as data about the panel, not as a staged camera view.
- **Asset sources and image workflow** — art and stock libraries, upload and scan, external paint-editor round-trips (edit a panel in a full drawing application and it updates back in the board), reuse libraries, and printing paper worksheets to draw on by hand and photograph back in.
- **Sharing, review, and approval** — view links, frame-level comments, approval statuses, version history that keeps comments intact, real-time collaboration, and task assignment. The intensity ranges from a full client-approval workflow to simply exporting files.
- **Templates** — board layouts, aspect-ratio and column presets, and ready-made storyboard templates.
- **PDF and print** — the canonical artifact format: contact sheets, styled PDFs with headers and watermarks, printable worksheets.

### One Structure, Many Implementations

The core model is conceptual. Products realize each part differently:

```text
Concept:            Panel image
Implementations:    drawn in-product · composed from an art library · uploaded/scanned ·
                    photographed from paper · AI-generated (as a draft or a reference to draw over)

Concept:            Organizing layer
Implementations:    scenes & sequences · script scenes · template grids · location/shoot-day groups

Concept:            The board artifact
Implementations:    presentation link · PDF / printed sheets · image exports ·
                    animatic movie · NLE interchange files
```

A reader who has only seen one implementation — say, a web tool where panels are assembled from stock images — should still recognize a hand-drawn desktop board, or a classroom grid of illustrated cells, as the same application.

## How It Works

### Start the board

```text
Create a project
→ start from a blank board, a template, or a script
→ if a script: import it and let its scenes organize the panels (or write the script in-product)
```

### Make the panels

```text
Add a panel
→ produce its image (draw · compose from library · upload/scan · photograph paper · generate)
→ write its caption (action, dialogue, shot notes)
→ duplicate, copy, paste, rearrange — reordering is constant
```

Panel production is deliberately low-friction: rough sketches are expected, and many products treat a generated or referenced image as something to be drawn over rather than a finished frame.

### Arrange the story

```text
Group panels into scenes (or let script scenes do it)
→ reorder panels and scenes as the story changes
→ keep shot numbering, aspect ratios, and layouts consistent across the board
```

### Review and approve

```text
Share the board (link, presentation, print, PDF)
→ readers comment frame by frame
→ revise; create a new version with comments intact
→ repeat until the board is approved
```

This loop is the reason the application exists: the board is the artifact that gets a story approved before production money is spent.

### Time the board (optional extension)

```text
Give panels durations (or record timing live)
→ add sound/dialogue where supported
→ play the board as a rough animatic
→ export the animatic movie, or an edit-ready sequence for the editing application
```

### Hand off to production

```text
Export the approved board (PDF / images / shot lists / animatic / NLE files)
→ the board travels to the shoot as the crew's visual shorthand
→ the animatic or sequence travels to the edit
```

### Core vs Common vs Optional

**Defining core** — without these, not a storyboard application:

- panel as framed image + caption
- ordered narrative sequence with a scene-level organizing layer
- the board as a reviewable, distributable artifact

**Standard capabilities** — present in most mature products:

- animatic playback (in varying depth; absent in some)
- script integration
- per-panel shot/camera notes
- asset sources and image workflow (libraries, external editors, paper import)
- sharing/review/approval machinery
- templates
- PDF/print export

**Optional / variant** — depends on audience, era, and product philosophy:

- drawing tools in-product (some products assemble panels entirely from libraries)
- AI image generation and consistent characters
- camera-move timelines, sound editing, and NLE round-trip conformance
- client approval workflows, classroom assignment flows
- 3D model import and multiplane staging aids

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Board view (panel strip / grid)

The primary surface: the ordered panels with their captions, usually grouped by scene.

- shows story order, scene grouping, shot numbering, approval status where supported
- primary actions: add/duplicate/reorder panels, edit captions, group into scenes

### Panel editor

Where a single panel's image and caption are produced.

- drawing tools or asset pickers (or both), reference layers, onion skin, guides
- caption fields: action, dialogue, shot type, timing
- primary actions: draw/compose/upload/generate the image, write the caption, edit in an external paint application

### Scene / sequence organizer

The layer above panels.

- scene list or script view; drag-to-reorder scenes and panels
- primary actions: create/reorder scenes, move panels between scenes, rename

### Script view

Where a screenplay or AV script lives alongside the board.

- script text side-by-side with frames; scene-to-board linkage
- primary actions: import script, tag a script line to create a panel, edit script text

### Animatic timeline (where present)

The timing surface over the board.

- panel durations, sound tracks, camera-move keyframes in deeper products
- primary actions: set timing, add sound, play, export the animatic

### Share / present view

The board as its readers see it.

- presentation layout, frame-by-frame commenting, approval statuses, version history
- primary actions: share a link, comment, set status, create/restore versions

### Export settings

- PDF/print layouts (headers, columns, watermarks), image exports, movie/animatic exports, NLE interchange

## Important Rules / Behaviors

### Panel order is story order

The sequence of panels *is* the narrative. Reordering panels and scenes is the primary revision act, and mature products make it cheap — renumbering, regrouping, and re-flowing captions automatically as frames move.

### Captions travel with panels

A panel's caption (action, dialogue, shot notes) belongs to the panel and follows it through reordering, duplication, and export. In some professional products, panel captions even become metadata on the sequence delivered to the editing application.

### Versions keep the review record

In review-centered products, creating a new version preserves the comments and approval history of the old one — the board's paper trail ("which version did the client approve?") is part of the artifact.

### The animatic is derived from the board

Playback timing comes from the panels' durations; the animatic is a preview of the board, not an independent work. Editing the board changes the animatic; the reverse does not hold.

### Boards are planning artifacts, never the finished work

The board's images are deliberately rough or symbolic. The application finishes nothing: its outputs are documents for other people — the crew on set, the editor in the cutting room, the client signing off.

### Rough fidelity is a feature

Stick figures, library stand-ins, and generated reference images are all legitimate panel content; the board's job is to communicate the story and the shot intent, not to look finished.

## Variants

- **craft-drawn production boards** — desktop tools with full drawing engines for professional board artists; deep animatic timelines and edit-interchange for studio pipelines
- **web review boards** — SaaS tools where the board is a client-facing document: scripts, shot lists, comments, approvals, and versions around a no-drawing board
- **free / open-source solo tools** — minimal drawing organizers for writers, directors, and indie teams, often bridging paper worksheets and external paint applications
- **suite-embedded storyboards** — the board as one module of a pre-production platform, linked to screenplays, breakdowns, shot lists, schedules, and call sheets
- **education and communication boards** — the same panel-grid form used in classrooms and businesses for storytelling, planning, and explanation, composed from art libraries with no production loop

A variant remains a variant as long as the defining core — captioned panels in ordered scenes, shipped as a reviewable board — still applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Previsualization Application | the closest neighbor; shares panels, scenes, and the animatic. The seam is the center of gravity: the storyboard centers on the captioned board as a narrative/review document and has no staging space; previsualization centers on the blocked scene in space (sets, camera setups, coverage) with playback as the evaluation act. The animatic is the shared overlap zone |
| 2D Animation Application | animation authors a frame-by-frame performance and delivers a finished moving work; the storyboard holds static planning panels and delivers a review artifact |
| Script Breakdown Application | breakdown inventories production elements per scene (cast, props, wardrobe); the storyboard pictures the shots. Complementary script-driven deliverables, sometimes bundled in one platform |
| Production Scheduling / Call Sheet Application | the schedule and call sheets organize the shoot and consume boards as reference; they do not author panels |
| Film Production Management | the production office's system of record (schedule, budget, logistics); the storyboard is the creative planning surface feeding it |
| UX Prototyping Application | both previsualize before building; the prototype simulates an interactive interface, the board pictures filmed or animated scenes |
| General design / template platforms | a layout tool can assemble framed images, but lacks panel/scene/shot semantics, script linkage, and the production review loop |
| Shot-list-only tools | an ordered shot list without panels sits below this Type; in mature products the shot list is a companion or derived artifact of the board |

## Representative Products

- Toon Boom Storyboard Pro — professional craft standard; drawn panels with a deep animatic timeline
- Boords — web SaaS; boards as client-review documents with approvals and versions
- Storyboarder (Wonder Unit) — free open-source drawing organizer with paper and Photoshop round-trips
- Storyboard That — education/communication pole; library-composed boards
- StudioBinder — storyboard module inside a pre-production platform

The defining core was checked against the analog paper-board tradition (framed captioned panels, pinned in scene order, presented for approval) to avoid defining the Type by any current implementation pattern.

## Sources

Research date: **2026-09-10**

- Toon Boom — Storyboard Pro product page: https://www.toonboom.com/products/storyboard-pro
- Toon Boom — Storyboard Pro Knowledge Base: https://helpcentre.toonboom.com/hc/en-ca/categories/39971055086995
- Boords — homepage and storyboard-software feature page: https://boords.com/ , https://boords.com/storyboard-software
- Wonder Unit — Storyboarder product page: https://wonderunit.com/storyboarder/
- Storyboard That — homepage and creator description: https://www.storyboardthat.com/
- StudioBinder — storyboard software feature page: https://www.studiobinder.com/storyboard-software/
- Toon Boom deep help-centre articles (panels/scenes/sequences, animatic, camera, conformation) were first fetched on 2026-09-08 during the paired previsualization research and are cited from that record.

> Sourcing limitation: evidence for all five products comes from official product and feature pages; in-app help-center depth was not fetched for Boords, Storyboard That, or StudioBinder. Whether StudioBinder offers animatic playback was not evidenced and is not claimed either way. Precise operational limits (frame counts, plan caps, format lists) are intentionally not stated. Detailed observations, the cross-product comparison matrix, and the boundary adjudication are recorded in the paired Research Notes.
