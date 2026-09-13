# Agricultural GIS

## Overview

An **Agricultural GIS** is a geographic information system specialized for farming: it manages a **georeferenced agricultural land base** — identified fields whose extents are recorded as spatial boundaries — carries **agronomic data layers registered to that land base** (satellite imagery, soil, yield, applied-input records, terrain), and works through a **map canvas** on which users measure, overlay, compare, and analyze spatial data to produce agronomic outputs such as management zones, variable-rate prescription maps, and reports.

The defining core is deliberately small:

```text
Agricultural land base (fields with boundaries)
└── Georeferenced data layers registered to the same land base
    └── Map canvas as the primary working surface
        └── Spatial operations (measure · overlay/compare · derive · analyze)
            └── Agronomic outputs (zones, prescriptions, reports)
```

Everything else commonly associated with the category — satellite crop monitoring, yield-data cleaning, scouting apps, AI recommendations, profit maps, equipment integrations, team organizations — is widespread in current products but is not what makes the product an Agricultural GIS. The underlying engine is the same generic GIS engine used by government and utility mapping systems; the agricultural specialization lies in the data domain (farm fields and agronomic layers) and the workflows built on it.

When the center of gravity shifts from the spatial data base to the variable-rate execution loop (prescription → machine → as-applied verification), the product is drifting toward a Precision Agriculture Platform; when records of activities, inputs, and money become the spine, it is drifting toward a Farm Management Platform.

## Users & Context

Primary users are people who make or support agronomic decisions over land:

- **Agronomists and crop consultants** — analyze field variability, build zones and prescriptions for many client farms, share maps with growers.
- **Farm managers and growers** — monitor their own fields, compare season results, prepare task maps for their equipment.
- **Precision-agriculture specialists** at cooperatives, input retailers, and equipment dealers — run zoning, soil-sampling, and trial programs as a service for customers.
- **GIS professionals** inside larger agribusinesses and agricultural agencies — manage the land base and produce maps and dashboards for the organization.

Secondary participants include equipment operators (who receive machine-ready prescription files and generate yield/as-applied data back), field scouts (who record observations on mobile devices), and administrators (who manage farms, users, and sharing).

The work follows the crop season: boundary and data setup in the off-season, prescription building before planting, imagery monitoring and scouting in-season, harvest-data analysis after harvest — with each season's results feeding the next season's zones and prescriptions.

## Core Model

### The Defining Core

**Agricultural land base.** The system's fundamental record is the **field**: a named, identified unit of farmland whose extent is stored as spatial geometry (a boundary polygon). Fields are organized under a container — a farm, operation, or client — and carry organizing labels such as crop, season, or client. Boundaries can be drawn by hand on the map, uploaded as GIS files, imported from equipment platforms, or (in some products) selected from a vendor-prepared library of detected field boundaries. Area is computed from the geometry. Boundaries are editable: correcting geometry keeps every analysis aligned with the real field.

**Data layers.** Onto this land base the system registers georeferenced data layers, each bound to a field (or set of fields):

- **satellite/aerial imagery** and derived vegetation indices, often attached automatically once a boundary exists;
- **yield maps** from harvest monitors;
- **as-applied / as-planted records** from sprayers, spreaders, and planters;
- **soil data** — lab results, soil-scanner readings, soil-type maps;
- **topography** — elevation, slope, aspect derived from machinery, LiDAR, or remote sensing;
- **derived layers** — management zones, prescription maps, equation-based analytics, profit maps.

A layer without a land unit to attach to has no home in the system; conversely, one field typically accumulates many layers across years.

**Map canvas.** The map is the primary working surface, not a report decoration. Fields are found spatially and by name; layers are switched, styled, and compared visually; measurements, zone edits, and boundary edits happen directly on the map.

**Spatial operations.** The system's analytical value comes from operations over the land base:

- **measurement** — area, distance (computed automatically from geometry);
- **overlay and comparison** — side-by-side maps, multi-layer analysis, layer transparency;
- **derivation** — clustering layer values into management zones under user-controlled parameters (input layers, weights, zone count, classification method), with zones remaining editable (merge, split, redraw);
- **query and filtering** — selecting fields and layers by attribute, label, or season.

**Agronomic outputs.** Spatial analysis terminates in artifacts people and machines use: management zones, variable-rate prescription maps (rate values assigned per zone for seed, fertilizer, lime, or crop protection), printed or PDF/CSV reports, and exported map files.

### Standard Capabilities of Mature Products

These capabilities are common across the researched sample and make the Type practical, without defining it:

- **Multi-source ingestion** — GIS files (shapefile, KML), machinery files (ISOXML and proprietary harvester/display formats), lab results (CSV/Excel), satellite imagery feeds, and direct synchronization with equipment data platforms.
- **Yield-data pipeline** — raw harvest files are reviewed (attributes, units, fit to the field boundary), cleaned and calibrated (outliers, striping, multi-machine and multi-day alignment), and only then used for zones and prescriptions.
- **Prescription building** — rates assigned to zones through a distribution tool; output as machine-ready files or pushed to an equipment platform.
- **In-season imagery monitoring** — vegetation-index time series, change detection, anomaly flags.
- **Scouting** — location-pinned observations recorded on a mobile app, often usable offline, and exportable as map layers.
- **Soil-sampling support** — grid- or zone-based sampling plans with generated points and routes.
- **Comparison and benchmarking** — compare fields, seasons, hybrids, or practices on comparable spatial footprints.
- **Sharing** — scoped sharing of an operation, farm, or single field with an agronomist or client; organizations and roles at team scale.
- **Mobile companion** — a field-side surface for viewing maps and recording observations.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Land base
Implementations:  user-drawn boundaries · uploaded GIS files · equipment-platform import ·
                  vendor-predefined detected boundary libraries

Concept:  Data layers
Implementations:  free public satellite imagery · paid high-resolution tasking · drone imagery ·
                  machinery files · lab results · soil-scanner passes

Concept:  Spatial analysis
Implementations:  full desktop GIS toolkits · guided cloud zoning wizards ·
                  equation/formula engines over layers

Concept:  Output handoff
Implementations:  machine files (ISOXML, shapefile) · wireless transfer ·
                  bi-directional equipment-platform integration · printed/PDF maps
```

## How It Works

### 1. Establish the land base

```text
Create the farm/operation container
→ add fields: draw the boundary on the map, upload a GIS file,
  or import from an equipment platform
→ the system computes area from the geometry
→ label fields (crop, season, client)
→ correct boundaries later as the real field changes
```

In several products, creating a boundary immediately triggers background processing: historical satellite imagery for that exact footprint is attached to the new field automatically.

### 2. Accumulate layers

```text
Import or connect data sources
→ machinery files (yield, as-applied, as-planted), GIS files, lab results,
  imagery feeds, equipment-platform sync
→ each dataset is linked to its field and appears as a layer
→ raw machinery data passes through review, cleaning, and calibration
  before it is trusted for analysis
```

### 3. Analyze on the map

```text
Open a field (or a whole farm view)
→ switch, style, and overlay layers
→ compare layers side by side or combine them
→ derive management zones from one or many layers
  (user sets inputs, weights, zone count, classification method)
→ edit zones (merge, split, redraw) and save the zones map
```

### 4. Produce and hand off outputs

```text
Assign rates to zones (seed / fertilizer / lime / crop protection)
→ generate the prescription map
→ export as a machine-ready file (e.g., ISOXML for displays, shapefile for GIS)
  or push it to an equipment data platform
