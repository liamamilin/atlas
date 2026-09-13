# UX Prototyping Application

## Overview

A **UX Prototyping Application** turns product ideas into experienceable interface simulations before any code is written: screens of the intended product are composed and linked with user-defined interactions into clickable flows, the simulation is run and shared, feedback and tests are collected, and the design is revised until it is approved for development.

The defining core is small:

```text
Screens of the intended interface
└── User-defined interactions (trigger → response)
    └── Clickable flows
        └── Run mode (the simulation, experienced without authoring tools)
            └── The validation loop: share → feedback/tests → iterate → approve → hand off
```

What makes this Type distinct is not an extra structure but the role the prototype plays: it is the instrument of the pre-implementation validation loop — the tool a team uses to decide *what to build* before building it. The prototype is never the deployed product; it operates on fabricated data and exists to be discussed, tested, and approved.

When the emphasis shifts to composing the polished screen design of record, the product is drifting toward a UI Design Application; when it shifts to the behavior depth and input realism of the simulation itself, toward an Interactive Prototype Builder; when the artifact becomes working software, the product has left prototyping entirely.

## Users & Context

The primary users are the people responsible for shaping a digital product before implementation:

- **UX/product designers** — build the screens, wire the interactions, run and refine the simulation.
- **Product managers and business analysts** — express requirements as clickable flows, validate scope with stakeholders, gather approval.
- **Founders, consultants, and non-designer product people** — sketch ideas quickly at low fidelity to communicate and test a concept.

Secondary participants consume the prototype rather than build it: **stakeholders and clients** review, comment, and approve; **developers** read specs and measurements for implementation; **test participants** click through the simulation in usability tests.

The work context is a team deciding what to build: early project phases, concept pitches, scope negotiations, design reviews, and pre-development approval. The characteristic tension the tool resolves is that static pictures undersell an interaction design, while working code is too expensive to change — the prototype sits deliberately between the two.

## Core Model

### The Defining Core

**Screens.** The prototype is composed of discrete UI surfaces — pages, screens, frames, or wireframes — each staging one state of the intended product. Screens are held in a navigable collection (a sitemap or page list) and may be drawn in the tool, assembled from UI element libraries, imported from design tools, or drafted by AI. Screens are the unit of composition and the targets of navigation.

**Interactions.** The behavior layer. The author binds a **trigger** — click/tap, double-click, hover, swipe, key press, page load, value change — on a screen element (or the screen itself) to a **response**: navigate to another screen, show/hide or toggle content, change an element's state, set a value. Interactions turn the screen set from pictures into an experience. Mature tools layer transitions and animations (easing, duration, delay) on top, and offer conditional logic — if-then-else rules over variables and input values — so the simulation can approximate real application behavior such as form validation.

**Flows.** Screens linked by interactions form paths through the product — a sign-up flow, a checkout flow. A prototype commonly carries multiple flows with their own starting points, and many tools also let the team *diagram* flows as first-class artifacts (user-flow maps, sitemaps) alongside the clickable simulation.

**Run mode.** A playback surface where the simulation responds to input the way the intended product would, experienced without authoring tools: a browser-based viewer, a full-screen present mode, or a companion app on a real device. The run mode is what stakeholders and test participants use; it is deliberately separate from the editor.

**The validation loop.** The prototype is built to leave the tool: shared by link with role-based access (viewers vs editors), annotated with comments, exercised in usability tests, revised through iterations or versions, and finally approved as the basis for development handoff. Mature tools make each stage of this loop a first-class surface — separate modes for experiencing, commenting, inspecting specs, and reading documentation.

### Standard Capabilities

These are carried by most mature products. They make the loop practical but do not define the Type:

- **UI element and stencil libraries** — ready-made, platform-specific controls (web, iOS, Android) dragged onto screens; custom libraries and design-system components in team settings.
- **The fidelity ladder in one artifact space** — the same tool carries work from rough wireframe through styled mockup to high-fidelity interactive prototype, so the team never has to switch tools as the idea matures.
- **Reusable components, masters, and templates** — shared elements that update everywhere; master screens applied across pages.
- **Overlays and state changes** — modals, menus, tooltips shown above the current screen; elements with named states.
- **Scroll behavior** — scrollable regions, sticky elements.
- **Responsive/adaptive variants** — the same screen laid out for multiple device sizes, previewed per breakpoint.
- **Forms and data simulation** — working inputs, dropdowns, data lists and grids, so data-entry experiences can be tested, not just pictured.
- **Logic depth** — variables, conditions, expressions; the depth varies widely by product (absent in the simplest tools, first-class in the most advanced).
- **Sharing and feedback machinery** — share links, viewer/editor roles, password protection, embeds, comment threads on the running prototype.
- **Device preview** — companion mobile apps and device frames so the simulation is felt on the hardware it targets.
- **Developer handoff** — spec/inspect surfaces, measurements and annotations, documentation, sometimes generated code.
- **Versioning** — iterations of the prototype so feedback can be tied to a specific round.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Screens:            drawn in-tool, assembled from stencil libraries,
                    imported/synced from design tools, AI-drafted,
                    photos of paper sketches
