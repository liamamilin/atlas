# Research Notes — Portfolio Management System

Cross-references: research/performance-attribution-platform.md §Boundary Findings (flags this leaf: "PMS manages portfolios forward"; boundary cross-check performed and confirmed, see Boundary Findings); research/algorithmic-trading-platform.md §Boundary Findings (strategy-vs-execution-algo distinction, EMS/OMS-adjacent); applications/performance-attribution-platform.md (sibling final doc).

## Research Goal

Establish what a Portfolio Management System (PMS) in the investment-management sense actually is as an Application Type: its core objects, its working loop, its rules, its variants across client tiers (institutional buy-side, hedge funds, asset owners, wealth/advisory), and its boundaries against sibling Types (Investment Management Platform, Performance & Attribution Platform, fund accounting, trading platforms, wealth platforms).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: operator-facing front-office software used by portfolio managers to hold the portfolio book of record, manage portfolios against mandates/models/benchmarks, generate and authorize trades, and monitor positions/exposures/cash — "managing portfolios forward".
- Nearest neighbors: Investment Management Platform (broader lifecycle), Performance & Attribution Platform (backward measurement), fund/investment accounting (books and NAV), Order/Execution Management (order lifecycle), wealth platforms (client-centric suites), retail trading (individuals), robo-advisors (automated consumer product), and — on names alone — Project Portfolio Management (§03.07, unrelated universe).
- Unknowns entering research: is pre-trade compliance part of the defining core or only common? Is the wealth-side rebalancing category the same Type or an adjacent one? How far does the "system" extend into execution (PMS vs OEMS bundling)?

## Research Questions

1. What is the central object — portfolio, account, position, order — and how do they relate?
2. Where does the position/cash book come from: in-system IBOR, custodian feeds, accounting books? How current is it?
3. What does "manage" concretely mean: what loop does a portfolio manager run day to day?
4. How do intended changes (orders, rebalances) flow, and where does the PMS end and order/execution management begin?
5. What role do mandate/rule checks (compliance) play, and at which points in the loop?
6. How do models, benchmarks and targets work — especially on the wealth side (households, sleeves, drift)?
7. Which analytics are embedded (risk, performance, attribution) vs consumed from sibling systems?
8. Who uses the system (roles), and on which surfaces?
9. Which states and lifecycles matter (positions, orders, breaches)?
10. Where are the boundaries with the sibling Types listed above?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different client tiers:

| Product | Vendor | Why selected | Segment |
|---|---|---|---|
| Charles River IMS (Portfolio Management, Compliance, Wealth Portfolio Management) | Charles River Development / State Street | classic institutional buy-side PMS+OEMS suite with unusually detailed public product pages; also documents the wealth/managed-accounts variant from the same vendor | institutional + enterprise wealth |
| Enfusion by Clearwater (+ Clearwater Portfolio & Order Management, IBOR pages) | Clearwater Analytics (Enfusion acquired) | cloud-native, single-database PMS/OEMS for hedge funds/asset managers; philosophy = one live ledger, front to back | hedge funds / asset managers |
| Orion Trading (+ Orion platform pages) | Orion Advisor Solutions | the wealth/RIA "portfolio rebalancing & trading" pattern: custodian-fed accounts, models, household rebalancing, tax-aware trading | wealth / advisory |
| Aladdin | BlackRock | whole-portfolio ecosystem angle; documents the boundary where PMS sits inside a full investment-management platform | institutional (all segments) |
| Axioma Portfolio Optimizer (within SimCorp Axioma Solutions / SimCorp One) | SimCorp (Deutsche Börse Group) | portfolio-construction/optimization specialist angle and the IBOR-centered platform angle | institutional |

## Sources

All fetched 2026-09-06. Evidence tier: official vendor product/solution pages (Tier 2); no client-only help centers were reachable.

