# Collaborative Presentation Editor

## Overview

A **Collaborative Presentation Editor** is a multi-user editing application whose unit of work is a shared, live presentation deck: an ordered sequence of slides, each slide a bounded canvas on which text, shapes, images, and media are freely arranged, composed for delivery to an audience.

Two structures define the type:

```text
Presentation grammar
└── Deck = ordered sequence of slides
    └── Slide = bounded canvas with freeform element placement
        └── composed as a sequential unit for delivery to an audience

Collaboration layer
└── Shared persistent deck (one live current version, no save-and-pass-around loop)
    └── Shared access beyond one author (invites / links, edit vs view)
        └── Concurrent multi-user editing merged into that single live version
```

The presentation grammar alone — a deck edited by one person and passed around as a file — is the older **Presentation Application**. The collaboration layer alone — a shared live canvas without ordered slides — drifts toward design platforms and whiteboards. This type exists where the two meet: several people building one deck together, seeing each other's changes as they happen, and then delivering that deck.

## Users & Context

The primary users are the small group of people responsible for one deck: a presenter preparing a pitch or briefing, teammates contributing their sections, a designer polishing layouts, a manager reviewing and approving. Typical occasions:

- a team deck assembled from contributions of several authors (sales pitch, project review, all-hands, course lecture)
- a deck one author drafts while others comment and correct in the same file
- a deck co-delivered by several presenters

Secondary concerns belong to the surrounding organization: workspace or drive administrators who control access, and template/brand owners who maintain the reusable slide furniture. The work environment is dominated by browser and desktop editors; mobile surfaces are typically used for reviewing, commenting, and sharing rather than heavy composition.

## Core Model

### The Defining Core

```text
Deck (shared, persistent, one live current version)
└── Slide (ordered position in the deck)
    └── Slide canvas (bounded, fixed-shape page)
        └── Elements (text, shapes, lines, images, video/audio, tables, charts)
```

Four properties. If any one is removed, the product is no longer recognizable as this type:

- **Shared persistent deck** — the deck lives in the product as one current version that is always there; nobody "owns the file" at a given moment, and there is no save/download/email-attachment loop between edits.
- **Ordered slides** — the deck is a sequence. Slide order is a first-class structure: slides can be added, duplicated, reordered, deleted, grouped, and skipped, and the order is what delivery follows.
- **Bounded slide canvas with freeform placement** — each slide is a fixed-shape page (typically widescreen) on which elements are placed, layered, sized, and aligned at will. This is what separates the slide from a document's continuous text flow and from a whiteboard's unbounded canvas.
- **Shared concurrent editing** — multiple invited participants edit the same live deck at once; changes appear for everyone without a merge step, and access is graduated (at minimum, some participants can edit while others can only view).

### Standard Capabilities

Mature products carry a common set of structures on top of this core. They are not what makes the product a collaborative presentation editor, but they make the daily work practical:

- **Theme / template layer** — a set of predesigned slide layouts, masters, and styles that slides inherit from; new slides start from layout placeholders rather than a blank page. Products differ in vocabulary (themes, templates, slide styles) but the structure is the same: reusable slide furniture held above the individual deck.
- **Element palette** — text boxes, shapes and lines, images, video and audio, tables, charts; with layering, grouping, alignment guides, and hyperlinks (to the web or to other slides in the same deck).
- **Speaker notes and presenter view** — per-slide notes visible to the presenter but not the audience; a presenter surface showing current and next slide, notes, and timing while the audience sees only the slide.
- **Delivery machinery** — full-screen slideshow mode, transitions between slides, object animations, automatic or click-driven advance, self-running options.
- **Comments** — slide-anchored discussion with replies and visible authorship, so review happens on the deck rather than beside it.
- **Sharing machinery** — invite collaborators by identity, share via link, distinguish who can edit from who can view, optionally admit guests or link-holders.
- **Live presence** — collaborators' names (and often cursors or selections) visible while editing; the ability to follow what another collaborator is looking at.
- **Version safety** — restore earlier versions of the deck, recover deleted slides, and resolve conflicts when concurrent edits collide.
- **Interchange** — import and export of the industry-standard presentation file format, PDF export for distribution, and embedding or publishing of a live deck into other pages.
- **Organization and search** — decks held in folders, drives, or workspace structures, with search and notifications across them.
- **AI assistance** — deck generation and drafting from a prompt or outline, AI image handling; increasingly common across current products.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Shared persistent deck
Implementations:  file in a cloud drive (edited live) · deck inside a team workspace · deck in a device-platform cloud

