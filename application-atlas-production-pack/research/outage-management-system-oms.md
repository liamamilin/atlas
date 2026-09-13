# Research Notes — Outage Management System / OMS

## Research Goal

Understand what "Outage Management System / OMS" software actually is as an Application Type: who operates it, what objects exist inside it, what lifecycle it drives (signal → event → crew → restoration → record?), and where its boundary lies against neighboring Types — especially Advanced Distribution Management System / ADMS (§19, processed, carries a pre-hung joint-review flag for this leaf), SCADA (§16), Grid Operations Platform (§19, processed — names this leaf as a member to cross-reference), DERMS (§19, processed), Utility GIS / AMI / MDMS / CIS (§19), Utility Field Service Management (§19, unprocessed), and Emergency Management Platform (§24).

Special obligations from STATUS.md:
- DISCHARGE the ADMS pass's pre-hung flag: "OMS is a module/pillar inside every sampled ADMS, but a standalone call-center-centric OMS without real-time network operations exists; structural test = real-time network monitoring/control on a connected network model (remove it → OMS remains; remove OMS → ADMS remains) — Capability/module relationship; flagged for joint review when OMS is processed."
- Treat applications/grid-operations-platform.md as counterparty (that pass listed outage-management-system-oms among unprocessed member leaves that should treat its document as the family map).

## Initial Boundary

Working hypothesis: an OMS is the utility's outage-response system — it turns signals that customers have lost power (trouble calls, meter pings, SCADA alarms) into predicted outage events on the network model, groups them, dispatches and tracks crews, maintains estimated restoration times, notifies customers, and records restoration for reliability reporting.

Nearest neighbors and expected seams:
- **ADMS** — real-time network operations (telemetry + supervisory control + network applications) vs the outage response loop. The ADMS pass already drew this seam; this pass must ratify it from the OMS side.
- **SCADA** — telemetry/control substrate; its alarms are an input signal to OMS.
- **Utility GIS** — holds the as-built connectivity model the OMS predicts on; no operational loop.
- **CIS / customer systems** — customer identity/phone/service-point data consumed for call matching; call logging without network-model prediction is the below-Type pole.
- **AMI/MDMS** — meter pings and last-gasp signals as an input; no response management.
- **Utility Field Service Management** — shares crew-dispatch machinery; expected seam is unplanned outage events vs scheduled service work.
- **Emergency Management Platform** — storm/mutual-aid coordination overlaps; OMS centers the restoration loop.
- **Incident Management (§14)** — name collision only (IT incidents vs grid outages); unrelated Types.
- **Order Management System / OMS (§05.07)** — pure name collision; unrelated Types.

## Research Questions

1. What is the core object — is there a persistent "outage event" record, and what does it carry?
2. How do incoming signals (calls, meter pings, SCADA alarms) become events? Is prediction on a network model the distinctive machinery?
3. What is the crew dispatch and restoration loop, and what states does it move through?
4. What is the estimated restoration time (ERT) and how is it maintained? Is it definitional or common?
5. How do customers participate (call taking, callbacks, notifications, public outage maps/portals)?
6. How do AMI and SCADA integrate, and are they definitional or input channels?
7. What reliability reporting exists (indices, cause codes, exclusions)?
8. What happens in storm mode, and is mutual-aid coordination part of the Type?
9. Where exactly is the OMS/ADMS seam, and can a standalone OMS exist without real-time network operations?
10. Would older, smaller, non-US, or paper-era outage response still fit the definition?

## Representative Products

| Product | Vendor | Segment / posture | Evidence depth |
|---|---|---|---|
| Oracle Utilities Network Management System (NMS) — OMS layer | Oracle | Large utilities; integrated ADMS platform whose OMS layer (Web Trouble Management) is deeply documented | **Deep** — Tier-1: full User Guide TOC fetched this pass; OMS-layer page-level observations carried from the ADMS pass's fetched Oracle pages |
| Milsoft OMS (+ FieldSyte, StormSyte, IVR) | Milsoft Utility Solutions | Co-ops/municipals; standalone OMS pole (no real-time network operations) | **Medium-deep** — Tier-2: OMS product page, FieldSyte page, StormSyte page, site navigation (all fetched) |
| SurvalentONE OMS (+ Call Handler, Customer Outage Portal, Polaris, OMS Dashboard, Damage Reporting & Assessment) | Survalent | Mid-market (co-ops/municipals); modular: OMS as separately documented product composing the ADMS | **Medium** — Tier-2: OMS product page + Call Handler page fetched |
| AspenTech OSI Outage Management System (inside DGM suite) | AspenTech (OSI) | Control-center specialist; OMS as named product inside the ADMS/DGM suite | **Light** — Tier-2: DGM suite page fetched (OMS named in suite + webinar listing); dedicated OMS page not found (404 on guess, not retried) |

