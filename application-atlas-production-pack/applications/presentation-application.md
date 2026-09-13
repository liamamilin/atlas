# Presentation Application

## Overview

A **Presentation Application** is an authoring application whose unit of work is a presentation deck: one self-contained document the author creates, keeps, revisits, and delivers, composed as an ordered sequence of slides — each slide a bounded, fixed-shape canvas on which text, shapes, images, media, tables, and charts are freely arranged — for delivery to an audience.

The defining structure is small:

```text
Deck (one authored presentation artifact — created, kept, handed off as a whole)
└── Slides (ordered sequence; the order is the delivery order)
    └── Slide canvas (bounded, fixed-shape page)
        └── Elements (text, shapes, images, media, tables, charts — placed freely)
            └── composed as a sequential unit for delivery to an audience
```

Everything commonly associated with modern presentation software — designer themes and template galleries, transitions and animations, speaker notes and presenter views, cloud storage, sharing and live co-editing, AI drafting — is widespread in current products but is not part of the defining core. File-based desktop products, platform-native applications, and open-source office modules all fit this definition without any of those specifics.

When the shared live deck with concurrent multi-user editing becomes the product's primary object rather than an added layer, the product is the neighboring **Collaborative Presentation Editor**. The grammar is the same on both sides; what changes is whether the deck is an authored document or a shared live object.

## Users & Context

The primary user is a single author who needs to stand in front of an audience — physically or remotely — and show a prepared sequence of visuals while speaking: a professional briefing a team or client, an educator teaching a class, a student presenting coursework, a founder pitching, a researcher reporting results.

Typical occasions:

- prepare a talk or lecture for a specific audience and date
- build a business deck — proposal, review, all-hands, training session
- assemble a one-off deck under deadline, reusing earlier slides or a template
- produce supporting visuals whose delivery is controlled by the presenter, slide by slide

Secondary roles appear in organizational settings: a designer who prepares the reusable theme, a colleague who reviews a draft and comments before the talk. The dominant work surface is a desktop editor; web and mobile surfaces are commonly used for reviewing, light edits, and presenting.

## Core Model

### The Defining Core

```text
Deck (authored presentation artifact)
└── Slide (ordered position in the deck)
    └── Slide canvas (bounded, fixed-shape page)
        └── Elements (text, shapes, images, video/audio, tables, charts)
```

Four properties. If any one is removed, the product is no longer recognizable as this type:

- **An authored deck artifact** — the presentation exists as one persistent, self-contained document the author creates, names, keeps, and hands off; content and design travel together as a whole. It may live as a local file, a device-stored document, or a cloud-stored document — the substrate varies, but the deck is one authored work, not a transient session surface. Without this, the product is a live-only canvas.
- **Ordered slides** — the deck is a sequence. Slide order is a first-class structure: slides can be added, duplicated, reordered, deleted, and (in many products) grouped or temporarily skipped, and delivery follows the order. Without the sequence, the artifact is a stack of pages or a poster, not a presentation.
- **Bounded slide canvas with freeform placement** — each slide is a page of fixed shape on which elements are placed, layered, sized, and aligned at will. Composition is spatial, not a continuous text flow (that is the document editor), and bounded, not an endless canvas (that is the whiteboard).
- **Audience delivery as the composing purpose** — the deck is composed to be shown to an audience, one slide at a time. The standard realization is the product's own full-screen playback, advanced by the presenter or timed; export to PDF, print, published pages, and recorded narrated video are alternative realizations of the same purpose. Without delivery, it is graphic composition with nowhere to go.

### Standard Capabilities

Mature products carry a common set of structures on top of this core. They are not what makes the product a presentation application, but they make the daily work practical:

- **Theme and template layer** — a set of predesigned themes with coordinated fonts and colors, slide layouts, and placeholders. New slides start from a layout; replacing placeholder text and images does the first draft's work; the theme can be changed under an existing deck. Products differ in vocabulary (themes, templates, masters, slide styles) but the structure is the same: reusable slide furniture held above the individual deck.
- **Element palette** — text boxes, shapes and lines, images and image galleries, video and audio, tables, and charts as the common core; icons, 3D objects, diagrams, equations, and live video as common extensions. Composition aids: layering, grouping, locking, alignment guides, rulers, and object lists.
- **Slide organization machinery** — a slide navigator or thumbnail pane and an overview view (slide sorter) for reordering; duplicate and delete; grouping and sections; slide numbers; slide size and background as deck-level properties.
- **Speaker notes and presenter support** — per-slide notes kept out of the audience's view; a presenter surface showing the current and next slide with notes while the audience sees only the slide; rehearsal with timing; remote control; a laser-pointer mode.
- **Delivery machinery** — full-screen slideshow mode; transitions between slides; object animations (builds) with ordering; automatic advance; self-running options for unattended display.
- **File machinery** — save and name (with autosave in cloud-backed products), version restore, file-size reduction, password protection, transfer between devices.
- **Interchange and alternative outputs** — the dominant presentation file format as the industry exchange standard (products import, modify, and export it); PDF export; printing of slides, handouts, and notes; publishing to HTML or the web; export of animated sequences or recorded narrated video.
- **Review furniture** — comments with visible authorship so a draft can be corrected before the talk; tracked-changes markup as an office-suite lineage extra.
- **Sharing and co-editing as a modern layer** — inviting others to a deck with edit or view roles, live co-authoring, comments. Common in current products, layered on the authored deck rather than replacing it.
- **AI assistance** — drafting a deck from a prompt or outline and generating slides; increasingly common, sometimes subscription-gated.

