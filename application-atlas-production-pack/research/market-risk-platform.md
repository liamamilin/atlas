# Research Notes — Market Risk Platform

Leaf: Market Risk Platform (DIRECTORY.md §08 Finance, Banking, Insurance & Investment)
Slug: `market-risk-platform`
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Determine what a "Market Risk Platform" actually is as an Application Type: its defining core, its users, its world model (objects and relations), its canonical workflows, its interfaces, its rules, and its boundaries. Four boundary questions dominate this pass:

1. **Umbrella-vs-slice joint review** vs Financial Risk Management Platform (processed) — the hub pass flagged market-risk/credit-risk/liquidity-risk as sibling slices; credit-risk-platform and liquidity-risk-platform (both processed 2026-09-08) each RATIFIED keep-both from their sides. This pass resolves from the market side, treating research/credit-risk-platform.md and research/liquidity-risk-platform.md §Boundary Findings as counterparties.
2. **Sibling seam vs Credit Risk Platform / Liquidity Risk Platform** — same hub family, different loss driver; both siblings recorded this pass as their remaining counterparty.
3. **Actuarial Modeling Platform joint-review flag** — the actuarial pass flagged actuarial-vs-market-risk as an open adjacency ("market-risk-platform side remains open until those siblings are processed"). This pass must discharge it from the market side.
4. **Seat boundaries** vs trading platforms (retail/professional/algorithmic), Portfolio Management System, Financial Market Data Terminal, Treasury Management System, Regulatory Reporting Platform, Energy Trading Platform (which recorded "market-risk apparatus" as a non-definitional standard capability).

## Initial Boundary (working hypothesis before research)

- Hypothesis: financial-institution-side (and investment-management-side) software that measures, monitors and controls the risk of losses from adverse movements in market prices — interest rates, foreign exchange, equity prices, credit spreads, commodity prices, volatility — across the institution's trading and/or investment portfolios. Center of gravity: positions mapped to risk factors, risk measures (sensitivities, distribution measures such as VaR, scenario/stress results) under current and stressed views, and limit/monitoring control against risk appetite.
- Nearest confusions:
  - **Financial Risk Management Platform** (processed) — institution-wide cross-risk hub; this leaf is expected to be the market-risk slice.
  - **Credit Risk Platform / Liquidity Risk Platform** (both processed) — sibling slices (default risk / funding risk vs price risk).
  - **Retail/Professional/Algorithmic Trading Platform** — execution and position keeping for traders; market risk is the measurement/control layer over positions.
  - **Portfolio Management System** — investment decisions; buy-side market risk sits beside it.
  - **Financial Market Data Terminal** — market data is an input to the risk computation, not the record.
  - **Treasury Management System** — deal layer vs risk layer.
  - **Regulatory Reporting Platform** — figures vs report production (same seam as both siblings found).
  - **Actuarial Modeling Platform** — liability/product projection vs risk-position measurement.
- Unknowns: whether VaR specifically is definitional or an era-specific common implementation (pre-VaR sensitivity/scenario practice must still fit — §24 check); whether stress machinery is definitional (it felt more central here than in credit risk); whether the buy-side (asset manager) realization fits the same core as the sell-side (bank trading book) realization; whether regulatory capital machinery (FRTB) is definitional; whether P&L attribution is definitional or common.

## Research Questions

1. What does the system hold as its record? (positions? sensitivities? risk factors? scenarios? valuation results?)
2. What measure families exist (sensitivities/deltas/durations, VaR-family, expected shortfall, scenario/stress results) and which are definitional?
3. How do risk-factor mapping and valuation machinery work (curves, vol surfaces, full revaluation vs approximation)? Core or common?
4. What does the what-if / scenario / stress loop look like (hypothetical scenarios, historical scenarios, regulatory exercises, reverse stress)?
5. How does monitoring/control work (limits on what quantities, at what granularity, intraday vs EOD, breach handling, backtesting)?
6. Is P&L attribution/explanation definitional or common?
7. Is regulatory capital machinery (FRTB-family) definitional or common?
8. Does the buy-side realization (asset-manager portfolios, factor models) share the same core as the sell-side (bank trading book) realization?
9. Who are the users and roles (market risk officers, risk quants, risk controllers, desk heads, CRO, investment teams)?
10. Where are the boundaries (hub, siblings, trading platforms, PMS, data terminals, TMS, reg reporting, actuarial)?
11. Historical check: would pre-VaR market risk practice (notional/duration/delta limits, gap reports, scenario analysis, stop-loss) still fit the definition?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer levels:

| Product | Pole | Customer level | Evidence |
|---|---|---|---|
| Murex — MX.3 for Enterprise Market Risk (within MX.3 ERM) | capital-markets platform module; sell-side trading + banking books | large global banks, all tiers ("more than 150 customers") | A (official ERM page with dedicated market-risk section) |
| Oracle Financial Services — Market Risk Measurement and Management (within FS Risk Management family) | enterprise analytics suite module; valuation-model-led | global banks and diversified institutions | A (official family page naming the product) |
| BlackRock Aladdin Risk | buy-side integrated platform component; factor-model-led; risk beside portfolio management | asset managers, pension funds, insurers, banks & brokers, wealth managers | A (official product page) |
| QRM — Quantitative Risk Management | balance-sheet analytics/consultancy-led; trading book + structural banking-book market risk | banks, thrifts, credit unions, building societies, mortgage lenders, insurers | A (official homepage, segment capability maps) |

