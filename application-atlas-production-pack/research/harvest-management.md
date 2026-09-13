# Research Notes — Harvest Management

Research date: 2026-09-08
Slug: harvest-management
Directory leaf: Harvest Management (§20 Agriculture, Food & Natural Resources)

## Research Goal

Understand what a "Harvest Management" application is as an Application Type: what its managed object is, who runs it, what the harvest workflow looks like in real products, where its boundaries sit against the neighboring already-processed Types (crop-management, farm-labor-management, food-traceability-platform, grain-management, farm-management-platform) and unprocessed siblings (produce-packing-house-management, precision-agriculture-platform, orchard/vineyard management), and whether the leaf is a genuine Type or a capability/module of crop management.

Pre-hung seams from sibling passes (STATUS.md Boundary Issues):

- **farm-labor-management** (processed 2026-09-08): sharpest seam — "harvest management centers the harvest operation and its product (what was picked, maturity, yield, inventory, quality); this leaf centers the workforce (who, in what crew, how long, how many pieces, owed what). They meet where pickers/hours link to bins (a sampled crop platform pairs its labor module with its harvest module as 'time against inventory')" — handoff seam, joint review recommended at this pass.
- **food-traceability-platform** (processed 2026-09-08): "vs produce-packing-house-management/harvest-management (one event source vs the chain-wide join)".
- **crop-management** (processed 2026-09-07): related-types row states "Harvest Management | centers the harvest operation itself (crews, bins, loads, packing); crop management treats harvest as the cycle's closing phase."
- Naming caution (farm-labor pass): "Harvest" (getharvest.com) is an unrelated generic time tracker — name collision only; must not be sampled as agriculture evidence.

## Initial Boundary

Working hypothesis before sampling: a Harvest Management application is the grower's/operator's system for running the harvest operation on specialty or high-value crops — deciding what is ready and how much is expected, recording the picking as it happens (who picked what from where), tracking the picked product as inventory (bins/totes/loads) into the next stage, and closing out per-block yield, quality and labor credit.

Most easily confused with:

- Crop Management — harvest as the closing phase of a crop-season record.
- Farm Labor Management — crews, hours, piece-rate pay (workforce center).
- Produce Packing House Management — post-harvest processing, packing, food safety.
- Food Traceability Platform — chain-wide lot ledger.
- Precision Agriculture Platform — machine-executed harvest (yield monitors, telemetry).
- Grain Management — stored-grain protection (different object entirely).
- Farm Management Platform — whole-farm business operations.

Unknowns at start: is there a real standalone product population, or only modules inside farm-management suites? Does the Type include machine-executed (broadacre/row-crop) harvest, or is it specialty-crop shaped? Does the planning/estimation side belong to the defining core?

## Research Questions

1. What is the unit of record — the harvest event, the bin/load, the block, the season?
2. How does the planned side work (maturity/readiness, yield estimates, crew/storage/sales alignment)?
3. How is harvest execution captured (who records, on what surface, at what moment, with what attribution)?
4. How does the picked product flow from field to the next stage, and who reconciles it?
5. How do workers/pickers attach to the record, and where does that stop being this Type?
6. What interfaces exist (field mobile, office web, packhouse/dock)?
7. What rules matter (attribution completeness, offline behavior, compliance, lot definition)?
8. What is variant vs defining across products, eras, geographies and crop types?

## Representative Products

Selection: market representativeness + documentation completeness + different product philosophies + different customer tiers + geography.

| Product | Role in sample | Segment / geography | Philosophy |
|---|---|---|---|
| Croptracker | Defining sample 1 | Specialty fruit & vegetable growers/packers, North America + global | Modular harvest system: block-to-bin inventory, traceability, labor, QC, receiving/storage |
| Hectre | Defining sample 2 | Orchard fruit (apples/cherries/pears/citrus), New Zealand/Australia origin, sold into US/global packers | Crediting-centric harvest: bin ticketing, real-time crediting, picker performance, fruit-quality AI |
| Fieldin | Boundary-check sample | High-value permanent crops (nuts, grapes, stone fruit, citrus), US/Israel | Mechanized-operations telemetry: harvest as machine activity to accelerate, not product inventory |
| Farmbrite | Module-packaging sample | Small/diversified farms, global | All-in-one farm software with harvest records + inventory inside |
| xFarm | Module-packaging sample | European farms (Switzerland/Italy + UK) | Farm-management app suite; activities/field notebook; no dedicated harvest product line visible |

