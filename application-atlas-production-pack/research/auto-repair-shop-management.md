# Research Notes — Auto Repair Shop Management

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what "Auto Repair Shop Management" is as an Application Type: the business-management software used by automotive repair shops (independent garages, tire shops, quick lube, heavy-duty truck shops). Identify the core objects (customer, vehicle, repair order, labor, parts, invoice), the repair-order lifecycle, who operates the system and from which surfaces, which structures are automotive-specific (vehicle as a record, odometer, labor guides, parts matrices, cores, DVI inspections, warranty payment types), and where the boundary lies against Collision Repair Management, Appliance Repair Management, Fleet Management System, Vehicle Inspection/Diagnostic Applications, Car Wash/Detailing Management, and appointment scheduling.

This leaf carries a **flagged joint review** with `appliance-repair-management` (field-based vs shop-based repair management; flagged when that leaf was processed — see STATUS.md Boundary Issues).

## Initial Boundary

Initial hypothesis (before research):

- Core use: shop-side operations software for businesses that repair vehicles at a fixed location — customers bring (or send) vehicles in; the shop writes up a repair order, inspects, estimates, gets authorization, orders parts, assigns technicians, performs and documents work, invoices, collects payment.
- Primary users: service advisor / service writer (front counter), technician (bays), parts/inventory staff, owner/manager.
- Nearest types: Collision Repair Management (body-shop sibling), Appliance Repair Management (field-based repair sibling), Fleet Management System (§18, manages vehicles owned by the operator, not a repair business), Vehicle Inspection / Diagnostic Application (§29 fragment), Car Wash / Detailing Management (§29 sibling), Appointment Scheduling Application (§03.09 fragment), Small Business FSM (§29 generic sibling).
- Expected distinguishing structures vs appliance repair: the vehicle should be a first-class structured record (VIN, make/model/year, plate, odometer) with per-vehicle service history — the appliance, by contrast, was found to be job content in that leaf; labor sold by book time; parts inventory central; work executed in shop bays with tech clock-in rather than field dispatch.
- Unknowns: exact RO lifecycle state vocabulary per product; whether estimate→RO→invoice are separate documents or one record re-labeled; how warranty vs customer-pay work is attributed; how deep pricing controls (labor rates, parts matrices) go; whether fleet accounts are structural.

## Research Questions

1. What objects constitute the system (customer, vehicle, repair order, parts, invoice) and how do they relate?
2. Is the vehicle a first-class structured record with per-vehicle history, or job content?
3. What is the repair-order lifecycle, and are estimate / repair order / invoice distinct document states?
4. How do estimates and customer authorization work (per-line approval, declined work, e-signatures)?
5. How does labor pricing work (labor operations, flat-rate/book times, labor rates, tech efficiency)?
6. How are parts modeled (inventory, supplier catalogs, purchase orders, cores, returns, price levels)?
7. What do digital vehicle inspections do and how do they feed authorization?
8. How do appointments/drop-off and the shop workflow board work?
9. What does the technician surface do (assignment, clock-in, WIP communication, photos)?
10. What roles/permissions exist, and how is customer-pay vs warranty vs internal work attributed?
11. What money mechanics exist (deposits, payment types, statements, accounting sync)?
12. Where are the boundaries against collision repair, fleet management, and field-service repair types?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Tekmetric | Cloud-native; SMB through multi-location groups; growth/ARO- and inspection-driven | Best accessible Tier-1 help center with full service-writer and technician RO workflow documentation |
| Shopmonkey | Cloud-native; SMB; all-in-one simplicity; serves auto repair, tire, quick lube, heavy duty, detail | Full Tier-1 help center; exposes the order-type model (estimate/RO/invoice) and workflow views explicitly |
| R.O. Writer | Legacy incumbent (~50 years, thousands of shops), now cloud; parts-catalog- and pricing-centric | Established-market counterweight; documents supplier-catalog integration, matrix pricing, cores, price levels |
| Shop-Ware | Professional/mid-market; workflow- and analytics-driven; multi-shop (MSO) focus | Confirms the pattern from a fourth independent vendor incl. capacity management and fleet module |

Market anchors not researchable in this environment (recorded as limitation): Mitchell 1 Manager SE (mitchell1.com unreachable, 2 attempts), AutoLeap / MaxxTraxx / Shop Boss (not attempted after sufficient sample reached). Their exclusion reduces sample breadth, not the validity of the observed core.

## Sources

### Tekmetric (official help center — Tier 1; official product pages — Tier 2)