Rejected/abandoned samples (network-limitation rule):
- **MSCI (RiskMetrics family)** — `msci.com` returned 404 on the solutions URL, then a bot "Challenge Validation" page. Abandoned after two attempts. This removes the classic vendor-measures pure-play pole from the sample — noted as a sourcing limitation.
- **Bloomberg MARS** — `bloomberg.com/professional` timed out twice. Abandoned.
- **SS&C Algorithmics** — `sscinc.com` returned 403. Abandoned (insurer/enterprise simulation pole lost from direct evidence).

Sample covers: sell-side capital-markets platform module, enterprise analytics suite module, buy-side integrated platform, balance-sheet analytics-led platform; global banks through mid-tier institutions and asset managers/pension funds/insurers; trading-book and banking-book and investment-portfolio scopes.

## Sources

All fetched 2026-09-08, Layer A (official vendor pages):

- Murex — Enterprise Risk Management page (incl. "Enterprise market risk and internal models", FRTB, Smart analysis and correction, Centralized risk control, Risk control operations sections): https://www.murex.com/en/solutions/business-solutions/enterprise-risk-management
- Oracle — Financial Services Risk Management family page (incl. "Market Risk Measurement and Management" named product, Stress Testing and Scenario Analysis, unified data model sections): https://www.oracle.com/financial-services/analytics/financial-services-risk-management/
- BlackRock — Aladdin Risk product page ("Risk Management Services | Aladdin"): https://www.blackrock.com/aladdin/products/aladdin-risk
- QRM — Quantitative Risk Management homepage (Depository Institution / Mortgage Lender / Insurance Company capability maps, seminar program): https://www.qrm.com/
- Local (prior passes, counterparties): research/credit-risk-platform.md, research/liquidity-risk-platform.md, research/financial-risk-management-platform.md §Boundary Findings; research/actuarial-modeling-platform.md flag (via STATUS.md Boundary Issues); research/energy-trading-platform.md (market-risk-apparatus note via STATUS.md).

**Source-access limitation:** no authenticated help-center / operational documentation was reachable for any sampled product (MSCI challenge-walled, Bloomberg timeouts, SS&C 403; Oracle datasheet PDFs not fetched — binary per prior passes). All evidence is official product/solution-page level (Layer A) plus cross-product commonality (Layer B). Precise numeric claims (calculation windows, limit values, confidence levels, holding periods, scenario parameters) are deliberately not asserted anywhere.

---

## Product Observations

### Murex — MX.3 for Enterprise Market Risk (Evidence Layer A, richest market-risk detail of the sample)

- Page title literally reads "Market Risk Management Platform | Murex" (naming evidence).
- Suite context: "MX.3 provides enterprise solutions that allow banks to control market, credit, and liquidity risk for internal and regulatory compliance. This is complemented by a real-time limit and exposure monitoring solution. The risk management platform covers internal market risk; fundamental review of the trading book (FRTB); X-valuation adjustment (XVA); standardized approach for measuring counterparty credit risk (SA-CCR); credit risk and initial margin (IM)."
- Market-risk product section (full quote): "MX.3 offers an end-to-end enterprise-wide solution used by more than 150 customers across all tiers to meet regulatory requirements. The solution provides a complete view of the risks taken by the organization. It supports historical value at risk (VAR), expected shortfall, stress testing and profit and loss explanations, all of which can be computed both with full revaluation as well as Taylor-based calculations. Stress-testing supports historical scenarios as well as the design of hypothetical adverse scenarios, leveraging criteria-based shifts and proxies, addressing risk management and regulatory purposes such as stressed risk measures."
  - → measure families named: historical VaR, expected shortfall, stress testing, P&L explanations
  - → computation machinery named: full revaluation vs Taylor-based calculations
  - → scenario machinery named: historical scenarios + hypothetical adverse scenario design (criteria-based shifts, proxies); purposes: risk management + regulatory ("stressed risk measures")
- FRTB: "end-to-end enterprise-wide solution for both the standardized approach, FRTB-SA, and the internal model approach, FRTB-IMA. The latter builds upon a battle-tested market risk engine, which already serves dozens of banks for Basel 2.5 approved internal VAR and stressed VAR models. FRTB-SA leverages over two decades of experience in sensitivity analytics."
  - → sensitivity analytics as a long-standing machinery line ("two decades of experience") — direct evidence that sensitivities predate the current regulatory layer as a core machinery.
- Risk-officer analysis loop ("Smart analysis and correction", full quote): "Risk officers enjoy strong analysis capabilities and have full autonomy in calculation process correction. From their day-to-day screen, they can slice and dice and drill down to the finest calculation inputs, such as trades, sensitivities, reference data and scenarios. Corrections trigger smart recomputation based only on what is impacted by the change. This enables risk officers to get corrected figures efficiently and meet the deadline for official results."
  - → the day-to-day workflow: drill-down to trades/sensitivities/reference data/scenarios; correction; selective recomputation; deadline-driven official results.
