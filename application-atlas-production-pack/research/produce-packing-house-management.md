# Research Notes — Produce Packing House Management

## Research Goal

Understand what software for managing a produce packing house actually is: what objects it manages, what the pack operation looks like in the system, how fruit moves from field arrival to packed, labeled, traceable product, and where this Type begins and ends relative to produce ERP, food traceability, WMS, harvest management, and food manufacturing ERP.

## Initial Boundary

Initial hypothesis: a packing house management application is the packer's post-harvest operations system of record — receiving produce from fields/growers, grading/sizing/packing it into saleable units, tracking packed inventory, labeling, and maintaining lot-level traceability. Likely confusions:

- Produce ERP (packer/shipper) — broader; packing is one module among sales, accounting, transport.
- Food Traceability Platform — traceability is a capability here, not the whole product.
- WMS — generic warehouse handling lacks the pack transformation and grade/size semantics.
- Harvest / Orchard Management — field-side; the bin ticket is the seam.
- Food Manufacturing ERP — recipe/formulation manufacturing vs sorting/grading/packing of fresh produce.

## Research Questions

1. What enters the system at receiving, and with what attribution (grower, block, variety, weight)?
2. What is the unit of record — bin, lot, pallet, carton — and how does it persist through the pack transformation?
3. How is the pack operation modeled (pack line, pack run, grade/size, pack style, packout)?
4. How do labels/tags (pallet tags, PTI/GS1 case labels) relate to traceability?
5. What inventory states exist (raw/field lots, WIP, finished goods, packaging materials, culls)?
6. Where does quality control sit (sampling, holds, release)?
7. Is grower settlement (pool pricing, advances, deductions) part of the Type or an adjacent module?
8. Where do storage/cold chain, sales orders, dispatch fit — core or optional?
9. What is the recall/traceback workflow?

## Representative Products

Selected for market representativeness, different product philosophy, and different customer tier:

- **Croptracker (Packing module)** — grower-side modular farm-management ERP; small/mid growers who pack their own crop. Philosophy: record-keeping modules that link field to pack.
- **Farmsoft / Producepak** — packhouse-specialist mid-tier software for fruit/vegetable packers, importers, exporters. Philosophy: the packhouse is the center of the world.
- **Aptean Fresh Produce ERP (Produce Pro lineage)** — enterprise produce ERP for growers/packers/shippers. Philosophy: whole produce business on one ERP.
- **inecta Produce Packer & Shipper ERP** — packer/shipper ERP on Dynamics 365 Business Central; mid/enterprise. Philosophy: produce-specific ERP vertical.
- **SG Systems V5** — pack-line MES/WMS shop-floor control for produce packing. Philosophy: control the pack line and QA process itself.

Adjacent samples used for boundary checks: Matthews iDSnet (line-level data capture, explicitly complementary), Hectre (orchard/harvest-side with packhouse quality scanning), PickTrace (harvest labor tracking incl. packing house), AgriERP / RSM Grower Accounting (grower settlement as a separable module).

## Sources

- Croptracker — Produce Packing Traceability Records (product page, fetched directly): https://www.croptracker.com/product/farm-management-software/produce-packing-traceability-records.html
- Croptracker — Predictive Packout Toolkit (product page): https://croptracker.com/product/predictive-packout-toolkit.html
- Farmsoft/Producepak — Packhouse management software (marketing/overview page; direct fetch returned 403, content from search index excerpt): https://farmsoft.com/traceability/packhouse-management-software
- Aptean — "The Life Cycle of Produce Pro Software: Meet Aptean Fresh Produce ERP" (vendor blog): https://aptean.com/en-US/resources/industry-insights/blog/produce-pro-software-evolution-fresh-produce-erp
- inecta — Produce Packer & Shipper ERP; Produce ERP (grower receiving & settlements) product pages: https://www.inecta.com/produce-packer-shipper , https://www.inecta.com/produce-erp-software
- SG Systems Global — Produce Packing Traceability & QA Hub (V5 MES & WMS guide): https://sgsystemsglobal.com/guides/produce-packing-control-hub
- Matthews — iDSnet Packhouse Software: https://www.matthews.com.au/packhouse-software
- Hectre — orchard management / fruit quality (boundary sample): https://hectre.com/
- PickTrace — farms & packing house labor (boundary sample): http://picktrace.com/farms
- AgriERP Grower Management; RSM Grower Accounting (settlement boundary samples): https://agrierp.com/product-features/growers-management , https://marketplace.microsoft.com/en-us/product/dynamics-365-for-operations/rsmproductsalesllc1604685958273.rsmccmgrower

