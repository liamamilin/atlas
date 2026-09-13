# Research Notes — Warehouse Management System / WMS

## Research Goal

Understand what a Warehouse Management System (WMS) actually is in the real market: what objects it manages, how physical goods flow through it (inbound → storage → outbound), how work is directed to warehouse staff, what distinguishes it from neighboring Types (Inventory Management, TMS, DOM, YMS/Dock, ERP), and which structures are definitional vs. common vs. variant.

## Initial Boundary

Initial hypothesis (pre-research): a WMS manages physical operations inside a warehouse — receiving, putaway, storage, picking, packing, shipping — with fine-grained location tracking and directed work for warehouse staff on mobile/RF devices.

Neighboring Types to watch:
- Inventory Management System (§10 sibling, processed 2026-09-07) — stock levels without directed handling
- Transportation Management System / TMS (§10, processed 2026-09-08) — transportation execution; its pass recorded "WMS = warehouse execution vs transportation execution"
- Distributed Order Management (§05.07, processed) — decides which node fulfills; its pass recorded "decides-vs-executes… deep warehouse execution is WMS"
- Yard Management System + Dock Scheduling Platform (§10 siblings, unprocessed) — facility periphery (trailers, dock appointments)
- ERP (§10) — orders/POs/financials; ERP-embedded WMS modules exist
- Manufacturing Execution System (§16) — production floor vs storage/handling

Pre-hung flags to discharge:
- TMS pass seam (7): "WMS = warehouse execution vs transportation execution (Oracle publishes a dedicated WMS↔TM integration guide — paired products)"
- inventory-management-system pass: warehouse depth (bins/serial/lot/pick zones) as the WMS-flavored extension; store-inventory pass: "When physical handling becomes the center, the product drifts to WMS"
- distributed-order-management pass: DOM decides, WMS executes inside the node
- garage-door pass: dock name collision with yard/warehouse resolved vendor-side (ServiceTitan FAQ) — no joint review required

Note on the leaf name: "Warehouse Management System / WMS" — the slash is an abbreviation (WMS), not two seller-model poles. Single Type.

## Research Questions

1. What is the core object model — warehouse, location hierarchy, item, inventory, work/task?
2. How is the physical space modeled (zones, aisles, bins, address schemes, capacity)?
3. How does inbound work (ASN/PO → receiving → putaway)?
4. How does outbound work (order → allocation/release → wave/batch → pick → pack → ship)?
5. What is "directed work" — how are tasks generated, assigned, and validated?
6. What role does mobile/RF scanning play (scan validation, confirmations)?
7. How do lot/serial/expiry and handling units (LPN) work?
8. How does cycle counting work (creation, execution, discrepancy resolution)?
9. What is the 3PL variant (multi-client, billing)?
10. How does the WMS integrate with ERP/OMS (orders in) and TMS/carriers (shipments out)?
11. Where exactly is the WMS/Inventory-Management seam?
12. Where is the WMS/TMS and WMS/DOM seam?

## Representative Products

| Product | Segment / philosophy | Why sampled | Evidence depth |
|---|---|---|---|
| Microsoft Dynamics 365 Warehouse Management (Supply Chain Management module) | Enterprise ERP-family WMS; configuration-driven process engine (work templates, location directives, waves) | Enterprise pole; deepest public Tier-1 docs | Tier-1 (6 pages fetched) |
| ShipHero | 3PL / e-commerce fulfillment WMS; picking/packing-first | 3PL + e-commerce pole; public Zendesk KB | Tier-1 (6 pages fetched) |
| Infoplus | 3PL WMS; fulfillment-plan-driven, multi-client billing | 3PL pole; public HubSpot KB + glossary | Tier-1 (3 pages fetched) |
| Logiwa IO | Mid/enterprise 3PL & DTC; self-described "AI-native WMS / warehouse execution platform", headless | Modern execution-platform positioning | Tier-2 (product page only; KB login-gated) |

Attempted but unreachable (Source-access Limitation):
- SAP EWM — help.sap.com returns a JS shell (×2)
- Oracle NetSuite WMS — docs.netsuite.com transport errors (×2)
- Odoo Inventory/Barcode — odoo.com 403 (×2)
- Manhattan Associates — manh.com 403 (×2)
- Logiwa KB — support portal login-gated (×1; product page reachable)

Consequence: the enterprise pole beyond Microsoft is under-observed at Tier-1. Assertions about enterprise-class products other than D365 are kept weak or omitted. No precise numeric claims are made anywhere.

