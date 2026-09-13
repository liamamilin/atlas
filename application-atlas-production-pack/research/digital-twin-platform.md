# Research Notes — Digital Twin Platform

## Research Goal

Understand what a **Digital Twin Platform** actually is as an Application Type: what objects exist inside it, how twins are modeled and kept synchronized with physical counterparts, what users do with twins, and where the boundary lies against Industrial IoT Platforms, SCADA/Historian systems, CAE/System Simulation, PLM, and BIM.

## Initial Boundary

Working hypothesis before research:

- Core purpose: maintain living digital representations of specific physical entities (devices, assets, places, processes, products) that stay synchronized with the physical world, used to monitor, analyze, predict, and act.
- Likely users: industrial/engineering/operations teams, OT/IT developers, asset owners.
- Likely nearest neighbors: Industrial IoT Platform, SCADA, Industrial Historian, CAE / System Simulation, PLM, BIM, Smart City Operations Platform, Dashboard Platform.
- Unknowns: is the twin *graph* definitional? Is 3D visualization definitional? Is sensor telemetry definitional (vs other sync sources)? Is bidirectional control definitional?

## Research Questions

1. What is a "twin" concretely in each product — what object, what identity, what state?
2. What is the model layer? Can users define reusable twin types? How?
3. How does synchronization work — what flows in, what flows out, what happens when the source is offline?
4. How do twins relate to each other (graph? hierarchy?) and is the relationship structure definitional?
5. What do consumers do with the twin space (query, visualize, subscribe, actuate)?
6. What lifecycle do twins and models have (create → update → retire)?
7. Where does this Type end and IIoT platform / simulation / BIM / dashboard begin?

## Representative Products

Selected for market representation + different product philosophy + different customer layer:

| Product | Philosophy | Customer layer | Evidence quality obtained |
|---|---|---|---|
| Microsoft Azure Digital Twins | cloud PaaS twin-graph primitive (developer builds solutions on it) | hyperscaler platform tier | Strong (official docs, 2 pages) |
| Eclipse Ditto | open-source twin middleware ("digital twin framework" — Thing/Feature/Policy, protocol bridging) | open-source / self-hosting tier | Strong (official docs, 2 pages) |
| Bentley Systems iTwin (iTwin.js / iModel) | engineering-data twin environment for infrastructure assets (iModel as synchronized asset container) | infrastructure owner/engineering tier | Strong (official open-source docs, 2 pages) |
| PTC ThingWorx | industrial IoT application-enablement platform with twin capability | industrial enterprise tier | Weak (product page only — help center unreachable) |

Coverage note: the simulation-first twin philosophy (physics/reduced-order models deployed as runtime twins fed by live data — the Ansys Twin Builder category) could not be directly researched; see Source-access Limitations. It is treated below only as a qualified market-pole observation.

## Sources

- Azure Digital Twins — Overview: https://learn.microsoft.com/en-us/azure/digital-twins/overview (fetched 2026-09-07)
- Azure Digital Twins — Digital twins and the twin graph: https://learn.microsoft.com/en-us/azure/digital-twins/concepts-twins-graph (fetched 2026-09-07)
- Eclipse Ditto — What is Eclipse Ditto: https://www.eclipse.dev/ditto/intro-overview.html (fetched 2026-09-07)
- Eclipse Ditto — Digital Twins Explained: https://www.eclipse.dev/ditto/intro-digitaltwins.html (fetched 2026-09-07)
- Bentley iTwin.js — Getting started: https://www.itwinjs.org/learning/ (fetched 2026-09-07)
- Bentley iTwin.js — iModel Overview: https://www.itwinjs.org/learning/imodels/ (fetched 2026-09-07)
- PTC — ThingWorx product page: https://www.ptc.com/en/products/thingworx (fetched 2026-09-07)

### Source-access Limitations

- **PTC ThingWorx help center** (support.ptc.com) rendered only a JS-required shell on two attempts (root and direct page). Per the network-restriction rule the source was abandoned after 2 failures. ThingWorx evidence is therefore limited to its product marketing page (positioning, capability headline groups, deployment options). Any ThingWorx structural detail beyond that is NOT claimed.
- **Ansys (simulation-first twin pole)**: ansys.com product URLs returned 404 twice. The simulation-first philosophy was abandoned as a direct source; it appears below only as a qualified market-pole note, not as observed evidence.
- **Bentley main site** (bentley.com) is login-gated; research used the publicly reachable iTwin.js open-source documentation site instead.
- No pre-IoT-era product was directly researched; the historical check is reasoning-based (recorded in Uncertainties).