Research date: 2026-09-10.

Source-access limitation: most vendor help centers were not directly fetchable; evidence for Farmsoft, Aptean, inecta, SG Systems rests on official product/marketing pages surfaced via search excerpts (Tier 2), not on operational help articles (Tier 1). Only Croptracker's product page was fetched in full. Precise operational details (exact label formats, numeric limits, specific state names) are therefore avoided or kept qualified.

## Product Observations

### Croptracker (evidence layer A — direct fetch)

- Packing module "used by growers of all sizes to record processing and retail product creation."
- "Move harvested inventory into packing to consume and record product creation" — the pack event consumes raw harvested inventory and produces packed product records.
- "Scan tags as they hit the pack line and record the packed results" — pack-line scanning records results.
- Pallet tags and individual product tags, created from web or mobile; customizable formats and codes.
- Custom product configurations with assigned packing materials and label formats; material use tracked to determine full cost of packing.
- Culls and inventory changes from drying/long-term storage, cutting/trimming recorded before products are retail ready.
- Traceability achieved by linking modules: Harvest, Receiving, Storage, Shipping, Order Desk, Punch Clock — "full traceability from raw harvested to processed and packed products."
- Packing is one module of a farm-management ERP; the standalone Packing module alone does not carry the full chain.

### Farmsoft / Producepak (evidence layer B)

- Positioned as "comprehensive packhouse management for fruit, vegetable, and fresh produce processors, packers, importers and exporters."
- Scope: "from delivery, short and long term storage, washing, packing, processing, and even full food manufacturing and value adding processes."
- Features listed: inventory control, quality control, bar code scanning, mobile inventory, temperature zone management, traceability reporting, batch cost management, sales, dispatch; bins and trucks tracking; packing and labeling; cool-store inventory; orders and payments; sales contracts, export documentation, shipping containers, invoice preparation.
- Traceability framed as the headline: "full traceability of all types of produce – from harvest through dispatch and all the way to the customer."

### Aptean Fresh Produce ERP / Produce Pro (evidence layer B)

- "Industry-specific ERP built for growers, packers and shippers."
- "Integrated lot management, warehouse tracking and FSMA-ready reporting tools – plus a recall module."
- "Attribute-based inventory tracking and mobile-enabled inspections" for quality control.
- "Shop floor monitoring with mobile-enabled tracking and automates over or under delivery adjustments… from receiving to shipment."
- EDI for traceability data exchange, vendor lot tracking, compliance reporting.
- 30+ years as produce-industry ERP; packing is embedded in a full supply-chain ERP.

### inecta Produce Packer & Shipper (evidence layer B)

- "Platform designed for operations that receive, pack, and distribute fresh produce."
- Receiving captures "weight, grade, variety, pack style, and harvest date" by lot; pickup tickets as lot attributes.
- Packing workflows: barcode scanning, directed pick and pack, scale weighing; generates customer labels, bills of lading, picking documents, invoices.
- PTI-compliant lot traceability "from source to shipping"; SQF/HACCP/GFSI/FSMA/PTI requirement management.
- Grower accounting: "pool pricing, advances, premiums, deductions, and per-grower formulas run into settlement statements"; retroactive settlement recalculation; multi-grower pooling.
- Multi-site inventory, FIFO/FEFO, transport management module.

### SG Systems V5 (evidence layer B)

- Produce packing modeled as MES + WMS: pack line operations with "grade, size, pack style, commodity & variety on each line."
- QA sampling & release: "appearance, brix, pressure, defects, shelf-life indicators"; "holds and releases are recorded with e-signatures and are traceable back to the originating field lots."
- Case & pallet labelling: PTI labels, GS1 case codes, pallet tags, customer formats.
- Storage/cold chain: cold rooms, staging, dwell time, temperature excursions.
- Loads & shipping: load plans, trailer temp, customer orders, ASNs; FSMA 204 CTEs/KDEs, traceback/traceforward by lot and load.
- Field lot identification scheme and harvest bin traceability as the entry point.

### Boundary samples