- Centralized risk control: "a leading limits and exposure monitoring solution across multiple source systems in real-time. It interacts with third-party deal capture systems. The solution covers the range of exposures for market, credit, liquidity and operational risks across trading, banking and investment books. The risk controller benefits from real-time position insights with the ability to take effective actions immediately. These include limit suspension, trade hedging or blocking contracts breaching limits. Central management enables consistent and efficient monitoring of intraday limit usage. Limits can be temporarily increased, or the limit line can be reallocated across business units and desks. Business dashboards summarize excess causes and resolution time and keep senior management informed."
  - → limits operate across source systems (including third-party deal-capture systems) — the risk layer sits over position-keeping systems; limit actions: suspension, hedging, blocking; intraday usage monitoring; limit reallocation across business units/desks; excess dashboards to senior management.
- Risk control operations: "full management of limit excesses, whether caused by intraday activity or end-of-day batch. Breaches are routed to a proper investigation and resolution of causes … Validation workflows that include the four-eyes principle can be applied to all changes made on reference data and limits. The solution includes full access rights management and audit procedures."
- Regulatory machinery: prepackaged regulatory content, local regulatory watch, Basel-standards-exception support; ISDA unit-test validation for FRTB-SA/SA-CCR/SIMM/SA-CVA.
- Roles named: CRO, CTO, Head of market risk, Head of credit risk, Head of finance, XVA trader, Risk controller.
- Technology: cloud (AWS/Azure), on-prem, SaaS/managed services; proprietary grid or IBM Symphony; CPU+GPU; "surgical recomputation" of impacted figures; XVA as a Service.

### Oracle Financial Services — Market Risk Measurement and Management (Evidence Layer A, positioning level)

- Named distinct product in the family: "Advance valuation methods for market risk — Oracle Financial Services Market Risk Measurement and Management enables institutions to establish reliable valuations of a wide array of simple and complex instrument types using sophisticated, prebuilt models." Direct evidence of the hub-sells-slices pattern; valuation-model-led positioning.
- Family framing: "spans credit, market, liquidity, interest rate, and business risk to provide you with a single, consistent view of risk and performance."
- Family stress product covers market-side scenarios: "Assess the impact of a single set of scenarios across a diverse set of metrics, including provisions, interest income, net interest income, profitability, risk-weighted assets, capital, leverage, and liquidity … what-if analysis, scenario analysis, stress tests, ad hoc impact assessments, attribution analysis, and reverse stress testing."
- Data foundation: "single source of truth for risk assessment … centralized, aggregated risk data through a unified financial services data model and common analytical infrastructure."
- Model governance: "robust model management and governance to create, inherit, and manage in-house, Oracle, and third-party models" (stress product; model management as first-class machinery).

### BlackRock — Aladdin Risk (Evidence Layer A, buy-side pole)

- Positioning: "Aladdin Risk is BlackRock's analytics engine—designed to deliver a consistent, integrated view of risk and return across asset classes … it enables teams to analyze portfolios with greater clarity and confidence." Audience: asset managers, asset servicers, banks & brokers, corporates, insurers, pension funds, private markets, wealth managers.
- Key capabilities (named on page):
  - Whole-portfolio view: "a comprehensive, connected view of risk and performance across public and private markets … consistent analytics across asset classes"
  - Driver analysis: "Analyze exposures at a granular level—by factor, sector, or security—to uncover the underlying drivers of portfolio behavior. Combined with scenario analysis and stress testing"
  - What-if: "Evaluate portfolio changes dynamically using forward-looking analytics and 'what-if' scenarios"
  - Unified data and analytics framework: "Integrate positions, data, and analytics into a single framework for a consistent view of the portfolio"
  - Multi-asset risk models: "Apply advanced risk models across equities, fixed income, derivatives, and alternatives … BlackRock's proprietary models and thousands of risk factors to measure risk consistently across public and private markets"
  - Scenario analysis and portfolio modeling: "stress testing, scenario analysis, performance attribution, and what-if modeling. Aladdin Risk combines historical market events with forward-looking, market-driven scenarios"
  - Governance and "Risk Radar": "integrated governance, compliance, and exception monitoring workflows … detect, analyze, and resolve risk issues through a transparent and auditable framework, supporting risk threshold monitoring, mandate compliance, and automated escalation workflows"
  - Extensibility: APIs/tooling (Aladdin Studio) to "embed Aladdin capabilities", run "what-if analysis, producing repeatable executive reporting, monitoring portfolio activity"
- Scale figures (marketing, not operational): 5,000 multi-asset risk factors; 300 risk & exposure metrics reviewed daily.
- FAQ definitions: risk management as "identifying, assessing, monitoring, and mitigating risks that may affect investment objectives" — the buy-side articulation of the same loop.
- Boundary-relevant: Aladdin is an integrated investment platform (portfolio management + risk + operations); Aladdin Risk is its risk-analytics component sold as "Risk Management Services". Buy-side market risk lives beside portfolio management, not inside a trading platform.

### QRM — Quantitative Risk Management (Evidence Layer A, banking-book analytics pole)

- Model: consultancy + research/data provider + applications developer; "high-precision cloud technology … a single foundation for measuring risk and calculating the best allocation of capital"; audiences: "commercial banks and thrifts, credit unions, building societies, mortgage lenders, REITs, asset management companies, and insurance companies."
- Depository-institution capability map — market risk appears as a **named distinct monitored risk line** inside "Evaluate the Present → Risk Profile and Limit Monitoring": "Credit Risk; Short-Term (LCR) and Structural (NSFR) Liquidity Risk; **Trading (FRTB) and Structural (IRRBB) Market Risk**."
  - → direct vendor evidence that market risk spans the trading book (FRTB) and the structural banking book (IRRBB) as one monitored risk line, alongside credit and liquidity.
