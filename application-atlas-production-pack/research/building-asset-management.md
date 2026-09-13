# Research Notes — Building Asset Management

## Research Goal

Understand what "Building Asset Management" software actually is as an Application Type: what the managed objects are, who uses it, how the asset lifecycle loop works, and how it differs from its very close neighbors (Building Maintenance Management, CMMS/EAM, Building Condition Assessment, Facility Management / IWMS, BMS, Building Energy Management).

## Initial Boundary

- Directory leaf: §17 Construction, Real Estate & Facilities — "Building Asset Management" (between "Building Condition Assessment" and "Building Energy Management").
- Working hypothesis: a system of record for the physical equipment and systems *inside and around* buildings (HVAC, boilers, electrical, elevators, roofs, pumps...) — asset register + location + care history + condition/lifecycle + renewal planning.
- Not to be confused with: financial asset management of real estate (separate leaf: Real Estate Investment Management), IT asset management, EAM for industrial plant.
- Risk identified up front: this Type is close to the CMMS/EAM family; the research must decide whether it is a distinct Type or an industry-flavored Variant.

## Research Questions

1. What counts as a "building asset" in real products? What fields/attributes does an asset record carry?
2. How are assets organized and located (building hierarchy, floor plans, systems, hierarchies, relationships)?
3. What is the care loop? How do work orders / preventive maintenance attach to assets?
4. Where do condition and lifecycle come from (assessments, work orders, meters, IoT)?
5. What is the renewal/capital-planning layer (replacement forecasting, FCI, deferred maintenance, funding scenarios)?
6. Who uses it (technicians, facility managers, capital planners, owners) and on what surfaces (desktop, mobile, QR scan)?
7. How does the sample differ from generic CMMS (Fiix) and from IWMS suites (IBM Maximo Real Estate & Facilities)?
8. Historical check: would pre-cloud facility asset management (asset registers + work logs) still fit the definition?

## Representative Products

| Product | Vendor / posture | Why sampled |
|---|---|---|
| Asset Essentials | Brightly (Siemens) — facility/infrastructure CMMS-led asset management | Market leader; education/government/healthcare/manufacturing anchor |
| Maintenance Connection | Accruent — enterprise CMMS/EAM sold under "Facility Asset Management" | Enterprise multi-site pole; explicit "Facility Asset Management" solution category |
| AkitaBox (Platform / Capital Management / Capture / FCA) | AkitaBox — facility asset lifecycle suite | Asset-data + capital-planning pole; FCA (facility condition assessment) integration; modern mid-market |
| Fiix | Fiix (Rockwell Automation) | Boundary anchor: generic industrial CMMS with an asset module — used to test what is building-specific vs generic |
| IBM Maximo Real Estate & Facilities (ex TRIRIGA) | IBM | Boundary anchor: IWMS suite posture — asset/maintenance as one module among lease/space/energy/capital |

Rejected for sample: eSSETS (site unreachable 503 ×2 — abandoned per network rules); UpKeep (redundant with Fiix as CMMS anchor).

## Sources

- Brightly, "Asset Essentials | CMMS Asset Management Software" — https://www.brightlysoftware.com/products/asset-essentials (fetched 2026-09-06)
- Brightly (Siemens), "Predictor — Capital Planning & Asset Management" — https://www.brightlysoftware.com/products/predictor (fetched 2026-09-06)
- Accruent, "Cut Costs with Maintenance Connection CMMS" — https://www.accruent.com/products/maintenance-connection (fetched 2026-09-06)
- Accruent, "Facility Asset Management Software" — https://www.accruent.com/solutions/facility-asset-management-software (fetched 2026-09-06)
- AkitaBox, "AkitaBox Platform – Asset & maintenance management" — https://home.akitabox.com/software/akitabox-platform/ (fetched 2026-09-06)
- AkitaBox, "AkitaBox Capital Management Software" — https://home.akitabox.com/software/akitabox-capital-management/ (fetched 2026-09-06)
- AkitaBox, homepage / suite overview (Capture, FCA, Inspections, Connect) — https://akitabox.com/ (fetched 2026-09-06)
- Fiix, "Asset maintenance management software" — https://www.fiixsoftware.com/cmms/asset-management-software/ (fetched 2026-09-06)
- Fiix, homepage — https://www.fiixsoftware.com/ (fetched 2026-09-06)
- IBM, "Real Estate and Facilities Management | IBM Maximo" — https://www.ibm.com/products/tririga (fetched 2026-09-06)

