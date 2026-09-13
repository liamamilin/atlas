# Research Notes — Budgeting Application

## Research Goal

Identify the smallest stable invariant that defines the **Budgeting Application** Application Type (DIRECTORY §08 Finance, Banking, Insurance & Investment, line 607), and place every other observed capability at the correct abstraction level.

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

> Budgeting Application (DIRECTORY §08 Finance, Banking, Insurance & Investment)

Nearest confusing Types:

- **Expense Tracking Application** (§08 sibling, processed 2026-09-06) — its research notes record the seam and a **joint-review flag**: "Budgeting centers on a plan-first allocation container (limits/envelopes set before spending, spending measured against the plan). Expense tracking centers on the record-first log." This pass must answer that flag.
- **Personal Finance Management Application** (§08 sibling, processed) — whole-picture money overview (accounts, balances, net worth) vs the plan layer.
- **Budgeting & Forecasting Platform** (§08, separate leaf, unprocessed) — organization-side budgeting (FP&A), not personal.
- **Public Budgeting Platform** (§24, separate leaf) — government fund/appropriation budgeting.
- **Accounting Software / Bookkeeping Application** (§08, processed) — accounting-software's STATUS entry already states "a product without the ledger core is an invoicing, expense-tracking, or budgeting tool."
- **Expense Management Platform / Spend Management Platform** (§08 siblings, unprocessed) — organization-side spend.
- **Net Worth Tracker** (§08 sibling, unprocessed) — position (assets − liabilities) vs plan/flow.
- **Debt Management Application, Retirement Planning Application** (§08 siblings) — payoff plan and long-horizon projection vs period spending plan.
- **Digital Banking / Mobile Banking Application** (§08) — a bank app's budgeting view is a capability of the account relationship.

Working hypothesis:

> A budgeting application lets a person or household decide in advance how much money may go to which purposes in a period, then measures actual spending against those decisions ("what's left?").

Key uncertainties at start:

1. Is **actuals-vs-plan comparison** definitional, or just the point of the tool? (Expected definitional.)
2. Is a **transaction register / accounts** required, or can actuals be simple entries? (Fudget said "no tracking" — test this.)
3. Is the **income side** definitional?
4. Is the **period** definitional?
5. Which machinery is **method-specific** (envelope, zero-based, auto spending plan, flex buckets) rather than structural?

## Research Questions

1. What is the smallest object model without which a product is no longer recognizable as a budgeting application?
2. How is the plan structured (allocation containers, periods, unallocated money) and how do implementations vary (envelope vs category vs bucket vs line item)?
3. How do actuals reach the comparison (manual entry, scheduled entries, import, bank sync), and is any capture mechanism definitional?
4. What comparison state does the Type reliably expose (planned / actual / remaining, left to spend, overspent)?
5. What happens on overspending, rollover, and period reset?
6. How do budgeting-method philosophies (envelope, zero-based, auto spending plan, flex bucket, minimal plan list) differ from Type structure?
7. What are the boundaries with Expense Tracking, PFM, corporate budgeting, accounting, banking apps?
8. Do older / analog / method-diverse forms (paper envelopes, kakeibo, spreadsheets, desktop-era budget modules) still fit the definition?

## Representative Products

| Product | Why selected | Docs accessed |
|---|---|---|
| YNAB | method-heavy premium consumer product; "give every dollar a job" assignment philosophy; public **API documentation** exposes the full object model (Tier 1) + official method page | yes (api.ynab.com overview + changelog; ynab.com/the-four-rules method page) |
| Goodbudget | classic digital **envelope** budgeting; manual-first with optional sync; freemium household segment; strong help center (Tier 1) | yes (help center: index, Step 1 add envelopes, Step 4 fill, Step 5 record expenses, What is Available money) |
| Monarch Money | sync-first modern product; **cash-flow-based** framing; auto-suggested plan; category vs flex budgeting; Planned/Actual/Remaining | yes (help center article "Creating Your Budget in Monarch") |
| Quicken Simplifi | mainstream budgeting inside a PFM suite; **auto-generated Spending Plan** ("budgeting your way" — method-agnostic) | yes (official product page incl. Spending-Plan FAQ) |
| Fudget | **minimal plan-only** product: no bank connections, no account tracking; free tier; desktop+mobile | yes (official product page incl. pricing tiers) |

Products attempted and abandoned per the network-failure rule (1–2 failures → abandon, no memory-fill):

