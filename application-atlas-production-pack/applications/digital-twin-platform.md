# Digital Twin Platform

## Overview

A **Digital Twin Platform** is a platform for creating and operating **digital twins**: persistent, individually identified digital objects, each standing for one specific physical counterpart — a device, machine, building, infrastructure asset, process, vehicle fleet, or population of products — instantiated from user-definable models and kept synchronized with that counterpart's state.

The defining structure is deliberately small:

```text
Twin model (reusable type of a physical kind)
└── Twin instance (persistent, identified digital object
    standing for one specific counterpart)
    └── Synchronized state (kept current from the counterpart side;
        readable even when the source is offline)
        └── Twin-space access (applications query, observe, and modify
            twins instead of integrating against each device or source)
```

Everything else commonly associated with the category — relationship graphs, 3D scene visualization, query languages, historization, AI-driven prediction, closed-loop control — is widespread in current products but is not what makes a platform a digital twin platform.

The boundary matters because this Type sits under several larger categories. When the packaged outcome is device connectivity and fleet management, the product is an **Industrial IoT Platform**. When the artifact is a standalone computational model with no bound counterpart, it is **simulation or CAD/BIM authoring**. When the artifact is a presentation of data, it is a **dashboard**. The digital twin platform is the layer that gives each physical entity a modeled, synchronized, addressable digital presence that other software can be built against.

## Users & Context

Two populations work with the platform, usually in the same deployment:

**Builders** create and maintain the twin environment:

- OT/IT developers and solution engineers define twin models, connect data sources, and build integrations
- data engineers wire telemetry, business systems, or engineering sources into twin state

**Consumers** use the twin space to do their work:

- operations and process engineers monitor current conditions and investigate anomalies in their physical context
- reliability and maintenance engineers examine the operating state of specific assets
- facility, plant, and asset managers oversee sites and asset populations as a whole
- analysts feed twin data into analytics and planning

Typical environments: manufacturing plants and production lines, energy networks and utilities, buildings and campuses, infrastructure such as railways and roads, urban systems, and fleets of connected products in the field. A deployment usually mirrors one organization's real environment and builds on connectivity or data investments that already exist.

## Core Model

### The defining core

Four properties. If any one is removed, the product is no longer recognizable as a digital twin platform:

- **Twin instances** — a twin is a persistent digital object that stands for one specific physical counterpart. It has an identity of its own, survives sessions and restarts, and remains distinct from every other twin. Without per-entity twins, there is no twin — only aggregated data.
- **Twin models** — the platform lets users define reusable types that specify what a twin of a kind carries: its state properties, its relationships, and in some approaches its structure or behavior. Twins are instantiated from these types, so a hundred buildings or a thousand pumps share a vocabulary while each keeping individual state. Without a model layer, the product is a bespoke one-off model rather than a platform.
- **Counterpart synchronization** — the platform keeps each twin's recorded state current with its real-world counterpart, from updates arriving on the counterpart side. The updates may be sensor telemetry, messages from operational systems, or synchronized engineering data — the invariant is that the twin tracks its counterpart, at minimum holding the last-known state, readable at any time even when the source is offline. Without synchronization, the object is just a static model or a data record.
- **Twin-space access** — applications and users work against the twin space through platform interfaces: reading and writing state, traversing relationships, subscribing to changes. The twin, not each individual device or data source, is the object that software integrates against. This is what makes the platform an enablement layer rather than a private file.

### What mature products add

These capabilities are common in current products and expected in serious deployments, but removing any one of them still leaves a recognizable digital twin platform:

- **Relationship graph** — twins connected by named relationships (contains, feeds, located-in) so the graph mirrors the structure of the physical environment. Some platforms make this graph the central representation of the whole environment; others treat twins as independent individuals and leave population structure to search.
- **Query and search** — a query language or search facility over the twin population: by model type, property values, relationships, or model metadata.
- **Change events** — notifications emitted when twin state changes, so downstream applications react to the physical world in near real time.
- **Historization** — a retained history of twin state or of changes, enabling trend analysis and after-the-fact investigation.
- **Ingestion machinery** — connections to IoT hubs, message brokers, business systems, or file-based engineering sources, usually with mapping that translates raw payloads into twin state.
- **3D and spatial visualization** — rendering twins in the visual context of their real environment so subject-matter experts can monitor and diagnose in place. Notably, several mature platforms operate entirely without it, which is why it is not definitional.
- **Access control** — roles or policies governing who may read or modify twin data, in some products down to individual state properties.
- **APIs and SDKs** — programmatic surfaces (REST/HTTP, WebSocket, client libraries) through which applications consume the twin space.
- **Model governance** — industry-standard vocabularies or validation schemes that models can adopt or be checked against.
- **Egress into analytics and AI** — routing twin data and graph updates into analytics stores, machine learning, and enterprise systems for prediction and optimization.

### One structure, many implementations

The core model is conceptual. Current products realize each concept differently:

```text
Concept:            Twin model
Implementations:    ontology-style twin type languages (properties, components,
                    relationships); lightweight JSON thing definitions with
                    optional validation schemas; heavyweight schema-governed
                    engineering data classes for a single asset

Concept:            Twin instance identity
Implementations:    platform-assigned or user-chosen identifiers, each bound
                    to one counterpart

Concept:            Synchronization source
Implementations:    device telemetry via IoT hubs and message brokers;
                    business systems via connectors and APIs; engineering
                    and design sources via file connectors

Concept:            Twin-space access
Implementations:    REST APIs plus query languages; graph explorers;
                    3D scene viewers; event streams
```

A reader who has only seen one style — for example, a 3D-rendered city twin — should still be able to recognize a plain JSON-state twin middleware or a synchronized engineering-data environment as the same Application Type.

## How It Works

The work of a digital twin platform is a recurring loop from the physical world into the digital twin space and back:

### 1. Define the model

```text
Choose or author twin types for the domain
→ specify state properties, relationships (and where applicable structure/behavior)
→ optionally adopt an industry vocabulary or validation scheme
```

This is a design-time activity performed by builders. Models express the organization's own vocabulary for its environment — the kinds of things that exist in a plant, a network, or a city, and what is worth knowing about each.

### 2. Instantiate twins

```text
Create a twin from a model type
→ give it an identity
→ initialize state properties as needed
→ connect it to other twins through model-defined relationships
```

A twin is created for each specific counterpart — one per building, pump, vehicle, or room. Creation can be one at a time through APIs or in bulk when standing up a whole environment.

### 3. Connect and synchronize

```text
Connect sources (devices, systems, engineering files)
→ map incoming payloads onto twin properties
→ platform updates twin state as updates arrive
→ twin state remains available to consumers regardless of source connectivity
```

Synchronization is the platform's heartbeat. Updates flow from the counterpart side into twin state; in products that support the reverse direction, desired values or commands written to the twin flow outward toward the physical side. Mapping between raw source data and modeled twin state ranges from declarative configuration to custom code, depending on the product and the source.

### 4. Consume the twin space

```text
Query twins by type, property, or relationship
→ observe live state and subscribe to changes
→ visualize in graphs, lists, or 3D scenes
→ feed twin data into analytics, AI models, and downstream systems
```

This is where consumers spend their time: answering questions about the current and historical condition of the environment, investigating anomalies in physical context, and supplying twin state to prediction and optimization.

### 5. Act on the physical world (where supported)

```text
Write a desired state or command to a twin
→ platform routes it toward the counterpart side
→ outcome reflected back as new observed state
```

Some deployments are monitor-and-analyze only; others close the loop from twin back to the physical world. Both are common postures of the same Type.

### 6. Maintain and retire

```text
Update models as the domain vocabulary evolves
→ add twins for new counterparts, update relationships as reality changes
→ retain or archive twin history
→ delete twins whose counterparts are retired
```

The twin population tracks reality over time. Twins outlive their sources' connectivity but not, in the long run, their counterparts.

### Tiers of capability

**Defining core** — without these, not a digital twin platform:

- persistent, identified twin instances standing for specific counterparts
- user-definable twin models from which twins are instantiated
- synchronization of twin state from the counterpart side, with last-known state readable at any time
- a platform access surface against the twin space

