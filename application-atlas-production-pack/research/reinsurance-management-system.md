# Research Notes — Reinsurance Management System

Research date: 2026-09-10
Slug: reinsurance-management-system
Leaf: Reinsurance Management System (§08 Finance, Banking, Insurance & Investment)
Sibling context: insurance-policy-administration-system (processed 2026-09-07) records this leaf as "treaty-side sibling — ceded/assumed reinsurance business between insurers; this Type administers direct policies sold to policyholders". insurance-underwriting-platform / underwriting-workbench (processed) record reinsurance underwriting as a use-case surface of the underwriting Type. actuarial-modeling-platform (processed) treats reinsurance as a management action inside models.

## Research Goal

Understand, from real products, what a Reinsurance Management System is: what the central objects are (reinsurance agreements/treaties, cessions, bordereaux, recoverables, settlements), how the ceded side (an insurer passing risk to reinsurers) and the assumed side (a reinsurer taking risk from cedents) are supported, what financial machinery the system carries, how it connects to policy administration and claims systems, and where its boundary lies against policy administration, claims, broking, and actuarial software.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the system of record for reinsurance business — the insurance that insurance companies buy and sell among themselves. Two sides: ceded (cedent/insurer manages its reinsurance program: treaties, facultative placements, cessions of premium/claims, bordereaux, recoverables, settlements) and assumed (reinsurer manages inwards treaties and the business inuring under them).
- Nearest neighbors: Insurance Policy Administration System (direct policies vs reinsurance agreements), Insurance Claims Management (loss lifecycle vs recovery side), Broker Management Platform (placement vs administration), Actuarial Modeling Platform (models vs contractual/financial record), Insurance Underwriting Platform (assumed-side treaty underwriting exists as a separate decision surface).
- Inherited flags to discharge:
  - PAS pass: "Reinsurance Management System | treaty-side sibling" — confirm the seam from this side.
  - Claims pass: reinsurance recoverable booking noted as not directly evidenced — check what reinsurance systems do with claims.
  - Underwriting passes: reinsurance underwriting (Send for Reinsurance Underwriting) is decision machinery; confirm the administration system is a different object.

## Research Questions

1. What is the central contract object (treaty, facultative certificate) and what does it carry (scope, share/limits/attachment, commissions, period, status)?
2. What is the unit of allocation (cession / inuring business) and how is it computed (premium cessions, loss cessions, recoveries)?
3. What financial machinery exists: technical accounts, bordereaux, balances, cash management, settlements, credit control?
4. How does the ceded flow work end to end (policy data in → allocation → bordereaux out → settlement)?
5. How does the assumed flow work (treaty accepted → inuring business in → accounting → settlement)?
6. What claims-side machinery exists (reinsurance claims, events, hours clauses, recovery maximization)?
7. What regulatory/statutory reporting is produced (Schedule F, IFRS 17, annual statement links)?
8. What contract lifecycle states exist (creation, negotiation, signed, run-off, commutation, renewal)?
9. Which capabilities are definitional vs common vs variant vs vendor-specific?
10. Where is the seam against policy administration, claims, broking, and actuarial software?

## Representative Products

