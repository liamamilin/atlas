# Research Notes — Inspection & Metrology Software

Research date: 2026-09-08

## Research Goal

Understand what Inspection & Metrology Software is as an Application Type in directory §16 (Engineering, Manufacturing & Industrial): what objects exist inside it, what users do with them, how the measurement-to-verdict loop works, what rules and states matter, and where its boundaries lie against neighboring Types (Calibration Management, Statistical Process Control / SPC, Machine Vision Platform, Mechanical CAD, CAM, Manufacturing QMS, 3D modeling / reverse engineering, Product Test Management, Government Inspection Management).

## Initial Boundary (hypothesis before research)

- Core guess: software that measures manufactured parts with metrology equipment (CMMs, portable arms, laser trackers, vision systems, scanners, CT) and judges the measured geometry against a nominal reference (CAD model / drawing) and its tolerances, producing per-characteristic results and inspection reports.
- Likely users: metrology technicians, quality inspectors, quality engineers, CMM programmers, shop-floor operators.
- Likely confusion points:
  - Calibration Management (§16 sibling, already processed) — instruments vs products (pre-hung seam: "inspection/metrology software measures products on production or lab equipment; calibration management assures the instruments themselves").
  - Statistical Process Control / SPC — process statistics vs part conformance.
  - Machine Vision Platform — line-rate automated inspection vs metrology-grade dimensional evaluation.
  - Mechanical CAD — nominal creation vs nominal consumption.
  - CAM / CNC Programming — same programming-loop philosophy, machine makes material vs measuring machine verifies it.
  - 3D Modeling / Photogrammetry / reverse engineering — geometry creation vs conformance verification.
  - Government/Property/Home Inspection Management — different object and operator entirely (parts vs premises).
- Unknowns at start: is offline CAD programming definitional? Is device-driving definitional, or can evaluation-only software qualify? How central is GD&T? Is the report/record definitional? How deep does the handoff to SPC go?

## Research Questions

1. What are the core objects? (part, inspection plan / part program / measurement plan, nominal reference/CAD, features, alignments, measured data, tolerances/GD&T, results, reports)
2. What is the canonical workflow? (author plan → set up device → execute → evaluate → report → archive; vs walk-up measure; vs evaluate imported data)
3. What role does the CAD model / drawing play, and is CAD-based comparison invariant or an implementation?
4. What is an alignment and how load-bearing is it?
5. Which device kinds do these products address, and is device-driving invariant?
6. What reporting outputs exist and where do results go (SPC, QMS)?
7. Who uses the software and at what stage of production (lab, shop floor, in-process)?
8. What are the main variants (offline vs online, OEM-tied vs device-independent, modality, deployment)?

## Representative Products

| Product | Vendor | Posture | Why selected |
|---|---|---|---|
| ZEISS CALYPSO | ZEISS (DE) | OEM-tied CMM inspection software; "one-stop system" with ZEISS measuring machines | Dominant OEM philosophy; inspection-plan (not code-programming) paradigm; deep machine coupling |
| ZEISS INSPECT | ZEISS (DE) | Device-independent evaluation of optical 3D / X-ray volume data | Data-evaluation-only pole (analyze data "regardless of which system you use"); parametric measurement plans; apps/scripting |
| Verisurf | Verisurf Software (US) | Model-based definition (MBD) inspection across any CAD and any device | CAD/MBD-first philosophy; portable + CMM breadth; first-article orientation |
| CMM-Manager | QxSoft (US; formerly under Nikon Metrology) | Device-independent multi-device CMM/vision/arm software for new and legacy machines | Retrofitter's philosophy (replace OEM software, standardize fleet); walk-up + offline programming; mid-market tier |
| VGSTUDIO MAX | Volume Graphics / Hexagon (DE) | CT volumetric inspection and metrology | Volumetric modality pole (interior geometry, porosity/defects); edition ladder; multipart measurement plans |
| Aberlink 3D | Aberlink (UK) | SMB/shop-floor bundled measurement software with own CMMs and vision systems | SMB tier; ease-of-use philosophy; 2D/3D without mandatory CAD; licensed by other device makers (sixth sample, cross-check) |

