# Research Notes — Forestry Management

## Research Goal

Understand what "Forestry Management" software actually is as an Application Type: what its system of record contains, who operates it, how forest work flows through it across its unusual multi-decade time signature, and where its boundaries sit against the neighboring Types in §20 (Logging Operations Management, Timber Supply Chain Management, Farm Management Platform, Fisheries Management, Natural Resource Rights Management) and in §21 (Conservation Management), plus the urban-forestry product cluster (no directory leaf exists for it).

## Initial Boundary

Hypothesis before research:

- Core use: managing forest land as a long-lived biological asset — knowing what grows where (inventory), planning and recording silvicultural treatment (planting, tending, thinning) and harvest over years-to-decades, within ownership/tenure and regulatory context.
- Likely users: forest managers/foresters, planners/analysts, field crews, landowners/TIMO asset managers, government agencies, consultants.
- Closest neighbors to disambiguate: Logging Operations Management (execution of harvest jobs), Timber Supply Chain (log flow to mill), Farm Management (annual-crop cousin), Conservation Management (protection-oriented land management), Fisheries Management (parallel regulated-harvest governance pattern), Government GIS / Land Records (spatial land data without the growing-resource semantics).
- Unknowns: whether the stand (management unit) is truly the universal organizing object; whether harvest is definitional or whether inventory+care-only forms exist (urban tree programs); how much of "operations" (machines, crews, loads) belongs to this Type vs the Logging sibling.

## Research Questions

1. What objects exist in the world of a forestry management system (estate, property, stand, compartment, coupe, block, tree)?
2. What does the inventory of record contain, and through what machinery is it maintained (cruise, mobile capture, remote sensing, LiDAR)?
3. What is the planning object — working plan, harvest schedule, silvicultural prescription — and what time horizon does it carry?
4. Which activities are planned and recorded (regeneration, tending, thinning, harvest, roads)?
5. What roles use it, and what are the main surfaces (map, table, planning workspace, mobile capture, dashboards)?
6. Which rules/constraints matter (tenure, regulation, certification, sustained yield)?
7. Where does this Type end and Logging Operations / Timber Supply Chain begin?
8. Does an inventory+care-only form (urban tree management) belong to this Type or sit across the boundary?

## Representative Products

Selected for market representativeness, different product philosophy, different customer tiers (with the caveat that the final reachable sample is skewed; see Sources & Limitations):

1. **Remsoft** (remsoft.com) — integrated forestry platform pole + optimization planning pole. Suite spans Forest Management System (FMS, built on the acquired INFLOR Forest), Planning & Optimization (Woodstock Optimization Studio, Tactical Optimization, Strategic Optimization), field capture (Prism), LiDAR inventory (AFRIDS), operations (Remsoft Operations, Op Tracker machine telematics), logistics (ScalePass load slips, LOGR delivery records), MRO. Clients named on-site: Mondi (~250,000 ha), Suzano, American Forest Management, Reliance Forest Fibre. Enterprise/industrial tier.
2. **PlanIT Geo TreePlotter** (planitgeo.com/treeplotter/) — urban/community forestry pole: tree inventory & asset management on a web GIS, desktop system of record + mobile field capture, work orders, reporting, canopy analysis. Government / university / nonprofit tier. Sampled deliberately as the closest boundary case (individual-tree object world).
3. **Trimble Forestry** (trimble.com/en/industries/forestry) — enterprise pole, positioning-level only (JS-gated content): "Powering the forestry business… forestry solutions that drive productivity and profitability," hero imagery spanning forest → processing → logs → trucks. Market anchor only; no operational claims.

Considered and rejected/unreachable:
- **SilviaTerra** (silviaterra.com) — domain now serves an unrelated PDF-download spam site; company site unreachable → abandoned (network rule).
- **Silvacom FMS** — vendor site now presents consulting services only; product pages not reachable from it → abandoned.
- **Lim Geomatics (Ops)** — /products/ops/ 404; root fetch returned unrelated content → abandoned.
- **INFLOR Forest** (inflor.com/inflor-forest/) — timeout ×2 → referenced only through Remsoft's own Tier-1 product listing.

