# Research Notes — Jewelry Repair Management

## Research Goal

Understand what "Jewelry Repair Management" software actually is and how it works in real products: what objects exist inside it, what the repair workflow looks like, which structures are defining vs merely common, and where its boundary sits against neighboring Application Types (other repair-shop verticals, ticketing systems, POS, appointment-based service management, custom-order management).

## Initial Boundary

Working hypothesis before research:

- Core purpose: operator-facing job tracking for businesses that repair customer-owned jewelry — intake, estimates, repair tickets, bench workflow, statuses, customer notification, pickup and billing.
- Likely users: counter/sales staff, bench jewelers, shop owners/managers.
- Nearest neighbors: Appliance Repair Management, Auto Repair Shop Management, Ticketing System, Retail POS, Appointment-based Service Business Management, jewelry store suites (custom/special orders).
- Open questions: standalone repair products vs suite modules; estimate/approval mechanics; outsource/trade-shop workflows; unclaimed-item handling.

## Research Questions

1. What is the central object (repair ticket / work order / job)? What does it bind together?
2. What is captured at intake (item description, condition, accessories, photos, instructions)?
3. What lifecycle do repair jobs follow? Which states? Who moves them?
4. How do estimates, customer approval, deposits, and pricing (labor vs materials) work?
5. How is bench work managed (technician assignment, parts, notes)?
6. How do completion, notification, pickup, and payment work?
7. How does repair management relate to the broader jewelry store suite (POS, inventory, special orders)?
8. Where are the boundaries vs adjacent Types?

## Representative Products

Selected for market representativeness, documentation quality, product philosophy, era, and geography:

| Product | Vendor / origin | Philosophy / tier | Evidence depth reached |
|---|---|---|---|
| Jewelry Shopkeeper | Compulink (US, Scarsdale NY) | 30+ year Windows suite for "retail & wholesale jewelers & repair shops" | Tier-2 homepage (repair module described) |
| Jewel360 | Jewel360 (US, Utah) | Modern cloud jewelry POS, all-in-one | Tier-1 knowledge base (Work Orders, Custom Work Order Statuses) + Tier-2 product pages |
| The Jewel Software | The Jewel Software SAL (Lebanon) | International full suite, cloud/on-prem, "trusted in 23+ countries" | Tier-2 homepage (module list) |

Rejected / unreachable samples (recorded for transparency):

- The Edge / Edge Retail (jewelsoft.com, edgeretail.com) — transport errors ×2, abandoned.
- Affinity by Stuller (affinity.stuller.com, affinitybiz.com) — transport errors, abandoned.
- GemEasy (gemeasy.com) — transport errors / empty responses, abandoned.
- GemVision Liberty (gemvision.com) — JS-only shell, no content.
- Capterra category page — 403.
- Search engines (DuckDuckGo html/lite, Mojeek) — timeouts / captcha; abandoned.
- jewelsoftware.com — name collision; it is an unrelated Dutch waste-collection/grounds-maintenance vendor. NOT a jewelry product.

## Sources

- Jewelry Shopkeeper — https://www.jewelryshopkeeper.com/ (homepage; repair-tracking module description) — fetched 2026-09-08.
- Jewel360 — https://jewel360.com/ and https://jewel360.com/custom-work-and-repairs (product pages) — fetched 2026-09-08.
- Jewel360 Knowledge Base — https://knowledge.jewel360.com/article/work-orders ; https://knowledge.jewel360.com/article/custom-work-order-statuses ; https://knowledge.jewel360.com/modules — fetched 2026-09-08.
- The Jewel Software — https://thejewelsoftware.com/ (homepage) — fetched 2026-09-08.

## Product A — Jewelry Shopkeeper (Compulink)

### Key observations (evidence layer A, homepage depth)

- Positioning: "For over thirty years Jewelry Shopkeeper has been the #1 software program for retail & wholesale jewelers & repair shops." Repair shops are an explicitly served segment, not only jewelry stores.
- Repair tracking module description (verbatim from homepage feature list): "Fast Repair Take-In Using Customized Lists of Common Repair Wording. Quickly Add Photos at Take-In and as the Job is Done. Customizable Repair Tickets for Customer and Repair Shop. Complete History of all In-Progress and of Years Past. SMS-Text Customers."
- Reading of that description:
  - take-in is a fast, standardized capture step, aided by preset lists of common repair wording (trade-standard service descriptions);
  - photos attach at take-in and during the job;
  - the repair ticket is printable in customized forms for two audiences: the customer and the repair shop (suggests in-house bench and/or trade-shop copies);
  - the system keeps a complete history of in-progress jobs and of past years;
  - customers can be texted (SMS).
