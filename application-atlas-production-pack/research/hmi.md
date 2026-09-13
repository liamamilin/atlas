# Research Notes — HMI (Human-Machine Interface)

## Research Goal

Understand the industrial HMI software Type as it exists in the market: what an HMI application consists of, how screens are engineered and run, how operator data acquisition and control actually work, how the alarm loop behaves, and where the boundary to SCADA, dashboards, and programming environments lies.

## Initial Boundary

Initial hypothesis before research:

- HMI = operator-facing visualization software for machines and industrial processes: graphical screens bound to live data from controllers (PLCs), operator write-back (setpoints/commands), alarm annunciation.
- Nearest neighbors in DIRECTORY.md §16: SCADA (previous leaf), Industrial Historian, Distributed Control System / DCS, PLC Programming Environment, Industrial IoT Platform, Digital Twin Platform. Also adjacent outside §16: Dashboard Platform (§13).
- Known market hazard: products self-label "HMI", "HMI/SCADA", or "visualization software" interchangeably; the same vendor often sells HMI and SCADA as separate product lines. This needs an explicit boundary finding.

## Research Questions

1. What is the unit of live process data (tag / variable / address) and how do screens bind to it?
2. How does the engineering→runtime cycle work (development environment vs deployed runtime)?
3. What does an operator actually do: observe, navigate, acknowledge, write values, command?
4. What is the alarm model (states, acknowledgment, journaling, notification)?
5. How do history/trends fit — inside the HMI or in a separate historian?
6. Who builds it (roles) and who operates it?
7. What are the deployment shapes (embedded panel, client/server, web/mobile)?
8. Where is the HMI vs SCADA boundary, given the market's "HMI/SCADA" bundling?
9. Would older/regional/panel-native products still satisfy the definition?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

1. **Ignition (Inductive Automation)** — independent platform vendor, web-based "HMI/SCADA" platform, unlimited licensing. Best publicly documented product in the space (official user manual fully reachable). Modern platform philosophy.
2. **AVEVA InTouch HMI** — the classic independent HMI lineage (Wonderware, 1980s origin) now inside a large industrial-software portfolio. Process-industry enterprise pole. Positioning + capability evidence reachable at Tier 2; operational docs not directly reachable.
3. **Red Lion (HMS Networks)** — panel HMI / hardware-attached software pole (machine builders, harsh environments). Positioning evidence only; Crimson operational documentation not directly reachable.

Considered and rejected/dropped during research: Siemens WinCC family (support.industry.siemens.com 403; siemens.com page 404 — abandoned per source-access rule), Rockwell FactoryTalk View (rockwellautomation.com 404 twice — abandoned). Their absence is recorded under Sources and lowers the claim strength for PLC-vendor-ecosystem specifics.

## Sources

Fetched 2026-09-08:

- Inductive Automation — Ignition product page: https://inductiveautomation.com/ignition/
- Inductive Automation — Ignition HMI solution page + FAQ: https://inductiveautomation.com/solutions/hmi
- Inductive Automation — Ignition 8.3 User Manual: Welcome / Introducing Ignition / Tags / Alarming / Perspective and Vision: https://docs.inductiveautomation.com/docs/8.3/...
- AVEVA — InTouch HMI product page: https://www.aveva.com/en/products/intouch-hmi/
- HMS Networks (Red Lion) — redlion.net/products/crimson redirects to HMS Networks corporate site (Red Lion brand positioning text)

Unreachable / limited (evidence strength reduced accordingly; no detail filled from memory):

- Siemens support portal (403), siemens.com product page (404)
- Rockwell Automation product pages (404 ×2)
- AVEVA help.aveva.com (404), docs.aveva.com (JS-rendered portal, no content), InTouch datasheet PDF (binary, unusable)
- HMS machine-visualization solution page (404 on guessed path)

Evidence layers used below: A = directly observed on an official source for that product; B = cross-product commonality across the sample; C = canonical inference from comparison + boundary reasoning.

## Product A — Ignition (Inductive Automation)

### Key observations (Layer A unless noted)

**Positioning.** Self-described platform: "One Industrial Platform for SCADA, IIoT, MES, and More"; HMI is one marketed "solution" of the platform. Sells as server software, hardware-agnostic ("does not sell any hardware"), cross-platform (Windows/macOS/Linux, ARM; even Raspberry Pi-class devices per FAQ).

