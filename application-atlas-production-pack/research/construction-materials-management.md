# Research Notes — Construction Materials Management

Research date: 2026-09-07
Leaf: Construction Materials Management (DIRECTORY §17 Construction, Real Estate & Facilities)
Slug: construction-materials-management

---

## Research Goal

Understand what "Construction Materials Management" software actually is as an Application Type: what the managed population is (bulk commodities? discrete items? both?), what core objects exist, what users do with them, how material flows from requirement to installation, which states and rules matter, and where the boundary lies against neighboring Types (equipment management, generic inventory, procurement/PO platforms, warehouse management, transportation/dispatch, field management, estimating/takeoff).

## Initial Boundary (hypothesis before research)

- Hypothesis: contractor/project-side management of physical construction materials — tracking what the project needs, what is ordered, what arrives, where it is stored (yard/warehouse/staging), and what has been installed — as a ledger of material quantities moving through the site supply chain.
- Likely confusions:
  - Construction Equipment Management (§17) — durable metered machines vs consumed materials (already researched; that pass drew the seam "materials are consumed against work; machines are durable, metered, reusable assets with hours/utilization").
  - Inventory Management System (§10) — standing stock replenishment vs project-anchored supply-to-installation.
  - Procurement Management / Purchase Order Management (§10) — buying transaction vs physical material journey.
  - Warehouse Management System (§10) — warehouse operations optimization vs multi-site material control.
  - Transportation Management System / Dispatch Management (§18) — truck orchestration vs material quantity/state.
  - Construction Field Management / Daily Log (§17) — deliveries as day events vs materials ledger as object of record.
  - Quantity Takeoff / Construction Estimating (§17) — pre-award required quantities vs post-award actual materials.
- Unknowns at start: is procurement execution definitional? Is inventory/stock management definitional? Is item-level identity required (vs bulk quantities)? Is requirement/takeoff linkage definitional? Does the hauling/dispatch perspective belong inside this Type? Does a supply-chain network perspective belong inside?

## Research Questions

1. What is a "material" in these systems — how are bulk commodities and discrete items represented?
2. Where do requirements come from (takeoff/BOQ/MTO/orders) and how are required vs actual quantities compared?
3. How are procurement/ordering and suppliers handled — and what happens to materials that are not procured through the system (free-issued)?
4. How are deliveries/shipments/loads recorded and tracked?
5. How is storage handled — yards, warehouses, laydown areas, custodians, locations?
6. How is consumption recorded (issue, withdrawal, installation, progress)?
7. What exceptions matter (over/short/damaged, defects, missing items)?
8. What interfaces exist (registers/grids, item detail, mobile scanning, maps, dispatch boards, reports)?
9. Who participates (contractor-only, or supply chain parties too)?
10. Where is the boundary against generic inventory, procurement, WMS, TMS, and equipment management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers. Three primary products, each a distinct pole:

1. **Track'em Materials** — materials control platform for capital-intensive construction, mining, oil & gas projects (owner operators, EPC/Ms, contractors; Australia/North America). The formal *material control* pole: registry of parts, custody, receipting/withdrawal, laydown yards, OSD reports, rules of credit.
2. **Matrak** — cloud materials-tracking network for head contractors plus their global supply chain (manufacturers, suppliers, logistics, installers; Australia-origin, global offsite/facade trades). The *supply-chain network* pole: BOQ from drawings, AI-ingested packing lists, QR-coded packs tracked from production to installation across parties.
3. **Trux** — dump-truck logistics software for aggregates/asphalt producers, heavy & civil contractors, haulers (US). The *bulk hauling logistics* pole: dispatch, loads, GPS cycle tracking, e-ticketing, delivered tons vs ordered.

Secondary cross-reference (evidence reused from the sibling Construction Equipment Management research pass, same date and environment):
- **Tenna** (construction equipment platform) — its managed population was directly observed to include "inventory and consumables" alongside machines, i.e. the equipment-platform pole embeds a materials slice.

