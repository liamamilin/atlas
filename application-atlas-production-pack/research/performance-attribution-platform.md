# Research Notes — Performance & Attribution Platform

## Research Goal

Understand what a Performance & Attribution Platform is in the **investment management** sense (DIRECTORY §08 Finance → Investment Management cluster, between Portfolio Management System and Investment Management Platform): what it measures, what it explains, what objects and models it is built on, who consumes its outputs, and where its boundary lies against neighboring Types — especially Portfolio Management System, Risk Analytics, Investment Accounting, and the unrelated Marketing Attribution Platform (§06).

## Initial Boundary (hypothesis before research)

- Core purpose: measure how investment portfolios performed over time, and explain **why** performance differed from a reference (benchmark / target / peer set) by decomposing the difference into named effects.
- Likely users: performance analysts, client reporting teams, portfolio managers, risk teams, asset owners (pension funds, insurers, sovereign funds), asset servicers (custodians/administrators).
- Likely confusion set: Portfolio Management System (manages portfolios forward), Investment Management Platform (whole lifecycle), Risk Analytics Platform (forward-looking), Marketing Attribution Platform (same word, different universe), BI/Reporting Platform (generic analytics).
- Unknowns: exact return-calculation machinery, attribution model taxonomy, whether retail fund performance reporting belongs to this Type, delivery variants (SaaS vs managed service vs suite module).

## Research Questions

1. What are the central objects? (portfolio, benchmark, return, effect, composite, hierarchy…)
2. How does the measurement loop work — from raw data to published results?
3. What attribution models exist and how do they relate (Brinson, factor, fixed income, currency, decision-based)?
4. What role do standards (GIPS) play in shaping the product?
5. Who are the users and what surfaces do they work in?
6. What variants exist (institutional attribution vs retail fund performance reporting vs asset-owner total-fund view vs private markets)?
7. What are the boundaries: vs Portfolio Management System, vs Risk Analytics, vs Investment Accounting, vs Marketing Attribution, vs BI?
8. What is delivery posture (standalone platform vs suite module vs managed service)?

## Representative Products

Selected for market representation, documentation reachability, different product philosophy, and different customer tiers:

| Product | Vendor | Philosophy / tier | Evidence tier reached |
|---|---|---|---|
| Revolution (+ Unity Performance, PARis, Revolution Composites) | Confluence Technologies (StatPro heritage) | Specialist cloud performance/attribution platform for asset managers, asset servicers, asset owners, consultants | Tier 2 (official solution + product pages) |
| PEARL | Ortec Finance | Asset-owner-centric performance measurement & attribution; decision-based attribution; SaaS + outsourced managed service | Tier 2 (official solution page + sub-pages listed) |
| SimCorp One + Axioma Solutions | SimCorp (Deutsche Börse group) | Suite-embedded: attribution/risk tools inside an IBOR-centered investment management platform | Tier 2 (official product pages) |
| Aladdin | BlackRock | Enterprise whole-portfolio ecosystem; performance sits beside risk, accounting, data | Tier 2 (official platform pages) |

Domain-standards source (not a product): **GIPS Standards** (CFA Institute) — the industry performance-presentation standard that several products explicitly support.

Rejected/dropped samples (source-access limitation): FactSet (product URLs 404), MSCI BarraOne (bot challenge), Morningstar Direct (empty responses ×2), Bloomberg PORT (timeout), Ortec Performance Pro URL (404; solution page used instead), Venn by Two Sigma (404), Northern Trust asset-servicing page (404; corporate root only).

## Sources

- Confluence — Performance & Attribution solution page: https://www.confluence.com/solutions/performance-attribution/
- Confluence — Revolution product page: https://www.confluence.com/products/revolution/
- Confluence — Unity Performance product page: https://www.confluence.com/products/unity-performance/
- Ortec Finance — Performance Measurement and Attribution (PEARL): https://www.ortecfinance.com/en/solutions/performance-measurement-and-attribution
- SimCorp — Axioma Solutions: https://www.simcorp.com/solutions/axioma-solutions ; SimCorp One (via https://www.simcorp.com/)
- BlackRock — Aladdin: https://www.blackrock.com/aladdin/
- GIPS Standards (CFA Institute): https://www.gipsstandards.org/ ; GIPS Standards for Firms: https://www.gipsstandards.org/standards/gips-standards-for-firms/