**Architecture (Tier-1 manual).** Three top-level parts:
- **Gateway** — the central server. Web-configured hub: device connections, database connections, security, backups, redundancy. Tag data, projects, alarm state are Gateway-scoped.
- **Designer** — development environment (desktop-launched, connects to the Gateway). Component palette, drawing tools, templates, property/data binding, scripting; concurrent designers on the same project; "Preview Mode" to test as an operator before deployment; saving a project publishes it to the Gateway.
- **Runtime clients** — Vision (desktop client, launched via launcher; "traditional industrial plant-floor and desktop screens, standalone HMIs"; can use OS resources) and Perspective (web/mobile sessions; kiosk mode; touch/device sensors). Clients/sessions are web-deployed from the server; unlimited counts under one license.

**Tags (Tier-1 manual).** "Tags are points of data and may have static values or dynamic values that come from an OPC address, an expression, or a SQL query. The values can be used on screens and in transaction groups." Tag database organized in folders/providers; UDTs give parameterized, inheritable device/object types; quality codes and overlays for data state; tag naming decoupled from underlying address ("Motor 3 Amps" example). Drag-and-drop tag→component binding creates bound components. Per-tag alarming and per-tag history. Performance framing: "many thousands of value changes per second and millions of tags" (vendor claim — do not generalize numerically).

**Connectivity.** OPC UA built in; native driver suites for Modbus, Siemens, Allen-Bradley, BACnet, etc.; third-party OPC servers supported; MQTT via partner modules. Device connections, barcode scanners, scales, sensors.

**Alarming (Tier-1 manual).** Alarms are configured on tags (any number per tag; dynamic bound setpoints). Alarm event model:
- Conditions: **Active vs Cleared** (value meets criteria / no longer meets) and **Unacknowledged vs Acknowledged**; four combined states (Active+Unacked, Active+Acked, Cleared+Unacked, Cleared+Acked). Cleared→Active does not resume a closed event; a new event is created.
- Acknowledgment: a user-visible flag "commonly used as a way for users to 'claim' an alarm when multiple operators are monitoring" — performed via Alarm Status Table components or scripting.
- **Shelving**: time-bounded suppression, hides events and blocks notifications (maintenance scenarios).
- **Alarm Journal**: historical alarm events (source, timestamps, property values at event time) stored to an external SQL database; filterable.
- **Notification pipelines**: drag-and-drop routing (Email/SMS/Voice), on-call rosters, schedules, escalation pipelines (e.g., re-notify if not acknowledged; escalate after N attempts).
- Alarm Status Table and Alarm Journal Table components in both Vision and Perspective; system tags expose live alarm counts per state.

**History.** Tag Historian: per-tag checkbox logs to SQL databases; partitioning/compression (vendor claim); tag historian + historian solution suite for the entry HMI bundle; historical bindings, trend components, reporting module separate.

**Security.** Users/roles management; per-component and per-tag security in clients; 2FA and federated identity supported; SSL; audit log module.

**Flow (Tier-1 manual "Understanding Ignition's Flow").** Launch Gateway webpage → configure connections (devices, databases, security) → launch Designer → build project (tags, screens, alarms, queries) → save to Gateway → launch Clients/Sessions which "talk directly to the Gateway".

**Editions.** Standard server; Ignition Edge (embedded/edge devices; Edge Panel edition runs a server local to an HMI panel for standalone HMI use with local client fallback + data buffer); Cloud Edition; Maker Edition.

## Product B — AVEVA InTouch HMI

### Key observations (Layer A, but Tier-2 marketing/support surface only)

**Positioning.** "AVEVA InTouch HMI is HMI visualization software that empowers operators to optimize routine human interactions with industrial automation systems." Tagline: "Visualize, control and optimize your operations"; "The world's most widely used plant HMI for process monitoring and control." Explicit **monitor and control** language: "Visualize and control vital plant processes in real time."

**Capability surface (product page).**
- **HTML5 web client**: "securely monitor, control and troubleshoot plant equipment or process from any location, on any device" — remote operator access as a first-class mode.
- **Industrial graphics library**: "situational awareness library" — prebuilt process graphics; frames the operator job as addressing abnormal situations "quickly and accurately, before they impact operations" (abnormal-situation framing consistent with alarm-centric operation).
- **Advanced development tools**: application templates, symbol wizards, UDT support, SVG support, "distribute and enforce standards", runtime localization ("translate the entire HMI application in runtime with a click").
- **Personal workspaces**: "ad hoc run-time displays without any engineering development tools or scripting" — operators compose their own runtime displays.
- **Integrated historian and reporting** — in the Unlimited Premier edition (AVEVA Historian); the historian is a separate product line in the portfolio; PI System companion for enterprise data.
- **Cloud integration**: upload of real-time process tag data to cloud analytics (anomaly detection) — analysis layer, not the operator loop.

