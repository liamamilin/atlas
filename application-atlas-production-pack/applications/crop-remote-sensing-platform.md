# Crop Remote Sensing Platform

## Overview

A **Crop Remote Sensing Platform** is a field-anchored agricultural monitoring application. It attaches imagery acquired by satellites, aircraft, or drones to identified fields, turns that imagery into dated crop-condition indicators, and translates within-field variability into crop-management decisions — surfacing problems to the people who act on them and, in mature products, converting them into zone and prescription outputs that machinery can execute.

The defining core is deliberately small:

```text
Field (boundary + crop + season context)
└── Imagery acquisitions from remote sensing, dated
    └── Crop-condition indicators computed over the field
        └── Within-field variability, delivered into crop management
            (views · alerts · reports · scouting handoff · zone/prescription maps)
```

Everything else commonly associated with the category — vegetation-index catalogs, cloud-free satellite backbones, weather layers, growth-stage models, yield estimation, AI advisors, equipment integrations — is widespread in current products but is not what makes the product this Type. Older forms satisfy the same structure: aerial infrared photography interpreted by an agronomist to locate stressed areas, and regional satellite crop-monitoring programs, are both recognizable instances of this Type without any of the modern machinery.

When the center of gravity shifts — to equipment data and execution, to records and economics, or to general-purpose map layers — the product is drifting toward a different Application Type (Precision Agriculture Platform, Farm Management Platform, Agricultural GIS).

## Users & Context

The primary users are people responsible for crop outcomes across many hectares:

- **growers / farm managers** — watch crop development across their own fields, decide where to spend inputs and attention
- **agronomists and crop consultants** — monitor fields for many clients at once, prioritize visits, and turn observed variability into recommendations
- **scouts and field staff** — receive where-to-look direction from the imagery and record what they find on the ground

Secondary consumers observed in the market include agribusiness and food companies monitoring contracted production, and insurers using imagery to date and localize damage. The work context is seasonal and split-surface: a web workspace in the office for portfolio-level review, and a mobile application in the field for ground-truthing. The platform is used repeatedly through the growing season rather than episodically — its value comes from watching change over time.

## Core Model

### The Defining Core

**1. The field as the anchor.** Everything in the system attaches to an identified field: a bounded parcel of land, usually carrying a crop and a season attribution. Fields are created by drawing on a map, importing boundary files, selecting from predefined boundaries, or syncing from equipment systems. The field — not the pixel, not the image — is the unit of record: imagery, indicators, zones, tasks, and history all hang from it. Crop and season context is what makes the same parcel's data interpretable year over year.

**2. Remotely sensed crop-condition indicators.** Imagery arrives from remote sensing platforms — earth-observation satellites, aircraft, or drones — and the platform processes it into indicator layers that describe crop state: vegetation vigor, biomass, moisture. Conceptually these are *dated observations of crop condition over a field*; the familiar vegetation indices (NDVI and its relatives) are the common implementation, and the specific index catalog varies by product and plan. Multiple acquisitions across the season are the norm — monitoring is a time-series activity, and historical seasons are retained for comparison.

**3. Within-field variability as the analytic output.** The platform's essential question is not "how is the crop?" but "where is it different, and where is it wrong?" Indicator maps are read for spatial patterns — low-vigor patches, stress gradients, anomalies between dates — and products typically formalize this into zones (management or productivity zones) and highlighted problem areas. This localization is what makes the output actionable rather than merely pictorial.

**4. Delivery into crop management.** Observed variability must reach the people and machines that act:

- **alerts and risk views** — notifications that something changed or a risk window opened
- **scouting handoff** — marked locations or tasks that direct ground inspection, with findings recorded back
- **reports** — field-state summaries shared with teams, clients, or stakeholders
- **zone and prescription maps** — machine-ready outputs (variable-rate seeding, fertilization, spraying) exported in equipment-compatible formats

The specific forms vary by product; the property that observation becomes input to crop-management decisions is constant. A product that only displays imagery with none of this delivery is an imagery viewer, not a monitoring platform.

### One Structure, Many Implementations

The core model is written conceptually. Current products realize each part differently:

```text
Field boundary:      drawn on map · imported files · predefined libraries ·
                     auto-detected · synced from equipment systems

Sensing source:      free public satellite constellations (the common backbone) ·
                     paid high-resolution commercial imagery · drone captures ·
                     combinations of these

Indicator:           vegetation indices (NDVI family) · biomass maps ·
                     moisture/water layers · derived stress or anomaly layers

Processing place:    provider cloud · offline on-device (desktop) · hybrid

Action delivery:     alerts · scout tasks/pins · PDF or generated reports ·
                     zone maps · variable-rate prescription exports
```

## How It Works

