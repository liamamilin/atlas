# Research Notes — Tower Management Platform

Research date: 2026-09-10
Slug: tower-management-platform
Directory location: §19 Energy, Utilities & Telecommunications (between Mobile Network Management and Telecom Provisioning Platform)

## Research Goal

Understand what a Tower Management Platform actually is from real products: what objects it holds, what work it runs, who uses it, and where its boundaries lie against Telecom OSS, EAM, Property Management, Lease Administration, Telecom Inventory Management, Telecom Field Service, and site-monitoring products.

Working hypothesis (Step 1): the software used by tower companies (towercos) and operators-with-towers to run a distributed portfolio of passive-infrastructure sites — sites, tenants/colocation, leases (both directions), site operations, and tenant billing. The telecom-oss pass (2026-09-10) pre-flagged this leaf as "passive-infrastructure asset management, adjacent not OSS" — to be confirmed or corrected.

## Initial Boundary

- The directory context (§19) and the market both disambiguate "tower" to telecom towers (macro towers, rooftops, poles, monopoles, shelters). Other "tower" readings (cooling towers, control towers) are out of scope.
- Industry vocabulary: "Tower Management System (TMS)", "Telecom Site Management Software (TSMS)", "towerco software", "passive infrastructure management". The directory leaf name "Tower Management Platform" is treated as the same Type.
- Known label ambiguity to resolve: remote site monitoring / IoT products also call themselves "tower management systems" (Errigal, Nuratech, GlobalMavin). Must decide: variant of this Type, or a different Type borrowing the label.

## Research Questions

1. What is the core object structure? (site, asset/equipment, tenant, lease, contract, project, work order, permit)
2. What business model does the software serve? (own passive infrastructure → lease space/power to tenants → bill → maintain)
3. How does colocation work as a workflow? (request → feasibility/capacity → contract → equipment rights → install → billing)
4. What are the two lease directions and how are they handled? (ground leases in — towerco as lessee; tenant leases out — towerco as lessor)
5. What operational layers exist? (rollout projects, O&M, field force, site access, monitoring, power/energy)
6. Who uses it, including external parties (tenants, landlords, contractors)?
7. What rules matter? (structural/space/power capacity, lease terms and escalations, pass-through costs, equipment-vs-lease-rights reconciliation)
8. Where are the boundaries against neighboring Types?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **Tarantula Red Cube** (tarantula.net) — vertical specialist; used at the largest towerco scale (Indus Towers ~100,000 towers per vendor-published testimonial; also American Tower, edotco, Viom, Torrecom, KIN Towers). Richest module documentation found.
2. **NEXSYS-ONE** (nexsysone.com) — dedicated towerco platform, end-to-end framing "site acquisition → built-to-suit → tenant billing"; modular suite (PROJECT/TOWER/ASSET/TASK/VENDOR/SITE/ADMIN/AUDIT/FLEET/ACCESS-ONE); Latin American heritage, also serves operators, fiber, EV, solar.
3. **Accruent Siterra** (accruent.com) — telecom site management from a real-estate/IWMS software house; site-centric architecture; different philosophy (site management as an extension of lease/real-estate administration); American Tower case study; enterprise tier.
4. **OneVizion TowerVizion** (onevizion.com) — newer entrant; "native data model built around tower, tenant, and lease relationships"; mid-market → enterprise (500–5,000 sites); leases/tenants/billing/permits framing.
5. **Xolas TMS** (xolas.io) — small regional vendor (Malaysia); role-based external views (Telco, Tower Supplier, Contractor, Backhaul, Landlord); evidence limited to marketing page (JS-only site, not fetchable) — used as a breadth/regional check, not a primary source.

Boundary/variant evidence (not primary sample): Errigal (equipment monitoring pole), Nuratech RTMS + GlobalMavin (IoT monitoring pole, emerging markets), Inspur TMS (China-Tower-ecosystem vendor; LATIS Saudi case), ZIRA (BSS/lead-to-cash pole), TCS Crystallus (CRM/partnership-management pole), MRI Software (lease-administration/accounting pole), FALCON/Salience (regulator-facing national permitting pole), UpStore TMS (Malaysian NFP-licensee compliance variant), Truebyl Tower Sense (lease/revenue pole).

## Sources