Attempted and unreachable (recorded as limitations): AgCode (agcode.com + www.agcode.com — transport errors ×2; a wine-grape harvest-tracking/grower-payment vendor per prior passes' notes), Farmable (farmable.app + www.farmable.ai — transport errors ×2), Bitwise Agronomy (www.bitwise.ag — transport error ×1). PickTrace had been found unreachable in the farm-labor-management pass (labor-adjacent anyway). No vendor help-center/login areas were fetched; evidence is official product/marketing-page level.

## Sources

Tier 1/2 (official product pages, fetched 2026-09-08):

- Croptracker — https://www.croptracker.com/ ; Harvest Management Software: https://www.croptracker.com/product/harvest-management-software.html ; Harvest Estimates: https://www.croptracker.com/product/farm-management-software/harvest-estimates.html ; Harvest Crop Yield Records: https://www.croptracker.com/product/farm-management-software/harvest-crop-yield-records.html
- Hectre — https://hectre.com/ ; Harvest: https://hectre.com/products/farm-management-software/harvest-management/
- Fieldin — https://fieldin.com/
- Farmbrite — https://www.farmbrite.com/
- xFarm — https://www.xfarm.ag/

Prior-pass context (same production pack): applications/crop-management.md, applications/farm-labor-management.md, applications/food-traceability-platform.md, applications/grain-management.md and their research notes; STATUS.md Boundary Issues entries for farm-labor-management and food-traceability-platform.

## Product Observations

### Croptracker (defining sample; evidence layer A)

Vendor's own definition (Harvest Management Software page): "Harvest management software records the work of the harvest season — yields by block, piece-rate labor, field packing, bin tagging, and quality — in one system used on mobile devices in the field. It replaces paper tallies and end-of-season transcription with records captured the day they happen." Positioning: "Yield, Labor, and Traceability from Block to Bin."

Workflow table on the same page (paper today → what the system records):

- Harvest recording: clipboard tallies → "Harvest events with tags scanned or printed in the field"
- Yield by block: hand-written totals → "Real-time totals by block, variety, and row as fruit comes in"
- Crew labor & piece rate: notebook tallies per picker → "Punch Clock time and piece-rate records per picker, led by crews"
- Field packing: run sheets, paper labels → "Field Pack labels, inventory, worker productivity, and material use"
- Bin tagging: handwritten bin tickets → "Barcode and QR tags linked to block and picker, printed or pre-printed"
- In-field QC: paper score sheets → "Digital inspection templates plus computer vision scans on the bin"
- Traceability: lost bin tickets → "Lot codes and critical tracking events from tag to dock and beyond"
- Dock handoff: weigh tickets, phone calls → "Receiving and storage records that link field inventory to the packhouse"

Specific mechanics observed:

- Harvest module: "records inventory the moment it comes in, tied to the block, variety, and picker who produced it. Crew leaders print or scan bin tags in the field, and each tag becomes a digital inventory record."
- Four recording workflows (Harvest Crop Yield Records page): pre-print & scan tags / print & tag as you go / record in bulk (shift end) / scan your own tags. "Link harvest inventory to pickers for traceability and piece rate pay calculations."
- Harvest Estimates module: "Enter the projected yields for each block on your farm… in terms of bin count or weight. Run reports to see projected yields over time" (multiple farms within an organisation). Purpose per marketing page: "so labor crews, storage bookings, and sales commitments line up with what really comes in."
- Punch Clock (labor): hourly + piece-rate schedules; piece-rate setup before season (base rates, harvest units per variety/block, crews + leaders); minimum-wage top-ups and overtime premiums computed from the same records; region-specific compliance context cited (California rest/recovery pay, Washington incidental-task hourly ruling) — vendor blog-level, kept qualitative.
- Field Pack module: labels, inventory, worker productivity, material use at the point of packing, offline.
- Quality Control module: inspection templates (size, color, pressure, defects) per variety "attached straight to the inventory lot"; inspections as bins fill; brix/starch-iodine/pressure readings captured on the same lot record. Harvest Quality Vision: phone scan of a bin → size/color distribution (a "3 mm" accuracy claim exists — vendor marketing, kept in these notes only).
- Traceability: "The moment fruit is harvested, its lot is defined: grower, block, variety, picker, and date. Every step after — field pack, receiving, storage, shipping — appends a critical tracking event to that lot."
- Dock handoff: Receiving Records module ("records the inbound load by lot code, with supplier, block, and arrival time… so the packhouse works from the same records your crew created in the field"); Storage Records (scanned into cold/CA rooms with timestamps and location); recall report from a single lot code.
- Offline: "All harvest functions run offline and sync when connectivity returns."
- Modular pricing: start with Harvest and Punch Clock; add Field Pack, Quality Control, Storage, Harvest Quality Vision. (Exact price points = vendor marketing; not carried into the final doc.)
- Customer evidence: Taggares Fruit Company — pre-printed tags, offline scanning, "removed the end-of-day ticket reconciliation," season moving 2,000 bins in a day; Mr Apple (NZ) large integrated grower-packer.

### Hectre (defining sample; evidence layer A)

Positioning: "The orchard management and fruit quality software that growers and packers love to use." Harvest product line: "Fast bin ticketing, crediting and tracking for traceability." Orchard Management suite: clock in workers, track agrochemical use, "record harvest in real-time," performance and cost insights, payroll automation.

Harvest page observations:

- Bin ticketing: "Scan your existing bin tickets or create waterproof bin tickets on-the-go"; supports third-party barcode/QR integration; online plus offline; bilingual interface.
- Crediting: "Real-time crediting of buckets, lugs, and bins" — harvest units credited to pickers as picked.
- Progress: "Bin counts to assess harvest progress"; "Real time data — get access to your bin totals anytime."
- Productivity: "Pinpoint pickers needing to improve; compare and assess the performance of teams"; connects picking quality with volume via the separate QC module and Analytics Pro.
- Costs: "Analyse costs by job, orchard, block and variety"; Analytics Pro tracks "bins/hour, picking speed vs defect rate, cost per acre, bins per acre, cost per bin by variety and block."
- Traceability: "Trace your fruit back to where it was picked"; "Scan, print bin tickets in the field to assign, add data"; "Scan tickets at the packhouse to connect data automatically to your existing systems"; "Provide early access to inventory data for managers and packhouses before they receive the fruit."
- Customer evidence: RJ Flowers ("we can trace our fruit right back to the picker and the block"; replaced handwritten bin cards and double/triple handling); Borton Fruit (~900 staff; "saving us about 90 minutes… each day, per crew leader").
- Fruit Quality AI (separate suite): fruit sizing and color grade in field/coolstore/packhouse, truck capture — harvest-adjacent quality, sold alongside.

### Fieldin (boundary-check sample; evidence layer A for what it is, B for the boundary)

- "Fieldin connects every spray, harvest, and tractor pass to real-time data—helping permanent crop operations spot issues early, improve execution, and maintain a clear record of every activity." Data source: smart sensors on existing equipment; "digitize the mechanized activities carried out in the field."
- Harvest appears as "Accelerate harvest": reduce task time, optimize labor costs, "actionable feedback to optimize harvest activities such as speeding up or slowing down tractors or shakers," supervisor reporting "across large geographical distances."
- Observed center: machine/crew execution (activity by block, speeds, operator efficiency, acres/hour, flow monitoring for material application). No bin-level product inventory, no picker crediting, no dock handoff observed on the fetched pages.
- Verdict: harvest-as-execution oversight over mechanized operations. Useful for the boundary: it manages the *performance of the harvest activity*, not the *product of the harvest*. Fits closer to an operations-telemetry / precision-agriculture pattern for the harvest window.

### Farmbrite (module-packaging sample; evidence layer A for packaging, B for capability)

- All-in-one farm software (livestock + crops + accounting + commerce). Harvest appears inside Crop Planning & Management and commerce: "automated picklists that integrate with harvests and inventory"; "Automate farm planning, management and yield estimates, track production." Harvest is a record/capability inside the farm system, not a product line. Confirms the module-variant packaging pattern and the small-farm tier.

### xFarm (module-packaging sample; evidence layer A for packaging)

- European farm-management app suite: field notebook, activities, machinery, irrigation, crop protection, economic management, logistics. No dedicated harvest-management product line visible on fetched pages; harvest is one of the activities. Confirms module packaging at the European farm tier.

## Cross-product Comparison

| Dimension | Croptracker | Hectre | Fieldin | Farmbrite / xFarm (suites) |
|---|---|---|---|---|
| Harvest event captured at pick, attributed to block/variety | ✔ harvest events; inventory tied to block/variety/picker | ✔ fast logging of bins; trace to block | ~ machine activity by block (no product event) | ✔ harvest records inside crop module |
| Picked product as identified inventory unit (bin/tag/ticket) | ✔ bin tags → digital inventory record; 4 tag workflows | ✔ bin tickets (scan existing or create; barcode/QR) | ✘ not observed | partial (harvest → inventory in Farmbrite) |
| Real-time totals / harvest progress | ✔ real-time totals by block/variety/row | ✔ bin totals anytime; bin counts for progress | ✔ live machine/crew progress | partial |
| Worker crediting from harvest records (piece-rate feed) | ✔ link harvest inventory to pickers for piece rate | ✔ real-time crediting of buckets/lugs/bins | ✘ (shift productivity, machine-side) | partial |
| Harvest estimation / projected yields | ✔ Harvest Estimates module (bin count or weight by block, over time) | not observed | not observed | "yield estimates" (Farmbrite) |
| Quality at harvest (incl. CV) | ✔ QC templates on lot; vision scans on bin | ✔ QC module; fruit sizing/color AI adjacent | ✘ | ✘ (mostly absent) |
| Handoff to next stage (dock/packhouse) | ✔ Receiving + Storage records link field inventory to packhouse | ✔ packhouse ticket scanning; early inventory for packhouses | ✘ | partial (orders/fulfillment) |
| Offline field capture | ✔ explicit | ✔ explicit | n/a (telemetry) | varies |
| Traceability output | ✔ lot codes + critical tracking events | ✔ fruit traced to picker and block | ~ digital block reports | partial |

Reading of the matrix: the two dedicated products agree on a stable spine (event capture at pick → credited bin/tag inventory → real-time progress → packhouse handoff → traceability), differ in emphasis (Croptracker: inventory/traceability-centric; Hectre: crediting/productivity-centric), while Fieldin (mechanized oversight) and the suites (harvest-as-module) fail or blur the spine — evidence that the spine is the Type, not the packaging.

## Canonical Abstraction

### L0 — Defining Invariant

The defining core is exactly three jointly-held structures:

1. **The harvest event as the unit of production record** — dated, attributed records of picking production bound to an identified production unit (block/field/orchard), capturing what was picked, where, when and how much, commonly by whom. Recorded at or near the moment of picking, accumulating into live totals. Remove → a crop-management season-closure record / agronomic yield log (harvest as a data point, not an operation).
2. **The harvested product as credited, traceable harvest inventory** — the pick materializes as identified units (bins, totes, crates, lugs, loads — a ticket/tag as the physical-digital link) each attributed to block and picker and tracked through crediting, movement and the handoff to the packhouse/processor/receiving point. Remove → a bare yield tally, or container logistics without harvest semantics.
3. **The harvest campaign as a managed whole** — the season's harvest is run and watched as one bounded operation: progress and accumulation observed in real time as it comes in, expectations (estimates) compared with actuals, field records reconciled against dock/packing receipts, totals closed per block/variety. Remove → per-event recording machinery with no managed campaign ("management" gone).

Jointly-held is load-bearing:

- 1 without 2 = yield log (crop-management closure capability)
- 2 without 1 = bin/container tracking tool
- 3 without 1+2 = generic progress board
- 1+2 without 3 = ticket-recording machinery with no managed season (the nightly-reconciliation problem the products themselves exist to remove)

Historical / market-sample check (§24-style): the pre-digital harvest system — crew tally sheets, bin tickets stapled to bins, load tickets to the winery/packing house, a harvest book of per-block season totals, maturity notes (sugar/pressure readings logged at pick) — satisfies all three legs on paper. Wine-grape and packing-house analog practices (scale tickets, weigh tickets) satisfy the handoff leg. The definition therefore names no mobile app, no barcode, no cloud: the ticket/tag is the modern realization of the identified credited unit. Machine-era broadacre harvest (yield monitors) also fits conceptually (event + measured production + season totals) though its product realization differs (see boundary).

### L1 — Common Mature Structure

Present in most modern products (both defining samples unless noted):

- worker crediting and piece-rate/hourly feed from the same harvest records (attribution of production to workers; payroll export lives on the labor side)
- quality assessment at harvest time: inspection templates against per-variety specs, increasingly computer-vision sizing/color; maturity readings (sugar/starch/pressure) captured on the record
- harvest estimation: projected yields by block (bin count or weight), tracked over the season to align crews, storage, sales (explicit in Croptracker; not observed in Hectre → held at single-product depth for the estimate *module*, though estimate-vs-actual comparison is the natural reading of the campaign leg)
- offline-first field capture with later sync
- dock/packhouse receiving and storage-location records (cold/CA rooms) extending the harvest inventory past the field
- reports/analytics: yield by block/variety, picker productivity, cost per bin/block/acre
- integration outward: payroll exports, packhouse systems

### L2 — Variant / Optional Structure

- field packing (labels, inventory, productivity at the point of packing) — packer-style operations
- harvest as a named module inside farm/crop management suites (Farmbrite, xFarm, Agrivi per prior pass) — packaging variant, not a different core
- mechanized-execution oversight: harvest managed through equipment telemetry (Fieldin) — shares the campaign leg, realizes the event leg as machine activity rather than product inventory
- processor/receiver-side harvest intake (winery/processor managing inbound grower fruit and grower payments) — plausible and referenced by the historical analog and by the unreachable AgCode's known category, but **not verified first-hand in this pass**; held unverified
- crew-size and crop-type range: bucket/lug-credited berry crews vs 2,000-bin orchard days vs machine-harvested nuts — same spine, different unit vocabulary

### L3 — Vendor-specific (research notes only)

- Croptracker module names (Harvest, Punch Clock, Field Pack, Quality Control, Storage Records, Receiving Records, Harvest Quality Vision™, Starch Quality Vision™, Crop Load Vision™, Predictive Packout Toolkit), the "3 mm" sizing-accuracy claim, pricing structure ($27.50/user/month, 10-user minimum), the CA/WA piece-rate compliance citations.
- Hectre "waterproof bin tickets on-the-go," bilingual interface, "98.7%" sizing accuracy claim, "3.8 billion pieces of fruit scanned," "22 countries," case-study numbers (Borton 90 min/day/crew leader; RJ Flowers trace-to-picker-and-block quote).
- Fieldin flow monitoring, ESG/GHG engine-hours angle, "750,000 acres" figure.

## Vendor-specific Findings

See L3 above; none of these enter the final document. The most tempting vendor patterns to over-generalize — and rejected — are below.

## Rejected Findings

- **"Harvest management = piece-rate labor management."** Both defining samples compute pay from harvest records, but both sell the workforce/payroll machinery as separate products/modules (Croptracker Punch Clock; Hectre Payroll/Timesheets), and the farm-labor pass independently established that Type's center as the workforce. In harvest management, worker attribution is *attribution of production* (who produced this bin), not management of the workforce. Rejected as definitional; kept as common capability with an explicit boundary.
- **"Harvest management = traceability platform."** Lot definition at harvest and critical tracking events exist in both samples, but the chain-wide cross-partner ledger is the food-traceability Type; harvest management is one event source plus field-side custody. Rejected as definitional.
- **"Harvest management = crop management's harvest page."** The suites show harvest records as a capability; the dedicated products show an operation system-of-record with inventory custody and campaign management that the crop-management pass itself assigned to this leaf. Keep-both with the closing-phase/operation seam.
- **"Bin/barcode tagging is definitional."** The tag is the modern realization; the analog ticket and the bulk-record workflow (Croptracker "record in bulk") show the invariant is the identified credited unit, not any capture hardware.
- **"Estimation belongs in the core."** Explicit in one defining sample only; held L1.

## Boundary Findings

| Neighboring Type | Seam | Removal test |
|---|---|---|
| Crop Management | crop-season lifecycle vs harvest operation; harvest is crop management's closing record, but harvest management holds no growing-season plan/inputs/spray record | Remove crop plan/inputs/spray → still harvest management; remove event+inventory+campaign and keep season ops → crop management |
| Farm Labor Management | workforce vs product: crews/hours/pay owed vs what was picked and where it went; meet at crediting ("time against inventory") | Remove worker records/scheduling/pay → harvest management intact (crediting stays as attribution); remove product/inventory and keep workforce → farm labor |
| Produce Packing House Management (unprocessed sibling) | the dock: harvest management ends at handoff (receiving/early inventory); packing-line processing, food safety, finished-goods inventory is the packhouse's | Remove field-side picking/event capture, keep pack lines/GMP → packhouse; keep field-side and stop at dock → harvest management. Flag for that pass |
| Food Traceability Platform | one event source vs chain-wide join: harvest events feed the ledger; no cross-partner linkage duty here | Remove cross-partner retrieval, keep harvest op → still harvest management; keep chain ledger only → traceability |
| Precision Agriculture Platform | product inventory vs machine execution: telemetry realizes the harvest as machine activity; no credited bins | Remove equipment telemetry → harvest management intact; remove product inventory and keep machine loop → precision-agriculture pattern |
| Grain Management | harvest operation vs stored-grain protection: different object (picked product vs grain in storage) | condition sensing/aeration absent → still harvest management |
| Farm Management Platform | harvest operation vs whole-farm business (finance, marketing, payroll) | Remove finance/grain-marketing/payroll → still harvest management |
| Orchard / Vineyard Management | crop-scoped management variants; harvest appears as one phase | leaf-level distinction; harvest management is crop-agnostic within specialty/high-value |
| Winery Management | adjacent: fruit intake at crush is the receiving end of the harvest handoff; winery production machinery is a different Type | (analog scale-ticket continuity noted; no first-hand sample this pass) |
| Inventory Management (generic) | harvest inventory is perishable, field-born, and production-attributed; not a generic stockroom | no production-unit attribution / season shape → generic inventory |

## Uncertainties

- Processor/receiver-side pole (winery/processor running harvest intake and grower payment): supported only by the analog pattern and the unreachable AgCode's known category; **unverified first-hand** — kept out of the final document's claims.
- Broadacre/row-crop harvest management as a distinct product population (vs yield-monitor/telemetry realization): not sampled; the final document speaks of machine-executed harvest only at Fieldin-level evidence and generalizes cautiously.
- Harvest estimation depth: single defining sample carries a dedicated module; estimate-vs-actual as a campaign-level behavior is inferred, not independently evidenced twice.
- Exact compliance mechanics (piece-rate top-ups, incidental-task pay) are vendor-cited and region-specific; qualitative only.
- Help-center-level documentation (field-level state machines, permission models) was not reachable for any sample; all evidence is product/marketing-page level. No numeric operational limits are asserted in the final document.

## Final Synthesis

Harvest Management is the grower's/operator's **harvest-operation system of record**: it turns the act of picking into an attributed production record (harvest events tied to block, variety, picker), materializes that production as identified, credited harvest inventory (the bin/tag/ticket) that stays traceable from field to dock, and manages the harvest as a bounded campaign watched in real time — progress, estimates vs actuals, and reconciliation with the receiving packhouse. Its neighbors own everything around it: the crop-season behind it (crop management), the workforce in it (farm labor management), the chain ahead of it (food traceability), the machines doing it (precision agriculture / operations telemetry), and the packing line after it (produce packing house management). The leaf is a genuine Type, not a capability: dedicated product lines exist and their shared spine differs from every neighbor's center. Keep-both with crop-management and farm-labor-management on the recorded seams; hand the dock seam to produce-packing-house-management.
