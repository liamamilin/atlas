# Research Notes — Liquidity Risk Platform

Leaf: Liquidity Risk Platform (DIRECTORY.md §08 Finance, Banking, Insurance & Investment)
Slug: `liquidity-risk-platform`
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Determine what a "Liquidity Risk Platform" actually is as an Application Type: its defining core, its users, its world model (objects and relations), its canonical workflows, its interfaces, its rules, and its boundaries. Three boundary questions dominate this pass:

1. **Umbrella-vs-slice joint review** vs Financial Risk Management Platform (processed) — the hub pass flagged market-risk/credit-risk/liquidity-risk as sibling slices; credit-risk-platform (processed 2026-09-08) RATIFIED keep-both from its side. This pass must resolve from the liquidity side, treating research/credit-risk-platform.md §Boundary Findings as counterparty.
2. **Seat boundary vs Liquidity Management Platform** (processed 2026-09-08) — that pass held the corporate-vs-bank/regulatory seam "conceptually, NOT verified against a sampled bank-side product" and asked this pass to ratify from its side. This pass must discharge that flag with product evidence.
3. **Sibling seam vs Market Risk Platform / Credit Risk Platform** — same hub family, different loss driver; market-risk-platform remains unprocessed (counterparty).

Secondary boundaries: Treasury Management System (both corporate and bank-treasury readings), Cash Management Platform, Regulatory Reporting Platform, ALM/balance-sheet-management platforms (no separate directory leaf — relationship must be recorded without inventing one).

## Initial Boundary (working hypothesis before research)

- Hypothesis: financial-institution-side (bank primarily) software that measures, monitors and controls the institution's risk of being unable to meet its obligations as they fall due — its liquidity risk. Center of gravity: the funding/liquidity position of the balance sheet, adequacy measures (coverage-style, stable-funding-style, maturity-mismatch), stress scenarios of outflows, buffers of liquid assets, contingency funding, and prudential/regulatory liquidity metrics (LCR/NSFR-family).
- Nearest confusions:
  - **Liquidity Management Platform** (processed) — corporate treasury steering the firm's own cash (consolidated position + projection + funding/deployment actions). Different seat, different objects.
  - **Financial Risk Management Platform** (processed) — institution-wide cross-risk hub; this leaf is expected to be the liquidity slice.
  - **Market Risk Platform / Credit Risk Platform** — sibling slices (price risk / default risk vs funding risk).
  - **Treasury Management System** — corporate instrument management; but bank-treasury deal-capture systems share the word "treasury" (MORS sells a bank TMS module).
  - **Regulatory Reporting Platform** — figures vs report production.
  - **ALM platforms** — asset-liability management platforms carry liquidity risk alongside IRRBB and profitability; no ALM leaf exists in the directory, so the relationship must be documented as packaging, not as a missing leaf.
- Unknowns: whether regulatory ratio computation (LCR/NSFR) is definitional or a common layer; whether intraday liquidity is definitional or a variant; whether stress machinery is definitional (it feels more central here than in credit risk); how the ALM-suite pole relates to the standalone pole; whether non-bank audiences (funds, insurers) are variants.

## Research Questions

1. What does the system hold as its record? (balance sheet? cash flows? securities inventory? ratios?)
2. What adequacy measures exist (LCR/NSFR-style, ladders, survival horizon, internal limits) and are they definitional?
3. How do stress/scenario assumptions work (run-off, rollover, buffer assumptions; regulatory vs internal scenarios)?
4. What does monitoring/control look like (limits, thresholds, early warnings, ALCO reporting, contingency funding)?
5. Is intraday liquidity definitional or a variant?
6. What is the data foundation (deal-level import, lineage, securities inventory)?
7. Who are the users and roles (liquidity risk officers, ALM quants, ALCO, treasury)?
8. Where are the boundaries (hub, siblings, liquidity management, TMS, reg reporting, ALM)?
9. Historical check: would pre-Basel III liquidity management (gap analysis, internal ratios, buffers, CFP) still fit the definition?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer levels:

| Product | Pole | Customer level | Evidence |
|---|---|---|---|
| Oracle Financial Services — Liquidity Risk Solution (within FS Risk Management family) | enterprise suite module; regulatory-rule-led | global banks; fund-industry variant documented | A (official family page) |
| Murex — MX.3 for Enterprise Liquidity Risk (within MX.3 ERM) | capital-markets platform; trading+banking book | large global banks | A (official ERM page, dedicated liquidity section) |
| QRM — Quantitative Risk Management (balance-sheet management / ALM applications) | analytics/consultancy-led balance-sheet platform | large banks, thrifts, credit unions, building societies; insurers/mortgage lenders adjacent | A (official homepage, depository-institution section) |
| MORS Software — ALM with Liquidity & Intraday Liquidity Risk Management | mid-tier specialist; all-in-one ALM+TMS for small/medium banks, point solutions for large banks | European challenger/neobanks and mid-tier banks | A (official homepage + ALM product page) |