Interactions:       hotspot links, event→action panels,
                    trigger→response with conditions and variables
Run mode:           browser viewer, full-screen present mode,
                    companion device app, embedded iframe
Validation loop:    share links + comments, review invitations,
                    usability-test modules, spec/documentation modes,
                    approval before development
```

A reader who has only seen one implementation — say, AI-drafted screens wired in a browser — should still recognize a paper-sketch prototype linked by hotspots as the same Type.

## How It Works

### Express the idea as screens

```text
Create a project (choose target device and canvas size)
→ compose screens: drag UI elements from libraries, draw shapes and text,
  import images or designs, or draft with AI
→ start rough (wireframe fidelity) or polished, depending on the question being asked
```

There is no backend, no real data, no deployment target. The screens represent intent.

### Wire the screens into an experience

```text
Select an element (or the screen)
→ add an interaction: choose a trigger (click, swipe, hover, load…)
→ choose a response (go to screen, show/hide, set state, set value…)
→ optionally add a transition (type, easing, duration)
→ repeat until the flow is walkable
→ optionally add conditions and variables for realistic behavior
```

Many tools shortcut the common case: dragging an element onto a target screen creates the click-to-navigate interaction automatically.

### Simulate

```text
Press play / open preview
→ the simulation runs in a viewer (browser, full screen, or device app)
→ click through the flows as a user would
→ navigate freely via the sitemap, or follow the defined paths
```

The author simulates to check the design; stakeholders and test participants simulate to experience and evaluate it.

### Share, gather feedback, iterate

```text
Share a link (viewers can experience and comment; editors can change)
→ stakeholders comment on the running prototype
→ usability tests exercise the flows with real participants
→ revise screens and interactions; keep iterations distinct
→ repeat until the design is agreed
```

### Approve and hand off

```text
Final review and approval
→ hand off: specs and measurements for developers, documentation for the team,
  annotations linked to requirements — sometimes generated code