- **EveryDollar** — everydollar.com 406 ×1; ramseysolutions.com/ramseyplus/everydollar 406 ×1 → abandoned; retained as market-context only (zero-based, manual-first), **zero claims**.
- **PocketGuard** — pocketguard.com 403 ×1 this pass (plus 403 in the sibling expense-tracking pass) → abandoned; market-context only ("left to spend"-style budgeting), **zero claims**.
- **YNAB user-facing help center** — docs.ynab.com and support.ynab.com render only a JS shell ("YNAB Help") → YNAB evidence rests on its public API documentation (Tier 1) and official method page; no help-center-level claims.

## Sources

Research date: **2026-09-06**

Directly fetched official sources (Layer A evidence):

- YNAB API — overview & object model (plans, months, categories, accounts, transactions, scheduled transactions, payees, money movements): https://api.ynab.com/
- YNAB API — changelog (category goal machinery, month/category transaction listings, credit-card payment categories): https://api.ynab.com/ (changelog section, in-page)
- YNAB — official method page ("The YNAB Method", "What's it for?"): https://www.ynab.com/the-four-rules
- Goodbudget Help Center — index: https://goodbudget.com/help/
- Goodbudget Help Center — Step 1. Add Envelopes to Create a Budget: https://goodbudget.com/help/getting-started-guide/step-1-add-envelopes/
- Goodbudget Help Center — Step 4. Fill Your Envelopes: https://goodbudget.com/help/getting-started-guide/step-4-fill-envelopes/
- Goodbudget Help Center — Step 5. Record Your Expenses: https://goodbudget.com/help/getting-started-guide/step-5-record-expenses/
- Goodbudget Help Center — What is Available money?: https://goodbudget.com/help/budgeting-with-goodbudget/what-is-available-money/
- Monarch Money Help Center — Creating Your Budget in Monarch: https://help.monarchmoney.com/hc/en-us/articles/360048883631-Creating-Your-Budget-in-Monarch
- Monarch Money Help Center — index (related articles: Rollover Budgets, Group Budgeting, Save Up/Pay Down Goals, Flex Budgeting): https://help.monarchmoney.com/hc/en-us
- Quicken Simplifi — official product page incl. "How is Quicken Simplifi's Spending Plan different from other budgets?" FAQ: https://www.simplifimoney.com/
- Fudget — official product page (features + pricing tiers): https://fudget.com/

Source-access Limitation (per `WORKFLOW_v1.1.md §23`):

- YNAB help center unreachable (JS shell ×2) → YNAB consumer-facing operational detail is **not** asserted; YNAB claims are calibrated to its API docs + method page.
- EveryDollar and PocketGuard unreachable (406/403) → named only as market context, zero product-specific claims.
- Quicken Simplifi evidence is its official product page + FAQ (Tier 2) — help center (support.simplifi.quicken.com) not fetched; page-level claims only, no numeric operational details beyond the page's own marketing figures (e.g. "14k financial institutions" — recorded as L3 vendor claim).
- Fudget evidence is its official product page (Tier 2); support pages not fetched.
- No precise numeric limits from help-center sources are asserted anywhere; vendor-claimed figures observed are recorded here as L3 marketing claims only.

## Product Observations

### YNAB (Layer A — public API docs + official method page)

**Object model (API docs):**

- The API's central resource is the **Plan** (`GET /v1/plans` returns plans with `name`, `first_month`, `last_month`). YNAB now calls the budget a "plan" throughout its app and API.
- Delta-request endpoints enumerate the model: `plans`, `accounts`, `categories`, `money_movements`, `money_movement_groups`, `months`, `payees`, `scheduled_transactions`, `transactions`.
- **Months** are first-class: `GET /plans/{plan_id}/months`; transactions are listable per month (`/months/{month}/transactions`), per category, per payee.
- **Categories** carry per-month budgeted amounts and balances; category machinery includes `goal_target`, `goal_target_date`, `goal_frequency` (`monthly`/`weekly`/`yearly`), "NEED"-type recurring targets with monthly rollover behavior flags (`goal_needs_whole_amount`: "Set Aside" vs "Refill"), and dedicated **Credit Card Payment categories** (goal machinery explicitly not supported there).
- **Accounts** have an `on_budget` flag — accounts can be inside or outside the plan.
- Transactions, scheduled transactions, payees, and money movements are all plan-scoped resources.
- API positioned as access to "your own plan"; OAuth read-only scope is defined in terms of modifying "a plan".

**Method page (official marketing/method content):**

