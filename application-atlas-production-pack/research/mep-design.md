# Research Notes — MEP Design

## Research Goal

Understand what an MEP Design application is as an Application Type: what the engineer's "world" consists of, what the design loop is, what calculations and rules are embedded, what deliverables leave the application, and where the boundary lies against neighboring Types (BIM Authoring, Architecture Design, Structural Engineering Design, Electrical Design Application, HVAC load-calculation tools, Building Energy Management).

## Initial Boundary

Working hypothesis at start:

- MEP Design = the engineer-facing authoring environment for designing building mechanical, electrical, and plumbing (and commonly fire-protection) systems: laying out physical components in a building context, sizing/verifying them by engineering calculation, and producing construction documentation.
- Likely confusions: generic BIM Authoring (discipline-agnostic), Architecture Design (same building, different objects), Electrical Design Application (directory §16 — industrial vs building electrical?), HVAC load-calculation tools (calculation-first pole), Building Energy Management (operations, not design), Mechanical CAD (products, not buildings).

## Research Questions

1. What are the core objects? (building context, systems, components, networks, loads)
2. What is the design loop? (layout → connect → size → calculate → verify → document)
3. Which calculations are embedded? (heating/cooling loads, duct/pipe sizing, pressure drop, voltage drop, lighting, sprinkler hydraulics)
4. What deliverables are produced? (plans, sections, schematics, schedules, BOM, reports)
5. How does multi-discipline coordination work? (federated model, clash checking, issue management, IFC)
6. What rules/standards govern the design? (national/European/international calculation standards, localisation)
7. What variants exist? (discipline scope, model-first vs drafting-first vs calculation-first, regional standards, platform form)
8. Where are the boundaries against neighboring Types?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / pole |
|---|---|---|
| MagiCAD (for Revit / AutoCAD / BricsCAD) | MagiCAD Group (Nemetschek) | MEP-specialized design layer with integrated calculations and manufacturer content; European engineering-consultancy market |
| ALLPLAN + AX3000 | ALLPLAN (Nemetschek) / ESS | MEP engineering inside a full multi-discipline BIM platform; German market |
| TRACE 3D Plus | Trane | Calculation-first HVAC load design & energy modeling; US commercial market |
| Right-Suite Universal | Wrightsoft (MiTek) | Residential/light-commercial HVAC design (loads + ducts + drawing); US contractor market |
| Revit / AutoCAD MEP (MEP toolset) | Autodesk | Market-dominant BIM/CAD platforms for MEP design — official docs NOT directly accessible (see Sources); included as market anchors with reduced assertion strength |

## Sources

Fetched 2026-09-09:

- MagiCAD Group — https://www.magicad.com/ (root), https://www.magicad.com/mep-design/ (MEP Design landing), https://www.magicad.com/applications/magicad-ventilation/, https://www.magicad.com/applications/magicad-piping/, https://www.magicad.com/applications/magicad-electrical/, https://www.magicad.com/mep-design/resources/standards-and-localisation/ — Tier 1/2, fetched successfully.
- ALLPLAN — https://www.allplan.com/en/ (root), https://www.allplan.com/industry-solutions/mep-engineering-software/ (MEP Engineering solution page) — Tier 1/2, fetched successfully.
- Trane — https://www.trane.com/commercial/north-america/us/en/products-systems/design-and-analysis-tools/trace-3d-plus.html (TRACE 3D Plus product page) — Tier 2, fetched successfully.
- Wrightsoft — https://wrightsoft.com/ (root, product/package chart, testimonials) — Tier 2, fetched successfully.
- Carrier — https://www.commercial.carrier.com/... (commercial landing; nav shows "HVAC System Design" software line incl. "REVIT® 3D Templates") — deep HAP page redirected to landing twice; abandoned per retry rule. Only the nav-level observation retained.

Source-access Limitations:

- **Autodesk (Revit, AutoCAD MEP)**: autodesk.com product pages returned HTTP 403; help.autodesk.com returned a JS-rendered shell ("Help") for Revit and 404 for AMEP paths; web.archive.org and en.wikipedia.org timed out repeatedly. No official Autodesk operational documentation could be fetched in this environment. Consequence: Revit/AutoCAD MEP are kept as representative products (market anchors), but **no precise claims about their native MEP feature sets are made**; Autodesk-side evidence is limited to what other vendors' official pages state about the platforms (MagiCAD: "fully integrates within the Revit, AutoCAD, and BricsCAD software platforms"; Wrightsoft customer testimonial referencing Revit as the professional HVAC design tool; Carrier nav listing "REVIT® 3D Templates").
- Bentley Hevacomp redirected to a sign-in page — abandoned.
- Design Master (designmaster.com) — transport errors, abandoned.
- DDS-CAD (dds-cad.net / dds.de) — 403 / transport errors, abandoned.
- Stabicad (stabicad.trimble.com) — transport error, abandoned.

