# Research Notes — Moving Company Management

## Research Goal

Understand what the software sold to moving companies actually is and how it works, from real vendor documentation — not from the category name. The leaf sits in DIRECTORY §29 "Home, Family, Personal & Local Services", among trade-business leaves (Junk Removal / Waste Hauling Management, Handyman Business Management, Small Business Field Service Management, Self-storage Management). The likely shape (hypothesis to verify): the operator-side business system of record for relocation carriers — quote-first jobs performed by crews with trucks between two customer addresses — as distinct from generic field service, hauling, and freight software.

## Initial Boundary

- The leaf names the **mover's own** business system (operator side), not a consumer moving marketplace and not carrier/freight logistics.
- Nearest neighbors to separate from:
  - Junk Removal / Waste Hauling Management (§29 sibling, processed 2026-09-08 — its Related Types table already records a Moving boundary: "same truck-and-crew shape, but cargo moves between two customer-controlled points (origin → destination); hauling cargo leaves the site toward disposal. Different pricing semantics").
  - Small Business Field Service Management (§29) — the generic sibling family.
  - Trucking Management System / Courier Management Platform / Last-mile Delivery Platform / Towing Dispatch Platform / Dispatch Management / Driver Management / Route Optimization Platform / Fleet Management System (§18).
  - Self-storage Management (§29) — mover-side storage modules may straddle.
  - Home Services Marketplace / Local Service Marketplace (§29) — demand side.
- Potential confusion inside the name: "Management" could mean CRM-only, dispatch-only, or full business system. Market sampling must decide what the market actually sells.

## Research Questions

1. What is the unit of business record — the "move"? What does one job bind together?
2. How is a move priced and sold? What does an estimate attach to (inventory? rooms? weight? hours)?
3. How does execution work: crews, trucks, legs (pickup/delivery), documents, signatures?
4. What money loop runs on the job (deposits, balance, payment on delivery, invoicing)?
5. Which objects are moving-industry-specific vs generic field service: inventory of goods, bill of lading, valuation/liability, storage-in-transit, claims, tariffs?
6. Who uses the system and on which surfaces (office, crew, customer)?
7. What lifecycle/states does a job traverse? What are the important exceptions (overbooking, scope changes, damage, destination not ready)?
8. Where is the boundary against generic FSM, hauling, trucking, and courier software — and what "remove X → becomes Y" criteria hold?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| SmartMoving | Modern cloud vertical SaaS, quote/sales-first philosophy, US market leader positioning | Deep public feature documentation (estimates, operations, storage) |
| Supermove | Modern AI-era platform, HHG + commercial/office & industrial movers | Different product philosophy (AI/automation-led), commercial pole |
| Elromco | Cloud all-in-one vertical (founded 2015), long-distance/interstate depth | Richest documentation of the long-distance/regulatory machinery (tariffs, binding estimates, SIT, weight tickets, BOL) |
| Workiz | Generic horizontal field-service platform with a Moving industries page | Generic-pole control: evidence that movers are also served by horizontal FSM (family boundary check) |
| MoveitPro | Long-established vertical suite (desktop heritage) | **Unreachable** — www and non-www both returned 403; abandoned after two attempts; recorded as sourcing limitation |

Historical / market-sample check performed conceptually at the paper-era analog level (see Final Synthesis) because the legacy-generation product could not be fetched.

## Sources

- SmartMoving — https://www.smartmoving.com/ ; feature pages: Smart Estimates (https://www.smartmoving.com/smart-estimates), Streamline Operations (https://www.smartmoving.com/streamline-operations), Manage Storage Efficiently (https://www.smartmoving.com/manage-storage-efficiently). Research date 2026-09-08. Tier 2 (official product pages).
- Supermove — https://www.getsupermove.com/ (home page; the site is an SPA serving identical content across deep URLs). Research date 2026-09-08. Tier 2.
- Elromco — https://www.elromco.com/ ; Long-Distance Moving Software (https://www.elromco.com/features/long-distance-moving-software). Research date 2026-09-08. Tier 2.
- Workiz — https://www.workiz.com/industries/ (industries index listing Moving). Research date 2026-09-08. Tier 2.
- Unreachable / abandoned: MoveitPro (403 ×2), Supermove help center (help.supermove.com, timeout), Jobber moving-industry URL (403). Per source-access rules, no claims drawn from these; precise screen-level workflows were not verifiable and the final document stays conceptual.

