# Research Notes — Electrical Design Application

Research date: 2026-09-08

## Research Goal

Understand what the market sells under the "electrical design software / electrical CAD" label as an Application Type: what the design of record is, what objects exist inside it (devices, wires, cables, terminals, PLC I/O, panels, harnesses), how engineers work in it, what deliverables it generates — and to conduct the joint review flagged by the ecad-eda pass (2026-09-07): is "Electrical Design Application" an alias of the electrical pole of ECAD/EDA, a distinct Type with its own core, or something else?

## Initial Boundary (working hypothesis before research)

- Hypothesis: products marketed as "electrical design software" are electrical-engineering CAD for machines, control cabinets, vehicles/harnesses and installations — symbol-based schematics whose meaning is wiring connectivity, plus derived deliverables (wire lists, terminal plans, BOM, panel layouts). This is the electrical pole already documented inside the ECAD/EDA leaf.
- Likely confusions:
  - vs ECAD/EDA (family overlap — the joint-review question)
  - vs PCB Design (the electronic pole's realization)
  - vs MEP Design (building services)
  - vs power-system analysis tools (ETAP-class — studies on network models, not a wiring design of record)
  - vs Diagramming Application (visual similarity, no electrical semantics)
- Unknowns: exact market coverage of the label; whether the electrical pole carries any defining structure beyond the shared four-part core (terminals/cables/structure as core vs common); how the building-installation edge relates to MEP Design.

## Research Questions

1. What do vendors calling their products "electrical design software" actually sell?
2. What is the design of record (project → pages/folios → devices and wires)?
3. Core objects: device, symbol/element, terminal, wire/conductor, cable/core, PLC I/O, function/location structure, cabinet/panel?
4. How do wires and cables get defined, designated, numbered?
5. What deliverables are generated (wire/conductor lists, terminal plans, BOM/nomenclature, panel data, formboards, machine data)?
6. What checks exist?
7. What is the physical-realization loop (cabinet layout 2D/3D, wire routing, lengths)?
8. What multi-discipline extensions exist (fluid, P&I, building automation, installation)?
9. What integrations exist (MCAD, PLM/ERP, manufacturing machines; component data repositories)?
10. Joint review vs ECAD/EDA: alias, sibling, or distinct Type?
11. What does the minimal end of the market look like — which structures survive without enterprise machinery?

## Representative Products

Selected for market representation + documentation quality + different philosophy + different customer level, all within the "electrical design / electrical CAD" label:

| Product | Segment | Philosophy | Evidence level |
|---|---|---|---|
| Zuken E3.series | enterprise; machinery, special vehicles, automotive, aerospace, harness | object-oriented single platform, concept → manufacture | Tier 2 product pages (rich) |
| EPLAN (Eplan Platform / Electric P8 / Pro Panel) | enterprise market leader; machine & panel builders | platform + device-data portal, "digital twin" | Tier 2 homepage only (subpages unreachable) |
| WSCAD ELECTRIX | European mid-market; multi-discipline | all-in-one suite, ease of use, free parts repository | Tier 2 site (good detail) |
| QElectroTech | free / open source; minimal standalone | project + folio diagram editor with element collections | Tier 1 official manual (TOC-level) |

Named but not directly observed: SOLIDWORKS Electrical, AutoCAD Electrical (both named by WSCAD's own case study as same-category products it replaces; both unreachable in this pass and in the prior ECAD/EDA pass).

Deliberately NOT sampled: KiCad / Altium (electronic pole — documented by the ecad-eda pass, used here only as joint-review cross-reference); ETAP/SKM-class power-system analysis (different object world — studies on network models); IGE+XAO SEE Electrical, ProfiCAD (fetches failed, marginal value).

## Sources

| # | Source | Tier | Result |
|---|---|---|---|
| S1 | Zuken — E3.series product page + module map (zuken.com/en/product/e3series/) | 2 | Page titled "Electrical Design Software"; full module map; core product descriptions; ecosystem pages. Fetched 2026-09-08. |
| S2 | EPLAN — homepage (eplan.com/en/) | 2 | Positioning, platform concept, product names, Data Portal claims, customer stories. Fetched 2026-09-08. Product subpages failed again: /en/products/electric-p8 (404), /en/products/eplan-electric-p8/ (404) — source abandoned. |
| S3 | WSCAD — wscad.com/en/ | 2 | Self-labeling "electrical CAD software"; discipline modules; parts repository; competitor names in case studies. Fetched 2026-09-08. |
| S4 | QElectroTech — qelectrotech.org + official documentation (qelectrotech.github.io/qelectrotech-doc) | 1 | Feature description, GPL license, full user-manual TOC (project / folio / element / conductor / reports / export structure). Fetched 2026-09-08. |
| S5 | ecad-eda pass — research/ecad-eda.md (2026-09-07) | — | Electronic-pole cross-reference (KiCad, Altium) and the joint-review flag this pass discharges. |
| S6 | G2 category "Electrical Design" (g2.com/categories/electrical-design) | 3 | FAILED — 403. Abandoned. |
| S7 | Autodesk — AutoCAD Electrical product page + online help | 2 | FAILED — 403 (product page), 404 ×2 (help URLs). Abandoned. |
| S8 | SOLIDWORKS — solidworks.com/product/solidworks-electrical | 2 | FAILED — timeout (repeat of prior session's failures). Abandoned. |
| S9 | ProfiCAD (profcad.com) | 2 | FAILED — transport error ×2. Abandoned. |
| S10 | IGE+XAO (ige.com) | 2 | FAILED — transport error. Abandoned. |

Source-access limitations: SOLIDWORKS Electrical and AutoCAD Electrical were observed only through a competitor's naming (WSCAD case study); EPLAN evidence is positioning-level; the market-category composition claim (which products the label covers) rests on vendor self-labeling plus one competitor naming, not on a directory source. Assertions calibrated accordingly; vendor marketing counts kept attributed and out of the final document.

## Product Observations

### Zuken E3.series — evidence layer A (Tier 2, rich)

- Page title: **"Electrical Design Software"**; alt-text labels: "electrical CAD software ... for electrical designers". Self-description: "Electrical Wiring, Control Systems and Fluid Engineering" — "a leading single-platform solution to take electrical and fluid control designs from concept to manufacture."
- Scope: "functional design, detailed schematics (electrical and fluid), wiring and tubing diagrams, through to control cabinet and wire harness layout in 2D and 3D."
- "All applications are driven by an intelligent database that enables electrical, and logical checks that ensure correct connections by design"; "any update made in one part of the design is automatically reflected across all related documents and views."
- **E3.schematic** (core module): "electrical system design, including schematic diagrams, terminal plans, and PLC documentation"; real-time design rule checks; smart parts library; hierarchical design with functional blocks.
- **E3.cable**: "design and document cable plans and cable harness drawings"; "combine individual wires into multicores or cable bundles, add shielding and twisted pair structures"; automatically displayed in the schematic. (Blog series: "Dynamic Cables: Cores, Shields, Twisted Pairs" — schematics, reports, and formboard outputs stay consistent.)
- **E3.panel**: "layout components within control cabinets in both 2D and 3D. The signal logic is inherited from the E3.schematic circuit diagram. Wires can be routed automatically"; links to wire-processing machines ("automatically stripped, crimped and marked").
- **E3.formboard** (1:1 harness manufacturing drawing), **E3.topology** (wiring topology), Harness Builder, E3.HarnessAnalyzer, E3.WiringSystemLab.
- **E3.fluid**: hydraulic, pneumatic, cooling, lubrication systems; standalone fluid schematics or mixed fluid+electrical designs.
- Checks: E3.eCheck (dedicated checking module); real-time design rule checks in the schematic.
- Libraries: smart parts library; Zuken Component Cloud; E3.series Component Editor.
- Data management: DS-E3 (WIP design data management, versioning, release process, re-use, "where-used" traceability, PLM/PDM sync, supply-chain component sync); E3.RevisionManagement (revision compare).
- Collaboration: E3.enterprise (real-time multi-user project collaboration), E3.ConnectivityBrowser; viewers (E3.viewer free, E3.ViewerPlus, E3.redliner markup).
- Manufacturing: E3.ExportToKomax, E3.ReportGenerator, E3.WiringDiagramGenerator, E3.AssemblingCockpit, E3.WiringCockpit, E3.WiringChecks.
- MCAD: E3.RoutingBridge (harness data → MCAD 3D routing with feedback), E3.3DTransformer.
- Electrical simulation listed among tour capabilities ("electrical simulation, detailed schematic, wiring diagram, cabinet layout, formboard, reports, and manufacturing documentation").
- Industries: industrial machinery, special vehicles, automotive, aerospace. Cabinets described as "the nerve center of complex control systems like switchgear, PLCs, motor control centers, and power distribution systems."
- Vendor-internal taxonomy: the same vendor's navigation separates "Electrical / Fluid Design" (E3.series) from "PCB Design / IC Packaging" (CR-8000, eCADSTAR).

### EPLAN — evidence layer A (Tier 2, homepage-level — limited)

- Positioning: "Eplan provides the leading software for electrical engineering. We enable machine and panel builders as well as their suppliers to design automation and power systems more efficiently." Extends to building automation and the energy sector.
- "Rely on our scalable, data driven solutions from assisted schematic creation to automated panel production."
- **Eplan Platform**: "brings together software solutions for various engineering disciplines. This creates a complete digital twin of the automation system for your machine or plant system."
- Products: Eplan Electric P8 (electrical engineering), Eplan Pro Panel (3D panel layouts), Eplan Data Portal (device data), Eplan Preplanning. Site nav discipline categories: Electrical Engineering, Basic Engineering, Panel Building, Cabling.
- Data Portal: "millions of ready-to-use device data sets and engineering templates" (page cites 2.3M static / well over 4M configurable components — vendor marketing counts, kept attributed).
- Customer stories: NIO (electrical design for production lines); "The system reliably determines the cable lengths ... routing paths are displayed in the viewer" (cable pro); "8 times faster creation of 3D panel layouts" (Pro Panel).
- Operational workflow detail NOT directly observed — no precise EPLAN-internal claims made anywhere.

### WSCAD ELECTRIX — evidence layer A (Tier 2, good)

- Self-labeling: "electrical CAD software"; headline claims "The first and only AI-powered electrical CAD" (ELECTRIX AI, AI Copilot, customer testimonials about automated checking and faster project completion).
- "All-in-one electrical CAD solution": "No matter if you are designing piping & instrumentation diagrams, fluid power or electrical schematics, cabinet engineering, building automation or electrical installation — WSCAD Software is the right tool for you. It connects all the engineering data on one common platform. No data transfer or conversion, no quality loss." "It works in small projects or big ones with user rights, different languages and international teams."
- Discipline modules:
  - **Electrical Engineering** — "Wiring diagram design"; "design medium and low voltage systems for machines, plants, industrial automation and building automation."
  - **Cabinet Engineering** — "Professional cabinet design and wire routing"; "panel design in 2D and 3D ... precise and optimal placement of components, collision checks or the calculation of wire lengths/routes."
  - **Piping & Instrumentation** — P&ID design, "process engineering and measuring point management."
  - **Fluid Engineering** — pneumatic and hydraulic systems.
  - **Building Automation** — "layouts and schematics for measurement control technology."
  - **Electrical Installation** — "Installation diagrams and distribution planning"; building system technology, medium- and low-voltage installations, antenna and fire alarm systems.
- Project Wizard addon; WSCAD Apps; education licenses; user rights for teams.
- **wscaduniverse.com**: free parts repository — "more than 2.2 million parts" from 457 manufacturers in WSCAD/EDZ/3D STEP formats (vendor counts, attributed).
- Case-study quote (Cummins): "We decided to replace AutoCAD Electrical and EPLAN and standardise our worldwide electrical engineering on WSCAD software" — direct competitor-naming evidence that AutoCAD Electrical and EPLAN belong to the same product category.
- Testimonial (HUG MSR-Technik): "we receive a near-finished layout that can be passed directly to CNC machining" — cabinet layout feeding manufacturing machinery.
- Industries: machinery equipment, plant engineering, building automation, electrical trade; "more than 35 years", "more than 40,000 users in over 100 countries" (vendor counts).

### QElectroTech — evidence layer A (Tier 1 manual, TOC-level)

- Self-description: "QElectroTech, or QET in short, is a free software to create industrial complex electric diagrams" — also reused for hydraulics, pneumatics, domotics, P&ID, photovoltaic. GNU/GPL; Windows/macOS/Linux; default element collection "over 8000 symbols".
- Manual structure (Tier 1 evidence of the minimal object model):
  - **Project** — create/open/save/close/clean; project properties; auto-numbering properties.
  - **Folio** = diagram sheet; types: **single line diagram, multiline diagram, control diagram**; title blocks (drawing-frame templates with their own collections); folio referencing; cross-reference settings.
  - **Element** = symbol; types: simple, **master, slave** (coordinated pairs, e.g. coil/contacts), **terminal block**; collections (QET default / user / project); element editor with graphic parts incl. **terminal**; element numbering; master/slave cross references (bind/untie/show linked).
  - **Conductor** = wire; single-line vs multiline conductors; conductor properties; **conductor numbering**.
  - Schema editing: add/edit elements, create/modify conductors, conductor text, text fields, search/replace across the project.
  - **Drawing**: "Design mounting plate", "Design Local Control Panel (LOP)" — 2D panel-layout surfaces exist even in the minimal tool.
  - **Reports**: summary; **nomenclature** (parts list); **conductor list**; **I/O list**.
  - **Export and print**: print project; PDF; export schema; export nomenclature; **export wires**; export internal project database.
- No PLC navigators, data portals, or multi-user machinery — the minimal pole of the market.

### Cross-reference (electronic pole, from the ecad-eda pass)

- KiCad and Altium Designer share the same four-part core (library with pin-level interfaces → schematic capture → nets → generated deliverables) with a different physical realization (board instead of cabinet/harness). Used here only to ground the joint review, not re-researched.

## Cross-product Comparison

| Aspect | E3.series | EPLAN | WSCAD | QElectroTech |
|---|---|---|---|---|
| Self-label | "Electrical Design Software" / electrical CAD | "software for electrical engineering" | "electrical CAD software" | "free electrical diagram software" |
| Design of record | project in object-oriented database | platform project ("digital twin") | project on one common platform | project with folios (diagram sheets) |
| Schematic | E3.schematic: schematics, terminal plans, PLC docs; hierarchical | "assisted schematic creation" | wiring diagram design (medium/low-voltage systems) | folios: single-line, multi-line, control diagrams |
| Connectivity | "correct connections by design"; one database, all views update | data-driven platform | one platform, no data conversion | conductors between element terminals; numbering |
| Device/symbol library | smart parts library + Component Cloud | Data Portal (millions of device data sets) | wscaduniverse (2.2M parts, 457 manufacturers, free) | 8000+ symbol collection + user/project collections |
| Terminals | terminal plans in the core module | (not directly observed) | (not detailed on homepage) | terminal blocks as element type |
| Cables/harness | E3.cable (multicores, shields, twisted pairs), formboard, topology | cable-length determination (customer story) | (not on homepage) | — |
| Cabinet/panel | E3.panel 2D+3D, auto wire routing, wire-machine links | Pro Panel 3D; "automated panel production" | Cabinet Engineering 2D/3D, collision checks, wire lengths/routes | mounting-plate design (2D) |
| PLC | PLC documentation, PLCBridge | automation/power-systems focus (positioning) | (not detailed) | I/O list report |
| Checks | real-time design rule checks; E3.eCheck | (not observed) | (not detailed; AI-check testimonials) | (not detailed) |
| Reports/deliverables | terminal plans, reports, formboard, wiring diagrams, machine export | panel production data | wire lengths/routes; CNC-ready layouts (testimonial) | nomenclature, conductor list, I/O list, export wires, PDF/print |
| Multi-discipline | fluid (E3.fluid) | building automation, energy (positioning) | P&ID, fluid, building automation, electrical installation | hydraulics/pneumatics/domotics reuse |
| Data management | DS-E3, revision management, where-used | ERP/PDM/PLM integration claimed | user rights, international teams | local project database export |
| Multi-user | E3.enterprise real-time | collaboration claimed | teams with user rights | — |
| MCAD | RoutingBridge / 3DTransformer | engineering-tool integration claimed | 3D STEP part data | — |
| Market level / price | enterprise | enterprise | mid-market ("2-3 times more favourable") | free, GPL |
| AI | automation/API (Python) | AI innovations (nav only) | ELECTRIX AI Copilot | — |

### Stable commonalities (all four, spanning enterprise → minimal)

1. Self-identification as electrical (CAD) design / diagram software for wiring electrically connected systems.
2. The schematic/diagram is the design of record: symbol-based drawings of devices and their connections, in single-line and multi-line forms, on titled pages.
3. Designs are composed from a device/symbol library carrying connection points (terminals) and part data; dedicated symbol/element editors; large shared collections or vendor-operated data repositories.
4. Connectivity is semantic: wires/conductors carry electrical meaning, connections are tracked as data, designations/numbering are automatic, and edits propagate to dependent documents and views.
5. Generated deliverables: parts lists/nomenclature, conductor/wire lists, I/O lists, terminal documentation, PDF/print drawing sets; in mature products, panel layouts, formboards, and machine-targeted manufacturing data.
6. A physical-realization surface exists in every sample, including the minimal one: cabinet/panel layout (2D, or 2D+3D) with wire routing/lengths; signal logic inherited from the schematic.
7. Outward integration: MCAD (placements, harness routes), PLM/ERP (part data), manufacturing machines; component-data repositories as the supply side.
8. Discipline extensions ride the same core: fluid, P&I, building automation, electrical installation.

### Electrical-pole specifics (vs the electronic pole documented in ecad-eda)

- Object families: devices, terminals, wires, cables/cores, shields, twisted pairs, PLC I/O, function/location structure — instead of footprints, copper, stackups.
- Deliverables: wire lists, terminal plans, cabinet layouts, formboards, assembly work instructions, wire-processing machine data — instead of Gerber/drill.
- The schematic remains the source of the signal logic that the physical views inherit.

## Canonical Abstraction

### L0 — Defining Invariant

The same four-part core as the ECAD/EDA family (the joint-review finding), realized for electrical engineering:

```text
Device/Symbol Library (parts with connection points + part data)
└── Wiring Schematic (design of record; single-line and multi-line diagram pages)
    └── Connectivity Semantics (wires/conductors as electrical meaning,
        designated and numbered, queryable and checkable)
        └── Generated Deliverables (wire/conductor lists, parts lists,
            terminal documentation, panel/harness production data
            derived from the connected design)
```

Four jointly-held properties:

1. **Device library with connection points** — designs are composed from catalogued devices/symbols carrying terminals and part data. Remove → drawing tool.
2. **Wiring schematic as design of record** — engineers author symbol-based diagrams of the wired system. Remove → parts/library system without design authoring.
3. **Connectivity semantics** — drawn connections are electrical data (designated wires/conductors), not lines; the system tracks what is connected to what across pages. Remove → vector drawing application.
4. **Generated deliverables** — lists and production artifacts are derived from the connected design, never hand-drawn. Remove → static illustration of a wiring diagram.

Jointly-held is load-bearing: schematic + connectivity without library and deliverables = a sketch tool; library + deliverables without schematic authoring = a parts system. All four observed in all four sampled products, including the minimal one (QElectroTech: elements with terminals, folios, conductors with numbering, nomenclature/conductor/I-O lists).

### L1 — Common Mature Structure

Present across the sample (or in all mature/enterprise products) but not required to recognize the Type:

- unique device designations with automatic numbering (devices and wires/conductors)
- cross-references between coordinated symbols (master/slave pairs such as coil and contacts) and across pages
- terminal management and terminal plans; cable/core management (bundles, shields, twisted pairs)
- PLC I/O documentation and I/O lists
- cabinet/panel layout in 2D and 3D inheriting the schematic's signal logic; wire routing and length calculation; collision checks
- connectivity/design-rule checking (real-time or report-based)
- structured, multi-page, often hierarchical projects with title blocks and page referencing
- report generation beyond BOM (wire lists, I/O lists, terminal schedules)
- MCAD integration; PLM/ERP integration; design data management (versions, release, where-used)
- multi-user collaboration; free viewers/markup for non-designers
- shared or vendor-operated component-data repositories

### L2 — Variant / Optional Structure

Depends on industry, scale, discipline scope, deployment:

- discipline extensions: fluid (hydraulic/pneumatic), piping & instrumentation, building automation, electrical installation (building distribution, fire alarm/antenna systems)
- harness ecosystems: wiring topology, formboards, harness builders/analyzers, wire-processing machine integration, assembly work-instruction cockpits
- electrical simulation
- MCAD-embedded companion products (electrical design sold as a mechanical-suite companion)
- AI assistance (copilots, automated checking)
- deployment/posture: enterprise platform vs standalone minimal tools; free/open-source; file-based vs database-backed; cloud
- education licensing, free trials/viewers as adoption funnels

### L3 — Vendor-specific Structure

(remains in Research Notes)

- Zuken: E3.schematic/cable/panel/formboard/topology/fluid/eCheck module naming, Component Cloud, DS-E3, E3.enterprise, RoutingBridge, ExportToKomax, WiringCockpit/AssemblingCockpit, Smart Cabinet Building Initiative.
- EPLAN: Eplan Platform / Electric P8 / Pro Panel / Data Portal / Preplanning naming; marketing figures (525,000 users; 19 of 20 largest automakers; 2.3M components) — attributed counts only.
- WSCAD: ELECTRIX AI, wscaduniverse.com (457 manufacturers, 2.2M parts), Project Wizard, discipline-module naming.
- QElectroTech: QET element/collection/folio terminology; title-block editor; internal-project-database export.
- Market-structure facts: WSCAD's own case study names AutoCAD Electrical and EPLAN as same-category products it replaces (evidence for family breadth, not for those products' internals).

## Rejected Findings

- "Electrical design software is a distinct Type from ECAD/EDA with its own defining core" — rejected on evidence: all four sampled products exhibit the same four-part core; the pole difference lies in object families and deliverables, not in the defining structure.
- "Electrical design = power-system analysis (load flow, short-circuit, arc flash class)" — rejected: that is a study/simulation object world (network model, scenarios, protection studies) closer to CAE / Engineering Simulation; no such study objects appear in the sampled design of record.
- "Electrical design = building electrical (MEP)" — rejected as identity: building-installation modules exist in this family (WSCAD Electrical Installation), but the Type's center of gravity is the wiring design of record for machines/panels/vehicles/installations; building-model-anchored services design is the MEP Design leaf's center.
- "3D is definitional" — rejected: the minimal sampled product is 2D and squarely within the Type; 3D panel/harness is mature-market common, not defining.
- "Database-backed platforms / multi-user are definitional" — rejected: the file-based minimal tool passes the core.
- "Fluid/P&I modules are part of the Type" — kept as L2 variant: only some vendors, same core mechanics.
- "PLC documentation is definitional" — kept as L1 common (core-module description in enterprise products; I/O list in the minimal one); a minimal wiring-design tool without PLC work still fits the Type.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/what differs) |
|---|---|---|
| ECAD / EDA | JOINT REVIEW — pole-level alias/sibling | products marketed as "electrical design software" are exactly the electrical pole documented inside the ECAD/EDA leaf; defining core identical. Recommended outcomes: (a) fold this leaf into ECAD/EDA as its named electrical pole, or (b) keep both as sibling leaves with cross-reference (ECAD/EDA = combined family incl. the electronic pole; Electrical Design Application = the electrical-engineering pole, documented here). This pass documents the pole under this leaf's own name and does not silently resolve the directory. |
| PCB Design | family sibling (electronic realization) | board layout is the electronic pole's physical realization; different object world (footprints, copper, fabrication files). |
| Semiconductor Design Platform | namesake neighbor | IC design (RTL → GDSII) is a different object world; separate leaf. |
| MEP Design | edge overlap | building-services design anchored in the building model (geometry, coordinated with architecture/structure) vs wiring design of record; WSCAD's Electrical Installation module shows this family reaching into building installation while keeping the wiring-diagram center. Boundary asserted from directory structure + one module observation — not deep-researched. |
| CAE / Engineering Simulation | adjacent discipline | power-system studies (load-flow/short-circuit class) are solver studies on network models; here the design of record is the wiring schematic; simulation appears only as an embedded capability. |
| Diagramming Application | visual look-alike | no device libraries with terminals, no connectivity semantics, no derived lists. |
| Mechanical CAD | co-discipline | geometry design of record; receives device placements/harness routes through bridges. |
| PLM / BOM Management | downstream consumer | parts lists are generated output; product-level lifecycle is PLM territory; design-data management modules sit at this seam. |
| CAM / CNC Programming | downstream handoff | cabinet-layout and wire data feed panel manufacturing; CNC receives layouts for machining (WSCAD customer evidence). |

## Historical / Market-Sample Check

- Minimal pole (QElectroTech — free, GPL, current): project + folios + elements/conductors + reports — all four core properties with no enterprise machinery. The core is not overfit to enterprise platforms.
- Older/regional: electrical CAD lineages on desktop CAD since the 1980s–90s already delivered schematics + wire lists + terminal diagrams (consistent with the ecad-eda pass's findings); before CAD, the same structure existed on paper — schematic drawings with hand-maintained wire and terminal schedules (reasoning-based; no pre-CAD product sampled).
- The definition does not depend on AI, cloud, 3D, data portals, multi-user platforms, or any single region's symbol standards.

## Uncertainties

1. SOLIDWORKS Electrical and AutoCAD Electrical internals unobserved (unreachable across two passes); their family membership rests on market labeling + one competitor's naming, not direct documentation.
2. EPLAN operational detail remains homepage-level; no EPLAN-internal workflow claims made.
3. The "market-labeled product set" claim rests on vendor self-labeling + one competitor naming; the G2/Capterra category pages were unreachable (403), so category composition is not independently verified.
4. The exact directory resolution (fold vs sibling leaves) belongs to maintainers; this pass documents the pole and records both options in STATUS.md.
5. Building-installation edge vs MEP Design asserted from directory structure + one module observation; not deep-researched.
6. Sub-chapter operational documentation for E3.series/WSCAD not fetched (module-level pages only in some cases); module descriptions rest on Tier 2 product pages.

## Final Synthesis

The market label "electrical design software / electrical CAD" names the electrical-engineering pole of the ECAD/EDA design family. Its design of record is the wiring schematic — symbol-based single-line and multi-line diagrams of devices and their connections; its meaning is the wiring connectivity the drawing expresses (designated, numbered wires/conductors, tracked as data across pages); designs are composed from a device/symbol library carrying connection points and part data; and the connected design drives generated deliverables — wire/conductor lists, terminal documentation, parts lists, I/O lists, and, in mature products, cabinet/panel layouts, harness documentation, and machine-targeted production data. Mature products add the physical-realization loop (cabinet layout in 2D/3D inheriting the schematic's signal logic, wire routing and lengths, collision checks), connectivity/design-rule checking, PLC I/O documentation, MCAD/PLM/ERP integration, governed component-data repositories, and multi-user/data-management machinery. Discipline extensions (fluid, P&I, building automation, electrical installation) ride the same core.

Joint review vs ECAD/EDA: the defining core is identical — this leaf is a pole-level alias/sibling, not a distinct Type with a different core. The electrical pole's distinctness is real but sits at the L1/L2 level (object families, deliverables, audience), which supports keeping a separately-focused document but does not support two different definitions. Recorded in STATUS.md with both resolution options (fold as named pole vs keep as cross-referenced siblings).
