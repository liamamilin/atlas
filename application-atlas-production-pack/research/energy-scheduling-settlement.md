# Research Notes — Energy Scheduling & Settlement

## Research Goal

Understand what "Energy Scheduling & Settlement" software actually is from real products: what a participant submits to an organized power market or transmission/settlement authority, what "settlement" concretely involves on the participant side, what objects and workflows make up the scheduling desk and the settlement/back office, and where this Type's boundary sits against Energy Trading Platform, Energy Forecasting Platform, Grid Operations/EMS, Meter Data Management, and Utility Billing.

## Initial Boundary (working hypothesis before research)

- Hypothesis: the Type is the **market-participant-side "bid-to-bill" back half** — a scheduling desk (bids/schedules/tags submitted to ISO/RTO or transmission/settlement authorities under deadlines) plus a settlement office (ingesting the market's settlement statements, validating them against the participant's own expectation, disputing discrepancies, and closing the books).
- Adjacent leaves in the directory: Energy Trading Platform (front/middle office), Energy Forecasting Platform, Grid Operations Platform, Energy Management System / EMS, Meter Data Management System, Utility Billing Platform, Energy Trading Platform family.
- Known ambiguity to resolve: does the leaf cover only participant-side software (commercially sold), or also the market/operator-side settlement machinery (e.g., a Nordic imbalance settlement agent)? Decision deferred to evidence.

## Research Questions

1. What exactly is "scheduling" in this context? What is submitted, to whom, by when, and what comes back?
2. What does "settlement" concretely involve on the participant side? What is a settlement statement and what happens to it?
3. What is shadow settlement / pre-settlement and why do products emphasize it?
4. What role do transmission tags (e-Tags), meter data, and contract billing play — are they part of this Type or adjacent?
5. Who are the users (roles) and what interfaces do they work in?
6. What rules dominate: deadlines, market-rule validation, versioned corrections, auditability?
7. How do products differ in philosophy: full suite vs point tools vs data-company platform; and is there a separate operator/agent-side pole?
8. Would older/bilateral-market forms (interchange scheduling, interchange accounting) still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| **PCI Energy Solutions** (Power Costs, Inc.; Norman, OK; founded 1992) | participant-side full suite (ETRM + Bid-to-Bill + Transmission) | market-leading incumbent for US ISO/RTO participants; deepest documented coverage of scheduling + e-tagging + settlements + billing |
| **Yes Energy** — PowerCore + Submission Services | participant-side platform from a data company | explicit "bid-to-bill" positioning with explicit "not an ETRM" statement on Submission Services; different lineage (market data) than PCI |
| **eSett Oy** (Helsinki; owned by the four Nordic TSOs) | market/operator-side settlement agent | deliberate counter-pole: settlement run market-wide as a regulated duty; Tier-1 handbook documents the settlement function's canonical mechanics |

Unreachable (recorded): **Adapt2** (adapt2.com transport error; yesenergy.com product-path guess returned 404) and **OATI** (oati.com timed out twice). Both are commonly cited participant-side vendors; their absence narrows the commercial sample to two participant products, both North American.

## Sources

- https://www.pcienergysolutions.com/ (root; solution family structure) — 2026-09-08
- https://www.pcienergysolutions.com/solutions/bid-to-bill/settlements-and-billing/ — 2026-09-08
- https://www.pcienergysolutions.com/solutions/bid-to-bill/wholesale-market-participation/ — 2026-09-08
- https://www.pcienergysolutions.com/solutions/transmission/etagging/ — 2026-09-08
- https://www.pcienergysolutions.com/solutions/etrm/back-office/ — 2026-09-08
- https://www.yesenergy.com/ (root; product family) — 2026-09-08
- https://www.yesenergy.com/products/powercore — 2026-09-08
- https://www.yesenergy.com/products/submission-services — 2026-09-08
- https://www.esett.com/ — 2026-09-08
- https://www.esett.com/handbook/ (NBS Handbook v5.4, June 2026, web version) — 2026-09-08

Unreachable: https://www.adapt2.com/ (transport error), https://www.yesenergy.com/products/adapt2 (404), https://www.oati.com/ and /products (timeouts ×2 — abandoned per retry discipline).

## Product Observations

