# Inspection & Metrology Software

## Overview

An **Inspection & Metrology Software** application verifies that a manufactured physical part conforms to its declared geometry. It holds the part's nominal reference — a CAD model and/or drawing-derived feature definitions carrying dimensions and tolerances — brings in measured geometry of real parts from coordinate measuring machines, portable measuring devices, vision systems, scanners, or industrial CT, evaluates the measurement against the reference, judges each characteristic against its tolerance, and retains the result as the part's inspection record.

The defining core is small:

```text
Nominal reference (CAD model / drawing-derived geometry + tolerances)
└── Measured part geometry (points, surfaces, volumes, or images of a physical part)
    └── Geometric evaluation against the reference
        (alignment, feature construction, deviation, tolerance judgment)
        └── Part-level inspection record (retained report and evidence)
```

Everything else the market associates with the category — offline programming from CAD, automated machine execution, deviation color maps, statistical handoff, multi-device fleets — is widespread in mature products but not part of what makes the software what it is. The software layer is deliberately distinct from the measuring hardware: machines acquire data, but it is here that nominal meets actual, the verdict is produced, and the evidence is kept.

When the dominant purpose shifts from verifying a part against its declared geometry — to controlling a process statistically, creating geometry from scans, making the part, or inspecting premises and facilities for regulatory conditions — the product has drifted into a neighboring Application Type.

## Users & Context

The people in front of this software are quality and metrology staff in manufacturing:

- **Metrology technicians and machine operators** run inspections on measuring machines — loading an inspection program, setting up the part, aligning it, executing the run, and responding to what the software guides or the machine performs.
- **CMM / metrology programmers** author the reusable inspection programs, typically offline from the CAD model: which features to measure, in which order, with which sensors, and against which tolerances.
- **Quality inspectors and quality engineers** define what must be checked for a part or revision, evaluate results, disposition parts, and own the inspection records as quality evidence.
- **Shop-floor operators** perform walk-up measurements at the point of production — quick checks without deep programming skills — on smaller devices and manual machines.

Secondary consumers read the output rather than operate the software: quality managers reviewing results, downstream statistical process control consuming characteristic values, design and manufacturing engineering studying deviation patterns, and auditors or customers receiving the reports as objective evidence.

Typical settings: the dimensioning room or metrology laboratory next to production; inspection cells on the shop floor; in-process checks during machining; first-article verification before a production run is released. Vendor industry framing commonly names automotive, aerospace, medical, electronics, and energy — settings where dimensional conformance carries contractual or regulatory weight.

## Core Model

### The Defining Core

Four structures. If any one is removed, the software stops being recognizable as this Type:

- **Nominal reference** — what the part *should be*, held as a CAD model and/or definitions derived from the drawing: geometric features (planes, cylinders, circles, curves, freeform surfaces), their nominal dimensions, and their tolerances. This is the yardstick the software measures against. Without it the product is a digitizing or scanning tool — measuring to *create* geometry (reverse engineering), not to verify it.
- **Measured part geometry** — the part *as it actually is*, captured as discrete points, scanned surfaces, volumetric voxel data, or images of one identified physical part instance. The software may drive the measuring device live or receive data the device has already produced. Without it the product is CAD or drawing analysis — geometry checked on the screen with nothing ever measured.
- **Geometric evaluation against the reference** — the measured data is related to the nominal in a defined coordinate relationship (alignment), features are constructed from the measurements, deviations from nominal are computed, and each characteristic is judged against its tolerance — producing a per-characteristic result and, rolled up, a verdict for the part. Without it the product is a measurement data logger or viewer.
- **Part-level inspection record** — the results are retained per part and session and emitted as inspection reports — result tables, deviation maps, verdicts — that serve as the quality evidence for the part. Without it the product is a live readout instrument; the evidentiary purpose of inspection collapses.

The structures are jointly held: a tolerance checker with no measurement is CAD analysis; a scanner with no nominal is a digitizer; measurement with no evaluation is telemetry; evaluation with no retained record is a gauge display.

### What Mature Products Add

Mature products carry a layer of standard capabilities around that core. These make inspection practical and repeatable, but they do not define the Type:

