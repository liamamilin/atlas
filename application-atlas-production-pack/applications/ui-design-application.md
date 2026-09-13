# UI Design Application

## Overview

A **UI Design Application** is an editor for designing the user interfaces of digital products — app screens, web pages, and the reusable components they are built from. Its world is organized around one authoritative artifact: the interface design file, whose unit of design is the **screen frame** — a bounded, individually addressable container representing one screen (or screen region) of an app or website, filled with editable, layered design objects, and destined to be implemented in code by someone else.

The defining core is small:

```text
Screen frame (the unit of design)
└── Editable layered UI composition inside the frame
    └── Design-of-record posture: the screens are a specification
        for an interface built elsewhere, not the interface itself
```

Everything else commonly associated with modern UI design tools — reusable components, auto-layout, design tokens, shared libraries, embedded prototyping, developer handoff surfaces, real-time collaboration, AI assist — is standard equipment in current products but is not what makes the product a UI design application. Older, native, single-user, and intentionally low-fidelity products fit the same definition without any of those specifics.

When the artifact stops being a design and becomes the working interface (deployed site, running app), the product has left this Type; when the artifact's center of gravity shifts from how screens look to how screens behave, it is drifting toward the prototyping Types.

## Users & Context

The primary user is a **product or UI designer** composing and refining the screens of a digital product — a mobile app, a website, a dashboard, an internal tool. Designers work screen by screen, assemble screens from reusable parts, keep visual language consistent across a product, and prepare the result for implementation.

Secondary participants surround the same artifact:

- **Developers**, who consume the design: they inspect measurements, styles, and assets, and build the real interface in code from what the design specifies.
- **Product managers, founders, business analysts, and other non-designer stakeholders**, who review screens, comment, and approve what should be built — some products are built primarily for this audience rather than for professional designers.
- **Design-system maintainers**, who curate the shared component and style libraries other designers draw from.

The work context is product development: designs are typically reviewed by teams, iterated through feedback, and handed off to engineering. Some products serve the early, rough phase of this loop (deciding what to build); others serve the polished phase (specifying exactly what was decided).

## Core Model

### The Defining Core

**1. The screen frame — the unit of design.**
The design file is organized around bounded containers, each representing one screen or screen-sized region of the product's interface: a mobile screen, a web page, a dialog, a card, a button. Products name these *frames*, *artboards*, or *boards*; the structure is the same. Frames carry a defined size (commonly chosen from device or platform presets), can nest (a component frame inside a screen frame), and together form a navigable collection — a canvas of screens organized in pages or boards. The frame is the hinge of the whole model: screen-level behavior (clipping, layout rules, presentation, prototype connections) attaches to frames, not to loose objects.

**2. Editable layered UI composition.**
Inside a frame, the interface is composed from directly manipulable design objects — rectangles and ellipses, text, images, vector paths, and ready-made UI controls — organized in a layer hierarchy with styling (fills, strokes, borders, shadows, opacity, blend). The composition stays live and re-editable: any element can be selected, moved, restyled, regrouped, or masked at any time. The design is never a flattened picture; that is what separates a design application from a mockup image or a screenshot.

**3. The design-of-record posture.**
The screens are a specification for an interface that will be implemented elsewhere. The design file is inert by design: nothing in it runs, connects to data, or serves users. Its value is that it fixes, precisely and unambiguously, what the interface should look like and how it should be built — which is why every product in this space eventually grows a surface whose consumer is not the designer but the developer (measurements, styles, assets, code). If the artifact becomes the working interface, the product is a website builder or application builder, not a UI design application.

### Standard Capabilities of Mature Products

These are the structures mature products commonly add around the core. They make the tool practical; removing any one of them leaves the Type intact.