**Standard capabilities** — present in most mature products:

- relationship graph, query/search, change events, historization, ingestion machinery, access control, APIs/SDKs, 3D or spatial visualization, egress into analytics/AI

**Variant / optional** — depends on segment and posture:

- closed-loop command toward the physical side
- industry-standard vocabularies and conformance
- physics- or simulation-based twin behavior (a recognized market pole in which a computational model of the counterpart runs alongside, or as, the twin)
- packaged vertical applications built on top of the platform

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Modeling surface

Where builders author twin types.

- typical information: type names, property definitions, relationship definitions
- primary actions: create and edit types, adopt or import vocabularies, validate models

### Twin explorer / graph view

Where the twin population is seen and managed as a whole.

- typical information: twins as nodes with model type and key state, relationships as named edges, search and filter results
- primary actions: create/edit/delete twins and relationships, edit models, run queries, inspect state

### 3D scene / spatial viewer

Where twins are monitored in the visual context of their environment.

- typical information: rendered environment with elements mapped to twins, live property values displayed in place
- primary actions: navigate, select a twin to inspect state, monitor and diagnose in context; in some products, build such scenes without code

### Query / API console

Where developers and analysts work against the twin space programmatically.

- typical information: query results over twins, relationships, properties, and model metadata
- primary actions: run queries, call APIs to read/write state, subscribe to change events

### Connection configuration

Where synchronization is set up.

- typical information: connected sources, protocols, mapping between raw payloads and twin properties
- primary actions: create/edit connections, define payload mappings, monitor ingestion

### Administration

Where governance lives.

- typical information: users and roles, access policies, deployment settings
- primary actions: grant/revoke access, configure policies, manage the deployment

### Operational dashboards and apps

Built on top of the platform rather than part of its core: role-specific views over twin state, and in some ecosystems packaged applications (operations monitoring, field work) that consume the twin space.

## Important Rules / Behaviors

- **Twins conform to their models.** What a twin can carry — properties, relationships — is defined by its type. Relationships, where modeled, are model-constrained: a relationship can only connect twins of types the model permits.
- **Twin state outlives source connectivity.** A twin holds its last-known state and serves it to consumers even while its device or source is offline. This cached-state behavior is a defining practical property of the Type, not an optimization detail.
- **Identity is per counterpart.** Each twin is individually addressable. Software refers to "that specific pump" or "that specific building" through the twin's identity, not through a query against an undifferentiated data stream.
- **Synchronization carries provenance.** Twin state commonly records when each property was updated; some platforms additionally distinguish when a value was processed by the platform from when it was observed in the real world.
- **Current and desired state can be distinct.** In products that support actuation, a twin may hold both the last-observed state of the counterpart and the state desired for it, with synchronization reconciling the two.
- **Access control attaches to twins.** Who may read or modify twin data is governed at platform level and, in some products, per twin or per state property.
- **Changes propagate as events.** Twin state changes are observable by other software, which is how the twin space functions as a living integration layer rather than a static record.
- **The population tracks reality.** Twins are created, updated, and deleted as the physical environment changes; deletion may be individual or in bulk.

## Variants