Selection logic: market representation across utility scale (large IOU → co-op/muni), different packaging philosophies (integrated ADMS layer vs standalone OMS vs modular suite vs control-center suite), and documentation accessibility. Oracle provides the Tier-1 operational depth; Milsoft provides the standalone pole that the ADMS pass's structural test requires; Survalent provides the modular mid-market pole with a dedicated CSR surface; AspenTech confirms the suite-embedded naming at a second control-center vendor.

## Sources

Fetched 2026-09-09 unless noted:

Tier 1 (official operational documentation):
- Oracle Utilities Network Management System documentation library (Release 25.12): https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html — fetched
- NMS User Guide (25.12) — full table of contents fetched (chapters: Web Workspace; Managing Events with Web Trouble Management; Managing Crews with Web Trouble Management; Web Call Entry; Web Callbacks; Storm Management; Service Alert Administration; Management Reporting; Flex SCADA; SCADA Extensions; Web Switching Management; Power Flow; Distribution State Estimation; Suggested Switching; Grid DERMS; plus a separate "NMS OMS for Water User Guide")
- Oracle NMS OMS-layer page-level observations (Event Details tabs, call entry/fuzzy calls, crew states, storm management, AMI requests, reliability indices) — carried from research/advanced-distribution-management-system-adms.md (fetched 2026-09-06 from the same documentation library)

Tier 2 (official product pages):
- Milsoft — Outage Management: https://www.milsoft.com/engineering-operations/outage-management/ — fetched
- Milsoft — FieldSyte: https://www.milsoft.com/engineering-operations/outage-management/milsoft-fieldsyte/ — fetched
- Milsoft — StormSyte: https://www.milsoft.com/engineering-operations/outage-management/milsoft-stormsyte/ — fetched
- Milsoft — site navigation (IVR Plus OMS, Outage Alerts, Texting, CIS, MDM/AMI pages listed) — fetched
- Survalent — SurvalentONE OMS: https://www.survalent.com/products/outage-management-system-oms/ — fetched
- Survalent — SurvalentONE Call Handler: https://www.survalent.com/products/outage-management-system-oms/call-handler-client/ — fetched
- AspenTech — Digital Grid Management suite: https://www.aspentech.com/en/products/suites/digital-grid-management — fetched

Not reachable / limitations:
- Oracle NMS individual topic pages (03_WT_EventMgmt.04.02.html, 03_WT_EventMgmt.04.06.html) — request timeout ×2 each; abandoned per network rules. The full TOC (fetched) plus the ADMS pass's page-level observations cover the OMS layer.
- AspenTech dedicated OMS product page — 404 on URL guess; not retried. OMS evidence stays at suite-page level (naming + webinar listing).
- GE Vernova GridOS OMS page — not probed (sample already at 4 products with stop conditions met).
- No pricing, no numeric limits, no default values asserted anywhere from any source.

---

## Product A — Oracle Utilities Network Management System (Tier 1, evidence layer A; TOC fetched this pass, page-level observations carried from the ADMS pass)

Oracle ships NMS as an integrated platform: the ADMS Implementation Guide names **OMS Modules** (data model, SCADA adapters, trouble management & events, web switching) beside **ADMS Modeling**. The User Guide's OMS-relevant chapters:

