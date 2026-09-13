# Research Notes — Actuarial Modeling Platform

Research date: **2026-09-06**

## Research Goal

Understand what an Actuarial Modeling Platform actually is from real products: what objects exist inside it (models, assumptions, data, runs, results), who uses it, how actuarial work flows through it, what rules govern it, and where its boundaries lie against adjacent Types (financial modeling, risk platforms, data science workbenches, policy administration, regulatory reporting).

## Initial Boundary

Working hypothesis at start:

- Software used by actuaries in insurance/reinsurance/pensions to define calculation models of insurance products and liabilities, run them over policy portfolios under assumptions/scenarios, and produce projected results (cash flows, reserves, capital, premiums) for pricing, valuation, reserving, capital, planning, and regulatory reporting.
- Nearest neighbors: Financial Modeling Application, Financial Risk Management Platform, Data Science Workbench, Spreadsheet Application (historical substrate), Regulatory Reporting Platform, Insurance Policy Administration System, Pension Administration Platform.
- Known risk: the name covers at least two job centers — forward projection/valuation (life/pension engines) and pricing/reserving model building (P&C) — which use different data objects (in-force portfolios vs historical experience). Definition must not overfit one center.

## Research Questions

1. What is an "actuarial model" as an object in these systems? How is model logic kept separate from data?
2. How are actuarial assumptions (mortality, lapse, expense, discount, rating factors) managed — tables, versioning, assumption sets?
3. What is the input data object (in-force / model points / seriatim records / experience data), and where does it come from?
4. How does a projection run work — deterministic vs stochastic, scenario structures, batch/grid/cloud execution?
5. What results are produced and how are they analyzed (drill-down, movement analysis, source of earnings, dashboards)?
6. What governance/audit/versioning structures exist and why?
7. What jobs does the platform serve (pricing, valuation, reserving, ALM, capital, planning, stress testing, experience studies)?
8. Where is the boundary vs spreadsheets, financial modeling tools, ML/data science workbenches, and reporting platforms?
9. Would older/regional products still fit the final definition?

## Representative Products

Chosen for market representativeness, documentation accessibility, different product philosophies (classic engine vs cloud-native platform vs AI-first pricing), and different market segments (life projection vs P&C pricing/reserving):

| Product | Vendor | Segment | Philosophy | Evidence |
|---|---|---|---|---|
| AXIS actuarial system | Moody's | Life & annuity projection/valuation (insurers, reinsurers, consultants); 30+ years market presence | Classic comprehensive projection engine, now enterprise/cloud-hosted | A (official pages fetched) |
| SLOPE (now Akur8 Life) | Slope Software / Akur8 | Life & annuities, pension & PRT, LTC; universities | Cloud-native, transparency-first visual modeling platform | A (official pages fetched) |
| Akur8 Pricing / Reserving (Arius) | Akur8 | P&C pricing and reserving, all lines, global incl. Japan/US/EU | AI-first transparent GLM/GAM modeling, modular pricing chain | A (official pages fetched) |

Additional market anchors (no official documentation accessible during research — see Sources limitations): Milliman MG-ALFA, WTW Unify / ResQ, Moody's Prophet; historical: GGY AXIS lineage (pre-Moody's), SunGard MoSes (discontinued). Used only for market-context statements, never for precise operational claims.

## Sources

Successfully fetched (2026-09-06):

- Moody's — Actuarial Modeling (AXIS actuarial system): https://www.moodys.com/web/en/us/solutions/capital-management/actuarial-modeling.html
- Moody's — Insurance solutions (actuaries / finance / risk personas): https://www.moodys.com/web/en/us/who-we-serve/insurance.html
- Slope Software — home (platform pillars, use cases, regulatory frameworks): https://slopesoftware.com/
- Slope Software — Model Development: https://slopesoftware.com/slope-platform/model-development/
- Slope Software — Assumption Management: https://slopesoftware.com/slope-platform/assumption-management/
- Slope Software — Results Analysis: https://slopesoftware.com/slope-platform/results-analysis/
- Akur8 — home (platform positioning, Pricing/Reserving/Life lines, AI posture): https://www.akur8.com/
- Akur8 — Discover module page: https://www.akur8.com/pricing/discover

