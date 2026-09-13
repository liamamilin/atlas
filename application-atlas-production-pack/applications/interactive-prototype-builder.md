# Interactive Prototype Builder

## Overview

An **Interactive Prototype Builder** is an application for building interactive simulations of a user interface. The author assembles a set of screens, connects them with user-defined interactions — "when the user taps this button, go to that screen" — and then experiences the result in a run mode that responds to input the way the intended product would.

The defining structure is small:

```text
Screen set (the staged UI surfaces)
└── Interactions (trigger → response, bound to elements or areas)
    └── Run mode (the simulation experienced without authoring tools)
        └── Design-artifact posture (a simulation of the product, not the product)
```

The prototype exists to make a design **experienceable, communicable, and testable** before engineering builds it: designers can preview flows, stakeholders can react to something concrete instead of static pictures, and researchers can put the intended product in front of real users. The boundary is equally important: a prototype simulates behavior with fabricated content and is never deployed as working software. When the artifact becomes a real application operating on real data, the work has left this Type.

## Users & Context

**Primary users** are product, UX, and UI designers. They build prototypes to explore how a design should behave, to communicate interaction intent to teammates and stakeholders, and to prepare usability tests. In products where design and prototyping share one file, the same designer moves between composing screens and wiring their behavior.

**Secondary users** experience prototypes rather than build them:

- product managers and founders, who walk through flows to validate product logic before committing to build
- stakeholders and clients, who review and comment on hosted prototypes
- researchers and test participants, who use the prototype as the stimulus in usability sessions
- developers, who consume the prototype (sometimes alongside specs or recordings) as the behavioral reference for implementation

Typical context: product definition and design refinement — from rough flow sketches to pixel-accurate simulations — used in design reviews, stakeholder demos, and user testing. Prototypes are usually short-lived artifacts tied to a design question; they are revised or discarded as the design settles, not maintained like production software.

## Core Model

### The Defining Core

**Screens.** The prototype is composed of one or more discrete UI surfaces — called frames, pages, or scenes depending on the product — that stage the simulated experience. Screens may be drawn with the tool's own design capabilities or imported as finished images; the Type does not require native drawing tools. Screens are the stages on which everything else happens.

**Interactions.** The author defines rules that bind a **trigger** — a user input event such as tap, click, hover, drag, or key press, occurring on a specific element or area of a screen — to a **response**: navigate to another screen, show or hide something, animate a change. The interaction is the unit that makes a mockup interactive; without it, the artifact is a static design.

**Run mode.** Every prototype builder provides a playback surface where the prototype runs as a simulation: the author or a viewer interacts with it, the current screen responds, transitions play, and navigation follows the defined interactions. The run mode is experienced without authoring tools — viewers navigate and trigger, but do not edit.

**Design-artifact posture.** The prototype stands in for the real product. Its data is fabricated, its buttons do not perform real transactions, and it is not deployed as software. This posture is what keeps the Type distinct from application builders.

### What Mature Products Add

These capabilities are widespread in current products but do not define the Type:

- **Transitions and animations** between screens — configurable movement type, direction, duration, and easing; some products can animate matching elements between screens automatically
- **Overlays and state changes** — content appearing above the current screen (menus, dialogs, tooltips) or elements changing visibility/appearance in place
- **Scroll behavior** — areas of a screen that scroll or page independently, enabling realistic lists, carousels, and galleries
- **Reusable interactive components** — buttons, menus, or cards defined once with their own interactions and reused across screens
- **Flows** — named paths through the prototype (e.g., sign-up, checkout), each with its own starting screen, so one prototype can cover several journeys
- **Hosted sharing** — the prototype published to a link that viewers open in a browser or mobile app, with comments attached at specific points
- **Device preview** — the prototype presented in a device frame or on a physical phone, so gestures and scale feel realistic

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Screen set
Implementations:  frames in a design file, pages in a desktop project,
                  scenes in a studio document, uploaded screen images

Concept:   Trigger
Implementations:  tap/click, hover, drag, key press, long press,
                  device sensors, voice, messages between devices

