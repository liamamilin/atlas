# Research Notes — Waste Hauling Management

Research date: 2026-09-10
Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

## Research Goal

Understand what "Waste Hauling Management" software (DIRECTORY §21 Environment, Sustainability & Climate, line 1514) actually is in the market: what system-of-record structure runs a waste hauling / collection operation, what its core objects and workflows are, and where its boundary sits against neighboring Types.

This pass carries three delegated obligations from processed siblings:

1. **junk-removal-waste-hauling-management (§29, processed 2026-09-08) — TAXONOMY FLAG / JOINT REVIEW**: the two leaves name near-identical operator-side software (hauler collection/route/billing/container/disposal systems) from two directory angles. That pass sampled the dedicated hauler market (Trash Flow, Waste Logics, Hauler Hero) plus the per-job junk-removal pole (Workiz) and recommended this pass reconcile — merge into one Type or explicitly split (municipal/program-scale hauling vs local-service junk-removal business operations), with disposal-side machinery (scale house/tip tickets/material destinations) and compliance paperwork as the likely §21-tilting elements.
2. **recycling-operations-management (§21, processed 2026-09-09)**: seam = the recovery ledger (classification-to-stock + commodity-out) vs the collection business (routes/service customers/service billing); scale+ticket machinery is shared substrate (Soft-Pak scale module probes this), so this pass must hold dispatch/route/service-billing as its center and NOT claim the material ledger.
3. **hazardous-waste-management (§21, processed 2026-09-08)**: hauler-side business operations (customers/routes/crews/billing) vs generator-side compliance record; the §29 junk-removal pass already held compliance manifests standard-NOT-definitional on the hauler side, symmetric to that pass holding truck dispatch outside.

## Initial Boundary