## Sources

Fetched 2026-09-08:

Microsoft Dynamics 365 (learn.microsoft.com, Tier-1):
- Warehouse management overview — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-management-overview
- Warehouse configuration overview — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-configuration
- Control warehouse work by using work templates and location directives — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/control-warehouse-location-directives
- Wave creation and processing — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wave-processing
- Cycle counting — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting
- Set up mobile devices for warehouse work — https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/configure-mobile-devices-warehouse

ShipHero (software-help.shiphero.com, Tier-1):
- Help Center root — https://software-help.shiphero.com/hc/en-us
- Picking & Packing category — https://software-help.shiphero.com/hc/en-us/categories/4419337429005-Picking-Packing
- Overview: Picking Methods in ShipHero — https://software-help.shiphero.com/hc/en-us/articles/46892350249997
- Warehouse Configuration & Hardware category — https://software-help.shiphero.com/hc/en-us/categories/4419337438477
- Inventory Management category — https://software-help.shiphero.com/hc/en-us/categories/4419337394573
- How to Manage Cycle Counts in ShipHero — https://software-help.shiphero.com/hc/en-us/articles/47709888701709
- 3PL category — https://software-help.shiphero.com/hc/en-us/categories/4419329732749

Infoplus (infopluscommerce.com, Tier-1):
- Knowledge Base root — https://www.infopluscommerce.com/knowledge-base/
- Getting Started — https://www.infopluscommerce.com/knowledge-base/getting-started
- Infoplus WMS Glossary — https://www.infopluscommerce.com/knowledge-base/warehouseglossary
- Locations Overview — https://www.infopluscommerce.com/knowledge-base/locations-overview

Logiwa (Tier-2):
- Product home — https://www.logiwa.com/ (KB at help.logiwa.com login-gated)

ShipHero product home (Tier-2): https://help.shiphero.com/ (marketing site; KB is the Tier-1 surface)

## Product A — Microsoft Dynamics 365 Warehouse Management

### Key observations

**Positioning [A]:** "The Warehouse management module lets you manage warehouse processes in manufacturing, distribution, and retail companies… fully integrated with other business processes such as transportation, manufacturing, quality control, purchase, transfer, sales, and returns." Process list includes: source-document support (sales orders, returns, transfer orders, production orders, kanban), inbound/outbound workflows "based on queries", full batch and serial item support, multiple picking strategies, outbound wave processing, manual packing and automatic containerization, cluster picking, cross docking, advanced counting, label printing (Zebra ZPL), full traceability of workers' material handling.

**Warehouse as modeled space [A]:** A warehouse must be "enabled for warehouse management processes". Layout entities: zone groups → zones → location profiles → location types → locations. "Locations — the lowest level of location information. Use locations to track where the on-hand inventory is stored and picked in a warehouse." Location stocking limits (e.g., one pallet per location), location profiles with weight/volume capacity, fixed picking locations and fixed packing locations, location setup wizard with name formats. Zones accommodate "temperature requirements, or various turnover rates".

**Directed work machinery [A]:** "Work templates… define what work is performed, and how the work is done." "Typically, warehouse work operations consist of a pair of actions: a warehouse worker picks up on-hand inventory in one location and then puts the picked inventory down in another location." Work templates have work order types (sales orders, replenishment, cycle counting, purchase orders…), work pools, work-split criteria (estimated pick time, volume, weight, quantity), work header breaks (grouping), stop work, work classes. "Location directives are rules that help identify pick and put locations… they define where to pick and put." Directive lines with min/max quantity, unit, split permission; directive actions with predefined strategies (e.g., "Empty location with no incoming work", "FEFO batch reservation").

**Outbound flow [A]:** "Release to warehouse" → wave templates (shipping / production / kanban) → wave created → processed → released; wave methods include creating loads, allocating lines, replenishment, containerization, creating picking work. Wave statuses (Created → Held; cancel after release possible). Inventory must be reserved before release for sales/kanban.

**Inbound flow [A]:** Mobile menu items for receiving: purchase order line/item receiving (and put away), license plate receiving (ASN by license plate), load item receiving, return order receiving (RMA), transfer order receiving, production "report as finished" (and put away). Receiving can create putaway work for another worker, or the same worker continues ("receiving and put away" variants).

