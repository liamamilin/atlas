# Research Notes — BIM Authoring

## Research Goal

Understand, from real products, what the software category that creates Building Information Models actually consists of: what the central persistent artifact is, what makes a model "information-rich" rather than mere geometry, how the model relates to drawings/schedules/exchange, and where the boundary lies with neighboring Types (Architecture Design Application, BIM Coordination, discipline engineering design, CAD/3D modeling).

This pass is also the **joint review** requested by the Architecture Design Application pass, which flagged heavy market overlap between "Architecture Design Application" and "BIM Authoring" and adopted a provisional lens distinction (architecture = the architect's design-and-documentation authoring surface; BIM = the data-rich coordinated model as a shared cross-discipline information asset).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: authoring a building/built-asset model whose elements carry structured data, maintained as a single source from which documentation, quantities, and exchange data derive.
- Primary users: architects and engineers in AEC practices; also detailers, fabricators, contractors on the construction side.
- Nearest neighbors: Architecture Design Application (17 — flagged near-alias), BIM Coordination (17), Structural/MEP/Civil design siblings, Mechanical CAD, 3D Modeling Application (04.13), Quantity Takeoff, Construction Reality Capture, Digital Twin Platform.
- Unknowns: whether "BIM Authoring" is separable at all in the current market; whether exchange (openBIM/IFC) is definitional or maturity; whether construction-side "constructible modeling" belongs here.

## Research Questions

1. What is the central persistent artifact — the model, the drawing set, or both — and which one is the system of record?
2. What does "data-rich" concretely mean in products: what data do elements carry, and how is it consumed?
3. How do drawings/schedules/quantities relate to the model? Derived or independently authored?
4. What exchange machinery exists (IFC, BCF, IDS, classification), and is it definitional or optional?
5. How does multi-user authoring work at product level (sharing/worksharing/cloud)?
6. How do discipline-scoped products (structural detailing, precast/steel) fit — same Type or a different one?
7. Which authoring philosophies exist (object-first parametric vs CAD-native classify/convert vs scan-to-BIM)?
8. What distinguishes this Type from Architecture Design Application, BIM Coordination, and generic CAD/3D modeling — operationally, not just by marketing?
9. What varies by segment/region/deployment?

## Representative Products

Selection rationale: market representativeness + different product philosophies + different customer tiers + documentation accessibility. Autodesk Revit — the market-dominant BIM platform — was intended as anchor sample but remained unreachable (see Sources); it is retained for market anchoring only, with no claims.

| Product | Philosophy / tier | Evidence tier reached |
|---|---|---|
| Graphisoft Archicad | architect-first full BIM authoring; OpenBIM champion; mid/large firms | Tier 2 (official product page; help center blocked — carried over from same-day Architecture pass) |
| Vectorworks Architect | hybrid precision-drafting + flexible 3D modeling with BIM layer | Tier 2 (official product + capabilities pages; carried over from same-day Architecture pass) |
| BricsCAD BIM (Bricsys/Hexagon) | CAD-native BIM: DWG platform, classify/convert 2D+3D assets into BIM data; cost-effective tier | Tier 2 (official product + BIM toolset pages) |
| Tekla Structures (Trimble) | constructible structural BIM: fabrication-grade detailing for engineers, detailers, fabricators, contractors | Tier 2 (official product page; user-guide URL 404) |
| ALLPLAN (Nemetschek) | multi-discipline BIM suite for modeling + design documentation (architects, consultancies, developers) | Tier 2 (official product page) |
| buildingSMART International | standards body — openBIM/IFC/IDS/BCF definitions used for boundary/concept evidence | Tier 1 (official standards-body pages) |

## Sources

Fetched 2026-09-06 (this pass):

- Bricsys — BricsCAD BIM product page: https://www.bricsys.com/en-intl/bim/
- Bricsys — BIM toolset page: https://www.bricsys.com/bricscad/features/bim
- Trimble — Tekla Structures product page: https://www.tekla.com/products/tekla-structures
- Nemetschek ALLPLAN — ALLPLAN Concept product page: https://www.allplan.com/products/allplan-architecture
- buildingSMART International — openBIM overview: https://www.buildingsmart.org/about/openbim/ (defines openBIM, IFC, IDS, BCF, bSDD)
- buildingSMART International — What is openBIM page: https://www.buildingsmart.org/about/what-is-openbim/ (navigation/standards index; body text thin)

Carried over from same-day Architecture Design Application pass (2026-09-06, evidence re-usable, URLs recorded there):

- Graphisoft — Archicad product page: https://graphisoft.com/archicad
- Vectorworks — Architect product + capabilities pages: https://www.vectorworks.net/en-US/architect , https://www.vectorworks.net/en-US/architect/capabilities

Unreachable / abandoned (consistent with the prior pass's findings on 2026-09-06):

- Autodesk Revit: product/help domains returned 403 / script-only shells (attempts on 2026-09-06 in both passes; help.autodesk.com JS shell returned only "Help" in this pass). Abandoned per source-access rules. **No operational or feature claims about Revit are made anywhere in this research or in the final document.**
- Graphisoft Help Center: 403 (prior pass). Archicad evidence stays Tier 2.
- Tekla user-guide URL: 404 in this pass; product-page evidence retained at Tier 2.

Implication: all cross-product claims below rest on five reachable products (four fetched this pass, two carried over) plus the standards body. No Tier-1 operational help documentation for any BIM authoring product was reachable in either pass; the final document therefore avoids operational precision (exact worksharing mechanics, exact format-version support, numeric limits).

## Product Observations

### BricsCAD BIM (evidence layer A — official product + toolset pages)

- Positioning: "2D & 3D CAD for building modeling and documentation"; "DWG-based CAD platform with BIM capabilities"; "The easiest path for CAD users to deliver BIM data."
- Philosophy: CAD-first conversion path — "Introduce 3D workflows alongside your familiar 2D drafting tools"; "Convert 2D and 3D assets into BIM data and increase LOD and LOI with automated tools."
- Toolset page: "A flexible BIM-authoring tool for engineering from a project's inception to completion, with unrivaled DWG and IFC interoperability."
- Data creation: BIMIFY — "AI-assisted component classification — automate tedious classification and data entry"; PROPAGATE — "distribute BIM detailing throughout a digital asset"; direct modeling + parametric modeling ("drive engineering data parametrically… access external data sources").
- Exchange/standards: "Incorporate best practices for IFC classification — core commitment to OpenBIM standards"; "Comply with BIM project standards using IDS XML"; "Collaborate in real-time with BCF"; "Use BIM data authored on other platforms"; "share work with other stakeholders in the industry-standard IFC format."
- Scan-to-BIM: native point clouds; "tools to align, render, and classify point cloud data and detect features such as floors, walls, and spaces"; single scan-to-BIM workflow; as-built drawing generation.
- Outputs: model-based quantity takeoff; shop drawings from design details; "Build high-fidelity BIM models in native DWG."
- Tier/pricing: ~€1,060/yr — the affordable CAD-native tier; customers include contractors (scaffolding/works-preparation use cases).

### Tekla Structures (evidence layer A — official product page)

- Positioning: "powerful structural BIM software"; "truly constructible BIM software"; "data-rich models."
- Core loop, in the vendor's words: "Create, combine, manage and share information-rich accurate 3D models that bring efficiencies at every phase of the construction project."
- Users: "structural engineers, designers, detailers, fabricators, contractors and project managers… on every stage of construction" — construction-side, not design-phase-first.
- Constructibility: "Deliver truly constructible data… the highest level of development (LOD) and reduce the uncertainty of uncoordinated construction documents"; "Accurate constructible data drives fabrication machinery and field hardware" — model feeds fabrication.
- Exchange: "Import, export and link your model data with other project parties, software, digital construction tools, and machinery"; "link with architectural, MEP and plant design software through IFC."
- Collaboration: Tekla Model Sharing — "Teams can work on the same model at the same time while avoiding colliding work"; subscription bundles Trimble Connect (cloud project platform).
- Outputs: customer stories emphasize "accurate schedules and drawings," precast elements flawlessly fitting on site, steel/rebar detailing.

### ALLPLAN / ALLPLAN Concept (evidence layer A — official product page)

- Positioning: "The BIM solution for modeling and design documentation, used by architectural offices, multi-disciplinary consultancies, residential developers and public authorities"; "contains tools needed for modeling, visualizing, evaluating and preparing documentation for buildings."
- Working methodology: "Flexible workflows in 2D, 2.5D and 3D as well as the full object-orientated BIM working methodology."
- Building components: "Flexible building components such as walls, slabs, beams, columns, foundations, stairs, roofs, windows, doors and facades."
- Deliverables: "Accurately generate plans, drawings, and reports from the 3D model and control information for high-quality documentation"; "Reliability in quantity takeoff" — "Precise, verifiable quantity takeoff and costing of modeled and non modeled objects."
- Data exchange: "All relevant file interfaces… including ifc, bcf, pdf, rvt, 3dm, skp, obj, LandXML, dwg, dgn… Software interfaces (Python API, Visual Scripting)"; "CONTENT PACKAGE BIM EASY — predefined yet customizable company standard… ensures well-structured data exchange, especially in openBIM projects."
- In-model quality: clash detection ("identify soft and hard collisions") inside the authoring tool.
- Cloud/collaboration: Bimplus (cloud BIM collaboration platform), ALLPLAN Share (teamwork across company network), Exchange (web-based plan distribution with change notifications), Model Viewer ("check IFC models visually before fully uploading and creating a revision in Bimplus").
- Engineering bridge: "Analytical Model Generation — conversion of geometrical models to analytical models… used by structural analysis solutions."
- Discipline siblings from the same vendor: ALLPLAN Engineering (structural), ALLPLAN Precast, SDS2 (steel detailing) — discipline-scoped BIM authoring exists as its own product line.

### Graphisoft Archicad (evidence layer A — official product page; carried over)

- Positioning: "BIM software for architects"; design→model→visualize→document→collaborate from concept through construction.
- "Parametric building elements: Wall, Slab, Roof, Column, and Beam tools"; "Intelligent objects: Doors, Windows, Stairs, Railings, and Curtain Walls."
- "Design once, document everywhere" — model→drawings with real-time updates; automated schedules; quantity take-offs.
- Data: "Enrich your BIM models with smart metadata, ensure compliance with standards, and enable smooth data exchange"; openBIM: IFC 4.3, BCF, IDS.
- Collaboration: BIMcloud — multiple users on the same model simultaneously; Studio vs Collaborate plans.
- Extras: energy/LCA, structural analytical model, BIMx viewer, AI visualizer.

### Vectorworks Architect (evidence layer A — official pages; carried over)

- "The Ultimate BIM Software for Architecture design — Sketch, Draw, and Model in a Fully Integrated BIM Workflow"; "BIM Software for Every Design Phase."
- Philosophy: precision drafting + most flexible 3D modeling ("not limited by presets and strict parameters"); explicit drafting-heritage migration ("migrate to BIM at your own pace").
- "Intelligent, data-rich BIM workflows that include parametric building objects like walls, doors, and windows"; "Documentation and Detailing… updates to your model automatically updates documentation."
- "Worksheets and Reporting — automatically generate… material quantity take-offs and schedules for doors, windows, room finishes"; "Maximize the I in BIM."
- openBIM/IFC; wide import/export; partner ecosystem (Solibri, BIMCollab etc.).

### buildingSMART International (evidence layer A — standards body)

- openBIM: "enables seamless data sharing and collaboration across platforms and stakeholders, while empowering you to maintain full flexibility in defining your own workflows."
- IFC: "a set of standardized, digital descriptions of the built asset industry."
- IDS: "Standard for defining and checking information requirements in a computer interpretable form to ensure data quality."
- BCF: "Standard communication protocol for efficient issue management and coordination on BIM projects."
- bSDD: "terms and definitions that describe the built environment to increase data consistency."
- Rationale: interoperability, quality benchmarks for data exchange, technology-choice flexibility, asset-lifecycle value.

## Cross-product Comparison

| Dimension | Archicad | Vectorworks Architect | BricsCAD BIM | Tekla Structures | ALLPLAN |
|---|---|---|---|---|---|
| Central artifact | BIM project model | 2D drawing layers + 3D model with BIM data layer | DWG file carrying BIM-classified elements | constructible structural model | BIM model (2D/2.5D/3D, object-oriented) |
| Element objects | Wall/Slab/Roof/Column/Beam + doors/windows/stairs/railings/curtain walls | parametric building objects (walls/doors/windows) | geometry converted/classified into BIM components (BIMIFY/PROPAGATE) | structural members, connections, rebar (constructible detailing) | walls/slabs/beams/columns/foundations/stairs/roofs/windows/doors/facades |
| Element data emphasis | "smart metadata", standards compliance, schedules | "data-rich BIM workflows", "Maximize the I in BIM", worksheets | "convert assets into BIM data… increase LOD and LOI"; classification | "information-rich models", LOD, constructibility | object-oriented methodology; verifiable quantity takeoff |
| Drawings from model | "design once, document everywhere" (real-time) | model updates documentation automatically | 2D↔3D↔BIM in one platform; as-built drawings | schedules and drawings from the model | "plans, drawings, and reports from the 3D model" |
| Quantities | quantity take-offs | take-offs, door/window/finish schedules | model-based quantity takeoff | accurate schedules; fabrication quantities | "precise, verifiable quantity takeoff and costing" |
| Exchange | IFC 4.3, BCF, IDS | openBIM/IFC + wide import/export | IFC, BCF, IDS XML, DWG native | IFC links to arch/MEP/plant; machinery data | IFC, BCF, DWG/DGN/RVT/SKP/OBJ/LandXML… |
| Multi-user | BIMcloud simultaneous | cloud services / multi-user | (not prominent on pages) | Model Sharing (same model, no colliding work) | Bimplus cloud; ALLPLAN Share network teamwork |
| In-authoring checks | clash detection, issue tracking | validate designs, data sheets | (classification quality emphasis) | constructibility focus | clash detection (soft/hard) |
| Authoring philosophy | object-first parametric | drafting-first + BIM layer | CAD-first classify/convert | fabrication-first constructible detailing | object-oriented, flexible 2D/2.5D/3D |
| Segment | mid/large architecture firms | firms valuing drafting freedom | CAD users moving to BIM; contractors | structural engineers/detailers/fabricators/contractors | architecture + multi-discipline consultancies |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as BIM authoring:

1. **Element-based building model** — the persistent artifact is a model composed of individual building elements, each an object representing a physical part of the building/built asset (wall, slab, column, opening, duct, beam, connection…), not undifferentiated geometry or linework.
2. **Data-bearing elements** — each element carries structured, queryable information beyond shape (identity, type, properties, classification), and that data is a first-class product: it can be extracted (schedules, quantities, reports) directly from the model without re-authoring it elsewhere.
3. **Model as the single source** — the project's coordinated outputs (drawings, schedules, data views) are derived from that one model, so changes to the model propagate; the model — not the drawing set — is the project's system of record.

Removal tests:

- Remove (1) → generic CAD / 3D modeling of a building (geometry only). Not BIM.
- Remove (2) → a geometry modeler with no information layer; the "I" disappears. Not BIM authoring.
- Remove (3) → drawings authored independently with attributes attached (2D drafting with data), or disconnected model fragments; the coordination promise of BIM dies. Not BIM authoring.

Historical / market-sample check (§24): early-2000s object-based BIM products (elements + properties + drawings derived from the model) satisfy all three invariants without cloud collaboration, openBIM certification, LOD frameworks, or AI classification. Discipline-specific constructible detailing tools (pre-dating the "BIM" marketing term) also satisfy them — element model + member data + drawings/schedules derived from the model. Conversely, a 2D CAD drawing with block attributes fails (1) and (3), and a freeform building massing model fails (2) — both correctly excluded. The invariant does not encode openBIM standards, cloud collaboration, LOD/LOI vocabulary, or scan-to-BIM; those are maturity layers.

### L1 — Common Mature Structure

Present across essentially all reachable products (evidence layers A/B):

- **Parametric building element toolset** — typed elements with editable properties and behavior (walls join slabs; openings live in hosts; stairs connect levels).
- **Documentation generation from the model** — plans/sections/elevations/sheets derived and kept consistent as the model changes ("design once, document everywhere" is Archicad's phrase for the shared pattern; ALLPLAN: "plans, drawings, and reports from the 3D model"; Vectorworks: "updates to your model automatically updates documentation").
- **Schedules and quantity take-off from element data** — door/window/finish schedules, material quantities, verifiable costing (all five products).
- **Type/element libraries and office standards** — templates, catalogs, predefined company standards (ALLPLAN Content Package; Vectorworks libraries; Tekla Warehouse in ecosystem).
- **Level/grid organization** — stories/levels and grids for horizontal/vertical organization (explicit in building-object products).
- **Interoperability and exchange** — IFC import/export, BCF issue exchange, CAD formats (DWG/DXF); "use BIM data authored on other platforms" (BricsCAD); link to arch/MEP/plant software (Tekla).
- **Multi-user model sharing** — simultaneous or coordinated team work on one model (BIMcloud, Model Sharing, Bimplus/Share).
- **Visualization** — renderings, walkthroughs, presentation output from the model.
- **Site/geolocation context** — terrain models, georeferencing (ALLPLAN terrain, BricsCAD georeferencing).

### L2 — Variant / Optional Structure

Depends on segment, discipline, region, delivery regime, deployment:

- **Discipline scope** — architecture-wide multi-discipline platforms vs discipline-scoped authoring (structural constructible detailing, precast, steel) vs engineering-conversion tools; discipline-scoped products blur toward the discipline engineering Types (see Boundary Findings).
- **Authoring philosophy** — object-first parametric authoring; drafting-first with BIM layer; CAD-native classify/convert of existing 2D/3D assets; scan-to-BIM from point clouds.
- **openBIM depth** — from basic IFC export to IFC classification best practice, IDS-based requirement checking, bSDD dictionaries, BCF coordination loops; driven by regional/public-client BIM mandates.
- **Construction-phase depth** — fabrication-level detail, machine-driving data, field hardware linkage (constructible-detailing pole).
- **In-authoring model quality tools** — clash detection, issue tracking, model viewing/checking before exchange (inside authoring tools, but mature coordination is the separate BIM Coordination Type).
- **Analytical/performance bridges** — analytical model generation for structural analysis; energy/LCA tooling.
- **Data-delivery frameworks** — LOD/LOI vocabulary used by vendors for model development/information level; formal data drops (e.g., FM handover) toward downstream platforms.
- **Deployment & packaging** — desktop perpetual/subscription vs cloud-connected suites; network worksharing vs cloud platforms; tiered editions.
- **AI assistance** — automated classification/data entry (BIMIFY), AI visualization (Archicad), AI scan-to-model.

### L3 — Vendor-specific

- BricsCAD: BIMIFY, PROPAGATE, native-DWG BIM, IDS XML compliance tooling, single scan-to-BIM workflow, Leica point-cloud formats.
- Tekla: Model Sharing, Trimble Connect bundling, PowerFab/warehouse ecosystem, "constructible" vocabulary.
- ALLPLAN: Bimplus, ALLPLAN Share/Exchange/Workgroup Manager, AutoConverter analytical models, Content Package BIM EASY, Parasolid kernel, Python/visual scripting.
- Archicad: BIMcloud, BIMx, GDL, Studio/Collaborate plan split, AI Visualizer.
- Vectorworks: design layers/classes, worksheets, Redshift link, mobile capture app.
- Autodesk Revit: unverified both passes — nothing recorded.

## Vendor-specific Findings

(see L3; none promoted into the canonical core. Notably: BIMIFY-style AI classification and IDS-XML checking are single-product features in the reachable sample.)

## Rejected Findings

- **"BIM Authoring = BIM software for architects"** — rejected as definition. Evidence: Tekla's audience is detailers/fabricators/contractors; BricsCAD targets CAD users and contractors; ALLPLAN ships discipline-specific siblings. The Type is broader than the architecture discipline.
- **"openBIM/IFC support is definitional"** — rejected as L0. Every sampled product has it, but early object-BIM products predate IFC maturity; a discipline-internal BIM model would still be a BIM model. Exchange depth is L1/L2. (Market reality: IFC/BCF presence is effectively universal in current products — recorded as common mature structure.)
- **"Clash detection is part of BIM authoring"** — rejected: present inside some authoring tools (ALLPLAN, Archicad) but its center of gravity is the separate BIM Coordination Type; in-authoring checks are a convenience layer.
- **"Multi-user cloud collaboration is definitional"** — rejected: historically file-based; collaboration form varies (L2). Single-user authoring is still full BIM authoring.
- **"LOD/LOI levels are part of the model structure"** — rejected: vendor vocabulary for describing data maturity; observed in 2 of 5 products; treated as common delivery vocabulary, not structure.
- **"Scan-to-BIM is part of the Type"** — rejected as definitional; it is an intake/conversion capability (L2) whose capture side belongs to Construction Reality Capture.
- **"AI classification/data entry is core"** — rejected: single-product feature (L3), marketing-led.

## Boundary Findings

- **vs Architecture Design Application (17) — the flagged near-alias, examined here as the joint review.** Evidence from this pass supports keeping two lenses rather than merging outright: (a) BIM Authoring's own market language centers on data and delivery — "deliver BIM data," "information-rich models," "LOD/LOI," "IFC/IDS/BCF," "data exchange" — while Architecture Design Application's language centers on design phases and drawing deliverables; (b) the BIM Authoring population includes products with no architecture-design center of gravity (constructible structural detailing; CAD-native conversion; discipline siblings like precast/steel detailing). The same leading products (Archicad, Vectorworks, ALLPLAN, Revit) genuinely occupy both lenses, so the overlap is real and the two leaves remain in tension. Adopted working distinction (consistent with the Architecture pass): if the primary artifact is the architect's design and its documentation deliverable → Architecture Design Application; if the primary artifact is the data-rich element model maintained as the cross-discipline information asset → BIM Authoring. **Flag stands: recommended for joint taxonomy review; probable partial alias in the current market.**
- **vs BIM Coordination (17)** — coordination federates models *authored elsewhere* to detect/resolve cross-discipline conflicts and manage issues; it does not create the elements. Remove "authoring" and it becomes BIM Coordination; add authoring and it is this Type.
- **vs Structural Engineering Design / MEP Design / Civil / Site Design (17)** — those Types center on engineering objects and analysis (member sizing, duct networks, grading); this Type centers on the information model. Boundary is blurry in practice: constructible-detailing products (Tekla-class) perform both authoring and fabrication-level engineering; discipline-branch products of BIM vendors (ALLPLAN Engineering, SDS2) sit between. When analysis/verification of load or flow becomes the primary job, the product belongs to the discipline Type. (Recorded as an uncertainty below.)
- **vs Mechanical CAD (16)** — precise part/product modeling without building-element semantics, building-scale context, or building data deliverables. Element semantics (walls/spaces/openings/systems) vs part semantics (features/parameters of a manufactured part).
- **vs 3D Modeling Application (04.13)** — freeform geometry without element identity, classification, or data extraction. A general modeler becomes adjacent to this Type only when its geometry is classified into building elements with data (the BricsCAD conversion path is precisely this bridge).
- **vs Quantity Takeoff / Construction Estimating (17)** — those Types consume element data to measure and price; the authoring tool's take-off is an output capability, not its center.
- **vs Construction Reality Capture Platform (17)** — capture/registration of scans is that Type; converting scans into classified elements (scan-to-BIM) is an intake capability of this Type.
- **vs Digital Twin Platform / FM handover surfaces** — operation-stage information products; authoring tools may export toward them (data drops), which does not make them the same Type.
- **vs Engineering Document Management / Construction Document Management (17)** — manage produced documents/transmittals; authoring creates the model the documents depict.
- Removal tests ("去掉什么就变成另一个 Type"): remove element identity/data → CAD or 3D modeling; remove authoring (consume models only) → BIM Coordination or Quantity Takeoff; remove the single-source model discipline → 2D drafting with attributes; narrow to engineering analysis as primary → Structural/MEP/Civil design Types; shift to operation-stage → Digital Twin / FM.

## Uncertainties

- **Autodesk Revit uncharacterized** — the dominant BIM platform was unreachable in both passes (403/JS shell). The final document contains no Revit claims. If a later pass verifies it, the canonical model should be re-checked against it (high prior that it fits — the market defines the category through it — but that is inference, not evidence).
- **No Tier-1 operational docs reachable for any BIM authoring product** in either pass (Graphisoft 403; Autodesk blocked; Tekla guide 404). All product evidence is Tier 2 (official product pages) + standards body. Operational mechanics (worksharing implementation, exact exchange dialogs, exact format-version support) were not verified; the final document stays at capability level.
- **Tekla's Type placement** — constructible structural detailing may be as close to Structural Engineering Design as to BIM Authoring; placed here because its own core loop is authoring an information-rich model (its structure is the model, not an analysis), but the BIM-Authoring ↔ Structural boundary is the softest edge in this research.
- **Phase vocabulary** (design phases vs construction phases) was not verified to generalize; the final document describes authoring contexts generically.
- **LOD/LOI** — treated as common delivery vocabulary (2 of 5 products evidenced); not asserted as an industry standard structure.

## Final Synthesis

BIM Authoring is the practice of authoring a building or built asset as a data-rich model of elements: each element is a typed object representing a physical part and carries structured, queryable information; the model is the project's single source, from which drawings, schedules, and quantities are derived and kept consistent; and the model's information is structured for exchange with other disciplines, tools, and downstream uses (IFC/BCF and related standards being the common current realization). Mature products add parametric element toolsets, documentation generation, schedules/take-offs, libraries and standards, level/grid organization, multi-user sharing, visualization, and site context. Disciplines span architecture to structural/constructible detailing to multi-discipline consultancies; philosophies span object-first authoring, drafting-hybrid, CAD-native conversion, and scan-to-BIM. The Type's hardest boundaries: BIM Coordination (consumes, does not author) and generic CAD/3D modeling (geometry without element data). Its softest boundary is Architecture Design Application — the two lenses overlap on the same leading products, the overlap is flagged for joint taxonomy review, and the working distinction is which artifact is the system of record: the design's documentation (Architecture) or the shared data-rich model (BIM).
