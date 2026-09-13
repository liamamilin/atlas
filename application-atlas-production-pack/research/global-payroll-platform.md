# Research Notes — Global Payroll Platform

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a "Global Payroll Platform" actually is as an Application Type: what objects exist inside it, how the multi-country pay cycle flows through it, what the consolidation/orchestration layer adds beyond a single-country payroll system, what execution models exist (own engines vs in-country partners vs managed service), and where its boundaries lie against Payroll System (sibling leaf, flagged for joint review), Employer-of-Record services, HRIS/HCM, and payment infrastructure.

Context carried in from the payroll-system pass (2026-09-06): the sibling leaf flagged "payroll-system vs global-payroll-platform (sibling under §09): scope gradient, not a wall — Rippling ships 'Payroll' (US) and 'Global Payroll' as separate products while Zoho ships one payroll product as regional editions; structural test = single-jurisdiction depth vs multi-country consolidation/orchestration as the primary object; probable adjacent-Types-sharing-a-core relationship — flagged for joint review when Global Payroll Platform is processed." This pass resolves that flag.

## Initial Boundary

Initial hypothesis (to be verified, not final):

- Core: an employer-side platform that runs pay for employees in many countries — per-country statutory payroll execution plus a consolidation layer (one process, one data standard, one view) over all countries.
- The country (jurisdiction/legal entity) is likely the unit of payroll execution; the multi-country portfolio is likely the primary managed object.
- Nearest neighbors: Payroll System (§09 sibling — single-jurisdiction depth), EOR services (service model where the vendor is the legal employer), HRIS/HCM (§09 — record master), Global payments infrastructure (rails), Contractor Management / Contingent Workforce (different worker type), Accounting/ERP (downstream), Benefits Administration (deductions).
- Main unknowns: Is embedded payment execution definitional or common? Is the consolidation layer definitional or just marketing? Is employer-owned-entity operation definitional (vs EOR-style)? Do older enterprise engines (SAP/ADP-class) satisfy the same definition? Is contractor payment part of the Type?

## Research Questions

1. What is the central object — the country payroll, the global cycle, the portfolio?
2. What execution models exist for the per-country pay computation (own local engines, in-country partners/ICPs, wholly-owned offices, managed service)?
3. What does the consolidation/orchestration layer actually provide (status, standardized data, one process, consolidated reporting, funding)?
4. How does employee data flow in (HRIS/HCM integration), and how is it standardized/validated across countries?
5. How do payments work (funding, multi-currency, employees + authorities + benefit providers, status tracking, fallbacks where third-party payment is restricted)?
6. What compliance machinery exists per country (statutory computation, filings, regulatory-change monitoring)?
7. What rules matter (cut-offs/calendars, approval gating, entity/registration requirements, data protection)?
8. What interfaces exist (global dashboard, country workspaces, exception queues, payments console, analytics, self-service)?
9. Where is the boundary vs Payroll System, EOR, HRIS, payment platforms?
10. Historical check: do older enterprise multi-country payroll engines and bureau-style operations fit the same definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Philosophy / tier | Access result |
|---|---|---|
| Papaya Global | Pure-play global payroll + payments orchestration platform (aggregate-model pioneer); enterprise | Root, /global-payroll/, /what-is-global-payroll/ fetched (Tier 2 with operational FAQ) |
| Remote | EOR-platform company with in-house multi-country payroll engines (own entities/engines, no outsourcing claim); SMB→mid-market | /global-payroll + /global-hr/payroll-payments fetched (Tier 2 with operational FAQ) |
| Rippling (Global Payroll) | HCM-native platform pole; Global Payroll as a separate product line alongside US Payroll and EOR | /en-US/global-payroll fetched (Tier 2) |
| CloudPay | Managed-service global payroll platform (25+ yr payroll heritage); large enterprise (Visa/Barclays/LSEG-class customers); positions platform as the operating layer beside enterprise HCM | Root + /service/platform/ fetched (Tier 2) |
| SAP SuccessFactors Employee Central Payroll | Enterprise HCM-suite payroll engine pole (multi-country localization on one engine, natively integrated with core HR/time/finance) | Product page fetched (Tier 2); help.sap.com portal is JS-rendered — operational docs not reachable |

Considered/rejected: Deel (help.deel.com transport error; www.deel.com 403 — unreachable after 2 attempts; market context only, no claims), ADP GlobalView/Celergo (ADP unreachable in prior pass), Workday Cloud Payroll (docs behind login), Immedis/UKG and Neeyamo (aggregation specialists; docs thin/JS), SAP help portal (JS-only).

## Sources

Tier 2 (official product pages, several with operational FAQ sections; directly fetched 2026-09-07):

