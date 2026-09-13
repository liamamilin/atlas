# Research Notes — Telecom Network Design

## Research Goal

Understand what a **Telecom Network Design** application is as an Application Type: what a "design" is inside these products, what objects and workflows constitute the design act, how designs relate to the built network and to the network record, and where the Type's boundary sits against Telecom Network Planning, Fiber Network Management, Telecom Inventory Management, Network Construction Management, and generic diagramming/CAD tools.

## Initial Boundary (hypothesis before research)

Working hypothesis: Telecom Network Design is the engineering application that turns deployment intent into a **buildable** network definition — proposed network elements and connectivity authored against a physical/geographic context, validated, quantified (materials, cost), and handed off to construction. Nearest neighbors:

- **Telecom Network Planning** — earlier-stage: where/what to build, demand, investment prioritization.
- **Fiber Network Management** — the persistent plant of record that designs flow into (fiber pass pre-held a seam: "design act vs plant of record — center-of-gravity, not exclusion").
- **Network Construction Management** — the build project that consumes the design.
- **Diagramming / CAD** — generic drawing without telecom network semantics.
- **ECAD / PCB Design** — same "design application" shape, different object world.

Unknowns going in: whether wireless RAN design (propagation-driven) and fixed-line OSP design (connectivity-driven) share one Type structure; whether design is a standalone product category or always a workflow inside a plant-record platform; how far cost/BOM machinery is definitional.

## Research Questions

1. What is the unit of design work (design/project/job)? What state does it carry (proposed vs built)?
2. What are the core objects being designed (elements, connectivity, structures, sites, equipment)?
3. Against what context is design authored (map, floor plan, terrain/propagation environment)?
4. What does the design workflow look like end to end (author → validate → quantify → hand off → as-built)?
5. What rules/constraints do products enforce (connectivity rules, QA/QC, error checking, design standards, catalogs)?
6. What build-ready outputs does design produce (BOM, cost estimates, work packets, drawings, reports)?
7. How does the wireless pole differ (propagation prediction, coverage/capacity analysis, model tuning)?
8. Who performs design (operator in-house vs engineering firms), and how does that shape the product?
9. Where exactly is the seam vs Telecom Network Planning and vs Fiber Network Management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Pole | Customer tier |
|---|---|---|---|
| 3-GIS \| Web (+ Prospector, Mobile, Admin) | 3-GIS | GIS-based fiber/copper network design inside a network system of record | Mid-size to tier-1 operators (TDC NET, Windstream, Orange Jordan) |
| Network Manager Telecom + Optimized Design use case (+ Comsof Fiber) | IQGeo | Geospatial network lifecycle platform with a dedicated design use case (LLD) | Tier-1 telcos (Deutsche Telekom, BT, AT&T-class logos) |
| VETRO FiberMap (+ Engineering package, Mobile) | VETRO | Cloud-native fiber design & management for operators and engineering firms | Regional ISPs / altnets / engineering firms |
| Atoll | Forsk | Desktop/server wireless (RAN) design & optimisation platform | MNOs, vendors, regulators, consultancies (140+ countries) |
| iBwave Design (Lite/Enterprise) | iBwave | In-building wireless network design suite with parts database and BOM | Carriers, system integrators, enterprises |

Pole coverage: fixed-line OSP (3 products, three philosophies: Esri-embedded, platform-suite, cloud-native) + outdoor RAN (Atoll) + in-building wireless (iBwave). No HFC/coax-only vendor sampled (3-GIS documents a Copper module — multi-media scope evidence only).

## Sources

All fetched 2026-09-10 (Tier 2 official product/solution pages; no Tier-1 help centers reachable — see Uncertainties):

- 3-GIS — root: https://www.3-gis.com/ ; solution: https://www.3-gis.com/telecom/fiber-network-planning-design ; product: https://www.3-gis.com/software/3-gis-web
- IQGeo — root: https://www.iqgeo.com/ ; design use case: https://www.iqgeo.com/telecom-use-cases/optimized-design
- VETRO — root: https://vetrofibermap.com/ ; engineering package: https://vetrofibermap.com/products/fibermap-engineering/
- Forsk — Atoll overview: https://www.forsk.com/atoll
- iBwave — iBwave Design: https://www.ibwave.com/products/ibwave-design/

