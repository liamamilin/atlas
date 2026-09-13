# Research Notes — Civil / Site Design

## Research Goal

Understand how civil/site design software actually works as an Application Type: what objects exist inside the design model, how the workflow flows from surveyed ground to documented construction deliverables, which rules constrain the design, and where this Type's boundaries lie against architecture design, structural/MEP engineering design, surveying, GIS, and construction-quantity products.

The leaf name contains a slash ("Civil / Site Design"), so a specific question is whether "civil" (corridor/infrastructure design) and "site" (land development/grading design) are one Type or two, and whether one definition can cover both without over-fitting to either pole.

## Initial Boundary (hypothesis before research)

- Core hypothesis: an authoring environment in which a practitioner designs land infrastructure — roads and corridors, graded sites, drainage networks — against measured existing terrain, producing engineering documentation (plans, long sections, cross sections, setout, volumes).
- Nearest neighbors: Architecture Design Application (building vs land), BIM Authoring (shared data model vs land design), Structural Engineering Design / MEP Design (analysis-first discipline siblings), Surveying workflows (capture vs design), Government GIS / Utility GIS (record vs design), Quantity Takeoff / Construction Estimating (downstream consumer), machine-control data prep (downstream).
- Known flags from earlier sibling passes: the Architecture Design Application and BIM Authoring documents both recorded Civil / Site Design as a "discipline sibling" — engineering objects and analysis (grading, drainage) as the primary structure.

## Research Questions

1. What are the core design objects? (surfaces, alignments, profiles, corridor templates, grading objects, pipe networks, parcels?)
2. How does the existing ground enter the model — survey points, LandXML, scanned level data, ground models?
3. What is the typical workflow from survey data → design → evaluation → documentation?
4. Which engineering rules are built into the tools (superelevation, daylight/batter slopes, pipe cover/slope, HGL, regional design standards)?
5. How are drainage/hydrology handled — inside the product or through companion analysis tools?
6. What outputs are produced (long sections, cross sections, sheet sets, setout tables, volume reports)?
7. Where exactly does this Type end: survey capture? hydrology analysis? construction quantities? machine-control data prep?

## Representative Products (selection rationale)

| Product | Pole | Why selected |
|---|---|---|
| Civil Site Design (Civil Survey Applications) | corridor-first civil package, add-on to AutoCAD / Civil 3D / BricsCAD; Australian council & land-development market | deep official product documentation; string-and-template design philosophy |
| Site3D | UK standalone site/road design specialist; small-firm pole | deep official product site; road-network + drainage + earthworks in one lightweight package |
| Trimble Business Center (Roading module) | survey-heritage field-to-finish office software | official help portal; shows the survey-data pole of the Type and its boundary with surveying |
| Autodesk Civil 3D | market-dominant model-based civil infrastructure platform | official Autodesk surfaces unreachable (403 / JS shell); characterized via authorized-reseller positioning only — no operational claims |

Rejected / unreachable: Bentley OpenRoads Designer (sign-in/JS gated — market context only), Carlson Civil (JS-gated site; KB root reachable but category pages not), 12d Model (sparse root; wiki 403). These are recorded as source-access limitations, not evidence.

## Sources

Fetched 2026-09-07:

- Site3D — official product site: https://www.site3d.co.uk/ (road networks, junctions, roundabouts, drainage, earthworks, ponds, 2D→3D conversion, setting out, BIM IFC)
- Civil Site Design — official product site: https://civilsitedesign.com.au/ and https://civilsitedesign.com.au/product-info/ (road design, pipe design, site grading, surface modelling, alignment design, HEC-RAS exchange, plotting/publishing)
- Civil Survey Solutions — vendor/reseller pages: https://civilsurveysolutions.com.au/products/civil-site-design/ and https://civilsurveysolutions.com.au/products/civil-3d/ (Civil 3D positioning and capability names)
- Trimble Business Center — official help portal: https://help.fieldsystems.trimble.com/tbc/home.htm, .../workflows.htm, .../discover-alignments-and-corridors.htm ; product page https://geospatial.trimble.com/en/products/software/trimble-business-center

Attempted and abandoned (2 failures each, per source-access rule):

