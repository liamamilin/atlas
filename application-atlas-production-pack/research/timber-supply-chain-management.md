# Research Notes — Timber Supply Chain Management

## Research Goal

Understand what "Timber Supply Chain Management" software actually is from real products: what objects it holds, who uses it, how the flow of wood from forest to mill is planned, executed, recorded, and settled, and where its boundary lies against Logging Operations Management (job execution), Forestry Management (estate), and generic freight/supply-chain planning Types.

## Initial Boundary

- The leaf sits in DIRECTORY §20 (Agriculture, Food & Natural Resources) between Logging Operations Management and Mining Operations Management. "Timber supply chain" in industry usage means the forest-to-mill flow of wood fiber (harvest → roadside → truck → mill/yard → mill consumption), not the wider "forest products" manufacturing chain.
- Working hypothesis (from the forestry-management and logging-operations-management passes' forward flags): this Type is the **logs-to-mill / chain-wide fiber flow object world** — allocation of wood to destinations, wood-flow planning, transport scheduling/dispatch, delivery records, mill/yard inventory, procurement/sales across the chain — while Forestry Management holds the estate and Logging Operations Management holds the harvest job.
- Predicted overlap zone (logging pass): transportation scheduling + load/delivery records + mill/yard inventory; proposed seam = center of gravity (executing the harvest job vs optimizing/trading the chain-wide fiber flow). This pass must discharge that flag.
- Nearest neighbors to test: Logging Operations Management, Forestry Management, Transportation Management System (§10), Supply Chain Planning Platform (§10), Freight Brokerage / Load Board (§18), market-intelligence/timber-price platforms, grain origination (§20 analog), mill production systems.

## Research Questions

1. What is the unit of managed work — the wood flow? the delivery? the allocation decision?
2. What objects exist: wood-flow plan, allocation, roadside inventory, transport schedule, load/delivery record, mill/yard inventory, procurement/sales contracts?
3. Who uses it (fiber supply/mill managers, procurement/marketing managers, transport managers, dispatchers, haulers, mill receiving)?
4. How does allocation work (supply points → destinations, against what constraints)?
5. How does transport scheduling/dispatch work, and how deep does it go?
6. How do loads/deliveries flow and settle across parties (scale, contracts, chain of custody)?
7. What is the plan-vs-actual loop at chain level (mill intake vs supply pipeline)?
8. Where does this Type end vs Logging Operations Management / Forestry Management / generic TMS / generic SCP?

## Representative Products

Selected for market representability, documentation depth, different product philosophies and customer tiers:

1. **Remsoft** (Canada) — planning-led forestry intelligence platform whose own family splits into FMS (estate) / Planning-Optimization / Operations (job execution) / **Logistics** (forest-to-mill delivery) / MRO. This pass samples the **Logistics line (Remsoft LOGR)** plus the two supply-chain-side role pages (Fiber Supply/Mill Manager; Timber Marketing/Procurement Manager) and the Tactical Optimization (wood-flow planning) line. Customer tier: large forest owners, mills, supply-chain organizations (Green Triangle Forest Products testimonial).
2. **Trimble Forestry** — execution-led forestry family whose industry page splits the forestry supply chain into five links: Forest Management / **Wood Procurement** / Forest Operations / **Logistics** / Mill. This pass samples the supply-chain links: **Wood Supply Execution (WSX)** ("log supply plan execution and dispatch"), **LogForce** (wood transportation), **SilvaPRO** (wood procurement ERP). Nordic customer base (Metsä Group, Metsähallitus).
3. **ResourceWise (Forest2Market)** — boundary pole, not a flow-management sample: market intelligence (timber pricing, benchmarks, forecasts, EUDR compliance data). Used to confirm what this Type is *not*.

Rejected / unreachable candidates (recorded for honesty): 3Log Systems (3log.com — timeout + transport error this pass; ×2 in the logging pass), Woodflow NZ (transport error this pass; ×3 in the logging pass), Logister SE (transport error this pass; ×2 prior), ForestX SE (transport error this pass; ×2 prior), F4 Tech (×1 prior), Farma (farma.fi is an agricultural foundation, wrong domain), Lim Geomatics (domain redirects to Remsoft — acquired), Silvacom (consulting only).

## Sources

Tier 1/2 official vendor surfaces, fetched 2026-09-10:

- Remsoft — https://remsoft.com/solutions/logistics/ (Logistics solution page)
- Remsoft — https://remsoft.com/remsoft-logr/ (LOGR product page, incl. FAQ)
- Remsoft — https://remsoft.com/roles/fiber-supply-mill-manager/ (Fiber Supply & Mill Manager role page, incl. FAQ)
- Remsoft — https://remsoft.com/roles/timber-marketing-procurement/ (Timber Marketing & Procurement role page, incl. FAQ)
- Remsoft — https://remsoft.com/tactical-optimization/ (Tactical Optimization product page)
- Trimble — https://www.trimble.com/en/industries/forestry (forestry industry page: five-link supply-chain map + product descriptions)
- Trimble — https://www.trimble.com/en/products/forestry/wood-supply-execution (hero positioning only; body JS-gated)
- Trimble — https://www.trimble.com/en/products/forestry/logforce (hero positioning only; body JS-gated)
- ResourceWise — https://www.forest2market.com/ (redirect to ResourceWise; market-intelligence positioning)

No vendor help-center / user-guide tier was reachable for either flow-management vendor (Remsoft support portal gated; Trimble product pages JavaScript-rendered — only hero positioning text server-rendered). All claims below are calibrated to product/solution/role-page evidence.

## Product A — Remsoft (Logistics line + supply-chain roles + planning line)

### Key observations (Evidence layer A unless noted)

- **Logistics solution page** — headline: "Every load. All parties. One trusted record." Sub: "Digital records for forest owners, truckers, and mills. One connected, auditable source of truth, from loading site to mill gate."
  - "Forestry logistics is evolving beyond paper tickets. Remsoft Logistics digitizes delivery documentation from loading site to mill gate, giving forest owners, truck drivers, and mills one shared record they can all trust. Track every load in real time. Proven chain of custody for FSC, SFI, PEFC, and EUDR compliance. With digital transport certificates and smart weigh station integration, you always know what's on the road, where it's going, and whether it arrived correctly."
  - Before/after framing: "Execution visibility is delayed until summaries arrive / Truck schedules live in inaccurate spreadsheets / Paper tickets get lost, damaged, or disputed / Unpredictable scale congestion…" → "Real-time wood flow visibility across supply chain / Multiparty digital record for all transport activities / One digital record everyone can trust / See inbound flow, anticipate bottlenecks, adjust schedules / Automated scale data reduces throughput time / Digital traceability and auditable records of every load."
  - "A multi-party solution for a multi-party problem. From electronic transport certificates to smart weighbridge integration, Remsoft Logistics captures digital load data across the forest-to-mill supply chain, giving forest owners, contractors, and mills a shared, auditable record of every load."
  - Capabilities: **Digital Tickets** ("Species, grade, volume, origin, timestamps, and GPS coordinates, in one shared digital record that travels with the load"); **Multiparty Insights & Shared Ledger** ("Electronic transport certificates act as a secure, multiparty ledger with role-based access. Forest owners see what left their land. Contractors see what they delivered. Mills see what arrived."); **Truck Scale Enablement** ("Convert existing truck scales into connected digital assets. Automated weight capture, load verification, and data exchange between drivers, mills, and forest owners — without replacing your hardware"); **Chain of Custody** ("Auditable, end-to-end traceability from forest to mill. Every load is documented with origin, route, and delivery confirmation — supporting FSC, SFI, PEFC certification and EUDR compliance"); **Delivery Process Management** ("Manage the entire delivery workflow — dispatch, transit, weighbridge, and mill intake. Real-time visibility into delivery status, exceptions, and ETAs"); In-Field Alerting.
- **LOGR product page** — "Remsoft LOGR is Remsoft's digital delivery record for forestry logistics. It captures what was loaded, hauled, weighed, and delivered — and makes that information available to every authorized party in one consistent view." / "a single digital record that follows each load from loading site to mill gate."
  - "Forestry deliveries break down when information is lost between the forest and the mill. Loads move across long distances, multiple organizations, and changing conditions. Paper tickets get lost. Details are recorded in multiple places, and questions surface days or weeks later when it's hard to reconstruct what happened."
  - Helps teams: "Track deliveries from loading site to mill gate / Verify delivery details with a shared digital record / Reduce disputes between forest owners, contractors, and mills / Support chain of custody and compliance requirements / See what's moving and what has arrived, without chasing updates."
  - Roles: Forest Owners & Supply Chain Leaders ("visibility into what is leaving the forest, where it is going, and whether it arrived as expected"); Mills & Receiving Operations ("Understand what is arriving before trucks reach the gate. LOGR connects delivery records with receiving and weighbridge processes"); Contractors & Haulers ("digital delivery records that work offline and sync automatically… fewer disputes, faster reconciliation"); IT & Digital Leaders ("Integrate delivery records with existing mill systems and ERPs").
  - Capabilities: digital delivery records (species, grade, volume, origin, timestamps, confirmations); shared multiparty record (role-based access, "without conflicting versions of the truth"); delivery visibility (real-time, ETAs, exceptions); chain of custody documentation; discrepancy and claims support.
  - FAQ: "enforces rules to ensure loads are picked up from the correct location and delivered to the right customer"; "Is LOGR a planning or scheduling system? **No. LOGR focuses on delivery execution and verification.** It captures what actually happened during transport and delivery and complements planning and operations systems by providing trusted execution data."; "LOGR delivery records cannot be forged or tampered with, and all parties reference the same validated information"; integrates with mill intake systems, ERPs (Microsoft ERP, Pronto, SAP named), connected weighbridge infrastructure; offline-capable capture; works with or without scales; fleet devices, RFID, hybrid paper-to-digital capture.
- **Fiber Supply / Mill Manager role page** — headline: "Keep the mill fed. Keep the plan moving." Sub: "Live visibility across the full delivery chain so you know what's coming before intake falls short."
  - "Keeping the mill fed means knowing what is loaded, what is moving, and what is arriving — before intake falls short. Remsoft gives you live visibility across the full delivery chain, digital documentation that replaces paper tickets, and a shared record every party works from. When volumes shift or schedules change, you have time to adjust."
  - Stay Ahead of Problems: "Know what is loaded, what is rolling, and what is arriving. If a road washes out or volumes drop, you see it before intake falls short."
  - Hit Delivery Targets: "Track on-time, in-spec activities across contractors and routes."
  - Adapt Quickly: "When mill shutdowns, road bans, or weather hit, reroute loads and reset schedules from one connected view."
  - Smarter Truck Utilization: "Coordinate fleet scheduling across your network. Fewer empty runs, faster turnaround, and reduced reconciliation disputes."
  - Operations for this role: "Schedule transportation fleets, track deliveries against plan, and see what's moving across your network in real time. Know what's arriving at the mill, when it's arriving, and whether it matches what production needs." — dynamic scheduling for truck fleets and equipment across the supply chain; real-time tracking of loads from forest site to mill yard; delivery vs. plan visibility for every truck, load, and arrival; **supply pipeline forecasting for production planning**; adjustments for weather, road closures, and operational changes.
  - Planning & Optimization for this role: "**Forecast supply based on harvest plans. Model what's available, when, and in what quantities so production can plan with confidence instead of guessing.**"
  - FMS for this role: "Source inventory data from the field. Reliable species, grade, and volume data at the point of harvest ensures accurate records flow through logistics and mill operations."
  - FAQ: "With visibility into what's roadside, rolling, and scheduled to arrive, production teams can forecast mill intake with confidence. Instead of guessing at supply or running inefficient production schedules, mill managers know exactly what species, grades, and volumes are arriving on what timeline. This enables smarter production planning, reduces overstocking and understocking, and improves uptime and efficiency."
  - Chain-of-custody FAQ: "Chain of custody is the unbroken record of who had custody of a load and when. Digital chain of custody captures timestamps, GPS coordinates, and signatures at each handoff (loading site, truck, scale, mill)."
- **Timber Marketing / Procurement Manager role page** — headline: "Right product. Right buyer. Right price." Sub: "Match fibre supply to contracts and delivery commitments with visibility into what's available, what's moving, and what's at risk."
  - "Remsoft connects fibre supply and delivery execution so you can see what's available, what's committed, and what needs to move. Make allocation decisions fast enough to protect margin when something changes."
  - Live Supply Visibility: "See real-time harvest output and inventory levels so allocation decisions reflect what is actually on the ground."
  - Smarter Allocation: "Model supply scenarios and evaluate contract commitments before committing volume to buyers."
  - Track Every Delivery: "Digital records from forest to mill. Know exactly what was delivered against each contract, with certified chain of custody."
  - Pivot When Markets Shift: "React to price changes, weather disruptions, or mill closures with connected data instead of phone calls and guesswork."
  - Planning & Optimization: "Model timber yield scenarios against market demand before committing to the harvest schedule. Forecast supply volumes and evaluate allocation strategies across your contract portfolio so every decision balances supply, buyer requirements, and margin." — model harvest scenarios with forecasted product mix and volumes; evaluate allocation strategies against buyer specifications and contract terms; forecast timber supply and demand across product grades and regions; optimize harvest sequence to match market opportunity and product demand.
  - Transportation & Logistics: "Track every load from forest to mill with full visibility into what's been harvested, what's moving, and what's been delivered against contracts. Digital records prove chain of custody and certification compliance so you can access certified timber markets and meet buyer audit requirements." — real-time tracking of harvest output and load status through the supply chain; digital delivery documentation and proof of certification for every transaction; **automated contract compliance checking against product specs and delivery terms**; complete chain of custody records for certified timber and ESG reporting.
  - FMS: "Live inventory records from harvest sites through staging and mill delivery… Product grading, certification status, and quality attributes tracked by load."
  - FAQ: "**Fibre allocation optimization** uses real-time inventory data, buyer specifications, contract terms, and market pricing to recommend which loads should go to which buyers to maximize total revenue while respecting delivery commitments and product requirements. Remsoft models scenarios so you can see trade-offs before making allocation decisions."
  - FAQ: "Remsoft Logistics tracks every load against contract terms in real time. As wood moves from harvest site through staging to mill delivery, the system confirms product specs, quantity, certification status, and delivery dates match contract requirements, and flags any mismatches before they become delivery problems."
  - FAQ: "Every load is tagged with its certification (FSC, SFI, PEFC), and as it moves through the supply chain, the system maintains complete traceability so you can prove certified status to buyers and pass audits without manual documentation work."
- **Tactical Optimization page** (planning line) — "aligns harvest scheduling and wood allocation to improve wood flow, delivery and capacity planning"; "roadside inventory and transportation management"; "lowest possible delivered wood costs"; "wood flow profile and costs"; "Reduce working capital requirements through leaner inventory management across the supply chain"; "report on road maintenance costs and harvest volumes transported by road segment".
- **Operations line** (cross-referenced from the logging pass's evidence, same vendor): Allocation Planning ("Assign product volume from harvest units – at either the area or unit level – to destination points"); Transportation Scheduling ("Assign transportation fleets to road-side inventory to create delivery schedules from the unit to the mill"); Mill/Yard Inventory Planning (production inventory, purchases, disposals, transfers, usage at mill/yard level).
- Customer voice (Supply Chain Coordinator, Green Triangle Forest Products): "The ability to have real time, accurate and complete information on all deliveries has significantly changed the way we work, leading to improved decision making and better outcomes for our business, for our suppliers and for our contractors."

## Product B — Trimble Forestry (Wood Procurement + Logistics links)

### Key observations (Evidence layer A, Tier 2 positioning; product bodies JS-gated)

- **Industry page framing**: "From forest-to-mill, connecting you to every step. Trimble Forestry solutions optimize each link in the forestry supply chain. From harvesting, to transporting, to mill production, we offer a connected operation that's seamless, streamlined and sustainable every step of the way."
- Five-link split (the vendor's own supply-chain map):
  - **Forest Management** — "Managing and planning the forest" (Land Resource Manager).
  - **Wood Procurement** — "From forest to factory, optimized. From sourcing raw timber to valuing and contracting for manufacturing and processing into usable goods, Trimble Wood Procurement products cover the biggest business challenges." Products: **SilvaPRO** ("SaaS ERP for forest planning, site monitoring and wood procurement, with a modern UI and map view for efficient operations"); **Log Inventory & Management System** ("Integrated software systems that connect your forestry operation").
  - **Forest Operations** — "Harvesting and field operations" (CF Harvest; sampled by the logging pass).
  - **Logistics** — "Wood transportation management." Products: **Wood Supply Execution (WSX)** ("A dedicated log supply plan execution and dispatch system for managing the execution of weekly log supply plans"); **LogForce** ("Ensures that the requested wood is transported to the right destinations based on real-time information"); **CFXchange** ("A cloud solution that boosts real-time visibility and security by sharing key metrics between office and field").
  - **Mill** — "Optimizing industrial flows" (Stratus).
- **WSX product hero**: "Trimble WSX: Collaborative platform for wood supply exchange" / "More efficient wood transport. The forestry operating environment is typified by remote sites, rugged conditions and a production process that can be highly uncertain. Trimble Wood Supply Execution helps solve those problems."
- **LogForce product hero**: "Better woodflow with logistics. LogForce makes updating the plans easy since the information is delivered digitally to trucks — no more staying on the phone all day!"
- From the same industry page (recorded in the logging pass's evidence): "Trimble Logistics Management help customers navigate the complex logistics of transporting harvest timber from the forest to processing facilities. Optimizing routes, tracking loads and managing the movement of resources."
- Customer logos on the family: Metsä Group, Metsähallitus (Finnish market).

## Product C — ResourceWise (Forest2Market) — boundary pole

### Key observations (Evidence layer A)

- "Forest2Market is now part of ResourceWise." Positioning: market intelligence — commodity pricing, forecasts, benchmarks, trade data and flows, plants/projects/supply-demand, EUDR compliance (Forest Trackt), news/insights.
- **SilvaStat360**: "a one-stop portal where you can conveniently access essential datasets and analytical tools vital for success in the forest supply chain. It provides instant conversions to units, grade scales, and currencies… along with regional datasets for international indexing and benchmarking."
- Reading: this is data *about* the forest supply chain (prices, benchmarks, trade flows) — not machinery that plans, executes, or records a company's wood flow. Confirms the boundary between supply-chain *intelligence* and supply-chain *management*.

## Cross-product Comparison

| Dimension | Remsoft (Logistics/LOGR + roles + Tactical) | Trimble (WSX + LogForce + SilvaPRO) | Reading |
|---|---|---|---|
| Center of gravity | the forest-to-mill flow: allocation, transport, delivery records, pipeline | "each link in the forestry supply chain": procurement → logistics → mill | B: the chain-wide fiber flow is the shared center |
| Unit of planning | allocation of harvest-unit volumes to destinations; supply forecast from harvest plans; contract-portfolio allocation | "weekly log supply plans" executed and dispatched | B: the wood-flow plan (supply → destinations over time) is the shared planning object |
| Unit of execution record | the load: species/grade/volume/origin/timestamps/GPS, one shared multiparty record, scale-verified | loads tracked from forest to processing facilities; "requested wood… transported to the right destinations" | B: the load/delivery record is the shared transactional unit |
| Transport scheduling/dispatch | transportation scheduling (fleet → roadside inventory → delivery schedules); dynamic rescheduling; digital updates to trucks | WSX = "execution and dispatch"; LogForce = transport to right destinations on real-time info | B: dispatch present in both; depth varies (Remsoft splits scheduling into Operations line, execution records into Logistics line) |
| Chain inventory | "what's roadside, rolling, and scheduled to arrive"; supply pipeline forecasting; mill/yard inventory planning (purchases/disposals/transfers/usage) | roadside/terminal inventory minimization (CF Harvest, ops line); mill link "optimizing industrial flows" | B: the chain inventory picture (roadside → rolling → yard/mill) is shared |
| Commercial layer | contract commitments, buyer specs, automated contract compliance checking, "delivered against each contract" | Wood Procurement: "sourcing raw timber to valuing and contracting"; SilvaPRO wood-procurement ERP | B: procurement/sales contracts checked against deliveries is shared |
| Multiparty structure | forest owner / hauler / mill on one record, role-based | office ↔ field sharing (CFXchange); haulers digital dispatch (LogForce) | B: multiparty chain is the shared operating reality |
| Chain of custody | FSC/SFI/PEFC/EUDR riding the load record; custody handoffs (loading site, truck, scale, mill) | not detailed on reachable pages | A (Remsoft) / unverified (Trimble) — held as common, depth varies |
| Optimization modeling | Tactical Optimization (harvest + roads + wood flow; delivered wood cost) | not on reachable pages | single-vendor depth → common capability, not defining |
| Scale/weighbridge | smart weighbridge integration, automated weight capture | not detailed on reachable pages | A (Remsoft) — held as common mechanism |
| Offline field reality | offline capture, sync, fleet devices, RFID, hybrid paper-digital | "remote sites, rugged conditions… highly uncertain" | B: disconnection tolerance shapes both |
| Estate record | separate FMS line | separate Land Resource Manager | B: estate lives in a sibling Type |
| Harvest job execution | separate Operations line | separate CF Harvest | B: job execution lives in a sibling Type |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The wood-flow allocation plan.** The chain's plan of record: fiber supply (harvest output by species/product, purchased wood) matched to demand (mill intake needs, buyer contracts) by assigning wood volumes to destinations over time. This is the "which wood goes to which mill, when" decision machinery. Remove it → harvest scheduling (estate/operations territory) or a bare trucking dispatch tool; the supply-demand matching across the chain is gone.
2. **The load/delivery record as the chain's shared transactional artifact.** Each load captured once — species, grade, volume or weight, origin, destination, timestamps — traveling with the load, verified at the scale, visible to all parties under role-based access, and checked against contract terms. It is the unit through which the flow executes and settles. Remove it → a plan with no execution record, or telematics/tickets with no chain transaction semantics.
3. **The chain inventory picture.** Wood held as flowing stock at the chain's nodes — roadside/landing inventory, in-transit (rolling), yard and mill inventory — continuously updated from load capture and scale data, feeding supply-pipeline forecasts and mill-intake planning. Remove it → dispatch and delivery records with no stock position; the "keep the mill fed" balancing act is gone.

Jointly load-bearing:
- 1 alone = an allocation spreadsheet / S&OP exercise
- 2 alone = load slips / e-dockets (the logging-ops production record, or a haulage ticketing app)
- 3 alone = inventory counters
- 1+2 without 3 = allocation + delivery records with no stock position (nothing to balance, no pipeline to forecast)
- 1+3 without 2 = planned flow over stock positions nobody executes
- 2+3 without 1 = loads moving with no allocation logic (pure dispatch + ticketing)

### L1 — Common Mature Structure

- transport scheduling and dispatch (fleet assignment against roadside inventory; delivery schedules from unit to mill; digital dispatch and plan updates to trucks)
- weighbridge/scale integration (automated weight capture, load verification, scale-throughput improvement)
- delivery-vs-plan visibility and supply-pipeline forecasting for production planning
- contract compliance checking (product specs, quantity, certification status, delivery dates vs contract terms; mismatch flagging)
- chain-of-custody / certification traceability riding the load record (FSC/SFI/PEFC-class schemes; regulatory regimes such as EUDR named at one vendor)
- multiparty role-based visibility (forest owner / hauler / mill each see their slice of the same record)
- disruption response (reroute loads, reset schedules on weather, road bans, mill shutdowns)
- truck utilization / fleet coordination (fewer empty runs, faster turnaround)
- offline field capture with sync; fleet devices, RFID, hybrid paper-digital capture
- mill/yard inventory planning (production inventory, purchases, disposals, transfers, usage)
- wood-flow optimization modeling (harvest + roads + wood flow; delivered wood cost) at the planning pole
- integration with ERPs / log-accounting systems / mill intake systems

### L2 — Variant / Optional Structure

- who leads the deployment: forest-owner/manager organization vs mill/procurement organization vs integrated forest-products company running the whole chain
- planning depth: optimization-modeled allocation vs manual allocation against spreadsheets
- commercial depth: contract portfolio management, pricing/market-data integration (market-intelligence platforms are a separate pole)
- regional haulage regimes: transport certificates, certified weighbridge processes, jurisdiction-specific documentation
- packaging: standalone logistics product vs suite line (alongside estate/operations/mill products) vs procurement-ERP module
- harvest-method context (cut-to-length vs tree-length) shaping where loads are built and what the production feed looks like
- trading/exchange surfaces (log trading marketplaces) — adjacent, not this Type

### L3 — Vendor-specific (kept out of the final document)

- Remsoft: LOGR/ScalePass/eDockets product names, Op Tracker, "electronic transport certificates" phrasing, "4 minutes per load" and Alberta-certification claims (recorded in the logging pass), Green Triangle testimonial, Woodstock/Tactical Optimization branding, client-driver statistics (58%/52%/35%/32%)
- Trimble: WSX/LogForce/CFXchange/SilvaPRO/Stratus product names, "weekly log supply plans" phrasing, five-link supply-chain map wording, Finnish customer logos, "1,000 contractors / 5,000 users" marketing counts (logging pass)

### Anti-overfitting checks

- **Digital transport certificates / e-dockets are not definitional** — the vendors' own framing is "evolving beyond paper tickets"; the paper ticket + scale ticket + phone dispatch era satisfies the same invariants.
- **Weighbridge integration is not definitional** — one vendor explicitly supports operations "with or without scales" (chain-of-custody and delivery verification still function).
- **Optimization modeling is not definitional** — evidenced at one vendor's planning line; manual allocation satisfies the invariant.
- **Chain-of-custody certification is not definitional** — it rides the load record as a capability; the record's origin/destination/timestamp structure stands without certification schemes.
- **GPS/telematics not definitional** — the load record's origin/timestamp binding is the invariant; GPS is the modern capture mechanism.
- **Cloud/SaaS not definitional** — deployment shape varies; nothing in the core requires it.

### Historical / market-sample check (§24)

Paper-era wood flow (conceptual check): a mill's or wood-room's allocation board matching incoming harvest supply to mill consumption needs; a dispatch desk assigning trucks by phone/radio against roadside piles; handwritten delivery tickets and scale tickets traveling with each load; a wood-yard ledger tracking roadside/yard/mill stock; contract books reconciling delivered volumes against purchase/sale terms. All three L0 structures present with zero software-era machinery. Nordic, North American, and Southern-plantation traditions all satisfy — the definition names no dispatch medium, no ticket format, no certification scheme, no deployment shape.

## Boundary Findings

- **vs Logging Operations Management** — DISCHARGES the logging pass's forward flag from this side; keep-both RATIFIED on the center-of-gravity seam exactly as that pass proposed. Logging Ops holds the harvest job (operation + crews/machines + attributed production + contractor settlement); this Type holds the chain-wide flow (allocation to destinations, transport scheduling/dispatch, delivery records as chain transactions, chain inventory, contract fulfillment). The predicted overlap zone (transportation scheduling, load/delivery records, mill/yard inventory) is real and resolved at center of gravity: in Logging Ops the load is the *production/settlement artifact of the job*; in this Type the load is the *chain's transaction* — allocated to a destination, dispatched, delivered against a contract, and balanced against a pipeline. Vendor product-line splits confirm the seam from both families (Remsoft: Operations vs Logistics; Trimble: CF Harvest vs WSX/LogForce). The hand-off is bidirectional: operations produce the loads that enter the flow; the flow's delivery records feed back into production and settlement. Remsoft's own FAQ draws the execution-side line: LOGR "is not a planning or scheduling system… complements planning and operations systems by providing trusted execution data."
- **vs Forestry Management** — estate record (units, standing inventory, multi-year program) vs flow. The flow plan consumes harvest plans and inventory forecasts from the estate ("Forecast supply based on harvest plans"); executed volumes write back. Vendor splits confirm (Remsoft FMS vs Logistics; Trimble Land Resource Manager vs WSX/LogForce).
- **vs Transportation Management System (§10)** — generic freight TMS manages shipments, carriers, rates for any freight; this Type's objects are wood-specific (species/grade/product volumes, roadside inventory, harvest-unit supply, mill consumption, scale tickets, chain of custody) and its plan is coupled to harvest plans. A generic TMS could haul logs as freight but holds no wood-flow allocation or chain inventory picture. Assertion calibrated: TMS not researched this pass; boundary drawn from the object-world contrast.
- **vs Supply Chain Planning Platform (§10)** — generic SCP plans demand/supply/inventory for manufacturing/retail; this Type is the wood-domain realization with harvest-coupled supply, transport-constrained flow, and scale-ticket settlement. Adjacent; calibrated assertion, not deeply researched.
- **vs Market intelligence / timber price platforms** (ResourceWise/Forest2Market pole) — CONFIRMED from this side: pricing datasets, benchmarks, forecasts, trade flows *about* the chain vs machinery that plans/executes/records a company's own flow. ResourceWise's own positioning (market intelligence, "datasets and analytical tools") shows the seam.
- **vs Chain-of-custody / compliance platforms** — chain of custody rides the load record here as a capability; dedicated traceability/compliance products exist as a separate category (ResourceWise sells EUDR compliance as its own solution). Boundary held.
- **vs Grain Origination Platform (§20, processed)** — parallel commodity-flow pattern in agriculture (grower contracts → elevator/end-user flow → settlement). Different object world: no harvest-plan coupling, no roadside inventory, no chain-of-custody certification riding loads; grain grades vs wood species/product mix. Noted as parallel, not merged.
- **vs Mill production systems** (Trimble "Mill — Optimizing industrial flows", Stratus) — the mill's internal production execution is downstream of mill intake; this Type ends at the mill gate/intake. Not researched; boundary noted from the vendor's own link split.
- **vs Freight Brokerage / Load Board (§18)** — matching loads to carriers vs managing the chain flow; adjacent, not researched.

## Uncertainties

- **Sample breadth**: the flow-management evidence rests on two vendors (Remsoft deep across product lines and role pages; Trimble at positioning tier) plus one boundary pole. Multiple specialist candidates (3Log scaling/settlement, Woodflow wood-flow optimization, Logister log haulage, ForestX, F4 Tech) were unreachable this pass and in the logging pass. Cross-product commonality (layer B) is real but narrow; a third independent vendor could shift L1/L2 assignments.
- **Procurement/settlement depth**: contract compliance checking and delivery-against-contract visibility are directly evidenced; in-product pay computation, pricing engines, and invoicing are not verified in public docs. Held as contract-fulfillment visibility, not in-product invoicing machinery.
- **Trimble feature depth**: product pages are JavaScript-rendered; only hero positioning and the industry-page descriptions were reachable. WSX/LogForce capability lists are unverified.
- **Mill-side depth**: the mill link ("optimizing industrial flows") was not researched; the exact seam at mill intake vs mill production is asserted from the vendor's link split only.
- **Wood-flow optimization depth**: optimization modeling is evidenced at one vendor (Remsoft Woodstock/Tactical); held as L1/variant, not definitional.
- **Numeric claims** (client-driver percentages, "4 minutes per load", contractor counts) are vendor marketing; recorded here, excluded from the final document.

## Final Synthesis

Timber Supply Chain Management is the wood-flow management application for the forest-to-mill chain. Its world is organized around the flow of fiber: a wood-flow plan that allocates supply (harvest output, purchased wood) to demand (mill intake, buyer contracts) over time; loads/deliveries as the chain's shared transactional records — captured once with wood attributes, origin, and destination, verified at the scale, visible to all parties, and checked against contract terms; and the chain inventory picture (roadside → rolling → yard → mill) that keeps the mill fed. Around this core, mature products add transport scheduling and dispatch, weighbridge integration, chain-of-custody traceability, disruption response, fleet-utilization coordination, and integration with ERPs and mill systems. The Type ends where the harvest job begins (Logging Operations Management), where the estate record begins (Forestry Management), where generic freight or generic planning begins (TMS / Supply Chain Planning), and where market data about the chain begins (timber market intelligence).