- Surrounding suite modules (context): inventory of finished goods, loose stones, findings; special orders; layaways; POS with customized receipts; price tags (dumbbell/ring tags, string tags, "resistant to steam and ultrasonic cleaning" — jewelry-specific physical artifacts); appraisals (implied by "per appraisal" imaging); customer lists/buying history; commissions; time clock; QuickBooks link.
- Digital imaging: "Multiple pictures per inventory item, per repair, per customer, per clerk, per appraisal" — photos are a first-class attachment type on repairs.

## Product B — Jewel360

### Key observations (evidence layer A, Tier-1 KB + Tier-2 pages)

Product page (custom-work-and-repairs):

- "Every custom work order lives in your point of sale (POS) system with customer details, job notes, due dates, and status attached."
- Create/manage repair and custom work orders directly from the POS; set target dates; track status; access active work orders from the customer record; assign work orders to technicians; manage access by user permissions.
- Automated text notifications when a work order is ready; customizable message and store signature; include customer info and work-order ID.
- Photos attached to orders "so your bench jeweler knows exactly what they're working on before they touch the piece."
- Pricing: flexible prices for repair/custom services; create and manage labor-based services; track service costs and customer prices; monitor profit/margins; "three-decimal pricing" for fractional cents.
- Multiple repairs for one customer: multiple jobs in a single transaction, each with its own details, due date, status, tied to the same customer record; completed work processed through the POS.
- Job templates; "split service tickets and customizable print options" so counter staff, bench jeweler, and customers work from the same documentation; customizable forms.
- FAQ: repair management is built into the POS (no separate software); each work order tracked with customer details, job info, services, due dates, status; multiple pieces at once supported; repairs and custom work share the machinery.

Knowledge Base — "Work Orders" article (Tier-1):