- Charles River — Portfolio Management & Risk Analytics: https://www.crd.com/solutions/portfolio-management
- Charles River — Compliance & Regulatory: https://www.crd.com/solutions/compliance/
- Charles River — Wealth Portfolio Management: https://www.crd.com/solutions/wealth-portfolio-management/
- Charles River — home (solution framing): https://www.crd.com/
- Clearwater Analytics — Portfolio & Order Management: https://cwan.com/solutions/portfolio-order-management/
- Clearwater Analytics — Investment Book of Record (IBOR): https://cwan.com/solutions/ibor/
- Clearwater Analytics — Enfusion product page: https://cwan.com/products/enfusion/
- Clearwater Analytics — home: https://cwan.com/ (Enfusion root redirected here)
- Orion Advisor Technology — Trading (rebalancing): https://orion.com/advisor-tech/trading
- Orion Advisor Technology — home: https://orion.com/ (orionadvisortech.com redirected)
- BlackRock — Aladdin: https://www.blackrock.com/aladdin/
- SimCorp — SimCorp One: https://www.simcorp.com/solutions/simcorp-one
- SimCorp — Axioma Solutions: https://www.simcorp.com/solutions/axioma-solutions

## Product Observations

### Charles River IMS (institutional)

Key observations (evidence layer A unless noted):

- Portfolio Management page frames the work as: portfolio analysis ("deep, real-time insights into portfolio composition, risk and exposures"), portfolio construction ("design and optimize portfolios that align with investment objectives"; "optimize portfolios against benchmarks and models"; "build and manage models"; "create and maintain benchmark blends / carve outs"), idea implementation ("create idea lists & park as needed"; "check scenarios against compliance and risk"; "understand cashflow impacts"; "rebalance portfolios"), historical lookback, private-asset portfolio monitoring.
- Explicit loop verbs: analyze positions → run what-if/scenario (order modeling, ex-ante risk on demand, what-if compliance, optimization) → generate orders with top optimizers → "view impact on compliance and risk" → monitor "from trade initiation through settlement".
- Compliance page: rules-based compliance embedded across the investment lifecycle — named checkpoints: pre-trade, in-trade, placement, post-trade, portfolio (batch), as-of portfolio, what-if, future position limits, historical compliance. Centralized rule management (create/edit/test/import/export rules; vendor claims "2,000+ sample rules" — vendor claim), dedicated compliance workspace with dashboards/alerts, audit trail, 100+ compliance reports (vendor claim), and third-party regulatory services integrations.
- Suite framing: compliance page lists what the platform combines — "Portfolio management system, Performance & risk analytics, Order and execution management, IBOR, Post-trade management, Data management".
- Wealth variant (separate page): managed accounts (SMA, UMA, Rep-as-PM programs), "enable discretionary and non-discretionary mandates", "facilitate efficient model delivery and rebalancing", overlay/portfolio-implementation services ("centralize trade generation and overlay coordination", "optimize for tax management at the household-level", "adhere to client- or manager-directed constraints"), personalization ("capture preferences, tax budgets, risk tolerances, and ESG/SRI filters", "customize at the household level"), "monitor and re-optimize portfolios with every update".
- Scale claims (vendor claims, kept out of canonical doc): ~$59T assets managed on the platform; ~300 investment managers trade on it; front office of State Street Alpha.

### Clearwater Analytics — Portfolio & Order Management / IBOR / Enfusion

Key observations (layer A):

- Portfolio & order management page positions the category: "Clearwater brings your PMS, OEMS, analytics, and compliance into one cloud-native platform."
- Portfolio management capabilities: real-time portfolio views ("positions, cash, and exposures across accounts, strategies, and asset classes"), multi-asset-class coverage, integrated risk and performance analytics ("monitor attribution, risk metrics, and benchmarks"), flexible modeling ("scenario analysis, stress tests, and forward-looking simulations"), customer hierarchies and views ("by desk, strategy, client, or vehicle"), historical data warehousing.
- Order management capabilities: order lifecycle management ("define trading strategies, route, manage, and allocate orders with full visibility from intent to execution"), integrated pre-trade compliance ("compliance rules that support regulatory, firm, and client restrictions"), customizable trading blotters ("real-time market data, order status, and exception handling"), trading connectivity, advanced allocation and post-trade matching, audit trails and trade oversight.
- IBOR page: "starts with accurate beginning of day positions and integrates orders, trades, and anticipated cash flows from investor activities and corporate actions to provide portfolio managers with the most accurate view of portfolio positions, exposures, and cash"; trade-date cash, cash ladders; explicit contrast between IBOR (front office) and Accounting Book of Record (ABOR, back office) — and FAQ language about removing the IBOR/ABOR reconciliation gap.
- Enfusion product page (hedge-fund focus): real-time PMS ("live positions, P&L, and analytics in one view — connected directly to execution"); "systematically generate orders from model changes, capital flows, or target exposure adjustments"; native OEMS ("orders flow from PM model directly to the market"; FIX connectivity to 300+ liquidity sources — vendor claim; confirmation/affirmation/break resolution); pre- and post-trade compliance embedded at order creation ("validated against your firm rules, regulatory requirements, and client mandates"; configurable severity — warning/note/hard block — vendor detail); data management (IBOR and ABOR on one database; security master; automated daily reconciliations); risk & analytics (what-if factor decomposition, live Greeks/DV01 — vendor detail; factor model choice).
- Positioning problems it claims to solve: "Before Enfusion" pain points describe the no-PMS state: "P&L, positions, and reporting built manually. No reliable single source of truth"; "No centralized order system… Nothing properly connected end to end."

