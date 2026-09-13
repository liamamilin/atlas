# Research Notes — Interactive Prototype Builder

Research date: 2026-09-07

## Research Goal

Understand what an Interactive Prototype Builder actually is as an Application Type: what objects exist inside it, how users build and experience interactive prototypes, how the interaction model works, how prototypes are shared and tested, and where the Type's boundaries lie against UI design tools, no-code builders, and adjacent leaves.

## Initial Boundary

Working hypothesis before research:

- Core purpose: build a clickable, interactive simulation of a user interface so a design can be experienced, communicated, and validated before engineering implementation.
- Likely users: UX/UI/product designers, product managers, researchers, stakeholders.
- Nearest neighbors: UI Design Application, UX Prototyping Application (same directory family 04.15), No-code Application Builder, Visual Website Builder, Digital Whiteboard, Collaborative Design Platform.
- Likely confusion: many products combine design + prototyping in one file (Figma, Sketch, Adobe XD); some prototyping tools drifted into website building (Framer). The Type boundary must be drawn on center of gravity, not on product packaging.

## Research Questions

1. What are the core objects (screens/frames/pages/scenes, hotspots, interactions, states, variables, flows)?
2. How are interactions expressed (trigger → response structure)?
3. What is the relationship between the design surface and the prototype (same file vs separate/imported)?
4. How does the run/preview mode work, and on what surfaces?
5. What logic capabilities exist (variables, conditions, expressions, data), and are they definitional or advanced-tier?
6. How are prototypes shared, reviewed, and tested?
7. Where is the boundary against no-code app builders and against UI design tools?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / position | Tier |
|---|---|---|
| Figma | Prototyping as a mode inside the dominant cloud design file; design + prototype in one artifact | Individual → Enterprise |
| Axure RP | Dedicated professional desktop prototyping tool; deepest explicit interaction/logic model | Professional / Enterprise |
| ProtoPie | Dedicated high-fidelity interaction specialist; sensor/voice/multi-device input; no-code formulas | Professional / Enterprise |
| Marvel | Lightweight web platform; screen-linking prototyping from uploaded images or simple in-tool design; user testing + handoff attached | Individual / SMB |

Deliberately excluded: InVision (discontinued; used only as a historical sample), Adobe XD (feature-frozen), Framer (drifted to website building — boundary case noted), Sketch (design tool with prototyping added; overlaps UI Design Application).

## Sources

All fetched 2026-09-07 (Tier 1 official documentation):

- Figma Help Center — "Guide to prototyping in Figma" — https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma
- Axure Docs — "Getting started with Axure RP" — https://docs.axure.com/axure-rp/
- Axure Docs — "Events, cases, and actions" — https://docs.axure.com/axure-rp/reference/events-cases-actions/
- ProtoPie Learn (official docs) — documentation index + "Triggers" — https://www.protopie.io/learn/docs/interactions/triggers (index covers Scenes, Layers, Containers, Devices, Triggers & Responses, Formulas, Variables, Components, Voice Prototyping, Connecting Devices, ProtoPie Cloud, ProtoPie Player, Teams, Handoff/Interaction Recordings, User Testing, ProtoPie Connect, Enterprise)
- Marvel Help Center — root + "A guide to creating your first prototype" — https://help.marvelapp.com/hc/en-us/articles/360002536038-How-to-create-a-prototype
- Marvel marketing site (Tier 2, positioning only) — https://marvelapp.com/

Failed fetches (recorded per source-access limitation rules): docs.axure.com interactions-basics URL (404, replaced by events-cases-actions), help.protopie.io (404, replaced by protopie.io/learn), marvelapp.com/help and one Marvel article (404/transport error, retried once then succeeded via help.marvelapp.com root + article).

## Product Observations

### Figma (evidence layer A — directly observed)

From the official prototyping guide:

- Prototyping is a mode of the design file ("Design" and "Prototype" tabs in the right sidebar; keyboard toggle). Anyone with edit access creates prototypes; anyone with view access plays them back in Presentation view.
- Stated purposes: preview interactions and user flows, share and iterate on ideas, get feedback, test interactions with users, present to stakeholders.
- **Flow** = the network of connected frames forming a path through a prototype; multiple flows per prototype; each flow has a **starting point**; a top-level frame can belong to multiple flows but has one starting point. Flow links can be shared individually.
- **Hotspot** = any object within a frame (link, button, image, icon) where an interaction takes place. **Connection** = the visual arrow ("noodle") from hotspot to destination; interaction and animation settings are applied via the connection.
- **Trigger** = the input event (tap, click, hover, drag, etc.). **Action** = the type of progression (navigate to another frame, open URL, etc.). **Animation/transition** = how the move happens (type, direction, duration, easing). Destination must be a top-level frame.
- **Overlays** = frames appearing above the current screen (tooltips, menus, alerts, confirmations). **Overflow behavior** = scroll response (carousels, galleries, maps). **Smart Animate** = advanced animation between frames.
- Advanced tier documented: variables, expressions, multiple actions and conditionals, variable modes.
- Prototype settings: device + model selection, background color, starting frame, orientation.
- Sharing/collaboration: share prototype, view on mobile device, comments on prototypes, presentation view options.

### Axure RP (evidence layer A)

From official docs (getting started + interactions reference):

- Dedicated desktop application. Files organized into **pages** (managed in a Pages pane); canvas for building; **widgets** from libraries (Default, Flow, Icons, Sample UI Patterns pre-installed; custom/team libraries possible).
- **Interactions** defined in an Interactions pane; explicit three-part structure: **event** (trigger fired by page/widget behavior, e.g. Click or tap) → **case** (ordered list of actions attached to an event; multiple cases per event; case selection can be manual at runtime or automatic via **conditional logic**) → **action** (the change, e.g. Open Link; actions execute in sequential order).
- Style effects change widget appearance on mouseover/click etc.; show/hide widgets dynamically; animations.
- Advanced tier: **variables**, conditional logic, **repeaters** (data-driven repeated widget structures), **adaptive views**.
- **Components** (reusable widget groups), **flow diagrams** as a separate artifact type, **page/widget notes** for documentation.
- **Publishing**: publish to Axure Cloud (hosted, shareable link, optional password) or private hosting (Axure Cloud for Business); **Preview** button opens the prototype in a local web browser; **team projects** for collaboration; AI/MCP integration documented.

### ProtoPie (evidence layer A)

From official docs (learn index + Triggers page):

- Dedicated desktop Studio + cloud ecosystem. Prototype file composed of **scenes**; screens built from **layers**; **containers**, **devices** (multi-device canvas), scroll/paging, system status bar.
- Interaction model: **Trigger → Response**. Trigger families documented: touch (tap, double tap, touch down/up, long press, fling, pull, drag, pinch, rotate — with per-trigger properties such as finger count, direction, distance, ratio, limits), conditional (chain — property of one layer drives another; range — fires when a property/variable enters a defined range; start — on scene load; detect — on property/variable change), mouse (over/out), key (press), input (focus in/out, return), sensor (tilt, compass, sound, 3D touch, proximity), **receive** (messages from other devices/scenes/components via Send/Receive with matching message strings and channels), voice command (with Listen response; include/exclude phrases).
- **Formulas** (expression language with functions and layer-property references) and **variables** (including predefined variables) are first-class.
- **Components** (reusable, nestable, with their own Send/Receive message channels), **interaction libraries** (shareable interaction collections).
- Run/test surfaces: **Preview window** in Studio; **ProtoPie Player** app on iOS/Android (and Wear OS) for on-device testing incl. offline; **ProtoPie Cloud** for managing/sharing prototypes; **user testing** module (test rooms, sessions, results/analysis, external integrations); **interaction recordings** as handoff artifacts.
- **ProtoPie Connect**: multi-prototype/multi-device/hardware/API communication server (Arduino, gamepad, steering wheel, IFTTT, Unity plugins; embedded variant for Raspberry Pi); positioned for automotive/aviation/IoT scenarios. Enterprise tier: SSO, organization settings.
- Import from Figma/Sketch/Adobe XD (design stays in the design tool; ProtoPie adds the behavior layer).

