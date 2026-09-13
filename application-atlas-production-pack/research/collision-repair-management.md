# Research Notes — Collision Repair Management

## Research Goal

Understand "Collision Repair Management" as an Application Type: the business-management software used by collision/body shops to run damage repairs — from accident-damage estimate intake through insurance-claim interaction, production (body/paint/frame), parts procurement, customer communication, and settlement. Identify the core objects (vehicle, claim, estimate/supplement, repair order/folder, parts, labor, production stages, paying parties), the repair-order lifecycle, who operates the system and from which surfaces, which structures are collision-specific (estimate import from estimating systems, claim/insurer payment machinery, body-shop department model, sublet, paint & materials), and where the boundary lies against Auto Repair Shop Management, Insurance Claims Management, estimating systems, and adjacent service-business types.

## Initial Boundary

- Nearest types: **Auto Repair Shop Management** (§29 sibling — flagged for joint review), **Insurance Claims Management** (§08, insurer side), **Car Wash / Detailing Management** (§29 sibling, prior pass held "no claim machinery" seam), Fleet Management System (§18), Towing/Roadside (§18 upstream), Appointment Scheduling (§03.09 fragment), Small Business Field Service Management (§29).
- Preliminary hypothesis: same generic repair-order spine as auto repair, but the intake artifact is an accident-damage estimate (authored in specialized estimating systems), the paying-party structure is customer-pay vs insurer-pay, and the shop is department-based (body / paint / frame). To be tested.
- Open question from prior passes: is this a separate Type or a trade-variant of Auto Repair Shop Management? (auto-repair pass flagged joint review; car-wash pass asserted "Collision Repair has claim machinery" as its own seam.)

## Research Questions

1. What objects does the system manage? Is the estimate an object inside the system or an import?
2. What is the repair-order lifecycle in a body shop (stages, departments, gates)?
3. How do insurance claims enter, attach, and drive the workflow? Who authorizes work? What happens when teardown reveals more damage (supplements)?
4. How does parts procurement work (states, vendor channels, returns/credits)?
5. How are paying parties and settlement handled (customer vs insurer, deductible, receivables)?
6. Who are the users/roles, and which surfaces do they use?
7. What KPIs dominate (cycle time, key-to-key, flagging efficiency, gross profit)?
8. Joint review: separate Type vs trade-variant of Auto Repair Shop Management?
9. Historical check: would a paper-estimate, manual-labor-guide body shop satisfy the definition?

## Representative Products

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Mitchell Cloud Repair + RepairCenter (Mitchell, an Enlyte company) | Management suites from an estimating-data incumbent; insurer-network gravity; cloud + legacy desktop poles | Richest reachable module documentation for both management poles |
| Solera AutoFocus (+ Qapter/Audatex context) | Shop management inside a claims-ecosystem vendor (FNOL→estimating→repair→settlement) | Documents the claims-ecosystem-embedded posture |
| Nexsyis Collision | Independent all-in-one body shop management with integrated accounting | Independent-management philosophy, deep PO/workflow detail, accounting-first |
| CCC ONE (CCC Intelligent Solutions) | Market-leading estimating + management suite | Market anchor — UNREACHABLE in this pass (see Sources) |

Rejected during sampling:
- **Ratchet** (getratchet.com) — domain parked/for sale; product unreachable.
- **AutoOps** (autoops.com) — product mismatch: online scheduling layer for general auto shops (integrates mechanical shop systems: Shop-Ware, Shopmonkey, Tekmetric, R.O. Writer, Mitchell1), not a collision repair management system. Capability slice of a different Type.
- **Mitchell1 / Tekmetric / Shopmonkey / R.O. Writer** — already sampled as the Auto Repair Shop Management pole in the sibling pass; used here only as contrast, not re-sampled.

## Sources

Fetched 2026-09-07 (all official vendor pages — Tier 2 product documentation; no Tier-1 help-center articles were reachable for any sampled product):