- **Matthews iDSnet**: line-level capture of "every carton that leaves the packing floor via its grade and its packer"; explicitly "integratable into standard packhouse management software" — i.e., a complementary capability layer, not the management system itself. Also shows packer-ID tracking feeding piece-rate pay administration.
- **Hectre**: orchard-side bin ticketing, crediting, picker performance, fruit sizing/color grading; "scan tickets at the packhouse to connect data automatically to your existing systems" — the field system hands off at the packhouse door.
- **PickTrace**: harvest labor/payroll with pallet/bin tracking "created, picked up, received, and moved" — labor-centric; packing house appears as a check-in location.
- **AgriERP / RSM Grower Accounting / Levridge**: grower settlement (contracts, advances, deductions, quality grades, settlement statements) exists as a separable module/solution — evidence that settlement is a capability that can live outside the packing house core.

## Cross-product Comparison

| Structure | Croptracker | Farmsoft | Aptean | inecta | SG V5 |
|---|---|---|---|---|---|
| Receiving with source attribution (grower/block/field lot) | ✓ (Receiving module link) | ✓ (delivery) | ✓ (receiving) | ✓ (pickup tickets, weight/grade/variety) | ✓ (field lot ID, bin traceability) |
| Pack transformation consuming raw lots → packed product | ✓ (consume & record product creation) | ✓ (washing, packing, processing) | ✓ (shop floor production tracking) | ✓ (pick and pack, scale weighing) | ✓ (pack line grade/size/pack style) |
| Lot identity persisting through transformation | ✓ (link harvest→packing records) | ✓ (traceability harvest→customer) | ✓ (lot management) | ✓ (lot attributes) | ✓ (traceable back to originating field lots) |
| Tags/labels on packed units (pallet/case, PTI/GS1) | ✓ (pallet & product tags) | ✓ (packing and labeling) | implied | ✓ (PTI labels, BOL) | ✓ (PTI, GS1, pallet tags) |
| Packed inventory / cool store | ✓ (storage module link) | ✓ (cool-store inventory, temp zones) | ✓ (warehouse tracking) | ✓ (multi-site inventory, FIFO/FEFO) | ✓ (cold rooms, staging) |
| Quality control / holds / release | ✓ (QC module) | ✓ (quality control) | ✓ (inspections, attribute tracking) | ✓ (quality control) | ✓ (sampling, holds, e-signature release) |
| Grower settlement / pool pricing | — | payments mentioned | — | ✓ (full settlement engine) | — |
| Sales orders / dispatch / export docs | ✓ (Order Desk, Shipping modules) | ✓ (sales, dispatch, export docs) | ✓ (EDI, shipment) | ✓ (transport mgmt, EDI) | ✓ (loads, ASNs) |
| Packaging materials management | ✓ (material use, cost of packing) | ✓ | — | — | — |
| Line-level packer attribution | — | — | — | — | ✓ (via complementary iDSnet-class tools) |

Reading: receiving-with-attribution, the pack transformation, and lot identity through the transformation appear in all five. Grower settlement appears in only the ERP-class products (2/5) — common in the packer/shipper segment but not definitional. Sales/dispatch appear in most but Croptracker delivers them via separate optional modules — common, not defining. Packaging materials and packer-level attribution are segment- or product-specific.

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The received lot of record with source attribution.** Incoming produce enters as identified lots (bins, pickup tickets, field lots) carrying source (grower/orchard/block/field), commodity, variety, and measured attributes (weight, condition). Remove → generic warehouse receiving.
2. **The pack transformation.** The system models the conversion of raw lots into packed product: grading/sizing decisions, pack style/configuration, consumption of raw inventory, creation of packed product records and packaging-material consumption, culls and shrink recorded. Remove → inventory tracker with no operation.
3. **Lot genealogy across the transformation.** Packed lots remain linked to their source lots (and onward to shipments), so any packed unit can be traced back to origin and any source lot forward to what was packed and where it went. Remove → production logging with no traceable identity; the recall/traceback job disappears.

The binding is fresh-produce semantics: perishability, grade/size as the transformation's central decisions, lot (not SKU) as the working unit.

### L1 — Common Mature Structure

- Pallet/case labeling to customer and regulatory formats (PTI, GS1) generated from lot data.
- Packed-goods inventory with storage locations and cool rooms / temperature zones.
- Quality control: inspections/sampling against standards, holds and releases.
- Dispatch/shipping linkage: orders, loads, BOL, ASN, traceability events at shipping.
- Packaging materials inventory and pack cost.
- Recall / traceback / traceforward reporting.

### L2 — Variant / Optional Structure