All observations below are Layer A (directly observed on the cited official page) unless marked B (cross-product) or C (canonical inference).

## Product A — SmartMoving (smartmoving.com)

### Key observations (A)

- Positioning: "All-in-One Moving Company Software and CRM"; explicitly: "SmartMoving doesn't work for electricians, plumbers or retailers. **We're purpose-built for moving companies and moving companies only**" — a vendor-drawn line against generic field service.
- Module map (nav): Sales Automation; Estimates & Pricing; Dispatch & Crew Management; Customer Experience; Reporting; Accounting & Payments; Storage Management; Reputation (ORM).
- Estimates page:
  - Inventory capture is the estimate's substrate: "pre-loaded list of inventory" items clicked into the CRM; item search; custom items; **room-based inventory list** ("Make reviewing inventory easier for the customer and your crew"); inventory taken on-site on a tablet; **virtual surveys** via video integration (LiveSwitch); customers can fill out inventory themselves via the **customer portal**; upsell of materials/additional services from inside the inventory workflow.
  - Pre-2024 workflow named as the enemy: "manually filling out cube-sheets to take inventory" — i.e., the traditional industry artifact the software digitizes is the **cube sheet** (room-by-room goods survey).
  - Pricing rules engine: minimum job hours, not-to-exceed amount, minimum price to book; crew base rates per day of week; trip and truck fees; default room sizes; **crew and truck requirements derived from weight or volume**; **crew capacity (weight/volume per hour)**; **time handicaps for stairs/elevators**; tariff groups per state; 400N-style tariff support ("SM-100 Managed Tariff"); hourly or mileage-based estimates; estimates can be **binding, non-binding, binding-not-to-exceed, or a price range**; valuation, sales tax, storage charges added on the estimate; system recommends "the time, trucks and crew required and cost of the move based on the move location, date and size of the move".
  - Estimate delivery: branded estimates by text/email, digital sign-off, **deposit paid from the customer's phone via the portal**.
- Operations page:
  - Real-time resource calendar: capacity vs demand per month; overbooking visibility; demand-based pricing ("raise your rates on high demand days").
  - Dispatch: drag-and-drop **trucks and crew members** onto moves; out-of-service trucks and movers-on-leave cannot be added accidentally; templates with pre-assigned crews/trucks for weekdays or long-distance moves.
  - Crew communications: automated texts on assignment; crew confirms availability in the **crew mobile app**; customer confirmation of move details the day before.
  - Progress monitoring: "Know when your crew has arrived, when they're loading the trucks and when they're on the go"; hours per step; delay identification.
  - Crew app: assignments, job details, **materials checklists**; ETA notifications to customers; **digital bills of lading** walked through with the customer, **electronic signatures** collected in-app; per-crew-member permissions (who may take payments, apply discounts); **automatic crew-hours calculation from job start/stop/travel/break times** "to simplify billing and payroll".
  - Digital documents: all linked to the customer's account; signatures on documents **and deposits**; reschedule/cancel with resource recalculation; one state regulator (North Carolina Utilities Commission) approval noted for digital documents for local and intrastate moves.
- Storage page: storage **accounts** (individual and commercial), imported via Excel; custom storage rates per warehouse/zone/customer; **containers occupied by each customer**; **printed container tags**; customer storage portal; auto-pay (card/ACH); aging/overdue reports; occupancy; move-ins/move-outs scheduling. This is the mover's own warehouse storage operation as recurring revenue.

## Product B — Supermove (getsupermove.com)

### Key observations (A)

