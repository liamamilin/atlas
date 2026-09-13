# Research Notes — Manufacturing Traceability

## Research Goal

Determine what Manufacturing Traceability is as a distinct Application Type: what core objects and structures define it, who uses it, how traceability work actually flows (capture → record → trace → respond), and where its boundaries lie against the dense cluster of neighboring manufacturing leaves (Manufacturing Execution System / MES, Manufacturing QMS, Manufacturing ERP, Inventory Management / WMS, SPC, Inspection & Metrology) and against the already-processed §20 food leaves (Food Traceability Platform, Food Recall Management).

This leaf carries a joint-review obligation recorded by the already-processed sibling leaf `manufacturing-execution-system-mes` (2026-09-09): "manufacturing-traceability pass should ratify genealogy-without-execution vs execution-produced-record." This pass must draw that seam from the traceability side and record agreement or disagreement.

## Initial Boundary (working hypothesis, pre-research)

- Core use: recording which lots/serials went into which products and where products went, so the manufacturer can answer "what is in this unit?" and "what else is affected?" — for quality investigations, recalls, audits, and customer/regulatory documentation.
- Likely users: quality engineers/managers, production staff capturing events, compliance/regulatory staff, customer service/warranty.
- Likely nearest neighbors: MES (produces the as-built record as a byproduct of execution), Manufacturing QMS (quality system of record; links to lots but does not own genealogy), Food Traceability Platform (supply-chain movement ledger), Food Recall Management (recall-event machinery), ERP/inventory lot tracking (movement grain).
- Unknowns: is material genealogy (lot→unit links) definitional, or is unit-bound record + trace retrieval the deeper invariant (test-data traceability products have no material genealogy)? Is response machinery (holds/quarantine/recall scoping) core or common? Does the definition survive the paper-traveler era? Where is the seam vs inventory-grain lot tracking?

## Research Questions

1. What is the tracked unit (lot, batch, serial) and what identity machinery exists (numbering, labeling, assignment rules)?
2. What is recorded against the unit (events, data), by what capture mechanisms, and with what retention?
3. What does a trace look like — query inputs, returned structure (tree/list/scope), backward and forward reach?
4. What triggers a trace (complaint, defect spill, recall, audit, customer request) and what does the loop produce (scope of affected units, documentation)?
5. What response machinery exists (holds, quarantine, disposition, mock recalls) and is it definitional?
6. Where does traceability live in the market (standalone product, MES module, QMS module, ERP feature) and what is the center of gravity in each?
7. Which rules matter (mandatory assignment, uniqueness, removal strategies, provenance)?
8. Where are the seams vs MES, QMS, ERP/inventory lot tracking, food traceability, recall management?
9. Would the definition survive the paper-traveler factory and older/regional products (historical/market-sample check)?

## Representative Products

Chosen for market representativeness, documentation accessibility, different product philosophies, and different customer tiers. Several first candidates were reduced by fetch failures — see Sources.

| Product | Pole | Tier / industries | Evidence quality |
|---|---|---|---|
| ParityFactory (Advantive) | traceability-first food & beverage WMS/MES; recall readiness as headline | mid-market food & bev processors | good (official product page, fresh fetch) |
| Sciemetric QualityWorX (Nordson) | serialized test-data / birth-history traceability for discrete assembly; quality-spill containment | automotive/powertrain, medical device, EV, aerospace MRO | excellent (official product + traceability + quality-spill pages, fresh fetch) |
| Odoo (Inventory + Manufacturing) | integrated-ERP minimal pole: lot/serial tracking at inventory/MO grain with traceability report | SMB → mid-market, all industries | excellent (official user docs, fresh fetch) |
| Siemens Opcenter (carried) | enterprise MOM suite; traceability as MES capability + industry-packaged eDHR/eBR/electronics genealogy | large enterprise, regulated + electronics | good (official pages fetched in sibling MES pass 2026-09-09, carried evidence) |
| Tulip (carried, boundary witness) | composable frontline platform keeping "unit-level traceability" while ERP/MES own orders/BOM/inventory | mid-market → enterprise | good (official integration doc from sibling pass) |

