# Research Notes — UI Design Application

Research date: **2026-09-09**

## Research Goal

Understand, from real products, what a UI Design Application actually is: what the central working artifact is, what UI-specific structure the object model carries (screen containers, layers, reusable components, layout machinery, design-system assets), what the typical workflow is from blank frame to implementation handoff, and where the boundary lies with the neighboring Types in family 04.15 (UX Prototyping Application, Interactive Prototype Builder) and adjacent families (Collaborative Design Platform, Graphic Design Application, Vector Graphics Editor, Visual Website Builder, AI Design Generator).

This pass also carries three ratification duties left by earlier passes:

1. **interactive-prototype-builder** (processed 2026-09-07): ratify from this side the center-of-gravity seam (static visual composition vs behavior + run mode) with merged-in-one-file products documented as capability-embedded packaging.
2. **collaborative-design-platform** (processed): ratify or reject the working distinction (collaboration structure vs target artifact) and resolve the "same flagship product" tension.
3. **ai-design-generator** (processed): ratify from this side the boundary against generation-first UI tools (Uizard-class).

The **ux-prototyping-application** leaf is still unprocessed; the joint review it owes this family can only be partially discharged from this side.

## Initial Boundary

- Hypothesis: a UI Design Application is an editor whose world is organized around **screens of digital product interfaces** — the design file holds screen-sized frames composed of editable layers, with UI-specific reuse machinery (components/symbols), and the output is a design that engineers implement in code.
- Primary users: product/UI designers, product teams; secondarily developers (as consumers of the design) and non-designer stakeholders (as reviewers).
- Nearest neighbors: UX Prototyping Application and Interactive Prototype Builder (same directory family), Collaborative Design Platform (the market flagship is the archetype of both leaves), Graphic Design Application, Vector Graphics Editor, Template-based Design Platform, Visual Website Builder / No-code Application Builder, AI Design Generator.
- Known tensions going in:
  - Figma is the archetype of both this leaf and Collaborative Design Platform (flagged by the collaborative-design-platform pass).
  - Figma/Sketch/Adobe XD merge design and prototyping in one file (flagged by the interactive-prototype-builder pass).
  - Uizard-class products generate UI designs from prompts (flagged by the ai-design-generator pass).
  - Wireframe-first products (Balsamiq-class) sit at a fidelity/phase pole that may belong either here or to UX Prototyping.

## Research Questions

1. What is the central artifact, and what is its internal structure (container → layers → objects)?
2. What makes the object model UI-specific rather than generic vector editing?
3. What reuse machinery exists (components/symbols/instances/variants/libraries) and how does it behave?
4. What layout machinery exists (constraints, auto-layout/stacks/flexible layout) and is it definitional?
5. What is the workflow from blank file to handoff? Where do prototyping, review, and developer handoff sit?
6. What is the design's relationship to the implemented product (design-artifact posture)?
7. Who uses the tool, and who only consumes its output?
8. Which capabilities are definitional vs common-mature vs variant vs vendor-specific?
9. Do older / differently-positioned products (pre-cloud, native, low-fi, single-user) still fit the definition?
10. Where are the exact seams vs UX Prototyping, Interactive Prototype Builder, Collaborative Design Platform, AI Design Generator, website builders?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence tier |
|---|---|---|---|
| Figma | browser-first, cloud-collaborative flagship; design+prototype+dev-mode suite | freemium individual → enterprise | Tier 1 (help center) |
| Sketch | Mac-native design tool lineage; design-system workflow; workspace sharing | professional designers / teams (paid Mac app) | Tier 1 (documentation) |
| Penpot | open-source, self-hostable, web-native; "Full-Stack Design" framing | free individuals → self-hosting orgs | Tier 1 (user guide) |
| Balsamiq | intentionally low-fidelity wireframing-first; "product people, not designers" | individuals / small product teams; per-editor SaaS + Confluence/Jira editions | Tier 1 (help center) + Tier 2 (product pages) |

