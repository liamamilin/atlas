# Research Notes — Shipment Visibility Platform

Slug: shipment-visibility-platform
Research date: 2026-09-09
Methodology: v1.1 (update-v1/)
Directory position: §18 Transportation, Mobility & Logistics

## Research Goal

Understand what a Shipment Visibility Platform is as an Application Type: its unit of record, how tracking data enters and is normalized, what the operational loop looks like, who uses it, which interfaces it presents, which rules and states matter, and where its boundary lies against the densest seam family in the directory (§18 delivery/transport cluster + adjacent Types).

This pass carries INHERITED JOINT REVIEW FLAGS that must be discharged:

1. **cold-chain-transportation-monitoring** (§18, processed): "apply the condition test when shipment-visibility-platform is processed" — condition-vs-requirement core (knowing where a shipment is vs whether the cargo environment held against a defined requirement, with the evidence record that follows); feature presence explicitly NOT the seam (Tive, Sensitech market one platform for both).
2. **delivery-experience-platform** (§05.08, processed): "apply the audience+surface test when shipment-visibility-platform is processed" — logistics-ops freight consoles vs brand-owned consumer surfaces with proactive customer comms; project44 is the live straddle.
3. **transportation-management-system-tms** (§10, processed): "shipment-visibility-platform = location/status layer without committing/executing (Shipwell's own FAQ treats them as potentially separate purchases; Turvo integrates P44 rather than being one)".
4. **parcel-management-platform** (§18, processed): "shipment-visibility-platform (watching/normalizing state vs transacting the ship)".
5. **on-demand-delivery-platform** (§18, processed): "shipment-visibility-platform (watching vs executing)".
6. **order-management-system-oms** (§05.07, processed): its removal tests name "shipment-visibility territory" for tracking/visibility without an order-of-record spine.
7. **courier-management-platform** (§18, processed): delivery-cluster tenant-identity seam (operator-business frame vs shipper-side orchestration).
8. **food-traceability-platform** (§20, processed): "lot identity + transformation modeling vs cargo-agnostic consignment transport status".
9. **freight-forwarding-system** (§18, processed): left a joint-review flag naming this leaf as unprocessed sibling (forwarder consignment/document/charge machinery vs visibility layer).

## Initial Boundary

Pre-research hypothesis:

- Core use: a shipper/3PL/LSP watches in-transit freight (truckload, LTL, parcel, ocean container, air, rail) that other parties carry, with live location/status/ETA assembled from carriers' systems, telematics, driver apps, and tracking devices, and works exceptions (delays, missed milestones) from a control-tower surface.
- Users: shipper logistics/supply-chain teams, 3PL/LSP operations, customer service, transport-executing parties (carriers/drivers) as data contributors.
- Nearest neighbors: TMS (§10/§18), Cold Chain Transportation Monitoring (§18), Delivery Experience Platform (§05.08), Courier Management / Last-mile Delivery / On-demand Delivery / Parcel Management (§18 cluster), Vehicle Telematics Platform (§18), Food Traceability Platform (§20), Freight Forwarding System (§18), OMS family (§05.07), Transportation Exception Management (§18), Proof of Delivery Platform (§18).
- Unknowns: whether the unit of record is the shipment or something coarser (order/PO); whether multi-source carrier-data aggregation is definitional; how the hardware-tracker pole (Tive) relates to the network/API pole (project44/Shippeo); whether exception management is definitional or common; whether analytics/carrier scorecards are definitional.

## Research Questions

1. What is the unit of record? What does a shipment record carry, and who creates it?
2. Where does tracking data come from, and how is it normalized across carriers/modes?
3. What status/milestone/ETA model does the platform present?
4. What is the exception/alert lifecycle, and who works it?
5. Who are the users, including the transport-executing parties that feed data?
6. What interfaces exist (map, list, detail, alert queue, sharing, analytics, network ops)?
7. What rules matter (record persistence, completion semantics, data quality, sharing permissions)?
8. Does the platform execute carriage (tender/book/rate/dispatch), or strictly watch?
9. Where does consumer-facing tracking (delivery experience) sit relative to this Type?
10. Where does cargo-condition monitoring sit relative to this Type?