→ operators execute in the field
```

### 5. Close the seasonal loop

```text
Monitor imagery in-season → scout problem areas (mobile, pinned notes)
→ harvest: yield and as-applied data flow back into the system
→ verify: compare prescribed vs actually applied rates, and yield by zone
→ post-season analysis (zone performance, trials, profit by zone)
→ next season's zones and prescriptions are built from the accumulated layers
```

The defining loop is therefore **land base → layers → spatial analysis → agronomic output → field execution → data back into the land base**. The land base is the durable spine; layers and derived artifacts accumulate around it year over year.

## Interfaces

Exact layouts vary by product; the following surfaces recur across the sample.

### Field list / farm view

The entry surface: fields listed and shown on a map, with labels, crops, and summary indicators.

- typical information: field name, farm, area, crop, season labels, latest imagery or alert state
- primary actions: open a field, add/edit a field or boundary, filter by label, bulk actions

### Field detail (layer workspace)

The per-field map workspace where all layers of one field are stacked.

- typical information: boundary, imagery time series, yield/soil/as-applied layers, dataset lists with dates
- primary actions: toggle and style layers, compare dates, import data, launch analysis

### Zone / prescription editor

The derivation surface where layers become zones and zones become prescriptions.

- typical information: input layer selection, zone count/classification parameters, per-zone rate values, computed statistics
- primary actions: generate zones, merge/split/draw zones, assign rates, save, export

### Comparison / analysis surface

Side-by-side and multi-layer comparison of maps, fields, seasons, or practices.

- typical information: synchronized maps, legends, per-zone or per-field statistics
- primary actions: select layers/fields to compare, compute comparisons, build reports

### Import / export surfaces

File upload (machinery, GIS, lab formats) and download/export (machine files, GIS files, reports), plus connections to equipment data platforms.

### Mobile scouting app

A field-side map surface for viewing layers and recording pinned observations, frequently with offline support.

### Administration / sharing

Farm and user management, organizations and roles, scoped sharing of farms or fields with colleagues, clients, or agronomists.

## Important Rules / Behaviors

- **Everything registers to the land base.** Data must be linked to a field to exist in the system; imported datasets are checked for fit against the field boundary. The boundary is the reference geometry for every layer and statistic.
- **Boundary edits re-align analytics.** Correcting a boundary is not cosmetic: area, zone statistics, and data-to-field matching follow the corrected geometry.
- **Raw machinery data is not analysis-ready.** Yield and as-applied files routinely contain noise (turns, stops, overlaps, striping between machines or days); cleaning and calibration is a standard, user-visible gate before the data feeds zones or prescriptions.
- **Derived layers are parameterized artifacts.** Zones maps and prescription maps are computed from chosen inputs and settings; they can be cloned, re-derived with different parameters, and kept as stable multi-year versions.
- **Prescriptions must match the machine.** A prescription is only executable once exported in a format the target display accepts; products commonly provide multiple format variants and leave the choice to the user's equipment.
- **Sharing is scoped.** Access is granted at the level of operation, farm, or single field; consultant and dealer usage depends on sharing one organization's fields with another account.
- **The map is the index.** Fields are located spatially as well as by name/label; a user who can find a place on the map can find the corresponding records.

## Variants

Common shapes of the Type:

- **Professional GIS toolkit** — a full GIS platform applied to agriculture; maximum analysis depth and generality, with the user assembling agricultural workflows from generic tools; typical in large agribusinesses, agencies, and GIS teams.
- **Turnkey cloud analytics platform** — guided zoning/prescription workflows over an automatically maintained land base; serves growers through consultants, co-ops, and dealers.
- **Grower self-service field-data platform** — simplified map-first surfaces, often coupled to proprietary capture hardware, oriented to a single operation.
- **Satellite-first platform** — the land base may come pre-populated from vendor-detected field boundaries; imagery is the default first layer; free or low-cost entry tiers.
- **Equipment-ecosystem-attached** — deep bi-directional integration with one equipment maker's data platform, with the GIS serving as the analysis layer around it.
- **Consultant/dealer multi-client operation** — the same core run across many client farms, with client/organization structures, batch processing, and white-label or API embedding.

A variant remains a variant while the defining core holds; when the execution loop or the record-keeping spine takes over, the product belongs to a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Precision Agriculture Platform | closest overlap | centers the variable-rate execution loop (prescription → machine → as-applied verification) with equipment data as a first-class citizen; Agricultural GIS centers the spatial data base and analysis. Remove the execution loop and an ag GIS remains; remove the land base and precision ag collapses into equipment control. Products frequently span both. |
| Crop Remote Sensing Platform | adjacent | imagery acquisition/analysis is the product (tasking, index services); in an Agricultural GIS imagery is one layer among many. Remove imagery and the remote-sensing platform disappears while the ag GIS survives on boundaries, soil, and yield. |
| Farm Management Platform | adjacent | centers operational and financial records (activities, inventory, inputs, people, costs); the spatial base is secondary. Remove the map/land base and farm management survives; remove the records and the ag GIS survives. |
| Field Management / Agronomy Management | adjacent | center field-level records and agronomic workflow rather than the georeferenced land base; their data commonly appears as layers inside an Agricultural GIS. |
| Government GIS / Utility GIS | same engine, different domain | all three are domain specializations of the generic GIS engine (create, manage, analyze, map spatial data); they differ in data model (administrative parcels and public assets / utility networks / farm fields and agronomic layers), users, and workflows. |
| Soil / Nutrient / Irrigation Management | capability hosts | domain practices whose data (soil tests, nutrient plans, irrigation zones) typically lives inside an Agricultural GIS as layers and prescriptions rather than as standalone map systems. |

## Representative Products

- **Esri ArcGIS** (agriculture industry focus) — professional GIS platform applied to agriculture; enterprise/GIS-team tier.
- **GeoPard** — cloud-native precision-agriculture analytics platform with full GIS machinery; grower-to-dealer tier.
- **Climate FieldView** — grower-tier cloud field-data platform with proprietary capture hardware.
- **OneSoil** — satellite-first platform with vendor-predefined field boundaries and a free entry tier; farmer and agri-service tier.

The definition was checked against the older desktop farm-mapping lineage (field boundaries + soil/yield layers + map canvas + measure/overlay/print) and against domain siblings (government/utility GIS) to avoid over-fitting to the current cloud era.

## Sources

Research date: **2026-09-06**

- Esri — GIS for Agriculture: https://www.esri.com/en-us/industries/agriculture/overview
- Esri — Farm Planning and Decision-Making: https://www.esri.com/en-us/industries/agriculture/segments/farm-planning-decision-making
- Esri — What is GIS?: https://www.esri.com/en-us/what-is-gis/overview
- GeoPard — product site: https://geopard.tech/
- GeoPard — official product documentation: https://docs.geopard.tech/geopard-tutorials/sitemap.md (incl. Zones Maps and Analytics; Draw a new field; Export VRA Map in ISOXML Format; Yield Data & Harvest Analytics)
- Climate FieldView — https://climate.com/ ; https://climate.com/en-us/solutions/build-prescriptions.html ; https://climate.com/en-us/solutions/analyze-data.html
- OneSoil — https://onesoil.ai/en/ ; https://onesoil.ai/en/platform

> Sourcing limitation: the classic desktop/dealer-tier agricultural GIS products (Ag Leader SMS, Trimble Ag Software/Farm Works, Agrian) could not be reached from the research environment on 2026-09-06 (404 / transport errors / 403), and John Deere Operations Center pages were JavaScript-rendered (its structure is evidenced only indirectly through GeoPard's official integration documentation). Claims about those products are therefore not made. Esri evidence is positioning-level rather than operational. Vendor marketing figures (yield-lift, ROI, correlation claims) observed on product pages were excluded from this document. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