- Papaya Global — home: https://www.papayaglobal.com/
- Papaya Global — Global Payroll: https://www.papayaglobal.com/global-payroll/
- Papaya Global — "What is Global Payroll" guide: https://www.papayaglobal.com/what-is-global-payroll/
- Remote — Global Payroll: https://remote.com/global-payroll
- Remote — Payroll Payments: https://remote.com/global-hr/payroll-payments
- Rippling — Global Payroll: https://www.rippling.com/en-US/global-payroll
- CloudPay — home: https://www.cloudpay.net/ (redirects to cloudpay.com)
- CloudPay — Platform (Navigator): https://www.cloudpay.com/service/platform/
- SAP — SuccessFactors Employee Central Payroll: https://www.sap.com/products/hcm/employee-central-payroll.html

Source-access limitation: no product's deep help-center articles were reachable this pass (Deel unreachable entirely; Papaya support portal and SAP help portal are JS-rendered applications; Rippling help center 404 at attempted paths). All product evidence is at product-page depth, where several pages include operational FAQ sections (Papaya, Remote). Assertion strength in the final document is calibrated accordingly: cross-product structures are written as common/typical; per-product operational mechanics (exact cut-offs, exact country counts, pricing, named modules) are recorded here only.

## Product Observations

### Papaya Global (orchestration/aggregation pole)

Key observations (Layer A unless noted):