**Deployment/licensing.** Perpetual entry + subscription editions; editions gate historian/alarms packaging depth (alarms implied throughout; explicit alarm feature list not on the reachable page).

**Sourcing limitation.** Operational documentation (tag model, alarm state machine, screen editor internals) not reachable this pass; all product-B observations stay at the positioning/capability level, marked Tier-2 strength.

## Product C — Red Lion (HMS Networks)

### Key observations (Layer A, thin; positioning only)

- redlion.net/products/crimson redirects to HMS Networks; Red Lion is an HMS brand.
- HMS brand copy: "Red Lion products enable data visualization and control. Examples include HMIs, panel meters and controllers built for harsh industrial environments."
- HMS markets a "Machine visualization/control" solution family — the machine-builder pole: visualization attached to machines/panels rather than plant-wide supervision.
- **Sourcing limitation**: Crimson configuration software docs not directly reachable; no operational claims drawn from this pole beyond positioning. Used only as evidence that the Type extends down to hardware-attached machine-level panels (customer-tier breadth), not as a source for canonical structure.

## Cross-product Comparison

| Aspect | Ignition | AVEVA InTouch | Red Lion / HMS (positioning only) |
|---|---|---|---|
| Self-label | "HMI software" as a solution on an HMI/SCADA platform | "HMI visualization software" / "plant HMI" | "HMIs, panel meters and controllers" |
| Core object for live data | Tag (static, OPC, expression, SQL; UDTs; quality codes) | "real-time process tag data" (tag vocabulary present) | not observed |
| Operator graphics | Engineered screens: components, symbols, templates, bindings; Vision desktop + Perspective web/mobile | Industrial graphics library / situational awareness; HTML5 web client; personal ad-hoc runtime displays | "data visualization and control" on panels |
| Operator write-back | "start and stop processes with the push of a button"; write back through bindings | "monitor, control and troubleshoot" explicitly | "control" |
| Alarms | Platform-level alarm engine: per-tag alarms, 4-state events, ack, shelving, journal, notification pipelines | abnormal-situation response framing; alarm machinery present (packaging varies by edition — not directly verified) | panel alarm displays expected; not verified |
| History | Tag historian to SQL; historian suite in entry bundle | Historian bundled at higher edition; separate product line | not observed |
| Engineering environment | Designer (IDE-like, concurrent, preview mode, save-to-server) | templates/wizards/standards enforcement; development tools | configuration software (not observed) |
| Deployment | Server + web-deployed clients/sessions; edge editions; cross-platform | Windows heritage + HTML5 web client; cloud upload layer | embedded panels, harsh environments |
| Customer tier | integrators/end users, single machine → enterprise | process-industry enterprise | machine builders / OEM |
| Business model | unlimited server license | perpetual + subscription editions | hardware-attached software |

### Cross-product commonalities (Layer B)

Across the reachable sample, the following recur:
1. **Tag vocabulary** — live data held as named points ("tag"/"process tag data") decoupled from raw device addresses.
2. **Engineered runtime screens bound to live tags** — graphics created in a separate development surface and executed as runtime displays.
3. **Explicit monitor + control duality** — every sample product pairs visualization with operator command (write-back), not just monitoring.
4. **Alarm machinery in the core offering** — alarm annunciation, abnormal-situation framing, alarm display surfaces (state-machine detail verified only in Ignition, Layer A).
5. **Engineering/runtime separation** — a configuration/development surface distinct from the operator runtime; deployment as a distinct act.
6. **History/trends present in some form** — embedded or via companion historian; edition-gated in InTouch, module/suite-gated in Ignition.
7. **User accounts/security for operations** — verified deeply in Ignition; implied by InTouch "securely monitor and control".
8. **Client surfaces beyond the fixed panel** — web/mobile sessions verified in both reachable major products.

## Canonical Model (Step 5)

The Type can be modeled as two linked worlds sharing one live-data spine:

```text
ENGINEERING WORLD                      RUNTIME WORLD
─────────────────────                  ─────────────────────
device connections / drivers           cyclic acquisition from controllers
        ↓                                      ↓
tag database (named live data          live tag values (+ quality/state)
 points mapped to device addresses)    [shared spine]
        ↓                                      ↓
screens: graphics + animation +        rendered screens: overview / detail /
 bindings to tags                       alarm / trend / parameter surfaces
        ↓                                      ↓
alarm conditions & access rules        annunciate → acknowledge → act
        ↓                                      ↓
deploy project to runtime              operator actions written back as
                                        setpoints/commands; history & alarm
                                        events logged
```