## Product Observations

### Product A — 3-GIS (Web / Prospector / Mobile / Admin)

Evidence layer: A (directly observed on official pages).

- Telecom overview: "a connected network record for planning, designing, building, documenting, and managing fiber and copper networks… from early planning and OSP design through construction, field updates, asset inventory, maintenance, operations, and serviceability."
- Dedicated solution page "Fiber network planning & design — Design networks ready to build": "connecting early strategy, route planning, detailed design, GIS data, and handoff workflows… network plans that are ready for construction, activation, operations, and future growth."
- **Planning vs design FAQ (verbatim, load-bearing for the boundary):**
  - "Fiber network planning determines where fiber should be deployed, what conditions shape the build, and how projects should be prioritized **before detailed design begins**."
  - "Fiber network design **turns deployment plans into constructible, connected network data**. It defines how the network should be built, how assets relate to one another, and what information teams need to carry work from planning through construction, activation, operations, and future growth."
- Design capabilities: Route planning ("evaluate routes, service areas, existing assets, build constraints… before capital is committed"); OSP design ("detailed fiber layouts, asset placement, structures, equipment, cables, routes, and connectivity in a GIS-based environment"); Network modeling ("fiber routes, network equipment, structures, splice points, strand-level detail, and connectivity in a way that carries forward into construction, documentation, operations, and future network changes"); Design standards ("configurable workflows, data standards, and repeatable design practices"); Cleaner handoffs ("into construction, field work, as-builts, activation, and operations").
- Depth claim: "from wavelengths running through individual strands to the racks, cards, slots, and chassis that define equipment relationships."
- "Planning and design should not create disposable project files… build a usable network record from the beginning."
- 3-GIS | Web product page: "The telecom network system of record… for planning, designing, documenting, analyzing, and managing the data behind telecom operations. Built around assets, connectivity, capacity, and change." Key feature groups: Model / **Design** / Trace / Operate. Design-to-build: "streamlined lateral creation, **work orders and project tracking, material placement, and constructible work packet generation**."
- Lifecycle continuity (verbatim): "Maintain continuity between **what was planned, what was designed, what was built, what changed in the field, and what is ready for service**."
- FAQ: "Is 3-GIS | Web just design software? No… it supports design workflows, but its larger role is telecom network management across the full lifecycle." — design is a workflow inside the plant record.
- Prospector: "rules-based modeling to generate prescribed fiber routes, **estimate costs, compare alternatives**, and identify revenue opportunities."
- Admin: "users, roles, permissions, data visibility, **QA/QC rules**, workflows."
- Users named: deployment stakeholders (leaders), network planners, OSP designers/engineers, operations teams.

### Product B — IQGeo (Network Manager Telecom / Optimized Design / Comsof Fiber)

Evidence layer: A.