## Representative Products

| Product | Pole | Customer level | Why selected |
|---|---|---|---|
| project44 | multi-modal network platform; ships TMS + Visibility + Yard + eCommerce Logistics as separate families | enterprise shippers & LSPs | market-defining network; straddles delivery-experience seam — needed for audience+surface test |
| FourKites | enterprise control tower; order/shipment/inventory/facility "twin" layering; AI-agent orchestration | Fortune-500 shippers & 3PLs | order-vs-shipment layering evidence; downstream action automation (appointments, POD, WISMO) |
| Shippeo | European road-first real-time visibility; carrier-network & data-quality-centric philosophy | enterprise shippers (retail, automotive, FMCG) | the "trusted data foundation" philosophy; data-completeness governance; Gartner RTTVP category anchor |
| Tive | IoT tracker + software platform (hardware-first) | mid-market → enterprise; pharma/food/fresh | hardware-vs-network realization axis; condition-data straddle evidence for the cold-chain test |

Category name check: Shippeo's site cites the Gartner® Magic Quadrant™ category "Real-Time Transportation Visibility Platforms" (2025 Leader listing) — the market's own name for this Type; the directory leaf name "Shipment Visibility Platform" is the same concept.

## Sources

Fetched 2026-09-09 (all WebFetch):

- Tive — External Knowledge Base (Tier 1, operational help center): support hub; Creating Shipments; Shipment List and Map; Tive Reveal: Overview; Sharing Data (hub). https://support.tive.com/
- Shippeo — product/marketing pages (Tier 2): root; Platform Overview (marketecture: Visibility Applications / Trusted Visibility Platform / Integration Hub / Multi-Modal Carrier Network); Real-Time Visibility. https://www.shippeo.com/
- project44 — root/product navigation (Tier 2): product families TMS / Visibility / Yard / eCommerce Logistics with sub-families; carrier connection types (DriveView app, Telematics, API/EDI); customer quotes. https://www.project44.com/
- FourKites — root/platform pages (Tier 2): Intelligent Control Tower, Digital Twins (Order/Shipment/Inventory/Facility/Asset), Digital Workers (Tracy/Alan/Cassie/Polly), Outcomes. https://www.fourkites.com/

Access limitations:

- project44 developer docs (docs.project44.com, developers.project44.com paths) unreachable this pass (transport error / 404). p44 evidence is Tier 2 (official product pages) — no p44 operational/UI detail asserted beyond what product pages state.
- FourKites evidence is Tier 2 marketing pages; structural claims only.
- Shippeo Help Center requires auth (login-gated) — not fetched; Shippeo operational claims kept to what public product pages state.
- No third-party review sites used; no precise market-scale numbers asserted as fact anywhere.

## Product A — Tive (Tier 1, operational)

Key observations (evidence layer A unless noted):

