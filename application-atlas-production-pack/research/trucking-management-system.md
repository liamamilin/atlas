# Research Notes — Trucking Management System

Research date: 2026-09-10
Slug: trucking-management-system
Directory leaf: §18 Transportation, Mobility & Logistics → "Trucking Management System"

## Research Goal

Understand the software an asset-based motor carrier runs its business on (directory leaf §18 "Trucking Management System", slug `trucking-management-system`): what the system's world consists of, how a load moves from tender/booking through dispatch, haul, delivery, billing, and driver settlement, what makes the carrier seat structurally different from the shipper (TMS) and broker (freight brokerage) seats on the same freight substrate, and where the boundaries sit against the dense §18 sibling cluster.

## Prior-pass obligations (seams this pass must discharge)

Four processed siblings left flags pointing at this leaf:

1. **Transportation Management System / TMS (§10, processed 2026-09-08)** — seam #1: "trucking-management-system = carrier-side seat of the same freight substrate (whose money and whose fleet); Turvo sells one collaborative TMS to shippers/3PLs/brokers/carriers, so seat is variant not product boundary — that pass should ratify from its side." Also: "The trucking-management-system pass must ratify the seat seam from its side" (Uncertainties).
2. **Freight Brokerage Platform (§18, processed 2026-09-08)** — flag #1: "same freight substrate, opposite supply identity (whose trucks/whose authority; owner-operator carriers the gray zone; the hybrid asset-based-brokerage pole runs both sides in one product — expected keep-both with supply-identity seam)." Structural test recorded there: "strip the resale/margin machinery → shipper TMS or carrier settlement system; strip third-party capacity → trucking territory."
3. **Load Board / Freight Marketplace (§18, processed 2026-09-09)** — flag #1: "carrier's own ops system vs the market where the carrier finds loads (a carrier uses both; the board holds no dispatch/fuel/maintenance/driver-settlement machinery)."
4. **Dispatch Management (§18, processed 2026-09-07)** — boundary table: "Add the freight business system — order-to-cash, carrier settlement, EDI tendering, compliance — → TMS/TMS-for-carriers. Dispatch is the operational core inside such suites (Truckbase self-labels 'dispatch-centric TMS')." That pass sampled Truckbase as a carrier-side trucking TMS whose center is dispatch/settlement for the carrier.

Also relevant processed siblings: Freight Forwarding System (naming note: forwarder products also marketed as "TMS" — the shared word spans seats), Fleet Management System (freight/loads/settlements explicitly outside its core), Driver Management (freight/loads/assignment/settlements explicitly outside its core), ELD/HOS (duty-status compliance, not freight execution), Courier Management (own-workforce delivery operator), Shipment Visibility Platform (watch layer), Transportation Exception Management (exception desk).

## Initial Boundary (pre-research hypothesis)

- A Trucking Management System (market vocabulary: "trucking TMS", "carrier TMS", "trucking software") is the **carrier-side** business system of record: a trucking company runs loads with **its own trucks and drivers** under its own operating identity, bills the customers (shippers/brokers), and pays its drivers (settlement).
- Its center is the **load** as the unit of revenue record, dispatched against **own capacity** (tractors/trailers + drivers), closed through **billing + driver settlement** on the carrier's own books.
- Nearest confusions: TMS (shipper seat — buys carriage), Freight Brokerage (principal reselling third-party capacity), Dispatch Management (assignment machinery without the business frame), FMS (vehicle estate), Driver Management (person records), ELD (duty-status compliance), Load Board (market venue), Courier Management (delivery-work semantics).

## Research Questions

1. What is the central object of record — load, order, trip? How does demand arrive (rate confirmation, EDI tender, load board, direct customer)?
2. How is the carrier's own capacity modeled — trucks/tractors/trailers, drivers, fleets? What availability state is maintained?
3. What does the dispatch loop look like (assignment, transmission to driver, status return)?
4. How is the money frame structured: customer billing (rates, accessorials, invoicing) AND driver settlement (pay arrangements, deductions, bonuses)? Are both held on the load?
5. What cost machinery ties trucks to the business (fuel, IFTA/fuel tax, maintenance)?
6. What compliance machinery exists (driver credentials, HOS, equipment)?
7. How does tracking work (ELD/telematics/driver app) and what flows to customers (portals, EDI status, tracking links)?
8. What roles staff the system (dispatcher, bookkeeper, owner/ops manager, driver)?
9. How do seat variants work: pure carrier vs hybrid (asset-based broker) vs private fleet vs multi-seat suites?
10. Historical check: does the paper-era trucking office satisfy the same core?
11. Boundary tests vs the ten neighbors above.

## Representative Products

Selected for market representativeness, different customer tiers, different product philosophies, and reachability. Three products fetched first-hand this pass; two further products carry corroborating first-hand evidence from prior sibling passes (recorded as such).

