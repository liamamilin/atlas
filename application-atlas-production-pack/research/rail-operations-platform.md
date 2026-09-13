# Research Notes — Rail Operations Platform

Research date: **2026-09-09**
Leaf: Rail Operations Platform (Directory §18 Transportation, Mobility & Logistics)
Slug: rail-operations-platform

---

## Research Goal

Understand what software marketed as rail operations / rail traffic management / train control-centre / railway dispatch software actually is: who uses it, what objects exist inside it, what work flows through it, and where its boundary lies against neighboring Types — especially **Public Transit Operations Platform** (joint-review flag from that pass must be discharged from this side), **Rail Booking & Ticketing** (processed sibling), rail **EAM/CMMS**, **SCADA**, and generic **Dispatch/TMS** Types.

## Initial Boundary (hypothesis before research)

- Working hypothesis: an operator-side system for running trains — planning (timetable/rolling stock/crew) + real-time monitoring + dispatch/regulation of train movements over track infrastructure.
- Likely confusions: transit operations platforms (road/mixed), passenger ticketing (the timetable also appears there), signaling/interlocking systems (safety-critical layer beneath), rail asset management (maintaining the infrastructure vs running trains on it), generic dispatch or trucking TMS.
- Expected market structure: European vertically-separated railways (operators order train paths from infrastructure managers) vs North American vertically-integrated freight railroads (dispatch their own network) vs urban metro (ops control centres over CBTC).

## Research Questions

1. What is the unit of work — train run, train path, trip, service?
2. How is the railway network represented (tracks, stations, routes, blocks)?
3. What does the planning side hold: timetable, train paths, rolling stock circulation, crew duties?
4. What does the real-time side do: monitoring, conflict detection, regulation, disruption handling?
5. What is the dispatch "authority" surface: directives/authorities (freight), route setting (CTC), re-planning measures (passenger)?
6. How do passenger vs freight vs metro variants differ in shape?
7. Which capabilities are definitional vs merely common (resource planning? passenger information? path ordering? reporting?)

## Representative Products

| Product | Vendor | Pole in market | Why selected |
|---|---|---|---|
| IVU.rail (+ IVU.suite) | IVU Traffic Technologies (Berlin) | rail-dedicated planning + dispatch suite for passenger/freight operators, European vertically-separated market (Trenitalia, DB Regio/Fernverkehr, DSB, SBB Cargo, MTR Elizabeth line) | the shared vendor family named in the transit-ops joint-review note (IVU.rail ships as a distinct rail line beside the bus+rail IVU.suite) |
| Movement Planner + TMDS™ Train Management Dispatch System | Wabtec Corporation (Pittsburgh) | North American Class-1 freight railroad network operations + dispatch control under CTC/TWC/Dark Territory/PTC | freight-network philosophy: visualization → optimization → auto-routing, plus the dispatch/authority surface |
| Mainline / Freight / Urban Rail Control & Supervision (Operations Control Centres incl. Traffic Management) | Hitachi Rail (global signaling vendor) | turnkey control-centre TMS over ERTMS/interlocking for mainline, freight, metro | the signaling-vendor TMS pole; cross-regional |
| EAM for Rail | Trapeze (Modaxo) | the transit-suite vendor's rail line — asset management, NOT operations | boundary specimen for the joint-review seam: shows where the shared transit-suite vendor family's rail offering actually sits |