- Core question: "What's your money for?" — "Every time you get money, ask yourself 'What's it for?' and make a thoughtful, flexible plan for your spending based on what matters most."
- "For Now": "Decide what you need your money to do **before you get paid again**. Making a plan for your spending **in advance** helps you avoid spending more important money on less important things."
- "For Later": non-monthly expenses — "Anticipate irregular expenses and **set aside manageable monthly amounts**."
- "For Ease": "Get a month ahead on bills. When next month's expenses are **covered**…"; user story: "all my categories were **fully funded**."
- "For change": "your plan for it can **change at any time**."
- Community framing: "Giving every dollar a job."
- Footer: YNAB is an agent of Plaid (regulated account information services) — i.e., direct-import bank connectivity is an optional layer.

### Goodbudget (Layer A — help center articles)

- Definition: "A budget is a **plan for how you would like to spend or save money**. You can use a budget to help you control your spending, pay down debt, or make room for the things that are important to you."
- **Step 1 — Add Envelopes**: "Choose a budgeting period" (monthly recommended, user-changeable); create **Envelopes** ("Groceries, Gas and Mortgage" as example common categories); **Annual Envelopes** (one-year period; "Enter how much you'd like to spend or save in a year, and Goodbudget sets aside the right amount each regular budget period" — $600/year holiday example → $50/month); **Goal Envelopes** (one-off, optional due date); **"Reality Check!"** — "Make sure that this amount doesn't exceed your total income for the budgeting period."
- **Step 4 — Fill Your Envelopes**: "Filling moves money from your **Available** to your Envelopes **so you know exactly how much you can spend**." Fill modes: "Add budgeted amount: **Rolls over leftovers** and adds the budgeted amount again"; "Set to budget amount: tops off the Envelope to exactly full"; fills can be scheduled to post automatically; warning shown when trying to fill more than Available ("turns red").
- **Available money** (dedicated article): "money that does not have a job yet"; computed as "All your Account money − All your Envelope money"; "Available is automatic" (cannot be edited directly); income goes up Available (or straight into envelopes); adding a credit card with balance **lowers** Available ("Goodbudget sets that money aside to pay the card"); **Debt Accounts are off-budget** ("Available does not change"); deleting an envelope returns its balance (positive or negative) to Available; imported transactions without an envelope lower Available until assigned and confirmed; negative Available = allocated more than you have; "Savings usually live inside a Savings Envelope."
- **Step 5 — Record Your Expenses**: expenses recorded against Accounts and assigned to Envelopes; "All expenses that you record will count against your *current* Envelope balances"; scheduled transactions for recurring expenses; bank-sync imports can be **Confirmed** and manual entries merged via a **Match tool**; location-based auto-suggest of Payee/Envelope/Account; credits recorded as negative amounts; Debt Accounts track loans/cards being paid off (separate debt-payment flow).
- Other: envelope groups; share budget with partner; device limits; free tier has an envelope-count limit ("Need more Envelopes? Sign up for a subscription… Unlimited Envelopes!"); product framing: "based on the envelope budget system"; replaces "family budget planner, worksheet or spreadsheet"; kakeibo and cash-stuffing pages in footer.

### Fudget (Layer A — official product page)

- Positioning: "Plan your monthly budget in minutes. **No bank connections, no tracking** — just simple budgeting that syncs across devices."
- "Monthly budget planning: Plan the month in minutes. **Add income and expenses, and always know what's left.**"
- "No bank linking: Manual budgeting without bank sync. No connections, no tracking, no surprises."
- "Events & projects: Weddings, holidays, renovations or side projects — manage them like a simple budget." (non-monthly budgets as first-class)
- Keyboard-first fast entry; sync across Mac/Windows/iOS/Android.
- Tiers (L3 pricing facts): Basic free (up to 5 budgets, 250 entries, 1 device); Plus (unlimited budgets & entries, multi-device, share account with a loved one, folders, partials, calculator, export, print, sort, reminders).
- Note what is absent: no accounts, no balances, no bank sync, no auto-categorization — yet the product is unambiguously a budgeting app.

### Quicken Simplifi (Layer A− — official product page + FAQ)

- Budgeting entry: "Budgeting your way — **Always know what's left to spend & save**: Visualize your income, bills, subscriptions, & savings, and always know how much you have available after expenses."
- **Spending Plan FAQ** (direct quote fragments): "it **starts with your monthly income, subtracts your bills & subscriptions, and generates a personalized Spending Plan that adjusts automatically as you spend**. No matter how you like to budget, the tools in Quicken Simplifi can accommodate any method you like to use — zero-based budgeting, envelope budgeting, 50-30-20, and more."
- Plan mechanics from FAQ bullets: "See how much you have **left to spend per day** for the rest of the month, calculated automatically"; "Add any **planned spending**, from groceries to birthday dinners, to set aside the money you need"; "Include your **savings goals** in your plan so you don't spend that money by mistake"; "Easily **ignore any spending** that you don't want to count toward your monthly budget."
- Surrounding capabilities: budgets + auto-categorized transactions; watchlists (implied via "identify any spending issues… keep your budget on track"); upcoming bills & subscriptions reminders with projected balances; savings goals ("commit cash, track progress"); projected cash flow; reports; retirement planner; investments.
- "Connect to over 14k financial institutions" (vendor claim, L3); sharing with one other person ("spaces & sharing").
- Product sits inside a PFM suite (cash flow, investments, net worth on the same page) — budgeting is one module.

