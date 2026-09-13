# Research Notes — Architecture Design Application

## Research Goal

Understand, from real products, what the software category used by architects to design and document buildings actually consists of: what objects the practitioner creates, how design intent becomes drawings and models, what the documentation deliverable looks like, and where the boundary lies with neighboring Types (BIM Authoring, generic CAD, 3D modeling, engineering design tools).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: authoring a building design (geometry of spaces and enclosing elements) and producing architectural documentation (plans, sections, elevations, schedules).
- Primary users: architects; secondary: designers, builders/remodelers, interior designers.
- Nearest neighbors: **BIM Authoring** (same directory family — likely deep overlap), Mechanical CAD, 3D Modeling Application (04.13), Structural/MEP/Civil design siblings, Construction Document Management.
- Unknowns: whether BIM is part of the definition or a modern posture; whether drawing-first tools still fit; whether "Architecture Design Application" is actually an alias of "BIM Authoring" in the current market.

## Research Questions

1. What is the central persistent artifact — drawing set, 3D model, or both?
2. What building-specific objects does the tool provide (walls, doors, windows, slabs, roofs, stairs…), and are they definitional or common?
3. How are the multiple representations (plan / section / elevation / 3D) related? Is model→drawing consistency automatic?
4. What does the documentation deliverable look like (sheets/pages, title blocks, scale, dimensions)?
5. What data outputs exist (schedules, materials lists, quantity takeoffs)?
6. How do libraries/components/manufacturer content participate?
7. Where does site/terrain context sit?
8. What varies by segment: full BIM delivery vs drafting heritage vs lightweight conceptual modeling vs residential automation?
9. What is the boundary against BIM Authoring, generic CAD/3D modeling, and construction-side document management?

## Representative Products

Selection rationale: market representativeness + different product philosophies + different customer tiers + documentation accessibility.

| Product | Philosophy / tier | Evidence tier reached |
|---|---|---|
| Graphisoft Archicad | architect-first full BIM authoring; mid/large firms | Tier 2 (official product page; help center blocked) |
| Vectorworks Architect | hybrid precision-drafting + flexible 3D modeling ("design anything") with BIM layer | Tier 2 (official product + capabilities pages) |
| SketchUp (+ LayOut) | lightweight general 3D modeler used heavily in early-phase architecture; documentation via companion app | Tier 1 (official help center) |
| Chief Architect Premier | residential/light-commercial automation-focused; small firms / builders / remodelers | Tier 2 (official product page) |
| Autodesk Revit | market-dominant BIM platform | **not reachable** (see Sources) |

## Sources

Fetched 2026-09-06:

- Graphisoft — Archicad product page: https://graphisoft.com/archicad (redirected to en-cn localized version)
- Vectorworks — Architect product page: https://www.vectorworks.net/en-US/architect
- Vectorworks — Architect capabilities page: https://www.vectorworks.net/en-US/architect/capabilities
- Trimble — SketchUp Help Center: https://help.sketchup.com/en/sketchup (Tier 1)
- Chief Architect — Premier product page: https://www.chiefarchitect.com/products/

Unreachable / abandoned:

- Autodesk Revit: https://www.autodesk.com/products/revit/overview → HTTP 403; https://help.autodesk.com/view/RVT/2025/ENU/ → JS shell returning only "Help". Abandoned after 2 attempts per source-access rules. **No operational or feature claims about Revit are made anywhere in this research or in the final document.** Revit is retained as a representative product name for market anchoring only.
- Graphisoft Help Center: https://helpcenter.graphisoft.com/ → HTTP 403 (1 attempt). Archicad evidence rests at Tier 2 (official product page).

Implication: all cross-product claims below are supported by the four reachable products. Archicad observations are Layer A but from marketing/product pages, not operational help; operational precision (menu-level behavior, exact dialogs) was not verified for any BIM-side product and no precise operational claims are made.

## Product Observations

### Graphisoft Archicad (evidence layer A — official product page)

