# Research Notes — Investment Management Platform

Cross-references (sibling passes whose flags this pass discharges):
- research/portfolio-management-system.md §Boundary Findings #1 — "whole↔slice relationship confirmed from the PMS side (Aladdin, SimCorp One, Clearwater all embed PMS as front-office slice); when the Investment Management Platform leaf is processed, the whole↔slice relationship should be stated mirror-side." → discharged in Boundary Findings #1.
- research/performance-attribution-platform.md §Boundary Findings — "IM platforms span the full lifecycle and embed P&A as a module (Axioma in SimCorp One, performance inside Aladdin) … flagged for boundary cross-check when those leaves are processed." → discharged in Boundary Findings #2.
- research/portfolio-management-system.md §Boundary Findings #2 (note for unprocessed siblings) — advisor rebalancing category is the PMS-shaped slice of wealthtech suites; recorded here as context for Boundary Findings #5.

## Research Goal

Establish what an Investment Management Platform (IMP) is as an Application Type in the §08 investment cluster: what the "platform" consists of, what holds it together beyond a bundle of tools, who operates it, what the working loop is, and where its boundaries lie against the many sibling Types (Portfolio Management System, Performance & Attribution Platform, fund administration/accounting, risk platforms, wealth platforms, trading platforms, research/data terminals).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the institutional buy-side investment organization's end-to-end operating platform — one shared record of the firm's investments plus the full lifecycle from portfolio decision through trading, compliance, settlement, accounting, and reporting. The "platform" quality is the unified record and connected lifecycle, not feature count.
- Nearest neighbors: Portfolio Management System (front-office slice), Performance & Attribution Platform (measurement slice), Fund Administration / Investment Fund Accounting (official books + investor register), Financial Risk Management Platform (risk module), Wealth Management Platform / Financial Advisor Platform (client-centric suites), trading platforms (execution), Investment Research / Market Data (inputs), ERP/GL (corporate ledger).
- Unknowns entering research: is the unified book of record truly the platform's defining structure or just modern marketing? Do all segments (hedge funds, asset owners, insurers) share one structure? Where exactly does the platform end and the GL / custodian / fund administrator begin?

## Research Questions

1. What do vendors themselves claim the platform is — and is "front-to-back" the market's own framing?
2. What is the shared record: one database, books of record (IBOR/ABOR/PBOR), or integration fabric?
3. Which lifecycle stages does the platform carry: front (decision/execution), middle (control), back (books/reporting)?
4. Who operates it (roles), and how do role surfaces differ?
5. What is the daily working loop from data in to reports out?
6. Which rules govern the flow (compliance checkpoints, reconciliation, audit, permissions)?
7. How do segments differ (asset manager vs asset owner/insurer vs hedge fund)?
8. Where do PMS, P&A, risk, accounting sit: inside as modules, or alongside as siblings?
9. What are the boundaries with each sibling Type — with removal tests?
10. Would older/regional/differently positioned products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different client tiers:

| Product | Vendor | Why selected | Segment / philosophy |
|---|---|---|---|
| Aladdin (+ Aladdin Accounting) | BlackRock | the risk-led mega-platform; "common data language" positioning; explicit IBOR/ABOR/PBOR unification in FAQ | institutional all segments (asset managers, insurers, pensions, corporates, banks); also wealth extension |
| SimCorp One | SimCorp (Deutsche Börse Group) | European front-to-back suite pole; "one live data foundation, front office to accounting" | asset managers, pensions, insurance, central banks, SWFs, hedge funds |
| Clearwater Analytics | Clearwater Analytics | cloud-native SaaS pole that literally self-labels "Unified Front-to-Back Investment Management Platform"; accounting-led heritage; strongest public lifecycle documentation | asset managers, insurers, pensions/endowments, corporates, banks, public sector, energy |
| Charles River IMS | Charles River Development / State Street | front-office-led IMS pole; "enterprise investment management platform"; middle office + accounting/IBOR modules; State Street Alpha services pairing | institutional investors, asset owners, insurers, wealth managers |
| Enfusion (by Clearwater) | Clearwater Analytics (acquired) | hedge-fund-native front-to-back pole; single-database IBOR+ABOR; "from portfolio decision to settled trade" | hedge funds and asset managers, from first build to re-platform |

