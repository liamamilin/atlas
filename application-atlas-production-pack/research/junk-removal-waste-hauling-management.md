# Research Notes — Junk Removal / Waste Hauling Management

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 + WRITING_GUIDE_v1.1)

## Research Goal

Understand what business-management software for companies that haul junk and waste actually is: what objects exist inside it, how work flows from customer request to billed service, what the junk-removal pole and the waste-hauling pole share, and where this Type sits against neighboring Types (generic field service, moving companies, municipal/environmental waste systems).

## Initial Boundary

- DIRECTORY position: §29 Home, Family, Personal & Local Services, among local service business management leaves (Moving Company Management, Handyman Business Management, Small Business Field Service Management). So the leaf is the **operator-side system of record for hauling businesses**, not a consumer-facing app.
- The leaf name spans two poles: **junk removal** (per-job cleanouts, bulky-item pickup) and **waste hauling** (recurring collection of residential/commercial waste, roll-off containers). The directory also contains a separate sibling leaf **Waste Hauling Management** in §21 Environment (line 1514) — a potential duplicate/alias across sections (see Boundary Findings).
- Nearest neighbors to separate from: Small Business Field Service Management (§29), Moving Company Management (§29), Waste Management Platform / Recycling Operations Management (§21), Route Optimization Platform / Dispatch Management (§18), Home Services Marketplace (§29, processed 2026-09-08).

Initial hypothesis: a field-service-style business system whose defining difference is the haul domain — the cargo is waste leaving the customer's site toward disposal, work is dispatched to truck crews (often recurring routes), and money is made per pickup/container/weight, including disposal fees.

## Research Questions

1. What are the core objects: customer accounts, jobs/stops/orders, trucks/routes, containers, disposal events?
2. How does work flow: request → quote/booking → scheduling/dispatch → field execution → billing → disposal documentation?
3. How does pricing work (per pickup, per volume/weight, per container rental, disposal/tip fees)?
4. How do recurring collection accounts differ from one-off junk jobs inside the software?
5. What machinery exists on the disposal side (scale house, tip tickets, material destinations, compliance paperwork)?
6. Which interfaces do office dispatchers vs drivers actually use?
7. What separates this Type from generic field service management applied to a vertical?
8. Is the junk-removal pole structurally the same Type as the waste-hauling pole?

## Representative Products

Selected for market representation, different product philosophy, different customer layer, and coverage of both poles in the leaf name:

| Product | Pole | Philosophy / layer | Docs reached |
|---|---|---|---|
| Trash Flow (Ivy Computer, Inc.) | waste hauling | legacy Windows desktop, module-priced, hauler-dedicated since 1985; small haulers | vendor product pages (routing, container tracking, landfill/TipTicket, TeleRoute, billing) |
| Waste Logics | waste hauling (UK) | cloud, end-to-end waste business automation incl. weighbridge + compliance; skip hire / trade waste / MRF / broker | vendor home + feature/plugin pages |
| Hauler Hero | waste hauling | modern cloud SaaS for haulers (residential / commercial / roll-off / government); dispatcher+driver+CSR positioning | vendor home + billing + mobile feature pages |
| Workiz (junk removal vertical) | junk removal | generic field-service platform with a dedicated junk-removal industry page and a large junk-removal customer roster | vendor root + industries + junk-removal page |

Rejections / gaps: Jobber and Housecall Pro junk-removal pages returned 403 (both are known to market junk-removal verticals; used only as background). JunkJam (dedicated junk-removal product) unreachable twice → abandoned. Docket (roll-off software) rendered empty. Workiz help center (Tier-1) timed out. Bing/DuckDuckGo searches unproductive.

## Sources

- Trash Flow — https://www.trashflow.com/ (root), /billing-solutions.php (linked, not fetched), /container-tracking.php, /landfill-management.php, /teleroute.php, /route-optimization.php (linked) — fetched 2026-09-08
- Waste Logics — https://wastelogics.com/ (home incl. feature/plugin summaries and FAQ) — fetched 2026-09-08
- Hauler Hero — https://www.haulerhero.com/ (home), /features/billing, /features/mobile — fetched 2026-09-08
- Workiz — https://www.workiz.com/ (root), /industries/ , /industries/junk-removal/ — fetched 2026-09-08
- Negative results: jobber.com & getjobber.com (403), housecallpro.com (403), junkjam.io (transport error ×2), withdocket.com (empty JS shell), help.workiz.com (timeout), bing.com search (unusable results), html.duckduckgo.com (timeout)