### PCI Energy Solutions — evidence layer A (Tier 2 official product pages + named-customer testimonials)

**Family structure ("Bid-to-Bill" umbrella, "From first forecast to final bill, across every market"):**
Forecasting → Market Participation → Scheduling & ISO Integration → e-Tagging → Meter Data Management → Settlements and Billing. Markets supported: CAISO, ERCOT, ISO-NE, MISO, NYISO, PJM, SPP, US bilateral markets, Canada (AESO, IESO), Mexico (MEM).

**Market Participation (GenManager):**
- "Automate all bid-to-bill, front and back office processes"; create reusable strategies to submit bidding positions; generate pre-settlements and shadow validation of ISO statements and invoices; create and submit virtual bids and offers.
- Documented participant workflow chain: ISO communication → LMP forecast (with "similar-day" profile library) → bid formulation → bid evaluation (day-ahead and real-time bid analysis, day-ahead adjustment-period analysis, bidding strategy P&L forecasting, **ISO market award validation**, multi-case analysis) → settlement (next-day preliminary settlements; shadow settlements and verify ISO invoices; **submit and track disputes**).
- "Quickly identify and dispute ISO settlement discrepancies"; automate collection of market data.

**Settlements and Billing:**
- **ISO & Shadow Settlements** — "Calculate preliminary pre-settlements of the ISO charges prior to the availability of the ISO statement to provide a comprehensive side-by-side comparison to quickly find discrepancies."
- **Transmission Shadow Settlements** — validate transmission provider bills by shadow settlement, expected vs actuals.
- **Contract Management & Billing** — invoice and shadow-settle "all contract types"; validate contract data before use; auto-map contract data to the general ledger; real-time data gathering so users "aren't waiting for preliminary month-end estimates".
- **Advanced Allocation** — allocate costs to internal and external entities before the GL pass; assign to rule-defined buckets; bill a joint owner; book AR/AP for complex market transactions.
- **Settlements Forecasting** — next-day settlements forecasting supports accruals and profitability analysis.
- **FERC EQR** — generates pre-formatted EQR files for ISO market transactions (regional-regulatory instance).

**e-Tag+ (energy tagging):**
- Create, edit, send, receive **NERC e-Tags**; tag templates store all e-Tag attributes including profiles; automatic tag creation; automatic validation and submission; **automatic approval or denial of requests and submissions to e-tag Authority**; interface with OASIS to validate transmission profiles; link multiple tags to a single deal; tag path and profile diagram; asynchronous status refresh; back-office e-Tag checkout with as-of requests and snapshot computation; checkout reports/exports "for further billing analysis"; e-Tag Forward distributes real-time tag data to third-party apps.

**ETRM Back Office:**
- "Consolidates settlements, meter data management, billing, and audit workflows into a single system… validate data, resolve discrepancies, accelerate month-end close, and maintain clean, compliant records."
- "Unify ISO/RTO statements, bilaterals, transmission, and meter data in one ETRM to surface discrepancies, shadow-settle, and close on time."
- Suite components: **ISO/RTO Settlements** (ingest market statements, calculate settlement charges, compare ISO results to internal expectations, drilldowns built for large data volumes); **Bilateral Settlement Processing** (configurable validations, comparison views, checkout workflows "that ensure both sides of the trade align before invoicing"); **Transmission Billing Management** (import/validate/review transmission provider invoices, flexible rate handling, discrepancy drilldowns); **Meter Data Validation** (centralize meter data, validate at granular intervals, correct values); **JDA and Complex Settlement Support** (multi-party agreements, settlement input files, reconciliation of partner activity across high-volume intervals); **Rebilling and Prior-Period Adjustments** (versioned workflows supporting incremental adjustments "without re-opening closed months").
- Faster-close machinery: "Automate trade-to-settlement workflows — from statement ingestion through reconciliation — to shorten month-end cycles"; "detect and correct sub-hourly settlement issues"; "shadow settlements and evidence-ready reports to initiate disputes and recover misapplied ISO/RTO charges."
- Customer-voiced outcomes (Layer A, product-specific): disputes filed with ISOs recovering money; "$1.2 million recovered… using PCI's shadow settlement and validation tools"; month-end close acceleration; roles cited include "Middle Office Manager", "Manager, Regulatory & Energy Settlements", "Sr. Market Coordinator", "Client Manager, Power Settlements"; "Divisional Accounting solution lets us easily create, update and link subaccounts to resources and transactions"; subhourly data granularity import.