### Marvel (evidence layer A)

From official help center:

- Web platform. **Project** (choose Prototype type, name, device) → **screens**: upload JPG/PNG/GIF images from the computer, design in Marvel's built-in tool (pre-made assets, stock photos, icons), or sync artboards from Sketch via plugin.
- Prototype construction: in the editor, **click and drag over any area of the design to draw a hotspot** → **select the target image (screen)** for the hotspot → **Play** to interact with the prototype.
- Stated positioning: "turns static mockups, wireframes, and designs into interactive mobile and web experiences, all without needing to code"; prototype "looks and feels just like the real thing."
- Stated uses: getting tangible ideas down from people who might not know how to code, testing ideas for websites and apps, understanding user behavior, demonstrating ideas to stakeholders.
- Attached modules (same platform): user testing, developer handoff (automatic design specs), feedback/collaboration, iOS/Android apps, integrations/API, enterprise tier.
- Help-center categories confirm: Prototyping, User Testing, Developer Handoff, Feedback and collaboration, Manage and organise projects, Team administration, Account/billing, iOS and Android apps, Security, Enterprise, Integrations and API.

## Cross-product Comparison

| Aspect | Figma | Axure RP | ProtoPie | Marvel |
|---|---|---|---|---|
| Packaging | Prototype mode inside cloud design file | Dedicated desktop app | Dedicated desktop Studio + cloud + player apps | Web platform + mobile apps |
| Screen unit | Frame (top-level) | Page | Scene | Screen (uploaded image, in-tool design, or Sketch sync) |
| Screen origin | Drawn in-tool | Drawn in-tool | Drawn in-tool or imported from Figma/Sketch/XD | Uploaded images, in-tool design, Sketch sync |
| Interaction unit | Interaction on hotspot: trigger + action + animation | Event → case(s) → ordered actions | Trigger → Response | Hotspot drawn over area → target screen |
| Navigation action | Navigate to frame / open URL / overlay | Open Link / show-hide / many action types | Jump (scene) / layer responses / Send | Go to target screen |
| Transitions/animations | Transition types, direction, duration, easing; Smart Animate | Animations, style effects | Timelines, easing curves | Transition settings (advanced section) |
| Overlays/state change | Overlays (frames above screen) | Show/hide widgets, style effects | Layer responses, containers | Not confirmed in fetched docs |
| Scroll behavior | Overflow behavior | (not fetched in detail) | Scroll/paging feature | (not fetched in detail) |
| Logic tier | Variables, expressions, conditionals (advanced) | Variables, conditional logic, repeaters | Variables, formulas, ranges (first-class) | Not part of basic model (not confirmed) |
| Reusable interactive units | Components with prototype interactions | Components (masters) | Components with message channels | (not confirmed) |
| Run mode | Presentation view; device preview; mobile viewing | Preview in browser; hosted Axure Cloud viewer | Preview window; ProtoPie Player on devices | Play mode; iOS/Android apps |
| Sharing | Share links, per-flow links, comments | Publish to Axure Cloud, shareable link, password | Cloud sharing, teams, editors/viewers | Share links, comments/collaboration |
| Testing | Test interactions with users (via shared prototype) | (via hosted prototype) | User testing module (rooms, sessions, analysis) | User testing module |
| Handoff/documentation | Dev Mode (separate product surface) | Page/widget notes, flow diagrams | Interaction recordings | Developer handoff (design specs) |
| Beyond-screen input | Mouse/touch triggers | Mouse/touch/keyboard events | Touch, mouse, key, input, sensor, voice, device messages | Touch/click hotspots |

## Canonical Abstraction

### L0 — Defining Invariant

