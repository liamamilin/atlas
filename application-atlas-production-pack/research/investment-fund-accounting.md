# Research Notes — Investment Fund Accounting

## Research Goal

Understand the "books leg" of the fund-operations family: what an Investment Fund Accounting system actually is, what objects it holds, how the accounting cycle works, and how it differs from (a) the fund-administration umbrella, (b) the transfer-agency register leg, (c) the investment-management platform whole, (d) generic accounting software / GL systems, and (e) the nonprofit "fund accounting" false friend.

This pass is responsible for discharging the joint-review flags recorded by the fund-administration-platform pass (2026-09-07), the transfer-agency-platform pass (2026-09-08, which ratified keep-all-three), and the investment-management-platform pass (2026-09-07, which asked this pass to hold the platform/accounting seam from its side).

## Initial Boundary

Working hypothesis before research:

- Investment Fund Accounting = the official books of record and valuation machinery for pooled investment vehicles: portfolio accounting, investor/partner capital-account accounting, fee accruals, NAV calculation, financial statements, GL feeds.
- NOT the investor register / dealing / LP-portal legs (fund administration, transfer agency).
- NOT the front-office investment lifecycle (portfolio management, investment management platform).
- NOT generic corporate accounting (management-company books).
- NOT nonprofit restricted-fund accounting (§25 false friend).

## Research Questions

1. What is the unit of record — fund, entity, portfolio, book?
2. What does the system hold: positions, transactions, prices, capital accounts, accruals?
3. What is the defining output: NAV per share/unit/class, financial statements, capital statements, GL feeds?
4. How does the periodic cycle work (reconcile → value → accrue → allocate → strike NAV / close → report)?
5. What fund-specific accounting machinery exists (multi-book/multi-basis, fee crystallization, waterfalls, equalization, tax allocations)?
6. Who operates it (fund accountants, administrators, asset-owner finance teams)?
7. What is deliberately NOT in it (register, dealing, portals, front office)?
8. Where is the boundary against generic GL/accounting software?
9. Historical check: would a paper-era fund bookkeeper's ledger satisfy the definition?

## Representative Products

Selected for market representativity, documentation quality, different product philosophies, and different customer levels:

| Product | Pole | Why sampled |
|---|---|---|
| SS&C Advent Geneva | classic standalone hedge-fund portfolio & investor accounting ("industry-standard") | the canonical fund-accounting product; shadow-accounting philosophy |
| Allvue Fund Accounting | modern cloud fund-accounting module for PE/credit, sold to GPs and fund administrators | vendor that brands the slice "Fund Accounting" and separates it from its own Investor Portal product |
| FundCount | unified portfolio + partnership accounting on one GL for hedge funds, PE, family offices, administrators | richest public workflow documentation; explicitly contrasts itself against generic GLs and PMS+accounting stacks |
| Clearwater Analytics (Investment Accounting) | asset-owner / asset-manager investment accounting (daily ABOR, multi-basis) | the pole without investor capital accounts — tests whether the definition over-fits the fund pole |

## Sources

All fetched 2026-09-10 (Tier 1/2 — official product and solutions pages; help-center depth not publicly reachable):

- SS&C Advent — https://www.advent.com/ (solutions taxonomy), https://www.advent.com/solutions/geneva/ , https://www.advent.com/solutions/?b=fund-accounting
- Allvue Systems — https://www.allvuesystems.com/ (product taxonomy), https://www.allvuesystems.com/solutions/fund-accounting/
- FundCount — https://fundcount.com/ , https://fundcount.com/solutions/partnership-accounting/
- Clearwater Analytics — https://cwan.com/ , https://cwan.com/solutions/investment-accounting-reporting/

Prior-pass evidence reused: research/fund-administration-platform.md, research/transfer-agency-platform.md, research/investment-management-platform.md (STATUS.md boundary records).

## Product Observations

### SS&C Advent Geneva (evidence layer A)