Research date: 2026-09-06.

**Sourcing limitation:** No vendor help-center / user-guide (Tier 1) documentation was reachable in this sample; all product evidence is Tier 2 (official product/solution pages). Several major vendors (FactSet, MSCI, Morningstar, Bloomberg) could not be reached at all. Consequently: no precise operational parameters (calculation frequencies, numeric limits, exact state names) are asserted anywhere; vendor-published figures are recorded below as vendor claims only.

---

## Product A — Confluence Revolution (and sibling products)

### Key observations (evidence layer A = directly observed on official pages)

- Confluence markets a dedicated **"Performance & Attribution"** solution category (alongside Composites & GIPS, Factor Analysis, Peer Analysis, Risk Analytics) — the leaf name matches a real market category.
- Positioning: "Calculate multi-asset performance results for large volumes of portfolios against a wide range of benchmarks quickly and efficiently. Gain insights to performance drivers with attribution analysis."
- Revolution = "multi-asset attribution analysis of risk and performance": "comprehensive multi-asset performance calculation, **contribution** and **multi-level attribution** in one integrated platform"; "pinpoint underlying drivers and factors through advanced **hybrid attribution models**".
- Fixed income: "flexible fixed income performance contribution, attribution and sensitivity analysis".
- Composites: Revolution Composites — "composite performance calculation and analysis with over 120 report templates and 1,000+ verifications for GIPS compliance" (vendor claim).
- Risk co-located: "comprehensive ex-post and ex-ante risk analytics" in the same platform (Revolution risk) — performance (backward-looking) and risk (forward-looking) sold as sibling modules.
- Data & workflow: "Streamlined data integration and automated workflows deliver comprehensive multi-asset class analytics on a single modularized cloud-based platform"; "Apply intelligent data management to improve the quality of performance and risk insights"; "controlled, automated workflows".
- Client reporting: "Flexible and customizable reporting with API access, multi-currency support and multi-lingual analysis".
- Managed services offered for analytics ("Reduce daily operational data management supporting performance and risk analytics").
- Segments: asset managers, asset owners, asset service providers, investment consultants. Vendor claims: 100,000+ actively managed portfolios supported; 9/10 of largest asset managers as clients; 80% of top 20 investment consultants use its institutional plan analytics.
- **Unity Performance** (sibling product): retail-fund performance measurement — "Automate fund performance calculation and reporting"; data "from your fund accounting and other source systems"; 200+ data fields "including NAVs, dividends, capital gains, net assets and expense ratios"; outputs: "over 40 daily standard performance returns, including load and no load, annualized and cumulative", "over 30 yield calculations", expense-adjusted hypothetical performance, gross-of-fee, after-tax, multi-currency, blended benchmarks, SEC N-1A risk/return, growth of 10K (vendor claims). Workflow: "data collection, aggregation, and validation to calculation of results and final report generation and distribution"; exception-based reviews; self-service platform; outsourced service (PROS).
- **PARis** (sibling): "performance measurement and attribution analysis for institutional plan types across asset classes. With straight-through data aggregation, portfolio analysis, reporting and peer benchmarking on a single platform."
- Awards: Risk.net "Performance Attribution Product of the Year" (vendor-claimed, 2022, sixth consecutive year) — evidence that "performance attribution" is a recognized product category with its own award line.

## Product B — Ortec Finance PEARL

### Key observations (layer A)