1. Nexsyis — home: https://www.nexsyiscollision.com/
2. Nexsyis — Repair Management: https://www.nexsyiscollision.com/repair-management
3. Nexsyis — Production Tracking: https://www.nexsyiscollision.com/production
4. Nexsyis — Purchasing: https://www.nexsyiscollision.com/purchasing
5. Nexsyis — CRM: https://www.nexsyiscollision.com/crm
6. Mitchell — Auto Physical Damage root: https://www.mitchell.com/solutions/auto-physical-damage
7. Mitchell — Collision Repairers overview: https://www.mitchell.com/solutions/collision-repairers
8. Mitchell Cloud Repair: https://www.mitchell.com/solutions/collision-repairers/repair-management/cloud-repair
9. Mitchell RepairCenter: https://www.mitchell.com/solutions/collision-repairers/repair-management/repair-center
10. Mitchell Cloud Estimating: https://www.mitchell.com/solutions/collision-repairers/estimating
11. Mitchell WorkCenter Loss Profiling & Dispatch (insurer side): https://www.mitchell.com/solutions/auto-insurers/loss-profiling-dispatch
12. Solera Claims home: https://www.claims.solera.com/
13. Solera AutoFocus (Shop Management): https://www.claims.solera.com/products/shop-management/
14. Enlyte root (Mitchell APD + PartsTrader): https://www.enlyte.com/

Unreachable (recorded per source-access rules):
- CCC / cccis.com — HTTP 403 on 3 attempts (solutions page, root). Market-leading anchor not verified from primary source; no CCC-specific claims made.
- getratchet.com — domain for sale; Ratchet unreachable.
- enlyte.com/products/mitchell-cloud-estimating — 404 (superseded by mitchell.com path, which worked).
- No help-center / support-portal articles for any sampled product were reachable in this pass (Wix-gated or login-gated support desks). Evidence tier: official product/marketing pages only → structural claims are well supported; operational details (exact statuses beyond those displayed, defaults, numeric limits) are NOT asserted.

## Product Observations

### Mitchell Cloud Repair (official product page)

Evidence layer: A (direct observation).

- Positioning: "cloud-based repair management… streamline your operations and efficiently manage repairs… from any internet-enabled device."
- **Repair Order Management**: dashboards to "track parts procurement, pricing changes and estimate revisions"; "automatically import estimates from all major platforms as opportunities"; download/print "RO documentation, work orders and invoices" from one location; "revenue totals from closed repair orders" reporting.
- **Production Management**: "track repair work and customer vehicles in your facility"; technicians "update the vehicle location to any custom shop department"; "provide insurance carriers with automatic repair status updates."
- **Parts Management**: "Fully integrated with OEC"; "submit purchase orders in a single click"; manage "parts invoices, credits and returns, as well as price changes on the estimate."
- **Sublet Management**: third-party vendor workflow "from scheduling to completion date and invoice posting."
- **Services Tracking**: "create cost invoices for towing, paint-and-materials and body supplies."
- **Accounting Integration**: "payables invoices and sales records to QuickBooks Online… Accounts Payable and Receivable."

### Mitchell RepairCenter (official product page; legacy desktop suite)

Evidence layer: A.

- Positioning: "Complete Collision Repair Management Solution… from estimating to blueprinting and scheduling to documentation"; cycle-time visibility "to deliver on customer and carrier expectations."
- **Repair Orders**: "virtual job files"; "Estimate Conversion Compatibility with All Major Estimating Systems"; overview of "labor totals, job costs and payments."
- **Online Repair Status**: text/email updates; "auto-trigger option when there is a vehicle department change during the repair."
- **TechAdvisor**: OEM repair procedures + Mitchell-authored parts and labor guides (30+ years).
- **Parts Management**: OEConnection integration; "CollisionLink online parts ordering system."
- **Parts & Labor Scrubbers**: "reclassifying parts and labor data according to your business needs… repairs that are classified differently in estimating systems."
- **AR Payments Management**: "Track customer and insurer payment amounts for each repair order… Confirm all estimate payment responsibilities… Certify amounts paid and dates received."
- **Job Costing**: costs by department, "net profits and break-even points."
- **Opportunity Management**: walk-in follow-up.
- **Labor Management**: "track and assign labor," "Place labor by type or operation."
- **Production Management**: "track repair progress per vehicle in each department"; production schedules; "vehicle location and key dates from any mobile device."
- **Attachments & Mobile**: photos/PDFs/video/audio/invoices attached to any repair order; mobile upload.
- **Repair Scheduling**: "by shop capacity and parts lead time for different vehicle makes"; multiple-shift scheduler; "Fastlane Scheduler for scheduling small jobs."
- **Analytics**: target profit percentages, daily work hour averages; Premium adds cycle-time reporting.
- **Shop Clock**: technician hours "for payroll and job costing."
- **Estimate Rules Analyzer**: "Scan estimates for inaccuracies… against pre-set criteria… before committing the estimate."
- **DMS Interfaces**: bi-directional with ADP / Reynolds & Reynolds (dealership collision centers).
- **Multi-Site**: "View all shops… each unit's performance, production status and accounting numbers"; corporate analytics drill-down.
- **Customer Engagement Tools**: satisfaction surveys.
- Packaging: modules (Essentials/Professional/Premier) — packaging posture, not structure.