- "Risk Factor Sensitivity Analysis — Margin; Economic Value of Equity (EVE)" — sensitivity analysis as a named capability.
- "Risk and Return Attribution — Risk and Profitability Metrics Calculated and Reported at Management-Driven Levels of Detail: Legal Entity / Business Line / Product / Desk / Officer" — attribution down to desk/officer granularity.
- Outcomes analysis: "Forecast-to-Actuals Comparison; Model Back Testing; Hedge Effectiveness Testing."
- Stress testing: "Stress Testing Design and Execution — Scenario Design and Identification; Traditional Silo-Based Capital Stress Testing and Liquidity Stress Testing; Comprehensive Enterprise Impact Analyses"; seminar "Generating Scenarios for CCAR, DFAST, BoE and Other Stress Testing Exercises"; "Risk Appetite Reassessment — Risk Exploration and Inter-connectivity; Limit Identification and Setting."
- Insurance segment: "ALM/ Interest Rate Risk; Credit Risk; Insurance Risk; Lapse Risk; Liquidity Risk; Longevity Risk and Pension Modeling; **Market Risk**" listed among exposure calculations — audience variant.
- Mortgage-lender segment: "Measuring the Pipeline and MSR Portfolio — Risk Profile and Value at Risk" — VaR applied beyond securities books (mortgage pipelines/servicing rights); "Funding — Liquidity Risk"; forecasting "Market Risk, Liquidity, and Capital Management."
- Data/market machinery: "QRM provides intraday market data snapshots to ensure that these processes are accurate and can be automated"; "Our researchers also design, develop, apply, and defend customer behavior models."

---

## Cross-product Comparison

| Finding | Murex | Oracle | Aladdin | QRM | Evidence | Layer |
|---|---|---|---|---|---|---|
| Consolidated position/holding view as the record | A (complete view of risks taken; interacts with deal-capture systems; trading/banking/investment books) | A (unified data model; valuations of instrument array) | A (positions + data + analytics in one framework; public+private) | A (balance-sheet measurement; pipeline/MSR portfolios) | B (4/4) | L0 |
| Positions mapped to risk factors / sensitivities | A ("two decades of experience in sensitivity analytics"; drill-down to trades, sensitivities) | A (prebuilt valuation models over instrument types) | A (exposures by factor/sector/security; thousands of risk factors) | A (Risk Factor Sensitivity Analysis; FRTB + IRRBB lines) | B (4/4) | L0 |
| Distribution/loss-distribution measures (VaR-family, ES) | A (historical VaR, expected shortfall named) | implied (market risk via valuation models; not named on page) | not named as VaR (factor/scenario-led framing) | A ("Risk Profile and Value at Risk"; FRTB line) | B (2–3/4 named) | L1 (named implementation) |
| Scenario / stress machinery (historical + hypothetical) | A (historical scenarios + hypothetical design, criteria-based shifts, proxies) | A (scenario analysis, stress tests, reverse stress, attribution analysis) | A (stress testing; historical market events + forward-looking market-driven scenarios) | A (scenario design/identification; CCAR/DFAST/BoE exercise scenarios) | B (4/4) | L0 (stressed view) / L1 (machinery) |
| Ongoing monitoring & control vs appetite (limits, thresholds) | A (real-time limits across source systems; intraday usage; limit reallocation) | implied (family framing; stress product dashboards) | A (Risk Radar: risk threshold monitoring, mandate compliance, automated escalation) | A (Risk Profile and Limit Monitoring; Limit Identification and Setting) | B (4/4) | L0 |
| Breach/exception handling as workflow | A (excess investigation & resolution; limit suspension/blocking; four-eyes on limit changes) | — (not observed) | A (Risk Radar: detect, analyze, resolve; auditable framework) | — (not observed) | B (2/4) | L1 |
| P&L attribution / explanation | A (profit and loss explanations) | A (attribution analysis in stress product) | A (performance attribution) | A (Risk and Return Attribution at desk/officer detail) | B (4/4) | L1 (strong; held out of core) |
| Backtesting / model validation | A (ISDA unit tests; Basel 2.5 approved models context) | A (model management and governance; in-house/Oracle/third-party models) | A (model oversight; quality-controlled data) | A (Model Back Testing; model validation seminars) | B (4/4) | L1 |
| What-if / pre-deal analysis | A (drill-down + correction loop; XVA what-if at suite level) | A (what-if analysis named) | A (what-if modeling; evaluate portfolio changes dynamically) | partial (scenario design; risk exploration) | B (3–4/4) | L1 |
| Regulatory capital machinery (FRTB-family) | A (FRTB-SA and FRTB-IMA named) | — (not named on page) | — (not named) | A (Trading (FRTB) line named) | B (2/4 named) | L1 |
| Sensitivities named as machinery ("Taylor", factor sensitivities) | A | implied (valuation models) | A (factor/sector/security) | A (Risk Factor Sensitivity; EVE/Margin) | B (3/4) | L0–L1 |
| Unified risk data foundation | A (common data model; shared reference data repository) | A (unified financial services data model) | A (single framework; common data language) | A (single foundation) | B (4/4) | L1 |
| Governance/senior-management reporting | A (business dashboards; senior management) | A (dynamic dashboards) | A (repeatable executive reporting; governance workflows) | A (management-driven levels of detail) | B (4/4) | L1 |
| Risk attribution granularity (desk/officer) | A (limits across business units and desks; drill to trades) | — (not stated) | A (by factor/sector/security; teams/strategies) | A (Legal Entity/Business Line/Product/Desk/Officer) | B (3/4) | L1 |
| Market data as input machinery | — (not named on page) | — (not named) | implied (market-driven scenarios) | A (intraday market data snapshots) | B (1–2/4) | L1 |
| Buy-side factor-model vs sell-side distribution posture | distribution/revaluation-led | valuation-model-led | factor/scenario-led | mixed (VaR + sensitivity + scenarios) | B (philosophy split) | L2 |
| Trading book + banking book in one type | A (trading, banking and investment books) | — (not stated) | — (investment portfolios) | A ("Trading (FRTB) and Structural (IRRBB) Market Risk") | B (2/4 explicit) | L1–L2 |
| Real-time / intraday posture | A (real-time limit monitoring; intraday limit usage) | — (not stated) | — (not stated) | A (intraday market data snapshots) | B (2/4) | L1–L2 |
| Packaging: platform module / suite module / integrated buy-side platform / analytics-led | platform module | suite module | integrated platform component | analytics/consultancy-led | B (4/4 poles) | L2 |

