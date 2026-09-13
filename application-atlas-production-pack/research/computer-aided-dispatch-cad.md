# Research Notes — Computer-aided Dispatch / CAD

Research date: 2026-09-07
Slug: computer-aided-dispatch-cad
Directory leaf: Computer-aided Dispatch / CAD (§24 Government, Public Sector & Civic)

---

## Research Goal

Understand what a Computer-aided Dispatch (CAD) application actually is as a software type: its core objects, the real-time workflow it supports, the interfaces its users operate, the rules that govern it, and where its boundary sits against neighboring types (records management, emergency management, commercial dispatch, call handling).

## Initial Boundary (pre-research hypothesis)

- CAD = real-time incident + resource management for dispatch operations; strongest sense is public-safety 911/112 dispatch (police, fire, EMS).
- Neighbors: Police Records Management System (post-incident records), Emergency Management Platform (EOC-level, multi-event), Fire Department Records / EMS Operations Platform (records/ePCR downstream), Taxi Dispatch Platform / Towing Dispatch Platform / Dispatch Management (§18, commercial dispatch siblings), On-call Management (scheduling, not dispatching), Contact Center Routing (agent routing, no field units).
- Known acronym collision: "CAD" also means Mechanical CAD (§16). Directory disambiguates by full name; no taxonomy action needed.
- Risk: over-fitting the definition to the modern US NG911 PSAP pattern; must survive the historical check (1970s–80s text-terminal CADs, non-US 112/999 centers, non-emergency dispatch operations).

## Research Questions

1. What is the core object model? (call/event → incident → unit → assignment → status → closure)
2. How does a call for service enter the system and become an incident?
3. What is a "unit"? How is status modeled and who updates it?
4. How does dispatch recommendation work (proximity, priority, response plans, traffic)?
5. What interfaces exist (call-taking, dispatch console, map, mobile field client, supervisor, admin, reporting)?
6. How does CAD connect to emergency call handling (E911/NG911), GIS, AVL, and records systems?
7. What rules matter (priority, jurisdiction, status discipline, audit, human-in-the-loop, resilience)?
8. What exceptions are structural (duplicate calls/merge, escalation, mutual aid, failover)?
9. What variants exist (discipline scope, emergency vs non-emergency workload, deployment, scale)?

## Representative Products

Selected for market representation + different product philosophy + different customer tier + documentation accessibility:

| Product | Vendor | Pole |
|---|---|---|
| Mark43 CAD | Mark43 | cloud-native multi-discipline CAD (law/fire/EMS), modern entrant, automation-forward |
| PremierOne / Flex / CommandCentral CAD | Motorola Solutions | enterprise incumbent, PSAP-centric, full command-center suite |
| ZOLL Dispatch | ZOLL Data Systems | EMS/ambulance-specialist CAD, transport-operations oriented |
| Public Safety Suite CAD (+ Vertex NG911, Unify) | CentralSquare | public-sector suite incumbent, call-handling + CAD + records family |

Additional major vendors acknowledged but not documented in this pass (official surfaces unreachable): Hexagon (public safety CAD), Tyler Technologies (Enterprise CAD). No claims made about them.

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

1. Mark43 homepage — https://mark43.com/
2. Mark43 CAD product page — https://mark43.com/platform/cad/
3. Motorola Solutions NG911 software page (incl. RapidDeploy-branded landing) — https://www.rapiddeploy.com/ (redirects to Motorola NG911 page)
4. Motorola Solutions "Voice & computer-aided dispatch" page — https://www.motorolasolutions.com/en_us/products/command-center-software/public-safety-software/voice-and-computer-aided-dispatch.html
5. ZOLL Data Systems homepage — https://www.zolldata.com/
6. ZOLL Dispatch product page — https://www.zolldata.com/ems-fire/dispatch
7. CentralSquare homepage — https://www.centralsquare.com/
8. CentralSquare Public Safety & Justice solutions page — https://www.centralsquare.com/solutions/public-safety-software

### Source-access Limitations