Two target products could not be fetched and were not used as claim sources (see Sources): Hexagon PC-DMIS (hexagon.com / hexagonmi.com returned 403) and InnovMetric PolyWorks (innovmetric.com / polyworks.com returned 451). PolyWorks Inspector appears in evidence only secondhand (Aberlink resells it on its CMMs); no product-specific claims are made about either.

## Sources

All fetches 2026-09-08 unless noted.

Tier 1/2 (official product documentation and product pages) — fetched successfully:

- ZEISS Calypso product page: https://www.zeiss.com/metrology/en/software/zeiss-calypso.html
- ZEISS INSPECT product page: https://www.zeiss.com/metrology/en/software/zeiss-inspect.html
- ZEISS Quality Software portfolio (incl. CALIGO, GEAR PRO, PiWeb, device-independence FAQ): https://www.zeiss.com/metrology/en/software.html
- ZEISS Quality Tech Guide (online help; listed as Tier-1 help surface, not article-fetched): https://techguide.zeiss.com/
- Verisurf home (application suites, modules, model-based positioning): https://www.verisurf.com/
- CMM-Manager home (QxSoft; configurations, compatible devices, open architecture): https://www.cmmmanager.com/ (serves https://qxcmm.com/)
- Volume Graphics VGSTUDIO MAX product page (editions, capabilities, reporting, Q-DAS interface): https://www.volumegraphics.com/en/products/vgstudio-max.html
- Aberlink home (Aberlink 3D positioning, modules: CAD Comparison / Programming from CAD / Vision Measurement; PolyWorks reseller page): https://www.aberlink.com/

Blocked (recorded as source-access limitations):

- Hexagon PC-DMIS: https://www.hexagon.com/products/pc-dmis (403) and https://www.hexagonmi.com/products/measurement-software/pc-dmis-cmm-software (403) — abandoned after 2 attempts. No claims made about PC-DMIS.
- InnovMetric PolyWorks: https://www.innovmetric.com/products/polyworks-inspector (451) and https://polyworks.com/ (451) — abandoned after 2 attempts. Secondhand evidence only (Aberlink "PolyWorks Inspector — Discover the Power of PolyWorks on Aberlink CMMs").
- LK Metrology CAMIO: https://lkmetrology.com/software/camio/ (403) — abandoned; LK hardware referenced only via CMM-Manager compatibility list.

Not consulted (not needed for stop conditions): pricing pages, user forums, third-party reviews, video walkthroughs.

## Product Observations

### ZEISS CALYPSO (evidence layer A)

- Positioning: "Your software for coordinate measuring machines: ZEISS CALYPSO measures geometrical elements simply, quickly and reliably. Just click the desired features to configure inspection plans. Combined with ZEISS measuring systems and sensors, you will have a powerful one-stop system."
- **Inspection plan as the central object**: "Create inspection plans with just a few simple clicks and without any programming skills. ZEISS CALYPSO is programmed directly at the workpiece or graphically at the CAD design."
- **Technology independence within the ZEISS fleet**: "combine tactile, optical and multi-sensor coordinate measuring machines as well as roughness sensors by ZEISS in a single inspection plan."
- **Offline planning as an add-on**: "Optional add-ons allow you to create and store entire CNC inspection plans on a remote workstation."
- **PMI-driven plan generation**: "automatically creates inspection plans based on PMI data including all relevant features and characteristics."
- **Versioning**: "All inspection plan variants are versioned. You do not have to work with various copies since everything is managed directly in the inspection plan."
- **Measuring strategies**: integrated tool to implement company-specific measuring strategies or optimize inspection plans per ZEISS recommendations.
- **Reporting via ZEISS PiWeb**: "integrated professional tool for protocol design. Create meaningful visualizations of your measuring results based on either protocol templates or customized reports and templates."
- Options for curve-related features, offline planning, surface analysis of non-standardized 3D geometries; add-on ecosystem; 25+ years of continuous releases; companion products in the same portfolio: CALIGO (freeform car-body surfaces), GEAR PRO (gear metrology), PiWeb (reporting and advanced statistics).