### Modeling observations

- **The record is the institution's position, expressed on a risk view — not the market data, and not the trades themselves.** Every product's center is a consolidated, inspectable view of holdings (trading-book positions, banking-book balance sheet, investment portfolios, even mortgage pipelines) mapped to market risk factors through valuation/sensitivity machinery. Murex's limit monitor "interacts with third-party deal capture systems" — the risk layer sits over position-keeping systems; QRM provides "intraday market data snapshots" — market data is an input. This is categorically different from a trading platform (execution/position keeping) or a market-data terminal (data provision).
- **Measures are potential-loss quantities under defined market moves.** The measure families are factor exposures (sensitivities: delta/duration-class, factor/sector/security exposures), scenario results (historical scenarios, hypothetical adverse scenarios, regulatory exercises), and distribution measures (VaR-family, expected shortfall). Every one is a function of governed model machinery — valuation models, risk-factor mappings, scenario sets, model parameters. The distribution measures are *named implementations*; the *stressed view* itself (the same position measured under defined adverse market moves) is cross-product at the conceptual level.
- **The monitor-and-control leg is appetite-shaped and desk-granular.** Limits operate on the risk quantities (not raw notional alone — limit reallocation across business units and desks; risk threshold monitoring; limit identification and setting), with breach/exception workflows (investigation and resolution of causes; detect-analyze-resolve; automated escalation), and governance reporting to senior management.
- **P&L attribution is universal in the sample but sits below the defining line**: Murex "profit and loss explanations", Oracle "attribution analysis", Aladdin "performance attribution", QRM "Risk and Return Attribution". It explains *why* measures moved — an analysis capability over the measurement core, not the core itself. (Held at L1 with strong 4/4 evidence.)
- **Regulatory capital machinery (FRTB-family) is named at two of four** and is the dominant commercial driver in the sell-side pole — but the buy-side pole (Aladdin) carries no FRTB language and remains squarely in-type. Regulatory capital is therefore a common (in sell-side, near-universal) implementation, not the definition.
- **One type, two books, two seats.** The sell-side realization measures trading-book (and banking-book) positions for a bank's risk function; the buy-side realization measures investment portfolios for asset managers/pension funds/insurers. QRM names both books in one line ("Trading (FRTB) and Structural (IRRBB) Market Risk"); Murex covers "trading, banking and investment books"; Aladdin covers "public and private markets". The core (position → factor mapping → measures under current and stressed views → limit control) is identical; the measure vocabulary and the seat differ.
- **The daily cycle is deadline-driven.** Murex: risk officers correct calculation inputs "to meet the deadline for official results" — official risk figures are produced on a daily sign-off cycle; breaches can be intraday or end-of-day batch. This operational rhythm (batch EOD + optional intraday) recurs across the sample.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal, jointly-held)

Three jointly-held structures:

1. **The market-risk position of record** — the institution's (or portfolio manager's) holdings held as an inspectable whole on a risk view: instruments/positions across the relevant books or portfolios, organized for aggregation by desk/portfolio/entity/asset class, mapped to market risk factors (rates, FX, equity, credit spread, commodity, volatility) through valuation and sensitivity machinery, fed from position-keeping/trading/portfolio systems. *Remove → a market-data terminal or a deal-capture system with nothing to measure.*
2. **Market-risk measures under current and stressed views** — the position translated into governed quantities of potential loss from adverse market-price movements: factor exposures/sensitivities, scenario and stress results (historical and hypothetical adverse market moves), and, in most current implementations, distribution measures (VaR-family, expected shortfall) — computed under the current view and under stressed assumptions, anchored by governed model machinery. *Remove → position keeping or a valuation library; the "risk" half is gone.*
3. **Ongoing monitoring and control against market-risk appetite** — the risk state kept under continuous supervision: limits/thresholds on the risk measures at desk/portfolio/entity granularity, breach/excess handling routed to investigation and resolution (with escalation and, in some products, pre-emptive action), and governance reporting to senior management/risk committees — plus, where regulation requires it, the capital figures computed from the same machinery. *Remove → one-off analytics, not an operating platform.*

