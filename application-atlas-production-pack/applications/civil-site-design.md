# Civil / Site Design

## Overview

A **Civil / Site Design application** is the authoring environment in which a practitioner designs proposed modifications of the land — roads and corridors, graded sites, and (typically) gravity drainage and sewer networks — against measured existing terrain, and turns that design into the annotated engineering documentation used to evaluate, approve, stake and construct the works.

The defining structure is small:

```text
Real-world-scaled land project anchored to measured existing ground
└── Proposed land-form design objects
    ├── linear routes (horizontal alignment + vertical profile + cross-section shape)
    └── graded proposed surfaces (pads, basins, embankments, site layouts)
        └── evaluated against the existing ground (cut/fill, volumes, cover)
            └── design-data-driven documentation (plans, long sections,
                cross sections, setout, volume reports)
```

Everything else the category is known for — drainage networks, superelevation rules, intelligent intersections, surface analysis displays, BIM exchange — is standard in mature products but is not what makes the software a civil/site design application. Tools that only view or record existing conditions (GIS), only capture survey data (surveying), or only measure and price a finished design (quantity takeoff) do not satisfy the structure above, because none of them authors proposed land-form objects against measured terrain.

The leaf's two named poles share one loop: **"Civil"** design (roadway and infrastructure corridors) and **"Site"** design (land development and grading) both survey the existing ground in, author land-form objects against it, evaluate earthworks and rules, and publish design-driven documentation. Products differ mainly in where the intelligence sits — rule-driven template objects versus hand-edited strings — not in the underlying structure.

## Users & Context

The primary user is a **civil engineer or civil designer** — in a land-development consultancy, a roadway/infrastructure consultancy, a municipal (council/public-works) engineering team, or a surveying firm that also designs. The application is their main working surface across a project's design life:

- **Land development**: subdivisions — residential road networks, lot grading, drainage — plus pads, detention basins, driveways and parking.
- **Roadway and infrastructure**: new roads and highways, road reconstruction (resurfacing/overlay), intersections and roundabouts, rural roads with ditches and drainage.
- **Municipal works**: drainage upgrades, crossing improvements, small-scale reconstructions designed in-house.

Secondary users include surveyors, who supply the existing-ground data (and in some products also run the design themselves); drainage engineers, who often analyse the networks in specialist tools fed by the design; and construction teams, who consume the documentation and setout. Managers configure the office's drafting standards, templates and regional rule tables rather than design directly.

The work is overwhelmingly desktop professional software. Several products run as engines inside a general CAD platform; others are standalone packages. Web and mobile surfaces are companions (viewing, model review) rather than the design surface.

## Core Model

### The defining core

**1. The land project and its existing ground.** The center of the application is a persistent, real-world-scaled project whose base datum is **measured existing terrain** — surveyed points, imported surface data (points, LandXML, drawing geometry, or level text lifted from legacy 2D survey drawings), assembled into a ground model/surface. Everything the design does is expressed against this base. Real-world scale is intrinsic: coordinates, elevations, chainage/stationing are true-world values, which is why setout and exports preserve measurement.

**2. Proposed land-form design objects.** The practitioner authors two kinds of real geometry that reshape the ground:

- **Linear routes** — a horizontal alignment (the route in plan, built from straight/curve/spiral segments and editable at its intersection points) plus a vertical profile (the route's elevations, edited graphically in a long-section window), shaped in cross section by a reusable **section template** (pavement, kerbs, shoulders, ditches). Roads, channels and utility corridors are all routes. Junction machinery ties routes together (kerb returns, cul-de-sacs, roundabouts, interchanges).
- **Graded surfaces** — proposed terrain created by assigning grades/slopes to outlines (building pads, detention basins, embankments, site areas) with **batter/daylighting** slopes that tie the design edge into the existing ground; some products add automatic corner cleanup at grading outlines and stepped grades for linear features along designs such as utility strips.

**3. The existing-vs-proposed relationship.** The design is continuously evaluated as a modification of measured terrain: cut/fill **earthwork volumes** between existing and proposed surfaces (with compaction/bulking adjustments), depth/cover relationships (pavement layers, pipe cover), and slope conditions along ties. Surface comparison displays — elevation banding, depth bands, slope arrows — make this relationship visible. This is the semantic that separates land design from drawing: the objects are not lines on a sheet but proposed ground whose difference from the surveyed ground is the thing being engineered.

**4. Design-data-driven documentation.** The deliverable is generated from the design objects and updates with them: annotated **plans**, **long sections (profiles)**, **cross sections** at chainage intervals, **setout tables** (coordinates/points for staking), **volume reports**, and pit/pipe schedules — composed into sheets that follow the office's or jurisdiction's drafting standards. A design change regenerates the affected drawings; products compete on how completely and how quickly this happens.

### Standard capabilities of mature products

Most current products carry the following. They make the design efficient and the deliverable complete, but a product can be a genuine civil/site design tool without all of them:

- **Drainage and sewer networks** — networks of pits/manholes and pipes laid out along runs or converted from polylines/alignments; initial sizing from minimum slope/cover and flow rules; invert levels, hydraulic-grade-line display on long sections; clash checks against other services; pipe/pit schedules.
- **Superelevation rules** — crossfall applied through curves from speed, radius and maximum-superelevation criteria, held in editable rule tables so regional practice can be configured.
- **Conditional earthwork machinery** — batters, ditches and benching that switch on/off or change slope by cut/fill depth conditions along the design.
- **Intelligent junction objects** — kerb returns, cul-de-sacs, roundabouts and similar elements that re-position and re-grade themselves when the roads they join change.
- **Surface analysis displays** — contours, elevation banding, slope ranges/directions, depth-band colouring between surfaces.
- **Road reconstruction support** — overlay/resheet depths, matching existing surface controls, multi-layer subgrade volumes.
- **3D model review** — a model viewer/3D window to inspect roads, junctions and grading as they develop.
- **Data exchange** — LandXML, CAD formats, IFC for BIM delivery, COGO points; survey data import; exports to other design, analysis and collaboration environments.
- **Analysis-tool exchange** — links to specialist hydrology/hydraulics packages: catchment and network geometry out, results (flows, water levels, hydraulic grade lines) back for documentation.
- **Regional standards localization** — output styles, superelevation and design-criteria tables, and named national manuals configured per market.

### One structure, several realizations

The core is stable, but products realize it with visibly different philosophies, and this explains most of what looks like disagreement between them:

```text
Concept:            linear route
Realizations:       alignment + profile objects edited via IPs and tables;
                    "string" networks of connected 3D lines;
                    road networks with auto-generated junction elements

Concept:            cross-section shape
Realizations:       named template/assembly libraries (editable);
                    slope/node instructions on a corridor;
                    fixed templates chosen from a supplied catalog

Concept:            existing ground
Realizations:       TIN surfaces from survey points/LandXML;
                    ground models converted from 2D level text;
                    surfaces imported from a survey-adjustment package

Concept:            tie-in to existing ground
Realizations:       daylight/batter objects with slope rules;
                    interface grades from design edge to a chosen ground model;
                    conditional ditches/benching by depth ranges

Concept:            drainage design
Realizations:       full in-product sizing/levelling; exchange with a
                    specialist drainage-analysis package; both in one product
```

A reader who has only seen one product should still be able to recognize the others from the core structure above.

## How It Works

A typical project moves through the following loop — iteratively, not strictly linearly:

**1. Bring in the existing ground.**
Import the survey — points and breaklines, surface files, drawing geometry, or level text from legacy 2D drawings — and build/verify the existing-ground surface. In CAD-platform products, existing survey objects may arrive from a companion survey/adjustment workflow.

**2. Lay out the design.**
Draw or convert the horizontal geometry: alignments for roads, utilities and channels; outlines for pads, basins and site areas. Convert polylines into intelligent objects; set design criteria (speed where relevant, typical sections, slopes).

**3. Design vertically.**
Edit profiles in long-section windows against the existing ground; apply superelevation rules through curves; set pad and basin levels; apply grading and batters that tie design edges into existing terrain. Multiple profile and cross-section windows stay live, so the effect of an edit is visible across a range of chainages or across connected strings (kerb returns, cul-de-sacs) simultaneously.

**4. Model the body of the works.**
Apply section templates or grading rules to generate the proposed surface — the corridor or graded site as real terrain. Junction elements re-grade themselves; ditches and batters appear or disappear per the conditional rules; the proposed surface updates.

**5. Design the networks.**
Lay out stormwater and sewer runs (by clicking, or from polylines/alignments); assign catchments from the surface; let minimum slope/cover and flow rules set initial sizes and levels; then adjust in the vertical editor with crossing services and clash detection visible; confirm depths and the hydraulic grade line.

**6. Evaluate earthworks and rules.**
Compare proposed against existing surfaces: cut/fill volumes with compaction factors, depth bands, slope displays; review compliance against the configured criteria (cover, clearances, driveway/vehicle clearance in some products). Iterate back to step 2–5 to optimize.

**7. Publish the documentation.**
Generate the sheets — plans, long sections, cross sections, drainage long sections with HGL, setout tables, pit/pipe schedules, volume reports — styled to the office's or jurisdiction's drafting standards, as layouts or separate drawings. Because they are generated from the design objects, they regenerate when the design changes.

**8. Exchange downstream.**
Export surfaces, alignments and models (CAD, LandXML, IFC) to BIM collaboration and downstream consumers; send network geometry to specialist drainage/hydraulic analysis and receive results back; produce data for staking and, in some products, for field devices and machine control.

**Core vs common vs optional**

- **Defining core** — existing-ground-anchored land project; proposed land-form objects (routes and/or graded surfaces); existing-vs-proposed evaluation; design-driven documentation.
- **Standard capabilities** — drainage/sewer networks; section templates; superelevation rules; conditional batters/ditches; intelligent junctions; surface analysis; volume machinery; setout; 3D review; exchange (LandXML/CAD/IFC, analysis links); regional standards localization.
- **Optional/variant** — in-product hydrology simulation; reconstruction-specific toolsets; rail/trackwork extensions; pressurized-utility design; AI-assisted road/subdivision generation; machine-control data prep.

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Plan (drawing) window

The primary working surface — the CAD-style plan view of everything.

- existing ground contours, survey data, alignments, grading outlines, networks, property boundaries
- primary actions: draw/convert alignments and grading outlines, edit geometry at intersection points, review labeling, compose plan sheets

### Long-section (profile) window

The vertical design editor for a route or run.

- existing ground line along the alignment; the design profile; curves; network pipes and HGL where relevant
- primary actions: add/move profile intersection points, edit curves, set pipe inverts, watch cover and cut/fill update

### Cross-section window

The section view at a chainage (usually browsable across a range).

- existing ground, template/assembly body, batters/ditches, pavement layers, pipes and services
- primary actions: inspect and adjust the section, review clearance/layer logic, verify tie-in behavior

### Grading / surface tools

The surfaces-and-terrain control surface.

- surface creation from points/LandXML/drawing data; display controls (contours, banding, slope arrows); grading objects with template and slope rules
- primary actions: create/edit surfaces and gradings, run comparisons, produce volume reports

### Network (pipe) editor

The drainage/sewer design surface (plan-linked).

- network tree or plan view of pits and pipes; catchment assignment; sizing and level controls
- primary actions: lay out runs, set inverts/sizes, review HGL and clashes, produce schedules and drainage long sections

### Sheet/output manager

The documentation surface.

- output styles, sheet layouts, scales, layers, content selection; long-section/cross-section/plan sheet generation; setout and volume report generation
- primary actions: configure and regenerate sheets, publish to layouts or drawing files

### 3D model viewer

The review surface.

- the designed works as a navigable 3D model (roads, junctions, grading, networks)
- primary actions: orbit/inspect, review junction grading, check the design reads correctly in space

## Important Rules / Behaviors

### Everything is measured against the existing ground

Cut/fill, cover, depth and daylight calculations all resolve against the surveyed terrain. The existing surface is not a backdrop; it is the base operand of the design loop. Products therefore make its accuracy, breaklines and boundaries a first-class concern.

### Rules are regional and editable

Design criteria — superelevation tables, minimum slopes and covers, output styles, named national design manuals — are held as configurable rule sets rather than hard-coded values, because practice varies by jurisdiction. Offices localize them once and reuse them; output styles are typically saved as reusable standards.

### The design regenerates the documentation

The practitioner edits the design, not the drawings. Sections, long sections, setout and volumes are views of the design objects and must follow edits; how completely a product automates this (and how junctions, kerb returns and cul-de-sacs re-grade when roads change) is a principal differentiator.

### Slopes, not just elevations

Grading is authored as slope relationships — batters from design edge to existing ground, crossfalls through curves, pipe gradients between minimum and maximum — rather than as fixed elevations. Conditional rules (add a ditch in cut, remove it in fill; change batter slope by depth) express constructible practice directly in the model.

### Networks live with the surfaces

Pipe design depends on surface levels for cover and on road/grading objects for pit placement and levels; mature products synchronize pits and pipes with the road or grading elements so that surface edits propagate into the network and its long sections.

### Exceptions the workflow must absorb

- **Design change after documentation** — the normal case; generated views and volumes re-derive, and a tool that let sheets silently contradict the model would fail as a civil design application.
- **Conflicts with existing services** — pipes must dodge utilities and other networks; clash detection in the section/vertical editors is the standard response.
- **Compliance failures surfaced late** — driveway/vehicle-clearance conflicts (in products that model driveways), house-connection depth limits, minimum-cover violations; products highlight and re-check these as the design moves.
- **Legacy data** — designs often start from old 2D survey drawings or prior CAD models; conversion of level text and drawing geometry into surfaces is a supported entry path.

## Variants

- **Roadway/infrastructure-focused platforms** — corridor-centric toolsets for highways, reconstruction, intersections and large multi-carriageway projects; often the largest products, extending to rail/trackwork and pressurized utilities.
- **Land-development/site-focused packages** — grading, pads, basins, subdivision roads and drainage as the center of gravity; often lighter, faster to learn, common in small consultancies and municipal teams.
- **CAD-platform engines vs standalone packages** — design engines that run inside a general CAD platform (and exchange objects with the platform's own design objects) versus self-contained design applications.
- **Survey-heritage suites** — survey/construction office software whose corridor and surface machinery serves both design and construction-data preparation; the seam with surveying workflows is deliberately blurred there.
- **In-product analysis vs companion analysis** — products that simulate drainage inside themselves versus those exchanging with specialist hydrology/hydraulics tools (a pattern that varies by market).
- **Regional editions** — the same category localized to different national criteria, output standards and analysis methods; vendors often lead in one regional market.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Architecture Design Application | discipline sibling — complementary | designs the *building* (spaces, enclosing elements, openings) with terrain as context; this Type designs the *land modification* (routes, graded terrain, drainage) against measured existing ground |
| Structural Engineering Design / MEP Design | discipline siblings — analysis-first | center on load/flow analysis and element sizing of structures and building services; this Type centers on land geometry, slopes, earthworks and geometric/cover rules |
| BIM Authoring | adjacent | centers the shared data-rich building model for cross-discipline delivery; civil/site products participate in BIM (IFC, model exchange) but author terrain/routes/networks |
| Surveying workflows (field-to-finish) | upstream / boundary-straddling | capture, adjust and draft *existing* conditions; this Type consumes that data as the design base and authors *proposed* works; survey office suites with corridor machinery straddle the seam |
| Government GIS / Utility GIS | adjacent — record vs design | records existing assets and terrain attributes; no proposed-works authoring, cut/fill loop or design documentation |
| Quantity Takeoff / Construction Estimating | downstream consumer | measures and prices from a design; volume reporting here is a byproduct of the design loop, not the center of gravity |
| Construction Scheduling / Project Management | downstream | consumes the approved design and documentation; does not author land-form geometry |
| Machine-control / data-prep workflows | downstream | translate the design into field-device and machine-guidance models; authoring the design is not their job |

The sharpest boundary is with **surveying/field-to-finish software**: the survey-heritage pole of this category processes field data *and* translates linear designs into constructible models in one environment. The working distinction: if the primary job is authoring proposed works against measured terrain, it is this Type; if it is processing and adjusting field data for delivery, it is survey-side.

## Representative Products

- **Civil Site Design** (Civil Survey Applications) — corridor-first civil design engine running on CAD platforms; road/subdivision/reconstruction, pipe design and site grading
- **Site3D** (Site3D Solutions) — standalone UK site/road design package; road networks, junctions, drainage, earthworks and setting out
- **Trimble Business Center** (Roading module) — survey-heritage office suite whose alignment/corridor machinery serves design data preparation and constructible models
- **Autodesk Civil 3D** — the market-dominant model-based civil infrastructure platform, listed for market completeness (its documentation could not be reviewed in this research pass; see Sources)

## Sources

Research date: **2026-09-07**

- Site3D — official product site (features: road networks, junctions/roundabouts, drainage, earthworks, ponds, 2D→3D conversion, setting out, BIM IFC): https://www.site3d.co.uk/
- Civil Site Design — official product site (product info: road design, pipe design, site grading, surface modelling, alignment design, plotting, HEC-RAS exchange): https://civilsitedesign.com.au/ , https://civilsitedesign.com.au/product-info/
- Civil Survey Solutions — vendor pages (Civil Site Design overview; Civil 3D positioning and capability names): https://civilsurveysolutions.com.au/products/civil-site-design/ , https://civilsurveysolutions.com.au/products/civil-3d/
- Trimble Business Center — official help portal (home, workflows, alignments-and-corridors workflow) and product page: https://help.fieldsystems.trimble.com/tbc/home.htm , https://help.fieldsystems.trimble.com/tbc/workflows.htm , https://help.fieldsystems.trimble.com/tbc/discover-alignments-and-corridors.htm , https://geospatial.trimble.com/en/products/software/trimble-business-center

> Sourcing limitation: the official product and help domains of Autodesk (Civil 3D) returned 403/JS-only pages and were abandoned after repeated attempts, consistent with earlier passes; Bentley (OpenRoads) help surfaces were sign-in gated, and Carlson/12d surfaces were JavaScript-gated or unreachable. The market-dominant platforms are therefore characterized here only through an authorized reseller's positioning page, and no precise operational details (numeric limits, defaults, exact state names, plan entitlements) are asserted for any product in this document. Cross-product claims rest on the three products with reachable official documentation; product-by-product observations and evidence calibration are recorded in the paired Research Notes.