## Sources

Fetched 2026-09-08 (WebFetch):

- https://www.remsoft.com/ — Tier-2: platform framing ("From forest inventory to mill delivery"), full product catalog with one-line positioning per product.
- https://remsoft.com/solutions/fms/ — Tier-2 (closest to Tier-1 available): FMS module list with functional descriptions (Land & Forest Registry, Integrated Forest Planning, Silviculture Management, Nursery & Seedling Production, Harvest & Operations Management, Operational Monitoring & Reporting; secondary capabilities; powering products Stratus/Prism/AFRIDS/INFLOR Forest).
- https://remsoft.com/woodstock-optimization-studio/ — Tier-2: optimization modeling platform detail (scenario/what-if, land valuation, strategic/tactical/S&OP planning incl. harvest-and-road planning, carbon).
- https://planitgeo.com/treeplotter/ — Tier-2: TreePlotter suite (INVENTORY, CANOPY, Mobile, Projects), desktop-as-system-of-record vs mobile-field-capture split, work orders.
- https://www.trimble.com/en/industries/forestry and https://forestry.trimble.com/ — Tier-2 positioning only; product detail JS-gated (2 fetch attempts, same shell content). Recorded as source-access limitation.

Unreachable / abandoned (each 1–2 attempts per network rule): silviaterra.com (domain squatted), inflor.com (timeout ×2), forestmetrix.com (timeout), limgeomatics.com (404/redirect), silvacom.com (product not surfaced).

Corroborating first-hand notes already in repo (other passes): conservation-management research cites CyberTracker as a shared field-tool layer used in "farming, forestry" (tool layer shared, purpose differs); crop-remote-sensing research lists forestry among a remote-sensing platform's served sectors.

## Product A — Remsoft

### Key observations

- **Platform span** ("From forest inventory to mill delivery"): FMS, Planning/Optimization, Operations, Logistics, MRO — a vendor-built statement that the market packages "forest management" as the land/asset half of a wider forest-to-mill chain.
- **FMS module set (functional descriptions, Tier-2):**
  - Land & Forest Registry — "Centralize property data, environmental documentation, and forest stand information in a structured digital registry."
  - Integrated Forest Planning — "Plan forestry activities with visibility into resources, operational constraints, and production targets."
  - Silviculture Management — "Plan and monitor silviculture activities including planting, fertilization, pest control, and maintenance."
  - Nursery & Seedling Production — "Manage seedling production and nursery operations with full traceability across planting programs."
  - Harvest & Operations Management — "Track harvesting preparation, contractor activities, and operational performance across the forestry production chain."
  - Operational Monitoring & Reporting — "dashboards and reports that support operational analysis and compliance reporting."
  - Secondary: Activity Management (plan/track forestry operations from scheduling to completion), Fibre Forecasting & Production Monitoring, Land & Property Management (ownership records, contracts, environmental documentation), Research & Genetic Programs.
- **Stand** is the named organizing unit ("forest stand information"); property/land/ownership context is explicit.
- **Inventory machinery**: mobile field data collection (Prism — "Mobile tools for capturing and syncing field data in real time", built on Esri ArcGIS per product blurb), LiDAR-derived inventory (AFRIDS — "LiDAR-driven system for high-resolution forest inventory and analysis").
- **Planning machinery (Woodstock)**: mathematical optimization modeling; scenario & what-if analysis; planning layers named Land Valuation ("timberland valuation and estate modeling… forest valuation, harvest and silviculture analysis, forecasting timber resource growth, forecasting product and environmental value (carbon)"), Strategic Planning ("long-term forest and sustainability management planning — harvest and product planning, silviculture planning, discounted cashflow analysis…"), Tactical Planning ("coordinated harvest and road planning, wood flow and delivery planning, capacity planning, budget planning"), S&OP. Solution page: "…schedule optimization to support decisions that balance timber yield, sustainability, and business goals across **multi-decade planning horizons**."
- **Time signature**: multi-decade planning horizons stated verbatim; growth forecasting ("forecasting timber resource growth") as a first-class analytic.
- **Compliance/reporting**: "reliable reporting for operational, regulatory, and certification requirements"; environmental documentation held in the registry.
- **Operations/execution machinery sits beside, not inside, the FMS**: Remsoft Operations ("Connect planning with day-to-day execution… schedules, equipment, loads, and workforce productivity"), Op Tracker (machine telematics), ScalePass (digital load slips), LOGR (delivery records). This is first-hand vendor evidence for the seam toward Logging Operations Management / Timber Supply Chain: the forestry-management product plans and tracks harvests on stands; machine-, crew- and load-level execution machinery is a separate product line.
- **Customers**: industrial forest products (Mondi, Suzano), timberland management (American Forest Management), integrated planning (Reliance Forest Fibre) — enterprise tier.

