# Research Notes — Industrial IoT Platform

## Research Goal

Understand what an **Industrial IoT Platform** really is as an Application Type: the defining structure that makes a product this Type (vs a message broker, a device inventory, a SCADA system, a historian, or a digital-twin platform), the objects users work with (devices, gateways, assets, telemetry, operations/commands, state representations), the lifecycle of a connected device on such a platform, the platform's role between OT equipment and consuming applications, and — critically — the boundaries against the neighboring §16 industrial-software Types (SCADA, HMI, Industrial Historian, Digital Twin Platform — the last carries a pre-hung forward flag for joint review with this pass) and against the horizontal IoT/security/data Types.

## Joint-review obligations carried into this pass

1. **digital-twin-platform (§16, processed 2026-09-07)** — forward flag: "device-connectivity/device-management as the packaged outcome (IIoT) vs the modeled synchronized per-entity representation layer as the packaged outcome (twin platform)"; the twin pass noted ThingWorx straddles and that Azure's own docs distinguish device twins from conceptual twins. Discharged below (Boundary Findings #1).
2. **industrial-historian (§16, processed 2026-09-08)** — boundary row: "IIoT's packaged outcome is device connectivity/device management; the historian's packaged outcome is the measurement archive of record. An IIoT platform typically *feeds* a historian." Ratified/sharpened below (Boundary Findings #2).

## Initial Boundary

Working hypothesis before research:

- Core use: connect fleets of industrial devices (machines, sensors, controllers, meters, gateways) to a central operated service; keep a registry of them; move telemetry up and commands/state down; make the fleet's data and control consumable by applications.
- Users: OT/automation engineers, IoT solution builders, operations/IT teams at industrial companies; secondarily equipment OEMs (servitization) and system integrators.
- Nearest neighbors: SCADA (control of live processes), Industrial Historian (measurement archive of record), Digital Twin Platform (modeled per-entity representation), IoT Security Platform (security lens over device estates), Agricultural IoT Platform (population-domain sibling), Event Stream Processing (data-flow subject), Message Queue Management (transport substrate), Fleet Management / Telematics (mobile-asset siblings), RMM (IT-endpoint cousin).
- Unknowns: Is device management definitional or common? Is the "industrial" population structural when the biggest platforms are population-agnostic? Is an asset/twin model layer definitional? Does the command path (write-back) belong in the core?

## Research Questions

1. What must a product hold for it to be an IIoT platform — device registry? connectivity machinery? data plane? app-enablement? management?
2. How does a device enter the platform (onboarding, identity, credentials) and how is it represented (registry record, fragments, thing, twin, managed object)?
3. How does data flow up (protocols, gateways/edge, brokers) and how far is the platform the data's home (buffer, transient relay, archive)?
4. How does action flow down (operations/commands/jobs/direct methods)? Is the command path definitional?
5. What state does the platform keep per device (last-known state, desired/reported, shadows/twins)? Is it definitional?
6. Who consumes the platform (built-in apps, custom apps, external enterprise systems) and through what surfaces (APIs, SDKs, dashboards)?
7. Which capabilities are universal vs variant: device management (OTA/config/health), asset hierarchies, alarms, analytics/AI, multi-tenancy, edge deployment, air-gapped operation?
8. What marks the "industrial" qualifier: population, protocols, or purpose — and how do population-agnostic hyperscaler services fit?
9. Where is the seam vs SCADA, vs historian, vs digital-twin platform, vs IoT security platform, vs stream processing/brokers?
10. Historical check: do pre-"IIoT"-era M2M device platforms (2000s device clouds) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation completeness, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy pole | Customer tier | Docs reached |
|---|---|---|---|
| **PTC ThingWorx** | application-enablement IIoT platform (build IIoT apps on a thing model) | enterprise ISV | Tier 2 product page; support docs JS-walled (known from digital-twin pass too) |
| **Cumulocity IoT** | device-management-and-connectivity suite with application enablement (telco/MSP heritage) | enterprise / MSP tier | Tier 1 (technical concepts + domain model) |
| **AWS IoT Core** | hyperscaler connectivity substrate (broker + registry + shadows + rules) | developers/platform builders | Tier 1 (developer guide) |
| **Azure IoT Hub** | hyperscaler message hub with device twins/direct methods + provisioning | developers/platform builders | Tier 1 (Microsoft Learn) |
| **Litmus (Edge / Edge Manager / Unify)** | edge-first industrial data platform (drivers, tags, unified namespace) | mid-market OT / manufacturers | Tier 1 (docs.litmus.io) + Tier 2 homepage |

Deliberately not sampled: **Siemens Insights Hub (ex-MindSphere)** — automation-vendor cloud pole — after two unreachable attempts (404 + transport error); recorded as a sourcing limitation. The automation-vendor pole is therefore held at market-structure strength only. GE Predix not sampled (defunct/rebranded).

## Sources

- AWS IoT Core — What is AWS IoT: https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html (fetched 2026-09-08)
- AWS IoT Core — Managing devices with AWS IoT (registry/things): https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html (fetched 2026-09-08)
- AWS IoT Device Shadow service: https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html (fetched 2026-09-08)
- AWS IoT Jobs: https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html (fetched 2026-09-08)
- Cumulocity — Introduction to the Cumulocity platform: https://cumulocity.com/docs/concepts/concepts-introduction/ (fetched 2026-09-08)
- Cumulocity — Cumulocity's domain model: https://cumulocity.com/docs/concepts/domain-model/ (fetched 2026-09-08)
- Azure IoT Hub — What is Azure IoT Hub?: https://learn.microsoft.com/en-us/azure/iot-hub/about-iot-hub (fetched 2026-09-08)
- Litmus — homepage + structured FAQ: https://litmus.io/ (fetched 2026-09-08)
- Litmus — Documentation home: https://docs.litmus.io/ (fetched 2026-09-08)
- Litmus — DeviceHub: https://docs.litmus.io/litmusedge/product-features/devicehub (fetched 2026-09-08)
- PTC — ThingWorx IIoT Platform product page: https://www.ptc.com/en/products/thingworx (fetched 2026-09-08)
- Prior-pass corroboration: digital-twin-platform (2026-09-07), industrial-historian (2026-09-08), hmi (2026-09-08), iot-security-platform (2026-09-08), factory-operations-management (2026-09-08) — recorded in STATUS.md.

---

## Product A — PTC ThingWorx (positioning-level; docs JS-walled)

Key observations (evidence layer A for what the vendor publishes; structural depth NOT observed):

- Self-labels "the IIoT platform purpose-built to address your business challenges"; market category "Industrial IoT Software / IIoT Platform" [A].
- Five published capability blocks: **Connect** ("standardized industrial connectivity across disparate devices and applications to enable access to multiple data sources"), **Build** ("pre-built tools and applications to fast-track and scale complete industrial IoT solutions and AR experiences"), **Analyze** ("real-time insights from complex industrial IoT data"), **Manage** ("assume control over connected devices, processes, and systems... Centralize Device Management"), **Experience** ("digital and AR interfaces contextualize data and guidance") [A].
- Deployment options published: on-premise, cloud, or hybrid [A].
- Use-case framing: manufacturing, service (servitization — "products as a service"), engineering [A].
- Corporate note: ThingWorx now part of Velotic, a new industrial software company (vendor fact, irrelevant to Type) [A].
- Structural internals (thing model, edge/KEPServerEX relationship, storage behavior) NOT observed — help center JS-walled this pass and in the digital-twin pass. No structural claims made from this product.

## Product B — Cumulocity IoT (Tier 1)

Key observations:

- Self-description: "a robust, secure and scalable Internet of Things (IoT) platform" with six named parts — Device integration, Device management, IoT data management, Application enablement, Analytics, Platform management [A].
- **Device integration**: pre-integrated certified gateways; thin-edge.io for custom integration; direct HTTP REST and MQTT; LwM2M and LoRa network-server support; OPC UA integration and "Cloud Fieldbus" for fieldbus protocols (CAN, Profibus, Modbus); "a common practice is to use a gateway device for data acquisition" [A].
- **Device management** (first-class, quoted feature list): device onboarding ("register and integrate any number of devices in just one go"); OTA firmware and software updates; configuration management; connection and connectivity monitoring ("identify devices that stopped communicating"); remote troubleshooting; device replacement ("replace your physical devices without losing the data history") [A].
- **Domain model** (the platform's world): *Inventory* stores "all master data related to devices, their configuration and their connections" plus "all related assets (like vehicles, machines, buildings) and their structure" — entries are **managed objects** (unique global ID, name, type, fragments like `c8y_IsDevice`); an **identity service** maps all external identifiers to one global ID so meter swaps can re-point history ("both previously collected and new meter readings are related to the correct customer"); two hierarchies — communication hierarchy (agent→gateway→devices, built by agents) and asset hierarchy (buildings→rooms etc., built by applications) [A]. *Measurements* = numeric sensor readings (value + unit fragments). *Events* = real-time information (base events / **alarms** requiring manual action with status+severity / **audit logs** for security-relevant events) [A]. *Operations* = "data that is sent to devices for execution or processing" — delivered via "a reliable queueing routine": asynchronous, because "devices are often connected over unreliable, low-bandwidth links... may, for example, only dial up once a day"; agents execute operations on their child devices and report results; operations "should always be idempotent" [A].
- **IoT data management**: canonical extensible data model decoupling device integration from applications; Data Preparation normalizes raw messages and can auto-create devices; **Digital Twin Manager (DTM)** models asset types/properties, creates "virtual representations of physical assets and their hierarchical relationships", links sensor data to the asset hierarchy; **optional DataHub** for SQL/ODBC-JDBC query and offload to data lakes [A].
- **Application enablement**: Cockpit (dashboards, reports, alarms); white-labeling; custom UI via Web SDK; custom backend microservices hosting; open REST APIs for the complete platform [A].
- **Analytics**: real-time streaming rules ("send operations back to the equipment"); ML/AI operationalization framing [A].
- **Platform management**: multi-tenancy with tenant hierarchy, RBAC, SSO, certificate-based device auth, data broker for tenant-to-tenant data sharing; SaaS cloud or on-prem **Cumulocity Edge** (single industrial PC / local Kubernetes, air-gapped networks supported); "develop once and deploy seamlessly across both cloud and edge" [A].
- M2M heritage documented in the product's own rationale: dial-up-once-a-day devices, agents owning device execution, vending machines and smart meters as canonical examples [A].

## Product C — AWS IoT Core (Tier 1)

Key observations:

- "AWS IoT provides the cloud services that connect your IoT devices to other devices and AWS cloud services" [A].
- **Message broker**: MQTT / MQTT-over-WSS / HTTPS publish-subscribe; LoRaWAN support ("replaces the need for you to develop and operate a LoRaWAN Network Server") [A].
- **Thing registry**: "a thing is a representation of a specific device or logical entity"; stored as JSON with name + attributes; "you don't need to create a thing in the registry to connect a device" (registry serves management/search); typical use is thing name = MQTT client ID; registry data usable inside rules [A].
- **Device Shadow**: "a reliable data store for devices, apps, and other cloud services to share data"; JSON document with `desired` (apps' requested state) / `reported` (device's actual state) / `delta` (difference); works while the device is offline; on reconnect "it receives the current state of its shadows so that it can update its state"; optional per thing (shadows exist only when created) [A].
- **Rules engine**: SQL-style SELECT over MQTT topics → actions (e.g., republish; by implication store/forward) [A].
- **Jobs** (device management machinery): "define a set of remote operations that can be sent to and run on one or more devices... download and install applications, run firmware updates, reboot, rotate certificates, or perform remote troubleshooting" [A].
- Console manages "thing objects, certificates, rules, jobs, policies" [A].
- Boundary evidence from the vendor itself: "If you don't require AWS IoT features such as device communications, rules, or jobs, see AWS Messaging" — the vendor's own line between message infrastructure and the IoT-platform feature set [A].

## Product D — Azure IoT Hub (Tier 1)

Key observations:

- "A managed service that acts as a central message hub in a cloud-based IoT solution. It enables reliable and secure communication at scale between an IoT application and its attached devices" [A].
- **Identity registry**: "Every IoT hub has an identity registry that stores information about the devices and modules permitted to connect to it. Before a device or module can connect, the IoT hub's identity registry must have an entry for that device or module" — SAS-token or X.509-certificate authentication; **Device Provisioning Service** for zero-touch provisioning at scale [A].
- Device realities documented by the vendor: embedded systems with no human operator, remote locations, behind firewalls, limited power, "intermittent, slow, or expensive network connectivity", industry-specific protocols [A].
- **Communication patterns**: device-to-cloud telemetry; file upload; cloud-to-device messages; **direct methods** (request-reply commands, e.g., "rebooting a device"); **device twins** for readable/writable properties (e.g., temperature as writable property) [A].
- **Data handling**: built-in endpoint retains messages "up to seven days"; **message routing** to custom endpoints (Storage, Event Hubs, Service Bus, Cosmos DB); Event Grid fan-out; integration with Stream Analytics / ML / Logic Apps [A].
- Industrial examples in the vendor's own text: refrigeration trucks, chemical plant batch reactors, wind farms, oil rigs [A].
- (Twin-pass corroboration: Azure's own docs distinguish device twins — "describe aspects and capabilities of a device itself" — from Azure Digital Twins' conceptual per-entity twins.)

## Product E — Litmus (Tier 1 docs + Tier 2 homepage)

Key observations:

- Self-label: "the modern industrial data foundation platform for AI" with six capabilities: Data Connectivity, Industrial DataOps, Edge Intelligence, Data Security, Data Governance, Central Management [A].
- **Litmus Edge**: "the industrial edge data platform for connecting industrial assets, modeling operational data, and running edge applications, analytics, and AI" — "connect PLCs and sensors, normalize tags, run flows and analytics, publish over OPC UA and MQTT" [A].
- **DeviceHub** (connectivity core, Tier 1): "Industrial devices such as PLCs store data in registers using proprietary protocols... DeviceHub is that translation layer"; device-specific drivers (Siemens, Allen Bradley, Hitachi named) over serial/Ethernet/Socketcan/file protocols; **asset discovery** (network scan); **tag browsing** and bulk tag import; scheduled polling per tag; normalization; publishes to the internal Message Broker where "any subscriber, such as a dashboard, analytics pipeline, or alerting system, can use it"; optional DataStore with retention; "Drivers form a two-way connection with PLC hardware devices" [A].
- **Digital Twins**: "Model an asset — build a Digital Twin from live tags" [A].
- **DataHub**: store and stream (topics, NATS, history); **Flows**: Node-RED flows on the edge [A].
- **Litmus Edge Manager**: "run many edges from one place: provision devices, push templates and apps, manage licences and RBAC, back up and restore"; Grafana dashboards over the fleet [A].
- **Litmus Unify**: "the MQTT broker and Unified Namespace: broker accounts and ACLs, topic hierarchy" [A].
- Developer surfaces: REST/GraphQL API (2,018 documented endpoints), Python SDK, CLI, MCP server ("turns Litmus Edge into tools an AI assistant can call: devices, tags, twins, DataHub") [A].
- Works across "legacy and modern industrial environments, including PLCs, SCADA platforms, historians, MES, cloud infrastructure"; air-gapped/offline supported; use cases: OEE, energy optimization, predictive maintenance, quality inspection, anomaly detection, digital twin [A].

---

## Cross-product Comparison

| Structure | ThingWorx | Cumulocity | AWS IoT Core | Azure IoT Hub | Litmus | Evidence |
|---|---|---|---|---|---|---|
| Persistent device population of record (registry with identity/credentials/metadata) | published as "Centralize Device Management" (positioning) | Inventory of managed objects + identity service [A] | thing registry (JSON, attributes) [A] | identity registry mandatory pre-connection [A] | DeviceHub device records + Edge Manager fleet provisioning [A] | A 4/5 (+1 positioning) |
| Gateway/agent/edge layer between platform and field devices | connectivity via partners/KEPServerEX (positioning) | gateways/thin-edge.io/agents documented [A] | Device SDKs; LoRaWAN gateways [A] | gateways for unreachable devices implied in device constraints [A] | Litmus Edge IS the edge layer [A] | A 5/5 (form varies) |
| Protocol-mediated telemetry up (MQTT/OPC UA/fieldbus/REST) | "standardized industrial connectivity" (positioning) | MQTT/REST/LwM2M/LoRa/OPC UA/fieldbus [A] | MQTT/WSS/HTTPS/LoRaWAN [A] | telemetry + file upload [A] | drivers/polling → internal broker → OPC UA/MQTT out [A] | A 4/5 (+1 positioning) |
| Command/operations path down (control/config/update) | "control over connected devices" (positioning) | Operations queue, agent-executed, idempotency guidance [A] | Jobs (firmware, reboot, certs) + shadow `desired` [A] | direct methods + device-twin writable properties [A] | two-way drivers [A] | A 4/5 (+1 positioning) |
| Per-device last-known state readable when offline | not observed | managed objects hold current fragments; lifecycle records [A] | Device Shadow (desired/reported/delta) [A] | device twins | tags/twins on edge [A] | A 4/5 (+1 positioning) |
| Management machinery: onboarding, OTA updates, config, health monitoring | "Centralize Device Management" (positioning) | full documented list [A] | Jobs + console [A] | DPS + "Device management and control" [A] | Edge Manager (provision/templates/RBAC/backup) [A] | A 4/5 (+1 positioning) |
| Event/alarm machinery | not observed | events/alarms/audit logs [A] | (rules over topics) | (routing; Event Grid) | subscribers incl. alerting systems [A] | B (strongest in Cumulocity) |
| Data normalization/contextualization + optional asset/twin model layer | thing model (positioning) | Data Preparation + DTM (asset types, hierarchies) [A] | registry attributes; shadows optional [A] | device twins; DTDL in sibling service (twin pass) | normalize tags; digital twins from tags [A] | B — present everywhere, depth and form vary |
| Built-in dashboards/apps + app-enablement surfaces (APIs/SDKs) | Build/Experience (positioning) | Cockpit + Web SDK + microservices + open APIs [A] | console + APIs/SDKs/CLI [A] | routing into Azure services | Grafana + API/SDK/CLI/MCP [A] | A/B |
| Rules/integration pipelines to storage/analytics/business systems | Analyze (positioning) | smart rules + streaming analytics [A] | rules engine [A] | message routing + Event Grid [A] | broker subscribers/flows [A] | A 4/5 |
| Security machinery (per-device credentials, certs, RBAC, tenancy) | not observed | certs, RBAC, SSO, multi-tenancy [A] | certificates + policies [A] | SAS/X.509 + registry [A] | RBAC, ACLs (Unify) [A] | A 4/5 |
| Edge/on-prem/air-gapped deployment variant | on-prem/cloud/hybrid (positioning) | Cumulocity Edge, air-gapped [A] | (edge via sibling service, not asserted) | (not asserted) | edge-first by design, air-gapped [A] | B |
| Raw device data as transient relay, long-term storage delegated | not observed | DataHub offload optional [A] | rules → other services [A] | built-in endpoint retention bounded ("up to seven days") + routing [A] | optional DataStore retention [A] | A 4/5 |
| Industrial population vs population-agnostic | industrial (manufacturing/service) [A] | "simple sensors to complex machinery", industrial protocols [A] | any device ("a light bulb or a switch") [A] | any device, industrial examples throughout [A] | industrial only [A] | mixed — see L0 note |

**Reading**: three structures appear in every sampled product with direct evidence or explicit positioning — (1) a persistent device population of record, (2) platform-operated two-way connectivity (telemetry up + operations down, gateway/agent-mediated, built for unattended intermittently-connected devices), (3) a platform consumption surface that decouples applications from devices (APIs, apps, rules/integration). Everything else — management application depth, state documents/twins, alarms, asset models, analytics, tenancy, edge packaging — varies in form and packaging while remaining near-universal in presence.

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

Three structures held jointly:

1. **The connected-device population of record.** The platform maintains a persistent registry of the attached devices — each an individually identified record carrying credentials, metadata, and connection state, with gateways/parent assets commonly represented alongside. Devices join the population through onboarding/registration machinery. (Remove → message broker / telemetry pipeline with no device subject; a device inventory without connectivity is an asset register, not this Type.)
2. **Platform-operated two-way connectivity at fleet scale.** The platform itself operates the network-facing machinery — protocol endpoints, message brokering, agent/gateway/driver interfaces — through which devices stream telemetry into the platform and through which operations (commands, configuration, updates, state changes) are delivered back to devices; engineered for unattended devices with intermittent, constrained, firewalled connectivity. (Remove the up-path → a management console with no data; remove the down-path → a telemetry collector; remove platform operation of the transport → point-to-point integrations.)
3. **The fleet as a platform resource for consumers.** Device data and device action are exposed through platform surfaces — APIs, built-in applications, rules/integration pipelines, app-enablement tooling — so consuming applications work against the device population (and its normalized data) rather than integrating device-by-device; the platform decouples applications from device and protocol specifics. (Remove → a connectivity gateway or management appliance with a private link; a single-site SCADA/HMI system.)

**Population scope**: the canonical population is devices and assets of industrial and commercial operations — machines, production equipment, sensors, controllers, meters, gateways, vehicles and field equipment — connected for operational purposes (monitoring, management, optimization, servicing). Population-agnostic hyperscaler services are in-market poles of the same structure deployed under industrial populations (Azure's own examples: chemical-plant reactors, refrigeration trucks, wind farms); the industrial qualifier distinguishes the leaf from consumer/smart-home IoT platforms, not a protocol or architecture.

**Jointly-held is load-bearing**:
- 1 without 2+3 = device inventory / asset register
- 2 without 1 = message broker / data pipeline (AWS's own AWS-Messaging cross-reference marks this line from the vendor side)
- 3 without 1+2 = application suite with no device substrate
- 1+2 without 3 = device-management / connectivity appliance, not a platform
- 1+3 without 2 = catalog with apps but no live fleet

### Level 1 — Common Mature Structure

- Device management machinery: bulk onboarding/provisioning, OTA firmware/software updates, configuration management, connection/health monitoring, remote troubleshooting, device replacement preserving data history (packaging varies: embedded application vs sibling services).
- Per-device state representation: last-known/desired/reported state documents (shadows/twins/managed-object fragments) readable and writable while the device is offline.
- Event/alarm/audit machinery over the device fleet.
- Data normalization/contextualization: raw payloads → platform data model; optional asset hierarchies and asset/twin model layers.
- Rules and integration pipelines: route device data to storage, analytics, and business systems; trigger workflows; send operations back.
- Built-in applications (dashboards, device-management console) plus app-enablement surfaces: open APIs, SDKs, CLIs, extensibility/microservice hosting.
- Security machinery: per-device credentials/certificates, policies/RBAC, SSO, multi-tenancy.
- Edge variant: edge runtimes/gateway software carrying connectivity, buffering, and processing on site; cloud/edge symmetric deployment; air-gapped support.

### Level 2 — Variant / Optional Structure

- Architecture philosophy: hyperscaler connectivity substrate (primitives composed by builders) vs packaged device-management suite vs application-enablement platform vs edge-first data platform / unified-namespace packaging.
- Deployment: SaaS cloud / on-premises / edge / hybrid / air-gapped.
- Asset-model depth: none (registry + attributes only) → per-device state documents → optional asset/twin manager → asset-model-first packaging.
- Protocol strategy: IoT messaging protocols (MQTT/LwM2M/LoRaWAN) vs industrial fieldbus/PLC drivers (OPC UA, Modbus, Profibus, vendor protocols) vs both.
- Population emphasis: industrial equipment/machinery (canonical) vs population-agnostic infrastructure services.
- Consumer: enterprise OT organizations, OEM servitization programs, MSP/telco resellers, developer platforms.
- Era packaging: the 2000s M2M device-cloud generation satisfies the core; cloud, MQTT, edge, digital twins, AI, unified namespaces are era machinery.

### Level 3 — Vendor-specific (research notes only)

- Cumulocity: managed objects/fragments, identity service, communication vs asset hierarchies, Cockpit, Cumulocity Edge, data broker.
- AWS: thing registry/shadow desired-reported-delta mechanics, Jobs, rules SQL, LoRaWAN network server.
- Azure: identity registry pre-connection requirement, direct methods, Device Provisioning Service, device twins vs Digital Twins split, seven-day built-in endpoint retention.
- Litmus: DeviceHub drivers/tag model, internal message broker + DataHub, Node-RED flows, Unify unified namespace, MCP server.
- PTC: Velotic corporate move; Connect/Build/Analyze/Manage/Experience marketing blocks.

## Rejected Findings (considered, deliberately NOT definitional)

- **"Device management application (OTA/config/health consoles) is definitional"** — rejected at strict level: near-universal, but packaging varies (AWS splits management across sibling services; registry exists for management/search and connection does not require a thing record), so the *capability substrate* (two-way connectivity, leg 2) is the invariant, the management application is L1.
- **"Asset/twin model layer is definitional"** — rejected: AWS registry carries plain attributes and shadows are strictly optional; Cumulocity's DTM is an additional offering; Litmus twins are one modeling surface among flows/tags. An IIoT platform operates without a user-defined asset model. (This is also the twin-platform seam — see Boundary #1.)
- **"MQTT/cloud is definitional"** — rejected: protocols vary (REST, LwM2M, LoRaWAN, fieldbus, proprietary PLC drivers); the M2M dial-up heritage is documented inside a current product's own rationale.
- **"Industrial protocols (OPC UA/fieldbus) are definitional"** — rejected: hyperscaler poles carry none natively; the fieldbus depth is a variant strategy.
- **"Built-in dashboards/analytics/AI are definitional"** — rejected: present in most, but the platform's defining role is enabling consumption, not performing it.
- **"Edge/gateway machinery is definitional"** — rejected as a separate leg: gateways/agents are the *form* the connectivity layer takes in industrial deployments (A 5/5 in varying degrees) but the invariant is platform-operated connectivity, however realized.
- **"Multi-tenancy is definitional"** — rejected: MSP/telco-heritage product emphasizes it; not structural.
- **"Population-agnostic scope disqualifies a product from the Type"** — rejected: hyperscaler poles are in-market realizations deployed under industrial populations; the qualifier marks the canonical population.

## Boundary Findings

| Neighboring Type | Relationship | Discriminator (what to remove/add to cross the seam) |
|---|---|---|
| **Digital Twin Platform** (§16, processed) — JOINT REVIEW DISCHARGED | closest overlap; straddling poles documented (twin pass: ThingWorx; this pass: Cumulocity DTM, Litmus twins, AWS shadows, Azure device twins) | Ratified with sharpening: IIoT's packaged outcome = the connected device fleet as managed, consumable resource (registry + connectivity + data access); twin platform's packaged outcome = the modeled, synchronized per-entity representation layer (user-definable types, twin graph/space, sync semantics) as the product's center. Evidence from this pass: the model layer inside IIoT platforms is optional and subordinate — Cumulocity's DTM is an additional offering, AWS shadows are explicitly optional per thing, registry-only operation is documented; Azure's own docs split device twins (device aspects) from conceptual twins. Remove the twin model/state layer → IIoT platform still stands (AWS registry-only, Cumulocity without DTM); remove connectivity/device-management/fleet machinery → twin platform layer. Keep-both. |
| **Industrial Historian** (§16, processed) — forward note RATIFIED | adjacent, feeder relationship | Historian = archival system of record for process measurements (high-density engine + time-range replay). IIoT platform = fleet connectivity/management/data access; its message/data layer is transient or buffered by default (Azure built-in endpoint retention bounded; optional DataStore retention in Litmus; offload-to-data-lake as separate machinery in Cumulocity DataHub) and typically feeds historians/data lakes. Remove the fleet/management/connectivity machinery → historian; remove the archive-of-record purpose → IIoT platform. |
| **SCADA** (§16, unprocessed) | adjacent | SCADA = supervisory control of live distributed processes (control-room loop, process write-back, per-site topology). IIoT platform = fleet-scale connectivity/management/data enablement across sites; process control is not the platform's defining duty — operations reach devices asynchronously through agents/gateways (Cumulocity's own rationale: async queueing, dial-up devices; no live supervisory-control semantics anywhere in-sample). Remove fleet-scale device population + app enablement → SCADA components; remove live-process supervision/control → IIoT platform. Qualified: SCADA pass unprocessed; the hmi pass's HMI↔SCADA flag remains open and is NOT discharged here. |
| **HMI** (§16, processed) | adjacent | HMI = engineered operator screens + live tag layer + operator write-back (per HMI pass). The IIoT platform supplies fleet data/connectivity upstream of any operator surface; no engineered screen core. |
| **IoT Security Platform** (§15, processed) | different lens, same estates | Security platform assembles the device population by network-side observation for security assessment/alerting; the IIoT platform enrolls/operates the population for connectivity/data/management. Different users (security vs OT/IT/IoT builders), different record origin (observed vs enrolled). |
| **Agricultural IoT Platform** (§20, unprocessed) | population-domain sibling | Expected same structural core (device registry + connectivity + management + consumption) with farm/crop/livestock population and agronomy semantics. Flag for that pass (see also environmental-monitoring pass's Campbell Scientific straddle note). |
| **Fleet Management System / Vehicle Telematics** (§18) | population sibling, application layer on top | Telematics connectivity spine is this Type's structure applied to vehicles; the fleet-management Type carries dispatch/route/driver/compliance/ELD semantics on top. |
| **Event Stream Processing / Stream Analytics Platform** (§13) | adjacent, downstream | ESP's subject = event flows and their computation; IIoT platform's subject = the device fleet. IIoT platforms commonly *route into* stream processing (Azure routing; Cumulocity streaming analytics). Remove the device registry/management → data-plane machinery. |
| **Message Queue / Broker Management** (§14) | substrate seam | A broker holds transport state only — no device population of record, no fleet management, no device-shaped data model. AWS's own AWS-Messaging cross-reference ("if you don't require device communications, rules, or jobs, see AWS Messaging") documents the vendor-side line. |
| **RMM / Endpoint Management** (§14) | structural cousin, different population | Same register-monitor-manage shape over IT endpoints (agent-enrolled desktops/servers); population, protocol world, and semantics (patching/end-user computing) differ from industrial devices. |
| **MOM / factory-operations-management, MES** (§16, processed/unprocessed) | consumers | Production-operations applications consume fleet data as one input; they own production orders, execution enforcement, performance records — not the device population or connectivity machinery. |
| **Building Management System** (§17) | population-domain sibling (buildings) | Control-system Type over building plant; adjacent pattern like the agricultural sibling. |
| **Smart City Operations Platform** (§24, unprocessed) | adjacent | City service workflows vs device-fleet platform; a city twin/IIoT substrate may underlie it (twin pass already noted the seam). |

## Uncertainties

1. **Siemens Insights Hub (automation-vendor cloud pole) unreachable** — 404 + transport error. The automation-vendor packaging pole (platform sold beside PLC/SCADA estates) rests on market-structure knowledge and is NOT evidenced first-hand this pass; no Siemens-specific claims made.
2. **PTC ThingWorx internals unobserved** (support docs JS-walled, same as digital-twin pass) — ThingWorx claims held at positioning level; the app-enablement pole's structural depth rests on Cumulocity/Litmus Tier-1 evidence plus ThingWorx positioning.
3. **AWS edge sibling (Greengrass) and Azure DPS details** not separately fetched; provisioning-at-scale and edge machinery asserted only where the fetched pages document them.
4. **Device management as "standard-not-definitional"** rests on 4/5 direct evidence + 1 positioning; a pole with literally zero command path was not found in the sample (all sampled products document some down-path) — the two-way nature of leg 2 is solid, but the exact market share of management-application depth is unquantified (deliberately no percentages asserted).
5. **Pre-2013 M2M device clouds not directly researched** — historical check is reasoning-based, strengthened by Cumulocity's own documentation of dial-up-era constraints and vending/meter examples inside a current Tier-1 doc. No specific legacy product is claimed.
6. **Corporate flux in the category** (Software AG ownership questions around Cumulocity, PTC→Velotic) noted only where vendor pages state it; no market-size or vendor-ownership assertions.

## Final Synthesis

An **Industrial IoT Platform** is the platform Type that turns a fleet of industrial devices into an operated, consumable resource. Its defining structure is three jointly-held legs: (1) a persistent **device population of record** — identified device/gateway/asset records with credentials, metadata, and state, entered through onboarding machinery; (2) **platform-operated two-way connectivity at fleet scale** — protocol endpoints/brokers/agents through which devices stream telemetry up and receive operations down, engineered for unattended, intermittently connected, firewalled equipment; (3) **the fleet as a platform resource** — data and device action exposed through APIs, built-in apps, and integration pipelines so applications consume the population instead of integrating device-by-device. Around this core, mature products standardly add device-management machinery (provisioning, OTA updates, configuration, health monitoring, replacement-with-history), per-device state representations readable while offline, event/alarm machinery, data normalization with optional asset/twin model layers, rules/routing into storage and analytics, app-enablement SDKs, security machinery, and edge/air-gapped deployment variants. The definition names no protocol, no cloud, no edge, no twin model, no AI — the 2000s M2M device-cloud generation satisfies it. The load-bearing seams: vs message brokers (no device population), vs device inventories/security platforms (no operated connectivity), vs SCADA/HMI (no live-process supervision/control loop), vs historians (no archival system of record — IIoT feeds historians), and vs digital-twin platforms (the twin model layer is optional/subordinate here, packaged there).
