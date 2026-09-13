# Research Notes — Logging Operations Management

## Research Goal

Understand what "Logging Operations Management" software actually is from real products: what objects it holds, who uses it, how the work of timber harvesting is planned, executed, recorded, and settled, and where its boundary lies against Forestry Management (estate side) and Timber Supply Chain Management (logs-to-mill side).

## Initial Boundary

- The leaf sits in DIRECTORY §20 (Agriculture, Food & Natural Resources) between Forestry Management and Timber Supply Chain Management. "Logging" here means timber harvesting, not IT logs (§14 Log Management) and not construction daily logs (§17 Daily Log Application) — name collisions only.
- Working hypothesis (from the forestry-management pass's forward flag): this Type is the **job-execution object world** — crews, machines, production, loads — while Forestry Management holds the estate + inventory + multi-year program, and Timber Supply Chain Management holds the logs-to-mill flow.
- Nearest neighbors to test: Forestry Management, Timber Supply Chain Management, Fleet Management System, CMMS, Field Service Management, Crop Management, Mining Operations Management.

## Research Questions

1. What is the unit of managed work? (harvest block? contract? work order?)
2. How are crews and machines assigned and tracked?
3. What counts as "production" and how is it captured (load slips? machine files? area depletion)?
4. How does hauling/dispatch relate to the operation?
5. How does production turn into payment (contractor settlement, procurement accounting)?
6. What is the plan-vs-actual loop and who consumes it?
7. What roles exist on the owner side vs contractor side, and how do the two views differ?
8. Where does this Type end and Forestry Management / Timber Supply Chain Management begin?

## Representative Products

Selected for market representability, documentation depth, different product philosophies and customer tiers:

1. **Remsoft** (Canada) — planning-led forest intelligence platform; the Operations product line (Remsoft Operations) plus execution components (Op Tracker machine telematics, ScalePass digital load slips, LOGR delivery records, MRO maintenance). Customer tier: large forest owners, mills, supply-chain organizations; explicit contractor-facing role.
2. **Trimble Forestry** (Trimble CF Harvest, formerly WoodForce) — execution-led harvesting management system aimed at contractors and mixed fleets, web + mobile, Nordic customer base (Metsä Group, Metsähallitus); the Trimble forestry family also spans Land Resource Manager (estate), SilvaPRO / Log Inventory & Management System (procurement), Wood Supply Execution (dispatch), LogForce (transport).

Rejected / unreachable candidates (recorded for honesty, not used as evidence): 3Log Systems (3log.com — transport errors ×2), Woodflow NZ (woodflow.co.nz / .com / .nz — failures ×3), Logister SE (×2), ForestX SE (×2), F4 Tech (×1), Silvacom (reachable but now a consulting firm, no software product line), Lim Geomatics (domain now redirects to Remsoft — acquired, no longer independent), ForestPro (domain unreachable).

## Sources

Tier 1/2 official vendor surfaces, fetched 2026-09-09:

- Remsoft — https://remsoft.com/solutions/operations/ (Operations solution page)
- Remsoft — https://www.remsoft.com/remsoft-operations/ (product page)
- Remsoft — https://remsoft.com/scalepass/ (digital load slip product page, incl. FAQ)
- Remsoft — https://remsoft.com/op-tracker/ (machine telematics product page, incl. FAQ + plan tiers)
- Remsoft — https://remsoft.com/roles/forestry-contractor/ (contractor role page, incl. FAQ)
- Remsoft — https://www.remsoft.com/ (platform overview: FMS / Planning / Operations / Logistics / MRO lines)
- Trimble — https://www.trimble.com/en/industries/forestry (forestry industry page: product family map)
- Trimble — https://www.trimble.com/en/products/forestry/cfharvest (CF Harvest product page, incl. testimonials)

No vendor help-center / user-guide tier was reachable for either vendor (Remsoft support portal is gated; Trimble product pages are marketing-tier). All claims below are calibrated to product/solution-page evidence.

## Product A — Remsoft (Operations line)

### Key observations (Evidence layer A unless noted)

- Vendor self-describes four solution lines: FMS (land & asset management), Planning/Optimization, **Operations** ("Connect plans with day-to-day execution. Schedule crews and equipment, track plan vs. actual in real time, monitor machine and workforce productivity, and adjust when field conditions change"), Transportation & Logistics, MRO. The vendor's own split confirms the estate-vs-execution seam.
- Remsoft Operations capabilities (product + solution pages):
  - **Annual Planning** — harvest operations planned at monthly/quarterly/seasonal level "to lay the groundwork for crew scheduling".
  - **Crew Scheduling** — "Assign crews to harvest units with intuitive drag-and-drop features. See the impact on activity schedules and key metrics immediately."
  - **Allocation Planning** — "Assign product volume from harvest units – at either the area or unit level – to destination points."
  - **Transportation Scheduling** — "Assign transportation fleets to road-side inventory to create delivery schedules from the unit to the mill."
  - **Mill/Yard Inventory Planning** — track production inventory, purchases, disposals, transfers, usage at mill/yard level.
  - **Live Plan vs. Actual** — "Continuously compare real-world performance against the plan and catch deviations early — not at the weekly review."
  - **Real-Time Telematics** — equipment use, movement, conditions; "Know where your machines are and how they're performing without phone calls."
  - **Over Air Actuals** — "Capture harvester head data files in StanForD automatically. Transform raw machine data into actionable information, no manual entry."
  - **Machine Utilisation Monitoring** — productive machine hours (PMH), utilization rates, productivity (m³/hr) by machine or fleet.
  - **Predictive Maintenance Signals** — early indicators of mechanical issues from real-time equipment data.
  - FAQ: "It integrates with harvesting equipment, telematics systems, and mill weigh scales to automatically capture production, location, and delivered volume data via Wi-Fi or satellite."
  - Users: "Operations managers, supply chain leaders, planners, supervisors, IT teams, and executives in forestry organizations."
- **Op Tracker** (machine telematics product):
  - GPS tracking of machines; in-cab alerting: "alerting machine operators before they go somewhere they shouldn't" (block boundary + ecological feature alerts, avoid trespassing, "complete ribbonless harvests"); "Auto start tracking when block entered to avoid data gaps."
  - PMH, utilization (per machine and fleet-wide), productivity.
  - **Activity codes, stop codes and KPIs** — "Prompt operators for activity codes so you always know what's going on in the field. Show KPIs to operator for performance management."
  - Offline/disconnected mode with sync; imagery/LiDAR backdrops; ArcGIS integration.
  - **Automated depletion geometries** — harvest progress mapped back as geometry (the block record is updated by the work).
  - GeoNotes — field features (log piles, washed-out roads, no-go zones) pinned and shared.
  - Machine- and manufacturer-agnostic ("perfect for mixed fleets"); used in both tree-length (TL) and cut-to-length (CTL) operations (FAQ).
  - Contractor access to web app with "Restricted Contractor Views"; benchmarking database (higher tier); integration with Log365 (harvester/processor file transfer).
  - Plan tiers: TAB (BYOD tablet) / BOX / BOX+ (telematics device, satellite) — deployment shape is a packaging variable.
- **ScalePass** (digital load slip product):
  - "the loader operator creates a digital load slip on-site and sends it to both the trucker's tablet and the office via Wi-Fi and satellite. When the truck arrives at the scales, an app installed in the tablet automatically sends the load slip data to the shed's computer for almost instantaneous weigh-ins."
  - "Maintain Chain of Custody — Send each load slip at time of creation to the office via satellite, link load slip to your FMS for traceability and never lose a load slip."
  - Works at mill gate or satellite yards; "understand your flow of volumes from forest to mill or yard to yard"; loads inbound "from the bush/woods or satellite yards".
  - Vendor claims (marketing, layer A but promotional): average 4 minutes saved per weigh-in; certified for use by the Government of Alberta; certified with WeighWiz scales.
- **Contractor role page** (contractor-side framing):
  - Headline: "Know where to go. Track your loads. Get paid on time."
  - "See your assigned blocks, boundaries, and GPS confirmations on a mobile device."
  - "Shared digital records of loads including species, grade, volume, and timestamps. Reduced scale delays and reconciliation disputes." / "Transparent delivery history for payment disputes."
  - LOGR FAQ: "your crew captures load information digitally on a tablet or mobile device at the load point. Species, grade, volume, weight, GPS location, and timestamp are all recorded automatically. The record is instantly available to the forest owner, the mill, and you… Payment disputes resolve faster because everyone sees the same data."
  - Operations FAQ: "Forestry software systems help harvest crews and independent operators manage field work, track loads, and capture data without relying on paper tickets or spreadsheets. It simplifies job assignments, confirms work location, records what was cut and delivered, and keeps records accessible for payment disputes."
  - "Visibility from contract to execution" — crew activities come from forest planning (FMS); load records feed logistics networks.
  - Maintenance tracking for contractors (MRO): "catches issues before they pull a machine out of service."
- Customer story title (Forico): "schedule harvest crews, view our production volumes and develop customer wood flows with one software application."

## Product B — Trimble Forestry (CF Harvest)

### Key observations (Evidence layer A unless noted)

- Trimble forestry industry page organizes the family by supply-chain link: Forest Management (Land Resource Manager) / Procurement (SilvaPRO "SaaS ERP for forest planning, site monitoring and wood procurement"; Log Inventory & Management System) / **Forest Operations (CF Harvest: "Harvesting and field operations")** / Logistics (Wood Supply Execution "a dedicated log supply plan execution and dispatch system for managing the execution of weekly log supply plans"; LogForce transport management) / Mill (Stratus). Same vendor-side split: estate vs procurement vs operations vs logistics.
- CF Harvest product page:
  - "Harvesting management system… web-based software service with the flexibility to suit diverse business processes within the forest industry worldwide."
  - "Manage mixed fleet harvest operations in one system… enable real-time mixed fleet management for maximum efficiency of dynamic logging operations."
  - "Scheduling on the go: Handy web-based and mobile apps, for day-to-day scheduling and control for harvesting execution and forestry services."
  - "Monitor the route: Know the productivity of your fleet through visibility of the harvester's route."
  - "Minimize wasted product: Reduce both roadside and terminal log inventory."
  - Value props: "Reliable product information — knowing how much wood has been cut and where it went — in real time"; "Origins known — traceability to wood origin"; "Alerts keep you safe — map symbol based alerts."
  - Testimonials (contractor voice): "CFHarvest is easy to use… You can use CFHarvest with a smartphone, so expensive equipment purchases are not required. Also, work planning is very fluent"; "gives user-friendly tools for contractors to manage work orders."
  - Vendor marketing counts: "Almost a 1,000 contractors", "Over 5,000 users" (promotional, not independently verified).
  - Customer logos: Metsä Group, Metsähallitus, Kuljetusliike Veljekset Moilanen (Finnish market).

## Cross-product Comparison

| Dimension | Remsoft Operations line | Trimble CF Harvest | Reading |
|---|---|---|---|
| Unit of managed work | harvest units/blocks; crews assigned to units; annual→daily schedule | work orders; day-to-day scheduling of harvesting execution | B: the harvest operation (block/unit under a work order) is the shared anchor |
| Resource model | crews + machines + transportation fleets; drag-and-drop assignment | mixed fleets (machine-agnostic); contractor crews | B: crews/machines assigned to operations; mixed-fleet support common |
| Production capture | StanForD harvester files auto-captured; mill weigh scales; digital load slips (ScalePass); automated depletion geometries | "how much wood has been cut and where it went — in real time"; traceability to origin | B: production = loads (species/grade/volume/weight/origin/time) + machine data + depleted area, bound to the operation |
| Haul/dispatch | transportation scheduling (fleet→roadside inventory→mill); LOGR multiparty delivery records | roadside/terminal log inventory minimization; (dispatch sits in sibling product Wood Supply Execution) | B: hauling coordination present; depth varies; load record is the shared unit |
| Plan vs actual | "Live Plan vs. Actual… catch deviations early"; replanning | real-time visibility of output and routes; lighter planning emphasis | B: comparison loop common; emphasis differs by product philosophy |
| Settlement | contractor page: payment reconciliation, dispute-free records; load record "instantly available to the forest owner, the mill, and you" | contractor testimonials about work orders; payment not detailed on public page | A for Remsoft framing; settlement depth unverified in public docs for both |
| Field conditions | offline mode, satellite comms, proximity alerts | smartphone-class devices sufficient (testimonial); map-based safety alerts | B: remote/offline reality shapes the products |
| Multiparty visibility | owner / contractor / mill see the same load record | contractors + forest owner + supply chain steps | B: the load record is a shared, multiparty settlement artifact |
| Maintenance | MRO line + predictive maintenance signals | not on public page | single-product depth → common capability, not defining |
| Estate/inventory | separate FMS line | separate Land Resource Manager product | B: estate record lives in a sibling Type, not here |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The harvest operation as the unit of managed work.** A defined harvest unit/block/tract, taken on under a contract or work order, carrying its plan (products, schedule, assigned crew/machines) and accumulating the operation's record. Remove it → telematics and load slips with nothing organized; not management.
2. **Attributed field production records.** What was actually cut and moved, captured at the point of work and bound to the operation and its resources: loads (species/grade/volume/weight/origin/timestamp), machine production data, depleted area. Remove it → a schedule with no record of what happened; a planning tool, not operations management.
3. **The settlement loop.** Production records reconcile into pay/billing under contract terms — executed in the product or handed to accounting as settlement-ready, dispute-resistant records. Remove it → monitoring/telematics; the work→pay consequence that makes it "management" collapses.

Jointly load-bearing:
- 1 alone = a schedule board / job tracker
- 2 alone = telematics / load-slip capture with no operation to organize it
- 3 alone = accounting with nothing to settle
- 1+2 without 3 = execution monitoring (plan-vs-actual only)
- 2+3 without 1 = free-floating tickets (the paper-ticket era's failure mode)
- 1+3 without 2 = planned and paid with no record of what happened

### L1 — Common Mature Structure

- plan-vs-actual comparison with early deviation warning and replanning
- map-centric operations view (blocks, boundaries, roads) with proximity/safety alerts
- machine telematics: GPS location, PMH/utilization/productivity, activity & stop codes, fuel
- harvester data capture (StanForD-class machine files) as one production channel
- digital load slips / delivery records with weighbridge integration
- transportation scheduling and dispatch (fleet to roadside inventory, delivery schedules)
- offline field capture with sync (satellite/cellular options)
- contractor-facing views/portals with restricted scope; multiparty record sharing (owner/contractor/mill)
- maintenance & parts management for machines
- reporting/analytics: production by block/crew/product, dashboards, benchmarking

### L2 — Variant / Optional Structure

- deployment: cloud SaaS vs on-prem; BYOD tablet vs purpose-built telematics hardware
- origin: independent platform vs equipment-maker suite (machine-side production systems)
- harvest method context: cut-to-length vs tree-length vs full-tree; mechanized vs manual crews
- procurement-side extension: wood procurement, contracts, landowner/stumpage accounting (sibling products in both sampled families)
- mill/yard inventory planning (sort yards, terminals)
- certification/chain-of-custody and environmental compliance reporting; ecological feature alerts
- optimization/AI overlays (crew scheduling optimization, predictive maintenance, benchmarking databases)
- regional regulatory certification of load-slip/weigh-in processes (e.g., one vendor's Alberta certification claim)

### L3 — Vendor-specific (kept out of the final document)

- Remsoft: Op Tracker TAB/BOX/BOX+ tiers, FPDat II device, GeoNotes, automated depletion geometries, ScalePass/LOGR/Prism/Log365 product names, ArcGIS foundation, "4 minutes per load" and Alberta-certification claims, Forico testimonial
- Trimble: CF Harvest (formerly WoodForce) name, SilvaPRO/LIMS/Wood Supply Execution/LogForce/Stratus family names, "1,000 contractors / 5,000 users" marketing counts, Finnish customer logos

### Anti-overfitting checks

- **StanForD is not definitional** — it is one realization of production capture; paper load tickets and manual entry satisfy the same invariant (Remsoft's own FAQ frames StanForD capture as removing "manual entry", implying the manual baseline).
- **GPS/telematics not definitional** — the contractor FAQ explicitly frames the value as replacing "paper tickets or spreadsheets"; the paper-ticket era satisfies L0.
- **Cloud/GIS not definitional** — CF Harvest is web-based, but the defining structures do not require either.
- **Map-centricity not definitional** — extremely common, but the operation/production/settlement structures stand without a map engine.
- **Hauling coordination is not definitional** — one sampled family places dispatch in a sibling product; the load *record* (production leaving the site) is the shared unit, not the dispatch engine.

### Historical / market-sample check (§24)

Paper-era logging contractor (conceptual check): a tract/contract book (the operation), crew and machine assignment, handwritten load tickets per truck (species, destination, scale weight), settlement against mill scale tickets, equipment logbooks. All three L0 structures present with zero software-era machinery. Nordic cut-to-length, North American tree-length, and manual operations all satisfy — the definition names no harvest method, no machine brand, no protocol, no deployment shape.

## Boundary Findings

- **vs Forestry Management** — CONFIRMED from this side (discharges the forestry pass's forward flag 3): the sampled vendors themselves split product lines exactly as predicted. Remsoft: FMS (estate) vs Operations (execution). Trimble: Land Resource Manager (estate) vs CF Harvest (execution). Remove the estate record, standing inventory, and multi-year program → job execution remains = this Type. Remove the job execution → the estate record remains = Forestry Management. The hand-off seam: operations consume blocks/units and plans from the estate record and write depletion/progress back.
- **vs Timber Supply Chain Management** (unprocessed sibling) — this Type holds the operation and its production records; the supply-chain Type holds the logs-to-mill flow (allocation to destinations, wood flow optimization, trading, procurement across the chain). Overlap zone: transportation scheduling, load/delivery records, mill/yard inventory. Seam = center of gravity: executing the harvest job vs moving and trading fiber across the chain. Flag for that pass.
- **vs Fleet Management System / CMMS** — machine maintenance appears here as a capability (MRO, predictive maintenance), not the center; the center is the harvest operation and its production. Remove production/settlement → fleet maintenance territory.
- **vs Field Service Management** — both dispatch field resources, but the object world differs: service work orders vs harvest production with settlement semantics; no production/settlement loop in FSM.
- **vs Crop Management / Farm Management** — annual crop cycles vs multi-year timber stands; harvest of crops vs harvest of standing timber under contracts; different object worlds (field/season vs block/operation).
- **vs Mining Operations Management** (§20 sibling, unprocessed) — parallel pattern (operations, production, equipment, haulage) on a different material and regulatory world; noted, not researched.
- **vs Log Management (IT, §14) / Daily Log Application (§17)** — name collisions only; no structural relationship.

## Uncertainties

- **Settlement depth**: no sampled product's public documentation details contractor-pay computation (rates, deductions, payables). The settlement loop is held as L0 on the strength of the contractor-facing framing ("get paid on time", "payment reconciliation", "payment disputes") and the historical load-ticket record, but its in-product depth is unverified; some deployments likely hand settlement to accounting systems. The final document states this as the settlement loop with an integration caveat, not as in-product payroll machinery.
- **Contractor-side standalone products** (US "jobber" software class) could not be reached; the contractor evidence comes from the two sampled vendors' contractor-facing roles/pages. The sample therefore skews toward enterprise platforms; a dedicated small-contractor product might emphasize ticketing/settlement even more strongly.
- **Regional variants** (Nordic CTL, North American tree-length, Brazilian plantation) are only partially evidenced (Op Tracker FAQ names TL and CTL); regional differences are kept as variants, not asserted in detail.
- **Numeric claims** (4 minutes per load, 1,000 contractors, 5,000 users) are vendor marketing; recorded here, excluded from the final document.
- **Woodflow / Logister / ForestX / 3Log** — likely informative samples (wood-flow optimization, log haulage, procurement ERP, scaling/settlement) but unreachable; their absence narrows the evidence base, especially on the settlement and haulage-dispatch depth.

## Final Synthesis

Logging Operations Management is the harvest job's operating system. Its world is organized around the harvest operation — a defined block/tract taken on under contract — to which crews and machines are assigned; production (loads with species/grade/volume/origin/time, machine data, depleted area) is captured at the point of work and bound to the operation; and production settles into pay under contract terms, with the load record serving as the multiparty, dispute-resistant settlement artifact shared by forest owner, contractor, and mill. Around this core, mature products add plan-vs-actual replanning, map-centric field guidance with boundary alerts, machine telematics, digital load slips with weighbridge integration, dispatch, maintenance, and analytics. The Type ends where the estate record begins (Forestry Management) and where the chain-wide flow of fiber begins (Timber Supply Chain Management).
