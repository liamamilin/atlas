# Research Notes — Enterprise Asset Registry

## Research Goal

Determine what an "Enterprise Asset Registry" is as an Application Type: what the system of record contains, who operates it, which workflows define it, and where its boundaries sit against the many adjacent registry-like Types in the directory (EAM, CMMS, IT Asset Management, CMDB, Inventory Management System, Equipment Administration Platform, sector asset-management leaves).

## Initial Boundary (hypothesis before research)

- Core hypothesis: an organization-scoped, item-level register of the physical assets the organization holds — one durable record per item, carrying identity, classification, tracked state (status / location / custodian), and history — maintained as the reference for "what do we have, where is it, who has it".
- Nearest neighbors expected to confuse: EAM / CMMS (§16), ITAM / CMDB (§14), Equipment Administration Platform (§10 sibling), Inventory Management System (§10), sector asset leaves (Public/Utility/Building Asset Management).
- Unknowns: whether the leaf name corresponds to a real market category; whether finance-oriented registers (fixed-asset ledgers) belong inside; whether checkout/reservation flows are defining or accessory; how the CMDB relationship graph differs structurally.

## Research Questions

1. What does one asset record contain across products (identity, classification, state, custody, financial, evidence, history)?
2. How do items enter and leave the register (registration/import → retirement/disposal), and which states do they pass through?
3. How is custody and location tracked (checkout/check-in, transfers, scans, default/return locations)?
4. Who uses the system (administrators, custodians, requesters, finance/auditors) and through which surfaces (web console, mobile scan, self-service)?
5. Which capabilities are defining vs common vs optional (audits, depreciation, maintenance, reservations, labeling, custom fields, roles)?
6. How does the type distinguish itself from quantity-based inventory, IT-specific ITAM, relationship-graph CMDB, and maintenance-centric CMMS/EAM?

## Representative Products

Chosen for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence tier reached |
|---|---|---|
| Snipe-IT | open-source, self-hosted; IT heritage, used cross-domain; record-centric | Tier-1 (official docs + API reference) |
| Asset Panda | cloud, mobile-first, cross-vertical enterprise asset tracking & accountability | Tier-2 (official product site) |
| EZO (EZOfficeInventory) | equipment-operations platform (EAM + CMMS posture), custody/request/maintain loops | Tier-2 (official product site) |
| Sortly | SMB, visual/photographic inventory-first with asset tracking as a use case | Tier-2 (official product site) |