Deliberately not used: marketing-only "rail operations" pages without operational content; single-nation niche products.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- IVU — https://www.ivu.com/en/ (root: suite structure, dispatching disruption copy, train-path copy) — **reachable**
- IVU — https://www.ivu.com/en/solutions/highlights/ivurail (IVU.rail product page: train path management, personnel control centre) — **reachable**
- IVU — https://www.ivu.com/en/solutions/highlights/ivurail/integrated-rail-control-centre (integrated rail control centre: disruption management, real-time info, on-board integration) — **reachable**
- Wabtec — https://www.wabteccorp.com/ (root: Digital Intelligence nav) — **reachable**
- Wabtec — https://www.wabteccorp.com/digital-intelligence/scheduling-planning-and-optimization (family page) — **reachable**
- Wabtec — https://www.wabteccorp.com/digital-intelligence/scheduling-planning-and-optimization/movement-planner (Movement Planner) — **reachable**
- Wabtec — https://www.wabteccorp.com/digital-intelligence/signaling-and-train-control/dispatch/tmds-train-management-dispatch-system (TMDS) — **reachable**
- Hitachi Rail — https://www.hitachirail.com/ + /products-and-solutions/mainline-rail-control-supervision/ + /freight-rail-control-supervision/ + /urban-rail-control-supervision/ — **reachable** (turnkey-category pages)
- Trapeze — https://trapezegroup.com/ + /enterprise-asset-management-rail/ (EAM for Rail) — **reachable**

Access limitations (recorded per source rule):

- **Alstom** (mastria / Iconis / ops-control pages): root and category fetches returned **403 (blocked)**. European control-centre TMS pole therefore rests on Hitachi + Wabtec evidence; no Alstom-specific claims made.
- **Siemens Mobility**: rail-automation category page guess **404**; abandoned after 1 attempt (network rule). No Siemens claims made.
- **No public help centers / user manuals / operational documentation were reachable for any sampled product** — all evidence is product/solution-page level (Tier 1 help-center evidence unavailable across the sample). Consequently: **no numeric limits, no exact state vocabularies, no default values, no time windows are claimed anywhere.** All capability claims are kept at structural level; Wabtec's own published performance figures (TPC accuracy, look-ahead hours, benefit percentages) are recorded as vendor-stated figures in these notes only, not generalized.
- DuckDuckGo HTML search timed out (used direct vendor URLs instead).

---

## Product observations

### Product A — IVU.rail (IVU Traffic Technologies) — Evidence layer A (directly observed, official product pages)

Positioning: "The IVU.suite for rail transport" — "IVU.rail comprises all products of the IVU.suite with special functions for rail transport. The system maps a railway company's operational processes in their entirety… from planners to train drivers… ensuring efficiency on the rails and in the control centre." Self-described "industry-leading resource management system"; references span passenger operators (Trenitalia, DB Regio, DB Fernverkehr, DSB, MTR Elizabeth Line, Arriva Rail London, Hellenic Train) and freight (SBB Cargo).

Observed structures:

- **Suite layering for bus+rail**: IVU.suite = Service Planning / Resource Planning / Dispatching / Fleet Management / Ticketing / Passenger Information / Controlling; IVU.rail = same products **with rail-specific functions**. (This is first-hand evidence for the shared-vendor-family point in the transit joint-review note: one vendor ships a rail line beside the generic transit line.)
- **Train path management** (rail-specific highlight): "Rail transport requires long-term planning of all operational resources: Train paths need to be ordered from the network operator…" — planners view the timetable planned by the **network operator** in IVU.rail, import train paths via interfaces, order/request train paths per **TAF/TAP TSI** (European standard), track train-path history (ordered vs received, changes from infrastructure work), and an **integrated conflict model** flags "technical conflicts between a train and a scheduled train path"; adjustments transfer automatically to scheduled trains. Construction-site documents import (DB InfraGo named) and automatic construction planning.
- **Vehicle & personnel dispatch**: graphical dispatch view displays "vehicle dispatch conflicts automatically using a colour code" for "dispatch managers in the control centre"; **IVU.controlcentre Personnel Control Centre** "visually represents the assignments of your employees and visualises conflicts – anytime and in real-time", synchronized with vehicle data, "conflicts are displayed and options for resolving them are suggested. All rules such as rest times or drivers' link knowledge are considered."
- **Integrated rail control centre** (separate highlight page): "From timetable planning and dispatching to disruption management and real-time information" — a "fully integrated standard solution". Disruption sources enumerated: personnel ill at short notice, vehicle restrictions, high passenger volumes, damage to the track, decisions of the infrastructure operator. "IVU's easy-to-operate incident management provides support in the event of disruptions, with **standardised documentation in the control centre log**." Dispatch-related changes "automatically pass… to the trains – keeping the drivers up to date"; on-board software monitors communication, vehicle state, connections; **passenger load display** for dispatch managers and passengers; real-time information distributed "on all channels – from the bus stop display to websites and apps to the data hubs."
- Customer quotes confirm daily work shapes: duty scheduling/dispatch standardization, planning train journeys and staff workload, "respond to disruption quickly" (Arriva Rail London), "dispatch all of our employees consistently and efficiently using a single system" with train crew supervisors/drivers/station staff (Keolis Downer).