Concept:   Response
Implementations:  navigate to screen, show/hide, animate property,
                  open overlay, jump to scene, send a message

Concept:   Run surface
Implementations:  in-editor preview, browser playback, hosted viewer,
                  native mobile player app
```

A reader who has only seen one implementation — say, hotspots drawn over uploaded images — should still recognize a variables-and-conditions prototype, and vice versa, as the same Type.

## How It Works

### The build loop

```text
Compose screens (draw them, import images, or sync from a design tool)
→ select an element or drag an area on a screen
→ choose a trigger (tap, click, hover, drag…)
→ choose a response and its target (another screen, an overlay, a state change)
→ configure the transition (movement, timing, easing)
→ run the prototype and try it
→ adjust screens and interactions, repeat
```

This loop is the daily work of the Type. Authoring tools make the interactions visible on the canvas — typically as arrows or markers connecting triggers to their targets — so the author can see the prototype's logic at a glance and edit it by manipulating those connections.

### The share-and-review loop

```text
Publish the prototype to a hosted link
→ viewers open it in a browser or on a phone
→ they experience the flows without authoring access
→ they leave comments at specific screens or moments
→ the author revises screens/interactions and republishes
```

Sharing separates the audience from the author: viewers get the run mode, not the editor. Larger teams manage versions, permissions, and multiple flows so different audiences can be given different journeys.

### The test loop

```text
Put the prototype in front of a user
(in person on a device, remotely via a link, or through an attached testing module)
→ observe where they tap, where they hesitate, where the flow breaks
→ feed the findings back into the design
→ rebuild the affected screens and interactions
```

Some products treat testing as an attached module with session recording and analysis; in others the loop is manual — the prototype is simply the stimulus a researcher hands to a participant.

### Logic depth (varies by product)

At the simple end, interactions are one trigger → one response. Advanced products add state that persists across screens — variables, conditions ("if the cart is empty, go here; otherwise, go there"), and computed values — allowing prototypes to simulate multi-step logic such as forms, carts, and personalized states. The depth is a differentiator between products, not a requirement of the Type.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Authoring canvas

Where screens live side by side and are composed or placed.

- typical information: the screen set, screen names, interaction markers/arrows between screens
- primary actions: create/duplicate/organize screens, draw or place content, draw hotspots, connect screens

### Interaction panel

Where a selected element's behavior is configured.

- typical information: the element's triggers, each trigger's responses, targets, and transition settings
- primary actions: add/edit/remove interactions, set trigger type, set response and target, set timing/easing

### Run / preview surface

The simulation itself, full-screen or in a device frame.

- typical information: the current screen, transition animations, overlays
- primary actions: interact (tap/click/hover/drag/scroll), navigate, restart, switch flows

### Share / viewer surface

The hosted experience for reviewers and testers.

- typical information: the running prototype, flow list, comments, version
- primary actions: play the prototype, switch flows, comment, report an issue

### Prototype settings

Per-prototype presentation configuration.

- typical information: device/frame, orientation, background, starting screen(s)
- primary actions: set device model, set starting point, configure sharing access

## Important Rules / Behaviors

- **Interactions bind to elements or areas, not to screens alone.** The same screen can behave differently depending on which part of it is triggered; a screen with no interactions is a dead end in the run mode.
- **The run mode is an experience, not an editor.** Viewers can navigate and trigger but cannot alter the prototype; editing happens only in the authoring surface, typically under separate permission.
- **Behavior is simulated.** Responses are pre-authored; data shown in the prototype is fabricated by the author. A prototype cannot do anything its interactions do not define.
- **Design and prototype stay coupled in same-file products.** Where the prototype is a mode of the design file, changes to a screen's visuals flow into the prototype automatically. Where screens are imported, the prototype reflects the imported snapshot; how design changes propagate afterward varies by product.
- **Multiple flows coexist in one prototype.** Each flow has its own starting screen; sharing can target the whole prototype or a single flow.
- **Fidelity is a spectrum under one interaction model.** The same trigger→response structure works over pencil-sketch photos, wireframes, and pixel-accurate screens; fidelity changes the look, not the mechanics.

## Variants

- **Suite-embedded prototyping** — prototyping as a mode of a design tool's file; design and behavior in one artifact; the dominant current packaging.
- **Dedicated prototyping tool** — a standalone application centered on the prototype itself, often importing screens from design tools; ranges from simple screen-linking web apps to professional desktop tools with deep logic.
- **Logic-heavy professional prototyping** — variables, conditions, expressions, and data-driven elements as the core pitch, for simulating complex product behavior.
- **High-fidelity interaction specialist** — emphasis on realistic motion and input: device sensors, voice, multi-device scenarios, hardware integration; common in automotive, IoT, and device-design contexts.
- **Lightweight screen-linking** — uploaded images + hotspots + transitions + sharing; optimized for speed and accessibility over depth.
- **Testing- and handoff-attached platforms** — prototyping bundled with user testing, developer handoff specs, or interaction recordings as one design-validation platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| UI Design Application | closest neighbor, often merged in one product | composes static screen visuals; has no interaction wiring or run mode as its center of gravity. A design tool's prototyping mode is this Type's capability embedded in that product |
| UX Prototyping Application | sibling leaf; heavy market overlap | leans toward early-stage, low-fidelity, process-oriented prototyping (wireframes, flows, concept validation); the Interactive Prototype Builder centers on the interactive clickable simulation itself. The seam deserves joint review |
| No-code Application Builder | boundary at the artifact posture | produces working software operating on real data and deployed to users; a prototype simulates behavior with fabricated data and is never the deployed product |
| Visual Website Builder | boundary at the artifact posture | publishes real websites; a prototype only simulates the website's behavior |
| Digital Whiteboard | adjacent ideation surface | free-form spatial canvas for ideation; no screen-and-interaction structure, no input-driven run mode |
| Collaborative Design Platform | packaging relationship | a platform may embed prototyping as one capability among design, handoff, and delivery |
| Presentation Application | superficial similarity | advances linearly through fixed slides; a prototype responds non-linearly to user input. Hyperlinks in presentations can fake simple prototypes — a boundary case, not the Type |

The boundary with the **UI Design Application** is the most important one, because current market leaders merge both in one file. The structural test is the center of gravity: strip the interactions and the run mode from a prototype builder and what remains is a design tool; a design tool without them was never a prototype builder.

## Representative Products

- **Figma** — prototyping as a mode of the dominant cloud design file; flows, triggers/actions, overlays, variables, presentation view
- **Axure RP** — dedicated professional desktop tool; explicit event/case/action interaction model with variables, conditional logic, and data-driven elements; hosted publishing
- **ProtoPie** — dedicated high-fidelity interaction specialist; trigger→response model extended to sensors, voice, and multi-device scenarios; on-device player and cloud sharing
- **Marvel** — lightweight web platform; screens from uploaded images, in-tool design, or Sketch sync; hotspots, transitions, play mode, with attached user testing and handoff

The core model was checked against older and differently positioned samples (HyperCard-style card stacks, paper-sketch photo prototyping, the discontinued screen-linking generation of web prototyping tools) to avoid defining the Type by the current design-suite implementation.

## Sources

Research date: **2026-09-07**

- Figma Help Center — Guide to prototyping in Figma — https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma
- Axure Docs — Getting started with Axure RP — https://docs.axure.com/axure-rp/
- Axure Docs — Events, cases, and actions — https://docs.axure.com/axure-rp/reference/events-cases-actions/
- ProtoPie Learn (official documentation) — Triggers — https://www.protopie.io/learn/docs/interactions/triggers (documentation index covering scenes, layers, triggers & responses, formulas, variables, components, cloud, player, user testing, connect)
- Marvel Help Center — A guide to creating your first prototype — https://help.marvelapp.com/hc/en-us/articles/360002536038-How-to-create-a-prototype
- Marvel — product site (positioning only) — https://marvelapp.com/

> Sourcing note: all claims above are grounded in the official documentation fetched on the research date. Some per-product details (e.g., the full response catalog of one product, advanced-feature depth in another) were not directly fetched and are therefore kept generic in this document; product-by-product observations and evidence limits are recorded in the paired Research Notes.