- **The inspection plan (part program / measurement plan)** — the reusable, editable, commonly versioned definition of what to measure and how: the features, the characteristics, the measuring strategies, the order. Plans are authored offline from the CAD model (increasingly generated automatically from the tolerancing information embedded in the model, or from drawing-derived definitions), or taught directly at the machine. Mature products treat plans as governed, long-lived assets — some organizations maintain their program libraries as a managed service.
- **Alignment and setup machinery** — relating the part's coordinate system to the measurement system's (commonly structured patterns such as datum-based or 3-2-1 alignments), plus probe and sensor configuration and measuring-tip qualification.
- **Execution machinery** — guided run modes for operators, direct control of motorized measuring machines, batch and multi-part runs, group and pattern measurement, cross-section scanning.
- **Simulation** — collision checking and path verification for offline-authored programs, extending in some products to full simulated measurement environments including robots.
- **Deviation visualization** — color-coded nominal-versus-actual comparison rendered over the model surface, alongside per-characteristic tables.
- **Feature and construct libraries** — geometric elements, constructions, and curve or freeform evaluation options.
- **Reporting machinery** — protocol templates, custom report design, exports to document and spreadsheet formats, graphical presentations of results.
- **Results traceability** — results stored per part and per plan version, so any report can be traced to the plan that produced it.
- **Statistics handoff** — interfaces that pass characteristic values to reporting and statistical process control platforms.
- **Multi-device abstraction** — one software environment spanning coordinate measuring machines, portable arms and trackers, vision and multi-sensor systems, and scanning or CT data. Device-independent products commonly support large mixed fleets — one sampled product documents compatibility with more than fifty machine brands and the execution of legacy program formats so programs survive machine changes.
- **Scripting and automation APIs** — recorded or hand-written scripts, automatic measurement sequences, robot integration.

### One Structure, Many Implementations

The core is written conceptually; implementations vary deliberately:

```text
Concept:   Nominal reference
Realized as:  CAD model with embedded tolerancing, drawing-derived feature
              definitions, or both; from full surface comparison down to
              a handful of drawing dimensions

Concept:   Measured part geometry
Realized as:  touch-probe points, scanned point clouds and meshes,
              vision images, CT voxel volumes — on lab machines,
              shop-floor devices, or imported from anywhere

Concept:   Geometric evaluation
Realized as:  feature-level dimension/GD&T judgment, surface deviation
              mapping, wall-thickness and volumetric analyses

Concept:   Inspection record
Realized as:  protocol reports, deviation color maps, result tables,
              exported datasets
```

A reader who has only seen CAD-driven CNC coordinate measuring machines should still recognize a walk-up shop-floor system or an evaluation-only CT analysis station as the same Type from this model.

## How It Works

The canonical loop runs from declared intent to retained evidence:

```text
Establish the nominal
  → import the CAD model or define features from the drawing;
    tolerances arrive with the model or are entered from the drawing
→ Author the inspection plan
  → select features and characteristics, define measuring strategies,
    configure probes/sensors — offline with simulation, or at the machine
→ Set up and execute
  → fixture the part, align it (establish the part's coordinate
    relationship to the measurement), run the program or follow
    the guided steps, acquire the data
→ Evaluate
  → construct features from measurements, compute deviations,
    judge every characteristic against its tolerance
→ Report and retain
  → produce the inspection report, store it against the part and
    plan version, pass results onward to statistics where used
```

Two recognized postures shorten or reshape the loop. **Walk-up inspection** collapses authoring and setup into operator-guided steps on the machine — measure features, see results immediately, save the session as the record. **Evaluation-only workflows** begin where the loop normally ends: measured data (scans, volumes) is imported from any source, and the software aligns, evaluates, and reports without ever touching a device.

### Core vs Standard vs Optional

**Defining core** — without these, not this Type:

- nominal reference (CAD and/or drawing-derived geometry with tolerances)
- measured part geometry of a physical part
- geometric evaluation against the reference with per-characteristic results
- part-level inspection record

**Standard in mature products:**

- reusable inspection plans with versioning
- alignment machinery and probe/sensor configuration
- guided execution, machine control, batch runs
- deviation visualization and template reporting
- results traceability per part and plan
- statistics/reporting handoff
- multi-device support and automation APIs

**Varies by product and segment:**

- device modality (tactile, portable, vision, scanning, CT)
- offline authoring depth and simulation
- evaluation depth (feature tables vs full-surface comparison vs volumetric analysis)
- specialist geometry packages (gears, blades/airfoils, freeform surfaces)
- volumetric extensions (wall thickness, porosity and inclusion analysis, material analysis)
- assisted or AI-based defect detection
- bundled adjacent capabilities (reverse engineering, tool and jig building)
- first-article-inspection-oriented reporting

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Plan editor / programming environment

The authoring surface, usually organized around the CAD view.

