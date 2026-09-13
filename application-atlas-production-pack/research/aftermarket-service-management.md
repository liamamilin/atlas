# Research Notes — Aftermarket Service Management

Research date: 2026-09-06
Leaf: Aftermarket Service Management (DIRECTORY §16 Engineering, Manufacturing & Industrial)
Slug: aftermarket-service-management

---

## Research Goal

Understand what "Aftermarket Service Management" software actually is, from real products: what objects it manages, who uses it, how service work flows, what rules govern it, and where its boundary lies against CMMS/EAM, Field Service Management, PLM, Customer Service Platforms, and warranty/returns software.

## Initial Boundary (working hypothesis before research)

- Hypothesis: software used by product manufacturers (or their authorized service networks) to manage the in-service phase of products already sold — warranty/service contracts, service requests, spare parts, field/depot service execution, service history.
- Likely confusions:
  - CMMS / EAM (maintaining the operator's OWN assets) — different asset ownership.
  - Field Service Management (scheduling/dispatching a mobile workforce) — fulfillment arm, not the whole.
  - PLM (as-designed/as-built product data) — upstream lifecycle stage.
  - Customer Service Platform / Help Desk (case management without product-unit anchoring).
  - Returns Management (e-commerce purchase returns) — different object and purpose.
- Unknowns at start: Is "installed base" the universal central object? Is entitlement (warranty/contract) definitional or just common? How do PLM-rooted and ERP-rooted products differ structurally?

## Research Questions

1. How is the population of sold, in-service product units modeled (naming, creation, customer attribution, serialization)?
2. How are service entitlements (warranty, service contracts, SLAs) represented, and how do they gate service delivery?
3. What is the central work object (service request / work order / case) and its lifecycle?
4. What fulfillment modes exist (field dispatch, depot repair, returns/RMA, remote service) and how are they structured?
5. How does service connect to the commercial side (parts, pricing, billing, service revenue)?
6. How does service connect upstream to product data (as-designed/as-built/as-maintained, service BOM, feedback to design)?
7. What interfaces exist (back office, dispatcher, technician mobile, depot, customer portal, partner portal)?
8. What rules matter (entitlement checks, coverage windows, SLA timers, traceability/compliance, parts consumption → ERP)?

## Representative Products

Selected for market representation + different product philosophy/root system + documentation reachability:

| Product | Root system / philosophy | Segment |
|---|---|---|
| PTC ServiceMax | Asset-centric field service management platform (built on Salesforce platform, now standalone) | Enterprise OEM/dealer service |
| Siemens Teamcenter Service Lifecycle Management (SLM) | PLM-rooted service engineering (service BOM, as-built/as-maintained configuration) | Large discrete manufacturers, A&D |
| SAP (S/4HANA Cloud for Service + Service Cloud + Field Service and Asset Management) | ERP-rooted service portfolio (contracts, returns/repair, billing inside ERP) | Enterprise, cross-industry |
| IFS Cloud (Service Management / FSM + Service Logistics & Depot Repair) | Service-centric ERP suite (FSM + parts + depot repair + warranty in one suite) | Enterprise, A&D/energy/field-heavy industries |

Also attempted: Mize (aftermarket/warranty-native mid-market vendor) — abandoned after 2 transport failures (see Sources).

## Sources

All successfully fetched 2026-09-06 (Tier 2 — official product pages; no Tier 1 operational help docs were reachable):

- PTC — ServiceMax product overview (asset-centric FSM): https://www.servicemax.com/ (served by ptc.com)
- PTC — ServiceMax Depot Repair & Service Logistics: https://www.ptc.com/en/products/servicemax/core/depot-repair
- Siemens — Teamcenter Service Lifecycle Management: https://www.siemens.com/en-us/products/teamcenter/solutions/service-lifecycle-management/
- SAP — Service Management overview (portfolio pillars): https://www.sap.com/products/service-management.html
- SAP — Field Service and Asset Management: https://www.sap.com/products/scm/field-service-and-asset-management.html
- SAP — Service Cloud: https://www.sap.com/products/crm/service-cloud.html
- IFS — Field Service Management: https://www.ifs.com/en/products/fsm
- IFS — Service Logistics and Depot Repair: https://www.ifs.com/en/products/fsm/service-logistics-and-repair

### Source-access Limitations (recorded per evidence rules)

- SAP Help Portal (help.sap.com) renders as a JS shell; no operational documentation reachable. SAP claims are therefore limited to official product-page positioning; no SAP-specific operational detail (state names, defaults, limits) is asserted anywhere.
- IFS documentation portal (docs.ifsworld.com) — transport error (1 attempt). IFS claims limited to product pages + on-site glossary.
- ServiceMax documentation portal (documentation.servicemax.com) — transport error (1 attempt). ServiceMax claims limited to PTC product pages (which are unusually detailed, including step-by-step depot workflow descriptions).
- Mize (mize.com) — transport error twice; abandoned. No mid-market aftermarket-native vendor in the sample.
- DuckDuckGo search endpoints timed out twice; abandoned. No search-engine-assisted discovery.
- Consequence: all evidence is Tier 2 (official product pages). No precise numeric limits, exact state labels, or default settings are asserted in either file. Assertion strength calibrated accordingly.

---

## Product Observations

### PTC ServiceMax (asset-centric FSM platform)

Evidence layer: A (directly observed on official product pages).

- Self-positioning: "asset-centric field service management"; "every service interaction is tied to a specific asset and its history — installation details and configuration, maintenance and repair records, warranty, entitlement, and contract data, performance and usage metrics."
- Installed base & asset lifecycle management: track asset health, maintenance history, service interventions across lifespans; supports change orders and recalls.
- Contracts, warranties, entitlements: contract creation/amendment/renewal; SLA and customer-commitment visibility "on every work order"; a rules-based "Entitlements engine" keeps contract/warranty data "accurate, available everywhere, and visible to all parties throughout the service delivery cycle"; prevents revenue leakage.
- Work execution management: "the entire service lifecycle from work order scheduling and dispatch to task execution, completion reporting, and invoicing."
- Scheduling/dispatch: Service Board; optimization engine matches technician by location, skills, availability, route, job requirements.
- Technician mobile: work orders, customer info, service procedures, checklists, forms; works offline; access to asset service history, required parts, entitlements/contract visibility.
- Depot Repair (separate pillar): RMA intake → inbound receiving (match against RMA, confirm condition/accessories) → triage & queue assignment (rules-based, manual override) → repair execution (task-level work plans; repairs, replacements, exchanges, returns; kanban status) → quality inspection & testing → outbound shipment; "connected to installed base & service history — every repair draws on full as-maintained installed base data"; service parts logistics (check availability, assign parts to work orders, track shipments); reverse logistics; remanufacturing as a disposition option.
- ERP integration: parts, inventory, contracts, financial data synced (e.g., SAP); depot FAQ: ERP handles invoicing/GL/inventory valuation, depot software passes parts consumption, labor, billing events back.
- Customer self-service: track service progress, schedule appointments, view asset data.
- Remote service: IoT data (ThingWorx or other) + service history for remote investigation; video/AR/chat to reduce truck rolls.
- Analytics: technician productivity, resolution times, cost to serve, service profitability.
- Preventive/predictive: maintenance schedules automated from usage, thresholds, or regulatory requirements.
- Industries: industrial equipment, medical devices (traceability/compliance), electronics/high-tech, equipment dealers (multi-brand: "service contracts, RMAs, depot repairs, and warranty claims"), oil & gas, HVAC.
- FAQ distinctions offered by the vendor itself: depot repair vs field service (ship to centralized repair center vs on-site); depot repair vs maintenance management (complementary); asset-centric model definition.

### Siemens Teamcenter Service Lifecycle Management (PLM-rooted)

Evidence layer: A (directly observed on official solution page).

- Positioning: SLM "helps you capitalize on product knowledge from service engineering for quality service planning and execution"; "one source of service knowledge."
- Service BOM (SBOM): integrated service BOM with engineering; "full understanding of your service BOM and physical asset configurations, including as-built BOM records, status and service history."
- Service plans: "create service plans powered by AI to optimize service operations and reduce asset downtime"; technicians prepared for "upgrades, as well as reactive and proactive service activities — improving first-time-fix rates."
- Execution split: Teamcenter = service engineering side; execution delegated via closed-loop integration to IBM Maximo (EAM) — "visibility of asset configurations to service technicians, and feedback of service activities to design engineers."
- Servitization: Salesforce partnership app — "Teamcenter manages connected product and service engineering data while Salesforce... manages the complete customer story."
- Product Support Data Management (PSDM): connects PLM and product support for defense OEMs; data exchange aligned with GEIA-STD-0007; product knowledge transfer OEM → operators.
- Teamcenter Share: extends service-related data/processes beyond internal teams.
- Aftermarket framing: analyst report titled "The future of the aftermarket business" (heavy equipment); servitization white papers; "Asset Monetization with Teamcenter SLM for Salesforce — Drive transformation to add new revenue for your aftermarket business."

### SAP (ERP-rooted service portfolio)

Evidence layer: A (directly observed on official product pages). Operational docs unreachable — positioning only.

- Service Management overview page maps the portfolio pillars:
  - Offering and sales (service subscriptions, quotation→payments) — S/4HANA Cloud for Service
  - Service contract management ("fulfill contractual agreements with the right mix of materials and human resources") — S/4HANA + Service Cloud
  - Customer engagement (omnichannel agent workspace, cross-departmental case management) — Service Cloud
  - Asset performance and predictive service — SAP APM
  - Service and spare parts planning — S/4HANA
  - Optimized scheduling and dispatching (Gantt/map, AI) — Field Service Management
  - Mobile field service execution (offline) — FSM + SAP Service and Asset Manager
  - Field service partner management (partner portal: manage technicians, track job orders, feedback) — FSM
  - **Customer returns and repair services**: "connecting accurate customer contract and product warranty information to customer service, returns logistics, repair work, and customer billing" — S/4HANA + Service Cloud
  - Billing, accounting, profitability — S/4HANA finance
- "Close the loop from service feedback to product design" — service→design feedback as a stated pillar.
- SAP Field Service and Asset Management: planning/scheduling/dispatch + mobile execution for "asset and customer service work"; technicians "receive assignments, access asset history, record time and materials, and close work orders — online or fully offline"; contractor/subcontractor portals; native ERP integration synchronizing "field activity with ERP financials, supply chain, and asset records."
- SAP Service Cloud: case management, agent workspace, omnichannel — generic customer service surface (not unit-anchored by itself).
- ITSM distinction stated by SAP itself: ITSM manages IT services; SAP service management "connects customer touchpoints to operations across... customer service, service operations, field service, asset management."

### IFS Cloud (service-centric ERP suite)

Evidence layer: A (directly observed on official product pages + on-site glossary).

- IFS glossary definition of Service Lifecycle Management (SLM): "manages the end-to-end service journey for a product or asset, from customer support and service requests to planning, execution, spare parts, warranties, and recalls... maximize uptime, extend asset life, grow profitable service revenue."
- FSM: "real-time visibility into asset history, warranty information, and SLA commitments"; Mobile Workforce Management (AI scheduling, field-to-office collaboration); Contractor Management (onboarding, billing, compliance); Workforce Planning & Scheduling.
- Service Logistics & Depot Repair: "streamlines handling returns, depot repairs, and warranty claims. From return authorization through inbound shipping, repair, outbound shipping, and billing"; automated returns tracking/authorization; repair + inventory management ("right parts at the right time"); reverse logistics; remanufacturing glossary entry.
- Suite framing: IFS positions ERP + EAM + FSM + ESM as one "Moment of Service" platform; service-centric ERP guide.

---

## Cross-product Comparison

| Dimension | ServiceMax (PTC) | Teamcenter SLM (Siemens) | SAP service portfolio | IFS Cloud |
|---|---|---|---|---|
| Central in-service object | Installed product / asset ("installed base") with service history | Physical asset configuration + as-built BOM records + service history | Equipment/asset records + customer contract & warranty info (ERP-side) | Asset history + warranty info per product/asset |
| Entitlement | Contracts/warranties/entitlements engine; SLA on every work order | (not prominent on page — service planning focus) | Customer contract + product warranty connected to service, returns, repair, billing | Warranty information + SLA commitments visible in service delivery |
| Central work object | Work order (field) / depot work order + RMA | Service plan → service activities (execution delegated to Maximo/Salesforce) | Service work across cases, returns/repair, field jobs | Service request/work order; return authorization |
| Field dispatch | Core (optimization engine, Service Board) | Delegated to execution systems | Core (FSM scheduling/dispatch, Gantt/map) | Core (MWM, PSO scheduling) |
| Depot repair / returns | Dedicated pillar (RMA→receiving→triage→repair→inspection→shipment) | Not on page (PLM side) | "Customer returns and repair services" pillar | Dedicated module (return authorization→shipping→repair→billing) |
| Spare parts | Service parts logistics; parts on work orders | Service BOM defines serviceable structure | Service and spare parts planning pillar | Service parts logistics module |
| Commercial settlement | Invoicing at end of work lifecycle; ERP sync | Asset monetization / aftermarket revenue framing | Billing/accounting/profitability pillar; quotation→payments | Billing in depot repair flow; service revenue growth framing |
| Upstream product linkage | Asset configuration + installation details | Service BOM integrated with engineering; feedback to design | "Close the loop from service feedback to product design" | (suite-level; not prominent on page) |
| Customer self-service | Track progress, schedule appointments, view asset data | Teamcenter Share (extend data beyond internal teams) | Customer engagement pillar (omnichannel) | (not prominent on page) |
| Partner/dealer channel | Equipment dealers: multi-brand service, contracts, RMAs, warranty claims | PSDM: knowledge transfer OEM→operators | Field service partner portal | Contractor management |
| Remote/IoT | IoT (ThingWorx) remote service | (not on page) | Asset performance/predictive service pillar | (not on page) |
| Compliance/traceability | MedTech/A&D traceability, audit-ready records | GEIA-STD-0007 PSDM for defense | (not on page) | (not on page) |

### Cross-product commonalities (Layer B)

1. **Installed base of identified in-service units** — every sampled product centers service on a registry of sold/in-service product units (named: installed base, installed products, assets, physical asset configurations, equipment) attributed to customers, carrying per-unit history.
2. **Entitlement as the commercial gate** — warranty/contract/SLA coverage is checked and displayed when service is demanded (explicit in 3 of 4 samples; Siemens' page focuses on service planning instead, where coverage lives in service plans/contracts at the engineering layer).
3. **Service demand as a tracked work object on a specific unit** — work order / service order / depot work order / return authorization, moving through a lifecycle to completion and (commonly) invoicing.
4. **Multiple fulfillment modes** — field dispatch, depot repair/returns (RMA), parts logistics; remote service in some products.
5. **Per-unit service history accumulates** — "as-maintained installed base data" (ServiceMax), "as-built BOM records, status and service history" (Siemens), "asset history" (IFS, SAP).
6. **Commercial settlement loop** — parts consumption, labor, billing events flow to ERP/finance; service is explicitly a revenue/profitability business ("aftermarket business", "service revenue growth", "asset monetization").
7. **Upstream linkage** — service BOM / as-built configuration / feedback loop to product design (explicit in PLM- and ERP-rooted samples; asset configuration in FSM-rooted).
8. **Extended surfaces** — customer self-service portal, partner/dealer/contractor portal, technician mobile app (offline), analytics.

### Where samples differ (philosophy, not structure)

- FSM-rooted (ServiceMax): starts from work execution + installed base; strongest on dispatch, mobile, depot, entitlements engine.
- PLM-rooted (Siemens): starts from service engineering (service BOM, as-maintained configuration, service plans); execution delegated to EAM/CRM partners.
- ERP-rooted (SAP): starts from contracts/billing/returns inside ERP; service Cloud handles cases; FSM handles dispatch.
- Suite-rooted (IFS): bundles FSM + parts logistics + depot repair + warranty in one suite.

---

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant (deliberately minimal)

The Type is recognizable only if all three hold:

1. **Installed base** — a managed registry of identified, in-service product units that the organization has sold (or services under contract), attributed to customer accounts, each unit accumulating its service history. The unit is the anchor object.
2. **Service entitlement** — recorded coverage (warranty, service contract, SLA) that defines what service a unit is owed, under what terms, and until when; consulted when service is demanded.
3. **Service demand as a tracked work object** — a service request/work order attached to a specific unit, moving through a tracked lifecycle (intake → coverage determination → fulfillment → completion → settlement) to resolution.

Tests:
- Remove the installed base (service not anchored to identified sold units) → generic customer service / ticketing / generic FSM job scheduling — not this Type.
- Remove entitlement (no warranty/contract semantics) → generic work-order dispatch; the aftermarket commercial meaning disappears.
- Remove the tracked work object (only a registry + contracts) → warranty/entitlement registry or product registry — not service management.

Historical/market-sample check (per §24-style reasoning): 1990s–2000s ERP customer-service modules (installed base/equipment + warranty + service orders), aviation/defense MRO systems (as-maintained configuration + maintenance work orders + MRO agreements), and equipment dealers servicing multiple brands all satisfy this L0 without any modern specifics (no IoT, no AI scheduling, no mobile apps). Conversely, a pure warranty-claims adjudication product without work-order fulfillment does NOT satisfy element 3 — it is a narrower capability, not this Type.

### L1 — Common Mature Structure (very common, not definitional)

- Field service scheduling & dispatch (optimization by skills/location/availability/priority; dispatcher board)
- Technician mobile execution (offline-capable; work orders, asset history, checklists, time & materials capture)
- Depot repair / returns processing (RMA issuance → receiving → triage/queues → repair/replacement/exchange/return → inspection → shipment)
- Spare parts logistics & parts-on-work-order (availability check, assignment, shipment tracking)
- Preventive maintenance planning (schedules from usage/thresholds/regulatory requirements; service plans)
- Customer self-service portal (register products, request service, track progress, view asset data)
- Partner / dealer / contractor portals (external service network management)
- Invoicing / billing integration with ERP (parts consumption, labor, billing events)
- Service analytics (technician productivity, resolution times, cost to serve, service profitability)
- Remote service via IoT data (remote investigation, reduced truck rolls)
- Service→design feedback loop (service data informing product improvement)

### L2 — Variant / Optional Structure (depends on segment/industry/deployment)

- Depth of as-maintained configuration management (full service BOM + as-built lineage in PLM-rooted deployments vs. simpler asset records in FSM-rooted ones)
- Industry/regulatory overlays: medical device traceability, aerospace & defense (GEIA-STD-0007 product support data), oil & gas field conditions
- Servitization commercial models (products-as-a-service, subscription service offerings, extended warranty sales)
- Remanufacturing / circular-economy dispositions
- Multi-brand dealer service (servicing equipment the dealer did not manufacture)
- Deployment: standalone FSM platform vs. ERP-embedded service module vs. PLM-integrated service engineering vs. suite
- AI posture: AI scheduling, AI recommendations, agentic workflows (current-generation marketing across all four samples — treat as evolving L2)

### L3 — Vendor-specific (Research Notes only)

- ServiceMax: "Entitlements engine", "Service Board", "Service flow engine", built-on-Salesforce platform history, FieldFX/Asset 360 product split, Spring 2026 "Holistic Repair" release framing.
- Siemens: Teamcenter Share, PSDM/GEIA-STD-0007 packaging, IBM Maximo co-engineered integration, Salesforce SLM app.
- SAP: product naming (S/4HANA Cloud for Service, Service Cloud, FSM, Service and Asset Manager, APM), Joule/agentic AI framing, utilities-specific Service Cloud features.
- IFS: "Moment of Service" positioning, PSO (planning & scheduling optimization), 7bridges acquisition, ITAR fact sheets.

---

## Vendor-specific Findings

See L3 above. Notable: only ServiceMax's page describes a complete step-by-step depot workflow (RMA→receiving→triage→repair→inspection→shipment) at operational granularity; treat that as product-specific depth, not a Type-wide standard, though the same skeleton appears in IFS's depot module description (return authorization → inbound shipping → repair → outbound shipping → billing), which supports it as a common pattern (Layer B for the skeleton, Layer A for the step detail).

## Boundary Findings

| Neighboring Type | Test ("remove what → becomes the other Type") | Notes |
|---|---|---|
| CMMS / EAM (§16) | Serviced units are the operator's OWN production assets (not sold units at customer sites) → EAM/CMMS | Asset ownership is the wall. Vendors blur it: SAP FSM explicitly supports "asset and customer service work" in one product; Siemens integrates Teamcenter SLM with Maximo (EAM) for execution. Same work-order machinery, different asset population. |
| Field Service Management (no generic leaf in §16; Utility FSM/Telecom FSM exist in §19) | Keep scheduling/dispatch, drop the installed-base + entitlement anchoring (jobs for any customer, equipment as free text) → generic FSM | Gradient, not a wall: all four sampled products are marketed as FSM/SLM; the aftermarket Type is the asset-centric superset. The directory has no generic FSM leaf in §16, so this leaf must carry the asset-centric service market. |
| PLM (§16) | Keep as-designed/as-built data, drop in-service service execution → PLM; keep service execution, drop design linkage → pure aftermarket service | Teamcenter SLM is the explicit bridge (service BOM, feedback to design). Boundary = lifecycle stage (in-service vs. design/build), not object type. |
| Customer Service Platform / Help Desk (§07) | Cases about inquiries/billing without unit anchoring or entitlement → customer service platform | SAP itself splits: Service Cloud (cases) vs. S/4HANA returns/repair/warranty (unit-anchored). The unit-anchored work object + entitlement is the differentiator. |
| Returns Management Platform (§05.09) | E-commerce purchase returns (refund/replace an order line) vs. service returns (RMA a serialized unit for repair) | Different object (order line vs. serialized unit) and purpose (money back vs. function restored). |
| Warranty Management (no dedicated leaf in §16) | Claims adjudication/registration without work-order fulfillment → warranty management capability | Present in the sample as embedded capability (ServiceMax dealer workflows, IFS depot warranty claims, SAP contract/warranty connection), not as standalone structure. |
| MRO (aviation/defense, no dedicated leaf in §16) | Same L0; differs by as-maintained configuration depth + regulatory data exchange | Treat as industry variant unless a dedicated MRO leaf is added. |

Taxonomy observations for STATUS.md:
1. The market sells this Type under several names: aftermarket service, service lifecycle management (SLM), asset-centric field service management, customer service & returns (ERP). The leaf name "Aftermarket Service Management" is defensible but the definition must be written broadly enough to include FSM-rooted, PLM-rooted, ERP-rooted, and suite-rooted products.
2. No generic Field Service Management leaf exists in §16 (only Utility FSM and Telecom Field Service in §19). If one is ever added, the boundary documented here (installed-base + entitlement anchoring vs. generic job dispatch) should govern the split.
3. No dedicated Warranty Management or MRO leaf exists in §16; both appear in the sample as embedded capabilities/industry variants of this Type.

## Uncertainties

- No Tier 1 operational documentation was reachable for any sampled product (see Sources). Exact work-order state machines, entitlement-check timing (quotation vs. execution), and default behaviors are unverified; nothing precise is asserted.
- Siemens' SLM page does not surface entitlement/contract management explicitly; whether Teamcenter carries warranty/contract objects natively (vs. in execution systems) is unverified. L0 element 2 is supported by 3 of 4 samples directly; for PLM-rooted deployments entitlement may live in the connected execution/commercial system.
- Mid-market / aftermarket-native vendors (e.g., warranty-centric platforms) were not sampled (Mize unreachable). The claim that such products are narrower capabilities (not this Type) rests on structural reasoning, not direct observation.
- The exact relationship between this leaf and a hypothetical generic FSM leaf is a gradient; the proposed test (installed-base + entitlement anchoring) is canonical inference (Layer C), not vendor-stated.

## Final Synthesis

Aftermarket Service Management is the application Type through which a product maker (or its authorized service network) runs the in-service life of what it sells. Its world has three load-bearing structures: an **installed base** of identified sold units (each accumulating service history), **service entitlements** (warranty/contract/SLA coverage defining what each unit is owed), and **service demands** (work objects attached to specific units, tracked through fulfillment — field visit, depot repair, parts replacement, or remote resolution — to completion and commercial settlement). Everything else commonly seen — dispatch boards, technician mobile apps, RMA queues, parts logistics, self-service portals, partner networks, IoT remote service, analytics — is mature but non-defining machinery. Products differ by root system (FSM, PLM, ERP, suite) in which layer they originate and which neighbors they integrate with, but all implement the same three-structure core.