Jointly-held is load-bearing:
- 1+3 without 2 = a position/limit register with no measurement
- 2+3 without 1 = a calculator/model with no institutional position behind it
- 1+2 without 3 = risk analytics/reporting, not management

Not in L0 despite being near-universal or era-defining: VaR specifically (sensitivity/scenario-era practice satisfies the core — §24 check), expected shortfall, FRTB/regulatory capital computation, Monte Carlo simulation, factor models, full-revaluation engines, real-time/intraday limit engines, market-data feeds, AI.

### L1 — Common Mature Structure

- Sensitivity analytics across risk factors (delta/duration-class, factor/sector/security exposures; Taylor-based approximations beside full revaluation)
- Distribution measures — historical VaR, Monte Carlo VaR, expected shortfall — with the backtesting machinery their use requires
- Scenario and stress machinery — historical scenario replay, hypothetical adverse scenario design, regulatory exercise scenarios (CCAR/DFAST/BoE-class), reverse stress testing
- P&L attribution/explanation — why risk and profit moved (universal in sample, 4/4)
- Limits and exposure monitoring across source systems, books and desks — incl. intraday limit usage in the sell-side pole; limit reallocation; pre-emptive actions (suspend, hedge, block)
- Breach/exception workflows — investigation and resolution of causes, four-eyes validation on limit/reference-data changes, auditable exception frameworks, automated escalation
- Backtesting and model governance — model back testing, hedge-effectiveness testing, unit-test validation, model management for in-house/vendor/third-party models
- What-if / pre-deal analysis — dynamic evaluation of prospective portfolio changes
- Unified risk data foundation — shared reference data, common calculation framework, single data language across books and asset classes
- Governance reporting — dashboards and official figures for senior management/risk committees on a deadline-driven daily cycle
- Regulatory capital machinery — FRTB standardized and internal-model approaches (sell-side); prepackaged regulatory content and local regulatory watch
- Market-data input machinery — curves, snapshots, scenario-eligible market data

### L2 — Variant / Optional Structure

- Packaging: capital-markets platform module vs enterprise analytics suite module vs buy-side integrated platform component vs balance-sheet analytics/consultancy-led platform
- Seat/book scope: bank trading book (+ banking book IRRBB) vs investment portfolios (asset managers, pension funds, insurers); mortgage pipelines/servicing rights as an extended application
- Measure philosophy: distribution-led (VaR/ES) vs factor/scenario-led vs valuation-model-led — a genuine philosophy split, not maturity ordering
- Real-time/intraday vs end-of-day batch; cloud vs on-prem; SaaS/managed services
- Regulatory regime emphasis (Basel/FRTB vs CCAR/DFAST/BoE exercises vs internal-only)
- Asset-class breadth (from thousands of products in capital-markets platforms to multi-asset incl. private markets on the buy side)
- Audience extensions: insurers (market risk among actuarial exposure lines), mortgage lenders (pipeline VaR)

### L3 — Vendor-specific (Research Notes only)

- Murex: page title "Market Risk Management Platform"; historical VaR + ES + stress + P&L explanations computed "with full revaluation as well as Taylor-based calculations"; criteria-based shifts and proxies in hypothetical scenario design; ">150 customers across all tiers"; Basel 2.5 approved internal VAR/stressed VAR models heritage; "two decades of experience in sensitivity analytics" (FRTB-SA); smart/surgical recomputation of impacted figures; ISDA unit-test validation (FRTB-SA/SA-CCR/SIMM/SA-CVA); four-eyes limit governance; limit suspension/hedging/blocking; intraday limit usage monitoring; 2,400+ products coverage; local regulatory watch; prepackaged regulatory content; AWS/Azure/on-prem/SaaS; proprietary grid or IBM Symphony; CPU+GPU; XVAaaS; sibling solutions (XVA, SA-CCR, IM, credit, liquidity) in one ERM suite.
- Oracle: product named "Market Risk Measurement and Management"; "reliable valuations … sophisticated, prebuilt models" positioning; family stress product with what-if/scenario/stress/attribution/reverse-stress; IFRS 9/ICAAP/ILAAP stress framing; model management across in-house/Oracle/third-party models; unified financial services data model; datasheet PDFs not fetched (binary).
- Aladdin: "analytics engine" positioning; 5,000 multi-asset risk factors; 300 risk & exposure metrics reviewed daily (marketing figures); Risk Radar governance/exception framework; factor/sector/security exposure granularity; public+private markets with look-through into fund holdings; whole-portfolio/Total Fund/Total Portfolio Approach framing; proprietary BlackRock models; Aladdin Studio API extensibility; institutional-investor-only distribution posture.
- QRM: consultancy+research+applications model; "Trading (FRTB) and Structural (IRRBB) Market Risk" as one monitored line beside credit and liquidity; Risk Factor Sensitivity Analysis (Margin, EVE); attribution at Legal Entity/Business Line/Product/Desk/Officer; Model Back Testing and Hedge Effectiveness Testing; CCAR/DFAST/BoE scenario seminars; mortgage pipeline/MSR "Risk Profile and Value at Risk"; intraday market data snapshots; customer behavior models; quarterly cloud evolution; seminar curriculum as the working practice of the type.

## Vendor-specific Findings

