# Research Notes — IT Asset Management

## Research Goal

Understand, from real products, what an IT Asset Management (ITAM) application is: what lives inside it, what its defining structure is, how the asset lifecycle actually flows, and how it differs from the neighboring types it converges with (CMDB, Endpoint Management/UEM, Enterprise Asset Registry, SaaS Management, EAM).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: keep an authoritative inventory of the organization's IT assets (hardware, software licenses) and manage them across their lifecycle — procure, deploy, maintain, retire.
- Primary users: IT asset managers, IT operations, procurement/finance, auditors.
- Nearest neighbors: CMDB (§14, processed), Endpoint Management/UEM (§14, processed), Enterprise Asset Registry (§10, processed), SaaS Management (§14, unprocessed), EAM/CMMS (§16, processed), Inventory Management System (§10).
- Known unknowns: is discovery definitional? Is the financial/commercial layer definitional or just common? Where exactly is the CMDB seam? Does software/license tracking belong in the core?

Pre-hung counterparty flags to discharge (from STATUS.md):

1. **CMDB pass (2026-09-07)**: "sharpest seam — asset/financial-lifecycle object vs CI/dependency object; remove relationships+service context → asset register"; recommended joint review when ITAM is processed; suggested recording the remove-relationships test as the canonical seam.
2. **UEM pass (2026-09-08)**: "UEM device records carry asset-like fields (asset number/ownership/purchasing data) and inventory, but the financial/contract/procurement lifecycle is ITAM" — flag expecting confirmation from this side.

## Research Questions

1. What is an "IT asset" in these systems — which classes of things get records?
2. What is the identity model (asset tag, serial, license key)?
3. What is the lifecycle — which states, which transitions, and what ends it?
4. What financial/commercial data lives on the record (cost, depreciation, warranty, contract, PO)?
5. What license/entitlement machinery exists (seats, reconciliation, compliance)?
6. How does the record population work — discovery, import, manual, purchase flow — and is any one method definitional?
7. What is the custody/assignment model (checkout, deployment to person/location)?
8. What verification machinery exists (audits, reconciliation)?
9. What interfaces does an asset manager actually operate?
10. What are the exact seams vs CMDB / UEM / Enterprise Asset Registry / SaaS Management / fixed-asset accounting?

## Representative Products

Chosen for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Shape / philosophy | Tier |
|---|---|---|
| Snipe-IT | free open-source, self-hosted, pure-play ITAM; custody/inventory-first | SMB/mid-market pole |
| ManageEngine AssetExplorer | dedicated ITAM product from an ITSM-suite vendor; lifecycle + license + PO/contract machinery | mid-market pole |
| Device42 | discovery-first platform packaging ITAM + CMDB + DCIM; data-center heritage | mid/enterprise pole |
| Freshservice | cloud ITSM suite with ITAM; CMDB-linked, AI-era positioning | cloud/SaaS pole |

Not directly sampled (docs gated or oversized; used as market context only, no claims rest on them): ServiceNow ITAM/SAM, Flexera, Ivanti, Lansweeper. Evidence for the enterprise pole comes from sampled vendors' own integration/partner listings (e.g., Device42 lists ServiceNow/JSM integrations).

## Sources

All fetched 2026-09-08.

- Snipe-IT official documentation (readme.io, Tier 1):
  - Overview: https://snipe-it.readme.io/docs/overview
  - Documentation index: https://snipe-it.readme.io/llms.txt
  - Depreciation Types: https://snipe-it.readme.io/docs/depreciation-types
  - Asset Models: https://snipe-it.readme.io/docs/asset-models
  - API reference index (license seats endpoints etc.): https://snipe-it.readme.io/llms.txt (API Reference section)
- ManageEngine AssetExplorer official product page (Tier 2): https://www.manageengine.com/products/asset-explorer/
- ManageEngine ServiceDesk Plus asset-scanning feature page (Tier 2): https://www.manageengine.com/products/service-desk/it-asset-management.html
- Device42 official site (Tier 2): https://www.device42.com/features/it-asset-management/ and https://www.device42.com/ (nav/positioning; best-practices content served on the ITAM page)
- Freshservice ITAM official product page (Tier 2): https://www.freshservice.com/it-asset-management