| Product | Vendor | Positioning | Why sampled | Sources used |
|---|---|---|---|---|
| ReinsurancePro | Sapiens | Dedicated cloud reinsurance management system for P&C carriers; ceded + assumed + retroceded; treaty + facultative; "market leader with highest global deployments" (self-claimed); Celent Functional Standout | Dedicated-system pole; ceded+assumed breadth | Product page (fetched), Microsoft Marketplace listing (fetched via search), brochure PDF (search-indexed) |
| ReinsuranceMaster | Sapiens | "Comprehensive single platform for large and multi-national reinsurance programs"; multi-country/multi-currency/intercompany; London Market requirements | Large/multi-national pole of the same vendor family | Product page (fetched) |
| Duck Creek Reinsurance | Duck Creek Technologies | "Beyond Core" reinsurance management module on the Duck Creek Intelligent Core; ceded + assumed + retroceded; four pillars: Contract & Partner Management, Claims, Accounting, Reporting; QBE reference customer (both ceded and assumed) | Suite-module pole; contract lifecycle detail | Product page (fetched), brochure + data sheet PDFs (search-indexed), launch blog + press release (search-indexed) |
| Sequel Re | Verisk Specialty Business Solutions (formerly Sequel) | "End-to-end outward reinsurance system for Lloyd's syndicates and London Market insurers"; real-time calculation engine; imports policy/premium/claims via APIs | Regional (London Market) ceded-side pole; standalone + suite deployment | Product news article (fetched), products page (fetched) |
| SolveXia | SolveXia (GTreasury group) | Finance-process automation platform applied to reinsurance: centralized treaty tables, bordereau calculations, reinsurance recoveries; life + general insurance case studies | Automation/thin pole — shows which structures are load-bearing | Financial-services solution page (fetched), case studies (search-indexed) |

Selection covers: dedicated system vs suite module vs regional specialist vs automation overlay; ceded-only vs ceded+assumed; P&C vs life; North America vs London Market.

## Sources

Fetched directly (A-layer):

- Sapiens ReinsurancePro product page — https://sapiens.com/us/reinsurance/reinsurancepro/
- Sapiens ReinsuranceMaster product page — https://sapiens.com/us/reinsurancemaster/
- Duck Creek Reinsurance product page — https://www.duckcreek.com/product/reinsurance/
- Verisk Specialty Business Solutions — Sequel Re v5 news article — https://www.verisksequel.com/news/latest-sequel-re-upgrade-enhances-competitive-advantages-for-lloyd-s-london-market-underwriters/
- Verisk products page — https://www.verisksequel.com/products/
- SolveXia financial services page — https://www.solvexia.com/solutions/financial-services

Search-indexed official documents (quoted verbatim by the search layer from official vendor domains; treated as A-layer with a note):

- Sapiens ReinsurancePro — Microsoft Marketplace listing — https://azuremarketplace.microsoft.com/en-us/marketplace/apps/sapiens.sapiensreinsurancepro?tab=overview (feature list: treaties for ceded/assumed/retroceded/pools/affiliates; attachment/calculation/posting of premium and loss cessions; per-risk/per-occurrence/proportional/catastrophe recoveries; reinsurance claims with billing/FNOL/status letters; interfaces to policy, premium, claims, GL, annual statement)
- Sapiens ReinsurancePro brochure PDF — https://sapiens.com/wp-content/uploads/2025/03/DS_ReinsurancePro-June24.pdf (linked from product page; not fetched)
- Duck Creek Reinsurance Management brochure 2024 — https://www.duckcreek.com/wp-content/uploads/2024/06/20013_DuckCreek_Brochure_Reinsurance_Management_2024.pdf (contract lifecycle: creation, pending negotiations, signed, run-offs, commutations; renewal by copying conditions; cession technical accounts and bordereaux; hours clause; placement simulations; audit trail)
- Duck Creek Reinsurance data sheet 2023 — https://www.duckcreek.com/wp-content/uploads/2023/01/Reinsurance_Data-Sheet.pdf (ceded/assumed/retroceded; treaties, facultative, fac-ob, proportional and non-proportional; covers: excess loss, stop loss, quota share, surplus, XS aggregate; cession calculations and recoverables tracking; ad hoc and Schedule F reporting)
- Duck Creek launch blog + press release (April 2026) — Active Delivery; recoverables; billing/tracking automation
- SolveXia case studies — reinsurance bordereaux (life), reinsurance recoveries, reinsurance and commission calculations — https://www.solvexia.com/case-study/reinsurance-bordereaux , https://www.solvexia.com/case-study/insurance-reinsurance-recoveries , https://www.solvexia.com/case-study/reinsurance-and-commission-calculations

Not fetched / not reachable:

- Duck Creek brochure PDF attempted directly; returned raw PDF binary (not parseable). Content taken from the search layer's verbatim quotation of the official-domain PDF. No retry per network rule.
- No in-product help centers or user guides were reachable for any sampled product (enterprise software; documentation gated). All workflow detail below is calibrated to product pages, official PDFs via search extraction, and vendor case studies.

## Product Observations

### Sapiens ReinsurancePro (dedicated system; ceded + assumed)

Key observations (A unless noted):

- Self-positioning: "cloud-based reinsurance management system for P&C carriers, managing all types—ceded, treaty, facultative—from contract definition through statutory reporting"; "market leader with highest global deployments" (self-claim, marketing).
- Scope statement: "automate the underwriting and administration of reinsurance, including treaty and facultative, ceded, assumed and retroceded reinsurance."
- Feature list (Marketplace listing, A): "Manages treaties for ceded, assumed, retroceded, pools and affiliates"; "Automates attachment, calculation, and posting of premium and loss cessions and retrocessions"; "Identifies and calculates per risk, per occurrence, proportional, and catastrophe loss recoveries"; "Manages reinsurance claims with customized billing, first notice of loss, and status request letters."
- Calculation engine: "powerful calculation engine handles complex contract terms while maintaining complete data integrity."
- Recoveries: "accurately tracks claims to maximize recoverables"; "reviews every claim against your contracts, finds those hidden recoveries" (claims-leakage framing).
- Accounting: "Supports reinsurance accounting and cash management"; interfaces "directly with core systems" — policy, premium, claims, general ledger, annual statement software (Marketplace listing).
- Statutory reporting: "One-click Schedule F generation"; "handles NAIC and international standards like IFRS 17 compliance, and maintains audit trails."
- Reporting: "Broad reporting capabilities available for any data stored in a single repository" — single data repository framing.
- Analytics: "'What-if' analysis to gain insights on contract terms impacting rate negotiations"; "data analytics to achieve objectives in enterprise risk management."
- Anti-spreadsheet framing: "eliminates manual processes and spreadsheets by automating premium/loss calculations, claims recoveries, and contract allocations."
- Case study (search-indexed PDF): specialty insurer consolidated treaty setup, intercompany treaties, multi-dimensional claims calculations, approval at policy level, reporting at multiple levels on one system.

### Sapiens ReinsuranceMaster (large/multi-national pole)

Key observations (A):

- Positioning: "Comprehensive single platform for large and multi-national reinsurance programs, providing full financial control and flexibility across all lines of business."
- "handle all reinsurance activities on a single platform… comprehensive in-depth business functionality for all types of programs and calculations."
- "streamlines integrated workflows across all contract types with complete audit trails, LORS integration, GL accounting, multicurrency and intercompany support and business analytics."
- "Multi-country and multi-currency functionality"; "Full support of auditing and statutory compliance requirements."
- "Consolidated view of liabilities and risks"; "Comprehensive data repository"; "Essential KPIs to support decision-making."
- Integration: "Standard interfaces to policy and claims applications"; "Native integration with document management systems"; "Meets London Market requirements."
- Celent Ceded Reinsurance Solutions Global 2023: "Luminary for Advanced Technology and Breadth of Functionality" (award framing).

### Duck Creek Reinsurance (suite module; ceded + assumed)

Key observations (A unless noted):

