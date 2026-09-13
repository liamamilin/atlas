# Research Notes — Agricultural GIS

## Research Goal

Understand what an **Agricultural GIS** is as an Application Type: the core objects it manages, the workflows users perform, the interfaces it presents, the rules that shape its behavior, and — most importantly — where it begins and ends relative to neighboring Types (Precision Agriculture Platform, Crop Remote Sensing Platform, Farm Management Platform, Government/Utility GIS).

## Initial Boundary

Working hypothesis before research:

- Core use: manage georeferenced spatial data about agricultural land — field boundaries, soil, yield, imagery — with a map as the working surface, and derive agronomic outputs (zones, prescriptions, reports) from spatial analysis.
- Primary users: agronomists, farm managers, precision-ag specialists, GIS staff at agribusinesses/co-ops/consultancies.
- Nearest neighbors: Precision Agriculture Platform (VRA execution loop), Crop Remote Sensing Platform (imagery as product), Farm Management Platform (operational/financial records), Government GIS / Utility GIS (same generic GIS engine, different domain).
- Unknowns: is prescription/VRA generation definitional or common? How deep does imagery analysis go before the product becomes a remote-sensing platform? Does the classic desktop "farm mapping" lineage still fit a cloud-era definition?

## Research Questions

1. What are the core "things" in the system? (fields/boundaries, layers, attributes, maps, zones, prescriptions)
2. How are field boundaries created, imported, edited, and organized (farm → field hierarchy)?
3. What layer types exist and how are they registered to the land base?
4. What spatial operations do users perform (measure, overlay/compare, zone derivation, classification)?
5. How are prescriptions / variable-rate maps produced and handed to equipment?
6. How does machinery data (yield, as-applied) enter and flow through the system?
7. How does satellite/drone imagery enter, and at what depth does imagery analysis stop being "a layer"?
8. What interface forms exist (desktop GIS, cloud map workbench, mobile field app)?
9. How do records (activities, inputs, people) relate to the spatial base?
10. Where are the boundaries vs Precision Agriculture Platform, Crop Remote Sensing Platform, Farm Management Platform, Government/Utility GIS?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence level reached |
|---|---|---|
| Esri ArcGIS (Agriculture industry focus) | professional/enterprise GIS platform applied to agriculture | Tier 2 (industry + segment pages, GIS definition page) |
| GeoPard | cloud-native precision-ag analytics platform (growers, consultants, co-ops, dealers) | Tier 1 (official product documentation, extensive) |
| Climate FieldView | grower-tier cloud field-data platform with own hardware | Tier 2 (solution/product pages) |
| OneSoil | satellite-first, free-entry platform for farmers + agri-service partners | Tier 2 (platform page + FAQ) |

Rejected / unreachable samples:

- **Ag Leader SMS** (classic desktop ag GIS/records) — vendor site returned 404 on two paths; abandoned per retry rule.
- **Trimble Ag Software (Farm Works lineage)** — transport errors on two fetches; abandoned.
- **Agrian** — 403; abandoned.
- **John Deere Operations Center** — marketing page JS-rendered, no content; its structure is nonetheless indirectly documented by GeoPard's official integration docs (boundaries, map layers, work plans, operation data, staff/partner sharing).

## Sources

- Esri — GIS for Agriculture overview: https://www.esri.com/en-us/industries/agriculture/overview (fetched 2026-09-06)
- Esri — Farm Planning and Decision-Making segment: https://www.esri.com/en-us/industries/agriculture/segments/farm-planning-decision-making (fetched 2026-09-06)
- Esri — What is GIS?: https://www.esri.com/en-us/what-is-gis/overview (fetched 2026-09-06)
- GeoPard — product site: https://geopard.tech/ (fetched 2026-09-06)
- GeoPard — official docs (Tier 1): sitemap https://docs.geopard.tech/geopard-tutorials/sitemap.md; Zones Maps and Analytics; Draw a new field; Export VRA Map in ISOXML Format; Yield Data & Harvest Analytics (all fetched 2026-09-06)
- Climate FieldView — home: https://climate.com/; Build Prescriptions: https://climate.com/en-us/solutions/build-prescriptions.html; Analyze Data: https://climate.com/en-us/solutions/analyze-data.html (fetched 2026-09-06)
- OneSoil — home: https://onesoil.ai/en/; Platform: https://onesoil.ai/en/platform (fetched 2026-09-06)