- Positioned as "an industry-standard and comprehensive **portfolio and investor accounting** solution" for alternative investment managers (hedge funds, private credit, multi-manager funds).
- Capability pillars on the product page: Portfolio and Fund Management & Reporting; **Investor Accounting & Reporting** ("multi-currency platform supporting trading, real-time portfolio management and accounting, investor accounting and reporting"); **Shadow Accounting** ("internal accounting is key to investor due diligence, client service expectations, operational flexibility and independence, and improve fund oversight"); Reconciliation & Workflow Management ("robust exception management and data governance workflows"); Data Management; Managed Services.
- Dedicated product briefs: "Geneva Private Markets", "Geneva Investor Accounting & Reporting", "Geneva for credit and derivative instruments", "Geneva Suite".
- SS&C Loan Data pairing: "the portfolio management and accounting system of choice for managing and processing the global loan lifecycle" — loan-level accounting complexity is in-scope.
- Won Hedgeweek "Best Fund Accounting and Reporting Software" award (vendor-cited).
- Advent's own solutions taxonomy lists **Fund Accounting** and **Investor Servicing** as separate business needs — the vendor itself splits the books leg from the investor-services leg.

### Allvue Fund Accounting (evidence layer A)

- "Cloud-based, fully integrated **back-office** solution purpose-built for private equity fund managers and fund administrators."
- Composition: "a **true general ledger**, multi-currency support, **partnership accounting**, automated **waterfall calculations**, and investor reporting in a single system."
- Feature list: true general ledger with financial-report library and flexible report writer; workflow standardization across multiple funds; optional waterfall module ("carry fee calculations with detailed modeling of LPAs"); cloud architecture on Microsoft Dynamics 365 Business Central / Azure; integration with management-company accounting ("fund accounting and management company books are maintained from a single source of record").
- Supported structures: "standard LP/GP structures, funds of funds, co-investment vehicles, and multi-currency funds"; multi-fund environments from a single instance.
- Quarter-end framing: "automating capital call processing, distribution calculations, and financial statement generation — replacing manual spreadsheet workflows."
- Allvue's product taxonomy separates **Fund Accounting / Investment Accounting / Corporate Accounting** (back office) from **Investor Portal / Fundraising** (investor relations) — the vendor sells the books leg and the investor-services leg as different products.
- FAQ explicitly compares against "Investran, Yardi, and other fund accounting platforms" and against "real estate or generic enterprise accounting" — the market itself recognizes a distinct fund-accounting category.

### FundCount (evidence layer A — richest operational documentation)

- Positioning: "Unified accounting & investment software — one source of truth for every entity, fund, and asset class… reconciled by construction, not assembled by hand."
- Platform diagram: source data & capital activity (custodian/bank feeds: positions, transactions, cash, valuations; holdings & transactions: buys, sells, corporate actions, pricing; private fund activity: capital calls, distributions, commitments; fees & expenses; multi-entity structures; supporting documents) → **Portfolio Accounting** (performance, valuations, exposures, FX, derivatives, multi-currency) + **Partnership Accounting** (capital accounts, allocations, fees, profit splits) → **General Ledger** (multi-entity, multi-currency; journals; intercompany; consolidations) → **Reporting** (financials, performance, NAV, look-through) → **Investor Portal** (permissioned access, document delivery).
- Hedge-fund pole: "Strike every NAV, crystallize every fee, shadow every administrator. Shareholder accounting and the investment book on one multi-currency ledger — **NAV by fund, class, series and side pocket**. Master-feeder, series and side pockets, allocated correctly. Incentive and management fees, crystallized correctly."
- PE pole: "capital accounts, waterfalls, partial transfers and side pockets… A configurable waterfall engine, not a spreadsheet… Capital calls and LP communication."
- Partnership-accounting page: commitments & capital calls, contributions & distributions, partner transfers (partial & full, one-to-many, many-to-one, mid-period), fees/carry/waterfall terms, multi-entity structures (LPs, feeders, SPVs, series LLCs, side pockets), investor & tax data.
- "One allocation engine. Configurable. Posted to the GL." — "posts the journal entries to the same general ledger that holds your trades, cash, and accruals. There is no bridge to rebuild because there are no two systems." "The capital account is a view of the ledger, not a parallel record."
- U.S. partnership tax in-system: Section 704(b) capital accounts, 704(c) built-in gain, 754 step-ups, IRS K-1 generation from the same ledger.
- Explicit boundary table against "Spreadsheet + generic GL (Sage / NetSuite / QuickBooks)" and "Specialized PMS + accounting system": "**Allocation logic generic ERPs cannot match**"; "One investment-aware, multi-currency ledger under every entity"; "The depth of a fund accountant. The reach of an investment platform."
- Multi-book: "IFRS / GAAP — multi-book, multi-currency, allocation-aware from day one."
- Scale claims: $100B+ assets on platform, 25 countries, 27+ years.