- Positioning: "BIM software for architects"; for architects, designers, engineers and other AEC professionals; design→model→visualize→document→collaborate "from initial concept through construction"; projects of any size; macOS + Windows.
- Building-element toolset: "Parametric building elements: Wall, Slab, Roof, Column, and Beam tools"; "Intelligent objects: Doors, Windows, Stairs, Railings, and Curtain Walls"; tools described as speaking "your language".
- Documentation model: "Design once, document everywhere" — "Turn your 3D models into accurate, fully coordinated drawings with real-time updates"; "Annotate once and let Archicad keep your drawings up to date".
- Early-stage design: "mass modeling and sketches to optioneering and quantity take-offs".
- Data: "Enrich your BIM models with smart metadata, ensure compliance with standards, and enable smooth data exchange"; automated schedules; clash detection; issue tracking (BIMx/BCF); export targets incl. PDF/XLS/Solibri/Bluebeam.
- OpenBIM: IFC 4.3, BCF, IDS (buildingSMART standards).
- Collaboration: BIMcloud — "Multiple users can work on the same model simultaneously"; Archicad Studio vs Collaborate plans (local vs cloud collaboration).
- Sustainability: built-in energy analysis and LCA tools.
- Structural: native structural modeling + automatic Structural Analytical Model for engineer coordination. MEP feature set present (blurring into MEP Design territory).
- Visualization: sketches / white models / photorealistic; AI Visualizer (cloud); BIMx (mobile/VR viewer, Apple Vision Pro); links to Enscape/Twinmotion/D5.

### Vectorworks Architect (evidence layer A — official product pages)

- Positioning: "The Ultimate BIM Software for Architecture design — Sketch, Draw, and Model in a Fully Integrated BIM Workflow"; "BIM Software for Every Design Phase": Pre-design → Schematic Design → Design Development → Construction Documentation.
- Philosophy: "freely sketch, model, and document your design ideas with precision drafting capabilities and the most flexible 3D modeling engine available, powered by SIEMENS Parasolid. So you're not limited by presets and strict parameters."
- Explicit drafting-heritage migration message: "doesn't require you to … toss your CAD standards and libraries out the window. We'll make the transition easy by helping you migrate to BIM at your own pace." → strong evidence that drawing-first practice remains a supported posture inside one product.
- BIM objects: "intelligent, data-rich BIM workflows that include parametric building objects like walls, doors, and windows."
- Documentation: "Documentation and Detailing — Easily generate comprehensive construction documentation, fabrication details, and shop drawings"; "updates to your model automatically updates documentation."
- Data/reporting: "Worksheets and Reporting — automatically generate pre-formatted and custom reports such as material quantity take-offs and schedules for doors, windows, room finishes"; "Maximize the I in BIM" — quantify/analyze early, "what if" scenarios, automate schedules, calculate costs, energy analysis.
- Quality assurance: "embedded data to visualize and validate your designs and generate detailed data sheets … code compliance and building performance."
- Interop: "most default import/export capabilities", openBIM/IFC, direct links Revit/SketchUp/Rhino/Photoshop/Cinema4D; partner ecosystem (Solibri, Bluebeam, Revizto, BIMCollab).
- Visualization/presentation: renderings, AR/VR, panoramas, mood boards, AI exploration, real-time rendering (Maxon Redshift), cloud processing.
- Space planning/analysis tools; interior design tools with manufacturer catalogs; mobile app (photos→3D models, point clouds, room plans).
- Algorithmic-aided design for custom parametric elements.

### SketchUp (+ LayOut) (evidence layer A — official help center, Tier 1)

- Positioning: general 3D modeler — "Create 3D models of buildings, furniture, interiors, landscapes, and more"; share as 2D/3D images, animated walkthrough, 3D print. NOT building-object-based: model is generic geometry.
- Modeling: lines/shapes/push-pull, arcs, freehand, follow-me, solid tools, section planes, precise measurement (Measurements Box, guides, tape measure), drawing axes, photo matching.
- Organization: groups, Outliner hierarchies, Tags (visibility control).
- Components: dynamic components with attributes; 3D Warehouse shared library; sharing/collections.
- Appearance: materials/textures, Styles (edge/face styles), scenes, shadows (real-world location/light), fog, walk-through.
- Geolocation & terrain: Add Location, site context imagery, terrain modeling (Sandbox), placing models on terrain.
- Classification & data: "Classifying Objects", IFC import/export, attribute reports, Generate Report service → the model can carry building-typed data without being object-based.
- **LayOut companion (documentation surface)**: create 2D documents; pages; scaled drawings; insert SketchUp model viewports tied to Scenes; dimension/label/text; Auto-Text for title blocks; tables; scrapbooks (reusable entities); templates; layers; PDF/print/image/CAD export; "Managing Changes and Updates to SketchUp Files" (model references update in the document).
- Interop: CAD (DWG/DXF) import/export, STL/3D printing, COLLADA/FBX/OBJ/KMZ/USDZ/glTF; printing views.
- Platform spread: desktop (Pro subscription), web, viewer apps (mobile/Quest/AR), Ruby API.