- DIRECTORY position: §21 Environment, Sustainability & Climate, among waste leaves (Waste Management Platform, Hazardous Waste Management, Recycling Operations Management, Waste Hauling Management, Circular Economy Platform). So the leaf is read from the **environmental-operations angle**: the waste collection business/operation as an environmental service.
- The §29 sibling leaf "Junk Removal / Waste Hauling Management" (line 2125) names near-identical software from the local-service-business angle — suspected duplicate (see Boundary Findings; this is the pass's central reconciliation deliverable).
- Initial hypothesis (to verify): the hauler-side system of record — served customers/locations with configured collection services, service events dispatched to truck crews, billing from recorded service — with the §21 tilt being municipal/program-scale context, disposal-side capture, and regulatory paperwork as standard/variant capabilities rather than a separate structure.

## Research Questions

1. What are the core objects: customer/service accounts, stops/orders/jobs, trucks/routes, containers, disposal events?
2. How does work flow: request → booking → scheduling/dispatch → field execution → billing → disposal documentation?
3. Does the enterprise/municipal pole (AMCS, Routeware SmartCity) carry the same spine as the small-hauler pole (Trash Flow, Hauler Hero)?
4. What does the municipal/government pole add or drop (billing? SLAs? multi-service: street cleansing, snow, sweeping)?
5. How deep does the disposal side go inside hauler products (scale/weighbridge, tip tickets, material destinations) — shared substrate or separate Type?
6. Does compliance paperwork (duty of care, consignment notes, digital waste tracking) become definitional in any market?
7. Does the roll-off/liquid-waste pole (CRO) carry the same spine?
8. Is the §21 leaf the same Type as the §29 junk-removal sibling — merge or split?

## Representative Products

Selected for market representation, different product philosophy, different customer layer, and §21-tilt coverage (enterprise/municipal scale, roll-off specialist, non-US regulatory market). Deliberately avoids re-sampling the §29 pass's products as primary samples (Trash Flow, Hauler Hero, Workiz are used as cross-referenced evidence only; Waste Logics re-fetched to verify §21-tilting elements).

| Product | Pole | Philosophy / layer | Docs reached |
|---|---|---|---|
| AMCS Platform (+ Platform for Municipalities) | enterprise/municipal flagship | enterprise-grade SaaS for waste & recycling operations; commercial & industrial, municipal, C&D, recycling, hazardous; 5,000+ customers (Recology, SUEZ UK) | vendor root + /solutions/amcs-platform/ + /solutions/amcs-platform-for-municipalities/ |
| Routeware (Elements + SmartCity) | hauler + government | cloud, hardware-light, BYOD; hauler suite (Elements) and municipal suite (SmartCity); 1,500 customers incl. Casella, Waste Pro, cities of Austin/Atlanta/Denver/Vancouver | vendor root + /products/routeware-elements/ + /products/routeware-smartcity/ |
| CRO Software | roll-off / liquid / solid waste ERP | ERP for owner-operators to multinationals; liquid waste, solid waste, roll-off & dumpster, scrap & recycling; now part of RapidWorks | vendor root (crosoftware.net) |
| Waste Logics | UK trade waste / skip hire / MRF / broker | cloud end-to-end waste business automation; usage-priced; weighbridge + compliance + Digital Waste Tracking | vendor home (re-fetched; extends §29 pass observations) |

Cross-referenced (not re-sampled): Trash Flow, Hauler Hero, Workiz (§29 pass, 2026-09-08); Soft-Pak (§21 recycling pass, 2026-09-09).

Rejections / gaps: none this pass — all four primary sources fetched on first attempt. No Tier-1 help-center/user-manual articles attempted beyond vendor product pages (consistent with the §29 pass finding that help centers are unreachable/timeout-prone in this environment; product pages are the reachable official layer).

## Sources

- AMCS — https://www.amcsgroup.com/ (root), https://www.amcsgroup.com/solutions/amcs-platform/ , https://www.amcsgroup.com/solutions/amcs-platform-for-municipalities/ — fetched 2026-09-10
- Routeware — https://routeware.com/ (root), https://routeware.com/products/routeware-elements/ , https://routeware.com/products/routeware-smartcity/ — fetched 2026-09-10
- CRO Software — https://www.crosoftware.net/ (root; redirects crosoftware.com content) — fetched 2026-09-10
- Waste Logics — https://wastelogics.com/ (home incl. features/plugins/FAQ) — fetched 2026-09-10
- Cross-referenced: research/junk-removal-waste-hauling-management.md (2026-09-08: Trash Flow, Waste Logics, Hauler Hero, Workiz); research/recycling-operations-management.md (2026-09-09: Soft-Pak probe, AMCS separate-solutions observation); research/hazardous-waste-management.md (2026-09-08)

Evidence layers used below: **[A]** directly observed on an official page of one product; **[B]** observed across multiple products; **[C]** canonical inference from cross-product comparison + boundary reasoning.

## Product A — AMCS Platform (enterprise/municipal flagship)

### Key observations [A unless noted]

- Positioning: "AI-enabled, end-to-end solution for waste and recycling operations"; enterprise-grade SaaS; industries: Commercial & Industrial, Construction & Demolition, Municipal and Residential Services, Recycling, **Hazardous waste**, Specialist waste and recycling. Customers include Recology, SUEZ recycling and recovery UK.
- The platform page enumerates seven operational stages — this is the cleanest vendor statement of the Type's internal structure:
  1. **Customer management** — "entire customer lifecycle — from onboarding and relationship management to contract and pricing hierarchy setup, including pricing automation"; self-service portals for customers, subcontractors, and trading partners.
  2. **Transport optimization** — "advanced route planning, dispatch, real-time tracking, transport validation, and master routing to cut mileage, fuel costs, and emissions. Use AI-powered contamination and overfill detection to identify **chargeable incidents**, reduce revenue leakage, and protect margins."
  3. **Mobile workforce** — field teams with "navigation, customer updates, photo capture, and fully connected end-to-end workflows."
  4. **Scale operations** — "accelerate accurate weigh-ins and material tracking with integrated, driver-friendly workflows designed to improve control and reduce errors."
  5. **Material and inventory** — "control of material flow and inventory with intelligent workflows, real-time planning, and cost tracking. Strengthen supplier collaboration through dedicated portals." (Material flow inside waste ops — NOT the recycling commodity ledger; AMCS ships metal recycling as a separate solution, per the recycling pass's observation.)
  6. **Financial automation** — "automate invoicing, payment processing, and account management with fully digital, accurate financial workflows."
  7. **Business intelligence** — real-time dashboards, self-service AI analytics, REST APIs.
- FAQ definition [A]: "Waste and recycling software is a system that helps companies manage, track, and optimize waste collection, recycling operations, trading and disposal processes."
- **Municipal variant** (Platform for Municipalities): "connected municipal waste solution that helps cities automate and manage waste services through a single, modern software platform." One solution for every municipal waste service: **Waste + Recycling Collections, Street Cleansing, Winter Maintenance, Bulky Waste Pickups, Vandalism/Graffiti removal, Public Bin/Asset Management, Public/Space/Park Maintenance, + Other Configurable Services**. Configurable services/tasks/workflows/SLAs; office/depot/field; "Meet SLAs, reduce missed pick-ups." Municipal pole = the same platform configured for multi-service municipal operations, not a different product family.

## Product B — Routeware (Elements for haulers + SmartCity for governments)

### Key observations [A unless noted]

- Elements page title: "**Waste Hauling Software for Haulers**" — the vendor's own name for the category matches the leaf name.
- Three-operations grouping (same on both hauler and government suites): **Collection Operations** (Route Optimization, Dispatch, In-Cab, Fleet & Equipment Reporting), **Customer Operations** (Customer Service, Customer Education & Outreach, Self-Service Tools), **Business Operations** (Compliance, Billing, Payments). Specialty Services: Medical Waste, Site Services, Regulation & Sustainability Reporting.
- Elements (hauler suite): Dispatch — "single view of trucks, orders, status"; Billing — "digital billing audits, invoicing, adjustments, and order creation… low processing rates and auto-pay"; Customer Service — "digital CRM… single-view of customer details, account status, service orders… customer portals support easy two-way communication and self-service." FAQ: migration "from alternative **trash billing systems**"; online payments.
- Partner integrations: Samsara, Geotab (telematics), Worldpay (payments), MyTruckScales (scales); Esri (GIS) on the government suite.
- **SmartCity (government suite)**: "Municipal Waste Software"; in-cab tools (apps, sensors, AI cameras), dispatch ("single view of trucks, orders, status"), customer service CRM ("single-view of customer details, service history"), customer portals. 150+ cities. **Notably, SmartCity's solution list shows Collection Operations + Customer Operations but NOT Business Operations (billing/payments)** — direct evidence that the municipal self-operated pole can run the collection core without the billing module. FAQ: "increased income from **chargeable services** can also add to the payback"; go-backs and customer service admin "fall away". Same platform also runs **snow operations and street sweeping** ("built for a range of heavy-duty public works fleets") — the municipal pole extends the same collection-operations machinery to non-waste municipal services.
- Customer stories: Casella (route optimization across acquisitions), City of Kansas City, Falkirk Council ("20% decrease in missed bin calls"), City of Concord.

## Product C — CRO Software (roll-off / liquid / solid waste ERP)

### Key observations [A unless noted]

- Positioning: "the leading ERP software solution for owner/operators to multinational organizations in the waste and recycling, liquid and solid waste, and construction and demolition industries." Single-truck owner/operators to multinational, publicly traded organizations.
- Industries served: **Liquid Waste** (portable toilets, septic, grease pumping), **Solid Waste** ("advanced routing, scheduling, and invoicing"), **Roll-Off & Dumpster** ("streamline dumpster rental operations with advanced scheduling, invoicing, and route optimization"), **Scrap & Recycling** ("precise scheduling, bin tracking, and route optimization").
- Advanced Data Solutions: "Eliminate Double Data Entry… **Automatic Data Transfers: Activity-based updates ensure completed tasks, whether in-field or office, instantly sync with records and invoices**"; "Intuitive Single-Screen Display."
- One platform connecting "clients, sales team, drivers, dispatchers, assets, accountants, and managers."
- Customer-review evidence (vendor-published testimonials) [A, third-party voice]: trucks "set up… by weight, rolloff and hooklift and different types of bins **so our dispatchers wont send the wrong truck to service the container**" — capability-matched dispatch; "requests that were set up as **reoccurring** all went unassigned from a truck" — recurring service requests assigned to trucks; "see the customers history right on the main deployment page"; drag-and-drop dispatching; QuickBooks integration; asset tracking (bins, portable toilets, ~2,000 units).

## Product D — Waste Logics (UK trade waste / skip hire / MRF / broker)

### Key observations [A; re-fetch confirms and extends §29 pass]

- Positioning: cloud "end-to-end waste management business automation"; used by skip hire companies, trade waste collection businesses, MRFs, waste transfer stations, waste brokers, tippers/aggregates, commodity trading firms, scrap metal processors.
- Module set: CRM (prospective + existing customers, opportunities/tasks, 12-month pipeline); Online Cart (quote → book → pay on the hauler's website, auto-synced); Order Management ("book orders, monitor availability of resources and track current orders from order to invoice"); Logistics (drag-and-drop rounds optimization, paper/paperless driver tickets); Brokerage & Subcontractor Portal (subcontract work, profit margin per job, auto-email POs); Billing (flexible sales invoices, self-bills, supplier invoice matching); Accounting integrations (Sage, QuickBooks, Xero, Pegasus Opera, SAP Business One, KashFlow); Driver Apps (vehicle checks, run sheet, navigation, e-signature, issues, photos, offline); **Weighbridge & Compliance** (live weighbridge link or manual weights, compliance issues with loads, deductions, photos); Customer Portal (copy invoices, e-tickets, recycling reports, booking, updates); Analytics (KPIs, custom dashboards, profit per round, landed price analysis, debtor management).
- §21-tilting elements confirmed [A]: "Electronically signed annual **duty of care** notes"; "Auto generated tickets and **consignment notes**"; "Waste Logics automatically generates key compliance documents using the information already stored in the system" (FAQ: Duty of Care and **Hazardous Waste Consignment Notes**); **Digital Waste Tracking** page — "foundational integration work… Focused Digital Waste Tracking development is planned ahead of the **October 2026 mandatory deadline**" (UK regulatory context); bin weigh systems and RFID integrations; weighbridge management "track all materials in and out of facilities"; recycling rates, CO₂ impact, ESG software integrations (SmartWaste, Sustain IQ).
- Containers [A]: "record and manage all of your containers in one system, including their type, size, location and movements… on site, out on hire, or due for collection."

## Cross-referenced evidence (from processed sibling passes)

- **Trash Flow, Hauler Hero, Workiz** (§29 pass, 2026-09-08): dedicated hauler products carry customer accounts with configured services/prices, work orders/stops dispatched to drivers/trucks, field execution capture (photos, exceptions, signatures), billing from recorded service, container tracking with placement state, scale-house/landfill ticketing (TipTicket), route management with as-run reordering, customer portals. Workiz shows the per-job junk-removal pole running on generic field-service machinery with no containers/rounds/scale.
- **Soft-Pak** (§21 recycling pass, 2026-09-09): entire suite hauler-centric (operations, in-cab, routing, billing); Scale-Pak (truck scales) one module — scale/ticket machinery is shared substrate, not a separate Type.
- **AMCS ships metal recycling as a separate solution** from its waste platform (recycling pass observation) — vendor-side confirmation that the collection business and the material-recovery ledger are held apart by the market.

## Cross-product Comparison

| Structure | AMCS | Routeware (Elements/SmartCity) | CRO | Waste Logics | Trash Flow* | Hauler Hero* | Workiz* (junk pole) |
|---|---|---|---|---|---|---|---|
| Customer/service accounts with configured services + prices + history | ✓ (lifecycle, contracts, pricing hierarchy) | ✓ (CRM single view, account status) | ✓ (customer history on dispatch screen) | ✓ (CRM + orders) | ✓ | ✓ | ✓ |
| Haul service event as unit of work (stop/order/job) | ✓ (orders; chargeable incidents) | ✓ (orders, stops) | ✓ (requests/jobs, recurring) | ✓ (orders) | ✓ (work orders) | ✓ (stops, services) | ✓ (jobs) |
| Dispatch to truck/driver/crew | ✓ (dispatch, master routing) | ✓ (single view of trucks/orders/status) | ✓ (drag-drop; capability-matched trucks) | ✓ (rounds, run sheets) | ✓ | ✓ | ✓ |
| Field execution capture (completion, exceptions, evidence) | ✓ (mobile workforce: photos, updates) | ✓ (in-cab, alerts, video) | ✓ (in-field sync to records/invoices) | ✓ (e-signature, photos, issues, offline) | ✓ | ✓ | ✓ |
| Billing generated from recorded service | ✓ (financial automation, invoicing) | ✓ (Elements billing; **absent from SmartCity product scope**) | ✓ (invoicing; QuickBooks) | ✓ (order→invoice, self-bills) | ✓ | ✓ | ✓ |
| Recurring routes/rounds | ✓ (route planning, master routing) | ✓ (route optimization) | ✓ (recurring requests) | ✓ (rounds, profit per round) | ✓ | ✓ | route planning only |
| Containers as placed assets | ✓ (public bin/asset mgmt; container context) | (not detailed on fetched pages) | ✓ (bins, roll-offs, portable toilets) | ✓ (type/size/location, on hire) | ✓ (placement slots) | ✓ (inventory) | — |
| Disposal-side capture (scale/weighbridge, tickets, destinations) | ✓ (scale operations stage) | ✓ (MyTruckScales integration) | (bin tracking; not detailed) | ✓ (weighbridge, e-tickets) | ✓ (TipTicket, MAT Track) | ✓ (scale integration) | — |
| Compliance paperwork (duty of care/consignment/manifests) | (hazardous listed as industry; not detailed) | ✓ (Compliance product; Regulation & Sustainability Reporting) | — | ✓ (duty of care, consignment notes, DWT) | — | — | — |
| Municipal multi-service extension (cleansing/snow/sweeping) | ✓ (Platform for Municipalities) | ✓ (SmartCity: snow, sweeping) | — | — | — | (governments segment) | — |
| Customer portal / self-service | ✓ (portals: customers, subcontractors, trading partners) | ✓ (portals, self-service) | ✓ (client connection) | ✓ (portal, online cart) | ✓ (Web Pay) | ✓ | ✓ |
| Brokerage / subcontracting | ✓ (subcontractor portals) | — | — | ✓ (brokerage portal, self-bills) | — | — | — |
| Recycling/diversion & sustainability reporting | ✓ (BI; sustainability suite) | ✓ (Regulation & Sustainability Reporting) | — | ✓ (recycling/CO₂ reports, ESG integrations) | — | — | — |
| Accounting integration | ✓ (financial automation) | ✓ (payments partners) | ✓ (QuickBooks) | ✓ (Sage/Xero/etc.) | ✓ | ✓ (APIs) | ✓ |

\* = observed in the §29 pass (2026-09-08), carried as cross-referenced evidence.

**[B] jointly held by all dedicated hauler products (6 of 6):** customer/service accounts with configured services and prices; the haul service event as unit of work; dispatch to truck/driver/crew; field execution capture; billing generated from recorded service (with the SmartCity municipal edge noted below); customer self-service surfaces; accounting integration.

**[B] held by dedicated products, absent from the generic-FSM junk pole:** recurring routes/rounds; containers as placed assets; disposal-side capture; hauling-specific KPIs.

**[A] single-product:** municipal multi-service extension (AMCS, Routeware SmartCity — two products, one pole); SmartCity shipping without the billing module; capability-matched truck/container dispatch (CRO); UK duty-of-care/consignment/DWT machinery (Waste Logics); brokerage self-billing (Waste Logics, AMCS subcontractor portals).

## Canonical Model

### Level 0 — Defining Invariant [C, supported by B evidence across 6 dedicated products + the §29 pass]

The hauler-side system of record for a waste collection/hauling operation, defined by three jointly-held structures plus the domain binding:

1. **Customer service accounts of record** — each served customer/location held persistently with its configured haul services and prices (what gets collected, how often or on request, at what container/size terms), accumulating service history. Remove → contact list / rate card, not a business system.
2. **The haul service event dispatched to truck crews** — the stop/order/job as the unit of work: material to be collected at a location, scheduled (recurring round or booked slot) or taken on demand, assigned to a truck/driver/crew, with execution recorded back (completion, exceptions, evidence). Remove → static customer database or a bare dispatch board.
3. **Billing generated from recorded service** — completed events and their attached charges are priced to the account and flow into invoices/payments. At the municipal pole the money loop may run through contract billing and chargeable services rather than per-customer invoicing (one sampled government suite ships without a billing module); the recorded-service-drives-the-account loop remains. Remove → dispatch tool with no revenue/accountability loop.

**Domain binding:** the cargo is unwanted material **leaving** the customer's site toward disposal/transfer/recovery; the mobile unit is the **truck and its crew**. [C]

Jointly-held is load-bearing:
- 1 alone = CRM/rate card; 2 alone = dispatch board; 3 alone = generic invoicing.
- 1+3 without 2 = a billing system (the "vs accounting package" seam).
- 1+2 without 3 = dispatch software with no financial loop (commercial pole fails; municipal pole degrades to chargeable-extras capture).
- 2+3 without 1 = one-off jobs with no served population.

### Historical / market-sample check [§24 discipline]

- Paper-era hauler office (route books/run sheets + customer cards with rates + trip tickets + dump tickets + billing ledger) satisfies all three legs at analog level. ✓ (carried from §29 pass)
- Paper-era municipal sanitation department: route books + resident service cards + missed-collection/complaint log + extra-work orders, with money running through contract billing (contracted operation) or chargeable-extras receipts (self-operated) — satisfies legs 1+2 and the money leg in its contract/chargeable form. ✓
- UK trade-waste/skip-hire pole satisfies without US roll-off vocabulary; duty-of-care paperwork is a regulatory variant. ✓
- Liquid-waste pole (septic/grease/portable toilets, CRO) satisfies the same spine with liquid cargo. ✓
- Per-job junk removal on generic field-service software satisfies legs 1–3 with none of the route/container/scale machinery. ✓ — the Type holds at maximum abstraction only if routes, containers, scale houses, compliance paperwork, and municipal multi-service are NOT required.

### Level 1 — Common Mature Structure [B for dedicated products]

- recurring routes/rounds: run sheets, stop reordering, route optimization, master routing, GPS fleet tracking
- driver/in-cab mobile capture: offline tolerance, photos, e-signature, exception reporting, navigation, vehicle/truck inspections; in-cab tablets/sensors/AI cameras at the enterprise end
- containers as placed assets (roll-off/skip/dumpster/cart lifecycle: drop → filled → pull; placement/on-hire state; rental terms; billing attached to placed service rather than serial number)
- disposal-side capture: scale-house/weighbridge weights, tip/dump tickets, material origins/destinations, overload/overfill billing; bin-weigh and RFID integrations
- customer self-service: portal (invoices, e-tickets, service history, recycling reports), online booking/cart, online payments, auto-pay
- exception/follow-up triage (missed-service, complaints, go-backs)
- hauling KPIs (pulls per day, yards per hour, profit per round, cost-per-stop class) and accounting-system integrations
- pricing machinery: per-customer pricing hierarchies, hauling rate types (base collection, extras, container rental, disposal/tip fees, overweight charges), pricing automation at the enterprise end
- recycling/diversion and sustainability reporting (recycling rates, CO₂), ESG-software integrations

### Level 2 — Variant / Optional Structure

- **Service-model pole**: (a) recurring route collection (residential/commercial rounds); (b) roll-off/skip/container services (container rental + pull cycle); (c) per-job removal (junk pole — frequently run on generic field-service platforms; see §29 sibling); (d) liquid waste (septic/grease/portable toilets).
- **Customer segment**: residential / commercial & industrial / construction & demolition / government-municipal contracts.
- **Operator type**: private hauler; municipality self-operating its collection fleet; waste broker with subcontractor portals and self-billing.
- **Municipal multi-service extension**: the same collection-operations machinery configured for street cleansing, winter maintenance, street sweeping, bulky waste, graffiti removal, public bins, parks (AMCS municipal, Routeware SmartCity) — a configuration of the Type, not a separate Type.
- **Regulatory context**: UK duty-of-care notes + hazardous-waste consignment notes + Digital Waste Tracking (October 2026 mandatory deadline); US scale-house practice; overweight enforcement. Machinery is regime-shaped; presence of some disposition documentation is standard at the dedicated end, not definitional.
- **Specialty waste lines**: medical waste, site services (Routeware specialty services); hazardous waste as an industry served by the enterprise platform (AMCS lists it; machinery not detailed on fetched pages).
- **Deployment/era**: legacy Windows desktop module suites (billing-led) through modern cloud SaaS (dispatch/driver-app-led); hardware-light BYOD vs in-cab hardware.

### Level 3 — Vendor-specific Structure (Research Notes only)

- AMCS: seven-stage platform enumeration; agentic AI framework; Vision AI contamination/overfill detection; Wastedge (ANZ); AMCS Pay; Recology/SUEZ customer evidence.
- Routeware: Elements/SmartCity/ReCollect/RCC/EnCore/EasyRoute/Recyclist/Compliance Publishing product names; "Hauler Hero"-style marketing figures (21% mileage reduction, $2M savings, 20% missed-bin-call decrease — vendor claims, not carried); MyTruckScales/Worldpay/Samsara/Geotab/Esri integrations; "deployed in under 90 days".
- CRO: RapidWorks acquisition; liquid/solid/roll-off/scrap industry pages; capability-matched truck setup (weight/rolloff/hooklift/bin types); AWS hosting/trust-center claims.
- Waste Logics: usage-based subscription; named accounting packages; Connect SMS; October 2026 Digital Waste Tracking deadline; SmartWaste/Sustain IQ integrations; "6.5 days per user per month" marketing figure.

## Vendor-specific Findings

See Level 3. AMCS's seven-stage enumeration and Routeware's three-operations grouping are two vendor views of the same underlying structure (accounts → events → trucks/routes → money), not competing models. CRO's capability-matched dispatch is an implementation of container/truck matching. Waste Logics's compliance-document generation is the UK-regime realization of disposition paperwork.

## Rejected Findings

- "Municipal multi-service software is a different Type" — rejected: AMCS municipal and SmartCity are the same platform/product family configured for additional municipal services; the collection core is identical. Held as variant.
- "Compliance paperwork is definitional" — rejected: present strongly in one market (UK) and one specialty product line; absent from the US junk pole and several US products; the §29 pass already held manifests standard-NOT-definitional on the hauler side. Held as regulatory variant.
- "Scale/disposal machinery is a separate Type" — rejected as a *separate* Type: it is standard shared substrate inside dedicated hauler products (AMCS scale operations, Trash Flow TipTicket, Waste Logics weighbridge, Soft-Pak Scale-Pak, Routeware MyTruckScales integration). The *facility-side* material ledger remains a separate Type (Recycling Operations Management) — this pass does not claim it.
- "AI contamination detection is core" — era-current single-vendor packaging (AMCS Vision AI); rejected for the Type.
- Marketing performance figures (21%, 20%, $2M, 6.5 days) — unverifiable vendor claims; rejected.
- "Billing is definitional in all configurations" — qualified: SmartCity (government suite) ships without the billing module; the money leg holds through contract billing/chargeable services at the municipal pole. Leg 3 wording adjusted accordingly.

## Boundary Findings

1. **vs Junk Removal / Waste Hauling Management (§29, processed 2026-09-08) — THE RECONCILIATION DELIVERABLE.** The two leaves name **one Application Type**: the hauler-side waste/junk collection business system of record. Evidence: (a) this pass's samples (AMCS, Routeware, CRO, Waste Logics) are the same dedicated-product population the §29 pass sampled (Trash Flow, Waste Logics, Hauler Hero); (b) Routeware's own page title for its hauler suite is "Waste Hauling Software for Haulers" — the §21 leaf name is the market's name for the §29 leaf's dedicated pole; (c) the §29 pass's L0 (three jointly-held structures + domain binding) is confirmed without modification against all four new samples; (d) the §21-tilting elements the §29 pass predicted (municipal/program-scale context, disposal-side capture, compliance paperwork) are all **standard or variant capabilities** of the same Type, not a separate structure — the municipal pole is a configuration (AMCS municipal, SmartCity), disposal-side capture is shared substrate, compliance paperwork is regime-shaped variant. **Holding: duplicate leaves; recommend merge** (retain one leaf, alias the other). The two realizations the §29 pass held (per-job junk removal; route-based waste hauling) remain realizations of the one Type. Recorded in STATUS.md Boundary Issues; no directory change made from this side.
2. **vs Recycling Operations Management (§21, processed 2026-09-09)** — flag honored: this pass holds dispatch/route/service-billing as the center and does NOT claim the material ledger. Disposal-side capture (scale/weighbridge/tickets) is shared substrate; the recovery loop (classification-to-stock + commodity-out) belongs to recycling ops. AMCS shipping metal recycling as a separate solution corroborates from the vendor side. Remove the collection business (routes/service customers/service billing) and this Type disappears into facility-side software; remove the material-processing loop and a hauler product remains this Type.
3. **vs Hazardous Waste Management (§21, processed 2026-09-08)** — flag honored: hauler-side business operations vs generator-side compliance record. Compliance manifests/duty-of-care paperwork held standard-NOT-definitional on the hauler side (symmetric to that pass holding truck dispatch outside its core). AMCS lists hazardous waste as a served industry; the machinery is not detailed on fetched pages and is not claimed.
4. **vs Waste Management Platform (§21, unprocessed)** — held conceptual (weak wording, consistent with the §29 pass): organization- or municipality-side waste *program* management (contracts, compliance, reporting across sites/contractors) vs the hauler's own *operations* system of record. That pass should test the three-way §21 seam (disposal ops / regulated-waste compliance record / recovery-ops ledger) and confirm this leaf as the collection-business pole.
5. **vs Small Business Field Service Management (§29, processed 2026-09-09)** — the per-job junk pole runs on generic FSM; the dedicated hauler structures generic FSM lacks are containers as placed assets, recurring rounds, disposal legs, weight/volume billing (consistent with both prior passes' holdings).
6. **vs Moving Company Management (§29, processed 2026-09-08)** — same truck+crew shape; moving cargo goes between two customer-controlled points; hauling cargo leaves the site toward disposal. Different pricing semantics.
7. **vs Municipal resident-request / 311 surfaces (§24, unprocessed)** — resident requests/complaints feed this Type's customer-service and exception machinery (Routeware ReCollect/SmartCity resident engagement), but the resident-facing request platform is a different surface; this Type is the operator's system of record.
8. **vs Fleet Management / Vehicle Telematics / Route Optimization (§18)** — capability vs business system of record; telematics/routing integrate in (Samsara, Geotab, Esri) but carry no service accounts, service events, or billing.
9. **vs Trucking Management System (§18, processed 2026-09-10)** — both are truck-fleet business systems, but TMS-for-carriers centers freight loads hauled for customers between points under carrier operating identity; hauling centers recurring collection service at served locations with disposal-side semantics. Different unit of business record (load vs service account/event).

## Uncertainties

- No Tier-1 help-center/user-manual articles reached (consistent with the §29 pass); all observations are official-product-page grade. Exact screen workflows, status names, numeric limits, and defaults are NOT asserted anywhere.
- AMCS's hazardous-waste machinery and "material and inventory" depth: pages fetched do not detail them; deliberately not characterized beyond "listed as served industry / material flow within waste ops."
- Whether any dedicated product positions itself as *only* municipal (no commercial billing at all): SmartCity ships without a billing module, but Routeware markets Elements (with billing) to the same company types; the fully billing-free municipal configuration is inferred from product scope, not observed in operation.
- Roll-off-only specialists (e.g., Docket) remain unsampled (JS-shell site, per §29 pass); the roll-off pole is evidenced through CRO's roll-off industry page + Trash Flow/Hauler Hero container machinery.
- The exact boundary behavior of "Site Services" and "Medical Waste" specialty lines (Routeware) is unverified beyond the menu labels.
- Digital Waste Tracking integration (Waste Logics) is pre-deadline ("planned ahead of the October 2026 mandatory deadline") — capability claimed as in development, not observed as shipped.

## Final Synthesis

Waste Hauling Management is the waste collection operation's system of record. The defining core is three jointly-held structures: (1) the customer service account of record — each served customer/location with its configured haul services and prices, accumulating service history; (2) the haul service event dispatched to truck crews — stop/order/job as the unit of work, executed and recorded back with completions, exceptions, and evidence; (3) billing generated from recorded service — completed events priced to the account into invoices/payments (contract billing and chargeable services at the municipal pole). The domain binding — waste leaving customer sites toward disposal, performed by truck crews — makes it hauling rather than generic field service or freight carriage.

Around this spine, mature dedicated products add: recurring routes/rounds, containers as placed assets, disposal-side capture (scale/weighbridge, tip tickets, material destinations), driver/in-cab capture, customer self-service, pricing machinery, hauling KPIs, and recycling/sustainability reporting. Variants span service model (route collection, roll-off/skip, per-job removal, liquid waste), customer segment (residential/commercial/C&D/municipal), operator type (private hauler, self-operating municipality, broker), regulatory regime (UK duty-of-care/DWT machinery), and deployment era. The municipal pole extends the same machinery to multi-service municipal fleet operations (cleansing, snow, sweeping) — a configuration, not a separate Type.

**Reconciliation holding:** the §21 leaf and the §29 sibling (Junk Removal / Waste Hauling Management) name the same Application Type; the market realizes one Type whose dedicated-product population both passes sampled. Recommended: merge the leaves. This document and the §29 document describe the same Type from the environmental-operations and local-service angles respectively; their defining cores agree.