## Product A — MagiCAD (for Revit / AutoCAD / BricsCAD)

### Key observations (evidence layer A unless noted)

- Positioning: "the leading BIM software for MEP design in Revit, AutoCAD, and BricsCAD"; "intelligent modelling tools, automated workflows and integrated calculations"; "number one BIM solution for Mechanical, Electrical and Plumbing (MEP) design used by thousands of companies in over 80 countries".
- Discipline modules: **Piping** ("design and calculation of heating, cooling and domestic water systems, including drainage, sprinkler and specialist systems"), **Ventilation**, **Electrical** ("design and calculation of electrical, lighting, telecommunication and data systems"), **Schematics** ("creating and synchronizing schematics"), **Supports & Hangers**, **Sprinkler Designer** ("powerful drawing tools with an intelligent, built-in sprinkler system calculation engine"), **Circuit Designer** ("creating electrical circuits"), **Comfort & Energy** (Room + RIUSKA "indoor climate and energy simulation"), **Room** ("creating 3D models of buildings" — for the CAD platforms that lack a native building model), **Common Tools**.
- Value framing: "Calculate and simulate systems to verify performance. With MagiCAD, you can trust that your design will work as intended." Coordination/collaboration as a pillar. BIM content as a pillar.
- Ventilation tools: product selection and installation; localisation; connection nodes between models; editing tools; ventilation calculations; duct drawing tools; distribution boxes; generic air handling units; part numbering; production model design; duct and device connections.
- Piping tools: product selection and installation; localisation; connection nodes between models; editing tools; radiator installation and connection; pipe drawing tools; integrated piping calculations; pipe series functions; pipe and device connections; gas system design and calculation; machine-learning auto-routing of underfloor heating circuits.
- Electrical tools: product selection and installation; localisation; DIALux evo compatibility (external lighting calc); switchboard schematics; integrated electrical calculations; automatic cable packet routing; cable drawing; cable tray filling ratios and cable layouts; symbol organiser; cable tray and conduit modelling; lighting track installation; system schematic drawings.
- Supported standards / localisation (structural, per-discipline, per-country):
  - Ventilation pressure loss: MagiCAD default (global), ASHRAE 2011 (USA/Global), Chinese, CIBSE (UK), DTU 68.3 (France).
  - Ventilation sound: A-filter, C-filter, NR.
  - Piping pressure loss: default, CIBSE Guide C (UK), DB-HS4/UNE 149201 (Spain), DIN 1988-300 (Germany), UNI 9182 (Italy).
  - Domestic water flow/sizing: BS 8558, CIPHE (UK), D1 (Finland), DIN 1988-300 (Germany), DS 439 (Denmark), DTU 60.11 (France), EN 806 (Europe), KS (Norway), PN-B-92-01706 (Poland), SBI 235 (Denmark), SP 30.13330.2016 (Russia), UNE 149201 (Spain), UNI 9182 (Italy), VVS 2000 (Sweden).
  - Hot-water circulation, drainage (EN 12056 system types 1–4), gas (CIBSE Guide C, UNI 7129).
  - Sprinkler: AS 2118 (Australia), BS 9251 (UK), CEA 4001 (Europe), CP 52 (Singapore), EN 12845, EN 16925, GB50084-2017 (China), MS 1910 (Malaysia), NFPA-13/15 (USA), SES (Switzerland), UNI 10779 (Italy).
  - Electrical: IEC 60909; interoperability with external electrical calculation software (ElectricalOM UK, Progetto INTEGRA Italy).
- Manufacturer content: MagiCAD Cloud — "over 1 million intelligent manufacturer BIM objects" from "over 300 manufacturers"; Manufacturer Product Selection ("configure, technically validate, and use manufacturer-specific products"); MagiCAD Create (custom objects).
- Customer quote (official references page): "The biggest benefits of MagiCAD are automatic calculations and Bill of Materials lists, access to an extensive product database." Used by engineering consultancies (AFRY, WSP, COWI, Ramboll, Sweco, Arup, Granlund, Royal HaskoningDHV per logo wall).