- **Managing Events with Web Trouble Management** — Event Details (information pane + tabs); Update Events (update multiple events, copy details to related partial-restoration events, complete an event); Confirm and Restore Outages (confirmed service outage, confirmed secondary outage, restore); Work Queues; **Event Grouping** (group events dialog, grouping rules, graphical grouping in supply-points mode, relate/ungroup events); associating/unassociating calls with devices or control zones (fuzzy calls); **Stable Predictions**; Damage Assessments (window + fuzzy damage assessments); **AMI Requests** (create/complete/cancel/re-submit — meter ping, load-side status, voltage reading); **Updating the ERT** (per event, clear, system-wide ERT); Trouble Summary (outage/damage/assessment summary data + trend graph).
- **Managing Crews with Web Trouble Management** — Crew Actions window (views + operations); Crew Makeup (personnel, vehicles); create/edit crews; **assign → en route → onsite → offsite → suspend → release**; crew assignment duration/order; unassign; bulk crew loading (admin).
- **Web Call Entry** — search customer (by call ID or caller info); call history; event history; **entering a customer call**; informational calls; **fuzzy calls**; canceling calls (incl. all calls for an account); outages summary.
- **Web Callbacks** — assign callbacks (by number or percentage, all remaining), view assignments, perform callbacks.
- **Storm Management** — full-operations / view-only / administration environments; storm modes; storm information + storm report; ERT overrides (manual); **storm mode vs non-storm mode algorithms** (different ERT calculation behavior).
- **Service Alert Administration** — Contact Manager, Group Manager, Parameter Manager, Utility Customer Manager, Attribute Manager (the customer-notification machinery).
- **Management Reporting** — its own chapter.
- Carried page-level observations (ADMS pass): Event Details tabs include Job Actions (restoration log with stages, per-stage CMI), Completion Actions (structured cause codes — system/sub-system/device type/failure/interrupting device/primary cause/weather/vegetation/foreign interference/defective equipment/scheduled/utility error + remedy; interruption-indices exclusion with recorded reason + post-completion edit log), Trouble Info (Callers / Customers / Supply Points / AMI Customers views), Damage Assessments (statuses incl. New/Assessing/Assessed/Standing By/Fixed/Obsolete), Event Log, Fault Location Analysis, FLISR Report; calls grouped into events by grouping rules; moving a customer to a different device re-runs prediction ("Calls may be grouped into another existing event or a new event will be created"); critical-customer counts (Emergency/Medical/Key/Sensitive); AMI confirm for outages; Smart Grid Gateway integration for outage operations.
- **OMS for Water User Guide** exists as a separate guide — the OMS layer is sold for a second carrier (water), evidence that the outage-response pattern is carrier-portable while the electric specifics (phases, feeders) are not the definition.

## Product B — Milsoft OMS (Tier 2, evidence layer A at product-page level)

Standalone OMS pole for cooperatives and municipals. Direct observations:

- Positioning: "Milsoft OMS delivers on power restoration tools…" — the product's center is outage response, not real-time network operation.
- **Prediction on the circuit model**: "The robust prediction engine processes the incoming events and provides the exact outage location on the circuit model"; "Detailed circuit model representation allows for quick location predictions of current outages so crews are dispatched to a specific piece of equipment in the field, eliminating the need for lengthy line patrol."
- **Fault analysis from protective devices**: "when a fault is measured at a protective device on the system, Milsoft Outage Management can give locations where that fault is possible."
- **Integrations as inputs**: "Integrations to other critical utility systems like Automated Metering, SCADA, and Billing put all the information needed for efficient outage management in one place"; DisSPatch "gives your system operators the ability to interact with data from several software systems, including Automated Metering, SCADA, Automated Vehicle Locations, and Customer Billing."
- **Switching/restoration representation on the model**: "The same model gives the dispatcher the power to represent what's happening in the area with robust switching and restoration tools. Equipment can be opened and closed, lines are broken to create open points, and jumpers installed to create new feeds." Switching Scheduler: engineers test switching scenarios in Milsoft Engineering Analysis; "Approved action plans can be accepted and sent directly to the Milsoft Outage Management system for implementation in the field."
- **Field**: Milsoft FieldSyte mobile — "personnel to work outages in real-time on mobile devices… the COMPLETE Milsoft data model accessible in the field, whether connected or disconnected to the network"; modules include OMS Tickets, OMS Assessments, Live Model, AMI Integration, AVL Integration.
- **Customer communication**: Milsoft Communications (IVR) — "Get rid of busy signals on the phone, give them accurate and up to date information about their specific outage… phone, text, or email"; Outage Web Viewer — "the public a map with all active outages on it"; customers "log into the outage web viewer to report outages for their accounts and view the status of existing outages affecting their accounts."
- **Storm/mutual aid**: StormSyte — separate web platform "to allow utilities or statewide organizations to easily coordinate mutual aid crews during large events"; role-based; request crews by type; coordinator assigns available crews to requesting utilities; "Export Crew Information assigned to you for importing into other Utility Systems"; "no matter what other systems you use at your utility, this platform will work for you."
- Heritage: "Taking on Storms Since 2002"; "Hundreds of utilities use Milsoft OMS already."

## Product C — SurvalentONE OMS (Tier 2, evidence layer A at product-page level)

Modular mid-market pole; OMS is a separately documented product composing the SurvalentONE ADMS.

