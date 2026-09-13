# Research Notes — Structural Engineering Design

## Research Goal

Understand what Structural Engineering Design software actually is and how it works, from real products: what objects exist inside it, what the engineer does with them, how the work flows from model to verified design to deliverables, which rules govern behavior, and where the Type's boundaries run against its neighbors (CAE / Engineering Simulation, BIM Authoring, Architecture Design Application, MEP Design, Civil/Site Design).

## Initial Boundary

Hypothesis at start:

- Core use: structural engineers verify that load-bearing structures (buildings, bridges, towers, industrial structures) safely carry their loads, per design codes.
- Main users: structural engineers in engineering offices; also students, reviewers, contractors consuming outputs.
- Nearest neighbors: CAE / Engineering Simulation (general FEA), BIM Authoring (data-rich element model), Architecture Design Application (geometry + documentation), MEP Design (building-services sibling), Civil / Site Design (land works), Mechanical CAD (products, not structures).
- Boundary risk: could collapse into "generic FEA" if defined only by analysis; could collapse into "BIM" if defined only by modeling.
- Unknowns at start: whether code-based member verification is definitional or merely standard; whether the analysis-only product pole belongs in the Type; how the physical vs analytical model split affects the definition.

## Research Questions

1. What is the unit of record — the model? The member? The calculation?
2. What exactly does the analysis step compute, and what does the engineer see?
3. How do loads enter the system (cases, combinations, code-generated)?
4. What does "design" mean operationally in these products — who decides member sizes, and how does code-checking work?
5. What is produced for others (reports, drawings, schedules, model exchange)?
6. How do products differ in packaging (modules vs integrated vs suite) and model philosophy (analytical-first vs physical-first)?
7. Where is the seam to CAE / Engineering Simulation and to BIM Authoring?
8. Would older (2D-frame-era), regional, and specialty products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, differing philosophies, differing geographies and customer levels:

| Product | Vendor / Geography | Philosophy / Positioning | Evidence tier |
|---|---|---|---|
| RFEM 6 (+ add-on modules) | Dlubal Software (DE/CZ) | FEA main program + purchasable design add-ons per material (concrete, steel, timber, glass); Eurocode-first; modular family also includes RSTAB 9 (member/beam analysis) | Tier 1–2 (official product pages) |
| SkyCiv Structural 3D | SkyCiv Engineering (AU/global) | 100% cloud/browser SaaS; analysis core + per-code design modules; self-serve from students to enterprises; exceptional public documentation | Tier 1 (official docs incl. Integrated Member Design page) |
| Tekla Structural Designer | Trimble / Tekla (UK/US) | Building-focused analysis + design in ONE model, no modules; physical-model-first with auto-generated analytical model; deep BIM sync (Tekla Structures, Revit) | Tier 2 (official product page, detailed capability prose) |
| RISA-3D / RISAFloor / RISAFoundation / RISAConnection | RISA Tech, Inc. (US, Nemetschek) | Suite of cooperating products with explicit "separation of tasks" philosophy; US-code-centric with international support | Tier 2 (official site incl. product-family FAQ) |
| SCIA Engineer | SCIA (BE, Nemetschek) | Integrated multi-material analysis + design for all structure types (office buildings, industrial plants, bridges); one model full design process; openBIM (IFC, SAF); Eurocodes + national annexes, US, NBR, SIA | Tier 2 (official product page) |

Market anchors not fetched (known-blocked or out of budget for this pass): Autodesk Robot Structural Analysis, CSI SAP2000/ETABS, Bentley STAAD, MIDAS, Oasys GSA, PKPM. No operational claims made for them; they are referenced only as the wider market context.

## Sources

All fetched 2026-09-10:

- Dlubal — RFEM 6 product page: https://www.dlubal.com/en/products/rfem-fea-software
- SkyCiv — root product page: https://www.skyciv.com/structural-3d/
- SkyCiv — documentation root: https://skyciv.com/docs/
- SkyCiv — Structural 3D docs section (Modelling / Members / Applying Loads / Solving / Design / Post Processing / Reporting): https://skyciv.com/docs/structural-3d/
- SkyCiv — Integrated Member Design article: https://skyciv.com/docs/skyciv-member-design/general/integrated/
- Tekla — Tekla Structural Designer product page: https://www.tekla.com/products/tekla-structural-designer
- RISA — company / product-family page: https://risa.com/
- SCIA — SCIA Engineer product page: https://www.scia.net/en/scia-engineer

## Product Observations

### Dlubal RFEM 6 (Evidence A unless noted)

Key observations:

- Self-positioning: "FEA Software for Structural Engineers"; "structural and dynamic analysis"; main program for "planar and spatial structural systems consisting of plates, walls, shells, and members", plus combined structures, solid and contact elements.
- The software computes: "deformations, internal forces, stresses, support forces, and soil contact stresses."
- Loads: "Load wizards simplify wind, snow, and other environmental influences"; tools for generating snow/wind/opening loads, converting surface loads to member loads; automatic generation of action combinations, load combinations, and design situations "according to Eurocode and other international standards", following "the corresponding combination expressions"; separate result combinations.
- Analysis types: linear static, second-order, large deformation (nonlinear); multiprocessor computation kernel; individual calculation parameters.
- Design: "add-ons integrated directly in the program allow you to easily carry out additional analyses and design checks according to various standards (for example, in reinforced concrete, steel, and timber structures)" — modular concept extends the main program with per-material design (concrete, steel, timber, glass construction).
- Design transparency: feature "Output of Design Check Formulas" — the check's own formulas appear in output.
- Interfaces/UI: CAD-like graphical workspace (central), Navigator tree (Data / Display / Views / Results tabs — Results appear "after the calculation"), spreadsheet-style Tables, control panel with result legend.
- Output: multilingual printout report with adaptable templates; integrate graphics, texts, MathML formulas, PDFs.
- Libraries: cross-section and material libraries with favorites.
- Ecosystem: gRPC API (Python), cloud calculations, RWIND (CFD "digital wind tunnel" for wind load determination), Dlubal Center (project/customer organization).
- Breadth claim (vendor): "One program for all types of structures, from single-span girders to complex 3D shell structures or NURBS solids."
- Family: RSTAB 9 = separate member/beam analysis family with its own add-ons; RFEM vs RSTAB = surface/solid FEA vs member analysis (product-family split inside one vendor).
- Pricing (L3, research notes only): RFEM 6 main program listed at 4,750 EUR purchase / rental / subscription options in the on-page webshop.

### SkyCiv Structural 3D (Evidence A)

Key observations (docs = official operational documentation):