- Wikipedia (Computer-aided dispatch) — timed out twice; abandoned. No third-party encyclopedic cross-check.
- Hexagon main site and Hexagon safety-infrastructure site — 403 / timeout; abandoned. Enterprise-incumbent pole covered via Motorola instead.
- Tyler Technologies product page — 403; abandoned.
- Mark43 Help Center (get.mark43.help) — Salesforce Lightning app, JS-rendered, returns CSS Error; no operational help articles reachable.
- ZOLL Dispatch Solution Overview PDF — binary PDF, not parseable; abandoned.
- Motorola PremierOne CAD detail page — not fetched (page tree reached only to the CAD overview level).

Consequence (evidence calibration): all product-specific claims below are anchored to the fetched pages (Layer A). Cross-product claims are Layer B over the four fetched vendors. No precise numeric limits, uptime percentages, status-code vocabularies, or timing windows are asserted anywhere, because no source at that precision was reachable. Model-memory knowledge of specific status codes / protocol integrations (e.g., EMD ProQA linkage) is NOT used to fill gaps; such items are listed under Uncertainties instead.

---

## Product A — Mark43 CAD

Source: mark43.com/platform/cad/ (Tier 2 official product page). Evidence layer: A (directly observed on page).

### Key observations

- Self-description: "Modern, cloud-native CAD for law enforcement, fire, and EMS — connects teams, strengthens resilience, and simplifies call intake, dispatch, and field work."
- "Cloud-native, multi-discipline system that unifies call intake, recommendations, and unit coordination across law, fire, and EMS."
- Value framing: "Dispatch is mission-critical and time-sensitive."
- Automation posture: "pairing predictive impact analysis with automated response plan execution and human-in-the-loop controls — so agencies move faster... while experienced dispatchers remain firmly in control."
  - "Intelligent Plan Builder": "Input dozens of plain-language rules grounded in policy, compliance, union agreements, and best practices; Mark43 generates comprehensive response plans automatically." "Predictive impact modeling — see how rule changes will affect staffing, unit recommendations, coverage, and response performance — before you publish." "Transparent, auditable logic."
  - "Automated Response Engine (Human-in-the-Loop)": "Execute response plans automatically from event inputs, with clear checkpoints for confirm/change/veto." "Keep experienced dispatchers and supervisors in control."
- Integration posture: "Connect the tools and data your teams depend on — maps, telephony, sensors, records, analytics, and more."
- Communications: "Keep dispatchers connected in real-time with responders in and out of their units."
- Multi-agency: "supports multi-agency law, fire, and EMS operations"; customer story: Camden County "breaks down silos between police and fire dispatch... dispatchers now share the same operational picture."
- Open API: Elk Grove PD uses "Mark43 CAD's open API to enable seamless integrations — including drones as first responders."
- Platform context: CAD is one module of a suite with RMS, Booking, OnScene (field), Insights (analytics) — "from the first call to the final report."
- Also ships "Mark43 Alternate CAD" (a separate product page exists; not fetched — likely a front-end for agencies keeping a legacy CAD; recorded as vendor-specific, unverified detail).
- Segments: law enforcement, dispatch, federal (FedRAMP High), campus, port and transportation, UK.

## Product B — Motorola Solutions CAD (PremierOne / Flex / CommandCentral CAD)

Sources: motorolasolutions.com voice-and-computer-aided-dispatch page + NG911 page (Tier 2). Evidence layer: A.

### Key observations

- Vendor's own definition (FAQ): "Computer aided dispatch software is a digital interface that manages the succession of an emergency call, from the initial 9-1-1 call to the final resolution on the scene."
- How it works (FAQ): "identifies a caller's location and incident details the moment a 9-1-1 call comes in, prioritizes the call based on severity and dispatches the nearest available field units in seconds."
- Key-features list (vendor-curated, cross-cutting):
  - Real-time reporting and analytics: "incident trends, response times and resource utilization."
  - Unified command experience: "a single interface consolidating 9-1-1 call data, dispatch controls and responder locations."
  - Intelligent mapping and routing: "integrated GIS to identify the nearest available units and optimize response routes."
  - Dynamic resource management: "real-time tracking of unit availability, status and location across jurisdictions."
  - NG911 integration: "support for calls, texts and multimedia from NG9-1-1 systems."
  - Seamless record integration: "automatic data transfer from CAD to records management systems to reduce duplicate entry."
