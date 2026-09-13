# Research Notes — Expense Tracking Application

## Research Goal

Identify the smallest stable invariant that defines the **Expense Tracking Application** Application Type (DIRECTORY §08 Finance, line 608), and place every other observed capability at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation (official source for a specific product)
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Expense Tracking Application (DIRECTORY §08 Finance, Banking, Insurance & Investment)

Nearest confusing Types:

- **Budgeting Application** (§08 sibling, unprocessed) — plan-first allocation vs record-first tracking
- **Personal Finance Management Application** (§08 sibling, processed 2026-09-06) — whole-picture money overview vs spending slice; PFM's STATUS entry already holds Expense Tracking as a "subset sibling … held on structural removal tests"
- **Net Worth Tracker** (§08 sibling, unprocessed) — position (assets − liabilities) vs flow (spending)
- **Expense Management Platform** (§08 sibling, unprocessed — a prior batch run FAILED per batch.log) — corporate expense reports/reimbursement vs personal record
- **Spend Management Platform / Corporate Card & Spend Platform** (§08 siblings, unprocessed) — organization-side spend
- **Bookkeeping Application / Accounting Software** (§08, processed) — books semantics vs no books semantics; bookkeeping's STATUS entry records the seam as "Expense Tracking (no books semantics)"
- **Digital Banking / Mobile Banking Application** (§08) — a bank app's spending view is a capability of the account relationship, not a standalone personal record system

Working hypothesis:

> An expense tracking application records individual money-out events as classified records and aggregates them over time so the user can see where their money goes.

Key uncertainties at start:

1. Is **categorization** definitional, or merely universal practice? (Historical check needed.)
2. Are **accounts/wallets** definitional (as in PFM) or optional organization?
3. Are **budgets** definitional or the adjacent Budgeting Type's core leaking in?
4. Does the Type include **income**, or is it strictly money-out?

## Research Questions

1. What is the smallest object model without which a product is no longer recognizable as an expense tracker?
2. Where do Expense record / Category / Tag / Account / Budget / Income / Recurring entry / Receipt / Report sit in the L0–L3 hierarchy?
3. How do capture mechanisms vary (manual quick-entry, bank sync, file import, receipt photo), and is any of them definitional?
4. What review/aggregation surfaces does the Type reliably expose (period totals, category breakdowns, trends, "left to spend")?
5. What is the structural boundary with Budgeting Application, PFM, Expense Management Platform, Bookkeeping/Accounting, and bank-app spending views?
6. Do older / analog / platform-native / differently-positioned products (paper expense diaries, desktop personal-finance products, aggregation-era web products) still fit the definition?

## Representative Products

| Product | Why selected | Docs accessed |
|---|---|---|
| Toshl Finance | mature cross-platform expense tracker; manual-first with optional bank sync; **public API documentation** exposes the full object model (Tier 1) | yes (developer.toshl.com docs: overview, entries, categories, budgets, accounts; toshl.com positioning page; official tutorial "How to Add and Track Expenses, Incomes and Transfers") |
| Wallet by BudgetBakers | sync-first aggregation philosophy; ML auto-categorization; family positioning | yes (budgetbakers.com product pages + "How to Start" guide; support.budgetbakers.com timed out ×2 — abandoned) |
| Money Lover | manual-first simple tracker; travel/multi-currency emphasis; debt/savings modules | yes (moneylover.me product page; support.moneylover.me transport error ×2 — abandoned) |
| Money Manager (Realbyte) | bookkeeping-flavored personal tracker (double-entry, asset graphs); different structural emphasis | yes (realbyteapps.com product page; help.realbyteapps.com transport error ×2 — abandoned) |

Products attempted and abandoned per the network-failure rule (1–2 failures → abandon, no memory-fill):

- **Spendee** — spendee.com and spendee.com/help timed out ×2
- **Monefy** — monefy.app timed out; www.monefy.app is a parked domain
- **PocketGuard** — pocketguard.com returned HTTP 403

Boundary-context products (positioning widely attested; **no product-specific claims made**, official docs not fetched): Expensify-class corporate expense-report products, YNAB-class budget-first products, GnuCash-class personal double-entry accounting, Quicken/Mint as historical market anchors, bank apps' built-in spending views.

## Sources

Research date: **2026-09-06**

Directly fetched official sources (Layer A evidence):