## Product B — ALLPLAN + AX3000 (MEP Engineering)

### Key observations

- Positioning: "ALLPLAN's BIM solutions for MEP and building services engineering cover the entire design to build process… integrated working with architectural and structural engineering disciplines." "Expect more from your MEP design software with ALLPLAN and AX3000."
- Workflow presented in three phases:
  1. **Design basis / Project coordination** — "centrally plan and manage different building systems such as ventilation, heating, sanitation, electrical, residential ventilation and sprinklers in a single 3D building model"; drawing-file system for reviewing systems "so that collisions and errors can be avoided in advance"; Bimplus Issue Manager synchronization.
  2. **Modeling** — Sanitation design (pipe networks in 3D, 3D libraries, manufacturer databases, automatic connection functions, calculations); Sprinkler design (Easyline dimensioning, sprinkler component library, custom sprinkler types); Electrics design ("from empty conduit and route planning to the construction of the electrical base and the checking of circuits, up to finished evaluations and lists in Microsoft Excel"); Residential ventilation (Room Book, air volumes, automated 3D planning, parts lists); Heating design (material databases, automation functions).
  3. **Analyses** — Energy analysis (variant comparisons, KfW funding level, standards compliance); Ventilation and cooling load calculation; "ductwork calculations, from pressure drop to sound to temperature drop"; Heating load calculation (AX3000 Room Book); Temperature simulation (dynamic thermal simulation, hourly heating/cooling loads).
- Deliverables: "Swiftly and accurately generate plans, drawings, and reports directly from the 3D model"; change management — "changes made automatically across deliverables simply by editing once in either the drawings or model"; "reliable automated quantities and materials take-off".
- Open BIM: IFC4 RV import/export; Bimplus collaborative platform.
- Working methods: "Flexible workflows in 2D, 2.5D and 3D as well as the full object-orientated BIM working methodology."
- Claims marketing percentages (50% faster/more accurate deliverables in 3D vs 2D; 70% more precise costing vs manual take-off; 30% productivity increase) — vendor claims, not independently verified; recorded as marketing, not evidence.

## Product C — Trane TRACE 3D Plus

### Key observations

- Positioning: "TRACE 3D Plus HVAC Design Software" — load design and energy modeling.
- Building modeling: "Model Complex Buildings & Systems with Ease" — building canvas with undo/redo, multi-story floors, detailed roofing, complex models; adiabatic/thermal boundary tool for retrofit analysis; precision PDF import for scaling/aligning floor plan images; 2D and 3D views of "architectural designs and HVAC systems".
- Systems: "Easily configure systems and plants schematically with built-in validation"; "powered by the accurate EnergyPlus® engine"; guided experience "that matches real-world design practices".
- Compliance/energy: step-by-step wizard for LEED and ASHRAE 90.1; automated fan calculations and libraries; ASHRAE 62.1 ventilation libraries; ASHRAE 170 healthcare airflow modeling (minimum vs absolute airflow); ASHRAE 140 compliance results published; energy modeling and economic analysis; compare up to 20 alternatives; decarbonization outputs; DOE 179D qualification documents.
- **Not present**: no duct/pipe physical routing, no electrical design, no plumbing design, no construction drawing production. This is the calculation-led pole: building context + loads + system/plant configuration + reports.

## Product D — Wrightsoft Right-Suite Universal

### Key observations

- Positioning: "World leader in HVAC design software"; "calculates loads for accurate size and system design to maximize comfort and efficiency in performance and installation"; "from plans to permits"; drag-and-drop interface.
- Scope: Residential Loads & Ducts (ACCA Manual J & S loads, ACCA Manual D ducts; Canada: F280-12 loads & HRAI ducts); Commercial Loads & Ducts (ACCA Manual N, ASHRAE loads and ducts); Right-Draw drawing; Right-CAD 3D add-on ("importing some of my more complex duct designs already created with RSU… The 3rd dimension takes the guesswork out of interstitial duct runs"); radiant panel loops; energy analysis & cost comparison; high-velocity ducts; geothermal; duct balancing & commissioning; code/energy links (REScheck, COMCheck, REMRate, Florida EGUSA, Title 24); mobile block-load tools; manufacturer equipment databases.
- Customer testimonial (official page): "the future of professional & field ready HVAC design, without the cost and lengthy learning curve of Revit" — indirect evidence that Revit is perceived as the professional-tier MEP/HVAC design tool.
- **Not present**: no electrical, no plumbing, no multi-discipline coordination. Residential/light-commercial HVAC pole.