- **Reusable components.** A designed element (button, nav bar, card, icon) is saved as a reusable definition — *component* or *symbol* — and placed elsewhere as an *instance*. Editing the definition updates every instance; individual instances can carry local overrides; variants group the states of a component (default / pressed / disabled) into one swappable object. This is the strongest common structure in the category — but it is an accretion, not the definition: one-off screen design without any reuse machinery is still UI design.
- **Layout machinery.** Rules governing what happens to a frame's contents when the frame resizes: per-edge pinning/constraints, and auto-layout-class systems (flexible stacks that space and size children automatically, commonly modeled explicitly on implementation concepts such as CSS Flexbox). This is how designs express responsive intent.
- **Design-system assets.** Named, reusable styles (colors, text styles, effects), variables or design tokens, and shared libraries: component and style collections published from one file and consumed across many, with update-and-accept flows so changes propagate under the consumers' control.
- **Embedded prototyping.** Connections between frames — tap this element, go to that screen — with a presentation mode that plays the screens as a clickable simulation. Nearly all current products embed this in the same file; it is a capability of the design tool, not a separate identity (see Related Application Types).
- **Developer handoff.** A surface where non-designers can inspect the design: measurements, spacing, typography, color values, exported assets, and increasingly code snippets or production-ready code views for the selected elements.
- **Review and collaboration.** Comments pinned to the canvas, share links, view/edit permissions, and — in current products — live multi-user editing with presence.
- **Interchange.** Import of designs from other tools, export of screens and assets as images or vectors, and starter kits / UI kits to begin from.

### One Structure, Many Implementations

```text
Concept:            Screen frame
Implementations:    frames (device presets), artboards, boards, wireframe canvases

Concept:            Reusable component
Implementations:    main component + instances, symbol source + instances,
                    library drag-in controls

Concept:            Layout intent
Implementations:    constraints/pins, auto layout / stacks / flexible layout,
                    fixed-size frames with no layout rules

Concept:            Implementation handoff
Implementations:    inspect panels with code snippets, browser-based inspect
                    for developers, asset exports, design-to-code links
```

A reader who has only seen one implementation — say, a browser-based collaborative tool — should still be able to recognize a native single-user design tool, or an intentionally sketchy wireframing tool, as the same Type from the Core Model.

## How It Works

### Start a design file and lay out the screens

```text
Create a design file
→ draw screen frames (blank, or from device/platform presets)
→ organize frames across pages or boards
→ optionally start from a UI kit or template
```

There is no deployment target, no data connection, no build step. The file is a design workspace.

### Compose a screen

```text
Select a frame
→ add objects (shapes, text, images, vector paths, UI controls)
→ arrange them in the layer hierarchy
→ style them (fills, strokes, text properties, effects)
→ apply layout rules (constraints or auto-layout) where resize behavior matters
```

The interaction loop is direct manipulation: select, move, resize, restyle — with zoomable canvas navigation and keyboard-driven precision.

### Reuse instead of redraw

```text
Design an element once (e.g., a button)
→ save it as a component/symbol
→ place instances across screens
→ override per-instance content where needed (labels, icons, states)
→ edit the source; every instance updates
→ publish shared components/styles as a library for other files and teammates
```

### Review and iterate

```text
Share the file or screens
→ stakeholders view and comment on the canvas
→ designer resolves feedback by editing the same live artifact
→ optionally connect frames into a clickable prototype and let reviewers click through
```

### Hand off to implementation

```text
Mark screens as ready for development
→ developers open the inspect surface (often without the design editor)
→ read measurements, styles, and structure; export assets
→ optionally copy code snippets for the selected elements
→ build the real interface in code
→ return to the design file when the interface changes
```

The loop closes back at the design file: it remains the design of record as the product evolves.

### Capability tiers

**Defining core** — without these, not a UI design application:

- screen frames as the unit of design
- editable layered composition inside frames
- the design-of-record posture toward implementation

**Standard capabilities** — present in most mature products:

- reusable components (source/instance/overrides/variants)
- layout machinery (constraints, auto-layout)
- design-system assets (styles, tokens, shared libraries)
- embedded prototyping
- developer handoff/inspect surface
- comments, sharing, permissions; live collaboration in current products
- import/export and starter kits