**Mobile worker surface [A]:** Warehouse Management mobile app; menu items in three modes: Indirect (activities/inquiries: location inquiry, item inquiry, license plate inquiry/build/break, change warehouse, driver check-in/out [TM integration], display open work list, container packing…), Work creation (the receiving/movement/adjustment table above), Existing work processing with "Directed by": System directed (system assigns + sorts), User directed, User grouping, System grouping (scan shipment/load ID), Validated user directed (scan load ID; error if item not associated), Cluster picking, Cycle count grouping, Transport loading. Work confirmations: require product / location / quantity confirmation (scan-based); options: anchoring (override staging location), allow splitting of work, pick oldest batch (none/warn/force), generate license plate, override target license plate, print label. Menus are assigned per work user — "each worker sees only the menu items that are relevant to them".

**Cycle counting [A]:** Three steps: create work (thresholds — auto when quantity falls below limit; plans — scheduled; manual by item/location; spot counting), process on mobile (user directed / system directed / grouping / spot), resolve differences (work status Pending review; supervisor approval on "Cycle count work pending review"; deviation limits per worker — max percentage/quantity). "The system never shows the expected quantity to count. This design prevents intentional miscounts." Counting work does not block on-hand inventory ("available for reservation and outbound processing, even though open counting work exists"). Cancel button hidden during counting workflows.

**Inventory properties [A]:** Full batch and serial support; inventory status controls; reservation hierarchy (batch/serial above or below location); license plates as handling units (build/break); unit sequence groups (boxes/pieces counting).

## Product B — ShipHero

### Key observations

**Positioning [A]:** "ShipHero powers 3PLs and brands shipping millions of orders." Product modules: Order Management, Inventory Management, Returns Management, Picking & Packing, Live Carrier Rate Shopping, Receiving & Putaway, Labor Management (WorkforceHero), 3PL Client Portal, Work Orders, Pick-to-Light / Pack-to-Light / Receive-to-Light / Tap-to-Pack, AI Picking, Picker/Packer Performance Dashboards.

**Locations [A]:** "Managing Locations" section: location types, naming schemes ("Optimizing Your Warehouse Layout with a Naming Scheme"), bulk CSV updates, staging locations report, LPNs (License Plate Numbers) with LPN types, reusable LPNs, unpack from LPN. Picking requires "inventory locations… marked as pickable".

**Picking methods [A]:** Overview table: Multi-Item Batch (MIB — "pickers carry multiple totes. Each order is assigned a tote and items are sorted into the correct tote as the picker moves through the warehouse"), Single-Item Batch (SIB — shared tote, sorted by packer), QR Code Picking (guided location route from a Picking List QR code), Pick-to-Light (LED hardware), Location-Aware Picking ("AI-driven pick route optimization and picker performance tracking… tracks picker movement against an AI-generated baseline"), Wave Picking ("each tote on the cart holds one SKU shared across every order in the wave"; requires Location-Aware Picking + PTL hardware), Mobile Picking Interface (optional location scan enforcement). Order routing: workflows, required-ship-date filtering, batch picking/order sorting settings. "Why Is My Order Not Pickable?" troubleshooting exists.

**Packing [A]:** Packing app / packing stations (workstation setup), standard pack flow, single-item batch pack, multi-package shipments, weight discrepancy detection, scale integration, invoice printing, "Hospital" feature (exception/damaged orders at packing stations), command barcodes.

**Inventory [A]:** Cycle counts: types (Items / Locations / Items Flagged for Recount), statuses (Processing → Pending → In Progress → Closed), due date, assigned user, progress %, discrepancies; "While a cycle count is In Progress, the location being counted becomes unpickable until the count is complete"; recount flags with different user assignment; locked locations must be unlocked to close a batch; inventory updates logged in product Inventory Log and Inventory Change Log; mobile inventory adjustments; LPN cycle counts. Products: serial numbers, kits, work orders (assembly), dropship-only/auto-fulfill settings. Purchase orders with statuses, sell-ahead.

**Receiving/putaway [A]:** "Receiving, Replenishment & Putaway" section: inbound shipments created in mobile, receive to location, reject items during receiving, unreceive, replenishment with UOMs, break UOM into smaller units.

**3PL [A]:** 3PL Client Management (add/configure clients, switch between client accounts, connect additional warehouses per client, show label cost to clients) + 3PL Billing (33 articles: picking fees, storage-by-product charges, return label/item fees).

