# Research Notes — Production Accounting Platform

Research date: 2026-09-09

## Research Goal

Understand what a Production Accounting Platform actually is from real products: what objects exist inside it, who uses it, how production money flows through it, what industry-specific rules shape it, and where its boundary lies against neighboring Types (general accounting software, payroll systems, production management software, budgeting tools).

## Initial Boundary Hypothesis

- The Type is the film/TV/commercial production's financial system of record: budget → actual cost capture → cost report loop.
- Nearest neighbors: Accounting Software (generic GL), Payroll System (entertainment payroll), Film Production Management (scheduling/breakdown/call sheets), Budgeting tools (Movie Magic Budgeting / Showbiz Budgeting / Hot Budget as budget-authoring poles).
- Suspected definitional core: production as financial unit + production chart of accounts + actuals coded to budget + periodic cost report with ETC/EFC/variance.

## Research Questions

1. What is the unit of record — the production, the budget, the cost report?
2. What objects exist: budget (top sheet/detail), chart of accounts, sub-accounts, POs, AP invoices, payroll invoices, journal entries, petty cash, PCards, GL, trial balance, cost report?
3. What is the operating rhythm (weekly cost report cycle)?
4. What do ETC / EFC / variance / approved overage mean and who maintains them?
5. How does payroll enter the books (timecards → hours-to-gross → payroll → GL posting)?
6. What industry rules matter: union fringes, accounting periods, effective dates, budget locks, COA mapping to studio charts and tax-credit reports?
7. Is payroll execution in-type or adjacent? Is budget authoring in-type or adjacent?
8. Where is the boundary vs generic accounting software and vs production management software?

## Representative Products

| Product | Position | Why sampled |
|---|---|---|
| GreenSlate | All-in-one cloud platform: production accounting software + entertainment payroll + incentives | Market-leading "one platform" philosophy; deep help center |
| Wrapbook | Production payroll + Production Accounting Suite (PAS), AI-assisted | Modern challenger philosophy; excellent Tier-1 docs (llms.txt index) |
| Media Services (Cast & Crew) — MediaWeb | Payroll-company-bundled SaaS production accounting | Older-generation service-bundled philosophy; payroll feed integration |
| Hot Budget (Hot Bricks) | Standalone desktop/Excel-based budgeting + actualizing tool for commercials/music videos | Budget-authoring/actualizing pole; AICP commercial world |
| Movie Magic Budgeting (Entertainment Partners) | Industry-standard budget-authoring tool | Referenced standard — both GreenSlate and Wrapbook document importing budgets from it; EP site unreachable (see Sources) |

## Sources

- GreenSlate — https://greenslate.com/ , https://greenslate.com/film-production-accounting , Help Center https://helpcenter.greenslate.com/en/ (Budget Tracking collection; "How to: Use the Chart of Accounts"; "How to: Make Cost Report Changes"; "Budget Options to Consider")
- Wrapbook — https://www.wrapbook.com/ , https://www.wrapbook.com/platform/production-accounting , Help Center https://help.wrapbook.com/ (llms.txt index; "About production accounting"; "About Budget/EFC (PAS)"; "Cost reports (PAS)")
- Media Services — https://www.mediaservices.com/ , https://www.mediaservices.com/payroll-tools/mediaweb-production-accounting-software/
- Hot Budget — https://hotbudget.com/overview/ , https://hotbudget.com/feature/
- Entertainment Partners / Movie Magic Budgeting — https://www.entertainmentpartners.com/movie-magic-budgeting/ and /movie-magic/ returned 404; homepage fetch returned empty. Movie Magic's role is evidenced indirectly: GreenSlate "How to: Import a budget from Movie Magic Budgeting" and Wrapbook "Import a project budget from Movie Magic (PAS)" both document it as the external budget-authoring standard.

## Product Observations

### GreenSlate (evidence layer: A — direct official docs)