- **Shipment as created record**: shipments are created in the platform (manual form, templates, CSV upload, bulk location upload; also API). Required fields to start: Shipment ID, trackers, ship-from/to, ship date. Fields include mode (Road/Air/Ocean/Rail), carrier per leg, multiple legs ("Create multi-stop shipments"), custom fields, alert presets, collaborators.
- **Shipment lifecycle states**: In-Transit / Upcoming / Completed (list tab structure). "Shipments cannot be deleted… a complete and permanent record… for reporting and auditing purposes." Editing restricted by status: Upcoming/In-Transit editable (tracker ID locked once in-transit); Completed locked/final. Completion derived from geofence arrival at destination; "auto-complete delay" setting; geofence default radius 1 km when a location has no configured custom geofence (product-specific detail).
- **Data sources attached to the record**: IoT trackers linked to the shipment ("Trackers: link tracker(s) to your shipment for real-time updates"); mode-specific references — AWB "used for tracking a shipment's location while in transit via air"; Container ID (MMSI) "enables ocean cargo tracking by displaying vessel location". Sensor data and charts (temperature etc.) per shipment; MKT / degree-minutes metrics.
- **Alerts/exceptions**: alert types include Temperature, Probe, Humidity, Shock, Light, Prolonged Stop, Route Deviation, Departure Delay, Arrival Delay, Battery, Connectivity, Geofence (plus ETA alerts, departure/arrival notifications, reefer start/stop). Alert states: Not Started → In Progress → Auto-Resolved / Resolved; resolution tab with comments and "assign next steps to users" — an operational triage loop ("Shipment Collaboration: Alert Resolution").
- **Watch surfaces**: Shipment Page = list + map; color-coded alert pills (Dark Red = active unresolved; Pale Red = in progress/auto-resolved; Green = resolved; Gray = completed with total alert count); map clusters; filters (origin/destination, tracker type, shared shipments, alert location in-transit, alert type Contains Any/All, arrival timing Today…This Month, on-time status Late/Early by thresholds — tier-gated).
- **Sharing**: Sharing Data section ("Sharing Shipments"); collaborators assigned per shipment with roles/permissions; filter "created by others" includes "shipments… shared with you via the shipment collaborator function" — cross-organization sharing is a real mechanism.
- **Analytics (Reveal)**: cleans/enriches completed-shipment data (validates departures, leg transitions, arrivals; smooths tracker anomalies; excludes invalid shipments); Lane Insights, Carrier Insights, Alert Heatmaps; network benchmarking against "millions of anonymized journeys across the Tive network". Analytics framed as unlocked by shipment creation.
- **Workflow automations**: templates for automated workflows (category exists; depth not fetched).

L2/L3 notes: tier gating (Essential/Plus/Premium) controls filters, AWB/container tracking, analytics; geofence/1 km/auto-complete-delay specifics are vendor detail; "Solo vs. Team Driver" ETA-accuracy setting is vendor detail.

## Product B — Shippeo (Tier 2 public product pages)

Key observations (evidence layer A for page statements, B for cross-product commonality):

- **Self-positioning**: "Real-time transportation visibility"; named a Leader in the 2025 Gartner® Magic Quadrant™ for Real-Time Transportation Visibility Platforms. Tagline: "Track every shipment, know every ETA, act with confidence".
- **Marketecture (platform overview)**: four layers — Visibility Applications / Trusted Visibility Platform / Integration Hub / Multi-Modal Carrier Network, with customer roles around the top. "Visibility Engine": "enriches and analyses every movement to deliver… reliable ETAs, milestones and early warnings when disruptions arise."
- **Multimodal network as data substrate**: Road FTL, Road LTL/Parcel & Last Mile, Ocean, Ports & Terminals, Intermodal Rail, Air. "Every shipment update, ETA, and milestone depends on the quality of carrier integrations."
- **Network operations as a first-class function**: "Network Operations Center… Onboard and connect carriers, systems, and partners… Govern integrations and monitor data quality to ensure complete, reliable visibility at scale." Data-quality dashboard example: "93% status completeness" with categories "tracked at loading & delivery / only at delivery / only at loading / not tracked", per-carrier breakdowns. Carrier onboarding SLA + tracking compliance SLA + ETA accuracy SLA; carrier recognition program; carrier "why join us" page (two-sided network posture).
- **Watch surface**: "See at-risk deliveries, ETAs, and location on the map"; "Search, filter and save views and homepage widgets using any reference"; milestone & location at "any site or port"; "standardized milestones and real-time status updates down to the SKU level, via deep carrier TMS integrations or Shippeo's mobile app for drivers"; predictive ETA "available for 100% of your shipments".
- **Distribution of visibility**: Communication module — notification channels SMS/Email/WhatsApp, language selection, message templates with placeholders; "Branded Portals: give recipients access to live shipment information"; driver mobile app (app-store listings for Shippeo Driver).
- **Derived solution layers**: eCMR & digital proof of delivery (transport-document digitization), Carbon Visibility (emissions calculation), D&D (detention & demurrage cost avoidance), Insights (carrier performance, port congestion analytics).
- **Users**: shipper supply-chain organizations (Renault Group control tower quote; Coca-Cola HBC; Carrefour Belgium depot ops; Leroy Merlin in-store ops); "keep customers informed"; "free your teams from manual 'where's my order?' chases".
- **Integration out**: "Integration Hub connects your enterprise systems, from TMS, ERP, and road planning tools to CRMs and data lakes."