Rejected as samples this pass: IBM Maximo / Fiix / MaintainX (EAM/CMMS pole — used only for boundary reasoning via EZO's own CMMS positioning), ServiceNow CMDB / BMC (CMDB pole — sources unreachable, see Sources).

## Sources

All fetched 2026-09-06.

- Snipe-IT official docs (Tier-1): https://snipe-it.readme.io/docs (introduction incl. "Which Tool is Right" tool-type comparison), https://snipe-it.readme.io/docs/asset-models.md, https://snipe-it.readme.io/docs/user-inventory.md, https://snipe-it.readme.io/docs/upcoming-audits.md, API reference https://snipe-it.readme.io/reference/hardware-create.md (asset record schema), doc index https://snipe-it.readme.io/llms.txt
- Asset Panda official site (Tier-2): https://www.assetpanda.com/ (platform, solutions, verticals, customer stories)
- EZO / EZOfficeInventory official site (Tier-2): https://www.ezofficeinventory.com/ (Track/Move/Maintain/Control, request portal, custody chain, FAQ incl. ITAM-family split, depreciation, lifecycle)
- Sortly official site (Tier-2): https://www.sortly.com/ (features, asset-tracking use case, folders/custom fields/audit reporting)

Unreachable (abandoned per network rules after repeated failures): ServiceNow CMDB pages (timeout ×1), BMC CMDB explainer (404), IBM Think CMDB topic (redirected to topic index), IBM Maximo docs (not attempted — budget). CMDB-side distinctions are therefore recorded at conceptual level only, without precise claims about specific CMDB products.

## Product Observations

### Snipe-IT (evidence layer A — Tier-1)

- Self-definition: free open-source "project asset management system", built for IT asset management ("track who has which laptop, when it was purchased, which software licenses and accessories are available"), explicitly used beyond IT ("oil rigs, theater equipment…").
- Official tool-type comparison (from the docs' "Which Tool is Right" list, credited to InvenTree): **Asset Management** "manages many unique items, which need tracking per part and are assignable to users / groups / locations… often include features like item states, refurbishing / maintenance / reservation, or request-flows" — explicitly contrasted with IMS (stock/part origin/orders/shelf life), PLM (BOMs/variants), MRP, ERP, CRM, MES.
- Asset record schema (from the /hardware create API, directly observed): **required**: `asset_tag` (or auto-generated when auto-increment enabled), `status_id` (status label), `model_id` (asset model). Optional: name, serial, purchase_date, purchase_cost, order_number, supplier_id, warranty_months, depreciate flag, notes, image, byod, requestable, `rtd_location_id` (documented as "where the item is when it's NOT checked out to someone"), location_id, last_audit_date, archived flag. Payload includes `physical` flag and `company_id` (company scoping).
- Checkout-on-creation accepts `assigned_user`, `assigned_asset`, or `assigned_location` — custody can bind to a person, another asset, or a place.
- Asset model: "Every asset needs an asset model" — models carry make/model, manufacturer, category, depreciation type, EOL, custom fieldsets, images; assets inherit from their model; requestable can be set at model or asset level.
- Audit loop: `last_audit_date` on the record, a per-asset audit API endpoint, "Upcoming Audits" notification with a configurable threshold; user-inventory emails list all items checked out to a user so they can self-report ("whether or not all of their items are still in their possession and in working order"); admins can trigger this from the People section.
- Asset acceptance: feature summary lists "asset acceptance confirmation"; "Unaccepted Asset Reminders" re-notify users who have not accepted their checked-out items.
- Non-unique holdings tracked as separate record classes: licenses (with seats, checkout per seat), accessories, consumables (checkout quantities), components.
- Supporting machinery observed: CSV import for assets/models/categories/locations/suppliers/manufacturers; custom fields/fieldsets; barcodes & asset label printing; depreciation types; activity report API; "multi-tenancy (ish)" — super-admins can restrict which assets non-super-admins see (company scoping); soft-deleted users can be restored; web-based, self-hosted (LAMP/Docker).

### Asset Panda (evidence layer A for its own product — Tier-2)

- Positioning: "asset intelligence platform"; central claim "Six connected jobs. One asset record."
- Record: "Asset details, photos, serial numbers, locations, users, costs, and warranties. One searchable record."
- Custody loop: "Assignments, checkouts, transfers, returns, and chain-of-custody history"; UrsaAI "watches every scan, transfer, and check-out, then keeps the record current."
- Mobile: "Mobile barcode and QR scanning to capture movements, inspections, and updates in real time. Warehouse, office, or job site."
- Inspections: checklists, condition photos, signatures, results logged against the asset.
- Lifecycle: "Track assets from deployment to retirement… deployment, maintenance, inspections, repairs, and disposal. The full lifecycle."
- Reporting: "Compliance, audit, maintenance, depreciation, and inventory reports"; "Audit readiness — full histories, documentation, and reports."
- Solutions list spans: asset tracking, inventory management (stock), IT asset management, fixed asset management, barcode tracking, mobile auditing, reservation management, maintenance management, facilities, inspections, repair tracking, calibration, equipment/tool/fleet tracking, lifecycle management, leased equipment tracking.
- Vertical editions: local government, public works, fire ("apparatus and gear mission-ready"), police ("issued equipment, assignments, and custody"), K-12/higher-ed device programs, construction, healthcare, energy/utilities.
- Sells "Asset Tags & Labels" (durable labels) as a companion product; customizable fields/workflows/reports; mobile apps.

### EZO / EZOfficeInventory (evidence layer A for its own product — Tier-2)

- Positioning: "Enterprise Asset Management Software & CMMS" — "Every Asset. Right Hands. Right Time. Right State."
- Four-part loop: **Track** ("See every asset across every site – checked out, in transit, under maintenance, or available"); **Move** ("Request, approve, dispatch, and confirm receipt with a full custody chain… self serve equipment portal… multi-tier approvals"); **Maintain** ("Schedule preventive maintenance, enforce checklists, and convert field reports into work orders… hold back equipment that is unsafe, damaged, or due for service"); **Control** ("Every checkout, return, transfer, and repair tied to the asset record… complete history of any item, any time").
- Lifecycle (FAQ): "from procurement and assignment to maintenance, audits, retirement, and disposal. Each asset record can hold custody history, maintenance activity, condition updates, documents, depreciation, and service records."
- Identification: barcode/QR/RFID tracking; GPS/telematics integrations (Samsara, Trackunit, John Deere, Hapn) for field equipment.
- Requests/reservations: request portal with availability check ("without double-booking assets"), approval routing; overdue check-in escalation; status auto-updates; low-stock alerts for consumables.
- Roles: granular access — "who can view, request, check out, move, or manage items by role, location, or responsibility".
- Depreciation: "Teams can also track depreciation and asset value over time, so Finance, Operations, and Asset Managers can make better decisions about replacement, utilization, and disposal."
- Family split (official FAQ): "For deeper IT asset management, software asset management, and ITSM workflows, AssetSonar is the purpose-built ITAM platform in the EZO product family"; EZRentOut is the rental sibling; EZO CMMS the maintenance sibling.
- Consumables/bulk stock managed alongside assets ("Break the Silos Between Assets and Bulk Items") — quantity records with min levels separate from per-item asset records.

### Sortly (evidence layer A for its own product — Tier-2)

- Positioning: "Simple Inventory Management Software… manage their physical inventory, including supplies, materials, tools, and equipment" (SMB).
- Asset tracking is one use case among several: "Track tools, equipment, and other high-value assets with ease"; separate solutions for supplies/consumables, parts, raw materials, PPE, IT assets, tool/equipment tracking.
- Structure: folders by location/type; custom fields on items; high-resolution photos ("visually track each item"); in-app barcode & QR scanning; low-stock and date-based alerts; reporting/exports "for audits, budgeting, and forecasting"; real-time multi-device sync; offline-capable mobile app (claimed).
- No custody-approval chain, depreciation, or CMMS claims on the pages observed — inventory-organization is the center; demonstrates the quantity-stock pole that registry products border.

## Cross-product Comparison

| Aspect | Snipe-IT | Asset Panda | EZO | Sortly |
|---|---|---|---|---|
| Central object | asset record (tag + status label + model) | "one asset record" (details/photos/serials/locations/users/costs/warranties) | asset record bound into track/move/maintain/control | item record (folder + custom fields + photos) |
| Per-item identity | asset tag (+ serial), auto-increment tags | serial numbers; barcode labels product | barcode/QR/RFID tagging | barcode/QR scanning |
| Classification | required asset model → manufacturer/category; custom fieldsets | customizable fields | asset records across sites/types | folders + custom fields |
| State vocabulary | status labels (configurable taxonomy) + archived flag | record state + lifecycle "deployment → retirement" | checked out / in transit / under maintenance / available | item states (not detailed on observed pages) |
| Custody | checkout to user / asset / location; RTD default location | assignments, checkouts, transfers, returns + chain-of-custody history | request → approve → dispatch → confirm receipt; full custody chain | not directly observed |
| Location | locations + return-to location | locations | multi-site | folders by location |
| Acquisition/financial | purchase date/cost, order no., supplier, warranty months, depreciation types | costs, warranties, depreciation reports | procurement → disposal, depreciation tracking | price fields (not directly observed) |
| Verification | audits (last audit date, upcoming-audit alerts, audit API), acceptance confirmation, user-inventory self-report | mobile auditing, audit-ready histories | audits in lifecycle FAQ | reporting/exports "for audits" |
| Movement history | activity report API | chain-of-custody history | complete history tied to record | user histories |
| Non-unique holdings | licenses (seats) / accessories / consumables / components as separate record classes | inventory management solution | bulk inventory + low-stock alerts | quantity stock (core) |
| Maintenance depth | minor module (maintenance API) | inspection/repair solutions | CMMS work orders + PM (heavy) | none |
| Requests/reservations | requestable flag | reservation management solution | request portal + approvals + reservations | — |
| Delivery | self-hosted web app | cloud SaaS + mobile apps | cloud SaaS + mobile | cloud + mobile (offline claimed) |

Convergent observations (evidence layer B, cross-product):

1. The system is organized around **one record per individually identified item**, not quantities.
2. Each record carries a stable **organization-level identity** (asset tag / label) in addition to any manufacturer serial.
3. Each record tracks **state over time**: availability/condition status, current location, and current custodian — with movement/check-out/check-in events logged to the record (chain-of-custody / complete history).
4. Records are **classified** (model/type/category) and commonly enriched with **custom fields**.
5. **Verification loops** exist to keep the register true: audits/counts (often scan-driven), acceptance confirmation, custodian self-report.
6. The register persists past operational life: retirement/disposal **archives** records rather than erasing them.
7. Products commonly **hybridize**: quantity-tracked classes (consumables, licenses, bulk stock) live alongside per-item records.
8. Mobile scanning (barcode/QR/RFID) is the standard capture surface for movements and audits.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

An **organization-scoped register of individually identified holdings**: one durable record per item the organization holds, carrying (a) the organization's own identity for the item, (b) attribution to the organization (owned/leased/held), and (c) tracked per-item state over time — status, location, and custody — retained through retirement.

Removal tests:
- Remove per-item identity (only quantities remain) → it becomes an inventory/stock system, not a registry.
- Remove tracked per-item state (a static snapshot list) → it is no longer the operational record the type exists to provide.
- Remove organization scope/ownership → it is a personal collection tracker, not an enterprise register.
- Remove persistence through retirement → audit/custody evidence collapses.

Everything else observed is L1/L2.

### L1 — Common Mature Structure

- Record anatomy beyond the invariant: classification catalogs (models/types/categories/manufacturers), acquisition & financial fields (purchase date/cost, supplier, order no., warranty), photos/documents/notes, custom fields.
- Custody machinery: checkout/check-in to persons (also to locations or other assets), transfers, default/return-to location, chain-of-custody movement history.
- Verification machinery: asset audits/counts (scan sweeps, upcoming-audit alerts), custodian acceptance confirmation, self-report inventory.
- Lifecycle end: retire/archive/dispose with record retained.
- Identification hardware loop: barcode/QR/RFID tagging + label printing + mobile scan capture.
- Reporting/exports for finance, audit, insurance, compliance.
- Roles & scoped visibility (admin vs custodian vs requester; location/company scoping).
- Handling of non-unique holdings (consumables, licenses, accessories, bulk stock) as quantity/seat records alongside per-item records.
- Bulk onboarding (CSV import) and APIs.

### L2 — Variant / Optional Structure

- Maintenance/work-order depth (CMMS posture) — product-dependent; heavy in some, absent or minimal in others.
- Reservation/request workflows with approvals and self-service portals.
- Depreciation/accounting depth (finance-register pole vs custody pole).
- Telematics/GPS/RFID ingestion; IT discovery/agent population (ITAM pole).
- Sector editions (government chain-of-custody, education device programs, construction tool tracking, healthcare/biomed).
- Deployment posture (self-hosted open source vs cloud SaaS), offline mobile, multi-entity/company scoping, AI assistants.

### L3 — Vendor-specific (research notes only)

- Snipe-IT: asset model is mandatory; status labels as a user-configured taxonomy; user-inventory artisan CLI; "multi-tenancy (ish)" company scoping; self-hosted LAMP/Docker; asset acceptance + unaccepted-asset reminders.
- Asset Panda: UrsaAI assistant; vertical product editions (Fire/Police/Public Works/Local Government); companion asset-tags/labels product.
- EZO: Zoe AI copilot; product family split (AssetSonar = ITAM sibling, EZRentOut = rental sibling, EZO CMMS); named telematics integrations (Samsara, Trackunit, John Deere, Hapn); 14-day managed setup.
- Sortly: folder-hierarchy organization; photos-first visual model; offline app claims.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model.

## Rejected Findings

- **"The registry is a depreciation/GL system"** — rejected as defining. Depreciation appears as reporting fields (Snipe-IT, Asset Panda, EZO all mention it), but general-ledger posting remains accounting software's job; the finance-oriented fixed-asset register is a variant pole (L2), not the core.
- **"Live telemetry/location is defining"** — rejected. GPS/telematics appears only in equipment/fleet-flavored products (EZO integrations); most registries track location as recorded state, not live feeds.
- **"Maintenance/work orders are defining"** — rejected. That is the CMMS/EAM center; in registry products maintenance ranges from absent (Sortly) to a minor module (Snipe-IT) to a marketed companion (Asset Panda, EZO). EZO itself pairs "EAM & CMMS" as distinct words.
- **"Quantity stock is part of the core"** — rejected as *defining*, while noting every sampled product hybridizes quantity classes alongside per-item records; the per-item record is what makes it a registry.
- **"This is an IT type"** — rejected. IT is one population (and one sibling product family per EZO's own FAQ); the sampled products emphasize cross-domain holdings (tools, vehicles, apparatus, devices, furniture, apparatus for fire/police, biomedical).

## Boundary Findings

1. **vs Inventory Management System (§10)** — record mode: individually identified per-item records vs quantity-based stock records. Snipe-IT's official tool-type table draws exactly this line ("unique items… tracking per part" vs IMS "stock, part origin, orders, shelf life"). Sortly shows one product can serve both modes; the boundary is the record mode in use, not the vendor.
2. **vs CMDB (§14)** — a CMDB holds configuration items (any managed IT thing, including non-assets such as services/applications/documents) whose defining structure is the **relationship/dependency graph between items for service impact**; the asset registry's defining structure is the **item's own custody/status record**. IT hardware records appear in both. *Sourcing limitation: CMDB vendor documentation (ServiceNow, BMC) was unreachable this pass — this distinction is stated at conceptual level only, without product-specific claims.*
3. **vs Enterprise Asset Management / EAM (§16)** — EAM is the registry **plus maintenance/operations as the primary job** (PM programs, work orders, reliability, MRO). The registry alone knows what exists and where/with whom; EAM runs the asset through operating life. EZO demonstrates the gradient (markets itself as "EAM & CMMS" while keeping the asset record as the spine); Snipe-IT demonstrates the registry without an EAM center.
4. **vs IT Asset Management (§14)** — ITAM is the same record logic **scoped to the IT estate** with IT-specific population (discovery agents) and license/contract depth. EZO's official family split (EZO for equipment operations vs AssetSonar "purpose-built ITAM") is direct vendor evidence that these are distinct products; Asset Panda sells ITAM as one solution on the same registry platform (center-of-gravity overlap).
5. **vs Equipment Administration Platform (§10 sibling)** — expected heavy overlap: equipment administration centers on **circulation workflows** (requests, reservations, checkout queues, assignments, usage), while the registry centers on the **record system**. In sampled products the record is the spine that custody flows bind to ("every checkout… tied to the asset record" — EZO). Flagged for joint review when the sibling leaf is processed; if that pass shows circulation workflow without a durable per-item record system as the center, the two remain separable Types.
6. **vs sector asset leaves (Public/Utility/Building/Renewable Asset Management §17/19/24, Fleet Management System §18)** — sector leaves carry sector operations (grid models, telematics, lease/tenancy, route operations). The enterprise asset registry is the **cross-domain record layer**; vehicles/transformers/buildings can each appear as records here while their operating Types live elsewhere. Fleet Management System (processed 2026-09-06) keeps telematics + driver + maintenance programs as its core — compatible boundary.
7. **Naming observation** — the market label for this type is overwhelmingly "asset tracking / asset management (software)" or the accounting term "asset register"; "Enterprise Asset Registry" reads as a descriptive name for the record-system core of that market. No directory change proposed; recorded for the taxonomy owner.

### Historical / market-sample check (per §24 method)

The minimal definition was tested against older and non-software-native forms: the paper/plant **asset register** (numbered lines per item: register number, description, location, cost, custodian) and the finance **fixed-asset ledger** both satisfy L0 — identified records, organization scope, tracked per-item state (custody/location; cost) — provided the finance pole's tracked state is read as financial. Modern products therefore do not redefine the type; they digitize and mobilize it (scanning, cloud, mobile capture). The definition is not over-fitted to the current cloud-mobile generation.

## Uncertainties

- Custody/checkout semantics in Sortly were not directly observed (product pages observed are inventory-organization-centric); Sortly is used only to anchor the quantity-stock boundary.
- CMDB-side evidence is conceptual (see Sources limitation); no precise CMDB-product claims are made anywhere.
- The exact position of large EAM suites' "asset registry" modules (Maximo-class) was not verified against vendor docs this pass; the EAM boundary rests on the sampled products' own positioning.
- Whether any vendor markets a product literally named "asset registry" as a category was not confirmed; the market labels observed are "asset tracking", "asset management", "asset register" (generic term).

## Final Synthesis

An Enterprise Asset Registry is the organization's item-level system of record for what it holds: one durable, identified record per individually tracked asset, classified, carrying acquisition/financial context, and continuously reconciled with reality through custody events (checkout/transfer/return), location updates, and verification loops (audits, acceptance, self-report), until retirement — with the record retained as evidence. Around this core, mature products add identification hardware loops (tags/labels/scanning), custom classification, reporting/exports, roles, and quantity-tracked classes for non-unique holdings; maintenance depth, reservations, depreciation depth, telematics, IT discovery, and sector editions are variant postures that push a product toward CMMS/EAM, ITAM, or sector-specific Types.

The leaf is a valid, distinct Type: the market contains a substantial product class whose entire center is this record system (open-source registry software, mobile asset-tracking platforms, equipment-operations platforms with the record as spine, inventory tools serving the asset-tracking use case). It is not merely a slice of EAM/ITAM: sampled products serve organizations that need the record without the operating programs. Boundary notes for the sibling leaf (Equipment Administration Platform) and the CMDB/ITAM/EAM neighbors are recorded above.
