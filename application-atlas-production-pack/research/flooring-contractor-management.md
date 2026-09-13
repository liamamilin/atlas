# Research Notes — Flooring Contractor Management

## Research Goal

Understand what business-management software for flooring businesses (floor-covering dealers, flooring contractors/installers) actually is: its system of record, its trade-specific structures, its canonical workflow, and its boundaries against horizontal field-service management, construction estimating/project tools, and inventory/distribution systems.

## Initial Boundary

Working hypothesis at start:

- **What it is**: operator-side business management system for a flooring business — the software of record for customers, jobs, measurement/estimating, material sourcing, installation scheduling, and billing.
- **Primary users**: flooring dealer/contractor staff — salespeople/estimators, office coordinators, installers/crews, warehouse staff, owner/bookkeeper.
- **Nearest Types**: Small Business Field Service Management (§29 sibling), Home Improvement Contractor Management (§29 sibling), Construction Estimating / Quantity Takeoff (§17), Construction Project Management (§17), Inventory Management System (§10), Appointment-based Service Business Management / Retail POS (§29/§05).
- **Suspected boundary risk**: the leaf may be "just" a trade skin of field-service management (the pattern found for electrical/cleaning/appliance-repair siblings), OR it may have a genuinely stronger vertical structure (flooring has its own ERP vendors, its own measurement-software category, and its own B2B data standard).
- **Unknowns**: does flooring-specific software have structures horizontal FSM lacks? Is measurement definitional or a bundled capability? How do retail-showroom and installation-contractor poles mix?

## Research Questions

1. What is the unit of work — job, order, project? What lifecycle does it carry?
2. What role does measurement/takeoff play, and is it inside the system or a separate tool?
3. How is material handled — catalog, inventory (rolls/boxes/dye lots), purchase orders, B2B vendor exchange?
4. How is installation scheduled and executed? What does the installer see?
5. How does money flow — deposits, invoicing, vendor invoices, installer pay, commissions, job costing, accounting?
6. What business segments do the products serve (residential retail, commercial contract, builder/multi-family, distribution)?
7. Do horizontal FSM products serve flooring, and with what structural difference?
8. Where is the seam to Construction Estimating / Quantity Takeoff and to distribution/wholesale?

## Representative Products

| Product | Pole | Tier sampled | Why selected |
|---|---|---|---|
| QFloors | flooring dealer business management (SMB→enterprise) | Tier 1/2 — root, business-management, product, estimation pages | most-cited flooring-specific management suite; rich feature pages |
| Comp-U-Floor | flooring ERP (cloud/web/mobile) | Tier 2 — home + ERP product page | most explicit end-to-end workflow statement of the three verticals |
| RFMS (Cyncly) | flooring ERP (dealer/enterprise; residential/commercial/builder/manufacturer) | Tier 2 — root page only (subpages 404) | industry-leading flooring ERP family; positioning-level evidence |
| Measure Square | flooring takeoff/estimating specialist (+CRM) | Tier 2 — root page + QFloors partnership page | the measurement-specialist pole; shows measurement as a distinct product category |
| Service Fusion | horizontal FSM control | Tier 2 — root page | control pole: generic FSM spine + industry list observed to exclude flooring |

Rejected candidates: Jobber (403 ×2 across passes), Housecall Pro flooring page (403), Service Fusion flooring-specific URL (404 — root used instead), Comp-U-Floor www host (transport error — non-www host used).

## Sources

All fetched 2026-09-08:

- QFloors — https://www.qfloors.com/ (root), /business-management-software/, /qfloors/, /floor-covering-estimation/
- Comp-U-Floor — https://comp-u-floor.com/ (root), /flooring-software-products/comp-u-floor-erp/
- RFMS / Cyncly — https://www.rfms.com/ (root only; /products/* and /industries/flooring/* returned 404)
- Measure Square — https://measuresquare.com/ (root)
- Service Fusion — https://www.servicefusion.com/ (root)

**Source-access limitation**: no Tier-1 help-center/user-guide content was reachable for any product (QFloors support portal is login-gated; RFMS subpages 404; Jobber/Housecall Pro 403). All evidence is Tier-2 official product pages. Assertion strength is calibrated accordingly: structural claims rest on multiple independent vendor pages agreeing; precise operational details (exact statuses, field names, limits, defaults) are not stated and are not inferred from model memory.

## Product Observations

### QFloors (flooring dealer management; SMB → enterprise)