**Hardware [A]:** BLE/HID scanners, Zebra printers, scales, Pick-to-Light, Pack-to-Light, Receive-to-Light, Tap-to-Pack.

## Product C — Infoplus

### Key observations

**Positioning [A]:** "Take Control of Your Warehouse"; KB glossary defines: "WMS (Warehouse Management System): Software… which controls the movement and storage of materials within a warehouse." Modules include 3PL Billing, Insights, API/EDI/scripting.

**Warehouse structure [A]:** Onboarding Step 1 "Warehouse Configuration": Warehouse → Building → Zone → Aisle → Locations. "A Location is a specific place used to put away (store), pick (retrieve), and replenish (refill) items… Every place an item could be placed needs to have a location in the system." Address example: "S PR-100-1-103" = South Warehouse, Pallet Rack Zone, Aisle 100, Level 1, Location Number 103. Location attributes: footprints (width/depth/height), billing types ("typically used by third-party logistics providers" — bill by square footage), address schemes, location builder (mass creation), location labels (barcoded), behavior types ("assigning a behavior type of 'Pallet'… means only pallets can be placed and removed"), mixing rules.

**Inbound [A]:** Step 8: Vendors → ASN ("often referred to as Purchase Orders") → Receiving Worksheet ("connects the ASN… to actual receipt… used to generate Put Away work tickets") → Item Receipts → Put Away work tickets → commit receipts ("items are available for ordering"). Quick receipts (SKU + quantity + location in two steps), blind receiving without ASN, receiving criteria schemes, unreceive.

**Outbound [A]:** Step 12: Orders (order sources, hold codes, backorders) → Fulfillment Plans ("a plan for how inventory will be picked and packed for an order") → Run Fulfillment → Fulfillment Process record → Work Tickets ("generate work tickets directly from allocation and picking processes") → picking methodologies (wave pick, pick to order, pick to tote; case pick, forward pick, pallet pick), pick carts, pick scan schemes, alternate pick (different location when inventory missing), no-stock recovery, cartonization (auto carton selection from item dimensions). Step 13: packing slips, parcel labels, rate shopping, ship station (mobile), ship non-parcel (LTL/TL/will call), unship, shipments/tracking.

**Inventory [A]:** Step 9: cycle counts ("physical count… may count only a portion… discrepancy… bound to occur due to human error"), inventory snapshot, quick adjustments, inventory adjustments table (quantity, reason, notes, PO affected). Allocation: "The process by which inventory is assigned to orders, removed from on-hand inventory, and the orders become ready for shipment"; allocation behaviors (oldest PO lot first, strict FIFO); lot control (strict/weak), serial number tracking; forward pick locations + pick face assignments (replenishment point, max quantity); replenishment ("movement of inventory from upstream product storage locations to downstream pick locations").

**Labor [A]:** Job Time / Job Type records (receiving, putaway, picking…), labor optimization ("allocate from the optimal location for minimizing labor"), labor tracking reports.

**3PL [A]:** Lines of Business (business units), 3PL customer access roles, location billing types, 3PL Billing module, custom logos/branding.

**Mobile floor apps [A]:** Load, ASN Inquiry, Change Inventory Status, Pick to Cart, Inventory Adjustment, Layout, Inventory Relocation, Item/Location/Order Inquiry, Interactive Receiving, Run Job, Job Inquiry, Pack Station, Ship Station, Location Move, barcode scans for pack station.

## Product D — Logiwa (Tier-2 only)

### Key observations

**Positioning [A, Tier-2]:** "AI-native WMS that optimizes warehouse fulfillment… Maximize throughput with AI-driven warehouse execution. Orchestrate your inventory, labor, and automation in real time." Self-describes as "warehouse execution platform" and "intelligent operating system for high-volume enterprise logistics"; 3PL and DTC/e-commerce industries; headless/API-first architecture, App Store, MHE/robotics integrations, labor planning. No operational documentation reachable (KB login-gated) — no workflow claims made.

## Cross-product Comparison