The season loop, as it typically flows:

### 1. Establish the field portfolio

```text
Create/import field boundaries
→ attribute each field with crop and season
→ (optionally) import prior-season history
```

Some products lower this to near-zero effort: predefined boundaries can be selected straight from a map, so monitoring can start without uploading anything. The field set is durable — it persists across seasons and accumulates history.

### 2. Receive and process imagery

```text
Satellite pass over the area (or a drone flight is flown)
→ imagery ingested and processed into indicator layers
→ cloud/shadow effects handled (masking, or substitution from a clearer pass)
→ new dated observation attached to the field
```

On satellite-first products this happens automatically as constellations revisit the area. On drone-first products the user flies, then processes — some process offline on a laptop within minutes; others use the provider's cloud. Paid high-resolution imagery is a common upgrade over the free-constellation backbone.

### 3. Review state and change

```text
Open a field (or scan the whole portfolio)
→ read the current indicator map
→ compare against earlier dates and prior seasons
→ inspect charts of indicator values over time
→ note anomalies, gradients, and problem patches
```

Portfolio-level review (a list or map of all fields with their latest state) is how users with many fields — and consultants with many clients — triage attention. Some products rank or alert on the fields that need attention first.

### 4. Ground-truth

```text
Flag suspicious zones on the map
→ send a scout / open the mobile app at the field
→ record findings with photos, tags, notes at the flagged spot
→ the ground observation is attached back to the field record
```

The imagery tells users where to look; the ground observation tells them what it actually is. Several products close this loop explicitly — shareable pins, assignable scouting tasks, or AI-generated inspection questions about a map.

### 5. Act

```text
Adjust the field operation the observation concerns
— direct inputs by zone (variable-rate map exported to machinery)
— time the operation (weather and spray-window views)
— treat the problem area (spot application)
→ outcomes (application records, later imagery) become new evidence on the field
```

### 6. Report and share

Field-state reports are generated (manually or automatically) and shared with teams, agronomists, or stakeholders; sharing can extend to whole operations or single fields with an outside advisor.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Portfolio view (field list / map)

The entry surface for multi-field operations.

- all fields with their latest indicator state and alert status
- primary actions: scan for problems, open a field, triage attention

### Field map workspace

The central analysis surface.

- the field's boundary on a base map with selectable indicator layers
- date navigation: switch acquisitions, play through the season, compare dates or seasons side-by-side
- layer pickers (vegetation, moisture, imagery basemaps), measurement and annotation tools
- primary actions: inspect zones, flag problem areas, create zones, launch scouting

### Time-series panel

- indicator values for the field (or a zone) charted across the season and prior seasons
- weather context commonly placed alongside
- primary actions: select dates, correlate a change with events

### Mobile scouting app

- field imagery on the phone, current location on the map
- primary actions: drop a pin with photos/tags/notes, complete assigned scouting tasks, work offline

### Zone / prescription editor

- convert an indicator map into management zones; assign values per zone
- primary actions: adjust zone boundaries, set rates, export in machinery-compatible formats

### Alerts, reports, sharing

- notification surfaces for crop-health, weather, and imagery-availability events
- generated or composed field reports; sharing controls for teams and external advisors

## Important Rules / Behaviors

### Imagery availability is governed by physics, not by the subscription alone

Satellite acquisitions depend on orbit schedules and weather: clouds can obscure passes, and products respond by masking affected areas, substituting a clearer acquisition, or offering paid higher-resolution sources. Users of satellite-first products plan around this; drone capture is the common way to fill a gap on demand. This availability rhythm is a structural behavior of the Type — monitoring is only as current as the last usable acquisition.

### Indicators are proxies, not diagnoses

A low-vigor zone means "something differs here" — moisture, nutrition, disease, compaction, soil, damage. The map directs attention; it does not by itself name the cause. Ground-truthing (scouting) is the normal closing step, and products that add advisory or AI layers still present them as guidance on top of the indicator, not as a replacement for field verification.

### The field is the unit that makes analysis meaningful

Indicator values are computed within field boundaries and against crop/season context. The same raw imagery without a field attribution is just pixels; crop and season context is what makes trends, comparisons, and zone statistics interpretable. Boundary edits and crop corrections change downstream analysis.

### Resolution and decision granularity are matched deliberately

Satellite indicator layers suit whole-field and zone-level decisions; drone captures resolve plant-level detail (weed patches, stand counts, damage assessment). Mature products either offer both sources or position themselves clearly on one side of that trade-off.

### Data ownership and sharing are first-class concerns

Who can see which fields — teams, advisors, clients — is governed by sharing and role controls, and the grower's ownership of their own agronomic data is an explicit product principle in parts of this market. Sharing an operation, a farm, or a single field are distinct, controllable acts.