Rejected/abandoned samples:
- **Wolters Kluwer OneSumX** (regtech pole, LCR/NSFR/ALM) — `wolterskluwer.com` returned 403. Abandoned per network-limitation rule after one attempt.
- **Abrigo** (US community-bank ALM pole) — `abrigo.com/alm/` returned 502. Abandoned after one attempt.
- **FIS / Finastra / Moody's** — not attempted within budget after four products reached stop conditions (credit-risk pass already documented Moody's as a data/ratings pole for credit, not liquidity).

Sample covers: enterprise suite module, capital-markets platform, balance-sheet/ALM analytics-led platform, mid-tier all-in-one specialist; global banks through challenger banks; prudential and internal management views; fund and insurance audience extensions documented at two vendors.

## Sources

All fetched 2026-09-08, Layer A (official vendor pages):

- Oracle — Financial Services Risk Management family page (incl. "Monitor and manage liquidity risk" section, Stress Testing section, fund-industry business brief reference): https://www.oracle.com/financial-services/analytics/financial-services-risk-management/
- Oracle — Liquidity Risk Management datasheet PDF: https://www.oracle.com/a/ocom/docs/industries/financial-services/liquidity-risk-management-ds.pdf (linked from family page; **not fetched** — prior passes showed Oracle datasheet PDFs return binary content)
- Murex — Enterprise Risk Management page (incl. "Enterprise liquidity risk" section): https://www.murex.com/en/solutions/business-solutions/enterprise-risk-management
- QRM — homepage (Depository Institution / Mortgage Lender / Insurance Company sections, seminar program): https://www.qrm.com/
- MORS Software — homepage: https://morssoftware.com/
- MORS Software — Asset Liability Management product page (Liquidity Risk / Intraday sections): https://morssoftware.com/mors-solution/asset-liability-management/
- Local (prior passes): research/credit-risk-platform.md (sibling slice, joint-review counterparty); research/liquidity-management-platform.md (corporate-seat sibling, seat-boundary flag to discharge); research/financial-risk-management-platform.md boundary findings (via STATUS.md); STATUS.md Boundary Issues lines for both flags.

**Source-access limitation:** no authenticated help-center / operational documentation was reachable for any sampled product (Wolters Kluwer 403; Abrigo 502; Oracle datasheet PDF not fetched as binary). All evidence is official product/solution-page level (Layer A) plus cross-product commonality (Layer B). Precise numeric claims (ratio thresholds, limit values, refresh windows, default assumptions) are deliberately not asserted anywhere.

---

## Product Observations

### Oracle Financial Services — Liquidity Risk Solution (Evidence Layer A)

- Family positioning: risk management software "spans credit, market, liquidity, interest rate, and business risk to provide you with a single, consistent view of risk and performance." Liquidity appears as a **named distinct product** in the family feature list ("Liquidity risk solution") — direct evidence for the hub-sells-slices pattern.
- Liquidity product: "Oracle Financial Services Liquidity Risk Solution enables banks to comply with ever-changing regulatory guidelines through flexible, prebuilt rules for different jurisdictions." — regulatory-rule-led positioning; jurisdiction rule packs are the named machinery. (LCR/NSFR not named on the fetched page — not asserted for this product.)
- Fund-industry variant: "Handling liquidity risk in investment funds" business brief — "the challenges of building and sustaining good liquidity risk measurement practices in the mutual fund industry, and learn how the versatility of the Oracle Financial Services Liquidity Risk Management solution can help." — same solution family sold into fund liquidity measurement (audience variant evidence).
- Stress machinery (sibling product in family): Stress Testing and Scenario Analysis assesses "the impact of a single set of scenarios across a diverse set of metrics, including provisions, interest income, net interest income, profitability, risk-weighted assets, capital, leverage, and **liquidity**"; meets "stress testing, sensitivity, and scenario analysis requirements for IFRS 9, the Internal Capital Adequacy Assessment Process (ICAAP), and the **Internal Liquidity Adequacy Assessment Process (ILAAP)**"; supports "what-if analysis, scenario analysis, stress tests, ad hoc impact assessments, attribution analysis, and reverse stress testing."
- Data foundation: "single source of truth for risk assessment … centralized, aggregated risk data through a unified financial services data model and common analytical infrastructure."
- Balance Sheet Management named as a separate family solution ("Optimize reward versus risk with accurate, up-to-date financial information") — ALM-adjacent packaging inside the same family.