| Structure | D365 | ShipHero | Infoplus | Logiwa | Evidence |
|---|---|---|---|---|---|
| Warehouse as configured facility with addressable locations | ✓ zones/profiles/types/locations, stocking limits, fixed pick locations | ✓ location types, naming schemes, pickable flag, staging | ✓ warehouse→building→zone→aisle→location, footprints, behavior types | implied (Tier-2) | B |
| Location addresses as scannable barcodes | ✓ (scan confirmations) | ✓ (location scans, naming schemes) | ✓ (location labels, barcoded addresses) | — | B |
| Location-granular inventory of record | ✓ on-hand by location, license plates | ✓ stock at locations, LPNs | ✓ warehouse inventory table, item receipts | implied | B |
| Directed work: system-generated pick/put/replenish/count/move tasks | ✓ work templates + location directives | ✓ picking batches, replenishment, cycle counts | ✓ work tickets (put away, pick, location move) | implied ("orchestrate") | B |
| Mobile/RF worker surface with scan validation | ✓ mobile app, confirmations (product/location/quantity) | ✓ mobile app, location scan enforcement option | ✓ mobile floor apps, pick scan schemes | implied | B |
| Inbound: ASN/PO receiving → putaway | ✓ PO/LP/load receiving (+put away variants) | ✓ inbound shipments, receive to location, reject | ✓ ASN → receiving worksheet → put away tickets | — | B |
| Outbound: order release → pick → pack → ship | ✓ release to warehouse → wave → work → pack/ship | ✓ order routing → batch pick → pack → ship | ✓ fulfillment plan → run fulfillment → pack → ship | implied | B |
| Wave/batch picking methods | ✓ waves, cluster picking | ✓ MIB/SIB/wave/QR/PTL | ✓ wave pick, pick to order/tote | — | B |
| Packing station + parcel label/rate shopping | ✓ packing, containerization, ZPL labels | ✓ packing app, rate shopping | ✓ pack station, rate shopping, cartonization | — | B |
| Replenishment (bulk → forward pick) | ✓ (wave replenishment, min/max) | ✓ (replenishment with UOMs) | ✓ (pick face assignments, replenishment points) | — | B |
| Cycle counting with discrepancy resolution | ✓ thresholds/plans/spot, pending review, deviation limits | ✓ types, statuses, recounts, location lock | ✓ cycle counts, snapshot, adjustments | — | B |
| Lot/serial/expiry tracking | ✓ full batch/serial, FEFO strategy | ✓ serial numbers on products | ✓ lot control (strict/weak), serial tracking | — | B |
| Handling units (LPN) | ✓ license plates (build/break) | ✓ LPNs, reusable LPNs | ✓ LPN (glossary) | — | B |
| Labor tracking/productivity | ✓ "full traceability of workers' material handling" | ✓ picker/packer performance dashboards | ✓ job time/job types, labor optimization | ✓ (labor planning, Tier-2) | B |
| 3PL multi-client + billing | — (not observed in fetched pages) | ✓ client management + billing (picking/storage/return fees) | ✓ lines of business, billing types, 3PL billing | ✓ (3PL industry, Tier-2) | B (2/3 deep) |
| ERP/OMS order intake integration | ✓ source documents (sales/transfer/production) | ✓ store integrations (Shopify etc.) | ✓ shopping carts, EDI, order sources | ✓ (ERP integrations, Tier-2) | B |
| Carrier/TMS handoff at dock | ✓ driver check-in/out (TM), ZPL labels | ✓ carrier management, rate shopping | ✓ parcel accounts, BOL, non-parcel | ✓ (carrier integrations, Tier-2) | B |
| Automation hardware (PTL/pack-to-light/MHE) | — (not in fetched pages) | ✓ PTL/PtL/RTL/Tap-to-Pack | — (printers/scales) | ✓ (MHE/robotics, Tier-2) | B (2/4) |
| AI-era features | — (not in fetched pages) | ✓ AI picking, AI baseline routing | — | ✓ (AI-native positioning) | B (2/4) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The warehouse as a modeled, addressable physical space.** The facility is configured in the system as a hierarchy of storage locations (zones/aisles/levels/bins or equivalent), each individually addressable (typically via scannable labels), carrying physical attributes (capacity/footprint/behavior rules). Remove → generic inventory system / space modeling; the "where" that drives everything disappears.

2. **Location-granular inventory of record.** Item quantities held at specific locations; movements recorded as the way state changes; lot/serial/handling-unit (LPN) tracking as the common extension of the same record. Remove → nothing for work to act on.

3. **Directed physical work execution.** Inbound and outbound flows are decomposed by the system into discrete handling tasks — receive, put away, pick, replenish, count, move — which are assigned/directed to workers step-by-step (typically on mobile/RF surfaces with scan validation) and whose execution is recorded back into the inventory record. Remove → inventory-management-system territory (stock levels without directed handling).