### Clearwater Analytics — Investment Accounting (evidence layer A)

- "Daily, validated, **multi-basis, multi-currency** investment accounting and reporting across public and private assets."
- "Automated **ABOR** — daily accounting and reconciliation across public and private assets, aligned to **GAAP, STAT, IFRS, tax**, and other local accounting basis."
- "Multi-basis logic engine — simultaneous calculations across books and currencies with configurable accounting treatments."
- "Validated data foundation — daily, automated feeds from custodians, managers, and internal systems, with built-in reconciliation and exception handling."
- "**GL integration** — journal-ready outputs tailored to your ERP or GL, with customizable logic and mapping."
- "Regulatory reporting — continuously updated templates for NAIC, Solvency II, and other frameworks."
- "Governance and controls — configurable roles, approval workflows, versioning, and audit logs."
- Names the ABOR/IBOR conflict: "Disconnected ABOR and IBOR systems create conflicting views of the portfolio"; "powered by a daily, automated Accounting Book of Record (ABOR) foundation."
- Serves asset owners (insurers, pensions, corporates, banks, public sector) and asset managers — **no investor register, no dealing, no LP portal** on this page; the investor-facing legs live elsewhere in the platform taxonomy.
- Clearwater's own taxonomy places "Accounting & reporting" as one solution inside a front-to-back investment lifecycle — the platform whole vs the accounting slice.

## Cross-product Comparison

| Structure | Geneva | Allvue FA | FundCount | Clearwater IA |
|---|---|---|---|---|
| Official books of record (investment-aware GL) | ✓ ("portfolio and investor accounting") | ✓ ("a true general ledger") | ✓ ("one investment-aware, multi-currency ledger") | ✓ (daily ABOR) |
| Investment portfolio accounting (positions/trades/corporate actions post to books) | ✓ | ✓ (investment accounting sibling) | ✓ (Portfolio Accounting) | ✓ |
| Investor/partner capital accounts + allocations | ✓ (Investor Accounting) | ✓ (partnership accounting) | ✓ (Partnership Accounting) | ✗ (asset-owner pole) |
| Fee machinery (mgmt/incentive/carry, waterfalls) | ✓ (fee-calculation whitepapers/webinars) | ✓ (waterfall module, LPA modeling) | ✓ (crystallization, configurable waterfall engine) | — (not on page) |
| NAV output | ✓ (fund accounting) | ✓ (quarter-end cycle) | ✓ (NAV by fund/class/series/side pocket) | — (NAV not the frame; entity books are) |
| Multi-book / multi-basis / multi-currency | ✓ (multi-currency) | ✓ (multi-currency GL) | ✓ (IFRS/GAAP multi-book) | ✓ (GAAP/STAT/IFRS/tax concurrent) |
| Periodic close → official outputs (financial statements, capital statements, K-1s) | ✓ | ✓ (financial statement generation) | ✓ (capital statements, K-1s) | ✓ (close, regulatory + stakeholder reporting) |
| GL feeds / journal entries to corporate ERP | implied (GL role) | ✓ (management-company integration) | ✓ (posts to GL) | ✓ (journal-ready GL outputs) |
| Reconciliation & exception handling | ✓ | implied | ✓ ("reconciled by construction") | ✓ (built-in reconciliation, exception handling) |
| Investor register / dealing / subscriptions-redemptions | ✗ (Investor Servicing is a separate Advent solution) | ✗ (Investor Portal is a separate product) | ✗ (Investor Portal is a separate solution) | ✗ |
| Front-office PMS/OMS | sibling product (Eze/Genesis) | sibling products | sibling capability framing | sibling solutions in lifecycle |