### Murex — MX.3 for Enterprise Liquidity Risk (Evidence Layer A)

- Suite positioning: "MX.3 provides enterprise solutions that allow banks to control market, credit, and liquidity risk for internal and regulatory compliance. This is complemented by a real-time limit and exposure monitoring solution." Liquidity risk is a **named distinct solution** within the ERM suite (brochure "MX.3 for Enterprise Liquidity Risk" exists as a download).
- Enterprise liquidity risk section (full quote): "The MX.3 platform offers banking book integration, a centralized inventory of all securities including from trading activity, securities lending and borrowing, repo collateral and securities held or pledged as collateral assets. The powerful MX.3 cash flow engine strengthens the solution by generating contractual flows and estimates future flows across all asset classes, enabling real-time monitoring of liquidity ladders. It facilitates the optimization of HQLA buffers and compliance checking."
  - → position machinery: banking-book integration + centralized securities inventory (trading, SFT, repo collateral, pledged assets)
  - → cash-flow machinery: contractual flows + estimated future flows across asset classes
  - → measurement surface: liquidity ladders monitored in real time
  - → buffer machinery: HQLA buffer optimization
  - → compliance: compliance checking
- Suite-level control (liquidity included): limits solution "covers the range of exposures for market, credit, liquidity and operational risks across trading, banking and investment books"; risk controller actions: "limit suspension, trade hedging or blocking contracts breaching limits"; "Limits can be temporarily increased, or the limit line can be reallocated across business units and desks"; "Business dashboards summarize excess causes and resolution time"; "full management of limit excesses … Breaches are routed to a proper investigation and resolution of causes"; four-eyes validation on reference-data and limit changes.
- Regulatory machinery: prepackaged regulatory content, local regulatory watch, support for Basel standards exceptions; shared reference data repository + common calculation framework enforcing risk-figure consistency across regulatory reporting solutions.
- Roles named: CRO, CTO, Head of market risk, Head of credit risk, Head of finance, XVA trader, Risk controller.

### QRM — Quantitative Risk Management (Evidence Layer A, positioning/capability level)

- Positioning: risk consultancy + research/data provider + **applications developer**; "high-precision cloud technology … a single foundation for measuring risk and calculating the best allocation of capital"; audience: "commercial banks and thrifts, credit unions, building societies, mortgage lenders, REITs, asset management companies, and insurance companies."
- Depository-institution capability map — liquidity appears as a first-class measured risk inside **Balance Sheet Measurement → Risk Profile and Limit Monitoring**: "Credit Risk; **Short-Term (LCR) and Structural (NSFR) Liquidity Risk**; Trading (FRTB) and Structural (IRRBB) Market Risk." — LCR named as the short-term liquidity measure, NSFR as the structural one, monitored alongside credit and market risk lines.
- Balance Sheet Management: "ALM Mismatch Alignment; Campaign Design and Monitoring; **Funding Availability and Optimization**; Hedge Identification…; Portfolio Restructuring and Optimization."
- Strategy/forecasting: "**Liquidity Planning and Contingencies**"; "Pro-Forma Capital and **Liquidity Sources and Uses** Analyses."
- Stress testing: "Stress Testing Design and Execution — … Traditional Silo-Based Capital Stress Testing and **Liquidity Stress Testing**"; "Recovery and Resolution Simulation and Planning (RRP)."
- Risk assessment: "(ICAAP / **ILAAP**)."
- FTP: "Profitability Measurement and Funds Transfer Pricing (FTP) — **Funding, Liquidity, and Option Risk Transfer**" — liquidity risk priced/transferred inside FTP.
- Behavior models: "Our researchers also design, develop, apply, and defend **customer behavior models** for the financial products our clients offer" — the behavioral-assumption machinery behind deposit run-off/rollover.
- Seminar program (official, dated): "Liquidity and Capital Stress Testing" (twice), "Modeling the Funding Plan", "Validating and Backtesting Deposit Models", "An Introduction to Resolution and Recovery Planning", "Integrating Risk Appetite into the Strategic Plan" — the working curriculum of the type.
- Insurance segment: "Liquidity Risk" listed among exposure calculations (alongside lapse, longevity, market, credit) — audience variant.

### MORS Software — ALM / Liquidity Risk (Evidence Layer A, richest operational detail of the sample)