### Solera AutoFocus (official product page) + Solera claims-ecosystem context

Evidence layer: A (AutoFocus); A (context pages).

- Positioning: "Body Shop Management Software… for small or demanding high production shops… automated parts management… productivity tracking."
- **Efficient Scheduling**: "Graphical, color coded listing of production capacity… consistent load levels. A time clock is included to record touch times."
- **Detailed Work Orders**: "Import from estimating systems with correct data translation"; "easy-to-follow worksheets with print options… for your labor types."
- **Visual Production Management**: "A view of all jobs to track workflow, technicians, parts, returns, orders, vendor invoices, receivables, **claim status** and communications."
- **Cycle Time Management**: "schedule jobs according to shop resources and production capability… proactively manage delays."
- **Complete Parts Management**: "send purchase orders via e-mail or fax, and track due dates, returns, credits and **supplements**."
- **Accurate Labor Costing**: "Flexible labor-costing and team-tracking tools… cycle times, labor efficiency and **payroll flagging**."
- Roles named: "estimator, parts manager, technician, bookkeeper, front office manager, or shop owner."
- Ecosystem context (same vendor, adjacent products): **Qapter Intelligent Estimating** — "automated, line-by-line vehicle repair estimates and optimal repair methods from damage photos"; **Qapter Mobile Inspection** — guided photos → "preliminary estimate in just minutes"; **AudaVIN** — VIN decode from photo; **Intelligent Triage** — "total loss or repairable"; total-loss valuations; **APU Parts Procurement** — "aftermarket parts, recycled and alternate OE" quotes; **AutoWatch** — technicians upload vehicle photos + repair status for customers; Managed Repair / Desk Review (carrier-side estimate review, rental coordination, payments). Home page: "reducing key-to-key times."

### Mitchell Cloud Estimating + WorkCenter (official product pages; estimating + insurer context)

Evidence layer: A.

- Cloud Estimating: VIN scanning "decode and populate vehicle data automatically"; parts diagrams; ADAS identification; aftermarket parts info; vehicle photos; "Integrated Repair Procedures… OEM repair information from the estimate line"; TruckMax (labor hours, aftermarket parts for trucks); "Mitchell Intelligent Estimating… collision estimates from images and vehicle information"; insurer-side "Estimate Profiles and Rules… appraisers follow pre-set guidelines before committing the estimate" (Estimate Advisor).
- WorkCenter (insurer side): FNOL photo capture; "method of inspection (MOI) selection"; assignment & dispatch (appointment booking, route optimization, resource allocation, workload distribution across "photo-based estimating, field appraisers or independent adjusters"); Mitchell Connect itinerary for appraisers. → The dispatch/assignment machinery is insurer-side; the shop-side system receives assignments/claim context.

### Nexsyis Collision (official product pages)

Evidence layer: A.