- **Twin substrate philosophy.** Graph-of-typed-twins platforms (an environment represented as a connected graph of model instances); lightweight thing-middleware frameworks (identified digital objects with policies, focused on state and access rather than graphs); engineering-data twin environments (one rich, schema-governed synchronized container per infrastructure asset); simulation-first approaches (a physics or data-driven model of the counterpart operating as the twin, fed by live data). These are genuinely different engineering cultures producing the same recognizable Type.
- **Synchronization origin.** Sensor-telemetry-first (operational state), business-system-first (records and context), engineering-source-first (design and as-built state), or mixes.
- **Direction.** Monitor-and-analyze only, versus closed-loop with commands or desired state flowing back to the physical side.
- **Domain flavor.** Manufacturing plants, energy networks, buildings and campuses, infrastructure, urban systems, connected products in the field. The substrate is the same; the models, vocabularies, and integrations differ.
- **Deployment and delivery.** Cloud platform services, vendor SaaS environments, self-hosted open-source frameworks, on-premise and hybrid deployments.
- **Scale.** A single critical asset twinned in depth, up to enterprise- or city-wide populations of many thousands of twins.
- **Platform versus packaged application.** This Type is the enablement layer. Vertical twin applications (a specific product's monitoring app, an AR work-instruction tool) are outcomes built on this layer or adjacent products in their own right.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Industrial IoT Platform | centers on device connectivity, device management, and telemetry pipelines; the twin platform centers on the modeled, synchronized representation layer bound to entities. Remove the twin model and per-entity state → IIoT platform; remove connectivity machinery → twin platform layer. Mature IIoT products increasingly carry twin capability, so real products straddle the line. |
| SCADA / HMI / Industrial Historian | deliver live process data, control screens, and data archives; the twin platform adds identity-bound, model-defined representations of entities and their relationships. Remove per-entity modeled representation → SCADA/historian. |
| CAE / System Simulation | produces computational models that run standalone against scenarios; a twin persists a binding and state synchronization to one specific real counterpart. Remove the bound counterpart → simulation. Simulation-first twin products bridge the two. |
| Product Lifecycle Management / PLM | manages as-designed product data across the lifecycle; the twin adds the as-operating, synchronized state of deployed entities. Remove live synchronization → PLM. |
| BIM Authoring / BIM Coordination | produces and coordinates building models as project deliverables; the twin environment keeps an asset's representation synchronized and queryable across its operating life. Remove continuous synchronization beyond the project → BIM authoring. |
| Smart City Operations Platform | centers on city service operations and workflows; a city twin is a twin-platform deployment over city systems' data. Remove the twin representation layer → operations platform. |
| Dashboard Platform | presents data for human viewing; the twin platform is the identity-bound object layer beneath — model, per-entity state, synchronization — on which dashboards may sit. Remove the object layer → dashboard tool. |
| Enterprise Asset Registry / EAM | maintains asset records and maintenance business processes; the twin adds live synchronized state and model-defined structure. Remove synchronization → asset registry. |

The most important boundary is with the **Industrial IoT Platform**, because the two overlap heavily in current products. The cleanest structural test: an IIoT platform can be described entirely in terms of devices, connectivity, and data; a digital twin platform cannot — it requires modeled entities that stand for specific physical counterparts.

## Representative Products

- Microsoft Azure Digital Twins — cloud PaaS twin-graph primitive
- PTC ThingWorx — industrial IoT application platform with twin capability
- Bentley Systems iTwin Platform (iTwin.js / iModel) — engineering-data twin environment for infrastructure assets
- Eclipse Ditto — open-source digital twin middleware

These were chosen to span the category's main philosophies and customer layers: cloud platform primitive, industrial application-enablement platform, infrastructure owner/engineering environment, and open-source self-hosted middleware. Other major market categories — comprehensive industrial-suite twin portfolios and simulation-first twin products — were not directly researched for this document.

## Sources

Research date: **2026-09-07**

- Microsoft — Azure Digital Twins documentation: overview and "Digital twins and the twin graph" — https://learn.microsoft.com/en-us/azure/digital-twins/overview , https://learn.microsoft.com/en-us/azure/digital-twins/concepts-twins-graph
- Eclipse Ditto documentation: "What is Eclipse Ditto" and "Digital Twins Explained" — https://www.eclipse.dev/ditto/intro-overview.html , https://www.eclipse.dev/ditto/intro-digitaltwins.html
- Bentley Systems — iTwin.js documentation: "Getting started" and "iModel Overview" — https://www.itwinjs.org/learning/ , https://www.itwinjs.org/learning/imodels/
- PTC — ThingWorx product page — https://www.ptc.com/en/products/thingworx

> Sourcing limitations: the PTC help center could not be fetched from the research environment (JavaScript-required pages), so ThingWorx is represented at product-page (positioning) level only, and no structural detail of that product is asserted. Simulation-first twin products could not be reached and are described only as a market pole without specific claims. Assertions in this document are calibrated accordingly: the defining core and the "standard capabilities" list rest on the three products with full documentation access, cross-checked for commonality.