### Product B — Wabtec Movement Planner + TMDS — Evidence layer A (directly observed, official product pages)

Positioning (family page): "Tools to optimize rail operations… Optimize mainline network, yards, and intermodal terminals so railroads can move goods faster, cheaper and on time… From deciding routes, to considering operating conditions, to selecting assets, to assigning crews, to factoring in yard operations… Wabtec's Scheduling, Planning, and Optimization solutions provide real-time visibility and optimization to help busy railroads stay on schedule and recover from disruptions faster."

**Movement Planner** ("optimize railroad day-of-operations from planning through execution"), three tiered capabilities:

- **Network Visualization**: "helps detect conflicts in the entire network and allows for manual resolution of conflicts. It gives real-time train status and uses a Train Performance Calculator (TPC) to model train travel time with an accuracy of +/- 5 minutes for a 2-hour horizon. It also generates a look ahead forecast of 8 to 12 hours to better plan for crew call and asset allocation." (figures vendor-stated)
- **Network Optimization**: "automated train **meet/pass** resolution based on Business Objective Functions (BOF) with a reliable and stable plan… reduced variability of dispatching decisions."
- **Auto-Routing**: "automatic execution of optimized plans… improves plan compliance."
- Benefit claims (vendor-stated, Class-1 railroad): network velocity +10%, expired crews −50%, capacity, schedule adherence/OTP.

Related family: **Service Design Schedule Viewer** ("simulation tool… predicted rail traffic performance… to drive optimal operating plans"), **Yard Planner**, **OASIS** (intermodal terminal TOS — adjacent, terminal-domain), **Precision Dispatch System**.

**TMDS™ Train Management Dispatch System** — "Comprehensive dispatch and back office control"; "an integrated dispatch control solution that brings together multiple dispatching functions for **Centralized Traffic Control (CTC), Track Warrant Control (TWC), Dark Territory (DT), and Positive Train Control (PTC)** into one system for efficient train management."

- **TMDS Computer-Aided Dispatch (CAD)**: "provides the **generation and management of all mandatory directives**, management of train operational data, and the presentation layer for train management/control." Sub-capabilities listed: presentation layer for traffic management / business rules / safety-conflict mitigation / resolution; **mandatory directive management (authority/restriction management)**; train information management; **signal system interfaces (SCADA)**; business management information interfaces; special system interfaces (weather, earthquake, CIS, web, PTC); business analysis reporting (**velocity, train schedule adherence, GTM**); **auto-routing** (tactical execution, schedule- or priority-route-based).
- **Back Office Server**: initialization/management/delivery of datasets ("authorities, bulletins, train-consist") to the I-ETMS locomotive segment; MDM distributes track databases; IVOC independently validates completeness/correctness of mandatory directives.

### Product C — Hitachi Rail Control & Supervision (Mainline / Freight / Urban) — Evidence layer A for positioning, thin on objects (turnkey category pages)

- Mainline: "Operations Control Centres including **Traffic Management and network optimisation** for conventional and ERTMS systems" listed inside a full-system offering spanning ERTMS/ETCS signalling, interlocking, ATO, telecoms, driver advisory. "signalling and traffic management systems that can span seamlessly across national borders."
- Freight: "Operational Control Centres including Traffic Management and network optimisation", "Positive Train Control and **Temporary Speed Restriction Management**", autonomous freight (GOA4); heritage: Union Switch and Signal (1881).
- Urban (metro/tram): "Smart Rail Operation Systems including **Operations Control Centre**, Automatic Train Stop & SCADA"; CBTC context.
- Structurally: the TMS/OCC is one pillar of a signaling+rolling-stock turnkey portfolio — the ops platform sits **above** interlocking/ATP, consuming and commanding via interfaces. Object-level detail not published on these pages (recorded as limitation; no object claims drawn from Hitachi).