- Positioning: "BEYOND CORE | reinsurance management software"; "enterprise-grade reinsurance platform built on Duck Creek's Intelligent Core"; purchasable standalone, à la carte, or in suite (FAQ).
- Four named pillars: **Contract and Partner Management**, **Claims**, **Accounting**, **Reporting**.
- Contract & partner management: "single source of truth for treaties, facultative agreements, ceded, assumed, and retroceded programs"; "Manage complex reinsurance relationships effortlessly across cedants, reinsurers, brokers, legal entities, and program structures at scale"; "Support treaties, facultative, proportional, and non-proportional programs across lines of business"; "Accelerate renewals… by adapting existing contracts and carrying forward terms, conditions, and structures consistently year over year"; "Understand program structures, layers, and financial positions in one clear view."
- Claims: "See every claim with full lifecycle visibility"; "Connect claims, events, and timelines in one place"; "Ensure accurate recoveries automatically by applying contract terms and clauses without manual effort"; (blog) "automatically determines the optimal period for retroceded amounts through an hours clause."
- Accounting: "Automate reinsurance accounting with built-in intelligence to ensure accurate, audit-ready financials across every partner and program"; "automatically applying complex premiums, claims, and commissions"; "managing all account types, currencies, and regulatory requirements in one system."
- Reporting: "accurate, automated regulatory reporting delivered on time"; powered by Duck Creek Clarity data foundation.
- Contract lifecycle (brochure PDF via search, A-with-note): "supports contract creation, pending negotiations, signed contracts, run-offs and commutations on one or several legal entities"; "A reinsurance contract can be renewed instantly by copying and pasting all conditions from one underwriting year to the next"; "automatic generation of cession technical accounts and bordereaux for premiums and claims"; "placement simulations"; "comprehensive support for all auditing requirements and statutory compliance."
- Contract types (data sheet PDF via search, A-with-note): "treaties, facultative reinsurance, fac-ob, proportional and non-proportional contracts, all types of covers (i.e., excess loss, stop loss, quota share, surplus, XS aggregate)"; "multiple layers and complex inurements"; "Cession calculations and recoverables tracking"; "Ad hoc and Schedule F Reporting."
- Ceding automation: "Use our LORS integration to automate and simplify reinsurance ceding processes."
- Customer (QBE, VP Strategy and Operations Ceded Reinsurance): "one 'source of truth' for reinsurance calculations throughout QBE – for both ceded and assumed reinsurance"; outcomes: multi-currency flexibility, calculation accuracy, automated recovery processes.
- Deployment: cloud-native SaaS on AWS (press release) / Azure (FAQ page — both claimed on different pages; treat hosting detail as variant), Active Delivery continuous updates.

### Sequel Re (Verisk; London Market outward/ceded)

Key observations (A):

- Positioning: "Sequel's end-to-end outward reinsurance system for Lloyd's syndicates and London Market insurers."
- Process span: "manages the entire reinsurance process, from initial policy enquiry to automated premium and recovery calculations and credit control, via an intuitive web-based user interface."
- Real-time engine: "The calculation engine operates in real-time, giving users a comprehensive and accurate view of their latest reinsurance positions across all outwards policies and inwards data."
- Data intake: "imports all policy, premium and claims records from Sequel Underwriting, with real-time updates, via APIs. As a standalone product, it also seamlessly integrates with data warehouses and policy administration systems."
- Consolidation: "consolidating vast quantities of inward data and outward reinsurance policy information into one system for ease of programme management."
- Inuring logic: "further coverage-based inuring logic for treaty as well as facultative premium values, inclusive or exclusive of specific policies or commissions."
- Statistical/finance outputs: "new Deemed Policy functionality and new Accounting Period Close functionality to present the full depth of the statistical position for downstream finance systems"; "new system-wide reports on unissued recoveries and premium statements."
- Market trend framing: "an increasing number of companies now choosing to purchase reinsurance centrally and buying enterprise-wide coverages."
- Suite context: part of the Verisk Specialty Business Solutions suite (underwriting, broking, claims, Rulebook pricing); Sequel Re not listed on the current products page nav (product list shows Underwriting/Broking/Impact/Rulebook/Claims/Whitespace/Digital Distribution/Solutions/Ignite) — Sequel Re evidence is from the 2021 product news article; current packaging may differ (uncertainty noted).

### SolveXia (automation overlay pole)

Key observations (A):

