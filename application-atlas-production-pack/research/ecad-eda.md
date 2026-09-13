# Research Notes — ECAD / EDA

Research date: 2026-09-07

## Research Goal

Understand what "ECAD / EDA" applications actually are as a Type: what the design of record is, what objects exist inside them, how engineers work in them, how the electrical-engineering pole (control panels, wiring, harnesses) relates to the electronic-engineering pole (circuits, PCBs), and where the boundaries lie against Mechanical CAD, diagramming tools, PCB Design, Semiconductor Design Platform, and Electrical Design Application (all present as separate directory leaves).

## Initial Boundary (working hypothesis before research)

- Hypothesis: ECAD/EDA = electrical/electronic design *authoring* tools. Engineers design electrically-connected systems by drawing symbol-based schematics whose meaning is electrical connectivity, backed by component libraries, and generate downstream deliverables.
- Likely confusions:
  - vs Mechanical CAD (geometry vs connectivity semantics)
  - vs Diagramming Application (visual similarity, no electrical semantics)
  - vs PCB Design leaf (the electronic pole may literally be PCB design products)
  - vs Semiconductor Design Platform leaf ("EDA" in the industry's broadest sense includes IC design)
  - vs Electrical Design Application leaf (possible alias of the electrical pole)
- Unknowns: whether the two poles share one core model; how much physical layout belongs here vs the PCB Design leaf; whether "Electrical Design Application" is an alias.

## Research Questions

1. What is the design of record (project? schematic pages? board file? database)?
2. What are the core objects: symbol, component/part, pin, net, wire, cable, terminal, footprint, board, cabinet?
3. How does connectivity work — how does drawing create electrical meaning (nets, labels, cross-page connections)?
4. What libraries exist and how are parts managed (manufacturer data, footprints, symbols)?
5. What downstream deliverables are generated (netlist, wire lists, BOM, terminal plans, Gerber, panel production data)?
6. What checks exist (ERC/DRC, connectivity errors, design rules)?
7. How do the two poles differ: electrical (cables, terminals, panels, PLC) vs electronic (footprints, copper, routing, fabrication)?
8. What interfaces do users face?
9. What rules/constraints matter?
10. How do products integrate with MCAD / PLM / ERP?

## Representative Products

Selected for market representation + documentation quality + different philosophy + different customer level, covering both poles:

| Product | Pole | Customer level | Philosophy |
|---|---|---|---|
| KiCad | electronic (schematic + PCB) | free / open source, hobbyist→professional | file-based project, separate editors per artifact |
| Altium Designer | electronic (schematic + PCB) | commercial, professional electronics teams | unified design environment + cloud platform |
| Zuken E3.series | electrical (machines, vehicles, harnesses, cabinets) | enterprise | object-oriented database, single platform concept→manufacture |
| EPLAN (Eplan Platform / Electric P8 / Pro Panel) | electrical (machine & panel builders) | enterprise | data-driven platform, digital twin of automation system |

Deliberately NOT sampled: Cadence / Synopsys / Siemens EDA (IC-level semiconductor design — separate directory leaf, out of scope); SOLIDWORKS Electrical / AutoCAD Electrical (MCAD-embedded electrical pole — fetch failed twice, recorded as limitation); WSCAD / Aucotec / IGE+XAO (same pole as E3.series/EPLAN, marginal value).

## Sources

| # | Source | Tier | Result |
|---|---|---|---|
| S1 | KiCad 9.0 — Getting Started in KiCad (official docs, docs.kicad.org) | 1 | Full tutorial: project model, schematic editor, ERC, BOM, PCB editor, DRC, fabrication outputs, symbol/footprint editors. Fetched 2026-09-07. |
| S2 | Zuken — E3.series product pages (zuken.com/en/product/e3series/) | 2 | Module map (E3.schematic/cable/panel/fluid/formboard/topology), object-oriented database claims, industries, DS-E3, MCAD bridges. Fetched 2026-09-07. |
| S3 | Zuken — E3.series Online Documentation portal (zuken.com/doc/e3/series/en/) | 1 | Portal + First Steps chapter list reachable; sub-chapter pages not fetched (time budget). |
| S4 | Altium — Altium Designer product page (altium.com/altium-designer/) | 2 | Positioning ("PCB Design Software"), unified data model, routing, simulation, constraint management, multiboard, harness, versioning, library management, supply chain data. Fetched 2026-09-07. |
| S5 | EPLAN — homepage (eplan.com/en/) | 2 | Positioning (machine/panel builders), platform concept, Electric P8 / Pro Panel / Data Portal / Preplanning product names, Data Portal component counts. Fetched 2026-09-07. |
| S6 | Zuken China site (zuken.com.cn) | 2 | Vendor-internal taxonomy: "电子设计（EDA）" (CR-8000 PCB) categorized separately from "电气CAD" (E3.series). Fetched 2026-09-07 (via redirect). |
| S7 | SOLIDWORKS Electrical product pages | 2 | FAILED — timeout ×2. Abandoned per network rule. |
| S8 | EPLAN Electric P8 / Platform product subpages | 2 | FAILED — 404 ×2 (only homepage reachable). Abandoned per network rule. |

Source-access limitations: EPLAN evidence is homepage-level (positioning + product names only, no operational workflow detail). SOLIDWORKS Electrical not observed at all. Electrical-pole operational detail therefore rests mainly on Zuken product pages (Tier 2). Assertion strength calibrated accordingly.

## Product Observations

### KiCad (electronic pole) — evidence layer A (Tier 1 official docs)

- **Project model**: a KiCad project is a folder with a project file (`.kicad_pro`), a schematic (`.kicad_sch`), a board (`.kicad_pcb`), and optionally libraries/simulation data. Project-level settings include net classes and design rules.
- **Two main tasks**: "drawing a schematic and laying out a circuit board." Schematic = "symbolic representation of the circuit: which components are used and what connections are made between them." Symbols are placed from symbol libraries; wires connect symbol pins.
- **Connectivity semantics**: wires connect pins; net labels name nets; "labels and power symbols with the same name are connected together" — connectivity without visible wires (cross-page/cross-sheet). Power symbols (VCC/GND) as named-net shorthand.
- **Annotation**: every symbol gets a unique reference designator (R1, D1, BT1...).
- **Symbol properties**: value fields (e.g. resistor value, manufacturer part number).
- **Footprint assignment**: each symbol is assigned a footprint ("a set of copper pads that match the pins on a physical component"); dedicated footprint-assignment tool with pin-count filtering.
- **ERC (Electrical Rules Check)**: checks unconnected pins, two power outputs shorted together, undriven power inputs, unannotated symbols, net-label typos; severity configurable; violations mapped to schematic locations; PWR_FLAG special symbol to mark driven nets.
- **BOM generation**: from symbol metadata, configurable grouping/export format.
- **PCB Editor**: board setup (stackup = copper/dielectric layers; design rules = track/via sizes and spacing; net classes = rule sets per net group); "Update PCB from Schematic" (manual forward sync); board outline on Edge.Cuts layer; footprint placement guided by ratsnest (unrouted-connection lines); routing tracks; vias for layer changes; copper zones (net-associated filled regions, thermal reliefs); DRC (clearance, shorts, schematic-layout mismatch, unrouted); 3D viewer; fabrication outputs (Gerber layers + drill files).
- **Schematic↔PCB sync**: forward update is manual and designer-controlled; changes made in board can be pushed back to schematic.
- **Libraries**: symbol libraries and footprint libraries are separate; global vs project library tables; Symbol Editor and Footprint Editor for creating symbols/footprints; linking symbols ↔ footprints ↔ 3D models.
- **Simulation**: integrated SPICE simulator.
- **Suite structure**: Project Manager, Schematic Editor, PCB Editor, Symbol Editor, Footprint Editor, Gerber Viewer, Drawing Sheet Editor, Calculator Tools, CLI.

### Altium Designer (electronic pole) — evidence layer A (Tier 2 official product page)

- Self-positioning: "The Industry's Leading PCB Design Software"; "an integrated, user-friendly tool incorporating everything from schematics and layout to simulation and analysis."
- **Unified Design Environment and Data Model**: "Create electronic designs from schematic capture to final design documentation and manufacturing files – all in one intuitive interface and unified data model."
- **Routing**: "smart interactive routing" for high-speed/dense layouts; assistive layout (reusable blocks, snippets, layout replication) "keeping schematic and PCB fragments synchronized."
- **Integrated analysis**: SPICE simulation, power analysis, signal integrity "within Altium Designer."
- **PCB co-authoring**: multiple engineers designing different parts of the same PCB simultaneously.
- **Multiboard**: "managing multiboard PCB interconnects in one environment, validating 3D assembly, and accelerating release with MCAD synchronization."
- **Constraint management**: "spreadsheet-like, object-based constraint editor" over nets and design objects.
- **Complexity features**: HDI, rigid-flex (configurable substacks, controlled bends), wire bonding, 3D-MID.
- **Data management**: versioning/revisioning with "visual change comparison between schematics, layouts, BOMs, and gerbers"; centralized component/library management with templates, lifecycles, where-used; supply-chain data (pricing, availability, risk) from providers.
- **Harness design**: "Design harnesses directly within the familiar Altium environment."
- **ECAD-MCAD**: connection to MCAD tools, Ansys, PLM systems.
- Platform packaging: Altium Designer delivered within Altium Develop / Agile Teams / Agile Enterprise (cloud platform tiers).

### Zuken E3.series (electrical pole) — evidence layer A (Tier 2 product pages) + S3/S6

- Self-positioning: "Electrical Wiring, Control Systems and Fluid Engineering" — "a leading single-platform solution to take electrical and fluid control designs from concept to manufacture."
- Scope: "functional design, detailed schematics (electrical and fluid), wiring and tubing diagrams, through to control cabinet and wire harness layout in 2D and 3D."
- **Object-oriented database**: "All applications are driven by an intelligent database that enables electrical and logical checks that ensure correct connections by design"; "any update made in one part of the design is automatically reflected across all related documents and views."
- **E3.schematic** (core module): "electrical system design, including schematic diagrams, terminal plans, and PLC documentation... real-time design rule checks and a smart parts library"; hierarchical design with functional blocks.
- **E3.cable**: "design and document cable plans and cable harness drawings... combine individual wires into multicores or cable bundles, add shielding and twisted pair structures... automatically display them in the schematic."
- **E3.panel**: "layout components within control cabinets in both 2D and 3D. The signal logic is inherited from the E3.schematic circuit diagram. Wires can be routed automatically through the control cabinet"; links to wire-processing machines (automatic strip/crimp/mark).
- **E3.formboard**: wire-harness formboard documentation (1:1 manufacturing drawing). **E3.topology**: wiring topology design. **E3.fluid**: hydraulic/pneumatic/cooling/lubrication systems, standalone or mixed with electrical.
- **Checks**: E3.eCheck (dedicated checking module); real-time design rule checks in schematic.
- **Component library**: smart parts library; Zuken Component Cloud; E3.series Component Editor (symbols + components creation, per First Steps chapter list).
- **Manufacturing outputs**: terminal plans, reports (E3.ReportGenerator), wiring diagram generation, formboard, export to wire-processing machines (E3.ExportToKomax), assembly cockpits (E3.AssemblingCockpit, E3.WiringCockpit, E3.WiringChecks).
- **Data management**: DS-E3 — WIP design data management, versioning, release process, design re-use, where-used traceability, PLM/PDM integration, component sync with supply-chain partners.
- **MCAD integration**: E3.RoutingBridge (harness data into MCAD for 3D routing, feedback back), E3.3DTransformer; "streamline the creation of digital twins."
- **Collaboration**: E3.enterprise (real-time multi-user project collaboration), E3.ConnectivityBrowser, viewers (E3.viewer free viewer, E3.redliner markup).
- **Industries**: industrial machinery, special vehicles, automotive, aerospace.
- Vendor-internal taxonomy (S6): Zuken's own site separates "电子设计（EDA）" (CR-8000 PCB design) from "电气CAD" (E3.series electrical CAD) — i.e., even one vendor treats "EDA"=electronic/PCB and "electrical CAD"=E3.series as distinct product families.

### EPLAN (electrical pole) — evidence layer A (Tier 2, homepage only — limited)

- Self-positioning: "the leading software for electrical engineering. We enable machine and panel builders as well as their suppliers to design automation and power systems more efficiently." Also building automation and energy sector.
- "Scalable, data driven solutions from assisted schematic creation to automated panel production."
- **Eplan Platform**: "brings together software solutions for various engineering disciplines. This creates a complete digital twin of the automation system for your machine or plant system."
- Products: Eplan Electric P8 (electrical engineering), Eplan Pro Panel (3D panel layout), Eplan Data Portal (component data), Eplan Preplanning.
- **Data Portal**: "more than 2.2 million static components, resulting in well over 4 million configurable components" — ready-to-use device data sets and engineering templates.
- Integration: "easily integrates with a wide range of engineering tools, ERP, PDM & PLM systems."
- Customer-story evidence: cable-length determination and routing-path display (cable pro D); "8 times faster creation of 3D panel layouts" (Pro Panel).
- Operational workflow detail NOT directly observed (subpages unreachable) — no precise claims made about EPLAN internals.

## Cross-product Comparison

| Aspect | KiCad | Altium Designer | E3.series | EPLAN |
|---|---|---|---|---|
| Design of record | project folder (schematic + board + libs) | project in unified data model | project in object-oriented database | project on platform ("digital twin") |
| Schematic capture | symbols + wires + net labels + power symbols | schematic capture in unified environment | E3.schematic: schematics, terminal plans, PLC docs | "assisted schematic creation" |
| Connectivity semantics | nets; same-name labels connect; net classes | nets; object-based constraint editor | "correct connections by design"; signal logic inherited downstream | data-driven device-centric model |
| Component library | symbol + footprint libraries, editors | centralized library, lifecycles, where-used, supply chain | smart parts library, Component Cloud, Component Editor | Data Portal (2.2M+ static / 4M+ configurable components) |
| Electrical checks | ERC (+ DRC on layout) | integrated analysis; constraints | real-time design rule checks; E3.eCheck | (not directly observed) |
| Physical layout surface | PCB Editor (outline, footprints, tracks, vias, zones) | PCB layout (routing, HDI, rigid-flex, multiboard) | E3.panel (cabinet 2D+3D, auto wire routing) | Pro Panel (3D panel layouts) |
| Schematic↔layout sync | manual forward update + push back | synchronized fragments/blocks | automatic — one database, all views update | platform data model |
| Downstream deliverables | BOM, Gerber + drill files | manufacturing files, documentation | terminal plans, reports, formboard, wire-machine export | automated panel production data |
| Simulation | SPICE | SPICE, SI, power | electrical simulation (listed) | — |
| Harness/cable | harness feature (newer) | harness design feature | E3.cable (multicores, shields, twisted pairs), formboard, topology | cable length determination |
| Fluid systems | — | — | E3.fluid | — |
| PLC | — | — | PLC documentation, PLCBridge | automation/power systems focus |
| MCAD integration | 3D viewer | MCAD sync, 3D assembly validation | RoutingBridge / 3DTransformer | engineering-tool integration, Pro Panel 3D |
| Data management | project files + backups | versioning, change comparison, cloud | DS-E3 (WIP, versions, where-used, PLM) | ERP/PDM/PLM integration, cloud |
| Multi-user | — | PCB co-authoring | E3.enterprise real-time | collaboration |
| Audience | hobbyist → professional | professional electronics teams | machinery/vehicle/aerospace electrical teams | machine & panel builders |

### Stable commonalities (across all four, both poles)

1. Schematic capture is the design of record: symbol-based diagrams of components and their connections.
2. Connectivity is semantics, not geometry: the system maintains an electrical network (nets) implied by the drawing; named labels connect across pages; connectivity is queryable and checkable.
3. Designs are composed from a component/part library carrying electrical interfaces (pins) and part data.
4. The connected design generates downstream deliverables: parts lists (BOM), connection lists (netlist/wire lists), and manufacturing/installation artifacts (fabrication outputs / terminal plans / panel production data).
5. A physical-layout surface realizes the connectivity in physical arrangement (PCB / cabinet / harness) — form differs by pole, existence does not.
6. Connectivity/design-rule checking is built in.
7. Integration outward: MCAD (mechanical context), PLM/ERP (part and lifecycle data), manufacturing equipment.

### Pole-specific differences

- **Electronic pole** (KiCad, Altium): objects are symbols/footprints/pads/tracks/vias/zones/stackup; deliverables are Gerber/drill; checks are ERC/DRC; simulation is SPICE-class; the board is the manufacturing target.
- **Electrical pole** (E3.series, EPLAN): objects are devices/terminals/cables/wires/plc-I/O; deliverables are terminal plans, wire lists, panel layouts, formboards; the cabinet/harness/machine wiring is the manufacturing target; fluid (hydraulics/pneumatics) appears as an adjacent discipline in the same tool family.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Component Library (parts with pin-level electrical interfaces + part data)
└── Schematic Capture (symbol-based design of record)
    └── Connectivity Semantics (nets: the electrical network implied by the drawing,
        addressable across pages via named labels)
        └── Generated Deliverables (connection lists / parts lists /
            manufacturing or installation artifacts derived from the connected design)
```

Four jointly-held properties:

1. **Schematic capture as design of record** — the engineer authors symbol-based diagrams of an electrically-connected system. Remove → drawing/diagramming tool.
2. **Connectivity semantics (nets)** — drawn connections carry electrical meaning; the system maintains the pin-to-pin network, not lines on a page. Remove → vector drawing application.
3. **Component library with electrical interfaces** — designs are built from catalogued parts with pins and part data, not freehand shapes. Remove → generic illustration.
4. **Deliverable generation from the connected design** — netlist/wire lists, BOM, and manufacturing/installation outputs are derived, not drawn. Remove → static illustration of a circuit.

Jointly-held is load-bearing: schematic + nets without library and deliverables = a netlist sketch tool; library + deliverables without schematic capture = a parts/PLM system.

### L1 — Common Mature Structure

Present across the sample (or across a whole pole) but not required to recognize the Type:

- physical-layout surface realizing the nets (PCB editor / cabinet-panel layout / harness formboard) with schematic↔layout synchronization
- connectivity and design-rule checking (ERC/DRC-class)
- multi-sheet and hierarchical schematics with cross-references
- unique device tagging / reference designators
- simulation (SPICE-class in the electronic pole; electrical simulation in the electrical pole)
- MCAD integration and 3D visualization
- design data management (versions, where-used, PLM/ERP integration)
- report generation (BOM, wire/terminal schedules)
- multi-user collaboration (co-authoring / real-time)

### L2 — Variant / Optional Structure

Depends on pole, industry, scale, deployment:

- pole object families: cables/harnesses (multicores, shields, twisted pairs), terminals, PLC I/O documentation, fluid schematics (electrical pole) vs footprints, copper zones, vias, stackups, net classes, HDI/rigid-flex (electronic pole)
- supply-chain integration (live pricing/availability/risk; vendor-maintained component data portals)
- cloud platforms and co-authoring tiers
- free viewers / markup roles for non-designers
- manufacturing-machine integration (wire processing: strip/crimp/mark, machine-specific export)
- preplanning / functional-design layers upstream of detailed schematics
- open-source vs commercial delivery; file-based vs database-backed projects

### L3 — Vendor-specific Structure

(remains in Research Notes)

- KiCad: file formats (.kicad_pro/.kicad_sch/.kicad_pcb), sym-lib-table/fp-lib-table, PWR_FLAG, ratsnest/zone-refill semantics, hotkey model, Gerber Viewer as separate app.
- Altium: Altium 365 packaging (Develop / Agile Teams / Agile Enterprise), Octopart supply-chain integration, IPC certification pathways, 3D-MID.
- Zuken: E3.series module naming (E3.schematic/cable/panel/fluid/formboard/topology/eCheck), DS-E3/DS-CR, Smart Cabinet Building Initiative, Komax export, E3.enterprise.
- EPLAN: Eplan Platform / Electric P8 / Pro Panel / Data Portal / Preplanning naming, Rittal partnership, marketing counts (525,000 users; 19 of 20 largest automakers).

## Rejected Findings

- "ECAD/EDA = PCB design" — rejected as the whole-Type definition: the electrical pole (E3.series, EPLAN) has no PCB objects at all. PCB design is one pole's physical-layout realization.
- "ECAD/EDA includes IC/semiconductor design" — rejected for this leaf: different objects (RTL, verification, place-and-route), separate directory leaf; Zuken's own site separates the two families.
- "Simulation is definitional" — rejected: SPICE is common in the electronic pole, absent/optional in the electrical pole; the design of record is the schematic, not a solver study.
- "3D is definitional" — rejected: KiCad's 3D is a viewer; EPLAN's Pro Panel is 3D; but 2D-only electrical design remains fully within the Type.
- "Database-backed single source is definitional" — rejected: KiCad is file-based and still squarely the Type; database-vs-files is an implementation axis.
- "Fluid/hydraulics design is part of the Type" — kept as L2 variant: only the electrical pole shows it, and only in one sampled vendor family; it rides on the same schematic+connectivity core.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove to cross the boundary) |
|---|---|---|
| Diagramming Application | visually adjacent | diagramming draws shapes/connectors with no pin/net semantics, no electrical part library, no netlist/BOM generation. Remove connectivity semantics + electrical library + deliverables → diagramming. |
| Mechanical CAD | co-discipline | MCAD's design of record is geometry (solids/surfaces); ECAD/EDA's is connectivity. MCAD integration is a bridge (harness routing, panel fit), not the core. |
| PCB Design (separate leaf) | pole overlap | the electronic pole's products self-identify as "PCB design software" (Altium; Zuken CR-8000). PCB Design is best understood as the board-layout-centered realization of the same family. Directory overlap — flagged for joint review. |
| Semiconductor Design Platform (separate leaf) | broader-industry namesake | "EDA" in the industry's broadest sense includes IC design (RTL→GDSII); that is a different object world and a separate leaf. This leaf's center of gravity is board/system-level electrical & electronic design. |
| Electrical Design Application (separate leaf) | probable alias | EPLAN and Zuken market exactly this Type's electrical pole as "electrical design software." Likely alias of the electrical pole — flagged for joint review. |
| CAE / Engineering Simulation | capability overlap | simulation is an embedded capability (SPICE); CAE's design of record is a solver study, not a connected design. |
| PLM / BOM Management | downstream consumer | BOM is generated output here; managing BOMs/lifecycle across the product is PLM territory. Design-data management modules (DS-E3, Altium 365) sit at this seam. |
| CAM | downstream handoff | fabrication outputs (Gerber/drill) are generated here; CAM transforms them into machine tooling. |

## Historical / Market-Sample Check

Would older products still fit the L0 definition? Yes:

- 1980s-generation schematic-capture + PCB tools (the DOS/PC era from which the sampled commercial vendors descend) already had symbol libraries, nets, netlists, BOM export, and Gerber output — all four L0 properties, none of the modern cloud/AI/co-authoring features.
- Electrical-pole CAD lineages (electrical schematics + wire lists + terminal diagrams on CAD) satisfy the same core without panels-in-3D or data portals.
- The definition therefore does not overfit to the current cloud-connected, supply-chain-integrated market form.

## Uncertainties

1. EPLAN operational workflow detail unverified (homepage-only evidence) — EPLAN-specific behavior kept out of precise claims.
2. SOLIDWORKS Electrical / AutoCAD Electrical (MCAD-embedded pole) unobserved — the claim "electrical CAD is commonly embedded in MCAD ecosystems" is plausible but unverified in this sample.
3. E3.series documentation sub-chapters not fetched — electrical-pole operational detail rests on Tier 2 product pages.
4. Whether the directory should merge "Electrical Design Application" into this leaf, and how "PCB Design" should be positioned relative to it — needs joint review; recorded in STATUS.md Boundary Issues.
5. Semiconductor-EDA boundary asserted from directory structure + one vendor's own categorization, not from sampling Cadence/Synopsys docs.

## Final Synthesis

ECAD / EDA is one Application Type with two market poles sharing a single defining core. The design of record is a symbol-based schematic; its meaning is the electrical connectivity (nets) it expresses; designs are composed from a component library carrying pin-level electrical interfaces and part data; and the connected design drives generated deliverables — connection lists, parts lists, and manufacturing/installation artifacts. Around this core, mature products add a physical-layout surface (PCB or cabinet/harness, depending on pole), connectivity/design-rule checking, simulation, MCAD/PLM integration, and design-data management. The electronic pole realizes the core for printed circuits (symbols/footprints/tracks → Gerber); the electrical pole realizes it for machines, panels, vehicles and harnesses (devices/terminals/cables → terminal plans, wire lists, panel production). The directory's neighboring leaves (PCB Design, Electrical Design Application, Semiconductor Design Platform) map onto: a pole-level realization, a probable alias, and a deliberately excluded deeper domain, respectively.
