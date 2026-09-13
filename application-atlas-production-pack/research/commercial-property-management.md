# Research Notes — Commercial Property Management

Research date: 2026-09-07
Slug: commercial-property-management
Directory leaf: Commercial Property Management (§17 Construction, Real Estate & Facilities)

## Research Goal

Understand what a Commercial Property Management application actually is as a software Type: its core objects, the workflows that drive it, its rules and states, and — critically — how it differs from its nearest neighbors (Residential Property Management, Lease Administration, Rent Collection, Property Maintenance Management, Real Estate Investment Management, IWMS/Facility Management).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: landlord/manager-side operating software for income-producing commercial real estate (office, retail, industrial). Core spine: property/space → business tenant → negotiated lease → lease-terms-driven billing & collection → operating expenses (with recovery) → maintenance → owner reporting.
- Likely confusions:
  - Residential Property Management (sibling leaf; same family, different lease economics)
  - Lease Administration (tenant/occupier side of the lease)
  - Rent Collection Platform (money-in slice only)
  - Property Maintenance Management (work-order slice only)
  - Real Estate Investment Management (capital/investor side)
  - IWMS / Facility Management (occupier-side building operations)
  - Hotel PMS (transient guests vs multi-year tenancies)
- Unknowns going in: exact mechanics of CAM reconciliation; how escalations/rent reviews are automated; how owner reporting is structured; how deep "commercial-only" specialists go vs mixed residential+commercial platforms.

## Research Questions

1. What are the core objects (property, space/unit, tenant, lease, charge, expense pool, work order, owner)?
2. How is a commercial lease modeled — which terms become structured data (escalations, options, recoveries, percentage rent, co-tenancy)?
3. How does billing get generated from lease terms (rent schedules, estimated charges, true-up)?
4. How does CAM / operating-expense recovery work (pools, allocations, caps, reconciliation)?
5. How are collection and arrears handled?
6. How does maintenance flow, and when do tenants get charged?
7. How is owner/investor accountability implemented (statements, distributions, reserves, portals)?
8. Where do accounting (GL/AP/AR/trust) and budgeting sit — built-in or connected?
9. Where do vacancy/leasing and tenant portals fit?
10. What structurally separates this Type from Residential Property Management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Positioning | Why selected |
|---|---|---|
| Yardi Breeze (Commercial) | Industry giant's lightweight commercial line; accounting-first | Most explicit commercial feature documentation (CAM recovery, percentage rent, owner tools) |
| AppFolio (Commercial) | Modern cloud platform, mixed residential+commercial portfolios, mid-market | Shows commercial as one market inside a multi-market platform; plan-tiered CAM |
| Buildium (Commercial) | SMB, residential-first platform with commercial support | Shows the boundary from the residential side; commercial as secondary capability |
| Re-Leased | Commercial-only cloud specialist (UK/AU/NZ/CA/US), lease-centric | Richest lease-structure documentation; non-US regional vocabulary (service charge, outgoings) |

Deliberately not sampled: Yardi Voyager / MRI (enterprise suites above the sampled tier — noted as context), Procore (construction), VTS (leasing/marketing side), Entrata (residential-heavy).

## Sources

All fetched 2026-09-07 via WebFetch (official vendor surfaces):

- Yardi Breeze — Commercial features page: https://www.yardibreeze.com/commercial-features/ (fetched OK; detailed feature sections)
- Yardi Breeze — homepage: https://www.yardibreeze.com/ (fetched OK; CAM recovery, tenant portal, investor relations, built-in accounting)
- Yardi Breeze — /help/ URL redirected to a blog post (Help Center article list not directly reachable); limitation noted
- AppFolio — Commercial page: https://www.appfolio.com/commercial-property-management-software/ (fetched OK; /property-management-software/commercial/ was 404)
- Buildium — Commercial portfolio page: https://www.buildium.com/portfolios/commercial-property-management/ (fetched OK; two other commercial URLs 404)
- Buildium — homepage: https://www.buildium.com/ (fetched OK)
- Re-Leased — homepage: https://www.re-leased.com/ (fetched OK)
- Re-Leased — Lease Management page: https://www.re-leased.com/product/tenant-lease-management (fetched OK; includes native lease-structure table and FAQ)

Evidence layers used below: **A** = directly observed on an official page of a specific product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### Yardi Breeze (Commercial) — commercial-features page + homepage

Key observations (Layer A):