### Product D — Trapeze EAM for Rail — Evidence layer A (boundary specimen)

The transit-suite vendor's rail line is **Enterprise Asset Management**: "real-time information on the health of your assets – from rolling stock and stations, to track and wayside equipment". Capabilities: rolling stock/track/signals/power/structures hierarchies; "In the Yard: plan, build, and cut your **consist** to prepare for service… identified defects trigger service requests, work orders, or flagging vehicles to pull from service… manage vehicle status and maintenance holds"; **linear reference system** for track work (segments, markers, offsets), track defects and inspections, "manage and clear **speed restrictions and slow zones**"; FTA/FRA compliance; PTC firmware compliance checks.

Interpretation: this is maintenance-of-asset semantics (work orders, inspection cycles, defect clearance), not train-running semantics (no timetable-of-trains, no live train running, no movement authority). Strong boundary evidence: the shared vendor family touches rail on the **asset** side; running trains is the other Type.

---

## Cross-product Comparison

| Dimension | IVU.rail (passenger/freight operator, EU) | Wabtec MP+TMDS (freight railroad, NA) | Hitachi OCC/TMS (signaling vendor) | Trapeze EAM Rail (boundary specimen) |
|---|---|---|---|---|
| Planned unit of work | train / trips bound to ordered **train paths** from network operator; timetable planning | operating plans; look-ahead plan; movement/plan compliance (train as moving unit; meets/passes) | traffic management over timetable within OCC turnkey | — (assets, work orders) |
| Network representation | train paths + conflict model train↔path; construction-site changes; infrastructure manager as path authority | network-wide conflict detection; track databases distributed to locomotives; routing | conventional + ERTMS network; interlocking beneath | linear asset hierarchy (segments/offsets) |
| Real-time running | graphical dispatch view; vehicle & personnel dispatch conflicts color-coded; real-time sync vehicle↔personnel | real-time train status; TPC travel-time model; conflict detection entire network | OCC real-time supervision (positioning-level only) | real-time vehicle status/location **for maintenance readiness** |
| Direction of movements (authority surface) | dispatch measures in disruption management; changes pushed to drivers/on-board; control-centre log | **mandatory directives** (authority/restriction management); meet/pass resolution; auto-routing execution; CTC/TWC/DT/PTC methods | traffic management commands within OCC (positioning-level) | — |
| Resource planning | vehicle working scheduling; duty/crew scheduling + personnel control centre; optimisation | crew call planning (look-ahead), asset allocation, train-consist datasets | — (not on category pages) | consist build in yard (pre-service preparation) |
| Disruption handling | incident management + standardized control-centre log; re-planning | "recover from disruptions faster"; manual conflict resolution → optimization → auto-routing | — | defect-triggered holds (asset side) |
| Passenger information | integrated: dispatch → on-board + station/web/app channels; passenger load display | — | — | — |
| Reporting | punctuality/efficiency via Controlling | velocity, train schedule adherence, GTM reporting | — | KPI dashboards (asset) |
| Interfaces beneath | on-board systems; data hubs; TAF/TAP TSI to infrastructure manager | signal system interfaces (SCADA), PTC office segment, weather/earthquake/CIS/web | interlocking, ETCS, SCADA, CBTC | maintenance systems |
| Vertical-market realization | vertically-separated EU market (path ordering external) | vertically-integrated NA freight (no external path authority) | both (global, turnkey) | NA transit agencies |

Stable cross-product reading (B-layer commonality): every genuine member of the Type couples (1) a **planned service over the track network** with (2) **live train running** against that plan and (3) an **authority/decision surface** through which operators direct movements — and the freight realization expresses (3) as mandatory directives + meet/pass + routing while the passenger-EU realization expresses it as dispatch measures over train-path conflicts pushed to drivers and the control-centre log.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The Type is recognizable only when **all three** of these are held together:

1. **The planned train service as the unit of work, bound to the railway network.** A timetable/plan of train runs over the track topology (paths, routes, stations), maintained as the system's plan of record. Remove the track-network binding → generic dispatch/scheduling; remove the plan → blind tracking.
2. **Real-time knowledge of train running against the plan.** Current position/status of trains on the network, continuously compared with the plan so deviations and conflicts surface (train-vs-path conflicts, network-wide conflicts, delay). Remove → a planning tool with no day-of-operations, or a passive feed.
3. **Operational authority over train movements.** The system is the medium through which operators direct the running railway — recorded control decisions/directives that change or govern movements (route/routing execution, movement authorities/restrictions, meet/pass and re-timing/re-planning measures, disruption instructions) and the control-centre record of them. Remove → an analytics/monitoring dashboard, the "operations" gone.

Jointly-held is load-bearing:

- 1 alone = timetable/scheduling software (planning tool)
- 2 without 1 = blind train tracking (generic AVL)
- 3 without 1+2 = a paper directive machine with no running picture
- 1+2 without 3 = visibility without control (monitoring dashboard)
- 1+3 without 2 = plan + paperwork, no live railway
- 2+3 without 1 = point control with no service plan to keep

**Anti-overfit check (shared-implementation rule):** the European **train-path-ordering** machinery (TAF/TAP TSI, network-operator path authority) is *not* in L0 — it is the European vertically-separated realization of leg 1; the North American freight realization holds the same leg without any external path authority (Wabtec: operating plans + network conflict detection, no path ordering). Likewise **auto-routing/optimization** is not in L0: manual conflict resolution is a documented first-class mode (Wabtec Network Visualization "allows for manual resolution"; IVU dispatch managers intervene on flagged conflicts). The invariant is the decision surface, not its automation.

### L1 — Common Mature Structure

Present across the mature sample but not required to recognize the Type:

- **Rolling stock planning** — vehicle/consist circulation matched to the timetable (IVU vehicle working scheduling; Wabtec asset allocation + train-consist datasets; Trapeze-yard consist build sits on the asset side of the seam).
- **Crew/duty planning and dispatch** — duties, rosters, qualifications and rest rules; personnel control centre synchronized with vehicle state (IVU; Wabtec crew-call look-ahead; "expired crews" benefit metric).
- **Conflict detection and re-planning support** — automated conflict models over plan+network with suggested resolutions (IVU conflict model; Wabtec network conflicts → optimization).
- **Integration with the signalling/safety layer** — the platform commands via interlocking/CTC/SCADA/PTC interfaces; safety-critical enforcement remains in that layer (Wabtec signal-system interfaces; Hitachi turnkey framing; I-ETMS datasets).
- **Disruption/incident management with a control-centre log** — standardized documentation of the operational response (IVU incident management).
- **Operational reporting** — schedule adherence/OTP, velocity, punctuality (Wabtec business analysis reporting; IVU punctuality framing in customer copy).
- **Passenger information distribution** (passenger-market products) — dispatch changes pushed to on-board/station/web/app channels (IVU).

### L2 — Variant / Optional Structure

Depends on market, segment, deployment:

- **Market regime**: vertically-separated Europe — train-path ordering from the infrastructure manager, external construction-site data, TAF/TAP TSI interfaces (IVU) ↔ vertically-integrated freight North America — dispatcher owns the network, methods of operation CTC/TWC/Dark Territory/PTC (Wabtec).
- **Segment shape**: passenger (connections, passenger load, public real-time info) / freight (meet/pass economy, yard and terminal planning — Yard Planner, intermodal TOS as adjacent products) / metro (ops control centre over CBTC, driverless operation).
- **Planning-side simulation** — service-design simulation of predicted traffic performance driving operating plans (Wabtec Service Design Schedule Viewer).
- **Temporary speed restriction management** as operational machinery in the ops stack (Hitachi freight page) — while *clearing* restrictions via maintenance workflows is EAM-side (Trapeze).
- **On-board/mobile driver integration** — dispatch-to-driver updates, on-board software (IVU; Wabtec PTC locomotive segment is the safety-layer twin).
- **Deployment**: integrated suite (planning→dispatch→info in one product family) vs control-centre TMS as one pillar of a signaling turnkey portfolio vs optimization overlay on an existing dispatch system (Movement Planner "tiered capabilities" atop a railroad's operations).

### L3 — Vendor-specific (Research Notes only)

- Wabtec: the three-tier Movement Planner decomposition (Network Visualization / Network Optimization / Auto-Routing); TPC accuracy "±5 minutes for a 2-hour horizon"; look-ahead "8 to 12 hours"; benefit figures (+10% velocity, −50% expired crews — "results vary"); TMDS module names (CAD/BOS/MDM/IVOC/NMS/Admin Tools); "GTM" reporting; methods-of-operation naming (CTC/TWC/DT/PTC).
- IVU: product naming (IVU.rail, IVU.suite products, IVU.pad, IVU.cloud, IVU.controlcentre personnel control centre), TCM train-building messages roadmap note, DB InfraGo construction-document import, brochure set.
- Hitachi: turnkey category taxonomy (Mainline/Freight/Urban Control & Supervision), GOA4, Shift2Rail founding membership, Union Switch & Signal heritage, HMAX asset management as sibling pillar.
- Trapeze: EAM-for-Rail feature names (linear reference system, consist cutting, FRA blue-card, TAM/NTD reports).

---

## Vendor-specific Findings

- The freight "mandatory directives" machinery (authority/bulletin management, independent validation of directives) is currently observed only at Wabtec TMDS — it is the NA freight regulatory/method-of-operation realization of L0-leg 3, not a generic feature claim.
- IVU's train-path ordering/import via TAF/TAP TSI and infrastructure-manager integration is a European-market realization; no claim that other markets implement path ordering the same way.
- Passenger-information integration depth (dispatch → passenger channels with load display) observed only at IVU in this sample — held as passenger-market common/optional, not definitional.

## Boundary Findings

1. **vs Public Transit Operations Platform (§18 sibling) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED.**
   The transit pass flagged the shared vendor families and proposed an object-of-work seam; this pass's independent evidence confirms it at center-of-gravity strength:
   - *Object of work*: transit ops centers the **agency's scheduled passenger service delivery** across road/mixed modes (routes/patterns/stops/trips; vehicles and crews against the plan). Rail ops centers **train running over railway infrastructure** — the planned unit is the train run bound to train paths/track topology; the distinctive machinery is track-occupancy-shaped (path conflicts, meet/pass, route setting, movement directives).
   - *First-hand vendor-family evidence from this side*: IVU itself ships one suite for bus+rail (IVU.suite) with IVU.rail as the distinct rail line whose named rail-specific feature is exactly the track-bound machinery (train path management, train↔path conflicts, rail crew dispatch). Trapeze — the other shared family — touches rail only via **EAM for Rail** (asset maintenance), i.e., not via a transit-ops-style rail operations product at all in this sample.
   - *Removal test both directions*: strip the track-bound train-running machinery from a rail ops platform → a generic transit/fleet ops loop (transit territory). Strip passenger-service delivery semantics from a transit ops platform → nothing meaningful remains, because that is its object. The seam holds; two Types.
2. **vs Rail Booking & Ticketing (processed sibling)**: the timetable appears in both but with opposite polarity — sellable inventory priced under a fare system with ticket lifecycle vs the operator's plan of work with running authority. Commerce surface (traveler, purchase, ticket) vs operations surface (dispatcher, plan, directives). Clean seam, consistent with that pass's own boundary.
3. **vs Rail EAM / CMMS (Enterprise Asset Management, §16 sibling)**: Trapeze EAM for Rail as specimen — maintenance of rolling stock/track/signals/power (asset hierarchies, work orders, defect inspections, linear referencing, restriction *clearing*) vs running trains on those assets (plan, live running, movement decisions). Overlap zone: pre-service yard/consist preparation and speed-restriction bookkeeping appear on both sides of the seam; center-of-gravity differs. Keep both.
4. **vs SCADA / DCS / signaling (§16 siblings)**: the safety-critical control layer (interlocking, ATP/PTC, SCADA for traction power etc.) enforces safe separation; the rail ops platform **sits above it** and commands through interfaces (Wabtec: "Signal System Interfaces (SCADA)"; Hitachi: TMS inside a signaling turnkey). The ops platform's objects are trains/services/directives, not physical process variables or field devices. SCADA may even be listed as a subsystem *inside* an OCC offering (Hitachi urban page) — bundling, not identity.
5. **vs Transportation Management System (TMS, §10) / Freight Brokerage (§18)**: trucking-freight logistics semantics (shipments, carriers, rates) vs train-running semantics. Wabtec's own catalog separates "Transportation Management" (Port Optimizer etc.) from "Scheduling, Planning & Optimization" and "Signaling & Train Control" — vendor-drawn internal seam corroborates.
6. **vs generic Dispatch Management (§18)**: generic dispatch assigns people/vehicles to jobs; rail dispatch directs trains through a capacity-constrained, safety-enforced track network under a published service plan. The track binding + movement authority make the difference.
7. **Sibling note (same §18 family)**: Airline Operations Platform / Airport Operations Platform / Port Terminal Operating System / Vessel Operations Platform are domain parallels (plan + live running + ops control in their domains); rail is distinguishable by track-bound capacity and the signalling/authority machinery, but the family pattern (plan-of-work + operations loop) is shared.

## Uncertainties

- **European control-centre TMS pole under-sampled**: Alstom unreachable (403), Siemens abandoned after one 404. The TMS-from-signaling-vendor pole rests on Hitachi's turnkey category pages, which do not publish object-level detail. Mitigation: no object-level claims drawn from Hitachi; freight dispatch pole (Wabtec) and operator-suite pole (IVU) carry the object model.
- **No help-center/user-manual tier reached for any sampled product** → no numeric limits, no exact state vocabularies (planned/rostered/actual…), no default timings asserted; all states written conceptually.
- Whether infrastructure-manager-side traffic management (national control centres managing *capacity and network* rather than an operator's trains) belongs in this Type or deserves a separate leaf is **not fully resolved** from reachable evidence: Hitachi/Wabtec sell OCC/TMS to infrastructure owners and railroads alike, and the L0 triad (plan+running+authority) holds for both postures. Recorded as a possible future refinement, not asserted either way.
- Exact boundary of "platform" vs the underlying dispatch *system* (TMDS-class) is packaging: Movement Planner is an optimization overlay atop a dispatch system; IVU.rail bundles planning+dispatch. Treated as variant axes (overlay vs suite vs turnkey pillar), not Type splits.

## Final Synthesis

A **Rail Operations Platform** is the rail operator's or infrastructure manager's operations-control system of record for running trains: it holds the **planned service over the track network** (timetable/train runs bound to paths, routes and stations), tracks **real-time train running** against that plan, and provides the **operational authority surface** through which dispatchers and control centres direct movements — route/routing execution, movement authorities and restrictions, meet/pass and re-planning decisions, disruption handling with a logged operational record. Mature products wrap this core with rolling-stock and crew planning/dispatch, automated conflict detection and optimization advisories, integration with the interlocking/PTC/SCADA safety layer, operational reporting, and — in passenger markets — real-time passenger information. The Type's market realization splits along regime (vertically-separated Europe with external train-path ordering vs vertically-integrated freight North America with directive-based dispatch under CTC/TWC/Dark Territory/PTC) and segment (mainline passenger / freight / metro), but the plan+running+authority triad is the recognizable constant, and it survives the historical check: timetable-and-train-order dispatching with a train sheet and dispatcher-issued orders — later CTC panels — satisfies all three legs with no modern machinery.