→ development proceeds; the prototype remains the record of what was agreed
```

The loop, not any single deliverable, is the unit of work: a prototype that is never shared, tested, or approved has not done its job, however polished its interactions.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Editor canvas

The authoring surface. A canvas holding the screens, flanked by:

- a **screens/pages panel** with a sitemap — add, nest, reorder, duplicate, hide screens
- **libraries** of UI elements and stencils, filtered by platform
- an **interactions panel** — triggers, responses, conditions per element
- **properties** — styling, position, size, visibility during simulation
- **layers/outline** — the element hierarchy of each screen

Primary actions: compose screens, wire interactions, manage pages.

### Run / preview mode

The simulation surface, reachable from the editor and from share links.

- presents the prototype full-screen or in a device frame, with touch-appropriate cursors
- responds to the defined interactions; often offers free navigation via the sitemap
- may expose toggles for adaptive variants and highlight where interactions exist

Primary actions: experience the flow; this surface is intentionally passive — no editing.

### Share / review surface

The loop's connection to stakeholders.

- share links with role selection (view vs edit), optional password, embed codes
- comment threads pinned to screens or moments in the flow
- review invitations and notifications

Primary actions: share, comment, reply, resolve feedback.

### Spec / documentation surface

The handoff connection to developers and the team record.

- measurements, styling values, and annotations per element
- documentation pages describing intended behavior
- sometimes generated code or code-backed component inspection

Primary actions: inspect, read, export.

### Device preview

A companion app on a real phone or tablet that loads the shared prototype with interactions intact, updating live as the author edits.

### Flow / sitemap views

Some tools add a diagram surface over the screen set — user-flow maps, sitemaps — for planning and communicating the experience's structure independently of the clickable simulation.

## Important Rules / Behaviors

### The prototype is never the product

The simulation operates on fabricated data and is not connected to production systems. The moment the artifact is connected to a real backend and deployed as working software, the team has left prototyping — this is the Type's hard boundary. (A few current products deliberately blur it by generating runnable code from prototype intent; see Variants.)

### Interactions live on elements, and they can break

Interactions attach to screen elements or to the screen itself. When a targeted element or screen is deleted, the interaction becomes broken; mature tools flag these visibly so dead links don't reach stakeholders. Interactions can usually be copied between elements and screens.

### Visibility governs the simulation

Hidden screens and layers are excluded from the run mode and exports; what the stakeholder experiences is exactly what the author chose to expose. Preview access (sitemap, comments, specs) is typically configurable per share link.

### Viewers experience; editors change

The share model separates people who can navigate and comment on the simulation from people who can modify it. Approval flows on top of this: the prototype's link is the artifact being approved.

### The simulation is stateless between sessions

A prototype run starts from its defined starting screen(s); it carries no user accounts and no persisted user data. Conditional logic manipulates in-memory variables for the sake of realism, not record-keeping.

### Fidelity is a deliberate choice

Low-fidelity rendering is often a feature, not a limitation: sketchy screens keep feedback focused on structure and flow rather than visual polish. The same tool typically supports raising fidelity in place as the design matures.

## Variants

- **Realism-first prototyping** — code-backed components and production-grade rendering so prototypes "feel like the real thing"; favored by enterprise design-system teams; often pairs deep logic (variables, conditions, API calls) with developer handoff.
- **Early-stage all-in-one workspaces** — wireframes, diagrams (user flows, sitemaps), whiteboards, and prototypes bundled in one collaborative app for cross-functional teams; prototyping is one pillar of a broader visual-collaboration surface.
- **Intentionally low-fidelity wireframing with clickable derivatives** — sketchy screens aimed at product people rather than designers; clickable prototypes generated from the wireframe set as a lightweight derivative.
- **Full-spectrum dedicated prototyping tools** — wireframe-to-high-fidelity in one project, with forms/data simulation, responsive prototyping, and requirements/specification modules attached.
- **Flow-and-presentation companions** — tools that import finished screens from design tools and center the user-flow diagram, design presentation, and asynchronous critique; the simulation is navigational rather than deeply behavior-simulating.
- **AI-drafted prototyping** — screens generated from text descriptions or imported webpages, then edited and wired by hand; AI as accelerator inside the loop.
- **Prototype-to-working-app (boundary-crossing)** — a current-generation posture that generates runnable code from prototype intent and hosts it as a working demo; deliberately crosses into no-code-builder territory while marketing itself as prototyping.
- **Specialist simulation depth** — sensor, voice, and multi-device input prototyping for embedded and hardware-adjacent experiences (documented under the sibling Interactive Prototype Builder Type; the populations overlap).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Interactive Prototype Builder | sibling; shares this Type's population and core | centers the interactive simulation artifact itself — behavior depth, input realism, run-mode fidelity (including specialist simulation tools); this Type centers the prototyping/validation process around that artifact. The two labels are used interchangeably in the market for the same products; the seam is emphasis, not structure |
| UI Design Application | sibling; heaviest packaging overlap | centers the screen-design artifact of record — the polished specification developers implement; this Type centers the process of exploring and validating what to build. Products that merge both are one market with two centers of gravity |
| Collaborative Design Platform | adjacent; packaging overlap | defined by shared multi-user design files, subject-agnostic (posters to product UI); here the defining object is the interactive prototype and the loop around it |
| AI Design Generator | adjacent; capability convergence | generation-first production of designs from prompts; here generation is at most an accelerator inside a human-directed process |
| No-code Application Builder / Visual Website Builder | hard boundary | produces working software operating on real data; the prototype simulates intent and is never deployed |
| Digital Whiteboard / Collaborative Canvas | adjacent | free-form ideation surface; lacks screen semantics, interaction wiring, and a run mode |
| Diagramming Application | adjacent | generic process diagrams; a user-flow *diagram* pictures the journey, the prototype makes it walkable |
| Presentation Application | weak overlap | advances linearly through slides; the prototype responds non-linearly to user input |
| Design Handoff / Developer-inspect surfaces | downstream consumer | consumes the approved prototype; handoff is one stage of this Type's loop, not the whole |

The 04.15 family (UI Design, UX Prototyping, Interactive Prototype Builder) describes one shared tool space from three centers of gravity — the design artifact, the validation process, and the simulation behavior. Flagship products span all three in one file; the Types remain distinct because their defining questions differ: *what should the screens look like*, *is this the right thing to build*, and *how should the experience behave*.

## Representative Products

- **UXPin** — realism-first pole: code-backed components, deep conditional logic, spec/documentation modes, AI product lines
- **Justinmind** — full-spectrum dedicated prototyping: wireframes to high-fidelity, forms/data simulation, requirements and specifications
- **Moqups** — early-stage all-in-one: wireframes, diagrams, and prototypes with real-time collaboration in one browser app
- **Balsamiq** — intentionally low-fidelity wireframing with clickable prototypes, aimed at product people

The core model was cross-checked against the sibling passes' samples (Figma, Axure RP, ProtoPie, Marvel, Sketch, Penpot) and against historical and boundary samples (HyperCard, early Axure, the InVision generation, paper-prototyping apps, and the user-flow tool Overflow) to avoid over-fitting to any one era, fidelity pole, or packaging.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces:

- UXPin Docs — https://www.uxpin.com/docs/ (Getting started; Editor interface; Interactions; What is Wire; Preview and Share)
- Justinmind Help Center — https://www.justinmind.com/support/ and https://www.justinmind.com/support/start-prototyping-web-and-mobile-apps/
- Balsamiq — https://balsamiq.com/support/getting-started/what-is-balsamiq/
- Moqups — https://moqups.com/ (product pages)
- Overflow — https://overflow.io/ (boundary probe, product pages)

Cross-pass context (fetched 2026-09-07 and 2026-09-09, recorded in the paired research notes): official documentation of Figma, Axure RP, ProtoPie, Marvel, Sketch, Penpot.

> Sourcing limitation: Moqups' help center could not be reached from the research environment (transport error; one attempt, then abandoned). Moqups observations therefore rest on its product pages, and claims about its prototyping mechanics are held at positioning strength. Balsamiq's clickable-prototype mechanics rely on the earlier pass's documentation fetches. Precise vendor-specific details (interaction-ordering rules, plan-gated features, named product modules) are kept in the Research Notes rather than asserted here.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample checks are recorded in the paired Research Notes.
