# Research Notes — Diagramming Application

## Research Goal

Understand what a Diagramming Application really is from real products: its core objects (shape, connector, page, document, shape library), its defining behavior (connector attachment/routing), its typical workflows (authoring, data-driven generation, export/publish), and — critically — its boundary against Digital Whiteboard / Collaborative Canvas (a pending boundary note from the collaborative-canvas pass asked this leaf to re-confirm the board-vs-diagram seam using the vendors' own taxonomy).

## Initial Boundary

Working hypothesis before research:

- Core: structured visual diagrams built from semantic shapes joined by connectors that stay attached — flowcharts, org charts, network diagrams, UML, ERDs, BPMN, floor plans.
- Users: engineers, IT/ops, business analysts, product managers, consultants, educators.
- Nearest neighbors: Digital Whiteboard / Collaborative Canvas (freeform facilitation surfaces), Vector Graphics Editor (artistic paths), Data Visualization Application (data-rendered charts), Software Architecture Modeling / Database Schema Design Tool (domain-specific with semantics beyond drawing), Presentation Application (slides).
- Known open question from research/collaborative-canvas.md: vendors' own migration tooling separates "diagrams" (Lucidchart, draw.io) from "boards" (Mural, FigJam, Jamboard, Conceptboard) — re-confirm with this leaf's own evidence.
- Unknowns: how far connector semantics go (fixed vs floating points, routing), whether data-linked diagrams are definitional or optional, whether real-time collaboration is definitional (historical check: Visio/draw.io heritage says no).

## Research Questions

1. What are the core objects? (shape, connector, page, document, shape library/stencil, layer, container)
2. What exactly do connectors do? (attachment points, glue, routing, re-route on move, labels, endpoints)
3. What is the typical authoring workflow end to end?
4. What notation/shape vocabulary do products supply? How broad?
5. How does data-linked / generated diagramming work, and is it definitional?
6. What collaboration surfaces exist, and are they definitional?
7. What are the import/export/publish paths? (Visio interop as lingua franca?)
8. Where is the boundary vs whiteboard/canvas products — per the vendors' own classification?
9. Historical check: do older, desktop, file-based, non-collaborative products still fit the definition?
10. What interfaces does a user actually face?

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| Lucidchart | Web-native commercial leader; deep help center | Commercial SaaS, individual→enterprise |
| draw.io / diagrams.net | Free, open-source, file-based, no-account | Free/open-source, privacy-first, bring-your-own storage |
| Microsoft Visio | Historical anchor of the category (1990s desktop), stencil/template model | Desktop+web enterprise, Microsoft 365 ecosystem |
| SmartDraw | Template-driven, Windows heritage, diagrams-from-data | Mid-market/enterprise site license |
| Miro | Boundary probe only — whiteboard family with diagramming capability | Whiteboard/canvas family (not counted as a representative of this Type) |

## Sources

All fetched 2026-09-07. Tier 1 (official operational documentation) unless noted.

- Lucid Help Center — https://help.lucid.co/hc/en-us (root)
- Lucid Help Center — Lucidchart category — https://help.lucid.co/hc/en-us/categories/14652087316628
- Lucid — Welcome to Lucidchart — https://help.lucid.co/hc/en-us/articles/11970952773652
- Lucid — Add and style lines in Lucidchart — https://help.lucid.co/hc/en-us/articles/16157138194836
- Lucid — Shape libraries in Lucidchart — https://help.lucid.co/hc/en-us/articles/14931750819476
- Lucid — Link data to a Lucidchart document — https://help.lucid.co/hc/en-us/articles/16493391394068
- draw.io — https://www.drawio.com/ (product root; lucidchart.com root returned 403, draw.io root used instead)
- draw.io — Using draw.io (manual intro) — https://www.drawio.com/docs/manual/
- draw.io — Work with connectors — https://www.drawio.com/docs/manual/connectors/
- draw.io — Example technical diagrams (types) — https://www.drawio.com/docs/diagram-types/
- Microsoft Support — Visio help & learning — https://support.microsoft.com/en-us/visio
- Microsoft Support — Beginner tutorial for Visio — https://support.microsoft.com/en-us/visio/beginner-tutorial-for-visio
- SmartDraw Knowledge Base — https://www.smartdraw.com/support/
- Miro Help Center — https://help.miro.com/hc/en-us (boundary probe only)

Fetch failures (per network rules, abandoned after retry): https://www.lucidchart.com/ (403, retried via help center — succeeded); https://www.drawio.com/doc/ and /doc/getting-started/ (404, retried via /docs/ — succeeded); a specific Miro diagramming article URL (404, retried via help center root — succeeded).

## Product Observations

### Lucidchart (Lucid) — evidence layer A (directly observed)

Positioning: "a visual workspace for diagramming, data visualization, and collaboration." The vendor's own help center separates **Lucidchart ("build intelligent diagrams")** from **Lucidspark ("collaborate in a virtual whiteboard")** — two products, two families.

Document/workspace structure (Welcome article):
- Home page: documents, folders, templates, import (Visio, Gliffy, Draw.io, OmniGraffle files).
- Workspace: header (title, revision history, collaborator colors, comments, presentation builder, Loom video recording, share), More menu (Edit in Lucidspark via "universal canvas", export, publish as URL/PDF/image, page settings, compare documents, document status, find & replace, select all lines/shapes by property, insert images/gifs/templates/document info, arrange/align/distribute/group, publish/embed).
- Formatting bar: paint format, text, shape/line formatting, link-to (URL/page/document), actions, **magnetize** (shapes to containers/swimlanes), lock, contextual panel.
- Primary toolbar: Lucid AI (generate/summarize/sort diagrams), template gallery, shapes panel (default Standard/Flowchart/Basic; "More shapes" library manager), containers, styles, conditional formatting, images panel, data linking panel (Enterprise), visual activities, **diagram-as-code (Mermaid)**, quick tools, integrations.
- Footer: page list, page menu (rename/duplicate/delete/move/color/**convert to master page**/new document from page), add page, layers, page insights (formulas), undo/redo, zoom/minimap, fullscreen.
- FAQ: **freehand drawing is NOT in Lucidchart — it is a Lucidspark feature.** Direct vendor-drawn boundary between diagramming and whiteboarding.

Lines/connectors (lines article):
- "Lines are essential to diagramming."
- Four ways to add: drag from a shape's node; quick-add line+shape from a preview node; drag a line shape from the Shape menu; right-click → Draw Line.
- **Connection maintenance: "If you move an object that is connected with a line to another object, the line will also move to maintain the connection."**
- Line connections can be toggled off in document settings (lines then move independently; previously connected lines stay connected).
- Line shapes: straight, curved, elbow (default; 90° bends following the canvas grid), two-way.
- Styling: color, width, dash patterns (custom dash/gap), DOUBLE (parallel lines), JUMP (line hops at crossings), TEXT PILL, MARKER (labelled circle mid-line); endpoint styles (arrows etc.), endpoint swap; ERD/UML-specific endpoint styles referenced.
- Text on lines (double-click), movable along the line.
- Path editing: anchor points/joints, remove joint, reset line.
- **Smart lines**: "automatically adjust their connection points to form the most efficient path between two objects."
- Conditional formatting can color lines by data values.

Shape libraries (shape libraries article):
- Pre-made libraries + custom libraries built from imported images, SVG files, and Visio stencils (.vss/.vssx/.vsx).
- Default libraries: Standard, Flowchart, Containers, Shapes. "Shapes in use" auto-section (shapes currently on canvas); "My saved shapes" fixed section.
- Favorite/reorder/hide libraries; pin to share with collaborators.
- Custom library sharing with permissions (can use / can edit / can edit and share) on Team/Enterprise.
- Search across shapes/images (Bing)/icons (Iconfinder)/GIFs (Giphy); import PDF/PNG/JPEG/GIF onto canvas.
- Templates auto-enable their libraries (e.g., ERD template enables the ER library).
- Some libraries plan-gated (mind maps, UI mockups, wireframes on paid plans).
- Video embed shape (YouTube/Vimeo) playable in presentation mode.

Data linking (data article):
- Import datasets from Google Sheets, Excel, CSV (Enterprise-only feature; FedRAMP: Excel/CSV only).
- Header row + reference key column (unique identifiers) chosen at import.
- Refresh: automatic (Google, ~30s), manual, never; Excel sync modes: two-way / pull / manual (two-way needs Team/Enterprise + integration).
- Assign data by dragging a cell/row onto a shape, a group, or the page; drag onto empty canvas to create a new linked shape.
- Display data as text on shapes; pull fill color from Google Sheets cells; custom data fields without a dataset.
- Data-linked documents include ERDs, org charts, Smart Containers, account maps; sources include BambooHR, AWS, SQL, Salesforce.
- Privacy note: viewers of a data-linked document see the full dataset even in view-only mode.
- One-time data imports (org charts, ERDs, mind maps) available on Free/Individual/Team; **data refresh is Enterprise-only**.

### draw.io / diagrams.net (draw.io Ltd / JGraph) — evidence layer A

Positioning: "Security-first diagramming for teams"; free forever, no sign-up, open source (Apache 2.0), bring-your-own storage (Google Drive, SharePoint/OneDrive, Confluence/Jira, GitHub, VS Code, Notion, device), desktop app, real-time collaboration with shared cursors, export SVG/PNG/PDF/HTML/URL, embeddable viewer.

Manual structure (docs/manual):
- Create/open diagram; **choose storage location** (a first-class decision); editor; shapes (quick-add, move/resize/rotate); connectors; text; styles; insert elements; **apply layouts** (flows, trees, organic, circular); import; export/publish; concurrent editing; layers; **multi-page diagrams**; links/tooltips/tags; **generate a diagram** (AI from text description, Mermaid code, SQL, CSV spreadsheet); templates; advanced (custom shape libraries, custom connection points, custom template libraries, keyboard shortcuts, embedding).
- Freehand drawing and scratchpad exist as auxiliary tools.
- Self-hosting (Docker) and offline desktop documented under security.

Connectors (connectors article):
- "Connectors are lines that connect your shapes together... In a diagram, connectors provide context information, showing how the various shapes and entities in your diagram are related. Connectors are used to group related information and systems, show flow of information and control, and specify the complex relationships between functions and systems in UML diagrams." Also: "Connectors are also known as lines or edges."
- **Floating connectors** ("move around the perimeter of the shape, taking the shortest route between the source and target shape") vs **fixed connectors** ("stay attached to fixed points on your shape"); can mix per end; Alt-drag to fix to any position; snap-to-point option; custom connection points per shape.
- Draw from directional arrows; clone-and-connect; drag a shape onto an arrow to connect.
- **Waypoints** as route anchors (drag sections to re-route; added/removed automatically); reverse/flip connector (labels swap); join two connectors with a waypoint shape (circuit diagrams).
- **Three labels per connector** (middle + both ends); labels move with the connector; draggable.
- Z-order front/behind shapes.
- Style: color/opacity/width/pattern, animated flow, bends sharp/rounded/curved, routing styles, arrowheads/technical symbols, endpoints outside/inside shape border, **line jumps** at overlaps, sketched/rough style.
- Related: Crow's foot notation for ERDs; UML class-diagram arrow symbols.

Diagram types (types page): UML (use case, class, sequence, component, composite structure, deployment, activity, state machine, communication, package, profile, timing), C4, BPMN 2.0 (orchestration/choreography), AWS/Azure/GCP/IBM/Veeam/Citrix/Salesforce/SAP architecture, network infrastructure, rack diagrams, floorplans, ER models, cross-functional/swimlane flowcharts, data flow diagrams, dependency graphs, gitflow, kanban boards, Ishikawa, PERT/Gantt, timelines/roadmaps, mindmaps/concept maps, Venn, Sankey, circuit/logic diagrams, threat modelling, org charts (incl. generated from CSV), story mapping, infographics, science illustrations.

### Microsoft Visio — evidence layer A

Positioning (beginner tutorial): "Visio lets you transform complicated text and tables that are hard to understand into visual diagrams that communicate information at a glance... organization charts, network diagrams, workflows, and home or office plans." Three basic steps: **choose a template → arrange and connect shapes → add text**.

Templates: "Templates include stencils, shapes, and grid measurements." Home Plan template ships wall/furniture/appliance stencils; Organization Chart template ships distinct shapes for executives, managers, assistants, positions, consultants, vacancies; Site Plan opens with an engineering scale (1 inch = 10 feet); some templates add special ribbon tabs (Office Layout → Plan tab) or wizards (Space Plan).

**Master/instance model**: "When you drag a shape from the Shapes window onto your drawing page, the original shape remains on the stencil. That original is called a *master shape*. The shape that you put on your drawing is a copy — also called an *instance*." Drag as many instances as wanted.

Connection: AutoConnect arrows on hover; Quick Shapes mini toolbar (top four shapes); drag arrow to a target shape; drag a new shape from the Shapes window onto an arrow to connect automatically. **Org chart auto-structure: "Drag each person's shape to the chart and drop it on top of their manager's shape. The shapes automatically connect to show the hierarchy."**

Shape data: Shape Data window per shape; "data-connected Visio diagrams that display data, are easy to refresh"; Visio Professional imports external data; **data graphics** display shape data visually on many shapes at once.

Special shape behavior: yellow control handles (stretch a People shape to show more people); right-click shortcut commands.

Finish: themes, backgrounds (background pages, VBackground-1), borders & titles, print scaling, present to audience, **Visio visuals in Power BI**, **Data Visualizer** (Excel data → process diagram), import data to shapes, org chart from worksheet data.

Licensing: Visio Plan 1 (web only) / Plan 2 (desktop + web); Professional/Standard perpetual versions.

### SmartDraw — evidence layer A (knowledge-base structure) / B

Knowledge base categories: FAQ, My Account, Videos, Templates & Documents, The Basics, **How to Draw Anything** (every diagram type + whiteboard visuals), **SmartDraw AI** (generate diagrams from natural-language prompts), Collaboration (share documents, create whiteboards), Integrations, **Diagrams from Data** ("Generate Automatic Diagrams from Data"), Printing, Reference.

Product/solution pages: Flowchart Maker, Floor Plan Creator, Organizational Chart Maker, "AutoCAD Alternative"; solutions span Diagramming, Whiteboarding, Data Visualization, Process Improvement, Organizational Design, IT Infrastructure, Technical Diagramming, Agile, Floor Planning. Enterprise site licensing, SOC2 Type II, "control your data" posture.

Observation: SmartDraw is template-first (start from a diagram type) and treats whiteboarding as a separate solution — another vendor-internal separation of the two families.

### Miro (boundary probe only — NOT a representative of this Type) — evidence layer A

Help center root is entirely **board**-centric: "restore a deleted board", "move boards", "add content to my board", board performance, board trash/restore. No diagram-document concept appears at the root level. Combined with the collaborative-canvas research (Miro's own migration titles: "Import Lucidchart diagrams" / "Import Draw.io diagrams" vs "Import Mural boards" / "Import FigJam boards"), Miro belongs to the whiteboard/canvas family; diagramming there is a capability (shape packs), not the organizing object model.

## Cross-product Comparison

| Structure / behavior | Lucidchart | draw.io | Visio | SmartDraw | Evidence |
|---|---|---|---|---|---|
| Persistent diagram document (multi-page) | document + pages | diagram file + pages | drawing + pages | document | A×4 |
| Shapes as discrete semantic objects placed on canvas | ✓ | ✓ | ✓ (master/instance) | ✓ | A×4 |
| Connectors attach to shapes and maintain connection on move | ✓ (explicit doc) | ✓ (floating/fixed, shortest route) | ✓ (AutoConnect; org-chart drop-on-manager) | ✓ (implied by product docs) | A×3 + B |
| Connector routing behavior (elbow/straight/curved, waypoints, line jumps) | ✓ (elbow default, smart lines, JUMP) | ✓ (waypoints, bends, jumps) | ✓ (AutoConnect/routing) | ✓ | A×4 |
| Connector labels (mid + ends) | ✓ (text on line, movable) | ✓ (three labels) | ✓ (text block on connector) | ✓ | A×3 + B |
| Application-supplied shape vocabulary (libraries/stencils) | ✓ (libraries, custom, Visio stencil import) | ✓ (libraries, custom, public) | ✓ (stencils, masters) | ✓ (symbols/templates) | A×4 |
| Templates per diagram type | ✓ (template gallery) | ✓ (template library) | ✓ (template = stencil + grid + scale + wizards) | ✓ (template-first) | A×4 |
| Notation breadth (flowchart, org, UML, ER, BPMN, network, cloud, floor plans…) | ✓ | ✓ (documented list) | ✓ | ✓ | A×4 |
| Containers/swimlanes | ✓ (containers, magnetize) | ✓ (tables, swimlane shapes) | ✓ (cross-functional templates) | ✓ | A×4 |
| Auto-layout / arrangement | ✓ (align/distribute; AI sort) | ✓ (layout engine: flows/trees/organic/circular) | ✓ (org chart auto-structure) | ✓ | A×4 |
| Layers | ✓ | ✓ | ✓ (background pages adjacent) | ✓ | A×3 + B |
| Export PNG/SVG/PDF (+ publish/embed) | ✓ (URL/PDF/image, embed) | ✓ (PNG/SVG/PDF/HTML/URL, viewer embed) | ✓ (print, Power BI, share) | ✓ | A×4 |
| Import from other diagramming tools (Visio interop) | ✓ (Visio/Gliffy/draw.io/OmniGraffle) | ✓ (import formats incl. .vsdx; Gliffy migration) | ✓ (ecosystem origin) | ✓ (Visio import claimed on product pages) | A×3 + B |
| Data-linked / generated diagrams | ✓ (Enterprise; org chart/ERD/mindmap one-time imports) | ✓ (CSV/SQL/Mermaid insert; AI generate) | ✓ (shape data, data graphics, Data Visualizer, org chart from worksheet) | ✓ (Diagrams from Data; AI) | A×4 — but plan-gated / auxiliary |
| Diagram-as-code / text-to-diagram | ✓ (Mermaid; Lucid AI) | ✓ (Mermaid/SQL/CSV/AI) | — (not observed) | ✓ (AI prompts) | A×3 |
| Real-time collaboration | ✓ | ✓ (shared cursors) | ✓ (web co-authoring; not in tutorial core) | ✓ (collaboration category) | A×4 — modern layer, not definitional |
| Comments / presentation mode | ✓ (comments, presentation builder) | — (not observed) | ✓ (present to audience) | — (not observed) | A×2 |
| Revision history | ✓ | — (file-version based) | ✓ (SharePoint/OneDrive dependent) | — | A×2 |
| Freehand drawing | ✗ (explicitly Lucidspark-only) | ✓ (auxiliary) | — | ✓ (whiteboard visuals) | A — boundary-relevant |
| Storage model | cloud (Lucid) | bring-your-own (device/Drive/OneDrive/Confluence/GitHub) + desktop | Microsoft 365 / local files | cloud + enterprise | A×3 — variant |
| Pricing posture | freemium SaaS, Enterprise tier | free, open source | subscription (Plan 1/2) + perpetual | site license | A×4 — variant |

## L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Diagramming Application:

```text
Diagram Document (persistent, page-oriented visual document)
└── Shapes — discrete semantic objects placed on the canvas
    └── Connectors — bound to shapes, maintained on move, routed as edges
        └── Application-supplied diagram shape vocabulary (stencils/libraries)
```

Four properties:

1. **Diagram document** — the diagram is a persistent, named, page-oriented document (not an ephemeral session surface). Remove it → an ephemeral sketch surface.
2. **Shapes as discrete semantic objects** — draggable, reusable, individually selectable/labelable objects (not freeform strokes). Remove it → a paint/freeform program.
3. **Connectors bound to shapes with maintained attachment and routing** — the line is a managed edge: it stays attached when shapes move and re-routes (shortest path / elbow / waypoints). Remove it → a freeform drawing surface (whiteboard/paint). This is the single most load-bearing property: Lucidchart states it verbatim; draw.io builds its connector chapter on it; Visio's AutoConnect and org-chart drop-on-manager implement it.
4. **Application-supplied diagram shape vocabulary** — the app ships notation-oriented shape sets (stencils/libraries/templates), not only generic drawing tools. Remove it → a generic shape editor, no longer a diagramming tool in the market sense.

Historical check (older / regional / platform-native products): Visio (1990s desktop, no real-time collaboration), draw.io (2005, file-based, no account), OmniGraffle, yEd — all satisfy exactly these four properties and nothing more. Real-time collaboration, cloud storage, AI, data refresh are NOT in L0. The definition survives the historical check.

Note on #4: the *user-manageable* library panel (enable/disable, custom libraries, sharing) is L1; the L0 form is only "the application supplies a diagram-oriented shape vocabulary" (even a fixed built-in set satisfies it).

## L1 — Common Mature Structure

Present in essentially all mature modern products; not definitional:

- Shape-library management (enable/disable, search, favorites, custom libraries, sharing with permissions)
- Template gallery organized by diagram type
- Text labels on shapes and connectors; rich styling (color, line style, endpoints/arrows, themes)
- Multi-page documents; layers; z-order
- Containers / swimlanes (cross-functional flowcharts) with shape-magnet behavior
- Auto-layout / arrangement (align/distribute; automatic flows/trees/organic/circular layouts)
- Grid, snapping, rulers, zoom/minimap, undo/redo
- Export (PNG/SVG/PDF), publish (URL/embed), print with scaling
- Import from other diagramming tools — Visio format as the interop lingua franca (Lucidchart imports Visio/Gliffy/draw.io/OmniGraffle; draw.io imports Visio/Gliffy; SmartDraw positions itself as a Visio alternative)
- Real-time collaboration (shared cursors), comments, presentation mode, revision history (modern web products)
- Data-linked diagrams in some form (all four sampled products have one) — but plan-gated and auxiliary; see L2

## L2 — Variant / Optional Structure

- **Data-linked diagram depth**: one-time generation (org chart from spreadsheet, ERD from schema) vs live refresh/sync (Lucidchart Enterprise-only refresh; Visio data graphics + Data Visualizer; draw.io CSV/SQL insert). Segment/plan dependent.
- **Diagram-as-code / text-to-diagram**: Mermaid, SQL, CSV, natural-language AI (draw.io, Lucidchart, SmartDraw; not observed in Visio docs).
- **Deployment/storage**: cloud SaaS vs bring-your-own storage vs desktop/offline vs self-hosted (draw.io Docker) vs embedded in host platforms (Confluence/Jira/VS Code/Google/Notion).
- **Business model**: free open-source vs freemium subscription vs perpetual license vs site license.
- **Scale drawing**: floor plans / site plans with real-world scale (Visio engineering scale, Lucidchart floor plans, SmartDraw floor plans) — a variant capability that leans toward CAD-lite.
- **Enterprise governance**: admin panels, SSO, FedRAMP environments, audit/compliance posture.
- **AI assistance**: generation from prompts, AI sorting/summarizing (era-common, product-dependent).

## L3 — Vendor-specific Structure (research notes only)

- Lucidchart: Smart Containers, Visual Activities, universal canvas (switch document to Lucidspark), Loom video recording, Page Insights formulas, magnetize toggle, conditional formatting on lines by data values, 3MB Excel/CSV dataset limit, ~30s Google refresh interval, plan tiers (Free/Individual/Team/Enterprise), custom-library permission tiers (can use / can edit / can edit and share).
- draw.io: waypoint shape (joins two connectors), sketch/rough style, scratchpad, sketch editor theme, storage-location comparison docs, viewer embed URL parameters, Apache 2.0 / "no artificial scarcity" positioning, Cloudcraft/Cloudockit export integrations.
- Visio: master shape/instance terminology, Shape Data window, data graphics, Data Visualizer, Power BI visuals, background pages (VBackground-1), yellow control handles with special shape behavior, Space Plan wizard, Plan 1 (web) vs Plan 2 (desktop+web) licensing, engineering-scale templates (1 inch = 10 feet in Site Plan).
- SmartDraw: enterprise site-license administration guide, "AutoCAD alternative" positioning, SOC2 Type II marketing.
- Miro (boundary probe): board as the only root object; apps marketplace; seats/guests billing model.

## Vendor-specific Findings

See L3. The most boundary-relevant vendor facts:

1. Lucid's own product split: Lucidchart = "intelligent diagrams" vs Lucidspark = "virtual whiteboard"; freehand drawing is explicitly a Lucidspark feature, not a Lucidchart feature.
2. Lucid's import taxonomy: Lucidchart imports *diagram files* (Visio, Gliffy, draw.io, OmniGraffle); Lucidspark imports *board files* (Miro, MURAL, FigJam). The vendor treats the two families as different file species.
3. Miro's help center is board-centric with no diagram-document concept at root level.
4. SmartDraw sells "Diagramming" and "Whiteboarding" as separate solutions.

## Boundary Findings

1. **vs Digital Whiteboard / Collaborative Canvas** (the pending re-confirmation): the boundary HOLDS, now with four independent pieces of vendor evidence:
   - Lucid ships two products (Lucidchart vs Lucidspark) and documents which features belong to which (freehand → Lucidspark only).
   - Lucid's import flow separates diagram files from board files.
   - Miro's documentation is board-centric; diagramming is a capability inside boards.
   - SmartDraw separates "Diagramming" and "Whiteboarding" solutions.
   Structural discriminator: in diagramming, the shape+connector graph with routing behavior and notation semantics IS the artifact; in whiteboards/canvases, free placement of heterogeneous content (stickies, images, frames) is the artifact and connections are auxiliary lines. Removal test: remove connector routing/notation semantics → whiteboard/canvas; impose strict node–edge structure with diagram-type semantics → diagramming application. Convergence trend to note: whiteboard products increasingly ship diagramming shape packs, and diagramming products add freeform surfaces (Lucid "universal canvas" bridges them) — the seam is blurring at the product level but the object models remain distinct.
2. **vs Vector Graphics Editor**: vector editors author artwork (bezier paths, illustration); no glue semantics, no notation vocabulary, no connector routing. Removal test: give shapes meaning and glue → diagramming; remove glue → vector editor.
3. **vs Data Visualization Application**: data viz renders charts from data automatically; diagramming is hand-authored structure where data linking is an optional layer. Removal test: remove hand-authoring of shape graphs → data visualization.
4. **vs Software Architecture Modeling / Database Schema Design Tool** (directory siblings in §12): those carry domain semantics beyond drawing (model validation, codegen, round-tripping with repositories). A diagramming application draws the notation without enforcing/deriving domain semantics. Products like draw.io draw UML/C4/ER without semantic validation — that is the seam.
5. **vs Presentation Application**: diagramming products have presentation modes, but the artifact is the diagram document, not a slide deck.
6. **vs Organization Design Platform** (per that leaf's research): "Diagramming holds shapes; an org design platform holds structured records with metrics, permissions, and lifecycle. A diagramming tool can draw an org chart but cannot answer 'what does this structure cost'."
7. **vs Architecture Design Application** (per that leaf's research): real-world scale/measure and building semantics → architecture design; diagramming is not-to-scale except the floor-plan variant.
8. **vs Mechanical CAD**: same scale/precision argument; diagramming shapes are symbolic, not manufactured geometry.

## Uncertainties

- SmartDraw's connector-level semantics were evidenced at knowledge-base structure level (categories, product pages), not per-feature article level; its connector behavior is asserted at layer B (cross-product commonality) rather than A. Its inclusion does not affect L0 (three products document connector maintenance at layer A).
- Visio's real-time co-authoring details were not fetched (tutorial focuses on authoring); collaboration is treated as a modern layer, not definitional, so this does not affect the model.
- Whether "diagram-as-code" (Mermaid/SQL) becomes a mainstream primary interface or remains an auxiliary input is unresolved; treated as L2.
- The directory's §03.05 sibling question (digital-whiteboard vs collaborative-canvas probable alias) is out of scope for this leaf; this research only confirms the diagram-vs-board seam.
- lucidchart.com marketing root was unreachable (403); Lucid positioning evidence comes from its help center (Tier 1), which is sufficient.

## Final Synthesis

A Diagramming Application is an editor whose world model is: **a persistent diagram document containing shapes drawn from an application-supplied notation vocabulary, joined by connectors that remain attached to their shapes and re-route as edges when the layout changes.** Everything else — libraries management, templates, styling, pages, layers, swimlanes, auto-layout, export/publish, Visio interop, real-time collaboration, data linking, diagram-as-code, AI — is mature structure or variant capability layered on that core. The Type's sharpest boundary is against the whiteboard/canvas family (free placement, facilitation surfaces), and the vendors themselves police that boundary in their product splits, import taxonomies, and feature assignments. The Type is historically robust: 1990s desktop stencils-and-glue products satisfy the same core as today's cloud AI products.