Evidence layer: A (directly observed on official pages).

- Positioning: "complete, flooring-specific business management solution" for floor-covering dealers; scales from small shops to multi-location enterprise; "six main screens" design philosophy.
- Main screens named on root page: Leads; Customer Invoices ("filling out a sales order… quickly add line items for material & labor, produce work orders, and schedule jobs"); Job Costing ("instantly job cost on the same screen as your sales invoice"); Inventory ("in stock, out of stock, and what's on order… create, track, and manage POs"); Vendor Invoicing ("assigning costs to sales orders"); Checkbook; Accounting (GL functions, bookkeeping, real-time financial reports); Reports ("commissions, contract labor, inventory, sales tax, profitability").
- Package list (business-management page): Customer Proposals & Invoices; Instant Job Costing; Product Catalog/FCB2B (advanced); Inventory Management (advanced); Fully Integrated Accounting; Vendor Invoicing; Checkbook; Built-in CRM/Lead Tracking; Advanced Reporting; User Permissions; Commercial Flooring Module; Multi-Family Housing Options; Builder/Construction; Integrated Credit Card Processing; MeasureSquare Estimation Software (Enterprise); Advanced QSched Scheduling (Enterprise); add-ons: QTagger (showroom pricing), Installer View (installer calendar), Account View (customer account access), QOrders (multi-family orders), QLeads, QReporter, QSched (job scheduling), Document Manager; e-signature product.
- Estimation page (Measure Square partnership): bluetooth laser measure; "instantly estimate product quantities, directions, and seam layouts"; capture room photos, floor conditions, customer approval signatures on the spot; 2D/3D layouts; seam placement options; pattern matching; drag-and-drop product switching; automatic waste/cut optimization; tile pattern designer; import "quantity, cost, and bid information from Measure Square into QFloors to automatically populate sales orders"; attach seam diagrams/cut sheets to Document Manager; installers receive seam placement, direction, cut sheets; commercial desktop: import blueprints (100+ pages), estimate by floor/installation phase/project, per-product waste percentages.
- Industries poles: Residential, Commercial, Builder, Multi-family, Mobile Showroom, Distribution (wholesale).

### Comp-U-Floor (flooring ERP; cloud/web/mobile)

Evidence layer: A (directly observed on official pages).

- Homepage workflow statement ("Simplify Your Flooring Work-Flow"), in order: TAKE MEASUREMENTS → QUOTE & CLOSE THE SALE → TAKE PAYMENTS → EFFICIENT MATERIAL ALLOCATION → PURCHASE ORDER PROCESSING (B2B) → SCHEDULE & MONITOR INSTALLATIONS (Mobile) → INVOICE SATISFIED CUSTOMERS → CONVERT LEADS INTO PROSPECTS.
- ERP page modules:
  - CRM: Lead Tracking → Lead Qualification ("convert leads into prospects") → Prospect Management ("essential stages of product selection and estimating") → Quote Preparation → Sales Order Conversion ("turn quotes into sales order jobs").
  - Point of Sale: showroom/warehouse cash-and-carry; charges to sub-contractors and tile setters with open accounts; pick-ticket printed at warehouse.
  - Sales Order Processing / Shop At Home: "One-Step" — floor estimate + quote + close sale + credit-card deposit payment in one step at the client's home or showroom; B2B technology for instant inventory stock checks; option to create purchase orders "as needed by the customer install requirements".
  - Purchase Order Processing: on-demand POs "linked to the original sales ticket"; material receipt alerts the organization via internal line-status messages; fcB2B electronic POs to major vendors/distributors.
  - Installation Management: installation labor lines processed within the sales order; schedule, monitor progress, job cost, pay installers, invoice completed jobs; Google Calendar interface alerts installers on newly scheduled jobs; installers verify assignments, confirm availability, get directions; HQ sees status (in progress, completed); two-way Installers App (documents, job-site photos).
  - Installer Mobile App: alerts to new work orders; review details including diagrams/pictures; integrated Google Calendar and maps; optional field payments; upload job-site pictures; mark job complete/in progress.
  - Inventory Control: integrated with sales/purchases/financial/accounting; audit trails, reordering, wireless, bar coding; "Dye-lots and shades are available as required by the floor covering industry."
  - Warehouse Management: daily reports alert on sales orders to be shipped and installations to be scheduled; wireless barcode for inventory, physical inventory, sales order shipping, "roll cutting", PO receiving.
  - fcB2B: online price catalogs and periodic updates; electronic POs and stock-available inquiries; vendor electronic invoices matched and reconciled against POs.
  - Multi-Location: multi-company/multi-location; receiving/drop-ship warehouses; installation crews assigned to multiple locations.
  - Finance & Accounting: AR, AP, cash reconciliation, bank reconciliation, GL; "no manual journal entries".
  - Sales Analysis & Reporting: profitability, sales commissions, daily sales logs.