### Yes Energy — PowerCore + Submission Services — evidence layer A (Tier 2 product pages + FAQ)

**PowerCore ("unified bid-to-bill platform purpose-built for energy market participants operating in ISO/RTO and bilateral markets"):**
- "Automates and connects bidding, scheduling, settlements, contract billing, and analytics into a single, audit-ready system."
- Position basis: "connects bids, schedules, trades, meters, settlements, and contracts into one source of truth"; front-, middle-, back-office teams; roles named: trading, scheduling, settlements, accounting, risk, utility operations. Audiences: utilities, public power, CCAs, IPPs, market operators.
- Settlement validation: "Automate ISO settlements, meter submissions, and shadow calculations. Compare ISO statements against predictive and 'what-if' settlements to detect discrepancies early and resolve disputes faster. Drill down to interval-level detail for billing determinants."
- Contract billing: "Manage, shadow, and invoice even the most complex power purchase agreements with version-controlled logic, automated validations, and complete audit trails."
- Submission side: "Automate ISO/RTO bidding, scheduling, and tag management with built-in business rules and real-time status monitoring — reducing submission errors."
- Position management: "Centralize trade capture, position management, credit exposure, contracts, and settlement outcomes across ISO and bilateral markets" — "one trusted book of record" (suite adjacency toward ETRM territory).
- Transmission: "Centralize transmission billing, shadow settlements, and cost allocations… accurately assign charges to cost-causing assets."
- Analytics: "reconcile awards, dispatch, meters, and settlements; identify uplift, congestion, deviations, and cost drivers."
- Rule maintenance as service: "PowerCore includes automatic market rule updates and a fully managed service — no scripts to maintain"; "market-specific data models and isolated ISO environments"; "full charge-level traceability."
- Vendor-claimed figures (Layer A as claims, unverified): "$9B+ gross settled and validated annually for a typical large IOU"; "6,100+ settlement disputes validated and resolved annually for a typical large IOU"; "90%+ reduction in contract billing time."

**Submission Services:**
- "Day-ahead virtual and spread trade submission… 7 US ISOs supported with a single, standardized execution workflow"; "79 validation checks embedded"; ISO-specific validation covering "node eligibility, pricing, volumes, and wash trades"; edit and submit "up until the submission deadlines"; submit and withdraw trades; ISO messaging shows "clear status of your trade submissions"; day-ahead clearances tracked near real time; API automation of submission, clearance retrieval, downstream integration.
- Explicit positioning (FAQ): **"Submission Services is not an ETRM"** — "a turnkey solution… its API will integrate with your current ETRM tool."

### eSett Oy — evidence layer A (Tier 1: NBS Handbook v5.4, web version)

**Seat:** "Imbalance Settlement Responsible" owned equally by the four Nordic TSOs (Energinet, Fingrid, Statnett, Svenska kraftnät); performs imbalance settlement and invoicing of BRPs (balance responsible parties) and BSPs (balancing service providers) on behalf of the TSOs. "Historically, Fingrid, Svenska kraftnät, Statnett and Energinet each have been operating their own imbalance settlement" — the common agent replaced four national ones.

**Purpose:** "establish a financial balance in the electricity market after the operation hour. Imbalances are calculated for each BRP based on the PX market trades, bilateral trades and on realised consumption and production." Balancing-service settlement compensates capacity/energy between TSOs and BSPs and computes regulation imbalances per BSP.