- Autodesk — https://www.autodesk.com/products/civil-3d/overview (403, consistent with the 2026-09-06 architecture pass); https://help.autodesk.com/view/CIV3D/2025/ENU/ (JS shell, content not rendered)
- Bentley — https://www.bentley.com/software/openroads-designer/ (sign-in); https://communities.bentley.com/... (JS shell)
- Carlson — https://www.carlsonsw.com/product/civil-suite/ and knowledge-base category pages (JS-gated)
- 12d Model — https://www.12d.com/ (sparse root), https://www.12dwiki.com.au/ (403)

## Product Observations

### Civil Site Design (Civil Survey Applications) — Evidence layer A (official product docs)

Platform posture: add-on/design engine operating on AutoCAD, Map 3D, Civil 3D (2012→current) and BricsCAD; in Civil 3D it uses Civil 3D surfaces/alignments and exports surfaces, alignments, profiles, corridors, COGO points back to the drawing. Positioning: "all-in-one road, piping and site design solution" for road/corridor projects, land development and site grading, stormwater, sewer and pipe design.

Key observations:

- **Road design = string + template.** Template-and-string-based design as the core philosophy; automated design elements for intersections, kerb returns, cul-de-sacs (circular/asymmetric/tear-drop/Y/T shapes), roundabouts, knuckles (localized widening) — described as intelligent/dynamic objects that re-position and update when roads change. Road design tools explicitly usable for "any generic corridor design: open channels, retaining walls, footpaths".
- **Vertical grading editor.** Vertical (long-section) design windows; multiple profile strings open simultaneously (roads, kerb returns, cul-de-sacs); multiple cross-section windows showing the impact of profile edits across a range of chainages; cut/fill bulking factors; summary volume reports; surface model creation.
- **Superelevation by rule.** Set a speed for the road length; superelevation rules (Australian or user-defined per region) calculate crossfall changes through curves from speed, curve radius and maximum superelevation; superelevation "table" is an editable text file; override per curve; shoulder rotation rules.
- **Daylighting / batters / ditches with conditions.** Design-controlled batter (daylighting) outputs; ditches that check fill conditions on the ditch bottom and remove the ditch when not required; conditional batter tools that add benching, change batter slopes, include/remove ditches based on depth-range conditions.
- **Road reconstruction.** Overlay/resheet depths, match-surface controls, design "envelopes" (projections from another string/code at grade), multi-layer subgrade volumes with automatic pavement layer adjustment against existing surfaces.
- **Pipe networks (stormwater, sewer, general).** Network layout by clicking or from polylines/alignments; initial layout based on minimum slopes and covers; vertical design windows showing crossing pipes and services with clash detection; pit/pipe schedules; long-section plotting with HGL. Stormwater built on the Australian Rainfall and Runoff manual / Rational Method — catchments from surface + polyline, auto pipe sizing/levels from flows, cover/slope/velocity rules. Sewer: house/property connections with depth controls; network auto-adjusts for compliance. Pipes synchronize with roads modules — pit levels/offsets connected to road elements with dynamic updates.
- **Site grading.** Polyline + cross-section template (assembly) → graded surface with corner cleanup; building pads and detention basins as flagship uses; batters; immediate volume review; grading linework updates as edits happen.
- **Surface modelling.** Surfaces from external point data, LandXML, and 3D drawing data; contour/layer/label display controls; elevation banding, slope ranges/directions/arrows; volumes between any two surfaces with compaction factors and height adjustments; works directly with Civil 3D surface objects.
- **Alignment design.** Draw a polyline → convert to alignment object; automatic customizable labeling (chainage, major/minor intervals); IP editing with spiral lengths, curve radius; alignment and curve tables regenerate after edits; LandXML import/export.
- **Documentation/plots.** Long-section and cross-section sheet generation, setout points, slope patterns, plan plotting of models — output styles customized to local drafting standards (defaults for Australian and many European customers), reusable plot styles, layouts or separate drawings.
- **Companion analysis exchange.** HEC-RAS menu (transfer section data, Manning's coefficients, overbank areas; waterline results back for presentation); two-way link to DRAINS (AU stormwater analysis; pits, pipes, catchments, overland flows; results back for plan production).
- **AI-era additions.** "Project Assist" for automated road and subdivision design; ScriptX for user-created template variations; high-resolution 3D model viewer.
- **Market context.** Used in 120+ Australian councils; road reconstruction, drainage upgrades, intersections/roundabouts.

### Site3D (Site3D Solutions, UK) — Evidence layer A (official product site)

Positioning: "intuitive civil engineering design software designed by engineers for engineers"; standalone Windows package.

Key observations:

- **Road networks.** Complex road networks with varying widths; major highways, link roads, bypasses; "automatic junctioning" to link roads.
- **3D junctions & roundabouts.** Junctions auto-calculate vertical kerb-return design tying roads together horizontally and vertically, updating on design change to maintain specified engineering criteria; 3D roundabouts per DMRB guidelines (UK design standard) with automatic vehicle deflection calculation; drag junctions and observe effects.
- **Formation surface & volumes.** One-click formation surface generation; instant cut and fill volume calculation; automatic isopachyte (depth-band) colouring.
- **Drainage.** Networks by placing manholes along runs; auto-sizing and levelling per surface cover levels, drainable areas and rainfall profile; drainage auto-displayed and annotated on long-sections, instantly updated; drainage simulation in-product or export/import with external drainage packages.
- **Earthworks.** Interface grades from design edges to a chosen ground model; stepped grades for utility strips and linear features (swales).
- **Ponds.** Dynamic cut/fill and water-storage volumes while defining pond shape/profile.
- **2D→3D conversion.** Reads level text on 2D drawings, finds insertion points, assigns levels to 2D feature lines to form an accurate 3D surface — i.e., consuming legacy surveyed 2D drawings as existing-ground input.
- **Setting out.** Annotated coordinate and setting-out tables auto-update on any design change.
- **BIM.** IFC export with layer naming per BS1192:2007 and design attribute information, into Revit/Navisworks-class collaboration tools.

### Trimble Business Center — Roading / corridors — Evidence layer A (official help portal)

Positioning: "complete office software solution for survey and construction professionals"; field-to-finish survey CAD. The Roading module: "parametric tools to translate linear infrastructure designs into constructible models."

Key observations (from the Alignments and corridors workflow page):

- Horizontal and vertical alignments defined from scratch or from existing CAD linework; support for station equations and superelevations.
- Corridor template instructions entered with interactive graphical feedback; conditional instructions and slope/node tables for complex roadway designs.
- Corridor features (interchanges, ramps, intersections) via parameter prompts.
- Corridor earthwork reports, material properties, subgrade surfaces.
- Related workflows: takeoff and mass haul (earthwork/material quantities), surfaces and volumes (surface models for field devices and machine control systems), utility modeling (gravity/pressure/cable networks — pipes, fittings, headwalls, junction boxes, manholes), CAD and drafting (final survey linework, construction models, roadway design plots), data prep (delivering models to field devices).

Boundary-relevant: TBC's center of gravity is survey data processing (GNSS baselines, point clouds, adjustment) with corridor machinery attached for data prep and constructible models — design and construction-data preparation in one environment.

### Autodesk Civil 3D — Evidence layer B (authorized-reseller positioning; no operational docs)

From the reseller's Civil 3D page (capability names and positioning; treated as vendor positioning, not operational evidence):

- "Design and documentation software for civil infrastructure"; 3D model-based design environment; "design-driven" plans production automated from the 3D design model; BIM workflows.
- Road design pole: survey (download/create/analyse/adjust survey data), corridor modelling (dynamic 3D road corridors), intersection design, drainage design incl. storm sewer, road rehabilitation (automated assembly generation).
- Site design pole: terrain modelling (ground topography for feasibility/flow studies), corridor modelling for residential roads/kerbs/footpaths/swales/carparks, storm & sanitary networks (resize pipes, reset inverts, compute energy and hydraulic gradient lines), stormwater analysis integration, pressurized utilities (3D pressure pipe networks), design automation via visual programming, materials & quantities (volume reports along an alignment comparing design vs existing ground surfaces).
- Rail design pole: alignments/profiles with cant, turnout libraries, corridor models with switches/platforms.

## Cross-product Comparison

| Structure | Civil Site Design | Site3D | TBC Roading | Civil 3D (positioning) | Strength |
|---|---|---|---|---|---|
| Survey/existing-ground input | point data, LandXML, drawing 3D data | 2D level-text conversion, ground models | survey sensor data, CAD linework | survey data download/adjust | Strong (A×3 + B) |
| Alignment + vertical profile as linear route | yes (polyline→alignment, IP editing, spirals, tables) | road networks with automatic junctioning (alignment concept implicit in roads) | H/V alignments, station equations | alignments and profiles | Strong |
| Cross-section template driving the road/body | templates (assemblies) | implied in roads/junctions (not named on fetched page) | corridor template instructions | corridor modelling / assemblies | Moderate–Strong (A×2 + B) |
| Proposed graded surface (pads/basins/batters) | site grading tools, batters, corner cleanup | earthworks interface grades, ponds | surfaces, subgrade surfaces | terrain modelling | Strong |
| Cut/fill earthwork evaluation | volume reports, bulking/compaction factors | instant cut/fill volumes, isopachytes | earthwork reports, mass haul | materials & quantities design-vs-existing | Strong |
| Drainage/pipe networks | storm/sewer pipes, pits, HGL, clash detection | manholes, auto-size/level, long-sections | utility modeling (gravity/pressure) | storm & sanitary networks, HGL | Strong |
| Hydrology analysis in-product vs companion | companion (DRAINS, HEC-RAS exchange) | either (in-product simulation or export) | takeoff/mass haul (not hydrology) | analysis integration positioned | Companion pattern dominant |
| Superelevation / speed-radius rules | rule tables by speed/radius, editable per region | DMRB roundabout criteria (named standard) | superelevation support + workflow | not evidenced on fetched surface | Strong (A×2), regionalized |
| Daylighting/batter to existing ground | conditional batters, ditches by cut/fill conditions | interface grades to ground model | slope tables, conditional instructions | not evidenced on fetched surface | Strong (A×2) |
| Intelligent intersection/junction objects | kerb returns, cul-de-sacs, roundabouts, knuckles | auto junctions, 3D roundabouts | parameter-prompted interchanges/ramps/intersections | intersection design | Strong |
| Design-driven documentation | long/cross-section sheets, setout, local styles | long-sections auto-annotated, setting-out tables | roadway design plots | design-driven plans production | Strong |
| Regional standards localization | AU/EU output styles, ARR/Rational Method, editable superelevation tables | DMRB, BS1192 layer naming | not evidenced on fetched surface | not evidenced on fetched surface | Strong (A×2) |
| BIM/IFC delivery | LandXML import/export; Civil 3D object exchange | IFC export (BS1192) | exports for field devices/third-party | BIM workflows positioning | Strong |
| Parcel/lot layout machinery | subdivision roads; property-boundary linkage in driveway tools; lot grading | not evidenced | not evidenced | not evidenced | Weak — qualified only |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant (deliberately small)

The design object is **the land itself**: a persistent, real-world-scaled project whose base is **measured existing ground**, on which the practitioner authors **proposed land-form objects** — linear routes (horizontal alignment + vertical profile, with cross-section shape) and/or **graded proposed surfaces** (pads, basins, embankments, site layouts) — that **reshape the terrain**, evaluated against the existing ground (**cut/fill relationship**), and delivered as **design-data-driven annotated documentation** (plans, long sections, cross sections, setout).

Four properties; remove any one and the product stops being recognizable as civil/site design:

1. **Real-world-scaled land project anchored to measured existing ground** — the survey-derived terrain (points, surfaces, ground models) is the base datum the design works against. Without it: generic CAD/3D drafting.
2. **Proposed land-form design objects** — either linear routes (alignment + profile + section shape) or graded surfaces/earthwork forms; real geometry in real coordinates that modifies the ground. Without it: viewing/analysis of existing conditions only (GIS/survey pole).
3. **Existing-vs-proposed evaluation** — the design is continuously evaluated as modification of measured terrain: cut/fill, volumes, cover/depth relationships. Without it: drawing, not land design.
4. **Design-data-driven documentation** — the deliverable (annotated plans, long sections, cross sections, setout, volume reports) is generated from the design objects and updates with them. Without it: analysis-only tool.

Note the disjunction in (2): it is what allows one Type to cover the leaf's two named poles — "Civil" (corridor/roadway design) and "Site" (grading/site layout). Historical check: the pre-dynamic-model generation of this category (survey-based road design and earthwork packages) already exhibited all four properties — alignments/profiles, section templates, earthwork quantities against surveyed ground, and plan/profile/section deliverables — so the invariant does not over-fit to modern dynamic-model implementations.

### L1 — Common Mature Structure (very common, not definitional)

- **Drainage / pipe networks** — storm and sanitary networks of pits/manholes and pipes tied to surfaces and roads: auto layout from minimum slope/cover, inverts, HGL display, clash checks against services, long-section annotation. Present in every sampled product (though a road- or grading-only scope is conceivable).
- **Cross-section templates/assemblies** as the reusable shape vocabulary of corridors (pavement, kerbs, shoulders, ditches).
- **Intelligent intersection/junction machinery** — kerb returns, cul-de-sacs, roundabouts, interchanges/ramps as rule-driven objects that update with the roads.
- **Superelevation rules** applied from speed/radius criteria through curves.
- **Daylighting/batter machinery** — slope-based tie-ins to existing ground, conditional ditches/benching by cut/fill depth conditions.
- **Surface analysis displays** — contours, elevation banding, slope arrows/ranges, isopachyte (depth-band) colouring.
- **Volume reporting machinery** — between any two surfaces, with compaction/bulking factors; mass-haul in some products.
- **Setout machinery** — coordinate/setting-out tables and staking outputs regenerated from the design.
- **CAD/BIM exchange** — LandXML, DWG/DXF, IFC, COGO points; import of survey data; export to BIM collaboration.
- **3D model visualization** — model viewers/3D windows for reviewing roads, junctions, grading.
- **Regional standards localization** — output styles, superelevation tables, named national criteria (e.g., DMRB, ARR/Rational Method) as editable configuration.
- **Companion-analysis exchange** — links to hydrology/hydraulics analysis tools (catchments, flows out; HGL/waterlines back).

### L2 — Variant / Optional Structure

- **Platform posture** — standalone design package vs add-on/engine on a CAD platform (AutoCAD/BricsCAD-class) vs module of a survey/construction office suite.
- **Pole emphasis** — roadway/infrastructure (highways, reconstruction, intersections) vs land development/site (subdivisions, pads, basins, parking) vs both.
- **Analysis depth in-product** — full hydrology simulation inside the product vs exchange-only with specialist drainage analysis tools.
- **Reconstruction specialization** — overlay/resheet depth tools, subgrade layer volumes, match-surface controls.
- **Rail / trackwork design** as an infrastructure extension (cant, turnouts, platforms) in the largest platforms.
- **Pressurized-utility (pressure pipe) design** alongside gravity networks.
- **AI-era automation** — automated road/subdivision generation assistants; AI feature extraction in the survey pole.
- **Customer scale** — small-firm standalone tools vs council/municipal deployments vs agency-scale corridor platforms.

### L3 — Vendor-specific (kept out of the final document)

- ScriptX user-scriptable template variations; Project Assist AI automation; Model Viewer productization (Civil Site Design).
- Named-product link integrations (DRAINS two-way link; HEC-RAS menu; InfoDrainage integration) and their data payloads.
- Isopachyte banding as a named feature; 2D→3D level-text converter; kerb-return multi-radius wizards; knuckle tool; tear-drop cul-de-sac geometry.
- Council-count claims (120+), version-numbered feature lists, pricing/licensing models (Flex tokens etc.).
- DMRB/BS1192/ARR named-standard citations are regional markers, not universal rules.

## Boundary Findings

- **vs Architecture Design Application** — the architect designs a *building* (spaces, enclosing elements, openings) with terrain as *context*; civil/site design designs *the land modification itself* (routes, graded terrain, drainage) with buildings as adjacent scope. Test: remove the building → the remaining terrain/route/drainage design is this Type; remove land-forming (keep only enclosing elements) → it is architecture. The architecture pass had already flagged this Type as the discipline sibling where "grading" objects become primary — confirmed.
- **vs Structural Engineering Design / MEP Design** — those Types center on load/flow *analysis* and element sizing of structures/building services; civil/site design centers on *geometry, slopes and earthworks* of land form, with rules expressed as geometric/cover criteria rather than structural analysis. Drainage hydraulics (flows, HGL) sit at the seam: sizing logic lives in the civil product, but full hydrological analysis is usually a companion tool.
- **vs BIM Authoring** — BIM authoring centers the shared data-rich *building* model for cross-discipline delivery; civil/site design centers the *land* design. Civil products participate in BIM (IFC export, model-based collaboration) but their model semantics are terrain/routes/networks.
- **vs Surveying (field-to-finish) workflows** — survey products capture, adjust and draft existing conditions; civil/site design *consumes* that data as the existing-ground base and authors proposed works. The seam products (survey office suites with corridor machinery) straddle: they process field data AND translate linear designs into constructible models. Boundary posture: when the primary job is authoring the design of proposed works, it is this Type; when it is processing/adjusting/delivering field data, it is survey-side.
- **vs Government GIS / Utility GIS** — GIS records *existing* assets and their attributes; civil/site design authors *proposed* works against terrain. Surface/terrain analysis overlaps, but the design-document deliverable and cut/fill loop are absent from GIS.
- **vs Quantity Takeoff / Construction Estimating** — takeoff measures and prices from a design; civil design *produces* the design that quantities are measured from. Volume reporting is a byproduct of the civil design loop, not its center. (Survey office suites often bundle takeoff — boundary posture again.)
- **vs Machine-control data prep** — downstream translation of the design into field-device/machine guidance models; the civil design product may export into it (surfacing in some suites) but authoring the design is not its job.
- **Removal tests** ("去掉什么就变成另一个 Type"): remove measured existing ground & cut/fill → generic CAD drafting or 3D modeling; remove the land-form authoring (consume only) → GIS / viewing / data prep; remove the documentation leg → analysis-only drainage/terrain tools; center load/flow analysis of structures instead → Structural/MEP design.

## Uncertainties

1. **Market-dominant pole under-evidenced.** Autodesk Civil 3D and Bentley OpenRoads official documentation was unreachable this pass (403 / sign-in / JS). Civil 3D is characterized only via reseller positioning (capability names, no operational detail); OpenRoads contributes no claims. The cross-product table's strongest rows rest on three products, two with deep docs.
2. **Parcel/lot layout machinery.** Subdivision roads are well-evidenced, but dedicated parcel/lot geometry tools (lot grading, boundary parcels) were only partially evidenced (property-boundary linkage in one product). Possibly a common capability that the fetched surfaces simply didn't document; qualified accordingly.
3. **Drainage networks: L0 vs L1.** Universal in the sample, but a road- or grading-scoped product without pipe networks is conceivable; placed in common structure with a note rather than the invariant.
4. **Hydrology in-product depth.** Products differ (in-product simulation vs companion exchange); the "companion pattern" is the safest generalization, asserted at moderate strength.
5. **Template/assembly vocabulary on one product.** Site3D's road/junction shape vocabulary was not directly evidenced on the fetched surface (page-level only); the cross-section-template row is marked Moderate–Strong.

## Final Synthesis

Civil / Site Design is the discipline-sibling authoring Type in the land-development/infrastructure family: its practitioners (civil engineers, civil designers, site/road designers, surveyor-designers in the survey-heritage pole) design *proposed modifications of measured terrain* — linear routes with vertical profiles and section shapes (roads, channels, utilities' corridors), graded surfaces (pads, basins, embankments, site layouts), and (commonly) gravity drainage/sewer networks — continuously evaluated as cut/fill against the existing ground and delivered as annotated, standards-localized engineering documentation (plans, long sections, cross sections, setout, volume reports) that drives construction and staking.

The Type's unity across its two named poles rests on the shared design loop: **survey/existing ground in → land-form design objects authored against it → earthwork/rule evaluation → design-driven documentation out**. Product philosophies differ mainly in where the intelligence sits (rule-driven template objects vs free strings edited by hand; in-product hydrology vs companion analysis; standalone vs CAD-platform engine), not in the underlying structure.