- PEARL = "performance measurement and attribution solution" for "asset owners, asset managers and fiduciary managers".
- Purpose framing: "Calculate the **added value of each investment decision**"; "Measure and analyze allocation decisions across multi-asset portfolios, currency hedges and overlay strategies."
- Attribution model catalog (each with a dedicated sub-page): **decision attribution** (proprietary IDP — Investment Decision Process — model: "dissect the contribution of your unique investment decisions to create a feedback loop"), **currency attribution** ("capture the impact of currency exposures and hedging decisions, both within a strategy or as part of an overlay, by analyzing tilts, proxies and instrument selection"), **multi-asset**, **equity** ("traditional **Brinson model** and/or **factor-based analysis**"), **fixed income** ("how yield, duration and credit quality impact your portfolio after splitting out the impact of currency, trading and pricing effects"), **private assets** ("illiquidity, valuations, and benchmarking challenges"), **ESG measurement** ("analyze both financial returns and environmental impact").
- Structural core: "Built upon **complex fund hierarchies** and **benchmark structures** that reflect investment strategies and overlays."
- Workflow: "Customizable data configurations, batch processing and interactive analysis; user-friendly interfaces, intuitive data validations and **audit trail** capabilities; configurable fund structures, multiple attribution models, and in-depth currency management; flexible reporting options, embedded **API data extraction** and integrated **GIPS reporting module**."
- Reporting: "online self-service platform that can be tailored to meet different stakeholder needs."
- Delivery: "offered as a SaaS with full implementation and data integration as well as an outsourced managed service (IPS) or a hybrid combination of both."
- Asset-owner extensions: funding-ratio attribution for asset owners; total-fund perspective; private-asset attribution under total-fund view; Total Portfolio Lens webinars (CalPERS case).
- Data dependency: partnership with Rimes "to optimize end-to-end data management for performance reporting … efficiently generates performance-ready data" — evidence that performance-ready data preparation is a distinct upstream concern.

## Product C — SimCorp (SimCorp One + Axioma Solutions)

### Key observations (layer A)

- SimCorp One: "unifies the full investment lifecycle, from portfolio construction and trading through to operations, accounting, and reporting, across every asset class, public and private"; "Axioma's portfolio construction, **risk, and attribution tools sit inside SimCorp One**".
- Axioma Solutions: "a powerful suite of risk, **performance** and portfolio construction tools"; "From **performance attribution** to backtesting to stress testing and scenario analysis" — attribution is one capability inside an analytics suite alongside optimizer and risk models (Axioma Risk, Axioma Factor Risk Models, Fixed Income Solutions).
- Industry coverage: asset management, pensions, insurance, central banks, sovereign wealth funds, wealth management, hedge funds.
- Awards: "Best IBOR Platform" (WatersTechnology, vendor-claimed) — the platform's center of gravity is the investment book of record; performance/attribution is a module on top of the IBOR.

## Product D — BlackRock Aladdin

### Key observations (layer A)

- Aladdin = "a tech platform that unifies the investment management process through a common data language … across public & private markets".
- Scope statement: "manage the entire process from building portfolios and **managing performance** to operations and accounting".
- Risk is the named product line (Aladdin Risk: "consistent, integrated view of risk and returns across asset classes"); performance is not a separately branded product page in the public nav — it appears as a capability inside the whole-portfolio platform.
- Client segments: asset managers, asset servicers, banks & brokers, corporates, insurers, pension funds, wealth managers; eFront/Preqin cover private markets.
- Disclaimer language confirms the calculation nature: "Performance and risk calculations … are based on assumptions, historical correlations, and other factors (such as inputs provided by the Aladdin users) and are not assured to predict future results."

## Product E (domain standard) — GIPS Standards (CFA Institute)

### Key observations (layer A)

- Purpose: "Firms comply with the GIPS standards to fulfill their ethical duty to **fully disclose and fairly present performance** … and respond to the demands of prospective clients and investors."
- Separate standards tracks: **for Firms**, **for Asset Owners**, **for Verifiers**, **for Fiduciary Management Providers** — mirrors the user segments seen in products.
- Guidance Statements exist for: Benchmarks, Overlay Strategies, OCIO Portfolios, Wrap Fee Portfolios, Broad Distribution Pooled Funds — the exact structural topics attribution platforms must handle (benchmarks, overlays, pooled funds).
- Adoption scale (vendor-neutral claims): 1,600+ organizations claim compliance; adopted in 54 markets; all top 25 asset managers claim compliance for all or part of their business.
- Related professional credential: CIPM — "Certificate in Investment Performance Measurement … performance evaluation, risk analysis, and manager selection" — confirms "performance measurement" is a named profession.

