# Utility GIS

## Overview

A **Utility GIS** is a geographic information system operated by a utility to maintain the authoritative georeferenced model of its physical network — the plant (conductors and wires, pipes, poles, transformers, valves, devices, meters, structures) and, critically, **how it connects** — and to turn that model into maps, tracing, and analysis for the utility's engineering, field, and operations work, and for the systems that consume the network model.

Its defining core is deliberately small: a persistent store of georeferenced data organized as layers, a map canvas that composites those layers, spatial operations over them, and the utility specialization — the system holds the network as a **connected, traversable model of record**, not merely a set of located assets.

Everything else commonly associated with modern utility GIS — packaged industry data models, connectivity-rule engines, trace toolkits, one-line schematic diagrams, design-to-as-built workflows, mobile field apps, AI-assisted validation — is standard or optional capability in current products, not part of the definition. The desktop utility GIS of the 1990s–2000s (connected features, printed circuit maps, tool-assisted tracing) fits the same definition without any of the modern machinery.

## Users & Context

The primary operator is the utility's own mapping/GIS function — the GIS analysts and mapping technicians of an electric distributor, gas utility, or water/wastewater utility. They maintain the network model: editing features and connectivity, validating changes, and keeping the model current as the network changes.

The model's consumers are broad, and their dependence on it is what shapes the system:

- **Distribution and transmission engineers** — trace the network, analyze connectivity and capacity, and prepare designs against the model.
- **Field crews** — locate assets in the field, and increasingly capture as-built changes directly into the model.
- **Operations and outage staff** — consume the model directly or through the operational systems (outage management, distribution management) that derive their working copies from it.
- **Customer service and billing** — look up which transformer or main serves a premises, using service-point bindings maintained in the model.

The work context is long-lived and custodial: the network model outlives any individual map, project, or staff tenure; it is edited by few and consumed by many; and it carries an accuracy expectation that ordinary business mapping does not — because outage prediction, isolation decisions, and crew safety depend on the model saying what the network actually is.

## Core Model

### The Defining Core

```text
The Utility's Connected Network Model of Record
└── Georeferenced layers (features: geometry + attributes, under a coordinate reference system)
    └── Map canvas (layers composited into an interactive map)
    └── Spatial operations (select/query, measure, overlay/proximity analysis)
    └── Connectivity (how features join into a traversable network)
    └── Persistent as-built custody by the utility operator
```

Five properties. If one is removed, the product is no longer recognizable as a Utility GIS:

- **Connected network model of record** — the data the system maintains is the utility's physical network held as a *connected* model: not just where each asset sits, but how the plant joins into a traversable whole — which conductor feeds which transformer, which valve isolates which main segment. This is what makes the specialization *utility*: the same engine mapping parcels and addresses is a Government GIS; mapping fields and agronomic layers is an Agricultural GIS. Without connectivity, only utility asset mapping remains — a substrate other systems maintain, not the network model the utility operates from.
- **Georeferenced layers** — the unit of data organization. A layer holds features (point, line, polygon — or raster cells) whose positions are tied to the earth through a coordinate reference system, each carrying attributes. Remove it and only a drawing or charting tool remains.
- **Map canvas** — layers composited, ordered, and styled into an interactive map the user navigates, queries, and reads. Remove it and the system is a database, not a mapping application.
- **Spatial operations** — selecting by location or attribute, measuring distance/area, overlaying layers to find intersections or proximity, deriving new layers. Remove them and the product is a static map image.
- **Persistent as-built custody** — edits accumulate in the store under the operator's governance; the model is the record of the network *as built*, surviving staff turnover and any individual project. Remove it and the product is a personal mapping project.

### Capabilities Shared by Mature Products

A typical modern Utility GIS carries most of the following. They make the custodial role practical, but they do not define the Type.