- Self-framing: "One platform. One process. One accountable partner. Manage global payroll, payments, compliance, and reporting across 180+ countries through one consolidated platform." (A, vendor claim on country count)
- Vendor's market definition: "Global payroll is the process of consolidating all payroll data streams from across the globe into one place, standardizing the data, and calculating and delivering payments across the globe in local currency in full legal compliance." Also: "What distinguishes a global managed payroll from a local payroll is the ability to carry out the necessary payroll steps for different countries simultaneously." (A)
- Product architecture: Workforce OS (payroll/EOR/COR + shadow payroll, time & attendance, workforce analytics, employee app, global benefits), Contingent OS (contractor management/classification), OnePay (payments: API, rails, wallet, split payments, virtual IBAN), OneData (single workforce data model, AI data validation, HCM/ERP connectors, payment connector, JE automation), One (compliance intelligence engine, Countrypedia country-by-country regulations). (A — branded module names are L3)
- Portfolio dashboard: cycle overview showing country payrolls by status ("182 On track, 29 Completed") and payroll analytics with total employer cost and delta. (A — screenshot on product page; numbers are illustrative)
- Vendor's own journey framing: **Plan** (connect HRIS, validate workforce data, prepare cycle) → **Process** (automated payroll calculations, AI validation, one approval workflow across every country) → **Pay** (execute employee, statutory, and vendor payments "with complete visibility from funding through delivery") → **Analyze** (analytics, automated journal entries, payroll reports, employee self-service). (A)
- Before/after framing: multiple vendors / manual reporting / fragmented data / different processes / limited visibility → one consolidated platform / one standardized process / embedded payments / real-time analytics / built-in compliance. (A)
- Three ways to run global payroll (vendor's market taxonomy): **In-house** (payroll offices in each country), **Distributed** (outsource to local experts per country — data siloed per location), **Consolidated** (unified platform + local experts, consolidated and standardized). (A)
- Two provider models (vendor's market taxonomy): **Wholly-owned model** (provider opens its own offices/entities in-country) vs **Aggregate model** (partnerships with vetted in-country partners — ICPs, "usually accounting firms or law firms" — executing payroll on the provider's platform; consolidation via platform + single-pane dashboard). Vendor argues the aggregate model gives flexibility/accountability. (A, as vendor positioning)
- Payments as "last mile": "Payments need to be made to no less than three parties (employees, tax authorities, benefits vendors), and sometimes as many as 10." (A)
- Payment scope: "We process payments to your workers and authorities, and provide detailed reconciliation reports"; payments in 130+ currencies (vendor claim); licensed payments arm (Azimo) — L3.
- Compliance built in: "Local expertise and AI continuously monitor regulatory changes"; in-country experts (Papaya Direct); dedicated payroll/compliance/implementation/account teams ("You'll never work alone"). (A)
- US coverage options: Payroll / PEO / ASO / EOR as four engagement models (A) — shows EOR and payroll as distinct services on one platform.
- Growth path guidance: "hire through an EoR and then change to regular payroll when the entity is processed"; "a workforce of 15–20 people is enough to warrant a shift from EoR to payroll" (vendor rule-of-thumb — L3).
- Challenge taxonomy (vendor's market analysis): labor laws/tax codes differ per country and per person and change without warning; data points per country in different languages/units (time & attendance, expenses, bonuses, commissions, 13th-salary norms); reporting & visibility (10 countries may mean 10 local payroll partners with data in own format/language/currency — consolidation manually "could take weeks"); payments (three+ parties); data security (GDPR/CCPA-class sensitivity); AI transparency; misclassification risk at scale. (A, as vendor market framing)
- "Global payroll reconciliation" defined: examining and aligning global payroll data; discrepancies investigated and rectified. (A)
- Shadow payroll capability (cross-border tax obligations) — L2/niche, noted for research only.
- Adjacent products on same platform: EOR, contractor management/classification, global benefits, global equity, immigration, expenses. (A — platform posture, not payroll core)

### Remote (in-house-engine pole within an EOR-ecosystem platform)

Key observations (Layer A unless noted):

- Positioning: "Pay employees in multiple countries through one platform. We handle the complex local tax and labor laws so you can run international payroll accurately and on time." Coverage claim: 100+ countries payroll, 70+ countries payments (vendor claims — L3). G2 badge: "Multi-Country Payroll" category leader — market category naming. (A)
- "100% payroll consolidation — All your payroll, HR, and expense data in one platform — no spreadsheets, no tool-switching"; "100% integrated payroll — Eliminate data fragmentation with centralized automation… goodbye to manual uploads and sync delays." (A)
- Unified multi-type workforce view: "From full-time employees in Canada to contractors in Australia, get unified visibility and control across every country, currency, and contract type. All in a single view." (A)
- Execution model: "We don't outsource payroll — we own it. With in-country experts in 100+ locations"; "native payroll engines that ensure local compliance"; "Home-grown payroll engines engineered for scale… ensures on-time payments for salaried and hourly workers alike." (A — direct counterpoint to Papaya's aggregate model)
- **Entity requirement FAQ (boundary evidence)**: "Paying employees in another country typically requires your business to: 1. Have a local business entity 2. Maintain a local business account 3. Register with local tax and labor authorities. If you don't have these, consider hiring employees through our Employer of Record service…" (A — vendor-confirmed structural split between Global Payroll and EOR)
- **Payments FAQ (operational, Layer A)**: "in some countries, Remote can automatically pay your employees and tax authorities using standard bank payment methods. Once you've completed our thorough and secure payments onboarding process, you can fund your virtual payroll wallet via bank transfer. After you approve the monthly payroll, we'll securely send payments to your employees and tax authorities in local currencies. You'll have complete visibility into the status of each payment." Also: "For all countries, you also have the option to download a 'bank file' that can be uploaded to your banking software for easy scheduling of salary, benefit, and tax payments." (A)
- Funding flexibility: "Funding multiple countries with one payment. Payments in different currencies are converted into local currencies using the Remote FX rate. Funding payroll with payment for each local currency used." (A)
- **Payment-restriction fallback**: "Some countries do not allow for third-parties to make payments to employees or authorities on behalf of an employer. In these situations, we'll work with you to create a bank file…" (A — single-source evidence for this rule; qualified in final doc)
- **US-vs-world payment nuance**: "In the US, payroll processing traditionally encompasses the calculation and distribution of payments. However, outside the US, paying (or 'disbursing' salaries and payments to authorities) are usually not included in the traditional payroll service. We offer an integrated solution that includes both payroll processing and payments." (A — important market-context finding: embedded payment execution is a differentiator outside the US, not a given)
- Compliance: Remote Watchtower — "We keep you informed automatically about changes that affect your business, including tax withholding and worker classification." In-house local payroll teams as country experts. (A)
- Controls: "Comprehensive verification processes, roles and permissions, and rigorous approval processes minimize risk"; "complete audit trail of all payroll transactions." (A)
- Pay cycle cadence evidence (customer quote): "We run monthly, semi-monthly and hourly payroll in multiple different currencies around the world and our Finance Manager has full visibility in a single platform." (A, customer testimonial)
- Pricing: $29/employee/month on one page vs $50/employee/month on another page (inconsistent across vendor's own pages — L3, do not assert).
- Implementation: "You'll be assigned a personal implementation specialist." (A)

### Rippling (HCM-native pole)

Key observations (Layer A unless noted):

- Positioning: "Pay employees and contractors around the world in a single system… Pay international employees in their local currency." (A)
- "Rippling instantly calculates and files payroll taxes for your employees worldwide." (A)
- Single-spine integration: "Sync hours, time off, deductions, and more with payroll from a single global system." (A)
- Three global engagement models listed on the page: "Global contractor payments — Hire and pay contractors globally. No entity required"; "Global Payroll via Rippling entities — Hire and pay employees globally via Rippling entities" (this is the EOR product per the vendor's own product taxonomy); "Global Payroll via your entities — Run payroll for employees globally via your own entities." (A — again vendor-confirmed EOR/payroll separation; Global Payroll proper = customer's own entities)
- Global reporting: "Monitor global compensation trends by department, location, and more, with built-in conversion to your local currency for easy comparison"; total compensation of domestic and international employees in a single system. (A)
- Permissions: "Precisely define which roles have access to payroll data and admin privileges—from approving hours worked to hitting 'Run.'" (A)
- GL sync: "payroll and expense data that's automatically categorized and synced to your general ledger." (A)
- Country-specific policy customization: "You can't customize policies by country" framed as the competitor problem — implying per-country policy configuration. (A)
- Product family split (from prior pass, reconfirmed): Payroll (US) / Global Payroll / EOR / Contractor-of-Record / Global Contractors as separate product lines. (A)

### CloudPay (managed-service unified platform pole)

Key observations (Layer A unless noted):

- Positioning: "Your global payroll, fully managed, every day"; "Global payroll, salary payments and pay-on-demand services – all delivered as managed services through a seamless, unified, global, cloud-based system"; "One operating system for end-to-end global payroll" (CloudPay Navigator). 25+ years payroll experience claim; large-enterprise customer base. (A)
- Platform framing: "a single, authoritative operating system that runs, governs, and improves every pay cycle… a single control hub for global pay management… governs every interaction from pre-payroll through to final payment – coordinating people, processes, and technology in one operating model." (A)
- Industry operating-model diagnosis: "For decades, global payroll… has been constrained by outdated operating models. Fragmented systems, disconnected payment flows, and country-by-country execution… Payroll is still run in batches. Visibility often comes too late. Issues are discovered after decisions have already been made." (A — vendor's characterization of the industry norm; useful for How It Works)
- Operating model pillars: "Orchestrates payroll and payments as one unified operating flow; Standardizes global processes across countries and entities; Automates validation…; Provides real-time insight into workflow status and exceptions; Guides users to the actions that matter, based on role and priority." (A)
- Exception-led operation: "Automated validation highlights what needs attention; Immediate click-through to the tasks requiring action; Prioritized to-do alerts guide action; Faster resolution without system switching." "You act by exception – not exhaustion." (A)
- Real-time visibility: "Live workflow status and progress tracking provide a clear, always-current view of where every payroll and payment stands – no reconciliation required." (A)
- Audience segmentation: payroll practitioners (tasks/status/exceptions), payroll leaders (governance/resourcing/planning), finance + business leaders (risk/control/planning). (A)
- Position vs HCM: "providing the unified payroll and payments operating layer that HR and finance systems don't deliver on their own" — payroll as the operating layer alongside enterprise HCM (Workday/Oracle/HiBob/SAP partnerships). (A)
- Integration: real-time bi-directional HCM integrations (Workday, Oracle); self-onboarding tool (Onboardify) — L3 names. (A)
- Automation: "driving automation across the entire payroll-to-pay cycle"; payslip splitting, bulk payslip generation (2024 automations) — L3. CloudPai AI reconciliation — L3. (A)
- Analytics: built into platform — real-time insights, benchmarking. Uptime claims (99.99%) — L3. (A)
- Three solution pillars: Payroll / Payments (with Payments Dashboard) / Pay On-Demand (earned wage access — L2 adjacency). (A)

### SAP SuccessFactors Employee Central Payroll (enterprise suite-engine pole)

Key observations (Layer A unless noted):

- Positioning: "Deliver accurate, on-time payroll globally with a trusted solution offering AI-powered experiences"; "flagship solution that simplifies and scales payroll operations with prebuilt integrations." (A)
- Localization coverage: "Compliance with local regulations and tax laws in 60 countries" (vendor claim — L3 number; confirms per-country localization as the structural mechanism for a suite engine). (A)
- Continuous payroll: "Continuous payroll with real-time processing, anomaly detection, and guided resolution"; FAQ: "Continuous payroll allows monitoring and automated validation of payroll data as soon as changes are made. It shifts payroll from a batch-mode process at the end of the pay period to a real-time, ongoing model that enables continuous simulation and minimizes payroll errors." (A — single-source concept; batch is the industry norm per CloudPay's diagnosis)
- Native integration: "Natively integrated solutions for core HR, benefits, time, payroll, and finance"; single-vendor benefit: "integrated, standardized processes… improves payroll speed and accuracy… aligns payroll with finance for better reporting." (A)
- Payroll Control Center dashboard (product hero) — monitoring/control surface for payroll operations. (A)
- AI agents (2026 release): Payroll Explanation Agent, Payroll Alert Resolution Agent, Payroll Validation Rule Agent, Employee Data Integration Agent — L3. (A)
- Market category evidence: product listed under SAP's HCM suite; customers cited for "standardized global payroll" and "global workforce… compliance with international laws." (A)

## Cross-product Comparison

| Structure | Papaya | Remote | Rippling | CloudPay | SAP ECP | Assessment |
|---|---|---|---|---|---|---|
| One employer operating pay across many countries (customer holds entities/registrations) | yes (entity-based payroll; EOR separate product) | yes (entity requirement FAQ explicit) | yes ("Global Payroll via your entities") | yes (employer-side managed pay) | yes (suite run for the customer's own workforce) | **L0** |
| Country (jurisdiction/entity) as the unit of pay execution under local statutory machinery | yes (local experts/ICPs per country; per-country processing) | yes ("native payroll engines… local compliance"; in-country experts) | yes (country-specific policies; taxes filed "worldwide") | yes ("country-by-country execution" being unified; standardization across countries and entities) | yes (per-country localization — 60-country claim) | **L0** |
| Consolidation/orchestration layer over all countries (one process, standardized data, unified status/costs) | yes ("one platform, one process"; consolidated view; standardized data) | yes ("100% payroll consolidation"; single view across countries/currencies) | yes (single system; global reports with currency conversion) | yes ("single control hub"; "standardizes global processes"; live status) | yes (one engine + prebuilt integrations; Control Center) | **L0** (the distinguishing layer vs a set of local payrolls) |
| Pay delivered in local currency; payment execution orchestrated/executed by platform or partners | yes (platform pays workers+authorities; "last mile" framing) | yes (virtual wallet, disbursement, status tracking; bank-file fallback) | yes ("pay in their local currency"; tax filing) | yes (payments as unified operating flow; Payments Dashboard) | implied via suite (payments not headlined on page — evidence weak) | **L0 as delivery/orchestration of pay** (direct execution depth is L1/L2; SAP page under-evidences it) |
| Durable per-country pay records + consolidated reporting/audit | yes (reconciliation reports, JE automation, analytics) | yes (audit trail of all payroll transactions) | yes (GL sync; global comp reports) | yes (analytics, benchmarking, audit-grade assurance framing) | yes (payroll + finance alignment for reporting) | **L0** (inherited payroll core: records; consolidation adds the cross-country roll-up) |
| HRIS/HCM integration as the workforce data source | yes (OneData connectors, HCM/ERP mapping) | yes (HR Core included; integrations) | yes (single employee spine) | yes (HCM partnerships; bi-directional integrations) | yes (native core-HR integration) | **L1** |
| Statutory compliance machinery per country (computation, filings, regulatory monitoring) | yes (compliance engine, Countrypedia, local experts monitoring changes) | yes (Watchtower alerts; local tax handling) | yes (files taxes worldwide) | yes (compliance service; country payroll guides) | yes (localization; local regulations/tax laws) | **L1** (inherited core obligation, expressed per country) |
| Embedded global payments layer (funding → multi-party disbursement → status) | yes (OnePay; workers+authorities+benefit vendors) | yes (virtual payroll wallet, FX, status per payment) | partial (payments implied; local currency pay) | yes (payments as one unified flow; Payments Dashboard) | not evidenced on page | **L1** (common and heavily marketed; SAP page under-evidences it; US-vs-world nuance shows it is a differentiator, not a given) |
| Multi-party payment targets (employees, tax authorities, benefit providers) | yes (three parties minimum claim) | yes (employees + tax authorities; benefits providers on payments page) | not explicit | yes (payroll and payments unified) | not evidenced | **L1** (two strong sources; part of the payments layer) |
| Unified/global approval workflow and permission gating before money moves | yes ("one approval workflow across every country") | yes ("rigorous approval processes", roles/permissions) | yes (role-based "Run" permission) | yes (role-and-priority-guided action; governance) | yes (implied via Control Center; not explicit) | **L1** (inherited payroll control, expressed globally) |
| Data standardization/validation machinery | yes (AI data validation) | yes (centralized automation; verification processes) | yes (sync automation) | yes (automated validation, exception queues) | yes (anomaly detection; validation-rule agent) | **L1** |
| Consolidated analytics/JE-to-GL handoff | yes (JE automation, cost analytics) | yes (accounting sync; audit trail) | yes (GL sync, cost comparison) | yes (analytics, benchmarking) | yes (payroll-finance alignment) | **L1** |
| Employee self-service (payslips/app) | yes (employee app) | not headlined on fetched pages | not headlined on fetched page | yes (CloudPay App; payslip automations) | yes (Explain Pay for employees) | **L1** |
| Human expert service layer (in-country experts, implementation specialists, managed pay) | yes (Papaya Direct, dedicated teams) | yes (in-country experts; implementation specialist) | not headlined | yes ("fully managed"; managed pay services) | partner-delivered (not headlined) | **L1/L2** (posture varies: software vs managed service) |
| Exception-led operating model (validation → prioritized exceptions → guided resolution) | partial (AI validation) | partial (verification) | not explicit | yes (core Navigator concept) | yes (anomaly detection, guided resolution, alert-resolution agent) | **L1→L2** (strong at two sources, present in spirit elsewhere; modernization-era framing) |
| Batch vs continuous processing | batch-cycle framing (cycle overview) | monthly/semi-monthly runs (customer quote) | not explicit | batch is the norm being replaced ("Payroll is still run in batches") | continuous payroll (real-time) as differentiator | **L2** (continuous = single-source differentiator; batch is the industry-norm rhythm) |
| Execution model: own local engines vs in-country partner network vs managed service vs suite module | aggregate model (ICPs) — vendor also describes wholly-owned as the alternative | own in-house engines ("we don't outsource") | own platform + Rippling entities (EOR) or customer entities | managed service on unified platform | suite module (customer runs with implementation partners) | **L2** (the market's main philosophy split) |
| Workforce mix: employees only vs + contractors | + contractors (Contingent OS) | + contractors (single view across contract types) | + contractors | employees (pay on-demand for workforce) | employees | **L2** (contractor payment is a common adjacency, not the core) |
| EOR on the same platform | yes | yes | yes | no | no | **L2** (platform-posture difference; structurally separate service) |
| Shadow payroll, pay-on-demand, equity, immigration, benefits | shadow payroll; benefits; equity; immigration | benefits; equity; mobility | benefits; equity | pay on-demand | benefits | **L2** (adjacent capabilities vary) |
| Country-coverage breadth claims | 180+ | 100+ (payroll) / 70+ (payments) | not stated on page | "0+" JS-animated (unreadable) | 60 | L3 (vendor claims; do not assert) |

Convergence summary (Layer B): all five products implement the same spine — one employer paying an employed workforce across many countries, where each country's pay is computed and executed under that jurisdiction's statutory machinery (by own engine, in-country partner, or managed operations), while the platform's distinctive layer standardizes the process, consolidates the data/status/costs across countries, gates the cycle behind unified review/approval, and (commonly) executes or orchestrates the funding and multi-party disbursement. The per-country payroll inherits the Payroll System core (pay records → cycle → gross-to-net → payment → records); the global layer is the portfolio management and consolidation machinery around those country payrolls.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

1. **One employer's multi-country pay operation** — a single employing organization operates pay for its employed workforce across multiple country jurisdictions, in which it holds (or establishes) the local entities/registrations that make it the legal employer. (If the vendor becomes the legal employer, that is EOR — a different service model.)
2. **Country-scoped pay execution under local statutory machinery** — for each country/entity, the pay cycle runs against that jurisdiction's rules: local gross-to-net computation, local statutory withholdings/filings, local payment norms, local payslip/statutory outputs. The country payroll is the recurring unit of execution.
3. **A consolidation/orchestration layer over the country payrolls** — the platform manages the country payrolls as one portfolio: a standardized process and workflow across countries, standardized/validated data, unified status visibility, consolidated cost and reporting (with currency normalization), and unified control (approval before money moves).
4. **Pay delivery completed in each country + durable consolidated records** — pay reaches workers in local currency (executed directly by the platform, by local partners, or completed through employer-executed payment files under the platform's orchestration), and the operation leaves durable records: per-country statutory records plus consolidated cross-country reports.

Remove any one and the Type collapses: without (1) it is a Payroll System (or several disconnected ones); without (2) it is a payments platform or a compliance content service, not payroll; without (3) it is the "distributed" market pattern (many local payroll vendors with no global management structure — explicitly not a platform); without (4) it is payroll computation/reporting consultancy rather than the system that gets people paid and keeps the record.

Deliberately **not** in L0 (tested and demoted):

- **Embedded payment execution by the platform itself** — Remote documents direct execution; Remote also documents the bank-file fallback where jurisdictions restrict third-party payment; the US-vs-world market note ("outside the US, paying… usually not included in the traditional payroll service") shows payment execution is a differentiating layer, not a given. Delivery/orchestration of pay is L0; direct disbursement machinery is L1/L2.
- **Virtual wallets, FX engines, payment rails** — implementation of the funding layer. → L1/L2.
- **HRIS/HCM integration** — universal in the sample but a data-source relationship, not the defining structure. → L1.
- **Compliance-change monitoring, in-country experts, managed services** — service/compliance depth. → L1/L2.
- **Contractor payment, EOR, benefits, equity, shadow payroll, pay-on-demand** — adjacent capabilities commonly bundled. → L2.
- **Continuous/real-time payroll, AI agents, exception-led consoles** — current-era modernizations over the batch-cycle norm. → L2.
- **Cloud dashboards** — the surface, not the structure; enterprise engines and bureau-era operations satisfy the L0 without them (see historical check).

### L1 — Common Mature Structure

- HRIS/HCM integration as the workforce data source (connectors/mapping; single-spine in suite products), with data standardization and validation machinery across countries
- per-country statutory compliance machinery: local computation rules, filings, statutory outputs; regulatory-change monitoring with alerting (two+ sources)
- embedded global payments layer: funding (wallet/funding accounts, FX conversion), disbursement to employees, tax authorities, and commonly benefit providers, per-payment status visibility (two strong sources; SAP page under-evidences)
- unified approval workflow and role-based permissions across countries before money moves
- consolidated reporting/analytics: global cost in a chosen reporting currency, per-country breakdown, benchmarking; journal-entry automation to GL/ERP
- payroll calendar management across staggered country cycles with per-country cut-offs
- exception management: automated validation, prioritized exception queues, guided resolution
- employee self-service (payslips, app) and payslip generation/splitting
- human expert layer: in-country payroll/compliance experts, implementation/onboarding specialists; managed-pay service posture in part of the market
- audit trail across the payroll-to-pay cycle

### L2 — Variant / Optional Structure

- execution model: provider-owned local engines vs in-country partner (ICP) network vs wholly-owned local offices vs managed service vs suite software the customer operates — the market's main philosophy split
- platform posture: pure-play global payroll/payments platform vs EOR-ecosystem product vs HCM-native product line vs enterprise HCM-suite payroll engine
- workforce mix: employees only vs employees + contractors (contractor payment as bundled adjacency)
- EOR on the same platform (three of five sampled products; structurally separate service)
- processing posture: batch country cycles (industry norm) vs continuous/real-time payroll (single-source differentiator)
- country-coverage breadth (vendor claims from dozens to 180+; do not assert numbers)
- adjacent capabilities: global benefits, equity, immigration, expenses, shadow payroll, pay-on-demand/earned wage access, worker classification
- service depth: self-service software vs high-touch managed service with dedicated teams
- regional nuances: US multi-state machinery as a "country-like" jurisdiction; regimes with wage-protection rails or 13th-salary norms

### L3 — Vendor-specific (stays in Research Notes)

- Papaya: Workforce OS / Contingent OS / OnePay / OneData / One module names; Countrypedia/Paymentspedia; Banco wallet; virtual IBAN; split payments; Azimo licensing; Papaya Direct; "182 on track / 29 completed" illustrative dashboard; 15–20-worker EOR→payroll rule-of-thumb; 130+ currencies / 180+ countries claims
- Remote: Watchtower; IP Guard; virtual payroll wallet; Remote FX rate; "we don't outsource" posture; G2 "Multi-Country Payroll" badge; 100+/70+ country claims; inconsistent $29 vs $50 pricing across own pages; personal implementation specialist
- Rippling: three-model global structure (contractors / Rippling entities / your entities); single employee spine; Workflow Studio permissions framing; $8/user starting price claim
- CloudPay: Navigator operating system; CloudPai AI; Onboardify; Payments Dashboard; Pay On-Demand + CloudPay App; payslip splitting/bulk generation; 99.99% uptime claims; "High-Performance Payroll People" positioning
- SAP ECP: Payroll Control Center; 60-country localization claim; continuous payroll; four named payroll agents (Explanation/Alert Resolution/Validation Rule/Employee Data Integration); 64%-error-reduction IDC claim

## Rejected Findings

- **"Global payroll = EOR + payroll + contractors in one definition"** — rejected as a Type definition. Papaya's total-workforce framing ("the definition of a multi-country payroll is the same regardless of whether a company has an entity… or hiring independent contractors") reflects one vendor's platform posture. Both Rippling and Remote structurally separate EOR from Global Payroll (entity requirement), and the payroll core of the Type is the employed workforce under the customer's own entities. Contractor payment = common adjacency (L2); EOR = different service model.
- **"Payment execution by the platform is definitional"** — rejected. Remote's own docs show bank-file fallback where jurisdictions restrict third-party payment, and note that outside the US payment execution is traditionally not part of payroll service. Delivery of pay is L0; the disbursement machinery is L1/L2.
- **"Global payroll = a dashboard over local payrolls"** — rejected as too weak. The consolidation layer includes process standardization, data standardization/validation, unified approval and control — not just visibility. (CloudPay explicitly distinguishes its model from "a dashboard layered on top of existing systems".)
- **"One unified global pay run"** — rejected. All evidence shows country-scoped execution (per-country engines, localizations, ICPs, calendars); "global" lives in the consolidation/control layer, not in a single worldwide computation.
- **"Continuous/real-time payroll is the new core"** — rejected (single source; batch country cycles remain the industry norm per CloudPay's own diagnosis). L2.
- **"Coverage breadth defines the Type"** — rejected. Country-count claims are vendor marketing (L3); the structure is country-scoped execution + consolidation regardless of breadth.

## Boundary Findings

1. **vs Payroll System (sibling leaf, §09) — RESOLVES the flagged joint-review issue.** The two Types are adjacent and share the payroll core (pay records → cycle → gross-to-net → payment → records). The distinguishing structure is the object of management: a Payroll System's primary object is the pay run under one (or few) jurisdiction(s) with deep local statutory machinery owned in one place; a Global Payroll Platform's primary managed object is the **multi-country payroll portfolio** — country payrolls as coordinated units plus the consolidation/orchestration layer (standardized process, unified status/data/costs, multi-currency funding) over them. Vendor-confirmed separations: Rippling ships Payroll (US) and Global Payroll as separate product lines; Papaya, Remote, and CloudPay are distinct products from any single-country payroll; Zoho's regional-edition pattern (one product family, one jurisdiction per edition) sits on the Payroll System side. Structural tests: remove multi-country scope → Payroll System; remove the consolidation layer → a set of disconnected local payrolls (the market's "distributed" pattern, which is precisely what the Type exists to replace); make the vendor the legal employer → EOR. **Recommendation: keep both Types as adjacent-Types-sharing-a-core; boundary = scope + the consolidation layer as primary object.** (Joint-review flag resolved; see STATUS.md.)
2. **vs Employer-of-Record (EOR) services** — the sharpest structural boundary: EOR = the vendor is the legal employer (no customer entity needed); Global Payroll = the customer is the legal employer (entities/registrations required). Direct evidence: Remote's entity-requirement FAQ routing entity-less employers to EOR; Rippling's "via your entities" (payroll) vs "via Rippling entities" (EOR) split; Papaya selling EOR and Global Payroll as separate products with a documented migration path (EOR → own entity → payroll). EOR platforms commonly bundle global payroll for customers' entities — same platform, different structures.
3. **vs HRIS / HCM (§09)** — the HRIS holds the worker master; global payroll consumes it per country (all five products integrate; suite products natively). CloudPay positions the payroll platform as "the unified payroll and payments operating layer that HR and finance systems don't deliver on their own" — a coexistence claim, not a merger. Test: remove pay execution/consolidation → HRIS remains.
4. **vs Global payments infrastructure / Payment Processing Platform (§08)** — the payments layer inside global payroll is purpose-built for workforce obligations: recurring, computed, compliance-bound, multi-party (employees, authorities, benefit vendors), multi-currency with funding-fronting mechanics. It is not merchant card acquiring nor P2P payments. Where the product's center of gravity is pure payment rails with no pay computation, that is payment infrastructure, not payroll.
5. **vs Contractor Management / Contingent Workforce Management (§10)** — contractor engagement/classification is a different worker type with its own compliance logic; global payroll products commonly add contractor payment as adjacency (three of five sampled products), but the payroll core is employed workers under local employment law.
6. **vs Accounting/ERP (§08) and Benefits Administration (§09)** — downstream/upstream integrations (JE automation into GL; benefit deductions applied in country runs); same producer→consumer relationships as the Payroll System Type, expressed across many countries.
7. **Time & Attendance (§09)** — input provider per country (hours, absence); not definitional (same result as the payroll-system pass).

## Historical / Market-Sample Check

- **Enterprise multi-country payroll engines (pre-cloud lineage)**: multinational payroll products that run country-localized payroll versions on one engine/one operations model, feeding consolidated HQ reporting, existed for decades (SAP-class payroll engines with country versions; ADP-class global payroll offerings — the latter unreachable, reasoned from category structure). These satisfy L0: one employer, country-scoped statutory execution, consolidation layer, delivered pay + records — with none of the modern wallet/AI/exception-console surfaces. ✓ (SAP ECP is the directly observed modern descendant; the historical shape is inferred from the structure, not asserted as specific product facts.)
- **Bureau/outsourced era**: multinationals coordinating many local payroll bureaus with HQ consolidation-by-spreadsheet correspond to the market's "distributed" pattern — Papaya's own taxonomy names it as the pre-platform state the Type replaces; it lacks the consolidation layer and therefore is not the Type, which supports (3) being definitional rather than incidental. ✓
- **Regional check**: the L0's "local statutory machinery" phrasing keeps any regime inside the definition (wage-protection rails, 13th-salary norms, US multi-state as jurisdiction-like). ✓
- **Platform-native check**: the same core appears as suite module (SAP), standalone platform (Papaya/CloudPay), EOR-ecosystem product (Remote), HCM-native product line (Rippling) — packaging does not change the structure. ✓
- Conclusion: L0 does not over-fit the current cloud orchestration era; the consolidation layer, not the dashboard, is the historical differentiator.

## Uncertainties

1. No Tier-1 help-article-level documentation was reachable for any sampled product this pass; all evidence is product-page depth (with operational FAQs on two products). Step-by-step mechanics (exact data-collection deadlines, per-country run state machines, file formats) are therefore not asserted anywhere.
2. Deel — a major EOR-ecosystem competitor — was unreachable (403/transport error); its structures are not claimed. The EOR-pole evidence rests on Remote alone; the pole's commonality with Papaya/Rippling on platform bundling reduces the risk, but Deel-specific mechanics are unknown.
3. SAP EC Payroll's payments depth (whether the suite executes disbursement or produces payment files) is not evidenced on the fetched page; the final document keeps payment-delivery (not direct execution) in the core for this reason.
4. The bank-file fallback for jurisdictions restricting third-party payment is single-source (Remote); treated as a qualified pattern ("some products"), though it is consistent with Papaya's own "how do you process international payroll" outsourcing framing.
5. Papaya's aggregate model (ICPs) is the vendor's own account of its delivery network; the balance between ICP-executed and platform-executed work per country is not directly observable.
6. Whether any current product runs multi-country pay without any per-country scoping (a literal single global pay run) was not observed and is believed not to exist given statutory localization; if found, it would challenge L0 item 2's phrasing.
7. Pricing figures across vendors were inconsistent or JS-animated; no pricing is asserted.
8. Contractor-payment depth varies (payment-only vs management/classification); the boundary to Contractor Management Types deserves its own pass.

## Final Synthesis

A Global Payroll Platform is the employer-side system that operates and consolidates pay across countries: **one employer's multi-country pay operation → country-scoped pay runs executed under each jurisdiction's statutory machinery (by the platform's own engines, in-country partners, or managed operations) → a consolidation/orchestration layer that standardizes the process, validates and unifies the data, provides unified status and control (approval before money moves), consolidates costs and reporting across currencies, and commonly executes or orchestrates funding and multi-party disbursement (employees, tax authorities, benefit providers) → per-country statutory records plus consolidated cross-country reporting**. Around this core, mature products add HRIS integration, per-country compliance monitoring, payments/funding machinery, exception management, employee self-service, and a human expert layer. The market's main splits are the execution model (own engines vs partner aggregation vs managed service vs suite module), the platform posture (pure-play vs EOR-ecosystem vs HCM-native vs enterprise suite), and service depth. The boundary with Payroll System is scope-plus-object (single-jurisdiction depth vs the multi-country portfolio as the managed object); the boundary with EOR is who the legal employer is. The joint-review flag from the payroll-system pass is resolved in favor of keeping both Types adjacent with a shared core.
