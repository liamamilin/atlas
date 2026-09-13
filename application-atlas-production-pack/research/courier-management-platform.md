# Research Notes — Courier Management Platform

Research date: 2026-09-07
Slug: courier-management-platform
Directory leaf: Courier Management Platform (§18 Transportation, Mobility & Logistics)

---

## Research Goal

Understand what a Courier Management Platform actually is as an Application Type, from real products:

- What is the unit of record around which the system revolves?
- Who runs it (which organization) and who uses it day to day?
- What workflows does the system carry (order → dispatch → pickup → delivery → billing)?
- What states, rules, and exceptions shape behavior?
- Where is the boundary against the dense cluster of neighboring Types in §18 (Last-mile Delivery Platform, On-demand Delivery Platform, Dispatch Management, Proof of Delivery Platform, Shipment Visibility Platform, Parcel Management Platform, Trucking Management System)?

## Initial Boundary (working hypothesis before research)

A Courier Management Platform is suspected to be operator-side software: run by a courier/delivery company (the operator) to run its own delivery business. Nearest confusion risks:

- **Last-mile Delivery Platform** — shipper/retailer-side delivery orchestration; same execution substrate, different tenant.
- **On-demand Delivery Platform** — consumer-facing instant delivery.
- **Dispatch Management** — generic field-workforce dispatch, industry-agnostic.
- **Proof of Delivery Platform / Shipment Visibility Platform** — capability slices.
- **Trucking Management System** — load-based long-haul trucking, not per-piece pickup→delivery.
- **Parcel Management Platform** — suspected shipper-side multi-carrier shipping management.

## Research Questions

1. What is the core object (courier order / shipment / job) and what does it carry?
2. How do orders enter the system (portal, API, EDI, phone, import)?
3. How does dispatch work — manual, assisted, automated? What is the unassigned→assigned flow?
4. What does the courier/driver do in the field, and on what device surface?
5. What is the status lifecycle of an order, and how is delivery confirmed (POD)?
6. How does pricing work (contracted rates, zones, distance, accessorials) and how does billing flow to customers?
7. Do platforms pay couriers/drivers from the same system (settlement/wages)?
8. What customer-facing surfaces exist (portal, tracking, invoices)?
9. What work-mix exists (on-demand single jobs vs scheduled/recurring routes)?
10. Which capabilities are definitional vs common vs optional/variant?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Evidence tier used |
|---|---|---|
| OnTime 360 (Vesigo Studios) | Classic, long-standing courier software; SMB→mid couriers; desktop-heritage "Smart Client", very feature-rich feature page | A (direct: homepage + full features page) |
| Dispatch Science | Modern cloud-native TMS "purpose-built for last-mile couriers"; role-structured product pages (Customer / Driver / Dispatcher / Back Office) | A (direct: homepage + dispatcher + back-office feature pages) |
| CXT Software | Courier + routed + on-demand TMS; healthcare/lab/chain-of-custody emphasis; multi-brand enterprise posture; hub named "Operations App" | A (direct: homepage + operations feature page) |
| Elite EXTRA | Routing/dispatch-engine-centric last-mile suite; couriers + distributors; third-party delivery network + returns modules | A (direct: homepage / suite overview) |

Note: CXT Software and e-Courier are operated under a common parent (Ionic Partners) per CXT's site; e-Courier was not separately researched.

## Sources

- OnTime 360 — https://ontime360.com/ and https://ontime360.com/features (accessed 2026-09-07)
- Dispatch Science — https://www.dispatchscience.com/, https://www.dispatchscience.com/software-features/dispatcher/, https://www.dispatchscience.com/software-features/back-office/ (accessed 2026-09-07)
- CXT Software — https://cxtsoftware.com/ and https://cxtsoftware.com/operations/ (accessed 2026-09-07)
- Elite EXTRA — https://eliteextra.com/ (accessed 2026-09-07)

Source-access limitation: all fetches were of vendor product/marketing/feature documentation (Tier 1–2). Article-level help-center content and driver documentation were not fetched for any product. No API reference pages were fetched. Consequently, precise operational facts (exact status-state names, numeric limits, default timeouts, per-plan feature gating) are NOT asserted anywhere; lifecycle states are described conceptually.

---

## Product Observations

### OnTime 360 (Evidence layer A — directly observed)