Note: Clearwater and Enfusion share an owner but are distinct product lines with distinct philosophies (SaaS accounting-led operations platform vs hedge-fund single-database PMS/OEMS); the PMS pass used the same pairing.

## Sources

All fetched 2026-09-07. Evidence tier: official vendor product/solution pages and FAQs (Tier 2). No client-only help centers / user guides were reachable for any sampled product (enterprise-gated).

- BlackRock — Aladdin home: https://www.blackrock.com/aladdin/
- BlackRock — Aladdin Accounting (incl. FAQ): https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting
- SimCorp — SimCorp One: https://www.simcorp.com/solutions/simcorp-one
- SimCorp — Asset & portfolio management industry page: https://www.simcorp.com/your-industry/asset-management
- Clearwater Analytics — home ("Unified Front-to-Back Investment Management Platform"): https://cwan.com/
- Clearwater Analytics — Investment lifecycle (front/middle/back office map): https://cwan.com/platform/investment-lifecycle/
- Clearwater Analytics — Investment accounting & reporting: https://cwan.com/solutions/investment-accounting-reporting/
- Clearwater Analytics — Enfusion product page: https://cwan.com/products/enfusion/
- Charles River — home: https://www.crd.com/
- Charles River — Charles River IMS overview: https://www.crd.com/solutions/charles-river-ims/

## Product Observations

### BlackRock Aladdin (+ Aladdin Accounting)

Key observations (layer A; marketing-tier + FAQ):

- Home: "Aladdin® is a tech platform that unifies the investment management process through a common data language. With a view of your whole portfolio—across public & private markets—it enables scale, provides insights, and supports business transformation."
- "The Aladdin® platform enables our clients to manage the entire process from building portfolios and managing performance to operations and accounting—helping them build a foundation for a streamlined and scalable operating model."
- Product lineup: Whole Portfolio, Risk, Accounting, Data Cloud, Sustainability, Climate, Copilot, Aladdin Studio (API layer), Aladdin Provider (asset servicers), Aladdin Wealth; eFront (private markets platform) and Preqin (private-markets data) as sibling platforms.
- Ecosystem: "The world's top asset servicers, broker dealers, trading platforms, and data providers are natively integrated into the Aladdin® platform."
- Institutions served: asset managers, asset servicers, banks & brokers, corporates, insurers, pension funds, private markets, wealth managers.
- Award line: "Best buy-side IBOR (investment book of record) platform" (Buy-Side Technology 2022, on page).
- Aladdin Accounting page: "Powerful investment accounting and performance solutions, integrated in a unified tech ecosystem … across the whole portfolio—enabling asset managers and asset owners, including insurers and pensions, to scale and optimize investment and accounting lifecycles."
- Aladdin Accounting FAQ (structural gold): "Aladdin Accounting unifies the Investment Book of Record (IBOR), Accounting Book of Record (ABOR) and Performance Book of Record (PBOR) into a single, integrated platform. This creates a single source and view across investment, accounting, and performance data. With a unified structure, front-, middle-, and back-office teams can align workflows, reduce reconciliations, and deliver consistent, high-quality outputs with confidence."
- Accounting capabilities: multi-basis accounting (GAAP, IFRS, STAT, TAX) "with journal entries to feed a general ledger & regulatory-compliant reporting"; configurable chart of accounts; locked-period official returns for SMAs; fund NAV & performance oversight (reconcile fund-administrator data); composite administration supporting GIPS; "investment accounting technology, as software or a service" (in-house or outsourced).
- Users named: asset managers and asset owners including insurers and pensions.

### SimCorp One

Key observations (layer A):