- **Distribution-measure naming is not uniform**: VaR/ES named directly at Murex and QRM; Aladdin frames risk in factor/scenario terms without naming VaR on the fetched page; Oracle's fetched page names valuation models, not VaR. The measure-family *concept* is universal; named implementations vary → VaR/ES held at L1.
- **FRTB as commercial driver** is sell-side-pole-specific in the sample (2/4) → L1, not core.
- **P&L attribution** is 4/4 but articulated differently per vendor (explanations/attribution/performance attribution/return attribution) → L1 with strong evidence.
- **Real-time limit monitoring and intraday usage** is deep at Murex (sell-side trading floor rhythm); the buy-side pages do not evidence an intraday posture → L1–L2, posture-dependent.
- **Pre-emptive limit actions (suspend/hedge/block)** are evidenced only at Murex → product-specific implementation of the control leg; do not generalize.
- **"Risk Radar"-style branded exception frameworks** (Aladdin) and **four-eyes limit governance** (Murex) are product-specific realizations of the same breach-workflow concept.
- **Mortgage pipeline/MSR VaR** (QRM) is an extended application of the machinery to non-securities books → variant.

## Boundary Findings

- **vs Financial Risk Management Platform (processed; joint-review flag) — RESOLVED from this side: keep both (hub + slice), RATIFIED**, completing the sibling set (credit and liquidity both ratified earlier). Evidence: Oracle sells "Market Risk Measurement and Management" as a named distinct product within its FS Risk Management family; Murex sells "MX.3 for Enterprise Market Risk" as a distinct solution/brochure within its ERM suite; QRM monitors market risk as a distinct named risk line within balance-sheet measurement; Aladdin sells Risk as a distinct "Risk Management Services" component. The hub's center of gravity is cross-risk-type (shared data foundation, cross-risk aggregation, consolidated limits, enterprise reporting); the market slice's center of gravity is market-risk-type depth (risk-factor mapping, sensitivities, distribution measures, scenario/stress machinery, trading-book limit control). Neither reduces to the other; each form also exists standalone (Aladdin Risk as a distinct service; QRM market-risk line; mid-tier institutions buy market-risk measurement without an enterprise hub).
- **vs Credit Risk Platform / Liquidity Risk Platform (siblings, processed) — seam held from this side**, discharging their carried counterparty flags: the discriminator is the **loss driver and the measured object**. Market risk measures losses from adverse market-price movements (rates, FX, equity, spread, commodity, volatility) on positions; credit risk measures obligor default on exposures; liquidity risk measures funding shortfalls on cash flows. The machinery families differ accordingly: factor mapping/sensitivities/distribution measures/stress on market moves vs rating/EL/RWA machinery vs ladder/coverage/buffer machinery — all three over the same "position of record + measures under current and stressed views + monitoring & control" skeleton, which is exactly why the hub exists. Interactions are real (market moves trigger collateral calls and rating downgrades; spread risk in the trading book is market risk while default risk is credit risk), but the measured objects do not merge.
- **vs Actuarial Modeling Platform (joint-review flag DISCHARGED from this side)** — the actuarial pass centers on liability/product models (reserving, cash-flow projection of insurance products, capital modeling for insurers) feeding capital, risk and reporting processes. A market-risk platform measures the institution's existing risk positions against market moves; it does not model insurance liabilities. QRM's insurance segment lists "Market Risk" as one exposure line beside lapse/longevity/insurance risk — the same institution runs both platforms on different objects. Adjacency confirmed, not duplicates.
- **vs Retail / Professional / Algorithmic Trading Platform** — trading platforms execute and keep positions for traders (front office); the market-risk platform measures and controls the risk of the aggregated positions (middle/back office risk function). Murex's own evidence states the limit monitor "interacts with third-party deal capture systems" — capture is elsewhere. A trading platform's on-screen risk (per-desk sensitivities) is an operational convenience; the platform type here is the system of record for institutional risk measurement and appetite control. Algorithmic trading adds strategy execution automation — different user, different loop.
- **vs Portfolio Management System** — portfolio management optimizes and implements investment decisions (construction, rebalancing, trade ideas); market risk measures and monitors the resulting risk. On the buy side they cohabit one platform (Aladdin: portfolio construction workflows beside Aladdin Risk), which is why the seam is easy to blur; the risk component's objects (risk factors, scenarios, thresholds, exceptions) and users (central risk teams, not portfolio managers alone) are distinct.
- **vs Financial Market Data Terminal** — market data (prices, curves, vols) is an *input* to the risk computation (QRM's "intraday market data snapshots"); the terminal's record is data and analytics over the market, not the institution's position or its risk appetite. Data terminals may embed portfolio analytics, but they do not hold the institution's limit state.
- **vs Treasury Management System / bank deal-capture** — deal layer (capture, processing, settlement) vs risk measurement layer over the captured positions; consistent with both siblings' finding. MORS selling ALM and TMS as separate modules is vendor-internal separability evidence (recorded there).
- **vs Regulatory Reporting Platform** — this type computes risk figures (VaR, FRTB capital inputs, stress results); reg-reporting produces/submits the reports. Same figures-vs-reports seam as credit and liquidity found. Murex's prepackaged regulatory content supports reporting *on* the risk figures without the platform becoming a reporting system.
- **vs Energy Trading Platform (processed)** — that pass recorded "market-risk apparatus (portfolio measures/what-if/stress)" as a standard capability *not definitional* for energy trading; consistent from this side: the energy type's defining core is the energy deal/position/value record, and generic market-risk machinery is the cross-asset layer this leaf documents. An energy desk that adopts a market-risk platform adds price-risk measurement for its book without changing what the energy platform is.
- **vs Financial Modeling Application** — single-analyst model building (spreadsheets/modeling tools) vs institutional multi-user risk operation with data foundations, limit state and governance. The former may compute a VaR; it cannot hold an institution's limit state.
- **IRRBB placement** — banking-book interest-rate risk (EVE/NII-class structural risk) is named *market risk* by a sampled vendor ("Structural (IRRBB) Market Risk") and is carried inside ALM/balance-sheet platforms; recorded as a variant of this type's machinery rather than a separate type. No taxonomy change proposed (ALM platforms have no directory leaf — same packaging note as the liquidity pass).

## Uncertainties

1. **No Tier-1 operational documentation** was reachable (help centers gated; MSCI challenge-walled; Bloomberg timed out; SS&C 403; Oracle datasheet PDFs not fetched). All observations are product/solution-page level. Screen-level workflow details (exact limit-state names, exact backtesting thresholds, default confidence levels, holding periods, scenario parameter values) are not asserted anywhere.
2. **Oracle's market-risk product depth** rests on one positioning paragraph + family context; measure families are not enumerated on the fetched page — calibrated as partial.
3. **The classic vendor-measures pure-play pole (MSCI RiskMetrics lineage) is absent from direct evidence** due to access failure; the factor-model philosophy is evidenced via Aladdin instead. Historical VaR standardization (RiskMetrics 1994 lineage) is common knowledge but was not re-verified against a live source — no precision claims depend on it.
4. **P&L attribution** is 4/4 in the sample but only at solution-page level; whether every market-risk product ships it cannot be asserted — held at L1.
5. **Real-time/intraday posture** is evidenced at the sell-side pole; the buy-side pages do not state freshness. Posture differences are recorded as variants, not verified in operational detail.
6. **The buy-side/sell-side unity** rests on the structural identity of the three legs across the four samples; a dedicated fund-risk or hedge-fund-risk product with materially different machinery (e.g., priming margin, look-through chains) could warrant a future variant pass — split-watch noted, no directory change proposed.
7. **IRRBB boundary** (banking-book rate risk in ALM platforms vs "structural market risk" naming) is a naming/packaging question that two sibling passes also hit; recorded consistently, no change proposed.

## Historical / Market-Sample Check (§24 reasoning)

Would older, regional, platform-native products still fit? Yes under the three-structure core: pre-VaR (1980s–early-1990s) bank market-risk practice maintained desk position sheets aggregated from trading systems (structure 1), computed sensitivity measures (delta, gamma, duration/DV01, greeks) and scenario/sensitivity results under defined rate/FX moves — the stressed view in embryo (structure 2), and ran notional/duration/delta limits with stop-loss discipline and daily reports to the risk/ALCO committee (structure 3) — without VaR (popularized mid-1990s), expected shortfall (2010s), Monte Carlo grids, factor models, FRTB (2010s) or real-time engines. The buy-side equivalent (duration, beta, sector and concentration limits over investment portfolios) fits the same core. Conversely, a market-data terminal without the institution's position does not fit (it is a data terminal); a trading system without risk measurement/control does not fit (it is a trading platform); a stress-report generator without the measured position does not fit (it is regulatory reporting). The definition therefore does not overfit the current VaR/FRTB implementation: VaR, ES, FRTB, factor models and real-time engines stay in the common/variant layers.

## Final Synthesis

A Market Risk Platform is the financial institution's (or investment manager's) market-risk system of record: it holds the institution's positions as an inspectable whole on a risk view — instruments mapped to market risk factors through valuation and sensitivity machinery, aggregatable by desk, portfolio and entity — translates that position into governed quantities of potential loss from adverse market moves (sensitivities, scenario and stress results, and, in most current implementations, distribution measures such as VaR and expected shortfall) under both current and stressed views, and keeps the whole state monitored and controlled against market-risk appetite through desk-level limits, breach/exception workflows, backtested model governance and governance reporting, computing regulatory capital figures from the same machinery where regulation requires. Its defining core is three jointly-held structures: the market-risk position of record, measures under current and stressed views, and the ongoing monitoring-and-control loop. Around this core, mature products add sensitivity analytics, VaR/ES machinery with backtesting, scenario/stress workbenches, P&L attribution, limit monitors with intraday usage and pre-emptive actions, exception workflows, unified risk data foundations, what-if analysis and regulatory capital machinery (FRTB-family). The market realizes the type along several poles: sell-side capital-markets platform modules (distribution/revaluation-led, trading-floor rhythm), enterprise analytics suite modules (valuation-model-led), buy-side integrated platform components (factor/scenario-led, beside portfolio management), and balance-sheet analytics-led platforms (banking-book structural market risk beside credit and liquidity) — with audience extensions to insurers and mortgage lenders. Boundaries: the multi-risk hub above it (ratified hub+slice from this side, completing the sibling set), credit and liquidity sibling slices (loss driver and measured object), actuarial modeling (liability projection vs risk-position measurement — flag discharged), trading platforms and portfolio management systems (execution/investment decisions vs risk measurement control), market-data terminals (input vs record), treasury/deal-capture systems (deal layer vs risk layer), regulatory reporting (figures vs reports), and energy trading (energy deal record vs generic cross-asset price-risk machinery).