Source-access limitations:

- ManageEngine admin-guide/help docs are JS-rendered; only product pages were reachable. AssetExplorer operational details beyond the product page are NOT asserted.
- Freshservice support portal articles unreachable (404 on the attempted article URL); product page only. No Freshservice operational/field-level claims asserted.
- Device42 docs (docs.device42.com) not fetched; claims rest on the vendor's own ITAM/best-practices pages (marketing+educational hybrid — treated as strong Tier 2, weaker than help-center Tier 1).
- Snipe-IT is the only sample with directly accessed operational (Tier 1) documentation; its specifics are kept product-specific in this file.

## Product A — Snipe-IT (evidence layer: A, Tier-1 docs)

Self-description: "a free, open source IT asset management system. Features include management of assets, users, licenses, accessories, consumables and components… asset acceptance confirmation."

Key observations:

- **Asset = anything important enough to warrant an asset tag**; "laptops, desktops, mobile phones, tablets, etc are common items". Every asset must have a unique asset tag, often used with printed asset labels; serial number may serve as tag; auto-increment tags optional. (A)
- **Custody model**: checkin/checkout are "two primary concepts". Checkout marks the asset as in possession of someone else; prevents "double-booking" (cannot be checked out to another person until checked back in). Assets can be checked out to people (recommended), locations, or other assets. Check-in happens when an employee leaves or an asset needs repair; the assigner then chooses a status. (A)
- **Status lifecycle**: status labels carry one of four state characteristics — Undeployable / Deployable / Archived / Pending; "Pending" = not yet assignable but eventually (e.g., re-imaging); a Deployable asset once assigned takes the meta status "Deployed"; Archived assets show only in the Archived view. (A)
- **Class model**: assets (tagged items) vs accessories (untagged multiples, checked out to people/assets) vs components (RAM, drives — checked out to assets) vs consumables (used up, checked out to people, never returned). (A)
- **Type/instance structure**: every asset needs an asset model (make/model of a laptop, etc.); models carry attributes inherited by instances — depreciation type, end of life, MAC-address fields; model images/files propagate to asset pages. (A)
- **Financial machinery**: three depreciation models (linear/straight-line computed from cost, floor, months; half-year convention variants tied to fiscal years) — asset current value computed from purchase cost. (A)
- **Licenses as assets**: licenses can be checked out (to users); API exposes per-license **seats** with per-seat checkin/checkout to user or asset. (A — API reference endpoints + overview text)
- **Suppliers** as a first-class record class (importer covers suppliers, manufacturers). (A — importer list)
- **Audits**: per-asset audit API endpoint; "Upcoming Audits" email alerts; audit due dates. (A — API + docs index)
- **Requests & acceptance**: assets and models can be marked requestable (end users request them); unaccepted-asset reminders; users accept EULAs for checked-out items (asset acceptance confirmation). (A)
- **Identity/access**: LDAP/AD sync, SAML SSO, SCIM provisioning, 2FA — admin-side machinery, not asset logic. (A)
- Notably: **no native network discovery** — population is via importers (CSV), manual entry, or API. The docs index contains no discovery/scanning section. (A — absence)

## Product B — ManageEngine AssetExplorer (evidence layer: A for product-page claims)

Self-description: "an IT asset management (ITAM) platform… Its out-of-the-box capabilities include hardware and software asset discovery and inventory management, custom workflows to automate life cycles, purchase and vendor management, and a CMDB."

Key observations:

- Positioning line: "Gain complete visibility and control over your IT assets, **from purchase to expiration**." (A)
- Lifecycle: "Govern every state of an asset, **from request initiation to asset disposal**"; "visual asset life cycles — a drag-and-drop canvas to design asset life cycles and ITAM processes; unique life cycles and workflows for each product type". (A)
- Discovery & inventory: agent-based and agentless discovery; barcode, QR code, RFID scanner support; real-time inventorying with automated asset scans. (A)
- Software management: "robust software inventorying **with reconciliation**", usage monitoring across installations, tracking unauthorized/prohibited software. (A)
- License management: "always-on **license compliance statuses**"; auto-allocate, upgrade, downgrade licenses; supports suites and service packs. (A)
- Purchase & contract machinery: "a purpose-built **purchase order and contract management system**"; cost center and general-ledger code support on POs; parent/child contracts. (A)
- CMDB adjacency: CMDB ships inside the product ("single source of truth for enterprise-wide configuration items"; business views of services and dependencies). (A)
- Edition matrix (free/trial/pro) lists the module set: IT asset inventory management, CMDB, software license management, software asset management, purchase order management, contract management, asset life cycle management, reports, asset tracking. (A)
- Integrations: Endpoint Central (endpoint management), Microsoft 365 subscription management, Zoho Analytics, SolarWinds, Lansweeper, Zapier. (A)