Not sampled directly (source-access limitations, see Sources):
- **StruxHub** (GC field-side materials delivery management) — site unreachable after 2 attempts.
- **Kojo** (construction materials procurement platform) — site unreachable after 2 attempts.
- **Hexagon Smart Materials / Intergraph Smart Materials** (classic EPC material control suite) — hexagon.com 403, docs portal is a JS-only application with no fetchable content.
- **ERP-embedded purchasing/inventory modules** (Viewpoint, Sage, CMiC, Foundation) — not attempted; treated as a boundary/variant note with reduced evidence only.

## Sources

All fetched 2026-09-07 (Tier 1/2 official vendor surfaces):

- Matrak homepage: https://matrak.com/
- Matrak Materials Tracking: https://matrak.com/materials-tracking-software/
- Matrak Supply Chain / Procurement: https://matrak.com/solutions-procurement/
- Track'em homepage: https://www.trackem.com.au/
- Track'em Materials Tracking: https://trackem.com.au/materials-tracking/
- Trux homepage: https://www.truxnow.com/
- Trux Materials product page: https://www.truxnow.com/products-trux-materials
- Tenna (cross-reference, fetched in the construction-equipment-management pass): https://www.tenna.com/ , https://www.tenna.com/use-cases/equipment-management-system/

Source-access limitations:
- StruxHub and Kojo unreachable → the GC field-side *delivery-request/appointment* machinery and the *supplier-quote-comparison procurement* machinery are NOT directly evidenced in this sample. No precise claims are made about them in the final document; the delivery-logistics capability is evidenced only through the hauling pole and network pole.
- Hexagon Smart Materials unreachable → the classic EPC material-control suite is represented only indirectly (Track'em documents the same EPC practices: receipting, requisitioning, free-issued materials, rules of credit, laydown yards). No claims about Hexagon's product appear anywhere.
- ERP-embedded materials modules not fetched → that realization is noted with reduced confidence and without any product-specific detail.
- All fetched pages are vendor marketing/product surfaces; no per-feature help articles were fetched (Track'em helpdesk and Matrak Help Centre exist but were not needed for the stable commonalities; Trux Help Center exists). Operational precision (exact limits, defaults, plan gates) is therefore avoided in the final document.

---

## Product A — Track'em Materials (EPC/resource material-control pole)

### Key observations (Evidence layer A unless noted)

- Self-positioning: "Materials Management and Tracking Software for capital intensive construction projects"; "Track'em Materials provides project-wide visibility of construction materials and parts and digitises critical material handling processes. Designed specifically for large construction, mining, oil and gas projects."
- Visibility framing: "gives stakeholders visibility across the supply chain: from fabrication, to installation, to maintenance"; "increases productivity and decreases project delays"; "interruptions caused by unavailable materials are flagged pro-actively."
- Registry: "A full registry of all your parts. Intuitive interfaces provide you with every little detail on the status, documentation and inventory levels of your materials. Track'em Materials can deal with multiple sites, locations and permission levels."
- Inventory & custody: "Have continuous insight into the status, location and custodian of all your parts at any part in the construction process."
- End-to-end tracking: "Stay on top of your inventory levels and delivery dates across the supply chain. Easily scan and update items." Stages named: "Fabrication tracking. Shipment Tracking. Stage tracking. Gate tracking. Warehouse and laydown yard management."
- Field app: "The Track'em materials app gives you all the functionality you need to find, receipt, update, issue or transfer materials." Scan barcodes/QR codes via smartphone or "(intrinsically safe) scanners"; works offline "in the most remote of locations"; permission-based access for supply-chain stakeholders.
- Digitized processes/documentation: "stock takes, delivery schedules, QA/QC, receipting and requisitioning, transfer requests"; "Digitise your forms such transfer requests, dockets, inspection documents and digitise your receipting and withdrawals."
- Movement documents: picklists, requests for install, transfer requests, inspection requests, materials movement tickets, requests for transport, print lists.
- OSD (Over, Short or Damaged) reports: created from app or desktop; "Add any photos and describing commentary, and assign the report to the responsible individual and track the status until it's resolved"; structured templates; status tracking to resolution.
- Material structure semantics: "Split, Group, Bulk Fab, Procured vs Free Issued. We've got that covered. Group materials and track them together while maintaining a record of each component's history. Split parts into separate items, while maintaining a record of origin. Clearly distinguish between (bulk) fabrication and materials items. Manage free issue (FIM) and procured materials."
- Rules of Credit: "Manage your Rules of Credit and stay on top of your earned value. Set the gates with their respective weights and progress materials through the activities for complete performance measurement." Progress: "Monitor usage and construction progress, manage rules of credit, and identify bottlenecks pro-actively."
- Location technology: barcodes, RFID, GPS, Bluetooth; mapping "accurate enough to manage laydown yard placements and on-site movements"; geofencing auto-updates items crossing virtual boundaries; heatmaps; route plotting with distance/maintenance implications.
- Audit: "logs every transaction"; "full history and audit trail of all touchpoints and individuals involved"; "Track every part and component back to its original source, whilst having a full historical trail of every change in status, location, custodian & condition."
- Inspections/maintenance: reminders for required maintenance/inspections; app-based checklists with photos.
- BIM integration: "Enrich your BIM models with a digital twin of construction progress and component status based on information from the field."
- Reporting: "Visualise, report and share data with stakeholders to track progress, delays and deviations." Alerts on inventory levels, progress deviations, upcoming inspections.
- Audience: Owners (insights into contractor management), EPC/Ms and head contractors (visibility/reputation), contractors (claims support, "get paid on time"). Case studies: Rio Tinto Iron Ore (owner operator — supply-chain track & trace across 17 mines/ports/logistics hubs, SAP + 3PL integration); AusGroup/Altrad (EPC — LNG turnaround time tracking). Customer quote (UGL): "Track'em puts 'control' back into materials control."
- Scale claim: "Over 40 million items tracked in engineering and construction projects" (vendor marketing claim).

## Product B — Matrak (supply-chain network pole)

### Key observations

- Self-positioning: "A cloud-based construction management software and materials tracking platform that enables end-to-end supply chain visibility for your team. Track material interactions and manage operations on a single global database." Marketed globally as "materials tracking"; trades covered: "Matrak started with facade, then joinery and now 30 different trades, from steel to sanitary, and pre-cast to plaster."
- Requirement origin: "Create a single Bill of Quantities on interactive drawings so everyone knows what's ordered for when"; "Upload your drawings, make them interactive and generate a bill of materials in a snap"; AI takeoff "finds every material and every task". Sync with "BOQs, drawings, and schedules" from existing tools.
- Document ingestion: "Matrak's AI system automatically analyses the POs and packing lists emailed from your suppliers, automating the tracking of materials and shipments without manual intervention"; "Stop wasting time wrangling disorganised packing lists, delivery dockets, or supplier spreadsheets… Matrak's AI cleans, structures, and maps your data automatically."
- Tracking lifecycle: "Our QR codes ensure you can track products from production to shipment, installation, and reorders." Status and location of "every component" is "critical to a project's progression, enabling supply chain visibility for everyone involved."
- Interactive drawings: "Easily update site progress, material status and get updates instantly from our interactive drawings." Progress tracker: "Track site progress on drawings & against program dates with all trades."
- Activity log: "Date and time-stamped activity logs to see every action made to materials to improve efficiencies, and help with dispute resolution to protect your business." Suppliers' angle: "one source of truth to review the history of all interactions with materials"; "share real-time, end-to-end, historical data on every piece of material supplied."
- QR machinery: "Easily generate, print and scan QR code stickers to instantly view and update materials or pack items using any smart phone or tablet."
- Network: "With over 2,000 companies on the Network and on over 1,100 construction projects" (and on the supply-chain page "over 800 companies… 500+ projects" — figures vary across pages, vendor marketing); roles: head contractors, manufacturers, suppliers, logistics, installers; multi-language UI ("English, Mandarin, Thai, Spanish and more") for cross-border factories; network directory of companies.
- Quality: "When your installer finds a defect on-site, your manufacturer on the other side of the world knows, too"; defect tagging with instant notifications; ITP checklists ("inspection and test plan checklists… tick them off as you go").
- Mobile/offline: "Designed for factory, warehouse and site teams… Matrak works offline—efficiently handling basements and tunnels—and saving your photos and updates whenever you're back in range."
- AI assistant "Digi": "proactively monitors your projects… can email your team and suppliers to prevent delays on your behalf while escalating areas of risk."
- Embodied carbon: "Matrak's AI tech uses our material passport data to provide real-time carbon budgets for products heading to your job site. From supplier EPDs to industry benchmarks like EC3 and NABERS." Scope-3 carbon reporting "as items move through your supply chain."
- Integrations: Procore, Autodesk Construction Cloud, Power BI, Dynamics, SAP, Excel, public API (developer.matrak.com), ERP connections.
- Customer examples: Metro Tunnel, Queens Wharf, Multiplex, John Holland, Lendlease, Hutchinson Builders (project-scale head contractors).

## Product C — Trux (bulk hauling logistics pole)

### Key observations

- Self-positioning: "Material Delivery Logistics and Dump Truck Dispatching… dump truck logistics software is designed to help you manage trucking logistics in one place -- from dispatching to delivery and everywhere in between." Audiences: aggregates & asphalt producers, sand/salt, heavy & civil contractors, fleet owners/owner-operators, brokers. "Trux is ideal for any bulk material that moves by dump truck—including stone, gravel, sand, asphalt, and fill."
- Orders and quantities: dispatch dashboard shows "planned, ticketed, and delivered tons, completion percentage"; "Load planning tools automatically calculate how many loads, trucks, or tons will be required to fill an order"; order confirmation communications include "material, quantity, velocity, start/end time, and delivery location."
- Dispatch machinery: "Drag and drop hauler dispatching, load stacking, and reassignment"; hauler utilization; automated communication of job details and changes; Trux Marketplace of third-party haulers (add-on); hauler compliance validation (COI, W-9, prevailing wage, DOT/MC numbers).
- GPS/cycle tracking: "Monitor the progress, time-stamped route, current location, and ETA of all loads and all trucks, in real-time and after delivery"; geofence arrival/departure; plant and jobsite wait times; cycle-time analytics; "Load Auto-Complete based on truck proximity to the paver and/or milling machine geofence" (HMA package).
- Tickets: "Digital slips are available directly from within Trux as soon as each load is completed"; e-ticketing with integrated scale systems; "View and export all scale data for easy job cost and hauler pay reconciliation"; paper ticket transcription add-on; "timestamped digital tickets to verify deliveries, reduce disputes."
- Customer-facing machinery: Trux Delivery Tracker (customer tracks "every truck, driver, load, and quantity between the plant and the job site", delivery velocity, e-tickets, "1-tap… reorder additional materials"); delivery confirmation emails with scale-ticket data.
- Cost: "Real-time project and hauling cost tracking of hours, loads, and quantity delivered by hauler and by project"; Trux Pay hauler payment processing; integrations: scale ticketing, ERP, accounting, "Sales Order APIs… Dispatch Order APIs… Scale System APIs."
- Products: Trux Materials (producers), Trux Construction (contractors' hauling fleets), Trux Ticketing (quarries/pits/plants scale ticketing), Trux Drive (hauler mobile app).

## Cross-reference — Tenna (equipment-platform pole embedding materials)

- Observed in the construction-equipment-management pass: Tenna's managed population includes "inventory and consumables" alongside machines; its platform includes parts inventory (maintenance-side) and inventory/consumables tracking. This shows the equipment-platform pole treats materials as an adjacent population inside an asset platform — the reverse of this Type's center of gravity. (Evidence layer A for Tenna specifically; used only as a boundary observation.)

---

## Cross-product Comparison

| Dimension | Track'em | Matrak | Trux |
|---|---|---|---|
| Self-label | Materials management & tracking software for capital-intensive projects | Materials tracking platform / supply-chain visibility network | Material delivery logistics & dump truck dispatching |
| Material form | Parts & materials: discrete items, grouped/split lots, bulk fabrication, piping; item-level identity | Discrete items and packs (facade/joinery/steel/etc.), item+pack-level identity | Bulk commodities by truckload (tons/loads): stone, gravel, sand, asphalt, fill |
| Requirement origin | Project material requirements; inventory levels; requisitions; delivery schedules (takeoff/MTO not surfaced in fetched pages) | BOQ generated from interactive drawings (AI takeoff); POs/packing lists ingested | Customer/sales orders; load planning computes loads/trucks/tons per order |
| Procurement in system | "Procured vs Free Issued" distinction — free-issued materials (FIM) tracked without procurement machinery | Procurement solution exists; POs arrive as ingested documents; ordering around the network | Producer-side sales orders (not procurement); marketplace for hauler capacity |
| Movement events tracked | Fabrication → shipment → gate → receipt → warehouse/laydown → transfer → issue/install; every transaction logged | Production → shipment → delivery → installation → reorder; QR scans update status; activity log | Dispatch → punch-in → loads hauled plant→site → punch-out → e-ticket |
| Receipt & exceptions | Receipting, OSD (over/short/damaged) reports with photos, assignment, status to resolution | Defect tagging with instant cross-party notification; dockets ingested | Rejected loads, delivery confirmation, dispute reduction via timestamped tickets |
| Storage/location | Warehouse & laydown yard management; custodian; mapping; geofences; heatmaps | Location/status per item/pack; on drawings/BIM; factory/warehouse/site teams | Plant vs jobsite locations; ETAs; geofence arrival/departure |
| Custody/parties | Custodian tracked; permission-based multi-stakeholder access | Multi-party network (head contractor, manufacturers, suppliers, logistics, installers) | Producer ↔ haulers ↔ customers; compliance validation of haulers |
| Consumption/progress | Issues/withdrawals; rules of credit weights per activity → earned value | Installation status; progress on drawings vs program dates | Delivered tons vs planned; delivery velocity; hauling cost by project |
| Mobile | App: find, receipt, update, issue, transfer; barcode/QR; offline | App + tablet; QR scan/stickers; offline for basements/tunnels | Trux Drive hauler app: find/accept/complete work; punch in/out |
| Auto-identification | Barcodes, RFID, GPS, Bluetooth, intrinsically safe scanners | QR code stickers/prints; AI document ingestion | GPS + driver app; scale-system integration; QR not central |
| Reporting/analytics | Advanced reporting (progress, delays, deviations); alerts on inventory levels/progress/inspections | Run-rate reports, progress graphs, dashboards; carbon reports | Delivery velocity, cycle times, utilization, tons delivered, exports for job cost/hauler pay |
| Integrations | SAP, 3PL, "multiple tracking technologies and business systems" | Procore, ACC, Power BI, Dynamics, SAP, Excel, public API | Scale systems, ERP, accounting; sales-order/dispatch-order/scale APIs |
| Distinctive extras | Rules of credit/EV; BIM digital twin; route heatmaps | Network directory; multi-language; embodied carbon/material passports; AI assistant | Hauler marketplace & payments; compliance validation; customer Delivery Tracker |

### Stable commonalities across the sample (Evidence layer B)

1. **Project-anchored material records**: identified materials with quantities exist as records in a project-wide register — discrete items/parts/lots (Track'em, Matrak) or bulk commodity quantities against orders (Trux). All three stress a single registry/database as the foundation.
2. **Recorded movement through the journey**: each system's core is the sequence of material events — fabrication/production → shipment/haul → receipt → storage → transfer/issue → installation — with the current state (location, custodian/holder, status) derivable from logged events ("logs every transaction" / "track products from production to shipment, installation" / "from dispatching to delivery").
3. **Location & status visibility**: continuous answer to "where is it and what state is it in" — via registry + app updates + (in two of three) maps/geofences, and drawings/BIM in two of three.
4. **Receipt & exception handling**: what arrives is checked against what should arrive — OSD reports (Track'em), defect tagging (Matrak), rejected loads/dispute defense via tickets (Trux).
5. **Mobile capture at the material touchpoint**: field/warehouse/factory workers scan or punch in/out on mobile; offline capability in both Australia-origin products.
6. **Audit trail**: date/time-stamped logs of every interaction with a material, positioned as dispute protection.
7. **Planned vs actual quantity comparison**: planned vs delivered tons (Trux), ordered/BOQ vs tracked progress (Matrak), inventory levels + availability-for-construction + progress deviations (Track'em).
8. **Integration outward**: ERP/accounting, project-management platforms, BIM — materials data flows to systems of cost/design rather than owning them.

### Divergences

- Material form: item-level identity (Track'em, Matrak) vs truckload/bulk quantities (Trux).
- Requirement machinery: drawing-generated BOQ (Matrak) vs requisitions/inventory levels (Track'em) vs sales orders (Trux).
- Party model: single organization + permissioned stakeholders (Track'em) vs multi-company network (Matrak) vs producer–hauler–customer triangle (Trux).
- Procurement: explicitly absent for free-issued materials (Track'em), document-ingested (Matrak), out of scope producer-side (Trux). Procurement execution is clearly NOT definitional.
- Storage depth: laydown-yard/warehouse management with custody (Track'em) vs light location/status (Matrak) vs no storage at all (Trux — material is in motion).
- Transport machinery: full hauling dispatch/GPS/e-ticketing (Trux) vs shipment status only (Matrak) vs gate/stage tracking (Track'em).
- Identity capture: barcode/RFID scanning (Track'em), QR stickers + document AI (Matrak), driver app + GPS + scale (Trux).
- Progress semantics: rules-of-credit earned value (Track'em) vs drawing-based site progress (Matrak) vs delivery velocity/tons (Trux).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

1. **Project-anchored material records with quantities** — the construction materials the project depends on exist as identified records (a commodity with spec/quantity, or a discrete item/lot) in a register. The managed population is materials, not machines, people, or contracts.
2. **Recorded material journey** — material state/quantity progresses through recorded movement events (requested/ordered → produced/shipped → received → stored → transferred/issued → installed), each leaving a trace; the current state (where it is, with whom, how much) is derivable from the records.
3. **Work anchoring** — material records and their states are tied to the project's work (orders, locations/phases, jobsites, cost objects), so material availability and consumption inform construction execution.

Rationale: remove (1) → nothing remains; remove (2) → a static materials catalog/BOM — an estimating/takeoff artifact, not materials management; remove (3) → generic warehouse inventory or a freight tracker, not construction materials management. Procurement execution, storage/stock depth, delivery scheduling, supply-chain networks, tagging technology, BIM linkage, and hauling dispatch are each absent or thin in at least one sampled pole → L1/L2.

### L1 — Common Mature Structure

- Requirement-vs-actual comparison: planned/required vs delivered/installed quantities (order-level, BOQ/MTO-level, or inventory-level depending on pole).
- Receipt processing and exception handling (over/short/damaged; defects; rejected loads) with assignment and status tracking to resolution.
- Storage/location surfaces: yards/warehouses/staging with custodian and location (where the pole includes storage).
- Mobile capture at material touchpoints: scan/update/receipt/issue; offline support in remote/basement conditions.
- Audit trail: time-stamped log of every material interaction, used for dispute resolution and accountability.
- Movement documents digitized: dockets, transfer requests, picklists, requisitions, movement tickets.
- Exception alerts and notifications (inventory levels, progress deviations, defects, delays).
- Reporting/analytics: delivered vs required, progress/run-rate, deviations, exports to cost/ERP systems.
- Integrations: ERP/accounting, project management platforms, BIM, scale/ERP APIs (hauling pole).
- Multi-party participation: permission-based access for suppliers/subcontractors/stakeholders; in one pole a full multi-company network.

### L2 — Variant / Optional Structure

- Requirement origin machinery: drawing/takeoff-generated BOQ; MTO-style material lists; sales orders.
- Procurement execution inside the product: supplier quotes/POs (one sampled product packages procurement as a separate solution line; another explicitly distinguishes procured vs free-issued).
- Identity-capture technology: barcode vs QR vs RFID vs GPS vs document-AI ingestion; intrinsically safe scanners.
- Mapping/geofencing/heatmap machinery for yards and sites.
- Hauling-execution machinery: truck dispatch, load stacking, GPS route/cycle tracking, e-ticketing, scale integration, hauler marketplace/payments/compliance (the bulk-hauling pole).
- Supply-chain network posture: shared cross-company platform, company directory, multi-language UI for overseas factories.
- Rules of credit / earned-value progress measurement over material activities (EPC practice).
- BIM/digital-twin enrichment of models with material status.
- Embodied-carbon/material-passport tracking tied to material flows.
- Regional/industry tuning: Australian resource and offsite-construction sectors vs US aggregates/asphalt vs global facade/manufacturing trades.
- ERP-embedded realization: construction ERP suites handle part of this journey through their purchasing and inventory modules — noted with reduced confidence (not directly examined in this pass).

### L3 — Vendor-specific (research notes only)

- Matrak: "Digi" AI assistant; material passports; EC3/NABERS benchmarking; network company directory; "2,000+ companies" marketing claim; specific integration list.
- Track'em: OSD report templates; "Rules of Credit" feature; group/split/bulk-fab/FIM vocabulary; intrinsically safe scanner support; "40 million items tracked" claim; Rio Tinto/AusGroup case studies.
- Trux: Trux Marketplace, Trux Pay, Trux Drive/Delivery Tracker product names; load auto-complete via paver geofence; ticket transcription; package ladder (Materials Starter/Aggregates/HMA); "$1.3B weekly hauler payments" marketing stat.

## Rejected Findings (not promoted)

- "Materials management = procurement software" — rejected: Track'em explicitly tracks free-issued (FIM) materials with no procurement; Trux's producer-side has sales orders, not purchasing; Matrak treats POs as documents to ingest. Procurement execution is L2.
- "Materials management = inventory/stock system" — rejected: the hauling pole holds no stock at all (material is in motion); storage/stock depth varies from full laydown-yard management to none. Inventory is L1/L2.
- "Materials must be discrete tagged items" — rejected: bulk commodity quantities (tons/loads) satisfy the core in the hauling pole; item-level tagging is a capture mechanism (L2).
- "Materials management requires a multi-party network" — rejected: only one sampled product is network-native; permissioned single-organization operation satisfies the core.
- "BIM linkage is definitional" — rejected: 2 of 3 sampled products; L2.
- "Rules of credit / earned value is definitional" — rejected: single product; EPC-specific practice; L2.
- "Delivery appointment scheduling (windows/docks) is a core capability" — rejected from the core: not directly evidenced in the sampled products' fetched pages (the GC field-delivery pole that would evidence it was unreachable); delivery timing appears only as planned load times/velocity in the hauling pole. Kept out of L1 to avoid speculation.

## Historical / Market-Sample Check (per workflow §24)

Pre-digital and pre-cloud practice for construction materials:
- Receiving logs + paper delivery dockets (recorded movements onto site) ✓
- Stock/bin cards in the yard or warehouse (material records with quantities, on-hand state) ✓
- Materials requisition slips and issue tickets charged to job numbers (movement events anchored to work/cost objects) ✓
- Paper load tickets at the scale for bulk hauling (movement + quantity + job) ✓
- Yard layouts/chalkboards and foreman knowledge for location (location state, however informal) ✓
- Procurement lived on paper POs; BOM/BOQ lived on paper takeoffs — none of it needs to be in the system for the three L0 structures to exist.
→ L0 survives the historical check. Requirement comparison existed as the paper BOQ/stock-card reconciliation; the modern software versions (AI takeoff, live dashboards, networks, QR, GPS) are L1/L2. Older ERP-embedded purchasing/inventory modules tied to job numbers also satisfy the core.

## Boundary Findings

| Neighboring Type | Distinction | "Remove what → becomes the other" |
|---|---|---|
| Construction Equipment Management (§17) | materials are consumed into the work; machines are durable, metered, reusable assets with hours/utilization (seam drawn in the equipment pass). Equipment platforms carry a small materials/consumables slice as an adjacent population. | Records become metered reusable machines with hours/allocation → equipment management. |
| Inventory Management System (§10) | generic inventory serves standing operations (replenishment, on-hand optimization); construction materials management is project-anchored and consumption-into-work driven. | Remove the project/work anchoring and journey-to-installation; manage standing stock for its own sake → inventory management. |
| Procurement Management / Purchase Order Management (§10) | procurement manages the buying transaction lifecycle; materials management manages the physical material after/around it. Free-issued materials and producer-side flows show the Type works without procurement in-system. | Keep only the buying transaction; drop physical journey tracking → procurement/PO management. |
| Warehouse Management System (§10) | WMS optimizes warehouse operations (bins, picking, labor); materials management spans supplier→site→installation with yards as one surface. Laydown-yard management here is location/custody tracking, not WMS operations. | Primary object becomes warehouse throughput and bin operations → WMS. |
| Transportation Management System / Dispatch Management (§18) | the hauling pole (Trux) shows real overlap: trucks, GPS, dispatch, e-tickets. The seam: the primary object of record is the material quantity (tons delivered vs ordered) with trucks as machinery. | Primary object becomes trucks/carriers/routes and carrier compliance; material becomes cargo → TMS/dispatch. |
| Construction Field Management / Daily Log (§17) | deliveries and material events can appear in the daily site record; there the day is the record, here the material is the record. | Primary object becomes the day's site activity → field management/daily log. |
| Quantity Takeoff / Construction Estimating (§17) | takeoff/estimating produce required quantities pre-award; materials management consumes those requirements and tracks actual materials post-award (Matrak generates BOQs from drawings as input). | Only the quantity measurement/pricing of unawarded work remains → takeoff/estimating. |
| Submittal Management (§17) | submittals approve product data/specimen before purchase; materials management tracks the physical material regardless of approval flow. | Primary object becomes the approval package → submittal management. |
| Construction Cost Management (§17) | material cost flows to cost control via commitments/invoices; materials management records physical quantities and hands off via integrations/job-cost codes. | Primary object becomes budget/commitment/actual cost → cost management. |
| Tool Management (§16) | tools are small durable reusable assets; materials are consumed. | Population becomes reusable small tools → tool management. |
| Grain Management / bulk commodity handling (§20) | bulk quantity logistics exists in agriculture too, but industry semantics (elevators, contracts, blending) differ. | Industry population/semantics change → grain/agriculture Types. |
| Construction Project Management (§17) | PM runs the project (schedule, commitments, changes); materials management runs the material population serving it. | Primary object becomes the project schedule/contract → project management. |

## Uncertainties

- The GC field-side delivery-management pole (StruxHub) and the materials-procurement pole (Kojo) were unreachable; delivery-request/appointment and supplier-quote-comparison machinery are therefore weakly evidenced and excluded from the core. If a future pass reaches them, the L1 list may grow a delivery-scheduling item.
- Hexagon Smart Materials (the classic EPC material-control suite) unreachable; EPC practices are evidenced via Track'em only. No claims are made about any specific EPC suite.
- ERP-embedded materials modules not examined; their exact capabilities (job-charged POs, receipts, issues inside construction ERPs) are inferred only from general market structure and are marked reduced-confidence.
- Whether requirement comparison is definitional was consciously resolved as L1: 3/3 products show it, but a delivery-logging-only product is still recognizable as materials tracking; historical receiving logs + bin cards satisfy the core without a live BOQ comparison.
- Cross-company network effects (Matrak) vs single-org permissioning (Track'em) vs producer-customer triangle (Trux): the market spread is real but only three products were sampled; no claim is made about market shares.
- Trux's classification inside this Type is a judgment call: it markets as logistics software, but its system of record is material quantity against orders/jobs (planned vs ticketed vs delivered tons), which is the materials ledger. Documented as a pole with the TMS boundary noted; flagged as a watch-item for the Dispatch Management/TMS pass.

## Final Synthesis

Construction Materials Management is the project-side system of record for physical construction materials. Its defining core is small: material records with quantities (bulk commodities or discrete items) anchored to the project; a recorded journey of those materials (ordered/produced → shipped/hauled → received → stored → issued/installed) from which current state — where, with whom, how much — is derivable; and the anchoring of material state to the work (orders, locations, jobs, cost objects) so availability and consumption inform execution. Around that core, mature products add requirement-vs-actual comparison, receipt and exception handling (over/short/damaged, defects), storage/custody surfaces for yards and warehouses, mobile scan/update capture with offline support, a time-stamped audit trail positioned as dispute protection, digitized movement documents, alerts, reporting, and integrations to ERP/project-management/BIM. The market realizes the Type through poles — formal material control for capital projects, supply-chain network tracking across manufacturers and installers, bulk hauling logistics for producers and civil contractors, plus adjacent realizations inside equipment platforms and construction ERPs — each emphasizing one part of the journey while keeping the same skeleton. Procurement execution, stock depth, tagging technology, networks, and hauling machinery are all real but non-definitional: free-issued materials, in-motion-only bulk flows, and paper-era dockets/stock cards/job-charged requisition slips all satisfy the core.