- Access: Modules > Work Orders; single-screen creation; "you are able to provide estimates and print out an initial ticket for the customer."
- Status drop-list (product's exact names): **Received** (estimate + ticket given to customer, item received, no work begun) → **In Process** → **In Process - Pending Approval** (waiting for customer approval on added work/price) → **In Process - Waiting for Parts** → **Ready for Pickup** (system offers to notify customer by email/SMS if contact info present) → **Completed** (full payment taken and item picked up; leaves the active list).
- Dates: received date auto-set; estimated completion date via date picker.
- **Bin Location**: track the physical bin/holding area of the item being worked on; dedicated work-order bin locations (separate from product bin locations); manageable list.
- **Sales Representative**: one or more reps with commission percentages.
- **Customer**: required to save the work order; searchable or created inline; clicking the name shows full details "including past work orders by that customer."
- Multi-location: work order assigned to a store location; location locked (grayed out) after save.
- **Item Attributes**: item description field; "whatever you enter here will also print on the Work Order Ticket."
- **Accessories**: "It is important to log on the initial drop-off the Accessories that were included with the main item by the customer, so there is no question on what they dropped off with you." Prints on the ticket; manageable accessory list.
- **Media**: upload files/images (from computer or camera); viewable at larger size; per-file limit 100 MB (product-specific).
- **Job Templates**: combine parts and service items for common jobs; reusable; editable per job.
- **Technician**: optional assignment; manageable technician list.
- **Job Services and Materials**: search services/parts (by Service ID); per-line notes that print on the ticket; create new materials/services inline; browse services by groups.
- **Estimates**: a line item can be an "Estimated Price"; checking the box treats the whole Job Total as an estimate.
- Multiple **Jobs** per Work Order ("no limit"), but "the Work Order is for work you are doing on a single item."
- **Work Order Totals**: subtotal, estimated tax, deposits paid; **Pay Deposit** routes into the Register and returns with the updated deposit amount.
- **Internal Comments** (staff-only, not printed) vs **Receipt Comments** (print on initial ticket and receipt; care instructions for the customer).
- **Add to Register**: take payment at any status; loads owed amount into the Register; deposit itemized on the final receipt.
- Deposit rule (product-specific): the Deposit field is only active while the Work Order is in "New" status (before first save).
- **Print Options**: email ticket, thermal receipt, full-page ticket, **Print Barcode** "so you can have a way to track the item and quickly look it up, and will help you to keep from confusing it with similar items."
- **Text Messaging in Work Orders**: two-way SMS conversation per work order with history; unread-message indicators on the alarm bell; filters for read/unread.
- Main list page: search by ID/status/customer/item title; date-range filters (creation/target/pickup date); location filter; status filter (default: all except Completed); technician filter; tags filter; text-message filter; bulk add to Register; export to spreadsheet.
- Work Orders in the Register: customer's open work orders accessible via Customer Actions; "wrench icon highlighted in gold" when ready for pickup; create new work orders from the Register; load ready work orders to complete; line items for each service and part; discounts; normal transaction completion; multiple work orders per customer in one register session.

Knowledge Base — "Custom Work Order Statuses" (Tier-1):

- Custom statuses can be created; each ties to a "parent" core status (Received, Pending, In Process, Ready for Pickup, Completed) — e.g., a "QA Confirmation" sub-status under In Process.
- Custom statuses appear in the module list, the Register's customer panel, and "on the customer account page for work orders" in the website login — customer-visible status consistency.
- Deleting a custom status reverts its work orders to the parent status.
- Managed at Settings > POS Settings > Work Orders.

## Product C — The Jewel Software

### Key observations (evidence layer A, homepage depth)

- Positioning: "The Innovative Solution for all Jewelers"; cloud or on-premise; mobile portal; "Trusted in 23+ Countries" (Lebanon-based, international footprint).
- Retail Shop Management module list includes: Gold Inventory management, Diamonds Inventory Management, Buying from Customers, **Repairs Management**, Special Orders Management, Expenses Management, Attendance & Employee Management.
- Wholesale & Factory Management includes Production Orders, **Polish & Plating Management**, Settings Management, Consignment Orders, Gem Inventory Management — the same vendor serves manufacturing-side workflows adjacent to repair work.
- Customer & Marketing: client profiling, bulk SMS & campaigns, dashboards, statements, funds management.
- Integrations: Shopify/WooCommerce, GIA/HRD/IGI certificate verification, Rapaport pricing; RFID item tracking.
- Repair-module detail is not documented on the reachable surface — only its existence as a named module alongside special orders and customer buying.

## Cross-product Comparison

| Aspect | Jewelry Shopkeeper | Jewel360 | The Jewel Software |
|---|---|---|---|
| Packaging | Windows suite for jewelers & repair shops | Cloud jewelry POS with built-in repair module | International suite (cloud/on-prem) |
| Central object | Repair ticket | Work order (single item, multiple jobs) | "Repairs Management" module (detail not documented) |
| Intake capture | fast take-in; preset common-repair wording lists; photos at take-in | single screen: customer (required), item description, accessories logged at drop-off, media/photos, dates, bin location | not documented |
| Lifecycle/status | in-progress vs past history implied | explicit: Received → In Process (+Pending Approval / Waiting for Parts) → Ready for Pickup → Completed; custom sub-statuses | not documented |
| Estimate & pricing | — | estimated-price line items; job total as estimate; labor-based services; materials; deposits; 3-decimal pricing | — |
| Bench/technician | — | optional technician assignment; photos "before they touch the piece" | Polish & Plating mgmt on factory side |
| Customer comms | SMS-text customers | automated ready-notification; two-way SMS per job; status visible in customer website login | bulk SMS (marketing context) |
| Documents | customizable repair tickets for customer and repair shop | print/email ticket, thermal receipt, barcode; internal vs receipt comments | — |
| Completion & payment | — | Add to Register → payment → receipt itemizes deposit; wrench icon when ready | — |
| History | complete history of in-progress and years past | customer record shows past work orders; filterable list page | — |
| Suite context | inventory (stones/findings), special orders, layaways, POS, tags, appraisals | POS, inventory, CRM, marketing, e-commerce, appraisals, metal buy, layaways | gold/diamond inventory, buying from customers, special orders, production, RFID |

### Evidence-layer reading

- Layer A (directly observed, per product): all rows above.
- Layer B (cross-product commonality, ≥2 products): repair job bound to customer + item; intake documentation (description, condition/accessories, photos); status lifecycle from received to completed; customer notification at readiness; printed/emailed tickets for customer and shop; per-customer repair history; payment at completion through the same system; repairs living inside a broader jewelry business suite.
- Layer C (canonical inference): the Type is a custody-based job-tracking system of record for customer-owned jewelry items, carried through a managed repair lifecycle to a billed return.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

1. **The repair job of record** — a persistent, individually identified job binding the customer, the specific item taken in, and the work requested, with the item's description/condition recorded at handover. Remove → generic ticketing or CRM with no custody of a physical piece.
2. **The managed repair lifecycle** — the job moves through defined states (received → in progress → ready → completed/returned) that shop staff update as work proceeds. Remove → a static log or to-do list; the "management" is gone.
3. **The return-and-settlement closure** — the item is returned to the customer and the job is billed (estimate → final charge → payment), which closes the job. Remove → internal work tracking with no customer transaction.

Historical check (§24-style reasoning): a pre-computer repair shop's handwritten repair envelope/tag — customer name, item description, requested work, estimate, claim check, filed after pickup and payment — satisfies all three invariants with zero software. Photos, SMS, barcodes, POS integration, named statuses, and technician fields are therefore NOT in L0. Older/regional/platform-native products fit.

### L1 — Common Mature Structure (very common, not defining)

- item-level intake detail: item description, condition notes, accessories received with the piece, photos at take-in and during work
- estimate/quote at intake; approval loop when added work changes the price (explicit "pending approval" state in Jewel360)
- labor-based service catalog plus materials/parts pricing on the job
- technician/bench assignment
- customer notification at readiness (SMS/email)
- printed/emailed tickets for the customer and the bench/shop; barcode/label for item identification
- per-customer (and effectively per-item) repair history retained over years
- deposits/prepayment on jobs
- payment at pickup processed through the same system (POS-integrated)

### L2 — Variant / Optional Structure

- packaging: module of a jewelry store suite (all three sampled products) vs standalone repair-shop product (Shopkeeper explicitly serves "repair shops"; standalone-only products could not be verified in this pass)
- repairs merged with custom work / special orders on shared job machinery (Jewel360 explicitly merges; Shopkeeper and The Jewel keep special orders as a separate module)
- trade-shop / wholesale repair workflows (Shopkeeper's "repair tickets for Customer and Repair Shop" hints at copies for an external repair shop; details unverified)
- multi-location assignment, bin-location tracking, RFID item tracking (The Jewel), appraisal modules, metal buy/scrapping, layaways
- customer-facing status visibility via website login (Jewel360)
- factory-side polish & plating management (The Jewel, wholesale/factory context)

### L3 — Vendor-specific (kept out of the final document)

- Jewel360: exact status names; deposit only collectable in "New" status; 100 MB per-file limit; three-decimal pricing; wrench icon; alarm-bell unread indicators; custom-status parent binding and revert-on-delete; location lock after save; default four-month list window.
- Jewelry Shopkeeper: "customized lists of common repair wording"; steam/ultrasonic-resistant tag stock; built-in financials vs QuickBooks export.
- The Jewel Software: GIA/HRD/IGI/Rapaport integrations; RFID locator; Lebanon origin.

## Vendor-specific Findings

See L3 above. None of these were promoted to the canonical model.

## Boundary Findings

- **vs Appliance Repair Management / Auto Repair Shop Management / Collision Repair Management**: the abstract job-shop shape (custody intake → lifecycle → billed return) is shared; the domain differs — jewelry items are individually valuable, described by metal/karat/stones, worked at a bench, and the trade has its own service vocabulary. These are sibling Types under the same abstract pattern, not the same leaf. Removing the jewelry domain (item semantics, trade vocabulary) turns this into the generic repair-shop pattern.
- **vs Ticketing System / Help Desk**: tickets route requests to an organization; no physical custody of a valuable item, no estimate-at-intake trade pricing, no pickup-and-return settlement. Remove custody + settlement → ticketing.
- **vs Retail POS**: POS centers on selling owned inventory; repair management centers on custody of the customer's item and the job lifecycle. Payment machinery is shared (Jewel360 completes work orders in the Register). Remove the job lifecycle → POS.
- **vs Appointment-based Service Business Management**: appointment-led scheduling vs custody-led job tracking. A promised completion date attaches to the job; the unit of work is the job, not the appointment slot.
- **vs Custom Order / Special Order Management**: restoring an existing customer item vs producing a new piece. Products often share machinery (Jewel360 merges repairs and custom work; others keep separate modules). Boundary is the object of work: the customer's existing item vs a new item to be produced.
- **vs Inventory Management**: parts/materials inventory (stones, findings) supports the work but is not the core; repair jobs reference materials, they are not inventory records.
- **vs Field Service Management**: work happens at the shop's bench, not at customer sites; no dispatch-to-location.

## Uncertainties

- Standalone jewelry-repair-only products (not part of a store suite): existence plausible (Shopkeeper serves "repair shops") but not directly verified — search engines were unavailable and several vendor sites unreachable.
- Outsource/trade-shop workflow details (sending work to a master jeweler, tracking outbound jobs): only hinted by Shopkeeper's "repair shop" ticket copy; not documented in fetched sources.
- Unclaimed-item handling (abandonment policies/timeframes): not evidenced in fetched sources; deliberately not written into the final document.
- Warranty-on-workmanship features: not evidenced.
- The Jewel Software's repair module internals: homepage-level evidence only; no workflow claims made from it.
- Jewelry Shopkeeper evidence is homepage-depth; its repair workflow details (statuses, estimates) were not verified and no precise claims were drawn from it.

## Final Synthesis

Jewelry Repair Management is the shop-side system of record for repair work on customer-owned jewelry. Its defining core is small: a repair job of record binding customer × item × requested work captured at handover; a managed lifecycle the shop advances (received → in progress → ready → completed); and a return-and-settlement closure (item returned, job billed, history retained). Everything else that modern products carry — photos, estimates and approval states, deposits, labor/material pricing, technician assignment, SMS notifications, barcoded tickets, customer portals — is common mature structure layered on that core, and the packaging (suite module vs standalone) is a variant, not the definition.