- Other products: Flooring Business CRM; fcB2B; Dealer Portal; QR Code Pricing; Mobile Flooring Showroom/Shop at Home; Wireless Warehousing; Flooring Service Management (separate service/repair product); industries: Residential, Commercial, Builder, Multi-family, Mobile Showroom, Distribution.
- Positioning copy: "ultimate management software for the flooring and remodeling industries"; installer/scheduler mobile app described as replacing "work orders and paperwork trails".

### RFMS / Cyncly (flooring ERP family)

Evidence layer: A for positioning only (root page); subpages unreachable.

- Root page product family (flooring): RFMS ERP ("Unified flooring operations"), Measure Desktop ("Enhance flooring efficiency"), JobRunner ("Manage flooring bids, projects, and finances").
- Flooring industries served: "Flooring businesses serving the builder market", "commercial market", "Residential flooring dealers and installers", "Flooring manufacturers".
- RFMS is part of Cyncly (design/CPQ/ERP software group spanning kitchen/furniture/flooring/windows).
- Limitation: /products/rfms-core, /products/rfms-core/capabilities, /products/measure-desktop, /products/job-runner (with and without trailing slash), and the residential-flooring industry page all returned 404. Module-level structure unverified; RFMS is used as market-structure/positioning evidence only.

### Measure Square (flooring takeoff/estimating specialist)

Evidence layer: A (directly observed on official pages, incl. the QFloors partnership page).

- Products: MeasureSquare 8 (desktop takeoff/estimating: "estimate all types of flooring, including carpet, sheet vinyl, tile, and hardwood"; "generate detailed reports, bid proposals, POs, and WOs in minutes"); MeasureSquare Mobile (on-site measure/estimate/quote; seam diagrams, tile layouts, 3D models); MeasureSquare CRM (contract flooring: takeoff → estimating → sales bid → job costing; "manage installation schedules, job costing, and SOVs (schedule of values), while tracking real-time profitability"); MeasureSquare Cloud; Room Scanner; Stone & Tile edition; AI positioning.
- Trades: Commercial Flooring, Residential Flooring, Multi-Family Flooring (core), plus Countertops, Stone & Tile, Commercial Cleaning, Landscaping, HVAC, Electrical, Security (adjacent takeoff trades).
- Via QFloors page: laser-measure capture; quantities/directions/seam layouts; room photos, floor conditions, customer approval signatures; waste/cut optimization; pattern matching; blueprint import (100+ pages); estimate by floor/phase/project; per-product waste percentages; quantities/costs/bids flow into the management system's sales orders; seam diagrams/cut sheets attach to job documents.
- Customer testimony (Flooring Liquidators): sales members and installers measure; measurements shared with installers, warehouse, and scheduling departments.

### Service Fusion (horizontal FSM — control pole)

Evidence layer: A (directly observed on official root page).

- Generic FSM spine: Create & Assign Jobs (work orders, drag-drop schedule, assign to technicians) → Dispatch & Send Reminders → Track Status; estimates convert to work orders; invoicing auto-generated from completed jobs incl. materials/labor/taxes; technician mobile app; GPS; customer management.
- Industries list observed on root page (~29 trades): HVAC, plumbing, electrical, appliance repair, garage door, locksmith, irrigation, pool, remodeling, cleaning, solar, water treatment, landscape, air duct, painting, alarm, septic, roofing, gutter, handyman, carpet cleaning, commercial food, chimney sweep, tree care, carpentry, snow removal, window cleaning, pressure washing, concrete.
- **Flooring is absent from the industry list** (carpet cleaning is present; flooring installation is not). Negative/market-structure observation: flooring is served by its own vertical software ecosystem rather than as a horizontal-FSM industry skin.

## Cross-product Comparison