- **Industry data models** — packaged plant taxonomies for electric, gas, water/wastewater (and commonly telecom) networks; transmission/distribution or pressure-tier organization; asset classification hierarchies.
- **Connectivity rules and validation** — rules governing which feature classes may connect to which; edit-time enforcement that rejects logically invalid connections; validation passes and error inspection that keep the model's topology current with its geometry.
- **Tracing toolkits** — upstream/downstream, isolation, and connected traces; condition barriers (for example, stop the trace at closed devices); named, reusable trace configurations shared with web and field applications.
- **Network diagrams** — schematic and one-line views derived from the same model, giving engineers a symbolic complement to the geospatial view.
- **Subnetwork management** — feeders, pressure zones, and circuits defined and maintained on the model, with customer and load summaries per subnetwork.
- **Model distribution to consumers** — publishing the model as services, exports, and integrations that feed outage management, distribution/grid management, asset management, field apps, and billing (service locations, transformer and feeder bindings).
- **Design-to-as-built loop** — proposed designs and staking captured as versions or proposals, then reconciled into the model once construction closes.
- **Field and mobile access** — viewing, collecting, and updating the model in the field, commonly offline with synchronization.
- **Cartographic production** — circuit and feeder maps, thematic maps per audience, print and PDF export, web maps.
- **Multiuser editing governance** — versions, conflict resolution, permissions, and audit-grade edit trails.
- **Landbase and basemap context** — parcels, addresses, imagery, and streets consumed as reference layers.
- **Service-point bindings** — links between network features (transformers, mains, service locations) and the customers they serve.

### One Structure, Many Implementations

The core model is written conceptually. Specific products realize it differently:

```text
Concept:              Connected Network Model
Implementations:      geometric-coincidence topology, explicit connectivity associations
                      between non-coincident features, connectivity fields on records,
                      vendor-packaged industry data models

Concept:              Network Model of Record
Implementations:      enterprise geodatabase, vendor proprietary store,
                      cloud-native platform store, single-user file geodatabase

Concept:              Distribution to Consumers
Implementations:      web map services, derived operational copies in consuming systems,
                      direct database integrations, packaged connectors
```

A reader who has only seen a modern cloud platform should still be able to recognize a desktop-era utility GIS — and vice versa — from the core model.

## How It Works

### Build and maintain the network model

```text
Create or acquire the model (convert legacy records, digitize, import)
→ define the industry data model (plant classes, connectivity rules)
→ edit under governance (snapping, connectivity rules, validation)
→ keep the model current as the network changes
  (as-built updates from design, construction, and field capture)
```

This is the perpetual loop that distinguishes the Type: the network is never finished. New services, replacements, and relocations alter the model every working day. Editing is deliberate and controlled — few staff, explicit rules, validation passes — because operational consumers depend on the model's accuracy.

### Trace and analyze the network

```text
Pick a start point
→ run a trace (upstream / downstream / isolation / connected)
→ apply barriers and conditions (e.g., stop at open devices)
→ read results (affected features, customers served, valves to close)
```

Tracing is the signature spatial operation of the Type — enabled by connectivity and meaningless in a generic GIS. Typical questions: what is upstream of this fault, which valves isolate this main break, which customers are served by this feeder.

### Produce map products

```text
Assemble layers → style and label
→ compose circuit/feeder maps and one-line diagrams
→ print, export, or publish as web maps
```

### Serve the model to consumers

```text
Publish the model as services and integrations
→ operational systems derive their working copies
  (outage prediction, distribution management, engineering analysis)
→ field apps render the model for crews
→ corrections to the model propagate to every consumer
```

This is the multi-consumer loop: one maintained model feeds the outage system's prediction logic, the engineer's trace, the crew's field map, and the billing system's service-point lookups — so all consumers work from the same as-built truth.

### Core vs Standard vs Optional

**Defining core** — without these, not a Utility GIS:

- connected network model of record (plant held with connectivity)
- georeferenced layers (geometry + attributes, coordinate reference systems)
- map canvas
- spatial operations
- persistent as-built custody

**Standard capabilities** — present in most mature products:

- industry data models, connectivity rules and validation, tracing toolkits
- network diagrams, subnetwork management, model distribution to consumers
- design-to-as-built loop, field/mobile access, cartographic production
- multiuser editing governance, landbase context, service-point bindings

**Optional / variant** — depends on commodity, scale, and era:

- packaged telecom-domain extension of the same engine
- AI-assisted validation and field guidance
- grid-orchestration integrations (the model as backbone for operational platforms)
- cloud-native or on-premises deployment choices

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Desktop editing workspace

The GIS professional's primary surface.

- map canvas at the center; layer list, attribute tables, and asset templates around it
- connectivity-aware editing tools (snapping, connection points, rule enforcement, validation)
- primary actions: add/edit features, establish connectivity, run validation, commit edits

### Map viewer / web maps

The browser surface for consumers across the utility.

- layer composition, basemaps, pop-ups with asset attributes
- primary actions: navigate, search assets, toggle layers, measure, open trace results

### Trace and analysis panels

The engineer's working surface.

- trace type selection (upstream/downstream/isolation/connected), barrier and condition setup
- primary actions: run traces, save named configurations, summarize results (customers, load)

### Network diagram views

Schematic surfaces derived from the same model.

- symbolic one-line or schematic representations with simplified content
- primary actions: generate from a selection or subnetwork, navigate, compare with the map

### Field / mobile apps

The crew-facing surface.

- the same network model rendered for field context, commonly offline
- primary actions: locate assets, inspect, capture as-built changes, sync when connected

### Administration

The governance surface.

- connectivity rules, validation settings, versions, permissions
- primary actions: configure rules, manage versions and access, monitor edit activity

## Important Rules / Behaviors

### Connectivity rules govern what may connect

The model is not free-form drawing: rules define which feature classes may connect or associate with which, and invalid edits are rejected or flagged at edit time. This is what keeps the model traversable — a trace is only as trustworthy as the connections it walks.

### The model is the record — many consume, few edit

Editing rights on the network model are restricted to designated staff; edits pass through explicit sessions and validation. Published maps and derived copies inherit whatever the model says — there is normally no separate "official" copy that drifts.

### Trace results are only as good as the model's currency

A stale model produces wrong isolation decisions and wrong outage extents. Mature products make topology currency visible (marking edited areas as not-yet-validated) so editors and consumers can see where the model lags reality.

### Flow physics differ by commodity

Electric distribution is typically radial with source-based flow; gas and water networks are pressurized and commonly looped, so flow direction can be ambiguous. The same trace machinery serves different physics — upstream/downstream semantics, isolation behavior, and loop handling are configured per network.

### Service points bind the network to customers

Bindings between network features (transformers, mains, service locations) and premises are what let the model answer customer-facing questions — and what operational and billing systems consume. Keeping these bindings current is part of the custodial duty.

### Coordinate reference systems are structural

All geometry lives under a defined coordinate reference system; mixing sources requires explicit handling, because measurements, overlays, and tracing are only meaningful within a consistent frame.

## Variants