- Positioning: "All-in-One Structural Engineering Software... Powerful and easy-to-use structural analysis and design software. Accessible anywhere from your browser." 100% cloud-based; free tier; student/teacher solutions; API; mobile app.
- Object model (docs tree, Structural 3D section): Nodes, Members (normal vs continuous, rigid, cables, curved/spiral, open-web steel joists), Sections, Materials, Supports, Plates (+ meshing), Rigid Diaphragms, Grids/Gridlines and Elevations, Strut-and-Tie Builder, Assembly Templates.
- Loads (docs tree): Point Loads, Distributed Loads, Moments, Area & Wind Loads, Pressures, Prestressed & Thermal, Self Weight; Load Groups; Load Combinations; Load Combination Schemas; Integrated Load Generator (wind/snow/seismic per ASCE 7, AS/NZS 1170, EN 1991, NBCC, IS 875, NSCP, CFE, SANS, NZS 1170.5...).
- Solving (docs tree): Repair Model; Linear Static; Linear Static + Buckling; Non-Linear Static & P-Delta; Dynamic Frequency; Response Spectrum + Seismic; solver errors/warnings list; model troubleshooting. (The solve is an explicit user step with its own docs section.)
- Design (docs tree): Member Design (integrated), RC Design, Connection Design, Wind Design, Member Designer (optimizer). Integrated = "you model them in the program and all the results, properties and dimensions are loaded directly into the program."
- Integrated member design workflow (Tier-1 article): select a design module from the "Design" bubble → the module opens with member/material/section data and internal member forces "automatically imported from the structural analysis, this includes load combinations" → "the software will design check based on the worst case for each member and load combination" → engineer controls design parameters (braced lengths Ly/Lz, effective length factors Ky/Kz, unbraced length Llt, slenderness and deflection limits) → run "Check Design".
- Design results: tabulated Pass/Fail (green/red, CSV export), graphical coloring on the model by maximum utility ratio (green < 1; orange 0.95–1 near full utilization; red > 1 fails; gray = no check performed, e.g. unsupported section shape or custom section), per-check ratio display (e.g. "1.321 Sl" for slenderness), PDF summary report export.
- Design codes carried as modules (product page + docs): US (AISC 360 ASD/LRFD, NDS, AISI S100), Europe (Eurocode 3, BS 5950, BS EN 12811), India (IS 800 LSM/WSM), Australia/NZ (AS 4100, AS 4600, AS 1720, AS/NZS 1576, AS/NZS 1664, NZ 3404), Canada (CSA S16, S157), Maritime (DNV 2.7-1); RC: ACI 318, Eurocode 2, AS 3600, CSA A23. Foundation: isolated footings, piles, combined footings, with superstructure reactions linked into the module. Connection: bolt/weld checks per AISC 360 / AS 4100 with parent/child members, design checks, detailed report.
- Post-processing (docs tree): sign conventions; reactions; shear/moment/torsion/axial diagrams; displacement/deflection; stress; plate analysis results; buckling; single-member analysis; result summary and limit checks; plate section cuts.
- Reporting (docs tree): analysis report + bill of materials; single-member reports; nodal/member/plate results; export drawings; user-defined screenshots.
- Adjacent product layers: Section Builder (custom/cold-formed sections with calculation verification), CloudCAD (drafting → exports to Structural 3D), free calculators (beam/truss/frame/wind/base plate/retaining wall...) as acquisition funnel, SkyCiv API for automation.
- Industries named: residential, steel, concrete, timber, cold-formed, shed/warehouse, mechanical, marine, offshore oil & gas, event rigging, scaffolding — structure breadth beyond buildings.

### Tekla Structural Designer (Evidence A)

Key observations (official product page, detailed capability prose):

- Positioning: "Analyze and design buildings efficiently... Seamlessly combine the design and analysis into one easy and efficient single model-based process... regardless of structural material."
- Model philosophy: "Physical modeling drives efficient designs from more accurate simulation." "The software auto-generates an analytical model allowing you to focus on the design" — physical model → derived analytical model, explicit.
- Integration posture: "analysis, design and BIM form an integrated, automated process... structural analysis and design proceed simultaneously"; "One product, one interface, one model... no additional modules to buy" (contrast with modular vendors); covers "both gravity and lateral systems" in one model.
- BIM sync: design model can start in Tekla Structural Designer, Tekla Structures, or Autodesk Revit; "synchronize models multiple times with confidence throughout the project to instantly assess the impact of changes."
- Loads: "Full building wind loads are automatically calculated and applied to your model" per the design code; "no need to worry about all the other lateral loading required by the design code."
- Analysis: FE engine, fully automated meshing; transparent results — "you can investigate the forces, deflections and all design calculations"; footfall (vibration serviceability) analysis; "rigorous slab deflection" (serviceability); Staged Construction Analysis (SCA) recognizing "a structure's changing state over time."
- Design: "fully automated design to your chosen building code... design all members and consider the overall 3D building design in one seamless process"; RC — "optimized design for all rebar within the beams, columns, slabs, flat plates and walls", then "detailed reinforcement drawings and accurate material quantities are automatically generated"; steel — "detailed design and optimization of composite beams, columns, US joists, trusses, braces and plated sections."
- Scheme work: create/compare alternative schemes in minutes; embodied-carbon comparison of design options; Grasshopper live link for parametric design.
- Other materials (precast, timber, masonry) via Tekla Tedds calculations (sibling calculation product).
- Output: "automatically produces accurate and detailed documentation including calculation reports, material take-offs and drawings"; "calculation reports are linked directly to the model, so they update automatically" (change management headline); export beam reactions / bracing forces to contractors; wide range of file formats.
- Codes: "Eurocodes, US, Indian and Australian codes, as well as British Standards."