### Monarch Money (Layer A — help article "Creating Your Budget in Monarch")

- "The **Budget** section is where you will **plan for your monthly expenses**."
- Two budgeting modes: **category budgeting** ("assign every expense category a budget, and track your spending at the category level") and **flex budgeting** (default: "tracking your flexible spending — a high-level bucket that contains all the categories containing expenses that tend to vary more"; categories organized into fixed / non-monthly / flex buckets).
- **Auto-suggested plan**: "The first time you build your budget, Monarch automatically fills it in for you, using the **average of your last six months of spending** in each expense category" + "Recalculate default budgets" + "Clear all budget values" + budget walkthrough.
- **Cash-flow framing**: "your Monarch budget is built around a **monthly cash flow system**. Your total monthly budget is based on how much **income you expect to receive** that month; expenses and savings are then subtracted from that income to create a **balanced budget**." … "Monarch uses a **cash flow–based approach rather than an account balance–based one**… Monarch instead helps you plan your future cash flow—how each month's income will be allocated to expenses and savings. **Account balances are used mainly for long-term goals, not day-to-day spending.**"
- **"Left to budget"**: "how much you have left to budget… the income remaining after your planned expenses are subtracted from your planned income for the month." Constraint framing: "**income = expenses + savings**."
- **Comparison columns**: "the web version shows three columns on the budget page (**Planned**, **Actual**, **Remaining**)" (mobile toggles Remaining/Actual).
- **Category taxonomy**: 3 layers — Type (Income / Expenses / Transfers, fixed) → Group (Housing, Food…, customizable) → Category (Rent, Groceries…, customizable); "approximately 60 category options"; ML auto-categorization of transactions; **Transfer and Credit Card Payment categories are excluded from budgets and cash flow** ("good for tracking money moved between your own accounts"); categories can be excluded from the budget individually (transactions still appear in cash flow).
- Setup precondition: connect financial accounts and categorize transactions accurately — "Since the budget is based on income, these are the most important transactions to categorize correctly."
- Related help articles (titles as evidence of machinery): Rollover Budgets, Group Budgeting, Using Save Up Goals, Using Pay Down Goals, Moving Funds In and Out of Goals, Using Flex Budgeting, Transfers and Credit Card Payments.

### Historical / market-sample breadth (§24 check)

- **Paper envelope budgeting / cash stuffing** (analog era): cash allocated into labeled envelopes per purpose per period; when the envelope is empty, spending stops. The comparison state is the physical envelope's remaining cash. Goodbudget explicitly digitizes this ("based on the envelope budget system"; "cash stuffing but make it virtual"); the analog practice predates software and satisfies the candidate L0 without any account, sync, or device.
- **Kakeibo** (Japanese household-ledger method, predating software): planned vs recorded amounts organized by purpose, reviewed periodically. Goodbudget markets a Kakeibo page; satisfies the candidate L0.
- **Spreadsheet budgets** (pre-app and current): rows = planned amounts per category, columns = actual vs planned, "left over" formulas. Goodbudget markets itself as a replacement for "family budget planner, worksheet or spreadsheet". Satisfies the candidate L0.
- **Desktop-era personal finance products** (Quicken-class): budget module over manually entered/imported transactions with budget-vs-actual reports. Widely attested; the same vendor now ships Simplifi with the Spending Plan. Satisfies the candidate L0.
- **Corporate budgeting** (FP&A / Budgeting & Forecasting Platform class): organization budget cycles, forecast versions, department rollups — different actors and objects; treated as a different Type (boundary, not counterexample).

All historical/analog forms satisfy the candidate L0; no era-, capture-, or method-specific mechanism is definitional.

## Cross-product Comparison