Defining structures (candidate L0):
1. **Live process-data layer** — named data points acquired from controllers/devices through industrial drivers/protocols, carrying value + state/quality, decoupled from raw device addressing.
2. **Engineered operator screens** — graphical runtime displays whose elements are bound to the live data layer, organized by navigation over a machine/process scope.
3. **Operator write-back loop** — operator actions (setpoints, commands, mode selections) written back to the process through the same live-data layer.

Jointly-held load-bearing test:
- 1+2 without 3 = a monitoring dashboard over industrial data (no machine interface).
- 1+3 without 2 = a protocol gateway/data router with no operator surface.
- 2+3 without 1 = a simulator/mockup with no real process behind it.

Alarm annunciation: universal in the sample and central to the operator's job, but held as the top of L1 (standard capability), not a defining invariant — a minimal machine HMI still remains an HMI when few or no alarms are configured; the *machinery* (alarm display + acknowledgment + event retention) is nonetheless present in essentially every product of the Type.

## Abstraction Hierarchy

### L0 — Defining Invariant

1. Live process-data layer (named live points acquired from controllers/devices, decoupled from raw addressing, carrying quality/staleness).
2. Engineered operator screens bound to that live data layer.
3. Operator write-back to the process through the same data layer.

Anti-overfitting notes applied:
- **OPC UA is NOT in L0.** Ignition's own docs treat OPC as one implementation ("an OPC address" among static/expression/SQL sources); native drivers and MQTT are equally valid realizations. L0 phrase: "industrial drivers/protocols".
- **Client/server web architecture is NOT in L0.** Embedded panels (Red Lion pole, Ignition Edge Panel) and desktop single-node runtimes satisfy the core without a server.
- **Historian is NOT in L0** — edition-gated in InTouch, suite-gated in Ignition.
- **Alarming as system capability held at L1** (see Canonical Model note).
- **Windows/GUI desktop is NOT in L0** (web/mobile + embedded panels + desktop all valid).

### L1 — Common Mature Structure

- Alarm machinery: condition evaluation on tags, annunciation surfaces, operator acknowledgment, event journal/log, commonly notification/escalation (full ISA-18.2-style state machine verified in one product only; the acknowledgment loop and event retention appear across the sample).
- Historical logging + trend displays (embedded or companion historian; edition/module packaging varies).
- Engineering environment: screen editor with symbol/component libraries, binding dialogs, tag database browser, alarm configuration, user management, deployment/download.
- Operator security: user accounts, role-based access to screens/actions (verified in detail in Ignition: per-component/per-tag security, 2FA/federated identity).
- Navigation structures (menu/overview → detail), equipment object templates (UDT-class, verified in Ignition + InTouch UDT support).
- Quality/staleness presentation of live data (quality codes verified in Ignition; implied by "real-time" framing elsewhere — held B-with-caveat).

### L2 — Variant / Optional Structure

- Deployment shape: embedded panel runtime / desktop client / web browser session / mobile / edge edition / cloud-hosted data layer.
- Ecosystem posture: PLC-vendor-bundled HMI (TIA Portal–integrated, PanelView-class) vs independent platform vs panel-maker software; suite packaging (HMI as one module of SCADA/MES platform).
- High-performance HMI / situational-awareness styling programs (graphics standards) — a design methodology sold with some products.
- Recipes/parameter-set management, script/logic extension layers, localization/multi-language runtime (verified InTouch one-click runtime translation), redundancy/store-and-forward, KPI/analysis layers, cloud analytics upload, personal ad-hoc operator displays.
- Scale-up: multi-site enterprise deployments, central aggregation — the seam toward SCADA (below).

### L3 — Vendor-specific (research notes only)

- Ignition: Gateway/Designer/Vision/Perspective naming; unlimited-tags licensing model; Tag Providers, alarm pipeline/roster specifics; Edge Panel single-HMI edition; QuestDB-powered core historian; Store & Forward.
- AVEVA: InTouch Unlimited editions; AVEVA Historian + PI System pairing; situational awareness library as branded differentiator; Integration Studio cloud development.
- Red Lion/HMS: hardware-software pairing with panels/meters in harsh environments.
- (Siemens TIA-Portal-integrated HMI, Rockwell FactoryTalk View ecosystem — not directly evidenced this pass; excluded from all assertions.)

## Boundary Findings

### vs SCADA (directory sibling, unprocessed leaf)

