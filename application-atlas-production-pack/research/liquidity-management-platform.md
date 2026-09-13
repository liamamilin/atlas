# Research Notes — Liquidity Management Platform

Leaf: Liquidity Management Platform (DIRECTORY.md §08 Finance, Banking, Insurance & Investment)
Slug: `liquidity-management-platform`
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Determine what a "Liquidity Management Platform" actually is as an Application Type: its defining core, its users, its world model (objects and their relations), its canonical workflow, its interfaces, its rules, and — critically — its boundary against the adjacent leaves **Treasury Management System**, **Cash Management Platform**, **Liquidity Risk Platform**, and **Financial Planning & Analysis / Budgeting & Forecasting**. The directory places this leaf immediately next to Treasury Management System and Cash Management Platform, so the Cash-vs-Liquidity seam is the primary boundary question of this pass.

## Initial Boundary (working hypothesis before research)

- Hypothesis: corporate-treasury-side software whose job is keeping the organization solvent day to day: consolidated view of where cash and available funding sit (banks, accounts, entities, currencies), forward projection of inflows/outflows against those balances, and a steering loop (fund shortfalls, deploy surpluses, move cash between entities/accounts).
- Nearest neighbors: Cash Management Platform (position + movement of the present), Treasury Management System (broader: instruments, debt, FX, risk), Liquidity Risk Platform (bank/regulatory side: LCR/NSFR-style prudential liquidity), FP&A (P&L-oriented planning).
- Unknowns: whether the market distinguishes "liquidity management" from "cash management" as products, or whether the two leaf names collapse into one Type; where crypto/on-chain liquidity fits; whether payment execution is definitional or optional.

## Research Questions

1. What is the core object of record — the position? the forecast? the cash flow line?
2. How does liquidity data enter the platform (bank connectivity, ERP, manual) and is connectivity definitional?
3. What does the forward projection look like (methods, horizons, granularity, sources of projected flows)?
4. What decisions/actions does the platform support (transfers, pooling, netting, facility draws, investments, payment timing) and are actions definitional or optional?
5. How do entities / banks / accounts / currencies structure the model?
6. Who uses it and how do roles differ (treasurer vs analyst vs CFO)?
7. Where does this Type end and Cash Management / TMS / Liquidity Risk begin?
8. What are the market's packaging variants (standalone vs suite pillar vs bank white-label vs ERP module)?

## Representative Products

Selected for market representation + documentation reachability + different customer levels + different philosophies:

| Product | Positioning observed | Customer level | Geography |
|---|---|---|---|
| Kyriba | "Liquidity Performance" platform; Connect–Protect–Forecast–Optimize pillars; explicit Liquidity Planning use case | Enterprise (+ midsize, public sector, banks/white-label) | Global (US) |
| Ripple Treasury (powered by GTreasury) | Enterprise TMS with a dedicated "Liquidity Management" solution as the modular entry point | Enterprise | Global (US) |
| Agicap | "Cash flow management software" marketing but full liquidity-planning content (13-week forecast, headroom, covenants, pooling) | SMB / mid-market | Europe (FR) |
| Nomentia | Modular "Smart Treasury Suite" (Connect / Pay / View / Manage / Optimise); payments-centric European lineage | Mid/large enterprise | Europe (FI) |

Rejected/abandoned samples:
- **Trovata** (US API-first cash management) — `trovata.com` is a women's clothing brand; `trovata.ai` returned 403 twice. Abandoned per network-limitation rule. The API-first pole is consequently under-sampled.
- **SAP / Oracle treasury modules** — ERP-embedded pole not fetched (prior passes documented these help portals as unfetchable SPAs). Under-evidenced pole, same pattern as the credit-management-platform pass.
- ION Treasury, FIS — not attempted within budget after four products reached stop conditions.

## Sources

All fetched 2026-09-08. All are Tier 1/2 official vendor pages (product pages, solution pages, use-case pages, FAQ sections). No authenticated help-center articles were reachable — vendor documentation portals are login-gated in this market segment.