## L0 / L1 / L2 / L3

### L0 — Defining Invariant (minimal)

Three jointly-held structures over one binding:

1. **The fund's official books of record.** A general ledger in which the vehicle's investment activity — positions, trades, corporate actions, income, cash — and its capital activity post as accounting entries; the investment record and the books are one record, not a position system reconciled to a separate ledger. Remove → portfolio management system / IBOR / data aggregator.
2. **Fund-specific accounting machinery.** The portfolio held at fair value with fund-specific treatments: multi-book/multi-basis (GAAP/STAT/IFRS/tax and local regimes), multi-currency, fee accruals (management/incentive/carry), and — in the fund pole — investor/partner capital accounts with allocation and waterfall logic, producing NAV per share/unit/class where the regime provides. Remove → generic accounting software / GL system.
3. **The governed periodic close producing official financial outputs.** A recurring cycle — reconcile, value, accrue, allocate, strike NAV / close the books — that ends in the vehicle's authoritative financial artifacts: financial statements, NAV, capital statements, tax packs (e.g., K-1s), and journal-ready feeds to the corporate ERP. Remove → analytics/reporting shell.

Binding: **investment-fund semantics** — the subject is pooled investment vehicles and investment portfolios under fund/investment accounting regimes. Remove → generic corporate accounting.

Jointly-held is load-bearing: (1 alone = PMS/IBOR; 2 without 1 = calculators over nothing; 3 without 1+2 = reporting shell; 1+2 without 3 = books that never close; 1+3 without 2 = generic ledger with a close; 2+3 without 1 = spreadsheet-era fire drill).

### L1 — Common Mature Structure

- Investor/partner capital-account accounting as a first-class leg (universal in the fund pole: Geneva "Investor Accounting", Allvue partnership accounting, FundCount Partnership Accounting); absent in the asset-owner pole.
- Automated data feeds from custodians, brokers, administrators, market-data vendors (FundCount data aggregation; Clearwater validated feeds; Advent data solutions).
- Reconciliation and exception-management workflows (Geneva, FundCount, Clearwater).
- Waterfall/allocation engines (Allvue optional module; FundCount configurable engine).
- Tax machinery (FundCount 704(b)/(c)/754 + K-1s; Allvue investor reporting).
- Regulatory-basis reporting templates (Clearwater NAIC/Solvency II).
- Shadow accounting posture (Geneva, FundCount) — manager-side books shadowing the administrator's official books.
- Governance: roles, approvals, versioning, audit logs, drill-down (Clearwater, FundCount).
- Performance/IRR/TVPI outputs computed from the books (FundCount).

### L2 — Variant / Optional

- Fund regime: open-ended (NAV cycle, classes/series/side pockets, equalization, crystallization) vs closed-ended (commitments, calls, distributions, waterfalls) vs asset-owner (no investor capital accounts; entity/regulatory books).
- Asset class tuning: hedge, PE/VC, private credit/CLO, loans (Geneva + SS&C Loan Data), real estate, fund of funds.
- Operating model: software used by the manager's own fund-accounting team vs used by third-party fund administrators (multi-tenant) vs shadow-accounting posture vs outsourced service.
- Delivery: cloud SaaS (Allvue/Azure, FundCount, Clearwater) vs legacy on-prem era.
- AI document extraction / assistants (Allvue Andi, FundCount AI Assistant, Clearwater GenAI) — era-common, not definitional.