- Property management section: "Manage retail, office and industrial properties from any device"; "Track lease expirations"; daily/weekly/monthly task and activity calendar; data access limited "at the property level and for maintenance staff". Premier adds: property and corporate general ledgers, menu-level security, centralized communications with "prospects, tenants and owners".
- Accounting: "Manage payables, receivables and general ledger functions"; "Maintain escrow and trust accounts for all properties"; financial statements with click-into transaction-level details; budgets tracking; 1099 e-filing.
- Accounts Payable: vendor/invoice tracking, recurring payables, "Pay vendors and owners via check or EFT".
- CAM Recovery (dedicated section): "Manage triple net (NNN), gross leases or combinations"; "Create custom expense pools and allocate expenses to tenants"; "Set up flexible common area maintenance (CAM) schedules and assign to tenants"; "Set up caps and percentage allocations for expense pools"; "Post estimated charges for monthly, quarterly or annual reconciliation".
- Rent Collection: "Specify and post rent escalations when due"; "Track sales information for retail leases"; "Post percentage rent where appropriate"; tenants view balances and pay online; autopay; debit/credit card; "Automate recurring rent and fee postings"; "Manage delinquencies and collections". Premier: rent deferral payments and accounting.
- Owner Tools: "Onboard new owners in minutes"; "Manage properties by owner and fraction ownership"; "Customize report packets by owner or property"; "Generate pro rata statements"; owner reports via email or secure portal; "Calculate owner payments while maintaining stipulated reserve amounts".
- Maintenance: online requests from tenants; photos/videos; assign tasks to vendors; "Monitor work order completion and link vendor invoices"; "Automatically charge tenants for work done".
- Setup: "Set up properties, units and tenants in minutes".
- Add-ons: CommercialCafe tenant portal (payments, maintenance requests, "access retail sales data online"); Investment Manager ("Track capital commitments, contributions and distributions"; investor portals); CHECKscan / PayScan (payment/invoice processing outsourcing).
- Pricing is per unit per month with a monthly minimum (commercial priced higher than residential) — pricing detail kept out of the final document.
- Homepage: "all-in-one tenant services, leasing, management and accounting software"; tenant portal/mobile app for "pay rent, submit maintenance requests, renew leases"; "Set up flexible CAM schedules and estimate reconciliation charges"; investor relations contact/activity tracking.

### AppFolio (Commercial) — commercial page

Key observations (Layer A):

- Positioning: "Strengthen & Unify Your Diverse Commercial Property Portfolio"; "the freedom to include commercial properties alongside other property types"; "market-specific features like Common Area Maintenance".
- Six capability areas: Communications & Service; Accounting & Reporting; Maintenance & Operations; Staffing & Training; Marketing & Leasing; Management & Growth.
- Maintenance & Operations: "Streamline your team's Common Area Maintenance tracking and reconciliation processes".
- Accounting & Reporting: "run consistent reports and easily account for multiple property types without leaving the platform".
- Marketing & Leasing: "streamline the entire leasing process... with marketing and leasing features tailored to commercial property management needs".
- Plans: Core includes "Property Accounting, Reports & CAM Tracking", "End-to-End Marketing & Leasing", "Work Order Management", "Inspections & Unit Turns", "Portals & Communication", "Purchase Orders & Inventory Tracking"; Plus adds "Corporate Accounting & Flexible Reports"; Max adds "Leasing CRM", "Leasing Signals", "Custom Fields", "Database API". (Plan gating = vendor detail.)
- Separate portals exist for Resident, Owner, Vendor, Investor (footer login links).
- Customer quotes reference "700+ commercial units", "800+ commercial units", "Senior Lease Administrator" roles — commercial portfolios measured in units; lease administration is a real user role.
- Marketing & Growth framing mentions "increase NOI".

### Buildium (Commercial) — commercial portfolio page + homepage

Key observations (Layer A):

- Commercial page pillars: "Account for everything" — "Capture online rent payments, forecast rent revenue, prepare 1099 e-filings, track certificates of insurance"; "Lease with ease" — "scheduling rent increases and tracking triple net charges to eLeasing"; "Speed up your maintenance" — "including CAM charges, tracking and reconciliation"; "Open up communication" — "Talk to lessees, vendors, and owners—all within Buildium... apps and portals".
- Homepage: all-in-one platform; property accounting (bank reconciliation, 1099 e-filing, property-specific financial reporting); online rent collection (ACH/credit card, funds transfer); leasing (listing syndication, applications, screening, digital leasing); maintenance (work orders, recurring tasks, bill/invoice management); mobile apps for managers/residents; Marketplace integrations; Open API (Premium).
- FAQ: "purpose-built for residential... and can also handle mixed portfolios with student housing, commercial properties, storage units"; customers range from landlords to third-party managers "all the way to fifteen thousand plus" units.
- Commercial is one portfolio type among many (Residential, Associations, Mixed-Use, Student, Enterprise) — commercial supported but not the product's center of gravity.