- **Predictive outage analysis**: "The solution provides predictive outage analysis that helps operators determine the probable fault location so that field crew can quickly commence restoration activities."
- **DER dispatch**: "For utilities with integrated DERs, it provides the ability to rapidly dispatch power to affected areas to reduce outage extents and durations."
- **Integration with SCADA/DMS**: "SurvalentONE OMS integrates seamlessly with SurvalentONE SCADA and DMS applications to ensure that all applications share the same data. For example, **FLISR events are automatically captured in the OMS**."
- **Transparency + damage assessment**: "enables transparency between the control room and field crew, as well as processes for rapid damage assessment, to ensure the right crews and equipment are dispatched at the onset of restoration."
- **Customer communications**: "automated text messaging and social media update capabilities to provide customers with up-to-date outage information, including the estimated time of restoration and safety information."
- **Stated benefits**: faster restoration; "Improved SAIDI and SAIFI reliability indices"; transparency; customer satisfaction.
- **Optional OMS applications** (packaging evidence): Customer Outage Portal; CSR Call Handler; Polaris (mobile crew); OMS Dashboard; Damage Reporting & Assessment.
- **Call Handler** (fetched): "a dedicated outage management tool for CSRs that provides access to current outage information, including estimated time of restoration"; CSRs "search for the customer's account using a variety of methods and then record information provided by the call"; "If authorized, CSRs can **ping customer meters** directly"; "**Call Handler automatically associates the call record to any active outage case** the caller is experiencing"; "CSRs can also create tickets for calls unrelated to outages"; available as SmartVU interface or web portal "without… requiring access to the utility's secure ADMS environment."

## Product D — AspenTech OSI Outage Management System (Tier 2, suite-page level)

- DGM suite page: "AspenTech OSI Advanced Distribution Management System™ — Integrated solution suite for active management of distribution grids including advanced applications, **outage management** and distributed energy resource management." Distribution pillar: "advanced automation, network model management, outage management and distributed energy resource integration."
- Named product: "**AspenTech OSI Outage Management System™ (OMS)**" with "**Compass™ mobile app**" — webinar listing: "Discover how the AspenTech OSI Outage Management System™ (OMS) and Compass™ mobile app work together to transform outage response and restoration."
- Adjacent named products: SOM Planner (Switch Order Management — "streamline outage scheduling, safe switching operations and permit management"); Operator Training Simulator; Cimphony Network Model Management.
- Dedicated OMS product page not found (404 on one URL guess; not retried). All AspenTech observations stay at naming/positioning level.

---

## Cross-product Comparison

