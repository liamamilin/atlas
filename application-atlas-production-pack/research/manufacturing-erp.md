# Research Notes — Manufacturing ERP

Research date: 2026-09-09
Directory leaf: Manufacturing ERP (§16 Engineering, Manufacturing & Industrial)
Slug: manufacturing-erp

## Research Goal

Understand what a Manufacturing ERP actually is as an application type: which structures make it an ERP (the inherited spine), which structures make it specifically *manufacturing* (the production layer), how production connects to commercial and financial records, and where its boundaries sit against generic ERP, Food Manufacturing ERP, MES, Production Planning / APS, WMS, PLM/BOM management, and the quality/maintenance siblings.

## Initial Boundary

- Working hypothesis: Manufacturing ERP = the integrated business back office (finance, purchasing, sales, inventory on one data core with automatic financial posting) of a manufacturer, plus manufacturing-native structures held as first-class objects: the build definition (bill of materials + routing/work centers), the production order as the unit of manufacture, and production costing reconciled into the ledger.
- Prior-pass context:
  - The ERP pass (§10, 2026-09-06) defined the parent Type (shared data core + operational documents + automatic financial posting + multi-function coverage) and explicitly recorded: "Manufacturing ERP / Agribusiness ERP (§16/§20 leaves) confirmed as industry-edition Variants of this same Type, not separate structures." In the parent's core model, the production structure (BOM/routing/work centers/production order) appears "where manufacturing is in scope," and production depth is listed as *optional* for generic ERP.
  - The food-manufacturing-erp pass (§20, 2026-09-08) hung a JOINT REVIEW flag on this leaf: "food manufacturing ERP is the food-industry edition of manufacturing ERP; the production structure is process/recipe-batch rather than discrete BOM assembly. BatchMaster explicitly spans food AND chemicals/nutraceuticals with one structure — evidence that recipe/batch is the process-manufacturing structure, with food adding the lot/shelf-life/traceability emphasis."
  - The WMS pass and MES-adjacent evidence (ParityFactory, food pass) established: shop-floor/warehouse execution products integrate with the ERP, which remains the commercial/inventory/financial system of record.
- Nearest neighbors: Enterprise Resource Planning / ERP (§10 parent), Food Manufacturing ERP (§20 sibling), Agribusiness ERP (§20 sibling), MES (§16), Production Planning / APS (§16), Shop Floor Management (§16), WMS (§10), PLM (§16), Bill of Materials Management (§16), Engineering Change Management (§16), Manufacturing QMS (§16), CMMS/EAM (§16), Inventory Management System (§10), Accounting Software (§08).

## Research Questions

1. What are the manufacturing-specific master data structures, and how are they held? (BOM, routing, work centers/resources)
2. What is the production order, and what is its lifecycle? Which states gate which actions?
3. How does planning work? (demand → planned production/purchase orders; MPS/MRP; multilevel explosion)
4. How does production costing work? (standard vs actual, WIP, variances, rollup)
5. How is shop-floor work recorded, and where does the ERP stop and MES begin?
6. How do sales orders connect to production (make-to-order), and how is availability promised?
7. What is inherited from the ERP spine, and what is manufacturing-specific?
8. What varies across products: production modes (MTS/MTO/ETO), discrete vs process, substrate (manufacturing-first vs general ERP + module), tier, deployment?
9. Historical check: would an MRP II-era system (1980s) satisfy the definition? Would regional/platform-native products?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

1. **Microsoft Dynamics 365 Business Central (Manufacturing area, Premium experience)** — mid-market platform-native general ERP where manufacturing is a deep application area; Tier-1 documentation on Microsoft Learn (reachable).
2. **Odoo Manufacturing (MRP app)** — open-source, modular SMB ERP; Tier-1 documentation (official docs repository, reachable).
3. **MRPeasy** — lightweight cloud MRP/manufacturing ERP for small manufacturers (10–200 employees, per vendor); Tier-1 user manual (reachable); regional European (Estonian) vendor.
4. **Epicor Kinetic** — mid-market manufacturing-first ERP ("global cloud ERP built for manufacturers", "specialized for discrete, make-to-order manufacturing"); Tier-2 product-page evidence only.
5. **SAP S/4HANA** — enterprise-tier market anchor; deep pages unreachable this pass (2× 404) and the parent pass recorded the SAP Help Portal as unreachable; positioning-level evidence only, inherited from the parent pass.