### Orion Advisor Technology (wealth / RIA side)

Key observations (layer A):

- Trading page: "the rebalancing platform for advisor firms operating at volume — household-level rebalancing, daily tax-loss harvesting, and multi-custodian routing from one workflow."
- FAQ-documented mechanics: household-level rebalancing "manages all of a household's accounts — taxable, IRA, Roth, trust, joint — as a single portfolio"; asset-location optimization; tax-loss harvesting surfaced in the trading workflow with per-client tax sensitivity and wash-sale rules; "sleeves" split an account into sub-accounts "each managed against a different model or strategy"; trade orders flow "directly to participating custodians" (multi-custodian); pre-trade compliance reviews ("a configurable rule set against pending orders before they reach the custodian"); cash monitoring automation; reads risk profiles and compliance rules from sibling Orion products.
- Portfolio Accounting (sibling product, menu text): "Billing, reporting, and performance at scale"; reconciliation claim "99% of the time, brokerage assets are reconciled before the market opens" (vendor claim).
- Platform framing: twelve connected products (CRM, planning, portfolio accounting, trading, compliance, portals) — i.e., portfolio management & trading is the investment slice inside a client-centric wealthtech suite.
- Named competitors in its own FAQ: iRebal, Tamarac Rebalancing — confirming a recognized market category of advisor rebalancing platforms.

### BlackRock Aladdin

Key observations (layer A, marketing-tier):

- Whole-portfolio framing: "a tech platform that unifies the investment management process through a common data language", across public and private markets.
- "The Aladdin platform enables our clients to manage the entire process from building portfolios and managing performance to operations and accounting."
- Product lineup shows the ecosystem: Whole Portfolio, Risk, Accounting, Data Cloud, Sustainability, Copilot; separate Aladdin Wealth offering.
- Award/positioning note: "Best buy-side IBOR platform" (Buy-Side Technology award listing on the page).
- Used here mainly as the boundary anchor: Aladdin is the shape where portfolio management is one function inside a full-lifecycle platform.

### SimCorp (SimCorp One / Axioma)

Key observations (layer A):

- SimCorp One: "every decision — across every asset class — is made using the same live data foundation, end-to-end, from front office to accounting. No waiting for reconciliation or EOD batch"; "See positions, cash, and risk update in real time across every asset class"; "See concentration risk across every strategy as it builds, at every level"; "Answer a regulator's question with the audit trail already in hand"; industries served: asset management, pensions, insurance, central banks, sovereign wealth funds, wealth management, hedge funds.
- Axioma Solutions (specialist layer): portfolio construction via Axioma Portfolio Optimizer ("virtually limitless objective functions, a vast constraint library") alongside risk models and performance attribution — evidence that construction/optimization is its own deep capability that PMS environments consume or embed.

## Cross-product Comparison