L2/L3 notes: SLA percentages, "Shippeo AI" agent framing, eCMR/regulatory tie-ins (Spain DeCA blog) are vendor/era-current details.

## Product C — project44 (Tier 2 official product pages)

Key observations:

- **Product-family split (first-hand, discharges the TMS + delivery-experience straddle observations)**: navigation lists four families — "Transportation Management: take control of pre-shipment workflows with rating, tendering, and enhanced analytics" / "Visibility: manage inventory in transit across every mode globally" / "Yard Management" / "eCommerce Logistics: improve delivery experience with visibility, exception management, and insights" (sub-families: Last Mile Resolution, Last Mile Insights, Consumer Visibility "post-purchase consumer visibility", Predictive Delivery Dates "predictive pre-purchase delivery dates"). Visibility and consumer-facing eCommerce Logistics are separately packaged product families under one roof — vendor-drawn audience+surface seam.
- **Visibility family scope**: Ocean (Container/RoRo/Barge/Emissions), Over-the-Road (FTL/LTL/Parcel), Air, Rail, Ports & Terminals ("terminal milestones and D&D cost data"), Emissions, Theft Prevention, Tariff Analytics.
- **Carrier connectivity as standing operation**: carriers connect via "DriveView Mobile App (drayage & owner-operators)", "Telematics (asset-based carriers)", "API/EDI (very high volumes)"; "Carrier Onboarding… Connection Accelerator"; carrier-facing pages ("reduce check calls"), Preferred Carrier Program, carrier FAQs/support portal. Network-scale claims (282K carriers, 1.5B+ shipments/yr, 700M+ events/day) are marketing figures — recorded, not asserted as fact.
- **Users**: Solutions → Shippers and LSPs; customer quotes name operations, sales, and customer-service teams consuming visibility via ERP integration (Saverglass); case studies across automotive/retail/food/manufacturing. July 2026 press release: split into two businesses — enterprise-shipper platform (p44) vs "LSP44" agent/API infrastructure for 3PLs, freight forwarders, brokers — seat-agnostic posture of the underlying visibility substrate.
- **Action layer**: "AI agents… from carrier outreach to exception resolution"; exception management and collaboration named as the family's purpose ("improve your supply chain operations end to end through collaboration and exception management").

L2/L3 notes: "Movement / Decision Intelligence" branding, tariff analytics, theft prevention, named stats — vendor/era-current, not definitional.

## Product D — FourKites (Tier 2 official product pages)

Key observations:

- **Shipment as digital twin**: "Shipment Twin: real-time tracking across all modes. ML-powered ETAs, carrier status, exception detection, proof of delivery." — shipment-level tracking with carrier status as the source signal.
- **Order layer above shipment**: "Order Twin: PO lifecycle from creation through delivery. Planned vs actual, supplier commitments, order-to-shipment linkage." — the order/PO is an upstream linkage layer, not the tracking unit. Customer story: "Orvis… moved off manual spreadsheet tracking to order-centric, real-time visibility."
- **Carrier connectivity**: "Carrier Connectivity: [N]K+ active carriers connected across every mode"; network graph of multi-tenant data; facilities/lanes modeled.
- **Downstream actions on visibility (the "act" half)**: Digital Workers — Tracy "chases ETAs, confirms milestones, and resolves status gaps"; Alan "ETA-driven dock appointment automation… creates, reschedules, manages appointments based on live shipment status"; Cassie "WISMO auto-resolution… resolves status queries from the Shipment Twin"; Polly "chases carriers for missing PODs". Outcomes: OTIF revenue protection, branded customer shipment tracking portal, ETA-driven appointment automation, automated carrier performance scorecards.
- **Adjacent scope**: Inventory Twin, Facility Twin (yard/dock/gate), Asset Twin (trailers/containers/reefers) — broader supply-chain mirror beyond the shipment; control-tower framing ("Intelligent Control Tower").

L2/L3 notes: named agents, "Loft" agent platform, network-graph "moat" claims — vendor-specific/era-current.

## Cross-product Comparison

| Dimension | Tive | Shippeo | project44 | FourKites | Evidence |
|---|---|---|---|---|---|
| Unit of record | Shipment (created; ID, legs, origin/destination, schedule, mode, carrier) | Shipment/flow tracked via carrier integrations; milestones/ETA per shipment | "Inventory in transit" per shipment/mode; visibility family | Shipment Twin under an Order Twin (PO linkage) | A/B |
| Data sources | Own IoT trackers linked to shipment; AWB (air), container ID/MMSI (ocean) as location references | Carrier TMS integrations, driver mobile app; multimodal carrier network | Carrier connections: mobile app, telematics, API/EDI | Carrier status across modes; carrier connectivity program | A/B |
| Normalization | Milestones/alerts per shipment; mode-specific tracking refs | "Standardized milestones"; predictive ETA for all shipments; data completeness SLA | Mode families; events/ETA across modes | "Real-time tracking across all modes"; ML ETAs | A/B |
| Exception loop | Alert types + Not Started/In Progress/Auto-Resolved/Resolved + resolution tab with comments/assignment | "Early warnings when disruptions arise"; exception management named | "AI agents… carrier outreach to exception resolution"; "collaboration and exception management" | "Exception detection"; Tracy "resolves status gaps" | A/B |
| Persistence | "Shipments cannot be deleted"; completed locked | Milestone history; analytics on completed flows | Event data graph (claims) | Twins as persistent mirrors | A/B |
| Sharing outward | Sharing shipments; collaborators with roles | Branded portals; SMS/Email/WhatsApp comms; driver app | Consumer Visibility / eCommerce family (separate) | Branded customer tracking portal outcome | A/B |
| Network/carrier ops | Tracker assignment; Reveal data cleaning | Network Operations Center; onboarding + completeness governance + SLAs | Connection Accelerator; carrier programs; 3 connection types | Carrier connectivity across every mode | A/B |
| Analytics | Lane/Carrier Insights, heatmaps, network benchmarking | Insights (carrier/port performance) | Procurement analytics (in TMS family) | Carrier scorecards outcome | A/B |
| Condition data | Temperature/shock/humidity/light alert types (sensor trackers) | not documented on fetched pages | not in fetched Visibility family scope | reefer monitoring mentioned under Facility/Asset twins | A (Tive only in fetched sample) |
| Consumer-facing surface | not in fetched scope | Branded portals (recipient access) | Consumer Visibility family (separate product line) | Branded tracking portal (outcome) | A/B |
| Executes carriage? | No (watch only) | No | No — rating/tendering/booking sit in the separate TMS family | No (appointment scheduling acts on ETAs, not carriage commitment) | A/B |

### Canonical abstraction (L0 → L3)

**L0 — Defining invariant (three jointly-held structures):**