- typical information: the model or feature set, the plan's feature list and characteristics, tolerances, measuring strategies, probe/sensor assignments
- primary actions: import CAD, select features, define characteristics and tolerances, order the measurement sequence, simulate paths, version and save the plan

### Run / measurement view

The execution surface at the device.

- typical information: current feature and position, live machine or sensor status, acquired points, progress through the plan
- primary actions: start/pause execution, align the part, drive or jog axes (where machine-controlled), confirm operator prompts, capture features manually (walk-up mode)

### Results / evaluation view

The verdict surface.

- typical information: per-characteristic table (nominal, actual, deviation, tolerance, in/out-of-tolerance state), overall part verdict, deviation color map over the model, trend views where kept
- primary actions: recompute, investigate a characteristic, annotate, assemble the report

### Report designer and viewer

The evidence surface.

- typical information: template library, part and plan identification, result tables, graphics
- primary actions: apply or design templates, generate the report, export (document, spreadsheet, or platform formats), archive

### Device connection / setup surfaces

The machine-side surfaces that bind software to hardware.

- typical information: connected machines and sensors, probe configurations, tip qualification state, machine compatibility settings
- primary actions: connect and select a device, configure and qualify probes/tips, manage error-correction or machine-specific settings

### Plan and result management

The library surface for the repeatable assets.

- typical information: plan versions and their changes, stored results per part and revision, batch sessions
- primary actions: manage versions, retrieve prior results, launch batch runs, hand data to reporting/statistics platforms

## Important Rules / Behaviors

### The alignment governs validity

Every result is only meaningful within a defined coordinate relationship between part and measurement system. Alignment is therefore a first-class, recorded step in every product's loop, with structured patterns (datum-based, 3-2-1) and — in tool-building contexts — repeated drift checks to confirm the setup still holds. An evaluation without a traceable alignment is not a usable result.

### Plans are governed, repeatable objects

Inspection plans (programs) are versioned and traced rather than disposable scripts: some products manage plan variants directly within the plan object itself, parametric systems record every step so plans stay editable and repeatable, and organizations treat program libraries as maintained assets — some even contracting them out as a service. Running the same plan against the same part should produce comparable results; that repeatability is what makes the records trustworthy evidence.

### The verdict is per-characteristic and rolls up

Each characteristic is judged individually against its own tolerance; the part-level outcome is assembled from the per-characteristic results. Evaluation depth varies — a drawing dimension judged from probe points, a geometric tolerance evaluated on constructed features, a full surface deviation map — but the characteristic-by-characteristic judgment is the constant output shape.

### Results are evidence

The report is designed for parties who were not in the room: the quality system, an auditor, a customer. Reports identify the part, the plan, and the results together; results are stored per part and plan version so any historical report can be traced to what produced it. This is why versioned plans, recorded alignments, and retained result histories are structural rather than conveniences.

### Measuring-system setup is a managed step

Probe configuration, measuring-tip qualification/calibration, and sensor settings are part of the operational loop inside the software — the inspection's trustworthiness depends on a qualified measuring system. (The lifecycle management of the instruments themselves belongs to a different Type; see Related Application Types.)

### Data quality is itself checked in volumetric modalities

In CT-based inspection the scan data's own resolution and contrast are monitored over time — some products conformance-check data quality against named ASTM practices — because every downstream measurement inherits the data's quality. This layer is modality-specific rather than universal.

## Variants