- Product family: PremierOne ("large-scale incident response coordination with speed and maximum configuration"), Flex ("built for a single or multiple jurisdictions"), CommandCentral CAD ("modern cloud CAD"), Rave Link ("share information easily when an incident response requires multiple jurisdictions and disparate teams"), Avtec Scout / CommandCentral AXS (voice dispatch consoles — adjacent, voice not incident management).
- Discipline pages: "CAD for law enforcement PSAPs — pinpoint callers with integrated GIS tools and route the nearest available unit within the service area... surfacing historical hot hit records and providing digital maps to field personnel, delivering a unified operational view from call to case closure." "CAD for fire and EMS PSAPs — locate and dispatch the most appropriate units through highly configurable databases... manage complex incident data in real time, even during large-scale events or natural disasters."
- NG911 ecosystem page: call handling (VESTA NXT / VESTA 911) is a separate product family from CAD (PremierOne, Flex). FAQ: "emergency call handling software such as VESTA NXT and computer-aided dispatch software such as PremierOne or Flex."
- NG911 concept: "NG911 enables the digital transfer of incident information with Emergency Incident Data Object (EIDO) exchange. EIDO allows receiving PSAPs to access and share critical incident details between public safety platforms (CAD, call handling, etc.)... rather than relying on verbal relay." E911 vs NG911: "E911... could show a dispatcher your phone number and location... essentially a 'voice-only' system. NG911 treats emergency calls like data, allowing you to send photos, videos and texts directly to dispatchers."
- Non-emergency extension: PremierOne CSR ("service request management") exists as a separate module.

## Product C — ZOLL Dispatch

Source: zolldata.com/ems-fire/dispatch (Tier 2). Evidence layer: A.

### Key observations

- Self-description: "the intelligent EMS and ambulance call taking and computer-aided dispatch (CAD) solution."
- Core problem framing: "Quickly getting the right level of care (BLS, ALS, etc.) to patients... align response with transport need and to optimally position vehicles."
- Recommendation logic: "ranking available resources based on proximity, real-time traffic, and road closures. Tap real-time situational analysis capabilities to select the fastest, most appropriate (BLS, ALS, etc.) vehicle."
- Map-centric posture: "map-centric fleet monitoring to monitor your service area and the locations and status of your entire fleet and incidents in progress in a single view."
- Assignment transmission: "automatically communicates response assignments to appropriate units, minimizing delays."
- Positioning/stacking: "use real-time information to support at-post positioning decisions" (dynamic deployment for EMS).
- Mobile companion: ZOLL Respond app (Android/iOS): "view, respond, and receive turn-by-turn routing guidance to trip pick-up and drop-off points... automatically transferring data between dispatch and crews in the field."
- Non-emergent workload: "efficient, cost-effective resource utilization for emergent and non-emergent transportation (NEMT)"; Mobile Care Connect module: "request, queue, deploy and manage non-emergency, inter-facility services — all in a dedicated queue."
- Scheduling: "intelligent estimated time of arrival (ETA) and available resource ranking"; "schedule patient transport requests."
- Downstream integration: "integrates with our cloud-based billing and ePCR solutions, ZOLL Billing and ZOLL emsCharts"; "4 data fields dispatch must get right for billing success" (dispatch data feeds billing).
- Deployment: "Accessible from a web browser, eliminating on-premises server maintenance and disaster risk"; "enables remote dispatching"; "cloud-based software, also known as SaaS."
- Data access: "Direct Data Access" for analytics.

## Product D — CentralSquare Public Safety Suite (CAD + Vertex NG911 + Unify)

Sources: centralsquare.com homepage + public-safety solutions page (Tier 2). Evidence layer: A.

### Key observations