Rejected / unreachable samples this pass: Siemens Opcenter Traceability dedicated product page (404 ×2 on both URL patterns), SAP Digital Manufacturing help portal (JS shell, empty), Aegis FactoryLogix (aegis.com is an unrelated security firm; aegisish.com transport error), CAT Squared (transport error), Katana (transport error ×2), TrakSYS (traksys.com is an unrelated music-store POS vendor). Consequence: the dedicated enterprise traceability-product pole (Opcenter Traceability, Aegis) is under-sampled; the enterprise leg rests on the carried Siemens Opcenter MES-family evidence and on the MES pass's own boundary statement.

## Sources

Fetched fresh this pass (2026-09-09):

- Advantive / ParityFactory — "ParityFactory: Intelligent traceability for food and beverage manufacturers" (WMS & MES product page): https://www.advantive.com/products/parityfactory/ (fetched as https://www.parityfactory.com/, canonical Advantive page)
- Sciemetric — QualityWorX Suite product page: https://www.sciemetric.com/products/qualityworx
- Sciemetric — "Trace Parts by Serial Number | Manufacturing Traceability": https://www.sciemetric.com/manufacturing-analytics/part-traceability
- Sciemetric — "Manage Quality Spills, Avoid Mass Recalls": https://www.sciemetric.com/manufacturing-analytics/manage-quality-spill
- Sciemetric — homepage (positioning, industries): https://www.sciemetric.com/
- Odoo 19.0 user documentation — "Lot numbers": https://www.odoo.com/documentation/latest/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html
- Odoo 19.0 user documentation — "Manufacture with lots and serial numbers": https://www.odoo.com/documentation/latest/applications/inventory_and_mrp/manufacturing/workflows/manufacture_lots_serials.html

Carried from the sibling pass `manufacturing-execution-system-mes` (fetched 2026-09-09, documented in its research notes):

- Siemens — Opcenter Execution (MES family page, incl. "Production tracking" capability with forward/backward traceability; industry families incl. eDHR/eBR/Electronics): https://www.siemens.com/en-us/products/opcenter/execution/
- Tulip — "Plan an integration between Tulip and an MES or ERP" (system-of-record split; Tulip keeps frontline context + unit-level traceability): https://support.tulip.co/docs/plan-an-integration-between-tulip-and-an-mes-or-erp

Carried from other processed leaves (documented in their research notes / STATUS entries):

- food-traceability-platform (§20, processed 2026-09-08) — "the food supply chain's standing lot-level movement ledger"
- food-recall-management (§20, processed 2026-09-08) — "the food supply chain's recall-event management system"
- manufacturing-qms (§16, processed) — related-types table: "Manufacturing Traceability | adjacent record system | owns the lot/serial genealogy chain; the QMS links quality records to lots but does not own genealogy"