- Positioning: "true business management and accounting application… for collision repair"; segments "MSOs | Independent Operators | Dealerships."
- **The Folder (repair order)**: "stores all important repair information. A Folder can be created with a customer name and phone #, **or by importing an estimate**." "Nexsyis allows you to **add multiple claims for the same vehicle to a single Folder**."
- **Vehicle Center (production tracking)**: vehicles move through stages "**Opportunity** → **Scheduled Drops** → **In Process** → **Completed, Not Delivered** → **Final Review** → **Outstanding A/R**"; statuses fully customizable ("number of statuses, order, color, description… specified by you"); custom hold/flag columns; saved views.
- **Purchasing (PO-based)**: statuses "**Not Ordered / Needs Ordered / Ordered (Not Received) / Received (Not Invoiced) / Rejected (Not Returned) / Returned (No Credit Memo) / Invoiced**"; vendor orders "through e-mail, fax, or a purchasing service such as **OEConnection**," attaching "photos, notes, and a copy of the estimate," with "an expected delivery date"; "Missing Parts (MP), Missing Sublet (MP)" visible live in the production screen.
- **Technician Time & Labor**: "flagging" to "measure and track technician efficiency."
- **Digital QC**: multi-point QC questions by department; "require photo documentation"; responses "recorded with date/time and USERID and can be audited."
- **Document Imaging**: attach images "directly to the transaction record."
- **Gross Profit Analyzer**: margins by "parts, labor, and materials."
- **Internal Messaging**: repair-related messages "automatically recorded in the repair Folder's notes."
- **Production Mobile App** (NexsyisNow): capture photos, record notes, update vehicle repair stage, complete QC from mobile.
- **Accounting**: integrated "payables and receivables… bank reconciliation… financial statements," fed by repair management data.
- **CRM / intake**: **online photo estimate** — website lead transfers into the application ("Capture customer & vehicle information, damage photos, and customer notes… text or e-mail the customer a link to view their estimate and invite them to schedule an appointment"); **e-signature** authorization ("Send customized, real-time documents for signature via text or e-mail"); **SMS/email templates** (appointment reminders, repair status updates, follow-up reminders); **digital vehicle check-in** — "curb-side check-in… capture customer contact preference, vehicle information, damage & UPD photos, complete a damage survey, and send the authorization for digital signature in one easy workflow"; **customer repair status portal** (status, documents, photos, message service writer); **online payment** (Global Payments integration).
- **Scheduling**: "flows seamlessly into the repair process" (scheduled drops stage).
- **Reporting/KPIs**: wide variety + custom reporting.

## Cross-product Comparison

| Structure | Mitchell Cloud Repair | Mitchell RepairCenter | Solera AutoFocus | Nexsyis | Verdict |
|---|---|---|---|---|---|
| Vehicle as identified object of work | ✔ (vehicle location/departments) | ✔ (per-vehicle per-department) | ✔ (jobs/vehicles) | ✔ (Vehicle Center) | Core (B) |
| Repair order / job file as center | ✔ (RO dashboards, docs, invoices) | ✔ (virtual job files) | ✔ (work orders) | ✔ (Folder) | Core (B) |
| Estimate intake from external estimating systems | ✔ ("import estimates from all major platforms as opportunities") | ✔ ("Estimate Conversion Compatibility with All Major Estimating Systems") | ✔ ("Import from estimating systems with correct data translation") | ✔ ("importing an estimate"; also manual creation) | Core (B) — collision-defining intake |
| Estimate line structure (labor by type, parts, materials, sublet) | ✔ (pricing changes, sublet, paint-and-materials services) | ✔ (parts & labor scrubbers, labor by type/operation) | ✔ (worksheets by labor types) | ✔ (gross profit by parts/labor/materials; missing sublet) | Core (B) |
| Insurance claim attached to repair | ✔ (carrier status updates) | ✔ (claim context; insurer payments) | ✔ ("claim status" in production view) | ✔ (multiple claims per Folder) | Core (B) |
| Paying-party split (customer + insurer) | ✔ (implied; carrier updates) | ✔ explicit ("customer and insurer payment amounts… certify amounts paid and dates received") | ✔ (receivables + claim status) | ✔ (Outstanding A/R; insurer invoices; customer online payment) | Core (B) |
| Production stage/department model | ✔ (custom shop departments) | ✔ (department change triggers) | ✔ (color-coded capacity, workflow view) | ✔ (stages Opportunity→Outstanding A/R, customizable) | Core (B) — stage names vary by product |
| Parts PO lifecycle incl. returns/credits | ✔ (invoices, credits, returns; OEC) | ✔ (OEConnection/CollisionLink) | ✔ (due dates, returns, credits) | ✔ (7 explicit PO states) | Core (B) |
| Supplement handling | ✔ ("estimate revisions") | ◐ (via estimate re-import / scrubbers) | ✔ explicit ("track… supplements") | ◐ (folder-based revisions; not named) | Common (B) — naming varies; supplement concept explicit in 2, adjacent in 2 |
| Sublet as cost category | ✔ (Sublet Management) | ◐ | ◐ | ✔ ("Missing Sublet" tracked) | Common (B) |
| Paint & materials / body supplies as cost category | ✔ (Services: towing, paint-and-materials, body supplies) | ◐ (TechAdvisor parts/labor guides) | ◐ | ✔ (gross profit by materials) | Common (B) |
| Technician time / flagging | ◐ | ✔ (Shop Clock; labor mgmt) | ✔ (touch times; payroll flagging) | ✔ (flagging efficiency) | Common (B) |
| Scheduling with capacity + parts lead time | ◐ | ✔ (capacity + parts lead time) | ✔ (production capacity load levels) | ✔ (scheduled drops; missing-parts visibility) | Common (B) |
| Customer repair-status communication | ✔ (to carriers automatically) | ✔ (text/email; dept-change auto-trigger) | ✔ (AutoWatch companion) | ✔ (portal, SMS/email templates) | Common (B) — both carrier- and customer-facing |
| Authorization / e-signature | — | — (insurer-side Estimate Advisor analog) | — | ✔ (e-signature; check-in→authorization workflow) | Common (B) — Nexsyis explicit; authorization concept implied by estimate-payment confirmation in RepairCenter |
| QC documentation with photos | ◐ (attachments) | ✔ (attachments mobile) | ◐ | ✔ (multi-point QC, photos, audit trail) | Common (B) |
| Accounting integration / job costing | ✔ (QBO) | ✔ (QuickBooks/BusinessWorks; job costing) | ✔ (profitability reporting) | ✔ (fully integrated GL) | Common (B) |
| KPI/analytics (cycle time, gross profit, target profit) | ✔ (closed-RO revenue) | ✔ (analytics, cycle time) | ✔ (productivity/profitability) | ✔ (KPIs, gross profit analyzer) | Common (B) |
| Estimate authoring inside the system | ✘ (imports) | ✘ (imports; estimating is add-on import automation) | ✘ (imports; Qapter is separate product) | ✘ (imports; manual creation possible) | Core pattern (B): management systems import; authoring lives in estimating systems |
| Multi-site / MSO | — | ✔ (multi-site analytics) | — | ✔ (MSO segment; locations) | Common (B) |
| AI photo estimating | — (sibling product) | — | ✔ (Qapter context) | — (photo-estimate intake only) | Optional (B) — sits in estimating systems / insurer triage more than shop management |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Collision Repair Management system is recognizable as this Type iff it manages:

1. **A damaged vehicle as the identified object of work** — accident/collision damage on a specific, identified vehicle brought to the shop.
2. **A line-item damage estimate that defines the job** — labor (by type/operation), parts, and materials priced against industry estimating data (OEM labor hours/parts reference), consumed by the system (authored internally or, dominantly, imported from a specialized estimating system) as the definition of work, subject to revision.
3. **An authorized repair order (job file) that carries the repair through the shop** — the estimate converts into a repair order; the vehicle progresses through shop stages/departments; the repair order accumulates labor, parts, materials, and sublet cost and holds documents/photos.
4. **Settlement across recorded paying parties** — customer-pay and/or insurance-pay amounts recorded per repair order and resolved as receivables/payments.

Remove the damage-estimate-defined work + paying-party settlement and what remains is a generic auto-repair or job-shop system. Remove the vehicle/shop-stage model and it is claim administration, not shop management.

### L1 — Common Mature Structure (very common, not definitional)

- Insurance claim machinery attached to repairs: claim records (multiple claims per vehicle/repair), claim status tracking, automatic repair-status updates to carriers, insurer payment certification and insurer AR.
- Supplements: mid-repair estimate revisions/re-additions when teardown reveals additional damage.
- Parts procurement: PO-based ordering with statuses (ordered → received → invoiced) plus returns, rejections, credits; parts-sourcing channels (OE dealer networks, aftermarket/recycled/alternate-OE quoting services).
- Department/stage production boards (body, paint, frame, detailing; custom statuses), vehicle location tracking, hold/flag states.
- Technician time capture and flagging (booked vs clocked efficiency), payroll linkage.
- Scheduling against capacity and parts lead time; drop-off scheduling.
- Customer communication: appointment reminders, status updates, photo sharing, repair-status portals, online payment, e-signature authorization; damage-survey check-in.
- QC documentation: multi-point inspections with photos and audit trails.
- Sublet and service cost categories (towing, paint & materials, body supplies).
- Accounting integration or built-in GL; job costing by department; gross-profit analysis by parts/labor/materials.
- KPI reporting: cycle time, throughput, target profit, labor efficiency.
- Estimate-scrubbing/compliance checks before committing estimates.
- Multi-site/MSO roll-up views.