Rejected/considered: Acumatica Manufacturing Edition (blocked, 405 ×2 — abandoned per network rule); BatchMaster (process-manufacturing pole — covered via the food pass's evidence, subpages were 403 there); Katana/Fishbowl (inventory-first, weaker ERP spine — not sampled).

## Sources

Tier-1 (fetched 2026-09-09):

- Microsoft Learn — Dynamics 365 Business Central: Manufacturing overview (production-manage-manufacturing); About production orders (production-about-production-orders); About planning functionality (production-about-planning-functionality); About finished production order costs (finance-about-finished-production-order-costs); Create production BOMs (production-how-to-create-production-boms); Set up work centers and machine centers (production-how-to-set-up-work-and-machine-centers); docs TOC (toc.json).
- Odoo documentation repository (github.com/odoo/documentation, master branch): manufacturing.rst (app overview); basic_setup/bill_configuration.rst (BoM); basic_setup/mo_costs.rst (MO costs); workflows/use_mps.rst (Master Production Schedule); TOC of manufacturing section (basic_setup, advanced_configuration, workflows, shop_floor, subcontracting, reporting).
- MRPeasy: homepage (positioning, module list); User Manual — Getting Started (mrpeasy.com/resources/user-manual/) with full section tree (CRM, Production planning, Stock, Procurement, Reporting, Settings, Accounting; professional/enterprise function lists).

Tier-2:

- Epicor — Kinetic product page (epicor.com/products/enterprise-resource-planning-erp/kinetic/): positioning, capabilities list, industries, packaging (bundles), MES sold separately.

Unreachable / limited:

- SAP — manufacturing solution pages 404 ×2 this pass; parent pass recorded SAP Help Portal unreachable (JS-only shell). SAP held as market anchor only.
- Acumatica — 405 ×2 (bot protection), abandoned.
- Wikipedia (Manufacturing resource planning) — fetch timed out; historical check kept conceptual (see Historical Check below).

## Product A — Microsoft Dynamics 365 Business Central (Manufacturing, Premium)

Evidence layer: A (directly observed, Tier-1).

Key observations:

- **Positioning**: "Manufacturing in Business Central helps you plan, schedule, execute, and analyze production." Manufacturing is a **Premium-experience** feature (edition gating — packaging evidence, not structure).
- **Build definition**: "Use production BOMs to define components, routings to define operations, and work and machine centers to model capacity and costs."
  - Production BOM: "holds master data that describes the components and subassemblies used in the production of an item." **"In some industries, production BOMs are referred to as recipes or formulas"** — direct Tier-1 cross-vocabulary evidence for the process-manufacturing pole inside a discrete-oriented ERP.
  - BOM lines: item or sub-assembly (production BOM) or phantom BOM; quantity per; scrap %; routing link code (binds component to operation). BOM **status lifecycle**: New / Under Development / **Certified** (must be certified to be used in production or planning). **Versions** with starting-date validity ("valid until the next version becomes valid"). Phantom BOMs: structural grouping without a separate production order or item record.
  - Standard cost rollup: "Calc. Production Std. Cost" from the item card; Standard Cost Worksheet for bulk updates; unit cost of parent computed from components + routing costs.
  - Assembly BOMs distinguished from production BOMs (assembly = simple kitting with basic resources, no work centers).
- **Capacity model**: hierarchy **work center group → work center → machine center**; shop calendars; capacity, efficiency, queue/setup/run/wait/move times; unit cost = direct unit cost + indirect cost % + overhead rate; flushing method per resource; consolidated calendar; **capacity-constrained resources** (finite loading for bottlenecks) vs default **infinite capacity scheduling**.
- **MES boundary (direct quote)**: "Business Central doesn't support detailed shop floor control. It plans for a feasible utilization of resources by providing a rough-cut schedule, but doesn't automatically create and maintain detailed schedules based on priorities or optimization rules." — the ERP's own documentation draws the MES/APS seam.
- **Production order**: "Use production orders to manage the conversion of purchased materials into manufactured items. Production orders route work through various work or machine centers on the shop floor." Created from Items + Production BOMs + Routings + Machine centers + Work centers; created manually or generated from Planning Worksheet / Sales Order Planning / Order Planning; automatically reserved and tracked to source when generated by planning.
- **Status lifecycle**: **Simulated → Planned → Firm Planned → Released → Finished**. Status controls what you can do: Simulated = costing/quotes only, invisible to planning; Planned = planning-generated suggestion, deleted on next planning run; Firm Planned = commitment placeholder, survives planning; Released = can record actual consumption/output (flushing only on released orders); Finished = fixed, costing lifecycle completes, reopen restricted (once, with restrictions).
- **Execution recording**: consumption, output, scrap, operation time recorded in **production journals** (combines consumption + output for one released order) or batch journals; or automatically via **flushing methods** (Manual / Forward / Backward) copied from item and work center cards; routing link codes make consumption follow operation output. "Consumption quantities are posted as negative item ledger entries, output quantities are posted as positive ledger entries, and times spent are posted as capacity ledger entries."
- **By-products**: no dedicated feature; recorded as negative consumption entries crediting WIP.
- **Planning**: "The planning system takes all demand and supply data into account, nets the results, and creates suggestions for balancing supply to meet demand." Gross-to-net calculation; planned order releases scheduled from routing (manufactured) or lead time (purchased); action messages; planning parameters on items/SKUs (reordering policies, safety stock, order modifiers); **multilevel production orders** — BOM explosion creates planned production orders per level, lower levels scheduled to finish before the parent starts; approaches: Regenerative Plan (MPS/MRP), Net Change Plan, Order Planning (MTO/one-off), Requisition Worksheet (purchasing); warnings (Emergency/Exception/Attention).
- **Costing**: "A finished production order brings together the actual cost of consumed materials, capacity, subcontracting, and overhead for the items produced. Cost adjustment reconciles those costs with work in process and inventory and calculates variances when you use standard costing." Only **Finished** orders are considered for cost adjustment. WIP: consumption + labor + overhead into WIP; on completion WIP reduced by standard cost; variances net to zero via Adjust Cost - Item Entries.
- **Connections**: subcontracting (outsource operations, subcontractor dispatch list); quality management (inspect production output); warehouse (pick for production, put away output); inventory; purchasing; analytics (Power BI manufacturing app: production order WIP, work/machine center load, capacity variance, scrap).

## Product B — Odoo Manufacturing (MRP app)

Evidence layer: A (directly observed, Tier-1 docs repository).

Key observations:

- **Positioning**: "Odoo Manufacturing helps manufacturers schedule, plan, and process manufacturing orders. With the work center control panel, put tablets on the shop floor to control work orders in real-time and allow workers to trigger maintenance operations, feedback loops, quality issues, etc." IoT Boxes (MES) referenced as separate doc.
- **BoM**: "documents specific components and their respective quantities that are needed to produce or repair a product... serve as blueprints for manufactured goods and kits and often include production operations and step-by-step guidelines." BoM per product (+ optional variant), quantity produced per BoM, **Reference** to differentiate alternative BoMs for the same product (GPU-shortage example), BoM type "Manufacture this product" (vs kit).
- **Operations**: added on the BoM's Operations tab (Work Orders feature); operation has **Work Center**, cost based on actual vs theoretical time, duration computation (fixed vs computed from last N work orders). Components can be "Consumed in Operation".
- **Instructions as quality control points**: BoM instructions become QCPs — instruction text, take a picture, register consumed materials, register production, print label, pass-fail, measure within tolerance. Quality app is a sibling module.
- **Work centers**: cost per hour (per workcenter + per employee); shop-floor tablets/control panel.
- **Manufacturing steps**: one-step / two-step / three-step manufacturing (manufacture only; + components transfer; + finished-goods transfer) — warehouse-integration depth.
- **MO costs**: distinguishes **MO cost** (should-cost from BoM configuration: components + operations + work center costs + employee costs) vs **real cost** (actual). Component cost from average purchase cost across POs; work center hourly cost; employee hourly cost.
- **MPS**: "plan long-term replenishment for products against a manually-adjustable demand forecast... generating suggested replenishment quantities based on forecasted demand and on user-specified stock targets." **"Adding a product to the MPS does not automatically create a purchase or manufacturing order"** — suggests, user commits. MTO strategies and reordering rules are the automatic alternatives.
- **Workflow breadth** (TOC): MPS, continuous production, work center time off, scrap, manufacturing backorders, split/merge MOs, unbuild orders, byproducts, dismantle products, continuous improvement, manufacture with lots/serials; subcontracting; shop floor; reporting; advanced configuration (work order dependencies, product variants, kit shipping).

## Product C — MRPeasy

Evidence layer: A (directly observed, Tier-1 user manual).

Key observations:

- **Positioning**: "The AI-powered MRP software for small manufacturers. Ideal for companies with 10–200 employees." Self-branded "Manufacturing ERP" (G2 badge "MRPeasy Manufacturing ERP"). "Suitable for both make-to-stock and make-to-order production."
- **Structure**: eight sections — **CRM** (sales and order management), **Production planning** (production planning and management), **Stock** (inventory), **Procurement** (purchasing), **Dashboard**, **My production plan / Internet-kiosk** (real-time shop-floor reporting by workers), **Settings**, **Accounting** ("standard accounting module").
- **Items**: procured items get **Purchase Terms** (vendors, cost, lead time); manufactured items get **BOM + Routing**. Item detail includes BOM and Routing tabs; Item Cost.
- **Manufacturing Order (MO)**: created manually, from reorder point (Stock → Critical on-hand), from forecasting, or generated from customer orders (MTO: one MO per CO line, one MO for multiple COs, or manual MO booked to the CO). MO details; production schedule; rescheduling.
- **Workstations**: workstation details, workstation groups, load/summary reports — the capacity model.
- **Booking/reserving**: "Items must be booked before they can be used in production"; booking reserves items from current stock **or from planned supply** (future PO or MO); unavailable items generate demand automatically. In-stock vs expected; available vs booked.
- **Stock**: stock lot tracking (batches), serial numbers, storage locations, write-offs, transfers, shipments, inventory counts; movement reports.
- **Shop floor**: "My Production Plan" for workers (MO details for worker), Internet-kiosk for shared-terminal reporting; "MES for Shop Floor Reporting" marketed as a feature page — light MES inside the product.
- **Tiered packaging**: **Professional Functions** (co-product BOM, disassembly BOM, expiry date, matrix BOM / product configurator, quality control, serial numbers, subcontracting, overlap/parallel operations, piece payment, non-inventory items, unscheduled MOs) and **Enterprise Functions** (approval system, backward scheduling, barcodes, maintenance management, **MPS**, multi-stock/production sites, packing, RMA, **revision/version control (VCS)**, sales forecasting, sales management, 2FA) — capability gating evidence.
- **Accounting**: "standard accounting module" — the financial spine present but lightweight; integrations to QuickBooks/Xero for fuller accounting.

## Product D — Epicor Kinetic

Evidence layer: A at positioning level (Tier-2 product page only; no operational mechanics asserted).

Key observations:

- **Positioning**: "Global Cloud ERP Built for Manufacturers"; "an industry-tailored, cognitive ERP"; **"Specialized for discrete, make-to-order manufacturing"**; "Cloud-focused solution with flexibility for on-premises and hybrid deployments."
- **Process breadth**: "Support Any Manufacturing Process — Discrete Manufacturing / Process Manufacturing / Make-to-Order."
- **Industries**: aerospace & defense, construction & engineering, electronics & high-tech, fabricated metals, furniture & fixtures, industrial machinery, medical devices, metal service centers, rubber & plastics.
- **Capability areas** (product page): Financials; Business Intelligence and Analytics; Supply Chain Management; **Planning and Scheduling** ("complex planning and scheduling needs... greater operational visibility"); **Production Management** ("efficient production control capabilities and Smart Factory innovation"); Services and Assets; IoT; Risk and Compliance; Omnichannel Sales; CRM; **Product Data Management** ("optimize your product lifecycle management processes"); Project Management ("detailed estimation, planning, scheduling, costing... for complete control and analysis of any project").
- **Demand/supply**: "Manage demand against supply with advanced tools for forecasting, **MRP**, Advanced Planning and Scheduling, and sourcing."
- **MES sold separately**: Epicor Advanced MES is a distinct product under "Manufacturing Execution (MES)" — the ERP/MES seam is a packaging fact at this vendor.
- **Packaging**: "Choose Your Platform Core → Choose Your Cloud Package → Choose Your Concurrent Users" (bundles).

## Product E — SAP S/4HANA (market anchor only)

Evidence layer: positioning only. Manufacturing solution pages returned 404 ×2 this pass; the parent ERP pass (2026-09-06) recorded the SAP Help Portal as unreachable (JS-only shell) and used the S/4HANA product page at positioning level. No operational claims about SAP manufacturing mechanics are made in this research. SAP is retained in the sample as the enterprise-tier anchor: the largest manufacturing-ERP installed base globally, and the vendor whose S/4HANA manufacturing vocabulary (BOM, routing, work center, production order, MRP) matches the structures documented at the Tier-1 products.

## Cross-product Comparison

| Structure | Business Central | Odoo | MRPeasy | Epicor Kinetic |
|---|---|---|---|---|
| Integrated back office (finance/purchasing/sales/inventory, one core) | Yes (full ERP; manufacturing = Premium area) | Yes (modular apps incl. Accounting, Purchase, Sales, Inventory) | Yes (8 sections incl. Accounting module; QuickBooks/Xero integrations) | Yes (Financials capability; ERP suite) |
| Build definition | Production BOM (+versions, phantom, certification) + Routing + work/machine centers | BoM (components + operations + work centers; reference for alternatives) | BOM + Routing on manufactured items; workstations | Production Management / Product Data Management (positioning level) |
| Production order as unit of manufacture | Production order, 5-status ladder | Manufacturing Order (MO), split/merge/backorder/unbuild | Manufacturing Order (MO), booking/reserving | Production Management (positioning level) |
| Execution recording | Production/consumption/output journals; flushing methods; capacity ledger entries | Work orders on shop-floor tablets/control panel; QCP steps | My Production Plan + Internet-kiosk worker reporting | (MES separate product) |
| Planning | MPS/MRP regenerative + net change + order planning; multilevel explosion; action messages | MPS (manual suggestion) + MTO + reordering rules | Reorder points, forecasting, requirements reports, MPS (Enterprise tier) | Forecasting, MRP, APS (positioning level) |
| Production costing | Standard cost rollup; WIP; variances on Finished; Adjust Cost batch | MO cost (should) vs real cost; component cost from POs; work-center hourly cost | Item cost; MO cost estimation at quote | Costing within Production Management (positioning level) |
| Subcontracting | Yes (operations outsourced, dispatch list) | Yes (subcontracting section) | Yes (Professional function) | Supply chain capability (positioning) |
| Lot/serial tracking | Item tracking (inherited inventory feature) | Lots/serials in manufacturing workflows | Stock lots + serial numbers (Professional) | (positioning) |
| Quality | Quality management module (output inspection) | Quality control points on BoM instructions; Quality app | Quality control (Professional function) | (positioning) |
| BOM revision control | BOM versions with validity dates + certification status | BoM reference (alternatives); PLM app separate | Revision/Version Control System (Enterprise function) | Product Data Management (positioning) |
| Shop-floor surface | Production journals (desktop); warehouse pick/put-away | Tablets / work center control panel | Worker terminal + Internet kiosk | Connected Worker / MES separate |
| MES boundary | Explicit: "doesn't support detailed shop floor control... rough-cut schedule" | IoT Box (MES) separate doc; control panel is light | "MES for Shop Floor Reporting" marketed as feature | Advanced MES separate product |
| Tier / packaging | Premium experience gating | Modular apps; edition tiers | Professional/Enterprise function tiers | Bundles (core + package + users) |
| Deployment | Cloud (SaaS) | Cloud or self-hosted | Cloud SaaS | Cloud, on-prem, hybrid |

Cross-product commonalities (evidence layer B):

1. All sampled products carry the ERP spine: finance + purchasing + sales + inventory on one data core (BC full ERP; Odoo modular apps; MRPeasy sections incl. Accounting; Epicor Financials).
2. All sampled products hold the build definition as master data attached to the manufactured item: components (BOM) + operations on resources (routing/work centers/workstations).
3. All sampled products run production through a named order object (production order / manufacturing order) with a lifecycle from planning through execution to completion.
4. All sampled products tie production to inventory transactions (consumption as issues, output as receipts) and to cost (should-cost vs actual; WIP/variances where documented).
5. All sampled products include demand-driven planning machinery (MRP-class: reorder points, forecasting, MPS/MRP, requirements reports) — universal in sample, but realization depth varies widely.
6. All sampled products include shop-floor recording in some form (journals, tablets, worker terminals) — but all sampled vendors either bound its depth explicitly (BC: rough-cut only) or sell deep MES separately (Epicor), or market it as a light feature (MRPeasy).
7. All sampled products gate capability depth by tier/packaging (BC Premium; Odoo apps/editions; MRPeasy Professional/Enterprise; Epicor bundles).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **The integrated business back office on one data core** (the inherited ERP spine): finance, purchasing, sales, and inventory as connected records, with operational documents posting automatically into the ledgers. Remove → a production planning/scheduling tool or shop-floor tool with no business record.
2. **The build definition as master data**: the manufactured product held as a makeable structure — a bill of materials (components and quantities, with versions) plus a routing (operations performed at work centers/resources with capacity and cost). The product is defined not only by what it is but by how it is made. Remove → a trading/distribution ERP (products bought and sold, not made).
3. **The production order as the unit of manufacture**: a scheduled execution of a build definition that advances through a status lifecycle (planned → released → executed → finished), consumes materials, records operations and output, and reconciles its costs into the ledger (work in process, variances). Remove → a planning spreadsheet or costing calculator; the "management" of manufacturing is gone.

Jointly-held load-bearing:

- 1 alone = the parent ERP Type (generic ERP).
- 2 alone = BOM/product-structure management (PLM-adjacent).
- 3 alone = production scheduling/tracking tool.
- 1+2 without 3 = product data + back office with no execution unit.
- 2+3 without 1 = production management without the commercial/financial record (MES-lite territory).
- 1+3 without 2 = work orders for unstructured work (job costing without a build definition — approached by the ETO variant, where the build definition is created per job; the structure exists, but job-specific rather than catalog-standing).

### L1 — Common Mature Structure

Present in essentially all mature products; makes the Type practical but does not define it:

- **MRP-class planning**: demand (sales orders, forecasts) + build definitions + inventory → suggested production and purchase orders; multilevel BOM explosion; master production schedule; action messages; planner commits suggestions into firm orders.
- **Shop-floor recording**: worker-facing surfaces (terminals, tablets, kiosks, journals) reporting consumption, output, time, scrap against released orders.
- **Production costing depth**: standard cost rollup from BOM + routing; actual cost collection; WIP accounting; variance analysis on completion.
- **Subcontracting**: routing operations outsourced to vendors, with component supply and subcontractor costs inside the production order.
- **Lot/serial tracking** on components and finished goods (inherited inventory capability, production-relevant).
- **Quality gates**: inspections/holds tied to receiving, in-process steps, and output.
- **Build-definition governance**: BOM/routing versions with validity dates, certification/approval states, revision control.
- **Capacity views**: load on work centers from planned and released orders; finite-loading options for bottlenecks (rough-cut).
- **By-products/co-products and scrap** recording.
- **Sales-order linkage**: make-to-order generation of production orders from order lines; availability/lead-time promising against planned supply.
- **Multi-site / multi-warehouse** operation.
- **Analytics/reporting** over production, capacity, cost, and inventory.

### L2 — Variant / Optional Structure

- **Production mode**: make-to-stock, make-to-order, assemble-to-order, engineer-to-order (job-specific BOMs), repetitive/flow.
- **Discrete vs process**: BOM/routing assembly vs recipe/formula batch production (the BC documentation itself notes BOMs "are referred to as recipes or formulas" in some industries; the food pass documented the process pole in depth).
- **Substrate**: manufacturing-first suite (Epicor) vs general ERP with a deep manufacturing area (Business Central Premium) vs modular open-source apps (Odoo) vs lightweight cloud MRP (MRPeasy).
- **Tier and packaging**: edition/function gating (Premium experience; Professional/Enterprise functions; app modules; bundles).
- **Deployment**: cloud SaaS, on-premises, hybrid, self-hosted.
- **Depth add-ons**: product configurators (matrix BOM), APS optimization, MES integration, IoT/machine data, AI assistance, PLM integration, project-based ETO job costing.

### L3 — Vendor-specific Structure (Research Notes only)

- **Business Central**: Simulated/Planned/Firm Planned/Released/Finished status ladder; flushing methods (Manual/Forward/Backward) with routing link codes; phantom BOMs; work center groups + consolidated calendars; capacity-constrained resources with critical load % and dampener; by-products via negative consumption; Power BI manufacturing app; Premium-experience gating; planning warnings (Emergency/Exception/Attention); Missing SKU Planning Policy.
- **Odoo**: BoM types (manufacture/kit); one/two/three-step manufacturing; work center control panel tablets; QCP-typed instructions (picture/measure/pass-fail/register); MO cost vs real cost; component cost auto-derived from PO average; MPS as manual suggestion (explicitly not auto-creating orders); unbuild/dismantle orders; split/merge MOs; manufacturing backorders.
- **MRPeasy**: eight-section structure; booking/reserving from stock or planned supply; Internet-kiosk shared-terminal reporting; Professional/Enterprise function tiers; co-product/disassembly/matrix BOMs as paid functions; "standard accounting module" with QuickBooks/Xero handoff.
- **Epicor**: "cognitive ERP" positioning; Prism AI agents; bundles packaging (platform core + cloud package + concurrent users); Advanced MES as separate product; industry bundles.

## Vendor-specific Findings

- BC's five-status production-order ladder and flushing-method machinery are product-specific realizations of the generic planned→released→finished lifecycle; other products use different state sets (Odoo MO states, MRPeasy MO scheduling states) — the *pattern* (planning objects early, costing objects at the end, decreasing mutability) is the common structure, not the labels.
- Odoo's "MPS does not automatically create orders" is a product design choice; BC's planning worksheet *does* create (planned) orders that are then carried out. Both realize "planning suggests, people commit" at different points.
- MRPeasy's "standard accounting module" shows the spine can be lightweight at the SMB pole, with fuller accounting delegated to integrated products (QuickBooks/Xero) — the spine remains structurally present (transactions, invoices, financial reports) even when depth is delegated.
- BC's "recipes or formulas" note and the food pass's BatchMaster evidence jointly establish that the process-manufacturing vocabulary lives inside the same build-definition structure — the discrete/process split is a variant axis, not a Type boundary.

## Boundary Findings

1. **vs Enterprise Resource Planning / ERP (§10 parent)**: industry-edition variant relationship, already ratified by the ERP pass ("Manufacturing ERP / Agribusiness ERP confirmed as industry-edition Variants of this same Type"). Test: remove the build definition and the production order → a generic ERP remains; elevate them from optional depth to the center of gravity → a Manufacturing ERP. In the parent's core model, production structure appears "where manufacturing is in scope" and production depth is listed as *optional*; in this Type it is the defining center. The leaf remains documentable because the manufacturing structures are stable and nameable across independent vendors (all four sampled products carry them as first-class furniture).
2. **vs Food Manufacturing ERP (§20 sibling) — JOINT REVIEW DISCHARGED (keep-both ratified)**: the food pass's flag asked whether the production structure is "process/recipe-batch rather than discrete BOM assembly." This pass's evidence resolves it: Manufacturing ERP spans **both** discrete (BOM + routing assembly) and process (recipe/formula batch) production — BC's own Tier-1 documentation states production BOMs "are referred to as recipes or formulas" in some industries, and the food pass documented BatchMaster spanning food AND chemicals with one recipe/batch structure. Food Manufacturing ERP is therefore the **food-industry edition** of this Type: same ERP spine and production-order machinery, with recipe/batch production and the lot/shelf-life/traceability layer elevated to the center (its L0), while generic Manufacturing ERP centers the build definition + production order + costing machinery without the food-material layer. Keep both leaves; cross-reference.
3. **vs MES (§16)**: the sharpest operational seam, documented from three directions: (a) BC's own docs: "Business Central doesn't support detailed shop floor control... rough-cut schedule"; (b) Epicor sells Advanced MES as a separate product beside Kinetic; (c) MRPeasy markets shop-floor reporting as a light "MES" feature inside the ERP. Seam: the ERP's production order **plans and costs** at business level (what to make, when, at what cost, posting into the books); MES **executes and controls** at operation/machine level in real time (sequencing, machine integration, operator workflows). Light shop-floor reporting inside the ERP is standard capability; deep execution is the sibling Type.
4. **vs Production Planning / APS (§16)**: BC's finite-capacity scheduling is explicitly "rough-cut" and its planning is replenishment-level (net requirements → planned orders); Epicor lists Planning and Scheduling as a capability area and APS as an advanced tool. Seam: optimization-depth planning (constraint-based scheduling, sequencing) is the APS leaf; ERP planning derives supply suggestions from demand.
5. **vs WMS (§10)**: ratified in the parent and WMS passes; BC includes warehouse pick-for-production and put-away-of-output as *integration* surfaces, while directed warehouse execution (bins, waves, device-directed work) is the WMS leaf's center.
6. **vs PLM (§16) / Bill of Materials Management (§16) / Engineering Change Management (§16)**: the ERP holds the **manufacturing-side** build definition as a production master (versions with validity dates, certification states — BC evidence; revision control as an Enterprise function — MRPeasy evidence). The engineering-side product data lifecycle (CAD-linked structures, change workflows, ECOs) is the PLM/ECM territory. The seam is the record's purpose: made-vs-designed.
7. **vs Manufacturing QMS (§16) / CAPA / SPC**: quality in the ERP is gates on the material flow (inspection statuses, holds, output inspection — BC/Odoo/MRPeasy evidence); the quality-management discipline (document control, audits, CAPA machinery) is the sibling Type.
8. **vs CMMS / EAM (§16)**: maintenance of the equipment that produces vs production of goods. Odoo references maintenance triggers from the shop floor (work center control panel) and MRPeasy sells Maintenance Management as an Enterprise function — integration hooks, not the center.
9. **vs Agribusiness ERP (§20 sibling)**: consistent with the agribusiness pass — primary production (land, crops, grower commerce) vs transformation of materials into products. Overlap at farm-level processing.
10. **vs Inventory Management System (§10) / Accounting Software (§08)**: inherited from the parent pass — no build definition/production orders (inventory tool); no operational documents posting into it (accounting tool).

## Historical Check (per §24)

Would older, regional, platform-native, or differently positioned products still fit the L0?

- **MRP II lineage (1980s)**: the classic MRP II structure — bill of materials, routing, work centers, master production schedule + MRP + capacity planning, shop (production) orders, standard costing, closed loop into financials — satisfies all three L0 legs. The sampled products' own Tier-1 vocabulary (production BOM, routing, work center, shop calendar, MRP, production order, standard cost, WIP) **is** the MRP II vocabulary carried forward unchanged into modern cloud products; the definition adds nothing era-specific.
- **Platform-native heritage**: Business Central's manufacturing model is the direct continuation of Dynamics NAV (and pre-NAV PLATO/Navision) manufacturing; same structures.
- **Regional pole**: MRPeasy is an Estonian vendor serving small manufacturers internationally; Odoo (Belgian open-source) carries the same structures in a modular shape. Both satisfy the L0 without US-enterprise packaging.
- **Definition hygiene**: the L0 names no cloud, no real-time machine integration, no AI, no specific planning algorithm, no graphical scheduler, no barcode/RF machinery. A 1980s MRP II installation and a 2026 cloud product both satisfy it; all of those are era machinery (L1/L2).
- Historical-check verdict: **passed**; no over-fitting to the current cloud/SMB implementation.

## Uncertainties

1. SAP unreachable this pass (404 ×2; parent-pass limitation recorded) — the enterprise pole is held as market anchor only; no operational claims about SAP manufacturing mechanics. The enterprise-tier realization of the L0 is inferred from the parent pass's SAP positioning evidence plus market structure, and is flagged as such.
2. Epicor evidence is product-page level (Tier-2). Its capability list and MES-separate packaging are asserted; no operational mechanics (order lifecycles, costing methods) are claimed.
3. Acumatica blocked (405 ×2) — the "vertical layer on a general ERP platform" substrate pole is described from the parent pass's packaging-variant evidence, not from a fresh sample.
4. Wikipedia MRP II fetch timed out — the historical check rests on the sampled products' own vocabulary continuity (Tier-1) rather than an external historical source; held conceptual.
5. Process-manufacturing depth inside generic Manufacturing ERPs varies; this pass documents the process pole via BC's recipe/formula note (Tier-1) and the food pass's BatchMaster evidence (prior pass). No independent process-ERP vendor was fetched this pass.
6. Exact planning-algorithm differences (net-change vs regenerative vs order-by-order; finite vs infinite capacity) are product-specific realizations; the final document describes the pattern, not any product's algorithm parameters.
7. The exact boundary behavior when a job-shop ETO product creates BOMs per job (no standing catalog BOM) is inferred from MRPeasy's ETO/CTO demo-video positioning and BC's sales-order-driven order creation; held as a variant, not independently verified at Tier-1 for a dedicated ETO vendor.

## Final Synthesis

A Manufacturing ERP is the manufacturer's single integrated business system: the ERP spine (finance, purchasing, sales, inventory on one data core with automatic financial posting) carries a first-class manufacturing layer — the build definition (bill of materials + routing/work centers) held as governed master data, and the production order as the unit of manufacture, advancing through a planned→released→finished lifecycle that consumes materials, records operations and output, and reconciles costs into the ledger (WIP, variances). Around that core, mature products add MRP-class planning, shop-floor recording, production costing depth, subcontracting, lot/serial tracking, quality gates, and capacity views; variants span production modes (MTS/MTO/ETO), discrete vs process vocabulary, substrates (manufacturing-first suite vs general ERP area vs modular apps vs lightweight cloud MRP), tiers, and deployments. The Type's identity is precisely the *integration* of making (build definition → production order → costing) with commerce and finance in one system: remove the integration and the remaining pieces are a generic ERP, a planning tool, or an MES.