**Common variants / optional** — depends on product, segment, era:

- fidelity posture (polished vs intentionally low-fidelity)
- editor substrate (browser vs native desktop; SaaS vs self-hosted)
- AI assist (drafting, prompt editing, agents, design-to-code links)
- suite scope (standalone editor vs multi-product design suite)
- audience breadth (professional designers vs non-designer product people)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Canvas with frames

The primary workspace: a zoomable canvas holding the screen frames side by side.

- typical information: frames with their names, layer outlines, alignment guides, device presets
- primary actions: create/duplicate/resize frames, move between pages, zoom and navigate

### Layers panel and inspector

The structural view and the property editor, usually flanking the canvas.

- typical information: layer hierarchy of the selected frame; position/size; fills, strokes, effects; text properties; layout rules
- primary actions: select/reorder/group/mask layers; edit properties; apply constraints or auto-layout

### Components / assets panel

The library of reusable elements available to the file.

- typical information: local components, imported libraries, styles and tokens
- primary actions: insert an instance, swap variants, create a component from a selection, publish or update libraries

### Prototype / presentation mode

The screen-flow surface.

- typical information: frames arranged as a flow with connections between them
- primary actions: link triggers to destinations, set device preview, play the prototype

### Inspect / developer surface

The implementation-facing view of the same design.

- typical information: measurements, spacing, typography and color values, layer structure, asset exports, code snippets
- primary actions: select elements, copy values/code, export assets, mark screens ready for development

### Comments and sharing

The review layer over the canvas.

- typical information: pinned comment threads, viewer presence, share permissions
- primary actions: comment, resolve, manage access

### File browser / dashboard

The container level above design files.

- typical information: projects, files, thumbnails, team/organization structure
- primary actions: create/organize files, open, share

## Important Rules / Behaviors

### Instances inherit; overrides bend; detach breaks

A placed instance follows its source: edits to the source propagate everywhere. Per-instance changes are overrides that bend the instance without breaking the link; detaching converts the instance into ordinary layers and ends the relationship. This inheritance discipline is what keeps a design system coherent across hundreds of screens.

### Layout rules bind the frame to its contents

Constraints and auto-layout attach behavior to structure: when a frame resizes, its children respond according to their constraints or stack rules, not arbitrarily. Designs that must express responsive intent carry these rules; purely fixed compositions may not.

### The frame defines the coordinate space and the screen boundary