## Product Observations

### Microsoft Azure Digital Twins (Layer A unless noted)

- PaaS offering: "enables the creation of twin graphs based on digital models of entire environments" — buildings, factories, farms, energy networks, railways, stadiums, "even entire cities".
- **Models**: user-defined twin types in DTDL (a JSON-like language). "DTDL models describe types of entities according to their state properties, components, and relationships." Users design model sets from scratch or adopt pre-existing industry ontologies. Example: Building / Floor / Elevator types for a building-management solution.
- **Twin instances**: "A digital twin is an instance of one of your custom-defined models." Created via APIs with a user-provided twin ID (`$dtId`), initial property values optional. Bulk import of twins/relationships via Import Jobs API.
- **Twin graph**: twins "connected to other digital twins via relationships to form a twin graph: this twin graph is the representation of your entire environment." Relationships are named edges (e.g. `contains`), with their own properties, and must be defined in the model (model-constrained). Relationship JSON: sourceId, targetId, name, properties.
- **State and provenance**: twin JSON carries per-property metadata: `lastUpdateTime` (when ADT processed the update) and optional writable `sourceTime` ("the timestamp when the property update was observed in the real world"). Properties, components (nested objects with own metadata), relationships.
- **Synchronization**: from IoT Hub-connected devices (hub-managed devices "provide the data that drives your model"); also from business systems via REST APIs and connectors (e.g. Logic Apps); an event system plus external compute (Azure Functions) processes data and drives graph updates. **Explicit differentiation**: "Digital twins in Azure Digital Twins are different from device twins in IoT Hub. IoT Hub device twins often focus on describing the aspects and capabilities of a device itself, while twins in Azure Digital Twins are more conceptual representations that can store user-defined insights about a device or many related devices."
- **Consumption**: query API over "the live execution environment" (property values, relationships, relationship properties, model information; a dedicated query language); Azure Digital Twins Explorer to "view, query, and edit your models, twins, and relationships"; 3D Scenes Studio (preview) — low-code builder mapping 3D elements to twins so "subject matter experts can monitor, diagnose, and investigate operational digital twin data with the visual context of 3D assets"; embeddable 3D viewer component.
- **Egress/historization**: data history feature historizes graph updates into Azure Data Explorer; event routes push twin data to Event Hubs/Event Grid/Service Bus → analytics, storage, workflows, custom apps.
- **Service instance**: stores models, the twin graph with its state, "orchestrates event processing."
- **Deletion**: delete APIs for twins/relationships; Delete Jobs API clears all models/twins/relationships in an instance.

### Eclipse Ditto (Layer A unless noted)