## Product E — Autodesk Revit / AutoCAD MEP (market anchors; docs not accessible)

### Key observations (indirect, reduced strength)

- MagiCAD's official pages repeatedly state it runs "within Revit, AutoCAD & BricsCAD" and "fully integrates within the Revit, AutoCAD, and BricsCAD software platforms" — confirming these platforms host MEP design work.
- MagiCAD's "Room" module exists specifically to "creat[e] 3D models of buildings" inside the CAD platforms — implying the CAD platforms do not natively provide the full building-model context that Revit does (inference, moderate confidence, from MagiCAD's own module descriptions).
- Carrier's commercial software nav lists "REVIT® 3D Templates" — manufacturers target Revit as an MEP design platform.
- Wrightsoft testimonial references Revit as the professional HVAC design alternative.
- No direct Autodesk documentation fetched; no precise claims made about native MEP feature sets.

## Cross-product Comparison

| Dimension | MagiCAD | ALLPLAN+AX3000 | TRACE 3D Plus | Right-Suite Universal |
|---|---|---|---|---|
| Building context | Revit model native; Room module builds 3D building in CAD platforms | single 3D building model in ALLPLAN | building canvas (floors/rooms/roofs), PDF plan import | floor-plan drawing (Right-Draw), 3D via Right-CAD |
| Discipline scope | mechanical (ventilation) + piping + electrical + sprinkler + schematics | ventilation, heating, sanitation, electrical, sprinkler | HVAC loads/systems/plants only | HVAC loads/ducts only (resi/light-commercial) |
| Physical network layout | ducts, pipes, cables, conduits, cable trays | pipe networks, conduits, ducts | no physical routing | duct layout (2D/3D) |
| Embedded calculations | ventilation (pressure loss, sound), piping (pressure loss, water flow, hot-water circulation, drainage, gas), sprinkler hydraulics, electrical (IEC 60909) | heating/cooling loads, ductwork (pressure drop, sound, temperature drop), energy, thermal simulation | hourly loads (EnergyPlus), system/plant sizing, energy & economics | Manual J/S/N loads, Manual D ducts, energy comparison |
| Standards/localisation | per-country standard selection (14+ water standards, 12 sprinkler standards, ASHRAE/CIBSE/DIN/DTU…) | German/European context (KfW, energy certificate, DIN-family via AX3000) | ASHRAE 90.1/62.1/140/170, LEED | ACCA Manual J/S/D/N, REScheck/COMCheck/Title 24 |
| Manufacturer content | MagiCAD Cloud (1M+ objects), product selection/validation | manufacturer databases in modules | Trane equipment libraries | manufacturer equipment databases |
| Deliverables | model + drawings + BOM lists + schematics | plans/drawings/reports from model, quantities take-off | load/energy/compliance reports | load reports, duct layouts, proposals |
| Coordination | connection nodes between models, collaboration tools | federated model, collision avoidance, Bimplus issues | alternatives comparison (design variants) | — |
| Platform form | plugin/module inside Revit/AutoCAD/BricsCAD | module inside ALLPLAN platform | standalone Windows app | standalone Windows app + add-ons |

### Stable commonalities (evidence layer B)

1. Building spatial context (levels/floors, rooms/spaces/zones) anchors the design — all four.
2. Building-services systems as networks of physical components with engineering parameters — all four (grain differs: physical routing in MagiCAD/Allplan/Wrightsoft; system/plant configuration in TRACE).
3. Engineering sizing/verification by calculation — all four; the calculation is bound to the designed objects (loads from rooms, flows from terminals, hydraulics from pipe networks).
4. Deliverables that communicate the design to others — all four (drawings/schedules/model vs reports).
5. Discipline-structured toolsets (mechanical / electrical / plumbing / fire) — MagiCAD, Allplan; absent in the HVAC-only poles (scope variant).
6. Manufacturer/product content — MagiCAD, Allplan, TRACE (Trane libraries), Wrightsoft (equipment databases).
7. Standards/localisation as a first-class axis — MagiCAD (explicit standard pickers), TRACE (ASHRAE/LEED), Wrightsoft (ACCA/REScheck/Title 24), Allplan (KfW/energy certificate).
8. Schematic representation alongside physical layout — MagiCAD (Schematics, switchboard schematics, system schematics), TRACE (system/plant schematics), Allplan (drawing-file system).

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

An MEP Design application is an engineer-facing authoring environment whose defining core is four jointly-held structures:

1. **Building-services systems as the unit of design** — networks of physical components (ducts, pipes, fittings, terminals, cables/conduits, panels, fixtures, equipment) that deliver mechanical, electrical, and plumbing services through a building. Remove → generic CAD/diagramming.
2. **Building spatial context** — components are placed in a building frame (levels/floors, rooms/spaces/zones) that the systems serve; the building model (authored, imported, or drawn) anchors placement and loads. Remove → industrial plant piping / product-design territory.
3. **Engineering sizing/verification loop** — the layout is designed against engineering quantities (loads, air/water flows, electrical demand, capacities); components are sized/selected and the design is verified by calculation bound to the designed objects. Remove → pure drafting tool.
4. **Design deliverables for others** — the design leaves the application as deliverables (plans/drawings, schedules/BOM, schematics, calculation/compliance reports) that communicate it to installers, reviewers, and permitting authorities. Remove → analysis sandbox.

Jointly-held load-bearing analysis:

- 1 alone = component catalog / diagramming tool
- 2 without 1 = architecture tool
- 1+2 without 3 = drafting/modeling without engineering (generic CAD)
- 1+3 without 2 = equipment sizing calculator with no building
- 3 without 1+2 = bare calculation engine
- 1+2+3 without 4 = analysis sandbox, not a design deliverable producer
- 2+4 without 1+3 = generic drafting in a building

### L1 — Common Mature Structure

- Discipline-specific component families with engineering parameters (ducts/terminals, pipes/fixtures, cables/panels, sprinklers)
- Network connectivity semantics (connectors, flow direction, system assignment; auto-connection functions)
- Automated routing/drawing aids (duct/pipe drawing tools, cable packet routing, Easyline-style dimensioning, ML auto-routing)
- Manufacturer product content (BIM object libraries, selection/validation tools, equipment databases)
- Multi-discipline coordination (single/federated building model, collision checking, issue management)
- Schedules/BOM/parts lists and quantities generated from the design
- Schematic diagrams (single-line, riser, system/plant schematics) alongside physical layout
- Model–drawing associativity (plans/sections/reports generated from the model; edit once, propagate)
- Interoperability (IFC import/export, links to external calculation tools: DIALux, ElectricalOM, REScheck/COMCheck)

### L2 — Variant / Optional Structure

- Discipline scope: full MEP+fire vs HVAC-only vs electrical-only poles
- Market scale: residential/light-commercial vs commercial/industrial
- Regional standards/localisation (ASHRAE/CIBSE/DIN/EN/NFPA/GB/AS + national water/drainage standards)
- Calculation depth: sizing-only ↔ full load design ↔ dynamic thermal/energy simulation & economic analysis
- Platform form: standalone app vs module/plugin inside a host CAD/BIM platform vs integrated multi-discipline suite
- Working method: 2D drafting ↔ 2.5D hybrid ↔ full 3D object-oriented BIM
- Compliance/energy-certification packaging (LEED, ASHRAE 90.1/62.1/170, KfW, REScheck/COMCheck, energy certificates, 179D)
- Fabrication-level depth (part numbering, production model design, supports & hangers)
- Energy/carbon analysis as bundled module

### L3 — Vendor-specific (research notes only)

- MagiCAD Cloud / Create / Object Enabler; RIUSKA; ML underfloor-heating auto-routing
- AX3000 module set (ESS); Bimplus; KfW funding transfer; DiBT print module; VR add-on
- TRACE: EnergyPlus engine; ASHRAE 140 compliance results; 179D documents; Trane equipment libraries; 20-alternative comparison
- Wrightsoft: ACCA-certified programs; Rheia add-on; Perfect Pitch (Daikin/Amana/Goodman); Fla-J/EGUSA links; mobile block-load products
- Vendor marketing percentages (Allplan 50/70/30 claims) — not evidence

## Vendor-specific Findings

See L3. Additionally: MagiCAD's per-country standard pickers are the clearest documentation of localisation as a product axis; Allplan's three-phase workflow (design basis → modeling → analyses) is a vendor workflow framing, not a Type invariant.

## Boundary Findings