### Re-Leased — homepage + lease management page

Key observations (Layer A):

- Positioning: "built for commercial and mixed-use portfolios where lease structures are complex and lease events drive operations. Rent calculations, critical-date alerts, tenant communications, and accounting sync - all centred around the lease."
- Native lease-structure table (lease types/components supported natively):
  - Triple net (NNN): "Base rent + tenant-paid taxes, insurance, CAM as separate billing components"
  - Gross: "Single all-inclusive rent figure"
  - Modified gross: "Base rent + tenant-paid select operating expenses; landlord-paid the rest"
  - Percentage rent: "Base rent + percentage of tenant sales above breakpoints; tenant sales reporting cadence per lease"
  - Ground lease: "Long-dated land-only rent; complex escalation cycles; multi-entity ownership"
  - Tenant improvement allowance (TIA): "budget, drawdowns, amortisation, reporting per lease"
  - CAM / outgoings / service charge: "RICS-compliant apportionment matrix; budget vs actuals; tenant charge-back"
  - Rent reviews: "CPI-linked, fixed percentage, market review, stepped, or hybrid"
  - Lease options: "Renewal options, break clauses, right of first refusal, right of first offer"
  - Co-tenancy clauses: "Anchor-tenant dependencies; rent reduction triggers; cure periods"
  - WALE: "Weighted average lease expiry calculated automatically across the portfolio"
- Rent Review Hub: central management of "upcoming and overdue rent reviews"; dashboard calendar; automated reminders; "schedule multiple future rent reviews and calculate the appropriate rent increases (including market increases, CPI, stepped and indexed)".
- Dashboard as "command center": key lease events, communications, maintenance, arrears.
- Property Operations: tenant/property-manager mobile apps; "the maintenance loop"; supplier processing; "automate CAM/Service charges/Outgoings effectively"; compliance assurance.
- Arrears and Credit Control: automated chasing; online rent payments (Re-Leased Pay); "Cut the time spent generating & reconciling invoices and chasing arrears".
- Budget Management module; Reporting module; Real Estate Insights (portfolio analysis).
- Accounting options: built-in accounting + "Connected Accounting" (two-way sync with Xero, Sage Intacct, QuickBooks, NetSuite — contacts, invoices, bills, credit notes, accounts, tracking categories, tax rates, payments; event-triggered/nightly/manual sync) + "Leading Trust Accounting" "Purpose-built for third-party property managers and agencies" + custom ERP connections via APIs.
- Tenant Portal: "log maintenance, view and pay invoices, access documents, and manage compliance"; tenants upload required compliance documents with status tracking.
- Email integration (Outlook/Gmail) centralizing tenancy/contact communications.
- Credia AI: Action (reads emails, creates maintenance tasks/reminders/notes/work orders "with your approval"), Extract (extracts key info from "insurance records, invoices, leases, compliance documents"), Advise (lease Q&A with source references; suggestions e.g. rent review clauses).
- Regional vocabulary: CAM (US) / service charge (UK) / outgoings (AU-NZ) treated as one concept family; RICS compliance mentioned; country sites for UK/AU/NZ/CA/US.
- FAQ claims about competitors (e.g., that some residential-first products "require workarounds" for NNN) are vendor marketing claims — recorded but not treated as evidence about those competitors.

## Cross-product Comparison