Evidence layers used below: **[A]** directly observed on an official page of one product; **[B]** observed across multiple products; **[C]** canonical inference from cross-product comparison + boundary reasoning.

## Product A — Trash Flow (Ivy Computer, Inc.)

### Key observations [A unless noted]

- Positioning: "all-in-one software solution" for waste haulers; developing for the hauling industry since 1985; Windows desktop, module-priced, network/SaaS options. Compares itself against QuickBooks ("the power of Trash Flow" vs general accounting) — marketing, but confirms the billing-led self-image.
- Billing (Standard/Advanced Billing): financial & customer reports; print statements and invoices; **create work orders and dispatch to specific drivers or trucks**; e-mail billing; online payments (Web Pay); Accounting Link; Event Tracking records account activity.
- Route management: real-time fleet tracking; route optimization ("shortest possible distance between stops"); AVS mapping of customer locations.
- Container Tracking: handles **roll-offs, compactors, dumpsters, carts** and other containers; track location, placement, purchase and placement history; search placements by container or customer; **placement slots** — bill the slot rather than the serial number, containers can be swapped without touching billing; rental fees beyond a free-day period; container inventory reports.
- Customer-specific rate types [A]: hauling fees, **tip / disposal fees**, flat rates, overweight charges, minimum charges, pick-up/pull fees, drop fees, daily rental fees.
- TeleRoute (in-truck app for tablets/phones): hands-free stop completion; report "no trash out" / "dumpster blocked" with one tap + photo **stored on the customer record**; record extra services (clean-ups, Christmas trees, couches) "for easy charging later"; dispatcher's work-order sequence appears on the driver device in real time; drivers record images/notes/activity per work order; works through intermittent cell service; routes in the office **auto-reorder based on how the driver actually ran them**; two-way messaging with quick replies; trucks "phone home" per stop (live map + historical stop times); **digitizes landfill tickets (tips and costs)**; fuel and breakdown tracking.
- Landfill Management / TipTicket: scale-house operations — weigh in/weigh out or tare-weight operation; separate tare weights for trailers/containers; charge by **ton / metric ton / pound / yard / each**; multi-pass; cash-customer warnings; ticket printing with dollar amounts; cash at the scale house; offsite scale house with central billing. Transfer-station management: outbound material recording, origins/destinations of materials, real-time material inventories, yard management, traffic monitoring.
- Material Tracking (MAT Track): assign destinations per material + quantities, assign trucks, track transactions.
- Dispatch: single screen for all container work orders; drag-and-drop reassignment between drivers.

## Product B — Waste Logics

### Key observations [A]

- Positioning: cloud "end-to-end waste management business automation" for **skip hire companies, trade waste collection businesses, MRFs, waste transfer stations, waste brokers, tippers/aggregates, scrap metal processors** (FAQ). Usage-priced subscription.
- CRM: prospective + existing customers, opportunities/tasks, 12-month pipeline.
- Online Cart: customer gets a quote, books and pays on the hauler's website; order auto-syncs into the main system.
- Order Management: book orders; monitor **resource availability**; track orders "from order to invoice"; historical/current/pending orders.
- Logistics: drag-and-drop **rounds** optimization with maps/trails; paper or paperless driver tickets (run sheets).
- Brokerage & Subcontractor Portal: subcontract work to others; track all parties and **profit margin per job**; auto-email purchase orders to subcontractors.
- Billing: flexible sales invoices per customer requirement; **self-bills**; supplier invoice matching; integrations with Sage, QuickBooks, Xero, Pegasus Opera, SAP Business One, KashFlow.
- Driver apps: walk-around **vehicle checks**; run sheet + job details; navigation; **electronic signature capture**; raise job issues; take photos; **offline** with sync.
- Weighbridge & Compliance: record weights via **live weighbridge link or manually**; detail compliance issues with loads; record deductions and photos; electronically signed **annual duty of care notes**; **auto-generated compliance documents** (incl. hazardous waste consignment notes); integration work for **Digital Waste Tracking** ahead of an October 2026 mandatory deadline (UK regulatory context).
- Containers: "record and manage all of your containers in one system, including type, size, location and movements… on site, out on hire, or due for collection" (FAQ).
- Customer Portal: self-serve copy invoices, e-tickets, **recycling reports**, book orders, order updates.
- Analytics: real-time KPIs, custom dashboards per role; **profit per round**; landed price analysis; debtor management; recycling rate and CO₂ reporting; ESG software integrations.
- Weighbridge management: "track all materials in and out of facilities."

