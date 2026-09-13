# Smart City Operations Platform

## Overview

A **Smart City Operations Platform** is a city's cross-domain operational system: it consolidates data from the city's separate systems and domains into one shared city data space, and presents a unified, real-time picture of city operating state through which city operators monitor and run the city.

The problem it exists to solve is stated almost identically across the market — by platform foundations, by cities themselves, and by the cities' own standards bodies: a city's systems are built domain by domain (traffic, energy, water, waste, environment, safety, services), and each domain's system is a silo. The platform breaks those silos by putting the city's live data in one shared place under common models, and by making the state of the whole city observable and operable from one place.

Its boundary: it is not a single-domain control system (that is a traffic management center, a utility SCADA, a building management system), not a geographic data infrastructure (that is Government GIS), not a resident-initiated request system (that is a 311 platform), not a disaster-lifecycle system (that is Emergency Management), and not a visualization layer over whatever data exists (that is BI). The defining combination is: **city-wide scope + a shared live data layer + one operational picture of the city**.

## Users & Context

The platform is operated by a city government — a municipality, a group of municipalities, or a metropolitan authority — as infrastructure for running the city day to day.

Primary users:

- **City operations staff / duty officers** — watch the city's operating picture, notice alerts and abnormal situations, and trigger or coordinate responses.
- **Department operations staff** — consume the part of the picture and the events that concern their domain, and act in their own departmental systems.
- **City IT / data teams** — connect data sources, register devices and applications, manage the shared data models, permissions, and the platform itself.

Secondary users:

- **City leadership** — consume KPI and summary views of how the city is running.
- **Application developers and integrators** — build city applications and dashboards on the platform's standard APIs (a defining practice of the open-platform segment of the market).

The work environment is an operations function: monitoring screens and dashboards showing live city state, alert queues, and maps — in smaller cities a set of browser views, in larger deployments a staffed operations center.

## Core Model

### The Defining Core

```text
The city as the managed system
└── Shared city data layer
    │   (data from many city systems and domains,
    │    under shared identity and data models)
    └── Unified operational picture
        (real-time cross-domain view of city state:
         dashboards, maps, KPIs, alerts)
```

Three properties. If any one is removed, the product is no longer recognizable as a city operations platform:

- **The city as the managed system** — the subject is the operating state of the whole city across multiple domains, not one department, one building, or one utility network. Without this, the product is a departmental system or a single-domain control room.
- **The shared city data layer** — data from heterogeneous city systems is consolidated into one addressable space: live observations, events, and commands, held under shared identity and shared data models rather than as static extracts. Without this, the product is a bundle of silos, or a generic data-integration/IoT platform.
- **The unified operational picture** — a real-time, cross-domain view of city state that city operators actually use to monitor and run the city: dashboards, maps, KPIs, alerts. Without this, the product is a data platform with no operations surface, or BI over stale data.

### What the Shared Layer Holds

Across the researched sample, the shared city data layer carries a stable set of object types:

- **Context entities** — the city's things and situations as identified, addressable records: intersections and traffic flows, parking, waste containers, air-quality points, energy readings, service points. Standardized shared data models for these entities are a first-class asset of this Type, not an implementation detail.
- **Observations** — time-stamped measurements and states flowing in from sensors, meters, cameras-as-data, departmental systems, and other city sources.
- **Alarms / alerts** — situations raised when live data violates configured rules (thresholds, changes, or other configured conditions) or when external systems raise events.
- **Orders / commands** — instructions sent back out to field devices and actuators, making the layer two-way in sensor-equipped deployments.
- **A catalog** — the registry of providers, devices, components, applications, and rules: what exists in the city's data space, who may read and write it.
- **Subscriptions** — standing requests by which applications and departments are notified of new data and events (push or polling).

### Standard Capabilities

Mature city platforms commonly add, on top of the defining core:

- **Alerting and rules engines** — validating each incoming value against configured business rules and publishing alarm events.
- **Actuation** — sending commands to field devices (where the city operates actuated infrastructure).
- **Real-time and historical processing** — the same layer serves live monitoring and historical analysis; historical export and time-series storage are common companions.
- **KPI monitoring and reporting** — aggregated views of how the city and its services are performing.
- **Open data publication** — selected city data published through standard APIs for third parties, a signature capability of this Type.
- **Departmental-system integration** — the platform's connective tissue: departmental systems feed it and consume from it; the standards work in this market explicitly frames cross-department cooperation as the goal.
- **Multi-tenancy and permissions** — departments and applications scoped to their own data, with read/write permissions managed per resource; the city-wide picture stays with the operations function.
- **Maps as a primary surface** — city state is commonly shown geographically, over the city's map base.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ on every axis:

```text
Concept:            Shared city data layer
Implementations:    open-source context-management platform with standard APIs;
                    city-built sensor/actuator platform;
                    vendor suite built around a vertical (assets, energy, safety)

Concept:            Shared data models
Implementations:    open standardized data models + standard API family;
                    proprietary models inside a vendor suite

Concept:            Unified picture
Implementations:    browser dashboards and map views;
                    staffed operations-center rooms with wall displays

Concept:            Ownership
Implementations:    open-source foundation; city-owned open source;
                    commercial vendor product
```

A reader who has only seen one implementation — say, a vendor command center with video walls — should still be able to recognize a city running on an open-source data platform with browser dashboards as the same Type.

## How It Works

### Connect the city's systems into the shared layer

```text
Identify sources (sensors, meters, departmental systems, cameras-as-data, feeds)
→ register providers/devices/applications in the catalog
→ connect each source through adapters / standard APIs
→ data lands in the shared layer as modeled entities and observations
→ permissions set: who may read and write what
```

This is the platform's founding act, and it is continuous: each new domain connected is a silo broken.

### Watch the city

```text
Live observations flow in
→ the picture updates: dashboards, map views, KPIs
→ rules run against the live data
→ violations raise alarms into alert queues
→ operators investigate on the map / entity views
```

The picture is the product's user-facing purpose: the state of the whole city, observable from one place, in real time.

### Act on what the city shows

```text
An alarm or situation is identified
→ the responsible domain is determined
→ response happens in the department's own system or channel
   (work order, dispatch, field crew) — commonly triggered through integration
→ commands to actuators where infrastructure is actuated
→ outcome flows back into the shared layer as data
```

In the open-platform segment, the platform itself stops at the shared layer, alarms, and APIs — the response loop runs in departmental systems connected to the platform. In the operations-center segment of the market, vendors package the coordination loop (tracked situations routed to departments) into the product; that posture is common in the market but was not verifiable from official documentation during research, so it is described here only as a variant, without operational detail.

### Publish and analyze