| Structure | QFloors | Comp-U-Floor | RFMS | Measure Square | Service Fusion (control) |
|---|---|---|---|---|---|
| Customer/lead → quote → sales order (job) | ✓ (Leads; sales order; proposals) | ✓ (CRM stages → "sales order jobs") | ✓ (JobRunner bids/projects) | ✓ (CRM leads → bid/quote) | ✓ (generic jobs/estimates) |
| Material & labor as distinct sale lines | ✓ ("line items for material & labor") | ✓ (installation labor lines within sales order) | positioning-level | ✓ (product + labor costs in estimates) | partial (materials on invoices, no trade semantics) |
| Measurement/takeoff producing quantities | ✓ (bundled Measure Square; quantities populate sales orders) | ✓ ("TAKE MEASUREMENTS" step 1; MeasureSquare partnership) | ✓ (Measure Desktop product) | ✓ (core product) | ✗ |
| Stock inventory with trade semantics (dye lots/shades, roll cutting) | ✓ (inventory mgmt advanced) | ✓ (dye-lots/shades; roll cutting; barcode) | positioning-level | ✗ (not its layer) | ✗ |
| POs linked to the job; vendor invoice matching | ✓ (PO management; vendor invoicing assigned to sales orders) | ✓ (POs linked to sales ticket; fcB2B invoice match) | positioning-level | partial (generates POs/WOs) | ✗ (generic purchasing absent) |
| B2B product catalog / electronic vendor exchange | ✓ (Product Catalog/FCB2B) | ✓ (fcB2B) | positioning-level | partial (API/B2B inventory integrations) | ✗ |
| Installation scheduling + installer app | ✓ (Installer View; QSched) | ✓ (Google Calendar alerts; two-way Installers App) | positioning-level | ✓ (CRM installation schedules) | ✓ (generic technician app) |
| Job costing on the order | ✓ ("instantly job cost on the same screen") | ✓ (job cost within installation mgmt) | positioning-level | ✓ (real-time profitability) | partial (generic reporting) |
| Deposits / field payments | ✓ (credit card processing) | ✓ (deposit in one-step sale; optional field payments) | positioning-level | ✓ (quote/close onsite) | ✓ (generic) |
| Installer/contract-labor pay + sales commissions | ✓ (commission & contract labor reporting) | ✓ (pay installers; commissions) | positioning-level | ✗ | ✗ |
| Built-in accounting (GL/AP/AR) or sync | ✓ (fully integrated accounting; checkbook) | ✓ (AR/AP/GL/bank rec) | positioning-level | ✗ (accounting integrations) | partial (QuickBooks sync) |
| Showroom POS / cash-and-carry | ✓ (QTagger showroom pricing) | ✓ (POS module) | positioning-level | ✗ | ✗ |
| Segments: residential / commercial / builder / multi-family / distribution | ✓ all six poles | ✓ all six poles | ✓ (builder/commercial/residential/manufacturer) | ✓ (commercial/residential/multi-family) | ✗ (no flooring) |

Reading: the three vertical management products agree on a common spine (lead → measure → quote/sale → material sourcing → installation → billing → costing/accounting) with flooring-specific semantics (measured quantities, material/labor split, dye-lot inventory, PO-to-job linkage, installer execution). Measure Square isolates the measurement layer as a product category of its own. Service Fusion shows the generic FSM spine without any of the flooring semantics — and does not even list flooring among its industries.

## Canonical Model

### L0 — Defining Invariant (minimal)

A flooring contractor management system is the operator-side business system of record for a flooring business. Its defining core is five jointly-held structures:

1. **The flooring job of record** — a persistent, individually identified job for a customer at a site, carrying both material and labor components, moving through a managed lifecycle (quoted → sold → fulfilled → billed). Remove → CRM + accounting with no trade operation.
2. **The measured-area quantity basis** — the job's material (and typically labor) content is quantified from measurements of the spaces to be floored, priced against a product catalog; quantities are captured directly or imported from a measuring/takeoff tool and flow into the job. Remove → generic field-service job with no trade quantity semantics.
3. **Material sourcing and allocation** — the material line is fulfilled from the business's own stock or by ordering from vendors/distributors (purchase orders linked to the job), tracked from order through receipt to allocation to the job. Remove → labor-only scheduling tool; the vertical's reason for being disappears.
4. **Installation execution** — the on-site installation is scheduled to installers/crews, tracked through status to completion. Remove → material/order system with no field operation (distribution territory).
5. **Money resolution against the job** — customer billing (deposits, invoices) plus cost capture (vendor invoices, installer/contract-labor pay, sales commissions, job costing) recorded against the job. Remove → measuring/quoting tool with no business operation.