- **By device modality** — tactile coordinate measuring machines (manual and CNC), portable arms and laser trackers, vision and multi-sensor systems, optical scanners, industrial CT. Modality so strongly shapes product families that entire product lines exist per modality, yet the core model is shared.
- **By vendor posture** — OEM-bundled software sold as a one-stop system with the vendor's own machines; device-independent software that standardizes mixed fleets and retrofits older machines (often explicitly marketed as replacing OEM software); and evaluation-only software that never drives a device and analyzes acquired data from any source.
- **By execution posture** — machine-driven inspection (CNC execution of authored programs), operator walk-up measurement (guided, low-programming), and post-hoc evaluation of imported data.
- **By customer tier and industry** — SMB shop-floor bundles (easy-to-use software sold with the machine, modest programming depth) through aerospace- and automotive-grade environments (model-based definition as design authority, heavy traceability, first-article reporting).
- **By geometry specialty** — packages for gears, turbine blades and airfoils, freeform body surfaces; volumetric extensions for wall thickness, porosity and inclusions; assisted and AI-based defect detection.
- **Bundled adjacent capabilities** — reverse engineering (measuring to create geometry), and tool/jig/fixture building with alignment and drift checks. Products bundle these without their presence defining the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Calibration Management | interlocking sibling | calibration management assures the *instruments* (fitness, intervals, certificates); this Type measures the *products*. Inspection assumes qualified instruments; probe-tip qualification inside inspection software is a device setup step, not instrument lifecycle management |
| Statistical Process Control / SPC | downstream consumer | SPC consumes time-ordered characteristic values to control the *process* (control charts, capability); this Type produces part-level *geometric conformance*. The handoff is an interface, and the geometry/nominal semantics live only here |
| Machine Vision Platform | adjacent, sometimes overlapping hardware | line-rate automated vision classifies, detects, and guides production; this Type produces traceable dimensional verdicts on parts. Vision measurement systems can be supported devices here; the metrology-grade conformance loop is the discriminator |
| Mechanical CAD | upstream | CAD *authors* the nominal design; this software *consumes* it as the reference and never authors the design. Bundled CAD/translators exist to import nominal geometry |
| CAM / CNC Programming | structural parallel | same authoring loop (offline programming, simulation, machine execution) but CAM writes material-removal paths that *make* the part; inspection programs write measurement paths that *verify* it. Where measurement happens on a production machine rather than a dedicated measuring machine, the execution site blurs — the program's purpose (verify, not make) does not |
| 3D Modeling / Photogrammetry / Reverse Engineering | edge overlap | those create geometry from scans; this Type judges scans against an existing nominal. Reverse-engineering modules bundled into inspection products are capability drift across the seam |
| Manufacturing QMS | evidence producer | the QMS holds the quality system (nonconformance, CAPA, audits); this Type produces the measurement evidence the QMS references. QMS core objects are absent here |
| Product Test Management | different verification object | product tests exercise *function and performance*; this Type verifies *geometry* against declared nominal |
| Government / Property / Home Inspection Management | name-cousin only | those manage inspections of premises and regulatory conditions by agencies or service firms; this Type measures manufactured parts. Different object, operator, and output entirely |
| Industrial Laboratory Management | co-located | lab management runs lab operations (samples, bookings, resources); this Type is the measurement-and-verdict system itself |

The most operationally confused boundary is with SPC: both live in quality departments and share characteristic data. The discriminator is the object — a part judged against its declared geometry (here) versus a process judged from its statistical behavior over time (SPC).

## Representative Products

- **ZEISS CALYPSO** — OEM-bundled coordinate measuring machine software; inspection-plan paradigm with PMI-driven plan generation and versioned plans
- **ZEISS INSPECT** — device-independent evaluation of optical 3D and X-ray volume data; parametric measurement plans, app ecosystem
- **Verisurf** — model-based inspection across any CAD format and any measuring device; portable and CMM inspection, first-article orientation
- **CMM-Manager (QxSoft)** — device-independent software for mixed and legacy fleets; walk-up and offline programming across 50+ machine brands
- **VGSTUDIO MAX (Volume Graphics)** — CT-based volumetric inspection and metrology; GD&T on volume data, batch measurement plans, defect analysis

The core model was additionally checked against a small-shop bundled product (Aberlink 3D — 2D/3D measurement software with CAD comparison as an optional module) to avoid over-fitting the definition to CAD-driven, machine-driven, or enterprise patterns.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (product pages and official product documentation):

- ZEISS — CALYPSO product page: https://www.zeiss.com/metrology/en/software/zeiss-calypso.html
- ZEISS — INSPECT product page: https://www.zeiss.com/metrology/en/software/zeiss-inspect.html
- ZEISS — Quality Software portfolio and device-independence FAQ: https://www.zeiss.com/metrology/en/software.html
- ZEISS — Quality Tech Guide (online help): https://techguide.zeiss.com/
- Verisurf — product home, suites, and modules: https://www.verisurf.com/
- QxSoft — CMM-Manager product home, configurations, compatibility: https://www.cmmmanager.com/ (serves https://qxcmm.com/)
- Volume Graphics — VGSTUDIO MAX product page: https://www.volumegraphics.com/en/products/vgstudio-max.html
- Aberlink — product home and software module pages: https://www.aberlink.com/

> Sourcing limitation: official pages for Hexagon PC-DMIS, InnovMetric PolyWorks, and LK Metrology CAMIO were not reachable from the research environment (blocked responses; recorded in the paired Research Notes). No product-specific claims rely on them; PolyWorks appears only as secondhand evidence via a reseller page. Precise operational details (numeric limits, accuracy figures, default settings, licensing specifics) are intentionally not stated in this document; detailed product observations and cross-product evidence are recorded in the Research Notes.

Detailed product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