- "With SimCorp One, every decision - across every asset class - is made using the same live data foundation, end-to-end, from front office to accounting. No waiting for reconciliation or EOD batch."
- "Changes made anywhere in the system are instantly reflected across your entire operation"; "All teams working from the same live data, front-to-back."
- Speed/accuracy/simplicity framing: "Decide on live positions, not this morning's start-of-day numbers"; "Move from data to decision without a reconciliation handoff in between"; "Catch a discrepancy before it reaches a client"; "Answer a regulator's question with the audit trail already in hand"; "Add a strategy without adding a system."
- Industries: asset management, pensions, insurance, central banks, sovereign wealth funds, wealth management, hedge funds.
- Asset-management industry page: "From portfolio construction and risk management to trading, performance measurement, operations, and accounting, the full investment lifecycle runs on one platform, enabling every team to work from the same trusted data."
- "A unified data layer connects every asset class and every stage of the investment lifecycle, so you get one real-time total portfolio view."
- "Axioma's optimization and risk models run inside SimCorp One's award-winning IBOR, covering every asset type, public, private, cash, and derivatives."
- Client cases: AXA IM replaced "several customized and best of breed tools" with "one integrated front to back platform"; PineStone: "unique, consolidated front-to-back approach"; ADIA data-foundation case.
- Scale claims (vendor, kept out of canonical doc): "more than half of the world's top 100 financial companies".

### Clearwater Analytics

Key observations (layer A; richest lifecycle documentation in sample):

- Page title: "Unified Front-to-Back Investment Management Platform"; hero: "one dataset. total clarity, front to back." / "The investment management platform for the entire lifecycle."
- "Clearwater unites investment data and workflows across the entire lifecycle, enabling teams to make better decisions, manage risk, and report with confidence."
- Explicit lifecycle map (three stages over a data layer):
  - Data Management: Security Master, Pricing, Market, Custodian, Index; Single Data Platform (Data Integration, Aggregation, Consolidation, Distribution).
  - Front office: Strategic Asset Allocation, Portfolio Management, Order & Execution Management, Portfolio Rebalancing, Pre-Trade Risk, IBOR, Pre-Trade Compliance.
  - Middle office: Trade Lifecycle, Post-Trade Compliance, Valuations & Pricing, Post-Trade Risk, Performance & Attribution.
  - Back office: Multi-Basis ABOR (GAAP, IFRS, statutory, management views in one system), Reconciliation, Regulatory Reporting, Client Reporting.
- "No more data gaps or disconnected workflows. Unify your front, middle, and back office on the world's leading investment platform built for scale."
- Accounting page: "daily, validated, multi-basis, multi-currency investment accounting and reporting across public and private assets"; Automated ABOR "aligned to GAAP, STAT, IFRS, tax, and other local accounting basis"; multi-basis logic engine (simultaneous calculations across books and currencies); validated data foundation (daily automated feeds from custodians, managers, internal systems with reconciliation and exception handling); GL integration ("journal-ready outputs tailored to your ERP or GL"); regulatory reporting (NAIC, Solvency II, other frameworks); stakeholder reporting; governance (roles, approval workflows, versioning, audit logs).
- Pain-point framing (the anti-pattern the Type sells against): "Data is fragmented across custodians, managers, and internal systems"; "Disconnected ABOR and IBOR systems create conflicting views of the portfolio"; "Each accounting basis requires separate, duplicative workflows."
- Products around the platform: Beacon (cross-asset trading and risk management), Enfusion (unified portfolio management and order execution), Compass, Investment Intelligence (data management).
- Industries: asset managers, energy, hedge funds, insurance; banks, corporates, pensions & endowments, public sector. Roles: finance & accounting, investment, operations, risk, technology.
- Scale claims (vendor): $10T assets, 2,400 clients, 1,000+ AI agents, 95% reporting-time reduction.

### Charles River IMS (State Street)

Key observations (layer A):