Four properties, held jointly. Removing any one stops the product from being an Interactive Prototype Builder:

1. **The screen set** — the prototype is composed of one or more discrete UI surfaces (screens / frames / pages / scenes) that stage the simulated experience. Screens may be drawn in the tool or imported as images. (Remove → no prototype exists.)
2. **User-defined interactions** — the author binds triggers (user input events on screen elements or areas) to responses (navigate to another screen, change what is shown, animate). This is the "interactive" in the Type name. (Remove → static mockup; UI-design territory.)
3. **Run mode** — a playback/simulation surface where the prototype responds to input as the real product would, experienced without authoring tools. (Remove → interaction specification document, not an experienceable prototype.)
4. **Design-artifact posture** — the prototype is a simulation of intended behavior for exploring, communicating, and validating design; it does not operate on real production data and is not deployed as working software. (Remove → no-code application builder.)

### L1 — Common Mature Structure

Present across the researched sample (3–4 of 4 products, directly observed) but not definitional:

- transitions/animations between screens with configurable type, direction, duration, easing
- overlays / show-hide state changes (modals, menus, tooltips, alerts)
- scroll/overflow behavior
- reusable interactive components (component/masters carrying their own interactions)
- multiple flows / starting points through one prototype
- hosted sharing with links (often password/permission options) and viewer access separate from editing
- comments/feedback on the prototype
- device preview / on-device testing apps
- version history / team collaboration (packaging varies)

### L2 — Variant / Optional Structure

- **Logic depth** — variables, expressions, conditional branching, data-driven repeated elements. Present as advanced tier in Figma, first-class in Axure/ProtoPie, absent from Marvel's basic model. Depth is a market differentiator, not a defining property.
- **Input breadth** — beyond touch/mouse: keyboard, device sensors (tilt, compass, sound, proximity), voice commands, inter-device messages, hardware/API integration. Specialist positioning (ProtoPie), not definitional.
- **Screen origin** — native design tools vs import from design tools vs uploaded images (paper-sketch photos in the POP tradition). All satisfy L0.
- **Attached workflow modules** — user testing, developer handoff/specs, interaction recordings, flow diagrams, documentation notes. Present in some products as adjacent modules.
- **Fidelity spectrum** — low-fidelity wireframe prototypes through high-fidelity pixel-accurate simulations.
- **AI assistance** — current-generation additions (AI interaction creation, AI document Q&A in one sampled product).

### L3 — Vendor-specific Structure (research notes only)

- Figma: Smart Animate; variable modes; per-flow share links; Dev Mode as separate surface; FigJam/Figma Sites/Figma Slides as sibling products (out of scope).
- Axure: explicit case model with runtime case-choice menus; adaptive views; repeaters; widget libraries; raised events; Axure Cloud for Business hosting; interaction disable toggles; MCP/AI integration.
- ProtoPie: Send/Receive message channels (scene/component/Studio/Connect); formulas syntax; predefined variables; ProtoPie Player (incl. Wear OS); ProtoPie Connect with plugin ecosystem (Arduino, Logitech G29, IFTTT, Unity, blokdots); interaction recordings; test rooms; enterprise SSO.
- Marvel: Ballpark (separate user-research product); Sketch sync plugin; automatic design-spec handoff; "Marvel vs InVision" positioning page.

### Rejected Findings

- "Prototyping requires variables/conditional logic" — rejected: Marvel's basic documented model has none; logic is a depth differentiator (L2).
- "Prototypes are built from screens designed in the same tool" — rejected: Marvel documents uploaded-image screens and Sketch sync; ProtoPie documents Figma/Sketch/XD import; POP-style paper-photo prototyping historically satisfies the Type. Screen origin is an implementation choice.
- "Prototyping requires cloud collaboration" — rejected: Axure RP is a desktop app with local preview; cloud sharing is a distribution mechanism (L1 at most).
- "Prototypes must target mobile" — rejected: web/desktop prototypes documented across the sample; device is a preview setting.
- "Prototype = wireframe" — rejected: wireframing is a design-side activity; the prototype builder's defining object is the interactive simulation, at any fidelity.