- **vs BIM Authoring (§17 sibling)**: BIM Authoring is the discipline-agnostic model-authoring environment (architecture, structure, MEP all author models in it). MEP Design is the discipline-specific slice: its objects are building-services systems and its loop is engineering sizing/verification. Remove the MEP discipline focus and the sizing loop → BIM Authoring. The two Types legitimately coexist: MEP design work happens either in discipline-specific environments (MagiCAD, AX3000, Wrightsoft) or in general BIM platforms used by MEP engineers (Revit). Keep both leaves; MEP Design is defined by discipline + engineering loop, not by platform.
- **vs Architecture Design Application**: same building context, different objects (spaces/envelope vs services networks) and different engineering (comfort/energy vs loads-flows-capacities of services).
- **vs Structural Engineering Design**: structure carries loads into the ground; MEP distributes services through the building. Different physics, different objects, different calculations.
- **vs Electrical Design Application (§16, Engineering/Manufacturing section)**: unresolved seam. Building electrical design (lighting, power, circuits, cable sizing) is one discipline inside MEP Design (evidenced by MagiCAD Electrical, AX3000 Electrics). The §16 leaf likely targets industrial/power-systems electrical design (a different object world). Recorded as a Boundary Issue for the taxonomy pass; this pass does not rewrite the directory.
- **vs HVAC load-calculation / energy-modeling tools** (HAP/TRACE-class): calculation-first products without physical network layout or installation documentation sit at the edge. TRACE 3D Plus was held **in-type as the calculation-led variant pole** (it has building context, system configuration, and produces engineering deliverables), but the seam is real: remove physical layout + installation deliverables and the product drifts toward a load-design/energy-modeling Type. Uncertainty recorded.
- **vs Building Energy Management / BMS (§17)**: design-time vs operations-time. The MEP design model may feed the BMS, but the BMS operates live systems through control logic — different object world (points, loops, schedules vs design components).
- **vs Mechanical CAD (§16)**: products/machines vs building services. Different context (assembly vs building), different calculations.
- **vs Construction Estimating / Quantity Takeoff**: downstream consumers of MEP models/schedules; MEP Design produces the quantities, takeoff tools price them.
- **"去掉什么就变成另一个 Type" 判据**: remove the building context → industrial piping/process design; remove the services-systems objects → architecture/CAD; remove the sizing loop → drafting; remove deliverables → analysis tool; remove the discipline focus → generic BIM authoring.

## Historical / Market-Sample Check (§24)

- Paper-era MEP design: hand-drawn plans/sections over architectural backdrops + hand calculations (heat-loss sheets, ductulator/duct-sizing tables, voltage-drop tables) + equipment schedules + specifications. All four L0 legs satisfied with no software.
- 1980s–90s software generation: 2D CAD with MEP symbol/component libraries + separate calculation programs (Hevacomp-class UK tools, Elite-class US tools); regional products (MagiCAD's Finnish origin, DDS-CAD Germany) — fit the definition without BIM, cloud, IFC, or manufacturer-content platforms.
- Regional products (Nordic MagiCAD, German ALLPLAN/AX3000, US ACCA-centric Wrightsoft) all satisfy the four legs — the definition is not US- or BIM-era-specific.
- Conclusion: L0 holds across eras and regions; BIM, cloud content, IFC, ML routing, energy simulation are era machinery (L1/L2), not invariants.

## Uncertainties

1. Autodesk Revit / AutoCAD MEP native feature sets not directly verified (source-access limitation). Representative status retained; no precise claims made.
2. Whether the sizing/verification loop is strictly invariant or "merely common": all sampled layout-capable products embed calculations, and no sampled product is marketed as MEP design software without calculation capability; held as invariant with moderate confidence, flagged for future passes.
3. Fire-protection coverage varies (sprinkler modules present in MagiCAD/AX3000; not universal) — held as a common discipline, not a required one.
4. TRACE 3D Plus classification (calculation-led variant vs neighboring load-design Type) — held in-type with the seam recorded.
5. The §16 "Electrical Design Application" leaf's intended scope (building vs industrial electrical) — unresolved; recorded as Boundary Issue.
6. Exact deliverable forms vary (installation drawings vs compliance reports); the invariant was abstracted to "design deliverables for others".

## Final Synthesis

MEP Design is the engineer-facing design environment for building services. Its defining core is the joint presence of: building-services systems as designed objects; a building spatial context; an engineering sizing/verification loop bound to those objects; and design deliverables for others. Around that core, mature products add discipline toolsets, connectivity-aware networks, manufacturer content, coordination, schedules/schematics, and standards-driven localisation. Variants span discipline scope, market scale, calculation depth, platform form, and regional standards. The Type is distinct from generic BIM authoring (discipline-agnostic), from architecture/structural design (different objects/physics), from industrial electrical design (different object world), and from operations-side building systems (design-time vs run-time).