Positioning: "courier software", "delivery management software for couriers and last mile"; serves "delivery businesses, carriers, freight brokers, messengers, dispatching services, and couriers". Product structure: Management Suite, Dispatch app, Mobile driver app, Customer Web Portal, API.

Key observations:

- **Order as unit**: "Tracking View — the tracking table displays every order in the system"; orders sorted/filtered/searched; real-time status; reassign packages to different drivers "while OnTime takes care of all the necessary notifications"; smart cancel "notify the appropriate people".
- **Order entry**: dispatcher order entry loads a customer profile with "all unique requirements" (collection/delivery points, pricing, notifications, options); auto-complete; quick quotes can be "placed on hold" with a reference number.
- **Unassigned queue**: "Orders submitted into the system that are not associated with a driver are placed into the unassigned queue… Drag a driver over a shipment to assign that order to that driver." Driver self-dispatch from the unassigned queue exists ("allows drivers to assign themselves those shipments from the field").
- **Rate/pricing machinery**: "Price Sets — maintain the prices charged to customers AND the wages paid to employees and subcontractors"; per-customer contracted rates; "Price Modifiers" as building blocks for accessorial charges; dimensional weight factors; zones + postal-code→zone recommendation feeding "real-time pricing quotes".
- **Billing**: "Billing Management — generating invoices and posting payments… automatically generated invoices… billing cycle to gather the right shipment information for the right customer"; invoice customization; QuickBooks/FreshBooks/Xero posting.
- **Driver pay**: time clock (clock in/out, time logged, distance, orders processed) + wage calculation from price sets.
- **Driver app**: assignment queues (direct assignments + unassigned), self-dispatch, easy POD entry ("drivers click 'Done'"), picture POD at collection/transit/delivery, COD + on-screen signature capture prompted per order options, barcode scanning (keyed/scanned; matches shipments server-side), GPS position to dispatch, offline work with auto-sync, customizable home screen.
- **Dispatch surface**: driver tracking (clocked-in state, location, queued assignments, last interaction), messaging (email/text/push), status color coding for past-due/impending orders, workload balancing view, geocoded road distances, postal-code distance calculator.
- **Scheduling/route work**: "Route and Presence Scheduling — configure routes that consist of routine, scheduled pickups and indicate when and where a driver will be during certain periods… You may offer customers lower rates on routine pickups scheduled in advance."
- **Customer portal**: self-dispatch (schedule pickups, create orders, with validation), real-time tracking (status, assigned driver, recipient, drop-off time, POD incl. signature), order history, personal address book, print shipping labels / waybills / bills of lading, export to Excel.
- **Reference data**: Location Management (every address picked up from or delivered to), Zone & Postal Code Management, vehicle management with maintenance tracking, custom user-defined fields, workflow designer (customize notification content/trigger/channel), international/regional support.
- Pricing/marketing facts (NOT canonical): plans from $49/month unlimited users; "over 3,900 features"; GPS "down to 3 seconds"; order entered and dispatched "within 15 seconds".

### Dispatch Science (Evidence layer A — directly observed)

Positioning: "next-generation Transportation Management System… Run dispatch, routing, tracking, billing, analytics, and integrations out of the box"; "purpose-built for last-mile couriers and delivery businesses" (own footer). Product structure by role: Customer, Driver, Dispatcher, Back Office; platform branded DSX.

Key observations:

- **Dispatcher**: graphical dispatch board (interactive display of orders and drivers); user-definable filters/groupings; "Automate dispatch for touchless order assignment based on business rules"; exception-based management via a Notification Hub; warnings for zone, price, or address errors; alerts for arrival-time delays and customer no-shows; monitor a driver's optimized stop sequence and route; workload balancing by distribution rules; two-way messaging; real-time driver speed and location; dashboard with pre-defined alerts (geo-location of drivers, orders put on hold, orders picked up).
- **Back office**: receives customer orders "in whatever format they transmit; email, Excel, EDI, or other"; intelligent self-service ordering and inquiry forms answering pricing/service-type questions; "Uber-style ordering and tracking"; complex pricing: "multi-price list, zone or distance-based" with variations by vehicle type, account, variable minimums/maximums; built-in geolocation, timestamps, automated wait-time calculations; automated alerts for late/at-risk/problematic orders; configurable notifications for drivers, dispatchers, or customers; view of drivers' workloads and earnings; DIY integrations via documented public API; process RFP requests to determine routes, drivers, and potential delivery costs; import multiple order formats "to become your shippers' trusted delivery provider".
- **Customer** (from homepage): self-serve portal for pre-orders and instant quotes; real-time delivery status with ETA predictions and completion notifications; schedule changes and feedback; "Issue invoices and pay bills via the portal"; self-service tracking to reduce support load.
- **Driver** (from homepage): job notifications and turn-by-turn directions via mobile app; customer-specific requirements (signatures, barcodes, QR scans, photos, installation); update delivery status; communicate with dispatchers, customers, or recipients via SMS, email, or phone.
- **Route optimization**: optimize routes "for thousands of stops… based on service level, vehicle, driver position, availability, and workload"; dispatchers tweak routes through the day.
- Customer roster is dominated by courier companies (courier/messenger/expedited names across the logo wall and case studies: e.g., healthcare expediting, local couriers).