- Self-description: "an open-source framework for building digital twins in the IoT"; "Ditto mirrors real-world devices as virtual 'Things' in the cloud."
- Definitional language: "A digital twin is a virtual representation of a physical device or asset that stays synchronized with the real world." The twin "mirrors a physical asset — stores the device's current and desired state as structured JSON"; "acts as a single source of truth — applications read from and write to the twin instead of talking directly to the device"; "stays synchronized — updates flow from device to twin and from twin to device"; "enforces access control — a Policy determines who can read or modify each part of the twin."
- **Last-known state**: "When the sensor sends a new reading, Ditto updates the twin. When your dashboard queries the twin, it gets the latest value — even if the sensor is temporarily offline." Caching device state so apps can read data when a device is offline is listed as a core responsibility.
- **Model entities**: Thing (identified JSON document: thingId, attributes, features → properties), Feature (grouped functionality with definition + properties, including "desired Feature Properties" — a current/desired state distinction), Policy (first-class object governing read/write per part of the Thing), namespaces, metadata. Thing/Feature definitions can be attached (Create a Definition / Feature Definition operations; W3C WoT integration for validation of definitions).
- **Twin/live channels**: the Ditto protocol distinguishes a "Twin channel" (interaction against the managed twin state) from a "Live channel" (messages directed at the actual device). Commands, events, messages, change notifications, announcements.
- **Connectivity**: connections to messaging systems via protocol bindings (AMQP 0.9.1/1.0, MQTT 3.1.1/5, HTTP, Kafka, Eclipse Hono) with payload/header mapping to translate device payloads into twin updates.
- **Consumption**: HTTP API, WebSocket, SSE; search across twin populations (RQL query expressions); change notifications; history capability; Explorer UI; client SDKs (Java, JavaScript).
- **Scope statement (boundary evidence)**: "Ditto is **not** an end-to-end IoT platform. It does not run software on gateways or edge devices, define or implement a device communication protocol, or prescribe the data structure a device must use. Ditto focuses on the backend layer... provides web APIs so your applications can work with those devices as digital twins."
- Industrial context note (vendor's own framing): digital twins track manufactured products and assets throughout their lifecycle; concept closely related to the "Asset Administration Shell" used in Industry 4.0.

### Bentley Systems — iTwin Platform / iTwin.js / iModel (Layer A unless noted)

- iTwin.js is "the iTwin Platform's digital twin open-source JavaScript library" — APIs for web frontends/backends, services, desktop, mobile "in any context an iModel is used."
- **iModel**: "a distributed relational database, based on SQLite, with a schema defined by BIS. An iModel holds information about a single infrastructure asset." May contain physical and functional models, drawings, specifications, analytical models.
- **Identity & persistence**: every iModel has a GUID, tracked and secured by iModelHub; briefcases hold copies.
- **Spatial grounding**: every iModel has a single spatial coordinate system positioned on the earth; project extents describe the volume of interest; multiple iModels can be oriented relative to each other and to external reality models / GIS.
- **Schema system**: BIS (Base Infrastructure Schemas) — domain-specific class definitions defining properties and relationships; all information in an iModel is an instance of some BIS class; iModel contains many Models (spatial, functional, drawing...), each Model contains Elements (smallest independently addressable building block).
- **Synchronization (engineering-data pole)**: many copies of an iModel exist simultaneously, synchronized via ChangeSets from iModelHub ("helpful analogy is Git and GitHub"); change summaries capture changes; applications always work on a copy (briefcase/checkpoint/snapshot). Connectors are the documented mechanism for writing data from external sources (write-a-connector tutorials) — i.e., sync from authoring/design sources.
- **Consumption**: ECSQL query language over BIS classes/properties; display system and iTwin viewer frontends; agents/services process iModels and respond to iModelHub events.
- Note: the pages fetched document the engineering-data synchronization pole. Live sensor-telemetry binding for iTwin was not directly observed in the fetched pages (recorded in Uncertainties).

### PTC ThingWorx (Layer B- weak; product page only — positioning level)

- Self-description: "ThingWorx, the IIoT platform purpose-built to address your business challenges"; "an industrial IoT and AI platform"; "complete IIoT platform" with end-to-end capabilities.
- Headline capability groups: **Connect** (standardized industrial connectivity across devices and applications, access to multiple data sources), **Build** (pre-built tools and applications to build IIoT solutions and AR experiences), **Analyze** (real-time insights from industrial IoT data to "proactively optimize operations and prevent problems"), **Manage** (centralize device management over "connected devices, processes, and systems"), **Experience** (digital and AR interfaces that "contextualize data and guidance").
- Use cases referenced: asset optimization, service, manufacturing, factory-floor visibility, servitization ("products as a service").
- Deployment: on-premise, cloud, or hybrid.
- 2026 corporate note: ThingWorx now part of "Velotic", a new industrial software company (vendor-organizational fact, not structural).
- **Not directly observed**: Thing model structure (Thing/Template/Shape), composer tooling, twin-specific terminology. Structural claims about ThingWorx are NOT made in this research.

## Cross-product Comparison

| Dimension | Azure Digital Twins | Eclipse Ditto | Bentley iTwin | PTC ThingWorx |
|---|---|---|---|---|
| Twin unit | digital twin = instance of a DTDL model, `$dtId`, properties/components/relationships | Thing = identified JSON document with features/properties + policy | iModel = schema-governed info container for ONE infrastructure asset (BIS classes, elements) | (not directly observed) |
| Model layer | DTDL twin types; industry ontologies adoptable; model-constrained relationships | Thing/Feature definitions; W3C WoT validation; lighter-weight | BIS schema family (domain schemas) — prescribed, rich | (not directly observed) |
| Synchronization source | IoT Hub devices; business systems via REST/connectors; event compute | devices via message brokers (MQTT/AMQP/Kafka/HTTP) with payload mapping | authoring/design sources via connectors; ChangeSets sync copies | connectivity to devices and applications (positioning) |
| Offline readability | twin graph + state stored in service instance; queryable | last-known state readable "even if the sensor is temporarily offline" (explicit) | full iModel copy available offline (briefcase/snapshot) | (not directly observed) |
| Reverse direction | via event processing/compute (custom) | updates flow "from twin to device"; desired properties; live channel | not observed | (not directly observed) |
| Relationship structure | named, model-constrained relationships → twin graph = representation of the environment | not a first-class graph (population queried via search) | BIS relationships inside one asset's iModel; iModels orientable relative to each other | (not directly observed) |
| Consumption | query API + language; Explorer; 3D Scenes Studio; event routes; embeddable viewer | HTTP/WebSocket/SSE APIs; RQL search; change notifications; Explorer UI | ECSQL; iTwin viewer; agents/services | apps, AR experiences, analytics (positioning) |
| Historization | data history → Azure Data Explorer | history capability | change summaries/versions (Git-like) | (not directly observed) |
| Access control | platform RBAC (service-level) | per-Thing Policies down to parts (first-class) | iModel owner-controlled access via iModelHub | (not directly observed) |
| Deployment | PaaS | open-source, self-hosted | cloud services + open-source library; copies anywhere | on-prem / cloud / hybrid |

### Stable commonalities (Layer B — cross-product)

1. **Twin as identified persistent object** standing for a specific physical counterpart — every sampled product.
2. **Model/type layer** from which twins are instantiated (DTDL / Thing definitions / BIS / — ThingWorx unobserved but positioned as building solutions) — 3 of 4 directly observed.
3. **Synchronized state kept current from the counterpart side**, readable by applications independent of the source's connectivity — every sampled product (Ditto explicit; Azure via stored graph state; Bentley via synchronized copies).
4. **Application-facing access surface** (APIs/query/UI) against the twin space rather than device-by-device integration — every sampled product.
5. **Query/search across the twin population** — Azure query language, Ditto RQL search, Bentley ECSQL.
6. **Change notification / event propagation** — Azure event system, Ditto change notifications + events, Bentley iModelHub events.
7. **State historization / versioned change tracking** — Azure data history, Ditto history, Bentley change summaries.
8. **Access control over twin data** — Azure RBAC, Ditto policies, Bentley iModelHub owner control.
9. **Ingestion machinery with payload/source mapping** — Azure connectors + event compute, Ditto connections + payload mapping, Bentley connectors.

### Divergences (philosophy poles)

- **Graph-first vs thing-first vs asset-container-first**: Azure centers a relationship graph of typed twins; Ditto centers individual Things with per-thing policies (relationships not first-class); Bentley centers one rich per-asset container.
- **Telemetry-first vs engineering-data-first**: Azure/Ditto synchronize operational/sensor state; Bentley synchronizes engineering/design state of an asset.
- **Platform-primitive vs framework vs environment**: Azure is a cloud primitive consumed by developers; Ditto is a self-hosted middleware framework; Bentley is an environment + toolchain; ThingWorx is an app-enablement platform.

## Canonical Model (abstraction hierarchy)

### Level 0 — Defining Invariant (minimal)

A Digital Twin Platform is recognizable as such iff it provides:

1. **Twin instances** — persistent, individually identified digital objects, each standing for one specific physical counterpart (a device, asset, place, process/system, or product/population).
2. **Twin models** — a user-definable layer of reusable types that specifies what a twin of a kind carries (state properties, relationships, structure/behavior), with twins instantiated from those types.
3. **Counterpart synchronization** — the platform keeps each twin's recorded state current with its counterpart, from updates arriving on the counterpart side (sensor telemetry, operational systems, or engineering sources); at minimum the twin holds last-known state that remains readable when the source is offline; the reverse direction (desired state/commands toward the physical side) is common but not required.
4. **Twin-space access surface** — applications and users consume the twin space through platform interfaces (query, observe, subscribe to changes, modify) — working against twins rather than against each device or data source directly.

Removal tests:
- Remove (1)+(2) → bespoke digital model/simulation artifact or a data pipeline — not a twin platform.
- Remove (3) → static 3D model / data catalog / design file — not a twin.
- Remove (4) → a private model file; there is no platform.

### Level 1 — Common Mature Structure (directly observed commonality, not definitional)

- **Relationship graph** over twins (containment/network of the environment) — first-class in Azure; present inside Bentley's BIS; NOT first-class in Ditto → common but not definitional.
- **Query language / population search** (SQL-like query API, RQL, ECSQL).
- **Change events / notifications** on twin state.
- **Historization of twin state** (data history; history capability; change summaries/versions).
- **Ingestion/connectors with payload mapping** (IoT hubs, brokers, business systems, engineering files).
- **3D/scene visualization** — Azure 3D Scenes Studio, Bentley viewer; Ditto has none native → proves non-definitional.
- **Access control** scaled from roles (Azure) to per-part policies (Ditto).
- **APIs/SDKs** (REST/HTTP, WebSocket, client SDKs) and **admin tooling** (explorer/consoles).
- **Model governance**: industry ontologies (Azure), WoT validation (Ditto), domain schemas (Bentley).
- **Egress/integration** to analytics/AI/downstream systems (Azure event routes; general pattern).

### Level 2 — Variant / Optional Structure

- **Twin substrate**: graph-of-typed-twins vs JSON Things vs schema-governed asset containers vs (qualified, unobserved) physics/reduced-order simulation models as runtime twins.
- **Sync origin**: operational telemetry vs business-system data vs engineering/design sources vs mixes.
- **Direction**: monitor-only ↔ closed-loop with desired-state/commands (twin→live channel).
- **Domain flavor**: buildings, factories, farms, energy networks, railways, stadiums, cities (Azure's own list); infrastructure assets (Bentley); devices/machines/vehicles/products across lifecycle (Ditto); manufacturing/service/factory-floor (ThingWorx positioning).
- **Deployment**: PaaS / SaaS+OSS library / self-hosted OSS / on-prem-cloud-hybrid.
- **Model rigor**: open JSON vs prescriptive ontology vs heavyweight domain schema.
- **Scale**: single-asset twin → site → enterprise/city-wide populations.
- **Packaged vertical twin applications** built ON twin platforms (operations apps, AR work instructions) — adjacent enablement outcome, not the Type itself.

### Level 3 — Vendor-specific (research notes only)

- Azure: DTDL/DTMI identifiers, Azure Digital Twins Explorer, 3D Scenes Studio, data history connection to Azure Data Explorer, event routes to Event Hubs/Grid/Service Bus, Import/Delete Jobs APIs, per-property sourceTime.
- Ditto: Thing/Feature/Policy model, twin vs live channel, RQL, W3C WoT integration, Eclipse Hono binding, payload/header mapping, Java/JS SDKs.
- Bentley: iModel, BIS (Base Infrastructure Schemas), ECSQL, briefcase/checkpoint/ChangeSets, iModelHub, connectors, iTwin viewer, project extents/spatial coordinate system.
- ThingWorx: (unobserved — no structural claims recorded).

## Rejected Findings (considered, deliberately NOT definitional)

- **3D visualization** — absent natively in Ditto; rejected as definitional.
- **Twin relationship graph** — not first-class in Ditto; a single-asset twin (e.g. one machine or one asset container) is still a twin; rejected as definitional (demoted to L1).
- **IoT/sensor telemetry as the sync source** — Bentley synchronizes engineering sources; Azure ingests business systems too; rejected as definitional (the invariant is "kept current from the counterpart side", source-agnostic).
- **Bidirectional control / desired state** — present in Ditto (desired properties, live channel) but monitor-only deployments are common; rejected as definitional.
- **Per-part access policies** — Ditto-only at that granularity in the sample; kept product-specific/L1.
- **Historization** — widespread but Ditto's history and Bentley's versioning differ in kind; common-not-core.
- **"Platform = cloud PaaS"** — Ditto (OSS self-hosted) and ThingWorx (on-prem) refute; rejected.
- **Industry 4.0 Asset Administration Shell conformance** — vendor framing in Ditto docs; not required by the sample.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (with removal test) |
|---|---|---|
| Industrial IoT Platform | closest overlap (ThingWorx straddles) | IIoT centers on device connectivity, device management, telemetry pipelines; twin platform centers on the modeled representation layer bound to entities. Evidence: Azure explicitly differentiates its twins from IoT Hub device twins ("device twins... describe aspects and capabilities of a device itself; twins in ADT are more conceptual representations... about a device or many related devices"); Ditto explicitly is "not an end-to-end IoT platform" (no edge, no device protocol). Remove the twin model/state layer → IIoT platform; remove connectivity/device management → twin platform layer. |
| SCADA / HMI / Industrial Historian | adjacent (reasoning-level; not directly sampled) | deliver live process data and control screens; the twin adds identity-bound, model-defined representation of entities with relationships. Remove the modeled per-entity representation → SCADA/historian. (Qualified: inference layer C.) |
| CAE / System Simulation | adjacent | simulation models run standalone without a bound counterpart; twins persist a binding + state sync to a specific entity. Simulation-first twin products bridge the two (export a physics model as a runtime twin fed by live data) — market pole, not directly researched. Remove counterpart binding → simulation. |
| PLM | adjacent | PLM manages as-designed product data through lifecycle; twins add as-operating synchronized state. Remove live sync → PLM. |
| BIM Authoring / BIM Coordination | adjacent (Bentley bridges) | BIM authoring produces the model as a project deliverable; the twin environment keeps the asset representation synchronized and queryable over the asset's operating life (iModel + connectors + change tracking is exactly this machinery). Remove continuous synchronization/life-cycle currency → BIM authoring. |
| Smart City Operations Platform | adjacent variant host | city twin = twin-platform deployment over city data (Azure lists cities; Bentley serves cities); smart-city operations centers on city service workflows. Remove the twin representation layer → operations platform. |
| Dashboard Platform / Data Visualization | adjacent | dashboards present data; the twin platform is the identity-bound object layer beneath (model, state, sync, relationships) on which dashboards may sit. Remove the object layer → dashboard tool. |
| Enterprise Asset Registry / EAM | adjacent | registries/EAM manage asset records and maintenance business processes; twins add live synchronized state + model-defined structure. Remove synchronization → asset registry. |

## Uncertainties

- **PTC ThingWorx structure** unobserved (help center JS-walled). ThingWorx is retained as a representative product for the industrial IIoT-app-platform pole, but only positioning-level facts are used.
- **Simulation-first twin pole** (physics/reduced-order models as runtime twins) not directly researched; asserted only as a known market pole at reduced confidence.
- **Bentley live telemetry binding**: the fetched pages document engineering-data synchronization; live sensor feeding of iTwin twins was not directly observed.
- **Pre-IoT historical products** not directly researched. The historical check is therefore reasoning-based: the definition deliberately excludes cloud/3D/graph/telemetry requirements so that earlier-generation and differently-positioned implementations (e.g., the Industry 4.0 Asset Administration Shell tradition that Ditto's docs reference, per-asset state registries feeding operational apps, paired engineering-data environments) still fit; this is plausible but unverified against a specific old product.
- **Actuation prevalence**: how commonly twins drive physical commands in the market (vs monitor-only) could not be quantified from the sample.

## Final Synthesis

The Digital Twin Platform's defining core is the **twin**: a persistent, individually identified digital object instantiated from a user-definable model, bound to one specific physical counterpart and kept synchronized with it — at minimum holding last-known state readable at any time — and consumed through platform interfaces (query/observe/subscribe/modify) so that applications work against the twin space rather than against each device or source directly.

Around that core, mature products add: relationship graphs, query languages, change events, historization, ingestion machinery, access control, 3D visualization, APIs/SDKs, and egress into analytics/AI. None of these is definitional: Ditto lacks native 3D and a first-class graph, Bentley synchronizes engineering rather than sensor state, and monitor-only deployments lack the reverse direction — each still unmistakably a digital twin platform.

The Type's center of gravity is the **enablement layer** on which twin solutions are built. Where the packaged outcome (connectivity + device management) becomes the point, the product is an IIoT platform; where a standalone model without a bound counterpart is the point, it is simulation or BIM/CAD authoring; where only presentation of the data is the point, it is a dashboard.