| Structure / capability | Oracle NMS | Milsoft OMS | SurvalentONE OMS | AspenTech OSI OMS | Layer |
|---|---|---|---|---|---|
| Persistent outage event record with lifecycle to completion + cause | ✓ (Event Details, complete event, cause codes) | ✓ (outage tickets worked to restoration) | ✓ ("active outage case") | n/e (naming level) | Core candidate |
| Signal→event prediction on a network/connectivity model | ✓ (prediction on network model; re-prediction on re-association) | ✓ ("exact outage location on the circuit model") | ✓ ("predictive outage analysis… probable fault location") | n/e (implied by suite framing) | Core candidate |
| Call taking incl. partial-information ("fuzzy") calls | ✓ (Web Call Entry, fuzzy calls) | ✓ (IVR front line; call handling) | ✓ (Call Handler: search, record, auto-associate) | n/e | Core-adjacent (call channel) |
| Call/signal grouping into events (rules-based) | ✓ (grouping rules, graphical grouping) | ✓ (prediction engine processes incoming events) | ✓ (auto-association to active outage case) | n/e | Core candidate (part of prediction) |
| Crew dispatch with states (assign→en route→onsite→…→release) | ✓ (Crew Actions) | ✓ (dispatching crews; FieldSyte) | ✓ (crews dispatched; Polaris) | ✓ (Compass mobile app) | Core candidate |
| Restoration recorded in stages; affected-customer counts update | ✓ (restoration log with stages, per-stage CMI) | ✓ (work tickets "to the point of restoration") | ✓ (partial-restore imagery; restoration activities) | n/e | Core candidate |
| ERT as maintained field (per-event; system-wide in storms) | ✓ (update/clear ERT; system-wide ERT) | ✓ (ETRs shown to public) | ✓ (ETR in customer comms) | n/e | Common mature |
| Customer notification (calls/SMS/email/social) | ✓ (Service Alert Administration; callbacks) | ✓ (IVR, texting, email; Outage Alerts) | ✓ (automated text + social media) | n/e | Common mature |
| Public outage map / customer portal (view, report, status) | n/e (not in fetched TOC layer) | ✓ (Outage Web Viewer) | ✓ (Customer Outage Portal) | n/e | Common mature |
| AMI integration (pings, status, confirm) | ✓ (AMI Requests; AMI Customers view) | ✓ (AMI integration; FieldSyte AMI module) | ✓ (CSR meter ping via Call Handler) | n/e | Common mature (input channel) |
| SCADA integration (alarms/lockouts as input) | ✓ (SCADA adapters; Flex SCADA in platform) | ✓ (SCADA named as integrated input) | ✓ (SCADA + DMS share data; FLISR events captured) | n/e | Common mature (input channel) |
| Fault-location analysis from protective-device data | ✓ (Fault Location Analysis tab) | ✓ (fault analysis → possible locations) | ✓ (probable fault location) | n/e | Common mature |
| Damage assessment machinery | ✓ (Damage Assessments + fuzzy assessments) | ✓ (FieldSyte OMS Assessments) | ✓ (Damage Reporting & Assessment product) | n/e | Common mature |
| Critical-customer tracking | ✓ (Emergency/Medical/Key/Sensitive counts) | n/e | n/e | n/e | Common (single-product-dominant observation) |
| Callbacks queue | ✓ (Web Callbacks) | n/e | n/e | n/e | Common |
| Storm mode (different ERT algorithms, view-only env, storm report) | ✓ (Storm Management chapter) | ✓ (StormSyte for large events) | n/e (Storm Response hub exists) | n/e | Common mature |
| Mutual-aid crew coordination | n/e | ✓ (StormSyte — separate product) | n/e | n/e | Optional (separable capability) |
| Reliability reporting (CMI, SAIDI/SAIFI-style, exclusions with reason) | ✓ (per-stage CMI; indices exclusion) | n/e (implied) | ✓ ("Improved SAIDI and SAIFI") | n/e | Common mature |
| Mobile field app (tickets, assessments, offline) | ✓ (Operations Mobile Application — install guide listed) | ✓ (FieldSyte, connected or disconnected) | ✓ (Polaris) | ✓ (Compass) | Common mature |
| Switching/restoration representation on the model | ✓ (Web Switching Management — ADMS layer) | ✓ (open/close, open points, jumpers; Switching Scheduler) | n/e (Switch Orders product exists) | ✓ (SOM Planner) | Common (ADMS-shared machinery) |
| DER dispatch to reduce outage extent | n/e | n/e | ✓ ("rapidly dispatch power to affected areas") | n/e | Optional (current-era) |
| Standalone deployment without real-time network operations | — (integrated platform) | ✓ (the product's whole posture) | — (modular but ADMS-composing) | — (suite-embedded) | Variant axis |
| Second-carrier realization (water) | ✓ (OMS for Water User Guide) | n/e | n/e (water industry page exists) | n/e | Variant axis |

Reading: the first five core-candidate rows are present in every product where the evidence layer allows observation; the input channels (AMI/SCADA), customer-communication layer, ETR, storm machinery, and reliability reporting are universal-or-near-universal but clearly additive modules (Survalent ships several as *optional applications*; Milsoft ships mutual aid as a *separate product*; Oracle documents storm/notification as separate chapters/tools).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal; three jointly-held structures)

```text
Outage Event (unit of record)
└── Signal-to-event prediction & grouping on the network connectivity model
    └── Crew dispatch & restoration loop (to a completed, cause-coded record)
```

1. **The outage event as the unit of record** — a persistent, individually identified record of one outage condition on the network, opened from incoming signals, carrying the affected customers, the predicted (and/or confirmed) outage device, its lifecycle state (open → crews working → restoration stages → completed), timestamps, and an estimated restoration time. Remove it → an outage call log with no managed event.
2. **Signal-to-event prediction and grouping on the network connectivity model** — incoming trouble calls (and commonly meter pings and SCADA alarms) are matched against the as-built connectivity model — which customers are served through which devices — to predict the outaged device and group related signals into one event; re-associating a signal re-runs the prediction and may regroup events. Remove it → generic call/work tracking (the below-Type pole); the OMS's distinctive intelligence is gone.
3. **The crew dispatch and restoration loop** — crews are assigned to events and tracked through states (assigned/dispatched/en route/on site/restoring/released — labels vary), restoration is recorded in stages that update affected-customer counts, and the event is completed with structured cause codes feeding the utility's reliability record. Remove it → a prediction console with no restoration management, or a generic dispatch board.