---

## Cross-product Comparison

| Dimension | Confluence Revolution | Ortec PEARL | SimCorp/Axioma | Aladdin |
|---|---|---|---|---|
| Measured units | portfolios at volume; fund hierarchies; composites; institutional plans | complex fund hierarchies + benchmark structures; total fund | portfolios on the IBOR, public + private | whole portfolios across public & private markets |
| Return measurement | multi-asset performance calculation + contribution | performance measurement across fund hierarchies | performance tools on IBOR data | "managing performance" inside the platform |
| Comparison reference | "wide range of benchmarks"; blended benchmarks (Unity) | benchmark structures reflecting strategies and overlays | factor models / benchmarks via Axioma | risk & return views vs benchmarks |
| Attribution models | multi-level, hybrid, fixed income, factor | decision (IDP), currency/overlay, multi-asset, equity Brinson + factor, fixed income, private assets, ESG | performance attribution within Axioma suite | not publicly detailed |
| Standards support | Revolution Composites: GIPS verifications | integrated GIPS reporting module | (not stated on fetched pages) | (not stated on fetched pages) |
| Reporting | customizable client reporting, API, multi-currency/lingual, 120+ templates | online self-service platform, tailored per stakeholder, API extraction | reporting inside SimCorp One | platform dashboards |
| Data posture | streamlined data integration, intelligent data management, pricing/benchmark data services | performance-ready data via Rimes partnership; data validations, audit trail | single data core (IBOR) — no reconciliation delays | common data language, Aladdin Data Cloud |
| Risk co-location | Revolution risk (ex-post + ex-ante) | separate Ortec solution line (Strategic Risk Management) | Axioma Risk sibling | Aladdin Risk flagship |
| Delivery | modularized cloud platform + managed services | SaaS / outsourced managed service / hybrid | suite module in SimCorp One | enterprise ecosystem |
| Primary segments | asset managers, servicers, owners, consultants | asset owners, asset managers, fiduciary managers | asset managers, pensions, insurers, central banks, wealth | asset managers, servicers, insurers, pensions, wealth |

**Layer B (cross-product commonality) findings:**

1. Every sampled product centers on **portfolios as measured units** organized in **structures** (hierarchies, composites, plans) — never a single flat list.
2. Every sampled product pairs **performance calculation** with **explanation** (attribution/contribution/drivers) — measurement alone is never the whole product.
3. Every sampled product treats **data readiness** as a first-class concern (integration, validation, audit trail, performance-ready data) — the platform consumes positions/valuations/cash flows produced elsewhere (fund accounting, IBOR, custodian).
4. Every sampled product's terminal output is **stakeholder-facing reporting** (client reports, self-service dashboards, API extracts).
5. **Benchmarks/benchmark structures** appear in every product as the comparison backbone.
6. **Risk analytics is a sibling, not the same thing** — co-located in the same vendors' catalogs but always a separate module/solution line (ex-ante vs ex-post).
7. **GIPS** appears where institutional/composite reporting matters (Revolution Composites, PEARL GIPS module) — standards-shaped functionality.
8. Delivery spans a gradient: standalone specialist platform (Revolution, PEARL) ↔ suite module (Axioma in SimCorp One) ↔ capability inside an ecosystem (Aladdin) ↔ outsourced managed service (PEARL IPS, Confluence PROS, Revolution managed services).

## Canonical Model (working abstraction)

```text
Measured portfolio population (identified portfolios/accounts in structures:
  hierarchies, composites, plans)
  └── fed by: positions, valuations, transactions/cash flows, prices (from
      accounting / IBOR / custodian / data vendors)
        └── Periodic return measurement (period returns, linked over time;
            contribution of holdings)
              └── Comparison reference (benchmark / target / peer structure)
                    └── Excess return
                          └── Attribution decomposition (named, quantified
                              effects: allocation, selection, currency,
                              factor, decision, …)
                                └── Performance reporting (reports,
                                    dashboards, extracts) to stakeholders
```

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **Measured portfolio population** — identified portfolios/accounts (with holdings, valuations, cash flows as input) are the units of measurement, organized in structures.
2. **Periodic return measurement** — returns are computed for defined periods from that data and linked into longer horizons.
3. **Comparison reference** — performance is evaluated against a defined reference (benchmark, target, or peer structure), producing an excess/relative result.
4. **Attribution decomposition** — the performance difference is broken into named, quantified effects tied to decisions or segments.
5. **Results surfaced for stakeholder consumption** — reports, dashboards, or data extracts.