- Positioning: "ALM software for banks that covers Financial Risk Management for Interest Rate, Liquidity and Credit Risk. Fully fledged profitability and performance forecasting." Sold as one integrated ALM system **or as point solutions**; "All-in-one Treasury and ALM Solution for Medium & Small Banks" and "Advanced Point Solutions for Large Banks … such as IRRBB, **Liquidity Risk Management**, and **Intraday Liquidity Risk**."
- Liquidity Risk section (full quote): "MORS Liquidity Risk covers both Liquidity and Intraday Liquidity Risk Management. With MORS, it is easy to measure key Liquidity Risk Indicators such as the **LCR, NSFR and Survival Horizon** in real-time or near-time. MORS also provides **liquidity ladder style reporting**, meaning calculations such as the Additional Liquidity Monitoring Metrics (ALMM) are supported. The MORS **rule engine** allows a broad range of scenarios to be set up, both **regulatory scenarios and scenarios for internal use**. In the scenario definition, the user can for example define **inflow and outflow assumptions, as well as assumptions for the liquid asset buffer**. **Forecasts for ratios are fully supported as well as historical analysis of key ratios and their components**."
- Intraday liquidity (full quote): "MORS supports Intraday Liquidity Risk Management both for **regulatory purposes**, for **operative intra-daily cash management**, as well as for **forecasting liquidity in the next business days**. Nostro account balances and payments can be imported from Swift messages (MT and Camt formats). MORS also supports IBM MQ messages. Finally, Open Banking style APIs are also an option for importing account balances and payments. A comprehensive set of reports for intraday analysis is included. These cover both the historical angle, as well as forward looking analysis."
- Position machinery: "Balance sheet imported into MORS on **single deal level**, providing excellent **data lineage** and superb analysis from a **top of the house view to single deal and single cashflow analysis**."
- Dual view: "Financial risks are covered both from **prudential and from internal risk management** points of view."
- Governance surface: "Visualization tools … especially for use at for example **board level and ALCO meetings**, providing excellent key decision support."
- Vendor philosophy (blog titles): "Why Intraday Liquidity Should Not Be a Standalone System"; "Intraday Liquidity for Instant Payments: What Banks Need to Operationalise" — intraday argued as integrated, not standalone (vendor-internal evidence of the intraday-as-module question).
- Deployment: Full SaaS / Private Cloud / On-Premise. Client base: European challenger/neobanks (Monzo, bunq, Oxbury, GB Bank, Chetwood, Northmill logos displayed) — the challenger-bank customer level.

---

## Cross-product Comparison

| Finding | Oracle | Murex | QRM | MORS | Evidence | Layer |
|---|---|---|---|---|---|---|
| Consolidated funding/liquidity position of the balance sheet as the record | A (unified data model; rules over bank data) | A (banking book integration + centralized securities inventory) | A (balance sheet measurement; sources & uses) | A (deal-level balance sheet import, lineage) | B (4/4) | L0 |
| Cash-flow view: contractual + estimated/behavioral future flows | implied (rules compute metrics) | A (cash flow engine: contractual + estimated flows) | A (behavior models; sources & uses) | A (single-cashflow analysis; scenario assumptions) | B (4/4) | L0–L1 |
| Adequacy measures: coverage / stable-funding / ladder-mismatch families | A (prebuilt jurisdiction rules; metrics unnamed) | A (liquidity ladders; HQLA buffers; compliance checking) | A (LCR short-term + NSFR structural, named) | A (LCR, NSFR, Survival Horizon, ladders/ALMM, named) | B (4/4) | L0 |
| Stressed views / scenario machinery | A (stress product covers liquidity metrics; ILAAP; reverse stress) | partial (suite stress testing; liquidity-specific stress not named on page) | A (liquidity stress testing; liquidity planning & contingencies; RRP) | A (rule engine: regulatory + internal scenarios; inflow/outflow + buffer assumptions) | B (3–4/4) | L0 (stressed view) / L1 (machinery) |
| Ongoing monitoring & control vs appetite | A (compliance reporting; dashboards via stress product) | A (real-time limits covering liquidity; breach investigation; limit suspension/blocking) | A (Risk Profile and **Limit Monitoring** incl. liquidity) | A (real-time/near-time indicators; ratio monitoring; ALCO visualization) | B (4/4) | L0 |
| Regulatory ratio computation (LCR/NSFR named) | rules-led (unnamed) | compliance checking (unnamed) | A (named) | A (named) | B (2/4 named, 4/4 regulatory) | L1 |
| Intraday liquidity monitoring | — (not observed) | partial (intraday limit usage, suite-level) | — (not observed) | A (full: regulatory + operative + next-days forecast; nostro/SWIFT/API feeds) | B (1–2/4) | L1–L2 |
| HQLA / liquid-asset buffer management | — (not named) | A (HQLA buffer optimization) | — (not named) | A (buffer assumptions in scenarios) | B (2/4) | L1 |
| Contingency funding / recovery & resolution | — (not observed) | — (not observed) | A (Liquidity Planning and Contingencies; RRP seminar) | — (not observed) | B (1/4) | L1–L2 |
| Behavioral/deposit models | — | — | A (customer behavior models; deposit-model validation seminars) | A (scenario assumption definition) | B (2/4) | L1 |
| Deal-level data lineage / unified data foundation | A (unified data model) | A (shared reference data repository) | implied (single foundation) | A (single-deal-level import, lineage) | B (4/4) | L1 |
| Governance reporting (ALCO/board) | — (not named) | A (business dashboards to senior management) | A (risk-appetite integration seminars) | A (board/ALCO visualization) | B (3/4) | L1 |
| Funding-cost awareness (FTP linkage) | — | — | A (FTP: funding, liquidity, option risk transfer) | A (profitability/FTP in ALM suite) | B (2/4) | L1–L2 |
| Ratio history + forecast | — | — | — (not stated) | A (forecasts for ratios; historical analysis of ratios and components) | single-product | L1 |
| Non-bank audience extension (funds / insurers) | A (fund-industry brief) | — | A (insurance: liquidity risk among exposures) | — | B (2/4) | L2 |
| Prudential + internal dual view | implied (regulatory + stress) | A ("internal and regulatory compliance") | A (ICAAP/ILAAP; economic + regulatory) | A (explicit: "both from prudential and from internal risk management points of view") | B (4/4) | L1 |
| Freshness: real-time/near-time vs batch | — | A (real-time ladders) | — (cloud, quarterly evolution) | A (real-time/near-time) | B (2–3/4) | L1–L2 |
| Packaging: suite module / platform module / ALM-led / all-in-one | suite module | platform module | ALM/balance-sheet-led | all-in-one + point solutions | B (4/4 poles) | L2 |