- Help center root: https://support.tekmetric.com/hc/en-us (categories: Getting Started, Training & Education, Reporting, Integrations, Video Library; "Topics By Role": Operations & Owners / Service Advisors / Technicians)
- Repair Order Workflow Overview for Service Writers (full article): https://support.tekmetric.com/hc/en-us/articles/360043239813 — write-up → DVI → ordering parts → performing work → checkout; odometer-on-RO recommendation and warranty/mileage rationale
- Repair Order Workflow for Technicians (full article): https://support.tekmetric.com/hc/en-us/articles/360047413853 — tech assignment, tech board, clock-in, efficiency (billed vs clocked labor), warranty traceability to tech, WIP tab
- Referenced article titles (inventories/links only, not fetched): Repair Order Navigation, Basic Job Board Navigation, View Customer History, Tech Board, Core Tracking Returns and Reports, Unpost Repair Order, How to Transfer Repair Orders, Creating & Editing Inspections, Internal Tekmetric Notifications, warranty-work reporting
- Product pages (Tier 2): https://tekmetric.com/feature/shop-management (Smart Jobs, estimates flow into ROs, labor and parts matrices, role-based permissions), /feature/digital-vehicle-inspection (DVI mobile app, photos/videos/markups, custom multi-point inspections, canned jobs mapped to inspection tasks, declined-work follow-up, DVI reporting), /feature/inventory (part/BIN search, min stocking levels, restocking suggestions, usage/dead-stock stats, return to inventory, PartsTech/Nexpart supplier ordering, multi-location part search), / (payments: text-to-pay/BNPL; online booking; two-way texting; multi-shop; tire suite)
- Customer story reference (vendor claim): Metro Motor — 19 shops, average repair order $800

### Shopmonkey (official help center — Tier 1; official product pages — Tier 2)

- Help center root: https://support.shopmonkey.io/hc/en-us (categories: Getting Started, Features, Reports, Shop Settings, Payments, Accounting, CRM Essentials, Shopmonkey HQ, Integrations, Mobile App for Techs, Academy)
- Features category (article inventory): https://support.shopmonkey.io/hc/en-us/categories/38367529632532 — Estimates and Invoices (28 articles), Customers (Add Customers / Add Fleets / Add Vehicles), Inspections (templates, perform, quick notes, customer e-signatures, send to customers), Calendar (appointments, confirmations/reminders, recurring), Inventory (manage, Parts & Tires Workflow, purchase orders, reserve parts), Payments on Orders (deposits, refunds, statements, bulk payments, coupons), Time Clocks, Best Practices (extended warranty contract claims)
- Workflow Views (full article): https://support.shopmonkey.io/hc/en-us/articles/38743858598676 — Columns (Estimates, Dropped Off, In Progress, Invoices), column settings: Convert to Repair Order / Convert to Invoice, auto-archive paid/inactive; List view; Parts & Tires view
- Convert Estimates to Invoices (full article): https://support.shopmonkey.io/hc/en-us/articles/38743626549780 — convert action, unpaid notice, auto-convert fully paid orders, order-checklist gating; related articles: Canned Service, Recommend Services on an Estimate, Deferred Services
- Product pages (Tier 2): https://www.shopmonkey.io/ — auto repair POS framing, DVI upsell/ARO, estimates/invoices/payments, native accounting, CRM Essentials; shop types: auto repair, tire, quick lube, heavy duty, wrap & detail; multi-shop (HQ)

### R.O. Writer (official product pages — Tier 2)

- Root: https://www.rowriter.com/ — "Trusted by thousands of auto shops for 50 years and now cloud-based"; DVI Suite; Smart eCat; Connect; Accounting Link
- Features page (full): https://www.rowriter.com/features/ — service writing (supplier catalogs, flat rate guides, repair guides ALLDATA/Identifix/Motologic launched from the RO with vehicle preselected, CARFAX QuickVIN from license plate, margin warnings), Smart eCat (up to 10 suppliers on one screen, order from within), Smart eJobs (parts + flat-rate labor times per job), Smart eOrder, Smart Scan (oil-sticker barcode → oil-change RO), Smart Oil/Smart Fluids (vehicle-specific), inventory (up to 5 price levels per part, core tracking purchase → core credit return, multi-store transfers), Smart Matrix Pricing (parts and labor margins, multiple matrices), DVI with pictures/videos, reporting by date/profit center/service writer, AR statements + interest on past-due accounts, built-in AP/AR, QuickBooks, multi-store RO history (2–100 stores)

### Shop-Ware (official product pages — Tier 2)

- Root: https://shop-ware.com/ — digital workflow per RO (job status + vehicle information), estimating with real-time photos/videos/chat, TechApp, DVX (Digital Vehicle Experience), Messenger, integrated payments, AI Parts Matrix, parts inventory + native parts catalog, capacity management, fleet management, marketing CRM, online service scheduler, AI receptionist, business analytics, multishop (MSO); owned by Vehlo; support portal https://support.shop-ware.com/s/ (not fetched)

### Blocked sources (limitation record)