Remove any one: without (1)–(2) it is not measuring anything; without (3)–(4) it is a valuation/BI tool, not performance & attribution; without (5) the results never reach the people the Type exists for.

### L1 — Common Mature Structure

- fund/account hierarchies and composites (incl. GIPS-style composite management)
- security-level contribution analysis alongside attribution
- multi-model attribution catalog: equity Brinson (allocation/selection/interaction), factor-based, fixed income (yield/duration/credit with currency/trading/pricing split-outs), currency & overlay attribution, decision-process attribution
- data ingestion/validation pipeline with quality controls and audit trail
- benchmark data management (index series, blended/custom benchmarks)
- report templates, scheduled/production reporting, API data extraction
- risk measures alongside returns (volatility, tracking error; ex-post)
- multi-currency (and commonly multi-lingual) results
- roles/permissions and audit trail for a controlled production process
- peer/universe comparison

### L2 — Variant / Optional Structure

- segment pole: institutional portfolio attribution ↔ retail fund performance reporting (NAV-based standard returns, yields, load/no-load, after-tax, growth-of-10K, regulatory formats) ↔ asset-owner total-fund/decision attribution ↔ private-markets performance (illiquidity, valuations, money-weighted measures)
- attribution model choice (Brinson vs factor vs hybrid vs decision-based) is a configuration, not a definition
- calculation cadence (daily vs monthly) — varies by segment; not asserted as a standard
- return methodology emphasis (time-weighted vs money-weighted) varies by asset class
- delivery posture: SaaS self-service vs managed/outsourced service vs suite module vs ecosystem capability
- ESG attribution; climate; funding-ratio/liability-side attribution for insurers/pensions
- regulatory/marketing output formats (e.g., SEC N-1A risk/return — vendor-specific instance)
- deployment: cloud vs on-premises

### L3 — Vendor-specific (research notes only)

- Confluence: Revolution's "120+ report templates / 1,000+ verifications", "80M+ API calls daily", POINT Prompt (plain-English queries in Excel), PARis plan universes, Unity's "40+ standard returns / 30+ yield calculations", PROS outsourcing brand, Risk.net award claims.
- Ortec: IDP (Investment Decision Process) decision-attribution model, PEARL brand, IPS managed-service brand, Pulse newsletter, Rimes partnership specifics.
- SimCorp: SimCorp One packaging, Axioma brand, IBOR award claims, Domos/support portals.
- BlackRock: Aladdin branding, Aladdin Wealth/Provider/Copilot lines, eFront/Preqin private-markets pairing, "language of the whole portfolio" positioning.

## Vendor-specific Findings

- Decision-process attribution (Ortec IDP) is currently a single-vendor framing; other vendors express the same intent as "performance drivers" / "hybrid attribution" — treat decision attribution as an L2 model choice, not a Type property.
- Retail fund performance reporting (Unity Performance) is a distinct segment pole with its own output formats; it shares the L0 (measured funds, period returns, reference where applicable, reporting) but its attribution content is thin — it is a Variant, not a separate Type (it still measures portfolio/fund performance for stakeholders).
- Managed-service delivery (PEARL IPS, PROS, Revolution managed services) shows the function is also sold as an operated service — delivery variant only.

## Rejected Findings

- "Performance & Attribution = risk analytics" — rejected: risk is consistently a separate module/solution line; ex-ante vs ex-post is the working split. Co-location ≠ identity.
- "Attribution requires a commercial benchmark index" — rejected: references can be targets, policy benchmarks, peer universes, or factor models; the invariant is a defined comparison basis, not an index license.
- "This Type is defined by GIPS compliance" — rejected: GIPS support is common where composites matter (L1) but several products/segments (asset-owner total-fund, retail fund reporting) operate without it.
- "Daily calculation is the standard" — rejected: cadence varies by segment and no cross-product evidence was reachable; left unstated in the final document.
- "Marketing attribution belongs here" — rejected: same word, different universe (see Boundary Findings).