1. **The in-transit shipment as the unit of record** — a persistent, individually identified record of one freight movement being carried by transport parties (road load, ocean container movement, air consignment, multi-leg journey), carrying its route/legs, planned schedule, participating carrier(s), and accumulating live progress. Remove → nothing to watch (a register/spreadsheet or generic dashboard).
2. **Transport-party-sourced signals aggregated and normalized onto the shipment record** — location, milestones, status, and arrival predictions assembled from data sources the platform does not itself execute: carrier systems/APIs/EDI, telematics feeds, driver apps, tracking devices, and mode-specific transport references (vessel/container ID, air waybill); normalized into a common status/milestone/ETA picture across carriers and modes. Remove the external sourcing → the platform would be running the transport itself (TMS/dispatch/telematics territory); remove the normalization/aggregation → a pile of per-carrier tracking pages, no unified picture.
3. **The operational watch-and-act loop over deviations** — live progress continuously compared against plan; deviations (ETA shifts, late/missing milestones, in-transit incidents) surfaced as managed alert/exception items with resolution states that users triage, work, and share onward. Remove → passive telemetry archive / raw feed dashboard.

Jointly load-bearing: 1 alone = shipment register; 2 without 1+3 = raw feed collector; 3 without 1+2 = exception workflow with nothing to watch; 1+2 without 3 = tracking data archive, no operational loop; 1+3 without 2 = exception management over un-fed shipments (order/exception management territory); 2+3 without 1 = generic monitoring/alerting with no shipment of record (observability-shaped, not freight-shaped).

**L1 — Common mature structure:** carrier/network onboarding & connectivity as a standing governed operation (NOCs, connection types, onboarding SLAs, carrier programs); live map + filterable shipment list with alert-status indication; standardized milestone model + predictive ETA; data-quality monitoring/cleaning as an explicit surface (completeness %, invalid-shipment filtering); sharing/distribution of live status to stakeholders (collaborators, branded portals, notification channels, APIs out to ERP/OMS/TMS); multi-modal coverage; lane/carrier analytics and scorecards; integration hub to enterprise systems; persistent shipment history (records kept, completed locked for audit).

**L2 — Variant / optional:** data-source emphasis (hardware trackers vs carrier-network/API vs driver apps vs hybrid) — realization axis, not definitional; sensor/condition alert types when the source carries sensors (condition rides the same watch loop; only Tive in the fetched sample documents these); downstream execution-adjacent actions (ETA-driven appointment scheduling, POD chasing, WISMO auto-response); branded recipient/consumer portals as sharing surfaces; derived commercial outputs (D&D cost avoidance, carbon/emissions, eCMR digital documents); order/PO linkage layer above shipments; control-tower/AI-agent orchestration layers (era-current); seat neutrality (shipper vs 3PL vs LSP; one vendor split its LSP business into a separate company).

**L3 — Vendor-specific (research notes only):** Tive geofence default 1 km, auto-complete delay, alert state names, tier gating, Solo/Team Driver setting; Shippeo SLA products, eCMR module, Gartner positioning, recognition program; project44 Movement/Decision Intelligence branding, LSP44 split, Preferred Carrier Program, connection-type marketing names; FourKites named digital workers, Digital Twin branding, network-graph "moat" claims.

### Historical / market-sample check (§24)