- Kyriba — homepage, Liquidity Performance product page, Liquidity Planning use-case page: https://www.kyriba.com/ , https://www.kyriba.com/products/liquidity-performance/ , https://www.kyriba.com/use-cases/liquidity-planning/
- Ripple Treasury (GTreasury) — homepage and Liquidity Management solution page: https://treasury.ripple.com/ , https://treasury.ripple.com/solutions/cash/liquidity-management/ (help center at rippletreasury.atlassian.net exists but was not fetched)
- Agicap — homepage and Cash Management product page: https://www.agicap.com/en/ , https://www.agicap.com/en/products/cash-management/
- Nomentia — homepage / Smart Treasury Suite overview: https://www.nomentia.com/

Source-access limitation: operational help-center documentation (exact workflow steps, default settings, permission models, refresh frequencies) was not accessible for any product. All claims below are calibrated to product-page evidence; no precise numeric limits, refresh windows, or default values are asserted in the final document.

---

## Product Observations

### Kyriba (evidence layer A)

- Markets itself as a **"Liquidity Performance" platform** — one platform connecting cash, payments, forecasting, and risk. Pillars: **Connect** (bank/ERP/API connectivity; "9,900+ banks, every account, entity, and currency"), **Protect** (payment fraud prevention), **Forecast** (AI-powered, explainable, scenario modeling / stress-testing), **Optimize** ("free up idle cash, lower financing costs"; recommendations tied to liquidity position).
- Products: Treasury ("real-time cash & treasury management"), Risk Management (FX, Debt, Investments, Interest Rates), Payments, Connectivity, Working Capital.
- Liquidity Planning use case: "Bring together cash forecasts, business inputs, and financial obligations to understand future liquidity needs across entities, currencies, and time horizons." A **Unified Worksheet** combines real-time cash positions, committed flows, short-term forecasts, and long-term plans "with spreadsheet-like flexibility and connected data". Advanced Liquidity Planning adds variance analysis, scenario modeling across working capital / FX / debt / investment / liquidity decisions.
- Vendor's own articulation of the seam: *"Where traditional cash forecasting only predicts future cash positions, [Liquidity Planning] surrounds the forecast with rich contextual data and AI-driven insights, enabling treasury teams to make better-informed liquidity decisions across diverse risk scenarios rather than simply reporting on them."*
- Forecast cycles: compare forecasts to actuals, analyze variances, refine assumptions.
- Segments: Enterprise, Midsize, Public Sector, Banks (white-label delivery of liquidity/payments/risk to corporate clients). A "Stablecoin and On-chain Liquidity" use case exists.
- CFO-facing artifact observed: debt-maturities ladder chart ("Cash is building. Debt is maturing.").

### Ripple Treasury, powered by GTreasury (evidence layer A)

- Enterprise TMS sold modularly; **"Liquidity Management" is a named solution and the documented entry module** ("Begin with a focus on liquidity management if that's all your company requires now. As your needs expand, seamlessly integrate additional modules such as Payments, Financial Instruments, and Accounting").
- Liquidity Management content: cash positions "derived from real-time transactional data aggregated from any bank, ERP, and other external sources"; **interactive cash position worksheets** with **transaction-level tagging** and customizable views; **automated cash-level optimization** via "target balance recommendations that automate transfers"; **scenario analysis** to "manage liquidity risks, identify potential counterparty exposures, and simulate cashflow impacts"; flexible reporting.
- AI layer (GSmart): learns from past cash flows/sales/treasury data, selects forecasting algorithms per scenario, reports which model was chosen and its expected error margin.
- Worksheet capabilities: "Flagging optimal cash transfers — quickly identify when to move funds based on surplus or deficit balances"; "Track actuals versus estimates"; "Monitor balances linked to credit facility usage, keeping a clear view of debt obligations."
- Homepage solution pillars: Total Cash Visibility, Cash Flow Forecasting, Capital Efficiency (debt & investment portfolios), Risk Management (FX/IR hedging), Netting, Payments. Digital assets: "digital wallets behave like bank accounts… real-time pricing converts holdings to current fiat value."

### Agicap (evidence layer A)