| Finding | YNAB | Goodbudget | Fudget | Quicken Simplifi | Monarch | Abstraction level |
|---|---|---|---|---|---|---|
| period-scoped plan as the organizing object | yes (Plan with first/last month; months first-class) | yes (budgeting period, changeable; Annual envelope = year; Goal envelope window) | yes (monthly budgets; events/projects as separate windowed budgets) | yes ("starts with your monthly income"; left-to-spend "for the rest of the month") | yes ("plan for your monthly expenses"; monthly cash-flow system) | **L0** |
| planned amounts assigned to purposes within the plan | yes (category budgeted amounts; "giving every dollar a job") | yes (envelope budget amounts) | yes (income/expense line items in the plan) | yes ("planned spending… to set aside the money you need"; auto Spending Plan) | yes (category budgets; flex bucket) | **L0** |
| actuals recorded/captured in-app feeding the comparison | yes (transactions, scheduled transactions; direct import optional) | yes (recorded expenses against envelopes; imports/scheduled) | yes (expense entries — no accounts) | yes (auto-categorized transactions adjust the plan) | yes (categorized transactions; auto-categorization) | **L0** |
| user-visible comparison state (planned vs actual vs remaining) | yes (category balances; "fully funded" categories) | yes (envelope balances = "exactly how much you can spend") | yes ("always know what's left") | yes ("left to spend per day") | yes (Planned / Actual / Remaining columns) | **L0** |
| unallocated money figure (unassigned remainder) | implied by assignment method (not asserted from fetched docs) | yes (Available = accounts − envelopes, computed) | not observed | not observed as separate figure (left-to-spend is the remaining state) | yes ("left to budget") | L1 |
| income input anchoring the plan | yes (assign money when received; plan in advance of payday) | yes (income; Reality Check: budgeted ≤ income) | yes (income entries) | yes (starts with monthly income) | yes (budget anchored on expected income; income = expenses + savings) | L1 |
| accounts as optional containers for actuals | yes (accounts with on_budget flag) | yes (Available is computed from accounts) | **no** (explicitly "no tracking") | yes (bank aggregation core) | yes (connect accounts first) | L1 |
| goals / sinking funds inside the plan | yes (category goal targets, NEED-type set-aside/refill) | yes (Annual/Goal envelopes; "sets aside the right amount each period") | not observed | yes (savings goals included in plan; "commit cash") | yes (Save Up / Pay Down Goals; balances used for long-term goals) | L1 |
| recurring/scheduled entries & bills | yes (scheduled_transactions) | yes (scheduled transactions; scheduled fills) | not observed (reminders in Plus tier) | yes (bills & subscriptions subtracted; reminders) | yes (fixed/non-monthly buckets) | L1 |
| rollover of unspent amounts | yes (NEED-type Refill vs Set Aside behavior) | yes (rollover toggle on fill) | not observed | not observed on fetched page | yes (Rollover Budgets article) | L1 |
| plan setup assistance from history | not observed in fetched docs | not observed (craft from past spending or income — user-driven) | no | yes (auto-generated Spending Plan) | yes (6-month average auto-fill; recalculate) | L1 |
| overspending states (remaining can go negative) | not asserted from fetched docs | yes (envelope can go negative; negative Available red warning) | not observed on fetched page | yes ("ignore any spending" implies exclusion control) | yes (Remaining implies negative possibility — not asserted) | L1 (moderate wording) |
| transfer / credit-card special handling | yes (Credit Card Payment categories; money_movements) | yes (credit card balances set aside from Available; debt accounts off-budget) | no (no accounts) | not observed on fetched page | yes (Transfer & Credit Card Payment categories excluded from budget) | L1 |
| reports / analytics beyond the comparison | not observed in fetched docs | not observed on fetched pages | export/print (Plus) | yes (reports & insights) | yes (cash flow; spending totals) | L1 |
| sharing / household budgeting | not observed in fetched docs | yes (share budget with partner) | yes (share account with loved one, Plus) | yes (spaces & sharing, one other person) | yes (Group Budgeting) | L1 |
| bank sync / capture posture | optional (Plaid agent footer) | optional (Automatic Bank Sync section; manual core) | **none** (explicit) | core (14k institutions claim) | core (connect accounts first) | L2 (capture posture) |
| budgeting-method philosophy | zero-based assignment ("every dollar a job") | envelope method | minimal plan list | method-agnostic auto Spending Plan (zero-based/envelope/50-30-20 accommodated) | cash-flow-based; category or flex; envelope/zero-based styles supported | L2 (philosophy) |
| envelope as named allocation container | no (categories) | yes (envelopes) | no (line items) | no | no (buckets/categories) | L2 (implementation naming) |
| non-monthly / project-event budgets | not observed | yes (Annual/Goal envelopes) | yes (events & projects) | not observed | yes (non-monthly bucket; goals with dates) | L1 |
| whole-picture PFM context (net worth, investments) | no | no | no | yes (suite) | yes (suite) | L2 (drifts toward PFM) |
| surface | web + mobile | web + iOS + Android | desktop + mobile | web + mobile | web + mobile | L2 (surface) |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as a budgeting application:

```text
Spending plan (period-scoped budget) as the organizing object
└── Allocations: planned amounts assigned to purposes (categories/buckets) within the plan
    └── Actuals captured in the app (entries or transactions) feeding the comparison
        └── Comparison state: planned vs actual vs remaining (left to spend / overspent)
```

Four properties:

- **Period-scoped plan** — the plan exists for a defined time scope (recurring period such as a month, or a one-off window such as a project/event/year).
- **Allocations** — the user assigns planned amounts to purposes within the plan (per category/envelope/bucket/line, or as a computed whole-plan division).
- **Actuals in the app** — spending (and, commonly, income) is captured or recorded in the application at entry or transaction grain.
- **Comparison state** — the application continuously shows where actuals stand against allocations (remaining, left to spend, overspent, funded/unfunded).

Removal tests:

- remove the *plan/allocation* → a record-first classified log (Expense Tracking Application) or a cash-flow forecast; not budgeting
- remove the *period scope* → an unconstrained target list; envelope, kakeibo, spreadsheet, and app forms all bound the plan in time
- remove *actuals* → a wish list; the "how much can I still spend?" question becomes unanswerable
- remove the *comparison state* → a note-taking surface; the Type's recurring value — knowing what's left before spending — disappears

§24 historical check: paper envelope budgeting, kakeibo, spreadsheet budgets, and desktop-era budget modules all satisfy the four properties. No era-, platform-, capture-, or method-specific mechanism is definitional. Therefore bank sync, auto-categorization, accounts, mobile-first surfaces, and any named budgeting method (envelope, zero-based, 50-30-20) are **not** L0.

## L1 — Common Mature Structure

Common across the researched sample; they make the plan practical but do not define the Type:

```text
Income input anchoring the plan (expected income; budgeted ≤ income checks; income = expenses + savings)
Unallocated-money figure (Available / left to budget / to assign — computed, not directly editable)
Accounts as optional containers for actuals (on-budget vs off-budget; balances)
Goals / sinking funds inside the plan (set aside per period toward a future expense; save-up/pay-down goals)
Recurring & scheduled entries (bills, subscriptions; scheduled allocations)
Rollover of unspent amounts (optional per allocation)
Fixed vs flexible spending separation (bills first, flexible spending after)
Plan setup assistance from history (auto-fill from past averages; auto-generated spending plan)
Overspending states (remaining can go negative; exclusion controls; carried or covered shortfalls)
Transfer / credit-card-payment special handling (excluded from spending; payment set-asides)
Non-monthly / project-event budgets (annual envelopes, events, dated goals)
Reports / analytics over plan vs actual
Sharing / household budgeting (partners, groups)
Alerts & reminders (budget states, due dates)
```

## L2 — Variant / Optional Structure

Presence or absence does not change the Type:

```text
Budgeting-method philosophy: envelope (allocation containers with carried balances) ↔
  zero-based assignment (allocate all money on receipt) ↔ auto-generated spending plan ↔
  flex-bucket (few buckets instead of per-category lines) ↔ minimal plan list
Allocation-container naming: envelope / category / bucket / line item (concept is identical)
Capture posture: manual-first ↔ bank-sync-first ↔ import-only ↔ no-connections
Plan scope: whole-money household plan ↔ single-purpose project/event budgets
PFM bundling: standalone plan-only product ↔ budgeting module inside a PFM suite (net worth, investments)
Segment: individual / couple / family (sharing depth)
Surface: mobile / web / desktop; local vs cloud sync
Method tooling depth: method-specific machinery (targets, refills, top-offs, watchlists)
```

## L3 — Vendor-specific Structure

Remains in Research Notes only:

- **YNAB**: the product calls the budget a "Plan" (API resources /plans, /months, /categories, /money_movements); category goal machinery (`goal_target`, `goal_target_date`, `goal_frequency`, NEED-type "Set Aside" vs "Refill" via `goal_needs_whole_amount`); Credit Card Payment categories excluded from goal machinery; accounts with `on_budget` flag; milliunits currency representation; "Age of Money" community metrics (third-party tools); Plaid-as-agent footer; OAuth restricted-mode limits.
- **Goodbudget**: "Available = All your Account money − All your Envelope money" with the exact behavioral rules (credit-card balances lower Available to set aside payment; debt accounts off-budget; deleting an envelope returns negative balances to Available; imported unassigned transactions lower Available until confirmed); fill modes "Add budgeted amount" (with rollover) vs "Set to budget amount" (top-off); scheduled fills; Match tool for manual-vs-imported merge; location-based payee/envelope suggestions; Quick Fills; free-tier envelope-count limit ("Unlimited Envelopes" via subscription); device limits; kakeibo and cash-stuffing marketing pages.
- **Monarch**: ~60 system categories in a fixed Type → Group → Category taxonomy; "left to budget"; income = expenses + savings constraint framing; Recalculate default budgets / Clear all budget values / Budget Walkthrough; per-category budget exclusion toggle; Planned/Actual/Remaining columns with mobile toggle; Flex vs Category budgeting modes.
- **Quicken Simplifi**: Spending Plan auto-generated as income − bills & subscriptions; "left to spend per day"; "ignore any spending" exclusion; savings-goal inclusion in the plan; "spaces & sharing" (one other person); "14k financial institutions" vendor claim; pricing/promo figures.
- **Fudget**: free-tier limits (5 budgets / 250 entries / 1 device); Plus extras (folders, partials, calculator, export, print, sort, reminders, loved-one sharing); keyboard-first positioning.

## Rejected Findings

- **"Accounts/bank sync are definitional"** — rejected. Fudget is a marketed budgeting app with explicit "no bank connections, no tracking"; Goodbudget's manual core predates its optional sync; all pre-sync analog forms satisfy the L0. Capture posture and account containers are L1/L2.
- **"The envelope model is definitional"** — rejected. Envelope is one implementation of the allocation container (Goodbudget); other products use categories, buckets, or auto-generated plans with no envelope naming. Concept at L0 is "allocation"; naming at L2.
- **"Zero-based assignment is definitional"** — rejected. It is YNAB's method philosophy; Simplifi explicitly accommodates "zero-based… envelope… 50-30-20, and more" without requiring any of them; Monarch supports but does not require zero-based style. L2.
- **"Auto-categorization / ML is definitional"** — rejected; absent in Fudget and Goodbudget's manual core. L2 (setup aid).
- **"The plan must be user-authored"** — rejected as a strict claim. Simplifi generates the plan automatically and Monarch auto-fills from history; the user reviews and edits. The user-approved plan is the invariant; who drafts it is not.
- **"Income tracking is definitional"** — rejected at L0 (a plan defined against a fixed allowance still works); held at L1 because every sampled product does anchor the plan on income. Near-universal ≠ defining (anti-overfitting rule).
- **"Savings goals are definitional"** — rejected; absent from Fudget's fetched pages; goals are the goal-tracking sibling capability absorbed as L1.
- **"Budgeting includes corporate planning cycles"** — rejected; that is the Budgeting & Forecasting Platform Type (organization actors, forecast versions, department rollups).
- **"A bank app's budget view is this Type"** — rejected as a Type claim; it is a capability of the account relationship (single institution, history tied to the account), noted as a boundary.

## Boundary Findings

### vs Expense Tracking Application (§08 sibling, processed — joint-review flag answered)

- Budgeting is **plan-first**: the organizing object is the period-scoped allocation; the record exists to feed the plan-vs-actual comparison. Expense tracking is **record-first**: the organizing object is the classified expense record; budgets are an optional comparison layer over the record.
- Direct evidence for the asymmetry: a budgeting product with **no records layer at all** exists and markets it (Fudget: "No bank connections, no tracking"); conversely the expense-tracking sample carried budgets only as an L1 comparison layer (per sibling research notes).
- Boundary test: 去掉"以支出记录为中心的分类日志"，只留"预算容器与计划对比" → Budgeting Application; 去掉计划容器、只留记录与归类 → Expense Tracking Application.
- Overlap is real (mature budgeting apps keep transaction registers; mature trackers include budgets); **center of gravity decides**. Both sampled products that straddle (Monarch, Simplifi) still keep the plan as the budgeting module's center. Joint-review flag from expense-tracking-application (2026-09-06): **held as distinct Types on center-of-gravity**; no merge recommended.

### vs Personal Finance Management Application (§08 sibling, processed)

- PFM's core is the consolidated whole picture (accounts, balances, income/spending/net worth). Budgeting's core is the plan. Fudget proves a plan-only product without accounts is still budgeting; a PFM without accounts is not a PFM.
- Simplifi and Monarch straddle: budgeting modules inside PFM suites. Seam: remove the whole-picture layer → standalone budgeting; remove the plan → PFM with spending analytics.

### vs Budgeting & Forecasting Platform (§08, separate leaf, unprocessed)