### L2 — Variant / Optional Structure

- Insurer-program posture: DRP/network-shop workflow where the shop receives carrier assignments (the dispatch machinery itself is insurer-side).
- Dealership collision-center variant: bi-directional DMS integration (vehicle/customer/RO data), OEM certification programs.
- MSO/multi-site operating model: centralized management, corporate analytics.
- Total-loss handling: repairable-vs-total-loss triage and valuations (mostly insurer-side; shop records the outcome).
- ADAS/diagnostics workflow integration (scan/calibration records attached to repairs).
- Glass-only shops, PDR (paintless dent repair), specialty vehicles (motorcycles, commercial trucks) estimating scopes.
- Photo/AI estimating and virtual appraisal; online photo-estimate lead capture from shop websites.
- Regional variants: bilingual (e.g., French-Canadian) deployments; regional labor-rate and regulatory postures.
- Packaging: cloud vs desktop suites; module ladders; standalone management vs suites bundled with estimating.

### L3 — Vendor-specific (research notes only)

- Nexsyis "Folder", "Vehicle Center", "Purchases Assistant", 7 named PO states, NexsyisNow mobile app, "Gross Profit Analyzer", Global Payments integration, "MSOs | Independent Operators | Dealerships" segmentation, "damage & UPD photos" (UPD = unrelated prior damage per industry usage; expansion not verified on page).
- Mitchell "Cloud Repair"/"RepairCenter"/"TechAdvisor"/"Estimate Rules Analyzer"/"Fastlane Scheduler"/"ToolStore"/WorkCenter/"Mitchell Connect"; module ladder QuickStart→Essentials→Professional→Premier; OEC integration; ADP/Reynolds & Reynolds DMS interfaces.
- Solera "AutoFocus"/"AutoWatch"/"Qapter"/"AudaVIN"/"XpertEstimate"/"APU"/"Intelligent Triage"; "key-to-key" phrasing.
- Enlyte corporate structure (Mitchell APD vs Mitchell1 mechanical lines; PartsTrader); OEConnection CollisionLink.

## Vendor-specific Findings

- The estimate-authoring layer is a separate product family (CCC ONE / Mitchell Cloud Estimating / Qapter class). Shop-management systems in this sample uniformly import estimates rather than author them. CCC ONE bundles estimating + management in one suite — a bundling posture, not evidence that authoring is part of management.
- Mitchell names the intake object an "opportunity" (imported estimate → opportunity → repair order); Nexsyis names it an "Opportunity" stage. Solera/AutoFocus name it a job/work order. Concept is stable, labels differ.
- Insurer-side products (Mitchell WorkCenter dispatch, Estimate Advisor rules; Solera Managed Repair/Desk Review) perform assignment and estimate review — the shop system's counterpart is receiving assignments and submitting/revising estimates.

## Boundary Findings