## Product C — Device42 (evidence layer: A for its own pages' claims; marketing-hybrid source)

Self-description: ITAM as "Most complete hybrid IT discovery, visibility and management"; the platform bundles ITAM + CMDB + DCIM + IPAM + software license management.

Key observations:

- **Industry definition given by the vendor**: "IT asset management (ITAM) is a methodology to **inventory and manage the quantity, usage, and financial value of IT assets across their lifecycles**, associating costs, and risks to each asset to determine their business value." And: "An ITAM strategy empowers you to manage the **financial, inventory, contractual, and risk management** responsibilities of the lifecycle of assets." (A, vendor-authored)
- **Asset classes**: "two main types of IT asset management solutions: software and hardware"; facilities assets (desks, chairs, vehicles, buildings) "usually fall in the facilities asset management space and do not involve IT" — explicit exclusion of non-IT estates. (A)
- **Lifecycle stages enumerated**: Planning → (purchasing) → Deployment → Service → Disposal — "IT asset lifecycle management is the practice of understanding the stages in the life of an asset and the effective planning, purchasing, utilization, and retirement of that asset." (A)
- **Financial framing**: CapEx depreciation as tax-deductible ("if there is no documented, up-to-date inventory of IT assets, your company might be missing out on potential tax savings"); Finance team uses hardware data "for amortization". (A)
- **Asset tracking vs ITAM**: asset tracking = utilization, location, in-service state; details "SKUs, purchase date, cost, technical specifications, and end of life/end of sale (EOL/EOS)". Spreadsheets named as the failing manual predecessor ("data quickly becomes obsolete as soon as the spreadsheet is done"). (A)
- **Contracts & warranty**: "Centrally manage all IT contract information for devices, hardware, and software assets… Track the entire lifecycle of your IP- and non-IP-based assets **from purchase to their day of decommissioning**"; automated **warranty lookups** from vendor APIs (Dell, IBM, Lenovo) writing warranty info into the database. (A)
- **License compliance**: "automatically discover licenses and then **compare current discovered count to purchased count**". (A)
- **Identity**: print customized QR codes, auto-assign customizable **asset numbers**; mobile-portal asset audits ("ensure that asset audits are both fast and accurate"). (A)
- **Custom asset types** (predefined or custom); **relationships between assets** tracked and visualized (CMDB-style); discovery-first positioning: "the most important aspect of an ITAM solution is the accuracy of information captured and breadth and depth of technology discovery". (A)
- **Inventory-tracking distinction**: "Unlike IT asset tracking, the goal of inventory tracking is the sale of assets and the quantity needed for replenishment" — explicit boundary vs retail/stock inventory. (A)
- **Estate answers**: lease renewal negotiation, customer (third-party) assets hosted on site, capacity planning, security/DR preparedness, audit/compliance. (A)

## Product D — Freshservice (evidence layer: A for product-page claims)

Self-description: "Freshservice ITAM gives the visibility and context for improved decisions…"; "Automate real time tracking across **hardware, software, and cloud tools** in an auto-updating CMDB."

Key observations:

- ITAM capabilities listed: **Automated Discovery** (on-prem, cloud, hybrid — "audit-ready inventory"), **Software License Management** ("complete, accurate profile of software to control costs, stay compliant, maximize software ROI"), **Dependency Mapping**, **DCIM**, **IPAM**, **Resource Utilization** (CPU/memory/IO to eliminate idle capacity). (A)
- Positioning: "Traditional ITAM tracks assets. Freshservice ITAM adds the context…" — CMDB/service-context adjacency claimed as the differentiator. (A)
- Value framing: cost optimization ("see software licenses clearly to cut out waste"), audit-readiness, change confidence via dependency mapping. (A)
- Customer testimonial: "every asset is tracked in Freshservice, with asset management built into every service request… centralized hierarchy to pinpoint asset failure impact" — the ITSM-suite consumption pattern (assets feed tickets). (A)
- AI-era module: Freddy Copilot surfaces assets related to incidents; AI-generated audit summaries "capture associated assets, related incidents". (A)