- Toshl Developer — API Overview (endpoint map): https://developer.toshl.com/docs/
- Toshl Developer — Entries: https://developer.toshl.com/docs/entries/
- Toshl Developer — Categories: https://developer.toshl.com/docs/categories/
- Toshl Developer — Budgets: https://developer.toshl.com/docs/budgets/
- Toshl Developer — Accounts: https://developer.toshl.com/docs/accounts/
- Toshl — positioning page ("Personal finance, budget and expense tracker app"): https://toshl.com/
- Toshl — official tutorial "How to Add and Track Expenses, Incomes and Transfers (Web App)": https://toshl.com/blog/how-to-track-expenses-incomes-and-transfers-web-app/
- BudgetBakers — homepage (Wallet / Board / ShareCost / AISP product map): https://budgetbakers.com/
- BudgetBakers — "How To Start" guide (day 1 / week 1 / month 1 flow): https://budgetbakers.com/en/how-to-start/
- Money Lover — product page: https://moneylover.me/
- Money Manager (Realbyte) — product page: https://realbyteapps.com/

Source-access Limitation (per `WORKFLOW_v1.1.md §23`):

- support.budgetbakers.com, help.realbyteapps.com, support.moneylover.me: unreachable (timeouts/transport errors ×2 each) → help-center-level operational detail for those three products is **not** asserted; their evidence is calibrated to official product/positioning pages (Tier 2).
- toshl.com/faq: HTTP 403 → consumer FAQ not used; Toshl evidence rests on its developer API docs + official tutorial instead (stronger sources).
- Spendee, Monefy, PocketGuard: unreachable → retained only as market-context names, zero claims.
- No precise vendor numbers (bank-connection counts, prices, user counts, free-tier limits) are carried into the final document; vendor-claimed figures observed (e.g. "15,000 banks", "20M+ downloads") are recorded here as L3 marketing claims only.

## Product Observations

### Toshl Finance (Layer A — official API docs + official tutorial + positioning page)

**Object model (API docs):**