## Boundary Findings

- **vs Portfolio Management System (§08 sibling):** PMS centers on constructing and managing portfolios going forward (positions, orders, rebalancing, pre-trade compliance). P&A measures and explains results after the fact. Structural test: remove attribution/excess-return decomposition → a PMS remains; remove portfolio construction/trading → P&A remains. Evidence: SimCorp ships both (front office vs Axioma attribution) as distinct capability sets; Aladdin separates "building portfolios" from "managing performance".
- **vs Investment Management Platform (§08 sibling):** the platform spans the full lifecycle (construction → trading → operations → accounting → reporting); P&A is the measurement/explanation slice, sold both inside such platforms (Axioma in SimCorp One, performance in Aladdin) and standalone (Revolution, PEARL). Gradient, not a wall — the same vendors appear on both sides.
- **vs Risk Analytics Platform (§08 sibling):** risk is forward-looking (ex-ante) exposure/scenario analysis; performance & attribution is backward-looking (ex-post) realized-result explanation. Products bundle both (Revolution, Axioma, Aladdin) but always as separate modules. Boundary held on center of gravity.
- **vs Investment Accounting / Fund Accounting:** accounting produces the books and NAV; P&A consumes them ("automate collection of data from your fund accounting and other source systems" — Unity Performance). Upstream producer vs downstream measurer.
- **vs Marketing Attribution Platform (§06):** same word "attribution", unrelated universe — marketing channels/campaigns/conversions vs investment portfolios/benchmarks/returns. No shared objects, users, or workflows. Critical disambiguation for the directory.
- **vs BI / Reporting Platform (§13):** generic analytics can slice any data; P&A embeds investment-specific computation (return math, benchmark structures, attribution models, GIPS semantics). A BI tool without the return/attribution model layer does not become a P&A platform.
- **"Remove what to become another Type":** remove the benchmark/reference and attribution decomposition → portfolio valuation/reporting tool (drifts toward accounting/BI); remove the measured-portfolio population → generic dashboard platform (BI); add forward-looking portfolio construction → Portfolio Management System.

**Historical / market-sample check:** older and regional shapes still fit L0 — custodian-supplied performance reports, spreadsheet-based Brinson attribution, monthly institutional reporting, non-GIPS regional markets, Japanese/Dutch pension reporting (Ortec's home market), platform-native custodian portals. None require cloud, factor models, GIPS modules, or daily cadence. L0 holds across eras and regions.

## Uncertainties

- Exact return-calculation mechanics (linking formulas, cash-flow treatments) could not be verified from Tier-1 docs — kept conceptual in the final document.
- Whether "Performance & Attribution" and a hypothetical "Performance Measurement" leaf should be separate — the market treats measurement and attribution as one bundled category (Confluence solution page; Ortec solution name; Risk.net award line); no split proposed.
- Aladdin's performance-specific capabilities are not publicly detailed; treated as ecosystem-embedded capability with positioning-level evidence only.
- Calculation cadence norms (daily vs monthly) per segment — unverified; not asserted.
- FactSet/MSCI/Morningstar/Bloomberg shapes unverified (unreachable); the sample may under-represent terminal/workstation-style implementations.

## Final Synthesis

A Performance & Attribution Platform is the investment industry's **measurement and explanation system for realized portfolio results**: it maintains a population of measured portfolios fed by positions/valuations/cash flows from upstream systems, computes periodic returns linked over time, evaluates them against defined references (benchmarks/targets/peers), decomposes the difference into named quantified effects (allocation, selection, currency, factor, decision), and packages the results as stakeholder-facing reports and extracts. Its defining core is small and era-independent; everything else — composites/GIPS, factor and fixed-income models, risk co-location, delivery posture, segment-specific output formats — is mature structure or variant. Its closest structural neighbors are the Portfolio Management System (forward-looking management) and Risk Analytics (forward-looking exposure), and it must never be confused with the same-named marketing discipline.