### Historical / Market-Sample Check

- **HyperCard (1987)**: stacks of cards, buttons linking cards, user mode vs editing mode — satisfies L0 (screens, interactions, run mode, design-artifact posture). ✓
- **POP / paper prototyping apps**: photos of paper sketches as screens, hotspots linking them, playback on a phone — satisfies L0; proves screens need not be natively drawn. ✓
- **InVision (2011–2024, discontinued)**: uploaded screen images + hotspots + transitions + comments + user testing — satisfies L0. ✓
- **Early Axure (2003+)**: pages + widgets + event/case/action interactions + browser preview — satisfies L0. ✓
- Conclusion: the L0 holds across eras, price tiers, and input paradigms. The definition must not require native design tools, cloud, collaboration, variables, or device frames.

## Boundary Findings

- **vs UI Design Application**: sharpest seam. Center of gravity: composing static screen visuals (design tool) vs making screens behave through interactions and run mode (prototype builder). Many products merge both in one file (Figma, Sketch, Adobe XD); the Type distinction is the center of gravity, not packaging. Removal test: strip interactions + run mode from a prototype builder → it becomes a UI design tool; strip nothing from a UI design tool and it still is one.
- **vs UX Prototyping Application (sibling leaf in 04.15)**: the two names overlap heavily in market usage — products documented here are sold as "prototyping tools" under both labels. Working seam from this side: UX Prototyping Application leans toward early-stage/low-fidelity/process-oriented prototyping (wireframes, flows, concept validation), while Interactive Prototype Builder centers on the interactive clickable simulation itself. This needs a joint review pass; recorded in STATUS.md.
- **vs No-code Application Builder / Web Application Builder**: the design-artifact posture is the seam. A prototype simulates behavior with fabricated data and is never the deployed product; a no-code builder produces working software operating on real data. Removal test: connect the artifact to a real backend and deploy it → no longer a prototype.
- **vs Digital Whiteboard**: whiteboard is a free-form ideation canvas (spatial, open-ended); prototype builder is structured screens + defined interactions + run mode. Some whiteboards add "connect to frame" presentation modes — presentation of static frames, not input-driven simulation.
- **vs Presentation Application**: presentations advance linearly through slides; prototypes respond non-linearly to user input. Hyperlink features in presentation tools can fake simple prototypes — a boundary case, not the Type.
- **vs Collaborative Design Platform**: platform packaging vs capability. Prototyping is one capability a design platform may embed.

## Uncertainties

- Marvel's advanced-prototyping depth (overlays, transitions detail) was not directly fetched; Marvel claims kept minimal accordingly.
- Axure's scroll behavior and comment features were not directly fetched; not claimed.
- ProtoPie's Responses list was read from the documentation index and Send/Receive docs, not the dedicated Responses page; response-type enumeration kept generic (move/scale/rotate/property-change/jump/send class).
- Whether the market still treats "UX Prototyping Application" and "Interactive Prototype Builder" as distinct categories is genuinely unclear; flagged for joint review rather than resolved here.
- InVision's shutdown (announced 2024) is background knowledge, not re-verified from a live source; used only as a historical sample note, not as evidence.

## Final Synthesis

An Interactive Prototype Builder is an application for building interactive simulations of user interfaces. Its world has four load-bearing structures: a set of screens staging the experience; user-defined interactions binding input triggers to responses; a run mode where the simulation is experienced; and the design-artifact posture — the simulation stands in for the real product without being one. Around this core, mature products add transitions, overlays, scroll behavior, reusable interactive components, flows, hosted sharing with comments, and device testing; logic depth, input breadth, screen origin, and attached testing/handoff modules vary by product and segment. The Type is defined by center of gravity: where a product's prototyping capability is a mode of a design tool, the Type still applies to that capability; where the artifact becomes working software, the product has left this Type.