| Structure / capability | Yardi Breeze Comm. | AppFolio Comm. | Buildium Comm. | Re-Leased | Layer |
|---|---|---|---|---|---|
| Property + space/unit inventory as managed asset | ✔ (retail/office/industrial; properties, units, tenants) | ✔ (mixed portfolio, commercial units) | ✔ (commercial in mixed portfolio) | ✔ (properties, tenancies) | B |
| Business tenant under negotiated lease | ✔ (NNN/gross/combo) | ✔ (commercial leasing tailored) | ✔ (triple net charges; rent increases) | ✔ (NNN/gross/mod-gross/percentage/ground) | B |
| Lease-terms-driven billing (schedules, escalations) | ✔ ("post rent escalations when due"; recurring rent/fee postings) | ✔ (implied via CAM tracking + leasing; not itemized on page) | ✔ ("scheduling rent increases") | ✔ (rent calculations from lease; rent review automation) | B |
| CAM / opex recovery with reconciliation | ✔ (expense pools, caps, % allocations, estimated charges, monthly/quarterly/annual reconciliation) | ✔ (CAM tracking & reconciliation; plan-gated) | ✔ (CAM charges tracking & reconciliation) | ✔ (apportionment matrix, budget vs actuals, tenant charge-back) | B |
| Percentage rent / retail sales | ✔ (track sales, post percentage rent) | — (not on fetched page) | — | ✔ (breakpoints, sales capture, year-end reconciliation) | A (2 products) |
| Arrears / collections | ✔ (delinquencies & collections) | (payments) | (online payments) | ✔ (dedicated Arrears & Credit Control) | B |
| Work orders / maintenance w/ tenant requests & vendor assignment | ✔ (+ auto-charge tenants) | ✔ (work order management) | ✔ (+ CAM in maintenance) | ✔ (maintenance loop, mobile apps, supplier processing) | B |
| Owner accounting & reporting | ✔ (fractional ownership, pro rata statements, reserves, owner portal) | ✔ (owner portal) | ✔ (owner communication) | ✔ (landlords & investors solution) | B |
| Built-in property accounting (AR/AP/GL, trust/escrow, 1099) | ✔ (incl. escrow/trust, 1099 e-file) | ✔ (property accounting; corporate accounting in Plus) | ✔ (property accounting, 1099 e-filing) | ✔ built-in OR connected (Xero/QBO/Sage Intacct/NetSuite) + trust accounting | B |
| Budgeting / budget-vs-actual | ✔ (track budgets) | (reports) | (forecast rent revenue) | ✔ (Budget Management module) | B |
| Vacancy / leasing pipeline | ✔ (online leasing, paperless) | ✔ (end-to-end marketing & leasing; Leasing CRM in Max) | ✔ (eLeasing, syndication, screening) | (less emphasized on fetched pages) | B |
| Lease critical dates / reminders | ✔ (track lease expirations) | — | (rent increase scheduling) | ✔ (key lease events, Rent Review Hub, reminders) | B |
| Tenant portal (pay, request, documents) | ✔ (+ renew leases, retail sales data) | ✔ (portals & communication) | ✔ (resident center) | ✔ (maintenance, invoices, documents, compliance) | B |
| COI / insurance certificate tracking | — | — | ✔ (track certificates of insurance) | ✔ (insurance records via AI extraction) | A (2 products) |
| Investor relations beyond owner statements | ✔ (Investment Manager add-on: commitments/contributions/distributions) | ✔ (Investor portal; separate Investment Management product) | — | (landlords & investors framing) | A |
| Portfolio dashboards / reporting | ✔ (automated reporting; Premier custom dashboards) | ✔ (on-demand insights) | ✔ (business performance) | ✔ (Insights, dashboards) | B |
| Mobile apps | ✔ | ✔ | ✔ | ✔ | B |
| AI assistance | — (not on fetched pages) | ✔ (Realm-X AI) | ✔ (agentic AI) | ✔ (Credia Action/Extract/Advise) | B (era-common) |
| Mixed residential+commercial in one system | ✔ (multi property-type platform) | ✔ (explicit) | ✔ (explicit) | ✖ (commercial/mixed-use focus; some adjacent verticals) | B |

Reading: the invariant spine (property/space → commercial tenant/lease → lease-driven billing → collection → opex with recovery → maintenance → owner accountability) appears in all four. Depth varies: Re-Leased exposes the deepest lease-term structure; Yardi Breeze the most explicit CAM mechanics; Buildium shows commercial as a secondary capability of a residential-first platform; AppFolio shows commercial as one market of a multi-market platform.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (deliberately minimal)

A Commercial Property Management application is recognizable when all of the following exist:

1. **Managed property inventory** — income-producing commercial real estate held as properties with rentable spaces (suites/units/floor area), organized into a portfolio that is the unit of operation.
2. **Commercial tenancy under a negotiated lease** — a business tenant occupies defined space bound by a lease whose negotiated commercial terms (term length, rent schedule, escalations/reviews, recoverable charges, options) are held as structured data that drives the system's behavior.
3. **Lease-driven billing and collection** — recurring rent and charges are computed from the lease's terms, posted to the tenant's account, and tracked to payment, partial payment, or arrears.
4. **Property-level operating expense record** — the costs of operating each property are recorded against the property (the income side and expense side together form the property P&L that recovery and owner reporting depend on).