- Suite structure: Public Safety Suite in three tiers (Enterprise / Pro / ONESolution) covering call handling, CAD, records, jail; plus separate products: Vertex NG911 Call Handling, Unify (CAD-to-CAD), Centerline AI.
- Customer framing (East Baton Rouge): "a seamless experience from the 911 caller to the dispatcher to the officer in the field" — call handling → CAD → field chain named explicitly.
- Multi-agency scale: Fairbanks ECC "improving coordination across 22 agencies."
- Mapping emphasis (Edgar County): "significantly improved their mapping accuracy, providing dispatchers faster, clearer location information that leads to more efficient call handling and response."
- CAD-to-CAD interoperability: "Unify™ (CAD-to-CAD)" is a named product category — interconnecting disparate CAD systems across jurisdictions.
- Emerging integration: "CAD-to-Drone-as-First-Responder (DFR) Integration" with Skydio: "One connected workflow — from dispatch to drone launch to case file."
- Cloud posture: "1,000 cloud deployments" press milestone; cloud benefits brochure; "continuity against natural disasters and cyber threats."

---

## Cross-product Comparison

| Dimension | Mark43 | Motorola CAD family | ZOLL Dispatch | CentralSquare |
|---|---|---|---|---|
| Call/event intake | "call intake" unified in CAD | 911 call data consolidated into CAD; NG911 calls/texts/multimedia | "call taking" for EMS/ambulance; NEMT request queue | 911 caller → dispatcher chain; Vertex call handling adjacent |
| Incident as tracked object | implied via events/incidents; "same operational picture" | "manages the succession of an emergency call... to final resolution"; incident management workflows | "incidents in progress" on map; trip lifecycle | incident data real time during large-scale events (via family framing) |
| Unit inventory + real-time status | "unit coordination", "responder status" | "real-time tracking of unit availability, status and location across jurisdictions" | "locations and status of your entire fleet" | coordination across agencies (suite framing) |
| Assignment / dispatch act | recommendations + automated execution with confirm/change/veto | "dispatches the nearest available field units" | "automatically communicates response assignments to appropriate units" | dispatch within suite |
| Recommendation logic | response plans from rules; predictive impact | nearest available unit via GIS/GPS; severity prioritization | ranking by proximity, real-time traffic, road closures; BLS/ALS capability | mapping accuracy → faster location (indirect) |
| Map/GIS | maps listed as integration | integrated GIS, digital maps to field | map-centric single view | mapping accuracy emphasized |
| Mobile field client | "responders in and out of their units" | digital maps to field personnel | ZOLL Respond app with turn-by-turn routing | "officer in the field" chain |
| Multi-agency / cross-jurisdiction | multi-agency law/fire/EMS; shared picture | Flex multi-jurisdiction; Rave Link | mutual-aid blog reference (weak) | 22-agency ECC; Unify CAD-to-CAD |
| Records integration | unified platform with RMS | "automatic data transfer from CAD to records management" | ePCR (emsCharts) + billing integration | suite includes RMS/JMS |
| Non-emergency workload | (not evidenced) | PremierOne CSR module | NEMT / inter-facility dedicated queue | (not evidenced) |
| Deployment | cloud-native | on-prem + cloud (CommandCentral CAD, VESTA NXT cloud) | cloud SaaS, browser, remote dispatch | cloud tiers, 1,000 cloud deployments |
| Resilience framing | "cloud-native availability... even in extreme situations" | large-scale events / natural disasters | "eliminating... disaster risk" | "continuity against natural disasters and cyber threats" |
| Automation posture | explicit human-in-the-loop automation engine | traditional dispatcher-driven (automation not claimed on fetched pages) | ranking/ETA decision support | AI suite-level (Centerline AI) |

### Layer-B findings (cross-product commonality, 4/4 or strong 3/4)

1. Service requests enter as discrete events and become tracked incidents (all four).
2. A dispatchable unit inventory with real-time status is maintained (all four).
3. The system recommends and/or executes unit-to-incident assignment; a human dispatcher role exists in all framings (all four).
4. Map/GIS is a primary working surface, not a decoration (all four).
5. A mobile/field client closes the loop back to the center (all four).
6. Multi-agency / multi-jurisdiction operation is a first-class concern (all four; strongest at Motorola/CentralSquare).
7. Downstream records integration is standard (all four, different targets: RMS / ePCR / billing).
8. Emergency call handling is an adjacent, distinct system that feeds CAD (Motorola explicit; CentralSquare explicit; Mark43 lists telephony as integration; ZOLL folds call-taking in for EMS).
9. Cloud deployment is the current market direction (all four; incumbents retain on-prem lines).
10. Resilience/availability is a first-class marketing and design concern (all four).