- Platform: "a single, end-to-end platform to plan, design, build, and operate their physical network infrastructure." Telecom use cases split **Plan & Design** into "Optimized Planning" and "Rapid Design" (separate pages) — the planning/design seam is explicit in the vendor's own taxonomy.
- Optimized Design page: "Low-level fiber design that delivers build-ready networks, right the first time." "translate plans into accurate, **construction-ready low-level designs**. By correcting and validating designs before build using real-world field and survey insight… ensure clean handoff into construction workflows."
- Old-way/best-practice contrasts (verbatim): "Static LLDs disconnected from field reality" vs "Designs corrected and validated using field and survey insight"; "Design issues discovered during construction" vs "**Pre-build design correction** before construction"; "Manual handoff from design to construction" vs "Seamless transition from LLD to construction workflows"; "Limited visibility into real-world constraints" vs "Designs reflect real-world and **permit constraints**."
- What design delivers: Construction-ready low-level design (LLD); Pre-build design correction; Field, survey, and permit constraint validation; **Connected network design model** ("Validate routes, structures, and connectivity across the network"); **Design-to-construction handoff** ("Generate construction-ready outputs that flow directly into execution workflows"); Inside and outside plant design capture.
- Customer quote (Deutsche Glasfaser): "With IQGeo you can pinpoint exactly what is **planned, what is under construction, and what is built**." — proposed/under-construction/built states on one record.
- Customer quote (Deutsche Telekom): "you still have the possibility to **try several versions of a network** if needed" — design variants.
- Customer quote (Brightspeed): "the upfront design takes much, much less time using IQGeo automated process… you go from the design phase into a field survey and then into construction."
- Comsof Fiber exists as a dedicated automated fiber design application (acquired design tool) — automation pole.
- ROI claims (50–90% design-effort reduction etc.) — marketing figures, excluded from canonical claims.

### Product C — VETRO FiberMap (Engineering package / Mobile)

Evidence layer: A.

- Positioning: "VETRO FiberMap — Fiber network design and management platform"; "Manage your network from **design to monetization**." Serves network operators, **engineering firms**, middle-mile, public sector; roles include Planning ("Design optimal, cost-effective fiber networks") and Operations ("construction, maintenance, and as-built documentation").
- Engineering package capabilities: Real-time Collaboration & Feedback ("share network plans on a single platform for instant client feedback"); **Automated Design & Standardized Templates**; **Live Field Updates** ("Integrate accurate field data directly into your designs"); Construction Progress Tracking; **Real-time As-Builts** ("Maintain accurate records and generate reports for compliance and quality assurance").
- Customer quotes (verbatim): "a **design program that could be easily modified**"; "VETRO Mobile enabled us to **directly submit drawings to editors** for immediate review and placement"; "By **validating connections in a network design**, VETRO **catches errors before they become problems**"; "fiber designs were immediately available for review and collaboration. VETRO became the **source of truth for the splicing of fiber circuits** and physical fiber assets"; "visibility into our contractor progress and '**ready for sales**' stages."
- Investment-facing outputs: "Generate precise **cost and revenue estimates** to invest with confidence"; grant-proposal support (ARPA application case).

### Product D — Atoll (Forsk)

Evidence layer: A.

- Self-description: "a multi-technology **wireless network design and optimisation platform**… from initial design to densification and optimisation." Also marketed as "radio planning and optimisation software" — the wireless pole's planning/design vocabulary is blurred by the vendor itself.
- "Advanced multi-RAT RAN design capabilities for 2G, 3G, 4G, and 5G… massive MIMO, 3D beamforming, and mmWave propagation for the design and roll-out of 5G networks."
- GIS features: digital elevation models, clutter data (type and height), 3D building data, traffic/population/climate data, integrated cartography editor, GIS interfaces (MapInfo, ArcGIS, Google Earth), WMS/online maps — the physical-context authoring layer for RF.
- Propagation modelling: integrated model library, ray-tracing models (Aster/Aster mmWave), **automatic propagation model tuning**, external model integration.
- Prediction + measurement: CW and drive-test data import/analysis; prediction/measurement comparison; live-network data (KPIs, traces, crowdsourced) feeding planning and optimisation (Atoll Live).
- Automation: ACP (Automatic Cell Planning), AFP (Automatic Frequency Planning).
- In-Building module: "modelling of floor plans and building elements, indoor propagation, equipment installation layouts, and **automatic calculation of bills of materials**."
- Backhaul: microwave/transmission link planning (Atoll Microwave).
- Platform mechanics: multi-user database with consistency management, user privileges, distributed computing, reporting, scripting.

### Product E — iBwave Design (Lite / Enterprise)

Evidence layer: A.