Jointly-held is load-bearing:
- 1 alone = facility/space modeling
- 2 alone = Inventory Management System (the sibling Type)
- 3 alone = generic task dispatch
- 1+2 without 3 = inventory system with bin depth — exactly the "WMS-flavored extension" seam the store-inventory pass recorded ("when physical handling becomes the center, the product drifts to WMS")
- 2+3 without 1, and 1+3 without 2, are incoherent: directed work presupposes locations and stock

Historical check (§24): paper-era warehouse — rack/bin labels + bin cards (location-granular stock) + pick tickets/putaway tickets (directed work) + count sheets with supervisor sign-off — satisfies all three legs at analog level. 1990s RF-directed WMS satisfies without cloud/AI/automation. ERP-embedded, standalone, 3PL, e-commerce-native, and AI-native-execution poles all satisfy. No modern capability is in the core.

### L1 — Common Mature Structure

- Inbound process: ASN/PO-driven receiving (receiving worksheets/records), directed putaway with strategies, cross-docking
- Outbound process: order release/allocation, wave/batch formation, multiple picking methods (discrete, batch, cluster, wave, zone), pick-path routing, packing stations, parcel label/rate shopping, staging/loading
- Replenishment from bulk/reserve to forward-pick locations
- Cycle counting with recount and approval mechanics
- Lot/serial/expiry tracking with FIFO/FEFO allocation behaviors
- Handling units / license plates (LPN)
- Mobile/RF scanning with scan validation (product/location/quantity confirmations)
- Labor tracking and productivity measurement
- Reporting/dashboards; integration spine (ERP/OMS orders in; carriers/TMS out; automation hardware)

### L2 — Variant / Optional Structure

- 3PL multi-tenancy: client accounts, per-client warehouses, client portals, 3PL billing (storage/picking/return fees, location billing types)
- Packaging: ERP-embedded module (D365) vs standalone vs e-commerce-native (ShipHero) vs headless execution platform (Logiwa)
- Automation depth: pick-to-light, pack-to-light, receive-to-light, tap-to-pack, conveyors/MHE, robotics
- Industry/regulatory: cold chain, hazardous, food/FEFO-heavy, manufacturing supply (production waves, raw material picking, report-as-finished putaway)
- Deployment: cloud vs on-prem
- AI-era: AI picking, AI route baselines, AI slotting

### L3 — Vendor-specific (Research Notes only)

- D365: work templates / location directives / wave templates as named configuration objects; reservation hierarchy; license plate build/break; anchoring; detours; work pools; directive strategies ("Empty location with no incoming work", "FEFO batch reservation"); system never shows expected count quantity; deviation limits per worker; driver check-in via TM
- ShipHero: MIB/SIB naming; QR-code picking; Hospital feature; Tap-to-Pack; Picker Performance Score vs AI baseline; wave picking requires Location-Aware Picking + PTL; location lock during count makes it unpickable; 3PL label-cost display
- Infoplus: fulfillment plans; AFR (Advanced Fulfillment Rules); smart filters/triggers; LocalConnect; lines of business; location behavior types; quick receipts; no-stock recovery; alternate pick
- Logiwa: IO branding; App Store; headless/API-first; "operational GPS" marketing

## Vendor-specific Findings

See L3. Additionally: ShipHero's "wave picking" is a cart-based single-SKU high-volume method (different from D365's wave = release-to-warehouse processing unit) — same word, different referents; the canonical concept (grouping orders for efficient picking) is L1, the mechanics are vendor-specific.

## Rejected Findings

- "WMS = inventory management with more fields" — rejected: directed work execution is the discriminator; the inventory-management-system pass's own L0 (stock records + events, no directed work) confirms the seam.
- "WMS includes transportation management" — rejected: carrier label/rate-shopping and driver check-in are handoff surfaces; transportation execution between locations is TMS (TMS pass seam 7 ratified from this side).
- "WMS decides which warehouse fulfills an order" — rejected: that is DOM (distributed-order-management pass: "decides-vs-executes… deep warehouse execution is WMS"). A WMS executes inside one node; multi-node decisioning arrives as released orders.
- "3PL billing is definitional" — rejected: 2/3 deep samples carry it; a brand-owned WMS (D365 pole) has none. Variant.
- "Automation hardware integration is definitional" — rejected: paper-era and RF-era WMS satisfy the core without it.
- "Wave processing is definitional" — rejected: wave is one outbound grouping mechanism; Infoplus fulfillment plans and ShipHero batch picking reach the same directed-work outcome without D365-style wave objects.