### One Structure, Many Implementations

The core model is written in conceptual terms; products realize it differently:

```text
Concept:   Authored deck artifact
Implementations:  local file · device-platform cloud document · suite cloud document

Concept:   Theme layer
Implementations:  themes with master layouts · template galleries · reusable slide styles

Concept:   Delivery
Implementations:  in-product slideshow on one display · presenter view on a second screen ·
                  video-conference presenting · recorded movie · kiosk/self-running · print/PDF/HTML

Concept:   Interchange
Implementations:  presentation-format import/export · PDF · print handouts · web publish
```

A reader who has only seen one implementation — say, a cloud-suite deck — should still recognize a file-based desktop product or an open-source module from the core model.

## How It Works

### Start the deck

```text
Create a new presentation
→ from a blank deck, a theme or template, an outline (often AI-drafted), or an imported file
→ the deck exists as a document that is then named and kept
```

### Compose the slides

```text
Add slides, each starting from a layout
→ replace placeholder text and images or place elements freely on the slide canvas
→ text, shapes, images, tables, charts, media — positioned, layered, aligned
→ reorder, duplicate, group, or skip slides as the argument takes shape
```

Composition is spatial, not linear: the author puts a heading here, a chart there, and alignment guides keep the arrangement tidy. The deck's argument is carried by slide order.

### Refine the delivery

```text
Add speaker notes for what will be said, not shown
→ apply transitions and object animations where they help
→ rehearse with timing; adjust pacing or advance behavior
```

### Keep and hand off

```text
Name and save the deck (locally or in cloud storage)
→ optional: version restore point, password protection, file-size reduction
→ optional: send, transfer between devices, or share for review with edit/view roles
```

### Deliver to the audience

```text
Start the slideshow (full-screen, from the beginning or the current slide)
→ advance slide by slide — presenter-paced (keys, click, remote) or timed (auto-advance)
→ presenter surfaces show notes and upcoming slides privately
→ end the show; the deck remains as the kept document
```

For audiences that will not see a live presenter, the same deck is realized differently: exported to PDF or print handouts, published as a page, or recorded as a narrated video. The composing intent — sequential delivery to an audience — is the constant; the realization varies.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### New-deck surface (theme chooser)

The entry surface.

- theme and template categories with previews; blank option
- primary actions: pick a theme, open an existing deck, import a file

### Slide editor (the working view)

The main surface where composition happens.

- slide canvas at the center; slide navigator/thumbnails at the side; element inserters and format inspectors around them
- primary actions: add/reorder/delete slides, apply layouts, insert and arrange elements, format text and objects, add notes

### Overview views

Whole-deck views for structure work.

- thumbnail grid or sorter showing every slide in order; sometimes a handout view
- primary actions: reorder, group/section, skip, duplicate

### Presenter surfaces

What the presenter sees and uses during delivery.

- full-screen audience display; private presenter view with current slide, next slide, notes, and timing
- primary actions: advance/back, blank the screen, point, end the show

### Print / export surfaces

The deck's exits into other media.

- output selection: slides, handouts with notes, notes pages, PDF, other presentation formats, video/animated export where offered
- primary actions: choose range and layout, export or print

## Important Rules / Behaviors

### Slide order is the delivery order

Playback follows the deck's sequence. Products give the author ways to vary what a given showing includes — skipping slides that stay in the deck, or defining a custom show sequence — without reordering the document itself.

### The theme sits above the slides

Slides inherit their look from the theme and start from its layouts. Changing the theme or a layout re-skins existing slides; the author's content and positions stay. This inheritance is why reusable templates work.

### Notes are presenter-side

Speaker notes belong to the presenter's surfaces. They are printed on notes pages when asked for, but the audience display shows only the slide.

### The canvas is fixed; elements are positioned

The slide is a page of fixed shape; changing the deck's slide size is a deliberate, deck-level operation. Elements keep their placed positions — the deck does not reflow the way a document's text does, which is why decks are checked visually rather than proofread as flow.

### Playback is sequential and controlled