Would older, regional, or platform-native products fit the L0? The modern category is a 2010s networked-SaaS phenomenon (the market's own Gartner category name dates its maturity). But the L0 names no GPS, telematics, AI, or cloud: a pre-SaaS shipper's freight desk — a per-shipment tracking log (leg 1), location/milestone information gathered by phone/portal from the carriers and forwarders carrying the freight, consolidated per shipment (leg 2), and a delay/exception follow-up practice worked against promised delivery dates (leg 3) — satisfies all three structures without any modern machinery. Mode-native tracking references (container numbers, AWBs, PROs) predate GPS trackers and are already abstracted into leg 2's "mode-specific transport references". The check therefore passes at the analog level; nothing era-current is definitional. Regional road-first (Shippeo, Europe) vs multi-modal network (p44/FourKites) vs hardware-first (Tive) poles all fit the same core.

## Boundary Findings

**1. vs Transportation Management System (§10/§18) — watching vs committing/executing. RATIFIED with first-hand evidence.** project44 sells "Transportation Management" ("pre-shipment workflows with rating, tendering") and "Visibility" ("inventory in transit across every mode") as separate product families; the visibility family holds no tender/book/rate machinery. Corroborates the TMS pass's seam ("location/status layer without committing/executing"; Shipwell FAQ treats them as separate purchases; Turvo integrates P44 rather than being one). The execution system is the visibility platform's data source, not its function. Removal test: add tender/rate/book commitment and the product becomes a TMS; strip execution from a TMS and only the visibility layer remains — this leaf.

**2. vs Cold Chain Transportation Monitoring (§18) — condition test APPLIED. RATIFIED, keep-both.** The seam is knowing where the consignment is / whether it is on schedule (movement-progress of record) vs whether the cargo environment held against a defined requirement (condition-of-record with evidence). Confirms the cold-chain pass's warning that feature presence is not the seam: Tive — named by that pass — documents temperature/shock/humidity/light alert types inside the same watch loop, riding on sensor trackers; condition data is an optional alert dimension of the shipment record here, whereas the cold-chain Type centers the condition requirement and its evidence record. Network-scale visibility products (p44/Shippeo/FourKites) center location/milestone/ETA with no condition-of-record in their fetched core. Keep-both with the condition-vs-movement seam; Tive is the live straddle (one platform marketed for both), consistent with the cold-chain pass's own observation.

**3. vs Delivery Experience Platform (§05.08) — audience+surface test APPLIED. RATIFIED, keep-both.** First-hand: project44 ships "Consumer Visibility" (post-purchase consumer visibility) inside a separate "eCommerce Logistics" family, distinct from its Visibility family; FourKites lists the branded consumer tracking portal as a Customer Fulfillment outcome beside its ops control tower; Shippeo's branded portals "give recipients access to live shipment information" as a sharing surface. The seam holds exactly as the delivery-experience pass drew it: logistics-operations freight consoles (ops teams watching in-transit freight against plan; consignment-anchored) vs brand-owned consumer post-purchase surfaces (order/parcel-anchored, proactive shopper comms). Visibility products may include sharing portals, but the served audience remains consignment stakeholders, not the shopper-brand relationship.

**4. vs the §18 execution cluster (courier-management, last-mile-delivery, on-demand-delivery, parcel-management) — watching vs executing. CONFIRMED from this side.** None of the sampled visibility products dispatches drivers, builds routes, matches per-request capacity, purchases postage/labels, or runs an operator-business frame (client-account rating/billing). Tive's shipments are watched records fed by trackers/references; Shippeo/p44/FourKites aggregate carrier-fed signals. Consistent with the seams those passes held (tenant identity, phase, capacity model). Reverse removal test: strip the watching/normalizing layer from any execution product and this leaf's core is what remains.

**5. vs Order Management System family (§05.07). CONSISTENT, keep-both.** The OMS pass's removal tests place "tracking console / visibility without management" outside OMS. First-hand support: FourKites explicitly layers the Order Twin (PO lifecycle) above the Shipment Twin with "order-to-shipment linkage" — the order is an upstream linkage layer; the visibility unit of record is the shipment. Order-level money/promises (capture, sourcing, fulfillment lifecycle) are not this Type's center.

**6. vs Food Traceability Platform (§20). RATIFIED from this side.** The sampled visibility Type has no lot/batch identity or transformation modeling; the unit is the cargo-agnostic consignment/shipment, and Tive's analytics are lane/carrier-level, not lot-level. Matches the food-traceability pass's seam (lot identity + transformation vs consignment transport status).

**7. vs Freight Forwarding System (§18). CONSISTENT.** The forwarder's unit of record is the multi-leg consignment with house/trade documents and the multi-party charge ledger (forwarder pass). Visibility platforms watch such consignments as data subjects; they hold no document/charge machinery in the core. Tive's multi-leg shipments with per-leg carriers are the visibility-side mirror of a consignment, without the forwarder's commercial layer. Forwarder systems and carriers are data sources for this Type (p44 explicitly splits LSP infrastructure out; Shippeo integration targets TMS/ERP).

**8. vs Vehicle Telematics Platform (§18, UNPROCESSED) — FLAG HUNG for that pass.** The object-of-record seam: telematics centers vehicle/asset health and behavior (the truck, the trailer, the reefer unit); this Type centers the consignment/shipment being carried. First-hand: project44 lists telematics as one of three carrier connection types feeding its visibility ("Telematics: asset-based carriers") — the telematics feed is a data source for the shipment picture, not the same object of record. That pass should apply the cargo-environment/asset test (vehicle/asset health vs what the freight experiences/where the freight is) and confirm keep-both.

**9. vs Transportation Exception Management (§18, unprocessed sibling).** In-sample evidence: exception/alert triage is a standard capability inside every sampled visibility product (alert states, resolution tabs, early warnings, agent-led exception resolution). A dedicated Transportation Exception Management Type can only stand apart if its center is the exception workflow itself (case management over transport disruptions) rather than the shipment watch loop. Flag recorded for that pass to apply the object test (exception case as unit of record vs shipment as unit of record).

**10. vs Observability/monitoring-shaped Types (§14).** Structural analogy only; the domain binding (freight consignments, carriers, transport milestones) and the shipment-of-record leg distinguish this Type categorically. No overlap concern; recorded for completeness.

## Uncertainties

1. project44's operational (Tier 1) documentation was unreachable this pass — no p44 UI/operational-detail claims made; p44 evidence restricted to product-page structure (Tier 2).
2. Shippeo Help Center is login-gated — Shippeo operational claims limited to public product-page statements; no Shippeo status-model detail asserted.
3. FourKites evidence is marketing-tier; its Order/Shipment Twin layering and digital-worker actions are treated as structural signals, not operational guarantees.
4. Whether carrier-API-only tracking (no hardware, no tracker) is universally available across the category is unverified beyond Tive's AWB/MMSI references and the network vendors' carrier-connectivity pages — asserted only as "data sources the platform does not execute", which all four products support.
5. Exact milestone vocabularies, alert thresholds, and SLA numbers vary per product/tier and were deliberately not canonicalized (Tive's fetched thresholds stay in research notes).
6. The pre-SaaS historical anchor is reasoned (phone/portal-era freight desk), not documentarily evidenced — flagged as inference, consistent with the class-level historical check practice.

## Final Synthesis

A Shipment Visibility Platform is the shipper/LSP-side operational system for watching freight that other parties carry. Its defining core is three jointly-held structures: (1) the in-transit shipment as a persistent, identified unit of record carrying route/legs, schedule, carriers, and accumulating live progress; (2) transport-party-sourced signals — carrier systems/APIs/EDI, telematics, driver apps, tracking devices, mode-specific references — aggregated and normalized onto that record into a common milestone/status/ETA picture across carriers and modes; (3) an operational watch-and-act loop that compares live progress against plan and surfaces deviations as managed, resolvable, shareable alerts. The platform watches, normalizes, and distributes; it does not tender, book, rate, dispatch, or purchase carriage — that absence is the load-bearing seam against TMS and the entire §18 execution cluster, and the audience/object seams against delivery-experience (consumer surfaces), cold-chain (condition-of-record), telematics (vehicle/asset-of-record), food traceability (lot-of-record), and OMS (order-of-record) all held under direct tests. Historical check passes at the analog freight-desk level; the category's own market name ("Real-Time Transportation Visibility Platforms") confirms independent status as a Type.