### Modeling observations

- **The record is the balance sheet's funding-and-cash-flow structure, not a cash position.** Every product's center is the institution's balance sheet organized into flows: MORS imports the balance sheet at single-deal level; Murex integrates the banking book and keeps a centralized securities inventory (including repo collateral and pledged assets) and runs a cash-flow engine over it; QRM measures the balance sheet and projects sources and uses; Oracle computes regulatory liquidity metrics over unified bank data. This is categorically different from the corporate liquidity-management record (consolidated cash across bank accounts).
- **Measures are adequacy quantities under assumptions.** The measure families are coverage of net outflows by liquid assets (LCR-style), structural funding (NSFR-style), maturity ladders/mismatch, survival horizon — and every one of them is a function of *assumptions* (run-off rates, rollover, buffer composition). MORS makes the assumption layer explicit (rule engine with inflow/outflow and buffer assumptions); QRM's behavior models serve the same leg; Murex's "estimated future flows" is the same structure.
- **The stressed view is intrinsic to the measurement, not an add-on.** Liquidity risk is only visible under outflow stress; all four products compute measures under regulatory and/or internal scenarios. (Murex's page names ladders and compliance but not a liquidity scenario engine — calibrated: stressed view is cross-product at the conceptual level; elaborate scenario machinery is common.)
- **Control is appetite-shaped**: limits/thresholds on ratios and exposures (QRM "limit monitoring", Murex real-time limits covering liquidity, MORS real-time indicators), buffer requirements, early-warning indicators, breach handling, and governance reporting to ALCO/board — plus regulatory compliance as a standing output.
- **Two clocks**: the daily/EOD ratio world and the intraday payment-flow world. MORS is the only sample documenting the intraday loop in product detail (and argues it should not be a standalone system); Murex covers intraday limit usage at suite level. Intraday is common-mature, not definitional.
- **Prudential and internal views coexist on one position** — explicit at MORS, visible at all four (regulatory compliance + internal risk management as two measure sets over the same data).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal, jointly-held)

Three jointly-held structures:

1. **The institution's liquidity position of record** — a consolidated, inspectable view of the institution's funding structure and cash flows: assets, liabilities and off-balance-sheet commitments organized by maturity, product, currency and entity, with the liquid-asset buffer identified (deal/instrument-level detail is the common implementation). *Remove → a treasury cash view or an ALM calculator with nothing to measure.*
2. **Liquidity adequacy measures under current and stressed views** — the position translated into governed quantities of the institution's ability to meet obligations as they fall due: coverage of net outflows by liquid assets, structural/stable-funding measures, maturity-mismatch/ladder measures — computed under the current view and under stressed assumptions (outflow run-off, funding-market closure). *Remove → cash-flow reporting; the "risk" half is gone.*
3. **Ongoing monitoring and control against liquidity risk appetite** — the liquidity state kept under continuous supervision: limits/thresholds and buffer requirements, early-warning indicators, breach/exception handling, and governance/regulatory reporting. *Remove → a one-off calculation tool rather than an operating platform.*

