# Research Notes — Credit Risk Platform

## Research Goal

Understand what a Credit Risk Platform actually is as a software type: its central objects (counterparty, exposure, credit quality measure, limit, portfolio), the workflows around them (exposure consolidation, credit-quality assessment, risk measurement, limit monitoring, stress/capital/ECL computation, reporting), the roles involved, and the boundaries against neighboring types — above all the umbrella-vs-slice joint-review flag against Financial Risk Management Platform, plus Credit Management Platform (trade credit, processed), Credit Decisioning Platform (processed), Credit Scoring Application, Loan Origination System, and the Market/Liquidity Risk sibling leaves.

## Initial Boundary

- Expected: software used by financial institutions (banks primarily; also specialized lenders, and to a lesser degree corporates monitoring counterparties) to measure, aggregate, monitor and control the risk of loss from borrowers/counterparties failing to meet obligations — the "credit risk" of the institution's positions.
- Nearest confusions:
  - **Financial Risk Management Platform** (processed) — institution-wide multi-risk layer; explicit joint-review flag recorded there: "umbrella-vs-slice … recommendation: keep all four leaves"; this pass must resolve from the credit-risk side.
  - **Credit Management Platform** (processed) — seller-side trade-credit system of record (customer credit accounts, AR exposure vs limits, order block/release). Different counterparty side and different machinery.
  - **Credit Decisioning Platform** (processed) — origination-time application evaluation; its final synthesis: "unit of work is the credit application … resolves it into an actionable credit decision".
  - **Credit Scoring Application** — score/scorecard production; likely a component of a credit risk platform, not the whole.
  - **Loan Origination System / Loan Management System** — case workflow and servicing vs risk measurement over positions.
  - **Market Risk Platform / Liquidity Risk Platform** (unprocessed siblings) — same hub, different loss driver.
  - **Regulatory Reporting Platform** — figures vs report production.
- Unknowns: whether limit machinery is definitional here (the hub also claims limits); whether regulatory-capital machinery (Basel RWA) is definitional or a common/variant layer; how the banking-book analytics pole and the trading-book counterparty pole relate; role model depth.

## Research Questions

1. What does the system hold as its record? (counterparties? exposures? ratings? loans?)
2. What credit-quality machinery exists (internal ratings, scorecards, PD models, external ratings/implied ratings)?
3. What risk measures are computed (EL, LGD, EAD, RWA, PFE, CVA, ECL) and over what scope (banking book, trading book, retail, wholesale)?
4. What is the monitoring/control loop (limits, breaches, watch lists, risk appetite)?
5. What scenario/stress machinery exists and how central is it?
6. What is the data foundation (unified data model, reference data, external data/ratings)?
7. Who are the users and roles?
8. Where are the boundaries (hub, siblings, trade-credit, decisioning, scoring, origination, reg-reporting)?
9. Historical check: would pre-Basel / regional / spreadsheet-era credit risk management still fit the definition?

## Representative Products

| Product | Why selected | Pole | Evidence level |
|---|---|---|---|
| SAS — Credit Risk Management solution family (incl. SAS Risk Engine, SAS Credit Scoring, SAS Solution for Regulatory Capital, SAS Allowance for Credit Loss; distributes Kamakura Risk Manager / KRIS) | analytics-led vendor; loan-portfolio credit risk; model development emphasis; banks + specialized lenders | banking-book analytics / modeling-led | A (official solution + product pages) |
| Oracle Financial Services — Credit Risk Analytics (within Financial Services Risk Management) | enterprise platform vendor; unified data model; retail + wholesale + counterparty across banking and trading books | suite-embedded enterprise platform | A (official solution page; datasheet PDF not machine-readable — see Sources) |
| Murex — MX.3 for Enterprise Credit Risk (within MX.3 ERM suite) | capital-markets front-to-risk platform; counterparty credit risk, PFE, regulatory capital, credit limits | trading-book / counterparty-led | A (official solution page) |
| Moody's (Moody's Analytics lineage) — Credit Risk capability (CreditView, Data Alliance, PD/implied-rating models, early-warning signals, CreditForecast) | data/ratings-led vendor; benchmarking + default-risk measures + portfolio monitoring | data/analytics-led | A (official capability page; product-level, not operational docs) |