### RISA (Evidence A)

Key observations (official site incl. product-family FAQ):

- Positioning: "Analysis and Design Software for Every Project and Engineer."
- Suite philosophy (vendor's own words): "RISA continues to promote a separation of tasks in order to streamline the modeling process, providing tools that cater to exactly what needs to be created"; "Leverage geometry, loading, design information and results from one RISA software to another in order to save time, avoid mistakes and maximize design coordination."
- Suite composition: RISA-3D ("general 3D analysis and design", "Trusted leader in 3D analysis and multi-material design"); RISA-2D; RISAFloor ("floor system modeling and design", "Model, load, analyze and design multi-story buildings"); RISAFoundation ("foundation system design", "at or below grade"); RISAConnection ("steel connection design", full 3D visualization/design/reporting); RISACalc ("member and component calculations", "instant feedback while also allowing full control"); RISASection (custom sections); ADAPT-Builder / ADAPT-PT/RC / ADAPT-Felt (post-tensioned concrete); Link Utilities ("integrations with Revit, Tekla, and other BIM tools").
- Codes: "ASCE 7 (loads), AISC 360 (steel), ACI 318 (concrete), NDS (wood), IBC, CSA, Eurocode and other region-specific codes."
- Industries: "Commercial and residential buildings; healthcare, education, government; industrial plants and warehouses; stadiums, arenas, cultural centers; bridges, towers, and specialty structures; solar, telecommunications, and utility infrastructure."
- Support/training: engineering-staffed support; online help manuals; training courses; cloud-based licensing (license sharing, offline borrowing).

### SCIA Engineer (Evidence A)

Key observations (official product page):

- Positioning: "an integrated, multi-material structural analysis software and design tool for all kinds of structures... office buildings, industrial plants, bridges or any other project, all within the same easy-to-use environment."
- One-model posture: "Full design process in one model... just one tool featuring CAD-like modelling, advanced analysis, code-compliant multi-material design and customizable reports."
- Productivity: adaptive mesh generation, optimization and reporting tools, intelligent automation.
- BIM: "Seamless exchange of models with other project stakeholders, through the powerful bi-directional links, IFC, SAF or third-party plug-ins"; openBIM innovation (SAF = Structural Analysis Format, SCIA-initiated open format for analysis-model exchange); customer quote evidencing shared-model workflow with architects ("our beams are their beams; their walls are our walls") and round-trip transfer to Tekla Structures.
- Codes: "the most comprehensive implementation of Eurocodes, including over 20 National Annexes, U.S. codes and other international standards like NBR or SIA" (national-annex depth is a vendor claim; the qualitative point — national-annex localization is a real dimension — is corroborated by Dlubal's "national and international standards" and multi-language output).
- Breadth in user stories: 290 m Rhine bowstring bridges, railway bridge replacement, glass-steel dome, football stadium, Port House Antwerp — large-project pole.

## Cross-product Comparison

| Dimension | RFEM 6 | SkyCiv S3D | Tekla SD | RISA | SCIA Engineer |
|---|---|---|---|---|---|
| Structure model of record | members + plates/walls/shells/solids, combined | nodes/members/plates/supports (+cables, joists) | physical building model (auto → analytical) | member models (3D/2D) + floor systems + foundations across products | multi-material structural model, all structure types |
| Loads | load wizards (wind/snow), surface↔member conversion | point/distributed/area/pressure/thermal/prestress/self-weight + generator | automated full-building wind per code | loads in each product (ASCE 7 named) | loads within one model process |
| Combinations | auto per Eurocode + international; action/load/result combos | load combinations + code schemas | lateral loading per design code | per code (ASCE 7) | per selected code + national annex |
| Analysis | linear static; 2nd order; large deformation | linear static, buckling, P-Delta, dynamic frequency, response spectrum | FE engine, auto mesh, footfall, slab deflection, staged construction | analysis in 2D/3D products | advanced analysis, adaptive mesh |
| Design checks | add-ons per material/standard | per-code modules (steel/timber/CF/RC/connections/foundations) | fully automated member design to chosen code; RC rebar + steel optimization | RISA-3D multi-material; separate RISAConnection/RISAFoundation/RISACalc | code-compliant multi-material design |
| Check semantics | design checks with formula output | utility ratio, pass/fail colors, worst-case per member/combination | transparent, all design calculations inspectable | instant feedback, full control (RISACalc) | safe/economical design compliant with codes |
| Output | multilingual printout report + MathML formulas | analysis report, BOM, drawings export, PDF design summary | calc reports (auto-update with model), rebar drawings, take-offs | reports in each product; connection reporting | customizable reports |
| Exchange | CAD/BIM interfaces, gRPC API, cloud calc | IFC/import-export, API, mobile | bi-directional Tekla Structures / Revit sync | Revit/Tekla link utilities | IFC, SAF, bi-directional links |
| Codes emphasis | Eurocode + international | AISC/EC/AS/CSA/IS/NDS/DNV... | Eurocodes, US, Indian, Australian, British | ASCE 7/AISC/ACI/NDS/IBC/CSA/EC | Eurocodes + national annexes, US, NBR, SIA |
| Packaging | main program + purchasable add-ons; RSTAB sibling | cloud SaaS, modules in one platform, free tier | one product, no modules | cooperating suite | one product (editions) |
| Audience | engineering offices (mid→large), 130k users claimed | students→SMB→enterprise; education programs | building design engineers | US firms, all sectors | mid→large, large-project pole |

Stable commonalities across the sample (Evidence B):

1. The structure exists as a persistent, editable engineered model with structural properties (elements, sections, materials, supports).
2. Loads are organized as load cases; mature products combine them into combinations, commonly generated to a selected code.
3. Analysis is a distinct, explicit step producing the structure's response: internal forces, deflections/deformations, reactions (and stresses).
4. Design verification is performed per selected design standards, per member/element, using the computed response; results are pass/fail-type ratios that drive sizing.
5. Every product documents/outputs the calculation (reports; two products output check formulas / fully inspectable calculations).
6. All ship libraries of standard sections and materials.
7. All connect outward: CAD/BIM exchange and/or APIs; construction-facing outputs (drawings, schedules, quantities, reactions for contractors).

## Canonical Model (synthesis)

Defining structure (Evidence C — canonical inference from cross-product comparison):

1. **The structural model of record** — the load-bearing structure held as an engineered, editable model: connected load-bearing elements (members as the canonical element class; surfaces/solids in FEM-based products) each carrying structural properties — cross-section, material, connectivity/end conditions — and support conditions grounding the structure. Remove → geometry/CAD model of a structure, no engineering semantics.
2. **The loading-and-analysis loop** — loads organized as explicit load cases (combinations in mature practice, commonly code-derived) applied to the model; the software computes the structure's response: internal forces, deflections, reactions. Remove → drafting/CAD; the engineering computation disappears. (The solver method — stiffness/FEM — is implementation, not definition: 2D member-frame products satisfy with simpler solvers.)
3. **Code-based verification and sizing** — computed response is checked against a recognized structural design standard (strength, stability, serviceability), element by element, producing utilization/pass-fail results that drive member selection/sizing. The design standard is the engineering authority; the specific code family is a variant. Remove → analysis tool (CAE drift): "design" is gone.

Jointly-held load-bearing tests:

- 1 alone = a CAD/geometry model of a structure → not this Type.
- 2 without 1 = forces on arbitrary geometry → generic FEA/CAE.
- 1+2 without 3 = structural *analysis* software → the analysis-only edge, drifting toward CAE / Engineering Simulation; the leaf's name ("Design") and the market's own "analysis and design" bundling support verification as definitional.
- 3 without 1+2 = standalone member/component calculators taking hand-entered forces → component slice below the Type (these exist as free tools and add-ons in-sample).
- 1+3 without 2 = code checks with no computed response → component checking tools; not the integrated Type.

Deliberately NOT definitional (anti-overfitting):

- FEM / solver method / analysis-type menu (linear, P-Delta, buckling, modal, response spectrum) — capability variants; even 2D frame analysis satisfies the core (RISA-2D in-sample).
- 3D modeling — 2D products satisfy; 3D is the modern norm, not the invariant.
- Building focus — bridges, towers, stadiums, solar/telecom structures, marine/offshore containers all in-sample (SCIA bridges; RISA bridges/towers/solar; SkyCiv DNV maritime); the object is any load-bearing structure.
- Specific code families (Eurocode, AISC, ACI, AS, IS, DNV...) — regional/regime realization; the invariant is that verification binds to *a* recognized standard with its load rules.
- Physical-first vs analytical-first model architecture — product philosophy variant (Tekla SD auto-generates the analytical model from a physical model; RFEM/SkyCiv/RISA model the analytical structure directly).
- Modular vs integrated packaging — business-model variant (Dlubal add-ons / RISA suite / SkyCiv modules vs Tekla "no additional modules" / SCIA one product).
- BIM integration, IFC/SAF, Revit/Tekla links — standard, not definitional (works standalone; predates BIM).
- Load generators (wind/snow/seismic per code), auto-meshing, design optimizers, rebar detailing output, connection/foundation design modules, staged construction, footfall, embodied-carbon comparison — standard-to-optional capabilities.
- Free calculators, education licensing, cloud deployment, licensing schemes — audience/business variants.
- Any precise price, user count, code-edition list, or numeric limit — vendor facts, research notes only.

## Vendor-specific Findings

- Dlubal: modular add-on architecture with separately priced design add-ons; RWIND CFD wind-tunnel companion; RSTAB 9 as a separate member-analysis family; printout report with MathML formula embedding; on-page webshop pricing (L3).
- SkyCiv: 100% browser SaaS + mobile app; free calculator funnel; education ecosystem; gRPC-style public API; DNV 2.7-1 maritime module; CloudCAD drafting companion.
- Tekla SD: physical→analytical auto-generation; "no additional modules to buy" positioning; Staged Construction Analysis; automatic reinforcement drawings + material quantities; report auto-update tied to model; Tedds for non-primary materials; scheme comparison + embodied carbon.
- RISA: explicit separation-of-tasks suite (RISAFloor floor-system lens, RISAConnection, RISAFoundation, RISACalc); ADAPT post-tensioning products; cloud license sharing/borrowing.
- SCIA: SAF (Structural Analysis Format) openBIM initiative; national-annex depth claim; large-project user stories (Rhine bridges, Port House Antwerp).
- Trimble/Tekla ecosystem and Nemetschek group ownership (RISA, SCIA, Dlubal-adjacent Allplan shop) — market-structure fact, not design semantics.

## Boundary Findings

1. **vs CAE / Engineering Simulation (§16)** — sharpest seam. CAE centers simulating engineering artifacts' physical behavior (multiphysics, general FEA) without binding results to a construction design standard or producing construction deliverables. Structural Engineering Design binds its verification loop to structural design codes and ends in constructable outputs. Test: remove code-based verification + construction deliverables → the product becomes a general FEA/CAE tool. The analysis-only product pole (e.g., an analysis family sold without its design add-ons) sits exactly on this seam — recorded as the below-the-Type edge for this leaf.
2. **vs BIM Authoring (§17)** — BIM authoring owns the data-rich element model as the project's cross-discipline record; structural design owns the engineering verification of that structure. Exchange runs IFC/links (evidenced in three sampled products). The analytical model used for verification is a derived, reduced representation (Tekla SD: "auto-generates an analytical model"). Test: remove verification/analysis → BIM authoring; remove the cross-discipline data-record role → structural design. Keep both.
3. **vs Architecture Design Application (§17)** — architect's surface: spatial/geometry design + building documentation. Engineer's surface here: verifying load-bearing behavior. Shared geometry does not merge the Types (architecture pass recorded the same lens distinction).
4. **vs MEP Design (§17, processed 2026-09-09)** — same engineering-office family pattern (context + designed objects + engineering sizing/verification loop + deliverables). Object worlds differ: load-bearing structure vs building-services networks. Load provenance differs: MEP derives loads from rooms/occupancy; structural loads come from self-weight, use, and environmental code actions. Keep both; family pattern ratified from this side. Note: the MEP pass held "design deliverables for others" as a defining leg; this pass holds documentation as a strongly standard capability but keeps the defining core at model+loading/analysis+verification. The difference is a depth judgment between two sibling passes, documented here; no directory impact.
5. **vs Civil / Site Design (§17, processed 2026-09-07)** — that pass pre-hung "Structural/MEP: analysis-first vs geometry/slope-rules-first". From this side the seam is confirmed and sharpened: civil/site authors proposed land-form objects against measured existing ground; structural models load-bearing elements and verifies them under code loading. Civil's evaluation is cut/fill/slope geometry; structural's evaluation is response-then-code-check. Keep both.
6. **vs Mechanical CAD / CAE (§16)** — subject is the load-bearing structure for construction, not a manufactured product; deliverables are construction documents, not manufacturing drawings.
7. **vs Quantity Takeoff / Construction Estimating (§17)** — those consume structural outputs (models, quantities — e.g., TSD's auto material take-offs feed estimating); they do not verify structures.
8. **Component-design slices** — connection design, base plates, footings, retaining walls are sold both standalone (SkyCiv modules/free tools; RISAConnection) and embedded. Standalone, they take forces as inputs without a structure of record → below this Type's bar; they live inside the Type as modules when fed by the analysis. No separate directory leaf exists; recorded as an in-Type layer, no flag needed.
9. **Bridge/specialty design** — bridges fit the core (SCIA bridge projects in-sample); bridge-specialized products (market anchors only) are a domain variant, not a separate Type under the current directory.

## Uncertainties

- Autodesk (Robot), Bentley (STAAD), CSI (SAP2000/ETABS), MIDAS, Oasys official documentation was not fetched this pass (known-blocked domains per prior passes; not attempted). Their inclusion as market anchors rests on general market standing, not this pass's evidence; no operational claims made for them.
- The analysis-only product pole's exact market share and whether any sampled vendor sells a design-capable product with verification fully absent — the pole is documented structurally (Dlubal's RSTAB is an analysis family whose design arrives via add-ons; this pass treats it as the edge, not as evidence of a separate Type).
- Solver internals, default limits, numeric capacities, and edition/feature matrices were deliberately not asserted; no precise numbers from marketing pages were promoted.
- Historical evidence is at class level: pre-FEM 2D frame analysis programs and spreadsheet-era practice satisfy the minimal core (model + loads/analysis; verification where present), consistent with the software's own evolution; no primary historical source was fetched.

## Final Synthesis

Structural Engineering Design software is the structural engineer's verification workbench. Its defining structure is three jointly-held parts: (1) the load-bearing structure held as an engineered model of record — connected elements carrying sections, materials, and supports; (2) the loading-and-analysis loop — explicit load cases (mature practice: code-derived combinations) applied to the model, with the software computing the structure's response (internal forces, deflections, reactions); (3) code-based verification and sizing — every element checked against a recognized design standard using the computed response, producing utilization/pass-fail results that drive member selection. Around this core, mature products standardly add section/material libraries, code-based load generation, advanced analysis types, per-material design modules (steel, reinforced concrete with rebar output, timber, cold-formed), connection and foundation design, design optimizers, calculation documentation with inspectable formulas, construction deliverables (drawings, schedules, quantities, reactions), and BIM/CAD/API exchange. Packaging (modular add-ons / integrated suite / one-product / cloud SaaS), model philosophy (analytical-first vs physical-first), regional code ecosystems, and structure domains (general vs building-specialized vs bridges/specialty) are variant axes. The Type ends where verification ends: without the code-bound check it is analysis/CAE; without the computed response it is component calculation; without the structure model it is neither.