Jointly-held is load-bearing:
- 1+3 without 2 = a funding register with governance but no measurement
- 2+3 without 1 = a calculator/model with no institutional position
- 1+2 without 3 = liquidity analytics/reporting, not management

Not in L0 despite being near-universal: LCR/NSFR computation as named regulatory ratios (a common implementation of structure 2), intraday liquidity monitoring, HQLA optimization machinery, contingency funding plans, behavioral model factories, deal-level lineage, real-time engines, AI.

### L1 — Common Mature Structure

- Regulatory liquidity ratio machinery — coverage and stable-funding measures computed under jurisdiction rule sets (LCR/NSFR named at two of four; regulatory rule packs at the others); Additional-monitoring-metrics-style ladder reporting
- Liquidity ladders / maturity mismatch views — contractual and behavioral cash flows bucketed over time
- Behavioral/assumption machinery — run-off, rollover, prepayment, deposit-behavior models; scenario assumption definition (inflow/outflow rates, buffer composition)
- Scenario and stress machinery — regulatory scenario sets and internal scenarios; ratio forecasting; reverse stress; recovery/resolution planning support
- Intraday liquidity monitoring — payment-flow-based intraday position, intraday limits/indicators, next-days liquidity forecasting (common-mature; module-integrated vs standalone is a vendor-philosophy question)
- HQLA / liquid-asset buffer management — inventory of eligible securities incl. pledged/repo collateral; buffer optimization
- Contingency funding planning — contingency funding plans, funding-plan modeling, recovery & resolution support
- Unified data foundation — deal-level import with lineage, shared reference data, reconciliation discipline
- Governance reporting — ALCO/board dashboards, ratio history and forecasts, risk-appetite reporting
- Funding-cost awareness — FTP linkage (funding/liquidity risk transfer pricing)
- Prudential + internal dual view — same position, two measure sets (regulatory compliance and internal risk management)

### L2 — Variant / Optional Structure

- Packaging: enterprise suite module vs capital-markets platform module vs ALM/balance-sheet-led platform vs mid-tier all-in-one (ALM+TMS)
- Audience extension: investment funds (fund liquidity measurement), insurance companies (liquidity among actuarial exposures)
- Freshness posture: batch EOD vs real-time/near-time vs intraday-integrated
- Bank-size poles: large-bank point solutions vs small/mid-tier all-in-one
- Intraday as integrated module vs standalone system (vendor philosophy split)
- Deployment: SaaS / private cloud / on-premise
- Regional regime emphasis (EU ILAAP/ALMM-flavored vs US LCR/NSFR/internal measures) — inferred from product mentions, not sampled regionally

### L3 — Vendor-specific (Research Notes only)

- Oracle: "flexible, prebuilt rules for different jurisdictions" positioning; fund-industry business brief; stress-metric list (provisions, NII, leverage, liquidity…); ILAAP/ICAAP stress framing; unified financial services data model; Balance Sheet Management as sibling family solution.
- Murex: centralized securities inventory spanning trading/SFT/repo/pledged collateral; cash flow engine across asset classes; real-time liquidity ladders; HQLA buffer optimization; four-eyes limit/reference-data validation; surgical recomputation; ISDA unit-test licensing (credit/market side); brochure "MX.3 for Enterprise Liquidity Risk".
- QRM: consultancy+applications model; LCR-as-short-term/NSFR-as-structural framing inside "Risk Profile and Limit Monitoring"; ALM Mismatch Alignment; Funding Availability and Optimization; Liquidity Planning and Contingencies; RRP; FTP "Funding, Liquidity, and Option Risk Transfer"; customer behavior models; seminar curriculum (liquidity & capital stress testing, funding-plan modeling, deposit-model validation, resolution & recovery planning); insurance/mortgage-lender segments.
- MORS: LCR/NSFR/Survival Horizon named indicators; ALMM ladder reporting; rule engine with regulatory + internal scenarios and buffer assumptions; ratio forecasts + component-level history; intraday via SWIFT MT/Camt, IBM MQ, Open Banking APIs; single-deal-level balance sheet import with lineage; "prudential and internal" dual-view phrasing; board/ALCO visualization; MORSia AI assistant; challenger/neobank client base; "intraday should not be standalone" blog position; 4–8 month implementations claim.

## Vendor-specific Findings