Tier 1/2 (official product surfaces; no public help-center/user-guide docs were reachable for any sampled product — see Uncertainties):

- Tarantula — Red Cube product page: https://www.tarantula.net/red-cube-telecom-site-management-software (fetched 2026-09-10)
- Tarantula — "Tower billing complexity" blog: https://www.tarantula.net/blog/towerco-billing (fetched 2026-09-10)
- Tarantula — Location module whitepaper abstract: https://www.tarantula.net/whitepaper/red-cube-location-module (fetched 2026-09-10; datasheet gated)
- NEXSYS-ONE — Telecom Tower Companies: https://www.nexsysone.com/telecom-tower-companies/ (fetched 2026-09-10)
- NEXSYS-ONE — Modules: https://www.nexsysone.com/modules/ (fetched 2026-09-10)
- Accruent — Siterra product page + FAQ: https://www.accruent.com/products/siterra (fetched 2026-09-10)
- OneVizion — TowerVizion: https://onevizion.com/towervizion/ (fetched 2026-09-10)
- Xolas — https://xolas.io/ (search-index content only; live fetch failed — JS-only site)
- Errigal — https://errigal.com/tower-management-systems/ (search-index content)
- Nuratech Labs — RTMS: https://www.nuratelabs.com/remote-tower-management-system.html (search-index content)
- Inspur — Tower Management System (Huawei Cloud Marketplace listing + LATIS case): https://marketplace.huaweicloud.com/intl/contents/6897de29-4c7f-49ca-8a0b-dca1eb254538 , https://inspur.com/en/2822607/2822609/2026060309001058018/index.html (search-index content)
- ZIRA — TowerCo BSS: https://ziragroup.com/solutions/towerco/3 (search-index content)
- TCS — Crystallus for Tower Companies: https://www.tcs.com/what-we-do/services/enterprise-solutions/solution/tcs-crystallus-telecom-towercos (search-index content)
- MRI Software — Telecom: https://www.mrisoftware.com/telecommunications/ (search-index content)
- Salience/FALCON — Tower Management System PDF: https://www.salience.ae/wp-content/uploads/2019/11/FALCON-Towers-Management-System.pdf (search-index content)
- UpStore — Telco Towers Management System: https://upstore.com.my/asset-management/industries/telco-towers/ (search-index content)
- Truebyl — Tower Management Solution: https://truebyl.com/solutions/tower-management-solutions (search-index content)
- Rakuten Symphony — Tower Site Manager: https://symphony.rakuten.com/enterprise/site-management/tower-company (search-index content)

## Product Observations

### Tarantula Red Cube (evidence layer A unless noted)