### Chief Architect Premier (evidence layer A — official product page)

- Positioning: "Professional Home Design Software" — "all aspects of residential and light commercial design"; audiences: architects & builders, remodelers, interior designers, kitchen & bath designers; DIY variant exists (Home Designer product line — different tier).
- **The core loop, stated verbatim in one sentence**: "As you draw walls and place smart architectural objects like doors and windows, the program creates a 3D model, generates a Materials List, and with the use of powerful building tools, helps produce Construction Documents with Site Plans, Framing Plans, Section Details, and Elevations."
- Automatic building tools: "Automatic and manual building tools allow you to create a variety of roof styles, stairs, framing — both stick and truss, schedules and materials lists for cut, buy and estimating, dimensioning, cross-sections, and elevations."
- 2D/3D simultaneity: "design in any view for seamless and simultaneous editing between 2D & 3D."
- Plan sets: "All views in your project - Floor Plans, Framing, Electrical, Section Details and Elevations have a user defined scale and link to a specific drawing that updates as your design changes. Layers control what displays for each of the drawing pages."
- Rendering/communication: photorealistic ray trace, artistic styles (watercolor/line drawing), 360° renderings, video walkthroughs, sun studies (time-lapse shadow animation).
- Smart objects + manufacturer catalogs: cabinets, appliances, doors, windows, countertops, flooring with product-specific details; 3D Library ("thousands of objects").
- CAD engine for custom objects; CAD-to-Walls tool (imports AutoCAD files, maps layers to walls → 3D); 500+ pre-made CAD details; import DWG/DXF/PDF details.
- Site planning: terrain import/modeling, roads/sidewalks, plants with hardiness zones, sun studies, decks/framing.
- Segment standards: NKBA dimension standards for kitchen & bath.
- Remodeling support: as-built and remodeling layers; changing room size immediately updates materials list.

## Cross-product Comparison

| Dimension | Archicad | Vectorworks Architect | SketchUp + LayOut | Chief Architect |
|---|---|---|---|---|
| Persistent design artifact | project (BIM model) | project (2D drawing layers + 3D model) | model file + separate LayOut document | project (plan + derived model) |
| Building objects (walls/doors/windows as typed objects) | Yes — core toolset (Wall/Slab/Roof/Column/Beam; Doors/Windows/Stairs/Railings/Curtain Walls) | Yes — parametric building objects | **No — generic geometry; classification/IFC optional** | Yes — "smart architectural objects" |
| 2D↔3D coupling | model → coordinated drawings, real-time | model updates documentation automatically; free drafting also allowed | model → LayOut viewports (scene-bound, manually refreshed) | draw walls → 3D model generated; simultaneous 2D/3D editing |
| Plan/section/elevation derivation | from model | from model; also fabrication details/shop drawings | section planes + LayOut scaled views | from model (framing/electrical plans, sections, elevations) |
| Sheets/pages with title blocks & per-view scale | export targets incl. PDF | construction documentation generation | LayOut pages, Auto-Text title blocks, per-viewport scale | plan sets, user-defined scale per view, layers per drawing page |
| Schedules / quantities / materials lists | quantity take-offs, automated schedules | worksheets: take-offs, door/window/finish schedules | attribute/Generate Report (optional classification) | automatic materials lists + schedules |
| Libraries | built-in + parametric libraries | manufacturer libraries | 3D Warehouse (community) | manufacturer catalogs + 3D Library |
| Site/terrain | (implied; not prominent on page) | site analysis tools | Add Location, terrain | terrain tools, roads, plants, sun studies |
| openBIM/IFC | IFC/BCF/IDS first-class | openBIM/IFC + wide import/export | IFC import/export + classification (secondary) | CAD import (DWG→walls) |
| Collaboration | BIMcloud real-time multi-user | multi-user environment; cloud services | web link-sharing (light) | (not prominent; single-user oriented) |
| Rendering/communication | photoreal + AI Visualizer + BIMx | render/AR/VR/panoramas/AI | styles + walkthrough + 3rd-party renderers | ray trace + artistic + 360 + walkthroughs |
| Analysis | energy + LCA; structural analytical model | energy + embodied carbon; QA data sheets | (none built-in) | sun studies; estimating-oriented lists |
| Segment | mid/large firms, full AEC | firms wanting drafting+BIM flexibility | early-phase conceptual + light documentation, all sizes | residential/light-commercial, builders/remodelers |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant

The smallest structure without which the product is no longer an architecture design application:

1. **Persistent scaled building-design document** — the practitioner's design for a specific building lives as a persistent, real-world-scaled, measurable project (drawing and/or model) that is iterated on over time.
2. **Building-organized geometry** — the geometry represents the building itself: its spaces and their enclosing elements and openings — whether authored as typed building objects (walls, slabs, roofs, doors, windows), as freely modeled measured geometry, or as drawn orthographic linework of plans/sections/elevations.
3. **Coordinated multi-view documentation of one design** — the design is documented through a set of building projections — plans, sections, elevations, and 3D views — plus dimensions and annotations, composed into a deliverable drawing/document output used to communicate, permit, and construct the design.

Removal tests:

- Remove (2) → generic CAD / 3D modeling application (e.g., pure mesh/NURBS modeling).
- Remove (3) → massing/sketch visualization tool (drifts toward 3D rendering or AI image generation surfaces).
- Remove (1) → throwaway sketching; not a design application.

Historical/market-sample check (per §24): 2D drafting-era architecture tools (drawing-based, no 3D model, no BIM) satisfy all three invariants: scaled drawing document (1), building linework with wall/opening representation (2), plan/section/elevation drawing set with dimensions (3). Cloud-era and object-based products also satisfy them. The invariant therefore does not encode BIM, parametric objects, or real-time consistency — those are maturity layers.

### L1 — Common Mature Structure

Present in essentially all mature modern products in the sample (evidence layers A/B):

- Typed/parametric building objects (walls, doors, windows, slabs/roofs, stairs, railings) with editable properties — Archicad, Vectorworks, Chief Architect (3 of 4; SketchUp is the structural exception).
- Model↔drawing linkage — change the design, views/documents follow. Automatic and real-time in object-based products (Archicad, Vectorworks, Chief Architect); scene-bound and manually refreshed in the modeler+companion pattern (SketchUp LayOut). In the drafting era this coordination was manual; the modern market treats automatic consistency as table stakes.
- Story/level organization for multi-floor buildings (explicit in building-object products; implicit in modelers via copying/floors).
- Schedules, materials lists, quantity take-offs generated from the model/geometry.
- Sheet/layout composition: pages, per-view scale, title blocks, dimension/label/text annotation.
- Component/object libraries, incl. manufacturer catalogs; community libraries (3D Warehouse).
- Site context: geolocation, terrain, sun studies.
- Visualization: styles/rendering from line/watercolor to photoreal; walkthroughs; 360 panoramas.
- Interoperability: CAD format import/export (DWG/DXF), image/PDF export; IFC/openBIM where BIM delivery is in scope.

### L2 — Variant / Optional Structure

Depends on segment, region, deployment, business model:

- BIM data depth and openBIM delivery (IFC/BCF/IDS classification, clash detection, issue tracking, code-compliance data sheets) — full-BIM posture vs drafting-first posture vs modeler posture.
- Real-time multi-user collaboration (centralized model hosting) vs file-based single-user work.
- Building-performance analysis: energy, embodied carbon/LCA, structural analytical model.
- Algorithmic/generative/automation tooling (parametric custom components, automatic framing/roof generation, optioneering).
- AI-assisted visualization and rendering services (cloud).
- Discipline extensions (MEP design, structural design) — drift toward separate Types when primary.
- Segment automation: residential-specific automatic framing/roofs; kitchen-bath NKBA-dimension standards; interior-design catalog depth.
- AR/VR/mobile presentation surfaces; cloud rendering.
- Pricing/packaging (plans tiering collaboration features) — market fact, not structure.

### L3 — Vendor-specific

- Archicad: BIMcloud, BIMx, GDL, AI Assistant/AI Visualizer, Studio vs Collaborate plan split.
- Vectorworks: Parasolid engine, design-layer/class organization, worksheets, Redshift integration, Vectorworks Cloud Services, mobile app (photos→models/point clouds).
- SketchUp: LayOut companion app structure, 3D Warehouse, Dynamic Components, Style Builder, Ruby API, tags/outliner vocabulary.
- Chief Architect: SSA premium catalog, CAD-to-Walls, as-built/remodeling layer conventions, Home Designer DIY sibling, 3D Viewer/As-Built apps, ChiefTalk.
- Autodesk Revit: unverified this run (source unreachable) — no claims recorded.

## Vendor-specific Findings

(see L3 above; none promoted into the canonical core)

## Rejected Findings