- Self-description: "the industry standard for designing indoor wireless networks… Import floor plans, design using a database of over 40,000 parts, simulate your network in advanced 3D for both coverage and capacity, and easily produce key project reports."
- Authoring: floor-plan import (CAD/PDF/JPG), "assign materials to walls and surfaces," 3D building model; components database (antennas, small cells, cables, access points, fiber hardware).
- Design automation: "automatic link budget calculations, automatic AP placement, automatic cable alignment and cable length calculations… built-in error validation."
- Validation: "Advanced RF Propagation… simulate network performance and verify that coverage, throughput and capacity will meet your customer's requirements… View prediction results in advanced 3D to **troubleshoot potential issues before deployment**"; **Automatic Error Checking** ("Establish thresholds, customize warnings and errors, and view errors on-screen as you design"); Capacity Analysis.
- Outputs: "Output Maps and Compliancy Reports… predicted performance… how it complies with their performance KPIs"; "**Equipment list and project cost reports**… accurate estimate of what will be required for deployment and how much the project will cost."
- Standardization & collaboration: ".ibw file format… industry standard file format"; free read-only **iBwave Viewer** for stakeholders; "Customized Templates… enforce consistency between all the designs"; iBwave Mobile integration ("from site walk to final delivery… field team collect measurements and start a preliminary design on-site… office design team can enhance and finish the design"); iBwave Unity (project/site management, tasks, estimates, tracking).
- Editions: Lite (passive DAS, single sector) vs Enterprise (active DAS, small cells, fiber backhaul, capacity analysis) — scale/complexity segmentation.

## Cross-product Comparison

| Structure | 3-GIS | IQGeo | VETRO | Atoll | iBwave | Layer |
|---|---|---|---|---|---|---|
| Design as distinct proposed state (planned/designed vs built/as-built) | ✔ ("planned, designed, built, changed in the field, ready for service") | ✔ ("planned, under construction, built"; LLD) | ✔ (designs → as-builts; "ready for sales") | ✔ (design project vs live network; live data separate) | ✔ (design project before deployment) | B |
| Authoring against physical context | ✔ GIS map | ✔ GIS map | ✔ GIS map | ✔ GIS + terrain/clutter/3D buildings | ✔ floor plans + 3D building | B |
| Network elements + connectivity as design content | ✔ routes/structures/splices/strands; racks/cards/slots | ✔ routes, structures, connectivity | ✔ connections, splicing of circuits | ✔ cells/transmitters/antennas (+links) | ✔ parts, cables, antennas, link budgets | B |
| Materials/equipment catalogs | ✔ configurable materials catalogs | ✔ (design capture; Comsof automation) | ✔ (implied via cost estimates) | ✔ equipment/antenna databases | ✔ 40,000+ parts database | B |
| Validation before build | ✔ QA/QC rules | ✔ pre-build design correction; validate routes/structures/connectivity | ✔ "validating connections… catches errors" | ✔ prediction + error surfaces; model tuning | ✔ automatic error checking; prediction | B |
| Build-ready quantification (BOM/cost) | ✔ material needs; work packets | ✔ construction-ready outputs | ✔ cost & revenue estimates | ✔ BOM (In-Building); equipment lists | ✔ equipment list + project cost reports | B |
| Design-to-construction handoff | ✔ "cleaner handoffs" | ✔ explicit deliverable | ✔ construction progress tracking | ✔ design outputs feed rollout (less explicit) | ✔ Mobile site-walk → design → delivery | B (A for IQGeo/3-GIS) |
| Field/real-world data feeding design | ✔ Mobile redlines/field validation | ✔ field, survey, permit constraint validation | ✔ live field updates | ✔ CW/drive-test tuning | ✔ Mobile site-walk measurements | B |
| Design standards/templates | ✔ design standards, repeatable practices | ✔ (design capture standards) | ✔ standardized templates | ✔ (customisation/scripting) | ✔ customized templates | B |
| Variants/scenario comparison | ✔ Prospector "compare alternatives" | ✔ "try several versions" | ✔ (cost/revenue scenarios) | ✔ ACP alternatives; predictions | ✔ (simulation before purchase) | B |
| As-built reconciliation in-product | ✔ | ✔ | ✔ | ✖ (out of scope; live data imported for tuning) | ◐ (Unity project tracking; closeout packages) | B (variant) |
| RF prediction machinery (propagation/coverage/capacity) | ✖ | ✖ | ✖ | ✔ core | ✔ core | B (pole-defining) |
| Automation of design authoring | ◐ Prospector rules-based routes | ✔ Comsof Fiber | ✔ automated design + templates | ✔ ACP/AFP | ✔ auto placement/link budget/cable length | B (depth varies) |