| Product | Segment / posture | Philosophy | Evidence |
|---|---|---|---|
| Truckbase | SMB–mid asset-based carriers ("turnkey at 5 trucks... powerful enough for 50") | dispatch-centric modern simplicity; text-first, app-optional; zero-data-entry automation | Tier-2 homepage + driver-settlement product page (this pass); dispatch pass sampled the same product's dispatch page |
| Trimble TMW.Suite / Trimble TMS for Carriers | enterprise truckload carriers (+ brokers, 3PLs, private fleets); "60% of the top 200 US-based carriers" (vendor claim) | enterprise order-to-cash suite; dispatch + telematics + billing unified; sibling products for maintenance/fuel-tax | Tier-2 solution/category/product pages (this pass) |
| Alvys | mid-market all-in-one; carriers + brokers + hybrid (asset-based broker) + enterprise + private fleets; load-based pricing | all-in-one operating system; hybrid toggle; native EDI; AI automation | Tier-2 homepage + carrier page + Tier-1 help-center index (this pass); brokerage pass documented the same help center's broker side |

Corroborating prior-pass evidence (context, not new fetches): dispatch pass's Truckbase observations (dispatch page, check-call era baseline); brokerage pass's Alvys help-center structure (Loads & Trips / Accounting & Settlements / Assets & Fleet / Safety & Compliance) and Tai TMS's explicit "NOT designed for asset-based brokers or carriers" seat exclusion; TMS pass's Turvo multi-seat marketing.

Rejected/abandoned samples (per source-abandonment rule): McLeod LoadMaster (403 ×2 across passes — the traditional enterprise carrier-suite pole unverified), Rose Rocket (403 ×3 across passes — modern multi-mode carrier SaaS pole unverified), Tailwind TMS (timeout ×2), TruckLogics (403 ×2), Axon (403), ITS Dispatch (transport error ×2), Dr Dispatch (403). The owner-operator/small-carrier thin pole and the legacy enterprise pole are therefore structurally inferred from the sampled range + ecosystem; no claim in this research depends on them.

## Sources

All fetched 2026-09-10 unless noted. Evidence is official vendor surfaces: product/solution pages, FAQ, and one help-center index.

- Truckbase homepage — https://truckbase.com/
- Truckbase Driver Settlement Software page — https://truckbase.com/driver-settlement-software
- Trimble Transportation homepage — https://transportation.trimble.com/
- Trimble Transportation Management category page — https://transportation.trimble.com/en/solutions/transportation-management
- Trimble TMW.Suite product page — https://transportation.trimble.com/en/solutions/transportation-management/tmw-suite-tms
- Alvys homepage — https://www.alvys.com/
- Alvys Carrier TMS page — https://alvys.com/tms-for-carriers
- Alvys Help Center index — https://help.alvys.com/en/
- Prior sibling research (context): research/transportation-management-system-tms.md, research/freight-brokerage-platform.md, research/dispatch-management.md, research/load-board-freight-marketplace.md, research/freight-forwarding-system.md, STATUS.md seam notes.

### Source-access Limitations

- No sampled vendor's deep help-center articles were drilled this pass beyond the Alvys index (Tier-1 structure only). Truckbase and Trimble evidence is product/marketing-page depth.
- McLeod, Rose Rocket, Tailwind, TruckLogics, Axon, ITS Dispatch, Dr Dispatch unreachable (see Representative Products). Consequence: exact status vocabularies, settlement-cycle defaults, pay-period conventions, numeric limits, and permission models are NOT asserted anywhere; claims are calibrated to the fetched pages.

## Product Observations

### Truckbase — SMB/mid dispatch-centric pole [Layer A]

From the homepage and driver-settlement page:

- Self-labeling: "Trucking TMS software for growing carriers"; "a carrier TMS that's easy to use"; footer: "Eliminate data entry and grow with a TMS built for growing asset-based carriers."
- Module structure (vendor's own nav): Trucking Dispatch Software / ELD + Truck Tracking / Trucking Invoicing Software / Customer Portal / **Driver Settlement Software** / Truckbase Intelligence (reporting).
- Use cases: Heavy Haul & Specialized, Long Haul, Regional, LTL and Partial Loads, Cross-Border (coming soon), Intermodal.
- Unit of work: the **load** — "organize load, documents, and invoices"; "Track all load information within a single calendar"; "load history".
- Intake: "Automate load creation with just a few clicks and our AI-powered load importer" (rate confirmations from PDF).
- Dispatch: "Send your drivers dispatch details via text or email all with a single click"; text-based dispatch, driver app optional ("Drivers all have their own logins to our mobile-friendly app... driver logins are an easy way for drivers to see their load history and schedule"); "status updates between driver & dispatcher"; "complete visibility over your drivers' schedules."
- Tracking: 30+ ELD integrations; "real-time load and truck visibility"; "eliminate check calls"; "Increase your carrier score with major brokerages by achieving 100% live tracking coverage"; HOS-aware alerting ("if they need to rest to remain compliant, they can be alerted automatically").
- Invoicing (revenue side): "Automate your back office with instant invoicing"; "Track all unpaid & overdue invoices on a single platform"; "Filter and search for documents by date, broker, and more"; factoring one-click emails (direct integration "coming soon").
- Driver settlement (pay side): "Build settlements according to load and driver without entering any data. Truckbase pulls data from dispatch and fills out the information for you"; "Save recurring bonuses and deductions, and make one-off adjustments"; "Generate settlements in one click, whether in bulk quickly or individually"; "Manage all of your saved settlements and track any revisions with complete visibility over all payments"; "Generate driver pay sheets that your drivers can understand and rely on"; "drivers easily view their base pay, deductions, bonuses, and other pay with clear itemization"; "wins the trust of company drivers and owner-operators."
- Roles named: Fleet owners, Dispatchers, Operations Managers, Bookkeepers; on the settlement page: Bookkeeper / Owner / Driver.
- Documents: mobile BOL scanning; rate confirmations; invoices ("manually re-enter data from rate confirmations, BOLs, and invoices" named as the pain being solved).
- EDI: "syncs your TMS with your customer's system... load acceptance, tracking, and invoicing"; "Email your broker updates & BOLs instantly."
- Cost machinery: fuel cards integration "COMING SOON — realtime visibility into costs by driver and unit"; QuickBooks sync; routing/mileage (PC*Miler/Google Maps) "COMING SOON" — no native optimization shipped.
- Scale/segment: "turnkey at 5 trucks and powerful enough for 50 trucks"; cloud-based; per-testimonial comparison against "a system like McLeod" (enterprise alternative named by a customer).

### Trimble TMW.Suite / TMS for Carriers — enterprise order-to-cash pole [Layer A]

From the Trimble Transportation homepage, Transportation Management category page, and TMW.Suite product page:

- The vendor **splits its own TMS line by seat**: "Trimble TMS — Carriers (/carrier-tms)" vs "Trimble TMS — Shippers (/shipper-tms)". Direct first-hand evidence that the market treats carrier-side and shipper-side TMS as distinct products.
- Category framing: "Comprehensive platforms for carriers and shippers"; "From sourcing and dispatching to payment reconciliation, our solutions provide the comprehensive logistic controls required to drive your business forward."
- **TMW.Suite**: "Enterprise TMS Software for Trucking Companies"; "enterprise level TMS purpose built for truckload carriers, brokers, 3PLs and private fleets"; three named seats: truckload carriers ("improve efficiency, utilization and operating ratios"), brokers/3PLs ("efficiently enter orders, cover loads and manage margin"), private fleets ("apply many of the same best practices used by leading commercial carriers").
- Order-to-cash framing: "Driving business excellence from order-to-cash"; "The enterprise standard for order-to-cash. Optimize every load and protect your margins by unifying your dispatch, telematics, and billing into one seamless management platform."
- Dispatch mechanics: "By quickly capturing load details, calculating miles, and analyzing pricing, TMW.Suite ensures correct, on-time dispatch... reducing empty miles and minimizing dispatch errors."
- **Trimble TMS for Carriers** (the modern SaaS carrier pole): "AI-powered TMS built for full truckload carriers looking to grow. Trimble TMS for Carriers automates your order-to-cash lifecycle"; "AI-powered dispatch and order management — Automate order entry, optimize driver assignments and grade incoming tenders based on financial viability"; "Pre-built integrations across accounting, payroll, ELD, EDI and shipment visibility"; "Proactive compliance and real-time visibility — Stay ahead of driver and equipment compliance deadlines, keep customers informed with automatic ETA updates and get a 360-degree view of your network."
- **TruckMate** (LTL sibling): "a comprehensive and trusted dispatch, operations and accounting system that streamlines your LTL operations from order entry to settlement"; terminal-centric LTL, intermodal ("manages the containers, drivers, power units, carriers and chassis"), complex carriers.
- **Fuel Dispatch** (segment sibling): fuel carriers; "Streamline the 'order-to-cash' cycle by automating load building and using real-time dashboards to track driver ETAs, asset assignments and shift planning"; tank-inventory forecasting.
- Modules/add-ons around the TMS: Reveal (BI), Smart Workflow (driver task-based workflows), Freight Sourcing & Settlement (procurement/tendering — the buy side for capacity shortfalls), Freight Visibility (ETA/exception monitoring), Fleet Hub (TMS↔in-cab tech integration hub); related products: CoPilot (navigation), Vusion ("full-service fuel tax solutions"), TMT Fleet Maintenance.
- AI era: Trimble Arc Agent — "high-volume operational workflows, from PDF order entry and contract intake to first-line customer support."
- Scale claim: "60% of the top 200 US-based carriers trust a Trimble TMS"; "1,000,000 trucks connected globally" (vendor claims, excluded from final-document assertions).

### Alvys — mid-market all-in-one / hybrid pole [Layer A]

From the homepage, carrier page, and help-center index:

- Self-labeling: "Transportation Management Software | Trucking TMS Software"; "#1 modern Trucking tms software"; carrier page: "#1 modern CARRIER TMS SOFTWARE — All-in-One TMS Software for Carriers."
- Seats (vendor's own nav): Carriers / Brokers / **Hybrid ("Asset-based freight broker")** / Enterprise / Private fleets. Demo form business types: Carrier, Shipper, Broker, Hybrid, Freight Forwarder, Partner.
- Carrier-page definition of the category (vendor's own FAQ): "Carrier TMS software is a specialized tool for trucking companies that centralizes fleet operations"; "Carrier TMS software manages various aspects of fleet operations... dispatch management, load planning, driver communication via a mobile app, and integrations with ELD systems, accounting software, and load boards."
- Quote-to-cash framing: "Our carrier TMS software gives you the smartest paths from quote to cash, covering dispatching, load and driver management, billing, and compliance."
- Feature blocks: Dispatching ("Load management, documentation, marketplace, and real-time visibility"); Driver app ("Document scanning and upload, in-field communication, and asset tracking"); Compliance & safety ("Driver, truck, trailer, carrier, safety, and maintenance management"); **Accounting & payments ("Invoicing, billing, IFTA reporting, and driver/agent/carrier settlement")**; Reporting & analytics; Native EDI; Marketplace ("Search, book, and dispatch"); IFTA (own feature page); Tracking & Tracing.
- Carrier driver management: "onboard drivers, stay compliant with FMCSA regulations, manage driver schedules, monitor hours of service, and features completely customizable pay arrangements."
- Native EDI: "Easily accept loads and send automatic load updates with native EDI... Get loads created automatically from the rate confirmation."
- Driver app: "fast eCheck capabilities for lumpers, document scanning and uploading, status updates, and instant communication with dispatchers."
- Load-lifecycle behaviors (homepage problem/solution list): notes attached to the load visible in real time; automatic load creation; alerts when loads fall behind; "With each action by the driver, the load status is updated automatically"; "Accessorials are automatically deducted so the right amount is invoiced"; "POD reconciliation... driver app automatically attaches all needed documents and receipts for fast invoicing."
- Hybrid posture: "Uniting your carrier and brokerage sides... Quickly toggle between your fleet and brokerage, and streamline your load management and accounting processes." Carrier AND driver AND carrier-settlement in one accounting block ("driver/agent/carrier settlement").
- Private-fleet seat: "The ultimate TMS for shippers with private fleets... cut costs, reduce empty miles, and keep your fleet running at peak performance."
- Help-center index (Tier-1, the operation's object vocabulary): "Create a Load — Enter the **customer, stops, and rates** for a new shipment"; "Loads & Trips — Create, dispatch, modify, and track loads and trips end to end"; "Accounting & Settlements — Invoicing, **driver and carrier settlements**, deductions, and e-checks"; "Assets & Fleet — Add and manage drivers, trucks, trailers, and fleets"; "Safety & Compliance — Verify motor carriers and keep your operation compliant"; "Run your operation — Day-to-day work, **from tender to settlement**." Integrations: ELD & Telematics (HOS, location, asset tracking), Accounting (QuickBooks/Sage Intacct/Business Central), Load Boards ("Post and source freight on DAT, Truckstop, and other boards"), EDI & Visibility ("Trade tenders and status updates with your customers"), Fuel & Tolls ("Import fuel and toll transactions for settlements and IFTA"), Factoring & Payments. Administration: "Roles, permissions, offices."
- Scale evidence: testimonials from 5-truck to 100-truck carriers; cross-border operations; "TRUSTED BY 3000+ MCs" (vendor claim).

## Cross-product Comparison

| Dimension | Truckbase | Trimble TMW.Suite / TMS for Carriers | Alvys |
|---|---|---|---|
| Self-label | "Trucking TMS... for growing carriers"; "asset-based carriers" | "Enterprise TMS Software for Trucking Companies"; "TMS for Carriers" | "Trucking TMS"; "Carrier TMS Software" |
| Unit of record | load ("load, documents, and invoices"; single calendar) | "capturing load details... Optimize every load"; order-to-cash | load ("customer, stops, and rates"); "Loads & Trips... end to end" |
| Own capacity | drivers (logins/schedules) + ELD-connected trucks | dispatch + telematics unified; driver assignments; equipment compliance | "Assets & Fleet — drivers, trucks, trailers, and fleets" |
| Money frame — revenue | instant invoicing; unpaid/overdue tracking; factoring emails | "order-to-cash"; billing unified with dispatch; margins protected | "quote to cash"; invoicing, billing; accessorials auto-deducted |
| Money frame — pay | driver settlements from dispatch data; base pay/deductions/bonuses/stop pay; company drivers + owner-operators | payroll integration named; TruckMate "order entry to settlement" | "driver/agent/carrier settlement"; "customizable pay arrangements"; e-checks |
| Intake | AI PDF rate-con importer; EDI load acceptance | AI order entry (Arc Agent PDF); tender grading | EDI rate-con auto load creation; AI document handling |
| Dispatch | text/email dispatch; single calendar; driver↔dispatcher status | "optimize driver assignments"; on-time dispatch | dispatch board; driver actions auto-update load status |
| Tracking | 30+ ELDs; eliminate check calls; broker scorecard coverage | telematics unified; automatic ETA updates; 360° network view | ELD HOS/location; tracking links to customers |
| Documents | mobile BOL scan; rate cons; invoices | order module; document machinery in suite | driver-app scanning; POD reconciliation |
| Compliance | HOS-aware alerts | "driver and equipment compliance deadlines" | FMCSA compliance; HOS monitoring; motor-carrier verification |
| Cost machinery | fuel cards (roadmap); QuickBooks | Vusion fuel tax; TMT Fleet Maintenance (siblings) | IFTA reporting; fuel & toll imports feeding settlements + IFTA |
| Customer side | customer portal; EDI status; broker emails | automatic ETA updates | tracking links; EDI status updates |
| Seats | asset-based carriers (5–50 trucks) | truckload carriers + brokers + 3PLs + private fleets | carriers + brokers + hybrid + enterprise + private fleets |
| Modes/segments | long haul, regional, heavy haul, LTL & partial, intermodal | truckload; LTL (TruckMate); fuel (Fuel Dispatch); intermodal | truckload-centric; cross-border testimonials |
| Optimization | none native (routing "coming soon") | mileage calculation in dispatch; PC*Miler-class ecosystem | not headlined; marketplace + planning |

### Layer-B findings (cross-product commonality, 3/3 first-hand + prior-pass corroboration)

1. **The load is the unit of record** with a tender/booking → dispatch → haul → deliver → bill lifecycle ("from tender to settlement" — Alvys help center; "order-to-cash" — Trimble ×3; "load, documents, and invoices" — Truckbase).
2. **Own capacity is the supply side**: drivers and trucks/trailers held as records ("Assets & Fleet"), schedules/availability visible, consumed by load assignment.
3. **Two money directions on the carrier's own books**: customer billing (rates, accessorials, invoicing, factoring) AND driver/owner-operator settlement (pay arrangements, deductions, bonuses) — both anchored on loads. All three products ship settlement machinery as a first-class module.
4. **Dispatch is the operational core**: assignment of loads to truck+driver, transmission to the field (text/email/app), status return.
5. **Event-driven tracking from the truck** (ELD/telematics/driver app) replaces check calls; live visibility is shared outward (customer portals, tracking links, EDI status updates, broker scorecard coverage).
6. **The document trio** (rate confirmation, BOL, POD) flows through the system; document capture is field-side (driver app scanning).
7. **EDI with customers** (tenders in, status out, invoices out) is the standard connectivity spine.
8. **Compliance machinery** (driver onboarding/credentials, HOS monitoring, equipment deadlines) is standard.
9. **Cost machinery ties trucks to the business**: fuel cards, IFTA/fuel-tax reporting, maintenance (module or sibling product).
10. **Role model**: dispatcher (operational core), bookkeeper/accounting (money), owner/operations manager (oversight), driver (field side).
11. **Integration spine**: ELD, accounting, load boards, factoring, fuel cards/tolls.
12. **Seat breadth is a product posture, not the Type's center**: pure carrier (Truckbase), carrier+broker+hybrid+private-fleet (Alvys, TMW.Suite). The hybrid pole toggles fleet and brokerage sides in one product.

## Canonical Abstraction

### L0 — Defining Invariant (minimal, jointly-held)

The Trucking Management System is the **motor carrier's own business system of record** — the system a trucking company runs its freight business on. Three jointly-held structures:

1. **The load as the unit of business record** — a freight movement the carrier commits to haul for a customer, held as a persistent identified record that accumulates the operation from booking/tender through dispatch, haul, and delivery to billing. (Remove → a dispatch board or work queue with no business record; a generic job tracker.)

2. **The carrier's own trucking capacity as the dispatchable supply** — the carrier's own trucks (tractors, trailers, equipment) and drivers held as records whose availability is consumed by load assignment and restored by completion; the loads are hauled by the carrier's own capacity under its own operating identity, not procured from third-party carriers. (Remove → freight-brokerage territory — procured supply; or a bare resource roster.)

3. **The load's money on the carrier's own books** — each load carries its revenue (the customer rate that becomes an invoice) and its pay side (the driver settlement computed from the load), with the carrier's operating-cost machinery (fuel, fuel-tax/IFTA-class reporting, maintenance) tied to the trucks that earn it; the carrier holds both directions of its own money rather than a resale margin between two parties. (Remove → dispatch management — assignment machinery with no business frame; or bare accounting.)

Jointly-held is load-bearing: 1 alone = a load log; 2 alone = a fleet roster; 3 alone = accounting software; 1+2 without 3 = dispatch management (the dispatch pass's own seam); 1+3 without 2 = billing for freight the carrier does not haul (broker/administrative shape); 2+3 without 1 = fleet cost accounting with no load business.

Deliberately NOT in L0: EDI, ELD/telematics, GPS tracking, driver mobile apps, AI automation, load-board integration, customer portals, IFTA specifically (held as the fuel-tax class of machinery), maintenance depth, optimization engines, cloud delivery, any specific regulator or pay-period convention.

### L1 — Common Mature Structure

Present across the sampled products (Layer B):

- dispatch board / load-planning surface as the dispatcher's working screen (calendar, board, or list of loads × trucks × drivers)
- event-driven tracking from the truck (ELD/telematics integration or native; driver app status updates) replacing check calls; HOS-aware alerting
- document machinery: rate confirmation intake, BOL capture (mobile scanning), POD collection and reconciliation
- EDI connectivity with customers: tenders in (often auto-creating loads from rate confirmations), status updates out, invoices out
- compliance machinery: driver onboarding/credential records, HOS monitoring, equipment compliance deadlines
- cost machinery: fuel-card imports, IFTA/fuel-tax reporting, maintenance management (module or sibling product)
- customer-facing surfaces: portals, tracking links, automated status/ETA updates
- analytics: revenue/margin per load, lane, driver, truck; utilization; carrier scorecard posture toward brokers
- integration spine: accounting (QuickBooks-class), factoring, load boards (DAT/Truckstop-class), fuel cards
- role model: dispatcher, bookkeeper/accounting, owner/operations manager, driver (field side)

### L2 — Variant / Optional Structure

- **Seat breadth**: pure carrier tool vs all-in-one sold across carrier/broker/hybrid/enterprise/private-fleet seats (Alvys, TMW.Suite) — the same product family spanning seats confirms the seam runs through products, not vendors.
- **Hybrid posture**: asset-based brokerage toggling fleet and brokerage sides in one platform (Alvys "Hybrid"); carriers brokering out excess loads are the same posture from the carrier side.
- **Private-fleet seat**: the same machinery applied to a shipper's own fleet (Alvys private-fleets page; TMW.Suite private fleets) — internal demand, cost-per-load focus instead of external billing.
- **Scale**: single-truck owner-operators to top-200 carriers; product positioning spans "turnkey at 5 trucks" (Truckbase) to enterprise suites (Trimble).
- **Segment/mode**: truckload, LTL (terminal-centric sibling products), heavy haul/specialized, fuel delivery (tank forecasting), intermodal, cross-border.
- **Automation depth**: text-based dispatch without an app (Truckbase) vs driver-app-centric (Alvys) vs AI agents (order entry, tender grading, document handling — era-current).
- **Optimization depth**: none native (Truckbase) to mileage/routing integrations to optimization-led planning — capability, not identity.
- **Regional/regulatory regime**: US FMCSA/IFTA vocabulary dominates the sample; other jurisdictions run equivalent regimes (tacho-graph-class duty records, national fuel-tax schemes) — the L0 is written regime-neutral.

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Truckbase: AI-powered PDF rate-con load importer; text-based dispatch without required app; 30+ ELD integrations; one-click broker update emails; factoring/routing/fuel-card integrations on roadmap; 5–50-truck positioning; QuickBooks sync; customer testimonial naming McLeod as the enterprise alternative.
- Trimble: product-line split (TMW.Suite / TruckMate / Fuel Dispatch / TMS for Carriers / TMS for Shippers); Reveal BI; Smart Workflow; Freight Visibility; Fleet Hub; Vusion fuel tax; TMT Fleet Maintenance; Arc Agent (PDF order entry, contract intake); "60% of top 200 carriers" and "1M trucks connected" claims; Azure hosting.
- Alvys: hybrid toggle; load-based pricing; native EDI engine (rate-con → load creation); e-checks incl. lumper eChecks; IFTA feature; marketplace feature; AI agents; 120+ integrations; unlimited users/divisions; "3000+ MCs" claim.

## Rejected Findings

- **"Trucking TMS = dispatch software"** — REJECTED as a complete definition. Dispatch is the operational core, but the Type is the carrier's business system: the money frame (billing + settlement), compliance, and EDI spine are what make it a management system rather than a dispatch board. The dispatch pass itself holds this seam ("add the freight business system → TMS-for-carriers").
- **"Trucking TMS = fleet management"** — REJECTED. The FMS centers on the vehicle estate (maintenance, fuel, telematics, compliance of assets); the trucking TMS centers on the load business, with trucks as revenue-producing capacity. Maintenance appears inside trucking TMS as a module or sibling product (Trimble TMT; Alvys maintenance inside compliance) — capability, not center. Consistent with the FMS pass holding freight/loads/settlements outside its core.
- **"A trucking TMS is just a TMS with a different logo"** — REJECTED. The seat seam is structural: the shipper TMS procures carriage from carriers at rates (carriers are the supply side); the trucking TMS sells carriage hauled by its own capacity (customers are the demand side). Trimble itself ships separate "TMS for Carriers" and "TMS for Shippers" products — first-hand vendor evidence for the split.
- **"Driver settlement is just payroll"** — REJECTED. Settlement is computed from the load record (per load/mile/percentage arrangements), pulled from dispatch data, with load-anchored deductions, bonuses, stop pay, and reimbursements — it is load-anchored money, not generic payroll. (The payroll-integration spine exists — Trimble names payroll integrations — but the settlement computation is the TMS's own.)
- **"Load boards are part of this Type"** — REJECTED. Posting/searching DAT/Truckstop-class boards is standard integration; the boards are the external market venue (own leaf). Consistent with the load-board pass.
- **"EDI is definitional"** — REJECTED. L1 integration spine; the paper-era carrier ran on phone, paper rate confirmations, and mailed invoices.
- **"AI order entry / tender grading is definitional"** — REJECTED. Era-current capability layer (present in all three sampled products' marketing; absent from the defining core).
- **"Own trucks only — carriers never subcontract"** — REJECTED as a definitional boundary. Carriers commonly broker out loads they cannot cover; the hybrid pole runs both supply identities in one product. The defining posture is own capacity as the center; subcontracting is a variant capability that imports the brokerage machinery per load.

## Boundary Findings

1. **vs Transportation Management System / TMS (§10, processed) — RATIFIED from this side.** The TMS pass recorded the seat seam ("whose money and whose fleet") and asked this pass to ratify it. Ratified with first-hand evidence: the shipper TMS is the buyer side — it holds shipments it needs moved, procures carriers at rates, and runs the tender-execute-track loop with carriers as the supply side; the trucking TMS is the seller side — it holds loads it has committed to haul, dispatches its own trucks and drivers, and bills the customers (shippers and brokers). Same substrate (loads, customers, rates, documents, tracking, settlement), opposite supply identity and opposite money direction. Trimble's own product split (TMS for Carriers vs TMS for Shippers) is direct vendor evidence; Turvo's one-platform-many-seats posture (prior TMS pass) shows the seam runs through product families as a seat variant, not a vendor boundary. Structural test: strip own-capacity dispatch and driver settlement, add carrier procurement and routing guides → shipper TMS; strip procurement, keep own capacity → trucking.
2. **vs Freight Brokerage Platform (§18, processed) — RATIFIED (supply-identity seam, keep-both).** The brokerage is a principal reselling third-party capacity: two-sided price on each load (customer charge vs carrier pay) with the margin spread managed and settled in both directions; it operates no trucks. The trucking TMS operates its own capacity: revenue billed to customers and pay settled to its own drivers on the carrier's own books — no resale margin. Strip the resale/margin machinery from a brokerage → a carrier's own books (trucking); strip own capacity from a carrier → brokerage. The hybrid asset-based-brokerage pole (Alvys "Hybrid"; TMW.Suite also serving brokers) runs both supply identities in one product with an explicit toggle — keep-both confirmed; the toggle is the seam made visible inside one product. Owner-operator pay is the recorded gray zone: the settlement payee can be a contracted owner-operator (pay form approaches carrier-pay), but the capacity is still the carrier's own dispatched supply — the seam holds on whose trucks and whose authority, not on the employment form.
3. **vs Load Board / Freight Marketplace (§18, processed) — RATIFIED.** The carrier's own operations system vs the market where the carrier finds loads. A carrier uses both: all sampled products integrate DAT/Truckstop-class boards (post and search), while the board holds no dispatch, fuel, maintenance, or driver-settlement machinery. Board integration is standard capability; venue membership is not part of this Type.
4. **vs Dispatch Management (§18, processed) — RATIFIED.** The dispatch machinery (work queue × resource roster × assignment act × live board) is the operational core inside the trucking TMS; the freight business frame (load money, settlement, compliance, EDI) is what makes the surrounding system a trucking TMS. Truckbase self-labels "dispatch-centric TMS" — the dispatch pass sampled its dispatch surface; this pass reads the same product as a trucking TMS whose flagship module is dispatch. Both readings are consistent: remove the business frame → dispatch management; add it → trucking TMS.
5. **vs Fleet Management System (§18, processed) — RATIFIED.** Vehicles as managed estate (maintenance/fuel/telematics center) vs loads as business record. The trucking TMS holds trucks as revenue-producing capacity and ties cost machinery to them; deep maintenance is a module or sibling product. Consistent with the FMS pass's own exclusion of freight/loads/settlements.
6. **vs Driver Management (§18, processed) — RATIFIED.** Person-centered credential/entitlement records (DQF-class files, licence checks, governed entitlement state) vs the carrier's capacity-and-payee view of drivers. The trucking TMS consumes driver availability and compliance state and holds pay arrangements; the person-record discipline is the sibling leaf's center.
7. **vs Electronic Logging Device / HOS Platform (§18, processed) — RATIFIED.** Duty-status compliance record vs freight execution. ELDs are the data suppliers (Truckbase: 30+ integrations; Alvys: HOS/location feeds); the HOS clocks and log governance live in the ELD leaf; the trucking TMS consumes them for dispatch awareness and alerting.
8. **vs Courier Management Platform (§18, processed) — HELD, keep-both.** Structurally similar shape (own workforce + orders + dispatch + POD + billing on the operator's own books), but different work semantics and cost machinery: courier = parcel/delivery jobs with zone/route/stop rating and courier workforces; trucking = freight loads with lane/equipment semantics, tractor-trailer equipment, driver settlement per load/mile/%, and fuel-tax machinery. The shared "own-capacity operator" pattern does not collapse the two; the work item's semantics and the money machinery differ.
9. **vs Freight Forwarding System (§18, processed) — light touch.** Naming note confirmed from this side: "TMS" is shared market vocabulary across seats (forwarder products are also marketed as TMS); the word does not isolate the Type. The forwarder's center is international consignment/document/charge machinery; the trucking TMS's center is domestic freight hauled by own trucks.
10. **vs Shipment Visibility Platform (§18, processed) — HELD.** The watching layer vs the system of record. The trucking TMS is the executing party; tracking data flows from its own trucks (ELD/driver app) into its own loads. Visibility platforms watch freight other parties carry without committing or settling.
11. **vs Transportation Exception Management (§18, processed) — HELD.** The exception desk vs the ops system; exception machinery inside the trucking TMS (alerts when loads fall behind, delay/breakdown handling) is an L1 capability.
12. **vs Route Optimization Platform (§18, unprocessed) — capability vs system.** Optimization depth varies (Truckbase ships none natively; mileage calculation is standard); the optimization engine is a capability the TMS may embed or integrate.
13. **vs School Transportation / Employee Transportation / NEMT platforms (§18, unprocessed)** — passenger-transport siblings: the managed object is passengers/recurring service routes, not freight loads; different money frame. Not sampled; recorded as adjacent, expected keep-both.
14. **vs Accounting Software (generic)** — the trucking TMS holds the load-anchored money frame and integrates to general accounting (QuickBooks-class sync in all samples); it is not the general ledger.

## Historical / Market-Sample Check

- **Paper-era trucking company** (pre-software): a dispatch board/logbook where loads were assigned to truck+driver by phone; a load ledger carrying rate, customer, and driver; driver pay statements computed per mile/load/percentage; fuel and maintenance logs per truck; fuel-tax/trip-permit reporting; invoices mailed to shippers and brokers; BOL/POD paper flow with document filing. All three L0 legs are satisfied at analog level — load record, own capacity, load-anchored money both directions — with zero software. The vendors' own marketing documents this baseline (Truckbase: "It's time to ditch the spreadsheets"; the dispatch pass recorded Truckbase's check-call-era narrative). PASSES.
- **Early PC-era trucking software** (1980s–90s dispatch/billing/settlement packages): load entry, dispatch, invoicing, driver settlement, fuel-tax reporting. PASSES with no EDI/ELD/GPS/cloud.
- **Regional check**: non-US carriers run equivalent businesses under different regimes (tacho-graph duty records, national fuel-tax schemes, different document customs); the L0 names no regulator, no ELD mandate, no IFTA specifically (fuel-tax machinery is named as a class). PASSES.
- **Owner-operator extreme**: a single-truck carrier is simultaneously the capacity, the dispatcher, and the bookkeeper; the three legs still hold (load records, own truck+driver, billing + self-settlement). PASSES.
- No over-fitting to the current SaaS/AI era detected: the L0 names no EDI, ELD, GPS, apps, AI, or cloud.

## Uncertainties

- **Deep help-center articles not drilled** (Alvys index only; Truckbase/Trimble at product-page depth). Exact status vocabularies, settlement-cycle defaults, pay-period conventions, invoice-match tolerances, and permission models are deliberately NOT asserted.
- **Enterprise/legacy pole unverified** (McLeod 403 ×2 across passes): the traditional enterprise carrier suite's internal structure is inferred from Trimble's enterprise positioning and ecosystem naming; no claim depends on it.
- **Modern multi-mode carrier SaaS pole unverified** (Rose Rocket 403 ×3 across passes): the newest SaaS carrier TMS generation is represented only by Trimble TMS for Carriers and Alvys; no claim depends on Rose Rocket.
- **Owner-operator settlement mechanics** (escrow, lease-purchase deductions, factoring advances) observed only as feature names; not asserted in detail.
- **Settlement depth variation**: whether every trucking TMS ships settlement natively vs via payroll integration could not be verified to equal depth in all products (Trimble names payroll integrations; Truckbase/Alvys ship native settlement). The L0 holds the pay side as load-anchored money; the native-vs-integrated realization is recorded as implementation variance.
- **Regional breadth**: all sampled products are North America-centric; the regime-neutral wording is a hedge, not direct non-US vendor evidence.
- **Private-fleet money frame**: for private fleets the "revenue" side may be internal cost allocation rather than external billing; the variant is recorded but the private-fleet pole was not sampled deeply (Alvys/TMW marketing pages only).

## Final Synthesis

A Trucking Management System is the motor carrier's own business system of record. Its defining core is three jointly-held structures: the load as the unit of business record carrying the operation from booking through dispatch, haul, and delivery to billing; the carrier's own trucking capacity — its trucks and drivers — as the dispatchable supply whose availability assignment consumes; and the load's money on the carrier's own books — the customer rate that becomes an invoice and the driver pay that becomes a settlement, with the trucks' operating costs tied to the business. Around this spine mature products add the dispatch board, event-driven tracking from the truck, the rate-confirmation/BOL/POD document flow, EDI connectivity with customers, compliance machinery, fuel-tax and maintenance cost machinery, customer-facing visibility, analytics, and an accounting/factoring/load-board integration spine. The Type's edges are held by seat (shipper TMS buys carriage — ratified; brokerage resells third-party capacity — ratified; load board is the venue — ratified), by act (dispatch is the operational core inside — ratified), by estate (FMS owns the vehicle estate), by person (Driver Management owns the person records), by duty-status compliance (ELD), and by work semantics (courier/delivery). The paper-era trucking office — dispatch board, load ledger, driver pay statements, fuel logs, invoices — satisfies the defining core, so the abstraction is not an artifact of the current SaaS market.