Concept:   Shared access
Implementations:  per-person invites with edit/view roles · link sharing with role settings · workspace membership + guests

Concept:   Theme layer
Implementations:  themes with master layouts · template galleries · reusable slide styles

Concept:   Delivery
Implementations:  local slideshow · presenter view on a second screen · web-based player · co-presented player with control handoff
```

A reader who has only seen one implementation (say, a drive-file product) should still be able to recognize a workspace-native product from the core model.

## How It Works

### Create the deck

```text
Start a deck
→ from a blank canvas, a template/theme, an outline (often AI-drafted), or an imported presentation file
→ deck exists immediately in the product's storage; no "save" step
```

### Compose slides

```text
Add slides from layouts
→ place and arrange elements on each slide canvas
→ text, shapes, images, tables, charts, media
→ reorder, duplicate, group, or skip slides as the argument takes shape
```

Composition is spatial, not linear: the author places a text box here, an image there, and alignment guides keep the arrangement tidy. The deck's argument is carried by slide order.

### Share and co-edit

```text
Invite collaborators (by identity or link) with edit or view access
→ everyone works in the same live deck
→ changes appear for all participants as they are made
→ presence shows who is in the deck; comments anchor review to slides
```

This is the step that defines the type. There is no round of "final_v3_FINAL.pptx" — the single live deck absorbs everyone's work, and version history stands behind it if something must be rolled back.

### Review

```text
Reviewers open the deck (edit or view role)
→ leave comments on slides, reply, resolve
→ authors act on comments in the same deck
→ some products add slide-level work tracking (status, assignees)
```

### Deliver

```text
Open present mode
→ audience sees slides full-screen, in order
→ presenter sees notes, next slide, and timing in a private presenter view
→ advance manually or automatically; transitions and animations play
→ variants: present over the web to remote viewers, hand presentation
   control between multiple presenters, or export to PDF / video for
   asynchronous delivery