| Dimension | Charles River IMS | Clearwater / Enfusion | Orion (wealth) | Aladdin | SimCorp One / Axioma |
|---|---|---|---|---|---|
| Central objects | portfolios/accounts, positions, models, benchmarks, compliance rules, orders | accounts/strategies, positions, cash, orders, rules; single IBOR+ABOR DB | households → accounts → sleeves; models; trade files to custodians | whole portfolio (public+private), positions, risk, accounting | portfolios/strategies, positions, cash, risk; one live data foundation |
| Book of record | IBOR inside suite; front-to-back | IBOR page: BOD positions + orders + anticipated cash flows; Enfusion: one DB with ABOR | custodian-fed, reconciled daily (before market open — vendor claim) | buy-side IBOR (award positioning) | live data foundation front-to-back; "no reconciliation handoff" |
| Management intent | benchmarks, models, benchmark blends, compliance rules (regulatory/firm/client) | firm rules, regulatory requirements, client mandates; target exposure | models per sleeve; risk profiles; compliance policies; tax preferences | whole-portfolio objectives, risk posture | objectives/constraints via optimizer; strategy-level concentration |
| Change-generation | optimizers, rebalance vs benchmark/model, idea lists, ETF baskets | orders from model changes, capital flows, target exposure adjustments | rebalancing (household level), tax-loss harvesting, asset location | building portfolios; platform-managed process | optimization with objective functions + constraints |
| Rule checking | full lifecycle: pre-trade → in-trade → placement → post-trade → portfolio batch → as-of → what-if → future limits → historical | pre-trade compliance at order creation; post-trade compliance | pre-trade reviews on pending orders | risk/compliance embedded platform-wide (less specific publicly) | audit trail; regulator-facing |
| Execution boundary | own OEMS (trading module) inside suite | native OEMS, FIX connectivity, confirm/affirm | trade files routed to custodians (no trading desk) | platform-integrated trading ecosystem | platform + partner ecosystem |
| Embedded analytics | ex-ante risk, scenarios, performance & attribution views | risk & analytics on live positions; factor models | risk intelligence via sibling product | risk engine as flagship | factor risk models, optimizer, attribution (Axioma) |
| Hierarchy of portfolios | accounts, portfolios, multi-portfolio reporting | desk / strategy / client / vehicle views | household → account → sleeve | whole portfolio across entities | strategy levels, total portfolio |
| Segment | institutional + enterprise wealth | hedge funds / asset managers | RIAs / advisor firms | all institutional segments | institutional, all listed segments |

Layer-B commonalities (present across ≥4 of 5): position/cash book kept current (real-time or reconciled); management against explicit intent (models/benchmarks/mandates/rules); a forward loop monitor → generate changes → check → release; order/trade generation as the loop's output; pre-trade-style validation against rules; multi-asset and multi-portfolio scale; audit trails; embedded portfolio analytics (exposure/risk, some performance views); reporting surfaces; role split (PM vs trader vs compliance vs operations).

## Canonical Model

### Level 0 — Defining Invariant (layer C, supported by A/B evidence)

1. **Managed portfolio book of record** — identified portfolios (accounts, funds, strategies, households) holding positions in instruments plus cash, maintained as the system's current record of what is owned (in-system real-time, or fed/reconciled from custodians and accounting).
2. **Defined management intent** — each portfolio is managed against explicit references: targets/model portfolios/benchmarks and/or rule sets (regulatory, firm, and client mandates, restrictions, limits).
3. **Forward-management loop** — the working cycle: monitor the current portfolio (positions, cash, exposures) against the intent → decide and generate the portfolio's changes (orders, rebalances, allocations) → validate them against the intent before they take effect → release them for execution → the book reflects the outcome.

Removal tests:
- Remove #1 → analytics on imported snapshots; not a management system.
- Remove #2 → a position register/blotter with no "toward what"; record-keeping, not management.
- Remove #3 → a static registry or a measurement system; the product stops being a PMS and becomes accounting, performance measurement, or a data platform.

Historical check (older/regional/differently positioned products): 1990s-era standalone PMS (on-prem, batch start-of-day data, separate order desks) still satisfy all three invariants — their books were batch-fed, their intent lived in mandate documents and rule tables, and their loop ran once daily instead of continuously. Real-time IBOR, embedded OEMS, cloud delivery, tax-aware trading, and household modeling are all era/segment implementations, not invariants.

### Level 1 — Common Mature Structure (layer B)