### History is retained and reused

Prior seasons remain attached to fields: current-season maps are read against historical baselines, and multi-season comparison is a standing analytic view, not an archive afterthought.

## Variants

Common realizations of the Type:

- **Satellite-first monitoring platforms** — cloud services built on earth-observation constellations; freemium access is common; portfolio view, alerts, reports, and APIs; the typical choice for consultants, agribusiness, and geographically dispersed operations.
- **Drone-first field tools** — desktop or tablet applications that process drone (often multispectral) captures, frequently offline and on the spot; strong on prescription-map output and spot applications; typical for agronomy service providers and tech-forward growers.
- **Imagery inside grower data platforms** — satellite imagery and scouting as one capability within a broader agronomic platform centered on the grower's own equipment and yield data; common in equipment-data-heavy regions, sometimes with proprietary cab hardware attached.
- **Lightweight free-entry platforms** — minimal onboarding (predefined field boundaries), monitoring-first, precision tools (zones, task maps) layered behind subscription; typical for smaller growers and emerging markets.
- **Advisory-augmented products** — imagery combined with agronomic models or AI assistants that rank what needs attention, suggest causes, or generate recommendations; depth varies and is evolving quickly.

Historical note: aerial-photography crop monitoring services and regional satellite crop-monitoring programs precede the current cloud era and satisfy the same core structure with none of its modern machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Precision Agriculture Platform | adjacent, broader | centers on equipment data and executing variable-rate operations; imagery is one input. Remove remote sensing and a precision-ag platform still stands; remove equipment telemetry and this Type still stands |
| Farm Management Platform | adjacent | centers on records, plans, inputs, and economics; imagery appears here only as an observation feed. Remove sensing and the FMS survives intact |
| Agronomy Management / Crop Management | sibling record types | manage agronomic decisions, recommendations, and programs as records; this Type supplies the observed evidence those decisions can draw on |
| Agricultural IoT Platform | adjacent, complementary | ground sensors measure point conditions continuously; remote sensing covers whole fields periodically. Products often combine both, but the sensing geometry differs |
| Agricultural GIS | adjacent | general geospatial layer management and cartography without crop semantics or the season monitoring loop |
| Photogrammetry Application | upstream machinery | reconstructs orthomosaics/3D from photos; a drone-realized crop platform builds on photogrammetry but its output is crop indicators, zones, and prescriptions |
| Environmental Monitoring Platform | domain neighbor | monitors environmental condition and compliance rather than crop production over fields; overlap only where agri-environment programs consume crop-imagery outputs |
| Irrigation Management | downstream consumer | a decision domain that can consume this Type's moisture and vigor indicators as one input |

The most important boundary is with **Precision Agriculture Platform**: the two overlap on zones and prescriptions. The structural test is the center of gravity — if the product's reason to exist is *sensing fields and localizing variability for decisions*, it is this Type; if it is *managing equipment data and executing operations*, it is Precision Agriculture. Products exist on both sides of the seam, and some span it deliberately.

## Representative Products

- **EOSDA Crop Monitoring** (EOS Data Analytics) — satellite-first monitoring platform, freemium, global; strong alert/risk and consultant orientation
- **OneSoil** — free-entry web + mobile platform with predefined field boundaries and precision-ag tools layered on subscription
- **Climate FieldView** (Bayer / Climate LLC) — imagery and scouting embedded in a broader grower data platform with equipment-data hardware; large commercial growers
- **PIX4Dfields** (Pix4D) — drone-first desktop tool with offline processing and built-in satellite access; prescription-map output

The core model was checked against older and differently positioned forms (aerial-photography-era crop monitoring, regional satellite programs, and imagery embedded in farm-management ecosystems) to avoid defining the Type by the current free-constellation, cloud-era pattern.

## Sources

Research date: **2026-09-07**

- EOS Data Analytics — EOSDA Crop Monitoring product page: https://eos.com/products/crop-monitoring/
- OneSoil — Platform page and FAQ: https://onesoil.ai/en/platform
- Climate LLC (Bayer) — Climate FieldView homepage and Scout Fields solution page: https://climate.com/ , https://climate.com/en-us/solutions/scout-fields.html
- Pix4D — PIX4Dfields product page: https://pix4d.com/product/pix4dfields/

> Sourcing limitation: vendor help centers and support portals were not reachable as full documentation from the research environment on 2026-09-07 (one vendor's site was entirely unreachable; others expose deep documentation behind interactive applications). Observations rest on official product pages and FAQs. Vendor-quantified figures (index counts, resolution tiers, forecast windows, performance claims) were reviewed but are intentionally not repeated in this document; capability statements are kept at the strength the accessible evidence supports.
