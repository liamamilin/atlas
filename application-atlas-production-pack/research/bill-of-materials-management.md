# Research Notes — Bill of Materials Management

Research date: **2026-09-06**
Methodology: update-v1 workflow (v1.1)

---

## Research Goal

Understand what a Bill of Materials (BOM) Management application actually is as a Type of software: what objects exist inside it, how product structure is authored, controlled, changed, and handed off; who uses it; which capabilities define the Type versus which are common mature additions; and where its boundaries sit against PLM, Engineering Change Management, Manufacturing ERP, Inventory Management, and Product Information Management.

## Initial Boundary

Hypothesis before research:

- Core use: manage the structured definition of what components make up a product, in what quantities, under revision control shared across engineering, manufacturing, and procurement.
- Users: design engineers, manufacturing/NPI engineers, purchasing/sourcing, contract manufacturers, operations.
- Nearest confusable Types: Product Lifecycle Management (broader suite), Engineering Change Management (separate directory leaf), Manufacturing ERP / Production Planning (consumes BOMs for planning), Inventory Management System (quantities on hand vs structure), PIM (commercial catalog data), Product Configuration Management (variants/options), CAD/PDM (upstream design source).
- Unknowns: whether BOM management stands as a standalone Type or collapses into PLM; how deep the EBOM/MBOM split runs across products; whether inventory/procurement are defining or optional.

## Research Questions

1. What is the central object — the BOM, the item record, or the change record? How do they relate?
2. What is the minimal BOM data structure (identity, quantity, unit of measure, reference)?
3. How does a BOM get created (CAD sync vs manual vs import) and how does it evolve (revisions, change requests/orders)?
4. What BOM views exist (multi-level, flat, costed, where-used)?
5. Who uses the system and what roles/permissions matter?
6. What rules govern change (release/revision semantics, interchangeability)?
7. How does the BOM hand off downstream (contract manufacturers, ERP, procurement)?
8. Boundary: standalone product vs PLM module vs ERP module — where does the Type live in the market?

## Representative Products

Selection rationale: market representativeness + documentation quality + different product philosophy + different customer tiers. All are BOM-centric cloud products; enterprise suites are covered as market context only (docs gated — see Source-access Limitations).

| Product | Philosophy / Position | Customer tier | Evidence quality |
|---|---|---|---|
| **OpenBOM** | cloud-native collaborative product-data platform; "catalogs + BOMs" information model; bottom-up adoption, CAD-integrated, spreadsheets-out replacement | individual engineers → SMB → enterprise | A (product + capability pages, deep) |
| **Aligni** | standalone "PLM + MRP" for electronics; BOM as operational source of truth; hardware-as-source-code analogy | SMB electronics manufacturers, EMS | A (product pages + operational documentation portal — strongest operational evidence) |
| **Duro** | hardware PLM, "programmer's PLM", API-first, GitHub-inspired change management; BOM as digital-thread foundation | hardware startups → mid-size; aerospace/defense (ITAR) | A/B (product + PLM pages; help center not fetched) |
| Arena PLM/BOM | cloud PLM with BOM entry tier (PTC) | mid-market | **unreachable** (2 transport errors) |
| Enterprise suites (Siemens Teamcenter, PTC Windchill, SAP ERP) | BOM as module inside PLM/ERP estates | enterprise | **not fetched** (gated docs) — context only |

## Sources

Fetched 2026-09-06 (Tier 2 product pages unless noted; Aligni docs portal is Tier 1 operational documentation):

- OpenBOM home — https://www.openbom.com/
- OpenBOM BOM Management capability — https://www.openbom.com/bom-management-capability
- OpenBOM Revision Control — https://www.openbom.com/revision-control
- Aligni home — https://www.aligni.com/
- Aligni BOMs and Revisions — https://www.aligni.com/product/boms-revisions/
- Aligni Documentation Portal: Mastering the BOM (Tier 1) — https://docs.aligni.com/guides/mastering-the-bom/
- Duro home — https://www.duroplm.com/ (redirects to durolabs.co)
- Duro Design PLM product page — https://durolabs.co/product-lifecycle-management/