## Product C — Hauler Hero

### Key observations [A]

- Positioning: cloud software for waste haulers; "designed not just for owners, but also for **dispatchers, customer service representatives, and dedicated haulers**"; 250+ haulers; serves **commercial, residential, roll-off, governments**. Seed-funded modern SaaS.
- CRM ("Customer Manager"): all customer info in a single view; **set prices, add services**; resolve issues; modern search.
- Dispatch & Routing: drag-and-drop dispatching; track **route progress**; "reroute with a click and keep your drivers in sync"; avoid scheduling errors.
- Mobile app ("Hauler Hero Road"): view and complete **stops on a map** (tap a stop, preview details, complete "as you grab a can in the field"); **offline mode** with sync when back online; drivers **log customer delays and route disruptions** ("understand cost-per-stop"); automatic property-feature alerts; exception notifications; "capture critical data at every stop"; **truck inspections before and after every shift** (drag-drop issue recording).
- Billing: **payment groups** — see which customers are in which **billing cycle** and their history; invoice search by payment/service type and status; **filter edge cases out of bulk invoicing**; **batch payments** for cash/check customers ("fly through entering a stack of payments"); **profile-based billing** — per-customer billing cycle and payment method.
- Reporting: real-time route progress, cashflow; **"pulls per day, yards per hour"** KPIs.
- Follow Up: capture and auto-generate **requests, complaints, exceptions** in one place for triage.
- Customer Portal: online payments, service history.
- Scale integration ("At The Scale"); inventory management; APIs for external integrations.
- Homepage: "bill accurately for **overloaded containers**"; "guide new drivers effortlessly to containers."
- Testimonial evidence: office manager describes billing cycles compressing a day of invoicing work; co-owner describes driver pins + check-offs and answering skip/when questions from the office.

## Product D — Workiz (junk removal vertical)

### Key observations [A for positioning/vertical evidence; features are generic field-service machinery]

- Positioning: dedicated junk-removal industry page ("The #1 junk removal app… over 3k haulers… Schedule, dispatch, estimates and invoices all in one place"); junk removal is one of ~24 named industries. Customer roster/testimonials include many junk removal & hauling companies (JDog Junk Removal & Hauling, Junk Doctors, McHugh Junk Removal, Sonoma Strong Hauling & Junk Removal, Haul Away Junk Removal, Junk Masters, Junk Trunk, Junk Out Now, Top Dawg, Bumsi, Bros Pro Hauling, Cupid Disposal) — strong evidence that **per-job junk removal businesses are substantially served by generic field-service platforms**.
- Job model: jobs scheduled on a drag-and-drop calendar and dispatched; junk removal jobs "categorized"; leads captured (incl. from lead-marketplace integrations: Angi, Thumbtack, Yelp, Google Local Services) and turned into jobs.
- Estimates: instant estimates to "be first to respond"; "good, better, best" sales proposals.
- Field execution: mobile app; on-my-way texts; **invoices generated as soon as the job is completed**; field payments with card readers; payment plans for high-priced jobs.
- Routing: route planning + **GPS tracking** of techs/trucks; route optimization claims.
- Communications/retention: reminders, review requests, campaigns.
- Accounting: QuickBooks sync. Payments via Stripe-based "Workiz Pay".
- Marketing figures on the page (e.g., "22% revenue increase", "30% gas cost reduction") — **vendor marketing, not carried into the final document**.
- Nothing junk-domain-specific observed in-product on fetched pages: no containers, no routes-as-rounds, no scale/disposal machinery.