### Layer-C canonical inference

The Type is best modeled as: **real-time coordination between a stream of service-request incidents and a fleet of status-tracked response units, with system-recommended, human-governed assignment, maintained as a live operational picture.** Everything else (911 integration, GIS, AVL, mobile apps, records feeds, cloud) is implementation or maturity layer.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **Service-request intake as incidents** — requests for service enter as discrete, tracked incident records (location, nature, priority, timeline).
2. **Dispatchable unit inventory with real-time status** — the system maintains the set of response units and their current status/location state.
3. **Unit-to-incident assignment** — the dispatch act: binding unit(s) to incident(s), whether dispatcher-executed or system-executed-with-confirmation.
4. **Live operational picture** — the above are maintained and presented as current state (status board + map), not as after-the-fact records.

Removal test: remove intake → fleet tracker/AVL only; remove unit status → call log (RMS territory); remove assignment → tracking board, not dispatch; remove real-time posture → records management. All four are required.

Historical check (§24): 1970s–80s text-terminal CADs (no AVL, no GIS map, single agency, no NG911) satisfy all four — status was manually updated, the board was the picture. Non-US 112/999 centers, private EMS dispatch, campus/port dispatch also satisfy all four. The definition is not over-fitted to the modern US NG911 cloud pattern. NG911, GIS, AVL, cloud, mobile apps are all later additions → L1/L2.

### L1 — Common Mature Structure

- Emergency-line integration (call handling handoff, caller number/location delivery; NG911 multimedia/EIDO in current-generation products)
- GIS map with geocoded addressing as a primary surface
- Priority/severity classification driving queue order and recommendation
- Unit recommendation engine (proximity, capability, availability; traffic/road-closure inputs at some products)
- AVL / GPS unit location
- Mobile field client (assignments out, status/messages/data back)
- Incident timeline / audit trail (public-safety records context)
- Multi-agency / multi-jurisdiction operation; CAD-to-CAD interoperability gateways
- Downstream records integration (RMS, ePCR, billing)
- Reporting/analytics (response times, unit utilization, incident trends)
- Supervisor functions (monitoring, reassignment, escalation)
- Resilience posture (redundancy, failover, remote dispatch capability)

### L2 — Variant / Optional Structure

- Discipline scope: law-only / fire-only / EMS-only / consolidated multi-discipline center
- Emergency vs non-emergency workload: 311-style service requests (CSR modules), NEMT / inter-facility transport queues
- Deployment: on-premises vs cloud-native (and hybrid backup)
- Customer scale: single agency vs regional consolidated center (dozens of agencies)
- Adjacent-domain CAD deployments: campus, port/transportation, private EMS, federal — same core, different governance
- Emerging integrations: drone-as-first-responder, sensor/video feeds, AI assistance (era-common)
- Automation depth: dispatcher-driven vs rule-driven response-plan execution with human checkpoints

### L3 — Vendor-specific (research notes only)

- Mark43: Intelligent Plan Builder, Automated Response Engine (confirm/change/veto checkpoints), predictive impact modeling, Alternate CAD product, open-API drone integration story, FedRAMP High federal line.
- Motorola: PremierOne (large-scale/max configuration) vs Flex (single/multi-jurisdiction) vs CommandCentral CAD (cloud) product ladder; Rave Link cross-jurisdiction sharing; VESTA call-handling pairing; EIDO framing; Avtec Scout / CommandCentral AXS voice consoles (adjacent); PremierOne CSR.
- ZOLL: ZOLL Respond mobile app, Mobile Care Connect (NEMT queue), Direct Data Access, emsCharts/Billing integration, BLS/ALS capability-matching framing, at-post positioning support.
- CentralSquare: Public Safety Suite tiering (Enterprise/Pro/ONESolution), Vertex NG911 Call Handling, Unify CAD-to-CAD, Skydio DFR integration, Centerline AI.

---

## Boundary Findings