- "Architecture design application = BIM software" — **rejected as definition**. Evidence: SketchUp (no building objects) and Vectorworks' explicit drafting-heritage migration messaging show the Type predates and exceeds BIM; BIM depth is an L2 posture. However, market language (ArchiCAD/Vectorworks marketing) heavily conflates the two — see Boundary Findings.
- "Real-time team collaboration is core" — rejected: several successful products are single-user/file-based; collaboration is segment- and scale-dependent (L2).
- "Energy/sustainability analysis is core" — rejected: present in 2 of 4 sampled products; optional (L2).
- "AI visualization is core" — rejected: marketing-led, vendor-specific (L3).
- "Built-in photorealistic rendering is core" — rejected: SketchUp relies on third-party renderers; rendering is L1/L2 communication capability, not defining.
- "Walls/doors/windows objects are definitional" — rejected as L0: SketchUp reaches the same Type without them (freely modeled + classified geometry + LayOut documentation). They are the dominant L1 implementation, not the invariant. (The building-organized-geometry invariant at L0 is phrased to include both authored-object and drawn/modeled-realizations.)

## Boundary Findings

- **vs BIM Authoring (directory sibling, 17)** — the most serious overlap. Sampled products self-describe as "BIM software for architects" (Archicad) / "BIM Software for Architecture design" (Vectorworks). In the current market the two leaf names point at overlapping tool categories. Distinguishing lens adopted: Architecture Design Application = the architect's design-and-documentation authoring surface (design intent → drawings/model deliverable); BIM Authoring = authoring the data-rich, coordinated building model as a shared cross-discipline information asset for delivery. Historical test supports keeping them separable: architecture design applications existed as 2D drafting tools long before BIM, so BIM capability cannot be the definition of either if "Architecture Design Application" is to keep historical coverage. **Flagged for joint review** — probable near-alias in the modern market.
- **vs Mechanical CAD (16) / 3D Modeling Application (04.13)** — generic precise geometry without building semantics or building-projection documentation. SketchUp sits close to 3D Modeling Application; what pulls it into this Type is its dominant architecture use + documentation path (LayOut scaled documents, IFC classification). Remove LayOut-style documentation and classification and SketchUp-class tools are generic modelers — the boundary test in action.
- **vs Structural Engineering Design / MEP Design / Civil / Site Design (17 siblings)** — discipline-specific objects and analysis (load-bearing models, duct/pipe systems, grading) as the primary structure. Archicad's structural/MEP feature sets show the drift; when discipline objects become primary, the product belongs to the engineering Type.
- **vs Construction Document Management (17)** — that Type manages produced documents/transmittals; this Type authors the design geometry that the documents depict.
- **vs Quantity Takeoff / Construction Estimating (17)** — those Types consume models/drawings to measure/price; this Type's schedules are an output capability, not its center of gravity.
- **vs Diagramming Application (03.05) / Digital Whiteboard** — not building-scaled, not real-world measured, no building projections.
- Removal tests ("去掉什么就变成另一个 Type"): remove building semantics → CAD/3D modeling; remove drawing/documentation production → massing/sketch tool; remove real-world scale/measure → diagramming; remove the single persistent design document → component library service.

## Uncertainties

- Autodesk Revit — the market's dominant BIM platform — was not directly verified (403 / JS shell). No claims made about it. If later processed, a BIM Authoring pass should re-verify.
- Archicad evidence is Tier 2 (product page); its help center was blocked. Operational detail (exact tool behavior, view/dependency mechanics) is inferred from cross-product patterns, and the final document deliberately avoids operational precision.
- Whether "pre-design/schematic/development/documentation" phase vocabulary (Vectorworks' framing) generalizes across the market — it matches industry practice but was only directly evidenced in one product; final document uses it as a common framing, not a universal standard.
- The exact structure of multi-user collaboration (reservation/locking vs real-time sync) was not verified; final document stays generic.

## Final Synthesis

An Architecture Design Application is the authoring environment in which a practitioner designs a specific building and documents it: the design lives as a persistent, real-world-scaled project whose geometry is organized around the building (spaces, enclosing elements, openings) — whether as typed building objects, freely modeled measured geometry, or drawn orthographic linework — and the deliverable is a coordinated set of building projections (plans, sections, elevations, 3D views) with dimensions and annotations, composed into sheets/documents used to communicate, permit, and construct the building. Mature modern products add parametric building objects with automatic model→drawing consistency, generated schedules/quantity take-offs, component and manufacturer libraries, site context, and visualization; BIM data depth, openBIM delivery, real-time collaboration, performance analysis, and automation are variant postures, not the definition. The Type's closest sibling — BIM Authoring — is heavily conflated with it in current market language and is flagged for joint review.