- Home: "Investment and wealth managers, asset owners and insurers in ~30 countries rely on Charles River IMS … Together with State Street's middle and back office services, Charles River's cloud-based front office technology forms the foundation of State Street Alpha®."
- IMS overview: "Streamline investment workflows across asset classes with Charles River IMS, the enterprise investment management platform that scales."
- "Charles River streamlines the entire investment process on one platform – front to back office, all global asset class support, and across public and private markets. Deliver investment strategies in any form, including mutual funds, UCITS, separate account, alternatives, and wealth management product lines." "One platform. One provider."
- Capability set ("Streamline the full investment lifecycle from front to back"): PM & Risk (portfolio management/construction & risk analytics, what-if simulations), OEMS (all-in-one order and execution management), Compliance (centralized rules across regulatory/firm/client; evaluation across "what if, pre-trade, intra-trade, post-execution, and batch" workflows), Post-Trade Operations (connectivity to automate post-trade processing; reduce settlement risk), Investment Accounting & IBOR ("Consolidate back office feeds and validate data via reconciliations … Real-time cash & positions throughout the investment lifecycle"), Data Management (EDM), Wealth Management (SMA/UMA/Rep-as-PM programs), Private Markets ("Efficiently manage deals and portfolios for private assets").
- Users: "portfolio managers, analysts, traders, operations, and leadership."
- Operating-model evidence: "A top global asset manager centralized their entire investment process on Charles River, retiring & decommissioning 27 legacy systems."
- Partner ecosystem supplies analytics/performance/data: MSCI, Axioma (SimCorp), FactSet, RIMES, Opturo (ex-post performance & attribution, GIPS composites), Jacobi (model portfolio construction), Snowflake/Microsoft (technology).
- State Street Alpha: "Supplement Charles River technology with the service offerings of State Street Alpha … a rich array of front, middle and back office services."
- Scale claims (vendor): $59T assets, 55 of 100 largest investment managers, ~300 clients in ~30 countries.

### Enfusion (by Clearwater)

Key observations (layer A):