Frames clip (or optionally don't clip) their contents, define the coordinate origin for what's inside, and act as the unit that presentation and prototype modes treat as "one screen". Content outside frames is workspace material, not part of any screen.

### The design is inert

Nothing in the design file executes. Prototypes simulate behavior with fabricated content; inspect surfaces describe the design; neither is the running product. The design's authority is descriptive — it specifies, it does not serve.

### Library updates are gated by the consumer

Changes to a shared library do not silently rewrite every consumer's file: consuming designers review and accept updates. This keeps shared evolution orderly across teams.

### Access distinguishes editing from viewing/inspecting

Permissions separate who may edit the design from who may view, comment, or inspect it. Developers commonly need inspect access without edit access; reviewers need comment access without either.

## Variants

- **Polished high-fidelity design tools** — the professional center of the category: full styling, component, layout, and handoff machinery for production-grade interface design.
- **Low-fidelity wireframing-first tools** — intentionally sketchy rendering and simple control libraries, built for the phase where teams are still deciding what to build; used heavily by non-designers; prototyping, where present, is a one-click derivative of the wireframe board.
- **Browser-first collaborative platforms** — the design file lives in the cloud, editing is real-time multiplayer, sharing and handoff are native to the medium.
- **Native desktop design tools** — the editor is a local application with local files; sharing and handoff added as layers on top (cloud workspaces, browser inspect).
- **Open-source / self-hostable tools** — the same core model, governed as open source and deployable on the buyer's own infrastructure.
- **Suite members** — UI design as the flagship editor of a wider design suite (whiteboards, slides, sites, prompt-to-code siblings sharing one file format and account).
- **AI-assisted editors** — any of the above with generation and prompt-driven editing layered in as accelerators.

A variant remains a variant unless it changes the defining core: a tool whose artifact becomes the working interface (website builder), or whose center of gravity becomes behavior rather than screen composition (prototype builder), has left the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Interactive Prototype Builder | sibling (04.15); sharpest seam | center of gravity: making screens *behave* through trigger→response interactions and a run mode, vs composing how screens *look*; merged products are one market with two centers of gravity — strip prototyping from a UI design tool and it is still one |
| UX Prototyping Application | sibling (04.15) | centers the prototyping/validation process (wireframes, flows, concept testing) rather than the screen-design artifact itself; the low-fidelity pole overlaps both — seam under joint review |
| Collaborative Design Platform | adjacent (04.01) | defined by its collaboration structure (shared multi-user design files) and subject-agnostic; a single-user UI design tool is in this Type without any shared file, and a shared design file holding a poster is not doing UI design |
| Graphic Design Application | adjacent (04.01) | same editor substrate (layers, vector tools), different target artifact: general visual deliverables vs user-interface screens with UI-specific machinery |
| Vector Graphics Editor | adjacent (04.03) | shares the vector substrate but has no screen frames, component/instance semantics, or implementation posture |
| Visual Website Builder / No-code Application Builder | adjacent (04.16 / 12) | produces the working interface operating on real data; the UI design application produces the specification of one — connect the artifact to a backend and deploy, and it has left this Type |
| AI Design Generator | adjacent (04.20) | generation-first (prompt → design) vs composition-first (human-directed editing); AI assist inside a manual editor does not change the Type |
| Template-based Design Platform | adjacent (04.01) | starts from browsed pre-made compositions for non-designers; UI design starts from blank or kit-seeded frames under designer control |
| Industrial Design Application | adjacent (04.15/16 domain) | designs physical product form with manufacturing precision; different design domain, only vocabulary overlap |

## Representative Products

- **Figma** — browser-first collaborative flagship; design, prototyping, and developer Dev Mode in one file system.
- **Sketch** — Mac-native design tool lineage; frames, symbols, libraries, workspace sharing, browser-based developer handoff.
- **Penpot** — open-source, self-hostable web tool; boards, components, tokens, inspect tooling.
- **Balsamiq** — intentionally low-fidelity wireframing-first tool; self-described "user interface design tool for creating wireframes", built for product people rather than designers.

The definition was checked against older and differently-positioned samples (the Fireworks generation, early single-user Sketch, the Photoshop/Illustrator comp era) to avoid over-fitting to the current cloud-collaborative pattern.

## Sources

Research date: **2026-09-09**

- Figma Help Center — https://help.figma.com/hc/en-us (Figma Design category; "Frames in Figma Design"; "Guide to components in Figma"; Dev Mode section)
- Sketch Documentation — https://www.sketch.com/docs/ (Designing; Frames; Symbols; Developer handoff)
- Penpot Help Center, User Guide — https://help.penpot.app/user-guide/ (Designing; Layers/Boards; Design Systems; Dev tools sections)
- Balsamiq — "What is Balsamiq?" https://balsamiq.com/support/getting-started/what-is-balsamiq/ ; "Spaces, projects, boards and wireframes" https://balsamiq.com/support/getting-started/cloud/spaces-projects-boards-and-wireframes/ ; product pages https://balsamiq.com/wireframes/ , https://balsamiq.com/product/wireframes/

> Sourcing notes: all four primary vendor surfaces were directly accessible on the research date. One Balsamiq documentation page (UI library reference) was not accessible; claims about that product are bounded accordingly. Historical samples were used for era-checks at market-structure strength and were not re-verified from live sources; no precise operational facts (numeric limits, defaults, plan-specific behavior) are asserted in this document.