Not reachable: SAP Digital Manufacturing operational docs (help portal renders empty shell), dedicated Opcenter Traceability product documentation, Aegis FactoryLogix, CAT Squared, Katana. No independent traceability-standards text (e.g., GS1 application standards beyond Odoo's GS1 pages, ISA-95 text) was retrieved; claims that would rest on standards are held on vendor statements only.

## Product Observations

### ParityFactory (Advantive) — traceability-first food & beverage WMS/MES

Evidence layer A — official product page (fresh):

- Headline positioning, verbatim: "ParityFactory: Intelligent traceability for food and beverage manufacturers — WMS and MES software purpose-built for food and beverage manufacturers that need real-time lot traceability, paperless production, and recall readiness in minutes." Also "FSMA-ready traceability."
- Scope of tracking, verbatim: "Real-Time Traceability From Receipt to Shipment — ParityFactory gives food manufacturers the control to track lots, inventory, work in progress, finished goods, and customer shipments in real time — reducing waste, improving recall readiness, and keeping every movement visible."
- Capture machinery: "Our software scans crates, boxes, or whole pallets directly into your inventory and checks them into their location – instantly tracking available ingredients and finished products, along with their precise locations. Our system also offers automatic FIFO and GS1 labeling for efficient lot tracing."
- Production-stage capture and validation, verbatim: "Embrace a paperless production process with comprehensive tracking at each step... alert users of potential ingredient mix-ups in your production run (i.e., organic vs. non-organic, allergen vs. non-allergen)." Production generates "finished goods and ingredient pick-lists... enabling inventory tracking even throughout work-in-progress steps."
- Quality module (PF Quality): "data capture via handheld scanners... record, track, and report quality data effectively and ensures regulatory compliance."
- Trace loop / response, verbatim: "It offers swift recall capabilities, allowing ParityFactory customers to perform a recall within minutes – significantly below the standard two-hour requirement... instant lot tracing sets your company apart"; "execute mock recalls within minutes."
- Production shape: "built to support food and beverage manufacturers with one-to-many manufacturing processes"; yield tracking, catchweight scheduling, recipe management.
- Deployment shape: integrates with accounting/ERP packages (NetSuite, QuickBooks, Sage Intacct, Dynamics 365 Business Central, Dynamics GP & NAV, SYSPRO, custom) — traceability layer beside the business system.
- Case study framing: "automate inventory and lot-level materials control from finished goods through transfer to third party storage and shipping to customers."

Interpretation: a product whose entire identity is traceability — the tracked unit is the lot (ingredients, WIP, finished goods), the record is the movement chain from receipt through production to shipment plus quality data, and the defining loop is the recall/trace query ("perform a recall within minutes", "mock recalls"). Capture is scan-driven at the point of work with validation alerts (mix-up warnings). The ERP integration posture shows traceability can be a dedicated layer over a business system rather than an ERP feature.

### Sciemetric QualityWorX (Nordson) — serialized test-data / birth-history pole

Evidence layer A — official product and solution pages (fresh):

- Positioning: "Use plant-floor data to improve product quality, efficiency, and traceability"; "full part traceability and birth history records by serial number."
- Record content, verbatim: "Collect process data from test systems and stations on the production line, including: full process signatures, pass/fail status, feature values with specification limits, user-defined part-specific parameters, defect and repair data, line configuration details, and machine vision images."
- Organization, verbatim: "In QualityWorX, data is stored by serial number and organized in a tree structure that mimics the line. You have a full replay of each process in the plant at your fingertips..." Also: "When storing serialized data, manufacturers can use QualityWorX to access a complete birth history for every part for easy retrieval and analysis. QualityWorX can also store non-serialized data or batch-identified data to provide access to station-level trends and analytics without serialization."
- Trace loop, verbatim (part traceability page): "Sciemetric's manufacturing traceability solutions give you insight into each manufactured component and its full history across each recorded assembly operation. We provide the tools to review and analyze this data by station(s), time span, shift or part population, with drill-down to individual serial numbers—in only a few clicks!" Purposes listed: "Easily provide objective proof that a part was made to spec"; "Identify the specific problem in a recall situation and pinpoint the affected parts quickly"; "Maintain regulatory record-keeping to comply with corporate requirements."
- Spill containment, verbatim (quality spill page): "quickly and accurately trace the root cause of the problem and identify affected parts by serial/batch number, timestamp, or other unique part identifiers"; "perform a targeted recall to avoid a mass recall"; "Use digital process signatures to characterize the defect and run a test against the lot potentially impacted."
- Case study, verbatim: suspected 10,000 engines → reprocessed historical signatures → "only 6 additional engines were affected. They were able to perform a focused recall of those 7 engines, by serial number—saving an estimated $5M."

Interpretation: the traceable unit is the serialized part (or batch); the record is the unit's complete process/test history (birth history) bound to that serial; the trace loop is investigation-driven — enter a serial, retrieve its full history, characterize the defect, and determine the affected population by re-querying historical data against the defect signature and criteria (station, time span, shift, population). Notably, no material-lot genealogy (which supplier lots went into the unit) is claimed — the "related population" is determined from unit-bound process data and criteria. This pole proves material genealogy is NOT definitional; the deeper invariant is the unit-bound record plus criteria-driven scope determination.

### Odoo (Inventory + Manufacturing) — integrated-ERP minimal pole

Evidence layer A — official user documentation (fresh):

- Unit semantics, verbatim: "Lots are one of the two ways to identify and track products in Odoo. They typically represent a specific batch of products that were received, stored, shipped, or manufactured in-house." Serial numbers "assign unique numbers to individual products"; lots "assign a single number to multiple units of a specific product."
- Purpose, verbatim: "Manufacturers assign lot numbers to groups of products sharing common properties, facilitating end-to-end traceability through their lifecycles. Lots are useful for... tracing items back to their group, particularly for product recalls or expiration dates."
- Configuration: a "Traceability" settings section enables "Lots & Serial Numbers"; per-product "Track Inventory" set to "By Lots" or "By Unique Serial Number" (default is quantity-only tracking).
- Mandatory assignment (blocking rule), verbatim: "Clicking Validate before assigning a lot number triggers an error, indicating that a lot number must be assigned before validating the receipt." In manufacturing: "Odoo requires the lot or serial number to be assigned to each product before manufacturing can be completed. This ensures that each product is properly tracked from the moment it enters inventory."
- ID machinery: auto-generation "using the next available number", editable; "Internal Reference: records an alternative lot/serial number used within the warehouse that differs from the one used by the supplier manufacturer"; custom properties on lots ("for enhanced traceability"); expiration dates; barcodes for lots/serials (GS1 nomenclature pages exist).
- Removal strategies: "The lot automatically chosen for delivery orders varies, depending on the selected removal strategy (FIFO, LIFO, or FEFO)."
- Operation-type rules: per operation type, whether new lots may be created or only existing ones used ("Create New" vs "Use Existing ones").
- Trace loop, verbatim: "Manufacturers and companies can refer to traceability reports to see the entire lifecycle of a product: where it came from, when it arrived, where it was stored, who it went to (and when)." The lot form has a "Traceability smart button" showing "a full stock moves report for a lot number."
- Customer-facing output: lot numbers can be displayed on delivery slips "in cases where lot numbers are needed, such as filing an RMA or repair request, or registering the product."
- Manufacturing grain: serial assignment splits a multi-unit MO into per-unit MOs ("WH/MO/00109-001", "-002").

Interpretation: the minimal pole — traceability as a feature of the integrated business system. The tracked unit is the lot or serial; the record is the stock-move chain (receipt → storage → manufacturing consumption → production → shipment) with attributes; the trace loop is the per-lot traceability report over the full lifecycle. Rules are instructive: assignment is blocking at receipt validation and production completion; removal strategies decide which lot ships; operation types constrain lot creation. No holds/quarantine machinery and no mock-recall tooling appear in the core docs — response machinery is NOT definitional.

### Siemens Opcenter (carried from the MES pass) — enterprise suite pole

Evidence layer A — official family page (fetched in sibling pass 2026-09-09, carried):

- "Production tracking — tracks and traces the status of production and disposition of work, including demonstration and documentation of regulatory and quality requirements... forward and backward traceability of components and their use within each end product."
- Industry-packaged MES families: Execution Electronics ("printed circuit board, mechanical assembly and box-build"), Execution Medical Device ("including electronic device history records (eDHR)"), Execution Pharma ("paperless manufacturing and electronic batch recording (eBR)"), Execution Semiconductor, Execution Discrete, Execution Process.
- The MES pass's own related-types table states the seam from the MES side: "Manufacturing Traceability | downstream record | genealogy is one leg of MES; standalone traceability systems keep and query the record without executing production. In suites, the record is produced by the execution engine."

Interpretation: in the enterprise suite, traceability appears as a named capability of the execution engine plus regulated-industry record packaging (eDHR/eBR). The capability language ("forward and backward traceability of components and their use within each end product") matches the canonical trace loop; the packaging (eDHR/eBR) is industry variant.

### Tulip (carried, boundary witness)

Evidence layer A — official integration doc (sibling pass): work orders, BOM, inventory, planning belong to ERP/MES; Tulip keeps "Tulip-Centric Context" including unit-level traceability captured at stations. Confirms that unit-level traceability records can be produced by frontline capture platforms outside a classic MES, and that the system-of-record seam is drawn explicitly in vendor documentation.

## Cross-product Comparison

| Dimension | ParityFactory | Sciemetric QualityWorX | Odoo | Siemens Opcenter (carried) |
|---|---|---|---|---|
| Tracked unit | lot (ingredients, WIP, FG) + shipments | serialized part; batch-identified data also supported | lot or serial, per product setting | unit/lot per industry family (serial units, lots, batches) |
| Record content | movement chain receipt→shipment, quality data, mix-up alerts | process signatures, pass/fail, feature values, defect/repair data, images | stock moves (receipt/store/consume/produce/ship), properties, expiry | consumption, operations, results, disposition (as-built record) |
| Genealogy mechanism | material lots → WIP → FG → shipments (one-to-many production) | station/process tree per serial; NO material-lot links claimed | stock-move chain incl. MO consumption/production | forward/backward component traceability |
| Trace loop | recall within minutes; mock recalls; instant lot tracing | serial/batch/timestamp query → birth history → affected-population by criteria | per-lot traceability report: full lifecycle "where it came from... who it went to" | forward and backward traceability; compliance documentation |
| Response machinery | recall readiness (mock recall tooling) | targeted-recall scope determination | none in core docs | disposition of work (in execution) |
| Capture | scanning at receipt/production/shipment; handheld QC scanners | station DAQ/test-system integration | manual entry, bulk import, barcode scanning | machine + operator entry (MES execution) |
| Where it lives | standalone WMS/MES beside ERP | standalone data platform beside the line | feature of integrated ERP | capability/module inside MES/MOM suite |
| Tier / industry | mid-market food & bev | automotive/medical/EV/MRO discrete | SMB → mid-market, generic | large enterprise, regulated + electronics |

Stable commonalities across the sample:

1. Every product centers on an **identified traceable unit** (lot/batch/serial) with an ID that production and distribution events reference.
2. Every product accumulates a **unit-bound record** of what happened to the unit (movements, consumption, operations, measurements, results) and keeps it.
3. Every product provides a **trace loop**: query a unit (or criteria) → retrieve its record → determine the related population (backward to inputs; forward to outputs/implicated units) → produce scope and documentation for quality/compliance response.
4. Triggers are consistently quality/compliance events: defect spill, complaint, recall, audit, customer request, RMA.
5. Capture is multi-mechanism (scan, manual, machine/test data, upstream systems) — no single mechanism is universal.
6. Response machinery (holds, quarantine, mock recalls) varies: present as headline in food, absent from Odoo core, scope-only in Sciemetric — NOT definitional.
7. Material genealogy (lot→unit links) is the dominant mechanism in material-producing industries but is absent from the test-data pole — the mechanism is common-mature, not invariant.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The identified traceable unit** — a lot, batch, or serial number as the unit of record: an ID assigned at receipt or production, carried on the physical material (label/barcode or record reference), which production and distribution events cite. Remove → unidentified production logs; nothing is traceable.
2. **The unit-bound production record** — events and data recorded against the unit's ID as it moves through production and out the door (what went into it, what was done to it, what was measured, where it went), kept as a lasting record. Remove → reports/dashboards with no memory; later questions cannot be answered.
3. **The trace loop** — given a trigger (defect, complaint, recall, audit, customer request), retrieve any unit's complete record and determine the related population — backward to its inputs, forward to what it went into / which units are implicated — producing the scope and documentation for response. Remove → a passive archive; the "trace-ability" is gone.

Jointly-held load-bearing: (1 alone = an ID registry; 2 without 1 = anonymous production logs; 3 without 1+2 = nothing to trace; 1+2 without 3 = an archive, not traceability; 1+3 without 2 = queries over nothing).

### L1 — Common Mature Structure

- **Material/assembly genealogy links** — recorded parent→child relations (consumed lots, installed serials → produced lots/units), the standard mechanism for the related-population determination in material-producing industries; spans operations, batches, and commonly sites and supplier/customer boundaries (one-up/one-back at minimum).
- **Unit-bound quality data** — inspection/test results, measurements, images, defect/repair records attached to the unit's ID.
- **ID machinery** — numbering rules and auto-generation, label/barcode printing (GS1-class), internal vs supplier references, custom attributes on lots.
- **Holds / quarantine / disposition marking** of suspect units and lots.
- **Recall scoping and simulation** — affected-units lists, mock recalls, recall-readiness reporting.
- **Compliance documentation** — eDHR/eBR-class records, proof of conformance, regulatory record-keeping outputs.
- **Date/expiration handling** — expiry dates on lots, FEFO/FIFO removal strategies deciding which lot ships.
- **Supplier/customer linkage** — vendor lot intake on receipts; lot numbers on delivery slips for customers (RMA/registration).

### L2 — Variant / Optional Structure

- **Deployment shape** — standalone traceability product; module inside MES/MOM suite; module inside QMS; feature of integrated ERP; frontline-platform capture feeding a system of record.
- **Industry packaging** — food & beverage (FSMA framing, allergen/organic mix-up checks, mock recalls), medical device (device history records), pharma (batch records), electronics (unit genealogy across assembly), automotive (spill containment), aerospace (records/certs).
- **Grain** — serialized unit vs lot/batch vs both (per product setting).
- **Data depth** — movement-level (stock moves) ↔ process-data-level (waveforms/signatures, images) ↔ document-level (certs, records).
- **Capture mechanism** — manual entry, bulk import, barcode/RFID scanning, machine/test-system integration, upstream-system feeds.
- **Deployment platform** — cloud SaaS ↔ on-premise; SMB ↔ enterprise scale.

### L3 — Vendor-specific (research notes only)

- Odoo: MO splitting per serial unit; operation-type "Create New" vs "Use Existing" lot rules; Traceability smart button; property fields on lots; removal-strategy set (FIFO/LIFO/FEFO/closest/least-packages).
- Sciemetric: digital process signature technology; tree structure mimicking the line; Studio tiers (LT/SE); "3 clicks" claim; 10,000→7 engines case study; sigPOD/EDGE hardware.
- ParityFactory: PF Quality module; fishermen settlements / grower payments; catchweight scheduling; 90-day implementation claim; "two-hour requirement" claim; named ERP integrations.
- Siemens: Opcenter family packaging (Execution Electronics/Medical Device/Pharma/Semiconductor...); MOM portfolio framing.

## Vendor-specific Findings

- The "recall within minutes" and "two-hour requirement" claims (ParityFactory) and the "3 clicks" claim (Sciemetric) are vendor marketing precision — recorded here, excluded from the canonical document.
- The 10,000→7 engines case is a single-customer anecdote (Sciemetric marketing) — evidence of the spill-containment loop's value, not a general claim.
- Odoo's MO-splitting behavior on serial assignment is product-specific implementation of unit-grain tracking.
- GS1 labeling appears at two poles (ParityFactory "automatic FIFO and GS1 labeling"; Odoo GS1 barcode nomenclature docs) — treated as common implementation of ID machinery, not definitional.

## Boundary Findings

1. **vs Manufacturing Execution System / MES** (ratifies the pre-hung flag from the MES pass): MES's defining core is the executed production order bound to a defined process; its as-built record — including genealogy — is produced as a byproduct of execution. Manufacturing Traceability's defining core is the unit-bound record plus the trace loop, which exists without executing production: links and data can be captured by scanning, test systems, manual entry, or received from MES/ERP (ParityFactory beside an ERP; Sciemetric beside test stations; Odoo's stock-move chain). Genealogy-without-execution = this Type; execution-produced-record = MES. In suites, traceability is a capability/module of the execution engine — packaging, not identity. **RATIFIED from this side; the two documents agree.**
2. **vs Manufacturing QMS**: the QMS pass's own table states the seam — "owns the lot/serial genealogy chain; the QMS links quality records to lots but does not own genealogy." The QMS is the quality system of record (nonconformances, CAPA, audits, complaints); traceability is the unit-level history its investigations consume. Holds/dispositions overlap is machinery-level. Keep both.
3. **vs Food Traceability Platform (§20, processed)**: that Type is "the food supply chain's standing lot-level movement ledger" — supply-chain movement focus. Manufacturing Traceability is factory-production oriented: genealogy across transformation events inside the plant (which inputs became which outputs) plus unit-bound production/quality data. Overlap exists at lot movement; the seam is production-transformation genealogy + production-context data vs supply-chain movement ledger. Keep both.
4. **vs Food Recall Management (§20, processed)**: that Type owns the recall event (declared→progressed→closed, notifications, regulatory reporting). Traceability produces the affected-units determination that a recall consumes; it does not run the recall event. Keep both.
5. **vs Inventory Management / WMS**: lot/serial tracking at pure movement grain (receipt/store/ship without transformation linkage) is inventory territory. The Manufacturing Traceability signature is genealogy across production transformation plus production-context data. Odoo sits at the minimal in-type pole because its MO consumption/production links provide transformation genealogy; a WMS without production linkage is out of type.
6. **vs SPC / Inspection & Metrology**: those Types analyze quality data for process control; traceability binds data to units and answers unit-level questions. Sciemetric straddles both (analytics + traceability); its traceability identity is the birth-history record and spill scoping, not the control charts.

## Historical / Market-Sample Check

Paper-era lot control satisfies all three L0 legs with no software: lot/serial numbers assigned at receiving or production and stamped on travelers and containers; component lot numbers and certs recorded on the job packet; movement and inspection entries kept in lot ledgers; recall or complaint response conducted by pulling the files and tracing by hand (the practice regulators predated software with). Older and regional products (paper, spreadsheet, desktop-era lot trackers) fit the same triple. Therefore nothing digital (barcodes, cloud, scanning, real-time) belongs in the defining core; capture mechanism, response tooling, and compliance packaging are era/segment variants.

## Uncertainties

- The dedicated enterprise traceability-product pole (Opcenter Traceability, Aegis FactoryLogix) could not be fetched; its structure is inferred from the carried Opcenter MES-family evidence and the MES pass's boundary statement. Assertions about deep enterprise genealogy features (e.g., parallel/serial assembly trees, segment data models) are NOT made for lack of direct evidence.
- Whether holds/quarantine machinery is universal in dedicated traceability products is unverified (present at the food pole, absent from Odoo core docs, scope-only at Sciemetric) — held as common-mature, not invariant.
- Regulatory minimums (e.g., "one-up/one-back" as a named requirement) were not verified against standards text; the phrase is used only as commonly-observed vendor language, not as a verified standard.
- Sciemetric's lack of material-lot genealogy is an absence of evidence on marketing pages, not a verified product limitation; the pole is used to show the mechanism is not definitional, not to characterize the product exhaustively.

## Final Synthesis

Manufacturing Traceability is the manufacturer's unit-level memory and reach-of-problem machinery: it assigns a lasting identity (lot/batch/serial) to material as it enters production, records what happens to each identified unit as production and distribution proceed, and — when a defect, complaint, audit, or recall demands it — traces any unit's complete history backward to its inputs and forward to everything it went into, producing the scope of the affected population and the documentation to respond. The defining core is exactly three jointly-held structures (identified traceable unit; unit-bound production record; trace loop). Material genealogy is the standard mechanism of the trace loop in material-producing industries but is not definitional (the test-data pole traces by unit-bound process data and criteria). Response machinery, capture mechanisms, compliance packaging, and deployment shape are common-mature or variant structure. The Type stands distinct from MES (which produces the record by executing production), from QMS (which consumes it for quality-system work), from food supply-chain traceability and recall management (supply-chain movement and recall-event machinery), and from inventory lot tracking (movement grain without transformation genealogy).