### CXT Software (Evidence layer A — directly observed)

Positioning: "Courier Software: Dispatch, Tracking & Delivery"; "last-mile, route, and on-demand shipment management technology"; suite = Client Portal + Operations App + Driver App.

Key observations:

- **Operations App** ("the central hub for your courier and logistics company"): dispatching, accounting, reporting, business integration; "all the tools you need for ordering, accounting, dispatching, tracking, driver management".
- **Dispatch**: Autonomous Dispatch (AI/ML assigns drivers from real-time data) with an explicit three-mode switch: full automation / assisted (recommendations) / manual control.
- **Route management**: "route-building tool that allows users to see and build out all routes in advance, and schedule and plan distribution services" — supports both on-demand and routed/recurring work (Itinerary Planning spans both).
- **Tracking**: real-time GPS, "up to the second map-based visibility into your orders, routes, and drivers", dispatch-center big-screen display; "in-depth parcel history to meet even the strictest chain of custody needs".
- **Parcel management**: "a parcel-centric ecosystem, following chain of custody through every handoff… know where each item is at all times" — item-level custody, healthcare emphasis.
- **Accounting**: invoicing with fully customizable templates; upload/download revenue data to QuickBooks and Sage or custom integration.
- **Driver settlements**: "set different rates for different drivers or for different types of work and fully customize rate and payment structures."
- **Multi-brand**: "Manage multiple brands or business verticals under one software suite… individual businesses, different assets, financials."
- **Client Portal**: clients place and track orders, view shipment history, manage payments, automated status alerts; white-labeled and embeddable.
- **Integration**: open API, EDI and "proprietary B2B methods", "hundreds of pre-built integrations" to shippers/third parties.
- **Contractor compliance**: GigSafe integration ("live driver compliance now flows directly into CXT's dispatch and routing workflows").
- Industries served: medical & labs, pharmacy, final-mile couriers, pick-up & delivery, distribution, automotive couriers, big & bulky, grocery.

### Elite EXTRA (Evidence layer A — directly observed, homepage-level)

Positioning: "last mile software solutions"; suite of three products: Routing & Dispatch (optimized route planning, real-time driver tracking, customer ETA notifications, business analytics), Delivery Network (on-demand third-party delivery with provider price/time comparisons and central contracting & billing), Returns Automation (automatic returns validation, policy enforcement, digital returns chain of custody, customer portal).

Key observations:

- Routing & Dispatch is the flagship: the dispatch/route engine + driver app + notifications stack is the core; this is the pole closest to generic last-mile dispatch.
- Serves couriers AND distributors (parts/product distribution) — the customer base straddles the courier boundary.
- Adds delivery outsourcing: orders can be handed to third-party providers (DoorDash, Uber, Roadie named) with central contracting/billing — an extension beyond the operator's own workforce.
- Returns automation as a companion product — extends the pickup→delivery machinery into reverse logistics.
- SaaS, month-to-month, no-hardware deployment posture; updates every 8 weeks (marketing facts, not canonical).

---

## Cross-product Comparison