Evidence layers: A = directly observed on a specific product's official pages; B = cross-product commonality (≥2 sampled products); C = canonical inference from cross-product comparison + boundary reasoning. All evidence in this pass is Layer A from vendor product/solution pages; no vendor help-center articles were fetched, so no precise operational numbers/defaults are asserted anywhere.

## Product Observations

### Brightly Asset Essentials (evidence A)

- Positioning: "Industry-leading CMMS for smarter asset management"; FAQ defines asset management as "track, manage and maintain assets associated with facilities or infrastructure… manage and track all work and parts associated with repairs and replacement of vital systems needed to maintain service levels."
- Asset register: "Build a richer, more reliable asset register by capturing comprehensive asset information — specifications, performance metrics and documentation."
- Care loop: work order management, "unified PM schedules and automated work order creation", technicians update asset histories from the field; Maintenance Copilot (AI) for guidance/summaries.
- Lifecycle/renewal: "identify problematic assets sooner and make better repair vs. replace decisions", "informed decisions for daily operations, capital planning and compliance management".
- Adjacent modules: parts inventory (low-stock notifications, PO sync with ERP), IoT remote monitoring → auto-generated corrective work orders, analytics/AI.
- Related Brightly products confirm the wider asset-management family: Predictor (asset lifecycle prediction modeling + capital planning, funding scenarios "decades into the future", degradation at "component, asset, asset type or asset class level"), Origin (asset health from CMMS data), Assetic/Confirm (public infrastructure asset management), TheWorxHub (senior-living facility CMMS), Energy Manager.
- Industries: education, government, healthcare, senior living, manufacturing, infrastructure.

### Accruent Maintenance Connection (evidence A)

- Positioning: multi-site CMMS and EAM; Accruent maintains a distinct "Facility Asset Management" solution category landing on these products.
- Features observed: work order management, asset & inventory control, preventive maintenance scheduling "based on time, usage, or condition-based triggers", mobile-first (offline, barcode & QR scanning), self-service reporting/analytics, automated notifications, integrations (Esri/ArcGIS, ERP, SCADA, HR, EDMS, IoT, open API), e-signatures and audit trails for compliance, SaaS or on-premises.
- Asset Lifecycle Management described as: "tracks and manages every aspect of an asset's lifecycle from acquisition to retirement, providing valuable insights into performance, usage and maintenance history."
- Customer quote (UC Riverside): asset module detail includes "warranty information and life expectancy" previously kept "in binders".
- FAQ taxonomy: distinguishes CMMS (maintenance tasks/schedules), EAM (asset lifecycle), ERP, APM, FM ("manage building systems and facilities"), IoT-enabled maintenance.
- Repair-vs-replace decision support named for manufacturing pole; retail/multi-site posture.

### AkitaBox (Platform + Capital Management + suite) (evidence A)

- Positioning: "Facility & Asset Lifecycle Software — Assess & Optimize Your Facilities"; "understand your building's history, current condition, and projected future."
- Suite decomposition (itself informative): Capture (facilities asset data collection app), FCA (digital facility condition assessment capture), Platform (asset + maintenance management + occupant portal), Capital Management (asset condition & failure probability tracking), Inspections (compliance), Connect (Procore integration for construction handover).
- Platform asset layer: digital floor plans (2D Revit-based) with location-based asset mapping; QR code scan on asset → documentation + maintenance history; asset & space inventory (rooms/spaces + assets by location); historical asset data ("monitor asset lifecycles… compared to the industry standard", "overall condition of every asset"); asset relationships ("which equipment serves which space", "which assets serve or depend on other assets"); customizable data fields; document management (warranties, manuals attached to rooms/assets).
- Platform maintenance layer: work orders (reactive + preventive), service request portal for occupants (submit request, pin location on floor plan, track status), PM schedules with automated reminders/routing, calendar view (drag-drop reschedule, filter by asset/trade/tech), maintenance reporting dashboards (WOs completed, hours logged, deferred/canceled), mobile apps (Work app, Capture app, browser).
- Capital Management: RSMeans data integration (industry-standard repair/replacement costs); 30-year cost projections; deferred maintenance; high-risk identification (condition, severity of failure, mission criticality); "continuous condition updates" — techs save asset/assembly conditions when completing work orders; Portfolio FCI tracking per building + projected FCI; budget scenario dashboards ("consequences of lower facility budgets, building FCI, maintenance backlog"); CRE framing (NOI, replacement reserves).
- Industries: healthcare, higher ed, K-12, government, commercial real estate, AEC/facilities services.