- **Platform engine** — a generic GIS platform with a purpose-built utility network data model that the utility configures; the dominant modern commercial form.
- **Purpose-built network model** — a vendor platform whose industry data model and network semantics are the product (heritage enterprise pole, strong in electric/gas and telecom).
- **Solution suite on a platform** — editing, design, web, and mobile applications layered on a GIS engine, packaging utility workflows out of the box.
- **Integrated small-utility suite** — GIS, outage management, engineering analysis, and billing from one vendor, with the GIS as the connectivity hub; common in the cooperative and municipal tier.
- **Work-execution layer** — a modern cloud platform that holds or connects to the network model and unifies field and office work around it; positions itself alongside or over the existing GIS.
- **Commodity flavors** — electric T&D, gas, water/wastewater, streetlight, and telecom extensions of the same structure, differing in plant taxonomy and flow physics.

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow, or rules in a way the core model no longer describes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Government GIS | sibling specialization of the same GIS engine | centers the jurisdiction's administrative geography (parcels, addresses, boundaries) for many departments and the public; Utility GIS centers the connected utility network for engineering, field, and operations |
| Agricultural GIS | sibling specialization of the same engine | centers farm fields and agronomic layers for growers and agronomists; Utility GIS centers the connected utility network |
| Utility Asset Management | adjacent, often coupled | holds asset records and their lifecycle (condition, work, cost, whole-life governance), consuming the GIS as location/connectivity substrate; the GIS holds the georeferenced connected model itself |
| Outage Management System / ADMS / Grid Operations | downstream consumer | derives working copies of the network model and runs real-time operational loops (outage prediction, switching, state estimation); the GIS holds the as-built model but runs no real-time operations |
| SCADA | adjacent | senses and controls live network state through telemetry; the GIS records what exists and how it connects, not the live state |
| Gas Pipeline Management | adjacent | adds the network-bound managed lifecycle (integrity, risk, hydraulic analysis, compliance programs) on top of a connected model; the model-plus-tracing layer alone is Utility GIS territory |
| Fiber Network Management / Telecom Network Design | adjacent, often built on GIS platforms | centers the fiber/telecom estate's worked lifecycle or the design act; the GIS supplies the substrate and data models; telecom-domain GIS exists as an extension of the same engine |
| Civil / Site Design | adjacent — record vs design | authors proposed works against terrain; the GIS records the as-built network; designs land in the GIS as as-built updates |
| Utility Field Service Management | adjacent consumer | holds work orders and crew capacity; the GIS provides the map/model context crews use, and receives as-built updates from field work |
| Land Records / Cadastre System | adjacent context provider | stewards the legal/ownership record of land; the utility GIS consumes parcels and addresses as reference layers, not as its record |

The family boundary worth stating plainly: Government, Utility, and Agricultural GIS share one generic engine (georeferenced layers + map canvas + spatial operations). The directory treats them as separate Types because the domain data model, the users, and the duties differ — official jurisdictional geography vs the connected utility network vs agronomic land units. This leaf's signature is connectivity: the network model records how plant joins into a traversable whole, which no other domain GIS carries as its center.

## Representative Products

- Esri ArcGIS Utility Network
- GE Vernova Smallworld GNM (Geo Network Management)
- Schneider Electric ArcFM Solution
- Milsoft WindMilMap
- IQGeo Network Manager Electric

The core model was checked across these poles — platform engine, heritage enterprise network model, solution suite on a platform, integrated small-utility suite, and modern cloud work-execution layer — so that the definition reflects the structure itself rather than one vendor's platform shape.

## Sources

Research date: **2026-09-10**

- Esri — "What is a utility network?" (ArcGIS Pro help) — https://pro.arcgis.com/en/pro-app/latest/help/data/utility-network/what-is-a-utility-network-.htm
- Esri — "Utility network vocabulary" (ArcGIS Pro help) — https://pro.arcgis.com/en/pro-app/latest/help/data/utility-network/utility-network-vocabulary.htm
- GE Vernova — Smallworld GNM product page (incl. FAQs) — https://www.gevernova.com/software/products/geospatial-network-management-smallworld-gis
- Schneider Electric — ArcFM for Utilities / ArcFM Web / ArcFM Viewer product pages — https://www.se.com/us/en/product-range/61765-arcfm-for-utilities , https://www.se.com/us/en/product-range/61755-ecostruxure-arcfm-web , https://www.se.com/us/en/product-range/61756-arcfm-viewer
- Schneider Electric — myArcFM ArcFM overview — https://myarcfm.schneider-electric.com/s/arcfm
- Esri partner listing — "ArcFM by Schneider Electric" — https://www.esri.com/partners/schneider-electric-a2T70000000TNg7EAG/arcfm-a2d70000000VGqyAAG
- Milsoft — GIS (WindMilMap) product page — https://www.milsoft.com/engineering-operations/gis-field-engineering/
- IQGeo — Network Manager Electric product page (incl. FAQs) — https://www.iqgeo.com/products/network-manager-electric

> Sourcing limitation: official operational user guides for Smallworld GNM, ArcFM, Milsoft, and IQGeo were not reachable from the research environment on 2026-09-10; their structural descriptions above rest on official product pages and FAQs (vendor self-description), while the platform-engine evidence is from official product help documentation. Claims about those vendors' internal mechanics are therefore kept generic; no precise operational figures (limits, counts, defaults) are asserted anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