- "Stop managing systems. Start managing capital. … Enfusion gives you one front-to-back platform." Trusted by "over 1,000 hedge funds and asset managers … in 30 countries" (vendor claims).
- Problem framing (the no-platform state): "P&L, positions, and reporting built manually. No reliable single source of truth. Everything downstream depends on someone getting it right each morning." / "No centralized order system … Nothing properly connected end to end."
- "Enfusion gives every team — PM, trader, back office, and fund admin — a live, unified view of positions, P&L, and cash. One database. No manual assembly. No conflicting versions of the same number."
- "Enfusion connects the full execution workflow in one system — from portfolio decision to settled trade, with pre-trade compliance checks running inline at the point of order. Every trade is captured, checked, and fully auditable."
- Capabilities: real-time PMS (live positions/P&L/analytics; order generation from model changes, capital flows, target exposure adjustments); native OEMS (orders flow from PM model to market; FIX connectivity to 300+ liquidity sources — vendor claim; confirmation/affirmation/break resolution); pre- & post-trade compliance embedded at order creation (firm/regulatory/client rules; configurable severity — warning/note/hard block — vendor detail); data management (IBOR and ABOR on one single database; security master maintained by vendor — 4M+ instruments vendor claim; automated daily reconciliations, settlements, corporate actions, financing, cash; pricing arbitration across sources); risk & analytics (live Greeks/DV01, what-if scenarios, factor exposure live, post-trade factor attribution; factor model choice: proprietary GR8, third parties such as Axioma, or client's own).
- Client quotes: "support from trade execution to operational and accounting" (Sigmoid CFO); "integrated general ledger for shadow accounting" (Livello); "Portfolio managers, traders, and back office teams all use the same platform and data set" (Sparta).

## Cross-product Comparison

| Dimension | Aladdin | SimCorp One | Clearwater | Charles River IMS | Enfusion |
|---|---|---|---|---|---|
| Self-label | platform unifying "the investment management process" via "common data language" | "same live data foundation, end-to-end, from front office to accounting" | "Unified Front-to-Back Investment Management Platform" / "platform for the entire lifecycle" | "enterprise investment management platform that scales"; "full investment lifecycle from front to back" | "one front-to-back platform" |
| Shared record | IBOR + ABOR + PBOR unified in one platform (FAQ) | one live data foundation; "no reconciliation handoff" | one dataset front to back; IBOR + multi-basis ABOR | IBOR + accounting module; back-office feeds consolidated & reconciled | IBOR + ABOR + security master on one single database |
| Lifecycle span | building portfolios → performance → operations → accounting | construction → risk → trading → performance → operations → accounting | front (SAA, PM, OEM, rebalancing, pre-trade risk/compliance, IBOR) → middle (trade lifecycle, post-trade compliance, valuations, post-trade risk, performance & attribution) → back (multi-basis ABOR, reconciliation, regulatory reporting, client reporting) | PM & risk → OEMS → compliance → post-trade → accounting & IBOR → data (+ wealth, private markets) | portfolio decision → order → execution → compliance → settlement → accounting |
| Control layer | risk engine as flagship; compliance embedded platform-wide | concentration risk "at every level"; audit trail for regulators | pre-/post-trade compliance; post-trade risk | compliance checkpoints: what-if, pre-trade, intra-trade, post-execution, batch | compliance inline at order creation; severity levels |
| Books & accounting | multi-basis accounting (GAAP/IFRS/STAT/TAX), journal entries to GL, CoA mapping, official returns, GIPS composites | accounting on the same platform ("front office to accounting") | multi-basis ABOR, reconciliation, GL-ready journals, regulatory reporting (NAIC, Solvency II) | Investment Accounting & IBOR module; reconciliations | ABOR + integrated GL for shadow accounting |
| Analytics posture | risk-led (Risk, Whole Portfolio) | Axioma optimizer/risk models inside the IBOR | risk & performance solution line; Beacon for trading risk | risk analytics native + partner analytics (MSCI, Axioma, Opturo) | live factor risk, Greeks/DV01, attribution native |
| Execution | ecosystem-integrated trading platforms | trading on platform | order & execution management stage | award-winning OEMS | native OEMS, FIX to 300+ venues (vendor claim) |
| Services posture | "software or a service" | platform + partner ecosystem | SaaS; managed services posture | front-office tech + State Street middle/back-office services (Alpha) | platform + support; lean-ops positioning |
| Segments | asset managers, insurers, pensions, corporates, banks, wealth | asset managers, pensions, insurance, central banks, SWFs, hedge funds | asset managers, insurers, pensions/endowments, corporates, banks, public sector, energy | institutional investors, asset owners, insurers, wealth managers | hedge funds, asset managers (long/short, macro, multi-strategy, credit) |
| Record currency | "real-time" positioning (marketing) | real-time live data foundation | daily validated accounting + live front office | real-time cash & positions | live/real-time single database |

Layer-B commonalities (present across all 5): (1) a shared investment record presented as the platform's foundation ("one database/data foundation/dataset/common data language"); (2) explicit front-to-back lifecycle span from portfolio decision to accounting/reporting; (3) portfolio management + order/trade handling as the front-office core; (4) compliance machinery spanning pre-trade and post-trade; (5) investment accounting with multi-basis outputs and GL handoff; (6) reconciliation as the standing control activity; (7) multi-asset, multi-currency, public+private coverage; (8) role-differentiated operation (PM/trader/compliance/operations/accounting); (9) audit trails and regulator-facing posture; (10) reporting outward (clients, boards, regulators); (11) data management layer (security master, pricing, custodian feeds); (12) integration fabric to custodians, brokers, data vendors, GL/ERP.

## Canonical Model

### Level 0 — Defining Invariant (layer C, supported by A/B evidence)

1. **The firm's unified investment record** — one governed book of record for the investment organization's holdings (positions, transactions, cash, instruments) from which every function works, replacing per-function books kept separately. In mature products this is expressed as unified books of record (investment book of record, accounting book of record, often a performance book) on one data foundation; the invariant is the single shared record, not any specific book taxonomy or real-time currency.
2. **The connected front-to-back investment lifecycle** — the platform carries the investment lifecycle end to end as connected workflows on that record: investment decision-making (portfolio analysis/construction/rebalancing), order and trade handling, compliance and risk control, settlement and post-trade operations, investment accounting (books, NAV, multi-basis results), and reporting outward. Both ends must be present and connected: remove the back-office leg (operations/accounting/reporting) and a Portfolio Management System remains; remove the front-office leg (decision/execution) and a fund-administration/investment-accounting system remains; disconnect the record into per-function books and the result is the bundle of point tools this Type exists to replace.

Removal tests:
- Remove #1 → a stack of disconnected tools (PMS + separate accounting + separate reporting) with reconciliation between them — the "siloed workflows" state every sampled vendor explicitly sells against; not a platform.
- Remove #2's back-office leg → a PMS (front-office slice).
- Remove #2's front-office leg → fund administration / investment accounting (books without the investment process).
- Shrink the operator to a single function or single portfolio → a workbench tool, not an organizational platform.

Historical / market-sample check (layer C): 1990s-era integrated front-to-back systems (on-prem, end-of-day batch, integrated database serving front and back office) satisfy both invariants — their record was batch-currency and their lifecycle ran daily rather than continuously. Asset-owner installations (pensions/insurers running their portfolios on the same structure) satisfy both. Real-time IBOR, cloud delivery, AI agents, three-book taxonomies, and embedded OEMS are era/segment implementations, not invariants. The definition survives the check.

### Level 1 — Common Mature Structure (layer B)

- Portfolio & order management slice: portfolio analysis/construction, models/benchmarks, rebalancing, order generation, blotters, execution connectivity, allocations (the PMS/OEMS capability set, embedded).
- Compliance machinery: centralized rule libraries (regulatory, firm, client mandates); checkpoint-based evaluation (pre-trade, intra-trade, post-trade, portfolio batch, what-if); exception/breach workflows; audit trails.
- Risk & performance analytics: ex-ante risk, scenario/stress testing, factor models; performance measurement and attribution — embedded natively, or supplied by partner engines integrated into the platform.
- Investment accounting: multi-basis books (GAAP/IFRS/statutory/tax), valuations/pricing, corporate actions, NAV and official returns, journal-ready output to the corporate GL, reconciliation of books and against custodians.
- Data management layer: security master, pricing/market/custodian/index data integration, consolidation and distribution — the "golden source" feeding every stage.
- Trade lifecycle / post-trade operations: confirmations/affirmations, settlement, breaks, custody/prime-broker connectivity.
- Reporting: client reporting, board/stakeholder reporting, regulatory reporting (framework templates), drill-down/audit-ready outputs.
- Multi-asset, multi-currency, multi-entity coverage; public and private assets side by side.
- Roles and scoped access: portfolio manager/analyst, trader, compliance officer, operations/middle office, fund/investment accountant, finance leadership, technology administrators; approval workflows, versioning, audit logs.
- Integration fabric and APIs; partner ecosystems for analytics/data; AI assistance embedded in workflows (era-typical).

### Level 2 — Variant / Optional Structure (layer A/B)

- Segment shapes: asset-manager suite; asset-owner/insurer total-portfolio operation; hedge-fund front-to-back (single-database, launch-to-scale); corporate treasury and energy/commodities books (one sampled platform).
- Operator poles: software-only vs platform-plus-outsourced-services (middle/back-office services wrapped around the technology).
- Book architecture: unified single-database IBOR+ABOR vs IBOR and ABOR maintained as distinct books with reconciliation vs three-book (investment/accounting/performance) unification.
- Record currency: live/real-time foundation vs daily validated batch accounting alongside live front office.
- Depth poles: risk-led, accounting-led, front-office-led, suite-led, fund-native (see comparison table).
- Private-markets handling: public+private side by side vs dedicated private-markets platform paired alongside; deal/portfolio management for private assets as extension.
- Wealth extension: platform-derived wealth variants (risk/model/personalization machinery handed to wealth managers).
- Deployment: cloud SaaS (dominant in current sample) vs hosted/on-prem heritage.

### Level 3 — Vendor-specific Structure (stays in these notes)

- Aladdin: "common data language" and "whole portfolio" positioning; Whole Portfolio/Risk/Accounting/Data Cloud/Sustainability/Climate/Copilot lineup; Aladdin Studio (API), Aladdin Provider (asset servicers), Aladdin Wealth; eFront + Preqin private-markets pairing; 25-years/600-accountants accounting claims; award lines ("Best buy-side IBOR platform").
- SimCorp: Axioma optimizer/risk models "inside SimCorp One's IBOR"; Domos/support portals; "more than half of the world's top 100 financial companies" claim; AXA IM/ADIA/PineStone case narratives.
- Clearwater: Beacon (trading risk), Compass, Investment Intelligence branding; 1,000+ AI agents / $10T / 2,400 clients / 95% reporting-time claims; NAIC/Solvency II template emphasis; Research Desk.
- Charles River: named compliance checkpoint set (what-if/pre-trade/intra-trade/post-execution/batch); State Street Alpha services pairing; "27 legacy systems retired" case; partner roster (MSCI, Axioma, FactSet, RIMES, Opturo, Jacobi); $59T/55-of-100 claims.
- Enfusion: 300+ FIX liquidity venues, 4M+ instrument security master, GR8 proprietary factor model, severity-level compliance (warning/note/hard block), pricing arbitration engine, 90% automation / 65% cost-reduction claims.

## Vendor-specific Findings

- The three-book taxonomy (IBOR/ABOR/PBOR) is currently explicit only in Aladdin's FAQ; Clearwater/Enfusion document IBOR+ABOR; SimCorp speaks of one data foundation without book names. Treat the named-book taxonomy as a common implementation vocabulary, not the invariant (the invariant is the unified record).
- The "platform + outsourced middle/back-office services" operating model is explicit at Charles River/State Street Alpha and Aladdin ("software or a service"); others sell software-first. Delivery variant, not structure.
- Inline compliance severity configuration (warning/note/hard block) is currently Enfusion-documented; other vendors describe checkpoints without publishing severity mechanics — product-specific detail.
- Partner-supplied performance/attribution (Opturo inside Charles River's ecosystem) vs native attribution (Enfusion, Clearwater) — both patterns exist; analytics sourcing is a variant.

## Rejected Findings

- "Investment Management Platform = any software an investment firm uses" — rejected: the sampled vendors converge on a specific structure (unified record + front-to-back lifecycle); research terminals, CRM, HR tools at the same firm are not the platform.
- "IMP = PMS with more features" — rejected: the difference is structural (shared record spanning books + connected back-office leg), not additive; removal tests separate them cleanly.
- "IMP requires real-time data" — rejected by the historical check (batch-era integrated systems fit) and by Clearwater's own daily-validated accounting posture alongside live front office.
- "IMP requires embedded OEMS/execution connectivity" — rejected: asset-owner and services-wrapped deployments operate with instruction handoffs; execution depth is a variant.
- "IMP = Aladdin" (or any single product) — rejected: five products with five different depth poles satisfy the same structure.
- "The platform replaces the corporate GL/ERP" — rejected: sampled products produce journal-ready output to the GL; the corporate ledger remains outside.
- "IMP includes the investor register / fund-administration machinery" — rejected on current evidence: none of the sampled platforms centers investor capital accounts, subscription/dealing machinery, or LP portals; that is the fund-administration sibling's structure.

## Boundary Findings

1. **vs Portfolio Management System (§08 sibling — mirror side of the PMS pass flag; DISCHARGED)**: the PMS is the front-office slice of this Type. The PMS pass already confirmed the embedding pattern (Aladdin, SimCorp One, Clearwater all embed PMS as front-office slice); this pass confirms the mirror: every sampled platform carries the PMS loop (book + intent + forward management) inside a larger span that adds middle-office control, settlement, accounting books, and reporting on the same record. Test: remove operations/accounting/reporting from any sampled platform → a PMS remains; a platform without the PMS loop would not be an investment management platform. Boundary held; both docs state the whole↔slice relationship.
2. **vs Performance & Attribution Platform (§08 sibling — mirror side of the P&A pass flag; DISCHARGED)**: P&A is the measurement/explanation slice. Clearwater's lifecycle map lists Performance & Attribution as a middle-office stage; Aladdin unifies a Performance Book of Record; SimCorp runs performance measurement on the platform; Charles River supplies it via partner (Opturo). P&A also sells standalone. Gradient, not a wall — same vendors on both sides. Boundary held on center of gravity.
3. **vs Fund Administration Platform / Investment Fund Accounting (§08 siblings)**: fund administration is the official books + investor register for funds (administrator posture, investor-facing services: capital accounts, statements, notices, portals). The IMP is the investment organization's own operating platform: the investment process is the center; accounting is one leg producing multi-basis books and GL feeds, with no investor register/dealing machinery at the center. Test: remove the investment decision/execution process from an IMP → investment accounting/fund-administration territory; add the investor register + investor services → fund administration. Clearwater's accounting page (GAAP/STAT/IFRS/tax, GL journals, NAIC/Solvency II) is investment accounting for asset owners/managers — not fund administration. Boundary held.
4. **vs Financial Risk Management Platform (§08 sibling)**: risk analytics is a module inside the platform (Aladdin Risk, Beacon, Axioma inside SimCorp) and a standalone Type; ex-ante risk is the separate Type's center of gravity. Consistent with the P&A pass finding that risk is "always a separate module even when bundled by the same vendors." Boundary held.
5. **vs Wealth Management Platform / Financial Advisor Platform (pending leaves)**: those are client-centric suites (households, advisors, planning, billing, portals). The IMP is investment-centric (the firm's books and lifecycle). The sampled platforms ship wealth extensions (Aladdin Wealth; Charles River wealth solution) — the extension pattern, not a merger. Per the PMS pass note, the advisor rebalancing category is the PMS-shaped slice inside wealthtech suites; the IMP leaf makes no claim on it. Boundary held.
6. **vs Retail Trading Platform / Brokerage Platform / Professional Trading Terminal / Algorithmic Trading Platform (processed siblings)**: different users and objects entirely — individuals, broker clients, strategy runtimes vs the investment organization's shared record and lifecycle. No shared center. Boundary clear.
7. **vs Investment Research Platform / Financial News & Research Platform / Financial Market Data Terminal (processed/pending siblings)**: research/data surfaces are inputs to the platform (integrated as partners: FactSet, MSCI, RIMES, Preqin). Consumption vs operation. Boundary clear.
8. **vs Private Market Investment Platform / Deal Management for PE-VC (§08)**: deal-centric lifecycle vs continuous portfolio lifecycle. The IMP extends into private assets (eFront/Preqin pairing; Charles River private markets; Clearwater alternatives; SimCorp public+private side by side) as a variant extension. Boundary held.
9. **vs ERP / General Ledger System**: the platform produces journal-ready, multi-basis output mapped to the corporate GL (Clearwater GL integration; Aladdin journal entries + CoA mapping); it does not replace the corporate ledger. Investment-specific books vs corporate books. Boundary held.
10. **vs BI / Reporting Platform (§13)**: reporting is one leg of the lifecycle, computed on the platform's own record with investment semantics (returns, bases, compliance states); generic BI lacks the record and the lifecycle. Boundary held.
11. **Taxonomy observation**: the market phrase "investment management platform" is also used loosely (some wealth/advisor vendors use similar phrasing). Within this directory, the §08 neighborhood (PMS, P&A, fund administration, wealth platforms as separate leaves) supports the institutional buy-side whole-lifecycle reading used here. No directory change proposed.

## Uncertainties

- No Tier-1 help-center/user-guide documentation was reachable for any sampled product; all evidence is official product/solution pages and FAQs. Operational fine structure (exact order state machines, permission models, NAV-strike steps, reconciliation cadences) is therefore not asserted anywhere.
- Aladdin's evidence is marketing-tier plus a product FAQ; workflow specifics are inferred from platform framing. Aladdin is used for structure anchoring, not capability precision.
- SS&C (Geneva/Anova), Allvue, LSEG, MSCI, FactSet platform shapes were not sampled (unreachable or adjacent Types); the sample may under-represent the alternatives-administration pole and the data-vendor-as-platform pole.
- The exact boundary between "investment accounting" as an IMP leg and "Investment Fund Accounting" as a sibling leaf will need the fund-accounting pass to hold (same pattern as the fund-administration pass's umbrella verdict).
- Market usage of "investment management platform" outside the institutional buy-side (wealth/advisor vendors) varies; treated as naming noise, not a Type conflict.

## Final Synthesis

An Investment Management Platform is the investment organization's end-to-end operating system: one unified record of the firm's investments — the shared book of record that every team works from — plus the full investment lifecycle carried as connected workflows on that record, from portfolio decision-making through order and trade handling, compliance and risk control, settlement and post-trade operations, investment accounting in multiple bases, to reporting outward to clients, boards, and regulators. The platform-ness is the unity: one record instead of per-function books, one connected lifecycle instead of siloed tools with reconciliation handoffs. The Portfolio Management System is its front-office slice; performance & attribution, risk, and compliance are embedded modules (also sold standalone); fund administration and the corporate GL sit outside it as producers/consumers of books. Everything else — real-time currency, cloud delivery, AI agents, three-book taxonomies, embedded execution, wealth and private-markets extensions — is mature structure or variant, not definition.