- Order generation and handoff: order lifecycle management, blotters, routing/connectivity to execution venues or custodians, allocations, post-trade matching; many products bundle OEMS with the PMS.
- Pre/post-trade compliance machinery: centralized rule libraries (regulatory/firm/client), checkpoint-based testing (pre-trade, post-trade, portfolio-level, as-of, what-if), alerting, breach workspaces.
- Portfolio analytics: exposure/characteristics, risk measures, factor views; performance and attribution views often embedded or pulled from sibling systems.
- What-if / scenario analysis and order modeling before commitment; portfolio construction/optimization tooling (sometimes a specialist engine plugged in).
- Cash management: trade-date cash, anticipated flows, cash ladders/liquidity monitoring.
- Portfolio hierarchies: accounts nested in strategies/desks/clients/vehicles; on the wealth side, households containing accounts containing model sleeves.
- Multi-asset-class coverage; multi-currency.
- Historical lookback, audit trails, timestamped activity logs.
- Integration fabric: market data/security master, accounting books (IBOR↔ABOR reconciliation), custodians/prime brokers, data vendors.
- Roles and scoped access: portfolio manager, trader, compliance officer, operations/middle office; differentiated surfaces.
- Reporting/dashboards for internal and external stakeholders.

### Level 2 — Variant / Optional Structure (layer A/B)

- Segment shapes: institutional buy-side PMS/OEMS (asset managers, hedge funds); asset-owner/insurer portfolios inside suites; wealth/advisory portfolio management (custodian-fed household accounts, models/UMA/SMA sleeves, drift-based rebalancing, tax-aware trading); cloud-native single-ledger funds.
- IBOR stance: real-time in-system book vs daily custodian-feed reconciliation vs collapsed IBOR+ABOR single database.
- Execution depth: full embedded OEMS/EMS vs trade-file handoff to custodians vs no execution at all (instructions only).
- Construction depth: embedded optimizers vs third-party optimizer integration vs rule/drift-based rebalancing only.
- Tax awareness: per-household tax budgets, loss harvesting, asset location (wealth segments; region-dependent).
- Private-markets handling: monitoring/blending vs full order flow (illiquid assets rarely run an order lifecycle).
- Deployment and packaging: standalone PMS, PMS+OEMS bundle, slice inside an investment-management platform, module inside a wealthtech suite.

### Level 3 — Vendor-specific Structure (stays in these notes)

- Charles River: named compliance checkpoint set (pre-trade/in-trade/placement/post-trade/portfolio batch/as-of/what-if/future position limits/historical); vendor-claimed 2,000+ sample rules; 100+ compliance reports; ETF basket workflow; "Idea lists & park" concept; compliance services (rule writing, law cards); part of State Street Alpha.
- Clearwater/Enfusion: single-database IBOR+ABOR; security master maintenance by vendor (vendor-claimed 4M+ instruments); 300+ FIX liquidity venues (vendor claim); configurable rule severity (warning/note/hard block); proprietary and third-party factor models ("GR8"); Beacon (risk) as sibling product.
- Orion: sleeve model per account; wash-sale-rule handling in workflow; multi-custodian simultaneous trade routing; Eclipse trading platform training series; iRebal/Tamarac named as category peers.
- Aladdin: whole-portfolio "common data language" positioning; Aladdin Wealth; Aladdin Studio API layer; Copilot.
- SimCorp: Axioma optimizer "limitless objective functions" constraint library; SimCorp One total-portfolio live-data positioning.
- Vendor scale/claims ($59T, 1,000+ funds, 99% reconciliation, 90% automation): marketing claims, not used canonically.

## Boundary Findings