- Positioning: "end-to-end solution for Telecom Site Management"; "single source of information"; "integrate operational processes with commercial reality".
- Modules (vendor-documented): Location (GIS site portfolio + online sales channel for site sharing), Site Inventory ("direct linkage between site inventory and lease rights to minimize revenue leakage"), Rollout (site rollout projects: approvals, candidate identification, survey management, milestone SLAs, documentation control), Co-Location ("fully integrated order-to-cash value chain that drives customer equipment rights and invoicing through linkage with contractual terms"; "capturing inventory data throughout the inbound colocation provisioning process"), Lease ("Track and account for landlord and tenant leases"; "automate lease renewal and termination"; "reconciling onsite assets and lease rights through revenue stream integration"; "comply with accounting standards"), Billing ("customer billing and property rent roll"; "flexible billing engine that incorporates rental costs, tax inputs, discount schemes"), Operations & Maintenance ("site maintenance schedules, site audits and inspections, and trouble ticket resolution"; "site asset health and energy consumption"), Field Force (work orders to field/contractors, proof-of-completion uploads), Site Access (planning/approving/monitoring site visits; visitor certifications; integrated site locking), Tower Acquisition (portfolio purchase: data capture, "creation and novation of relevant leases", field audits, regulatory compliance checklists), Transmission (link lifecycle), Reporting.
- CAPP framework (vendor's own abstraction): Contract Management ("know your rights and obligations") + Asset Management ("know what is on and planned to be on the site") + Process Management ("know what is meant to happen") + Project Management ("know what is happening"). Configurable components: workflows, data forms, milestones, reports.
- Billing blog (vendor domain knowledge, layer A for Tarantula's framing of the industry): pricing variables — tower structure type (ground-based/rooftop/special), equipment type, equipment height, location (urban/rural), tenancy count (utilization discounts), power consumption; billing models — per equipment count, per occupied area, per aperture size, per weight/wind/ice load, point-based systems; pass-through costs — ground-lease rent above thresholds, energy costs (grid + diesel + batteries); discounts (volume/strategic accounts); multi-currency and multi-tax; separate vs consolidated bills; multiple invoice templates per contract type.
- Signature problem the product claims to solve: "MNOs add equipment to towers but miss out on notifying the infrastructure hosts" → equipment-vs-lease-rights reconciliation as revenue-leakage control.
- Add-ons: IFRS 16 (ground-lease accounting standard), HQ reporting (multi-country), GDPR, Approvals mobile app, AI document intelligence (OCR), Digital Twin.
- Scale claims (vendor marketing, not asserted in final doc): 450,000+ towers, 30+ countries, 7.5M+ assets tracked.

### NEXSYS-ONE (evidence layer A)

- Towerco framing: "Managing end-to-end Tower Company's operations: from site acquisition, over built-to-suit to tenant billing"; "Colocation & tower sharing functionality to manage the reservations and tenant onboarding processes"; "Complex tenant billing scenarios with accurate and consolidated billing data"; "End-to-end asset and inventory management integrated with purchasing"; "Monitoring passive network infrastructure and initiating preventive/corrective maintenance"; "Linking finance, assets, and project management into one platform".
- Modules: PROJECT-ONE (site acquisition → procurement → final acceptance; milestones), TOWER-ONE ("centralizing all site information"; "From lease management and billing to streamlined tower-sharing processes"; "attract additional tenants per site"), FIBER-ONE (fiber routes/locations), ASSET-ONE (assets across warehouses/vehicles/sites; barcode/RFID; handovers; refurbish/resale), TASK-ONE (field activities ↔ NOC; trouble ticketing; preventive/corrective maintenance; workflow templates; KPIs/SLAs), VENDOR-ONE (vendor onboarding, contracts, insurance, POs/invoices/shipments, scorecards), SITE-ONE (remote monitoring of "energy components, power systems, and environmental data"; security sensors against unauthorized access/theft/damage), ADMIN-ONE (self-administration: projects, fields, menus, workflows, business rules, KPIs/SLAs, milestones, lead-times, user profiles/permissions, bulk uploads — no coding), AUDIT-ONE (on-site acceptance/quality checks), FLEET-ONE (vehicles), ACCESS-ONE (digital access control; smart locks; entry codes generated through TASK-ONE for scheduled work).
- Same platform sold to telecom operators, fiber companies, IBS, EV charging, solar/wind, O&M companies — infrastructure-management platform family with a towerco configuration.

### Accruent Siterra (evidence layer A)

- Positioning: "Streamline your sites, assets, projects, and leases"; "single cloud solution purpose-built for Telecom site management"; "site-centric architecture with intuitive hierarchy, single source of truth and collaborative ecosystem".
- Capabilities (vendor-documented): per-site data drill-down for technicians; site-based licensing ("add as many users as needed per site"); pre-built/customizable reports; bulk and cascading operations (deactivate site assets + open projects via Project Cancellation); high customizability; portfolio map view with drill-down; project management for "site construction, openings, and capital improvements"; configurable workday/holiday calendars per country for schedule math; workflow dependencies ("automatically re-opening all dependent tasks and subtasks when an approver rejects a deliverable").
- Leases demo framing: "Comprehensive lease data, payments & reconciliation, critical date alerts and abstracting & reporting". Site navigation demo: "Customer self-service, manage sites and assets, and request new sites".
- FAQ definition of the category (vendor's words): "Telecom Site Management Software (TSMS) streamlines the operations of telecom infrastructure sites through site monitoring, asset tracking, maintenance scheduling, and real-time performance analytics."
- Philosophy note: Accruent is a real-estate/facilities software company (IWMS, lease administration, CMMS); Siterra extends that grammar to telecom sites. Vendor explicitly cross-links Siterra lease management to its Lucernex lease-administration product.
- Scale claims (vendor marketing): 1.3M sites, 2M+ projects, 8M+ assets, 100M+ documents; American Tower case study ("consolidated software, reduced manual communication, optimized workflows").

### OneVizion TowerVizion (evidence layer A)

- Positioning: "One platform for leases, tenants, billing, and permits"; "helps tower owners, asset managers, and site operations teams manage distributed telecom portfolios".
- Problem framing (vendor): "Leasing, finance, and site ops each keep their own records — usually in spreadsheets. That's how overbilling slips through, rent escalations get missed, and permits fall out of sync with what's actually built on-site."
- Capabilities (vendor-documented): "Near real-time tracking of tenants, equipment, and tower space use"; "Automated lease schedules, rent escalations, and notifications"; "Accurate tenant billing, tied directly to lease terms"; "Site-level revenue, expenses, and performance insights"; "Maintenance tracking by vendor, date, and cost"; "Permit tracking from intake through approval"; "Document and photo records linked to each asset — searchable, exportable"; "Acquisition pipeline and due diligence workflows"; colocation pipeline "from prospect to signed lease"; map views.
- Data-model claim: "native data model built around tower, tenant, and lease relationships — not bolted onto a generic CRM or adapted from commercial real estate tools."
- Scenario framing: multi-tenant towers with overlapping lease terms; legacy assets from bulk buys/M&A; rural/remote sites; high-turnover markets. Scale tiers: <500 / 500–2,500 / 2,500+ sites.

### Xolas TMS (evidence layer A-, marketing page only; live fetch failed)

- Role-based views: Tower View (role-dependent access), Telco View (Sites, Requests, Maps, Tickets), Tower Supplier View (sites by supplier, structure report, site structure and equipment), Contractor View (assigned tickets, site workflows), Backhaul View (sites by provider, requests), Landlord View (rental report, tenancy due).
- Modules: Sites (rollout report, site groups, tower suppliers, structure report, equipment report), Maintenance (tickets, site workflows), Property (average rental, expiry report, tenancy due, landlords report, rental by month), Finance (total due by sharers, new revenue by year, utility report).
- Regional interest: Malaysia; customer quote from D'Harmoni Telco Infra (towerco). Confirms the same core grammar (sites + sharers/tenants + landlords + maintenance + finance) in a small regional product.

### Boundary-evidence products (observations, layer A for each as marketing-page evidence)

- **Errigal** ("Tower Management Systems"): "Simplify the management of tower equipment, including lights, generators, and multi-vendor devices… fault management, automation, and real-time reporting." → equipment/telemetry monitoring pole; no tenancy/lease layer visible. Label collision with the portfolio-management Type.
- **Nuratech RTMS / GlobalMavin**: IoT event monitoring against "poor grid power supply, operational leakages, diesel pilferage and equipment vandalism"; SLA/downtime; field-force app integration. → monitoring pole, emerging-market energy focus.
- **Inspur TMS** (China Tower ecosystem; LATIS Saudi Arabia, 8k+ towers): Portal (role views), Site Management (room plan, device panel visualization), CRM (operator customers signing lease agreements), Cost Management (tower service fee, rental costs), Monitoring (performance/alarm → trouble tickets to EOMS), EOMS (O&M workflow platform; preventive + corrective tickets; field engineer mobile app). → same core grammar, delivered as an integrator-built suite.
- **ZIRA TowerCo BSS**: lead-to-cash for towercos — product catalog, partner management, order management, billing; "passive infrastructure leasing, collocation enablement". → BSS pole: the commercial chain without the site-operations estate.
- **TCS Crystallus for Tower Companies**: property-owner + CSP partnership management; landlord self-service portal (site info, contracts, cases, payments); lead-to-cash on Salesforce/ServiceNow/SAP; co-location subscriptions; site contract management. → CRM/service pole.
- **MRI Software (Telecom)**: lease administration + AI lease abstraction + IFRS 16 lease accounting + revenue assurance (billing vs contracts) + energy management "for TowerCo and Telco organizations". → lease-administration pole: the lease layer alone, at accounting depth.
- **FALCON (Salience)**: centralized regulator↔operator platform for tower permitting and compliance ("operators apply for permits and regulators… issue permits and monitor compliance"); infrastructure-sharing detection. → regulator-facing national registry pole; different user and different core object (permits).
- **UpStore TMS (Malaysia)**: "Built MCMC-grade for Malaysian NFP licensees managing site permits, insurance, billing, and… reporting standards." → compliance-heavy regional variant.
- **Truebyl Tower Sense**: lease & contract management (multi-party agreements, revenue-sharing), asset tracking, revenue management (rental/energy/shared-cost billing), ISA tracking, landlord/contractor self-care app. → confirms lease+revenue core from another vendor.
- **Rakuten Symphony Tower Site Manager**: lifecycle orchestration (permitting → structural validation → commissioning → tenant onboarding), colocation & tenant management with feasibility checks and SLA tracking. → confirms colocation onboarding as a managed workflow.

## Cross-product Comparison

| Dimension | Tarantula Red Cube | NEXSYS-ONE | Accruent Siterra | OneVizion TowerVizion | Xolas TMS |
|---|---|---|---|---|---|
| Site portfolio of record | Location + Site Inventory (GIS, capacity) | TOWER-ONE + ASSET-ONE (sites, assets) | Site-centric hierarchy (sites → assets) | Native tower/tenant/lease model | Sites (structure/equipment reports) |
| Tenancy / colocation | Co-Location module (order-to-cash, equipment rights) | TOWER-ONE (reservations, tenant onboarding, sharing) | Customer self-service "request new sites" | Colocation pipeline "prospect → signed lease"; tenants tracked | Telco View: requests; "total due by sharers" |
| Leases (both directions) | Lease module: landlord + tenant leases; IFRS 16 add-on | TOWER-ONE lease management | Leases demo: payments & reconciliation, critical dates, abstracting | Lease schedules, escalations, billing tied to lease terms | Property: landlords, tenancy due, rental |
| Tenant billing / revenue | Billing module: rent roll, flexible engine | TOWER-ONE billing; consolidated billing | Lease payments & reconciliation | Tenant billing tied to lease terms; site-level revenue | Finance: revenue by sharers, utility report |
| Rollout / build projects | Rollout + Tower Acquisition | PROJECT-ONE (acquisition → acceptance) | Projects (construction, openings, capital improvements) | Acquisition pipeline & due diligence | Rollout report |
| O&M / field | O&M + Field Force + Site Access | TASK-ONE + AUDIT-ONE + ACCESS-ONE | Maintenance scheduling; technician site data | Maintenance by vendor/date/cost | Maintenance tickets, contractor view |
| Remote monitoring | (via asset health/energy; not a headline module) | SITE-ONE (energy, power, environment, security sensors) | "site monitoring" per FAQ | "near real-time tracking of tenants, equipment, space use" | — |
| Permits / compliance | Regulatory compliance checklists (acquisition) | — (not headline) | Critical dates | Permit tracking intake → approval | (regulatory variant: UpStore in same market) |
| Documents per site | Documentation control; OCR add-on | Documentation structure (ADMIN-ONE) | 100M+ documents claim | Searchable dossier per asset | PDF uploads (council docs, cover notes) |
| External parties | Online sales channel; contractor proof-of-completion | Vendor portal (VENDOR-ONE); access codes | Customer self-service | — (pipeline-oriented) | Telco/Supplier/Contractor/Landlord views |
| Configurability | CAPP framework; 30+ process templates | ADMIN-ONE self-administration, no code | "Highly customizable"; bulk operations | Native data model | Fixed small-product shape |
| Customer tier | Tier-1 towercos (100k+ towers) | Mid/large towercos + operators | Enterprise (American Tower) | 500–5,000 sites | Small regional towercos |

Cross-product commonalities (layer B):

1. Every sampled product is organized around a **site/tower record** as the anchor object to which assets, tenants, leases, documents, work, and money attach.
2. Every sampled product carries a **tenancy/colocation structure** (tenants on sites, space/power occupancy, sharing) — Tarantula Co-Location, NEXSYS-ONE TOWER-ONE, TowerVizion tenants, Xolas "sharers", Siterra self-service site requests.
3. Every sampled product carries **leases in both directions** (landlord/ground leases and tenant leases) with payments, renewals/terminations, escalations, critical dates.
4. Every sampled product carries **tenant-side revenue** (billing/rent roll/revenue by sharer) and, in most, **landlord-side cost** (ground rent payable).
5. Every sampled product carries **site lifecycle work**: build/rollout projects on the way in, maintenance/trouble tickets on the way through.
6. Every sampled product holds **per-site documents** (leases, permits, drawings, photos) and a **map/GIS view** of the portfolio.
7. Recurring signature behavior: reconciling **what is physically on the site** against **what contracts say should be there / is paid for** (Tarantula "linkage between site inventory and lease rights"; TowerVizion "permits fall out of sync with what's actually built on-site", "overbilling slips through"; Tarantula billing blog "MNOs add equipment… but miss out on notifying").

## Canonical Abstraction

### L0 — Defining Invariant

The Tower Management Platform is the tower infrastructure owner's system of record for a distributed passive-infrastructure portfolio. Its defining core is three jointly-held structures:

1. **The site portfolio of record** — persistent, individually identified site records (towers, rooftops, poles, shelters), each anchored to a location, a physical structure, and a capacity (space, power, structural load), holding what stands on it.
2. **The occupancy structure** — who/what occupies each site: tenants under agreement and/or equipment mounted, tracked against the site's capacity. Tenancy is the revenue engine of the tower business; equipment rights are its physical expression.
3. **The lease/agreement structure binding sites to land and occupancy to tenants** — ground/land leases inward (the owner as lessee) and tenant leases outward (the owner as lessor), carrying terms, escalations, renewals, payments — the commercial instruments from which tenant billing and landlord rent-roll are derived.

Jointly load-bearing: (1) alone = a GIS site list / asset register; (2) without (1)+(3) = a tenant list with nothing to occupy; (3) without (1)+(2) = lease administration; (1)+(3) without (2) = property/lease records with no occupancy truth; (1)+(2) without (3) = site inventory with no commercial instrument; (2)+(3) without (1) = contracts with no site estate. Remove any one and the product stops being a tower management platform and becomes one of the neighboring Types.

Historical check (§24): a paper-era towerco — site register + lease files (land + tenants) + maintenance logbooks — satisfies all three structures; the structures, not any digital implementation, are the invariant. Operator-owned tower portfolios (no external tenants) thin structure 2 to own-equipment occupancy but keep the shape. Regional variants (India, Malaysia, Middle East, LatAm) all exhibit the same three structures. Passes.

### L1 — Common Mature Structure

Present across the sampled products; expected in a mature modern implementation but not definitional:

- Colocation order management: tenant request → feasibility/capacity check → reservation → contract/lease → equipment rights → install → billing (Tarantula, NEXSYS-ONE, TowerVizion, Rakuten Symphony)
- Rollout/build project management: candidate identification, surveys, permits, milestones/SLAs, acceptance (Tarantula Rollout, NEXSYS-ONE PROJECT-ONE, Siterra Projects)
- O&M: preventive maintenance schedules, inspections/audits, trouble tickets, fault management (all sampled)
- Field force / contractor work orders with proof-of-completion (Tarantula Field Force, NEXSYS-ONE TASK-ONE, TowerVizion, Xolas)
- Site access control: visit planning/approval, visitor certification, smart locks (Tarantula Site Access, NEXSYS-ONE ACCESS-ONE)
- Billing engine: rental, energy/pass-through, discounts, taxes, multi-currency, consolidated vs split invoices (Tarantula, NEXSYS-ONE, TowerVizion, Xolas)
- Per-site document dossier (leases, permits, drawings, photos) with search (TowerVizion, Siterra, Tarantula, UpStore)
- Portfolio map/GIS view with drill-down (Tarantula Location, Siterra, TowerVizion, Xolas)
- Vendor/contractor management (NEXSYS-ONE VENDOR-ONE, Tarantula, TowerVizion)
- Reporting/analytics and role-based dashboards (all)
- External-party self-service portals (tenants, landlords, contractors) (Siterra, TCS, Truebyl, Xolas role views)
- Platform configurability: workflow templates, custom fields/forms, role/permission administration (Tarantula CAPP, NEXSYS-ONE ADMIN-ONE, Siterra)

### L2 — Variant / Optional Structure

Depends on market, owner type, geography, regulatory posture:

- Remote monitoring / IoT telemetry of site power, fuel, security, environment (NEXSYS-ONE SITE-ONE; the Errigal/Nuratech/GlobalMavin pole; emerging-market driver: grid instability, diesel pilferage)
- Energy management as a discipline: generators, batteries, solar hybrid, energy pass-through billing, energy-ESG (Tarantula O&M energy; MRI energy; Nuratech)
- Regulatory/permitting management: permit intake→approval tracking, structural audits, aviation lighting, national regulator reporting (TowerVizion permits; UpStore MCMC; FALCON regulator pole)
- Lease accounting compliance (IFRS 16 / ASC 842) (Tarantula add-on; MRI pole)
- Portfolio M&A: acquisition due diligence, lease novation, bulk data migration (Tarantula Tower Acquisition, TowerVizion acquisition pipeline)
- Adjacent infrastructure on the same platform: fiber/transmission links, small cells/DAS/edge (Tarantula Transmission, NEXSYS-ONE FIBER-ONE, ZIRA)
- Built-to-suit / turnkey delivery as a managed project class (NEXSYS-ONE)
- Digital twin / structural visualization (Tarantula add-on, NEXSYS-ONE views, Axximum LiDAR)
- BSS-grade lead-to-cash (catalog, order orchestration, receivables) (ZIRA pole)
- CRM/service management for landlord/tenant relationships (TCS Crystallus pole)
- Hosting and licensing shape: SaaS vs on-prem; site-based licensing (Siterra)

### L3 — Vendor-specific (research notes only)

- Module names and branded frameworks: RED CUBE, CAPP, TOWER-ONE/PROJECT-ONE/ASSET-ONE/TASK-ONE/SITE-ONE/ADMIN-ONE/AUDIT-ONE/FLEET-ONE/ACCESS-ONE/VENDOR-ONE, TowerVizion, Tower Sense, Crystallus.
- Vendor scale claims: Tarantula 450,000+ towers / 7.5M+ assets; Siterra 1.3M sites / 100M+ documents; TowerVizion ROI-from-tenancy stat citing Mordor Intelligence; Inspur LATIS 8k+ towers.
- Tarantula billing-blog industry economics: "power accounts for one-third of the profit and loss structure of towercos" (vendor claim, not independently verified).
- Inspur EOMS (enterprise O&M workflow platform) as a separate paired system in the China-Tower ecosystem pattern.
- Xolas role-view naming (Telco/Tower Supplier/Contractor/Backhaul/Landlord views).

## Vendor-specific Findings

- Tarantula's CAPP framework (Contract/Asset/Process/Project as the four "knows") is a vendor articulation of the same structure found across products — useful as corroboration, not adopted as canonical vocabulary.
- NEXSYS-ONE sells one platform into many infrastructure industries (towers, fiber, EV, solar) — the towerco configuration is the relevant instance; the multi-industry breadth is vendor strategy.
- Accruent Siterra's site-based licensing ("add as many users as needed per site") is a commercial model detail, not a Type property.
- TowerVizion's explicit "not adapted from commercial real estate tools" positioning is a competitive claim that nonetheless confirms the property-management adjacency is real in the market.

## Boundary Findings

1. **vs Telecom OSS** (processed 2026-09-10): OSS is the network engine — services and the active resources carrying them, fulfillment + assurance. A towerco has no service to activate or assure; its product is space/power on passive structures. Tower management holds sites/tenancy/leases, not network elements/service state. Confirms the telecom-oss pass's forward note ("passive-infrastructure asset management, adjacent not OSS"). Remove the tenancy/lease layer and add service/network semantics → OSS territory.
2. **vs Enterprise Asset Management / EAM (§16)**: EAM maintains an asset base (lifecycle, maintenance, work orders). Tower management runs a leasing business on top of the asset base: tenancy, leases in both directions, tenant billing. Strip tenancy+leases → EAM/CMMS. The maintenance module inside tower management is EAM-shaped but subordinate to the commercial structures.
3. **vs Property Management (§17)**: shares the landlord/tenant/lease grammar (and vendors compete across the boundary — TowerVizion's positioning, Accruent's heritage, MRI's lease stack). The object differs: human occupancy of dwellings/commercial space vs equipment occupancy of infrastructure sites; tower management adds structural/space/power capacity, colocation fulfillment, site power/O&M, and ground-lease pass-through economics. Strip the infrastructure/colocation semantics → property management.
4. **vs Lease Administration (§10/§17)**: the lease layer alone at administration/accounting depth (MRI pole). Tower management binds leases to physical sites and drives fulfillment and operations from them; a lease-administration product does not run colocation onboarding or site O&M.
5. **vs Telecom Inventory Management (§19, processed)**: that Type is the estate of telecom services/equipment consumed or delivered (circuits, lines, network elements) with a recorded lifecycle reconciled to carrier/network reality. Tower management's inventory is passive site holdings bound to lease rights; the reconciliation axis is commercial (contract vs installed) rather than service (order vs network). Overlap: both hold equipment records; different center of gravity.
6. **vs Telecom Field Service (§19, processed)**: field workforce system of record (work orders, crews, dispatch-to-closure). Tower management consumes field execution as one module (TASK-ONE, Field Force); its defining core is the site/tenancy/lease record, not workforce capacity.
7. **vs Construction Project Management (§17)**: rollout projects are a module inside tower management; the site portfolio persists beyond any project. A construction PM product has no tenancy/lease estate.
8. **vs site monitoring / IoT products using the "tower management" label** (Errigal, Nuratech, GlobalMavin): these monitor tower equipment (lights, generators, power, security) and raise faults. They lack the tenancy/lease/commercial layer entirely. They are a different Type (monitoring/telemetry) borrowing the label — recorded as a label-collision issue, not a variant of this Type.
9. **vs regulator-facing national tower registries** (FALCON/Salience): government-side permitting/compliance registries over national tower populations. Different user (regulator), different core object (permit), different workflow (application→approval→compliance). Adjacent; the towerco-side permit tracking is the mirror image.
10. **"Remove what to become another Type" summary**: remove tenancy+leases → EAM/site-asset tool; remove sites → lease administration/property management; remove leases → site inventory/monitoring; remove the passive-infrastructure object and add network services → Telecom OSS; remove the site estate and keep only the commercial chain → TowerCo BSS.

## Uncertainties

- **No Tier-1 help-center/user-guide documentation was reachable for any sampled product.** All evidence is from official product/marketing pages, vendor blogs, and gated-whitepaper abstracts. Per the source-access limitation: assertion strength is calibrated down; no precise defaults, limits, state names, or numeric thresholds are asserted in the final document; vendor scale/economics claims stay in these notes.
- Xolas TMS could not be fetched live (JS-only site); its observation rests on search-index content of the official page. Used as a breadth check only.
- The exact module boundary between "tower management platform" and paired systems (ERP for accounting, BSS for lead-to-cash, monitoring/IoT for telemetry, field service for workforce) varies by vendor and deployment; the researched sample suggests the platform's own record is the site/tenancy/lease estate, with the surrounding systems integrated.
- Whether operator-owned tower portfolios (no external colocation) constitute the same Type or a thin variant: the sample (NEXSYS-ONE selling to both towercos and operators; Tarantula serving telcos) supports "same Type, thinned occupancy layer", but the towerco pole is the center of gravity of the market and of this document.
- Market-size/ROI figures seen in vendor materials (tenancy-ratio ROI, power share of P&L) were not independently verified and are excluded from the final document.

## Final Synthesis

A Tower Management Platform is the tower infrastructure owner's operating system of record. Its world has three jointly-held structures: the site portfolio (identified passive-infrastructure sites with location, structure, capacity, and holdings), the occupancy on each site (tenants and/or equipment, tracked against capacity), and the lease/agreement structure binding sites to land and occupancy to tenants (ground leases in, tenant leases out, with terms and payments). Around that record it runs the portfolio's life: acquiring and building sites (rollout projects), onboarding tenants (colocation from request to contract to equipment rights), collecting tenant revenue and paying ground rent (billing both directions), and keeping the structures serving (maintenance, inspections, site access, optionally remote monitoring). The signature behavior that makes the three structures one system — rather than three tools — is reconciliation: what is physically on a site must match what contracts say should be there and what is being paid, in both directions (tenant equipment vs tenant leases; land occupancy vs ground leases). The Type is adjacent to, but distinct from, Telecom OSS (active network vs passive infrastructure business), EAM (assets without a leasing business), Property Management (human occupancy vs equipment occupancy), Lease Administration (the lease layer alone), and Telecom Field Service (workforce execution without the estate).