Historical / market-sample checks (not live-fetched; held at market-structure strength, see Uncertainties): Adobe Fireworks generation, early single-user Sketch, the Photoshop/Illustrator comp era.

## Sources

All fetched 2026-09-09. All four primary vendor surfaces were reachable.

- Figma Help Center (Tier 1): https://help.figma.com/hc/en-us — home; Figma Design category (https://help.figma.com/hc/categories/360002042553); "Frames in Figma Design" (https://help.figma.com/hc/en-us/articles/360041539473); "Guide to components in Figma" (https://help.figma.com/hc/en-us/articles/360038662654); Dev Mode section (https://help.figma.com/hc/sections/15023066873239).
- Sketch Documentation (Tier 1): https://www.sketch.com/docs/ — Designing section (https://www.sketch.com/docs/designing/); Frames (https://www.sketch.com/docs/designing/frames/); Symbols (https://www.sketch.com/docs/symbols-and-styles/symbols/); Developer handoff (https://www.sketch.com/docs/developer-handoff/).
- Penpot Help Center (Tier 1): https://help.penpot.app/ — User guide (https://help.penpot.app/user-guide/); Designing section (https://help.penpot.app/user-guide/designing/); Layers/Boards (https://help.penpot.app/user-guide/designing/layers/).
- Balsamiq (Tier 1 help + Tier 2 product): "What is Balsamiq?" (https://balsamiq.com/support/getting-started/what-is-balsamiq/); "Spaces, projects, boards and wireframes" (https://balsamiq.com/support/getting-started/cloud/spaces-projects-boards-and-wireframes/); wireframe product page (https://balsamiq.com/product/wireframes/); Cloud product page (https://balsamiq.com/wireframes/).
- Access limitation: https://balsamiq.com/wireframes/ui/ returned HTTP 403 (1 attempt, abandoned per the network rule). Balsamiq's component-library mechanics are therefore evidenced at product-page + help-center level, not at per-control documentation level.
- Historical samples (Fireworks, early Sketch, Photoshop/Illustrator comp era) were **not** re-verified from live sources; used only for qualitative era-checks, no precise claims.

## Product Observations

### Figma (evidence layer A — Tier 1 help center)

- Product family positioning: "Figma Design — Design and prototype in one place"; marketing use-case pages include "UI design", "UX design", "Prototyping", "Wireframing", "Graphic design" (the tool is positioned across the whole visual-design spectrum; UI design is the lead use case).
- **Design file + canvas + frames**: "Frames are layers that act as containers to organize other layers—such as shapes, images, and text—into cohesive designs… build everything from individual elements like icons or buttons, to entire website layouts and mobile app designs." Top-level frames vs nested frames; parent/child/sibling relationships; frame presets for Phone / Tablet / Desktop / Presentation / Watch / Paper / Social Media.
- **Frame-gated features**: layout guides, auto layout, constraints, and prototyping all require frames — the frame is the structural hinge of the object model.
- **Layers & editing**: layer types, vector networks, shape builder, text/typography with text styles, fills/strokes/effects/blend modes, grouping, masking, boolean operations (shape builder), bulk editing.
- **Auto layout**: "dynamic frames that respond to their contents"; documented "with CSS Flexbox in mind" — layout machinery explicitly modeled on implementation concepts.
- **Components**: "elements you can reuse across your designs… A main component defines the properties… an instance is a copy… linked to the main component and receives any updates." Variants, component properties, overrides, swap, detach; organization by naming.
- **Design-system layer**: styles (color/text/effect/layout-guide), variables (collections and modes), libraries published from a file and consumed across files; "Review and accept library updates" flow; UI kits (e.g., Apple's UI kit) consumable as libraries.
- **Prototyping**: connections between frames, triggers, flows, overlays, smart animate, variables in prototypes, device settings, present mode — a full prototyping capability embedded in the same file.
- **Dev Mode**: separate surface — "Translate designs into code": inspecting, measurements/annotations, code snippets, Code Connect, dev resources linked to layers, "ready for dev" statuses, focus view; VS Code extension.
- **Collaboration**: comments (canvas-pinned), cursor chat, spotlight, multiplayer editing, branching and merging, viewer history.
- **Interchange**: import Sketch files, copy assets between design tools, export static designs; plugin ecosystem; AI features (Figma agent in design files); sibling products (FigJam whiteboard, Slides, Sites beta, Buzz beta, Make prompt-to-code, Draw, Motion) — suite posture.

### Sketch (evidence layer A — Tier 1 documentation)

- Product nav: Design / Collaboration / Prototyping / Developer Handoff / AI — the four-pole structure of a UI design tool with embedded prototyping and handoff.
- **Frames**: "If you're designing screens for a mobile app, pages of a website, or putting together a UI, you'll want to use Frames to organize your work. Frames are a container for interface design and other layout work. They can hold both an entire design and individual parts of it." Templates with device presets; clip content; nesting; frames define the coordinate space for their contents; rulers re-origin to the closest frame.
- **Layers & editing**: layer basics, vector editing, shapes, graphics, images, text, data (dynamic content), color profiles; styling (fills, borders, shadows, inner shadows, effects, tints); grouping, masks; boolean ops implied by vector editing docs.
- **Sizing & layout**: Fixed / Relative / Fit / Fill sizing; **pins** (per-edge pinning with auto-pin); **Stack Layout** (flexible layout machinery; Smart Layout marked legacy). Resizing respects pins; edit mode to resize without contents.
- **Symbols**: "save and reuse common elements across your designs… changes to a Symbol appear everywhere you use it." Source + instances; overrides (colors, nested symbols, text/styles, images); nested symbols; swap; detach; Symbols page; Components View; symbol groups via `Group/Name` convention.
- **Styles & Libraries**: layer/text styles; Libraries shared across documents (Workspace); frame templates shareable via libraries.
- **Prototyping**: hotspots, links between frames (documented under Prototyping; overrides can retarget hotspots).
- **Developer handoff**: "browser-based handoff tools, any developer can grab the information they need for any part of a design, at any time… invite developers to inspect designs… they won't even need the Mac app"; inspect permissions; previews with inspecting enabled.
- **Collaboration**: Workspace documents, share links, comments, viewing in browser; Mac app is the editor substrate (native); View & Mirror iOS app; MCP server for AI clients.

### Penpot (evidence layer A — Tier 1 user guide)

- Positioning: "Full-Stack Design"; product pillars Design / Code / Collaboration / Integrations & API / Self-host; open source (GitHub), self-hostable.
- **Boards** (the frame equivalent): "layers that serve as your high-level containers for content organization and layout. Boards are useful if you want to design for a specific screen or print size… First level boards are shown by default at the View mode, acting as screens of a design or pages of a document." Board presets with common device/print resolutions; nesting; clip content; per-board guides; "show in View mode" toggle (first-level boards default on, nested default off); copy link to board; set as thumbnail.
- **Layers**: boards, rectangles, ellipses, text, curves (freehand), paths (bézier), images; layer actions (create/duplicate/move/select/hide/lock/group/mask/resize/scale/rotate/flip/align/distribute/boolean); styling (radius, shadows, blur incl. background blur, opacity, blend modes); copy/paste properties.
- **Constraints**: horizontal/vertical constraint map (left/right/center/scale etc.) governing behavior when the parent container resizes.
- **Flexible layouts**: dedicated section — "Create designs that adapt automatically" (auto-layout-class machinery).
- **Design systems**: Components ("speed your design workflow with reusable components"), Variants ("group components into a single, customizable one"), Design Tokens ("synchronize visual elements across your designs"), Libraries ("organize and manage your stored elements").
- **Prototyping & testing**: "Build interactive prototypes to mimic your product behaviour"; View mode presents first-level boards as screens.
- **Dev tools**: "Inspect design — Get production-ready code."
- **Export & Import**: interchange section; SVG-native heritage (renderer notes reference SVG export path).

### Balsamiq (evidence layer A for help pages, A/Tier-2 for product pages)

- **Self-label (Tier 1)**: "Balsamiq is a **user interface design tool** for creating wireframes (sometimes called mockups or low-fidelity prototypes). You can use it to generate digital sketches of your idea or concept for an application or website, and to facilitate discussion and understanding **before any code is written**. The completed wireframes can be used for user testing, clarifying your vision, getting feedback from stakeholders, or getting approval to start development."
- **Container grammar (Tier 1)**: Space → Project (single .bmpr file) → Board ("a canvas upon which you put your wireframes, prototypes, reference images, annotations and comments") → Wireframe ("a rough schematic created in the early stages of digital product design to help visualize and communicate the structure of a feature, product or website").
- **Editing model (Tier 2)**: drag from a **component library** of UI controls, or describe a screen to Balsamiq AI / drop in a screenshot → "an editable, intentionally low-fi wireframe"; edit by prompt or by hand; intentionally sketchy rendering "so the team debates the idea, not the pixels."
- **Prototype generation**: "Select your screens and generate a clickable prototype" from the same board — prototyping as a one-click derivative of the wireframe board, not the center.
- **Handoff**: share links, comments/reactions on the board, embed in Jira/Confluence/Notion, export PNG/PDF, MCP server to AI coding tools ("generate production code" from the validated design).
- **Positioning (Tier 2)**: "Figma is for polished UI. Miro is a blank canvas… Balsamiq is built for the part of the process where you're still figuring out what to build: fast, low-fi wireframes and clickable prototypes, on purpose." Audience: "built for product people, not designers" (PMs, founders, BAs, IT).
- **No evidence found of**: instance/override component machinery, constraint/auto-layout machinery, design tokens, inspect/code-export surface. (Absence claims are bounded by the 403 on the UI-library docs page; asserted as "not surfaced in the researched documentation", not as absolute product facts.)

## Cross-product Comparison

| Dimension | Figma | Sketch | Penpot | Balsamiq | Assessment |
|---|---|---|---|---|---|
| Screen container as unit of design | Frames (+ device presets) | Frames ("container for interface design", templates) | Boards ("design for a specific screen… acting as screens") | Wireframes on a Board (canvas) | **All 4 — definitional candidate** |
| Editable layered composition | Layers panel, vector/text/image layers, styling | Layer List, vector/text/image layers, styling | Layers panel, shapes/text/paths/images, styling | Editable wireframe elements on canvas | **All 4 — definitional candidate** |
| Design → implementation posture | Dev Mode "translate designs into code" | Developer Handoff "from design to code" | Dev tools "get production-ready code" | "before any code is written… approval to start development" | **All 4 — definitional candidate** |
| Reusable components (source/instance/override) | Components, variants, properties | Symbols, overrides, nested symbols | Components, variants | Component library (drag-in; simpler model) | 3/4 full instance machinery; 4/4 some reuse → common-mature, not definitional |
| Layout machinery (constraints/auto-layout) | Constraints + auto layout (Flexbox-modeled) | Pins + Stack Layout | Constraints + flexible layouts | none surfaced | 3/4 → common-mature, not definitional |
| Design-system assets (styles/tokens/libraries) | Styles, variables, published libraries | Styles, Libraries | Styles, tokens, libraries | none surfaced | 3/4 → common-mature / variant |
| Prototyping embedded | Full prototyping in-file | Hotspot prototyping | Prototyping + View mode | One-click prototype generation | 4/4 embedded, but removable (historical poles lacked it) → common-mature, capability-embedded |
| Developer handoff/inspect surface | Dev Mode (dedicated surface) | Browser inspect (free for devs) | Inspect (dev tools) | Export/embed/MCP handoff | 4/4 → common-mature |
| Real-time collaboration | Multiplayer, comments, branching | Workspace docs, comments | Real-time, comments | Real-time, comments/reactions | 4/4 current; single-user eras existed → common-mature, not definitional |
| AI assist | Figma agent, AI features | MCP server / AI connect | MCP server | Balsamiq AI drafting | 4/4 current; era-dependent → variant/optional |
| Editor substrate | Browser | Native Mac app (+ browser viewing) | Browser (self-host or SaaS) | Browser (+ desktop + Atlassian editions) | implementation variant |
| Fidelity posture | Polished, production-grade | Polished | Polished | Intentionally low-fi | variant axis |
| Audience center | Product/UI designers → whole org | Professional designers | Designers + developers (open-source) | Product people / non-designers | variant axis |

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures. Removing any one collapses the Type:

1. **The screen frame as the unit of design.** A persistent, individually addressable, bounded container — frame (Figma/Sketch), board (Penpot), wireframe-on-board (Balsamiq) — representing one screen (or screen-region/component) of a digital product's interface, held in a navigable collection (canvas/pages/file). All four products name it as the thing you design "for a specific screen", "screens for a mobile app, pages of a website", "entire website layouts and mobile app designs". Remove → generic vector editor or graphic-design application (no screen semantics).
2. **Editable layered UI composition inside the frame.** The frame's content is composed from directly manipulable, re-editable design objects (shapes, text, images, UI controls) with layer structure and styling; the artifact stays a live editable design, never a flattened picture. All four document layer/element editing as the primary activity. Remove → static mockup image / screenshot / one-shot generated image.
3. **The design-of-record posture toward implementation.** The screens are the design of an interface that will be built elsewhere in code — a specification artifact, not the working interface. All four stake identity on this seam: "translate designs into code" (Figma), "from design to code" (Sketch), "production-ready code" (Penpot), "before any code is written… approval to start development" (Balsamiq). Remove → the artifact becomes working software (website builder / no-code builder territory) or non-implementation art (graphic design).

Jointly-held load-bearing checks: (1) alone = vector/graphic editor; (2) without (1) = image editor or mockup-image tool; (3) without (1)+(2) = spec document; (1)+(2) without (3) = working-product builder (website builder) or pure illustration.

### L1 — Common Mature Structure

Present in most mature modern products; not required to recognize the Type:

- Reusable component machinery: source/main + instances, overrides, variants, swapping, detaching (full form in Figma/Sketch/Penpot; simpler library-drag form in Balsamiq).
- Layout machinery: constraints/pins and auto-layout/stack/flexible-layout systems (3/4 sampled; explicitly modeled on implementation concepts like Flexbox).
- Design-system assets: styles, variables/tokens, shared libraries with publish/update-accept flows.
- Embedded prototyping capability (connections/triggers between frames; present 4/4, but historically absent poles remain in-type).
- Developer handoff/inspect surface (dedicated dev mode, browser inspect, code snippets/production-ready code view).
- Comments, sharing links, review flows; real-time multi-user editing in current products.
- Import/export interchange (e.g., Sketch-file import in Figma; SVG/PNG/PDF exports; asset export).
- UI kits / starter templates / component libraries to start from.

### L2 — Variant / Optional Structure

- Fidelity posture: polished high-fidelity vs intentionally low-fidelity wireframing.
- Editor substrate: browser vs native desktop; SaaS vs self-hosted open source.
- Collaboration depth: single-user local files (historical/minimal poles) ↔ real-time multiplayer with branching.
- AI posture: assistive generation/editing inside the editor; MCP/AI-client integration; prompt-to-design drafting.
- Audience breadth: professional designers ↔ non-designer product people.
- Suite posture: standalone editor ↔ multi-product suite (whiteboard/slides/sites/prompt-to-code siblings).
- Handoff depth: static specs/exports ↔ code snippets, code connect, ready-for-dev statuses, MCP-to-code.

### L3 — Vendor-specific Structure (research notes only)

- Figma: Dev Mode ready-for-dev statuses and focus view; Code Connect; variables with modes; branching/merging; slots; Figma agent; default 100×100 first-frame size; sibling products (FigJam, Slides, Sites, Buzz, Make, Draw, Motion).
- Sketch: Mac-app-only editing substrate; Workspace documents; View & Mirror iOS app; Command Bar; Components View; frame templates with `Previews/` naming convention; data (dynamic content); `Group/Name` symbol-organization convention.
- Penpot: open-source governance and self-hosting; SVG-native rendering heritage; background blur's WebGL-renderer dependency and export limitation; "Full-Stack Design" framing; board "show in View mode" defaults.
- Balsamiq: intentionally sketchy control rendering; Space/Project/Board/Wireframe grammar with .bmpr files; Confluence/Jira/Desktop editions; "0 day learning curve" positioning; reviewers-free pricing posture.

## Rejected Findings

- **"A UI design application must be cloud-based / collaborative"** — rejected: Sketch's editor is a native Mac app; Balsamiq ships a desktop edition; early-generation tools were single-user local files. Collaboration is common-mature, not definitional.
- **"A UI design application must have components/symbols"** — rejected as definitional: Balsamiq's documented model is a drag-from-library flow without instance/override machinery, and the Type is recognizable without any reuse machinery (one-off screens). Reuse is the strongest common-mature structure, not the invariant.
- **"A UI design application must have auto-layout/responsive constraints"** — rejected: absent from the low-fi pole's surfaced documentation; 3/4 sample. Common-mature.
- **"UI design = prototyping"** — rejected: all four embed prototyping, but the interactive-prototype-builder pass's removal test holds from this side too — strip prototyping and the product is still a UI design tool (historical poles: early Sketch, the Fireworks generation). Prototyping is capability-embedded packaging.
- **"Wireframing tools are a different Type from UI design tools"** — rejected at the population level: Balsamiq's own help center self-labels it "a user interface design tool for creating wireframes". Low-fidelity wireframing is a fidelity/phase pole inside this population. (Whether the directory's separate UX Prototyping leaf should claim the process-oriented center remains open — see Boundary Findings.)
- **"UI design tools are just vector editors with presets"** — rejected: the screen-frame structure, UI reuse machinery, and implementation posture are absent from generic vector editors; the vector substrate is an implementation choice, not the identity.

## Boundary Findings

1. **vs Interactive Prototype Builder — RATIFIED from this side.** Center of gravity: composing the static visual design of screens (this Type) vs making screens behave through trigger→response interactions and a run mode (that Type). All four sampled products embed prototyping as a capability of the same file — capability-embedded packaging, exactly as the prototype-builder pass recorded. Removal tests agree from both directions: strip interactions + run mode from a prototype builder → UI design tool; strip prototyping from a UI design tool → still a UI design tool. Keep both Types; merged products are one market, two centers of gravity.
2. **vs Collaborative Design Platform — RATIFIED keep-both, different defining axes.** The collaborative-design-platform pass's working distinction is confirmed from this side: that Type is defined by its collaboration structure (shared multi-user design files, subject-agnostic); this Type is defined by its target artifact (user-interface screens). Evidence: single-user/local UI design tools (Balsamiq desktop edition; the early-Sketch generation) are fully in-type here without any shared-multi-user file; conversely a collaborative design file holding a poster or social graphic is not doing UI design. The flagship straddle (one product archetype of both) is market position, not Type identity. Keep both; the joint review is discharged from this side.
3. **vs AI Design Generator — RATIFIED from this side.** Defining act: human-directed composition (this Type) vs generation-first production of designs from prompts (that Type). UI design tools absorb AI as assist (drafting, editing by prompt, agents) without changing Type — Figma agent and Balsamiq AI both documented as accelerators inside a manual-composition editor. Uizard-class generation-first products remain on the AI-generator side per that pass; the overlap (editable multi-screen output) is capability convergence. Joint review discharged from this side.
4. **vs UX Prototyping Application — OPEN; partially discharged.** The sibling leaf is unprocessed. From this side: the low-fidelity/early-phase pole (Balsamiq-class) is inside the UI-design-tool population by self-label, while its positioning ("the part of the process where you're still figuring out what to build") is process-oriented. Working seam held for the next pass: UI Design Application centers the screen-design artifact itself (at any fidelity); UX Prototyping Application (hypothesis) centers the prototyping/validation process (wireframes, flows, concept tests). Final ratification belongs to the ux-prototyping-application pass; recorded in STATUS.md.
5. **vs Graphic Design Application** — target artifact: user-interface screens vs general visual deliverables. Confirms the graphic-design pass's conceptual seam; the same editor substrate (layers, vector tools) serves both, the artifact and its UI-specific machinery differ.
6. **vs Vector Graphics Editor** — substrate overlap (both vector-based) but no screen frames, no UI component/instance semantics, no handoff posture in a vector editor; conversely UI tools' defining structures (frames-as-screens, constraints, dev inspect) are absent there. Distinct Types.
7. **vs Visual Website Builder / No-code Application Builder** — the design-artifact posture is the seam: the UI design is an inert specification implemented elsewhere; a website builder's artifact is the working site. Removal test: connect the artifact to a real backend and deploy → left this Type. (Same test direction the prototype-builder pass used against no-code.)
8. **vs Industrial Design Application** — different design domain (digital interfaces vs physical product form); confirms that pass's note; only vocabulary overlap.
9. **vs Digital Whiteboard / Collaborative Canvas** — free-form ideation surface vs structured screen frames with UI semantics; whiteboards lack the frame/component/handoff structure.

## Historical / Market-Sample Check

- **Adobe Fireworks generation (2000s–2013)** — pages as screens, states, symbols, vector+bitmap hybrid editing, built for web/app screen design: satisfies all three L0 legs without cloud, multiplayer, auto-layout, or tokens. ✓ (market-structure strength; not live-re-verified)
- **Early Sketch (2010s, single-user Mac)** — artboards + symbols + styles, no cloud/collaboration/prototyping in early versions: satisfies L0. ✓ (the current docs still describe the same core; the single-user era is market-structure knowledge)
- **Photoshop/Illustrator comp era** — generic layer editors used for UI comps: no screen-frame semantics (no artboards/pages), no UI reuse machinery; held as **conceptual lineage / practice**, not the dedicated Application Type. The dedicated Type crystallized with the screen-frame + UI-reuse generation (Fireworks/Sketch-class). This parallels how other passes treated paper-era lineage.
- **Balsamiq (2008→)** — low-fi pole, desktop and cloud editions across its history: satisfies L0 at every era. ✓
- Conclusion: the three-leg definition holds across eras, substrates, fidelity poles, and business models. Nothing era-specific (cloud, multiplayer, AI, auto-layout, tokens) is in the defining core.

## Uncertainties

- Balsamiq's component-library internals (whether any instance/override semantics exist) could not be verified — the UI-library docs page returned 403. Claims about Balsamiq are bounded to "not surfaced in the researched documentation".
- Penpot's flexible-layout and token machinery was evidenced at section-description level (section titles + one-line descriptions), not per-feature article level; mechanics asserted only at capability level.
- Historical samples (Fireworks, early Sketch, Photoshop-comp era) were not re-verified from live sources; used only for qualitative era-checks at market-structure strength.
- The UX Prototyping Application seam is this pass's hypothesis, not a ratified market split; the joint review remains open.
- The proportion of real-world UI design work done in general-purpose tools vs dedicated UI tools is not measurable from documentation; no claim made.

## Final Synthesis

A UI Design Application is the screen-design editor of digital product development. Its world is organized around one authoritative artifact — the interface design file — whose unit of design is the screen frame: a persistent, addressable, bounded container representing one screen (or screen-region) of an app or website, composed from editable layered objects, and destined for implementation in code by someone else. Around that three-part spine, mature products converge on a standard structure: reusable components with source/instance/override semantics and variants; layout machinery (constraints, auto-layout-class systems) that lets compositions respond to resizing; design-system assets (styles, tokens, shared libraries); an embedded prototyping capability; a developer handoff/inspect surface; comments and sharing; and interchange (import/export, UI kits). Products differentiate along fidelity posture (polished ↔ intentionally low-fi), substrate (browser ↔ native; SaaS ↔ self-hosted open source), audience (designers ↔ non-designer product people), collaboration depth, AI posture, and suite scope. The Type is defined by the artifact and its posture, not by any packaging: prototyping, collaboration, and AI are capabilities a UI design tool carries, not what makes it one.