## Product B — PlanIT Geo TreePlotter (boundary pole — urban forestry)

### Key observations

- Positioning: "tree inventory and asset management software… to map and manage your urban forest," "built on a web-based GIS platform and optimized for mobile use."
- Object world: individual trees (asset management of trees), not stands; but the record structure rhymes with production forestry: map-based inventory as system of record, per-tree attributes, care programs.
- Desktop is described verbatim as "your **full system of record**… complete inventory data, reporting, and planning tools all in one place"; Mobile is "built for the field… for crews and inspectors to capture and update tree data on-site, in real time."
- Header function set: "Inventory, Management, Outreach, Reporting, Work Orders" — care work orders as the program leg (planting/pruning/removal analog of silviculture); CANOPY adds analysis ("View, plan, and grow the urban forest with data analysis tools").
- Clients: government, university/campus, nonprofits — municipal/community tier.
- Reading: urban tree management shares inventory-of-record + care-program + work-order machinery with this Type but replaces the stand-based estate with individual trees and harvest with removals. It is the closest relative across the boundary; the directory has no leaf for it, so it is recorded as a boundary finding and flagged, not forced into the Type.

## Product C — Trimble Forestry (positioning anchor only)

### Key observations

- "Trimble Forestry — Powering the forestry business. Adaptive, reliable, industry-leading forestry solutions…"
- Hero imagery spans the whole chain: forest, processing facility, stacked logs, logging truck — the category is marketed as land-to-mill.
- Product documentation JS-gated; nothing operational claimed from this source. (Evidence Layer A denied; used only as B-level corroboration that the category label "forestry" spans estate management through delivery.)

## Cross-product Comparison

| Dimension | Remsoft (FMS + Woodstock) | TreePlotter (urban) | Trimble (positioning only) |
|---|---|---|---|
| Managed subject | forest estate: properties/land + forest stands | urban forest as individual-tree asset population | forest business (imagery spans land→mill) |
| System-of-record framing | "structured digital registry" of property data, environmental documentation, forest stand information | "full system of record… complete inventory data" | n/a |
| Inventory machinery | mobile field capture (Prism), LiDAR inventory (AFRIDS), growth forecasting | field/mobile capture and update in real time; canopy analysis | n/a |
| Program machinery | Integrated Forest Planning; Silviculture Management (planting/fertilization/pest/maintenance); Harvest & Operations Management; Activity Management | Management + Work Orders (care programs); removals | n/a |
| Time signature | multi-decade planning horizons (verbatim); strategic/tactical layers | seasonal/annual work programs (implied) | n/a |
| Harvest | explicit (harvest preparation, contractor activities, harvest scheduling, harvest-and-road planning) | absent (removals only) | implied (logs/trucks imagery) |
| Compliance/reporting | operational, regulatory, certification reporting | reporting/outreach to community | n/a |
| Execution machinery | separate product lines (Operations/Op Tracker/ScalePass/LOGR) | work-order completion by crews | n/a |

Stable commonalities across the reachable sample (independent vendors):
1. A map-anchored inventory of record for trees/forest (Remsoft registry; TreePlotter system of record).
2. Planned-and-recorded care/treatment/harvest programs over that record (silviculture/harvest; work orders).
3. Mobile field capture as the standing data-maintenance surface.
4. Reporting oriented to accountability (regulatory/certification; public/community reporting).

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The forest estate of record** — forest land held as a managed estate, organized into spatially addressed management units (stand / compartment / coupe / block — vocabulary varies by region and vendor), each carrying identity, area, location, and tenure/ownership context.
   - Remove → land/property registry or cadastral/GIS viewer; the "managed forest estate" is gone.