**Source-access limitation:** official operational documentation for Milliman MG-ALFA and WTW Unify/ResQ could not be reached (repeated 404s on all attempted URL patterns for milliman.com and wtwco.com). Search engines were unusable from the research environment (DuckDuckGo/Brave timeouts, Bing localized results). Wikipedia timed out. Per evidence rules: no precise claims are made for MG-ALFA/Unify/Prophet in either document; these vendors appear only as market anchors; cross-product claims are supported by the three products with direct evidence, with assertion strength calibrated accordingly. Moody's Prophet was NOT directly documented in fetched pages; Prophet is mentioned only as a known Moody's-era market product, with all structural claims anchored to the AXIS pages.

## Product Observations

### Moody's AXIS (actuarial system) — Evidence Layer A

From the official "Actuarial Modeling" solution page (fetched 2026-09-06):

- Positioning: "a powerful modeling solution used by insurers, reinsurers, and consultants for actuarial analysis of life insurance and annuity business"; "single integrated platform" for "core actuarial tasks across products, lines of business, and regulatory use cases"; 30+ years in the market.
- Context driver named by vendor: IFRS 17, LDTI and financial disclosures "generate exponential growth in modeling complexity and volume"; reporting deadlines and governance standards pressure.
- **Pricing and product development**: specify "detailed issue age- and risk class-specific product features" by generating or importing product values; explore distribution compensation (commission/bonus structures); "defining applicable reserve methods and assumptions for multiple valuation purposes"; define capital targets and taxation; simulate sales illustrations; project earnings "on multiple bases"; calculate profitability/return on capital; "solving for target values of any of the above by making iterative adjustments" (goal-seeking).
- **Liability valuation**: "Based on full seriatim in-force business data files for a single valuation date, the AXIS system can transform and allocate policy data to AXIS model definition and control objects created by the user, and calculate up to eight independent reserve calculations in a single run" — statutory, Solvency II best estimate, tax, US GAAP/IFRS public reporting, economic balance sheets, embedded value, stochastic options/guarantees value, capital requirements. Multiple in-force files and multiple assumption bases; movement tracing of business and reserves through the reporting period; granular data files for IFRS 17 / LDTI.
- **Asset allocation and investment**: import in-force investment data; project detailed cash flows "on a monthly, quarterly, or annual basis for up to 100 years"; asset movements (maturities, defaults, sales, prepayments, calls); income statement and balance sheet detail; multiple asset accounting bases; links to a structured finance cash-flow engine.
- **Risk and capital**: regulatory risk-based capital calculations (named: Solvency II, C-ROSS, NAIC, Hong Kong RBC); applies from "a single policy, product, or product group; a line of business; or entity level"; models in-force portfolios and new business sales plans; "stochastic calculations... at time zero and nested into projections at multiple levels."
- **Earnings and performance analysis**: margins by assumption; movement analysis reports (policy count, sums insured, reserves); "source of earnings analysis... by the major sources of profit (also called gain and loss analysis)"; experience analysis (actual vs expected) "for purposes of assumption refinement."
- **Business planning**: current-reporting asset/liability/capital calculations as foundation for "projected financials on multiple bases for up to 100 years"; "Assets and liabilities dynamically interact based on the economic scenario path and chosen reinvestment strategies"; metrics incl. embedded value, VaR/CTE; "sensitivity analysis and stress testing capabilities ('what if?' analysis)".
- **Stress testing and ORSA**: deterministic scenarios of single/multiple interacting stress events or trends; reverse stress testing "through an automatic iterative process"; stresses combined with management actions (reinsurance, repricing, investment strategies, hedging, sales plan adjustments).
- **Execution architecture**: "centralized enterprise modeling environment that supports governance, control, and scalability across cloud-based infrastructure"; managed cloud (AXIS Cloud), client-cloud orchestration (Enterprise GridLink), pay-per-use GridLink-as-a-Service — i.e., large projection workloads are distributed/scaled as a first-class concern.
- **Companion products**: Market-Consistent Scenario Generator (risk-neutral scenarios), Real-World Scenario Generator (ALM), LifeRisks (mortality/longevity catastrophe), Risk-Integrated Credit Solution — scenario/asset modeling is packaged adjacent to the actuarial system and integrated ("run both models without the need for manual intervention or file conversions" per vendor whitepaper abstract).
- **Governance signals**: "fully transparent and documented" capabilities; SOC 1/2 Type 2 reports for named cloud solutions; "controlled access, workflow management, automation, and scalable job execution."
- From the insurance solutions page (personas): actuaries — "project future cash flows, assess profitability, explore diverse scenarios, and efficiently create new insurance products", "easily compute results under multiple bases"; finance managers — regulatory reporting for Solvency II, LICAT, LDTI, CECL, IFRS 17, IFRS 9; risk managers — ORSA, stress conditions, risk appetite limits.