Jointly-held is load-bearing:
- 1+2 without 3+4+5 = estimating/takeoff tool (Measure-Square-without-CRM territory → Quantity Takeoff / Construction Estimating).
- 1+3+4+5 without 2 = generic FSM with material lines (Service-Fusion-style → Small Business Field Service Management).
- 2+3 without 1+4+5 = catalog/inventory system (distributor territory).
- 1+4+5 without 2+3 = generic FSM.

### L1 — Common Mature Structure (not definitional)

- CRM/lead tracking with lead → prospect → quote stages (all three verticals).
- Product catalog with vendor pricing; B2B electronic catalogs and PO/invoice exchange (fcB2B-class).
- Installer mobile app: job alerts, work-order details with diagrams/cut sheets, directions, status updates (in progress/complete), photos, optional field payments.
- Customer-facing machinery: proposals, e-signature/approvals, notifications, customer account access.
- Showroom POS / cash-and-carry sales; showroom pricing tags.
- Shop-at-home / mobile-showroom selling (in-home measure + quote + close + deposit).
- Warehouse management: barcode/wireless receiving, shipping, roll cutting, physical inventory.
- Multi-location / multi-warehouse / crew assignment across locations.
- Reporting: sales, commissions, contract labor, inventory, sales tax, profitability.
- Credit-card processing integration; document management (seam diagrams, cut sheets, photos).
- Accounting: built-in GL/AP/AR or sync to external accounting.

### L2 — Variant / Optional Structure