Jointly-held is load-bearing:
- 1 alone = outage log / incident register
- 2 without 1 = prediction calculator with no memory
- 3 without 1+2 = generic crew dispatch (Utility FSM territory)
- 1+2 without 3 = call-grouping console, restoration unmanaged
- 1+3 without 2 = dispatch keyed to raw outage reports (below-Type pole)
- 2+3 without 1 = ephemeral dispatch, no record

Deliberately NOT in L0 (tested against the ADMS pass's structural test and the historical check):
- **Real-time telemetry and supervisory control of the network** — this is the ADMS differentiator. A standalone OMS (Milsoft pole) predicts and dispatches without operating the network in real time; SCADA/AMI data arrive as inputs.
- **Power-flow / network applications** (state estimation, FLISR, VVO) — ADMS territory; where present, their events flow INTO the OMS (Survalent: "FLISR events are automatically captured in the OMS").
- **AMI, SCADA, IVR, web portals, mobile apps, cloud** — input channels and surfaces; the paper-era loop satisfies L0 without any of them.
- **Specific reliability indices (SAIDI/SAIFI)** — reporting regime machinery, common but not definitional.

### Historical / market-sample check

- **Paper-era outage response**: call takers with customer card files + circuit maps; calls pinned/grouped on a wall map by feeder; dispatcher assigning line crews by radio; restoration logged on paper outage tickets; monthly reliability tallies compiled from tickets. All three L0 legs satisfied at analog level — event record (ticket), prediction/grouping on the connectivity model (circuit map + pins), crew dispatch/restoration tracking (radio + log). No AMI, no web map, no cloud, no ETR algorithms in the core.
- **1990s client-server trouble-call OMS generation**: call entry + prediction on a connectivity model + crew boards + restoration logging, integrated to CIS and (later) SCADA — satisfies without AMI, web portals, or mobile apps.
- **Non-US / smaller utilities**: the same loop holds; regional differences (safety-document regimes, reliability-reporting obligations) sit in the variant layer.
- Conclusion: the definition is era- and scale-robust; nothing current-era (AMI, apps, AI, cloud, DER dispatch) is required.

### L1 — Common Mature Structure (standard capabilities; not definitional)

- **ERT as a maintained field** — per-event ERT that operators update; system-wide ERT for major events (Oracle); published to customers (Milsoft, Survalent).
- **Customer communication layer** — outbound notifications (phone/text/email/social), callback queues, service-alert administration (Oracle Service Alert Administration; Milsoft Communications/IVR; Survalent automated text + social).
- **Public outage map / customer portal** — view active outages + ETRs, report an outage, check status (Milsoft Outage Web Viewer; Survalent Customer Outage Portal).
- **AMI integration** — meter pings, load-side status, voltage readings, last-gasp-style unsolicited status; AMI confirmation of outage extents (Oracle AMI Requests; Milsoft AMI integration; Survalent CSR-authorized meter ping).
- **SCADA integration** — breaker lockouts and device alarms as prediction inputs (all sampled where observable).
- **Fault-location analysis** — probable fault points from protective-device fault measurements (Oracle FLA tab; Milsoft fault analysis; Survalent probable fault location).
- **Damage assessment** — structured assessment records with statuses, including fuzzy/partial assessments (Oracle; Milsoft FieldSyte OMS Assessments; Survalent Damage Reporting & Assessment).
- **Critical-customer tracking** — emergency/medical/key customer flags affecting priority (Oracle-documented; treated as common, single-product-dominant observation).
- **Reliability reporting** — customer-minutes interrupted accumulated per restoration stage; structured cause codes; index exclusions only with recorded reason; SAIDI/SAIFI-style indices as the stated benefit (Oracle; Survalent).
- **Storm mode** — behavior switch under mass outages: different ERT algorithms, view-only environments, storm reports (Oracle Storm Management; Milsoft storm positioning).
- **Mobile field apps** — outage tickets, assessments, live model, offline capability (Oracle Operations Mobile Application; Milsoft FieldSyte; Survalent Polaris; AspenTech Compass).
- **Switching/restoration representation on the model** — open/close equipment, create open points, install jumpers; planned switching prepared in engineering/switching tools and executed against the OMS's model (Milsoft; Oracle Web Switching Management as the ADMS-shared layer; AspenTech SOM Planner).

### L2 — Variant / Optional Structure

- **Packaging** — standalone OMS (Milsoft pole); OMS as a separately licensed module composing an ADMS (Survalent, Oracle modules); OMS as a named product inside a control-center suite (AspenTech). The ADMS-embedded realization is dominant in the current market but the standalone pole is real and documented.
- **Customer scale/segment** — co-ops/municipals (Milsoft, Survalent) vs large utilities (Oracle, AspenTech OSI).
- **Carrier substrate** — electric is canonical; Oracle ships an OMS for Water guide; Survalent sells into water/wastewater. The outage-response pattern is carrier-portable; electric specifics (phases, feeders, protective devices) are content, not structure.
- **Storm/mutual-aid coordination** — built into the OMS's storm mode (Oracle) or shipped as a separate cross-utility coordination product (Milsoft StormSyte); the separability is vendor-documented.
- **DER dispatch during outages** — current-era capability at some vendors (Survalent: "rapidly dispatch power to affected areas").
- **Deployment** — on-premises control-room heritage vs web/cloud clients (current direction; web portals and browser surfaces documented at Milsoft/Survalent).
- **Regional regimes** — reliability-index definitions, regulatory reporting, safety-document conventions vary by jurisdiction; products adapt through configuration.

### L3 — Vendor-specific (research notes only; must not enter the final document)

- Oracle: "fuzzy calls" and "stable predictions" terminology; supply-points-mode graphical grouping; confirmed service outage vs confirmed secondary outage distinction; Emergency/Medical/Key/Sensitive customer classes; Smart Grid Gateway integration product; OMS for Water guide.
- Milsoft: DisSPatch, FieldSyte, StormSyte, Outage Web Viewer product names; Switching Scheduler via Milsoft Engineering Analysis; "Taking on Storms Since 2002" heritage claim; RC Map Engine.
- Survalent: Call Handler / SmartVU / Polaris / OMS Dashboard product names; "FLISR events are automatically captured in the OMS" integration claim; CSR-authorized meter pings.
- AspenTech: Compass mobile app; SOM Planner; monarch platform framing.

### Rejected Findings (considered and rejected for the core)

- "OMS = call center software" — rejected: call taking is one input channel; the defining machinery is model-based prediction + event management + restoration tracking. A call center without prediction is the below-Type pole.
- "OMS requires AMI" — rejected: the paper-era and 1990s generations satisfy the core without AMI; AMI is an input channel that improves prediction confidence.
- "OMS includes FLISR/restoration automation" — rejected: automation belongs to the ADMS/DMS layer; its events flow into the OMS as records (Survalent's own wording). The OMS manages the response; it does not have to compute or execute restoration automation.
- "OMS includes customer information/billing" — rejected: CIS is a consumed data source (customer identity, phone, service point); Milsoft sells CIS as a separate product line.
- "OMS includes GIS" — rejected: the connectivity model is consumed/derived from GIS or maintained in the OMS; GIS is the as-built source, not the operational loop.
- "Mutual-aid coordination is definitional" — rejected: Milsoft ships it as a separate product that "will work for you" regardless of the OMS in use — vendor-documented separability.

## Boundary Findings

1. **vs Advanced Distribution Management System / ADMS (§19, processed) — DISCHARGES the pre-hung joint-review flag.** Keep-both RATIFIED from this side, on exactly the seam the ADMS pass proposed: the discriminator is **real-time network operations** — live telemetry rendered on a connected electrical model plus supervisory control of field devices plus network applications computed on live state. The OMS's center is the outage-response loop: signals → predicted events → crews → restoration → reliability record. Removal tests hold in both directions: strip real-time monitoring/control from an ADMS and an OMS-centric trouble system remains (the Milsoft pole proves a full OMS exists there); strip the outage loop from an ADMS and the ADMS remains (network model + control + applications). In modern integrated products the OMS is a layer of the ADMS on one network model (Oracle: OMS Modules beside ADMS Modeling; Survalent: OMS beside SCADA/DMS with FLISR events auto-captured; AspenTech: OMS inside the ADMS suite) — packaging, not identity. The model itself differs in kind: the OMS needs the as-built **connectivity** model (who is served through what) for prediction; the ADMS additionally carries **live electrical state** (voltages, flows, islands) and computes on it. Shared machinery when integrated: events, crews, ERT, switching — which is why the two Types are easy to conflate and why the market sells them as one platform.
2. **vs SCADA (§16)** — substrate/input relationship. SCADA acquires telemetry and executes control; its alarms (breaker lockouts) are prediction inputs to the OMS. SCADA holds no outage events, no crews, no restoration records. Confirmed at Oracle (SCADA adapters as OMS modules' input side) and Milsoft (SCADA as an integrated data source).
3. **vs Grid Operations Platform (§19, processed)** — counterparty relationship per that pass's family map: the OMS is the **outage-layer member** of the control-room family ("The call → event → crew → restoration loop; standalone as a call-center system, otherwise a layer of the ADMS within the estate"). This document is the member's own record; the family map lives in the grid-operations-platform document. No conflict found.
4. **vs DERMS (§19, processed)** — DERMS coordinates the DER fleet; during outages it may act as an execution arm (Survalent: dispatch DER power to reduce outage extent), but the outage event/crew/restoration record lives in the OMS. Consistent with the DERMS pass's SCADA/ADMS/OMS division-of-labor note (restoration support).
5. **vs Utility GIS (§19, unprocessed)** — model source. GIS holds as-built geographic asset records; the OMS consumes/derives the connectivity model and runs the operational loop on it. Milsoft's own framing ("the Milsoft Circuit Model" shared between OMS and Engineering Analysis, fed by their GIS) shows the model as shared substrate, not the OMS itself.
6. **vs Utility Customer Information System / CIS (§19, unprocessed)** — data source + below-Type pole. CIS holds customer identity/phone/service-point master data the OMS matches callers against; a call-logging module without network-model prediction is trouble-call logging, not an OMS. Forward note for the CIS pass.
7. **vs Utility Field Service Management (§19, unprocessed)** — shared crew-dispatch machinery; expected seam = unplanned outage events predicted on the network model vs scheduled service work orders against appointments. Forward note for that pass.
8. **vs AMI / MDMS (§19, processed)** — signal source. Meter pings and unsolicited status refine/confirm outage extents; neither manages the response. The MDMS pass's billing-quality-data center is unrelated.
9. **vs Emergency Management Platform (§24, unprocessed)** — overlap on storm response; OMS centers the outage restoration loop with the network model; emergency management centers all-hazards coordination. Milsoft shipping mutual-aid coordination as a separate cross-system product supports the seam.
10. **vs Incident Management (§14, processed)** — name-collision guard only: IT incident response vs grid outage response; unrelated Types, never merge.
11. **vs Order Management System / OMS (§05.07, processed)** — pure name collision (commerce order lifecycle vs utility outage response); unrelated Types.
12. **Customer-facing outage surfaces** — public outage maps/portals and notification engines ship as OMS modules or companion products (Survalent Customer Outage Portal; Milsoft Outage Web Viewer + Outage Alerts); they are the OMS's outward face, not a separate Type.

## Uncertainties

- Oracle topic-page bodies were not fetched this pass (timeouts ×2, abandoned); OMS-layer page-level detail rests on the ADMS pass's fetched pages plus this pass's full TOC. No claim in the final document exceeds what those two layers support.
- AspenTech OSI OMS is evidenced at suite/naming level only; no operational mechanics claimed.
- Whether every standalone OMS in the market maintains its own connectivity model vs consuming GIS directly was not exhaustively verified; Milsoft documents a shared circuit model, Oracle documents model import from GIS. Held as implementation variance.
- Critical-customer tracking and callback queues are single-product-dominant observations (Oracle); treated as common-mature at most, never definitional.
- Water-OMS depth (Oracle's OMS for Water guide) not fetched; carrier portability asserted only at guide-existence level.
- No numeric limits, ETR algorithm details, or default values asserted anywhere — none were reachable at assertion-worthy depth.

## Final Synthesis

An Outage Management System is the utility's outage-response system of record. Its defining core is exactly three jointly-held structures: the **outage event** as the persistent unit of record (opened from incoming signals, carrying affected customers, the predicted device, lifecycle state, ERT, and closing with cause codes); **signal-to-event prediction and grouping on the network connectivity model** (trouble calls — and commonly meter pings and SCADA alarms — matched against who-is-served-through-what to predict the outaged device and group related signals, with re-prediction on re-association); and the **crew dispatch and restoration loop** (crews tracked through assignment states, restoration recorded in stages updating affected-customer counts, completion feeding the reliability record). Everything else — ETR publication, customer notifications, public outage maps, AMI/SCADA integration, fault-location analysis, damage assessment, storm mode, mobile field apps, reliability indices, mutual-aid coordination, DER dispatch — is common mature or optional machinery layered on that spine. The Type's packaging spans standalone OMS products (co-op/muni pole), OMS modules composing ADMS platforms, and suite-embedded OMS products; the ADMS seam is real-time network operations, ratified from this side per the pre-hung flag. The paper-era loop satisfies the core with no software-era machinery.