## Cross-product Comparison

| Structure | Trash Flow | Waste Logics | Hauler Hero | Workiz (junk vertical) |
|---|---|---|---|---|
| Customer accounts with configured services + prices + history | ✓ | ✓ (CRM + contracts/rounds) | ✓ ("set prices, add services") | ✓ (customer history) |
| Haul service event as unit of work (stop / order / job) | ✓ (work orders, stops) | ✓ (orders) | ✓ (stops, services) | ✓ (jobs) |
| Dispatch to truck / driver / crew | ✓ (to specific drivers or trucks) | ✓ (rounds, run sheets, driver app) | ✓ (drag-drop, reroute, driver sync) | ✓ (drag-drop calendar, GPS) |
| Field execution capture by the crew | ✓ (complete stops, photos, exceptions, extra services) | ✓ (signature, photos, issues, offline, vehicle checks) | ✓ (complete stops, data capture, delays, offline) | ✓ (mobile job completion, on-site invoicing/payment) |
| Billing generated from recorded service | ✓ (invoices/statements; disposal & rental rate types) | ✓ (order→invoice, self-bills) | ✓ (cycles, profiles, batch payments) | ✓ (invoices, field payments) |
| Recurring routes / rounds | ✓ (route management, reordering, optimization) | ✓ (rounds, profit per round) | ✓ (route progress, cycles) | route planning only (no rounds concept observed) |
| Containers as placed assets (roll-off/dumpster/skip) | ✓ (placement slots, rental, history) | ✓ (type/size/location, on hire, due for collection) | ✓ (inventory, container guidance, overload billing) | — |
| Disposal side (scale/weights/tip tickets/material destinations) | ✓ (TipTicket scale house; MAT Track) | ✓ (weighbridge, e-tickets, duty of care) | ✓ (scale integration; overload billing) | — |
| Compliance paperwork (manifests/duty of care) | — | ✓ (auto-generated consignment notes) | — | — |
| Customer portal / online booking & payment | ✓ (Web Pay) | ✓ (portal + online cart) | ✓ (portal) | ✓ (online booking) |
| Brokerage / subcontracting | — | ✓ | — | — |
| Accounting integration | ✓ | ✓ | ✓ (APIs) | ✓ |
| Driver vehicle/truck inspections | — | ✓ | ✓ | — |

**[B] jointly held by all four:** customer service accounts; the service event as unit of work; dispatch to truck crews; field execution capture; billing from recorded service. These are the candidate defining structures.

**[B] held by the three dedicated hauler products only:** recurring routes/rounds; containers as placed assets; disposal-side capture (scale/weights/tickets/destinations); hauling-specific KPIs (pulls per day, yards per hour, profit per round).

**[A] single-product:** brokerage/subcontractor portal (Waste Logics); UK duty-of-care/consignment-note generation (Waste Logics); placement-slot billing implementation (Trash Flow); payment groups / profile-based billing (Hauler Hero); good-better-best proposals (Workiz).

## Canonical Model

### Level 0 — Defining Invariant [C, supported by B evidence]

The hauler-side system of record for a waste/junk hauling business, defined by three jointly-held structures plus the domain binding:

1. **Customer service accounts of record** — each served customer/location held persistently with the haul services configured and priced for it (what gets collected, how often or on request, at what container/size terms), accumulating service history. Remove → contact list / rate card, not a business system.
2. **The haul service event dispatched to truck crews** — the stop/order/job as the unit of work: material to be collected at a location, scheduled (recurring round or booked slot) or taken on demand, assigned to a truck/driver/crew, with execution recorded back (completion, exceptions, evidence such as photos). Remove → static customer database or a bare dispatch board.
3. **Billing generated from recorded service** — completed events and their attached charges (base service, extras, exceptions) are priced to the account and flow into invoices/payments. Remove → dispatch tool with no revenue loop; the "management" is gone.