2. **Standing forest inventory per unit** — the growing stock described per unit (species composition, age/size class, stocking/volume) as maintained data — the estate's living biological asset base — updated through measurement (field cruise, remote sensing) and/or modeled growth.
   - Remove → property records with no forest state; inventory-only tools become one-shot cruise calculators or map viewers.
3. **The multi-year silviculture-and-harvest program** — treatments planned and recorded per unit across years to decades (regeneration/planting, tending, thinning, harvest), accumulating each unit's treatment history; scheduling the program across the estate (harvest scheduling / sustained-yield planning) is the mature form.
   - Remove → static inventory census/valuation snapshot, or a generic activity tracker with no forest semantics.

Jointly-held is load-bearing:
- 1 alone = land registry / Government GIS territory
- 2 alone = cruise calculator / one-shot inventory report
- 3 alone = generic plan/task tracker
- 1+2 without 3 = inventory census (inventory-first capability slice at the Type's edge)
- 1+3 without 2 = activity mapping with no forest state behind it
- 2+3 without 1 = plot-level records with no estate structure (cruise-tool territory)

### L1 — Common Mature Structure (standard, not definitional)

- Map/GIS surfaces (web GIS, stand polygons, layers) — the dominant navigation surface
- Mobile field data capture (cruise/inspection apps, real-time sync)
- Remote-sensing / aerial-imagery / LiDAR inventory as an era-current inventory update channel
- Growth & yield modeling / timber-resource growth forecasting
- Harvest scheduling with scenario & what-if analysis (optimization is the enterprise pole, not the invariant)
- Timberland valuation / estate modeling (cash flow, discounted value)
- Roads/infrastructure planning coupled to harvest
- Permit / regulatory / certification reporting and environmental documentation storage
- Activity/operations scheduling and completion tracking; contractor activity tracking
- Operational dashboards and reporting

### L2 — Variant / Optional Structure

- Customer-shape variants: industrial forest-products owner; timberland investment manager (asset-management/valuation emphasis); government agency (multi-use estate, public accountability); consultant serving many small owners; family/community forests.
- Region/workflow variants: plantation vs natural forest; even-aged vs uneven-aged management; regional silvicultural traditions and terminology (compartment/coupe/stand).
- Nursery & seedling production, research/genetic improvement programs (module-gated; Remsoft-only evidence in sample → optional).
- Carbon accounting/value as a modeled output (era-current; one vendor in sample).
- Urban/community forestry (individual-tree object world, care work orders, canopy analysis) — closest cross-boundary relative; see Boundary Findings.
- Integration toward execution: machine telematics, load slips, delivery records — held by adjacent Types' machinery (Logging Operations / Timber Supply Chain), appearing in this Type only as packaging.

### L3 — Vendor-specific Detail (research notes only)

- Remsoft product names: Woodstock Optimization Studio, Tactical/Strategic Optimization, Stratus, Prism, AFRIDS, Op Tracker, ScalePass, LOGR, MRO; INFLOR Forest (acquired 2026 per vendor news; AFM testimonial names "INFLOR FMS").
- Remsoft's ArcGIS underpinnings for Prism/AFRIDS; "Forest Intelligence Platform" branding; customer-survey statistics on homepage (efficiency/precision percentages — marketing, not operational fact).
- TreePlotter product names: INVENTORY, CANOPY, Projects, Mobile; NatureScore; UK/localized support lines.
- Trimble "Arc Agent" AI-agent marketing (cross-industry, not forestry-specific).

## Boundary Findings

- **vs Logging Operations Management (§20 sibling)** — sharpest industrial seam, corroborated first-hand by a vendor's own product split: Remsoft keeps "Forest Management" (estate, silviculture, harvest planning/tracking on stands) separate from "Operations" (schedules, equipment, loads, workforce) and machine telematics (Op Tracker). Removal test: remove the estate/inventory/silviculture record and only job execution remains → Logging Operations; remove job-execution machinery and the estate record remains → this Type. The forestry Type records *what the forest got and what was cut*; logging records *how the job ran*.
- **vs Timber Supply Chain Management (§20 sibling)** — downstream log flows (landing → truck → mill, load slips, delivery records, trade) are supply-chain machinery (Remsoft ScalePass/LOGR live there, not in FMS). Remove the mill-side log flow and this Type stands; remove the estate and only the supply chain remains.
- **vs Farm Management Platform (§20)** — both manage land + a biological production cycle, but the time signature and inventory semantics differ: crops reset annually on fields; forests persist across decades with standing stock that grows between selective/partial interventions. Harvest ends a rotation that was planned decades earlier.
- **vs Conservation Management (§21)** — re-confirms that pass's recorded seam: production orientation (timber yield/revenue from the estate) vs protection/restoration orientation; field-data tooling may be shared, record structure and purpose differ.
- **vs Fisheries Management (§20)** — DISCHARGES that pass's forward flag ("parallel resource-governance pattern — harvest rights, permits, harvest records on a regulated common resource"). The parallel is real but partial: both record authorized harvest of a biological resource. The seam is the object world: fisheries governs catch of a wild common stock via entitlements/limits, with no managed standing asset owned by the harvester and no treatment of the resource; forestry manages an owned/tenured standing biological asset whose growth the owner invests in over decades and actively shapes (planting, thinning). Forestry's tenure/permit layer is a variant (Crown/concession estates exist), not the frame itself.
- **vs Government GIS / Land Records / Cadastre (§24)** — 1-alone failure mode: parcel records without growing-stock semantics or a treatment program.
- **vs Natural Resource Rights Management (§20)** — rights/permits as the whole world vs permits as a reporting/tenure layer inside the estate record.
- **vs Utility Vegetation Management (§19)** — vegetation managed for infrastructure clearance vs forest managed as a production/stewardship estate.
- **vs Urban tree inventory management (no directory leaf; TreePlotter pole)** — shares inventory-of-record + care-program + work-order machinery but replaces the stand-based estate with individually addressed trees and harvest with removals/care. Held as a boundary finding: if this cluster is ever added to the directory it likely warrants its own leaf or an explicit variant decision; recorded in Boundary Issues.

## Uncertainties

- Reachable sample is Remsoft-heavy (three of four sampled surfaces belong to one vendor after consolidation); independent corroboration comes from TreePlotter (urban analog) and Trimble positioning only. Claims are therefore calibrated ("in the researched sample…"), and several structure claims rest on Remsoft's Tier-2 module descriptions plus the urban analog's rhyming structure.
- Official help-center/user-guide documentation (Tier-1 operational detail: exact stand attribute schemas, cruise methods, schedule granularity, state names) was not reachable for any sampled product; no precise numeric/limit claims are made anywhere.
- The historical check is conceptual, not source-verified: the paper-era working-plan tradition (compartment registers + stand maps + cruise tally sheets + yield tables + rotation-based working plans) is asserted from domain knowledge of the discipline, not from a fetched historical source. It passes the three-leg test analogically; no digital-era feature appears in the definition.
- Whether inventory-first products (LiDAR/cruise layers sold standalone) should be read as capability slices of this Type or a sub-Type was resolved as "capability slice at the Type's edge" (precedent: other passes' edge poles), based on the single reachable inventory-first surface being absorbed into a suite (AFRIDS inside Remsoft's platform).
- Urban forestry placement (own Type vs variant) is a genuine taxonomy question — flagged, not decided.

## Final Synthesis

Forestry Management software is the forest estate's system of record: the estate as mapped, addressed management units; the standing forest inventory that makes the estate a living measured asset; and the multi-year silviculture-and-harvest program that the owner plans, executes, and accumulates per unit — with compliance reporting and (in the mature form) scenario-driven scheduling across decades. It ends where the harvest job is executed (Logging Operations), where logs become loads to mills (Timber Supply Chain), and where the land's purpose flips to protection (Conservation). The urban-tree cluster is the closest relative across the boundary and is flagged for the taxonomy owner.