### Fiix (boundary anchor — generic CMMS) (evidence A)

- Asset module: asset records with repair history, cost, parts consumption; QR/barcode attach-and-scan; asset hierarchy (drag-drop tree, parent-child filtering); multi-site organization by location; asset categories; meter readings (usage-based maintenance triggers); downtime tracking + MTTR/MTBF KPIs; custom fields; criticality ratings; asset insights dashboards (abnormal maintenance spend).
- Maintenance-strategy framing: reactive / preventive / predictive / reliability-centered.
- Industries: oil & gas, heavy equipment, food & beverage, manufacturing — i.e., the production-equipment pole. Facility managers appear among customers, but the product is not building-specific.
- Confirms: the asset record + work order + PM loop is a *generic* CMMS structure; what the building type adds is the building/location model, the building-systems asset taxonomy, and the renewal/capital economics.

### IBM Maximo Real Estate & Facilities (boundary anchor — IWMS suite) (evidence A)

- Suite modules: lease management (AI lease abstraction, lease accounting), space management (occupancy analytics, layouts), capital planning, maintenance and operations ("aligned locations, assets, and work orders" in one mobile-optimized system), environmental & energy management.
- Deployment: SaaS editions ("Essentials" packages for Space/Lease/Capital Planning on AWS Marketplace), full suite, customer-managed; FedRAMP for government.
- Industries: government, healthcare, education, corporate real estate.
- Confirms: in an IWMS, building asset/maintenance management is one module among real-estate and space functions; the asset-location-work order alignment is shared with the standalone type.

## Cross-product Comparison

| Finding | Asset Essentials | Maintenance Connection | AkitaBox | Fiix | Maximo REF | Layer |
|---|---|---|---|---|---|---|
| Identified asset records as central object (specs, serial/model, docs) | ✓ | ✓ | ✓ | ✓ | ✓ ("locations, assets") | B |
| Assets located within a building/site structure | ✓ (facility/infrastructure framing) | ✓ (multi-site, GIS) | ✓✓ (floor plans, rooms, asset pins) | location = site-level | ✓ (locations aligned) | B |
| Work orders + PM attached to assets | ✓ | ✓ (time/usage/condition triggers) | ✓ (reactive + PM + occupant requests) | ✓ | ✓ | B |
| Care history accumulating per asset | ✓ ("update asset histories") | ✓ ("maintenance history") | ✓ ("historical asset data") | ✓ (repair history) | ✓ | B |
| Condition captured/updated (assessments, WO completion) | ✓ (asset health, Predictor) | ✓ (condition-based triggers) | ✓✓ (FCA capture + WO-completion condition updates) | ✓ (criticality, meters) | ✓ ("condition insights") | B |
| Lifecycle outlook / repair-vs-replace | ✓ (repair vs replace) | ✓✓ (acquisition → retirement) | ✓✓ (lifecycle vs industry standard) | – (cost/KPI level) | ✓ (capital planning module) | B |
| Capital planning / replacement forecasting (FCI, backlog, funding scenarios) | via Predictor companion | – (not observed) | ✓✓ (Capital Management: 30-yr projections, portfolio FCI) | – | ✓ (capital planning module) | B |
| Mobile + barcode/QR on assets | ✓ (field technicians) | ✓ (barcode & QR scanning) | ✓ (QR scan → history; Capture app) | ✓ | ✓ (mobile-optimized) | B |
| Parts/inventory management | ✓ (low-stock, PO sync) | ✓ | – (not observed) | ✓ | – (not observed) | B |
| Occupant service requests | – (not observed) | – (not observed) | ✓ (occupant portal) | – | – | A (product-specific) |
| Energy/BMS/IoT monitoring integration | ✓ (IoT → corrective WOs) | ✓ (SCADA/IoT integration) | – (not observed) | partial (Optix integration) | ✓ (energy management module) | B |
| Construction-to-operations handover | – (not observed) | – (not observed) | ✓✓ (Capture app + Procore Connect) | – | – | A (product-specific) |
| Cost-standard libraries (RSMeans-type) | – (not observed on AE page) | – | ✓✓ | – | – | A (product-specific) |