- Markets as "cash flow management software" but its product page carries the full liquidity-planning stack; targets SMB/mid-market; 7,000+ businesses claim (marketing figure, not carried forward).
- **Real-time cash positioning**: "consolidated cash position in real time, across all accounts, credit lines, financial investments, and intercompany balances."
- **Forecasting**: "Direct method cash forecast, indirect method liquidity planning"; forecasts built from "P&L budget, FP&A data, financial KPIs, historical actuals and recurring cash flows"; fed by financing operations, intercompany flows, AP, AR modules; horizons "daily, weekly, and monthly" with "13-week cash flows, quarterly working capital forecasts, and annual strategic plans."
- **Scenario modeling**: "Stress-test cash flow scenarios. Instantly model how market changes will impact your liquidity headroom, FX exposure, and bank covenants before committing."
- **Steering machinery**: automated cash pooling suggestions and intercompany netting "with interest calculations"; payment runs; surplus cash monitoring with "investment simulations across different time horizons"; investment maturity/yield tracking.
- **Debt management**: credit facilities, loans, authorized overdrafts "synced with your cash flow plan"; net financial position; amortization schedules integrated into the rolling 13-week forecast; covenant and repayment-deadline monitoring; intercompany loans with configurable interest.
- **Receivables financing**: factoring drawdown modeling with advance rates and fees feeding the 13-week runway.
- **Reconciliation**: AI matches bank transactions to outstanding invoices; automatic journal posting.
- **Reporting**: dashboards, forecast-vs-actual variance analysis "by group, subsidiary, or category", multi-entity consolidation in group currency, Excel/PDF exports.
- Explicit positioning against FP&A: "While FP&A focuses on long-term planning, Agicap is built for daily cash management."
- A Claude/MCP integration page exists (AI assistant surface).

### Nomentia (evidence layer A)

- **Smart Treasury Suite** with five named module families: **Connect** (10,000+ bank connections claim; bank connectivity as a service, ERP integrations, trading platforms, market data), **Pay** (payments hub, bank account management, direct debits, sanctions screening, fraud prevention), **View** (**Cash Flow Forecasting**, **Cash Positioning** — "See current and expected cash positions earlier, compare forecasts with actuals, and support liquidity decisions with a clearer view of what is driving cash"), **Manage** (debt & investments, derivatives, guarantees, exposure & risk, treasury & hedge accounting), **Optimise** (**In-House Bank** — "Centralise intercompany funding", **Intercompany Netting**, **Cash Pooling** — "Optimise group liquidity", bank account reconciliation, cash application).
- Use-case buckets: Payments / **Cash & Liquidity** / Treasury & Risk Management. Role pages: CFO ("Steer liquidity and funding strategy with full visibility and confidence"), Treasury ("Control cash, risk and payments across every entity"), IT/Operations.
- European positioning ("Secure, Certified, European"; local practices/regulatory requirements).

---

## Cross-product Comparison