```

### Manage the estate

```text
Decks accumulate in folders / workspaces
→ search, notifications, duplicate-as-template
→ restore earlier versions, recover deleted slides
→ export, embed, or archive finished decks
```

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Deck home / dashboard

The entry surface listing the user's decks.

- recent decks, folders or workspace structure, shared-with-me, search
- primary actions: open a deck, create a deck (blank / template / import / AI), organize into folders

### Slide navigator

The deck-level view of slide order.

- thumbnail strip or grid of slides in sequence, sections or groups, slide numbers
- primary actions: add, duplicate, reorder, delete, group, skip slides

### Slide canvas editor

The main composition surface.

- the current slide at full size, element palette, alignment guides, layers, format controls for the selected element, theme/layout picker
- presence indicators of other collaborators editing the same deck
- primary actions: insert and arrange elements, format them, apply layouts, add speaker notes

### Present / player mode

The delivery surface.

- full-screen slide, advance controls, transitions and animations
- primary actions: start, advance, exit; in web-player variants, share a link that lets remote viewers watch

### Presenter view

The presenter's private companion surface.

- current and next slide, speaker notes, elapsed time, navigation controls — while the audience sees only the slide

### Comments

The review surface, anchored to slides.

- comment threads with authors and replies, resolve state
- primary actions: comment, reply, resolve; in some products, set a slide's status or assignee

### Sharing dialog

The access-control surface for the deck.

- current collaborators and their roles, invite field, link with role setting
- primary actions: invite, change someone's role, stop sharing

### Version history

The safety surface.

- list of earlier versions or changes, preview, restore
- primary actions: preview an earlier version, restore it

## Important Rules / Behaviors

### One live version absorbs all edits

The defining behavior: there is no per-editor copy to reconcile. Concurrent edits land in the same deck. When the same region is edited simultaneously, products either merge the changes or surface a conflict to resolve — conflict handling is part of the live-deck reality, not an error state.

### Access is graduated and enforced

At minimum, edit vs view. View-only participants can watch, comment (in most products), and present nothing back; edit participants change the shared deck for everyone. Who may reshare, and whether link-holders or guests may enter, is governed by the sharing settings.

### Slide order is content

Reordering slides changes the delivered argument. Skip-slide behavior (a slide retained in the deck but excluded from delivery) exists in several products precisely because order and inclusion are meaningful decisions.

### The theme layer propagates

Slides inherit appearance from the deck's theme, template, or master layouts. Changing the theme layer restyles the deck; overriding on one slide is possible but is a deliberate act. This is what keeps a multi-author deck visually coherent.

### Delivery is a projection of the deck, not a copy

Present mode renders the current live deck. What the audience sees follows the deck as it stands — which is why last-minute edits by a co-author can reach the screen, and why presenter view exists to keep notes and navigation private.

### Notes are presenter-private

Speaker notes belong to the presenter surface; they are part of the deck but not part of what the audience sees (unless explicitly printed or shared).

## Variants

- **Suite file variant** — the deck is a file in a cloud drive inside an office suite (documents, spreadsheets, presentations alongside each other); collaboration rides on the suite's sharing layer.
- **Workspace-native variant** — decks live inside a dedicated workspace with team-scoped areas, folders, guests, and collaboration extras (slide status, co-presenting, analytics); common in sales-oriented standalone products.
- **Platform-native variant** — the editor is a device-platform application whose collaboration rides on the platform's cloud account and shared folders.
- **Template-first variant** — presentations as one artifact inside a broader template-driven design platform; the deck grammar is present but the product's center of gravity is visual design.
- **Governance-heavy variant** — office-suite lineage adds formal review machinery (tracked changes, document inspection, digital signatures) for regulated environments.
- **Delivery-extended variant** — web-based players, co-presenter control handoff, live audience features, deck analytics, and recorded video decks extend the delivery step for remote and asynchronous audiences.

A variant remains a variant while the defining core holds. When the artifact stops being an ordered deck for delivery — an unbounded canvas, a linear document, a design file without slide sequence — it has become a different Application Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Presentation Application | same deck grammar, but single-author files with a save-and-pass-around loop; no shared live layer |
| Collaborative Document Editor | same collaboration skeleton (shared live artifact, shared access, concurrent merge), but the grammar is continuous linear text flow, not ordered bounded slides |
| Collaborative Design Platform | shared live design files, but subject-agnostic visual production (frames, boards, prototyping, handoff) rather than an ordered deck for sequential delivery |
| Digital Whiteboard | shared live canvas, but unbounded and exploratory; slide order and delivery are not the organizing principle |
| Collaborative Spreadsheet | same collaboration skeleton, but the grammar is cells, rows, and formulas; decks may consume spreadsheet charts but do not compute |
| Webinar / Virtual Meeting Platform | delivers live meetings to audiences; the deck here is the edited artifact, and present features are delivery aids, not meeting infrastructure |
| Video Editor | sequences frames on a timeline for rendered output; a deck is delivered live, slide by slide, not rendered |

The two most important boundaries: against the **Presentation Application** (the collaboration layer is the discriminator — a pre-cloud single-author presentation product is the parent type, not a member) and against the **Collaborative Document Editor** (the grammar is the discriminator — the two types share the collaboration skeleton but differ in what the artifact is).

## Representative Products

- Microsoft PowerPoint (Microsoft 365 / web)
- Google Slides
- Pitch
- Keynote (with iCloud collaboration)
- Canva Presentations

The defining core was checked against the platform-native sample (Keynote for iCloud) and the workspace-native sample (Pitch) to avoid over-fitting to any one container philosophy; the office-suite incumbent (PowerPoint) anchors the file-based variant.

## Sources

Research date: **2026-09-06**

- Microsoft Support — PowerPoint help & learning: https://support.microsoft.com/en-us/powerpoint
- Microsoft Support — Collaborate and share (PowerPoint): https://support.microsoft.com/en-us/powerpoint/collaborate-and-share
- Microsoft Support — Slides and text (PowerPoint): https://support.microsoft.com/en-us/powerpoint/slides-and-text
- Microsoft Support — Print and present (PowerPoint): https://support.microsoft.com/en-us/powerpoint/print-and-present
- Pitch Help Center: https://help.pitch.com/ (incl. "Getting started with Pitch", "Present your ideas with your teammates", collections "Get started with Pitch" and "Become a Pitch power user")
- Apple — Keynote User Guide for iCloud: https://support.apple.com/guide/keynote-icloud/welcome/icloud
- Apple — Keynote Support: https://www.apple.com/keynote/

> Sourcing limitation: official help-center articles for Google Slides and Canva could not be fetched from the research environment (timeouts; browser-gated pages), and deep Microsoft help articles were unreachable (category pages only). Claims for those products are therefore limited to their standing as market anchors; no operational details are asserted for them. Precise numeric limits, defaults, and plan-gated features are intentionally not stated anywhere in this document; product-by-product observations are recorded in the paired Research Notes.