- Positioning: "the industry's only all-in-one platform for film production accounting and payroll"; modules: Accounts Payable, Crew Expenditures, Purchase Orders, Crew & Cast Payroll; "post payroll directly to the General Ledger in one step".
- Help Center collections: Accounting (general ledger, journal entries, bank recs), Budget Tracking (chart of accounts, bank accounts, cost report), Accounts Payable (vendors, purchase orders, bills, check requests), Crew Expenditures (petty cash, pcards), Project (accounting code types, start work codes), Payroll (start work, timecards), Global (tax incentives, approval flows), Integrations (export data, publish Netflix cost reports).
- Chart of Accounts: hierarchical — header accounts with sub-accounts; options: Show All Projects, Show Sub Accounts, Show Uncommitted POs, Show Inactive, Suppress Zeros, Negative ETCs, Negative EFCs, Show YE; location/episode code filters; click an account number to open its General Ledger; export PDF/Excel.
- Cost Report: editable ETC/EFC/Budget/Approved Overage columns; changes require an effective date ("any future changes must use an effective date equal to or greater than the previous change") and a reason per change; preview before submit; budget lock concept ("If the budget is not locked, the budget column will be editable"); ETC↔EFC auto-update; approved overage entered manually and EFC updated to reflect it; multi-budget cost reporting by location/episode with collapsible rollups; custom views/groupings.
- Budget options: sub-accounts required for budgeting (header/rollup accounts hold totals only, no costs posted; default "00" sub-account catches uncoded costs and payroll import); multiple budgets via location/episode codes (each transaction coded to a budget); enforced vs non-enforced location (enforced = every transaction must carry exactly one location; non-enforced = one transaction may span locations, and per-location trial balance is unavailable).
- Budget import from Movie Magic Budgeting documented.
- Tax incentives: Tax Credit Module, account mapping for GA/NY tax credit reports, incentives dashboard/calculator.
- Bank accounts: positive pay, ACH, CASHét Pay; multi-currency pro tips.

### Wrapbook (evidence layer: A — direct official docs)