- Positioning: "The Complete Moving Company Software Platform"; "an AI-enabled operating system". Move Types nav: **HHG Moving** and **Commercial Office & Industrial Movers** — both residential-household and commercial poles named by the vendor.
- Solutions: Sales ("book more moves"), Accounting ("automated booking, invoicing, reconciliation"), Operations ("complex dispatch and capacity management into automated workflows… your best people on the best jobs"), Customers (5-star experience), Crews (crew retention and management; crew tips), Reporting.
- Dedicated apps: **Office app, Crew app, Estimator app, Storage app**, Supermove Payments; plus AI call center / voice agents / auto dialer (era machinery).
- Customer-facing promises: protection plans ("Peace of Mind: Offer protection plans, real-time truck tracking"), automated texts, real-time communication.
- Calendar: "View your bookings and open capacity in a single calendar view" (bookings + capacity, same shape as SmartMoving's resource calendar).
- Limitation: SPA — deep pages return identical home content; help center timed out. All claims above from the single official home surface.

## Product C — Elromco (elromco.com)

### Key observations (A)

- Positioning: "All-in-One cloud-based moving company software platform… combines a moving company CRM, dispatch, instant online quoting, electronic bill of lading (eBOL), invoicing, payroll… into a single system — replacing the 5+ disconnected tools most movers currently use."
- Dashboard mock: leads with **statuses** (New / Follow Up / Can Book / Reserved / Booked / Expired), today's moves, revenue estimates, referral sources, sales performance; unassigned / postponed / cancelled counters; **service types**: Local Move, Loading Help, Unloading Help, Interstate Move; leads carry **origin → destination** (e.g., "Boston, MA → NYC, NY") and a price.
- Feature list (24 features): Sales CRM (color-coded lead statuses, automated follow-ups); Lead Scoring; **Pricing Engine** ("3 pricing models, seasonal rates, fee types, auto-calculated"); **Long-Distance & Interstate** ("Mileage tariffs, FMCSA-compliant binding estimates, SIT, weight tickets"); **Online Quotes** (three form types: quick estimate, detailed inventory, virtual survey; real-time price calculation); **Client Portal** (white-labeled; customers submit inventory lists, upload photos, update move details — every change **auto-recalculates the quote**); **Online Booking** (review quote → e-sign agreement → pay deposit by card or ACH → lands on dispatch calendar); **Corporate & Affiliate Accounts** (B2B partner portals, lifetime revenue tracking, recurring corporate relocations); **Dispatch** (Gantt chart, drag-and-drop crew assignment, avoid double-booking trucks); **Job Tracker** (staged real-time tracking with timestamps, "from assigned to completed", under/over-estimate comparison, crew arrival / loading start / drive time between stops / unloading finish); **Electronic BOL** (paperless, timestamps & signatures, foreman submits from crew portal, auto-invoice and auto-payroll on submit); **Crew Portal** (foreman tools, shift confirmation, mobile-first); Invoicing (auto-generated when a job completes, online payment links); **Payroll** (calculated from eBOL data / actual hours worked); **Storage** ("full facility management, tenant tracking"); Reports; **Multi-Branch** (all locations one dashboard, leads assigned to nearest branch); Communications; Automation; AI; **Calendar** ("multi-view scheduling for trucks, crews, and jobs"); **Inventory** ("AI-powered photo inventory with auto-detected items and CuFt" — cubic-feet volume measure); Tasks; White-Label.
- Three-step workflow page: 01 Get quotes & book → 02 Manage & dispatch ("your crew has everything they need on their phone — from BOL to inventory to photos… your foreman submits the electronic bill of lading from the crew portal and the paperwork is finished before the truck leaves the driveway") → 03 Grow revenue (auto-invoicing, payroll from actual hours, revenue analytics).
- **Long-distance page** (interstate household goods carrier operations) — the deepest domain evidence in the sample:
  - Pricing: three tariff models — mileage tariff (distance × weight in CWT or cubic feet; "compatible with the standard 400N tariff structure"), regional zone tariff (postal-code lane lookup), line-haul + transportation (accessorials priced separately: origin packout, destination delivery, SIT); example binding estimate showing line-haul, packout, delivery/unload, fuel surcharge, full-value protection, storage-in-transit lines.
  - Regulatory machinery (US): binding and non-binding estimate workflows; the delivery-collection cap rule (110% of estimate at delivery, balance billed later); required customer disclosures (Rights & Responsibilities pamphlet, Ready to Move, dispute settlement); MC and USDOT number capture on documents; FMCSA-required BOL fields (carrier identifiers, shipper and consignee, dates, pickup/delivery windows, declared valuation, services, weights, charges, signature blocks at origin and destination).
  - **Valuation coverage**: Released Value Protection vs Full Value Protection offered at estimate, election captured with signature, "carried through to the BOL and **claims workflow**".
  - Multi-day / multi-stop: multi-pickup and multi-delivery legs each scheduled separately with own arrival window, crew assignment, and BOL line items; multi-day timeline (packout → line-haul → intermediate stops → delivery); driver line-haul tracking with GPS; customer sees sanitized transit status in the portal.
  - **Storage-in-Transit (SIT)**: carrier holds the shipment when the destination isn't ready; SIT is a billable period tracked against the tariff and **transitions to permanent storage rates**; the move switches to delivery-pending status; SIT lives in the same storage module as permanent storage tenants.
  - **Weight-ticket billing**: tare weight (empty truck) and gross weight (loaded) from certified scale tickets photographed and attached to the order; net = gross − tare; pricing recalculated; non-binding adjustments reconciled "light-bill vs heavy-bill" before invoicing; customer-requested reweigh supported.
  - Interstate vs intrastate as "two different regulatory worlds" (separate rate tables, disclosures, licensing fields).
  - Six-stage journey: Quote → Binding estimate → Deposit & booking → Packout & origin services → Line-haul transit (or SIT) → **Delivery & claims window** (claims window opens at delivery).

## Product D — Workiz (workiz.com/industries/) — generic pole control

### Key observations (A)

- Horizontal field-service management platform ("Schedule jobs, dispatch, invoice and get paid all in one place").
- Its industries index lists **Moving** alongside junk removal, cleaning, locksmith, landscaping, etc. — A-level evidence that moving companies are a served segment of generic FSM software.
- No moving-domain objects on the index page (no inventory, no BOL, no storage) — consistent with the generic realization of the same job spine (job → dispatch → invoice).

## Cross-product Comparison

| Structure | SmartMoving | Supermove | Elromco | Workiz (generic) |
|---|---|---|---|---|
| Move job of record (customer × origin→destination × date) | yes (jobs/moves; documents linked to customer account) | yes (bookings on calendar; office app) | yes (orders with origin→destination, move date, service type, staged tracking) | generic job (no two-address relocation semantics observed) |
| Goods-scoped priced offer (survey/inventory → estimate) | yes — inventory-first estimates, rules engine, binding/non-binding/NTE types | yes — Estimator app (depth not documented on reachable page) | yes — quick/detailed-inventory/virtual-survey quote forms; weight/CuFt pricing; binding estimates | generic estimates (no goods survey observed) |
| Crew + truck assignment & recorded execution | yes — drag-drop trucks/crew, resource calendar, progress events (arrived/loading/on the go), materials checklists | yes — dispatch & capacity management, crew app | yes — Gantt dispatch, staged job tracking with timestamps, crew portal | generic scheduling/dispatch |
| Completion document signed by customer | yes — digital bills of lading with e-signatures | protection plans + tracking (BOL not named on reachable page) | yes — eBOL with timestamps & signatures, shipper/consignee signatures | generic job completion (no BOL) |
| Money loop on the job | yes — deposit from portal, payments/discounts permissions, accounting & payments | yes — payments, invoicing, reconciliation | yes — deposit at booking, final invoice on completion, SIT/weight billing | yes — generic invoice/get paid |
| Inventory machinery | room-based lists, customer self-fill, tablet capture | not detailed | photo inventory w/ auto items + CuFt, customer-submitted lists | — |
| Storage (SIT / mover warehouse) | yes — accounts, containers, tags, occupancy, auto-billing | yes — Storage app (naming only) | yes — SIT + permanent storage tenants in one module | — |
| Valuation / liability options | yes — valuation added on estimates | yes — protection plans | yes — released vs full value, carried to BOL & claims | — |
| Crew hours → payroll | yes | yes (crew pay/tips emphasis) | yes — payroll from eBOL data | generic |
| Customer portal | yes | yes (customer experience solutions) | yes — inventory submission, live recalculation, e-sign, deposit, status | — |
| Multi-branch | multi-location case studies | scale-focused messaging | yes — multi-branch dashboard | — |
| Long-distance/regulatory machinery | 400N-style tariff support; estimate types; state regulator approval for digital docs | not on reachable page | full: mileage/zone tariffs, 110%-rule guardrails, disclosures, MC/DOT, weight tickets, reweigh, SIT tariff transitions, claims window | — |
| AI-era additions | automations, ORM | AI voice agents, AI sales copilot, pricing automation | AI on every field, AI photo inventory | AI-assisted replies |

Reading (B): the four-part spine — move job of record + goods-scoped offer + crew/truck execution with signed completion + money loop — is present in all three dedicated products despite three different product philosophies and eras. The moving-domain extras (inventory machinery, BOL-style documents, valuation, storage/SIT, payroll linkage, portals) recur across the dedicated sample and are absent from the generic control.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The operator-side business system of record for a moving company, whose defining core is **four jointly-held structures**:

1. **The move job of record** — a persistent, identified job binding the customer to a relocation from an origin to a destination on service date(s) (local single-day or multi-day long-distance), accumulating quote, assignments, execution records, documents, and charges on one record. *Remove → a CRM/calendar with no move semantics.*
2. **The goods-scoped priced offer** — the estimate is built from a surveyed scope of the customer's goods (rooms, items, size/volume/weight) plus addresses and access conditions, priced under the company's pricing rules; the offer precedes and anchors the move, and its acceptance (signature, deposit) creates the booked job. *Remove → dispatch with flat catalog pricing — generic field service, or a calculator.*
3. **Crew-and-truck execution recorded on the job** — the office assigns crews and trucks (respecting capacity/availability), and execution is recorded against the job at pickup and delivery: progress events, times, materials, extra services, and a customer-signed completion/delivery document. *Remove → a sales/quoting tool with no operations.*
4. **The job's money loop** — a deposit to book, charges accumulated on the job (labor, materials, extras, storage), and the balance resolved into payment/invoice on completion or delivery. *Remove → an operations shell that never closes the business.*

Jointly-held is load-bearing: (1) alone = lead CRM; (2) without (1) = pricing calculator; (3) without (1)+(2) = generic dispatch board; (4) without (1) = invoicing tool; (1)+(2) without (3) = quote-follow-up CRM, not operations; (2)+(3) without (1) = disconnected ops; (1)+(3) without (2) = the generic-FSM pole (below), which loses the move's economics.

Historical check (§24 conceptual): a paper-era mover — estimate written from an in-home survey, move order/bill-of-lading book, household-goods inventory sheets with item tags, crew/truck assignment board, certified-scale weight tickets for long-distance hauls, payment collected on delivery, vault tags for storage-in-transit, damage noted at delivery feeding claims correspondence — satisfies all four legs at analog level. The definition names no tariff regime, no US federal rules, no cloud, no AI, no instant-online quoting: older, regional, and platform-native realizations all fit.

### L1 — Common Mature Structure (dedicated products)

- Itemized inventory machinery: room-based lists, item catalogs, photo inventory, size/volume measures (CuFt-class), customer-submitted or customer-self-filled inventories, virtual/video surveys.
- Quote/survey capture forms (quick, detailed-inventory, virtual survey) and rules-based pricing engines (crew/truck requirements derived from goods size; access handicaps such as stairs/elevators; capacity per hour; seasonal/day-of-week rates; fee types).
- Customer portal: e-signatures on estimates/documents, deposit payment, status visibility, self-service inventory.
- Dispatch/scheduling board: resource calendar of crews and trucks, capacity vs demand, drag-and-drop assignment, overbooking avoidance, multi-day support.
- Staged job tracking with timestamps and estimate-vs-actual comparison (arrival, loading, transit, unloading).
- Crew mobile app: assignments, job details, materials checklists, progress events, ETA notifications, on-site payments/discounts under permissions.
- Digital move-day documents with customer signatures — bill-of-lading class completion/delivery documents.
- Crew-hours capture flowing to billing and payroll.
- Storage-in-transit and mover-run storage accounts (containers/vaults, occupancy, recurring storage billing, move-in/move-out).
- Valuation/liability coverage options presented at estimate and carried on documents.
- Automated customer communications (confirmations, reminders, transit updates); review/reputation tooling.
- Reporting: revenue by service type/referral source/rep, estimate accuracy, profitability.

### L2 — Variant / Optional Structure

- Pricing model by market/scale: local hourly (crew-hour) pricing vs long-distance weight/volume tariff pricing vs flat/zone rates; several models coexisting per product.
- Regulatory-context machinery for household-goods carriage (the researched sample is US-centric): binding/non-binding estimate types with delivery-time collection caps, mandated disclosures, carrier identifiers printed on documents, regulated BOL fields, certified weight tickets and reweigh rights, defined claims windows. US-interstate in the sample; treated as market machinery, not definition.
- Commercial/office & industrial moving: B2B corporate accounts, partner/affiliate portals, recurring corporate relocations.
- Mover + storage businesses (permanent storage tenants beside SIT).
- Multi-branch operations (nearest-branch lead assignment, consolidated reporting).
- Self-serve instant online quoting on the mover's own website vs office-built estimates.
- AI-era additions: AI voice agents/after-hours booking, AI-assisted estimating, AI photo inventory, automated data entry.
- Attached growth surfaces: mover websites/white-labeling, reputation management.
- Intrastate/state-level and non-US regulatory variants (inferred, not sampled — see Uncertainties).

### L3 — Vendor-specific (Research Notes only)

- SmartMoving: "SM-100 Managed Tariff" (400N-style), LiveSwitch virtual-survey integration, NC Utilities Commission approval for digital documents, ORM module.
- Elromco: "9-stage" job tracker, "14 color-coded statuses", "16 fee types", "AI on every field", 12 fuel-surcharge calculation methods, instant-online-quote widget as the differentiator.
- Supermove: AI Voice Agents / "Autopilot" branding, crew-tip amplification claims, AI call center.

## Vendor-specific Findings → rejected from canonical core

- "Moving software = a CRM" (SmartMoving's own label) — CRM is the sales layer over the move job; the job record, execution, and money loop are the substance.
- "Instant online quotes" (Elromco differentiator) — quoting machinery is common; instant self-serve quoting is one sales-motion variant.
- AI-enabling ("AI-enabled operating system", "AI on every field") — era machinery.
- Any numeric claim (9 stages, 14 statuses, 16 fee types, 12 fuel methods) — vendor-specific counts.
- Tariff structures (400N, SM-100) — market/regulatory machinery, US interstate; not definitional.

## Boundary Findings

- **vs Junk Removal / Waste Hauling Management** (§29, processed): same truck-and-crew shape; the junk pass already records the seam from its side. Removal test: remove the two-point origin→destination carriage of the customer's own goods and the two-ended (pickup + delivery) obligation → the hauling Type remains (cargo leaves the site toward disposal; load/volume/disposal pricing). Conversely, hauling's disposal/scale/volume-load semantics are absent here. Distinctive here: goods-scoped estimates, inventory/condition records, valuation, SIT, deposits + payment-on-delivery.
- **vs Small Business Field Service Management** (§29): shared family spine (job → dispatch → complete → invoice); Workiz evidence shows movers served by horizontal FSM. Removal test: remove the moving-domain objects (two-address move job, goods-surveyed estimates, BOL-class completion documents, deposit/delivery payment rhythm, SIT) → generic FSM remains. The generic pole is held as a **variant realization** of this Type, not a separate market (precedent: junk-removal pass).
- **vs Trucking Management System** (§18): freight carriage of shipper/consignee goods under load/tender machinery vs household/commercial relocation sold directly to the moving customer; the mover's system centers estimate/inventory/signed-delivery documents and crew economics, not carrier operations. (Structural reasoning; TMS pass not jointly reviewed.)
- **vs Courier Management / Last-mile Delivery Platform** (§18): parcels to recipients vs household-scale loads moved by crews between customer residences/businesses with quotes, inventory, and storage semantics.
- **vs Towing Dispatch Platform** (§18): vehicle recovery dispatch; no relocation job economics (quotes, deposits, delivery completion).
- **vs Dispatch Management / Route Optimization / Driver Management / Fleet Management System** (§18): capabilities that appear inside this Type (assignment boards, capacity, GPS tracking) but are not business systems of record — no customer, quote, document, or billing objects at the center.
- **vs Self-storage Management** (§29): the mover's storage module serves *moving* customers (SIT, vaulted household goods) while self-storage management operates a rental facility (units, gate access, retail tenants); some overlap in account/occupancy/billing shapes, different center of gravity. Movers that run storage businesses use both shapes in one product.
- **vs Home Services Marketplace / Local Service Marketplace** (§29): demand-side venues vs the mover's internal system of record.
- **vs Appointment-based Service Business Management** (§29, processed): quote-first scoped jobs with crews and goods (not catalog appointments delivered to a visiting client).

Taxonomy note: no alias/variant/duplicate problem found. The leaf earns independent Type status; the generic-FSM realization is held as a variant per family precedent. No directory change proposed.

## Uncertainties

- **Claims/damage handling depth**: Elromco documents a claims window and valuation-to-claims linkage; Supermove mentions protection plans; SmartMoving's researched pages do not document a claims module. Claims machinery is therefore held at L1-with-qualified-evidence (common but unevenly documented), not core.
- **Legacy/desktop generation**: MoveitPro unreachable (403 ×2); the historical check is paper-era conceptual, not vendor-documented for the desktop generation. Generation-breadth claim avoided.
- **Non-US markets**: all sampled vendors are US-market movers; the definition deliberately abstracts away US regulatory specifics, but regional variant claims (UK/EU movers) are inference, not observation.
- **Supermove depth**: SPA site — estimator/storage app details beyond naming not observable; claims about Supermove kept at naming level.
- **Screen-level workflows**: help centers largely unreachable; workflow descriptions remain conceptual (no click-paths, no exact status names asserted in the final document).

## Final Synthesis

A Moving Company Management application is the moving company's job-based business system of record. Its world is organized around the **move job** — one persistent record binding a customer to a goods-scoped, priced relocation from origin to destination — with four jointly-held structures: the job of record, the goods-scoped priced offer (survey/inventory → estimate → signed acceptance + deposit), crew-and-truck execution recorded on the job (assignment, progress events, materials, signed delivery/completion documents), and the job's money loop (deposit → accumulated charges → payment/invoice at delivery). Around this core, mature dedicated products add the trade's machinery: itemized inventory with volume/weight measures, rules-based pricing engines, capacity-aware dispatch boards, staged tracking with timestamps, crew apps feeding payroll, digital bills of lading, customer portals, storage-in-transit, and liability-coverage options. US interstate regulatory machinery, AI-era automation, commercial/B2B postures, and multi-branch operations are variants. The Type sits between generic field service (which shares the spine and serves movers generically) and freight/trucking software (which shares trucks but not the moving customer's estimate-inventory-delivery economy); the two-point origin→destination carriage of customer goods is the crisp discriminator against the junk-hauling sibling.