## Canonical Model (C-layer synthesis)

```text
Building/Facility Portfolio (sites → buildings → floors/areas → rooms)
└── Building Asset (identified record: system/trade, make/model/serial, install date,
│   expected life, replacement cost, documents/warranty, condition)
│   ├── Location binding (where it is; often mapped on floor plans)
│   ├── Care events (work orders: reactive, preventive, inspections; labor + parts + cost)
│   ├── Condition & lifecycle state (age/usage/condition → remaining life)
│   └── Relationships (serves which spaces; depends on / feeds which assets)
└── Renewal outlook (deferred maintenance backlog, replacement forecast,
    FCI/condition indices, funding scenarios → capital plan)
```

Defining-invariant candidates (L0, deliberately small):

1. **Building-located physical asset records** — individually identified equipment/systems/components of a building portfolio, bound to a place in the building.
2. **Recorded care attached to each asset** — maintenance/service events accumulate on the asset as durable, attributable history.
3. **Lifecycle outlook per asset** — condition/age/expected-life view that projects future care and replacement (the register exists so owners can decide what to fix, keep, and replace).

Fails-the-type tests:
- Remove (1)'s building/location context → generic EAM/CMMS.
- Remove (3) → work-order maintenance management (CMMS) or a static inventory.
- Remove (2) → an inventory/condition-assessment registry, not management.
- Remove the asset anchoring itself (work orders without objects) → generic maintenance operations.

L1 (common mature structure): work order + PM engine bound to assets; service requests; asset detail attributes (make/model/serial, install date, warranty, expected life, replacement cost, custom fields, photos, documents); site→building→floor→room location model with visual mapping (floor plans); system/trade grouping + parent-child hierarchy + serves/depends-on relationships; mobile apps + barcode/QR; per-asset cost tracking; parts inventory; condition ratings & assessment capture; KPI dashboards & audit trails; role-based access; ERP/GIS/IoT integrations.

L2 (variant structure): center-of-gravity pole (maintenance-operations-first vs capital-planning-first vs data-capture/FCA-first); suite-embedded (IWMS module) vs standalone; portfolio scale (single building → multi-site → public infrastructure); industry tuning (education/government bond & deferred-maintenance framing, healthcare criticality/compliance, CRE NOI/reserves framing, manufacturing plants); capital-planning depth (FCI, scenario/funding modeling, cost-standard data libraries); data acquisition strategy (vendor data-collection services, self-capture apps, BIM/construction handover, IoT/BMS feeds); financial-layer depth (depreciation/fixed-asset alignment); standards vocabulary (ISO 55000-flavored public asset management).

L3 (vendor-specific, keep out of final doc): Brightly product names (Asset Essentials, Predictor, Origin, TheWorxHub, Assetic, Confirm, Maintenance Copilot), client counts and case-study figures; Accruent product names (TMS, FAMIS 360, Observe, RedEye, Meridian, Data Connect, Esri integration), SaaS/on-prem split; AkitaBox module names (Pulse, Capture, FCA, Capital Management, Inspections, Connect), Revit-pinned floor plans, RSMeans integration, 30-year projection, SOC2; Fiix MAX AI, FactoryTalk Optix, MTTR/MTBF specifics, uptime/backup stats; IBM TRIRIGA lineage, AI lease abstraction, FedRAMP, AWS Marketplace Essentials editions.

## Vendor-specific Findings

- AkitaBox occupant service-request portal with floor-plan pinning — only in-sample instance (product-specific, plausible common in facility suites but not generalized).
- AkitaBox construction handover (Capture + Procore Connect) — product-specific in sample.
- AkitaBox RSMeans cost-data integration + 30-year projections — product-specific implementation of a plausible common need.
- Brightly splits lifecycle prediction/capital planning into a companion product (Predictor) fed by CMMS data — packaging-specific; Accruent and Maximo embed equivalents.
- Fiix's meter-based maintenance triggers and MTTR/MTBF KPIs — CMMS-generic; not building-specific.
- IBM's lease management / space management / energy modules — suite-specific; define the IWMS boundary, not this Type.

## Boundary Findings