### SLOPE (Akur8 Life) — Evidence Layer A

From official platform pages (fetched 2026-09-06):

- Positioning: "Actuarial Modeling Platform — actuarial modeling, made transparent. Every assumption, formula, and result in SLOPE is made visible"; "Transparent Actuarial Modeling Platform."
- **Three platform pillars (vendor's own module split)**:
  - **Assumptions** — "Aggregate and manage data from upstream sources to build robust assumptions"; "define, consolidate, and manage the many inputs that drive your models"; import/export in various formats; in-app adjustments with "automatically track the version history of changes"; "auto-versioning of assumptions for audit trails"; dynamic table management ("define your table structures during model development", file imports, table editor); field-level real-time validation ("avoid run-time errors"); **assumption set management** ("groupings of assumptions that stack on one another to more easily control values at run time... flexibility necessary for complex scenarios"); dynamic investment strategies (allocation, invest/disinvest, duration/convexity matching); grouping for large datasets; projection templates ("build commonly run setups once and use as a template").
  - **Models** — "Build models to meet your exact business needs... transparent and flexible"; visual code interface (formulas, user-defined variables, "without the need for code"); **Relationship View** ("see the flow of data as it moves from your assumptions to your outputs... determine the drivers of results"); real-time formula validation ("catch problems before they occur" / "prevent... projection run errors"); easy table management (custom input tables with indexes/columns referenced in formula builder); flexible file formats (Excel, delimited); **simplified scenario setup** ("fixed income yield curves, variable rates, and indexes... multiple currencies"); **pre-built library** of asset and liability products; customer quote: model "products that have unique features without... system limitations".
  - **Results** — embedded analytics engine "automatically populates report dashboards with key data from your model runs"; "no post-processing or data migration is required after execution"; pre-built report suite + custom reports; **drill-down**: "trace calculations through individual model points and timesteps"; shareable links, exports, shared company dashboards; debug "unexpected model behavior".
- **Runs/performance**: "Complete projections at lightning speed"; High Performance Mode ("complete runs 10 times faster" per vendor marketing — treat multiplier as vendor claim); cloud-native; API for automation; Snowflake integration (query actuarial output alongside company data); "Record and access all inputs used for a run."
- **Use cases (vendor's own list)**: Pricing ("explore every possibility and iterate faster"); Valuation ("calculate reserves with confidence"); ALM ("asset adequacy"); Experience Studies ("build robust, well-tested assumptions to better your company's actuarial models").
- **Industries**: Life & Annuities; Pension & PRT; Supplemental Health/Disability/LTC; Universities (classroom use).
- **Regulatory frameworks (vendor's own list)**: Bermuda BSCR, IFRS 17, LICAT, LDTI, Solvency II.
- **Users (vendor's own list)**: Actuaries; Managers; C-Suites.

### Akur8 (Pricing / Reserving) — Evidence Layer A

From official pages (fetched 2026-09-06):

- Positioning: "The Global Actuarial AI Platform"; "AI-first, end-to-end actuarial solutions, built for trust and transparency"; 350+ insurers claimed.
- **Product lines**: Pricing (P&C), Reserving (P&C; product family "Arius", "Arius Enterprise", "Triangles on Demand"), Life (via acquisition of Slope Software).
- **Pricing module chain (vendor's own nav)**: Data → Risk → Demand → Rate (Rate Repo) → Optim → Deploy — i.e., data prep, risk premium modeling, demand modeling, rate plan construction, optimization, deployment to production rating. Plus "Discover" (SERFF filing market intelligence; vendor-specific adjacency).
- **AI posture**: "Transparent GAMs/GLMs fully automated... powered by proprietary algorithms (Derivative Lasso, Elasticity Modeling)"; GBMs "that complement GLM modeling, while maintaining interpretability and traceability"; agentic AI/LLMs for workflow automation and market intelligence.
- **Governance emphasis**: "built-in guardrails, and full model explainability, ensuring every decision is auditable, compliant, and scalable"; customer testimonials repeatedly cite "transparency and control", "governance framework — some guardrails", "robust and safe" process.
- Life line description: "Gain complete visibility across the modeling lifecycle, from initial assumptions to resulting outputs" — same assumptions→outputs lifecycle as the projection platforms.
- **Deployment**: cloud-native, integration partnerships (e.g., Guidewire Marketplace accelerator for Deploy), 150+ consulting partners.

## Cross-product Comparison

| Structure | AXIS (Moody's) | SLOPE (Akur8 Life) | Akur8 Pricing/Reserving | Assessment |
|---|---|---|---|---|
| User-defined model as explicit, inspectable calculation logic | "model definition and control objects created by the user"; product features/definitions | visual formula interface, user-defined variables, relationship view | transparent GLMs/GAMs built by actuaries | Common to all → core |
| Model logic kept separate from data/assumptions | multiple assumption bases vs in-force files; "reserve methods and assumptions" definable per valuation purpose | Assumptions module separate from Models module | Data/Risk modules separate from model fitting | Common to all → core |
| Managed assumption tables/sets (rates, curves, factors) | "multiple assumption bases"; experience assumptions for mortality/lapses/expenses | first-class Assumptions pillar; versioning; stacked assumption sets | assumptions in pricing/reserving lifecycle ("from initial assumptions to resulting outputs") | Common to all → core |
| Insurance data intake (in-force / experience) structured for the model | seriatim in-force files for a valuation date; transform & allocate policy data | aggregate data from upstream sources; model points in results | policy/claims data in Data module; triangles for reserving | Common to all → core |
| Executed runs producing persisted, analyzable results | "in a single run"; runs at enterprise scale; movement/source-of-earnings reports on results | model runs; "all inputs used for a run"; dashboards from runs | model builds/iterations; pricing output to Rate/Deploy | Common to all → core |
| Deterministic stress / scenario analysis | stress testing & ORSA section; reverse stress testing | scenario setup (yield curves, variable rates) | (not primary in pricing) | Common in projection segment (2/3) → common mature |
| Stochastic projection / economic scenario generation | nested stochastic; companion scenario generators | (not surfaced on fetched pages) | (not primary) | Strong in classic engines; single-product evidence → common/optional |
| Asset-side modeling / ALM | dedicated section (investment projection, reinvestment, dynamic interaction) | ALM use case; dynamic investment strategies; pre-built asset library | (not primary) | Common in life projection segment (2/3) → common |
| Multi-basis / multi-framework calculation | "multiple bases"; named frameworks (Solvency II, C-ROSS, NAIC, HK RBC, IFRS 17, LDTI) | named frameworks (IFRS 17, LDTI, LICAT, Solvency II, Bermuda) | regulatory defensibility emphasized (filing context) | Common (2/3 direct) → common mature |
| Versioning / audit trail of assumptions & runs | governance/control enterprise environment; documented | auto-versioning, audit trails, all inputs per run recorded | auditability, guardrails, explainability | Common (2/3 explicit) → common mature |
| Drill-down from results to model point / timestep | granular data files; movement analysis by assumption | "trace calculations through individual model points and timesteps" | (results granularity not surfaced) | 2/3 direct → common |
| Grid / cloud / distributed execution | GridLink, AXIS Cloud, hosted, pay-per-use | cloud-native, High Performance Mode | cloud-native | Common (3/3) but deployment-shaped → common, not defining |
| Pre-built model/product libraries | (system maintained by vendor; not framed as user library) | pre-built library of asset/liability products | (templates not surfaced) | Single-product evidence → optional/product-leaning |
| Experience studies feeding assumption refinement | experience analysis section | Experience Studies use case | (implied in pricing data cycle) | Common (2/3) → common |
| Goal-seeking / iterative solving | "solving for target values... iterative adjustments"; reverse stress testing | (not surfaced) | Optim module (optimization) | Partial → common/optional |
| ML-assisted model fitting | whitepaper (clustering for efficiency) — research-level | (not surfaced) | core proposition (transparent GLM/GAM, GBM) | Product-specific to pricing segment for now |
| Deployment to production rating | (not in scope of AXIS page) | (not surfaced) | Deploy module, Guidewire accelerator | Product-specific |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Smallest structure without which the software is not recognizable as an actuarial modeling platform:

1. **User-defined actuarial model** — explicit, inspectable calculation logic representing insurance business (product rules, liabilities and their cash flows; or rating/loss behavior), maintained separately from both the data it acts on and the parameter values it uses.
2. **Managed actuarial assumptions** — first-class, replaceable inputs to the model (rates, tables, curves, factors: mortality, lapse, expenses, discounting, rating factors), held and versioned as distinct objects rather than hard-coded logic.
3. **Insurance data intake structured for the model** — policy-level in-force/experience datasets loaded, validated, and shaped into the form the model consumes (in-force portfolios for projection; experience/claims data for pricing and reserving).
4. **Controlled projection/calibration runs as managed executions** — the platform executes model × assumptions × data (under selected scenario settings where projection applies) as distinct, repeatable runs whose inputs and outputs are recorded and re-openable.

Rationale: remove the model → it is a data/analytics tool, not modeling. Remove assumptions-as-inputs → actuaries cannot do the core actuarial act (assumption setting/sensitizing). Remove structured insurance data → nothing actuarial to compute. Remove managed runs → a spreadsheet/calculator, not a modeling platform. All four are directly evidenced in all three sampled products and plausibly present across the market's classic engines (market anchors) — and satisfy the historical check: 1990s-era engines (AXIS lineage, MoSes, Prophet-era systems) already exhibited user-defined product models, assumption tables, in-force files, and batch runs; regional frameworks differ only in which bases/frameworks are computed (L2).

### L1 — Common Mature Structure

Present in most mature modern products (evidence: 2–3 of 3 sampled, or 1 with strong structural role):

- Deterministic stress/what-if scenarios and scenario management (AXIS, SLOPE)
- Stochastic projection with economic scenario generation for valuation/ALM/capital (AXIS explicit + companion generators; historically central to classic engines)
- Asset-side modeling and ALM (asset projections, reinvestment strategies, dynamic asset-liability interaction) (AXIS, SLOPE)
- Multi-basis / multi-regulatory-framework calculation and reporting support (IFRS 17, LDTI, Solvency II, LICAT, local statutory/GAAP) (AXIS, SLOPE, Akur8 defensibility)
- Assumption and run governance: versioning, audit trails, recorded run inputs, controlled access (SLOPE explicit; AXIS enterprise governance; Akur8 auditability)
- Results analysis: report dashboards, drill-down to model point/timestep/assumption level, movement & source-of-earnings analysis, export (SLOPE, AXIS)
- Experience studies / actual-vs-expected analysis feeding assumption refinement (AXIS, SLOPE)
- New business / sales-plan modeling and business planning projections (AXIS; classic engine behavior generally)
- Goal-seeking and iterative solving (target premiums/reserves; reverse stress testing) (AXIS; Akur8 Optim analog)
- High-performance / distributed execution of large runs (AXIS GridLink/Cloud; SLOPE High Performance; cloud-native Akur8)
- Pre-built product/asset libraries and projection templates (SLOPE; templating implied by AXIS "system maintained" posture)

### L2 — Variant / Optional Structure

- **Job center**: valuation/projection-first (AXIS, SLOPE, classic engines) vs pricing-first (Akur8 Pricing) vs reserving-first (Akur8 Arius). These change the primary data object (in-force vs experience/triangles) and the primary output (projected liabilities vs fitted rating plans / reserve estimates).
- **Business line**: life & annuities; pensions (incl. PRT); supplemental health/disability/LTC (SLOPE); P&C pricing/reserving (Akur8); mortality/longevity catastrophe overlays (Moody's LifeRisks).
- **Deployment**: on-premise/managed grids → vendor-hosted cloud → client-cloud orchestration → SaaS (AXIS hosted/GridLink/Cloud; SLOPE cloud-native; Akur8 cloud-native).
- **Authoring surface**: proprietary engine languages/tables (classic engines' historical pattern) vs visual code-free formula interfaces (SLOPE) vs automated ML with actuarial guardrails (Akur8).
- **Regulatory regime packaging**: which frameworks are shipped as built-ins (Solvency II, C-ROSS, NAIC, HK RBC, LICAT, Bermuda, IFRS 17, LDTI) — regional, era-dependent.
- **Suite coupling**: standalone actuarial system vs component of a wider insurance-risk suite with scenario generators, credit solutions, IFRS 17 reporting engines (Moody's ecosystem), or pricing-deployment integration into policy admin/rating systems (Akur8 Deploy ↔ Guidewire).
- **Data platform integration**: warehouse/lakehouse connectivity for actuarial output (SLOPE ↔ Snowflake).

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Moody's AXIS: "up to eight independent reserve calculations in a single run"; projections "up to 100 years" at monthly/quarterly/annual granularity; GridLink / GridLink-as-a-Service / AXIS Cloud product names; RiskIntegrity for IFRS 17; Market-Consistent / Real-World Scenario Generators; LifeRisks; RICS; SOC report scope list; Chartis award claims.
- SLOPE: Formula Wheel, Relationship View, High Performance Mode ("10×" vendor claim), SLOPE API PDF, Snowflake integration, university program, pre-built library.
- Akur8: module names Data/Risk/Demand/Rate/Rate Repo/Optim/Deploy/Discover; Arius / Arius Enterprise / Triangles on Demand; proprietary algorithms (Derivative Lasso, Elasticity Modeling); Guidewire Marketplace accelerator; 350+ clients and 150+ partner claims; biweekly SERFF refresh claims.

## Vendor-specific Findings

(Consolidated above under L3; nothing from this list enters the canonical document.)

## Rejected Findings

Considered and rejected for the defining core, with reasons:

- **"Stochastic scenario execution is defining"** — rejected: historically valid platforms ran deterministic projections; pricing platforms calibrate without stochastic projection. Scenarios are L1.
- **"Forward multi-period projection is defining"** — rejected as an invariant: the pricing variant fits rating models on historical experience rather than projecting an in-force forward. Kept instead as the *dominant job* of the valuation/projection variant, with the pricing variant documented separately.
- **"Multi-framework regulatory calculation is defining"** — rejected: framework set is era/region dependent (L2); a pricing platform can be fully actuarial without any of them.
- **"Seriatim policy-level granularity is defining"** — rejected: granularity of model points varies and some products aggregate; drill-down granularity is L1 analysis capability.
- **"Grid/cloud distributed execution is defining"** — rejected: deployment posture (L2); even classic single-machine engines fit the Type.
- **"Life insurance only"** — rejected: pensions, LTC, P&C pricing/reserving all fit with the same core (L2 segment variants).
- **"ML/AI is defining"** — rejected: only the pricing-segment product leads with it; classic engines fit the Type without it.
- **"Pre-built product libraries are defining"** — rejected: single-product evidence; convenience layer, not structure.
- **"IFRS 17 / LDTI support is defining"** — rejected: regulatory-era dependent; the same product existed before these standards and will outlive them.

## Boundary Findings

- **vs Spreadsheet Application (§03.03)** — historical substrate, not a sibling: actuarial work predates platforms on spreadsheets, and spreadsheets still host models. The structural test: a spreadsheet has no managed model objects, no first-class assumption sets/versions, no managed runs with recorded inputs/outputs, no model-point machinery. If those are removed → spreadsheet-based modeling, not an actuarial modeling platform.
- **vs Financial Modeling Application (§08 sibling)** — gradient, not a wall. Both "build models and project numbers". The distinguishing semantics: actuarial platforms model insurance liabilities/products with actuarial decrements (mortality/lapse), multi-basis valuation, and policy-portfolio data; financial modeling applications model corporate financial statements/valuation for finance teams. Test: replace insurance-product semantics with generic statement/DCF semantics → becomes the other Type. Flag for joint review when Financial Modeling Application is processed.
- **vs Financial Risk Management Platform / Market Risk Platform (§08 siblings)** — adjacent and intertwined: actuarial platforms feed capital and risk numbers (AXIS page explicitly serves risk/capital managers), and vendors ship risk suites around the actuarial core. Structural center differs: liability/product projection vs enterprise/market-risk aggregation and monitoring. Scenario generators sit between the two (sold as companion products). Flag for joint review.
- **vs Regulatory Reporting Platform (§08 sibling)** — capability relationship: vendors ship both (e.g., an IFRS 17 reporting engine alongside an actuarial system). The actuarial platform computes actuarial results; the reporting platform assembles/discloses them. Some products blur this by shipping regulatory-output modules. Flag for joint review.
- **vs Insurance Policy Administration System (§08)** — upstream data relationship, not overlap: the in-force extract consumed by actuarial platforms originates in policy admin; policy admin operates per-policy transactions, not portfolio projection.
- **vs Pension Administration Platform (§23)** — admin = member/benefit records and processes; actuarial modeling = valuation of the pension liability. Actuarial platforms include pension valuation solutions (SLOPE Pension & PRT) but not member administration.
- **vs Pricing/rating execution (Insurance Quote Platform, Underwriting Workbench, §08)** — the actuarial pricing platform *builds* rating plans/risk models; quote/underwriting systems *apply* them per risk. Akur8's Deploy module explicitly bridges toward production rating (product-specific evidence of the handoff).
- **vs Catastrophe Modeling (Moody's RMS-style, §08-adjacent)** — cat models are vendor-supplied hazard/loss models over exposures; actuarial modeling platforms are user-defined business/liability models. They interoperate but are different Types.
- **Internal segment gradient (worth recording)**: "actuarial modeling" spans projection/valuation engines (data object: in-force) and pricing/reserving builders (data object: historical experience/triangles). The L0 was deliberately phrased ("policy/experience datasets... projection/calibration runs") to cover both. If a future review prefers a narrower definition centered on projection, the pricing segment would need its own Type decision.

## Uncertainties

- Milliman MG-ALFA and WTW Unify/ResQ documentation was unreachable; their inclusion as "classic engines with the same core" rests on market standing and the §24 historical check, not on direct evidence. No precise claims made about them.
- Moody's Prophet was not directly evidenced; treated as a market anchor only.
- Whether stochastic scenario generation should sit in L1 or L2 long-term (pricing-reserving variants may never need it) — kept in L1 as it is strongly characteristic of the projection variant, with the job-center variance documented.
- Exact mechanics of assumption-to-model binding differ per product (tables vs sets vs bases); final document describes the conceptual role only.
- The extent to which pricing platforms' "Deploy" handoff to production rating systems is common across the Type is unclear (single-product evidence).

## Final Synthesis

An Actuarial Modeling Platform is the actuary's modeling workbench for insurance business: the user defines explicit models of insurance products/liabilities (or rating/loss behavior), attaches managed, versioned actuarial assumptions, loads structured insurance data (in-force portfolios or experience data), and executes controlled, repeatable runs whose recorded results — projected cash flows, reserves, capital, fitted premiums — are then analyzed (dashboards, drill-down, movement/source-of-earnings), refined, and fed into pricing decisions, financial statements, capital regimes, planning, and regulatory filings. Around this core, mature products add scenario/stress machinery (deterministic and stochastic), asset-side/ALM modeling, multi-basis multi-framework calculation, governance and audit trails, distributed execution, experience studies, and pre-built libraries. Variants differ mainly by job center (valuation/projection vs pricing vs reserving), business line, deployment, and regulatory regime. The Type is bounded from spreadsheets (no managed models/runs), from generic financial modeling (no insurance-liability semantics), from risk platforms (centers on liability models, not enterprise risk aggregation), and from reporting/administration systems (computes actuarial results rather than disclosing them or administering policies).