| Finding | Kyriba | Ripple/GT | Agicap | Nomentia | Evidence | Layer |
|---|---|---|---|---|---|---|
| Consolidated cash position across banks/accounts/entities/currencies | A | A | A | A | B (4/4) | L0 |
| Forward projection of cash (forecast with dated inflows/outflows against balances) | A | A | A | A | B (4/4) | L0 |
| Projection supports liquidity decisions (funding/deployment), not just reporting | A ("decisions", not "reporting") | A (flag transfers; scenarios) | A (headroom, covenants, draws) | A ("support liquidity decisions") | B (4/4) | L0 |
| Steering machinery: transfers / pooling / netting across the group | A | A (target balances, optimal transfers) | A (pooling, IC netting, IC loans) | A (pooling, netting, in-house bank) | B (4/4) | L0 (concept) |
| Bank/ERP/manual connectivity as the acquisition layer | A | A | A | A | B (4/4) | L1 |
| Transaction-level detail, tagging, worksheets | A | A | A (matching/reconciliation) | — (not directly observed) | B (3/4) | L1 |
| Availability beyond cash in position: credit lines/facilities, investments, intercompany | A (debt ladder; investments) | A (facility usage) | A (explicit) | A (debt & investments) | B (4/4) | L1 |
| Multiple horizons & granularities (short rolling / medium / long) | A (short-term + long-term) | — (not stated) | A (daily→annual, 13-week) | A ("current and expected") | B (3/4) | L1 |
| Scenario modeling / stress | A | A | A | — (not directly observed) | B (3/4) | L1 |
| Forecast-vs-actual variance loop | A | A | A | A | B (4/4) | L1 |
| Surplus investment management | A | A (capital efficiency) | A | A | B (4/4) | L1 |
| FX exposure view / hedging | A (product) | A (risk solution) | A | A (exposure & risk) | B (4/4) | L1–L2 |
| Debt/covenant/repayment awareness | A | A (facility usage) | A | A | B (4/4) | L1 |
| Payment execution in-product (hub, approvals, fraud/sanctions) | A (product) | A (module) | A | A (module) | B (4/4) | L2 |
| Reconciliation / cash application / journal posting | — (not observed) | — (not observed) | A | A | B (2/4) | L2 |
| Bank account management (mandates/signatories) | — | — | — | A | single-product observed | L2 |
| In-house bank (centralized IC funding) | — | A (feature list "In-House Banking") | — (IC loans observed; IHB not named) | A | B (2/4) | L2 |
| Instrument management (derivatives, guarantees, hedge accounting) | A (Risk product) | A (Financial Instruments module) | partial (hedging instruments modeling) | A | B (3–4/4) | L2 (TMS-expansion) |
| AP/AR automation as feeding modules | — | A (AR/AP forecasting solution page exists) | A | — | B (2/4) | L2 |
| AI/ML forecasting & assistance | A | A | A | A (AI assistants/agents) | B (4/4) | L1 (era-current, not definitional) |
| Digital assets / stablecoins / on-chain liquidity | A (use case) | A (wallets as bank accounts) | — | — | B (2/4) | L2 variant |
| White-label delivery to banks | A | — | — | — | single-product | L3 |
| Public sector vertical | A | — | — | — | single-product | L3 |
| Mobile companion app | — | — | A | — | single-product | L3 |
| Planning worksheets with "spreadsheet-like flexibility" | A (Unified Worksheet) | A (Worksheets) | — (import/export spreadsheets) | — | B (2/4) | L1 |

### Modeling observations

- **The position is derived, not authoritative.** Every product describes the position as aggregated from banks/ERPs/external sources. The platform is the consolidation and decision layer, not the money ledger of record (the banks hold the accounts; the ERP/GL holds the business transactions).
- **The forecast is anchored to the position.** Projection is described as flows projected onto balances (direct method: scheduled/expected flows; indirect: from P&L/budget/KPIs), producing expected liquidity at future dates.
- **"Management" = the decision/steering loop.** All four products surround the forecast with action surfaces: transfer flags/target balances, pooling/netting, facility headroom tracking, investment deployment. Kyriba's own copy contrasts "liquidity decisions" with "simply reporting on them".
- **Facility/debt capacity is a tracked object everywhere.** Credit facilities/overdrafts with headroom appear in all four, tied into the forecast (debt service, covenant deadlines).
- **Group structure is the modeling frame for enterprise products.** Entities, subsidiaries, group currency consolidation, intercompany flows, pools. The SMB pole (Agicap) still models entities but more lightly.
- **Variance loop is universal**: forecasts are continuously compared with actuals and refined.

## Canonical Model (synthesis)

```text
Liquidity Structure        entities / bank accounts / banks / currencies / pools
        │
        ▼
Liquidity Position         consolidated available resources NOW
        │                    (cash balances; commonly + facility headroom,
        │                     liquid investments, intercompany balances)
        ▼
Cash Flow Lines            dated projected inflows/outflows with source/category
        │                    (committed flows, scheduled obligations, historical
        │                     patterns, plan/budget data)
        ▼
Liquidity Projection       expected position by date/entity/currency over a horizon
        │                    → headroom or shortfall against upcoming obligations
        ▼
Liquidity Actions          move cash (transfer/sweep/pool/net), source funds
        │                    (draw facility / intercompany funding), deploy
        │                    surpluses (investment), adjust payment timing
        ▼
Executed & Recorded        in-product execution or via banks; results return
        │                    into the position
        ▼
Variance Loop              forecast vs actuals → refine assumptions/accuracy
```

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal, jointly-held)