The market straddles hard: Ignition self-labels both "HMI software" and "SCADA software" on one platform; AVEVA keeps InTouch HMI and (Citect) SCADA as separate lines. Working discriminator (Layer C, proposed for the SCADA pass to ratify):
- **HMI** = the operator interface for a machine or local process: the screen/tag/alarm/write-back surface. Scope: an operator station or panel; a plant area at most.
- **SCADA** = supervisory system across sites/areas: telemetry from remote field sites, central multi-site data collection and historians, fleet-scale alarming, system-of-systems topology. Every SCADA deployment still *contains* operator HMI surfaces — the seam is the supervisory multi-site system around them, not the operator screen.
- Remove-tests both directions: strip multi-site telemetry/supervision from an Ignition deployment → clean single-site HMI remains; add a supervisory network of RTUs + central historian → the same product family becomes SCADA.
- Directory implication: keep both leaves; HMI documents the operator-interface Type; the SCADA pass should define the supervisory-system Type and record the straddle (flagged in STATUS Boundary Issues).

### vs PLC Programming Environment / DCS

Control logic lives in the controller; the HMI visualizes and commands but does not execute the process logic. The PLC programming environment engineers the logic; the HMI engineering environment engineers screens/tags/alarms. Same vendor bundles often ship both (TIA Portal-class), which is packaging, not identity.

### vs Industrial Historian

Historian = dedicated long-term time-series system of record. HMI trends are a display capability over recent/short history; both sampled major products pair with or gate a separate historian product/suite. Keep separate.

### vs Dashboard Platform (BI, §13)

Dashboards render business/analytical data; no controller protocols, no operator write-back to a process, no operator alarm-acknowledgment loop, no engineering/runtime deployment cycle. An HMI whose data layer is unplugged from controllers collapses toward a dashboard — the live process-data layer and write-back are the wall.

### vs Industrial IoT Platform

IIoT = device connectivity, data pipelines, cloud analytics (HMS itself sells both families under one roof — connectivity brands vs "machine visualization/control"). IIoT dashboards without write-back/alarm-ack are monitoring, not HMI. The HMI's defining write-back loop is the seam; MQTT/IIoT transport is an acceptable implementation of the HMI data layer (Ignition MQTT modules), so transport does not separate the Types.

### vs Digital Twin Platform

Twin centers on a model/simulation of the asset; HMI centers on the live process surface. Twins may embed HMI-like visuals; separate Types.

## Historical / Market-Sample Check

- **1980s–90s software HMI generation** (Wonderware InTouch lineage; FIX/Cimplicity/RSView-class): tag/variable databases, animated graphics ("mimics"), alarm annunciation + acknowledgment, trends, recipes, scripting — satisfies all three L0 legs with no web, no cloud, no OPC UA.
- **Panel HMI generation** (Pro-face GP-class, Siemens OP/TP, Allen-Bradley PanelView): screen editor + address/tag binding + alarm window + recipe + embedded runtime — satisfies all three legs on hardware-attached single-device scope.
- **Physical predecessor**: hardwired operator stations — indicator lamps/mimic panels + pushbuttons/annunciators — are the conceptual lineage of screens + write-back + annunciation; the software Type digitizes them (conceptual, not source-evidenced — held as reasoning only).
- **Modern web/mobile HMI** (Ignition Perspective, InTouch HTML5 web client): satisfies with server-centric deployment.
- Conclusion: the L0 holds across eras; the definition names no deployment shape, protocol, OS, or business model. Check passed.

## Uncertainties

1. **PLC-vendor-ecosystem HMI specifics** (Siemens WinCC, Rockwell FactoryTalk View) unverifiable this pass (403/404). Claims about ecosystem-bundled HMI are held at market-structure strength, not product-verified.
2. **InTouch alarm machinery detail** — alarm state machine, shelving, journal behavior not directly verified; only the abnormal-situation framing and general capability are asserted.
3. **Red Lion Crimson operational structure** — not verified; used only for customer-tier breadth.
4. **Whether alarming should be L0 or L1** — resolved to L1 with reasoning recorded; if the SCADA pass later argues alarm-ack is definitional to the operator loop, revisit.
5. **HMI vs SCADA discriminator** — proposed here, needs ratification by the SCADA leaf's own pass.
6. Numeric claims (tag counts, value-change rates, session counts) observed only as vendor marketing claims in Ignition material; deliberately excluded from both documents.

## Final Synthesis

An HMI Application is the **operator-facing live interface between people and controlled industrial processes**: a live process-data layer (tags) acquired from controllers through industrial drivers, an engineered set of runtime operator screens bound to that live data, and an operator write-back loop returning setpoints and commands to the process through the same data layer. Alarm annunciation with operator acknowledgment, historical trends, an engineering environment, operator security, and deployment machinery are the standard mature structure around that core. Deployment shapes (embedded panel, desktop client, web/mobile session, edge) and ecosystem posture (panel-maker, independent platform, PLC-vendor bundle) are variants. The seam to SCADA is the multi-site supervisory system, not the operator surface.