Tests:
- Remove the negotiated-lease structure (standardized consumer leases only) → Residential Property Management.
- Remove property operations (expenses, maintenance, owner accountability), keep lease + money-in → a Rent Collection / lease-billing tool, not property management.
- Remove the tenant/lease/income side, keep building operations → Facility Management / BMS territory.
- Remove the property operations, keep capital/investors → Real Estate Investment Management.
- Historical check: 1980s–90s desktop commercial PM products (and pre-software practice) already ran on property + commercial lease + rent schedule + expense recovery + owner accounting; portals, cloud, AI, built-in GL are not required for the Type to be recognizable. L0 survives the historical check.

### L1 — Common Mature Structure (standard capabilities; not definitional)

- CAM / operating-expense recovery machinery: expense pools, allocation bases, caps/percent limits, estimated charges during the year, periodic reconciliation/true-up, tenant charge-back. (Present in all four sampled products; near-universal in commercial practice, but a gross-lease-only portfolio can run without it — hence L1, not L0.)
- Escalation / rent-review automation (fixed, CPI/indexed, market review, stepped), with reminders and central review hubs.
- Lease critical-date management: expirations, renewals, options, break clauses, reminders.
- Delinquency / collections workflow (reminders, late fees, write-offs, deferrals in some products).
- Work orders / maintenance: tenant-submitted requests (portal/app, photos), vendor assignment, completion tracking, vendor invoice linkage, charge-back to tenants or recovery pools.
- Owner accounting & reporting: properties held per owner with fractional ownership, owner statements, pro-rata distributions, reserve retention, owner portals/report packets.
- Property accounting: AR/AP/GL with property-level financial statements, drill-down, escrow/trust accounts for third-party management, 1099 e-filing; alternatively delegated to connected external accounting platforms.
- Budgeting and budget-vs-actual tracking per property.
- Vacancy & leasing: availability tracking, marketing/listing, prospect pipeline, applications/screening, electronic lease execution.
- Tenant portal: balances and payment, maintenance requests, documents, (sometimes) sales reporting and compliance uploads.
- Retail sales tracking & percentage rent for retail leases.
- Insurance certificate (COI) tracking and compliance documents.
- Portfolio-level reporting/dashboards (occupancy, arrears, NOI-style performance views), mobile apps.
- Investor-relations extensions (commitments, contributions, distributions, investor portals) — common in owner/investment-adjacent products but a seam toward Real Estate Investment Management.

### L2 — Variant / Optional Structure

- Property-type mix: office / retail / industrial / mixed-use; mixed residential+commercial portfolios in one system vs commercial-only focus.
- Lease-type depth: NNN / gross / modified gross / percentage rent / ground leases; TIA amortization; co-tenancy clauses; WALE analytics (specialist depth).
- Regional vocabulary & regime: CAM (US) vs service charge (UK) vs outgoings (AU/NZ); RICS-style apportionment compliance; country-specific compliance.
- Accounting posture: built-in GL vs two-way connection to external accounting/ERP vs trust accounting for third-party managers (jurisdiction-dependent).
- Customer tier & packaging: SMB lightweight lines vs mid-market platforms vs enterprise suites; plan-tiered capability gating; standalone vs suite module.
- Operator type: third-party property manager (trust accounts, owner funds, management fees) vs owner-operator (self-managed).
- AI assistance (email-to-task, document extraction, lease Q&A) — era-common, maturity varies.
- Vertical extensions: local-government property, rural/heritage estates, healthcare, build-to-rent (specialist vendor verticals).

### L3 — Vendor-specific (research notes only)

- Yardi Breeze: Breeze vs Breeze Premier split; CommercialCafe tenant portal; Investment Manager add-on; CHECKscan/PayScan outsourced processing; per-unit pricing with minimums; menu-level security in Premier.
- AppFolio: Core/Plus/Max plan gating (CAM tracking in Core; corporate accounting in Plus; Leasing CRM/Signals/Custom Fields/Database API in Max); AppFolio Stack integrations; Realm-X AI; separate Investment Management product; unit-minimum pricing.
- Buildium: RealPage ownership; Marketplace integrations; Maintenance Contact Center; Open API gated to Premium plan; Resident Center naming; residential-first positioning with commercial as one portfolio type.
- Re-Leased: Credia AI (Action/Extract/Advise); Re-Leased Pay; RICS-compliant apportionment matrix; automatic WALE; Rent Review Hub; trust-accounting module; connected-accounting sync mechanics (event-triggered/nightly/manual); implementation as a service (4–12 weeks per its FAQ — vendor claim).