1. **The whole-organization liquidity position of record** — a consolidated, inspectable picture of the organization's immediately available liquid resources across its bank accounts, entities, and currencies (in mature products extended with facility headroom, liquid investments, and intercompany balances). *Remove → per-bank portals / statements; the "whole organization, one picture" property is gone.*
2. **The date-aware liquidity projection** — projected inflows and outflows laid onto that position over defined horizons, producing expected future liquidity (headroom/shortfall) against upcoming obligations. *Remove → cash management/bank reporting; the platform only answers "where is cash now", never "will we meet what's coming".*
3. **The liquidity steering loop** — projected position and current position jointly convert into funding and deployment decisions that are tracked and reflected back: moving cash (transfers/sweeps/pooling/netting), sourcing funds (facility draws, intercompany funding), deploying surpluses (investment), adjusting timing. *Remove → a liquidity reporting/monitoring view, not management.*

Jointly-held is load-bearing:
- 1+3 without 2 = cash positioning/payments platform (present-movement focus)
- 2+3 without 1 = budgeting/forecasting (plans without consolidated actual position)
- 1+2 without 3 = liquidity reporting / BI over cash data

Not in L0 despite being near-universal: bank/ERP connectivity (manual consolidation satisfies it historically), transaction-level tagging, payment execution in-product, AI, scenario modeling, multi-currency, in-product investment machinery.

### L1 — Common Mature Structure

- Acquisition layer: automated bank connectivity (API/EBICS/H2H/SWIFT/file), ERP feeds, spreadsheet/manual import
- Transaction-level detail with tagging/categorization; interactive position worksheets (spreadsheet-like planning surfaces with connected data)
- Availability beyond cash in the position: credit lines/facilities with headroom, liquid investments, intercompany balances
- Forecast machinery: direct and indirect methods; multiple horizons (short rolling — commonly weekly/13-week — plus quarterly/annual) and granularities (daily/weekly/monthly); feeds from AP/AR, debt service, financing operations, plan/budget data
- Funding-capacity tracking: facilities, overdrafts, amortization schedules, covenant/repayment deadlines
- Scenario modeling / stress-testing of headroom, FX exposure, covenants
- Variance loop: forecast vs actuals by group/entity/category; accuracy refinement
- Surplus deployment: investment options, maturities/yields tracking
- Group-liquidity optimization structures: cash pooling, intercompany netting (with interest), consolidation in group currency
- FX exposure consolidation view; hedging instrument awareness
- Reporting/dashboards and exports; surplus/deficit flagging and recommendations; AI/ML forecasting assistance (era-current)

### L2 — Variant / Optional Structure

- In-product payment execution (payments hub, approvals, sanctions screening, fraud prevention)
- Bank account management (accounts registry, mandates/signatories)
- In-house bank (centralized intercompany funding with interest)
- Treasury instrument management (debt portfolios, investments, derivatives, guarantees, hedge accounting) — the TMS-expansion pole
- Reconciliation / cash application / journal posting
- AP/AR automation as feeding modules
- Digital assets / stablecoins / on-chain liquidity as additional resource classes
- Regional connectivity regimes (European open-banking emphasis vs SWIFT/H2H/file-based), regional deployment (European-certified pole)
- White-label delivery to bank clients; public-sector verticals
- Mobile companion surfaces

### L3 — Vendor-specific (Research Notes only)

- Kyriba: "Liquidity Performance" framing, Connect–Protect–Forecast–Optimize pillars, Unified Worksheet, TAI agentic AI, Liquidity Calculator, white-label for banks, public-sector solutions, "9,900+ banks" claims
- Ripple Treasury: GSmart AI (model selection + reported error margins), 90-day implementation, "13,000 connected banks"/"$12.5T payments volume" claims, Ripple-native digital wallet, OCC/NYDFS infrastructure framing, "Worksheets" product name
- Agicap: Claude/MCP integration, 24-hour trial, factoring module with advance rates, WAR/coverage-ratio tracking, H2H/BACS/SWIFT/EBICS claims, "7,000+ businesses"
- Nomentia: Connect/Pay/View/Manage/Optimise module naming, Treasury Maturity Assessment, "10,000+ bank connections" claim

## Historical / Market-Sample Check