- Positioning: general finance-process automation platform; reinsurance appears as use cases within life and general insurance solution lists.
- Life insurance: "Reinsurance bordereaux calculations — Eliminate your dependency on disconnected legacy scripts and processes. Maintain all of your business and calculation rules through a centralised treaty table."
- General insurance: "Reinsurance recoveries — Calculate amounts to be recovered for claims based on a centralised arrangement table. Eliminate dependency on key staff to perform the calculations."
- Case study (life bordereaux): "collects and validates data from multiple administration systems, allocates benefits to the correct reinsurance treaties, and calculates premiums"; "Business users can configure the logic behind allocations and calculations using simple, rule-based controls"; outputs "individual bordereau reports, which are sent to each reinsurer"; exception reports, traceability, audit readiness.
- Case study (recoveries): "compare monthly claims data against reinsurance rules and accurately calculate the amounts to be recovered."
- Case study (reinsurance + commission): weekly calculation of reinsurance, fees and commissions; produces "a journal for their accounting system."
- What it does NOT carry (from the same pages): no contract lifecycle management, no reinsurance claims surface, no assumed-side processing, no statutory reinsurance reporting. It is a calculation/allocation/reporting automation layer over a "centralised treaty table."

## Cross-product Comparison

| Structure / capability | Sapiens ReinsurancePro | Sapiens ReinsuranceMaster | Duck Creek Reinsurance | Sequel Re | SolveXia | Strength |
|---|---|---|---|---|---|---|
| Reinsurance agreement (treaty/fac) as managed record of contract terms | ✓ explicit ("manages treaties… contract definition") | ✓ ("all contract types") | ✓ explicit (pillar 1; lifecycle states) | ✓ (programme management; treaty + fac inuring logic) | △ "centralised treaty table" (attributes/rules only, no lifecycle) | A 4/5 full + 1 thin — Core |
| Allocation of underlying business to agreements (cession / inuring) with computed shares | ✓ ("attachment, calculation, and posting of premium and loss cessions") | ✓ ("automated reinsurance calculations") | ✓ ("automates cessions"; cession technical accounts) | ✓ ("coverage-based inuring logic"; premium/recovery calculations) | ✓ ("allocates benefits to the correct reinsurance treaties") | A 5/5 — Core |
| Calculation engine applying contract terms | ✓ | ✓ | ✓ | ✓ (real-time) | ✓ (rule-based) | A 5/5 — Core |
| Claims → recovery computation | ✓ (per risk/per occurrence/proportional/cat) | ✓ ("superior claim recovery") | ✓ (claims pillar; hours clauses) | ✓ (recovery calculations; unissued recoveries) | ✓ (recoveries from claims data + arrangement table) | A 5/5 — Core |
| Counterparty financial loop (accounts, balances, cash/settlement, credit control) | ✓ (reinsurance accounting and cash management) | ✓ (GL accounting, multicurrency, intercompany) | ✓ (accounting pillar; all account types) | ✓ (credit control; accounting period close) | △ (journals out to accounting system; no settlement ledger) | A 4/5 full + 1 partial — Core |
| Bordereaux / partner statements output | ✓ (statutory reports; single repository) | ✓ (statutory compliance) | ✓ ("bordereaux processing"; "automated report production for partners") | ✓ (premium statements) | ✓ (bordereau reports per reinsurer) | A 5/5 — Core |
| Inward data intake from policy/claims systems | ✓ (interfaces: policy, premium, claims, GL, annual statement) | ✓ (standard interfaces to policy and claims) | ✓ (LORS ceding integration; suite integration) | ✓ (APIs from underwriting/PAS/data warehouses) | ✓ (ingests from administration systems) | A 5/5 — Core |
| Reinsurance claims management surface (FNOL, claim lifecycle, events) | ✓ ("manages reinsurance claims… first notice of loss") | (not stated) | ✓ (claims pillar: claims, events, timelines) | (not stated) | ✗ | A 2/5 — Common, not universal |
| Contract lifecycle states (negotiation → signed → run-off → commutation) | △ ("contract definition through statutory reporting") | ✓ ("integrated workflows across all contract types") | ✓ explicit (creation, pending negotiations, signed, run-offs, commutations) | (not stated) | ✗ | A 2/5 explicit — Common |
| Statutory/regulatory reporting (Schedule F, IFRS 17, NAIC) | ✓ (Schedule F one-click; NAIC; IFRS 17) | ✓ (statutory compliance) | ✓ (Schedule F; regulatory reporting) | (not stated; London context) | ✗ | A 3/5 — Common; region-shaped |
| Assumed-side processing | ✓ | ✓ (multi-national programs) | ✓ (QBE: ceded + assumed) | ✗ (outward only) | ✗ | A 3/5 — Variant (side of the market) |
| Retrocession | ✓ | ✓ | ✓ | (not stated) | ✗ | A 3/5 — Variant |
| Placement simulation / what-if | ✓ (what-if on contract terms) | (not stated) | ✓ (placement simulations) | (not stated) | ✗ | A 2/5 — Optional |
| Multi-currency / intercompany / legal entities | (multi-national via sibling) | ✓ explicit | ✓ (currencies, legal entities) | (not stated) | ✗ | A 2/5 explicit — Common at scale |
| London Market machinery (LORS) | (via Master: LORS + London requirements) | ✓ | ✓ (LORS integration) | ✓ (native Lloyd's/London) | ✗ | A 3/5 — Regional variant |
| Audit trails / controls | ✓ | ✓ | ✓ (audit-ready) | (implied) | ✓ (traceability, audit readiness) | A 4/5 — Common |
| Analytics / consolidated risk views | ✓ | ✓ (consolidated liabilities/risks) | ✓ (reporting pillar) | ✓ (positions view) | ✗ | A 4/5 — Common |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a reinsurance management system. Three jointly-held structures:

1. **The reinsurance agreement as the managed contract of record.** A persistent, identified agreement between the operator (ceding insurer, or assuming reinsurer) and its reinsurance counterparties, carrying: scope (which underlying business it applies to), financial terms (share or limit/attachment structure, commissions), period, and status. Treaty and facultative placements are the two agreement forms; proportional and non-proportional are term configurations of the same object. Remove → a policy administration system or a contract document store.
2. **Allocation of underlying business to agreements — the cession/inuring operation.** Units of the underlying business (policies, premiums, claims/benefits) are attached to the agreements that cover them, and each party's share is computed under the agreement's terms — premium cessions outward (or inwards premium inuring), loss cessions and recoveries. This computation is the system's unit of work. Remove → a contract registry with no operational content, or a generic calculator.
3. **The counterparty financial loop.** The computed shares accumulate into balances with each counterparty — premium due to reinsurers, recoverable due from reinsurers — are reported to counterparties (bordereaux, technical accounts, statements), tracked through settlement/cash handling, and passed to the general ledger. Remove → a calculation tool with no money semantics.

Jointly-held test: 1 alone = treaty document library; 2 alone = allocation calculator; 3 alone = generic accounting; 1+2 without 3 = calculations nobody settles; 1+3 without 2 = contracts with no business attached; 2+3 without 1 = spreadsheet-style computation with no contract of record. All three are required, and all five full samples hold all three (SolveXia holds 2+3-partial+1-thin — the thin pole that confirms which structures are load-bearing).

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- Reinsurance claims surface — claims and events linked to contracts, recovery computation per claim, recovery maximization / claims-leakage framing (2/5 explicit, framed as a benefit everywhere)
- Contract lifecycle machinery — negotiation states, renewal by carrying terms forward, run-off, commutation (2/5 explicit)
- Statutory/regulatory reporting — Schedule F, NAIC annual statement links, IFRS 17 (3/5; region-shaped)
- GL integration, multi-currency, intercompany/multi-entity support (2/5 explicit; implied at scale)
- Audit trails and controls (4/5)
- Analytics — consolidated views of positions, exposures, liabilities; KPIs (4/5)
- Placement simulation / what-if on contract terms (2/5)
- London Market machinery — LORS integration, broker-facing outputs (3/5, regional)

### L2 — Variant / Optional Structure

- Side of the market: ceded-only (Sequel Re outward; SolveXia use cases) vs ceded+assumed+retroceded (Sapiens, Duck Creek) vs reinsurer-side assumed deployments
- Line-of-business shaping: P&C (per-risk/per-occurrence/catastrophe recoveries, Schedule F) vs life (benefit/premium allocation cycles, weekly/monthly bordereaux runs)
- Regional machinery: US statutory (Schedule F/NAIC) vs London Market (LORS, Lloyd's syndicates) vs multi-country/multi-currency programs
- Packaging: dedicated system (Sapiens) vs beyond-core suite module (Duck Creek) vs standalone+suite dual deployment (Sequel Re) vs automation overlay (SolveXia)
- Pools, affiliates, intercompany treaties (Sapiens explicit)
- Hosting: cloud SaaS (current default across samples) vs legacy on-premise estates being replaced

### L3 — Vendor-specific Structure (Research Notes only)

- Sapiens' two-product split: ReinsurancePro (P&C carriers, mid-market-to-enterprise) vs ReinsuranceMaster (large/multi-national, London Market requirements) — same family, scale-tiered packaging
- Duck Creek "Active Delivery" continuous-update model; Clarity data foundation; LORS ceding integration; "Beyond Core" suite positioning; conflicting cloud statements (AWS in 2026 press release vs Azure in FAQ) — hosting detail unstable across pages
- Sequel Re "Deemed Policy" functionality, "Accounting Period Close", microservice-based calculation engine, real-time position view
- SolveXia no-code process automation, Excel-formula calculation maintenance, SQL-server processing environment
- QBE testimonial specifics (multi-currency across divisions, calculation accuracy, automated recovery)
- Celent recognition framing ("Functional Standout", "Luminary")

## Vendor-specific Findings

See L3. None of these carry into the canonical document beyond neutral mention as product examples.

## Boundary Findings

- **vs Insurance Policy Administration System** — the master-record seam. PAS holds direct policies sold to policyholders (parties × coverage × premium × period, governed lifecycle). RMS holds reinsurance agreements between insurers/reinsurers and allocates PAS business to them. The cession is the bridge object: PAS is the upstream source of policy/premium/claims data; RMS consumes it and computes ceded shares. Remove the reinsurance agreement and the counterparty loop → PAS territory. Confirmed from both sides (PAS pass listed this Type as treaty-side sibling; PAS products ship reinsurance as a separate module or integration seam — Duck Creek Reinsurance is a separate "Beyond Core" product from Duck Creek Policy).
- **vs Insurance Claims Management** — the loss-vs-recovery seam. Claims systems own the loss lifecycle (FNOL → adjudication → payment). RMS consumes claim data to compute recoveries; some RMS products carry a reinsurance-claims surface (Sapiens "manages reinsurance claims with… first notice of loss"; Duck Creek claims pillar) but that surface is the recovery side of claims (matching claims to contracts, computing recoverable amounts, billing/status letters), not the adjuster's loss adjudication.
- **vs Broker Management Platform** — the principal seam. Reinsurance brokers place reinsurance and process bordereaux on behalf of cedents/reinsurers (Willis Re ran Sequel's broking software); the RMS manages the insurer's or reinsurer's own treaty/cession/settlement record. Same market, different principal and different record.
- **vs Insurance Underwriting Platform / Underwriting Workbench** — the decision-vs-administration seam. Assumed-side treaty underwriting (e.g., Send for Reinsurance Underwriting) decides which treaties to write; the RMS administers the agreed business (cession processing, accounting, settlement). Placement simulation inside RMS is a capability, not the decision machinery.
- **vs Actuarial Modeling Platform** — the model-vs-record seam. Actuarial platforms model risk, pricing, reserves (reinsurance appears as a management action inside models); RMS holds the contractual and financial record of actual reinsurance business.
- **vs generic finance automation / reconciliation platforms** — the thin pole. An automation platform can carry a treaty table, allocation rules, and bordereaux output (SolveXia), but without the agreement lifecycle, claims/recovery machinery, and settlement ledger it is an overlay on the reinsurance function rather than the system of record. This boundary is graded, not binary — SolveXia deployments sit inside reinsurance departments doing reinsurance work; the distinguishing question is whether the agreement of record and the counterparty financial loop live in the system.
- **"去掉什么就变成另一个 Type" 判据**: remove the reinsurance agreement (treaty/fac) → policy administration; remove the cession/allocation computation → contract repository; remove the counterparty financial loop → calculator or BI; remove the insurance subject matter entirely → generic contract + finance automation.

## Historical / Market-Sample Check

- Pre-digital reinsurance departments ran on treaty ledgers, manually prepared bordereaux, cash sheets and settlement records with each reinsurer — the agreement record + cession registers + counterparty financial loop all existed on paper. The L0 holds without any digital-era feature.
- Life reinsurance has long been administered through ceded-reinsurance modules on life administration systems with periodic (weekly/monthly) allocation cycles — the same structures at different cadence.
- Regional breadth: US statutory practice (Schedule F), London Market practice (Lloyd's outwards reinsurance, LORS), multi-national programs — all instantiate the same core.
- The check passes: the definition is not over-fitted to the current cloud-SaaS generation or to the ceded-P&C pole.

## Uncertainties

1. **In-product workflow depth** — no help centers/user guides were reachable; the cession-processing and settlement workflows are reconstructed from product-page capability statements, official brochure text (via search extraction), and case studies. Exact screen-level flows, state vocabularies, and default settings are not evidenced and are deliberately not asserted.
2. **Sequel Re current packaging** — the 2021 news article is the direct source; the current Verisk products page does not list "Sequel Re" by name in its navigation (products listed: Underwriting, Broking, Impact, Rulebook, Claims, Whitespace, Digital Distribution, Solutions, Ignite). The product may have been renamed or folded into "Broking". Treat Sequel Re as a documented London-market outward reinsurance system of the 2020–2021 generation.
3. **Duck Creek hosting statements conflict** — AWS (2026 press release) vs Azure (FAQ page). Hosting is variant detail; not resolved here.
4. **Assumed-side depth** — assumed processing is evidenced as supported (Sapiens "assumed processing capabilities"; Duck Creek QBE quote "both ceded and assumed"), but no sampled product page details the assumed-side workflow (inwards bordereaux intake, treaty accounting) at the same depth as the ceded side. The final document describes the assumed side at the evidenced level of generality.
5. **Facultative workflow** — facultative is evidenced as an agreement type handled by all full samples; the facultative-specific submission/acceptance workflow is not separately evidenced and is not asserted.
6. **Market-size / deployment-count claims** ("market leader with highest global deployments") are vendor marketing; not used.

## Final Synthesis

A Reinsurance Management System is the insurance industry's system of record for reinsurance business — the risk-sharing contracts insurers and reinsurers write with each other. Its world is built from three jointly-held structures: the reinsurance agreement (treaty or facultative placement) as the managed contract of record; the allocation operation (cession/inuring) that attaches units of underlying business — policies, premiums, claims, benefits — to those agreements and computes each party's share under the agreement's terms; and the counterparty financial loop that accumulates those shares into balances with each reinsurer or cedent, reports them (bordereaux, technical accounts, statements), and settles them into the ledger. Around that core, mature products add reinsurance claims and recovery machinery, contract lifecycle states (negotiation through run-off and commutation), statutory reporting (Schedule F, IFRS 17), multi-currency/intercompany accounting, audit trails, and analytics. The Type spans ceded-side systems for insurers, assumed-side processing for reinsurers, and retrocession; it is shaped by line of business (P&C occurrence/cat recoveries vs life allocation cycles) and by market machinery (US statutory vs London Market). Its seams: policy administration feeds it business and holds the direct policy record; claims systems hold the loss and feed recovery computation; broking systems serve a different principal; underwriting platforms make the treaty decisions it administers; actuarial platforms model what it records.