- Corporate budgeting plans organizational money over planning cycles with departments, versions, forecasts, and rollups; personal budgeting plans an individual/household's money per period. Different actors, objects, and rules. Same organizational-vs-personal wall recorded by expense-tracking vs Expense Management Platform.

### vs Public Budgeting Platform (§24, separate leaf)

- Government fund/appropriation budgeting — different domain, actors, and legal constraints entirely.

### vs Accounting Software / Bookkeeping Application (§08, processed)

- No ledger semantics: no chart of accounts, no double-entry posting, no financial statements. Consistent with accounting-software's STATUS entry ("a product without the ledger core is an invoicing, expense-tracking, or budgeting tool"). Allocations are plan labels, not ledger accounts.

### vs Net Worth Tracker (§08 sibling, unprocessed)

- Position (assets − liabilities at a point in time) vs plan (allocations over a period). Products with net-worth surfaces (Simplifi, Monarch) bundle both; the plan remains the budgeting module's center.

### vs Digital/Mobile Banking Application (§08)

- A bank app's budgeting view plans only that institution's flows and is a capability of the account relationship. The standalone Type plans money regardless of where it is held (cash, multiple banks, cards) and survives independently of any account relationship.

### vs Debt Management Application / Retirement Planning Application (§08 siblings)

- Debt payoff scheduling and long-horizon retirement projection have different central objects (payoff schedule; retirement trajectory). Budgeting absorbs them only as L1 goals inside the plan (pay-down goals; save-up goals).

### vs Expense Management Platform / Spend Management Platform (§08 siblings, unprocessed)

- Organization-side spend processes (reports, approvals, reimbursement, corporate cards) vs personal plan. Same personal-vs-organizational wall.

## Uncertainties

- YNAB's consumer-facing overspending handling and unassigned-money naming could not be verified (help center JS-gated); no YNAB-specific claims made beyond the API surface and method page.
- Simplifi's help center was not fetched; its Spending-Plan mechanics rest on the official product page + FAQ (Tier 2). The "ignore spending" exclusion and watchlists are named there but not operationally detailed.
- Fudget evidence is product-page level (Tier 2); the minimal-pole L0 argument would be strengthened by its support docs, which were not fetched.
- Whether the unallocated-money figure belongs at L0 or L1: held at L1 because Simplifi's auto-generated plan exposes the remaining state without an explicit unassigned pool in fetched evidence. If a mature product without any unassigned figure were confirmed, L1 placement is correct; no counter-evidence found.
- Monarch/Simplifi straddle the PFM boundary by design; if the Personal Finance Management Application document (processed) treats them as PFM-first, the budgeting module reading still holds — flagged as context, not conflict.
- The sample is US-market-heavy (YNAB, Goodbudget, Simplifi, Monarch); Fudget is sold internationally. Regional budgeting methods (kakeibo via Goodbudget's marketing page only) were not researched through native regional products; the historical check covers the analog forms instead.

## Final Synthesis

Canonical Budgeting Application:

```text
L0 (defining invariant)
- Spending plan (period-scoped budget) as the organizing object
- Allocations: planned amounts assigned to purposes within the plan
- Actuals captured in the app (entries or transactions) feeding the comparison
- Comparison state: planned vs actual vs remaining (left to spend / overspent)

L1 (common mature structure)
- Income input anchoring the plan (budgeted ≤ income; income = expenses + savings)
- Unallocated-money figure (Available / left to budget)
- Accounts as optional containers for actuals (on-budget vs off-budget)
- Goals / sinking funds inside the plan
- Recurring & scheduled entries; fixed-vs-flexible spending separation
- Rollover; plan setup assistance from history
- Overspending states; transfer/credit-card-payment special handling
- Non-monthly / project-event budgets; reports; sharing/household; alerts

L2 (variant / optional)
- Budgeting-method philosophy (envelope / zero-based / auto spending plan / flex bucket / minimal list)
- Allocation-container naming (envelope / category / bucket / line)
- Capture posture (manual-first / sync-first / none); plan scope (household vs project)
- PFM bundling; segment (individual/couple/family); surface; local vs cloud

L3 (vendor-specific — Research Notes only)
- YNAB Plan/Months/Category-goal API machinery, on_budget flags, Plaid agency
- Goodbudget Available arithmetic rules, fill modes, Match tool, quick fills, tier limits
- Monarch taxonomy/flex modes/auto-fill/walkthrough specifics
- Simplifi Spending-Plan specifics, sharing, vendor figures
- Fudget tier limits and extras
```

The Application Document will present the L0 as the defining core and L1 as standard capabilities, with a Variants section naming L2 options. L3 stays in Research Notes.