Advance is presenter-paced or timed. Products add guardrails for unattended display (self-running shows, and in some products a password required to exit).

### The deck travels as a whole

A deck can be moved, sent, exported, and opened elsewhere as one unit. Interchange with other presentation products is an industry expectation — the industry-standard presentation format serves as the exchange medium — but fidelity across products is best-effort: complex effects and layout may not survive a round trip exactly.

### Review furniture stays editing-side

Comments and tracked changes belong to the authoring context; they are not part of what the audience sees during delivery.

## Variants

Common realizations of the type:

- **office-suite presentation module** — one member of a document/spreadsheet/presentation suite, file-based or cloud-backed (e.g. PowerPoint, Impress)
- **platform-native application** — bound to a device platform's document and storage model, with the authored file loop as the primary documented flow (e.g. Keynote)
- **web-first cloud-suite editor** — browser surface with sharing and live co-editing as everyday practice; the grammar core unchanged (e.g. Google Slides)
- **collaborative-first standalone** — the shared live deck as the product's center (the neighboring Collaborative Presentation Editor, e.g. Pitch)
- **design-platform module** — presentations as one artifact kind inside a broader design tool (e.g. Canva)
- **delivery specialization** — kiosk/self-running shows, recorded narrated videos, video-conference presenting, printed handouts as the dominant output

A variant remains a variant while the defining core holds. When the shared live merged deck becomes the primary object, the product belongs to the Collaborative Presentation Editor type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Collaborative Presentation Editor | same slide grammar, but the shared live merged deck with concurrent editing is the defining object; here the authored deck is the unit of work and collaboration is a layered capability |
| Document Editor | authored prose flowing across pages for reading; not ordered slides for delivery; different grammar on the same authored-artifact skeleton |
| Collaborative Document Editor | shared live text document; grammar difference separates it where collaboration exists on both sides |
| Desktop Publishing / Page Layout | fixed pages composed for print reproduction; the deck is composed for sequential on-screen delivery — printing handouts is an output, not the center |
| Digital Whiteboard | unbounded persistent spatial board for free exploration; not bounded ordered slides with a delivery sequence |
| Diagramming Application | shapes with connector and notation semantics as the organizing structure; slides contain shapes but without connector semantics |
| Graphic Design Application / Template-based Design Platform | design deliverables (posters, assets) as the output; presentations as one artifact kind inside such products is a straddle, not the center |
| eLearning Authoring Tool | produces learner-driven interactive content (questions, branching) handed to a delivery system; the deck is presenter-driven sequential delivery |
| Video Editor | timeline editing of footage; a recorded narrated deck is an output of the deck, not timeline editing |

The boundary with the Collaborative Presentation Editor is the important one, because the two types share their grammar. The structural difference is whether the deck is an authored document that the author keeps and delivers — with collaboration available as an added layer — or a shared live object whose concurrent multi-user editing is the defining requirement.

## Representative Products

- Microsoft PowerPoint
- Apple Keynote
- LibreOffice Impress

The core model was checked across three product philosophies — office-suite incumbent (including still-current perpetual desktop editions), platform-native file-first application, and open-source file-based module — with Google Slides and Canva Presentations used as boundary anchors for the collaborative-first and design-platform realizations.

## Sources

Research date: **2026-09-08**

- Apple — Keynote User Guide for Mac: https://support.apple.com/guide/keynote/welcome/mac ; Create a presentation in Keynote on Mac: https://support.apple.com/guide/keynote/create-a-presentation-tan317e80e8c/15.3/mac/1.0
- Microsoft — PowerPoint help & learning hub: https://support.microsoft.com/en-us/powerpoint ; Create a presentation in PowerPoint: https://support.microsoft.com/en-us/powerpoint/training/create-a-presentation-in-powerpoint ; Print and present: https://support.microsoft.com/en-us/powerpoint/print-and-present
- LibreOffice — Impress Help: https://help.libreoffice.org/latest/en-US/text/simpress/main0000.html ; Impress Features: https://help.libreoffice.org/latest/en-US/text/simpress/main0503.html ; Instructions for Using LibreOffice Impress: https://help.libreoffice.org/latest/en-US/text/simpress/guide/main.html

Supporting category-taxonomy evidence for PowerPoint (collaborate-and-share, slides-and-text) and collaborative-pole evidence (Pitch, Keynote for iCloud) is documented in the paired Research Notes and the sibling type's Research Notes (fetched 2026-09-06).

> Sourcing limitations: Google Slides and Canva help surfaces could not be fetched (network failures in this and the sibling research pass), so they are used only as boundary anchors with no operational claims. External historical references were unreachable, so the continuity of the type across older file-based generations is reasoned from the products' own documented lineage rather than from historical sources. No numeric limits (slide counts, file sizes, dimensions, durations) are stated anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