### L3 — Vendor-specific (research notes only)

- Geneva: "shadow accounting" as a branded pillar; SS&C Loan Data pairing; Hedgeweek award claim.
- Allvue: Andi assistant, Dynamics 365 Business Central substrate, FirmView carry/compensation sibling, "Investran/Yardi comparison" FAQ.
- FundCount: AI Document Intelligence (PDF alternatives statements posted to the book), "reconciled by construction" branding, series-LLC/debt-provider participation modeling, demo-environment walkthrough sales motion.
- Clearwater: ABOR terminology, Beacon/Enfusion platform siblings, NAIC/Solvency II template updates, $10T assets claim.

## Vendor-specific Findings

- Only FundCount documents open-ended mechanics at this depth (NAV by class/series/side pocket, crystallization); only FundCount documents U.S. partnership-tax machinery in-system. Treat equalization/series and 704 machinery as regime/segment structures, not Type-defining.
- Only Geneva frames "shadow accounting" as a first-class capability; FundCount echoes it ("shadow every administrator", "shadow your administrator with confidence"). Two products → common in the hedge-fund pole, not definitional.
- Only Clearwater frames the ABOR/multi-basis daily cycle as the center; the fund-pole products frame the NAV/capital cycle as the center. Both are the same underlying structure (books + periodic close) at different customer levels.
- Allvue's FAQ naming Investran/Yardi as comparators confirms the market recognizes "fund accounting software" as a category with multiple vendors.

## Boundary Findings

| Neighboring Type | Relationship | Sharpest seam ("remove X → becomes the other Type") |
|---|---|---|
| **Fund Administration Platform** | umbrella vs books leg | Remove the investor register + investor-facing services (statements/notices/portal) from fund administration → investment fund accounting. **Joint-review flag DISCHARGED from this side: keep-all-three RATIFIED.** Vendor corroboration: Allvue sells Fund Accounting and Investor Portal as separate products; FundCount lists Investor Portal as a separate solution; Advent separates Fund Accounting from Investor Servicing. None of the sampled fund-accounting surfaces claims the register or dealing as its center. |
| **Transfer Agency Platform** | register leg vs books leg | Transfer agency = securityholder register + register-maintaining transactions + holder servicing, no portfolio books/NAV. This Type = the books; the register is not among its objects. Consistent with the transfer-agency pass's finding that SS&C puts NAV under fund administration, not transfer agency. |
| **Investment Management Platform** | whole vs slice | IMP = unified investment record + connected front-to-back lifecycle (decision → execution → reporting). This Type = the back-office books of record only. Clearwater's own taxonomy places "Accounting & reporting" as one solution inside the lifecycle; the investment-management-platform pass already held this seam from the platform side. **Held from this side: no front-office objects (ideas, orders, compliance, risk) at this Type's center.** |
| **Portfolio Management System / Performance & Attribution** | decision support vs books of record | PMS supports investment decisions/monitoring; this Type is the official record. FundCount's own comparison table treats "Specialized PMS + accounting system" as a two-system stack this Type replaces — the market itself keeps them separate and reconciles across the boundary. |
| **Accounting Software / General Ledger System** | generic ledger vs investment-aware fund books | A generic GL cannot hold the portfolio at fair value, compute NAV per class, accrue/crystallize incentive fees, or run LP waterfalls/704 allocations. FundCount's comparison table names the generic pole explicitly (Sage/NetSuite/QuickBooks + spreadsheet capital accounts). Remove the fund-specific machinery → generic accounting. |
| **Corporate Accounting / management-company books** | sibling books, different subject | Allvue ships Corporate Accounting as a separate product; the fund books and the management-company books integrate but are distinct records. |
| **Nonprofit Fund Accounting (§25)** | terminology false friend | Nonprofit fund accounting = restricted-fund ledgers for donor-restricted resources; no pooled investor capital, no NAV, no valuation machinery. Different Type entirely (already recorded by the nonprofit pass). |
| **Investor Portal** | delivery surface vs books | The LP portal is a standard adjacent surface (FundCount, Allvue both sell it separately); the books stand without it. |
| **Financial Consolidation Platform** | downstream consumer vs source | Consolidation combines entity financial statements; fund accounting produces them per vehicle and feeds the GL. |