Reading: the fixed-line pole and the wireless pole realize the same three-part structure (proposed configuration authored against physical context → validated → quantified for build) with **different validation physics**: connectivity/rules validation (fiber) vs propagation/prediction validation (RF). Both converge on BOM/cost and construction handoff.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The proposed network configuration as the unit of design work** — a persistent, editable composition of network elements (equipment, cables/links, structures/sites) with their connectivity and engineering attributes, representing infrastructure to be built or changed, held as a distinct design state separate from the built network.
   - Remove → a plant-record viewer or a generic GIS/CAD canvas; the "design" as a distinct authored proposal disappears.
2. **Engineering authoring against a physical context** — elements are placed, routed, and connected in a representation of the physical world (geographic map, building floor plan, or terrain/propagation environment), with engineering attributes (materials, capacities, equipment specifications) drawn from catalogs and design standards.
   - Remove → abstract diagramming or freehand drawing with no physical or engineering grounding.
3. **The design-to-build conversion** — the design is validated (against connectivity rules and/or predicted performance), quantified into build-ready outputs (materials/BOM, cost estimates, construction documentation/work packets), and handed off toward construction, where the built outcome is reconciled back as the as-built network.
   - Remove → an analysis or drawing tool with no construction consequence; the reason the design exists disappears.

Jointly-held is load-bearing: 1 alone = a proposed-objects list (inventory with a flag); 2 without 1 = a map/floor-plan editor; 3 without 1+2 = a BOM calculator; 1+2 without 3 = pretty proposals nobody builds; 1+3 without 2 = abstract schematics; 2+3 without 1 = per-drawing drafting with no design object.

### L1 — Common Mature Structure

Present in most mature products, not required for recognition:

- proposed-vs-built states carried on a shared network record (fiber pole) or as managed design projects (wireless pole)
- design validation machinery: connectivity QA/QC rules, automatic error checking, prediction-based verification
- design variants/scenarios with comparison (alternatives, cost/revenue scenarios)
- field-data integration feeding design correction (surveys, site walks, redlines, drive tests)
- as-built capture/reconciliation closing the loop (fiber pole; wireless pole often hands off instead)
- design standards, templates, and governed materials/equipment catalogs
- multi-user collaboration, versioning, roles/permissions
- construction handoff artifacts: work packets, drawings, schematics/diagrams, prediction/compliancy reports
- integration outward: permitting, construction management, OSS/BSS, serviceability
- reporting and visualization (maps, 3D, diagrams)

### L2 — Variant / Optional Structure

- **Domain scope**: OSP fiber (aerial/buried), copper/coax, in-building wireless, outdoor RAN (macro/small cell), microwave backhaul, private networks — the same Type realized over different network media.
- **Validation physics**: connectivity/rules-based (fiber/copper) vs propagation/prediction-based (RF) — the deepest structural variant.
- **Automation depth**: manual drafting → rules-based route generation → automated design (auto-routing, auto-placement, ACP/AFP, auto-BOM).
- **Who produces designs**: operator in-house teams vs engineering firms/consultancies as the design producer (shapes collaboration, client review, deliverable packaging).
- **Platform substrate**: GIS-embedded (Esri), geospatial platform suite, cloud-native SaaS, desktop engineering tool with license models.
- **Costing depth**: materials estimate → investment-grade cost/revenue modeling → grant/bid proposals.
- **Lifecycle span**: design-only tools vs design-through-operations platforms (center of gravity).
- **Deployment**: SaaS / on-premises / desktop licenses.