### ZEISS INSPECT (evidence layer A)

- Positioning: "your software to analyze multiple data sources efficiently"; variants: Optical 3D, X-Ray, VMM (vision), CMM; "regardless of which system you use."
- Device independence stated in the portfolio FAQ: "You can also use various ZEISS Quality Software products without a ZEISS system. Our analysis software is device-independent. With ZEISS INSPECT, for example, you can evaluate and analyze your optical 3D or volume data, regardless of the source, and create comprehensive reports."
- **Parametric measurement plans**: "The software saves each inspection step, thereby making measurement plans traceable, repeatable, and editable. With the cluster & pattern function, multiple elements can be easily adapted."
- **Nominal-actual comparison**: "Match polygon meshes to CAD data and visualize deviations using a highly intuitive color scale."
- **GD&T evaluation**: "Check in just a few steps whether the shape and position of your components are within the defined tolerances."
- **Defect inspection**: assisted tools "automatically detect quality issues and categorize them"; AI-based ZADD segmentation for automated defect detection.
- **Reporting**: graphics or tables, presentations or PDFs; PiWeb Reporting Plus app to "organize and visualize your quality data."
- **Automation**: project templates, automatic measurement sequences, script recorder turning actions into editable Python scripts; Virtual Measuring Room app to simulate/automate robotic measurements.
- App ecosystem: 100+ prebuilt apps (e.g., Airfoil Inspection for blades).

### Verisurf (evidence layer A)

- Positioning: "Model-Based Inspection & Measurement Software. One Common Metrology Platform for all 3D Measuring Devices"; "Manufacturers require more reporting, traceability, and continuity of data than ever before. Intelligent 3D CAD models are now the standard design authority in manufacturing."
- **Nominal vs actual in real time**: "Verisurf metrology software lets you see the difference between the nominal CAD design and finished machine part in real-time. Perfect for fast, in-process first article or automated production inspection that improves your manufacturing enterprise."
- **Any CAD / any device**: "Work with any CAD format and measure with any device."
- Suites: Metrology Enterprise; CMM Programming & Inspection ("Object oriented CMM programming with efficient operation and quality reporting for all brands of CMMs"); Inspection & Analysis ("Connect to any manual and portable CMMs for probing and scanning. Inspect to drawings or CAD models with intelligent MBD"); 3D Scanning Inspection & Analysis; Tool Building & Inspection ("Use portable CMMs to build tools, jigs and fixtures. Perform alignments, drift checks, and bundling, and inspect to CAD in real time"); 3D Scanning & Reverse Engineering.
- Modules (menu evidence): CAD, MEASURE, BUILD, ANALYSIS, AUTOMATE, UNIVERSAL CMM, REVERSE, QUICK SURFACE, TRANSLATORS, VALIDATE, SDK, MOBILE.
- Reverse engineering is an adjacent application realized inside the same platform (separate suite), i.e., the Type's edges extend into geometry creation.

### CMM-Manager / QxSoft (evidence layer A)

- Positioning: "Software for any CMM" — "runs inspections on vision systems, manual CMMs, portable devices, and multi-sensor CNC coordinate measuring machines using a single software environment."
- **Fleet standardization / retrofit philosophy**: "replace complicated OEM software with a more intuitive interface… shops can standardize their inspection workflow while making better use of the equipment they already own"; 50+ device brands listed (Zeiss, Mitutoyo, Hexagon/Brown & Sharpe, DEA, Sheffield, LK, Wenzel, Nikon, FARO, Romer, Renishaw Equator, Micro-Vu, Starrett, Aberlink, Coord3, Helmel…).
- **Walk-up and programming**: "object-based interface allows quick walk-up inspection and CMM program creation without complex a text-based programming language."
- **Built-in operational machinery**: "graphical probe configuration management, automatic tip calibration, easy Alignment tools, cross section scanning, built-in Batch execution, and group feature measurement."
- **Offline/remote programming seat** as a product configuration; **native CAD import** as an option; gear inspection and automation as options; DCC Standard / Manual Standard / Vision Systems / Offline configurations.
- **Open architecture / standards**: "DMIS program execution allows running legacy programs from old software. Direct plug-n-play connection along with I++ interface to any CMM. Error Map / Volumetric Correction files are human readable text."
- Tag evidence (site taxonomy): GD&T, ASME, ISO, Excel, reporting, offline, CAD, automation, robot, PLC.