**Source-access Limitations:**

- https://www.arena.io/ — transport error ×2 → abandoned per network rule. Arena (a pure "BOM management"-branded tier product) therefore contributes no direct evidence.
- https://en.wikipedia.org/wiki/Bill_of_materials — request timed out → abandoned. General EBOM/MBOM/indented-BOM terminology is instead grounded in the sampled products themselves (OpenBOM explicitly names "EBOM, MBOM" BOM types; multi-level vs flat views confirmed on OpenBOM and Aligni).
- Enterprise PLM/ERP suite documentation not fetched (gated/heavy). Claims about suite-embedded BOM management are kept generic and marked as inference, not direct observation.

---

## Product Observations

### Product A — OpenBOM

Observations (evidence layer A unless noted):

- Self-positioning: "cloud-native product data platform for engineering and manufacturing teams"; connects CAD, BOM, PDM, PLM, ECO, procurement, ERP workflows in one collaborative workspace.
- Defines the domain itself: "A bill of materials (BOM), or product structure, is a comprehensive set of information that describes all items, quantities and related data … describing what is needed of each to get a finished product."
- Information model: **Catalogs** (item database: "you can think of your catalogs as a database for all items you can use in your BOMs") + **BOMs** built by referencing catalog items via part number; item data propagates automatically ("adding the item … adds all of its related information").
- BOM views: switchable **single-level, multi-level, flattened** views from a dropdown; "Excel-like" grid UI.
- Revision control page articulates the discipline: three elements — **capture of changes** (what/who/when/why), **baselines** ("snapshot of a product at a specific point in time … freeze the state for manufacturing, compliance, or analysis"), **interchangeability** ("whether a newer version … can replace an older one without disrupting form, fit, or function" — determines new part number vs new revision).
- Change process: **Change Request (CR)** documents proposed modification (part update, vendor change, material substitution); approved CR links to an updated item revision; **Change Order (CO)** consolidates multiple CRs into one approval workflow. BOM Comparison tool to validate updates; change reports/export.
- Revision baselines stored as **immutable snapshots**; bottom-up and top-down revision control; "Order BOM" can be created from a released revision for purchasing.
- Terminology split (product-specific): "Version" for CAD files/documents; "Revision" for items and formal change control.
- Collaboration: real-time simultaneous multi-user editing (patented), cross-company sharing (multi-tenant, suppliers/contractors in the same workspace).
- BOM types named: **EBOM, MBOM** and other views ("Support multiple BOM types: EBOM, MBOM, etc.").
- Downstream: inventory, RFQs, POs, supplier collaboration; ERP sync (QuickBooks, Xero, NetSuite, Odoo, Dynamics, Katana MRP).
- CAD: extraction of items/BOMs from CAD assemblies; 15+ CAD systems (SolidWorks, Onshape, Fusion 360, Altium…); WIP "Design Items" for pre-release design data.
- Cost: product cost management with roll-up (customer testimonial: ingredient cost change propagates to all product recipes; roll-up to finished product).
- Where-used: repeatedly cited as a headline feature ("You just can't do a where-used operation in an Excel BOM").
- Industries served: machine design, high-tech/electronics, furniture/apparel/CPG, AEC, **food and process** (recipe-BOM use case confirmed by a chocolate manufacturer's testimonial).

### Product B — Aligni

Observations (evidence layer A; docs portal is operational documentation):

- Positioning: "cloud-based software for product lifecycle and manufacturing management"; SMB electronics focus; "Aligni is source-code management for your hardware."
- **Necessary and sufficient BOM elements** (from "Mastering the BOM" guide — a rare explicit minimal-data claim):
  1. Manufacturer + Manufacturer P/N (uniquely identifies the item in the world of components; MPN treated as a SKU of identical **form, fit, function, or formulation**)
  2. Quantity and Units (each, milliliters, centimeters…)
  3. Reference Designators (where parts go; unique within the BOM; electronics C1/C2/R1 convention; mechanical drawing callouts analogous)
  - "If any of these components is missing from the BOM, it is incomplete." Everything else (pricing, suppliers, lead time, datasheets, alternates) is optional and lives in the **item master**, combined with the BOM when shared with vendors.
- Item master discipline: database records avoid duplication; BOMs link to item records; MPN = SKU; new SKU required when form/fit/function/formulation changes.
- BOM features: multi-level BOM ("see what components go into a build – even in its sub-assemblies"); **where-used** visibility ("puts every component's footprint at your fingertips"); **BOM Compare** tool ("highlights changes item by item" between versions, used for audits and design reviews); **cost sheet** view (drill-down hierarchical costing, volume price breaks, attrition, excess material).
- Revisions: "Every change to a BOM is documented — with the what, when, and why"; "See who made the change and when it was released"; discussions and decision notes attached to revisions.
- Change management: built-in Engineering Change Management (ECM) — change request and change order iterations integrated with BOMs; change audits; Form/Fit/Function guide.
- Alternates: substitute components linked to specified parts with pricing/availability; approved alternates used when parts are out; vendor part numbers linked to a single canonical part record (packaging-suffix problem: one part, many vendor PNs).
- Handoff: **Vaults** — secure sharing of BOMs + drawings with outside vendors/customers, pulling live data from the item master ("no risky file exports or outdated PDFs"), audit logs, role-based access, change notifications.
- Surrounding operational modules (context): inventory (on-hand visible before sourcing), procurement (RFQ/PO from BOMs and shortages), builds (production runs against a BOM revision, allocations, deviations), material planning (MRP), quality control.
- Roles surfaced: product engineer, buyer/planner, project manager, inventory manager, purchase manager, admin.
- Industries: electronics manufacturing services, contract manufacturing, medical devices.

### Product C — Duro

Observations (evidence layer A on positioning/roles, B on mechanism detail):

- Positioning: "Duro Design PLM is AI-native, API-first … Centralize part data, manage change orders, and build a true digital thread"; "Duro makes your BOM the foundation of a complete digital thread."
- Engineering role: "combine BOMs from mechanical, electrical, industrial, and manufacturing disciplines"; release and organize component data from CAD via native integrations (SolidWorks, Onshape, Altium 365).
- Change management: "tailored change order workflows, approval templates, Slack alerts"; "GitHub-inspired change management" with "approvals, impact analysis, and automation"; compare any two revisions; view how often a component/product has been used (where-used analog).
- Manufacturing role: "syncs directly with your MES and ERP systems, so you can be confident that your manufacturing teams have the latest **released revisions**."
- Operations role: "Check the status of any BOM at any time. Lead time roll-ups … understand when changes are in process."
- Supply chain role: sourcing module with real-time distributor data (cost/availability) to "adapt designs earlier in development."
- Error class targeted: "building off of the wrong design revisions" named as the expensive engineering-manufacturing miscommunication.
- Cost: "View cost roll-ups, revision changes, and product status at a glance."
- Governance: customer quote (launch-vehicle engineer): "Without being able to define a **baseline** or manage changes to our products … we wouldn't have the confidence in our design to seek launch permission."
- Configurability: fields/workflows/validation rules via low-code/YAML; GraphQL API; embedded 3D viewers; Slack/Jira alerts.
- Compliance/security: SOC 2, ITAR-compliant cloud, SSO/2FA, deployment options multi-tenant → dedicated → self-hosted.
- Industries: aerospace & defense, industrial automation, computer infrastructure, energy management. Customer tier: startups/scale-ups (space, robotics).
- Note: Duro brands itself PLM, not BOM management — but the researched surface shows the same BOM-centric core (part data + BOM + revisions + change orders + where-used + roll-ups).

## Cross-product Comparison

| Finding | OpenBOM | Aligni | Duro | Evidence layer | Level |
|---|---|---|---|---|---|
| Item/part records as identified database objects (item master / catalogs / part libraries) | Catalogs | Part item management | "centralize part data" | B | core |
| BOM = product structure referencing item records × quantities | yes | yes (necessary element) | yes | B | **core** |
| Quantity + unit of measure on BOM lines | yes | yes (explicit) | yes | B | **core** |
| Released revisions / baselines; current definition unambiguous | immutable revision snapshots | revisions w/ release + who/when/why | released revisions, baselines | B | **core** |
| Change recorded (what/who/when/why) + change workflow (request → order → release) | CR/CO | CR/CO (ECM) | change orders, approval templates | B | core-adjacent (L1 workflow machinery; the *controlled change itself* is core) |
| Multi-level (indented) BOM hierarchy | yes | yes | implied (assembly views) | B | L1 |
| Flat / rolled-up BOM views | yes (dropdown) | cost sheet drill-down | cost roll-ups | B | L1 |
| Where-used | headline feature | headline feature | usage frequency view | B | L1 |
| BOM compare between revisions | BOM Comparison tool | BOM Compare | compare any two revisions | B | L1 |
| CAD integration / BOM extraction | 15+ CAD systems | Altium connector; partlist import | native CAD integrations | B | L1 |
| Change-request/change-order approval workflow | yes | yes | yes | B | L1 |
| Cost roll-up to top level | yes | yes (cost sheet) | yes | B | L1 |
| Handoff to contract manufacturers/suppliers | share workspace w/ suppliers | Vaults + vendor portal | sourcing/distributor data | B | L1 |
| Downstream sync to ERP / procurement / production | ERP sync (NetSuite etc.) | MRP native (builds, POs) | MES/ERP sync | B | L1 |
| Manufacturer part number (MPN) as world identity; internal part number separate | yes (MPN + supplier PN columns) | yes (MPN = SKU; vendor PNs linked) | distributor data | B | L1 (electronics-strong; identity concept general) |
| Reference designators (where parts go) | not directly observed in fetched pages | explicit, necessary | not directly observed | A (single product) | L1/L2 (strong in electronics) |
| Alternates / substitutes / approved vendors | substitution in CR context | first-class alternates | alternative suppliers via sourcing | B | L1/L2 |
| Inventory on-hand linked to BOM | yes (inventory module) | yes (on-hand before sourcing) | not core (sourcing only) | B (2/3) | L2 |
| Procurement / RFQ / PO | yes | yes | sourcing only | B (2/3) | L2 |
| EBOM / MBOM formal multi-view | explicit ("EBOM, MBOM, etc.") | implicit (engineering + production builds) | implied (mech/elec/manu BOMs combined) | B/C | L2 |
| Production build execution vs BOM | production planning capability | builds module (allocate/reserve/finalize) | MES integration only | B | L2 |
| MRP / material planning | production planning | MRP (shortage report, demand, safety stock) | lead-time roll-ups | B | L2 |
| Compliance data (RoHS-style) / regulated industries | compliance management capability | medical devices vertical | ITAR, aerospace | B | L2 |
| Food/recipe (formulation) BOM | explicit (food & process vertical, testimonial) | chemical industry named in docs intro | — | A (single product feature, cross-industry concept) | L2 (industry overlay) |
| Real-time multi-user collaborative editing | patented, headline | discussions, not real-time co-editing emphasized | not emphasized | A (single product) | L2/vendor-posture |
| Deployment: multi-tenant cloud → dedicated → self-hosted; ITAR | multi-tenant SaaS | cloud SaaS | multi-tenant/dedicated/ITAR/self-hosted | B | L2 |

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product stops being recognizable as BOM management:

1. **Identified item records** — the referenced things (parts, materials, assemblies) exist as individually addressable records with part-number identity.
2. **Product-structure record** — for a parent product/assembly, a structured record of which items go into it and in what quantities (unit of measure).
3. **Controlled current definition** — the structure is versioned: a released/released-current definition exists, prior versions remain accessible, and changes to it are recorded (what/who/when/why).

Remove #1 → generic list manager. Remove #2 → item catalog / parts database, not a BOM. Remove #3 → a static parts list (spreadsheet), not *management*. All three are present in every sampled product and are historically present (MRP-era BOMs with engineering change orders; drawing revision blocks) — the definition survives the historical check.

### Level 1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not definitional:

- item master with rich attributes (descriptions, manufacturer/MPN, suppliers, lifecycle state, custom parameters, attachments)
- multi-level (indented) assembly hierarchy; flat and rolled-up views of the same structure
- where-used (reverse traversal across all BOMs)
- BOM comparison between revisions (item-by-item diff)
- BOM creation machinery: CAD extraction/sync, spreadsheet import, manual authoring against the item master
- change workflow: change request → change order → approval → released revision, with audit trail and notifications
- cost roll-up (line cost × quantity aggregated through levels)
- sharing/handoff to contract manufacturers and suppliers (exports, vaults, portals; controlled, current-version guaranteed)
- downstream synchronization to ERP/procurement/production (BOM as source of truth for purchasing and build)
- roles/permissions: who may edit, who may release, who consumes read-only
- alternate/substitute parts and approved-manufacturer relationships
- discussions/notes attached to BOMs and changes (decision context kept with the record)

### Level 2 — Variant / Optional Structure

Depends on segment, industry, deployment, business model:

- formal EBOM/MBOM (as-designed / as-built / as-maintained) duality and BOM transformation
- inventory on-hand linkage; procurement (RFQ/PO); production build execution; MRP/material planning
- effectivity (date/serial/lot) on BOM lines
- configurable/product-variant BOMs (options, 150%-BOMs)
- compliance data sets (substance/restricted-material; regulatory industries)
- industry overlays: electronics (reference designators, distributor data, packaging variants), process/formulation (recipes, percentages, intermediates), AEC takeoff-style structures
- PDM/CAD-file vaulting bundled alongside BOM
- deployment/security posture: multi-tenant SaaS, dedicated, ITAR, self-hosted
- real-time co-editing vs formal workflow-first collaboration posture
- AI assistance (part selection, change analysis, natural-language rules)

### Level 3 — Vendor-specific (research notes only)

- OpenBOM: catalogs-as-database model; "xBOM" branding; Product Memory platform vision; patented simultaneous editing; Design Items (WIP) layer; version-vs-revision terminology split; Order BOM from released revision; AECBOM spin-off.
- Aligni: DiscussAnything™; TimeWarp™ (lead-time navigation); Vaults; ActiveQuote (RFQ); Part Cart; Octopart integration; packaging-suffix MPN resolution (TPS2552DBVT/R worked example); "source-code management for your hardware" analogy; MRP-as-ERP positioning.
- Duro: "Programmer's PLM"; YAML/natural-language validation rules; GitHub-inspired change management; GraphQL API-first; Slack/Jira native alerts; embedded 3D viewers; ITAR multi-tenant.

## Boundary Findings

- **vs Product Lifecycle Management (PLM)**: BOM management is the structural spine of PLM, and the market gravitates toward PLM-branded packaging (Duro self-labels PLM; OpenBOM lists a PLM capability; Aligni pairs PLM+MRP). The BOM-management core remains extractable and independently sellable (OpenBOM, Aligni, and the formerly distinct "Arena BOM" tier). Boundary criterion: center of gravity — if the product's estate expands to CAD vaulting/file management, requirements, quality, portfolio workflows as first-class objects, it is PLM; if the item/BOM/revision structure is the managed world (with everything else as adjunct modules), it is BOM management. **Recommendation: keep the directory leaf; record the packaging-gradient.**
- **vs Engineering Change Management (separate leaf)**: every sampled BOM product embeds a change workflow (CR/CO/approval) scoped to items, BOMs, and revisions. The separate leaf is defensible only for change-centered products whose managed objects span documents/files/etc. across engineering. Potential alias risk if the ECM leaf is defined broadly. **Flagged for STATUS.**
- **vs Manufacturing ERP / Production Planning / MRP**: ERP-embedded BOM modules consume the structure for planning, costing, and execution; BOM management owns the authoring/definition/control side and hands off (sync/export). Aligni's "MRP as ERP" SMB positioning shows the boundary blurring at the low end (the BOM system grows planning features), and ERP BOM modules show it blurring from the other side. Direction of truth-flow (engineering definition → business consumption) is the discriminator.
- **vs Inventory Management System**: inventory is about quantities on hand in locations; BOM management is about structure. Several products bundle inventory (OpenBOM, Aligni) — optional module, not defining.
- **vs Product Information Management (PIM)**: no confusion risk found — PIM manages commercial/catalog content for selling channels; BOM management manages engineering/manufacturing structure. Distinct identity vocabularies (MPN vs SKU-as-product-offering).
- **vs Product Configuration Management**: configurable BOMs (options/variants) appear as L2 here; configuration-centered tools justify the separate leaf.
- **vs CAD/PDM**: upstream source of EBOM data and design files. PDM manages CAD documents/check-in-out; BOM management manages the structural definition and its change history. OpenBOM's version(CAD) vs revision(item/BOM) terminology split explicitly encodes this boundary.
- **"去掉什么就变成另一个 Type" 判据**: remove controlled change/revision discipline → parts catalog or static list, not this Type; shift center to CAD-file vaulting → PDM; shift to full lifecycle estate → PLM; shift to consuming structures for planning/production execution → Manufacturing ERP/Production Planning; shift structure content to commercial selling data → PIM.

## Uncertainties

- Enterprise-suite BOM management (Teamcenter/Windchill/SAP) not directly researched (gated docs). Their structures (multi-view BOM, effectivity, plant-level MBOM) are believed to fit the same canonical model, but this is **canonical inference (C)**, not direct observation.
- EBOM/MBOM transformation depth varies widely; only OpenBOM among sampled products explicitly names multiple BOM types. The formal multi-view discipline may be more characteristic of suite-grade products — L2 assignment is conservative.
- Reference designators as a "necessary" BOM element come from one product's documentation (electronics-centric). For mechanical/process industries the analog ("where the part goes" instance callout) takes other forms (position numbers, BOM structure). Kept at L1/L2 with electronics emphasis.
- Effectivity dates, 150%/configurable BOMs: known industry concepts but **not directly observed** in the fetched sample — deliberately not asserted as standard in the final document.
- Historical check performed conceptually (MRP-era BOM + ECN, drawing revision blocks fit the L0); no archival product documentation was fetched.

## Final Synthesis

A Bill of Materials Management application is the system of record for **what a product is made of, controlled over time**. Its world consists of identified item records; product-structure records binding parent products to component items with quantities; and a versioned, change-controlled lifecycle that keeps a released "current definition" of each product with full history. Around that core, mature products add the machinery that makes the structure usable across an organization: multi-level/flat/where-used views, CAD and spreadsheet intake, change requests/orders with approvals, cost roll-ups, revision comparison, supplier/contract-manufacturer handoff, and synchronization into ERP, procurement, and production. Inventory, MRP, procurement, compliance, and configuration are optional satellites whose presence varies by segment; EBOM/MBOM formalization varies by manufacturing depth. The Type's boundary is drawn by its center of gravity: the structural definition and its controlled evolution — not the CAD files upstream, not the planning/execution downstream, not the commercial catalog data of PIM, and not the full PLM estate around it.