- Intraday liquidity depth (nostro feeds via SWIFT MT/Camt, IBM MQ, Open Banking APIs; operative + regulatory + next-days forecast) is directly evidenced only at MORS → product-specific depth; the *existence* of intraday monitoring as common-mature is supported by Murex suite-level intraday limit usage + market structure, but the detailed machinery is not generalized.
- "Survival Horizon" and "ALMM" as named measures are MORS-specific vocabulary → do not generalize as the type's standard measure names.
- QRM's FTP-integrated liquidity transfer pricing is a balance-sheet-management philosophy feature → variant, not core.
- Oracle's fund-industry positioning and QRM's insurance listing are audience extensions → variants.
- Murex's four-eyes limit governance is suite-level risk-control machinery (also recorded in the credit-risk pass) → product-specific implementation of the control leg.

## Boundary Findings

- **vs Financial Risk Management Platform (processed; joint-review flag)** — RESOLVED from this side: **keep both (hub + slice), ratified**, consistent with the credit-risk pass's ratification. Evidence: Oracle sells "Liquidity Risk Solution" as a named distinct product within its FS Risk Management family; Murex sells "MX.3 for Enterprise Liquidity Risk" as a distinct solution/brochure within its ERM suite; MORS packages "Liquidity Risk Management" as a point solution for large banks within its ALM suite; QRM monitors liquidity as a distinct risk line within balance-sheet measurement. The hub's center of gravity is cross-risk-type (shared data foundation, cross-risk aggregation, consolidated limits, enterprise reporting); the liquidity slice's center of gravity is liquidity-type depth (funding structure, coverage/stable-funding/mismatch measures, buffers, contingency funding, prudential liquidity compliance). Neither reduces to the other: remove cross-risk aggregation from the hub and it becomes one of the slices; remove funding/adequacy semantics from this type and it becomes the generic hub. Each form also exists standalone (MORS sells liquidity risk management as a point solution; mid-tier banks buy liquidity/ALM without an enterprise hub).
- **vs Liquidity Management Platform (processed; seat-boundary flag DISCHARGED from this side)** — the flag held there ("bank/regulatory prudential liquidity vs corporate steering… NOT verified against a sampled bank-side product") is now verified with product evidence: all four sampled products are financial-institution-side — their objects are balance-sheet funding structures, regulatory liquidity metrics, HQLA buffers, ALCO governance and prudential compliance; their users are bank treasury/ALM/risk functions. The corporate liquidity-management record (consolidated cash across the corporate's own bank accounts/entities + projection + funding/deployment steering) does not appear in any sampled product. The seam is the **seat and the object**: the financial institution's risk function measuring its own funding adequacy (this type) vs the corporate finance function steering its own cash (that type). Naming trap recorded: "liquidity management" (corporate) vs "liquidity risk" (institution prudential) blur in market copy, but the product populations are distinct; bank treasury sits between the two (it *manages* funding day-to-day in treasury systems and *measures/controls* the risk in this type).
- **vs Market Risk Platform / Credit Risk Platform (siblings; credit processed, market unprocessed)** — same hub family, different loss driver: inability to fund obligations as they fall due (this type) vs adverse market-price movement (market) vs obligor default (credit). Interplay noted: credit deterioration can trigger liquidity outflows (collateral calls, rating-triggered draws) and market stress can close funding markets — the risk types interact, but the measured objects and measure families differ. market-risk-platform remains unprocessed — its pass should treat research/credit-risk-platform.md and this file as counterparties.
- **vs Treasury Management System** — two readings, both distinct from this type: (a) corporate TMS (instrument/payment management for the corporate treasury seat — the liquidity-management pass's superset); (b) bank treasury systems (deal capture, position keeping, trade processing — MORS sells a bank TMS module alongside its ALM module). The liquidity risk platform is the **risk measurement/control layer over the funding position**; bank TMS is the front/middle-office deal layer that feeds it. MORS selling ALM and TMS as separate modules of one suite is vendor-internal evidence of separability.
- **vs ALM / Balance Sheet Management platforms (no directory leaf)** — ALM platforms (QRM, MORS) carry IRRBB + liquidity risk + profitability/FTP on one balance-sheet foundation. This leaf documents the **liquidity-risk capability** as the type; an ALM-suite realization satisfies it when liquidity risk is a first-class measured/monitored/controlled surface (true for both sampled ALM vendors). IRRBB/profitability are sibling capabilities inside the same platform family, not part of this type's core. No taxonomy change proposed; the relationship is packaging, not a missing leaf.
- **vs Regulatory Reporting Platform** — this type computes liquidity risk figures (ratios, ladders, buffer positions) as part of risk management; reg-reporting produces/submits the reports (liquidity returns among them). Same figures-vs-reports seam as the credit-risk pass found.
- **vs Cash Management Platform (§08, unprocessed)** — corporate-side present-tense position + money movement (and bank-side cash management for corporate clients). Different seat and different clock (present movement vs forward adequacy under stress). The cash-management pass should treat research/liquidity-management-platform.md §Boundary Findings as its primary counterparty; this type is separated from it by the same seat test as Liquidity Management Platform.
- **vs Financial Planning & Analysis / Budgeting & Forecasting** — corporate planning layer; feeds plan data into corporate liquidity projection. Not the institution's prudential risk view.
- **Fund/insurance liquidity risk** — audience variants of this type's machinery (Oracle fund brief; QRM insurance listing), not separate types; fund liquidity (redemption liquidity of pooled investments) is the most divergent variant and may deserve its own pass if the market grows dedicated products.

## Uncertainties

1. **No Tier-1 operational documentation** was reachable (help centers gated; Wolters Kluwer 403; Abrigo 502; Oracle datasheet PDF not fetched). All observations are product/solution-page level. Screen-level workflow details (exact ladder bucketing, exact limit-state names, exact approval chains, default assumption values) are not asserted anywhere.
2. **Murex liquidity-specific stress machinery** is not named on the fetched page (suite stress testing is market-risk framed); the stressed-view leg for Murex is inferred from "estimated future flows" + compliance checking + suite machinery — calibrated as partial.
3. **Oracle's liquidity product depth** rests on one positioning paragraph + family context; the datasheet PDF was not fetched (binary). LCR/NSFR are not asserted for Oracle specifically.
4. **Regional regime packaging** (EU vs US emphasis) inferred from product mentions (ILAAP, ALMM, EBA-style rule packs) but not sampled regionally.
5. **Intraday liquidity** is deeply evidenced at one product only; its common-mature status rests on that product plus Murex suite-level intraday limits and market structure — held at L1 with a product-specific depth note, not promoted to core.
6. **Contingency funding planning** is directly evidenced at one product (QRM) → L1/L2 boundary, kept out of core.
7. The **fund-liquidity variant** (pooled-investment redemption liquidity) may be structurally different enough (investor redemption flows vs balance-sheet funding) that a future dedicated pass could split it — recorded as a variant with a split-watch note, no directory change proposed.

## Historical / Market-Sample Check (§24 reasoning)

Would older, regional, platform-native products still fit? Yes under the three-structure core: a pre-Basel III (1980s–2000s) bank treasury/ALM function maintained a maturity ladder/gap view of its balance sheet (structure 1), computed internal liquidity ratios and mismatch measures under behavioral assumptions (core-deposit stickiness, rollover rates) — the stressed view in embryo (structure 2), and ran liquidity limits, liquid-asset buffer policies, contingency funding plans and ALCO reporting (structure 3) — without LCR/NSFR (introduced 2010s), intraday monitoring frameworks (2013+), HQLA classification machinery, real-time engines or AI. Conversely, a corporate cash-forecasting tool without balance-sheet funding semantics does not fit (it is Liquidity Management / cash management territory); a regulatory-report generator without a measured position does not fit (it is Regulatory Reporting); a deal-capture treasury system without measurement does not fit (it is a bank TMS). The definition therefore does not overfit the current prudential-ratio implementation: LCR/NSFR, intraday monitoring and HQLA optimization stay in the common/variant layers.

## Final Synthesis

A Liquidity Risk Platform is the financial institution's liquidity-risk system of record: it holds the institution's funding position — the balance sheet's assets, liabilities and commitments as a structure of cash flows and liquid-asset buffers — translates that position into governed adequacy measures (coverage of net outflows, structural funding, maturity mismatch) under both current and stressed assumptions, and keeps the whole state monitored and controlled against the institution's liquidity risk appetite, feeding ALCO/board governance and prudential compliance. Its defining core is three jointly-held structures: the liquidity position of record, adequacy measures under current and stressed views, and the ongoing monitoring-and-control loop. Around this core, mature products add regulatory ratio machinery (LCR/NSFR-family), liquidity ladders, behavioral assumption engines, scenario/stress machinery, intraday liquidity monitoring, HQLA buffer management, contingency funding planning, unified deal-level data foundations, governance reporting and FTP linkage. The market realizes the type along several poles: enterprise suite modules (regulatory-rule-led), capital-markets platform modules (banking book + securities inventory + cash-flow engine), ALM/balance-sheet-led analytics platforms, and mid-tier all-in-one ALM+TMS specialists — with audience extensions to funds and insurers. Boundaries: the multi-risk hub above it (ratified hub+slice from this side), market/credit sibling slices (loss driver), the corporate-seat Liquidity Management Platform (seat + object — flag discharged with product evidence), bank/corporate treasury systems (deal layer vs risk layer), regulatory reporting (figures vs reports), and cash management (present movement vs stressed adequacy).