### VGSTUDIO MAX / Volume Graphics (evidence layer A)

- Positioning: "delivers non-destructive insights at every stage of the product lifecycle… full spectrum of inspection tools, from CT reconstruction and AI-based segmentation to GD&T, material analysis, and simulation."
- Editions ladder: Essential (core volume analysis, subvoxel-precise surface determination, entry-level porosity analysis, automation, reporting), **Dimensions** ("Complete GD&T and high-end metrology… full GD&T functionality, pattern creation, and the multipart group concept for building fast, repeatable measurement plans across many parts"), Analyse (material/casting), Battery, Pro.
- Feature inventory: data import (voxel data, meshes, point clouds, CAD IGES/STEP); simple alignments; coordinate measurement; complex alignments; multipart; **nominal/actual comparison**; wall thickness analysis; **CAD import with PMI**; fixture simulation; reverse engineering; porosity/inclusion analysis; fiber composite analysis; volume meshing; CT reconstruction; deep segmentation.
- **Metrology semantics**: "All CT-based metrology relies on accurate surface determination in the voxel model, which reduces measurement uncertainty… subvoxel-accurate and locally adaptive"; alignment features "including Simple 3-2-1 alignment"; reference instruments (distance, polyline length, angle).
- **Multipart automation**: "import an entire batch of CT datasets, apply a single measurement plan to all of them, and deliver the results in one automated run"; CM objects stay synced; dedicated multipart reporting.
- **Reporting and SPC handoff**: "customisable inspection reports, and interface with third-party quality management or statistical process control software like Q-DAS or Metrology Reporting."
- Data-quality machinery: "Monitor the data quality of your CT scans over time… according to ASTM E 1441 and ASTM E 1695."
- Automation "compatible with nearly every CT system."

### Aberlink 3D (evidence layer A; sixth sample)