- **vs CMMS / Maintenance Management (§16) and Building Maintenance Management (§17)** — the sharpest seam. All building-asset-management products contain a CMMS-shaped care loop. The differentiator is the *center of gravity*: in a CMMS the work order/maintenance program is the central object; in Building Asset Management the durable asset record with location + condition + lifecycle economics is central, and work orders are evidence that advance each asset's state. Test: remove the renewal/lifecycle layer and the building-location model → it degrades into a CMMS. Conversely a CMMS can be used for building assets without ever modeling renewal — which is why generic CMMS is a sibling tool, not this Type.
- **vs Enterprise Asset Management (§16)** — EAM spans all asset classes (plant, fleet, IT, infrastructure) with deep finance alignment. Building Asset Management is the buildings/facility-scoped slice. Public-infrastructure asset management (Brightly Assetic/Confirm pole) sits between the two and shows the boundary is domain-of-assets, not feature set.
- **vs Building Condition Assessment (§17)** — assessment is a periodic data-production activity (condition surveys, FCI); asset management maintains the continuous record the assessment feeds. AkitaBox literally ships them as separate modules (FCA vs Platform/Capital Management). Remove the continuous care/lifecycle loop → you have an assessment tool.
- **vs Facility Management System / IWMS (§17)** — IWMS is a suite whose center is the real-estate/space estate (lease, space, projects) with asset/maintenance as one module (Maximo REF). Remove lease/space/energy and keep the asset loop → this Type.
- **vs Building Management System / BMS (§17)** — BMS is real-time control/automation of building plant; asset management is the record/planning system. IoT feeds can connect the two, but the objects and loops do not overlap.
- **vs Building Energy Management (§17)** — energy management optimizes consumption/performance; asset management governs care and replacement. Overlap point: shared equipment records and IoT monitoring, but the optimization objective differs.
- **vs Enterprise Asset Registry (§10) and Equipment Administration Platform (§10)** — registry = record of holdings without the care/lifecycle loop; equipment administration = circulating movable pool (checkout/return custody). Building assets are fixed systems whose "circulation" is maintenance, not handover.
- **vs Real Estate Investment Management (§17)** — "asset" in the financial-property-value sense vs physical operating assets. Different objects, different loops; only the word overlaps.
- **vs Capital Improvement Planning (§24)** — public-sector capital program planning consumes this Type's condition/FCI data as an input; it is a downstream planning process, not the asset record system.

Taxonomy note: market speech supports "Building Asset Management" as a recognizable slice ("facility asset management", "facility asset lifecycle") — Accruent maintains it as a named solution category, and the directory's §17 placement among building leaves is coherent. It is, however, conceptually an industry-scoped member of the asset-management family; flag for joint review with CMMS/EAM leaves if the taxonomy team wants a single family treatment.

## Historical / Market-Sample Check

Would older, regional, platform-native products fit the L0? Yes: pre-cloud facility departments kept asset registers (card files → spreadsheets → local CMMS) with work histories and replacement schedules; UK/NHS "estates" systems, Australian public-works asset management (Brightly Assetic lineage), and 1990s facility CMMS all exhibit: identified physical assets in buildings + recorded maintenance + condition/renewal outlook. None of the modern implements (floor-plan mapping, QR, IoT, AI forecasting, cost-data libraries) are required by the definition. No era/vendor over-fit detected.

## Uncertainties

- No vendor help-center articles were fetched (all evidence from product/solution pages, Layer A). Field-level asset-record schemas, exact state names, permission models, and numeric limits are therefore unasserted.
- eSSETS (pure-play "facility asset management" vendor) unreachable — cannot confirm the small-vendor pole; sample skews mid/enterprise.
- Whether "Building Asset Management" should be treated as an independent Type or as a §17-flavored variant of CMMS/EAM is a judgment call; market naming supports independent treatment, but the family relationship is strong and flagged for joint review.
- Occupant-facing service requests: observed in one sample product; likely common in facility suites but unverified breadth.
- Cost-standard data integrations (RSMeans-type) and construction-handover (BIM/COBie-style) breadth across the market unverified.

## Final Synthesis

Building Asset Management is the buildings-scoped member of the asset-management family: a durable register of the physical systems and equipment that make up a building portfolio, located within a building/room structure, accumulating care history, and projecting each asset's condition and replacement forward into renewal/capital decisions. Its care loop is CMMS-shaped; its location model and lifecycle/renewal economics are what make it "building" asset management rather than generic maintenance management. Products range from maintenance-operations-first to capital-planning-first to data-capture-first, and appear both standalone and embedded in IWMS suites.