- Positioning: "production payroll, spend, and accounting in one AI-powered system"; modules: Onboarding, Payroll, Accounts Payable (cost tracking), Production Accounting, Data Insights.
- Production Accounting Suite (PAS) features: Budget/EFC tracker; vendor management and payments; PO, AP, and payroll invoice management; journal entries, posting, and bank reconciliation; accounting reports including GL, trial balance, and cost reports.
- Explicit FAQ definition: "Production accounting refers to the management of film and TV production finances through a centralized system."
- PAS vs Cost tracking distinction (vendor's own boundary): PAS = centralized management of production finances (budget tracking, vendor management, payroll invoice management, GL); Cost tracking/Payables = lighter reporting comparing committed, actual, and estimated final costs without the full GL.
- Budget/EFC: project budget contains anticipated costs — worker wages and fringes, rentals, location fees, other expected expenses; Budget/EFC dashboard reviewable by period or effective date; EFC = "a number that updates based on actual costs incurred against the budget"; budget import from Movie Magic; budget lock; budget overages; fringes and fees added to budget; episodic projects typically have one budget per episode.
- Cost report: "compares budgets to actual expense transactions, including purchase orders (POs)"; types: summary, detail, combined, episodic summary, episodic detail; columns: Account, Description, Period actuals, Actuals to date, POs, Total to date, ETC, EFC, Budget, Approved overages, Total budget, Variance, Period variance, % complete; filters: period range, transaction date, posted date, ACCT numbers, LO (location), PRD (production), SET, FF1 (free field); effective-date reporting for POs (report shows PO state as of a selected date); export PDF/XLSX/CSV; templates; AI natural-language report filtering ("type in what you're looking for… AI applies the right filters to your general ledger").
- Vendor glossary (from help articles): Cost report = "A detailed weekly report that summarizes cost compared to budget… organized by department and reflects cost analysis in terms of current week's spend, actual spend to date, PO commitments, estimate to complete (ETC), current estimated final cost (EFC)… and any overages (approved or not), and overage/underage detail by account." PO = "A financial document committing the production to expenditure… sent for approval and, once approved, allows for the vendor to be paid." GL = "Original and detailed book of record for all accounting transactions arranged by departmental account codes that occurs throughout the lifetime of a production." Chart of Accounts = "The master list of all the accounts used to track production costs… In commercials, typically AICP line numbers are utilized in its stead." Trial balance = "The summary statement of all accounts in the general ledger. This document accompanies the weekly Cost Report."
- Transactions: AP invoices (add, post, reverse; direct ACH vendor payments; paper checks; NACHA; approval workflows; cover sheets & approval attestation; urgent flag); journal entries (add, post, reverse; bulk PCard JEs); PCards; petty cash (add funds, distribute, document purchases); payroll invoices (auto-coded timecards/expenses/fringes when payroll is funded; split/merge distribution lines; tag payroll transactions; post to GL).
- Controls: permission-based access (Company Admin / Accountant roles); accounting periods can be closed (no self-serve reopen); approval workflows configurable per studio/network/production; audit log.
- Payroll side: startwork, timecards (day types, work zones, meal breaks, overtime, allowances), hours-to-gross, union compliance (SAG-AFTRA/IATSE/DGA/WGA/Teamsters), fringes, payroll funding, payroll register/edit reports; "Export a payroll log to Hot Budget".
- Projects have statuses: Active, Wrapped, Draft.

### Media Services — MediaWeb (evidence layer: A — direct official product page)

- "Production Accounting Software for Film, TV and New Media" — feature film, TV series, streaming, webisode, branded content, sports media.
- True SaaS production accounting platform — no local install required.
- Cost reporting optimized for production as well as stakeholders.
- Automated payroll feed from Media Services payroll.
- Import purchase card data from Cashet or PEX.
- Create multiple budgets for each production.
- Dozens of standard and custom reports; unlimited file attachments; ACH payments to production vendors.
- Free for Media Services production payroll clients (service-bundled model).
- Sibling tools: Digital Purchase Order (DPO), Purchase Cards for Crew, Mobile Timecards, TiM Digital Onboarding; Showbiz Budgeting 10 (cloud-collaborative budgeting), Showbiz Timecards (hours-to-gross with union rules).

### Hot Budget (evidence layer: A — direct official site)

- Budgeting software for commercials, promos, music videos; AICP-standard templates (e.g., "Commercial 9-16-459 AICP", post production, animation templates with page/section/line counts).
- Original Budget / Running Budget / Actual Budget viewed simultaneously; "An integrated running budget can be directly compared to the original budget to identify variances as a project evolves. Actual costs can be logged and compared directly to the original budget, and running budget."
- Logs: Purchase Order Log, Petty Cash Log, Payroll Log; import timecard batch CSVs into the payroll log; port logs between files.
- Contingencies on the cost summary page; fringe isolation (below-the-line P&W configuration); overtime calculator; travel budget; currency conversion; PDF output of budgets.
- Excel/VBA-workbook based (relaunch recovery for "excel visual basic failure"); desktop download + license.
- Users named: bidders, executive producers, producers, production managers, production coordinators, post staff, accountants.

### Movie Magic Budgeting (evidence layer: A− — indirect via import documentation)

- Both GreenSlate and Wrapbook document importing budgets from Movie Magic — it is the budget-authoring standard whose output seeds the accounting platform's budget of record.
- Entertainment Partners' own product pages were unreachable (404 / empty fetch) — direct observation limited to the import paths.

## Cross-product Comparison

| Structure | GreenSlate | Wrapbook PAS | MediaWeb | Hot Budget | Verdict |
|---|---|---|---|---|---|
| Production/project as financial container | Project + accounting code types | Projects (Active/Wrapped/Draft) | Per-production books | Per-project workbook | Universal → L0 |
| Budget of record on a production chart of accounts | Chart of Accounts (header/sub-accounts) | Budget/EFC + COA + line numbers | Multiple budgets per production | AICP templates / cost summary | Universal → L0 |
| Actual cost transactions coded to accounts | AP bills, POs, petty cash, pcards, payroll → GL | AP invoices, POs, JEs, PCards, petty cash, payroll invoices → GL | Payroll feed, pcard import, ACH | PO/Petty Cash/Payroll Logs | Universal → L0 |
| Budget-vs-actual comparison report with ETC/EFC/variance | Cost Report (editable ETC/EFC/overage) | Cost report (ETC/EFC/variance/% complete) | "Cost reporting optimized for production" | Original/Running/Actual side-by-side | Universal → L0 |
| General ledger as book of record | Searchable/editable GL | GL web view + reports | implied ("dozens of reports") | absent (logs only) | Common (full GL) — Hot Budget pole lacks it |
| PO commitment tracking | Show Uncommitted POs; PO module | POs in cost report; effective-date PO history | DPO tool | PO Log | Universal → L1 (commitment concept L0-adjacent) |
| Payroll execution in-product | Yes (crew & cast payroll) | Yes | Bundled payroll service | No (imports payroll logs) | Common, NOT definitional |
| Petty cash + purchase cards | Crew Expenditures | Petty cash + PCards | Cashet/PEX import | Petty Cash Log | Universal → L1 |
| Journal entries / posting / bank rec / trial balance | Yes | Yes | implied | No | Common → L1 |
| Approval workflows | Digital approval flows | Configurable approvals (PO/AP/timecard/payroll) | — | — | Common → L1 |
| Effective dates + change reasons on budget/EFC edits | Yes (enforced ordering) | Period/effective-date views | — | — | Common → L1 |
| Accounting period close | implied (bank rec) | Yes (closed periods) | — | — | Common → L1 |
| Multi-budget (episodes/locations) | Location/episode codes, enforced option | One budget per episode; episodic reports | Multiple budgets | — | Common → L1 |
| COA mapping to external charts (studio/tax credit) | GA/NY tax credit mapping; map COA for cost reporting | COA Mapping (PAS); show native accounts | — | — | Common → L2 (stakeholder-dependent) |
| Tax incentive coding/tracking | Tax Credit Module, incentives dashboard | Incentives service + coding cheat sheet | Incentives service | — | Common → L2 (region-dependent) |
| Multi-currency | Yes | Yes | — | Currency converter | Common → L2 |
| Budget authoring in-product | Import from Movie Magic | Create/duplicate/import budgets | Create budgets | Primary purpose | Variant axis |
| AI assistance | — | Code Assist, AI report filtering | — | — | Vendor-era → L2/L3 |
| Excel substrate | No | No | No | Yes (VBA workbooks) | Variant |

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures:

1. **The production as the financial unit of record** — a bounded, identified media production (film, series, episode, commercial, etc.) with its own books; budget, transactions, and reports all belong to a production, and the production's lifecycle (setup → shoot → wrap) bounds the accounting. Remove → generic accounting software.
2. **The production budget as the financial plan of record** — the anticipated cost of the production organized by the production's chart of accounts (cost accounts arranged by department/section). Remove → bookkeeping with no plan to hold costs against.
3. **Actual cost capture coded to the budget** — every cost the production incurs (vendor invoices, purchase orders, payroll, petty cash, card spend, adjustments) is recorded as a transaction coded to budget accounts, accumulating into the production's general ledger. Remove → budgeting tool only.
4. **The budget-vs-actual control loop (cost report)** — a recurring report comparing, per account: budget, actuals to date, committed POs, estimate-to-complete, estimated final cost, and variance — with the accountant maintaining EFC/overages through controlled, dated, reasoned changes. Remove → GL bookkeeping without production cost control.

Jointly-held load-bearing: (1) alone = generic accounting; (2) alone = budget spreadsheet; (3) without (2) = bookkeeping; (4) without (1)–(3) = a spreadsheet comparison with no books.

### L1 — Common Mature Structure

- Chart of accounts with departmental hierarchy and sub-accounts; header/rollup accounts as totals
- PO commitment tracking (committed vs actual; uncommitted-PO visibility)
- Payroll as a coded cost stream (timecards → hours-to-gross → payroll → posted to GL as payroll invoices/distribution lines)
- Petty cash and purchase cards as crew expenditure channels
- Vendor management and payment execution (checks, ACH)
- Journal entries, posting, bank reconciliation, trial balance
- Configurable approval workflows (POs, invoices, timecards, payroll)
- Effective-date + reason discipline on budget/EFC changes; budget locks; accounting period close
- Multi-budget structures (episodes/locations) with enforced coding options
- Report templates, PDF/Excel export, drill-down from account to ledger to transaction

### L2 — Variant / Optional Structure

- Payroll execution in-product vs bundled payroll service vs external payroll feed
- Budget authoring in-product vs import from dedicated budgeting tools (Movie Magic)
- COA mapping to studio/network charts and tax-credit report formats
- Tax incentive tracking/coding (region-dependent)
- Multi-currency for international productions
- Episodic budget/report structures (one budget per episode)
- Commercial-world AICP line numbers in place of feature/TV account codes
- AI assistance (account-code suggestions, natural-language report filtering)
- Contingency and overage-approval machinery depth
- Excel-substrate tooling (Hot Budget pole) vs SaaS platform

### L3 — Vendor-specific (research notes only)

- Wrapbook: PAS vs Cost tracking product split; Code Assist; AI GL filtering; CASHétPay; urgent-flag workflow; NACHA payments
- GreenSlate: CASHét Pay bank setup; Netflix cost report publishing; Alteryx collections; GA/NY tax credit templates; sub-account masks ("00" defaults)
- Media Services: MediaWeb free-with-payroll bundling; Cashet/PEX pcard import
- Hot Budget: VBA framework, relaunch recovery, budget porting, AICP template library, Hot Bricks ecosystem

## Vendor-specific Findings

- Wrapbook explicitly distinguishes its full PAS from its lighter "Cost tracking" module — evidence that the market itself recognizes a depth axis (cost reporting vs full GL) inside the same Type.
- GreenSlate's enforced/non-enforced location option and sub-account requirement show how coding discipline is configurable per production.
- MediaWeb's "free for payroll clients" shows the service-bundled commercial model, not a structural difference.
- Hot Budget's simultaneous Original/Running/Actual view is the budgeting-pole realization of the same comparison loop.

## Boundary Findings

- **vs Accounting Software (generic)**: generic accounting centers on the going concern's full financials (revenue, AR, company-wide COA). Production accounting centers on a temporary production entity, a production-specific cost-account chart, and the budget-vs-actual cost report loop; the production wraps and the books close. Remove the production-bounded budget/control loop → generic accounting territory.
- **vs Payroll System / Entertainment Payroll**: payroll processing (taxes, paymasters, union rules, pay stubs) is its own machinery. In sampled products it is commonly bundled, and its output enters the books as coded payroll cost — but Hot Budget satisfies the Type with payroll only as an imported log, and MediaWeb treats payroll as a sibling service. Payroll execution is therefore common-mature, not definitional.
- **vs Film Production Management** (scheduling, breakdown, call sheets): different object world (shoot days, scenes, crew scheduling) and no budget-vs-actual loop. Remove the money loop → production management territory.
- **vs Budgeting tools (Movie Magic Budgeting, Showbiz Budgeting)**: budget authoring is a neighboring capability; accounting platforms import budgets from them, and the budgeting pole (Hot Budget) lacks the GL. The accounting platform's defining addition is actuals + books + the control loop.
- **vs Budgeting & Forecasting Platform (corporate FP&A)**: different unit (production vs enterprise), different rhythm (weekly cost report during production vs monthly/quarterly forecast cycles), different objects (POs, petty cash, timecards vs scenarios/drivers).
- **"去掉什么就变成另一个 Type" 判据**: remove the production container → generic accounting; remove the budget of record → bookkeeping; remove actuals → budgeting tool; remove the cost-report loop → GL without control; remove the industry coding (cost accounts, fringes, POs) → generic expense tracking.

## Uncertainties

- Movie Magic Budgeting's current cloud capabilities could not be verified directly (EP pages unreachable); its role as budget-authoring standard is evidenced only through import documentation at two vendors.
- MediaWeb's full feature depth (GL editing, period close, EFC mechanics) is documented only at marketing-page depth; its help center was not reachable in this pass. Assertions about MediaWeb are kept at the level of its published feature list.
- Whether every production accounting platform supports formal accounting-period close is unverified beyond Wrapbook (direct) and GreenSlate (bank rec implied).
- Residuals processing appears as an adjacent service at GreenSlate/Media Services; whether any platform embeds residuals in the accounting core was not researched.
- The exact industry-standard account-number ranges (e.g., 1000–5000 series) were observed only as examples (1001 STORY, 1101 WRITER, 1201 PRODUCER at Wrapbook; 1100 header at GreenSlate); no canonical numbering is claimed.

## Final Synthesis

A Production Accounting Platform is the production's financial system of record: it holds the production's budget on a production chart of accounts, captures every actual cost as coded transactions accumulating into the production's general ledger, and runs the recurring budget-vs-actual control loop — the cost report with ETC/EFC/variance — through which the production accountant keeps the estimated final cost honest until wrap. Payroll execution, budget authoring, tax incentives, and stakeholder chart mapping are common mature or variant capabilities layered around that core, not the core itself.