### L3 — Vendor-specific (research notes only)

- 3-GIS: Prospector / Diagramming / Admin / Copper module names; "work packets"; Telecom Domain Network (Esri) positioning; marketing scale figures (500M+ records, 170K+ miles, 50M+ transactions).
- IQGeo: "LLD" (low-level design) vocabulary; Comsof Fiber (acquired automated design tool); NetLux AI; Visual Agent Studio + named agents; Workflow Manager; ROI percentages (50–90%, 33%, 6×, 100% AI-audited).
- VETRO: Z-Manager (demand publishing), AddressBook, "ready for sales" stage label, "design to monetization" framing.
- Forsk: Atoll module names (Atoll Live, Atoll In-Building, Atoll One, Atoll Microwave), Aster/CrossWave propagation models, ACP/AFP acronyms, license-count marketing (11,000+ licenses, 500+ customers, 140+ countries).
- iBwave: .ibw file format, iBwave Viewer, iBwave Unity, iBwave License Manager (license models), 40,000+ parts database, 500,000-networks claim.

## Rejected Findings

- **"Telecom network design = GIS."** Rejected: GIS is the common substrate for the fixed-line pole (3-GIS on Esri; IQGeo "goes far beyond GIS"), but the wireless pole authors on floor plans and terrain models, and the invariant is the proposed configuration + physical context + build conversion, not a GIS engine.
- **"Design is a standalone product category separate from network management platforms."** Rejected as absolute: in the fixed-line pole, design is a workflow inside the plant-record platform (3-GIS FAQ: "supports design workflows, but its larger role is telecom network management"); in the wireless pole, design is the product's center (Atoll, iBwave). The Type is defined by the design act, wherever it is hosted.
- **"Design includes construction management."** Rejected as definitional: construction tracking appears as adjacent modules (VETRO, IQGeo Build use cases) but the design Type's terminal output is the buildable definition and handoff, not the build project itself.
- **"RF prediction is the defining mechanism."** Rejected: prediction is the wireless pole's validation physics; the fiber pole validates by connectivity rules. The invariant is "validated before build," not "propagation-modeled."
- **"Design requires automated design (auto-routing/AI)."** Rejected: automation depth is a variant axis; paper-era and manual-drafting products satisfy the core.
- Precise numeric claims (ROI percentages, parts counts, license counts, network scale figures) — rejected from the final document: marketing figures without operational documentation.

## Boundary Findings

- **vs Telecom Network Planning**: the sampled vendors themselves draw the seam. 3-GIS FAQ (verbatim): planning "determines where fiber should be deployed, what conditions shape the build, and how projects should be prioritized **before detailed design begins**"; design "turns deployment plans into **constructible, connected network data**." IQGeo splits "Optimized Planning" from "Rapid Design" as separate use cases. Seam: planning = demand/coverage/investment decisions producing deployment intent; design = engineering that intent into a buildable artifact. The blur is real and vendor-labeled ("planning & design" solution naming; Atoll self-labels "planning and optimisation" while doing detailed design) — recorded as a straddle, not resolved by exclusion.
- **vs Fiber Network Management**: confirms the pre-held seam from the fiber pass. Fiber Network Management centers the **persistent plant of record** (connected, geospatial, lifecycle-worked); Telecom Network Design centers the **design act** (proposed configurations, validation, build conversion). In sampled fiber products design happens *inside* the plant record as proposed-vs-built states (3-GIS: "what was planned, what was designed, what was built"; IQGeo/DG: "planned, under construction, built") — center-of-gravity seam, not exclusion. Remove the design act → plant record management; remove the persistent record → pure design tooling.
- **vs Telecom Inventory Management**: inventory holds the estate of record (equipment/services, buy-side or operator-side); design proposes *changes* to the network that inventory will later hold. Design consumes the record as context and produces the as-built that updates it. Different temporal orientation (future proposed vs current actual).
- **vs Network Construction Management**: construction centers the build project (schedules, contractors, budgets, progress); design produces the buildable definition and hands off. Field-capture and construction-progress modules blur at the seam (VETRO, IQGeo Build).
- **vs Telecom Provisioning Platform**: provisioning activates services on the *built* network; design creates the network to be built. Downstream neighbor.
- **vs Mobile Network Management**: RAN management (NMS/OSS) operates the live radio network; RAN design (Atoll) engineers it before it exists and imports live data only to inform design/tuning. Different lifecycle stage and object world (live cells/KPIs vs proposed transmitters/predictions).
- **vs Diagramming Application / CAD**: generic drawing lacks (a) telecom network semantics (connectivity, strands, RF), (b) governed catalogs/standards, (c) the build conversion. Remove those → diagramming/CAD territory.
- **vs ECAD / PCB Design**: same application *shape* (author → validate → BOM → fabrication handoff) but a different object world (circuit boards/components vs network plant/RAN). The directory's placement of Telecom Network Design under §19 (telecom) rather than §16 (electronics) is correct.
- **vs Utility GIS**: GIS platforms supply the substrate and data models; design applications supply the design act on top. Substrate, not identity.