**Domain binding:** the cargo is unwanted material **leaving** the customer's site toward disposal/transfer/recovery; the mobile unit is the **truck and its crew** (not a technician visiting a site). This binding is what makes it hauling rather than generic field visits or goods relocation. [C]

Jointly-held is load-bearing:
- 1 alone = CRM/rate card; 2 alone = dispatch board; 3 alone = generic invoicing.
- 1+3 without 2 = a billing system (the software's own "vs QuickBooks" seam confirms this is not enough for the Type).
- 1+2 without 3 = dispatch software with no financial loop.
- 2+3 without 1 = one-off jobs with no served population (booking tool).

### Historical / market-sample check [§24 discipline]

- Paper-era hauler office: route books / run sheets listing each truck's stops; customer cards with rates, container sizes, collection frequency; trip tickets for extra pickups; dump tickets from the scale house; monthly billing ledger compiled from the run sheets — satisfies all three legs at analog level. ✓
- UK trade-waste pole with skip hire terminology satisfies without US "roll-off" vocabulary; duty-of-care paperwork is a regulatory variant, not part of the invariant. ✓
- A junk-removal business run on generic field-service software satisfies legs 1–3 with none of the route/container/scale machinery (the domain binding lives in how jobs are named and performed). ✓ — the Type holds at maximum abstraction only if the route/container/disposal machinery is NOT required.

### Level 1 — Common Mature Structure [B for dedicated products]

Very common in mature dedicated products; not required to define the Type:

- recurring routes/rounds with run sheets, stop reordering, route optimization, GPS fleet tracking
- driver mobile app: offline tolerance, photos, e-signature, exception reporting ("no trash out", "blocked"), navigation, vehicle/truck inspections
- containers as placed assets (roll-off/skip/dumpster lifecycle: drop → filled → pull; placement/on-hire state; rental-beyond-free-period)
- disposal-side capture: scale-house weights, tip/dump tickets, material origins/destinations, overload billing
- customer self-service: portal (invoices, e-tickets, service history, recycling reports), online booking/cart, online payments
- exception/follow-up triage (requests, complaints, missed-service handling)
- hauling KPIs (pulls per day, yards per hour, profit per round, cost-per-stop class metrics) and accounting-system integrations

### Level 2 — Variant / Optional Structure

- **Pole by service model**: (a) per-job junk removal (on-demand, quoted jobs — frequently run on generic field-service platforms; disposal machinery often absent in-product); (b) recurring route collection (residential/commercial rounds); (c) roll-off/skip/container services (container rental + pull cycle). The leaf name explicitly spans (a) and (b/c).
- Customer segment: residential / commercial / industrial / government-municipal contracts.
- Regulatory context: UK duty-of-care + consignment notes + digital waste tracking; US scale-house practice; overweight enforcement.
- Business model: direct hauler vs waste broker with subcontractor portals and self-billing.
- Deployment/era: legacy Windows desktop module suites vs modern cloud SaaS.
- Scale-house operator as a distinct seat; offsite scale houses.

### Level 3 — Vendor-specific Structure (Research Notes only)

- Trash Flow: TipTicket, TeleRoute, MAT Track, AVS Mapping, Unified BillCom names; listed module prices ($250–$4,150; $35/truck/month); Windows 10/11 runtime; "QuickBooks comparison" marketing.
- Hauler Hero: "payment groups", "Hauler Hero Road", Hero Vision/Hero Chat/Hero Routing AI prototypes, TrashBolt integration, marketing percentages (19% faster cash collection etc.).
- Waste Logics: usage-based subscription; named accounting packages; 6.5-days-saved marketing figure; October 2026 Digital Waste Tracking deadline; Connect SMS.
- Workiz: Genius AI suite (Answering/Scheduling/Marketing), Workiz Pay (Stripe), Sunbit/Wisetack financing, lead-marketplace integrations, "3k haulers"/"22%"/"30%" claims.

## Vendor-specific Findings

See Level 3. Additionally: Trash Flow's placement-slot billing and Hauler Hero's payment groups are implementations of the shared concepts (container billing; billing-cycle management) and are not promoted to the canonical model.

## Rejected Findings

- "AI call answering is core" — single-vendor packaging (Workiz Genius); rejected for the Type.
- Marketing performance figures (22% revenue, 30% fuel, 19% cash collection) — unverifiable vendor claims; rejected.
- "Desktop Windows is the norm" — Trash Flow's packaging only; cloud is equally represented; rejected.
- "Bill by placement slot" — implementation detail of one product; the concept (containers billed independently of physical serial numbers) is retained at concept level only.
- "Compliance paperwork generation is definitional" — Waste Logics only [A]; UK regulatory context; held as variant.

## Boundary Findings

- **vs Waste Hauling Management (§21 Environment sibling, unprocessed)**: suspected duplicate/alias — the §21 leaf and this §29 leaf name near-identical software (hauler-side collection/route/billing systems). The dedicated products sampled here are exactly what a §21 "Waste Hauling Management" research pass would sample. → Flag for joint review; recommend the two leaves be reconciled (merge or explicit split by operator scale/municipal context).
- **vs Small Business Field Service Management (§29 sibling)**: the junk-removal pole demonstrably runs on generic FSM products (Workiz's vertical page + roster). The seam: dedicated hauler products carry structures generic FSM lacks (containers, rounds, scale/disposal, hauling rate types). Keep both Types; record the overlap. If a future pass finds the leaf only describable as "FSM vertical," downgrade to Variant.
- **vs Moving Company Management (§29 sibling)**: same truck+crew+job shape, but moving cargo goes between two customer-controlled points (origin→destination household/business); hauling cargo leaves the customer's site toward disposal. Different billing semantics (load/volume/disposal fees vs move/crew/hours).
- **vs Waste Management Platform (§21)**: enterprise/municipal waste *program* management (contracts, compliance, reporting across sites/contractors) vs the hauler's own *operations* system of record. Not fetched this pass — distinction held conceptual, weak wording.
- **vs Recycling Operations Management (§21)**: facility-side processing (MRF operations) vs collection side. Trash Flow's landfill/scale modules show dedicated hauler products can extend into facility management — adjacent extension, not the Type.
- **vs Home Services Marketplace (§29, processed)**: consumer-facing two-sided venue vs operator-side system of record. Marketplace pass listed junk-removal as one trade among many.
- **vs Route Optimization Platform / Dispatch Management (§18)**: algorithmic capability vs complete business system of record (dispatch is one surface inside this Type).

## Uncertainties

- No Tier-1 help-center/user-manual articles were reachable for any sampled product (Workiz help center timed out; Trash Flow/Waste Logics/Hauler Hero pages are official product pages, which document feature existence but not detailed UI workflows). → All workflow descriptions in the final document are kept conceptual; no numeric limits, exact status names, or default values are asserted.
- The junk-removal pole is evidenced mainly through generic-FSM vertical pages; dedicated junk-removal products (e.g., JunkJam) were unreachable. Whether such products carry containers/disposal machinery is unknown.
- Whether generic FSM products model dump fees/disposal costs in-product: not evidenced either way; not claimed.
- Enterprise/municipal hauler segment (government contract billing, municipal rounds at city scale) under-sampled (Hauler Hero governments page not fetched).
- Hauler Hero "At The Scale" page not fetched; scale integration claimed at homepage level only [A, weak depth].

## Final Synthesis

One Application Type with two realizations sharing one spine:

> A junk removal / waste hauling management application is the hauling company's system of record: it holds each served customer/location with its configured services and prices; materializes every pickup as a service event dispatched to a truck crew; records what the crew actually did in the field (completions, exceptions, evidence); and turns those recorded events into the company's billing — with the domain binding that the work is waste leaving customer sites toward disposal.

The dedicated-hauler realization wraps this spine in route/round machinery, container asset tracking, and disposal-side capture (scale, tip tickets, material destinations); the per-job junk-removal realization runs the same spine, frequently on generic field-service platforms, organized around quoted one-off jobs. Older, regional (UK skip-hire/trade-waste), and paper-era operations satisfy the same three-leg definition, so the defining core is deliberately free of routes, containers, scale houses, AI, and any specific identity or pricing implementation.