## Cross-product Comparison

| Dimension | Snipe-IT | AssetExplorer | Device42 | Freshservice | Evidence layer |
|---|---|---|---|---|---|
| Identified asset records w/ unique tag/number | A (unique asset tag) | A (barcode/QR/RFID) | A (QR, asset numbers) | A (tracked assets) | Core (A×4) |
| Hardware + software/license classes | A | A | A | A | Core (A×4) |
| Commercial facts on record (cost, supplier/vendor, warranty/contract/license terms) | A (cost, supplier, warranty fields on model/asset) | A (POs, contracts, GL codes) | A (purchase date, cost, contracts, warranty lookups) | A (license cost/compliance framing) | Core (A×4) |
| Lifecycle states + recorded transitions to disposal | A (status labels: deployable/undeployable/pending/archived; deployed meta-state) | A (request initiation → disposal; designed lifecycles) | A (planning → purchasing → deployment → service → disposal) | A (tracking across lifecycle implied; audit-ready inventory) | Core (A×4; state vocabulary differs) |
| Financial value machinery (depreciation / current value) | A (3 depreciation models) | indirect (GL/cost-center on POs) | A-claim (depreciation/amortization framing) | not observed | Common (2.5/4) — NOT definitional |
| License entitlement vs deployment reconciliation | A (license seats per-seat checkout) | A (license compliance statuses; software reconciliation) | A (discovered vs purchased count) | A (license profile, compliance) | Core-adjacent (A×4) — the software-side engine |
| Contract/warranty management | A (warranty fields; supplier records) | A (PO + contract system; parent/child contracts) | A (contract management; warranty auto-lookup) | not observed on page | Common (3/4) |
| Discovery (agent/agentless network scan) | **absent** (A — absence) | A | A (defining positioning) | A | Common (3/4) — NOT definitional |
| Audits / verification loops | A (audit endpoint, upcoming-audit alerts) | A (audit-ready claims; barcode scanning) | A (mobile asset audits) | A ("audit-ready inventory") | Common (A×4) |
| Custody checkout (to person) | A (defining mechanic) | A (auto-assign to users; acknowledgements) | A (who is responsible/using) | A (asset per request) | Common (A×4; center of gravity differs) |
| CMDB / dependency mapping adjacency | absent | A (CMDB module) | A (CMDB + ADM) | A (auto-updating CMDB, dependency mapping) | Variant adjacency (3/4) |
| Purchase order / vendor management | A (suppliers; importer) | A (PO system, vendor management) | A (track purchases; vendors) | not observed | Common (3/4) |
| End-user requests / acceptance | A (requestable assets; EULA acceptance) | A (acknowledgements, auto-assign) | not observed | A (AI agent raises/fulfills requests) | Common (3/4) |
| Barcode/QR/RFID labels | A (asset labels, barcodes) | A | A (QR) | not observed | Common (3/4) |
| ITSM/ticket linkage | not native | A (via suite) | A (integrations: ServiceNow/JSM/Zendesk) | A (assets feed incidents) | Variant adjacency |
| Cloud/SaaS subscriptions as tracked assets | absent (hardware-centered + licenses) | A (Microsoft 365 subscriptions) | A (cloud discovery: AWS/Azure) | A ("hardware, software, and cloud tools") | Variant breadth (3/4) |

## Abstraction Hierarchy

### Level 0 — Defining Invariant (minimal; jointly-held)

Three jointly-held structures. Removing any one makes the product stop being ITAM:

1. **The IT asset inventory of record** — individually identified (asset tag/number or license identity), classified records of the organization's IT assets, deliberately spanning BOTH physical hardware (serial-numbered devices) AND non-physical classes (software licenses/entitlements; in modern products also cloud subscriptions/services). Each record carries its commercial facts: acquisition/purchase cost, source (supplier/vendor), and its coverage terms (warranty, maintenance contract, license terms). Domain binding: IT estate only — Device42 explicitly excludes facilities assets. Remove → a generic holding register or a mere device list.
2. **The tracked lifecycle of record** — every asset is held in an explicit lifecycle state and its transitions are recorded, from acquisition (request/purchase/receive) through deployment and in-use maintenance to retirement/disposal, and the record survives disposal (archived/history). The record — not tribal knowledge or a spreadsheet — is the authoritative answer to "what do we own, where/with whom is it, what state is it in, when does it expire". Remove → spreadsheets or one-shot trackers; no system of record.
3. **The estate's commercial reconciliation and reporting** — the system is where the organization's money-and-compliance story about the IT estate is computed and answered from the records: license/entitlement position vs actual deployment, financial value of the estate over time, contract/warranty coverage and upcoming expirations, spend and audit reporting. Remove → an asset register without financial/commercial agency (the Enterprise Asset Registry / asset-tracking territory).

Jointly-held is load-bearing:

- 1 alone = IT device inventory / enterprise asset registry (no lifecycle authority, no financial engine)
- 2 without 1 = workflow machinery with nothing to manage
- 3 without 1+2 = fixed-asset accounting ledger / license-count spreadsheet (records without lifecycle custody of the estate)
- 1+3 without 2 = a static register with financial fields (no live lifecycle)
- 1+2 without 3 = pure asset tracking / custody registry (§10 Enterprise Asset Registry shape)

### Level 1 — Common Mature Structure (very common; not definitional)

- Discovery (agent-based/agentless network scans, cloud discovery connectors) as a record-population method — 3/4 samples; Snipe-IT, the reference pure-play, has none (A — absence)
- Audit/verification loops (scheduled audits, audit-due alerts, mobile audit scanning)
- Custody checkout/check-in with exclusivity (one holder at a time) and end-user acceptance confirmations
- Type/model layer carrying defaults inherited by instances (depreciation profile, EOL)
- Contract & purchase-order machinery (POs, vendors/suppliers, parent/child contracts, cost centers)
- Requestable-asset catalogs and self-service request flows
- Barcode/QR/RFID labeling and mobile scanning surfaces
- Reporting/dashboards (compliance, depreciation, expirations, estate composition)
- Depreciation/current-value computation (A in 1, strong claims in 2 others — common but not universal in the sample)
- Integration/export to ITSM, finance, and endpoint tools; REST APIs

### Level 2 — Variant / Optional Structure

- Product shape: standalone pure-play (Snipe-IT), ITSM-suite module (AssetExplorer within ServiceDesk Plus family, Freshservice), discovery-first platform (Device42)
- Deployment: open-source self-hosted, on-premises, cloud SaaS
- CMDB/dependency-mapping adjacency: bundled CMDB, service views, application dependency mapping (3/4) — an adjacency, not the Type
- Estate breadth: cloud subscriptions, IPAM, DCIM, resource utilization, certificates — platform adjacencies varying by vendor
- SAM depth: usage monitoring, unauthorized-software detection, reconciliation engines (deep pole vs seats-only pole)
- Third-party/customer assets hosted on site (Device42 scenario)
- AI-era features: AI copilots summarizing asset context, AI-fulfilled software requests

### Level 3 — Vendor-specific (kept out of the final document)

- Snipe-IT: four status-label meta-types with "Deployed" meta-state; EULA acceptance flow; "multi-tenancy (ish)" company scoping; depreciation formulas (linear/half-year-convention with/without condition); accessory/component/consumable four-class split
- AssetExplorer: drag-and-drop lifecycle canvas; parent/child contracts; auto-assign assets by login history; license auto-allocate/upgrade/downgrade; free-edition node caps (25/50/250 nodes)
- Device42: automated warranty lookups via Dell/IBM/Lenovo APIs; EnrichAI/InsightsAI-DOQL; Affinity Move Groups; "resolve outages 10x faster / 4.8x ROI" marketing stats
- Freshservice: Freddy AI Copilot incident-asset linking; Resource Utilization module; benchmark/ROI stats (156% etc.)

## Vendor-specific Findings

See Level 3. Additional positioning notes:

- Device42 positions **discovery breadth** as "the most important aspect of an ITAM solution" — a vendor-specific emphasis that contradicts the sample (Snipe-IT lacks discovery entirely). Not generalizable.
- Freshservice positions **CMDB context** as the differentiator over "traditional ITAM" — marketing differentiation inside a converging suite market.
- AssetExplorer bundles **CMDB** even in its free edition — suite-convergence pattern (matches CMDB pass's "Freshservice sells its CMDB under IT Asset Management" observation).

## Rejected Findings

1. **"Discovery is definitional for ITAM"** — REJECTED. Snipe-IT (pure-play, Tier-1-documented) has no native discovery; population is manual/import/API. Discovery is the dominant population method in 3/4 samples (Level 1), not the invariant. Also the historical check: manual/barcode-entry ITAM predates agent discovery.
2. **"ITAM = CMDB with financial fields"** — REJECTED. The organizing object differs: ITAM centers on the asset's own record + its commercial lifecycle; CMDB centers on CIs + typed relationships + service impact. Device42 ships both as separately named capabilities; the CMDB pass independently held this seam. Convergence is commercial packaging, not identity.
3. **"ITAM includes device administration (patching, remote control, configuration)"** — REJECTED. That machinery appears in samples only as suite bundling (ServiceDesk Plus unified agent; Endpoint Central integration) — the UEM seam, not the Type.
4. **"Checkout/custody workflow is definitional"** — REJECTED as L0. Strong (A) in Snipe-IT only as a named mechanic; other products express deployment/assignment differently. Level 1.
5. **"ITAM covers facilities/physical assets generally"** — REJECTED by the evidence itself: Device42 explicitly puts desks/vehicles/buildings in facilities asset management, "not IT".
6. **"Depreciation is definitional"** — REJECTED as L0 (present as machinery in 1, claims in 2, absent-observation in 1). Level 1 common.
7. **"ITAM requires per-asset purchase records from an embedded procurement system"** — REJECTED as L0: commercial facts must be on the record, but a full PO system is Level 1/2 depth.

## Boundary Findings

**vs CMDB (§14, processed — counterparty flag DISCHARGED):**
- Seam confirmed both directions. CMDB's object = configuration item + typed relationships + service/impact model; its central problem is keeping the dependency model aligned with reality. ITAM's object = the asset's own record + its commercial/compliance lifecycle; its central problem is keeping ownership, custody, money and entitlements aligned with reality.
- Remove-relationship test (proposed by the CMDB pass, confirmed here): strip relationships/service context from a CMDB → you hold an asset register with financial fields (ITAM's leg 1). Strip financial/commercial facts and lifecycle-of-money from ITAM → you hold a configuration inventory without commercial agency.
- Convergence zone is real and commercial: Device42, Freshservice, AssetExplorer all bundle CMDB+ITAM in one platform; Freshservice markets its CMDB under the ITAM umbrella. The seams remain structural, not commercial. Keep both leaves. Joint review recommendation satisfied by this file + updated STATUS entry.

**vs Endpoint Management / UEM (§14, processed — counterparty flag DISCHARGED):**
- Seam confirmed: UEM = operational administration of devices through a management channel (enrollment, config policy, compliance enforcement, remote actions); ITAM = the estate's records + financial/commercial lifecycle. UEM owns no purchase/warranty/contract/depreciation authority; ITAM owns no device-configuration authority.
- Drift zone documented from this side too: UEM consoles carry asset-like fields (asset number, ownership, purchasing data) and inventory; ITAM suites integrate endpoint agents for discovery (ServiceDesk Plus unified agent; AssetExplorer↔Endpoint Central integration). Field overlap ≠ object identity.

**vs Enterprise Asset Registry (§10, processed):**
- The registry Type = register of identified holdings + tracked state, retained through retirement — generic, any physical estate. ITAM = registry + the commercial/financial/compliance machinery (entitlement reconciliation, contracts/warranty, value-over-time) bound to the IT domain and spanning non-physical asset classes (licenses/entitlements/subscriptions), which the registry's physical holding model doesn't natively carry.
- Registry pass noted the market label collision ("asset tracking / asset management software" naming). From this side: keep-both — ITAM is the IT-specific, finance-bound superset; the registry is the cross-domain thin ancestor/neighbor. Remove IT-binding + financial machinery from ITAM → the registry.

**vs SaaS Management (§14, unprocessed sibling):**
- Expected seam (per UEM pass note): SaaS Management's object = SaaS subscriptions/usage/spend with discovery from cloud identity/SaaS systems and optimization actions; ITAM treats SaaS/cloud subscriptions as one asset class among the estate. ITAM products increasingly absorb subscription tracking (Microsoft 365 in AssetExplorer; cloud discovery in Device42/Freshservice). Flag left for the SaaS Management pass; no claim asserted about that Type's internal structure.

**vs EAM/CMMS (§16, processed):**
- EAM = maintenance-program-centered management of physical assets for asset-intensive operators (work orders, PM schedules). ITAM carries no maintenance program engine; its service/maintenance content is warranty/contract coverage of IT assets, not work-order execution.

**vs Inventory Management System (§10):**
- Device42's own text: retail inventory tracking exists "for the sale of assets and the quantity needed for replenishment" — a different object (stock for resale) from the IT estate's in-use asset records. Boundary corroborated by vendor language (A).

**vs fixed-asset accounting / financial modules:**
- Finance owns depreciation policy in the ledger; ITAM feeds it (cost, in-service dates, disposal) and may compute indicative value (Snipe-IT depreciation models). The seam: accounting ledger entries vs operational asset records. ITAM without the estate-operations side is just accounting data.

**Historical / market-sample check (per §24):**
- Paper-era IT department ledger: asset register with purchase price, supplier, warranty expiry, license counts, custody log, retirement entries, annually reconciled — satisfies all three L0 legs at analog level (identified records + lifecycle through disposal + commercial reconciliation done by hand).
- Spreadsheet era: satisfies legs 1–2 and partially 3 — Device42's own narrative treats the spreadsheet as the manual predecessor ITAM replaces ("data quickly becomes obsolete as soon as the spreadsheet is done"), consistent with the machinery leg being the upgrade step.
- 2000s on-prem barcode ITAM tools: satisfy the core without cloud, agent discovery, APIs, or AI.
- Conclusion: no modern machinery (cloud discovery, AI, SaaS breadth, auto-reconciliation engines) enters L0. Definition abstracts above the current dominant implementation.

## Uncertainties

1. Enterprise leaders (ServiceNow, Flexera, Ivanti) not directly evidenced — docs gated/oversized. The enterprise pole's object structure is inferred from sampled vendors' integrations/partner listings, not from those vendors' docs. No enterprise-specific operational claims are made anywhere.
2. Whether "cloud/SaaS subscriptions as first-class asset records" is now universal: A-evidenced in 3/4 (absent from Snipe-IT's center). Held as Level 2 breadth, not L0.
3. Depreciation universality uncertain (see Rejected 6). Wording in the final document keeps depreciation as common, not definitional.
4. Freshservice/AssetExplorer/Device42 evidence is product-page level (Tier 2); no field-level or workflow-step-level claims were drawn from them beyond what their pages state.
5. Snipe-IT license-seat mechanics are evidenced by API endpoint titles + overview text, not a dedicated concept page; seat-level detail (limits, behavior) not asserted.
6. The exact boundary between "software asset management" as a named sub-discipline and ITAM varies by market (SAM sometimes sold separately at enterprise scale); the directory has no separate SAM leaf, so this pass documents SAM machinery as the software-side engine of ITAM. Recorded as a taxonomy note for the owner.

## Final Synthesis

IT Asset Management is the IT department's asset system of record. Its world is made of identified asset records — hardware devices and software entitlements alike — each carrying the commercial facts of its existence (what it cost, who supplied it, what covers it) and held in an explicit lifecycle from acquisition through deployment and service to disposal, with the record surviving as history. Around the records, the system continuously reconciles and reports the estate's commercial position: entitlements vs deployments, coverage and expirations, value over time, audit readiness. Discovery, audits, checkout, labeling, purchase orders, CMDB views, and AI assistants are the common or variant machinery of different market poles — none of them is what makes a product an ITAM product. What makes it one is the joint presence of the estate's records, the lifecycle of record, and the money-and-compliance engine over them, bound to the IT domain.