**Source-access limitations:** the classic desktop/dealer-tier ag GIS lineage (Ag Leader SMS, Trimble Ag/Farm Works, Agrian) could not be fetched on 2026-09-06 (404/transport/403). Claims about that tier are kept weak and are anchored only in Esri's industry positioning and the cloud products' file-format compatibility (shapefile/ISOXML import-export implies the surrounding GIS ecosystem). John Deere Operations Center was not directly fetchable; its structure is asserted only where GeoPard's official integration documentation describes it. No precise numeric limits (zone counts, acreage caps, file sizes) are asserted anywhere in this research except where a fetched page states them.

## Product A — Esri ArcGIS (Agriculture)

### Key observations (evidence layer A unless noted)

- Positioning (Tier 2): "Collect, maintain, analyze, and share your agriculture data with ArcGIS… Integrate Earth observations, imagery, field data, and real-time data streams." Agriculture is one industry vertical over a general GIS platform.
- Precision-farming framing (Tier 2): "Create maps and dashboards that integrate important variables such as soils, irrigation, yield, production costs, profit, and compliance data"; "Add maps, imagery, field data collections, and real-time sensor feeds into interactive apps"; deploy on premises and/or cloud.
- Farm Planning segment (Tier 2) names the capability stack: Mapping; Imagery and remote sensing; Spatial analysis; Real-time visualization; Decision-making.
- Products named for the agriculture segment (Tier 2): ArcGIS Pro (desktop GIS), ArcGIS Living Atlas (online geographic information collection), ArcGIS Field Maps (mobile data collection/editing), ArcGIS Dashboards, plus packaged solutions (e.g., Invasive Pest Inspections).
- Generic GIS definition (Tier 2, vendor's own formal definition): "GIS is a technology that is used to create, manage, analyze, and map all types of data… connects data to a map, integrating location data (where things are) with all types of descriptive information (what things are like there)." Four functions: data management; mapping and visualization; spatial analysis; communication.
- Observation (layer B): Esri demonstrates that the *generic GIS engine* is domain-agnostic; the agricultural specialization comes from the data domain (fields, soils, yield, imagery) and the agronomic workflows built on top, not from a different engine.

## Product B — GeoPard

### Key observations (Tier 1 official docs unless noted)

- **Land base hierarchy**: Farms → Fields. "Create a new farm… to organize fields, analytics, and team workflows." Fields are created by (a) drawing a boundary manually on the map (point-by-point polygon; the app "automatically calculate[s] the size of the selected area"), (b) uploading a boundary file (.shp), or (c) importing from John Deere Operations Center (boundaries, fields, yield, as-planted, as-applied, tillage data). Boundaries can be edited ("Adjust field boundaries to fix geometry and keep analytics aligned with the real field"), renamed, and labeled (client, crop, season, workflow tags).
- **Automatic layer population**: after drawing a boundary, "the first historical satellite images will be available in a couple of minutes, and the complete dataset in about 1 hour or less" — the platform attaches a satellite-imagery layer set to the new land unit automatically.
- **Layer model**: datasets attach to fields — satellite imagery (Landsat/Sentinel/Planet; 35+ years history; 20 indices), yield datasets, soil datasets (shapefile with coordinates; lab results CSV/Excel "smart import"; soil scanner data: electrical conductivity, moisture, Veris, SoilOptix, TopSoilMapper), as-applied/as-planted data, topography (elevation, slope, aspect from machinery/remote-sensing/LiDAR), zones maps, equation-based maps.
- **Zones Maps and Analytics** (core spatial-analysis surface): "Create Zones Map" flow with input-type choice — satellite imagery, soil/yield/as-applied data, topography, template, or clone of an existing zones map. Multi-layer analytics: "integrate multiple data layers to create management zones. You control weights, indices, the number of zones, clustering type, and minimum polygon area." Classification methods: AUTO, Natural Breaks, Equal Interval, Equal Count, Spatially Localized. Zones are editable (merge/split polygons; draw zones manually; clone polygons from an existing layer). Multi-year zones for stable productivity zones. Variability metrics: heterogeneity factor, relative variation factor.
- **Prescription/VRA**: "Assign Variable Rates in Zones (Ag Input Rates Distribution Tool)" — "Assign seed, fertilizer, lime, or input rates to zones and build machine-ready prescription maps." Equation-based analytics: agronomic formulas over imagery/yield/soil/machinery data; predefined equation catalog + custom equations/functions (Python).
- **Yield pipeline** (Tier 1, "Yield Data & Harvest Analytics"): Import (shp, ISOXML, proprietary machinery formats jdl/cn1/adm/dat, or John Deere) → Process (review attributes, units, field fit, machine paths) → Clean and calibrate (remove outliers/noise, fix striping, crop to boundary, align multiple combines/days, pathwise vs average/total calibration, USDA yield cleaning protocol) → Restore gaps (synthetic yield maps from historical behavior + remote sensing; partial restore) → Build recommendations (zones, equations, nutrient-uptake VRA: NU/NUE/NS; profit maps combining yield, prices, costs) → Share outputs (send layers/Rx to John Deere Ops Center as files, work plans, map layers, or operation data).
- **Equipment handoff**: export zones maps as shapefile; satellite imagery as GeoTIFF/GeoJSON; scouting notes as shapefile; VRA maps as ISOXML (ISO 11783, three variants in a zip "Check your monitor spec to choose the right one"); direct push to John Deere Ops Center (files, work plans, map layers, application-operation data); batch export of boundaries/zones/pins.
- **Organization/sharing**: organizations and roles; farms sharing between accounts and organizations; client/colleague account management (consultant/dealer pattern); John Deere staff-member and partner-organization sharing.
- **Mobile**: mobile app for scouting — view satellite images, zones, soil, yield, topography, as-applied datasets; record notes/pins; work offline.
- **Trials**: on-farm trials design (strip trials, RCBD plots, split-plot, checkerboard, zone-based), machine-ready export, spatial analysis of results.
- **Soil sampling**: automated planning — grid or zones, core/composite, algorithm-placed points and routes, lab labels, export (KML/shapefile).
- **API**: GraphQL/REST; objects include Farm, Field, SatelliteImages, RasterMaps, ZonesMaps, TopographyMap, YieldDatasets, SoilDatasets; mutations to generate zones/raster maps and export archives.
- Positioning (Tier 2): "All-in-One Precision Agriculture Software… powerhouse analytics platform"; roles served: growers, ag consultants & service companies, cooperatives & agriholdings, input producers/dealers, equipment producers/dealers, agtech companies, science/education.

## Product C — Climate FieldView

### Key observations (Tier 2 product/solution pages)

- Positioning: "The all-in-one digital farming solution"; four solution pillars: Gather Information; Scout Fields; Build Prescriptions; Analyze Data.
- **Data collection**: FieldView Drive 2.0 hardware ("easy to install, works with most equipment, connects to your iPad via Bluetooth to collect data"); "recording every pass throughout the season"; "upload data seamlessly from flash drives or other systems"; display adapter kits for CNH and John Deere GreenStar displays.
- **Prescriptions** ("Build Prescriptions"): "Create tailored prescriptions to optimize seeding rates, fertility and crop protection." Features: Adjustable Scripts; Automated Rates ("seed scripts can find the ideal rate for your field using data from over a million test plots" — vendor-claimed); Fertility Prescription Tools (nitrogen, phosphorus, potassium, lime); Crop Protection Plans (herbicide/fungicide/insecticide); Enhanced Scripts; Easy Exporting ("Convert your script into one of the many different file types to upload or send wirelessly").
- **Analysis** ("Analyze Data"): "Compare hybrids, inputs or practices on the same map"; "Harvest records, planting and application data in color-coded charts and maps"; "Side-by-Side Maps — compare any field, product or practice with a few taps"; Custom Reports (PDF or CSV for one field or the entire operation).
- **Sharing**: "Share your operation, a farm, or single fields with your agronomist."
- **Scouting**: high-definition imagery; real-time alerts, pins, in-depth imagery (from solution nav descriptions).
- **Partners**: "connectivity with 60+ partners"; "compatible with most equipment types."
- Observation (layer B): FieldView is a grower-tier cloud platform whose spatial machinery (fields, imagery layers, yield maps, side-by-side comparison, scripts) is the same structure GeoPard exposes, packaged for farmer self-service with hardware for data capture.

## Product D — OneSoil

### Key observations (Tier 2 platform page + FAQ)

- Positioning: "Satellite-powered intelligence for modern agriculture — from field monitoring and variable-rate application maps to crop identification"; "precision agriculture platform designed for farmers and agri-service companies."
- **Zero-data onboarding**: "No data is needed from your side to start getting value… Select fields from predefined boundaries and start working" — i.e., the platform ships a pre-existing library of detected field boundaries; users can also "upload or select your fields on the map in few clicks" or draw fields.
- **Monitoring**: satellite field monitoring (NDVI, NDRE, RECI, moisture, weather layers per FAQ); anomaly detection; hyperlocal weather per field; season-over-season comparison; machinery data overlaid on satellite imagery.
- **Analysis/action**: productivity zones (vendor-claimed ">90% correlation to yield map"); VRA/task maps ("machine-ready maps for seeding, fertilizing, and spraying"); savings estimate before application; zone-based soil sampling; field trials (control/treatment strips); scouting prioritization; spraying windows; field diary.
- **Equipment**: "Send maps to John Deere or export in the right format"; FAQ: "integrates directly with John Deere Operations Center and supports export formats compatible with most modern variable-rate equipment, making it easy to transfer prescription maps and import yield data."
- **Surfaces**: OneSoil Pro (web) for planning/analysis; OneSoil Mobile for scouting/observations/offline; API for embedding. Both products "share the same fields, users, and data."
- **Multiuser**; field boundaries export; batch creation of task maps; Planet Lab high-resolution imagery (paid).
- **Global Analytics** (separate product): field-boundary + crop-identification data across countries (vendor-claimed 650M ha analyzed) for food companies/traders/finance/governments — an adjacent data business built on the same boundary-detection machinery.
- Observation (layer B): OneSoil demonstrates the "satellite-first" pole: the land base can be *pre-populated by the vendor* (auto-detected boundaries) rather than user-drawn, and imagery is the default first layer.

## Cross-product Comparison

| Dimension | Esri ArcGIS (Ag) | GeoPard | Climate FieldView | OneSoil |
|---|---|---|---|---|
| Land base | generic GIS feature layers; agriculture as data domain | Farm → Field; draw/upload/import boundaries | fields (via equipment/partners/data upload) | fields; vendor-predefined detected boundaries or draw/upload |
| Layer types | feature layers, imagery, dashboards, sensor feeds | satellite, yield, soil, as-applied/as-planted, topography, zones, equations | imagery, yield, planting/application data, scripts | satellite indices, weather, machinery data, zones |
| Map canvas | yes (maps/dashboards/apps) | yes (field page, zones creator, compare) | yes (field maps, side-by-side) | yes (web + mobile map) |
| Spatial operations | full GIS spatial analysis | zone derivation (multi-layer clustering, classification), equations, topography analytics, merge/split editing | yield analysis maps, side-by-side comparison | productivity zones, anomaly detection, trials |
| Prescription/VRA output | via workflows/apps (positioning-level) | rates distribution tool → ISOXML/SHP/John Deere | scripts (seed/fertility/crop protection) → file export/wireless | VRA/task maps → John Deere WorkPlans/export |
| Machinery data in | sensor feeds (positioning-level) | yield/as-applied/as-planted import incl. proprietary formats; cleaning/calibration | Drive hardware + flash drives + partner systems | machinery data overlay; yield import (FAQ) |
| Mobile field surface | Field Maps (collection/editing) | mobile scouting app, offline | iPad app + Drive hardware | OneSoil Mobile, offline |
| Sharing/collab | orgs, dashboards, apps | organizations/roles, farm sharing, client accounts | share operation/farm/fields with agronomist | multiuser |
| Reports/exports | dashboards, apps | PDF/shapefile/GeoTIFF/GeoJSON/ISOXML, batch export | PDF/CSV reports, script file export | boundaries export, task-map export |
| Customer tier | enterprise/GIS professional | growers→consultants→co-ops→dealers | growers (US-centric) + agronomists | farmers + agri-service partners; free entry |

### Stable commonalities (layer B, cross-product)

1. **Georeferenced field/land units** — every product's fundamental record is a field with a spatial boundary, organized under a farm/operation container (Esri: generic feature layers; GeoPard: Farm→Field; FieldView/OneSoil: fields).
2. **Georeferenced layers registered to the same land base** — imagery, yield, soil, as-applied, topography, zones all attach to fields and render on the shared map.
3. **Map canvas as the primary working surface** — all planning, analysis, and scouting happens on the map.
4. **Spatial operations** — measurement (area auto-calc on boundary draw), overlay/comparison (side-by-side, multi-layer analytics), zone derivation (clustering/classification), filtering/querying by attributes/labels.
5. **Agronomic outputs derived from spatial analysis** — management zones, prescription/VRA maps, reports.
6. **Multi-source ingestion** — satellite imagery, machinery files (ISOXML + proprietary), GIS files (shapefile), lab results, partner-platform imports.
7. **Equipment/external handoff** — machine-ready exports (ISOXML, shapefile) and/or platform integrations (John Deere Operations Center named by three of four products).
8. **Mobile field companion** — scouting/notes/offline viewing on a phone/tablet.
9. **Sharing with agronomists/clients** — from simple field sharing to organizations/roles.

### Product-specific findings (layer A, single-product)

- GeoPard: synthetic yield maps (gap restoration), equation catalog with custom Python functions, on-farm trial designs (RCBD etc.), soil-sampling route planning with lab labels, MCP server for LLM agents, API object model (ZonesMaps/RasterMaps).
- FieldView: proprietary Drive hardware for data capture; seed scripts trained on vendor-claimed "million test plots"; grain futures via Combyne; display adapter kits.
- OneSoil: vendor-predefined auto-detected field boundaries (zero-data onboarding); Global Analytics data product (country-scale crop identification); AgroCopilot AI daily ranked attention list.
- Esri: Living Atlas curated content; packaged industry solutions (Invasive Pest Inspections); desktop GIS (ArcGIS Pro) as the analysis workhorse.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

1. **Georeferenced agricultural land units** — identified fields/parcels whose extent is recorded as spatial geometry (boundaries), organized under an operation/farm container or equivalent.
2. **Georeferenced data layers registered to the shared land base** — agronomically meaningful spatial datasets (imagery, soil, yield, as-applied, topography, derived zones) that attach to the land units.
3. **Map canvas as the primary working surface** — the land base and its layers are worked on visually on a map, not primarily in tables.
4. **Spatial operations over the land base** — at minimum measurement and overlay/comparison; characteristically zone derivation and spatial analysis producing agronomic outputs.

Remove any one and the Type collapses: remove (1) → generic drawing/analysis tool; remove (2) → single static map viewer; remove (3) → attribute database (farm records software); remove (4) → map viewer, not a GIS.

Agricultural specialization lives in (1)+(2): the land units are farm fields and the layers carry agronomic meaning. The engine itself is the generic GIS engine (create/manage/analyze/map spatial data — the vendor-standard definition).

### L1 — Common Mature Structure

- Field boundary lifecycle: draw manually, upload (shapefile/KML), import from equipment/partner platforms, edit geometry, auto-computed area, labels/tags (crop, season, client).
- Multi-source ingestion: satellite imagery (Sentinel/Landsat, optionally paid high-res), machinery files (ISOXML + proprietary formats), GIS files, lab results (CSV/Excel), partner-platform sync.
- Yield data pipeline: import → attribute/unit review → clean & calibrate (outliers, striping, multi-machine alignment) → analyze → reuse for zones/prescriptions.
- Management zones: derived from single or multi-layer inputs with user-controlled parameters; editable (merge/split/draw); multi-year stable zones; variability metrics.
- Prescription/VRA map creation: assign rates to zones (seed/fertilizer/lime/crop protection), export machine-ready (ISOXML, shapefile) or push via platform integrations.
- Satellite/imagery monitoring: vegetation indices, time series, in-season change detection.
- Scouting: location-pinned notes/observations; mobile app, often offline.
- Soil data: sampling plans (grid/zone), lab-result mapping, soil-scanner data.
- Topography analytics: elevation/slope/aspect from machinery, LiDAR, or remote sensing.
- Comparison surfaces: side-by-side maps, multi-layer analytics, field benchmarking.
- Reports and exports: PDF/CSV reports; boundary/layer/map exports.
- Sharing/collaboration: share farms/fields with agronomists or clients; organizations/roles at team scale.
- Mobile companion surface for field work.

### L2 — Variant / Optional Structure

- Deployment & form: desktop GIS suite vs cloud platform vs mobile-first; API/white-label embedding.
- Positioning pole: professional GIS toolkit (analysis-first, user must assemble workflows) vs turnkey agronomy analytics (workflow-first) vs grower self-service field-data app.
- Equipment coupling depth: hardware dongles/display adapters; deep bi-directional platform integration; format-only exchange.
- Imagery sourcing: free public satellites vs paid high-resolution tasking vs drone vs vendor hardware.
- Agronomic intelligence depth: AI assistants/recommendations, spraying windows, crop identification, anomaly alerts.
- Economic layer: profit maps, input-savings calculators, market data.
- Trials/experimentation: on-farm trial design and spatial analysis.
- Enterprise structure: organizations/roles, client management for consultants/dealers, multi-farm scale.
- Regional data foundations: national soil surveys, cadastre, vendor-predefined boundary libraries.
- Business model: free tier, per-hectare, subscription, enterprise licensing.

### L3 — Vendor-specific (stays out of the final document)

- GeoPard: ZonesMap/RasterMap API objects; equation catalog + custom Python functions; synthetic yield; MCP server; ADAPT framework usage; specific classification method names.
- FieldView: FieldView Drive hardware; "million test plots" seed-script claim; Combyne grain futures; display adapter kits.
- OneSoil: auto-detected global boundary library; Global Analytics (650M ha claim); AgroCopilot.
- Esri: ArcGIS Pro/Online/Field Maps/Dashboards product names; Living Atlas; geodatabase; Invasive Pest Inspections solution.

## Vendor-specific Findings

See L3 above. Additionally: FieldView's "+5 bu/ac" and OneSoil's "3x–28x ROI" / ">90% correlation" are vendor marketing claims — recorded here, excluded from the final document.

## Boundary Findings

1. **vs Precision Agriculture Platform** (sibling under §20): the sharpest overlap. All sampled precision-ag platforms (GeoPard, OneSoil, FieldView) implement the full ag-GIS core (land base + layers + map + spatial operations); conversely, prescription/VRA machinery appears in every ag-GIS-adjacent product. The working distinction is **center of gravity**: Agricultural GIS centers the *spatial data base and analysis* (the map is the product's spine; outputs are maps/layers/reports), while Precision Agriculture Platform centers the *variable-rate execution loop* (prescription → machine → as-applied verification → agronomic response, with equipment data as a first-class citizen). Structural test: remove the equipment-execution loop → an ag GIS remains; remove the spatial land base/layer model → precision ag collapses into equipment control. This is a gradient, not a wall — products legitimately span both. **Flagged for joint review when Precision Agriculture Platform is processed.**
2. **vs Crop Remote Sensing Platform** (sibling under §20): remote sensing centers *imagery acquisition/analysis as the product* (satellite tasking, index services, imagery delivery); ag GIS consumes imagery as one layer among many. Test: remove imagery → a remote-sensing platform disappears; an ag GIS remains (boundaries, soil, yield still function). In the sampled cloud products satellite monitoring is bundled L1, so the boundary is center of gravity, not feature presence.
3. **vs Farm Management Platform / Field Management / Agronomy Management** (§20 siblings): FMS centers operational/financial records (activities, inventory, inputs, people, costs); ag GIS centers the spatial land base. Sampled products carry *light* record surfaces (field diary, operations log) as secondary features. Test: remove the map/land base → FMS remains; remove records/finances → ag GIS remains.
4. **vs Government GIS / Utility GIS** (§24/§19): all three are domain specializations of the *same generic GIS engine* (create/manage/analyze/map spatial data). They differ in domain data model (administrative parcels & public assets vs utility networks vs farm fields & agronomic layers), users, and workflows — not in engine structure. **Taxonomy observation:** the directory has no generic "GIS" leaf; the three domain GIS leaves share a common core and may deserve a shared framing in a joint review.
5. **Naming observation:** the market rarely sells "agricultural GIS" as a category label; products are marketed as precision-agriculture platforms, field-data platforms, or farm mapping software. The leaf is best understood as the *GIS-structured segment* of agricultural software — defined by structure (land base + layers + map + spatial operations), not by vendor vocabulary.
6. **Historical/market-sample check (§24):** the L0 holds for the classic desktop lineage (1990s–2010s farm mapping products: field boundaries + soil/yield layers + map canvas + measure/overlay/print) and for regional/platform-native products; it does not require satellite imagery, cloud deployment, VRA, or AI. Conversely, a modern precision-ag product stripped of its land base would not be an ag GIS. The definition is therefore not over-fitted to the current cloud era.

## Uncertainties

- The classic desktop/dealer-tier ag GIS lineage (Ag Leader SMS, Trimble Ag/Farm Works, Agrian) was unreachable; its inclusion in the Type rests on indirect evidence (file-format ecosystem, Esri positioning). Assertions about that tier are kept weak.
- John Deere Operations Center was not directly sampled; its structure (boundaries, map layers, work plans, operation data) is asserted only where GeoPard's official integration docs describe it.
- Esri's agriculture-specific *operational* workflows (e.g., how a prescription is built in ArcGIS) were not verified at Tier 1; Esri evidence is positioning-level.
- Exact numeric limits (zone counts, acreage caps, file-size limits, imagery resolution floors) were not researched and are not asserted.
- Whether the market would merge this leaf into Precision Agriculture Platform is a genuine open question; recorded as a boundary issue rather than resolved unilaterally.

## Final Synthesis

An Agricultural GIS is the agriculture-domain specialization of a GIS: a system whose world is a **georeferenced agricultural land base** (identified fields with boundaries) carrying **georeferenced agronomic data layers**, worked on through a **map canvas**, and processed with **spatial operations** (measure, overlay/compare, derive zones, analyze) to produce agronomic outputs — management zones, prescription/VRA maps, reports — that are handed to equipment or people. Everything else commonly bundled (satellite monitoring, yield cleaning, scouting apps, AI advice, profit maps, equipment integrations, organizations/roles) is common mature structure or variant structure, not definition. The Type's sharpest boundary is with Precision Agriculture Platform (center of gravity: spatial data base & analysis vs VRA execution loop) and with Farm Management Platform (spatial land base vs operational/financial records); its sharpest family resemblance is to Government/Utility GIS (same engine, different domain).