## Historical / Market-Sample Check (§24)

Paper-era telecom design satisfies the core: OSP designers drawing proposed routes on base maps with staking sheets and material lists (proposed configuration + physical context + build conversion), RF engineers doing link budgets and coverage curves on maps before site build. Red-lined as-builts returned from the field closed the loop by hand. No GIS, cloud, mobile, AI, or automation is required. Conversely, a modern interactive 3D map canvas with no connectivity semantics, no governed catalogs, and no build outputs fails the core — supporting the three-part invariant over any particular implementation era. The definition is not over-fitted to the current GIS/cloud/AI implementation.

## Uncertainties

- No Tier-1 help-center documentation reached for any sampled product; all evidence is official product/solution/FAQ pages. Operational specifics (exact object schemas, state-name vocabularies, validation-rule details, numeric limits) are deliberately not asserted in the final document.
- VETRO's help center (Zendesk) requires authentication; not accessed. VETRO evidence is product pages + customer quotes.
- Atoll's operational documentation (user manual) sits behind the downloads portal; not accessed. Atoll evidence is the product overview page.
- The wireless pole's planning/design blur (Atoll self-labeling) is recorded but not resolved; the final document treats planning and design as distinct centers of gravity with heavy product-level straddle.
- Core/transport (logical) network design — e.g., transport topology design inside OSS suites — was not sampled; the documented Type is grounded in physical-access/RAN design. Scope note recorded, no claim made about logical-design products.
- HFC/coax design vendors (e.g., CAD-based broadband designers) were not sampled; multi-media scope rests on 3-GIS's Copper module evidence only.
- Whether Esri's Telecom Domain Network should eventually read as platform-native variant or competing substrate remains unresolved (carried from the fiber pass; same evidence base).

## Final Synthesis

Telecom Network Design is the engineering application that converts deployment intent into a buildable network. Its defining core is three jointly-held structures: (1) the **proposed network configuration** as the unit of design work — a persistent, editable composition of network elements, connectivity, and engineering attributes held as a distinct design state separate from the built network; (2) **engineering authoring against a physical context** — elements placed, routed, and connected on a map, floor plan, or terrain/propagation environment with attributes drawn from governed catalogs and design standards; (3) the **design-to-build conversion** — validation (connectivity rules and/or predicted performance), quantification into build-ready outputs (materials/BOM, cost, construction documentation), and handoff toward construction with as-built reconciliation as the common mature closure. The Type spans two structural poles — fixed-line plant design (connectivity-validated, usually hosted inside the network record) and wireless design (prediction-validated, usually standalone engineering tools) — that realize the same core with different validation physics. The seam vs Telecom Network Planning is intent-vs-buildable-artifact (vendor-verbatim); the seam vs Fiber Network Management is design-act-vs-plant-of-record (center of gravity, not exclusion).