```text
Selected data published via standard APIs as open data
→ third parties build services on it
→ historical data accumulates in the layer
→ KPIs and reports inform planning and governance
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Operations dashboard / city picture

The primary monitoring surface.

- live indicators across domains, trend and status views, KPI summaries
- primary actions: watch, drill into a domain or entity, open an alert

### Map view

The geographic face of the city's state.

- live entities and events placed on the city's basemap, layers per domain
- primary actions: filter by domain/time, inspect an entity, locate an alarm

### Alert / event queues

The operational inbox.

- alarms with source, rule violated, time, location, state
- primary actions: acknowledge, investigate, hand off to the responsible domain

### Catalog / admin console

The platform's registry and control surface.

- providers, devices, components, applications, rules, users, permissions
- primary actions: register sources and apps, configure rules, manage access

### Public / open data surfaces

- public views of registered sensors and data (where the city publishes them)
- standard APIs for third-party consumption

### APIs

A first-class interface of this Type, not an add-on: city applications, departmental systems, and third-party services integrate through the platform's standard APIs.

## Important Rules / Behaviors

### The city owns its data space

The platform is the city's substrate. Data in the shared layer belongs to the city's data space under the city's terms — this is the explicit posture of both the open-source products and the cities' standards work (which frames digital sovereignty and vendor-independence as goals). Vendor lock-in avoidance is a stated design criterion of the Type, realized through open APIs and shared data models.

### Shared models are the price of admission

Data only becomes city data when it is represented in the shared models. Integration work is largely model work: mapping each source's data into the common entity vocabulary. This is what makes data from different domains comparable and applications portable across cities.

### Departmental scoping

The shared layer is city-wide, but access is scoped: departments and applications see and write their own resources; the city-wide picture belongs to the operations function. Permissions are managed per resource and per application.

### Live and historical are one continuum

The same layer serves real-time monitoring and historical analysis. Real-time storage, alerting, and historical export coexist; neither replaces the other.

### Alerts are raised by rules, resolved by people

Alarms originate from configured rules over live data (thresholds, changes, or other configured conditions) or from external events. The platform raises and routes them; the response happens in the responsible domain's own systems and channels.

### The picture is operational, not editorial

Dashboards show the city as it is — current state, not curated reports. Reporting cycles belong to governance processes that consume the platform's data, not to the picture itself.

## Variants

- **Open-platform posture** — an open-source, standards-based data platform assembled from components; the city (or its integrators) builds dashboards and applications on standard APIs. Strong in the European market, supported by cities' interoperability standards.
- **City-built posture** — a platform developed and owned by a city (or region) as open source, run as a horizontal utility for the city's sensor and actuator data, reusable by other cities.
- **Operations-center posture** — vendor-packaged command-center products that bundle the picture with coordination workflows for large-city deployments. (Official documentation for this posture was not reachable during research; described as a market variant without operational detail.)
- **Vertical-suite posture** — commercial suites that approach city operations from one vertical (asset management, energy, safety) and expand outward; the departmental asset/work-management family is adjacent rather than part of this Type.
- **Regional regimes** — standardized shared models and APIs in some regions; proprietary national platforms elsewhere. The defining structure is unaffected.
- **Deployment** — cloud-hosted or on-premises, often driven by data-sovereignty requirements.
- **Scale** — whole-city, metropolitan, or district/campus deployments of the same structure.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Government GIS | holds the city's authoritative geographic data (parcels, networks, basemaps); the operations platform holds the city's operating state over time and consumes GIS as substrate |
| 311 / Citizen Service Request Platform | unit of record is the resident-initiated request with a case lifecycle; the operations platform's subject is city operating state; 311 feeds it as one source |
| Emergency Management Platform | disaster lifecycle (preparedness/response/recovery); the operations platform is everyday operations; emergency functions may ship as a module |
| Digital Twin Platform | 3D/physics representation layer over city data; the operations platform is operational state and workflows; twin views are an optional layer |
| Industrial IoT Platform | device connectivity and data for industrial fleets; the operations platform's subject is the city and its governance picture |
| Dashboard Platform / BI | visualization and analytics over data; the operations platform includes the shared live data layer as part of the product |
| Government Performance Management | governance KPI cycles (plan→measure→report); the operations platform is live operational state; KPI views are a shared capability |
| Public Works Management / Public Asset Management | one department's assets and work orders; the operations platform is city-wide and cross-domain |
| SCADA / BMS / DCS | control of one system (a plant, a building, a network); the operations platform is the cross-system city picture above them |
| Government Open Data Portal | publication of datasets; the operations platform is live operations, of which open data is one output |
| Public Alert & Warning System | alerting the public outward; the operations platform monitors and coordinates inward |

The closest and most important boundary is with **Government GIS**: both are city-wide, both are map-centric, and they are frequently procured together. The structural difference is what they hold — GIS holds where things are; the operations platform holds how the city is running.

## Representative Products

- **FIWARE** — open-source smart-city platform framework (Context Broker, standard APIs, shared data models, component catalogue); the reference open-platform posture.
- **Sentilo** — Barcelona City Council's open-source sensor and actuator platform; the reference city-built posture, deployed by Barcelona and reused by other cities and regions.

The cities' interoperability standards (Open & Agile Smart Cities' Minimal Interoperability Mechanisms) were used as the standards-layer reference. Vendor operations-center products of the "city brain" / "intelligent operations center" family belong to the same market; their official documentation was not reachable during research and they are therefore described only as a variant posture.

## Sources

Research date: **2026-09-09**

- FIWARE — Smart Cities: https://www.fiware.org/smart-cities/
- FIWARE — Catalogue: https://fiware.org/catalogue/
- Sentilo — project home: https://www.sentilo.io/
- Sentilo — Architecture documentation: https://sentilo.readthedocs.io/en/latest/architecture.html
- Open & Agile Smart Cities & Communities — MIMs: https://oascities.org/minimal-interoperability-mechanisms/
- Trimble Unity Maintain (ex-Cityworks) — adjacent-Type evidence: https://www.cityworks.com/
- Huawei — Government industry pages (market-structure observation): https://e.huawei.com/en/industries/government
- Fujitsu — Public sector pages (market-structure observation): https://www.fujitsu.com/global/solutions/industry/public-sector/smart-city/

> Sourcing limitation: official documentation for the vendor operations-center product family (city command-center / "city brain" products) could not be accessed from the research environment — vendor pages returned errors or no longer market these products in English channels, and archived copies were unreachable. Claims about that segment are intentionally limited to its existence and general posture; no precise operational details are stated. All structural claims in this document are grounded in the reachable official sources (an open-source platform foundation, a city-owned platform, and the cities' interoperability standards body).

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