- Positioning: "Industry standard 2D and 3D measurement software - making measurement easy"; "can work in 2D or 3D, on manual or CNC CMMs and is equally at home when used with either touch, scanning or vision systems"; licensed "by numerous other manufacturers of measuring devices" (bundled-software posture).
- Modules: **CAD Comparison** ("compare points to a CAD model"), **Programming from CAD** ("generate programmes offline"), **Vision Measurement**; automation and tool-offset correction listed as software capabilities.
- CAD as an option, not a precondition — the core offer is feature measurement with 2D/3D evaluation, showing the CAD-based pole is not universal.
- Aberlink also resells PolyWorks Inspector for its CMMs (secondhand evidence of PolyWorks' independent-software posture).
- SMB tier context: contract inspection and contract programming services ("Let us write and maintain your library of inspection programs") — evidence that inspection programs are a maintained organizational asset even at the small-shop tier.

## Cross-product Comparison

| Dimension | ZEISS CALYPSO | ZEISS INSPECT | Verisurf | CMM-Manager | VGSTUDIO MAX | Aberlink 3D |
|---|---|---|---|---|---|---|
| Central repeatable object | inspection plan (versioned) | parametric measurement plan | model-based program (CAD/MBD) | CMM program / walk-up session | measurement plan (multipart) | inspection program |
| Nominal reference | CAD graphic + PMI; workpiece teaching | CAD data (mesh match) | CAD/MBD "design authority", any format | native CAD import (option) | CAD IGES/STEP + PMI | CAD comparison module (optional) |
| Measured data | tactile/optical/multi-sensor CMM + roughness | optical 3D, X-ray volume, VMM, CMM data | probing + scanning on any device | touch/scanning/vision/multi-sensor | voxel/CT volumes, meshes, point clouds | touch/scanning/vision, 2D/3D |
| Device-driving | yes (ZEISS fleet) | no (evaluation-only; machine variants exist) | yes (all brands of CMMs, portable) | yes (50+ brands, DCC/manual/vision) | no (batch import; automation per CT system) | yes (own + OEM-licensed devices) |
| Alignment machinery | measuring strategies | parametric, editable | alignments, drift checks (tool building) | easy Alignment tools, probe config, tip calibration | 3-2-1 and complex alignments | via programs |
| Tolerance semantics | features and characteristics from PMI | GD&T, within-tolerance checks | MBD/GD&T, drawings or models | GD&T, ASME/ISO tags | full GD&T (Dimensions edition) | 2D/3D feature evaluation (GD&T tag on site) |
| Verdict output | measuring results visualized, protocol templates | within-tolerance checks; defect categorization | real-time nominal-vs-part difference | reporting (Excel tag) | measurement results, per-part verdicts | measurement reports |
| Reporting | PiWeb protocol design, templates/custom | graphics/tables/PDF; PiWeb Reporting Plus | quality reporting (per suite text) | Excel reporting tag | customizable inspection reports | inspection reports |
| Results handoff | PiWeb (reporting + advanced statistics) | PiWeb Reporting Plus | (reporting/traceability emphasis) | (Excel; robot/PLC tags) | Q-DAS / Metrology Reporting interface | (not evidenced) |
| Reusable automation | CNC plans; offline add-on | automatic sequences, Python scripts, VMR | AUTOMATE module | batch execution; automation option; DMIS legacy | multipart batch runs; automation | automation capability; offline programming module |
| Offline authoring/simulation | offline add-on (remote workstation) | VMR simulation | CMM programming from CAD | offline seat | fixture simulation | Programming from CAD module |
| Specialist geometry | GEAR PRO, CALIGO freeform | Airfoil app, 100+ apps | tool building/jigs | gear inspection option | wall thickness, porosity, fiber, battery | (none evidenced) |
| Vendor posture | OEM-tied | device-independent | device-independent | device-independent | device-independent (modality-specific data) | OEM + OEM-licensing |
| Customer tier | enterprise OEM fleets | lab/enterprise analysis | aerospace-tier enterprises | mid-market retrofit | lab/enterprise CT | SMB shop floor |
| Deployment signal | machine-bundled, add-on options | 30-day trial, store, subscription/upgrade options | suites + modules | 30-day trial, SSC contract, configurations | edition ladder, trial licenses | bundled with CMMs |

Reading of the matrix: every product holds a **reusable measurement definition** bound to a **nominal reference**, applied to **measured geometry of physical parts**, evaluated under **tolerance semantics**, producing **part-level results/reports**, with **automation/repeatability** machinery around execution. Device-driving varies (INSPECT and VGSTUDIO MAX are evaluation-centric); CAD comparison varies in depth (Aberlink optional, feature-level vs surface-deviation); modality varies fully. These are the variant axes, not the core.

## Canonical Model (Layered Abstraction)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as Inspection & Metrology Software:

```text
Nominal reference
  (the part's intended geometry + its tolerances, held as CAD model
   and/or drawing-derived feature definitions)
    └── Measured part geometry
        (coordinate/surface/volume/image data of a physical part instance,
         acquired from a measuring device or received from measurement systems)
        └── Geometric evaluation against the reference
            (measured data related to nominal in a common coordinate system,
             features constructed from measurements, deviations judged
             against tolerances → per-characteristic results / verdict)
            └── Part-level inspection record
                (results retained and emitted as reports/evidence
                 for the quality process)
```

Four properties:

1. **Nominal reference** — the software holds what the part *should be*: a CAD model and/or drawing-derived definitions of features with dimensions and tolerances. This is the conformance yardstick. Without it the product is a digitizing, scanning, or reverse-engineering tool (measuring to *create* geometry, not to verify it).
2. **Measured part geometry** — actual geometry of a physical part instance captured as points, surfaces, volume voxels, or images by coordinate metrology, optical, or volumetric means, whether the software drives the device live or receives the data. Without it the product is CAD/drawing geometry analysis with nothing measured.
3. **Geometric evaluation against the reference** — measured data is related to the nominal (alignments / common coordinate system), features are constructed from measurements, deviations are computed and judged against tolerances, producing per-characteristic results and an overall verdict. Without it the product is a measurement-data logger or viewer.
4. **Part-level inspection record** — the results are retained per part/session and emitted as reports (dimensional report, deviation map, results tables) that serve as quality evidence downstream. Without it the product is a live readout instrument; the evidence purpose of inspection collapses.

Jointly-held load-bearing:

- 1 without 2+3 = CAD/tolerance documentation or PMI checker
- 2 without 1+3 = scanner/digitizer data tool (reverse-engineering capture)
- 1+2 without 3 = mesh/CAD visualization without conformance semantics
- 1+3 without 2 = design-side geometry analysis (no measurement)
- 2+3 without 1 = measurement data processing with no conformance purpose
- 3+4 without 1 = SPC / measurement-data collection territory
- 4 without 1+2+3 = inspection paperwork (QMS territory)

Historical check (§24): the paper-era form — an inspector reads dimensions from a drawing (nominal + tolerances), measures with calipers/micrometer, writes actual vs nominal vs tolerance with pass/fail, and files the inspection report — satisfies all four properties with zero software machinery. 1980s/90s CMM software with part programs, alignments, and printed measurement protocols satisfies it. Shop-floor digital-gage logging against drawing tolerances satisfies it. The definition therefore holds no CAD import, no offline programming, no point clouds/CT, no PMI, no automation, and no specific device kind in the core.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Inspection plan / part program / measurement plan** as the reusable, editable, versioned definition of what to measure and how (CALYPSO versioned inspection plans; INSPECT parametric plans; CMM-Manager programs + walk-up; VG multipart measurement plans; Verisurf model-based programs; Aberlink program libraries)
- **Offline authoring from CAD** and/or **PMI-driven plan generation**; teach-at-the-workpiece authoring as the alternative
- **Alignment machinery** — relating part coordinate system to machine/data coordinate system (3-2-1, datum/best-fit); probe/sensor configuration and tip calibration
- **Execution machinery** — guided run modes, DCC machine control, batch/multi-part runs, group/pattern features, cross-section scanning
- **Simulation/collision avoidance** for offline paths (fixture simulation, virtual measuring room)
- **Nominal-actual comparison visualization** — color-coded deviation maps over the CAD/mesh, beyond per-feature tables
- **Feature/construct library** — geometric elements (planes, cylinders, curves), constructions, curve-related options
- **Rich reporting** — protocol templates, custom report design, graphics/tables/PDF/Excel export
- **Results storage and traceability** per part and per plan version
- **Handoff to statistics/reporting platforms** — PiWeb-class reporting/advanced statistics; Q-DAS-class SPC interfaces
- **Device abstraction across modalities** — one environment over CMM/portable/vision/CT families; standard interfaces (I++ DME, DMIS-class programs)
- **Scripting/automation APIs** (Python scripts, macro recorders, robot integration)

### L2 — Variant / Optional Structure

- **Device modality** as the product-family axis: tactile CMM / manual CMM / portable arm & laser tracker / vision & multisensor / optical scanner / industrial CT — often a whole product line each
- **Vendor posture**: OEM-tied (bundled with own machines, "one-stop") vs device-independent (multi-brand fleets, retrofits) vs data-evaluation-only
- **Execution posture**: machine-driving inspection (DCC/CNC) vs operator-driven (manual/walk-up) vs post-hoc evaluation of acquired data
- **Offline vs online programming**; simulation depth
- **Specialist geometry packages**: gears, airfoils/blades, freeform car-body surfaces, curves
- **First-article inspection orientation** (aerospace-style reporting; evidenced as a named use in one sample's positioning, common in the market)
- **Volumetric extensions**: wall thickness, porosity/inclusion analysis, material/fiber analysis, battery analysis (CT pole)
- **Defect detection machinery**: assisted and AI-based defect detection/segmentation
- **Adjacent capability bundling**: reverse engineering, tool/jig building with drift checks, on-machine probing
- **Regulated-industry evidence depth** (aerospace/automotive traceability emphasis)
- **Licensing shapes**: machine-bundled, module/option ladders, edition ladders, subscriptions, trials

### L3 — Vendor-specific (kept out of the final document)

- ZEISS: CALYPSO 25+ year release lineage and option/add-on model; PiWeb (reporting + advanced statistics) and PiWeb Reporting Plus; CALIGO (freeform car bodies); GEAR PRO; ZEISS Quality Suite / Quality Software Store / Tech Guide / Quality Forum; ZADD AI segmentation; Virtual Measuring Room; Airfoil app; 100+ app ecosystem; Python script recorder; device-independence FAQ statement; O-DETECT/DuraMax machine pairings
- Verisurf: module names (MEASURE/BUILD/ANALYSIS/AUTOMATE/UNIVERSAL CMM/REVERSE/QUICK SURFACE/TRANSLATORS/VALIDATE/SDK/MOBILE); Master3DGage/3DGage/CMM Master hardware; Verisurf University; partner hardware wall (FARO, Nikon, Renishaw, Wenzel…); customer logos (SpaceX, Boom, Haas F1)
- QxSoft: CMM-Manager configurations (DCC/Manual/Vision/Offline); SSC service contract; weekly web demos; made-in-USA; QxSoft/Nikon lineage; DMIS + I++ + human-readable error-map openness; 50+ brand compatibility list
- Volume Graphics: edition ladder (Essential/Dimensions/Analyse/Battery/Pro); ASTM E 1441/E 1695 data-quality conformance; multipart handling claims (handling-time reduction); myVGL free viewer; VGMETROLOGY/VGinLINE siblings; Hexagon rebrand
- Aberlink: Axiom/Halo/Extol CMM lines; Kings Award 2024; no-annual-maintenance posture; contract inspection/programming services; UK manufacturing identity

## Vendor-specific Findings

- ZEISS INSPECT is the strongest single piece of evidence that device-driving is NOT invariant: an OEM's own inspection-analysis product is sold as evaluating data "regardless of the source," and the portfolio FAQ makes device independence explicit for analysis software.
- VGSTUDIO MAX shows the evaluation-only pole in the volumetric modality and also shows the sharpest published SPC boundary: it explicitly names third-party SPC software (Q-DAS, Metrology Reporting) as the downstream consumer of its results.
- CMM-Manager's compatibility list (50+ brands, incl. rivals' machines) is the clearest evidence that the *software layer* is a market distinct from the *machine layer*, and that inspection programs are long-lived assets worth porting (DMIS execution of legacy programs).
- CALYPSO's inspection-plan versioning ("managed directly in the inspection plan") is the best direct evidence that plans are governed, versioned objects rather than disposable scripts.
- Aberlink 3D proves the no-CAD-required floor: 2D/3D feature measurement software with CAD comparison as an optional module.
- Verisurf's tool-building suite (alignments, drift checks, bundling) shows the Type's extension into building/verifying tooling — measured objects are not limited to production parts.
- CMM-Manager's "automatic tip calibration" is a device-side probe qualification routine inside inspection software; it is not instrument-lifecycle calibration management (do not confuse with Calibration Management Type).

## Boundary Findings

- **vs Calibration Management (§16, pre-hung)**: inspection/metrology software measures *products*; calibration management assures the *instruments*. The two interlock (inspection assumes qualified/calibrated devices; probe qualification routines live inside inspection software), but the managed object differs. Remove the product-conformance loop and keep instrument fitness → calibration management.
- **vs Statistical Process Control / SPC (§16)**: SPC consumes time-ordered streams of characteristic values to control *processes* (control charts, capability); inspection software produces part-level *geometric conformance*. The handoff is an interface (VGSTUDIO MAX → Q-DAS/Metrology Reporting; CALYPSO/INSPECT → PiWeb). Remove the geometry/nominal semantics and keep statistical process monitoring → SPC.
- **vs Mechanical CAD (§04.13-adjacent / MCAD)**: CAD authorsthe nominal design; inspection software consumes it as the reference and never authors the design. Bundled CAD/translators modules (Verisurf CAD, translators) exist to *import* nominal geometry.
- **vs CAM / CNC Programming (§16)**: parallel program-authoring loops (offline programming, simulation, machine execution) but CAM writes *material-removal* paths for machine tools; inspection programming writes *measurement* paths for measuring machines and its output is a verdict, not a part. On-machine probing blurs the edge at the execution site, not in the core.
- **vs Machine Vision Platform (§16)**: production-line vision systems classify/detect/guide at line rate; metrology software produces traceable dimensional evaluation of parts with tolerance verdicts. Overlap exists (vision-based measurement systems are supported devices in CMM-Manager/ZEISS VMM variants); the discriminator is metrology-grade geometric conformance reporting vs automated high-rate machine control.
- **vs 3D Modeling / Photogrammetry / Reverse Engineering (§04.13)**: those create geometry from scans; inspection judges scans against an existing nominal. Products bundle RE modules (Verisurf RE, ZEISS REVERSE ENGINEERING, VG reverse engineering) — capability drift across the seam, with the conformance loop as the Type's center.
- **vs Manufacturing QMS (§16)**: inspection software produces the measurement evidence; QMS holds the quality system (nonconformance, CAPA, audits, documents). Reports flow QMS-ward; the QMS core objects are absent here.
- **vs Product Test Management / Industrial Laboratory Management (§16/§23)**: product tests are functional/performance trials; lab management runs lab operations (samples, bookings). The metrology Type's object is part geometry vs declared nominal.
- **vs Government/Property/Home/Construction Inspection Management (other families)**: same word "inspection," entirely different object (premises/regulatory conditions vs manufactured parts), different operator and output. Multiple processed documents already cross-reference this leaf with that distinction; this research corroborates it: no regulatory-case machinery exists anywhere in the sampled products.
- **"Measurement software" ambiguity**: the word also names device firmware/control panels (digital readouts, sensor consoles). Those lack the nominal/tolerance conformance loop and report-of-record — instrument territory, not this Type.

## Uncertainties

- No numeric limits, accuracy figures, default settings, or pricing asserted anywhere (none consistently evidenced).
- PC-DMIS (market-leading CMM software by general industry reputation) could not be fetched; its absence from the evidence base is recorded. The L0 does not depend on it, but the "offline programming from CAD" L1 claim is supported by 5 of 6 sampled products rather than by the market leader directly.
- PolyWorks Inspector's exact posture (its point-cloud/module structure) is unverified; kept out of all claims.
- Whether any in-type product exists with *no* report/record output at all was not observed (all sampled products lead with reporting); L0 leg 4 rests on cross-product evidence plus the paper-era conceptual check.
- First-article reporting depth (e.g., standardized FAI form structures) was not evidenced at the level of specific form machinery in fetched pages; held at "recognized use/variant" strength only.
- Roles/permissions inside these products were not evidenced in fetched material; not claimed in the final document.
- ZEISS INSPECT CMM/VMM machine-variant boundaries (which machine pairs with which INSPECT variant) are vendor-stated and not independently verified.

## Final Synthesis

Inspection & Metrology Software is the manufacturing software layer whose unit of work is a physical part's conformance to its declared geometry. It holds the nominal reference (CAD model and/or drawing-derived features with tolerances), takes in measured geometry of real parts from coordinate, optical, or volumetric measuring devices (driving the device or receiving its data), relates measurement to nominal through alignment and feature construction, judges every characteristic against tolerance, and retains the result as the part's inspection record and report. Around this core, mature products add the reusable inspection plan (authored offline from CAD/PMI or taught at the machine), probe/sensor configuration and qualification, batch and automated execution with simulation, deviation-map visualization, template-driven reporting, results handoff to SPC/reporting platforms, and multi-device abstraction across CMMs, portable arms, vision systems, and CT. The market splits along three variant axes — device modality, vendor posture (OEM-tied vs device-independent), and execution posture (drive-the-machine vs evaluate-the-data) — with products spanning SMB shop-floor bundles to aerospace-grade model-based enterprises. Its sharpest boundaries: instruments vs products (Calibration Management), process statistics vs part conformance (SPC), nominal creation vs nominal consumption (CAD), making vs verifying (CAM), and line-rate classification vs metrology-grade verdicts (Machine Vision).