**One-liners:** remove the books posture → PMS/IBOR; remove the fund-specific machinery → generic GL; remove the periodic close → reporting shell; add the register + dealing + investor services → fund administration; add the front office → investment management platform.

## Historical / Market-Sample Check

Paper-era form: the fund accountant's bound ledger — positions carried at cost/market by hand, capital accounts per partner updated for contributions/distributions/allocations, management and incentive fees calculated and accrued manually, NAV struck periodically on a worksheet, financial statements and partner statements typed and mailed — satisfies all three L0 legs with none of the modern machinery. Early computerized fund-accounting systems (1980s–90s portfolio accounting packages) satisfy likewise. Conclusion: the definition does not depend on cloud delivery, automated custodian feeds, AI extraction, multi-basis engines, or any specific fund regime; the open-ended fund, the closed-ended PE fund, and the asset-owner portfolio all fit the same books-and-close core.

## Uncertainties

1. **Button-level workflow not publicly documented.** No sampled vendor exposes help-center depth (exact NAV-strike steps, state names, permission models); the cycle reconstruction rests on vendor workflow diagrams and capability descriptions — strong at structure level, weak at step level. All precise operational parameters are withheld from the final document.
2. **Open-ended vs closed-ended weighting.** Open-ended mechanics (equalization, series accounting) evidenced at depth only via FundCount; classic hedge-fund administrators (SS&C fund services, Citco, Apex) were not directly reachable. Open-ended findings marked cross-check-before-generalizing.
3. **Market-usage variance.** "Fund accounting" vs "investment accounting" as marketed varies by vendor (Allvue sells both as separate products; Clearwater brands the asset-owner form "investment accounting"). The boundary drawn here is a structural judgment, not a market-usage law.
4. **Asset-owner pole inclusion.** Clearwater's product lacks investor capital accounts; it is included as the Type's asset-owner pole on the strength of the shared books+close core (daily ABOR, multi-basis, GL feeds). If the directory intends "Investment Fund Accounting" to mean only the pooled-vehicle pole, the asset-owner form would belong to a sibling "investment accounting" reading — recorded as a boundary note, not silently resolved.

## Final Synthesis

An Investment Fund Accounting system is the official books of record for investment vehicles and investment portfolios: an investment-aware general ledger in which the portfolio (positions, trades, corporate actions, income, cash) and the vehicle's capital activity post as one reconciled record; fund-specific accounting machinery (fair-value valuation, multi-book/multi-basis, multi-currency, fee accruals, and in the fund pole investor/partner capital accounts with allocation and waterfall logic); and a governed periodic close that turns the books into the vehicle's authoritative financial outputs — NAV where the regime provides, financial statements, capital statements, tax packs, and journal-ready feeds to the corporate ERP.

Around that core, mature products add automated custodian/broker feeds, reconciliation and exception workflows, tax machinery, regulatory-basis reporting, governance/audit tooling, and AI document ingestion. Packaging varies (standalone books system, module inside an investment platform, tool of fund administrators, asset-owner service); fund regime and asset class vary; the books, the machinery, and the close do not.

The Type is the middle slice of the §08 fund-operations trio: fund administration = umbrella (books + register + investor services); investment fund accounting = the books leg; transfer agency = the register leg. Keep-all-three is confirmed from this side.