| Neighbor type | Relationship | Boundary criterion ("remove X → becomes the other") |
|---|---|---|
| Police Records Management System (§24) | downstream seam | CAD holds the live incident + unit state; RMS holds the post-incident case record. Remove real-time unit dispatch/status → the incident log becomes an RMS object. Add case investigation/arrest/evidence → RMS. Evidence: Motorola "automatic data transfer from CAD to records management systems"; Mark43 suite splits CAD vs RMS. |
| Emergency call handling (E911/NG911; realized in market as VESTA/Vertex-class products; no dedicated directory leaf) | upstream seam | Call handling manages the telephone call (voice, caller location, multimedia); CAD manages the incident and units. The call→incident handoff is the seam. Remove incident/unit management → call-handling system. Evidence: Motorola sells them as separate product families; CentralSquare pairs Vertex with CAD. |
| Emergency Management Platform (§24) | adjacent, confusable at scale | EM platform coordinates multi-event, multi-agency, long-duration disaster response at EOC level (planning, resource requests, situational awareness); CAD is per-incident, real-time, unit-level. Large-scale events stress CAD toward EM but the unit of work differs (incident vs event/disaster). |
| Fire Department Records / Operations System; EMS Operations Platform (§24) | downstream | Records/ePCR systems consume CAD output; they do not dispatch units. Evidence: ZOLL dispatch→emsCharts(ePCR)→billing chain. |
| Taxi Dispatch Platform; Towing Dispatch Platform (§18) | structural siblings, commercial | Same mechanics (jobs, units, status, assignment, map) but commercial service orders, revenue settlement, no emergency priority/protocols/public mission. Remove emergency/public-safety semantics and add fare/tariff settlement → commercial dispatch. (Directory already separates these leaves; confirmed distinct.) |
| Dispatch Management (§18, freight) | structural sibling, logistics | Load/freight assignment over commercial logistics; no incident/priority/response semantics. |
| On-call Management (§14) | adjacent | Schedules who is available; does not run incidents or dispatch. |
| Contact Center Routing Platform (§07) | superficial resemblance | Routes customer contacts to agents; no field units, no incidents, no status cycle. |
| Public Alert & Warning System (§24) | adjacent | Outbound mass alerting to populations; not incident-level unit dispatch. |
| Mechanical CAD (§16) | name collision only | Entirely different domain (engineering design). Directory full-name disambiguates. |

Taxonomy verdict: the leaf is a legitimate standalone Type. No alias/variant/duplicate problem found. The §18 commercial-dispatch siblings are correctly separate leaves.

## Uncertainties

1. **Unit status vocabularies**: all four vendors confirm status tracking, but no fetched source documents a canonical status sequence (available → assigned → en route → on scene → clear). Treated as agency-configured; final doc uses hedged conceptual wording only.
2. **EMD/protocol-tool integration** (e.g., emergency medical dispatch protocol software driving call prioritization): not evidenced in fetched pages; not asserted. Listed here so a future pass can verify.
3. **Exact resilience figures** (uptime percentages, failover timing): not reachable; not asserted.
4. **Hexagon / Tyler CAD structure**: unreachable this pass; the enterprise-incumbent pole is covered by Motorola/CentralSquare instead. A future pass could add them.
5. **Mark43 Alternate CAD**: product exists (nav title) but page not fetched; nature unverified — kept out of final doc.
6. **Non-US market shape** (112/999 control rooms, European CAD vendors): no sources fetched; the historical/regional check rests on the structural argument that L0 predates NG911-era specifics, not on direct non-US vendor evidence.

## Final Synthesis

A Computer-aided Dispatch system is the real-time operational heart of a dispatch operation: it turns incoming service requests into tracked incidents, keeps a live inventory of response units and their statuses, recommends and (under human governance) executes the binding of units to incidents, and presents the whole response as a live map-and-status picture until each incident closes. Around that core, mature products add emergency-line integration, GIS, AVL, mobile field clients, multi-jurisdiction operation, records hand-off, analytics, and resilience machinery; discipline scope, emergency-vs-non-emergency workload, deployment model, and automation depth vary by segment. The type's sharpest seams are upstream (call handling owns the call; CAD owns the incident and the units) and downstream (records systems own the aftermath; CAD owns the response).