Pre-software treasury practice: a treasurer compiling bank statements into a cash book across subsidiaries (position), maintaining a rolling cash-flow forecast on paper/spreadsheet (projection), and deciding overdraft draws, intercompany loans, and surplus placements (steering). The 13-week rolling forecast is a decades-old treasury artifact. This satisfies the L0 triple without real-time APIs, cloud, AI, payment hubs, or automated pooling. **Historical check passed.** ERP-embedded treasury modules (SAP-class) with cash positioning + forecasting + pooling also fit the core structurally, though not directly fetched in this pass.

## Boundary Findings

| Neighbor | Relationship | Distinction (remove-what test) |
|---|---|---|
| **Cash Management Platform** | sibling, heavily conflated in market naming | Center of gravity test: cash management = present position + money movement (aggregation, positioning, sweeps, payments). Liquidity management = forward adequacy + funding steering across time (projection against obligations, funding/surplus decisions). Remove the projection+steering machinery → cash management; remove the present-tense aggregation → forecasting tool. Market evidence: a vendor can sell "liquidity management" as its cash-visibility entry module (Ripple) while another sells "cash management" with full liquidity-planning content (Agicap). **Joint review with the cash-management-platform leaf is recommended.** |
| **Treasury Management System** | superset | TMS adds the instrument-level world: debt/investment portfolios, derivatives, guarantees, hedge accounting, risk analytics. Liquidity Management is the cash/liquidity heart; when instrument management and risk become the primary objects → TMS. All four sampled products are TMS-capable suites whose liquidity modules alone still satisfy L0. |
| **Liquidity Risk Platform** | different seat (bank/regulatory vs corporate) | Bank-side prudential liquidity (ALM, LCR/NSFR-style metrics, stress testing, deposit run-off) vs corporate steering of the firm's own cash. Different users (bank treasury/ALM vs corporate treasury), different objects (regulatory metrics vs consolidated corporate position). Not directly verified against a sampled product — held conceptually. |
| **Financial Planning & Analysis / Budgeting & Forecasting** | adjacent, feeds | FP&A plans P&L/balance-sheet over long horizons; liquidity platform operates cash-dated, obligation-anchored, day-to-day. Agicap explicitly positions itself against FP&A ("FP&A focuses on long-term planning, Agicap is built for daily cash management"); plan/budget data feeds the forecast. |
| **Accounting Software / GL / ERP** | upstream source | ERP/GL records business transactions; the liquidity platform consolidates and projects them. Position is derived data; corrections happen upstream or as adjustments. |
| **Payment Orchestration / Payments platforms** | optional machinery | Payment execution inside the liquidity platform is common but not definitional; steering can be recommendation + execution via bank channels. |
| **Business Banking Portal** | different seat | Bank-side, per-bank account view vs organization-side multi-bank consolidated view. |

## Uncertainties

1. **No authenticated help-center documentation** was reachable for any sampled product; all evidence is product/solution-page level. Exact workflow steps, permission models, refresh frequencies, and defaults are unverified — the final document deliberately contains no precise numbers or defaults.
2. **Trovata (API-first pole) unreachable** (403 ×2); the standalone API-first philosophy is under-sampled.
3. **ERP-embedded pole (SAP/Oracle) not fetched**; structural fit argued, not observed.
4. **Liquidity Risk Platform boundary** is reasoned, not verified against a sampled bank-side product.
5. **Market naming conflation** (cash management vs liquidity management) is real and documented from vendor copy itself; the seam chosen here (present-movement vs forward-adequacy center of gravity) is a research judgment that should be re-tested when the `cash-management-platform` leaf is processed.

## Final Synthesis

A Liquidity Management Platform is the finance function's forward-adequacy system of record: it consolidates the organization's available liquid resources into one position across banks, accounts, entities, and currencies; projects that position against dated inflows/outflows and committed obligations to expose future headroom or shortfall; and converts those projections into tracked funding and deployment actions (move cash, source funds, deploy surpluses, time payments), closing the loop by comparing forecasts with actuals. Its defining core is the jointly-held triple of consolidated position + date-aware projection + steering loop. Connectivity, transaction tagging, facility tracking, scenarios, pooling, AI, and payment execution are mature or optional layers, not the definition.