**Model functions (handbook's own decomposition):** settlement structure management; metering; reporting data; settlement; invoicing; reporting; collateral management; communication; market behavior monitoring; market analysis.

**Settlement rhythm:** **preliminary imbalance settlement** → **reconciliation settlement** (differences between preliminary and final profiled consumption settled at day-ahead prices); invoicing performed weekly; no invoicing on public holidays; CET operation.

**Role obligations (settlement-relevant excerpts):**
- **BRP**: "Planning balanced schedules on an hourly basis; Submitting plans per RO to the TSO; Submitting bilateral trade information to eSett and verifying the correctness of the bilateral trades submitted by its counterparts…; Verifying all relevant data reported by eSett, and notify deviations"; financial counterpart for imbalances; provides collaterals; keeps settlement structure information up to date.
- **DSO**: meters production/consumption/exchange and reports metered data; calculates final profiled consumption; imbalance corrections after reporting closes are settled between DSO and RE.
- **NEMO (power exchange)**: reports day-ahead and intraday trade data per RE and MBA to eSett.
- **Service Provider**: may perform reporting, verification of calculated imbalances, or collateral management on the online service on behalf of a market party.
- Agreements: Imbalance Settlement Agreement (BRP↔eSett) covering fees, invoicing/payment process, collateral procedures, settlement rules, dispute resolution; settlement banks approved for the money flow; exclusion procedures for breach.

**Surfaces:** Online Service (login portal for participants), Open Data portal, Handbook as single consolidated rule source.

## Cross-product Comparison

| Structure / capability | PCI (participant suite) | Yes Energy PowerCore / Submission Services | eSett (agent) | Judgment |
|---|---|---|---|---|
| Time-structured submissions to a market/TSO authority (bids/schedules/tags/plans) | ✔ bids, virtuals, e-Tags with path/profile, deadlines, validation, status | ✔ bidding, scheduling, tag management, real-time status; day-ahead virtual/spread submission with ISO-specific validation, withdraw, clearances | ✔ BRP plans per RO, bilateral trade reports; plans hourly | **Core** (all three hold it, in regime-specific realizations) |
| Submission validity checks against the governing rulebook | ✔ automatic validation, e-Tag Authority approval automation | ✔ 79 validation checks (node eligibility, pricing, volumes, wash trades), managed rule updates | ✔ validation of reported data; structure rules | **Core ingredient** |
| Awards / clearances / acceptance status returned and tracked | ✔ ISO market award validation | ✔ clearances, ISO messaging status, real-time status monitoring | ✔ verification of reported data; deviations notified | **Core ingredient** |
| Ingestion of an itemized settlement statement/invoice as authoritative claim | ✔ ISO/RTO statements, transmission provider invoices, bilateral counterparty invoices, JDA files | ✔ ISO statements; transmission billing | ✔ (as producer of the invoice; participants verify) | **Core** |
| Independent recomputation of expected settlement (shadow / pre-settlement) | ✔ pre-settlements before statement availability; transmission shadow settlements | ✔ predictive and "what-if" settlements compared to ISO statements | ✔ (agent computes the settlement itself; participant verifies) | **Core** |
| Discrepancy → dispute → recovery lifecycle | ✔ submit and track disputes; evidence-ready reports; $ recovered (customer-voiced) | ✔ disputes validated and resolved; drilldown to billing determinants | ✔ deviation notification; dispute resolution in agreements | **Core** |
| Versioned corrections / rebills without reopening closed months | ✔ versioned rebills, prior-period adjustments | ✔ audit trails; "every charge traceable" | ✔ reconciliation settlement corrects preliminary results | **Common mature** |
| Meter data as validated settlement input | ✔ meter data validation module | ✔ meter submissions & validation | ✔ DSO metering is the settlement's data basis | **Common mature** (embedded; deep MDM is a separate Type) |
| Billing of own contracts (PPA/bilateral/member) from validated data | ✔ any contract type, AR/AP, joint-owner billing, GL mapping | ✔ PPA/bilateral invoicing, version-controlled logic | ✖ (out of agent scope) | **Common mature** (the "bill" half of bid-to-bill; absent agent-side) |
| Cost allocation (internal/external, joint owners, cost-causing assets) | ✔ advanced allocation | ✔ allocations to cost-causing assets | ✖ | Common (participant-side) |
| Pre-statement settlement estimates for accruals/P&L | ✔ next-day settlements forecasting | ✔ predictive settlements | ✖ | Common (participant-side) |
| Settlement collateral / credit risk machinery | ✖ (not observed) | ~ credit exposure sits in position-management adjacency | ✔ collateral management, settlement banks | Variant (seat-dependent) |
| Regulatory filing outputs | ✔ FERC EQR generation | ✖ (not observed) | ✔ market monitoring/KPIs | Variant (regional) |
| Market-rule update maintenance as part of the service | ✔ explicit ("monitor and respond to market changes") | ✔ explicit ("automatic market rule updates") | ✔ Handbook update cycle (twice yearly) | Common mature |
| Audit posture (charge-level traceability, audit-ready records) | ✔ audit workflows | ✔ audit-ready, charge-level traceability | ✔ published rules, structure records | Common mature |
| Analytics over settlement drivers | ✔ (Insights; uplift/congestion via suite) | ✔ visual analytics: awards, dispatch, meters, settlements, uplift, congestion, deviations | ✔ KPI monitoring (agent-side) | Common mature |

**Reading:** the three-part structure (submission → statement → reconciliation-to-closure) is held by every product in its own seat. Participant-side products add billing/allocation/accruals (financial closure outward); the agent-side pole adds collateral/risk/market-monitoring (financial control market-wide). The scheduling half and the settlement half are always co-present at the level of the function, even when packaged as separate products.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The market submission of record** — time-structured energy quantities (bids/offers, self-schedules, transmission tags/plans, bilateral trade reports) composed against the participant's position in a **named market**, validated against that market's rules, and submitted to the market/transmission/settlement authority **under deadline**, carrying identity (participant, resource/unit, location, path, interval) and returning recorded **awards / clearances / acceptance status**.
   - Remove → a bid-submission tool or data feed; there is no settlement side, and the product is a thin execution utility (observed as a real thin pole: a submission-only point tool).
2. **The settlement statement of record** — the counterparty's (market operator, settlement agent, transmission provider, bilateral counterparty) **itemized statement of charges and credits** by charge type, interval, and subject, ingested as the authoritative claim on money owed by and to the participant.
   - Remove → a scheduling desk with no settlement function; "settlement" has no object.
3. **The participant-side reconciliation loop** — an **independent recomputation of what the settlement should be** (shadow settlement / pre-settlement / verification) from the participant's own position, awarded/scheduled quantities, measured quantities, and prices; a **side-by-side comparison** against the statement producing tracked **discrepancies**; discrepancies driven through **dispute/adjustment/rebill to recorded financial closure**.
   - Remove → statement ingestion without checking is a data feed; there is no settlement office.

Jointly-held is load-bearing:
- 1 alone = bid/schedule submission tooling (real thin pole).
- 2+3 without 1 = a settlement bureau over statements with no position of its own — this is the **agent-side seat** (observed: the settlement agent holds the settlement loop and receives participant reports; the commercial leaf is realized on the participant side).
- 1+3 without 2 = accrual/pre-settlement calculation with nothing to settle against.
- 2 alone = statement ingestion/reporting.

### L1 — Common Mature Structure

- **Award validation** — checking returned market awards against submitted bids/schedules; day-ahead vs real-time analysis.
- **Deadline mechanics** — edits/submissions up to gate closure; withdrawal; real-time submission status monitoring.
- **Tag/path machinery** (North American realization) — e-Tag creation with source/sink path and hourly profile, template-driven creation, approval chains to a tag authority, transmission-profile validation against OASIS, tag checkout/reports feeding billing.
- **Meter data as settlement input** — centralized, interval-level validation and correction before it feeds settlements and billing.
- **Preliminary → final rhythm with versioned corrections** — preliminary settlements/statements first, final/reconciliation later; rebills and prior-period adjustments via versioned workflows that never reopen closed months.
- **Pre-statement estimates** — next-day/preliminary expected settlements feeding accruals and P&L.
- **Contract billing and allocation** — invoicing PPAs/bilateral contracts/members from the same validated data; cost allocation to internal/external parties and cost-causing assets; AR/AP; GL mapping.
- **Dispute management** — filing, tracking, evidence-ready reports; recovery of misapplied charges as a designed outcome.
- **Market-rule maintenance** — the vendor absorbs market/tariff rule changes into the software as an ongoing service (explicit in both participant products; the agent side publishes consolidated rulebooks on a fixed cycle).
- **Audit posture** — charge-level traceability, audit trails, clean records supporting month-end close.
- **Settlement analytics** — reconciliation of awards/dispatch/meters/settlements; drivers like uplift, congestion, deviations.

### L2 — Variant / Optional Structure

- **Seat**: participant-side (the commercial default) vs market-wide settlement agent (regulated duty; collateral management; market-behavior monitoring; public data).
- **Market regime**: organized ISO/RTO markets (charge-coded statements, virtual bids, e-Tags) vs bilateral markets (counterparty invoices, interchange-style settlement, "both sides align" checkout) vs Nordic imbalance settlement (hourly plans + metered balance, weekly invoicing, reconciliation month, collateral). Other regional regimes (e.g., GB-style BSC settlement) were not sampled — recorded as presumed by structure, not asserted.
- **Participant class**: generators/IPPs; load-serving utilities, public power, CCAs; cooperatives with member billing; marketers/traders. Smaller participants run scheduling + settlements + analytics in one team/platform.
- **Packaging**: submission-only point tool; settlement-only back office; integrated bid-to-bill platform; full ETRM suite where this Type's functions sit beside deal capture and risk (packaging overlap, not identity — see Boundary Findings).
- **Commodity scope**: power-only vs power + gas/fuels in one back office; interval granularity (hourly vs sub-hourly settlement issues).
- **Delivery posture**: fully managed SaaS with vendor-run ISO environments vs deployable enterprise software.

### L3 — Vendor-specific Structure (research notes only)

- PCI: GenManager®, GenTrader®, e-Tag+, PCI Insights™, ISO Bot / M+ Bot / CEN Bot, FERC EQR generation, 15-minute on-call support claim, 75%+/60% market-penetration claims, "Divisional Accounting", JDA support, WEIS/RTC+B market-migration support notes.
- Yes Energy: PowerCore™, Submission Services™, PowerSignals®, DataSignals®, Position Management; claimed metrics ($9B+ settled/validated annually for a typical large IOU; 6,100+ disputes annually; 90%+ contract-billing time reduction; 79 validation checks; 7 ISOs; 10,000+ trades per submission).
- eSett: Online Service, Open Data portal, NBS Handbook versioning, settlement banks, approved-bank requirement, volume-fee-zeroing news, country-specific exclusion handling (Denmark/Finland/Norway/Sweden variants).

## Rejected Findings

- **Bid-strategy optimization and portfolio optimization** (forecasting, LMP optimization, storage optimization): observed only as adjacent suite modules; belong to Portfolio Optimization / Energy Forecasting leaves. The Type's bid capability is composition, validation, submission — not strategy generation.
- **Deal capture, position, and credit risk**: observed inside suites ("one trusted book of record") but explicitly differentiated by a sampled vendor ("not an ETRM"); belongs to Energy Trading Platform territory. Kept out of the core.
- **Retail consumer billing on tariffs**: different counterparty (end consumer) and logic; Utility Billing Platform territory.
- **Real-time grid control / balancing operations** (BA operations module): physical operations; Grid Operations / EMS territory. The agent's own scope statement supports the seam: "All matters directly related to system operations… are outside the scope of the Imbalance Settlement Model."
- **Deep meter-data management as an enterprise record system**: embedded validation is common, but the enterprise MDM is its own directory leaf.

## Boundary Findings

- **vs Energy Trading Platform** — the sharpest seam. Trading systems hold deals/positions/risk; this Type holds **submissions and settlement statements** — the market-facing expression of those deals and the money the market claims from them. Suites bundle both (PCI ETRM), and one sampled product family explicitly positions itself as "not an ETRM". Suite overlap is packaging; object-of-record differs. Keep-both ratified from this side.
- **vs Energy Forecasting Platform** — forecasts are inputs to bid composition; the forecasting leaf produces and verifies the numbers, this leaf submits them and settles their consequences. (Both sampled suite vendors bundle a forecaster as an adjacent module.)
- **vs Grid Operations Platform / EMS** — physical real-time supervision/control of the network vs the market-financial aftermath of the operating day. Different users (system operators vs schedulers/settlement staff), different objects (telemetry/switching vs submissions/statements).
- **vs Meter Data Management System** — enterprise metering record vs meter data validated as a settlement determinant. Suites embed the latter; the former is a distinct Type.
- **vs Utility Billing Platform** — bills end consumers on retail tariffs; this Type settles wholesale market money with market operators, settlement agents, transmission providers, and bilateral counterparties. (At load-serving entities the two meet: retail billing consumes the same meter data.)
- **Agent-side pole** — a TSO-owned settlement agent executes the same settlement function market-wide as a regulated duty (collateral, invoicing, structure management). The directory leaf is realized commercially on the participant side; the agent seat is recorded as a variant/boundary rather than a separate leaf decision. If the directory is ever revised, "market settlement agent" could stand alone; splitting is not forced by this pass.
- **Remove-what-becomes-another-Type tests**: remove the market context (no market operator/agent, only private counterparties) → back-office contract/interchange billing (the historical ancestor); remove settlement → submission tooling; remove submissions → settlement-reconciliation bureau (agent seat).

## Historical / Market-Sample Check

- **Bilateral-era ancestor (reasoning-based, layer C):** before organized ISO/RTO markets, utilities scheduled interchanges bilaterally and settled them through interchange accounting against counterparty statements. The sampled products still carry this form explicitly: PCI lists "US Bilateral Markets" among supported regimes and its bilateral settlement processing requires "both sides of the trade align before invoicing" (checkout semantics of a paper-era practice); eSett's handbook documents that national TSOs each ran their own imbalance settlement before the common agent, and that bilateral trades are reported and verified as settlement inputs. The three-part core (submit/schedule → counterparty statement → reconcile to closure) holds without ISO charge statements, virtual bids, e-Tags, or cloud delivery.
- **Agent-side continuity:** the same settlement function existed as a TSO department before becoming a dedicated company — evidence that the "settlement office" is a stable function independent of its seat.
- **No modern-era specifics entered L0:** no ISO charge codes, no virtual bidding, no e-Tags, no OASIS, no managed SaaS, no AI. Regional/regime mechanics live in L1/L2.

## Uncertainties

- **Sample breadth:** only two commercial participant-side products reachable, both North American; Adapt2 and OATI unreachable (transport error / timeouts). European participant-side back-office products were not sampled; the Nordic agent is the only non-NA pole.
- **Agent-side descriptions rest on one product** (eSett). General agent-side claims in the final document are kept minimal and generic; GB-style settlement agents (e.g., Elexon-class) were not fetched.
- **Vendor-claimed figures** (settled dollars, dispute counts, validation-check counts, market penetration) are marketing claims, not independently verified; they appear only in research notes.
- **Precise market timetables** (statement cadences, preliminary→final intervals, invoice cycles beyond eSett's weekly invoicing) were deliberately not researched to assertion precision; none are stated in the final document.
- **e-Tag rulebook details**: the term "NERC e-Tags" is directly evidenced on a product page; the underlying standard's mechanics were not independently fetched.
- **Exact packaging split between "Scheduling & ISO Integration" and "Power Scheduling and Trading" at PCI** was not disambiguated beyond the family structure; treated as one scheduling capability in the model.

## Final Synthesis

An **Energy Scheduling & Settlement** system is the wholesale power market participant's market-facing operations system of record. Its defining core is three jointly-held structures: (1) the **market submission of record** — time-structured energy quantities (bids, schedules, tags/plans) composed against the participant's position, validated against the governing market's rules, submitted under deadline, with awards/clearances returned and tracked; (2) the **settlement statement of record** — the market operator/agent/counterparty's itemized claim of charges and credits ingested as authoritative; (3) the **participant-side reconciliation loop** — an independent shadow computation of what the settlement should be, compared side-by-side against the statement, with discrepancies tracked through dispute, adjustment, and rebill to auditable financial closure (accruals, billing of own contracts, allocation, GL handoff). Standard capabilities (award validation, virtuals, tag-path machinery, meter-data validation, versioned rebills, pre-statement estimates, dispute recovery, managed rule updates, audit traceability, settlement analytics) are widespread but not definitional. Variants follow seat (participant vs market-wide settlement agent), market regime (organized ISO/RTO vs bilateral vs Nordic imbalance model), participant class, and packaging (point tools to full ETRM suites). The sharpest boundary is against Energy Trading Platform (deals/positions vs submissions/statements; suite overlap is packaging, not identity), with further seams against Energy Forecasting, Grid Operations/EMS, Meter Data Management, and Utility Billing. The historical check passes: bilateral-era interchange scheduling and counterparty accounting satisfy the core without any ISO-era machinery.