- Grower settlement (pool pricing, advances, deductions, settlement statements) — packer/shipper ERP segment; separable module elsewhere.
- Sales contracts, export documentation, container management — exporter variant.
- Value-adding / fresh-cut processing — drifts toward food manufacturing.
- Line-level packer attribution feeding piece-rate pay — integration with labor systems.
- Fruit sizing / color grading technology (vision scanning) — quality-tech variant.
- Multi-site / multi-facility estate.

### L3 — Vendor-specific

- Croptracker's module-linkage model (Packing + Harvest + Receiving + …).
- inecta's Business Central tenant integration and retroactive settlement recalculation.
- SG V5's e-signature release and QMS/CAPA linkage.
- Matthews iDSnet's carton-level packer-ID capture.

## Historical / Market-Sample Check

Would older, regional, paper-based packing sheds fit the L0? Yes: a packing shed running on paper bin tickets (attributing bins to grower/block), packout tally sheets (recording what was graded, sized, packed, culled), lot stamps/labels on cartons and pallets, and a lot book linking packed lots back to bin tickets satisfies all three L0 structures. The definition does not depend on barcodes, PTI, cloud, or scanning. Conversely, a generic WMS without pack transformation and lot genealogy fails L0 — confirming the boundary.

## Vendor-specific Findings

- Croptracker: packing as one purchasable module; full traceability requires pairing modules.
- Farmsoft: markets "90% reduction" claims — marketing, not evidence.
- inecta: settlement statements posted to GL in the same ERP tenant.
- SG V5: QA holds/releases with e-signatures; FSMA 204 CTE/KDE framing.
- Matthews: positions itself explicitly as complementary to "standard packhouse management software."

## Boundary Findings

- **vs Produce ERP (packer/shipper)**: ERP adds sales, accounting, procurement, transport around the same packing core. Remove the ERP back office → still packing house management; remove receiving/pack/lot-genealogy → generic ERP. Packaging seam: many packers run one product containing both; the packing house core is the operational spine.
- **vs Food Traceability Platform**: traceability platforms hold traceability data/records across supply chain actors; packing house management runs the operation that generates those events. Remove the operation → traceability registry.
- **vs WMS**: WMS stores and moves identified goods; it does not model grading/sizing/packing transformation or field-lot genealogy. Remove the pack transformation → WMS.
- **vs Harvest / Orchard Management**: field-side systems end at the bin ticket handed to the shed; packing house systems begin at receiving that bin. The bin ticket / pickup ticket is the shared artifact and the seam.
- **vs Farm Labor Management**: packer piece-rate pay consumes packout records; labor management is a separate Type that integrates.
- **vs Food Manufacturing ERP**: fresh produce packing = sorting/grading/packing of perishable whole goods with lot genealogy; food manufacturing = recipe/formulation transformation. Value-adding (fresh-cut, processing) is the drift zone — Farmsoft explicitly spans it.
- **vs Food Safety / HACCP Management**: compliance program management vs the operational system that records QC events inline.
- **vs Grain Elevator Management**: same family shape (receive from growers, handle, settle) but grain's core is storage condition and commerce; produce packing's core is the pack transformation. Different Type.

**"Remove what to become another Type" test**: remove the pack transformation and genealogy → WMS/inventory; remove the produce/lot semantics and keep the ERP shell → generic produce ERP; remove the operation and keep only records → food traceability platform; move upstream of the bin ticket → harvest management.

## Uncertainties

- Exact workflow granularity inside the pack run (per-line vs per-order packing) varies and was not verifiable from Tier-1 docs; kept generic.
- Whether QC holds/release is universal or segment-dependent (SG shows it explicitly; others list QC without hold semantics) — treated as common, not defining.
- The degree to which dispatch/export is in-scope vs integrated varies widely; treated as common/optional.
- Farmsoft evidence is from a search excerpt of an unreachable page (403) — assertions kept at positioning level.

## Final Synthesis

A Produce Packing House Management application is the packing house's post-harvest operations system of record. Its defining core is three jointly-held structures: the received lot of record with source attribution, the pack transformation that consumes raw lots and creates packed product (with grade/size/pack-style decisions, culls, and packaging materials), and lot genealogy that keeps every packed unit traceable to its source and onward to shipment. Around this core, mature products add labeling to customer/regulatory formats, cool-store inventory, QC holds and releases, dispatch linkage, and recall reporting; grower settlement, export documentation, value-adding processing, and packer-pay integration are segment variants. The Type is bounded upstream by the bin/pickup ticket (harvest management's handoff), downstream by the shipped load (sales/transport territory), and sideways by generic WMS (no pack transformation) and food manufacturing ERP (no fresh-produce lot semantics).