## Vendor-specific / Rejected Findings

- Re-Leased FAQ's competitor claims (residential-first products "require workarounds" for NNN) — vendor marketing; not evidence about competitors; rejected as cross-product evidence.
- Pricing figures ($/unit/month, minimums, plan thresholds) — vendor commercial terms; excluded from the canonical document.
- AppFolio "Leasing Signals", Buildium "Maintenance Contact Center", Yardi "CHECKscan" — branded modules; L3.
- "Increase NOI" / "boost profitability" marketing language — rejected from canonical prose.

## Boundary Findings

- **vs Residential Property Management** (sibling leaf): same family spine (property → tenant → lease → billing → maintenance → owner). The commercial Type is defined by business tenants under negotiated leases whose structured terms (escalations, recoverable charges, options, percentage rent) drive billing, plus opex recovery. Residential leases are largely standardized consumer instruments; billing is simpler; no CAM-style recovery. Mixed-portfolio products support both under one platform — the Type boundary is in the lease economics, not the vendor.
- **vs Lease Administration**: tenant/occupier side manages its own leases as commitments/liabilities (critical dates, obligations, ASC 842-style accounting); Commercial PM is the landlord/manager side operating income property. Same lease object, opposite economic perspective.
- **vs Rent Collection Platform**: rent collection is only the money-in slice; Commercial PM adds lease-term structure, expenses/recovery, maintenance, owner accountability.
- **vs Property Maintenance Management**: work orders are one module here; that Type makes maintenance the primary object.
- **vs Real Estate Investment Management**: capital side (acquisitions, funds, LP reporting, commitments/distributions) vs operations side. Products blur the seam via investor portals and investment add-ons (Yardi Investment Manager; AppFolio Investment Management) — evidence the seam is real and commercially significant.
- **vs IWMS / Facility Management / BMS**: occupier-side operations of buildings the organization itself uses vs landlord-side operation of income property. No tenant/lease income loop in IWMS.
- **vs HOA / Community Association Management**: assessments levied on member-owners vs rent charged to tenants under leases.
- **vs Hotel PMS**: transient nightly guests with folios vs multi-year commercial tenancies with negotiated leases.
- **vs Property Listing Platform**: public marketing of vacancies vs internal operation of the leased portfolio (PM's leasing module is the internal pipeline, not a public marketplace).
- "去掉什么就变成另一个 Type" 判据：去掉商业租约结构 → Residential PM；去掉物业运营与业主问责 → Rent Collection / Lease Administration；去掉租户与收入 → Facility Management；去掉运营只留资本 → Real Estate Investment Management。

## Uncertainties

- AppFolio's fetched commercial page does not itemize escalation/percentage-rent mechanics; its CAM detail is summary-level. Deeper AppFolio help-center articles were not fetched (URL discovery failed); AppFolio-specific claims kept at summary strength.
- Buildium's commercial documentation is thin (one portfolio page); its CAM reconciliation depth is asserted by the page but not detailed. Claims about Buildium kept at summary strength.
- Yardi Breeze Help Center article list not directly reachable (redirect to blog); CAM mechanics evidenced from the commercial-features page (still Layer A, official).
- Trust/escrow accounting regulatory specifics vary by jurisdiction; not researched in depth — kept generic.
- Lease-accounting (ASC 842/IFRS 16) integration was not observed on fetched pages; not claimed in the final document.
- Enterprise suites (Yardi Voyager, MRI) were not directly sampled; statements about the enterprise tier are contextual, not evidence-based.

## Final Synthesis

Commercial Property Management is the landlord/manager-side operating system of record for income-producing commercial real estate. Its defining spine is: a managed portfolio of properties with rentable spaces; business tenants bound by negotiated leases held as structured terms; billing computed from those lease terms and tracked to collection; operating expenses recorded against the property and commonly recovered from tenants through estimate-then-reconcile machinery; maintenance run as work orders with tenant charge-back; and owner-level accountability through statements, distributions, and portals. Around that spine, mature products add lease critical-date management, arrears workflows, budgeting, built-in or connected property accounting, vacancy/leasing pipelines, tenant portals, COI tracking, and portfolio analytics. The Type's sharpest boundary is with Residential Property Management (same family, standardized consumer leases, no recovery machinery) and with Lease Administration (the tenant-side mirror of the same lease object). The market realizes the Type both as commercial-only specialists and as commercial markets inside mixed residential+commercial platforms; both realizations share the same core model.