Sample covers: two enterprise suites (analytics-led, platform-led), one capital-markets platform, one data/ratings vendor; banking book and trading book; regulated-bank and (Moody's) corporate audiences.

## Sources

- SAS — Risk Management solutions page: https://www.sas.com/en_us/solutions/risk-management.html (fetched 2026-09-08, Layer A)
- SAS — Credit Risk Management solution page: https://www.sas.com/en_us/solutions/risk-management/solution/credit-risk-management.html (fetched 2026-09-08, Layer A)
- SAS — Risk Engine product page: https://www.sas.com/en_us/software/risk-engine.html (fetched 2026-09-08, Layer A)
- Oracle — Financial Services Risk Management page: https://www.oracle.com/financial-services/analytics/financial-services-risk-management/ (fetched 2026-09-08, Layer A)
- Oracle — Credit Risk Analytics datasheet PDF: https://www.oracle.com/a/ocom/docs/industries/financial-services/ofs-credit-risk-management-ds.pdf (fetched 2026-09-08 — **binary, not machine-readable**; contents not used)
- Murex — Enterprise Risk Management page (incl. "Enterprise credit risk" section): https://www.murex.com/en/solutions/business-solutions/enterprise-risk-management (fetched 2026-09-08, Layer A)
- Moody's — Credit Risk capability page: https://www.moodys.com/web/en/us/capabilities/credit-risk.html (fetched 2026-09-08, Layer A)
- Local (prior passes): research/financial-risk-management-platform.md (hub boundary findings + joint-review flag); research/credit-decisioning-platform.md (final synthesis); research/credit-management-platform.md (trade-credit core, from STATUS.md summary); STATUS.md Boundary Issues line for the hub-vs-siblings flag.

**Source-access limitation:** vendor help centers / operational documentation (SAS documentation portal, Murex customer portal, Oracle OFSAA docs) were not reachable through this environment; the Oracle datasheet PDF returned binary content. All evidence is therefore product-page/positioning level (Layer A) and cross-product commonality (Layer B). No Tier-1 operational documentation was available; precise numeric claims, default values, and detailed screen-level behavior are deliberately not asserted.

## Product Observations

### SAS — Credit Risk Management solution family (Evidence Layer A)

- Solution positioning: "Deploy a broad range of scalable credit models to continuously manage your loan portfolios." "Optimize credit decisions and meet expected credit loss (ECL) accounting requirements by developing models that predict potential risks. Enjoy on-demand reporting and real-time decisioning you can trust."
- Scope: "analyze large credit portfolios down to individual loan assessments"; audience includes "a specialized lender or diverse multinational financial institution".
- Capability claims: automation of "complex risk management processes" with "well-defined, automated governance and workflow"; "customizable, adaptable data & reporting" — "flexible framework … to integrate and stage high-quality data", "transparency needed for a full range of on-demand reporting"; "powerful modeling environment" — build models in SAS code, Python, R, incl. AI/ML; champion/challenger model testing; "assess risk exposures and inform credit and pricing decisions using a broad range of scoring methodologies"; "comprehensive view of risk and model performance".
- Component products under the credit risk family: SAS Risk Engine ("Calculate exposures on demand in near-real time across risk types"; "Assess firmwide risk exposure intraday or in near-real time across all risk types – market, credit and liquidity"; "Complete risk aggregations. Assess market, liquidity and credit risk. And calculate exposure and CVA"), SAS Credit Scoring ("Develop, validate and monitor credit scorecards"), SAS Solution for Regulatory Capital ("single, end-to-end risk management environment" for regulatory risk), SAS Allowance for Credit Loss ("Address CECL and IFRS 9 requirements with a fully governed, automated workflow"), SAS Risk Modeling ("develop, validate, deploy and track risk models in house"), SAS Model Implementation Platform, SAS Regulatory Content for EBA Taxonomies, KRIS Risk Data and Analytics ("Forecast default risk across the full-term structure with proprietary models based on market, macro-economic and financial data as well as spread, implied ratings and sector analytics"), SAS Credit Origination (separate decisioning product — "automates decisions, orchestrates data"), SAS Credit Customer Management ("Detect, prevent and manage risk across the entire customer life cycle").
- Distributed partner products: Kamakura Risk Manager ("transaction-level valuation, income simulation, liquidity stress testing, cash flow analysis, credit-adjusted economic capital adequacy assessment and regulatory/accounting reporting in a single, integrated ALM solution").
- Roles implied: model developers, risk analysts, executives/business users ("interactive stress testing enables all levels of users – from quantitative analysts to business users").
- Vendor awards/claims (Chartis RiskTech100 categories incl. IFRS 9, Model Risk Management, Capital Optimization) — positioning signals only, not asserted.

### Oracle Financial Services — Credit Risk Analytics (Evidence Layer A)

- Family positioning: "helps improve how you measure, manage, mitigate, and report risk across your organization … spans credit, market, liquidity, interest rate, and business risk to provide you with a single, consistent view of risk and performance."
- Credit Risk Analytics: "brings together data from multiple sources to enable a holistic, enterprisewide view of credit risk, including retail, wholesale, and counterparty credit risk, across both the banking and trading books."
- Sibling product evidence for machinery: Stress Testing and Scenario Analysis — "Assess the impact of a single set of scenarios across a diverse set of metrics, including provisions, interest income, net interest income, profitability, risk-weighted assets, capital, leverage, and liquidity"; "stress testing, sensitivity, and scenario analysis requirements for IFRS 9, … (ICAAP), and … (ILAAP)"; "what-if analysis, scenario analysis, stress tests, ad hoc impact assessments, attribution analysis, and reverse stress testing"; "robust model management and governance to create, inherit, and manage in-house, Oracle, and third-party models"; "dynamic dashboards".
- Data foundation: "single source of truth for risk assessment … centralized, aggregated risk data through a unified financial services data model and common analytical infrastructure."
- Climate Change Analytics shows credit-model integration points: prebuilt scorecard framework "offers the flexibility to add … probability of default (PD) and loss given default (LGD) models" — evidence that PD/LGD-style parameters are native objects in the Oracle credit risk stack.
- Named solution family structure: separate products per risk type under one risk-management hub (credit / market / liquidity / stress / climate) — relevant to the umbrella-vs-slice question.

### Murex — MX.3 for Enterprise Credit Risk (Evidence Layer A)

- Suite positioning: "MX.3 provides enterprise solutions that allow banks to control market, credit, and liquidity risk for internal and regulatory compliance … complemented by a real-time limit and exposure monitoring solution." Per-risk solutions sold as distinct packages ("MX.3 for Credit Risk" brochure) under one ERM suite.
- Enterprise credit risk section: "MX.3 gives a consolidated view of exposures across entities with incremental intraday variation computed in batch or in real-time. This enterprise-wide solution … has a broad range of analytical and simulated methodologies, such as Monte Carlo potential future exposure (PFE). It provides accurate credit risk measures (e.g., issuer lending, notional, pre-settlement, settlement)—across all asset classes. The solution enables capital management via risk-weighted assets (RWA), including exposure-at-default either with a standard (e.g., SA-CCR) or internal model method (PFE with IMM waiver), CVA risk charge and central counterparty (CCP) capital charge calculation."
- Analysis surface: "credit risk officers take advantage of in-memory aggregation technology. From their day-to-day screen, they can slice and dice and drill down to the finest calculation inputs"; "a high-performance simulated PFE calculation engine gives end users access to an accurate real-time intraday exposure"; "surgical recomputation based on what is impacted" for corrections.
- Limits / control (suite-level risk control, credit included): "leading limits and exposure monitoring solution across multiple source systems in real-time … covers the range of exposures for market, credit, liquidity and operational risks across trading, banking and investment books"; risk controller actions: "limit suspension, trade hedging or blocking contracts breaching limits. … Limits can be temporarily increased, or the limit line can be reallocated across business units and desks. Business dashboards summarize excess causes and resolution time"; "full management of limit excesses … Breaches are routed to a proper investigation and resolution of causes"; "Validation workflows that include the four-eyes principle can be applied to all changes made on reference data and limits. The solution includes full access rights management and audit procedures."
- Client quote (Banorte, FRM Executive Director Risk): "we successfully implemented the Murex PFE solution to enhance the analytical credit risk solution and deploy more modern credit limit management metrics" — evidence that credit limit management metrics are part of the credit risk solution in practice.
- Consistency machinery: "shared reference data repository and a common calculation framework" enforcing "risk figure consistency across regulatory reporting solutions, such as CVA capital charge, counterparty credit risk risk-weighted assets (RWA), central counterparty (CCP) charge, large exposure reporting or leverage ratio."
- Roles named: CRO, Head of market risk, Head of credit risk, credit risk officers, risk controller, XVA trader.
- Regulatory content: "prepackaged regulatory content … local regulatory watch … support Basel standards exceptions"; ISDA-licensed validation (SA-CCR, SIMM, FRTB, SA-CVA unit tests).

### Moody's — Credit Risk capability (Evidence Layer A, product/positioning level)

- Positioning: "extensive data, actionable insights, and robust analytics to navigate uncertainty, strengthen your credit risk assessment"; "We help you monitor portfolios, manage exposures, and anticipate risks, so you can stay ahead of challenges, rebalance risk, and identify new opportunities."
- Data/ratings substrate: global credit insights "for over 460 million entities"; standardized financials ("all financial data standardized to Moody's Chart of Accounts"); benchmarking; ratings and research from Moody's Ratings; interactive scorecard tool "based on credit rating methodologies of Moody's Ratings and your qualitative inputs".
- Modeling and scoring: "Apply Moody's credit risk models to measure the financial soundness of more than 580 million pre-scored companies worldwide"; "Automated credit risk measures, with the option to use your own data"; "Forward-looking risk measures for every company in the dataset including Probability of Default (PD), Implied Ratings, and PD sector risk triggers"; "Early warning signal flags"; "300,000+ peer group comparisons, drivers of risks and sensitivities … news-based credit sentiment".
- Portfolio-level machinery: Data Alliance — "high-quality credit risk insights for portfolio-level benchmarking and data augmentation … Organizations often use Data Alliance to fill in data gaps in portfolios and conduct stress tests"; models "calibrate[d], regularly validate[d], and develop[ed] … to address regulatory reporting needs and loan origination, portfolio, and monitoring practices".
- Consumer credit: CreditForecast / Consumer Credit Analytics — "benchmark their portfolios against the credit market, conduct loss forecasting, perform stress-testing exercises, and ultimately make better lending decisions."
- Economic scenarios: "foundation of 'what if?' analysis, stress testing, and regulatory compliance" — scenario data feeding institutions' own stress machinery.
- Corporate audience: "We help corporations monitor the increased risk of their counterparties and adapt terms and conditions in advance of defaults or delayed payments" (trade-credit-adjacent use of counterparty credit data — boundary relevance).
- Chartis award categories visible on page: "Credit Risk for the Banking Book", "Credit Data Wholesale" (vendor-displayed positioning signal only).

## Cross-product Comparison

| Aspect | SAS Credit Risk Management | Oracle Credit Risk Analytics | Murex MX.3 Enterprise Credit Risk | Moody's Credit Risk |
|---|---|---|---|---|
| Center of gravity | credit risk analytics & model factory over loan portfolios | enterprise risk platform; credit risk view on unified data model | consolidated counterparty exposure + PFE + capital + limits inside capital-markets platform | external data/ratings/models feeding customers' assessment |
| Held records | credit portfolios, models, staged data | credit risk data across retail/wholesale/counterparty, banking+trading books | exposures across entities (intraday increments), reference data | entity credit measures (PD, implied ratings), benchmark datasets |
| Credit-quality machinery | scorecards (Credit Scoring), default-risk models (KRIS) | PD/LGD model slots (via scorecard framework) | counterparty exposure machinery (quality parameters implicit on fetched page) | PD, implied ratings, ratings methodologies, early-warning signals |
| Risk measures | ECL, regulatory capital, exposure, CVA | provisions, RWA, capital under scenarios | PFE (Monte Carlo), EAD (SA-CCR/IMM), pre-settlement/settlement/issuer/notional, RWA, CVA, CCP charge | PD, loss forecasting, forward-looking measures |
| Scenario / stress | stress testing family, what-if, champion/challenger | scenario impact across metrics incl. provisions/RWA/capital; reverse stress testing | stress testing in suite; PFE simulation | stress tests via Data Alliance; economic scenario datasets |
| Monitoring/control | on-demand reporting, real-time decisioning claims | dashboards, what-if | real-time limits, breach investigation/resolution, limit suspension/blocking, four-eyes limit changes | early-warning signals, rating-transition alerts, rebalancing guidance |
| Regulatory machinery | Regulatory Capital solution, EBA taxonomy content | IFRS 9 / ICAAP / ILAAP stress requirements | SA-CCR/IMM/CVA/CCP/large-exposure/leverage-ratio consistency; regulatory content packs | models for regulatory reporting needs |
| Data foundation | data integration & staging framework | unified financial services data model + common analytical infrastructure | shared reference data repository + common calculation framework | proprietary entity/financial data; standardized financials |
| Analysis surface | portfolio-to-loan drill-down | dashboards, attribution analysis | slice-and-dice drill-down to calculation inputs without recalculation | peer comparison charts, benchmarking |
| Roles | model developers, risk analysts, business users | risk function enterprise-wide | head of credit risk, credit risk officers, risk controller, CRO | credit teams at banks/corporates |

**Cross-product invariants (Layer B / C):**

1. Every product maintains a **credit-risk view of the institution's positions** — exposures attributed to identified counterparties/obligors and aggregated across products, books and entities (SAS "credit portfolios down to individual loans"; Oracle "holistic, enterprisewide view of credit risk … retail, wholesale, and counterparty … banking and trading books"; Murex "consolidated view of exposures across entities"; Moody's "monitor portfolios, manage exposures").
2. Every product carries **credit-quality assessment machinery** — some way of grading/grading-quantifying each obligor's default likelihood (scorecards, PD models, ratings, implied ratings, early-warning signals). (Murex page implies rather than names it — calibrated below.)
3. Every product **translates exposure × quality into credit risk measures** under current and adverse views (ECL/regulatory capital at SAS; provisions/RWA/capital at Oracle; PFE/EAD/CVA/RWA at Murex; PD/loss forecasting at Moody's). The measure families differ by pole but the "exposure plus quality produces a risk quantity" structure is common to all four.
4. Every product provides **ongoing portfolio-level monitoring and control surfaces** — dashboards/reports/limits/breaches/early-warning signals that keep the credit risk state under supervision and feed credit risk governance.

**Common but not definitional (Layer B):** scenario/stress machinery; regulatory capital computation (Basel-family RWA, SA-CCR/IMM/CVA); ECL accounting measures (IFRS 9 / CECL); model development/validation/governance environments; unified data models / shared reference data; drill-down analysis surfaces; early-warning signals; concentration/benchmarking views; external ratings & data integration.

**Pole-specific (Layer A, product-level):** in-memory grids and recomputation on correction (SAS, Murex); four-eyes validation on limit/reference-data changes (Murex); climate-risk analytics as credit-model extension (Oracle); proprietary pre-scored entity universe and Data Alliance benchmarking (Moody's); ALM-adjacent packaging via partner products (SAS/Kamakura).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Four jointly-held structures:

1. **The credit exposure position of record** — the institution's credit-risk view of who owes it what: identified counterparties/obligors carrying exposures aggregated from the institution's lending, trading and investment positions across products, books and entities. Remove → an obligor-rating tool or a loss-model library with nothing to measure.
2. **Credit-quality assessment attached to each obligor** — a governed, comparable measure of each debtor's default likelihood (internal rating scale, scorecard score, PD model output, external rating, or implied rating). Remove → an exposure register or ledger, not risk management.
3. **Computed credit risk measures** — exposure and quality combined into risk quantities under current and forward-looking/adverse views (expected loss, loss-given-default applications, risk-weighted exposure, potential future exposure, credit-loss allowances — name varies by pole). Remove → static register of ratings and balances.
4. **Ongoing portfolio monitoring and control against credit risk appetite** — the credit risk state is kept under continuous supervision (limits/thresholds/watch state at counterparty, sector and portfolio level; breach and exception handling; reporting to credit risk governance). Remove → a one-off calculation/modeling tool rather than an operating platform.

Jointly-held is load-bearing: (1) without (2)–(4) = a positions list; (2) without (1) = a rating tool; (3) without (1)–(2) = a modeling library; (4) without (1)–(3) = generic governance reporting.

### L1 — Common Mature Structure

- Scenario and stress machinery (adverse scenarios; impact across provisions/RWA/capital; reverse stress testing)
- Regulatory capital computation (Basel-family RWA; standardized and internal-model approaches; counterparty capital charges; regulatory content packs / jurisdiction taxonomies)
- Accounting-standard credit loss measures (IFRS 9 / CECL allowances, provisions)
- Model development, validation and governance environments (in-house model factories, champion/challenger, third-party model management, model inventory)
- Unified data foundation (centralized staged credit data, unified data models, shared reference data, reconciliation discipline)
- Analysis surfaces (slice-and-dice, drill-down from portfolio to loan/trade/calculation input, what-if, attribution)
- Early-warning machinery (deterioration signals, rating-transition alerts, watch lists)
- External data/ratings integration (bureau and rating-agency data, market data feeds, benchmark datasets)

### L2 — Variant / Optional Structure

- Book emphasis: banking-book analytics-led vs trading-book counterparty-led (PFE/CVA/collateral machinery) vs both on one platform
- Regulatory posture: regulatory-capital-led (Basel) vs accounting-led (ECL/IFRS 9/CECL) vs portfolio-economics-led (risk-adjusted return, economic capital)
- Segment emphasis: retail vs wholesale/structured vs mixed
- Freshness: batch end-of-day vs intraday/near-real-time exposure
- Packaging: standalone pure-play vs suite module vs platform module vs data/vendor-service layer
- Audience extension: corporate counterparty monitoring (non-bank)
- External credit-quality sourcing: internal models only vs external ratings/implied ratings vs hybrid

### L3 — Vendor-specific (Research Notes only)

- SAS: Risk Engine in-memory grid, open pricing framework (QuantLib/FINCAD), champion/challenger, Event Stream Processing integration; solution-family naming (Credit Origination, Credit Customer Management); Kamakura/KRIS distribution.
- Oracle: unified financial services data model; Climate Change Analytics with PD/LGD scorecard extension; stress-metric list (provisions, NII, leverage, liquidity…).
- Murex: four-eyes validation workflows; surgical recomputation; ISDA unit-test licensing; XVA suite (CVA/DVA/FVA/MVA/KVA); XVAaaS; shared reference data repository; Banorte PFE/credit-limit case study.
- Moody's: Data Alliance datasets and coverage figures; 580M+ pre-scored companies; Research Assistant (GenAI); CreditForecast with Equifax; entity-coverage counts (460M entities, 12,000 unrated entities in CreditView) — vendor-claimed figures, not asserted anywhere.

## Vendor-specific Findings

- Limit-change governance with four-eyes principle and full access-rights/audit is directly observed only at Murex → product-specific, do not generalize as the norm's exact form.
- "Real-time decisioning" as a credit risk solution capability is a SAS positioning claim; in the wider market real-time decisioning belongs to the Credit Decisioning type → treated as positioning, not structural.
- Moody's pre-scored entity universe and Data Alliance are a data-vendor pole; institutions with internal-only rating infrastructures do not require them → variant (external sourcing), not core.
- Oracle climate analytics extends credit risk with climate-adjusted PD/LGD — current-market extension, optional.

## Boundary Findings

- **vs Financial Risk Management Platform (processed; joint-review flag)** — RESOLVED from this side: **keep both (hub + slice), ratified**. Evidence: all three suite vendors sell credit risk as a distinct, separately-packaged solution within their multi-risk families (SAS "Credit Risk Management" solution; Oracle "Credit Risk Analytics" product; Murex "MX.3 for Credit Risk" brochure) — confirming the market realizes both the hub and the slice. The hub's center of gravity is cross-risk-type: shared data foundation, cross-risk aggregation, consolidated limits, enterprise reporting. The credit slice's center of gravity is credit-type depth: credit-quality measures per obligor, default-loss machinery, credit-specific capital/ECL, credit exposure semantics. Neither reduces to the other: remove cross-risk aggregation from the hub and it becomes one of the slices; remove credit-quality/default-loss semantics from this type and it becomes the generic hub. Each form also exists standalone (SAS markets credit risk to specialized lenders; Moody's credit-risk solutions serve corporates that buy no hub).
- **vs Market Risk Platform / Liquidity Risk Platform (siblings, unprocessed)** — same hub, different loss driver: default of an obligor vs adverse market-price movement vs inability to fund. Consistent with hub leaf's recommendation to keep all siblings.
- **vs Credit Management Platform (trade credit, processed)** — different counterparty side and machinery. Trade credit: seller extends credit to customers; system of record = per-customer credit account + governed credit limit + AR/open-order exposure + order block/release actions. This type: lender/investor side; exposures from lending/trading positions; measures are default-probability/loss-based; control is risk-appetite monitoring rather than order release. Overlap zone: corporates use counterparty credit data (Moody's corporate use case) to inform trade-credit terms — data feed, not the same system of record.
- **vs Credit Decisioning Platform (processed)** — seam confirmed by SAS's own product split (Credit Origination vs Credit Risk Management): decisioning's unit of work is the credit application (origination-time decision record); this type's unit is the portfolio position (exposure × quality over time). Decisioning consumes scores; the platform measures/monitors positions.
- **vs Credit Scoring Application** — score/scorecard production is one component of the credit-quality leg; the platform consumes scores into portfolio measurement/monitoring. Scoring alone is not portfolio risk management.
- **vs Loan Origination System / Loan Management System** — origination = booking workflow for new loans; servicing = repayment administration; this type = risk view over booked positions. Exposure data flows from these systems into the platform.
- **vs Regulatory Reporting Platform** — this type computes credit risk figures (RWA, EAD, large exposures) as part of risk management; reg-reporting produces/submitsthe reports. Consistent with the hub leaf's finding.
- **vs Debt Collection / Collections platforms** — post-default recovery work; this type manages pre-default risk. Defaulted exposure may transfer out to collections processes.
- **vs Underwriting Workbench (insurance)** — different risk object (insurance policies vs credit obligations); insurance credit-risk teams consume rating/transition data (Moody's insurance audience) but that is data consumption, not this type.

## Uncertainties

- No Tier-1 operational documentation was reachable (help centers gated; Oracle datasheet PDF binary). All observations are product-page level. Screen-level workflow details (exact drill-down paths, exact limit-state names, exact approval chains) are not asserted anywhere.
- Whether formal credit **limit enforcement** (as opposed to monitoring/reporting) is definitional: directly evidenced at Murex (credit limit management metrics, breach investigation/resolution); positioned as monitoring/dashboards at the others. The L0 therefore uses the broader "monitoring and control against credit risk appetite", with limit enforcement as the strongly-evidenced common implementation — precise limit-state lifecycles not asserted.
- Murex page does not explicitly name rating/PD machinery; counterparty exposure measurement (PFE/EAD) necessarily depends on default parameters, but this pass does not document Murex rating internals. Credit-quality leg is evidenced strongly at SAS/Oracle/Moody's (Layer B across three products).
- Retail-side consumer-credit risk machinery evidenced via Moody's CreditForecast and SAS scoring/origination components; depth of retail-specific structures (behavioral scoring, vintage analysis) not researched in detail.
- Regional practices (e.g., EU IFRS 9-heavy vs US CECL-heavy packaging) inferred from product mentions (EBA taxonomies, CECL/IFRS 9 solutions) but not sampled regionally.

## Historical / Market-Sample Check (§24 reasoning)

Would older, regional, platform-native products still fit? Yes under the four-structure core: a pre-Basel (1980s–90s) bank credit-risk department maintained obligor rating scales (structure 2), an exposure register per counterparty aggregated across facilities and books (structure 1), computed provisioning/loss estimates and concentration views (structure 3), and ran watch lists, per-obligor limits and credit-committee reporting (structure 4) — without Monte Carlo PFE, Basel RWA formulas, IFRS 9 ECL, in-memory grids or AI. Conversely, a modern automated decisioning engine without portfolio exposure records does not fit (it is Credit Decisioning); a rating-model repository without exposure and monitoring does not fit (it is a modeling tool). The definition therefore does not overfit the current regulatory-heavy implementation: Basel capital, ECL, PFE/CVA and stress-testing stay in the common/variant layers.

## Final Synthesis

A Credit Risk Platform is the credit-risk slice of financial risk management: the institution's system of record for its credit risk position — who owes it what, how likely each obligor is to default, how much could be lost — and the operating platform that keeps that position measured and controlled over time. Its defining core is four jointly-held structures: the credit exposure position (obligors carrying exposures aggregated across lending, trading and investment positions), the credit-quality assessment attached to each obligor (ratings/scores/PD machinery, internal or external), the computed credit risk measures (exposure × quality translated into expected-loss, risk-weighted, potential-future-exposure or allowance quantities under current and adverse views), and the ongoing monitoring-and-control loop against credit risk appetite (limits/thresholds/watch state, breach handling, credit risk governance reporting). Around this core, mature products add scenario/stress machinery, regulatory capital computation, accounting-standard credit-loss measures, model factories with governance, unified credit data foundations, drill-down analysis, early-warning signals, and external data/ratings integration. The market realizes the type along several poles: banking-book analytics/modeling-led suites, enterprise platform modules on a unified data model, capital-markets counterparty-exposure platforms (PFE/CVA/capital/limits), and data/ratings-led measurement services; with variants by book, regulatory posture, segment, freshness and packaging. Boundaries: the multi-risk hub above it (ratified hub+slice), market/liquidity siblings (loss driver), trade-credit credit management (counterparty side), credit decisioning (application-time vs portfolio-time; vendor-internal split evidence), credit scoring (component vs whole), loan origination/servicing (workflow vs risk view), regulatory reporting (figures vs reports), collections (post-default).