1. **vs Investment Management Platform** (broader Type): IM platforms span the full lifecycle — front office (PMS function), middle office, accounting, operations, reporting; the PMS is the portfolio-management slice. Test: remove accounting/settlement/middle-office from Charles River IMS or SimCorp One and a PMS remains; a "platform" without positions/order/rebalancing loop would not be a PMS. Aladdin, Clearwater, SimCorp One all evidence the embedding pattern. Boundary held. (No separate §08 "Investment Management Platform" doc exists yet — when that leaf is processed, the whole↔slice relationship should be stated mirror-side.)
2. **vs Performance & Attribution Platform** (already processed): direction of time. P&A measures and explains realized results backward (returns vs reference → decomposed effects); PMS manages forward (intent → changes → checked → executed). PMS products embed performance/attribution views (Charles River lists attribution; Clearwater "monitor attribution") — the difference is center of gravity, not absence. Removal tests hold both ways: strip attribution from a PMS and it remains one; strip the forward loop from a P&A platform and it remains one. Cross-check of the flag recorded in research/performance-attribution-platform.md: **confirmed**.
3. **vs trading OMS/EMS**: order lifecycle is a first-class L1 capability of modern PMS, and the market norm is PMS+OEMS bundling (Charles River, Enfusion, Clearwater explicitly). The distinguishing center remains the portfolio and its intent, not the order: a PMS without execution connectivity is still a PMS (Orion routes files; asset owners instruct managers), while an OMS without a portfolio book of record is an execution tool. The directory has no trading-OMS leaf (§05.07 "Order Management System / OMS" is the commerce/sales-order universe); recorded as a taxonomy note, not a defect.
4. **vs Wealth Management Platform / Financial Advisor Platform** (both pending leaves): the wealth-side "portfolio rebalancing & trading" category (Orion Trading, Tamarac/iRebal, Black Diamond) satisfies this Type's L0 — portfolios (households/accounts/sleeves), intent (models, risk profiles, tax preferences), forward loop (rebalance → pre-trade review → custodian delivery). It is usually sold as the investment slice inside a client-centric suite (CRM/planning/billing/portals). Recorded so the future wealth-platform passes treat the rebalancing engine as a PMS-shaped slice, not a separate Type.
5. **vs Project Portfolio Management Application** (§03.07): total namesake collision. "Portfolio" = collection of projects/programs there; collection of investments here. No shared objects, users, or workflows. Recommend the §03.07 pass state the mirror-side distinction.
6. **vs Retail Trading Platform / Brokerage / Algorithmic Trading Platform** (one processed): the user is an individual or a strategy runtime acting on market opportunities, not an operator managing a portfolio of mandates; no managed population of portfolios, no model/mandate intent structure. Algorithmic-trading research already recorded the mirror side (strategy runtime vs human decision); a PMS keeps the human/organizational decision loop over a book.
7. **vs Robo-advisor** (pending leaf): a robo-advisor productizes portfolio construction for consumers; a PMS is the operator's tool for human-run management. Structural similarity of the rebalancing engine exists (drift-based, model-driven); the user, the object population (thousands of client portfolios vs the firm's managed portfolios), and the decision authority differ.
8. **vs fund/investment accounting** (pending leaves): accounting produces the books of record (ABOR, NAV) that the PMS either consumes or reconciles against; Clearwater's IBOR/ABOR pages document the two-book structure explicitly. A PMS may hold an IBOR; it does not become an accounting system by doing so.
9. **vs Private Market Investment Platform / Deal Management for PE-VC** (pending leaves): deal-centric lifecycle (sourcing → close → hold → exit) vs continuous position management; private-markets *monitoring* inside a PMS (Charles River private markets page, eFront) is a variant extension where order flow is mostly absent.
10. **Rejected finding**: "PMS = portfolio analytics/monitoring dashboard" — rejected: analytics without the intent structure and change loop is a reporting surface (or the P&A/BI Types). Also rejected: "PMS requires real-time IBOR" — rejected by the historical check and by the Orion custodian-fed pattern.

## Uncertainties

- No Tier-1 help-center/user-guide documentation was reachable; all evidence is official product/solution pages. Operational fine structure (exact order state machines, exact rule DSLs, exact rebalancing cadences) is therefore not asserted anywhere.
- Aladdin's public pages are marketing-tier; its portfolio-management workflow specifics are inferred from platform framing, not product documentation. Aladdin is used for boundary anchoring, not for capability claims.
- The asset-owner PMS shape (pensions/insurers managing mandates in suites) is evidenced indirectly (SimCorp industry pages, Charles River asset-owner pages) rather than through a dedicated product page.
- Precise market-share/category boundaries inside wealthtech (PMS vs "portfolio accounting vs rebalancing") vary by vendor naming; treated as one slice pattern rather than resolved into sub-Types.
- Whether the directory intends "Investment Management Platform" to exist as a separate canonical doc is a taxonomy question; evidence supports whole↔slice rather than two peer Types.

## Final Synthesis

A Portfolio Management System is the investment industry's forward-management application: it keeps the current book of portfolios (positions and cash), holds each portfolio's intent (models/benchmarks/mandate rules), and runs the loop by which the portfolio moves toward or stays within that intent — monitor, decide, generate changes, check them against the rules, release them, and update the book. Everything else commonly bundled — OEMS, compliance engines, optimizers, risk and performance analytics, tax-aware trading, real-time IBOR, custodian connectivity — is mature structure around that loop. The Type spans institutional and wealth segments with the same core; what varies is where the book comes from, how changes reach the market, and how intent is expressed.