| Structure / capability | OnTime 360 | Dispatch Science | CXT | Elite EXTRA | Assessment |
|---|---|---|---|---|---|
| Courier order/shipment as unit of record (pickup→delivery) | ✔ (orders/shipments/packages) | ✔ (orders) | ✔ (shipments, parcel-centric) | ✔ (stops/deliveries) | All 4 → Core |
| Operator tenant: run by the delivery company for its own customers | ✔ ("your customers", contracted rates) | ✔ ("your shippers' trusted delivery provider") | ✔ ("your courier and logistics company") | ✔ (couriers & distributors) | All 4 → Core (defining context) |
| Dispatch / assignment to operator's couriers (manual + assisted/automated) | ✔ (drag-assign, unassigned queue, self-dispatch) | ✔ (touchless auto-assign by rules; board) | ✔ (autonomous/assisted/manual) | ✔ (routing & dispatch flagship) | All 4 → Core |
| Recorded execution: status events to delivery confirmation / POD | ✔ (tracking view, POD incl. signature/photo) | ✔ (status updates, POD via app) | ✔ (chain of custody, parcel history) | ✔ (driver app, tracking) | All 4 → Core |
| Customer contracted-rate pricing engine (price sets / multi-price lists / zones / distance) | ✔ (price sets + modifiers + dim weight) | ✔ (multi-price lists, zone/distance, vehicle-type/account variations) | ✔ (driver rates; customer invoicing; rates implied) | partial (central contracting & billing in Delivery Network) | 3.5/4 → Core-adjacent; rate-driven billing is strongly common |
| Billing / invoicing of customers | ✔ (billing management, accounting sync) | ✔ (billing; customer pays bills in portal) | ✔ (accounting, invoicing templates) | partial (billing inside Delivery Network module) | Common-strong; kept out of strict definition |
| Driver pay / settlement (wages, time clock, per-driver rates) | ✔ (wage calc from price sets + time clock) | ✔ (view drivers' workloads and earnings) | ✔ (driver settlements) | not observed | 3/4 → Common, not definitional |
| Customer web portal (self-service orders, tracking, history, address book) | ✔ | ✔ (+ invoices/pay bills) | ✔ (+ payments) | ✔ (returns customer portal) | All 4 → standard capability |
| Order intake: phone/desk entry + portal + API/EDI/file import | ✔ (REST/SOAP API, Excel/CSV import) | ✔ (email/Excel/EDI/API, RFP intake) | ✔ (open API, EDI, B2B) | not detailed | All observed → standard capability |
| Route optimization / route building | ✔ (route & presence scheduling; distances) | ✔ (thousands of stops) | ✔ (route building + itinerary planning) | ✔ (flagship) | All 4 → standard capability |
| Driver mobile app (assignments, navigation, scans, signature/photo POD, offline) | ✔ | ✔ | ✔ | ✔ | All 4 → standard capability |
| Real-time driver/order map tracking + ETAs | ✔ (GPS) | ✔ (+ETA predictions) | ✔ (big-screen dispatch) | ✔ | All 4 → standard capability |
| Automated customer notifications (status/ETA) | ✔ (notification workflow designer) | ✔ (configurable, Notification Hub) | ✔ (automated status alerts) | ✔ (ETA notifications) | All 4 → standard capability |
| Exception management (late/at-risk, no-show, zone/price/address warnings) | ✔ (color coding, past-due) | ✔ (exception-based mgmt) | ✔ (on-time rates focus) | not detailed | Common |
| Chain of custody (item-level, regulated segments) | ✔ (digital chain of custody blog; secure) | ✔ (healthcare expediting customers) | ✔ (granular chain of custody, healthcare emphasis) | ✔ (returns chain of custody) | Common, segment-amplified |
| Scheduled / recurring route work alongside on-demand jobs | ✔ (route & presence scheduling) | ✔ (pre-orders) | ✔ (routed + on-demand) | ✔ (recurring orders in migration testimonial) | All 4 → standard capability |
| Third-party delivery outsourcing (other carriers fulfill some orders) | not observed | not observed | not observed | ✔ (Delivery Network) | Product-specific → variant |
| Returns management companion | not observed | not observed | not observed | ✔ (Returns Automation) | Product-specific → variant |
| Multi-brand / multi-business-vertex tenancy | not observed | not observed | ✔ (Multi-Brand) | not observed | Product-specific → variant |
| Vehicle maintenance management | ✔ | not observed | not observed | not observed | Product-specific → optional |
| Accounting integration spine (QuickBooks/Sage/Xero/FreshBooks/BI tools) | ✔ | ✔ (via platform/API) | ✔ (QuickBooks, Sage, Tableau/Power BI/Zoho) | not detailed | Common |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Four structures. Remove any one and the product is no longer recognizable as a Courier Management Platform:

1. **The courier order as the unit of record** — a request to collect items at an origin and deliver them to a destination, belonging to a customer account, carrying service timing. The system of record is the order list; every other structure hangs from it.
2. **Dispatch to the operator's own courier workforce** — orders are assigned to the delivery company's drivers — employees or contracted couriers — individually or batched into routes. The workforce being managed belongs to the operator (or its contractor network), not to a neutral marketplace.
3. **Recorded execution ending in delivery confirmation** — each order advances through attributed, time-stamped status events (received → assigned → picked up → en route → delivered / failed) and is closed by proof of delivery captured in the field. This execution record is what the operator sells and what its customers are shown.
4. **The courier-business frame** — the platform exists to run a delivery service business: external customer accounts hold contracted rates that price each order, and completed delivery work becomes billed revenue. Remove this and the same software becomes a shipper's internal fleet tool — a different Type.

Historical check (per workflow): 1990s–2000s desktop courier systems (order entry + rate card + radio/dispatch board + digital waybill/manifest + POD + invoicing) satisfy all four without cloud, GPS, mobile apps, route optimization, or customer portals. Regional motorcycle/courier firms price per job and bill accounts — they fit. The definition survives.

### L1 — Common Mature Structure (standard capabilities)

- Customer web portal: self-service ordering with validation, quotes, order history, personal address books, live tracking, document printing (labels/waybills), invoice access/payment
- Multi-channel order intake: dispatcher order entry, portal, API (REST-style), file/EDI/email import
- Contracted-rate pricing engine: per-customer price sets, zone/distance/weight/vehicle factors, accessorial modifiers, quotes and quote-on-hold
- Route machinery: route building/optimization, route & presence scheduling, recurring/scheduled route work alongside on-demand jobs
- Driver mobile app: assignment lists, navigation/turn-by-turn, barcode/QR scanning, signature capture, photo POD, COD collection, offline operation with sync
- Real-time visibility: map-based driver/order tracking, ETAs, status color/urgency coding
- Automated notifications: status/ETA alerts to customers and internal parties across channels (email/SMS/push); exception alerts (late/at-risk, no-show, data-quality warnings)
- Billing: invoice generation cycles, invoice templates, payment posting; accounting-system integrations
- Driver pay machinery: time clocks, wage/settlement calculation per driver and work type
- Reference data: customer/location address books, zones & postal-code mapping, geocoding/distance services
- Reporting/analytics dashboards; API/integration spine (EDI, B2B, shipper systems)
- Chain-of-custody-grade parcel/item tracking (amplified in regulated segments)

### L2 — Variant / Optional Structure

- Work-mix emphasis: on-demand expedited vs scheduled/routed vs mixed
- Industry tuning: healthcare/lab/pharmacy (chain of custody, STAT runs), retail/e-commerce, automotive parts, big & bulky, grocery, distribution
- Third-party delivery outsourcing: handing orders to external delivery providers with central contracting/billing (one sampled product)
- Returns/reverse-logistics companion modules (one sampled product)
- Deployment heritage: cloud SaaS vs desktop/smart-client lineage; on-prem vs hosted
- Tenant scale/shape: single-operator SMB vs multi-brand/multi-vertical enterprises
- Vehicle/fleet asset management (maintenance) inside the platform
- Driver-compliance/contractor-onboarding integrations (one sampled product)

### L3 — Vendor-specific (kept out of the final document)

- OnTime 360: Workflow Designer, Smart Client offline technology, WAP device editions, Google Plus Codes / what3words addressing, ~300 supported regions, price-from-$49 marketing, "3,900 features" count
- Dispatch Science: DSX platform branding, DataBridge / DataSync / DataHive data layer names, Notification Hub as branded module
- CXT: Autonomous Dispatch three-mode branding, "Driver 3 / NextStop" app names, GigSafe integration, Multi-Brand module, SOC 2 posture, Ionic Partners/e-Courier consolidation
- Elite EXTRA: RTx / RAx product names, Epicor ownership, DoorDash/Uber/Roadie named partners, 8-week release cycle, 325,000-user count

## Vendor-specific Findings

See L3 above. Notable single-product findings that must NOT generalize:

- Third-party delivery-network outsourcing (Elite EXTRA only in sample)
- Returns automation suite (Elite EXTRA only)
- Multi-brand tenancy (CXT only)
- Vehicle maintenance tracking (OnTime only)
- In-app customer payment of invoices (Dispatch Science, CXT portals — 2/4, treated as common-leaning but portal depth varies)

## Rejected Findings (considered and rejected as core)

- **Route optimization as definitional**: present in all samples, but historic courier operations ran on manifests and dispatcher knowledge; optimization is a modern common capability, not the defining structure.
- **GPS/real-time tracking as definitional**: fails the historical check (dispatch boards + phone check-ins predate GPS).
- **Driver settlement/pay as definitional**: strong (3/4) but not universal in the sample; payroll can sit outside.
- **Consumer-style "Uber tracking"**: a customer-portal pattern, not the Type's core.
- **"TMS" self-labeling (Dispatch Science)**: vendor positioning; do not adopt TMS semantics (loads, carriers, freight audit) into this Type.
- **Courier = parcel networks (UPS-style)**: sampled products are business couriers/expeditors; national parcel-carrier internal systems are out of scope for this market category (those carriers buy/build such platforms, but the commercial category is the regional/B2B courier software market).

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| Last-mile Delivery Platform | closest neighbor, shared execution substrate | Last-mile platforms serve shippers/retailers orchestrating delivery of *their own* goods with customer-experience focus. Remove the courier-business frame (external customer accounts, contracted rates, billing, driver pay) from a Courier Management Platform and it becomes a last-mile delivery platform. Elite EXTRA demonstrates the drift: it brands itself "last mile software" while still serving courier operators. |
| On-demand Delivery Platform | adjacent | Consumer-facing instant delivery marketplace with its own demand generation; courier management is B2B back-office for a delivery operator fulfilling its customers' work. |
| Dispatch Management (generic) | capability overlap | Generic dispatch spans any field workforce (services, trades). Courier management adds courier order semantics: pickup→delivery, items, POD closure, rating/billing. |
| Proof of Delivery Platform | capability slice | POD here is one closure step of the order lifecycle, not the whole product. |
| Shipment Visibility Platform | different side | Visibility platforms aggregate/track shipments across carriers for shippers; courier management *executes* the work on the operator side. |
| Parcel Management Platform | different side (suspected) | Shipper-side multi-carrier parcel shipping management (rate shopping, labels across carriers) — the shipper buys delivery; the courier operator sells it. Not directly researched this pass; boundary recorded with moderate confidence. |
| Trucking Management System | same industry, different unit of work | Trucking moves loads (FTL/LTL, trips, HOS, carrier settlements); courier moves individual pickup→delivery jobs priced per order in local/regional networks. |
| Freight Brokerage Platform | different business model | Brokerage matches shippers to third-party carriers; courier management runs the operator's own fulfillment workforce. |
| Route Optimization Platform | capability slice | Optimization is a standard capability here, not a standalone Type boundary. |
| Delivery Scheduling Platform | capability slice | Scheduling of deliveries/routes is embedded; the standalone Type is narrower. |

## Uncertainties

1. **Exact status-state vocabularies**: only fragments observed ("orders put on hold", "orders picked up", "en route"); exact state lists are product-specific — final document uses conceptual states.
2. **Driver settlement universality**: 3/4 products show it; Elite EXTRA unverified. Kept as common, not core.
3. **Parcel Management Platform's exact market meaning** (the neighboring leaf): not directly researched this pass; boundary stated conservatively.
4. **Geographic breadth**: sample is North America-heavy; OnTime claims international support, but regional products (e.g., European/Korean/Indian courier software) were not sampled. Assertions kept implementation-level, not region-specific.
5. **Elite EXTRA depth**: only homepage/suite-level documentation fetched; feature-page detail (driver app POD specifics, rate machinery) not directly verified.
6. **Help-center-level documentation** was not fetched for any product; numeric limits, timeouts, and defaults are deliberately absent.

## Final Synthesis

A Courier Management Platform is the operations system of record for a courier/delivery company. Its defining core is four structures: (1) the courier order — a pickup→delivery job for a customer account with service timing — as the unit of record; (2) dispatch of those orders to the operator's own or contracted courier workforce; (3) recorded execution through attributed status events closing in field-captured proof of delivery; (4) the courier-business frame that prices each order against contracted customer rates and turns completed work into billed delivery revenue. Everything else — portals, route optimization, driver apps, tracking maps, notifications, billing machinery, settlements, chain of custody — is the mature capability stack that makes the core operational at scale, with industry tuning (healthcare, pharmacy, retail, distribution) and work-mix (on-demand vs routed) as the main variant axes. The Type's identity is anchored in the operator tenant: when the business frame is removed, the same execution machinery becomes a Last-mile Delivery Platform — the closest and most important boundary in the directory's crowded §18 delivery cluster.