1. **vs Auto Repair Shop Management (§29 sibling — flagged joint review, now completed)**: shared spine = customer → vehicle → repair order → labor/parts → invoice → accounting. Structural differences: (a) **intake artifact** — collision jobs are defined by a line-item accident-damage estimate consumed from specialized estimating systems (all four sampled collision products import estimates; the mechanical sample creates estimates internally from inspections/DVIs); (b) **paying-party structure** — collision carries a persistent customer-vs-insurer payment split with insurer AR and payment certification; mechanical is customer/warranty-pay; (c) **shop model** — collision is department/stage-based (body/paint/frame) with vehicle-location tracking; mechanical is bay/technician-based; (d) **authorization gates** — work is authorized by a party external to the shop (insurer) for most volume, with a recurring supplement loop after teardown; (e) **cost categories** — paint & materials, sublet, towing as first-class lines. **Existence proof of separate markets: the same parent vendors ship separate product lines** — Enlyte runs Mitchell (collision) and Mitchell1 (mechanical); Solera runs Audatex/Qapter (collision) and Identifix Direct-Hit (mechanical). Verdict: **related Types sharing a repair-order pattern, not aliases and not a trade-variant pair.** The generic "repair business" pattern is the shared abstraction; the objects and rules above the pattern differ. Joint-review flag discharged.
2. **vs Insurance Claims Management (§08)**: the claim system's object is the insurance claim (coverage, adjudication, settlement); the collision shop system's object is the repair (estimate, production, parts, delivery). The shop system records claim context (claim numbers, carrier, adjuster interactions, payments received) and communicates status outward; it does not adjudicate coverage or settle the claim. Carrier-side dispatch/estimate-review products sit on the other side of the seam.
3. **vs Estimating systems (no directory leaf; product family: CCC ONE estimating, Mitchell Cloud Estimating, Qapter)**: authoring the damage estimate against OEM labor-hours/parts databases is a distinct instrument; management systems import its output, track revisions, and scrub for compliance. The two are tightly coupled (a management product without estimate import is not viable in this market) but the objects differ (estimate lines vs jobs/production). Bundling exists (CCC ONE).
4. **vs Car Wash / Detailing Management (§29 sibling)**: appearance services with package pricing and no damage-estimate/claim machinery — consistent with the prior pass's seam; collision's estimate/claim/production structure is the separator.
5. **vs Fleet Management System (§18)**: FMS manages an organization's own vehicles in operation; collision management runs a service business on customers' vehicles. Fleet accounts appear only as customer segments.
6. **vs Towing Dispatch / Roadside Assistance (§18)**: towing appears as a sublet cost line / service invoice inside collision management; dispatching tow trucks is a different Type.
7. **vs Appointment Scheduling Application (§03.09) and Small Business Field Service Management (§29)**: scheduling is one module; shops do not dispatch technicians to customer locations — vehicles come to the shop.
8. **Name-collision guard**: "Collision Repair Management" shares the word "repair" with Appliance/Auto Repair Shop Management and "claims" territory with Insurance Claims Management; documented to prevent future conflation.

## Uncertainties

- **CCC ONE (market leader) unverified from primary source** — cccis.com returned 403 on all attempts. CCC's exact management feature set is not asserted anywhere in this research; CCC is cited only as a representative market product. The estimating-led suite posture attributed to CCC follows from the industry's estimating-system structure but was not verified.
- **No Tier-1 help-center documentation reachable** for any sampled product (Wix/login-gated support desks; HugeDomains-parked Ratchet). All evidence is official product pages (Tier 2). Consequence: no numeric limits, no default settings, no exact stage/permission semantics asserted; stage names quoted are the products' own examples, not industry standards.
- The **"supplement"** concept is explicit in two products (AutoFocus "track… supplements"; Cloud Repair "estimate revisions"); its exact approval workflow (who signs off, carrier approval flow) was not documented on reachable pages — kept at capability level.
- **UPD** acronym (Nexsyis check-in) expansion ("unrelated prior damage") is industry usage; not verified on the fetched page.
- Shop-side **estimate compliance** (RepairCenter "Estimate Rules Analyzer") and insurer-side estimate rules (Estimate Advisor) both exist; the split of compliance responsibility between shop and carrier is posture-dependent and was not fully evidenced.
- "Blueprinting" (RepairCenter) and "damage survey" (Nexsyis) suggest a formal teardown/inspection stage between estimate and repair; its exact position and gates vary by shop process — kept qualitative.

## Final Synthesis

Collision Repair Management is the operator-side business system for collision/body shops. Its defining core is small: a damaged vehicle as the object of work; a line-item damage estimate (labor/parts/materials, priced against industry estimating data) that defines the job and is subject to revision; an authorized repair order that carries the vehicle through shop stages/departments while accumulating labor, parts, materials, and sublet cost; and settlement recorded across paying parties (customer and/or insurer). Around this core, mature products add the structures the market expects: insurance-claim attachment and carrier status/payment machinery, supplement handling, PO-based parts procurement with returns/credits and sourcing channels, department production boards with vehicle location and holds, technician flagging and payroll linkage, capacity/parts-aware scheduling, customer status portals with photos and e-signature authorization, QC documentation, accounting integration/job costing, cycle-time and gross-profit KPIs, and multi-site roll-ups. The intake mechanism — importing estimates authored in specialized estimating systems — binds this Type to the estimating-system family without merging with it. Historical check: a paper-era body shop running manual flat-rate estimating guides, handwritten repair orders, and telephone status calls satisfies the minimal core; DRP networks, AI photo estimating, portals, and KPI dashboards are modern additions, not definitions. Joint review verdict: separate Type from Auto Repair Shop Management — shared repair-order pattern, different intake artifact, paying-party structure, shop model, and authorization rules, with same-vendor separate product lines as market evidence.