- Segment poles: residential retail dealer (showroom + shop-at-home) / commercial contract flooring (blueprint takeoff, bids, phases, SOVs) / builder & multi-family (project/tract work, order hierarchies) / distribution (wholesale — sell material without installation).
- Measurement tooling: integrated module vs specialist product (Measure Square, RFMS Measure Desktop) vs manual entry; laser measures, room scanners.
- Installation labor model: in-house crews vs subcontracted installers (open accounts for sub-contractors/tile setters observed in one product).
- Accounting posture: built-in full accounting vs external sync.
- Service/repair work as a side product (warranty/service calls) — separate module in one product.
- Regional/industry infrastructure: fcB2B as the North American floor-covering B2B data exchange (regional marker).
- AI assistance (current-gen, one vendor's positioning).
- Franchise/big-box/chain scale (multi-location enterprise tier).

### L3 — Vendor-specific (kept out of the final document)

- QFloors: six-screen design philosophy; QTagger, Roomvo bundles, QOrders, QReporter, QSched, Installer View, Account View naming; published price points.
- Comp-U-Floor: "One-Step Competitive Advantage"; Wireless Warehousing; QR Code Pricing; Pensoft/Paragon partnerships; AnyDesk support.
- RFMS/Cyncly: Measure Desktop, JobRunner product names; Cyncly cross-industry ecosystem; portal/ROS account surfaces.
- Measure Square: Stone & Tile edition; Room Scanner; Udemy classes; Facebook user group; AI branding.

### Historical / Market-Sample Check (§24)

- Paper-era flooring dealer practice — tape measure + sketch, estimate pad, signed ticket, PO phoned to the distributor, installer schedule board, invoice, commission sheet — satisfies all five L0 structures without any software. The definition does not depend on cloud, mobile apps, laser measures, or B2B exchange.
- The vertical products themselves are long-lived (customer testimonials reference continuous use since 2003/2004/2005), so the structure is not a current-era artifact.
- The measurement basis is era-robust: tape-and-paper satisfies "measured-area quantity basis captured directly"; laser/LiDAR tools are implementations, not the invariant.
- Older/regional check: fcB2B is regional (North America) and is held at L2, not L0. ✓

## Vendor-specific / Rejected Findings

- **Rejected as definitional**: built-in accounting (one product ships it fully; others sync) — L1. Showroom POS — L1/L2 (segment-dependent). B2B electronic exchange (fcB2B) — L2 (regional infrastructure; the invariant is "POs linked to the job", not the electronic standard). Installer mobile app — L1 (paper-era practice satisfies L0 without it). AI — L2/L3.
- **Rejected claims**: none of the sampled marketing numbers (productivity %, review counts, price points) are carried into the canonical model.
- **Product Mismatch check**: Measure Square is not itself a full management system (no stock inventory, no vendor-invoice matching in its core) — it is the measurement-specialist pole and is treated as a capability supplier to the Type, not as the Type's center. Service Fusion is the control, not a member.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling, unprocessed)**: the generic spine (customer+site → job → technician → invoice) is shared. The seam is the flooring trade semantics: measured-area quantity basis + material sourcing/allocation (stock, dye-lots, POs linked to jobs) + dealer-style sale (material+labor quote, deposits). Market-structure evidence: the sampled horizontal FSM vendor's industry list (~29 trades) excludes flooring; flooring is served by a dedicated vertical ecosystem (management ERPs + measurement specialists + a B2B data standard). A labor-only flooring installer running generic FSM is a boundary pole — for that pole the relationship is probably trade-Variant (consistent with the electrical/cleaning/appliance passes' convention); for the dealer/contractor vertical documented here, the structures are distinct. Flag for joint review when Small Business Field Service Management is processed.
2. **vs Home Improvement Contractor Management (§29 sibling, unprocessed)**: one sampled vendor positions itself for "the flooring and remodeling industries" — overlap acknowledged. The seam is the flooring-specific structures (measured-area basis, dye-lot/roll inventory, fcB2B, installer-calendar semantics); home-improvement is the generalist pole.
3. **vs Construction Estimating / Quantity Takeoff (§17)**: the measurement layer IS flooring takeoff — Measure Square is essentially a flooring takeoff product, and commercial-flooring takeoff imports blueprints and produces bid proposals. The seam: takeoff/estimating alone (no job of record, no material sourcing, no installation execution, no billing) is a tool the Type consumes. research/construction-estimating.md already records per-trade specialization pages including flooring — cross-reference recorded.
4. **vs Construction Project Management (§17)**: the commercial contract pole (large projects, phases, SOVs, bid workflows) drifts toward construction project machinery. The dealer-retail core (showroom, stock, consumer sale, deposits) is not construction. Seam: project-based contract work vs ongoing dealer business operation.
5. **vs Inventory Management System / distribution (§10/§05)**: the distribution pole (wholesale floor-covering distributor) uses the same products but without installation execution and with a different money model. The contractor Type requires installation execution; distribution is a variant pole of the same product family, not of this Type.
6. **vs Retail POS / Appointment-based Service Business Management (§05/§29)**: showroom cash-and-carry POS is a capability inside the Type; standalone POS or appointment-book systems lack the job/material/installation structures.
7. **Taxonomy note**: the leaf sits among §29 trade business-management leaves. Flooring shows an unusually strong vertical ecosystem (own ERP vendors, own measurement-software category, own B2B standard) — stronger than the electrical/cleaning siblings — but the defining core remains the trade instantiation of the shared family pattern (customer+site → job → execution → billing) with flooring semantics. Keep as its own leaf; record the stronger-verticality observation.

## Uncertainties

- RFMS module-level structure unverified (subpages 404); RFMS evidence is positioning-level. The L0 does not depend on it (three other products carry the structure), but RFMS-specific claims are avoided in the final document.
- No Tier-1 help-center documentation reached for any product; all workflow claims are Tier-2 (official product pages). Multiple independent vendor pages agree on the spine, which raises confidence, but exact statuses, field names, limits, and defaults are not asserted.
- The "labor-only installer on horizontal FSM" pole is inferred from the horizontal product's generic structure plus the absence of flooring from its industry list — not from a flooring-specific horizontal page (Jobber/Housecall Pro flooring pages 403).
- Regional coverage: all sampled verticals are North American; fcB2B is a North American standard. European/Asian flooring software not sampled — regional variants unverified.
- Warranty/service-call handling observed as a separate product in one vendor only — held as optional, not definitional.

## Final Synthesis

Flooring Contractor Management is the flooring trade's business system of record. Its defining core is the jointly-held five: the flooring job of record (customer+site, material+labor, quoted→sold→fulfilled→billed), the measured-area quantity basis (quantities derived from measurements of the space, priced from a product catalog, captured or imported), material sourcing and allocation (stock or PO-linked vendor ordering, dye-lot/roll semantics), installation execution (scheduled installers/crews tracked to completion), and money resolution against the job (deposits/invoices, vendor invoices, installer pay, commissions, job costing). The market realization is a dedicated vertical ecosystem — dealer-management suites, flooring ERPs, and a measurement-specialist category feeding quantities into the job — while horizontal FSM serves only the labor-only boundary pole. The canonical loop: lead → measure → quote → close (deposit) → source material (stock check → PO → receive → allocate) → schedule installation → install (status/photos) → invoice → job costing/commissions/accounting.