- **Entries** endpoint "can be used to interact with users expenses and incomes. Expenses have a negative prefix, incomes don't have a prefix. Every entry is part of an account, is in one category, *can* have tags, *can* be part of a repeat, *can* be part of a transaction and *can* include images."
- Entry properties: signed `amount`; `currency` (ISO 4217, with exchange rate vs account currency and vs user's main currency); `date`; `desc`; `account` (required); `category` (exactly one); `tags` (array); `location` (lat/long, Foursquare venue id); `repeat` (RFC 5545 RRULE: start/end/frequency/interval/count/byday; template + iteration; automatic/confirm/confirmed detection); `transaction` (paired companion entry — "a transfer of funds from one account to the other"; editing one side auto-updates the companion); `images` (up to 4, pro-gated — free tier gets 403); `reminders` (up to 5, period/number/at-time); `import` provenance (bank import or file import: memo, payee, `pending` flag); `review` link (types: expense, income, transfer, repeat; completed flag); `split` (parent/children — "created by splitting up another" entry); `completed` ("if the bill has been paid… reminders no longer fire").
- **Categories**: `name`, `type` (`expense`, `income`, `system`), usage counts (entries, tags, budgets), **merge** operation, dedicated **sums** endpoint. Preset categories exist ("name_override (deprecated) — is true if name is overriden with a custom name" implies a preset set).
- **Tags**: own endpoint with merge + sums; cross-cutting labels (many per entry).
- **Accounts**: `name`, `balance` (calculated), `initial_balance`, `type` (`custom, depository, credit_card, loan, mortgage, brokerage, investment, savings, other`), `limit` (credit limit), per-account median/avg expense & income stats, `goal` (savings goal with amount/start/end), `connection` (bank-sync status: connected/disconnected/inactive/error), `settle`/`billing` (credit-card cycle days), move/reorder/merge operations. Free-tier account-count limit (403 on exceeding).
- **Budgets**: `limit`, calculated `amount` (spent so far), `planned` (expenses that will fall in after today), `median` (history), `rollover` (carry unspent remainder to next period), `recurrence` (one-time/daily/weekly/monthly/yearly), `type` (`regular`, `delta` = monthly ±, `percent` = % of monthly income), scope by included/excluded **categories, tags, accounts**; status active/inactive/archived; budget history endpoint. Constraint: "Only one active monthly budget for all expenses can exist at any one time" (403 on second general monthly budget); free-tier limit of 3 budgets (403 on third).
- **Aggregation surfaces**: `entries/sums`, `categories/sums`, `tags/sums`, `entries/timeline`, `me/summary`; **Reports** (create/update/**send**); **Exports**; **Planning** endpoint.
- **Bank ingestion**: bank institutions (list/popular/countries), bank connections (create/refresh/re-auth), bank imports (file imports).
- **Me**: settings, devices, **shares** (share with another user), notifications, payments (subscription).

**User-facing capture flow (official tutorial):**

- "For a basic expense all you need to do is: **enter the amount**, **select a category** and **click Save**."
- "Assigning a category is required for every entry." Preset categories cover most cases; user can add custom ones inline; same for tags.
- Required info: "the amount, category, account and date – has already been entered or pre-set."
- Tags: "Unlike the categories which are limited to one per entry, multiple tags can be assigned"; tags auto-sorted by selected category and by frequency of use.
- Accounts: "This option is displayed only if you use more than one financial account… When you sign up with Toshl, a Cash account is added automatically."
- Date: defaults to today; "Any entries set in the future will be grouped as 'planned' and displayed on top of the expense list."
- Advanced options: location, description, repeats, reminders, photos (repeats/reminders/photos pro-gated).
- Save → "the expense will appear in the expense lists, graphs and other sums."
- Edit / **duplicate** / delete from the entry detail.
- **Transfers**: "you can also record a money transfer between two financial accounts… there are no categories or tags"; ATM withdrawal example = transfer from card account to cash; shown with a special two-arrows icon.

**Positioning page:**

- Title: "Personal finance, budget and expense tracker app"; "Track all your cards and cash in one place. Connect your financial accounts, or enter expenses using our quick and slick Toshl apps."
- Three entry paths: bank connections / "4 quick taps to add an expense or income" / file import ("8 file import formats supported in the web app").
- Review surfaces: "River flow" (money in/out over a period), "Monthly overview" ("compare how much you spent to the time already passed in the month… you'll know exactly how much you have Left to spend"), "Planning" (longer periods, "the growth of your net worth"), "Expenses" graphs ("Break it down by category, tag and discover where your hidden money sinkholes lie"), "Locations" ("the sum of your spending per store, restaurant or bar").
- Audience pages in footer: business expense reports, digital nomad finances, freelancers finances, family finances.

### Wallet by BudgetBakers (Layer A for positioning/flow pages; help center unreachable)

- Positioning: "Wallet — Personal & Family Finance Manager… smart budgeting, expense tracking, and bank synchronization"; "Wallet is all your money in one app."
- "How To Start" guide structures onboarding in three phases:
  - **First Day — Add Your Accounts**: "Choose from over 15,000 banks and providers; Upload Transaction History; Wallet will automatically categorize spending." Outcomes: "Balance: See how much money you have; Cash Flow: Spend less than you earn; Spending: See where your money goes; Credit limit: Use credit responsibly."
  - **First Week — Aggregate All Accounts**: "Add as many financial accounts as you own; Label Your Transactions; Machine learning algorithms learn your finances." Outcomes: monitor all balances in one place, cash-flow trends, "Sort: By category or payee", "Automate: Labeling works automatically."
  - **First Month — Set Up Budgets & Planning**: "Start predicting finances weeks ahead; Enrich Your Categories; Create detailed spending categories." Outcomes: "Plan: See future cash flow; Predict: Spot issues before they happen."
- "Pro Tips": "Review Daily — Spend 2 minutes each day reviewing transactions to keep categories accurate"; "Set Realistic Budgets — Base budgets on actual spending history, not wishful thinking"; "Use Analytics — Check weekly and monthly reports to understand spending patterns"; "Enable Notifications — Stay informed about unusual transactions and budget alerts."
- Vendor-claimed stats (L3): 14M+ downloads, 15K+ bank connections, 50 languages, ISO 27001/GDPR.
- Sibling products (L3): Board (small-business cash flow), ShareCost (split expenses with groups), AISP (banking API platform), MCP AI assistants, REST API.

### Money Lover (Layer A for product page; support site unreachable)

- Self-description: "No.1 Expense Manager Budget Planner"; "Simple way to manage personal finances."
- "Simple money tracker: It takes seconds to record daily transactions. Put them into clear and visualized categories such as Expense: Food, Shopping or Income: Salary, Gift."
- "Painless budgeting" (budget feature).
- "The whole picture in one place: One report to give a clear view on your spending patterns. Understand where your money comes and goes with easy-to-read graphs."
- Features: "Multiple devices — safely synchronize across devices"; "Recurring transaction — get notified of recurring bills and transactions before due date"; "Travel mode — all currencies supported with up-to-date exchange rate"; "Saving plan — keep track on savings progress to meet your financial goals"; "Debt and loan — manage your debts, loans and payment process in one place"; "Effortless transaction entry — manually or automatically."
- User review quoted on page: household use ("my husband and I use it to track all our expenses and income… household accounts and budget").

### Money Manager / Realbyte (Layer A for product page; help center unreachable)

- Self-description: "Money Manager Expense & Budget — The easiest way to manage personal finances."
- Features: "Weekly, Monthly total and budgets are provided"; "Photo Save — save receipt or memories together"; "Reinforced Filter — review your transactions with more filtering options"; "Improved Calendar Visuals — review all your monthly transactions in one place"; "Aesthetically Improved Charts — review your expenses with improved and well-organized charts"; "**Easier Double-entry Booking — manage your savings, insurance, loans and real-estate**"; "Advanced Budget Feature — set a monthly budget for each category"; "Asset Graphs — review asset trend in your chart."
- Vendor-claimed stats (L3): 20M+ downloads, Editors' Choice.

### Historical / market-sample breadth (Layer B / widely-attested only — no product-specific claims)

- **Paper expense diaries/ledgers** (analog era): dated amounts, a named purpose per line, tallies per category per period. The analog practice already combines record + classification + periodic tally — the L0 candidate predates software.
- **Desktop-era personal finance products** (Quicken/Microsoft Money class, widely attested): manually entered or statement-imported transactions, expense categories, category reports. Fits the candidate L0; capture mechanism differs (L2).
- **Aggregation-era web products** (Mint class, widely attested): bank-fed transactions auto-categorized into spending breakdowns and trends. Fits; capture mechanism differs (L2).
- **Bank-app spending views** (capability, not a Type): categorize and break down the spending that passes through that one bank relationship; no cross-bank/cash capture, no user-owned continuous history independent of the account relationship. Treated as a capability inside the Banking Application Types, not a counterexample.
- **Personal double-entry accounting** (GnuCash class, widely attested): has expense accounts and reports but centers on books semantics (chart of accounts, balanced posting, statements) → sits on the Bookkeeping/Accounting side of the boundary, not a counterexample.

## Cross-product Comparison

| Finding | Toshl | Wallet (BudgetBakers) | Money Lover | Money Manager (Realbyte) | Abstraction level |
|---|---|---|---|---|---|
| expense recorded as an individual dated amount event | yes (entry, signed amount, date) | yes (transactions) | yes ("record daily transactions") | yes (transactions) | **L0** |
| classification into spending categories | yes (**required**, exactly one; presets + custom) | yes (auto-categorize; "enrich your categories"; sort by category) | yes ("clear and visualized categories") | yes (per-category budgets presuppose categories) | **L0** |
| aggregated view over time (period totals, category breakdowns, trends) | yes (sums, graphs, monthly overview, reports) | yes (analytics, weekly/monthly reports, trends) | yes ("one report… easy-to-read graphs") | yes (weekly/monthly totals, charts) | **L0** |
| income records alongside expenses | yes (entries = expenses + incomes) | yes (cash flow "spend less than you earn") | yes (Income: Salary, Gift) | yes (implied by totals/budget framing) | L1 |
| accounts/wallets as optional containers | yes (required field but auto Cash singleton; hidden when only one) | yes (central — "add your accounts", aggregate all) | yes (wallets) | yes (asset accounts) | L1 |
| transfers between own accounts (not expenses) | yes (paired entries, no category) | yes (implied by multi-account aggregation) | not observed on fetched page | not observed on fetched page | L1 |
| budgets with spent-vs-limit comparison | yes (limit/amount/planned/rollover, per category/tag/account scope) | yes ("set up budgets", budget alerts) | yes ("painless budgeting") | yes ("monthly budget for each category") | L1 |
| recurring entries + reminders | yes (RRULE repeats, reminders, completed flag) | yes (planning/predict future cash flow) | yes (recurring + due-date notifications) | not observed on fetched page | L1 |
| receipt photos / attachments | yes (up to 4 images, pro-gated) | not observed on fetched pages | not observed on fetched page | yes ("Photo Save") | L1 |
| reports & export | yes (reports create/send; exports) | yes (weekly/monthly reports) | yes (report page) | yes (charts) | L1 |
| capture assistance (auto-categorization / rules / ML) | yes (repeat detection, review queue for imports) | yes (ML learns labeling) | yes ("manually or automatically") | not observed | L1 |
| notifications (budget alerts, unusual transactions, due dates) | yes (reminders; notifications endpoint) | yes (budget alerts, unusual transactions) | yes (due-date notifications) | not observed | L1 |
| bank sync / aggregation | yes (optional: bank connections + file imports) | yes (core posture) | yes ("automatically") | not observed | L2 (capture posture) |
| multi-currency + exchange rates | yes (per-entry currency + rates) | not observed on fetched pages | yes (travel mode) | not observed | L2 |
| locations / per-merchant spending | yes (location object, per-store sums) | not observed | not observed | not observed | L2 |
| expense splitting | yes (split parent/children) | sibling product ShareCost (separate) | not observed | not observed | L2 |
| shared/household use | yes (me/shares endpoint) | yes ("Personal & Family") | yes (household review quote) | not observed | L2 |
| savings goals | yes (account goal object) | not observed | yes (saving plan) | not observed | L2 |
| debt/loan tracking | yes (account types loan/mortgage) | not observed | yes (debt and loan module) | yes (double-entry booking for loans/real-estate) | L2 |
| double-entry / asset-position emphasis | no (flow-oriented) | no | no | yes (variant flavor) | L2 (variant posture) |
| planned (future-dated) entries held separately | yes ("grouped as planned") | yes (predict future cash flow) | not observed | not observed | L1 |
| surface: mobile app / web app / desktop | mobile + web | mobile + web | mobile | mobile | L2 (surface) |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as an expense tracking application:

```text
Expense record (money-out event: amount + date + what it was for)
└── Spending categories (user-manageable classification of records)
    └── Aggregated view over time (period totals, category breakdowns, trends)
```

Removal tests:

- remove the *expense record* → there is nothing being tracked; not the Type
- remove *categorization* → a bare dated transaction list (a bank-statement register); the Type's core question — "where does my money go?" — loses its answering structure
- remove the *aggregated view* → a log with no tracking; the user cannot see where money goes

§24 historical check: the paper expense diary (dated amounts + named purpose + periodic tally), the desktop-era personal-finance product (categories + reports over manual/imported transactions), and the aggregation-era web product (auto-categorized bank spending) all satisfy the three properties. No era-, platform-, or capture-specific mechanism is definitional. Therefore manual entry, bank sync, receipt OCR, mobile-first surfaces, and cloud storage are all **L2**, not L0.

## L1 — Common Mature Structure

Common across the researched sample (all four products document them); they make tracking practical but do not define the Type:

```text
Income records (mirror of the expense record; enables a cash-flow view)
Accounts / wallets as optional containers (cash, cards, bank; balances)
Transfers between own accounts (recorded as transfers, not expenses)
Budgets on categories/periods with spent-vs-limit comparison and rollover
Recurring entries (bills, subscriptions, salary) + reminders + planned state
Receipt photos / attachments
Reports, charts, export
Capture assistance (auto-categorization, rules, ML labeling, import review)
Notifications (budget alerts, unusual transactions, due dates)
Planned vs actual separation (future-dated entries held as planned)
```

## L2 — Variant / Optional Structure

Presence or absence does not change the Type:

```text
Capture posture: manual-first ↔ bank-sync-first ↔ file-import ↔ receipt-photo/OCR
Multi-currency with exchange rates (travel emphasis)
Locations / per-merchant spending analysis
Expense splitting (item-level or group split; group-billing siblings)
Shared/household wallets and shared access
Savings goals
Debt/loan/mortgage tracking depth
Asset-position emphasis (double-entry flavor, asset graphs) — drifts toward bookkeeping
Investment/brokerage account types
Surface: mobile / web / desktop; local storage vs cloud sync
Gamification / engagement layers
```

## L3 — Vendor-specific Structure

Remains in Research Notes only:

- **Toshl**: signed-amount entry model (expenses negative, incomes positive); exactly-one-category rule enforced at entry; RRULE-based repeats with automatic detection/confirmation; transaction = paired auto-updating entries; review queue for imported entries (types expense/income/transfer/repeat); "river flow" visualization; "Left to spend" monthly framing; locations with Foursquare venue ids; credit-card settle/billing cycle fields; account types incl. brokerage; budget types regular/delta/percent; single-general-monthly-budget constraint; free-tier limits (3 budgets, account count, image gating); 8 file-import formats; monsters gamification; me/shares sharing; planning endpoint.
- **Wallet (BudgetBakers)**: "15,000 banks" / "15K+ bank connections" claims; ML labeling that "learns your finances"; day/week/month onboarding framing; sibling products Board (small-business cash flow), ShareCost (group expense splitting), AISP open-banking platform; MCP AI assistants.
- **Money Lover**: "No.1 Expense Manager Budget Planner" positioning; travel mode; debt & loan module; saving plans; vendor user-count claims.
- **Money Manager (Realbyte)**: "Easier Double-entry Booking" for personal savings/insurance/loans/real-estate; asset graphs; Editors' Choice badge; vendor download claims.

## Rejected Findings

- **"Budgets are definitional"** — rejected. Budgeting is the adjacent Budgeting Application Type's core (plan-first allocation). All four sampled products include budgets, but the paper-era and minimal-manual analogs satisfy the L0 without any budget object; budgets are L1 despite near-universality in the modern sample. (Anti-overfitting rule: shared implementation across the sample ≠ defining invariant.)
- **"Bank sync is definitional"** — rejected. Manual-first capture (Toshl's manual mode, Money Lover's "seconds to record") and all pre-sync eras satisfy the L0. Capture mechanism is an L2 posture.
- **"Income tracking is definitional"** — rejected. A pure money-out tracker is still an expense tracker; income is L1 (very common, enables cash-flow views).
- **"Accounts/wallets are definitional"** — rejected. Toshl's own tutorial shows the account field disappearing when only one (auto-created Cash) account exists — direct evidence that account structure is optional organization, not the record's backbone. L1.
- **"Receipt scanning / OCR is definitional"** — L2; present in some products, absent in others.
- **"Mobile-first is definitional"** — rejected; surface is L2 (web and desktop surfaces exist in the sample).
- **"Expense tracking includes reimbursement/approval"** — rejected; that is the corporate Expense Management Platform Type (employee → report → approval → reimbursement). The personal Type records spending for the spender's own insight.
- **"A spending breakdown inside a bank app is this Type"** — rejected as a Type claim; it is a capability of the banking relationship (single institution, no cash capture, history tied to the account). Noted as a boundary, not a counterexample.

## Boundary Findings

### vs Budgeting Application (§08 sibling, unprocessed)

- Budgeting centers on a **plan-first allocation container** (limits/envelopes set before spending, spending measured against the plan). Expense tracking centers on the **record-first log** (what happened, classified, aggregated).
- The sampled expense trackers all *include* budgets — but as a comparison layer over the record, not as the organizing object.
- Boundary test: 去掉"以支出记录为中心的分类日志"，只留"预算容器与计划对比" → Budgeting Application; 去掉预算、只留记录与归类 → Expense Tracking Application.
- Many products do both; center of gravity decides. **Joint-review flag** for when budgeting-application is processed (consistent with the flag already recorded by personal-finance-management-application).

### vs Personal Finance Management Application (§08 sibling, processed)

- PFM's documented core: person/household **money accounts as managed records + transaction register + consolidated whole-picture** (balances / income-spending / net worth).
- Expense tracking centers the **expense record + where-money-goes analysis**; account balances and net worth are not the center (Toshl exposes net worth only inside its broader "Planning" surface; the sampled trackers' home surfaces are spending views).
- Boundary test: 去掉账户余额/净资产全貌 → expense tracker; 去掉支出记录中心性 → PFM. Consistent with PFM's STATUS entry, which holds Expense Tracking as a subset sibling on structural removal tests.

### vs Expense Management Platform (§08 sibling, unprocessed — prior batch run FAILED)

- Corporate expense management: **employee** submits **expense reports** for **reimbursement**; approval workflow; policy compliance; corporate-card reconciliation. User acts for an organization; money spent is the organization's.
- Personal expense tracking: the spender records their own spending for their own insight; no approval, no reimbursement, no policy.
- Boundary test: 去掉组织/报销/审批语境 → personal expense tracking; 加入组织审批与报销 → Expense Management Platform.
- Caution: the sibling leaf is unprocessed (batch FAIL), so this boundary is held structurally only.

### vs Bookkeeping Application / Accounting Software (§08, processed)

- Bookkeeping/accounting: **books semantics** — chart of accounts, balanced posting, financial statements, tax readiness.
- Expense tracking: **no books semantics** — categories are analytical labels, not ledger accounts; no double-entry, no statements. Matches the seam recorded in bookkeeping-application's STATUS entry ("Expense Tracking (no books semantics)") and accounting-software's ("a product without the ledger core is an invoicing, expense-tracking, or budgeting tool").
- Money Manager's "double-entry booking" is a personal-asset variant flavor (L2), not business books: no chart of accounts, no statements, no tax workflow observed.
- Boundary test: 加入科目表与报表 → bookkeeping/accounting; 去掉 books 语义 → expense tracking.

### vs Net Worth Tracker (§08 sibling, unprocessed)

- Net worth = **position** (assets − liabilities at a point in time); expense tracking = **flow** (spending over time). Different central object; overlap only where trackers add asset accounts (L2).

### vs Digital/Mobile Banking Application (§08)

- A bank app's spending view categorizes only what passes through that bank relationship; it is a feature of the account, not a user-owned record system. The standalone Type captures spending **regardless of where money is held** (cash, multiple banks, cards), keeps history independent of any single account relationship, and lets the user own/repair the classification.
- Boundary test: 把记录绑定到单一银行关系、随账户走 → banking-app capability; 记录独立于任何账户关系、由用户持有 → Expense Tracking Application.

### vs Spend Management Platform / Corporate Card & Spend Platform (§08 siblings, unprocessed)

- Organization-side spend visibility and control over corporate spend; same personal-vs-organizational wall as Expense Management Platform.

## Uncertainties

- The sample rests on four products; Spendee, Monefy, and PocketGuard were unreachable, so the "minimal manual-first" pole is represented indirectly (Toshl's manual mode; Money Lover's "seconds to record" framing) rather than by a dedicated minimal product's docs. If a later pass reaches such products, confirm that even minimal trackers carry categories + some aggregation (expected, since the paper analog already does).
- Categorization is held at L0 on cross-product evidence (all four sampled products) + historical analogs + one product making it mandatory (Toshl). If a mature product were found that treats categories as fully optional decoration, the L0 might need re-examination; no such product was observed.
- Budgeting Application and Expense Management Platform leaves are unprocessed (the latter's prior batch run FAILED); the corresponding boundaries are held structurally and flagged for joint review rather than confirmed against their documents.
- The exact placement of "planned vs actual" (L1) rests on two products' fetched pages (Toshl directly; Wallet's planning/predict framing); other products' fetched pages did not mention it. Kept at L1 with moderate wording in the final document.

## Final Synthesis

Canonical Expense Tracking Application:

```text
L0 (defining invariant)
- Expense record (money-out event: amount + date + what it was for)
- Spending categories (user-manageable classification)
- Aggregated view over time (period totals, category breakdowns, trends)

L1 (common mature structure)
- Income records; cash-flow view
- Accounts/wallets as optional containers; transfers between own accounts
- Budgets with spent-vs-limit comparison (+ rollover)
- Recurring entries + reminders; planned vs actual
- Receipt photos/attachments
- Reports/charts/export
- Capture assistance (auto-categorization, rules, ML, import review)
- Notifications (budget alerts, unusual transactions, due dates)

L2 (variant / optional)
- Capture posture (manual-first / sync-first / import / receipt-OCR)
- Multi-currency + exchange rates; travel emphasis
- Locations / per-merchant analysis
- Splitting; shared/household wallets; savings goals; debt/loan depth
- Asset-position/double-entry flavor (drifts toward bookkeeping)
- Surface (mobile/web/desktop); local vs cloud

L3 (vendor-specific — Research Notes only)
- Toshl signed-entry/one-category/RRULE/review-queue/river-flow machinery
- Wallet ML labeling + bank-connection scale claims + sibling products
- Money Lover travel/debt/saving modules + positioning claims
- Money Manager double-entry/asset-graph flavor + claims
```

The Application Document will present the L0 as the defining core and L1 as standard capabilities, with a Variants section naming L2 options. L3 stays in Research Notes.