- Mitchell 1 (Manager SE — major legacy incumbent): https://www.mitchell1.com/products/manager-se/ and https://www.mitchell1.com/ → transport errors (2 attempts; abandoned)
- Tekmetric help-center article "Core Tracking, Returns, and Reports" (https://support.tekmetric.com/hc/en-us/articles/360039834833) → 403 on fetch; existence and title confirmed from the linked-article inventory only
- Shopmonkey help center root: first fetch attempt transport-errored; retry succeeded (no further limitation)

---

## Product A — Tekmetric

### Key observations (evidence layer A — directly observed)

- **Object model**: Customer + Vehicle + Repair Order + Inspections + Estimates + Parts/Inventory + Invoices + Payments; nav surfaces: Job Board, Tech Board, Reporting; role-based permissions confirmed in FAQ ("Permission levels are the easiest way to control access").
- **Canonical RO workflow (service-writer view, vendor's own training structure)**: **Writing Up the Customer → Performing the Digital Vehicle Inspection → Ordering Parts for Approved Work → Performing Work on the Vehicle → Checking Out the Customer**. Estimates flow directly into ROs ("no duplicate entry"). Two workflow PDF variants exist: with and without a diagnostic step.
- **Odometer as RO data**: vendor recommends requiring odometer entry on every RO — it appears on the customer's invoice, supports "when and at what mileage was this done" lookups, **is required to track warranty parts and their failures**, and drives mileage-based service recommendations/reminders.
- **Technician execution model**: tech assignment on ROs is highly valuable — managers see each technician's workload on the **Tech Board** and dispatch work; technicians see what to prioritize; **techs clock into jobs**; **efficiency = clocked time vs billed labor** (vendor's illustrative example: diagnostic tech ~80–100%, strong R&R tech ≥120%, junior ~50–60% — vendor illustration, not a canonical norm); assignment history supports warranty-work traceability to the performing technician; **WIP (work-in-progress) tab carries tech↔shop communication** on the RO.
- **Order state machinery**: articles exist for Unpost Repair Order (i.e., a posted/finalized RO can be reverted) and How to Transfer Repair Orders (reassign between techs).
- **DVI (digital vehicle inspection)**: performed on mobile; photos, videos, markups, findings; **custom multi-point inspection templates per work type; canned jobs mapped to inspection tasks auto-added to ROs**; past inspections viewable as vehicle history; inspection reports sent to customer by text/email; **declined estimate lines are saved so advisors can follow up and build repair plans**; DVI performance benchmarked per technician; customer engagement with inspection reports tracked.
- **Parts/inventory**: search by part number/brand/name/BIN; **minimum stocking levels + restocking suggestions**; usage statistics ("last used", "units used in last 30 days", "units per month", "jobs per month") exposing dead stock; **return parts to inventory**; integrated supplier ordering (PartsTech, Nexpart) with price/ETA comparison; **multi-location part search**; jobs source parts from inventory ("swap a similar part or order through integrated suppliers"); Core Tracking article exists (cores as tracked objects).
- **Pricing**: "Labor and parts matrices keep pricing consistent and margins protected"; parts ordering + inventory "prevent shortages".
- **Money**: Tekmetric Payments — invoicing, text-to-pay, buy-now-pay-later, capital financing; checkout surfaces; reporting tracks revenue/productivity; warranty-work reporting supported.
- **Customer communication**: two-way texting, automated reminders, scheduled campaigns, online booking, Google reviews; website product.
- **Multi-shop**: multi-location management; tire suite as a product line; "15,000+ shops" vendor claim.

## Product B — Shopmonkey

### Key observations (evidence layer A — directly observed)

- **Order-type model (explicit)**: orders exist as **Estimates → Repair Orders → Invoices**; the workflow page is organized by order status columns (e.g., **Estimates, Dropped Off, In Progress, Invoices**); columns are customizable (add/rename/reorder/hide); **column settings include "Convert to Repair Order" and "Convert to Invoice" when an order is dropped into the column**, "Archive Paid Orders", "Archive When Inactive (N days)" — i.e., document-type conversion is a workflow action.
- **Conversion rules**: manual "Convert to Invoice" on an estimate; **auto-convert fully paid orders to invoices** (shop setting), including payments taken from the workflow page, customer page, or the public payment link; **Order Checklists can gate conversion** (banner prompts conversion until required checklist items complete; optional-only checklists auto-complete).
- **Customers**: Add Customers, **Add Fleets** (fleet as a customer type), **Add Vehicles** (vehicle as its own object under the customer); customer info/preferences; Message Center.
- **Inspections**: inspection templates, performing inspections, quick notes, **customer e-signatures on inspections**, sending inspections to customers.
- **Calendar**: schedule appointments, confirmation & reminders, recurring appointments, calendar settings/filters.
- **Inventory**: manage inventory; **Parts & Tires Workflow view — the workflow can be viewed by part status with the corresponding work order**; purchase orders; **reserve parts**; order line items can be added back into inventory.
- **Payments**: record a deposit on a work order; edit/refund posted payments; refund a line item; create statements; record bulk payments; coupons.
- **Labor/time**: Track Hours with Time Clocks; Shopmonkey for Techs mobile app category.
- **Service catalog**: **Canned Services** (predefined services), Recommend Services on an Estimate (recommended vs requested work), **Deferred Services** (work proposed now, deferred to a later visit), Service Level Categories.
- **Warranty**: best-practice article for extended warranty contract claims; warranty payments implied by payment-type handling.
- **Ecosystem**: native accounting ledger (Shopmonkey Accounting) or QuickBooks; CRM Essentials (marketing/reviews); Shopmonkey HQ (multi-location); Heavy Duty edition (truck repair, multiple fleets, batch payments); shop types incl. quick lube and detail shops.

## Product C — R.O. Writer

### Key observations (evidence layer A for feature facts; marketing-depth source)

- **Positioning**: legacy incumbent — "trusted by thousands of auto shops for 50 years and now cloud-based"; customers incl. franchise chains (Midas/IMDA).
- **Service writing**: integrated parts supplier catalogs; **flat rate guides**; repair-guide integrations (ALLDATA, Identifix, Motologic) that **launch from the repair order with the vehicle preselected**; **CARFAX QuickVIN — retrieve VIN from the license plate number**; margin-warning indicators on low-margin parts and labor; "create repair orders in fewer clicks".
- **Parts sourcing**: Smart eCat — **pricing and availability from up to 10 suppliers on one screen, order from within**; catalog integrations list: ACDelco, AutoZone, Epicor, Federated, IMC, Motorcraft eCounter, MyPlace4Parts, NAPA PROLink, OEConnect RepairLink, PartsTech, Transtar Transend, WHI Nexpart, WORLDPAC SpeedDIAL; Smart eOrder one-click ordering; **parts post to the RO with a click, no rekeying**.
- **Job composition**: **Smart eJobs — design a job containing all parts and labor needed, walking through steps with parts from suppliers and flat-rate labor times**; Smart Scan scans the oil-sticker barcode to auto-create the oil-change RO incl. correct oil/filter; Smart Oil selects viscosity/capacity per vehicle and adjusts price for additional oil; Smart Fluids for flush jobs.
- **Inventory**: built-in pricing tools with **up to 5 price levels per part**; **core tracking from part purchase to core credit return**; multi-store part transfers; automatic purchase orders and live stock tracking.
- **Pricing**: **Smart Matrix Pricing for parts AND labor margins**; multiple matrices by supplier, part type, or job.
- **DVI**: replace paper inspections with tablets/smartphones; send inspection reports with pictures and videos; DVI Suite SmartStatus for shop-flow management.
- **Money/accounting**: built-in AP/AR; AR statements to customers; **interest automatically applied to past-due accounts**; QuickBooks integration (Accounting Link).
- **Reporting**: sales, inventory, time tracking, marketing, payables, receivables; by date range, **profit center, or service writer**; drill-down.
- **Multi-store**: 2–100 stores; **vehicle repair-order history visible at each store regardless of which store repaired the vehicle**; enterprise real-time reporting; labor rates/job-cost setting.
- **Customer communication**: two-way texting/email included; customer & vehicle history pull-up; follow-ups/reminders; Connect add-on (marketing automation + AI).

## Product D — Shop-Ware

### Key observations (evidence layer A for module inventory; marketing-depth source)

- **Digital workflow**: workflow surface showing **job status and vehicle information** per RO; "keeps communication about every RO flowing"; goal framing "from check-in to check-out".
- **Team management**: Employee Management; **TechApp — technicians add their findings** via a purpose-built app; AutoWrite (AI-assisted write-up).
- **Parts**: Parts Inventory; **Native Parts Catalog**; **AI Parts Matrix — "hit your parts pricing targets every time"** (matrix pricing as a first-class tool).
- **Estimates**: prepare and share quotes in seconds; real-time photos, videos, and chat; **work approval rate 89% (vendor claim)**.
- **Customer experience**: DVX — "immersive, interactive eCommerce Digital Vehicle Experience" for approvals; Messenger (live chat to speed approvals); Integrated Payments; Online Service Scheduler; AI Receptionist; Marketing CRM.
- **Business management**: Business Analytics; **Capacity Management** (shop capacity as a managed object); **Fleet Management module**; Multishop (MSO) with advanced analytics.
- **Integrations**: MOTOR, QuickBooks, Back Office, CARFAX, PartsTech (logos on site).

---

## Cross-product Comparison

| Structure | Tekmetric | Shopmonkey | R.O. Writer | Shop-Ware | Assessment |
|---|---|---|---|---|---|
| Customer records | Yes | Yes (+ Fleets) | Yes | Yes | Core (4/4) |
| **Vehicle as first-class record** (per-vehicle history, VIN/plate/odometer) | Yes (odometer per RO; warranty parts need odometer; mileage-based reminders; VIN/plate scan in app) | Yes (Add Vehicles object) | Yes (vehicle history; QuickVIN from plate; vehicle-preselected guides) | Yes (vehicle info on workflow) | **Core (4/4) — defining vs appliance-repair type** |
| Repair order as unit of work with lifecycle | Yes (write-up → parts → work → checkout; transfer/unpost machinery) | Yes (Estimate → RO → Invoice order types; workflow columns) | Yes (RO screen is the hub; multi-store RO history) | Yes (workflow per RO) | Core (4/4) |
| Estimates + customer authorization | Yes (estimates flow into ROs; declined work saved for follow-up) | Yes (send estimates; e-signatures on inspections; checklist gates) | Yes (easy-to-understand estimates; margin warnings) | Yes (fast quotes; 89% approval claim; DVX) | Core (4/4) |
| Labor + parts line composition on the RO | Yes (labor and parts matrices) | Yes (canned services, recommend/deferred services) | Yes (flat-rate guides; Smart eJobs parts+labor) | Yes (estimating + parts matrix) | Core (4/4) |
| In-shop execution: advisor ↔ technician coordination | Yes (tech board, dispatch, WIP tab, clock-in, efficiency) | Yes (workflow columns incl. Dropped Off; techs app; time clocks) | Yes (service writing + techs notes; time tracking reports) | Yes (TechApp; digital workflow) | Core (4/4) |
| Billing: invoice from RO → payment | Yes (invoicing, text-to-pay, BNPL) | Yes (auto-convert paid; deposits; statements; bulk payments) | Yes (built-in AP/AR; statements; interest on past-due) | Yes (integrated payments) | Core (4/4) |
| Appointments/calendar + reminders | Yes (online booking, reminders) | Yes (calendar, recurring, reminders) | Yes (scheduling; follow-ups/reminders) | Yes (online service scheduler) | Common (4/4) |
| Digital vehicle inspections (DVI) | Yes (mobile, photos/videos, templates, canned-job mapping, DVI reporting) | Yes (templates, e-signatures, send to customers) | Yes (DVI Suite; SmartStatus) | Yes (TechApp findings + DVX) | Common (4/4) — signature capability of the Type |
| Workflow/job board by RO status | Yes (Job Board) | Yes (Columns/List; customizable; archive rules) | Yes (track progress, monitor ROs) | Yes (digital workflow) | Common (4/4) |
| Technician clock-in / efficiency reporting | Yes (billed vs clocked labor; per-tech benchmarking) | Yes (time clocks; track hours) | Yes (time tracking reports) | Yes (analytics) | Common (4/4) |
| Parts inventory + supplier catalogs + POs | Yes (BIN search, min stock, restock suggestions, dead stock, PartsTech/Nexpart) | Yes (inventory, POs, reserve parts, Parts & Tires view) | Yes (14 catalogs, eCat multi-supplier compare, 5 price levels) | Yes (inventory + native catalog) | Common (4/4) |
| Parts cores / returns | Yes (Core Tracking article title; return parts to inventory) | Yes (add line items back to inventory; refunds) | Yes (core tracking purchase → credit return) | — (not observed) | Common-ish; evidence depth varies |
| Pricing controls (labor rates, parts matrices/price levels) | Yes (labor and parts matrices) | — (not directly observed at matrix depth) | Yes (Smart Matrix Pricing; 5 price levels; margin warnings) | Yes (AI Parts Matrix) | Common (3/4); depth varies |
| Vehicle odometer capture per visit | Yes (explicit recommendation/requirement) | — (not directly observed) | — (implied by vehicle history/oil-sticker scan) | — (not observed) | Common in segment; not universal in evidence |
| Customer-pay vs warranty vs internal attribution | Yes (warranty-work reporting; warranty parts tracking) | Yes (extended warranty contract claims best practice) | — (not directly observed) | — (not observed) | Common; warranty handling mature in evidence |
| Declined-work tracking / repair plans | Yes (explicit) | Partial (Recommend/Deferred Services) | — (not directly observed) | — (implied by approval workflows) | Common; strongest in modern cloud products |
| Accounting sync / back office | — (integrations exist; not directly observed) | Yes (QuickBooks; native accounting) | Yes (built-in AP/AR; QuickBooks) | Yes (QuickBooks, Back Office) | Common (all) |
| Fleet accounts / fleet module | — (not directly observed) | Yes (Add Fleets; Heavy Duty batch payments) | — (not observed) | Yes (Fleet Management module) | Optional/variant |
| Tire-specific tooling | Yes (Tire Suite) | Yes (tire inventory/brands/models) | — (not observed) | — | Optional/variant |
| Multi-location (group/MSO) | Yes (multi-shop; 19-shop story) | Yes (Shopmonkey HQ; 75-location onboarding claim) | Yes (2–100 stores; cross-store history) | Yes (MSO solutions) | Optional/variant (scale-dependent) |
| Marketing / reviews / reputation | Yes (campaigns, Google reviews, websites) | Yes (CRM Essentials) | Yes (Connect add-on) | Yes (Marketing CRM, AI receptionist) | Optional |
| Consumer financing / BNPL | Yes (BNPL, capital financing) | Yes (BNPL) | — | — (payments only observed) | Optional |
| Shop capacity management | — (not observed) | — (not observed) | — (not observed) | Yes (Capacity Management) | Product-specific in sample |
| Native accounting ledger inside the product | — | Yes (Shopmonkey Accounting) | Partial (built-in AP/AR + link) | — | Optional/product-specific |

### Key finding — the vehicle is a first-class structured record (unlike the appliance-repair sibling)

Across all four products the vehicle is a named object with per-vehicle service history (and commonly VIN, plate, make/model/year, odometer). Tekmetric ties odometer to warranty-parts tracking and mileage-based services; R.O. Writer keys repair guides and fluid selection to the vehicle and makes cross-store RO history vehicle-indexed; Shopmonkey exposes Add Vehicles as a peer of Add Customers. This contrasts with the appliance-repair leaf, where the repaired appliance was captured as job content in the whole sampled market. Canonical statement: in auto repair shop management, the RO binds customer × **vehicle**, and vehicle history is the shop's institutional memory.

### Key finding — the RO lifecycle has explicit document-type transitions

Shopmonkey makes the pattern explicit: Estimate → Repair Order → Invoice are order types with conversion actions (manual, column-drop-triggered, or auto after full payment), gated by optional checklists. Tekmetric's service-writer flow (write-up → inspect → order parts for approved work → perform → check out) plus its "estimates flow directly into ROs" and Unpost machinery imply the same three-stage document progression. R.O. Writer's RO screen with posted/unposted semantics and Shop-Ware's workflow corroborate. Canonical lifecycle: **written up → estimated → authorized → (parts) → worked → completed → invoiced/posted → paid**, with unpost/transfer as guarded state changes.

### Key finding — labor is sold by book time and measured against clock time

R.O. Writer integrates flat-rate guides; Smart eJobs composes parts + flat-rate labor times; Smart Matrix Pricing covers labor margins. Tekmetric computes technician efficiency as clocked vs billed labor and benchmarks technicians; Shopmonkey ships time clocks; Shop-Ware ships analytics. Book-time labor + clock-time measurement is a mature, cross-product structure — the pricing mechanism (matrix vs list vs manual) varies.

### Key finding — parts are managed stock with supply-chain integration

Every product has parts inventory with supplier-catalog ordering (14 named catalogs at R.O. Writer; PartsTech/Nexpart at Tekmetric; native catalog at Shop-Ware; POs and reservations at Shopmonkey). Cores (returnable core credit) and returns are evidenced at three products. Inventory depth is far beyond the "materials as line items" level seen in appliance repair.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being an auto repair shop management application:

```text
Customer
└── Vehicle — an identified, structured record of the vehicle being serviced
    │   (identity + per-vehicle service history)
    └── Repair order — the unit of work binding customer × vehicle × requested service,
        │   carried through a shop-executed lifecycle
        │   (written up → estimated → authorized → worked → completed → invoiced → paid)
        └── Labor and parts as the substance of the work (line items on the RO)
        └── Shop-side execution — front-counter staff write up and manage,
            technicians perform and document the work in the shop
```

Four properties:

1. **Vehicle as the object of record** — the repair binds to a structured vehicle record with per-vehicle history; the vehicle (not a location) is what returns to the shop. Remove it → generic invoicing/appointment software.
2. **Repair order as durable unit of work with a lifecycle** — one RO per engagement, surviving from write-up to payment, with guarded state changes. Remove it → a calendar + ledger.
3. **Labor-and-parts composition** — the RO is priced work made of labor (time/rate) and parts (stock/purchased), not a flat service transaction. Remove it → generic POS.
4. **In-shop execution with front/back coordination** — a front-counter role sells and administers; technicians execute and document inside the shop; the system coordinates them. Remove it → a booking or accounting tool.

Billing (invoice → payment) rides on the RO lifecycle; a repair-order system that cannot close the money loop does not manage the shop's business, so it is included in the lifecycle rather than as a fifth independent property.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required to recognize the Type:

- appointments/calendar with confirmations and reminders; online booking
- estimates with per-line customer authorization (approve/decline; e-signature); declined-work retention and follow-up; deferred/recommended services
- digital vehicle inspections (templates, photos/videos, findings, sent to customer)
- workflow/job board organizing ROs by status (columns/boards; "dropped off" state)
- technician assignment + tech board + clock-in per job; efficiency (billed vs actual) reporting
- labor operations / canned services with book times; labor rates
- parts inventory (stock levels, minimums, restocking suggestions, usage stats); supplier catalog integration; purchase orders; reservations; returns; core tracking; price levels/markup matrices
- pricing controls: labor rates, parts matrices/multi-level pricing, margin warnings
- per-vehicle service history; odometer capture; mileage-based service reminders
- invoicing from the RO; deposits; payment collection (counter/online/text); statements
- customer-pay vs warranty vs internal work attribution; warranty traceability
- reporting (sales, technician productivity, inventory usage); accounting integration (in practice QuickBooks in the North American market)
- two-way customer messaging/approvals; role-based permissions

### L2 — Variant / Optional Structure

Depends on segment, scale, business model:

- fleet accounts (companies with vehicle pools; statement/batch billing) and fleet-management modules
- tire-specific suites (tire inventory, fitment); quick-lube speed workflows (sticker-scan ROs)
- heavy-duty/truck shops; multi-shop organizations (MSO) with cross-store history and enterprise reporting
- shop capacity management; courtesy-check-only visits
- marketing automation, reputation/review management, AI receptionists, customer websites
- consumer financing (BNPL, installment), capital financing
- native accounting ledgers vs external accounting sync
- repair-data/diagnostic content integrations (repair guides, VIN decoders, license-plate lookup)

### L3 — Vendor-specific Structure

(Research Notes only)

- Tekmetric: Smart Jobs, Tech Board specifics, "Master Tek" training, Tektonic user conference, Shop Index benchmarking, DVI engagement tracking, 19-shop Metro Motor story, tire suite packaging
- Shopmonkey: Workflow Cards (Standard/Condensed), Parts & Tires workflow view, Order Checklist conversion gating, auto-archive settings, Deferred Services as a named primitive, Shopmonkey HQ, CRM Essentials, native Accounting, Heavy Duty edition, "Norman"-style mascot branding n/a, French/Spanish support lines
- R.O. Writer: Smart eCat/eJobs/eOrder/Scan/Oil/Fluids tool suite, Smart Matrix Pricing naming, DVI Suite SmartStatus, Connect (AI marketing), Constellation ownership, 50-year heritage positioning, 14 named catalog integrations
- Shop-Ware: AutoWrite, TechApp, DVX (Digital Vehicle Experience), AI Parts Matrix, AI Receptionist, Capacity Management packaging, Vehlo ownership, 89% approval-rate claim, "Raise the Standard" positioning

---

## Historical / Market-Sample Check (§24)

Question: would older, regional, or differently positioned shops still fit the L0?

- **Pre-software practice**: the handwritten repair ticket (customer name, vehicle, plate/mileage, complaint, listed parts and labor, technician assignment) + wall scheduling board + parts room tickets + carbon invoice. This satisfies the L0 exactly: the ticket is the RO with a lifecycle; the vehicle line is the vehicle record; parts/labor lines are the composition; the invoice closes the loop. The L0 does not depend on cloud, mobile apps, VIN decoding, or text messaging.
- **Regional**: independent mechanical repair is a global trade; nothing in the L0 is US-specific (no tax rules, no emissions regimes, no payment rails in the core). Labor-book conventions vary by region but "labor sold as priced time" is general.
- **Differently positioned**: a two-bay independent garage running ROs without inspections or matrices satisfies the L0 (DVI and matrices are L1); a quick-lube with 15-minute sticker-scan ROs satisfies it with the RO lifecycle compressed; a fleet-only truck shop satisfies it with fleet accounts as an L2 overlay; a mobile mechanic who travels to the car is drifting toward field service (no fixed shop) — treat as an edge variant, not the center.
- Conclusion: the L0 survives the historical check. Modern implementations (cloud, mobile, DVI, text approvals, catalog integrations) are L1/L2, not definition.

---

## Vendor-specific Findings

See L3. Additional:

- Tekmetric and Shopmonkey both position the product as "all-in-one" with payments inside the platform; payments-as-product is a business-model feature (payment processing revenue), not a structural requirement of the Type.
- R.O. Writer's feature page frames the same core as "service writing + parts + pricing + reporting" — the legacy framing centers the parts catalog and matrix pricing; the modern framing centers inspections and ARO growth. Same spine, different emphasis.
- Shop-Ware is the only sampled product exposing **shop capacity management** and an **AI receptionist** as named modules; both are plausible L2 structures pending broader evidence.
- Vendor ARO/approval claims ($800 ARO, 89% approval) are marketing metrics, not structures; recorded here only as evidence that inspection-driven upsell is a design goal of the category.

## Boundary Findings

1. **vs Appliance Repair Management (§29 sibling — flagged joint review, now completed)**: both are "repair management" business systems sharing customer → job → execution → billing. Structural differences: (a) **execution surface** — appliance repair is field-based (technician travels to the appliance; dispatch/routing central; the job binds to a service location), auto repair is shop-based (vehicle brought to the shop; the job binds to the shop; bay/tech coordination central); (b) **object of repair** — the appliance is job content in the appliance-repair sample, while the vehicle is a first-class structured record with per-vehicle history in all four sampled products here; (c) **work economics** — auto repair has book-time labor, parts matrices, cores, warranty payment types; appliance repair has flat-rate service-call economics. Verdict: **related Types sharing a repair pattern, not duplicates and not a trade-variant pair** — the execution surface and object-of-record differences are structural, not semantic. This resolves the flagged joint review.
2. **vs Collision Repair Management (§29 sibling)**: collision/body shops run the same RO spine but estimate from accident damage against insurance claim processes, with paint/materials, frame/measuring, and total-loss workflows; customer-pay vs insurer-pay attribution dominates. Related, adjacent Type (already a separate directory leaf); joint review recommended when Collision Repair Management is processed.
3. **vs Fleet Management System (§18)**: FMS manages vehicles owned by the organization running the software (telematics, drivers, routes, compliance); this Type runs a service business whose customers own the vehicles. Inverse population; fleet accounts and fleet modules inside shop software are L2 service-customer structures, not FMS.
4. **vs Vehicle Inspection / Diagnostic Application (§29)**: the DVI is a module inside this Type; standalone inspection/diagnostic products are technician instruments (scan tools, inspection checklists) without the business lifecycle. Fragment, not duplicate.
5. **vs Car Wash / Detailing Management (§29 sibling)**: detailing/wash is appearance-service work with package pricing and quick turnover; no parts/labor diagnostic composition. Some vendors serve both from one platform (Shopmonkey lists detail shops); the RO economics differ enough to keep them separate leaves.
6. **vs Appointment Scheduling Application (§03.09)**: booking is one module; the Type is the whole shop operation.
7. **vs Small Business Field Service Management (§29)**: same relationship as appliance repair — field dispatch vs shop execution; auto repair shops do not route technicians to customers.
8. **Dealer Management Systems (not a directory leaf)**: franchised dealers sell and repair under OEM warranty with parts departments and OEM integration; independent shop software is the aftermarket equivalent. Recorded for orientation only.

## Uncertainties

- **RO state vocabulary**: lifecycle labels differ (columns vs statuses vs posted/unposted); canonical states are conceptual. Exact per-product state lists were not exhaustively researched (Tekmetric's state list lives in video training; only Unpost/Transfer article titles were observable).
- **Core tracking depth**: evidenced at three products (Tekmetric article title + returns; R.O. Writer explicit; Shopmonkey inventory returns) but the full workflow (core charge billing, credit receipt) was not article-verified.
- **Warranty payment mechanics**: warranty attribution and traceability are evidenced (Tekmetric; Shopmonkey extended-warranty best practice); full warranty-claim submission/reimbursement flows (e.g., aftermarket warranty administrators) were not verifiable in this sample.
- **Odometer universality**: explicitly documented at Tekmetric; implied elsewhere; treated as common rather than universal.
- **Enterprise tier**: Mitchell 1 Manager SE (the largest legacy incumbent) was unreachable; enterprise-specific structures are unverified. Two accessible products cover multi-location scale, mitigating but not eliminating this gap.
- **Regional products**: sample is North America-centric (as is the accessible documentation); non-North-American shop systems may differ in tax/fiscal integration (e.g., invoice regimes), which would be L2.

## Final Synthesis

Auto Repair Shop Management is the business-management application of a vehicle repair shop. Its defining core is small: a customer with a vehicle as the structured object of repair (with per-vehicle history), a repair order as the durable unit of work carrying the engagement from write-up through authorization, parts, labor, completion, invoicing, and payment, the labor-and-parts composition of priced work, and in-shop execution coordinated between front-counter staff and technicians. Around this core, mature products add the standard machinery of the trade: appointments and reminders, estimates with per-line authorization and declined-work follow-up, digital vehicle inspections, a status-organized workflow board, technician assignment with clock-in and efficiency measurement, labor operations with book times, parts inventory tied into supplier catalogs with purchase orders, cores, and matrix pricing, per-vehicle odometer history with mileage-based reminders, payment collection with warranty attribution, reporting, and accounting sync. The work happens at the shop — vehicles arrive, bays and technicians are the capacity — which structurally separates this Type from field-service repair management (appliance repair), while the vehicle-as-record and book-time-labor economics separate it from generic field service management. Fleet accounts, tire/quick-lube/heavy-duty specializations, multi-location groups, marketing, and financing are variant structures that scale the same core.