## Boundary Findings

1. **vs Inventory Management System (§10, processed 2026-09-07)** — RATIFIED keep-both from this side. Inventory = what we have where (stock records + recorded events; no directed work). WMS = how it physically moves (directed handling over location-granular stock). The inventory pass itself flagged bin/serial/lot/pick-zone depth as the "WMS-flavored extension" and the store-inventory pass wrote "when physical handling becomes the center, the product drifts to WMS" — this pass confirms the drift point is the directed-work leg. WMS contains an inventory layer as substrate (L0 leg 2) but the Type is defined by leg 3.

2. **vs Transportation Management System / TMS (§10, processed 2026-09-08)** — seam 7 DISCHARGED from this side. TMS = transportation execution (tender/rate/track between locations); WMS = inside-the-building execution. Handoff at the dock: WMS produces shipment/label/staging; TMS/carrier takes over. D365 documents driver check-in/out as a TM integration surface — the boundary is visible inside the product itself. Paired-products relationship (Oracle WMS↔TM guide per TMS pass) consistent.

3. **vs Distributed Order Management (§05.07, processed)** — RATIFIED from this side. DOM decides which node fulfills; WMS executes inside the node. Kibo's own wording (per DOM pass): assignment "initiates the fulfillment workflow (picking, packing, shipping) at the assigned location" — the WMS is what executes that workflow. A WMS may receive released orders from a DOM/OMS/ERP; it does not make network-level sourcing decisions.

4. **vs Yard Management System (§10, unprocessed)** — seam recorded: YMS = trailers/trucks/dock doors/parking in the yard; WMS = goods handling inside the building. D365's driver check-in and staging/loading locations are the WMS-side edge of this seam. No merge; the YMS pass should ratify.

5. **vs Dock Scheduling Platform (§10, unprocessed)** — seam recorded: dock appointments (time-slot booking) vs WMS receiving (goods handling once they arrive). Appointment machinery ships as TMS modules (per TMS pass) and stands alone; WMS consumes the arrival. No merge.

6. **vs ERP (§10)** — ERP holds orders/POs/financials; WMS executes physical fulfillment. ERP-embedded WMS modules (D365 module observed; SAP EWM/Oracle by market position) are a packaging variant, not a boundary collapse: the module still models the warehouse space and directs work.

7. **vs Manufacturing Execution System (§16, unprocessed)** — seam recorded: production floor vs storage/handling. D365 WMS touches production via raw-material picking and report-as-finished putaway — the WMS handles storage-side legs of production supply; conversion itself is MES territory.

8. **"Warehouse Execution System" (WES) market label** — Logiwa self-labels a WMS as a "warehouse execution platform". Held as a positioning/packaging variant of this Type (execution emphasis + automation orchestration), not a separate Type: the observed product still centers locations + inventory + directed work.

## Uncertainties

- Enterprise pole beyond Microsoft under-observed at Tier-1 (SAP EWM, Manhattan, Blue Yonder, Körber, NetSuite, Odoo all unreachable). The L0 is expected to hold for them (their market descriptions consistently name warehouse process management), but this is inference, not direct observation for those products.
- Exact status vocabularies (wave statuses, cycle-count statuses, work statuses) are product-specific; only conceptual states are claimed.
- Cold-chain/hazardous/ASRS-deep deployments not directly observed; held as plausible variants only.
- Logiwa operational behavior unknown (Tier-2 only); no workflow claims made for it.
- Whether every WMS carries labor management: 3/4 sampled carry some form; held as common (L1), not definitional.

## Final Synthesis

A WMS is the warehouse's physical-execution system of record. Its world is built from three jointly-held structures: the warehouse modeled as addressable physical space (location hierarchy with scannable addresses and physical attributes); location-granular inventory of record (what is where, at bin granularity, with lot/serial/handling-unit extensions); and directed physical work (the system decomposes inbound/outbound flows into discrete handling tasks, directs them to workers step-by-step on mobile/RF surfaces with scan validation, and records execution back into inventory). Everything else — waves, picking methods, replenishment, cycle counting, packing, parcel shipping, labor, 3PL billing, automation hardware, AI — is mature structure or variant layered on that spine. The Type's edges are sharp: without directed work it is an inventory management system; beyond the dock door it is TMS/YMS territory; above the node it is DOM; inside production it is MES.
